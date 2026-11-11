---
type: Skill Reference
title: Outputs
description: The outputs od-retro must deliver, who receives each one, and what makes each complete.
resource: ../SKILL.md
status: draft
tags: [outputs, handoff]
---
# Outputs

`od-retro` delivers one retro record per month that ends in exactly one decided adjustment. A retro that produces only a list has not produced a decision.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Check of last month's adjustment | Section of `assets/retro-record.md` | OD lead | Last month's check question answered with evidence; outcome kept, changed or dropped |
| Learning list with evidence | Evidence list in the retro record | OD lead | Each item states what happened, evidence, dated source and which input it came from; an item without evidence is marked `⟨evidence missing⟩` or left out |
| The one adjustment | Adjustment section of the retro record | The deciding role named in the current approval policy; the next COP input | Exactly one action with a role as owner, a date and the observable that will show it worked; why this one is stated in one sentence; decider role recorded or shown as `⟨decider role⟩` open |
| Parking list | Parking list in the retro record | Next month's retro | Unchosen items carried with the month they first appeared |
| Escalations | Items that fail the "OD can change it alone" test | `od-decision-routing` | Each item routed, not counted as an adjustment |

## Handoff

- **Also receives from:** `od-project-order`: Lessons learned.
- **Also receives from:** `od-governance-cadence`: Follow-up log.
- **Receives from:** `od-scorecard-reporting` (metrics with read date, COP round results), `od-risk-watch` (risk reading for the month), `od-portfolio-and-savings-analysis`, plus incidents and COP feedback.
- **Next in the flow:** the next COP input, or the deciding role via `od-decision-routing` if others must act; `od-context-freshness` if the adjustment changes a context file.
- **Stops here when:** no evidence-backed candidate exists. Record "no adjustment: no evidence-backed candidate" with the inputs read; do not invent one. An adjustment that needs a gate outside OD is routed, not called done.
