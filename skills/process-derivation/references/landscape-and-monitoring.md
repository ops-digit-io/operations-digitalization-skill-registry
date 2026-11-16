---
type: Skill Reference
title: Landscape and monitoring
description: How to hook the derived process into the organisation's BPMN process landscape and how to design its monitoring so it can be checked later - placement level, reference numbers, interfaces, event data, review cadence. Open it for steps 8 and 9.
resource: ../SKILL.md
status: draft
tags: [process-derivation, landscape, monitoring]
---
# Landscape and monitoring

Source keys [PDn] are listed in `public-methods.md`. **Inference** marks this skill's own reasoning.

## Step 8: hook the process into the landscape

The department does not define a process landscape in this registry. Ask the owner which one the organisation uses and record it; if none exists, say so and use the placement rules below as a proposal.

**Placement levels.** The APQC framework has five levels: category (13 at the top), process group, process, activity, task; "a process is defined by the activities underneath it" [PD7]. **Inference:** a derived business process is a Level 3 **process**; the activities inside it are the steps of the BPMN diagram; tasks are the standard-work lines. If the derived process is smaller than the landscape's smallest process, it becomes an activity of an existing process, and the existing process model changes instead.

**Order is not implied.** APQC says its numbering "does not imply that process elements occur in a certain order" [PD7]. The sequence lives in the BPMN model, not in the numbers.

**Reference numbers.** In the framework each element has a unique five-digit reference number so organisations can rename processes "but keep the reference numbers" [PD7]. **Inference:** give the derived process one stable id and keep it when the name changes; record the parent (the process group it belongs to), the id of the use case in `catalog-usecase`, and the version.

| Field of the landscape entry | Content |
|---|---|
| Process id | ⟨stable id from the organisation's landscape or a proposed one⟩ |
| Name | ⟨verb and object⟩ |
| Level and parent | ⟨level, parent process group⟩ |
| Owner role | ⟨role, never a person⟩ |
| Model | ⟨path of the BPMN file, version, date⟩ |
| Interfaces | ⟨upstream process and what it hands over; downstream process and what it receives⟩ |
| Use case | ⟨use case id and the skill chain that produced it⟩ |
| Standard work | ⟨path or `none`, with the reason⟩ |
| Review | ⟨next review date and the role that reviews⟩ |

Interfaces are where processes in a landscape break. For each, name the **message or data object** that crosses (BPMN shows it as a message flow or data object [PD3]); an interface with no named object is open.

## Step 9: monitoring designed now

The Process Mining Manifesto aims at improving "(re)design, control, and support of operational business processes" [PD13]. Its guiding principles are the checklist for this step:

| Principle [PD13] | Question to answer in the package |
|---|---|
| GP1 Event data should be treated as first-class citizens | Which events does the use case system record, with which timestamp and case id? If none, the process cannot be checked later; write it as an open item |
| GP2 Log extraction should be driven by questions | Which three questions will the owner ask of the live process? Extract only what answers them |
| GP3 Concurrency, choice and other basic control-flow constructs should be supported | Does the model contain parallel paths and choices the data can show? Name them |
| GP4 Events should be related to model elements | Which event maps to which task or event of the BPMN model? Write the mapping table |
| GP5 Models should be treated as purposeful abstractions of reality | Which differences between model and practice are acceptable, and which are not? |
| GP6 Process mining should be a continuous process | Who looks at the comparison, how often, and what triggers a model change? |

The manifesto also lists "Dealing with Concept Drift" as a challenge (C4) [PD13]. **Inference:** a process changes after go-live; write a review interval and the trigger for a new version (a new machine, a new role, repeated exceptions).

**Do not** promise that process mining will be run. The skill only prepares the data and the questions; running it is a separate piece of work for a role that has the event data. Put the indicators the owner reads (counts, waits, exception rate) into `metrics-scorecard` where it is used; give each one a source and a date or mark it `⟨to collect⟩`.

## What counts as hooked in

The landscape entry is complete, the model is in the landscape's repository under that id, the interfaces name their objects, and a human owner has accepted the entry. Until then the process is a proposal.
