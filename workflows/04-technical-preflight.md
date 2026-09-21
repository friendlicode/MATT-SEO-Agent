# Technical SEO Preflight Workflow

Use this before publishing or after changing templates, navigation, metadata, URLs, or structured data.

## Inputs

- URL or template being changed
- Site config
- Pull request or changed files, if available
- GSC indexing information, if available

## Checks

- URL is indexable when it should be.
- Canonical URL is correct.
- Title is unique and aligned with intent.
- Meta description is useful and non-duplicative.
- H1 is present and unique.
- Headings are logical.
- Internal links point to and from relevant pages.
- Images have useful alt text where appropriate.
- Structured data is valid where used.
- Sitemap impact is understood.
- Redirects are planned if URLs change.
- Page does not create thin, duplicate, or orphaned content.

## Output

- `outputs/technical-preflight-[page-or-template].md`

## Done when

- The user has a publish or no-publish recommendation with fixes and verification steps.
