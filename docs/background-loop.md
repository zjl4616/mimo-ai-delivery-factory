# Background Loop

The Codex app automation wakes an agent periodically, but the Windows background loop makes MiMo work even when the chat is not being actively used.

## Scripts

- `scripts/mimo_loop.ps1` - one background production run
- `scripts/install_mimo_loop_task.ps1` - installs the Windows Scheduled Task

## Schedule

Default: every 30 minutes for 31 days.

Task name:

```text
MiMo Token-To-Cash Background Loop
```

## What Each Run Does

1. Reads Obsidian product pool, demand radar, and recent execution log.
2. Calls MiMo through `scripts/mimo_chat.ps1`.
3. Generates one concrete next output.
4. Writes the result into:
   - `D:\Obsidian\AI一人公司操作系统\08.GENERATED\MiMo-Token-To-Cash\runs\`
   - `generated\mimo-loop\`
5. Appends a summary to Obsidian `执行日志.md`.
6. Creates a queue note only if user confirmation is actually needed.

## Manual Run

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File D:\Codex\mimo-ai-delivery-factory\scripts\mimo_loop.ps1
```

## Install Task

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File D:\Codex\mimo-ai-delivery-factory\scripts\install_mimo_loop_task.ps1
```

## Check Task

```powershell
Get-ScheduledTask -TaskName "MiMo Token-To-Cash Background Loop"
```
