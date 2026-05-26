#!/usr/bin/env python3
"""
preprocess_script.py — Normalize non-standard scripts into a standard format for parsing.
Handles novel-style prose, dialogue-only scripts, outlines, and mixed-language text.

Usage:
    python preprocess_script.py input.txt --type auto --output standardized.txt
"""

import argparse
import re
from pathlib import Path


def detect_script_type(text: str) -> str:
    """Heuristically detect script format."""
    lines = text.strip().splitlines()
    if not lines:
        return "unknown"

    # Count screenplay markers
    scene_headers = sum(1 for l in lines if re.match(r"^(INT|EXT|内景|外景|场景)\.", l.strip(), re.I))
    # Count dialogue patterns (NAME\nline)
    dialogue_patterns = 0
    for i, line in enumerate(lines):
        if i + 1 < len(lines) and line.strip().isupper() and len(line.strip()) < 40:
            dialogue_patterns += 1

    if scene_headers > 2:
        return "screenplay"
    elif dialogue_patterns > len(lines) * 0.1:
        return "dialogue_only"
    elif len(text) < 2000 and "\n" not in text[:500]:
        return "outline"
    else:
        return "novel"


def normalize_screenplay(text: str) -> str:
    """Standardize screenplay format (already mostly correct)."""
    lines = text.splitlines()
    normalized = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        # Ensure scene headers have INT./EXT. prefix
        if re.match(r"^(内景|外景|场景)[\s\.·]", line):
            line = line.replace("内景", "INT.").replace("外景", "EXT.").replace("场景", "SCENE")
        normalized.append(line)
    return "\n\n".join(normalized)


def normalize_novel(text: str) -> str:
    """Convert novel prose into pseudo-screenplay format."""
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    normalized = []
    current_scene = "INT. UNKNOWN LOCATION — DAY"
    normalized.append(current_scene)
    normalized.append("")

    for para in paragraphs:
        # Check if paragraph starts with a location/time indicator
        if re.match(r"^(在|于|At|In)\s+", para):
            location = para.split("，")[0].split("。")[0]
            normalized.append(f"INT. {location} — DAY")
            normalized.append("")
            continue

        # Check for dialogue
        dialogue_match = re.findall(r'["""](.+?)["""]', para)
        if dialogue_match:
            # Treat surrounding text as action, quoted as dialogue
            action = re.sub(r'["""].+?["""]', "", para).strip("，。 \n")
            if action:
                normalized.append(action)
                normalized.append("")
            for quote in dialogue_match:
                normalized.append("CHARACTER")
                normalized.append(quote)
                normalized.append("")
        else:
            normalized.append(para)
            normalized.append("")

    return "\n".join(normalized)


def normalize_dialogue_only(text: str) -> str:
    """Add action descriptions around bare dialogue."""
    lines = text.splitlines()
    normalized = ["INT. UNKNOWN LOCATION — DAY", ""]
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        # If line is all caps and short, treat as character name
        if line.isupper() and len(line) < 40:
            normalized.append(line)
            if i + 1 < len(lines):
                normalized.append(lines[i + 1].strip())
                i += 2
            else:
                i += 1
            normalized.append("")
        else:
            normalized.append(line)
            normalized.append("")
            i += 1
    return "\n".join(normalized)


def normalize_outline(text: str) -> str:
    """Expand outline bullet points into scene descriptions."""
    lines = text.splitlines()
    normalized = []
    for line in lines:
        line = line.strip().lstrip("-*·•1234567890. ")
        if not line:
            continue
        normalized.append(f"SCENE. {line}")
        normalized.append("")
        # Add placeholder action and dialogue
        normalized.append(f"Action: {line}")
        normalized.append("")
    return "\n".join(normalized)


def preprocess(input_path: Path, script_type: str, output_path: Path):
    text = input_path.read_text(encoding="utf-8")

    if script_type == "auto":
        script_type = detect_script_type(text)
        print(f"[INFO] Detected script type: {script_type}")

    normalizers = {
        "screenplay": normalize_screenplay,
        "novel": normalize_novel,
        "dialogue_only": normalize_dialogue_only,
        "outline": normalize_outline,
    }

    if script_type not in normalizers:
        print(f"[WARN] Unknown type '{script_type}', falling back to novel mode")
        script_type = "novel"

    normalized = normalizers[script_type](text)
    output_path.write_text(normalized, encoding="utf-8")
    print(f"[OK] Standardized script saved to: {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Preprocess non-standard scripts into standard format")
    parser.add_argument("input", help="Input script file (txt, md)")
    parser.add_argument("--type", choices=["auto", "screenplay", "novel", "dialogue_only", "outline"],
                        default="auto", help="Script type (auto-detect if not specified)")
    parser.add_argument("--output", "-o", help="Output file path")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output) if args.output else input_path.with_suffix(".standardized.txt")

    preprocess(input_path, args.type, output_path)


if __name__ == "__main__":
    main()
