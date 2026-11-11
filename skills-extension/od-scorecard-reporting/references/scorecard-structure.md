---
type: Skill Reference
title: Scorecard structure
description: Why the scorecard's metrics are grouped the way they are, and the discipline a new metric must meet before it is added.
resource: ../SKILL.md
status: stable
tags: [all, practice, scorecard]
---
# Scorecard structure

## Why the metrics split this way

The Digitalization Scorecard's metrics are not one flat list by accident — they sit on the
same cause-and-effect chain the Balanced Scorecard method names (Kaplan & Norton, 1992,
*Harvard Business Review*, "The Balanced Scorecard — Measures That Drive Performance"):
capability built now shows up as adoption later, and adoption later shows up as value last.
Reading this registry's own metrics against that chain:

| Perspective | This department's metric | Lags or leads |
|---|---|---|
| **Build capacity** (learning & growth) | Integrated Equipment per month/year | Leading — the earliest signal |
| **Delivery** (internal process) | Integrated Use Cases per month/year | Leading, one step downstream of capacity |
| **Adoption** (customer — the plant is the customer here) | Use-case utilization rate; readiness RAG | Leading on value, lagging on delivery |
| **Value** (financial) | Tracked and proven savings (`od-benefit-calculation`) | Lagging — the last thing to move, and the easiest to overstate early |

**The practical use of this ordering:** when a leading metric (equipment, use cases built)
is on target but a lagging one (utilization, proven savings) is not, the finding is an
adoption or value-realization problem, not a delivery problem — see
`od-handover-and-adoption` and `od-benefit-calculation` before re-litigating the build. The
reverse — a lagging metric look fine while a leading one is red — does not happen in a
healthy portfolio; if it does, the lagging number is stale, not the leading one.

## The discipline a new metric must meet before it joins the table

ISO 22400-2:2014 (*Key performance indicators for manufacturing operations management*)
specifies its KPIs by **formula and corresponding elements, time behaviour, unit/dimension,
and the user group and production methodology it applies to** — not as a bare number with a
name attached. Hold any new scorecard row to the same five fields before it is added:

1. **Formula** — exactly how it is computed, not just what it is called.
2. **Elements** — which recorded fields feed the formula.
3. **Time behaviour** — a point-in-time reading, a rate, or a cumulative total (the
   existing table already separates "year" from "per month" for this reason — a month at
   11 against a 12 target is red even when the year total still looks fine).
4. **Unit/dimension** — count, €, %, days — stated, not implied by the column header.
5. **User group** — who reads it and acts on it (this registry's existing table's "Intervene
   from" column is this field, OD-specific).

A metric that cannot state its formula and elements is not ready for the table — record
honestly that no target exists rather than publishing a number nobody can recompute. Some
rows are legitimately in this state: use-case utilization rate and asset mix carry no fixed
target by design (trend-only, descriptive), and the value-delivery-cycle row is not
captured in any system.

## Equipment work units, specifically

ISO 22400-2 ties its equipment-side KPIs to **work units as defined in IEC 62264** (the
enterprise-control integration standard this registry already uses for the ISA-95
hierarchy in `od-signal-standardization` and `od-use-case-solution-evaluation`). The
Integrated Equipment metrics are this department's instance of a work-unit KPI — keeping
the machine-level granularity (not aggregating to "plant") is what makes the per-month red
bar meaningful at the level where someone can act on it.
