---
type: Skill Reference
title: Readiness gate
description: The five gate criteria for telling a use case outwards, the sensitivity screen, the audience table (plants and key users, BA Operations leadership, all employees, OPEX and PPI/ME) and the refusal patterns. Open it when a selection is unclear.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [lane-4, practice]
generated: { by: claude-code/1, at: 2026-11-10T00:00:00Z }
---
# Readiness gate for a use-case story

Source of the rule set: the owner's request of 2026-11-10 (an outbound lane via Internal Communications), the department's delivery states and utilization metric (`00-core/07-metrics.md`), and the registry's own savings rule. The gate is **proposed**; the OD lead has not confirmed it.

## The gate

| # | Criterion | Passes when | Evidence | Fails to |
|---|---|---|---|---|
| 1 | Live and adopted | Status `PRODUCTIVE`, recipient confirmed adoption, utilization not `NEVER` | Handover record, Scorecard utilization | Hold |
| 2 | Plant owner agrees | A named role at the plant accepted the plant being named and the claims | The owner's written answer | Hold or No |
| 3 | Claims carry evidence | Each figure has a class and a source; savings are results only with a registered project and baseline | Savings register entry, business-case file | Hold (reword the claim) |
| 4 | Sensitivity screen clear | None of the items below is in the story | Reviewer's check | No, or Hold until removed |
| 5 | Audience named | At least one audience with a next step | The selection record | Hold |

## Sensitivity screen

Out of every story: names of individuals (use the role and the plant); host names, addresses, credentials, network layouts; supplier or customer names and prices; security weaknesses or open cyber findings; anything the plant owner marks as not for release; figures from a draft or an unreviewed source.

## Audiences and what each should do next

| Audience | What they want from the story | Call to action |
|---|---|---|
| Other plants and key users | Whether they can run it themselves | Pull it from the catalogue (`catalog-usecase`) or ask for a Lane 2 definition |
| BA Operations leadership | Value and progress | The value claim with its class, and the decision or support it needs, if any |
| All employees | What changed on the shopfloor and for whom | Where to read more; no figures beyond the evidenced ones |
| OPEX and PPI/ME community | How the use case supports the method (Lean and Digital) | Which method step it supports and how to combine it |

## Refusal patterns

| Pattern | Response |
|---|---|
| "Announce it at go-live." | Hold until adoption is confirmed |
| "Use the business-case savings in the headline." | Reword as a claim, or hold until registered |
| "Mention who built it." | Role and plant only |
| "It worked at one machine, say plants." | State the scope exactly: one plant, one line |
| The plant owner has not answered | Hold; never infer consent from silence |

## Open points

- Whether OD needs the OD lead's sign-off for every story or only for those with a figure. ⟨to confirm⟩
- Which Internal Communications review applies on top of this gate. ⟨to confirm, from the IC brief⟩
