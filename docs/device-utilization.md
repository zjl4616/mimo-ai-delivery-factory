# Device Utilization

Use the available machines as a small delivery system, not as a token resale setup.

## Windows Workstation

Role:

- primary agent workstation
- MiMo API verification and local tooling
- Obsidian asset mining
- proposal generation
- GitHub publishing

Current confirmed assets:

- MiMo Token Plan key stored outside the repository
- OpenCode configured with MiMo models
- local preview server works on port 8765
- GitHub CLI authenticated as `zjl4616`

## Server

Role:

- public landing pages
- lightweight demos
- client-facing static assets
- optional n8n or automation runtime later

Current confirmed assets:

- SSH host alias: `server`
- web root is writable at `/var/www/1993921.xyz`
- published page path: `/var/www/1993921.xyz/mimo-ai-delivery-factory/`

Public URL:

- https://1993921.xyz/mimo-ai-delivery-factory/

## Feiniu NAS

Role:

- durable storage for knowledge base, examples, and client artifacts
- optional backup target for generated proposals and handoff packages

Current confirmed access:

- server can see Feiniu mounts under `/mnt/feiniu_*`
- Windows can reach NAS file sharing on `192.168.31.64`

Boundary:

- direct NAS SSH username is not confirmed yet

## Mac

Role:

- optional test machine for Apple-specific workflows, screenshots, or local app behavior

Boundary:

- no confirmed direct SSH target from this Windows session yet
- add SSH host details or enable Remote Login before assigning Mac-side work

## Deployment Rule

Prefer this order:

1. Local preview for fast iteration.
2. Server static path for immediately shareable public links.
3. GitHub Pages as backup/public proof after account Pages settings are healthy.

## Client Data Rule

Do not place private client data in the public repository or public web root. Use local generated files, private NAS folders, or a private repo for real delivery artifacts.
