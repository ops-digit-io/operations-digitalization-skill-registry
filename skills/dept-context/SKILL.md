---
name: dept-context
description: >-
  Gives every OD skill the same ground truth: the department vocabulary (use case, asset, capability, cluster tag, IIoT Edge, data platform, MSB, COP), the three lanes plus the outbound Lane 4, which SharePoint list holds which figure, and the honesty rules (tracked is not proven, absence is not zero, no figure without a source). Use before any OD work, when a term, lane, gate or list name is unclear, or before quoting an OD number such as savings, use-case counts or machine counts. Not for who may approve something (dept-decision-rights) or for sorting a new request into a lane (dept-intake).
license: MIT
metadata:
  id: dept-context
  aliases: [od-context]   # former name (naming convention, 2026-11-11)
  tier: foundation
  lane: all
  new_state_lane: "Spine"
  new_state_step: "Supporting spine"
  department_names: ["dept-os"]
  owner_role: OD lead
  tags: [all, foundation]
  authority_level: read-only
  status: stable
  okf:
    type: Agent Skill
    title: OD context
    tags: [all, foundation]
---

# OD context

## Purpose and where it sits

- The foundation every other OD skill assumes: one vocabulary, the three new-state lanes, who decides what, where the truth lives, and the honesty rules.

- **Outputs:** [`references/outputs.md`](references/outputs.md) lists what this skill must deliver, to whom, and when each output is complete.

## What the department does

- Operations digitalization turns a shop-floor problem into a digital asset the plant uses daily (dashboard, app, alert, report) and rolls it out to other plants with the same problem.
- It runs across the manufacturing plants of all regions (count them in the plant master data).
- Every piece of work is recorded against one plant, one of four material families (Rubber, Plastic, Metal, Assembly) and one cross-plant digital capability; that three-way coordinate makes a use case findable from another plant.

- **Mandate.** Enable the "Road to Smart Factory": measurable value from shopfloor data through lean, standardized, scalable digital use cases.

- **Not OD's** (refuse or route, do not absorb): functional lead of Plant ME and automation-solution development; customer-project industrialization, RFQ and P-FMEA/process-parameter standards; energy/facility and green production; tool-center operations; ERP / S4HANA ownership.
- OD supports these digitally but does not own them.

## The three lanes (new state)

- The department segments demand by effort, ownership and novelty into **three branched lanes** (the new-state lane drafts, status DRAFT: the department is being transformed, the model is the plan of record for this registry but not yet locked).
- Each demand is classified into exactly one lane at intake (`dept-intake`); branches chain afterwards.

| Lane | Branches | Trigger | Ownership | Money | Entry skill |
|---|---|---|---|---|---|
| **Lane 1** Run a known use case | 1a connected machine · 1b standardized-system onboarding | Reuse a catalogued use case | Plant self-service; OD supplies catalog, templates, guardrails | 1a none · 1b predictable (cost template) | `catalog-usecase` |
| **Lane 2** Develop a new use case | funnel; chains to Lane 3, graduates to Lane 1 | A genuinely new recurring need on connected equipment | OD-led (DBVE) | Business-case driven | `funnel-use-case` |
| **Lane 3** New system or connector | front-end, then 3a new system (3a.1 reuse, 3a.2 self-develop, 3a.3 external build, 3a.4 integrate a foreign app) or 3b new connector | Something needed does not exist yet | Front-end OD-led (OD lead); build OD + external; integrate and connect IT, Cyber Security gated | Variable (business case) | `funnel-requirements` → `invest-screen` |

- **How the branches connect.** Lane 1 falls through to Lane 2 (not truly catalogued) or Lane 3 (non-standard system, new machine).
- Lane 2 chains to 3a (needs software) or 3b (needs a connection), and a proven, repeatable Lane 2 result is catalogued and becomes a Lane 1 case.
- Lane 3's front-end (requirements → tool-decision gate → business case → capital request → handover) routes to 3a or 3b and hands over to IT or external delivery only once the demand is clear (OpenSpec IT demand, external).

- **Old to new.** The four functional service lines are retired; a requester who names one is translated with the crosswalk in `dept-intake` (also in `references/background.md`).

- Step ids, route options and department skill names: `references/process-chain-practice.md`, "Step ids and skill names".

- **Lane 2 order.** Prototype comes before the business case: requirements → features and data check → prototype → business case → capital request.
- This follows the department's Lane 2 file; the naming convention's chain `bc-build → funnel-prototype` describes how its packaged skills hand over, not the process order.
- A prototype that changes the value picture updates the business case.

