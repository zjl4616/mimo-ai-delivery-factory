param(
  [string]$RepoRoot = "D:\Codex\mimo-ai-delivery-factory",
  [string]$VaultRoot = "D:\Obsidian",
  [string]$Model = "mimo-v2.5",
  [int]$MaxTokens = 2200
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)
$OutputEncoding = [System.Text.UTF8Encoding]::new($false)

function U([string]$Hex) {
  $chars = New-Object System.Collections.Generic.List[char]
  foreach ($part in $Hex -split ' ') {
    if ($part.Trim().Length -gt 0) {
      $chars.Add([char][Convert]::ToInt32($part, 16))
    }
  }
  return -join $chars
}

$osDirName = (U "0041 0049 4E00 4EBA 516C 53F8 64CD 4F5C 7CFB 7EDF")
$logName = (U "6267 884C 65E5 5FD7 002E 006D 0064")
$poolName = (U "4EA7 54C1 5B9E 9A8C 6C60 002E 006D 0064")
$radarName = (U "4E92 8054 7F51 9700 6C42 96F7 8FBE 002E 006D 0064")
$confirmName = (U "786E 8BA4 961F 5217 002E 006D 0064")
$runSuffix = (U "002D 004D 0069 004D 006F 540E 53F0 5DE5 5382 8F93 51FA 002E 006D 0064")
$factoryTitle = (U "004D 0069 004D 006F 0020 540E 53F0 5DE5 5382 81EA 52A8 8FD0 884C")

$projectDir = Join-Path $VaultRoot (Join-Path $osDirName "08.GENERATED\MiMo-Token-To-Cash")
$logPath = Join-Path $projectDir $logName
$poolPath = Join-Path $projectDir $poolName
$radarPath = Join-Path $projectDir $radarName
$confirmPath = Join-Path $projectDir $confirmName
$outputDir = Join-Path $projectDir "runs"
$repoOutputDir = Join-Path $RepoRoot "generated\mimo-loop"

New-Item -ItemType Directory -Force -Path $outputDir, $repoOutputDir | Out-Null

$now = Get-Date
$stamp = $now.ToString("yyyy-MM-dd HH:mm:ss")
$fileStamp = $now.ToString("yyyyMMdd-HHmmss")

$pool = if (Test-Path $poolPath) { Get-Content -LiteralPath $poolPath -Raw -Encoding UTF8 } else { "" }
$radar = if (Test-Path $radarPath) { Get-Content -LiteralPath $radarPath -Raw -Encoding UTF8 } else { "" }
$recent = if (Test-Path $logPath) {
  (Get-Content -LiteralPath $logPath -Encoding UTF8 | Select-Object -Last 120) -join "`n"
} else {
  ""
}

$prompt = @"
You are the background factory for the MiMo Token-To-Cash 30-day experiment.

Reply in Simplified Chinese Markdown.

Hard boundaries:
- Do not use existing contacts, WeChat friends, Feishu groups, or private networks.
- Use public internet demand and existing public product experiments only.
- You may draft public outreach, pricing, and delivery materials, but do not impersonate, exaggerate cases, or guarantee revenue.
- Payment accounts, payment links, contracts, customer private data, and paid platform setup still need user confirmation.

Based on the product pool, demand radar, and recent execution log below, choose the single most valuable next action and produce something directly usable.

Output sections:
1. This run's choice
2. Why this choice
3. Concrete output
4. File-ready content
5. Next step
6. NEEDS_USER_CONFIRMATION (write "none" if none)

Prioritize:
- P01 export/CTA/sales copy
- P02 n8n JSON Chinese explainer
- P03 customer reply draft generator
- P05 small business workflow template pack

[Product Pool]
$pool

[Demand Radar]
$radar

[Recent Log]
$recent
"@

$chatScript = Join-Path $RepoRoot "scripts\mimo_chat.ps1"
$result = & $chatScript -Model $Model -MaxTokens $MaxTokens -Prompt $prompt

$runFile = Join-Path $outputDir ($fileStamp + $runSuffix)
$repoRunFile = Join-Path $repoOutputDir "$fileStamp-loop-output.md"
if ([string]::IsNullOrWhiteSpace($result)) {
  $result = @"
# MiMo 后台工厂输出为空

时间：$stamp

本轮未获取到有效内容。可能原因：
- 模型返回为空或被截断
- 网络/服务抖动导致响应异常

建议：稍后重试一次；或降低 MaxTokens 以减少长输出失败风险。
"@
}

$result | Set-Content -LiteralPath $runFile -Encoding UTF8
$result | Set-Content -LiteralPath $repoRunFile -Encoding UTF8

# Update public dashboard status snapshot (sanitized, local)
try {
  $snapshotScript = Join-Path $RepoRoot "scripts\status_snapshot.py"
  $dashboardOut = Join-Path $RepoRoot "dashboard\status.json"
  if (Test-Path $snapshotScript) {
    & python $snapshotScript --base $RepoRoot --repo $RepoRoot --runs $outputDir --logs $repoOutputDir --output $dashboardOut | Out-Null
  }
} catch {
  # Dashboard generation must never break the loop.
}

$summary = ($result -split "`n" | Select-Object -First 40) -join "`n"
$entry = @"

## $stamp $factoryTitle

### Output files

- Obsidian: $runFile
- Repo: $repoRunFile

### Summary

$summary

"@

Add-Content -LiteralPath $logPath -Value $entry -Encoding UTF8

$hasConfirmation = ($result -match "NEEDS_USER_CONFIRMATION") -and ($result -notmatch "NEEDS_USER_CONFIRMATION\s*:?\s*(none|None|NONE)")
if ($hasConfirmation) {
  $queueDir = Join-Path $VaultRoot (Join-Path $osDirName "07.QUEUE\inbox")
  New-Item -ItemType Directory -Force -Path $queueDir | Out-Null
  $queueFile = Join-Path $queueDir "PROJECT-MiMo-$fileStamp-background-confirmation.md"
  $queueContent = @(
    "---",
    "type: confirmation",
    "project: MiMo Token-To-Cash 30-day growth experiment",
    "status: pending-review",
    "created: $stamp",
    "tags: [MiMo, confirmation, background-loop]",
    "---",
    "",
    "# PROJECT-MiMo-$fileStamp-background-confirmation",
    "",
    "Source file: ``$runFile``",
    "",
    "``````text",
    $result,
    "``````"
  ) -join "`n"
  $queueContent | Set-Content -LiteralPath $queueFile -Encoding UTF8
}

Write-Output "MiMo loop completed: $runFile"
