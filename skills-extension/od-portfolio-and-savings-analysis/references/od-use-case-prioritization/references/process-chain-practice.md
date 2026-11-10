---
type: Skill Reference
title: Process chain practice
description: How ranking is run at step 24 of the AI-driven chain - planning states, an explicit ordering rule, cluster-first ranking, dependency and foundation-first logic, value tiers and grounding tags, kill and defer outcomes, handoff and agent operating notes.
resource: ../procedure.md
status: draft
owner: human:jakob.gabriel
tags: [use-case-support-service, practice, prioritization, process-chain]
derived_from:
  - Operations Digitalization slide decks (priorities, planning, strategy, business-case and gap-analysis decks), abstracted into process guidance; no figures.
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Process-chain practice - prioritization (step 24)

Adds to `SKILL.md` and `ranking-criteria.md`; weighted-score mechanics stay in `od-portfolio-and-savings-analysis`.
`PROPOSAL` marks synthesis that no deck states.

## Where it sits

Lane 2 step **24 Business case and rank** (proposed skill on that step), after `od-use-case-solution-evaluation`
and with `od-benefit-calculation`; feeds step 25 (`od-decision-routing`, `od-investment-input`). It receives
defined, evaluated candidates and hands a ranked list with an unscored bucket.

## 1 · Method in practice

1. **Admit and group.** Gates first (`ranking-criteria.md`, section 1). Then group candidates by process or
   capability cluster (for example performance control, energy efficiency, automated versus manual process or
   product measurement); rank clusters, then use cases inside them.
2. **State scaling as demand, not as proof.** Express scaling as "recorded: use cases in plants" and "applies to
   every machine class with connectivity". A recorded count is demand; it is not a proven saving.
3. **Check for a validated prototype.** Two states are planned separately: a validated prototype exists, and a
   container- or template-based application that can scale still has to be built. Name which state each
   candidate is in.
4. **Record the planning state.** Each iteration gets a numbered planning state with its trigger: initial state
   after analysis of the list; iteration on technical inputs; iteration on the latest workshops; iteration on the
   latest plant priority. The state number, the trigger and the baseline file name belong on the record.
5. **Priority per process** can be written high / medium / low with a reason; lower the priority when
   infrastructure (cabling, terminals, a quality app) must come first, because the time frame is longer while
   other measures have direct impact.
6. **Foundation first, analytics last.** Rank by return **and** by dependency: platform and standards first,
   enablers (training) next, risk and compliance, and analytics last because it only proves benefit once the
   others exist. Make dependency an explicit column in the ranking record (`PROPOSAL`).
7. **Show the dependency chain per candidate:** process values depend on equipment integration and bus rollout;
   maintenance data on the maintenance system and its availability; quality data on the quality-app rollout.
8. **Use the two ranking views OD has** (`ranking-criteria.md`, section 4): urgency and importance, and value and
   risk. The technology-versus-business-value matrix has no published construction (`how to generate?` is open);
   do not invent one.

## 2 · Decision rules

- **Ordering rule, stated explicitly.** Savings first (value, ROI); generalization potential and effort are
  secondary criteria; dependency order (foundations before what depends on them) is the tie-breaker. Write the
  order used into the record header and do not mix orders inside one list.
- **Wave allocation.** Eligibility follows request order; central capacity goes first to first-mover plants that
  are staffed. Write the plant tier next to the queue position (tiers: `od-use-case-intake-triage`).
- **Three-way bucket as sort key:** just do, go forward, lead change. Just do is cheap and needs no new
  development; go forward names its enabler; lead change is exploratory.
- **Maturity sanity check for AI items.** Do not rank AI use cases above basic data-model and reporting work in
  a plant that has not reached reporting.
- **Cheapest test.** Build low-risk high-value; proof of concept where both are high; do not test or build
  low-value high-risk. Estimated value per use case decays as the best ones are done first.
- **Kill, cancel, defer are recorded outcomes** with a reason (no data foundation, insufficient savings, another
  party already collects the data). A low-saving item is cleaned from the list, but may stay as a scaling item
  if it is cheap to scale (`PROPOSAL`).
