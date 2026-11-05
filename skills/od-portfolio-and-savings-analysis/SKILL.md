---
name: od-portfolio-and-savings-analysis
description: >-
  Analyse the OD portfolio and its savings ledger without being wrong about it — cut the
  plant use cases by plant, region, capability, cluster, status and asset; read the savings
  ledger for what it does and does not claim; and apply the three ways this data most
  often misleads (absence read as zero, tracked read as proven, implemented read as in
  use). Use for any portfolio question, regional or plant comparison, standardization or
  conversion-rate analysis, savings roll-up, or when a number about the portfolio is going
  into a deck, a board paper or a business case.
license: Internal — OESL MPEE Operations Digitalization. Not for external distribution.
metadata:
  id: od-portfolio-and-savings-analysis
  tier: practice
  lane: [analytical-support-service, use-case-support-service]
  owner_role: Digital-Business-Value-Engineer (DBVE)
  authority_level: read-only
  status: stable
  sources_read: 2026-10-22
  requires: [od-context]
  composes: [od-sharepoint-list-export, od-benefit-calculation, od-use-case-standardization, od-scorecard-reporting, od-decision-routing]
  derived_from:
    - ops-knowledge-graph/_knowledge/20-Done/Use case portfolio analysis.md
    - ops-knowledge-graph/_knowledge/10-Department/Savings and value tracking.md
    - ops-knowledge-graph/_knowledge/10-Department/Use case lifecycle.md
    - ops-knowledge-graph/_knowledge/10-Department/Systems of record.md
    - Project Management Institute (2017). The Standard for Portfolio Management, 4th edition. PMI. Categorization, evaluation and prioritization/balancing as distinct steps — the rollup and regional-handling method's backbone.
    - weighted-scoring and value-vs-effort prioritization models (standard project-portfolio practice; see references/prioritization.md for the specific criteria adaptation, ours).
  okf:
    type: Agent Skill
    title: Portfolio and savings analysis
    tags: [analytical-support-service, practice, use-case-support-service]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-08-25T00:00:00Z }
---

# Portfolio and savings analysis

Read `od-context` first.

## The references are the substance

| File | Use it for |
|---|---|
| [`references/rollup-method.md`](references/rollup-method.md) | Which boundaries a sum may never cross (tracked/proven, reliability class) — the general rule behind "never merge tracked and proven" |
| [`references/prioritization.md`](references/prioritization.md) | A weighted-scoring/value-effort method for ranking use cases in a review, and the unscoreable bucket for `UNKNOWN` priority/potential |
| [`references/regional-handling.md`](references/regional-handling.md) | Why Europe/Americas/Asia are never blended into one conversion figure, and what to report instead |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | Order of ranking criteria, numbered planning states, the where-saved matrix, dependency versus return ordering, kill and hold hygiene, and what an agent may draft |
| [`references/strategic-initiatives-and-savings.md`](references/strategic-initiatives-and-savings.md) | How to read strategic business cases next to plant savings: addressable vs realistic, anchors, no double counting, what may enter the portfolio |

Output: [`assets/portfolio-review-protocol.md`](assets/portfolio-review-protocol.md) — one
document per review round, built from `od-sharepoint-list-export`'s capture and
`od-benefit-calculation`'s ledger, feeding `od-scorecard-reporting`'s round prep.

## The shape of the portfolio: how to read it, not what it is

This skill carries no counts. Every figure comes from a live read of the use case list
(`od-sharepoint-list-export`) with its capture date. The cuts to take, and what each field means:

| Delivery status | Means |
|---|---|
| `IDEA` | Recorded, not yet committed to a plan |
| `PLANNED` | Committed, not yet built |
| `IMPLEMENTED` | Built and handed to the plant |
| `PRODUCTIVE` | In daily use |
| `STOPPED` | Deliberately discontinued |

The share of what has been asked for that has been built is `IMPLEMENTED` plus `PRODUCTIVE`
over all use cases; the rest is a queue with a known shape rather than a wish list. Always
state the denominator.

