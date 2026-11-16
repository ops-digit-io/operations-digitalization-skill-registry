---
type: Skill Reference
title: Background
description: Context, rationale, examples and notes that stood in SKILL.md, moved here unchanged. Open it for the why; it is never an instruction.
resource: ../SKILL.md
status: draft
tags: [background]
---
# Background

## Example

Fictional example (all values invented for illustration):

If it fails: a route marked TODO, stub or absent is invalid as a standard system; the record says "no standard system" and hands to `invest-screen` and Lane 3.

## Outputs and hand-off: the text before outputs.yaml

`catalog-systems` delivers a system match record for a catalogued use case on a machine that is not connected yet: a standardized system, or a plain statement that no standard system exists. It recommends only; ordering, connecting and spend approval stay human.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| System match record | `assets/standard-system-entry.md`, filled | `dept-decision-rights` (cost template), `mi-equipment` (order and connect) | Every field set or marked missing: request and plant, machine class, route and status with its source, candidate kit or "no standard system", cost-template inputs, Cyber Security status, next step |
| Cost-template inputs | Section of the system match record | `dept-decision-rights`, approved by the plant budget owner | Inputs given or marked missing; no kit price or lead time quoted unless it is in the kit list |
| "No standard system" statement | Section of the system match record | `invest-screen`, then Lane 3 (3b) | Route is TODO, stub or absent in the validated routes; the record says so and names Lane 3 as the next step |

## Handoff

- **Receives from:** `catalog-usecase` (the match record, branch 1b only), plus the machine facts (controller vendor and model, protocol, program version, where the data should land).
- **Next in the flow:** step 1b2 `dept-decision-rights` (cost template and approval), step 1b3 `mi-equipment` (order and connect), step 1b4 `ops-analytics-asset` (apply template and go live); acceptance by `deploy-acceptance`. With no standard system: `invest-screen` and Lane 3 (3b).
- **Stops here when:** the route is not written in full, the tool boundary is not met, or the tool has no named operations owner and support level. A security-relevant connection also goes to `deploy-cybersec`, and Cyber Security sign-off stays human. Do not offer a non-standard system.

## Open questions

- No validated route is known to rest on a real kit list (kit contents, price, lead time). Until the OD lead confirms one, every route is a route candidate and the match record says "kit not yet defined". Supplier: OD lead.
- An earlier version of SKILL.md cited a file `decision-paths.md` that this skill does not ship; route status is now read from `references/validated-routes.md`. Where the original route guide lives is unconfirmed.

## Sources used in the improvement run

- None added; no vault or archive claim was introduced in this run.
