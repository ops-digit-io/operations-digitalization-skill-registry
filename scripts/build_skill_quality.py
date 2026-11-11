#!/usr/bin/env python3
"""Turn a SkillEvaluator quality-check report into the registry's skill ratings (stdlib).

    python scripts/build_skill_quality.py CORE.json [EXTENSION.json ...] [--default-report DEFAULT.json] \
        --tool-commit d717f22 --run-date 2026-11-10          # write docs/new-state/skill-quality.json + docs/skill-quality.md
    python scripts/build_skill_quality.py --check            # fail if the page is stale or a skill has no rating

The ratings come from NVIDIA SkillEvaluator (Apache-2.0, https://github.com/NVIDIA/SkillEvaluator), tier 1
`quality-check`, run with this repository's `config/skill-quality.yaml`:

    skillevaluator quality-check skills --quality-config config/skill-quality.yaml -r json -o <output>
    skillevaluator quality-check skills-extension --quality-config config/skill-quality.yaml -r json -o <output>

The tool is not run here (it needs Python 3.12 or newer and its own dependencies); this script only reads its JSON
report. Category scores are derived as 100 minus the deductions of that category, which reproduces the tool's overall
score exactly (checked per skill; a skill that does not reproduce is stored without category scores).
"""
from __future__ import annotations

import collections
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
import skillpaths as skp  # noqa: E402

DATA = ROOT / "docs" / "new-state" / "skill-quality.json"
PAGE = ROOT / "docs" / "skill-quality.md"
WEIGHTS = {"correctness": 0.35, "discoverability": 0.25, "reliability": 0.25, "efficiency": 0.15}
LABEL = {"correctness": "Correctness", "discoverability": "Discoverability", "reliability": "Reliability", "efficiency": "Efficiency"}
SCALE = [("A", 90), ("B", 80), ("C", 70), ("D", 60), ("F", 0)]


def grade_of(score: float) -> str:
    return next(g for g, lo in SCALE if score >= lo)


def read_report(path: Path) -> dict:
    """Per skill: overall score, grade and the findings with their category and deduction."""
    d = json.loads(path.read_text(encoding="utf-8"))
    r = d["results"][0]
    out: dict[str, dict] = {}
    for x in r["success_details"]:
        m = re.match(r"\[(.+?)\] quality_score", x["check"])
        if m:
            out[m.group(1)] = {"score": x["metadata"]["overall_score"], "grade": x["metadata"]["grade"],
                               "type": x["metadata"].get("skill_type", ""), "findings": []}
    for f in r["findings"]:
        m = re.match(r"\[(.+?)\]", f["file_path"])
        if m and m.group(1) in out:
            out[m.group(1)]["findings"].append({"dimension": f["metadata"]["dimension"], "deduction": f["metadata"]["deduction"],
                                                "message": f["message"], "suggestion": f.get("suggestion", "")})
    return {"skills": out, "config": d.get("quality_config", {}), "min_score": d.get("quality_config", {}).get("min_score")}


