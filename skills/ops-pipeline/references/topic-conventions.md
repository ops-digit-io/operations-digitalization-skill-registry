---
type: Skill Reference
title: Topic conventions
description: The two topic grammars the flows publish and subscribe to, plus the small tail that follows neither; vocabulary and conventions, no usage counts.
resource: ../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [node-red, mqtt, topics]
generated: { by: claude-code/1, at: 2026-08-25T00:00:00Z }
---
# MQTT topic conventions

What the flows actually publish and subscribe to. Two families, plus a small tail. Count usage live from the `mqtt in` / `mqtt out` topic fields; no counts are kept here.

| Root | Prevalence | What it is |
|---|---|---|
| `datatroniq/…` | dominant | Protobuf `PLCPacketList` — the machine data spine |
| `CT/…` | common | ISA-95-shaped hierarchical topic, one signal per topic |
| `extrusion-cutting/…` | rare | Line-specific JSON feed |
| `spBv1.0/…` | rare | Sparkplug B |
| `ProductCounter`, `TEST`, `signal`, `$SYS` | rare | Ad hoc and broker internals |

## Family 1 — `datatroniq` (the spine)

```text
datatroniq/data/protob/plc/<edge-device>/<driver>/<id>
                    │         │             │        └─ data-block or device id — `<id>`
                    │         │             └────────── connector/driver family
                    │         └──────────────────────── edge device host — `<edge-device>`
                    └────────────────────────────────── payload encoding: protob
```

**Driver segment vocabulary:** `dqcdc` · `cifx` · `tia` · `ads` · `abrock` (others exist; see `corpus-census.md`).
These name the connector family reaching the PLC — see
`mi-connector` (guidance route) for the connector table.

`ads` is the `DTQ-Beckhoff-Connector`, and it is worth knowing that this is the **only ADS
path in the estate**: the Central Aggregation Server's Softing dataFEED has no Beckhoff
driver and no ADS at all. A Beckhoff machine seen on this spine got there through an edge
device, and it cannot be moved to the aggregation server without changing protocol
(Modbus TCP, or a TwinCAT OPC UA server in front).

**Edge device names** are host names of the edge devices; list them live from the edge platform
(`GET .../datatrons`), do not copy a remembered list.

**A flow normally subscribes and publishes on the same broker and the same family.** It
reads raw packets from one topic and writes a *derived* packet back — with a different
UUID, taken from flow config. The topic may be the same or a sibling; the identity that
must differ is the UUID.

**Wildcards.** `#` is used at the device or block level (`…/<edge-device>/ads/#`) when a flow
wants everything from one device and filters by UUID in `filter uuids` instead. That is
the house pattern: **subscribe broadly, filter by UUID.** It keeps the topic stable when a
data block is renumbered.

## Family 2 — `CT` (hierarchical, one signal per topic)

```text
CT / <BA> / <region> / <country> / <plant> / <area> / <sub-area> / <machine> / <signal>
 │     │       │          │           │        │         │            │           └─ leaf value
 │     │       │          │           │        │         │            └───────────── <machine>
 │     │       │          │           │        │         └────────────────────────── <sub-area>
 │     │       │          │           │        └──────────────────────────────────── <area>
 │     │       │          │           └───────────────────────────────────────────── QDA, SPR, CSHZ
 │     │       │          └───────────────────────────────────────────────────────── CHN, USA
 │     │       └──────────────────────────────────────────────────────────────────── AS, NA
 │     └──────────────────────────────────────────────────────────────────────────── OESL, MFS
 └────────────────────────────────────────────────────────────────────────────────── legacy root
```

Observed vocabulary per position:

| Position | Values seen |
|---|---|
| BA | `OESL` · `MFS` |
| Region | `AS` · `NA` |
| Country | `CHN` · `USA` |
| Plant | `QDA` · `SPR` · `CSHZ` |
| Area | process area of the plant (`<area>`) |
| Sub-area | cell or line within the area (`<sub-area>`) |
| Machine | `<machine>` (equipment id or name as in the Machine List) |
| Signal | `production_output` · `MachineStatus` · `StandardOperationTime` · `StandardSpeed` · `RecipeIDRunning` · `ProcessTime` · `ProcessCycleCount` · `*_sv` setpoints · `*_Filtered` |

> **`CT` is a legacy root.** The topic tree, the `ct-oesl-*` instance names and the `OESL` /
> `MFS` business-area segments all date from before the rebrand. **Do not rename them** — a
> topic is an interface and every subscriber breaks, and the doc generator matches instance
> repositories on `^ct-oesl-.*-nodered-(prod|test).*`. Changing either is a data-model and
> tooling decision, not a tidy-up. **No migration is planned.** `CT` stays as a permanent
> legacy label — treat it the same as any other interface name that outlived the rebrand.

Plant codes here match the Node-RED instance codes: `QDA` → `ct-oesl-qda-*`,
`SPR` → `ct-oesl-spr-*`, `CSHZ` → `ct-oesl-cshz-*`.

**One signal per topic, not a packet.** This family is the *published* shape for
consumers that want a named value at a path — dashboards and other systems. It is the readable counterpart to the UUID-keyed `datatroniq` spine.

**Subscribing uses `#` at the machine level** (`…/<machine>/#`) to take all of a
machine's signals at once — a common subscription form.

**The `_sv` suffix marks a setpoint** (`<Quantity>_sv`), distinct from
the measured value. `_Filtered` marks a smoothed signal (`<Quantity>_Filtered`).
Preserve both conventions when adding a signal.

> A misspelling can be live in a topic name (a typo for a quantity such as *vacuum*). Do not silently "fix" a
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
