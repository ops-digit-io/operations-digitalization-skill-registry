---
type: Skill Reference
title: Roles and support model
description: Who does what around the IIoT edge and manufacturing suite at a plant according to the operations concept deck - local key user, business-area key user, governance board, central key user, divisional engineering, divisional and local IT, platform provider - plus the incident, change and security-incident flows.
resource: ../procedure.md
status: draft
owner: human:jakob.gabriel
tags: [information-integration-service, lane]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---

# Roles and support model

The lane page speaks of Plant ME and Plant IT. The operations concept for the IIoT edge
computing platform is more specific: it names the roles a plant meets when something has to
be installed, changed or fixed. A local key user needs it to know **who to call and what is
theirs**.

**Source and grade.** One deck: *Operation Concept IIoT and Edge Computing* (the process slides carry the deck's date), described in the vault's `Slide Index` and in the
archive-evidence block of the tool note `Concept 3 - IIoT Edge Computing Platform`
("AI-drafted ... not reviewed by a human"). The Slide Index keeps a snippet of about 400
characters per slide; **several role slides are cut off** (marked "..."). What is listed below
is what the snippets and the tool note show. The full responsibilities per role are in the
deck itself and are open (⟨to read in the archive deck, slides 5 to 21⟩). Use titles as the
deck gives them; the deck does not name individuals here and neither does this file.

## Scope and principle (slides 2 and 3)

- Aim: a well-structured support organisation aligned between local and central teams and the
  external provider(s); maximum standardized implementation of regional or local templates on
  a global base ("if you know one installation, you know the others"); one operations model for
  all teams; clear responsibilities and IT support processes (ITSM).
- **Divisional standard versus local or business-unit support.** A divisional standard
  application (the deck's example is SAP ME) has global IT application management support for
  implementation and operation. A local or business-unit application has **no** such support,
  only local IT infrastructure. Interfaces (read or write access) between managed applications
  and legacy or non-standard applications **need approval by the governance board** (the deck
  says the board is "to be defined").

## Roles (slides 5 to 15)

| Role | Operations, as far as the snippet shows | Implementation projects |
|---|---|---|
| **Local key user** | First-level support together with the plant's manufacturing engineering; escalation to second level (IT service desk); administration and configuration of the local edge device management system; requirements for new data flows and machine integration go to the central requirements management | Planning and participation of machine (OT) connectivity; training of the local team (troubleshooting); further items cut off |
| **Business-area key user** | Review of new IIoT and edge requirements | Central project lead; order clarification (fit/gap analysis of prerequisites); budget planning and resource allocation (for example the local key user); communication to plant key user and local engineering |
| **Governance board** | Requirements steering and approval; review of proposals for new applications and services with deployment on the edge platform | Program steering |
| **Divisional engineering support** | New requirements (change management) | Consultancy; intermediary for communication with an external machine supplier or maintenance service provider (the deck excludes one named internal organisation) |
| **Central key user** | Demand management; managing new requests; prioritization and cost management | Program management |
| **Divisional IT** | Service ownership; new requirements (change management); rollout of a new release of the template | Central project lead IT; coordination of the infrastructure setup process |
| **Local IT** | Operation of local IT infrastructure; backup and restore; operating-system patch management; performance monitoring; access control to local servers and to the production firewall | Provisioning local IT infrastructure: local servers, production firewall, directory service, handling of server certificates |
| **IT application management and platform service provider** | Service owner for ITSM (incident, change, problem management); second-level user help desk; escalation to third level; operation of the cluster and standard API interfaces; access control to platform instances (users and certificates); application patch management | Rollout project management support; installation and initial setup (cut off) |
| **IT infrastructure** | Operation of cloud server infrastructure; backup and restore; OS patch management; performance monitoring; provider management (cost and service contract) | Provisioning of local IT servers: Linux virtual machines for the Kubernetes cluster |

The department's *Decision rights* and *Roles and organization* notes use different labels
(Plant ME, Plant IT, IIAE, OD lead, DBVE). The deck's roles and the registry's roles are **not
mapped to each other in any note read.** ⟨The mapping, for example: is the registry's Plant ME
the deck's local key user? Who could supply it: OD lead.⟩ Until then, use the deck's title when
you talk to IT and the registry's role when you talk to the lane.

## Processes (slides 16 to 21)

The snippets show only the actors, not the steps. What can be read:

| Process | What the snippet shows |
|---|---|
| Incident management | Two paths by who is affected: a key user of the DATATRONiQ-supported platform, and a key user whose problem is outside that scope (for example corporate infrastructure) |
| Regular user revalidation | A central IT key user, "for each plant" |
| Security incident management | Same two paths; "forward to cybersecurity organization", "define resolution", "select checkbox security incident"; the incident is rated priority 1 or 2 before it is flagged as a security incident; the central cybersecurity office is informed automatically from the ticket system |
| Security incident indicators | Missing files on the server; malfunctioning applications or functions; unusual file manipulation; high CPU, memory or disk load; unknown programs; failed login attempts; measurements: regular vulnerability scan, monitoring and alerting of basic system utilization |
| Change management | Actors: local IT key user, change coordinator, the platform provider, business-area key user and the requestor; the change manager assigns cyber security as an additional approver; **approval from cyber security in case of a security change** |

## Using it

1. **Requesting a new data flow or machine integration:** it goes through the local key user
   to the central requirements management; the business-area key user reviews it; the
   governance board approves new applications and services deployed on the edge platform.
   Cross-check with `od-decision-routing` for the department's own gates.
2. **Connecting a legacy or non-standard application to a managed one:** needs governance board
   approval (deck, slide 3). The legacy landscape is in
   [`legacy-applications-landscape.md`](../../../../invest-screen/references/legacy-applications-landscape.md).
3. **A change that touches security** needs cyber-security approval in the change flow.
   Planning an external connection starts with `od-cybersec-gate`.
4. **Support:** first level is the local key user with the plant's manufacturing engineering;
   second level is the IT service desk. Say who the plant's local key user is (role, not
   name) in the plant readiness brief ([`plant-readiness-brief.md`](../../../assets/plant-readiness-brief.md)).

## Sources

- Vault `Slide Index` (deck `Operation Concept IIoT and Edge Computing`, slides 2, 3, 5 to 21), read 2026-11-05.
- Vault `Graph/Tools/Concept 3 - IIoT Edge Computing Platform` archive-evidence block.
