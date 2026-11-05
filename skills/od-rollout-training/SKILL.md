---
name: od-rollout-training
description: >-
  Draft the plant training package and the competence checklist for a solution that is
  rollout-ready - who at the plant must be able to do what without the OD builder, which
  modules teach it at the real screen or machine, how each competence is evidenced, and how
  the plant avoids a single person who knows. The plant confirms competence; this skill
  never does. Use when a use case, machine connection or app passed acceptance and is going
  to a plant, when a plant starts a new integration wave, when a key user is to be
  enabled, or when a plant asks how to run this without OD.
license: Internal — OESL MPEE Operations Digitalization. Not for external distribution.
allowed-tools: Read Grep Glob
metadata:
  id: od-rollout-training
  tier: practice
  lane: project-support-consultancy
  new_state_lane: Lane 3a (rollout), Lane 1 go-live, Lane 2 step 6
  new_state_step: "Rollout and adopt: training package and competence checklist"
  owner_role: human:jakob.gabriel
  authority_level: draft the training package and competence checklist; the plant confirms competence
  status: draft
  sources_read: 2026-11-05
  requires: [od-context]
  composes: [od-handover-and-adoption, od-acceptance-test]
  derived_from:
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/OD_Skill_Map.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/20-lanes/information-integration-service/playbook.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/20-lanes/project-support-consultancy/playbook.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/20-lanes/project-support-consultancy/agent-brief.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/10-modules/smart-factory-use-case/capabilities.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/00-core/09-risks.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/00-core/08-decision-rights.md
    - Skills od-handover-and-adoption (three-question test, ADKAR actions, evidence tiers), od-acceptance-test (witness rule), od-equipment-integration (guidance protocol gates), od-decision-routing, od-context, deploy-appstore, read 2026-11-05
    - Registry docs/new-state-flow.md and docs/new-state diagrams, the Lane 3a step "Rollout and adopt" and the Lane 1 and Lane 2 go-live steps, read 2026-11-05
    - Work vault (Work-OpsDigit-Knowledge), ODEC Facts notes Department KPIs and Roadmap Status (training figures 2023), Plant - San Luis Potosi, Delicias, Montemorelos, Ponta Grossa, Somersworth (Americas training roadmap 2025, workshop agenda), Changchun, Changshu, Qingdao (training achievements), Monterrey (QFPR training), Other (WiriTec key users, Secure Critical Automation Software); Graph/Tools (16 tool notes, rollout and use counts) and Concept 3 (roles of the operations concept); Graph/Plants (Carei as the profile pattern); Case Groups (40 groups, delivered counts), read 2026-11-05
  okf:
    type: Agent Skill
    title: Rollout training
    tags: [project-support-consultancy, practice, new-state, draft]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---

# Rollout training

Read `od-context` first.

**Status: draft, and the thinnest-sourced skill in the registry.** The skill map calls this "the decentralization skill"
and says it "is under-specified in the current Department OS and needs the most new content". The sources give the
control point ("rollout-ready; plant trained"), a few training facts from call decks, and the plant roles. They do
**not** give a training standard, a list of modules or a competence model. This skill assembles a package from what
the neighbouring skills already teach, and every proposal that is not a recorded fact is labelled **proposal**.

## Purpose, trigger, done

- **Trigger.** A solution is rollout-ready: acceptance passed (`od-acceptance-test`), Cyber Security cleared where it
  applies (`od-cybersec-gate`), and the plant is to run it. Also: a new integration wave starts, or a key user is to
  be enabled. Playbook step 6 of the Information Integration lane: "Prepare Manufacturing Software Suite rollout;
  equipment integration training - Human (IIAE) - Rollout-ready; plant trained".
- **Output.** A filled [`assets/training-package.md`](assets/training-package.md) and a filled
  [`assets/competence-checklist.md`](assets/competence-checklist.md) for one plant and one solution.
- **Done.** Each competence on the checklist is confirmed **by the plant** with evidence, and no critical skill rests on
  one person. Delivery of a session is not done.

## The references

| File | Use it for |
|---|---|
| [`references/plant-landscape.md`](references/plant-landscape.md) | How a plant is organised for this purpose: roles, the tools a plant actually has, the training and workshop history in the call decks, with counts and dates |
| [`references/curriculum-modules.md`](references/curriculum-modules.md) | The module catalogue (M0 to M7): audience, what the trainee must be able to do, the skill that already holds the content, and the hands-on form |
| [`references/competence-and-sustainment.md`](references/competence-and-sustainment.md) | How competence is evidenced, the single-point-of-failure rule, hand-down from key user to key user, and what keeps it alive after the trainer leaves |

