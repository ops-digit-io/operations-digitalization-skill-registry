---
type: Skill Reference
title: Tool decision gate
description: "The Lane 3 tool-decision / IT-footprint gate (the department's investment-screening, od-system-fit-check): the software and IT-footprint hard gate, the route to 3a.1-3a.4 or 3b, the sourcing criteria from the OD x IT alignment, and the verdict words the department already uses."
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [lane-3, gate, it-footprint, sourcing, new-state]
derived_from:
  - "Work vault, OD Department Knowledge/OD-instance/20-lanes-newstate-DRAFT/lane-3-new-system-or-connector.md (front-end step 2, branch 3a options, guardrails), read 2026-11-10"
  - "Work vault, OD Department Knowledge/OD-instance/2026-09-02_OD_Investment_Screen.md (a run of the department's investment-checking skill: involvement classes, de-noise rule, the software / IT-footprint gate in use, verdict legend), read 2026-11-10"
  - "Work vault, OD Department Knowledge/OD-instance/skills-inventory-and-roadmap.md (od-system-fit-check feature list), read 2026-11-10"
  - "Work vault, OD Department Knowledge/OD-instance/20-lanes-newstate-DRAFT/Transcripts/2026-09-11_OD-IT-alignment_meeting-notes.txt (themes 2, 5, 6, 7), read 2026-11-10"
generated: { by: claude-code/1, at: 2026-11-10T00:00:00Z }
---
# Tool decision gate

Lane 3, front-end step 2 (`process.yaml` step 32). The department calls it `investment-screening`
(`od-system-fit-check` under its naming convention) and makes it **mandatory**: no Lane 3 demand leaves the
front-end without it, and it decides which 3a option or 3b the demand takes. The department's packaged
skill (`30-skills/investment-checking.zip`) is the full rubric; this file carries what its recorded run
and the lane file make visible, so the gate can be run from the registry. Where the package says more,
the package wins.

## 1 · Software and IT-footprint hard gate

Run it on every demand, and on every equipment or indirect purchase that rides along with it. The
department's rule of thumb: *any machine, retrofit, camera, laser or marking unit, measuring device or
"device" that includes a computer or software is an OD and Cyber Security item, even when it is booked
as equipment.*

The points the recorded screen checks (the package holds the full eight-point list):

| Check | Trips the gate when |
|---|---|
| Shipped PC or controller | A PC, embedded computer or controller software comes with the purchase |
| Framework or stack | The software rests on a framework or runtime nobody in the estate runs |
| Exposed endpoints | It opens FTP, its own database, OPC or another endpoint to the network |
| Licence | It carries a licence or recurring software cost without a named owner |
| Hosting | Nobody can say where it runs |
| Data ownership | Nobody can say who owns its data or its model |
| Interface | It brings its own proprietary interface instead of a standard one (OPC UA, MQTT, the service bus, the data platform), or duplicates a connector the estate already has |
| Cyber Security status | No Cyber Security clearance before an external connection |

Any open point → verdict **Blocked** until it is closed. "Under-flagging is the expensive error": when
unsure, keep the item and mark it ⟨confirm⟩.

**De-noise.** Commodity IT lifecycle (laptops, printers, generic network or server refresh) and pure
mechanical rows with no controller, data or marking output carry no OD footprint. Count them, do not gate
them.

## 2 · Route the demand

| Route | When | Ownership | Next skill |
|---|---|---|---|
| **3a.1** Available codebase or app to the platform | Existing code or app covers the need; lowest effort | OD + external | `deploy-appstore` |
| **3a.2** New codebase, self-developed | The capability is tied to manufacturing or engineering know-how | OD + external (DevOps via externals) | `deploy-appstore` |
| **3a.3** New codebase, external developer ("guided buy") | Build is needed but not core know-how; IT sets architecture and technology guidelines | OD + external | `it-demand-package`, then `deploy-appstore` |
| **3a.4** Integrate a foreign or other app | A product exists; only integration is needed | IT, Cyber Security gated | `it-demand-package` |
| **3b** New connector | The gap is a machine connection, not software | IIAE; Cyber Security gated | `od-equipment-integration` |
| Lean-footprint redesign | A lighter tool already covers it (section above) | — | back to the calling skill |

### Sourcing criteria (OD x IT, 2026-09-11)

- **Solution-design stage first.** Business and IT look at the need together before anyone commits to
  build or buy: existing product, externally delivered solution, or internal development.
- **Do not become a software house.** Build internally only where the capability is tied to
  manufacturing, operations or engineering expertise. Do not recreate enterprise products.
- **Prefer out-of-the-box cloud services and suitable open source** (messaging, databases, serverless,
  streaming) over custom code when a well-understood service meets the need.
- **Guided buy keeps the code where appropriate**, and is judged on multi-year total cost of ownership.
- **Prefer the CMO deployment path.** An app that fits the CMO (Kubernetes) structure and its standard
  manifests is the preferred route, because Cyber Security can treat it at platform level.

The formal sourcing criteria and TCO rules are an open IT action item (IT and the OD lead). Record
the route as `recommend`, cite these principles, and mark the criteria ⟨to confirm⟩ until published.

## 3 · Verdict

Use the department's own verdict words, so a gate record reads the same as an invest-review screen:

| Verdict | Meaning |
|---|---|
| **Go** | Healthy and standard; proceed on the named route |
| **PoC-first** | Real value; prove small before committing (`od-prototype-poc`) |
| **Reduce-complexity** | Workable; steer to the simpler or standard path |
| **Hold** | Missing business case or blocked dependency; revisit on a named trigger |
| **Blocked** | Software or IT footprint unresolved; clear it before any Go |
| **Engage** | OD should co-own or advise; not a spend gate |

The gate recommends. The tool or system rollout decision stays with the OD lead and the decision rights
in `od-decision-routing`. A failed gate holds the demand in the front-end: re-scope or reject, never pass
an under-specified demand on.
