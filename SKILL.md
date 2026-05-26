---
name: sloth-comicsmith-den
version: 2.1.0
description: >-
  Transforms text scripts into production-ready comic/video projects with dramatic
  structure analysis, character arc tracking, color scripting, and precise cinematography.
  Use when the user wants to create comics, storyboards, animated videos from scripts,
  or when they mention 剧本, 漫画, 分镜, storyboard, character design, or video synthesis from text.
description_zh: >-
  匠漫 · 剧本到漫画视频流水线 v2。将文本剧本转化为结构化漫画/视频项目，
  支持戏剧结构分析、角色弧光追踪、色彩脚本、精准镜头语法与声音设计。
  当用户要求创作漫画、生成分镜、将剧本转为视频、或提及剧本/漫画/分镜时调用。
license: MIT
metadata:
  author: wangguobao0215 (Sloth-Eido family)
  tags: comic storyboard script character-design video-synthesis ai-pipeline cinematography color-script
---

# Sloth-ComicSmith-Den — 匠漫 · 剧本到漫画视频流水线 v2.1

> <p align="center"><img src="https://raw.githubusercontent.com/wangguobao0215/Sloth-ComicSmith-Den/main/assets/qrcode.jpg" width="80" /><br/><sub>扫码关注 <b>树懒老K</b> · 获取更多 AI 技能</sub><br/><i>慢一点，深一度</i></p>
>
> 将文本剧本锻造成有灵魂的结构化漫画/视频项目。剧本解析（含戏剧结构） → 角色一致性（含弧光与表情表） → 色彩脚本 → 智能分镜（含镜头语法与声音设计） → AI 出图（含 Seed 锁定） → 视频合成（含精准 Motion）。

Transform a text script into a production-ready comic or animated video project through five stages. This pipeline treats story as drama, not just text — analyzing three-act structure, tracking character arcs, scripting color narratives, and applying professional cinematography principles to every shot.

## Prerequisites

Before starting, confirm the user has:
- A script file (txt, md, docx, pdf) or pasted text
- API keys for at least one image model (DALL-E, Midjourney, Stable Diffusion, or Gemini Image)
- For video synthesis: API keys for video models (Kling, Seedance, Veo, Runway, or Pika) — optional

If the user lacks API keys, complete stages 1–3 (text/structured outputs) and pause before stage 4.

## Workflow Overview

Run these stages sequentially. After each stage, present the output to the user and wait for confirmation before proceeding. At critical decision points (style selection, storyboard review, color direction), present **3 options** rather than a single default.

```
Stage 1: Parse Script          → scenes.json + raw_script.md
Stage 2: Design World          → characters.json + environments.json + color_script.json + character_prompts.md + assets/characters/ + references/
Stage 3: Generate Storyboard   → storyboard.json + shot_list.md
Stage 4: Generate Images       → assets/images/ + assets/comic-pages/ (optional)
Stage 5: Synthesize Video      → assets/video/ + output_raw.mp4 (optional)
Stage 5b: Post-Production      → output_final.mp4 + post_production_plan.json
```

All structured files use the schemas defined in [reference.md](reference.md).

---

## Stage 1: Parse Script

**Goal**: Extract scenes, dialogues, character mentions, setting descriptions, and **dramatic structure**. Support multilingual scripts.

**Input**: Raw script text or file.

**Process**:
1. Read the script. If it is a file, extract text using appropriate tools.
2. Segment into scenes. A scene change occurs on explicit headers (INT./EXT., 场景), time/location shifts, or major narrative breaks.
3. For each scene, extract:
   - `scene_id`: sequential number (S01, S02...)
   - `setting`: time and location (bilingual: `setting` + `setting_zh`)
   - `characters`: list present
   - `action`: descriptive narration
   - `dialogue`: lines with speaker, **type** (`spoken` / `narration` / `thought`), and **subtext** (infer the unspoken meaning behind the line)
   - `mood`: emotional tone
   - `scene_function`: dramatic purpose — `exposition` / `rising_action` / `turning_point` / `climax` / `falling_action` / `resolution`
4. **Dramatic Structure Analysis**: Identify the script's three-act architecture:
   - `inciting_incident`: the scene/event that disrupts the status quo
   - `midpoint`: the scene where the story pivots (false victory or false defeat)
   - `climax`: the peak confrontation scene
   - `all_is_lost`: the lowest emotional point
   - Tag each scene with its structural position: `act_1` / `act_2a` / `act_2b` / `act_3`
