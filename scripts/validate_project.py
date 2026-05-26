#!/usr/bin/env python3
"""
Validate Sloth-ComicSmith-Den v2.1 project files for schema compliance.
Usage: python validate_project.py <project_folder>
"""

import sys
import os
import json

VALID_SCENE_FUNCTIONS = {"exposition", "rising_action", "turning_point", "climax", "falling_action", "resolution"}
VALID_ACT_POSITIONS = {"act_1", "act_2a", "act_2b", "act_3"}
VALID_DIALOGUE_TYPES = {"spoken", "narration", "thought"}
VALID_SHOT_FUNCTIONS = {"establishing", "master", "insert", "reaction", "pov", "cutaway", "transition"}
VALID_FRAMINGS = {"wide", "medium", "close-up", "extreme-close-up"}
VALID_AXIS_SIDES = {"left", "right", "neutral"}
VALID_TIMING_STYLES = {"real_time", "slow_motion", "held_frame", "staccato"}
VALID_BEAT_TYPES = {"reaction", "realization", "decision", "suppression", "release"}
VALID_DOFS = {"deep_focus", "shallow_focus", "rack_focus", "full_blur"}
VALID_MC_STRATEGIES = {"layered_composite", "occlusion", "master_extra", "ebsynth"}
VALID_CULTURAL_CONTEXTS = {"western", "east_asian", "custom"}
VALID_PAGE_TURN_TYPES = {"cliffhanger", "reveal", "transition", "breath"}


