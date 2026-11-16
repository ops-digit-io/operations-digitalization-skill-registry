---
name: funnel-workshop
description: >-
  Prepare, run and close an OD Use Case Definition Workshop, Use Case Integration Workshop or Machine Integration Workshop at a plant: pick the format and order, set purpose and audience, send the pre-read, capture demand, savings pre-evaluation and tool and machine needs in one sheet, and turn the output into a follow-up list with owners. Use when a workshop is requested or scheduled, a plant is onboarded or a new demand wave starts, a use case is ready for integration, or workshop notes exist but no follow-up list. Drafts materials; the DBVE facilitates, the Plant ME owns the plant side. Not for a single ad-hoc process issue (funnel-first-aid) or defining one use case (funnel-use-case).
license: MIT
allowed-tools: Read Grep Glob
metadata:
  id: funnel-workshop
  aliases: [od-workshop-facilitation]   # former name (naming convention, 2026-11-11)
  tier: practice
  lane: [lane-2, lane-3]
  new_state_lane: "Extension, deepens Lane 2 (21), Lane 3 front-end (31)"
  new_state_step: "Capture the idea, process diagnostics; Requirements engineering"
  owner_role: human:jakob.gabriel
  authority_level: draft
  status: draft
  requires: [dept-context]
  composes: [funnel-use-case, dept-intake, bc-portfolio, bc-build, funnel-requirements, mi-data-availability, invest-screen, catalog-standardization, mi-equipment, deploy-cybersec, funnel-first-aid]
  okf:
    type: Agent Skill
    title: Workshop facilitation
    tags: [use-case-support-service, practice, workshop]
---
# Workshop facilitation

- Read `dept-context` first.
- Authority: **draft**. The DBVE facilitates, the Plant ME owns the plant side, and nothing is committed in the room (investment, equipment integration and external connection are other decisions).
- **Outputs:** [`references/outputs.md`](references/outputs.md) lists what this skill must deliver, to whom, and when each output is complete.

## Purpose

- Prepare, run and close a workshop so that demand, a savings pre-evaluation and tool and machine needs end up in one sheet and then in a follow-up list with owners.
- It produces four things: agenda, pre-read, capture sheet, follow-up list.

## Terms (one name per format)

| Name used here | When |
|---|---|
| Use Case Definition Workshop | Plant onboarding or a new demand wave |
| Use Case Integration Workshop | A use case is ready for integration |
| Machine Integration Workshop | Machine connectivity is the need |

- Other formats OD has run (equipment integration, combined, savings) are in `references/workshop-formats.md`; "workshop" alone means any of them.

## Inputs and output

| | Content |
|---|---|
| Needs | Plant, requested format, plant owner (role), existing use case list, tool availability, machine list and connectivity status |
| Produces | Agenda and pre-read, filled capture sheet, follow-up list and summary for the Plant ME |

## Procedure

- Copy this checklist and tick it off:

```text
[ ] 1-6   Before: format, purpose, audience, plant file, pre-read, wait states
[ ] 7-11  During: days, capture live, savings pre-evaluated, light ranking, disagreement logged
[ ] 12-15 After: summary, routed items, owners and dates, utilization session booked
```

### A · Before

1. **Pick the format** from [`references/workshop-formats.md`](references/workshop-formats.md).
   - Which comes first, a Machine Integration Workshop or a Use Case Definition Workshop, depends on the plant: machine integration first when connectivity is missing, use case first when machines are connected.
   - Write the reason for the order into the pre-read; confirm with the OD lead where an agenda fixes an order.
   - If the plant has an ad-hoc process issue and no use case, it is not a workshop; use `funnel-first-aid`.
2. **State purpose and timeframe** in the style of OD's agenda slide: a short purpose list (what is defined, what status is followed up, what is prioritized, what project it starts) and a window agreed with the plant.
   - See the plant-agenda example in the formats reference.
3. **Fix the audience.** The standard agenda marks each item Required or Recommended for: Project Manager MSB, Machine Integration Lead, Quality, Production, CBS, IT.
   - Open slide 2 of the Standard Agenda deck for the per-item matrix.
   - Add the Plant ME, the plant owner of any use case already on the list, OPEX and Engineering for utilization sessions.
4. **Prepare the plant file.** Existing use case list for the plant, case groups where the plant is white space or has Delivered use cases (`bc-portfolio`), the plant's tool availability table, machine list and connectivity status.
   - Tools to check: IIoT Edge, MSB/MQTT broker, rule engine, MES, QFPR, recipe management, image library, Data Science Factory.
   - Check tool availability because a tool demoed at a plant is not the same as a use case being in scope there (`dept-intake`, refusal playbook).
5. **Send the pre-read** from [`assets/workshop-agenda-and-preread.md`](assets/workshop-agenda-and-preread.md): agenda, purpose, blank Use Case Canvas, savings pre-evaluation template with examples, utilization template, priority machines to have ready, who attends which day.
6. **Name the wait states** you must not promise around.
   - Cyber Security sign-off runs in parallel and blocks only the go-live of an external machine connection; start the package early (`deploy-cybersec`).
   - Investment approval is a separate human decision.

