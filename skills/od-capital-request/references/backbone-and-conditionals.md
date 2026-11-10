---
type: Skill Reference
title: Backbone and conditionals
description: "The eCR backbone in layered markdown and the conditional rules (GPA vs non-GPA, when sensitivity is mandatory) that decide which sections apply."
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [capital-request, ecr, department-package]
derived_from:
  - "Work vault, OD Department Knowledge/OD-instance/30-skills/ecr-builder.zip/reference/backbone-and-conditionals.md, read 2026-11-10"
generated: { by: claude-code/1, at: 2026-11-10T00:00:00Z }
---
> Transcribed from the department package `ecr-builder.zip/reference/backbone-and-conditionals.md` (the master).

# eCR backbone, layered-markdown format, and conditional rules

## The section backbone (convention, not law)

The OESL / ContiTech eCR **Management Summary** follows this sequence. Numbering is
a *convention* — real teams reorder (e.g. promote P&L from Backup into the body, or
move Key Figures late). Keep the reader's logic intact; don't renumber for its own
sake.

1. **Executive summary** — What / Why / How, plus a data rail carrying the headline
   financials: Request Type, Investment Class, Request amount (GPA / non-GPA / Total,
   kEUR), NPV / IRR / payback / RoS (and IIR if Right-of-Use), scope, PCIS ref.
   *The headline financials belong here, not buried later — this is the most common
   real-world weakness.*
2. **Project description** — 2a current situation, 2b planned situation.
3. **Investment data** — capex split GPA (globally pooled assets) vs non-GPA / RPE
   (regional plant equipment).
4. **Additional details / assumptions** — 4a volume, capacity & utilization;
   4b savings; 4c price / cost development.
5. **Key figures of the financial analysis** — 5a sensitivity calculation.
6. **Risks & opportunities** — a *rated table*, not free text:
   `item | actions | level (High/Med/Low, colour-coded) | sensitivity/upside case`.
7. **Alternative solutions** — options evaluated, one selected, why.
8. **Plant / production layout** — *if applicable*.
9. **Project timeline** — milestones from approval to SOP.
- **Backup** — customer/PCIS, P&L and cash-flow statement, CT Engineering Checklist,
  **Open items & conflicts** (this skill's final slide), Glossary, growth/value field.

## The layered-markdown backbone you compile (step 3)

Mirror `eCR_Management_Summary_inventory.md` in the OD-instance root. Produce
`eCR_<slug>_backbone.md` with three layers so the deck build is mechanical:

**Layer 1 — section & process map.** One block per eCR section: is it present in the
material, which source(s) feed it, and which conditional rules fire (below).

**Layer 2 — per-slide intent.** For each slide: the message in one sentence, and the
2–4 facts/figures it will show.

**Layer 3 — field-level values with grounding tags.** Every figure as
`value [tag] — source`. Example:

```
### 3) Investment data
- Spiral-crimping machine | 145 kEUR [input] — supplier quote Q-2025-118.pdf
- Tooling & fixtures       | 44 kEUR [a]   — our estimate, no quote yet
- Total capital request    | 398 kEUR [input] — sum of quotes + [a]
Conditional: GPA/non-GPA split present → yes (GPA 332 / non-GPA 66)
```

Tags: `[input]` grounded · `[a]` assumption · `[m]` market/standard · `[?]`
low-confidence/unknown. This layer maps 1:1 onto the `CASE`/slide-assembly code in
`../scripts/build_ecr.py` — the chip on the slide is just the tag made visible.

## Governance conditional rules (confirmed against a real filled deck)

- **Sensitivity (5a) is mandatory only for projects > EUR 1M *or* realization
  > 24 months.** Below both thresholds, state plainly that it is not required
  (optionally add a voluntary robustness check) — do not fabricate a sensitivity.
- **Investment class = Expansion → the growth / value field applies.**
- **Right-of-Use asset → report IIR** on the financial rail.
- **Plant/production layout, PCIS reference, and the growth/value field are
  "if applicable"** — omit cleanly rather than padding.
- **Terminology varies by plant:** the capex split may appear as GPA / RPE (+ "Non
  ICO"); RPE ≈ the template's "non-GPA". Define every acronym in the Glossary
  (GPA, RPE, ICO, SNL, SOP, PCIS, PPAP, NPV, IRR, RoS, WACC, IIR).

## Real-world weaknesses to coach against (build the deck so these can't happen)

- Exec summary that omits the headline financials → put them on the data rail.
- Risks/opportunities as free bullet text → use the rated, colour-coded table.
- Over-dense PN/investment tables at unreadable font → group, summarise, move detail
  to Backup.
- Inconsistent chrome (ContiTech vs Continental, mixed date formats/authors,
  off-by-one section numbers) → one consistent footer/title system throughout.
- Undefined acronyms → Glossary slide.
