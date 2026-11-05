---
type: Skill Reference
title: Compatibility tests
description: The tests to run per dimension in which plants differ, what a pass and a fail look like, and which existing skill supplies the evidence.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [information-integration-service, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---

# Compatibility tests

Run a row only when at least one plant in scope differs from the first plant on that dimension
([`plant-differences.md`](plant-differences.md)). The tests restate nothing from the composed skills; they say what to ask
and where the answer comes from. Every test ends in one of: consumable, consumable with mapping, not consumable, unknown.

| # | Dimension | Question | Evidence from | Pass | Fail or mapping |
|---|---|---|---|---|---|
| T1 | Signal name | Does the plant's list contain the standard name, a known variant, or a local-language term for each signal of the standard? | `od-signal-standardization` analyser (`name-collision`, `local-language-name`, `non-canonical-name`, `likely-typo` checks) and its signal catalogue | Standard name present, or alias mapping complete | Mapping needed per variant; collision or mixed-script name is a blocker in that skill |
| T2 | Signal meaning | Does the same name mean the same thing? Where does a cycle start, what counts as a stop? | `od-signal-standardization` machine-context reference (the sequence chart, layout, handbook, HMI) | Boundary and state model written and equal | Different boundary or state model: not comparable; fix is a definition, not a rename |
| T3 | Machine-state model | Does the plant's state set map onto the standard state set without loss? (several names for machine state exist in the estate.) | `od-signal-standardization` public data models (PackML 17 states, OPC UA Machinery states) | Every local state maps to one standard state and back | Lossy mapping: say which states merge and what downtime reporting loses |
| T4 | Unit and type | Do unit, scale and data type match? | Machine documentation; the edge data-point list carries only `uuid` and `label`, nothing else | Unit and type recorded and equal | Unknown unit is *unknown*, not a pass |
| T5 | Ingress route | Is the signal produced the same way on the route this plant uses (IIoT Edge, central OPC UA aggregation, evaluation ongoing)? | `od-equipment-integration` concepts and connectors; `od-data-availability-check` for what the platform actually receives | Same name and timestamp behaviour on each route in use | Route sets the name or the time stamp differently: mapping at the route, not in the standard |
| T6 | Connector | Does a connector exist for this plant's controller and network (Siemens, Rockwell, Beckhoff, Bachmann, B&R, Engel, Mitsubishi, Omron, Schneider...)? | `od-equipment-integration` connectors reference; the Connector Overview list | Connector exists and is in use | No connector: this is `od-barrier-triage` (planned) territory; the standard is not consumable until the signal can be read |
| T7 | Tool version | Does the use case or flow need a tool or version that the plant does not have (MSB 1.0 / 2.0 / 4.0, MDA/PDA 1.0 / 2.0 / 3.0, RuleEngine 2.0)? | Tool Overview list; `od-system-fit-check` tool boundaries | Tool version recorded as available | Tool "ongoing" or not recorded: *unknown* until the IIAE role confirms |
| T8 | Platform and dashboard layer | Is the consumer on the right layer? Local Grafana per plant for line-side dashboards; Databricks to the Azure storage account (Parquet) for cross-plant analysis | `od-context` (global platform, local dashboards); `build-grafana-ops-dashboard` | Local view reads local data; cross-plant view reads the global layer | A cross-plant view built on one plant's Grafana, or a plant Grafana pointed at the global platform: wrong layer |
| T9 | Plant-specific hard-coding | Does the flow, dashboard or query contain a plant, line, machine or topic-root literal that other plants cannot supply? | Read the artefact; `od-node-red-flow-builder` topic conventions | No literal; parameters named | Replace by a parameter or a lookup; a literal in a "standard" is a fail |
| T10 | Cyber Security | Does the connection route need a Cyber Security / OT sign-off at this plant that the first plant had? | `od-cybersec-gate` (planned); the sign-off standard is "to collect" | Sign-off recorded per plant | Not recorded: *unknown*. Never act on an external connection without sign-off (od-context rule 7) |
| T11 | Use-case instance | Is there already an instance of the capability at this plant, and in what state? | Capability Epics note for the plant; `catalog-usecase` | Instance present and compatible | Instance exists with a local variant: record the delta, see `od-use-case-standardization` (deltas against the baseline) |

## How to record a mapping

A mapping is a row, never a code branch inside the standard:

| Plant | Local name / state / unit | Standard name / state / unit | Where the mapping lives | Owner role | Date |
|---|---|---|---|---|---|
| ⟨plant⟩ | ⟨as the plant has it⟩ | ⟨as the standard has it⟩ | ⟨flow, route, view⟩ | ⟨Plant IT / IIAE⟩ | ⟨date⟩ |

The local name remains an alias of the standard name; it is not replaced (`od-signal-standardization`, multilingual tags).

## Worked pattern (illustrative, no plant data claimed)

A standard for the capability *Downtime Reporting* has to define "machine stopped" the same way for plants whose controllers
publish a numeric state code, a Boolean run flag, or an alarm word. T3 forces the mapping onto one state set; T2 forces
the plant to say which stops count as downtime (PackML's acting/wait distinction is the departing point named in
`od-signal-standardization`). T5 asks whether the central OPC UA aggregation route and the IIoT Edge route deliver the
state with the same name. The verdict is per plant and per route, then summarised in the check grid.
