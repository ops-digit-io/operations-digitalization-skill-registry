---
name: deploy-appstore
description: >-
  Prepares the deployment package for a manufacturing app on the plant platform (Lane 3a), checks it against the department's GitOps shape and runs the release gate: sourcing route (reuse, self-developed, external, foreign app), maturity of the platform, rollback owner, acceptance protocol, Cyber Security sign-off requested or granted, then handover to rollout. Use after the requirement, tool decision and business case are done and before an app goes to the app store or edge runtime, or when someone asks what is needed to deploy an app. Drafts only; deploying and the sign-off are human-only. Not for building the app, not for the Cyber Security package itself (deploy-cybersec).
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
  tags: [project-support-consultancy, practice, new-state, ready]
  authority_level: draft the deployment package and checklist; deploying to a shared platform is human-approved; Cyber Security sign-off is human-only
  status: ready
  requires: [dept-context]
  composes: [invest-screen, dept-decision-rights, deploy-acceptance, deploy-handover, deploy-cybersec]
  okf:
    type: Agent Skill
    title: App deployment to the platform
    tags: [project-support-consultancy, practice, new-state, ready]
---

# App deployment to the platform

- Read `dept-context` first.

- **Status: ready (awaiting sign-off).** The department has a drafted engine skill for this step (`Manufacturing-App-Store-Ops`, GitOps / ArgoCD with a standard Kubernetes manifest set and the HDAS reference instance);
- its shape and the OD x IT CMO rules are in [`references/gitops-deployment-shape.md`](references/gitops-deployment-shape.md).
- This skill defines the gates and the package and checks a package against that shape.
- It contains **no deployment commands**; the department's package is the master for those.
- Serves 3a.1 and 3a.2, and 3a.3 once the external build is delivered (OpenSpec IT demand, external).

## Purpose

- **Outputs:** [`references/outputs.md`](references/outputs.md) lists what this skill must deliver, to whom, and when each output is complete.
- Defines the gates and the deployment package for putting an app on the platform (routes 3a.1 and 3a.2, and 3a.3 once the external build is delivered), and checks a package against the department's GitOps shape.
- Use it after the Lane 3 front-end is done and before rollout.

## Inputs and output

- **In:** the accepted requirement, the tool decision, the business case, the sourcing route and the app's owner and sponsor.
- **Out:** the deployment package ([`assets/deployment-package.md`](assets/deployment-package.md)): app, owner, target, route, data, dependencies, rollback owner, acceptance protocol, gate table and open questions.

- Fictional example (names invented for illustration):

```text
App: demo-dashboard, owner role: DBVE, sponsor: plant X (fictional)
Target: IIoT Edge runtime via CMO; route 3a.2
Gate table: protocol drafted; Cyber Security sign-off requested, not granted
Open: lead time, deploy rights (OD lead to supply)
```

- If a field is missing or the sign-off is not granted, the package is invalid for release: list the gap with its owner and stop.

## Which platform

