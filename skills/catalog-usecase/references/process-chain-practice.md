---
type: Skill Reference
title: Process chain practice
description: Method, decision rules, handoff contract, pitfalls and agent notes for the catalog step, abstracted from the Operations Digitalization slide decks - archetypes, what graduation from validated prototype to configurable container app means, what a catalog entry should say, and why a scaled use case needs utilization, not a rollout count. Guidance only, no figures.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [all, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Process-chain practice - picking and graduating

Deck-derived practice for steps 1a1, 1b1 (pick) and 26 (graduate). Statements marked `PROPOSAL` are the registry's own synthesis.
Where the decks disagree the safer reading is written and tagged `<to confirm>`.

## 1. Method in practice

**Picking (Lane 1).**
1. The plant states the need in its own words. Reduce the sentence to **object** (part, order, tool, recipe, batch, carrier), **event** (error, change, stop, NOK part) and **time axis**.
   Many "unique" requests collapse to a few shapes this way; ask for object and event before judging uniqueness (`od-use-case-intake-triage`).
2. Match the shape to a capability template and a library entry. A request that only changes the look of an existing screen is not a catalog match.
3. Check the two preconditions the decks repeat: **the machine is connected** and **the needed signals are selected**. A use case is available only for machines that are already connected;
   a requirement beyond the agreed timeframe becomes an additional use-case phase, not scope creep.
4. Branch 1a or 1b as in `SKILL.md`. Ask who at the plant will use the result and in which meeting (see section 5).

**Graduating (end of Lane 2).** The decks describe one graduation pattern:

| Stage | What exists | Counts as catalogued? |
|---|---|---|
| Proof of concept | a minimal test that de-risks the idea | no |
| Validated prototype | works for one plant, validated with its owner | no - it is a candidate |
| Configurable container app | flexible algorithms and configurable rule sets, packaged, deployed through the app store | yes, once the four conditions in `SKILL.md` hold |
| Standard | the app is the thing other plants take | yes |

A use case is **standard** when a validated prototype exists and only the more flexible, configurable container or app is missing. It is **special** when its data source is
proprietary or external, or when it is process-specific and the generic method is still undefined. Machine-learning-based standards additionally need: a requirements document,
data from several plants, a validated model, the model packaged with a defined interface to its trained parameters, a monitoring and retraining process and a visualization concept validated with the plant.

## 2. Decision rules

**Archetypes - three classes, one action each** (deck rule, restated):

| Archetype | Depends on | Typical constraint | Action in the catalog |
|---|---|---|---|
| Standard, **cross-process** | nothing about the core process | has limits (for example not meaningful for continuous processes) and needs integration work because data models differ | catalogue with priority; state the limits in the entry |
| Standard, **per-process** | process values of one core process | fewest constraints; scales fastest | catalogue; instantiate from the process data model |
| **Unique** | factory conditions, a legacy system, a one-off problem | not scalable beyond the site | do not catalogue; run an impact analysis first, then decide |

Custom use cases are possible only if the expected value is very high; they may be prototyped, and count as mature only after integration into the standard systems.

**Triage buckets** (deck, `PROPOSAL` for using them as catalog routing): *just do* - generic dashboard, notification or energy case on already integrated equipment, copy from another site,
no new development; *go forward* - continue or integrate an earlier proof of concept that depends on a shared enabler; *lead change* - exploratory, needs a prototype first, human call.

**Kill and hold.** A request can end as cancelled with a recorded reason (no data foundation, insufficient savings, another party already collects the data). Keep the reason so the idea is not re-raised from scratch.

**Plant tiering decides capacity, not eligibility.** A first-mover plant gets central support first; a fast follower picks from the catalog with central help only when capacity allows.
First-mover criteria in the decks: high estimated value-add, coverage of regions, segments and technologies, capacity and knowledge in the plant, integration synergies, and a dedicated, staffed key user.
The tier is a property of the plant, looked up live (`od-context-freshness`); never copy a plant list into a skill.

**Zero-saving scaled entries.** Where an entry is deployed widely and reports no saving, do not write "no potential" - write "to be evaluated" and list three things: where it saved, where it was deployed without saving, where it still has potential.
Until investigated the entry stays "to be evaluated". Only a human (the OD lead with the plant owner) may decide "no potential" or retirement; an agent never writes it.

## 3. Handoff contract

| From | Must hand over | Receives from this skill |
|---|---|---|
| `od-use-case-intake-triage` | object / event / time, archetype guess, machine-connected flag | - |
| `od-data-availability-check` | verdict on signals, per plant | - |
| `od-use-case-standardization` / `od-use-case-promotion` | template, cluster, CSP status, graduation checklist | - |
| to `od-analytics-asset-build` (1a) | match record, entry id, reference plant, deltas to record | the baseline to copy |
| to `catalog-systems` (1b) | match record, machine class, where the data should land | - |
| to Lane 2 / Lane 3 | reason for fall-through, what was missing | - |
| to `od-handover-and-adoption` | **named utilization moment** (who opens it, in which meeting, which action follows) | - |

## 4. Pitfalls and lessons

- **Deployed is not used.** Many widely scaled use cases ran with no reported saving. The count of delivered entries is not an impact indicator; a high count can hide unreported impact or unused potential. A catalog is judged by utilization and by savings where they exist.
- **Visibility alone creates no saving.** Savings appeared where the screen drove a defined action by a named owner. A catalog entry without an action owner is a build smell.
- **Local solutions are input, not new demand.** A plant may already run a local solution that fits the method but is not standard. Treat it as input to standardization.
- **Dashboards per plant, never harmonized** is a recurring debt. Manual-entry use cases (lab data, quality data) need data model, storage, input screen and analytics in one standard, otherwise every plant builds its own variant.
- **Rollout is gated by integration, not by the dashboard.** A dashboard "ready" for a second process is pending until that process's machines and tags are selected.
- **Entry rots.** Use-case lists and libraries hold stale or low-value entries and drafts with empty data and dependency boxes. A canvas with empty data and dependency boxes is not ready for the data check.

## 5. Questions to ask and definition of done

- Which object does the answer need to be keyed on, and where does its identifier live today (signal, MES or ERP, manual entry)?
- Live view, report on a cadence, or a record to be entered? What decision follows the number, and who is the named plant owner?
- Is there a plant-side method the screen feeds (changeover method, digital Gemba, switch-off campaign)? The pairing of *standard method + digital standard use case + standard process* is what makes an entry get used.
- What can the use case do, and what can it not do (for example: explain an equipment issue and notify, but not recommend or solve)? Put both in the entry.

**Entry content the decks want** (a catalog entry is also its own marketing page): used for what; why (the story behind it); how it helps (functions); what it can do; what it cannot do; an example screen; reference plant; maturity;
where applied; next call to action; and *can it substitute an existing manual practice*.

**Done for a pick:** match record written; branch named; preconditions evidenced; utilization moment named; no figure without source.

## 6. AI agent operating notes

- **Can do:** reduce the plant's sentence to object / event / time; propose template and library entry; list which preconditions are evidenced; flag empty canvas boxes (data, dependencies, success criteria); check graduation conditions and list the missing ones; draft the entry text from the plant's answers.
- **Needs:** use-case list row, machine list status, library entry, CSP field, read dates.
- **Human gate:** the plant decides what it runs; the CSP decision stays with its owner; assigning *lead change* and keeping a *unique* case alive are human calls.
- **Must cite:** library entry id, list row, source of the connected-machine fact, read date.
- **Hands over:** the match record to the next skill named in `SKILL.md`, with the utilization moment filled or marked `<to confirm>`.
