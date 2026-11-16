---
name: know-training
description: >-
  Draft the plant training package and the competence checklist for a solution that is
  rollout-ready: who at the plant must be able to do what without the OD builder, which
  modules teach it at the real screen or machine, how each competence is evidenced, and how
  the plant avoids a single person who knows. Use when a use case, machine connection or app
  passed acceptance and is going to a plant, when a plant starts a new integration wave, when
  a key user is to be enabled, or when a plant asks how to run this without OD. The plant
  confirms competence; this skill never does. Not for the handover test or the adoption
  diagnostic (deploy-handover) and not for the acceptance test (deploy-acceptance).
license: MIT
allowed-tools: Read Grep Glob
metadata:
  id: know-training
  aliases: [od-rollout-training]   # former name (naming convention, 2026-11-11)
  tier: practice
  lane: all
  new_state_lane: "Extension, deepens Lane 1a (1a3), Lane 1b (1b4), Lane 2 (26), Lane 3a (3a6)"
  new_state_step: "Guardrails, go live, confirm adoption; Standardized deployment, go live, confirm adoption; Implement, evaluate impact, ensure adoption, catalogue; Rollout and adoption; ownership on formal acceptance"
  owner_role: human:jakob.gabriel
  authority_level: draft the training package and competence checklist; the plant confirms competence
  status: draft
  requires: [dept-context]
  composes: [deploy-handover, deploy-acceptance]
  okf:
    type: Agent Skill
    title: Rollout training
    tags: [project-support-consultancy, practice, new-state, draft]
---

# Rollout training

- Read `dept-context` first.
- Status: draft. The module catalogue and the hand-down model are proposals, not a department standard; every proposal is labelled **proposal** (why, see `references/background.md`).

## Purpose

- **Trigger.** A solution is rollout-ready: acceptance passed (`deploy-acceptance`), Cyber Security cleared where it applies (`deploy-cybersec`), and the plant is to run it.
   - Also: a new integration wave starts, or a key user is to be enabled.
   - Playbook step 6 of the Information Integration lane: "Prepare Manufacturing Software Suite rollout; equipment integration training - Human (IIAE) - Rollout-ready; plant trained".
- **Done.** Each competence on the checklist is confirmed **by the plant** with evidence, and no critical skill rests on one person. Delivery of a session is not done.
- Not repeated here: `deploy-handover` holds the handover test, the ADKAR diagnostic and the evidence tiers. This skill starts **before** it and produces the people who can pass the three-question test without the builder; link there, do not copy.

## Inputs and output

- **In:** one plant, one solution (use case, machine connection or app), one rollout moment; the acceptance record; the plant roles in play.
- **Out:** a filled [`assets/training-package.md`](assets/training-package.md) and a filled [`assets/competence-checklist.md`](assets/competence-checklist.md) for that plant and solution.
- [`outputs.yaml`](outputs.yaml) lists required outputs, criteria, checks and sign-offs.

## Procedure

1. **Fix the scope.** One plant, one solution, one rollout moment. Name the plant owner and the plant roles in play (Plant ME, Plant IT, shift lead, key user). Roles only, never names.
2. **Check readiness.** Rollout-ready means acceptance passed, the data path is written down to the machine, the sign-off gate is answered, and the plant infrastructure is live.
   - Infrastructure is a recorded cause of delay: call decks give "infrastructure harmonization" (China) and delayed infrastructure from hardware suppliers (Americas) as blocking points.
   - If not ready, say so in the package and do not schedule training on a demo environment. Reason: Ability is confirmed at the point of use (`deploy-handover`).
3. **Find who must be able to do what.** Per role, from `curriculum-modules`. Start from the decisions the plant will take alone and the gates it must route (`dept-decision-rights`); a competence for a gate is "stops and routes", not "does it".
4. **Choose modules and the hands-on form.** Start from the default minimum set below; change it only with a reason written in the package.
   - Every module ends in something the trainee does on the real screen, the real machine or in a real shift.
   - Durations, formats and trainers are `⟨…⟩` until the OD lead supplies the standard training formats (their titles are not in the sources).
5. **Check the trainer capacity honestly.** The Information Integration lane has a small number of IIAE roles, some positions open (`capabilities.md`; check the current staffing).
   - A plan that needs the IIAE in every session is not decentralized.
   - Use the hand-down rule in `competence-and-sustainment` (a proposal).
6. **Draft the package and the checklist.** Fill both assets. Mark every duration, date and trainer `⟨…⟩` unless a source gives it.
7. **Run, then let the plant confirm.** The trainer role delivers; the **plant owner** confirms each competence with evidence. The assistant never marks a competence confirmed.
8. **Hand to adoption.** The completed checklist is the input of the handover in `deploy-handover` (Knowledge and Ability elements); the Scorecard utilization rate then carries Reinforcement.
9. **Report gaps upward.** A competence that cannot be confirmed, or a skill held by one person, goes to the OD lead via COP. Reason: "single point of failure identified" is the risk-register escalation trigger for limited internal IT knowledge.

### Default minimum modules per rollout (proposal)

