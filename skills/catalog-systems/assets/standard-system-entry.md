---
type: Skill Asset
title: Standard system entry
description: The blank entry for the standardized-system list and the system match record, each pre-filled with the facts the knowledge base carries and with every missing field marked. Copy one per route or per request.
resource: ../SKILL.md
status: draft
tags: [all, practice]
---
# Standard system entry and system match record

## A - The entry (one per route; proposal for the list)

```text
Entry id / date / author (role):
Machine class:   controller vendor ____  model family ____  field protocol ____
Route:           edge (topology 1) / container (2) / aggregation server (3) / OPC UA server already present
Connector(s):    ____ (Connector Overview status: Productive / Idea / Development; utilization USE / NOT AVAILABLE / DO NOT USE)
Guide status:    written in full / TODO / stub / absent         Source: decision-paths.md, rules.json / rules-next.json
Evidence:        machines INTEGRATED through this route ____ at ____ plants (count live on the Machine List, date ____)
Kit contents:    hardware ____  software ____  licences ____                 [knowledge base: not recorded]
Indicative cost: ____                                                       [knowledge base: not recorded]
Lead time:       procurement ____  Cyber Security / OT sign-off ____       [knowledge base: not recorded]
Cyber Security:  status ____                                                [sign-off is human-only]
Blockers known:  (barrier-classes.md; PLC program missing; no approved small edge device)
Validated at:    plants ____
Maintained by:   ____ (role)
Class:           A written + proven / B proven, unwritten / C fallback or single plant / D none
```

Admission rule proposed here (to confirm with the OD lead): class A **and** kit contents, cost and lead time filled in from a source. Until then the entry is a **route candidate** and carries the words "kit not yet defined".

## B - Route-candidate template (illustrative rows; fill the evidence column from a live Machine List count)

| Entry | Route | Guide | Evidence (Machine List, export date ⟨date⟩) | Kit, cost, lead time |
|---|---|---|---|---|
| Siemens S7 / TIA on the edge | topology 1, `DTQ-S7` / `DTQ-TIA` / `DTQ-S7-NET` | ⟨written / TODO / stub⟩ | ⟨machines⟩ at ⟨plants⟩ | large edge device is the only approved hardware; ⟨cost⟩ ⟨lead time⟩ |
| Siemens S7 / TIA on the aggregation server | topology 3, Softing dataFEED, bridge `DTQ-OPCUA` | ⟨status⟩ | ⟨machines⟩ at ⟨plants⟩ | no device at the machine, needs the edge platform behind the server and a driver licence per PLC family unless the extended suite is in place; ⟨cost⟩ ⟨lead time⟩ |
| Rockwell / Allen Bradley on the edge | topology 1, `DTQ-ALLENBRADLEY-ROCKWELL` | ⟨status⟩ | ⟨machines⟩ at ⟨plants⟩ | ⟨kit⟩ ⟨cost⟩ ⟨lead time⟩ |
| Rockwell / Allen Bradley on the aggregation server | topology 3 | ⟨status⟩ | ⟨machines⟩ at ⟨plants⟩ | ⟨kit⟩ ⟨cost⟩ ⟨lead time⟩ |

Any route that is not class A in [validated-routes.md](../references/validated-routes.md) is class B, C or D and gets **no entry** until the procedure is written (B) or a second route is proven (C).

## C - System match record (one per request, branch 1b)

```text
Request / plant / plant owner (role):                 Catalog match record: (from catalog-usecase, pick)
Machine:   name ____  controller ____ model ____  protocol ____  Machine List status: INTEGRATED / NOT INTEGRATED / ONGOING / blank
PLC program in hand?   yes / no (no = cannot connect; fallbacks.md)
OPC UA server already in front of the machine?   yes / no / not known   (cheapest path in the tree)
Plant platforms (tools-and-footprint.md):   edge platform Available? ____  aggregation server Available? ____
Route found:   entry ____  class A / B / C / D
Candidate kit:   ____ | "no standard system" -> Lane 3b via invest-screen
Footprint:   inside / outside (outside -> invest-screen, tool-rollout decision)
Legacy application touched (legacy-application-position.md):   ____ licence ____ support ____ criticality ____
Cost-template inputs:   given: ____   ⟨missing⟩: ____
Approval route (dept-decision-rights):   ____
Cyber Security status:   ⟨not requested / requested on ____ / granted by ____⟩    (human-only)
Next step:   1b order and connect (mi-equipment) -> deploy-acceptance -> apply template and go live (catalog-usecase, go-live)
```

Every ⟨…⟩ is closed by the person named in the SKILL.md "Open" section, not by the agent.
