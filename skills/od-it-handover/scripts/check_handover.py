#!/usr/bin/env python3
"""Check an OD handover package: OpenSpec validation rules (strict) plus the OD annex.

    python3 check_handover.py <path-to-openspec/changes/<change-id>> [--json]

Mirrors the rules of OpenSpec's own validator (github.com/Fission-AI/OpenSpec,
src/core/validation) so the package passes `openspec validate --strict` on IT's side:
Why 50-1000 chars, What Changes non-empty, at least one delta, delta headers, SHALL/MUST in
every requirement body, at least one '#### Scenario:' per requirement with WHEN/GIVEN and THEN,
requirement text <= 500 chars, Purpose >= 50 chars for a new capability, kebab-case capability
paths, <= 10 deltas, numbered checkbox tasks. Adds the OD annex: every '(blocking)' section of
handover.md filled (no open placeholder). Any open placeholder in the OpenSpec files is an error:
IT must not receive a template. Exit 1 on any error or (strict) warning. Standard library only.
"""
from __future__ import annotations
import json, pathlib, re, sys

MIN_WHY, MAX_WHY, MIN_PURPOSE, MAX_REQ, MAX_DELTAS = 50, 1000, 50, 500, 10
KEBAB = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
PLACEHOLDER = re.compile(r"⟨[^⟩]*⟩")
DELTA_HDR = re.compile(r"^## (ADDED|MODIFIED|REMOVED|RENAMED) Requirements\s*$", re.M)

errors: list[str] = []
warnings: list[str] = []


def section(text: str, title: str) -> str | None:
    m = re.search(rf"^## {re.escape(title)}\s*$(.*?)(?=^## |\Z)", text, re.M | re.S)
    return m.group(1).strip() if m else None


def check_proposal(p: pathlib.Path) -> None:
    if not p.exists():
        errors.append("proposal.md is missing"); return
    t = p.read_text(encoding="utf-8")
    why = section(t, "Why")
    if why is None:
        errors.append("proposal.md: no '## Why' section")
    elif len(why) < MIN_WHY:
        errors.append(f"proposal.md: Why is {len(why)} chars, needs at least {MIN_WHY}")
    elif len(why) > MAX_WHY:
        errors.append(f"proposal.md: Why is {len(why)} chars, at most {MAX_WHY}")
    what = section(t, "What Changes")
    if not what:
        errors.append("proposal.md: '## What Changes' is missing or empty")
    if section(t, "Capabilities") is None:
        errors.append("proposal.md: no '## Capabilities' section")


def check_spec(p: pathlib.Path, rel: str) -> int:
    t = p.read_text(encoding="utf-8")
    if not DELTA_HDR.search(t):
        errors.append(f"{rel}: no '## ADDED/MODIFIED/REMOVED/RENAMED Requirements' header")
        return 0
    purpose = section(t, "Purpose")
    if "## ADDED Requirements" in t and (purpose is None or len(purpose) < MIN_PURPOSE):
        warnings.append(f"{rel}: '## Purpose' missing or under {MIN_PURPOSE} chars (new capability)")
    reqs = re.split(r"^### Requirement:", t, flags=re.M)[1:]
    if not reqs:
        errors.append(f"{rel}: delta has no '### Requirement:' blocks")
    for block in reqs:
        name, _, body = block.partition("\n")
        name = name.strip() or "(unnamed)"
        head = re.split(r"^#### Scenario:", body, flags=re.M)
        text = re.split(r"^## ", head[0], flags=re.M)[0].strip()
        if not text:
            errors.append(f"{rel}: requirement '{name}' has no text")
        elif not re.search(r"\b(SHALL|MUST)\b", text):
            errors.append(f"{rel}: requirement '{name}' body must contain SHALL or MUST")
        if len(text) > MAX_REQ:
            warnings.append(f"{rel}: requirement '{name}' text is {len(text)} chars (> {MAX_REQ})")
        if re.search(r"^###\s+Scenario:", body, re.M):
            errors.append(f"{rel}: requirement '{name}' uses '### Scenario' - scenarios need exactly four '#'")
        scenarios = head[1:]
        if not scenarios:
            errors.append(f"{rel}: requirement '{name}' has no '#### Scenario:'")
        for sc in scenarios:
            sname, _, sbody = sc.partition("\n")
            sbody = re.split(r"^#{2,3} ", sbody, flags=re.M)[0]
            if not sbody.strip():
                errors.append(f"{rel}: scenario '{sname.strip()}' is empty")
            elif not (re.search(r"\*\*(WHEN|GIVEN)\*\*", sbody) and re.search(r"\*\*THEN\*\*", sbody)):
                warnings.append(f"{rel}: scenario '{sname.strip()}' needs a **WHEN** (or **GIVEN**) and a **THEN** step")
    return 1


