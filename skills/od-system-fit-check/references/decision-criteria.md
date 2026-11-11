---
type: Skill Reference
title: Decision criteria
description: "The six scored decision criteria and the verdict taxonomy Go / PoC-first / Reduce-complexity / Hold / Reject / Blocked, with one decisive reason."
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [invest-screen, gate, department-package]
derived_from:
  - "Department knowledge base, read 2026-11-10"
generated: { by: claude-code/1, at: 2026-11-10T00:00:00Z }
---
> Transcribed from the department package `investment-checking.zip/reference/decision-criteria.md` (the master).

# Decision criteria — scored rubric and verdict mapping

Score criteria 1–5 on 0 / 1 / 2. Criterion 6 is the **hard gate** (see `software-footprint-gate.md`), not a soft score. Show every sub-score.

## 1. Healthy business case
- **2** — nameable value (saving / lead-time / risk-reduction / customer-mandatory), linked to a plant or central roadmap, a rough payback, and a kill criterion.
- **1** — value plausible but unquantified, or roadmap link unclear.
- **0** — no value stated, or "nice to have" only. If 0 and OD-touching, the honest position is: not OD's to push.

## 2. Compounding across the organisation
- **2** — reuses / extends an existing platform or standard, or creates a reusable capability (standard signal model, repeatable use case, template) that others can adopt.
- **1** — some reuse, but largely plant-local.
- **0** — one-off island; every future instance would re-buy from scratch.

## 3. Interface standardisation
- **2** — uses standardised interfaces (OPC UA / MQTT / MSB connector / data-platform path) or is easily steered there.
- **1** — mixed; a standard path exists but the vendor default is proprietary.
- **0** — proprietary/ad-hoc endpoints (vendor FTP, bespoke DB dumps, a parallel data path) that compete with internal connectors and lock in custom glue.

## 4. Complexity load (footprint & PoC-first)
- **2** — keeps the footprint lean; fits existing operations; or is scoped as a small proof before any wider commitment.
- **1** — adds moderate operational burden; manageable but watch it.
- **0** — heavy new footprint, new tool/vendor to operate, or an org-wide commitment with no proof yet. Ask: *what must be proven first?* Prefer PoC-first; name a complexity-reduction alternative.

## 5. Cross-region / tech interlock
- **2** — clearly woven with OD elsewhere; co-ownership defined or proposed.
- **1** — some technological overlap; needs a conversation.
- **0** — treated as standalone though it will parallel or collide with an OD platform (e.g. a fresh energy-data silo, a parallel MES-like control system). *(A 0 here is a flag to engage, not necessarily to reject.)*

## 6. Software / IT-footprint gate (HARD)
Pass / **Blocked** per `software-footprint-gate.md`. A Blocked gate overrides the numeric total.

---

## Score → verdict

Let `S = sum(criteria 1–5)` (max 10).

| Condition | Verdict |
|---|---|
| Gate (6) tripped & unresolved | **Blocked** — resolve footprint before any other verdict stands |
| Gate clear · `S ≥ 8` · no criterion at 0 | **Go** |
| Real value but crit 4 = 0 or major unknowns | **PoC-first** — define & scope the proof small |
| Workable but crit 3 = 0 or over-engineered | **Reduce-complexity** — name the simpler / standard path |
| Business case missing (crit 1 = 0) or blocked dependency, not clearly dead | **Hold** — state the revisit trigger |
| Hits a non-bet / no value / duplicates a stopped initiative | **Reject** — name the non-bet or reason |

When several conditions apply, the **most upstream blocker wins**: Blocked > Reject > Hold > Reduce-complexity > PoC-first > Go. State the single decisive reason.

## Strategy anchors (from `00-core/02-strategy.md`)
- Reinforces a **bet** (data platform / MSB+CyberSec / MES-pilot-only) → supports Go/PoC-first.
- Hits a **non-bet** (standardised MES rollout, EMS restart, OD building automation or owning energy/facility, tool proliferation) → pushes Hold/Reject.
- Prefer few systems / small footprint / standardised modular deployments.
