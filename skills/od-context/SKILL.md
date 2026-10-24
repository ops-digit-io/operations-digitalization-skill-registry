---
name: od-context
description: >-
  The shared ground truth for MPEE Operations Digitalization (OD) — the department's
  vocabulary, its four service lines, who decides what, where the truth actually lives,
  and the honesty rules every other OD skill inherits. Load this before any OD work:
  before answering a question about a use case, a machine, a saving, a plant or a
  scorecard figure; before routing a request to a service line; before quoting any OD
  number. Use it whenever terms like use case, asset, equipment integration, the data
  platform, Databricks, MSB,
  IIoT Edge, MDA/PDA, MES, ODEC, COP, DBVE, IIAE, Digitalization Scorecard, CSP, eCR or
  SPRINT appear and must resolve to exactly one meaning.
license: Internal — OESL MPEE Operations Digitalization. Not for external distribution.
metadata:
  id: od-context
  tier: foundation
  lane: all
  owner_role: OD lead (Thomas Zipf)
  authority_level: read-only
  status: stable
  sources_read: 2026-10-23
  derived_from:
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/00-core/01-charter.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/00-core/04-service-catalog.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/00-core/08-decision-rights.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/00-core/14-glossary.md
    - ops-knowledge-graph/_knowledge/10-Department/Operating model.md
    - ops-knowledge-graph/_knowledge/10-Department/Systems of record.md
    - ops-knowledge-graph/_knowledge/10-Department/Roles and organization.md
  okf:
    type: Agent Skill
    title: OD context
    tags: [all, foundation]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-08-25T00:00:00Z }
---

# OD context

Every other skill in this registry assumes this file. It exists because inconsistent
vocabulary and unlabelled numbers are the two ways OD work goes wrong that no amount of
procedure fixes.

## What the department does

Operations digitalization turns a problem somebody has on a shop floor into a digital
asset that plant uses every day — a dashboard, an app, an alert, a report — and then
rolls the same asset out to the other plants that have the same problem.

It runs across **33 plants in three regions** (20 Europe, 9 Americas, 4 Asia). Every
piece of work is recorded against one plant, one of four material families (Rubber,
Plastic, Metal, Assembly), and one of eleven cross-plant digital capabilities. That
three-way coordinate is what makes a use case at one plant findable from another.

**Mandate.** Enable manufacturing on its "Road to Smart Factory": generate measurable
value from shopfloor data through digital use cases, delivered maximally value-adding, lean,
standardized and scalable.

**Not OD's** (refuse or route, do not absorb): functional lead of Plant ME and
automation-solution development; customer-project industrialization, RFQ and
P-FMEA/process-parameter standards; energy/facility and green production; tool-center
operations; ERP / S4HANA ownership. OD supports these with digital solutions but does
not own them.

## The four service lines

| Lane | Trigger | Definition of done | Owner | Skill |
|---|---|---|---|---|
| Smart Factory Use Case Support Service (incl. Process First-Aid Kit) | Plant use-case demand or definition-workshop request | Use case defined, prioritized, impact-evaluated, handed to integration with a business case | DBVE (2 roles) | `od-use-case-support-service` |
| Information Integration Service | Equipment integration or data-model harmonization need per roadmap | Machine/equipment integrated, signals standardized, data landing on the data platform | IIAE (3 roles) | `od-information-integration-service` |
| Project Support & Application Consultancy | Digital investment project kick-off | Integration project managed to acceptance test; application consulted and accepted | IIAE | `od-project-support-consultancy` |
| Analytical Support Service (incl. Ad-Hoc Analytics) | Analytical request or ad-hoc process-insight need | Process diagnostics / analytical insight delivered | DBVE | `od-analytical-support-service` |

Lane cut rule: **one lane = one trigger + one definition of done + one autonomy
profile.**

## Vocabulary — one term, one meaning

