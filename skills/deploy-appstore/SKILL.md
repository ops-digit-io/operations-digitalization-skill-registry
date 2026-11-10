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
  deployment, or when the deploy step of a new system is planned. Checks the package against
  the department's GitOps / ArgoCD deployment shape (standard manifests on CMO, reference instance HDAS).
license: MIT
allowed-tools: Read Grep Glob
metadata:
  id: deploy-appstore
  tier: practice
  lane: lane-3
  new_state_lane: "Lane 3a (3a4, 3a5)"
  new_state_step: "Build or integrate (3a.1 reuse, 3a.2 self-develop, 3a.3 external build, 3a.4 foreign app); Deploy to the platform, acceptance, Cyber Security sign-off"
  owner_role: human:jakob.gabriel
  authority_level: draft the deployment package and checklist; deploying to a shared platform is human-approved; Cyber Security sign-off is human-only
  status: draft
  sources_read: 2026-11-10
  requires: [od-context]
  composes: [od-system-fit-check, od-decision-routing, od-acceptance-test, od-handover-and-adoption, od-it-handover, od-cybersec-gate]
  derived_from:
    - The new-state flow (docs/new-state-flow.md and the four diagrams in docs/new-state/), the Lane 3a step "Deploy to platform + CS", the four 3a options and the gap register entry, read 2026-11-05
    - ops-knowledge-graph/.../10-modules/smart-factory-use-case/systems-of-record.md
    - ops-knowledge-graph/.../20-lanes/project-support-consultancy/skills.md
    - ops-knowledge-graph/.../00-core/08-decision-rights.md
    - Department deck AI_Where_We_Apply_Today.pptx (one slide; the line "Manufacturing App Store - GitOps deployment (pilot)"), text extracted and read 2026-11-05
    - Work vault (Work-OpsDigit-Knowledge), Graph/Keynote Initiatives notes Manufacturing App Store (CMO), AI-Coding Assimilation, Cybersec Backlog Closure and AI Requirements Eng. Pipeline, read 2026-11-05
    - Work vault, Microservice Apps (WIP), the notes Microservice Landscape, Platform Extensibility and Onboarding, Cross-Cutting Platform Concerns, Platform Services (Shared Kernel), Recipe Values Service, User Interfaces and Interaction Layer and Extension Services, AI-drafted and not reviewed, read 2026-11-05
    - Work vault, Graph/Tools (Concept 3, IIoT Edge Computing Platform) and the skill od-equipment-integration reference iiot-edge-platform.md, read 2026-11-05
    - "Work vault, OD Department Knowledge/OD-instance/skills-inventory-and-roadmap.md and OD_Skill_Naming_Convention.md, read 2026-11-10"
    - "Work vault, OD Department Knowledge/OD-instance/20-lanes-newstate-DRAFT/Transcripts/2026-09-11_OD-IT-alignment_meeting-notes.txt, read 2026-11-10"
  okf:
    type: Agent Skill
    title: App deployment to the platform
    tags: [project-support-consultancy, practice, new-state, draft]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---

# App deployment to the platform

Read `od-context` first.

**Status: draft.** The department has a drafted engine skill for this step (`Manufacturing-App-Store-Ops`,
GitOps / ArgoCD with a standard Kubernetes manifest set and the HDAS reference instance); its shape and the
OD x IT CMO rules are in [`references/gitops-deployment-shape.md`](references/gitops-deployment-shape.md).
This skill defines the gates and the package and checks a package against that shape. It contains **no
deployment commands**; the department's package is the master for those. Serves 3a.1 and 3a.2, and 3a.3
once the external build is delivered (`od-it-handover`).

## Which platform

How the sources name the target:

- The knowledge bundle records manufacturing apps and dashboards in the **manufacturing app store on the IIoT Edge
  platform** (the plant Kubernetes runtime), written by the dev team, per release, data owner OD. The Project Support lane
  lists "Manufacturing Apps / app store (IIoT Edge)" with the access "deploy".
- The new-state flow says **"Container Orchestration Platform"**: that is the edge runtime of the IIoT Edge platform (Concept 3); use both terms as synonyms.

Two layers: the app store initiative calls its platform CMO (Container Management and Orchestration: registry, source host, GitOps catalog) and lists the IIoT edge
runtime as a prerequisite that is already deployed; the edge runtime is where the app runs, CMO is how it gets there. Record both in the package.
See `references/platform-and-pilot-status.md`.

**Maturity, checked every time.** Never describe the app store or the platform as more mature than it is. Classify each element as
running, pilot, planned or design-only and look the current status up in the sources named in
[`references/platform-and-pilot-status.md`](references/platform-and-pilot-status.md); this skill does not carry a status snapshot.

## The references

- [`references/gitops-deployment-shape.md`](references/gitops-deployment-shape.md): the GitOps / ArgoCD deployment set the department's skill authors, the CMO standard-manifest rule, the roadmap gate agents.

| File | Use it for |
|---|---|
| [`references/platform-and-pilot-status.md`](references/platform-and-pilot-status.md) | How to classify maturity (running, pilot, planned, design-only) and where to look the current status up; the two layers (edge runtime and app store / CMO); the three onboarding scenarios and their inferred match to routes 3a.1 to 3a.4 |
| [`references/app-manifest-and-release-gate.md`](references/app-manifest-and-release-gate.md) | The proposed app manifest, interface and versioning rules, what the vault does NOT hold, and the release-gate checklist R1 to R11 |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | The deploy step in the chain: source-ownership scenarios, GitOps shape, local preparation checklist, migration and cutover pitfalls, pilot scope limits, back-out gap, handoffs, agent notes |
| [`references/microservice-app-pattern.md`](references/microservice-app-pattern.md) | The service-per-capability pattern (design proposal): event envelope, what each capability service does, contract, config, degradation, shared kernel, composition, where a new request belongs |
| [`assets/deployment-package.md`](assets/deployment-package.md) | The package and gate table to fill per app |

## Where the flow puts it

Lane 3, branch 3a (new system), after the shared front-end (requirements, tool-decision gate, business case). Four sourcing routes:

| Route | Meaning | What this skill does |
|---|---|---|
| 3a.1 Reuse | Deploy an existing codebase or app | Package and gate |
| 3a.2 Self-developed | Build in OD, then deploy | Package and gate; the build is not covered here |
| 3a.3 External | Spec in-house, build externally | Starts with `od-it-handover`, then package and gate |
| 3a.4 Integrate | Integrate a foreign app via IT and Cyber Security | Starts with `od-it-handover`, then package and gate |

## Procedure

1. **Precondition.** The front-end is done: requirement (`od-requirements-breakdown`), tool decision (`od-system-fit-check`,
   `od-decision-routing`), business case (`od-benefit-calculation`), capital approved where needed.
2. **Confirm the target and the route** (above). Record both.
3. **Assemble the deployment package** (ask for source ownership in the supplier contract; otherwise the highest-effort scenario applies, see `references/process-chain-practice.md`): what the app is and who owns it; the plant sponsor; the target; the sourcing route;
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
- ⟨The pilot's scope, plants and exit criteria⟩ - the department deck marks the GitOps deployment as a pilot and says no more.

## Do not

- Write or run a deployment command. None is recorded.
- Treat a missing Cyber Security sign-off as optional, or grant it.
- Deploy to a shared platform without the named human approval.
- Assume the container platform of the flow is the IIoT Edge runtime.
