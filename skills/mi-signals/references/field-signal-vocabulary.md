---
type: Skill Reference
title: Field signal vocabulary
description: How to read the signal names in use on the flow side (flow-config keys, CT leaf names) and on the dashboard side (display labels in several languages) - where the sides disagree, the collisions to expect and the rules that follow. No counts; re-measure on the live corpus.
resource: ../SKILL.md
status: draft
tags: [information-integration-service, technical, signals]
---
# Field signal vocabulary

`signal-catalogue.md` gives the canonical names. This file shows **how to read what is in use on
the two sides that consume signals** and where the two sides disagree. It holds no counts: take
them from the live corpus and name the date. Rules are marked as such.

| Side | Source | What to count |
|---|---|---|
| Flow side | `ops-knowledge-graph/_knowledge/node-red-auto-docs/docs` (flow files) | change nodes that set a flow variable named `datapoint<Concept>` |
| Topic side | same files | the last segment of `CT/...` topics |
| Dashboard side | `Dashboard Exports/Dashboard Notes` and `specs/data/dashboard-inventory.jsonl` | "Signal labels used in the queries" lines and template variable names |

A flow-config key is **not** the label stored on the edge platform: it is the name the flow
author gave the UUID inside one flow. The two should be the same word and often are; this file
uses the config key because the edge platform's label list is not in the material read
(⟨data-point label export per edge device - IIAE⟩).

## 1. Flow side: `datapoint<Concept>` keys

Count the distinct `datapoint*` keys and, per key, the flows that write it and the sites
(site codes) those flows belong to. Counts are **config-key writes per flow**; they are not
comparable with all-references counts of signal names. Both agree on the ranking: counting and
machine state dominate.

How to read the key families (key without the prefix):

| Concept (key) | Catalogue name | Note |
|---|---|---|
| `TotalPartCounter` | `TotalPartCounter` | typically the most used signal in the estate |
| `PartProducedTrigger` | `PartProducedTrigger` | |
| `ToolId` | `ToolId` | |
| `Config`, `ConfigFilter` | (flow plumbing) | the UUID set the filter passes; not a signal |
| `ShiftPartProduced` | `ShiftPartProduced` | derived, needs a reset |
| `Partnumber` | `Partnumber` | collides with `PartNumber` (below) |
| `Pressure` | `Pressure` | |
| `CycleTime` | `CycleTime` | |
| `CycleStepChain`, `CycleStepChainValue` | `CycleStepChain` | machine-specific by design |
| `EjectedVolume`, `AccuVolumeActual`, `PurgeVolume`, `ShotweightEstimated` | listed as legitimate | injection moulding, often one site |
| `UpperTolerance`, `LowerTolerance` | `UpperTolerance`... | |
| `MachineStatus` | `MachineStatus` | |
| `MachineModeNormalized`, `MachineMode` | same | raw integer vs mapped string |
| `TotalCycleCounter` | `TotalCycleCounter` | |
| `CycleStart`, `CycleStartValue` | `CycleStart` | |
| `ValueToolId`, `ValuePartnumber` | variants of `ToolId`, `Partnumber` | `Value` prefix = the compared constant |
| `LoadingTime` | `LoadingTime` | |
| `ProductName`, `StandardSpeed` | `StandardSpeed` | |
| `MachineIsReleased`, `MachineState`, `MachineSetup` | `MachineIsReleased`, `MachineSetup`; `MachineState` is a variant | often one site |
| `MetersPerMinute` | unit in the name | contradicts the no-units rule |
| a misspelled average-temperature key | typo of the `...Temperature` name | the live misspelling: find it with the `likely-typo` check |
| `HardUpper/LowerLimit`, `SoftUpper/LowerLimit`, `LimitValue`, `CurrentValue`, `EvaluationResult` | quality-and-limits family | the most consistent family |
| `MachineModeAutomatic/Manual` (+ `Value`) | per-mode booleans and their codes | |
| `ToolIdContinuous`, `ToolIdChanging` | two behaviours | legitimate distinction |

**The `Value` suffix is a convention to keep.** `MachineModeManualValue` holds the *code* that
means "manual" for this PLC, `MachineModeManual` the UUID. Making the code a config key is the
right shape (the mapping is data, not logic) and it is the part that differs between machines
of the same family.

### Collisions inside the flow vocabulary

Groups of keys that differ only by case or separators. Look for these kinds:

| Variants | Meaning | Risk |
|---|---|---|
| `Partnumber` / `PartNumber` | part number | a reader on one spelling gets `undefined` from the other |
| `DownTime` / `Downtime` | downtime | same |
| `MachineState` / `_machine_state` / `_machinestate` | machine state | the underscore forms look like raw PLC symbols |

