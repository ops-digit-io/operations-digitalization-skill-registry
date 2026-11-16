---
type: Skill Reference
title: Derivation method
description: How to get from a validated prototype to a to-be process model - reading the prototype as as-is evidence, the redesign checklist, the BPMN modelling rules the skill applies, and when a decision table or a case model is better than a flow. Open it for steps 3 to 5 of the procedure.
resource: ../SKILL.md
status: draft
tags: [process-derivation, redesign, bpmn]
---
# Derivation method

Source keys [PDn] are listed in `public-methods.md`. Text marked **Inference** is this skill's own reasoning from those sources, not something a source says.

## Step 3: the prototype is the as-is evidence

The BPM lifecycle runs identification, discovery, analysis, redesign, implementation, monitoring [PD1]. A validated prototype has already done part of discovery: it showed what users did and said. Read the validation record for four things and write each in the package:

| Read from the validation record | Write in the package |
|---|---|
| What the user did with the prototype, step by step | The as-is sequence the use case will replace or extend |
| Which roles took part | The roles of the to-be process (a role, never a person) |
| What the pass criterion was and what the result said | The reason the process is worth changing |
| What the prototype did **not** test (mock data, no integration, one shift) | The open items the process model must not hide |

**Inference:** do not start a new interview round if the record answers these. Ask the plant validator only for what is missing, and mark it `⟨to confirm⟩` until answered.

## Step 4: the question the redesign answers

Write one sentence: "Today <role> does <work> with <system or paper>; after the change <role> does <work> with <use case output>." A process change that cannot be said this way is not yet understood. **Inference:** if the sentence needs "and also" twice, split it into two processes.

## Step 4 (continued): the redesign checklist

The redesign heuristics of Reijers and Liman Mansar are offered as "a check list for process redesign" and are judged on cost, flexibility, time and quality [PD2]. The paper's abstract says the emphasis is "on the mechanics of the process, rather than on behavioral or change management aspects" [PD2]. Use them that way:

1. Take the as-is sequence from step 3.
2. For each activity ask which redesign heuristic from the paper applies (the paper holds the list; open the full text, the abstract has no list). Write the heuristic by its name in the paper, not a paraphrase.
3. For each candidate change write the expected effect on **cost, flexibility, time and quality**, qualitatively, with the evidence (prototype result, plant statement) or `⟨not evidenced⟩`.
4. Keep only changes with evidence. A change without evidence is an open item, not a design decision.
5. **Inference:** the four dimensions often pull against each other (a faster path can cost flexibility). Write the trade-off in one line so the owner decides it knowingly.

Numbers: never invent a time or a cost. A figure is allowed only from the validation record or a named plant source, with its place.

## Step 5: model the to-be process in BPMN

BPMN 2.0 is the notation [PD3]; ISO/IEC 19510:2013 is the ISO standard for it (the IEC page says it is identical to BPMN 2.0.1) [PD4]. Rules this skill applies (**Inference**, standard good practice for readable models, not requirements of the standard):

- One pool for the organisation or the plant; one lane per role. Every task sits in a lane.
- Exactly one start event per process and at least one end event; name every event by what has happened ("Downtime detected"), every task by verb and object ("Record reason").
- A gateway that splits has a name (a question) and every outgoing flow has a label (the answer). No unlabelled exclusive split.
- Show the exception path next to the happy path: what happens if the data is missing, if the reason is unknown, if nobody answers. A to-be model without exceptions is a prototype.
- External waits are timer or message events, so the model shows where the process depends on someone else.
- One level of detail per diagram. If a task needs more than a sentence, make it a collapsed sub-process with its own diagram.
- Name the use case's output where it enters the process (a data object or a message), so the link to the use case is visible.

Check the file with `scripts/check_derivation.py` before anyone reads it.

## Step 5 (continued): decision table or case model instead of a flow

- **DMN** gives "two tools for modeling decision-making: a graphical notation and an expression language" [PD6]. **Inference:** use a decision table when a gateway chain would decide on more than two inputs, or when the rule will change more often than the flow.
- **CMMN** defines "a common meta-model and notation for modeling and graphically expressing a Case" [PD5]. **Inference:** use it only when the course of work cannot be fixed in advance (investigation, exception handling). A routine use case does not need it.
- Both are optional. If used, the package names the file and the process model calls the decision or case by name.

## Plant process descriptions

For a technical plant process (material, energy, information flow through machines) some departments use VDI/VDE 3682 [PD8]. Only its catalogue page was read, and it says the guideline is being revised. Use it only if the plant already works with it; do not introduce it for one use case.

## Stop conditions

Stop and return to the sender if: the validation record says "inconclusive" or "failed"; the roles of the process cannot be named; the change needs a decision that belongs to the Plant ME or the OD lead (`dept-decision-rights`) and has not been taken.
