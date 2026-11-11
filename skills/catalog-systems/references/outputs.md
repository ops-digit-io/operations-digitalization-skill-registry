---
type: Skill Reference
title: Outputs
description: The outputs catalog-systems must deliver, who receives each one, and what makes each complete.
resource: ../SKILL.md
status: draft
tags: [outputs, handoff]
---
# Outputs

`catalog-systems` delivers a system match record for a catalogued use case on a machine that is not connected yet: a standardized system, or a plain statement that no standard system exists. It recommends only; ordering, connecting and spend approval stay human.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| System match record | `assets/standard-system-entry.md`, filled | `od-decision-routing` (cost template), `od-equipment-integration` (order and connect) | Every field set or marked missing: request and plant, machine class, route and status with its source, candidate kit or "no standard system", cost-template inputs, Cyber Security status, next step |
| Cost-template inputs | Section of the system match record | `od-decision-routing`, approved by the plant budget owner | Inputs given or marked missing; no kit price or lead time quoted unless it is in the kit list |
| "No standard system" statement | Section of the system match record | `od-system-fit-check`, then Lane 3 (3b) | Route is TODO, stub or absent in the validated routes; the record says so and names Lane 3 as the next step |

## Handoff

- **Receives from:** `catalog-usecase` (the match record, branch 1b only), plus the machine facts (controller vendor and model, protocol, program version, where the data should land).
- **Next in the flow:** step 1b2 `od-decision-routing` (cost template and approval), step 1b3 `od-equipment-integration` (order and connect), step 1b4 `od-analytics-asset-build` (apply template and go live); acceptance by `od-acceptance-test`. With no standard system: `od-system-fit-check` and Lane 3 (3b).
- **Stops here when:** the route is not written in full, the tool boundary is not met, or the tool has no named operations owner and support level. A security-relevant connection also goes to `od-cybersec-gate`, and Cyber Security sign-off stays human. Do not offer a non-standard system.
