# Setup

This guide gets a new site owner from clone to first SEO audit.

## 1. Fork or clone the repo

```bash
git clone https://github.com/YOUR-USERNAME/MATT-SEO-Agent.git
cd MATT-SEO-Agent
```

## 2. Create a site config

```bash
cp config/site.example.json config/my-site.json
```

Edit `config/my-site.json`:

- Replace the domain.
- Replace competitors.
- Replace audience and business goal.
- Set the CMS.
- Set markets, language, and location.
- Set integration flags.

Validate the config:

```bash
python3 scripts/validate_site_config.py config/my-site.json
```

## 3. Install or reference the skill

Use `skills/matt-seo-agent/SKILL.md` as the agent's SEO operating instructions.

In Codex, you can either:

- Keep this repo open and tell Codex to use the skill file.
- Copy `skills/matt-seo-agent/` into your Codex skills directory if you want it available globally.

Prompt:

```text
Use the MATT SEO Agent skill from skills/matt-seo-agent/SKILL.md. Read config/my-site.json and run prompts/foundation-audit.md.
```

## 4. Connect optional integrations

The repo works with manual exports, but it is much better with:

- Google Search Console access
- DataForSEO/Data4SEO MCP
- GitHub repo access

See `docs/integrations.md`.

## 5. Run the first audit

```text
Use the MATT SEO Agent skill.
Read config/my-site.json.
Run workflows/01-foundation-audit.md.
Save outputs in outputs/.
```

## 6. Turn recommendations into work

After the audit:

```text
Use workflows/05-github-issue-planning.md to turn outputs/content-opportunity-backlog.md and outputs/technical-seo-checklist.md into GitHub issues.
```
