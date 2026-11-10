---
type: Design Record
title: Lane 4 use case promotion
description: "Design of the new outbound service lane that promotes live, adopted use cases to other plants, leadership and colleagues through Internal Communications: trigger, steps, owners, gates, authority, the three skills, the lane measures, risks and the open points that wait for the Internal Communications brief."
status: draft
owner: human:jakob.gabriel
tags: [process-flow, lanes, lane-4, outbound]
generated: { by: claude-code/1, at: 2026-11-10T00:00:00Z }
---
# Lane 4: use case promotion (outbound)

**Origin.** Requested by the owner on 2026-11-10: a new service lane that is mainly outbound, for use-case marketing via the internal communications department. Decisions taken the same day: it starts when a use case is **live and adopted**; the audiences are other plants and key users, BA Operations leadership, all employees, and the OPEX and PPI/ME community; Internal Communications (IC) receives the brief that the owner will supply; the scope of this step is the design, the skills and the diagram.

**Status.** Draft, AI-assembled, not reviewed by a human. The department's own lane files describe three lanes (`20-lanes-newstate-DRAFT`); Lane 4 is an addition of this registry and is not in the department's decision rights.

## What it is

Lanes 1 to 3 bring demand in and deliver. Lane 4 sends results out: it tells the company what a use case delivered, so that other plants pull catalogued use cases (Lane 1 demand) and leadership sees progress. It is **not an intake lane**: no demand is classified into it. It is entered from a use case that is live and adopted, at Lane 1 go-live or Lane 2 graduation.

| | |
|---|---|
| Trigger | A use case at `PRODUCTIVE` with adoption confirmed by the recipient |
| Customer | Internal Communications (as publisher) and the four audiences |
| Ownership | OD-led (DBVE); the plant owner consents; IC decides channel, form, date and publishes |
| Money | None. Effort only |
| Done | A story published by IC, every reaction routed into Lanes 1 to 3, a review date set |

## Steps

| Step | Flow id | Skill | Control point | Who |
|---|---|---|---|---|
| Select and check the story | 41 | `od-showcase-selection` | Gate passed: live and adopted, plant owner agrees, claims carry evidence, nothing sensitive, people content handled (consent or a documented balancing, otherwise roles and screenshots only), audience named | DBVE; plant owner decides |
| Brief Internal Communications | 42 | `od-comms-brief` | Brief checked by `check_comms_brief.py` | DBVE |
| Review and publish | 43 | `od-comms-brief` (approvals list) | Approvals: plant owner, OD lead, IC | Humans; IC publishes. External wait: IC |
| Follow up and feed back | 44 | `od-showcase-followup` | Each reaction routed; review date set | DBVE |

Feed-back routes: a request for a catalogued use case goes to Lane 1, a new recurring need to intake and Lane 2, a need for a system or connector to intake and Lane 3.

## Built on the department's own material

Lane 4 reuses what OD already has: the CSP appetizer fields, the pairing of an OPEX method with a digital standard use case, the plant testimonial template and the story shapes used at ODEC (`od-comms-brief`, `references/department-formats.md`), and it lists the peer-sharing channels that exist (ODEC use-case slot, CoP best-practice slot, the OPEX exchange call, the Yokoten database) as options to confirm. The January 2026 marketing-template initiative planned a marketing process and communication channels but left its results slide empty: Lane 4 is the first attempt to finish it, and its status is to be confirmed by the owner.

## Rules the lane enforces

- **No invented figures** (vault `CLAUDE.md` 1.5). Every figure carries an evidence class: `CALCULATION`, `ESTIMATION` or `not yet assessed`.
- **A saving is a claim until it is registered.** It counts as a result only with a registered plant savings project and a baseline (registry rule in `od-use-case-definition`).
- **Roles, not individuals** (vault `CLAUDE.md` 3); no host names, addresses or links to internal systems.
- **OD never publishes.** The agent drafts and checks; every approval is human; IC publishes.
- English deliverables.

## Authority

No row for outbound communication exists in `08-decision-rights.md`. `od-decision-routing` carries a **proposed** row (DBVE with the plant owner and IC, tandem, approval yes, not reversible once published, `recommend`). The OD lead has to confirm it.

## Measures (definitions only, no targets)

Time to story; requests from stories; story-to-request rate; stale stories. Defined in `od-showcase-followup`. The department sets targets.

## Risks

| Risk | Mitigation |
|---|---|
| Claims run ahead of evidence | The gate (step 41) and the check script (step 42); savings stay claims until registered |
| A plant is named without consent | Written consent of the plant owner is a gate criterion |
| A published story ages or is restated | Review date; IC corrects or withdraws; `od-showcase-followup` |
| IC's process differs from the generic brief | The brief is a hand-over, not a template IC must adopt; IC's own form replaces it once supplied |
| Marketing load pulls OD into a communications role | OD drafts for IC and does not publish; the lane is limited to live, adopted use cases |

## Open points (waiting for the Internal Communications brief)

Intake channel or role at IC; channels per audience; lead time; an IC template or review route; brand and tone rules and the neuwerk template; a second approval or language; the reach or response data IC returns. Recorded as topic 6 of `PHASE1-ELICITATION.md` and in `skills/od-comms-brief/references/ic-handover.md`.

## What was added to the registry

Three core skills (draft): `od-showcase-selection`, `od-comms-brief` (with `check_comms_brief.py` and tests), `od-showcase-followup`. Lane 4 in `process.yaml`, the Mermaid flow, the owner's process diagram (a Lane 4 block in the same style, the three skills in the net-new strip) and the site. A paragraph in `od-context` and a proposed row in `od-decision-routing`.
