---
type: Skill Reference
title: Process chain practice
description: How acceptance is run at chain steps 3a5 and 3b6 and as the close of a use-case sprint - reconciliation against the paper process, utilization table, parallel run and switch-off, pre-go-live adoption checklist, handoffs and agent notes.
resource: ../SKILL.md
status: draft
tags: [information-integration-service, practice, process-chain, draft]
---
# Process-chain practice - acceptance as the step that proves use, not delivery

Derived from the Operations Digitalization slide decks (sprint reviews, integration workshops, MES and energy-monitoring lessons,
gap analysis), abstracted into process guidance. No figures. `PROPOSAL` = synthesis not stated in a deck; `<...>` = unknown.
The test structure, sign-off authority and rework loops stay in the neighbouring references.

## Where it sits in the chain

3a5 (with `deploy-appstore`), 3b6 (acceptance and Cyber Security, live on the data platform), and as the closing check of a
use-case sprint (lane 2 step 23 into 26). Downstream: `deploy-handover`.

## 1 Method in practice

### Acceptance has two halves

1. **The data is right** (the existing FAT, SAT, SIT path: signal, connector, data path, asset).
2. **It will be used** (the half the decks show is usually missing): a deployed use case with no reported saving is the typical
   failure, so acceptance also checks that a named ritual of use exists.

### Dashboard-to-paper reconciliation

Accept a dashboard only after reconciling it with the paper process the plant already trusts. Run one deep dive with production
(production records against dashboard downtime) and one with engineering (cycle-time records); explain every difference (breaks,
shift changes, tolerance not yet applied) before settling signal selection and categories. Check for organisational loss before
proposing technology: human-dependent automation (for example a feeder that works one piece at a time) caps what a dashboard can
show, and the fix may be organisational.

### Parallel run and switch-off

- Run old and new in parallel for a limited, stated period to check. Match the reading date to the period it is compared with
  (for example the billing period for energy readings). Add plausibility checks and a manual correction route.
- **Name who stops the old process.** Lessons from MES rollouts: paper and system ran side by side because nobody trusted the new
  process and no one was assigned to switch the old one off. The protocol's section 6 must name the switch-off owner and date.
- Failure of acceptance means "back to rework", not "retry quietly" (existing rule); here, also record which half failed.

### Sprint-end definition of done (use-case sprint)

Dashboards live; flows and dashboards documented; a scalability statement; open topics list; impact of IT issues stated;
flows kept in version control (redeploying a flow-runtime container lost production flow configuration once). Add the
**savings-forecast completeness gate**: a forecast and a registered plant savings project exist before the sprint closes;
otherwise the sprint is "implemented, no forecast". Notification channels and data historization are IT changes; check they were
requested early or the alert use case stalls at acceptance.

### Utilization table (start it at acceptance)

Columns: use-case name (dashboard, app or analytics workflow); who uses it (team); related process or meeting (for example the
daily shop-floor meeting); utilization method in one to three sentences, including the initial state without digital support;
utilization rate (daily, weekly, monthly, on demand, never); impact or potential (low, medium, high); relevant to plant
management (yes or no). Review it with Production and the continuous-improvement function after go-live. The adoption test is
"integrated into a standard operating procedure with dashboards and escalation flows", not "dashboard live".

## 2 Decision rules

| Situation | Rule |
|---|---|
| Dashboard disagrees with the paper record | Do not pass; explain the difference first |
| No named ritual of use and no action owner | Build smell; accept the data half only, mark the use half open |
| Old process still running at handover | Pass blocked on §6 until a switch-off owner and date are named |
| Cyber Security sign-off missing | Hold go-live and any test that needs the live connection (`deploy-cybersec`, a parallel track); attach the recorded answer as evidence once given |
| Deployed use case with no reported saving | "To be evaluated until investigated", never "no potential" written by an agent (only the OD lead with the plant owner may decide that); do not pass as value delivered |
| Handover from another organisation | Accept only with documented transformation, owned workspace, access control, a named successor |

## 3 Handoff contract

| Direction | Skill | Content |
|---|---|---|
| Receive | `funnel-requirements` / `mi-signals` | Signals, tolerances, data path, acceptance criteria written before the build |
| Receive | `deploy-cybersec` | Recorded answer with scope and conditions |
| Receive | `deploy-appstore` | Deployment package, rollback owner |
| Hand on | `deploy-handover` | §6 filled: output asset, business process, utilization expectation, data path, named plant owner, utilization table started |
| Hand on | `metrics-scorecard` | Readiness moved with evidence; acceptance and rework outcome |

## 4 Pre-go-live adoption checklist (from MES and monitoring lessons)

- Is the rollout team stable (roles not tied to people about to leave)?
- Is a first-level local key user, a business-area key user and a use-phase owner named (shop-floor IT, ERP key user)?
- Is the interface between ERP and the shop-floor system tested, and is vendor reaction time and out-of-hours coverage known?
- Is an emergency strategy defined for when the system is down?
- Is the old process scheduled to stop, and by whom?
- Are training and vendor support planned (the tool is complex)?
- Is the data in the backup routine and the documentation complete?

## 5 Pitfalls and lessons

- A demonstration is not acceptance (existing rule); the plant owner has to use it in a real shift.
- The signal that proves a pass is a value in the real shift, not a green tile.
- Requirements change weekly and stakeholders cannot state them: schedule an explicit requirements-iteration loop after first
  delivery; dashboards are "not 100 percent right at first delivery".
- Dashboards built per plant and not harmonised create standardisation debt; note it as a finding.
- Large numbers of dashboards are a result of good integration, not proof of value.

## 6 Questions to ask and definition of done

Questions: which real shift will use it, who opens it and when, which action follows, what is the initial state without it, what
makes people use it, who stops the old process?

Done = the existing definition of done, plus: reconciliation against the paper record documented, utilization table started with
a named ritual of use, switch-off owner named, savings-forecast and registered project present for a sprint close.

## 7 AI agent operating notes

- **Can do**: draft the protocol before the build, run the reconciliation arithmetic when both records are supplied, draft the
  utilization table rows, check the sprint-end definition and the pre-go-live checklist, flag "implemented, no forecast".
  `PROPOSAL`: derive utilization rows from dashboard usage logs (the decks do not show the data source).
- **Inputs required**: signal standard, requirement list, both records for reconciliation, deployment package.
- **Evidence to cite**: protocol item ids, record sources and dates, the log used.
- **Human gate**: sign-off by a named human on the receiving side; the plant owner confirms adoption; an agent reports results, it
  never approves.
- **Handover**: protocol plus §6 to `deploy-handover`.
