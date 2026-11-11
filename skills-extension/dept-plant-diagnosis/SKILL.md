---
name: dept-plant-diagnosis
description: >-
  Diagnose why plants with a similar system landscape and similar integration effort deliver unequal
  savings - read the gap across four Ishikawa branches (people, method, machine and IT, environment),
  tier plants as first mover or fast follower with stated criteria, and turn the result into a plant
  roadmap with a status and a "call for action" per row, rolled up into a regional roadmap. Includes how
  to synthesise interview and workshop evidence without over-claiming. Use when two plants look alike
  but save differently, when a plant enters OD scope and must be tiered, when a plant or regional
  roadmap must be drafted or refreshed, when a call needs per-plant status and call-for-action text, or
  when interview notes must be turned into a diagnosis.
license: MIT
allowed-tools: Read Grep Glob
metadata:
  id: dept-plant-diagnosis
  aliases: [od-plant-diagnosis]   # former name (naming convention, 2026-11-11)
  tier: practice
  lane: all
  new_state_lane: "Extension, deepens Lane 2 (24), Spine"
  new_state_step: "Business case (value and cost), assessment, ranking; Supporting spine"
  owner_role: human:jakob.gabriel
  authority_level: draft the diagnosis, tiering proposal and roadmap; recommend on sequencing and tier; tier assignment and roadmap approval are human
  status: draft
  origin: plan-draft
  requires: [dept-context]
  composes: [dept-plant-onboarding, catalog-compatibility, bc-portfolio, metrics-scorecard, mi-equipment, dept-decision-rights, dept-risk]
  okf:
    type: Agent Skill
    title: Plant gap diagnosis, tiering and roadmap
    tags: [all, practice, new-state, draft]
---

# Plant gap diagnosis, tiering and roadmap

Read `dept-context` first. This skill holds **no figures** about plants or savings. It is a method; the numbers
come live from the lists and the scorecard (`bc-portfolio`, `metrics-scorecard`).
Statements marked `PROPOSAL` are this skill's own synthesis, not a decision of the department.

## Purpose and definition of done

Two plants can connect a similar number of machines on a similar system landscape and still show very
different savings. The decks' working rule: **equal integration effort with little or no saving points to
people and method, not to technology**. This skill makes that visible per plant, decides how much central
support the plant gets, and writes the plant's next steps into a roadmap that a call can track.

Done when: (1) the comparison set is fair (procedure step 1); (2) each gap is placed on an Ishikawa branch
with evidence and a confidence label; (3) the plant has a tier (first mover or fast follower) with each
criterion answered; (4) the plant roadmap has one row per workstream with status and a call-for-action cell;
(5) the regional roadmap is updated from the plant rows; (6) open unknowns are listed with an owner role.
- **Outputs:** [`references/outputs.md`](references/outputs.md) lists what this skill must deliver, to whom, and when each output is complete.

## Where it sits in the chain

| Step id | Role of this skill |
|---|---|
| Spine, plant onboarding (`dept-plant-onboarding`, stages 1-3 and 8) | Tiers the plant when it enters scope and again at the rhythm review; writes its roadmap |
| 24 Business case and rank (`bc-portfolio`, `bc-portfolio`) | Explains a zero or low saving by plant before a use case is judged "no potential"; supplies the tier as a capacity input to ranking |
| Spine, rhythm (`metrics-scorecard`) | Feeds the status and call-for-action cells of the plant status table in the community-of-practice call and the regional roadmap in the strategy round |
| Lane 3b step 3b4 (`catalog-compatibility`) | Receives its verdict when a gap is technical (a plant cannot consume a standard) |

Proposed step ids for the registry: spine (plant onboarding, rhythm) and 24.

## References and assets

| File | Use it for |
|---|---|
| [`references/ishikawa-gap-diagnosis.md`](references/ishikawa-gap-diagnosis.md) | The four branches, the causes recorded per branch, the good-practice and bad-practice signature, how to compare plants fairly, and the scaling test for zero-saving use cases |
| [`references/tiering-criteria.md`](references/tiering-criteria.md) | First mover vs fast follower: criteria, what each tier gets, how to apply them, wave allocation (request order, then staffed first movers) |
| [`references/roadmap-templates.md`](references/roadmap-templates.md) | Plant roadmap rows, status colours, call for action, regional roadmap fields, the call agenda that consumes them |
| [`references/evidence-synthesis.md`](references/evidence-synthesis.md) | Turning interviews and workshops into a diagnosis: grounding tags, coverage, splitting variable, open questions |
| [`assets/plant-gap-diagnosis-record.md`](assets/plant-gap-diagnosis-record.md) | The record: comparison set, Ishikawa, signature, tier, evidence, open questions |
| [`assets/plant-roadmap-template.md`](assets/plant-roadmap-template.md) | Plant roadmap and regional roll-up tables with status and call-for-action cells |

Not repeated here: starting profiles and the onboarding path (`dept-plant-onboarding`), whether a standard is
consumable at a plant (`catalog-compatibility`), rollup rules and the three misleading readings of the
data (`bc-portfolio`), ranking of use cases (`bc-portfolio`), classifying a
machine that will not connect (`mi-equipment`).

## Procedure

1. **Build a fair comparison set.** Pick plants with a similar system landscape and a similar machine and
   integration position; read the live lists on the day (`know-sharepoint-export`). If the plants differ in
   a splitting variable (for example whether the plant owns its machine programs in-house), compare within the
   segment, not across it (`references/evidence-synthesis.md`). Absence of a record is not zero
   (`bc-portfolio`).
2. **Collect the observable facts per plant**: integration status, systems deployed, use cases deployed,
   use cases with a registered saving project, utilisation, key user staffing, open barriers, ticket age for
   IT issues. Missing fields stay `<unknown>`.
