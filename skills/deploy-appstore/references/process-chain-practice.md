---
type: Skill Reference
title: Process chain practice
description: How the deploy step (3a5) is run in the chain - the three onboarding scenarios and the source-ownership rule, the GitOps chain and deployment set, local preparation checklist, pitfalls from platform rollouts and migrations, PoC scope limits, handoffs and agent notes.
resource: ../SKILL.md
status: draft
tags: [project-support-consultancy, practice, process-chain, draft]
---
# Process-chain practice - deployment to the platform

Derived from the Operations Digitalization slide decks (app-store architecture, platform rollout, migration and community-call decks),
abstracted into process guidance. No figures. The decks hold the shape and the pitfalls of deployment, not commands; this file adds
no commands either. `PROPOSAL` = synthesis not stated in a deck; `<...>` = unknown.

## Where it sits in the chain

3a5 deploy to the platform and Cyber Security (with `od-acceptance-test` and, proposed, `od-cybersec-gate`). Upstream:
`it-demand-package` (3a.3, 3a.4) and `od-system-fit-check`. Downstream: `od-handover-and-adoption`.

## 1 Method in practice

### Scenario decides the effort

| Scenario | What the developer delivers | Effort | Rule |
|---|---|---|---|
| A internal development | Source in Git; continuous integration builds and pushes the image | Lowest, automated | Preferred |
| B external developer owns the code and works in our Git | Source in our Git | Treated as internal once code is delivered | Ask for it in the supplier contract |
| C external developer, no code ownership | Image plus deployment files only | Highest; the cyber-security check weighs most | Accept only if source ownership was not obtainable, and carry its cost |

Matching to the sourcing routes is in `platform-and-pilot-status.md`. The decision rule: **ask for source ownership in the supplier
contract; otherwise scenario C and its cost.**

### The GitOps chain (shape only)

User space (source plus deployment files, or image plus deployment files) -> central (Git as the source of truth, the build pipeline
produces a versioned image in the registry, one folder per app is discovered automatically, a namespace per app) -> local (a
cluster-side delivery tool reconciles Git to the cluster, self-heals and prunes). The deployment set per app: deployment (image,
probes, resources), service, configuration map, namespace. The structure is fixed and declarative, so a coding assistant can draft the
set from a template; a human reviews it.

### Local preparation checklist (platform rollouts stall without it)

Rollouts stalled on reverse proxy, too-small disks, ordering and a cancelled e-signature. For each rollout keep a local preparation
checklist and plan an on-site visit: network and certificates, source repositories and artifact registry, directory integration,
licences, firewall rules, order status, signatures, disk capacity, reverse-proxy and access rules for the users.

### Migration or cutover across plants

Scope per location with the central server team and the application owner; communicate ahead of time; a checklist file with a
traffic light per location; reserve an outage window per location for reconfiguring edge devices and announce that process data and
dashboards are unavailable meanwhile; a location-specific meeting with the key users to verify every migration item after cutover.
Before moving a virtual server check the runtime licence model (an OPC-UA runtime licence can be bound to one machine; keep the key),
and confirm DNS, certificates for new names and user access carry-over. Per application keep a service concept: change and incident
process, connection matrix, roles and responsibilities, risk and gap assessment.

### Notification channels, historization and flows

Notification channels and data historization are IT changes: request them early or an alert use case stalls. Redeploying or upgrading
the flow-runtime container lost production flow configuration; keep flows in version control and check the redeployment impact
before the release. Low-cost sensors over a wide-area radio network with a gateway, delivered through the app store stack, are
positioned as an enabler for simple measurement tasks and use the same channel.

## 2 Decision rules

| Situation | Rule |
|---|---|
| Source ownership unknown | Record scenario C until the contract says otherwise |
| App writes to a machine | Changes the review path (see the manifest field in `app-manifest-and-release-gate.md`) |
| Pilot or proof of concept | State what it does not do (no machine connectivity, no production gateway, deployment unchanged); keep a "used in the pilot" list beside a "deferred, needs further approval" list; time-bound, named users, explicit capacity and evaluation date |
| Tool without an operations concept | Do not deploy productively; business owner, IT owner, service concept, support level first |
| Back-out plan | Required artefact; the decks hold diagrams only with two actors (central IT, central engineering); content is `<...>`; name the owner and the trigger |
| Supplier code | Assume it may be partly AI-generated; security review accordingly |
| Platform choice | Name the target exactly as requested (existing open question); tool status is time-stamped, look it up live |

## 3 Handoff contract

| Direction | Skill | Content |
|---|---|---|
| Receive | `it-demand-package` | Decision of the evaluation board, route, owners, open IT points |
| Receive | `od-system-fit-check` | Sourcing route and scenario, data path, run owner |
| Receive | `od-cybersec-gate` | Package inputs; recorded answer comes back as release evidence |
| Hand on | `od-acceptance-test` | Deployment package and rollback owner |
| Hand on | `od-handover-and-adoption` | Run owner, support level, release notes, training need |

## 4 Pitfalls and lessons

- Customer-driven projects concentrate on the old stack; a migration that pauses it stops benefits and further use-case development at
  once. Check customer deadlines (audits) before taking a line down.
- A location with no legacy baseline (new installation) is the hardest case.
- Separation from a former parent carries over service documentation, contracts and processes: list each as an item with an owner.
- A prototype outside the standard may run only with a path back to the reference architecture.

## 5 Questions to ask and definition of done

Which scenario? Who owns the source? What does the app read and write? Which operations owner and support level exist? What is the
back-out plan and who triggers it? Is the local preparation checklist complete? Is the sign-off recorded by a named human?

Done = package complete, gate table filled, sign-off recorded or held with owner, deploy approved by a named human, rollback owner
named, hand-over to adoption started.

## 6 AI agent operating notes

- **Can do**: draft the deployment set from a template, fill the package and gate table, run the release-gate checklist, run the local
  preparation checklist, monitor open checklist items per location and flag silent threads.
- **Inputs required**: scenario, repository or image reference, manifest fields, probes and resources, configuration, data objects.
- **Evidence to cite**: the checklist row, the contract clause on source ownership, the sign-off record.
- **Human gates**: the deployment to a shared platform (a human with deploy rights), the Cyber Security sign-off (human-only), the
  decision to proceed in the board.
- **Handover**: deployment package and release-gate result to acceptance and adoption.
