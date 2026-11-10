---
name: od-cybersec-gate
description: >-
  Assemble the sign-off package that goes to Cyber Security / OT before an external machine
  connection or an app deployment - classify the case, list what leaves the machine or the
  plant network and where it lands, collect the evidence the neighbouring skills already
  produce, route the request, and record the wait state and the answer. Drafts and
  recommends only; the Cyber Security sign-off itself is human-only and has no expedited
  path. Use before scheduling a machine connection, before an app goes to the platform,
  when a plant asks what Cyber Security needs, or when a connection waits on sign-off.
license: MIT
allowed-tools: Read Grep Glob
metadata:
  id: od-cybersec-gate
  tier: practice
  lane: [lane-1, lane-3]
  new_state_lane: "Lane 1b (1b3), Lane 3a (3a5), Lane 3b (3b5)"
  new_state_step: "Order and connect; Cyber Security sign-off in parallel; Deploy to the platform, acceptance, Cyber Security sign-off; Procure and connect; Cyber Security sign-off in parallel; execution supplier-dependent"
  owner_role: human:jakob.gabriel
  authority_level: recommend - the Cyber Security sign-off itself is human-only
  status: draft
  sources_read: 2026-11-10
  requires: [od-context]
  composes: [od-equipment-integration, od-decision-routing, od-acceptance-test, deploy-appstore]
  derived_from:
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/OD_Skill_Map.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/20-lanes/information-integration-service/agent-brief.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/20-lanes/information-integration-service/playbook.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/20-lanes/information-integration-service/tasks.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/20-lanes/information-integration-service/skills.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/20-lanes/project-support-consultancy/agent-brief.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/00-core/08-decision-rights.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/00-core/09-risks.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/00-core/15-resources.md
    - Skills od-information-integration-service (guardrails), od-decision-routing (escalation triggers and the cybersecurity worked example), od-equipment-integration (SKILL.md, references barrier-classes, fallbacks, iiot-edge-platform, decision-paths) and deploy-appstore, read 2026-11-05
    - Registry docs/new-state-flow.md and the Mermaid and skill-map diagrams in docs/new-state, the Cyber Security steps of Lanes 1b and 3, read 2026-11-05
    - Work vault (Work-OpsDigit-Knowledge), ODEC Facts notes Tools and Systems (Groot2B, QFPR), Plant - Auburn, Plant - Monterrey and Other (AI news session disclaimer, Shopfloor Applications List); Graph/Tools QFPR and Concept 3; Graph/Legacy Applications (268 notes, aggregate counts); Graph/Registers Blocker Register; Graph/Connectors and Graph/Tools for the connected platforms, read 2026-11-05
    - "Work vault, OD Department Knowledge/OD-instance/20-lanes-newstate-DRAFT/Transcripts/2026-09-11_OD-IT-alignment_meeting-notes.txt, read 2026-11-10"
  okf:
    type: Agent Skill
    title: Cyber Security sign-off gate
    tags: [information-integration-service, practice, new-state, draft]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---

# Cyber Security sign-off gate

Read `od-context` first.

**Status: draft.** The department's own sources fix *that* the gate exists and *who* may not pass it, but
the sign-off standard itself is not collected (`15-resources.md` lists it as `⟨standard doc - to collect, with
Cyber Security⟩`). This skill therefore builds the **request package** and the **wait-state record**. It does
not state what Cyber Security requires, how long it takes, or how to ask. Those are marked `⟨…⟩` below.

## Purpose, trigger, done

- **Trigger.** A machine connection that involves an external connection is planned (Lane 1b "order and connect",
  Lane 3b "procure and connect"), or an app is ready to go to the platform (Lane 3a "deploy to platform + CS").
- **Output.** A completed [`assets/cybersec-signoff-package.md`](assets/cybersec-signoff-package.md), a routed
  decision request, and a dated record of the answer.
- **Done.** The sign-off is recorded as given by a named human with its scope and conditions, or the case is
  held at the wait state with an owner and an escalation date. Never "done" because the work was built.

## The references

| File | Use it for |
|---|---|
| [`references/gate-rules.md`](references/gate-rules.md) | Every rule that governs the gate, one line each with its source: guardrail, decision right, risk row, wait state, what is not collected |
| [`references/package-contents.md`](references/package-contents.md) | What the package holds for a machine connection and for an app deployment, and which existing skill or record already produces each item |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | The gate as a parallel go-live gate: security-relevance questions, request sequence, documentation completeness checklist, PoC scope limits that keep a pilot off the heavy OT path, the data-protection and works-council items, handoffs and agent notes |
| [`references/precedents.md`](references/precedents.md) | Patterns from the department's own record: the Groot2B programme, an app that waited on approval, a plant network-separation case, how application cyber status is recorded, how security shows up in blocker records |

## The rule

**A missing sign-off holds the case. There is no expedited path and no authority level that shortens it.**
(`od-equipment-integration` guardrail; `od-equipment-integration` error paths.) An agent never
connects, never approves an external connection, and never records "signed off" on its own say-so.

The gate is **decoupled and runs in parallel**: start the package alongside planning and build. It blocks only go-live
(the live connection and live operation), not planning, build or an integration wave's preparation.

## Procedure

1. **Classify the case.** Machine connection (A) or app deployment (B). Name the plant, the machine or app, and
   the lane step. For an app, the target platform is itself open - see `deploy-appstore` ("Which platform").
2. **Decide whether it is external - ask, do not assume.** The sources use "external connection" without
   defining it. ⟨Definition of "external connection" for a machine, and of the cases that need a sign-off for an
   app⟩ - to be supplied by the OD lead with Cyber Security. Working rule of this skill (not from a source):
   when in doubt, treat the case as needing the gate and let Cyber Security say otherwise.
