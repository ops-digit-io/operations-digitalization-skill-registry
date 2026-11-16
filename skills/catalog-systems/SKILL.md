---
name: catalog-systems
description: >-
  Match a catalogued use case to a standardized system or connection kit that a plant can order itself (Lane 1b): look up the machine's route, test the tool boundary, and write the system match record with kit, cost-template inputs and Cyber Security status. Use when a plant wants a catalogued use case on a machine that is not connected yet, asks "what do we need to order to connect this press", or when a route must be checked as standard or not. If no standardized system exists, the record says so and hands to Lane 3. Recommends only; ordering, spend approval and Cyber Security sign-off stay human. Not for choosing the use case (catalog-usecase), cost approval (bc-cost) or ordering and connecting (mi-equipment).
license: MIT
metadata:
  id: catalog-systems
  tier: practice
  lane: lane-1
  new_state_lane: "Lane 1b (1b1)"
  new_state_step: "Pick the use case and the standard system"
  department_names: ["catalog-systems"]
  owner_role: Digital-Business-Value-Engineer (DBVE); the plant self-serves
  tags: [department-core, lane-1]
  authority_level: draft the match record; recommend only - ordering, connecting and the spend approval stay human
  status: ready
  requires: [dept-context]
  okf:
    type: Agent Skill
    title: Catalog systems
    tags: [department-core, lane-1]
---
# Catalog systems

## Purpose

- Match a catalogued use case to a standardized system that a plant can order itself (Lane 1b, step 1b1).
- Use it when a plant wants a catalogued use case on a machine that is not connected yet.
- Anything non-standard goes to Lane 3, because only a route written in full with a purchasable kit can be self-served.
- Read `dept-context` first.

## Terms used here

- **Standardized system**: until the OD lead says otherwise, a route written down in full **and** a purchasable kit. The `catalog-systems` catalog lists them.
- **Route candidate**: a route written in full and proven in at least two plants, but with no kit, price or lead time on record. It is not yet a standardized system.
- **Kit**: the hardware, software and licences ordered for one route.

## Inputs and output

- Inputs: the match record from `catalog-usecase`, the machine facts (controller vendor and model, protocol, program version, where the data should land), and the validated routes and tool boundaries in `references/`.
- Output: the system match record ([`assets/standard-system-entry.md`](assets/standard-system-entry.md)) with machine class, route and status, candidate kit or "no standard system", cost-template inputs, Cyber Security status and next step.
- The use case comes from `catalog-usecase`; cost and approval follow in `dept-decision-rights` and `bc-cost` (plant budget owner approves); ordering and connecting in `mi-equipment`.
- Branch 1b flow after this skill: cost template and approval, "Order and connect" (`mi-equipment`), then "Apply template and go live".

## Procedure

1. **Take the match record** from `catalog-usecase`. Branch 1b only.
2. **Collect the machine facts**: controller vendor and model, protocol, program version, where the data should land. Add the machine to the machine list first.
3. **Look up the route** in `references/validated-routes.md`. Written in full: candidate standardized system. TODO, stub or absent: **no standardized system**; say so and hand to `invest-screen` and Lane 3 (3b).
4. **Check the route class.** A route that is not class A gets no entry until the procedure is written (class B) or a second route is proven (class C). The route-candidate pattern and entry fields are in `catalog-usecase` `references/sources-and-entry-fields.md`.
5. **Test the tool boundary**: what the tool is, what it is not, the "recommended if" trigger (`references/tool-boundaries-mda-mes-mil-msb-qfpr.md`). A recommendation names the defined use case behind it; without one it is not made.
6. **Screen for a heavy request disguised as a dashboard**: order or recipe execution, labels, batch genealogy and material validation are execution-system territory.
   - Map the asked functions to the shop-floor function list first.
   - Where performance analysis overlaps with MES, choose the lighter solution and name the overlap.
7. **Pick the route by data class** (feeds `mi-equipment`, `mi-signals`): transactional (events, counters, alarms) goes by service bus (OPC UA); time series by MQTT stream; master data: ERP leads and pushes by API, local systems are derived.
   - Edge device versus plain OPC UA client and where logic lives: `catalog-usecase` `references/process-chain-practice.md`, Part B.
