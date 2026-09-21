# Monthly SEO Cycle Workflow

Use this once per month after the foundation audit.

## Inputs

- Current site config
- Previous month outputs
- Google Search Console data for:
  - Last 28 days
  - Previous 28 days
  - Same period last year, if available
- DataForSEO keyword and SERP enrichment, if available
- GitHub issues and recently shipped changes

## Steps

1. Summarize organic performance changes.
2. Identify wins:
   - Queries gaining clicks
   - Pages gaining impressions
   - Newly ranking URLs
   - Recently shipped work that appears to help
3. Identify losses:
   - Pages losing clicks
   - Queries slipping from top positions
   - Pages with falling CTR
   - Indexing or sitemap issues
4. Find opportunities:
   - Position 4-20 keywords
   - High-impression low-CTR queries
   - Competitor content gaps
   - Internal link targets
   - Refresh candidates
5. Create the next month's action plan.
6. Convert approved actions into GitHub issues.

## Outputs

- `outputs/monthly-seo-report.md`
- `outputs/next-month-action-plan.md`
- `outputs/content-briefs.md`
- `outputs/github-issue-backlog.md`

## Done when

- The site owner knows what changed, why it matters, and what to do next.
