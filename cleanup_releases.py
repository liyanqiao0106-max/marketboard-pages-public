"""Delete only this dashboard's snapshot releases older than 90 UTC days."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from datetime import date, timedelta


def obsolete(tags: list[dict], today: date) -> list[str]:
    cutoff = today - timedelta(days=90)
    result = []
    for item in tags:
        tag = item.get("tagName", "")
        if not re.fullmatch(r"snapshot-\d{4}-\d{2}-\d{2}", tag):
            continue
        try:
            if date.fromisoformat(tag[9:]) < cutoff:
                result.append(tag)
        except ValueError:
            continue
    return result


def main() -> None:
    tags = json.load(sys.stdin)
    for tag in obsolete(tags, date.today()):
        subprocess.run(["gh", "release", "delete", tag, "--yes", "--cleanup-tag"], check=True)
        print(f"Deleted {tag}")


if __name__ == "__main__":
    main()
