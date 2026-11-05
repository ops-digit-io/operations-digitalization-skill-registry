---
type: Skill Reference
title: Tool fact sheets
description: One fact sheet for each of the sixteen shop-floor tools in the Tool Overview - what it is, where it is rolled out, what it connects to and what its records say about cost, hardware, status and open blockers - for the key user who has to explain or install it.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [information-integration-service, lane]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---

# Tool fact sheets

The lane page names the three integration concepts and the data platform. Plants also meet
the **other tools** the lane prepares for (step 6: "Prepare Manufacturing Software Suite
rollout") and the ones use cases run on. This file gives what the vault records about each,
so a key user can answer "what is it, where is it, what does it need".

**Grades.**

- **Record**: from the Tool Overview as quoted in `Graph/Tools` (export 2026-08-24).
- **Archive-based, AI-drafted**: from the "Archive evidence" blocks of those tool notes, which
  summarize archive decks and say "AI-drafted ... not reviewed by a human". Open the deck
  ([`finding-decks.md`](finding-decks.md)) before quoting a figure.
- Plant lists per tool and per plant: [`plant-tool-availability.md`](../../od-system-fit-check/references/plant-tool-availability.md).
  What each tool **is not** for: [`tool-boundaries.md`](../../od-system-fit-check/references/tool-boundaries.md).

## The three integration concepts

Detail and routing are in [`od-equipment-integration`](../../od-equipment-integration/SKILL.md).

| Tool | Record | Archive-based facts |
|---|---|---|
| Concept 1, central OPC-UA server | 11 plants, all `AVAILABLE`, 2020 (Mako, Ponta Grossa) to 2025 (Ostrava, Somersworth); 24 use cases name it | OPC UA is described as a platform-independent, service-oriented architecture for machine-to-machine and machine-to-enterprise interoperability (external source R07, as cited in the tool note) |
| Concept 2, container-based machine integration | 1 plant (Carei, 2022) | |
| Concept 3, IIoT edge computing platform | 14 plants `AVAILABLE`, Waltershausen 2019 to Northeim and San Luis Potosi 2025; 200 use cases name it | Operations concept deck: the goal is "a reliable and cost efficient support model" for the world-wide implementation and operation of the manufacturing suite, with a shared operating model between local and central teams and standardized regional and local implementation templates ("if you know one installation, you know the others"). Roles and support model: [`roles-and-support-model.md`](roles-and-support-model.md). Architecture slide: machines over Profinet, Profibus or Modbus through an edge or OPC layer to a regional or central data centre (MQTT broker, cloud gateway, big-data services, a manufacturing data lake), from which data reaches ERP, MRMS, MII and a shop-floor dashboard tool |

## Data and service layer

| Tool | Record | Archive-based facts |
|---|---|---|
| MSB (Manufacturing Service Bus): 1.0, 2.0, 4.0 | 1.0: 3 plants (Changchun, Changshu, Korbach, 2022). 2.0: 13 plants (2019 to 2025). 4.0: 9 plants (6 available, Changchun, Changshu, Qingdao ongoing 2024), planned at Auburn. 2.0 is named by 184 use cases, 4.0 by 90, 1.0 by 31 | The bus sits between operation technology (edge devices, PLCs, machines over Modbus TCP, an SPS driver or an OPC UA server) and IT (ERP, MES, MDA/PDA, the ProView server, energy management, cloud apps), exposing OPC UA publish/subscribe and MQTT or API interfaces on the IT side; stated intent: a "Data Autobahn with standardized on-ramps and exits". The deck does not name a release, so this applies to the family. Mako note: "MSB will be upgraded during 2022 to include the MQTT and the LFT". The department's eight named MSB rollout projects carry these use case counts (note *MSB rollout projects*, `_knowledge/20-Done`): Karben 33, Carei 32, Mako 26, Somersworth 21, Timisoara 20, Dolne Vestenice 20, San Luis Potosi 19, Subotica 18 - a real reference for "one plant's worth of work". The Machine List carries the same projects as `project_reference` ([`blockers-and-waves.md`](../../od-equipment-integration/references/blockers-and-waves.md)) |
| MDA/PDA (machine and process data acquisition): 1.0, 2.0, 3.0 | 1.0: 6 plants (2020 to 2022). 2.0: 14 plants (2019 to 2025). 3.0: 3 plants (Korbach 2022, Caluire and Waltershausen 2023) plus Auburn ("Dashboarding AddOn with SQL"). Use cases: 12, 28 and 20 | The registry's `deployment-reality.md` names the MDA/PDA system as Iconics Genesis64. Caluire's 3.0 row: "Handover done - with open topics" |
| RuleEngine 2.0 | 19 plants (Ponta Grossa 2020 to San Luis Potosi 2025), Auburn planned; 203 use cases | The Transformation Flow Library (Jan 2024 update of the use case support process) documents new transformation flows, technical and functional standard workflows and plant-specific workflows (not every flow is documented). Example, Monterrey, May 2025: a flow turns process values arriving over MQTT into a relational table view, with named instances for a helium leak test, a flow test and an end-of-line test, so an hourly overview can be drilled down to serial-part results |
| Data Science Factory | Northeim `ONGOING` 2023 ("Conjunction with MIL"); `STOPPED (MANAGEMENT DECISION)` at Carei and Waltershausen 2024; 6 use cases | Scoped (March 2024 one-pager) as needing to be available within the Manufacturing Data Lake. A December 2023 architecture presentation contrasts micro-batching (fresh data from the bus or MQTT broker; Node-RED) with scheduled or batched jobs (heavier transformations; Apache Beam with an optional Flink runner) and flags as open how to host the resulting ETL components as apps |

## Plant systems the lane prepares for

| Tool | Record | Archive-based facts |
|---|---|---|
| MES 1.0 | Korbach, `AVAILABLE` 2022 | A 2019 production-IT functional analysis maps order release and capacity control to the ERP and detailed scheduling, quality, maintenance, materials and most equipment-status data to the MES (informed by VDI 5600); energy management is mapped to the WiriTec tool rather than to MES. It is "an example / discussion mapping, not a finalized specification". SAP ME deployments are described for two other sites (about 96 workplaces and 10 machines in one; about 68 machines in the other). A December 2025 architecture review for one plant's mixing shop floor describes the target as IIoT Edge Platform, MSB, a recipe management system and SAP DMC, "Scope 2025", not delivered |
| Energy Management 1.0 and 2.0 (WiriTec) | 1.0: `AVAILABLE` 2016 to 2025 (Karben 2016; Carei, Hann. Münden, Oedelsheim 2018; Northeim 2025; Dannenberg and Rennes year missing), notes "Still Local System > Potential for Cloud". 2.0: 19 plants, 18 available and Auburn "Not Available", "API available" on many; 6 use cases name 2.0, 1 names 1.0 | WiriTec was set as the uniform energy-monitoring standard on 2012-07-19, supporting data collection, analysis, consumption monitoring, billing, forecasts. **On-premises (1.0)**: a Windows server with the product's web server and data connector, an SQL Server or Oracle database, a "Watchdog", and a "WiriBox" data logger on a small industrial PC (dual-core 2 GHz, 16 GB RAM, 250 to 500 GB disk). **Field interfaces**: M-Bus, Modbus RTU, LON bus, pulse counters via a logger; Modbus TCP, BACnet/IP, Siemens RFC1006, Ethernet/IP; CSV, e-mail or FTP import; ODBC; SNMP; REST; OPC UA; MQTT. **Recorded standard price (2020/2021 editions quote the same figures)**: about 5,000 EUR one-time licence per location, 1,200 EUR per year maintenance, 1,700 EUR per consulting day, about 1,200 EUR each for administrator and user training; five implementation steps (project start with local team including MTO and local IT, hardware/software gap check, hardware, bus and cost planning, purchasing, commissioning, training). **Cloud (2.0)**: logger devices send over OPC, REST, Ethernet or HTTPS/SFTP through the MSB's shop-floor component where installed, to an Azure-hosted platform; prerequisite: separated office and shop-floor networks with encrypted, certificate-based communication; logger cost recorded as about 2,000 to 3,000 EUR per location, with 5 to 15 loggers typically needed per site. **Migration to OESL-managed servers, 2025**: 13 of 17 locations done by 2025-10-20; each cutover is roughly a one-day outage while loggers are reconfigured |
| QFPR (Quality Feedback and Part Routing) | Waltershausen `AVAILABLE` 2021; Monterrey `ONGOING` 2023; 27 use cases at 8 plants | Integrates quality data from machines or manual input; SPC charts from manually collected data, a reaction log for quality incidents, alerting on not-OK parts, scrap and part-issue collection. 2024: test instances at Carei, Delicias, Monterrey and Somersworth; "develop once, deploy everywhere"; cyber-security approval mandatory before any productive rollout (vulnerability scan and penetration test stage by December 2024); development delayed at Waltershausen, stalled at Monterrey pending purchasing. Monterrey rollout also recorded with a blocker around the plant's financial-guideline restrictions on app development |
| MIL 1.0 (Manufacturing Image Library) | Northeim `ONGOING` 2023; `STOPPED (MANAGEMENT DECISION)` at Delicias, Mako, Dolne Vestenice; 19 use cases | Northeim pilot blockers and the Monterrey and Karben image use cases: see [`../../od-equipment-integration/references/blockers-and-waves.md`](../../od-equipment-integration/references/blockers-and-waves.md) §5. A separate "Image Browser" went live in a first version in November 2025, piloted on the Monterrey lines (filter by process and date range, thumbnails with part and timestamp). A 2024 one-pager scoped MIL to 4 plants alongside MDL integration at all plants and QFPR at 7 plants |

## How to use the sheets

1. When a plant asks "can we have X", read the tool's row, then the plant's row in the matrix.
2. For a rollout preparation (step 6), the tool-specific prerequisites are the ones in the
   sheet: network separation and certificates for the cloud energy tool; a security approval
   for QFPR; edge and MSB in place for the rule engine.
3. Prices and hardware specifications above are **recorded figures from older decks**, not
   offers. Do not quote them to a plant as a budget: ⟨current price and hardware list. Who
   could supply it: OD lead or the tool owner.⟩

## Sources

- Vault `Graph/Tools` (16 notes), including the archive-evidence blocks, read 2026-11-05.
- Vault `Slide Index` (deck `Operation Concept IIoT and Edge Computing`, slides 2 to 3).
