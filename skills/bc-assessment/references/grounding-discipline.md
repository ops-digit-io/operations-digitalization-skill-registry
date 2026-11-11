---
type: Skill Reference
title: Grounding discipline
description: "The four grounding tags and how each figure earns one; what counts as input, assumption, market and unknown."
resource: ../SKILL.md
status: draft
tags: [business-case, assessment, department-package]
---
> Transcribed from the department package `bc-assessment.zip/reference/grounding-discipline.md` (the master).

# Grounding discipline, de-banking, and house conventions

## Grounding tags (every figure carries one)

- **[input]** — stated in the source material (interview, mockup/clickdummy, document). A fact.
- **[assumption]** — our estimate, not in the sources. Defensible but ours to own.
- **[market]** — a market/standard value used *because none was provided*. Clearly flagged,
  added to open items to firm later. Never left blank, never blocks the case.
- **[unknown]** — a crucial missing input we refuse to fake. Drives the de-banking rule.

Small immaterial uncertainties are fine to assume. Big-but-undependable upside is treated
qualitatively (a soft cluster) or ring-fenced as a sensitivity — not forced into a number.

## The five discipline rules

1. **Never state as fact what is not in the inputs.** Tag it, or don't print it as a number.
2. **Lead with the high-confidence number.** The headline is the grounded hard subtotal; name
   the upside separately as *potential*.
3. **Keep value and cost apart.** The BC is value-only; cost lives in the investment file and is
   never silently netted in.
4. **De-bank high-impact/low-confidence levers** (see below) rather than printing a confident
   figure for something that rests on a guess.
5. **Make every driver SMART and sourceable.** Decompose to numbers an area owner or Controlling
   can actually supply (machines in the area, € per machine-hour, minutes per line) — not an
   abstract lump. A driver you can't ask a plant for is a driver you can't sign.

## De-banking rule (high impact + low confidence → do NOT print a banked number)

If a lever is a big mover but rests on a crucial **[unknown]** input:

- Show it as a **sensitivity range only**, labelled **not banked**.
- **Never** sum it into the headline. The case is signed on the *expected* = grounded hard subtotal.
- Convert it into the single **highest-value open question**, and name the exact missing input
  that would move it.
- Record, per lever, *why* its confidence is high/mid/low.

In the Gemba example this is lever **O1** (reaction-time idle hours): shown as `~EUR ⟨low⟩–⟨high⟩k`
sensitivity, not banked, because the crucial idle-hours-per-machine input is `[unknown]`.

## Factual-language rule (E1)

- No AI-slop words. "**swing**" is banned; so are vague intensifiers dressed up as precision.
- A wide range is described **factually** — e.g. *"wide range: near-zero to substantial"* — and
  flagged with **brand-red = Melon-dark `F37558`**. The red marks *wide uncertainty*, not a
  value judgment and not a warning of something bad.
- Titles/headings: sentence case, no terminal full stop, plain nouns over slogans.

## Tilde convention (E2)

- **Estimated** euro figures carry a leading `~EUR` with **no space**: `~EUR ⟨X⟩k`, `~EUR ⟨low⟩-⟨high⟩k`.
- **Defined rates** stay literal: `EUR 40/h`, `EUR 250/machine-h`.
- **Discrete options** stay literal: `EUR 100 / 250 / 500`.
- **Exact zero** stays literal: `EUR 0`.
- **Positive adds** use `+~EUR X`: `+~EUR ⟨X⟩k`.
- **Table register cells** stay bare numbers under a `EUR k / yr` unit header (e.g. `22|25|27`).
- **No "yet" fragments.** Write "not quantified", "not in the equation" — never "not yet
  quantified" ("yet" fragments the read without adding meaning).
- Apply the convention **consistently on every slide** — inconsistency is itself a gap (E2).
