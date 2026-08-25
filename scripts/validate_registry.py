#!/usr/bin/env python3
"""Guard for the OD skill registry.

Checks the things that silently rot: a skill folder with no registry entry, a
registry entry with no folder, frontmatter that will not parse, a name that does
not match its directory, a description too thin to trigger on, and a `requires` or
`composes` reference to a skill that does not exist.

    python3 scripts/validate_registry.py

Exits non-zero on the first category of failure found, listing every instance.
"""

from __future__ import annotations

import pathlib
import re
import sys

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("PyYAML is required: pip install pyyaml")

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
REGISTRY = ROOT / "registry.yaml"

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
MIN_DESCRIPTION = 120
MAX_DESCRIPTION = 1024
MAX_NAME = 64

errors: list[str] = []


def fail(msg: str) -> None:
    errors.append(msg)


def read_frontmatter(path: pathlib.Path) -> dict | None:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail(f"{path.relative_to(ROOT)}: no YAML frontmatter")
        return None
    end = text.find("\n---\n", 3)
    if end == -1:
        fail(f"{path.relative_to(ROOT)}: frontmatter is not terminated")
        return None
    try:
        data = yaml.safe_load(text[4:end])
    except yaml.YAMLError as exc:
        fail(f"{path.relative_to(ROOT)}: frontmatter does not parse — {exc}")
        return None
    if not isinstance(data, dict):
        fail(f"{path.relative_to(ROOT)}: frontmatter is not a mapping")
        return None
    return data


def main() -> int:
    if not REGISTRY.exists():
        sys.exit("registry.yaml is missing")

    registry = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))
    listed = {entry["id"] for entry in registry.get("skills", [])}
    tiers = set(registry.get("tiers", {}))

    on_disk = {p.name for p in sorted(SKILLS_DIR.iterdir()) if p.is_dir()}

    for missing in sorted(listed - on_disk):
        fail(f"registry.yaml lists '{missing}' but skills/{missing}/ does not exist")
    for unlisted in sorted(on_disk - listed):
        fail(f"skills/{unlisted}/ exists but is not listed in registry.yaml")

    frontmatters: dict[str, dict] = {}

    for name in sorted(on_disk):
        skill_file = SKILLS_DIR / name / "SKILL.md"
        if not skill_file.exists():
            fail(f"skills/{name}/: no SKILL.md")
            continue

        fm = read_frontmatter(skill_file)
        if fm is None:
            continue
        frontmatters[name] = fm

        declared = fm.get("name")
        if declared != name:
            fail(f"skills/{name}/SKILL.md: name '{declared}' does not match its directory")
        if declared and not NAME_RE.match(str(declared)):
            fail(f"skills/{name}/SKILL.md: name must be lowercase, digits and hyphens")
        if declared and len(str(declared)) > MAX_NAME:
            fail(f"skills/{name}/SKILL.md: name exceeds {MAX_NAME} characters")

        description = (fm.get("description") or "").strip()
        if not description:
            fail(f"skills/{name}/SKILL.md: description is missing")
        elif len(description) < MIN_DESCRIPTION:
            fail(
                f"skills/{name}/SKILL.md: description is {len(description)} chars — "
                f"too thin to trigger on reliably (min {MIN_DESCRIPTION})"
            )
        elif len(description) > MAX_DESCRIPTION:
            fail(f"skills/{name}/SKILL.md: description exceeds {MAX_DESCRIPTION} characters")

        meta = fm.get("metadata") or {}
        if meta.get("id") != name:
            fail(f"skills/{name}/SKILL.md: metadata.id '{meta.get('id')}' does not match its directory")
        for field in ("tier", "lane", "owner_role", "authority_level", "status", "derived_from"):
            if not meta.get(field):
                fail(f"skills/{name}/SKILL.md: metadata.{field} is missing")
        if meta.get("tier") and meta["tier"] not in tiers:
            fail(f"skills/{name}/SKILL.md: tier '{meta['tier']}' is not one of {sorted(tiers)}")
        if name != "od-context" and "od-context" not in (meta.get("requires") or []):
            fail(f"skills/{name}/SKILL.md: every skill must require od-context")

    for name, fm in frontmatters.items():
        meta = fm.get("metadata") or {}
        for field in ("requires", "composes"):
            for ref in meta.get(field) or []:
                if ref not in on_disk:
                    fail(f"skills/{name}/SKILL.md: metadata.{field} references unknown skill '{ref}'")

    for entry in registry.get("skills", []):
        fm = frontmatters.get(entry["id"])
        if not fm:
            continue
        meta = fm.get("metadata") or {}
        if entry.get("tier") != meta.get("tier"):
            fail(
                f"registry.yaml: '{entry['id']}' tier '{entry.get('tier')}' disagrees with "
                f"its SKILL.md tier '{meta.get('tier')}'"
            )

    if errors:
        print(f"FAIL — {len(errors)} problem(s):\n", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return 1

    print(f"OK — {len(on_disk)} skills, registry and frontmatter agree.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
