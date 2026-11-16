#!/usr/bin/env python3
"""Compare two SharePoint-FullExport.json runs for schema drift and progress.

    python3 check_export_schema.py OLD.json NEW.json

Reports: item-count delta, whether NEW's ExportDate is actually after OLD's (a stale
re-export looks like success but moves nothing forward), and any column added, removed or
renamed on the `Item` object - compared across every item, not just the first, because a
column introduced partway through a list will not show up on item 1.

Requirements: Python 3.8 or newer, standard library only. No prompts.

Exit codes:
    0  OK - no drift, checkpoint advanced
    1  finding - a column was removed, or the checkpoint did not advance
    2  bad input - wrong argument count, file missing, not valid JSON, or not an export object
"""

from __future__ import annotations

import argparse
import json
import sys


class InputError(Exception):
    """The file cannot be used as an export; the message says which file and why."""


def load(path: str) -> dict:
    try:
        with open(path, encoding="utf-8") as fh:
            data = json.load(fh)
    except FileNotFoundError:
        raise InputError(f"{path}: file not found") from None
    except OSError as err:
        raise InputError(f"{path}: cannot be read ({err.strerror or err})") from None
    except json.JSONDecodeError as err:
        raise InputError(
            f"{path}: not valid JSON (line {err.lineno}, column {err.colno}: {err.msg}); "
            "re-run the export instead of editing the file"
        ) from None
    if not isinstance(data, dict):
        raise InputError(f"{path}: expected a JSON object with ItemCount, ExportDate and Data")
    if not isinstance(data.get("Data", []), list):
        raise InputError(f"{path}: 'Data' must be a list of rows")
    return data


def field_union(export: dict) -> set[str]:
    fields: set[str] = set()
    for row in export.get("Data", []):
        item = row.get("Item", {}) if isinstance(row, dict) else {}
        if isinstance(item, dict):
            fields.update(item.keys())
    return fields


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Compare two SharePoint-FullExport.json runs for schema drift and a non-advancing checkpoint.",
        epilog="Exit codes: 0 OK, 1 finding (removed column or checkpoint not advanced), 2 bad input.",
    )
    p.add_argument("old", metavar="OLD.json", help="the previous export")
    p.add_argument("new", metavar="NEW.json", help="the export just made")
    return p


def main(argv: list[str]) -> int:
    args = build_parser().parse_args(argv[1:])  # argparse exits with 2 on a wrong argument count
    try:
        old, new = load(args.old), load(args.new)
    except InputError as err:
        print(f"ERROR: {err}", file=sys.stderr)
        return 2
    problems = []

    old_count, new_count = old.get("ItemCount", 0), new.get("ItemCount", 0)
    print(f"Items: {old_count} -> {new_count} ({new_count - old_count:+d})")

    old_date, new_date = str(old.get("ExportDate", "")), str(new.get("ExportDate", ""))
    print(f"ExportDate: {old_date} -> {new_date}")
    if new_date <= old_date:
        problems.append("checkpoint did not advance - NEW is not newer than OLD; "
                        "a failed or re-run export can look like a success without this check")

    old_fields, new_fields = field_union(old), field_union(new)
    added = new_fields - old_fields
    removed = old_fields - new_fields
    if added:
        print(f"Columns added:   {', '.join(sorted(added))}")
    if removed:
        print(f"Columns removed: {', '.join(sorted(removed))}")
        problems.append(f"{len(removed)} column(s) disappeared - anything reading them now "
                        "reads an absent field, not an error; check bc-portfolio "
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
