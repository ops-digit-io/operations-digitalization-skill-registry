#!/usr/bin/env python3
"""The file set every skill ships, declared in config/skill-deliverables.yaml and checked by validate_registry.py.

    python3 scripts/skill_deliverables.py --draft     # rewrite the contract from the folders as they are now (review the diff)

The contract lists, per skill, every file the skill ships besides SKILL.md and the generated index.md files. The check
(`check()`, called by validate_registry.py) fails when:
  - a skill has no entry, or an entry names a skill that does not exist;
  - a declared file is missing or empty;
  - a shipped file is not declared (adding a file to a skill means declaring it);
  - a declared file cannot be reached by Markdown links from SKILL.md, unless it is listed under `unlinked` (scripts,
    examples and vendored files that are used by path, not linked); an `unlinked` file that is in fact linked is an error;
  - a core skill's SKILL.md lacks one of the sections config/skill-quality.yaml expects (an extension skill only warns).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
import skillpaths as skp  # noqa: E402

CONTRACT = ROOT / "config" / "skill-deliverables.yaml"
QUALITY = ROOT / "config" / "skill-quality.yaml"
LINK = re.compile(r"\]\(\s*<?([^)\s>#]+)")
SKIP_NAMES = {"SKILL.md", "index.md"}


def shipped(name: str) -> list[str]:
    base = skp.skill_dir(name)
    return sorted(p.relative_to(base).as_posix() for p in base.rglob("*")
                  if p.is_file() and p.name not in SKIP_NAMES and "__pycache__" not in p.parts and p.suffix != ".pyc")


def linked(name: str) -> set[str]:
    """Files reachable from SKILL.md through Markdown links (followed through .md files only)."""
    base = skp.skill_dir(name).resolve()
    seen: set[Path] = set()
    stack = [base / "SKILL.md"]
    while stack:
        cur = stack.pop()
        if cur.suffix != ".md" or not cur.is_file():
            continue
        for href in LINK.findall(cur.read_text(encoding="utf-8")):
            if href.startswith(("http://", "https://", "mailto:")):
                continue
            target = (cur.parent / href).resolve()
            if target.is_file() and base in target.parents and target not in seen and target.name != "index.md":
                seen.add(target)
                stack.append(target)
    return {p.relative_to(base).as_posix() for p in seen}


def draft() -> None:
    out = {"skills": {}}
    for name in skp.all_ids():
        files, ok = shipped(name), linked(name)
        entry: dict = {"files": files}
        loose = [f for f in files if f not in ok]
        if loose:
            entry["unlinked"] = loose
        out["skills"][name] = entry
    header = ("# What each skill ships (every file except SKILL.md and the generated index.md files). Checked by\n"
              "# scripts/validate_registry.py via scripts/skill_deliverables.py. Add a file to a skill, add it here.\n"
              "# `unlinked`: shipped files that SKILL.md and its references do not link to (scripts, examples, vendored\n"
              "# files); they are used by path. Keep this list short: link the file instead where you can.\n")
    CONTRACT.write_text(header + yaml.safe_dump(out, sort_keys=True, allow_unicode=True, width=120), encoding="utf-8")
    print(f"wrote {CONTRACT.relative_to(ROOT)}: {len(out['skills'])} skills, "
          f"{sum(len(v['files']) for v in out['skills'].values())} files")


def required_sections() -> list[tuple[str, list[str]]]:
    cfg = yaml.safe_load(QUALITY.read_text(encoding="utf-8")) or {}
    return [(h["heading"], h.get("alternatives", [])) for h in cfg.get("expected_headers", [])]


def check(fail) -> None:
    contract = (yaml.safe_load(CONTRACT.read_text(encoding="utf-8")) or {}).get("skills", {}) if CONTRACT.exists() else None
    if contract is None:
        fail("config/skill-deliverables.yaml is missing (python3 scripts/skill_deliverables.py --draft)")
        return
    ids = set(skp.all_ids())
    for name in sorted(set(contract) - ids):
        fail(f"skill-deliverables.yaml names '{name}' but no such skill exists")
    sections = required_sections()
    for name in sorted(ids):
        where = f"{skp.folder_of(name)}/{name}"
        entry = contract.get(name)
        if entry is None:
            fail(f"{where}/: no entry in config/skill-deliverables.yaml")
            continue
        declared, loose = set(entry.get("files") or []), set(entry.get("unlinked") or [])
        base = skp.skill_dir(name)
        for rel in sorted(declared):
            f = base / rel
            if not f.is_file():
                fail(f"{where}/: declared file '{rel}' is missing")
            elif f.stat().st_size == 0 or (f.suffix == ".md" and not f.read_text(encoding="utf-8").strip()):
                fail(f"{where}/: declared file '{rel}' is empty")
        for rel in sorted(set(shipped(name)) - declared):
            fail(f"{where}/: ships '{rel}' but it is not declared in config/skill-deliverables.yaml")
        for rel in sorted(loose - declared):
            fail(f"{where}/: 'unlinked' lists '{rel}', which is not a declared file")
        ok = linked(name)
        for rel in sorted(declared - ok - loose):
            fail(f"{where}/: '{rel}' is not linked from SKILL.md or from a file it links to (link it, or list it under unlinked)")
        for rel in sorted(loose & ok):
            fail(f"{where}/: '{rel}' is listed under unlinked but is linked; remove it from unlinked")
        text = (base / "SKILL.md").read_text(encoding="utf-8")
        for heading, alts in sections:
            if not any(h in text for h in [heading, *alts]):
                msg = f"{where}/SKILL.md: missing section '{heading}' (or {', '.join(alts) or 'no alternative'})"
                if skp.library_of(name) == "core":
                    fail(msg)
                else:
                    print(f"note: {msg}", file=sys.stderr)


if __name__ == "__main__":
    if "--draft" in sys.argv:
        draft()
    else:
        sys.exit(__doc__)
