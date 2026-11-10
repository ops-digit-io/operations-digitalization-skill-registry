---
type: Skill Asset
title: Workshop prep checklist
description: Preparation checklist for an equipment-integration workshop at a plant - inputs, IT and physical access, attendees, agenda order and outputs; to be completed before the visit.
resource: ../procedure.md
status: draft
owner: human:jakob.gabriel
tags: [information-integration-service, practice, template]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Equipment-integration workshop - preparation checklist · `<plant>` · `<date>`

Format and agenda mechanics are in `od-workshop-facilitation`; this list is the machine-integration part.
Mark each item `done`, `open` (owner, week) or `not applicable`.

## Purpose

Start the priority machines: plant tour, PLC overview and machine list (program availability, interfaces,
network), project plan and budget calculation for the next year, use-case requirements from Production,
Engineering and OPEX, application assessment.

## A Inputs to have before the visit

- [ ] Equipment configuration list with technical interfaces (precondition file)
- [ ] Machine list from the use-case definition; machine CVs (latest PLC programs, versions, vendor)
- [ ] Priority list per machine with "best starting point / best stop point"
- [ ] Integration method per machine (edge or non-edge) as a first proposal (`route-choice-per-machine-type`)
- [ ] Examples from other plants for the same process, for the requirements part

## B IT side

- [ ] Access to jump hosts and servers (internal and external support)
- [ ] Firewall rules in place
- [ ] Platform apps running
- [ ] Physical access to all edge devices, including unmounted ones
- [ ] Known gaps listed (operating system, admin rights, support, especially GPU or vision PCs)
- [ ] IT and OT assessments scheduled as separate meetings

## C People

- [ ] Attendees: project manager, machine-integration lead, plant IT, vendor or integrator; optional production, quality, maintenance, process engineering
- [ ] Rollout team staffed in the room, local key user named, lab responsible if lab equipment is in scope
- [ ] Hands-on variant: several machines per day with a daily priority list

## D Agenda order

1. Status of priority equipment and IT infrastructure (network, servers)
2. Project plan and budget
3. Use-case requirements with production, engineering, OPEX
4. Plant tour of priority equipment
5. Side topics (custom connectors for SCADA, PLC or proprietary systems are collected here)
6. Wrap-up: local next steps and central next steps, each with a target window

## E Outputs to capture

- [ ] Updated machine list and baseline; remaining machines with their blocker
- [ ] Use cases per area; IT preconditions
- [ ] Kick-off date fixed; standing rhythm (short regular team meeting, planner board, steering board)
- [ ] Machine list finalised for the capital request (`bc-capital-request`)
- [ ] Tag selection open items ("what needs to be collected?")
- [ ] Barrier log updated (`references/barrier-log-and-cost-of-non-decision.md`)

## F AI agent notes

An agent can pre-fill sections A and E from the machine list and PLC exports, flag open items and draft the
follow-up list. The plant confirms the items; the agent does not request access or change firewall rules.
