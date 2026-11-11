---
type: Skill Reference
title: Corpus census
description: Guidance, no figures - how to census the Node-RED flow corpus live (disabled flows, driver segments, MQTT settings, triggers and timers, flow-config vocabulary, global context, HTTP and UI use) and how to read what the census shows.
resource: ../SKILL.md
status: draft
tags: [information-integration-service, technical, node-red]
---
# Corpus census: how to read and how to obtain

This file extends `instances.md`, `artefacts.md` and
`topic-conventions.md`. It holds **no counts**. Every figure about the estate
(how many flows, instances, drivers, nodes) changes with each export; re-count on the live export
before quoting one, and quote it with its source and date.

## Method and scope

- Source: `ops-knowledge-graph/_knowledge/node-red-auto-docs/docs/` - one folder per instance, one flow
  JSON file and one generated Markdown page per flow. A "flow" is one tab; the file is
  `[tab, node, node, ...]`.
- To count: a throw-away script over the JSON files (a node is counted once per occurrence; "flows"
  means files). The analyser (`scripts/analyze_flow.py`) run over the same files gives the
  blocker and warning tallies.
- The flow JSON carries no data, only the flow logic. Do not reproduce a UUID, host name, credential
  or e-mail address from it.
- A generated dashboard page may state totals (flows, active, inactive) that differ from the number of
  files in the folder. **Two sources that do not reconcile are a data-quality trap:** quote the figure
  with its source ("N flow files read on <date>"), and ask whoever runs `generate_docs.py` which count
  is current.

## Disabled flows

The tab object carries `disabled: true`, and the generated page says `Disabled: Yes`. An earlier
statement that "no flow is disabled" was wrong for the export; the export does keep the state.

How to count: test `disabled` on the first element of each flow file; split by prod/test instance and
by tab title.

How to read it:

- The schema-bootstrap tab `Inject protobuffer config once` is **meant** to be disabled after it has run
  once, so a disabled bootstrap tab is normal, not a fault.
- Other disabled tabs are working flows that were parked, test or template tabs, or abandoned flows.
  Titles to expect: test and template tabs, connection tests, alerting flows.
- Rule: **before diagnosing "a flow that does nothing", check whether the tab is disabled on that
  instance.** It is the cheapest explanation.
- Disabled tabs concentrate on test instances of the busiest sites.

## Flows per site code

The site code is the third segment of `ct-oesl-<code>-nodered-...`. Count flows per code across prod and
test instances of the code. Several codes can belong to one site (numbered instances of the same site;
see `instances.md`). The code-to-plant table is open (⟨site-code table - IIAE⟩); the Connector and
Machine notes in the knowledge base do not carry the node-red code, so do not derive it by guessing.

## What each site builds (flow titles, keyword match)

A keyword test on flow **titles** tells you who has already built a family (autoclave / vessel, tool /
mould, part counter, cycle time, alerting / notification, pressure / temperature, shift, OEE, downtime,
scrap / NOK). A flow can match several families; the match is not a classification. Use it to find who
has built something similar, not to size a family.

Titles that are not findable: default titles such as `Flow 1`. Rule (already in `artefacts.md`): name a
flow `<asset> - <artefact>`.

## Driver segment per site

Topic family 1 (`datatroniq/data/protob/plc/<edge-device>/<driver>/<id>`) carries a `<driver>` segment.
To obtain the live mix: count the segment over `mqtt in` / `mqtt out` nodes, per site code.

Driver families seen: `ads`, `tia`, `cifx`, `dqcdc`, `abrock`, plus `opcua`, `ethercat`, `s7net`,
`mqtt`, `omron`, `omronnxnj`. `topic-conventions.md` lists the first five.

The knowledge base's Connector notes name the container image of several of them: `tia` -> `DTQ-TIA-Connector`
(image name `datatron-tia-collect`), `ads` -> `DTQ-Beckhoff-Connector` (`datatron-ads-collect`),
`abrock` -> `DTQ-ALLENBRADLEY-ROCKWELL-Connector` (`datatron-abrock-collect`), `cifx` ->
`DTQ-S7-Connector` (`datatron-cifx`), `omron` -> `DTQ-OMRON FINS-Connector` (`datatron-omron-collect`).
**That is a naming match between the topic segment and the image name, not a statement in either
note** - confirm with the IIAE before using it as a rule. For `dqcdc`, `opcua`, `ethercat`, `s7net` the
Connector notes give no image name: ⟨driver-to-connector table - IIAE⟩.

The Connector notes also carry per-connector machine and plant counts; read them live in the knowledge base's
Graph/Connectors profile blocks. Note that a driver can be unique to one connector (the `ads` segment is
specific to the Beckhoff connector), which is a useful cross-check between topic and connector.

## MQTT node settings

Fields to read on `mqtt in` / `mqtt out`: QoS, retain, payload data type.

- The spine is read mostly at QoS 0 and published at the node default (blank QoS). A higher QoS is paid
  for in broker round-trips; why a given flow needs it is not recorded in the flow (⟨ask the flow's
  author⟩).
- Retain on `mqtt out` is rare; check it deliberately before turning it on.
- For protobuf, the `mqtt in` data type should be `buffer` or `auto`; the analyser check
  `mqtt-datatype-for-protobuf` flags an input that is neither. `buffer` is the safe choice.