8. **Footprint, cost, approval**: look up the footprint in `references/tools-and-footprint.md`; hand the cost-template inputs to `dept-decision-rights`. Ordering and connecting is `mi-equipment`; acceptance is `deploy-acceptance`.
9. **Write the system match record** from the template: request and plant; machine class; route and status; candidate kit or "no standard system"; cost-template inputs given or marked missing; Cyber Security status; next step (1b order and connect, or Lane 3).

### Gates and vocabulary

- Recommendation vocabulary: recommended / recommended if ⟨condition⟩ / not recommended / not available, each with date and source.
- **Operations-concept gate:** a tool without a named operations owner, service and support level is not matched for rollout, because nobody would run it after go-live.
- Security-relevant (connects to central systems, holds operational or customer data, profound effect on manufacturing) goes to `deploy-cybersec`.

### Check before handoff

- [ ] Every field of the record is set or marked missing.
- [ ] The route class is stated with its source (class A confirmed, or "no standardized system").
- [ ] The tool boundary was tested and a defined use case is named behind any recommendation.
- [ ] No kit price or lead time appears unless it is in the kit list.
- [ ] The Cyber Security status is stated and the next step names Lane 1b or Lane 3.

## Examples

```text
Input : request "catalogued use case on a press", controller vendor A, protocol OPC UA (fictional)
Steps : route looked up in the validated-routes list: written in full -> candidate standardized system
Output: system match record: machine class press; route status candidate;
        kit "see kit list" (price and lead time: <missing>); Cyber Security status open;
        next step: 1b order and connect
```

```text
Input : request "andon board on an old press", controller vendor B, proprietary serial protocol (fictional)
Steps : route lookup: TODO in the validated-routes list -> no standardized system
Output: system match record: route status TODO; kit "no standard system";
        cost-template inputs <missing>; next step: invest-screen, then Lane 3 (3b)
```

## Pitfalls

- A heavy request disguised as a dashboard (order execution, labels, batch genealogy) is matched as a dashboard route; it then fails at go-live. Screen it in step 6.
- A TODO or stub route read as a standardized system: there is no kit to order, so the plant waits for nothing.
- A route candidate read as a standardized system: no price, lead time or kit is on record, so the plant cannot budget.
- A kit price or lead time quoted from memory: it is wrong or stale and ends up in the approval. Read it from the kit list or mark it missing.
- A tool recommended without a defined use case behind it: the recommendation cannot be tested.

## Human gate and AI-agent notes

- An agent may draft the system match record and recommend (recommended, recommended if, not recommended, not available).
- Ordering, connecting and the spend approval stay human: the plant budget owner role approves cost, the Cyber Security role signs off a security-relevant connection, and the OD lead role decides what counts as a standardized system.
- An agent never quotes a kit price or lead time that is not in the kit list.

## Do not

- Do not offer a system that is not standardized; route it to Lane 3.
- Do not quote a kit price or lead time from memory; read it from the kit list or mark it ⟨…⟩.
- Do not give a non-class-A route an entry.

## Definition of done

- The system match record is filled (every field set or marked missing), the route status is stated with its source, and the next step (1b order and connect, or Lane 3) is named.
- The check before handoff is ticked.

## Outputs

- [`outputs.yaml`](outputs.yaml): required outputs, criteria, checks and sign-offs.
- [`references/outputs.md`](references/outputs.md): what this skill must deliver, to whom, and when each output is complete.
- One run record per call: `python scripts/run_record.py new <skill-id>` (registry root).

## References

| File | Open when |
|---|---|
| [`assets/standard-system-entry.md`](assets/standard-system-entry.md) | Step 9: writing the record, or adding a route entry |
| [`references/validated-routes.md`](references/validated-routes.md) | Step 3 and 4: deciding whether a route is written in full and proven, and counting evidence live |
| [`references/tool-boundaries-mda-mes-mil-msb-qfpr.md`](references/tool-boundaries-mda-mes-mil-msb-qfpr.md) | Step 5 and 6: what each tool is and is not for, when it is recommended |
| [`references/tools-and-footprint.md`](references/tools-and-footprint.md) | Step 8: the tools of the lean footprint and where each runs |
| [`references/background.md`](references/background.md) | You need the context, rationale or open questions; never an instruction |
| [`evals/evals.json`](evals/evals.json) | Test cases and trigger queries to run with and without this skill |
