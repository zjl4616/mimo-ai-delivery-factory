# P02 Reply Kit — n8n expression / JSON error threads (public-only)

Date: 2026-05-27

Use: reply to public threads on `community.n8n.io` or Reddit. Not for DMs. Not for spam.

Links (copy/paste):
- Tool demo (offline): https://1993921.xyz/mimo-ai-delivery-factory/tools/n8n-json-explainer/
- Public issue intake (sanitized JSON): https://github.com/zjl4616/mimo-ai-delivery-factory/issues/new?template=p02-n8n-workflow-review-request.yml
- Repo: https://github.com/zjl4616/mimo-ai-delivery-factory

## 1) English — "Invalid expression" checklist + tool

Hey — a few quick checks for “Invalid expression” issues in n8n:

1) **Make sure it’s an expression field** (not a plain text field). In most nodes you need to toggle the parameter into *Expression* mode.
2) **Wrapper format**: expression values typically need the `={{ ... }}` wrapper. Missing `=` or mismatched braces often yields this error.
3) **Quoting**: if you’re building strings, confirm you’re quoting literals properly (single vs double quotes) and not accidentally concatenating `undefined`.
4) **Field path**: verify the referenced field exists on the current item (check the incoming data shape). A typo in a JSON path can look like a syntax error.
5) **Minimal repro**: try isolating the smallest node chain where the expression fails.

If you want to share your workflow safely for debugging, I built a small **browser-only** tool that:
- turns an exported workflow JSON into a readable explanation
- includes a 1-click *sanitizer* (please double-check before sharing)

Tool (offline, no backend):  
https://1993921.xyz/mimo-ai-delivery-factory/tools/n8n-json-explainer/

If you’re okay with public collaboration, please post a **sanitized** minimal JSON (or the failing part) via this GitHub issue template, and I’ll reply with a structured checklist + refactor suggestions in the same public thread:  
https://github.com/zjl4616/mimo-ai-delivery-factory/issues/new?template=p02-n8n-workflow-review-request.yml

## 2) English — "JSON validation / import error" quick reply

A quick way to narrow down JSON validation/import errors:

- Confirm the JSON is a **workflow export** (not a node snippet) and includes required top-level keys.
- Try exporting again from the same n8n version (workflow schema changes across versions can break imports).
- If you copied JSON from a post, ensure it’s not truncated and doesn’t contain smart quotes.

If you want a safer way to share for debugging, here’s an offline browser tool that can generate a readable doc and sanitize obvious credential-like fields (still: double-check):  
https://1993921.xyz/mimo-ai-delivery-factory/tools/n8n-json-explainer/

Public issue intake (sanitized JSON):  
https://github.com/zjl4616/mimo-ai-delivery-factory/issues/new?template=p02-n8n-workflow-review-request.yml

## 3) 中文 — 表达式报错（Invalid expression）回复模板

我先给你一个最短排查清单（不用先贴敏感信息）：

1) **这个参数是否切到了 Expression 模式**（不是纯文本模式）  
2) **表达式外层格式**：很多场景需要 `={{ ... }}`，少了 `=` / 花括号不配对都会报错  
3) **引号**：字符串拼接时确认引号正确、不要把 `undefined/null` 拼进去  
4) **字段路径**：引用的字段在当前 item 里是否真的存在（先看输入数据结构）  
5) **最小复现**：把问题缩小到 1–2 个节点，看看是不是某个节点输出为空导致后续表达式失败  

如果你愿意公开协作排查，但担心泄露 credentials/webhook/url，我做了个浏览器端离线小工具（不上传数据）：
- 把 workflow JSON 变成可读文档
- 一键脱敏（仍建议你自己再检查一遍）

工具：  
https://1993921.xyz/mimo-ai-delivery-factory/tools/n8n-json-explainer/

如果方便，把“脱敏后的最小 JSON / 或只包含报错相关节点的 JSON”贴到这个 GitHub Issue 模板里（公开留痕、方便协作），我会在 issue 里交付一份结构化 Review（风险清单 + 改造建议）：  
https://github.com/zjl4616/mimo-ai-delivery-factory/issues/new?template=p02-n8n-workflow-review-request.yml

