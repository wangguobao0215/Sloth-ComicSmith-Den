# Sloth-ComicSmith-Den — Examples

## Example 1: Short Scene — "The Coffee Shop"

### Input Script

```markdown
# The Coffee Shop

INT. COFFEE SHOP — MORNING

Lin pushes open the door. Morning light floods the room. She looks like she hasn't slept.

LIN
One black coffee, please.

The BARISTA, a friendly middle-aged woman, notices the bags under Lin's eyes.

BARISTA
Rough night?

Lin manages a half-smile.

LIN
You could say that.

NARRATOR (V.O.)
The rain outside matched her mood.

LIN (V.O.)
If only I could turn back time...

She takes her coffee and sits by the window, staring at the rain outside.
```

### Stage 1 Output: scenes.json

```json
{
  "title": "The Coffee Shop",
  "language": "en",
  "total_scenes": 1,
  "dramatic_structure": {
    "inciting_incident": null,
    "midpoint": null,
    "climax": null,
    "all_is_lost": null
  },
  "scenes": [
    {
      "scene_id": "S01",
      "act_position": "act_1",
      "scene_function": "exposition",
      "setting": "INT. COFFEE SHOP — MORNING",
      "setting_zh": "内景 咖啡店 — 早晨",
      "characters": ["Lin", "Barista"],
      "action": "Lin enters a coffee shop looking tired. She orders coffee. The barista notices her exhaustion. Lin sits by the window watching rain.",
      "dialogue": [
        {"speaker": "Lin", "line": "One black coffee, please.", "type": "spoken", "subtext": "Don't talk to me."},
        {"speaker": "Barista", "line": "Rough night?", "type": "spoken", "subtext": "Another exhausted customer."},
        {"speaker": "Lin", "line": "You could say that.", "type": "spoken", "subtext": "I'm not ready to share."},
        {"speaker": "Narrator", "line": "The rain outside matched her mood.", "type": "narration", "subtext": null},
        {"speaker": "Lin", "line": "If only I could turn back time...", "type": "thought", "subtext": "I regret what happened yesterday."}
      ],
      "mood": "melancholic, weary, introspective"
    }
  ]
}
```

### Stage 2 Output: characters.json

```json
{
  "visual_style_anchor": "Anime cel-shaded style, soft pastel backgrounds, expressive character designs, warm indoor lighting",
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
        "hair": "short black hair with subtle blue highlights",
        "eyes": "amber, tired-looking",
        "clothing": "worn brown leather jacket, gray hoodie, dark jeans"
      },
      "personality": ["reserved", "weary", "dry humor"],
      "props": ["old notebook in jacket pocket"],
      "consistency_prompt": "Young woman, 28, short black hair with subtle blue highlights, amber tired-looking eyes, slender build. Wearing a worn brown leather jacket over a gray hoodie and dark jeans. Reserved weary expression with a hint of dry humor. Old notebook visible in jacket pocket. Anime cel-shaded style, soft pastel backgrounds, expressive character designs, warm indoor lighting.",
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
        "forced_smile": "mouth smiles but eyes remain flat, tension at jaw corners",
        "gaze_aversion": "eyes dart downward and to the side, shame or hiding",
        "lip_tremble": "lower lip quivers slightly, on the edge of tears",
        "jaw_clench": "masseter muscle tightens, suppressed anger or resolve"
      },
      "posture_emotion_map": {
        "hunched_shoulders": "defensive, weary, fearful",
        "open_chest": "confident, confrontational",
        "lean_forward": "interest, intimacy, aggression",
        "lean_away": "disgust, rejection, fear"
      },
      "arc_stages": [
        {"act": 1, "emotional_state": "weary_defensive", "visual_cues": "hunched posture, avoids eye contact, cool blue lighting"},
        {"act": 2, "emotional_state": "conflicted", "visual_cues": "restless movements, mixed warm/cool lighting"},
        {"act": 3, "emotional_state": "acceptance", "visual_cues": "upright posture, direct eye contact, warm golden lighting"}
      ],
      "outfits": [
        {"scene_range": "S01", "description": "worn leather jacket, gray hoodie, dark jeans", "narrative_reason": "default everyday wear"}
      ]
    }
  ]
}
```

### Stage 2 Output: color_script.json

```json
{
  "color_arc": [
    {"scene_range": "S01", "dominant_color": "cool_blue_gray", "accent_color": "amber", "emotion": "weary isolation", "temperature": "cool"}
  ]
}
```

