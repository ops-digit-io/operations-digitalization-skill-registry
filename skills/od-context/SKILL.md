---
name: od-context
description: >-
  Shared ground truth for MPEE Operations Digitalization (OD): vocabulary, the three
  new-state lanes (and the retired four service lines), who decides what, where the truth lives, and the honesty rules every OD skill
  inherits. Load before any OD work, before quoting any OD number, before routing a request,
  and whenever terms like use case, asset, MSB, MES, ODEC, COP, DBVE, IIAE, CSP, eCR or SPRINT
  must resolve to one meaning.
license: MIT
metadata:
  id: od-context
  tier: foundation
  lane: all
  new_state_lane: "Spine"
  new_state_step: "Supporting spine"
  department_names: ["dept-os"]
  owner_role: OD lead
  authority_level: read-only
  status: stable
  sources_read: 2026-11-10
  derived_from:
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/00-core/01-charter.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/00-core/04-service-catalog.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/00-core/08-decision-rights.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/00-core/14-glossary.md
    - ops-knowledge-graph/_knowledge/10-Department/Operating model.md
    - ops-knowledge-graph/_knowledge/10-Department/Systems of record.md
    - ops-knowledge-graph/_knowledge/10-Department/Roles and organization.md
    - "Work vault, OD Department Knowledge/OD-instance/20-lanes-newstate-DRAFT (README, lane 1-3), read 2026-11-10"
  okf:
    type: Agent Skill
    title: OD context
    tags: [all, foundation]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-08-25T00:00:00Z }
---

# OD context

## Purpose and where it sits

The foundation every other OD skill assumes: one vocabulary, the three new-state lanes, who decides what, where the
truth lives, and the honesty rules. Serves every process step as the precondition (it is not a step of its own);
users are all roles and every AI agent, which loads it before any OD work.
**Inputs:** none (read-only). **Output:** a resolved term, route or source, never a figure (numbers are read live from
the lists below).

## What the department does

Operations digitalization turns a shop-floor problem into a digital asset the plant uses daily (dashboard, app,
alert, report) and rolls it out to other plants with the same problem.
It runs across the manufacturing plants of all regions (count them in the plant master data). Every piece of work is
recorded against one plant, one of four material families (Rubber, Plastic, Metal, Assembly) and one cross-plant
digital capability; that three-way coordinate makes a use case findable from another plant.

**Mandate.** Enable the "Road to Smart Factory": measurable value from shopfloor data through lean, standardized,
scalable digital use cases.

**Not OD's** (refuse or route, do not absorb): functional lead of Plant ME and automation-solution development;
customer-project industrialization, RFQ and P-FMEA/process-parameter standards; energy/facility and green production;
tool-center operations; ERP / S4HANA ownership. OD supports these digitally but does not own them.

## The three lanes (new state)

The department segments demand by effort, ownership and novelty into **three branched lanes**
(`OD-instance/20-lanes-newstate-DRAFT/`, status DRAFT: the department is being transformed, the
model is the plan of record for this registry but not yet locked). Each demand is classified into
exactly one lane at intake (`od-use-case-intake-triage`); branches chain afterwards.

| Lane | Branches | Trigger | Ownership | Money | Entry skill |
|---|---|---|---|---|---|
| **Lane 1** Run a known use case | 1a connected machine · 1b standardized-system onboarding | Reuse a catalogued use case | Plant self-service; OD supplies catalog, templates, guardrails | 1a none · 1b predictable (cost template) | `od-catalog` |
| **Lane 2** Develop a new use case | funnel; chains to Lane 3, graduates to Lane 1 | A genuinely new recurring need on connected equipment | OD-led (DBVE) | Business-case driven | `od-use-case-definition` |
| **Lane 3** New system or connector | front-end, then 3a new system (3a.1 reuse, 3a.2 self-develop, 3a.3 external build, 3a.4 integrate a foreign app) or 3b new connector | Something needed does not exist yet | Front-end OD-led (OD lead); build OD + external; integrate and connect IT, Cyber Security gated | Variable (business case) | `od-requirements-breakdown` → `od-system-fit-check` |

**How the branches connect.** Lane 1 falls through to Lane 2 (not truly catalogued) or Lane 3
(non-standard system, new machine). Lane 2 chains to 3a (needs software) or 3b (needs a connection),
and a proven, repeatable Lane 2 result is catalogued and becomes a Lane 1 case. Lane 3's front-end
(requirements → tool-decision gate → business case → capital request → handover) routes to 3a or 3b
and hands over to IT or external delivery only once the demand is clear (`od-it-handover`).

**Old to new.** The four functional service lines are retired:

| Old service line (owner) | New state |
|---|---|
| Smart Factory Use Case Support Service, incl. Process First-Aid Kit (DBVE) | Known use cases → Lane 1; genuinely new → Lane 2 |
| Analytical Support Service, incl. Ad-Hoc Analytics (DBVE) | Retired as a standing lane; ad-hoc analytics routes to Lane 1 self-service, Lane 2, or external support (`od-first-aid-kit`) |
| Information Integration Service (IIAE) | Lane 3 branch 3b; integration-project management folds in (`od-equipment-integration`) |
| Project Support & Application Consultancy (IIAE) | The shared Lane 3 front-end: requirements → decision gate → clear demand → handover (`od-it-handover`) |

