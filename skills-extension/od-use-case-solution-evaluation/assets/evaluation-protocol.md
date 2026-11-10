---
type: Skill Asset
title: Evaluation protocol
description: The defined output of the method - driver profile, case ranking, per-area gap, sequencing and a total evaluation score, so the result is a reusable record rather than prose.
resource: ../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [use-case-support-service, template, protocol]
generated: { by: claude-code/1, at: 2026-10-22T00:00:00Z }
---

# Use-case solution evaluation — ⟨use case name⟩

Copy once per use case. Run `python3 scripts/evaluate_fit.py <your-use-case>.json` first and
paste its output into the two sections marked below — the visualization and the score are
the record, not a summary written after the fact from memory of the run.

| | |
|---|---|
| **Use case** | ⟨name, plant, line⟩ |
| **From definition** | ⟨`od-use-case-definition` protocol reference⟩ |
| **Evaluator / date** | ⟨name⟩ · ⟨date⟩ |
| **Overall verdict** | ⟨ready to build · needs a capability raised first · over-engineered · escalate⟩ |

## 1 · Driver profile

Rated independently by ⟨requester⟩ and ⟨DBVE/IIAE⟩, then reconciled.

| Driver | Rating | Reconciled | Note |
|---|---|---|---|
| ⟨a14 — shop-floor control/monitoring⟩ | ⟨h/d⟩ | ⟨h/d⟩ | |
| ⟨…⟩ | | | |

Only drivers rated **h** or **d** above feed step 2; see `references/complexity-drivers.md`
for the full 27 and which focus areas each one points at.

## 2 · Candidate focus areas

⟨List from `scripts/evaluate_fit.py`'s "Step 0+2" block — paste it here.⟩

## 3 · Case ranking (pre-evaluation)

**Paste the script's "Step 0: case ranking" block here, unedited — this is the
visualization, not a paraphrase of it.**

A best match at or above ~80% means a documented configuration already looks like this one;
treat it as a reason to move faster through steps 4-6, not as a reason to skip them. No case
within reasonable distance of any candidate area is itself the finding: this use case is
genuinely novel for this registry, and `od-decision-routing` should know that before the
business case is calculated.

## 4 · As-is and target, per candidate area

| Focus area | As-is | Evidence | Target | Justified by (driver / business need) |
|---|---|---|---|---|
| ⟨F11 Degree of data collection⟩ | ⟨level + label⟩ | ⟨source⟩ | ⟨level + label⟩ | ⟨a14, a23 / or the named business need⟩ |
| ⟨…⟩ | | | | |

A target with nothing in the last column is the over-engineering case — lower it or name
what actually justifies it before moving on.

## 5 · Gaps and sequencing

**Paste the script's "Steps 3-4: gap per focus area" block here, unedited.**

| Gap | Ready now / blocked on | Owner | Target skill |
|---|---|---|---|
| ⟨F11: historical → real-time⟩ | ⟨ready now / blocked on C15-1⟩ | ⟨name⟩ | `od-data-availability-check` |
| ⟨…⟩ | | | |

## 6 · Total evaluation score

**Paste the script's "Total evaluation score" block here, unedited — this is the number
the verdict rests on, not a restatement of it.**

| Component | Score | What moves it |
|---|---|---|
| Case-fit confidence | ⟨n⟩ / 40 | Best case-ranking match — higher is a more de-risked shape |
| Driver-justified targets | ⟨n⟩ / 30 | Share of set targets that land on a driver-justified candidate area |
| Gap feasibility | ⟨n⟩ / 30 | Share of gaps that are ready now or fully sequenceable within this plan |
| **Total** | **⟨n⟩ / 100** | |

## 7 · Verdict and next step

⟨Ready to build → `bc-build` · Needs a capability raised first → name the gap
owner and hand off per §5 · Over-engineered → lower the target or name the missing
justification · Escalate → `od-decision-routing`⟩

---

## Worked example (ready to copy the shape, not the numbers)

```text
=== Illustrative: predictive quality alert, <line> ===

-- Step 0+2: candidate focus areas (from drivers rated high/dominant) --
  F11  Degree of data collection           <- a14, a23
  F13  Point of information processing     <- a14, a23
  F14  Data analytics                      <- a23
  F3   Degree of intelligence              <- a14

-- Step 0: case ranking (pre-evaluation, top 5 of 70 literature cases) --
  case 11 Forstner and Dummler (2014)      [####################] 100.0%
  case 24 Kassner and Mitschang (2015)     [####################] 100.0%
  case 45 Regulin et al. (2014)            [####################] 100.0%
  case  2 Binder and Post (2012)           [###################_]  93.3%
  case 19 Herterich et al. (2015)          [###################_]  93.3%

-- Steps 3-4: gap per focus area --
  F11  Degree of data collection           2 historical       -> 3 real-time              [ready now]
  F13  Point of information processing     2 outsourced       -> 3 combined               [ready now]
  F14  Data analytics                      2 descriptive      -> 4 predictive             [ready now]
  F16  Continuity of the information model 1 no continuity    -> 2 partly continuous      [ready now]
  F3   Degree of intelligence              2 data handling    -> 3 information recognition [blocked on C2-3]
  OVER-ENGINEERED: target set with no rated driver behind it -> F16

-- Total evaluation score --
  Case-fit confidence:         40 / 40  (best match 100%)
  Driver-justified targets:    24 / 30
  Gap feasibility:             24 / 30
  TOTAL                        88 / 100

VERDICT: NEEDS A CAPABILITY RAISED FIRST
```

Reading this one: three close literature matches at 100% say the *shape* is well
understood — four of five targets are driver-justified, but F16 was set without a rated
driver behind it (fix: either rate the information-flow driver that actually justifies it,
or drop the F16 target). F3's gap is blocked on F2 reaching "active" first — that is the
named capability raise, handed to whichever skill owns F2/F9 in this registry, before this
use case's business case is calculated.
