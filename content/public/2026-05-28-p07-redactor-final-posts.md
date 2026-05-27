**中文主帖 (可直接粘贴)**

大家好，我们注意到在 n8n 社区中，一个常见的求助方式是“请贴出你的 workflow JSON”。然而，直接导出的 JSON 文件通常包含了凭证名称/ID、Webhook URL、API Token 等敏感信息。许多用户并不清楚应该删除哪些字段、删除到什么程度才安全，常常在“方便复现”与“信息安全”之间纠结。

补充一个可引用的公开依据：n8n 官方的导出/导入文档里也提到了导出时的 **“remove credentials（清除凭证）”** 选项，说明“分享/导出前要注意凭证信息”本身就是官方承认的风险点（https://docs.n8n.io/workflows/export-import/）。另外社区里也有人专门讨论 “workflow JSON 会泄露 credentials/token 的常见原因与修复方式”（https://community.n8n.io/t/why-your-n8n-workflow-json-is-leaking-credentials-and-the-architectural-fix/289576）。

为此，我们提供一个**纯前端的离线工具**来帮助大家解决这个痛点。

**核心功能：**
1.  **一键脱敏**：粘贴你的 workflow JSON，工具会自动移除凭证引用、HTTP请求中的认证头、Webhook URL、Token 等敏感信息。
2.  **脱敏报告**：清晰展示工具具体修改和删除了哪些路径，让你完全知情。
3.  **标准求助模板**：自动生成一份包含必要说明（如使用场景、遇到的问题）和免责声明的 Markdown 模板，方便你发起更高效、更安全的求助。

**特点与承诺：**
-   **完全离线**：工具在浏览器本地运行，**绝不上传你的 JSON 数据到任何服务器**。你的 workflow 内容始终只存在于你的设备上。
-   **人工复核**：自动化脱敏后，仍建议你快速浏览一遍确认，工具无法保证 100% 覆盖所有边缘情况。
-   **免费公益**：此工具旨在降低社区交流门槛，提升求助安全性。

**如何使用：**
1.  访问工具页面：https://1993921.xyz/mimo-ai-delivery-factory/tools/n8n-workflow-redactor/
2.  将你的 workflow JSON 粘贴到文本框。
3.  点击“脱敏”，获取安全版本及报告。
4.  参考生成的模板发起你的社区求助帖。

我们希望通过这个小工具，能让社区互助更顺畅、更安心。对于需要更深度工作流安全与可靠性分析的用户，我们后续也会有更专业的服务（`offers/p02-n8n-security-review/`），敬请关注。

感谢大家的使用与反馈！

---
**English Version (for Community Post)**

**Subject: Share Workflows Safely: New Offline JSON Redactor for n8n**

Hi everyone,

We've noticed a common pattern in n8n help requests: "Please share your workflow JSON." However, exported JSONs often contain sensitive data like credential names, webhook URLs, and API tokens. Users are often unsure what to delete, balancing between **reproducibility** and **security**.

To help with this, we've built a **purely frontend, offline tool**.

**What it does:**
1.  **One-Click Redaction:** Paste your workflow JSON, and the tool automatically removes sensitive info (credential refs, auth headers, webhook URLs, tokens).
2.  **Redaction Report:** See exactly which paths were modified or deleted.
3.  **Help Template Generator:** Creates a standard Markdown template for your help post, including key details and a disclaimer.

**Key Points:**
-   **100% Offline:** Runs entirely in your browser. **No data is ever uploaded.** Your workflow stays on your machine.
-   **Manual Review Recommended:** While the tool is robust, always do a quick final check.
-   **Free & Community-Focused:** Built to lower barriers and improve safety in community support.

**How to Use:**
1.  Visit the tool: https://1993921.xyz/mimo-ai-delivery-factory/tools/n8n-workflow-redactor/
2.  Paste your workflow JSON.
3.  Click "Redact" to get a safe version and report.
4.  Use the generated template to post your help request.

Our goal is to make community help-sharing safer and smoother. For users needing deeper security/reliability reviews for critical workflows, a dedicated service is in development (`offers/p02-n8n-security-review/`).

We hope this tool is helpful. Thanks for your feedback!

---
**5 评论区回复模板**

1.  **（针对询问安全性）**
    > 感谢提问！这个工具是**纯前端、离线运行**的。所有处理都在你的浏览器本地完成，代码开源可查（如果你访问的是 GitHub 页面），我们**绝不上传或存储你的任何 JSON 数据**。你的隐私和安全是第一位的。

2.  **（针对“这解决了我的问题”）**
    > 很高兴这个工具能帮到你！是的，它能快速去掉那些麻烦又敏感的字段，让你专注于描述问题本身。如果生成的模板或报告有需要调整的地方，也欢迎随时反馈。

3.  **（针对“链接在哪里”或“怎么使用”）**
    > 使用链接在此：`https://1993921.xyz/mimo-ai-delivery-factory/tools/n8n-workflow-redactor/`。流程很简单：粘贴 JSON -> 点击脱敏 -> 复制输出的干净 JSON 和报告，然后就可以使用下方自动生成的模板来发帖求助了。

4.  **（针对提出功能建议或发现边界情况）**
    > 非常感谢你的细致测试和宝贵建议！你发现的这个情况很有价值，我们会记录下来用于改进工具的脱敏规则。社区的反馈是让工具变得更好的重要动力。

5.  **（通用友好回复/引导至更深度服务）**
    > 谢谢你的认可！我们希望通过这个小工具先解决最常见的安全分享问题。如果你的工作流涉及核心业务、复杂安全设计或需要全面的架构审查，我们正在准备更深度的 **n8n Workflow Security & Reliability Review** 服务，可以关注后续动态（`offers/p02-n8n-security-review/`）。
