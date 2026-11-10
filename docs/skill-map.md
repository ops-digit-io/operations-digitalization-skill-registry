---
type: Map of Content
title: Skill map
description: "The four lane skill maps read as one: which capability each lane names, where they overlap, and which registry skill covers each."
resource: ../registry.yaml
status: stable
owner: human:jakob.gabriel
tags: [skill-map, lanes]
generated: { by: claude-code/1, at: 2026-08-25T00:00:00Z }
---
# The OD skill map — consolidated

The four lane `skills.md` files in the knowledge graph each answer the same question for
one service line: *what may this lane work with, without searching?* Consolidated here as
one table, because the overlaps are the interesting part — they are where two lanes touch
the same system with different rights, and where a handover is really a change of write
right.

Source: `_knowledge/OperationsDigitalization-Department/20-lanes/*/skills.md`, verified
2026-08-10. `⟨…⟩` marks a gap carried through unchanged from the source.

## Systems, tools and interfaces by lane

| Skill / Tool / Interface | Use Case Support | Information Integration | Project Support | Analytical Support |
|---|---|---|---|---|
| **Data platform** — Databricks → Azure Storage Account, Parquet | read (written by the edge offload) | write via the offload | — | read |
| **IIoT Edge Platform** (plant Kubernetes runtime) | read / deploy | deploy / configure | — | — |
| **Manufacturing Service Bus (MSB)** | read / write ⟨scope to confirm⟩ | configure ⟨scope to confirm⟩ | — | — |
| **Data pipelines** (transformation / standardization) | write ⟨with IIAE⟩ | write | — | — |
| **Machine connectors / signal standards** | — | configure | — | — |
| **OESL Dashboards / Power BI** | read / author | — | — | author |
| **Digitalization Scorecard** | read / author | readiness matrix: read / update | — | Use Case Utilization: read / update |
| **Equipment Integration report** (Power BI) | — | read / update | — | — |
| **ODEC reporting** (progress & impact) | — | — | read / update | — |
| **Use-case library / SharePoint** | read / write | — | — | — |
| **Process diagnostics methods** | read | — | — | apply |
| **Benefit-calculation method** | author | — | — | — |
| **Machine Learning models** (labeling / training) | — | — | — | build ⟨scope to confirm⟩ |
| **Analytics / report / app assets** | — | — | — | author |
| **Ad-Hoc Analytics / Process First-Aid Kit** | Process First-Aid Kit | — | — | apply |
| **Project management method / tracker** | — | — | read / update | — |
| **Manufacturing Software Suite** | — | rollout preparation | configure ⟨scope to confirm⟩ | — |
| **Manufacturing Apps / app store (IIoT Edge)** | — | — | deploy | — |
| **Acceptance-test protocols** | — | author | author | — |
| **Investment planning templates** | — | investment planning | author | — |
| **Cyber Security / OT interface** | respect the gate | consult | respect the gate | — |

## What the overlaps say

**The data platform is the seam of the whole department.** Information Integration writes it
through the edge offload — Databricks to an Azure Storage Account, Parquet — and Use Case
Support and Analytical Support read it. Every "where is my data?" question is a question
about that seam, which is why `od-data-availability-check` exists as its own skill rather
than a paragraph in two lanes.

**Write rights are the real lane boundary.** Use Case Support may write pipelines only
*with IIAE*. Project Support may deploy apps but never writes the data model. The lane cut
rule — one trigger, one definition of done, one autonomy profile — shows up here as one
write right per system per lane.

**Two lanes author acceptance protocols and neither may sign one.** That asymmetry is
deliberate and is the reason `od-acceptance-test` states sign-off as human-only at every
authority level.

**Three of the four lanes touch the Scorecard, each on a different surface** — utilization,
readiness, counts. `od-scorecard-reporting` collects those into one place so that a single
figure does not get reported three ways.

**Three lanes carry a Cyber Security gate.** It is a constraint, not a task, which is why it
lives in `od-context` and is inherited rather than restated per skill.

## Capability bottlenecks and skill gaps

From `10-modules/smart-factory-use-case/capabilities.md` — the honest statement of what the
department cannot currently do at volume:

| Capability | Bottleneck | Skill gap |
|---|---|---|
| Machine & equipment integration | IIAE capacity — 3 roles, open positions Asia/Americas | Signal standardization, edge integration |
| Data-model harmonization & offload | Operations concepts missing for the data platform / MSB | Limited internal data-platform / MDA-PDA IT knowledge |
| Use-case definition & benefit calculation | DBVE capacity — 2 roles | Process diagnostics + business-case skills |
| Analytics / ML models | Data readiness on the data platform | ML labeling / training capability ⟨to confirm⟩ |
| App / dashboard development | Licensing | ⟨to confirm⟩ |

Global staffing: open positions planned in Asia and the Americas; Europe partly staffed.

These are the entries a registry cannot fix. A skill makes a procedure repeatable; it does
not add an IIAE. Where a skill sits on top of a named bottleneck — `od-signal-standardization`
on the data-platform / MSB operations-concept gap, `od-equipment-integration` on IIAE
capacity — it says so in the body, so the reader knows the constraint is real and not a
process failure.
