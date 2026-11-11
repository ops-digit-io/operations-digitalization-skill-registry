---
type: Skill Reference
title: Outputs
description: The outputs catalog-usecase must deliver, who receives each one, and what makes each complete.
resource: ../SKILL.md
status: draft
tags: [outputs, handoff]
---
# Outputs

`catalog-usecase` delivers a match record that says whether a plant request is a catalogued use case, which branch it takes and which skill comes next. At the end of Lane 2 it delivers a graduation proposal instead. The skill is not done until the output exists in the stated form.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Match record | `assets/catalog-match-record.md`, filled | `ops-analytics-asset` (branch 1a), `catalog-systems` (branch 1b), Lane 2 or Lane 3 on fall-through | Names the branch (1a, 1b, Lane 2 or Lane 3) and the next skill; CSP status (`Yes` / `No` / not decided) with its source and read date; preconditions with the data-availability verdict; the plant's utilization moment or `<to confirm>` |
| Fall-through statement | Section of the match record | Requester, then `funnel-use-case` (Lane 2) or `funnel-requirements` (Lane 3) | A candidate with no recorded CSP `Yes`, or a failed precondition, is stated plainly as not catalogued and routed |
| Graduation proposal (step 26 only) | Proposal with the entry content | OD lead, with `deploy-handover` for the plant handover | All four conditions hold (CSP `Yes`, capability template, standardized signals, plant owner with a passed handover test) and the plant's utilization moment is recorded |

## Handoff

- **Also receives from:** `ops-dashboard-datatron`: Dashboard; Published example.
- **Also receives from:** `comms-followup`: Routed reactions.
- **Also receives from:** `catalog-compatibility`: Verdict grid for the catalog.
- **Receives from:** `dept-intake` (the classified request), `mi-data-availability` (machine connected, signals present), `deploy-handover` (the handover record, at step 26).
- **Next in the flow:** step 1a1 to `ops-analytics-asset` (step 1a2); step 1b1 to `catalog-systems`, then `dept-decision-rights` (1b2); a result that falls through goes to Lane 2 (`funnel-use-case`) or Lane 3 (`funnel-requirements`). At step 26 the entry becomes a future Lane 1 case.
- **Stops here when:** the candidate has no recorded CSP `Yes`, a precondition fails, or the need sits outside the lean footprint and `invest-screen` has not run. Do not present it as catalogued or let the plant self-serve it; the CSP decision itself stays with its owner.
