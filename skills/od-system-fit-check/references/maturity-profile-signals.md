---
type: Skill Reference
title: Maturity profile signals
description: Which levels of the IT/OT maturity model on a requested or existing system act as fit-check signals - MES-shaped need, edge need, reporting-before-AI order, integration cost - and how to cite them without turning them into a verdict.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [practice, system-fit, maturity, draft]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Maturity profile signals for the fit check

Source layer: the IT/OT maturity model (focus areas F1 to F16) summarised in `od-use-case-solution-evaluation`. Everything here is `PROPOSAL`
(this registry's synthesis, `<to confirm>` with the OD lead); the boundary sentences in `tool-boundaries.md` remain the fit test. The profile
is evidence next to the boundary line, never a replacement for it.

## When to ask for a profile

Run `od-use-case-solution-evaluation` on the requested or existing system when the boundary walk is inconclusive, when the plant already runs a parallel
system (`legacy-applications-landscape.md`), or when the cost class of "integrate" is in question. Skip it when one boundary line settles the need.

## Signals

| Observation (area, level) | Reads as | Use in the check |
|---|---|---|
| The asked function is order or recipe execution, sequencing, genealogy or material validation (F15 central control; F1 per-instance records) | MES-shaped need | Step 2: cross the MES line and quote it; this is the "none of the lightweight tools cover it" case |
| The need is real-time within the shift (F11 level 3) from a source at historical level | A data gap before a tool question | Return to requirements; route to `od-data-availability-check` |
| Traceability or high-rate demand and the source holds data only centrally (F12 level 2) | Data loss on outage | Edge rule of `process-chain-practice.md` applies; record it |
| An AI or prediction ask (F14 predictive or prescriptive) while the source is below descriptive reporting on a shared model (F14 level 2, F16 level 1) | Out of order | AI-above-reporting sanity check; redesign onto the basics |
| The existing system speaks a proprietary protocol and its names are not shared (F10 level 2, F16 level 1) | Integration is costly per interface | Do not recommend "just integrate"; hand to `od-system-fit-check` for integrate, keep or replace |
| No named business owner, IT owner and support level for the system | Service gap | Operations-concept precondition; the verdict cannot be "fits" |

## Rules

- A signal changes what you ask next, not the verdict. The verdict still follows the three outcomes of this skill and the human gate.
- Cite the area, the level, the evidence grade (seen, told, assumed) and the read date next to the boundary sentence. Assumed evidence opens a
  question only.
- The profile describes this plant's system, not the estate. Do not read one plant's profile into another (`deployment-reality.md`).
- Do not turn levels into a score or a ranking of systems.
