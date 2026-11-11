---
type: Skill Reference
title: Footprint and data path
description: Guidance, no figures. The reference architecture and systems of record an app design must fit, how to read the rollout and use of the tools, how the lean footprint is bounded, and the discrepancies to confirm before citing a tool status.
resource: ../procedure.md
status: draft
owner: human:jakob.gabriel
tags: [project-support-consultancy, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Footprint and data path

## The data path an app sits on

`landscape.md` (module), approach reference: *minimal architecture*
**Machine / workplace, IIoT Edge (one of three ingress variants), MQTT / Node-RED, offload via Databricks to
an Azure Storage Account (Parquet), then Manufacturing Apps or local Grafana dashboards.**

Systems of record (`systems-of-record.md`; it carries a review date, so check it is current before
using it). The module's rule: "two sources for the same data object are the most reliable way to make an
agent answer wrongly."

| Data object | Source | Note for an app design |
|---|---|---|
| Machine / equipment signals | IIoT Edge Platform (plant Kubernetes runtime) | Near real-time; local buffer `⟨to confirm⟩`; owner IIAE |
| Standardized / transformed data | Data platform: Databricks to Azure Storage Account, Parquet | Access path `⟨to confirm⟩`; the global, cross-plant layer |
| Use-case data exchange | Manufacturing Service Bus (MSB) | Event-driven; write right `⟨to confirm⟩`; the bus is not the data platform |
| Use-case and integration status | Digitalization Scorecard (Power BI) | Refreshed periodically |
| Machine / production data | MES (pilot plants only), MDA/PDA | System interface `⟨to confirm⟩`; MES is ERP-dependent |
| Manufacturing apps and dashboards | Manufacturing app store on the IIoT Edge | Dev team; owner OD |

Glossary distinctions that matter in a design: Grafana is a **local instance per plant**; the data platform
is **global**; MSB is the bus, not the data platform; MDA/PDA is data acquisition, not execution (not MES).

## How the footprint is bounded

Strategy (`02-strategy.md`; it carries a review date, so check it is current). Trade-offs: a limited
number of systems with a small operational footprint against broad tool coverage; highly standardized
modular deployments against bespoke per-plant solutions; maximal value-add with lowest dependencies
against maximal feature coverage. Non-bets: no standardized MES rollout short or mid-term (ERP-dependent;
"check light-weight substitutes e.g. QFPR"); EMS rollout paused until operational criteria are resolved;
OD does not build automation solutions (Manufacturing Engineering) or own energy and facility topics; no
broad tool proliferation. Bet B1: drive the edge offload into the data platform as the primary route for
use-case data.

How to treat each system in a design (guidance; the live position is the Tool Overview and
`od-system-fit-check`, not this file): MDA/PDA and IIoT Edge are the widely deployed base, verify per
plant; MES is rollout-on-hold and ERP-dependent; MSB is limited, confirm availability at the plant; MIL
has demand but limited deployment, do not depend on it; EMS rollout is subject to operational criteria,
confirm the current position.

## The tools: how to read rollout and use

Source: the department knowledge base `Graph/Tools` notes (rollout records and the use cases that name each tool). Tools:
Concept 1 central OPC-UA server, Concept 2 container-based machine integration, Concept 3 IIoT Edge
Computing Platform, RuleEngine 2.0, MSB 1.0 / 2.0 / 4.0, MDA/PDA 1.0 / 2.0 / 3.0, QFPR, MIL 1.0,
Energy Management 1.0 / 2.0, Data Science Factory, MES 1.0. Do not copy a table of counts into a
recommendation: re-count on the live notes.

How to count live, per tool:

1. Plants with a rollout record, split by status (available, ongoing, stopped, planned, not available).
   A plant with no row has no record, which is not the same as "not available".
2. Use cases naming the tool, with the number of plants they sit at.
3. Of those use cases, the share that is `PRODUCTIVE` against `IDEA`. Many use cases that name a tool
   are `IDEA`; naming a tool is not use.

How to read it in a design conversation: the tools that carry `PRODUCTIVE` use cases are typically the
edge platform, RuleEngine and the Manufacturing Service Bus. A request that needs a tool with many
rollouts and few productive uses points at an adoption question before a build question
(`od-handover-and-adoption`). A tool named by many use cases at plants where it is not rolled out is a
demand signal, not an availability fact (`od-system-fit-check`, plant tool availability).

## Discrepancies to confirm before quoting a status

| Item | One source says | Another says | Action |
|---|---|---|---|
| MES | `systems-of-record`: pilot plants in progress, rollout on hold | Tool note MES 1.0: a rollout record at one plant | Ask the OD lead which is current |
| EMS | Strategy: rollout paused until operational criteria are resolved | The tool catalogue in `od-system-fit-check` and tool notes: rolled out at many plants | Do not pick the convenient version; ask |
| QFPR | `od-system-fit-check` expands it as "Quality Feedback App" | The tool note records a work note expanding it as "Quality Feedback Part Routing" | Use "QFPR" until confirmed |
| MDA/PDA versions | `systems-of-record`: MDA/PDA as one deployed tool | Tool notes: versions 1.0, 2.0 and 3.0 with separate plant lists | Ask which version a plant runs before designing against it |

## Support tiers, from the IIoT Edge operations concept

The operations-concept deck summarised in the Concept 3 tool note distinguishes a **Divisional Standard**
application (its example: SAP ME) with global IT application-management support, from **local or business-unit
applications** with no IT application-management support and only local IT infrastructure; interfaces between
the two need governance-board approval. Roles named there: Local Key User, BA/BU Key User, Governance Board,
Central Key User, Divisional Engineering Support, Divisional IT, Local IT, and the provider of the platform
service. This is an AI-drafted summary of an archive deck (not reviewed by a human); confirm before using it
to assign support in a recommendation.