## What this skill does not repeat

`od-handover-and-adoption` already holds the handover test, the ADKAR diagnostic for a stalled use case and the
evidence tiers. This skill starts **before** that: it produces the people who can pass the three-question test
without the builder. Where a module needs that content it links there; it does not copy it.

## Procedure

1. **Fix the scope.** One plant, one solution (use case, machine connection, or app), one rollout moment. Name the
   plant owner and the plant roles in play (Plant ME, Plant IT, shift lead, key user). Roles only, never names.
2. **Check readiness.** Rollout-ready means acceptance passed, the data path is written down to the machine, the
   sign-off gate is answered, and the plant infrastructure is live. Infrastructure is a recorded cause of delay:
   call decks give "infrastructure harmonization" (China) and delayed infrastructure from hardware suppliers
   (Americas) as blocking points. If not ready, say so in the package and do not schedule training on a
   demo environment (`od-handover-and-adoption`: Ability is confirmed at the point of use).
3. **Find who must be able to do what.** Per role, from [`references/curriculum-modules.md`](references/curriculum-modules.md).
   Start from the decisions the plant will take alone and the gates it must route
   (`od-decision-routing`); a competence for a gate is "stops and routes", not "does it".
4. **Choose modules and the hands-on form.** Every module ends in something the trainee does on the real screen,
   the real machine or in a real shift. Durations, formats and trainers are `⟨…⟩` until the OD lead supplies the
   standard training formats (the 2023 call deck says content exists for 8 formats; their titles are not in the
   sources).
5. **Check the trainer capacity honestly.** The Information Integration lane has 3 IIAE roles with open positions
   in Asia and Americas (`capabilities.md`). A plan that needs the IIAE in every session is not decentralized.
   Use the hand-down rule in `references/competence-and-sustainment.md` (a proposal).
6. **Draft the package and the checklist.** Fill both assets. Mark every duration, date and trainer `⟨…⟩` unless a
   source gives it.
7. **Run, then let the plant confirm.** The trainer role delivers; the **plant owner** confirms each competence
   with evidence. The assistant never marks a competence confirmed.
8. **Hand to adoption.** The completed checklist is the input of the handover in `od-handover-and-adoption`
   (Knowledge and Ability elements); the Scorecard utilization rate then carries Reinforcement.
9. **Report gaps upward.** A competence that cannot be confirmed, or a skill held by one person, goes to the OD
   lead via COP (risk register: "single point of failure identified" is the escalation trigger for limited internal
   IT knowledge).

## Decision table

| Situation | Action | Source |
|---|---|---|
| Solution not accepted yet | Do not train; fix acceptance first | `od-acceptance-test` |
| Sign-off from Cyber Security open | Training may cover the gate; no live connection exercise | `od-cybersec-gate` |
| Only one plant person can do a critical task | Not done; name a second | risk register trigger |
| Trainee passes the session but cannot do it in a shift | Competence not confirmed | `od-handover-and-adoption` evidence tiers |
| Utilization is `NEVER` after training | Run the ADKAR diagnostic before more training | `od-handover-and-adoption` |
| The plant wants a module not in the catalogue | Propose it; the catalogue is a draft | this skill |

## Open - what only the OD lead, DBVE and IIAE can supply

- ⟨Titles, content and length of the 8 standard training formats⟩ reported in the 2023 call deck, and the 3 planned in 2024.
- ⟨Who may train whom⟩: is a trained plant key user allowed to train other plants' staff? Not in the sources.
- ⟨Competence standard⟩: who, if anyone, certifies a person; no certification is recorded.
- ⟨Where training attendance is recorded⟩: the 2024 plan was to "improve recorded training sessions"; no system is named.
- ⟨Named plant owners and key users per plant⟩: role labels only in the sources; the registry lists named owners as an open gap.
- ⟨The training offer for non-OD tools⟩ (MES, MDA/PDA): not in the sources.

## Do not

- Do not mark a competence confirmed, a session as adoption, or a person as qualified: the plant confirms.
- Do not teach on a demo environment and call it rollout training.
- Do not name individuals in the package; use roles.
- Do not invent durations, counts or certification levels; leave `⟨…⟩`.
- Do not copy the handover or ADKAR content; link to `od-handover-and-adoption`.
- Do not train anyone to connect a machine or approve an external connection alone: both are human
  `execute-with-approval` with Cyber Security sign-off first.
