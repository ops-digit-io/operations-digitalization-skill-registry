---
type: Skill Reference
title: Process chain practice
description: How a flow fault is handled inside the new process chain - where the symptom usually comes from, the handoff contract, ownership signals, platform-change causes, pitfalls, and AI agent operating notes. Process guidance only; no figures.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [node-red, troubleshooting, process-chain, ai-agent]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Process-chain practice

Derived from the Operations Digitalization slide decks, abstracted into process guidance. Examples are illustrative and use
`<placeholders>`. Own synthesis is marked `PROPOSAL`; unknowns are `<...>`. The decks hold little troubleshooting detail; this file
only adds what they support.

## Where it sits

Step **3b5** (procure and connect the machine), when a connected machine's flow does not deliver, and **3b6** (acceptance), when the
end-to-end test fails. Faults reach it also from step **23** or **26** as "the dashboard is flat".

## Handoff contract

| Receives | From | Must be there |
|---|---|---|
| A symptom in the plant's words ("flat since", "wrong value") | `od-acceptance-test`, the dashboard owner, the key user | When it started, what changed |
| The flow export and the tab description | `od-node-red-flow-builder` | The flow-config contract |
| Whether the machine still publishes | `od-data-availability-check` | Step reached |

| Hands on | To | What it carries |
|---|---|---|
| Fix on a test instance, proposed prod change | the human approver | Analyser result, test evidence |
| A signal or topic problem | `od-signal-standardization` | Raised as a data-model change, not patched |
| A connection or machine problem | `od-equipment-integration`, `od-barrier-triage` | Class, owner |
| An ownership gap | `od-decision-routing` | Named gap |
| Triage record | the plant key user | Cheapest checks first, what was ruled out |

## Method in practice

1. **Walk outward from the machine** (as in the skill), but ask first what changed: a redeploy, a platform migration, a firewall or
   network separation, a new software version, a changed machine program.
2. **Check the cheap platform causes before the flow:** the tab is enabled; configuration is in version control and was not lost on
   a runtime redeploy; the machine still publishes; the connection has an owner.
3. **Wrong value, not no value.** A cycle time that looks too short may be a transactional record that shows only the visible part
   of the cycle (overridden start and stop needed); a number off by a factor may be a missing unit conversion; a mismatched
   identifier may be padding or a wrong stored type; a stale lookup may be an unsynchronized mapping file.
4. **After a platform or server migration** the flow itself is rarely the cause: check DNS, certificates for the new names, user
   access carry-over, the runtime licence of the connector or OPC server (bound to one machine; keep the key), the outage window
   and the per-location checklist item.
5. **Run the analyser, read findings in the skill's order,** then the symptom table.

## Ownership signals

Weeks of unanswered follow-ups, an unclear owner for access to a registry or repository, and nobody asking why other sites work
are signs of **missing ownership**, not a technical puzzle. Ask three questions: who is responsible for the connection; what do
the other sites do that works; what is the alternative if it never works. Escalate the gap through `od-decision-routing`; a
hard external deadline (for example a customer audit) outranks internal plans.

## Pitfalls and lessons

- IT architecture changes during a sprint (firewall separation, access for local users) look like flow faults and cost weeks.
- Cyber Security patching and approvals on controllers block waves; a flow fault on a blocked machine is a barrier, not a bug.
- Fixing a data-model problem inside a function hides it from every other plant.
- Treating a quiet dashboard as a flow fault when the machine stopped publishing.

## Questions to ask

- What changed, and when did it last work?
- Is the tab enabled, and is this the deployed version?
- Does the machine publish at all on the topic; does the input uuid appear?
- Wrong value: is a unit, type, padding or mapping step missing?
- Who owns the connection and the access?

## Definition of done

The cause is named in one of: flow, configuration, machine, connector, platform change, ownership; the fix is tested on the test
instance; the triage record is filled; any data-model change is raised, not patched; the plant key user confirmed the asset shows
correct values again.

## AI agent operating notes

- **Can do:** run the analyser over the export; classify the symptom against the table; list recent changes from the ticket thread;
  draft the triage record; detect silent threads and unowned items; propose the cheapest next check.
- **Required inputs:** flow JSON, symptom, last-known-good date, change history.
- **Evidence it must cite:** the analyser check id and node, the symptom row, the thread excerpt.
- **Human gate:** deploying a fix to a production instance; rotating a secret; deciding that a barrier is a roadmap, strategy or
  substitution matter; the escalation wording.
- **Hands over:** the triage record, with fixes only on a test instance, to the approver.
