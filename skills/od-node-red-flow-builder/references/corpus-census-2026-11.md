---
type: Skill Reference
title: Corpus census 2026-11
description: Re-count of the Node-RED flow corpus on 2026-11-05 - disabled flows, driver mix per site, MQTT settings, triggers and timers, flow-config vocabulary, global context keys, HTTP and UI use - with a correction to the earlier disabled-flow statement.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [information-integration-service, technical, node-red]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Corpus census, read 2026-11-05

This file extends [`instances.md`](instances.md), [`artefacts.md`](artefacts.md) and
[`topic-conventions.md`](topic-conventions.md). It repeats nothing they already say unless a
number changed. **Counts are counts from the export read on 2026-11-05; rules are marked
"Rule".** Nothing here is a statement about the live instances.

## Method and scope

- Source: `ops-knowledge-graph/_knowledge/node-red-auto-docs/docs/` - 53 instance folders,
  825 flow JSON files and 825 generated Markdown pages (counted on 2026-11-05). A "flow" is one
  tab; the file is `[tab, node, node, ...]`.
- Counts were produced by a throw-away script over those 825 JSON files (a node is counted once
  per occurrence; "flows" means files). The analyser of `od-node-red-flow-troubleshooting`
  was re-run over the same 825 files and reproduced the totals in its SKILL.md (40 / 39 / 19 /
  18 / 1 blocker flows, 98 flows with a blocker, 380 without `catch`).
- The flow JSON carries no data, only the flow logic. No UUID, host name, credential or
  e-mail address is reproduced here.

## Correction: disabled flows are not zero

`instances.md` says "No flow in the corpus is marked disabled - 0 of 825" and suspects that
the export drops the state. **That is wrong for this export.** The tab object carries
`disabled: true` and the generated page says `Disabled: Yes`:

| | Flows |
|---|--:|
| Tabs with `disabled: true` | **72** of 825 |
| of these on prod instances / test instances | 35 / 37 |
| Tabs titled `Inject protobuffer config once` (the schema bootstrap tab) | 35, of which 32 disabled |
| Disabled tabs with any other title | 40 |

Reading (inference from the tab titles): the bootstrap tab is *meant* to be disabled after
it has run once, so a disabled `Inject protobuffer config once` is normal, not a fault. The
other 40 are working or abandoned flows - titles such as `AAS test`, `Flow 1`, `Template Flow`,
`OPCUA Server Connection and Read Test`, blow-moulding `Average Melt Temperature per Cycle`
tabs and `Alert System - Call for Help Engineering`. Rule: **before diagnosing "a flow that
does nothing", check whether the tab is disabled on that instance** - it is the cheapest
explanation and it applies to 72 tabs here. Disabled tabs are concentrated in the
`som` test instance (16 of 97) and `som` prod2 (6 of 13).

`ops-knowledge-graph/.../node-red-auto-docs/docs/index.md` (the generated dashboard page)
states a different total: 905 flows, 830 active, 75 inactive. The folder holds 825 files. The
two do not reconcile in the material read. ⟨Which count is current, and whether 80 flows were
generated but not exported - ask whoever runs `generate_docs.py`.⟩ Until then quote the
figure with its source ("825 flow files read on 2026-11-05").

## Flows per site code

22 site codes (the third segment of `ct-oesl-<code>-nodered-...`), 825 flows. Counts are
across prod and test instances of the code:

| Code | Flows | Code | Flows | Code | Flows |
|---|--:|---|--:|---|--:|
| som | 167 | tsaz | 58 | cshz | 14 |
| wth4 | 81 | del | 46 | car | 12 |
| mak | 80 | qda | 43 | cal | 9 |
| sub | 66 | pogz | 39 | dol / mpee | 6 each |
| wth2 | 65 | krb | 33 | wth3 | 4 |
| vac | 31 | spr | 23 | ccn / nomz | 2 each |
| mty | 21 | wth1 | 17 | | |

`wth1` to `wth4` are four instances at one site (see `instances.md`). The code-to-plant table
is still open (⟨site-code table - IIAE⟩); the Connector and Machine notes in the vault do not
carry the node-red code, so it was not derived here.

## What each site builds (flow titles, keyword match)

Counts of flows whose **title** matches a family keyword (a flow can match several; the match is
a keyword test, not a classification). Use it to find who has already built a family, not to
size it.

| Family | Sites with the most matching titles |
|---|---|
| Autoclave / vessel | mak 45, del 35, car 9, cshz 9 |
| Tool / mould | som 33, wth2 8, wth4 8 |
| Part counter | sub 31, som 22, wth4 22, wth2 21, tsaz 13, mak 10 |
| Cycle time | som 25, mak 22, sub 22, del 20, wth4 13 |
| Alerting / notification | som 17, wth2 10, wth4 10, sub 5 |
| Pressure / temperature | mak 30 / 19, wth4 6, tsaz 3 |
| Shift | som 11, wth4 9, wth2 8, del 6, sub 6 |
| OEE | mty 9, del 2 |
| Downtime | som 11, qda 2, sub 3 |
| Scrap / NOK | tsaz 6, vac 4, mak 3 |

