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
