---
name: mi-equipment
description: >-
  Recommend how to connect machines to the platform and draft the assessment behind it. Use when
  a machine will not connect, when someone asks "which connector or route do we use for this
  PLC", "what do we need at the plant to connect these machines", or "what blocks this
  machine", when a plant or wave of machines needs an integration plan, when a machine is to be
  routed to IIoT Edge or dataFEED, or when gates (budget, infrastructure, PLC program, tags,
  Cyber Security) must be cleared before connecting. Drafts assessments, roadmaps and routes;
  a human connects the machine and approves any external connection. Not for acceptance
  (deploy-acceptance), signal standards (mi-signals) or checking data (mi-data-availability).
license: MIT
metadata:
  id: mi-equipment
  aliases: [od-equipment-integration]   # former name (naming convention, 2026-11-11)
  tier: technical
  lane: [lane-1, lane-3]
  new_state_lane: "Lane 1b (1b3), Lane 3b (3b4, 3b5)"
  new_state_step: "Order and connect; Cyber Security sign-off in parallel; Connector design and data pipeline (edge to data platform); Procure and connect; Cyber Security sign-off in parallel; execution supplier-dependent"
  department_names: ["mi-connector", "mi-roadmap", "mi-readiness", "connector-design"]
  owner_role: IIoT Interface & Automation Engineer (IIAE)
  tags: [information-integration-service, technical]
  authority_level: draft on assessments and roadmaps; recommend a route and a configuration; never connect, never approve an external connection
  status: stable
  requires: [dept-context]
  composes: [mi-signals, deploy-acceptance, dept-decision-rights, mi-flow]
  okf:
    type: Agent Skill
    title: Equipment integration — assessment and guidance
    tags: [information-integration-service, technical]
---

# Equipment integration

## Purpose

- Read `dept-context` first.
- Use this skill to decide how machines get connected: per plant or wave (**Mode A**) and per machine (**Mode B**).
- It returns a route, a connector, a sequence position and a record of barriers, never a connection made by an agent.
- Serves process steps **1b3** (order and connect), **3b4** (connector and pipeline), **3b5** (procure and connect).
- Key user: IIoT Interface & Automation Engineer (IIAE), in tandem with Plant ME / Plant IT. AI agent: drafts and recommends only.
- Where the guide's `rules.json` and this skill disagree, `rules.json` wins (the maintained artefact). Detail behind every rule below: `routing-detail`.

### Terms (used one way throughout)

| Term | Meaning |
|---|---|
| Mode A / Mode B | The two entry modes of this skill: assessment of a plant or wave / guidance for one machine |
| Route | The whole path of a machine's data to the platform: variant plus connector (or driver) plus pattern |
| Variant | One of three ways to connect a PLC family: 1 edge device, 2 connector without device, 3 via aggregation server |
| Connector | The software that reaches a PLC family (edge) or the data source driver (aggregation server) |
| Concept | The integration concept for the target system; no concept means escalate to strategy |

## Inputs and output

| Mode | Needs | From | Output (fill as the work happens) |
|---|---|---|---|
| Plant level, before either | Plant row from the records, flags, plant-only questions | Machine List, Tool Overview | [`plant-readiness-brief.md`](assets/plant-readiness-brief.md) |
| **A** | Machine List export for the plant, accepted or planned use cases, roadmap, readiness matrix | `dept-context`, `mi-data-availability` | [`assessment-protocol.md`](assets/assessment-protocol.md): one per plant/wave, machine table, sign-off |
| **B** | A Mode A inventory row for the machine | Mode A | [`guidance-protocol.md`](assets/guidance-protocol.md): one per machine, gates in order, handoff to `deploy-acceptance` |

- Choose: no assessment yet for this plant or wave -> A.
- Assessment done, one machine needs route, connector, configuration -> B.
- B without an A inventory: start at A, do not guess scope.
- [`outputs.yaml`](outputs.yaml) lists required outputs, criteria, checks and sign-offs.

## Procedure - Mode A (assessment)

1. **Inventory** the plant's machines against the Machine List (vendor, PLC model, part number, protocol, criticality, status). Count live; `NOT INTEGRATED` is not a backlog of failures, a blank status is a data gap.
2. **Filter by demand**: only machines an accepted or planned use case needs. No use case, no integration.
3. **Classify the barrier tier** per machine (`barrier-classes`; the practitioner ranking differs from raw integration rates).
4. **Route each machine** through the Mode B gates for concept and connector; log a barrier where no route exists.
5. **Sequence the wave** against roadmap and readiness matrix: strategic plants first, then red capabilities; wave allocation by request order with first-mover capacity.
6. **Size the investment** and take it through integration investment planning (`execute-with-approval`, Tandem with Plant ME / Plant IT).
7. **Start Cyber Security decoupled and in parallel**; track controller patch status and sign-off scope on the wave plan. It blocks only go-live, not planning or build; open patches delayed a wave in practice (`process-chain-practice`).
8. Hand to execution, then `mi-signals`, then `deploy-acceptance`.

