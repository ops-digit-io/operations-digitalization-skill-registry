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

Read `od-context` first.

Connecting a machine gets you a signal. **Standardizing it is what makes that signal
comparable to the same signal at the other plants** — which is the only reason a
cross-plant capability template means anything.

## Why this is the department's most-recorded blocker

*Data model standardization* is among the most-recorded integration blockers in the estate
(tally the blocker text on the Machine List live). And the flow corpus shows why: **many
distinct signal names for a far smaller set of concepts**.

| Concept | What the variance looks like |
|---|---|
| Machine state | the most names of any concept (raw code, mapped string, status, state, setup...) |
| Part number | several (internal, supplier, gauge, OK/NOK qualified) |
| Counter | several (total, trigger, setup, cycle) |
| Tool id | a few |
| Temperature | a few, one of them a typo that many flows now read |

A misspelled temperature name that many flows read is now an interface: all of them would break
if it were corrected. **That is the cost of not catching a name at creation**, and it is the
whole argument for doing this before a flow is built rather than after.

## The references

| File | Use it for |
|---|---|
| [`references/signal-catalogue.md`](references/signal-catalogue.md) | The canonical vocabulary by family, the variance quantified, the naming rules, and what must never be a signal name |
| [`references/standards.md`](references/standards.md) | The normative KPI definitions — ISO 22400-2, VDI 3423, ISA-95, ISO 22005 — and what each capability's checklist requires *before* you choose signals |
| [`references/multilingual-tags.md`](references/multilingual-tags.md) | **Tags are not in English.** Chinese, German, Spanish, French, Romanian, Hungarian, Slovak/Czech, Serbian and Portuguese terms, the normalization that must happen before any comparison, and why the local name is an alias rather than a replacement |
| [`references/machine-context.md`](references/machine-context.md) | **The other input.** What a PLC program, sequence chart, layout, handbook, HMI or schematic each tells you about how the machine works, with confidence per source and what to do when the context is thin |
| [`assets/signal-analysis-report.md`](assets/signal-analysis-report.md) | The defined output format — the report this skill produces |
| [`references/public-data-models.md`](references/public-data-models.md) | **Check before defining anything.** OPC UA for Machinery (VDMA 40001), EUROMAP 77/83/84 for Plastic and Rubber, PackML's state model — and what each solves here |
| [`references/clustering-signals.md`](references/clustering-signals.md) | Search patterns that sort a raw signal list into functional areas, and the importance score that says what to standardize first |
| [`scripts/analyze_signals.py`](scripts/analyze_signals.py) | Runs the checks, and with `--cluster` the functional-area grouping and ranking |
| [`references/field-signal-vocabulary.md`](references/field-signal-vocabulary.md) | **How to read what is in use on the consuming sides.** The flow-config signal keys and collisions, the `CT` leaf names, display labels in several languages on the dashboards, and the rules that follow |
| [`references/capability-template-signal-sets.md`](references/capability-template-signal-sets.md) | **Per capability template**, what the existing dashboards typically read (signals, variables, data sources), the template boundary, blocker themes to expect and how to look up reference solutions - to set against the requirement sets above |
| [`references/machine-vendor-and-connector-landscape.md`](references/machine-vendor-and-connector-landscape.md) | How to read the machine records by controller vendor, integration route and status, and what each connector family reaches |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | **How the step runs in the chain**: data class and route, information-model layering, the five data-model steps, AI-assisted signal selection, decision rules, handoff contract, AI agent operating notes |
| [`assets/signal-binding-sheet.md`](assets/signal-binding-sheet.md) | **Form.** One row per signal - unit, scale, value type, delta meaning, setpoint or actual, consumers - the record the dashboard exports show is missing |

## Two inputs, one output

**Input A — the tag list.** What the machine emits: the data-point list from the edge
platform, or a tag/symbol export. Machine-readable, and what the analyser consumes —
**in whatever language the PLC programmer thinks in**. The corpus already carries Chinese
(`存储设定值`), German (`Rüstzeit`) and Spanish (`Pza`, `Contador`) tags, and six more plant
languages are in scope. → [`multilingual-tags.md`](references/multilingual-tags.md)

