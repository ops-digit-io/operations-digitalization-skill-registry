#!/usr/bin/env python3
"""Build docs/skill-review.md from docs/new-state/skill-review.json (the reviews of every skill against docs/skill-review-rubric.md).

    python scripts/build_skill_review.py --merge <folder with one <skill>.json per review> [--facts facts.json] [--run-date YYYY-MM-DD]
                                                      # read the reviews, validate them, write docs/new-state/skill-review.json, then the page
    python scripts/build_skill_review.py              # rebuild the page from docs/new-state/skill-review.json
    python scripts/build_skill_review.py --check      # fail if the page is stale

The measured facts (scripts/skill_facts.py) are recomputed here, never taken from a reviewer. The judgements are a reviewer's reading of
the skill text against the criteria of the rubric, with a quote as evidence. Nothing is scored by a formula: the overall rating is the
reviewer's, and the counts are reported next to it. The page compares the judgement with the SkillEvaluator rating of
docs/new-state/skill-quality.json, which measures other things (a fixed set of rules and headings).
"""
from __future__ import annotations

import collections
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
import skill_facts as sfx  # noqa: E402
import skillpaths as skp  # noqa: E402

DATA = ROOT / "docs" / "new-state" / "skill-review.json"
QUALITY = ROOT / "docs" / "new-state" / "skill-quality.json"
PAGE = ROOT / "docs" / "skill-review.md"
RATINGS = ("meets", "partly", "gap", "n/a")
OVERALL = ("strong", "adequate", "needs-work")
CRITERIA = {
    "J1": "Description says what and when", "J2": "Description: one point of view, user intent", "J3": "Concise: only what the agent lacks",
    "J4": "Specificity matches fragility", "J5": "Procedures over declarations", "J6": "Defaults, not menus", "J7": "Gotchas in SKILL.md",
    "J8": "Output templates", "J9": "Concrete examples", "J10": "Checklist, validation loop, plan-validate-execute",
    "J11": "Progressive disclosure: says when to read what", "J12": "Consistent terminology", "J13": "Explains the why",
    "J14": "Scripts solve, handle errors, state dependencies", "J15": "One coherent unit", "J16": "Grounded in real expertise",
}


def validate(r: dict) -> list[str]:
    errs = []
    if set(r.get("criteria", {})) != set(CRITERIA):
        errs.append(f"{r.get('skill')}: criteria must be exactly {sorted(CRITERIA)}")
        return errs
    for k, v in r["criteria"].items():
        if v.get("rating") not in RATINGS:
            errs.append(f"{r['skill']} {k}: rating '{v.get('rating')}'")
        if v.get("rating") != "n/a" and not str(v.get("evidence", "")).strip():
            errs.append(f"{r['skill']} {k}: no evidence")
        if v.get("rating") in ("partly", "gap") and not str(v.get("change", "")).strip():
            errs.append(f"{r['skill']} {k}: {v['rating']} without a change")
    if r.get("overall", {}).get("rating") not in OVERALL or not r["overall"].get("reason"):
        errs.append(f"{r['skill']}: overall rating and reason needed")
    return errs


def merge(folder: Path, run_date: str) -> dict:
    reviews, errs = {}, []
    for p in sorted(folder.glob("*.json")):
        r = json.loads(p.read_text(encoding="utf-8"))
        errs += validate(r)
        reviews[r["skill"]] = r
    missing = sorted(set(skp.all_ids()) - set(reviews))
    if missing:
        errs.append(f"no review for: {', '.join(missing)}")
    if errs:
        print("\n".join(f"  - {e}" for e in errs), file=sys.stderr)
        raise SystemExit(f"{len(errs)} problem(s) in the reviews")
    return {"run_date": run_date, "rubric": "docs/skill-review-rubric.md", "reviewed_by": "an AI reviewer reading each skill; not a human review",
            "skills": {k: reviews[k] for k in sorted(reviews)}}


def evidence_check(rev: dict) -> tuple[int, int, int]:
    """(quotes checked, quotes found in the skill's own files, 'absent' statements). A quote is what the reviewer put between quotation marks."""
    def norm(t):
        return re.sub(r"\s+", " ", re.sub(r"[*_`]", "", t)).strip().lower()

    total = found = absent = 0
    for name, r in rev.items():
        d = skp.skill_dir(name)
        corpus = norm(" ".join(f.read_text(encoding="utf-8", errors="ignore") for f in d.rglob("*") if f.is_file() and f.suffix in (".md", ".yaml", ".py")))
        for v in r["criteria"].values():
            if v["rating"] == "n/a":
                continue
            ev = v["evidence"].strip()
            if ev.lower().startswith("absent"):
                absent += 1
                continue
            total += 1
            qs = re.findall(r'["\u201c\u00ab]([^"\u201d\u00bb]{12,})["\u201d\u00bb]', ev) or [re.sub(r"\s*\([^)]*\)\s*$", "", ev)]
            if any(q and norm(q).rstrip(".")[:60] in corpus for q in qs):
                found += 1
    return total, found, absent


