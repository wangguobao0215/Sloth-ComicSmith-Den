# Quality Checklist — Sloth-ComicSmith-Den v2.1

Use this checklist at the end of each pipeline stage. Every item is scored Pass / Modify / Block.

- **Pass** — meets standard; proceed.
- **Modify** — needs revision within stage; do not proceed until fixed.
- **Block** — critical flaw; rollback to previous stage or restart.

---

## Stage 1 — Parse Script

| # | Checkpoint | Criteria | Score |
|---|------------|----------|-------|
| 1.1 | Scene integrity | Every scene has unique `scene_id`, `title`, `mood`. | |
| 1.2 | Dialogue typed | All dialogue entries have `type` ∈ {spoken, narration, thought}. | |
| 1.3 | Dramatic structure mapped | `inciting_incident`, `midpoint`, `climax` are assigned to scene IDs. | |
| 1.4 | Subtext noted | Key scenes have `subtext` field explaining implied meaning. | |
| 1.5 | Character roster complete | Every speaker in dialogue exists in `characters.json`. | |
| 1.6 | Language consistent | `language` field matches actual script language. | |

**Stage Gate**: If any item is Block, fix `scenes.json` before proceeding.

---

## Stage 2 — Design World

| # | Checkpoint | Criteria | Score |
|---|------------|----------|-------|
| 2.1 | Character 4-view refs | Each major character has `reference_images` with 4 views. | |
| 2.2 | Expression sheet | Each major character has `expression_sheet` with ≥ 5 emotions. | |
| 2.3 | Micro-expression sheet | Each major character has `micro_expression_sheet` with nuanced expressions. | |
| 2.4 | Posture-emotion map | `posture_emotion_map` connects body language to psychological states. | |
| 2.5 | Outfit tracking | `outfits` array covers all acts; no undefined costume at any scene. | |
| 2.6 | Color script coverage | `color_script.json` has entry for every scene; dominant + accent defined. | |
| 2.7 | Color arc logic | Colors progress logically across acts (e.g., warm → cool → warm). | |
| 2.8 | Cultural context | `cultural_context` is set (western/east_asian/custom); color symbolism is appropriate. | |
| 2.9 | Lighting script | Each environment has `lighting_scenarios` with direction, quality, motif, rim light plan. | |
| 2.10 | Environment keys | Every scene location exists in `environments.json` with spatial layout + lighting. | |
| 2.11 | Seed strategy | `seed_pool` has ≥ 1 locked seed per major character. | |
| 2.12 | Reference board | `references/` folder has mood/style boards; `ref_index.json` links to shots. | |

**Stage Gate**: If 2.1, 2.2, 2.6, or 2.9 is Block, do not proceed to storyboard.

---

## Stage 3 — Storyboard

| # | Checkpoint | Criteria | Score |
|---|------------|----------|-------|
| 3.1 | Shot function purpose | Every shot has `function` explaining its narrative job. | |
| 3.2 | Framing variety | No adjacent identical framings without narrative reason. | |
| 3.3 | Axis consistency | `axis_side` is consistent per scene; axis jumps are intentional and noted. | |
| 3.4 | Camera motion precision | `camera_movement` uses verb + direction + magnitude + duration format. | |
| 3.5 | Prompt quality | `image_prompt` ≥ 30 words; includes subject, environment, lighting, style, silhouette insurance. | |
| 3.6 | Video prompt quality | `video_prompt` specifies motion, not just adjectives; aligns with `acting_beats`. | |
| 3.7 | Acting beats | Key performance shots have `acting_beats` with `beat_type`, `micro_expression`, `body_language`. | |
| 3.8 | Timing style | `timing_style` is deliberate (real_time / slow_motion / held_frame / staccato). | |
| 3.9 | Eye trace | `eye_trace_in` / `eye_trace_out` create smooth gaze flow between adjacent shots. | |
| 3.10 | Silhouette check | `silhouette_check` confirms subject readability; rim light added when needed. | |
| 3.11 | Depth of field | `depth_of_field` choice serves narrative (deep = objective, shallow = subjective). | |
| 3.12 | Master layout anchor | One shot per scene is `master_layout_anchor: true` with full spatial description. | |
| 3.13 | Multi-character strategy | Shots with 2+ characters have `multi_character_strategy` (composite / occlusion / master_extra). | |
| 3.14 | Audio direction | Every scene has `audio_direction` with ambience + foley key moments + music mood + voice direction. | |
| 3.15 | Scene function alignment | Shot `function` aligns with scene `scene_function`. | |
| 3.16 | Character arc visibility | Act 3 shots show arc change compared to Act 1 (expression, posture, outfit). | |
| 3.17 | Color direction | Shot prompts reference `color_direction` from color script. | |

**Stage Gate**: If 3.1, 3.3, 3.5, 3.9, or 3.12 is Block, revise storyboard before generation.

---

## Stage 4 — Generate Images / Video

