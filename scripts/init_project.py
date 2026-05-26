#!/usr/bin/env python3
"""
Initialize a Sloth-ComicSmith-Den v2.1 project folder with the required structure.
Usage: python init_project.py <project_name>
"""

import sys
import os
import json


def init_project(name):
    base = os.path.join(os.getcwd(), name)
    dirs = [
        os.path.join(base, "assets", "images"),
        os.path.join(base, "assets", "video"),
        os.path.join(base, "assets", "comic-pages"),
        os.path.join(base, "references", "mood_board"),
        os.path.join(base, "references", "style_board"),
        os.path.join(base, "references", "animatic"),
    ]
    for d in dirs:
        os.makedirs(d, exist_ok=True)

    # scenes.json v2.1 template
    scenes = {
        "title": name,
        "language": "zh",
        "total_scenes": 0,
        "dramatic_structure": {
            "inciting_incident": None,
            "midpoint": None,
            "climax": None,
            "all_is_lost": None
        },
        "scenes": []
    }
    with open(os.path.join(base, "scenes.json"), "w", encoding="utf-8") as f:
        json.dump(scenes, f, ensure_ascii=False, indent=2)

    # characters.json v2.1 template
    characters = {
        "visual_style_anchor": "",
        "visual_style_preset": "",
        "characters": []
    }
    with open(os.path.join(base, "characters.json"), "w", encoding="utf-8") as f:
        json.dump(characters, f, ensure_ascii=False, indent=2)

    # environments.json v2.1 template
    environments = {
        "environments": []
    }
    with open(os.path.join(base, "environments.json"), "w", encoding="utf-8") as f:
        json.dump(environments, f, ensure_ascii=False, indent=2)

    # color_script.json v2.1 template
    color_script = {
        "cultural_context": "western",
        "color_arc": []
    }
    with open(os.path.join(base, "color_script.json"), "w", encoding="utf-8") as f:
        json.dump(color_script, f, ensure_ascii=False, indent=2)

    # storyboard.json v2.1 template
    storyboard = {
        "total_shots": 0,
        "shots": []
    }
    with open(os.path.join(base, "storyboard.json"), "w", encoding="utf-8") as f:
        json.dump(storyboard, f, ensure_ascii=False, indent=2)

    # comic_pages.json v2.1 template
    comic_pages = {
        "total_pages": 0,
        "pages": []
    }
    with open(os.path.join(base, "comic_pages.json"), "w", encoding="utf-8") as f:
        json.dump(comic_pages, f, ensure_ascii=False, indent=2)

    # generation_log.json v2.1 template
    log = {
        "project": name,
        "generated_at": "",
        "image_model": "",
        "video_model": "",
        "batch_size": 5,
        "images": [],
        "videos": []
    }
    with open(os.path.join(base, "generation_log.json"), "w", encoding="utf-8") as f:
        json.dump(log, f, ensure_ascii=False, indent=2)

    # failed_shots.json v2.1 template
    failed = {
        "failed_at": "",
        "failed_images": [],
        "failed_videos": []
    }
    with open(os.path.join(base, "failed_shots.json"), "w", encoding="utf-8") as f:
        json.dump(failed, f, ensure_ascii=False, indent=2)

    # post_production_plan.json v2.1 template
    ppp = {
        "stages": [
            {"stage": "concat", "tool": "ffmpeg", "status": "pending"},
            {"stage": "color_grade", "tool": "davinci_resolve", "reference_shot": "", "status": "pending"},
            {"stage": "stabilize", "tool": "after_effects", "shots": [], "status": "pending"},
            {"stage": "face_repair", "tool": "facefusion", "shots": [], "status": "pending"},
            {"stage": "flicker_fix", "tool": "davinci_resolve", "status": "pending"},
            {"stage": "subtitle_burn", "tool": "ffmpeg", "status": "pending"},
            {"stage": "bgm_mix", "tool": "audition", "status": "pending"}
        ]
    }
    with open(os.path.join(base, "post_production_plan.json"), "w", encoding="utf-8") as f:
        json.dump(ppp, f, ensure_ascii=False, indent=2)

    # references/ref_index.json v2.1 template
    ref_index = {
        "boards": []
    }
    with open(os.path.join(base, "references", "ref_index.json"), "w", encoding="utf-8") as f:
        json.dump(ref_index, f, ensure_ascii=False, indent=2)

    # Markdown files
    for fname in ["raw_script.md", "character_prompts.md", "shot_list.md"]:
        with open(os.path.join(base, fname), "w", encoding="utf-8") as f:
            f.write(f"# {fname.replace('_', ' ').title()}\n\n")

    print(f"Project '{name}' initialized at {base}")
    print("v2.1 structure includes: scenes.json, characters.json, environments.json,")
    print("color_script.json, storyboard.json, comic_pages.json,")
    print("generation_log.json, failed_shots.json, post_production_plan.json,")
    print("references/ref_index.json")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python init_project.py <project_name>")
        sys.exit(1)
    init_project(sys.argv[1])