### Stage 2 Output: environments.json

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
        }
      ],
      "cultural_context": "Contemporary urban, 2020s"
    }
  ]
}
```

### Stage 3 Output: storyboard.json (excerpt)

```json
{
  "total_shots": 7,
  "shots": [
    {
      "shot_id": "S01-01",
      "scene_id": "S01",
      "framing": "wide",
      "function": "establishing",
      "subject": "coffee shop interior, Lin entering",
      "action": "Lin pushes open the door, morning light streams in",
      "camera_movement": "static",
      "subject_motion": "character walks forward and pushes door open",
      "environment_motion": "dust particles drift in sunbeams",
      "lighting_mood": "warm golden morning sun, dust particles",
      "color_direction": {"dominant": "warm_gold", "accent": "cool_blue"},
      "axis_side": "left",
      "dialogue_ref": [],
      "duration": 4,
      "timing_style": "real_time",
      "rhythm_pattern": "4",
      "acting_beats": [
        {"start": 0.0, "end": 0.8, "beat_type": "reaction", "micro_expression": "eyebrows_raise", "body_language": "shoulders_tense"},
        {"start": 0.8, "end": 2.5, "beat_type": "suppression", "micro_expression": "forced_smile", "body_language": "hands_clench"}
      ],
      "eye_trace_in": "center",
      "eye_trace_out": "bottom_right",
      "silhouette_check": "character backlit by warm door light, strong rim separation from cool blue exterior",
      "depth_of_field": "deep_focus",
      "master_layout_anchor": true,
      "image_prompt": "Warm golden morning light with cool blue exterior contrast, wide establishing shot, young woman with short black hair and blue highlights wearing worn brown leather jacket, pushes open coffee shop door, cozy interior with dust particles in sunbeams, soft natural lighting, strong silhouette, clear readable pose, rim light separating subject from background, anime cel-shaded style, vibrant colors, clean black outlines",
      "video_prompt": "Cinematic wide establishing shot, camera static. Young woman with short black hair pushes open coffee shop door. Warm golden morning light floods in, dust particles dance in sunbeams. Cool blue exterior visible through door. She wears a worn brown leather jacket. Slow natural walk motion. Anime cel-shaded style.",
      "audio_direction": {
        "ambience": "quiet coffee shop, distant espresso machine hiss",
        "foley": "door bell chime, door push squeak",
        "foley_key_moments": [{"timestamp": 0.5, "sound": "door_bell", "intensity": "medium", "duration": 0.8}],
        "stinger": null,
        "voice_direction": null,
        "music_mood": "sparse piano, melancholic",
        "silence_flag": false
      },
      "special_visual_treatment": null,
      "multi_character_strategy": null
    },
    {
      "shot_id": "S01-02",
      "scene_id": "S01",
      "framing": "medium",
      "function": "master",
      "subject": "Lin at counter, Barista behind",
      "action": "Lin orders coffee, Barista looks at her with concern",
      "camera_movement": "static",
      "subject_motion": "character leans slightly on counter, barista turns to face",
      "environment_motion": "steam rising from espresso machine",
      "lighting_mood": "warm overhead lighting, soft shadows",
      "color_direction": {"dominant": "warm_gold", "accent": "amber"},
      "axis_side": "left",
      "dialogue_ref": ["One black coffee, please.", "Rough night?"],
      "duration": 5,
      "timing_style": "real_time",
      "rhythm_pattern": "5",
      "acting_beats": [
        {"start": 0.0, "end": 1.5, "beat_type": "reaction", "micro_expression": "gaze_aversion", "body_language": "hunched_shoulders"},
        {"start": 1.5, "end": 3.0, "beat_type": "decision", "micro_expression": "forced_smile", "body_language": "lean_forward"}
      ],
      "eye_trace_in": "bottom_right",
      "eye_trace_out": "center_left",
      "silhouette_check": "both characters clearly separated by warm overhead light",
      "depth_of_field": "deep_focus",
      "master_layout_anchor": false,
      "image_prompt": "Warm golden overhead lighting, medium master shot, young woman with short black hair and blue highlights wearing worn brown leather jacket leans on coffee counter, middle-aged barista with curly gray-brown bun and green apron turns to face her with concerned expression, steam rising from espresso machine, strong silhouette, clear readable pose, anime cel-shaded style, soft pastel backgrounds, expressive character designs",
      "video_prompt": "Cinematic medium master shot, camera static. Young woman with short black hair leans on coffee counter. Middle-aged barista with curly bun turns to face her with concerned motherly expression. Steam rises from espresso machine. Warm coffee shop lighting. Anime cel-shaded style.",
      "audio_direction": {
        "ambience": "coffee shop chatter, espresso machine",
        "foley": "cup placed on saucer, steam hiss",
        "foley_key_moments": [{"timestamp": 2.0, "sound": "cup_on_saucer", "intensity": "soft", "duration": 0.5}],
        "stinger": null,
        "voice_direction": "lin: flat, minimal energy, short breaths between words; barista: warm, maternal, slightly slower pace",
        "music_mood": "sparse piano continues",
        "silence_flag": false
      },
      "special_visual_treatment": null,
      "multi_character_strategy": "occlusion"
    },
    {
      "shot_id": "S01-03",
      "scene_id": "S01",
      "framing": "close-up",
      "function": "reaction",
      "subject": "Lin's half-smile",
      "action": "Lin smiles wearily",
      "camera_movement": "static",
      "subject_motion": "character's mouth forms small half-smile, eyes soften slightly",
      "environment_motion": null,
      "lighting_mood": "soft side light from window",
      "color_direction": {"dominant": "warm_gold", "accent": "soft_pink"},
      "axis_side": "left",
      "dialogue_ref": ["You could say that."],
      "duration": 3,
      "timing_style": "held_frame",
      "rhythm_pattern": "3",
      "acting_beats": [
        {"start": 0.0, "end": 0.5, "beat_type": "reaction", "micro_expression": "forced_smile", "body_language": "shoulders_drop"},
        {"start": 0.5, "end": 2.0, "beat_type": "suppression", "micro_expression": "gaze_aversion", "body_language": "hand_clenches_pocket"}
      ],
      "eye_trace_in": "center_left",
      "eye_trace_out": "center",
      "silhouette_check": "character face clearly separated from warm bokeh background by rim light",
      "depth_of_field": "shallow_focus",
      "master_layout_anchor": false,
      "image_prompt": "Soft side light from window, close-up reaction shot, young woman with short black hair and blue highlights, amber tired eyes, small weary half-smile, warm bokeh background, shallow depth of field, strong rim light separating face from background, anime cel-shaded style, soft pastel backgrounds",
      "video_prompt": "Close-up reaction shot, camera static. Young woman with short black hair gives a small weary half-smile. Soft side light from window creates gentle shadows on face. Subtle eye movement. Held frame for 2.5 seconds. Anime cel-shaded style.",
      "audio_direction": {
        "ambience": "quiets slightly",
        "foley": null,
        "foley_key_moments": [],
        "stinger": null,
        "voice_direction": "lin: flat, dry, slight pause before 'could'",
        "music_mood": "piano pauses, single sustained note",
        "silence_flag": false
      },
      "special_visual_treatment": null,
      "multi_character_strategy": null
    },
    {
      "shot_id": "S01-04",
      "scene_id": "S01",
      "framing": "wide",
      "function": "establishing",
      "subject": "rain-streaked window, coffee shop interior",
      "action": "Narration overlay, rain outside matches mood",
      "camera_movement": "static",
      "subject_motion": "character sits still by window, back to camera",
      "environment_motion": "rain droplets stream down window glass",
      "lighting_mood": "cool blue-gray exterior light, warm interior contrast",
      "color_direction": {"dominant": "cool_blue_gray", "accent": "warm_gold"},
      "axis_side": "neutral",
      "dialogue_ref": ["The rain outside matched her mood."],
      "duration": 4,
      "image_prompt": "Cool blue-gray exterior with warm gold interior contrast, wide establishing shot through rain-streaked coffee shop window, blurred silhouette of young woman with short black hair sitting inside, rain droplets on glass, desaturated muted tones with atmospheric haze, text overlay area in lower third, anime cel-shaded style, soft pastel backgrounds",
      "video_prompt": "Wide establishing shot, camera static, viewed through rain-streaked window. Blurred silhouette of young woman with short black hair sits inside coffee shop. Rain droplets stream down glass. Cool blue exterior, warm interior glow. Slow continuous rain motion. Anime cel-shaded style.",
      "audio_direction": {
        "ambience": "rain on glass, distant traffic",
        "foley": null,
        "music_mood": "music drops out, ambient drone only",
        "silence_flag": false
      },
      "special_visual_treatment": "narration"
    },
    {
      "shot_id": "S01-05",
      "scene_id": "S01",
      "framing": "extreme-close-up",
      "function": "insert",
      "subject": "Lin's eyes, pensive gaze",
      "action": "Inner monologue, introspective moment",
      "camera_movement": "static",
      "subject_motion": "slow blink, eyes shift slightly off-frame",
      "environment_motion": null,
      "lighting_mood": "soft vignette, muted colors",
      "color_direction": {"dominant": "muted_pastel", "accent": "soft_blue"},
      "axis_side": "neutral",
      "dialogue_ref": ["If only I could turn back time..."],
      "duration": 3,
      "image_prompt": "Muted pastel colors with soft blue accent, extreme close-up insert shot on young woman's amber tired eyes, looking off-frame with pensive distant gaze, soft vignette border, slight blur on edges, introspective mood, shallow depth of field, anime cel-shaded style, soft pastel backgrounds",
      "video_prompt": "Extreme close-up insert shot, camera static. Amber tired eyes look off-frame with pensive distant gaze. Slow blink. Soft vignette, muted pastel tones. Subtle breathing motion. Anime cel-shaded style.",
      "audio_direction": {
        "ambience": "fades to near silence",
        "foley": null,
        "music_mood": null,
        "silence_flag": true
      },
      "special_visual_treatment": "thought"
    },
    {
      "shot_id": "S01-T01",
      "scene_id": "S01",
      "framing": "wide",
      "function": "transition",
      "transition_type": "dissolve",
      "duration": 1,
      "image_prompt": "Soft crossfade blur, abstract light particles dissolving between warm interior and cool rain exterior",
      "video_prompt": "Smooth dissolve transition, 1 second, soft light particles drifting between scenes"
    }
  ]
}
```

### Stage 4: Batch Generation with Seed Locking

```
Model: Midjourney v6
Character seed (Lin): 42
Reference: --cref assets/characters/Lin/front.png --cw 100

