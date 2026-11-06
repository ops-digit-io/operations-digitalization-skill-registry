---
name: od-signal-standardization
description: >-
  Analyse a machine's signals and standardize them so a second plant can consume them
  without asking a question. Reads the machine context - PLC program, tag export, sequence or
  flow chart, layout, handbook, HMI, or the machine itself - to establish how the machine
  works, inventories the data points an edge platform exposes, checks
  them against the canonical vocabulary and against what a capability actually requires,
  finds the name collisions, raw PLC tags and coverage gaps that stop a use case being
  built, and takes the result through the data-model decision. Use when a machine is newly
  connected and its signals need naming, when a use case cannot be built because a signal
  is missing or ambiguous, when two plants' versions of the same signal will not compare,
  or before publishing any derived data point. Covers the public data models — OPC UA for
  Machinery, EUROMAP, PackML — so a standard is adopted rather than re-invented, and produces
  a defined signal analysis report as its output.
license: MIT
allowed-tools: Read Grep Glob Bash(python3 scripts/analyze_signals.py:*)
metadata:
  id: od-signal-standardization
  tier: technical
  lane: information-integration-service
  scope: od
  origin: derived
  owner_role: IIoT Interface & Automation Engineer (IIAE)
  authority_level: recommend on standards; configure the offload
  status: stable
  sources_read: 2026-11-05
  requires: [od-context]
  composes: [od-equipment-integration, od-data-availability-check, od-node-red-flows, od-acceptance-test]
  derived_from:
    - ops-knowledge-graph/_knowledge/node-red-auto-docs/docs/** (signal vocabulary in use)
    - ops-knowledge-graph/_knowledge/90-Sources/org-analysis/usecase-standardization-knowledgebase.md
    - ops-knowledge-graph/_knowledge/10-Department/Use case standardization.md
    - ops-knowledge-graph/.../20-lanes/information-integration-service/{playbook,skills}.md
    - ops-knowledge-graph/.../10-modules/smart-factory-use-case/systems-of-record.md
    - Work vault (Work-OpsDigit-Knowledge), Dashboard Exports/specs SPEC-02 Telemetry Data Contract and the dashboard inventory, Dashboard Exports/Dashboard Notes, Graph/Use Case Views (template views and template-standards), Graph/Machines (front matter) and Graph/Connectors, read 2026-11-05
    - Node-RED auto-docs flow JSON, read 2026-11-05 for flow-config keys and CT topic leaves (ops-knowledge-graph/_knowledge/node-red-auto-docs/docs)
  okf:
    type: Agent Skill
    title: Signal analysis and standardization
    tags: [information-integration-service, od, technical]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-08-25T00:00:00Z }
---

# Signal analysis and standardization

Read `od-context` first. Connecting a machine gets you a signal; **standardizing it is what makes it comparable to the same
signal at other plants**, the only reason a cross-plant capability template means anything. Serves process steps **3b4**
(connector and pipeline), **22** (signal selection for a use case) and **1a2** (a template works only on standardized signals).
Key user: IIoT Interface & Automation Engineer (IIAE). AI agent: analyses and proposes, never enacts a standard.
Detail behind each step: [`procedure-detail.md`](references/procedure-detail.md).

## Inputs and output

- **A - tag list**: edge-platform data points (`{uuid, label}`) or a tag/symbol export, any plant language; from `od-equipment-integration`.
- **B - machine context**: PLC program (version confirmed), sequence chart, layout, handbook, HMI, schematic or proven instance; plus the machine CV and integration plan. **A tag list without context gives names without meanings.**
- Also: missing-signal table and verdict from `od-data-availability-check`; tags of interest and stories from `od-requirements-breakdown` (one vocabulary).
- **Output**: [`signal-analysis-report.md`](assets/signal-analysis-report.md) (comparable between machines) and the filled [`signal-binding-sheet.md`](assets/signal-binding-sheet.md) (one row per signal: unit, scale, value type, delta meaning, setpoint or actual, consumers).

```bash
python3 scripts/analyze_signals.py points.json --capability oee --report > report.md
```

The report fills what is derivable; context sections stay `⟨…⟩` placeholders on purpose.

## Procedure

1. **Inventory** the points: `GET .../api/datatrons/{id}/data_points`. Only `uuid` (join key) and `label` exist; unit, scale, method and type must be established outside it.
2. **Run the analyser** (`scripts/analyze_signals.py`); exit 2 = blockers, 1 = warnings, 0 = clean. Checks and severities in `procedure-detail.md`.
3. **Establish how the machine works**: write what it makes, what one cycle is, where it waits, what makes a part good. If you cannot, context is insufficient and every later decision is a guess. Read the PLC program here (it is also the connection breakpoint); an archived project is not the deployed program, so mark Medium confidence and verify on live data.
4. **Check public models first** ([`public-data-models.md`](references/public-data-models.md)): EUROMAP 83/77/84 for plastic and rubber, OPC UA for Machinery (VDMA 40001) for any machine, PackML for machine state. Do not invent what is standardized; require it at purchase.
5. **Cluster and rank** (`--cluster`, [`clustering-signals.md`](references/clustering-signals.md)): start with `MachineStatus`, `TotalPartCounter`, `CycleStart`/`CycleEnd`, `CurrentValue` + limits. A low rank is unknown demand, not zero.
6. **Classify each signal**: canonical, variant, local language, machine-specific, raw PLC tag, derived. **Qualify, do not coin.**
7. **Check against the capability, not the machine** (`--capability`, requirement checklist in [`standards.md`](references/standards.md) before choosing signals). Name the owner of a gap: PLC does not expose it (machine/engineering) vs not configured on the edge (integration, cheap).
8. **Make each signal standardized**: canonical name, defined meaning, stated unit and scale, stated collection method (transition or sample, interval).
9. **Register derived outputs**: a derived signal gets a new UUID registered on the edge platform first; name raw vs derived explicitly (`MachineMode` / `MachineModeNormalized`).
10. **Write the report** and state the context situation (full context, tag export only, handbook only, nothing but the machine, proven instance). Not standardizing is a valid outcome: record it as a decision.

## Decision rules

- Raw PLC tag, name collision, mixed script, missing/duplicate UUID, capability gap -> **blocker**; fix before any flow consumes it.
- Variant or typo -> rename to canonical **before** anything consumes it; a live signal rename is a breaking change with migration.
- Local-language name -> map to canonical, keep the original as alias in report and Machine CV. Never machine-translate a name into the label; get a native reading from the plant.
- Public model covers it -> adopt it. Genuinely machine-specific -> keep, name by concept, record why.
- Missing signal needing a PLC change -> route to `od-equipment-integration` (guidance route).
- Machine-specific barrier -> `od-barrier-triage` (class, owner).
- Data-model or signal-standard change: **Consultation**, IIAE decides (tool or system rollout in tandem with the IT-responsible role of the business side). Machine standards for digital connection: OD lead in Consultation with Manufacturing Engineering, aligned with M+E standards.
- Data class decides the route: transactional -> service bus with OPC-UA; time-series -> MQTT stream; master data -> ERP leads ([`process-chain-practice.md`](references/process-chain-practice.md)).

## Handoff

| To | Carries |
|---|---|
| `od-node-red-flows` (flow config contract) | Canonical names, units, collection method, derived outputs to register; also feeds `od-requirements-breakdown` section 5 (Tags of Interest) |
| `od-acceptance-test`, `od-cross-plant-compatibility` | Report and binding sheet; a second plant can consume it without asking |
| `od-equipment-integration` (guidance), Machine CV | Signals the PLC must expose |
| `od-barrier-triage` | Machine-specific barrier with class and owner |
| IIAE (consultation) | Proposed standard change |

## Human gate and AI-agent notes

- **Agent may**: run the analyser, cluster, draft the report and binding sheet, propose a standard change.
- **Only a human** enacts a data-model or signal-standard change; a native speaker confirms a local-language reading.
- Cite evidence: analyser check id, source of context and its confidence, standard clause. Do not present a guess as a finding; if a source could not be obtained, say so rather than infer from a name.

## Definition of done

How the machine works written down; sources used and confidence recorded; signals named from the canonical vocabulary; no analyser blockers; capability requirement set covered; unit and collection method stated; derived outputs registered; report written; a second plant's instance can consume it. Then `od-acceptance-test`.

## Pitfalls and open points

- **Do not fix a gap downstream**: a per-plant transformation in a Node-RED function or Grafana query hides lost comparability.
- **Do not rename a live signal casually**: many flows can depend on one misspelling.
- **Do not accept a raw PLC tag** into the data-point config: unmatched at other plants, wrong after the next PLC change.
- **Do not standardize a name without its meaning**: meaning comes from the machine context, not the tag list.
- Archived PLC project produces tags that connect and read nothing.
- **Open points**: ⟨Unit and scale: the estate has no written convention - confirm with the IIAE. `CycleTime` is seconds by convention; `MetersPerMinute` carries its unit in the name, which contradicts the naming rule.⟩

## References

| File | Open when |
|---|---|
| [`procedure-detail.md`](references/procedure-detail.md) | Analyser checks, contract, classes, the four things, step detail |
| [`signal-catalogue.md`](references/signal-catalogue.md) | Canonical vocabulary, naming rules, what must never be a signal name |
| [`standards.md`](references/standards.md) | KPI definitions (ISO 22400-2, VDI 3423, ISA-95, ISO 22005) and capability checklists |
| [`multilingual-tags.md`](references/multilingual-tags.md) | Non-English tags: term table, normalization |
| [`machine-context.md`](references/machine-context.md) | What each context source tells you, confidence, thin context |
| [`public-data-models.md`](references/public-data-models.md) | Before defining anything: OPC UA for Machinery, EUROMAP, PackML |
| [`clustering-signals.md`](references/clustering-signals.md) | Functional-area patterns and importance score |
| [`field-signal-vocabulary.md`](references/field-signal-vocabulary.md) | Signal keys, collisions, `CT` leaf names and labels on the consuming sides |
| [`capability-template-signal-sets.md`](references/capability-template-signal-sets.md) | What dashboards per capability template read; blocker themes |
| [`machine-vendor-and-connector-landscape.md`](references/machine-vendor-and-connector-landscape.md) | Machine records by vendor, route and status |
| [`process-chain-practice.md`](references/process-chain-practice.md) | Data class and route, information-model layering, data-model steps, AI-assisted selection, agent notes |
| [`scripts/analyze_signals.py`](scripts/analyze_signals.py) | Run the checks, clustering, report |
