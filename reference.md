# Sloth-ComicSmith-Den — Reference

## JSON Schemas

### scenes.json

```json
{
  "title": "Script Title",
  "language": "zh",
  "total_scenes": 3,
  "dramatic_structure": {
    "inciting_incident": "S02",
    "midpoint": "S05",
    "climax": "S08",
    "all_is_lost": "S07"
  },
  "scenes": [
    {
      "scene_id": "S01",
      "act_position": "act_1",
      "scene_function": "exposition",
      "setting": "INT. COFFEE SHOP — MORNING",
      "setting_zh": "内景 咖啡店 — 早晨",
      "characters": ["Lin", "Barista"],
      "action": "Lin enters the coffee shop, looking tired.",
      "dialogue": [
        {"speaker": "Lin", "line": "One black coffee, please.", "type": "spoken", "subtext": "Don't talk to me."},
        {"speaker": "Barista", "line": "Rough night?", "type": "spoken", "subtext": "Another exhausted customer."},
        {"speaker": "Narrator", "line": "The rain outside matched her mood.", "type": "narration", "subtext": null},
        {"speaker": "Lin", "line": "If only I could turn back time...", "type": "thought", "subtext": "I regret what happened yesterday."}
      ],
      "mood": "melancholic, weary"
    }
  ]
}
```

### characters.json

```json
{
  "visual_style_anchor": "Anime cel-shaded style, vibrant colors, clean black outlines, Studio Ghibli-inspired backgrounds",
  "visual_style_preset": "anime-cel",
  "characters": [
    {
      "name": "Lin",
      "role": "protagonist",
      "age": 28,
      "gender": "female",
      "appearance": {
        "height": "average",
        "build": "slender",
        "hair": "short black hair with blue highlights",
        "eyes": "amber",
        "clothing": "worn leather jacket, gray hoodie, dark jeans"
      },
      "personality": ["reserved", "observant", "sarcastic"],
      "props": ["silver pendant", "old notebook"],
      "consistency_prompt": "Young woman, 28, short black hair with subtle blue highlights, amber eyes, wearing a worn brown leather jacket over a gray hoodie and dark jeans. She has a silver pendant around her neck and carries an old notebook. Reserved expression, observant gaze. Anime cel-shaded style, vibrant colors, clean black outlines.",
      "seed": 42,
      "four_views": {
        "front": "assets/characters/Lin/front.png",
        "side": "assets/characters/Lin/side.png",
        "back": "assets/characters/Lin/back.png",
        "three_quarter": "assets/characters/Lin/three_quarter.png"
      },
      "expression_sheet": {
        "neutral": "assets/characters/Lin/expressions/neutral.png",
        "happy": "assets/characters/Lin/expressions/happy.png",
        "sad": "assets/characters/Lin/expressions/sad.png",
        "angry": "assets/characters/Lin/expressions/angry.png",
        "surprised": "assets/characters/Lin/expressions/surprised.png",
        "disgusted": "assets/characters/Lin/expressions/disgusted.png",
        "fearful": "assets/characters/Lin/expressions/fearful.png",
        "determined": "assets/characters/Lin/expressions/determined.png"
      },
      "micro_expression_sheet": {
        "eyebrows_raise": "surprise micro-reaction, 0.3s",
        "forced_smile": "mouth smiles but eyes do not, tension",
        "jaw_clench": "suppressed anger, tight masseter",
        "lip_tremble": "onset of tears, vulnerable",
        "eye_narrow": "suspicion or evaluation",
        "gaze_aversion": "shame, hiding, or deception",
        "nostril_flare": "controlled rage or exertion"
      },
      "action_units_facs": {
        "AU1": "inner brow raise",
        "AU2": "outer brow raise",
        "AU4": "brow lowerer",
        "AU6": "cheek raise (real smile)",
        "AU7": "lid tightener",
        "AU12": "lip corner puller (smile)",
        "AU15": "lip corner depressor (sadness)"
      },
      "posture_emotion_map": {
        "hunched_shoulders": "defensive, weary, fearful",
        "open_chest": "confident, confrontational, triumphant",
        "hand_in_pocket": "casual, hiding, avoiding",
        "arms_crossed": "guarded, defiant, cold",
        "weight_shifted": "restless, eager to leave, uncertain",
        "lean_forward": "interest, aggression, intimacy",
        "lean_away": "disgust, fear, rejection"
      },
      "arc_stages": [
        {"act": 1, "emotional_state": "weary_defensive", "visual_cues": "hunched posture, avoids eye contact, cool blue lighting"},
        {"act": 2, "emotional_state": "conflicted", "visual_cues": "restless movements, mixed warm/cool lighting"},
        {"act": 3, "emotional_state": "acceptance", "visual_cues": "upright posture, direct eye contact, warm golden lighting"}
      ],
      "outfits": [
        {"scene_range": "S01-S03", "description": "worn leather jacket, gray hoodie, dark jeans", "narrative_reason": "default everyday wear"},
        {"scene_range": "S04-S05", "description": "borrowed oversized coat, still damp from rain", "narrative_reason": "after the rain scene, someone gave her a coat"}
      ]
    }
  ]
}
```

### environments.json

```json
{
  "environments": [
    {
      "setting_key": "coffee_shop",
      "setting": "INT. COFFEE SHOP",
      "design_brief": "Cozy third-wave coffee shop with exposed brick walls, vintage pendant lights, large rain-streaked front window. Mismatched wooden furniture, chalkboard menu, espresso machine as central visual anchor. Morning light floods through east-facing window.",
      "key_props": ["espresso machine", "chalkboard menu", "rain-streaked window", "mismatched mugs"],
      "time_variations": {
        "morning": "warm golden light, dust particles, quiet atmosphere",
        "evening": "warm tungsten glow, crowded, steam from cups visible"
      },
      "lighting_scenarios": [
        {
          "scenario_id": "morning_key",
          "light_direction": "side_light_from_east_window",
          "light_quality": "soft_diffused",
          "color_temp_k": 5500,
          "light_movement": "static",
          "shadow_casting": "soft_shadows_to_west",
          "lighting_motif": "hope and exposure — the outside world enters",
          "rim_light": false
        },
        {
          "scenario_id": "evening_neon",
          "light_direction": "multiple_sources_from_street",
          "light_quality": "hard_colored",
          "color_temp_k": 3200,
          "light_movement": "flickering_neon_reflection",
          "shadow_casting": "high_contrast_colored_shadows",
          "lighting_motif": "urban loneliness — beauty and alienation coexist",
          "rim_light": true,
          "rim_light_color": "magenta"
        }
      ],
      "cultural_context": "Contemporary urban, 2020s"
    }
  ]
}
```

### color_script.json

```json
{
  "cultural_context": "western",
  "color_arc": [
    {"scene_range": "S01-S02", "dominant_color": "cool_blue_gray", "accent_color": "amber", "emotion": "weary isolation", "temperature": "cool"},
    {"scene_range": "S03-S05", "dominant_color": "muted_teal", "accent_color": "warm_orange", "emotion": "conflicted hope", "temperature": "mixed"},
    {"scene_range": "S06-S08", "dominant_color": "warm_gold", "accent_color": "deep_crimson", "emotion": "climactic confrontation", "temperature": "warm"},
    {"scene_range": "S09", "dominant_color": "soft_dawn_blue", "accent_color": "pale_yellow", "emotion": "resolution and peace", "temperature": "neutral_warm"}
  ]
}
```

