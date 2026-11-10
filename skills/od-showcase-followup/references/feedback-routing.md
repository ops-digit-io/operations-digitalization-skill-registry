---
type: Skill Reference
title: Feedback routing
description: How a reaction to a published use-case story is routed into Lane 1, Lane 2 or Lane 3, how to answer without promising delivery, and when to refresh or retire a story. Open it when a plant reacts to a story or a story is due for review.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [lane-4, practice]
generated: { by: claude-code/1, at: 2026-11-10T00:00:00Z }
---
# Feedback routing

The routing follows the department's three lanes and their fall-through (`20-lanes-newstate-DRAFT`, lane 1 to 3): a catalogued use case is Lane 1, a genuinely new recurring need is Lane 2, a missing system or connector is Lane 3, and every demand is classified into exactly one lane at intake.

## Routing table

| Reaction | Route | Next skill |
|---|---|---|
| "We want this use case." and it is catalogued with a recorded decision to share | Lane 1, branch by whether the machine is connected | `catalog-usecase` |
| "We want this." but it is not catalogued, or only one plant has it | Intake: Lane 2 if the need recurs | `od-use-case-intake-triage` |
| "We want this, but our machine is not connected." | Lane 1b if a standard system fits, else Lane 3 | `catalog-systems`, then intake |
| "Can it also do ⟨other thing⟩?" | A new demand, classified at intake, not an extension of the story | `od-use-case-intake-triage` |
| A question about how it works | Answer from the handover record and the catalogue entry | `catalog-usecase` |
| An objection or a doubt about a claim | Check the evidence; correct the log; tell IC if a published item changes | `od-showcase-selection` (claims) |
| A complaint about the use case itself | Not a promotion matter: route to the plant owner and the handover record | `od-handover-and-adoption` |

## Answering

Answer only what the story said. Say where to go next (the catalogue, intake) and who decides. Do not give delivery dates, cost or effort: those are outputs of a business case and the decision rights. Mask individuals in the log; keep roles.

## Review and retirement

| Trigger | Action |
|---|---|
| The review date passes | Re-read the claims against the current register entry; renew or retire |
| The savings are restated, or the use case is stopped or changed | Update the log the same day; tell Internal Communications; they correct or withdraw the item |
| The plant owner withdraws consent | Treat as a No: tell Internal Communications at once |
| The catalogue entry is replaced by a newer version | Point the story at the new entry or retire it |

## Open points

- How long a story stays current before it needs a review. ⟨to confirm⟩
- Whether Internal Communications can correct or withdraw a published item, and how fast. ⟨to confirm, from the IC brief⟩
