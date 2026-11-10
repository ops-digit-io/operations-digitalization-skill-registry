---
type: Skill Reference
title: Strategic initiatives and savings
description: How to read the strategic AI and operations business cases next to the plant savings portfolio without mixing them - addressable versus realistic value, author inputs versus recorded savings, enabling value booked once, and the checks to run on a value anchor. Pattern only, no values.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [all, practice, ai]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Strategic initiatives and savings

Source: knowledge base `Graph/Business Cases` and `Graph/Keynote Initiatives` / `Graph/Keynote Clusters` (strategic cases and their value
domains), `Case Groups` (the plant use-case groups) and the overview's own "things to know first". All AI-curated, not reviewed
by a human. This file holds **no value ranges, costs or counts**; read them live and quote the read date.

## Two portfolios, two meanings

| | Plant use-case portfolio (case groups, savings list) | Strategic business cases and initiatives |
|---|---|---|
| Unit | A use case at a plant; a case group is a capability in a process family | An initiative across the estate |
| Value source | Savings rows entered in the list; some marked proven | Authors' inputs: anchors, ranges, a mid-point |
| Reliability | Tracked or proven (see `rollup-method.md`) | Estimate; a PoC is still an estimate |
| Costs | The case-group notes take external cost as zero by owner statement and do not price internal effort, so delivery capacity limits rollout | The cases carry resource and cost estimates (people, compute, licences) |
| Use | Where saved, where delivered without saving, where potential | Which bets to fund, in which order |

The knowledge base says it explicitly: the strategic cases are "a different set" and "were not merged" with the case groups. Do not add,
rank or convert between them. A strategic case may *name* plant use cases it would build on; that is a link, not a transfer of
euros.

## Reading a strategic value claim

1. **Addressable versus realistic.** The keynote value domains (performance, availability, quality, facility and general
   operations, R&D) give a large addressable base and a much smaller realistic share, or "to be defined" for exploratory work.
   Quote the realistic reading, name the domain, and never present the addressable base as the expectation.
2. **Anchors.** Each case builds value from named anchors: a base (assets, incidents, hours) times a rate (cost per hour, burden)
   times an effect share (avoided, recovered, reduced). Check that every factor has a source, that the effect share is stated as a
   range, and that the base is the population the pilot will really reach.
3. **Convergent range.** A range is the author's converged reading of several anchors. Ask which anchor carries it. If one
   anchor does, the case is only as good as that anchor.
4. **Sensitivity.** Read the conservative version the case itself gives, and the condition that shrinks the case (for example the
   dependent case does not consume the output). Use the conservative version in a ranking unless the pilot has passed.
5. **Confidence labels.** Where value confidence and capability or adoption confidence differ, keep them apart in the record.
6. **Cost.** A low cost can be low because something already exists (a pipeline, a pilot). Without that head start the cost class
   changes; note the dependency.

## Never double count

- **Enabling value** is booked in the dependent case. An enabler's own value is its direct engineering effect only.
- **Overlapping domains.** A first-pass-yield effect can appear in an event-mining case and a predictive-quality case. The cases
  state which share is counted where; if they do not, treat both ranges as overlapping and do not sum.
- **Bundles** carry no standalone euro without their parent.
- **Outcome cases** (for example ramp-up acceleration, OEE attribution) are not additional to the levers that produce them.
- **Tracked and proven** stay separate in every rollup; a strategic estimate is never "tracked" until a measured baseline exists.
- **External evidence** (case studies of other firms, standards) is context. The knowledge base marks such figures as "not our result".

## What may go into the savings portfolio

| Item | Goes in as | Condition |
|---|---|---|
| Business-case range | Not in the portfolio | It stays in the strategic list as an estimate |
| PoC or pilot effect | Tracked, labelled estimate or pilot | Test conditions stated; no extrapolation to the estate |
| Productive deployment, no measurement | A delivered case without a saving | It is a candidate for evidence collection (`od-handover-and-adoption`) |
| Measured effect with baseline and owner | Proven, per row | Reliability class stated; period stated |

## Check list before you quote a strategic number

- Which list, which item, which read date?
- Is it an author input, a pilot result or a measured effect?
- What is counted here, what is booked in a dependent case?
- Does it overlap another case's range?
- What is the conservative version and the condition for it?
- Which rung of `ai-initiative-maturity-ladder.md` (skill `od-ai-generation-playbook`) is the initiative on?

## AI agent notes

An agent may extract anchors, bases and rates from a case record into a table, flag overlaps between cases, and compute the
conservative reading from the case's own sensitivity text. It labels every figure with source and class, never adds a strategic
estimate to a tracked or proven total, and hands the interpretation to the OD lead.
