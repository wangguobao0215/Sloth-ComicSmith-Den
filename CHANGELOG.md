# Changelog

## [2.2.0] - 2026-05-26

### 玩家评估报告优化（按骨灰级玩家反馈逐一修复）

#### P0 级：防止弃坑

- **诚实前置 AI 限制**：Prerequisites 新增 ⚠️ Honest Limitations 章节，明确告知 AI 视频角色一致性无法保证、10 分钟视频预估成本 $50-200
- **预算模式**：新增 `full` / `key_shots_only` / `storyboard_only` 三种预算模式，storyboard_only 零 API 成本输出专业分镜稿
- **Stage 3.5 快速验证**：新增 Validate & Preview 阶段，先生成 1-2 张测试图确认风格和角色后再投入完整生产
- **Stage 5b 重构**：改为「可选高级工作流」，提供 FFmpeg-only 快速编译路径（`scripts/compile_video.py`）和专业修复路径两套方案
- **成本估算器升级**：`scripts/cost_estimator.py` 支持 `--mode` 参数（full/key_shots_only/storyboard_only），自动输出 `cost_estimate.json`

#### P1 级：提升体验

- **风格一致性检查**：新增 `scripts/check_style_drift.py`，对比生成图与 style board 的色彩直方图差异，超出阈值时报警
- **项目快照**：新增 `scripts/snapshot.py`，支持 git commit 或 zip 存档，实验前一键保存状态
- **风格切换**：新增 `scripts/switch_style.py`，支持 8 种预设（anime-cel/ghibli/noir/cyberpunk-neon 等）一键切换，无需重新解析剧本
- **未来兼容标记**：`acting_beats`、`micro_expression`、`action_units_facs` 明确标注为 🔮 Future-proof 字段，当前仅作人类参考

#### P2 级：扩展能力

- **剧本预处理**：新增 `scripts/preprocess_script.py`，自动识别 screenplay / novel / dialogue_only / outline 四种格式并标准化
- **共享模板**：新增 `templates/` 目录，内置 cyberpunk-neon、ghibli、noir、manga-ink 四种风格模板

#### P3 级：锦上添花

- **AI 模型评测矩阵**：`reference.md` 新增 Midjourney/DALL-E/SDXL/Flux/Gemini/Kling/Runway 七模型横评表，含角色一致性、动漫风格、多角色同框、成本等维度

---

## [2.1.1] - 2026-05-26

### 品牌重命名

- 中文品名从「匠漫」升级为「深匠绘 · 剧本到漫画视频流水线」
- `SKILL.md`：更新 `description_zh` 与 H1 标题
- `README.md`：更新 H1 标题，新增「## 品名释义」章节，阐释「深」「匠」「绘」三字含义
- `README_EN.md`：标题嵌入中文品名，格式为 `Sloth-ComicSmith-Den — 深匠绘 · Script to Comic/Video Pipeline`

## [2.1.0] - 2026-05-26

### 新增（资深动漫设计师评估后优化）

