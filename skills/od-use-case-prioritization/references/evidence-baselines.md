---
type: Skill Reference
title: Evidence baselines
description: What the vault already says about a candidate use case before anyone is asked - its case group, rollout map, savings basis, white space and demand signals - and how far each may be trusted when ranking.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [use-case-support-service, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Evidence baselines

Source: `Work-OpsDigit-Knowledge/Case Groups` (overview and group notes, built 2026-11-04 from
SharePoint list fields; "AI-grouped ... indicative arithmetic only; not reviewed by a human"),
read 2026-11-05. Treat everything here as a starting point to check with the Plant ME.

## What a case group is

36 case groups cover all 650 plant use cases. A group is one standard template (11 templates) in one
process family; the vault calls it the unit from which a business case can be derived. Every group
note carries: a rollout map per plant (Delivered, Planned, Idea, White space), recorded savings,
recorded potential and scalability, and a business case derivation sheet.

To find your candidate's group: template (capability) and process family (Rubber, Plastic, Metal,
Assembly, cross-process, other families). Process family is inferred for 251 use cases that had
none recorded (`Case Groups/Process Family Inference`); inferred members are marked in the notes.

## How strong is the evidence?

The overview rates each group's savings basis. Count over the 36 group notes read on 2026-11-05:

| Savings basis | Groups |
|---|--:|
| Weak | 11 |
| Very weak | 15 |
| None | 10 |
| Strong or moderate | 0 |

No group has a basis above "Weak". Consequences for ranking:

- Never rank by a group's indicative rollout value alone. The vault itself calls it "plants in the
  stage times the median recorded saving", with "no probability of delivery".
- Three facts from the overview apply to every ranking: recorded savings are thin (62 of 650 use
  cases, EUR 2,384,217, not stated as yearly); 269 delivered cases have no recorded saving; costs
  are taken as zero by owner statement of 2026-11-04 (internal effort not priced), so delivery
  capacity, not payback, is the binding limit on rollout.
- Because capacity is the limit, rank by **what the capacity buys**: evidence gap closed, plant
  roadmap served, second plant enabled.

## Reading a rollout map

Worked example, group CG-03 Andon Board - Assembly (44 plant use cases, read 2026-11-05):

| Stage | Plants | Reading for a ranker |
|---|--:|---|
| Delivered | 10 | A working precedent exists; effort for a new plant should be lower; ask the delivering plants what it took |
| Planned | 2 | Already committed; do not re-rank against ideas, rank the order of delivery |
| Idea | 1 | Wanted but not committed; a candidate for this exercise |
| White space | 7 | Plants that have use cases of this process family but no member here. "A pointer, not a demand signal" (the vault's wording) |

The same note lists recorded savings of EUR 42,000 in 3 of 44 cases (basis Weak), 27 of 27 delivered
cases without a recorded saving, and states that recording savings for those "is the cheapest way
to strengthen a business case for this group". For a ranker this means: a candidate in a group with
many delivered cases and no savings is a **candidate for evidence collection** (hand to
`od-impact-evaluation`), and the group's lack of euros is not a reason to rank the candidate low.

The derivation sheet at the end of each group note lists what is still unrecorded; for CG-03 the
baseline and KPI and the owner and decision are "Not recorded". Copy that gap into your record.

## Demand signals other than the list

| Signal | What the vault shows | Use and limit |
|---|---|---|
| ODEC use case upvoting | 2025 ODEC slides (June and August) put four use cases to the locations: downtime reduction, digital Gemba, peak detection, shut-down initiative; the August slide reports location interest per use case (one entry reads "75% of locations interested") | The extraction does not say which figure belongs to which use case; open the archive slide before quoting. Interest is not a commitment |
| Workshop collection | A Definition Workshop leaves a use case list with savings estimation as an open task; Carei 2024 collected about 33 use cases (workshop summary slide) | Counts at that workshop date only |
| Engineering roadmap input | ODEC 2025 slides define input for the 2026 engineering roadmap: carry over or continue projects, new project requests with high value-add (necessity for standardization and future rollouts), integration rollout and extension, strategic initiatives | Names the categories of input; does not rank them |
| Top 10 use cases template | ODEC 2024 strategy slide: "XX Savings in Location Y, Deployed without Savings in Location X,Z, Potential to Location D" per use case | The template shows the framing OD uses for a cross-plant story: where saved, where deployed without saving, where potential |

## What to write into the record

For each candidate: group id, stage per plant, the group's savings basis, the candidate's own saving
rows (with reliability), and "not recorded" where that is true. Never fill a blank to make the
ranking look complete.