**Input B — the machine context.** How the machine *works*: a PLC program, a sequence or flow
chart, a layout, the handbook, the HMI, an electrical schematic, a proven instance at another
plant, or ten minutes with the setter. → [`machine-context.md`](references/machine-context.md)

> **A tag list without context gives names without meanings** — which is the failure this
> skill exists to prevent. `CycleTime` from two plants is not comparable unless somebody knows
> where each machine's cycle starts, and no tag list carries that.

**The context is not recorded anywhere.** `documentation_available` and `documentation_link`
exist as fields on every machine row and have not been filled (check the live list). So it is
gathered per machine from whatever the plant can produce — and the report says which sources
were used and how far to trust each.

**Output — the signal analysis report.** A defined format, so the result is comparable between
machines and directly usable by the next skill:
[`assets/signal-analysis-report.md`](assets/signal-analysis-report.md).

```bash
python3 scripts/analyze_signals.py points.json --capability oee --report > report.md
```

That fills everything derivable from the tag list — inventory with canonical mapping and a
per-signal action, functional-area clustering and priority, capability coverage, findings, and
a first cut of the action list. **The context sections come out as `⟨…⟩` placeholders**,
deliberately: how the machine works, which sources you used, the standard mapping, units,
collection method and owners cannot be inferred from names, and a report that guessed at them
would be worse than one that asks.

## Step 1 — inventory what exists

The data-point list comes from the IIoT edge platform:

```text
GET {url}/api/datatrons                    → the edge devices
GET {url}/api/datatrons/{id}/devices       → the machines behind one
GET {url}/api/datatrons/{id}/data_points   → the points, each { uuid, label }
```

`uuid` is the identity and the join key; `label` is the human name. **Nothing else is
carried** — no unit, no scale, no collection method, no data type. Everything this skill is
about has to be established outside that contract.

## Step 2 — run the analyser

```bash
python3 scripts/analyze_signals.py points.json
python3 scripts/analyze_signals.py points.json --capability oee
python3 scripts/analyze_signals.py points.csv  --json
```

Takes the `/data_points` response, any JSON array of `{uuid, label}`, or a CSV with those
columns. Exit **2** on blockers, **1** on warnings, **0** clean.

| Check | Severity | Catches |
|---|---|---|
| `missing-uuid`, `duplicate-uuid` | BLOCKER | A point no flow can filter for |
| `unnamed-point` | BLOCKER | A point nothing can describe |
| `name-collision` | BLOCKER | `MachineState` vs `machinestate` — a consumer silently misses half |
| `mixed-script-name` | BLOCKER | `Temp压力` — Latin and non-Latin in one label, unmatchable in both |
| `local-language-name` | WARN | A term in one of nine plant languages, with the canonical suggestion |
| `non-latin-script` | WARN | Chinese, Cyrillic, Japanese, Korean, Greek, Arabic labels |
| `raw-plc-tag` | BLOCKER | `DB15.DBW20`, `_part0_io` — an address is not a name |
| `capability-gap` | BLOCKER | The use case cannot be built to the standard yet |
| `non-canonical-name` | WARN | A known variant of a canonical name |
| `likely-typo` | WARN | `Tempature`, `Vocuum` — before they become interfaces |
| `duplicate-name` | WARN | The same name twice on one machine |
| `outside-catalogue` | INFO | Possibly legitimate, worth checking first |

## Step 2b — establish how the machine works

Before mapping a single name, write three or four sentences: **what it makes, what one cycle
is, where it waits, and what makes a part good.**

If you cannot write that, the context is not yet sufficient and every signal decision after it
is a guess. [`machine-context.md`](references/machine-context.md) says which source answers
which question — the sequence chart gives the cycle boundary and the wait states, the layout
gives the count point, the handbook gives modes, alarm codes and **units**, and the HMI shows
what the operator actually uses, which is the cheapest importance signal available.

Two things worth knowing before you ask for anything:

- **You already need the PLC program.** It is the breakpoint for connecting the machine at
  all, so reading it here is not an extra ask.
