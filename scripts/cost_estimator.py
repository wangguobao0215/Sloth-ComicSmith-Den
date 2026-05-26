#!/usr/bin/env python3
"""
Cost Estimator for Sloth-ComicSmith-Den projects.
Reads project JSONs and estimates API spend by model.
Usage: python cost_estimator.py <project_dir> [--model <model_name>]
"""

import sys
import os
import json
import argparse

# Pricing table: USD per unit
# Images: per image. Videos: per video (5s clip).
PRICING = {
    "midjourney": {"type": "image", "unit_usd": 0.10, "note": "Standard plan avg"},
    "dalle3": {"type": "image", "unit_usd": 0.040, "note": "1024x1024"},
    "dalle3_hd": {"type": "image", "unit_usd": 0.080, "note": "1024x1024 HD"},
    "sd_api": {"type": "image", "unit_usd": 0.003, "note": "Stability AI avg"},
    "kling": {"type": "video", "unit_usd": 0.50, "note": "5s standard"},
    "runway": {"type": "video", "unit_usd": 0.20, "note": "Gen-3 5s"},
    "pika": {"type": "video", "unit_usd": 0.30, "note": "1.5 5s"},
    "veo": {"type": "video", "unit_usd": 0.35, "note": "Veo 2 5s"},
    "gemini_image": {"type": "image", "unit_usd": 0.00, "note": "Free tier / variable"},
    "gemini_video": {"type": "video", "unit_usd": 0.00, "note": "Free tier / variable"},
}


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def estimate(project_dir, filter_model=None, mode="full"):
    storyboard_path = os.path.join(project_dir, "storyboard.json")
    if not os.path.exists(storyboard_path):
        print(f"Error: storyboard.json not found in {project_dir}")
        sys.exit(1)

    sb = load_json(storyboard_path)
    shots = sb.get("shots", [])

    # Budget mode filtering
    total_shots = len(shots)
    if mode == "storyboard_only":
        print(f"\n[MODE: storyboard_only] Zero API cost. Outputs professional storyboard PDF only.")
        print(f"Total shots in storyboard: {total_shots}")
        return

    filtered_shots = shots
    if mode == "key_shots_only":
        key_functions = {"establishing", "master", "climax", "transition"}
        filtered_shots = [s for s in shots if s.get("function") in key_functions]
        print(f"\n[MODE: key_shots_only] Generating {len(filtered_shots)}/{total_shots} shots (establishing/master/climax/transition)")
    else:
        print(f"\n[MODE: full] Generating all {total_shots} shots")

    counts = {}
    for shot in filtered_shots:
        model = shot.get("model", "midjourney")
        shot_type = shot.get("type", "image")
        key = model.lower().replace(" ", "_")
        if key not in counts:
            counts[key] = {"image": 0, "video": 0}
        counts[key][shot_type] += 1

    print(f"\n{'Model':<18} {'Type':<8} {'Count':>6} {'Unit $':>10} {'Subtotal $':>12} {'Note'}")
    print("-" * 80)
    total = 0.0
    for model, cnt in sorted(counts.items()):
        info = PRICING.get(model, {"type": "image", "unit_usd": 0.0, "note": "Unknown"})
        for st in ("image", "video"):
            c = cnt.get(st, 0)
            if c == 0:
                continue
            if filter_model and filter_model.lower() not in model.lower():
                continue
            unit = info["unit_usd"]
            sub = c * unit
            total += sub
            print(f"{model:<18} {st:<8} {c:>6} {unit:>10.4f} {sub:>12.2f}  {info['note']}")

    print("-" * 80)
    print(f"{'TOTAL':<28} {'':>6} {'':>10} {total:>12.2f}")

    # Retry buffer estimate (20% extra for failed/regenerated shots)
    buffer = total * 0.20
    print(f"{'With 20% retry buffer':<28} {'':>6} {'':>10} {total + buffer:>12.2f}")

    # Local GPU alternative estimate
    if mode != "storyboard_only":
        local_hours = total_shots * 0.5 / 60  # ~30s per shot on RTX 4090
        print(f"\n[LOCAL ALT] SDXL + AnimateDiff on RTX 4090: ~{local_hours:.1f} hours, $0 API cost")
        print(f"[LOCAL ALT] Requires: 8GB+ VRAM, Python, ComfyUI or Automatic1111 setup")

    # Save cost_estimate.json
    estimate_data = {
        "mode": mode,
        "total_shots": total_shots,
        "generated_shots": len(filtered_shots),
        "estimated_usd": round(total, 2),
        "with_buffer_usd": round(total + buffer, 2),
        "local_gpu_hours": round(local_hours, 1) if mode != "storyboard_only" else 0,
        "currency": "USD"
    }
    out_path = os.path.join(project_dir, "cost_estimate.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(estimate_data, f, indent=2, ensure_ascii=False)
    print(f"\n[OK] Saved cost_estimate.json")


def main():
    parser = argparse.ArgumentParser(description="Estimate AI generation costs")
    parser.add_argument("project_dir", help="Path to project directory")
    parser.add_argument("--model", help="Filter by model name substring", default=None)
    parser.add_argument("--mode", choices=["full", "key_shots_only", "storyboard_only"], default="full",
                        help="Budget mode: full=all shots, key_shots_only=establishing+climax, storyboard_only=zero cost")
    args = parser.parse_args()
    estimate(args.project_dir, args.model, args.mode)


if __name__ == "__main__":
    main()
