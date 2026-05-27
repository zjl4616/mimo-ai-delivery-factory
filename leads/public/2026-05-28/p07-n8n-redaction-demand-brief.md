# P07 Demand brief — n8n workflow JSON redaction / safe sharing

Date: 2026-05-28
Owner: automation (public-only)

## Problem statement (public)

n8n troubleshooting threads often require posting workflow JSON to reproduce an issue. But exports commonly include sensitive or identifying information:

- credentials references and auth headers
- webhook URLs (can be abused)
- tokens / API keys / internal domains
- emails / phone numbers / IDs embedded in node parameters

Users are stuck between:

1) oversharing (security/privacy risk), or  
2) undersharing (helpers cannot reproduce)

## Public demand signals (to collect URLs)

This experiment explicitly needs linkable sources (public URLs) from:

- community.n8n.io threads where people request workflow JSON
- Reddit / HN-style threads about “can’t share workflow / contains secrets”
- n8n docs that explain workflows export/share and credentials handling

Add the exact URLs + 1–2 sentence notes below once confirmed.

### Sources

1. TODO: n8n docs — export/share workflow JSON + credentials separation  
   - URL: (add)  
   - Note:

2. TODO: n8n community thread — “please share your workflow JSON”  
   - URL: (add)  
   - Note:

3. TODO: Reddit r/n8n thread — workflow JSON sharing + secrets concern  
   - URL: (add)  
   - Note:

## Our response (deliverable assets)

- Offline tool: `site/tools/n8n-workflow-redactor/`
- Landing offer: `site/offers/p02-n8n-security-review/`
- Public intake: GitHub Issue template `p02-n8n-workflow-review.yml`

## Next action (public-only, needs operator confirmation)

Post once on ONE platform (n8n Community / Reddit r/n8n / Show HN) with:

- the tool link
- the “manual review / no 100% safety” disclaimer
- optional CTA to the review offer

