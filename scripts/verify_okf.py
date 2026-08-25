#!/usr/bin/env python3
"""Verify this registry against the Open Knowledge Format contract.

    python3 scripts/verify_okf.py

OKF §11 asks a consumer for very little — parseable frontmatter and a non-empty `type` — and
tells consumers to tolerate broken links, unknown types and missing optional fields. It says
nothing about what a *producer* should let into its own bundle, and the answer here is: less.

The rules, and the failure each prevents, are in docs/okf-conventions.md.

Exit code: 1 if any problem, 0 otherwise.
"""

from __future__ import annotations

import pathlib
import re
import sys
import urllib.parse

try:
    import yaml
except ImportError:                                          # pragma: no cover
    print("PyYAML is required: pip install pyyaml", file=sys.stderr)
    raise SystemExit(1)

ROOT = pathlib.Path(__file__).resolve().parent.parent
KG = ROOT.parent / "ops-knowledge-graph"

RESERVED = {"index.md", "log.md"}
STATUSES = {"draft", "stable", "deprecated"}
TYPES = {"Agent Skill", "Skill Reference", "Skill Asset", "Skill Guide",
         "Map of Content", "Design Record"}
# The six fields the Agent Skills spec allows at the top level of a SKILL.md. Anything else
# makes packaging and upload to claude.ai or the Skills API fail with a hard error, which is
# why a skill's OKF fields live under `metadata.okf` instead.
SPEC_KEYS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
ACTOR = re.compile(r"^(human:[\w.\-]+|process:[\w.\-]+|[\w\-]+/[\w.\-]+)$")
ISO = re.compile(r"^\d{4}-\d{2}-\d{2}(T[\d:]+Z)?$")
LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
WIKILINK = re.compile(r"(?<!\!)\[\[[^\]]+\]\]")

problems: list[tuple[str, str]] = []


def bad(path: pathlib.Path, message: str) -> None:
    problems.append((str(path.relative_to(ROOT)), message))


def slug(s: str) -> str:
    s = s.lower().replace("&", "and")
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", s)).strip("-")


def frontmatter(path: pathlib.Path) -> dict | None:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        bad(path, "frontmatter is not terminated")
        return None
    try:
        fm = yaml.safe_load(text[4:end])
    except yaml.YAMLError as exc:
        bad(path, f"frontmatter does not parse — {exc}")
        return None
    return fm if isinstance(fm, dict) else None


def check_stamp(path: pathlib.Path, where: str, stamp) -> None:
    if not isinstance(stamp, dict) or "by" not in stamp or "at" not in stamp:
        bad(path, f"`{where}` is not an OKF stamp — it needs `by` and `at`")
        return
    if not ACTOR.match(str(stamp["by"])):
        bad(path, f"`{where}.by` \"{stamp['by']}\" is not an OKF actor "
                  "(human:<id>, process:<id> or <producer>/<version>)")
    import datetime
    at = stamp["at"]
    if not (isinstance(at, (datetime.date, datetime.datetime)) or ISO.match(str(at))):
        bad(path, f"`{where}.at` \"{at}\" is not an ISO 8601 timestamp")


def check_resource(path: pathlib.Path, where: str, value: str) -> None:
    """In-repo paths must exist. Knowledge-graph paths are checked when the bundle is
    beside this repo, and reported as unchecked when it is not — never silently passed."""
    if value.startswith(("http://", "https://")):
        return
    if value.startswith("ops-knowledge-graph/"):
        if not KG.exists():
            return
        rest = re.sub(r"\s*\(.*\)\s*$", "", value.split("/", 1)[1]).strip()
        if not resolves_in_kg(rest):
            bad(path, f"`{where}` points at {value}, which is not in the bundle")
        return
    target = (path.parent / urllib.parse.unquote(value)).resolve()
    if not target.exists():
        bad(path, f"`{where}` points at {value}, which does not exist")


def resolves_in_kg(rest: str) -> bool:
    """Resolve a knowledge-graph path, including the abbreviated forms the skills use:
    `.../` for an elided middle, `{a,b}` for alternatives, and `*`/`**` globs."""
    if (KG / rest).exists():
        return True
    for opt in expand_braces(rest):
        pattern = opt.replace(".../", "**/")
        if pattern.startswith("**/"):
            pattern = "**/" + pattern[3:]
        try:
            if next(KG.glob(pattern), None) is not None:
                return True
        except (ValueError, IndexError):
            continue
    return False


def expand_braces(s: str) -> list[str]:
    m = re.search(r"\{([^{}]*)\}", s)
    if not m:
        return [s]
    out = []
    for alt in m.group(1).split(","):
        out += expand_braces(s[: m.start()] + alt.strip() + s[m.end():])
    return out


def path_shaped(value: str) -> bool:
    """A derived_from entry may be a sentence rather than a path; only paths are checkable."""
    head = value.split()[0] if value.split() else ""
    return "/" in head and " " not in head.split("(")[0]


