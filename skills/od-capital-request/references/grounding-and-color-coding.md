---
type: Skill Reference
title: Grounding and color coding
description: "The honesty layer: four grounding tags rendered as colour-coded chips (A amber, M blue, ? red) on every figure of the eCR deck."
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [capital-request, ecr, department-package]
derived_from:
  - "Work vault, OD Department Knowledge/OD-instance/30-skills/ecr-builder.zip/reference/grounding-and-color-coding.md, read 2026-11-10"
generated: { by: claude-code/1, at: 2026-11-10T00:00:00Z }
---
> Transcribed from the department package `ecr-builder.zip/reference/grounding-and-color-coding.md` (the master).

# Grounding tags, slide colour code, and challenge principles

This is the honesty layer. The rule it serves, verbatim:

> **Never invent information that you cannot derive from the material, a question
> back, or public web material. Mark low-confidence points.**

## The four grounding tags

Every figure carries exactly one tag. In the backbone markdown use the bracket
form; on the slide it becomes a coloured chip via `chip()` in `build_ecr.py`.

| Tag | Backbone | Chip | Colour | Means |
|-----|----------|------|--------|-------|
| grounded | `[input]` | none | Navy (plain text) | stated in a source; a fact |
| assumption | `[a]` | **A** | Peach `F8AF99` | our estimate, not in the sources; we own it |
| market/standard | `[m]` | **M** | Periwinkle `8793CA` | standard value used because none was given; firm later |
| low-confidence / unknown | `[?]` | **?** | Melon-dark `F37558` | crucial input we could not derive and refuse to fake |

Rules of use:
- **Grounded is the default and needs no chip.** Only deviations are marked, so the
  eye goes straight to what to question.
- **Lead with grounded numbers.** The exec-summary headline and any total should be
  built on grounded figures; name estimated upside separately as *potential*.
- **A wide/uncertain range is stated factually** ("near-zero to substantial"), not
  dressed up as precision, and flagged red. Red marks *uncertainty*, not "bad".
- **Estimated euro figures carry `~EUR`** with no space (`~EUR 0.44M`); defined
  rates stay literal (`EUR 250/machine-h`); exact zero stays `EUR 0`.
- **The legend appears once**, on the exec-summary slide (`tag_legend()`), so the
  deck isn't cluttered; individual chips carry the meaning elsewhere.

## Where chips go on the deck

- **Exec-summary data rail** — chip the request amount and the financial block if
  they rest on assumptions; show the full legend beneath the slide.
- **Any KPI, savings, volume or cost figure** that is `[a]`/`[m]`/`[?]` — a chip at
  the top-right of its card/box.
- **Never chip a grounded figure** — absence of a chip is information too.

## Challenge principles — what to interrogate before you trust the material

Before a number becomes `[input]`, challenge it. These are the questions that catch
a weak eCR before a reviewer does:

1. **Is this a fact or someone's hope?** A volume in a signed OEM call-off is
   `[input]`; the same volume in an internal ambition slide is `[a]`.
2. **Value vs cost kept apart?** Savings (value) and capex (cost) come from
   different files and must never be silently netted. Check the total isn't
   double-counting.
3. **Is the baseline real?** "We save X vs today" needs a defensible *today*. If the
   current-state cost is itself estimated, the saving inherits `[a]`.
4. **Single-source risk.** If one file is the only source for a big number, say so;
   don't launder a single estimate into a fact by restating it.
5. **Does it survive a sensitivity?** For any big value driver, ask what a 25% miss
   does to payback/NPV. If the case dies, the driver belongs in the sensitivity, not
   the headline.
6. **Rate/standard values** (duty %, WACC, FX, depreciation life) — if not given,
   use a defensible public/standard value, tag `[m]`, and list it as an open item.
   Public web material may be used *only* for such standard reference values, and it
   is still tagged `[m]`, never `[input]`.
7. **Thresholds & governance** — does the request cross EUR 1M / 24 months
   (sensitivity), is it Expansion (growth field), Right-of-Use (IIR)? A missing
   mandatory section is a gap, not a stylistic choice.

Anything you cannot resolve becomes either a `[m]` (standardised) or a `[?]`
(carried to the Open-items slide) — and if the `[?]` items are load-bearing, see the
refusal gate in `open-items-and-conflicts.md`.
