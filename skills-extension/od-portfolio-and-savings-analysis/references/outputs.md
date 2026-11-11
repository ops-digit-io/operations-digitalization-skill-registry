---
type: Skill Reference
title: Outputs
description: The outputs od-portfolio-and-savings-analysis must deliver, who receives each one, and what makes each complete.
resource: ../SKILL.md
status: draft
tags: [outputs, handoff]
---
# Outputs

`od-portfolio-and-savings-analysis` delivers one portfolio review protocol per review round, with every figure dated and labelled, and a prioritization record when candidate use cases compete. It reads and analyses; it does not change any list.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Portfolio review protocol | `assets/portfolio-review-protocol.md`, filled | `od-scorecard-reporting` (round prep), DBVE | Surface and capture date stated; cuts by more than one dimension for any scale claim; every empty field stated as unknown or nil; every euro figure labelled tracked or proven; denominator on every rate |
| Savings read | Section of the protocol | `od-scorecard-reporting`, `od-benefit-calculation` | Tracked and proven euros never added; reliability classes not rolled into one headline; regions not blended |
| Prioritization record | Record built with `references/od-use-case-prioritization/procedure.md` | `od-decision-routing`, OD lead | Ranking only within a category; the order of criteria and the planning state named; the unscoreable bucket kept visible |

## Handoff

- **Receives from:** `od-sharepoint-list-export` (dated capture of the use-case and savings lists), `od-benefit-calculation` (the saving rows and their firmness).
- **Next in the flow:** `od-scorecard-reporting` (round prep), `od-plant-diagnosis` (savings by plant, status cut), `od-use-case-standardization`, `od-project-order` (use case, scope, demand); the ranking feeds step 24 and `od-decision-routing`.
- **Stops here when:** a figure has no read date, a rate has no denominator, or a "no potential" conclusion would rest on zero reported saving for a scaled use case. Mark it for further investigation instead of publishing the number.
