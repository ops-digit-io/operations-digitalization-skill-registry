---
name: od-node-red-flow-troubleshooting
description: >-
  Diagnose an OESL Node-RED flow that is broken, silent, or producing wrong values —
  starting from its exported flow JSON. Runs a static analyser over the export to find the
  failure modes that actually occur in this estate (unpacked or unre-packed sysTime,
  protobuf oneof violations, hardcoded secrets or thresholds, a severed pipeline, UUIDs
  buried in function bodies, missing error handling, unset flow context), then works a
  symptom-to-cause table for anything the analyser cannot see. Use when a flow publishes
  nothing, publishes the wrong value or a nonsense timestamp, stops after a redeploy, when
  a dashboard has gone flat, or when reviewing a flow before it goes to a prod instance.
license: Internal — OESL MPEE Operations Digitalization. Not for external distribution.
allowed-tools: Read Grep Glob Bash(python3 scripts/analyze_flow.py:*)
metadata:
  id: od-node-red-flow-troubleshooting
  tier: technical
  lane: information-integration-service
  scope: od
  origin: derived
  owner_role: IIoT Interface & Automation Engineer (IIAE)
  authority_level: read and diagnose; fixes on a test instance; prod deploys are human-approved
  status: stable
  sources_read: 2026-11-05
  corpus: validated against 825 flows across 53 ct-oesl instances
  requires: [od-context]
  composes: [od-node-red-flow-builder, od-data-availability-check, od-acceptance-test]
  derived_from:
    - ops-knowledge-graph/_knowledge/node-red-auto-docs/docs/** (825 flow JSON exports)
    - Analyser re-run unchanged over all 825 flow files on 2026-11-05 and the same files re-counted for disabled tabs, drivers and context keys
    - Work vault (Work-OpsDigit-Knowledge), Graph/Connectors, DTQ-Beckhoff-Connector profile block, read 2026-11-05
  okf:
    type: Agent Skill
    title: Node-RED flow troubleshooting
    tags: [information-integration-service, od, technical]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-08-25T00:00:00Z }
---

# Node-RED flow troubleshooting

Read `od-context` first. To **build** a flow, use `od-node-red-flow-builder` — this skill is
for when one already exists and is wrong.

**Start from the flow JSON.** Every flow in the estate is exported as JSON beside its
generated page (`node-red-auto-docs/docs/<instance>/<Flow_Name>.json`), or can be exported
from the editor. The analyser reads that file; you do not need access to the running
instance to find most problems.

## Step 1 — run the analyser

```bash
python3 scripts/analyze_flow.py path/to/Flow.json
python3 scripts/analyze_flow.py docs/ct-oesl-som-nodered-prod/*.json --quiet   # whole instance
python3 scripts/analyze_flow.py Flow.json --json                              # machine-readable
```

No dependencies beyond the standard library. Exit code **2** if any blocker, **1** if any
warning, **0** otherwise — so it drops into CI or a pre-deploy check unchanged.

**Severities.** `BLOCKER` corrupts or loses data · `WARN` degrades it or makes the flow
unmaintainable · `INFO` is hygiene.

Every check exists because the failure it catches is present in the estate. Run over all
825 flows, the analyser finds:

| Check | Severity | Flows |
|---|---|--:|
| `hardcoded-secret` | BLOCKER | 40 |
| `systime-not-unpacked` | BLOCKER | 39 |
| `systime-not-repacked` | BLOCKER | 19 |
| `oneof-violation` | BLOCKER | 18 |
| `systime-unpaired` | BLOCKER | 1 |
| `no-flow-description` | WARN | 813 |
| `no-catch` | WARN | 380 |
| `output-uuid-not-set` | WARN | 203 |
| `no-flow-config` | WARN | 136 |
| `hardcoded-threshold` | WARN | 68 |
| `spine-severed` | WARN | 67 |
| `unset-context-read` | WARN | 99 |
| `mostly-unnamed-nodes` | WARN | 47 |

**119 blocker findings across 98 flows.** These are not hypothetical. `hardcoded-threshold`
is the newest check, added once `od-node-red-flow-builder` named the pattern (P4/P12): a
limit compared directly in a function body instead of read from flow config — real examples
range from a pressure threshold to a day-length constant, and all of them make the flow
untunable without a redeploy.

## Step 2 — read the findings in this order

1. **`hardcoded-secret`** — stop and rotate. The flow repositories are the documentation
   source and are cloned by the doc generator; a literal token in one is a token in every
   clone. Replace with `$env(...)` / `env.get()` or Node-RED credentials.
2. **`systime-*`** — the flow's timestamps are wrong and nothing errors. See
   *Silent corruption* below.
3. **`oneof-violation`** — more than one `measured_value` field survives to the encode.
4. **`spine-severed`** — a decode, split, encode or mqtt out node with no inbound wire. The
   flow moves no data at all; this is usually why "it publishes nothing".
5. **`hardcoded-threshold`** — not data loss, but the flow cannot be tuned or ported without
   editing a function. 68 flows in the corpus carry one; see `od-node-red-flow-builder`'s
   P4/P12 for the pattern it should have been instead.
6. Everything else, in the order printed.

## Step 3 — what the analyser cannot see

It reads a static export. It cannot see the broker, the edge platform, the PLC, or
anything that depends on runtime state. For those, work
[`references/symptoms.md`](references/symptoms.md) — a symptom-to-cause table with the
layer to check at each step.

The single most useful runtime move: **walk the path outward from the machine**, not
inward from the dashboard. Machine → connector → ingress variant → edge → flow → offload →
the asset. Most "the dashboard is broken" reports are a machine that stopped publishing.

## The three silent corruptions

These are the ones that matter, because **nothing errors and the flow looks healthy**.

**1 · sysTime.** `PLCPacket.sys_time` is a packed `uint64` — seconds in the upper four
bytes, nanoseconds in the lower four. Unpack inbound, re-pack outbound. Symptoms:

| What you see | Cause |
|---|---|
| Timestamps in the 23rd century | Read as epoch **milliseconds** without unpacking |
| Timestamps far past any plausible date | Read as epoch **seconds** without unpacking |
| Downstream time is wrong but the flow "works" | Unpacked inbound, **never re-packed** before the encode |

The two conversions are a pair. 19 flows in the estate ship one without the other.

**2 · The protobuf `oneof`.** `measured_value` is a `oneof`: exactly one of
`value_integer` / `value_string` / `value_double` / `value_bool` / `value_bytes` may be
present. The standard `prepare for protob encoding` change node **deletes** the ones that
do not apply. Skip that and the packet encodes and decodes to something unintended.

**3 · Modbus and unit conversion.** Where a flow carries a Modbus-sourced value, there is
no type system underneath it: a holding register is sixteen bits and nothing says it is
tenths of a degree. If the conversion is missing the data flows and is wrong. See
`od-equipment-integration` (guidance route).

## More material (2026-11-05)

| File | Use it for |
|---|---|
| [`references/symptoms-extended.md`](references/symptoms-extended.md) | **Check the tab is enabled first** (72 of 825 tabs are disabled). Where the analyser findings concentrate by site, eleven more symptom rows, three worked findings on real flows |
| [`assets/triage-record.md`](assets/triage-record.md) | The record to fill in while diagnosing: cheapest checks first, analyser result, what the analyser cannot see, decision |

## Fast triage by symptom

| Symptom | Look here first |
|---|---|
| Publishes nothing at all | `spine-severed`; then the broker connection; then whether the input UUID appears on the topic at all |
| Published value is always the same | `rbe` filtering on the wrong property, or `isDelta` gating that never opens |
| Value is right, timestamp is wrong | The sysTime pair |
| Works on test, silent on prod | Different UUIDs in `Set flow config`; different broker; the flow is disabled on prod |
| Stopped after a redeploy | Flow context is cleared on deploy — a counter or accumulator that is never seeded starts at `undefined`, not 0 |
| Counter resets or jumps | `flow.set` accumulator with no reset trigger, or two flows on the same tab writing the same key |
| Dashboard flat since a fixed date | Almost never the flow — check the machine and the connector first |
| Error appears with no node name | An unnamed node: `{{error.source.name}}` resolves to nothing |

## Flow context is per-tab, and it is cleared on deploy

`flow.get` / `flow.set` appear ~14,000 / ~12,700 times across the corpus, so almost every
flow carries state. Two consequences that produce most "it worked yesterday" reports:

- **Scope is the tab.** Two flows on one tab share context. A key written by one and read
  by another works — until somebody moves a flow.
- **Deploy clears it** unless context storage is configured to persist. Any accumulator
  must tolerate `undefined`: the house pattern is `flow.get("ShiftPartProduced") || 0`.

## Guardrails

- **Diagnose on the export; fix on a test instance.** Deploying to a prod instance is
  human-approved.
- **Never "fix" a topic name.** A topic is an interface; renaming it breaks every
  subscriber. Raise it as a data-model change.
- **Never widen a filter to make data appear.** If `filter uuids` drops everything, the
  UUID is wrong or the machine is not publishing — removing the filter hides that.
- **Never delete a `catch`** to quieten a debug pane.
- **Rotate any secret the analyser finds**, do not just remove it from the current version:
  it is in the git history.

## What good looks like

A flow passes when the analyser reports **zero blockers**, the tab carries a description,
`Set flow config` holds every UUID, the sysTime pair is present, a `catch` reports with the
flow name, and the output UUID differs from the input. That is the same bar
`od-node-red-flow-builder` sets for a new flow — this skill just checks it after the fact.
