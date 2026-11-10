---
type: Skill Reference
title: Procedure detail
description: The detail behind the signal standardization procedure - why the blocker is so common, the edge-platform data-point contract, the analyser checks, the machine-context test, public data model choice, the four signal families, signal classes, and the language rule.
resource: ../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [signals, analyser, standardization]
generated: { by: claude-code/1, at: 2026-11-06T00:00:00Z }
---
# Procedure detail

Moved out of `SKILL.md`. The procedure and rules stay there; the tables and reasoning are here.

## Why this is the most-recorded blocker

*Data model standardization* is among the most-recorded integration blockers (tally the blocker text on the Machine List live).
The flow corpus shows many distinct signal names for a far smaller set of concepts.

| Concept | What the variance looks like |
|---|---|
| Machine state | the most names of any concept (raw code, mapped string, status, state, setup...) |
| Part number | several (internal, supplier, gauge, OK/NOK qualified) |
| Counter | several (total, trigger, setup, cycle) |
| Tool id | a few |
| Temperature | a few, one a typo that many flows now read |

A misspelled name that many flows read is an interface: all would break if it were corrected. That is the cost of not catching a
name at creation, and the argument for standardizing before a flow is built.

## Two inputs

**A - the tag list**: the data-point list from the edge platform or a tag/symbol export, in whatever language the PLC programmer
thinks in (Chinese, German, Spanish already in the corpus, six more plant languages in scope) -
`multilingual-tags.md`. **B - the machine context**: a PLC program, sequence or flow chart, layout,
handbook, HMI, electrical schematic, a proven instance at another plant, or ten minutes with the setter -
`machine-context.md`.

> A tag list without context gives names without meanings. `CycleTime` from two plants is not comparable unless somebody knows
> where each machine's cycle starts, and no tag list carries that.

`documentation_available` and `documentation_link` exist on every machine row and have not been filled (check live), so context is
gathered per machine and the report says which sources were used and how far to trust each.

## Step 1 - the data-point contract

```text
GET {url}/api/datatrons                    -> the edge devices
GET {url}/api/datatrons/{id}/devices       -> the machines behind one
GET {url}/api/datatrons/{id}/data_points   -> the points, each { uuid, label }
```

`uuid` is the identity and join key; `label` the human name. **Nothing else is carried** - no unit, scale, collection method or
data type. All of that must be established outside this contract.

## Step 2 - the analyser

```bash
python3 scripts/analyze_signals.py points.json
python3 scripts/analyze_signals.py points.json --capability oee
python3 scripts/analyze_signals.py points.csv  --json
python3 scripts/analyze_signals.py points.json --capability oee --report > report.md
```

Takes the `/data_points` response, any JSON array of `{uuid, label}`, or a CSV with those columns. Exit **2** on blockers, **1** on
warnings, **0** clean. `--report` fills everything derivable (inventory with canonical mapping and per-signal action, clustering and
priority, capability coverage, findings, first cut of the action list). The context sections come out as `⟨…⟩` placeholders,
deliberately: how the machine works, sources, standard mapping, units, collection method and owners cannot be inferred from names.

| Check | Severity | Catches |
|---|---|---|
| `missing-uuid`, `duplicate-uuid` | BLOCKER | A point no flow can filter for |
| `unnamed-point` | BLOCKER | A point nothing can describe |
| `name-collision` | BLOCKER | `MachineState` vs `machinestate` - a consumer silently misses half |
| `mixed-script-name` | BLOCKER | `Temp压力` - Latin and non-Latin in one label |
| `local-language-name` | WARN | A term in one of nine plant languages, with the canonical suggestion |
| `non-latin-script` | WARN | Chinese, Cyrillic, Japanese, Korean, Greek, Arabic labels |
| `raw-plc-tag` | BLOCKER | `DB15.DBW20`, `_part0_io` - an address is not a name |
| `capability-gap` | BLOCKER | The use case cannot be built to the standard yet |
| `non-canonical-name` | WARN | A known variant of a canonical name |
| `likely-typo` | WARN | `Tempature`, `Vocuum` - before they become interfaces |
| `duplicate-name` | WARN | The same name twice on one machine |
| `outside-catalogue` | INFO | Possibly legitimate, check first |

## Step 2b - how the machine works

Before mapping a name, write three or four sentences: **what it makes, what one cycle is, where it waits, what makes a part
good.** If you cannot, the context is insufficient and every later decision is a guess. The sequence chart gives the cycle
boundary and wait states, the layout the count point, the handbook modes, alarm codes and **units**, the HMI what the operator
actually uses (the cheapest importance signal). You already need the PLC program (the connection breakpoint), so reading it here
is no extra ask. **An archived PLC project is not the deployed program**: a symbol import from last year's archive produces tags
that connect and read nothing; if the version cannot be confirmed mark those signals Medium confidence and verify on live data
before acceptance.

