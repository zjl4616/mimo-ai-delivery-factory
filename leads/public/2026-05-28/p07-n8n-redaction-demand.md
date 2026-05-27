# P07 Demand Note — n8n workflow JSON 脱敏器（离线）

日期：2026-05-28

## 观察到的公开需求
- 很多 n8n 用户在社区求助时被要求“贴 workflow JSON”，但 workflow 导出通常会包含凭证相关信息（至少是 credential 的 name/id 之类标识符），以及 HTTP 请求节点里的 headers/auth/token/webhook URL 等。
- 用户往往不知道该删哪些字段、删到什么程度才安全；“为了复现”与“为了安全”冲突。

## 可交付的最小解决方案（Lead Magnet）
- 一个纯前端离线工具：粘贴/上传 workflow JSON → 一键脱敏 → 输出：
  - 脱敏后的 JSON（可复制/下载）
  - 脱敏报告（修改/删除了哪些路径）
  - 可公开求助的 Markdown 模板（含说明与免责声明）
- 价值：降低用户发帖阻力、提高求助质量、同时避免泄露风险。

## 导流到收入
- 免费：提供脱敏器 + 公开求助模板（引流 + 收集真实样本）。
- 付费：引导到 “n8n Workflow Security & Reliability Review” 服务（公开 mini-review 或付费深度 review），用 GitHub Issue intake 收集脱敏后的 JSON + 复现信息。

## 下一步（48h）
- 在一个公开渠道发 1 条帖子，强调：
  - 工具离线、不联网
  - 输出包含脱敏报告 + 求助模板
  - 仍需人工复核（不能保证 100%）
  - 引导链接：/tools/n8n-workflow-redactor/ 和 /offers/p02-n8n-security-review/

