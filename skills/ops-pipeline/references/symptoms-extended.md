---
type: Skill Reference
title: Symptoms extended
description: Guidance, no figures - the disabled-tab check, how to measure where analyser findings concentrate, extra symptom rows, and three illustrative worked findings.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [information-integration-service, technical, node-red]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Symptoms, extended

Adds to [`symptoms.md`](symptoms.md); nothing there is replaced. This page holds no counts of the
estate. Every "how often" question is answered by running `scripts/analyze_flow.py` over the
instance exports on the day (`--quiet` for a whole instance, `--json` to tally) and by counting in
the flow export itself.

## 0. First question: is the tab disabled?

A tab can carry `disabled: true`. Some are disabled by design (for example the one-shot schema
bootstrap tab `Inject protobuffer config once`, which is turned off after its first run); others
are working flows that were parked, or abandoned.

To count them live: read the first element of each flow export (`[tab, ...nodes]`) and test
`disabled`. Cross-tabulate against the analyser findings.

What to expect: findings on a disabled tab are not "live" faults. A `spine-severed` finding on an
enabled tab is a real "publishes nothing" candidate; on a disabled tab it is a parked flow. The same
applies to `no-catch` and blockers. Rule: read the tab's state before reading its findings. If the
tab is disabled on the instance where the symptom was seen, that is the diagnosis.

## 1. Where findings tend to concentrate, and how to measure it

Analyser findings are not spread evenly. They cluster by **site code** (the instance repository name
carries it) and by **prod versus test**. To get the live picture: run the analyser over every flow in
each instance directory, tally the check names per site code and per environment, and compare.

Patterns to expect, to be confirmed by the tally rather than assumed:

- **Timestamp corruption clusters at the sites where one flow was copied to build the next.** If the
  symptom is "timestamp wrong" at a site, run the analyser on the whole instance first; the cause is
  probably a pattern copied between flows there. Check the neighbours before fixing one flow. Do not
  assume it is a test-only artefact: prod instances carry it too.
- **`oneof` violations tend to sit on test instances,** where flows are still being built. Confirm
  whether the same flow exists on prod.
- **OPC UA and InfluxDB-style instances show no output-UUID warning but many unset context reads.**
  Those flows are not PLCPacket flows, so the UUID check does not apply. Do not read "0" as "clean".
- **Secrets cluster where flows call external services,** and more often on test instances. Rotate;
  do not just delete (see `SKILL.md`).
- **`no-catch` is the commonest gap** and is concentrated at sites that built flows from a
  template without the error group.

## 2. More symptom rows

Each row names the layer and the evidence. "Inference" means the cause is read from the
export, not observed on an instance.

| Symptom | Likely cause | Check | Evidence |
|---|---|---|---|
| Machine silent on an `.../ads/...` topic | The machine may not be integrated yet. The connector's machine list carries an integration status per machine (watch for blank or inconsistent status values) | Machine List integration status before opening the flow | Connector note |
| Counter jumps to zero at an odd hour | Shift reset is a cron `inject`; the shift boundaries differ per plant and the instance timezone is not recorded in any flow | Compare the inject's cron with the plant shift plan **and** the instance clock | Export review |
| Shift state differs between two flows on one instance | On some instances shift state is held in **global** context, so any flow can overwrite it | Search the instance for other writers of the same global key | Export review; inference |
| Value read as `undefined` though the other flow writes it | Context keys are case-sensitive and spelling variants exist between flows (`PartNumber` vs `Partnumber`, `MachineState` vs `_machine_state`) | Compare the exact spelling at the writer and the reader | Export review |
| Signal keyed by a raw PLC-style name (an address-like key such as `_part0_io`) | Data point named after an address, not a concept | `od-signal-standardization`, `raw-plc-tag` | Export review |
| Notification never arrives | A webhook `http request` node fails on the HTTP side; with no `catch` nothing reports it | Does the flow have a `catch`? Does the node status show an HTTP error? | Export review; inference |
| `http request` goes to the wrong place | Many `http request` nodes carry no URL in the export - it is set at run time from `msg.url` | Debug `msg.url` before the node | Export review |
| Flow is correct but nothing to analyse in subflow | The per-flow export does not contain subflow bodies | Open the subflow on the instance | Export review |
| Analyser says "0 blockers" on an OPC UA or InfluxDB flow | The sysTime/oneof checks are written for PLCPacket flows; these flows have another shape | Read the flow by hand: endpoint, security, node status | Export review; inference |
| Copy of a flow works at no other site | The copy kept the source site's `datatronName`/UUIDs | Re-fill the config contract (`assets/flow-config-contract.md`) | Export review |
| Several tabs titled `Flow 1` | The default tab title was never changed; the generated page cannot be found by name | Rename to `<asset> - <artefact>` | Export review |

## 3. Three illustrative worked findings

Illustrative shapes, run with `python3 scripts/analyze_flow.py <file>`. Names are placeholders;
no real flow or identifier is reproduced.

**A. Silent timestamp corruption - `<asset> - <artefact>` (`<site>-nodered-prod`).** Findings:
`systime-not-unpacked` and `systime-not-repacked`, both BLOCKER. Reading: the flow decodes a
`PLCPacketList` and encodes a packet and touches neither end of `sysTime`. Nothing errors;
downstream timestamps are wrong. Fix: add the unpack function after the decode and the pack
function before the encode (the two standard functions in the build part of this skill,
`standard-functions.js`). Flows copied from one another carry the same pair of findings, so check
the neighbours before fixing one.

**B. oneof violation - `<calculator> - <asset>` (`<site>-nodered-test`).** Findings: BLOCKER
`oneof-violation` ("valueDouble, valueInteger" both left set) and WARN `unset-context-read`
(a `datapoint...` key read but never written in this flow). Reading: the output packet carries two
value fields, so it encodes to something unintended; the context read returns `undefined` on this
tab. Fix: run the `prepare for protob encoding` change node that deletes the unused fields
(pattern P9); write the key in the config group or move the reader to the tab that writes it.
Note that this tab sits on a test instance.

**C. Pipeline severed - `<asset> - <artefact>` (`<site>-nodered-prod`).** Findings: three
`spine-severed` WARNs - the decode, an unnamed `mqtt out` and the encode have no inbound wire.
Reading: the flow moves no data ("publishes nothing"). First confirm the tab is enabled, then
re-wire mqtt in -> decode -> filter -> split -> ... -> encode -> mqtt out. Unnamed or generically
named nodes are also why an error from this tab would not name its source.

## 4. What the analyser still cannot see

- Whether the tab is deployed and the broker connected: the export is configuration only.
- UUID correctness: a wrong UUID looks like a correct one. Check against the live topic.
- Anything inside a subflow, any config node, and global context contents.
- The meaning of a threshold: `hardcoded-threshold` finds the literal, not whether it is right.
