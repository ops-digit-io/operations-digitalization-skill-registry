---
type: Skill Reference
title: Outputs
description: The outputs od-signal-standardization must deliver, who receives each one, and what makes each complete.
resource: ../SKILL.md
status: draft
tags: [outputs, handoff]
---
# Outputs

`od-signal-standardization` delivers the analysis and the standardized signal set that let a second plant consume a machine's
signals without asking a question. It recommends standards; only a human enacts a change.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Signal analysis report | `assets/signal-analysis-report.md`, filled | `od-acceptance-test`, `od-cross-plant-compatibility` | How the machine works written down; context sources used and confidence recorded; no analyser blockers; capability requirement set covered; a second plant's instance can consume it |
| Signal binding sheet | `assets/signal-binding-sheet.md`, one row per signal | `od-node-red-flow-builder`, `od-acceptance-test` | Each row carries canonical name, unit, scale, value type, delta meaning, setpoint or actual, consumers and collection method |
| Derived-output spec | Rule-engine spec (pattern, inputs, output name and unit, priority order for states) | `od-node-red-flow-builder` | Each derived signal has a new UUID registered on the edge platform first; raw and derived named explicitly |
| Signals the PLC must expose, machine-specific barriers | List with class and owner | `od-equipment-integration` | Each gap names its owner (machine or engineering vs edge configuration) |
| Proposed standard change | Proposal | IIAE (consultation) | Evidence cited: analyser check id, context source and confidence, standard clause |

## Handoff

- **Also receives from:** `od-use-case-solution-evaluation`: Sequenced gaps with owner.
- **Also receives from:** `od-event-object-modelling`: Data requirements statement.
- **Receives from:** `od-equipment-integration` (the tag list and machine context), `od-data-availability-check` (missing-signal
  table and verdict), `od-requirements-breakdown` (tags of interest and stories).
- **Next in the flow:** `od-node-red-flow-builder` (step 3b4), then `od-acceptance-test` (step 3b6);
  `od-cross-plant-compatibility` receives the report and binding sheet. It also serves step 22 (signal selection) and 1a2.
- **Stops here when:** the analyser reports blockers (raw PLC tag, name collision, mixed script, missing or duplicate UUID,
  capability gap), or only a tag list exists without machine context. Not standardizing is a valid outcome, recorded as a
  decision. Do not fix a gap downstream in a flow or query.
