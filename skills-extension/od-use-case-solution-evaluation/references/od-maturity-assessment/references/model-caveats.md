---
type: Skill Reference
title: Model caveats
description: What the IT/OT maturity model is and is not - provenance of levels and dependencies, the numbering reconciliation, the undefined levels, the architecture-choice areas, and why the literature distributions are not a benchmark.
resource: ../procedure.md
status: draft
tags: [practice, maturity, caveats, draft]
---
# Model caveats - read before quoting the model

Source: the knowledge base's External Research note set on the IT/OT maturity model, compiled by AI from published papers and marked there as not
reviewed by a human. Cite the model as a literature framework, never as an internal standard.

## Provenance

- **From the papers**: the level labels of the 16 areas, the 27 complexity drivers, the realization dependencies and the idea of choosing a target
  from need. The first-hand source of the area definitions (a 2017 book chapter, and a 2018 dissertation behind the tables) was **not available**
  to the compiler; only labels are published.
- **From the knowledge base (operationalization)**: the observable evidence per level, relevance for the namespace and AI work, assessment questions,
  indicators, critique and target guidance, and the mapping of drivers to areas. This skill's rubric restates that layer; it is a working
  reading, not the paper's definition.
- **From this skill**: the object-level rubric, the evidence grade, the route signals and the plausibility checks (marked `PROPOSAL`).

## Known weak points

1. **Two numbering schemes.** The level tables count from 1, the case base counts from 0. The knowledge base converts everything to the 1-based scale;
   do not mix tables from different sources without checking the base.
2. **The dependency table does not reproduce the published development paths**, even read with the best-fit shift. Further, unpublished
   dependencies were evidently used. Treat it as a prompt for the sequence, validate the sequence against the own architecture in a pilot.
3. **Two levels are undefined in the published table**: the fourth level of protocols (read as standard protocol plus standard semantics) and
   the fourth level of control structure (decentralized, agent-based). When you use them, say they are the operationalization's reading.
4. **Architecture choices, not maturity**: mobility, interfaces, storage and processing are ordered by a decentralization paradigm. A higher
   level there is an option; "combined" is often the right end state.
5. **Self-assessment** was the source's method for the driver profile; the weakest point. Use two raters.
6. **The literature case base** is research and pilot cases of an earlier period, not an industrial population. Its distributions show what was
   published. They are not a benchmark for any plant, and this skill does not use them.
7. **The papers' case study** (three plants of one company) is not carried into this skill; only the method travels.

## What to do with that

- Quote levels with their source layer ("paper label", "knowledge base cue", "this skill's reading").
- Keep the rating qualitative: levels, evidence grade, high-medium-low drivers. Do not add up levels into a score and do not rank objects by a
  total; the model offers no weighting.
- Put an own validation on the open list: a pilot on one object type that checks whether the backbone order holds.
