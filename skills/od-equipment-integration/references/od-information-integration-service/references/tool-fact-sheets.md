---
type: Skill Reference
title: Tool fact sheets
description: Guidance for answering "what is it, where is it, what does it need" for each shop-floor tool in the Tool Overview - what each tool is for, which records to read for rollout, cost, hardware, status and blockers, and the prerequisites to check. No figures; counts, prices and plant lists are looked up live.
resource: ../procedure.md
status: draft
tags: [information-integration-service, lane]
---

# Tool fact sheets

The lane page names the three integration concepts and the data platform. Plants also meet
the **other tools** the lane prepares for (step 6: "Prepare Manufacturing Software Suite
rollout") and the ones use cases run on. This file says what each tool is, where its record
lives and what to check, so a key user can answer "what is it, where is it, what does it need".
**It holds no counts, prices or plant lists** - those change; read them live.

**Where the live truth lives.**

- **Record**: the Tool Overview as quoted in `Graph/Tools` (one note per tool): plants per tool
  with year and status, use cases that name the tool. Count on the current export and name the
  export date.
- **Archive-based, AI-drafted**: the "Archive evidence" blocks of those tool notes summarize
  archive decks and say "AI-drafted ... not reviewed by a human". Open the deck
  ([`finding-decks.md`](finding-decks.md)) before quoting anything from them.
- Plant lists per tool and per plant: [`plant-tool-availability.md`](../../../../od-system-fit-check/references/plant-tool-availability.md)).
  What each tool **is not** for: [`tool-boundaries.md`](../../../../od-system-fit-check/references/tool-boundaries.md)).

## The three integration concepts

Detail and routing are in [`od-equipment-integration`](../../../SKILL.md).

| Tool | What to read in the record | Qualitative facts |
|---|---|---|
| Concept 1, central OPC-UA server | Plants with status and year; use cases naming it | OPC UA is a platform-independent, service-oriented architecture for machine-to-machine and machine-to-enterprise interoperability |
| Concept 2, container-based machine integration | Plants with status and year | Connector with no device at the machine; no written route |
| Concept 3, IIoT edge computing platform | Plants with status and year; use cases naming it | Operations concept deck: the goal is a reliable and cost-efficient support model for implementing and operating the manufacturing suite, with a shared operating model between local and central teams and standardized regional and local templates ("if you know one installation, you know the others"). Roles: [`roles-and-support-model.md`](roles-and-support-model.md). Architecture: machines over Profinet, Profibus or Modbus through an edge or OPC layer to a regional or central data centre (MQTT broker, cloud gateway, big-data services, a manufacturing data lake), from which data reaches ERP, MRMS, MII and a shop-floor dashboard tool |

## Data and service layer

| Tool | What to read in the record | Qualitative facts |
|---|---|---|
| MSB (Manufacturing Service Bus): 1.0, 2.0, 4.0 | Plants per release with year and status (including ongoing and planned); use cases per release | The bus sits between operation technology (edge devices, PLCs, machines over Modbus TCP, an SPS driver or an OPC UA server) and IT (ERP, MES, MDA/PDA, the ProView server, energy management, cloud apps), exposing OPC UA publish/subscribe and MQTT or API interfaces on the IT side; stated intent: a "Data Autobahn with standardized on-ramps and exits". The architecture deck does not name a release, so it applies to the family. The department's named MSB rollout projects (note *MSB rollout projects*, `_knowledge/20-Done`) are a real reference for "one plant's worth of work": read the use case count per project there. The Machine List carries the same projects as `project_reference` ([`blockers-and-waves.md`](../../blockers-and-waves.md)) |
| MDA/PDA (machine and process data acquisition): 1.0, 2.0, 3.0 | Plants per release with year and status; use cases per release | The registry's `deployment-reality.md` names the MDA/PDA system as Iconics Genesis64. A "handover done - with open topics" status is a signal to ask what is open |
| RuleEngine 2.0 | Plants with year and status; use cases naming it | The Transformation Flow Library documents new transformation flows, technical and functional standard workflows and plant-specific workflows (not every flow is documented). Typical example: a flow turns process values arriving over MQTT into a relational table view, with named instances per test type, so an overview can be drilled down to serial-part results |
| Data Science Factory | Plants with status (ongoing, stopped by management decision) | Scoped as needing to be available within the Manufacturing Data Lake. An architecture presentation contrasts micro-batching (fresh data from the bus or MQTT broker; Node-RED) with scheduled or batched jobs (heavier transformations; Apache Beam with an optional Flink runner) and flags as open how to host the resulting ETL components as apps |

