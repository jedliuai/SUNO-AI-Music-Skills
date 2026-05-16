# Codex AI Music Skills 中文说明

这是一个面向 Codex 改造后的 AI 音乐制作技能包，来源于 [`bitwize-music-studio/claude-ai-music-skills`](https://github.com/bitwize-music-studio/claude-ai-music-skills)。它保留了原项目中用于专辑策划、歌词创作、Suno 提示词、资料研究、音频处理、母带、宣发和发行准备的工作流，同时去掉了 Claude 专属的模型路由和插件市场元数据。

## 这个技能包能做什么

- 策划一张完整专辑，包括主题、曲目、风格、叙事线和制作路线。
- 编写、审查和润色歌词，检查押韵、韵律、视角、长度、可唱性和 AI 腔。
- 为 Suno 生成风格提示词、结构标签、发音提示和负面提示。
- 为真实事件、纪录片、人物或机构主题歌曲做资料研究和来源核验。
- 导入歌词、音频和封面素材，按约定目录整理项目文件。
- 进行混音建议、音频修复、母带处理和流媒体响度检查。
- 生成专辑封面方向、宣传文案、宣传视频和发行检查清单。

## Codex 改造内容

- 增加根目录 `SKILL.md`，作为 Codex 识别和路由的总入口。
- 将所有 `skills/*/SKILL.md` 的 frontmatter 统一改为只保留 `name` 和 `description`。
- 移除所有硬编码的模型字段，不再指定 Opus、Sonnet、Haiku 或任何外部模型。
- 统一策略为：所有技能都使用 Codex 当前默认模型。
- 将原根级说明改造为 `AGENTS.md`，作为 Codex 使用本仓库时的工作规则。
- 删除 Claude Code 插件市场相关元数据，让这个目录成为独立的 Codex skill package。

## 目录结构

```text
SKILL.md              Codex 总入口
AGENTS.md            仓库级工作规则
skills/              各个专业技能
reference/           Suno、母带、发行、研究等参考资料
genres/              音乐风格资料库
templates/           专辑、歌曲、研究、宣传模板
tools/               音频、宣传、乐谱、云上传等工具脚本
servers/             bitwize music MCP server
config/              配置示例和覆盖规则
README.md            英文说明
README.zh-CN.md      中文说明
使用说明.md          面向使用者的操作手册
```

## 推荐入口

日常使用时优先读根目录的 `SKILL.md`。如果已经知道自己要做什么，可以直接使用对应子技能：

- 写歌词：`skills/lyric-writer/SKILL.md`
- 润色歌词：`skills/lyric-refiner/SKILL.md`
- 歌词终审：`skills/lyric-reviewer/SKILL.md`
- Suno 提示词：`skills/suno-engineer/SKILL.md`
- 发音检查：`skills/pronunciation-specialist/SKILL.md`
- 专辑策划：`skills/album-conceptualizer/SKILL.md`
- 资料研究：`skills/researcher/SKILL.md`
- 混音建议：`skills/mix-engineer/SKILL.md`
- 母带处理：`skills/mastering-engineer/SKILL.md`
- 宣传文案：`skills/promo-writer/SKILL.md`
- 宣传视频：`skills/promo-director/SKILL.md`
- 发行准备：`skills/release-director/SKILL.md`

## 安装和准备

如果只把它当作 Codex 的知识和工作流技能包使用，可以直接放在当前工作区中使用。

如果要运行其中的 Python 工具、音频处理脚本或 MCP server，需要安装依赖：

```bash
python -m venv .venv
.venv\Scripts\pip install -r requirements.txt
```

Linux 或 macOS 使用：

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

完整本地工作流通常还需要配置 `~/.bitwize-music/config.yaml`。可以参考：

- `config/config.example.yaml`
- `config/README.md`
- `skills/setup/SKILL.md`
- `skills/configure/SKILL.md`

## 使用原则

- 不手动指定 AI 大模型，始终使用 Codex 当前默认模型。
- 先让 Codex 判断应该使用哪个 skill，再进入具体工作。
- 做真实事件、人物、法律、金融、安全等题材时，必须重视来源核验。
- 生成 Suno 歌词前，先做发音、显式内容、艺术家名字和来源检查。
- 音频工作建议顺序是：导入音频、混音或修复、母带、质检、发行。

## 来源和许可

原项目地址：https://github.com/bitwize-music-studio/claude-ai-music-skills

原项目使用 CC0/Public Domain。本 Codex 改造版本沿用该许可。
