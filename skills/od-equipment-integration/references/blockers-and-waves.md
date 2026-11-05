---
type: Skill Reference
title: Blockers and waves
description: What the 110 recorded integration blocker texts say, grouped by kind and plant, how integration waves and the eCR step are recorded, and the department roadmap numbers that sit next to the Machine List - each marked as record count or as unverified staging.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [information-integration-service, technical]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---

# Blockers and waves

Two things a plant key user is asked about at every roadmap conversation: "what is stopping
the remaining machines?" and "which wave is this machine in?". The Machine List holds both
as free text. This reference reads them as a whole.

**Evidence grades used here.**

- **Record count**: counted from `Graph/Machines` notes (Machine List export 2026-08-21) on
  2026-11-05.
- **Staging (unverified)**: facts from the vault's `ODEC Facts` folder, extracted by AI from
  ODEC and CoP call slides, "not reviewed by a human". Open the cited slide in the archive
  before relying on a staging number.
- **Rule**: marked as such, with its source.

## 1. The 110 blocker texts (record count)

The field is `integration_blockers` (in the Machine List export: free text). 110 of 1,715 rows
carry a value. Plants: Caluire 23, Karben 22, Subotica 21, Mako 17, Tlalnepantla 12, San
Luis Potosi 6, Somersworth 4, Delicias 4, Timisoara 1. Status of the 110 rows: 40 integrated,
4 ongoing, 20 not integrated, 46 without status.

| Kind (grouping by this analysis) | Rows | Where | Wording in the record (quoted or shortened) |
|---|--:|---|---|
| Data model standardization | 23 | Caluire (all 23) | "Data model Standardization (CT Base)". 14 of these machines are already `INTEGRATED`, 8 `NOT INTEGRATED`, 1 ongoing |
| Firmware patching for cyber security | 13 | Mako (13) | "Blocking Point: Patching of the firmware due to cyber security"; 10 on S7-1200; 8 integrated, 2 ongoing, 3 without status |
| TIA V16 to V17 | 12 | Subotica (12) | "TIA V16 Upgrade necessary for TIA V17 - Discuss with Karben"; 11 on S7-1500, 1 on S7-1200; all `NOT INTEGRATED` |
| Cyber-security vulnerability | 5 | Tlalnepantla (5) | "Needs to be patched before integration"; all S7-1500; no status |
| Edge device allocation or hardware | 20 | Karben 13, Subotica 7 | "1x Edge Device dedicated to Module n needed"; "1x Edge Device (PROFIBUS / cifx) as actual machine"; "both BLM machines connected to 1 Edge Device"; "Edge (together with camera)" (5 Subotica rows); "Camera Hardware and Integration" (2); "no Edge device needed - S7-NET connector, due to manual operations within cell" (1); "both Laser Welding machines have 1 PLC and 2 Software Units, can be connected with 1 Edge Device" |
| PLC program or PLC identity | 6 | Karben 4, Subotica 2 | "PLC Program missing, was wrong"; "when PLC Program is available, Integration is possible" (2); "Timeline for PLC / HMI renewal needs to be checked"; "IM151-1 Standard: No PLC. Which PLC-Type is used?" (2) |
| Not a blocker: labels, codes, numbers | 26 | San Luis Potosi, Tlalnepantla, Somersworth, Mako, Delicias, Timisoara | "AC01", "BMM1", "M418", "GM", "4", "56" … Probably machine labels or counts typed into the wrong column |
| Pointers and comments | 5 | Karben | "see: …" another machine; "Is part of Laser Welding Machines similar to KUKA Robots"; "see Planner Board regarding multiple sub plc programs" |

How to use this table:

1. **Three of the four largest are not connectivity problems.** Data-model standardization
   (23), firmware patching (13) and the TIA upgrade (12) need a data-model decision, an OT
   patch window and an engineering-software upgrade respectively. This repeats what
   [`barrier-classes.md`](barrier-classes.md) says; the table gives the sizes and plants.
2. **A blocker text on an `INTEGRATED` machine is not a stop.** 40 of 110 blocker rows are on
   machines recorded as integrated (CT Base 14, firmware 8, edge or hardware 5, other 12, PLC
   program 1). Read them as an open follow-up, or as stale text, and ask which. Do not
   count them as the reason the plant is stuck.
