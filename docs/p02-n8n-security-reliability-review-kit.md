# n8n Workflow Security + Reliability Review

---

## Service Scope

This micro-offer provides a focused review of your n8n workflow configuration to identify security misconfigurations and common reliability pitfalls. The deliverable is a structured checklist with actionable recommendations, not a full penetration test or workflow development service.

**Includes:**
- Review of a single workflow (JSON) submitted via a public GitHub Issue.
- Analysis focused on credential exposure, node permissions, error handling, and data flow.
- Delivery of annotated checklist and a summary of high-priority findings.

**Excludes:**
- Custom workflow development or implementation of fixes.
- Review of workflow functionality or data correctness.
- Audit of the underlying n8n server or infrastructure security.

---

## 10-Item Security Checklist

*   [ ] **Hardcoded Credentials:** No credentials (API keys, passwords, tokens) are hardcoded directly in node configurations.
*   [ ] **Credential Reuse:** Credentials are not reused across unrelated or low-trust workflows.
*   [ ] **Environment Variables:** Secrets are managed via environment variables or n8n's credential storage, not in the workflow JSON.
*   [ ] **HTTP Node Security:** HTTP Request nodes use HTTPS and validate SSL certificates.
*   [ ] **Data Minimization:** Workflow does not unnecessarily copy or log sensitive data (like full user records).
*   [ ] **Webhook Security:** Webhook nodes have authentication enabled (basic auth, header auth) if publicly accessible.
*   [ ] **File Handling:** File read/write nodes use safe, non-system paths and sanitize file names.
*   [ ] **Third-Party Nodes:** Use of community nodes is audited for known vulnerabilities.
*   [ ] **Execution Logging:** Sensitive data (PII, secrets) is not logged to the n8n execution history.
*   [ ] **User Permissions:** Workflow is assigned to the most restrictive user/group role required.

---

## 10-Item Reliability Checklist

*   [ ] **Error Handling:** Critical nodes (e.g., HTTP, database) have error handlers (`ONERROR`) or catch branches.
*   [ ] **Timeout Configuration:** HTTP Request and other external call nodes have appropriate timeouts set.
*   [ ] **Retry Logic:** Workflows for critical tasks use built-in retry mechanisms for transient failures.
*   [ ] **Data Validation:** Key input data (from webhooks, databases) is validated before processing.
*   [ ] **Resource Cleanup:** Temporary files or database connections are explicitly closed or handled.
*   [ ] **Idempotency:** Workflows triggered by repeated events (webhooks) are safe to run multiple times.
*   [ ] **Node Configuration:** Nodes use explicit expressions instead of ambiguous default values.
*   [ ] **Version Control:** The workflow JSON is exported and version-controlled (e.g., in Git).
*   [ ] **Execution History:** Retention policies are set to prevent performance degradation from history buildup.
*   [ ] **Environment Segmentation:** Separate workflows or credentials are used for development vs. production.

---

## What NOT to Share

**DO NOT** include in your public GitHub Issue:
- **Actual Credentials:** API keys, passwords, OAuth secrets, database connection strings.
- **Personally Identifiable Information (PII):** Real user data, email addresses, or other sensitive content used in test runs.
- **Internal Hostnames/IPs:** Non-public server addresses, internal database hosts, or private API endpoints.
- **Specific License Keys:** Any proprietary or paid service keys.

**Safe to Share:**
- A sanitized `workflow.json` file with all credential nodes removed or replaced with `{{ CREDENTIAL_ID }}` placeholders.
- A "reduced repro" workflow that uses mock data and free public APIs to illustrate the issue.

---

## Disclaimer

This review is a best-effort analysis provided "as is" for educational and advisory purposes. It does not guarantee the security or reliability of any workflow. The recommendations are based on common best practices but may not address all potential threats or runtime scenarios. The final responsibility for securing and operating workflows in production lies with the workflow owner. This service does not constitute legal or professional security consultation.

---

## Pricing Options

| Tier | Description | Timeframe | Price |
| :--- | :--- | :--- | :--- |
| **Free Public Mini-Review** | Submit your sanitized workflow via a **public GitHub Issue**. We provide a brief public response highlighting 1-2 critical findings from the checklists above. | Best effort, no SLA | **Free** |
| **Paid Deep Review** | Submit your sanitized workflow via a **private GitHub Gist or email**. A detailed review (1-3 hours of work) with a fully annotated checklist, specific mitigation steps, and a summary report delivered as a PDF. | Within 7 business days | **$75 - $150 USD** |

*   Prices are for a single workflow review.
*   Payment via PayPal or Stripe. A quote will be provided after initial triage.
*   No guarantee of specific findings or outcome.

---

# n8n 工作流安全与可靠性审查

---

## 服务范围

本微型服务提供聚焦于您的 n8n 工作流配置的审查，旨在识别安全配置错误和常见的可靠性隐患。交付物是一份带有可操作建议的结构化清单，而非完整的渗透测试或工作流开发服务。

**包含内容：**
- 通过公开 GitHub Issue 提交的单个工作流（JSON）审查。
- 分析重点在于凭据暴露、节点权限、错误处理和数据流。
- 交付附有注释的清单和高优先级发现摘要。

**不包含内容：**
- 定制工作流开发或修复实施。
- 审查工作流的功能或数据正确性。
- 审核底层 n8n 服务器或基础设施安全。

---

## 10项安全清单

*   [ ] **硬编码凭据：** 没有凭据（API密钥、密码、令牌）被直接硬编码在节点配置中。
*   [ ] **凭据复用：** 凭据未被无关或低信任度工作流复用。
*   [ ] **环境变量：** 机密信息通过环境变量或n8n的凭据存储管理，而非工作流JSON中。
*   [ ] **HTTP节点安全：** HTTP Request节点使用HTTPS并验证SSL证书。
*   [ ] **数据最小化：** 工作流不会不必要地复制或记录敏感数据（如完整用户记录）。
*   [ ] **Webhook安全：** 如果Webhook节点可公开访问，则启用了身份验证（基本认证、头部认证）。
*   [ ] **文件处理：** 文件读/写节点使用安全的、非系统的路径并清理文件名。
*   [ ] **第三方节点：** 使用的社区节点经过已知漏洞审计。
*   [ ] **执行日志：** 敏感数据（PII、机密）未被记录到n8n执行历史中。
*   [ ] **用户权限

