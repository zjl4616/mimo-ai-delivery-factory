# P02 Public Content Pack — n8n workflow JSON 脱敏与安全分享（科普帖 + 回复模板 + Checklist）

时间：2026-05-27  
产品：P02 n8n JSON 中文解释器（浏览器端离线运行）  
Demo：`https://1993921.xyz/mimo-ai-delivery-factory/tools/n8n-json-explainer/`  
Repo：`https://github.com/zjl4616/mimo-ai-delivery-factory`  
协作入口（公开 Issue intake）：`https://github.com/zjl4616/mimo-ai-delivery-factory/issues/new?template=p02-n8n-workflow-review-request.yml`

原则：
- 只在公开互联网渠道发布/回复（不使用私域/私聊）。
- 不承诺“必定解决”或“必有收益”，只提供可验证的工具与公开协作路径。
- 强调：离线运行、无后端、不上传数据；同时提醒用户自行检查脱敏结果。

---

## 1) n8n Community 论坛科普帖（英文 + 中文双语）

### 🇬🇧 English Version

**Title: Sharing n8n Workflows? Here’s How to Spot & Remove Sensitive Data Before Posting**

Hi everyone,

Sharing workflow JSON is great for learning, but it often accidentally includes API keys, passwords, or personal URLs. I built a free, offline tool that helps you review your JSON for common leaks before you share it publicly.

**Key points to check in your workflow JSON:**
- `credentials` sections (even if referenced by ID, sometimes tokens are inline)
- `httpRequest` headers, URLs, and body payloads
- `webhook` URLs (especially those with unique paths or query parameters)
- Hardcoded values in `executeCommand`, `readWriteFile`, or `code` nodes
- Any `binary` data property paths that might contain base64-encoded content

**Important:** This tool runs entirely in your browser (offline, no data sent anywhere). You still need to verify the results yourself, as some sensitive data might be deeply nested or obfuscated.

If you’d like a free, community-driven review of your **sanitized** workflow JSON, you can submit it as a GitHub Issue here:
👉 https://github.com/zjl4616/mimo-ai-delivery-factory/issues/new?template=p02-n8n-workflow-review-request.yml

Stay safe and happy automating!

---

### 🇨🇳 中文版

**标题：分享 n8n 工作流 JSON 前，如何自查并移除敏感信息？**

大家好，

分享工作流 JSON 对社区学习很有帮助，但它常常会不小心包含 API 密钥、密码或个人 URL。我做了一个免费的离线工具，可以帮助你在公开分享前检查 JSON 中的常见泄露点。

**自查时请重点关注这些字段：**
- `credentials` 部分（即使通过 ID 引用，有时令牌会直接写入）
- `httpRequest` 节点中的请求头、URL 和请求体
- `webhook` 的 URL（尤其是带有特定路径或查询参数的）
- 在 `executeCommand`、`readWriteFile` 或 `code` 节点中硬编码的值
- 任何 `binary` 数据属性路径（可能包含 base64 编码内容）

**请注意：** 此工具完全在浏览器中运行（离线、无数据上传）。你仍需自行验证检查结果，因为一些敏感数据可能被深层嵌套或经过混淆处理。

如果你想申请一次免费的、公开的 Review（只提交已脱敏 JSON），可以用这个 GitHub Issue 模板：
👉 https://github.com/zjl4616/mimo-ai-delivery-factory/issues/new?template=p02-n8n-workflow-review-request.yml

---

## 2) 公开回复模板（英文，3 个）

### Template ①：如何安全分享 workflow JSON

> Good question! Before sharing, you should sanitize your JSON to remove any hardcoded credentials, tokens, or private URLs. An easy way is to use a tool like the **n8n Workflow JSON Explainer** — it runs offline in your browser and highlights potential sensitive fields for you to review:  
> https://1993921.xyz/mimo-ai-delivery-factory/tools/n8n-json-explainer/  
> Remember: always double-check the output yourself, especially in `httpRequest` headers, `webhook` URLs, and `credentials` sections.  
> If you’d like a community review after sanitization, you can submit your cleaned JSON via GitHub Issue here:  
> https://github.com/zjl4616/mimo-ai-delivery-factory/issues/new?template=p02-n8n-workflow-review-request.yml

### Template ②：Expression/undefined/item-not-found 类错误求助

> These errors usually happen when a node is trying to reference data that doesn’t exist or isn’t mapped correctly. A common cause is when the workflow JSON was shared without the full `execute` data or with sanitized placeholders.  
> To debug:  
> 1) Check if the referenced field exists in the previous node’s output.  
> 2) Look for missing `item.json` or `item.binary` paths in expressions.  
> 3) Ensure static data or parameters weren’t removed during sanitization.  
> If you’re reviewing a sanitized JSON, you can use the **n8n Workflow JSON Explainer** to see which fields were flagged:  
> https://1993921.xyz/mimo-ai-delivery-factory/tools/n8n-json-explainer/  
> For a deeper look, you’re welcome to submit the (sanitized) JSON for a free public review:  
> https://github.com/zjl4616/mimo-ai-delivery-factory/issues/new?template=p02-n8n-workflow-review-request.yml

### Template ③：关心 credentials/安全的用户

> You’re right to be cautious — workflow JSONs can leak sensitive info if not cleaned properly. The **n8n Workflow JSON Explainer** is an offline tool (runs entirely in your browser) that helps you identify risky spots like hardcoded tokens, URLs, or credential references. It doesn’t upload your data:  
> https://1993921.xyz/mimo-ai-delivery-factory/tools/n8n-json-explainer/  
> Even after using such a tool, you should always manually verify the JSON before sharing. Things like `env` variables, `executeCommand` scripts, or `httpRequest` headers might still contain clues.  
> If you want a second set of eyes, you can submit your sanitized JSON for a free community review here:  
> https://github.com/zjl4616/mimo-ai-delivery-factory/issues/new?template=p02-n8n-workflow-review-request.yml

---

## 3) n8n 工作流 JSON 脱敏自查清单（中文，10 条）

1. **检查 `credentials` 节点引用**：确认是否存在内联的 `accessToken` / `apiKey` / `password` 明文。  
2. **审查所有 `httpRequest` 节点**：检查 `url` / `headers` / `body` / `authentication`，移除硬编码密钥与私有域名。  
3. **清理 `webhook` URL**：避免暴露唯一识别符或敏感 query 参数。  
4. **移除 `executeCommand` / `code` 中的明文**：命令、脚本、变量里常出现密码或私有路径。  
5. **检查 `readWriteFile` 路径**：不要泄露本地路径或敏感文件名。  
6. **删除 `binary` 数据中的实际内容**：移除 base64 内容，仅保留结构说明。  
7. **审查 `env` / `staticData`**：不要把连接串/密钥放在静态数据里。  
8. **注意条件节点的硬编码值**：内部 ID、私有枚举、业务规则可能泄露。  
9. **检查字符串拼接**：拼接后的字符串可能包含敏感片段（即使部分被移除）。  
10. **最终确认：n8n 不会自动清理你手动填入的任何明文**：节点参数、标题、表达式里的内容都必须你自己识别并移除。  

