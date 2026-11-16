---
type: Skill Reference
title: Background
description: Context, rationale, examples and notes that stood in SKILL.md, moved here unchanged. Open it for the why; it is never an instruction.
resource: ../SKILL.md
status: draft
tags: [background]
---
# Background

## Purpose

This skill takes a use case that has a **request**, a **demand** and a **validated prototype** and derives the business process around it: what changes in the work, who does what, how it is modelled in BPMN, how it is standardised, how people are brought along, where it sits in the process landscape and how it will be checked once it runs. The aim is a process the organisation keeps running after the project team has left.

Text marked **Inference** is reasoning, not a source's statement.

## Example

Fictional example (invented, not a company figure):

If it fails: when the prototype record says "inconclusive", the refusal note names `funnel-prototype` as the place to continue and no model is drawn.

## Outputs and hand-off: the text before outputs.yaml

`process-derivation` delivers a process derivation package: a gate record, a to-be model, the plan to make it last and the landscape entry. It records a proposal for the owner to accept, never a finished process.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Process derivation package | `assets/process-derivation-package.md`, filled | `bc-build` (the change effort and the baseline for the business case); the process owner (a role) | The gate record names the request, the demand and the validated prototype with their records; sections 1 to 9 are filled or say `⟨not recorded⟩` with who supplies it; every design change has evidence or is listed as an open item |
| To-be process model | A BPMN 2.0 file (pattern: `assets/to-be-process.example.bpmn`) | `deploy-handover` (the embedding in step 26); the process owner | `scripts/check_derivation.py` reports no findings; start and end events, named gateways, every task in a lane, an exception path shown |
| Adoption and embedding plan | Section 6 of the package | `deploy-handover`; the plant representative | Every role group of the model has an ADKAR row with evidence, the owner role is named, the review date is set |
| Landscape entry | Section 7 of the package | The owner of the process landscape (a role) | The fields of the entry are filled, the interfaces name the object that crosses, a human owner has accepted it (until then it is a proposal) |
| Refusal note | One paragraph in the package | The role that owns the missing input (use case, demand or prototype) | Names which of the three gate items is missing and what would fill it |

## Handoff

- **Receives from:** `funnel-prototype` (the validation record with result passed), `funnel-use-case` (the defined use case and its request) and `funnel-requirements` (the demand with its requirement and acceptance criteria).
- **Next in the flow:** the package goes to `bc-build` (step 24): the change effort and the redesign effects are evidence for the benefit rows, not a result. The model, the adoption plan and the landscape entry wait for the approval route (`bc-capital-request`, `dept-decision-rights`) and are carried out in step 26 with `deploy-handover`; the use case then enters the catalog with `catalog-usecase`.
- **Stops here when:** one of the three gate items is missing, the prototype result is failed or inconclusive, no role can be named for the process, or a decision that belongs to the OD lead or the Plant ME has not been taken. A refusal is a result, not a failure.

## Open questions

- The skill has not been run on a real validated prototype record; the composition of public methods is this skill's own inference. Run it once on a real record and record what changed.
- Some sources in `public-methods.md` were read in part only (for example abstract only); the review asked for them to be read in full before the skill leaves draft.
