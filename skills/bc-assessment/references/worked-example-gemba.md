---
type: Skill Reference
title: Worked example gemba
description: "A complete assessment run with the rubric: the Gemba app case scored C1-C5, D1-D8 and E with evidence, the maturity-gate verdict and the ranked open questions."
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [business-case, worked-example, department-package]
derived_from:
  - "Work vault, OD Department Knowledge/OD-instance/30-skills/../Business-Cases/gemba-app/bc-assessment-report.md, read 2026-11-10"
generated: { by: claude-code/1, at: 2026-11-10T00:00:00Z }
---
> Transcribed from the department package `../Business-Cases/gemba-app/bc-assessment-report.md` (the master). Money figures in examples are masked as ⟨€⟩.

# BC Assessment Report — Gemba App

**Case:** Gemba App — digital shopfloor Gemba management (Levels 1–3 + walk)
**Assessed against:** `30-skills` → `bc-assessment` rubric (`criteria-checklist.md`)
**Backbone:** `Business-Cases/gemba-app/business-case.md`
**Inputs reviewed:** `inputs/gemba-alignment-transcript.md`, `inputs/gemba-management.html` (mockup),
`inputs/gemba-app-business-case-REFERENCE.md`, `inputs/interview-cross-check.md`
**Deck rendered:** `bc-gemba-onepager-neuwerk.pptx` (10 slides: 9 + provenance backup)
**Date:** 2026-09-08

---

## 1. Maturity-gate verdict

**Sign the floor, validate the upside.** All core-integrity criteria (C1–C5) pass: the case is
value-only, every figure is grounded-tagged, the expected/potential split is clean, the reaction
lever is correctly de-banked, and the hard-floor arithmetic is reproducible. The case can be
signed on the **expected ⟨€⟩ / plant / yr hard floor** now. It is **not yet a fully signed
number** because every magnitude rests on `[assumption]`/`[market]` inputs — the interview
contained zero quantities. One short quantitative round at a paper/whiteboard plant closes it.

---

## 2. Criteria scorecard

| Criterion | Verdict | Evidence | Note |
|---|---|---|---|
| C1 Value-only separation | pass | backbone header + `investment-estimate.md` | Cost kept out of the headline. |
| C2 Grounding tags on every figure | pass | §3, §6; slide-1 legend | `[input]/[assumption]/[market]/[unknown]` throughout. |
| C3 Expected vs potential apart | pass | headline `~EXPECTED ⟨X⟩k (min ⟨min⟩ / potential ~⟨max⟩)` | Potential never summed in. |
| C4 De-banking applied | pass | O1 `⟨€⟩`, not banked | Rests on `[unknown]` idle-hours; = top open question. |
| C5 Auditable arithmetic | pass | slide-3 callout: `9.4 min × 6 × 3 × 220 = 618 h × ⟨€⟩` | Re-derivable by hand. |
| D1 Lever register | pass | §3 H1–H3 / O1–O4 | H1/H2/H3 split labelled illustrative. |
| D2 Contribution matrix | pass | slide 3 | min\|exp\|max + confidence + counted/uncounted split. |
| D3 Sub-cases + effort | pass | slide 2 (F/R/S/Soft) | Status + qualitative effort chips. |
| D4 Value vs. dependencies | pass | slide 4 | Achievement axis, distinct from euro confidence. |
| D5 Abstracted before/after | pass | slide 5; full BPMN in §2A | Only the 3 changing steps marked. |
| D6 SMART gated milestones | pass | slide 6 (M0–M4) | Dates `⟨set after approval⟩`; € unlock marked. |
| D7 Soft/strategic clusters | pass | slide 7 | Kept qualitative; O2–O4 sized in register. |
| D8 Ranked refinement questions | pass | slide 8; §8A | Worked examples; ranked by €-influence. |
| D9 Overall-picture slide | pass | slide 1 | C-level headline + assumptions + potential + legend. |
| E1 Factual language | pass | slide 2 R row | "swing" removed; wide range flagged brand-red `F37558`. |
| E2 Tilde convention | pass | all slides | `~EUR` estimates; literal rates; no "yet" fragments. |
| E3 Market-based rule | pass | §6; ⟨€⟩/h, ⟨€⟩/machine-h `[market]` | Flagged, in open items. |
| E4 Baseline honesty | pass | backbone Baseline field | Representative paper/whiteboard plant. |
| E5 Scaling separation | pass | §5; slide-1 potential panel | Rollout ceiling = future potential only. |
| E6 Neuwerk brand | pass | visual QA all 10 slides | Sun ≤10–15%; no white-on-light; no stripes. |

