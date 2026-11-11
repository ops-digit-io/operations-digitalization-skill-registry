---
type: Skill Reference
title: Cost lines
description: The cost lines an investment input pack can carry, where each line's figure must come from, and how to size a wave from the live machine records. Guidance only - no prices or estate figures.
resource: ../SKILL.md
status: draft
tags: [information-integration-service, practice]
---
# Cost lines

Rule: a line with no sourced figure carries `⟨not known: who can supply⟩`. This file holds no prices. Every
figure in a pack comes from a supplier quote, a catalogue entry or a business-case proposal that is read live,
and is copied with its scope and date. Nothing here is a price list or a quote.

## Where cost shows up in an integration

`od-equipment-integration`, decision paths, gate 3 ("the preparation gates, in the order they bite"), names
the **budget** block first: *edge device and OT hardware; IT infrastructure and licences*. "Budget fails:
wave slips; nothing technical is wrong." The edge pattern adds that the cost sits in hardware, cabinet work
and a shopfloor network drop. The lines below follow from those two statements and from the fallbacks.

| Line | Applies when | Where the figure comes from | Who can supply |
|---|---|---|---|
| Edge device (large) | variant 1 (edge device) or the bridge in variant 3 | Supplier quote. Only the **large** device is approved; there is no approved small edge device (decision paths, edge-device hardware) | IIAE |
| OT hardware (cabinet work, power, network drop, protocol gateway for a PLC without Ethernet) | cabinet or network work is needed | Supplier quote or plant maintenance estimate | Plant ME / Plant IT, IIAE |
| IT infrastructure and licences | aggregation server, edge runtime, tool licences | Plant IT quote; the owner of external tooling and licensing decisions is open in the risk register | Plant IT, OD lead |
| Connector development | no route exists (for a controller family or equipment type whose connector is only an idea or in development, check the connector catalogue for the current state) | Development estimate; lead times for OT and IT cyber-security approvals are described as "high" (fallbacks), no number | IIAE |
| PLC program from the machine supplier | program unavailable (fallbacks, item 1) | Supplier; the work takes weeks and sometimes a commercial negotiation | Plant ME, supplier |
| PLC program change | nobody can change it (fallbacks, item 2) | A resourcing and scheduling block, line stop needed | Plant ME |
| Sensor or camera added instead of reading the machine | fallbacks, item 1, last rungs | Supplier quote; see "Reference figures" below | IIAE, Plant ME |
| Cyber Security / OT review | external connection | No figure; bundling it with the wave is the department's own bet (strategy B2) | `od-cybersec-gate` |
| Training and rollout | rollout of a tool or app | Look up with `od-rollout-training` | `od-rollout-training` |
| Internal effort (OD, plant) | always | Not priced in the sources; some notes take cost as zero by an owner statement, which is a convention of that note and not a rule for this pack. Whether the pack prices it is `⟨OD lead decision⟩` | OD lead |

## Reference figures: where to look, not what they are

Cost references exist for **tools and business-case proposals**, not for connecting a machine. Look them up live
and copy them only with scope and date; never carry a figure from memory or from an older pack.

| Kind of reference | Where to read it | Caveat |
|---|---|---|
| Tool catalogue cost notes (app development per plant, deployment, one-time connectors for camera systems) | the tool catalogue as recorded in `od-system-fit-check` (tool boundaries) | Scope per plant or per tool; check the date; the tool's status can be a live discrepancy in the registry, so confirm status first |
| Energy-system rollout examples | same source | A rollout example at one plant, not a price list |
| Sensor-retrofit heuristic per machine, with a stated real range depending on PLC vendor, sensor type and edge-connectivity needs | Department knowledge base | An internal heuristic marked "refine per machine class"; a proposal in the AI-at-Operations list, not an approved budget |
| Legacy PLC migration programme range | Department knowledge base | A business-case proposal with a confidence label; not approved |

The business-case entries belong to a separate portfolio ("AI at operations"); the Case Groups overview says that
set was not merged with the plant use cases. Use them to show the order of magnitude of a substitution or
retrofit option next to a connection option, and mark them as proposals.

## How big is the wave

Size the wave from the live machine records (bundle file `kg_nodes.csv`, or the machine list it is exported from).
Use it as a plausibility check on the demand filter, never as the scope. Re-count on the live list and quote the
read date.

| Slice to count | How |
|---|---|
| Integration status | Group by status (`INTEGRATED` / `NOT INTEGRATED` / `INTEGRATION ONGOING`). A blank status is not "not integrated": report blanks separately and ask who owns the record |
| Priority of the not-integrated machines | Group by integration priority; keep blank as its own group |
| Planned method of the not-integrated machines | Group by planned method (IIoT Edge Platform / Central Aggregation Server / evaluation ongoing / blank) |
| Controller vendor of the not-integrated machines | Group by PLC vendor; the vendor mix decides which connectors and gateways the wave needs |

Two readings follow. A machine planned for the **edge platform** is where edge-device lines apply; one planned for
the **aggregation server** needs no device in its cabinet but still needs the edge somewhere (decision paths,
gate 3). On delivery rate: read the lane's monthly target and the actual from `od-equipment-integration`; if the lane
is not the constraint, a delayed wave points at budget, infrastructure or the PLC program.

## Spend already visible as a gate

`od-benefit-calculation` records dependencies on saving rows: `ECR APPROVAL`, `ECR CREATION` and
`MACHINE INTEGRATION` are the values that mark an open spend or integration gate. Filter the live ledger on the
dependency field and re-count before quoting. The spend gate is a recorded reason a booked saving is not yet real.
