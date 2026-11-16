---
type: Skill Reference
title: Background
description: Context, rationale, examples and notes that stood in SKILL.md, moved here unchanged. Open it for the why; it is never an instruction.
resource: ../SKILL.md
status: draft
tags: [background]
---
# Background

## The references are the substance

Output: `assets/portfolio-review-protocol.md` (`assets/portfolio-review-protocol.md`) — one
document per review round, built from `know-sharepoint-export`'s capture and
`bc-build`'s ledger, feeding `metrics-scorecard`'s round prep.

## Outputs and hand-off: the text before outputs.yaml

`bc-portfolio` delivers one portfolio review protocol per review round, with every figure dated and labelled, and a prioritization record when candidate use cases compete. It reads and analyses; it does not change any list.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Portfolio review protocol | `assets/portfolio-review-protocol.md`, filled | `metrics-scorecard` (round prep), DBVE | Surface and capture date stated; cuts by more than one dimension for any scale claim; every empty field stated as unknown or nil; every euro figure labelled tracked or proven; denominator on every rate |
| Savings read | Section of the protocol | `metrics-scorecard`, `bc-build` | Tracked and proven euros never added; reliability classes not rolled into one headline; regions not blended |
| Prioritization record | Record built with `references/od-use-case-prioritization/procedure.md` | `dept-decision-rights`, OD lead | Ranking only within a category; the order of criteria and the planning state named; the unscoreable bucket kept visible |

## Handoff

- **Receives from:** `know-sharepoint-export` (dated capture of the use-case and savings lists), `bc-build` (the saving rows and their firmness).
- **Next in the flow:** `metrics-scorecard` (round prep), `dept-plant-diagnosis` (savings by plant, status cut), `catalog-standardization`, `deploy-project-order` (use case, scope, demand); the ranking feeds step 24 and `dept-decision-rights`.
- **Stops here when:** a figure has no read date, a rate has no denominator, or a "no potential" conclusion would rest on zero reported saving for a scaled use case. Mark it for further investigation instead of publishing the number.

## Standing findings (context for reading the portfolio)

- The catalogue is built to standardize and has not scaled: capabilities are instantiated at (nearly) every plant, so templates are not the constraint, adoption of the proven instance is. Verify on the live capability instance list.
- The savings ledger is mostly empty scaffolding. Pattern: the tracker was actively maintained for a period and then largely abandoned, so the reliability field is mostly empty and few use cases carry a figure. Verify by counting blank reliability.
- The regions are not variations of one another. A low-converting region is a different problem from a high-converting one, not a smaller one; a plan that treats regions as scaled copies fails in the weakest one. The best-converting region's rate is the one worth interrogating for what it does differently.
- C12 "Other and plant-specific" is a data-quality signal, not only a topical one; track its size over time rather than quoting it once.
- Version history carries text the current record does not: rationale, blockers and comments were written during active work and later tidied back to `-`. An analysis over the current snapshot alone misses part of the narrative.
- The absorbed prioritization job (formerly `od-use-case-prioritization`, merged 2026-11-10) keeps its own references and assets under `references/od-use-case-prioritization/` and the authority it had (recommend).
