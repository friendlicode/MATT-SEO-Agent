# Adapting To A New Site

To adapt this repo to a new site, change only the site context and data sources.

## Replace the config

Start from:

```bash
cp config/site.example.json config/my-site.json
```

Update:

- `site_name`
- `domain`
- `cms`
- `primary_audience`
- `business_goal`
- `markets`
- `topics`
- `competitors`
- `conversion_events`
- `publishing_constraints`
- `integrations`

## Replace example keyword inputs

Create a private keyword file when needed:

```bash
cp config/keywords.example.csv config/keywords.local.csv
```

Files ending in `.local` are intended to stay local.

## Choose the first workflow

New site:

```text
Run workflows/01-foundation-audit.md.
```

Existing site with data:

```text
Run workflows/02-monthly-seo-cycle.md.
```

Single content idea:

```text
Run workflows/03-content-brief.md.
```

Before publishing:

```text
Run workflows/04-technical-preflight.md.
```

## Keep reusable and private context separate

Reusable:

- Skill
- Prompts
- Workflows
- Public examples
- Setup docs

Private:

- Real GSC exports
- Private keyword research
- Competitor strategy
- Conversion data
- Client names
- Draft roadmaps
