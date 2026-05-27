# Public Outreach Pack — P02 n8n JSON 中文解释器

时间：2026-05-27  
目标：在公开渠道发布免费工具，吸引“看不懂 n8n JSON / 模板”的真实需求，导向公开合作与交付（不引导私域）。

## 1) Reddit 发帖（英文）

**Title (Option A)**: I built a browser-only Chinese explainer for n8n workflow JSON (offline, no backend)  
**Title (Option B)**: Paste n8n workflow JSON → get a readable doc + risk checklist (browser-only)

**Body**

Hi folks — I often see people sharing n8n templates, but the JSON is still hard to read / review quickly.

So I built a tiny **browser-only** tool that:
- parses an exported n8n workflow JSON
- generates a **readable explanation** (node list + simplified flow overview)
- adds a small **risk checklist** (heuristics like timeout / secrets / error-handling)

It runs **fully offline** (no server, no external CDN).  

- Demo: `https://1993921.xyz/mimo-ai-delivery-factory/tools/n8n-json-explainer/`  
- Source: `https://github.com/zjl4616/mimo-ai-delivery-factory`

Feedback welcome — especially which node types should be explained first.

## 2) Reddit 发帖（中文）

**标题（备选 A）**：我做了个“n8n 工作流 JSON 中文解释器”（纯前端离线可用）  
**标题（备选 B）**：粘贴 n8n workflow JSON → 生成中文说明 + 风险清单（无需后端）

**正文**

大家好，我观察到 n8n 模板越来越多，但很多人拿到 workflow JSON 以后还是很难快速理解、review、改造。

我做了一个小工具（**纯前端、离线可用**）：  
- 粘贴/导入 n8n workflow JSON  
- 自动生成：节点中文解释、简化流程概览、风险点清单（启发式）  

不需要后端，不走外部 CDN，不上传数据。

- Demo：`https://1993921.xyz/mimo-ai-delivery-factory/tools/n8n-json-explainer/`  
- 源码：`https://github.com/zjl4616/mimo-ai-delivery-factory`

欢迎提需求：你最希望优先支持哪些节点的中文解释？

## 3) HN/Show HN（英文）

**Title**: Show HN: Offline explainer for n8n workflow JSON → readable doc + risk checklist  

**Text**

I built a small static tool to turn an exported n8n workflow JSON into a readable explanation (flow overview + node descriptions + heuristic risks).  
Runs fully offline in the browser (no backend, no CDN).

Demo: `https://1993921.xyz/mimo-ai-delivery-factory/tools/n8n-json-explainer/`  
Repo: `https://github.com/zjl4616/mimo-ai-delivery-factory`

## 4) GitHub Issue 模板（公开合作/交付）

如果有人在公开渠道回复“能不能帮我看一下模板/改一下流程”，把 TA 引导到 GitHub Issue（公开、留痕、可交付）。

**Issue title**

`[P02] n8n workflow review request (sanitized)`

**Issue body**

- Goal / desired outcome:
- Current pain:
- Workflow JSON (sanitized / secrets removed):
- Any constraints (tools, data sources, compliance):

Notes:
- Please remove any credentials/tokens before posting.
- I will respond with risk checklist + suggested refactor plan.



---

## 5) 新增：公开协作脱敏入口（更易获得真实样本）

为了让大家更愿意贴出 workflow JSON（又不泄露凭证），P02 工具新增了 **一键脱敏**：

- 在工具页点击「公开协作：一键脱敏（推荐）」→「生成脱敏 JSON」
- 复制脱敏 JSON，粘贴到 GitHub Issue 模板（公开留痕，方便协作交付）

GitHub Issue 模板（公开）：
- `https://github.com/zjl4616/mimo-ai-delivery-factory/issues/new?template=p02-n8n-workflow-review-request.yml`

提醒：Issue 是公开的，请务必脱敏后再发。