- **Ownership tiers.** Self-service (plant executes inside pre-approved guardrails) · OD-led · OD + external (OD scopes, externals deliver) · IT, Cyber Security gated (OD does not control the gate).

- Lane cut rule: **one lane = one trigger + one definition of done + one autonomy profile.**

- **Lane 4, the outbound lane.** Lane 4 promotes a proven use case to other plants, leadership and colleagues through Internal Communications (IC).
- It is not an intake lane: no demand is classified into it.
- It is entered from a use case that is live and adopted (Lane 1 go-live or Lane 2 graduation) through `comms-showcase`, continues with `comms-brief` and `comms-followup`, and feeds reactions back into Lanes 1 to 3.
- OD drafts; the plant owner, the OD lead and IC approve; IC publishes.
- IC's own process is not yet recorded (the IC brief is to be supplied).

## Vocabulary — one term, one meaning

| Term | Means here | Not to be confused with |
|---|---|---|
| Use Case | A defined shopfloor digitalization solution delivering measurable operational value | Asset (its delivered form) |
| Asset | The delivered form of a use case — Dashboard, Analytics, Report, App or Agent | A connected data point |
| Equipment / Machine Integration | Connecting a machine or workplace to the digital platform for data read/write | Use-case delivery, which comes after |
| Capability | One of the cross-plant templates a use case hangs off | Cluster tag (a classification, not a template) |
| Cluster tag | One of the C01–C12 tags assigned by a deterministic classifier | Capability |
| IIoT Edge | Plant Kubernetes runtime for data acquisition and app deployment | The data platform it offloads to |
| Data platform | Where shopfloor data lands for analysis: the IIoT Edge Platform offloads through Databricks to an Azure Storage Account, main file format Parquet | MSB, the bus; the IIoT Edge runtime |
| MDL | "OESL Manufacturing Data Lake" in older department files, including the new-state lane drafts. **Not used** (owner decision, `docs/derivation.md`): read every MDL in a source as the data platform above | A separate system |
| ContiTech | Named in older department files (lane drafts, decision rights) as shared-service partner and counterpart. **Not used** (owner decision, `docs/derivation.md`): where a decision names ContiTech, the counterpart is the IT-responsible role of the business side | — |
| MSB | Manufacturing Service Bus — use-case enabler / integration backbone | The data platform |
| MES | Manufacturing Execution System — rollout on hold, ERP/S4HANA-dependent | MDA/PDA (acquisition, not execution) |
| MDA/PDA | Machine Data Acquisition / Process Data Acquisition | MES |
| Digitalization Scorecard | The authoritative Power BI report of OD targets vs. actuals and readiness | The Use Case / Equipment Integration reports, which feed it |
| Readiness (RAG) | System integration & availability per dimension × location — red not available, yellow in rollout, green available | — |
| ODEC | Operations Digitalization Exchange Call — **historical** strategy forum (no longer held, no fixed replacement forum; held monthly before it ended); a source of information (past decisions, decks, facts) | COP |
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

- Business-case terms (SMART statement to Tracked / proven) and the acronym list: `references/process-chain-practice.md`, "Vocabulary, second part".

## Where the truth lives

- **Write surface: SharePoint lists.** A correction reaches everyone by being made there, not in a downstream copy.

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

- **Read surfaces.** The Digitalization Scorecard and the two OD Power BI reports (`OD-Report-Use_Case_Integration`, `OD-Report-Equipment_Integration`); **Grafana, a local instance per plant**, where most delivered dashboards are seen; the knowledge graph, rebuilt from the lists, which does **not** pass corrections back.

- **The data path.** Where shopfloor data goes after it is read:

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

- **Global platform, local dashboards.** Databricks and the storage account are the **global** layer (cross-plant analysis); **Grafana is a local instance per plant**, built on that plant's data.
- A line-side dashboard belongs on the local instance, a cross-plant question on the global platform.
- Do not point a plant's Grafana at the global platform, and do not build a cross-plant view on a local one.

- **Shop-floor tools.** The MSB family (rollout backbone), MDA/PDA, MES, MIL, QFPR, Energy Management, RuleEngine, the Data Science Factory and the three machine-integration concepts.
- A **tool** is a system a plant uses; a **connector** reaches a machine; never the same row.

## Procedure

1. Load this skill before any OD work; take terms only from the vocabulary table or its reference.
2. Resolve each term, lane and gate to one meaning; if two sources disagree, the SharePoint list wins, because the lists are the write surface.
3. Find the source in "Where the truth lives" and read the figure live from the list (cite list and export date).
4. Route a gate through `dept-decision-rights`; a decision stays with the named role.
5. If a figure has no source or a term does not resolve, mark it `⟨… — to confirm⟩` and stop; do not fill the gap.
6. Answer in the reply template below; nothing else leaves this skill.

