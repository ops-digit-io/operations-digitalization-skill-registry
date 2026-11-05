---
type: Skill Reference
title: Pattern evidence
description: Portfolio aggregates that frame a promotion decision - declared standard, library and CSP counts, the 36 case groups, handover and utilization - with what each number does and does not show.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [analytical-support-service, practice, aggregate]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Pattern evidence

All counts are from the bundle file `kg_nodes.csv` and the vault's Case Groups notes (read 2026-11-05;
Case Groups generated 2026-11-04 and labelled "AI-grouped from SharePoint list fields; indicative
arithmetic only; not reviewed by a human"). They frame a decision; they never replace the evidence about
the single asset.

## How much is already declared standard

| Category at intake (650 use cases) | Count |
|---|--:|
| Standard use case, cross process | 253 |
| Standard use case, per process | 222 |
| Non-standard, unique to one plant | 88 |
| AI use case (generative 15, machine learning 3, deep learning 2) | 20 |
| Category not recorded | 66 |
| Group record | 1 |

Delivery status: `IDEA` 229, `PLANNED` 122, `IMPLEMENTED` 129, `PRODUCTIVE` 167, `STOPPED` 2. Handover:
`DONE` 272, `ONGOING` 38, not recorded 340. Output asset recorded for 202: dashboards 173, reports 12, apps
11, analytics workflows 5, agent 1. Utilization where recorded: 125 daily, 8 `NEVER`
(`od-handover-and-adoption`, `od-analytical-support-service`).

Reading: 475 of 650 use cases are declared standard at intake (253 + 222), so "promotion" is mostly about assets that
**started outside the portfolio** (ad-hoc requests) and about the 88 "unique" ones that turn out to recur.

## The library and the CSP gate

100 library use cases (proven reference solutions). CSP decision: `Yes` 5, `No` 46, no decision recorded 49;
"CSP initiated" `Yes` 5, `No` 42, blank 53. The Knowledge Bundle, `Decision rights`, states the gate "applied
to 51 of the 100 entries so far". Reading: only five entries are recorded as standard enough to roll out, so
the realistic outcome of a promotion today is *prepared for the CSP gate*, not *in the catalog*
(`catalog-usecase`).

## The 36 case groups (template x process family)

A case group is a capability template in one process family. 36 groups cover all 650 use cases; 296 are
delivered (`PRODUCTIVE` or `IMPLEMENTED`); 62 use cases carry a recorded saving, €2,384,217 in total. The groups'
recorded-savings basis: 15 "very weak", 11 "weak", 10 "none"; none is "moderate". "Other Use Cases" groups are
"a catch-all, not a pattern".

Where a pattern already recurs across plants (plants delivered):

| Group | Use cases | Delivered | Plants delivered | Cases with a saving | Basis |
|---|--:|--:|--:|--:|---|
| Andon Board, Assembly | 44 | 27 | 10 | 3 | Weak |
| Process Values, Assembly | 45 | 17 | 8 | 5 | Weak |
| Process Values, Rubber | 62 | 39 | 7 | 7 | Weak |
| Andon Board, Rubber | 32 | 17 | 7 | 1 | Very weak |
| Cycle Time, other families | 18 | 10 | 7 | 4 | Weak |
| Downtime Reporting, other families | 17 | 12 | 7 | 3 | Weak |

Twelve of the 36 groups are delivered at five or more plants; six are delivered at one plant or none.

How to use it in a promotion:

- **An ad-hoc asset that belongs to a group already delivered at 5 or more plants is probably a reuse
  case,** not a new standard: check the group's reference solutions (for CG-03 the note lists 16 reference
  solutions and 7 scale-up candidates) before proposing anything.
- **An asset in a group delivered at 0 to 1 plants** is where a first proven instance is worth the most, and
  also where evidence is thinnest.
- **White space is a pointer, not a demand signal** (Case Groups note): plants that have the process family
  but no member. Do not cite it as demand for the promoted asset.
- **Savings basis is weak everywhere.** In CG-03, 27 of 27 delivered cases have no recorded saving; the
  group note calls recording them "the cheapest way to strengthen a business case". The same applies to a
  promotion: recording the saving of the first instance is the cheapest evidence to add.
- **Costs in the Case Groups arithmetic are taken as zero** by an owner statement of 2026-11-04 ("no
  external cost, internal effort not priced"; the binding limit is delivery capacity per plant). Do not
  carry that convention into a promotion package as if it were a finding.

## What these numbers do not show

- Whether the second plant **took** the first plant's solution: adoption is the measure of
  standardization (`od-use-case-standardization`), and the portfolio analysis finds the catalogue
  "built to standardize and has not scaled".
- The promotion rate: the lane lists it as a metric with source `⟨tracker — to collect⟩`; no promotion is
  recorded in any source read, so there is no baseline.
- Regional difference: Europe 312 use cases with 81 productive, Americas 168 with 70, Asia 138 with 16
  (`od-use-case-standardization`). A promotion built on a Europe asset says nothing yet about Asia.
