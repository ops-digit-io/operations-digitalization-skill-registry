---
type: Skill Reference
title: Ranking criteria
description: Every criterion OD has itself used to rank or classify use cases, each with its source and its limit, so a ranking can be built from the department's own language and not from invented scores.
resource: ../procedure.md
status: draft
tags: [use-case-support-service, practice]
---
# Ranking criteria

Nothing here is a formula OD has published. These are the criteria that appear in OD's own
documents and decks; the *weights* are not written down anywhere read (see `SKILL.md`, "What is
still open"). Pick the criteria, agree weights with the Plant ME, and write both into the record.

## 1 · Gates (pass or fail, never scored)

| Gate | Rule | Source |
|---|---|---|
| Roadmap link | A request without a plant roadmap link is refused | `00-core/05-intake.md` "Explicitly refused" |
| Nameable business case | A request without one is refused and returned to the demand owner | `05-intake.md`; playbook error path |
| Lean standardized footprint | Solutions needing systems outside it (example in the source: non-standard MES rollout short or mid term) are refused | `05-intake.md` |
| Sibling-function ownership | Automation-solution build, facility/energy and tool-center work is not OD's | `05-intake.md` |
| Strategic-plant alignment | Prioritization aligns with strategic-plant scope | `05-intake.md` "Prioritisation" |

A candidate that fails a gate is not ranked low; it is out of this exercise (`od-use-case-intake-triage`).

## 2 · Value criteria

| Criterion | What to read | Source | Limit |
|---|---|---|---|
| Saving potential | Tracked saving rows and their reliability label | `00-core/05-intake.md` ("savings, lead-time reduction, cost avoidance"); `od-benefit-calculation` | Many use cases carry no saving figure (count them in the ledger); blank is "not assessed", not zero |
| Generalization potential | Is this a standard use case that other plants can take over? | Workshop slide "Collection of Smart Factory Use Case demand": classification and priority currently by highest generalization potential, then highest saving potential | The slide is a workshop deck, not a rule document |
| Roadmap fit | Does it sit in the plant's machine integration wave or project (for example MSB rollout, QFPR rollout)? | A definition workshop's stated purpose, for example "Use Case Prioritization for the next Machine Integration Wave" | Plant specific |
| Lead-time or cost avoidance | Named separately in the intake rule | `05-intake.md` | No metric or unit given: ⟨how lead time is valued⟩ |

## 3 · Effort and risk criteria

| Criterion | What to read | Source |
|---|---|---|
| Dependencies | `ECR APPROVAL`, `ECR CREATION`, `PLANT`, `MACHINE INTEGRATION`, `OTHERS`, `NO DEPENDENCY` and who owns each | `od-benefit-calculation` |
| Data readiness | Machines connected, signals available | `od-data-availability-check` |
| Category | A standard use case with an existing library entry costs less to repeat than a non-standard one | `od-use-case-definition`, `od-use-case-standardization` |
| Fit of the solution | Does the idea quietly need MES/EMS or a capability nobody has? | `od-use-case-solution-evaluation` |
| Wait states OD does not control | Investment approval (OD lead, BA Operations); Cyber Security sign-off for an external machine connection | `playbook.md` "Wait states" |
| Infrastructure effort | Example in a definition-workshop summary slide: a measure rated low because "Infrastructure (Cabling) + QFPR is needed to be deployed, thus time frame is longer, while other Measures have direct impact" | Split Slides, a definition-workshop summary (Slide Index note for 10-Workshops) |

## 4 · The two views OD uses to show a ranking

| View | Axes | Where it appears |
|---|---|---|
| Urgency and Importance | Each 1 to 4, Low to High, plus a Cost/Benefit field and the remark "incremental value: even if some objectives are not reached, the use case provides tangible benefits for the organization" | Use Case Canvas page 2 (Standard Agenda deck, canvas templates per plant) |
| Technology and business value | Two-dimensional diagram; the slide note says "How to generate matrix?" and gives no answer | Use Case Canvas speaker note |
| Value and risk | "Build the cheapest possible test design to learn the most important thing": low-risk high-value means just build it; low-value items are not worked on, not tested and in most cases not built | Standard Agenda deck, slide "How - Value Creation by Digitalization" |
| Planning tiers | "Just do it", "Go forward", "Lead change" over clusters, with columns Cluster, Use Case, Description, Impact, Year, Budget | UseCase_Priorities deck (tiers slides and table slide) |

Reading the planning tiers as used there (by their own wording): *Just do it* = generic, low-effort use cases (dashboard,
notification, reaction time); *Go forward* = continue or integrate a prototype that needs a data aggregation step first;
*Lead change* = exploratory topics (simulation, digital shadow, agentic AI). The deck states these as headlines of a
planning state, not as a scoring rule; open the current deck for the current content.

## 5 · The planning iteration

The priorities deck labels its state as a numbered planning state and lists three inputs that drive each
iteration: technical inputs, the latest use case workshops, and the latest input on plant priority
(slide 6). Use the same three when you re-rank: technical constraints, what the last workshop
collected (`od-workshop-facilitation`), and what the plant says now.

## 6 · A portfolio pattern worth borrowing

The knowledge base's Business Cases notes (`Graph/Business Cases`) carry a
"portfolio tier" such as Quick Win, Big Bet, Enabler, Platform and "Defer to Year 2+", plus score
fields (strategic fit, synergy, value-effort score, confidence). They belong to a separate AI
business case list, so do not copy their scores onto plant use cases. What transfers is the idea of
**naming an enabler that earns no euro of its own** (for example the Catalog Maturity Sprint, whose
stated gate is that catalogued use cases carry priority, potential and risk scores): enablers are ranked by what they unlock, not by savings.
