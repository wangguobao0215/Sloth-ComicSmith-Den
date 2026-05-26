# Templates

Preset style and color packages for quick project initialization.

## Usage

Copy a template's `color_script.json` into your project directory after `init_project.py`:

```bash
cp templates/cyberpunk-neon/color_script.json my_project/color_script.json
```

## Available Templates

| Template | Style | Mood | Best For |
|----------|-------|------|----------|
| `cyberpunk-neon` | Cyberpunk, neon lighting, high contrast | Dystopian, urban, tech-noir | Sci-fi, action, conspiracy |
| `ghibli` | Studio Ghibli inspired, soft natural lighting | Warm, whimsical, emotional | Fantasy, coming-of-age, nature |
| `noir` | Film noir, B&W, dramatic shadows | Cynical, tense, mysterious | Crime, thriller, detective |
| `manga-ink` | Black & white manga, heavy inking | Dynamic, stark, high energy | Action, horror, classic manga |

## Creating Your Own Template

1. Create a new directory under `templates/{your-name}/`
2. Add a `color_script.json` with your color arc
3. Optionally add `environments.json` and `characters.json` snippets
4. Update this README
