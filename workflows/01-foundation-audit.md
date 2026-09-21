# Foundation SEO Audit Workflow

Use this when setting up the agent for a site for the first time.

## Inputs

- `config/my-site.json`
- Google Search Console access or exported CSVs
- DataForSEO/Data4SEO MCP access, if available
- Current sitemap URL
- Known competitors
- Any existing keyword list

## Steps

1. Read the site config.
2. Confirm the domain, audience, business goal, market, and conversion events.
3. Pull or request GSC data for the last 3 months and last 16 months if available.
4. Use DataForSEO for keyword and competitor enrichment where available.
5. Review core technical SEO risks:
   - Indexability
   - Canonicals
   - Sitemap and robots.txt
   - Title and meta description patterns
   - Heading structure
   - Internal links
   - Structured data
   - Page performance risks
6. Build a keyword and page opportunity map.
7. Create a 90-day roadmap.

## Outputs

- `outputs/foundation-audit.md`
- `outputs/technical-seo-checklist.md`
- `outputs/keyword-map.md`
- `outputs/content-opportunity-backlog.md`
- `outputs/90-day-seo-roadmap.md`

## Done when

- The site has a documented baseline.
- Top SEO risks are prioritized.
- The next 90 days of work are clear.
- High-impact items can be converted into GitHub issues.
