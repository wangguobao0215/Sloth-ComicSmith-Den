<p align="center">
  <img src="assets/sloth-avatar-round.png" width="120" />
</p>

<h1 align="center">Sloth-ComicSmith-Den — 匠漫 · 剧本到漫画视频流水线</h1>

<p align="center">
  <strong>将文本剧本转化为有灵魂的结构化漫画/视频项目</strong><br/>
  支持戏剧结构分析、角色弧光追踪、色彩脚本、精准镜头语法与声音设计。
</p>

<p align="center">
  <img src="assets/qrcode.jpg" width="140" /><br/>
  <sub>扫码关注 <strong>树懒老K</strong> · 获取更多 AI 技能</sub><br/>
  <em>慢一点，深一度</em>
</p>

---

## 功能概览

1. **剧本解析（含戏剧结构）**：自动识别三幕结构、触发事件、中点转折、高潮和至暗时刻
2. **角色一致性设计**：四视图参考图、表情表、角色弧光追踪、服装变化记录
3. **色彩脚本**：全片色彩叙事蓝图，情绪到色彩的自动映射
4. **智能分镜**：专业镜头语法（景别+功能）、机位运动精确描述、180度轴线追踪、声音设计
5. **AI 图像生成**：多模型支持，Seed 锁定策略，批量容错
6. **视频合成**：精准 Motion 描述，转场效果，字幕烧录
7. **漫画排版**：HTML/CSS 或 Pillow 合成完整漫画页

## 快速开始

1. 克隆仓库
2. 初始化项目：
   ```bash
   cd Sloth-ComicSmith-Den/scripts
   python3 init_project.py my_comic_project
   ```
3. 按 SKILL.md 的五阶段流程逐步执行
4. 校验项目文件：
   ```bash
   python3 validate_project.py my_comic_project
   ```
5. 自动生成色彩脚本：
   ```bash
   python3 generate_color_script.py my_comic_project
   ```

## 版本

当前版本：2.1.0

## 许可证

MIT License
