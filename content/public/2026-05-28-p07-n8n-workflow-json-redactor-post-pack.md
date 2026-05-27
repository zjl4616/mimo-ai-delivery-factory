# P07 public post pack — n8n workflow JSON 脱敏器（离线）

日期：2026-05-28

> 原则：只做公开渠道，不触达私域联系人/群/私聊。内容不夸大，不承诺收入或效果。

## 1) 主贴（中文，适合 n8n Community / Reddit r/n8n）

标题候选：
- [Tool] Offline n8n workflow JSON redactor + “safe to share” help template
- 离线 n8n workflow JSON 脱敏器：一键去掉 credentials/token/webhook URL（附求助模板）

正文：
大家好，我做了一个**完全离线**的小工具：把 n8n workflow JSON 粘贴进去，它会在浏览器本地做脱敏并生成“可公开求助”的模板。

痛点：很多求助帖都会被要求贴 workflow JSON，但导出里经常夹着 `credentials`、HTTP headers/auth、token、webhook URL、邮箱/手机号、内网域名等敏感信息；不贴别人很难复现，贴了又不安全。

工具输出 3 样东西（都在本地生成，不联网）：
1) 脱敏后的 JSON（可复制/下载）
2) 脱敏报告（改了哪些路径）
3) 公开求助帖 Markdown 模板（结构化描述问题 + 附脱敏 JSON）

免责声明：任何自动脱敏都**不能保证 100% 安全**。发帖前请人工复核，不要分享 token / API key / webhook URL / 客户信息。

链接：
- 工具：`https://1993921.xyz/mimo-ai-delivery-factory/tools/n8n-workflow-redactor/`
- 如果你愿意，我也提供一次公开 mini-review / 付费深度 review（基于脱敏后的 JSON + 复现信息）：`https://1993921.xyz/mimo-ai-delivery-factory/offers/p02-n8n-security-review/`

欢迎反馈：你觉得还应该默认脱敏哪些字段？有没有你最担心泄露的字段路径？

---

## 2) 主贴（英文，适合 Reddit / Show HN 风格）

Title:
- Offline n8n workflow JSON redactor + public help template (no backend)

Body:
I built a small **offline** web tool to help n8n users share workflow JSON safely when asking for help.

Problem: many troubleshooting threads ask for full workflow JSON, but exports often contain sensitive bits (`credentials`, auth headers, tokens, webhook URLs, emails/phones, private domains). People either overshare or share too little to reproduce.

This tool runs fully in your browser (no network) and generates:
1) Redacted JSON (copy/download)
2) A redaction report (what paths changed)
3) A Markdown help template you can paste into forums/issues

Disclaimer: no tool can guarantee 100% safety. Please review manually before posting anything publicly.

Links:
- Tool: `https://1993921.xyz/mimo-ai-delivery-factory/tools/n8n-workflow-redactor/`
- Optional review offer (public mini-review or paid deep review): `https://1993921.xyz/mimo-ai-delivery-factory/offers/p02-n8n-security-review/`

Feedback welcome: which fields should be redacted by default?

---

## 3) 评论区/回复模板（把别人引导到脱敏器）

中文回复（对“请贴 workflow JSON”的场景）：
你可以先用这个离线脱敏器把 workflow JSON 处理一下再贴：它会去掉 credentials/token/webhook URL 等敏感字段，并生成求助模板（全程本地、不联网）。
工具：`https://1993921.xyz/mimo-ai-delivery-factory/tools/n8n-workflow-redactor/`

英文回复：
If you’re hesitant to paste the full workflow JSON publicly, you can run it through this offline redactor first (removes credentials/tokens/webhook URLs and gives you a help template).
Tool: `https://1993921.xyz/mimo-ai-delivery-factory/tools/n8n-workflow-redactor/`

