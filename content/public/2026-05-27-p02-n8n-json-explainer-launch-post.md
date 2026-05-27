# P02 Launch Posts — n8n JSON 中文解释器（离线 + 脱敏 + 风险清单）

时间：2026-05-27  
产品：P02 n8n JSON 中文解释器（浏览器端离线运行）  
Demo：`https://1993921.xyz/mimo-ai-delivery-factory/tools/n8n-json-explainer/`  
Repo：`https://github.com/zjl4616/mimo-ai-delivery-factory`  
协作入口（公开）：`https://github.com/zjl4616/mimo-ai-delivery-factory/issues/new?template=p02-n8n-workflow-review-request.yml`

原则：
- 不使用私域联系人；只在公开渠道发布/回复。
- 不承诺“必定解决”，只提供可验证的工具与公开协作路径。
- 强调：离线、无后端、不上传数据；仍提醒用户自行检查脱敏结果。

---

## A) Show HN（英文）

**Title**: Show HN: Offline explainer for n8n workflow JSON → readable doc + risk checklist

**Text**

I built a small static tool that turns an exported n8n workflow JSON into a readable explanation (flow overview + node descriptions + heuristic risk checklist).

Everything runs **offline in your browser** (no backend, no external CDN). Your workflow data never leaves your device.

- Demo: `https://1993921.xyz/mimo-ai-delivery-factory/tools/n8n-json-explainer/`
- Repo: `https://github.com/zjl4616/mimo-ai-delivery-factory`

If you want help reviewing/debugging a workflow safely, there’s a public issue template. Please remove secrets first (or use the built-in “sanitize” button), then post the sanitized JSON:

- Public issue intake: `https://github.com/zjl4616/mimo-ai-delivery-factory/issues/new?template=p02-n8n-workflow-review-request.yml`

Feedback welcome: which node types or expression patterns should I support next?

---

## B) Reddit（英文）

**Title (Option A)**: I built a browser-only explainer for n8n workflow JSON (offline, no backend)  
**Title (Option B)**: Paste n8n workflow JSON → get a readable doc + risk checklist (browser-only)

**Body**

Hi folks — I often see people sharing n8n templates, but the workflow JSON is still hard to review quickly (and it’s scary to share because of credentials).

So I built a tiny **browser-only** tool that:
- parses an exported n8n workflow JSON
- generates a **readable explanation** (node list + simplified flow overview)
- adds a small **risk checklist** (heuristics like secrets, error handling, timeouts)
- can **sanitize** obvious credential-like fields (still: please double-check before sharing)

Runs **fully offline** (no server, no external CDN).

- Demo: `https://1993921.xyz/mimo-ai-delivery-factory/tools/n8n-json-explainer/`
- Source: `https://github.com/zjl4616/mimo-ai-delivery-factory`

If you want me to take a look, please post a **sanitized** JSON to the public GitHub issue template so the discussion stays transparent:
- `https://github.com/zjl4616/mimo-ai-delivery-factory/issues/new?template=p02-n8n-workflow-review-request.yml`

---

## C) n8n 社区论坛（英文，贴合“求助帖回复”场景）

> 用于回复具体求助帖，不用于“硬广”。先给实质性帮助，再顺带提工具。

**Reply Template — JSON / Expression error**

Hey — thanks for sharing the details.

Based on what you described, this looks like an `expression` / parameter formatting issue around `[NODE_NAME]` (common cases: missing quotes, wrong `={{ ... }}` wrapper, or referencing a field that doesn’t exist on the incoming item).

To make it easier to debug and share safely, I’ve been using a small browser-only tool that can:
- generate a readable explanation of an exported n8n workflow JSON
- highlight a few heuristic risks
- produce a *sanitized* version of the JSON for public sharing (still: please double-check for secrets)

Demo (offline, no backend):  
`https://1993921.xyz/mimo-ai-delivery-factory/tools/n8n-json-explainer/`

If you can post a **sanitized** JSON (or the minimal failing part) in this public GitHub issue template, I can respond with a focused checklist + suggested refactor path:
`https://github.com/zjl4616/mimo-ai-delivery-factory/issues/new?template=p02-n8n-workflow-review-request.yml`

---

## D) n8n 社区论坛（中文，贴合“分享模板/担心泄露”场景）

**回复模板 — 分享/脱敏顾虑**

理解你对分享 workflow 的安全顾虑（credentials / webhook url / internal ids 等确实容易不小心暴露）。

我最近做了一个浏览器端离线小工具，用来把 n8n workflow JSON 变成可读文档，并提供一键脱敏（仍建议你自己再检查一遍）：
- Demo：`https://1993921.xyz/mimo-ai-delivery-factory/tools/n8n-json-explainer/`
- Repo：`https://github.com/zjl4616/mimo-ai-delivery-factory`

如果你愿意公开协作排查/改造，可以把“脱敏后的 JSON / 最小复现片段”贴到这个 GitHub Issue 模板里（公开留痕，方便协作）：
`https://github.com/zjl4616/mimo-ai-delivery-factory/issues/new?template=p02-n8n-workflow-review-request.yml`

