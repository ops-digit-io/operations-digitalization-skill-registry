#!/usr/bin/env python3
"""Read-only freshness report for the OD skill registry and its knowledge bundle.

Three checks, each optional, all read-only (no file is opened for writing):

  --skills DIR    every DIR/<skill>/SKILL.md: sources_read age, status, and the number of
                  unresolved gap markers (the angle-bracket placeholders) in SKILL.md and
                  references/*.md. Templates under assets/ are NOT counted: they are
                  placeholders by design.
  --bundle DIR    every .md under DIR with front matter keys valid-until, last-verified
                  and review-cadence: expired, expiring soon, overdue by cadence.
  --registry FILE registry.yaml: data_as_of / graph_as_of / flows_as_of ages and the number
                  of open_gaps entries.
  --cross ROOT    (with --skills) for each skill, the bundle files named in derived_from as a
                  full path starting ops-knowledge-graph/ (resolved under ROOT, the folder
                  that holds ops-knowledge-graph): is the source itself expired or overdue?
                  A skill read its source recently, but the source may not have been
                  re-verified for months. Paths with braces or ellipses cannot be resolved
                  and are counted, not guessed.

Standard library only. The front matter is read line by line, not with a YAML parser, so
it understands only plain "key: value" lines (that is all these files use).

Examples:
  python context_freshness.py --skills ../../ --registry ../../../registry.yaml
  python context_freshness.py --bundle <bundle>/OperationsDigitalization-Department --today <YYYY-MM-DD>

Exit status is 0 unless --fail-on-findings is given and something was found.
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path

GAP_RE = re.compile("⟨[^⟩\n]*⟩")  # angle-bracket placeholder
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}")
CADENCE_DAYS = {"weekly": 7, "monthly": 31, "quarterly": 92, "yearly": 366}


def split_front_matter(text: str):
    """Return (front_matter_lines, body) or (None, text) when there is no block."""
    text = text.lstrip("﻿")
    if not text.startswith("---"):
        return None, text
    lines = text.splitlines()
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return lines[1:i], "\n".join(lines[i + 1:])
    return None, text


def fm_value(fm_lines, key):
    """First 'key: value' (any indentation) in the front matter, or None."""
    pat = re.compile(r"^\s*" + re.escape(key) + r"\s*:\s*(.*?)\s*$")
    for line in fm_lines or []:
        m = pat.match(line)
        if m:
            return m.group(1).strip().strip("'\"")
    return None


def parse_date(value):
    """A YYYY-MM-DD date at the start of value, else None (placeholders, blanks, text)."""
    if not value or not DATE_RE.match(value):
        return None
    try:
        return dt.date.fromisoformat(value[:10])
    except ValueError:
        return None


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def md_table(headers, rows):
    out = ["| " + " | ".join(headers) + " |", "|" + "|".join("---" for _ in headers) + "|"]
    for r in rows:
        out.append("| " + " | ".join(str(c) for c in r) + " |")
    return "\n".join(out)


def check_skills(root: Path, today: dt.date, threshold: int):
    rows, problems = [], []
    for skill_md in sorted(root.glob("*/SKILL.md")):
        name = skill_md.parent.name
        fm, body = split_front_matter(read(skill_md))
        if fm is None:
            problems.append((name, "no front matter"))
            continue
        sr = parse_date(fm_value(fm, "sources_read"))
        status = fm_value(fm, "status") or "?"
        gaps = len(GAP_RE.findall(body))
        for ref in sorted((skill_md.parent / "references").glob("*.md")):
            if ref.name == "index.md":
                continue
            _, rbody = split_front_matter(read(ref))
            gaps += len(GAP_RE.findall(rbody))
        if sr is None:
            problems.append((name, "sources_read missing or not a date"))
            continue
        rows.append((name, sr, (today - sr).days, status, gaps))
    return rows, problems


DERIVED_PATH_RE = re.compile(r"ops-knowledge-graph/[^\s'\"`,;()]+?\.md")


def source_state(md: Path, today: dt.date):
    """'expired' / 'overdue' / 'ok' / 'undated' for one bundle file."""
    fm, _ = split_front_matter(read(md))
    if fm is None:
        return "undated", ""
    vu = parse_date(fm_value(fm, "valid-until"))
    lv = parse_date(fm_value(fm, "last-verified"))
    cadence = (fm_value(fm, "review-cadence") or "").lower()
    if vu is not None and vu < today:
        return "expired", f"valid-until {vu}"
    if lv is not None and cadence in CADENCE_DAYS and lv + dt.timedelta(days=CADENCE_DAYS[cadence]) < today:
        return "overdue", f"{cadence}, last-verified {lv}"
    if vu is None and lv is None:
        return "undated", ""
    return "ok", ""


def check_cross(skills_root: Path, repo_root: Path, today: dt.date):
    rows, unresolved = [], 0
    for skill_md in sorted(skills_root.glob("*/SKILL.md")):
        fm, _ = split_front_matter(read(skill_md))
        if fm is None:
            continue
        seen = set()
        for line in fm:
            for m in DERIVED_PATH_RE.findall(line):
                if m in seen:
                    continue
                seen.add(m)
                if "{" in m or "..." in m:
                    unresolved += 1
                    continue
                target = repo_root / m
                if not target.is_file():
                    unresolved += 1
                    continue
                state, detail = source_state(target, today)
                if state in ("expired", "overdue"):
                    rows.append((skill_md.parent.name, m.split("_knowledge/", 1)[-1], state, detail))
    return rows, unresolved


def check_bundle(root: Path, today: dt.date, soon: int):
    findings, scanned, with_dates = [], 0, 0
    for md in sorted(root.rglob("*.md")):
        fm, _ = split_front_matter(read(md))
        if fm is None:
            continue
        scanned += 1
        valid_until = parse_date(fm_value(fm, "valid-until"))
        last_verified = parse_date(fm_value(fm, "last-verified"))
        cadence = (fm_value(fm, "review-cadence") or "").lower()
        if valid_until is None and last_verified is None and not cadence:
            continue
        with_dates += 1
        rel = md.relative_to(root).as_posix()
        if valid_until is not None:
            left = (valid_until - today).days
            if left < 0:
                findings.append((rel, "EXPIRED", f"valid-until {valid_until} passed {-left} days ago"))
            elif left <= soon:
                findings.append((rel, "EXPIRES SOON", f"valid-until {valid_until} in {left} days"))
        if last_verified is not None and cadence in CADENCE_DAYS:
            due = last_verified + dt.timedelta(days=CADENCE_DAYS[cadence])
            if due < today:
                findings.append((rel, "REVIEW OVERDUE",
                                 f"{cadence}; last-verified {last_verified}, due {due}, {(today - due).days} days late"))
        elif last_verified is None and cadence in CADENCE_DAYS:
            findings.append((rel, "NO last-verified", f"review-cadence {cadence} but no usable last-verified date"))
        elif cadence and cadence not in CADENCE_DAYS:
            findings.append((rel, "UNKNOWN CADENCE", f"review-cadence '{cadence}'"))
    return findings, scanned, with_dates


def check_registry(path: Path, today: dt.date):
    text = read(path)
    marks = []
    for key in ("data_as_of", "graph_as_of", "flows_as_of"):
        m = re.search(r"^\s*" + key + r"\s*:\s*(\d{4}-\d{2}-\d{2})", text, re.M)
        d = parse_date(m.group(1)) if m else None
        marks.append((key, d, (today - d).days if d else None))
    gaps = 0
    in_gaps = False
    for line in text.splitlines():
        if re.match(r"^open_gaps\s*:", line):
            in_gaps = True
            continue
        if in_gaps:
            if re.match(r"^\s+-\s+\S", line):
                gaps += 1
            elif line.strip() and not line.startswith((" ", "\t", "#")):
                break
    return marks, gaps


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--skills", type=Path, help="the skills/ directory")
    ap.add_argument("--bundle", type=Path, help="root of the knowledge bundle to scan")
    ap.add_argument("--registry", type=Path, help="path to registry.yaml")
    ap.add_argument("--cross", type=Path,
                    help="folder that holds ops-knowledge-graph; with --skills, checks the sources each skill names")
    ap.add_argument("--today", help="override today's date, YYYY-MM-DD (for repeatable reports)")
    ap.add_argument("--threshold", type=int, default=90,
                    help="days after which sources_read counts as stale (default 90)")
    ap.add_argument("--soon", type=int, default=30,
                    help="days ahead in which a valid-until counts as expiring (default 30)")
    ap.add_argument("--fail-on-findings", action="store_true", help="exit 1 if anything is reported")
    args = ap.parse_args(argv)

    if not (args.skills or args.bundle or args.registry):
        ap.error("give at least one of --skills, --bundle, --registry")
    today = parse_date(args.today) if args.today else dt.date.today()
    if today is None:
        ap.error("--today must be YYYY-MM-DD")
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    found = 0
    print(f"# Context freshness report - {today}\n")
    print(f"Read-only. Thresholds: sources_read stale after {args.threshold} days; valid-until flagged "
          f"{args.soon} days ahead.\n")

    if args.skills:
        rows, problems = check_skills(args.skills, today, args.threshold)
        stale = [r for r in rows if r[2] > args.threshold]
        priority = [r for r in stale if r[4] > 0]
        print(f"## Skills ({len(rows)} read)\n")
        print(f"Stale (sources_read older than {args.threshold} days): {len(stale)}. "
              f"Stale and carrying gap markers: {len(priority)}.\n")
        if stale:
            print(md_table(["skill", "sources_read", "age (days)", "status", "gap markers"],
                           [(n, s, a, st, g) for n, s, a, st, g in sorted(stale, key=lambda r: -r[2])]))
            print()
        else:
            print("No skill is stale.\n")
        oldest = min(rows, key=lambda r: r[1]) if rows else None
        if oldest:
            print(f"Oldest sources_read: {oldest[0]} ({oldest[1]}, {oldest[2]} days).\n")
        if problems:
            print("Could not assess:\n")
            print(md_table(["skill", "problem"], problems))
            print()
        found += len(priority) + len(problems)
        if args.cross:
            cross, unresolved = check_cross(args.skills, args.cross, today)
            print("### Sources the skills name that are themselves out of date")
            print()
            if cross:
                print(md_table(["skill", "source file", "state", "detail"], cross))
                print()
            else:
                print("None of the resolvable sources is expired or overdue.")
                print()
            print(f"Source paths that could not be resolved (braces, ellipsis or missing file): {unresolved}.")
            print()
            found += len(cross)

    if args.bundle:
        findings, scanned, with_dates = check_bundle(args.bundle, today, args.soon)
        print(f"## Knowledge bundle ({scanned} files with front matter, {with_dates} carry a freshness field)\n")
        if findings:
            print(md_table(["file", "finding", "detail"], findings))
            print()
        else:
            print("No expired, expiring or overdue file.\n")
        found += len(findings)

    if args.registry:
        marks, gaps = check_registry(args.registry, today)
        print("## Registry data marks\n")
        print(md_table(["mark", "date", "age (days)"],
                       [(k, d if d else "not found", a if a is not None else "-") for k, d, a in marks]))
        print(f"\nopen_gaps entries: {gaps}\n")
        found += sum(1 for _, d, a in marks if d is None or a > args.threshold)

    return 1 if (args.fail_on_findings and found) else 0


if __name__ == "__main__":
    raise SystemExit(main())
