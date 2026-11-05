#!/usr/bin/env python3
"""Check every skill against the open Agent Skills specification and export spec-strict copies.

The specification is https://agentskills.io/specification (reference validator: skills-ref, in
https://github.com/agentskills/agentskills). The rules used here, as read from those pages on 2026-11-05:

  name            1-64 characters, lowercase letters, digits and hyphens, no leading or trailing hyphen,
                  no "--", equal to the parent directory
  description     1-1024 characters
  license         optional string
  compatibility   optional, 1-500 characters
  metadata        optional, "a map from string keys to string values"
  allowed-tools   optional, a space-separated string (experimental)
  no other top-level key
  SKILL.md        recommended under 500 lines; file references relative to the skill root and one level deep

The registry keeps structured metadata (lists, and the nested `okf` block) because its own tooling reads it. The
specification asks for string values. This script therefore does two things:

  python scripts/agent_skills_spec.py                 report the source skills (metadata value types are a known deviation)
  python scripts/agent_skills_spec.py --export DIR    write spec-strict copies of all skills to DIR and validate them

Exit code 1 if an export is not spec-valid, or if a source skill has an error other than the known metadata deviation.
Standard library plus PyYAML.
"""
from __future__ import annotations

import json
import re
import shutil
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
import skillpaths as sp
SKILLS = ROOT / "skills"
ALLOWED = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
LINK = re.compile(r"\]\(([^)#\s]+)(?:#[^)]*)?\)")


def split(text: str):
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---", 4)
    if end == -1:
        return None, text
    return yaml.safe_load(text[4:end]) or {}, text[end + 4:].lstrip("\n")


def flatten(prefix: str, value, out: dict) -> None:
    """metadata value -> string-to-string entries; nested mappings become dotted keys, lists become 'a, b'."""
    if isinstance(value, dict):
        for k, v in value.items():
            flatten(f"{prefix}.{k}" if prefix else str(k), v, out)
    elif isinstance(value, (list, tuple)):
        out[prefix] = ", ".join(str(x).replace("\n", " ").strip() for x in value)
    elif value is None:
        out[prefix] = ""
    else:
        out[prefix] = " ".join(str(value).split())


def check(skill: Path):
    """-> (errors, warnings, deviations). deviations are the known metadata-type findings."""
    errs, warns, devs = [], [], []
    sm = skill / "SKILL.md"
    if not sm.exists():
        return ["no SKILL.md"], warns, devs
    try:
        fm, body = split(sm.read_text(encoding="utf-8"))
    except yaml.YAMLError as e:
        return [f"frontmatter does not parse: {str(e)[:120]}"], warns, devs
    if fm is None:
        return ["no frontmatter"], warns, devs
    extra = set(fm) - ALLOWED
    if extra:
        errs.append(f"unexpected top-level key(s): {sorted(extra)}")
    name = fm.get("name")
    if not isinstance(name, str) or not name:
        errs.append("name is missing")
    else:
        if not (1 <= len(name) <= 64) or not NAME_RE.match(name):
            errs.append("name must be 1-64 characters: lowercase letters, digits, single hyphens, none at the ends")
        if name != skill.name:
            errs.append("name must equal the directory name")
    desc = fm.get("description")
    if not isinstance(desc, str) or not desc.strip():
        errs.append("description is missing")
    elif len(desc.strip()) > 1024:
        errs.append(f"description is {len(desc.strip())} characters (max 1024)")
    if "license" in fm and not isinstance(fm["license"], str):
        errs.append("license must be a string")
    if "compatibility" in fm:
        c = fm["compatibility"]
        if not isinstance(c, str) or not (1 <= len(c) <= 500):
            errs.append("compatibility must be a string of 1-500 characters")
    if "allowed-tools" in fm and not isinstance(fm["allowed-tools"], str):
        errs.append("allowed-tools must be a space-separated string")
    meta = fm.get("metadata")
    if meta is not None:
        if not isinstance(meta, dict):
            errs.append("metadata must be a map")
        else:
            for k, v in meta.items():
                if not isinstance(k, str):
                    errs.append(f"metadata key {k!r} is not a string")
                if not isinstance(v, str):
                    devs.append(k)
    lines = len(body.splitlines())
    if lines > 500:
        warns.append(f"SKILL.md body has {lines} lines (recommended under 500)")
    # file references: relative, existing, and one level deep from SKILL.md
    for href in LINK.findall(body):
        if href.startswith(("http://", "https://", "mailto:")):
            continue
        if href.startswith("/"):
            errs.append(f"absolute link {href}")
        elif not (skill / href).exists():
            errs.append(f"SKILL.md links to {href}, which does not exist")
        elif href.startswith(".."):
            warns.append(f"SKILL.md links into another skill ({href}); rewritten to a text reference on export")
    for sub in ("references", "assets"):
        d = skill / sub
        if not d.is_dir():
            continue
        for f in sorted(d.glob("*.md")):
            if f.name == "index.md":
                continue
            for href in LINK.findall(f.read_text(encoding="utf-8")):
                if href.startswith(("http://", "https://", "mailto:", "../SKILL.md")):
                    continue
                if not (f.parent / href).exists():
                    errs.append(f"{sub}/{f.name} links to {href}, which does not exist")
                elif href.startswith(".."):
                    warns.append(f"{sub}/{f.name} links into another skill ({href}); rewritten to a text reference on export")
                else:
                    warns.append(f"{sub}/{f.name} links on to {href} (references should stay one level deep from SKILL.md)")
    return errs, warns, devs


