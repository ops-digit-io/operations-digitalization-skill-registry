---
type: Skill Reference
title: Rule engine patterns
description: "The rule-engine patterns (mapping, normalization, counters, triggers, lookups, durations) and when to pick which."
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [node-red, rule-engine, department-package]
derived_from:
  - "Work vault, OD Department Knowledge/OD-instance/30-skills/ops-rule-engine.skill/references/patterns.md, read 2026-11-10"
generated: { by: claude-code/1, at: 2026-11-10T00:00:00Z }
---
> Transcribed from the department package `ops-rule-engine.skill/references/patterns.md` (the master).

# Pattern catalog

Each pattern gives: when to use, spec settings, the `calc` body for `build_flow.py`, and
the production example it was derived from (`rule-engine-examples/<file>`). Inside `calc` you have:

- `v.<Name>` latest typed value per input (`undefined` until first seen)
- `t.<Name>` its sysTime in unix ms
- `trigger` the packet that caused this evaluation (`trigger.isDelta`, `trigger.uuid`, value fields)
- `triggerName` input name of that packet
- `state` object persisted in flow context (`ruleState`), deleted by the optional cron reset
- `lookup` rows of the optional mapping table (`[{key, value}, ...]`)

Return the output value, or `null`/`undefined` to publish nothing.

## Contents
1. Arithmetic combination (sum, ratio, formula)
2. Multi-bit state -> status string (machine status / mode)
3. Code -> text lookup (alarm/status text, tool id -> part number)
4. Event trigger (OK/NOK part produced, alert occurred)
5. Event counter with shift reset
6. Duration between events (downtime, cycle time from start/end)
7. Peak/sawtooth capture (cycle time from a running timer)
8. Scaled / engineering value (mantissa + exponent, raw/100, unit conversion)

---

## 1. Arithmetic combination
Use: output = f(x, y, z) of current values (total = OK + NOK, OEE ratio, yield %).
Settings: `evaluate: perBatch`, `publishOnChangeOnly: true`.
Example: `20_pink_total_parts_ok_plus_nok.json`.
```js
if (v.OkParts === undefined || v.NokParts === undefined) return null;
return v.OkParts + v.NokParts;
```
Yield: `const total = v.OkParts + v.NokParts; if (total === 0) return null; return Math.round(v.OkParts / total * 10000) / 100;`

## 2. Multi-bit state -> status string
Use: several bool/int DPs describe one state (running, faults, setup, mode bits).
Settings: `evaluate: perBatch`, `publishOnChangeOnly: true`, output `valueString`.
Examples: `12_ac402_machine_status_mapping.json` (Running/Equipment/Quality/Changeover/Others/Idle),
`16_m1072_machine_mode_normalization.json` (Automatic/Manual/Diagnostic/Single Step/Fault).
Order the checks by priority instead of requiring exact one-hot combinations - the legacy
exact-match chains fall through to "undefined" whenever two bits overlap for one scan.
```js
if (v.MachineState === undefined) return null;
if (v.MachineState === 1) return 'Running';
if (v.MachineFault)   return 'Equipment';
if (v.QualityFault)   return 'Quality';
if (v.Setup)          return 'Changeover';
if (v.OtherFault)     return 'Others';
return 'Idle';
```
Ask the user for the priority if faults can overlap.

## 3. Code -> text lookup
Use: integer status/alarm/tool code must become text.
Settings: `lookupTable: {columns:["key","value"], separator:";", rows:"0;IDLE\n1;..."}`,
output `valueString`, `evaluate: perPacket`.
Examples: `19_blm_ast30_status_code_lookup.json`, `21_line15_toolid_to_partnumber_lookup.json`.
```js
const row = lookup.find(r => Number(r.key) === v.StatusCode);
return row ? row.value : 'Unknown code ' + v.StatusCode;   // or null to publish nothing
```
Paste the user's table as-is into `rows`; tab-separated tables use `separator: "\t"`.

