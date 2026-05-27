param(
  [string]$TaskName = "MiMo Token-To-Cash Background Loop",
  [string]$RepoRoot = "D:\Codex\mimo-ai-delivery-factory",
  [int]$IntervalMinutes = 30
)

$ErrorActionPreference = "Stop"

$loopScript = Join-Path $RepoRoot "scripts\mimo_loop.ps1"
$action = New-ScheduledTaskAction `
  -Execute "powershell.exe" `
  -Argument "-NoProfile -ExecutionPolicy Bypass -File `"$loopScript`""

$trigger = New-ScheduledTaskTrigger -Once -At (Get-Date).AddMinutes(1) `
  -RepetitionInterval (New-TimeSpan -Minutes $IntervalMinutes) `
  -RepetitionDuration (New-TimeSpan -Days 31)

$settings = New-ScheduledTaskSettingsSet `
  -AllowStartIfOnBatteries `
  -DontStopIfGoingOnBatteries `
  -StartWhenAvailable `
  -MultipleInstances IgnoreNew

Register-ScheduledTask `
  -TaskName $TaskName `
  -Action $action `
  -Trigger $trigger `
  -Settings $settings `
  -Description "Runs the MiMo Token-To-Cash background loop every $IntervalMinutes minutes." `
  -Force | Out-Null

Write-Output "Installed scheduled task: $TaskName"