### B · During

7. **Day structure for a Use Case Definition Workshop** (OD Standard Agenda; check the deck for the current version):
   - Day 1 introduction: OD and its service lines, tools, use case creation process, use case library, analytics use case library.
   - Day 2 definition: plant tour with focus on priority machines; collection of use case demand.
   - Day 3 detail evaluation: savings pre-evaluation of found use cases; assessment of Smart Factory tools needed; assessment of machine integration demands.
   - Trim days the plant already knows. The earlier interactive variant uses six creation steps (machine integration, data availability, data standardization, data integration, dashboard creation, use case utilization).
8. **Capture live, in one sheet** ([`assets/workshop-capture-template.md`](assets/workshop-capture-template.md)).
   - For each demand run the questions of the `funnel-use-case` questionnaire; do not define a duplicate of something already logged.
   - Check the library before drafting from a blank page.
9. **Savings: pre-evaluate, do not promise.** Use OD's pre-evaluation template and mark each figure with its basis (calculated, estimated or none); make tool recommendations only against a named use case.
   - Past summaries carried "Savings Estimation for Use Cases: open task", and fitting the calculation into the agenda stalled it (`bc-build`).
   - So book the calculation as a follow-up with OD's calculator and fix the date in the room.
10. **Rank lightly.** Use the standard agenda's classification: highest generalization potential, highest saving potential; custom use cases per plant may need extra budget. Leave the full ranking to `bc-portfolio`.
11. **Record disagreement.** If participants describe the same need differently, that is several use cases (`funnel-use-case`); log them separately.

### C · After

12. **Summarize within the follow-up window** in the shape of OD's summary decks.
   - Content: tool availability with recommendation; top three or four use cases by current priority per process; next steps split into local and central.
   - Skeleton in [`assets/workshop-follow-up-list.md`](assets/workshop-follow-up-list.md). The window is not set anywhere; agree it with the OD lead.
13. **Route every item**: use case to definition or `dept-intake`; machine need to `mi-equipment` or the Information Integration lane; savings to `bc-build`; ranking to `bc-portfolio`; standard candidates to `catalog-standardization`; ad-hoc issues to `funnel-first-aid`.
14. **Give each follow-up an owner role and a date, or mark it open.** An item with no owner is not a follow-up.
15. **Ask for utilization feedback at the next visit.** Integration workshops end with a utilization session (who uses it, how often, which actions); schedule it.

## Example

```text
Capture sheet row (fictional):
Need:        Stop reasons are collected on paper at the end of the shift
Moment:      Daily Gemba          Already logged: no       Library precedent: Downtime Reporting
Category:    standard per process Plant owner (role): Production lead
Savings:     first figure "open"  Basis: none (pre-evaluation only)
Follow-up:   OD calculates with the calculator   Owner role: DBVE   Date: set in the room
```

## Human gate and AI-agent notes

- The DBVE facilitates; the Plant ME confirms the plant side; the OD lead decides lead times and formats not in the standard agenda.
- An agent drafts agenda, pre-read, capture sheet and follow-up list from the plant file; it never commits investment, integration or a connection.
- Every figure it writes carries its basis; unknowns stay marked not recorded.

## Definition of done

- Purpose, audience and timeframe were agreed with the plant; the pre-read went out.
- The capture sheet is filled and legible to someone who was not present; every demand is logged against the plant roadmap or returned with a reason.
- The follow-up list has owner roles, dates or explicit "open"; the summary reached the Plant ME.

## Pitfalls

- Do not leave the room with savings figures that have no basis; record them as pre-evaluation, because an unfounded number gets quoted later.
- Do not accept a use case on a tool that is not available at the plant without recording the rollout dependency.
- Do not commit machine integration, investment or an external connection in the room; those are other decisions.
- Do not define a duplicate of a logged use case; check the list first.
- Do not name individuals in the record; use roles. Do not paste credentials, hostnames or addresses.
- Do not try to calculate savings in the workshop; it stalled past agendas.

## Outputs

- [`outputs.yaml`](outputs.yaml): required outputs, criteria, checks and sign-offs.
- One run record per call: `python scripts/run_record.py new <skill-id>` (registry root).

## References

| File | Open when |
|---|---|
| [`references/workshop-formats.md`](references/workshop-formats.md) | Step 1: choosing a format, or you need purpose lines, days, audience and typical outputs |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | Steps 4 to 11: order decision, IT-side preparation checklist, in-room practices, utilization table, handoff contract |
| [`assets/workshop-agenda-and-preread.md`](assets/workshop-agenda-and-preread.md) | Step 5: agenda skeletons per format and the pre-read checklist |
| [`assets/workshop-capture-template.md`](assets/workshop-capture-template.md) | Step 8: the sheet filled during the workshop |
| [`assets/workshop-follow-up-list.md`](assets/workshop-follow-up-list.md) | Step 12: the follow-up list and summary skeleton |
| [`references/background.md`](references/background.md) | You need provenance, the open questions (template, lead times, outcomes) or the output table; never an instruction |
| [`evals/evals.json`](evals/evals.json) | Test cases and trigger queries to run with and without this skill |
