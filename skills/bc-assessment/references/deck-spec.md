---
type: Skill Reference
title: Deck spec
description: "The standard business-case one-pager deck (9 slides plus provenance backup): slide by slide content rules."
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [business-case, assessment, department-package]
derived_from:
  - "Department knowledge base, read 2026-11-10"
generated: { by: claude-code/1, at: 2026-11-10T00:00:00Z }
---
> Transcribed from the department package `bc-assessment.zip/reference/deck-spec.md` (the master).

# Deck specification — the 9 slides + provenance backup

The standard BC one-pager is **cover + 8 content slides**, each with one purpose. Render with
`../scripts/build_bc_short.py` (see `build-engine.md`). Keep the sequence; adapt content to the case.
Append the provenance/conflict slide as the last (appendix) slide (see
`provenance-and-conflicts.md`).

## Sequence

- **Cover** — title + one lead line ("Value first, assumptions derived from the case, before/
  after in one view"). Layout 1; footers filled; the review stage in the date footer.

- **Slide 1 — The business case on one page (C-level).** A Navy headline band with the
  `~ EXPECTED … (min … / potential …)` figure, a one-line "expected vs potential" gloss, and a
  one-line verdict. Below: three panels — key assumptions (area averages, each tagged), savings
  (expected/min/max), further & soft potential. Footer legend = the four grounding tags. This is
  the only slide most executives read; it must stand alone.

- **Slide 2 — Sub-business cases + effort.** A 4-row matrix: each sub-case (e.g. F Admin floor /
  R Reaction / S Rollout / Soft) with value, a status chip (Banked / Not banked / Potential /
  Optional), a qualitative effort chip (LOW/MEDIUM/HIGH/VARIES) and the key dependency to realize.
  The de-banked row shows its value in **brand-red (`F37558`)** with the factual wide-range note.
  Effort = dependencies to realize, not build hours.

- **Slide 3 — Contribution register (every line, counted or not).** Bar spans min→max, bold tick
  = expected. Hard levers with euros → hard subtotal (BANKED) → de-banked O1 as a parenthetical
  sensitivity → uncounted O2–O4 with HIGH/MED/LOW potential chips. A Navy callout folds in the
  hard-floor arithmetic (kills the need for a separate numbers slide). *Note: the current deck has
  no separate confidence-map slide — confidence lives in this register's Confidence column.*

- **Slide 4 — Value vs. dependencies.** A 2×2: Y = likeliness the value lands (achievement),
  X = how many dependencies must line up. Distinct from confidence in the euro (slide 3). Bubbles
  for each sub-case; a "start here" detail box explaining why the floor lever is self-contained.

- **Slide 5 — Process, abstracted.** Two lanes (Today paper/whiteboard vs. With the app), three
  steps, numbered badges marking **only where it changes**, each pinned to the lever it creates
  (e.g. "no manual entry → H1+H2", "latency h→min → O1"). Full BPMN stays in backbone §2A.

- **Slide 6 — Milestones (SMART, gated).** M0–M4 cards, each specific + measurable, with a
  target row (`T + ⟨..⟩ wks`) and a value-unlocked tag; a € badge marks the gates where hard /
  reaction value comes online. Time-to-first-value called out. Dates `⟨set after approval⟩`.

- **Slide 7 — Soft & strategic stakes.** Two clusters (people/operating discipline; organisation/
  option value), kept qualitative on purpose. Note that sizeable operational levers (availability,
  scrap, reporting) live in the register as O2–O4, not here.

- **Slide 8 — Refinement, led by worked examples.** Blocks (R / F / S / G), each leading with a
  worked example that makes the answer easy to correct, then the proxy questions. Ranked by how
  much each moves the total. Answer a block, close a sub-case.

## Backup slide — Provenance & conflicts (appendix)

Append as slide 10. See `provenance-and-conflicts.md` for the full spec. In short: a left column
listing every input file with what the BC drew from it, and a right column = a conflict register
(thesis/assumption conflicts across sources, how each resolved into the BC, and the residual
grounding tag). This is the audit trail behind the one-pager.

## Brand discipline (applies to every slide)

Poppins; Navy/White equal weight; **Sun ≤10–15% — only the template title rule + logo**; semantic
colours (Melon=problem/not-banked, Mint=solution/banked, Blue=neutral, Azure=cross-plant);
no white text on light tints; no decorative bars/stripes; every slide has a visual; never below
8pt. Enforce the factual-language + tilde conventions (`grounding-discipline.md`) on every slide.
