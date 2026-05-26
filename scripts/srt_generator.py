#!/usr/bin/env python3
"""
SRT Subtitle Generator v2 for Sloth-ComicSmith-Den.
Reads storyboard.json + audio_plan.json, outputs styled SRT with precise timing.
Supports speaker labels, thought bubbles, and color coding.

Usage:
    python srt_generator.py <project_dir> [--style dialogue|anime|minimal]
"""

import sys
import os
import json
import argparse


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


def generate_srt_v1(project_dir, output_path=None):
    """Legacy v1: Read scenes.json + storyboard.json directly."""
    scenes_path = os.path.join(project_dir, "scenes.json")
    sb_path = os.path.join(project_dir, "storyboard.json")

    scenes_data = load_json(scenes_path) if os.path.exists(scenes_path) else {"scenes": []}
    sb = load_json(sb_path) if os.path.exists(sb_path) else {"shots": []}

    DEFAULT_SHOT_DURATION = 4.0
    entries = []
    global_time = 0.0
    index = 1

    shots = sb.get("shots", [])
    scenes_list = scenes_data.get("scenes", [])

    for shot in shots:
        duration = shot.get("duration", DEFAULT_SHOT_DURATION)
        shot_id = shot.get("shot_id", "")
        scene_id = shot.get("scene_id", "")

        # Find matching scene for dialogue
        scene_meta = None
        for sm in scenes_list:
            if sm.get("scene_id") == scene_id:
                scene_meta = sm
                break

        if scene_meta and "dialogue" in scene_meta:
            for dlg in scene_meta["dialogue"]:
                dlg_type = dlg.get("type", "spoken")
                line = dlg.get("line", "")
                speaker = dlg.get("speaker", "")

                if not line:
                    continue

                # Estimate timing: spoken lines start 0.5s after shot, thoughts span the shot
                if dlg_type == "spoken":
                    start = global_time + 0.5
                    end = min(global_time + duration - 0.5, start + len(line) * 0.25)
                    text = f"{speaker}：{line}" if speaker else line
                    style = "dialogue"
                elif dlg_type == "thought":
                    start = global_time + 0.5
                    end = global_time + duration - 0.5
                    text = f"（{speaker} 内心）{line}" if speaker else f"（内心）{line}"
                    style = "thought"
                elif dlg_type == "narration":
                    start = global_time
                    end = global_time + duration
                    text = f"【{line}】"
                    style = "narration"
                else:
                    continue

                entries.append({
                    "index": index,
                    "start": sec_to_srt(start),
                    "end": sec_to_srt(end),
                    "text": text,
                    "style": style,
                    "shot_id": shot_id,
                })
                index += 1

        global_time += duration

    return entries, global_time


def generate_srt_v2(project_dir, output_path=None):
    """v2: Read audio_plan.json for precise timing from voice cues."""
    audio_plan_path = os.path.join(project_dir, "audio_plan.json")

    if not os.path.exists(audio_plan_path):
        print("[INFO] audio_plan.json not found, falling back to v1 (estimated timing)")
        return generate_srt_v1(project_dir, output_path)

    audio_plan = load_json(audio_plan_path)
    subtitle_entries = audio_plan.get("subtitle_entries", [])

    entries = []
    for i, sub in enumerate(subtitle_entries):
        entries.append({
            "index": i + 1,
            "start": sec_to_srt(sub["start"]),
            "end": sec_to_srt(sub["end"]),
            "text": sub["text"],
            "style": sub.get("style", "dialogue_white"),
            "speaker": sub.get("speaker", ""),
            "shot_id": sub.get("shot_id", ""),
        })

    total_duration = audio_plan.get("total_duration", 0)
    return entries, total_duration