| # | Checkpoint | Criteria | Score |
|---|------------|----------|-------|
| 4.1 | Seed locked | Character shots use locked seed from `seed_pool`. | |
| 4.2 | Reference attached | `--cref`, IP-Adapter, or equivalent reference is used per model strategy. | |
| 4.3 | Prompt builder followed | Prompts follow reference.md builder order (color → subject → expression → environment → lighting → silhouette → style → camera → motion). | |
| 4.4 | Style consistency | All shots use the same `visual_style` preset; deviations are intentional. | |
| 4.5 | Reference board used | Prompts incorporate `references/ref_index.json` linked mood/style references. | |
| 4.6 | Lighting scenario respected | Generated images match `lighting_scenarios` direction, quality, and motif. | |
| 4.7 | Generation log updated | Every attempt is logged in `generation_log.json` with seed, model, result. | |
| 4.8 | Failed shots tracked | Failures are captured in `failed_shots.json` with reason and retry plan. | |
| 4.9 | Batch plan followed | Generation follows `batch_plan.json`; no RPM/RPD limit breaches. | |
| 4.10 | Cost estimate reviewed | Actual spend is within `cost_estimator.py` estimate ± 20%. | |

**Stage Gate**: If 4.1 or 4.2 is Block for a main character, regenerate those shots.

---

## Stage 5 — Synthesize Video

| # | Checkpoint | Criteria | Score |
|---|------------|----------|-------|
| 5.1 | Asset inventory | All generated files exist and match `storyboard.json` shot list. | |
| 5.2 | Sequence order | Video sequence matches storyboard scene/shot order. | |
| 5.3 | Transition intent | `transition` fields are respected (hard cut / fade / match cut). | |
| 5.4 | Subtitle sync | `output.srt` timing aligns with shot durations; text matches spoken dialogue only. | |
| 5.5 | Audio mix | BGM mood aligns with `audio_direction.music_mood`; dialogue is audible. | |
| 5.6 | Color grading | Final output reflects `color_script.json` arc; no jarring color jumps. | |
| 5.7 | Axis spatial coherence | 180° rule is not accidentally broken in final edit. | |
| 5.8 | Pacing check | Total runtime feels intentional; `timing_style` intentions are preserved. | |

**Stage Gate**: If 5.1 or 5.4 is Block, do not render final output.

---

## Stage 5b — Post-Production & Repair

| # | Checkpoint | Criteria | Score |
|---|------------|----------|-------|
| 5b.1 | Flicker removal | Temporal NR applied; no frame-to-frame color/noise variance. | |
| 5b.2 | Face repair | Bad face frames identified and replaced (FaceFusion / manual). | |
| 5b.3 | Motion stabilization | Jittery camera motion smoothed (Warp Stabilizer or equivalent). | |
| 5b.4 | Color consistency | All shots color-matched to `master_layout_anchor` reference frame. | |
| 5b.5 | Audio layering | Ambience + foley key moments + stinger + BGM properly mixed; silence_flags respected. | |
| 5b.6 | Voice direction | Recorded/ synthesized dialogue matches `audio_direction.voice_direction` notes. | |
| 5b.7 | Post plan completed | All stages in `post_production_plan.json` marked completed. | |

**Stage Gate**: If 5b.1 or 5b.4 is Block, return to color grade and re-export.

---

## Comic Page Assembly (Optional)

| # | Checkpoint | Criteria | Score |
|---|------------|----------|-------|
| 6.1 | Panel flow | Reading order (Z-pattern for LTR, reverse for RTL) is obvious. | |
| 6.2 | Bleed safety | Art intended for bleed extends ≥ 3mm past trim line. | |
| 6.3 | Balloon placement | Speech balloons do not cover character eyes or key action. | |
| 6.4 | Gutters consistent | Margin between panels is uniform unless intentional stylistic gap. | |
| 6.5 | Page turn design | Each page has deliberate `page_turn_type` (cliffhanger / reveal / transition / breath). | |
| 6.6 | Speed lines | Action/emphasis panels use appropriate speed lines (radial / parallel / turbulent / streamline). | |
| 6.7 | SFX typography | Sound effects are sized to intensity, positioned away from key action, styled to sound quality. | |

---

## Overall Quality Score

For each stage, count: Pass = 1, Modify = 0.5, Block = 0.
Divide by total items in stage to get stage score.

| Stage | Items | Formula |
|-------|-------|---------|
| Parse Script | 6 | Score / 6 |
| Design World | 12 | Score / 12 |
| Storyboard | 17 | Score / 17 |
| Generate | 10 | Score / 10 |
| Synthesize | 8 | Score / 8 |
| Post-Production | 7 | Score / 7 |
| Comic (optional) | 7 | Score / 7 |

**Project Grade**
- ≥ 90% — Release ready
- 75–89% — Release with minor revisions
- 60–74% — Major revision required before release
- < 60% — Return to earliest Block stage and rework

---

*Version: 2.1.0 | Update with each project retrospective.*