- Two layers, both recorded in the package: the **edge runtime** (the flow's "Container Orchestration Platform", where the app runs) and **CMO** (registry, source host, GitOps catalog: how the app gets there).
- Naming, the sources and the status of each layer: `references/platform-and-pilot-status.md`.
- **Maturity, checked every time.** Never describe the app store or the platform as more mature than it is, because pilot status changes and an old claim misleads sponsors into planning on a platform that is not there.
- Classify each element as running, pilot, planned or design-only and look the current status up in `references/platform-and-pilot-status.md`; this skill carries no status snapshot.

## The references

| File | Open when |
|---|---|
| [`references/gitops-deployment-shape.md`](references/gitops-deployment-shape.md) | You check a package against the GitOps / ArgoCD deployment set, the CMO standard-manifest rule and the roadmap gate |
| [`references/platform-and-pilot-status.md`](references/platform-and-pilot-status.md) | You name a target or classify maturity: how to classify it (running, pilot, planned, design-only) and where to look the current status up; the two layers (edge runtime and app store / CMO); the three onboarding scenarios and their inferred match to routes 3a.1 to 3a.4 |
| [`references/app-manifest-and-release-gate.md`](references/app-manifest-and-release-gate.md) | You fill the manifest or run the release gate: the proposed app manifest, interface and versioning rules, what the knowledge base does NOT hold, and the release-gate checklist R1 to R11 |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | You prepare a rollout, a migration across plants or the local checklist: the deploy step in the chain: source-ownership scenarios, GitOps shape, local preparation checklist, migration and cutover pitfalls, pilot scope limits, back-out gap, handoffs, agent notes |
| [`references/microservice-app-pattern.md`](references/microservice-app-pattern.md) | Optional, only when the app implements a standard capability or you ask where a request belongs (design proposal, not the build recipe): the service-per-capability pattern: event envelope, what each capability service does, contract, config, degradation, shared kernel, composition, where a new request belongs |
| [`assets/deployment-package.md`](assets/deployment-package.md) | You start a package: the package and gate table to fill per app |

## Where the flow puts it

| Route | Meaning | What this skill does |
|---|---|---|
| 3a.1 Reuse | Deploy an existing codebase or app | Package and gate |
| 3a.2 Self-developed | Build in OD, then deploy | Package and gate; the build is not covered here |
| 3a.3 External | Spec in-house, build externally | Starts with OpenSpec IT demand (external), then package and gate |
| 3a.4 Integrate | Integrate a foreign app via IT and Cyber Security | Starts with OpenSpec IT demand (external), then package and gate |

## Procedure

1. **Precondition.** The front-end is done: requirement (`funnel-requirements`), tool decision (`invest-screen`,
   `dept-decision-rights`), business case (`bc-build`), capital approved where needed.
2. **Confirm the target and the route** (above). Record both.
3. **Assemble the deployment package** (ask for source ownership in the supplier contract; otherwise the highest-effort scenario applies, see `references/process-chain-practice.md`): what the app is and who owns it; the plant sponsor; the target; the sourcing route;
   - the data it reads and writes (against `systems-of-record`); the dependencies; the rollback owner; the acceptance protocol.
   - Containerization requirements, image and registry rules and resource limits are not recorded in the sources: list them as open questions with an owner (OD lead), do not invent them.
   - A proposed manifest (name, owner, topics consumed and published, API description, whether it writes to a machine, identity, Cyber Security review state) is in `references/app-manifest-and-release-gate.md`; it is a design proposal, not the pilot's procedure.
4. **Release gate.** Draft the acceptance protocol with `deploy-acceptance`. Cyber Security sign-off is requested through the
   approval route (`dept-decision-rights`) and is **human-only**. 
   - Wait state: the flow marks it as weeks; lead time is not recorded, so write it as an open question with an owner.
5. **Deploy.** A human with deploy rights on the platform does it.
6. **Hand over** to rollout and adoption (`deploy-handover`).

## Output - the deployment package

- Fields of step 3, a gate table (protocol drafted, Cyber Security sign-off requested / granted by whom and when, approval route), and the open questions with their owners.

## Human gate and AI-agent notes

- **Agent may:** assemble and check the package, draft the acceptance protocol, list open points. **Humans decide:** Cyber Security sign-off, the approval route, and the person with deploy rights who deploys.
- **Evidence to cite:** the route, the maturity class of each platform element, the gate table.

## Definition of done

- The package is complete, the release gate is passed or its gaps are named with owners, a human with deploy rights has deployed, and the hand-over to `deploy-handover` is made.

## Do not

- Write or run a deployment command. None is recorded.
- Treat a missing Cyber Security sign-off as optional, or grant it.
- Deploy to a shared platform without the named human approval.
- Treat CMO and the edge runtime as one thing: CMO delivers, the edge runtime runs; record both layers.
- Let a migration pause a customer-driven line unchecked: check customer deadlines (audits) before taking a line down.
- Treat a location with no legacy baseline (new installation) as routine; it is the hardest case.
- Run a prototype outside the standard without a path back to the reference architecture.
- Assume source ownership: ask for it in the supplier contract, otherwise the highest-effort scenario applies.

## Outputs

- [`outputs.yaml`](outputs.yaml): required outputs, criteria, checks and sign-offs.
- One run record per call: `python scripts/run_record.py new <skill-id>` (registry root).

## References

| File | Use it for |
|---|---|
| [`references/background.md`](references/background.md) | Context, rationale, examples and notes moved out of this file; never an instruction |
| [`evals/evals.json`](evals/evals.json) | Test cases and trigger queries to run with and without this skill |