| Rollout | Minimum modules | Audience first |
|---|---|---|
| Delivered dashboard or Andon board | M1, M2, M7; M4 for the maintainer | Shift lead, plant owner, key user |
| Newly connected machine wave | M0, M2, M3, M5, M6 | Plant ME, Plant IT |
| New app on the platform | M1, M5, M6, M7 | Plant owner, key user |
| New plant entering the programme | M0 first, then the rows above in roadmap order | Managers, plant owner |

- Module titles and the full catalogue (M0 to M7) are in `curriculum-modules`.

### Example: one checklist row (fictional)

```text
Competence checklist - Plant X (fictional) - Andon board for line 3
C4 | Traces the data path from screen to machine and names the link that broke | KU, ME | M2 | critical: yes
   Content held in: deploy-handover (Q2)
   Evidence tier: 1 (system record - key user's trace sheet from a replayed outage, 2026-02-10, fictional)
   Persons confirmed: 2 of 2 (key user A, Plant ME B; roles only)
   Confirmed by: plant owner (role)   Date: <plant owner fills>
   Package row: M2 | Hands-on: trace this Andon board to its machine on paper, then check each link | Duration <...> | Trainer <...>
```

## Decision table

| Situation | Action | Source |
|---|---|---|
| Solution not accepted yet | Do not train; fix acceptance first | `deploy-acceptance` |
| Sign-off from Cyber Security open | Training may cover the gate; no live connection exercise | `deploy-cybersec` |
| Only one plant person can do a critical task | Not done; name a second | risk register trigger |
| Trainee passes the session but cannot do it in a shift | Competence not confirmed | `deploy-handover` evidence tiers |
| Utilization is `NEVER` after training | Run the ADKAR diagnostic before more training | `deploy-handover` |
| The plant wants a module not in the catalogue | Propose it; the catalogue is a draft | this skill |

## Human gate and AI-agent notes

- **Agent may:** draft the package and checklist, find the plant's roles and tools, list gaps.
- **The plant owner (role) confirms** each competence with evidence; the OD lead receives the gap report via COP.
- **Never:** mark a competence confirmed, a session as adoption, or a person as qualified.
- Physical machine connection and external connections are human `execute-with-approval` with Cyber Security sign-off first; training teaches the plant to prepare and hold the gate.

## Open - what only the OD lead, DBVE and IIAE can supply

- ⟨Titles, content and length of the standard training formats⟩ reported in the call decks, and the ones planned.
- ⟨Who may train whom⟩: is a trained plant key user allowed to train other plants' staff? Not in the sources.
- ⟨Competence standard⟩: who, if anyone, certifies a person; no certification is recorded.
- ⟨Where training attendance is recorded⟩: a call-deck plan was to "improve recorded training sessions"; no system is named.
- ⟨Named plant owners and key users per plant⟩: role labels only in the sources; the registry lists named owners as an open gap.
- ⟨The training offer for non-OD tools⟩ (MES, MDA/PDA): not in the sources.

## Pitfalls

- Do not schedule a rollout where no one can run the solution afterwards; enabling comes first (`process-chain-practice`).
- Do not mark a competence confirmed, a session as adoption, or a person as qualified: the plant confirms.
- Do not teach on a demo environment and call it rollout training.
- Do not name individuals in the package; use roles.
- Do not invent durations, counts or certification levels; leave `⟨…⟩`.
- Do not copy the handover or ADKAR content; link to `deploy-handover`.
- Do not train anyone to connect a machine or approve an external connection alone: both are human `execute-with-approval` with Cyber Security sign-off first.

## Definition of done

- Package and checklist are filled for one plant, one solution, one rollout moment, with roles only.
- Readiness is stated; if not ready, no training is scheduled.
- Every competence is confirmed by the plant owner with evidence, and no critical skill rests on one person.
- Gaps are reported to the OD lead via COP; the checklist is handed to `deploy-handover`.

## Outputs

- [`outputs.yaml`](outputs.yaml): required outputs, criteria, checks and sign-offs.
- One run record per call: `python scripts/run_record.py new <skill-id>` (registry root).

## References

| File | Open when |
|---|---|
| [`references/curriculum-modules.md`](references/curriculum-modules.md) | Step 3 and 4: the module catalogue (M0 to M7) with audience, what the trainee can do afterwards, where the content lives and the hands-on form |
| [`references/plant-landscape.md`](references/plant-landscape.md) | Step 1 and 5: plant roles, how to find the tools a plant has, the kinds of training recorded in the call decks, where to read live data |
| [`references/competence-and-sustainment.md`](references/competence-and-sustainment.md) | Step 5, 7 and 9: how competence is evidenced, the single-point-of-failure rule, hand-down between key users, keeping it alive |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | You need the training offer process, training-need capture, tools before pilots, or what an agent may draft |
| [`assets/training-package.md`](assets/training-package.md) | Step 6: the package template |
| [`assets/competence-checklist.md`](assets/competence-checklist.md) | Step 6 and 7: the checklist template the plant owner confirms |
| [`references/background.md`](references/background.md) | You need the status and sourcing rationale; never an instruction |
| [`evals/evals.json`](evals/evals.json) | Test cases and trigger queries to run with and without this skill |
| [`references/outputs.md`](references/outputs.md) | The output contract in full (generated from outputs.yaml) |
