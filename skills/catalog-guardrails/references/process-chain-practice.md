---
type: Skill Reference
title: Process chain practice
description: Method, decision rules, handoff contract, pitfalls and agent notes for the go-live self-check, abstracted from the Operations Digitalization slide decks - reconciling a screen with the paper process, naming the utilization ritual and action owner, operations concept, switching off the old process. Process-level guardrail candidates, no figures.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [all, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Process-chain practice - going live without OD labour

Deck-derived practice for steps 1a3 and 1b4 (and the same checks at the end of step 26). The numbered guardrails G1 to G19 stay in `SKILL.md` and the other references.
This file adds **process-level candidates**, labelled P1 to P7 so they do not collide with the G numbers. All are `PROPOSAL`: the decks support the lesson, the OD lead decides whether it blocks or warns.

## 1. Method in practice

1. The plant owner (a role) opens the match record from `catalog-usecase` and, on branch 1b, the system match record.
2. Run G1 to G7, then the P-candidates below when the plant has built or copied the screen itself.
3. Do one **deep dive against the paper process** before declaring the screen live: compare the screen with the plant's production records (and, for cycle time, the engineering records), explain every difference
   (breaks, shift changes, tolerance not yet applied), then settle signal selection and categories. Run one deep dive with production and one with engineering.
4. Name the **utilization ritual** in the record: who opens the screen, in which meeting, which action follows and who owns it. Write the expectation into the record before go-live.
5. The plant decides to go live. The skill never does.

## 2. Process-level guardrail candidates

| # | Candidate | Lesson behind it | Suggested setting |
|---|---|---|---|
| P1 | **Reconciled with the paper process** - differences between screen and record are explained, not ignored | dashboards were accepted only after reconciliation; unexplained downtime differences destroy trust | block |
| P2 | **Utilization ritual named** - who opens it, when, which action follows | deployment without a defined routine produced no saving; the successful plants defined the utilization process with production and the operational-excellence function first | block |
| P3 | **Action owner named** - a screen with no owner for the action it should trigger | visibility alone created no saving; savings appeared where a screen drove a defined action | warn |
| P4 | **Operations concept present** - business owner, IT owner, service concept, roles, change and risk process | tools without an operations concept were the most repeated rollout barrier | block for a new system; warn for a catalogued template on existing systems |
| P5 | **Old process has an owner for switching it off** | parallel running of old and new because nobody trusted the new process and nobody was assigned to stop the old one | block |
| P6 | **IT changes requested early** - notification channel, data historization, reverse proxy, user access | alert use cases stalled on late change requests; architecture changes mid-sprint cost weeks | warn |
| P7 | **Flows under version control** - redeploying the flow runtime lost the production flow configuration | keep flows versioned and check the redeploy impact | warn |

Two further checks come from the same lessons and belong in the G-set once the OD lead agrees: **personal-data and worker-performance question answered** (does the screen process personal data or measure workers' performance; is the works council or data-protection notification needed - notification content: purpose, functions, data fields, access rules, retention, council category),
and **savings forecast and registered project present** (a use case implemented without forecast or registered savings project is invisible to the savings ledger; the forecast is checked before the sprint closes). Both `PROPOSAL`.

## 3. Decision rules

- **Go-live = all G1 to G7 passed, evidence cited.** "Yes" without evidence counts as not checked.
- **Requirements still moving?** A first delivery is not fully right. Plan the requirements-iteration loop after first delivery; it is not a reason to withhold go-live and not a reason to let scope grow silently.
- **Change of look is not a guardrail topic.** Requests about fonts, colours and headlines are capacity burners: route by cost-saving impact and time-box them.
- **Failed guardrail routes back:** data to `od-data-availability-check`; footprint to `od-system-fit-check`; handover to `od-handover-and-adoption`; security to `od-cybersec-gate`. Say which.
- **Human-dependent automation caps what a screen can show** (for example a machine that works one item at a time without fast-forward during breaks). Check for organizational loss before proposing technology.

## 4. Handoff contract

| Receives | From |
|---|---|
| match record, system match record, data verdict, security status | `catalog-usecase`, `catalog-systems`, `od-data-availability-check` |
| deltas the plant recorded against the baseline | `od-analytics-asset-build` |

| Hands on | To |
|---|---|
| go-live check record with the final line "go-live decision: the plant's", utilization ritual, action owner, savings-forecast status | `od-handover-and-adoption`, `od-rollout-training` (1a3) |
| failed guardrail and its route | the skill named in section 3 |
| utilization expectation | `od-scorecard-reporting` (utilization is reported next to the count of deliveries) |

## 5. Pitfalls and lessons

- **Low trust is expensive to win back.** Where earlier integrations were not trusted, stabilize before putting more use cases on top.
- **Nobody trusts a number nobody can explain.** Unexplained differences to the paper record end adoption early.
- **Plant scepticism at the start is normal**; acceptance grew by raising awareness step by step and showing the first real use. Do not read early silence as agreement.
- **Missing training or enabling knowledge** at the plant makes a correct screen unusable.
- **Quality dashboards that do not depend on machine connectivity** (lab tests) run on another path owned by the local quality team; do not push them through the machine-integration checks.

## 6. Questions to ask and definition of done

Who opens it and when? What do they do when the number is red? Where does the number differ from the paper record and why? Who runs the tool when it breaks? Who switches the old way off? Is any personal data or worker-performance measure involved?

**Done:** record complete, every result has evidence, date and answerer; the P-candidates are answered or marked not applicable with a reason; the utilization expectation is written down.

## 7. AI agent operating notes

- **Can do:** draft the check record from the match records; run the evidence check ("Yes" without evidence becomes *not checked*); compare screen output with a paper-record extract the plant supplies and list the differences; check that no figure lacks a source and read date; list unanswered P-candidates.
- **Needs:** the two match records, the verdict of the data check, the plant owner's role, the paper-record extract.
- **Human gate:** the plant owner answers G1 to G7 and decides `PRODUCTIVE`; Cyber Security sign-off is human-only; the OD lead decides which candidate blocks.
- **Must cite:** evidence for each answer (verdict id, list row, dated statement), read dates.
- **Hands over:** the check record plus the list of failed guardrails and where each was routed.
