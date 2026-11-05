---
type: Skill Reference
title: Worked cases
description: Seven recorded cases from the plants and tool notes, each read as an acceptance question - what the record shows, what an acceptance would have had to evidence, and what stays open - for protocol authors who want a concrete picture of a pass, a conditional pass or a fail.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [information-integration-service, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---

# Worked cases

These are **not** acceptance protocols from the department: none exists in the vault (see
the open item in [`acceptance-by-route.md`](acceptance-by-route.md)). They are real records,
read from the acceptance side: "if this had been the artefact, what would the protocol have
needed to show?". Each case says which part is **record** (with source and date) and which is
**reading** (this analysis).

## Case 1: A delivered Process Values use case with no recorded saving (Karben)

- **Record.** Plant note, vault state 2026-11-05: Karben has 46 machines, all edge-routed; 23
  `INTEGRATED`, 23 without status; 22 machines carry blocker text. 36 use cases (productive 10,
  implemented 4, planned 4, idea 17, stopped 1), savings recorded 0 EUR. The Case Group
  *Process Values - Assembly* (CG-02, generated 2026-11-04) lists "Process Values Coolant Jacket
  Assembly" at Karben as `PRODUCTIVE`, flagged scalable, saving not recorded; in that group 15
  of 17 delivered cases carry no saving and the "Baseline and KPI" row reads *Not recorded*.
- **Reading.** A productive use case at a plant where half the machines have no recorded status
  cannot show which machines feed it. Acceptance would have needed the machine list for the use
  case (the data path "written down to the machine", per the *Handover* note), the baseline
  (scrap, downtime or reporting hours) and the plant owner's use in a real shift.
- **Use.** Items 2 and 3 of [`acceptance-by-route.md`](acceptance-by-route.md) §1 and the
  baseline item in [`cluster-acceptance-criteria.md`](cluster-acceptance-criteria.md).

## Case 2: A dry run recorded as "not productive" (Northeim image pilot)

- **Record.** Tool note `MIL 1.0` (archive-based, AI-drafted): a 10,000-image dry run of the
  data-logging and transfer tool is "not productive"; metadata storage and image availability
  exist "in theory" with documentation; live operation had not started; a labelling tool was
  tested against an annotation tool with a working interface; a firewall change request was
  raised but not tested; the tool is not yet deployed on the edge platform; stated priority:
  images land in the blob store of the OESL data lake.
- **Reading.** A clean example of the difference between "tested" and "accepted". Four
  conditions would have to flip before a SAT/SIT: the tool on the edge platform, the firewall
  change tested, images in the target store, live operation. A dry run on a test path is the
  FAT-equivalent, not the gate ([`test-structure.md`](test-structure.md)).
- **Use.** Never count a dry run as an acceptance item; list the unflipped conditions as
  open findings in section 4 of the protocol.

## Case 3: Productive only after a security approval (QFPR rollout)

- **Record.** Tool note `QFPR` (archive-based): test instances at Carei, Delicias, Monterrey and
  Somersworth through 2024; cyber-security approval pending throughout 2024 and "treated as
  mandatory before any productive (not just test) rollout", at the vulnerability-scan and
  penetration-test stage with Group IT by December 2024; development delayed at Waltershausen
  and stalled at Monterrey pending purchasing. Tool Overview export 2026-08-24: Waltershausen
  `AVAILABLE` 2021; Monterrey `ONGOING` 2023 ("eCR review and iteration done - December 2023").
- **Reading.** The acceptance gate has a precondition outside the build: the security approval.
  The protocol's first section should say whether the instance is a test instance or a
  productive one, and the approval reference should be an item.
- **Use.** Item 6 of §1 in `acceptance-by-route.md`; the cyber gate is `od-cybersec-gate`.

## Case 4: Integrated machines carrying open firmware blockers (Mako)

- **Record.** Machine List export 2026-08-21: Mako has 128 machines, 71 `INTEGRATED`, 5 ongoing,
  52 without status; 13 rows carry the blocker "Patching of the firmware due to cyber
  security" (10 on S7-1200), 8 of them recorded as `INTEGRATED`, 2 ongoing. Mako holds 17 rows
  with planned integration date 2023-12, 12 `INTEGRATED` and 5 `INTEGRATION ONGOING`.
- **Reading.** The acceptance skill states that "a
  partial pass is not a pass". Either the blocker is stale and the row should be cleaned, or
  the machine was accepted with an open item. The protocol must say which.
- **Use.** Item 8 of §1; ask the Plant IT whether a patch window exists.

## Case 5: A traceability flow (Monterrey, Tesla parts)

- **Record.** Tool note `RuleEngine 2.0` (archive-based; ODEC slide of May 2025): a flow turns
  process values arriving over MQTT into a relational table view, with named instances for a
  helium leak test, a flow test and an end-of-line test, so that an hourly production
  overview can be drilled down to quality and process results per serial part (serial numbers
  collected per hour and linked to each part's test result).
- **Reading.** The acceptance question is the drill-down, not the flow: take a serial number
  from the hourly overview, find its three test results, and check them against the
  stations' own records. That is a UAT scenario tied to the benefit (C07 one up, one down,
  and C03).
- **Use.** [`cluster-acceptance-criteria.md`](cluster-acceptance-criteria.md) C07; write the
  serial number used in the evidence column.

## Case 6: A migration accepted location by location (energy management)

- **Record.** Tool note `Energy Management 2.0`: migration of WiriTec instances from
  ContiTech-managed to OESL-managed servers, tracked through 2025; 13 of 17 locations done by
  2025-10-20; a per-location, colour-coded checklist and a per-location cutover with about a
  day's outage while logger devices are reconfigured; recent completions named: Somersworth and
  Ponta Grossa, Changshu, Ostrava.
- **Reading.** A pattern for a repeatable acceptance: one checklist, one result per location,
  the outage window planned. The department's note does not record the checklist items.
- **Use.** Section 5 of `acceptance-by-route.md`; ⟨the checklist itself. Who could supply it:
  the energy tool owner.⟩

## Case 7: Integrated but not documented (Northeim)

- **Record.** Machine List export 2026-08-21: 87 machines, 83 `INTEGRATED` (72 with integration
  date 2023), PLC model and network protocol blank on all 87 rows, route blank on 73;
  connectors: `SFT-OPC-Suite` is recorded as connecting the 24 Bachmann OPC machines; Engel
  has no available connector and 31 Engel machines are integrated with no route recorded.
- **Reading.** An acceptance protocol that was never written back to the Machine List
  leaves the next engineer unable to tell how any of these machines delivers data. That is the
  failure "the protocol itself is the source system" is meant to prevent.
- **Use.** Items 2 and 3 of §1; when re-opening Northeim, fill one protocol per route family
  (Engel, Bachmann, Siemens) rather than per machine, and name the connector chain.

## What the cases have in common

1. Every case turns on a **condition outside the build**: a security approval, a patch window, a
   firewall change, a Machine List write-back, a baseline.
2. In none of them does the record show who accepted what. The acceptance/rework rate is
   "not captured in any system" ([`od-information-integration-service`](../../od-information-integration-service/SKILL.md)).
   Start capturing it with the next protocol.

## Sources

- Vault `Graph/Plants/Karben`, `Graph/Machines` (Mako, Northeim rows), `Case Groups/CG-02`, and
  `Graph/Tools` notes `MIL 1.0`, `QFPR`, `RuleEngine 2.0`, `Energy Management 2.0`, read 2026-11-05.
- Department note *Handover* (`_knowledge/10-Department`).