Titles that are not findable: `Flow 1` appears on 22 tabs. Rule (already in `artefacts.md`):
name a flow `<asset> - <artefact>`.

## Driver segment per site

Topic family 1 (`datatroniq/data/protob/plc/<edge-device>/<driver>/<id>`) has 1,221 uses. The
`<driver>` segment, counted over `mqtt in` / `mqtt out` nodes:

| Driver | Uses | Sites (uses) |
|---|--:|---|
| `ads` | 437 | som 258, wth4 90, wth2 88, krb 1 |
| `tia` | 246 | sub 60, tsaz 58, krb 31, mak 36, vac 30, wth4 16, del 6, wth2 7, som 2 |
| `cifx` | 184 | sub 48, tsaz 37, krb 23, wth2 21, wth4 21, car 18, vac 12, som 4 |
| `dqcdc` | 130 | mak 90, som 40 |
| `abrock` | 92 | del 73, mty 19 |
| `opcua` | 49 | mak 26, wth4 12, som 11 |
| `ethercat` | 19 | sub 12, tsaz 7 |
| `s7net` | 12 | vac 12 |
| `mqtt` 6, `omron` 2, `omronnxnj` 2 | | mak 6, cal 2, tsaz 2 |

`topic-conventions.md` lists the first five. The vault's Connector notes name the container
image of five of them: `tia` -> `DTQ-TIA-Connector` (image name `datatron-tia-collect`),
`ads` -> `DTQ-Beckhoff-Connector` (`datatron-ads-collect`), `abrock` ->
`DTQ-ALLENBRADLEY-ROCKWELL-Connector` (`datatron-abrock-collect`), `cifx` ->
`DTQ-S7-Connector` (`datatron-cifx`), `omron` -> `DTQ-OMRON FINS-Connector`
(`datatron-omron-collect`). **That is a naming match between the topic segment and the image
name, not a statement in either note** - confirm with the IIAE before using it as a rule. For
`dqcdc`, `opcua`, `ethercat`, `s7net` the Connector notes give no image name:
⟨driver-to-connector table - IIAE⟩.

Connector facts (Graph/Connectors, profile blocks, read 2026-11-05): the TIA connector lists 416
machines at 20 plants, the S7 connector 330 at 20, the Allen-Bradley connector 220 at 6, the
Beckhoff connector 42 at 5, the Omron FINS connector 12 at 2; the Beckhoff connector is the
only one with `ads`, consistent with `topic-conventions.md`.

## MQTT node settings

| Setting | Count |
|---|---|
| `mqtt in` QoS 0 / 1 / 2 | 580 / 45 / 117 |
| `mqtt out` QoS blank (node default) / 2 / 0 / 1 | 601 / 31 / 20 / 9 |
| `mqtt out` retain on | 8 of 661 |
| `mqtt in` payload type: auto 365, buffer 239, auto-detect 89, json 48, utf8 1 | 742 |
| `mqtt out` data type recorded | none (field absent) |

Reading: the spine is read mostly at QoS 0 and published at the node default. QoS 2 is used on
117 inputs - the guarantee is paid for in broker round-trips; ⟨why those flows need it - not
recorded⟩. The `mqtt-datatype-for-protobuf` analyser check (1 flow) concerns an input that is
not `buffer`/`auto`; 239 inputs are explicitly `buffer`, the safe choice for protobuf.

## Triggers and timers

| Pattern | Count |
|---|--:|
| `inject` once after start, no repeat | 725 |
| `inject` with repeat | 66 (+61 that also fire once) |
| `inject` with cron | 147 (+1 once) |
| `inject` manual only | 154 |
| `delay` as fixed pause, 20 ms | 43 |
| `delay` fixed 5 s / 30 ms / 3 s / 500 ms | 20 / 15 / 4 / 3 |
| `rbe` on `payload.isHigh` / `valueString` / `valueInteger` / `valueBool` | 43 / 42 / 32 / 16 |
| `rbei` (ignore initial) on `payload.valueDouble` | 22 |
| `rbe` on the whole `payload` | 13 |
| `catch` scope all / scoped | 446 / 2 |

**Cron times in use** (count of inject nodes): 21:00 (24), 13:00 (19), 05:00 (18), 11:00 (14), 23:00
(12), `0 0-22 * * *` hourly (12), 12:00 (8), 11:30 (6), 05:30 (6), 04:00 (6), 20:00 (6). The
05 / 13 / 21 o'clock triple is a three-shift reset (eight hours apart); 04 / 12 / 20 and
11:30 / 05:30 are other patterns. ⟨Which timezone the instance clock runs in is not recorded in
the flow - check it before trusting any shift reset; see the "shift counter" rows in the
troubleshooting symptoms.⟩

