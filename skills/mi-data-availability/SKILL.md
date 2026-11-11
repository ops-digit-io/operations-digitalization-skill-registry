---
name: mi-data-availability
description: >-
  Check whether the data a use case needs exists, is reachable and fit for use before anything is promised; name the step it fails at. Not for designing a signal standard (mi-signals).
license: MIT
allowed-tools: Read Grep Glob Bash(python3 scripts/check_availability.py:*)
metadata:
  id: mi-data-availability
  aliases: [od-data-availability-check]   # former name (naming convention, 2026-11-11)
  tier: practice
  lane: lane-2
  new_state_lane: "Lane 2 (22)"
  new_state_step: "Requirements, features and data check"
  owner_role: Digital-Business-Value-Engineer (DBVE), with IIAE for the integration side
  tags: [analytical-support-service, practice, use-case-support-service]
  authority_level: read-only
  status: stable
  requires: [dept-context]
  composes: [mi-equipment, mi-signals]
  okf:
    type: Agent Skill
    title: Data availability check
    tags: [analytical-support-service, practice, use-case-support-service]
---

# Data availability check

Read `dept-context` first. This is step 2 of the Analytical lane and a precondition of any
use-case scope. It exists to stop the most expensive mistake in the function: promising an
answer the data cannot support.

**The output is not "available" or "not available".** It is *which of the six steps the
request dies at*, because the shortfalls at steps 2, 4 and 5 look identical from a dashboard
and are three different problems with three different owners and costs between an afternoon
and two quarters.

## Purpose

Finds out which of the six availability steps a data request dies at, before anyone promises an answer the data cannot support. Use it at step 2 of the Analytical lane, before a use-case scope is agreed.
- **Outputs:** [`references/outputs.md`](references/outputs.md) lists what this skill must deliver, to whom, and when each output is complete.

## Inputs and output

- **In:** the request (plant, machine, signals or data needed), the Machine List, the Connector Overview and the flow corpus.
- **Out:** the filled [`assets/data-availability-verdict.md`](assets/data-availability-verdict.md) naming the step where the request stops, and, for a gap, [`assets/data-gap-request.md`](assets/data-gap-request.md).

## Procedure

1. Translate the request into objects, events and time; list missing signals up front.
2. Run the script (section "Run it before you reason about it").
3. Walk the six steps in order (section "Walk the path, in this order"), watching the traps listed after it.
4. Check freshness against the pipeline cadence.
5. Fill the verdict; route a shortfall as described in "What to do with a shortfall".

## The references

| File | Use it for |
|---|---|
| [`references/sources.md`](references/sources.md) | The five sources, what each genuinely answers, which fields and patterns to expect, and where each stops |
| [`references/failure-modes.md`](references/failure-modes.md) | The three indistinguishable shortfalls, plus the two that are not data gaps at all |
| [`references/freshness.md`](references/freshness.md) | Cadence per source, the slowest-input rule, and history depth |
| [`references/plant-instance-map.md`](references/plant-instance-map.md) | Which Node-RED instance is which plant, how each was established, and how to find the plants with no evidence |
| [`references/machine-list-completeness.md`](references/machine-list-completeness.md) | How to measure, live, how complete the Machine List is per plant, and which kinds of plant cannot answer step 2 from the list |
| [`references/data-needs-by-capability.md`](references/data-needs-by-capability.md) | Per capability template: what it covers, the department standard, how to count the recorded use cases that list no machine, and what the capability and process epic shells do and do not say |
| [`references/non-machine-data-sources.md`](references/non-machine-data-sources.md) | Data that is not a PLC signal - how to read the legacy application records, camera, file, lab and energy sources, and which connectors exist for them |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | **How the step runs in the chain**: objects, events and time first, the missing-signal table up front, decision rules, handoff contract, pitfalls, AI agent operating notes |
| [`assets/data-availability-verdict.md`](assets/data-availability-verdict.md) | The defined output to fill in |
| [`assets/data-gap-request.md`](assets/data-gap-request.md) | The named request a data gap becomes when it is routed to the Information Integration lane |
| [`scripts/check_availability.py`](scripts/check_availability.py) | Walks the six steps against the real sources |

## Run it before you reason about it

```bash
python3 scripts/check_availability.py --plant Mako --signals TotalPartCounter,MachineState
python3 scripts/check_availability.py --plant Karben --machine "Lean Cell" --report
```

Exit **2** if a step blocks, **1** if a step is unproven, **0** if all six are answered. It
reads the Machine List, the Connector Overview and the flow corpus from the knowledge-graph
checkout (`--kg`, default `../ops-knowledge-graph`).

The script never guesses. Where a source cannot answer, it says *unproven* rather than
*absent* — and **step 5 comes back unproven every time**, deliberately, because nothing in
the bundle records fitness for use.

## Walk the path, in this order

First translate the request into the **objects** it is about, the **events** that happen to them and the **time** axis; a sensor value is not an event, and a missing relation to the product or order is a data gap, not something to approximate ([`process-chain-practice.md`](references/process-chain-practice.md)). Report anything needed but not collecting **up front** as a missing-signal table (`signal id | label | why needed`).

