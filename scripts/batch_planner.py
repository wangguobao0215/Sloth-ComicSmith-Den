#!/usr/bin/env python3
"""
Batch Planner for Sloth-ComicSmith-Den.
Splits generation workload into API-friendly batches based on rate limits.
Usage: python batch_planner.py <project_dir> [--rpm N] [--rpd N] [--max-concurrent N]
"""

import sys
import os
import json
import argparse
import math

# Default rate limits (can be overridden)
DEFAULT_LIMITS = {
    "midjourney": {"rpm": 1, "rpd": 200, "max_concurrent": 1, "cooldown_sec": 60},
    "dalle3": {"rpm": 5, "rpd": 50, "max_concurrent": 2, "cooldown_sec": 12},
    "sd_api": {"rpm": 10, "rpd": 1000, "max_concurrent": 4, "cooldown_sec": 6},
    "kling": {"rpm": 2, "rpd": 100, "max_concurrent": 1, "cooldown_sec": 30},
    "runway": {"rpm": 3, "rpd": 150, "max_concurrent": 2, "cooldown_sec": 20},
    "pika": {"rpm": 3, "rpd": 150, "max_concurrent": 2, "cooldown_sec": 20},
    "veo": {"rpm": 2, "rpd": 100, "max_concurrent": 1, "cooldown_sec": 30},
}


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def plan_batches(project_dir, override_rpm=None, override_rpd=None, override_maxc=None):
    sb_path = os.path.join(project_dir, "storyboard.json")
    if not os.path.exists(sb_path):
        print(f"Error: storyboard.json not found in {project_dir}")
        sys.exit(1)

    sb = load_json(sb_path)
    scenes = sb.get("scenes", [])

    # Group shots by model
    model_shots = {}
    for scene in scenes:
        for shot in scene.get("shots", []):
            model = shot.get("model", "unknown").lower().replace(" ", "_")
            if model not in model_shots:
                model_shots[model] = []
            model_shots[model].append({
                "scene_id": scene.get("scene_id"),
                "shot_id": shot.get("shot_id"),
                "type": shot.get("type", "image"),
                "function": shot.get("function", ""),
            })

    print(f"\n{'Model':<18} {'Shots':>6} {'RPM':>5} {'RPD':>6} {'Concurrent':>10} {'Cooldown':>9} {'Batches':>8} {'Est. Time':>10}")
    print("-" * 95)

    total_time_sec = 0.0
    for model, shots in sorted(model_shots.items()):
        limit = DEFAULT_LIMITS.get(model, {"rpm": 5, "rpd": 500, "max_concurrent": 2, "cooldown_sec": 12})
        rpm = override_rpm if override_rpm else limit["rpm"]
        rpd = override_rpd if override_rpd else limit["rpd"]
        maxc = override_maxc if override_maxc else limit["max_concurrent"]
        cooldown = limit["cooldown_sec"]

        count = len(shots)
        # Simple batching: each batch = max_concurrent shots, then cooldown
        batches = math.ceil(count / maxc)
        est_time = (batches - 1) * cooldown if batches > 0 else 0

        # Also respect daily limit
        if count > rpd:
            print(f"  WARNING: {model} requires {count} shots but RPD is {rpd}. Will span multiple days.")

        total_time_sec += est_time
        print(f"{model:<18} {count:>6} {rpm:>5} {rpd:>6} {maxc:>10} {cooldown:>9}s {batches:>8} {est_time:>8}s")

    print("-" * 95)
    minutes = int(total_time_sec // 60)
    seconds = int(total_time_sec % 60)
    print(f"{'TOTAL WALL TIME (serial models)':<50} {minutes}m {seconds}s")
    print(f"  Note: Models can run in parallel. Actual wall time ≈ max(model_est_time).")
    print()

    # Write batch plan JSON
    plan_path = os.path.join(project_dir, "batch_plan.json")
    plan = {
        "models": {},
        "total_shots": sum(len(v) for v in model_shots.values()),
        "estimated_wall_time_sec": total_time_sec,
    }
    for model, shots in model_shots.items():
        limit = DEFAULT_LIMITS.get(model, {"rpm": 5, "rpd": 500, "max_concurrent": 2, "cooldown_sec": 12})
        maxc = override_maxc if override_maxc else limit["max_concurrent"]
        batches = []
        for i in range(0, len(shots), maxc):
            batches.append(shots[i:i+maxc])
        plan["models"][model] = {
            "total": len(shots),
            "batch_size": maxc,
            "batch_count": len(batches),
            "batches": [{"index": i+1, "shots": b} for i, b in enumerate(batches)],
        }

    with open(plan_path, "w", encoding="utf-8") as f:
        json.dump(plan, f, ensure_ascii=False, indent=2)
    print(f"Batch plan written to: {plan_path}")


def main():
    parser = argparse.ArgumentParser(description="Plan generation batches by API limits")
    parser.add_argument("project_dir", help="Path to project directory")
    parser.add_argument("--rpm", type=int, help="Override RPM for all models", default=None)
    parser.add_argument("--rpd", type=int, help="Override RPD for all models", default=None)
    parser.add_argument("--max-concurrent", type=int, help="Override max concurrent for all models", default=None)
    args = parser.parse_args()
    plan_batches(args.project_dir, args.rpm, args.rpd, args.max_concurrent)


if __name__ == "__main__":
    main()
