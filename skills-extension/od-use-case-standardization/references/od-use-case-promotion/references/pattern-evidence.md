---
type: Skill Reference
title: Pattern evidence
description: How to read the portfolio aggregates that frame a promotion decision (declared standard, library and CSP status, case groups, handover and utilization), how to count them live, and what they do not show - guidance only, no figures.
resource: ../procedure.md
status: draft
tags: [analytical-support-service, practice, aggregate]
---
# Pattern evidence

Sources: the bundle file `kg_nodes.csv` and the knowledge base's Case Groups notes (labelled "AI-grouped from SharePoint list fields;
indicative arithmetic only; not reviewed by a human"). They frame a decision; they never replace the evidence about the single
asset. **This file carries no counts**: re-count on the live lists and quote the result with its source and date.

## How much is already declared standard

Recipe: on the use-case list, group by the category recorded at intake and count each category.

| Category at intake | Reading |
|---|---|
| Standard use case, cross process | Declared standard at intake |
| Standard use case, per process | Declared standard at intake |
| Non-standard, unique to one plant | The group where genuinely recurring needs hide |
| AI use case (generative, machine learning, deep learning) | Separate track |
| Category not recorded | A data gap, not a category |
| Group record | A container row, not a use case |

Also count, live: delivery status (`IDEA`, `PLANNED`, `IMPLEMENTED`, `PRODUCTIVE`, `STOPPED`), handover (`DONE`, `ONGOING`, not
recorded), the output asset recorded (dashboard, report, app, analytics workflow, agent) and utilization where recorded
(`od-handover-and-adoption`, `od-first-aid-kit`).

Reading: when most use cases are declared standard at intake, "promotion" is mostly about assets that **started outside the
portfolio** (ad-hoc requests) and about the "unique" ones that turn out to recur.

## The library and the CSP gate

Recipe: on the UseCase Library list, count entries by CSP decision (`Yes`, `No`, no decision recorded) and by "CSP initiated".
The Knowledge Bundle, `Decision rights`, states how far the gate has been applied. Reading: if only a few entries are recorded as
standard enough to roll out, the realistic outcome of a promotion is *prepared for the CSP gate*, not *in the catalog*
(`catalog-usecase`).

## The case groups (template x process family)

A case group is a capability template in one process family; the groups together cover all plant use cases. Recipes on the live
Case Groups overview: how many use cases are delivered (`PRODUCTIVE` or `IMPLEMENTED`); how many carry a recorded saving and the
total (and whether it is stated yearly); the recorded-savings basis per group (very weak / weak / none / moderate); how many groups
are delivered at several plants and how many at one plant or none. "Other Use Cases" groups are "a catch-all, not a pattern".

How to use it in a promotion:

- **An ad-hoc asset that belongs to a group already delivered at many plants is probably a reuse case,** not a new standard:
  check the group's reference solutions and scale-up candidates in its note before proposing anything.
- **An asset in a group delivered at 0 to 1 plants** is where a first proven instance is worth the most, and also where
  evidence is thinnest.
- **White space is a pointer, not a demand signal** (Case Groups note): plants that have the process family but no member. Do not
  cite it as demand for the promoted asset.
- **Savings basis is usually weak.** Group notes can show delivered cases without any recorded saving and call recording them
  "the cheapest way to strengthen a business case". The same applies to a promotion: recording the saving of the first
  instance is the cheapest evidence to add.
- **Costs in the Case Groups arithmetic may be taken as zero** by an owner statement ("no external cost, internal effort not
  priced"; the binding limit is delivery capacity per plant). Check the overview for that convention and do not carry it into
  a promotion package as if it were a finding.

## What these numbers do not show

- Whether the second plant **took** the first plant's solution: adoption is the measure of standardization
  (`od-use-case-standardization`), and the portfolio analysis finds the catalogue "built to standardize and has not scaled".
- The promotion rate: the lane lists it as a metric with source `⟨tracker — to collect⟩`; if no promotion is recorded in any
  source, there is no baseline.
- Regional difference: use cases and productive use cases differ by region (`od-use-case-standardization`). A promotion built
  on an asset from one region says nothing yet about another.