## Step 3 - public models

| Family | Check |
|---|---|
| Plastic, Rubber | **EUROMAP 83** (general types), then **77** (injection moulding) or **84** (extrusion) |
| Any machine | **OPC UA for Machinery** (VDMA 40001) - `MachineIdentification` is what the Machine List is trying to be; `MachineryItemState` answers the many names for machine state |
| Machine state anywhere | **PackML** (ISA-TR88.00.02) - fixed state model, and the acting/wait split that decides which stops count as downtime |

Adopting a companion specification buys a vendor-neutral name, a defined meaning and machines that arrive speaking it. The
cheapest moment to require it is at purchase (requirement spec, not integration plan): no PLC program change, no tag export.
Detail: `public-data-models.md`.

## Step 4 - cluster and rank

`--cluster` groups signals into functional areas (identification, machine state, cycle and timing, counting, quality and limits,
alerting, energy, process values), marks setpoints separately from actuals, and ranks areas by capability coverage x consumer
demand, both derived from the use-case portfolio. Scoring model and patterns: `clustering-signals.md`.

| Signal family | Feeds |
|---|---|
| `MachineStatus` | OEE, Downtime Reporting, Andon Board, Analytics |
| `TotalPartCounter` | OEE, Cycle Time, Analytics, Activity Tracking |
| `CycleStart` / `CycleEnd` | Cycle Time, OEE performance, Process Quality |
| `CurrentValue` + limits | Process Quality Data, SPC Charts, Machine Alerts |

Standardize those four on a machine and most of the portfolio becomes buildable on it; the rest is a long tail per demand. A low
rank is *unknown demand* (`business_process` and `targets` are populated on only part of the use cases); absence is not a zero.

## Step 5 - classes

| Class | Test | Then |
|---|---|---|
| Canonical | In the vocabulary | Use as-is |
| Variant | Same concept, different spelling | Rename to canonical before anything consumes it |
| Local language | The concept in the plant's language | Map to canonical; **keep the original as an alias** in the report and Machine CV |
| Genuinely machine-specific | No other plant has this machine | Keep, name by concept, record why |
| Raw PLC tag | An address or internal tag | Must be named. Blocker |
| Derived | Computed, not read | An *output* data point (step 8) |

Most of the long tail is legitimate (a braider has a braid speed, an extruder does not). Rule: **qualify, do not coin** -
`Zone1Temperature`, not a new root concept.

## Step 6 - missing signal, two owners

**The PLC does not expose it** -> machine and engineering; may need a PLC program change (program plus someone able to change it;
`od-equipment-integration` guidance route). **It exists but is not configured** on the edge platform -> integration, cheap. Read
the capability's checklist in `standards.md` before deciding the signal set: an OEE without an agreed ideal cycle
time and a documented micro-stop threshold cannot be compared whatever the signals are called.

## Step 7 - the four things

A signal is standardized when a second plant can consume it without asking a question: (1) canonical name
(`signal-catalogue.md`), (2) defined meaning (`standards.md`), (3) stated unit and scale,
(4) stated collection method (transition or sample, at what interval). Two plants publishing `CycleTime`, one load-to-load, the
other start-to-start, have standardized the name and nothing else - invisible from the data.

## Step 8 - derived outputs

A flow that derives a signal publishes it under a **new UUID**, registered on the edge platform's data-point config first; until it
exists, everything downstream ignores the packet. Name from the same vocabulary and make raw/derived explicit: `MachineMode` is the
raw integer, `MachineModeNormalized` the mapped string. See `od-node-red-flow-builder`.

## Step 9 - context situation

State it honestly: *full context*, *tag export only*, *handbook only*, *nothing but the machine*, *adopting a proven instance*. "Tag
export only, existence unverified" is usable; omitting it invites the reader to assume more certainty than exists, and that is how
a misspelled name ends up read by many flows.

## Language

The canonical name is English; the local name is an alias, not a replacement - a name only one plant can read defeats the
vocabulary. The data-point contract has one label field, so the label carries the canonical name and the local name lives in the
report and the Machine CV. **Never machine-translate a signal name and use the result directly**: Chinese `设定值` renders as "set
value", which reads like a command rather than a setpoint. Get a native reading from the plant. Term table and normalization:
`multilingual-tags.md`.
