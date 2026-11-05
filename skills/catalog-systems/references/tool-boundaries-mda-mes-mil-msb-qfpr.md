---
type: Skill Reference
title: Tool boundaries MDA MES MIL MSB QFPR
description: Is / is-not / recommended-if boundary for five shop-floor tools that the tool overview lists without a strong definition - MDA/PDA, MES, MIL, MSB and QFPR - with the traps each one brings to a match. Pattern only, no rollout status, counts or plants.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [all, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Tool boundaries: MDA/PDA, MES, MIL, MSB, QFPR

Source: vault `Graph/Tools` (tool notes from the tool-overview list, each with a short definition from the department glossary and,
for MSB, MES, MIL and QFPR, archive evidence curated by AI and not reviewed by a human). The archive evidence is dated and partly
planned or pilot state: a plan is not a deployed capability. **Rollout status per plant changes: read the tool note and the
systems-of-record note live and time-stamp it** (see `tools-and-footprint.md`). This file carries the boundaries only.

The test for every entry, from `process-chain-practice.md` section 1: what the tool **is**, what it **is not**, and the
**"integration recommended if"** trigger, tied to a named use case. A tool recommendation without a use case is not made.

| Tool | Is | Is not | Recommended if (trigger) |
|---|---|---|---|
| MDA/PDA (machine and process data acquisition; versions 1.0, 2.0, 3.0) | The data-acquisition tool family: reads machine and process data and holds the plant data model the earlier use cases were built on. Used heavily behind SPC, line monitoring and Andon cases | A service bus; an analytics or ML platform; a recipe or master-data store. Versions are generations, not sizes: they differ in data model and add-ons (one note records a dashboarding add-on with SQL) | The use case needs process or quality data from machines at a plant where this family is the standard acquisition route and the signals fit its model |
| MES (1.0) | The shop-floor execution layer between ERP and the machines: detailed scheduling, production control and sequencing, quality management, maintenance management, materials and work-in-progress, most equipment-status data. The vault frames the split with ERP using VDI 5600 | An energy-management tool (energy is mapped separately); a dashboard tool; a data-acquisition gateway. In the vault no use case is linked to it | The request is really order or recipe execution, labels, batch genealogy, material validation or lot tracing: the "heavy request disguised as a dashboard" |
| MIL (Manufacturing Image Library) | The store for inspection and process images with metadata, retrieval, and a path to the data lake; image acquisition is the enabling step for vision and defect use cases | A process-parameter store; a model-training platform; a viewer by itself (a separate image browser exists for review) | The use case needs images per part kept and searched (vision inspection, defect analysis, labelling), and the image-transfer path exists or is funded |
| MSB (Manufacturing Service Bus; versions 1.0, 2.0, 4.0) | Middleware between the machine side (PLCs, edge devices, OPC UA servers, vendor protocols) and the IT side (ERP, MES, data acquisition, energy, cloud apps) with publish/subscribe and message interfaces; the integration backbone most use cases are deployed on. The archive describes the role for the family, not per version | A calculator or interpreter of signals; a dashboard; a substitute for the edge platform's acquisition and historisation; a data store | Several systems must exchange events; the use case is event-driven and cross-system; a machine's data must be offered to more than one consumer |
| QFPR (Quality Feedback and Part Routing) | An app for quality data from machines or typed on a station screen: SPC charts from manually collected data, a reaction log for quality incidents, alerts on not-OK parts, scrap and part-issue collection; intended standard data model for manual quality data | A KPI calculator; a master-data store; an automated inline measurement system; an MES | The use case is paper or spreadsheet quality capture that should feed SPC and reaction handling, at a plant that is on the rollout list |

## Traps the notes show

### MDA/PDA

- A use case naming a version does not prove the machine is on it: check the machine list (`validated-routes.md`).
- A data model that is available only through one tool makes that tool the dependency of every consumer; say so in the entry.
- Several versions co-exist at plants. Ask which one the plant runs before you size the work.

### MES

- The vault holds a target architecture where the edge platform owns acquisition and historisation, a recipe management system
  owns recipe versions and release, and a cloud MES owns order tracking, traceability, shop-floor reporting and batch validation.
  It is a **design for one plant, scope-dated, not delivered**. Do not quote it as available.
- MES rollout is ERP-dependent and was recorded as on hold in the systems-of-record note: a dependency on MES is blocked, not
  planned. The footprint rule forbids a kit that requires MES.
- The business-case arithmetic in the archive (manual form entry removed per production step) is the authors' worked example for
  one plant, not a benchmark.

### MIL

- The pilot the notes describe is blocked on several fronts at once: the transfer tool from local storage to the cloud was tested
  but not productive, live operation had not started, a firewall change was raised and untested, the transfer tool was not on the
  edge platform, and the stated top requirement is that images land in the data lake's blob store. Treat "MIL needed" as a
  **dependency on a platform that is not ready**, not a ready service.
- Plants keep images locally in their own naming convention with a manual backup; the pain is retrieval and storage growth. Ask
  for: naming convention, formats (full resolution and annotated overlay), retention, who needs them and how fast.
- Where the vision system is not connected to the bus, reports and images are pulled by hand from the machine with a delay; the
  blocker is the connection, not the library.
- Do not confuse the library, the transfer tool, a labelling tool and the image browser: four things, four statuses.

### MSB

- The newer version can be Ongoing at a plant while an older one is Available: name the version in the entry.
- The bus carries; if the request is calculation, put it in the rule engine or the capability service
  (`microservice-app-pattern.md` in skill `deploy-appstore` for the proposed split).
- A path to the central lake goes through an edge or OPC server at the plant; confirm the plant's edge platform first.

### QFPR

- Cyber Security approval was pending throughout the documented period and is mandatory before any productive (not just test)
  rollout; plan it as work, not as a formality (`od-cybersec-gate`).
- The per-location deployment method was still open ("develop once, deploy everywhere" was the intent): do not promise a
  one-click rollout.
- Blockers recorded: development delayed in continuous-production areas, a plant's financial-guideline restriction on app
  development, purchasing stalls after requirements had been handed over.
- It serves manual quality capture. Automated inline measurement belongs to Process Quality Data and a different route.

## Decision shortcuts

| Request says | First test | Likely route |
|---|---|---|
| "We need process data on this machine" | Is the machine integrated? Which acquisition family does the plant run? | MDA/PDA family or edge route per `od-equipment-integration` |
| "Quality sheet to digital" | Typed by a person? | QFPR if the plant is on its list; else a form app (Manual Quality Data) |
| "Images per part" | Is the image path (connection, transfer, storage) ready? | MIL-dependent: park behind the platform, or a local interim with an explicit end date |
| "Batch, order, label, genealogy" | Execution-system territory | MES discussion with the OD lead; not a kit |
| "Send machine events to several systems" | Event exchange | MSB; check the version and the edge platform |

## Open

- ⟨Which MDA/PDA version is the standard for a new plant⟩ - OD lead.
- ⟨Whether the image-library pilot has a funded path to productive⟩ - OD lead, IIAE.
- ⟨Where performance analysis sits between MES and the capability services⟩ - the process-chain note leaves this open.
