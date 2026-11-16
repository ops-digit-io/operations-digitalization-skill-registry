---
type: Skill Reference
title: Adoption and embedding
description: How the skill plans for the process to be lived, not only designed - standard work for repetitive tasks, the adoption plan per role group, a change-control checklist for processes that touch plant operation, and the signs that a change did not take hold. Open it for steps 6 and 7.
resource: ../SKILL.md
status: draft
tags: [process-derivation, adoption, change]
---
# Adoption and embedding

Source keys [PDn] are listed in `public-methods.md`. **Inference** marks this skill's own reasoning. The redesign paper says it does not cover "behavioral or change management aspects" [PD2]; this file is where the skill adds them from other public sources.

## Step 6: standard work, where the work is repetitive

Standardized work is "precise procedures for each operator's work in a production process", built on takt time, the work sequence and the standard inventory [PD9]. Once established and displayed at workstations it "is the object of continuous improvement through kaizen" [PD9].

- **Use** it when the to-be process contains repetitive operator or shift tasks (recording a reason, a check, a hand-over).
- **Write** for each such task: the sequence, the role, the trigger and what the use case shows at that moment. Takt time only where the work is paced by demand; if no demand rate is recorded write `⟨not recorded⟩`, never a guess.
- **Post** it where the work happens, and name who may change it. **Inference:** a standard nobody may change is ignored; a standard anybody may change is not a standard. Name the role that approves a change and the interval at which it is reviewed.
- **Do not** use it for knowledge work that has no fixed sequence; use the case model in `derivation-method.md` or no standard at all.

## Step 7: the adoption plan

Two public frameworks, used at two scales. Both are vendor pages (tier 4) and nothing about their effectiveness is claimed.

**Per role group: ADKAR [PD10].** "ADKAR is a model for individual change." The elements are Awareness, Desire, Knowledge, Ability, Reinforcement; they are "sequential but not linear", and the guidance is to "identify where progress is blocked and focus support on the earliest unmet element." [PD10]

| Role group of the to-be process | Earliest unmet element today | Evidence (a statement, an observation, a prototype session) | Action and owner (a role) |
|---|---|---|---|
| ⟨e.g. shift lead⟩ | ⟨Awareness / Desire / Knowledge / Ability / Reinforcement⟩ | ⟨what shows it⟩ | ⟨what is done, by which role⟩ |

Fill one row per role group of the model. **Inference:** the evidence column is the control point. A plan that rates every group "Awareness" from habit is a template, not an assessment.

**Programme level: Kotter [PD11].** The page names eight steps: Create A Sense of Urgency; Build A Guiding Coalition; Form A Strategic Vision; Enlist A Volunteer Army; Enable Action By Removing Barriers; Generate Short-Term Wins; Sustain Acceleration; Institute Change. **Inference:** use them as a check on the programme around the process, not per task: is there a sponsor with authority (coalition), is the barrier list owned (removing barriers), is there a first result to show (short-term win), and who holds the change after the project (institute change). One use case rarely needs all eight; say which you used and why.

## Change control for processes that touch plant operation

A checklist pattern, not a legal duty. 29 CFR 1910.119(l) requires written procedures to manage changes (except "replacements in kind") and says they must address before any change [PD12]:

1. the technical basis for the proposed change,
2. the impact of the change on safety and health,
3. modifications to operating procedures,
4. the necessary time period for the change, and
5. authorization requirements for the proposed change.

Affected employees "shall be informed of, and trained in, the change prior to start-up" [PD12].

**Use** the five points as headings in the package when the process changes how a line, a machine or a safety-relevant task is operated. **Do not** write that the regulation applies: it covers processes defined in its paragraph (a) [PD12]. The plant's safety role names the local requirement. If the process only moves information (a report, a data entry), the checklist is usually not needed; say that in one line.

## Embedding: what makes it last (Inference)

The sources describe change as a path with a barrier point [PD10] and as a programme that ends by "Institute Change" [PD11]. For this skill the following must exist before the process is called embedded:

- an **owner role** for the process, not the project team;
- the **standard** (where there is one) posted and a named role who can change it;
- **training** done for the role groups whose ADKAR row said Knowledge or Ability;
- the **monitoring** of `landscape-and-monitoring.md` running, with a first review date;
- the old way **switched off** or explicitly allowed as a fallback, written down.

Signs the change did not take hold (collect them at the first review): people keep a side list or spreadsheet; the use case output is open but not acted on; exceptions are handled outside the model; the owner cannot say who last changed the standard.
