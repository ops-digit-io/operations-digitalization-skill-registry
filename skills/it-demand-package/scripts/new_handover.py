#!/usr/bin/env python3
"""Scaffold an OpenSpec change folder for an OD handover to IT.

    python3 new_handover.py <out-dir> <change-id> [--capability <name>] [--with-config]

Writes <out-dir>/openspec/changes/<change-id>/ from the templates in ../assets/openspec/
(.tmpl files, written out as plain OpenSpec files). --with-config also writes
<out-dir>/openspec/config.yaml when the receiving repository has none. Never overwrites.
Standard library only.
"""
from __future__ import annotations
import argparse, datetime, pathlib, re, sys

KEBAB = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
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
    ap.add_argument("out_dir")
    ap.add_argument("change_id")
    ap.add_argument("--capability", default=None, help="first capability path (kebab-case)")
    ap.add_argument("--with-config", action="store_true")
    a = ap.parse_args()
    if not KEBAB.match(a.change_id):
        sys.exit("change id must be kebab-case, e.g. add-downtime-reason-capture")
    cap = a.capability or a.change_id.split("-", 1)[-1]
    if not all(KEBAB.match(seg) for seg in cap.split("/")):
        sys.exit("capability path segments must be kebab-case")
    values = {"change_id": a.change_id, "capability": cap, "date": datetime.date.today().isoformat()}
    root = pathlib.Path(a.out_dir) / "openspec"
    change = root / "changes" / a.change_id
    tmpl = ASSETS / "change"
    for src in sorted(tmpl.rglob("*.tmpl")):
        rel = src.relative_to(tmpl).with_suffix("")          # drop .tmpl
        parts = list(rel.parts)
        if parts[:2] == ["specs", "capability"]:
            parts = ["specs", *cap.split("/"), *parts[2:]]
        render(src, change.joinpath(*parts), values)
    (change / "attachments").mkdir(parents=True, exist_ok=True)
    (change / "attachments" / ".gitkeep").write_text("", encoding="utf-8")   # the user's own files go here; register each in the annex
    if a.with_config:
        render(ASSETS / "config.yaml.tmpl", root / "config.yaml", values)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
