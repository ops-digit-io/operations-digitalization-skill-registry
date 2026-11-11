---
name: od-retro
description: >-
  Run the department's monthly retrospective so that it ends in exactly one decided
  adjustment - gather the three inputs the operating rhythm names (incidents, metrics,
  COP feedback and the historical ODEC record), list what was learned with its evidence, pick the one change, record
  who decides it and how it will be checked next month, and review last month's change first.
  Use when the monthly retro is due, after a COP round, after an incident or a
  missed threshold, or when someone asks what the improvement loop is and why a retro that
  produces a list has not produced a decision.
license: MIT
allowed-tools: Read Grep Glob
metadata:
  id: od-retro
  tier: practice
  lane: all
  new_state_lane: "Extension, deepens Spine"
  new_state_step: "Supporting spine"
  owner_role: human:jakob.gabriel
  authority_level: draft
  status: draft
  requires: [od-context]
  composes: [od-scorecard-reporting, od-risk-watch, od-portfolio-and-savings-analysis, od-decision-routing, od-context-freshness]
  okf:
    type: Agent Skill
    title: Monthly retrospective
    tags: [all, practice, new-state, draft]
---

# Monthly retrospective

Read `od-context` first.

Plan item O-06 of the department's skill map (wave 3). The operating rhythm marks the retro with a star and calls it
mandatory: **"What did we learn -> 1 change"**, input *incidents, metrics, ODEC/COP feedback* (ODEC no longer meets; read its records as history), output *1 decided
adjustment*, cadence *at least monthly*. The reason is stated there too: without a minimal retro cadence the department
has no improvement loop, and "learning is a leadership duty (PDCA/Kaizen)".

`od-scorecard-reporting` already prepares and follows up the COP rounds and reads the historical ODEC records and states that the retro output is
exactly one decided adjustment. This skill does **not** repeat the round preparation. It starts from the finished
round and its numbers and turns them into one change.

- **Outputs:** [`references/outputs.md`](references/outputs.md) lists what this skill must deliver, to whom, and when each output is complete.

## The rule that defines it

**A retro that produces a list has not produced a decision.** The record has a list (what was learned) and exactly one
adjustment. Everything else goes to the parking list and is revisited, not decided.

## The references

| File | Use it for |
|---|---|
| [`references/retro-inputs.md`](references/retro-inputs.md) | Where each of the three inputs is read from, what a usable item looks like, which signals the sources already supply and the limits of each |
| [`references/reading-change-logs.md`](references/reading-change-logs.md) | What the generated use-case change logs record, how to read a line, which changes are signal and which are sweeps or tidy-ups, limits to state, and how to turn a log into a retro item |
| [`assets/retro-record.md`](assets/retro-record.md) | The one-page record: last month's check, the evidence list, the one adjustment, the parking list |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | Where good learning items come from, a cause classification, clean-up and kill/hold hygiene, and what an agent may draft |

## Procedure

1. **Close last month first.** Open last month's record and answer its check question with evidence: did the adjustment
   happen, did it do what it was meant to? Outcomes: kept, changed, dropped. Without this step the loop is Plan-Do with
   no Check or Act.
2. **Gather the three inputs** ([`retro-inputs.md`](references/retro-inputs.md)): incidents, metrics, COP feedback and the historical ODEC
   record (past decisions, decks, facts). Use `od-scorecard-reporting` for the metrics, with the read date; use `od-risk-watch` for the risk readings
   if it has been run this month.
3. **Write the learning list.** Each item: what happened, evidence, source with date, and which input it came from. An
   item with no evidence is not a learning; mark it `⟨evidence missing⟩` or leave it out.
4. **Test each item for being changeable by OD.** Three questions: can OD change this by itself (no gate outside OD)? Is
   it reversible? Will next month's inputs show whether it worked? An item that fails the first question is not an
   adjustment but an escalation: send it to `od-decision-routing` (strategy and priority: the OD lead or the deciding role named in the current approval policy, look up; technical: COP).
5. **Choose exactly one.** Preference order, which is a working rule of this skill, not of the Department OS:
   a. an item behind a crossed intervention threshold or an escalation trigger (`07-metrics.md`, `09-risks.md`);
   b. an item that recurred across more than one input or more than one month;
   c. the cheapest reversible change that addresses the item.
   Say why this one and not the others in one sentence.
6. **State the adjustment as an action**, with a role as owner (never a name), a date, and the observable that will
   show it worked: "From ⟨date⟩, ⟨role⟩ does ⟨X⟩; we will see it in ⟨metric or record⟩ at the next retro."
7. **Record who decided it.** The operating rhythm says "decided adjustment" without naming the decider:
   `⟨decider role for the monthly adjustment, to confirm with the OD lead⟩`. This skill's authority is `draft`: it
   prepares the record and proposes the one change; the decider takes it. If the change touches a row of the
   decision-rights table (priority, rollout, standards, investment), the usual route applies via `od-decision-routing`.
8. **Park the rest.** Carry unchosen items to the parking list with the month they first appeared; two months parked
   is a signal for rule (b) next time.
9. **Hand the one adjustment on:** into the next COP input, or to the deciding role named in the current approval policy (look up), if others must act; into `od-context-freshness`
   (planned) if the adjustment is a change to a context file.

## Decision table: which item becomes the adjustment

| Situation | Choose |
|---|---|
| A metric crossed its intervention threshold and nothing was changed last month | The item addressing that metric, if OD can change it; otherwise escalate and choose the next item |
| An escalation trigger in the risk register was hit | The item that lowers the cause, not the symptom |
| Same item appeared in two months | It, ahead of newer items |
| Last month's adjustment did not work | Rework it or replace it, and say which; the check result is itself an input |
| Two items equal | The reversible and cheaper one |
| No evidence-backed item at all | Record "no adjustment: no evidence-backed candidate", with the inputs read; do not invent one |

## Output

[`assets/retro-record.md`](assets/retro-record.md), kept with the month's COP outputs and any ODEC records used. The operating rhythm
file deliberately **excludes agenda templates and participants as names**; the record therefore has no agenda and lists
roles only.

## What is still open

- **Who decides the adjustment** and who attends: not stated in the sources (see step 7).
- **Where the record is kept** (a SharePoint list, the OD Teams site, the decision log): the Department OS has a
  `decision-log.md` concept "not in the core", but no location for it is recorded. `⟨location, to confirm⟩`.
- **Incident definition and source.** The input is called "incidents"; no incident register is named in the sources
  read. Candidates in the sources are the Blocker Register (a derived view of list fields), the ODEC/COP "issues and
  feedback" inputs, and support tickets named as an early indicator in `09-risks.md` with no source system.
  `⟨incident source, to confirm⟩`.
- **Escalation window** of ODEC and COP is `⟨to confirm⟩` in the operating rhythm; `od-scorecard-reporting` uses "one round".
- **Cadence beyond monthly.** "At least monthly" is the rule; whether quarterly deeper retros exist is not recorded.

## Do not

- Do not propose a new tracker, slide or system as the adjustment when removing or merging one would address the item.
- Do not end with a list of actions. One adjustment; the rest is parked.
- Do not name individuals in the record: roles only.
- Do not count an intention as a result: the check at the next retro needs an observable.
- Do not pick an adjustment that needs a gate outside OD and call it done; route it.
- Do not use the retro to re-open decisions already routed through COP or the deciding role, only to learn from them.