| Term | Means here | Not to be confused with |
|---|---|---|
| Use Case | A defined shopfloor digitalization solution delivering measurable operational value | Asset (its delivered form) |
| Asset | The delivered form of a use case — Dashboard, Analytics, Report, App or Agent | A connected data point |
| Equipment / Machine Integration | Connecting a machine or workplace to the digital platform for data read/write | Use-case delivery, which comes after |
| Capability | One of eleven cross-plant templates a use case hangs off | Cluster tag (a classification, not a template) |
| Cluster tag | One of twelve C01–C12 tags assigned by a deterministic classifier | Capability |
| IIoT Edge | Plant Kubernetes runtime for data acquisition and app deployment | The data platform it offloads to |
| Data platform | Where shopfloor data lands for analysis — the IIoT Edge Platform offloads through **Databricks** to an **Azure Storage Account**, main file format **Parquet** | MSB, the bus |
| Databricks | The data platform the edge offloads through | The storage account it writes to |
| Azure Storage Account | The offload target | Databricks, which writes it |
| Parquet | The main file format on the storage account | — |
| MSB | Manufacturing Service Bus — use-case enabler / integration backbone | The data platform |
| MES | Manufacturing Execution System — rollout on hold, ERP/S4HANA-dependent | MDA/PDA (acquisition, not execution) |
| MDA/PDA | Machine Data Acquisition / Process Data Acquisition | MES |
| Digitalization Scorecard | The authoritative Power BI report of OD targets vs. actuals and readiness | The Use Case / Equipment Integration reports, which feed it |
| Readiness (RAG) | System integration & availability per dimension × location — red not available, yellow in rollout, green available | — |
| ODEC | Operations Digitalization Exchange Call — monthly **strategy** cadence | COP |
| COP | Community of Practice Call — monthly **technical** cadence | ODEC |
| DBVE | Digital-Business-Value-Engineer — owns use-case value | IIAE |
| IIAE | IIoT Interface & Automation Engineer — owns integration | DBVE |
| Route 25 | OESL Smart Factory strategy program / bootstrapping-tools assessment | — |
| CSP | Common Solution Portfolio decision — the gate that says a library entry is standard enough to roll out | — |
| eCR | Engineering change request — the spend route | — |
| SPRINT | The portfolio review that turns a tracked saving into a proven one | — |
| Process First-Aid Kit | Rapid diagnostic offering inside Use Case Support | Ad-Hoc Analytics (Analytical lane) |

Acronyms: OD = Operations Digitalization · MPEE = Manufacturing Process & Equipment
Engineering ⟨expansion to confirm⟩ · OESL = Original Equipment Solutions (confirmed —
the title slide of every ODEC/CoP call deck names it) · OPEX/CBS = Operational Excellence /
Continental Business System · MIL = Manufacturing Image Library (confirmed 2026-10-22, see
`od-system-fit-check/references/tool-boundaries.md`) · EMS = Energy Management System,
**not** "Equipment Management System" (confirmed 2026-10-22, same source — WiriTec) ·
ME = Manufacturing Engineering.

## Where the truth lives

**Write surface — SharePoint lists.** A correction reaches everyone by being made
there, not in a downstream copy.

| List | Holds |
|---|---|
| SmartFactory UseCase Savings | 650 plant use cases and the whole taxonomy |
| UseCase SavingCalculation | 553 saving rows |
| UseCase Library | 100 standardized reference solutions |
| Machine List | 1,715 machines and their integration state |
| Connector Overview | 26 machine connectors |
| Tool Overview | Tool rollouts, one row per tool per plant |
| Legacy Application List | 268 applications being replaced or retired |
| Business Cases (AI at Operations) | The strategic business-case set |

**Read surfaces.** The Digitalization Scorecard and the two OD Power BI reports
(`OD-Report-Use_Case_Integration`, `OD-Report-Equipment_Integration`); **Grafana — a local
instance per plant**, where most delivered dashboards are actually seen; and the knowledge
graph, which is rebuilt from the lists and does **not** travel corrections back.

**The data path.** Where shopfloor data goes after it is read:

```
PLC ──(one of three ingress variants)──► IIoT Edge Platform ──MQTT──► Node-RED
                                                  │
                                              offload
                                                  ▼
                                            Databricks ──► Azure Storage Account
                                                                 (Parquet)
                                                                     │
                                                                     ▼
                                                        analytics · dashboards · use cases
```