**Step ids and route options.** Process step ids (`3a4`, `3a5`, `3a6`, `3b4` …) number the steps of a
branch; route options are written with a dot (`3a.1` reuse, `3a.2` self-develop, `3a.3` external build,
`3a.4` integrate a foreign app). Step `3a4` ("build or integrate") serves all four route options.

**Lane 2 order.** Prototype comes before the business case: requirements → features and data check →
prototype → business case → capital request. This follows the department's Lane 2 file; the naming
convention's chain `bc-build → funnel-prototype` describes how its packaged skills hand over, not the
process order. A prototype that changes the value picture updates the business case.

**Department skill names.** The department's naming convention (`<family>-<object>`, 2026-09-21) names
the same capabilities differently; each skill lists its department names in `metadata.department_names`,
so a request using either name finds the skill.

**Ownership tiers.** Self-service (plant executes inside pre-approved guardrails) · OD-led · OD +
external (OD scopes, externals deliver) · IT, Cyber Security gated (OD does not control the gate).

Lane cut rule: **one lane = one trigger + one definition of done + one autonomy profile.**

## Vocabulary — one term, one meaning

| Term | Means here | Not to be confused with |
|---|---|---|
| Use Case | A defined shopfloor digitalization solution delivering measurable operational value | Asset (its delivered form) |
| Asset | The delivered form of a use case — Dashboard, Analytics, Report, App or Agent | A connected data point |
| Equipment / Machine Integration | Connecting a machine or workplace to the digital platform for data read/write | Use-case delivery, which comes after |
| Capability | One of the cross-plant templates a use case hangs off | Cluster tag (a classification, not a template) |
| Cluster tag | One of the C01–C12 tags assigned by a deterministic classifier | Capability |
| IIoT Edge | Plant Kubernetes runtime for data acquisition and app deployment | The data platform it offloads to |
| Data platform | Where shopfloor data lands for analysis — the IIoT Edge Platform offloads through **Databricks** to an **Azure Storage Account**, main file format **Parquet** | MSB, the bus |
| Databricks | The data platform the edge offloads through | The storage account it writes to |
| Azure Storage Account | The offload target | Databricks, which writes it |
| Parquet | The main file format on the storage account | — |
| MDL | "OESL Manufacturing Data Lake" in older department files, including the new-state lane drafts. **Not used** (owner decision, `docs/derivation.md`): read every MDL in a source as the data platform above | A separate system |
| ContiTech | Named in older department files (lane drafts, decision rights) as shared-service partner and counterpart. **Not used** (owner decision, `docs/derivation.md`): where a decision names ContiTech, the counterpart is the IT-responsible role of the business side | — |
| MSB | Manufacturing Service Bus — use-case enabler / integration backbone | The data platform |
| MES | Manufacturing Execution System — rollout on hold, ERP/S4HANA-dependent | MDA/PDA (acquisition, not execution) |
| MDA/PDA | Machine Data Acquisition / Process Data Acquisition | MES |
| Digitalization Scorecard | The authoritative Power BI report of OD targets vs. actuals and readiness | The Use Case / Equipment Integration reports, which feed it |
| Readiness (RAG) | System integration & availability per dimension × location — red not available, yellow in rollout, green available | — |
| ODEC | Operations Digitalization Exchange Call — **historical** strategy forum (monthly only until 2025-12, no longer held, no fixed replacement forum); a source of information (past decisions, decks, facts) | COP |
| COP | Community of Practice Call — **technical** round | ODEC (historical) |
| DBVE | Digital-Business-Value-Engineer — owns use-case value | IIAE |
| IIAE | IIoT Interface & Automation Engineer — owns integration | DBVE |
| Route 25 | OESL Smart Factory strategy program / bootstrapping-tools assessment | — |
| CSP | Common Solution Portfolio decision — the gate that says a library entry is standard enough to roll out | — |
| eCR | Electronic capital request — the spend route for a project or integration wave | — |
| SPRINT | The portfolio review that turns a tracked saving into a proven one | — |
| Process First-Aid Kit | Rapid diagnostic offering for a one-off plant process issue; routes to Lane 1, Lane 2 or external support | A standing analytics lane (retired) |
| CMO | Container Management and Orchestration: the Kubernetes-based platform (registry, source host, GitOps catalog) apps deploy to; the preferred route for platform-level Cyber Security approval | The IIoT Edge runtime |
| Key user | The plant role that runs catalogued, self-service work inside OD's guardrails | The OD builder |

Acronyms: OD = Operations Digitalization · MPEE = Manufacturing Process & Equipment Engineering (expansion: see open
points) · OESL = Original Equipment Solutions (confirmed, named on every ODEC/CoP deck title slide) · OPEX/CBS =
Operational Excellence / Continental Business System · MIL = Manufacturing Image Library and EMS = Energy Management
System, **not** "Equipment Management System" (both confirmed 2026-10-22, `od-system-fit-check/references/tool-boundaries.md`)
· ME = Manufacturing Engineering.

