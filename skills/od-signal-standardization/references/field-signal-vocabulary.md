---
type: Skill Reference
title: Field signal vocabulary
description: The signal names actually in use on the flow side (255 flow-config keys, 47 CT leaf names) and on the dashboard side (display labels in four languages), with counts, collisions and the rules that follow.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [information-integration-service, technical, signals]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Field signal vocabulary

`signal-catalogue.md` gives the canonical names. This file shows **what is in use on the two
sides that consume signals** and where the two sides disagree. Counts are from exports read on
2026-11-05; rules are marked as such.

| Side | Source | What was counted |
|---|---|---|
| Flow side | `ops-knowledge-graph/_knowledge/node-red-auto-docs/docs` (825 flow files) | change nodes that set a flow variable named `datapoint<Concept>` |
| Topic side | same files | the last segment of 144 `CT/...` topics |
| Dashboard side | `Work-OpsDigit-Knowledge/Dashboard Exports/Dashboard Notes` (1,010 notes) and `specs/data/dashboard-inventory.jsonl` | "Signal labels used in the queries" lines and template variable names |

A flow-config key is **not** the label stored on the edge platform: it is the name the flow
author gave the UUID inside one flow. The two should be the same word and often are; this file
uses the config key because the edge platform's label list is not in the material read
(⟨data-point label export per edge device - IIAE⟩).

## 1. Flow side: `datapoint<Concept>` keys

255 distinct `datapoint*` keys, 1,506 writes. The first column is the key without the prefix;
"flows" is the number of flows that write it, "sites" the number of site codes.

| Concept (key) | Flows | Sites | Catalogue name | Note |
|---|--:|--:|---|---|
| `TotalPartCounter` | 118 | 8 | `TotalPartCounter` | the most used signal in the estate |
| `PartProducedTrigger` | 88 | 8 | `PartProducedTrigger` | |
| `ToolId` | 46 | 4 | `ToolId` | |
| `Config`, `ConfigFilter` | 42 / 35 | 8 | (flow plumbing) | the UUID set the filter passes; not a signal |
| `ShiftPartProduced` | 35 | 4 | `ShiftPartProduced` | derived, needs a reset |
| `Partnumber` | 32 | 5 | `Partnumber` | collides with `PartNumber` (below) |
| `Pressure` | 24 | 2 | `Pressure` | |
| `CycleTime` | 21 | 6 | `CycleTime` | |
| `CycleStepChain`, `CycleStepChainValue` | 21 / 14 | 3 / 2 | `CycleStepChain` | machine-specific by design |
| `EjectedVolume`, `AccuVolumeActual`, `PurgeVolume` | 21 / 20 / 10 | 1 | listed as legitimate | injection moulding, one site |
| `UpperTolerance`, `LowerTolerance` | 19 / 19 | 1 | `UpperTolerance`... | |
| `MachineStatus` | 19 | 2 | `MachineStatus` | |
| `MachineModeNormalized`, `MachineMode` | 17 / 16 | 5 / 4 | same | raw integer vs mapped string |
| `TotalCycleCounter` | 17 | 3 | `TotalCycleCounter` | |
| `CycleStart`, `CycleStartValue` | 20 / 18 | 2 / 1 | `CycleStart` | |
| `ValueToolId`, `ValuePartnumber` | 16 / 12 | 3 / 1 | variants of `ToolId`, `Partnumber` | `Value` prefix = the compared constant |
| `ShotweightEstimated` | 14 | 1 | listed as legitimate | |
| `LoadingTime` | 12 | 2 | `LoadingTime` | |
| `ProductName`, `StandardSpeed` | 12 / 12 | 2 / 1 | `StandardSpeed` | |
| `MachineIsReleased`, `MachineState`, `MachineSetup` | 11 each | 1 | `MachineIsReleased`, `MachineSetup`; `MachineState` is a variant | one site |
| `MetersPerMinute` | 11 | 1 | unit in the name | contradicts the no-units rule |
| `AverageMeltTempature` | 11 | 1 | typo of `AverageMeltTemperature` | the live misspelling |
| `HardUpper/LowerLimit`, `SoftUpper/LowerLimit`, `LimitValue`, `CurrentValue`, `EvaluationResult` | 9 each | 3 | quality-and-limits family | the most consistent family |
| `MachineModeAutomatic/Manual` (+ `Value`) | 9 each | 3 | per-mode booleans and their codes | |
| `ToolIdContinuous`, `ToolIdChanging` | 10 / 10 | 1 | two behaviours | legitimate distinction |

Counts here are **config-key writes per flow**; the 3,400-reference figure in `SKILL.md` counts
all references and is not comparable. Both agree on the ranking: counting and machine state
dominate.

**The `Value` suffix is a convention to keep.** `MachineModeManualValue` holds the *code* that
means "manual" for this PLC, `MachineModeManual` the UUID. Making the code a config key is the
right shape (the mapping is data, not logic) and it is the part that differs between machines
of the same family.

### Collisions inside the flow vocabulary

Three groups of keys differ only by case or separators:

| Variants | Meaning | Risk |
|---|---|---|
| `Partnumber` / `PartNumber` | part number | a reader on one spelling gets `undefined` from the other |
| `DownTime` / `Downtime` | downtime | same |
| `MachineState` / `_machine_state` / `_machinestate` | machine state | the underscore forms look like raw PLC symbols |

