---
name: od-showcase-followup
description: >-
  Close the loop after a use-case story is published (Lane 4): record it, route reactions to the right lane, keep the story true, capture lessons. Use after Internal Communications has published.
license: MIT
metadata:
  id: od-showcase-followup
  tier: practice
  lane: lane-4
  new_state_lane: "Lane 4 (44)"
  new_state_step: "Follow up and feed back into Lanes 1 to 3"
  owner_role: Digital-Business-Value-Engineer (DBVE)
  tags: [lane-4, practice, draft]
  authority_level: draft the follow-up log and the routing and recommend; OD lead and plant owners decide; Internal Communications owns any correction of a published item
  status: draft
  requires: [od-context]
  composes: [od-comms-brief, catalog-usecase, od-use-case-intake-triage, od-handover-and-adoption]
  okf:
    type: Agent Skill
    title: Showcase follow-up
    tags: [lane-4, practice, draft]
---

# Showcase follow-up

Read `od-context` first. A story that is published and then forgotten is a cost. This skill is step 44: it turns the reactions to a story into demand for the lanes that can serve it, and keeps the story true.

## Inputs and output

- **In:** the approved brief (`od-comms-brief`), the publication facts as Internal Communications gives them (channel, date, any reach figure), and the reactions: questions, requests, objections.
- **Out:** the filled [`assets/followup-log.md`](assets/followup-log.md), one per story, with each reaction routed and the review date set.

## Procedure

1. **Record the publication:** the use case, the plant, the channel, the date, the audiences, the claims as published. Copy the reach or response figures exactly as IC reports them, with their source; if IC reports none, write "not reported", never an estimate.
2. **Route every reaction** ([`references/feedback-routing.md`](references/feedback-routing.md)): a plant that wants a catalogued use case becomes a Lane 1 request (`catalog-usecase`); a need that no catalogue entry fits is a demand for intake (`od-use-case-intake-triage`, Lane 2); a need for a new system or connector goes to Lane 3 through intake. Do not promise delivery in the answer.
3. **Answer within the story's promise** only: what the story said it could do. Anything else is an intake request, with the usual refusal list.
4. **Keep it true.** Set a review date. When the use case changes (a new version, a status change, a corrected saving), update the log and tell Internal Communications, who decides whether the published item is corrected or withdrawn.
5. **Learn.** One line per promotion for the monthly retro: what worked, what did not, one change.
6. **Measure,** with the definitions below and no targets until the department sets them.

## Purpose

Turns the reactions to a published use-case story into routed demand for the lanes that can serve it, and keeps the story true over time. Use it after Internal Communications publishes a story (step 44).

## Measures of the lane (definitions, proposed; no targets)

The stage column follows the AMEC Integrated Evaluation Framework (a professional body's free framework for evaluating communication): reach is an output, not a result, so report the outcome and impact measures next to it.

| Measure | AMEC stage | Definition | Source |
|---|---|---|---|
| Time to story | Output (activity) | Days from `PRODUCTIVE` with adoption confirmed to publication | Handover record, publication date |
| Reach or response | Output | As Internal Communications reports it, or "not reported" | The publication record |
| Reactions recorded | Out-take | Count of reactions in the log, by audience | The follow-up log |
| Requests from stories | Outcome | Count of Lane 1 requests and intake demands whose source is a story | The follow-up log |
| Story to request rate | Outcome | Requests from stories divided by stories published in the period | The follow-up log |
| Second-plant adoptions from stories | Impact | Count of use cases running at a plant other than the story's plant (`PRODUCTIVE`, adoption confirmed) whose request source is a story | The follow-up log, the handover record |
| Stale stories | Quality of the record | Published stories past their review date without a review | The follow-up log |

## Human gate and AI-agent notes

- **Agent may:** keep the log, route reactions, draft the answers, flag stale stories. **Humans decide:** every promise, every acceptance into a lane, any correction of a published item (Internal Communications).
- **Evidence to cite:** the publication record, the reaction text (masked of individuals), the routing result.

## Pitfalls

- Treating reach as success. A story is worth what it moves into the lanes, and in the end what runs at another plant.
- Answering a plant's request with a delivery date.
- Quoting an IC reach figure that IC did not give.
- Leaving a story up after the savings were restated.

## Example

Fictional example (plant and reaction invented for illustration):

```text
Story: use case U, plant X, channel: internal news, published 2026-01-01 (fictional)
Reach: not reported by IC
Reaction: "Plant Y wants this" -> Lane 1 request (catalog-usecase)
Reaction: "Can it also read machine Z?" -> intake demand (Lane 2)
Review date: set; next retro line: one change
```

If a reaction cannot be placed or a figure has no source, write "not reported" or ask the routing owner; do not guess. Check each log entry for a route and a review date before closing it, and treat an entry without them as invalid.

## Definition of done

The publication is recorded, every reaction has a route, the answers stay within the story's promise, a review date is set, and the log is filled.

## References

Each template, asset and other resource of this skill is listed here:

| File | Open when |
|---|---|
| [`references/feedback-routing.md`](references/feedback-routing.md) | Routing a reaction into a lane, answering, refreshing or retiring a story |
| [`assets/followup-log.md`](assets/followup-log.md) | The log to fill |