## Plant systems the lane prepares for

| Tool | What to read in the record | Qualitative facts |
|---|---|---|
| MES 1.0 | Plants with status and year | A production-IT functional analysis maps order release and capacity control to the ERP and detailed scheduling, quality, maintenance, materials and most equipment-status data to the MES (informed by VDI 5600); energy management is mapped to the energy tool rather than to MES. It is "an example / discussion mapping, not a finalized specification". Architecture reviews describe targets (IIoT Edge Platform, MSB, a recipe management system and SAP DMC) that may be scope, not delivered: check delivery before quoting |
| Energy Management 1.0 and 2.0 (WiriTec) | Plants per release with year and status; notes column (for example "Still Local System > Potential for Cloud", "API available"); missing years are a data gap | WiriTec was set as the uniform energy-monitoring standard, supporting data collection, analysis, consumption monitoring, billing, forecasts. **On-premises (1.0)**: a Windows server with the product's web server and data connector, an SQL Server or Oracle database, a "Watchdog", and a "WiriBox" data logger on a small industrial PC. **Field interfaces**: M-Bus, Modbus RTU, LON bus, pulse counters via a logger; Modbus TCP, BACnet/IP, Siemens RFC1006, Ethernet/IP; CSV, e-mail or FTP import; ODBC; SNMP; REST; OPC UA; MQTT. **Cost model** (look up the current price list: OD lead or tool owner): one-time licence per location, yearly maintenance, consulting days, administrator and user training, plus logger hardware. **Implementation steps**: project start with local team including MTO and local IT, hardware/software gap check, hardware, bus and cost planning, purchasing, commissioning, training. **Cloud (2.0)**: logger devices send over OPC, REST, Ethernet or HTTPS/SFTP through the MSB's shop-floor component where installed, to an Azure-hosted platform; prerequisite: separated office and shop-floor networks with encrypted, certificate-based communication. **Migration to OESL-managed servers**: each cutover is a short outage while loggers are reconfigured; read the migration tracker for progress |
| QFPR (Quality Feedback and Part Routing) | Plants with status and year; use cases naming it | Integrates quality data from machines or manual input; SPC charts from manually collected data, a reaction log for quality incidents, alerting on not-OK parts, scrap and part-issue collection. Principle: "develop once, deploy everywhere". Cyber-security approval (vulnerability scan and penetration test) is mandatory before any productive rollout. Typical blockers: development delay, stalled purchasing, plant financial-guideline restrictions on app development |
| MIL 1.0 (Manufacturing Image Library) | Plants with status (ongoing, stopped by management decision) | Pilot blockers and the image use cases: see [``../../od-equipment-integration/references/blockers-and-waves.md``](../../blockers-and-waves.md) §5. A separate "Image Browser" exists as a first version piloted on one plant's lines (filter by process and date range, thumbnails with part and timestamp). Earlier one-pagers scoped MIL alongside MDL integration and QFPR; check the scope on the current one-pager |

## How to use the sheets

1. When a plant asks "can we have X", read the tool's row, then the plant's row in the matrix.
2. For a rollout preparation (step 6), the tool-specific prerequisites are: network separation
   and certificates for the cloud energy tool; a security approval for QFPR; edge and MSB in
   place for the rule engine.
3. Prices and hardware specifications in older decks are **not offers**. Do not quote them to a
   plant as a budget: ⟨current price and hardware list. Who could supply it: OD lead or the
   tool owner.⟩

## Sources

- Knowledge base `Graph/Tools` (one note per tool), including the archive-evidence blocks.
- Knowledge base `Slide Index` (deck `Operation Concept IIoT and Edge Computing`, slides 2 to 3).
