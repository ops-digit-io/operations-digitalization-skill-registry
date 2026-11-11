---
type: Skill Reference
title: Estate patterns
description: How to read the Machine List for barrier patterns - where NOT INTEGRATED clusters by vendor, protocol and plant, how to group recorded blocker texts by class, and the data gaps that make triage impossible. Guidance and live-count recipes; no figures.
resource: ../procedure.md
status: draft
tags: [information-integration-service, practice, aggregate]
---
# Estate patterns

How to read the `Machine` records (Machine List, or the machine nodes in the knowledge-graph export) as patterns, not
one by one. Counts describe what was recorded, not what is true on the line. **This file carries no counts:** run the
recipes below on the live list and quote the result with its date. The connector set is summarised in
`od-equipment-integration` (`connectors`).

## Status: four values, not three

| Integration status | Read it as |
|---|---|
| `INTEGRATED` | Recorded as connected |
| `NOT INTEGRATED` | A state, not a failure; may simply have no demand yet |
| `INTEGRATION ONGOING` | In flight |
| No status recorded | Nobody has classified it; often a large group |

Count all four on the live list. A triage that counts only `NOT INTEGRATED` misses machines nobody has classified;
the blank group is usually larger than the ongoing group and is a data-quality finding in itself.

## Where `NOT INTEGRATED` sits

Recipe: group the Machine List by PLC vendor, and per vendor count all machines, `NOT INTEGRATED` and `INTEGRATED`
(plus the blank-status remainder). Do the same by field network (protocol) and by plant.

What to expect, qualitatively:

- **The big vendors dominate the absolute numbers**, so compare rates, not counts. A vendor with few machines and
  every one `NOT INTEGRATED` is a stronger barrier signal than a big vendor with the same absolute count.
- **Vendors at the bottom of the difficulty ranking** (`barrier-classes`) show up as near-total `NOT INTEGRATED`, and
  the table agrees with the ranking there.
- **A vendor high in the ranking can still show a high integration rate** because it was integrated through a
  historical aggregation route, not because a *new* machine is easy. Do not use the rate to promise an easy machine.
- **A vendor may appear twice** under slightly different names (a separate "OPC" entry for the same maker); normalise
  before comparing.
- **Protocol:** serial and legacy fieldbus networks (PROFIBUS, MPI) are the typical weak spots; a protocol with
  almost everything integrated through the aggregation route may still lack an edge connector - the "Modbus
  contradiction" in `barrier-classes`, not an easy protocol.
- **By plant:** `NOT INTEGRATED` usually concentrates in a few plants. A plant-level triage should start with the
  plants carrying most of the not-integrated machines and not spread evenly. Read the planned-method field
  (edge platform, central aggregation server, evaluation ongoing, none recorded) alongside; "none recorded" is a gap.

## What the recorded blocker texts say

Recipe: filter the integration-blockers field for non-empty text; group by keyword (your grouping, not a recorded
taxonomy); map each group to a class in `classes-and-routes`. Typical groups and their class:

| Group of text | Class (`classes-and-routes`) |
|---|---|
| Data model standardization | C7 |
| Firmware patching for cyber security; vulnerability to patch before integration | C3, and C2 or C6 behind it |
| Edge device notes (one device dedicated to a module, device for a standalone machine) | C4 (edge hardware planning) |
| Engineering-software version upgrade needed, "to be discussed with a plant" | `⟨class to confirm⟩`: the text does not say why the upgrade is required |
| Robot or laser-welding signals possibly available in the related machine or PLC | substitution, ladder rung 6 |
| Camera hardware and integration | substitution, rung 7 |
| PLC program missing or wrong; "when the PLC program is available, integration is possible"; no source code | C1 |
| PLC type unknown | facts first, then classify |
| Other: machine ids, copied hardware lists, unclear text | not classifiable |

Two traps follow. First, **most `NOT INTEGRATED` machines carry no blocker text at all**, so for them the reason is not in
the data and the triage has to collect it. Second, **the field is partly a history of blockers that were cleared**:
texts also sit on machines already `INTEGRATED`, so a recorded blocker is not proof the machine is stuck now.

## Gaps that stop a triage

Count, on the live list: machines with no PLC vendor, no network protocol, no PLC model, no part number. A machine
without protocol and model cannot be placed in the ranking or routed; the first action is a site visit or a Plant ME /
Plant IT answer, not a decision. Also check whether the `production criticality`, network-status and
cyber-security-status fields are populated at all - if they are empty for every machine, the "criticality" of the
assessment protocol has no data behind it in that export, and you must say so.

## Landscape facts the exits rely on

Read the `landscape` module (check its `last-verified` date) for: which plants run the IIoT Edge Platform and the data
platform offload; the known barriers recorded for strategic plants (typically "operations concepts missing for several
tools" and "limited internal IT knowledge"); which plants are MES-pilot plants (MES in progress, ERP / S4HANA
dependent); and where the Manufacturing Image Library is not yet deployed ("depends on the data platform; licensing to
clarify"). These are the C4 cases that go to strategy.
