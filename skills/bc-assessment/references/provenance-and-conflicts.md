---
type: Skill Reference
title: Provenance and conflicts
description: "Provenance register and conflict log: every source listed, every conflict between sources resolved visibly with an owner."
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [business-case, assessment, department-package]
derived_from:
  - "Work vault, OD Department Knowledge/OD-instance/30-skills/bc-assessment.zip/reference/provenance-and-conflicts.md, read 2026-11-10"
generated: { by: claude-code/1, at: 2026-11-10T00:00:00Z }
---
> Transcribed from the department package `bc-assessment.zip/reference/provenance-and-conflicts.md` (the master).

# Provenance & conflict backup slide + conflict register

The backup slide (and the matching section of the QA report) makes the one-pager auditable: it
shows **which input files fed the business case, what each contributed, and where sources
conflicted** — and how each conflict was resolved into the final BC.

## How to build it

1. **List every input file** in `<case>/inputs/` plus the backbone. For each, one line: what
   info the BC drew from it, and the dominant grounding tag it produced.
2. **Annotate contributions.** For each material fact/figure in the BC, note the source file and
   part. Group by lever where possible.
3. **Flag every conflict** between theses/assumptions across sources — differing lever counts,
   changed formulas, a number in one draft not carried into the final, a leading/throwaway figure
   that was deliberately *not* enshrined, single-source risk.
4. **For each conflict, state the resolution**: which version the BC adopted, why, and the residual
   grounding tag (does it stay `[assumption]`, get promoted to `[input]`, or remain `[unknown]`?).

## Slide layout (appendix, slide 10)

Two columns. **Left = input inventory**: one card per source file (transcript, mockup/clickdummy,
reference draft, cross-check, backbone) with a one-line "contributed:" note and a grounding chip.
**Right = conflict register**: one row per conflict — `Conflict | Sources | Resolution in BC |
Residual tag`. Use Melon for conflicts, Mint where a conflict was cleanly resolved, Blue for
neutral provenance. Keep the Sun budget (title rule + logo only). Title e.g. *"Provenance &
conflicts — what fed the case, and how disagreements were resolved"*.

## Conflict register — the Gemba example (reference content)

Encode these when rendering the Gemba backup slide; regenerate for other cases.

- **Lever count H1–H4 vs H1–H3.** The reference draft (`gemba-app-business-case-REFERENCE.md`)
  used four hard levers, including **H4 = Gemba-walk documentation**. The final backbone uses
  **H1–H3**; walk-documentation/handover value moved to the soft clusters (slide 7). *Resolution:*
  H4 de-scoped from the banked floor to keep the floor to the three highest-confidence admin
  levers; walk value carried qualitatively. Residual: `[assumption]`, not banked.

- **Reaction (O1) formula changed.** REFERENCE O1 = `Δlatency(h) × downtime_cost(€/h) ×
  events/yr × p_avoidable`. Final backbone O1 = `machines × avoidable idle h/machine ×
  EUR 250/machine-h` — a machine-based, more sourceable driver. *Resolution:* adopted the
  machine-based form (SMART/sourceable rule); the crucial idle-hours input stays `[unknown]`,
  so O1 is de-banked as a `~EUR ⟨low⟩–⟨high⟩k` sensitivity.

- **"4 min" throwaway not enshrined.** An earlier session floated "4 min" per entry; it appears
  in **neither** the transcript nor the mockup. *Resolution:* deliberately **not** used; the admin
  time was derived from the supervisor sweep cadence (every 1–2 h → ~30 min-equivalent bundled
  admin) and tagged `[assumption]`, not `[input]`.

- **Baseline asked-but-unanswered.** In the transcript (13:31–14:15) the OD lead asked the baseline
  quantification question; it was left unresolved. *Resolution:* analyst-set baseline = a
  representative paper/whiteboard plant (E4), tagged `[assumption]`; the open question is carried
  as the top item to close.

- **All magnitudes are [assumption]/[market].** The interview contained **zero quantities**
  (times, frequencies, counts, rate). *Resolution:* every euro is `[assumption]` or `[market]`;
  the *structure/logic* is `[input]` from the mockup + interview. This is the maturity gate working
  as intended, not a failure — the case is signed on structure, sized after one data round.

- **Single-source / confirmation-bias caveat.** The interview is one source (Adrian Dreava,
  2026-09-02) with some leading questions. *Resolution:* `[input]` tags carry a single-source
  caveat; cross-check flags recorded in `interview-cross-check.md`.

- **Management reporting input-grounded but uncounted.** KPI consolidation / management reporting
  is described in the sources (so `[input]`-grounded) but left **uncounted** (O4, HIGH potential
  chip) — a candidate second hard lever. *Resolution:* kept out of the banked floor pending a
  quantification round; flagged as the biggest next case.

## In the QA report

Reproduce the conflict register as a markdown table, plus a provenance table
`Input file | Contributed to BC | Dominant grounding tag`. This is the written twin of the slide.
