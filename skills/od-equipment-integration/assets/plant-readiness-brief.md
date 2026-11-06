---
type: Skill Asset
title: Plant readiness brief
description: One-page form a local key user or IIAE fills before a plant integration conversation, a status request or a wave capital request (eCR) - the plant's row from the records, the flags to clear, and the open questions that only the plant can answer.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [information-integration-service, technical]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---

# Plant readiness brief

Fill this **before** the conversation, from the sources named in each section. It does not
replace [`assessment-protocol.md`](assessment-protocol.md) (Route A, machine by machine); it
prepares the plant-level picture that protocol starts from. Every number you copy in gets its
export date. Record counts come from [`../references/plant-integration-status.md`](../references/plant-integration-status.md)
and must be re-run on the live Machine List before they go into a decision.

## 0. Header

| | |
|---|---|
| Plant | |
| Prepared by (role) | Plant ME / Plant IT / IIAE |
| Date; Machine List export date used | |
| Occasion | plant start / wave capital request (eCR) / status request / use case blocked for machine data |

## 1. The plant's row from the records

| Item | Value | Source and date |
|---|---|---|
| Machine rows | | Machine List |
| Integrated / not integrated / ongoing / **no status** | | Machine List |
| Route recorded: edge / aggregation / evaluation ongoing / **blank** | | Machine List |
| Controller vendors (main ones) | | Machine List |
| Concepts available in the Tool Overview (1, 2, 3) | | Tool Overview |
| Machines routed to a concept the Tool Overview does not list for this plant | | compare the two rows |
| Blocker texts (kinds; count live) | | [`blockers-and-waves.md`](../references/blockers-and-waves.md) |
| Project reference(s) / wave | | Machine List |
| Legacy applications at the plant | | Legacy Application List |

## 2. Flags to clear (tick, then name who answers)

- [ ] Status blank on more than half the rows. Ask Plant ME for the true state per machine.
- [ ] Route blank on integrated machines. Ask which connector(s) read them (rule: the row
      names every connector in the chain).
- [ ] Vendor or model or protocol blank on integrated machines. A second engineer could not
      repeat the integration.
- [ ] Route `EVALUATION ONGOING` on machines nobody is evaluating. Close or decide.
- [ ] Blocker text on an `INTEGRATED` machine. Stale, or an open follow-up?
- [ ] Planned integration date in the past on a machine not integrated.
- [ ] No concept in the Tool Overview, yet machines are integrated. Correct the Tool Overview
      or the Machine List.

## 3. Pre-assessment tells (site, from [`barrier-classes.md`](../references/barrier-classes.md))

| Tell | Observed |
|---|---|
| Panel / cabinet condition | |
| Network cabinet and cabling: is there a usable drop near the machine | |
| Plant IT / ME contact responsive | |
| PLC type, interfacing, machine network topology | |
| PLC program available and under own control, or only the OEM can touch it | |
| Is the machine already on an OPC UA server (cheapest variant) | |

## 4. Questions only the plant can answer

| Question | Answer | Who |
|---|---|---|
| Which use cases are waiting for data from the not-integrated machines? | | Plant ME / DBVE |
| Is there a patch window for the firmware-patching blockers? | | Plant IT / OT |
| Does Cyber Security / OT sign-off exist for the external connections planned? | | Plant IT; `od-cybersec-gate` |
| Who is the Local OT Expert for the eCR? | ⟨role⟩ | Plant ME |
| What edge hardware is already in the plant? Check which edge device sizes are currently approved | | IIAE |

## 5. Hand-off

Machines in scope go to Route B ([`guidance-protocol.md`](guidance-protocol.md)), one document
per machine. Barriers with no route go to `od-barrier-triage` and the landscape module.
Investment input goes to `od-investment-input`. Open items stay here with a named role.
