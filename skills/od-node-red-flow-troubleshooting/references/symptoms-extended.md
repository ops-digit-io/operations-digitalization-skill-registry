---
type: Skill Reference
title: Symptoms extended
description: Where the analyser findings concentrate by site and prod or test, the disabled-tab check, extra symptom rows drawn from the 2026-11-05 re-count, and three worked analyser findings on real corpus flows.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [information-integration-service, technical, node-red]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Symptoms, extended

Adds to [`symptoms.md`](symptoms.md); nothing there is replaced. Counts are from the flow
export read on 2026-11-05 (825 flow files, `ops-knowledge-graph/_knowledge/node-red-auto-docs/docs`)
and from re-running `scripts/analyze_flow.py` unchanged over every file: the totals match the
table in `SKILL.md` (40 secret, 39 not-unpacked, 19 not-repacked, 18 oneof, 1 unpaired; 98 flows
with a blocker; 380 without `catch`).

## 0. First question: is the tab disabled?

72 of 825 tabs carry `disabled: true` (35 on prod instances, 37 on test). 35 tabs are the
schema bootstrap `Inject protobuffer config once`, 32 of them disabled - by design, after the
first run. The other 40 disabled tabs are working or abandoned flows.

| Of the disabled tabs | Findings |
|---|--:|
| with a `spine-severed` finding | 10 of 67 flows with that finding |
| with a blocker | 3 of 98 flows with a blocker |
| with no `catch` | 63 of 380 |

So of the 67 "pipeline severed" findings, **57 are on enabled tabs** and are real "publishes
nothing" candidates; 10 are parked flows. Rule: read the tab's state before reading its
findings. If the tab is disabled on the instance where the symptom was seen, that is the
diagnosis.

## 1. Where the findings concentrate

Number of **flows** with the check, per site code (all instances of the code; `som` counts
prod, prod2, test and test2). Only checks that produce blockers or "publishes nothing" are shown.

| Site | Flows | Secret | sysTime not unpacked / repacked | oneof | Severed | No catch | Output UUID not set | Unset context read |
|---|--:|--:|--:|--:|--:|--:|--:|--:|
| som | 167 | 9 | 1 / 0 | 10 | 9 | 92 | 57 | 14 |
| wth4 | 81 | 10 | 0 / 0 | 0 | 8 | 17 | 21 | 3 |
| mak | 80 | 0 | 0 / 0 | 1 | 10 | 5 | 38 | 2 |
| sub | 66 | 1 | 0 / 0 | 0 | 2 | 62 | 22 | 2 |
| wth2 | 65 | 11 | 0 / 0 | 0 | 5 | 15 | 13 | 1 |
| tsaz | 58 | 1 | 3 / 2 | 0 | 5 | 38 | 19 | 12 |
| del | 46 | 1 | 2 / 0 | 0 | 4 | 8 | 9 | 2 |
| qda | 43 | 0 | 0 / 0 | 0 | 7 | 25 | 0 | 20 |
| pogz | 39 | 0 | 0 / 0 | 0 | 0 | 30 | 0 | 21 |
| krb | 33 | 2 | **17 / 17** | 0 | 4 | 5 | 4 | 4 |
| vac | 31 | 4 | 0 / 0 | 0 | 3 | 4 | 12 | 2 |
| mty | 21 | 0 | 4 / 0 | 7 | 0 | 8 | 0 | 8 |
| wth1 | 17 | 0 | **12** / 0 | 0 | 3 | 17 | 0 | 2 |
| cshz | 14 | 0 | 0 / 0 | 0 | 5 | 13 | 0 | 4 |

Sites not shown (`spr`, `car`, `cal`, `dol`, `mpee`, `wth3`, `ccn`, `nomz`) have no sysTime or
oneof blocker; `cal` has 1 secret. Reading, as counts rather than causes:

- **Timestamp corruption is a `krb` and `wth1` problem in this export** (29 of the 39
  not-unpacked flows). If a symptom is "timestamp wrong" at one of those sites, run the analyser
  on the whole instance first; the cause is probably a pattern copied between flows there.
  Prod carries 33 of the 39 not-unpacked flows, test only 6, so this is not a test-only artefact.
- **oneof violations sit on test instances** (17 of 18): `som` test and `mty` test2. They have
  not reached prod (1 of 18 is on a prod instance).
- **`pogz` and `qda` have no output-UUID warning but many unset context reads (21 / 20)**: those
  flows are OPC UA / InfluxDB or `CT/...` flows, not PLCPacket flows, so the UUID check does not
  apply to them. Do not read "0" as "clean".
- **Secrets are mostly on `wth2`/`wth4` (21 of 40) and `som` (9)**; 21 are on test instances.
  Rotate; do not just delete (see `SKILL.md`).

## 2. More symptom rows

Each row names the layer and the evidence. "Inference" means the cause is read from the
export, not observed on an instance.

