---
type: Skill Reference
title: Topic conventions
description: The two topic grammars the 825 flows publish and subscribe to, plus the small tail that follows neither.
resource: ../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [node-red, mqtt, topics]
generated: { by: claude-code/1, at: 2026-08-25T00:00:00Z }
---
# MQTT topic conventions

What the 825 flows actually publish and subscribe to. Two families, plus a small tail.

| Root | Uses | What it is |
|---|--:|---|
| `datatroniq/…` | 1,221 | Protobuf `PLCPacketList` — the machine data spine |
| `CT/…` | 144 | ISA-95-shaped hierarchical topic, one signal per topic |
| `extrusion-cutting/…` | 9 | Line-specific JSON feed |
| `spBv1.0/…` | 4 | Sparkplug B |
| `ProductCounter`, `TEST`, `signal`, `$SYS` | 6 | Ad hoc and broker internals |

## Family 1 — `datatroniq` (the spine)

```
datatroniq/data/protob/plc/<edge-device>/<driver>/<id>
                    │         │             │        └─ data-block or device id — e.g. 2, 111, 811-7
                    │         │             └────────── connector/driver family
                    │         └──────────────────────── edge device host — e.g. ski4-bm01, mx-datatron02
                    └────────────────────────────────── payload encoding: protob
```

**Driver segment vocabulary observed:** `dqcdc` · `cifx` · `tia` · `ads` · `abrock`.
These name the connector family reaching the PLC — see
`od-machine-integration-guidance` for the connector table.

`ads` is the `DTQ-Beckhoff-Connector`, and it is worth knowing that this is the **only ADS
path in the estate**: the Central Aggregation Server's Softing dataFEED has no Beckhoff
driver and no ADS at all. A Beckhoff machine seen on this spine got there through an edge
device, and it cannot be moved to the aggregation server without changing protocol
(Modbus TCP, or a TwinCAT OPC UA server in front).

**Edge device names observed:** `ski4-bm01`…`ski4-bm12`, `mx-datatron02`, `sklx004x`,
`datatron-pink`, `datatron-grazioli`, `ka-tscc41005346`, `ka-tscc41005381`, `csedge004`,
`lj-ed-pots`, `wte0060x`, `hmi-notification-system`.

**A flow normally subscribes and publishes on the same broker and the same family.** It
reads raw packets from one topic and writes a *derived* packet back — with a different
UUID, taken from flow config. The topic may be the same or a sibling; the identity that
must differ is the UUID.

**Wildcards.** `#` is used at the device or block level (`…/ski4-bm11/ads/#`) when a flow
wants everything from one device and filters by UUID in `filter uuids` instead. That is
the house pattern: **subscribe broadly, filter by UUID.** It keeps the topic stable when a
data block is renumbered.

## Family 2 — `CT` (hierarchical, one signal per topic)

```
CT / <BA> / <region> / <country> / <plant> / <area> / <sub-area> / <machine> / <signal>
 │     │       │          │           │        │         │            │           └─ leaf value
 │     │       │          │           │        │         │            └───────────── AC324_Braider
 │     │       │          │           │        │         └────────────────────────── Braider_Area
 │     │       │          │           │        └──────────────────────────────────── AC, Extrusion, Packing, Cure…
 │     │       │          │           └───────────────────────────────────────────── QDA, SPR, CSHZ
 │     │       │          └───────────────────────────────────────────────────────── CHN, USA
 │     │       └──────────────────────────────────────────────────────────────────── AS, NA
 │     └──────────────────────────────────────────────────────────────────────────── OESL, MFS
 └────────────────────────────────────────────────────────────────────────────────── legacy root
```

Observed vocabulary per position:

| Position | Values seen |
|---|---|
| BA | `OESL` (120) · `MFS` (24) |
| Region | `AS` (98) · `NA` (46) |
| Country | `CHN` (98) · `USA` (46) |
| Plant | `QDA` (74) · `SPR` (46) · `CSHZ` (24) |
| Area | `AC` · `Extrusion` · `Autoclave_1/2/3` · `Packing` · `Cover` · `Cure` |
| Sub-area | `Braider_Area` · `Cover_Extrusion_Area` · `Extrusion_301` · `Cure_2` |
| Machine | `AC301/307/311/313/324_Braider` · `AC402_Cover_Extrusion_line` |
| Signal | `production_output` · `MachineStatus` · `StandardOperationTime` · `StandardSpeed` · `RecipeIDRunning` · `ProcessTime` · `ProcessCycleCount` · `*_sv` setpoints · `*_Filtered` |

> **`CT` is a legacy root.** The topic tree, the `ct-oesl-*` instance names and the `OESL` /
> `MFS` business-area segments all date from before the rebrand. **Do not rename them** — a
> topic is an interface and every subscriber breaks, and the doc generator matches instance
> repositories on `^ct-oesl-.*-nodered-(prod|test).*`. Changing either is a data-model and
> tooling decision, not a tidy-up. ⟨Whether a new root is planned — to confirm.⟩

Plant codes here match the Node-RED instance codes: `QDA` → `ct-oesl-qda-*`,
`SPR` → `ct-oesl-spr-*`, `CSHZ` → `ct-oesl-cshz-*`.

**One signal per topic, not a packet.** This family is the *published* shape for
consumers that want a named value at a path — dashboards and other systems. It is the readable counterpart to the UUID-keyed `datatroniq` spine.

**Subscribing uses `#` at the machine level** (`…/AC324_Braider/#`) to take all of a
machine's signals at once — 30 of the 144 `CT` topics end in `#`.

**The `_sv` suffix marks a setpoint** (`Diameter_sv`, `Zone1_Temperature_sv`,
`Head_Temperature_sv`, `Pressure_sv`, `Screw_Temperature_sv`, `Vocuum_sv`), distinct from
the measured value. `_Filtered` marks a smoothed signal (`Pressure_Filtered`,
`Hose_Diameter_Filtered`). Preserve both conventions when adding a signal.

> `Vocuum_sv` is a typo for *vacuum* that is live in the estate. Do not silently "fix" a
> topic name — a topic is an interface, and correcting the spelling breaks every
> subscriber. Raise it as a data-model change per `od-signal-standardization`.

## Choosing a topic for a new derived signal

1. **Deriving a packet for the spine** → publish on `datatroniq/data/protob/plc/…` with a
   new UUID from flow config. Do not reuse the input UUID.
2. **Publishing a named value for consumers** → publish on the `CT/…` hierarchy at the
   machine's path, one signal per topic.
3. **Both** is legitimate and common: the spine keeps the estate uniform, the hierarchy
   makes the value findable.

Never invent a new root. `extrusion-cutting/…` exists and is line-specific; adding a
third family is a data-model decision, not a flow decision.
