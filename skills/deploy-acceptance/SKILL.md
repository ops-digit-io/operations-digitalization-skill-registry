---
name: deploy-acceptance
description: >-
  Author and run the acceptance test that closes an integration or delivered solution; route failures into rework. Sign-off is human-only. Not for building (mi-equipment).
license: MIT
metadata:
  id: deploy-acceptance
  aliases: [od-acceptance-test]   # former name (naming convention, 2026-11-11)
  tier: practice
  lane: lane-3
  new_state_lane: "Lane 3a (3a5), Lane 3b (3b6)"
  new_state_step: "Deploy to the platform, acceptance, Cyber Security sign-off; Acceptance test, live on the data platform"
  owner_role: IIoT Interface & Automation Engineer (IIAE)
  tags: [information-integration-service, practice, project-support-consultancy]
  authority_level: draft the protocol; report the result; sign-off is human-only
  status: stable
  origin: derived
  requires: [dept-context]
  composes: [deploy-handover]
  okf:
    type: Agent Skill
    title: Acceptance test
    tags: [information-integration-service, practice, project-support-consultancy]
---

# Acceptance test

Read `dept-context` first.

Acceptance is the gate between "we built it" and "it is yours". It is the control point
on step 5 of both the Information Integration and the Project Support playbooks, and it
is the one an agent may prepare but never pass. Every kind of work composing into this
gate — a connected machine, a Node-RED flow, a dashboard, an evaluated use case — passes
through the same gate, but not the same test: see `references/test-structure.md`.

## Purpose

Use this skill when an integration or a delivered solution is ready to be declared done. It defines what "passed"
means before the build, checks the result against it, and routes a failure into the right rework loop.
- **Outputs:** [`references/outputs.md`](references/outputs.md) lists what this skill must deliver, to whom, and when each output is complete.

## Inputs and output

- **In:** the requirement breakdown, the signal standard, the artefact to test, the plant witness.
- **Out:** a filled [`assets/acceptance-test-protocol.md`](assets/acceptance-test-protocol.md) with every result recorded,
  a sign-off by a human on the receiving side, and section 6 for `deploy-handover`.

Short example of one protocol item (fictional example; the signal and values are invented):

```text
Item 3   Signal: spindle_temp (fictional)   Path: machine -> connector -> edge -> offload -> data platform -> dashboard
Expected: value within the stated tolerance at the dashboard   Witness: plant ME (role)
Result:   passed | failed   Finding (if failed): written in section 4, rework loop named
```

If an item fails or the data stops short of the asset the plant opens, the acceptance is not valid: record the
finding and follow the rework loop below.

## The references are the substance

| File | Use it for |
|---|---|
| [`references/test-structure.md`](references/test-structure.md) | The test-case structure per artefact type — FAT/SAT/SIT for hardware and connectivity, UAT for dashboards and evaluated use cases — and what every type shares |
| [`references/signoff-and-rework.md`](references/signoff-and-rework.md) | Who signs off on each artefact type, what a failure actually means, and which rework loop it routes into |
| [`references/acceptance-by-route.md`](references/acceptance-by-route.md) | What to test per route (edge, aggregation, file or image endpoint, energy tool), each item graded as rule, record pattern or suggested check, and the failure patterns the Machine List and tool notes typically show. Guidance only, no figures |
| [`references/cluster-acceptance-criteria.md`](references/cluster-acceptance-criteria.md) | The department's standard per use case cluster (C01 to C12) restated as UAT items, with the baseline item every acceptance should add |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | Acceptance as proof of use at 3a5 / 3b6 and at sprint close: reconciliation against the paper process, parallel run and switch-off owner, utilization table, pre-go-live adoption checklist, handoffs, agent notes |
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
6. On pass → fill §6 (handover readiness) and go to `deploy-handover`, which reads
   it directly. On failure → the matching rework loop from `references/signoff-and-rework.md`,
   with the finding written down in §4.

## Human gate and AI-agent notes

- **Agent may:** draft the protocol from the requirement breakdown, prepare the test items, run the checks it has
  access to and report each result, passes included.
- **Only a human decides:** sign-off, by the plant witness or receiving owner (a role, named in the protocol); the
  builder alone is not enough. The agent never passes, signs or marks `INTEGRATED`.

## Definition of done

Acceptance test passed, witnessed and signed by a named human on the receiving side; every
item's result recorded, passes included; on the Information Integration side, the readiness
dimension moved with evidence; §6 of the protocol filled so `deploy-handover` can
read the output asset, business process, utilization expectation, data path and named plant
owner straight off it.

## Do not

- Do not sign off acceptance as an agent, under any authority level.
- Do not accept "it works on the edge" as an integration passing — the pipeline into the
  offload to the data platform and the asset on top of it are in scope.
- Do not mark a machine `INTEGRATED` or a readiness dimension green ahead of the pass.
- Do not pass a dashboard that disagrees with the paper record the plant trusts, or a handover
  whose old process has no named switch-off owner (`references/process-chain-practice.md`).
- Do not treat a demonstration as an acceptance test. The plant owner has to have used it
  in a real shift; see `deploy-handover`.
