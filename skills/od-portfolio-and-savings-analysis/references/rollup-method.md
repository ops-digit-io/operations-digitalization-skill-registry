---
type: Skill Reference
title: Rollup method
description: How individual savings rows become a portfolio-level number without crossing a boundary that changes what the number means.
resource: ../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [practice, use-case-support-service, analytical-support-service]
generated: { by: claude-code/1, at: 2026-10-22T00:00:00Z }
---
# Rollup method

PMI's *Standard for Portfolio Management* separates **categorization** (group components
that share a common goal and can be measured on the same basis) from **evaluation**
(score within a category) as two distinct steps, precisely because summing across a
category boundary produces a number that means something different from what it looks
like. This skill's one rule — never merge tracked and proven euros — is that principle
applied to one specific boundary; this file states it as a general rollup procedure so the
same mistake does not recur on a different boundary.

## The rule: sum only within one cell, never across a boundary

A rollup is a sum over one **(dimension × reliability-class)** cell, never across cells
that differ in what the number is allowed to claim. The boundaries that matter here, in
the order they must be applied:

1. **Tracked vs. proven** — `od-benefit-calculation`'s own boundary. A tracked total and a
   proven total are two different categories by definition (OD's own assertion vs.
   finance-confirmed through SPRINT); summing them produces a figure that is neither.
2. **Reliability class** — `CALCULATION` (a stated formula), `ESTIMATION` (no formula),
   and **not recorded** (474 of 553 rows). A regional or plant total that silently includes
   `not recorded` rows as if they were zero undercounts without saying so; one that
   silently includes them at face value overstates a figure nobody can check. State the
   split, every time a total crosses this boundary.
3. **Plant / region / capability / cluster** — a legitimate rollup axis, but never collapse
   a cut across it that the regional-handling reference below forbids (Asia and Europe do
   not share a conversion rate).

## Worked example

Twelve rows for one plant: 3 `CALCULATION` tracked (€45,000), 2 `ESTIMATION` tracked
(€12,000), 1 proven via SPRINT (€8,000, already counted inside the tracked total — proven
is a subset, not an addition), 6 not recorded.

**Wrong:** "Plant X: €57,000 in savings." (silently drops the proven/tracked distinction,
and silently drops the six unrecorded rows from view entirely.)

**Right:** "Plant X: €57,000 tracked (€45,000 `CALCULATION`, €12,000 `ESTIMATION`), of
which €8,000 is SPRINT-proven; 6 of 12 rows carry no reliability label and are not
reflected in this figure." Four sentences instead of one, because the one-sentence version
is the one that gets quoted without its qualifiers three forwards later.

## Applying this to a portfolio view

A portfolio rollup table therefore always carries reliability as a row or column, never
collapses it into the total alone, and states the capture date it was read against
(`od-sharepoint-list-export`). See `assets/portfolio-review-protocol.md` for the table
shape this produces.