def esc(s) -> str:
    """One line for a table cell; links inside quoted evidence become plain text (they would not resolve from docs/)."""
    return re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", " ".join(str(s).split())).replace("|", "/")


def render(data: dict) -> str:
    rev = data["skills"]
    q = json.loads(QUALITY.read_text(encoding="utf-8"))["skills"] if QUALITY.exists() else {}
    facts = {n: sfx.facts(n) for n in rev}
    n = len(rev)
    core = [s for s in rev if skp.library_of(s) == "core"]
    ov = collections.Counter(rev[s]["overall"]["rating"] for s in rev)
    ovc = collections.Counter(rev[s]["overall"]["rating"] for s in core)

    def count(s):
        c = collections.Counter(v["rating"] for v in rev[s]["criteria"].values())
        return c["gap"], c["partly"]

    out = ["---", "type: Design Record", "title: Skill review", f"description: \"The review of all {n} skills against Anthropic's skill authoring best practices and the Agent Skills specification - measured facts, a judgement per criterion with a quote as evidence, an overall rating, and how it compares with the SkillEvaluator rating.\"",
           "status: draft", "owner: human:jakob.gabriel", "tags: [skills, review, anthropic]", "generated: { by: claude-code/1, at: 2026-11-16T00:00:00Z }", "---",
           "# Skill review", "",
           f"Reviewed {data['run_date']} against [`skill-review-rubric.md`](skill-review-rubric.md). **{data['reviewed_by']}.** The rubric is taken from Anthropic's published best practices and the open Agent Skills specification; each criterion carries its source quote there.", "",
           "- **Measured facts** (`scripts/skill_facts.py`) are computed from the files and checked against the limits the sources state.",
           "- **Judgements** are a reviewer's reading of the skill text per criterion, each with a quote as evidence and, for a weakness, one concrete change. The overall rating is the reviewer's, with a reason. Nothing is a formula.",
           "- **Not measured:** whether the skill makes an agent behave better. The sources ask for evaluations with and without the skill; none of the skills has any (see the facts).",
           "- **Evidence check:** " + "{} of {} evidence quotes were found word for word in the skill's own files by a script; the rest mix a quote with a description, or are plain statements of absence ({} of those). A reviewer can be wrong: confirm a rating before acting on it.".format(*evidence_check(rev)[1::-1], evidence_check(rev)[2]), "",
           "## Overall", "", "| | strong | adequate | needs-work |", "|---|---|---|---|",
           f"| All {n} skills | {ov['strong']} | {ov['adequate']} | {ov['needs-work']} |", f"| {len(core)} core skills | {ovc['strong']} | {ovc['adequate']} | {ovc['needs-work']} |", ""]
    out += ["## Measured facts", "", "| Fact (source key) | Result |", "|---|---|",
            f"| F1 name valid (AS, AB) | {sum(f['name_valid'] for f in facts.values())} of {n} |",
            f"| F2 description non-empty, at most 1024 characters (AB, AS) | {sum(f['description_ok'] for f in facts.values())} of {n}; longest {max(f['description_chars'] for f in facts.values())} |",
            f"| F3 body under 500 lines (AB, AS) | {sum(f['body_under_500_lines'] for f in facts.values())} of {n}; longest {max(f['body_lines'] for f in facts.values())} lines |",
            f"| F4 body under about 5,000 tokens, estimated (AS) | {sum(f['body_tokens_estimate'] < 5000 for f in facts.values())} of {n}; over: {', '.join(s for s, f in facts.items() if f['body_tokens_estimate'] >= 5000) or 'none'} |",
            f"| F5 references one level deep (AB, AS) | {sum(not f['nested_reference_links'] for f in facts.values())} of {n}; nested links in: {', '.join(s for s, f in facts.items() if f['nested_reference_links']) or 'none'} |",
            f"| F6 long references have a table of contents (AB) | {sum(not f['long_references_without_toc'] for f in facts.values())} of {n} |",
            f"| F7 forward slashes only (AB) | {sum(f['windows_paths_in_body'] == 0 for f in facts.values())} of {n} |",
            f"| F9 evaluations exist (AB, AE) | {sum(f['has_evals'] for f in facts.values())} of {n} |", ""]
    out += ["## Criteria across all skills", "", "| Criterion | meets | partly | gap | n/a |", "|---|---|---|---|---|"]
    tally = {k: collections.Counter(rev[s]["criteria"][k]["rating"] for s in rev) for k in CRITERIA}
    for k, label in CRITERIA.items():
        t = tally[k]
        out.append(f"| {k} {label} | {t['meets']} | {t['partly']} | {t['gap']} | {t['n/a']} |")
    weakest = sorted(CRITERIA, key=lambda k: -(tally[k]["gap"] * 2 + tally[k]["partly"]))[:5]
    out += ["", "Where most skills fall short, by gaps first: " + "; ".join(f"{k} {CRITERIA[k]} ({tally[k]['gap']} gap, {tally[k]['partly']} partly)" for k in weakest) + ".", ""]
    out += ["## Per skill, next to the SkillEvaluator rating", "",
            "The SkillEvaluator rating checks a fixed set of rules and headings (the registry's configuration); this review judges the text against the published practices. They measure different things.", "",
            "| Skill | Library | Review | Gaps | Partly | SkillEvaluator | Description chars | Body lines | Evals |", "|---|---|---|---|---|---|---|---|---|"]
    for s in sorted(rev):
        g, p = count(s)
        qq = q.get(s, {})
        out.append(f"| [`{s}`](#{s}) | {skp.library_of(s)} | {rev[s]['overall']['rating']} | {g} | {p} | {qq.get('grade', '?')} {qq.get('score', '')} | {facts[s]['description_chars']} | {facts[s]['body_lines']} | {'yes' if facts[s]['has_evals'] else 'no'} |")
    disagree = [s for s in sorted(rev) if q.get(s, {}).get("grade") == "A" and rev[s]["overall"]["rating"] == "needs-work"] + \
               [s for s in sorted(rev) if q.get(s, {}).get("grade") in ("B", "C") and rev[s]["overall"]["rating"] == "strong"]
    out += ["", "**Where the two disagree:** " + (", ".join(f"`{s}` (SkillEvaluator {q[s]['grade']}, review {rev[s]['overall']['rating']})" for s in disagree) if disagree else "none by this simple comparison") + ".", ""]
    out += ["## House rules against the published practices", ""]
    eff = [(s, e) for s in sorted(rev) for e in rev[s].get("house_rule_effects", [])]
    out += [f"- `{s}`: {esc(e)}" for s, e in eff[:60]] or ["- none reported"]
    out += ["", "## The skills", ""]
    for s in sorted(rev):
        r = rev[s]
        g, p = count(s)
        out += [f"### {s}", "", f"**{r['overall']['rating']}**: {esc(r['overall']['reason'])} ({g} gap, {p} partly; {skp.library_of(s)} library)", ""]
        if r.get("top_improvements"):
            out += ["Improve first:"] + [f"{i}. {esc(x)}" for i, x in enumerate(r["top_improvements"], 1)] + [""]
        weak = [(k, v) for k, v in r["criteria"].items() if v["rating"] in ("gap", "partly")]
        if weak:
            out += ["| Criterion | Rating | Evidence | Change |", "|---|---|---|---|"]
            out += [f"| {k} {CRITERIA[k]} | {v['rating']} | {esc(v['evidence'])} | {esc(v['change'])} |" for k, v in weak]
            out.append("")
        if r.get("fact_notes"):
            out += ["Facts: " + "; ".join(esc(x) for x in r["fact_notes"]), ""]
    return "\n".join(out).rstrip() + "\n"


def main(argv: list[str]) -> int:
    if "--merge" in argv:
        run_date = argv[argv.index("--run-date") + 1] if "--run-date" in argv else "2026-11-16"
        data = merge(Path(argv[argv.index("--merge") + 1]), run_date)
        DATA.write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    data = json.loads(DATA.read_text(encoding="utf-8"))
    text = render(data)
    if "--check" in argv:
        cur = PAGE.read_text(encoding="utf-8").replace("\r\n", "\n") if PAGE.exists() else ""
        print("skill review up to date" if cur == text else "stale: docs/skill-review.md")
        return 0 if cur == text else 1
    PAGE.write_text(text, encoding="utf-8", newline="\n")
    print(f"wrote {PAGE.name}: {len(data['skills'])} skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
