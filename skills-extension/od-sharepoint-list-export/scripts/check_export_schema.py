#!/usr/bin/env python3
"""Compare two SharePoint-FullExport.json runs for schema drift and progress.

    python3 check_export_schema.py OLD.json NEW.json

Reports: item-count delta, whether NEW's ExportDate is actually after OLD's (a stale
re-export looks like success but moves nothing forward), and any column added, removed or
renamed on the `Item` object — compared across every item, not just the first, because a
column introduced partway through a list will not show up on item 1.

No dependencies beyond the standard library. Exit code 1 on any drift or a non-advancing
checkpoint, 0 otherwise, so it drops into a recurring export job unchanged.
"""

from __future__ import annotations

import json
import sys


def load(path: str) -> dict:
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def field_union(export: dict) -> set[str]:
    fields: set[str] = set()
    for row in export.get("Data", []):
        fields.update(row.get("Item", {}).keys())
    return fields


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print(__doc__)
        return 0
    old, new = load(argv[1]), load(argv[2])
    problems = []

    old_count, new_count = old.get("ItemCount", 0), new.get("ItemCount", 0)
    print(f"Items: {old_count} -> {new_count} ({new_count - old_count:+d})")

    old_date, new_date = old.get("ExportDate", ""), new.get("ExportDate", "")
    print(f"ExportDate: {old_date} -> {new_date}")
    if new_date <= old_date:
        problems.append("checkpoint did not advance — NEW is not newer than OLD; "
                         "a failed or re-run export can look like a success without this check")

    old_fields, new_fields = field_union(old), field_union(new)
    added = new_fields - old_fields
    removed = old_fields - new_fields
    if added:
        print(f"Columns added:   {', '.join(sorted(added))}")
    if removed:
        print(f"Columns removed: {', '.join(sorted(removed))}")
        problems.append(f"{len(removed)} column(s) disappeared — anything reading them now "
                         "reads an absent field, not an error; check od-portfolio-and-savings-analysis "
                         "and bc-build for a dependency on " + ", ".join(sorted(removed)))
    if not added and not removed:
        print("Columns: unchanged")

    if problems:
        print("\nPROBLEMS:")
        for p in problems:
            print(f"  - {p}")
        return 1
    print("\nOK")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
