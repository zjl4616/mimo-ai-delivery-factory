# MiMo Token Plan Setup

## Local Configuration

The working Token Plan key on this machine is stored outside the repository:

```text
C:\Users\Administrator\.secrets\mimo-token-plan.key
```

OpenCode is configured at:

```text
C:\Users\Administrator\.config\opencode\opencode.json
```

It declares:

```text
xiaomimimo/mimo-v2.5-pro
xiaomimimo/mimo-v2.5
```

## Verified API Probe

The OpenAI-compatible endpoint responded successfully:

```text
GET https://token-plan-sgp.xiaomimimo.com/v1/models
```

Returned models include:

- mimo-v2-omni
- mimo-v2-pro
- mimo-v2-tts
- mimo-v2.5
- mimo-v2.5-pro
- mimo-v2.5-tts
- mimo-v2.5-tts-voiceclone
- mimo-v2.5-tts-voicedesign

## Important Key Note

The Token Plan endpoint accepted the `tp-...` dedicated key from the local OpenClaw configuration. It rejected the `sk-...` key with HTTP 401.

## Usage Boundary

Use the key in supported coding/agent tools to produce work. Do not:

- publish the key
- commit the key
- resell the key
- expose it in a public backend
- run arbitrary customer API traffic through it

## Practical Use

Use MiMo heavily for:

- generating implementation plans
- writing code
- producing tests
- refactoring templates
- drafting proposals
- creating customer handoff docs
- producing course and content drafts

## Start It Working

The Token Plan is already connected locally in two ways:

1. OpenCode default model:

```text
xiaomimimo/mimo-v2.5-pro
```

2. Direct UTF-8 chat helper:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\mimo_chat.ps1 -Prompt "用中文写一个客户自动化服务方案"
```

Use the faster model for drafts:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\mimo_chat.ps1 -Model mimo-v2.5 -Prompt "生成10条中文获客私信"
```

Use the Pro model for harder planning or coding:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\mimo_chat.ps1 -Model mimo-v2.5-pro -Prompt "为一个询盘回复自动化项目写交付计划"
```

## Language

MiMo is not English-only. It follows the prompt and system message.

For Chinese, say:

```text
默认使用简体中文回答。
```

For English, say:

```text
Reply in English.
```

The most common Chinese failure on Windows is encoding, not model ability. Send request bodies as UTF-8 bytes and include:

```text
Content-Type: application/json; charset=utf-8
```