def check_tasks(p: pathlib.Path) -> None:
    if not p.exists():
        errors.append("tasks.md is missing"); return
    items = re.findall(r"^- \[[ xX]\] (\S+)", p.read_text(encoding="utf-8"), re.M)
    if not items:
        errors.append("tasks.md: no checkbox tasks ('- [ ] 1.1 ...')")
    for n in items:
        if not re.match(r"^\d+\.\d+$", n):
            errors.append(f"tasks.md: task number '{n}' is not 'group.item'")


def check_annex(p: pathlib.Path) -> list[str]:
    if not p.exists():
        errors.append("handover.md (OD annex) is missing"); return []
    t = p.read_text(encoding="utf-8")
    opened = []
    for m in re.finditer(r"^## (\d+)\. (.+?)\s*$(.*?)(?=^## |\Z)", t, re.M | re.S):
        num, title, body = m.group(1), m.group(2), m.group(3)
        if "(blocking)" in title and PLACEHOLDER.search(body):
            errors.append(f"handover.md: blocking section {num} '{title.replace(' (blocking)', '')}' still has an open field")
        elif PLACEHOLDER.search(body):
            opened.append(f"{num} {title}")
    return opened


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) != 1:
        sys.exit(__doc__)
    change = pathlib.Path(args[0])
    if not change.is_dir():
        sys.exit(f"not a directory: {change}")
    if not KEBAB.match(change.name):
        errors.append(f"change id '{change.name}' is not kebab-case")
    meta = change / ".openspec.yaml"
    if not meta.exists():
        errors.append(".openspec.yaml is missing")
    else:
        m = meta.read_text(encoding="utf-8")
        if not re.search(r"^schema:\s*spec-driven\s*$", m, re.M):
            errors.append(".openspec.yaml: schema must be spec-driven")
        if re.search(r"^skip_specs:\s*true", m, re.M):
            errors.append(".openspec.yaml: skip_specs is not allowed for an OD handover (it must carry specs)")
    check_proposal(change / "proposal.md")
    deltas = 0
    for spec in sorted((change / "specs").rglob("spec.md")) if (change / "specs").is_dir() else []:
        rel = spec.relative_to(change).as_posix()
        for seg in spec.parent.relative_to(change / "specs").parts:
            if not KEBAB.match(seg):
                errors.append(f"{rel}: capability path segment '{seg}' is not kebab-case")
        deltas += check_spec(spec, rel)
    if deltas == 0:
        errors.append("change has no delta specs (specs/<capability>/spec.md)")
    if deltas > MAX_DELTAS:
        warnings.append(f"{deltas} deltas: consider splitting the change (> {MAX_DELTAS})")
    if not (change / "design.md").exists():
        errors.append("design.md is missing (route, hosting, interfaces, data model, Cyber Security, who runs it)")
    check_tasks(change / "tasks.md")
    for f in ["proposal.md", "design.md", "tasks.md", *[s.relative_to(change).as_posix() for s in change.rglob("spec.md")]]:
        fp = change / f
        if fp.exists() and PLACEHOLDER.search(fp.read_text(encoding="utf-8")):
            errors.append(f"{f}: still contains template placeholders - IT must not receive a template")
    open_annex = check_annex(change / "handover.md")
    ready = not errors and not warnings
    if "--json" in sys.argv:
        print(json.dumps({"change": change.name, "ready": ready, "errors": errors, "warnings": warnings,
                          "open_non_blocking": open_annex}, indent=2))
    else:
        for e in errors: print("ERROR  ", e)
        for w in warnings: print("WARN   ", w)
        for o in open_annex: print("OPEN   ", f"annex section {o} (non-blocking, list it under open items)")
        print("READY to hand over" if ready else "NOT READY - fix the errors and warnings above (strict mode)")
    return 0 if ready else 1


if __name__ == "__main__":
    raise SystemExit(main())
