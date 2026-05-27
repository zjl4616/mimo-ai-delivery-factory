"""Redact sensitive fields in n8n workflow JSON.

Best-effort, deterministic key-based redaction.

Usage:
  python tools/n8n-workflow-redactor/redact.py --in-place path1.json path2.json
  python tools/n8n-workflow-redactor/redact.py --input in.json --output out.json

Never assume this guarantees safety. Always review manually.
"""

from __future__ import annotations

import argparse
import json
import os
from copy import deepcopy
from pathlib import Path
from typing import Any, Iterable


DEFAULT_KEYWORDS = [
    "credential",
    "credentials",
    "password",
    "secret",
    "token",
    "apiKey",
    "apikey",
    "accessKey",
    "privateKey",
    "clientSecret",
    "authorization",
    "bearer",
    "webhook",
    "cookie",
    "set-cookie",
]


def _matches_key(key: str, keywords: Iterable[str]) -> bool:
    k = key.lower()
    for kw in keywords:
        if kw.lower() in k:
            return True
    return False


def _redact_value(value: Any) -> Any:
    if value is None:
        return None
    if isinstance(value, (int, float, bool)):
        return value
    if isinstance(value, str):
        if not value:
            return value
        return "REDACTED"
    return "REDACTED"


def redact_json(obj: Any, *, keywords: list[str] | None = None) -> Any:
    keywords = keywords or DEFAULT_KEYWORDS

    def walk(node: Any) -> Any:
        if isinstance(node, dict):
            out: dict[str, Any] = {}
            for k, v in node.items():
                if _matches_key(str(k), keywords):
                    out[k] = _redact_value(v)
                else:
                    out[k] = walk(v)
            return out
        if isinstance(node, list):
            return [walk(x) for x in node]
        return node

    return walk(obj)


def _read_json(path: Path) -> Any:
    # Try utf-8-sig first to handle BOM, then utf-8.
    data = path.read_bytes()
    for enc in ("utf-8-sig", "utf-8"):
        try:
            return json.loads(data.decode(enc))
        except Exception:
            continue
    return json.loads(data.decode("utf-8", errors="replace"))


def _write_json(path: Path, obj: Any) -> None:
    text = json.dumps(obj, ensure_ascii=False, indent=2, sort_keys=False)
    # Use UTF-8 with BOM for Windows/PowerShell friendliness.
    path.write_text(text + "\n", encoding="utf-8-sig")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--in-place", action="store_true")
    parser.add_argument("--input", type=str)
    parser.add_argument("--output", type=str)
    parser.add_argument("paths", nargs="*")
    args = parser.parse_args()

    if args.in_place:
        if not args.paths:
            raise SystemExit("--in-place requires one or more paths")
        for p in args.paths:
            path = Path(p)
            if not path.exists() or not path.is_file():
                continue
            try:
                obj = _read_json(path)
            except Exception:
                continue
            redacted = redact_json(obj)
            _write_json(path, redacted)
        return 0

    if not args.input or not args.output:
        raise SystemExit("Provide --input and --output, or use --in-place")

    inp = Path(args.input)
    outp = Path(args.output)
    obj = _read_json(inp)
    redacted = redact_json(obj)
    outp.parent.mkdir(parents=True, exist_ok=True)
    _write_json(outp, redacted)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
