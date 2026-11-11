#!/usr/bin/env python3
"""Add the OD part to an OpenSpec change that OpenSpec itself created.

    python3 new_handover.py <path-to-openspec/changes/<change-id>> [--with-config]

OpenSpec writes the change (`openspec new change <change-id> --store <store>`, then its own skills fill
proposal, specs, design and tasks; see ../references/openspec/skills/). This script adds only what OD carries on
top: handover.md (the OD annex, from ../assets/openspec/change/handover.md.tmpl) and attachments/ for the user's
files. --with-config also writes <root>/openspec/config.yaml (OD context and per-artifact rules) when the store
has none. Never overwrites. Standard library only.
"""
from __future__ import annotations

import argparse
import datetime
import pathlib
import sys

ASSETS = pathlib.Path(__file__).resolve().parent.parent / "assets" / "openspec"


def render(src: pathlib.Path, dst: pathlib.Path, values: dict) -> None:
    if dst.exists():
        sys.exit(f"refusing to overwrite {dst}")
    text = src.read_text(encoding="utf-8")
    for k, v in values.items():
        text = text.replace("{" + k + "}", v)
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(text, encoding="utf-8")
    print("wrote", dst)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("change", help="the change folder OpenSpec created: <root>/openspec/changes/<change-id>")
    ap.add_argument("--with-config", action="store_true")
    a = ap.parse_args()
    change = pathlib.Path(a.change)
    if not (change / ".openspec.yaml").is_file():
        sys.exit(f"{change} is not an OpenSpec change: create it first with "
                 "`openspec new change <change-id> --store <store>` (see references/openspec/skills/openspec-new-change)")
    if change.parent.name != "changes" or change.parent.parent.name != "openspec":
        sys.exit("the change must sit at <root>/openspec/changes/<change-id>")
    values = {"change_id": change.name, "date": datetime.date.today().isoformat()}
    render(ASSETS / "change" / "handover.md.tmpl", change / "handover.md", values)
    (change / "attachments").mkdir(exist_ok=True)
    keep = change / "attachments" / ".gitkeep"
    if not keep.exists():
        keep.write_text("", encoding="utf-8")   # the user's own files go here; register each in the annex
    if a.with_config:
        config = change.parent.parent / "config.yaml"
        bare = config.exists() and [ln.strip() for ln in config.read_text(encoding="utf-8").splitlines()
                                    if ln.strip() and not ln.strip().startswith("#")] == ["schema: spec-driven"]
        if bare:
            config.unlink()   # OpenSpec's default holds only the schema line; the OD template keeps it and adds the rest
        if config.exists():
            print("kept", config, "(the store already has a project context; merge the OD context and rules from "
                  "assets/openspec/config.yaml.tmpl by hand)")
        else:
            render(ASSETS / "config.yaml.tmpl", config, values)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
