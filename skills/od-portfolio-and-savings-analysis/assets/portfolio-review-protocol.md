---
type: Skill Asset
title: Portfolio review protocol
description: The defined output of a portfolio review - snapshot, rollup, ranking and regional read, built from od-sharepoint-list-export's export and od-benefit-calculation's ledger, so the result is a reusable record rather than prose.
resource: ../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [analytical-support-service, use-case-support-service, template, protocol]
generated: { by: claude-code/1, at: 2026-10-22T00:00:00Z }
---
# Portfolio review — ⟨period, e.g. 2026-Q4⟩

Copy once per review round (monthly / ODEC / ad hoc). Fill as the review happens.

| | |
|---|---|
| **Inputs** | `od-sharepoint-list-export`'s `assets/export-run-log.md` (list(s), capture date, row count, checkpoint) · `od-benefit-calculation` ledger as of ⟨date⟩ |
| **Reviewer / date** | ⟨name⟩ · ⟨date⟩ |
| **Surface read** | ⟨knowledge-graph rebuilt view / SharePoint write surface — state which⟩ |

## 1 · Snapshot

| Delivery status | Count |
|---|--:|
| `IDEA` | ⟨n⟩ |
| `PLANNED` | ⟨n⟩ |
| `IMPLEMENTED` | ⟨n⟩ |
| `PRODUCTIVE` | ⟨n⟩ |
| `STOPPED` | ⟨n⟩ |

Cut further by plant / capability / cluster / asset only where the review question needs
that cut — see `references/rollup-method.md` for which boundaries may and may not be
crossed when totalling.

## 2 · Savings rollup

Per `references/rollup-method.md` — reliability and tracked/proven stay visible, never
collapsed into one total.

| Cut | Tracked (`CALCULATION`) | Tracked (`ESTIMATION`) | Not recorded (rows) | Proven (SPRINT) |
|---|--:|--:|--:|--:|
| ⟨plant/region/capability⟩ | €⟨n⟩ | €⟨n⟩ | ⟨n⟩ rows | €⟨n⟩ |

## 3 · Regional read

Per `references/regional-handling.md` — three rows, never blended.

| Region | Use cases | Productive | Conversion | What is driving it |
|---|--:|--:|---|---|
| Europe | | | | |
| Americas | | | | |
| Asia | | | | |

## 4 · Prioritization

Per `references/prioritization.md`. Rank within category, not across Europe/Asia/Americas.

| Use case | Category | Value signal | Effort signal | Rank | Unscoreable? |
|---|---|---|---|---|---|
| ⟨…⟩ | | | | | |

**Unscoreable bucket** (⟨UNKNOWN⟩ priority/potential — do not rank, do not zero): ⟨n⟩ use
cases, listed separately: ⟨…⟩.

## 5 · Standing findings — check the review against these, every time

- [ ] Catalogue is built to standardize and has not scaled (adoption, not templates, is
      the constraint).
- [ ] Savings ledger is a floor, not a measure of total worth.
- [ ] Regions are not variations of one another.
- [ ] C12 "Other and plant-specific" size, as a data-quality read.

## 6 · Handoff

This protocol feeds `od-scorecard-reporting`'s ODEC/COP/retro prep with the *why* behind
the monthly numbers (the regional diagnosis, the savings honesty, the ranked backlog) —
it does not replace the Scorecard/Power BI figures `od-scorecard-reporting` reads directly
from their own authoritative sources; name which of the two a number in a deck came from.

**Next:** ⟨`od-scorecard-reporting` round prep · `od-decision-routing` for a ranked item
that needs a gate · back to `od-benefit-calculation` for a ledger gap found during review⟩