3. **A 22-row blocker list is mostly one cell design.** At Karben the Edge allocation notes
   say, in effect, "a dedicated edge device per module" or "share one device between two
   machines". The decision is about how many edge devices the plant buys (see the
   "approved large edge device only" constraint in [`SKILL.md`](../SKILL.md)).
4. **Blockers sit on 6% of rows.** Most of the 395 `NOT INTEGRATED` machines carry no blocker
   text (only 20 do). The reason for most of them is not recorded: use the wave and project
   reference next, then ask the plant. ⟨Why the other 375 `NOT INTEGRATED` machines are not
   integrated. Who could supply it: Plant ME / IIAE, per plant.⟩

**Rule (existing `barrier-classes.md`):** distinguish symptom from root cause before sizing a
fix. A firmware-patching text can mean no owner for the patch, no OT window, hardware that
cannot be patched, a missing program, or a vendor that no longer exists.

## 2. Waves and project references (record count)

The `project_reference` field is filled on 687 of 1,715 rows. It names the project a machine
belongs to. The largest values:

| Project reference (as written) | Rows | Plants |
|---|--:|---|
| Machine Integration Next Wave 2 - 2025 | 154 | Subotica |
| Machine Integration Wave 2 - 2024 | 71 | Karben 32, Delicias 20, Carei 12, Changshu 7 |
| Machine Integration Wave 2 - Monterrey | 57 | Monterrey |
| ADESAI-202403190806-V1 | 29 | Qingdao (looks like a request identifier rather than a project name) |
| MSB Rollout Project - Somersworth / Waltershausen | 26 each | Somersworth, Waltershausen |
| Wave 2 | 19 | Monterrey 8, Ponta Grossa 11 |
| Machine Connectivity Wave 2 - 2024 | 18 | Changchun |
| MSB Rollout Project - Dolne Vestenice / Qingdao / Caluire / Timisoara / Vac | 19 / 18 / 17 / 17 / 16 | the named plants |
| SecureMix - 2025 | 17 | Hannover Stöcken |

Reading it:

- **Two generations of project are visible.** MSB rollout projects (2019 to 2024, one per
  plant, 16 to 26 machine rows each) and the Machine Integration waves (2024 onwards). Mako
  and Tlalnepantla carry no project reference on 99 and 82 rows.
- **The 2025 wave is one plant.** All 154 Next Wave 2 - 2025 rows are Subotica rows, and
  Subotica has 142 `NOT INTEGRATED` rows in total. The wave is planned volume, not delivered
  volume.
- **Integration dates by year (816 rows have one):** 2022: 77; 2023: 120; 2024: 123; 2025: 346;
  2026 up to the export date: 150. 7 `INTEGRATED` rows have no date and 2 not-integrated rows
  have one. The "338 integrated against a target of 331" figure in [`SKILL.md`](../SKILL.md)
  is a scorecard count; it does not match the 150 rows dated 2026 in this export.
  ⟨Reconciliation of the two counts. Who could supply it: the owner of
  `OD-Report-Equipment_Integration`.⟩
- **Planned integration dates are filled on 84 rows only** (Qingdao 48, Mako 17, Sun Prairie
  16, Changshu 1, Carei 1, Tanger 1). All are before the export date, and 63 of the 84 rows are
  already `INTEGRATED`: they were dates for a finished step, not a forward plan.

## 3. The eCR step in a wave (staging, unverified)

From the ODEC Facts staging notes (`Plant - Carei`, `Other`, `Department KPIs`), which
quote slides of the ODEC and CoP calls:

- **"Machine Integration Next Wave: Process Overview (Milestone 1: eCR)"**, slide dated
  2024-02-29: step 1 exchange call with the Local OT Expert about the next machines (calendar
  week 6); step 2 prepare the eCR with the Local OT Expert "as per planned budget" (CW 7);
  step 3 upload the eCR with the local team (CW 8); step 4 close-loop communication until the
  eCR is approved. The wave slides list plants per quarter with "First come first serve".
- **Status slide dated 2024-06-14:** kick-off with all input collected for Carei, Mako,
  Delicias, Monterrey, Ponta Grossa, Qingdao; "delayed" Karben, Changchun, Changshu; "at
  risk" Timisoara, Subotica, Northeim; eCR upload CW 11-12.
