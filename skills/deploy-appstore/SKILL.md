---
name: deploy-appstore
description: >-
  Prepare and gate the deployment of a manufacturing app to the platform (new-state Lane
  3a) - confirm the target and the sourcing route (reuse, self-developed, externally
  developed, integrated foreign app), assemble the deployment package, run the release
  gate including the Cyber Security sign-off, and hand over to rollout. Drafts the package
  and the checklist; deploying to a shared platform is human-approved and the sign-off is
  human-only. Use when an app is ready to go to the manufacturing app store on the IIoT
  Edge platform or the container platform, when someone asks what must be true before a
  deployment, or when the deploy step of a new system is planned. Draft scaffold: the
  platform procedure is not recorded in the sources.
license: Internal — OESL MPEE Operations Digitalization. Not for external distribution.
allowed-tools: Read Grep Glob
metadata:
  id: deploy-appstore
  tier: practice
  lane: project-support-consultancy
  new_state_lane: Lane 3 (3a)
  new_state_step: Deploy to platform + Cyber Security
  owner_role: human:jakob.gabriel
  authority_level: draft the deployment package and checklist; deploying to a shared platform is human-approved; Cyber Security sign-off is human-only
  status: draft
  sources_read: 2026-11-05
  requires: [od-context]
  composes: [od-system-fit-check, od-decision-routing, od-acceptance-test, od-handover-and-adoption, it-demand-package]
  derived_from:
    - The new-state flow (docs/new-state-flow.md and the four diagrams in docs/new-state/), the Lane 3a step "Deploy to platform + CS", the four 3a options and the gap register entry, read 2026-11-05
    - ops-knowledge-graph/.../10-modules/smart-factory-use-case/systems-of-record.md
    - ops-knowledge-graph/.../20-lanes/project-support-consultancy/skills.md
    - ops-knowledge-graph/.../00-core/08-decision-rights.md
    - Department deck AI_Where_We_Apply_Today.pptx (one slide; the line "Manufacturing App Store - GitOps deployment (pilot)"), text extracted and read 2026-11-05
    - Work vault (Work-OpsDigit-Knowledge), Graph/Keynote Initiatives notes Manufacturing App Store (CMO), AI-Coding Assimilation, Cybersec Backlog Closure and AI Requirements Eng. Pipeline, read 2026-11-05
    - Work vault, Microservice Apps (WIP), the notes Microservice Landscape, Platform Extensibility and Onboarding, Cross-Cutting Platform Concerns, Platform Services (Shared Kernel), Recipe Values Service, User Interfaces and Interaction Layer and Extension Services, AI-drafted and not reviewed, read 2026-11-05
    - Work vault, Graph/Tools (Concept 3, IIoT Edge Computing Platform) and the skill od-equipment-integration reference iiot-edge-platform.md, read 2026-11-05
  okf:
    type: Agent Skill
    title: App deployment to the platform
    tags: [project-support-consultancy, practice, new-state, draft]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---

# App deployment to the platform

Read `od-context` first.

**Status: draft scaffold.** The new-state flow names "containerize and deploy an app to the platform, with
Cyber Security sign-off" as a net-new build for Lane 3a. The sources read do not record how a deployment is
done. This skill defines the gates and the package. It contains **no deployment commands**.

## Which platform

Two descriptions exist, and the sources do not say they are the same:

- The knowledge bundle records manufacturing apps and dashboards in the **manufacturing app store on the IIoT Edge
  platform** (the plant Kubernetes runtime), written by the dev team, per release, data owner OD. The Project Support lane
  lists "Manufacturing Apps / app store (IIoT Edge)" with the access "deploy".
- The new-state flow says **"Container Orchestration Platform"** and marks the platform "to confirm".

⟨Is the Container Orchestration Platform of the flow the IIoT Edge plant runtime?⟩ Until the OD lead answers, name the target
exactly as the requester does and record the open question in the package.
**Partial answer from the vault (2026-11-05):** the sources describe two layers, not one. The app store initiative calls its platform CMO (Container Management and
Orchestration: registry, source host, GitOps catalog) and lists the IIoT edge runtime as a prerequisite that is already deployed; the edge runtime is where the app
runs, CMO is how it gets there. The flow's term most likely means CMO, but no source says so - the marker stays. See `references/platform-and-pilot-status.md`.

