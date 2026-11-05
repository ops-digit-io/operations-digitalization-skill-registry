---
type: Skill Reference
title: Process chain practice
description: Method, decision rules, handoff contract, pitfalls and agent notes for the cross-plant check, abstracted from the Operations Digitalization slide decks - where the base data model does and does not fit, process-specific models, data classes and the leading system, plant differences that break a standard, adding one unknown machine type at a time. Guidance only, no figures.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [all, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Process-chain practice - testing a standard at the second plant

Deck-derived practice for step 3b4 (proposed) and for the standardization check at step 26. `PROPOSAL` = registry synthesis; `<to confirm>` = decks disagree.

## 1. Method in practice

1. **Name the archetype first.** A cross-process standard is independent of the core process but has limits (for example not meaningful for continuous processes) and needs integration work because data models differ. A per-process standard depends on process values of one core process and scales fastest. A unique case is not tested for cross-plant use at all.
2. **Check the model scope before the plants.** The foundation (base) data model holds no process values and was found to fit **greenfield, discrete-process, time-series-centric machines**. Brownfield with many controller types and continuous processes needed other models. Roadmap material says "all connected machines"; the thesis-level evidence says a minority. Safer reading: test fit per machine class `<to confirm>`.
3. **Check the production-metadata relation.** Use cases that need order, part, batch or recipe cannot be served by signals alone. Where no standard execution or planning system exists, the relation is the blocker. First look at what object data the controller already carries; route a missing relation as a data gap.
4. **Test the model layering.** Public companion specifications (types) -> company extensions for generalized use cases -> plant instance model; instances only from predefined types; models kept machine-readable and documented with context. Test: can every plant's machine of the process family be instantiated from the same type and expose the same views?
5. **Process-specific model creation** (the standard fix for a per-process standard): survey public standards; draft the in-house extension in a modelling editor; combine with the public standard and make an example instance for one machine; review and iterate with process engineering until release; instantiate per machine and roll out. Order across processes can be set by a plant vote.
6. Continue with `SKILL.md` steps 3 to 8.

## 2. Plant differences that break a standard (add to the grid)

| Dimension | What to look at |
|---|---|
| Controller families and program versions | entry-level controllers with no interface; the smallest high-end controller at its capacity limits, making tag export slow; new machines still delivered without an integration standard |
| Machine state model | brownfield state-machine standardization: analyse control types and data models, define the target state machine, standard flows for cycle time, availability and error messages |
| Production structure | planning per cell (lean U-cell) versus per machine; an app built for per-machine planning does not fit a cell plant |
| Data class | transactional (hub: service bus), time series (hub: MQTT), master data (single source of truth, leading system pushes by API). Local masters (recipes, meter structures) may disagree with the stated leader; reconciliation is `<to confirm>` |
| Ingress path | edge device versus plain OPC UA client; cameras through one edge device per line |
| Tag language and naming | no naming convention across plants, cryptic labels, scaling and units as tribal knowledge |
| Runtime licences | OPC UA server licences bound to one machine: have the key before migrating a virtual server; confirm new DNS, certificates and access |
| Data types in flows | values stored as the wrong type, padded identifier fields, unit conversions, mapping-file synchronization |
| Lab and test equipment | dongle-bound software on a single test system; hardware or licence constraint belongs in the data-availability step |
| Security status | patch status of installed controllers blocked a second integration wave; a precondition |
| Machine-list completeness | response to a vulnerability notice or migration is bounded by the machine list; lists were not updated at most plants |

## 3. Decision rules

- **Add one unknown machine type per new deployment at most.** Scaling known machine types worked; connecting the difficult ones first failed. Document the process per controller type and create an integration standard. The opposite advice appears in older material `<to confirm>`.
- **Consumers get one interface.** Applications are not tailored to device interfaces; third-party models are mapped into the standard model, which provides the first level of context. Predictable node identifiers where only equipment number and workplace change.
- **Mapping beats branching** (restated from `SKILL.md`): normalize vendor naming in a mapping layer; never add a plant branch inside the standard.
- **Same views for all machines of one core process** is the aim; if a plant needs a different view, the finding is against the standard or against the model scope.
- **Wireless or low-cost routes** are proved on a few machines first and kept simple; address translation on an existing switch can serve many machines with one configuration (low data frequency only).
- **Do not migrate everything at once.** Legacy middleware flows move to the rule engine per flow, with plant key users, a change request to uninstall, and an updated application list; risk-based prioritization and redeployment beat a big-bang migration.

## 4. Handoff contract

| Receives | From |
|---|---|
| the standard under test (signal set, model, flow, dashboard) and its first plant | `od-signal-standardization`, `od-use-case-standardization` |
| per-plant data reality | `od-data-availability-check` |

| Hands on | To |
|---|---|
| verdict grid (consumable / with mapping / not consumable / unknown) with evidence and owner of each mapping | `catalog-usecase`, `od-decision-routing`, the technical community call |
| model-scope finding (which machine classes fit) | `od-signal-standardization` |
| missing-relation or missing-signal table | Information Integration lane |

## 5. Pitfalls and lessons

- **The data lands, but the standard does not hold:** two plants can land different names for one concept.
- **Reputation cost.** An unsuccessful first attempt at difficult machines made plants reluctant; stabilize trust before adding use cases.
- **Relocating simple machines repeatedly** delays integration; check layout stability.
- **Integrating an additional system without a standard integration and interface layer yields no benefit;** the processes were not understood.
- **Customer-driven programs** (a customer mandating a process-control framework with staged compliance targets) have another driver than savings and another KPI (compliance progress); do not force them through the savings-driven grid `<to confirm>`.

## 6. Questions to ask and definition of done

Which archetype and which machine classes? Greenfield discrete or brownfield? Does the use case need production metadata and where does it live? Which data classes? Cell or machine planning? Who consumes it? Who owns each mapping?

**Done:** grid complete with verdict and evidence per plant in scope; unknown never rounded to consumable; model scope stated; owner named per mapping.

## 7. AI agent operating notes

- **Can do:** build the plant grid from machine list and tool overview; propose mappings from local to standard names with the rule used; detect naming drift and unit or type mismatches in flow exports; instantiate-and-compare a model type across two machines; draft the grid.
- **Needs:** machine list, signal lists per plant, the standard, read dates.
- **Human gate:** verdict per plant is confirmed by the plant IT role; the data-model decision is the integration engineer's by consultation; model-scope calls are the OD lead's.
- **Must cite:** machine list rows, signal ids, mapping rule, read date.
- **Hands over:** the grid with unknown plants listed with the evidence that would resolve each.