- `mqtt out` nodes usually record no data type at all (field absent).

## Triggers and timers

Patterns to look for and what they mean:

| Pattern | Reading |
|---|---|
| `inject` once after start, no repeat | The usual way to run `Set flow config` and bootstrap tabs |
| `inject` with repeat | Polling or heartbeat; check the interval against the load |
| `inject` with cron | Shift resets and daily jobs; see the timezone trap below |
| `inject` manual only | A button somebody has to press; config lost after redeploy if "once after start" is not ticked |
| `delay` as a fixed short pause | Rate-limiting between split packets; see `streaming.md` |
| `rbe` on `payload.isHigh` / value fields | Edge detection on a flag or value; see P4 |
| `rbei` (ignore initial) | As `rbe`, but the first value after deploy is not passed |
| `rbe` on the whole `payload` | Usually a mistake: a changing timestamp defeats it |
| `catch` scope all vs scoped | Scope all is the house pattern; scoped misses the nodes you forgot |

**Cron times.** Shift resets are typically cron `inject` nodes spaced by the shift length (three
eight-hour shifts is the common triple); other plants use other patterns. ⟨Which timezone the instance
clock runs in is not recorded in the flow - check it against the plant's shift plan before trusting any
shift reset; see the "shift counter" rows in the troubleshooting symptoms.⟩ To list the cron
expressions in use, tally the `crontab` fields of `inject` nodes.

## Flow-config vocabulary

To count: tally the `p` fields of `change` nodes with `pt: flow` and `t: set`; group by key. The change
node is called `Set flow config` in most flows; others use names such as `Input for calculation` or
`Remember cycle start`. Many keys start with `datapoint`.

The keys are the flow's contract with the machine. Common keys and what they read as (inference from the
name - confirm in the flow's `config flow` comment):

| Key | Reads as |
|---|---|
| `datatronName` | edge device the flow listens to |
| `machineName` | machine id / label for the message |
| `datapointTotalPartCounter` | UUID of the part counter |
| `datapointPartProducedTrigger` | UUID of the part trigger |
| `cycleStartTime`, `cycleEndTime` | remembered timestamps (state, not config) |
| `cycleTimeUUID` | UUID the derived duration is published under |
| `cycleStartUUID`, `cycleEndUUID` | UUIDs of the two events |
| `datapointToolId`, `datapointPartnumber` | tool and part-number points |
| `datapointConfig`, `datapointConfigFilter` | the UUID set the `filter uuids` node passes |
| `alertVariableName`, `alertmessageConfig`, `error_message_uuid` | alerting flows |
| `ShiftPartProduced`, `datapointShiftPartProduced` | shift accumulator |
| `valueUpper/LowerRunningTolerance`, `...StoppedTolerance` | static limits |

Rule (from `SKILL.md`): every UUID and every limit is a config key, never a literal. The asset
`../assets/flow-config-contract.md` turns this into a form.

Naming of the `datapoint*` keys follows the signal vocabulary of `mi-signals` (see its
`field-signal-vocabulary.md`): the key is `datapoint` + the concept name. Context keys are
case-sensitive, and spelling variants exist between flows; compare exact spellings.

## Global context

`global.get` / `change ... global` appear for a small set of keys, in practice at one or two sites.
Typical global keys are shift-state flags (for example `TurnoA/B/C`, with matching `resetA/B/C`;
*Turno* is Spanish/Portuguese for *shift*), a run counter and a big-integer helper. Reading
(inference): shift state held **globally** instead of per tab means a second flow can overwrite it, and a
deploy of any flow on the instance does not clear it (global context is separate from flow context).
⟨Whether global context storage is persistent on that instance - ask the plant IIAE.⟩ To find global
use, search function nodes for `global.get` / `global.set` and `change` nodes for `pt: global`, and
list the keys per instance.

## HTTP and storage nodes

`http request` nodes fall into kinds by target. To classify, read the URL field with the host removed:

- URL empty in the export: set at run time from `msg.url` (debug `msg.url` before the node).
- Incoming-webhook posts for chat notifications: fail on the HTTP side; with no `catch` nothing reports.
- Calls to a REST gateway (`/users`, `/rpc/...`, `/api/...` paths): often test calls; ⟨what the gateway
  is - not stated⟩.
- SOAP calls to an internal exchange endpoint.

Methods are GET, POST, `use msg.method`, occasionally DELETE.

Other targets: `influxdb out`; OPC UA nodes `OPCUA-IIoT-*`; `ui-*` / `ui_*` dashboard nodes. One site's
instances are mainly OPC UA + InfluxDB rather than PLCPacket-over-MQTT; Grafana dashboards at some sites
also read InfluxDB (`ops-analytics-asset`). The analyser's sysTime and oneof checks are written for
PLCPacket flows and do not apply to those shapes.

## Hygiene counters

To measure observability discipline, count `node.status`, `node.error` and `node.warn` over function
nodes (see `symptoms.md`). They are barely used; flows drop messages correctly and say nothing about it.
`node.send` indicates functions that emit more than one message.

## What this file cannot tell you

- Whether a flow is deployed and running (the export is configuration, not state).
- What the subflows contain: subflow types are in use and their bodies are not in the per-flow files.
- What any datapoint UUID means - that lives on the edge platform's data-point configuration.
