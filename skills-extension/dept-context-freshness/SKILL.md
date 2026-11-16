---
name: dept-context-freshness
description: >-
  Finds out whether the context behind the OD skills is still true and drafts the quarterly hygiene report. Lists the knowledge-bundle files whose valid-until has passed or whose review is overdue, the skills whose sources_read is old and that still carry open gaps, the skills that rest on an out-of-date source, and the registry data marks (data_as_of, graph_as_of, flows_as_of). Use at the start of each quarter, before quoting a decision table, a target or a figure, when a valid-until date is near, or when someone asks "is this still current?" or "which skills are stale?". Reports only: it repairs nothing and never edits a date. Not for deciding who may approve (dept-decision-rights) or for explaining a term (dept-context).
license: MIT
allowed-tools: Read Grep Glob
metadata:
  id: dept-context-freshness
  aliases: [od-context-freshness]   # former name (naming convention, 2026-11-11)
  tier: practice
  lane: all
  new_state_lane: "Extension, deepens Spine"
  new_state_step: "Supporting spine"
  owner_role: human:jakob.gabriel
  authority_level: read-only on the registry; draft the hygiene report
  status: draft
  requires: [dept-context]
  okf:
    type: Agent Skill
    title: Context freshness
    tags: [all, practice, hygiene, draft]
---

# Context freshness

- Read `dept-context` first.

- The skill map names this skill "the skill that keeps every other skill honest": a skill repository whose context layer has silently expired gives confident wrong answers.
- Every other skill copies facts from the Department OS (decision rights, risks, targets) and from the knowledge base.
- This skill checks, once a quarter, whether those sources and the skills' own dates are still current, and writes down what is not.
- It **repairs nothing**.

## Purpose, trigger, done

- **Trigger.** Start of a quarter (the skill map says quarterly), five weeks before a `valid-until` date, before a
  decision table or a target is quoted, or on the question "is this still true?".
- **Output.** A dated hygiene report from [`assets/hygiene-report.md`](assets/hygiene-report.md) with the script's
  tables pasted in and a decision per finding left to its owner.
- **Done.** Every finding has an owner and an action; nothing was edited to make a date look newer.
- **Outputs:** [`references/outputs.md`](references/outputs.md) lists what this skill must deliver, to whom, and when each output is complete.

## The references and the script

| File | Use it for |
|---|---|
| [`references/staleness-signals.md`](references/staleness-signals.md) | How each layer marks freshness (bundle file, skill, registry, knowledge base note) and what each mark does and does **not** prove |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | Which time-bound facts go stale fastest (tool status, plant tier, forum status, vocabulary, KPI basis), copy residue and orphaned ownership, handoff and agent notes |
| [`references/triage-and-actions.md`](references/triage-and-actions.md) | Each flag type, who owns it, the action, and how to read a run (what to lead with, what the typical pattern is) |
| [`references/fact-triage-and-generated-registers.md`](references/fact-triage-and-generated-registers.md) | Triage pattern for a staging pile of extracted facts (verdicts, plant buckets), limits of text extraction, honesty rules for generated registers, the masking review |
| [`scripts/context_freshness.py`](scripts/context_freshness.py) | Standard-library, read-only report. Opens files for reading only; writes only to the terminal |

## The rule

- **A date is a claim about a read, not about the world.** `sources_read` records when the source data was read.
- It says nothing about whether that source had been re-verified.
- A skill read on one date from a bundle file last verified months earlier is only as fresh as that earlier verification.
- The report therefore checks *both*: the skill's own date and the dates of the sources it names (`--cross`).

## Procedure

1. **Run the script, read-only.** Needs Python 3 and nothing else (standard library). From the registry root:
   ```
   python skills-extension/dept-context-freshness/scripts/context_freshness.py \
     --skills skills --registry registry.yaml \
     --bundle <path to>/ops-knowledge-graph/_knowledge/OperationsDigitalization-Department \
     --cross <folder that holds ops-knowledge-graph>
   ```
2. **Read the bundle table.** `EXPIRED` and `EXPIRES SOON` come from `valid-until`, which only the critical files
   carry; `REVIEW OVERDUE` comes from `last-verified` plus `review-cadence`
   (weekly 7, monthly 31, quarterly 92, yearly 366 days). Cadence lengths are the script's own convention.
3. **Read the skills table.** The priority list is skills that are both stale and carry unresolved `⟨…⟩` markers in
   SKILL.md or references. Templates under `assets/` are excluded because placeholders are their purpose.
4. **Read the cross table.** A skill whose named source is expired or overdue needs a human to re-read the source before its figures or tables are trusted.
   - List which skill copies which file, so the owner of the file sees what depends on it.
5. **Read the registry marks.** `data_as_of` (Scorecard / Power BI figures), `graph_as_of` (portfolio and ledger
   figures), `flows_as_of` (Node-RED corpus and machine estate), and the number of `open_gaps`.
6. **Do the checks the script cannot.** (a) Run the figure finder (`scripts/check_no_figures.py` in the registry root, not in this skill; `python scripts/check_no_figures.py <skill-id>`):
   - skills should quote no company figures, so any hit is a finding (rewrite it, or record it as a technical constant or method value), and any dated figure that slipped in is compared with the registry marks.
   - (b) Compare the bundle README's open-gap list with `open_gaps` in `registry.yaml`: which entries are closed, which are new.
   - (c) Note the date stamps of knowledge base notes you relied on (`enriched:`, `generated:`, export dates, `review_status`).
