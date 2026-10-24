---
type: Skill Reference
title: Public data models
description: OPC UA for Machinery, EUROMAP and PackML - what each already standardizes, so a signal set is not invented twice.
resource: ../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [signals, opc-ua, euromap, packml]
generated: { by: claude-code/1, at: 2026-08-25T00:00:00Z }
---
# Public data models — do not invent what is already standardized

Before defining a signal set, check whether a published companion specification already
defines it. Adopting one buys three things a local model cannot: **a vendor-neutral name**,
**a defined meaning**, and **machines that arrive already speaking it**.

This matters more here than in most estates, because **two of the four material families —
Plastic and Rubber — are covered by a dedicated companion-specification family (EUROMAP)**,
and machine builders in those segments increasingly ship it.

> **Sourcing.** Facts below come from the specification bodies' own pages, retrieved
> 2026-08-25 and cited inline. The specification documents themselves were not read in
> full — treat the mappings as a starting point to confirm against the current spec, not as
> a conformance statement. ⟨Whether any machine in the estate already exposes one of these
> is not recorded — check per machine.⟩

---

## The landscape, and which applies here

| Model | Body | Covers | Relevance |
|---|---|---|---|
| **OPC UA for Machinery** (VDMA 40001) | VDMA + OPC Foundation | The base building blocks for *all* machinery: identification, state, order management | **All four families.** The foundation to check first |
| **EUROMAP 83** | EUROMAP | General types shared by all plastics and rubber machinery | **Plastic and Rubber** — the base for 77 and 84 |
| **EUROMAP 77** | EUROMAP | Injection moulding machine ↔ MES: machine status, configuration, process and job parameters | **Plastic Injection Molding** process groups |
| **EUROMAP 84** | EUROMAP | Extrusion lines and components — 12 parts | **Extrusion** process groups |
| **PackML** (ISA-TR88.00.02) | ISA / OMAC | 17-state machine state model, modes, PackTags | **The machine-state problem** — see below |
| **umati** | VDMA | The marketing/interoperability initiative carrying OPC UA companion specs to market | How a machine builder describes what it ships |