| Symptom | Likely cause | Check | Evidence |
|---|---|---|---|
| Machine silent on an `.../ads/...` topic | The machine may not be integrated yet. The Beckhoff connector lists 42 machines at 5 plants, 22 of them `NOT INTEGRATED` and 17 `INTEGRATED` (Graph/Connectors, read 2026-11-05) | Machine List integration status before opening the flow | Connector note |
| Counter jumps to zero at an odd hour | Shift reset is a cron `inject`; the corpus uses 05:00 / 13:00 / 21:00 most (24, 19, 18 injects) and the instance timezone is not recorded in any flow | Compare the inject's cron with the plant shift plan **and** the instance clock | Census |
| Shift state differs between two flows on one instance | At one instance (`pogz`) shift state is **global** (`TurnoA/B/C`, `resetA/B/C`, 79 and 40 uses), so any flow can overwrite it | Search the instance for other writers of the same global key | Census; inference |
| Value read as `undefined` though the other flow writes it | Context keys are case-sensitive and the corpus has name collisions: `PartNumber` vs `Partnumber`, `DownTime` vs `Downtime`, `MachineState` vs `_machine_state`/`_machinestate` among the `datapoint*` keys | Compare the exact spelling at the writer and the reader | Census of 255 keys |
| Signal keyed by a raw PLC-style name (`_part0_io` .. `_part4_io`) | Data point named after an address, not a concept (9 writes in 3 flows at one site) | `od-signal-standardization`, `raw-plc-tag` | Census |
| Notification never arrives | The 23 webhook `http request` nodes (`som` 12, `wth2` 4, `wth4` 4, `cal` 2, `del` 1) fail on the HTTP side; with no `catch` (380 flows) nothing reports it | Does the flow have a `catch`? Does the node status show an HTTP error? | Census; inference |
| `http request` goes to the wrong place | 92 of 142 nodes have no URL in the export - it is set at run time from `msg.url` | Debug `msg.url` before the node | Census |
| Flow is correct but nothing to analyse in subflow | 5 subflow types are in use (largest 66 nodes); the per-flow export does not contain their bodies | Open the subflow on the instance | Census |
| Analyser says "0 blockers" on an OPC UA or InfluxDB flow | The sysTime/oneof checks are written for PLCPacket flows; `pogz` (153 OPC UA nodes) is another shape | Read the flow by hand: endpoint, security, node status | Census; inference |
| Copy of a flow works at no other site | The copy kept the source site's `datatronName`/UUIDs; 398 flows carry that key | Re-fill the config contract (`od-node-red-flow-builder`, `assets/flow-config-contract.md`) | Census |
| Several tabs titled `Flow 1` | 22 tabs have that title; the generated page cannot be found by name | Rename to `<asset> - <artefact>` | Census |

## 3. Three worked findings on real corpus flows

Run with `python3 scripts/analyze_flow.py <file>` on 2026-11-05. Flow names are the tab
labels; instance names are the repository names. No identifiers are reproduced.

**A. Silent timestamp corruption - `Coolant Jacket - Druckprüfung - IO Count Total`
(`ct-oesl-krb-nodered-prod`).** Findings: `systime-not-unpacked` and `systime-not-repacked`,
both BLOCKER. Reading: the flow decodes a `PLCPacketList` and encodes a packet and touches
neither end of `sysTime`. Nothing errors; downstream timestamps are wrong. Fix: add the
unpack function after the decode and the pack function before the encode (the two standard
functions in `od-node-red-flow-builder`, `standard-functions.js`). Because 17 flows at this site
carry the same pair of findings, check the neighbours before fixing one.

**B. oneof violation - `oee Calculator - C1 YX-2` (`ct-oesl-mty-nodered-test2`).** Findings:
BLOCKER `oneof-violation` ("valueDouble, valueInteger" both left set) and WARN
`unset-context-read` (`datapointShiftCycleProduced` read but never written in this flow).
Reading: the output packet carries two value fields, so it encodes to something unintended; the
context read returns `undefined` on this tab. Fix: run the `prepare for protob encoding` change
node that deletes the unused fields (pattern P9); write the key in the config group or move the
reader to the tab that writes it. This tab also sits on a test instance.

**C. Pipeline severed - `BMW Lean Cell - Cycle Time` (`ct-oesl-krb-nodered-prod`).**
Findings: three `spine-severed` WARNs - `DecodeProto`, an unnamed `mqtt out` and `EncodeProto`
have no inbound wire. Reading: the flow moves no data ("publishes nothing"). First confirm the
tab is enabled (it is, in this export), then re-wire mqtt in -> decode -> filter -> split -> ... ->
encode -> mqtt out. Three unnamed or generically named nodes are also why an error from this tab
would not name its source.

## 4. What the analyser still cannot see

- Whether the tab is deployed and the broker connected: the export is configuration only.
- UUID correctness: a wrong UUID looks like a correct one. Check against the live topic.
- Anything inside a subflow, any config node (the corpus has zero), and global context contents.
- The meaning of a threshold: `hardcoded-threshold` finds the literal, not whether it is right.