Batch 1/2 Summary:
- Success: 3 images (S01-01, S01-02, S01-03) — all with seed 42 + shot_index
- Retried: 1 image (S01-04, succeeded on retry with simplified prompt, same seed 45)
- Failed: 1 image (S01-05, content_policy — see failed_shots.json)
- Estimated cost: $0.42
```

`failed_shots.json`:
```json
{
  "failed_at": "2025-05-26T10:30:00Z",
  "failed_images": [
    {
      "shot_id": "S01-05",
      "original_prompt": "Muted pastel colors with soft blue accent, extreme close-up insert shot on young woman's amber tired eyes...",
      "simplified_prompt": "Close-up portrait of a young woman's eyes, muted pastel colors, anime style",
      "error": "content_policy",
      "model": "midjourney",
      "seed": 47,
      "suggested_action": "Try DALL-E 3 or use placeholder text panel"
    }
  ]
}
```

### Stage 4b: Comic Page Layout

`comic_pages.json`:
```json
{
  "total_pages": 1,
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
        },
        {
          "panel_id": "P01-03",
          "shot_id": "S01-03",
          "position": {"x": 0.6, "y": 0.35, "w": 0.4, "h": 0.35},
          "dialogue_boxes": [
            {"speaker": "Lin", "line": "You could say that.", "type": "spoken", "pos": "bottom-center"}
          ]
        },
        {
          "panel_id": "P01-04",
          "shot_id": "S01-04",
          "position": {"x": 0, "y": 0.7, "w": 0.5, "h": 0.3},
          "dialogue_boxes": [
            {"speaker": "Narrator", "line": "The rain outside matched her mood.", "type": "narration", "pos": "bottom-center"}
          ]
        },
        {
          "panel_id": "P01-05",
          "shot_id": "S01-05",
          "position": {"x": 0.5, "y": 0.7, "w": 0.5, "h": 0.3},
          "dialogue_boxes": [
            {"speaker": "Lin", "line": "If only I could turn back time...", "type": "thought", "pos": "top-center", "style": "italic-cloud"}
          ]
        }
      ],
      "reading_direction": "left-to-right"
    }
  ]
}
```

### Stage 5: Subtitle SRT Output

```srt
1
00:00:00,500 --> 00:00:02,800
One black coffee, please.

