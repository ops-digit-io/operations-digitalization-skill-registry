---
type: Skill Reference
title: Blockers and waves
description: Guidance for reading the recorded integration blocker texts by kind, how integration waves and the eCR step are recorded, and where the department roadmap figures live - how to count and interpret, with no company figures.
resource: ../SKILL.md
status: draft
tags: [information-integration-service, technical]
---

# Blockers and waves

Two things a plant key user is asked about at every roadmap conversation: "what is stopping
the remaining machines?" and "which wave is this machine in?". The Machine List holds both
as free text. This reference says how to read them as a whole.

**This file holds no counts, plant statuses or dated roadmap figures.** Those were a snapshot and
go stale. Count live on the Machine List (and read the cited slides at their source) before quoting.

**Evidence grades used here.**

- **Record**: read from the `Graph/Machines` notes or the live Machine List export.
- **Staging (unverified)**: facts from the knowledge base's `ODEC Facts` folder, extracted by AI from
  ODEC and CoP call slides, "not reviewed by a human". Open the cited slide in the archive
  before relying on it.
- **Rule**: marked as such, with its source.

## 1. Reading the blocker texts

The field is `integration_blockers` (free text in the Machine List export). Only a minority of
rows carry a value, and the texts cluster in a few plants. To count: filter the field for
non-blank, group by plant and by status, then classify each text with the table.

| Kind | How to recognise it | What to do |
|---|---|---|
| Data model standardization | "Data model Standardization (CT Base)"; often recorded on rows whose controllers differ and that are often already `INTEGRATED` | A data-model decision, not a connectivity problem; see `mi-signals` |
| Firmware patching for cyber security | "Blocking Point: Patching of the firmware due to cyber security"; typically S7-1200 | An OT patch window and an owner for the patch; cyber security gate |
| TIA V16 to V17 | "TIA V16 Upgrade necessary for TIA V17"; typically S7-1500 and S7-1200, `NOT INTEGRATED` | An engineering-software upgrade, discussed with the plant that already did it |
| Cyber-security vulnerability | "Needs to be patched before integration"; typically S7-1500 | Patch first, then integrate |
| Edge device allocation or hardware | "1x Edge Device dedicated to Module n needed"; "1x Edge Device (PROFIBUS / cifx) as actual machine"; "both machines connected to 1 Edge Device"; "Edge (together with camera)"; "Camera Hardware and Integration"; "no Edge device needed - S7-NET connector, due to manual operations within cell" | A cell-design decision: how many edge devices the plant buys (see the "approved edge device" constraint in [`SKILL.md`](../SKILL.md)) |
| PLC program or PLC identity | "PLC Program missing, was wrong"; "when PLC Program is available, Integration is possible"; "Timeline for PLC / HMI renewal needs to be checked"; "IM151-1 Standard: No PLC. Which PLC-Type is used?" | The PLC-program gate; see `fallbacks.md` |
| Not a blocker: labels, codes, numbers | Short codes such as "AC01", "BMM1", "M418", "GM", or bare numbers | Probably machine labels or counts typed into the wrong column; ignore, and tell the list owner |
| Pointers and comments | "see: ..." another machine; "Is part of Laser Welding Machines similar to KUKA Robots"; "see Planner Board regarding multiple sub plc programs" | Follow the pointer; not a blocker by itself |

How to use this:

1. **Several of the most common classes are not connectivity problems.** Data-model
   standardization, firmware patching and the TIA upgrade need a data-model decision, an OT
   patch window and an engineering-software upgrade respectively. This repeats what
   `barrier-classes.md` says.
2. **A blocker text on an `INTEGRATED` machine is not a stop.** Read it as an open follow-up, or as
   stale text, and ask which. Do not count it as the reason the plant is stuck.
3. **A long blocker list at one plant is often one cell design.** The edge allocation notes say, in
   effect, "a dedicated edge device per module" or "share one device between two machines". The
   decision is about how many edge devices the plant buys.
4. **Blockers sit on a small share of rows.** Most `NOT INTEGRATED` machines carry no blocker
   text; the reason for most of them is not recorded. Use the wave and project reference next,
   then ask the plant. ⟨Why the other `NOT INTEGRATED` machines are not integrated. Who could
   supply it: Plant ME / IIAE, per plant.⟩

**Rule (existing `barrier-classes.md`):** distinguish symptom from root cause before sizing a
fix. A firmware-patching text can mean no owner for the patch, no OT window, hardware that
cannot be patched, a missing program, or a vendor that no longer exists.

## 2. Waves and project references

The `project_reference` field is filled on a part of the rows. It names the project a machine
belongs to. To read it: group by the field and by plant, and compare against the status.

Patterns:

- **Two generations of project are visible.** Per-plant MSB rollout projects (earlier years) and
  the Machine Integration waves (later years). Some plants carry no project reference at all.
