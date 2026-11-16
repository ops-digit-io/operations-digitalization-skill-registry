#!/usr/bin/env python3
"""Measurable facts about every skill, against the limits Anthropic and the Agent Skills specification state (stdlib + PyYAML).

    python scripts/skill_facts.py [--json out.json]     # print a table; optionally write the facts as JSON

This script measures. It does not score: whether a skill is good is a judgement made against docs/skill-review-rubric.md.
Every fact names the source rule it comes from (keys in the rubric). Token counts are an estimate (characters / 4).
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import skill_form as sf  # noqa: E402
import skillpaths as skp  # noqa: E402

RESERVED = ("anthropic", "claude")
NAME = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
MD_LINK = re.compile(r"\[[^\]]*\]\(([^)#]+)(?:#[^)]*)?\)")
DATE = re.compile(r"\b(20\d\d)-(\d\d)-(\d\d)\b|\b(?:before|after|until|since) (?:20\d\d|[A-Z][a-z]+ 20\d\d)\b")


def frontmatter(text: str) -> tuple[dict, str]:
    text = text.replace("\r\n", "\n")
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    return (yaml.safe_load(m.group(1)) or {}, text[m.end():]) if m else ({}, text)


def facts(name: str) -> dict:
    d = skp.skill_dir(name)
    fm, body = frontmatter((d / "SKILL.md").read_text(encoding="utf-8"))
    desc = " ".join(str(fm.get("description", "")).split())
    refs = sorted((d / "references").glob("*.md")) if (d / "references").is_dir() else []
    nested = []
    for r in refs:
        text = r.read_text(encoding="utf-8")
        if r.name == "index.md":
            continue
        for tgt in MD_LINK.findall(text):
            if tgt.startswith("http"):
                continue
            t = (r.parent / tgt).resolve()
            if t.suffix == ".md" and t.parent.name == "references" and t != r.resolve() and t.name != "index.md":
                nested.append(f"{r.name} -> {t.name}")
    long_no_toc = []
    for r in refs:
        if r.name == "index.md":
            continue
        lines = r.read_text(encoding="utf-8").split("\n")
        if len(lines) > 100 and not re.search(r"(?im)^#{1,3}\s+(contents|table of contents)\b", "\n".join(lines[:60])):
            long_no_toc.append(f"{r.name} ({len(lines)} lines)")
    scripts = sorted((d / "scripts").glob("*.py")) if (d / "scripts").is_dir() else []
    script_facts = []
    for s in scripts:
        t = s.read_text(encoding="utf-8")
        script_facts.append({
            "file": s.name, "is_test": s.name.startswith("test_"),
            "arg_parsing": bool(re.search(r"argparse|sys\.argv", t)),
            "help": bool(re.search(r"argparse|--help|__doc__", t)),
            "interactive_input": bool(re.search(r"(?<![\w.])input\(", t)),
            "exit_codes": bool(re.search(r"sys\.exit|SystemExit|return \d", t)),
        })
    windows = len(re.findall(r"(?<![\w:/])(?:scripts|references|assets)\\[\w.-]+", body))
    return {
        "skill": name, "library": skp.library_of(name),
        "name_valid": bool(NAME.match(name)) and len(name) <= 64 and not any(r in name for r in RESERVED) and fm.get("name") == name,
        "description_chars": len(desc), "description_ok": 0 < len(desc) <= 1024 and "<" not in desc,
        "body_lines": body.count("\n") + 1, "body_under_500_lines": body.count("\n") + 1 < 500,
        "body_tokens_estimate": round(len(body) / 4),
        "reference_files": len(refs), "nested_reference_links": nested, "long_references_without_toc": long_no_toc,
        "windows_paths_in_body": windows,
        "scripts": script_facts,
        "has_evals": (d / "evals" / "evals.json").is_file(),
        "dates_in_body": sorted(set(m.group(0) for m in DATE.finditer(body)))[:5],
        "form_findings": len(sf.lint(name)),
        "top_level_keys": sorted(fm),
    }


def main(argv: list[str]) -> int:
    rows = [facts(n) for n in sorted(skp.all_ids())]
    if "--json" in argv:
        Path(argv[argv.index("--json") + 1]).write_text(json.dumps(rows, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"{'skill':28} {'desc':>5} {'lines':>5} {'~tok':>5} {'nest':>4} {'scr':>3} {'evals':>5}")
    for r in rows:
        print(f"{r['skill']:28} {r['description_chars']:5d} {r['body_lines']:5d} {r['body_tokens_estimate']:5d} {len(r['nested_reference_links']):4d} {len(r['scripts']):3d} {str(r['has_evals']):>5}")
    print(f"\n{len(rows)} skills | name invalid: {sum(not r['name_valid'] for r in rows)} | description over 1024 or empty: "
          f"{sum(not r['description_ok'] for r in rows)} | body 500 lines or more: {sum(not r['body_under_500_lines'] for r in rows)} | "
          f"nested reference links: {sum(bool(r['nested_reference_links']) for r in rows)} | with evals: {sum(r['has_evals'] for r in rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
