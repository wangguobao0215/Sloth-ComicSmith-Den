#!/usr/bin/env python3
"""
Storyboard to Prompts Exporter for Sloth-ComicSmith-Den.
Reads storyboard.json and exports image_prompts / video_prompts as CSV and plain text.
Usage: python storyboard_to_prompts.py <project_dir> [--format csv|txt|json]
"""

import sys
import os
import json
import csv
import argparse


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def export_prompts(project_dir, fmt="csv"):
    sb_path = os.path.join(project_dir, "storyboard.json")
    if not os.path.exists(sb_path):
        print(f"Error: storyboard.json not found in {project_dir}")
        sys.exit(1)

    sb = load_json(sb_path)
    scenes = sb.get("scenes", [])

    rows = []
    for scene in scenes:
        scene_id = scene.get("scene_id", "")
        for shot in scene.get("shots", []):
            rows.append({
                "scene_id": scene_id,
                "shot_id": shot.get("shot_id", ""),
                "type": shot.get("type", "image"),
                "model": shot.get("model", ""),
                "function": shot.get("function", ""),
                "framing": shot.get("framing", ""),
                "image_prompt": shot.get("image_prompt", ""),
                "video_prompt": shot.get("video_prompt", ""),
                "seed": shot.get("seed", ""),
                "axis_side": shot.get("axis_side", ""),
            })

    base = os.path.join(project_dir, "prompts_export")
    os.makedirs(base, exist_ok=True)

    if fmt in ("csv", "all"):
        csv_path = os.path.join(base, "prompts.csv")
        with open(csv_path, "w", encoding="utf-8-sig", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=rows[0].keys() if rows else [])
            writer.writeheader()
            writer.writerows(rows)
        print(f"CSV exported: {csv_path}")

    if fmt in ("txt", "all"):
        txt_path = os.path.join(base, "prompts.txt")
        with open(txt_path, "w", encoding="utf-8") as f:
            for r in rows:
                f.write(f"--- [{r['scene_id']}:{r['shot_id']}] {r['type'].upper()} | Model: {r['model']} ---\n")
                if r["image_prompt"]:
                    f.write(f"[IMAGE] {r['image_prompt']}\n")
                if r["video_prompt"]:
                    f.write(f"[VIDEO] {r['video_prompt']}\n")
                f.write(f"Seed: {r['seed']} | Axis: {r['axis_side']} | Framing: {r['framing']} | Function: {r['function']}\n")
                f.write("\n")
        print(f"TXT exported: {txt_path}")

    if fmt in ("json", "all"):
        json_path = os.path.join(base, "prompts.json")
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(rows, f, ensure_ascii=False, indent=2)
        print(f"JSON exported: {json_path}")

    print(f"\nTotal prompts exported: {len(rows)}")


def main():
    parser = argparse.ArgumentParser(description="Export prompts from storyboard")
    parser.add_argument("project_dir", help="Path to project directory")
    parser.add_argument("--format", choices=["csv", "txt", "json", "all"], default="all", help="Export format")
    args = parser.parse_args()
    export_prompts(args.project_dir, args.format)


if __name__ == "__main__":
    main()