2
00:00:03,200 --> 00:00:04,800
Rough night?

3
00:00:05,500 --> 00:00:06,800
You could say that.
```

---

## Example 2: Multi-Scene Script with Dramatic Structure

For a 3-act script with 9 scenes:

1. **Stage 1** identifies `inciting_incident` at S03, `midpoint` at S05, `climax` at S08, `all_is_lost` at S07.
2. **Stage 2** generates color_arc: cool blue (Act 1) → mixed teal/orange (Act 2) → warm gold/crimson (Act 3 climax) → soft dawn blue (resolution).
3. **Stage 3** applies pacing templates:
   - Act 1 scenes: stable, 4-6s durations, establishing shots
   - Act 2a: accelerating, 2-4s, more close-ups
   - Midpoint (S05): axis jump, jarring angle, color shift
   - Act 2b: increasingly claustrophobic framing
   - Climax (S08): rapid 1-2s cuts, extreme close-ups, maximum saturation
   - Resolution (S09): wide shots, 5-8s, soft warm light
4. **Stage 4** locks seeds per character across all acts for consistency.
5. **Stage 5** uses precise motion descriptions per shot function.

---

## Example 3: Precise Motion Descriptions

### Good (use these)

| Shot Function | Video Prompt Motion Description |
|--------------|--------------------------------|
| establishing | "camera static, no movement, hold frame for 4 seconds" |
| push_in | "camera slowly pushes in 20% closer to character's face over 3 seconds" |
| reaction | "camera static, character's eyes widen slightly, head tilts 5 degrees left" |
| track | "camera tracks horizontally to the right at walking pace, keeping character centered in frame" |
| transition | "smooth dissolve, 1 second, soft light particles drift across frame" |

### Bad (never use)

- "gentle camera movement"
- "character moves"
- "smooth motion"
- "dynamic shot"
- "cinematic feel"

---

## Example 4: Three-Act Structure — "The Last Train"

This example demonstrates how dramatic structure, color arc, character arc, and pacing templates work together across a 9-scene short script.

### Input Script (Abbreviated)

```markdown
# The Last Train

SCENE 1 — MORNING, BEDROOM
MAYA (28, software engineer) stares at her phone. A text: "Project canceled. Team dissolved."

SCENE 2 — NOON, CAFETERIA
Maya's colleague JASON tries to cheer her up. She brushes him off.

SCENE 3 — DUSK, TRAIN STATION
Maya sees an old woman struggling with luggage. She helps. The woman thanks her warmly.

SCENE 4 — NIGHT, TRAIN INTERIOR
Maya sits alone. She opens her laptop and starts writing — not code, but a story.

