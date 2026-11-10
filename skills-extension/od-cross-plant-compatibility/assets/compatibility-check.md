---
type: Skill Asset
title: Compatibility check
description: The output of the cross-plant compatibility check - subject, plant grid with a verdict per plant, mappings, findings and the recommendation to route.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [information-integration-service, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---

# Compatibility check

Procedure: [`../SKILL.md`](../SKILL.md). Tests: [`../references/compatibility-tests.md`](../references/compatibility-tests.md).
Authority level: recommend.

## 1. Subject

| Field | Entry |
|---|---|
| Capability (one of eleven) | ⟨e.g. the capability template name⟩ |
| Standard under test | ⟨signal set / data model / flow / dashboard / library entry, with the reference to its source document⟩ |
| First plant, and evidence from it | ⟨plant, report reference⟩ |
| Plants in scope | ⟨all instantiating the capability, or the stated subset and why⟩ |
| Prepared by (role) / date | ⟨role, YYYY-MM-DD⟩ |
| Snapshot date of the plant data used | ⟨date of the Machine List / Tool Overview extract⟩ |

## 2. Plant grid

One row per plant in scope. Verdict values: consumable · consumable with mapping · not consumable · unknown.

| Plant | Region | Controller vendor(s) | Field network | Ingress route | Tools relevant | Tag language | Capability instance state | Tests run | Verdict | Evidence / mapping ref |
|---|---|---|---|---|---|---|---|---|---|---|
| ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨IIoT Edge / central OPC UA / evaluation⟩ | ⟨⟩ | ⟨or "not recorded"⟩ | ⟨none / idea / planned / implemented / productive⟩ | ⟨T1 ... ⟩ | ⟨⟩ | ⟨⟩ |

Tally: consumable ⟨n⟩ · with mapping ⟨n⟩ · not consumable ⟨n⟩ · unknown ⟨n⟩ · of ⟨N⟩ plants in scope.

## 3. Mappings written

| Plant | Local | Standard | Where it lives | Owner role | Date |
|---|---|---|---|---|---|
| ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ |

## 4. Findings against the standard

| # | Finding | Plants affected | Fix: change the standard / add a mapping rule / narrow the scope |
|---|---|---|---|
| 1 | ⟨⟩ | ⟨⟩ | ⟨⟩ |

## 5. Recommendation

| Field | Entry |
|---|---|
| Recommendation | ⟨standard for all in-scope plants / standard for the checked plants only / not yet a standard⟩ |
| Plants it does not cover, and the evidence that would resolve each | ⟨⟩ |
| Decision owner and mode | IIAE, consultation; for a tool or system rollout, in tandem with the IT-responsible role of the business side (`08-decision-rights.md`) |
| Forum | ⟨COP if a data model or connector changes; the deciding role or forum named in the current approval policy (look up) if rollout or priority⟩ |
| Routed with | `od-decision-routing`, `assets/decision-request.md` |
| Handed to the catalog? | ⟨yes: grid passed to `catalog-usecase` / no⟩ |

## 6. Still open

⟨consumer inventory, tag languages, tool versions not recorded, plants with no machine records⟩
