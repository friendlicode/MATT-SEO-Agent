# Agent Instructions

Use this repo as a reusable SEO operating system for any public website.

Before producing SEO recommendations:

1. Read the selected site config from `config/`.
2. Read `skills/matt-seo-agent/SKILL.md`.
3. Identify the workflow type: foundation, monthly, content, technical, GitHub planning, or reporting.
4. State which data sources are available and which are missing.
5. Keep outputs generic unless the site config provides specific facts.

Never assume private project history. Never reference any site, brand, Search Console account, or analytics data that is not present in the current repo or explicitly supplied by the user.

When live integrations are unavailable, ask for exported CSVs or produce a manual-input version with clear placeholders.

Write final deliverables into `outputs/` unless the user asks for GitHub issues, pull requests, or inline analysis.
