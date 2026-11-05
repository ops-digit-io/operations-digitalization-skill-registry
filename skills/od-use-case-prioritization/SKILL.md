---
name: od-use-case-prioritization
description: >-
  Rank several competing candidate use cases for a plant or region into a recommended order, against the plant roadmap and strategic-plant scope, and write the ranking down as a prioritization record with the evidence behind each position. Uses OD's own criteria (saving potential, generalization potential, roadmap link, effort and dependencies) and keeps unscored use cases in a separate bucket. Use when more than one use case is waiting for the same capacity, after a definition workshop has collected demand, before a planning round or ODEC input, or when a plant asks which of its use cases OD should do first.
license: Internal — OESL MPEE Operations Digitalization. Not for external distribution.
allowed-tools: Read Grep Glob
metadata:
  id: od-use-case-prioritization
  tier: practice
  lane: use-case-support-service
  new_state_lane: Lane 2
  new_state_step: Business case and rank
  owner_role: human:jakob.gabriel
  authority_level: recommend
  status: draft
  sources_read: 2026-11-05
  requires: [od-context]
  composes: [od-use-case-intake-triage, od-use-case-definition, od-benefit-calculation, od-portfolio-and-savings-analysis, od-use-case-solution-evaluation, od-use-case-standardization, od-decision-routing, od-data-availability-check, od-investment-input, od-cybersec-gate, od-workshop-facilitation]
  derived_from:
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/OD_Skill_Map.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/00-core/05-intake.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/00-core/08-decision-rights.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/00-core/04-service-catalog.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/20-lanes/use-case-support-service/playbook.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/20-lanes/use-case-support-service/agent-brief.md
    - Work vault (Work-OpsDigit-Knowledge), Slide Index notes for 03-AMT_MI_Standard_Agenda_Use_Case_Workshop (collection of demand, Use Case Canvas urgency and importance, value and risk slide) and for 50-Use_Case_Planning (Use Case Priorities decks, planning states), read 2026-11-05
    - Work vault (Work-OpsDigit-Knowledge), Split Slides of 50-Use_Case_Planning 2025-03-10 UseCase_Priorities slides 2 to 7 (priority tiers and cluster table columns), read 2026-11-05
    - Work vault (Work-OpsDigit-Knowledge), Case Groups overview and CG-03 Andon Board - Assembly (rollout map, evidence gap, white space), read 2026-11-05
    - Work vault (Work-OpsDigit-Knowledge), ODEC Facts - Department KPIs and Roadmap Status (use case upvoting slides 2025), read 2026-11-05
    - Work vault (Work-OpsDigit-Knowledge), Graph/Business Cases notes (portfolio tier and score fields; Catalog Maturity Sprint UC-Y; Cycle Time Optimization), read 2026-11-05
    - Skill od-portfolio-and-savings-analysis, references/prioritization.md (weighted scoring and the unscoreable bucket)
    - Skill od-use-case-intake-triage and od-use-case-definition, admission rule and control points
  okf:
    type: Agent Skill
    title: Use case prioritization
    tags: [use-case-support-service, practice, prioritization]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Use case prioritization

Read `od-context` first. This skill turns "several use cases want the same capacity" into a
**recommended order with reasons**. It does not decide: prioritization and selection is a
*recommend* decision of the DBVE together with the Plant ME (Tandem, no approval, reversible,
"within plant roadmap scope" — `08-decision-rights.md`). Money is a different decision
(`od-decision-routing`, `od-investment-input`).

## When it applies