MDLINK = re.compile(r"\[([^\]]*)\]\(([^)\s]+)\)")


def rewrite_cross_links(md: Path, skill_root: Path) -> None:
    """A link that leaves the skill folder cannot work once the skill is packaged alone: name the sibling skill instead."""
    text = md.read_text(encoding="utf-8")

    def sub(m):
        label, href = m.group(1), m.group(2)
        pure = href.split("#")[0]
        if not pure or href.startswith(("http://", "https://", "mailto:", "#")):
            return m.group(0)
        try:
            (md.parent / pure).resolve().relative_to(skill_root.resolve())
            return m.group(0)
        except ValueError:
            pass
        rest = [p for p in Path(pure).parts if p != ".."]
        if not rest:
            return label
        inner = "/".join(rest[1:])
        return f"{label} (skill `{rest[0]}`{', `' + inner + '`' if inner else ''})"

    new = MDLINK.sub(sub, text)
    if new != text:
        md.write_text(new, encoding="utf-8")


def export_skill(skill: Path, dest: Path) -> None:
    text = (skill / "SKILL.md").read_text(encoding="utf-8")
    fm, body = split(text)
    out = {}
    for k in ("name", "description", "license", "compatibility"):
        if k in fm:
            out[k] = fm[k].strip() if isinstance(fm[k], str) else fm[k]
    if "allowed-tools" in fm:
        out["allowed-tools"] = fm["allowed-tools"]
    meta = {}
    flatten("", fm.get("metadata") or {}, meta)
    out["metadata"] = {k: v for k, v in meta.items() if k}
    target = dest / skill.name
    if target.exists():
        shutil.rmtree(target)
    shutil.copytree(skill, target, ignore=shutil.ignore_patterns("index.md", "__pycache__", "*.pyc", "._DAV", "*.dir", "*.pag"))
    head = yaml.safe_dump(out, sort_keys=False, allow_unicode=True, width=100000, default_flow_style=False)
    (target / "SKILL.md").write_text(f"---\n{head}---\n\n{body}", encoding="utf-8")
    for md in target.rglob("*.md"):
        rewrite_cross_links(md, target)


def main(argv):
    names = sp.all_ids()
    rows, fail = [], False
    for n in names:
        e, w, d = check(sp.skill_dir(n))
        rows.append({"skill": n, "errors": e, "warnings": w, "metadata_non_string": d})
        if e:
            fail = True
    result = {"skills": len(names), "source": rows}
    print(f"source skills: {len(names)}")
    print(f"  spec errors (other than metadata types): {sum(1 for r in rows if r['errors'])} skills")
    print(f"  metadata with non-string values (known deviation): {sum(1 for r in rows if r['metadata_non_string'])} skills")
    print(f"  warnings: {sum(len(r['warnings']) for r in rows)} in {sum(1 for r in rows if r['warnings'])} skills")
    for r in rows:
        for m in r["errors"]:
            print(f"  ERROR {r['skill']}: {m}")
    if "--export" in argv:
        dest = Path(argv[argv.index("--export") + 1]).resolve()
        dest.mkdir(parents=True, exist_ok=True)
        ex = []
        for n in names:
            export_skill(sp.skill_dir(n), dest)
            e, w, d = check(dest / n)
            ex.append({"skill": n, "errors": e, "warnings": w, "metadata_non_string": d})
            if e or d:
                fail = True
                for m in e:
                    print(f"  EXPORT ERROR {n}: {m}")
                if d:
                    print(f"  EXPORT ERROR {n}: metadata still has non-string values: {d}")
        result["export"] = ex
        print(f"exported {len(names)} skills to {dest}: {sum(1 for r in ex if not r['errors'] and not r['metadata_non_string'])} spec-valid")
    if "--json" in argv:
        Path(argv[argv.index("--json") + 1]).write_text(json.dumps(result, ensure_ascii=False, indent=1), encoding="utf-8")
    return 1 if fail else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
