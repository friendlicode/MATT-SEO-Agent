# DataForSEO/Data4SEO MCP Workflow

DataForSEO is the market research and SERP enrichment layer. It should complement Google Search Console, not replace it.

## Use DataForSEO for

- Keyword volume and trends
- Keyword difficulty
- Search intent
- CPC and competition context
- Competitor ranked keywords
- Domain intersections
- SERP competitor discovery
- Live SERP shape

## Recommended endpoint families

DataForSEO Labs:

- Keyword Overview
- Keyword Suggestions
- Bulk Keyword Difficulty
- Search Intent
- Ranked Keywords
- Competitors Domain
- Domain Intersection

SERP API:

- Live Google Organic SERP Advanced
- Google Organic SERP Task GET Advanced

## Suggested prompt

```text
Use the MATT SEO Agent skill and config/my-site.json.
Use DataForSEO/Data4SEO MCP to enrich the keyword list in config/keywords.example.csv.
For each keyword, collect market, language, volume, difficulty, intent, SERP competitors, and SERP notes.
Save a prioritized keyword opportunity map in outputs/.
```

## What to capture

For each pull, record:

- Endpoint or MCP tool used
- Date
- Market/location
- Language
- Keyword list
- Filters
- Any cost-sensitive assumptions

## Guardrails

- Do not burn API credits on huge keyword lists without batching or approval.
- Use GSC to judge actual site performance.
- Use DataForSEO to understand the market around keywords and competitors.
- Treat keyword volume and difficulty as directional.
