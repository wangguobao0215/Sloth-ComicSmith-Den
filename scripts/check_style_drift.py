#!/usr/bin/env python3
"""
check_style_drift.py — Detect style drift between generated images and the style board.
Compares color histograms and edge density. Warns if drift exceeds threshold.

Usage:
    python check_style_drift.py my_project --threshold 0.3
"""

import argparse
import json
import sys
from pathlib import Path

try:
    from PIL import Image
    import numpy as np
except ImportError:
    print("[ERROR] Requires Pillow and numpy. Install: pip install Pillow numpy")
    sys.exit(1)


def color_histogram_distance(img1: Image.Image, img2: Image.Image) -> float:
    """Compare RGB histograms using correlation distance (0=identical, 1=totally different)."""
    size = (128, 128)
    img1 = img1.convert("RGB").resize(size)
    img2 = img2.convert("RGB").resize(size)

    hist1 = np.array(img1.histogram()) / (size[0] * size[1])
    hist2 = np.array(img2.histogram()) / (size[0] * size[1])

    # Correlation distance
    corr = np.corrcoef(hist1, hist2)[0, 1]
    if np.isnan(corr):
        return 1.0
    return 1.0 - max(0.0, corr)


def edge_density(img: Image.Image) -> float:
    """Simple edge density proxy using grayscale variance."""
    gray = img.convert("L").resize((128, 128))
    arr = np.array(gray).astype(float)
    # Laplacian variance as edge proxy
    laplacian = np.abs(arr[1:, 1:] - arr[:-1, :-1])
    return float(np.mean(laplacian))


def check_drift(project_dir: Path, threshold: float):
    refs_dir = project_dir / "references" / "style_board"
    images_dir = project_dir / "assets" / "images"

    if not refs_dir.exists() or not any(refs_dir.iterdir()):
        print("[WARN] No style board found in references/style_board/. Skipping drift check.")
        return

    if not images_dir.exists():
        print("[WARN] No generated images found.")
        return

    # Use first style board image as anchor
    anchor_path = sorted(refs_dir.glob("*"))[0]
    anchor = Image.open(anchor_path)
    anchor_edge = edge_density(anchor)

    print(f"[INFO] Style anchor: {anchor_path.name}")
    print(f"[INFO] Drift threshold: {threshold}")

    drift_detected = False
    for img_path in sorted(images_dir.glob("*.png")):
        img = Image.open(img_path)
        color_dist = color_histogram_distance(anchor, img)
        img_edge = edge_density(img)
        edge_ratio = abs(img_edge - anchor_edge) / max(anchor_edge, 1.0)

        # Combined drift score
        drift_score = (color_dist + min(edge_ratio, 1.0)) / 2

        status = "OK" if drift_score < threshold else "⚠️ DRIFT"
        if drift_score >= threshold:
            drift_detected = True

        print(f"  {img_path.name:20} color={color_dist:.3f} edge={edge_ratio:.3f} drift={drift_score:.3f} [{status}]")

    if drift_detected:
        print(f"\n[⚠️ ALERT] Style drift detected! Consider:")
        print(f"  1. Regenerating drifted images with the same seed")
        print(f"  2. Adding more specific style keywords to the prompt")
        print(f"  3. Regenerating the style board anchor from a current good image")
    else:
        print(f"\n[OK] All images within style threshold.")


def main():
    parser = argparse.ArgumentParser(description="Check for style drift in generated images")
    parser.add_argument("project_dir", help="Path to project directory")
    parser.add_argument("--threshold", type=float, default=0.3,
                        help="Drift alert threshold (0.0-1.0, default 0.3)")
    args = parser.parse_args()

    check_drift(Path(args.project_dir), args.threshold)


if __name__ == "__main__":
    main()
