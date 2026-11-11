---
type: Skill Reference
title: Savings proof path
description: The path a use case saving takes from a workshop pre-evaluation to a SPRINT-proven row as OD's own decks describe it, the firmness label at each step, and where it stalls.
resource: ../procedure.md
status: draft
tags: [use-case-support-service, practice]
---
# Savings proof path

Read with `bc-build`, which owns how a saving row is built. This file adds the
*path* a row travels and how to evaluate where a given row stands. Sources are OD workshop decks
(Use Case Creation Process; Workshop Summary), the department's saving
ledger as described in `bc-build`, and the knowledge base's case groups.
The decks are presentations, not rule documents; re-open them before quoting wording.

## The steps, as the decks describe them

| # | Step | What the decks say | Firmness label to record |
|---|---|---|---|
| 1 | **Pre-evaluation in the savings list** | A template for savings pre-evaluation exists with examples. Savings are collected in the Savings List initially; every saving must be linked to a concrete use case in the plant's use case list; cumulated savings per use case are entered in the list (older and newer decks) | Pre-evaluation. Not a ledger claim yet |
| 2 | **Calculated, not guessed** | Later deck: "The Savings shall be calculated, only in some minor cases they can be estimated". Older deck: the figure in the list "can also be a first realistic estimation, because the Savings must be reported within the SPRINT" | `CALCULATION` if a methodology line exists, otherwise `ESTIMATION` (labels from `bc-build`) |
| 3 | **Linked to a SPRINT project** | Later deck: savings "are linked to the Use Case and finally to the Sprint Project that will be created"; the pre-evaluation "can in the end be linked with the Sprint project" | Linked, not proven |
| 4 | **Use in the process** | Utilization process slide: connect relevant machines (high runners, troublemakers); collect and select parameters; analyse parts produced, utilization rate, downtimes, parameter specification; analyse root cause (the slide names commonly known methods such as A3); "create and calculate cost saving project and report savings"; eliminate the deviations | Evidence that the mechanism ran |
| 5 | **SPRINT portfolio review** | `dept-context` and `bc-build`: only SPRINT turns a tracked saving into a proven one | Proven. Count proven rows and euros live on the ledger and quote the read date |

Calculation categories named on the "Use Case Calculation Methods" slide: cycle time
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
| Is there a baseline measured before the use case (scrap, downtime, reporting hours, parts per tool life)? | Record "baseline not recorded" and name who can measure it. A case group's derivation sheet can list the baseline and KPI as "Not recorded" for the whole group (seen for an Andon Board group) |
| Does the methodology line show a formula with real inputs that a stranger can recompute? | Label `ESTIMATION`; do not upgrade. A `CALCULATION` without methodology is an estimation wearing the wrong label (`bc-build`) |
| Did the figure come from OD's calculator, or from the plant alone? | Treat a plant-only figure with no formula as an estimation candidate. The department's own record: plants asked to self-originate a number tended to produce none; the working approach is OD computing a first number the plant reacts to (`bc-build`, `references/review-checklist.md`) |
| Is the dependency recorded with its owner (`ECR APPROVAL`, `MACHINE INTEGRATION`, `PLANT` ...)? | Record it on the row; a gated saving stays visible instead of being dropped |
| Is it linked to a SPRINT project? | Prepare it for the SPRINT review: row, rationale, methodology, baseline, evidence of use |
| Has SPRINT confirmed it? | Only then say proven |

## Where it stalls (observations from the knowledge base, not rules)

- **Delivered, no saving.** Many delivered use cases in the case groups have no recorded saving. The Case
  Groups overview calls recording savings for them the cheapest way to strengthen a business case. Count them
  live in the overview before quoting.
- **Weak basis everywhere.** The case groups carry a savings-basis grade (Weak, Very weak, None, ...). Read
  the grade per group in the live overview; do not compare groups by recorded euros.
- **Savings not linked to a registered project.** A historical ODEC slide stated that most plants had no registered
  "CSP Project" in relation to digitalization for the year. The deck uses "CSP" for a savings-tracking
  project; `dept-context` defines CSP as the Common Solution Portfolio gate. ⟨Whether these are the same CSP
  — to confirm with the OD lead⟩ before the term is used in a record.
- **Yearly or not?** The ledger does not say whether a figure is yearly, and years differ across
  rows (case group note, section 4). Record the period for every figure you quote.
- **Fear of the number.** The same retrospective record behind `bc-build` says plants
  lack confidence in use case evaluation. Offer a first computed number, not a blank field.

## Worked example (illustrative; shape only, no figures)

Case group ⟨group name⟩ with delivered cases and no saving recorded. A key user
evaluating one delivered Andon board: (1) confirms use with the Gemba owner's dated statement
(tier 2); (2) writes the initial state without the board and the action it now triggers; (3) asks
whether a baseline exists for the loss the board is meant to cut (for example waiting time between
a stop and a reaction) and records ⟨baseline not recorded⟩ if not; (4) drafts one row with
rationale and methodology line using inputs the plant can name; (5) labels it `ESTIMATION` until
the baseline exists; (6) names the SPRINT link as the next step. The record shows adoption
confirmed and saving unproven, which is an honest and useful outcome.
