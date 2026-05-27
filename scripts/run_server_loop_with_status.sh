#!/usr/bin/env bash
set -u

BASE="/home/ubuntu/mimo-token-to-cash"
WEB_ROOT="/var/www/1993921.xyz/mimo-ai-delivery-factory"
LOG_FILE="$BASE/logs/cron.log"

mkdir -p "$BASE/logs" "$WEB_ROOT/dashboard"

{
  printf '\n[%s] loop start\n' "$(date '+%Y-%m-%d %H:%M:%S %z')"
} >> "$LOG_FILE"

/usr/bin/python3 "$BASE/server_loop.py" >> "$LOG_FILE" 2>&1
loop_status=$?

/usr/bin/python3 "$BASE/repo/scripts/status_snapshot.py" \
  --output "$WEB_ROOT/dashboard/status.json" >> "$LOG_FILE" 2>&1 || true

{
  printf '[%s] loop exit=%s status snapshot refreshed\n' "$(date '+%Y-%m-%d %H:%M:%S %z')" "$loop_status"
} >> "$LOG_FILE"

exit "$loop_status"
