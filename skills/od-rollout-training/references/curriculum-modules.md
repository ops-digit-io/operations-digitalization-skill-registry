---
type: Skill Reference
title: Curriculum modules
description: The module catalogue for plant rollout training (M0 to M7) - audience, what the trainee must be able to do, the skill that already holds the content, and the hands-on form - a proposal built from existing skills and the recorded workshop content.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [project-support-consultancy, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Curriculum modules

**This catalogue is a proposal.** No source lists the department's standard training formats (the call decks report
content for a set of formats without titles). The modules below are assembled from content that **already exists in this
registry** and from the workshop content recorded in the call decks. Each module says where its content lives, so it
does not drift from the original. Durations, formats and trainers are `⟨…⟩`.

Audience codes: **ME** Plant ME, **IT** Plant IT, **KU** key user, **SL** shift lead or operator, **PO** plant owner
of the solution, **MG** plant and department managers.

## Catalogue

| # | Module | Audience | The trainee can afterwards | Content already held in | Hands-on form |
|---|---|---|---|---|---|
| M0 | Orientation: what OD does, the three lanes, who decides what | MG, PO, KU | Say which lane a request belongs to, who decides, and what the plant may do alone | `od-context`; `od-decision-routing` (decision table, five gates) | Walk one real request through the decision table |
| M1 | Read and act on a delivered use case | SL, PO | Say what decision it supports, in which ritual (Gemba walk, shift check, Andon escalation), and what to do when it shows a deviation | `od-handover-and-adoption` (three-question test, Q1); the plant's own use-case record | At the real screen, in a real shift (the ADKAR Knowledge action) |
| M2 | Diagnose a silent dashboard | KU, ME, IT | Trace the data path from screen to machine and say which link broke; know which layer is local (plant Grafana) and which is global (data platform) | `od-handover-and-adoption` (Q2); `od-equipment-integration` `references/iiot-edge-platform.md`; registry open gap on local versus global layers | Trace one real dashboard to its machine on paper, then check each link |
| M3 | Machine integration for Plant ME | ME, IT | Decide with the guidance protocol which route fits a machine, what is installed at the plant, what blocks it; draft the protocol for one machine | `od-equipment-integration` (`assets/guidance-protocol.md`, `references/decision-paths.md`, `barrier-classes.md`) | Fill the guidance protocol for a real, unconnected machine; **no live connection** |
| M4 | Use-case tools: Grafana, Node-RED, Jupyter Notebook | ME, KU | Build or adjust a dashboard of the delivered template; read a flow; find a broken flow | `build-grafana-ops-dashboard`; `od-node-red-flow-builder`; `od-node-red-flow-troubleshooting`; the recorded workshop content (Grafana, Node-RED, Jupyter Notebook as taught at a plant workshop) | One change on the plant's own instance, reviewed by the trainer |
| M5 | Gates: when to stop and route | ME, IT, KU, PO | Name the gate (spend, IT demand, standard, Cyber Security, daily use), fill a decision request, and not proceed without the answer | `od-decision-routing` (assets/decision-request.md); `od-cybersec-gate` | Fill a decision request for a realistic plant case |
| M6 | Acceptance and handover, plant side | PO, KU | Act as the witness at an acceptance test (never the builder); say what a handover is complete against; record adoption evidence | `od-acceptance-test` (protocol, witness rule); `od-handover-and-adoption` (`references/evidence-of-adoption.md`) | Witness one real or replayed acceptance item and write the evidence line |
| M7 | Run and sustain: COP, reporting, utilization | KU, PO | Bring a technical item to COP, read the utilization rate, know when to escalate and to whom | `od-decision-routing` (`references/escalation-worked-examples.md`); `od-scorecard-reporting` | Prepare one COP item from a real open issue |

## Which modules for which rollout

| Rollout | Minimum modules | Why |
|---|---|---|
| A delivered dashboard or Andon board (Lane 1 go-live, Lane 2 step 6) | M1, M2, M7; M4 for the person who maintains it | The consumers are shift lead and plant owner; the data path must be diagnosable without OD |
| A newly connected machine wave (Lane 1b, Lane 3b) | M0, M2, M3, M5, M6 | The Plant ME and Plant IT must hold the route, the gates and the acceptance witness role |
| A new app on the platform (Lane 3a) | M1, M5, M6, M7 | Deployment is human-approved; the plant owner needs the adoption side. ⟨App-specific operation training⟩ comes from the app's own owner, for example the QFPR basic training |
| A new plant entering the programme | M0 first, then the rows above in the order of its roadmap | The skill map lists plant onboarding as a separate planned skill (`od-plant-onboarding`) |

## Notes per module

- **M1 and M2** follow the ADKAR actions in `od-handover-and-adoption`: Awareness once at the ritual it belongs to,
  Knowledge as one walkthrough at the actual screen during a real shift, Ability confirmed at the point of use. A
  classroom session without the real screen does not count.
- **M3** stops short of connecting. Physical integration is human `execute-with-approval`, Tandem with the IIAE,
  and external connections need Cyber Security sign-off first. The module teaches the plant to prepare and to
  hold the gate.
- **M4** covers local tooling. The Grafana of a plant is a local instance for that plant's dashboards; do not train
  anyone to point it at the global data platform.
- **M5** makes decentralization safe: a trained plant person who proceeds past a gate is worse than an untrained one.
- **M6** exists because the acceptance protocol requires a witness from the receiving side, never the builder
  (`od-acceptance-test`). If the plant has nobody who can witness, the rollout is not ready.

## What is open

- ⟨Titles of the 8 standard formats⟩ and how they map to M0 to M7.
- ⟨Durations and trainer role per module⟩.
- ⟨Material per module⟩: slides and exercises are not in the sources.
- ⟨Training for MES and MDA/PDA⟩: these tools have rollout records but no training content is recorded.