The 20 ms `delay` (43 uses) is placed between split packets to rate-limit; see `streaming.md`.

## Flow-config vocabulary

688 of 825 flows set at least one flow variable; the change node is called `Set flow config` in
662 places (467 unnamed, 136 `Input for calculation`, 110 `Remember cycle start`). 549
distinct flow-variable keys are written; **255 of them start with `datapoint`** (1,506 writes).
The keys are the flow's contract with the machine; the most common, with the number of flows
that write each:

| Key | Flows | Reads as (inference from the name - confirm in the flow's `config flow` comment) |
|---|--:|---|
| `datatronName` | 398 | edge device the flow listens to |
| `machineName` | 245 | machine id / label for the message |
| `datapointTotalPartCounter` | 118 | UUID of the part counter |
| `datapointPartProducedTrigger` | 88 | UUID of the part trigger |
| `cycleStartTime`, `cycleEndTime` | 134 / 130 | remembered timestamps (state, not config) |
| `cycleTimeUUID` | 85 | UUID the derived duration is published under |
| `cycleStartUUID`, `cycleEndUUID` | 47 / 46 | UUIDs of the two events |
| `datapointToolId`, `datapointPartnumber` | 46 / 32 | tool and part-number points |
| `datapointConfig`, `datapointConfigFilter` | 42 / 35 | the UUID set the `filter uuids` node passes |
| `alertVariableName`, `alertmessageConfig`, `error_message_uuid` | 39 / 37 / 37 | alerting flows |
| `ShiftPartProduced`, `datapointShiftPartProduced` | 42 / 35 | shift accumulator |
| `valueUpper/LowerRunningTolerance`, `...StoppedTolerance` | 20 / 20 / 19 / 19 | static limits |

Rule (from `SKILL.md`, restated because the counts back it): every UUID and every limit is a
config key, never a literal. The asset [`../assets/flow-config-contract.md`](../assets/flow-config-contract.md)
turns this into a form.

Naming of the 255 `datapoint*` keys follows the signal vocabulary of
`od-signal-standardization` (see its `field-signal-vocabulary.md`): the key is `datapoint` +
the concept name.

## Global context

`global.get` / `change ... global` appear for a small set of keys, almost all at one site: `TurnoA`,
`TurnoB`, `TurnoC` (79 each), `CounterRun` (45), `resetA/B/C` (40 each), `bigInt` (12). The
function nodes that read `Turno*` sit in the `pogz` instances only. *Turno* is Spanish/Portuguese
for *shift*. Reading (inference): shift state is held **globally** at that site, not per tab -
which means a second flow can overwrite it, and a deploy of any flow on the instance does not
clear it (global context is separate from flow context). ⟨Whether global context storage is
persistent on that instance - ask the plant IIAE.⟩

## HTTP and storage nodes

`http request` nodes: 142 (read 2026-11-05). By target type, host removed: **92 with the URL set at
run time** (empty in the export; `som` 72, `mty` 10), **23 incoming-webhook posts** for chat
notifications (`som` 12, `wth2` 4, `wth4` 4, `cal` 2, `del` 1), **17 calls to a REST gateway**
with `/users`, `/rpc/...` or `/api/...` paths (`wth4` 11, `krb` 3, `spr` 3 - the paths look like
test calls; ⟨what the gateway is - not stated⟩), **5 SOAP calls** to an `ExchangeWS` endpoint
(`som` only; internal address, not reproduced) and 5 others. Methods: GET 70, POST 59, `use
msg.method` 12, DELETE 1.

Other targets: `influxdb out` 39 nodes (`pogz` 37, `spr` 2); OPC UA nodes `OPCUA-IIoT-*`
209 (`pogz` 153, `spr` 24, `qda` 19, `cal` 16); `ui-*`/`ui_*` dashboard nodes 375 across 13 sites
(`wth4` 63, `mpee` 58, `wth3` 57, `sub` 47, `som` 42, `spr` 41, `mty` 30). The `pogz` instance
is therefore the only one that is mainly OPC UA + InfluxDB; the Changshu and Sun Prairie
Grafana dashboards also read InfluxDB (`od-analytics-asset-build`, estate baseline).

## Hygiene numbers that did not change

`node.status` 8, `node.error` 6, `node.warn` 4 across 4,670 function nodes (re-counted,
unchanged from `symptoms.md`). `node.send` 25: functions that emit more than one message.

## What this file cannot tell you

- Whether a flow is deployed and running (the export is configuration, not state).
- What the subflows contain: 5 subflow types are in use (the largest 66 nodes in
  `subflow:e38c467b545b6fe2`); their bodies are not in the per-flow files.
- What any datapoint UUID means - that lives on the edge platform's data-point configuration.
