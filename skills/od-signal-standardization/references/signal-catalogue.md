# The signal catalogue

What the estate actually names its signals, mined from the flow corpus: **260 distinct
signal names across 3,400 references** in 825 flows.

**260 names for a far smaller set of concepts is the finding**, not a curiosity. It is the
measurable form of "the catalogue is built to standardize and has not scaled".

---

## The variance, quantified

The same concept, named up to eight ways:

| Concept | Names in use | References |
|---|---|--:|
| **Machine state** | `MachineMode` · `MachineModeNormalized` · `MachineStatus` · `MachineState` · `MachineStatusMapped` · `MachineOperationMode` · `MachineSetup` · `MachineModeSetup` | 430 |
| **Part number** | `Partnumber` · `InternalPartnumber` · `SupplierPartnumber` · `PartnumberGauge` · `NokPartnumber` · `OkPartnumber` · `ValuePartnumber` | 100 |
| **Tool id** | `ToolId` · `ToolIdContinuous` · `ToolIdChanging` · `ValueToolId` | 193 |
| **Temperature** | `Temperature` · `MeltTemperature` · **`AverageMeltTempature`** *(typo, 34 refs)* | 73 |
| **Counter** | `TotalPartCounter` · `PartCounterTrigger` · `SetupPartCounter` · `TotalCycleCounter` · `MinutesCounter` | 427 |

Some of the variants are legitimate distinctions — `MachineMode` is the raw integer,
`MachineModeNormalized` the mapped string; `ToolIdContinuous` and `ToolIdChanging` are two
different behaviours. **Most are not.** `MachineState` versus `MachineStatus` is one concept
spelled two ways, and a consumer matching on the name silently misses half its machines.

**`AverageMeltTempature` is a misspelling with 34 references.** It is now an interface: 34
places would break if it were corrected. That is the cost of not catching a name at
creation, and the reason this skill exists.

---

## The canonical vocabulary

Use these names. Anything else needs a reason.

### Counting & throughput — 26 names in use, 1,029 references

| Canonical | Is | Type |
|---|---|---|
| `TotalPartCounter` | Cumulative parts produced, from the machine | integer |
| `PartProducedTrigger` | One part completed — an event, not a total | bool / delta |
| `ShiftPartProduced` | Parts this shift — **derived**, needs a reset | integer |
| `TotalCycleCounter` | Cumulative machine cycles | integer |
| `ShiftCycleProduced` | Cycles this shift — derived | integer |

Also observed and legitimate where the process has them: `EjectedVolume`,
`AccuVolumeActual`, `PurgeVolume`, `MetersPerMinute`, `ShotweightEstimated`.

### Cycle & timing — 23 names, 369 references

| Canonical | Is |
|---|---|
| `CycleStart` | Rising edge of a cycle |
| `CycleEnd` | Falling edge |
| `CycleTime` | Derived duration, seconds |
| `CycleTrigger` | A single event marking a cycle |
| `LoadingTime` | Derived duration for a load phase |
| `ProcessTime` | Duration of the process step itself |

`CycleStepChain` (79 refs) is the machine's internal step sequence — genuinely
machine-specific, and correctly not normalized.

### Machine state — 27 names, 430 references

| Canonical | Is |
|---|---|
| `MachineMode` | The **raw** integer from the PLC |
| `MachineModeNormalized` | The mapped **string** — publish this, not the code |
| `MachineStatus` | The consumer-facing state |
| `MachineIsReleased` | Boolean release/enable |
| `MachineSetup` | In setup |

**Publish the name, not the code.** A consumer that has to know 15 means Setup is coupled to
one PLC program. This is what `MachineModeNormalized` exists for, and why a normalization
flow is one of the estate's standard artefacts.

### Process values — 41 names, 339 references

`Pressure` · `Temperature` · `MeltTemperature` · `StandardSpeed` · `HeatingProgram`

