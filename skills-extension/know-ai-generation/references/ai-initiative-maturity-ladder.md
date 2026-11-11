---
type: Skill Reference
title: AI initiative maturity ladder
description: The evidence ladder for AI and agentic initiatives (idea, drafted case, prototype or PoC, validated pilot, productive, proven), what each rung may claim, the rule that PoC claims are not savings, and the failure modes the strategic business cases name. Not the data-maturity ladder of ai-governance. Pattern only, no values.
resource: ../SKILL.md
status: draft
tags: [all, practice, ai]
---
# AI initiative maturity ladder

Source: knowledge base `Graph/Keynote Initiatives` (initiatives with a "(PoC)" marker or an agentic proof of concept and their archive
evidence), `Graph/Keynote Clusters` and `Graph/Business Cases` (key risk, validation plan and sensitivity fields). AI-curated and
not reviewed by a human. Not to be confused with the **data-maturity** ladder in `ai-governance.md` section 1 (data anarchy to data
economy), which says whether a plant is ready for AI at all. This ladder says **how much an initiative has proved**.

## The ladder

| Rung | Name | What exists | What it may claim | What it may not claim |
|---|---|---|---|---|
| 0 | Idea | A named initiative or keynote entry; sometimes no business case linked | A direction and an owner question | Any value |
| 1 | Drafted case | A business case with authors' inputs: value anchors, key risk, validation plan | A range with its arithmetic shown, as an **estimate** | A saving; the knowledge base says the case-study figures are not verified against the reference library |
| 2 | Prototype / PoC | A running prototype or pilot-scale tool, often on one plant or a sample; "prompt-to-prototype" is a demo | That the method works on the sample; a possible lead time or effort effect, stated with its test conditions | A saving. A PoC result is a **claim**, not a recorded saving |
| 3 | Validated pilot | The pilot met the pass criterion that was written **before** it ran (recognition rate by domain leads, lead time and false-positive limit, latency target) at plants chosen to include a sceptical and a complex one | That the method works under plant conditions; adoption is plausible | A fleet-wide saving; scaling needs the organisation, not only the model |
| 4 | Productive | Used in daily operation at one or more plants with utilization recorded; container app or configurable service | A deployment; utilization | Value, unless a baseline and a measured effect exist |
| 5 | Proven | A baseline was measured before, the effect after, an owner confirmed it; the saving is booked with its reliability class | A **proven** saving, labelled proven | Transfer to another plant without a second validation |

Climbing a rung needs evidence of that rung, not a decision. Name the rung in every record; an initiative has one rung, not
"mostly 3".

## The rule: PoC claims are not savings

1. A PoC or pilot figure goes into the portfolio as **tracked at best, "estimate"**, never as proven (see
   `bc-portfolio`, `references/rollup-method.md`). Tracked and proven are never added.
2. A **target** is not a **result**. An initiative one-pager may state targets (share of tasks automated, response-time cut, number
   of workflows, adoption level). Quote them as targets with the page date. If the results slide is empty, there is no result.
3. A **range from a business case** is an author's input. Quote it as "business case estimate by `<author role>`, `<date>`" and
   not as expected savings.
4. **External benefit** (a case study of another firm) is context, not our result. Mark it so.
5. **Enabling value** is booked in the dependent case, not in the enabler (to avoid double counting). A PoC for an enabler (for
   example a label corpus) has a direct value and a separate enabling value; report them apart.
6. An **agentic or GenAI PoC** carries a different benefit unit: time freed, decision quality, knowledge retention. State the
   measure and the baseline; do not convert hours into euros without a recorded baseline and owner.
7. Before a PoC result is reported as a saving, hand it to `deploy-handover` and `bc-build`.

## What the pilot design looks like (pattern)

Each strong business case states, before the work: **the single falsifiable assumption**, a time-boxed MVP on a small number of
plants, a **pass criterion** a domain lead can judge, and what happens if it fails. Observed shapes:

- recognition test: domain leads name a stated share of the top mined patterns as recognisable failure modes, within a fixed
  period, and map a share of them to past incidents; if they cannot, the label corpus is unusable downstream;
- alert quality test: lead time, recall on labelled events and a false-positive ceiling per asset and month;
- load test: throughput at the full machine reach with a latency ceiling;
- adoption test: usage by the intended roles, not accuracy alone.

Pick pilot plants as **one willing, one sceptical, one complex**; a pilot only at the willing plant proves the least.

## Failure modes the cases name

| Failure mode | Seen in | Early signal | Mitigation named |
|---|---|---|---|
| Adoption collapses after false alerts | predictive maintenance, predictive quality | maintenance ignores alerts within weeks | agree the false-positive ceiling first; start on critical assets |
| Labels are missing or too costly | predictive quality, vision quality control | every defect class needs a large hand-labelled set | active learning, synthetic data, self-supervised pre-training; build the labelling pipeline before the model |
| State rules do not transfer between plants | state labelling | the same event means something else on another site | validate at more than one plant before claiming 1:N |
| Source data is heterogeneous | production risk scoring | pre-work to structure documents dominates | defer behind a data-engineering step |
| Inferred specs need heavy manual confirmation | reverse engineering of controller code, state-machine mining | most inferred states need a human | use as engineering acceleration, not as automatic harmonization |
| Generated code fails certification first time | PLC migration with AI translation | safety functions in scope | separate safety-relevant (human-led, AI-assisted) from non-safety (AI-led, human review) |
| Adoption lower than planned | agentic admin workflows, AI-assisted coding | usage of the first agents stays low | plan with a lower adoption than the deck; agents fail at adoption more often than at capability |
| The organisation cannot absorb the technology | app store, agentic workflows | partners resist central orchestration | start with a forcing function (compliance mandate); keep the onboarding path single |
| Capability build slower than the value | simulation / digital twin | talent is scarce | start with an external partner; separate value confidence from capability pace |

## Definition of done for a rung change

- The rung evidence is linked (the pilot protocol, the pass criterion and the result, or the baseline and the measured effect).
- The claim in the record matches the rung (estimate, pilot result, deployment, proven saving).
- The owner role is named and the handover is in place for rung 4 (`deploy-handover`).
- For rung 5: baseline, measurement method, period and reliability class are stated; the number is not copied from the case.

## AI agent notes

An agent may read the initiative and case records, propose the rung with the evidence for it, flag claims that exceed the rung
(a PoC range quoted as a saving, a target quoted as a result, an external benefit quoted as ours) and draft the validation plan
with a falsifiable assumption. It cites the record and the read date. It never moves an initiative up a rung, never books a saving,
and hands the rung change to the OD lead and the impact evaluation.
