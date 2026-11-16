---
name: comms-followup
description: >-
  Close the loop after Internal Communications has published a use-case story (Lane 4): record the publication facts as IC gave them, route every reaction to the right lane (catalog request, intake demand, new system), answer without promising delivery, set a review date so the story stays true, and write one lesson for the retro. Use when a story is out and plants start asking "we want this too", when someone asks what happened after the story, or when a published saving or version has changed. Drafts the log and recommends; the OD lead and plant owners decide, and IC owns any correction. Not for writing the story (comms-brief) or deciding what may be told (comms-showcase).
license: MIT
metadata:
  id: comms-followup
  aliases: [od-showcase-followup]   # former name (naming convention, 2026-11-11)
  tier: practice
  lane: lane-4
  new_state_lane: "Lane 4 (44)"
  new_state_step: "Follow up and feed back into Lanes 1 to 3"
  owner_role: Digital-Business-Value-Engineer (DBVE)
  tags: [lane-4, practice, ready]
  authority_level: draft the follow-up log and the routing and recommend; OD lead and plant owners decide; Internal Communications owns any correction of a published item
  status: ready
  requires: [dept-context]
  composes: [comms-brief, catalog-usecase, dept-intake, deploy-handover]
  okf:
    type: Agent Skill
    title: Showcase follow-up
    tags: [lane-4, practice, ready]
---

# Showcase follow-up

## Purpose

- Turn the reactions to a published use-case story into routed demand for the lanes that can serve it, and keep the story true over time (step 44).
- Use it after Internal Communications (IC) has published a story, because a story that is published and then forgotten is a cost.
- Read `dept-context` first.

## Terms used here

- **Reaction**: the raw input a plant or reader sends after the story (question, wish, objection).
- **Request**: a reaction after routing: a Lane 1 request or an intake demand with an id.
- **Story**: the published item; **brief** is the hand-over from `comms-brief`.

## Inputs and output

- **In:** the approved brief (`comms-brief`), the publication facts as IC gives them (channel, date, any reach figure), and the reactions.
- **Out:** the filled [`assets/followup-log.md`](assets/followup-log.md), one per story, with each reaction routed and the review date set.
- Output contract: [`references/outputs.md`](references/outputs.md) lists what this skill must deliver, to whom, and when each output is complete.

## Procedure

1. **Record the publication:** the use case, the plant, the channel, the date, the audiences, the claims as published.
   - Copy reach or response figures exactly as IC reports them, with their source; if IC reports none, write "not reported", never an estimate.
2. **Route every reaction** (`references/feedback-routing.md`): a plant that wants a catalogued use case becomes a Lane 1 request (`catalog-usecase`); a need that no catalog entry fits is a demand for intake (`dept-intake`, Lane 2).
   - A need for a new system or connector goes to Lane 3 through intake.
   - Do not promise delivery in the answer, because the story only promised what it said.
3. **Answer within the story's promise** only: what the story said it could do. Anything else is an intake request, with the usual refusal list.
4. **Keep it true.** Set a review date. When the use case changes (a new version, a status change, a corrected saving), update the log and tell IC, who decides whether the published item is corrected or withdrawn.
5. **Learn.** One line per story for the monthly retro: what worked, what did not, one change.
6. **Measure** with the few measures below and no targets until the department sets them.
7. **Close the log check** before you hand it to the OD lead.

### Closing check

- [ ] The publication block is filled; reach is a figure with a source or "not reported".
- [ ] Every reaction row has a route and an answer inside the story's promise.
- [ ] Every request has an id or "none".
- [ ] A review date is set and any change to the story is logged with IC told.
- [ ] One lesson line is written for the retro.

## Measures the log records (no targets)

| Measure | Definition | Source |
|---|---|---|
| Reactions recorded | Count of reactions in the log, by audience | The follow-up log |
| Requests from stories | Count of Lane 1 requests and intake demands whose source is a story | The follow-up log |
| Second-plant adoptions from stories | Use cases running at another plant (`PRODUCTIVE`, adoption confirmed) whose request source is a story | The follow-up log, the handover record |
| Stale stories | Published stories past their review date without a review | The follow-up log |

- Reach is an output, not a result: report requests and adoptions next to it. The full proposed measure set is in `references/background.md`.

## Example

```text
Story: use case U, plant X, channel: internal news, published (date) (fictional)
Reach: not reported by IC
Reaction 1: "Plant Y wants this" -> request: Lane 1 (catalog-usecase), id R-1 (fictional)
Reaction 2: "Can it also read machine Z?" -> request: intake demand (Lane 2), id R-2 (fictional)
Answer: "The story covers the downtime screen only; your second question goes to intake."
Review date: set; retro line: one change
```

## Human gate and AI-agent notes

- **Agent may:** keep the log, route reactions, draft the answers, flag stale stories.
- **Humans decide:** every promise, every acceptance into a lane, any correction of a published item (IC).
- **Evidence to cite:** the publication record, the reaction text (masked of individuals), the routing result.

## Pitfalls

- Treating reach as success: a story is worth what it moves into the lanes, and in the end what runs at another plant.
- Answering a plant's request with a delivery date: the story promised no date and OD has not accepted the demand.
- Quoting an IC reach figure that IC did not give.
- Leaving a story up after the savings were restated: readers keep quoting the old figure.
- Naming the person who reacted: log the role, not the name.

## Errors and validation

- **A reaction fits no lane:** record it in the log as unrouted with the date and ask the OD lead; do not guess a lane.
- **The published text differs from the approved brief:** record the difference, stop further reuse of the story and tell the owner of the brief.
- **A measure has no source:** leave it empty and say why; the log never carries an invented figure or a target.

## Definition of done

- The publication is recorded, every reaction has a route, the answers stay within the story's promise, a review date is set, and the log is filled.
- The closing check is ticked.

## Outputs

- [`outputs.yaml`](outputs.yaml): required outputs, criteria, checks and sign-offs.
- One run record per call: `python scripts/run_record.py new <skill-id>` (registry root).

## References

| File | Open when |
|---|---|
| [`references/feedback-routing.md`](references/feedback-routing.md) | Step 2 to 4: routing a reaction into a lane, answering, refreshing or retiring a story |
| [`assets/followup-log.md`](assets/followup-log.md) | Step 1: the log to fill |
| [`references/background.md`](references/background.md) | Context, rationale, the full proposed measure set and open questions; never an instruction |
| [`evals/evals.json`](evals/evals.json) | Test cases and trigger queries to run with and without this skill |
