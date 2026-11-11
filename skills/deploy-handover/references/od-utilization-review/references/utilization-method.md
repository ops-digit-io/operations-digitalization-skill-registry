---
type: Skill Reference
title: Utilization method
description: The utilization table columns, the questions that find out what makes a use case utilized, the dashboard-without-action-owner smell, dashboard-to-paper reconciliation and the follow-up list.
resource: ../procedure.md
status: draft
tags: [use-case-support-service, practice]
---
# Utilization method

## 1 Method in practice

Run it as a short session with the plant owner, Production, OPEX and Engineering (the decks pair the review with the
lean routine; a review without those functions finds only what the builder already knows). Order: fill the table, ask
the questions, run the smells, assign verdicts, write the follow-up list. Revisit with the same people after a settling
period (`<months>` - not set in the sources). Two decks use the same loop for plants: connect high-runners and trouble-makers,
run the use cases, select parameters, analyse (parts, utilization, downtime), find the root cause with a known method (for example A3),
create and calculate a cost-saving project, eliminate deviations.

## 2 The table (columns as used in the decks)

| Column | Ask |
|---|---|
| Use case name | Dashboard, app or analytics workflow? |
| Site | Which plant or area (one row per site) |
| Who uses it | Which department or team |
| Related process / meeting | Which recurring routine (for example a daily Gemba, a process-improvement meeting) |
| Utilization method | 1-3 sentences, **including the initial state without digital support** |
| Utilization rate | Daily, weekly, monthly, on demand, never |
| Impact / potential | L / M / H |
| Plant-management relevant | Y / N |
| Link | Where it lives |
| Perceived value | Free text from the user (one deck variant of the table) |
| In use | Yes / No (same variant) |

Two deck variants of the table exist (one with utilization rate, impact and management relevance; one with link, frequency,
perceived value and in-use). The union above covers both; keep the plant's own variant if it already has one
(`<to confirm>` which is canonical).

## 3 "What makes it utilized?" - questions

1. Who opens it, when, in which meeting or routine? If it belongs to no moment, that is the finding.
2. Which action follows, and who owns that action?
3. What did people do before (paper, spreadsheet, nothing)? What is better now?
4. What would make people use it (access on tablet or at the line, a user list, a category list, training, a sponsor)?
5. Who attests the value - Production, OPEX, Manufacturing Engineering? Is there a named testimonial?
6. What can it do and what can it not (a short "can / cannot" statement helps adoption)?
7. Is a lean method paired with it (SMED, waste types, value-stream mapping, switch-off campaign) so the dashboard drives a follow-up?

## 4 Smells

- **Dashboard without action owner.** Visibility alone does not create savings; savings appeared where the dashboard drove a defined
  action. No action owner means no saving path: treat as a build defect, and send it back to definition (`funnel-use-case`).
- **No ritual of use.** Nobody can say who opens it and when.
- **Paper and system in parallel**, nobody assigned to stop the old process (`deploy-handover`).
- **Unassigned or unstable key user.**
- **Big count of views** (overview, per-equipment, process value, alert, andon) read as proof of value: it shows good integration only.
- **The deployer does not report**: unreported saving looks like non-utilized potential. Ask before concluding.

## 5 Reconcile with the paper record

Accept a dashboard only after it matches the paper process. Run one deep dive with Production (production records vs dashboard downtime)
and one with Engineering (cycle-time records). Explain each difference (breaks, shift changes, a tolerance not yet applied), then settle
signal selection and categories (for example a standard downtime reason list). The decks show this at an integration workshop; where
it sits as a formal acceptance step is open (`PROPOSAL`: also a check in `deploy-acceptance` and `catalog-usecase`).

## 6 Follow-up list

One line each: action, role (never a person name), due, how it will be checked. Typical items: name the ritual, assign
the action owner, fix access, standardize categories, train (`know-training`), re-evaluate after `<months>`, ask OPEX/ME for a
testimonial, register the saving or project, retire. A follow-up with no check date is not a follow-up.

## 7 Definition of done

Table filled for every live use case under review; each row has a verdict and a cited basis; each smell is answered; every no-saving
case has a decision (`no-saving-decision.md`); follow-up list dated and owned; plant owner has confirmed adoption or the gap is logged.
