---
type: Skill Reference
title: Process chain practice
description: Recurring blocker patterns from the decks mapped onto the seven barrier classes, the ownership signals that show a stuck case early, the blocker one-pager, barrier reporting with cost of non-decision, handoffs and agent notes.
resource: ../procedure.md
status: draft
tags: [information-integration-service, practice, process-chain, draft]
---
# Process-chain practice - recurring blockers and how to spot them early

Derived from the Operations Digitalization slide decks (gap analysis, strategy, community-call, rollout and blocker decks), abstracted
into process guidance. No figures. The class list is the one in `classes-and-routes.md` (a proposal, not yet confirmed by the OD
lead); this file maps recurring patterns onto it. `PROPOSAL` = synthesis not stated in a deck; `<...>` = unknown.

## Where it sits in the chain

3b4 (proposed), 1b3 and every step where a case stalls. Triage runs when a case has no route or a wait that no one owns.

## 1 Method in practice

### Patterns from the decks mapped to the classes

| Pattern seen in the decks | Class | Early tell | Exit |
|---|---|---|---|
| Machine list not updated; vendor, controller or patch status unknown | C1 information missing | Blank fields on the list; response to a vulnerability notice is slow | Roadmap; fix the list first |
| Old device signals incompatible with the bus or logger; old HMI hard to connect | C6 legacy limit | Compatibility not checked before the cost line | Substitution or replacement through `bc-cost` |
| Controller patch or approval open; second wave blocked | C3 security gate | Sign-off scope unknown at wave planning | Roadmap (go-live hold); parallel track, start the package early |
| Connectivity budget approved, plant lacks resources or skill | C2 owner, window or will | Plant resource rating "average" or "insufficient" | Roadmap; capability gap to the OD lead |
| Tool rolled out or requested, nobody runs it | C4 platform missing, operations concept | No named business owner, IT owner, service concept or support level | Strategy: tool rollout decision; no rollout on demand until the concept exists |
| Protocol outside the connector set; branch not written | C5 no route | Branch marked unwritten in the guide | Substitution or connector development; name dependent use cases |
| Data connected but not comparable across plants | C7 data model | Tags follow the PLC layout | `mi-signals` |
| Machines relocated repeatedly; area layout unstable | C2 (no stable window) | Layout changed more than once | Hold until the area is stable |
| Hardest machines first burned the local project | not a class; a sequencing error | The plan starts with the unknown types | Re-plan: known machine types first, at most one unknown type per deployment |
| Platform rollout waits on reverse proxy, disk, order, cancelled e-signature | C4 platform missing | No local preparation checklist | Roadmap with checklist; on-site visit |

### The recurring blocker: a tool without an operations concept

"Operations concept missing" was the most repeated barrier in the tool landscape review. It is a **service gap**, not a connection
problem and not a use case: the machine can be connected and still have nowhere to send data. Test for the four components: a named
business owner, an IT owner, a service concept with support level (out-of-hours or not), and a change and risk process. If one is
missing, class C4, exit Strategy via `dept-decision-rights`. No rollout without an operations concept and a named run owner; stop until both exist.

### Ownership signals (spot a stuck case early)

A technical puzzle that no one is working is usually missing ownership. Tells:

- no reply to follow-ups over weeks,
- unclear owner for access to an artifact registry or a connection,
- no one asking why other sites work,
- a "waiting" status with no named owner and no date to look again.

Ask: who is responsible for the connection; what do the other sites do; what is the alternative if it never works. If the owner is
unnamed, the exit is Strategy (decision above the machine), not Roadmap.

### Blocker one-pager (situational awareness)

When a programme is blocked, write it in sections: technical, commercial (supplier), customer; a blockers list per section; a
timeline; a record of what was shown to the customer; an options page with **three separate deadlines** (decision date,
infrastructure change deadline, customer deadline); a named list of who can support local IT. Options in one case: new server on the
old stack (rejected as pointless), old server with domain transfer (quick fix), roll out the strategic platform (long-term, needs
external support). A customer audit is a hard external deadline that outranks the internal plan.

### Preconditions that should exist before a migration or connection starts

Artifact registry, source-code host, firewall changes, cloud-system approval, runtime licence key, DNS and certificates, a named
owner for each. A new installation without the legacy baseline is the hardest case (a "special" site).

### Barrier reporting

Plot the barrier that holds the case back and the **cost of non-decision** to the decision makers (`PROPOSAL`: computed from the
portfolio with the read date); propose a rapid decision board for holdbacks; keep an error log with a regular review. A weekly
issue-log review asks "what went wrong" and classifies by knowledge, service lines and processes, IT, project-management overhead.
Interview-style check: a claim "not found in the evidence" is carried as unverified, not dropped and not repeated as fact. A kill or
hold register with a recorded reason stops cancelled ideas from being re-raised (`PROPOSAL`).

## 2 Decision rules

| Situation | Rule |
|---|---|
| Two classes apply | The one that blocks first decides (existing rule); note the other as "behind it" |
| Case has no named owner | Not Roadmap; escalate as ownership gap |
| Open sign-off | Hold go-live only; never connect first; parallel track, planning and build continue |
| Substitution adds a tool | Back through `invest-screen` |
| Legacy application that cannot be replaced yet | Write a "continue as is" scenario with its consequences (persistent security issues, rising patching and compatibility problems, loss of know-how, expiring support) |

## 3 Handoff contract

| Direction | Skill | Content |
|---|---|---|
| Receive | `mi-equipment` | Machine facts, ladder result, blocker text, use cases waiting |
| Receive | `deploy-cybersec` | A refusal or a wait with owner |
| Hand on | `dept-decision-rights` | Strategy exit as a decision request with the risk of not deciding |
| Hand on | `bc-cost` | Substitution that costs money |
| Hand on | `mi-signals` | A data-model blocker |
| Hand on | `mi-equipment` | Roadmap items with sequence position, owner and look-again date |

## 4 Questions to ask and definition of done

Which use case is waiting and who is its owner? Which class blocks first? Who owns the next step and by when? What do other sites do?
What is the alternative if it never works? What happens if we do nothing, and what does waiting cost?

Done = the existing definition (one class, a tier, an exit, an owner and forum, a logged barrier), plus: an owner and a look-again
date for Roadmap exits, an operations-concept check for any C4 case, and a "cost of non-decision" line for Strategy exits.

## 5 AI agent operating notes

- **Can do**: classify the blocker text into a class with the question that identified it, spot the ownership tells (silent
  threads, no owner, no date), draft the blocker one-pager from tickets and mail, group blocker texts by class (`estate-patterns.md`),
  compute the where-stuck summary.
- **Inputs required**: the Machine List row, the blocker text, the ladder result, the use case waiting, the ticket or mail thread.
- **Evidence to cite**: the list row and read date, the ticket reference, the class question answered.
- **Human gates**: the exit choice and the escalation wording (OD lead); never connect, patch, write to a PLC or approve a
  connection.
- **Handover**: the triage record to the receiving skill with owner role and look-again date.
