from __future__ import annotations

import argparse
import csv
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TRACKER = ROOT / "templates" / "lead-tracker.csv"


def main() -> None:
    parser = argparse.ArgumentParser(description="Append a lead to the local tracker.")
    parser.add_argument("--name", required=True)
    parser.add_argument("--channel", required=True)
    parser.add_argument("--url", default="")
    parser.add_argument("--pain", default="")
    parser.add_argument("--score", default="")
    args = parser.parse_args()

    with TRACKER.open("a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(
            [
                args.name,
                args.channel,
                args.url,
                args.pain,
                date.today().isoformat(),
                "",
                args.score,
                "no",
                "",
                "new",
            ]
        )

    print(TRACKER)


if __name__ == "__main__":
    main()