- Targets: look up the current integration target and actual in the department KPI and roadmap status (owner: OD lead), state the date, never plan from remembered numbers.

## Procedure - Mode B (guidance, one machine)

1. **Gate 0 - what is installed at this plant?** Decides which patterns exist (`decision-paths`).
2. **Cheap question first: is the machine already on an OPC-UA server?** Yes -> variant 3, bridge `DTQ-OPCUA-Connector`, no PLC program or cabinet work. Largest cost difference in the guide.
3. **Gate 1 - variant** for this PLC family: 1 edge device, 2 connector without device, 3 via aggregation server. A per-machine decision, not vendor or plant policy (comparison table in `routing-detail`).
4. **Gate 2 - connector** (edge) or **data source driver** (aggregation). Check that it exists and is usable first (see Pitfalls).
5. **Walk the pattern**: `softing-datafeed` or `iiot-edge-platform`.
6. **Gate 3 - clear preparation blocks in order**: budget, infrastructure, **PLC program**, tags, cyber security.
7. **Blocked?** Work `fallbacks` before recording it as blocked.
8. **Gate 4 - record**: Machine List, Machine CV (mandatory vs optional tags), Edge Device List, inform MPEE OD. `INTEGRATED` only after `deploy-acceptance` passes.

### Gate check before recording (validation loop)

- [ ] Gates 0 to 4 are written in order with the evidence for each (Machine List row with date, `rules.json` branch, reference file).
- [ ] Every gate that would fail is either cleared, escalated or logged as a barrier; none is skipped.
- [ ] If a box is unchecked, return to that gate and repeat; do not hand over a partial route.

```text
Machine: M-017 (fictional), PLC family from the Machine List row (dated)
Gate 0: edge platform installed   Gate 1: variant 3 (already on an OPC-UA server)
Gate 2: DTQ-OPCUA-Connector, available   Gate 3: PLC program present, cyber security open -> waits for go-live
Handoff: deploy-acceptance; INTEGRATED only after it passes
```

- If a gate would fail or a guide branch is `TODO`, do not compose a route: use the fallbacks or escalate as stated in the decision rules.

## Decision rules

- **No PLC program -> "we CAN NOT connect the PLC!"** Raise at the first conversation; work the seven non-PLC rungs in `fallbacks` section 1 before declaring blocked.
- **Variant 3 needs the IIoT Edge Platform behind the Softing server**; without it nothing reaches the data platform.
- **Variant 2 has no written route** -> IIAE conversation, never a standard option.
- **Both 1 and 3 available at a plant** -> choose per machine; driver gaps decide (Beckhoff: edge connector, no Softing driver; Modbus: Softing driver, unwritten edge branch). Cameras: variant 1 only.
- **No route exists** -> log the barrier in the landscape module and escalate into the roadmap; never a silent omission from the wave.
- **Guide branch is `TODO`** -> say which branch is unwritten; take the other platform's route if written, else escalate to the IIAE. Never compose a procedure.
- **Cyber Security sign-off missing** -> machine waits to go-live; no expedited path. External connection: confirm the gate before scheduling.
- **No operations concept for the target system** (MSB / data platform) -> escalate to strategy as a tool-rollout decision.
- **Approved edge device sizes**: re-confirm with the IIAE before sizing a wave (small/medium may not exist).
- Overlapping ladders: apply the stricter route.

## Lane 3b order and the absorbed procedures

- The department's Lane 3b runs: connector design → data-pipeline design (edge to the data platform) → Cyber Security sign-off → procurement and hardware → integration execution → acceptance test, live on the data platform.
- Cyber Security runs **in parallel** with planning and build and blocks go-live, not the start (owner decision, 2026-11-06; `process-chain-practice`).
- **Integration execution is supplier-dependent and not covered by any OD skill**: the department records it as a gap waiting on a supplier decision (the App-Store-Ops feature request). Record the wait, do not plan around it.

