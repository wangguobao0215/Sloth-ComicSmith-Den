#!/usr/bin/env python3
"""
synthesize_voice.py — Generate character voice clips from audio_plan.json using TTS APIs.
Supports ElevenLabs (recommended), Azure TTS, and edge-tts (free/local fallback).

Usage:
    python synthesize_voice.py my_project --provider elevenlabs --api-key YOUR_KEY
    python synthesize_voice.py my_project --provider edge  # free, local, no API key
"""

import argparse
import json
import os
import subprocess
import sys
import time
from pathlib import Path
from typing import Optional


def load_audio_plan(project_dir: Path) -> dict:
    path = project_dir / "audio_plan.json"
    if not path.exists():
        print(f"[ERROR] audio_plan.json not found. Run generate_audio_plan.py first.")
        sys.exit(1)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def synthesize_elevenlabs(text: str, voice_id: str, api_key: str, output_path: Path, speed: float = 1.0) -> bool:
    """Synthesize voice using ElevenLabs API."""
    import urllib.request
    import urllib.error
    
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": api_key
    }
    
    data = json.dumps({
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75,
            "speed": speed
        }
    }).encode("utf-8")
    
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    
    try:
        with urllib.request.urlopen(req, timeout=60) as response:
            with open(output_path, "wb") as f:
                f.write(response.read())
        return True
    except urllib.error.HTTPError as e:
        print(f"[WARN] ElevenLabs API error: {e.code} {e.reason}")
        return False
    except Exception as e:
        print(f"[WARN] ElevenLabs request failed: {e}")
        return False


def synthesize_edge_tts(text: str, voice_name: str, output_path: Path, speed: float = 1.0) -> bool:
    """Synthesize voice using edge-tts (free, local, no API key)."""
    try:
        # edge-tts uses percentage: -50% to +50%
        rate_str = f"{int((speed - 1.0) * 100)}%"
        cmd = [
            "edge-tts",
            "--voice", voice_name,
            "--text", text,
            "--rate", rate_str,
            "--write-media", str(output_path)
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        return result.returncode == 0 and output_path.exists() and output_path.stat().st_size > 1000
    except FileNotFoundError:
        print("[WARN] edge-tts not installed. Install: pip install edge-tts")
        return False
    except Exception as e:
        print(f"[WARN] edge-tts failed: {e}")
        return False


# Edge-TTS voice mapping by character archetype
EDGE_VOICE_MAP = {
    "young_female_weary": "zh-CN-XiaoxiaoNeural",
    "young_female_determined": "zh-CN-XiaoyiNeural",
    "middle_age_male_kind": "zh-CN-YunxiNeural",
    "narrator": "zh-CN-YunjianNeural",
}


def synthesize_all(project_dir: Path, provider: str, api_key: Optional[str]):
    audio_plan = load_audio_plan(project_dir)
    voice_cues = audio_plan.get("voice_cues", [])
    
    if not voice_cues:
        print("[INFO] No voice cues found in audio_plan.json")
        return
    
    # Create output directory
    voice_dir = project_dir / "assets" / "audio" / "voice"
    voice_dir.mkdir(parents=True, exist_ok=True)
    
    success_count = 0
    fail_count = 0
    
    for i, cue in enumerate(voice_cues):
        text = cue["text"]
        speaker = cue["speaker"]
        output_file = Path(cue["output_file"])
        output_path = project_dir / output_file
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        print(f"[{i+1}/{len(voice_cues)}] {speaker}: {text[:30]}... → {output_path.name}")
        
        if provider == "elevenlabs":
            if not api_key:
                print("[ERROR] --api-key required for ElevenLabs")
                sys.exit(1)
            voice_config = cue.get("voice_config", {})
            voice_id = voice_config.get("voice_id", "XB0fDUnXU5powFXDhCwa")
            speed = voice_config.get("speed", 1.0)
            success = synthesize_elevenlabs(text, voice_id, api_key, output_path, speed)
        
        elif provider == "edge":
            voice_config = cue.get("voice_config", {})
            voice_key = voice_config.get("voice_id", "narrator")
            # Map to edge-tts voice
            edge_voice = EDGE_VOICE_MAP.get(voice_key, "zh-CN-XiaoxiaoNeural")
            speed = voice_config.get("speed", 1.0)
            success = synthesize_edge_tts(text, edge_voice, output_path, speed)
        
        else:
            print(f"[ERROR] Unknown provider: {provider}")
            sys.exit(1)
        
        if success:
            success_count += 1
            # Small delay to avoid rate limiting
            time.sleep(0.5)
        else:
            fail_count += 1
            print(f"[FAIL] {speaker}: {text[:30]}...")
    
    print(f"\n[OK] Voice synthesis complete: {success_count} success, {fail_count} failed")
    print(f"  Output directory: {voice_dir}")
    
    if fail_count > 0:
        print(f"  Tip: Failed clips need manual recording or retry with different provider.")


def main():
    parser = argparse.ArgumentParser(description="Synthesize character voices from audio plan")
    parser.add_argument("project_dir", help="Path to project directory")
    parser.add_argument("--provider", choices=["elevenlabs", "edge"], default="edge",
                        help="TTS provider (elevenlabs=high quality paid, edge=free local)")
    parser.add_argument("--api-key", help="API key for ElevenLabs", default=None)
    args = parser.parse_args()
    
    synthesize_all(Path(args.project_dir), args.provider, args.api_key)


if __name__ == "__main__":
    main()
