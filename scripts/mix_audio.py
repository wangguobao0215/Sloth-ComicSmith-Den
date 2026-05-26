#!/usr/bin/env python3
"""
mix_audio.py — Mix BGM + voice clips + foley/ambience into a single audio track.
Uses FFmpeg for all audio processing. No DAW required.

Usage:
    python mix_audio.py my_project --bgm assets/audio/bgm/rainy_night.mp3
    python mix_audio.py my_project --auto-bgm  # auto-select BGM per audio_plan.json
"""

import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path


def load_audio_plan(project_dir: Path) -> dict:
    path = project_dir / "audio_plan.json"
    if not path.exists():
        print("[ERROR] audio_plan.json not found. Run generate_audio_plan.py first.")
        sys.exit(1)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def create_silence(duration: float, output_path: Path):
    """Create a silent audio track of given duration."""
    subprocess.run([
        "ffmpeg", "-y", "-f", "lavfi", "-i", f"anullsrc=r=48000:cl=stereo",
        "-t", str(duration), "-acodec", "libmp3lame", "-q:a", "4", str(output_path)
    ], capture_output=True)


def overlay_clips(base_audio: Path, clips: list, output_path: Path):
    """Overlay multiple audio clips onto a base track at specified timestamps."""
    if not clips:
        # Just copy base
        subprocess.run(["cp", str(base_audio), str(output_path)], capture_output=True)
        return
    
    # Build FFmpeg complex filter
    inputs = ["-i", str(base_audio)]
    filter_parts = ["[0:a]aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo[base]"]
    
    current = "base"
    for i, clip in enumerate(clips):
        idx = i + 1
        inputs += ["-i", str(clip["file"])]
        
        # Pad with silence to correct position, then mix
        delay_ms = int(clip["timestamp"] * 1000)
        volume = clip.get("volume", 1.0)
        
        filter_parts.append(
            f"[{idx}:a]adelay={delay_ms}|{delay_ms},volume={volume}[clip{idx}]"
        )
    
    # Build amix filter
    mix_inputs = "[base]" + "".join(f"[clip{i+1}]" for i in range(len(clips)))
    filter_parts.append(f"{mix_inputs}amix=inputs={len(clips)+1}:duration=first:dropout_transition=2[aout]")
    
    full_filter = ";".join(filter_parts)
    
    cmd = ["ffmpeg", "-y"] + inputs + ["-filter_complex", full_filter, "-map", "[aout]",
           "-acodec", "libmp3lame", "-q:a", "2", str(output_path)]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"[WARN] Audio mix warning: {result.stderr[:200]}")


def mix_audio(project_dir: Path, bgm_path: Path = None, auto_bgm: bool = False):
    audio_plan = load_audio_plan(project_dir)
    total_duration = audio_plan.get("total_duration", 60)
    
    audio_dir = project_dir / "assets" / "audio"
    audio_dir.mkdir(parents=True, exist_ok=True)
    
    # Step 1: Create base silence track
    base_silence = audio_dir / "_base_silence.mp3"
    create_silence(total_duration + 2, base_silence)
    
    # Step 2: Handle BGM
    bgm_layer = audio_dir / "_bgm_layer.mp3"
    
    if bgm_path and bgm_path.exists():
        # Use provided BGM, loop/truncate to match duration
        subprocess.run([
            "ffmpeg", "-y", "-i", str(bgm_path), "-filter_complex",
            f"[0:a]aloop=loop=-1:size=2e+09,atrim=0:{total_duration + 2},afade=t=out:st={total_duration}:d=2[aout]",
            "-map", "[aout]", "-acodec", "libmp3lame", "-q:a", "2", str(bgm_layer)
        ], capture_output=True)
        print(f"[OK] BGM layer created from {bgm_path}")
    elif auto_bgm:
        # Create placeholder with prompts for each segment
        bgm_cues = audio_plan.get("bgm_cues", [])
        print(f"[INFO] Auto-BGM mode: {len(bgm_cues)} segments need music")
        for cue in bgm_cues:
            print(f"  [{cue['start_time']:.1f}s - {cue['end_time']:.1f}s] {cue['generation_prompt']}")
        print(f"  [TIP] Use Suno/Udio with above prompts, then re-run with --bgm <file>")
        # Use silence as placeholder
        bgm_layer = base_silence
    else:
        bgm_layer = base_silence
        print("[INFO] No BGM provided. Output will be voice + foley only.")
    
    # Step 3: Collect voice clips
    voice_clips = []
    voice_dir = project_dir / "assets" / "audio" / "voice"
    for cue in audio_plan.get("voice_cues", []):
        clip_file = project_dir / cue["output_file"]
        if clip_file.exists():
            voice_clips.append({
                "file": clip_file,
                "timestamp": cue["timestamp"],
                "volume": 1.0
            })
        else:
            print(f"[WARN] Voice clip missing: {clip_file}")
    
    # Step 4: Collect foley clips
    foley_clips = []
    foley_dir = project_dir / "assets" / "audio" / "foley"
    for cue in audio_plan.get("foley_cues", []):
        clip_file = Path(cue["suggested_file"])
        if not clip_file.is_absolute():
            clip_file = project_dir / clip_file
        if clip_file.exists():
            foley_clips.append({
                "file": clip_file,
                "timestamp": cue["timestamp"],
                "volume": 0.6 if cue.get("type") == "ambience" else 0.8
            })
    
    # Step 5: Mix voice onto BGM
    voice_mix = audio_dir / "_voice_mix.mp3"
    all_clips = voice_clips + foley_clips
    overlay_clips(bgm_layer, all_clips, voice_mix)
    
    # Step 6: Final output
    final_output = project_dir / "assets" / "audio" / "mixed_audio.mp3"
    subprocess.run(["cp", str(voice_mix), str(final_output)], capture_output=True)
    
    print(f"\n[OK] Mixed audio saved: {final_output}")
    print(f"  Duration: {total_duration:.1f}s")
    print(f"  Voice clips: {len(voice_clips)}")
    print(f"  Foley clips: {len(foley_clips)}")
    print(f"\n  Use with: compile_video.py {project_dir} --audio {final_output}")
    
    # Cleanup temp files
    base_silence.unlink(missing_ok=True)
    voice_mix.unlink(missing_ok=True)
    if bgm_layer != base_silence:
        bgm_layer.unlink(missing_ok=True)


def main():
    parser = argparse.ArgumentParser(description="Mix audio layers into final track")
    parser.add_argument("project_dir", help="Path to project directory")
    parser.add_argument("--bgm", help="Path to background music file", default=None)
    parser.add_argument("--auto-bgm", action="store_true", help="Show BGM prompts from audio_plan.json")
    args = parser.parse_args()
    
    bgm_path = Path(args.bgm) if args.bgm else None
    mix_audio(Path(args.project_dir), bgm_path, args.auto_bgm)


if __name__ == "__main__":
    main()
