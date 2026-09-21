# Google Search Console Workflow

Google Search Console is the best source for how the site is actually performing in Google Search.

## What to connect

Connect the property that matches the site config:

- URL-prefix property example: `https://www.example.com/`
- Domain property example: `sc-domain:example.com`

Use read-only access when possible.

## What Codex should pull or request

For foundation audits:

- Last 3 months queries
- Last 3 months pages
- Last 16 months queries, if available
- Last 16 months pages, if available
- Query by page data for priority URLs
- Sitemap and indexing context, if available

For monthly cycles:

- Last 28 days
- Previous 28 days
- Same period last year, if useful

## Useful dimensions

- `query`
- `page`
- `date`
- `country`
- `device`
- `searchAppearance`

## Core analyses

Ask Codex to find:

- High-impression, low-CTR queries.
- Position 4-20 queries with upside.
- Pages losing clicks month over month.
- Pages gaining impressions but not clicks.
- Queries where mobile and desktop behavior differs.
- Pages that rank for too many unrelated intents.
- Pages that should be refreshed, split, consolidated, or internally linked.

## Manual export fallback

If live GSC access is unavailable, export CSVs from Search Console:

- Performance > Search results > Queries
- Performance > Search results > Pages
- Filtered query/page exports for priority URLs

Then ask:

```text
Use the MATT SEO Agent skill. Read config/my-site.json and these GSC CSV exports. Run the monthly SEO cycle with exported data only.
```

## Notes

Google's Search Analytics API supports custom filters, dimensions such as query/page/country/device, and metrics including clicks, impressions, CTR, and position. See the official Search Analytics query docs for exact API behavior.
