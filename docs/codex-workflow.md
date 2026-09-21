# Codex Workflow

Codex is the execution layer for this repo.

## Start a run

Use a prompt like:

```text
Use the MATT SEO Agent skill from skills/matt-seo-agent/SKILL.md.
Read config/my-site.json.
Run workflows/01-foundation-audit.md.
Use GSC and DataForSEO/Data4SEO MCP if available.
Save outputs in outputs/.
```

## Good operating pattern

1. Read the site config.
2. Read the workflow.
3. Confirm available integrations.
4. Pull data or ask for exports.
5. Produce a draft.
6. Turn the draft into prioritized actions.
7. Create GitHub issues or implementation notes.

## When integrations are missing

Codex should continue, but label the output:

- `Data used`
- `Data missing`
- `Assumptions`
- `Follow-up needed`

## Skill usage

The skill file gives Codex the durable behavior. The prompts give Codex the task. The site config gives Codex the context.

This separation is what makes the repo reusable across sites.
