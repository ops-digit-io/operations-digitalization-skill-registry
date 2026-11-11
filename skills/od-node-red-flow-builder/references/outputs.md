---
type: Skill Reference
title: Outputs
description: The outputs od-node-red-flow-builder must deliver, who receives each one, and what makes each complete.
resource: ../SKILL.md
status: draft
tags: [outputs, handoff]
---
# Outputs

`od-node-red-flow-builder` delivers a tested Node-RED flow (build, step 3b4) or a named cause with a tested fix
(troubleshoot, step 3b5). A prod import is a request to a human approver, never an agent action.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Importable flow | Flow export built from the filled `assets/flow-config-contract.md`, deployed on a `test` instance | `od-acceptance-test` | Analyser reports zero blockers; `Set flow config` holds every UUID; sysTime unpack and re-pack pair present; a `catch` reports with the flow name; output UUID differs from input |
| Tab description and flow documentation | Tab description, named nodes, config contract in the `config flow` comment node | Plant key user, IIAE | The tab says what it produces, for which machine and which use case |
| Analyser result and test evidence | Output of `scripts/analyze_flow.py` plus the `test` run | Human approver (with the IIAE) | Attached to the prod import request |
| Findings and triage record (troubleshoot) | `assets/triage-record.md`, filled | Plant key user | Cause named as flow, configuration, machine, connector, platform change or ownership; fix tested on `test`; plant key user confirmed the values are correct |
| Flow-library entry | Entry for the flow (new, standard or plant-specific) | OD lead | Filed once the flow passes |

## Handoff

- **Also receives from:** `od-event-object-modelling`: Archetype class, category, method, ETL list.
- **Receives from:** `od-signal-standardization` (signal analysis report, derived outputs to register), `od-equipment-integration` (integration plan and tag list), `od-data-availability-check` (tags not collecting closed), and the plant key user (filled config contract). For troubleshooting, a symptom from `od-acceptance-test`, the dashboard owner or the key user, with the flow export.
- **Next in the flow:** `od-acceptance-test` (step 3b6); a prod import goes to the human approver. Steps in `process.yaml`: 3b4, 3b5 (also 1a2 and 1b4 for calculated datapoints).
- **Stops here when:** the analyser reports any blocker, or the flow has a hardcoded secret (rotate it). A prod import needs the human approver. Never change the signal standard or a topic inside a flow; raise it with `od-signal-standardization`.