| Absorbed procedure | Open it | Use when |
|---|---|---|
| Wave plan | [`references/od-machine-integration-plan/procedure.md`](references/od-machine-integration-plan/procedure.md) | A wave goes from the machine list to flow design: known types first, route per machine type, readiness, barrier log, workshop preparation |
| Barrier triage | [`references/od-barrier-triage/procedure.md`](references/od-barrier-triage/procedure.md) | A machine will not connect: classify the barrier and route it to the roadmap, strategy or a substitution path |
| Former lane | [`references/od-information-integration-service/procedure.md`](references/od-information-integration-service/procedure.md) | You need the old Information Integration lane's tool fact sheets, roles and support model, finding decks or lane handoffs |

## Handoff

- Mode A -> Mode B per machine in the wave.
- Mode B -> `mi-signals` (tag list, PLC program version, Machine CV), then `deploy-acceptance`; `mi-flow` for the pipeline; `dept-decision-rights` for investment approval.
- Receiver needs: concept, connector, sequence position, logged barriers, Cyber Security status.

## Human gate and AI-agent notes

- **Agent may**: inventory, filter, classify barriers, draft the protocol, recommend route and configuration; cite the Machine List row (dated), the `rules.json` branch, reference file and manual page.
- **Only a human** connects a machine or approves an external connection (`execute-with-approval`, Tandem with Plant ME / Plant IT, Cyber Security / OT sign-off first). Only a human changes a signal or data-model standard (Consultation).
- Never enable **Write Permission** on an aggregation-server data source unless a use case writes to the PLC; read-only is the default.
- Never structure tags to the PLC layout; use the agreed data model (recorded as *CT Base*).
- Never mark `INTEGRATED` before acceptance passes, never claim a readiness dimension "Available" without evidence, never record a machine integrated without a barrier-tier judgement.

## Definition of done

- **A**: inventory and roadmap agreed with Plant ME / Plant IT; each machine in scope carries concept, connector and sequence position; barriers logged; investment planned; Cyber Security gate identified.
- **B**: Machine List, Machine CV and Edge Device List updated; MPEE OD informed; `INTEGRATED` only after `deploy-acceptance`.

## Pitfalls

- **An unavailable native connector is not an unreachable PLC.** Check a connector's status in `connectors` before routing: `Idea`, `NOT AVAILABLE` and `DO NOT USE` are not routes; the standing fallback is `DTQ-OPCUA-Connector` over OPC UA via the aggregation server.
   - Named cases (B&R, Bachmann, Siemens S7) are in `connectors` and `connector-fact-sheets`.
- **OESL guidance errors** (a missing Beckhoff data source, a discontinued gateway protocol) are listed in `decision-paths`. Source of truth is `rules.json`; the fix is there.
- Softing drivers with no OESL route: put to the IIAE. Each PLC family needs its own licence unless Suite Extended; check licensed concurrent configurations.
- Empty Machine List fields (`production_criticality`, `cyber_security_status`, `machine_blockers`, `input_protocol`) are not values.
- The common recorded blockers (data-model standardization, firmware patching, TIA V16->V17, cyber-security vulnerability) are mostly not connectivity problems.

## Outputs

- [`outputs.yaml`](outputs.yaml): required outputs, criteria, checks and sign-offs.
- One run record per call: `python scripts/run_record.py new <skill-id>` (registry root).

## References

| File | Open when |
|---|---|
| [`references/routing-detail.md`](references/routing-detail.md) | You need terminology, the three variants and comparison table, estate status vocabulary, connector traps, OESL errors or live constraints |
| [`references/decision-paths.md`](references/decision-paths.md) | You walk the four gates or look up PLC family -> routes and where a path dead-ends |
| [`references/barrier-classes.md`](references/barrier-classes.md) | You classify a machine's barrier tier or ask the Modbus/aggregation question |
| [`references/connectors.md`](references/connectors.md) | You check what a connector reaches and whether it is available |
| [`references/connector-fact-sheets.md`](references/connector-fact-sheets.md) | You need signal limits, sampling rates, file and camera endpoints or build estimates |
| [`references/vendor-protocol-routes.md`](references/vendor-protocol-routes.md) | You look up the route for a vendor, PLC model and protocol, or a combination with no route |
| [`references/softing-datafeed.md`](references/softing-datafeed.md) | The route is variant 3: aggregation server pattern, driver list, licensing, per-driver settings |
| [`references/softing-tag-syntax.md`](references/softing-tag-syntax.md) | You write a tag identifier for a PLC family on the aggregation server |
| [`references/softing-data-targets.md`](references/softing-data-targets.md) | You decide how data leaves dataFEED: OPC UA path, Store and Forward, MQTT |
| [`references/iiot-edge-platform.md`](references/iiot-edge-platform.md) | The route is variant 1: edge pattern, six phases, hardware sequence, sizing, non-PLC endpoints |
| [`references/fallbacks.md`](references/fallbacks.md) | Before recording a machine as blocked |
| [`references/plant-integration-status.md`](references/plant-integration-status.md) | You build a plant-by-plant status view from the Machine List and Tool Overview |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | You need the weekly capital-request micro-process, Cyber Security as parallel gate, planning workflow, data classes or lessons |
| [`references/blockers-and-waves.md`](references/blockers-and-waves.md) | You need kinds of recorded blocker, projects and waves, the eCR step or roadmap figures (staging, unverified) |
| [`references/background.md`](references/background.md) | You need context and rationale; never an instruction |