- **表演节拍系统**：storyboard 增加 `acting_beats` 数组，支持 reaction / realization / decision / suppression / release 五种节拍，含微表情与肢体语言标注
- **时间节奏脚本**：新增 `timing_style`（real_time / slow_motion / held_frame / staccato）与 `rhythm_pattern` 时长比例描述
- **微表情与肢体语言数据库**：characters.json 扩展 `micro_expression_sheet`、`action_units_facs`、`posture_emotion_map`
- **光影脚本**：environments.json 新增 `lighting_scenarios`，将光提升为一级叙事元素（方向、质感、色温、运动、阴影、主题、轮廓光）
- **景深叙事指导**：新增 `depth_of_field` 字段（deep_focus / shallow_focus / rack_focus / full_blur），按镜头功能推荐策略
- **视线轨迹设计**：新增 `eye_trace_in` / `eye_trace_out`，控制观众 gaze 在镜头间的流动
- **剪影价值检查**：新增 `silhouette_check`，强制在 prompt 中附加轮廓光保险
- **多角色同框一致性策略**：新增 `multi_character_strategy`（layered_composite / occlusion / master_extra / ebsynth），诚实标注 AI 当前技术限制
- **后期修复策略（Stage 5b）**：新增 `post_production_plan.json`，涵盖闪烁修复、面部修复、运动稳定、色彩匹配、音频分层
- **主镜头锚定策略**：新增 `master_layout_anchor`，确保整场戏空间坐标一致
- **速度线与拟声词排版**：comic_pages.json 新增 `speed_lines` 与 `sfx_typography`，支持集中线/速度线/涡卷线/流线及拟音字体设计
- **翻页悬念设计**：comic_pages.json 新增 `page_turn_type`（cliffhanger / reveal / transition / breath）
- **文化语境色彩映射**：color_script.json 新增 `cultural_context`（western / east_asian / custom），自动调整色彩象征意义
- **参考板机制**：新增 `references/` 目录结构（mood_board / style_board / animatic）与 `ref_index.json`
- **声音设计深化**：audio_direction 新增 `foley_key_moments`（精确拟音事件）、`stinger`（戏剧重音）、`voice_direction`（配音指导）

### 脚本工具更新

- `init_project.py`：升级至 v2.1，新增 `post_production_plan.json`、`references/ref_index.json` 模板
- `validate_project.py`：升级至 v2.1，验证所有新增可选字段（acting_beats、timing_style、lighting_scenarios 等）

## [2.0.0] - 2026-05-26

### 新增

- **戏剧结构分析**：Stage 1 新增三幕结构识别（inciting incident、midpoint、climax、all_is_lost）
- **潜台词推断**：dialogue 增加 subtext 字段，支持表层文本与深层含义分离
- **场景功能分类**：scenes 增加 scene_function（exposition/rising_action/turning_point/climax/falling_action/resolution）
- **角色弧光追踪**：characters.json 增加 arc_stages，跨幕追踪情感状态与视觉线索
- **表情表生成**：Stage 2 新增 8 核心表情参考图（neutral/happy/sad/angry/surprised/disgusted/fearful/determined）
- **服装变化追踪**：characters.json 增加 outfits 数组，按场景范围记录服装与叙事原因
- **色彩脚本**：新增 color_script.json，全片色彩叙事蓝图，含情绪-色彩自动映射
- **场景设计**：新增 environments.json，含设计简报、关键道具、时间变化、文化语境
- **镜头语法双层结构**：storyboard 增加 framing + function（establishing/master/insert/reaction/pov/cutaway/transition）
- **机位运动三要素**：camera_movement / subject_motion / environment_motion
- **色彩方向**：每张 shot 增加 color_direction（dominant + accent）
- **轴线追踪**：storyboard 增加 axis_side（left/right/neutral），180度规则 enforcement
- **声音设计**：storyboard 增加 audio_direction（ambience/foley/music_mood/silence_flag）
- **Seed 锁定策略**：按模型的一致性控制方案（Midjourney --cref、SD IP-Adapter、Gemini 多图引用）
- **视频 Motion 精确化**：强制使用 动词+方向+幅度+时长 格式
- **批量容错**：三级重试阶梯，保留 Seed，failed_shots.json 追踪
- **规则打破指导**：新增"何时打破一致性/轴线/色彩/景别"的创作指导

### 脚本工具

- `init_project.py`：支持 v2.0 完整 8 个 JSON 模板初始化
- `validate_project.py`：支持 v2.0 全部 schemas 字段值域校验
- `generate_color_script.py`：从 mood 自动生成色彩脚本
- `check_axis.py`：轴线一致性检测与越轴警告

## v1.0.0 — 2026-05-26

### 初始版本

- 五阶段流水线：剧本解析 → 角色设计 → 分镜生成 → 图像生成 → 视频合成
- 四视图角色一致性
- 基础分镜生成（wide/medium/close-up）
- 多模型图像/视频生成支持
- 漫画页面排版（HTML/CSS + Pillow）
- FFmpeg 后处理（转场、字幕、BGM）
