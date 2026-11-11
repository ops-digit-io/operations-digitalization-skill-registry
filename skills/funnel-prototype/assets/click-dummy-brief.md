---
type: Skill Asset
title: Click-dummy brief
description: The brief to write before a click-dummy is built - context, screens, mock data, flow, limits and the question it answers - distilled from the Gemba App click-dummy prompt system.
resource: ../SKILL.md
status: draft
tags: [use-case-support-service, template]
---
# Click-dummy brief - ⟨use case name⟩

Structure distilled from the click-dummy template and the worked production-dashboard example in the Gemba App
Claude project export (see [`../references/gemba-app-pilot.md`](../references/gemba-app-pilot.md)). Fill it before
anyone, or any tool, builds. Keep it to one page. A click-dummy is non-functional: layout and flow only.

| | |
|---|---|
| **Use case** | ⟨name, plant, line - from the `funnel-use-case` record⟩ |
| **Requirements it covers** | ⟨requirement ids from `funnel-requirements`; atomic and testable⟩ |
| **Data verdict** | ⟨verdict from `mi-data-availability`⟩ |
| **Author / date** | ⟨role⟩ · ⟨date⟩ |

## 1 · The question this mock-up answers

⟨One sentence, usability or scope, in the plant's words. Example form: "Can a shift supervisor find the open
stoppage and log its cause in under a minute?" If the question is about data or euros, a click-dummy is the wrong tool.⟩

## 2 · Application context

| | |
|---|---|
| **Type** | ⟨dashboard / form / workflow / report / app⟩ |
| **Users** | ⟨roles in the plant: operator, shift supervisor, line leader, maintenance⟩ |
| **Moment of use** | ⟨Daily Gemba / shift check / escalation / other - named⟩ |
| **Main purpose** | ⟨one line⟩ |
| **Key features** | ⟨three to five⟩ |

## 3 · Screens

One block per screen. Three to six screens are enough for a first round.

| Screen | Purpose | Components | User actions and what happens |
|---|---|---|---|
| ⟨1⟩ | ⟨⟩ | ⟨⟩ | ⟨action -> result⟩ |
| ⟨2⟩ | ⟨⟩ | ⟨⟩ | ⟨action -> result⟩ |

## 4 · Mock data

- Invented, realistic, and **marked as example data on the screen**. No real machine ids, no real people, no
  production values.
- Include variety: several statuses, one very long text, one empty list, one error.
- Define the entities and their fields in plain words (machine, event, alert) so the screens agree.

## 5 · Interaction flow

1. ⟨landing state⟩
2. ⟨user action -> result⟩
3. ⟨final state⟩

## 6 · Limits (copy as written)

- Client-side only: no real API calls, no database, no authentication, no connection to a plant system.
- One self-contained file that opens in a browser; a target size under 5 MB.
- Shows loading, empty and error states; works on a phone-sized screen; light and dark if the plant uses both.
- ⟨Tool and stack the OD lead has approved - not stated in the sources⟩

## 7 · Check before showing

- [ ] Every screen is reachable from the navigation
- [ ] Every button gives visible feedback
- [ ] Forms show validation
- [ ] Empty and error states exist
- [ ] Text is readable at the line
- [ ] A user can say what it is for without explanation
- [ ] Example-data marking is visible

## 8 · Not in scope

⟨What the mock-up does not claim: live data, cost, benefit, rollout, hardware.⟩
