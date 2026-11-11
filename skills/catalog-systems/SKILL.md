---
name: catalog-systems
description: >-
  Match a catalogued use case to a standard system or connection kit a plant can order itself (Lane 1b); non-standard falls to Lane 3. Not for choosing the use case (catalog-usecase) or cost approval.
license: MIT
metadata:
  id: catalog-systems
  tier: practice
  lane: lane-1
  new_state_lane: "Lane 1b (1b1)"
  new_state_step: "Pick the use case and the standard system"
  department_names: ["catalog-systems"]
  owner_role: Digital-Business-Value-Engineer (DBVE); the plant self-serves
  author: Digital-Business-Value-Engineer (DBVE); the plant self-serves
  tags: [department-core, lane-1]
  authority_level: draft the match record; recommend only - ordering, connecting and the spend approval stay human
  status: draft
  sources_read: 2026-11-10
  requires: [od-context]
  derived_from:
    - "Department knowledge base (skills table, gap), read 2026-11-10"
    - "Split from catalog-usecase (formerly od-catalog), 2026-11-10"
  okf:
    type: Agent Skill
    title: Catalog systems
    tags: [department-core, lane-1]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-11-10T00:00:00Z }
---
# Catalog systems

## Purpose

Match a catalogued use case to a standardized system or connection kit that a plant can order itself (Lane 1b, step 1b1). Use it when a plant wants a catalogued use case on a machine that is not connected yet; anything non-standard goes to Lane 3.

## Inputs and output

Inputs: the Part A match record, the machine facts (controller vendor and model, protocol, program version, where the data should land) and the validated routes and tool boundaries in `references/`. Output: the system match record ([`assets/standard-system-entry.md`](assets/standard-system-entry.md)) with machine class, route and status, candidate kit or "no standard system", cost-template inputs, Cyber Security status and next step.

Read `od-context` first. The department's `catalog-systems`: the catalogue of standardized systems and connection kits a plant can order in Lane 1b. Only standardized systems qualify for 1b; anything non-standard goes to Lane 3. The use case itself comes from `catalog-usecase`; cost and approval follow in `od-investment-input` (plant budget owner approves); ordering and connecting in `od-equipment-integration`.

## Pick a standardized system (step 1b1, hand to 1b2 / 1b3)

Branch 1b only: after the match record, flow continues with cost template and approval (`od-decision-routing`), "Order and connect"
(`od-equipment-integration`), then "Apply template and go live" (Part C).

Sources and the route-candidate pattern (a route "written in full and proven in at least two plants"; none has a kit, price or lead time on record, so they are **route candidates**, not standard systems): [`references/sources-and-entry-fields.md`](../catalog-usecase/references/sources-and-entry-fields.md)).

**Entry fields** (machine class, route, kit, cost, lead time, Cyber Security status, validated at, is / is-not, recommended-if, cost class, operations concept, known blockers): [`references/sources-and-entry-fields.md`](../catalog-usecase/references/sources-and-entry-fields.md)); blank entry in `assets/standard-system-entry.md`.

A **standardized system** is, until the OD lead says otherwise, a route written down in full **and** a purchasable kit. A route
marked TODO or stub is not a standard system. Any route that is not class A in `validated-routes.md` gets no entry until the procedure is written (B) or a second route is proven (C).

## Procedure - system match

1. **Take the match record** from Part A. Branch 1b only.
2. **Collect the machine facts**: controller vendor and model, protocol, program version, where the data should land. Add the machine to the machine list first.
3. **Look up the route** in `decision-paths.md`. Written in full - candidate standard system. TODO, stub or absent - **no standard system**: say so, hand to `od-system-fit-check` and Lane 3 (3b).
4. **Test the tool boundary**: what the tool is, what it is not, the "recommended if" trigger ([`references/tool-boundaries-mda-mes-mil-msb-qfpr.md`](references/tool-boundaries-mda-mes-mil-msb-qfpr.md)). A recommendation names the defined use case behind it; without one it is not made.
5. **Heavy request disguised as a dashboard**: order or recipe execution, labels, batch genealogy, material validation are execution-system territory. Map the asked functions to the shop-floor function list before choosing; where performance analysis overlaps with MES, choose the lighter solution and name the overlap.
6. **Pick the route by data class** (feeds `od-equipment-integration`, `od-signal-standardization`): transactional (events, counters, alarms) - service bus (OPC UA); time series - MQTT stream; master data - ERP leads and pushes by API, local systems are derived. Edge device versus plain OPC UA client and where logic lives: [`references/process-chain-practice.md`](../catalog-usecase/references/process-chain-practice.md)) Part B.
7. **Footprint**, **cost and approval**: hand the cost-template inputs to `od-decision-routing`. **Order and connect** is `od-equipment-integration`; acceptance is `od-acceptance-test`.
8. **Write the system match record** ([`assets/standard-system-entry.md`](assets/standard-system-entry.md)): request and plant; machine class; route and status; candidate kit or "no standard system"; cost-template inputs given or ⟨missing⟩; Cyber Security status; next step (1b order and connect, or Lane 3).

Recommendation vocabulary: recommended / recommended if ⟨condition⟩ / not recommended / not available, each with date and source.
**Operations-concept gate:** a tool without a named operations owner, service and support level is not matched for rollout. Security-relevant (connects to central systems, holds operational or customer data, profound effect on manufacturing) means `od-cybersec-gate`.

---


## References

| File | Use it for |
|---|---|
| [`assets/standard-system-entry.md`](assets/standard-system-entry.md) | What one standardized-system entry must hold |
| [`references/tools-and-footprint.md`](references/tools-and-footprint.md) | The tools of the lean footprint and where each runs |
| [`references/validated-routes.md`](references/validated-routes.md) | Connection routes already proven |
| [`references/tool-boundaries-mda-mes-mil-msb-qfpr.md`](references/tool-boundaries-mda-mes-mil-msb-qfpr.md) | What each tool is and is not for |

## Do not

- Do not offer a system that is not standardized; route it to Lane 3.
- Do not quote a kit price or lead time from memory; read it from the kit list or mark it ⟨…⟩.

## Human gate and AI-agent notes

An agent may draft the system match record and recommend (recommended, recommended if, not recommended, not available). Ordering, connecting and the spend approval stay human: the plant budget owner role approves cost, the Cyber Security role signs off a security-relevant connection, and the OD lead role decides what counts as a standardized system. An agent never quotes a kit price or lead time that is not in the kit list.

## Example

Fictional example (all values invented for illustration):

```text
Input : request "catalogued use case on a press", controller vendor A, protocol OPC UA
Steps : route looked up in the validated-routes list: written in full -> candidate standard system
Output: system match record: machine class press; route status candidate;
        kit "see kit list" (price and lead time: <missing>); Cyber Security status open;
        next step: 1b order and connect
```

If it fails: a route marked TODO, stub or absent is invalid as a standard system; the record says "no standard system" and hands to `od-system-fit-check` and Lane 3.

## Definition of done

The system match record is filled (every field set or marked missing), the route status is stated with its source, and the next step (1b order and connect, or Lane 3) is named.
