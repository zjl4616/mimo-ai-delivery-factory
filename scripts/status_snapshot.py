#!/usr/bin/env python3
"""Create a sanitized public status snapshot for the MiMo project dashboard."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path


DEFAULT_BASE = Path(os.environ.get("MIMO_FACTORY_BASE", "/home/ubuntu/mimo-token-to-cash"))
DEFAULT_REPO = DEFAULT_BASE / "repo"
DEFAULT_RUNS = DEFAULT_BASE / "runs"
DEFAULT_LOGS = DEFAULT_BASE / "logs"


PRODUCTS = [
    {
        "id": "P01",
        "name": "AI 自动化机会评分器",
        "channel": "公开网页 / GitHub / SEO",
        "status": "online",
        "stage": "已上线",
        "progress": 72,
        "url": "https://1993921.xyz/mimo-ai-delivery-factory/tools/automation-scorecard/",
        "next": "增加导出报告、CTA，并启动公开推广。",
    },
    {
        "id": "P02",
        "name": "n8n JSON 中文解释器",
        "channel": "GitHub / n8n 社区搜索流量",
        "status": "building",
        "stage": "构建中",
        "progress": 28,
        "url": "",
        "next": "做脚本、示例 JSON 和网页 Demo。",
    },
    {
        "id": "P03",
        "name": "客户回复草稿生成器",
        "channel": "搜索 / 外贸内容 / 公开页面",
        "status": "queued",
        "stage": "待构建",
        "progress": 8,
        "url": "",
        "next": "做英文询盘和中文客服双场景 demo。",
    },
    {
        "id": "P04",
        "name": "自动化 ROI 单页生成器",
        "channel": "公开页面 / 报价前工具",
        "status": "queued",
        "stage": "待并入 P01",
        "progress": 12,
        "url": "",
        "next": "并入 P01 报告导出和报价前说明。",
    },
    {
        "id": "P05",
        "name": "小企业工作流模板包",
        "channel": "Gumroad / Ko-fi / GitHub",
        "status": "waiting",
        "stage": "等待",
        "progress": 5,
        "url": "",
        "next": "先做免费版 5 个模板。",
    },
]


def read_text(path: Path, limit: int = 8000) -> str:
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except FileNotFoundError:
        return ""
    return text[-limit:]


def command_output(args: list[str], cwd: Path | None = None) -> str:
    try:
        completed = subprocess.run(
            args,
            cwd=str(cwd) if cwd else None,
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            timeout=20,
        )
        return completed.stdout.strip()
    except Exception:
        return ""


def iso_from_timestamp(ts: float) -> str:
    return datetime.fromtimestamp(ts, tz=timezone.utc).astimezone().isoformat(timespec="seconds")


def status_from_age(minutes: float | None) -> str:
    if minutes is None:
        return "unknown"
    if minutes <= 45:
        return "healthy"
    if minutes <= 120:
        return "late"
    return "stale"


def extract_heading(text: str) -> str:
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("#") and not re.match(r"^#+\s*\d+\.", stripped):
            return stripped.lstrip("#").strip()[:120]
    choice = extract_section(text, "本轮选择") or extract_section(text, "This run's choice")
    if choice:
        return choice[:120]
    return "未识别标题"


def extract_section(text: str, title: str) -> str:
    pattern = re.compile(rf"^#+\s*(?:\d+\.\s*)?{re.escape(title)}\s*$", re.MULTILINE | re.IGNORECASE)
    match = pattern.search(text)
    if not match:
        return ""
    rest = text[match.end() :]
    next_heading = re.search(r"^#+\s+", rest, re.MULTILINE)
    section = rest[: next_heading.start()] if next_heading else rest
    return " ".join(line.strip(" -*\t") for line in section.splitlines() if line.strip())[:220]


def recent_runs(runs_dir: Path, limit: int = 5) -> list[dict[str, object]]:
    files = sorted(runs_dir.glob("*.md"), key=lambda p: p.stat().st_mtime, reverse=True)[:limit]
    runs: list[dict[str, object]] = []
    for path in files:
        text = read_text(path, 12000)
        runs.append(
            {
                "file": path.name,
                "updatedAt": iso_from_timestamp(path.stat().st_mtime),
                "title": extract_heading(text),
                "choice": extract_section(text, "本轮选择") or extract_section(text, "This run's choice"),
                "paymentReady": extract_section(text, "PAYMENT_READY") or "none",
                "needsUserConfirmation": extract_section(text, "NEEDS_USER_CONFIRMATION") or "none",
            }
        )
    return runs


def public_metrics(repo: Path, runs_dir: Path) -> dict[str, object]:
    online = sum(1 for p in PRODUCTS if p["status"] == "online")
    building = sum(1 for p in PRODUCTS if p["status"] == "building")
    run_count = len(list(runs_dir.glob("*.md"))) if runs_dir.exists() else 0
    git_head = command_output(["git", "rev-parse", "--short", "HEAD"], repo)
    git_branch = command_output(["git", "branch", "--show-current"], repo)
    return {
        "productsTotal": len(PRODUCTS),
        "productsOnline": online,
        "productsBuilding": building,
        "serverRuns": run_count,
        "promotionState": "素材已生成，尚未确认真实外部发布记录",
        "revenueState": "暂无付款记录",
        "git": {"branch": git_branch or "unknown", "head": git_head or "unknown"},
    }


def build_snapshot(base: Path, repo: Path, runs_dir: Path, logs_dir: Path) -> dict[str, object]:
    now = datetime.now().astimezone()
    run_files = sorted(runs_dir.glob("*.md"), key=lambda p: p.stat().st_mtime, reverse=True) if runs_dir.exists() else []
    latest_run = run_files[0] if run_files else None
    latest_run_at = iso_from_timestamp(latest_run.stat().st_mtime) if latest_run else None
    age_minutes = None
    if latest_run:
        age_minutes = round((datetime.now().timestamp() - latest_run.stat().st_mtime) / 60, 1)

    cron_log = logs_dir / "cron.log"
    server_log = logs_dir / "server-loop.log"
    health = status_from_age(age_minutes)

    return {
        "generatedAt": now.isoformat(timespec="seconds"),
        "project": {
            "name": "MiMo Token-To-Cash 30 天增长实验",
            "goal": "让 MiMo 在 30 天内持续产出可交付产品、推广素材和销售资产，验证付款闭环。",
            "publicSite": "https://1993921.xyz/mimo-ai-delivery-factory/",
            "dashboard": "https://1993921.xyz/mimo-ai-delivery-factory/dashboard/",
            "validUntil": "2026-06-27",
        },
        "health": {
            "status": health,
            "label": {"healthy": "运行正常", "late": "略有延迟", "stale": "需要检查", "unknown": "未知"}[health],
            "latestRunAt": latest_run_at,
            "latestRunAgeMinutes": age_minutes,
            "cron": "*/30 * * * * server_loop.py",
            "cronLogBytes": cron_log.stat().st_size if cron_log.exists() else 0,
            "serverLogBytes": server_log.stat().st_size if server_log.exists() else 0,
        },
        "metrics": public_metrics(repo, runs_dir),
        "products": PRODUCTS,
        "promotion": {
            "status": "ready_not_published",
            "label": "推广素材已准备，尚未记录正式外发",
            "nextChannels": ["GitHub README", "n8n 相关公开讨论", "技术社区长文", "SEO 页面"],
            "nextAction": "先发布 P01 工具介绍，再用 P02 承接 n8n 模板搜索需求。",
        },
        "confirmationQueue": [
            {
                "type": "payment",
                "status": "not_needed_yet",
                "text": "出现付款意向后，需要用户确认收款账号、付款链接或二维码。",
            }
        ],
        "recentRuns": recent_runs(runs_dir),
        "safety": {
            "publicSnapshot": True,
            "containsSecrets": False,
            "note": "状态文件只包含公开运营信息，不包含 Token、服务器密钥、私密客户资料或私人联系人。",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", type=Path, default=DEFAULT_BASE)
    parser.add_argument("--repo", type=Path, default=DEFAULT_REPO)
    parser.add_argument("--runs", type=Path, default=DEFAULT_RUNS)
    parser.add_argument("--logs", type=Path, default=DEFAULT_LOGS)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    snapshot = build_snapshot(args.base, args.repo, args.runs, args.logs)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(snapshot, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"wrote {args.output}")


if __name__ == "__main__":
    main()