### Reply template

```text
Term / gate / figure: <what was asked>
Meaning or route:     <one meaning, or the owning role and skill>
Source and date:      <list name, export date>  |  ⟨… — to confirm⟩
```

### Example: a quoted figure (fictional)

```text
Request:  "How many use cases are proven at plant X?"
Term:     "proven" = value proven after a SPRINT portfolio review (not tracked, not implemented)
Source:   SmartFactory UseCase Savings + UseCase SavingCalculation, export 2026-01-15 (fictional)
Reply:    Term / gate / figure: proven use cases, plant X
          Meaning or route:     saving rows marked proven after SPRINT review; tracked is reported beside it
          Source and date:      UseCase SavingCalculation, export 2026-01-15 (fictional)
No export date given -> Source and date: ⟨export date — to confirm⟩, no number stated.
```

## Who decides

- The function proposes; other people decide. Most gates sit outside OD, because OD does not own spend, IT platforms or the plant's daily use.
- The five gates: spend (eCR), demand on IT platforms, CSP (standard enough to roll out), into daily use (the plant owns `PRODUCTIVE`), value proven (SPRINT review).
- Thresholds are looked up, never guessed: ask Controlling or the eCR process owner for the current approval policy.
- Routes, authority levels and modes (Tandem, Consultation, Information): `dept-decision-rights` owns them.

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

- Other skills take from here a resolved term, a gate route (`dept-decision-rights`) or a source list.
- Blocked work goes to the OD lead; strategy, priority and rollout matters to the role named in the current approval policy (look up), technical ones may use the **COP**; ODEC is historical, not a route.
- In the OD lead's absence the next-higher management role decides prioritization and rollout within the roadmap; investment stays with the approval body.

## Human gate and AI-agent notes

- An agent may resolve terms, quote a figure only from a live list (cite list and export date), and route.
- It never states an unsourced figure, writes to the graph, or acts on an external machine connection.
- Humans decide every gate named under "Who decides".

## Pitfalls

- Adding tracked and proven savings into one number; quote both, separately (rule 1).
- Reading `UNKNOWN` priority or an empty reliability as low or zero; count them as unknown (rule 3).
- Correcting the knowledge graph instead of the SharePoint list; the graph does not pass corrections back (rule 6).
- Mixing the local Grafana with the global platform: a line-side view is local, a cross-plant question is global.
- Quoting a figure from memory or from an old deck; read it live and cite list and export date.
- Treating a historical forum (ODEC) as a route; it is a source of past decisions only.

## Outputs

- [`outputs.yaml`](outputs.yaml): required outputs, criteria, checks and sign-offs.

## Run record: every skill call, no exception

- Before the first step: `python scripts/run_record.py new <skill-id>` (registry root). The record lists the gate, every criterion, every check and every sign-off of the skill.
- Fill the gate rows. One row not met: set the status to `refused`, name what is missing, stop.
- Write each output into its own file; enter the file, the evidence and the status `done` per criterion row. No evidence, no `done`.
- Run every check of the skill; enter the exit code and the time. A check that does not exit 0 means the output is not done.
- A sign-off is entered only by the role that signs. Until then the status is `awaiting-signoff`, never `done`.
- Close: `python scripts/run_record.py check <record>` must print CLOSABLE. Then set the status.
- A new attempt is a new record with `--supersedes <run-id>`; a record is never overwritten.
- Records live in `runs/` of the working repository and are committed with the work.
- Contract and hook: [`docs/skill-output-contract.md`](../../docs/skill-output-contract.md).

## References

| File | Open when |
|---|---|
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | You need the currency rule for a field, the three demand shapes, plant tiering, the AI maturity check or the handoff contract |
| [`references/swot-and-dependency-seams.md`](references/swot-and-dependency-seams.md) | You test an action against the SWOT, need a dependency seam and its mode, or look for a recorded correction or resolved gap |
| [`references/knowledge-graph-reading.md`](references/knowledge-graph-reading.md) | You answer a question from the knowledge graph or need to know how reliable a node description is |
| [`references/provenance-and-source-catalogue.md`](references/provenance-and-source-catalogue.md) | The content sits in a non-Markdown source, you quote the reference library or a benchmark, or you must tag provenance |
| [`references/background.md`](references/background.md) | You want the why behind a rule, the old-to-new service-line crosswalk or the facts behind a date; never an instruction |
| [`evals/evals.json`](evals/evals.json) | Test cases and trigger queries to run with and without this skill |
