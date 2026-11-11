---
name: od-use-case-standardization
description: >-
  Make one plant's solution into every plant's — check a use case against the
  cross-plant capability templates and the reference library before anything is
  specified, apply the cluster classification (C01-C12), take a use case through the CSP
  (Common Solution Portfolio) gate, and measure standardization by adoption rather than
  by how many templates exist. Use when a use case is declared standard, when a second
  plant wants something a first plant already has, when a library entry is proposed for
  rollout, when a cluster tag needs assigning or checking, or when someone asks why the
  catalogue has not scaled.
  Also decides whether a recurring ad-hoc asset becomes a standard use case and assembles the promotion package (formerly od-use-case-promotion).
license: MIT
metadata:
  id: od-use-case-standardization
  tier: practice
  lane: lane-2
  new_state_lane: "Lane 2 (26)"
  new_state_step: "Implement, evaluate impact, ensure adoption, catalogue"
  department_names: ["catalog-synergy"]
  owner_role: Digital-Business-Value-Engineer (DBVE); CSP decision outside OD
  authority_level: recommend
  status: stable
  requires: [od-context]
  composes: [od-decision-routing, od-portfolio-and-savings-analysis, od-benefit-calculation]
  okf:
    type: Agent Skill
    title: Use-case standardization
    tags: [practice, use-case-support-service]
---

# Use-case standardization

Read `od-context` first.

- **Outputs:** [`references/outputs.md`](references/outputs.md) lists what this skill must deliver, to whom, and when each output is complete.

## The references are the substance

| File | Use it for |
|---|---|
| [`references/clusters.md`](references/clusters.md) | All clusters' standard definition, KPI set and requirements checklist — the default baseline for an undocumented use case, each with its source cited and marked verified or carried-over |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | Archetypes (cross-process, per-process, unique), category to method to data-job mapping, prototype to configurable container app, scaling lessons (utilization, not rollout count), handoff contract, agent notes |
| [`references/process-family-patterns.md`](references/process-family-patterns.md) | What a use case looks like per process family (rubber, plastic, metal, assembly, cross-process): process groups, typical capabilities, data needed, standardization potential, traps, blocker themes per capability |

The function's leverage is not building one dashboard well. It is building one dashboard
well and then having the other plants **take** it rather than re-specify it.
Three mechanisms exist for that, at different levels.

## 1. The cross-plant template

A use case is never recorded loose. It hangs off a **capability** — eleven of them,
cross-plant: Andon Board, OEE Calculation, Downtime Reporting, Process Quality Data,
Machine Alerts, Cycle Time, Recipe Values, Process Values, Manual Quality Data,
Analytics, Other Use Cases (check the live capability list before quoting it) — and off a
**process group**, which sits inside a material family (rubber, plastic, metal, assembly).
Both templates exist once and are instantiated per plant.

Every capability is meant to be instantiated at every plant; check the live capability
instance list for which plants are missing one. **The templates are not aspirational and
they are not the constraint** — the estate is mapped onto them. What varies is how far
each instance has got, which is what makes a gap visible as a gap.

## 2. The reference library and the CSP gate

Already-built, standardized solutions are kept as their own catalogue (the reference
library), separate from the plant use cases. A library entry is a solution somebody proved, with its methods and
actions written down — the thing a plant should take instead of starting from a blank
page.

The **CSP (Common Solution Portfolio) decision** is the gate that says an entry is
standard enough to roll out. The decision is recorded per library entry as `Yes`, `No`
or blank (not yet submitted). Count the three outcomes on the live library before
quoting a status: a blank means the gate has not been applied, not that the entry failed.

A `No` is information, not a failure. It says this entry is not yet the thing another
plant should take.

## 3. The cluster tags

Every use case carries exactly one cluster tag (C01–C12), assigned by a
**deterministic rule-based classifier** over three signals in priority order:

1. the use case's own **category** — an AI category routes straight to the AI cluster;
2. the **capability template** it belongs to;
3. **keyword matching** across its title, notes, blockers and target text.

Deterministic and reproducible: re-running the classifier after a data refresh reproduces
the tags exactly. Do not hand-assign a tag — fix the input fields and re-run.

Each cluster carries a standard **definition**, a standard **KPI set** and a
**requirements checklist** drawn from published references — ISO 22400-2, VDI 3423,
ISA-95, ISO 22005 and the TPS literature; the full set is in
[`references/clusters.md`](references/clusters.md). The checklist is the **default
requirements baseline for a use case with no local notes**: a plant then records only its
own deltas — which machines, which line, which local constraint — instead of re-deriving
what a good Andon board is.

**C12 Other and plant-specific tends to be the largest cluster, and its size is a
data-quality number as much as a topical one; count it live and track it over time.** It is the bucket for everything the
classifier could not place, and it should shrink as plant notes get written. A rising C12
means the intake text is getting thinner, not that the portfolio is getting more
idiosyncratic.

## Procedure

1. **Before specifying anything**, search the library for a proven entry against the same
   capability. Take it if it exists.
2. Place the use case on its **capability** and **process group**.
3. Let the classifier assign the **cluster tag**; pull its definition, KPI set and
   requirements checklist as the baseline.
4. Record only the plant's **deltas** against that baseline.
5. If a solution is a candidate to roll out, prepare it for the **CSP decision** —
   methods and actions written down, evidence it works at its first plant.
6. Measure the result by adoption (below), not by the existence of the template.

## How standardization is measured

Not by how many templates exist — all of them do — but by **how often the second plant
takes the first plant's solution**, and then by whether it is **used** there: a deployment count is not a value
measure, and a scaled use case needs utilization (and a saving where one is reported) before it counts as scaled. Capability instances are the denominator; delivered
instances are the numerator. Compute both from the live use case list and quote the read date.

The portfolio analysis is blunt about the finding: *the catalogue is built to standardize
and has not scaled.* Adoption of the proven instance is the constraint. And the regions
are not variations of one another: compare use cases to productive use cases per region on
the live list, and expect the conversion pattern to differ by region. **A region with a
low conversion rate is a different problem from one with a high rate, not a smaller
one**, and a standardization plan that treats one region as a scaled-down copy of another
will not work.

## Output — the protocol

The procedure does not end in prose. Fill
[`assets/standardization-review.md`](assets/standardization-review.md) as the work
happens — one document per use case: template placement, library check, cluster baseline
and delta, and the CSP-readiness verdict, written so it hands off directly into
`od-decision-routing`'s "standard enough to roll out" gate and into
`od-benefit-calculation`'s business case, instead of needing to be re-asked from scratch.

## Absorbed: Promote a recurring ad-hoc asset into a standard use case (formerly od-use-case-promotion)

Run [`references/od-use-case-promotion/procedure.md`](references/od-use-case-promotion/procedure.md) when a dashboard, report or app built for one request keeps being asked for and should become a standard use case. It keeps its own references and assets under that folder and the authority it had.

## Do not

- Do not create a new capability or process group to accommodate one plant.
- Do not hand-edit cluster tags.
- Do not treat a `No` at the CSP gate as a rejection of the use case — it is a statement
  about rollout readiness.
- Do not count templates as evidence of standardization.
