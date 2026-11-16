---
type: Skill Reference
title: Background
description: Context, rationale, examples and notes that stood in SKILL.md, moved here unchanged. Open it for the why; it is never an instruction.
resource: ../SKILL.md
status: draft
tags: [background]
---
# Background

## Outputs and hand-off: the text before outputs.yaml

`dept-retro` delivers one retro record per month that ends in exactly one decided adjustment. A retro that produces only a list has not produced a decision.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Check of last month's adjustment | Section of `assets/retro-record.md` | OD lead | Last month's check question answered with evidence; outcome kept, changed or dropped |
| Learning list with evidence | Learning list in the retro record | OD lead | Each item states what happened, evidence, dated source and which input it came from; an item without evidence is marked `⟨evidence missing⟩` or left out |
| The one adjustment | Adjustment section of the retro record | The deciding role named in the current approval policy; the next COP input | Exactly one action with a role as owner, a date and the observable that will show it worked; why this one is stated in one sentence; decider role recorded or shown as `⟨decider role⟩` open |
| Parking list | Parking list in the retro record | Next month's retro | Unchosen items carried with the month they first appeared |
| Escalations | Items that fail the "OD can change it alone" test | `dept-decision-rights` | Each item routed, not counted as an adjustment |

## Handoff

- **Also receives from:** `deploy-project-order`: Lessons learned.
- **Also receives from:** `dept-governance`: Follow-up log.
- **Receives from:** `metrics-scorecard` (metrics with read date, COP round results), `dept-risk` (risk reading for the month), `bc-portfolio`, plus incidents and COP feedback.
- **Next in the flow:** the next COP input, or the deciding role via `dept-decision-rights` if others must act; `dept-context-freshness` if the adjustment changes a context file.
- **Stops here when:** no evidence-backed candidate exists. Record "no adjustment: no evidence-backed candidate" with the inputs read; do not invent one. An adjustment that needs a gate outside OD is routed, not called done.

## Provenance

Plan item O-06 of the department's skill map (wave 3). The operating rhythm marks the retro with a star: input incidents, metrics, ODEC/COP feedback (ODEC no longer meets; its records are history), output one decided adjustment, cadence at least monthly. It states the reason: without a minimal retro cadence the department has no improvement loop, and learning is a leadership duty (PDCA/Kaizen). The operating rhythm excludes agenda templates and participants as names.

## What is still open

- **Who decides the adjustment** and who attends: not stated in the sources.
- **Where the record is kept** (a SharePoint list, the OD Teams site, the decision log): the Department OS has a `decision-log.md` concept "not in the core", but no location is recorded. `⟨location, to confirm⟩`.
- **Incident definition and source.** No incident register is named in the sources read. Candidates: the Blocker Register (a derived view of list fields), the ODEC/COP "issues and feedback" inputs, and support tickets named as an early indicator in `09-risks.md` with no source system. `⟨incident source, to confirm⟩`.
- **Escalation window** of ODEC and COP is `⟨to confirm⟩` in the operating rhythm; `metrics-scorecard` uses "one round".
- **Cadence beyond monthly.** Whether quarterly deeper retros exist is not recorded.

## Sources used in the improvement run

- None beyond the existing skill material; no vault or archive claim was added.
