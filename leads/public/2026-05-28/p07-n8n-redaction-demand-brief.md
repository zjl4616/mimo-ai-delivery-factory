# P07 Demand brief — n8n workflow JSON redaction / safe sharing

Date: 2026-05-28
Owner: automation (public-only)

## Problem statement (public)

n8n troubleshooting and collaboration frequently require posting workflow JSON to reproduce an issue. But exports (and/or node params) can contain sensitive or identifying information:

- credential references (name/id), and sometimes hard-coded secrets in node parameters
- auth headers / tokens / API keys accidentally pasted into nodes
- webhook URLs (can be abused)
- internal domains, emails / phone numbers / IDs embedded in fields

Users get stuck between:

1) oversharing (security/privacy risk), or
2) undersharing (helpers cannot reproduce)

## Public demand signals (verifiable URLs)

This experiment needs linkable public sources showing the pain is real.

### n8n docs

- https://docs.n8n.io/workflows/export-import/
  - Note: official export docs mention a “remove credentials” option, implying sharing/export needs caution.

### community.n8n.io / public posts (workflow JSON + credential leakage)

- https://community.n8n.io/t/why-your-n8n-workflow-json-is-leaking-credentials-and-the-architectural-fix/289576
  - Note: directly discusses workflow JSON leaking credentials/tokens in real-world sharing scenarios.

### Reddit discussions (anonymizing / redacting workflow JSON)

- https://www.reddit.com/r/n8n/comments/1mkluki/anonymizing_n8n_workflow_json/
  - Note: users discuss that exports can still include identifiers (credential IDs, sheet IDs, channels) and how to anonymize.
- https://www.reddit.com/r/n8n/comments/1mthdfd/i_built_a_tool_to_clean_sensitive_data_from_n8n/
  - Note: existence of a similar tool is proof the demand exists; we differentiate via report + help template + review offer.

## Our response (deliverable assets)

- Offline tool: `site/tools/n8n-workflow-redactor/`
- Optional service offer: `site/offers/p02-n8n-security-review/`
- Public intake: GitHub Issue template `p02-n8n-workflow-review.yml` (sanitized JSON + repro details)

## Next action (public-only, needs operator confirmation)

Post once on ONE platform (n8n Community / Reddit r/n8n / Show HN) with:

- tool link
- “manual review / no 100% safety” disclaimer
- optional CTA to the review offer + GitHub issue intake

