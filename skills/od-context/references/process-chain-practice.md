---
type: Skill Reference
title: Process chain practice
description: Method, decision rules, handoff contract, pitfalls and agent notes for the department context layer, abstracted from the Operations Digitalization slide decks - why a structured context is the precondition for agent work, the currency rules per field, the three demand shapes, plant tiering (first mover, fast follower), maturity sanity check. Guidance only, no figures.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [all, foundation]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Process-chain practice - the context layer and plant tiering

Deck-derived practice for the spine. `PROPOSAL` = registry synthesis; `<to confirm>` = decks disagree.

## 1. Method in practice

**The context layer is the precondition for agent work.** An agent that finds no owner, boundary or source behind a figure cannot act. The decks describe the department once, in a fixed structure, so that scope questions are not re-settled in meetings,
knowledge does not leave with turnover, recurring analyses are not rebuilt from zero, and versions stop disagreeing:

| Layer | Holds |
|---|---|
| Core (short files) | mandate and explicit out-of-scope topics; services with customer, trigger, owner and completion criteria; targets; metrics with source; decision rights; risks; standards; vocabulary; reusable assets |
| Service pack (one per service line) | how the work runs including exceptions; tools and interfaces; **how far an agent may act and who signs off** |
| Process module (optional) | system of record per data object; cross-cutting budget, compliance and security rules; capacity and bottlenecks, **stated before anything is automated** |

Fill it from existing sources (shared drives, team sites, spreadsheets); never retype. Every field is cited, proposed for ratification, or an honest gap.
Pilot sequence: one department, one named owner with calendar time, fill the key files, generate two outputs, connect one consumer (an agent that answers scope questions).

**Derived outputs once the layer exists** (what the registry's skills consume): presentation and SWOT, responsibility overview, metrics report, onboarding pack, scope and audit answers, routing, and intake that already knows trigger, owner and completion criteria.
Across two or more departments the same layer allows a process register, orphan and duplicate topics, mismatching handovers and vocabulary conflicts to be found.

## 2. Decision rules

- **Four currency rules** (per field, not per document): one named person (a role, not a team) per section; a review date that automatically flags stale sections; fields not prose (trigger, owner, source, threshold); missing values stay marked open.
- **Per-field metadata set:** owner, review date, source, expiry. Metrics carry formula, source and read date; authority level and definition of done are machine-readable.
- **Honesty for generated artefacts.** "To confirm" gaps stay out of the output; every element traces to a source field; figures are confirmed as still current by a human.
- **Chain rule** (`PROPOSAL`): an agent step may start only when a human has named the process owner, the data source and the review point. A minimum version without a review screen is acceptable only for read-only extraction.
- **Three demand shapes map onto the three lanes.** (a) A use case on an already connected machine: Lane 1 or 2. (b) A machine that is not yet connected: an equipment-integration wave first, use cases only afterwards. (c) A tool or system that does not exist in the toolbox: requirements, tool decision, IT and security gate (Lane 3).
  A demand that is really a **service gap** (a tool without an operations concept or support role) is not a use case: route it to the system and operations-concept discussion.
- **Explicit "not ours" list.** Smart-automation and smart-equipment measures were excluded from the strategy; triage needs the list written down (`SKILL.md`, "Not OD's").
- **Plant tiering decides capacity, not eligibility.**
  - *First mover:* high estimated value-add; all regions, segments and technologies covered; capacity and knowledge in the plant; integration synergies; a dedicated, staffed key user. Gets central support and review first.
  - *Fast follower:* central support only when capacity allows; locally driven; limited, resource-adjusted funding; roadmap from local assessment.
  The department-level definition is authoritative; a sector-level list for a broader suite is background. The tier of a given plant is a live fact; never copy it into a skill.
- **Maturity sanity check for AI requests.** The value-creation ladder runs from uncontrolled data, through reporting and data-driven processes, to a data-centric architecture and a data economy; AI starts at the third level. Do not rank AI use cases above basic data-model and reporting work in plants that have not reached reporting.
- **Ordering of priorities.** Workshop material ranks by generalization first and savings second; strategy material stresses savings. Say which was used `<to confirm>`.

## 3. Handoff contract

| Receives | From |
|---|---|
| the request, in the requester's words | any intake channel |
| plant, material family, capability coordinate | plant master data, lists named in `SKILL.md` |

| Hands on | To |
|---|---|
| resolved vocabulary, service line, decision right, honesty rules | every other skill (they load this one first) |
| list of gaps marked `<...>` with a supplier role | `od-context-freshness`, the OD lead |
| out-of-scope answer with route | the requester |

## 4. Pitfalls and lessons

- **New systems, slides and trackers added instead of cleaning up** ("if a system is insufficient people introduce another insufficient system"). Retire before adding.
- **Single-person knowledge.** A single technical key user left within weeks of an announcement; no successor was named. Every section needs a named successor.
- **Vocabulary drift.** Several recommendation words for the same tool status; several words for one expansion. One term, one meaning - and look time-bound facts (tool status, plant tier, forum cadence) up live.
- **Reference decks contradict each other** (forum cadence, tool direction, who evaluates use-case value: plants or OD). Prefer the later dated source, say so, and mark `<to confirm>`.
- **Averaging over two populations.** Sort by the variable that drives the economics (for example whether a plant owns its source code) before stating a fleet baseline.
- **A department context that is only prose** cannot be consumed by an agent; use fields.

## 5. Questions to ask and definition of done

Who is the named person for this section and when is it reviewed? Which source holds the value and what is its read date? Is the term already defined here? Is the demand a use case, a connection, a system, or a service gap?

**Done for a context entry:** owner role, review date, source, expiry, and an explicit marker where unknown.

## 6. AI agent operating notes

- **Can do:** answer scope and ownership questions from the layer with the source field cited; classify a demand into one of the three shapes; list gaps and orphan topics; detect vocabulary conflicts across skills; draft derived outputs (metrics report, onboarding pack) with every element traced to a field.
- **Needs:** the context files and list extracts with read dates.
- **Human gate:** ratifying a proposed field; choices the context cannot derive (lane, depth, language); closing "to confirm" gaps; confirming figures are still current; review before an audience sees an output.
- **Must cite:** field and source, owner role, review date.
- **Hands over:** outputs with gaps left as `<...>`, never filled by guess.
- **Reference pipeline for a template-bound deliverable (7 steps):** read context by relevance; read the template and layouts; human gate on the underivable; map fields to elements with a source each; apply the honesty rules; build, render, inspect and fix (overflow, invisible text, contrast); deliver editable with a validation and placeholder-leak check (`od-template-resolution`).
