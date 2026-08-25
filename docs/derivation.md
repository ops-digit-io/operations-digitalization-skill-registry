# How this registry was derived

Every skill in this registry traces to concepts in the `ops-digit-io/ops-knowledge-graph`
bundle. Nothing here was invented. Where the source carried an explicit gap — the `⟨…⟩`
convention — the gap is carried through unchanged rather than filled.

## The two maps used

**The skill map** — the four service lines' own answer to "what may this lane work with,
and what does it repeatedly do":

```
_knowledge/OperationsDigitalization-Department/20-lanes/<lane>/
  skills.md       what the lane may work with, and with which access right
  tasks.md        the recurring tasks, their trigger and their template
  playbook.md     happy path, error paths, wait states, handover / rework rule
  metrics.md      the lane's own metrics, targets and intervention thresholds
  agent-brief.md  may / may not / authority_level / guardrails / escalation
```

**The Node-RED flow corpus** — 825 exported flow JSON files and their generated pages
across 53 `ct-oesl-*-nodered-*` instances, plus the generator that produces them:

```
_knowledge/node-red-auto-docs/docs/<instance>/<Flow_Name>.json   the flow, tab + nodes
_knowledge/node-red-auto-docs/docs/<instance>/<Flow_Name>.md     the generated page
_knowledge/node-red-auto-docs/generate_docs.py                   what reads which field
```

**The machine estate and its integration guidance** — the decision tree the Equipment
integration guide walks, and the machine and connector rows behind it:

```
_knowledge/_apps/machine-integration-guidance-app/rules.json       live tree, 25 q / 27 recs
_knowledge/_apps/machine-integration-guidance-app/rules-next.json  next tree, 35 q / 31 recs
_knowledge/90-Sources/generated/kg_nodes.csv                       1,715 Machine + 26 Connector
```

The raw SharePoint exports under `90-Sources/**/*.json` are Git-LFS pointers and were not
pulled; the machine and connector figures therefore come from the graph export
(`kg_nodes.csv`), which is the same data after the pipeline. Stated here because the two
could drift and the export is the one that was actually read.

**The Operations Digitalization department map** — how the department works:

```
_knowledge/OperationsDigitalization-Department/00-core/   charter, strategy, objectives,
                                                          service catalog, intake, operating
                                                          rhythm, metrics, decision rights,
                                                          risks, portfolio, SWOT, glossary,
                                                          resources
_knowledge/OperationsDigitalization-Department/10-modules/smart-factory-use-case/
                                                          systems-of-record, landscape,
                                                          capabilities, operating-context
_knowledge/10-Department/                                 operating model, use case lifecycle,
                                                          standardization, machine integration,
                                                          handover, savings, decision rights,
                                                          rituals, roles, systems of record
_knowledge/20-Done/                                       delivered methods and tooling
```

## Explicitly out of scope

The **Digital Unit** material — `_knowledge/260825_DU_Pilot_Business-Cases.md` and
`_knowledge/90-Sources/du-overview/**` — is excluded. The Digital Unit is a new department;
this registry describes Operations Digitalization as it works today. Nothing in any skill
is derived from that material.

## Traceability

