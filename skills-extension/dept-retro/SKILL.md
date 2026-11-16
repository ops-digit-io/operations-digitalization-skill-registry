---
name: dept-retro
description: >-
  Runs the department's monthly retrospective so that it ends in exactly one decided adjustment, not a
  list. Closes last month's change first, gathers the three inputs (incidents, metrics, COP feedback
  with the historical ODEC record), lists what was learned with its evidence, picks the one change,
  and records who decides it and how it will be checked next month. Use when the monthly retro is due,
  after a COP round, an incident or a missed threshold, or when someone asks what the improvement loop
  is and why a retro that produced a list has not produced a decision. Not for preparing the COP round
  (metrics-scorecard) or reading the risk register (dept-risk).
license: MIT
allowed-tools: Read Grep Glob
metadata:
  id: dept-retro
  aliases: [od-retro]   # former name (naming convention, 2026-11-11)
  tier: practice
  lane: all
  new_state_lane: "Extension, deepens Spine"
  new_state_step: "Supporting spine"
  owner_role: human:jakob.gabriel
  authority_level: draft
  status: draft
  requires: [dept-context]
  composes: [metrics-scorecard, dept-risk, bc-portfolio, dept-decision-rights, dept-context-freshness]
  okf:
    type: Agent Skill
    title: Monthly retrospective
    tags: [all, practice, new-state, draft]
---

# Monthly retrospective

- Read `dept-context` first.
- The operating rhythm calls the retro mandatory: "What did we learn -> 1 change". Inputs: incidents, metrics, COP feedback (ODEC is historical). Output: one decided adjustment, at least monthly.
- This skill does **not** repeat the round preparation (`metrics-scorecard`); it starts from the finished round and its numbers and turns them into one change.
- **Outputs:** [`references/outputs.md`](references/outputs.md) lists what this skill must deliver, to whom, and when each output is complete.

## The rule that defines it

- **A retro that produces a list has not produced a decision.** The record has a learning list (what was learned) and exactly one adjustment.
- Everything else goes to the parking list and is revisited, not decided, because a department that acts on five things checks none of them.

## The references

