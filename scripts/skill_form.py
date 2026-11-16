#!/usr/bin/env python3
"""The form of every SKILL.md: structure only, no prose.

    python scripts/skill_form.py              # lint every skill; exit 1 on findings
    python scripts/skill_form.py <skill-id>   # one skill

A SKILL.md body may contain only: headings, tables, list items (bulleted or numbered, at most 40 words each, continuation
lines included), fenced code blocks (examples, commands) and HTML comments. Any other line is prose and belongs in
references/background.md, which is context and rationale and never an instruction. The skill must link outputs.yaml, its
output contract (see scripts/skill_outputs.py).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import skillpaths as skp  # noqa: E402

MAX_ITEM_WORDS = 40
LIST = re.compile(r"^\s*([-*]|\d+[.)])\s+\S")
MARKER = re.compile(r"^\s*([-*]|\d+[.)])\s+")


def nwords(line: str) -> int:
    """Words of a list item line without its bullet or number."""
    return len(MARKER.sub("", line).split())


def body_of(text: str) -> tuple[str, int]:
    """The body after the frontmatter and the number of lines the frontmatter took."""
    text = text.replace("\r\n", "\n")
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            head = text[:end + 5]
            return text[end + 5:], head.count("\n")
    return text, 0


def classify(body: str):
    """Yield (line number within body, kind, text) with kind in heading, table, item, continuation, code, comment, blank, prose."""
    fence = False
    prev = "blank"
    in_comment = False
    for n, line in enumerate(body.split("\n"), 1):
        s = line.strip()
        if s.startswith("```") or s.startswith("~~~"):
            fence = not fence
            yield n, "code", line
            prev = "code"
            continue
        if fence:
            yield n, "code", line
            continue
        if in_comment or s.startswith("<!--"):
            in_comment = "-->" not in s
            yield n, "comment", line
            continue
        if not s:
            yield n, "blank", line
            prev = "blank"
            continue
        if line.startswith("#"):
            kind = "heading"
        elif s.startswith("|"):
            kind = "table"
        elif LIST.match(line):
            kind = "item"
        elif line[:1] in (" ", "\t") and prev in ("item", "continuation"):
            kind = "continuation"
        else:
            kind = "prose"
        yield n, kind, line
        prev = kind


def lint(name: str) -> list[str]:
    d = skp.skill_dir(name)
    f = d / "SKILL.md"
    if not f.is_file():
        return [f"{name}: no SKILL.md"]
    body, offset = body_of(f.read_text(encoding="utf-8"))
    out: list[str] = []
    item_words = 0
    item_line = 0
    for n, kind, line in list(classify(body)) + [(0, "end", "")]:
        if kind in ("item", "continuation"):
            if kind == "item":
                if item_words > MAX_ITEM_WORDS:
                    out.append(f"{name}/SKILL.md:{item_line + offset}: list item of {item_words} words (at most {MAX_ITEM_WORDS})")
                item_words, item_line = nwords(line), n
            else:
                item_words += len(line.split())
            continue
        if item_words > MAX_ITEM_WORDS:
            out.append(f"{name}/SKILL.md:{item_line + offset}: list item of {item_words} words (at most {MAX_ITEM_WORDS})")
        item_words = 0
        if kind == "prose":
            out.append(f"{name}/SKILL.md:{n + offset}: prose ({line.strip()[:50]}...): move it to references/background.md")
    if "outputs.yaml" not in body:
        out.append(f"{name}/SKILL.md: does not link outputs.yaml (the output contract)")
    return out


def main(argv: list[str]) -> int:
    names = argv or skp.all_ids()
    findings: list[str] = []
    for n in names:
        findings += lint(n)
    for f in findings:
        print(f"  - {f}", file=sys.stderr)
    if findings:
        print(f"FAIL: {len(findings)} form finding(s) in {len({x.split('/')[0].split(':')[0] for x in findings})} skill(s)", file=sys.stderr)
        return 1
    print(f"OK: {len(names)} skills, SKILL.md is structure only")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
