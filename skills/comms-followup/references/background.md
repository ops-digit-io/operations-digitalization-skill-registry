---
type: Skill Reference
title: Background
description: Context, rationale, examples and notes that stood in SKILL.md, moved here unchanged. Open it for the why; it is never an instruction.
resource: ../SKILL.md
status: draft
tags: [background]
---
# Background

## Example

Fictional example (plant and reaction invented for illustration):

If a reaction cannot be placed or a figure has no source, write "not reported" or ask the routing owner; do not guess. Check each log entry for a route and a review date before closing it, and treat an entry without them as invalid.

## Outputs and hand-off: the text before outputs.yaml

`comms-followup` (step 44) delivers the follow-up log for one published story: every reaction routed to the lane that
can serve it, and a review date so the story stays true. It is the end of Lane 4.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Follow-up log | `assets/followup-log.md`, one per story | OD lead | Publication recorded (use case, plant, channel, date, audiences, claims as published); reach figures copied exactly as Internal Communications reports them, or "not reported" |
| Routed reactions | Entries in the follow-up log | `catalog-usecase` (catalogued use case, Lane 1), `dept-intake` (new need, or a need for a new system or connector, via intake) | Every reaction has a route; answers stay within the story's promise; no delivery date promised |
| Review date and correction notice | Review date in the log; notice when the use case changes | Internal Communications | Review date set; on a changed use case or restated saving, the log is updated and Internal Communications told, who decides on correcting or withdrawing |
| Retro line | One line per promotion in the log | OD lead | What worked, what did not, one change, ready for the monthly retro |

## Handoff

- **Receives from:** `comms-brief` (the approved brief), and Internal Communications (channel, date, any reach figure) with the reactions: questions, requests, objections.
- **Next in the flow:** the end of Lane 4. Reactions feed back into the other lanes: a catalogued use case to Lane 1 (`catalog-usecase`), a need no catalogue entry fits to Lane 2 and a need for a new system or connector to Lane 3, both through `dept-intake`.
- **Stops here when:** a reaction cannot be placed or a figure has no source: write "not reported" or ask the routing owner, do not guess. Any promise, any lane acceptance and any correction of a published item is a human decision.

## Measures of the lane (proposed definitions, no targets; moved from SKILL.md)

- The stage column follows the AMEC Integrated Evaluation Framework (a professional body's free framework for evaluating communication): reach is an output, not a result, so report the outcome and impact measures next to it.
- Measurable from the log today: reactions recorded, requests from stories, second-plant adoptions, stale stories. The others depend on IC or the handover record.

| Measure | AMEC stage | Definition | Source |
|---|---|---|---|
| Time to story | Output (activity) | Days from `PRODUCTIVE` with adoption confirmed to publication | Handover record, publication date |
| Reach or response | Output | As Internal Communications reports it, or "not reported" | The publication record |
| Reactions recorded | Out-take | Count of reactions in the log, by audience | The follow-up log |
| Requests from stories | Outcome | Count of Lane 1 requests and intake demands whose source is a story | The follow-up log |
| Story to request rate | Outcome | Requests from stories divided by stories published in the period | The follow-up log |
| Second-plant adoptions from stories | Impact | Count of use cases running at a plant other than the story's plant (`PRODUCTIVE`, adoption confirmed) whose request source is a story | The follow-up log, the handover record |
| Stale stories | Quality of the record | Published stories past their review date without a review | The follow-up log |

## Open questions

- The measure set is a proposal built on the AMEC framework and has not been tested on a real published story. Test it on at least one and record where each value was read. Supplier: OD lead.

## Sources used in the improvement run

- None added; no vault or archive claim was introduced in this run.