def build(reports: list[Path], default_report: Path | None, tool_commit: str, run_date: str) -> dict:
    main = read_report(reports[0])
    for extra in reports[1:]:
        main["skills"].update(read_report(extra)["skills"])
    dflt = read_report(default_report)["skills"] if default_report else {}
    skills = {}
    registry = set(skp.all_ids())
    for name, v in sorted(main["skills"].items()):
        if name not in registry:   # a skill copied unchanged inside another one (e.g. OpenSpec's in it-demand-package) is not rated
            continue
        dims = collections.defaultdict(float)
        for f in v["findings"]:
            dims[f["dimension"]] += f["deduction"]
        derived = round(sum(w * (100 - dims[k]) for k, w in WEIGHTS.items()), 1)
        entry = {"score": v["score"], "grade": v["grade"], "skill_type": v["type"],
                 "folder_hash": skp.folder_hash(name),
                 "findings": sorted(v["findings"], key=lambda f: (-f["deduction"], f["dimension"], f["message"]))}
        if abs(derived - v["score"]) < 0.06:
            entry["categories"] = {k: round(100 - dims[k], 1) for k in WEIGHTS}
        if name in dflt:
            entry["default_score"] = dflt[name]["score"]
        skills[name] = entry
    mean = round(sum(s["score"] for s in skills.values()) / len(skills), 1)
    core_scores = [s["score"] for n, s in skills.items() if skp.library_of(n) == "core"]
    return {
        "tool": {"name": "NVIDIA SkillEvaluator", "license": "Apache-2.0", "source": "https://github.com/NVIDIA/SkillEvaluator",
                 "commit": tool_commit, "tier": "1, quality-check (deterministic, offline)",
                 "docs": "https://docs.nvidia.com/skills/skillevaluator/"},
        "config": {"file": "config/skill-quality.yaml", "digest": main["config"].get("digest", "")},
        "run_date": run_date,
        "weights": WEIGHTS,
        "scale": {g: lo for g, lo in SCALE},
        "mean": mean,
        "mean_core": round(sum(core_scores) / len(core_scores), 1),
        "skills": skills,
    }


def render(data: dict) -> str:
    sk = {n: v for n, v in data["skills"].items() if skp.library_of(n) == "core"}  # the published page lists core skills only
    L = ["---", "type: Design Record", "title: Skill quality",
         'description: "How the core skills are rated (NVIDIA SkillEvaluator tier 1 quality-check with the registry\'s own configuration): the scale, the four categories, what the score does not measure, and the score of every core skill."',
         "status: draft", "owner: human:jakob.gabriel", "tags: [quality, rating, process-flow]",
         "generated: { by: claude-code/1, at: 2026-11-10T00:00:00Z }", "---",
         "<!-- Generated by scripts/build_skill_quality.py from docs/new-state/skill-quality.json - do not edit by hand. -->",
         "# Skill quality", "",
         f"Each core skill carries a quality rating on the process map and the flow: a **grade** (A to F) and a **score** (0 to 100). "
         f"The rating comes from the open-source tool [{data['tool']['name']}]({data['tool']['source']}) ({data['tool']['license']}), "
         f"{data['tool']['tier']}, run on {data['run_date']} (tool commit `{data['tool']['commit']}`) with this repository's "
         f"configuration `{data['config']['file']}`. It replaces the earlier Built, Partial and Gap status: every skill exists.", "",
         "## How the score is made", "",
         "| Category | Weight | What it covers (the tool's own words) |", "|---|---|---|",
         '| Correctness | 35% | "Frontmatter, naming, examples, paths, and skill-type-specific structure" |',
         '| Discoverability | 25% | "Description quality, trigger wording, purpose, scope, and naming" |',
         '| Reliability | 25% | "Error handling, prerequisites, limitations, troubleshooting, and implementation safeguards" |',
         '| Efficiency | 15% | "Token budget, body length, repetition, instruction clarity, and reference use" |', "",
         "Each category starts at 100 and loses points for each finding; the score is the weighted sum. Grades: A from 90, B from 80, C from 70, D from 60, F below 60. "
         "The tool's default expects the headings Prerequisites, Limitations and Troubleshooting; this registry replaces them (tool option `--quality-config`) "
         "with the sections it expects of every skill: Inputs, Procedure, Human gate, Do not (or Pitfalls), Definition of done (or Handoff), 5 points each.", "",
         "## What the score does not measure", "",
         "- It rates **documentation quality**: structure, wording, size and completeness. It does **not** measure whether a skill helps an agent do the task; "
         "that is the tool's tier 3 (live runs with and without the skill) and the evaluation method of the Agent Skills guides, neither of which has been run.",
         "- Part of the score is the tool's own convention, not a department rule: every skill loses the same points for the frontmatter fields `version`, `metadata.author` and `metadata.tags`. "
         "The Agent Skills specification allows only six top-level keys, so `version` cannot be added without breaking the specification export, and the registry has not added `metadata.author` and `metadata.tags`; "
         "differences between skills come from the other findings.",
         "- Tool and rubric are third-party and marked experimental by the vendor. A grade is a prompt for a review, not a verdict on a skill's content.", "",
         f"## Scores of the core skills (mean {data['mean_core']})", "",
         "| Skill | Grade | Score | Correctness | Discoverability | Reliability | Efficiency | Largest deduction |", "|---|---|---|---|---|---|---|---|"]
    for name, s in sorted(sk.items(), key=lambda kv: (-kv[1]["score"], kv[0])):
        c = s.get("categories", {})
        top = next((f for f in s["findings"] if "recommended field missing" not in f["message"]), None)
        L.append(f"| [`{name}`](../skills/{name}/SKILL.md) | {s['grade']} | {s['score']} | " +
                 " | ".join(str(c.get(k, "-")) for k in WEIGHTS) + f" | {top['message'] + ' (-' + str(top['deduction']) + ')' if top else '-'} |")
    L += ["", "## Where the points go", "",
          "| Finding | Skills affected | Points each |", "|---|---|---|"]
    cnt: dict[tuple, int] = collections.Counter()
    for s in sk.values():
        for f in s["findings"]:
            cnt[(f["message"], f["deduction"])] += 1
    for (m, p), n in sorted(cnt.items(), key=lambda kv: (-kv[1], kv[0][0]))[:12]:
        L.append(f"| {m} | {n} of {len(sk)} | {p} |")
    L += ["", "## Sources", "",
          "- NVIDIA SkillEvaluator documentation, https://docs.nvidia.com/skills/skillevaluator/ , and source repository, https://github.com/NVIDIA/SkillEvaluator (Apache-2.0), read 2026-11-10. The categories, weights and grade bands above are quoted from its documentation; the deduction model was checked in its source (`validators/quality_score.py`).",
          "- Agent Skills specification and guides, https://agentskills.io/specification.md and https://agentskills.io/skill-creation/evaluating-skills.md , read 2026-11-10: the evaluation method (test cases, with-skill and without-skill runs) that this rating does not replace.", ""]
    return "\n".join(L)


