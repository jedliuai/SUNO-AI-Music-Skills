---
name: ai-music-studio
description: End-to-end AI music production workflow for Codex. Use when creating albums or songs with Suno, writing or reviewing lyrics, planning album concepts, generating Suno style prompts, researching source-based tracks, checking pronunciation or explicit content, importing audio/art, mixing, mastering, creating promo assets, or preparing releases.
---

# AI Music Studio

Use this as the package-level entry point. For specialized work, load the matching sub-skill from `skills/<skill-name>/SKILL.md` and follow its instructions.

## Routing

- New album or album planning: `skills/new-album/SKILL.md`, then `skills/album-conceptualizer/SKILL.md`.
- Track lyrics: `skills/lyric-writer/SKILL.md`; review with `skills/lyric-reviewer/SKILL.md`; refine with `skills/lyric-refiner/SKILL.md`.
- Suno prompts: `skills/suno-engineer/SKILL.md`; pronunciation: `skills/pronunciation-specialist/SKILL.md`; explicit content: `skills/explicit-checker/SKILL.md`.
- True-story or documentary research: start with `skills/researcher/SKILL.md`, then load the relevant `skills/researchers-*` specialist.
- Album status and next action: `skills/resume/SKILL.md` or `skills/next-step/SKILL.md`.
- Importing assets: `skills/import-track/SKILL.md`, `skills/import-audio/SKILL.md`, `skills/import-art/SKILL.md`.
- Audio work: `skills/mix-engineer/SKILL.md`, then `skills/mastering-engineer/SKILL.md`.
- Promotion and release: `skills/promo-writer/SKILL.md`, `skills/promo-director/SKILL.md`, `skills/release-director/SKILL.md`.

## Core Rules

- Use the current Codex default model for every workflow. Do not choose Opus, Sonnet, Haiku, GPT, Gemini, or any other named model from these instructions.
- Read `AGENTS.md` for repository-wide workflow rules before doing album state, setup, or release work.
- Prefer structured tools and scripts in `tools/` and `servers/` when they exist; do not reimplement audio analysis, mastering, or state parsing manually.
- Read only the reference files needed for the current task. Large genre, Suno, mastering, and release references live under `reference/` and `genres/`.
- Keep user-facing outputs focused on the next useful production step: concept, lyrics, style prompt, verification result, mastered asset, promo copy, or release checklist.
