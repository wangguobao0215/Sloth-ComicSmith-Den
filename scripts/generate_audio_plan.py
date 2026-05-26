#!/usr/bin/env python3
"""
generate_audio_plan.py — Auto-generate a complete audio design plan from storyboard.json.
Outputs audio_plan.json with BGM cues, voice assignments, foley events, and subtitle timing.

Usage:
    python generate_audio_plan.py my_project [--bgm-source auto|suno|epidemic|file]
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, List, Optional


# BGM emotion mapping: mood keywords → music characteristics
BGM_CATALOG = {
    "melancholic": {"genre": "solo_piano", "tempo_bpm": 60, "key": "minor", "instruments": ["piano", "strings_pad"], "intensity": 0.3},
    "weary": {"genre": "ambient", "tempo_bpm": 50, "key": "minor", "instruments": ["synth_pad", "rain_ambience"], "intensity": 0.2},
    "introspective": {"genre": "solo_piano", "tempo_bpm": 65, "key": "minor", "instruments": ["piano", "soft_strings"], "intensity": 0.3},
    "hopeful": {"genre": "acoustic_folk", "tempo_bpm": 80, "key": "major", "instruments": ["acoustic_guitar", "strings"], "intensity": 0.5},
    "tense": {"genre": "orchestral_tension", "tempo_bpm": 90, "key": "minor", "instruments": ["strings", "timpani"], "intensity": 0.7},
    "climactic": {"genre": "orchestral", "tempo_bpm": 120, "key": "minor", "instruments": ["full_orchestra"], "intensity": 1.0},
    "peaceful": {"genre": "ambient", "tempo_bpm": 55, "key": "major", "instruments": ["synth_pad", "bells"], "intensity": 0.2},
    "lonely": {"genre": "solo_piano", "tempo_bpm": 55, "key": "minor", "instruments": ["piano", "solo_violin"], "intensity": 0.3},
}

# Default BGM for mood not explicitly listed
DEFAULT_BGM = {"genre": "ambient", "tempo_bpm": 60, "key": "minor", "instruments": ["piano", "pad"], "intensity": 0.3}

# Scene function → BGM intensity curve
FUNCTION_INTENSITY = {
    "exposition": 0.2,
    "rising_action": 0.5,
    "turning_point": 0.7,
    "climax": 1.0,
    "falling_action": 0.4,
    "resolution": 0.2,
}

# TTS voice presets per character archetype
TTS_VOICES = {
    "young_female_weary": {"provider": "elevenlabs", "voice_id": "XB0fDUnXU5powFXDhCwa", "speed": 0.95, "pitch_shift": 0},
    "young_female_determined": {"provider": "elevenlabs", "voice_id": "XB0fDUnXU5powFXDhCwa", "speed": 1.05, "pitch_shift": 1},
    "middle_age_male_kind": {"provider": "elevenlabs", "voice_id": "TX3AE3VoIzMeN6BkC0Gl", "speed": 0.9, "pitch_shift": -1},
    "narrator": {"provider": "elevenlabs", "voice_id": "N2lVS1w4EtoT3dr4eOWO", "speed": 0.92, "pitch_shift": 0},
}


def match_bgm(mood: str, scene_function: str) -> dict:
    """Match BGM characteristics based on mood and scene function."""
    mood_lower = mood.lower()
    
    # Find best matching mood keyword
    matched_bgm = DEFAULT_BGM
    for keyword, bgm in BGM_CATALOG.items():
        if keyword in mood_lower:
            matched_bgm = bgm
            break
    
    # Adjust intensity based on scene function
    func_intensity = FUNCTION_INTENSITY.get(scene_function, 0.3)
    final_intensity = (matched_bgm["intensity"] + func_intensity) / 2
    
    result = dict(matched_bgm)
    result["intensity"] = round(final_intensity, 2)
    result["mood_matched"] = mood
    result["scene_function"] = scene_function
    return result


def generate_audio_plan(project_dir: Path, bgm_source: str = "auto"):
    storyboard_path = project_dir / "storyboard.json"
    scenes_path = project_dir / "scenes.json"
    characters_path = project_dir / "characters.json"
    
    if not storyboard_path.exists():
        print(f"[ERROR] storyboard.json not found in {project_dir}")
        sys.exit(1)
    
    with open(storyboard_path, "r", encoding="utf-8") as f:
        storyboard = json.load(f)
    
    scenes_data = {}
    if scenes_path.exists():
        with open(scenes_path, "r", encoding="utf-8") as f:
            scenes_data = json.load(f)
    
    characters_data = {}
    if characters_path.exists():
        with open(characters_path, "r", encoding="utf-8") as f:
            characters_data = json.load(f)
    
    shots = storyboard.get("shots", [])
    scenes_list = scenes_data.get("scenes", [])
    characters_list = characters_data.get("characters", [])
    
    # Build character voice mapping
    character_voices = {}
    for char in characters_list:
        name = char["name"]
        age = char.get("age", 25)
        gender = char.get("gender", "female")
        personality = char.get("personality", [])
        
        # Simple heuristic for voice assignment
        if age < 30 and gender == "female":
            if "weary" in personality or "reserved" in personality:
                voice_key = "young_female_weary"
            else:
                voice_key = "young_female_determined"
        elif age > 45 and gender == "male":
            voice_key = "middle_age_male_kind"
        else:
            voice_key = "narrator"
        
        character_voices[name] = {
            "name": name,
            "assigned_voice": voice_key,
            "tts_config": TTS_VOICES.get(voice_key, TTS_VOICES["narrator"]),
            "emotion_hint": ", ".join(personality[:2]) if personality else "neutral"
        }
    
    # Build audio plan per shot
    global_time = 0.0
    bgm_cues = []
    voice_cues = []
    foley_cues = []
    subtitle_entries = []
    
    for shot in shots:
        shot_id = shot.get("shot_id", "")
        duration = shot.get("duration", 4)
        mood = shot.get("lighting_mood", "")
        scene_id = shot.get("scene_id", "")
        audio_dir = shot.get("audio_direction", {})
        dialogue_refs = shot.get("dialogue_ref", [])
        
        # Find scene meta for mood and function
        scene_meta = None
        for s in scenes_list:
            if s.get("scene_id") == scene_id:
                scene_meta = s
                break
        
        scene_function = scene_meta.get("scene_function", "exposition") if scene_meta else "exposition"
        scene_mood = scene_meta.get("mood", "neutral") if scene_meta else "neutral"
        
        # BGM cue
        bgm_match = match_bgm(scene_mood, scene_function)
        bgm_cues.append({
            "shot_id": shot_id,
            "start_time": round(global_time, 2),
            "end_time": round(global_time + duration, 2),
            "bgm": bgm_match,
            "silence_flag": audio_dir.get("silence_flag", False),
            "bgm_source": bgm_source
        })
        
        # Voice cues from dialogue
        if scene_meta and "dialogue" in scene_meta:
            for dlg in scene_meta["dialogue"]:
                speaker = dlg.get("speaker", "")
                line = dlg.get("line", "")
                dlg_type = dlg.get("type", "spoken")
                
                if not line:
                    continue
                
                # Skip narrator for now (can be added as voice-over option)
                if dlg_type == "spoken" and speaker in character_voices:
                    voice_cues.append({
                        "shot_id": shot_id,
                        "timestamp": round(global_time + 0.5, 2),  # slight delay after shot start
                        "duration": min(len(line) * 0.25, duration - 1),  # estimate: 0.25s per char
                        "speaker": speaker,
                        "text": line,
                        "voice_config": character_voices[speaker]["tts_config"],
                        "emotion": dlg.get("subtext", "neutral"),
                        "output_file": f"assets/audio/voice/{shot_id}_{speaker}.mp3"
                    })
                    
                    # Subtitle entry
                    subtitle_entries.append({
                        "index": len(subtitle_entries) + 1,
                        "shot_id": shot_id,
                        "start": round(global_time + 0.5, 2),
                        "end": round(global_time + 0.5 + min(len(line) * 0.25, duration - 1), 2),
                        "speaker": speaker,
                        "text": line,
                        "type": dlg_type,
                        "style": "dialogue_white" if dlg_type == "spoken" else "thought_italic"
                    })
                
                elif dlg_type == "thought" and speaker in character_voices:
                    # Inner thoughts as subtitles only (no voice by default)
                    subtitle_entries.append({
                        "index": len(subtitle_entries) + 1,
                        "shot_id": shot_id,
                        "start": round(global_time + 0.5, 2),
                        "end": round(global_time + duration - 0.5, 2),
                        "speaker": speaker,
                        "text": f"（内心）{line}",
                        "type": dlg_type,
                        "style": "thought_italic"
                    })
        
        # Foley cues from foley_key_moments
        foley_events = audio_dir.get("foley_key_moments", [])
        for event in foley_events:
            event_time = global_time + event.get("timestamp", 0)
            foley_cues.append({
                "shot_id": shot_id,
                "timestamp": round(event_time, 2),
                "sound": event.get("sound", ""),
                "intensity": event.get("intensity", "medium"),
                "duration": event.get("duration", 0.5),
                "suggested_file": f"assets/audio/foley/{event['sound']}.mp3"
            })
        
        # Ambience cue per shot
        ambience = audio_dir.get("ambience", "")
        if ambience:
            foley_cues.append({
                "shot_id": shot_id,
                "timestamp": round(global_time, 2),
                "sound": f"ambience_{ambience.replace(' ', '_')}",
                "intensity": "low",
                "duration": duration,
                "type": "ambience",
                "suggested_file": f"assets/audio/ambience/{ambience.replace(' ', '_')}.mp3"
            })
        
        global_time += duration
    
    # Consolidate BGM: merge adjacent shots with same BGM characteristics
    consolidated_bgm = []
    current_bgm = None
    for cue in bgm_cues:
        if current_bgm is None or cue["bgm"]["genre"] != current_bgm["genre"] or cue["silence_flag"] != current_bgm["silence_flag"]:
            if current_bgm is not None:
                consolidated_bgm.append(current_bgm)
            current_bgm = {
                "start_time": cue["start_time"],
                "end_time": cue["end_time"],
                "genre": cue["bgm"]["genre"],
                "tempo_bpm": cue["bgm"]["tempo_bpm"],
                "key": cue["bgm"]["key"],
                "intensity": cue["bgm"]["intensity"],
                "instruments": cue["bgm"]["instruments"],
                "silence_flag": cue["silence_flag"],
                "shots": [cue["shot_id"]],
                "bgm_source": bgm_source,
                "generation_prompt": f"{cue['bgm']['genre']}, {cue['bgm']['key']} key, {cue['bgm']['tempo_bpm']} BPM, {', '.join(cue['bgm']['instruments'])}, intensity {cue['bgm']['intensity']}"
            }
        else:
            current_bgm["end_time"] = cue["end_time"]
            current_bgm["shots"].append(cue["shot_id"])
    
    if current_bgm is not None:
        consolidated_bgm.append(current_bgm)
    
    # Build final audio plan
    audio_plan = {
        "project": project_dir.name,
        "total_duration": round(global_time, 2),
        "character_voices": character_voices,
        "bgm_cues": consolidated_bgm,
        "voice_cues": voice_cues,
        "foley_cues": foley_cues,
        "subtitle_entries": subtitle_entries,
        "execution_steps": [
            "1. Run synthesize_voice.py to generate voice clips from voice_cues",
            "2. Obtain BGM files matching bgm_cues (generate with Suno or download from Epidemic Sound)",
            "3. Obtain foley/ambience files matching foley_cues (from freesound.org or ElevenLabs SFX)",
            "4. Run mix_audio.py to combine all audio layers",
            "5. Run compile_video.py --audio mixed_audio.mp3 --subtitles subtitles.srt"
        ]
    }
    
    output_path = project_dir / "audio_plan.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(audio_plan, f, indent=2, ensure_ascii=False)
    
    print(f"[OK] Audio plan generated: {output_path}")
    print(f"  Total duration: {global_time:.1f}s")
    print(f"  BGM cues: {len(consolidated_bgm)} segments")
    print(f"  Voice cues: {len(voice_cues)} lines")
    print(f"  Foley cues: {len(foley_cues)} events")
    print(f"  Subtitle entries: {len(subtitle_entries)} lines")
    print(f"\nNext step: Run synthesize_voice.py {project_dir}")


def main():
    parser = argparse.ArgumentParser(description="Generate audio design plan from storyboard")
    parser.add_argument("project_dir", help="Path to project directory")
    parser.add_argument("--bgm-source", choices=["auto", "suno", "epidemic", "file"], default="auto",
                        help="BGM acquisition method")
    args = parser.parse_args()
    
    generate_audio_plan(Path(args.project_dir), args.bgm_source)


if __name__ == "__main__":
    main()
