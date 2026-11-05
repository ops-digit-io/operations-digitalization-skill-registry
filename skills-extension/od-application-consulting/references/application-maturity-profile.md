---
type: Skill Reference
title: Application maturity profile
description: How to read a plant-local or foreign application on the IT/OT focus areas that matter for integration - which areas to rate, what the levels say about integrate, keep or replace, the data path and the run owner.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [project-support-consultancy, practice, maturity, draft]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Application maturity profile - integrate, keep or replace

Source layer: the IT/OT maturity model summarised in `od-maturity-assessment` (rubric, evidence grade, plausibility checks). The mapping to
integrate, keep or replace is `PROPOSAL`, `<to confirm>` with the OD lead. The profile informs the recommendation; the recommendation and its
acceptance stay human.

## Areas that describe an application

| Area | Ask of the application | Why it matters for the recommendation |
|---|---|---|
| F10 Protocols | Which interfaces, open standard or proprietary? | Standard interface: integrate is cheap. Proprietary: each interface is a connector to build and own |
| F2 Communication capabilities | Does it expose data on request only, push events, or offer defined services? | Request-only means a polling gateway; services mean it can be a producer for the data path |
| F16 Information model | Do its names for asset, order, material and signal match the platform's? | Level 1 means a mapping per interface and a cross-plant compatibility risk |
| F12 Information storage | Where is its system of record, and what happens when the network fails? | Decides whether it can be the single source for a data object, and whether an edge buffer is needed |
| F13 Information processing | What logic runs inside it; who can change it? | Logic locked inside an app nobody can change argues for replace or wrap |
| F15 Control structure | Does it plan, sequence or execute? | Execution role overlaps MES territory: back to `od-system-fit-check` |
| F1 System familiarity | Does it identify assets and products by the same IDs as the platform? | Identity mismatch breaks joins across systems |
| F7 and F8 Point of use | Who sees it, on which device, with what HMI? | Adoption and training scope; harmonization effort |

## Reading the profile

- **Integrate** is plausible when F10 is open standard, F16 at least partly continuous, the record sits in a named system and an owner with a support
  level exists. Still check the cross-plant rule and the build path.
- **Keep** is plausible when the app satisfies the need, has a named owner, can be placed on the data path through a gateway, and its profile does not
  make a mapping per interface the main cost.
- **Replace** is plausible when interfaces are proprietary, the model is isolated, logic is locked, no owner or support exists, or it sits in the
  execution role the footprint does not cover; compare with the lighter tool the fit check suggests.
- **Unknown** on F10, F12 or the owner blocks the recommendation: ask the plant, do not design around it.

## Handoff

The profile goes into the design recommendation (data path and run-owner sections) with evidence grade and read date per area. Costs go to
`od-investment-input`, the tool rollout decision to `od-decision-routing`.