## 4. Event trigger
Use: emit `true` each time a source DP changes (counter increments, alarm raised) so
DATATRON/Grafana can count events.
Settings: `evaluate: perPacket`, `publishOnChangeOnly: false` (every event must go out), output `valueBool`.
Examples: `15_m1072_part_counter_trigger.json`, `23/24_erlas2_*_part_trigger.json`,
`17_m1072_alert_counter_trigger.json` (same idea, `valueString: "Alert occured"`).
```js
if (trigger.isDelta !== true) return null;   // ignore snapshots/re-sends
return true;
```
Only rising counter values: `if (triggerName !== 'PartCounter' || !trigger.isDelta) return null; const prev = state.last; state.last = v.PartCounter; return (prev !== undefined && v.PartCounter > prev) ? true : null;`

## 5. Event counter with shift reset
Use: count events per shift/day.
Settings: `evaluate: perPacket`, `publishOnChangeOnly: false`,
`resetCrons: ["00 04 * * *","00 12 * * *","00 20 * * *"]` (shift starts; container time is usually UTC - confirm), output `valueInteger`.
Example: `14_m1072_shift_part_counter.json`.
```js
if (trigger.isDelta !== true) return null;
state.count = (state.count || 0) + 1;
return state.count;
```
Counting a counter DP by difference (robust to missed messages):
`const prev = state.last; state.last = v.TotalCounter; if (prev === undefined || v.TotalCounter < prev) return state.count || 0; state.count = (state.count || 0) + (v.TotalCounter - prev); return state.count;`

## 6. Duration between events
Use: downtime, cycle time from start/end signals, time in a state.
Settings: `evaluate: perPacket`, `publishOnChangeOnly: false`, output `valueDouble` (seconds).
Example: `22_grazioli_downtime_duration.json` (running false -> start, running true -> end).
```js
if (triggerName !== 'MachineRunning' || trigger.isDelta !== true) return null;
if (v.MachineRunning === false) { state.stopMs = t.MachineRunning; return null; }
if (state.stopMs === undefined) return null;
const seconds = (t.MachineRunning - state.stopMs) / 1000;
delete state.stopMs;
return seconds >= 0 ? seconds : null;
```
Two separate DPs (start / end): store `state.startMs = t.CycleStart` when `triggerName === 'CycleStart'`, compute on `CycleEnd`.

## 7. Peak / sawtooth capture
Use: a timer DP counts up during the cycle and resets to 0; the cycle time is the peak.
Settings: `evaluate: perPacket`, `publishOnChangeOnly: false`, output `valueDouble`.
Example: `18_m1072_cycle_time_normalization.json`.
```js
if (trigger.isDelta !== true) return null;
const cur = v.CycleTimer, last = state.peak || 0;
if (cur > last) { state.peak = cur; return null; }
if (cur < last) { state.peak = cur; return last; }   // reset detected -> publish peak
return null;
```

## 8. Scaled / engineering value
Use: value split across DPs (mantissa + exponent), fixed-point integers, unit conversion.
Settings: `evaluate: perBatch` (mandatory when two DPs change together), `publishOnChangeOnly: true`, output `valueDouble`.
Example: `13b_helium09_leakrate_FIXED.json` (broken original: `13_helium09_leakrate_BROKEN.json`).
```js
if (v.LeakBase === undefined || v.LeakIndex === undefined) return null;
return Number(((v.LeakBase / 100) * Math.pow(10, v.LeakIndex)).toExponential(2));
```
Fixed-point: `return v.RawTemp / 10;`  Unit: `return v.PressureMbar / 1000; // bar`

---

## Choosing perBatch vs perPacket

- **perBatch**: output depends on the *combination of current values*. Evaluated once per
  MQTT batch after all packets are stored, so two DPs that change in the same scan are never
  mixed old/new. Use with `publishOnChangeOnly: true`.
- **perPacket**: output depends on *each event* (counting, triggers, durations, peaks). Every
  relevant packet is evaluated, including several in one batch. Usually `publishOnChangeOnly: false`.

## Heartbeat

`heartbeatMinutes: N` resends the last output every N minutes (legacy `intervaltime` trigger).
Use for slowly changing states (status, leak rate) so Grafana panels don't go stale. Don't use
it for triggers/counters - each resend would count as a new event.