Rule (extends the `name-collision` check of `scripts/analyze_signals.py`, which works on
labels, not on config keys): treat a config key like a signal name - pick one spelling per
concept before the second flow is written.

### Names that come from the PLC, not from a concept

`_part0_io` to `_part4_io` (8 to 9 writes each, in 3 flows at one site) are PLC symbol names that
reached the flow config. This is the `raw-plc-tag` class; the analyser blocks it for labels.
Other non-English keys: `PzaScaneadas_last` (17 writes) and `valor` (24 writes), Spanish for *scanned pieces*
and *value* (see `multilingual-tags.md`).

## 2. Topic side: the `CT/...` leaf names

144 `CT/...` topic uses (`topic-conventions.md` has the grammar). The **last segment** has 47
distinct values; 63 uses are the wildcard `#`. The named ones, by uses: `production_output` 6,
`MachineStatus` 6, `ProcessTime` 5, `StandardOperationTime` 5, `RecipeIDRunning` 4, `StandardSpeed`
4, `ProcessCycleCount` 3, then 2 each for the setpoints `Diameter_sv`, `Zone1_Temperature_sv`,
`Zone2_Temperature_sv`, `Head_Temperature_sv`, `Pressure_sv`, `Screw_Temperature_sv`,
`Vocuum_sv`, `MachineState`, `DownLastTime`.

- Two names for machine state appear on the leaves: `MachineStatus` (6 uses) and `MachineState`
  (2) - the same concept the flow side spells `MachineMode`, `MachineStatus` and `MachineState`.
- Extruder zones are numbered into the name: `Ext_25_Temperature_Zone_1_Escalated`,
  `Ext_35_Temperature_Zone_2_Escalated`. Those topics end at the machine level of the grammar
  (the name sits where the machine id would be), so the machine number and the signal share one
  segment. Rule: one segment, one meaning - machine in the machine segment, signal in the leaf.
- `Escalated` and `_Filtered` are processing qualifiers on a leaf; the catalogue has no entry
  for either. ⟨Meaning of `Escalated` - ask the IIAE who wrote those flows.⟩
- `production_output` is snake_case, the rest PascalCase: two styles on one tree.

The leaf names also reach the dashboards: the Changshu and Sun Prairie Grafana dashboards read
InfluxDB by `topic` tag with the same `CT/OESL/...` path (for example a Changshu vulcanizer
job-information leaf and a Sun Prairie `Cover_1/Line_Running` leaf), so a topic rename breaks a
dashboard as surely as a UUID change breaks a PostgreSQL one.

## 3. Dashboard side: display labels in four languages

The dashboards carry the signal's **display name** next to the value (an alias in the query or a
panel title). 1,010 notes; the most repeated labels and the English reading are below. The
reading of non-English terms is the author's and **must be confirmed by a native speaker
before it is used** (rule from `multilingual-tags.md`).

| Display label | Language | Reading (confirm) | Concept in the catalogue | Dashboards (largest count in one template) |
|---|---|---|---|--:|
| `IO` / `NIO`, `Schicht IO/NIO`, `Zelle 1 IO` | German | OK / not OK | `Partnumber` qualifier `Ok`/`Nok` | 5 |
| `Piezas OK`, `Total piezas`, `Paro (min)`, `Tiempo de ciclo (s)` | Spanish | parts OK, total parts, stop (min), cycle time (s) | counters, `CycleTime` | 2 |
| `合格` / `不合格` | Chinese | pass / fail | OK / NOK parts | 22 |
| `白班开始时间`, `白班结束时间`, `晚班开始时间`, `晚班结束时间` | Chinese | day-shift start / end, evening-shift start / end | shift boundaries | 20 each |
| `最大值`, `起始值` | Chinese | maximum, start value | | 24 |
| `Istwert`, `Zykluszeit`, `Obere/Untere Eingriffsgrenze` | German | actual value, cycle time, upper / lower intervention limit | `CurrentValue`, `CycleTime`, `Hard/SoftLimit` | 3-4 |
| `Turno`, `Etiquetas`, `Usuario`, `Severidad`, `Fecha de registro` | Spanish | shift, tags, user, severity, record date | downtime-entry fields | 10 |
| `Setpoint`, `Actual`, `Min`, `Max`, `Speed actual`, `Speed setpoint` | English | | setpoint / actual | 23 |
| `OEE A`, `OEE P`, `OEE Q`, `OEE_APQ` | English | availability, performance, quality | OEE chain | 20 |

Two things follow. **The same concept is labelled in at least four languages on the display
side while the data model has one name** - that is the argument for a display-name column in the
signal record rather than per-panel strings. And **shift boundaries are being passed as
signals** (the four Chinese shift labels appear in 20 dashboards of one OEE family): a shift is
configuration, not a measurement; see `assets/signal-binding-sheet.md`.

## 4. Rules that follow

1. One spelling per concept across config keys, `CT` leaves and labels - check all three.
2. A qualifier the path or the config already carries does not go into the leaf name.
3. Setpoint and actual are two signals (`_sv`, `SV`/`PV`, `Setpoint`, `Soll`/`Ist` all occur).
4. Code tables (`...Value` keys) are configuration; the signal publishes the name, not the code.
5. A display string is an alias held in one place; never a second name for the data point.