3. **Look for an existing cover first.** The department's own strategy bet is to bundle the sign-off with the
   wave or with the MSB rollout at strategic plants rather than ask per machine
   (`od-equipment-integration` `references/fallbacks.md` section 4; `09-risks.md`). Check whether a
   wave-level sign-off exists for this plant and whether this machine or app falls inside its scope.
   ⟨Where wave-level sign-offs are recorded⟩ is not known.
   For a pilot, keep the scope small enough to stay off the heavy OT path and list what is
   deferred (`references/process-chain-practice.md`).
4. **Fill the package** from existing outputs, not from memory: the data path and the integration concept from
   `od-equipment-integration` (assessment or guidance protocol), the app package from `deploy-appstore`, the
   acceptance protocol from `od-acceptance-test`. Use `references/package-contents.md` as the checklist. Leave
   credentials, addresses, certificates and tokens **out of the package**: list that they exist and who holds
   them, never their values.
5. **Route it.** Open a decision request ([`od-decision-routing`](../../skills/od-decision-routing/assets/decision-request.md))
   on the row "Equipment integration go-ahead" (Tandem IIAE with Plant ME / Plant IT, approval yes,
   `execute-with-approval`). Record the sign-off as a **dependency** on the use case or the machine record.
   Where the case involves personal data, worker-performance measurement or a new platform
   record the data-protection and works-council items next to the package (same file).
6. **Submit - by a human.** This skill hands the package to the IIAE or Plant IT.
   ⟨Submission channel, form and the Cyber Security contact role⟩ are not in the sources.
7. **Hold at the wait state.** Record the submission date, the owner of the follow-up and the next check.
   ⟨Typical lead time⟩ is not recorded; the new-state flow marks the step only as "weeks". While waiting, no
   machine goes live, no app is deployed live, no go-live date is promised to the plant; planning and build continue.
8. **Escalate on the triggers**, not on impatience. Technical items stuck beyond one COP cycle go to the OD lead; the
   strategic half of cyber topics (the standard, the posture) goes to the deciding role or forum named in the current approval policy (look up), the project half is COP's
   (`od-decision-routing` `references/escalation-worked-examples.md`). A security gap on a connected asset is
   an immediate escalation to the OD lead and Cyber Security (`09-risks.md`).
9. **Record the answer** in the package: who answered, date, scope (machines or apps covered), conditions,
   validity. Three outcomes:
   - *Granted* - attach it to the acceptance protocol evidence (`od-acceptance-test`), then proceed.
   - *Granted with conditions* - the conditions become open items on the case; re-check before go-live.
   - *Refused* - route the barrier (`od-equipment-integration` `references/barrier-classes.md`); the
     two-path model is "substitute the solution" or "approve and manage it externally" (see precedents).
10. **After go-live** the risk register's early indicator is "non-compliant connection detected". Anything
    found later is escalated, not quietly patched.

## Pre-evaluation and platform-level approval (OD x IT, 2026-09-11)

- **Pre-evaluate before the formal review.** Run this skill's package as a repeatable pre-evaluation that
  names every missing input before Cyber Security sees it: fewer round trips, a team that learns the
  process, less load on Cyber Security. The approach is an open action item (Thomas, Ignacio, aligned with
  Axel); until it is agreed, the package is the pre-evaluation.
- **Approve at platform level where possible.** Once a platform or connectivity pattern (Grafana,
  connectivity, the CMO deployment structure) is approved, an app using the same pattern should not need a
  full review only because it runs on another machine or at another location. The model is an open IT item
  (Ignacio): record which approved pattern a case reuses and ask, do not assume the shortcut.
- **CMO compliance is the preferred route** for apps (`deploy-appstore`).

## Decision table - what blocks what

| Situation | Action | Source |
|---|---|---|
| External connection planned, no sign-off | Hold. No expedited path | `od-equipment-integration` SKILL.md |
| Sign-off requested at wave level | Check the covered scope, then proceed machine by machine inside it | fallbacks.md section 4 |
| Firmware patch required for security | Barrier class; patch before integration | barrier-classes.md |
| Controller cannot do security-compliant communication | A security position, not a preference; the conversation ends | decision-paths.md (S7-300/400) |
| App needs the platform | Same gate, via `deploy-appstore` step 4 | deploy-appstore |
| Sign-off held beyond one COP cycle | Escalate to the OD lead for capacity or priority | escalation-worked-examples.md |

## Open - only the OD lead and Cyber Security can supply

- ⟨The Machine-connection / Cyber Security sign-off standard⟩ (`15-resources.md` owner: OD lead + Cyber Security).
- ⟨What counts as an external connection⟩, ⟨what Cyber Security requires for an app⟩, ⟨lead time⟩, ⟨validity of a sign-off⟩.
- ⟨Who at the plant submits⟩ and ⟨to which Cyber Security role⟩ - roles only, never names.
- The machine-level `cyber_security_status` field has been an open gap in `registry.yaml`; before relying on
  it, check on the live Machine List whether it is filled. Where it is empty, no machine record can show
  whether a sign-off exists.

## Do not

- Do not connect a machine, deploy an app or schedule either on the strength of an unanswered request.
- Do not mark a sign-off granted, or write it as "implied", "verbal" or "covered" without the named answer.
- Do not paste credentials, addresses, certificates or tokens into the package.
- Do not send package contents to an external AI tool: the department's own AI session carried the line
  "Do not Share/Upload company data without Cyber Security approval" (ODEC Facts - Other).
- Do not restate what Cyber Security requires; the standard is not collected. Point to it once it is.
