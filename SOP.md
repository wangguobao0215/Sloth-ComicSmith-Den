# 深匠绘 · 实际操作 SOP

> 从零开始，用 30 分钟跑完一个完整漫画/视频项目的完整操作手册。

---

## 准备阶段（5 分钟）

### 1. 确认你的剧本

找一个 300-800 字的小故事，或者自己写一个。下面是一个可以直接复制的测试剧本：

```markdown
# 雨夜便利店

内景 便利店 — 深夜

林推门而入，雨水顺着她的伞滴落在地板上。她看上去已经三天没睡了。

林
一包烟，最便宜的。

店员是个五十多岁的大叔，头也不抬地指了指货架。

店员
货架第三排，自己拿。

林走到货架前，却没有拿烟。她盯着窗外的大雨发呆。

林（内心独白）
如果昨天我没有上那辆车...

店员抬起头，看了她一眼。

店员
小姑娘，雨一时半会儿停不了。

林苦笑了一下，从口袋里掏出一枚硬币放在柜台上。

林
那...给我一把伞吧。

店员递给她一把透明雨伞。林撑开伞，走进雨里。

店员（对着她的背影）
明天见。

林停下脚步，没有回头，只是轻轻点了点头，然后消失在雨幕中。
```

把上面这段保存为 `rainy_store.txt`。

### 2. 确认你的预算模式

根据你的 API 预算选择模式：

| 模式 | 成本 | 输出 | 适合谁 |
|------|------|------|--------|
| **storyboard_only** | ¥0 | 专业分镜稿 PDF | 零预算、想先试流程 |
| **key_shots_only** | ¥5-15 | 关键镜头图 + 分镜稿 | 低预算、想做概念展示 |
| **full** | ¥30-100+ | 全量图 + 视频 | 有预算、追求完整输出 |

**建议第一次用 `storyboard_only`，先跑通流程。**

### 3. 确认 API Key（如选 full/key_shots_only 模式）

- **图像生成**（必选）：OpenAI (DALL-E 3)、Midjourney、Stability AI 或 Gemini Image 任选一个
- **视频生成**（可选）：Kling、Runway、Pika 或 Veo

如果只有免费选项：用 **Gemini Image**（免费额度约 60 张/天）+ **本地 SDXL**（需 8GB+ 显存）。

---

## 第一阶段：初始化项目（2 分钟）

```bash
# 1. 进入脚本目录
cd Sloth-ComicSmith-Den/scripts

# 2. 初始化项目
python3 init_project.py rainy_store

# 你会看到：
# [OK] Created project: rainy_store
# [OK] Created 10 JSON templates
```

生成的项目结构：
```
rainy_store/
├── scenes.json
├── characters.json
├── environments.json
├── color_script.json
├── storyboard.json
├── generation_log.json
├── failed_shots.json
├── post_production_plan.json
├── batch_plan.json
├── cost_estimate.json
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
    ├── images/
    ├── comic-pages/
    └── video/
```

---

## 第二阶段：剧本预处理（1 分钟，可选）

如果你的剧本不是标准格式（比如上面的小说是 prose 格式），先标准化：

```bash
python3 preprocess_script.py ../rainy_store.txt --type auto --output ../rainy_store_standardized.txt
```

如果剧本已经是分场景格式（有"内景/外景"标注），可以跳过这步。

---

## 第三阶段：与 AI 协作完成各阶段

### Stage 1 — 剧本解析

把 `rainy_store.txt` 的内容复制粘贴给 QoderWork（或你使用的 AI 助手），然后说：

> "请按 Sloth-ComicSmith-Den 的 Stage 1 流程，解析这个剧本，输出 scenes.json。"

AI 会输出一个 JSON。把它保存到 `rainy_store/scenes.json`。

**验证**：
```bash
python3 validate_project.py ../rainy_store
```

### Stage 2 — 世界观设计

继续对 AI 说：

> "基于上面的 scenes.json，请执行 Stage 2：生成 characters.json、environments.json、color_script.json。"

**如果你选了 storyboard_only 模式**：
- 不需要 API key
- AI 会输出纯文本的 JSON 结构
- 保存到对应文件即可

**如果你选了 full/key_shots_only 模式**：
- 给 AI 你的 API key
- AI 会调用图像 API 生成角色四视图和表情表
- 图片自动保存到 `assets/characters/`

**快速应用模板**（可选）：
```bash
# 比如想做成赛博朋克风格
cp ../templates/cyberpunk-neon/color_script.json ../rainy_store/color_script.json
```

### Stage 3 — 分镜生成

> "请基于 scenes.json 和 characters.json，执行 Stage 3，输出 storyboard.json。"

AI 会为每个场景生成 3-6 个镜头的分镜。

**关键检查点**：
- 确认每个镜头的 `function`（establishing/master/close-up 等）是否合理
- 确认 `axis_side` 没有跳轴
- 确认 `color_direction` 符合 color_script.json 的色彩弧线

### Stage 3.5 — 快速验证（强烈推荐）

**如果是 full/key_shots_only 模式**：

> "请从 storyboard.json 中选一个 establishing shot 和一个 close-up shot，生成测试图。"

AI 生成 2 张测试图，保存到 `rainy_store/test_images/`。

**检查**：
- 角色长相是否一致？
- 风格是否符合预期？
- 如果不对：调整 `visual_style_anchor` 或 `consistency_prompt`，重新生成

**成本估算**：
```bash
python3 cost_estimator.py ../rainy_store --mode key_shots_only
# 输出示例：
# [MODE: key_shots_only] Generating 4/12 shots
# TOTAL                                    0.80
# With 20% retry buffer                    0.96
```

