#!/usr/bin/env python3
"""
Auto-generate color_script.json from scenes.json mood fields.
Usage: python generate_color_script.py <project_folder>
"""

import sys
import os
import json

# Mood → color mapping
MOOD_COLOR_MAP = {
    "isolation": {"dominant": "cool_blue_gray", "accent": "pale_silver", "temperature": "cool"},
    "melancholic": {"dominant": "desaturated_blue", "accent": "soft_amber", "temperature": "cool"},
    "weary": {"dominant": "muted_gray", "accent": "dusty_rose", "temperature": "cool"},
    "lonely": {"dominant": "deep_indigo", "accent": "cold_white", "temperature": "cool"},
    "hopeful": {"dominant": "soft_dawn_blue", "accent": "pale_gold", "temperature": "neutral_warm"},
    "conflicted": {"dominant": "muted_teal", "accent": "warm_orange", "temperature": "mixed"},
    "tense": {"dominant": "dark_charcoal", "accent": "electric_yellow", "temperature": "cool"},
    "angry": {"dominant": "deep_crimson", "accent": "burnt_orange", "temperature": "warm"},
    "danger": {"dominant": "blood_red", "accent": "black", "temperature": "warm"},
    "passionate": {"dominant": "rich_magenta", "accent": "deep_purple", "temperature": "warm"},
    "joyful": {"dominant": "bright_sunshine", "accent": "sky_blue", "temperature": "warm"},
    "peaceful": {"dominant": "soft_sage", "accent": "cream", "temperature": "neutral"},
    "nostalgic": {"dominant": "sepia", "accent": "soft_pink", "temperature": "warm"},
    "mysterious": {"dominant": "deep_purple", "accent": "neon_green", "temperature": "cool"},
    "triumphant": {"dominant": "royal_gold", "accent": "deep_crimson", "temperature": "warm"},
    "broken": {"dominant": "ash_gray", "accent": "faded_blue", "temperature": "cool"},
    "acceptance": {"dominant": "soft_dawn_blue", "accent": "pale_yellow", "temperature": "neutral_warm"},
}


def parse_mood(mood_str):
    """Extract mood keywords from a mood string."""
    mood_str = mood_str.lower()
    keywords = []
    for key in MOOD_COLOR_MAP:
        if key in mood_str:
            keywords.append(key)
    # Fallback if no match
    if not keywords:
        keywords = ["melancholic"]
    return keywords


def merge_colors(colors_list):
    """Merge multiple mood colors; use first as dominant, blend accents."""
    if not colors_list:
        return {"dominant": "neutral_gray", "accent": "soft_white", "temperature": "neutral"}
    return colors_list[0]


def generate_color_script(project_folder):
    scenes_path = os.path.join(project_folder, "scenes.json")
    output_path = os.path.join(project_folder, "color_script.json")

    if not os.path.exists(scenes_path):
        print(f"ERROR: scenes.json not found in {project_folder}")
        sys.exit(1)

    with open(scenes_path, "r", encoding="utf-8") as f:
        scenes_data = json.load(f)

    color_arc = []
    for scene in scenes_data.get("scenes", []):
        scene_id = scene.get("scene_id", "")
        mood = scene.get("mood", "")
        keywords = parse_mood(mood)
        colors = [MOOD_COLOR_MAP[k] for k in keywords]
        merged = merge_colors(colors)

        color_arc.append({
            "scene_range": scene_id,
            "dominant_color": merged["dominant"],
            "accent_color": merged["accent"],
            "emotion": mood,
            "temperature": merged["temperature"]
        })

    color_script = {"color_arc": color_arc}

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(color_script, f, ensure_ascii=False, indent=2)

    print(f"Generated color_script.json at {output_path}")
    print(f"Mapped {len(color_arc)} scenes to color directions.")
    print("Review and adjust colors before locking. AI suggestions are starting points, not final art direction.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate_color_script.py <project_folder>")
        sys.exit(1)
    generate_color_script(sys.argv[1])
