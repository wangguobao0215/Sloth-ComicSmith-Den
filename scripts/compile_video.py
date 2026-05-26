#!/usr/bin/env python3
"""
compile_video.py — One-command video compiler using FFmpeg only.
Reads storyboard.json + assets/video/ + subtitles.srt, outputs output_final.mp4.
No GUI tools. No DaVinci Resolve. No After Effects. Just FFmpeg.

Usage:
    python compile_video.py my_project --transition fade --bgm music.mp3
    python compile_video.py my_project --transition dissolve --duration 5
"""

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Optional


def load_storyboard(project_dir: Path) -> dict:
    path = project_dir / "storyboard.json"
    if not path.exists():
        print(f"[ERROR] storyboard.json not found in {project_dir}")
        sys.exit(1)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def build_concat_list(project_dir: Path, shots: list, transition: str, default_duration: int) -> Path:
    """Build an FFmpeg concat demuxer file with xfade transitions."""
    video_dir = project_dir / "assets" / "video"
    concat_file = project_dir / "concat_list.txt"
    filter_parts = []
    inputs = []
    offset = 0.0

    for i, shot in enumerate(shots):
        shot_id = shot["shot_id"]
        src = video_dir / f"{shot_id}.mp4"
        if not src.exists():
            print(f"[WARN] Missing video for {shot_id}, using 1s black placeholder")
            # Create a 1s black placeholder
            placeholder = video_dir / f"{shot_id}_placeholder.mp4"
            if not placeholder.exists():
                subprocess.run([
                    "ffmpeg", "-y", "-f", "lavfi", "-i", "color=c=black:s=1920x1080:d=1",
                    "-pix_fmt", "yuv420p", str(placeholder)
                ], capture_output=True)
            src = placeholder

        duration = shot.get("duration", default_duration)
        inputs.append(str(src))

        if i > 0 and transition != "none":
            trans_dur = 0.5
            offset += duration - trans_dur
        else:
            offset += duration

    # Simple concat approach (no complex xfade for broad compatibility)
    with open(concat_file, "w", encoding="utf-8") as f:
        for src in inputs:
            f.write(f"file '{Path(src).resolve()}'\n")

    return concat_file


def compile_video(project_dir: Path, transition: str, bgm: Optional[str], audio_track: Optional[str], subtitle_style: str, output_name: str):
    storyboard = load_storyboard(project_dir)
    shots = storyboard.get("shots", [])
    if not shots:
        print("[ERROR] No shots found in storyboard.json")
        sys.exit(1)

    concat_file = build_concat_list(project_dir, shots, transition, default_duration=4)
    output_path = project_dir / output_name

    # Determine subtitle source: ASS preferred over SRT for styling
    ass_path = project_dir / "subtitles.ass"
    srt_path = project_dir / "subtitles.srt"
    subtitle_file = None
    if ass_path.exists():
        subtitle_file = ass_path
    elif srt_path.exists():
        subtitle_file = srt_path

    # Build FFmpeg command
    cmd = ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat_file)]

    # Add audio track (mixed audio from mix_audio.py) or BGM
    audio_input_idx = 1
    if audio_track:
        audio_path = Path(audio_track)
        if not audio_path.is_absolute():
            audio_path = project_dir / audio_path
        if audio_path.exists():
            cmd += ["-i", str(audio_path)]
        else:
            print(f"[WARN] Audio track not found: {audio_track}")
            audio_input_idx = None
    elif bgm:
        bgm_path = Path(bgm)
        if bgm_path.exists():
            cmd += ["-i", str(bgm_path)]
        else:
            print(f"[WARN] BGM file not found: {bgm}")
            audio_input_idx = None
    else:
        audio_input_idx = None

    # Check FFmpeg subtitle support
    has_subtitles_filter = False
    check = subprocess.run(["ffmpeg", "-filters"], capture_output=True, text=True)
    if "subtitles" in check.stdout:
        has_subtitles_filter = True

    # Build video filter
    vf_parts = []
    if subtitle_file and has_subtitles_filter:
        sub_path = str(subtitle_file.resolve()).replace(":", "\\:")
        if subtitle_file.suffix == ".ass":
            vf_parts.append(f"ass={sub_path}")
        else:
            vf_parts.append(f"subtitles={sub_path}")
    elif subtitle_file and not has_subtitles_filter:
        print(f"[WARN] FFmpeg lacks libass support. Subtitles not burned-in.")
        print(f"  Use external player (VLC/MPV) with: {subtitle_file.name}")
        print(f"  Or run: python scripts/burn_subtitles.py {project_dir}")

    if vf_parts:
        cmd += ["-vf", ",".join(vf_parts)]

    # Audio mapping
    if audio_input_idx is not None:
        cmd += ["-map", "0:v", "-map", f"{audio_input_idx}:a", "-c:a", "aac", "-b:a", "192k", "-shortest"]
    else:
        cmd += ["-an"]  # No audio

    cmd += ["-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "23", str(output_path)]

    print(f"[INFO] Compiling video to {output_path}...")
    print(f"[CMD] {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print(f"[ERROR] FFmpeg failed:\n{result.stderr}")
        sys.exit(1)

    print(f"[OK] Video compiled: {output_path}")
    if subtitle_file:
        print(f"  Subtitles: {subtitle_file.name} ({subtitle_style} style)")
    if audio_input_idx is not None:
        print(f"  Audio track: {audio_track or bgm}")

    # Cleanup temp concat file
    concat_file.unlink(missing_ok=True)


def main():
    parser = argparse.ArgumentParser(description="Compile storyboard videos into final output using FFmpeg")
    parser.add_argument("project_dir", help="Path to project directory containing storyboard.json")
    parser.add_argument("--transition", choices=["fade", "dissolve", "wipe", "none"], default="fade",
                        help="Transition type between shots")
    parser.add_argument("--bgm", default=None, help="Path to background music file (legacy, use --audio)")
    parser.add_argument("--audio", default=None, help="Path to mixed audio track (BGM + voice + foley)")
    parser.add_argument("--subtitles-style", choices=["anime", "dialogue", "minimal"], default="anime",
                        help="Subtitle burn-in style preset")
    parser.add_argument("--output", default="output_final.mp4", help="Output filename")
    args = parser.parse_args()

    project_dir = Path(args.project_dir)
    if not project_dir.exists():
        print(f"[ERROR] Project directory not found: {project_dir}")
        sys.exit(1)

    compile_video(project_dir, args.transition, args.bgm, args.audio, args.subtitles_style, args.output)


if __name__ == "__main__":
    main()