def validate_scenes(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert "title" in data, "Missing 'title' in scenes.json"
    assert "scenes" in data, "Missing 'scenes' array in scenes.json"
    assert "dramatic_structure" in data, "Missing 'dramatic_structure' in scenes.json"
    ds = data["dramatic_structure"]
    for key in ["inciting_incident", "midpoint", "climax", "all_is_lost"]:
        assert key in ds, f"Missing '{key}' in dramatic_structure"
    for i, scene in enumerate(data["scenes"]):
        assert "scene_id" in scene, f"Scene {i} missing 'scene_id'"
        assert "setting" in scene, f"Scene {i} missing 'setting'"
        assert "characters" in scene, f"Scene {i} missing 'characters'"
        assert "action" in scene, f"Scene {i} missing 'action'"
        assert "scene_function" in scene, f"Scene {i} missing 'scene_function'"
        assert scene["scene_function"] in VALID_SCENE_FUNCTIONS, f"Scene {i} invalid scene_function: {scene['scene_function']}"
        assert "act_position" in scene, f"Scene {i} missing 'act_position'"
        assert scene["act_position"] in VALID_ACT_POSITIONS, f"Scene {i} invalid act_position: {scene['act_position']}"
        if "dialogue" in scene:
            for j, d in enumerate(scene["dialogue"]):
                assert "type" in d, f"Scene {i} dialogue {j} missing 'type'"
                assert d["type"] in VALID_DIALOGUE_TYPES, f"Scene {i} dialogue {j} invalid type: {d['type']}"
                assert "subtext" in d, f"Scene {i} dialogue {j} missing 'subtext'"
    print("scenes.json: OK")


def validate_characters(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert "visual_style_anchor" in data, "Missing 'visual_style_anchor' in characters.json"
    assert "visual_style_preset" in data, "Missing 'visual_style_preset' in characters.json"
    assert "characters" in data, "Missing 'characters' array in characters.json"
    for i, char in enumerate(data["characters"]):
        assert "name" in char, f"Character {i} missing 'name'"
        assert "consistency_prompt" in char, f"Character {i} missing 'consistency_prompt'"
        assert "seed" in char, f"Character {i} missing 'seed' (v2.0 requires seed locking)"
        assert "four_views" in char, f"Character {i} missing 'four_views'"
        if "expression_sheet" in char:
            expr = char["expression_sheet"]
            for key in ["neutral", "happy", "sad", "angry", "surprised", "disgusted", "fearful", "determined"]:
                assert key in expr, f"Character {i} expression_sheet missing '{key}'"
        if "micro_expression_sheet" in char:
            assert isinstance(char["micro_expression_sheet"], dict), f"Character {i} micro_expression_sheet must be a dict"
        if "posture_emotion_map" in char:
            assert isinstance(char["posture_emotion_map"], dict), f"Character {i} posture_emotion_map must be a dict"
        if "arc_stages" in char:
            for stage in char["arc_stages"]:
                assert "act" in stage, f"Character {i} arc_stage missing 'act'"
                assert "emotional_state" in stage, f"Character {i} arc_stage missing 'emotional_state'"
                assert "visual_cues" in stage, f"Character {i} arc_stage missing 'visual_cues'"
    print("characters.json: OK")


def validate_environments(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert "environments" in data, "Missing 'environments' array in environments.json"
    for i, env in enumerate(data["environments"]):
        assert "setting_key" in env, f"Environment {i} missing 'setting_key'"
        assert "design_brief" in env, f"Environment {i} missing 'design_brief'"
        if "lighting_scenarios" in env:
            for j, ls in enumerate(env["lighting_scenarios"]):
                assert "scenario_id" in ls, f"Environment {i} lighting_scenario {j} missing 'scenario_id'"
                assert "light_direction" in ls, f"Environment {i} lighting_scenario {j} missing 'light_direction'"
    print("environments.json: OK")


def validate_color_script(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert "color_arc" in data, "Missing 'color_arc' in color_script.json"
    if "cultural_context" in data:
        assert data["cultural_context"] in VALID_CULTURAL_CONTEXTS, f"Invalid cultural_context: {data['cultural_context']}"
    for i, arc in enumerate(data["color_arc"]):
        assert "scene_range" in arc, f"Color arc {i} missing 'scene_range'"
        assert "dominant_color" in arc, f"Color arc {i} missing 'dominant_color'"
        assert "accent_color" in arc, f"Color arc {i} missing 'accent_color'"
    print("color_script.json: OK")


def validate_storyboard(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert "shots" in data, "Missing 'shots' array in storyboard.json"
    for i, shot in enumerate(data["shots"]):
        assert "shot_id" in shot, f"Shot {i} missing 'shot_id'"
        assert "scene_id" in shot, f"Shot {i} missing 'scene_id'"
        assert "framing" in shot, f"Shot {i} missing 'framing' (v2.0 uses 'framing' not 'type')"
        assert shot["framing"] in VALID_FRAMINGS, f"Shot {i} invalid framing: {shot['framing']}"
        assert "function" in shot, f"Shot {i} missing 'function' (v2.0 requires shot function)"
        assert shot["function"] in VALID_SHOT_FUNCTIONS, f"Shot {i} invalid function: {shot['function']}"
        assert "image_prompt" in shot, f"Shot {i} missing 'image_prompt'"
        assert "color_direction" in shot, f"Shot {i} missing 'color_direction' (v2.0 requires color)"
        assert "axis_side" in shot, f"Shot {i} missing 'axis_side' (v2.0 requires axis tracking)"
        assert shot["axis_side"] in VALID_AXIS_SIDES, f"Shot {i} invalid axis_side: {shot['axis_side']}"
        if shot.get("function") != "transition":
            assert "audio_direction" in shot, f"Shot {i} missing 'audio_direction' (v2.0 requires audio)"
        # v2.1 optional fields
        if "timing_style" in shot:
            assert shot["timing_style"] in VALID_TIMING_STYLES, f"Shot {i} invalid timing_style: {shot['timing_style']}"
        if "acting_beats" in shot:
            for j, beat in enumerate(shot["acting_beats"]):
                assert "beat_type" in beat, f"Shot {i} beat {j} missing 'beat_type'"
                assert beat["beat_type"] in VALID_BEAT_TYPES, f"Shot {i} beat {j} invalid beat_type"
        if "depth_of_field" in shot:
            assert shot["depth_of_field"] in VALID_DOFS, f"Shot {i} invalid depth_of_field: {shot['depth_of_field']}"
        if "multi_character_strategy" in shot and shot["multi_character_strategy"] is not None:
            assert shot["multi_character_strategy"] in VALID_MC_STRATEGIES, f"Shot {i} invalid multi_character_strategy"
    print("storyboard.json: OK")


def validate_comic_pages(path):
    if not os.path.exists(path):
        print("comic_pages.json: SKIP (optional)")
        return
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert "pages" in data, "Missing 'pages' array in comic_pages.json"
    for i, page in enumerate(data.get("pages", [])):
        if "page_turn_type" in page:
            assert page["page_turn_type"] in VALID_PAGE_TURN_TYPES, f"Page {i} invalid page_turn_type: {page['page_turn_type']}"
    print("comic_pages.json: OK")


def validate_references(path):
    ref_index = os.path.join(path, "references", "ref_index.json")
    if not os.path.exists(ref_index):
        print("references/ref_index.json: SKIP (optional)")
        return
    with open(ref_index, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert "boards" in data, "Missing 'boards' in ref_index.json"
    print("references/ref_index.json: OK")


def validate_post_production(path):
    ppp = os.path.join(path, "post_production_plan.json")
    if not os.path.exists(ppp):
        print("post_production_plan.json: SKIP (optional)")
        return
    with open(ppp, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert "stages" in data, "Missing 'stages' in post_production_plan.json"
    print("post_production_plan.json: OK")


def validate(folder):
    files = {
        "scenes.json": validate_scenes,
        "characters.json": validate_characters,
        "environments.json": validate_environments,
        "color_script.json": validate_color_script,
        "storyboard.json": validate_storyboard,
        "comic_pages.json": validate_comic_pages,
    }
    for fname, validator in files.items():
        fpath = os.path.join(folder, fname)
        if not os.path.exists(fpath):
            print(f"MISSING: {fname}")
            continue
        try:
            validator(fpath)
        except Exception as e:
            print(f"{fname}: ERROR — {e}")
    # v2.1 optional files
    try:
        validate_references(folder)
    except Exception as e:
        print(f"references: ERROR — {e}")
    try:
        validate_post_production(folder)
    except Exception as e:
        print(f"post_production_plan.json: ERROR — {e}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate_project.py <project_folder>")
        sys.exit(1)
    validate(sys.argv[1])