Rule (extends the `name-collision` check of `scripts/analyze_signals.py`, which works on
labels, not on config keys): treat a config key like a signal name - pick one spelling per
concept before the second flow is written.

### Names that come from the PLC, not from a concept

PLC symbol names that reached the flow config (patterns like `_part<n>_io`) are the
`raw-plc-tag` class; the analyser blocks it for labels. Also expect keys in the plant's own
language (for example Spanish for *scanned pieces* or *value*; see `multilingual-tags.md`).

## 2. Topic side: the `CT/...` leaf names

`topic-conventions.md` has the grammar. List the **last segment** of every `CT/...` topic; a
share of them will be the wildcard `#`. The named leaves to expect: production output, machine
status, process time, standard operation time, recipe ID running, standard speed, process cycle
count, and setpoints with the `_sv` suffix (diameter, zone and head temperatures, pressure,
screw temperature, vacuum), machine state, down last time.

- Two names for machine state appear on the leaves (`MachineStatus`, `MachineState`) - the same
  concept the flow side spells `MachineMode`, `MachineStatus` and `MachineState`.
- Extruder zones can be numbered into the name (illustrative form:
  `Ext_<n>_Temperature_Zone_<k>_Escalated`). Those topics end at the machine level of the
  grammar (the name sits where the machine id would be), so the machine number and the signal
  share one segment. Rule: one segment, one meaning - machine in the machine segment, signal
  in the leaf.
- `Escalated` and `_Filtered` are processing qualifiers on a leaf; the catalogue has no entry
  for either. ⟨Meaning of `Escalated` - ask the IIAE who wrote those flows.⟩
- Mixed styles on one tree (snake_case next to PascalCase) are a finding.

The leaf names also reach the dashboards: Grafana dashboards that read InfluxDB select by the
`topic` tag with the same `CT/<...>` path, so a topic rename breaks a dashboard as surely as a
UUID change breaks a PostgreSQL one.

## 3. Dashboard side: display labels in several languages

The dashboards carry the signal's **display name** next to the value (an alias in the query or a
panel title). The most repeated labels and their English reading are below. The reading of
non-English terms is the author's and **must be confirmed by a native speaker before it is used**
(rule from `multilingual-tags.md`). Count how many dashboards use each label live.

| Display label | Language | Reading (confirm) | Concept in the catalogue |
|---|---|---|---|
| `IO` / `NIO`, `Schicht IO/NIO`, `Zelle 1 IO` | German | OK / not OK | `Partnumber` qualifier `Ok`/`Nok` |
| `Piezas OK`, `Total piezas`, `Paro (min)`, `Tiempo de ciclo (s)` | Spanish | parts OK, total parts, stop (min), cycle time (s) | counters, `CycleTime` |
| `合格` / `不合格` | Chinese | pass / fail | OK / NOK parts |
| `白班开始时间`, `白班结束时间`, `晚班开始时间`, `晚班结束时间` | Chinese | day-shift start / end, evening-shift start / end | shift boundaries |
| `最大值`, `起始值` | Chinese | maximum, start value | |
| `Istwert`, `Zykluszeit`, `Obere/Untere Eingriffsgrenze` | German | actual value, cycle time, upper / lower intervention limit | `CurrentValue`, `CycleTime`, `Hard/SoftLimit` |
| `Turno`, `Etiquetas`, `Usuario`, `Severidad`, `Fecha de registro` | Spanish | shift, tags, user, severity, record date | downtime-entry fields |
| `Setpoint`, `Actual`, `Min`, `Max`, `Speed actual`, `Speed setpoint` | English | | setpoint / actual |
| `OEE A`, `OEE P`, `OEE Q`, `OEE_APQ` | English | availability, performance, quality | OEE chain |

Two things follow. **The same concept is labelled in several languages on the display
side while the data model has one name** - that is the argument for a display-name column in the
signal record rather than per-panel strings. And **shift boundaries are being passed as
signals** (the Chinese shift labels in an OEE dashboard family): a shift is configuration, not a
measurement; see `assets/signal-binding-sheet.md`.

## 4. Rules that follow

1. One spelling per concept across config keys, `CT` leaves and labels - check all three.
2. A qualifier the path or the config already carries does not go into the leaf name.
3. Setpoint and actual are two signals (`_sv`, `SV`/`PV`, `Setpoint`, `Soll`/`Ist` all occur).
4. Code tables (`...Value` keys) are configuration; the signal publishes the name, not the code.
5. A display string is an alias held in one place; never a second name for the data point.
