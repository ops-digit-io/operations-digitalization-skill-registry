---
name: od-use-case-standardization
description: >-
  Make one plant's solution into every plant's — check a use case against the eleven
  cross-plant capability templates and the 100-entry reference library before anything is
  specified, apply the twelve-cluster classification, take a use case through the CSP
  (Common Solution Portfolio) gate, and measure standardization by adoption rather than
  by how many templates exist. Use when a use case is declared standard, when a second
  plant wants something a first plant already has, when a library entry is proposed for
  rollout, when a cluster tag needs assigning or checking, or when someone asks why the
  catalogue has not scaled.
license: Internal — OESL MPEE Operations Digitalization. Not for external distribution.
metadata:
  id: od-use-case-standardization
  tier: practice
  lane: use-case-support-service
  owner_role: Digital-Business-Value-Engineer (DBVE); CSP decision outside OD
  authority_level: recommend
  status: stable
  sources_read: 2026-08-10
  requires: [od-context]
  composes: [od-decision-routing, od-portfolio-and-savings-analysis]
  derived_from:
    - ops-knowledge-graph/_knowledge/10-Department/Use case standardization.md
    - ops-knowledge-graph/_knowledge/20-Done/AI cluster classification.md
    - ops-knowledge-graph/_knowledge/20-Done/Use case portfolio analysis.md
  okf:
    type: Agent Skill
    title: Use-case standardization
    tags: [practice, use-case-support-service]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-08-25T00:00:00Z }
---

# Use-case standardization

Read `od-context` first.

The function's leverage is not building one dashboard well. It is building one dashboard
well and then having the other thirty-two plants **take** it rather than re-specify it.
Three mechanisms exist for that, at different levels.

## 1. The cross-plant template

A use case is never recorded loose. It hangs off a **capability** — eleven of them,
cross-plant: Andon Board, OEE Calculation, Downtime Reporting, Process Quality Data,
Machine Alerts, Cycle Time, Recipe Values, Process Values, Manual Quality Data,
Analytics, Other Use Cases — and off a **process group**, 29 of them inside four material
families. Both templates exist once and are instantiated per plant.

Every capability is instantiated at 32 or 33 of the 33 plants. **The templates are not
aspirational and they are not the constraint** — the whole estate is already mapped onto
them. What varies is how far each instance has got, which is what makes a gap visible as
a gap.

## 2. The reference library and the CSP gate

100 already-built, standardized solutions are kept as their own catalogue, separate from
the plant use cases. A library entry is a solution somebody proved, with its methods and
actions written down — the thing a plant should take instead of starting from a blank
page.

The **CSP (Common Solution Portfolio) decision** is the gate that says an entry is
standard enough to roll out. Applied to 51 of the 100 entries so far: **5 `Yes`,
46 `No`**. That is the honest state — the library exists, the gate exists, and it has
been applied to about half the catalogue.

A `No` is information, not a failure. It says this entry is not yet the thing another
plant should take.

## 3. The cluster tags

All 650 use cases carry exactly one of twelve cluster tags (C01–C12), assigned by a
**deterministic rule-based classifier** over three signals in priority order:

1. the use case's own **category** — an AI category routes straight to the AI cluster;
2. the **capability template** it belongs to;
3. **keyword matching** across its title, notes, blockers and target text.

Deterministic and reproducible: re-running the classifier after a data refresh reproduces
the tags exactly. Do not hand-assign a tag — fix the input fields and re-run.

Each cluster carries a standard **definition**, a standard **KPI set** and a
**requirements checklist** drawn from published references — ISO 22400-2, VDI 3423,
ISA-95, ISO 22005 and the TPS literature. The checklist is the **default requirements
baseline for a use case with no local notes**: a plant then records only its own deltas
— which machines, which line, which local constraint — instead of re-deriving what a good
Andon board is.

**C12 Other and plant-specific is the largest cluster at 168 use cases, and that is a
data-quality number as much as a topical one.** It is the bucket for everything the
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
takes the first plant's solution**. Capability instances are the denominator; delivered
instances are the numerator.

The portfolio analysis is blunt about the finding: *the catalogue is built to standardize
and has not scaled.* Adoption of the proven instance is the constraint. And the regions
are not variations of one another — Europe 312 use cases with 81 productive, the Americas
168 with 70 (the best conversion rate in the estate), Asia 138 with 16. **Asia is a
different problem from Europe, not a smaller one**, and a standardization plan that
treats it as a smaller Europe will not work.

## Do not

- Do not create a new capability or process group to accommodate one plant.
- Do not hand-edit cluster tags.
- Do not treat a `No` at the CSP gate as a rejection of the use case — it is a statement
  about rollout readiness.
- Do not count templates as evidence of standardization.