- **Some values are not project names.** A value shaped like a request identifier (for example
  `ADESAI-...`) is an identifier, not a project.
- **A wave is planned volume, not delivered volume.** A plant with many rows in a wave and many
  `NOT INTEGRATED` rows shows work still to do.
- **Integration dates by year.** Group rows by year of the integration date. Rows `INTEGRATED`
  without a date and not-integrated rows with a date are data-quality traps.
- **A scorecard count of integrated machines may not match the Machine List.** The KPI scorecard
  and the Machine List can count differently (date range, definition). ⟨Reconciliation of the two
  counts. Who could supply it: the owner of `OD-Report-Equipment_Integration`.⟩
- **Planned integration dates are filled on few rows,** and often are dates for a finished step,
  not a forward plan: compare them with the export date and the status.

## 3. The eCR step in a wave (process, staging, unverified)

From the ODEC Facts staging notes (`Plant - Carei`, `Other`, `Department KPIs`), which quote
slides of the ODEC and CoP calls:

- **"Machine Integration Next Wave: Process Overview (Milestone 1: eCR)"**: step 1 exchange call
  with the Local OT Expert about the next machines; step 2 prepare the eCR with the Local OT Expert
  "as per planned budget"; step 3 upload the eCR with the local team; step 4 close-loop
  communication until the eCR is approved. The wave slides list plants per quarter; request order sets
  eligibility and central capacity goes first to staffed first-mover plants.
- **Status slides** carry per-plant states for each wave (kick-off done, delayed, at risk, eCR
  approved, in implementation) and cost figures that cannot be assigned to a plant from the
  extracted text (see `vendor-protocol-routes.md`). Read the current
  status slide; do not quote an old one.
- **Pre-planning rule:** pre-planning is based on use case identification; eligibility follows request
  order to use the given budget at its best; redistribution based on on-going use case identification is possible.
- **Regional roadmap slides** list plants as "Done in site", "Done remote" or "Pending: ..."
  (for example "Pending: data lake integration?"). Read the latest slide.

What this means for a key user: the eCR is the approved-budget step before execution
(`execute-with-approval`, Tandem with Plant ME / Plant IT in [`SKILL.md`](../SKILL.md)). The
wave slides show that the Local OT Expert is the plant's counterpart for choosing the
machines. ⟨The eCR template and the cost calculator. The Triage note records "a
machine-integration eCR cost calculator" among the unclassified slides; the file itself is not
in the knowledge base areas read. Who could supply it: OD lead.⟩

## 4. Department numbers next to the Machine List (where they live)

The historical ODEC series carried recurring figures: target versus actual integrated machines, implemented
use cases, regional plan versus actual, machines connected, tags or datapoints, energy sensors,
use cases deployed. Each slide is staging, unverified.

- Do not quote a figure from memory. Open the latest slide of the series and quote it with the
  slide date.
- The Machine List's count of integrated rows and the slides' "machines connected" are not the
  same measure and are not reconciled in any note read. ⟨Definition of "connected" behind each.
  Who could supply it: OD lead.⟩

## 5. Other recorded stoppers that are not in the Machine List (patterns)

| Kind of dependency | What the record shows | Grade |
|---|---|---|
| Image or vision pilots | A data logging or transfer tool tested only in a dry run, "not productive"; a firewall change request raised but not tested; the tool not yet deployed on the edge platform; a vision system whose connection to the MSB is the stated blocker, with reports and images pulled by manual download in the meantime | Tool note `MIL 1.0` (archive-based, AI-drafted, not reviewed) |
| Apps waiting on cyber-security approval | Approval "treated as mandatory before any productive rollout", at vulnerability-scan / penetration-test stage; development delayed pending purchasing | Tool note `QFPR` (archive-based, AI-drafted) |
| Cloud migration of loggers | Each location cutover involves an outage while the logger devices are reconfigured | Tool note `Energy Management 2.0` (archive-based) |
| MSB assessment at a SCADA plant | IT/OT separation done; cyber-security assessment of the SCADA tool to follow; plan: inventory connected machines and use cases, bill of material for what is needed to bring current data acquisition onto the platform, non-invasive plan | ODEC Facts, staging |

Each row is the kind of dependency a key user finds only by asking. Add the relevant row to
the machine's record in `../assets/guidance-protocol.md`
when a machine depends on it.

## Sources

- Knowledge base `Graph/Machines`, `Graph/Plants`, `Graph/Tools`, read 2026-11-05.
- Knowledge base `ODEC Facts` folder: `Triage`, `Department KPIs and Roadmap Status`, `Plant - Carei`,
  `Plant - Auburn`, `Other` (staging, AI-extracted, not human-reviewed).
- Registry reference `barrier-classes.md` for the symptom-versus-root-cause rule.
