# P07 target threads (public-only) — n8n workflow JSON redaction

Date: 2026-05-28
Owner: automation

Goal: pick 3–5 public threads to reply to with value-first help + link to the offline redactor.

Rules:
- public internet only
- no DMs, no warm network
- no spam: reply only where clearly relevant
- always include “manual review / not 100% safe” disclaimer

## Seed evidence (public)

- n8n docs export/import mention “remove credentials”: https://docs.n8n.io/workflows/export-import/
- n8n community discussion on workflow JSON leaking credentials: https://community.n8n.io/t/why-your-n8n-workflow-json-is-leaking-credentials-and-the-architectural-fix/289576
- Reddit: anonymizing n8n workflow JSON: https://www.reddit.com/r/n8n/comments/1mkluki/anonymizing_n8n_workflow_json/
- Reddit: tool to clean sensitive data from n8n exports: https://www.reddit.com/r/n8n/comments/1mthdfd/i_built_a_tool_to_clean_sensitive_data_from_n8n/

## Targets (fill during execution)

| # | Platform | Thread URL | Their problem | Our helpful reply angle | Posted? | Outcome |
|---|---|---|---|---|---|---|
| 1 | n8n Community | TODO | They need workflow JSON but worry about secrets | Give checklist + offline redactor link | no | |
| 2 | n8n Community | TODO | Helper requests full JSON | Offer redaction + template generator | no | |
| 3 | Reddit r/n8n | TODO | “anonymize/sanitize workflow export” | Link tool + warn manual review | no | |
| 4 | Reddit r/n8n | TODO | Sharing workflows / templates publicly | Recommend remove creds + redaction report | no | |
| 5 | HN / other forum | TODO | Posting JSON config with secrets | Suggest safe sharing pattern | no | |

## Reply skeleton (value-first)

1) Acknowledge risk and context (what to redact and why).
2) Suggest the official baseline (“remove credentials” option).
3) Offer offline redactor + report + help template link:
   - https://1993921.xyz/mimo-ai-delivery-factory/tools/n8n-workflow-redactor/
4) Disclaimer: manual review required; never share tokens/webhooks.

