---
type: Skill Asset
title: Idea check
description: A plain-language self-fill sheet for anybody with a use case idea - ten questions in the order that saves the most work (has it been done already first), a one-page summary and the next step, with no department jargon. Fill it before talking to OD; "I don't know" is a valid answer.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [lane-2, practice, blank]
generated: { by: claude-code/1, at: 2026-11-10T00:00:00Z }
---
# Idea check: ⟨your idea in one sentence⟩

You do not need to know the department's methods to fill this in. Answer in your own words, say "don't know" where you do not know, and never guess a number: write where it would come from instead. Terms you are unsure about are explained in the vocabulary of `od-context`. The questions are a short form of the full questionnaire (`use-case-definition-questionnaire.md`), which OD uses with you if your idea goes ahead.

## The ten questions, in this order

1. **Has someone already done this?** Look in the Use Case Library and ask the digitalization key user at your plant or at a neighbouring plant. If a plant already runs it and it is catalogued, **stop here**: you do not need a definition, you need to ask for the catalogued use case (`catalog-usecase`, Lane 1).
2. **Is it one need?** Say it in one sentence with no "and". If it needs "and", it is two ideas: fill in one sheet for each.
3. **When in the day does it matter, and how often?** For example the daily shopfloor review of problems, troubleshooting, tracking activities, quality, traceability, energy (`references/vocabulary.md` has the full list). A need that comes up only once is a one-off question for the Process First-Aid Kit, not a use case.
4. **What happens today, and what should happen instead?** Describe the symptom, not the fix. Numbers only if you have them, with their source.
5. **Where, when, who: and where is it fine?** Name the line or station where it happens and a comparable one where it does not, the shift or condition, and who is affected. What differs between the two places is usually the lead.
6. **Why does it happen?** Ask "why" three times. Stop at something someone can act on, not at a person and not at "that is just how it is".
7. **Who would do something differently once it exists, and who would notice if they did not?** Give a role. A screen nobody acts on delivers nothing: the benefit is the decision someone makes differently.
8. **What data would it need, where does it come from, and is that machine connected today?** If the machine is not connected, the first step is a connection, not a use case.
9. **What have you tried, and what else could you do?** Include "do nothing" and a smaller version.
10. **What do you know about size?** How often, how long each time, how many machines or shifts, what one loss costs. Write only what you can source; otherwise write "unknown" and who could tell you.

## One-page summary (fill in from the answers)

| | |
|---|---|
| Idea | ⟨one sentence⟩ |
| Plant and line | ⟨place, not a person⟩ |
| Moment in the day and how often | ⟨…⟩ |
| Today / should be | ⟨…⟩ / ⟨…⟩ |
| Who acts differently (role) and who confirms | ⟨…⟩ / ⟨…⟩ |
| Data and machine, connected today? | ⟨…⟩ / ⟨yes / no / don't know⟩ |
| Already exists? | ⟨where, or no⟩ |
| Size, with its source | ⟨figure and source, or "unknown, ask ⟨role⟩"⟩ |
| What else you could do | ⟨…⟩ |
| Next step | ⟨from the table below⟩ |

## What happens next

| Your answers say | Next step | Who |
|---|---|---|
| It already exists and is catalogued | Ask for it: Lane 1 | Your digitalization key user or your OD contact |
| A new, recurring need on equipment that is already connected | Hand it to OD as a new use case: Lane 2 (a definition workshop, a value estimate, a decision) | Your OD contact |
| It needs new software or a new machine connection | OD routes it to Lane 3 after the requirements | Your OD contact |
| A one-off question | Process First-Aid Kit | Your OD contact |
| No nameable benefit or no link to the plant roadmap, or it needs a system outside the lean standard footprint | OD may decline and will say why and where to go instead | Your OD contact |

Your OD contact is the person named for your region; use the role, not a remembered name. ⟨to confirm: the contact role per region⟩

A first rough estimate of what the idea might be worth is in `od-benefit-calculation` ("First estimate in five steps"). It is a labelled range for your own understanding, not a figure to publish.
