---
name: comms-showcase
description: >-
  Decide which use case is ready to be told company-wide and which claims it may carry (Lane 4): go, hold or no. Not for writing the story (comms-brief).
license: MIT
metadata:
  id: comms-showcase
  aliases: [od-showcase-selection]   # former name (naming convention, 2026-11-11)
  tier: practice
  lane: lane-4
  new_state_lane: "Lane 4 (41)"
  new_state_step: "Select the use case and check the story"
  owner_role: Digital-Business-Value-Engineer (DBVE); the plant owner agrees
  tags: [lane-4, practice, draft]
  authority_level: draft the selection record and recommend go, hold or no; the plant owner and the OD lead decide
  status: draft
  requires: [dept-context]
  composes: [deploy-handover, bc-build, catalog-usecase, comms-brief]
  okf:
    type: Agent Skill
    title: Showcase selection
    tags: [lane-4, practice, draft]
---

# Showcase selection

Read `dept-context` first. Lane 4 is the outbound lane: it tells other plants, leadership and colleagues what a use case delivered, through Internal Communications (IC). It is entered only from a use case that is **live and adopted** (Lane 1 go-live, or Lane 2 graduation), never from intake. This skill is step 41: choose what is worth telling and what may be said.

## Inputs and output

- **In:** a use case at `PRODUCTIVE`, its handover record (`deploy-handover`), its savings status (`bc-build`), the plant owner.
- **Out:** the filled [`assets/selection-record.md`](assets/selection-record.md): go, hold or no, the audience, the claims that may be made with their evidence class, and the open points. A `go` goes to `comms-brief`.
- **Outputs:** [`references/outputs.md`](references/outputs.md) lists what this skill must deliver, to whom, and when each output is complete.

## Purpose

Decides whether a live, adopted use case is ready to be told to the rest of the company, and which claims it may carry. Use it when a use case has gone productive, when someone asks to publicise a result, or before any story is briefed to Internal Communications (step 41).

## The gate, in order

1. **Live and adopted.** Delivery status `PRODUCTIVE`, and the recipient confirmed adoption into the daily process. Implemented is not adopted; a use case with utilization `NEVER` is not a story yet.
2. **The plant owner agrees,** in writing, to be named as the plant (not as a person) and to the claims.
3. **Evidence per claim.** Every figure gets one class: `CALCULATION` (with its method), `ESTIMATION`, or `not yet assessed`. A saving counts as a **result** only when a plant savings project and a baseline are registered; before that it is a **claim** and is worded as one. Never invent or round up a figure.
4. **Sensitivity screen.** No individual named, no host name, address or credential, no supplier or customer detail, nothing that exposes the cyber posture of a plant ([`references/readiness-gate.md`](references/readiness-gate.md)).
5. **People content.** A photo, video or quote of a member of staff needs that person's consent or a documented balancing of interests; otherwise the story uses roles and screenshots only. A balancing of interests lists the employer's reasons, the employees' counter-reasons and the weighing ([`references/readiness-gate.md`](references/readiness-gate.md)).
6. **Audience fit.** Name the audiences the story is for and what each should do next ([`references/readiness-gate.md`](references/readiness-gate.md)).

## Verdicts

| Verdict | When | Next |
|---|---|---|
| **Go** | Gate steps 1 to 6 pass | `comms-brief` |
| **Hold** | Adoption not yet confirmed, a figure is still a claim and the story needs it, the plant owner has not answered | Name what is missing and the owner; revisit at the next review |
| **No** | The plant owner declines, the use case is not live, or the story cannot be told without a sensitive detail | Record the reason; do not retry through another channel |

## Procedure

Work the six gate steps in order ("The gate, in order"), fill the selection record, and give one verdict from the table above. If a gate step fails validation (a failure, not a pass), the verdict is Hold (something is missing) or No (the owner declines or a sensitive detail cannot be removed); record the reason either way.

Fictional example (plant and figures invented for illustration):

```text
Use case: U at plant X, status PRODUCTIVE, adoption confirmed
Claim: "saves 1,000 EUR per year" - ESTIMATION (fictional figure), no baseline registered -> worded as a claim
Sensitivity screen: pass; people content: roles and screenshots only
Verdict: Go -> comms-brief
```

## Human gate and AI-agent notes

- **Agent may:** read the use-case record, draft the selection record, list what is missing. **Humans decide:** the plant owner (consent and claims), the OD lead (whether OD tells it).
- **Evidence to cite:** the status and adoption date, the savings register entry or its absence, the owner's consent.
- A use case chosen only because it is impressive fails step 3 sooner than it passes.

## Pitfalls

- Telling the story at go-live: the first weeks show delivery, not use.
- Quoting the savings from the business case as if they were measured.
- Naming the engineer who built it. Name the role and the plant.
- Treating a published story as permanent: it ages (see `comms-followup`).

## Definition of done

The selection record is filled: verdict, audiences, claims with their evidence class, open points and owners. A Go has been handed to `comms-brief`.

## References

Each template, asset and other resource of this skill is listed here:

| File | Open when |
|---|---|
| [`references/readiness-gate.md`](references/readiness-gate.md) | The gate criteria, the sensitivity screen, the audience table, refusal patterns |
| [`assets/selection-record.md`](assets/selection-record.md) | The record to fill, one per use case |
