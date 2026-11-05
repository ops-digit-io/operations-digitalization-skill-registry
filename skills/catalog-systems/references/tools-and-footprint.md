---
type: Skill Reference
title: Tools and footprint
description: The sixteen shop-floor tools with their rollout and use, the three machine-integration concepts with the plants that have them, and what "inside the lean footprint" means in practice. Open it when you need to know what a plant can already order against.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [all, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Tools and footprint

Sources, read 2026-11-05: vault `Graph/Tools` (16 notes from the SharePoint list `ToolOverview-List`, export of 2026-08-24; rollout and use counts as the notes state them), `_knowledge/OperationsDigitalization-Department/10-modules/smart-factory-use-case/systems-of-record.md` (last verified 2026-08-10, valid until 2026-11-10), skill `od-requirements-breakdown` `references/legacy-system-assessment.md` for the footprint rule.

## The three integration concepts (the "where does the data go" choice)

| Concept (tool note) | What it is | Plants with rollout status `Available` | Use cases that name it |
|---|---|---|---|
| Concept 1 - Central OPC-UA Server | machines aggregated through one central OPC UA server (topology 3) | 11: Mako, Ponta Grossa (2020); Caluire (2021); Changchun, Changshu, Korbach, Qingdao, Sun Prairie (2022); Waltershausen (2023); Ostrava, Somersworth (2025; taken over or migrated) | 24 at 6 plants |
| Concept 2 - container-based Machine Integration | container-based, no edge device at the machine (topology 2) | 1: Carei (2022) | 85 at 13 plants |
| Concept 3 - IIoT Edge Computing Platform | the terminus of every ingress variant; offloads through Databricks to an Azure storage account | 14: Waltershausen (2019); Caluire (2021); Carei, Delicias, Karben, Monterrey, Somersworth, Subotica, Timisoara (2022); Mako, Vac (2023); Dolne Vestenice (2024); Northeim, San Luis Potosi (2025). Further records: Hann. Muenden ongoing; Korbach, Changchun, Changshu, Qingdao planned and not started | 200 at 16 plants |

Use `Available` as "the plant has the platform". A use case naming a concept does not prove the machine is on it.
The Machine List (see [validated-routes.md](validated-routes.md)) shows machines integrated through the edge at 17 plants, while the Concept 3 note records 14 plants as `Available`; for the aggregation server both sources give 11 plants. ⟨Why the edge counts differ⟩ - IIAE (integration before the rollout was recorded, or rollout records not updated).

An aggregation-server (Concept 1) route **also needs the edge platform** behind it: the server concentrates, it is not a destination (`od-equipment-integration`, `decision-paths.md`).
Of the 11 Concept 1 plants, seven have no Concept 3 `Available` record in the tool notes: Changchun, Changshu, Qingdao and Korbach are recorded as planned and not started; Ponta Grossa, Sun Prairie and Ostrava have no Concept 3 record. For these a Concept 1 route cannot be offered until the edge is confirmed (IIAE).

## The other shop-floor tools

| Tool | What the tool note says it is | Rollout records | Use cases naming it |
|---|---|---|---|
| MSB 1.0 / 2.0 / 4.0 | Manufacturing Service Bus, the use-case enabler and integration backbone | 1.0: 3 plants Available; 2.0: 13 Available; 4.0: 6 Available, 3 Ongoing (Changchun, Changshu, Qingdao) | 31 / 184 / 90 |
| RuleEngine 2.0 | rule engine for rule-based alerting | 19 plants Available | 203 at 18 plants |
| MDA/PDA 1.0 / 2.0 / 3.0 | machine and process data acquisition family | 6 / 14 / 3 plants Available | 12 / 28 / 20 |
| MES 1.0 | manufacturing execution system | 1 plant Available | no use-case line in the note |
| MIL 1.0 | Manufacturing Image Library (per 2024 work notes) | 1 plant Ongoing | 19 at 9 plants |
| QFPR | Quality Feedback Part Routing (per a 2022 work note) | 1 Available, 1 Ongoing | 27 at 8 plants |
| Energy Management 1.0 / 2.0 | energy management tool | 4 / 24 plants Available (2.0: one Not Available) | 1 / 6 (all 6 at `IDEA`) |
| Data Science Factory | recorded in the tool overview | 1 plant Ongoing | 6 at 4 plants |

## Deployment status as the systems-of-record note gives it (Route 25 assessment, verified 2026-08-10)

| System | Status | Consequence for a match |
|---|---|---|
| MDA/PDA | about 16 plants significantly deployed | likely available; verify per plant |
| IIoT Edge | significantly deployed | the safe assumption |
| MES | 2 plants in progress, rollout on hold, ERP-dependent | a dependency on MES rollout is blocked, not planned |
| MSB | limited | confirm at this plant |
| MIL | high demand, not deployed | do not depend on it |
| Energy Management (1.0 / 2.0) | deployed, rollout stopped pending operational criteria | do not extend it |

The note's own validity window ends 2026-11-10; re-read it before quoting this table after that date.

## Lean footprint - what the sources actually fix

The bundle says the aim is a **lean, standardized system footprint**, measured as the number of systems in operation (target still to be confirmed; `00-core/03-objectives.md`). In practice the footprint rule of `od-requirements-breakdown` applies: a requirement that needs a system outside the table above is not a use case but a tool-rollout decision, routed to the OD lead (`od-decision-routing`). For a standard-system entry that means: the kit may use Concept 1, 2 or 3 and the connectors in the Connector Overview; it may not require MES, MIL or an extension of Energy Management, and it may not add a new tool.

## Data layer a standard system feeds

Machine and equipment signals arrive near real time on the IIoT Edge platform (the plant Kubernetes runtime); standardized data lands in the data platform (Databricks to an Azure Storage Account, Parquet) per offload; use-case data exchange runs over the MSB, event-driven (systems-of-record). A plant's Grafana is local; the global layer is not wired into it (guardrail G2 of `catalog-guardrails`). ⟨Access paths, local buffer and fallback per data object⟩ are marked "to confirm" in the note itself - IIAE.

## Open

- ⟨Which plants have no edge platform at all⟩ - a plant with no row in the tool overview is unknown, not a "No".
- ⟨Licence position of the aggregation server per PLC family⟩: the product needs a licence per family unless the extended suite is in place (`od-equipment-integration`, `softing-datafeed.md`); the vault does not say which plants hold which.