| # | Question | Where to look | If no |
|---|---|---|---|
| 1 | Does a **machine** produce the signal at this plant? | Machine List — rows with vendor, PLC, protocol, criticality | Not a data gap; a measurement gap. Say so. |
| 2 | Is the machine **integrated**? | Machine List status — `INTEGRATED`, `NOT INTEGRATED`, `ONGOING`, or blank | → `mi-equipment` (assessment route) |
| 3 | Is there a **connector and concept** for it? | Connector Overview — one connector per protocol or vendor family; three integration concepts | Barrier: log it in the landscape module |
| 4 | Is the signal **standardized** and offloaded to the data platform? | The edge offload | → `mi-signals` |
| 5 | Is the data **fit for use** — right granularity, freshness, completeness? | Databricks / the Azure Storage Account | Data gap, with the reason named |
| 6 | Does an **existing asset** already answer this? | Use-case portfolio; the reference library | Do not rebuild it |

The three failures at steps 2, 4 and 5 look identical from a dashboard and are entirely
different problems. Name which one you have →
[`failure-modes.md`](references/failure-modes.md).

## Three traps the sources set

**A blank is not a no.** Machines are `INTEGRATED`, `NOT INTEGRATED` or ongoing — and a
sizeable block carries **no status at all** (count it live). Reading a blank as "not
integrated" fabricates a gap across part of the estate, and the fabricated gap gets routed to
a lane that then finds nothing to do.

**A connector existing is not a connector you may use.** Only connectors that are `Productive`
and marked `USE` count; `NOT AVAILABLE` and `DO NOT USE` do not. An `Idea` connector is a
roadmap item, not a route to data.

**A flow proves presence, never absence.** A signal can be published with nothing consuming
it, so "not in any flow" is a prompt to check the edge platform — not a verdict. And for
plants with no Node-RED instance in the corpus (derive the list as in
[`plant-instance-map.md`](references/plant-instance-map.md)), step 4 cannot be answered from
the bundle at all.

## Two more traps

**Some plants cannot answer step 2 at all.** Some plants have no status on any row, and others
on most rows (find them by counting status per plant on the current export). Say "not
recorded" for those, and see
[`machine-list-completeness.md`](references/machine-list-completeness.md).

**Not every request is a machine request.** Many legacy applications are standalone and many
hold the data a use case wants (laboratory, camera, PLC programs). Use
[`non-machine-data-sources.md`](references/non-machine-data-sources.md) when the data is not a
PLC signal, and [`data-needs-by-capability.md`](references/data-needs-by-capability.md) to see
which agreement (reason catalogue, ideal cycle time, recipient) the capability needs before
the data means anything.

## Freshness expectations

Machine signals arrive **near real-time** at the edge; data platform history lands **per
offload**;
MSB exchange is **event-driven**; the Digitalization Scorecard refreshes **monthly**. An
analysis whose conclusion depends on data being fresher than its pipeline delivers is not
supportable — check the cadence before the query, not after.

## What to do with a shortfall

**Flag the data gap rather than filling it.** That is a standing guardrail of the
Analytical lane. Concretely:

- Route it to the Information Integration lane as a named request — which machines, which
  signals, which plant, which use case is waiting.
- Record it as a **dependency** on the use case record so it stays visible after the
  requester has moved on. `MACHINE INTEGRATION` is already a recorded dependency class on
  savings rows.
- Tell the requester what *can* be answered with what exists, and what cannot. A partial
  answer that is labelled is useful; an unlabelled one is not.

## Human gate and AI-agent notes

- **Agent may:** run the script, read the sources, fill the verdict and draft the data-gap request, label what is unproven.
- **Roles decide:** the Information Integration lane accepts or rejects a routed request; the plant key user confirms what a machine really produces; the requester's lead decides whether a partial answer is enough. The agent promises no turnaround.

## Available Scripts

| Script | Purpose | Arguments |
|---|---|---|
| `scripts/check_availability.py` | Walk the six steps against the Machine List, Connector Overview and flow corpus and say which step blocks. Exit 2 blocked, 1 unproven, 0 answered | `--plant <name>` (required), `--machine <name>`, `--signals <comma list>`, `--kg <path>` (default `../ops-knowledge-graph`), `--report`, `--json`, `-h` |

An agent runs a script with its code or shell tool (`run_script` in tools that expose it) and reads the exit code and output.

## Example

Fictional example; plant, signal and output are made up for illustration.

```text
$ python3 scripts/check_availability.py --plant ExamplePlant --signals PartCounter
step 1 machine produces signal   OK
step 2 machine integrated        BLOCKED (status NOT INTEGRATED)
step 5 fit for use               UNPROVEN (no source records it)
exit 2   -> verdict: dies at step 2; route to mi-equipment
```

If the script cannot read a source, it reports the step as unproven, not absent; check the `--kg` path first.

## Do not

- Do not substitute a proxy signal without saying so in the deliverable.
- Do not read a missing field as a zero. Absence is common in this portfolio and is not a
  value.
- Do not treat the knowledge graph as the check — it is a rebuilt read surface. Check the
  Machine List and the data platform.
- Do not report *unproven* as *absent*. One is a question for the platform; the other is a
  request to another lane, and sending the wrong one wastes both.
- Do not skip step 6. Several existing cycle-time use cases at one plant is a normal result, and
  rebuilding one of them is the failure the whole standardization effort exists to prevent.
- Do not promise a turnaround before step 5 has been answered.

## Definition of done

The verdict names the step where the request stops, with the evidence and the owner; each shortfall is routed or recorded as a dependency on the use case; the requester knows what can and cannot be answered now.
