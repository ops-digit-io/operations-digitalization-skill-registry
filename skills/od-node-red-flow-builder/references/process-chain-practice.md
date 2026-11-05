---
type: Skill Reference
title: Process chain practice
description: How a flow is built and handed on inside the new process chain - placement of logic, the flow library classes, streaming against scheduled work, legacy-middleware migration, version control, handoff contract, pitfalls, and AI agent operating notes. Process guidance only; no figures.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [node-red, process-chain, ai-agent]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Process-chain practice

Derived from the Operations Digitalization slide decks, abstracted into process guidance. Examples are illustrative and use
`<placeholders>`. Own synthesis is marked `PROPOSAL`; unknowns are `<...>`. The decks call the transformation tool the
"rule engine"; this registry builds on Node-RED instances `<to confirm that they are the same thing>`.

## Where it sits

Step **3b4** (connector and pipeline to the data platform), last in the sequence machine list, integration plan, tag list,
hardware, software, **flow design to the standard base model**. The same flows serve **22** (transformation jobs behind a use case)
and **26** (a flow becomes a standard flow).

## Handoff contract

| Receives | From | Must be there |
|---|---|---|
| Signal analysis report, binding sheet, derived outputs to register | `od-signal-standardization` | Canonical names, units, collection method |
| Filled flow-config contract | the plant key user | Identity, input and output uuids, limits, shift and timezone, topics |
| Integration plan, program version, route | `od-equipment-integration` | The tag list per machine |
| Tags found not collecting | `od-data-availability-check` | Missing-signal table closed |

| Hands on | To | What it carries |
|---|---|---|
| Flow on a test instance, documentation page, flow-library entry | `od-acceptance-test` | End-to-end proof from machine to the asset |
| Prod import request | the human approver | Analyser result, test evidence |
| Broken flow | `od-node-red-flow-troubleshooting` | Export plus symptom |
| Derived signal | `od-analytics-asset-build` | uuid, name, unit, meaning |

## Method in practice

1. **Place the logic.** Keep in the PLC what controls the process or depends on equipment condition or safety (process values,
   set values, machine mode, safety doors). Put in the flow what needs context from several machines or systems, is a
   single-source-of-truth concept (work-centre or location naming), or is complex logic likely to be iterated (SPC rule alerts,
   statistical functions). The rule engine transforms and standardizes streams; it is **not** a substitute for the service bus
   for dashboards or application connectivity.
2. **Choose streaming or scheduled.** Micro-batching or streaming from the broker serves fresh data immediately (roll-ups,
   statistics on process values, thresholds from configuration). Scheduled or batch jobs serve mapping-file synchronization,
   image uploads and roll-ups. Decide by the freshness requirement and the need to synchronize with an external system; batch
   tooling is heavier and has no graphical development.
3. **Typical transformations** the builder does: edge-to-level conversion (pulse heartbeat to continuous availability), virtual
   identifier creation (a batch opens when automatic mode starts and closes when it stops), counters per context (good and bad per
   batch), topic adaptation, soft logic from raw state to the KPI contract.
4. **Override cycle boundaries where the record is partial.** A transactional record shows only the visible part of a cycle; an
   overridden start and stop in the flow gives the realistic cycle.
5. **Keep flows modular.** The single-file flow structure makes modularization brittle and reuse hard, and a high degree of
   freedom yields unstructured custom flows. The canonical seven-group layout is the counter-measure; flows that may not scale
   should be reviewed against it.
6. **Document in the library.** Flows are recorded in a transformation-flow library with three classes: **new flow**,
   **technical or functional standard flow**, **plant-specific flow**. Not every flow is documented; share new and standard
   flows proactively in the technical community call. An assistant can turn a flow configuration into structured documentation
   (purpose, flow functionality, node functionality).
7. **Request the IT changes early.** Notification channels and data historization are IT changes; asked late, the alert use case
   stalls. Agree architecture and user access before the sprint (firewall separation cost weeks).

## Legacy-middleware migration into the rule engine (decision sequence)

- Consult the plant key users.
- If other software lives on the machine (for example an aggregation server), decide whether it stays.
- If the flows are important, make a per-flow migration plan with the key users and execute with shared responsibility.
- If unknown flows exist, hand over to the business area that owns them.
- Raise a change request to uninstall the middleware and release the virtual machine.
- Update the application list.
- Announce a migration by e-mail with a feedback deadline, then a plant-specific plan.

When a platform changes (server migration), plan an outage window per location for reconfiguring the edge devices and check
runtime licences bound to one machine before moving a virtual machine.

## Decision rules

- `PROPOSAL:` classify a flow as standard if the logic repeats across a process family and a validated prototype exists,
  plant-specific if it depends on a local system, new otherwise; promotion to standard goes through `od-use-case-promotion`.
- No literal secret, no uuid in a function body, no change of the signal standard inside a flow (the skill's guardrails).
- Where the data is a manual entry (lab, quality), the flow is not the right home; use a data model, storage, input interface and
  analytics in one standard, otherwise each plant builds its variant.

## Pitfalls and lessons

- Values stored as the wrong type, padded identifier fields, unit conversions and mapping-file synchronization are the usual tasks
  that go wrong.
- **Redeploying or upgrading the flow-runtime container has lost production flow configuration.** Keep flows in version control
  and check the redeployment impact first.
- A flow built before the signal is standardized fixes the problem downstream and hides it.
- Flow documentation left to the end is not written.

## Questions to ask

- What does the flow read, what does it publish, with which uuid and which meaning?
- Is the logic in the right place (PLC, flow, bus)?
- Streaming or scheduled; what is the freshness requirement?
- Which library class is it; who maintains it; where is it version-controlled?
- Which IT changes (notification, historization, access) are already requested?

## Definition of done

As in the skill (analyser clean, description, flow config, sysTime pair, catch, differing output uuid), plus: library class
stated and entry written; version-control location named; IT changes requested; flow-config contract filed; acceptance test planned.

## AI agent operating notes

- **Can do:** draft a flow on a test instance from the flow-config contract and the signal report; run the analyser; write the
  documentation entry from the flow export; list the IT changes needed; review a flow against the eight review questions.
- **Required inputs:** signal analysis report, flow-config contract, protobuf schema bootstrap present on the instance.
- **Evidence it must cite:** the pattern used, the analyser result, the library class.
- **Human gate:** deploying to a production instance is human-approved; changing a signal standard or a topic is a data-model
  decision for the IIAE; the agent never invents a uuid or rotates a secret without a human.
- **Hands over:** the flow, its documentation and test evidence to `od-acceptance-test`; a fault to `od-node-red-flow-troubleshooting`.
