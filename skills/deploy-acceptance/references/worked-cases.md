---
type: Skill Reference
title: Worked cases
description: Guidance, no figures. Seven illustrative case patterns read as acceptance questions - what the record typically shows, what an acceptance would have to evidence, and what stays open - for protocol authors who want a concrete picture of a pass, a conditional pass or a fail. Plants and values are placeholders.
resource: ../SKILL.md
status: draft
tags: [information-integration-service, practice]
---

# Worked cases

These are **illustrative patterns**, drawn from kinds of records the knowledge base holds. They are not
acceptance protocols from the department: none exists in the knowledge base (see the open item in
`acceptance-by-route.md`). Plants, counts and dates are placeholders
(`<plant>`, `<n>`); look up the real record before applying a case. Each case says what the
**record pattern** looks like and what the **reading** is.

## Case 1: A delivered Process Values use case with no recorded saving

- **Record pattern.** A plant note shows many machines edge-routed, a share of them without
  an integration status, blocker text on others; the use case list shows a productive
  Process Values use case flagged scalable with the saving "not recorded". In its case group
  the "Baseline and KPI" row reads *Not recorded*.
- **Reading.** A productive use case at a plant where many machines have no recorded status
  cannot show which machines feed it. Acceptance would have needed the machine list for the use
  case (the data path "written down to the machine", per the *Handover* note), the baseline
  (scrap, downtime or reporting hours) and the plant owner's use in a real shift.
- **Use.** Items 2 and 3 of `acceptance-by-route.md` §1 and the
  baseline item in `cluster-acceptance-criteria.md`.

## Case 2: A dry run recorded as "not productive" (image pilot)

- **Record pattern.** Tool note `MIL 1.0` (archive-based, AI-drafted) describes a dry run of
  the data-logging and transfer tool as "not productive"; metadata storage and image
  availability exist "in theory" with documentation; live operation had not started; a firewall
  change request was raised but not tested; the tool is not yet deployed on the edge platform;
  the stated priority is images in the blob store of the OESL data lake.
- **Reading.** A clean example of the difference between "tested" and "accepted". Several
  conditions would have to flip before a SAT/SIT: the tool on the edge platform, the firewall
  change tested, images in the target store, live operation. A dry run on a test path is the
  FAT-equivalent, not the gate (`test-structure.md`).
- **Use.** Never count a dry run as an acceptance item; list the unflipped conditions as
  open findings in section 4 of the protocol.

## Case 3: Productive only after a security approval (QFPR rollout)

- **Record pattern.** Tool note `QFPR` (archive-based): test instances at several first-mover
  plants; cyber-security approval pending and "treated as mandatory before any productive (not
  just test) rollout", at the vulnerability-scan and penetration-test stage with Group IT;
  development delayed or stalled pending purchasing at some plants. The Tool Overview rows
  differ between plants (available at one, ongoing at another).
- **Reading.** The acceptance gate has a precondition outside the build: the security approval.
  The protocol's first section should say whether the instance is a test instance or a
  productive one, and the approval reference should be an item.
- **Use.** Item 6 of §1 in `acceptance-by-route.md`; the cyber gate is `deploy-cybersec`.

## Case 4: Integrated machines carrying open firmware blockers

- **Record pattern.** The Machine List shows rows with the blocker "Patching of the firmware due
  to cyber security", mostly on S7-1200 controllers, some of them recorded as `INTEGRATED`,
  others ongoing; a batch of rows with one planned integration date, some `INTEGRATED`, some
  `INTEGRATION ONGOING`.
- **Reading.** The acceptance skill states that "a partial pass is not a pass". Either the
  blocker is stale and the row should be cleaned, or the machine was accepted with an open
  item. The protocol must say which.
- **Use.** Item 8 of §1; ask the Plant IT whether a patch window exists.

## Case 5: A traceability flow (process values to per-part test results)

- **Record pattern.** Tool note `RuleEngine 2.0` (archive-based; ODEC slide): a flow turns
  process values arriving over MQTT into a relational table view, with named instances for
  test stations (for example a leak test, a flow test and an end-of-line test), so that an hourly
  production overview can be drilled down to quality and process results per serial part.
- **Reading.** The acceptance question is the drill-down, not the flow: take a serial number
  from the hourly overview, find its test results, and check them against the stations' own
  records. That is a UAT scenario tied to the benefit (C07 one up, one down, and C03).
- **Use.** `cluster-acceptance-criteria.md` C07; write the
  serial number used in the evidence column.

## Case 6: A migration accepted location by location (energy management)

- **Record pattern.** Tool note `Energy Management 2.0`: migration of WiriTec instances from
  one hosting domain to another, tracked location by location with a colour-coded checklist
  and a per-location cutover with a planned outage while logger devices are reconfigured.
- **Reading.** A pattern for a repeatable acceptance: one checklist, one result per location,
  the outage window planned. The department's note does not record the checklist items.
- **Use.** Section 5 of `acceptance-by-route.md`; ⟨the checklist itself. Who could supply it:
  the energy tool owner.⟩

## Case 7: Integrated but not documented

- **Record pattern.** A plant's Machine List shows nearly all machines `INTEGRATED` (most with
  one integration year), PLC model and network protocol blank on every row, route blank on most;
  one connector is recorded as connecting a group of OPC machines of one vendor; another
  vendor's machines have no available connector and yet are integrated with no route recorded.
- **Reading.** An acceptance protocol that was never written back to the Machine List
  leaves the next engineer unable to tell how any of these machines delivers data. That is the
  failure "the protocol itself is the source system" is meant to prevent.
- **Use.** Items 2 and 3 of §1; when re-opening such a plant, fill one protocol per route family
  (by vendor) rather than per machine, and name the connector chain.

## What the cases have in common

1. Every case turns on a **condition outside the build**: a security approval, a patch window, a
   firewall change, a Machine List write-back, a baseline.
2. In none of them does the record show who accepted what. The acceptance/rework rate is
   "not captured in any system" (`mi-equipment` (`../../../skills/mi-equipment/references/od-information-integration-service/procedure.md`)).
   Start capturing it with the next protocol.

## Sources

- Knowledge base `Graph/Plants`, `Graph/Machines`, `Case Groups/CG-02`, and `Graph/Tools` notes `MIL 1.0`,
  `QFPR`, `RuleEngine 2.0`, `Energy Management 2.0`, read 2026-11-05.
- Department note *Handover* (`_knowledge/10-Department`).
