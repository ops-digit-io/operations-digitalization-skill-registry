---
type: Skill Reference
title: Outputs
description: The outputs od-data-availability-check must deliver, who receives each one, and what makes each complete.
resource: ../SKILL.md
status: draft
tags: [outputs, handoff]
---
# Outputs

`od-data-availability-check` delivers a verdict that names the step of the six-step path where a data request stops, not a
plain yes or no, and routes every shortfall instead of filling it.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Data availability verdict | `assets/data-availability-verdict.md`, filled | `od-requirements-breakdown`, `od-prototype-poc`; the requester | Names the step where the request stops, with evidence and owner; unproven is not reported as absent; the requester knows what can and cannot be answered now |
| Data gap request | `assets/data-gap-request.md`, one per gap | `od-equipment-integration` (information integration lane) | Names machines, signals, plant and the use case waiting |
| Dependency on the use case record | Dependency entry on the use case record | DBVE (record owner) | Each shortfall is recorded as a dependency so it stays visible after the requester has moved on |
| Missing-signal table | Table `signal id / label / why needed`, up front in the verdict | `od-requirements-breakdown`, `od-signal-standardization` | Every signal needed but not collecting is listed with its reason |

## Handoff

- **Also receives from:** `od-use-case-solution-evaluation`: Sequenced gaps with owner.
- **Also receives from:** `od-first-aid-kit`: Data check and scenario.
- **Also receives from:** `od-event-object-modelling`: Object relation.
- **Also receives from:** `od-ai-generation-playbook`: Missing-signal and binding table.
- **Also receives from:** `catalog-guardrails`: Routing of failed guardrails.
- **Receives from:** `od-use-case-definition` (the use case and its data points split by source); the request with plant,
  machine and signals; `od-requirements-breakdown` (signals to verify).
- **Next in the flow:** `od-requirements-breakdown` (signal verdicts, step 22), `od-prototype-poc` (step 23),
  `od-equipment-integration` (a step 2 shortfall) or `od-signal-standardization` (a step 4 shortfall).
- **Stops here when:** the verdict shows the request dies at a step. Flag the gap and route it; do not fill it, do not
  substitute a proxy signal without saying so, and do not promise a turnaround before step 5 is answered.
