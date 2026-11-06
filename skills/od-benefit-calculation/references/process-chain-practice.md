---
type: Skill Reference
title: Process chain practice
description: How the business-case step (24, 33) is run in the AI-driven chain - segment before averaging, grounding tags on every figure, banked floor versus potential versus de-banked value, baseline first, what to hand to the capital request, and what an agent may draft. Pattern only, no figures.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [use-case-support-service, practice, process-chain, draft]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Process-chain practice

Distilled from the Operations Digitalization slide decks, abstracted into process guidance. No company figures. Anything
marked `PROPOSAL` is a synthesis, not a deck rule; `<...>` is unknown.

This file sharpens the ledger rules in [`SKILL.md`](../SKILL.md). It does not replace them: **tracked versus proven** stays
the status axis of a saving row; **banked floor / potential / de-banked** below is a second, independent axis (how well the
number is grounded). Keep both on every figure that leaves the department.

## 1. Method in practice (steps 24 and 33)

1. **Split the estate by the variable that drives the economics, then state a baseline per segment.** Look for the
   splitting variable first (in one worked case: who owns and controls the machine programs in-house, which separated the
   plants into two operating models). One fleet median or average over two populations hides the value; baselines are
   often bimodal. Say which variable you used and why.
2. **Credit a lever only on the slice it can reach.** A lever that attacks the integration part of a ramp-up is credited on
   that part, not on total effort. A contract clause that works only for custom builds carries no target for catalogue
   purchases. Re-scope inherited targets to the addressable slice before you print them.
3. **Read a low rate carefully.** A low change count at a locked site means improvement is impossible there, not that the
   process is stable (suppressed demand). Never take it as a healthy baseline.
4. **Tag every figure** with its grounding (section 2). No tag, no release.
5. **Express benefit as frequency x duration x rate, per role**, and list softer effects as "not yet considered" instead of
   dropping them. Take assumptions from the plant's own answers, not from market studies; show a range, not a point; the
   purpose is to rank investments, not to budget to the euro.
6. **Baseline first.** If no measured baseline exists, do not print NPV, IRR or payback. Defer the return until the baseline
   is captured, and fund the measurement layer first (`od-investment-input`, `od-capital-request`).
7. **Rank open questions, not just answers.** List the unknowns that move the result most, each led by a worked example so
   the answerer can correct a number rather than invent one, each with an owner role (controlling, purchasing, quality).
8. **A case that is mainly an enabler** for other cases is scored as an enabler. Write the entry-condition relation down
   (which case it unlocks); do not double-count its effect inside the cases it unlocks.

## 2. Decision rules

| Tier | Meaning | May be summed with |
|---|---|---|
| **Banked floor** | Small, sourced today, a stated input from a named role | Only other banked floor rows |
| **Potential** | Top-down envelope; the mechanism is validated, the euro total is not | Never with the floor |
| **De-banked** | Rests on a crucial unknown; shown only as sensitivity | Never |

- **Never net value against cost.** Show value and cost as separate lines; a "net" figure hides which side moved.
- **Name the gap** between floor and envelope and turn its largest part into the top open question.
- **Grounding tag per figure:** `[input]` stated by a source, `[assumption]` our estimate, `[market]` a standard value
  where none was given, `[unknown]` a crucial missing input we refuse to fake. A claim "not found in the source" is carried
  as **unverified**, not dropped and not repeated as fact.
- **Evidence coverage** is reported per segment (full / partial / thin or none). A target that leans on thin coverage is
  flagged. "Not mentioned" is not "absent".
- **Hard anchors stay single-site.** An observed per-case cost or supplier-support spend is a single-site anchor until a
  second site confirms it; do not scale it to the estate from one site.
- **Countable only with a before/after condition.** A use case that cannot show a condition before and after is not counted
  as a saving.
- **Interviews validate mechanism and baselines**, not a bottom-up euro total. Say so in the case.
- **Savings basis label at workshop time:** `calculated`, `estimated` or `none`. "Open task" stays open until a basis is
  shown; do not quote a savings sum in a summary without it.
