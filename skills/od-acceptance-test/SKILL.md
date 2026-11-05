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
  origin: derived
  sources_read: 2026-11-05
  requires: [od-context]
  composes: [od-handover-and-adoption]
  derived_from:
    - ops-knowledge-graph/.../20-lanes/information-integration-service/{playbook,tasks}.md
    - ops-knowledge-graph/.../20-lanes/project-support-consultancy/{playbook,tasks,agent-brief}.md
    - IEC 62381, Automation systems in the process industry — factory acceptance test (FAT), site acceptance test (SAT), and site integration test (SIT). Standard not opened directly; structure verified via automationforum.co's summary, 2026-10-22.
    - "Standard ISO/IEC/IEEE 29119-1:2022, Software and systems engineering — Software testing — Part 1, Concepts and definitions (test case, pass/fail criteria). Verified via Wikipedia's summary of the standard, 2026-10-22."
    - "BrowserStack, User Acceptance Testing (UAT): Templates and Examples. browserstack.com/guide/user-acceptance-testing-template. Retrieved 2026-10-22."
    - Work vault (Work-OpsDigit-Knowledge), Graph/Machines, Graph/Connectors and Graph/Tools (MIL 1.0, QFPR, RuleEngine 2.0, Energy Management 2.0 archive-evidence blocks), read 2026-11-05
    - Work vault (Work-OpsDigit-Knowledge), _knowledge/30-Nodes cluster notes C01 to C12 and Case Groups (overview and CG-02), read 2026-11-05
    - Department notes Use case lifecycle, Handover and Operating model (ops-knowledge-graph _knowledge 10-Department), read 2026-11-05
    - Work vault (Work-OpsDigit-Knowledge), _knowledge/90-Sources/org-analysis usecase-standardization-knowledgebase (cluster KPIs and requirements checklists, generated 2026-08-24), read 2026-11-05
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
is the one an agent may prepare but never pass. Every kind of work composing into this
gate — a connected machine, a Node-RED flow, a dashboard, an evaluated use case — passes
through the same gate, but not the same test: see `references/test-structure.md`.

## The references are the substance

| File | Use it for |
|---|---|
| [`references/test-structure.md`](references/test-structure.md) | The test-case structure per artefact type — FAT/SAT/SIT for hardware and connectivity, UAT for dashboards and evaluated use cases — and what every type shares |
| [`references/signoff-and-rework.md`](references/signoff-and-rework.md) | Who signs off on each artefact type, what a failure actually means, and which rework loop it routes into |
| [`references/acceptance-by-route.md`](references/acceptance-by-route.md) | What to test per route (edge, aggregation, file or image endpoint, energy tool), each item graded as rule, record pattern or suggested check, and the failure patterns the Machine List and tool notes typically show. Guidance only, no figures |
| [`references/cluster-acceptance-criteria.md`](references/cluster-acceptance-criteria.md) | The department's standard per use case cluster (C01 to C12) restated as UAT items, with the baseline item every acceptance should add |
| [`references/worked-cases.md`](references/worked-cases.md) | Seven illustrative case patterns read from the acceptance side: what the record typically shows, what the protocol would have needed to evidence |

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
metric precisely so that repeated failures become visible — see
`references/signoff-and-rework.md` for why the protocol itself, once enough exist, is the
source system rather than a separate tool waiting to be built.

## Procedure

Copy the items for the route or cluster from [`assets/prefilled-test-items.md`](assets/prefilled-test-items.md)
into §1 to §3 first. Fill [`assets/acceptance-test-protocol.md`](assets/acceptance-test-protocol.md) as the work
happens — one document per artefact, its six sections matching the steps below:

1. Draft the protocol from the requirement breakdown and the signal standard — §1-2,
   **before** the build is tested.
2. Confirm the plant witness and the date.
3. Run it end to end, along the full data path — §3, using the matching table in
   `references/test-structure.md`.
4. Record every result — passed items as well as failures. A protocol with only failures
   recorded cannot be re-run — §3-4.
5. **A human signs off.** Not the builder alone, and never an agent — §5.
6. On pass → fill §6 (handover readiness) and go to `od-handover-and-adoption`, which reads
   it directly. On failure → the matching rework loop from `references/signoff-and-rework.md`,
   with the finding written down in §4.

## Definition of done

Acceptance test passed, witnessed and signed by a named human on the receiving side; every
item's result recorded, passes included; on the Information Integration side, the readiness
dimension moved with evidence; §6 of the protocol filled so `od-handover-and-adoption` can
read the output asset, business process, utilization expectation, data path and named plant
owner straight off it.

## Do not

- Do not sign off acceptance as an agent, under any authority level.
- Do not accept "it works on the edge" as an integration passing — the pipeline into the
  offload to the data platform and the asset on top of it are in scope.
- Do not mark a machine `INTEGRATED` or a readiness dimension green ahead of the pass.
- Do not treat a demonstration as an acceptance test. The plant owner has to have used it
  in a real shift; see `od-handover-and-adoption`.