### Stage 4 — 图像生成（如选 full/key_shots_only 模式）

> "请基于确认的 storyboard.json，执行 Stage 4，生成所有图像。"

AI 会：
1. 按 batch 生成（每批 5-8 张）
2. 自动记录到 `generation_log.json`
3. 失败的保存到 `failed_shots.json`

**风格漂移检查**（生成过程中或生成后）：
```bash
python3 check_style_drift.py ../rainy_store --threshold 0.3
```

**如果发现漂移**：
```bash
# 保存当前状态
python3 snapshot.py ../rainy_store --message "before style fix"

# 调整风格
python3 switch_style.py ../rainy_store --preset ghibli

# 重新生成漂移的图
```

### Stage 5 — 视频合成（可选，如选 full 模式）

> "请基于生成的图像，执行 Stage 5，输出视频片段。"

**注意**：视频生成成本高（$0.2-0.5/5秒），且角色一致性不保证。建议：
- 只把 climax 和 transition 镜头做成视频
- 其他用静态图 + 缓慢缩放（Ken Burns 效果）

### Stage 5b — 输出成品

**快速路径（推荐）**：
```bash
# 自动生成带转场和字幕的最终视频
python3 compile_video.py ../rainy_store --transition fade --bgm ../your_music.mp3

# 输出：rainy_store/output_final.mp4
```

**专业路径**（如需要调色/修复）：
- 用 DaVinci Resolve 导入 `assets/video/`
- 参考 `post_production_plan.json` 逐项修复

---

## 第四阶段：漫画排版（可选）

如果你想输出漫画页而不是视频：

> "请基于 storyboard.json，执行漫画排版，输出 comic_pages.json。"

AI 会：
1. 把镜头按 3-6 个一组分页
2. 设计每页的 `page_turn_type`（悬念/揭示/过渡/喘息）
3. 标注 speed_lines 和 sfx_typography 位置

**手动合成**：
- 目前需要手动把 `assets/images/` 里的图放入排版模板
- 或用 Pillow 脚本自动裁切对齐（后续版本会提供自动化脚本）

---

## 完整命令速查表

```bash
# 初始化
python3 init_project.py my_project

# 剧本预处理（非标准格式时）
python3 preprocess_script.py input.txt --type auto

# 成本估算
python3 cost_estimator.py my_project --mode storyboard_only
python3 cost_estimator.py my_project --mode key_shots_only
python3 cost_estimator.py my_project --mode full

# 校验
python3 validate_project.py my_project

# 自动生成色彩脚本
python3 generate_color_script.py my_project

# 轴线检查
python3 check_axis.py my_project

# 风格漂移检查
python3 check_style_drift.py my_project --threshold 0.3

# 快照（实验前保存状态）
python3 snapshot.py my_project --message "before style change"

# 风格切换
python3 switch_style.py my_project --preset ghibli
python3 switch_style.py my_project --custom "Oil painting style"

# 批量规划
python3 batch_planner.py my_project

# 导出 prompts
python3 storyboard_to_prompts.py my_project --format csv

# SRT 字幕生成
python3 srt_generator.py my_project

# 一键编译视频
python3 compile_video.py my_project --transition fade --bgm music.mp3
```

---

## 常见问题 FAQ

### Q1: 我没有 API key，能跑吗？
**能。** 选 `storyboard_only` 模式。输出是专业的分镜稿（scenes.json + storyboard.json + shot_list.md），可以直接交给画师或作为创作参考。

### Q2: 生成到一半发现风格不对怎么办？
```bash
# 1. 保存快照
python3 snapshot.py my_project --message "before redo"

# 2. 切换风格
python3 switch_style.py my_project --preset anime-cel

# 3. 重新生成（只需重新跑 Stage 4）
```

### Q3: 角色脸崩了怎么修？
- **静态图**：用 Midjourney 的 `--cref` 重新生成，或手动在 Photoshop 中替换
- **视频**：目前无自动化方案。建议接受一定漂移，或用 `compile_video.py` 快速出片后手动替换关键帧

### Q4: 我想做连载漫画，角色一致性怎么保证？
**诚实回答**：当前 AI 无法保证跨集角色 100% 一致。建议：
1. 锁定 seed 和 consistency_prompt
2. 每集开头重新生成一张角色 reference 图
3. 用 `check_style_drift.py` 监控漂移
4. 关键镜头（封面、climax）人工精修

### Q5: 整个流程要多久？
| 模式 | AI 协作时间 | 等待生成时间 | 总耗时 |
|------|------------|-------------|--------|
| storyboard_only | 20-30 分钟 | 0 | **20-30 分钟** |
| key_shots_only | 20-30 分钟 | 5-10 分钟 | **30-40 分钟** |
| full (静态图) | 20-30 分钟 | 20-40 分钟 | **1-1.5 小时** |
| full (含视频) | 20-30 分钟 | 1-3 小时 | **2-4 小时** |

---

## 下一步建议

1. **第一次跑**：用上面的「雨夜便利店」剧本，选 `storyboard_only` 模式，20 分钟跑完流程
2. **第二次跑**：同一个剧本，选 `key_shots_only`，体验图像生成
3. **第三次跑**：换你自己的剧本，选 `full` 模式，完整体验
4. **进阶**：阅读 `references/ASSESSMENT_PLAYER.md` 了解骨灰级玩家的踩坑经验

---

*SOP 版本：v2.2.0*
*最后更新：2026-05-26*
