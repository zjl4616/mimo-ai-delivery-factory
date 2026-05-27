from __future__ import annotations

import argparse
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "templates" / "proposal.md"


def main() -> None:
    parser = argparse.ArgumentParser(description="Draft a fixed-scope AI automation proposal.")
    parser.add_argument("--client", required=True)
    parser.add_argument("--workflow", required=True)
    parser.add_argument("--price", default="RMB 1,999 to 4,999")
    parser.add_argument("--out", default="")
    args = parser.parse_args()

    text = TEMPLATE.read_text(encoding="utf-8")
    text = text.replace("Client:\n", f"Client: {args.client}\n")
    text = text.replace("Workflow:\n", f"Workflow: {args.workflow}\n")
    text = text.replace("Fixed fee:\n", f"Fixed fee: {args.price}\n")

    out = Path(args.out) if args.out else ROOT / "generated" / f"{safe(args.client)}-{safe(args.workflow)}-proposal.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    print(out)


def safe(value: str) -> str:
    return "".join(ch.lower() if ch.isalnum() else "-" for ch in value).strip("-")


if __name__ == "__main__":
    main()