7. **Draft the report** and name an owner per finding (table in `references/triage-and-actions.md`).
8. **Hand over.** Bundle files go to the OD lead (owner of the Department OS); skills and registry marks go to the
   registry owner (`human:jakob.gabriel`). Nothing is changed by this skill.
- Add `--today YYYY-MM-DD` for a repeatable report; `--threshold` (default 90 days, about one quarter) and `--soon` (default 30 days).
- Exit codes: 0 report written; 1 findings with `--fail-on-findings`; 2 a path or argument is wrong (the message names the flag). On 2, fix the path and rerun; do not report from a partial run.
- Windows: set `PYTHONIOENCODING=utf-8`.

## Decision table

| Finding | Means | Action | Owner |
|---|---|---|---|
| Bundle file `EXPIRED` | The file says itself that it is no longer to be trusted | Ask the OD lead to re-verify; list dependent skills; mark their quoted tables as unverified in the report | OD lead |
| `EXPIRES SOON` | Review needed before the date | Put the file on the next review agenda | OD lead |
| `REVIEW OVERDUE` | Cadence missed; content may still be right | Ask for a re-verify; no urgency unless a skill quotes it as a rule | OD lead |
| Skill stale and carries gaps | Old read and open questions | Ask whether the gaps were answered since; re-read the sources if so | registry owner |
| Skill stale, no gaps | Old read, nothing flagged open | Spot-check one figure | registry owner |
| Skill rests on an expired source | Copy may be out of date | Re-read the source, then update the skill, then (and only then) its `sources_read` | registry owner |
| Skill states a time-bound fact (tool status, plant tier, forum status, KPI basis) as current | A fresh read date does not make a moving fact current | Look the fact up live and name the source and its date in the report; list in `references/process-chain-practice.md` | registry owner |
| Registry mark older than the threshold | Figures quoted by skills may have moved | Ask for a new export of the Scorecard or graph; do not edit the mark | registry owner |

## Example: one finding (fictional)

```text
Bundle table : 08-decision-rights.md   EXPIRED (valid-until 2026-01-31)   (fictional)
Cross table  : dept-decision-rights reads it                              (fictional)
Report row   : finding = expired source | dependent skill = dept-decision-rights |
               action = ask the OD lead to re-verify; mark the skill's quoted table
               as unverified in this report | owner = OD lead | edited nothing
```

## Open

- ⟨Who re-verifies a bundle file when the OD lead is away⟩: deputisation covers prioritization and rollout, not hygiene.
- ⟨Whether 90 days is the right staleness threshold⟩ for skills: it follows the quarterly cadence, nothing else.
- ⟨A `verified` field⟩: no skill has one (`docs/okf-conventions.md`: every concept is unverified), so "stale" and
  "verified" cannot yet be told apart. Until somebody adds `verified: {by: human:<id>, at: <date>}`, freshness means
  "last read", not "last checked by a human".
- Company figures inside prose (counts, euro amounts, dates of the company's own state) should not exist in skills; the figure finder in step 6 is a heuristic, so read the flagged files too.

## Pitfalls

- Reading a fresh `sources_read` as proof the content is current: the date records a read, not a verification, so check the source's own marks too (`--cross`).
- Running without `--cross`: a skill read recently from a long-expired file looks fine.
- Fixing a finding in the same pass: the owner may disagree, and a bumped date hides the evidence.
- Trusting the figure finder as a verdict: it is a heuristic, so read the flagged files.
- Reporting after exit code 2: the run was partial, so the tables are incomplete.

## Do not

- Do not edit any `last-verified`, `valid-until`, `sources_read` or `*_as_of` value to clear a finding.
- Do not bump a skill's `sources_read` unless the sources were re-read in that session.
- Do not mark anything verified, expired or stable on the script's say-so alone: the report recommends.
- Do not open knowledge base or registry files for writing; the script has no write path.
- Do not fix the findings in the same pass; report first, then let the owners decide.

## Human gate and AI-agent notes

- An agent may run the script, read the tables, run the figure finder and draft the report with an owner per finding.
- Humans decide: the OD lead re-verifies bundle files; the registry owner updates skills and registry marks.
- The agent never edits a date to clear a finding and never marks anything verified.

## Definition of done

- The hygiene report exists with the date, the script's tables, an owner and an action per finding, and the checks the script cannot do (step 6).
- Nothing was edited to make a date look newer.

## Outputs

- [`outputs.yaml`](outputs.yaml): required outputs, criteria, checks and sign-offs.
- One run record per call: `python scripts/run_record.py new <skill-id>` (registry root).

## References

| File | Open when |
|---|---|
| [`references/staleness-signals.md`](references/staleness-signals.md) | You must say what a date, a status or a stamp does and does not prove (steps 2 to 5) |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | A skill states a time-bound fact (tool status, plant tier, forum status, KPI basis) or you meet copy residue or orphaned ownership |
| [`references/triage-and-actions.md`](references/triage-and-actions.md) | You draft the report (step 7), assign an owner per flag, or decide what to lead with |
| [`references/fact-triage-and-generated-registers.md`](references/fact-triage-and-generated-registers.md) | A staging pile of extracted facts or a generated register is about to be relied on, or a masking review is due (step 6c) |
| [`scripts/context_freshness.py`](scripts/context_freshness.py) | Step 1; run `--help` for flags. Read-only, standard library |
| [`assets/hygiene-report.md`](assets/hygiene-report.md) | You write the report (step 7) |
| [`references/background.md`](references/background.md) | You want the context and rationale; never an instruction |
| [`evals/evals.json`](evals/evals.json) | Test cases and trigger queries to run with and without this skill |
