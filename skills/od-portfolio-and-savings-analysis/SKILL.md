---
name: od-portfolio-and-savings-analysis
description: >-
  Analyse the OD portfolio and its savings ledger without being wrong about it — cut 650
  use cases by plant, region, capability, cluster, status and asset; read the savings
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
  sources_read: 2026-08-24
  requires: [od-context]
  composes: [od-sharepoint-list-export, od-benefit-calculation, od-use-case-standardization]
  derived_from:
    - ops-knowledge-graph/_knowledge/20-Done/Use case portfolio analysis.md
    - ops-knowledge-graph/_knowledge/10-Department/Savings and value tracking.md
    - ops-knowledge-graph/_knowledge/10-Department/Use case lifecycle.md
    - ops-knowledge-graph/_knowledge/10-Department/Systems of record.md
  okf:
    type: Agent Skill
    title: Portfolio and savings analysis
    tags: [analytical-support-service, practice, use-case-support-service]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-08-25T00:00:00Z }
---

# Portfolio and savings analysis

Read `od-context` first.

## The shape of the portfolio

650 plant use cases.

| Delivery status | Count | Means |
|---|--:|---|
| `IDEA` | 229 | Recorded, not yet committed to a plan |
| `PLANNED` | 122 | Committed, not yet built |
| `IMPLEMENTED` | 129 | Built and handed to the plant |
| `PRODUCTIVE` | 167 | In daily use |
| `STOPPED` | 2 | Deliberately discontinued |

Roughly **45 % of what has been asked for has been built**, and the rest is a queue with a
known shape rather than a wish list.

| Workflow state | DONE | ONGOING |
|---|--:|--:|
| Development | 307 | 30 |
| Implementation | 303 | 27 |
| Handover | 272 | 38 |

| Category | Count |
|---|--:|
| Standard use case, cross process | 253 |
| Standard use case, per process | 222 |
| Non-standard, unique to one plant | 88 |
| AI use case (generative, ML or deep learning) | 20 |

Rollout phase `PHASE 1`–`PHASE 5` is recorded on 319 use cases; Phase 1 is largest (197),
Phase 5 second (73). Phases are **named rollout batches, not sequential queues**.

Output assets, of the 202 that record one: 173 dashboards, 12 reports, 11 apps,
5 analytics workflows, 1 agent. Utilization, where recorded: 125 daily, 8 `NEVER`.

## Regional shape — the finding that matters most

| Region | Use cases | Productive | Conversion |
|---|--:|--:|---|
| Europe | 312 | 81 | 26 % |
| Americas | 168 | 70 | **42 % — best in the estate** |
| Asia | 138 | 16 | 12 % |

**Asia is a different problem from Europe, not a smaller one.** Any plan that treats the
three regions as scaled copies of each other will fail in Asia. The Americas' conversion
rate is the one worth interrogating for what it does differently.

## The savings ledger

553 rows, **€2,384,217 tracked**, **€653,820 proven** across 19 rows. Reliability:
43 `CALCULATION`, 36 `ESTIMATION`, **474 not recorded**. Automated 477, manual 76. Only
**62 of 650 use cases carry a saving figure of any kind.**

The tracker was actively maintained for a period and then largely abandoned. Treat the
total as a **floor on what has been captured**. See `od-benefit-calculation` for how a
row is built and what may be added to what.

## The three ways this data misleads

1. **Absence read as a zero.** 362 use cases carry `UNKNOWN` priority, 405 `UNKNOWN`
   potential, 474 saving rows no reliability. "The top priorities" phrased so that the
   remainder is low is reading absence as an answer.
2. **Tracked read as proven.** Never add the two.
3. **`IMPLEMENTED` read as in use.** It is not; that is what `PRODUCTIVE` and the
   utilization field are for.

And one about provenance: **version history carries text the current record does not.**
Rationale, blockers and comments were written during active work and later tidied back to
`-`. An analysis over the current snapshot alone is missing a large part of the narrative
— export versions, not just items (`od-sharepoint-list-export`).

## Standing findings to check an analysis against

- **The catalogue is built to standardize and has not scaled.** Every capability is
  instantiated at 32 or 33 of 33 plants, so templates are not the constraint — adoption of
  the proven instance is.
- **The savings ledger is mostly empty scaffolding.**
- **The regions are not variations of one another.**
- **C12 "Other and plant-specific" at 168 use cases is a data-quality signal**, not only a
  topical one.

## Procedure

1. State which surface you are reading and when it was captured. The knowledge graph is a
   rebuilt read surface; the SharePoint lists are the write surface.
2. Cut by plant / region / capability / cluster / status / asset — never by one dimension
   alone when a claim about scale is being made.
3. For every empty field, decide and **state** whether it is unknown or genuinely nil.
4. Label every euro figure tracked or proven.
5. Name the denominator on every rate.

## Do not

- Do not roll up savings across reliability classes into one headline.
- Do not compare regional counts without their conversion rates.
- Do not present a portfolio figure without the date it was read.
