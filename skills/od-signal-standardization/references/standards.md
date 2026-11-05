---
type: Skill Reference
title: Standards
description: "ISO 22400-2, VDI 3423, ISA-95 and ISO 22005 - which standard governs which cluster's KPIs, and what it requires of the signals."
resource: ../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [signals, standards, kpi]
generated: { by: claude-code/1, at: 2026-08-25T00:00:00Z }
---
# The normative standards behind a signal set

Signal standardization is not a naming exercise. A signal exists so a KPI can be computed,
and the KPI definitions are **published standards**, not local choices. Building to them is
what makes one plant's number comparable to another's.

**Source.** The department's own standardization knowledge base
(`90-Sources/org-analysis/usecase-standardization-knowledgebase.md`) gives each of the twelve
cluster tags a definition, a standard KPI set and a requirements checklist, drawn from
**ISO 22400-2**, **VDI 3423**, **ISA-95**, **ISO 22005** and the TPS literature. That file is
the authority; this is the signal-side view of it.

---

## Why the standard matters before the signal

A KPI defined loosely produces a number that cannot be compared, and the signals feeding it
will be wrong in ways nobody notices:

- **OEE without a fixed ideal cycle time** is a number that moves when somebody re-tunes an
  assumption. The standard requires the ideal cycle time to be *agreed once and documented*,
  not silently re-tuned.
- **Availability without a micro-stop threshold** counts a 20-second jam differently at every
  plant. The convention is **1–5 minutes**, agreed and documented per line.
- **Quality rate without a defined defect** counts rework differently everywhere.

So: **read the cluster's requirements checklist, then decide which signals you need.** Doing
it the other way round produces a signal set that cannot answer the question.

---

## C01 · Real-time line & OEE — ISO 22400-2, VDI 3423

**OEE = Availability × Performance × Quality.**

| KPI | Needs |
|---|---|
| Availability | Run/stop state over time — `MachineStatus` |
| Performance | Actual vs **ideal** cycle time — `CycleTime`, `StandardSpeed` |
| Quality | Good vs total counts — `TotalPartCounter` plus a defect signal |
| OEE | The product of the three |
| TEEP | OEE × loading rate |

**Requirements that constrain the signal set:**

- Automatic or semi-automatic collection of run/stop, actual vs ideal cycle time, and
  good/defective counts. Manual entry is a valid fallback and degrades accuracy.
- A fixed, documented **ideal cycle time** per product — agreed once.
- A documented **micro-stop threshold** (1–5 min) per line.
- **Publish the three components separately**, not only the blended percentage — an operator
  needs to know which loss to attack.
- **Do not use OEE to rank machines, shifts or plants.** It is a loss-diagnosis tool per
  asset. This is a documented pitfall, and the fastest way to lose the shop floor.

## C02 · Digital Andon, Gemba & escalation — TPS / Jidoka

| KPI | Needs |
|---|---|
| Andon-pull rate | An event signal per pull |
| Time-to-acknowledge, time-to-resolve | Timestamped state transitions per tier |
| % closed with a documented root cause | A verdict field |
| Line-stop minutes from andon events | State duration |

**Two-step signalling is required**: the first signal requests help *without stopping the
line*, the second stops it if unresolved. A single signal that always stops the line is not
an Andon implementation. Defined escalation tiers L1→L2→L3, each with a time-boxed SLA.

**Every event is logged, not only displayed.** The log is what makes the improvement
analysis possible, and a display-only Andon signal cannot be aggregated later.

## C03 · SPC & in-process quality — Shewhart, Western Electric rules

| KPI | Needs |
|---|---|
| Cp, Cpk | A measured value plus specification limits |
| Out-of-limit event rate | `CurrentValue` against `HardUpperLimit` / `HardLowerLimit` |
| Control-chart rule violations | The measured series, not just breaches |
| Scrap / rework rate, first-pass yield | Counts by outcome |

This is why the **quality and limits** family is the best-named in the estate: SPC forces a
model — a value, a spec, a verdict — before anything is built.

**Specification limits are not control limits.** Spec limits come from the product; control
limits from the process. Feeding one where the other is meant produces a chart that is
statistically meaningless while looking correct.

## C05 · Downtime reporting & machine alerts

Needs `MachineStatus` with **timestamped transitions**, plus a reason code. A downtime
duration derived from polling a state at intervals is only as accurate as the interval —
use the transition, not the sample.

## C07 · Recipe, traceability & process parameters — ISO 22005

Needs `RecipeId`, `ToolId`, `Partnumber` and the process values that were **actually in
force** during the run. Traceability is about what the parameters *were*, so a setpoint
alone is not traceability — the measured value has to be recorded too.

## C08 · Energy management — ISO 50001 family

Needs consumption per asset with a time base, and a production reference to normalize
against. Energy per unit produced is the comparable figure; total kWh is not.

---

## The rule this file exists to state

**A signal is standardized when a second plant can consume it without asking a question.**

That requires four things, and a name is only the first:

1. **A canonical name** — [`signal-catalogue.md`](signal-catalogue.md).
2. **A defined meaning**, from the cluster's standard — this file.
3. **A stated unit and scale** — the estate has no written convention, which is a gap.
4. **A stated collection method** — transition or sample, and at what interval.

Two plants publishing `CycleTime` where one measures load-to-load and the other
start-to-start have standardized the name and nothing else. That is the failure this whole
skill is trying to prevent, and it is invisible from the data.

## Where the checklists live

The full twelve-cluster set — definitions, KPI sets, requirements checklists and public
references — is in the department's standardization knowledge base. **Use the checklist as
the default requirements baseline for a use case with no local notes**, then record only the
plant's deltas on top. That is the mechanism by which a use case with no narrative
detail can still be built to a standard.