### Absorbed procedures: their supporting files

| File | Open when |
|---|---|
| [`references/od-machine-integration-plan/assets/wave-plan-template.md`](references/od-machine-integration-plan/assets/wave-plan-template.md) | You write one wave plan: machine list and CV fields, route per machine type, cost line, readiness check, barrier log |
| [`references/od-machine-integration-plan/assets/workshop-prep-checklist.md`](references/od-machine-integration-plan/assets/workshop-prep-checklist.md) | You prepare an equipment-integration workshop at a plant, before the visit |
| [`references/od-machine-integration-plan/references/barrier-log-and-cost-of-non-decision.md`](references/od-machine-integration-plan/references/barrier-log-and-cost-of-non-decision.md) | You keep the wave's barrier log or must state the cost of non-decision |
| [`references/od-machine-integration-plan/references/route-choice-per-machine-type.md`](references/od-machine-integration-plan/references/route-choice-per-machine-type.md) | You choose connector and route for a machine type: data classes, edge device need, camera and legacy cases |
| [`references/od-machine-integration-plan/references/wave-planning-and-readiness.md`](references/od-machine-integration-plan/references/wave-planning-and-readiness.md) | You allocate a wave or judge readiness: scale-known-types rule, status taxonomy, phase sequence |
| [`references/od-barrier-triage/assets/barrier-triage-record.md`](references/od-barrier-triage/assets/barrier-triage-record.md) | You record one blocked machine: facts, demand, root-cause class, tier, exit, owner, wait state |
| [`references/od-barrier-triage/references/classes-and-routes.md`](references/od-barrier-triage/references/classes-and-routes.md) | You need the seven root-cause classes of a machine that will not connect and the exit for each |
| [`references/od-barrier-triage/references/estate-patterns.md`](references/od-barrier-triage/references/estate-patterns.md) | You read the Machine List for barrier patterns by vendor, protocol and plant |
| [`references/od-barrier-triage/references/process-chain-practice.md`](references/od-barrier-triage/references/process-chain-practice.md) | You map recurring blocker patterns to barrier classes or write a blocker one-pager |
| [`references/od-information-integration-service/assets/plant-status-input.md`](references/od-information-integration-service/assets/plant-status-input.md) | A plant fills the equipment-integration line of a status request |
| [`references/od-information-integration-service/references/finding-decks.md`](references/od-information-integration-service/references/finding-decks.md) | You must find which archive deck holds what for machine integration |
| [`references/od-information-integration-service/references/lane-handoffs.md`](references/od-information-integration-service/references/lane-handoffs.md) | You match a happy-path step to the asset the composed skill now produces |
| [`references/od-information-integration-service/references/process-chain-practice.md`](references/od-information-integration-service/references/process-chain-practice.md) | You need the former lane's wave cadence, community call pack, plant tiering and hand-over to use-case support |
| [`references/od-information-integration-service/references/roles-and-support-model.md`](references/od-information-integration-service/references/roles-and-support-model.md) | You need who does what around the edge and manufacturing suite at a plant |
| [`references/od-information-integration-service/references/task-chain-and-tool-use.md`](references/od-information-integration-service/references/task-chain-and-tool-use.md) | You need the lane's recurring tasks as a trigger chain, the readiness matrix and source-catalogue traps |
| [`references/od-information-integration-service/references/tool-fact-sheets.md`](references/od-information-integration-service/references/tool-fact-sheets.md) | You answer "what is it, where is it, what does it need" for a shop-floor tool in the Tool Overview |
| [`evals/evals.json`](evals/evals.json) | Test cases and trigger queries to run with and without this skill |
| [`references/outputs.md`](references/outputs.md) | The output contract in full (generated from outputs.yaml) |
