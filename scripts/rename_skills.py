#!/usr/bin/env python3
"""Rename skills by a map file: folders, every mention in the repository, and an alias for the old name.

    python3 scripts/rename_skills.py config/skill-renames-2026-11-11.yaml [--dry]

A mention is the old name as a whole token. Left alone: names inside a `references/<old>/` path (absorbed procedures
keep their folder), department package names (`<old>.zip`, `<old>.skill`), log.md (history), and the OpenSpec copy.
Each renamed SKILL.md gets `metadata.aliases` with the old name (plus the convention's aliases such as eCR).
Generated files (indexes, maps, ratings, the deliverables contract) are rebuilt afterwards by their own scripts.
"""
from __future__ import annotations

import pathlib
import re
import subprocess
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import skillpaths  # noqa: E402

TEXT = {".md", ".yaml", ".yml", ".py", ".html", ".json", ".mermaid", ".txt", ".js", ".sh", ".tmpl", ".example", ".csv"}
SKIP = {"log.md", "rename_skills.py"}   # and every config/skill-renames-*.yaml map (see main)


def main(argv: list[str]) -> int:
    cfg = yaml.safe_load((ROOT / argv[0]).read_text(encoding="utf-8"))
    renames: dict[str, str] = cfg["renames"]
    extra: dict[str, list[str]] = cfg.get("extra_aliases") or {}
    dry = "--dry" in argv
    ids = set(skillpaths.all_ids())
    assert set(renames) <= ids, sorted(set(renames) - ids)
    targets = list(renames.values())
    assert len(set(targets)) == len(targets) and not (set(targets) & (ids - set(renames))), "name clash"
    # longest names first, so od-context-freshness is not hit by od-context
    pats = [(re.compile(r"(?<![\w.-])(?<!references/)" + re.escape(o) + r"(?![\w-])(?!\.zip|\.skill)"), n)
            for o, n in sorted(renames.items(), key=lambda kv: -len(kv[0]))]
    files = subprocess.run(["git", "-C", str(ROOT), "ls-files"], capture_output=True, text=True).stdout.splitlines()
    changed = 0
    for rel in files:
        p = ROOT / rel
        if p.name in SKIP or p.name.startswith("skill-renames-") or p.suffix not in TEXT or skillpaths.is_vendored(p) or not p.is_file():
            continue
        b = p.read_bytes()
        try:
            t = b.decode("utf-8")
        except UnicodeDecodeError:
            continue
        n = t
        for pat, new in pats:
            n = pat.sub(new, n)
        if n != t:
            changed += 1
            if not dry:
                p.write_bytes(n.encode("utf-8"))
    print(f"{'would change' if dry else 'changed'} {changed} files")
    if dry:
        return 0
    for old, new in renames.items():
        src = skillpaths.skill_dir(old)
        subprocess.run(["git", "-C", str(ROOT), "mv", str(src), str(src.parent / new)], check=True)
    for old, new in renames.items():
        p = skillpaths.LIBRARIES[skillpaths.library_of(new)] / new / "SKILL.md"
        b = p.read_bytes().decode("utf-8")
        nl = "\r\n" if "\r\n" in b else "\n"
        aliases = [old, *extra.get(new, [])]
        line = f"  aliases: [{', '.join(aliases)}]   # former name (naming convention, 2026-11-11)"
        b = re.sub(rf"^  formerly: {re.escape(new)}\s*{re.escape(nl)}", "", b, count=1, flags=re.M)   # self-reference left by the rename
        b = re.sub(r"^(  id: " + re.escape(new) + r")(?=\r?$)", lambda m: m.group(1) + nl + line, b, count=1, flags=re.M)
        assert "aliases:" in b, new
        p.write_bytes(b.encode("utf-8"))
    print(f"renamed {len(renames)} skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
