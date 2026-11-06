---
type: Skill Reference
title: Tiering criteria
description: First mover vs fast follower - the stated criteria, what each tier receives, how to apply them at intake and onboarding, and the open conflict with first-come-first-served wave allocation; open it to tier a plant.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [all, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---

# Plant tiering criteria

No plant is named here. The tier is a **capacity** criterion for central workshops, support and review, **not an
eligibility** criterion. The stated driver is limited central capacity.

## The criteria

| Criterion | First mover | Fast follower |
|---|---|---|
| Estimated value-add | High | Lower or not yet estimated |
| Coverage | Contributes regions, segments or technologies not yet covered | Covered elsewhere |
| Capacity and knowledge in the plant | Present | Limited |
| Integration synergies | Present | Few |
| Key user | A dedicated, staffed key user is nominated | Not (yet) dedicated |
| Central IT / support | Secured | Not secured |

A plant is a **first mover** when the criteria hold together, with the staffed key user as the practical gate
(`PROPOSAL`: treat a missing staffed key user as "fast follower for now", whatever the value estimate, because the
decks make the key user part of the definition). The department-level definition above is authoritative; a
sector-level list that means "whole plant, broad rollout of a manufacturing suite" is background only
(`<to confirm>`).

## What each tier gets

| | First mover | Fast follower |
|---|---|---|
| Central workshops, support and review | First | Only when central capacity allows |
| Projects | Centrally supported | Driven locally |
| Funding for scale-out | Per the normal route | Limited, resource-adjusted |
| Roadmap and use cases | Agreed with OD | From the plant's own local assessment |
| Visits and definition workshops | Priority | Remote or later (`od-workshop-facilitation`) |

Staffing changes the outcome: the same portfolio is projected differently under "central staffing only" and "central
plus dedicated plant key users", mostly through machine connectivity. State the staffing assumption next to every
savings projection.

## How to apply

1. Run it at intake or onboarding (`od-plant-onboarding`, stages 1-3) and re-read when staffing changes.
2. Answer each criterion with its source: list read and date, or a stated answer from a role. Unknown stays `<unknown>`.
3. Propose the tier; the OD lead decides. Record the reason in `assets/plant-gap-diagnosis-record.md`.
4. A fast follower can promote itself by closing the gap: name a staffed key user, secure central IT support, show an
   estimated value. Put those as roadmap rows.
5. Use the tier as an input to ranking (`od-use-case-prioritization`), not as a filter on eligibility.

## Wave allocation

Eligibility follows request order (within a quarter and budget class): a request is never refused because of the
tier. Central capacity goes first to first-mover plants that are staffed; a fast follower is scheduled when capacity is
free. Raise an exception through `od-decision-routing`.

## Pitfalls

- Treating the tier as a quality verdict on the plant.
- Naming a key user who has no time; "dedicated, staffed" means time is available.
- A first-mover plant with a lone technical key user: key user loss is a recurring risk (`od-risk-watch`).
- Letting the tier stand after staffing changed.
