# Sloth-ComicSmith-Den 大师评估报告

> 评估人：匿名 · 从业 23 年的动画导演 / 编剧 / 角色设计总监
> 评估日期：2026-05-26
> 评估对象：Sloth-ComicSmith-Den v1.0.0 SKILL.md + reference.md

---

## 一、总体印象

这个 Skill 的工程骨架是扎实的。五阶段流水线（剧本→角色→分镜→图像→视频）覆盖了从文字到影像的完整链路，JSON 化中间产物、批量容错、字幕烧录、漫画排版这些工程细节都考虑到了。作为一个**AI 辅助生产工具**的说明书，它是合格的。

但如果目标是**"把剧本变成有灵魂的作品"**，它现在更像是一台精密的印刷机，而不是一位导演在指挥一场戏。以下从导演、编剧、设计三个维度，指出那些隐藏在技术完备性之下的叙事与美学盲区。

---

## 二、导演维度：你会拍镜头，但还不会讲故事

### 2.1 景别 ≠ 镜头语言

当前 `type` 字段只有 `wide / medium / close-up / extreme-close-up / over-shoulder / aerial`，这是**景别分类**，不是**镜头语法**。

一个真实的分镜表需要区分的是镜头在叙事中的功能：
- **Establishing Shot** —— 建立空间关系，不是简单的 wide
- **Insert Shot** —— 关键道具特写，推动剧情（如角色拿起毒药瓶）
- **Reaction Shot** —— 反打反应，承载情绪转折
- **POV Shot** —— 主观视角，让观众"成为"角色
- **Master Shot** —— 整场戏的全景覆盖，用于剪辑时的"安全网"
- **Cutaway** —— 打断主线的时间跳跃或隐喻画面

**建议**：将 `type` 扩展为两层结构 —— `framing`（景别）+ `function`（镜头功能）。一个 shot 的景别和功能可能组合出完全不同的叙事效果。

### 2.2 机位运动描述过于粗糙

`camera: "static, low angle"` 远远不够。真实的运动镜头需要精确的动词：
- **Push In** —— 推，强调情绪压迫感
- **Pull Back** —— 拉，揭示更大的真相或孤独感
- **Pan / Tilt** —— 摇，引导观众视线
- **Tracking / Dolly** —— 跟，保持主体在画面中的位置关系
- **Crane / Jib** —— 升降，制造史诗感或坠落感
- **Handheld / Steadicam** —— 手持/稳定器，决定画面的呼吸感和纪实性

**致命问题**：当前 `video_prompt` 里的 "slow gentle camera movement" 交给 AI 视频模型，几乎等于让模型自己猜。Kling 和 Runway 需要明确的 motion 指令（如 "camera slowly pushes in on character's face"），否则生成的运动是随机的、叙事无关的。

**建议**：在 storyboard.json 中增加 `camera_motion` 字段，使用标准电影术语，并在生成 video_prompt 时将其作为最高优先级的运动描述。

### 2.3 轴线意识缺失

现在的 Skill 完全没有考虑 **180度轴线规则**。如果 Scene 1 中 Lin 在画面左侧、Barista 在右侧，Scene 2 如果突然变成 Lin 在右、Barista 在左，观众会产生"角色换位置了"的困惑。

**建议**：在 Stage 3 增加 **Axis Tracking** 逻辑 ——
1. 为每个场景定义一条虚拟轴线（连接两个主要角色的直线）
2. 所有镜头默认保持在轴线同一侧
3. 只有明确的 "Axis Jump"（越轴）意图时（如制造混乱、打斗、情绪断裂），才允许越轴
4. 在 `storyboard.json` 中增加 `axis_side: "left|right|neutral"` 字段

### 2.4 节奏（Pacing）完全交给 AI 猜测

当前 `duration` 是估计值，但没有任何关于**这场戏该快还是该慢**的指导。动漫不是每段对话都匀速播放的。

- **对话戏**：语速 120-150 字/分钟，配合停顿和反应镜头
- **动作戏**：快速剪辑，2-3 秒一个 shot
- **情绪高潮**：长镜头，让情绪在时间里发酵（参考《紫罗兰永恒花园》的凝视镜头）
- **蒙太奇**：用音乐节拍来切割镜头

