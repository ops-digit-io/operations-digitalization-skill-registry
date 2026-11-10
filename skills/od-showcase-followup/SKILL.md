---
name: od-showcase-followup
description: >-
  Close the loop after a use-case story is published (new-state Lane 4, step 44): record what was published and
  where, route every reaction back into the right lane (a plant that wants a catalogued use case goes to Lane 1, a
  new need to Lane 2, a need for a system or connector to Lane 3), keep the story true as the use case changes, and
  capture what the promotion taught OD. Defines the few measures of the lane without targets. Use after Internal
  Communications has published, when a plant reacts to a story, or when a published story may have gone stale.
license: MIT
metadata:
  id: od-showcase-followup
  tier: practice
  lane: lane-4
  new_state_lane: "Lane 4 (44)"
  new_state_step: "Follow up and feed back into Lanes 1 to 3"
  owner_role: Digital-Business-Value-Engineer (DBVE)
  authority_level: draft the follow-up log and the routing and recommend; OD lead and plant owners decide; Internal Communications owns any correction of a published item
  status: draft
  sources_read: 2026-11-10
  requires: [od-context]
  composes: [od-comms-brief, catalog-usecase, od-use-case-intake-triage, od-handover-and-adoption]
  derived_from:
    - "Owner request, 2026-11-10: a new outbound service lane for use-case marketing via the internal communications department"
    - "Work vault, OD Department Knowledge/OD-instance/00-core/06-operating-rhythm.md (monthly retro: what did we learn, one change), read 2026-11-10"
    - "Work vault, OD Department Knowledge/OD-instance/20-lanes-newstate-DRAFT/lane-1-run-known-uc.md and lane-2-develop-new-use-case.md (fall-through and cataloguing), read 2026-11-10"
    - "Work vault, OD Department Knowledge/OD-instance/00-core/07-metrics.md (utilization rate), read 2026-11-10"
  okf:
    type: Agent Skill
    title: Showcase follow-up
    tags: [lane-4, practice, draft]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-11-10T00:00:00Z }
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

## Measures of the lane (definitions, proposed; no targets)

| Measure | Definition | Source |
|---|---|---|
| Time to story | Days from `PRODUCTIVE` with adoption confirmed to publication | Handover record, publication date |
| Requests from stories | Count of Lane 1 requests and intake demands whose source is a story | The follow-up log |
| Story to request rate | Requests from stories divided by stories published in the period | The follow-up log |
| Stale stories | Published stories past their review date without a review | The follow-up log |

## Human gate and AI-agent notes

- **Agent may:** keep the log, route reactions, draft the answers, flag stale stories. **Humans decide:** every promise, every acceptance into a lane, any correction of a published item (Internal Communications).
- **Evidence to cite:** the publication record, the reaction text (masked of individuals), the routing result.

## Pitfalls

- Treating reach as success. A story is worth what it moves into the lanes.
- Answering a plant's request with a delivery date.
- Quoting an IC reach figure that IC did not give.
- Leaving a story up after the savings were restated.

## References

| File | Open when |
|---|---|
| [`references/feedback-routing.md`](references/feedback-routing.md) | Routing a reaction into a lane, answering, refreshing or retiring a story |
| [`assets/followup-log.md`](assets/followup-log.md) | The log to fill |
