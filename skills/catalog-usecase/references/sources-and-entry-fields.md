---
type: Skill Reference
title: Sources and entry fields
description: What the catalog and standard-system match build on today (sources, route-candidate pattern) and the field list a standardized-system entry must hold. Moved out of SKILL.md.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [catalog, new-state]
generated: { by: claude-code/1, at: 2026-11-06T00:00:00Z }
---
# Sources and entry fields

## What exists today to build on - Part A (use-case catalog)

| Source | What it gives |
|---|---|
| `od-use-case-standardization` | The eleven cross-plant capability templates, the reference library, the cluster tags and the CSP gate - run by OD, not by plants |
| Knowledge bundle, `Decision rights` | Standard enough to roll out across plants is the **CSP** decision, recorded per reference-library entry. The bundle states how many entries have been decided so far, split into `Yes` and `No` (check its date and re-count in the vault) |
| Same | A use case has a plant owner, and the plant decides whether it goes into daily use |

At most the entries with a recorded CSP `Yes` are standard enough for another plant to take as they are. To see the
current state, count the library entries in `Graph/Use Cases` by `csp_decision` (`Yes`, `No`, no recorded decision) and name
those with a `Yes` ([`library-and-csp-state.md`](library-and-csp-state.md)). Re-count before quoting.

## What exists today to build on - Part B (standard systems)

| Source | What it gives |
|---|---|
| `od-equipment-integration`, `decision-paths.md` | Integration routes per controller, protocol and platform, with their status |
| Knowledge bundle, objectives | The aim of a lean, standardized system footprint |
| Knowledge bundle, decision rights | Equipment-integration go-ahead sits with the integration owner and the plant, per investment plan, with Cyber Security sign-off for an external connection |
| `registry.yaml`, open gaps | Some routes are marked TODO (for example Beckhoff on edge, Modbus on edge, OPC-UA on the aggregation server); some plants have no integration concept recorded (read the open gaps live) |

**Pattern from mining the vault:** a route meets the proposed test when it is "written in full and proven in at least two plants"
(typically Siemens S7/TIA and Rockwell, on the edge and on the aggregation server; re-derive live). None has a kit, price or lead
time on record, so they are **route candidates**, not yet standard systems. Routes in use at only one or two plants with an unwritten
procedure (typically some Beckhoff, Omron, B&R, Bachmann and Modbus routes) are not candidates.

## What a standardized-system entry must hold (proposal)

| Field | Source of the value |
|---|---|
| Machine class: controller vendor and model, protocol | machine record |
| Integration route | `od-equipment-integration`, `decision-paths.md` - only a route written down in full counts |
| Kit contents (hardware, software) | ⟨to be supplied⟩ - the only hardware fact on record: for the edge route only the large edge device is approved |
| Indicative cost | ⟨to be supplied⟩ - feeds the cost template |
| Lead time (procurement, Cyber Security) | ⟨to be supplied⟩ |
| Cyber Security status | ⟨to be supplied⟩ |
| Validated at | plants where machines are recorded `INTEGRATED` through the route - count live ([`validated-routes.md`](../../catalog-systems/references/validated-routes.md)), state the Machine List export date); ⟨plants where the *kit* runs⟩ to be supplied |
| What it is / what it is **not** | the tool's boundary sentences, so a request can be tested against them |
| Integration recommended if | the trigger condition, tied to a named use case |
| Cost class | free / per-connector / per-plant development - a class, not a number |
| Operations concept | named operations owner, service and support level at the plant - without it no rollout match |
| Known blockers | `od-equipment-integration`, `barrier-classes.md` |

A **standardized system** is, until the OD lead says otherwise, a route written down in full **and** a purchasable kit. A route
marked TODO or stub is not a standard system. Any route that is not class A in `validated-routes.md` gets no entry until the procedure is written (B) or a second route is proven (C).
