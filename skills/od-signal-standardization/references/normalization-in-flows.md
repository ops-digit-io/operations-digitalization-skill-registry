---
type: Skill Reference
title: Normalization in flows
description: "How a standardization decision becomes running logic: the department's rule-engine patterns that normalize signals (machine mode, status codes, cycle time, scaled values, totals) and the production flows that show each one."
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [signals, normalization, rule-engine, department-package]
derived_from:
  - "Work vault, OD Department Knowledge/OD-instance/30-skills/ops-rule-engine.skill (references/patterns.md, examples/*.json), read 2026-11-10"
generated: { by: claude-code/1, at: 2026-11-10T00:00:00Z }
---
# Normalization in flows

This skill decides **what** a standard signal is (name, meaning, unit, value set). When the machine does not deliver
it in that form, the department derives it as a calculated datapoint with its rule engine. The build is
`od-node-red-flow-builder` ([rule-engine workflow](../../od-node-red-flow-builder/references/rule-engine.md)); this table
says which pattern implements which normalization and where a production example is.

| Normalization | Rule-engine pattern | Production example (in `od-node-red-flow-builder/references/rule-engine-examples/`) |
|---|---|---|
| Several status bits to one **machine mode / state** text (Running, Equipment, Quality, Changeover, Others, Idle; or Automatic, Manual, Diagnostic, Single Step, Fault) | 2 Multi-bit state to status string, checks ordered by priority | `16_m1072_machine_mode_normalization.json`, `12_ac402_machine_status_mapping.json` |
| Vendor **status or alarm code** to the standard text | 3 Code to text lookup (the table pasted as-is) | `19_blm_ast30_status_code_lookup.json` |
| **Tool ID to part number** (production metadata a use case needs) | 3 Lookup | `21_line15_toolid_to_partnumber_lookup.json` |
| **Cycle time** from a running timer (one value per cycle) | 7 Peak / sawtooth capture | `18_m1072_cycle_time_normalization.json` |
| Raw register to **engineering value** (mantissa and exponent, raw / 100, unit conversion) | 8 Scaled / engineering value | - |
| **Total parts** = OK + NOK | 1 Arithmetic combination | `20_pink_total_parts_ok_plus_nok.json` |
| **Downtime** between two events | 6 Duration between events | `22_grazioli_downtime_duration.json` |
| **Part events** and per-shift counts for counting in Grafana | 4 Event trigger, 5 Counter with shift reset | `15_m1072_part_counter_trigger.json`, `14_m1072_shift_part_counter.json`, `23/24_erlas2_*_part_trigger.json` |

## Rules that come from the patterns

- **Priority, not one-hot.** A state mapping orders its checks by priority; exact bit-combination chains fall through to
  "undefined" whenever two bits overlap for one scan. Ask the plant for the priority when faults can overlap, and
  write it into the signal binding sheet.
- **perBatch for combinations, perPacket for events.** A normalized state or ratio is evaluated per batch with publish
  on change; counts, triggers, durations and peaks per packet.
- **Heartbeat only for slow states** (status, leak rate) so panels do not go stale; never for triggers or counters.
- **The output datapoint must exist** in DATATRON with the standard name before the flow publishes; this skill names
  it, the platform registers it, the flow builder wires it.
- **Unknown codes stay visible** (`Unknown code <n>` or nothing published), never mapped to a default state.
