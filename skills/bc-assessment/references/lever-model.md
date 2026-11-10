---
type: Skill Reference
title: Lever model
description: "Lever register (H hard / O optional IDs), formulas and drivers, contribution matrix min|exp|max, de-banking of low-confidence levers."
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [business-case, assessment, department-package]
derived_from:
  - "Work vault, OD Department Knowledge/OD-instance/30-skills/bc-assessment.zip/reference/lever-model.md, read 2026-11-10"
generated: { by: claude-code/1, at: 2026-11-10T00:00:00Z }
---
> Transcribed from the department package `bc-assessment.zip/reference/lever-model.md` (the master).

# Value model — levers, matrix, headline, scaling

The BC is **value-only** and built bottom-up from **one plant** (the first implementation area).
Two levels are always kept separate and **never summed into one headline**.

## Lever register (D1)

Give every € contribution a stable ID and a one-line definition:

- **H1, H2, H3…** — hard levers: high-confidence, employee-independent, banked into the floor.
- **O1, O2, O3…** — optional/perspective levers: lower-confidence; validate before banking.

Keep them in a small register table (ID | lever | formula | drivers | €/plant/yr | confidence).
Where a real lever is a bundle you can't yet split by measurement, allocate it **illustratively**
across sub-IDs and **label the split illustrative** — the combined figure stays the defensible
one; the split just makes each part referenceable. Add the split as an open/proxy question.

Gemba example register:
- H1 Hourly KPI entry → one-tap/MES capture · H2 shift-end board → Excel transcription ·
  H3 issue write-up → auto-recorded once. Hard subtotal ≈ `~EUR 25k` (min 22 / max 27), split
  illustratively H1 ~60% / H2 ~32% / H3 ~8%.
- O1 reaction-time idle hours (de-banked, `~EUR 5–56k`, not banked) · O2 availability/repeat
  stops · O3 quality/scrap · O4 management reporting / KPI consolidation (input-grounded but
  uncounted — a candidate second hard lever).

## Contribution matrix (D2)

A lever × scenario matrix: rows = each lever + hard subtotal + total; columns = min | expected |
max; a confidence per lever. Reading down a column gives a scenario total; reading across a row
shows how much each lever moves the total. Counted lines carry euros and sum into the floor;
uncounted lines (O2–O4) carry a qualitative potential chip (HIGH/MED/LOW), never a summed figure;
the de-banked O1 shows a ring-fenced sensitivity in parentheses, never summed.

## Headline format (C3)

```
~ EXPECTED <€> / plant / yr   (min <€ floor> / potential ~<€ upside>)
```

*Expected* = grounded, bankable hard subtotal. *Potential* adds the de-banked lever's upside,
explicitly **not banked**. Full-rollout ceiling (per-plant × N sites) is stated separately as
**future potential**, never merged in.

## SMART, sourceable drivers (rule 5)

Decompose to numbers a plant can actually supply, using **averages for the first implementation
area**: machines in the area, € per machine-hour, hours lost per machine, minutes per line,
entries per shift, shifts/day, operating days/yr, loaded labour rate. Avoid abstract aggregates
(a lump "downtime cost/hour"). The hard floor must be reproducible by hand, e.g.:

```
9.4 min saved × 6 lines × 3 shifts × 220 days = 618 h/yr × EUR 40/h ≈ ~EUR 25k
O1 range = machines × avoidable idle h/machine × EUR 250/machine-h
```

## Cost envelope (scenarios)

On the value side, express affordability as a **cost envelope** = the one-time spend that still
pays back within 12 months at that scenario's annual value. When a real cost is known (from the
investment file), the envelope becomes a payback. Costs stay out of the headline on purpose.

## Scaling & transferability (E4, E5)

- **Saving factor = one plant**, built bottom-up from the first area's averages.
- Keep two axes separate: per-plant value tiers vs. rollout scope.
- **Lead with the first implementation** (one pilot plant/area) as the signed primary case.
- State **full rollout to all sites** as the optimistic ceiling = per-plant × ⟨N sites⟩
  (source: MI-Machine List / plant register), **explicitly future potential, never merged in**.
- **Baseline** = representative paper/whiteboard plant; already-digital sites (e.g. Timișoara)
  credited only for the remaining delta.

## Additional impact clusters (brainstorm before finalizing)

Probe clusters beyond the counted levers so nothing material is missed: reporting/consolidation,
quality/scrap, availability/repeat-stops, handover losses, cross-site learning, audit/compliance,
safety, onboarding/language, employee experience, platform/option value. Keep them out of the
headline until quantified; promote any that prove to be real hard levers into the register.