### storyboard.json

```json
{
  "total_shots": 6,
  "shots": [
    {
      "shot_id": "S01-01",
      "scene_id": "S01",
      "framing": "wide",
      "function": "establishing",
      "subject": "coffee shop interior, Lin entering",
      "action": "Lin pushes open the door, morning light streams in",
      "camera_movement": "static",
      "subject_motion": "character walks forward and pushes door",
      "environment_motion": "dust particles drift in sunbeams",
      "lighting_mood": "warm morning sun, dust particles in light",
      "color_direction": {"dominant": "warm_gold", "accent": "cool_blue"},
      "axis_side": "left",
      "dialogue_ref": [],
      "duration": 4,
      "timing_style": "real_time",
      "rhythm_pattern": "4",
      "acting_beats": [
        {"start": 0.0, "end": 1.0, "beat_type": "reaction", "micro_expression": "eyebrows_raise", "body_language": "shoulders_tense"},
        {"start": 1.0, "end": 2.5, "beat_type": "suppression", "micro_expression": "forced_smile", "body_language": "hands_clench"}
      ],
      "eye_trace_in": "center",
      "eye_trace_out": "bottom_right",
      "silhouette_check": "character backlit by warm door light, strong rim separation from cool blue exterior",
      "depth_of_field": "deep_focus",
      "master_layout_anchor": false,
      "image_prompt": "Wide establishing shot, warm golden morning light streaming through glass door of cozy coffee shop. Cool blue exterior contrast. Young woman with short black hair and blue highlights, worn brown leather jacket, pushing door open. Dust particles visible in sunbeams. Anime cel-shaded style, vibrant colors, clean black outlines, Studio Ghibli-inspired background.",
      "video_prompt": "Cinematic wide establishing shot, camera static. Young woman with short black hair pushes open coffee shop door. Warm golden morning light floods in, dust particles dance in sunbeams. Cool blue exterior visible through door. She wears a worn brown leather jacket. Slow, natural walk motion. Anime cel-shaded style.",
      "audio_direction": {
        "ambience": "quiet coffee shop, distant espresso machine hiss",
        "foley": "door bell chime, door push squeak",
        "foley_key_moments": [{"timestamp": 0.5, "sound": "door_bell", "intensity": "medium", "duration": 0.8}],
        "stinger": null,
        "voice_direction": "lin: flat, minimal energy, short breaths between words",
        "music_mood": "sparse piano, melancholic",
        "silence_flag": false
      },
      "special_visual_treatment": null,
      "multi_character_strategy": null
    },
    {
      "shot_id": "S01-T01",
      "scene_id": "S01",
      "framing": "wide",
      "function": "transition",
      "transition_type": "dissolve",
      "duration": 1,
      "timing_style": "real_time",
      "rhythm_pattern": "1",
      "acting_beats": [],
      "eye_trace_in": "center",
      "eye_trace_out": "center",
      "silhouette_check": "abstract light particles, no solid subject",
      "depth_of_field": "full_blur",
      "master_layout_anchor": false,
      "image_prompt": "Soft crossfade blur, abstract light particles dissolving between warm interior and cool rain exterior",
      "video_prompt": "Smooth dissolve transition, 1 second, soft light particles drifting",
      "audio_direction": {
        "ambience": "fading interior",
        "foley": null,
        "foley_key_moments": [],
        "stinger": null,
        "voice_direction": null,
        "music_mood": "crossfade between two themes",
        "silence_flag": false
      },
      "special_visual_treatment": null,
      "multi_character_strategy": null
    }
  ]
}
```

### comic_pages.json

```json
{
  "total_pages": 2,
  "pages": [
    {
      "page_id": "P01",
      "layout": "masonry",
      "panels": [
        {
          "panel_id": "P01-01",
          "shot_id": "S01-01",
          "position": {"x": 0, "y": 0, "w": 1.0, "h": 0.35},
          "dialogue_boxes": []
        },
        {
          "panel_id": "P01-02",
          "shot_id": "S01-02",
          "position": {"x": 0, "y": 0.35, "w": 0.6, "h": 0.35},
          "dialogue_boxes": [
            {"speaker": "Lin", "line": "One black coffee, please.", "type": "spoken", "pos": "bottom-right"},
            {"speaker": "Barista", "line": "Rough night?", "type": "spoken", "pos": "top-left"}
          ]
        }
      ],
      "reading_direction": "left-to-right",
      "page_turn_type": "breath",
      "speed_lines": null,
      "sfx_typography": []
    }
  ]
}
```

### generation_log.json

```json
{
  "project": "Script Title",
  "generated_at": "2025-05-26T10:00:00Z",
  "image_model": "midjourney",
  "video_model": "runway",
  "batch_size": 5,
  "images": [
    {"shot_id": "S01-01", "status": "success", "path": "assets/images/S01-01.png", "prompt_hash": "abc123", "seed": 42, "retries": 0},
    {"shot_id": "S01-02", "status": "success", "path": "assets/images/S01-02.png", "prompt_hash": "def456", "seed": 42, "retries": 1},
    {"shot_id": "S01-03", "status": "failed", "error": "content_policy", "seed": 42, "retries": 2, "fallback": "placeholder"}
  ],
  "videos": [
    {"shot_id": "S01-01", "status": "success", "path": "assets/video/S01-01.mp4", "duration": 5}
  ]
}
```

### failed_shots.json

```json
{
  "failed_at": "2025-05-26T10:30:00Z",
  "failed_images": [
    {
      "shot_id": "S01-03",
      "original_prompt": "...",
      "simplified_prompt": "...",
      "error": "content_policy",
      "model": "midjourney",
      "seed": 42,
      "suggested_action": "Try DALL-E 3 or use placeholder panel"
    }
  ],
  "failed_videos": []
}
```

---

## Dramatic Structure Guide

### Scene Function Definitions

| Function | Purpose | Typical Pacing | Visual Signature |
|----------|---------|---------------|------------------|
| `exposition` | Establish world, characters, rules | Slow, stable | Wide shots, even lighting |
| `rising_action` | Build tension, complicate goals | Accelerating | Shorter shots, increasing contrast |
| `turning_point` | Change direction of story | Jarring | Axis break, extreme angle, color shift |
| `climax` | Peak confrontation / revelation | Fastest | Rapid cuts, maximum saturation, extreme close-ups |
| `falling_action` | Consequences unfold | Decelerating | Wider shots, softer focus |
| `resolution` | Return to equilibrium | Slowest | Stable compositions, warm/soft light |

### Three-Act Markers

- **Act 1**: Status quo → Inciting Incident → First Plot Point
- **Act 2a**: Rising action → Midpoint (false victory or false defeat)
- **Act 2b**: Complications deepen → All Is Lost → Second Plot Point
- **Act 3**: Climax → Resolution → Final Image

---

## Cinematography Reference

### Shot Function vs. Framing

A shot has two layers. `framing` is how close you are; `function` is why the shot exists.

| Function | Narrative Purpose | Typical Framing |
|----------|------------------|-----------------|
| `establishing` | Orient viewer in space | wide |
| `master` | Cover entire scene for editing safety | wide |
| `insert` | Highlight key prop / detail | close-up / extreme-close-up |
| `reaction` | Show emotional response to event | close-up |
| `pov` | Let viewer see through character's eyes | subjective framing |
| `cutaway` | Break timeline with metaphor / time jump | any |
| `transition` | Bridge scenes spatially or temporally | any |

### Camera Movement Glossary