5. Write `scenes.json` and `raw_script.md`.

**Output format**: See `scenes.json` schema in [reference.md](reference.md).

---

## Stage 2: Design World

**Goal**: Build a consistent character bible, expression sheet, color script, and environment design — not just isolated character descriptions.

**Process**:
1. **Character Bible**: Collect unique characters from `scenes.json`. For each:
   - Name, age, gender, role (protagonist/antagonist/supporting)
   - Physical appearance, personality traits, key props
   - **Character Arc (`arc_stages`)**: Track emotional state and visual cues across acts. Example: Act 1 "hunched, avoids eye contact, cool lighting" → Act 3 "upright, direct gaze, warm gold"
   - **Outfits**: Array of clothing by scene range, with narrative reason for changes
   - Generate `consistency_prompt` (80–120 words)
2. **Expression Sheet**: For each character, generate 8 core expressions (neutral / happy / sad / angry / surprised / disgusted / fearful / determined). Save to `assets/characters/{name}/expressions/`. Use as reference during shot generation.
3. **Micro-Expression & Body Language Database**:
   - Build `micro_expression_sheet` with 7+ nuanced expressions: forced smile, jaw clench, lip tremble, eye narrow, gaze aversion, etc.
   - Build `posture_emotion_map`: map body postures (hunched, open chest, arms crossed, lean forward) to emotional states
   - Add `action_units_facs` for advanced users (reference FACS AU1–AU15)
4. **4-View Reference Images** (requires image API key):
   - Front, side, back, 3/4 view — save to `assets/characters/{name}/`
   - Assign a **fixed seed** per character for regeneration consistency
5. **Color Script (`color_script.json`)**:
   - Read the full `scenes.json` and identify the emotional arc
   - Assign each scene a `dominant_color` and `accent_color`
   - Generate a `color_arc` array showing the chromatic journey of the story
   - Set `cultural_context`: `western` / `east_asian` / `custom` (affects color symbolism)
   - Present 3 color-direction options to the user before locking
6. **Lighting Script (`environments.json`)**:
   - For each unique setting, write a 100-word design brief: spatial layout, key props, time-of-day variations, cultural/era context
   - Add `lighting_scenarios` array per setting: light direction, quality, color temp (K), movement, shadow casting, lighting motif, rim light needs
   - Lighting is a **narrative device**, not an afterthought
7. **Visual Style Anchor**: Present 3 presets from [reference.md](reference.md) or accept custom. Lock one.
8. **Reference Board (`references/`)**:
   - Collect mood images, style references, composition references into `references/mood_board/` and `references/style_board/`
   - Write `references/ref_index.json` linking references to shots
   - Even rough phone photos of lighting or poses help prevent AI hallucination
9. Write `characters.json`, `environments.json`, `color_script.json`, `character_prompts.md`.

---

## Stage 3: Generate Storyboard

**Goal**: Convert each scene into a shot-by-shot visual plan using **professional cinematography principles**.

**Process**:
1. Iterate over `scenes.json`, using `scene_function` and `act_position` to select pacing templates:
   - `exposition`: stable, informative, longer durations (4–6s)
   - `rising_action`: accelerating pace, shorter durations (2–4s)
   - `turning_point`: axis breaks, jarring angles, visual shock
   - `climax`: maximum contrast, rapid cuts, saturated colors
   - `falling_action`: breathing room, wider shots, softer light
