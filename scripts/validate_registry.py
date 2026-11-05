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
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import skillpaths  # noqa: E402

LIBRARIES = ("core", "extension")
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

    on_disk = set(skillpaths.all_ids())
    for entry in registry.get("skills", []):
        lib = entry.get("library")
        if lib not in LIBRARIES:
            fail(f"registry.yaml: '{entry['id']}' needs library: core or extension")
        elif entry["id"] in on_disk and skillpaths.library_of(entry["id"]) != lib:
            fail(f"registry.yaml: '{entry['id']}' is library {lib} but its folder is {skillpaths.folder_of(entry['id'])}/")

    for missing in sorted(listed - on_disk):
        fail(f"registry.yaml lists '{missing}' but no skills*/{missing}/ folder exists")
    for unlisted in sorted(on_disk - listed):
        fail(f"{skillpaths.folder_of(unlisted)}/{unlisted}/ exists but is not listed in registry.yaml")

    frontmatters: dict[str, dict] = {}

    for name in sorted(on_disk):
        skill_file = skillpaths.skill_dir(name) / "SKILL.md"
        if not skill_file.exists():
            fail(f"{skillpaths.folder_of(name)}/{name}/: no SKILL.md")
            continue

        fm = read_frontmatter(skill_file)
        if fm is None:
            continue
        frontmatters[name] = fm

        declared = fm.get("name")
        if declared != name:
            fail(f"{skillpaths.folder_of(name)}/{name}/SKILL.md: name '{declared}' does not match its directory")
        if declared and not NAME_RE.match(str(declared)):
            fail(f"{skillpaths.folder_of(name)}/{name}/SKILL.md: name must be lowercase, digits and hyphens")
        if declared and len(str(declared)) > MAX_NAME:
            fail(f"{skillpaths.folder_of(name)}/{name}/SKILL.md: name exceeds {MAX_NAME} characters")

        description = (fm.get("description") or "").strip()
        if not description:
            fail(f"{skillpaths.folder_of(name)}/{name}/SKILL.md: description is missing")
        elif len(description) < MIN_DESCRIPTION:
            fail(
                f"{skillpaths.folder_of(name)}/{name}/SKILL.md: description is {len(description)} chars — "
                f"too thin to trigger on reliably (min {MIN_DESCRIPTION})"
            )
        elif len(description) > MAX_DESCRIPTION:
            fail(f"{skillpaths.folder_of(name)}/{name}/SKILL.md: description exceeds {MAX_DESCRIPTION} characters")

        meta = fm.get("metadata") or {}
        if meta.get("id") != name:
            fail(f"{skillpaths.folder_of(name)}/{name}/SKILL.md: metadata.id '{meta.get('id')}' does not match its directory")
        for field in ("tier", "lane", "owner_role", "authority_level", "status", "derived_from"):
            if not meta.get(field):
                fail(f"{skillpaths.folder_of(name)}/{name}/SKILL.md: metadata.{field} is missing")
        if meta.get("tier") and meta["tier"] not in tiers:
            fail(f"{skillpaths.folder_of(name)}/{name}/SKILL.md: tier '{meta['tier']}' is not one of {sorted(tiers)}")

        scope = meta.get("scope", "od")
        if scope not in ("od", "portable"):
            fail(f"{skillpaths.folder_of(name)}/{name}/SKILL.md: metadata.scope '{scope}' is not 'od' or 'portable'")
        # OD-scoped skills inherit the department's vocabulary and honesty rules. A
        # portable skill is domain-generic and must instead say how it plugs in.
        if scope == "od" and name != "od-context":
            if "od-context" not in (meta.get("requires") or []):
                fail(f"{skillpaths.folder_of(name)}/{name}/SKILL.md: every od-scoped skill must require od-context")
        if scope == "portable":
            note = meta.get("od_integration")
            if not note:
                fail(f"{skillpaths.folder_of(name)}/{name}/SKILL.md: a portable skill must declare metadata.od_integration")
            elif not (ROOT / note).exists():
                fail(f"{skillpaths.folder_of(name)}/{name}/SKILL.md: metadata.od_integration path '{note}' does not exist")

    for name, fm in frontmatters.items():
        meta = fm.get("metadata") or {}
        for field in ("requires", "composes"):
            for ref in meta.get(field) or []:
                if ref not in on_disk:
                    fail(f"{skillpaths.folder_of(name)}/{name}/SKILL.md: metadata.{field} references unknown skill '{ref}'")

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
        # authority_level was cross-checked nowhere, and the registry had drifted into
        # paraphrase - in one case granting execute-autonomously where the skill capped at
        # recommend. The machine-readable index must not be able to widen a skill's authority.
        if str(entry.get("authority_level", "")).strip() != str(
                meta.get("authority_level", "")).strip():
            fail(
                f"registry.yaml: '{entry['id']}' authority_level disagrees with its SKILL.md\n"
                f"      registry: {entry.get('authority_level')}\n"
                f"      SKILL.md: {meta.get('authority_level')}"
            )
        for key, value in meta.items():
            if isinstance(value, str) and "\u27e8" in value:
                fail(
                    f"{entry['id']}/SKILL.md: metadata.{key} carries a placeholder "
                    f"({value!r}). A placeholder is fine in prose, where it marks an open "
                    "gap; in machine-readable metadata a consumer reads it as the value."
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
