#!/usr/bin/env python3
"""
Check 180-degree axis consistency in storyboard.json.
Flags unintentional axis jumps within scenes.
Usage: python check_axis.py <project_folder>
"""

import sys
import os
import json
from collections import defaultdict


def check_axis(project_folder):
    storyboard_path = os.path.join(project_folder, "storyboard.json")

    if not os.path.exists(storyboard_path):
        print(f"ERROR: storyboard.json not found in {project_folder}")
        sys.exit(1)

    with open(storyboard_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Group shots by scene
    scenes = defaultdict(list)
    for shot in data.get("shots", []):
        scenes[shot.get("scene_id", "")].append(shot)

    warnings = []
    for scene_id, shots in scenes.items():
        if not scene_id:
            continue

        # Filter non-transition shots with axis_side
        axis_shots = [s for s in shots if s.get("function") != "transition" and "axis_side" in s]
        if len(axis_shots) < 2:
            continue

        sides = [s["axis_side"] for s in axis_shots]
        # Count left vs right
        left_count = sides.count("left")
        right_count = sides.count("right")
        neutral_count = sides.count("neutral")

        # Determine dominant side (ignore neutral for dominance)
        if left_count > 0 and right_count > 0:
            # Check if axis jump is intentional
            dominant = "left" if left_count >= right_count else "right"
            minority = "right" if dominant == "left" else "left"
            minority_shots = [s["shot_id"] for s in axis_shots if s["axis_side"] == minority]
            warnings.append({
                "scene": scene_id,
                "type": "axis_jump",
                "dominant_side": dominant,
                "minority_side": minority,
                "minority_shots": minority_shots,
                "message": f"Scene {scene_id}: {len(minority_shots)} shot(s) on '{minority}' side while majority is '{dominant}'. "
                           f"If intentional (confusion/power shift/emotional rupture), add a note. "
                           f"If unintentional, flip axis_side to '{dominant}'."
            })

    print(f"Axis Check Report for {project_folder}")
    print(f"Total scenes checked: {len(scenes)}")
    print(f"Axis warnings: {len(warnings)}\n")

    if warnings:
        for w in warnings:
            print(f"[WARNING] {w['message']}")
            print(f"  Affected shots: {', '.join(w['minority_shots'])}")
            print()
    else:
        print("All scenes maintain consistent axis. No warnings.")

    # Save report
    report_path = os.path.join(project_folder, "axis_check_report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump({"warnings": warnings, "total_scenes": len(scenes)}, f, ensure_ascii=False, indent=2)
    print(f"Report saved to {report_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python check_axis.py <project_folder>")
        sys.exit(1)
    check_axis(sys.argv[1])