- **An archived PLC project is not the deployed program.** A symbol import from last year's
  archive produces tags that connect and read nothing. If the version cannot be confirmed,
  mark those signals Medium confidence and verify against live data before acceptance.

## Step 3 — check whether a public model already defines it

**Do not invent what is already standardized.** Adopting a published companion specification
buys a vendor-neutral name, a defined meaning, and machines that arrive already speaking it.

| Family | Check |
|---|---|
| **Plastic, Rubber** | **EUROMAP 83** (general types), then **77** (injection moulding) or **84** (extrusion). Two of the four material families are covered by a dedicated spec family |
| **Any machine** | **OPC UA for Machinery** (VDMA 40001) — `MachineIdentification` is what the Machine List is trying to be; `MachineryItemState` is the answer to eight names for machine state |
| **Machine state anywhere** | **PackML** (ISA-TR88.00.02) — a fixed state model, and the acting/wait split that decides which stops count as downtime |

Detail, mappings onto the estate's own signals, and the open questions:
[`public-data-models.md`](references/public-data-models.md).

**The cheapest moment to require this is at purchase.** A machine shipping a companion
specification needs no PLC program change and no tag export — put it in the requirement spec,
not in the integration plan.

## Step 4 — cluster and rank what is left

Hundreds of data points, a handful needed. Sort them, then decide what is worth the effort.

```bash
python3 scripts/analyze_signals.py points.json --cluster
```

Groups every signal into a **functional area** (identification, machine state, cycle and
timing, counting, quality and limits, alerting, energy, process values), marks setpoints
separately from actuals, and ranks the areas by **capability coverage × consumer demand** —
both derived from the use-case portfolio, not invented.

**The shortcut that works without scoring anything.** Four families feed most of the
portfolio:

| Signal family | Feeds |
|---|---|
| `MachineStatus` | OEE · Downtime Reporting · Andon Board · Analytics |
| `TotalPartCounter` | OEE · Cycle Time · Analytics · Activity Tracking |
| `CycleStart` / `CycleEnd` | Cycle Time · OEE performance · Process Quality |
| `CurrentValue` + limits | Process Quality Data · SPC Charts · Machine Alerts |

Standardize those on a machine and most of the portfolio becomes buildable on it. The rest
is a long tail worth doing per demand.

**Not standardizing is a valid outcome** — record it as a decision, not an omission. And
treat a low rank as *unknown demand*: `business_process` and `targets` are populated on only
part of the use cases, so the ranking sees only part of the portfolio. Absence is not a zero.

Patterns, the German-language caution and the full scoring model:
[`clustering-signals.md`](references/clustering-signals.md).

## Step 5 — classify each signal

| Class | Test | Then |
|---|---|---|
| **Canonical** | It is in the vocabulary | Use the name as-is |
| **Variant** | Same concept, different spelling | Rename to canonical — before anything consumes it |
| **Local language** | The concept in the plant's language | Map to canonical; **keep the original as an alias** in the report and Machine CV |
| **Genuinely machine-specific** | No other plant has this machine | Keep it, name it by concept, record why |
| **Raw PLC tag** | An address or an internal tag | Must be named. Blocker |
| **Derived** | Computed, not read | It is an *output* data point — see step 5 |

**Most of the long tail is legitimate.** A braider has a braid speed and an extruder does
not. The rule is not "force everything into the catalogue" — it is **qualify, do not coin**:
`Zone1Temperature` rather than a new root concept.

## Step 6 — check against the capability, not the machine

The question is never "what does this machine expose". It is **"what does the use case
need"** — and that comes from the cluster's standard, not from the PLC.

```bash
python3 scripts/analyze_signals.py points.json --capability oee
# → 'oee' needs MachineStatus, TotalPartCounter, CycleTime, StandardSpeed; missing: CycleTime, StandardSpeed
```

**A missing signal is two different problems with two different owners.** Say which:

- **The PLC does not expose it** → machine and engineering. May need a PLC program change,
  which needs the program and somebody able to change it —
  `od-equipment-integration` (guidance route).
- **It exists but is not configured** on the edge platform → integration. Cheap.