| File | Open when |
|---|---|
| [`references/retro-inputs.md`](references/retro-inputs.md) | Step 2: you gather the three inputs and need to know where each is read, what a usable item looks like and the limits of each |
| [`references/reading-change-logs.md`](references/reading-change-logs.md) | Step 2: you use the generated use-case change logs as evidence and must tell signal from sweeps and tidy-ups |
| [`assets/retro-record.md`](assets/retro-record.md) | Step 1: you start the one-page record (last month's check, learning list, the one adjustment, parking list) |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | Steps 3-5: you look for good learning items, classify causes or decide clean-up and kill/hold |
| [`references/background.md`](references/background.md) | You need the provenance, the open questions or the required-output table; never an instruction |

## Procedure

1. **Close last month first.** Open last month's record and answer its check question with evidence: did the adjustment happen, did it do what it was meant to?
   - Outcomes: kept, changed, dropped.
   - Without this step the loop is Plan-Do with no Check or Act.
2. **Gather the three inputs** (`references/retro-inputs.md`; change logs: `references/reading-change-logs.md`): incidents, metrics, COP feedback and the historical ODEC record (past decisions, decks, facts).
   - Use `metrics-scorecard` for the metrics, with the read date; use `dept-risk` for the risk readings if it has been run this month.
3. **Write the learning list.** Each item: what happened, evidence, source with date, and which input it came from. An item with no evidence is not a learning; mark it `⟨evidence missing⟩` or leave it out.
4. **Test each item for being changeable by OD.** Three questions: can OD change this by itself (no gate outside OD)?
   - Is it reversible?
   - Will next month's inputs show whether it worked?
   - An item that fails the first question is not an adjustment but an escalation: send it to `dept-decision-rights` (strategy and priority: the deciding role per the current approval policy, look up; technical: COP).
5. **Choose exactly one.** Preference order, a working rule of this skill, not of the Department OS: a. an item behind a crossed intervention threshold or an escalation trigger (`07-metrics.md`, `09-risks.md`);
   - b. an item that recurred across more than one input or more than one month; c. the cheapest reversible change that addresses the item.
   - Say why this one and not the others in one sentence.
6. **State the adjustment as an action**, with a role as owner (never a name), a date and an observable:
   - "From ⟨date⟩, ⟨role⟩ does ⟨X⟩; we will see it in ⟨metric or record⟩ at the next retro."
7. **Record who decided it.** The operating rhythm says "decided adjustment" without naming the decider: `⟨decider role for the monthly adjustment, to confirm with the OD lead⟩`.
   - This skill's authority is `draft`: it prepares the record and proposes the one change; the decider takes it.
   - If the change touches a row of the decision-rights table (priority, rollout, standards, investment), the usual route applies via `dept-decision-rights`.
8. **Park the rest.** Carry unchosen items to the parking list with the month they first appeared; two months parked is a signal for rule (b) next time.
9. **Hand the one adjustment on:** into the next COP input, or to the deciding role named in the current approval policy (look up), if others must act; into `dept-context-freshness` (planned) if the adjustment is a change to a context file.
10. **Check the record before it goes out.** Last month's check answered with evidence; every learning item has a dated source; exactly one adjustment with role, date and observable; decider role named or marked open.

## Decision table: which item becomes the adjustment

| Situation | Choose |
|---|---|
| A metric crossed its intervention threshold and nothing was changed last month | The item addressing that metric, if OD can change it; otherwise escalate and choose the next item |
| An escalation trigger in the risk register was hit | The item that lowers the cause, not the symptom |
| Same item appeared in two months | It, ahead of newer items |
| Last month's adjustment did not work | Rework it or replace it, and say which; the check result is itself an input |
| Two items equal | The reversible and cheaper one |
| No evidence-backed item at all | Record "no adjustment: no evidence-backed candidate", with the inputs read; do not invent one |

## Example (fictional)

```text
Month 2026-03 (fictional). Inputs read: metrics 2026-03-02, COP 2026-03-05,
  incidents (support tickets) 2026-03-01, risk reading 2026-03-03.
1 Check of last month: "Plant key users get a 15-minute intro call" - done;
  observable (new-user questions per week) fell. Outcome: kept.
2 Learning list:
  #1 Three plants asked the same signal question; source COP 2026-03-05; input COP; OD can change: yes; first seen 2026-02
  #2 Dashboard load error on one edge instance; source ticket 2026-03-01; input incident; OD can change: no
  #3 Saving projects registered late; source metrics; input metric; OD can change: yes; first seen 2026-03
3 The one adjustment (rule b, recurred): From 2026-04-01 the OD data role adds a
  signal FAQ to the intro call; observable: repeats of that question in COP in April.
4 Parking: #3 (first seen 2026-03).   5 Escalation: #2 -> dept-decision-rights.
```

## Pitfalls

- **Ending with a list of actions.** One adjustment; the rest is parked, because a list is not a decision.
- **Proposing a new tracker, slide or system** when removing or merging one would address the item.
- **Naming individuals in the record.** Roles only.
- **Counting an intention as a result.** The check at the next retro needs an observable.
- **Picking an adjustment that needs a gate outside OD and calling it done.** Route it; OD cannot decide it alone.
- **Re-opening decisions** already routed through COP or the deciding role. Learn from them, do not reopen them.
- **Inventing a candidate** when no item has evidence. Write "no adjustment" instead.
- **Adding an agenda or participant names.** The operating rhythm excludes both; the record lists roles only.

## Human gate and AI-agent notes

- The agent drafts the record and proposes the one adjustment; the deciding role takes it. Its authority is `draft`.
- The agent never marks an adjustment decided and never counts an escalated item as the adjustment.

## Outputs

- [`outputs.yaml`](outputs.yaml): required outputs, criteria, checks and sign-offs.
- [`assets/retro-record.md`](assets/retro-record.md), kept with the month's COP outputs and any ODEC records used.
- One run record per call: `python scripts/run_record.py new <skill-id>` (registry root).

## References

| File | Open when |
|---|---|
| [`references/background.md`](references/background.md) | You need the provenance, the open questions or the required-output table; never an instruction |
| [`evals/evals.json`](evals/evals.json) | Test cases and trigger queries to run with and without this skill |
