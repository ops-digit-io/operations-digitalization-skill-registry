---
type: Skill Asset
title: Business case backbone
description: "The department's business-case backbone template (value only), condensed: header, inputs inventory A-L, before/after process, lever register, contribution matrix, de-banked levers, gated value realization, scaling, assumptions, open questions."
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [business-case, template, department-standard]
derived_from:
  - "Work vault, OD Department Knowledge/OD-instance/Business-Cases/_template/business-case-template.md, read 2026-11-10 (condensed; the vault file is the master)"
generated: { by: claude-code/1, at: 2026-11-10T00:00:00Z }
---
# Business Case — ⟨case name⟩

> Value only. Cost lives in the investment estimate (`bc-cost`) and is never netted into
> this headline. Tag every figure `[input]`, `[assumption]`, `[market]` or `[unknown]`. Leave what is
> not known as ⟨…⟩.

| Field | Value |
|---|---|
| Case ID | ⟨slug⟩ |
| Status | ⟨idea / drafting / in-review / validated / decided⟩ |
| Owner · contributors | ⟨…⟩ |
| Baseline | ⟨representative plant, not the best-case site⟩ |
| Headline | ~ EXPECTED ⟨EUR⟩ / plant / yr (min ⟨floor⟩ / potential ⟨upside⟩) |
| Future potential | rollout across ⟨N⟩ sites (illustrative, never in the headline) |
| Bankable vs assumption-dependent | ⟨which levers are bankable; which depend on assumptions⟩ |
| Investment envelope | ⟨max one-time spend that still pays back⟩ |
| Min viable rollout · max scale-out | ⟨…⟩ · ⟨…⟩ |
| Investment estimate | ⟨link to the bc-cost estimate⟩ |
| Overall confidence | ⟨low / medium / high⟩ |
| Last updated | ⟨YYYY-MM-DD⟩ |

## 1. Summary
⟨problem, change, value; lead with the grounded number, name the upside separately⟩

## 2. Inputs inventory
A identity · B current state · C volume and scaling drivers · D pain quantification · E target state ·
F operating model · G hard vs optional · H transferability · I baseline · J sources and confidence per
figure · K cost pointer · L completeness and maturity gate.

## 3. Process before / after
```
BEFORE: ⟨step⟩ → ⟨step (loss)⟩ → …
AFTER:  ⟨step (H1)⟩ → ⟨step (O1, not banked)⟩ → …
```

## 4. Lever register and contribution matrix
| ID | Lever | Formula (value × driver) | Drivers | Conservative | Base | Optimistic | Confidence and why |
|---|---|---|---|---|---|---|---|
| H1 | ⟨…⟩ | ⟨…⟩ | ⟨…⟩ | ⟨…⟩ | ⟨…⟩ | ⟨…⟩ | ⟨…⟩ |
| O1 | ⟨…⟩ | ⟨…⟩ | ⟨…⟩ | not banked | not banked | ⟨range⟩ | ⟨missing input⟩ |

Hard subtotal and optional levers are never summed into one headline.

## 5. Value realization gates
| Gate | Milestone | Owner | Date | Value unlocked | Make-or-break condition |
|---|---|---|---|---|---|
| G0 | ⟨baseline measured⟩ | ⟨…⟩ | ⟨set after approval⟩ | enabling | ⟨…⟩ |

## 6. Scaling
⟨first implementation (signed) · full rollout ceiling (future potential)⟩

## 7. Assumptions
| Assumption | Tag | Source | Confidence | Easy to prove? |
|---|---|---|---|---|

## 8. Open questions (ranked)
| Rank | Influence (0-100) | Block | Question | Best answer now | Easier proxy |
|---|---|---|---|---|---|

## 9. Assessment verdict
⟨maturity-gate verdict, recommend only; who signs⟩

## 10. Changelog
| Date | Who | Change |
|---|---|---|