def check_links(path: pathlib.Path, text: str) -> None:
    if WIKILINK.search(text):
        bad(path, "contains a wikilink; OKF cross-references are Markdown links")
    for href in LINK.findall(text):
        href = href.split("#")[0].strip()
        if not href or href.startswith(("http://", "https://", "mailto:", "⟨")):
            continue
        if href.startswith("/"):
            bad(path, f"link `{href}` is bundle-relative; a leading / means the repository "
                      "root on GitHub, so use a relative link")
            continue
        if not (path.parent / urllib.parse.unquote(href)).exists():
            bad(path, f"link `{href}` resolves to nothing")


def main() -> int:
    if not (ROOT / "index.md").exists():
        problems.append(("index.md", "the bundle root has no index.md (OKF §8)"))
    root_fm = frontmatter(ROOT / "index.md") or {}
    if set(root_fm) - {"okf_version"}:
        bad(ROOT / "index.md", "the root index may carry only `okf_version` (OKF §8)")

    concepts = 0
    for path in sorted(ROOT.rglob("*.md")):
        if any(p.startswith((".", "__")) for p in path.relative_to(ROOT).parts):
            continue
        text = path.read_text(encoding="utf-8")

        if path.name in RESERVED:
            if path.name == "index.md" and path != ROOT / "index.md" and text.startswith("---\n"):
                bad(path, "an index.md carries no frontmatter (OKF §8); only the bundle root may")
            check_links(path, text)
            continue

        fm = frontmatter(path)
        if fm is None:
            bad(path, "no parseable YAML frontmatter — OKF §11.2 requires it of every concept")
            continue
        concepts += 1

        if path.name == "SKILL.md":
            extra = set(fm) - SPEC_KEYS
            if extra:
                bad(path, f"top-level key(s) {sorted(extra)} are not in the Agent Skills spec; "
                          "packaging and upload fail with a hard error. Put producer fields "
                          "under `metadata`")
            okf = (fm.get("metadata") or {}).get("okf")
            if not isinstance(okf, dict):
                bad(path, "no `metadata.okf` — a skill carries its OKF fields there, because "
                          "the spec forbids extra top-level keys")
                continue
            if not fm.get("description"):
                bad(path, "no `description`")
            # A skill's findable identity is `name`, which the loader ties to the directory —
            # a stronger check than the filename rule that applies to every other concept,
            # because SKILL.md is the same filename 24 times over. `title` is the display
            # name and is free to read like one.
            expect = path.parent.name
            if fm.get("name") != expect:
                bad(path, f"`name` \"{fm.get('name')}\" is not the skill directory `{expect}`; "
                          "the command name comes from the directory")
            if not str(okf.get("title", "")).strip():
                bad(path, "no `metadata.okf.title`")
            body_fm, name_key = okf, "metadata.okf"
        else:
            body_fm, name_key = fm, "frontmatter"
            title = str(fm.get("title", ""))
            if not title:
                bad(path, "no `title`")
            elif slug(title) != slug(path.stem) and path.stem.lower() != "readme":
                bad(path, f"`title` \"{title}\" does not slug to the filename `{path.stem}`")
            if not fm.get("description"):
                bad(path, "no `description` — a concept in the graph with nothing under its name")
            for key in ("resource",):
                if fm.get(key):
                    check_resource(path, key, str(fm[key]))

        typ = str(body_fm.get("type", "")).strip()
        if not typ:
            bad(path, f"`{name_key}.type` is empty — OKF §11.2's one requirement")
        elif typ not in TYPES:
            bad(path, f"type \"{typ}\" is not one this bundle declares "
                      f"({', '.join(sorted(TYPES))})")

        status = str((fm.get("metadata") or {}).get("status", fm.get("status", ""))).strip()
        if status and status not in STATUSES:
            bad(path, f"status \"{status}\" is not one of {' | '.join(sorted(STATUSES))}")

        if "generated" in body_fm:
            check_stamp(path, f"{name_key}.generated", body_fm["generated"])
        else:
            bad(path, f"no `{name_key}.generated` — OKF §4 records who produced a concept and when")
        for i, v in enumerate(body_fm.get("verified", []) or []):
            check_stamp(path, f"{name_key}.verified[{i}]", v)

        for i, s in enumerate((fm.get("metadata") or {}).get("derived_from", []) or []):
            if path_shaped(str(s)):
                check_resource(path, f"metadata.derived_from[{i}]", str(s))

        check_links(path, text)

    if problems:
        print(f"{len(problems)} problem(s):\n", file=sys.stderr)
        for p, m in problems:
            print(f"  {p} — {m}", file=sys.stderr)
        return 1
    note = "" if KG.exists() else "  (knowledge-graph paths unchecked: bundle not beside this repo)"
    print(f"OKF OK — {concepts} concept(s) conform.{note}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