| Skill | Primary sources |
|---|---|
| `od-context` | `00-core/01-charter`, `04-service-catalog`, `08-decision-rights`, `14-glossary`; `10-Department/Operating model`, `Systems of record`, `Roles and organization` |
| `od-use-case-support-service` | `20-lanes/use-case-support-service/*`; `10-Department/Use case lifecycle` |
| `od-information-integration-service` | `20-lanes/information-integration-service/*`; `10-Department/Machine integration` |
| `od-project-support-consultancy` | `20-lanes/project-support-consultancy/*`; `00-core/12-portfolio` |
| `od-analytical-support-service` | `20-lanes/analytical-support-service/*` |
| `od-use-case-intake-triage` | `00-core/05-intake`, `04-service-catalog`, `01-charter`, `13-swot` |
| `od-use-case-definition` | `20-lanes/use-case-support-service/{playbook,tasks}`; `10-Department/Use case lifecycle`, `Use case standardization` |
| `od-benefit-calculation` | `10-Department/Savings and value tracking`, `Decision rights`; `20-lanes/use-case-support-service/*` |
| `od-use-case-standardization` | `10-Department/Use case standardization`; `20-Done/AI cluster classification`, `Use case portfolio analysis` |
| `od-equipment-integration-assessment` | `10-Department/Machine integration`; `20-Done/Equipment integration guide`; `20-lanes/information-integration-service/*` |
| `od-signal-standardization` | `20-lanes/information-integration-service/*`; `10-modules/smart-factory-use-case/systems-of-record`; `00-core/08-decision-rights` |
| `od-acceptance-test` | `20-lanes/{information-integration-service,project-support-consultancy}/{playbook,tasks,agent-brief}` |
| `od-handover-and-adoption` | `10-Department/Handover`, `Rituals`, `Use case lifecycle` |
| `od-data-availability-check` | `20-lanes/analytical-support-service/{playbook,tasks}`; `10-Department/Machine integration`; `10-modules/.../systems-of-record` |
| `od-analytics-asset-build` | `10-Department/Operating model`, `Rituals`; `20-Done/Grafana dashboard screenshot automation`; `20-lanes/analytical-support-service/*` |
| `od-scorecard-reporting` | `00-core/07-metrics`, `06-operating-rhythm`; all four `20-lanes/*/metrics.md` |
| `od-portfolio-and-savings-analysis` | `20-Done/Use case portfolio analysis`; `10-Department/Savings and value tracking`, `Use case lifecycle`, `Systems of record` |
| `od-decision-routing` | `00-core/08-decision-rights`, `09-risks`; `10-Department/Decision rights` |
| `od-sharepoint-list-export` | `20-Done/SharePoint list export procedure`; `90-Sources/sharepoint-export-playbook.md` |
| `od-machine-integration-guidance` | `machine-integration-guidance-app/dataFEEDOPCSuite_de.pdf` (Softing dataFEED OPC Suite V5.70 manual); `_apps/machine-integration-guidance-app/{rules,rules-next}.json`; `90-Sources/generated/kg_nodes.csv`; `10-Department/Machine integration`; `20-Done/Equipment integration guide` |
| `od-node-red-flow-builder` | `node-red-auto-docs/docs/**` (825 flows); `node-red-auto-docs/generate_docs.py`; `10-Department/Machine integration` |
| `build-grafana-ops-dashboard` | **not derived** — vendored from the author's skill, 2026-08-25 |

## Editorial decisions worth knowing about

**Three tiers, not one flat list.** The source has two natural layers — a department layer
that is true everywhere and a lane layer that is true in one service line — and a third
emerges from the tasks and playbooks: procedures that several lanes run identically
(acceptance testing, handover, data availability). Flattening them would duplicate the
guardrails into every skill, and duplicated guardrails drift.

**`od-context` is a skill, not a preamble.** The glossary and the honesty rules are the
part of the source that most changes an answer, and the source itself says why:
*inconsistent vocabulary is a top agent-failure cause*. Making it loadable means the rules
arrive with the work rather than being restated per skill.

**Figures are quoted with their read date, or not at all.** The Scorecard values are
2026-08-10; the portfolio and ledger figures are from the 2026-08-24 bundle. Both drift.
Every skill that carries a number says when it was read and tells the reader to refetch.

**Gaps stay gaps.** `⟨…⟩` is copied through. A registry that quietly resolves an open
question is worse than one that shows where the department has not decided yet.

**The technical tier is measured, not asserted.** The Node-RED and machine-integration
skills state frequencies (620 of 825 flows carry a *prepare and convert payload* group;
1,032 of 1,715 machines are Siemens; 1 % of flows carry a description) because a house
pattern claimed without a count is one person's preference. Every number in those two
skills was computed over the corpus, and the computation is reproducible from the paths in
the traceability table. Where the corpus is inconsistent, the skill says so rather than
picking a winner.

**One skill is vendored, and it kept its name.** `build-grafana-ops-dashboard` is
domain-generic and already had an identity, including a cross-reference to `/build-dashboard`
that would break under a rename. Its body and its 22 reference files are unchanged; the only
edit is an added `metadata:` block in the frontmatter. That made a second scope necessary:
`od` skills inherit the department's vocabulary and must require `od-context`, while a
`portable` skill instead ships an `od_integration` note saying what changes when it is used
for OD work. The validator enforces both halves, so a future vendored skill cannot quietly
skip the integration note.

**References carry patterns, not statistics.** The machine-integration references were
rebuilt around what a reader has to *do*: `decision-paths.md` (four gates, routing,
connector selection, dead ends), `softing-datafeed.md` (per-driver configuration procedures
for the Central Aggregation Server), `iiot-edge-platform.md` (the six phases and the
hardware sequence) and `fallbacks.md` (the eight ways an integration blocks and what to try
first). An earlier pair of reference files that were mostly estate breakdowns was removed —
a distribution table tells a reader what the estate looks like, not what to do next, and
the few figures that genuinely change a routing decision now sit in `SKILL.md` with the
consequence attached.