**建议**：在 Stage 1 解析剧本时，识别场景的功能类型 —— `exposition` / `rising_action` / `climax` / `falling_action` / `resolution`，并在 Stage 3 根据场景功能推荐不同的 duration 基线和剪辑节奏。

### 2.5 声音设计维度为零

这是一个只有画面的 Skill。但动画的 50% 冲击力来自声音：
- **环境音（Ambience）**：雨声、咖啡馆的背景 chatter、远处的车声
- **拟音（Foley）**：推门时的铃铛声、咖啡杯放到碟子上的清脆声
- **音乐情绪（Music Cue）**：哪些场景需要配乐？什么情绪？
- **静默（Silence）**：有时候最响的声音是无声

**建议**：在 storyboard.json 中增加 `audio_direction` 字段，至少标注 `ambience`、`foley`、`music_mood`、`silence_flag` 四个维度。即使 Skill 不生成音频，也要让导演在审阅分镜时"听见"这场戏。

---

## 三、编剧维度：你提取了文字，但没理解戏剧

### 3.1 没有识别三幕结构

当前 Stage 1 把剧本切成 scenes，但 scenes 只是地理和时间单位，不是**戏剧单位**。一部戏的真正骨架是：
- **第一幕（Setup）**：世界观、角色、欲望、冲突的种子
- **第二幕（Confrontation）**：上升动作、中点转折、下降动作
- **第三幕（Resolution）**：高潮、结局、余韵

以及更细粒度的 **15 Beat Sheet**（ Save the Cat 结构）或 **Hero's Journey** 节拍。

**后果**：Skill 可能会在第二幕的紧张对峙场景和第三幕的情感高潮场景使用同样的景别策略、同样的 duration、同样的 lighting mood。这会让整部作品扁平如一潭死水。

**建议**：在 Stage 1 增加 **Dramatic Structure Analysis** ——
1. 识别 Inciting Incident（触发事件）
2. 识别 Midpoint（中点转折）
3. 识别 Climax（高潮）
4. 识别 All Is Lost（至暗时刻）
5. 将每个 scene 标记其在戏剧结构中的位置
6. 在 Stage 3 中，不同结构位置的 scene 使用不同的分镜策略模板

### 3.2 角色弧光（Character Arc）追踪缺失

现在 `characters.json` 只记录了角色的**静态属性**（外貌、性格、道具），但没有记录角色的**动态变化**。

Lin 在 Act 1 是 "reserved, weary"，在 Act 3 应该是 "broken but resolved" 或 "open to connection"。这个变化需要在视觉上有明确的轨迹：
- 服装从凌乱到整洁（或反之，取决于弧光方向）
- 眼神从低垂到正视
- 姿态从蜷缩到舒展
- 打光从冷蓝到暖金

**建议**：在 `characters.json` 中增加 `arc_stages` 字段：
```json
"arc_stages": [
  {"act": 1, "emotional_state": "weary_defensive", "visual_cues": "hunched posture, avoids eye contact, cool lighting"},
  {"act": 2, "emotional_state": "conflicted", "visual_cues": "restless movements, mixed warm/cool lighting"},
  {"act": 3, "emotional_state": "acceptance", "visual_cues": "upright posture, direct eye contact, warm golden lighting"}
]
```

### 3.3 潜台词（Subtext）识别为零

当前 `dialogue` 只记录了表面文字。但好编剧都知道：
- "One black coffee, please." 表面是点咖啡，潜台词可能是 "别跟我搭话"
- "Rough night?" 表面是关心，潜台词可能是 "我又得听客人倒苦水了"

如果 Skill 不理解潜台词，它生成的分镜就会**字面化** —— 角色真的只是在点咖啡，而不是在建立一道情感围墙。

**建议**：在 Stage 1 增加 **Subtext Inference** 步骤 —— 为每段对话标注 `surface_meaning` 和 `subtext`。在 Stage 3 生成分镜时，让 shot 的 lighting、mood、camera angle 服务于 subtext 而非 surface text。

### 3.4 场景功能（Scene Function）分类缺失

