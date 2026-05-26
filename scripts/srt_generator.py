#!/usr/bin/env python3
"""
SRT Subtitle Generator for Sloth-ComicSmith-Den.
Reads scenes.json + storyboard.json, outputs subtitles in SRT format.
Usage: python srt_generator.py <project_dir> [--output srt_path]
"""

import sys
import os
import json
import argparse
import re


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def sec_to_srt(t):
    """Convert seconds to SRT timestamp HH:MM:SS,mmm"""
    hours = int(t // 3600)
    minutes = int((t % 3600) // 60)
    seconds = int(t % 60)
    millis = int(round((t % 1) * 1000))
    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{millis:03d}"


def generate_srt(project_dir, output_path=None):
    scenes_path = os.path.join(project_dir, "scenes.json")
    sb_path = os.path.join(project_dir, "storyboard.json")

    if not os.path.exists(scenes_path):
        print(f"Error: scenes.json not found in {project_dir}")
        sys.exit(1)
    if not os.path.exists(sb_path):
        print(f"Error: storyboard.json not found in {project_dir}")
        sys.exit(1)

    scenes_data = load_json(scenes_path)
    sb = load_json(sb_path)

    # Default duration per scene if not specified
    DEFAULT_SCENE_DURATION = 5.0  # seconds per scene as base
    DEFAULT_SHOT_DURATION = 3.0   # seconds per shot

    entries = []
    global_time = 0.0
    index = 1

    scenes = sb.get("scenes", [])
    for sidx, scene in enumerate(scenes):
        scene_id = scene.get("scene_id", sidx + 1)
        # Find matching scene metadata for dialogue
        scene_meta = None
        for sm in scenes_data.get("scenes", []):
            if sm.get("scene_id") == scene_id:
                scene_meta = sm
                break

        shots = scene.get("shots", [])
        for shot in shots:
            duration = shot.get("duration", DEFAULT_SHOT_DURATION)
            shot_id = shot.get("shot_id", "")

            # Collect spoken dialogue only (skip narration/thought unless --all)
            lines = []
            if scene_meta and "dialogue" in scene_meta:
                for dlg in scene_meta["dialogue"]:
                    if dlg.get("type", "spoken") == "spoken" and dlg.get("text"):
                        speaker = dlg.get("speaker", "")
                        text = dlg["text"]
                        lines.append(f"{speaker}: {text}" if speaker else text)

            # Also check shot-level dialogue override
            if shot.get("dialogue"):
                for dlg in shot["dialogue"]:
                    if dlg.get("type", "spoken") == "spoken" and dlg.get("text"):
                        speaker = dlg.get("speaker", "")
                        text = dlg["text"]
                        lines.append(f"{speaker}: {text}" if speaker else text)

            if lines:
                start = global_time
                end = global_time + duration
                text = "\\n".join(lines)
                entries.append({
                    "index": index,
                    "start": sec_to_srt(start),
                    "end": sec_to_srt(end),
                    "text": text,
                    "shot_id": shot_id,
                })
                index += 1

            global_time += duration

    if not output_path:
        output_path = os.path.join(project_dir, "output.srt")

    with open(output_path, "w", encoding="utf-8") as f:
        for e in entries:
            f.write(f"{e['index']}\n")
            f.write(f"{e['start']} --> {e['end']}\n")
            f.write(f"{e['text']}\n\n")

    print(f"Generated {len(entries)} subtitle entries → {output_path}")
    print(f"Total duration: {sec_to_srt(global_time)}")


def main():
    parser = argparse.ArgumentParser(description="Generate SRT subtitles from project JSONs")
    parser.add_argument("project_dir", help="Path to project directory")
    parser.add_argument("--output", help="Output SRT file path", default=None)
    args = parser.parse_args()
    generate_srt(args.project_dir, args.output)


if __name__ == "__main__":
    main()