def write_srt(entries, output_path, style_mode="anime"):
    """Write SRT file with optional style overrides."""
    style_overrides = {
        "anime": {
            "dialogue_white": {"FontName": "Arial", "FontSize": 24, "PrimaryColour": "&H00FFFFFF", "OutlineColour": "&H00000000", "Outline": 2, "Alignment": 2},
            "thought_italic": {"FontName": "Arial", "FontSize": 22, "PrimaryColour": "&H00E0E0E0", "OutlineColour": "&H00000000", "Outline": 2, "Alignment": 2, "Italic": 1},
        },
        "dialogue": {
            "dialogue_white": {"FontName": "Arial", "FontSize": 28, "PrimaryColour": "&H00FFFFFF", "OutlineColour": "&H00000000", "Outline": 2, "Alignment": 2},
            "thought_italic": {"FontName": "Arial", "FontSize": 26, "PrimaryColour": "&H00CCCCCC", "OutlineColour": "&H00000000", "Outline": 2, "Alignment": 2, "Italic": 1},
        },
        "minimal": {
            "dialogue_white": {"FontName": "Helvetica", "FontSize": 20, "PrimaryColour": "&H00FFFFFF", "OutlineColour": "&H00000000", "Outline": 1, "Alignment": 2},
            "thought_italic": {"FontName": "Helvetica", "FontSize": 18, "PrimaryColour": "&H00DDDDDD", "OutlineColour": "&H00000000", "Outline": 1, "Alignment": 2, "Italic": 1},
        }
    }

    styles = style_overrides.get(style_mode, style_overrides["anime"])

    with open(output_path, "w", encoding="utf-8") as f:
        for e in entries:
            f.write(f"{e['index']}\n")

            # Build style override string for FFmpeg
            style = e.get("style", "dialogue_white")
            style_config = styles.get(style, styles["dialogue_white"])
            style_str = ",".join(f"{k}={v}" for k, v in style_config.items())

            f.write(f"{e['start']} --> {e['end']}\n")
            f.write(f"{e['text']}\n\n")

    # Also write an ASS version with full styling for advanced use
    ass_path = output_path.replace(".srt", ".ass")
    write_ass(entries, ass_path, styles)

    print(f"Generated {len(entries)} subtitle entries → {output_path}")
    if os.path.exists(ass_path):
        print(f"Styled ASS version → {ass_path}")


def write_ass(entries, ass_path, styles):
    """Write ASS subtitle file with full style support."""
    header = """[Script Info]
Title: Sloth-ComicSmith-Den Auto-Generated Subtitles
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
"""

    style_lines = []
    for name, cfg in styles.items():
        fontname = cfg.get("FontName", "Arial")
        fontsize = cfg.get("FontSize", 24)
        primary = cfg.get("PrimaryColour", "&H00FFFFFF")
        outline_c = cfg.get("OutlineColour", "&H00000000")
        outline = cfg.get("Outline", 2)
        italic = 1 if cfg.get("Italic", 0) else 0
        alignment = cfg.get("Alignment", 2)
        style_lines.append(
            f"Style: {name},{fontname},{fontsize},{primary},&H000000FF,{outline_c},&H00000000,0,{italic},0,0,100,100,0,0,1,{outline},0,{alignment},10,10,30,1"
        )

    events_header = """
[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""

    with open(ass_path, "w", encoding="utf-8") as f:
        f.write(header)
        for line in style_lines:
            f.write(line + "\n")
        f.write(events_header)
        for e in entries:
            style = e.get("style", "dialogue_white")
            speaker = e.get("speaker", "")
            name_field = speaker if speaker else "Unknown"
            text = e["text"].replace("\n", "\\N")
            f.write(f"Dialogue: 0,{e['start'].replace(',', '.')},{e['end'].replace(',', '.')},{style},{name_field},0,0,0,,{text}\n")


def main():
    parser = argparse.ArgumentParser(description="Generate SRT/ASS subtitles from project")
    parser.add_argument("project_dir", help="Path to project directory")
    parser.add_argument("--output", help="Output SRT file path", default=None)
    parser.add_argument("--style", choices=["anime", "dialogue", "minimal"], default="anime",
                        help="Subtitle style preset")
    args = parser.parse_args()

    # Try v2 first (precise timing from audio_plan), fallback to v1
    entries, total_duration = generate_srt_v2(args.project_dir, args.output)

    if not entries:
        print("[WARN] No subtitle entries generated")
        return

    output_path = args.output or os.path.join(args.project_dir, "subtitles.srt")
    write_srt(entries, output_path, args.style)
    print(f"Total duration: {sec_to_srt(total_duration)}")


if __name__ == "__main__":
    main()