2. For each shot, define:
   - `shot_id`: scene-prefixed (S01-01, S01-02...)
   - `framing`: wide / medium / close-up / extreme-close-up
   - **Shot `function`**: `establishing` / `master` / `insert` / `reaction` / `pov` / `cutaway` / `transition`
   - `subject`: who or what is in frame
   - `action`: what happens
   - **Camera motion** (three sub-fields):
     - `camera_movement`: static / push_in / pull_back / pan / tilt / track / dolly / crane / handheld
     - `subject_motion`: specific character/object movement
     - `environment_motion`: background/atmosphere motion
   - `lighting_mood`: lighting and atmosphere
   - `color_direction`: dominant and accent colors for this shot (derived from `color_script.json`)
   - `axis_side`: `left` / `right` / `neutral` (enforce 180-degree rule unless intentionally broken)
   - `dialogue_ref`: linked lines
   - `duration`: estimated seconds
   - **Timing & Rhythm**:
     - `timing_style`: `real_time` / `slow_motion` / `held_frame` / `staccato`
     - `rhythm_pattern`: duration ratio string like `"4-4-2"` describing relative shot lengths in a sequence
   - **Acting Beats** (`acting_beats`): Array of performance micro-moments within the shot:
     - `start` / `end`: timestamp within shot
     - `beat_type`: `reaction` / `realization` / `decision` / `suppression` / `release`
     - `micro_expression`: reference from character's micro_expression_sheet
     - `body_language`: posture change within the beat
   - **Eye Trace** (`eye_trace_in` / `eye_trace_out`): Guide viewer's gaze flow between shots. Values: `top_left`, `center`, `bottom_right`, `subject_eyes`, etc.
   - **Silhouette Check** (`silhouette_check`): Verbal description confirming subject is readable as a black shape against background. If not, add rim light to prompt.
   - **Depth of Field** (`depth_of_field`): `deep_focus` / `shallow_focus` / `rack_focus` / `full_blur`
   - **Master Layout Anchor** (`master_layout_anchor`): `true` for the one shot per scene that establishes the complete spatial layout
   - `image_prompt`: full prompt (color direction at front, consistency prompt, shot details, style anchor, silhouette insurance, rim light if needed)
   - `video_prompt`: full prompt with **precise motion descriptions** (e.g., "camera pushes in 20% closer over 3 seconds")
   - **Audio direction** (`audio_direction`):
     - `ambience`: background sound environment
     - `foley`: key sound effects tied to action
     - `foley_key_moments`: Array of precise foley events with timestamp, sound name, intensity, duration
     - `stinger`: sudden sound effect for dramatic punctuation (or null)
     - `voice_direction`: delivery notes for voice actors (pace, energy, breath)
     - `music_mood`: emotional direction for scoring
     - `silence_flag`: true if this shot should be musically or totally silent
   - `special_visual_treatment`: `narration` (text overlay + desat) / `thought` (vignette + muted) / null
   - `multi_character_strategy`: `layered_composite` / `occlusion` / `master_extra` / `ebsynth` / null (for single character)
3. **Insert transition shots** where narrative continuity demands:
   - Between scenes: fade/dissolve/wipe/match-cut
   - Between emotional shifts: reaction close-up or bridging motion
   - Mark with `function: "transition"` and `transition_type`
4. **Reference expression sheets AND micro-expression sheet** when assigning character emotions to shots. Use `beat_type` + `micro_expression` to specify nuanced performance.
5. **Apply spatial coherence**: Ensure `master_layout_anchor` shot defines room layout, and all subsequent shots respect door positions, light source direction, and prop placement.
6. Write `storyboard.json` and `shot_list.md`.

**Review checkpoint**: Present shot list with **framing + function** columns, **color preview**, and **audio direction** summary. Ask user to approve or edit before Stage 4.

---

## Stage 4: Generate Images (Optional)

**Goal**: Produce static images with strict consistency controls, batch fault tolerance, and optional comic page layout.

**Prerequisites**: User has confirmed storyboard and provided image API keys.

**Process**:
1. **Seed & Reference Strategy** (per model):
   - **Midjourney**: Use `--cref {character_front_url} --cw 100` for strong character consistency. Use `--seed {locked_seed}` per character. Use `--sref {style_board_url}` for style consistency.
   - **Stable Diffusion / ComfyUI**: Use IP-Adapter with 4-view references + ControlNet OpenPose. Lock seed in sampler.
   - **DALL-E 3**: No direct reference; rely on hard-coded consistency prompt at prompt front + locked seed if API supports.
   - **Gemini**: Use multi-image reference with character images in the API call.
2. **Multi-Character Shot Strategy**: Before generating any shot with 2+ characters visible:
   - Check `multi_character_strategy` in storyboard.
   - If `layered_composite`: Generate background + characters separately, composite in post.
   - If `occlusion`: Design shot so secondary character is backlit, in shadow, or silhouette.
   - If `master_extra`: Lock all resources on protagonist; let secondary character be generic.
   - If `ebsynth`: Generate perfect keyframe, propagate style to adjacent frames.
   - **Honest limitation**: Tell the user that unassisted AI cannot reliably maintain two distinct faces in motion. Plan for compositing.
3. For each shot, build `image_prompt` using this priority order:
   1. `color_direction` (highest weight — color impacts AI models strongly)
   2. Character consistency prompt + expression/micro-expression reference
   3. Shot-specific details (framing, function, action, environment, lighting scenario)
   4. Silhouette insurance + rim light if needed
   5. Style anchor + reference board tags
   6. Spatial context from master layout anchor
