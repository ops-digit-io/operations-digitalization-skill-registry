---
type: Skill Reference
title: Savings proof path
description: The path a use case saving takes from a workshop pre-evaluation to a SPRINT-proven row as OD's own decks describe it, the firmness label at each step, and where it stalls.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [use-case-support-service, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Savings proof path

Read with `od-benefit-calculation`, which owns how a saving row is built. This file adds the
*path* a row travels and how to evaluate where a given row stands. Sources are OD workshop decks
(Use Case Creation Process, 2024-07-29; Workshop Summary, 2022-07-13), the department's saving
ledger as described in `od-benefit-calculation` (state of 2026-10-22), and the vault's case groups
(2026-11-04). The decks are presentations, not rule documents.

## The steps, as the decks describe them

| # | Step | What the decks say | Firmness label to record |
|---|---|---|---|
| 1 | **Pre-evaluation in the savings list** | A template for savings pre-evaluation exists with examples. Savings are collected in the Savings List initially; every saving must be linked to a concrete use case in the plant's use case list; cumulated savings per use case are entered in the list (2022 and 2024 decks) | Pre-evaluation. Not a ledger claim yet |
| 2 | **Calculated, not guessed** | 2024 deck: "The Savings shall be calculated, only in some minor cases they can be estimated". 2022 deck: the figure in the list "can also be a first realistic estimation, because the Savings must be reported within the SPRINT" | `CALCULATION` if a methodology line exists, otherwise `ESTIMATION` (labels from `od-benefit-calculation`) |
| 3 | **Linked to a SPRINT project** | 2024 deck: savings "are linked to the Use Case and finally to the Sprint Project that will be created"; the pre-evaluation "can in the end be linked with the Sprint project" | Linked, not proven |
| 4 | **Use in the process** | Utilization process slide: connect relevant machines (high runners, troublemakers); collect and select parameters; analyse parts produced, utilization rate, downtimes, parameter specification; analyse root cause (the slide names commonly known methods such as A3); "create and calculate cost saving project and report savings"; eliminate the deviations | Evidence that the mechanism ran |
| 5 | **SPRINT portfolio review** | `od-context` and `od-benefit-calculation`: only SPRINT turns a tracked saving into a proven one | Proven. 19 of 553 rows, EUR 653,820, as of the 2026-10-22 ledger state |

Calculation categories named on the "Use Case Calculation Methods" slide (2024): cycle time
monitoring, produced parts per tool lifetime, process parameter monitoring (temperatures,
pressures, speeds and so on); the slide adds that the list of potential categories "can be checked
with the plant domain" and that workshop outputs may give more. The pre-evaluation template examples
are grouped as productivity (lot optimization, setup optimization), quality (scrap and waste
reduction) and maintenance (reduction of reaction time and breakdown time).

## How to place a row on the path

Ask in order; the first "no" is where the row stands and what the next step is.

| Question | If no |
|---|---|
| Is the row linked to a named use case? | Link it. Nothing else counts |
| Is there a baseline measured before the use case (scrap, downtime, reporting hours, parts per tool life)? | Record "baseline not recorded" and name who can measure it. CG-03's derivation sheet lists the baseline and KPI as "Not recorded" for the whole Andon Board - Assembly group |
| Does the methodology line show a formula with real inputs that a stranger can recompute? | Label `ESTIMATION`; do not upgrade. A `CALCULATION` without methodology is an estimation wearing the wrong label (`od-benefit-calculation`) |
| Did the figure come from OD's calculator, or from the plant alone? | Treat a plant-only figure with no formula as an estimation candidate. The department's own record: plants asked to self-originate a number tended to produce none; the working approach is OD computing a first number the plant reacts to (`od-benefit-calculation`, `references/review-checklist.md`) |
| Is the dependency recorded with its owner (`ECR APPROVAL`, `MACHINE INTEGRATION`, `PLANT` ...)? | Record it on the row; a gated saving stays visible instead of being dropped |
| Is it linked to a SPRINT project? | Prepare it for the SPRINT review: row, rationale, methodology, baseline, evidence of use |
| Has SPRINT confirmed it? | Only then say proven |

## Where it stalls (observations from the vault, not rules)

- **Delivered, no saving.** 269 delivered use cases in the case groups have no recorded saving
  (Case Groups overview, 2026-11-04). The overview calls recording savings for them the cheapest way
  to strengthen a business case.
- **Weak basis everywhere.** Over the 36 case groups read, none has a savings basis above "Weak"
  (11 Weak, 15 Very weak, 10 None). Do not compare groups by recorded euros.
- **Savings not linked to a registered project.** An ODEC slide of 2024-02-29 states that 85 % of
  plants had no registered "CSP Project" in relation to digitalization for 2024. The deck uses
  "CSP" for a savings-tracking project; `od-context` defines CSP as the Common Solution Portfolio
  gate. ⟨Whether these are the same CSP — to confirm with the OD lead⟩ before the term is used in a
  record.
- **Yearly or not?** The ledger does not say whether a figure is yearly, and years differ across
  rows (case group note, section 4). Record the period for every figure you quote.
- **Fear of the number.** The same retrospective record behind `od-benefit-calculation` says plants
  lack confidence in use case evaluation. Offer a first computed number, not a blank field.

## Worked example (shape only, no figures)

Group CG-03 (Andon Board - Assembly), 27 delivered cases, none with a saving recorded. A key user
evaluating one delivered Andon board: (1) confirms use with the Gemba owner's dated statement
(tier 2); (2) writes the initial state without the board and the action it now triggers; (3) asks
whether a baseline exists for the loss the board is meant to cut (for example waiting time between
a stop and a reaction) and records ⟨baseline not recorded⟩ if not; (4) drafts one row with
rationale and methodology line using inputs the plant can name; (5) labels it `ESTIMATION` until
the baseline exists; (6) names the SPRINT link as the next step. The record shows adoption
confirmed and saving unproven, which is an honest and useful outcome.