每个 scene 在叙事中承担的功能是不同的：
- **Setup Scene** —— 埋设信息，需要清晰、稳定、信息密度高
- **Turning Point** —— 转折点，需要越轴、打破节奏、视觉冲击
- **Emotional Beat** —— 情感节拍，需要特写、长镜头、音乐介入
- **Action Sequence** —— 动作戏，需要短镜头、快速剪辑、动态构图
- **Transition / Montage** —— 转场/蒙太奇，需要象征性画面、音乐驱动

**建议**：在 `scenes.json` 中增加 `scene_function` 字段，并在 Stage 3 为每种功能提供不同的分镜模板。

---

## 四、设计维度：你会画角色，但还没建世界

### 4.1 四视图不够，还需要表情表（Expression Sheet）

四视图解决了"这个角色长什么样"，但没解决"这个角色怎么演"。

一个专业的角色设定包（Character Packet）包括：
- **Turnaround**（四视图 + 俯视图 + 仰视图）—— 已有，很好
- **Expression Sheet**（6–12 个关键表情）：neutral / happy / sad / angry / surprised / disgusted / fearful / determined / broken / hopeful
- **Mouth Chart**（口型表）：A-I-E-O-U 发音口型，用于配音同步
- **Hand Gestures**（手势表）：关键手部姿态
- **Outfit Variations**（服装变化）：同一场景 vs 不同场景的服装差异

**建议**：在 Stage 2 增加 **Expression Sheet Generation** —— 为每个角色生成 8 个核心表情的参考图，保存到 `assets/characters/{name}/expressions/`。在 Stage 3 分镜时，根据 scene mood 和 dialogue emotion 引用对应的表情参考。

### 4.2 色彩脚本（Color Script）完全缺失

这是 Skill 目前最大的美学盲区。

《千与千寻》为什么动人？不是因为角色画得好，而是因为**色彩在讲故事**：
- 开场：灰蓝色调（现实世界，压抑）
- 进入神隐世界：突然饱和的红与金（奇幻，危险而诱人）
- 高潮：暗红与黑的对抗（生死之战）
- 结局：清晨的蓝与白（净化，归来）

当前 Skill 只有每个 shot 独立的 `lighting_mood`，没有**全片的色彩叙事蓝图**。

**建议**：在 Stage 2 或 Stage 3 早期增加 **Color Script** 生成 ——
1. 为每个 scene 定义一个主色（Dominant Color）和辅色（Accent Color）
2. 生成一条 `color_arc`，展示全片色彩的起伏变化
3. 在 `storyboard.json` 的每个 shot 中增加 `color_direction` 字段
4. 在生成 image_prompt 时，将 color direction 放在 prompt 的前段（色彩描述对 AI 图像生成影响极大）

### 4.3 场景/世界观设计（Environment Design）缺失

`setting` 字段只有 "INT. COFFEE SHOP — MORNING"，这远远不够。

一个场景的设计需要：
- **Floor Plan**（平面图）：空间布局决定机位选择
- **Key Props**（关键道具）：哪些道具会被特写？哪些推动剧情？
- **Time-of-Day Variation**（时间变化）：同一场景在早晨/黄昏/雨夜的不同面貌
- **Cultural / Era Context**（文化/年代语境）：1980s 东京 vs 2020s 上海，完全不同的视觉逻辑

**建议**：在 Stage 1 解析场景后，为每个 setting 生成 **Environment Design Brief** —— 一段 100 字的环境描述 + 关键道具列表 + 时间变化说明。保存到 `environments.json`，在 Stage 3 分镜时作为空间参考。

### 4.4 服装变化没有被追踪

Lin 在 Scene 1 穿皮衣，Scene 5 如果还是同样的皮衣，观众不会注意。但如果她在 Scene 3 淋了雨、Scene 4 换了干衣服、Scene 5 发现新衣服是别人送的 —— 这就是一个**无声的角色弧光**。

当前 `characters.json` 只有一套 `clothing`。

**建议**：将 `clothing` 改为 `outfits` 数组，按 scene 关联：
```json
"outfits": [
  {"scene_range": "S01-S03", "description": "worn leather jacket, gray hoodie", "narrative_reason": "default everyday wear"},
  {"scene_range": "S04-S05", "description": "borrowed oversized coat, still damp", "narrative_reason": "after the rain scene, someone gave her a coat"}
]
```

---

## 五、工程/技术维度： prompt 工程还不够"工程"

### 5.1 没有 Seed 锁定策略

