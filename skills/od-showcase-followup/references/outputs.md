---
type: Skill Reference
title: Outputs
description: The outputs od-showcase-followup must deliver, who receives each one, and what makes each complete.
resource: ../SKILL.md
status: draft
tags: [outputs, handoff]
---
# Outputs

`od-showcase-followup` (step 44) delivers the follow-up log for one published story: every reaction routed to the lane that
can serve it, and a review date so the story stays true. It is the end of Lane 4.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Follow-up log | `assets/followup-log.md`, one per story | OD lead | Publication recorded (use case, plant, channel, date, audiences, claims as published); reach figures copied exactly as Internal Communications reports them, or "not reported" |
| Routed reactions | Entries in the follow-up log | `catalog-usecase` (catalogued use case, Lane 1), `od-use-case-intake-triage` (new need, or a need for a new system or connector, via intake) | Every reaction has a route; answers stay within the story's promise; no delivery date promised |
| Review date and correction notice | Review date in the log; notice when the use case changes | Internal Communications | Review date set; on a changed use case or restated saving, the log is updated and Internal Communications told, who decides on correcting or withdrawing |
| Retro line | One line per promotion in the log | OD lead | What worked, what did not, one change, ready for the monthly retro |

## Handoff

- **Receives from:** `od-comms-brief` (the approved brief), and Internal Communications (channel, date, any reach figure) with the reactions: questions, requests, objections.
- **Next in the flow:** the end of Lane 4. Reactions feed back into the other lanes: a catalogued use case to Lane 1 (`catalog-usecase`), a need no catalogue entry fits to Lane 2 and a need for a new system or connector to Lane 3, both through `od-use-case-intake-triage`.
- **Stops here when:** a reaction cannot be placed or a figure has no source: write "not reported" or ask the routing owner, do not guess. Any promise, any lane acceptance and any correction of a published item is a human decision.