Read the capability's requirements checklist in
[`standards.md`](references/standards.md) **before** deciding the signal set. An OEE built
without an agreed ideal cycle time and a documented micro-stop threshold produces a number
that cannot be compared, whatever the signals are called.

## Step 7 — the four things that make a signal standardized

A name alone is not standardization. **A signal is standardized when a second plant can
consume it without asking a question**, and that needs all four:

1. **A canonical name** — [`signal-catalogue.md`](references/signal-catalogue.md).
2. **A defined meaning**, from the cluster's standard — [`standards.md`](references/standards.md).
3. **A stated unit and scale.** ⟨The estate has no written convention — confirm with the
   IIAE. `CycleTime` is seconds by convention; `MetersPerMinute` carries its unit in the
   name, which contradicts the naming rule.⟩
4. **A stated collection method** — transition or sample, and at what interval.

> Two plants publishing `CycleTime`, one measuring load-to-load and the other
> start-to-start, have standardized the name and nothing else. **That failure is invisible
> from the data** and it is what this skill exists to prevent.

## Step 8 — register derived outputs

A flow that derives a signal publishes it under a **new UUID**, and that UUID has to be
registered on the edge platform's data-point config first. It is not something a flow
invents — until it exists, everything downstream ignores the packet.

Name the derived point from the same vocabulary, and make the raw/derived distinction
explicit in the name: `MachineMode` is the raw integer, `MachineModeNormalized` the mapped
string. See `od-node-red-flows`.

## Step 9 — write the report

The output is the report, not a list. Generate the derivable half, then complete the context
sections from Step 2b:

```bash
python3 scripts/analyze_signals.py points.json --capability oee --report > report.md
```

**State the context situation honestly** — *full context* · *tag export only* · *handbook
only* · *nothing but the machine* · *adopting a proven instance*. A report that says
"tag export only, existence unverified" is usable. One that omits it invites the reader to
assume more certainty than exists, and that assumption is how a misspelled name ends up read
by many flows.

The report feeds `od-requirements-breakdown` §5 *Tags of Interest*,
`od-equipment-integration` (guidance route), the flow config in `od-node-red-flows`, and the
Machine CV.

## A word on language

**The canonical name is English; the local name is an alias, not a replacement.** Not because
English is better, but because a name only one plant can read defeats the point of having a
canonical vocabulary at all.

The data-point contract has one label field, so the label carries the canonical name and the
local name lives in the report and the Machine CV. **Never machine-translate a signal name and
use the result directly** — Chinese `设定值` renders as "set value", which reads like a command
rather than a setpoint, and a wrong reading becomes an interface within a few flows. Get a
native reading from the plant. Details, the term table and the normalization:
[`multilingual-tags.md`](references/multilingual-tags.md).

## Decision rights

Changing a data model or a signal standard is **Consultation** at `recommend` authority and
is reversible — IIAE decides after consultation (for a tool or system rollout, in tandem with the IT-responsible role of the business side). Machine standards for
digital connection sit one level up: OD lead, in Consultation with Manufacturing
Engineering, aligned with M+E standards.

An agent may draft and propose a standard change. It may **not** enact one.

## Definition of done

How the machine works written down; the sources used and their confidence recorded; signals
named from the canonical vocabulary; no blockers from the analyser; the capability's
requirement set covered; unit and collection method stated; derived outputs registered; the
report written; and a second plant's instance of the same capability able to consume the
result. Then `od-acceptance-test`.

## Do not

- **Do not fix a standardization gap downstream.** A per-plant transformation buried in a
  Node-RED function or a Grafana query is how comparability is lost — and it is invisible.
- **Do not rename a live signal casually.** It is an interface: many references can depend on one
  misspelling. Renaming is a breaking change with a migration, not a tidy-up.
- **Do not accept a raw PLC tag** into the data-point config. It is unmatched at every other
  plant and silently wrong after the next PLC change.
- **Do not standardize a name without its meaning.** The name is the easy quarter of it, and
  the meaning comes from the machine context, not the tag list.
- **Do not present a guess as a finding.** If a source could not be obtained, say so in the
  report rather than inferring the answer from a name.
- **Do not enact a data-model change.** Propose it.