Trigger (plan UC-05): several candidate use cases compete. Typical moments: after a Definition
Workshop has collected demand (`od-workshop-facilitation`), at playbook step 4 ("prioritize by
value — savings / lead-time / cost avoidance"; control point "business case and priority agreed
with Plant ME"), before ODEC or roadmap input, or when a plant asks "what first?".

Definition of done: a ranked list per plant (or per region and category, see step 2) where every
position carries its criteria, its evidence strength and its open dependencies; unscored use
cases sit in a separate bucket; the Plant ME has seen the list; the record is filled
([`assets/prioritization-record.md`](assets/prioritization-record.md)).

## The references

| File | Use it for |
|---|---|
| [`references/ranking-criteria.md`](references/ranking-criteria.md) | Every criterion OD itself has used to rank, with the source of each, and what each one is not |
| [`references/evidence-baselines.md`](references/evidence-baselines.md) | How to read what the vault can say about a candidate before anyone is asked: case groups, rollout maps, savings basis, white space, upvoting (reading guide, no figures) |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | Chain practice for step 24: planning states, explicit ordering rule, foundation-first and dependency column, value tiers and grounding tags, kill/defer outcomes, handoff columns, agent notes |
| [`assets/prioritization-record.md`](assets/prioritization-record.md) | The output: candidate table, scoring sheet, unscored bucket, recommendation, sign-off |

Weighted-score mechanics are not repeated here; they live in
`od-portfolio-and-savings-analysis` (`references/prioritization.md`). This skill supplies the
inputs that skill's method scores, and the plant-facing record around it.

## Procedure

1. **Admit only what is admissible.** Run each candidate past `od-use-case-intake-triage`. No
   plant roadmap link or no nameable business case means it is not ranked; it goes back to the
   demand owner (`05-intake.md` "Explicitly refused"; playbook error path). Work outside the
   lean standardized footprint (for example a non-standard MES rollout short or mid term) is also
   refused there, not ranked.
2. **Fix the comparison set.** Rank only within one plant roadmap, or within one category and
   region. Do not put Europe, Americas and Asia on one axis (`od-portfolio-and-savings-analysis`,
   `references/regional-handling.md`) and do not mix a standard per-process use case with a
   one-plant non-standard one without saying so.
3. **Collect the minimum per candidate** from the use case record, not from memory: plant,
   capability and process group (`od-use-case-definition`), category (standard cross process,
   standard per process, non-standard, AI), stated objective, tracked savings with reliability
   label (`od-benefit-calculation`), dependencies with owner, machines and data readiness
   (`od-data-availability-check`).
4. **Look up the baseline** in [`references/evidence-baselines.md`](references/evidence-baselines.md):
   which case group the candidate belongs to, which plants already run it (read the group's rollout map), and how strong the
   savings basis of that group is. A strong precedent lowers effort; a group with no recorded
   savings is a gap in evidence, not a verdict on value.
5. **Score on the criteria** of [`references/ranking-criteria.md`](references/ranking-criteria.md).
   Use the weights OD agrees with the Plant ME for this round and write them into the record;
   ⟨default weights — none found in the sources; the OD lead and Plant ME set them⟩. State the
   ordering rule in the record header (workshop decks: generalization potential first, then saving
   potential; strategy decks stress savings; `<to confirm>` with the OD lead), number the planning
   state with its trigger, and add the dependency column.
6. **Check fit before you fix the order** for the top candidates: `od-use-case-solution-evaluation`
   (does the envisioned solution need capability nobody has?). If a machine connection is
   involved, flag the Cyber Security wait state (`od-cybersec-gate`) so the plan does not promise
   a date OD does not control.
7. **Separate the unscored.** A candidate with `UNKNOWN` priority or potential, or no value field,
   goes into the "unscored" bucket and is reported next to the list, never at its bottom
   (`od-portfolio-and-savings-analysis`).
8. **Write the recommendation and walk the Plant ME through it** (Tandem: both must agree on the
   plant-level order). Record agreement, and any use case the Plant ME wants moved, with the
   reason. Disagreement is recorded, not smoothed.
9. **Hand over**: agreed top candidates go to `od-benefit-calculation` (if not yet costed) and then
   to integration (`od-information-integration-service`); standard candidates are checked against
   `od-use-case-standardization`. Money needs go to `od-investment-input`.

## Output

[`assets/prioritization-record.md`](assets/prioritization-record.md), one per plant round. It feeds
the planning inputs the ODEC calls collect and the portfolio reviews in
`od-portfolio-and-savings-analysis`.

## What is still open

- ⟨Formal prioritisation rule⟩ — `05-intake.md` itself marks it "to confirm". Supplier: OD lead.
- ⟨Weights between value, generalization and effort⟩ — not written anywhere read. Supplier: OD
  lead with Plant ME.
- ⟨How capacity is counted⟩ — the service catalogue names the DBVE roles as the capacity limit for the
  lane, but gives no unit per use case. Supplier: OD lead.
- ⟨Lane lead time⟩ — "to confirm" in the service catalogue, so "overdue" cannot be flagged.

## Do not

- Do not rank a use case that fails intake; return it with the written reason.
- Do not read a blank value field as low value, and do not default it to a midpoint.
- Do not add or compare tracked and proven euros as one number (`od-benefit-calculation`).
- Do not invent weights, scores or savings; mark them ⟨to be collected⟩ and name who collects.
- Do not commit investment, equipment integration or an external connection; those are other
  decisions with other authority levels (`08-decision-rights.md`).
- Do not read a recorded-demand count or a rollout count as proven saving; both are demand or reach.
- Do not decide "no potential" for a scaled use case that has no tracked saving: it is "further
  investigation necessary".
- Do not treat white space in a case group as demand. It means "has no member here", nothing more.
