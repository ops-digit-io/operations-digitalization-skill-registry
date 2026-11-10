---
type: Skill Reference
title: Process chain practice
description: How rollout training (steps 1a3, 26, 3a6) is run in the AI-driven chain - the training offer process, plant hands-on training with central material as support, training-need capture, tools-before-pilots, and what an agent may draft. Pattern only, no figures.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [project-support-consultancy, practice, process-chain, draft]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Process-chain practice

Distilled from the Operations Digitalization slide decks, abstracted into process guidance. No company figures. `PROPOSAL`
marks a synthesis; `<...>` is unknown. The decks cover the *offer* of training more than its content; module content stays in
[`curriculum-modules.md`](curriculum-modules.md).

## 1. Method in practice

**Training offer process (what a plant does).** Check the offer overview -> register -> wait for the invitation (sessions are
planned on a regular review cycle) -> join -> give feedback. If nothing fits, state the need and the idea and request a topic.
For those who do not want to wait: self-paced recordings. Training need is raised by request or in the regular project and
community calls.

**Capture training needs as a list** with the fields training, description, requester, status. Typical gaps seen: SQL for
dashboards, the edge platform, dashboard creation and integration in the BI tool, ETL tools, scripting for time-series
transformation. A short survey (level of understanding, expectations for knowledge transfer, wished topics) is analysed in the
next community call.

**Sessions per tool, stepwise from entry to advanced.** Start with hands-on sessions in the plant, in small groups, on the plant's real data; central
material per tool supports them (a recorded central intro may serve as preparation). Content is iterated into self-learning videos; micro-learning (short units),
real-world use-case trainings and structured learning paths by level and function are the stated direction.

**Train the people who will build before they build.** For pilots of new kinds (analytics, AI), train the team on the tools
first (dashboarding, SQL, flow tool, basic modelling), then start with labelled data and first insights. Training is a
precondition of the pilot, not an add-on at its end.

**Training by workshop.** In definition and integration workshops a "how to use the use cases in daily work" slot, anchored
on an example the plant already runs, is the first adoption training. Hands-on use-case creation with key users, and tool
trainings (ticketing, advanced dashboard, data transformation), appear as extra days of a longer visit.

## 2. Decision rules

- **Enabling capacity before rollout.** If the plant has no one who can run the solution, do not schedule the rollout;
  schedule enabling first ("sold a rocket to someone who can't fly it").
- **Plant-specific competence needs plant-specific hands-on.** Training is hands-on in the plant, in small groups, on the
  plant's real data, on the real screen or machine. Central material is support only; a recorded central intro may serve
  as preparation, not as the training.
- **Use a regional or central role to point to training**, with one responsible person per location for digitalisation use
  cases and a know-how item in the regional roadmap.
- **Admin and user training are separate** for any monitoring or data system; the database or data store goes into the backup
  routine in the same step; vendor support is "very important" for complex tools.
- **Marketing and ambassadors:** a use-case marketing template (why, how, can / cannot, example) and a use-case ambassador
  model (central plus plant) were proposed to raise uptake. Treat as optional. `<to confirm>`
- **Do not train for a gate you cannot pass.** Training covers the gate and its routing, not the approval itself.

## 3. Handoff contract

| Receives (from) | Hands on (to) |
|---|---|
| Acceptance protocol, data path to the machine (`od-acceptance-test`), cyber status (`od-cybersec-gate`) | Training package and competence checklist, confirmed by the plant owner |
| Requirements funnel and iterated tag list (`od-analytics-asset-build`) | Key-user hand-down plan; training-need list entries with requester and status |
| Utilisation read (`od-handover-and-adoption`) | Targeted refresher only after the adoption diagnostic names Knowledge or Ability as the barrier |

Completed checklist -> `od-handover-and-adoption` (Knowledge and Ability elements). Single points of failure -> OD lead via
the community call (`od-risk-watch`).

## 4. Pitfalls and lessons

- Calls and training under-used: feedback channels and regular exchange not used, participation missing. Low participation
  correlates with low understanding and low savings.
- Skills held by a single plant person: not done until a second person is named.
- Training on a demo environment and calling it rollout training.
- A key user who leaves within weeks of a handover takes the competence with them; the hand-down must have happened before.
- Training offered but no place where attendance is recorded `<unknown>`.

## 5. Questions to ask / definition of done

- Which decisions will this plant take alone? Who runs it when the trainer leaves? Who can train the next person?
- What is the plant's level of understanding (survey), and what do they want next?
- Done when: each competence is confirmed by the plant with evidence at the point of use; no critical skill rests on one
  person; the need list entry is closed or has an owner.

## 6. AI agent operating notes

- **Can do:** draft the training package from the module catalogue and the role list; turn recordings and call notes into
  short self-learning material and a Q&A list; classify incoming feedback into the question-pack categories (technical issues,
  data-model updates, flows, dashboards, training schedule, connectors, ideas); keep the need list current.
- **Required inputs:** plant roles (roles only), acceptance status, survey answers, session recordings.
- **Human gate:** the plant owner confirms every competence; the trainer role delivers; an agent never marks a person qualified.
- **Evidence to cite:** checklist row, recording or session date, survey source.
- **Hands over:** the filled checklist to `od-handover-and-adoption`.
