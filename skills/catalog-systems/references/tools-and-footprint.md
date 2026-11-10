---
type: Skill Reference
title: Tools and footprint
description: Guidance, no figures - the three machine-integration concepts, the other shop-floor tools and how to read their rollout and deployment status live, and what "inside the lean footprint" means in practice. Open it when you need to know what a plant can already order against.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [all, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Tools and footprint

This file holds **no counts, plant lists or status snapshots**. Read the live sources: vault `Graph/Tools` (notes from the
SharePoint list `ToolOverview-List`, with rollout records per plant and "used by" links), the department's
systems-of-record note (`_knowledge/OperationsDigitalization-Department/10-modules/smart-factory-use-case/systems-of-record.md`,
which carries its own verification and validity dates: re-read it, and check its validity before quoting), and skill
`funnel-requirements` `references/legacy-system-assessment.md` for the footprint rule.

## The three integration concepts (the "where does the data go" choice)

| Concept (tool note) | What it is | How to find who has it |
|---|---|---|
| Concept 1 - Central OPC-UA Server | machines aggregated through one central OPC UA server (topology 3) | Tool note: plants with rollout status `Available` |
| Concept 2 - container-based Machine Integration | container-based, no edge device at the machine (topology 2) | Tool note: plants with rollout status `Available` |
| Concept 3 - IIoT Edge Computing Platform | the terminus of every ingress variant; offloads through Databricks to an Azure storage account | Tool note: plants with rollout status `Available`, also `Ongoing` and planned records |

Use `Available` as "the plant has the platform". A use case naming a concept does not prove the machine is on it.
The Machine List (see [validated-routes.md](validated-routes.md)) can show machines integrated through a concept at plants
whose tool note does not record it as `Available`. Treat that mismatch as a question for the IIAE (integration before the
rollout was recorded, or rollout records not updated), not as a fact either way.

An aggregation-server (Concept 1) route **also needs the edge platform behind it**: the server concentrates, it is not a
destination (`mi-connector`, `decision-paths.md`). So before offering a Concept 1 route, confirm for the plant
that Concept 3 is `Available`. A plant with a Concept 1 record but only a planned, not-started or missing Concept 3 record
cannot be offered a Concept 1 route until the edge is confirmed (IIAE).

## The other shop-floor tools

Read each tool's note for its rollout records and the use cases naming it.

| Tool | What the tool note says it is |
|---|---|
| MSB (versions 1.0 / 2.0 / 4.0) | Manufacturing Service Bus, the use-case enabler and integration backbone; a newer version can be Ongoing at plants while an older one is Available |
| RuleEngine 2.0 | rule engine (Node-RED) for rule-based alerting; "rule engine" and "Node-RED" are the same thing in these skills |
| MDA/PDA (versions 1.0 / 2.0 / 3.0) | machine and process data acquisition family |
| MES 1.0 | manufacturing execution system |
| MIL 1.0 | Manufacturing Image Library |
| QFPR | Quality Feedback Part Routing |
| Energy Management (1.0 / 2.0) | energy management tool |
| Data Science Factory | recorded in the tool overview |

## Deployment status: how to read the systems-of-record note

The note gives a deployment reading per system. The pattern to apply (re-read the note for the current wording and dates):

| System | Typical reading | Consequence for a match |
|---|---|---|
| MDA/PDA | significantly deployed | likely available; verify per plant |
| IIoT Edge | significantly deployed | the safe assumption |
| MES | rollout on hold, ERP-dependent | a dependency on MES rollout is blocked, not planned |
| MSB | limited | confirm at this plant |
| MIL | high demand, not deployed | do not depend on it |
| Energy Management | deployed, rollout stopped pending operational criteria | do not extend it |

The note has its own validity window; if it has expired, re-read the underlying sources before quoting this table.

## Lean footprint - what the sources actually fix

The bundle says the aim is a **lean, standardized system footprint**, measured as the number of systems in operation (target
still to be confirmed; `00-core/03-objectives.md`). In practice the footprint rule of `funnel-requirements` applies: a
requirement that needs a system outside the tools above is not a use case but a tool-rollout decision, routed to the OD lead
(`od-decision-routing`). For a standard-system entry that means: the kit may use Concept 1, 2 or 3 and the connectors in the
Connector Overview; it may not require MES, MIL or an extension of Energy Management, and it may not add a new tool.

## Data layer a standard system feeds

Machine and equipment signals arrive near real time on the IIoT Edge platform (the plant Kubernetes runtime); standardized
data lands in the data platform (Databricks to an Azure Storage Account, Parquet) per offload; use-case data exchange runs
over the MSB, event-driven (systems-of-record). A plant's Grafana is local; the global layer is not wired into it (guardrail
G2 of `catalog-usecase`). ⟨Access paths, local buffer and fallback per data object⟩ are marked "to confirm" in the note
itself - IIAE.

## Open

- ⟨Which plants have no edge platform at all⟩ - a plant with no row in the tool overview is unknown, not a "No".
- ⟨Licence position of the aggregation server per PLC family⟩: the product needs a licence per family unless the extended
  suite is in place (`mi-connector`, `softing-datafeed.md`); the vault does not say which plants hold which.
