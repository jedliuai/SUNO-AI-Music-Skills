---
name: skill-model-updater
description: Checks this Codex AI Music Skills package for provider-specific model references and rewrites them to the default-model policy. Use when importing upstream updates or auditing the package for non-default AI model instructions.
---

# Default Model Policy Auditor

Use this skill when upstream changes reintroduce provider-specific model choices.

## Policy

- Every skill uses the current Codex default model.
- `SKILL.md` frontmatter must contain only `name` and `description`.
- Do not add provider-specific model selection fields or tool-routing fields to skill frontmatter.
- Replace named AI model families in workflow instructions with "default model" unless the text is historical source attribution.

## Audit Steps

1. Search `skills/`, `docs/`, and `reference/` for provider-specific AI model IDs, named model families, or legacy frontmatter fields beyond `name` and `description`.
2. For every `skills/*/SKILL.md`, keep only `name` and `description` in YAML frontmatter.
3. Rewrite any model-selection instructions to say: use the current Codex default model.
4. Leave non-AI uses of the word "model" alone, such as business model, data model, or audio equipment model.
5. Re-run the search and report remaining matches with whether they are acceptable historical/source references or need cleanup.

## Output

Report:

- Files changed.
- Remaining provider-specific AI model references, if any.
- Whether every skill frontmatter is Codex-compatible.
