#!/usr/bin/env python3
"""Create a new OD skill folder in the registry's anatomy (standard library only).

    python3 scaffold_skill.py NAME --tier practice --lane all --owner-role ROLE --authority TEXT
                              [--library extension|core] [--out REPO_ROOT]

Writes <library folder>/NAME/SKILL.md with the frontmatter the registry validates and the sections it expects,
then prints the registry.yaml entry and the next commands. The body is a template: every TODO has to be replaced
before the skill is reviewed. Refuses to overwrite an existing folder.
"""
from __future__ import annotations

import argparse
import datetime
import re
import sys
from pathlib import Path

TIERS = ("foundation", "lane", "practice", "technical")
LIBRARIES = {"extension": "skills-extension", "core": "skills"}
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
DESCRIPTION = ("TODO: say what the skill does and when to use it, in the third person, with the words a user would use "
               "(for example: Run X when Y happens). End with a boundary: Not for Z, use the skill that owns Z instead.")

TEMPLATE = """---
name: {name}
description: >-
  {description}
license: MIT
metadata:
  id: {name}
  tier: {tier}
  lane: {lane}
  owner_role: {owner_role}
  authority_level: {authority}
  status: draft
  sources_read: {today}
  requires: [od-context]
  derived_from:
    - "TODO: each source you opened, with the date, for example: Department knowledge base, <path>, read {today}"
  okf:
    type: Agent Skill
    title: {title}
    tags: [{tier}]
    owner: human:jakob.gabriel
    generated: {{ by: claude-code/1, at: {today}T00:00:00Z }}
---

# {title}

Read `od-context` first.

## Purpose

⟨What the skill is for and when it is worth using, in one paragraph.⟩

## Inputs and output

- **In:** ⟨what the skill needs⟩
- **Out:** ⟨what it returns, and in which format⟩

## Procedure

1. ⟨First step. Control point: ...⟩
2. ⟨Second step. Control point: ...⟩

```text
⟨One worked example: a short input and the output it should give.⟩
```

## Human gate and AI-agent notes

- **Agent may:** ⟨draft, check, list what is missing⟩. **Humans decide:** ⟨the decisions that stay with a role⟩.
- **Evidence to cite:** ⟨what the agent must point at⟩.

## Pitfalls

- ⟨A failure the department has seen⟩

## Definition of done

⟨When the work is finished and who receives it.⟩

## References

| File | Open when |
|---|---|
| ⟨`references/topic.md`⟩ | ⟨the situation in which to open it⟩ |
"""


def title_of(name: str) -> str:
    words = name.split("-")
    if words[0] == "od":
        words = words[1:]
    return " ".join(words).capitalize()


def scaffold(root: Path, name: str, tier: str, lane: str, owner_role: str, authority: str, library: str = "extension") -> Path:
    if not NAME_RE.match(name) or len(name) > 64:
        raise ValueError("name must be lowercase letters, digits and single hyphens, at most 64 characters")
    if tier not in TIERS:
        raise ValueError(f"tier must be one of {', '.join(TIERS)}")
    if library not in LIBRARIES:
        raise ValueError("library must be extension or core")
    if any(ch in owner_role + authority for ch in "⟨⟩"):
        raise ValueError("owner role and authority must not contain placeholders")
    folder = root / LIBRARIES[library] / name
    if folder.exists():
        raise FileExistsError(f"{folder} already exists")
    folder.mkdir(parents=True)
    today = datetime.date.today().isoformat()
    (folder / "SKILL.md").write_text(TEMPLATE.format(
        name=name, tier=tier, lane=lane, owner_role=owner_role, authority=authority, today=today,
        description=DESCRIPTION, title=title_of(name)), encoding="utf-8", newline="\n")
    return folder


def registry_entry(name: str, tier: str, lane: str, owner_role: str, authority: str, library: str) -> str:
    return (f"  - id: {name}\n    library: {library}\n    tier: {tier}\n    lane: {lane}\n"
            f"    owner_role: {owner_role}\n    authority_level: {authority}\n    summary: <the description of SKILL.md, once written>\n")


def find_root(start: Path) -> Path:
    for p in [start, *start.parents]:
        if (p / "registry.yaml").exists():
            return p
    raise SystemExit("registry.yaml not found: run from the repository or pass --out")


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("name")
    ap.add_argument("--tier", required=True, choices=TIERS)
    ap.add_argument("--lane", default="all")
    ap.add_argument("--owner-role", required=True)
    ap.add_argument("--authority", required=True)
    ap.add_argument("--library", default="extension", choices=tuple(LIBRARIES))
    ap.add_argument("--out", type=Path, default=None)
    a = ap.parse_args(argv)
    root = a.out or find_root(Path.cwd())
    try:
        folder = scaffold(root, a.name, a.tier, a.lane, a.owner_role, a.authority, a.library)
    except (ValueError, FileExistsError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    print(f"created {folder}")
    print("\nAdd to registry.yaml (the summary is the SKILL.md description; authority_level must equal the SKILL.md):\n")
    print(registry_entry(a.name, a.tier, a.lane, a.owner_role, a.authority, a.library))
    print("Next: replace every TODO and placeholder; place the skill in docs/new-state/process.yaml (an extension skill as 'proposed' on a step or the spine); add the README row;")
    print("then python scripts/build_okf_index.py, python scripts/validate_registry.py, python scripts/agent_skills_spec.py --export dist, and the quality-check.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