**Pilot status, stated once.** The manufacturing app store with GitOps deployment is a **pilot** (department AI deck, one line, no date, no plant list).
The wider app-store initiative (X1, "CMO") is **planned**, and the microservice landscape that would use it is **design only**. Details and the table of what is
running, pilot, planned and design-only are in [`references/platform-and-pilot-status.md`](references/platform-and-pilot-status.md).

## The references

| File | Use it for |
|---|---|
| [`references/platform-and-pilot-status.md`](references/platform-and-pilot-status.md) | What is running, pilot, planned, design-only; the two layers (edge runtime and app store / CMO); the three onboarding scenarios and their inferred match to routes 3a.1 to 3a.4 |
| [`references/app-manifest-and-release-gate.md`](references/app-manifest-and-release-gate.md) | The proposed app manifest, interface and versioning rules, what the vault does NOT hold, and the release-gate checklist R1 to R11 |
| [`assets/deployment-package.md`](assets/deployment-package.md) | The package and gate table to fill per app |

## Where the flow puts it

Lane 3, branch 3a (new system), after the shared front-end (requirements, tool-decision gate, business case). Four sourcing routes:

| Route | Meaning | What this skill does |
|---|---|---|
| 3a.1 Reuse | Deploy an existing codebase or app | Package and gate |
| 3a.2 Self-developed | Build in OD, then deploy | Package and gate; the build is not covered here |
| 3a.3 External | Spec in-house, build externally | Starts with `it-demand-package`, then package and gate |
| 3a.4 Integrate | Integrate a foreign app via IT and Cyber Security | Starts with `it-demand-package`, then package and gate |

## Procedure

1. **Precondition.** The front-end is done: requirement (`od-requirements-breakdown`), tool decision (`od-system-fit-check`,
   `od-decision-routing`), business case (`od-benefit-calculation`), capital approved where needed.
2. **Confirm the target and the route** (above). Record both.
3. **Assemble the deployment package**: what the app is and who owns it; the plant sponsor; the target; the sourcing route;
   the data it reads and writes (against `systems-of-record`); the dependencies; the rollback owner; the acceptance protocol.
   ⟨Containerization requirements, image and registry rules, resource limits⟩ - to be supplied. A proposed manifest (name, owner, topics consumed and published,
   API description, whether it writes to a machine, identity, Cyber Security review state) is in `references/app-manifest-and-release-gate.md`; it is a design proposal, not the pilot's procedure.
4. **Release gate.** Draft the acceptance protocol with `od-acceptance-test`. Cyber Security sign-off is requested through the
   approval route (`od-decision-routing`) and is **human-only**. Wait state: ⟨lead time, to be supplied⟩ (the flow marks it as weeks).
5. **Deploy.** A human with deploy rights on the platform does it. This skill does not deploy.
6. **Hand over** to rollout and adoption (`od-handover-and-adoption`).

## Output - the deployment package

Fields of step 3, a gate table (protocol drafted, Cyber Security sign-off requested / granted by whom and when, approval
route), and the open questions with their owners.

## Open - what only the OD lead can supply

- ⟨The target platform⟩ and ⟨the deployment procedure⟩, including who holds deploy rights.
- ⟨The Cyber Security requirements for an app⟩ and ⟨the lead time⟩.
- ⟨The release cadence⟩ - the bundle says "per release" without a rhythm; neither the AI deck nor the initiative note gives one.
- ⟨The pilot's scope, plants and exit criteria⟩ - the deck marks the GitOps deployment as a pilot and says no more.

## Do not

- Write or run a deployment command. None is recorded.
- Treat a missing Cyber Security sign-off as optional, or grant it.
- Deploy to a shared platform without the named human approval.
- Assume the container platform of the flow is the IIoT Edge runtime.
