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
