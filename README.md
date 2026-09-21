# MATT SEO Agent

A public, plug-and-play starter repo for running repeatable SEO workflows with Codex, Google Search Console, DataForSEO/Data4SEO MCP, and GitHub.

This repo is intentionally generic. It contains no private site data, no proprietary keyword lists, no analytics exports, no credentials, and no references to any specific private project.

## What this is

MATT SEO Agent is a reusable operating system for SEO work. It gives Codex:

- A reusable SEO skill in `skills/matt-seo-agent/SKILL.md`
- Site configuration templates in `config/`
- Prompt templates in `prompts/`
- Repeatable workflow docs in `workflows/`
- Setup and integration docs in `docs/`
- GitHub issue templates for SEO tasks

Use it to run foundation audits, monthly SEO cycles, content briefs, technical checks, internal linking reviews, and performance retrospectives.

## How the pieces fit

| Tool | Role |
| --- | --- |
| Codex | Reads this repo, follows the SEO skill, creates plans, briefs, tickets, audits, and implementation-ready recommendations. |
| Google Search Console | Provides real performance data: queries, pages, clicks, impressions, CTR, average position, indexing, and sitemap context. |
| DataForSEO/Data4SEO MCP | Adds market and SERP data: keyword volume, difficulty, intent, competitors, ranked keywords, SERP snapshots, and domain intersections. |
| GitHub | Stores the playbook, tracks SEO work as issues, reviews changes through pull requests, and keeps decisions visible. |

## Quick start

1. Clone or fork this repo.

   ```bash
   git clone https://github.com/YOUR-USERNAME/MATT-SEO-Agent.git
   cd MATT-SEO-Agent
   ```

2. Copy the example site config.

   ```bash
   cp config/site.example.json config/my-site.json
   ```

3. Fill in `config/my-site.json` with your own public site details.

4. Open the repo in Codex.

5. Ask Codex:

   ```text
   Use the MATT SEO Agent skill. Read config/my-site.json and run the foundation SEO workflow. Save outputs in outputs/.
   ```

## Recommended first run

Ask Codex:

```text
Use the MATT SEO Agent skill.
Read config/my-site.json.
Run workflows/01-foundation-audit.md.
If GSC or DataForSEO access is unavailable, tell me exactly what data is missing and produce the best possible manual-input version.
Save final files in outputs/.
```

Expected outputs:

- `outputs/foundation-audit.md`
- `outputs/technical-seo-checklist.md`
- `outputs/keyword-map.md`
- `outputs/content-opportunity-backlog.md`
- `outputs/90-day-seo-roadmap.md`

## Common commands to give Codex

Foundation audit:

```text
Use the MATT SEO Agent skill with config/my-site.json. Run a foundation SEO audit and save the deliverables in outputs/.
```

Monthly SEO cycle:

```text
Use the MATT SEO Agent skill with config/my-site.json. Run the monthly SEO cycle. Use GSC for performance data and DataForSEO MCP for keyword and SERP enrichment where available.
```

Content brief:

```text
Use the MATT SEO Agent skill with config/my-site.json. Create a content brief for the keyword "[KEYWORD]" and include search intent, suggested title, outline, internal links, competing pages, and publish checklist.
```

Technical check:

```text
Use the MATT SEO Agent skill with config/my-site.json. Run a technical SEO preflight before publishing. Check indexability, canonicals, metadata, headings, schema, internal links, sitemap impact, and performance risks.
```

GitHub task creation:

```text
Use the MATT SEO Agent skill. Convert outputs/content-opportunity-backlog.md into GitHub issues using the SEO task template. Group issues by impact and effort.
```

## Setup guides

- [Setup](docs/setup.md)
- [Integrations](docs/integrations.md)
- [Google Search Console workflow](docs/google-search-console.md)
- [DataForSEO MCP workflow](docs/dataforseo-mcp.md)
- [Codex workflow](docs/codex-workflow.md)
- [GitHub workflow](docs/github-workflow.md)
- [Adapting to a new site](docs/adapting-to-a-new-site.md)
- [Security and privacy](docs/security-and-privacy.md)

## Validate your config

This repo includes a tiny local validator for the example config shape.

```bash
python3 scripts/validate_site_config.py config/my-site.json
```

It does not call Google, DataForSEO, OpenAI, GitHub, or any external service.

## Public repo safety rules

Do not commit:

- API keys or OAuth credentials
- Search Console exports from a private property
- Private analytics screenshots
- Proprietary keyword research
- Unpublished product plans
- Client names, private domains, or internal notes unless they are meant to be public
- Generated SEO outputs that reveal private strategy

Use `.env.local`, private GitHub repos, or local-only files for sensitive work.

## License

MIT
