#!/usr/bin/env python3
"""
snapshot.py — Save a project snapshot as a git commit or zip archive.
Use before risky experiments (style changes, mass regeneration, etc.).

Usage:
    python snapshot.py my_project --message "before style change"
    python snapshot.py my_project --zip
"""

import argparse
import subprocess
import sys
from datetime import datetime
from pathlib import Path
import zipfile


def git_snapshot(project_dir: Path, message: str):
    if not (project_dir / ".git").exists():
        print("[INFO] Initializing git repo for snapshots...")
        subprocess.run(["git", "init"], cwd=project_dir, capture_output=True)

    subprocess.run(["git", "add", "-A"], cwd=project_dir, capture_output=True)
    result = subprocess.run(
        ["git", "commit", "-m", f"[snapshot] {message}"],
        cwd=project_dir, capture_output=True, text=True
    )
    if result.returncode == 0:
        print(f"[OK] Git snapshot saved: {message}")
    else:
        # Might be nothing to commit
        print(f"[INFO] {result.stderr.strip() or 'No changes to snapshot'}")


def zip_snapshot(project_dir: Path, message: str):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    zip_name = project_dir / f"snapshot_{timestamp}_{message.replace(' ', '_')}.zip"

    with zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in project_dir.rglob("*"):
            if ".git" in str(f) or f.name.startswith("snapshot_") and f.suffix == ".zip":
                continue
            if f.is_file():
                zf.write(f, f.relative_to(project_dir))

    print(f"[OK] Zip snapshot saved: {zip_name}")


def main():
    parser = argparse.ArgumentParser(description="Save a project snapshot")
    parser.add_argument("project_dir", help="Path to project directory")
    parser.add_argument("--message", "-m", default="manual snapshot", help="Snapshot description")
    parser.add_argument("--zip", action="store_true", help="Save as zip instead of git commit")
    args = parser.parse_args()

    project_dir = Path(args.project_dir)
    if not project_dir.exists():
        print(f"[ERROR] Directory not found: {project_dir}")
        sys.exit(1)

    if args.zip:
        zip_snapshot(project_dir, args.message)
    else:
        git_snapshot(project_dir, args.message)


if __name__ == "__main__":
    main()
