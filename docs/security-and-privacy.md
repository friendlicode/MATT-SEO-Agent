# Security And Privacy

This repo is designed to be public safe, but only if users keep private data out of commits.

## Never commit

- API keys
- OAuth tokens
- `.env.local`
- Google service account files
- GSC exports from private sites
- Private analytics reports
- Private keyword research
- Client strategy
- Internal roadmaps
- Sensitive competitor analysis

## Recommended pattern

Public repo:

- Templates
- Example configs
- Generic prompts
- Generic workflows
- Public docs

Private repo or local files:

- Real configs
- Real exports
- Generated audits
- Keyword maps
- Monthly reports
- GitHub issues for private strategy

## Environment variables

Use `.env.example` as a guide. Put real values in `.env.local` or your normal secret manager.

The `.gitignore` excludes common local secret files, but review changes before pushing.

## Before making the repo public

Run:

```bash
git status --short
git grep -n "api_key\|secret\|password\|token\|private\|client"
```

Then manually inspect anything suspicious.