The long tail here is real: `Zone1`, `CompressorPressure1/2`, `BraidSpeedSV`, `PitchSV`,
`AccuPushoutPushbutton`. **Process values are the family where machine-specific names are
most often justified** — a braider has a braid speed and an extruder does not. Qualify with
the zone or axis rather than inventing a new concept.

The `_sv` suffix seen on `CT/…` topics marks a **setpoint** as opposed to the measured
value. Keep that distinction; losing it makes a dashboard compare a target with itself.

### Quality & limits — 13 names, 238 references

| Canonical | Is |
|---|---|
| `CurrentValue` | The measured value being judged |
| `HardUpperLimit` / `HardLowerLimit` | Breach = out of tolerance |
| `SoftUpperLimit` / `SoftLowerLimit` | Breach = warning band |
| `UpperTolerance` / `LowerTolerance` | The tolerance band itself |
| `LimitValue` | The target / nominal |
| `EvaluationResult` | The verdict, as a string |

This family is **the most consistently named in the whole estate**, and it is no accident:
it is the one built as a multi-input rule from the start. Consistency follows from having a
model, not from discipline.

### Identification — 14 names, 311 references

`ToolId` · `Partnumber` · `RecipeId`

Qualify a derived variant rather than coining a new root: `Partnumber` with an `Ok`/`Nok`
qualifier is one concept with a state, not two concepts.

### Alerting — 4 names, 20 references

`ErrorActive` · `AlertMessage`

Thin, because alerting is mostly done by CSV lookup on an error **code** rather than by a
named signal per alert. That is the right shape — see the alerting artefact.

---

## What must never be a signal name

**Raw PLC addressing.** The corpus contains `_part0_io`, `_part1_io` … `_part4_io`,
`_automatic`, `_stra`, `_feature0`. These are PLC tag names that reached the data-point
config unchanged.

A name like `DB15.DBW20` or `_part0_io` is:

- **unmatched at any other plant**, because the address is a property of one PLC program;
- **silently wrong after a PLC change**, because the address moves and the name does not;
- **the single most-recorded integration blocker in the estate** — *data model
  standardization*, 23 machines.

The analyser flags these as blockers.

---

## Naming rules

| Rule | Example |
|---|---|
| **PascalCase, no separators** | `TotalPartCounter`, not `total_part_counter` |
| **Concept, not address** | `MeltTemperature`, not `DB20.DBD14` |
| **Qualify, do not coin** | `Zone1Temperature`, not `TempZoneOne` |
| **Raw and derived are different names** | `MachineMode` (int) vs `MachineModeNormalized` (string) |
| **Setpoint marked** | `Pressure` vs `PressureSetpoint` / `_sv` on topics |
| **No units in the name** | `CycleTime` in seconds by convention; record the unit in the data model |
| **Spell it correctly the first time** | Renaming a live point is a breaking change |

⟨The estate has no written unit convention. `CycleTime` is seconds and `MetersPerMinute`
carries its unit in the name, which contradicts the rule above. Confirm the intended
convention with the IIAE before standardizing a new numeric signal.⟩

## Capability requirement sets

What a use case needs before it can be built to the standard — the analyser checks these
with `--capability`:

| Capability | Requires |
|---|---|
| `oee` | `MachineStatus`, `TotalPartCounter`, `CycleTime`, `StandardSpeed` |
| `cycle-time` | `CycleStart`, `CycleEnd` |
| `downtime` | `MachineStatus` |
| `part-count` | `PartProducedTrigger` |
| `tolerance` | `CurrentValue`, `HardUpperLimit`, `HardLowerLimit`, `MachineMode` |
| `traceability` | `ToolId`, `Partnumber`, `RecipeId` |
| `alerting` | `ErrorActive`, `AlertMessage` |

A missing signal is not one problem but two, with different owners: **the PLC does not
expose it** (machine, engineering) or **it is not configured on the edge platform**
(integration). Say which.