SCENE 5 — MIDNIGHT, TRAIN PASSING A CITY
Maya looks out at the city lights. She smiles for the first time.

SCENE 6 — PRE-DAWN, TRAIN RESTAURANT CAR
Jason appears — he followed her. "I quit too," he says. "Want to build something weird?"

SCENE 7 — DAWN, TRAIN APPROACHING COAST
Maya stares at the ocean through the window. She doesn't answer. She doesn't need to.

SCENE 8 — SUNRISE, COASTAL PLATFORM
Maya and Jason step off the train. Golden light everywhere.

SCENE 9 — MORNING, BEACH
Maya opens her laptop on a driftwood log. Types the first line of her novel.
```

### Stage 1: Dramatic Structure

```json
{
  "title": "The Last Train",
  "language": "en",
  "total_scenes": 9,
  "dramatic_structure": {
    "inciting_incident": "S01",
    "midpoint": "S05",
    "climax": "S07",
    "all_is_lost": "S02"
  },
  "scenes": [
    {"scene_id": "S01", "act_position": "act_1", "scene_function": "exposition", "mood": "shocked, numb"},
    {"scene_id": "S02", "act_position": "act_1", "scene_function": "exposition", "mood": "defensive, isolated"},
    {"scene_id": "S03", "act_position": "act_1", "scene_function": "rising_action", "mood": "tentative, warm"},
    {"scene_id": "S04", "act_position": "act_2a", "scene_function": "rising_action", "mood": "focused, hopeful"},
    {"scene_id": "S05", "act_position": "act_2a", "scene_function": "turning_point", "mood": "joyful, liberated"},
    {"scene_id": "S06", "act_position": "act_2b", "scene_function": "rising_action", "mood": "surprised, conflicted"},
    {"scene_id": "S07", "act_position": "act_2b", "scene_function": "climax", "mood": "triumphant, silent"},
    {"scene_id": "S08", "act_position": "act_3", "scene_function": "falling_action", "mood": "peaceful, golden"},
    {"scene_id": "S09", "act_position": "act_3", "scene_function": "resolution", "mood": "acceptance, quiet"}
  ]
}
```

### Stage 2: Color Script

```json
{
  "color_arc": [
    {"scene_range": "S01-S02", "dominant_color": "cool_blue_gray", "accent_color": "electric_yellow", "emotion": "shocked isolation", "temperature": "cool"},
    {"scene_range": "S03-S04", "dominant_color": "muted_teal", "accent_color": "warm_orange", "emotion": "tentative hope", "temperature": "mixed"},
    {"scene_range": "S05", "dominant_color": "bright_sunshine", "accent_color": "sky_blue", "emotion": "joyful liberation", "temperature": "warm"},
    {"scene_range": "S06", "dominant_color": "rich_magenta", "accent_color": "deep_purple", "emotion": "surprised passion", "temperature": "warm"},
    {"scene_range": "S07", "dominant_color": "royal_gold", "accent_color": "deep_crimson", "emotion": "triumphant silence", "temperature": "warm"},
    {"scene_range": "S08-S09", "dominant_color": "soft_dawn_blue", "accent_color": "pale_gold", "emotion": "peaceful acceptance", "temperature": "neutral_warm"}
  ]
}
```

### Stage 2: Character Arc (Maya)

```json
{
  "arc_stages": [
    {"act": 1, "emotional_state": "shocked_defensive", "visual_cues": "hunched over phone, cool overhead light, avoiding eye contact"},
    {"act": 2, "emotional_state": "tentatively_hopeful", "visual_cues": "sitting upright by window, mixed warm/cool light, focused gaze"},
    {"act": 3, "emotional_state": "liberated_accepting", "visual_cues": "open posture facing sunrise, warm golden backlight, direct eye contact"}
  ]
}
```

### Stage 3: Pacing by Scene Function

| Scene | Function | Duration Base | Shot Count | Framing Bias |
|-------|----------|--------------|------------|-------------|
| S01 | exposition | 5-6s | 3 | wide, medium |
| S02 | exposition | 4-5s | 3 | medium, close-up |
| S03 | rising_action | 4-5s | 4 | medium, insert |
| S04 | rising_action | 3-4s | 4 | close-up, insert |
| S05 | turning_point | 6s | 2 | wide, extreme-close-up |
| S06 | rising_action | 4-5s | 4 | medium, reaction |
| S07 | climax | 8s | 2 | wide, extreme-close-up |
| S08 | falling_action | 5-6s | 3 | wide, medium |
| S09 | resolution | 7-8s | 2 | wide, insert |

Notice: The climax (S07) uses only **2 shots** but holds them for **8 seconds total** — a long wide shot of the ocean, then an extreme close-up of Maya's eyes. No rapid cuts. The tension is in the silence, not the editing.

### Stage 3: Axis & Shot Function Example (S06)

```json
{
  "shot_id": "S06-01",
  "framing": "medium",
  "function": "master",
  "camera_movement": "static",
  "axis_side": "left",
  "color_direction": {"dominant": "rich_magenta", "accent": "deep_purple"},
  "duration": 4,
  "audio_direction": {
    "ambience": "train rattle, distant conversation",
    "foley": "door sliding open, footsteps approaching",
    "music_mood": "sustained string note, held breath",
    "silence_flag": false
  }
},
{
  "shot_id": "S06-02",
  "framing": "close-up",
  "function": "reaction",
  "camera_movement": "static",
  "axis_side": "left",
  "color_direction": {"dominant": "rich_magenta", "accent": "warm_gold"},
  "duration": 3,
  "audio_direction": {
    "ambience": "train rattle fades slightly",
    "foley": null,
    "music_mood": "music drops out",
    "silence_flag": true
  }
}
```

### Rule-Breaking Moment (S07)

The climax intentionally **breaks the color script**: Maya is bathed in cool dawn blue while the world around her is warm gold. This visual counterpoint signals that her internal state (calm clarity) now contrasts with the external chaos she has escaped.

In `storyboard.json`, this is marked:
```json
{
  "shot_id": "S07-02",
  "special_notes": "COLOR_SCRIPT_BREAK: Character in cool blue against warm gold environment. Intentional counterpoint for thematic clarity."
}
```

---

## Example 5: When to Break Consistency

In a hypothetical Act 3 breakdown scene for Lin (from Example 1):

**Normal consistency prompt**: "Young woman, 28, short black hair with blue highlights, amber eyes..."

**Broken consistency prompt for breakdown shot**: "Young woman, 28, short black hair with blue highlights, face distorted by grief, eyes larger than normal proportions, tears streaming, mouth open in silent scream. Anime cel-shaded style but lines are rougher, colors bleed outside edges."

The break is **intentional, singular, and narrative-driven**. It returns to normal consistency in the next shot.

---

## Example 6: v2.1 Advanced Features — "The Rain Room"

This example demonstrates the v2.1 features added after the designer assessment: acting beats, lighting script, eye trace, silhouette checks, comic page turn design, post-production plan, and cultural color context.

### Input Script

```markdown
# The Rain Room

