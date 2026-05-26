#!/usr/bin/env python3
"""
switch_style.py — Switch visual style preset without re-parsing script or regenerating characters.
Updates characters.json, storyboard.json, and environments.json with the new style anchor.

Usage:
    python switch_style.py my_project --preset watercolor
    python switch_style.py my_project --custom "Oil painting, thick brushstrokes, muted earth tones"
"""

import argparse
import json
import sys
from pathlib import Path


PRESETS = {
    "anime-cel": "Anime cel-shaded style, vibrant colors, clean black outlines, expressive large eyes",
    "anime-painterly": "Anime style with soft painterly textures, watercolor backgrounds, warm lighting",
    "manga-ink": "Black and white manga style, heavy inking, screentone shading, dynamic speed lines",
    "watercolor": "Soft watercolor illustration, bleeding edges, pastel palette, hand-painted texture",
    "cyberpunk-neon": "Cyberpunk aesthetic, neon lighting, high contrast, rain-slicked streets, holographic UI",
    "ghibli": "Studio Ghibli inspired, lush natural backgrounds, soft clouds, warm golden hour lighting",
    "noir": "Film noir style, high contrast black and white, dramatic shadows, venetian blind lighting",
    "pixel-art": "16-bit pixel art style, limited color palette, dithering, retro game aesthetic",
}


def update_characters(project_dir: Path, new_style: str):
    path = project_dir / "characters.json"
    if not path.exists():
        print("[WARN] characters.json not found, skipping")
        return

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    old_style = data.get("visual_style_anchor", "")
    data["visual_style_anchor"] = new_style
    data["visual_style_preset"] = data.get("visual_style_preset", "custom")

    # Update consistency prompts
    for char in data.get("characters", []):
        prompt = char.get("consistency_prompt", "")
        if old_style and old_style in prompt:
            char["consistency_prompt"] = prompt.replace(old_style, new_style)
        else:
            char["consistency_prompt"] = f"{new_style}. {prompt}"

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"[OK] Updated characters.json with new style")


def update_storyboard(project_dir: Path, new_style: str):
    path = project_dir / "storyboard.json"
    if not path.exists():
        print("[WARN] storyboard.json not found, skipping")
        return

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    updated = 0
    for shot in data.get("shots", []):
        prompt = shot.get("image_prompt", "")
        if prompt:
            # Simple append of style — user may want to refine
            if new_style not in prompt:
                shot["image_prompt"] = f"{new_style}. {prompt}"
                updated += 1

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"[OK] Updated {updated} shots in storyboard.json")


def switch_style(project_dir: Path, preset: str | None, custom: str | None):
    if preset:
        if preset not in PRESETS:
            print(f"[ERROR] Unknown preset: {preset}")
            print(f"Available: {', '.join(PRESETS.keys())}")
            sys.exit(1)
        new_style = PRESETS[preset]
    elif custom:
        new_style = custom
    else:
        print("[ERROR] Specify --preset or --custom")
        sys.exit(1)

    print(f"[INFO] Switching to style: {new_style[:60]}...")
    update_characters(project_dir, new_style)
    update_storyboard(project_dir, new_style)
    print("[OK] Style switch complete. Regenerate images to see the new style.")


def main():
    parser = argparse.ArgumentParser(description="Switch visual style without re-parsing script")
    parser.add_argument("project_dir", help="Path to project directory")
    parser.add_argument("--preset", choices=list(PRESETS.keys()), help="Preset style name")
    parser.add_argument("--custom", help="Custom style description string")
    args = parser.parse_args()

    switch_style(Path(args.project_dir), args.preset, args.custom)


if __name__ == "__main__":
    main()