- **Each saving row links to a use-case id, a baseline and, later, a registered plant savings project.** A use case with no
  registered project is invisible to the ledger.

Where decks disagree:

- *Calculated or estimated?* Workshop summaries carry "estimation: open task". A saving is **estimated** until it is
  confirmed; **calculated** only with a documented basis. Label the basis on every row and label every figure input /
  assumption / market / unknown; finance-proven values stay separate.
- *Realized or estimated?* A one-pager headline described as realized rested on a top-down estimate. Treat such a headline as
  **potential** until a banked floor is shown.
- *Who evaluates, the plant or OD?* After go-live the plant evaluates its use cases; OD provides the calculator and the
  method and reviews the result. Before go-live OD drafts with the calculator and the plant owner confirms baseline and
  factor.

## 3. Handoff contract

| Receives (from) | Hands on (to) |
|---|---|
| Use-case canvas with current state, objective, success criterion (`od-use-case-definition`) | Benefit rows with tier, grounding tag, basis label, dependency and owner role -> `od-portfolio-and-savings-analysis` (rank) |
| Workshop savings pre-evaluation, capture sheet with plant, process, owner role (`od-workshop-facilitation`) | Cost-side request: which value rows depend on the spend -> `od-investment-input`, `od-capital-request` |
| Validation record (`od-prototype-poc`) | Ranked open-question list with owners -> back to the requester, not forward |
| Baseline from plant controlling | The row to SPRINT only when defensible (`od-impact-evaluation`) |

## 4. Pitfalls and lessons

- Averages that mix two populations; targets copied from a blueprint without a baseline check; one site's relief counted at
  fleet scale.
- Counting delivery as value: scaling count and "recorded demand" are not savings; reusability is cheap, monetary impact is
  derived per site.
- Savings missing because the baseline was never defined at sprint start (see `od-impact-evaluation`, forecast gate).
- Unreported versus unused: a missing saving may be unreported (the deployers do not report) or truly unused potential.
  Find out which before drawing a conclusion.
- Stating the staffing assumption nowhere: the same portfolio gives different projections under central-only staffing and
  central-plus-dedicated plant key users. State the assumption next to every projection.
- Savings registered by hand lag the work done; a short-term fix is to register a savings project for what is already
  implemented.

## 5. Questions to ask / definition of done

- Which variable splits this estate? Which segment is this case about? What is the baseline there, and who measured it?
- What decision or action follows from the number, and who owns it?
- Which figures are `[input]`, which `[assumption]`, `[market]`, `[unknown]`? Where is the sensitivity?
- Done when: every figure is tagged; floor, potential and de-banked are separate; value and cost are not netted; open
  questions are ranked with owners; the gap to a baseline, if any, is named as the first deliverable.

## 6. AI agent operating notes

- **Can do:** build the base / improved-by / factor / yearly table from a capture sheet; check that each row links to a
  use-case id and a baseline; mine interview or workshop transcripts per segment and extract candidate anchors with a quote
  and a source link; assign a draft grounding tag; flag any figure with no tag or no source; compute the where-saved /
  deployed-without-savings / potential matrix and label tracked versus proven. `PROPOSAL`: a lint that rejects a figure
  leaving a case without a tag, and one that rejects NPV or IRR printed without a baseline.
- **Required inputs:** use-case record, savings ledger read with its date, transcripts or capture sheets, baseline source.
- **Human gate:** plant controlling accepts baseline and factor; the business-value role decides what counts as `[input]`
  versus `[assumption]` and signs the ranked open questions. An agent never writes "proven" and never decides "no potential".
- **Evidence to cite:** ledger row id and read date, transcript location, baseline file, the rule that set the tag.
- **Hands over:** the tagged rows and the ranked open questions to `od-portfolio-and-savings-analysis` and
  `od-capital-request`; unresolved `[unknown]` figures travel with the package, not removed.
