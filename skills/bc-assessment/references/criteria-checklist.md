---
type: Skill Reference
title: Criteria checklist
description: "The scored rubric: core integrity C1-C5 (a gap blocks signing), deck-renderable structure D1-D8, discipline E; pass / partial / gap with evidence."
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [business-case, assessment, department-package]
derived_from:
  - "Department knowledge base, read 2026-11-10"
generated: { by: claude-code/1, at: 2026-11-10T00:00:00Z }
---
> Transcribed from the department package `bc-assessment.zip/reference/criteria-checklist.md` (the master).

# Criteria checklist — the scored rubric

This is what "assess the business case" means. Go criterion by criterion. For each, record a
verdict — **pass / partial / gap** — with the evidence (file + section/line) and a one-line
note. A `gap` on any C1–C5 criterion means the case is **not ready to sign** (maturity gate).
Criteria are grouped: C = core integrity, D = deck-renderable structure, E = discipline.

Score each criterion `pass` (fully met), `partial` (present but incomplete/mislabelled), or
`gap` (missing or violated). Report as a table `Criterion | Verdict | Evidence | Note`.

## C — Core integrity (a gap here blocks signing)

- **C1 Value-only separation.** The backbone headline is value only; cost/effort lives in a
  separate `investment-estimate.md` and is never silently netted into the headline. *Pass* = cost
  is out; *gap* = a euro figure already nets cost.
- **C2 Grounding tags on every figure.** Every number carries `[input] / [assumption] /
  [market] / [unknown]`. No bare figures. *Gap* = any material figure untagged.
- **C3 Expected vs potential kept apart.** Headline = `~ EXPECTED <€> (min <floor> /
  potential ~<upside>)`. The grounded hard subtotal is the *expected*; any high-impact/
  low-confidence lever is *potential*, never summed in.
- **C4 De-banking applied.** Any big-mover lever resting on a crucial `[unknown]` is shown as a
  **sensitivity range only, labelled not banked**, never summed into the headline, and converted
  into the single highest-value open question. *Gap* = a confident figure printed for a lever
  whose crucial input is missing.
- **C5 Auditable arithmetic.** Each lever is `value × driver`, reproducible by hand; the hard
  floor derivation is shown (e.g. `min saved × lines × shifts × days = h/yr × €/h`). *Gap* =
  a lump sum nobody can re-derive.

## D — Deck-renderable structure (needed to render the standard deck)

- **D1 Lever register.** Every € contribution has a stable ID (H1, H2… hard; O1, O2… optional)
  with a one-line definition. Bundles split illustratively are **labelled illustrative**.
- **D2 Contribution matrix.** A lever × scenario (min | expected | max) matrix with a confidence
  per lever, a hard subtotal, and the counted/uncounted split. This is slide 3.
- **D3 Sub-business-case split + effort.** The case decomposes into sub-cases (e.g. Admin floor /
  Reaction / Rollout / Soft) each with its own value, status (banked/not banked/potential), and a
  qualitative *effort/dependency to realize* (not build hours). This is slide 2.
- **D4 Value vs. dependencies.** A 2×2 of "likeliness value lands" × "how many dependencies must
  line up" — confidence-in-achievement, distinct from confidence in the euro (D2). Slide 4.
- **D5 Abstracted before/after.** A condensed before/after (2 lanes) marking **only the steps
  that change**, each pinned to the lever it creates. Full BPMN stays in backbone §2A. Slide 5.
- **D6 SMART gated milestones.** M0–M4 gates, each specific + measurable, marking the gate at
  which each lever's € unlocks; dates left as `⟨set after approval⟩`. Slide 6.
- **D7 Soft/strategic clusters.** Kept qualitative on purpose (not forced into the number);
  sizeable operational ones (availability, scrap, reporting) live in the register as O2–O4. Slide 7.
- **D8 Ranked refinement questions.** Open questions ranked by €-influence, grouped by block,
  each led by a worked example that makes the answer easy to correct. Slide 8.
- **D9 Overall picture slide.** One C-level slide: headline band + key assumptions + savings +
  further/soft potential, with the grounding-tag legend. Slide 1.

## E — Discipline & house conventions

- **E1 Factual language.** No AI-slop words ("swing", vague intensifiers). A wide range is
  described factually ("wide range: near-zero to substantial") and flagged with brand-red
  (Melon-dark `F37558`) — the red marks *wide uncertainty*, not a value judgment.
- **E2 Tilde convention.** Estimated euro figures carry leading `~EUR` (no space). Defined rates
  (`EUR 40/h`, `EUR 250/machine-h`), discrete options (`EUR 100 / 250 / 500`) and exact zero
  (`EUR 0`) stay literal. Positive adds use `+~EUR X`. Table register cells stay bare under a
  "EUR k / yr" unit header. No stray "yet" fragments ("not quantified", not "not yet quantified").
- **E3 Market-based rule.** Where an input was not provided, carry a market/standard value tagged
  `[market]`, clearly flagged, added to open items — never left blank, never blocks the case.
- **E4 Baseline honesty.** Baseline = a representative paper/whiteboard plant, not a best-case
  site; already-digital sites credited only for the remaining delta.
- **E5 Scaling separation.** Per-plant value (the signed unit) and rollout scope kept on separate
  axes; full-rollout ceiling stated as *future potential*, never merged into the headline.
- **E6 Neuwerk brand.** Poppins + Navy/White equal weight; Sun ≤10–15% (only title rule + logo);
  semantic colours (Melon=problem/not-banked, Mint=solution/banked, Blue=neutral, Azure=cross-plant);
  no white text on light tints; no decorative bars/stripes. See `build-engine.md`.

## Maturity gate (report verdict)

State one of: **Ready to sign** (all C1–C5 pass; expected floor is grounded) · **Sign the floor,
validate the upside** (C-criteria pass but a de-banked lever awaits its input) · **Not ready**
(any C-gap; name the missing input and its owner). Cross-reference the ranked open questions (D8)
so the reader knows what to answer first.
