---
type: Skill Reference
title: Footprint and data path
description: The reference architecture and systems of record an app design must fit, the rollout and use counts of the 16 tools, how the lean footprint is bounded, and the discrepancies to confirm before citing a tool status.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [project-support-consultancy, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Footprint and data path

## The data path an app sits on

`landscape.md` (module, last verified 2026-08-10), approach reference: *minimal architecture*
**Machine / workplace, IIoT Edge (one of three ingress variants), MQTT / Node-RED, offload via Databricks to
an Azure Storage Account (Parquet), then Manufacturing Apps or local Grafana dashboards.**

Systems of record (`systems-of-record.md`; valid until 2026-11-10 - check it is current). The module's
rule: "two sources for the same data object are the most reliable way to make an agent answer wrongly."

| Data object | Source | Note for an app design |
|---|---|---|
| Machine / equipment signals | IIoT Edge Platform (plant Kubernetes runtime) | Near real-time; local buffer `⟨to confirm⟩`; owner IIAE |
| Standardized / transformed data | Data platform: Databricks to Azure Storage Account, Parquet | Access path `⟨to confirm⟩`; the global, cross-plant layer |
| Use-case data exchange | Manufacturing Service Bus (MSB) | Event-driven; write right `⟨to confirm⟩`; the bus is not the data platform |
| Use-case and integration status | Digitalization Scorecard (Power BI) | Monthly |
| Machine / production data | MES (2 plants, in progress), MDA/PDA (16 deployed) | System interface `⟨to confirm⟩`; MES is ERP-dependent |
| Manufacturing apps and dashboards | Manufacturing app store on the IIoT Edge | Dev team; owner OD |

Glossary distinctions that matter in a design: Grafana is a **local instance per plant**; the data platform
is **global**; MSB is the bus, not the data platform; MDA/PDA is data acquisition, not execution (not MES).

## How the footprint is bounded

Strategy (`02-strategy.md`, verified 2026-08-10, valid until 2026-11-10). Trade-offs: a limited number of
systems with a small operational footprint against broad tool coverage; highly standardized modular
deployments against bespoke per-plant solutions; maximal value-add with lowest dependencies against maximal
feature coverage. Non-bets: no standardized MES rollout short or mid-term (ERP-dependent; "check
light-weight substitutes e.g. QFPR"); EMS rollout stopped until operational criteria are resolved; OD does
not build automation solutions (Manufacturing Engineering) or own energy and facility topics; no broad tool
proliferation. Bet B1: drive the edge offload into the data platform as the primary route for use-case data.

Deployment status as recorded (Route 25, in `systems-of-record.md`): MDA/PDA about 16 significantly
deployed; IIoT Edge significantly deployed; MES 2 in progress (rollout on hold, ERP-dependent); MSB
limited; MIL high demand, not deployed; EMS deployed but rollout stopped.

## The 16 tools: rollout and use (work vault, Graph/Tools, read 2026-11-05)

Counts are from the tool notes (rollout records and use cases that name the tool). A use case "uses" a tool
as recorded in the use-case list; many are `IDEA`. Plant counts are of plants with a record, not of all
plants.

| Tool | Plants with rollout record (status) | Use cases naming it (plants) | Of which `PRODUCTIVE` |
|---|---|---|--:|
| Concept 3, IIoT Edge Computing Platform | 14 (available) | 200 (16) | 74 |
| RuleEngine 2.0 | 19 (available) | 203 (18) | 70 |
| MSB 2.0 | 13 (available) | 184 (18) | 49 |
| MSB 4.0 | 9 (6 available, 3 ongoing) | 90 (10) | 35 |
| Concept 2, container-based machine integration | 1 (available) | 85 (13) | 12 |
| MSB 1.0 | 3 (available) | 31 (6) | 6 |
| MDA/PDA 2.0 | 14 (available) | 28 (11) | 3 |
| QFPR | 2 (1 available, 1 ongoing) | 27 (8) | 2 |
| Concept 1, central OPC-UA server | 11 (available) | 24 (6) | 5 |
| MDA/PDA 3.0 | 3 (available) | 20 (5) | 1 |
| MIL 1.0 | 1 (ongoing) | 19 (9) | 1 |
| MDA/PDA 1.0 | 6 (available) | 12 (4) | 0 |
| Energy Management 2.0 | 24 (23 available, 1 not) | 6 (5) | 0 |
| Data Science Factory | 1 (ongoing) | 6 (4) | 4 |
| Energy Management 1.0 | 4 (available) | 1 (1) | 1 |
| MES 1.0 | 1 (available) | no use line in the note | not recorded |

How to read it in a design conversation: the tools that carry `PRODUCTIVE` use cases are the edge platform,
RuleEngine, MSB 2.0 and 4.0. A request that needs a tool with many rollouts and few productive uses (EMS 2.0,
MDA/PDA 1.0) points at an adoption question before a build question (`od-handover-and-adoption`).

## Discrepancies to confirm before quoting a status

| Item | One source says | Another says | Action |
|---|---|---|---|
| MES | `systems-of-record`: "MES 2 in progress, rollout on hold" | Tool note MES 1.0: one rollout record, available, one plant | Ask the OD lead which is current |
| EMS | Strategy: "rollout stopped until operational criteria are resolved" | The January 2025 tool catalogue in `od-system-fit-check`: rolled out to most locations; tool notes: Energy Management 2.0 has 23 plants available | Do not pick the convenient version; ask |
| QFPR | `od-system-fit-check` expands it as "Quality Feedback App" | The tool note records a 2022 work note expanding it as "Quality Feedback Part Routing" | Use "QFPR" until confirmed |
| MDA/PDA versions | `systems-of-record`: MDA/PDA about 16 deployed | Tool notes: 1.0 (6 plants), 2.0 (14), 3.0 (3) | Ask which version a plant runs before designing against it |

## Support tiers, from the IIoT Edge operations concept

The operations-concept deck summarised in the Concept 3 tool note distinguishes a **Divisional Standard**
application (its example: SAP ME) with global IT application-management support, from **local or business-unit
applications** with no IT application-management support and only local IT infrastructure; interfaces between
the two need governance-board approval. Roles named there: Local Key User, BA/BU Key User, Governance Board,
Central Key User, Divisional Engineering Support, Divisional IT, Local IT, and the provider of the platform
service. This is an AI-drafted summary of an archive deck (note dated 2026-09-29, not reviewed by a human);
confirm before using it to assign support in a recommendation.