Sources: [OPC UA for Machinery / VDMA 40001](https://vdma-interoperability-guide.org/OPC_UA/OPC_UA_Information_Layer/VDMA%2040001%20-%20OPC%20UA%20for%20Machinery/) · [EUROMAP OPC UA overview](https://euromap.org/i40/OPCUA) · [EUROMAP 77](https://www.euromap.org/euromap77) · [EUROMAP 83](https://www.euromap.org/euromap83) · [OPC UA for Plastics and Rubber Machinery](https://opcfoundation.org/markets-collaboration/plastics-and-rubber-machinery/) · [ISA-TR88.00.02](https://www.isa.org/products/isa-tr88-00-02-2022-machine-and-unit-states-an-imp) · [umati Machinery](https://umati.org/industries_machinery/)

---

## OPC UA for Machinery (VDMA 40001) — the foundation

Developed by VDMA with the OPC Foundation as **the basic specification for the entire
machinery and plant engineering sector**. It provides *building blocks* that other
specifications and vendor information models pick from, rather than one monolithic model.

Two building blocks map directly onto problems in this estate:

**`MachineIdentification`** — identify a machine uniquely, potentially across several OPC UA
servers, with standardized manufacturer and serial-number information.

> This is what the **Machine List** is trying to be. It already records vendor, PLC model,
> part number and plant per machine — 1,715 rows. Where a machine exposes
> `MachineIdentification`, that inventory can be **read rather than maintained by hand**,
> which is the difference between a list that drifts and one that does not.

**`MachineryItemState`** — a standardized machine state.

> This is the answer to the estate's **eight different names for machine state**. Adopting a
> standard state model means the mapping is defined once against the specification, not
> re-invented per machine — see PackML below for the state vocabulary itself.

## EUROMAP — Plastic and Rubber, which is half the estate

**EUROMAP 83** is the base: general types used by all the plastics and rubber machinery
specs, so that object types usable across several machines are defined only once. **83 is
the one to read first** — 77 and 84 build on it.

**EUROMAP 77** is the injection-moulding machine ↔ MES interface: machine status and
configuration, process and job parameters, and transfer of configuration data sets.

> Directly relevant to the `Plastic Blow Molding` / injection process groups. The estate's
> `EjectedVolume`, `AccuVolumeActual`, `PurgeVolume`, `ShotweightEstimated`, `MeltTemperature`
> family is exactly the parameter set 77 standardizes. **Check 77 before naming another one.**

**EUROMAP 84** covers extrusion lines and components across 12 parts.

> Directly relevant to the estate's extrusion flows and their `MetersPerMinute`,
> `Diameter_sv`, `Zone1_Temperature_sv`, `Screw_Temperature_sv`, `Head_Temperature_sv`
> signals. The `_sv` setpoint convention already in use is the same distinction 84 makes
> between setpoint and actual.

**Metal and Assembly have no equivalent family.** For those, OPC UA for Machinery plus
PackML is the available foundation.

## PackML (ISA-TR88.00.02) — the state model

Defines a common set of machine **states**, **modes** and data structures (PackTags) for
automated machinery, developed by OMAC on the ISA-88 basis. **17 states**: Idle, Starting,
Execute, Completing, Complete, Resetting, Holding, Held, Unholding, Suspending, Suspended,
Unsuspending, Stopping, Stopped, Aborting, Aborted, Clearing — grouped into *acting* states
(the machine is running a sequence) and *wait* states (waiting for a command or condition).

**Why this is the highest-value model to adopt here.** The estate's machine-state family is
its worst: `MachineMode`, `MachineModeNormalized`, `MachineStatus`, `MachineState`,
`MachineStatusMapped`, `MachineOperationMode`, `MachineSetup`, `MachineModeSetup` — 430
references across eight names, plus per-machine integer codes mapped ad hoc in 29 separate
normalization flows.

PackML replaces "what does 15 mean on this machine" with a **fixed vocabulary every plant
already shares**. The mapping from a machine's raw integer to a PackML state is then written
once per machine and reviewed against a standard, instead of being invented in a switch
chain per flow.

The acting/wait split also answers a question the estate currently cannot: **which stops
count as downtime.** `Held` and `Suspended` are different things — one is the machine
waiting on the operator, the other on upstream/downstream — and an availability figure that
merges them is not comparable between lines.

---

## How to use a public model here

1. **Identify the machine's family.** Plastic or Rubber → EUROMAP 83, then 77 or 84.
   Anything → OPC UA for Machinery.
2. **Ask the machine builder what it already exposes.** A machine shipping an OPC UA
   companion spec needs no PLC program change and no tag export — it is the cheapest
   integration available. Put this in the requirement spec **at purchase**, not at
   integration: `od-equipment-integration`'s (guidance route) new-machine branch exists for this.
3. **Map, do not translate.** Where the standard has a name, use the standard's name in the
   data-point label. A local alias defeats the point.
4. **Record the deviation** where the machine cannot supply a standard element.
5. **Keep the raw and the mapped separate** — the raw integer stays available for
   diagnostics; the mapped state is what use cases consume. That is exactly the existing
   `MachineMode` / `MachineModeNormalized` distinction, and it is the one variant pair in the
   estate that is *correct*.

## What adopting one does not solve

- **Unit and scale.** Companion specs define these where they define a value; the estate has
  no written convention of its own. ⟨Confirm.⟩
- **Collection method.** Transition versus sample, and at what interval, stays a local
  decision and stays undocumented unless you write it down.
- **The existing 260 names.** A standard applies to what you build next. Migrating a live
  signal is a breaking change with a migration plan — see the skill's *Do not*.

## Open questions worth answering once

⟨Which machines in the estate already expose an OPC UA companion specification — this is not
recorded anywhere and would change the integration route for every one of them.⟩

⟨Whether the requirement spec used at machine purchase (PRS, Doc ID 215534) already asks for
a companion specification. If not, that is a one-line change with a large downstream effect.⟩

⟨Whether the estate's data model — recorded as *CT Base* — was derived from any of these, or
independently. That decides whether adoption is a migration or a reconciliation.⟩
