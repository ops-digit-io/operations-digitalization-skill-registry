---
type: Skill Reference
title: SWOT and dependency seams
description: How to use the department's SWOT as a machine-checkable filter on a proposed action (ids, evidence, so-what, derived moves), how to read the operating-context table of dependency seams and interaction modes, and how the filled-instance README records corrections to source decks and open gaps.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [all, practice, context, strategy]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# SWOT and dependency seams

Derived from the department OS notes (SWOT, operating context, README of the filled instance). This file holds the **method of
reading**. The current entries, their evidence and the numbers cited as evidence change quarterly: read them from the live note
(`00-core/13-swot.md`, `10-modules/smart-factory-use-case/operating-context.md`) and quote them with their `last-verified` date.
Own synthesis is marked `PROPOSAL`; unknowns are `<...>`.

## 1. The SWOT as a filter, not a poster

The SWOT exists so that an agent (or a key user) can test a proposed action against it. Each entry carries an `id` so that bets,
risks and objectives can reference it.

| Part | Internal / external | Columns to read | Use |
|---|---|---|---|
| Strengths (`S<n>`) | internal, present | claim, evidence, so what (where it gives leverage) | something to build on |
| Weaknesses (`W<n>`) | internal, present | claim, evidence, so what (where it costs) | something an action must cover or avoid |
| Opportunities (`O<n>`) | external, potential | claim, signal, window | something an action could capture |
| Threats (`T<n>`) | external, potential | claim, signal, linked risk | something an action must mitigate |
| Derived moves | pairs of the above | move, type, pairs, owner, strategy or objective it serves | the actual decisions |

**The test.** For a proposed action, name which entry id it leverages, covers, captures or mitigates. If it touches none, flag it:
it is either outside the strategy or the SWOT is out of date. Both are findings. If it touches only a strength ("we are good at
this"), ask what it fixes.

**Derived-move types.** Strength with opportunity: use. Weakness with opportunity: fix. Strength with threat: defend.
Weakness with threat: avoid. Every derived move has a named owner role and points to a strategy bet or objective. A move without an
owner or a target is a wish.

**Coaching prompt for the owner.** "Which of these four boxes would a competitor most want us to ignore?" Use it when a SWOT
refresh produces a list that only grows in one box.

## 2. What belongs in each box (shape, not content)

The entries of this department fall into recognisable families. Reading the live note, expect:

- **Strengths:** clear service structure with explicit triggers and definitions of done; proven ability to connect machines at
  scale; a standardized, modular, lean architecture; an established operating rhythm with transparency.
- **Weaknesses:** operations concepts missing or immature for core systems; limited internal IT knowledge on a few platforms;
  staffing gaps in some regions and a thin team; integration behind the yearly target; a value delivery cycle not yet proven or
  measured.
- **Opportunities:** integration with OPEX methods (turn SMED, TPM, Jidoka, VSM into digital use cases); scale-out to high-impact
  locations on own tooling; the data platform as a flexible base; advanced analytics on the integrated base; the savings mandate
  and its budget frame.
- **Threats:** dependence on external tooling and ERP/MES; cyber security and OT exposure when machines are connected; value not
  materialising and investment scrutiny.

These are the *families*; whether an entry is still true, and its evidence figures, are in the live note. The honesty rule of
`od-context` applies: the evidence column quotes Scorecard values with a read date; never carry them into a skill or a deck as
current.

## 3. Exclusions the SWOT keeps on purpose

The SWOT deliberately leaves out: the full competitive analysis (strategy note), risk scoring and mitigation plans (risk register,
`od-risk-watch`) and action tracking (objectives). Do not reintroduce them; link instead. An agent drafting a SWOT refresh should
**read** those notes and reference ids, not copy their content.

## 4. Dependency seams (operating context)

The operating-context note is triggered "when this process depends strongly on other units". It is a table of three columns.

| Column | Meaning |
|---|---|
| Dependency | The other unit |
| Seam | The interface where the two meet, with a link to the term or note that defines it |
| Mode | How the two interact: **tandem** (work is shared, both own the result), **consultation** (the other unit is asked and its answer binds or is weighed), **information** (the other unit is told) |

Seams recorded for smart-factory use-case delivery, by kind of partner (roles and units, not names):

| Partner kind | Seam | Mode |
|---|---|---|
| OPEX / continuous-improvement unit | Digital use cases support OPEX methods (the OD-OPEX interface) | Tandem |
| Plant ME and plant teams | Use-case demand, rollout execution, adoption | Consultation |
| Cyber Security / OT | Machine-connection sign-off, bundling with MSB rollout | Consultation |
| IT / ERP | The MES dependency | Information |
| Manufacturing Engineering (automation) | Insight-based ideation for control optimisation | Consultation |

**How to use it.** Before committing to a plan, list each seam the plan crosses and check its mode. A consultation seam is a **gate**:
the answer must be on record (this is why `od-machine-integration-plan` waits for Cyber Security). A tandem seam means you cannot
plan alone; name the partner's role in the plan. An information seam needs a message, not a meeting. `PROPOSAL`: put the seam and
its mode in the plan header so a reviewer sees the dependencies without reading the body.

## 5. Corrections recorded against the source decks

The README of the filled instance has a "corrections applied" table with the columns *source decks say / actually*. The pattern is
worth copying wherever a source is raw:

1. The raw export is **not edited**; the corrected statement lives in the layer above it, with the date.
2. Each correction is a row: what the source says, what is true now.
3. **Live identifiers are untouched on purpose** (repository names that tooling matches on, message-topic roots, recorded names of
   blockers). A topic is an interface; renaming a label is not worth breaking one.
4. Where a correction removes a counterpart (a party that no longer takes part in a decision), the slot is left `<to confirm>`,
   not guessed.

For an agent: when an old deck, a legacy tool record or a vendored skill names a platform or party that the README lists as not used,
follow the README. See `od-information-integration-service/references/tool-fact-sheets.md` for the platform names.

## 6. The open-gaps list as a work queue

The README closes with a numbered list of gaps: named owners behind role labels, targets and thresholds, a metric with no defined
source, adoption feedback, system interface detail, data-platform detail, decision counterparts, naming after an organisation
rename. Treat that list as the **queue of questions an agent may put to the OD lead**, ranked by how many skills carry a `<...>`
for the same gap. When a gap is closed, the closing note goes to the source note first, then into the skills that carry the
placeholder (`od-context-freshness` finds them).

## AI agent operating notes

- **May do:** test a proposed action against the SWOT ids and report which it leverages, covers, captures or mitigates (or none);
  list the seams a plan crosses with their mode; compare a deck's statement with the corrections table; draft a SWOT refresh as
  proposed rows with evidence cells filled from named sources.
- **Inputs:** the live SWOT, the operating-context note, the README corrections and gaps, the proposed action.
- **Evidence to cite:** entry ids, note path, `last-verified` date.
- **Human gate:** the OD lead owns the SWOT and the derived moves; an agent proposes rows, never changes the live note. Strategy
  statements are not edited by agents.
- **Hands over to:** `od-decision-routing` (when no entry is touched), `od-risk-watch` (threats), `od-context-freshness` (stale
  evidence).
