# Model Strategy

This Codex adaptation intentionally removes all provider-specific model assignments from skill frontmatter.

## Policy

- Use the current Codex default model for every skill.
- Do not add provider-specific `model:` fields to `SKILL.md`; Codex only needs `name` and `description` to trigger skills.
- Escalate reasoning effort through the active Codex runtime when the task is unusually complex, rather than hard-coding model families into the skill files.
- Keep skill behavior portable: references may discuss creative difficulty, but they must not require a named external LLM.

## Practical Impact

The original upstream project divided work into creative, reasoning, and mechanical tiers. In this port, those distinctions are treated as workflow risk levels, not model-selection directives. Lyrics, research verification, mastering, setup, and file operations all run on the default model unless the user or runtime explicitly chooses otherwise.