## Where the truth lives

**Write surface: SharePoint lists.** A correction reaches everyone by being made there, not in a downstream copy.

| List | Holds |
|---|---|
| SmartFactory UseCase Savings | The plant use cases and the whole taxonomy |
| UseCase SavingCalculation | The saving rows (value, reliability, status) |
| UseCase Library | The standardized reference solutions |
| Machine List | The machines and their integration state |
| Connector Overview | The machine connectors |
| Tool Overview | Tool rollouts, one row per tool per plant |
| Legacy Application List | The applications being replaced or retired |
| Business Cases (AI at Operations) | The strategic business-case set |

**Read surfaces.** The Digitalization Scorecard and the two OD Power BI reports (`OD-Report-Use_Case_Integration`,
`OD-Report-Equipment_Integration`); **Grafana, a local instance per plant**, where most delivered dashboards are seen;
the knowledge graph, rebuilt from the lists, which does **not** pass corrections back.

**The data path.** Where shopfloor data goes after it is read:

```text
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

**Global platform, local dashboards.** Databricks and the storage account are the **global** layer (cross-plant
analysis); **Grafana is a local instance per plant**, built on that plant's data. A line-side dashboard belongs on the
local instance, a cross-plant question on the global platform. Do not point a plant's Grafana at the global platform,
and do not build a cross-plant view on a local one.

**Shop-floor tools.** The MSB family (rollout backbone), MDA/PDA, MES, MIL, QFPR, Energy Management, RuleEngine, the
Data Science Factory and the three machine-integration concepts. A **tool** is a system a plant uses; a **connector**
reaches a machine; never the same row.

## Who decides

The function proposes; other people decide. Most gates sit outside OD.

| Gate | Route | Threshold |
|---|---|---|
| Spend | eCR | Per the current approval policy (look up: Controlling / the eCR process owner) |
| Demand on IT platforms | IT demand management + demand evaluation board | anything OD does not own |
| Standard enough to roll out | CSP decision per library entry | Decision recorded per entry in the library |
| Into daily use | The plant | plant owns `PRODUCTIVE` |
| Value is proven | SPRINT portfolio review | Saving row marked proven after review |

`authority_level` ∈ { `read-only`, `draft`, `recommend`, `execute-with-approval`,
`execute-autonomously` }. Modes at seams: **Tandem** (both must agree) · **Consultation**
(hear, then decide alone) · **Information**. Full routing: `od-decision-routing`.

## The honesty rules — non-negotiable, inherited by every OD skill

1. **Tracked is not proven; never add the two.** Both are true of the same portfolio; quoting one without the other
   loses the audience that matters. Read both live from the saving rows.
2. **Built is not handed over, and handed over is not in use.** `IMPLEMENTED` and `PRODUCTIVE` fail separately.
3. **Absence is not a zero.** Many use cases carry `UNKNOWN` priority and many saving rows no reliability (count live);
   reading those as "low" is the most frequent error about this portfolio.
4. **Never state a figure without a nameable source**, never invent one. Mark unknowns `⟨… — to confirm⟩`.
5. **Version history carries text the current record does not** (rationale, blockers, comments later tidied to `-`).
6. **The graph is a read surface.** Corrections go to the SharePoint list.
7. **Never act on an external machine connection** without Cyber Security / OT sign-off.

## Handoff

Other skills take from here a resolved term, a gate route (`od-decision-routing`) or a source list. Blocked work goes to
the OD lead; strategy, priority and rollout matters to the role named in the current approval policy (look up),
technical ones may use the **COP**; ODEC is historical, not a route. In the OD lead's absence the next-higher
management role decides prioritization and rollout within the roadmap; investment stays with the approval body.

## Human gate and AI-agent notes

An agent may resolve terms, quote a figure only from a live list (cite list and export date), and route. It never
states an unsourced figure, writes to the graph, or acts on an external machine connection. Humans decide every gate
in the table above.

## Pitfalls and open points

- Recurring errors: honesty rules 1, 3 and 6, and mixing the local Grafana with the global platform.
- **Open points (to confirm):** Databricks access paths, workspace and container naming, catalog layout; MPEE expansion; named owners per lane (role labels only today); lane target lead times; budget figure; MES / MDA-PDA interface detail, write rights and freshness. Resolved gaps: `references/swot-and-dependency-seams.md`.

## References

| File | Open when |
|---|---|
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | Currency rules per field, three demand shapes, plant tiering, AI maturity check, handoff contract |
| [`references/swot-and-dependency-seams.md`](references/swot-and-dependency-seams.md) | Testing an action against the SWOT; dependency seams and their mode; corrections table; open-gaps queue; resolved gaps |
| [`references/knowledge-graph-reading.md`](references/knowledge-graph-reading.md) | Reading the knowledge graph: node kinds, relations, provenance of descriptions |
| [`references/provenance-and-source-catalogue.md`](references/provenance-and-source-catalogue.md) | Finding content in non-Markdown sources; reference library tiers; benchmarks without overclaiming; provenance tags |
