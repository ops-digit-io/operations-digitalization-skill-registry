---
type: Skill Reference
title: Evidence baselines
description: How to read the knowledge base's case groups, rollout maps and savings basis for a candidate use case, and the other demand signals - a reading guide with live-count recipes, no figures.
resource: ../procedure.md
status: draft
tags: [use-case-support-service, practice]
---
# Evidence baselines

Source: `Case Groups` (overview and group notes, built from SharePoint list fields; "AI-grouped ...
indicative arithmetic only; not reviewed by a human"). Check the overview's build date, and treat everything you read there as a
starting point to check with the Plant ME. This file carries no counts: re-count on the live notes and quote with the date.

## What a case group is

A case group is one standard template (capability) in one process family; the knowledge base calls it the unit from which a business case
can be derived. The overview groups all plant use cases into such groups. Every group note carries: a rollout map per plant
(Delivered, Planned, Idea, White space), recorded savings, recorded potential and scalability, and a business case derivation sheet.

To find your candidate's group: template (capability) and process family (Rubber, Plastic, Metal, Assembly, cross-process, other
families). The process family is inferred for use cases that had none recorded (`Case Groups/Process Family Inference`); inferred
members are marked in the notes, so check whether yours is one.

## How strong is the evidence?

The overview rates each group's savings basis (for example Strong, Moderate, Weak, Very weak, None). Count the groups per rating on
the live overview before you argue from it. Patterns that have held when read:

- Ratings tend to be low: recorded savings are thin, so a group is rarely rated above "Weak". Say what the rating is when you quote
  a group.
- Never rank by a group's indicative rollout value alone. The knowledge base itself calls it "plants in the stage times the median recorded
  saving", with "no probability of delivery".
- Three facts from the overview apply to every ranking; re-read each live: how many use cases carry a recorded saving at all (and
  whether the figure is yearly or not stated); how many delivered cases have no recorded saving; and whether costs are taken as zero
  by owner statement (internal effort not priced), in which case delivery capacity, not payback, is the binding limit on rollout.
- Because capacity is the limit, rank by **what the capacity buys**: evidence gap closed, plant roadmap served, second plant enabled.

## Reading a rollout map

Illustrative example (placeholders, not real values): group `<CG-nn> <Template> - <Process family>`.

| Stage | Plants | Reading for a ranker |
|---|--:|---|
| Delivered | `<n>` | A working precedent exists; effort for a new plant should be lower; ask the delivering plants what it took |
| Planned | `<n>` | Already committed; do not re-rank against ideas, rank the order of delivery |
| Idea | `<n>` | Wanted but not committed; a candidate for this exercise |
| White space | `<n>` | Plants that have use cases of this process family but no member here. "A pointer, not a demand signal" (the knowledge base's wording) |

A group note may show recorded savings in only a few of its cases and delivered cases without any recorded saving, and may say that
recording savings for those "is the cheapest way to strengthen a business case for this group". For a ranker this means: a candidate in
a group with many delivered cases and no savings is a **candidate for evidence collection** (hand to `od-handover-and-adoption`), and the
group's lack of euros is not a reason to rank the candidate low.

The derivation sheet at the end of each group note lists what is still unrecorded (typically baseline and KPI, owner and decision).
Copy that gap into your record.

## Demand signals other than the list

| Signal | What the knowledge base shows | Use and limit |
|---|---|---|
| ODEC use case upvoting | ODEC slides put a handful of use cases to the locations and report location interest per use case | The text extraction may not say which figure belongs to which use case; open the archive slide before quoting. Interest is not a commitment |
| Workshop collection | A Definition Workshop leaves a use case list with savings estimation as an open task | The list is valid at the workshop date only |
| Engineering roadmap input | ODEC slides define the input for the next engineering roadmap: carry over or continue projects, new project requests with high value-add (necessity for standardization and future rollouts), integration rollout and extension, strategic initiatives | Names the categories of input; does not rank them |
| Top-use-cases template | ODEC strategy slide template: "savings in location Y, deployed without savings in location X, Z, potential to location D" per use case | Shows the framing OD uses for a cross-plant story: where saved, where deployed without saving, where potential |

## What to write into the record

For each candidate: group id, stage per plant, the group's savings basis, the candidate's own saving rows (with reliability), and
"not recorded" where that is true. Never fill a blank to make the ranking look complete.
