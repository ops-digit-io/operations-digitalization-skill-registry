# Operations Digitalization — Skill Registry

The repeatable procedures of **MPEE Operations Digitalization (OD)** at OESL, written as
loadable [Agent Skills](https://code.claude.com/docs/en/skills) and indexed so a person or
an agent can find the right one without reading the whole department.

Derived from the [`ops-knowledge-graph`](https://github.com/ops-digit-io/ops-knowledge-graph)
bundle — specifically its **skill map** (the four service lines' own skills, tasks,
playbooks, metrics and agent briefs) and the **Operations Digitalization department map**
(the department OS core, the smart-factory module, and the `10-Department` practices).
Nothing here was invented; see [`docs/derivation.md`](docs/derivation.md) for the
concept-by-concept trace.

> **Scope note.** The **Digital Unit** material in the knowledge graph is deliberately
> excluded. The Digital Unit will be a new department; this registry describes Operations
> Digitalization as it works today.

## The 23 skills

### Foundation — load first

| Skill | What it settles |
|---|---|
| [`od-context`](skills/od-context/SKILL.md) | The vocabulary, the four service lines, where the truth lives, who decides what, and the seven honesty rules every other skill inherits |

### Lanes — one per service line

| Skill | Trigger | Definition of done | Owner |
|---|---|---|---|
| [`od-use-case-support-service`](skills/od-use-case-support-service/SKILL.md) | Plant use-case demand or a definition-workshop request | Use case defined, prioritized, impact-evaluated, handed to integration with a business case | DBVE |
| [`od-information-integration-service`](skills/od-information-integration-service/SKILL.md) | Equipment integration or data-model harmonization need per roadmap | Machine integrated, signals standardized, data landing on the data platform | IIAE |
| [`od-project-support-consultancy`](skills/od-project-support-consultancy/SKILL.md) | Digital investment project kick-off | Integration project managed to acceptance; application consulted and accepted | IIAE |
| [`od-analytical-support-service`](skills/od-analytical-support-service/SKILL.md) | Analytical or ad-hoc process-insight request | Process diagnostics / analytical insight delivered | DBVE |

### Practices — one repeatable procedure each

| Skill | Use it when |
|---|---|
| [`od-use-case-intake-triage`](skills/od-use-case-intake-triage/SKILL.md) | A request arrives and it is not clear whether it is OD's, which lane, or whether to refuse |
| [`od-use-case-definition`](skills/od-use-case-definition/SKILL.md) | A demand has to become a defined use case, or a workshop needs preparing |
| [`od-benefit-calculation`](skills/od-benefit-calculation/SKILL.md) | A business case is needed, a saving is recorded, or a euro figure is leaving the department |
| [`od-use-case-standardization`](skills/od-use-case-standardization/SKILL.md) | A second plant wants what a first plant has; CSP, cluster tags, the reference library |
| [`od-equipment-integration-assessment`](skills/od-equipment-integration-assessment/SKILL.md) | A plant or wave needs an integration roadmap; a machine's route is unclear |
| [`od-acceptance-test`](skills/od-acceptance-test/SKILL.md) | An integration or solution is being declared done |
| [`od-handover-and-adoption`](skills/od-handover-and-adoption/SKILL.md) | Handing to a plant, or asking whether something is actually in use |
| [`od-data-availability-check`](skills/od-data-availability-check/SKILL.md) | Before promising any answer that depends on shop-floor data |
| [`od-analytics-asset-build`](skills/od-analytics-asset-build/SKILL.md) | Designing or reworking the dashboard, report, app or agent a plant opens |
| [`od-scorecard-reporting`](skills/od-scorecard-reporting/SKILL.md) | Monthly or ODEC reporting; "how is OD tracking?"; preparing or following up a round |
| [`od-portfolio-and-savings-analysis`](skills/od-portfolio-and-savings-analysis/SKILL.md) | Any cut of the 650 use cases or the 553 saving rows |
| [`od-decision-routing`](skills/od-decision-routing/SKILL.md) | "Am I allowed to do this, and if not, who decides?" |
| [`od-sharepoint-list-export`](skills/od-sharepoint-list-export/SKILL.md) | OD source data has to leave SharePoint, with its version history intact |

### Technical — hands-on build guidance, with reference material

| Skill | Use it when | Scope |
|---|---|---|
| [`od-machine-integration-guidance`](skills/od-machine-integration-guidance/SKILL.md) | Deciding how to connect a specific machine — route, connector, and the checklist it must clear | OD |
| [`od-node-red-flow-builder`](skills/od-node-red-flow-builder/SKILL.md) | Writing, reviewing or porting a Node-RED flow on the shop-floor estate | OD |
| [`od-node-red-flow-troubleshooting`](skills/od-node-red-flow-troubleshooting/SKILL.md) | Diagnosing a flow that is silent, wrong, or broken — from its exported JSON | OD |
| [`od-signal-standardization`](skills/od-signal-standardization/SKILL.md) | Analysing a machine's data points and standardizing them so another plant can consume them | OD |
| [`build-grafana-ops-dashboard`](skills/build-grafana-ops-dashboard/SKILL.md) | Building an importable Grafana `.json` over live SQL | portable |

These carry `references/` alongside `SKILL.md`, and for the two derived skills the
references are the substance rather than an appendix:

- **machine integration** (six files, ~1,600 lines) — `decision-paths.md` (the four gates,
  PLC family → available routes, connector selection, dead ends, and a worked routing end to
  end), `softing-datafeed.md` (the Central Aggregation Server from the Softing dataFEED
  **V5.70 manual** with page references: driver list, licensing, per-driver settings, and
  where the OESL guidance does not match the product), `softing-tag-syntax.md` (tag
  identifiers per family), `softing-data-targets.md` (how the data leaves — the OPC UA path
  the edge reads, Store and Forward, the Preprocessing Engine, the unrouted MQTT capability),
  `iiot-edge-platform.md` (the three layers, six phases, hardware sequence, and how to choose
  when both routes are open), `fallbacks.md` (the eight ways an integration blocks and what
  to try first)
- **Node-RED building** (eight files) — the artefact catalogue crawled from all 825 flows,
  the ten transformation patterns with real implementations, how the real-time streaming
  works, the canonical flow walkthrough, the PLCPacket schema, the topic grammar, the
  standard function bodies and the instance inventory
- **Node-RED troubleshooting** — a static analyser (`scripts/analyze_flow.py`) that reads a
  flow JSON and reports the failure modes that actually occur in this estate, plus a
  symptom-to-cause table for what static analysis cannot see
- **signal standardization** — the canonical vocabulary mined from 260 signal names in use,
  the normative KPI standards behind each capability, and an analyser
  (`scripts/analyze_signals.py`) that checks a machine's data points for collisions, raw PLC
  tags and capability coverage gaps

`build-grafana-ops-dashboard` is **vendored** — the author's own skill, body and references
unchanged, keeping its original name rather than an `od-` prefix. Only a `metadata:` block
was added to its frontmatter so it satisfies the registry contract, and
[`OD-INTEGRATION.md`](skills/build-grafana-ops-dashboard/OD-INTEGRATION.md) beside it says
what changes when the dashboard is an OD deliverable. It is the registry's one `portable`
skill; every other skill is `od`-scoped and must require `od-context`, which the validator
enforces.

A consolidated view of what each lane may work with — and what the overlaps mean — is in
[`docs/skill-map.md`](docs/skill-map.md).

## How to use it

**As a person.** Start at `od-context`, then open the lane you are in. The practice skills
are the steps its playbook points at.

**As an agent.** Load `od-context` first — every other skill declares it in
`metadata.requires` and the validator enforces it. Then load the lane or practice skill for
the work in hand; each declares what it composes with.

**In a Claude Code project**, symlink or copy the skills into the skills directory:

```bash
mkdir -p .claude/skills
for s in skills/*/; do ln -sfn "$(pwd)/$s" ".claude/skills/$(basename "$s")"; done
```

## The data path, in one line

```
PLC ──(one of three ingress variants)──► IIoT Edge Platform ──MQTT──► Node-RED
                                                 └── offload ──► Databricks ──► Azure Storage Account (Parquet)
```

**Databricks** is the data platform the IIoT Edge Platform offloads through, the target is an
**Azure Storage Account**, and the main file format is **Parquet**. Anything that reads
shopfloor history reads from there.

**Global platform, local dashboards.** Databricks and the storage account are the global
layer. **Grafana is a local instance per plant**, building that plant's manufacturing
dashboards from that plant's data. A line-side dashboard belongs on the local instance; a
cross-plant question belongs on the global platform.

> The source decks still name an **MDL** and treat **ContiTech** as a shared-services partner
> and standing constraint. **Neither is used.** Both were removed here and in the knowledge
> bundle; the raw exports under `90-Sources/` are never hand-edited, so they still say the old
> thing — see [`docs/derivation.md`](docs/derivation.md) § *Where this registry deliberately
> contradicts the bundle* before regenerating anything.

## What the skills are opinionated about

The registry inherits the department's own rules rather than inventing house style. The
four that change answers most often:

1. **Tracked is not proven.** €2,384,217 tracked and €653,820 finance-proven are both true
   about the same portfolio. They are never added together.
2. **Built is not handed over, and handed over is not in use.** `IMPLEMENTED` and
   `PRODUCTIVE` fail separately, which is why handover has its own tracked state.
3. **Absence is not a zero.** 362 of 650 use cases carry `UNKNOWN` priority; 474 of 553
   saving rows carry no reliability. Reading those as "low" is the most frequent way to be
   wrong about this portfolio.
4. **No figure without a nameable source and a read date**, and no invented figure at all —
   open questions stay `⟨… — to confirm⟩`.

## Figures, and when they were read

Scorecard and Power BI values: **2026-08-10**. Portfolio and savings-ledger figures from
the knowledge bundle: **2026-08-24**. Node-RED flow corpus and machine estate:
**2026-08-25**. All drift — every skill that quotes a number says so and tells you to
refetch. `registry.yaml` carries the three dates as `data_as_of`, `graph_as_of` and
`flows_as_of`.

## Verification status

**Unverified.** The skills were drafted from the knowledge bundle; nobody has read them
line by line against the source systems. That matches the bundle's own trust statement and
is stated rather than glossed. The open gaps the department has not yet closed are listed
in `registry.yaml` under `open_gaps` and appear as `⟨…⟩` in the skills themselves.

## Repository layout

```
registry.yaml                    machine-readable index: tiers, owners, authority levels, open gaps
skills/<skill-id>/SKILL.md       one skill
skills/<skill-id>/references/    supporting material for the technical skills
docs/skill-map.md                the four lanes' skills/tools/interfaces, consolidated
docs/derivation.md               concept-by-concept trace back to the knowledge graph
scripts/validate_registry.py     guard: registry ↔ folders ↔ frontmatter ↔ cross-references
```

## Validating a change

```bash
pip install pyyaml
python3 scripts/validate_registry.py
```

It checks that every folder has a registry entry and vice versa, that frontmatter parses,
that each `name` and `metadata.id` matches its directory, that descriptions are substantial
enough to trigger on, that tiers agree between the two, that every `od`-scoped skill
requires `od-context` while a `portable` one instead ships a real `od_integration` note, and
that no `requires` or `composes` points at a skill that does not exist.

When a source concept changes, follow "Keeping this registry true" in
[`docs/derivation.md`](docs/derivation.md).

---

*Owner: Thomas Zipf (OD lead). Internal — OESL MPEE Operations Digitalization.*