- **Workflow state** (Development, Implementation, Handover, each `DONE` or `ONGOING`):
  read it as a funnel, and cross-check it against the delivery status before quoting either;
  the two are maintained separately and can disagree.
- **Category**: standard use case cross process, standard per process, non-standard unique
  to one plant, AI use case (generative, ML or deep learning). Rank within a category.
- **Rollout phase** (`PHASE 1` onwards) is recorded only on some use cases. Phases are
  **named rollout batches, not sequential queues**; a blank phase is not "phase 0".
- **Output asset** (dashboard, report, app, analytics workflow, agent) and **utilization**
  (Daily, Weekly, Monthly, On-Demand, `NEVER`) are recorded only where someone filled them.
  Count the recorded ones as the denominator, never the whole portfolio.

## Regional shape: the finding that matters most

Cut use cases, productive use cases and conversion (productive over all) per region, live.
Expect the regions to differ sharply, and never blend them (`references/regional-handling.md`).
**A low-converting region is a different problem from a high-converting one, not a smaller
one.** Any plan that treats the regions as scaled copies of each other will fail in the
weakest one. The best-converting region's rate is the one worth interrogating for what it
does differently.

## The savings ledger

Read the ledger live: row count, tracked euros, proven euros and proven rows, the split by
reliability (`CALCULATION`, `ESTIMATION`, not recorded), automated versus manual rows, and
the number of use cases that carry a saving figure of any kind. Quote each with its capture
date. Pattern to expect: the tracker was actively maintained for a period and then largely
abandoned, so the reliability field is mostly empty and few use cases carry a figure. Treat
the total as a **floor on what has been captured**. See `od-benefit-calculation` for how a
row is built and what may be added to what.

## The three ways this data misleads

1. **Absence read as a zero.** Many use cases carry `UNKNOWN` priority or `UNKNOWN`
   potential, and many saving rows carry no reliability. "The top priorities" phrased so
   that the remainder is low is reading absence as an answer.
2. **Tracked read as proven.** Never add the two.
3. **`IMPLEMENTED` read as in use.** It is not; that is what `PRODUCTIVE` and the
   utilization field are for.

And one about provenance: **version history carries text the current record does not.**
Rationale, blockers and comments were written during active work and later tidied back to
`-`. An analysis over the current snapshot alone is missing a large part of the narrative
— export versions, not just items (`od-sharepoint-list-export`).

## Standing findings to check an analysis against

- **The catalogue is built to standardize and has not scaled.** Capabilities are
  instantiated at (nearly) every plant, so templates are not the constraint — adoption of
  the proven instance is. Verify on the live capability instance list.
- **The savings ledger is mostly empty scaffolding.** Verify by counting blank reliability.
- **The regions are not variations of one another.**
- **C12 "Other and plant-specific" is a data-quality signal**, not only a topical one;
  track its size over time rather than quoting it once.

## Procedure

1. State which surface you are reading and when it was captured. The knowledge graph is a
   rebuilt read surface; the SharePoint lists are the write surface.
2. Cut by plant / region / capability / cluster / status / asset — never by one dimension
   alone when a claim about scale is being made.
3. For every empty field, decide and **state** whether it is unknown or genuinely nil.
4. Label every euro figure tracked or proven, per `references/rollup-method.md`.
5. Name the denominator on every rate, and never blend the three regions into one —
   `references/regional-handling.md`.
6. Rank only within a category — `references/prioritization.md` — and keep the unscoreable
   bucket visible rather than folding it into the bottom of a ranked list.
7. Fill [`assets/portfolio-review-protocol.md`](assets/portfolio-review-protocol.md) as the
   review happens; it is the record a reader who was not in the room can act on.

## Do not

- Do not treat rollout or deployment count as value, and do not write "no potential" for a scaled use case without savings; mark it for further investigation.
- Do not rank without saying which order of criteria was used and which planning state it is.
- Do not roll up savings across reliability classes into one headline.
- Do not compare regional counts without their conversion rates.
- Do not present a portfolio figure without the date it was read.
