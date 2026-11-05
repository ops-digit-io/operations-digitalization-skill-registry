---
type: Skill Reference
title: Rounds and escalation
description: How to prepare and follow up ODEC and COP specifically - the real recurring shape of each round's content, and where the escalation gaps actually sit.
resource: ../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [all, practice, scorecard]
generated: { by: claude-code/1, at: 2026-10-22T00:00:00Z }
---
# Rounds and escalation

## ODEC's recurring shape

Across past ODEC rounds, the KPI content that actually gets presented breaks out **by
region** against its own plan, not as one department-wide number: Equipment Integration
and Use Case Development each reported as *today vs. plan*, region by region (the
regions as named on the Scorecard), not blended into a single total. Mirror that shape when
preparing a round — a blended total hides exactly the regional divergence
`od-use-case-standardization` documents (conversion of proven use cases differs by region,
and a lagging region is "a different problem, not a smaller one").
Report per-region figures first; the department-wide total is a secondary rollup, not the
headline.

Recurring ODEC content, from what past rounds have actually covered: a strategy recap
against the year's KPI targets, a ranked or upvoted use-case list (what plants want built
next), the engineering-roadmap input process (carry-over projects, new high-value requests,
rollout/extension of existing system+equipment+use-case integration, strategic initiative
topics), and standing agenda items such as Smart Factory tool training uptake. Prepare
against whichever of these the round's actual agenda names — do not invent a generic
agenda when a specific one exists.

## COP's recurring shape

Technical rather than strategic: connector and data-model updates, new use-case ideas from
a technical angle, cyber-security aspects of a rollout, and — per the existing failure-loop
table in `od-acceptance-test` — failed-acceptance findings that need a technical decision
rather than a plant-level one.

## Preparing a round

1. Pull the scorecard figures with their read date (per the main `SKILL.md` procedure).
2. Split by region before summarizing department-wide — region-blind figures have hidden
   regional divergence before and will again.
3. Match content to the round's own input column (strategy and rollout items to ODEC,
   technical and connection items to COP) — a technical blocker raised at ODEC gets
   redirected, not solved there.
4. Bring the **one** retro change forward if it affects either round's content.

## Following up a round

Record the output column's commitments against a named owner and the round that produced
them — an ODEC roadmap decision or a COP technical guidance update that is not written down
against an owner is indistinguishable, a cycle later, from a decision nobody made.

## The escalation window, confirmed 2026-10-22

`od-decision-routing` names the escalation **destination** (OD lead, via ODEC for strategy
or COP for technical matters); this skill names the escalation **window**: one round. An
item unresolved at one ODEC or COP cycle escalates into the next, rather than being carried
quietly for an unstated number of cycles.