**Databricks** is the data platform the IIoT Edge Platform offloads through; the target is an
**Azure Storage Account**, and the main file format is **Parquet**. ⟨Access paths, workspace
and container naming, and the catalog layout are not recorded here — to confirm.⟩

**Global platform, local dashboards.** Databricks and the storage account are the **global**
layer, where cross-plant analysis happens. **Grafana is a local instance per plant**, building
that plant's manufacturing dashboards from that plant's data. A line-side dashboard belongs
on the local instance; a cross-plant question belongs on the global platform. Do not point a
plant's Grafana at the global platform, and do not build a cross-plant view on a local one.

**Shop-floor tools.** Sixteen are rolled out at plants: the MSB family (1.0, 2.0, 4.0)
as the rollout backbone, MDA/PDA (1.0, 2.0, 3.0), MES 1.0, MIL 1.0, QFPR, Energy
Management (1.0, 2.0), RuleEngine 2.0, the Data Science Factory, and the three
machine-integration concepts. A **tool** is a system a plant uses; a **connector**
reaches a machine. They are never the same row.

## Who decides

The function proposes; other people decide. Four of the five gates sit outside OD.

| Gate | Route | Threshold |
|---|---|---|
| Spend | eCR | CTO up to €150k; Board above €75k |
| Demand on IT platforms | IT demand management + demand evaluation board | anything OD does not own |
| Standard enough to roll out | CSP decision per library entry | 5 `Yes` / 46 `No` of 51 decided |
| Into daily use | The plant | plant owns `PRODUCTIVE` |
| Value is proven | SPRINT portfolio review | 19 of 553 saving rows |

`authority_level` ∈ { `read-only`, `draft`, `recommend`, `execute-with-approval`,
`execute-autonomously` }. Modes at seams: **Tandem** (both must agree) · **Consultation**
(hear, then decide alone) · **Information**. Full routing: `od-decision-routing`.

## The honesty rules — non-negotiable, inherited by every OD skill

1. **Tracked is not proven, and the two are never added together.** €2.38 M tracked and
   €653 k proven are both true about the same portfolio; quoting the first without the
   second is the easiest way to lose the audience that matters.
2. **Built is not handed over, and handed over is not in use.** `IMPLEMENTED` and
   `PRODUCTIVE` are separate statuses because they fail separately.
3. **Absence is not a zero.** 362 of 650 use cases carry `UNKNOWN` priority and 474 of
   553 saving rows carry no reliability. Reading those as "low" is the most frequent way
   to be wrong about this portfolio.
4. **Never state a figure without a nameable source**, and never invent one. Mark
   unknowns as `⟨… — to confirm⟩` rather than filling them.
5. **Version history carries text the current record does not.** Rationale, blockers and
   comments were often written during active work and later tidied back to `-`.
6. **The graph is a read surface.** Corrections go to the SharePoint list.
7. **Never act on an external machine connection** without Cyber Security / OT sign-off.

## Escalation

Blocked work → OD lead (Thomas Zipf), via **ODEC** for strategy, priority and rollout
matters, via **COP** for technical ones. In the OD lead's absence ⟨deputy — to confirm⟩
decides prioritization and rollout within the agreed roadmap; investment commitments
wait for the OD lead.

## Open gaps carried from the source

Named owners per lane (role labels only today) · lane target lead times · budget figure ·
MES / MDA-PDA interface detail, write rights and freshness.

**Resolved 2026-10-22/23, no longer open:** the value-delivery-cycle metric is confirmed
not captured in any system today (`od-scorecard-reporting`) rather than merely unconfirmed;
the adoption-confirmation mechanism is the three-tier evidence ranking in
`od-handover-and-adoption/references/evidence-of-adoption.md` (system usage log > named
owner's dated statement > third-party observation).

## Provenance

Derived from the `ops-knowledge-graph` bundle: `OperationsDigitalization-Department/`
(charter, service catalog, decision rights, glossary, resources) and `10-Department/`
(operating model, systems of record, roles and organization). Portfolio figures read
2026-08-10 and **will drift** — refetch before acting on any of them.