**The Softing material is now grounded in the vendor manual, and the disagreements are
reported rather than resolved.** The dataFEED OPC Suite V5.70 manual (1,540 pp.) reached the
bundle after the first pass; the Softing references were rewritten against it with page
references throughout, and two OESL recommendations turned out to describe steps the product
cannot perform — a Beckhoff/ADS data source that does not exist, and a NetLink protocol
discontinued in V5.38. Neither was quietly corrected in the skill: `rules.json` stays
authoritative for what OESL permits and the manual for what the product does, the mismatch
is stated in `SKILL.md` and both references, and the fix is recorded in `registry.yaml` as a
change owed to `rules.json`. A skill that silently patched the guidance would leave the tool
everyone actually uses still wrong.

**A topology error, corrected twice.** An earlier version of the machine-integration skill
presented the IIoT Edge Platform and the Central Aggregation Server as alternative
destinations. They are not: the edge is the terminus, and machines behind the Softing server
are integrated into it **via OPC UA** using the `DTQ-OPCUA-Connector`. The guide says so in
two places — its `IIoT Edge Platform → OPC-UA Server` recommendation *is* that bridge, and
its Siemens S7 aggregation recommendation states the PLCs cannot be connected without the
edge platform as well.

The second correction split the remaining "direct" case in two, giving **three ingress
variants**: PLC → **edge device** with connector → platform; PLC → **connector** → platform,
with no device at the machine; PLC → **aggregation server** → platform. That is not an
invention — it is exactly the three concepts the Tool Overview already records as *Concept 3
— IIoT Edge Computing Platform* (20 plants), *Concept 2 — container-based Machine
Integration* (1 plant), *Concept 1 — Central OPC-UA Server* (11 plants). Reading the rollout
histories also killed a second assumption: **eight plants carry both the edge and the
aggregation concept**, so "which platform does this plant have" is often the wrong question.

Both corrections propagated through all six references, the skill's topology diagram, the
worked example and the two adjacent skills. Wording moved from "two routes" to "three ingress
variants, one terminus", because the earlier phrasing was itself carrying the error.

**One name per thing, stated once.** The sources disagree on what to call the two routes —
the Equipment integration guide says *IIoT Edge Platform* and *Central Aggregation Server*,
the department notes say *IIoT edge computing platform* and *central OPC-UA server*, and the
recommendation bodies add *Softing OPC-UA Aggregation Server* and *Softing DataFeed*. Rather
than pick one and silently rewrite the others, `od-machine-integration-guidance` carries a
Terminology table mapping canonical name to alias to what the thing actually is, states that
the concept and the route are the same thing seen from two sides, and the adjacent skills
(`od-equipment-integration-assessment`, `od-information-integration-service`) now name both
and point here for per-machine routing. The rule for prose: use the guide's wording when
handing someone a procedure, because that is the label on their screen.

**Secrets found in the source are named, never reproduced.** The flow corpus contains 23
literal Teams webhook URLs and 30 literal Bearer tokens. The Node-RED skill states the
counts and makes replacing them a guardrail; no skill or reference file contains one, and
the finding is listed in `registry.yaml` under `open_gaps` so it reaches someone who can
rotate them.

**Some procedures deliberately became one skill, not several.** Signal standardization and
pipeline construction are steps 3 and 4 of one playbook but one write right and one
decision mode, so they are one skill. Acceptance testing appears in two lanes with one
protocol, so it is one skill referenced twice.

## Keeping this registry true

The knowledge graph is the source; this registry is derived. When a lane pack, a core file
or a `10-Department` concept changes:

1. Re-read the changed concept.
2. Update the skills listed against it in the traceability table.
3. Update `last_verified` in the affected skills' frontmatter and the `data_as_of` /
   `graph_as_of` / `flows_as_of` fields in `registry.yaml`.
   For the technical tier, re-run the counts over the corpus rather than editing a figure
   by hand — the numbers are the evidence, and a hand-edited one stops being that.
4. Run `python3 scripts/validate_registry.py`.

Corrections to the underlying facts do not belong here or in the graph — they go to the
SharePoint list that owns them. See `od-context`, "Where the truth lives".

## Verification status

**Unverified.** Every derived skill was drafted from the bundle; nobody has read them line
by line against the source systems. `build-grafana-ops-dashboard` is vendored and carries
its author's own status. That is accurate, not modest — it matches the source bundle's
own trust statement. Add a verification note to a skill's frontmatter once somebody has.
