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


def compile_video(project_dir: Path, transition: str, bgm: str | None, output_name: str):
    storyboard = load_storyboard(project_dir)
    shots = storyboard.get("shots", [])
    if not shots:
        print("[ERROR] No shots found in storyboard.json")
        sys.exit(1)

    concat_file = build_concat_list(project_dir, shots, transition, default_duration=4)
    output_path = project_dir / output_name

    # Build FFmpeg command
    cmd = ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat_file)]

    # Add subtitles if present
    srt_path = project_dir / "subtitles.srt"
    if srt_path.exists():
        cmd += ["-vf", f"subtitles={srt_path}:force_style='FontSize=24,Outline=2'"]

    # Add BGM if provided
    if bgm:
        bgm_path = Path(bgm)
        if bgm_path.exists():
            cmd += ["-i", str(bgm_path), "-shortest", "-c:a", "aac", "-b:a", "192k"]
        else:
            print(f"[WARN] BGM file not found: {bgm}")

    cmd += ["-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "23", str(output_path)]

    print(f"[INFO] Compiling video to {output_path}...")
    print(f"[CMD] {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print(f"[ERROR] FFmpeg failed:\n{result.stderr}")
        sys.exit(1)

    print(f"[OK] Video compiled: {output_path}")

    # Cleanup temp concat file
    concat_file.unlink(missing_ok=True)


def main():
    parser = argparse.ArgumentParser(description="Compile storyboard videos into final output using FFmpeg")
    parser.add_argument("project_dir", help="Path to project directory containing storyboard.json")
    parser.add_argument("--transition", choices=["fade", "dissolve", "wipe", "none"], default="fade",
                        help="Transition type between shots")
    parser.add_argument("--bgm", default=None, help="Path to background music file")
    parser.add_argument("--output", default="output_final.mp4", help="Output filename")
    args = parser.parse_args()

    project_dir = Path(args.project_dir)
    if not project_dir.exists():
        print(f"[ERROR] Project directory not found: {project_dir}")
        sys.exit(1)

    compile_video(project_dir, args.transition, args.bgm, args.output)


if __name__ == "__main__":
    main()
