#!/usr/bin/env python3
"""Evaluate a use case's envisioned solution against the 16-focus-area maturity model.

    python3 evaluate_fit.py USE_CASE.json              # full report, ASCII visualization
    python3 evaluate_fit.py USE_CASE.json --json        # machine-readable
    python3 evaluate_fit.py --demo                      # built-in worked example

USE_CASE.json shape (see ../assets/example-use-case.json for a filled-in example):

    {
      "name": "Illustrative: predictive quality alert, <line>",
      "drivers": {"a14": "h", "a23": "d", "a9": "m"},   # rated h/d matter; n/l/m are context
      "as_is":  {"F3": 2, "F11": 2, "F13": 2, "F14": 2, "F16": 1},
      "target": {"F3": 3, "F11": 3, "F13": 3, "F14": 4, "F16": 2}
    }

Only list the focus areas you actually have evidence for in `as_is`; `target` is optional —
omit it to get the candidate areas and the case ranking only (step 0 and step 2 of the
skill), without a gap analysis.

No dependencies beyond the standard library. Loads `model_data.json` (focus-area levels,
complexity-driver -> area mapping, best-fit realization dependencies — generalized from
Schott et al. 2017/2020, see SKILL.md `derived_from`) and `../assets/case-library.csv` (the
70-case literature cold-start base, same source) from fixed relative paths.
"""

from __future__ import annotations

import csv
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
MODEL = json.loads((HERE / "model_data.json").read_text(encoding="utf-8"))
CASE_LIB = HERE.parent / "assets" / "case-library.csv"

AREAS = MODEL["focus_areas"]          # Fn -> {name, levels: [{code, level, label, evidence}]}
DRIVERS = MODEL["complexity_drivers"]  # an -> {name, category, areas: [Fn, ...]}
DEPS = MODEL["dependencies_best_fit"]  # "Cn-L" -> ["Cm-K", ...]

RATED_HIGH = {"h", "d"}


def area_level_label(area: str, level: int) -> str:
    for L in AREAS[area]["levels"]:
        if L["level"] == level:
            return L["label"]
    return "?"


def max_level(area: str) -> int:
    return max(L["level"] for L in AREAS[area]["levels"])


def code_of(area: str, level: int) -> str:
    return f"C{area[1:]}-{level}"


# ── step 0+2: candidate areas from rated drivers ─────────────────────────────

def candidate_areas(drivers: dict) -> dict:
    """area -> list of driver ids (rated h/d) that make it a candidate."""
    out: dict[str, list[str]] = {}
    for d_id, rating in drivers.items():
        if rating not in RATED_HIGH or d_id not in DRIVERS:
            continue
        for area in DRIVERS[d_id]["areas"]:
            out.setdefault(area, []).append(d_id)
    return out


# ── step 0: case ranking (pre-evaluation) ────────────────────────────────────