**No gaps.** All C-criteria pass; the only reason the number is not "fully signed" is the pending
quantitative round (see §4), which is the maturity gate working as intended, not a defect.

---

## 3. Provenance & conflict register

**Provenance — what fed the case.**

| Input file | Contributed to the BC | Dominant grounding tag |
|---|---|---|
| `gemba-alignment-transcript.md` | Current-state process, media breaks, sweep cadence, operating model | `[input]` (structure) |
| `gemba-management.html` (mockup) | Target-state capabilities; pins each lever to a process step | `[input]` (structure) |
| `gemba-app-business-case-REFERENCE.md` | Earlier lever set + formulas (superseded — see conflicts) | `[assumption]` |
| `interview-cross-check.md` | Gap flags: no quantities, baseline open, single-source bias | caveat |
| `business-case.md` (backbone) | Final levers H1–H3 / O1–O4, headline, grounding tags | source of truth |

**Conflicts — thesis/assumption disagreements and how each flowed into the BC.**

| # | Conflict | Sources | Resolution in the BC | Residual |
|---|---|---|---|---|
| 1 | Hard-lever count H1–H4 vs H1–H3 | REFERENCE vs backbone | H4 Gemba-walk doc de-scoped from the banked floor to soft clusters (slide 7) | not banked |
| 2 | Reaction O1 formula: `latency×events×cost` vs `machines×idle-h×€/machine-h` | REFERENCE vs backbone | Adopted machine-based, sourceable form; crucial idle-h stays `[unknown]` → O1 de-banked `⟨€⟩` | de-banked |
| 3 | "4 min" per entry — floated in an earlier session, in no source | prior session vs sources | Deliberately not enshrined; admin time derived from the 1–2 h sweep cadence | `[assumption]` |
| 4 | Baseline asked in interview (13:31–14:15) but left unanswered | transcript | Analyst-set to a representative paper/whiteboard plant; carried as the top open question | `[assumption]` |
| 5 | Interview holds zero quantities; single source (Adrian, 2026-09-02) + some leading questions | transcript + cross-check | Every euro tagged `[assumption]`/`[market]`; structure is `[input]`; case signed on logic, sized after one data round | maturity gate |
| 6 | Management reporting / KPI consolidation described but uncounted | mockup + interview | Kept `[input]`-grounded but out of the floor (O4, HIGH chip) — the candidate 2nd hard lever | uncounted |

All conflicts were resolved toward the more sourceable, lower-risk option, and quarantined (not
banked) wherever a crucial input is still missing.

---

## 4. Prioritized gaps to close the number

Ranked by €-influence (mirrors backbone §8A and slide 8):

1. **Idle hours per machine per year waiting for a reaction (R / O1)** — the single biggest mover;
   moves O1 across `⟨€⟩`. Currently `[unknown]`. Owner: area supervisor / OPEX.
2. **Go-live gate: board off or run in parallel? (G)** — if the paper board is kept in parallel,
   the admin floor never banks (⟨€⟩). Owner: plant lead.
3. **Admin minutes per line/shift on board + shift-end Excel (F)** — sets the hard-floor size;
   each +1 min ≈ +⟨€⟩/yr. Owner: line supervisor.
4. **Machines/lines in the first implementation area (S)** — the per-plant multiplier. Source:
   MI-Machine List.
5. **Cost of one idle machine-hour (⟨€⟩/ 250 / 500)** — scales O1. Owner: Controlling.

One short data round at a representative paper/whiteboard plant, plus `L` from the MI-Machine List,
closes items 1–5 and turns the expected floor into a fully signed figure.