def check() -> int:
    if not DATA.exists():
        print("missing docs/new-state/skill-quality.json")
        return 1
    data = json.loads(DATA.read_text(encoding="utf-8"))
    core = [n for n in skp.all_ids() if skp.library_of(n) == "core"]
    missing = [n for n in skp.all_ids() if n not in data["skills"]]
    if missing:
        print("skills without a quality rating:", ", ".join(missing))
        return 1
    cur = PAGE.read_text(encoding="utf-8") if PAGE.exists() else ""
    if cur.replace("\r\n", "\n") != render(data):
        print("stale: docs/skill-quality.md")
        return 1
    stale = [n for n in skp.all_ids() if data["skills"][n]["folder_hash"] != skp.folder_hash(n)]
    print("skill quality ratings present for all skills" + (f"; changed since the rating run (rerun the tool): {', '.join(stale)}" if stale else ""))
    return 0


if __name__ == "__main__":
    a = sys.argv[1:]
    if "--check" in a:
        raise SystemExit(check())
    opts = {"--default-report", "--tool-commit", "--run-date"}
    reps = [Path(x) for i, x in enumerate(a) if not x.startswith("--") and (i == 0 or a[i - 1] not in opts)]
    dflt = Path(a[a.index("--default-report") + 1]) if "--default-report" in a else None
    commit = a[a.index("--tool-commit") + 1] if "--tool-commit" in a else ""
    day = a[a.index("--run-date") + 1] if "--run-date" in a else ""
    data = build(reps, dflt, commit, day)
    DATA.write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    PAGE.write_text(render(data), encoding="utf-8", newline="\n")
    print(f"wrote {DATA.relative_to(ROOT)} and {PAGE.relative_to(ROOT)}: {len(data['skills'])} skills, mean {data['mean']}")
