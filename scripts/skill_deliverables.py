#!/usr/bin/env python3
"""The file set every skill ships, declared in config/skill-deliverables.yaml and checked by validate_registry.py.

    python3 scripts/skill_deliverables.py --draft     # rewrite the contract from the folders as they are now (review the diff)

The contract lists, per skill, every file the skill ships besides SKILL.md and the generated index.md files. The check
(`check()`, called by validate_registry.py) fails when:
  - a skill has no entry, or an entry names a skill that does not exist;
  - a declared file is missing or empty;
  - a shipped file is not declared (adding a file to a skill means declaring it);
  - a declared file cannot be reached by Markdown links from SKILL.md. A core skill must link every file it ships;
    an extension skill may list files under `unlinked` (scripts, examples, vendored files used by path). An `unlinked`
    file that is in fact linked is an error;
  - a skill has no references/outputs.md, or it does not follow the outputs format (see check_outputs);
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
              "# files); they are used by path. Core skills may not have any: every file must be linked from SKILL.md.\n")
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
    check_outputs(fail, lambda m: print(f"note: {m}", file=sys.stderr))
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
        core = skp.library_of(name) == "core"
        if core and loose:
            fail(f"{where}/: a core skill may not list files under 'unlinked' ({', '.join(sorted(loose))}); link them from SKILL.md")
        for rel in sorted(declared - ok - loose):
            hint = "link it from SKILL.md" if core else "link it, or list it under unlinked"
            fail(f"{where}/: '{rel}' is not linked from SKILL.md or from a file it links to ({hint})")
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


# ---- outputs: every skill states what it must deliver, to whom, and when that is complete -------------------------------
OUTPUTS = "references/outputs.md"
OUT_COLUMNS = ["Output", "Form", "Recipient", "Complete when"]
SKILL_PREFIXES = ("od-", "catalog-", "deploy-", "it-", "bc-", "funnel-", "ops-", "build-")
TICK = re.compile(r"`([^`]+)`")


def _section(text: str, heading: str) -> str | None:
    m = re.search(rf"^## {re.escape(heading)}\s*$(.*?)(?=^## |\Z)", text, re.M | re.S)
    return m.group(1) if m else None


def _skill_tokens(cell: str) -> list[str]:
    return [x for x in TICK.findall(cell) if x.startswith(SKILL_PREFIXES) and re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)+", x)]


def output_recipients(name: str) -> set[str]:
    """Skill ids named as recipient in a skill's outputs.md (empty when it is missing or malformed)."""
    f = skp.skill_dir(name) / OUTPUTS
    sec = _section(f.read_text(encoding="utf-8"), "Required outputs") if f.is_file() else None
    out: set[str] = set()
    for line in (sec or "").splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 4 and not set(line) <= set("|-: "):
            out |= set(_skill_tokens(cells[2]))
    return out


def _handoff_of(name: str) -> str:
    f = skp.skill_dir(name) / OUTPUTS
    return (_section(f.read_text(encoding="utf-8"), "Handoff") or "") if f.is_file() else ""


def check_outputs(fail, warn=None) -> None:
    ids = set(skp.all_ids())
    recipients: dict[str, set[str]] = {}
    for name in sorted(ids):
        where = f"{skp.folder_of(name)}/{name}"
        f = skp.skill_dir(name) / OUTPUTS
        if not f.is_file():
            fail(f"{where}/: no {OUTPUTS} (the outputs this skill must deliver, per scripts/skill_deliverables.py)")
            continue
        text = f.read_text(encoding="utf-8")
        sec, hand = _section(text, "Required outputs"), _section(text, "Handoff")
        if sec is None:
            fail(f"{where}/{OUTPUTS}: no '## Required outputs' section")
            continue
        if hand is None or not hand.strip():
            fail(f"{where}/{OUTPUTS}: no '## Handoff' section")
        rows = [ln for ln in sec.splitlines() if ln.strip().startswith("|")]
        if len(rows) < 3:
            fail(f"{where}/{OUTPUTS}: the Required outputs table needs a header and at least one output")
            continue
        header = [c.strip() for c in rows[0].strip().strip("|").split("|")]
        if header != OUT_COLUMNS:
            fail(f"{where}/{OUTPUTS}: table columns must be {' | '.join(OUT_COLUMNS)}")
            continue
        rec: set[str] = set()
        for row in rows[2:]:
            cells = [c.strip() for c in row.strip().strip("|").split("|")]
            if len(cells) != 4 or not all(cells):
                fail(f"{where}/{OUTPUTS}: every output needs all four cells: {row.strip()[:80]}")
                continue
            rec |= set(_skill_tokens(cells[2]))
        recipients[name] = rec
        for tok in sorted((rec | set(_skill_tokens(hand or ""))) - ids):
            fail(f"{where}/{OUTPUTS}: names '{tok}', which is not a skill")
    # a recipient must know where its input comes from: it names the sender somewhere in its own folder
    for sender, recs in sorted(recipients.items()):
        for r in sorted(recs & ids):
            if r == sender:
                continue
            body = "\n".join(p.read_text(encoding="utf-8") for p in skp.skill_dir(r).rglob("*.md")
                             if p.name != "index.md" and p.name != OUTPUTS) + _handoff_of(r)
            if sender not in body:
                fail(f"{skp.folder_of(r)}/{r}/: receives output from '{sender}' (its {OUTPUTS}) but never mentions it")
    # the process flow: between consecutive steps of a branch, some skill hands over to a skill of the next step
    proc = ROOT / "docs" / "new-state" / "process.yaml"
    if proc.exists():
        data = yaml.safe_load(proc.read_text(encoding="utf-8"))
        branches = [("intake", data["intake"]["steps"])]
        branches += [(f"{lane['id']}/{b['id']}", b["steps"]) for lane in data["lanes"] for b in lane["branches"]]
        for label, steps in branches:
            for a, b in zip(steps, steps[1:]):
                src, dst = set(a.get("skills") or []), set(b.get("skills") or [])
                if not src or not dst or src == dst:
                    continue
                if not any(recipients.get(s, set()) & dst for s in src):
                    (warn or fail)(f"process flow {label}: no skill of step {a['id']} ({', '.join(sorted(src))}) names a skill of "
                                   f"step {b['id']} ({', '.join(sorted(dst))}) as recipient of an output")
