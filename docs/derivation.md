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
| `od-machine-integration-guidance` | `_apps/machine-integration-guidance-app/{rules,rules-next}.json`; `90-Sources/generated/kg_nodes.csv`; `10-Department/Machine integration`; `20-Done/Equipment integration guide` |
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
