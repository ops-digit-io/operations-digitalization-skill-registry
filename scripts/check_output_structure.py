#!/usr/bin/env python3
"""Check that a filled output keeps the structure of its template (stdlib only).

    python scripts/check_output_structure.py <output.md> <template.md>

Findings (exit 1): the output is empty; a heading of the template is missing from the output; a placeholder
(an angle-bracket mark like the ones a template uses) is still unfilled. The three markers that mean "known gap with a named
supplier" are allowed: not recorded, to confirm, to collect, not evidenced. The check says nothing about whether the content is
true: that is a human sign-off.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

OPEN, CLOSE = "⟨", "⟩"
ALLOWED = {"not recorded", "to confirm", "to collect", "not evidenced", "to be collected", "to confirm or create"}
HEADING = re.compile(r"^(#{2,6})\s+(.*?)\s*$", re.M)


def norm_heading(text: str) -> str:
    text = re.sub(re.escape(OPEN) + r"[^" + re.escape(CLOSE) + r"]*" + re.escape(CLOSE), "", text)
    return re.sub(r"[\s*_`:.\-·]+", " ", text).strip().lower()


def body(text: str) -> str:
    text = text.replace("\r\n", "\n")
    return text.split("\n---\n", 1)[1] if text.startswith("---\n") and "\n---\n" in text else text


def findings(output: str, template: str) -> list[str]:
    out_body, tpl_body = body(output), body(template)
    if not out_body.strip():
        return ["the output is empty"]
    have = {norm_heading(m.group(2)) for m in HEADING.finditer(out_body)}
    out: list[str] = []
    for m in HEADING.finditer(tpl_body):
        h = norm_heading(m.group(2))
        if h and h not in have:
            out.append(f"missing section: {m.group(2).strip()[:70]}")
    marks = re.findall(re.escape(OPEN) + r"([^" + re.escape(CLOSE) + r"]*)" + re.escape(CLOSE), out_body)
    open_marks = [x.strip() for x in marks if x.strip().lower() not in ALLOWED]
    if open_marks:
        out.append(f"{len(open_marks)} placeholder(s) still unfilled, first: {OPEN}{open_marks[0][:50]}{CLOSE}")
    return out


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(__doc__)
        return 2
    res = findings(Path(argv[0]).read_text(encoding="utf-8-sig"), Path(argv[1]).read_text(encoding="utf-8-sig"))
    if res:
        print("NOT READY")
        for r in res:
            print(f"- {r}")
        return 1
    print("READY")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
