---
type: Skill Reference
title: Process chain practice
description: How the Cyber Security gate is run in the chain (1b3, 3a5, 3b6) as a parallel track that blocks only go-live - security-relevance questions, the request sequence, documentation completeness, PoC scope limits that keep a pilot off the heavy OT path, the data-protection and works-council notification, handoffs and agent notes.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [information-integration-service, practice, process-chain, draft]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Process-chain practice - the gate as a parallel go-live gate, plus the data-protection gate

Derived from the Operations Digitalization slide decks (platform, tool, community-call and capital-request decks), abstracted into
process guidance. No figures. It adds practice only; it does not state what Cyber Security requires (the standard is not
collected, see `gate-rules.md`). `PROPOSAL` = synthesis not stated in a deck; `<...>` = unknown.

## Where it sits in the chain

1b3 order and connect, 3a5 deploy to the platform and Cyber Security, 3b6 acceptance and Cyber Security. Read it also as a
**parallel track of the integration wave** (see `od-equipment-integration`, practice file): the sign-off is decoupled, runs alongside
planning and build, and blocks only go-live. Start the package early so the scope is known when the wave is ready to go live.

## 1 Method in practice

### Is the case security relevant?

A system is a security-relevant candidate if it connects to central systems or holds relevant data; has a profound impact on
manufacturing; or holds operational or customer data (CSV exports, vision pictures, quality data). For any change ask: does it
affect confidentiality, integrity or availability (downtime excluded), or touch access control, encryption, hardening, network
security, backup and recovery, logging and monitoring, or security services? A yes to either means security relevant. Patch and
update management is part of any approval, also for locally operated solutions.

### Request sequence as seen in practice

1. Inputs prepared for group IT: functions, network, components.
2. Vulnerability scan.
3. Penetration test.
4. Report plus action list.
5. Budget estimate for the fixes.
6. Additional documentation (network and architecture diagrams).
7. Further development or integration.

**Documentation is the known critical path.** Two outcomes exist: substitute the solution, or approve it (possibly with external
management). Prepare the documents for new hardware up front, for example with a hardened operating-system image, so that
approval is a request and not a research task.

### Documentation completeness before the request (PROPOSAL)

Run this checklist before the gate request is routed; it only checks that the documents exist, not what Cyber Security accepts:
network diagram, architecture diagram, component list, data classification, patch plan, hardened image where new hardware is
involved, list of what leaves the machine or plant network and where it lands, back-out plan (see gaps below).

### Prerequisites that recur

- Cloud energy tools: office and shop-floor network separation and certificate-based encrypted traffic between them.
- Firewall rules and VLAN configuration were the recurring delay in a regional security rollout.
- A call for action in four steps: check the project overview and process flow; check own status and missing factors in the shared
  dashboard; contact OD for the remaining steps; implement and finish before the deadline. Operations management sets the
  escalation date.
- OT security handled as application screening, impact analysis and migration planning, owned by the interface-engineer role;
  PLC screening and program collection for knowledge management.
- Vulnerability notice pattern: affected machines are found through the machine list; speed of response is bounded by machine-list
  completeness. Keep the list current as a security task.

## 2 Decision rules

| Situation | Rule |
|---|---|
| Open controller patch or open approval | Hold go-live (the live connection); run the sign-off as a parallel track started early, not a late surprise |
| What does the gate block? | State it on the record: only go-live (the live connection and productive operation). Planning, build, use-case definition and prototype work on existing data continue in parallel |
| Pilot or proof of concept | Keep it small enough to stay off the heavy OT path (next section) |
| New hardware | Documentation and hardened image prepared first |
| Productive rollout of a tool | Operations concept must exist (business owner, IT owner, service concept, roles, change and risk process) |

### Scope limits that keep a proof of concept off the heavy OT path

State in the request what the pilot does **not** do: no machine connectivity, no production gateway, deployment through existing
processes unchanged. Keep two lists side by side in the package: *used in the proof of concept* and *deferred after the proof of
concept, needs further Cyber Security approval*. Pilots are time-bound, software-only, with a named user group, explicit capacity
and an evaluation date that feeds a scale decision. Two decks disagree on whether the framework may later redeploy to machines
through a gateway: the pilot scope is "no gateway"; the gateway is a post-pilot option needing its own approval (`<to confirm>`).
Prove the foundations before the request: cyber assessment status, data protection, no customer data used for model training,
single-sourcing alignment with purchasing. A reorganisation can orphan the security ownership or the central funding path: list
them as open items.

## 3 Data-protection and works-council gate (PROPOSAL as a chain gate)

For a new platform or tool record these items next to the security package; they are asked in 3a5 and, when worker data is
involved, at intake:

- purpose, functions, data fields,
- access rules,
- retention (log data short, process data longer),
- the works-council category (co-determination),
- whether the tool measures worker performance or processes personal data (intake canvas question),
- AI data use: no company data uploaded to an external AI tool without Cyber Security approval.

Structure for worker-performance data: a balancing-of-interests write-up (purpose, necessity, less intrusive alternative,
effect on the worker) can be reused. The notification itself is submitted by a human; the agent only assembles it. Contents of the
local notification form and the works-council categories are `<...>` (not in the decks).

## 4 Handoff contract

| Direction | Skill | Content |
|---|---|---|
| Receive | `od-equipment-integration` | Data path, integration concept, what leaves the machine, connector and route |
| Receive | `deploy-appstore` / `od-application-consulting` | App package, component list, source-ownership scenario, operations concept |
| Receive | `od-capital-request` | Cost line for fixes and the security decision in the capital request checklist |
| Hand on | `od-decision-routing` | Decision request; open conditions |
| Hand on | `od-acceptance-test` | The recorded answer as evidence |
| Hand on | `od-barrier-triage` | A refusal as a barrier class with owner |

## 5 Pitfalls and lessons

- Approval and purchasing lead times are longer than project timelines. Start the request early; never promise a date.
- Platform rollouts stall on reverse proxy, disk size, ordering and a cancelled e-signature: keep a local preparation checklist and
  an on-site visit for each rollout.
- Back-out plans exist per platform component but the decks hold only diagrams with two actors (central IT, central engineering);
  their content is `<...>`. Treat "back-out plan named, owner named" as a required item and its content as a known gap.
- A decision paper lists the decisions with the proposal and the **risk of not deciding**; use that phrasing for conditions that wait.

## 6 Definition of done and questions

Questions: does anything leave the plant network; who holds credentials (never paste them); is there a wave-level cover; what is
the data classification; is a notification to the works council needed? Done = the sign-off is recorded by a named human with scope
and conditions, or the case is held at the wait state with an owner and an escalation date; the documentation checklist is
complete; the data-protection items are recorded.

## 7 AI agent operating notes

- **Can do**: classify the case (machine or app), run the security-relevance questions, run the documentation completeness
  checklist, assemble the package from existing outputs, draft the data-protection items, track the wait state and flag silent
  threads.
- **Inputs required**: data path, component list, diagrams, patch plan, scope of any wave-level sign-off.
- **Evidence to cite**: the existing record each package item came from and its date.
- **Human gates**: the sign-off (human-only, no expedited path), submission, the works-council notification, the credential handling.
- **Handover**: package plus wait-state record; an answer is recorded only when a named human gave it.
