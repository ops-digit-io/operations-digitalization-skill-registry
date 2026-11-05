---
name: od-data-availability-check
description: >-
  Check whether the data a use case or an analysis needs actually exists, is reachable and
  is fit for use — before anything is promised. Walks the path from the machine through
  its connector and integration variant to the data platform, distinguishes "not integrated" from
  "not standardized" from "not fit for use", and turns a shortfall into a named data gap
  routed to the Information Integration lane rather than an approximation. Runs the six
  steps against the Machine List, the Connector Overview and the deployed flow corpus, and
  writes a defined verdict naming which step the request dies at. Use at the start of any
  analytical request, before scoping a use case, and whenever an analysis is about to be
  built on data whose provenance has not been checked.
license: Internal — OESL MPEE Operations Digitalization. Not for external distribution.
allowed-tools: Read Grep Glob Bash(python3 scripts/check_availability.py:*)
metadata:
  id: od-data-availability-check
  tier: practice
  lane: [analytical-support-service, use-case-support-service]
  owner_role: Digital-Business-Value-Engineer (DBVE), with IIAE for the integration side
  authority_level: read-only
  status: stable
  sources_read: 2026-11-05
  requires: [od-context]
  composes: [od-equipment-integration, od-signal-standardization]
  derived_from:
    - ops-knowledge-graph/.../20-lanes/analytical-support-service/{playbook,tasks}.md
    - ops-knowledge-graph/_knowledge/10-Department/Machine integration.md
    - ops-knowledge-graph/.../10-modules/smart-factory-use-case/systems-of-record.md
    - Work vault (Work-OpsDigit-Knowledge), Graph/Machines (field completeness per plant), Graph/Legacy Applications, Graph/Capability Epics and Process Epics, Case Groups (member and machine counts) and _knowledge/30-Nodes cluster notes C01 to C12, read 2026-11-05
    - Work vault (Work-OpsDigit-Knowledge), Graph/Connectors and Graph/Tools notes for the non-PLC connectors, MIL, QFPR and Energy Management, read 2026-11-05
    - Work vault (Work-OpsDigit-Knowledge), _knowledge/90-Sources/org-analysis usecase-standardization-knowledgebase (cluster KPIs and requirements checklists), read 2026-11-05
  okf:
    type: Agent Skill
    title: Data availability check
    tags: [analytical-support-service, practice, use-case-support-service]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-08-25T00:00:00Z }
---

# Data availability check

Read `od-context` first. This is step 2 of the Analytical lane and a precondition of any
use-case scope. It exists to stop the most expensive mistake in the function: promising an
answer the data cannot support.

**The output is not "available" or "not available".** It is *which of the six steps the
request dies at*, because the shortfalls at steps 2, 4 and 5 look identical from a dashboard
and are three different problems with three different owners and costs between an afternoon
and two quarters.

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

| # | Question | Where to look | If no |
|---|---|---|---|
| 1 | Does a **machine** produce the signal at this plant? | Machine List — rows with vendor, PLC, protocol, criticality | Not a data gap; a measurement gap. Say so. |
| 2 | Is the machine **integrated**? | Machine List status — `INTEGRATED`, `NOT INTEGRATED`, `ONGOING`, or blank | → `od-equipment-integration` (assessment route) |
| 3 | Is there a **connector and concept** for it? | Connector Overview — one connector per protocol or vendor family; three integration concepts | Barrier: log it in the landscape module |
| 4 | Is the signal **standardized** and offloaded to the data platform? | The edge offload | → `od-signal-standardization` |
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
