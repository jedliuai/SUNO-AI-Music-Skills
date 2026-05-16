# Codex AI Music Skills

A Codex-ready port of [`bitwize-music-studio/claude-ai-music-skills`](https://github.com/bitwize-music-studio/claude-ai-music-skills). It keeps the music-production workflows, references, templates, scripts, and genre knowledge, while removing Claude-specific model routing and marketplace metadata.

## What Changed

- Added a package-level `SKILL.md` entry point for Codex.
- Converted every `skills/*/SKILL.md` frontmatter to Codex-compatible `name` + `description` only.
- Removed all hard-coded provider-specific model fields from skill frontmatter.
- Replaced model strategy with a simple rule: use the current Codex default model for every skill.
- Converted root instructions from `CLAUDE.md` to `AGENTS.md` for Codex-oriented repository guidance.
- Removed `.claude-plugin/` marketplace metadata because this folder is now a Codex skill package, not a Claude Code plugin package.

## How To Use

Use the root `SKILL.md` as the entry point. For a specific task, open the matching sub-skill under `skills/`:

- `skills/lyric-writer/SKILL.md` for writing lyrics.
- `skills/suno-engineer/SKILL.md` for Suno style prompts.
- `skills/researcher/SKILL.md` and `skills/researchers-*` for source-based songs.
- `skills/mix-engineer/SKILL.md` and `skills/mastering-engineer/SKILL.md` for audio polish and mastering.
- `skills/promo-writer/SKILL.md`, `skills/promo-director/SKILL.md`, and `skills/release-director/SKILL.md` for launch work.

For full workflow rules, read `AGENTS.md`. For default-model policy, read `reference/model-strategy.md`.

## Setup Notes

The upstream project includes Python tools and an MCP server for album state, audio processing, promotion, and database-backed workflows. Those tools are preserved, but some scripts may still contain upstream implementation assumptions. Start with the `setup` and `configure` skills if you want to run the full local workflow.

Typical Python setup:

```bash
python -m venv .venv
.venv\Scripts\pip install -r requirements.txt
```

On Linux/macOS, use the equivalent `source .venv/bin/activate` flow.

## Source And License

Original project: https://github.com/bitwize-music-studio/claude-ai-music-skills

The upstream project is CC0/Public Domain. This Codex adaptation keeps that license.
