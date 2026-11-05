#!/usr/bin/env python3
"""List lines in skills/ that look like current company figures (stdlib, read-only).

Heuristic, not a verdict: it flags counts of estate entities, money amounts, dated
export/snapshot statements and large numbers. Technical constants (ports, versions,
QoS, scoring scales) are not flagged on their own. Exit 1 if any line is flagged.

Usage: check_no_figures.py [skill-name ...]   (default: all skills)
"""
import io
import re
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
import skillpaths as sp
ENT = (r"machines?|plants?|sites?|flows?|instances?|use cases?|dashboards?|apps?|applications?|"
       r"signals?|tags?|decks?|notes?|rows?|records?|templates?|panels?|tools?|connectors?|"
       r"controllers?|lines?|users?|projects?|epics?|items?|entries|files?|workshops?|reviews?")
RULES = [
    ("money", re.compile(r"(€\s?\d|\d\s?(?:€|EUR|k€|T€|TEUR|k\s?EUR)\b|\b\d+\s?k\b)", re.I)),
    ("count", re.compile(rf"(?<![\w.-])\d[\d,.]*\s+(?:\w+\s+){{0,2}}(?:{ENT})\b", re.I)),
    ("count-of", re.compile(rf"\b(?:{ENT})\s*[:=(]\s*\d{{2,}}", re.I)),
    ("snapshot", re.compile(r"(export of|re-?counted|snapshot|as of 20\d\d|read on 20\d\d|census|sample of \d)", re.I)),
    ("big-number", re.compile(r"\b\d{1,3}(?:,\d{3})+\b|\b\d{4,}\b(?!-)")),
    ("percent", re.compile(r"\b\d+(?:\.\d+)?\s?%")),
]
SKIP = re.compile(r"^(name|version|generated|sources_read|created|updated|last_reviewed|review_by|expires):")

def lines(skill):
    for p in sorted(sp.skill_dir(skill).rglob("*")):
        if not p.is_file() or p.name == "index.md" or p.suffix not in (".md", ".py", ".yaml", ".yml", ".txt"):
            continue
        for n, l in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            if SKIP.match(l.strip()) or re.match(r"^\s*(-|\*)?\s*(derived_from|sources)", l):
                continue
            if re.search(r"\b20\d\d-\d\d-\d\d\b", l) and not RULES[3][1].search(l):
                pass
            hit = [k for k, r in RULES if r.search(l)]
            if hit:
                yield p.relative_to(sp.skill_dir(skill).parent), n, hit, l.strip()

def main():
    names = sys.argv[1:] or sp.all_ids()
    total = 0
    for s in names:
        for f, n, hit, l in lines(s):
            total += 1
            print(f"{f}:{n} [{','.join(hit)}] {l[:140]}")
    print(f"-- {total} flagged line(s)", file=sys.stderr)
    return 1 if total else 0

if __name__ == "__main__":
    sys.exit(main())
