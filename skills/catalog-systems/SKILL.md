---
name: catalog-systems
description: >-
  Match a catalogued use case to a standardized system or connection kit that a plant can
  order and connect (new-state Lane 1b), and say when no standard system fits so the demand
  moves to Lane 3. Defines what a standardized-system entry must hold and checks a request
  against the integration routes that are actually written down, including the ones that
  are not. Use when a plant wants a catalogued use case on a machine that is not yet
  connected, when someone asks which system to order, or when an entry for the
  standardized-system list is proposed. Draft scaffold: no standardized-system list exists
  in the sources.
license: Internal — OESL MPEE Operations Digitalization. Not for external distribution.
allowed-tools: Read Grep Glob
metadata:
  id: catalog-systems
  tier: practice
  lane: all
  new_state_lane: Lane 1 (1b)
  new_state_step: Pick UC + standardized system
  owner_role: human:jakob.gabriel
  authority_level: recommend - ordering and connecting stay with the integration owner and the approval route
  status: draft
  sources_read: 2026-11-05
  requires: [od-context]
  composes: [catalog-usecase, od-equipment-integration, od-system-fit-check, od-decision-routing, od-acceptance-test]
  derived_from:
    - The new-state flow (docs/new-state-flow.md and the four diagrams in docs/new-state/), the Lane 1b step "Pick UC + std system" and the gap register entry, read 2026-11-05
    - registry.yaml open_gaps, the integration routes marked TODO and the plants without an integration concept
    - ops-knowledge-graph/.../00-core/03-objectives.md
    - ops-knowledge-graph/.../00-core/08-decision-rights.md
    - Skill od-equipment-integration, references/decision-paths.md, the routes by controller and protocol
    - Work vault (Work-OpsDigit-Knowledge), Graph/Machines, the machine notes aggregated by controller vendor, model, protocol, integration status and method, read 2026-11-05
    - Work vault, Graph/Tools, Graph/Connectors and Graph/Legacy Applications (aggregated), read 2026-11-05
    - Work vault, _knowledge/OperationsDigitalization-Department/10-modules/smart-factory-use-case, the systems-of-record note
  okf:
    type: Agent Skill
    title: Standardized-systems catalog
    tags: [all, practice, new-state, draft]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---

# Standardized-systems catalog

Read `od-context` first.

**Status: draft scaffold.** The new-state flow lists a "standardized connection-kit list a plant can
match a use case against and order" as a net-new build. Nothing in the sources read holds such a list,
with kits, prices or lead times. This skill defines how a request is matched and what an entry must
hold. It names no kit.

## Where the flow puts it

Lane 1, branch **1b** (machine not connected): "Pick UC + std system", followed by a cost template and
a lightweight approval (`od-decision-routing`), then "Order and connect" (`od-equipment-integration`),
then "Apply template and go live". If no standard system fits, the demand falls through to **Lane 3**.

## What exists today to build on

| Source | What it gives |
|---|---|
| `od-equipment-integration`, `decision-paths.md` | Integration routes per controller, protocol and platform, with their status |
| Knowledge bundle, objectives | The aim to keep a **lean, standardized system footprint** (measured as the number of systems in operation; the target is still to be confirmed) |
| Knowledge bundle, decision rights | Equipment-integration go-ahead sits with the integration owner and the plant, per investment plan, with **Cyber Security sign-off for an external connection** |
| `registry.yaml`, open gaps | Some routes are marked TODO (for example Beckhoff on edge, Modbus on edge, OPC-UA on the aggregation server); some plants have no integration concept recorded (read the open gaps live) |

## The references

| File | Use it for |
|---|---|
| [`references/validated-routes.md`](references/validated-routes.md) | How to classify a route: written down **and** proven in the Machine List, in four classes (A written and proven, B proven but unwritten, C fallback or single plant, D none), and how to count the evidence live |
| [`references/tools-and-footprint.md`](references/tools-and-footprint.md) | The three integration concepts, the shop-floor tools, how to read rollout and deployment status live, what lean footprint means for a kit |
| [`references/legacy-application-position.md`](references/legacy-application-position.md) | What the kit meets on the floor: how to read licence, support, criticality and cyber-security position of the legacy application list |
| [`assets/standard-system-entry.md`](assets/standard-system-entry.md) | The blank entry, the route-candidate template, and the system match record |

**Pattern from mining the vault:** a route meets the proposed test when it is "written in full and proven in at least two plants" (typically Siemens S7/TIA and Rockwell, on the edge and on the aggregation server; re-derive live). None of them has a kit, price or lead time on record, so they are **route candidates**, not yet standard systems. Routes that are in use at only one or two plants with an unwritten procedure (typically some Beckhoff, Omron, B&R, Bachmann and Modbus routes) are not candidates.

## What a standardized-system entry must hold (proposal)

| Field | Source of the value |
|---|---|
| Machine class: controller vendor and model, protocol | machine record |
| Integration route | `od-equipment-integration`, `decision-paths.md` - only a route that is written down in full counts |
| Kit contents (hardware, software) | ⟨to be supplied⟩ - the only hardware fact on record: for the edge route only the large edge device is approved (`decision-paths.md`) |
| Indicative cost | ⟨to be supplied⟩ - feeds the cost template |
| Lead time (procurement, Cyber Security) | ⟨to be supplied⟩ |
| Cyber Security status | ⟨to be supplied⟩ |
| Validated at | plants where machines are recorded `INTEGRATED` through the route - count live per `references/validated-routes.md` (Machine List, state the export date); ⟨plants where the *kit* runs⟩ to be supplied |
| Known blockers | `od-equipment-integration`, `barrier-classes.md` |

A **standardized system** is, until the OD lead says otherwise, a route that is written down in full **and** a purchasable kit.
A route marked TODO or stub is not a standard system.

## Procedure

1. **Take the catalog match record** from `catalog-usecase`. Branch 1b only.
2. **Collect the machine facts**: controller vendor and model, protocol, where the data should land.
3. **Look up the route** in `decision-paths.md`. Written down in full - candidate standard system. TODO, stub or absent - **no standard system**:
   say so and hand to `od-system-fit-check` and Lane 3 (3b, new connector).
4. **Footprint.** The kit must stay inside the lean footprint (`od-system-fit-check`).
5. **Cost and approval.** Hand the cost template inputs to `od-decision-routing` for the approval route.
6. **Order and connect** is `od-equipment-integration`; acceptance is `od-acceptance-test`. Any external connection needs a
   **Cyber Security sign-off, which is human-only**.
7. **Write the system match record.**

## Output - the system match record

Request and plant; machine class; route and its status; candidate kit or "no standard system"; cost-template inputs
marked as given or ⟨missing⟩; Cyber Security status; next step (1b order and connect, or Lane 3).

## Open - what only the OD lead can supply

- ⟨The list itself⟩: kits, prices, lead times, validated plants, and ⟨who maintains it⟩. The route evidence is now in `references/validated-routes.md`; the kit side is still open.
- ⟨Whether "standardized" means a validated route plus a purchasable kit⟩.
- ⟨The Cyber Security sign-off standard document⟩ - listed in the bundle as still to be collected.

## Do not

- Name a kit, a price or a lead time that no source states.
- Treat a route marked TODO or stub as a standard system. Beckhoff on the edge platform is the standing example.
- Approve a connection or sign off Cyber Security. Both stay human.
- Propose a system outside the lean footprint without `od-system-fit-check`.