def load_case_library() -> list[dict]:
    with open(CASE_LIB, encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def rank_cases(levels: dict, top_n: int = 5) -> list[tuple[dict, float]]:
    """Similarity = 1 - mean absolute level difference / 3, over the areas both the use
    case and the case specify. 3 is the largest level span any area has (F7, F14). A case
    that shares no dimension with the input is dropped, not scored 0 - it is not comparable,
    not merely dissimilar."""
    scored = []
    for case in load_case_library():
        diffs = []
        for area, lvl in levels.items():
            v = case.get(area, "")
            if v == "":
                continue
            diffs.append(abs(int(v) - int(lvl)))
        if not diffs:
            continue
        similarity = 1.0 - (sum(diffs) / len(diffs)) / 3.0
        scored.append((case, max(0.0, similarity)))
    scored.sort(key=lambda cs: -cs[1])
    return scored[:top_n]


# ── steps 3-4: gaps, dependency sequencing, over-engineering ─────────────────

def analyze_gaps(as_is: dict, target: dict, candidates: dict) -> dict:
    gaps = {}
    over_engineered = []
    for area, tgt in target.items():
        cur = as_is.get(area, 0)
        if area not in candidates:
            over_engineered.append(area)
        if tgt > cur:
            gaps[area] = {"from": cur, "to": tgt}
    return {"gaps": gaps, "over_engineered": over_engineered}


def sequence_gaps(gaps: dict, as_is: dict) -> dict:
    """Ready now (prerequisites already met by as_is), or blocked on a named prerequisite
    this use case has not planned. Not a full topological sort across gaps planned together
    in the same wave - see references/dependencies.md for why that needs human judgement."""
    satisfied = {code_of(a, lvl) for a, lvl in as_is.items()}
    # also: any lower level of an area already reached implies every level below it
    for a, lvl in as_is.items():
        for L in range(1, lvl + 1):
            satisfied.add(code_of(a, L))

    result = {}
    for area, g in gaps.items():
        target_code = code_of(area, g["to"])
        reqs = DEPS.get(target_code, [])
        missing = [r for r in reqs if r not in satisfied and r not in
                   {code_of(a2, gg["to"]) for a2, gg in gaps.items()}]
        result[area] = {"target_code": target_code, "requires": reqs, "missing": missing,
                         "ready": not missing}
    return result


# ── score and verdict ─────────────────────────────────────────────────────────

def total_score(best_sim: float | None, target: dict, candidates: dict, seq: dict) -> dict:
    # Case-fit confidence (0-40): no comparable case at all scores 0, not a free pass.
    case_fit = round((best_sim or 0.0) * 40)

    # Driver-justified targets (0-30): share of set targets that land on a candidate area.
    if target:
        justified = sum(1 for a in target if a in candidates)
        driver_score = round(30 * justified / len(target))
    else:
        driver_score = 0  # nothing to judge yet - not a free pass either

    # Gap feasibility (0-30): share of gaps that are ready now or have every prerequisite
    # inside this same plan. No gaps at all scores full marks - there is nothing blocking.
    if seq:
        ready = sum(1 for s in seq.values() if s["ready"])
        gap_score = round(30 * ready / len(seq))
    else:
        gap_score = 30

    total = case_fit + driver_score + gap_score
    return {"case_fit": case_fit, "driver_score": driver_score, "gap_score": gap_score,
            "total": total}


def verdict(score: dict, over_engineered: list, seq: dict) -> str:
    unresolved = [a for a, s in seq.items() if not s["ready"]]
    if over_engineered and not seq:
        return "OVER-ENGINEERED"
    if len(unresolved) >= 3 or (seq and len(unresolved) == len(seq) and len(seq) > 1):
        return "ESCALATE AS A PLATFORM INVESTMENT"
    if not seq and not over_engineered:
        return "READY TO BUILD"
    if score["total"] >= 70 and not unresolved:
        return "READY TO BUILD" if not over_engineered else "OVER-ENGINEERED"
    return "NEEDS A CAPABILITY RAISED FIRST"


# ── ASCII visualization ───────────────────────────────────────────────────────

def bar(pct: float, width: int = 20) -> str:
    filled = round(width * max(0.0, min(1.0, pct)))
    return "[" + "#" * filled + "_" * (width - filled) + "]"


def render(uc: dict) -> str:
    name = uc.get("name", "(unnamed use case)")
    drivers = uc.get("drivers", {})
    as_is = uc.get("as_is", {})
    target = uc.get("target", {})

    candidates = candidate_areas(drivers)
    ranked = rank_cases(target or as_is)
    gaps_info = analyze_gaps(as_is, target, candidates) if target else {"gaps": {}, "over_engineered": []}
    seq = sequence_gaps(gaps_info["gaps"], as_is)
    best_sim = ranked[0][1] if ranked else None
    score = total_score(best_sim, target, candidates, seq)
    v = verdict(score, gaps_info["over_engineered"], seq)

    L = []
    L.append(f"=== {name} ===\n")

    L.append("-- Step 0+2: candidate focus areas (from drivers rated high/dominant) --")
    if candidates:
        for area, by in sorted(candidates.items()):
            L.append(f"  {area:4s} {AREAS[area]['name']:35s} <- " + ", ".join(by))
    else:
        L.append("  none - rate at least one driver h or d to get candidates")
    L.append("")

    L.append(f"-- Step 0: case ranking (pre-evaluation, top {len(ranked)} of 70 literature cases) --")
    for case, sim in ranked:
        L.append(f"  case {case['case_no']:>2s} {case['source']:<32s} {bar(sim)} {sim*100:5.1f}%")
    if not ranked:
        L.append("  no comparable case - give at least one as_is or target level")
    L.append("")

    if target:
        L.append("-- Steps 3-4: gap per focus area --")
        if gaps_info["gaps"]:
            for area, g in sorted(gaps_info["gaps"].items()):
                span = max_level(area)
                frm_lbl = area_level_label(area, g["from"])
                to_lbl = area_level_label(area, g["to"])
                s = seq[area]
                tag = "ready now" if s["ready"] else f"blocked on {', '.join(s['missing'])}"
                L.append(f"  {area:4s} {AREAS[area]['name']:35s} {g['from']} {frm_lbl:22s}"
                          f"-> {g['to']} {to_lbl:22s} {bar(g['to']/span)} [{tag}]")
        else:
            L.append("  no gap - every target is already met")
        if gaps_info["over_engineered"]:
            L.append("  OVER-ENGINEERED: target set with no rated driver behind it -> "
                      + ", ".join(gaps_info["over_engineered"]))
        L.append("")

    L.append("-- Total evaluation score --")
    L.append(f"  Case-fit confidence:        {score['case_fit']:3d} / 40  "
             f"(best match {(best_sim or 0)*100:.0f}%)")
    L.append(f"  Driver-justified targets:   {score['driver_score']:3d} / 30")
    L.append(f"  Gap feasibility:            {score['gap_score']:3d} / 30")
    L.append(f"  TOTAL                       {score['total']:3d} / 100")
    L.append("")
    L.append(f"VERDICT: {v}")
    return "\n".join(L)


DEMO = {
    "name": "Illustrative: predictive quality alert, <line>",
    "drivers": {"a14": "h", "a23": "d", "a9": "m", "a20": "l"},
    "as_is":  {"F3": 2, "F11": 2, "F13": 2, "F14": 2, "F16": 1},
    "target": {"F3": 3, "F11": 3, "F13": 3, "F14": 4, "F16": 2},
}


def main(argv: list[str]) -> int:
    if "--demo" in argv:
        uc = DEMO
    else:
        paths = [a for a in argv[1:] if not a.startswith("--")]
        if not paths:
            print(__doc__)
            return 0
        uc = json.loads(pathlib.Path(paths[0]).read_text(encoding="utf-8"))
    if "--json" in argv:
        candidates = candidate_areas(uc.get("drivers", {}))
        ranked = rank_cases(uc.get("target") or uc.get("as_is", {}))
        gaps_info = analyze_gaps(uc.get("as_is", {}), uc.get("target", {}), candidates) if uc.get("target") else {"gaps": {}, "over_engineered": []}
        seq = sequence_gaps(gaps_info["gaps"], uc.get("as_is", {}))
        score = total_score(ranked[0][1] if ranked else None, uc.get("target", {}), candidates, seq)
        print(json.dumps({
            "candidates": candidates,
            "ranked_cases": [{"case_no": c["case_no"], "source": c["source"], "similarity": s}
                             for c, s in ranked],
            "gaps": seq,
            "over_engineered": gaps_info["over_engineered"],
            "score": score,
            "verdict": verdict(score, gaps_info["over_engineered"], seq),
        }, indent=2, ensure_ascii=False))
        return 0
    print(render(uc))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