INT. SMALL APARTMENT — NIGHT

Rain hammers the window. MIRA (30s) sits on the floor, surrounded by unpacked moving boxes. She holds a framed photo.

MIRA
(whisper)
You said you'd be here.

She looks at the empty bed. Back to the photo.

MIRA
I moved the bed. Like you asked.

Lightning flashes. For one second, the room is silver-white. Mira doesn't flinch.

MIRA
I'm not scared of storms anymore.

She places the photo face-down. Stands. Walks to the window.

MIRA
I'm scared of the quiet after.

The rain slows. She rests her forehead against the glass.
```

### Stage 2: characters.json (v2.1 Micro-Expressions)

```json
{
  "characters": [
    {
      "name": "Mira",
      "micro_expression_sheet": {
        "forced_calm": "relaxed mouth but micro-tremor at lower lip, eyes too still",
        "gaze_detach": "eyes focused on middle distance, not seeing the room",
        "nostril_flare_controlled": "controlled rage, breathing constrained",
        "single_tear_hold": "tear collects but does not fall, held by will"
      },
      "posture_emotion_map": {
        "sitting_floor": "defeated, childlike, groundless",
        "forehead_glass": "surrender, exhaustion, seeking cold comfort",
        "standing_from_floor": "decision, resolve, refusing to stay down"
      }
    }
  ]
}
```

### Stage 2: environments.json (Lighting Script)

```json
{
  "environments": [
    {
      "setting_key": "mira_apartment",
      "design_brief": "Small studio apartment, unpacked boxes, single bed, rain-streaked window facing alley. Cluttered but not messy — life interrupted.",
      "lighting_scenarios": [
        {
          "scenario_id": "night_rain",
          "light_direction": "back_light_from_window",
          "light_quality": "hard_colored",
          "color_temp_k": 7000,
          "light_movement": "flickering_street_lamp_through_rain",
          "shadow_casting": "long_sharp_shadows_across_floor",
          "lighting_motif": "external chaos illuminates internal stillness",
          "rim_light": true,
          "rim_light_color": "cool_silver"
        },
        {
          "scenario_id": "lightning_flash",
          "light_direction": "omnidirectional_white",
          "light_quality": "hard_instant",
          "color_temp_k": 9000,
          "light_movement": "single_instant_burst_then_dark",
          "shadow_casting": "frozen_hard_shadow_for_one_frame",
          "lighting_motif": "truth revealed in a split second",
          "rim_light": false
        }
      ]
    }
  ]
}
```

### Stage 2: color_script.json (Cultural Context)

```json
{
  "cultural_context": "western",
  "color_arc": [
    {"scene_range": "S01", "dominant_color": "deep_indigo", "accent_color": "cold_white", "emotion": "grief in solitude", "temperature": "cool"}
  ]
}
```

### Stage 3: storyboard.json (Acting Beats + Eye Trace + Silhouette)

```json
{
  "total_shots": 4,
  "shots": [
    {
      "shot_id": "S01-01",
      "framing": "wide",
      "function": "establishing",
      "duration": 5,
      "timing_style": "real_time",
      "rhythm_pattern": "5-3-4-6",
      "acting_beats": [
        {"start": 0.0, "end": 1.0, "beat_type": "reaction", "micro_expression": "gaze_detach", "body_language": "sitting_floor"},
        {"start": 1.0, "end": 3.0, "beat_type": "suppression", "micro_expression": "forced_calm", "body_language": "shoulders_drop"}
      ],
      "eye_trace_in": "center",
      "eye_trace_out": "bottom_left",
      "silhouette_check": "Mira's hunched shape readable against window light, photo frame creates distinct silhouette extension",
      "depth_of_field": "deep_focus",
      "master_layout_anchor": true,
      "image_prompt": "Deep indigo night with cold white accents, wide establishing shot, woman sitting on floor surrounded by moving boxes, rain-streaked window behind her, cool silver rim light separating her from dark room, strong silhouette, clear readable pose, anime cinematic style, moody atmospheric lighting",
      "video_prompt": "Camera static wide shot. Woman sits on floor surrounded by boxes. Rain streams down window behind her. Cool silver rim light creates strong silhouette. Flickering street lamp light through rain. Slow breathing motion. Anime cinematic style.",
      "audio_direction": {
        "ambience": "heavy rain on glass, distant thunder rumble",
        "foley": "cardboard box settling, photo frame tap",
        "foley_key_moments": [{"timestamp": 0.2, "sound": "photo_tap", "intensity": "soft", "duration": 0.3}],
        "stinger": null,
        "voice_direction": "mira: whisper, breathy, barely audible",
        "music_mood": "sparse ambient drone, no melody",
        "silence_flag": false
      },
      "multi_character_strategy": null
    },
    {
      "shot_id": "S01-02",
      "framing": "close-up",
      "function": "insert",
      "duration": 3,
      "timing_style": "held_frame",
      "acting_beats": [
        {"start": 0.0, "end": 1.5, "beat_type": "realization", "micro_expression": "nostril_flare_controlled", "body_language": "thumb_rubs_photo_edge"},
        {"start": 1.5, "end": 2.5, "beat_type": "decision", "micro_expression": "single_tear_hold", "body_language": "jaw_sets"}
      ],
      "eye_trace_in": "bottom_left",
      "eye_trace_out": "center",
      "silhouette_check": "hands and photo frame have strong contrast against dark clothing",
      "depth_of_field": "shallow_focus",
      "master_layout_anchor": false,
      "image_prompt": "Cold white accent on deep indigo, extreme close-up of hands holding framed photo, shallow depth of field, thumb rubbing frame edge, tear forming but not falling, strong rim light on knuckles, anime cinematic style",
      "video_prompt": "Extreme close-up on hands holding photo frame. Thumb slowly rubs edge. Single tear forms but does not fall. Held frame for 2 seconds. Shallow focus. Anime cinematic style.",
      "audio_direction": {
        "ambience": "rain muffles slightly",
        "foley": "thumb rubbing glass frame",
        "foley_key_moments": [{"timestamp": 1.0, "sound": "glass_rub", "intensity": "very_soft", "duration": 1.0}],
        "stinger": null,
        "voice_direction": null,
        "music_mood": "single piano note, held",
        "silence_flag": false
      }
    },
    {
      "shot_id": "S01-03",
      "framing": "medium",
      "function": "reaction",
      "duration": 4,
      "timing_style": "staccato",
      "acting_beats": [
        {"start": 0.0, "end": 0.2, "beat_type": "reaction", "micro_expression": "forced_calm", "body_language": "body_tenses"},
        {"start": 0.2, "end": 0.5, "beat_type": "release", "micro_expression": "gaze_detach", "body_language": "shoulders_drop"}
      ],
      "eye_trace_in": "center",
      "eye_trace_out": "top_right",
      "silhouette_check": "lightning flash freezes silhouette clearly against white room",
      "depth_of_field": "deep_focus",
      "master_layout_anchor": false,
      "image_prompt": "Omnidirectional cold white lightning burst, medium shot woman on floor, room illuminated silver-white for one instant, hard frozen shadows, her face caught between fear and calm, anime cinematic style, high contrast",
      "video_prompt": "Medium shot, woman on floor. Lightning flashes — room turns silver-white for one instant. Her face caught between fear and calm. Then back to darkness. Staccato timing. Anime cinematic style.",
      "audio_direction": {
        "ambience": "rain cuts out for split second",
        "foley": null,
        "foley_key_moments": [],
        "stinger": {"timestamp": 0.2, "sound": "thunder_crack", "intensity": "maximum", "duration": 0.5},
        "voice_direction": null,
        "music_mood": "complete silence during flash",
        "silence_flag": true
      }
    },
    {
      "shot_id": "S01-04",
      "framing": "close-up",
      "function": "reaction",
      "duration": 6,
      "timing_style": "slow_motion",
      "acting_beats": [
        {"start": 0.0, "end": 2.0, "beat_type": "suppression", "micro_expression": "single_tear_hold", "body_language": "forehead_glass"},
        {"start": 2.0, "end": 5.0, "beat_type": "release", "micro_expression": "forced_calm", "body_language": "eyes_close"}
      ],
      "eye_trace_in": "top_right",
      "eye_trace_out": "center",
      "silhouette_check": "forehead and nose pressed against glass create strong profile silhouette",
      "depth_of_field": "shallow_focus",
      "master_layout_anchor": false,
      "image_prompt": "Soft cool blue with pale gold accent, close-up profile of woman pressing forehead against rain-streaked window, shallow depth of field, rain droplets in sharp focus on glass, her face softly blurred behind, single tear finally falls, anime cinematic style, melancholic beauty",
      "video_prompt": "Slow motion close-up profile. Woman presses forehead against rain-streaked window. Rain droplets slide down glass in slow motion. Single tear falls down her cheek. Eyes close slowly. Anime cinematic style.",
      "audio_direction": {
        "ambience": "rain slows to gentle patter",
        "foley": "breath fogging glass",
        "foley_key_moments": [{"timestamp": 3.0, "sound": "tear_drop", "intensity": "soft", "duration": 0.5}],
        "stinger": null,
        "voice_direction": "mira: final line delivered on exhale, no force left",
        "music_mood": "ambient drone resolves to single warm chord",
        "silence_flag": false
      }
    }
  ]
}
```

### Stage 4: comic_pages.json (Page Turn Reveal)

```json
{
  "total_pages": 2,
  "pages": [
    {
      "page_id": "P01",
      "layout": "asymmetric",
      "panels": [
        {"panel_id": "P01-01", "shot_id": "S01-01", "position": {"x": 0, "y": 0, "w": 1.0, "h": 0.5}},
        {"panel_id": "P01-02", "shot_id": "S01-02", "position": {"x": 0, "y": 0.5, "w": 0.6, "h": 0.5}},
        {"panel_id": "P01-03", "shot_id": "S01-03", "position": {"x": 0.6, "y": 0.5, "w": 0.4, "h": 0.5}}
      ],
      "reading_direction": "left-to-right",
      "page_turn_type": "cliffhanger",
      "speed_lines": null,
      "sfx_typography": [
        {"text": "CRACK", "style": "bold_jagged", "position": "top_right", "panel_id": "P01-03"}
      ]
    },
    {
      "page_id": "P02",
      "layout": "masonry",
      "panels": [
        {"panel_id": "P02-01", "shot_id": "S01-04", "position": {"x": 0, "y": 0, "w": 1.0, "h": 1.0}}
      ],
      "reading_direction": "left-to-right",
      "page_turn_type": "reveal",
      "speed_lines": {"type": "streamline", "direction": "vertical", "intensity": "subtle"},
      "sfx_typography": [
        {"text": "tap... tap...", "style": "thin_fading", "position": "bottom_center", "panel_id": "P02-01"}
      ]
    }
  ]
}
```

- **P01** ends with the lightning flash (`cliffhanger`) — the reader must turn the page to see the aftermath.
- **P02** begins with the slow-motion tear reveal (`reveal`) — the turn pays off the tension built on P01.

### Stage 5b: post_production_plan.json

```json
{
  "stages": [
    {"stage": "concat", "tool": "ffmpeg", "status": "completed"},
    {"stage": "color_grade", "tool": "davinci_resolve", "reference_shot": "S01-01", "status": "pending", "notes": "Match all shots to S01-01 cool indigo temperature"},
    {"stage": "stabilize", "tool": "after_effects", "shots": ["S01-04"], "status": "pending", "notes": "Slow-motion shot has micro-jitter from AI generation"},
    {"stage": "face_repair", "tool": "facefusion", "shots": ["S01-02"], "status": "pending", "notes": "Extreme close-up has eye asymmetry on frame 12"},
    {"stage": "flicker_fix", "tool": "davinci_resolve", "status": "pending", "notes": "S01-03 lightning flash causes 2-frame color jump"},
    {"stage": "subtitle_burn", "tool": "ffmpeg", "status": "pending"},
    {"stage": "bgm_mix", "tool": "audition", "status": "pending", "notes": "Layer ambient drone + piano + rain. Duck music during silence_flag shots."}
  ]
}
```

### Key v2.1 Takeaways

1. **Acting beats** turn a static "she looks sad" into a 3-second micro-performance with specific facial muscle and posture changes.
2. **Lighting scenarios** treat light as narrative — the lightning flash is not "bright light" but "truth revealed in a split second."
3. **Eye trace** ensures the reader's gaze flows from the photo (P01-02) to the lightning (P01-03) to the window (P02-01) without visual whiplash.
4. **Page turn design** uses the physical boundary of the page as a dramatic tool, not just a layout constraint.
5. **Post-production plan** acknowledges AI limitations upfront and schedules repair work before the deadline.
