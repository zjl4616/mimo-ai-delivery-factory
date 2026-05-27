﻿# P07 — n8n Workflow JSON Redactor (Offline)

A browser-only, offline tool to help you **redact** sensitive fields in exported n8n workflow JSON before you share it publicly (forums / Reddit / GitHub issues).

## Use

- Open the tool:
  - `site/tools/n8n-workflow-redactor/index.html` (for GitHub Pages)
  - or `product-lab/n8n-workflow-redactor/index.html` (source copy)
- Paste workflow JSON and click **Start redaction**.
- Copy/download:
  - redacted JSON
  - redaction report
  - public help template (Markdown)

## Safety

This is best-effort automation, not a guarantee. Always manually review before posting.

## Why this exists

Public helpers often ask for workflow JSON to reproduce problems, but exports may contain sensitive metadata (tokens, webhook URLs, headers, internal domains, emails/phones, etc.).

