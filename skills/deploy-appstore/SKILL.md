---
name: deploy-appstore
description: >-
  Prepare and gate deployment of a manufacturing app (Lane 3a): sourcing route, deployment package, release gate with Cyber Security sign-off, handover to rollout. Sign-off human-only.
license: MIT
allowed-tools: Read Grep Glob
metadata:
  id: deploy-appstore
  tier: practice
  lane: lane-3
  new_state_lane: "Lane 3a (3a4, 3a5)"
  new_state_step: "Build or integrate (3a.1 reuse, 3a.2 self-develop, 3a.3 external build, 3a.4 foreign app); Deploy to the platform, acceptance, Cyber Security sign-off"
  department_names: ["deploy-appstore", "Manufacturing-App-Store-Ops", "container-deploy", "deploy-entrygate", "deploy-exitgate"]
  owner_role: human:jakob.gabriel
  tags: [project-support-consultancy, practice, new-state, draft]
  authority_level: draft the deployment package and checklist; deploying to a shared platform is human-approved; Cyber Security sign-off is human-only
  status: draft
  requires: [dept-context]
  composes: [invest-screen, dept-decision-rights, deploy-acceptance, deploy-handover, deploy-it-demand, deploy-cybersec]
  okf:
    type: Agent Skill
    title: App deployment to the platform
    tags: [project-support-consultancy, practice, new-state, draft]
---

# App deployment to the platform

Read `dept-context` first.

**Status: draft.** The department has a drafted engine skill for this step (`Manufacturing-App-Store-Ops`,
GitOps / ArgoCD with a standard Kubernetes manifest set and the HDAS reference instance); its shape and the
OD x IT CMO rules are in [`references/gitops-deployment-shape.md`](references/gitops-deployment-shape.md).
This skill defines the gates and the package and checks a package against that shape. It contains **no
deployment commands**; the department's package is the master for those. Serves 3a.1 and 3a.2, and 3a.3
once the external build is delivered (`deploy-it-demand`).

## Purpose

Defines the gates and the deployment package for putting an app on the platform (routes 3a.1 and 3a.2, and 3a.3 once the external build is delivered), and checks a package against the department's GitOps shape. Use it after the Lane 3 front-end is done and before rollout. It does not deploy.
- **Outputs:** [`references/outputs.md`](references/outputs.md) lists what this skill must deliver, to whom, and when each output is complete.

## Inputs and output

- **In:** the accepted requirement, the tool decision, the business case, the sourcing route and the app's owner and sponsor.
- **Out:** the deployment package ([`assets/deployment-package.md`](assets/deployment-package.md)): app, owner, target, route, data, dependencies, rollback owner, acceptance protocol, gate table and open questions.

Fictional example (names invented for illustration):

```text
App: demo-dashboard, owner role: DBVE, sponsor: plant X (fictional)
Target: IIoT Edge runtime via CMO; route 3a.2
Gate table: protocol drafted; Cyber Security sign-off requested, not granted
Open: lead time, deploy rights (OD lead to supply)
```

If a field is missing or the sign-off is not granted, the package is invalid for release: list the gap with its owner and stop.

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
| [`references/app-manifest-and-release-gate.md`](references/app-manifest-and-release-gate.md) | The proposed app manifest, interface and versioning rules, what the knowledge base does NOT hold, and the release-gate checklist R1 to R11 |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | The deploy step in the chain: source-ownership scenarios, GitOps shape, local preparation checklist, migration and cutover pitfalls, pilot scope limits, back-out gap, handoffs, agent notes |
| [`references/microservice-app-pattern.md`](references/microservice-app-pattern.md) | The service-per-capability pattern (design proposal): event envelope, what each capability service does, contract, config, degradation, shared kernel, composition, where a new request belongs |
| [`assets/deployment-package.md`](assets/deployment-package.md) | The package and gate table to fill per app |

## Where the flow puts it

Lane 3, branch 3a (new system), after the shared front-end (requirements, tool-decision gate, business case). Four sourcing routes:

| Route | Meaning | What this skill does |
|---|---|---|
| 3a.1 Reuse | Deploy an existing codebase or app | Package and gate |
| 3a.2 Self-developed | Build in OD, then deploy | Package and gate; the build is not covered here |
| 3a.3 External | Spec in-house, build externally | Starts with `deploy-it-demand`, then package and gate |
| 3a.4 Integrate | Integrate a foreign app via IT and Cyber Security | Starts with `deploy-it-demand`, then package and gate |

## Procedure

1. **Precondition.** The front-end is done: requirement (`funnel-requirements`), tool decision (`invest-screen`,
   `dept-decision-rights`), business case (`bc-build`), capital approved where needed.
2. **Confirm the target and the route** (above). Record both.
3. **Assemble the deployment package** (ask for source ownership in the supplier contract; otherwise the highest-effort scenario applies, see `references/process-chain-practice.md`): what the app is and who owns it; the plant sponsor; the target; the sourcing route;
   the data it reads and writes (against `systems-of-record`); the dependencies; the rollback owner; the acceptance protocol.
   ⟨Containerization requirements, image and registry rules, resource limits⟩ - to be supplied. A proposed manifest (name, owner, topics consumed and published,
   API description, whether it writes to a machine, identity, Cyber Security review state) is in `references/app-manifest-and-release-gate.md`; it is a design proposal, not the pilot's procedure.
4. **Release gate.** Draft the acceptance protocol with `deploy-acceptance`. Cyber Security sign-off is requested through the
   approval route (`dept-decision-rights`) and is **human-only**. Wait state: ⟨lead time, to be supplied⟩ (the flow marks it as weeks).
5. **Deploy.** A human with deploy rights on the platform does it. This skill does not deploy.
6. **Hand over** to rollout and adoption (`deploy-handover`).

## Output - the deployment package

Fields of step 3, a gate table (protocol drafted, Cyber Security sign-off requested / granted by whom and when, approval
route), and the open questions with their owners.

## Open - what only the OD lead can supply

- ⟨The target platform⟩ and ⟨the deployment procedure⟩, including who holds deploy rights.
- ⟨The Cyber Security requirements for an app⟩ and ⟨the lead time⟩.
- ⟨The release cadence⟩ - the bundle says "per release" without a rhythm; neither the AI deck nor the initiative note gives one.
- ⟨The pilot's scope, plants and exit criteria⟩ - the department deck marks the GitOps deployment as a pilot and says no more.

## Human gate and AI-agent notes

- **Agent may:** assemble and check the package, draft the acceptance protocol, list open points. **Humans decide:** Cyber Security sign-off, the approval route, the person with deploy rights who deploys, and the OD lead for the open items above.
- **Evidence to cite:** the route, the maturity class of each platform element, the gate table.

## Definition of done

The package is complete, the release gate is passed or its gaps are named with owners, a human with deploy rights has deployed, and the hand-over to `deploy-handover` is made.

## Do not

- Write or run a deployment command. None is recorded.
- Treat a missing Cyber Security sign-off as optional, or grant it.
- Deploy to a shared platform without the named human approval.
- Assume the container platform of the flow is the IIoT Edge runtime.