- **eCR status slide dated 2024-08-26:** three eCRs approved in the last month (Delicias,
  Monterrey, Ponta Grossa, "Wave 2"), one earlier approved and in implementation (San Luis
  Potosi, "Wave 1"), "Total: >187 Machines" for the Americas line. The slide also carries a
  cost figure that cannot be assigned to a plant from the extracted text (see
  [`vendor-protocol-routes.md`](vendor-protocol-routes.md)).
- **Slide dated 2026-02-02:** "Pre-planning based on use case identification; however, first
  come / first serve approach to utilize given budget at its best; redistribution based on
  on-going use case identification possible."
- **Regional roadmap slide dated 2025-11-19 (Americas):** "Done in site": Sun Prairie,
  Montemorelos, Tlalnepantla; "Done remote": Somersworth, Monterrey, San Luis Potosi, Ponta
  Grossa, Delicias; Auburn "Pending: data lake integration?".

What this means for a key user: the eCR is the approved-budget step before execution
(`execute-with-approval`, Tandem with Plant ME / Plant IT in [`SKILL.md`](../SKILL.md)). The
wave slides show that the Local OT Expert is the plant's counterpart for choosing the
machines. ⟨The eCR template and the cost calculator. The Triage note records "a
machine-integration eCR cost calculator" among the unclassified slides; the file itself is not
in the vault areas read. Who could supply it: OD lead.⟩

## 4. Department numbers next to the Machine List (staging, unverified)

Slides of the ODEC series; none re-checked. Quote with the slide date.

| Slide date | Statement as extracted |
|---|---|
| 2025-03-27 (2024 recap) | Target integrated machines 200, actual 145; 54 implemented use cases |
| 2025-08-19 (Q2 2025 KPI update) | Equipment integration "today (plan)": EMEA East 51 (63), EMEA West 95 (107), Americas 81 (85); APAC value cut off |
| 2025-10-15 (mid-year update) | "> 600 machines connected", "~ 350,000 tags / datapoints", "~ 1,300 energy sensors connected", "~ 200 use cases deployed" |
| 2025-10-20 | "Insight driven manufacturing": > 600 machines contribute process, machine and (partly) quality data; > 350,000 datapoints via IIoT and manufacturing data lake |

The Machine List export shows 821 integrated rows. The ODEC slides say "> 600 machines
connected". The two are not the same measure and are not reconciled in any note read.
⟨Definition of "connected" behind each. Who could supply it: OD lead.⟩

## 5. Other recorded stoppers that are not in the Machine List (record or staging, as marked)

| Where | What the record says | Grade |
|---|---|---|
| Northeim, image library pilot | Data logging/transfer tool tested with a 10,000-image dry run, "not productive"; firewall change request raised but not tested; the tool is not yet deployed on the edge platform; stated priority-1 requirement: images land in the OESL Datalake blob store | Tool note `MIL 1.0` (archive-based, AI-drafted, not reviewed) |
| Vac, Smart Klaus vision system | Connecting it to the MSB is the stated blocker for faster results; today reports and images are pulled by manual USB download with about a week's delay | Tool note `MIL 1.0` (same) |
| Quality feedback app (QFPR) | Cyber-security approval "treated as mandatory before any productive rollout", at vulnerability-scan / penetration-test stage by December 2024; development delayed at Waltershausen and stalled at Monterrey pending purchasing | Tool note `QFPR` (archive-based, AI-drafted) |
| Energy management (WiriTec) cloud migration | Each location cutover involves roughly one day of outage while the logger devices are reconfigured; 13 of 17 locations done by 2025-10-20 | Tool note `Energy Management 2.0` (archive-based) |
| Auburn, MSB assessment (2025-05-21) | IT/OT separation done; cyber-security assessment for the Ignition SCADA to follow; plan: inventory connected machines and use cases, bill of material for what is needed to bring current data acquisition onto the platform, non-invasive plan | ODEC Facts, staging |

Each row is the kind of dependency a key user finds only by asking. Add the relevant row to
the machine's record in [`../assets/guidance-protocol.md`](../assets/guidance-protocol.md)
when a machine depends on it.

## Sources

- Vault `Graph/Machines` (1,715 notes), `Graph/Plants` (33), `Graph/Tools` (16), counted or read 2026-11-05.
- Vault `ODEC Facts` folder: `Triage`, `Department KPIs and Roadmap Status`, `Plant - Carei`,
  `Plant - Auburn`, `Other` (staging, AI-extracted, not human-reviewed).
- Registry reference [`barrier-classes.md`](barrier-classes.md) for the symptom-versus-root-cause rule.
