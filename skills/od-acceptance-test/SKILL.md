---
name: od-acceptance-test
description: >-
  Author and run the acceptance test that closes an equipment integration or a delivered
  solution — define what "passed" means before the build, verify against it, and route a
  failure into the right rework loop rather than around it. Use when an integration is
  complete, a solution is ready, an acceptance protocol needs writing, or a delivery is
  being declared done. Acceptance sign-off is human-only; an agent drafts the protocol
  and reports the result, never approves it.
license: Internal — OESL MPEE Operations Digitalization. Not for external distribution.
metadata:
  id: od-acceptance-test
  tier: practice
  lane: [information-integration-service, project-support-consultancy]
  owner_role: IIoT Interface & Automation Engineer (IIAE)
  authority_level: draft the protocol; report the result; sign-off is human-only
  status: stable
  sources_read: 2026-08-10
  requires: [od-context]
  composes: [od-handover-and-adoption]
  derived_from:
    - ops-knowledge-graph/.../20-lanes/information-integration-service/{playbook,tasks}.md
    - ops-knowledge-graph/.../20-lanes/project-support-consultancy/{playbook,tasks,agent-brief}.md
  okf:
    type: Agent Skill
    title: Acceptance test
    tags: [information-integration-service, practice, project-support-consultancy]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-08-25T00:00:00Z }
---

# Acceptance test

Read `od-context` first.

Acceptance is the gate between "we built it" and "it is yours". It is the control point
on step 5 of both the Information Integration and the Project Support playbooks, and it
is the one an agent may prepare but never pass.

## Write the protocol before the build, not after

An acceptance protocol written after delivery tests what was built. Written before, it
tests what was asked for. It states:

1. **The signals or functions in scope**, named individually.
2. **The expected value or behaviour** for each, with its tolerance.
3. **The data path being verified** — machine → connector → ingress variant → edge →
   offload → data platform → the asset the plant opens. A test that stops at the data
   platform has not tested the use case.
4. **Who witnesses it** — the plant side, by name.
5. **What a failure means** — which rework loop it triggers.

## Which rework loop a failure triggers

| Failure | Loop |
|---|---|
| Integration fails acceptance (Information Integration lane) | Equipment returns for rework; readiness dimension does not turn "Available" |
| Solution fails acceptance (Project Support lane) | Back to step 3, integration project management |
| Use case fails acceptance after handover to integration (Use Case Support lane) | Rework loop back to the integration hand-off |

A failure is recorded, not retried quietly. The **acceptance / rework rate** is a lane
metric precisely so that repeated failures become visible — ⟨the source system for it is
not yet in place; to collect⟩.

## Procedure

1. Draft the protocol from the requirement breakdown and the signal standard.
2. Confirm the plant witness and the date.
3. Run it end to end, along the full data path.
4. Record every result — passed items as well as failures. A protocol with only failures
   recorded cannot be re-run.
5. **A human signs off.** Not the builder alone, and never an agent.
6. On pass → `od-handover-and-adoption`. On failure → the matching rework loop, with the
   finding written down.

## Definition of done

Acceptance test passed, witnessed and signed by a named human on the receiving side; the
result recorded; on the Information Integration side, the readiness dimension moved with
evidence.

## Do not

- Do not sign off acceptance as an agent, under any authority level.
- Do not accept "it works on the edge" as an integration passing — the pipeline into the
  offload to the data platform and the asset on top of it are in scope.
- Do not mark a machine `INTEGRATED` or a readiness dimension green ahead of the pass.
- Do not treat a demonstration as an acceptance test. The plant owner has to have used it
  in a real shift; see `od-handover-and-adoption`.
