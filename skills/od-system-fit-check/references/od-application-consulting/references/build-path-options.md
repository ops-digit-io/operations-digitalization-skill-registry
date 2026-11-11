---
type: Skill Reference
title: Build path options
description: The four ways an application question can be answered in Lane 3a - reuse, self-develop, external development, integrate a foreign app - with the selecting question, executing skill, gates and what is not yet defined.
resource: ../procedure.md
status: draft
tags: [project-support-consultancy, practice]
---
# Build path options

Source of the four paths: the new-state flow's branch 3a (VSM skill map, read 2026-11-05). The flow says
which skill serves each path; it does not say who decides among them (`⟨open⟩`). The selecting questions
below are this skill's reading of the paths and the lane's gates, not a department rule.

Precondition for all four: the need has passed the footprint check (`od-system-fit-check`) with verdict
"fits" or "redesigned", or an exception has been routed.

| Path | Selecting question | Executed by | Gates it triggers |
|---|---|---|---|
| **3a.1 Available codebase or app** | Is there an app in the app store, a reference solution, or a plant-local app that already does this and can be deployed to this plant? | `deploy-appstore` (draft) | Deploy to the platform, Cyber Security sign-off (step 4a); `od-acceptance-test` |
| **3a.2 New codebase, self-developed** | Is it a flow or dashboard-sized build the OD or plant team can make on the standard stack? | `od-node-red-flow-builder` (flow-type development, built) or `od-analytics-asset-build`, then `deploy-appstore` | Cyber Security; acceptance; handover |
| **3a.3 New codebase, external development** | Is it larger than the team can build, and can the specification be written in-house with a partner building it? | `it-demand-package` and an external developer | IT demand and demand evaluation; Cyber Security; spend (eCR); licensing decision owner `⟨to confirm⟩` |
| **3a.4 Integrate a foreign app** | Is it a third-party or plant-local application whose data or function must be connected rather than rebuilt? | `it-demand-package` | IT demand, Cyber Security; possibly a tool rollout decision |

Recorded design intent for app onboarding (department knowledge base, Manufacturing App Store initiative, Graph/Keynote
Initiatives and its business case, read 2026-11-05): three onboarding scenarios - internal development;
external development with the source owned; external development with no source access - through a
source repository, continuous integration, a container registry and a GitOps tool; infrastructure whose
rollout extent is stated in an initiative deck (look up: Graph/Keynote Initiatives; do not quote it from here). These come from an AI-at-operations business case
(tier and confidence are in the case itself; its own key risk: plants accepting central orchestration),
a proposal and not an approved programme. Use it to understand where 3a is heading, not to promise it.

## How to choose, in order

1. **Reuse before build.** The strategy trade-off "one plant's solution is takeable by the next" and the
   `od-use-case-standardization` rule (search the library first) put reuse first.
2. **Stay on the standard stack.** A need that fits a flow and a dashboard on the edge, the data platform
   and the plant's Grafana is a 3a.2 case; a need that does not is 3a.3 or 3a.4, and costs IT demand time.
3. **Integrate what exists only when rebuilding is worse.** Plant-local apps are mostly tied to one
   machine family (see the legacy application landscape); integrating them means an interface the central
   side must govern.
4. **Escalate when none fits.** A need that no path covers inside the footprint is MES- or EMS-shaped or
   a new tool: it goes to the tool / system rollout decision, with the system-fit record attached.

## What must be in the recommendation per path

| Path | Must state |
|---|---|
| 3a.1 | Which app and version, which plants already run it, the plant owner, the data it needs and where that data comes from |
| 3a.2 | The flow or asset, the standard it follows, who maintains it after hand-over, the test that ends the build |
| 3a.3 | The specification outline, who owns the source, support after delivery, the IT demand and spend route, the licence question |
| 3a.4 | The foreign app and its supplier status, the interface, the Cyber Security route, who supports the interface |

## Open

- `⟨Who decides among 3a.1 to 3a.4⟩` and the criteria; the flow shows them as options after the gate.
- The platform on which apps are deployed ("Container Orchestration Platform" in the VSM skill map) is the edge runtime of the IIoT Edge platform (Concept 3).
- `⟨Lead times⟩` for IT demand, Cyber Security and external development: the flow marks them as weeks
  and leaves the figures open.
