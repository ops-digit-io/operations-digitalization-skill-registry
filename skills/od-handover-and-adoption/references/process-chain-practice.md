---
type: Skill Reference
title: Process chain practice
description: How handover and adoption (steps 26 and 3a6) is run in the AI-driven chain - deployed is not used, the pre-go-live checklist from rollout lessons, the operations-concept gate, the pitfalls of handing over a dashboard or data product, the use-case exchange with OPEX, and what an agent may draft. Pattern only, no figures.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [all, practice, adoption, process-chain, draft]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Process-chain practice

Distilled from the Operations Digitalization slide decks, abstracted into process guidance. No company figures. `PROPOSAL`
marks a synthesis; `<...>` is unknown. It adds to [`adkar-diagnostic.md`](adkar-diagnostic.md) and
[`evidence-of-adoption.md`](evidence-of-adoption.md).

## 1. Method in practice

**Deployed is not used; adoption is a standard operating procedure.** Adoption means the use case is integrated into a
standard operating procedure with dashboards and escalation flows, usually a recurring shop-floor meeting. Name that ritual
(who opens it, when, which action follows) before the handover is accepted. Pair the digital use case with the plant's own
lean method and standard process so the data leads to follow-up.

**Use-case exchange with OPEX** (a recurring call with OPEX, engineering, OD and the plant): present a small number of use
cases per call, a few minutes each, with scope and potential. Homework per presented item for OPEX and the plant: what is the
defined working procedure with this artefact, is there an estimated impact, and if not, what holds you back? Next call: the
impact is presented. Library fields to capture per item: presented, potential defined, standard procedure defined, impact
estimated, action for impact measurement, improvement project initiated (with link). Handover to OPEX per item: awareness,
evaluation and feedback, improvement.

**"Can / cannot" statement.** Give the plant a sentence of what the use case can do (explain equipment issues, derive
actions, notify immediately) and what it cannot (recommend solutions or fix them). Add "how can you use this in your daily
work", anchored on an example the plant already runs.

**Integration to use-case support.** After an integration workshop, hand the machines over with the known process flow, the
signal list and the first datasets, so use-case support does not re-ask.

**Dashboard-to-paper reconciliation** before acceptance (see `od-impact-evaluation`).

## 2. Decision rules

### Pre-go-live checklist (from rollout lessons)
Block the go-live, or record it as a named risk with an owner, if any of these is true:
- Old and new process will run in parallel because nobody trusts the new one, and **nobody is assigned to switch the old one
  off** (set an end date for any parallel run).
- The rollout team is unstable, or responsibilities in the use phase are unassigned (no shop-floor IT role, no key user for the
  business application).
- No operations concept: no named operations owner, no service level, no support level, no incident and change route. A tool
  without one is a **service gap**; hold the rollout (`od-decision-routing`).
- Interface faults with neighbouring systems are known and unresolved; the vendor has no round-the-clock service for a
  production-critical system and no emergency strategy exists.
- Runtime licences are bound to a machine and the key will not travel with a migrated server.
- Moving data to a new central environment changes every workflow and connection at every location; the plan does not say so.
- Dashboards were built per plant and not harmonised: a standardisation debt that will resurface at rollout.

### Operating model to hand over to
First-level local key user; business-area key user (fit and gap, budget, resources); central key user (demand, priority,
acceptance of updates); governance board (templates, new proposals); divisional engineering (consultancy, supplier liaison);
service owner or application management (incident, change, problem); local IT (servers, firewall, backup, patches). Managed
applications get central support; local solutions get none. Regular user revalidation is a per-plant process.

### Handing over a dashboard or data product between organisations
Accept the handover only if all of these exist:
1. The transformation (ETL) flow is documented, with its entry points, and a runbook "in case of trouble".
2. One owned workspace, not scattered ones.
3. Access management under the receiving side's control.
4. A named successor; the only technical key user leaving within weeks of the announcement is the typical failure.
5. A requirements list (one time) plus a **continuous requirements funnel**: collect always, evaluate and improve periodically,
   each entry with functional description, value add and success criteria for review.
6. An operations and run description. Lab devices with dongle-bound software: check licence and hardware constraints in the
   data-availability step.

Typical failures when these are missing: stakeholders do not know the underlying transformation, data quality is poor because
acquisition was unstructured, nobody owns the run.

## 3. Handoff contract

| Receives (from) | Hands on (to) |
|---|---|
| Acceptance protocol (`od-acceptance-test`), training checklist (`od-rollout-training`) | Handover protocol with ritual, data path to the machine, named plant owner, tier of evidence |
| Iterated tag list, process description, refined requirements, reference dashboard (`od-analytics-asset-build`) | Utilisation expectation and requirements funnel to the plant; utilisation read-back to `od-scorecard-reporting` |
| Sprint close inputs: baseline, forecast, project id | `od-impact-evaluation` (savings-forecast gate) |
| Service concept and operations owner (`od-decision-routing`) | Run description and escalation route |

## 4. Pitfalls and lessons

- Plant scepticism at the start ("basically no trust in digitalisation projects"): acceptance grows by raising awareness step
  by step and connecting more machines; low trust in an existing integration is expensive to regain, so stabilise before
  rolling more use cases onto it.
- Human-dependent automation caps what a dashboard can show; check organisational loss before technology.
- Delivered use cases without any measurement of utilisation or saving are not done.
- Gap-analysis causes (condensed): no savings-calculation standard, weak requirements management, no systematic follow-up and
  escalation, scattered infrastructure, unclear OD / IT / plant roles, approvals and purchasing slower than project timelines,
  no incident management for operational systems.
- "Ever sold a rocket to someone who can't fly it": rolling out without enabling capacity.

## 5. Questions to ask / definition of done

- Who opens it, when, and what do they do next? What happens on the day it is silent? Who is the successor? Who switches the
  old process off, and when?
- Done when: the checklist is clean or its open items have owners; the three-question test passes without the builder; the
  utilisation ritual is named; the evidence tier is stated; nothing is recorded stronger than the evidence.

## 6. AI agent operating notes

- **Can do:** compare the handover package with the list above and report gaps (`PROPOSAL`: a handover-readiness checker);
  keep the library fields (presented, standard procedure, impact estimate, impact check) current from call notes and chase open
  homework; draft the can / cannot statement; monitor utilisation.
- **Required inputs:** the package, the acceptance protocol, call notes, usage records.
- **Human gate:** the plant owner confirms adoption and the standard procedure; an agent never writes "adopted".
- **Evidence to cite:** package item, call note date, usage record and tier.
- **Hands over:** the filled protocol to the plant owner and `od-scorecard-reporting`; gaps to the named owners.
