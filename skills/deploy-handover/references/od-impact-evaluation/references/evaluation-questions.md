---
type: Skill Reference
title: Evaluation questions
description: The questions to put to the plant owner and the records to read when evaluating a live use case, built from OD's own use case utilization template, the Use Case Canvas success criteria and the integration workshop utilization sessions.
resource: ../procedure.md
status: draft
tags: [use-case-support-service, practice]
---
# Evaluation questions

Sources: OD's "Use Case Utilization" slide template (Standard Agenda folder, one table per
location), the Use Case Canvas page 2 "Success Criteria" block, and the recent Use Case Integration
Workshop decks, all in the knowledge base's Slide Index and Split Slides. Re-open them before quoting wording.

## 1 · OD's utilization description, field by field

The template is a table headed "<LOCATION NAME> USE CASE UTILIZATION" with these columns. Fill one
row per use case with the plant owner.

| Field (as in the template) | Ask | Example text in the template |
|---|---|---|
| Use case name | Which dashboard, application or analytics workflow? | A dashboard for hourly production output of a named assembly cell |
| Who shall use it? | Which department, team or group? | Production, Manufacturing Engineering, Quality |
| Related process | In which recurring meeting or routine? | Daily Gemba level meeting; bi-weekly meeting for process improvements |
| Utilization method | How is it used, in one to three sentences, including the initial state without digital support? | "We use the dashboard in our daily gemba level meetings to review the production output since yesterday to take action on occurred issues" |
| Utilization rate | Daily, Weekly, Monthly, On-Demand or Never | Daily |
| Impact / potential | Low, Medium or High | High |
| Plant management relevant | Yes or No, and why | Yes (customer escalation) |

The integration workshop decks add the question set OD asked in the room: purpose lines read
"Use Case Utilization (Process: who?, how often?, which actions?, etc.)" and "Use Case Feedback
OPEX / Engineering / Production". Ask exactly those three, plus "what do you need that is not
there".

## 2 · Success criteria, from the Use Case Canvas

Page 2 of the Canvas has a Success Criteria block. Two of its questions are directly reusable:
"How do you measure success and failure?" and "How can you quantify the business impact?"
(a third question in the block is cut off in the extraction; open the canvas template before
quoting it). Compare the answer given at definition with the answer today:

| Canvas statement at definition | Today | Gap |
|---|---|---|
| Objective of the use case | ⟨⟩ | ⟨⟩ |
| Success measure and how it is measured | ⟨⟩ | ⟨⟩ |
| Expected users and their contribution | ⟨⟩ | ⟨⟩ |
| Obstacles / risks named | ⟨⟩ | ⟨⟩ |
| Scalability: where else could it apply, what would block it | ⟨⟩ | ⟨⟩ |

## 3 · Questions behind the utilization view

The integration workshop status slides frame each view by the question it answers. Reuse the
pattern: for every view or alert the use case offers, write the question it answers and ask whether
anyone asks it.

| View type (as phrased on the slides) | The question it answers |
|---|---|
| Production view of the last 24 hours up to one week, per machine (parts, stops, cycle times) | What happened during the past hours or days? What should be improved regarding output and stoppages? |
| Andon board, high level, real time | What is happening at the moment? |

If nobody can name the question, the view is a candidate for the ADKAR diagnostic
(`deploy-handover`) or for retirement.

## 4 · Records to read before asking anyone

| Record | What it gives you | Caveat |
|---|---|---|
| Output asset's own usage log (views, queries, exports) | Tier 1 adoption evidence | Not every platform logs it: ⟨which platforms log views⟩ |
| Use case record in the SharePoint list: status, three workflow states, utilization rate, dependency | Declared state | `IMPLEMENTED` is not use |
| Saving rows with reliability, methodology, proven flag | Promise and firmness | Version history carries text the current record does not (`bc-portfolio`) |
| Digitalization Scorecard, Use Case Utilization (monthly) | Utilization trend | No fixed target; trend only (`metrics-scorecard`) |
| Case group note of the use case | Where else it runs, group savings basis | Indicative, AI-grouped, not reviewed by a human |

## 5 · Interview discipline

- Ask for an occasion, not an opinion: "tell me about the last time you used it".
- Write the owner's words, date and role in the record; do not paraphrase into a stronger claim.
- Ask what the owner would lose if it were switched off tomorrow. "Nothing" is a finding.
- Separate what the owner says changed from what the data shows changed; record both and label the
  source of each.
