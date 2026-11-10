---
type: Skill Reference
title: GitOps deployment shape
description: "What the department records about its drafted App-Store deployment skill (Manufacturing-App-Store-Ops, renamed deploy-appstore): GitOps / ArgoCD, the Kubernetes manifest set, PostgreSQL with a migration job, sub-path-aware ingress, manual secrets, the HDAS reference instance, and the OD x IT CMO rules. Shape only, no commands."
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [lane-3a, deployment, cmo, gitops]
derived_from:
  - "Work vault, OD Department Knowledge/OD-instance/skills-inventory-and-roadmap.md (deploy-appstore: traditional process, features, Copilot portability), read 2026-11-10"
  - "Work vault, OD Department Knowledge/OD-instance/OD_Skill_Naming_Convention.md (Manufacturing-App-Store-Ops renamed deploy-appstore; GitOps / ArgoCD; reference instance HDAS), read 2026-11-10"
  - "Work vault, OD Department Knowledge/OD-instance/20-lanes-newstate-DRAFT/Transcripts/2026-09-11_OD-IT-alignment_meeting-notes.txt (theme 2, CMO and standard manifests), read 2026-11-10"
generated: { by: claude-code/1, at: 2026-11-10T00:00:00Z }
---
# GitOps deployment shape

The department holds a drafted engine skill for this step (`Manufacturing-App-Store-Ops`, renamed
`deploy-appstore` under its naming convention; "Copilot portability confirmed"). Its package was not
available to this registry; this file records the shape the department describes so the release gate can
check a package against it. The department's package is the master for the commands.

## The deployment set

| Part | What the department's skill authors |
|---|---|
| Delivery | GitOps: the app's manifests live in a repository; ArgoCD syncs them to the cluster |
| Namespace and base objects | Namespace, infrastructure and service manifests |
| Database | PostgreSQL as a StatefulSet, plus a migration Job |
| Ingress | Traefik ingress, aware of the sub-path the app is served under (base path) |
| Secrets | Created manually, not committed |
| Reference instance | HDAS: the worked example to copy from |

The traditional process it replaces: hand-written Kubernetes manifests, error-prone ingress and secrets,
expert-bound and not repeatable by key users.

## CMO rules from the OD x IT alignment (2026-09-11)

- **Standard manifests.** Apps entering the cluster use the standardized manifests, giving a consistent
  deployment structure; a supplier or internal app that conforms is accepted faster.
- **CMO compliance is the preferred route**, because Cyber Security can approve at platform level
  (`od-cybersec-gate`) instead of reviewing every similar app.
- **Keep the capability in house**: CMO knowledge is worth retaining given distributed plants and central
  governance. The CMO target blueprint (scope across plants, hybrid scenarios) is an open IT item
  (IT).

## Department roadmap items that build on it

Open the skill to key users with guardrails; an entry-gate agent (containerized, interfaces, hosting
checked before build); an exit-gate agent (manifests, ingress base path, secrets and standards checked
before go-live); Git pipeline scaffolding from templates. None of these exist yet.