Use these exact terms in `camera_movement`:

- **static**: no camera movement
- **push_in**: camera moves closer to subject (emphasis, revelation)
- **pull_back**: camera moves away from subject (isolation, reveal)
- **pan**: horizontal rotation (follow action, reveal space)
- **tilt**: vertical rotation (reveal height, follow vertical action)
- **track**: camera moves parallel to subject (follow walk, maintain composition)
- **dolly**: camera moves on wheels in any direction (smooth, cinematic)
- **crane**: vertical sweep (epic scale, bird's-eye)
- **handheld**: unsteady, breathing motion (documentary, urgency)
- **steadicam**: smooth floating motion (dreamlike, continuous)

### Axis Rule (180-Degree Rule)

- Draw an imaginary line between two characters facing each other.
- All shots of this interaction should stay on the same side of the line.
- Only cross the axis ("axis jump") for intentional effect: confusion, violence, power shift, or emotional rupture.
- Mark intentional axis jumps in `storyboard.json` with a note.

---

## Color Script Guide

### Building a Color Arc

1. Read all `mood` fields in `scenes.json`
2. Map moods to color temperatures:
   - Isolation / melancholy → cool blue, desaturated
   - Hope / warmth → amber, gold, soft orange
   - Danger / anger → crimson, deep red, high contrast
   - Confusion / transition → mixed warm/cool, green undertones
   - Peace / resolution → soft dawn blue, pale yellow, low saturation
3. Create a `color_arc` array showing the chromatic journey
4. For each shot, derive `color_direction` from the scene's position in the arc

### Prompt Priority for Color

Color descriptions have disproportionate impact on AI image models. Always place `color_direction` at the **start** of the image prompt:

```
[Color direction], [Subject], [Action], [Environment], [Lighting], [Style anchor]
```

Example:
```
Warm golden morning light with cool blue exterior contrast, wide shot of cozy coffee shop interior...
```

---

## Character Design Reference

### Expression Sheet Prompts

For each expression, use: `[consistency_prompt], [expression descriptor], neutral background, head-and-shoulders framing, [style anchor]`

Expression descriptors:
- **neutral**: "relaxed face, neutral mouth, calm eyes"
- **happy**: "gentle smile, slight eye crinkle, relaxed brows"
- **sad**: "downcast eyes, slight frown, drooping shoulders"
- **angry**: "furrowed brows, tight jaw, intense gaze"
- **surprised**: "wide eyes, raised brows, open mouth"
- **disgusted**: "wrinkled nose, narrowed eyes, turned-down mouth"
- **fearful**: "wide eyes with whites showing, tense mouth, raised shoulders"
- **determined**: "set jaw, focused eyes, forward lean"

### Character Arc Visualization

When generating shots across acts, reference the character's `arc_stages`:
- Act 1 shots: use posture and lighting from `arc_stages[0]`
- Act 2 shots: blend between stages or use `arc_stages[1]`
- Act 3 shots: use `arc_stages[2]`

This ensures the character's visual journey matches their emotional journey.

---

## Audio Direction Guide

### Fields

- `ambience`: Background environment sound (rain, crowd, wind, machinery)
- `foley`: Specific sound effects tied to on-screen action (footsteps, door creak, glass clink)
- `music_mood`: Emotional direction for scoring, not specific tracks — e.g., "sparse piano", "rising orchestral tension", "silent except for ambient drone"
- `silence_flag`: True if this shot should have no music and minimal ambience. Silence is a powerful dramatic tool.

### Pacing by Scene Function

| Function | Typical Duration | Audio Signature |
|----------|-----------------|-----------------|
| exposition | 4–6s | Full ambience, sparse music |
| rising_action | 2–4s | Increasing music tempo, sharper foley |
| turning_point | 3–5s | Sudden silence or music cut, jarring foley |
| climax | 1–3s | Loudest music, densest sound layer |
| falling_action | 4–6s | Music decrescendo, softer ambience |
| resolution | 5–8s | Warm music resolution, gentle ambience |

---

## Seed & Reference Strategy

### Per-Model Consistency Controls

| Model | Reference Method | Seed Control | Notes |
|-------|-----------------|--------------|-------|
| **Midjourney v6** | `--cref {url} --cw 100` | `--seed {n}` | Best character consistency. `--cw 100` locks face, hair, outfit. `--cw 0` only face. |
| **Stable Diffusion** | IP-Adapter + ControlNet | Sampler seed field | Use IP-Adapter with 4-view images. ControlNet OpenPose for pose consistency. |
| **ComfyUI** | IP-Adapter Face/Style nodes | KSampler seed | Most flexible. Chain multiple IP-Adapters for face + style + pose. |
| **DALL-E 3** | None (prompt-only) | Limited API support | Rely on hard-coded consistency prompt at prompt front. No direct reference. |
| **Gemini** | Multi-image reference in API | Limited | Pass character images as inline references in the generation call. |

### Seed Assignment Protocol

1. Assign each character a unique base seed (e.g., Lin = 42, Barista = 73)
2. For each shot featuring a character, append shot number: `seed = base_seed + shot_index`
3. On retry, always reuse the original seed
4. Log used seeds in `generation_log.json`

### Retry Ladder with Seed Preservation

```
Attempt 1: Full prompt, locked seed
  └── Success → save image
  └── Fail → Attempt 2

Attempt 2: Simplified prompt (remove 30% clauses), SAME seed
  └── Success → save image, log retry_count: 1
  └── Fail → Attempt 3

Attempt 3: Minimal prompt (color + subject + style), SAME seed
  └── Success → save image, log retry_count: 2
  └── Fail → Mark FAILED, write failed_shots.json, continue
```

---

## Prompt Engineering Templates

### Image Prompt Builder (v2 Priority Order)

```
[Color direction], [Shot function + framing], [Subject with consistency prompt], [Action], [Environment], [Lighting], [Style anchor]
```

Example:
```
Warm golden morning light with cool blue exterior contrast, wide establishing shot, young woman with short black hair and blue highlights wearing worn brown leather jacket, pushes open coffee shop door, cozy interior with dust particles in sunbeams, soft natural lighting, anime cel-shaded style, vibrant colors, clean black outlines
```

### Video Prompt Builder (Precise Motion)

Never use vague motion. Always specify: **verb + direction + magnitude + duration**.

Structure:
```
[Framing], [Subject], [subject_motion: verb + direction + magnitude], [camera_movement: verb + direction + magnitude + duration], [environment_motion], [Lighting], [Style]
```

Good examples:
- "camera slowly pushes in 20% closer to character's face over 3 seconds"
- "character turns head 45 degrees to the left, hair flows with the motion"
- "camera tracks horizontally to the right at walking pace, keeping character centered"
- "rain droplets stream down window glass, slow continuous motion"

Bad examples (never use):
- "gentle camera movement"
- "character moves"
- "smooth motion"
- "dynamic shot"

### Special Visual Treatments

For narration lines:
```
Wide establishing shot, [scene setting] in soft focus, desaturated muted tones, large elegant text box overlay area in lower third, atmospheric haze, [color_direction], [style anchor]
```

For thought lines:
```
Extreme close-up on [character]'s pensive eyes, soft vignette border, muted pastel colors, slight blur on edges, introspective mood, [color_direction], [style anchor]
```

---

## Batch Fault Tolerance Strategy

### Placeholder Policy

When a shot fails all retries:
1. Generate a text placeholder: `assets/images/{shot_id}_placeholder.txt` with descriptive caption
2. In comic layout, render as a text panel with light gray background
3. In video, skip the failed shot or hold the previous frame for its duration

### Batch Reporting Template

After each batch:
```
Batch X/Y Summary:
- Success: N images (seeds locked)
- Retried: M images (all succeeded on retry with same seed)
- Failed: K images (see failed_shots.json)
- Estimated cost: $X.XX
```

---

## SRT Subtitle Generation

### Mapping Dialogue to Timing

1. For each `spoken` dialogue line in `scenes.json`, find its linked shot via `dialogue_ref`
2. Calculate timestamp:
   - Start: shot start time + 0.5s lead-in
   - End: shot start time + shot duration - 0.5s lead-out
   - If multiple lines in one shot, divide duration evenly
3. Format as SRT:

```srt
1
00:00:01,500 --> 00:00:03,800
One black coffee, please.
```

### Multi-line Dialogue

If a single subtitle exceeds 40 characters, split into two lines:
```srt
3
00:00:10,000 --> 00:00:13,000
If only I could turn back time
and fix everything.
```

---

## Comic Page Layout

### HTML/CSS Composition (Recommended)

Use a single HTML file with CSS Grid to composite panels:

```html
<!DOCTYPE html>
<html>
<head>
<style>
  .comic-page {
    width: 1200px;
    height: 1800px;
    background: #fff;
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-template-rows: 1fr 1fr;
    gap: 8px;
    padding: 16px;
  }
  .panel {
    position: relative;
    overflow: hidden;
    border: 2px solid #000;
  }
  .panel img { width: 100%; height: 100%; object-fit: cover; }
  .dialogue-box {
    position: absolute;
    background: rgba(255,255,255,0.9);
    border: 2px solid #000;
    border-radius: 12px;
    padding: 8px 12px;
    font-family: sans-serif;
    font-size: 14px;
  }
</style>
</head>
<body>
<div class="comic-page">
  <div class="panel" style="grid-column: 1 / 3;">
    <img src="assets/images/S01-01.png" />
    <div class="dialogue-box" style="bottom: 10px; right: 10px;">One black coffee, please.</div>
  </div>
  <div class="panel">
    <img src="assets/images/S01-02.png" />
  </div>
  <div class="panel">
    <img src="assets/images/S01-03.png" />
    <div class="dialogue-box" style="top: 10px; left: 10px;">Rough night?</div>
  </div>
</div>
</body>
</html>
```

Render to PNG using Playwright or headless Chrome.

### Python Pillow Alternative

```python
from PIL import Image, ImageDraw, ImageFont

def compose_page(panels, output_path, page_size=(1200, 1800)):
    page = Image.new('RGB', page_size, 'white')
    draw = ImageDraw.Draw(page)
    for p in panels:
        img = Image.open(p['image'])
        img = img.resize((int(p['w']*page_size[0]), int(p['h']*page_size[1])))
        page.paste(img, (int(p['x']*page_size[0]), int(p['y']*page_size[1])))
        for box in p.get('dialogue_boxes', []):
            # ... render text
    page.save(output_path)
```

---

## Visual Style Presets

Present these during Stage 2. Each includes a style anchor and recommended model settings.

| Preset ID | Name | Style Anchor | Best Model |
|-----------|------|-------------|------------|
| `anime-cel` | Anime Cel-Shaded | Anime cel-shaded style, vibrant colors, clean black outlines, expressive large eyes | DALL-E 3, Midjourney --niji |
| `ghibli-soft` | Ghibli Soft | Studio Ghibli-inspired, soft pastel backgrounds, warm natural lighting, hand-painted textures | DALL-E 3, Stable Diffusion |
| `realistic-cinematic` | Realistic Cinematic | Photorealistic, cinematic color grading, shallow depth of field, dramatic lighting | Midjourney --v 6, DALL-E 3 HD |
| `ink-wash` | Ink Wash 水墨 | Traditional Chinese ink wash painting, flowing brush strokes, monochrome with subtle color accents, rice paper texture | Stable Diffusion, Gemini |
| `retro-comic` | Retro Comic | 1980s American comic book style, bold Ben-Day dots, heavy ink lines, saturated primaries | Midjourney, DALL-E 3 |
| `minimalist-geo` | Minimalist Geometric | Flat vector illustration, bold geometric shapes, limited color palette, Swiss design influence | DALL-E 3, Gemini |
| `watercolor-dream` | Watercolor Dream | Soft watercolor wash, bleeding edges, dreamy atmosphere, delicate linework | DALL-E 3, Midjourney |

---

## API Integration Patterns

### Midjourney with Character Reference

```
/imagine prompt: [image_prompt] --cref https://example.com/lin_front.png --cw 100 --seed 42 --ar 16:9
```

- `--cref URL`: character reference image
- `--cw 100`: character weight (100 = face + hair + outfit, 0 = face only)
- `--seed 42`: locked seed for consistency
- `--ar 16:9`: aspect ratio

### Stable Diffusion + IP-Adapter

```python
# Use ComfyUI or Automatic1111 with IP-Adapter extension
# Load character 4-view images into IP-Adapter Face model
# Set weight: 0.7-1.0 for strong consistency
# Lock seed in KSampler
```

### DALL-E 3 (Prompt-Only Consistency)

```python
import openai
client = openai.OpenAI(api_key="YOUR_KEY")

# DALL-E 3 does not support reference images or seed locking
# Rely entirely on hard-coded consistency prompt at prompt front

response = client.images.generate(
    model="dall-e-3",
    prompt=shot["image_prompt"],  # color direction + consistency prompt + details
    size="1792x1024",
    quality="hd",
    n=1,
)
```

### Gemini with Multi-Image Reference

```python
import google.generativeai as genai
genai.configure(api_key="YOUR_KEY")
model = genai.GenerativeModel('gemini-2.0-flash-exp-image-generation')

# Pass character reference images inline
response = model.generate_content(
    [shot["image_prompt"], character_front_image, character_expression_image],
    generation_config=genai.types.GenerationConfig(
        response_modalities=['Text', 'Image']
    )
)
```

### Runway Gen-3 (ML API)

```python
import requests
headers = {"Authorization": "Bearer YOUR_RUNWAY_KEY"}
payload = {
    "promptImage": image_url_or_base64,
    "promptText": shot["video_prompt"],  # must contain precise motion
    "duration": 5,
    "ratio": "16:9"
}
response = requests.post(
    "https://api.runwayml.com/v1/image_to_video",
    headers=headers,
    json=payload
)
```

---

## Video Post-Processing with FFmpeg

### Concatenate with Fade Transitions

Create `concat_list.txt`:
```
file 'assets/video/S01-01.mp4'
file 'assets/video/S01-02.mp4'
file 'assets/video/S01-03.mp4'
```

Simple concat:
```bash
ffmpeg -f concat -safe 0 -i concat_list.txt -c copy output_raw.mp4
```

With crossfade:
```bash
ffmpeg -i S01-01.mp4 -i S01-02.mp4 -i S01-03.mp4 \
  -filter_complex \
  "[0:v][1:v]xfade=transition=fade:duration=1:offset=4[vt1]; \
   [vt1][2:v]xfade=transition=fade:duration=1:offset=8[v]" \
  -map "[v]" -map 0:a -c:v libx264 -crf 23 -preset fast output_faded.mp4
```

Common xfade transitions: `fade`, `fadeblack`, `fadewhite`, `dissolve`, `wipeleft`, `wiperight`, `slideleft`, `slideright`.

### Burn Subtitles (SRT)

```bash
ffmpeg -i output_faded.mp4 -vf "subtitles=subtitles.srt:force_style='FontSize=24,PrimaryColour=&HFFFFFF&,OutlineColour=&H000000&,Outline=2'" -c:a copy output_subtitled.mp4
```

### Add Background Music

```bash
ffmpeg -i output_subtitled.mp4 -i bgm.mp3 -c:v copy -c:a aac -shortest -map 0:v:0 -map 1:a:0 output_with_bgm.mp4
```

### Full Pipeline

```bash
ffmpeg -f concat -safe 0 -i concat_list.txt \
  -vf "subtitles=subtitles.srt,format=yuv420p" \
  -i bgm.mp3 -shortest -map 0:v:0 -map 1:a:0 \
  -c:v libx264 -crf 23 -preset fast -c:a aac -b:a 192k \
  output_final.mp4
```

---

## Emotion-Color Mapping Reference

Use this table when building or reviewing `color_script.json`. Each emotion maps to a dominant color, accent color, and temperature. Combine emotions for layered scenes.

| Emotion | Dominant Color | Accent Color | Temperature | Usage |
|---------|---------------|--------------|-------------|-------|
| Isolation | cool blue gray | pale silver | cool | Opening, alienation |
| Melancholy | desaturated blue | soft amber | cool | Loss, memory |
| Weariness | muted gray | dusty rose | cool | Exhaustion, routine |
| Loneliness | deep indigo | cold white | cool | Solitude, night scenes |
| Hope | soft dawn blue | pale gold | neutral warm | New beginnings |
| Conflict | muted teal | warm orange | mixed | Internal struggle |
| Tension | dark charcoal | electric yellow | cool | Suspense, threat |
| Anger | deep crimson | burnt orange | warm | Rage, injustice |
| Danger | blood red | black | warm | Violence, stakes |
| Passion | rich magenta | deep purple | warm | Love, obsession |
| Joy | bright sunshine | sky blue | warm | Triumph, reunion |
| Peace | soft sage | cream | neutral | Resolution, nature |
| Nostalgia | sepia | soft pink | warm | Memory, childhood |
| Mystery | deep purple | neon green | cool | Discovery, unknown |
| Triumph | royal gold | deep crimson | warm | Victory, climax |
| Brokenness | ash gray | faded blue | cool | Defeat, grief |
| Acceptance | soft dawn blue | pale yellow | neutral warm | Healing, ending |

### Combining Emotions

When a scene contains multiple emotions, pick the **dominant** emotion for `dominant_color` and the **secondary** emotion for `accent_color`.

Example: "melancholic but hopeful" → dominant: desaturated blue, accent: pale gold.

---

## Sound Design Template Library

### Scene Function Audio Templates

Copy and adapt these templates into `audio_direction` fields.

**Exposition Template**
```json
{
  "ambience": "full environment sound, no isolation",
  "foley": "everyday sounds that establish location",
  "music_mood": "sparse, tentative, world-building",
  "silence_flag": false
}
```

**Rising Action Template**
```json
{
  "ambience": "increasingly intrusive, harder to ignore",
  "foley": "sharper, more percussive sounds",
  "music_mood": "building tension, rhythmic pulse emerging",
  "silence_flag": false
}
```

**Turning Point Template**
```json
{
  "ambience": "suddenly altered or dropped",
  "foley": "single sharp sound or unexpected silence",
  "music_mood": "sudden shift — key change, instrument drop, or complete cut",
  "silence_flag": true
}
```

**Climax Template**
```json
{
  "ambience": "overwhelming, all layers active",
  "foley": "maximum impact sounds, crashes, screams, explosions",
  "music_mood": "full orchestra or dense electronic, highest energy",
  "silence_flag": false
}
```

**Falling Action Template**
```json
{
  "ambience": "returning but changed, echoes remain",
  "foley": "debris settling, breathing, slow footsteps",
  "music_mood": "decrescendo, solo instrument, unresolved chord",
  "silence_flag": false
}
```

**Resolution Template**
```json
{
  "ambience": "gentle, restored but not identical to opening",
  "foley": "soft, rhythmic, heartbeat-like",
  "music_mood": "resolution chord, warm, fading out",
  "silence_flag": false
}
```

### Environment Ambience Quick Reference

| Location | Morning | Evening | Rain | Night |
|----------|---------|---------|------|-------|
| Coffee shop | quiet, distant espresso hiss | crowd chatter, warm | rain on glass, muffled | almost empty, refrigerator hum |
| City street | traffic builds, birds | rush hour, neon buzz | wet pavement, umbrellas | distant sirens, cat noises |
| Apartment | alarm, shower running | cooking sounds, TV | rain on AC unit | refrigerator, ticking clock |
| Forest | birds, wind in leaves | insect chorus, crackling fire | rain on leaves, mud | owls, rustling branches |

---

## Subtext Inference Guide

### Common Patterns

| Surface Text | Likely Subtext | Visual Treatment |
|-------------|----------------|------------------|
| "I'm fine." | "I am not fine. Do not ask." | Turn away, shadows on face, avoid eye contact |
| "It's nothing." | "It's everything. I'm terrified to say it." | Fidget with object, shallow depth of field |
| "You should go." | "Please stay. I can't ask you to." | Look at door, then back at person, hesitation |
| "I don't care." | "I care too much. It hurts." | Jaw clench, forced neutral expression |
| "Nice weather." | "I have nothing to say to you." | Wide empty frame, distance between characters |
| "Rough night?" | "I see your pain. I want to help." | Soft focus, warm side light, leaning in |
| "One black coffee." | "Don't talk to me. I need solitude." | Counter barrier between characters, cool light |

### Inference Rules

1. **Context first**: The same line has different subtext depending on preceding action and relationship history.
2. **Contradiction**: When body language contradicts words, subtext follows body language.
3. **Repetition**: Repeated phrases often mask escalating emotion ("I'm fine" in Act 1 vs Act 3 means different things).
4. **Silence**: What characters don't say is often more important than what they do.

### Applying Subtext to Storyboard

Once subtext is identified, modify the shot to serve the unspoken meaning:
- **Subtext of distance**: Wide shots, physical barriers, cool colors, characters on opposite sides of frame
- **Subtext of longing**: Close-ups on eyes, soft focus, warm colors, characters almost touching but not
- **Subtext of hiding**: Shadows, partial face obscured, character turned away from camera
- **Subtext of revelation**: Push-in, eye light increases, color temperature shifts warm

---

## When to Break the Rules

This Skill enforces many rules for consistency. But great art often comes from **deliberate rule-breaking**. Here's when and how to break them.

### Breaking Character Consistency

**When**: Emotional extreme moments — breakdown, epiphany, transformation.
**How**: Allow facial proportions to distort slightly, let colors bleed outside lines, exaggerate expressions beyond the expression sheet.
**Example**: In Act 3 climax, Lin's face might be drawn with larger eyes and more angular features than her neutral sheet — because she is no longer the person she was in Act 1.

### Breaking the 180-Degree Rule

**When**: Intentional disorientation — confusion, violence, power reversal, dream sequence.
**How**: Mark the axis jump clearly in `storyboard.json` with a note. Pair it with other disorienting techniques: Dutch angle, strobe lighting, sudden silence.
**Never break**: During calm dialogue scenes unless the conversation itself is a power struggle.

### Breaking the Color Script

**When**: Thematic counterpoint — showing a character's inner state contradicting the external environment.
**How**: Keep the environment in the scripted color, but bathe the character in the opposite color. Or desaturate everything except one key prop.
**Example**: A joyful wedding scene (warm gold script) where the protagonist is in cool blue — because they are miserable.

### Breaking Shot Function Templates

**When**: Subverting audience expectation — comedy, horror, or emotional whiplash.
**How**: Use an `insert` shot where an `establishing` is expected. Hold a `reaction` shot for 10 seconds. Cut to `extreme-close-up` during an exposition scene.
**Example**: During a tense negotiation, cut to an extreme close-up of a character's finger tapping — the rhythm reveals their hidden anxiety.

### Breaking Framing Conventions

**When**: Creating subjectivity or claustrophobia.
**How**: Use Dutch angles (tilted horizon) for unease. Use extreme low angles to make a character imposing. Use extreme high angles to make them powerless.

### Golden Rule

Break **one** rule at a time. If you break consistency, axis, color, and framing all in the same shot, the audience gets confused instead of moved. Breaking a rule should feel **intentional**, not **sloppy**.

---

## Composition Rules Reference

Apply these classical composition principles when writing `image_prompt` and planning `framing`.

### Rule of Thirds
Divide the frame into a 3×3 grid. Place the subject or key horizon line on the grid lines or intersections.
- **When to use**: Almost always for natural, balanced shots.
- **Prompt hint**: `"subject positioned at left third intersection, horizon on lower third line"`
- **When to break**: Symmetrical shots (temples, reflections) where centering creates power.

### Golden Ratio / Fibonacci Spiral
Place the focal point along the spiral path, with the densest detail near the spiral center.
- **When to use**: Scenes with organic flow (wind, water, hair, movement).
- **Prompt hint**: `"composition follows golden spiral, eye drawn from lower left to upper right focal point"`

### Leading Lines
Use architectural edges, roads, shadows, or gazes to direct the viewer's eye toward the subject.
- **When to use**: Establishing shots, master shots, any shot needing spatial depth.
- **Prompt hint**: `"strong diagonal leading lines from foreground pillars directing eye to subject"`

### Framing Within Frames
Place the subject inside a natural frame (window, doorway, branches, mirror).
- **When to use**: To create intimacy, voyeurism, or to separate a character from the world.
- **Prompt hint**: `"subject framed by arched stone doorway, shallow depth of field outside the frame"`

### Negative Space
Leave large areas of the frame empty to isolate the subject and create loneliness, freedom, or scale.
- **When to use**: Emotional isolation, vast landscapes, minimalist aesthetic.
- **Prompt hint**: `"subject small in lower right corner, vast empty sky occupying 70% of frame"`

### Depth Layers (Foreground / Midground / Background)
Ensure at least two of three layers have detail to create dimensional depth.
- **Prompt hint**: `"foreground: out-of-focus branches; midground: subject; background: misty mountains"`

---

## Advanced Comic Layout Modes

When assembling `comic_pages.json`, use these layout modes beyond basic grids.

### Bleed Pages
Art extends past the trim edge to the paper border.
- **Usage**: Openings, dream sequences, emotional peaks.
- **Safety**: Keep critical content 3mm inside trim; bleed art 3mm outside trim.
- **JSON flag**: `"bleed": true, "safe_zone_margin_mm": 3`

### Spread (跨页)
Two facing pages treated as one continuous canvas.
- **Usage**: Panoramic establishing shots, parallel action comparisons, time jumps.
- **Prompt hint**: `"ultra-wide panoramic composition, 2:1 aspect ratio, left half village / right half city"`
- **JSON flag**: `"type": "spread", "panels": [{"span": "left"}, {"span": "right"}]`

### Asymmetric Layouts
Panels of varying sizes create rhythm and hierarchy.
- **Usage**: Action acceleration (small → large), flashback (irregular borders), emphasis (one dominant panel).
- **Rule**: The largest panel should contain the narrative focal point; smaller panels support context.
- **Example layout**: `[1x1 large top, 1x2 small bottom-left, 1x2 small bottom-right]`

### Silent Panels (无台词画格)
Panels with no dialogue or sound effects.
- **Usage**: Let visuals breathe after dense dialogue; show time passing; build tension.
- **Rule**: Surround silent panels with thin gutters to create isolation.

### Overlay Panels (叠层画格)
A smaller panel overlaid on a larger background panel.
- **Usage**: Show memory/flashback over present action, or detail insert over wide shot.
- **JSON**: `"overlay": { "base": "scene_1A", "overlay": "scene_1B", "position": "top-right", "opacity": 1.0 }`

### Decompression vs Compression
- **Decompression**: Many panels for a brief moment (slow motion, emotional beat). Use when subtext is rich.
- **Compression**: One panel covers hours (montage, travel). Use when time must accelerate.

---

## AI Model Parameter Tuning Tables

Use these parameters when calling APIs directly or configuring generation settings in `generation_log.json`.

### Image Generation Parameters

| Parameter | Midjourney | DALL-E 3 | Stable Diffusion | Gemini |
|-----------|-----------|----------|------------------|--------|
| `--cref` | Yes (`--cref URL`) | N/A | N/A | N/A |
| `--cw` | 0–100 (100 = full) | N/A | N/A | N/A |
| `--sref` | Yes (style ref) | N/A | N/A | N/A |
| `--stylize` | 0–1000 | N/A | N/A | N/A |
| `--seed` | Yes (0–4294967295) | No | Yes | N/A |
| `--ar` | Yes (`--ar 16:9`) | N/A (edit size) | Manual | N/A |
| `CFG Scale` | N/A | N/A | 7–12 (default 7) | N/A |
| `Steps` | N/A | N/A | 20–50 | N/A |
| `Sampler` | N/A | N/A | DPM++ 2M Karras / Euler a | N/A |
| `Temperature` | N/A | N/A | N/A | 0.4–1.0 |

### Video Generation Parameters

| Parameter | Kling | Runway Gen-3 | Pika 1.5 | Veo 2 |
|-----------|-------|--------------|----------|-------|
| Duration | 5s / 10s | 5s / 10s | 3s / 5s | 5s / 8s |
| Resolution | Up to 1080p | Up to 1080p | Up to 1080p | Up to 1080p |
| Aspect Ratio | 16:9, 9:16, 1:1 | 16:9, 9:16, 1:1 | 16:9, 9:16, 1:1 | 16:9, 9:16, 1:1 |
| Motion Strength | Medium / High | Low / Med / High | 1–5 | Subtle / Moderate / Strong |
| Camera Control | Text prompt only | Text + direction | Text prompt only | Text prompt only |
| Seed | No | Yes | No | No |
| Reference Image | Yes | Yes | Yes | Yes |

### Recommended Settings by Shot Function

| Shot Function | CFG | Steps | Stylize | Motion Strength | Notes |
|---------------|-----|-------|---------|-----------------|-------|
| Establishing | 7 | 30 | 250 | Low | Maximize detail, minimize motion |
| Master | 7 | 25 | 200 | Medium | Balanced detail and motion |
| Insert | 9 | 35 | 150 | N/A (image) | High CFG for crisp detail |
| Reaction | 7 | 25 | 200 | Medium | Capture subtle facial motion |
| POV | 8 | 30 | 200 | Medium | High CFG for immersive clarity |
| Cutaway | 7 | 25 | 150 | Low | Decorative, lower stylize |
| Transition | 6 | 20 | 100 | High | Motion over detail |
| Climax | 8 | 35 | 300 | High | Max everything for impact |

### Temperature Guide for Text Prompt Refinement (LLM-assisted prompt engineering)

| Task | Temperature | Why |
|------|-------------|-----|
| Literal prompt expansion | 0.3 | Stay close to source vocabulary |
| Style rephrasing | 0.6 | Some creative synonym variation |
| Motion description generation | 0.7 | Needs fluent natural language |
| Full prompt rewriting | 0.8 | Balanced creativity and coherence |
| Experimental / wild ideas | 1.0 | Maximum divergence for inspiration |

---

## Lighting Script Guide

Light is not a byproduct of environment — it is a narrative device. Every scene should have a deliberate lighting scenario.

### Building a Lighting Scenario

For each scene, ask:
1. **What is the key light source?** (sun, lamp, fire, neon, phone screen)
2. **What does the light quality say about the world?** (soft = safe/romantic, hard = danger/truth, flickering = instability)
3. **What does the light do to the character's face?** (side light = mystery, front light = openness, under light = horror)
4. **Does the light move?** (static = stability, sweeping = search, flickering = anxiety)

### Lighting Motif Examples

| Motif | Light Behavior | Emotional Meaning |
|-------|---------------|-------------------|
| "The Last Window" | Single warm light source, rest in shadow | Hope in despair |
| "Interrogation" | Hard overhead light, deep eye shadows | Truth forced out |
| "Phone Glow" | Cool blue face light in dark room | Isolation, digital escape |
| "Neon Baptism" | Colored light flooding character | Transformation, city consumes |
| "Fading Candle" | Light slowly dims across scene | Death, loss, time running out |

---

## Depth of Field Narrative Guide

Depth of field is psychological distance made visible.

| DOF Strategy | Narrative Effect | When to Use |
|--------------|-----------------|-------------|
| Deep focus (f/8–f/16) | Character and environment equally important | Power dynamics, environmental storytelling |
| Shallow focus (f/1.4–f/2.8) | Subject isolated, world dissolves | Intimacy, obsession, mental prison |
| Rack focus | Shift attention from A to B | Revelation, discovery, threat emergence |
| Tilt-shift (miniature) | World feels like toy/model | Detachment, nostalgia, omniscience |
| Bokeh shapes | Background lights become pattern | Dreaminess, urban romance, intoxication |

### Prompt Hints for DOF

- Deep focus: `"deep focus, everything sharp from foreground to background"`
- Shallow focus: `"shallow depth of field, creamy bokeh background, subject isolated"`
- Rack focus: `"rack focus from background to foreground subject"` (note: AI video models may not handle this well; plan as two separate shots)

---

## Eye Trace Design

The viewer's eye should travel smoothly from shot to shot. Violent eye jumps create fatigue; smooth eye traces create hypnosis.

### Rules

1. **Adjacent shots**: The interest point of shot N should be within 1/3 frame width of shot N+1's interest point.
2. **Action direction**: If a character looks left in shot A, show what they see in shot B with the subject positioned on the right (creating a visual line across the cut).
3. **Motion continuation**: If an object moves top-to-bottom in shot A, it should enter shot B from the top.

### Eye Trace Annotation

In `storyboard.json`, use `"eye_trace_in"` and `"eye_trace_out"` with values:
- `top_left`, `top_center`, `top_right`
- `center_left`, `center`, `center_right`
- `bottom_left`, `bottom_center`, `bottom_right`
- `subject_eyes`, `subject_hand`, `prop_focal`

### Smoothing Violent Jumps

When a jump is unavoidable:
- Insert a **motion blur bridge** or **light flash**
- Use a **whip pan** transition
- Place a **bright element** at the destination point to attract the eye

---

## Silhouette Value & Rim Light

If the audience can't identify the character by silhouette alone, the shot fails.

### Silhouette Check Protocol

For every shot, verify:
1. Can the character's pose be read as a black shape against a white background?
2. Is there sufficient brightness contrast between subject and background?
3. Do key props (weapon, pendant, hat) extend the silhouette for identification?

### Rim Light Deployment

When subject and background are similar in value:
- Add `"rim light"` to the prompt: `"strong rim light separating character from dark background"`
- Specify rim color: `"warm gold rim light"` or `"cool blue rim light"`
- Rim light motivation: always motivated by a light source in the scene (window, lamp, explosion)

### AI Prompt Insurance

Always append to character shots:
```
strong silhouette, clear readable pose, rim light separating subject from background
```

---

## Multi-Character Consistency Strategies

AI image/video models cannot reliably maintain multiple distinct character identities in a single generation. Here are proven workarounds.

### Strategy 1: Layered Compositing (Recommended)

Generate separately, composite in post:
1. Generate background plate with no characters
2. Generate character A in pose against green/gray screen (or with alpha if model supports)
3. Generate character B in pose against green/gray screen
4. Composite in Photoshop / After Effects / Blender

**Pros**: Perfect consistency, full control over interaction
**Cons**: Requires post-production skill, no natural shadow interaction

### Strategy 2: Occlusion & Evasion

Design shots to avoid multi-character front-facing interaction:
- **Over-shoulder**: Show character A's shoulder in foreground (blurred), character B in focus
- **POV chain**: A looks at B → B's reaction (never both in frame together)
- **Reflection**: One character in mirror, other in real space
- **Silhouette**: Secondary character as silhouette or shadow
- **Split screen**: Divide frame with architecture (door frame, window pane)

### Strategy 3: Master-Extra Hierarchy

If two characters must interact:
- Lock all consistency resources on the **protagonist** (seed, cref, IP-Adapter)
- Let the **secondary character** be less consistent — back to camera, in shadow, motion-blurred, or generic

### Strategy 4: EbSynth Style Propagation

For video sequences:
1. Generate a perfect keyframe with both characters (manual compositing or luck)
2. Use EbSynth to propagate the style to adjacent frames
3. Manually fix drift frames

### Honest Limitation Note

As of 2026, no AI video model reliably maintains two distinct character faces across motion. Do not promise users seamless multi-character dialogue scenes without post-production compositing.

---

## Post-Production & Repair (Stage 5b)

AI-generated video requires repair before release. This is not optional.

### Common Defects & Fixes

| Defect | Cause | Fix Tool | Fix Method |
|--------|-------|----------|------------|
| Flickering | Frame-to-frame color/noise variance | DaVinci Resolve "Temporal NR" | Apply temporal noise reduction, strength 20–40 |
| Morphing | Character face/body drifts between frames | EbSynth + manual keyframes | Generate perfect keyframes, propagate style, fix drift |
| Face崩坏 | AI loses facial structure in motion | FaceFusion / Rope | Detect bad face frames, replace with generated still face |
| Color inconsistency | Same scene shifts hue across shots | DaVinci Resolve Color Match | Use color chart or pick stable reference frame |
| Jittery motion | AI generates unstable camera motion | After Effects "Warp Stabilizer" | Subspace warp, smoothness 10–30% |
| Ghosting | Moving objects leave trails | Topaz Video AI | Deinterlace + enhance motion clarity |

### Recommended Post-Production Chain

```
Raw AI clips
  → Concatenate with transitions (FFmpeg xfade)
  → Color grade for consistency (DaVinci Resolve)
  → Stabilize motion (After Effects / DaVinci)
  → Face repair (FaceFusion on bad frames)
  → Flicker removal (DaVinci Temporal NR)
  → Subtitle burn (FFmpeg)
  → BGM mix (DaVinci / Audition)
  → Export final
```

### Post-Production Plan Template

Save as `post_production_plan.json`:

```json
{
  "stages": [
    {"stage": "concat", "tool": "ffmpeg", "status": "pending"},
    {"stage": "color_grade", "tool": "davinci_resolve", "reference_shot": "S01-01", "status": "pending"},
    {"stage": "stabilize", "tool": "after_effects", "shots": ["S02-03", "S04-01"], "status": "pending"},
    {"stage": "face_repair", "tool": "facefusion", "shots": ["S03-02"], "status": "pending"},
    {"stage": "flicker_fix", "tool": "davinci_resolve", "status": "pending"},
    {"stage": "subtitle_burn", "tool": "ffmpeg", "status": "pending"},
    {"stage": "bgm_mix", "tool": "audition", "status": "pending"}
  ]
}
```

---

## Master Shot & Spatial Coherence

Every scene needs a spatial anchor. Without it, characters teleport and rooms reshape themselves.

### Master Layout Shot Protocol

1. For each scene, designate one shot as `"master_layout_anchor": true`
2. This shot must show the **entire space** and **all character positions**
3. Write a `"spatial_description"` field: 50 words describing room dimensions, furniture placement, door positions, window locations
4. All subsequent shots in the scene must reference this spatial description

### Spatial Coherence Checklist

Before generating shots in a scene, verify:
- [ ] Door is on the same wall in all shots
- [ ] Light source direction is consistent
- [ ] Character A is always to the left of Character B (per axis)
- [ ] Props don't disappear or change position
- [ ] Background elements (paintings, clocks, plants) are stable

### Prompt Enforcement

Append to every shot prompt in the scene:
```
Spatial context: [room dimensions], [key furniture positions], [light source location]
```

---

## Comic Grammar: Speed Lines & SFX Typography

Comic is not film. It has its own visual language.

### Speed Lines (集中線 / 速度線)

| Type | Visual | Usage | Prompt Hint |
|------|--------|-------|-------------|
| Radial (集中線) | Lines radiating from center | Shock, realization, focus | `"radial speed lines converging on character's face"` |
| Parallel (速度線) | Horizontal/angled streaks | Motion, speed, action | `"parallel speed lines behind running character"` |
| Turbulent (渦巻き線) | Spiral / vortex | Chaos, confusion, psychic power | `"turbulent spiral lines around character"` |
| Streamline (流線) | Smooth curved lines | Wind, water, graceful motion | `"elegant streamline curves following hair and cloth"` |

### Sound Effect Typography (擬音 / 擬態語)

SFX text is not caption — it is part of the image.

| Sound | Western Style | Manga Style | Font Direction |
|-------|--------------|-------------|----------------|
| Impact | CRASH, BOOM | ドカーン, ゴゴゴ | Bold, jagged, explosive shape |
| Slice | SLASH, SWISH | ザシュッ, スパッ | Sharp, diagonal, thin strokes |
| Heartbeat | THUMP-THUMP | ドクン, ドクン | Pulsing, rounded, expanding |
| Silence | ... | シーン... | Thin, fading, small |
| Wind | WHOOOSH | ビュオオ | Wavy, horizontal stretch |

### SFX Placement Rules

1. Never cover a character's eyes or the key action
2. SFX should "point" toward the sound source
3. SFX size = sound intensity (whisper = small, explosion = page-spanning)
4. Use SFX to fill negative space and balance composition

---

## Page Turn Reveal Design

The page turn is a comic's most powerful cut. Design it deliberately.

### Page Turn Types

| Type | Right Page Last Panel | Left Page First Panel | Effect |
|------|----------------------|----------------------|--------|
| `cliffhanger` | Question, threat, discovery | Does NOT answer immediately | Forces reader to turn |
| `reveal` | Mysterious silhouette or close-up | Full reveal of identity/event | Satisfying payoff |
| `transition` | Calm scene ending | New location/time begins | Breather, reset |
| `breath` | Dense action peak | Empty space or silent panel | Emotional recovery |

### Designing the Turn

1. The right page's last panel should create **narrative tension** (not just visual beauty)
2. The gutter between right and left pages is a **time gap** — use it
3. After a cliffhanger turn, delay the answer by 1–2 panels to build suspense
4. Never put essential dialogue on the turn gutter (it gets lost in the spine)

---

## Cultural Color Context

Color emotion is not universal. Adapt `color_script.json` to your audience's cultural context.

### Color Meaning by Culture

| Color | Western Context | East Asian Context | When to Override |
|-------|----------------|-------------------|------------------|
| White | Purity, wedding | Death, mourning | Funerals in Asia → cool gray, not white |
| Red | Danger, love, passion | Luck, celebration, revolution | Weddings in China → red dominant, not white |
| Gold | Wealth, greed, success | Imperial, divine, prosperity | Triumph scenes across cultures → gold is safe |
| Black | Evil, death, elegance | Mystery, water (五行), solemnity | Villain design: black works globally |
| Yellow | Cowardice, caution | Royalty, sacred (Buddhism), pornography | Caution in Western UI → yellow; sacred in temples → yellow |
| Green | Nature, envy, go | Growth, harmony, infidelity (historical) | Nature scenes → green is universal; jealousy varies |
| Purple | Royalty, luxury, magic | Spirituality, mourning (Thailand) | Luxury branding → purple; Thai funeral → avoid purple |
| Blue | Trust, calm, sadness | Healing, immortality, villainy (historical) | Corporate trust → blue; healing → blue |

### Implementation

In `color_script.json`:
```json
{
  "cultural_context": "east_asian",
  "color_arc": [...]
}
```

When `cultural_context` is set, the prompt builder auto-adjusts color language:
- `east_asian`: red = celebration, white = solemn, gold = divine
- `western`: white = purity, black = death, purple = royalty
- `custom`: user-defined mapping in `color_cultural_map` field

---

## Reference Board System

Before generating, collect visual references. This prevents "prompt hallucination" where the AI invents details you didn't intend.

### Reference Board Structure

Create `references/` folder:

```
references/
├── mood_board/
│   ├── atmosphere_01.jpg      # General mood reference
│   ├── lighting_ref_01.jpg    # Specific lighting you want
│   └── color_palette.png      # Extracted color palette image
├── style_board/
│   ├── target_artist_01.jpg   # Target style reference
│   ├── target_artist_02.jpg
│   └── composition_ref.jpg    # Specific composition you want to echo
├── animatic/
│   ├── scene_01_timed.mp4     # Rough motion reference (even phone recording)
│   └── scene_02_keyposes.png  # Hand-drawn pose sheet
└── ref_index.json             # Index linking references to shots
```

### ref_index.json Schema

```json
{
  "boards": [
    {
      "board_id": "mood_rainy_night",
      "type": "mood",
      "files": ["references/mood_board/atmosphere_01.jpg"],
      "linked_shots": ["S02-01", "S02-02", "S02-03"],
      "notes": "Blade Runner rainy street mood, neon reflections on wet pavement"
    }
  ]
}
```

### Usage in Prompts

When a shot has linked references, prepend to prompt:
```
Style reference: [style_board description]. Mood reference: [mood_board description].
```

For Midjourney `--sref`, pass style board images:
```
/imagine prompt: [prompt] --sref https://.../style_ref.jpg --sw 200
```

---

*Reference Version: 2.2.0 | Aligns with SKILL.md v2.1.0*
