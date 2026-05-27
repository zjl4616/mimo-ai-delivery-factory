# P07 — Offline n8n workflow JSON redactor (Lead magnet → Issue intake)

日期：2026-05-28

## 目标（到 2026-06-27）
- 在公开渠道验证“workflow JSON 脱敏 + 求助模板”是否能带来真实样本与可交付的 review 机会。
- 目标 KPI（48h）：获取 ≥1 个脱敏后的真实 workflow JSON + 报错/现象描述（通过 GitHub Issue intake）。

## 用户画像（公开流量）
- n8n 用户在社区/Reddit/GitHub 讨论中遇到 workflow 报错、表达式报错、HTTP Request 鉴权失败、Webhook 触发异常等问题。
- 希望别人帮排查，但担心贴 JSON 会泄露凭证、客户信息、内部域名。

## 核心资产
- 工具：`/tools/n8n-workflow-redactor/`（离线脱敏器）
- 付费/交付承接：`/offers/p02-n8n-security-review/`（安全+可靠性审查）
- intake：GitHub Issue 模板（P02 已有）

## 机制（why it works）
- 把“我不敢贴 JSON”转化为“你可以贴脱敏 JSON + 报告 + 模板”，降低参与门槛。
- 脱敏报告 + 模板能让求助帖更结构化，提高回复率。
- 收到样本后可交付 mini-review（公开）或深度 review（付费）。

## 风险与规避
- 风险：工具无法保证 100% 脱敏 → 明确免责声明 + 10 条人工检查清单（在帖子和工具内强调）。
- 风险：过度脱敏导致不可复现 → 提供“内部讨论模式”（更宽松），并提示可只截取相关 nodes 片段。

## 下一步动作（不涉及私域）
- 等用户确认 1 个公开渠道后：
  - 发布 1 条主贴（工具介绍 + 使用方法 + 免责声明）
  - 在 3–5 个相关求助帖下用模板回复，引导到脱敏器 + Issue intake

