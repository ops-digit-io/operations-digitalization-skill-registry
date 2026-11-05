---
type: Skill Reference
title: Cost lines
description: The cost lines an investment input pack can carry, which have a recorded figure in the sources (with scope and date) and which are open, plus the size of the machine estate a wave draws on.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [information-integration-service, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Cost lines

Rule: a line with no sourced figure carries `⟨not known: who can supply⟩`. The figures below are the only
ones the sources gave; none is a price list and none is a quote.

## Where cost shows up in an integration

`od-equipment-integration`, decision paths, gate 3 ("the preparation gates, in the order they bite"), names
the **budget** block first: *edge device and OT hardware; IT infrastructure and licences*. "Budget fails:
wave slips; nothing technical is wrong." The edge pattern adds that the cost sits in hardware, cabinet work
and a shopfloor network drop. The lines below follow from those two statements and from the fallbacks.

| Line | Applies when | Figure in the sources | Who can supply |
|---|---|---|---|
| Edge device (large) | variant 1 (edge device) or the bridge in variant 3 | `⟨not recorded⟩`. Only the **large** device is approved; "no approved small edge device available" (decision paths, edge-device hardware) | IIAE, supplier quote |
| OT hardware (cabinet work, power, network drop, protocol gateway such as a Helmholz NetLink for a PLC without Ethernet) | cabinet or network work is needed | `⟨not recorded⟩` | Plant ME / Plant IT, IIAE |
| IT infrastructure and licences | aggregation server, edge runtime, tool licences | `⟨not recorded⟩`; the owner of external tooling and licensing decisions is open in the risk register | Plant IT, OD lead |
| Connector development | no route exists ("Integration of Other PLCs"; the B&R, Bachmann, Engel, Zwick, SMB and SmartKlaus connectors are Idea or Development, not available) | `⟨not recorded⟩`; lead times for OT and IT cyber-security approvals are "high" (fallbacks, item 5), no number | IIAE |
| PLC program from the machine supplier | program unavailable (fallbacks, item 1) | `⟨not recorded⟩`; "weeks and sometimes a commercial negotiation" | Plant ME, supplier |
| PLC program change | nobody can change it (fallbacks, item 2) | `⟨not recorded⟩`; a resourcing and scheduling block, line stop needed | Plant ME |
| Sensor or camera added instead of reading the machine | fallbacks, item 1, rung 7 | see "Figures that exist" below | IIAE, Plant ME |
| Cyber Security / OT review | external connection | no figure; bundling it with the wave is the department's own bet (strategy B2) | `od-cybersec-gate` |
| Training and rollout | rollout of a tool or app | `⟨not recorded⟩` | `od-rollout-training` |
| Internal effort (OD, plant) | always | not priced in the sources; the Case Groups note takes cost as zero by an owner statement of 2026-11-04. Whether the pack prices it is `⟨OD lead decision⟩` | OD lead |

## Figures that exist, with scope

These are cost references for **tools and business-case proposals**, not for connecting a machine. Copy
them only with scope and date.

| Figure | Scope | Source and date |
|---|---|---|
| QFPR: app development about EUR 25k per plant; deployment about EUR 5k per plant if externally supported | Quality feedback app, per plant | January 2025 tool catalogue, as recorded in `od-system-fit-check` (tool boundaries) |
| MIL: connectors for different camera systems about EUR 5k to 10k, one time | Image library camera connector | same |
| WiriTec EMS: EUR 250k to 300k, one plant (Monterrey) | Energy system rollout example; the EMS status is a live discrepancy in the registry | same; confirm status first |
| Retrofit heuristic: "EUR 5K envelope" per machine, real range EUR 2K to 30K depending on PLC vendor, sensor type and edge-connectivity needs | Sensor retrofit decision (business case UC9, an internal heuristic, "refine per machine class") | Work vault `Graph/Business Cases/Sensor-Upgrade Decision Frame`, list item created 2026-05-13, export 2026-08-24; a proposal in the AI-at-Operations list, not an approved budget |
| PLC Evergreening: cost range EUR 0.4M to 0.8M (mid 0.6M) for a programme with one pilot site and five machines | A business-case proposal for legacy PLC migration | Work vault `Graph/Business Cases/PLC Evergreening`, same list and dates; confidence "Med"; not approved |

The last two belong to a separate portfolio ("AI at operations"); the Case Groups overview says that set
was not merged with the plant use cases. Use them to show the order of magnitude of a substitution or
retrofit option next to a connection option, and mark them as proposals.

## How big is the wave

Aggregate of the 1,715 machine records (bundle file `kg_nodes.csv`, read 2026-11-05). Use it as a
plausibility check on the demand filter, never as the scope.

| Slice | Count |
|---|--:|
| `INTEGRATED` / `NOT INTEGRATED` / `INTEGRATION ONGOING` / no status recorded | 821 / 395 / 48 / 451 |
| Of the 395 `NOT INTEGRATED`: integration priority 1 / 2 / 3 / 4 / 5 / blank | 89 / 150 / 95 / 5 / 19 / 37 |
| Of the 395: planned method IIoT Edge Platform / Central Aggregation Server / evaluation ongoing / blank | 225 / 58 / 57 / 55 |
| Of the 395: PLC vendor Siemens / Rockwell / Beckhoff / Delta / Bachmann / Philips / Mitsubishi | 232 / 58 / 22 / 14 / 10 / 9 / 8 |

Two readings follow. A machine planned for the **edge platform** is where edge-device lines apply (225 of
the 395); one planned for the **aggregation server** needs no device in its cabinet but still needs the
edge somewhere (decision paths, gate 3). On delivery rate: the lane target is 25 machines a month
(overshoot 30), and 338 against 331 on 2026-08-10 (`od-equipment-integration`); the lane is not the
constraint, so a delayed wave points at budget, infrastructure or the PLC program.

## Spend already visible as a gate

`od-benefit-calculation`: of 60 saving rows with a recorded dependency, `ECR APPROVAL` 14, `ECR CREATION` 6,
`MACHINE INTEGRATION` 6. The spend gate is a recorded reason a booked saving is not yet real.