3. **Diagnose with the four branches** (`references/ishikawa-gap-diagnosis.md`): people, method, machine and
   IT, environment. For each gap name the branch, the cause, the evidence and a confidence label. Check the
   technology branch last: it is the least likely cause when effort is equal.
4. **Read the signature.** Does production proactively drive ideas, does the plant ask for blueprints from
   others, are requirements formalised with OD, are savings calculated with controlling and registered before
   the next wave? Or is the plant contact "only responsible for the technical part", the production demand
   unknown, standards ignored, savings not calculated? The signature decides which branch to start with.
5. **Run the scaling test** for any use case deployed in several plants with zero saving somewhere: three
   lists - where it saved, where it was deployed without savings, where it still has potential. A
   deployment without savings means *to be evaluated until investigated*, not *no potential*. Only a human
   (the OD lead with the plant owner) may decide "no potential"; an agent never writes it.
6. **Tier the plant** with `references/tiering-criteria.md`. Tier decides central capacity, not eligibility.
7. **Write the roadmap rows** from the gaps: one row per workstream, owner role, target date, status colour,
   call-for-action text (`references/roadmap-templates.md`). Fix people and method gaps before adding
   technology rows.
8. **Roll up to the regional roadmap** and prepare the call inputs. Report per region against plan with a
   short relative judgement, not a blended number.
9. **Hand over** (below) and file the record.

## Handoff contract

| Receives | From |
|---|---|
| Plant placed by starting profile, machine and use-case lists read on the day | `dept-plant-onboarding`, `know-sharepoint-export` |
| Savings by plant with tracked and proven kept apart, and the use-case status cut | `bc-portfolio` |
| Barrier log for machines that will not connect | `mi-equipment` |
| Compatibility verdict per plant for a standard | `catalog-compatibility` |

| Hands on | To |
|---|---|
| Tier per plant as a capacity input; gap reasons for a use case judged low | `bc-portfolio`, `bc-portfolio` |
| Roadmap rows with status and call-for-action text; regional roll-up | `metrics-scorecard` (call and strategy-round inputs) |
| A technical gap on a standard | `catalog-compatibility` |
| A rollout or tier exception, a resource request, an escalation with a deadline | `dept-decision-rights` |
| Open risks (staffing, central IT commitment, key user loss) | `dept-risk` |
| Confirmed lessons | `dept-retro` |

Nobody should re-ask the plant for: the facts in step 2, the tier criteria answers, the owner per roadmap row.

## Questions to ask the plant key user

- Who proposes the ideas - production, OPEX, engineering, or only OD? Who asks other plants for blueprints?
- Who calculates the saving, with whom (controlling), and when is it registered relative to the project wave?
- Which functions attend the requirement meetings with OD?
- Who is the named, staffed key user, how much time is available, and is there a deputy?
- Which IT or cyber-security approvals are open, and how old are those tickets?
- Is the layout of the machines stable enough to commit an integration wave?
- Which use cases are deployed and used, which are deployed and not used (utilisation)?

## Pitfalls and lessons

- **Reading a technology gap into a people gap, or the reverse.** Check effort parity first; only then place the cause.
- **A hand-registered savings list lags the work.** A saving may exist but not be registered; short-term
  measure: register a savings project for what is already implemented, then compare.
- **"Not mentioned" is not "absent"** when interview coverage was uneven (`references/evidence-synthesis.md`).
- **Ideas-driven demand.** Requests launched without pre-alignment with OD, driven by an idea instead of an
  expected effect, create friction and non-scalable one-offs: route them through `dept-intake`.
- **Tier read as eligibility.** A fast follower is not refused; it is supported when capacity allows.
- **Dashboard-type use cases without a saving** are counted as transparency outcomes in some material and as
  gaps in the gap analysis; state which reading the comparison uses.
- **A suppressed-demand site** (locked or frozen) shows few changes because work is impossible, not because
  it is stable.

## AI agent operating notes

An agent can: read the live lists and build the comparison set; compute per-plant facts; draft the Ishikawa
table from interview notes, citing the source line per cause; pre-fill the tier criteria from the lists and flag
the ones it cannot answer (key user staffing, local knowledge); draft roadmap rows, status colours and
call-for-action text; roll plant rows into the regional table; list overdue rows and ageing tickets (`PROPOSAL`).

Required inputs: plant list reads dated that day, savings view from `bc-portfolio`,
barrier log, interview or workshop notes, previous roadmap.

**Human gate.** The OD lead (with the regional lead) assigns the tier and approves the roadmap; the local key
user confirms the facts and the owner per row; a tier or wave exception goes to `dept-decision-rights`. The
agent never changes a tier, never marks a row green without the evidence named in the status rule, and never
shares a plant comparison outside the department without approval.

Evidence to cite: list name and read date, deck or interview source role, grounding tag
(`references/evidence-synthesis.md`). Hand over by filing the record and the roadmap tables and naming the
rows that need a decision.

## Still open

- `<Tier criteria thresholds>`: the criteria are qualitative; no threshold is stated for "high estimated value".
- `<Sector-level vs department-level first-mover lists>`: treat the department definition as authoritative.
- `<Whether a tier is reviewed at fixed intervals>` and by whom.
- `<Form and location of the roadmap>` (list, deck or scorecard section).

## Do not

- Do not quote plant figures from memory; read the lists and date the read.
- Do not name individuals; roles only.
- Do not conclude "no potential" from zero reported saving before the scaling test.
- Do not sum tracked and proven savings (`bc-portfolio`).
- Do not use the tier to refuse a request; use it to schedule central capacity.
- Do not set a roadmap row to green without evidence; a missing close-loop update is yellow.