4. Generate in batches of 5–8. Track with `generation_log.json`.
5. **Batch fault tolerance**:
   - Attempt 1: full prompt with locked seed
   - Attempt 2: simplified prompt (remove 30% clauses), same seed
   - Attempt 3: minimal prompt (subject + color + style), same seed
   - All failed: mark as `failed`, write `failed_shots.json`, generate placeholder text, continue
6. **Comic page layout** (if requested):
   - Group shots into pages (3–6 panels)
   - Design `page_turn_type` for each page: `cliffhanger` / `reveal` / `transition` / `breath`
   - Add `speed_lines` and `sfx_typography` where appropriate
   - Generate `comic_pages.json` with panel positions, dialogue box styles, bleed flags
   - Composite via HTML/CSS or Pillow
7. Write/update `generation_log.json`.

---

## Stage 5: Synthesize Video (Optional)

**Goal**: Turn images into animated clips with precise motion control, smooth transitions, and subtitle integration.

**Prerequisites**: User has image outputs and video API keys.

**Process**:
1. Per shot, use `video_prompt` with **precise motion**:
   - Never use "gentle camera movement"
   - Always specify: verb + direction + magnitude + duration
   - Example: "camera slowly pushes in 20% closer to character's face over 3 seconds"
   - Reference `acting_beats` to ensure motion aligns with performance micro-moments
2. Call video API (image-to-video preferred):
   - **Kling / Seedance / Runway Gen-3 / Pika / Veo**
3. Save to `assets/video/{shot_id}.mp4`.
4. **Reference style consistency**: If using `--sref` or style board, ensure video generation references the same style anchor.

---

## Stage 5b: Post-Production & Repair (Required for Release)

**Goal**: Fix AI artifacts, ensure color consistency, stabilize motion, and deliver a professional final cut.

**Process**:
1. **Concatenate** raw clips with FFmpeg `xfade` transitions (fade / dissolve)
2. **Color grade** for consistency across shots:
   - Pick a reference frame from `master_layout_anchor` shot
   - Match all shots to reference color temperature and saturation
3. **Stabilize motion**: Apply warp stabilizer or smoothing to jittery clips
4. **Face repair**: Use FaceFusion or Rope to replace崩坏 facial frames
5. **Flicker removal**: Apply temporal noise reduction (DaVinci Resolve Temporal NR)
6. **Generate & burn subtitles**:
   - Generate `subtitles.srt` from `spoken` dialogue with timing mapped to shots
   - Burn subtitles with style override using FFmpeg
7. **Audio mix**:
   - Layer ambience + foley key moments + stinger events + BGM
   - Apply voice direction notes from `audio_direction.voice_direction`
8. **Final export** to `output_final.mp4`

**Tools**: DaVinci Resolve (color/flicker), After Effects (stabilize), FaceFusion (face repair), EbSynth (style propagation), FFmpeg (concat/subtitles), Audition / Reaper (audio mix).

**Output**: `post_production_plan.json` tracking each repair step status.

---

## Project Output Structure

```
comic-project/
├── scenes.json
├── characters.json
├── environments.json
├── color_script.json
├── storyboard.json
├── comic_pages.json
├── generation_log.json
├── failed_shots.json
├── batch_plan.json
├── post_production_plan.json
├── subtitles.srt
├── raw_script.md
├── character_prompts.md
├── shot_list.md
├── references/
│   ├── mood_board/
│   ├── style_board/
│   ├── animatic/
│   └── ref_index.json
└── assets/
    ├── characters/
    │   └── Lin/
    │       ├── front.png
    │       ├── side.png
    │       ├── back.png
    │       ├── three_quarter.png
    │       └── expressions/
    │           ├── neutral.png
    │           ├── sad.png
    │           └── ...
    ├── images/
    │   ├── S01-01.png
    │   └── ...
    ├── comic-pages/
    │   ├── page_01.png
    │   └── ...
    └── video/
        ├── S01-01.mp4
        └── ...
```

---

## Additional Resources

- For detailed JSON schemas, prompt templates, visual style presets, cinematography glossary, seed/reference strategies, and API integration patterns, see [reference.md](reference.md).
- For a complete example project with sample inputs and outputs, see [examples.md](examples.md).
- For the critical assessment that shaped this v2.0 redesign, see [ASSESSMENT.md](references/ASSESSMENT.md).
