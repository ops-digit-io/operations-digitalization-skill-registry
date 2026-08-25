---
name: od-signal-standardization
description: >-
  Analyse a machine's signals and standardize them so a second plant can consume them
  without asking a question. Inventories the data points an edge platform exposes, checks
  them against the canonical vocabulary and against what a capability actually requires,
  finds the name collisions, raw PLC tags and coverage gaps that stop a use case being
  built, and takes the result through the data-model decision. Use when a machine is newly
  connected and its signals need naming, when a use case cannot be built because a signal
  is missing or ambiguous, when two plants' versions of the same signal will not compare,
  or before publishing any derived data point. Covers the public data models — OPC UA for
  Machinery, EUROMAP, PackML — so a standard is adopted rather than re-invented.
license: Internal — OESL MPEE Operations Digitalization. Not for external distribution.
metadata:
  id: od-signal-standardization
  tier: technical
  lane: information-integration-service
  scope: od
  origin: derived
  owner_role: IIoT Interface & Automation Engineer (IIAE)
  authority_level: recommend on standards ⟨decision counterpart to confirm⟩; configure the offload
  status: stable
  last_verified: 2026-08-25
  corpus: 260 distinct signal names across 3,400 references in 825 flows
  requires: [od-context]
  composes: [od-machine-integration-guidance, od-data-availability-check, od-node-red-flow-builder, od-acceptance-test]
  derived_from:
    - ops-knowledge-graph/_knowledge/node-red-auto-docs/docs/** (signal vocabulary in use)
    - ops-knowledge-graph/_knowledge/90-Sources/org-analysis/usecase-standardization-knowledgebase.md
    - ops-knowledge-graph/_knowledge/10-Department/Use case standardization.md
    - ops-knowledge-graph/.../20-lanes/information-integration-service/{playbook,skills}.md
    - ops-knowledge-graph/.../10-modules/smart-factory-use-case/systems-of-record.md
---

# Signal analysis and standardization

Read `od-context` first.

Connecting a machine gets you a signal. **Standardizing it is what makes that signal
comparable to the same signal at the other thirty-two plants** — which is the only reason a
cross-plant capability template means anything.

## Why this is the department's most-recorded blocker

*Data model standardization* is the single most-recorded integration blocker in the
estate — **23 machines**. And the corpus shows why: **260 distinct signal names across 3,400
references** for a far smaller set of concepts.

| Concept | Names in use |
|---|--:|
| Machine state | **8** |
| Part number | 7 |
| Counter | 5 |
| Tool id | 4 |
| Temperature | 3, one of them a typo with 34 references |

`AverageMeltTempature` is now an interface. Thirty-four places would break if it were
corrected. **That is the cost of not catching a name at creation**, and it is the whole
argument for doing this before a flow is built rather than after.

## The references

| File | Use it for |
|---|---|
| [`references/signal-catalogue.md`](references/signal-catalogue.md) | The canonical vocabulary by family, the variance quantified, the naming rules, and what must never be a signal name |
| [`references/standards.md`](references/standards.md) | The normative KPI definitions — ISO 22400-2, VDI 3423, ISA-95, ISO 22005 — and what each capability's checklist requires *before* you choose signals |
| [`references/public-data-models.md`](references/public-data-models.md) | **Check before defining anything.** OPC UA for Machinery (VDMA 40001), EUROMAP 77/83/84 for Plastic and Rubber, PackML's 17-state model — and what each solves here |
| [`references/clustering-signals.md`](references/clustering-signals.md) | Search patterns that sort a raw signal list into functional areas, and the importance score that says what to standardize first |
| [`scripts/analyze_signals.py`](scripts/analyze_signals.py) | Runs the checks, and with `--cluster` the functional-area grouping and ranking |

## Step 1 — inventory what exists

The data-point list comes from the IIoT edge platform:

```
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
| `raw-plc-tag` | BLOCKER | `DB15.DBW20`, `_part0_io` — an address is not a name |
| `capability-gap` | BLOCKER | The use case cannot be built to the standard yet |
| `non-canonical-name` | WARN | A known variant of a canonical name |
| `likely-typo` | WARN | `Tempature`, `Vocuum` — before they become interfaces |
| `duplicate-name` | WARN | The same name twice on one machine |
| `outside-catalogue` | INFO | Possibly legitimate, worth checking first |

## Step 3 — check whether a public model already defines it

**Do not invent what is already standardized.** Adopting a published companion specification
buys a vendor-neutral name, a defined meaning, and machines that arrive already speaking it.

| Family | Check |
|---|---|
| **Plastic, Rubber** | **EUROMAP 83** (general types), then **77** (injection moulding) or **84** (extrusion). Two of the four material families are covered by a dedicated spec family |
| **Any machine** | **OPC UA for Machinery** (VDMA 40001) — `MachineIdentification` is what the Machine List is trying to be; `MachineryItemState` is the answer to eight names for machine state |
| **Machine state anywhere** | **PackML** (ISA-TR88.00.02) — 17 states, and the acting/wait split that decides which stops count as downtime |

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
treat a low rank as *unknown demand*: `business_process` is populated on 150 of 650 use cases
and `targets` on 59, so the ranking sees a quarter of the portfolio. Absence is not a zero.

Patterns, the German-language caution and the full scoring model:
[`clustering-signals.md`](references/clustering-signals.md).

## Step 5 — classify each signal

| Class | Test | Then |
|---|---|---|
| **Canonical** | It is in the vocabulary | Use the name as-is |
| **Variant** | Same concept, different spelling | Rename to canonical — before anything consumes it |
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
  `od-machine-integration-guidance`.
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
string. See `od-node-red-flow-builder`.

## Decision rights

Changing a data model or a signal standard is **Consultation** at `recommend` authority and
is reversible — IIAE hears ⟨the counterpart, to confirm⟩, then decides. Machine standards for
digital connection sit one level up: OD lead, in Consultation with Manufacturing
Engineering, aligned with M+E standards.

An agent may draft and propose a standard change. It may **not** enact one.

## Definition of done

Signals named from the canonical vocabulary, no blockers from the analyser, the capability's
requirement set covered, unit and collection method stated, derived outputs registered, and
a second plant's instance of the same capability able to consume the result. Then
`od-acceptance-test`.

## Do not

- **Do not fix a standardization gap downstream.** A per-plant transformation buried in a
  Node-RED function or a Grafana query is how comparability is lost — and it is invisible.
- **Do not rename a live signal casually.** It is an interface: 34 references depend on one
  misspelling today. Renaming is a breaking change with a migration, not a tidy-up.
- **Do not accept a raw PLC tag** into the data-point config. It is unmatched at every other
  plant and silently wrong after the next PLC change.
- **Do not standardize a name without its meaning.** The name is the easy quarter of it.
- **Do not enact a data-model change.** Propose it.
