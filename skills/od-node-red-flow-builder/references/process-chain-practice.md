---
type: Skill Reference
title: Process chain practice
description: How a flow is built, handed on and repaired inside the new process chain - placement of logic, the flow library classes, streaming against scheduled work, legacy-middleware migration, version control, handoff contracts for build (3b4) and troubleshoot (3b5), ownership signals, pitfalls, and AI agent operating notes. Process guidance only; no figures.
resource: ../SKILL.md
status: draft
tags: [node-red, process-chain, troubleshooting, ai-agent]
---
# Process-chain practice

Derived from the Operations Digitalization slide decks, abstracted into process guidance. Examples are illustrative and use
`<placeholders>`. Own synthesis is marked `PROPOSAL`; unknowns are `<...>`. The decks call the transformation tool the
"rule engine"; in these skills the rule engine is Node-RED (the roadmap's term and the Node-RED instances are the same thing).
The decks hold little troubleshooting detail; the troubleshooting section only adds what they support.

This file has two sections, one per half of the skill: **Build** (step 3b4) and **Troubleshoot** (step 3b5, and 3b6 when
the end-to-end test fails). Merged from `od-node-red-flow-builder`.

---

# Build (step 3b4)

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
| Broken flow | the troubleshoot part of this skill | Export plus symptom |
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
  plant-specific if it depends on a local system, new otherwise; promotion to standard goes through `od-use-case-standardization`.
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
- **Hands over:** the flow, its documentation and test evidence to `od-acceptance-test`; a fault to the troubleshoot part of this skill.

---

# Troubleshoot (step 3b5)

## Where it sits

Step **3b5** (procure and connect the machine), when a connected machine's flow does not deliver, and **3b6** (acceptance), when the
end-to-end test fails. Faults reach it also from step **23** or **26** as "the dashboard is flat".

## Handoff contract

| Receives | From | Must be there |
|---|---|---|
| A symptom in the plant's words ("flat since", "wrong value") | `od-acceptance-test`, the dashboard owner, the key user | When it started, what changed |
| The flow export and the tab description | the build part of this skill | The flow-config contract |
| Whether the machine still publishes | `od-data-availability-check` | Step reached |

| Hands on | To | What it carries |
|---|---|---|
| Fix on a test instance, proposed prod change | the human approver | Analyser result, test evidence |
| A signal or topic problem | `od-signal-standardization` | Raised as a data-model change, not patched |
| A connection or machine problem | `od-equipment-integration`, `od-equipment-integration` | Class, owner |
| An ownership gap | `od-decision-routing` | Named gap |
| Triage record | the plant key user | Cheapest checks first, what was ruled out |

## Method in practice

1. **Walk outward from the machine** (as in the skill), but ask first what changed: a redeploy, a platform migration, a firewall or
   network separation, a new software version, a changed machine program.
2. **Check the cheap platform causes before the flow:** the tab is enabled; configuration is in version control and was not lost on
   a runtime redeploy; the machine still publishes; the connection has an owner.
3. **Wrong value, not no value.** A cycle time that looks too short may be a transactional record that shows only the visible part
   of the cycle (overridden start and stop needed); a number off by a factor may be a missing unit conversion; a mismatched
   identifier may be padding or a wrong stored type; a stale lookup may be an unsynchronized mapping file.
4. **After a platform or server migration** the flow itself is rarely the cause: check DNS, certificates for the new names, user
   access carry-over, the runtime licence of the connector or OPC server (bound to one machine; keep the key), the outage window
   and the per-location checklist item.
5. **Run the analyser, read findings in the skill's order,** then the symptom table.

## Ownership signals

Weeks of unanswered follow-ups, an unclear owner for access to a registry or repository, and nobody asking why other sites work
are signs of **missing ownership**, not a technical puzzle. Ask three questions: who is responsible for the connection; what do
the other sites do that works; what is the alternative if it never works. Escalate the gap through `od-decision-routing`; a
hard external deadline (for example a customer audit) outranks internal plans.

## Pitfalls and lessons

- IT architecture changes during a sprint (firewall separation, access for local users) look like flow faults and cost weeks.
- Cyber Security patching and approvals on controllers hold go-live (the sign-off is a parallel track); a flow fault on a blocked machine is a barrier, not a bug.
- Fixing a data-model problem inside a function hides it from every other plant.
- Treating a quiet dashboard as a flow fault when the machine stopped publishing.

## Questions to ask

- What changed, and when did it last work?
- Is the tab enabled, and is this the deployed version?
- Does the machine publish at all on the topic; does the input uuid appear?
- Wrong value: is a unit, type, padding or mapping step missing?
- Who owns the connection and the access?

## Definition of done

The cause is named in one of: flow, configuration, machine, connector, platform change, ownership; the fix is tested on the test
instance; the triage record is filled; any data-model change is raised, not patched; the plant key user confirmed the asset shows
correct values again.

## AI agent operating notes

- **Can do:** run the analyser over the export; classify the symptom against the table; list recent changes from the ticket thread;
  draft the triage record; detect silent threads and unowned items; propose the cheapest next check.
- **Required inputs:** flow JSON, symptom, last-known-good date, change history.
- **Evidence it must cite:** the analyser check id and node, the symptom row, the thread excerpt.
- **Human gate:** deploying a fix to a production instance; rotating a secret; deciding that a barrier is a roadmap, strategy or
  substitution matter; the escalation wording.
- **Hands over:** the triage record, with fixes only on a test instance, to the approver.