- **Scaling test per top use case:** three lists: where it saved, where it was deployed without savings, where it
  still has potential. A scaled-out use case with deployments but no savings is "to be evaluated"
  until investigated, not "no potential"; the algorithm may flag it but must not decide it.
- **Value tiers are never summed.** Keep a small **banked floor** that is sourced today, a **potential** envelope
  that is top-down, and **de-banked** items that rest on a crucial unknown (sensitivity only). Tag every figure:
  `[input]` stated by a source, `[assumption]` our estimate, `[market]` standard value, `[unknown]` crucial
  missing input we refuse to fake. An untagged figure does not leave the department. Report evidence coverage per
  cluster (full / partial / thin) and flag targets that lean on thin coverage.
- **Look for the splitting variable before averaging.** If one variable (for example who owns the source code of
  machine programs in-house) splits the estate into two operating models, state the baseline per group; a single
  average hides both. Re-scope a target to the addressable slice, not total effort.
- **Low change counts at a locked site mean suppressed demand,** not stability.
- **State the staffing assumption** beside every projection (central staffing only versus central plus dedicated
  plant key users), and record the **KPI basis with its date**: counts against a threshold assume the past
  year's system landscape and break after data-platform centralisation.
- **Customer-driven AI packages:** cost is built bottom-up per plant and divided across participating plants;
  flag items "on risk budget" (`<to confirm>` the rule for who carries risk).
- **Compliance or security items** are a risk and compliance programme, not a classic return case; say so.

## 3 · Handoff contract

**Receives:** from `od-use-case-definition` the demand rows; from `od-use-case-solution-evaluation` the verdict
and score; from `od-benefit-calculation` the savings rows with basis label and reliability; from
`od-data-availability-check` the readiness verdict.

**Hands on:** the ranking table with columns cluster, use case, bucket, scaling estimate (recorded, as demand),
prototype state, dependency (with owner), evidence per cell, planning state and trigger, plant tier, weights used;
the **unscored bucket** next to it; disagreement recorded. To `od-benefit-calculation` for uncosted top items; to
`od-decision-routing` / `od-investment-input` for money; to `od-use-case-standardization` for standard
candidates; to `od-portfolio-and-savings-analysis` for portfolio review.

## 4 · Pitfalls and lessons

- Recorded demand used as an impact proxy.
- Impact estimation not in place, then announced as mandatory: ask for it at definition.
- A savings figure from a plant describing effects only qualitatively: capture figures through existing lists
  (machine list with controller type and code status, OEE and maintenance extracts) with selection fields, not
  free text.
- A funding window or deadline drives a calendar: list it as a constraint, not as value.
- A pipeline can run empty if savings estimates are missing: add a potential-estimation attribute with an own-
  judgement fallback, labelled.
- Reported savings lag implemented work; delivered count can be on target while savings look missed.

## 5 · Questions to ask / definition of done

Which cluster; recorded demand and where; prototype validated or not; what must exist first and who owns it;
which tier is each figure; which planning state is this and why was it re-run; who disagrees and why.
Done (adds to `SKILL.md`): ordering rule and planning state on the record; dependency column filled; figures
tagged; unscored bucket present; staffing assumption and KPI basis dated.

## 6 · AI agent operating notes

- **Can do:** build the ranking table with the columns above and cite evidence per cell; compute the three-list
  matrix (saved / deployed without savings / potential) from the use-case list and savings ledger; flag blank
  reliability; draft calculation rows and flag missing inputs; put baseline-less items in the unscored bucket.
- **Must not:** decide "no potential", add tracked and proven money into one number, or choose weights.
- **Required inputs:** use-case list, savings ledger, evaluation verdicts, tier list, read dates.
- **Human gates:** weights and ordering rule (OD lead with Plant ME); assumptions and ranking sign-off;
  plant controlling accepts baseline and factor.
- **Evidence to cite:** list row, ledger row, library entry, evaluation score, planning-state file.
- **Hand over:** the table and the unscored bucket to the skills in section 3.