如果 batch 中某张图失败了，重试时即使 prompt 相同，AI 模型也会生成完全不同的图像。这意味着角色的脸可能在同一场戏里突然"换头"。

**建议**：在 reference.md 中增加 **Seed Management** 指南 ——
- 为每个角色分配一个固定 seed 区间
- 重试时必须复用原 seed（如果模型支持）
- 如果模型不支持 seed，使用 Reference Image 强引用（Midjourney `--cref`，Stable Diffusion IP-Adapter）

### 5.2 Reference Image 权重控制缺失

当前提到 "Reference the 4-view images if available"，但没有说明**怎么用**。

不同模型的引用能力差异巨大：
- **Midjourney v6**：`--cref URL --cw 100`（强角色一致性）
- **Stable Diffusion**：IP-Adapter + ControlNet OpenPose
- **DALL-E 3**：不支持直接引用，需要用 prompt 硬编码 + seed 控制
- **Gemini**：支持多图 reference，但需要特定 API 格式

**建议**：在 reference.md 中为每种模型提供精确的 reference image 调用方案，包括权重参数。

### 5.3 视频生成的 Motion 描述太模糊

当前的 `video_prompt` 只有 "Slow gentle camera" 这种模糊描述。AI 视频模型对 motion 的理解非常字面化，需要精确的动词 + 方向 + 幅度：
- 错误："gentle camera movement"
- 正确："camera slowly pushes in 20% closer to character's face over 3 seconds"
- 错误："character moves"
- 正确："character turns head 45 degrees to the left, hair flows with the motion"

**建议**：在 reference.md 的 Video Prompt Builder 中，强制要求 `motion` 字段包含三个子元素：`subject_motion`、`camera_motion`、`environment_motion`。

---

## 六、优先级修复清单

| 优先级 | 问题 | 修复方案 | 影响 |
|--------|------|---------|------|
| **P0** | 镜头功能缺失 | type → framing + function 双层结构 | 决定叙事是否成立 |
| **P0** | 色彩脚本缺失 | 增加全片 color_arc + shot color_direction | 决定作品是否有美学灵魂 |
| **P0** | 潜台词识别缺失 | dialogue 增加 subtext 字段 | 决定分镜是否字面化 |
| **P1** | 表情表缺失 | Stage 2 增加 expression sheet 生成 | 决定角色是否能"演" |
| **P1** | 机位运动描述粗糙 | camera 改为标准电影术语 + motion 三要素 | 决定视频生成可控性 |
| **P1** | 角色弧光缺失 | characters.json 增加 arc_stages | 决定角色是否扁平 |
| **P2** | 轴线意识缺失 | storyboard.json 增加 axis_side | 决定空间连贯性 |
| **P2** | 声音设计缺失 | storyboard.json 增加 audio_direction | 决定视听完整性 |
| **P2** | 场景设计缺失 | 增加 environments.json | 决定世界观可信度 |
| **P3** | Seed / Reference 控制 | reference.md 增加模型级引用方案 | 决定一致性工程可靠性 |

---

## 七、最后的忠告

这个 Skill 现在是一台**能运转的机器**。但要让它成为一台**能创造艺术的机器**，需要在以下三个问题上做出选择：

1. **你是想做工具，还是想做导演？** 工具只管执行，导演要理解每场戏为什么存在。如果 Skill 的定位是"帮用户当导演"，那么它需要内置戏剧分析能力，而不仅仅是文本解析能力。

2. **一致性（Consistency）和艺术性（Artistry）之间的张力。** 四视图和 consistency prompt 追求的是"每张图都像同一个人"，但好动画在关键时刻会故意打破一致性 —— 夸张变形、风格切换、色彩爆发。Skill 需要给用户留出手工打破规则的出口。

3. **不要替用户决定所有事情。** 当前 Skill 在每个阶段都试图自动生成一切。但创作的核心乐趣在于选择。建议在关键节点（风格选择、分镜确认、色彩方向）增加**"提供 3 个选项让用户选"**的模式，而不是只有一个默认输出。

慢一点，深一度。这句话作为品牌口号很好，但不要让 Skill 本身成为那个"深"的瓶颈 —— 它应该帮助用户更快地到达"深"的地方，而不是把浅表的工作自动化后让用户失去深入的机会。
