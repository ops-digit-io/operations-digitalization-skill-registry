---
type: Skill Asset
title: Epic and stories
description: "The blank epic to copy: background, epic statement, both epic axes, and the user story shape."
resource: ../SKILL.md
status: stable
tags: [requirements, epic, blank]
---
# EPIC-⟨id⟩ · ⟨plant⟩ · ⟨capability or process⟩

## Background — what this is used for

⟨Prose, 5–10 sentences. Not a table. Somebody who was not in the room must be able to decide
whether a story is right after reading only this.⟩

**Today.** ⟨The actual sequence: who does what, when, how often. Name the role and the hour,
not "manual data collection".⟩

**The moment of use.** ⟨When the output gets looked at, by whom, and what they do next. If no
moment can be named, stop here and refuse — see the skill's refusal section.⟩

**The decision it changes.** ⟨What a named person will do differently, and what that is worth
in time or scrap or reaction.⟩

**Why now.** ⟨The trigger: customer complaint, line moved, audit finding, machine purchased,
roadmap item.⟩

**What this is not for.** ⟨The scope fence. Written here it holds.⟩

## Epic statement

**As** ⟨named role or function⟩, **we want** ⟨capability⟩, **so that** ⟨outcome particular to
this plant and this process — if it would read the same on another plant's epic, rewrite it⟩.

## Epic frame

| | |
|---|---|
| Capability epic | ⟨one of the capability templates⟩ |
| Process epic | ⟨one of the process templates⟩ — *record both axes* |
| Cluster | ⟨C01…C12⟩ |
| Plant / machines | ⟨plant⟩ · ⟨machine ⟨EQ id⟩, …⟩ |
| Lane | ⟨use-case / integration / project / analytical⟩ |
| Requirement | ⟨link to the §1–§11 requirement this epic comes from⟩ |
| Owner | ⟨name, role⟩ |
| Value (epic total) | ⟨amount⟩ ⟨year⟩ · ⟨CALCULATION / ESTIMATION / not yet assessed⟩ |
| Standard or specific | ⟨standard — adopt ⟨source plant⟩ / standard with deltas / genuinely specific because ⟨reason⟩⟩ |

## Scope

**In.** ⟨⟩
**Out.** ⟨⟩

## User stories

⟨At least two. If there is only one, this is a story, not an epic. If there are more than
about eight, this is two epics.⟩

### US-⟨n⟩ · ⟨short title⟩

**As** ⟨named plant role⟩, **I want** ⟨capability in the plant's own words⟩, **so that**
⟨the decision or action this specific story changes⟩.

**Background.** ⟨2–3 sentences specific to this story. The epic's background does not
substitute for this.⟩

**Signals**

| Signal | Direction | Exists? | Unit | Collection |
|---|---|---|---|---|
| ⟨CanonicalName⟩ | in | ⟨yes ⟨uuid⟩ / no — blocked on ⟨what⟩⟩ | ⟨unit⟩ | ⟨transition / sample @ interval⟩ |

**Acceptance criteria**

1. **Given** ⟨state⟩, **When** ⟨event⟩, **Then** ⟨observable result with a specific value⟩.
2. **Given** ⟨⟩, **When** ⟨⟩, **Then** ⟨⟩.
3. ⟨**Use in a real shift** — required. E.g. "⟨role⟩ completes ⟨routine⟩ without ⟨old manual
   route⟩ for ⟨n⟩ consecutive shifts."⟩

**Blockers.** ⟨class⟩ — ⟨what⟩ · owner ⟨name⟩ · ⟨needed by⟩
**Value.** ⟨share of the epic figure, or "carried at epic level"⟩ · ⟨reliability label⟩
**Depends on.** ⟨story or precondition that must be true first, or "nothing"⟩
**Definition of done.** Development ⟨status⟩ · Implementation ⟨status⟩ · Handover ⟨status⟩

### US-⟨n+1⟩ · ⟨short title⟩

⟨repeat⟩

## Epic acceptance

⟨What is only true across the whole epic — the capability registered against the cluster
template, the old manual route stopped, output data points registered. If it is genuinely
"all stories accepted", write that.⟩

## Open questions

| Question | Who answers | Needed by |
|---|---|---|
| ⟨⟩ | ⟨⟩ | ⟨⟩ |
