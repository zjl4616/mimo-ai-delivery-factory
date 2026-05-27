param(
  [Parameter(Mandatory = $true)]
  [string]$Prompt,

  [string]$Model = "mimo-v2.5",
  [int]$MaxTokens = 2048,
  [string]$Language = "zh"
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)
$OutputEncoding = [System.Text.UTF8Encoding]::new($false)

$keyPath = Join-Path $env:USERPROFILE ".secrets\mimo-token-plan.key"
$key = (Get-Content -LiteralPath $keyPath -Raw).Trim()

$systemPrompt = if ($Language -eq "en") {
  "You are a practical delivery assistant. Reply in English unless the user asks otherwise."
} else {
  "You are a practical delivery assistant. Reply in Simplified Chinese unless the user explicitly asks for English."
}

$messages = @(
  @{ role = 'system'; content = $systemPrompt }
  @{ role = 'user'; content = $Prompt }
)

$body = @{
  model = $Model
  messages = $messages
  max_tokens = $MaxTokens
  temperature = 0.3
} | ConvertTo-Json -Depth 8

$client = New-Object System.Net.WebClient
$client.Encoding = [System.Text.UTF8Encoding]::new($false)
$client.Headers.Add("Authorization", "Bearer $key")
$client.Headers.Add("Content-Type", "application/json; charset=utf-8")

$json = $client.UploadString(
  "https://token-plan-sgp.xiaomimimo.com/v1/chat/completions",
  "POST",
  $body
)

$response = $json | ConvertFrom-Json

$response.choices[0].message.content
