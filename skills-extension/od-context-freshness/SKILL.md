---
name: od-context-freshness
description: >-
  Run the quarterly freshness check that keeps every other OD skill honest - find the
  knowledge-bundle files whose valid-until has passed or whose review is overdue, the
  skills whose sources_read is old and that still carry unresolved gaps, the skills that
  rest on an out-of-date source, and the registry data marks; then draft the hygiene report.
  Read-only on the registry; includes a small stdlib script. Use at the start of each
  quarter, before relying on a decision table or a figure, when a valid-until date is near,
  or when someone asks whether the context behind a skill is still true.
license: MIT
allowed-tools: Read Grep Glob
metadata:
  id: od-context-freshness
  tier: practice
  lane: all
  new_state_lane: "Extension, deepens Spine"
  new_state_step: "Supporting spine"
  owner_role: human:jakob.gabriel
  authority_level: read-only on the registry; draft the hygiene report
  status: draft
  sources_read: 2026-11-05
  requires: [dept-os]
  derived_from:
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/OD_Skill_Map.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/README.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/00-core/08-decision-rights.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/00-core/14-glossary.md
    - Registry registry.yaml (data_as_of, graph_as_of, flows_as_of, status, open_gaps), docs/okf-conventions.md (sources_read, verified, statuses) and docs/derivation.md, read 2026-11-05
    - Front matter of the 38 files of the Department OS bundle (owner, review-cadence, last-verified, valid-until, verification-method, source-of-truth), read by the bundled script on 2026-11-05
    - Work vault (Work-OpsDigit-Knowledge), generated and enriched stamps and review_status lines of Graph notes, ODEC Facts and Registers, and Vault conventions in the bundle, read 2026-11-05
  okf:
    type: Agent Skill
    title: Context freshness
    tags: [all, practice, hygiene, draft]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---

# Context freshness

Read `dept-os` first.

The skill map names this skill "the skill that keeps every other skill honest": a skill repository whose context
layer has silently expired gives confident wrong answers. Every other skill copies facts from the Department OS
(decision rights, risks, targets) and from the vault. This skill checks, once a quarter, whether those sources
and the skills' own dates are still current, and writes down what is not. It **repairs nothing**.

## Purpose, trigger, done

- **Trigger.** Start of a quarter (the skill map says quarterly), five weeks before a `valid-until` date, before a
  decision table or a target is quoted, or on the question "is this still true?".
- **Output.** A dated hygiene report from [`assets/hygiene-report.md`](assets/hygiene-report.md) with the script's
  tables pasted in and a decision per finding left to its owner.
- **Done.** Every finding has an owner and an action; nothing was edited to make a date look newer.

## The references and the script

| File | Use it for |
|---|---|
| [`references/staleness-signals.md`](references/staleness-signals.md) | How each layer marks freshness (bundle file, skill, registry, vault note) and what each mark does and does **not** prove |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | Which time-bound facts go stale fastest (tool status, plant tier, forum status, vocabulary, KPI basis), copy residue and orphaned ownership, handoff and agent notes |
| [`references/triage-and-actions.md`](references/triage-and-actions.md) | Each flag type, who owns it, the action, and how to read a run (what to lead with, what the typical pattern is) |
| [`references/fact-triage-and-generated-registers.md`](references/fact-triage-and-generated-registers.md) | Triage pattern for a staging pile of extracted facts (verdicts, plant buckets), limits of text extraction, honesty rules for generated registers, the masking review |
| [`scripts/context_freshness.py`](scripts/context_freshness.py) | Standard-library, read-only report. Opens files for reading only; writes only to the terminal |

## The rule

**A date is a claim about a read, not about the world.** `sources_read` records when the source data was read. It says
nothing about whether that source had been re-verified. A skill read on one date from a bundle file last verified
months earlier is only as fresh as that earlier verification. The report therefore checks *both*: the skill's own date and the dates of
the sources it names (`--cross`).

## Procedure

1. **Run the script, read-only.** From the registry folder:
   ```
   python skills/od-context-freshness/scripts/context_freshness.py \
     --skills skills --registry registry.yaml \
     --bundle <path to>/ops-knowledge-graph/_knowledge/OperationsDigitalization-Department \
     --cross <folder that holds ops-knowledge-graph>
   ```
   Add `--today YYYY-MM-DD` for a repeatable report; `--threshold` (default 90 days, about one quarter) and
   `--soon` (default 30 days). Windows: set `PYTHONIOENCODING=utf-8`.
2. **Read the bundle table.** `EXPIRED` and `EXPIRES SOON` come from `valid-until`, which only the critical files
   carry; `REVIEW OVERDUE` comes from `last-verified` plus `review-cadence`
   (weekly 7, monthly 31, quarterly 92, yearly 366 days). Cadence lengths are the script's own convention.
3. **Read the skills table.** The priority list is skills that are both stale and carry unresolved `⟨…⟩` markers in
   SKILL.md or references. Templates under `assets/` are excluded because placeholders are their purpose.
4. **Read the cross table.** A skill whose named source is expired or overdue needs a human to re-read the source
   before its figures or tables are trusted. List which skill copies which file, so the owner of the file sees what
   depends on it.
5. **Read the registry marks.** `data_as_of` (Scorecard / Power BI figures), `graph_as_of` (portfolio and ledger
   figures), `flows_as_of` (Node-RED corpus and machine estate), and the number of `open_gaps`.
6. **Do the checks the script cannot.** (a) Run the figure finder (`scripts/check_no_figures.py`): skills should
   quote no company figures, so any hit is a finding (rewrite it, or record it as a technical
   constant or method value), and any dated figure that slipped in is compared with the registry marks. (b) Compare the bundle README's open-gap list with `open_gaps` in `registry.yaml`: which entries
   are closed, which are new. (c) Note the date stamps of vault notes you relied on (`enriched:`, `generated:`,
   export dates, `review_status`).
7. **Draft the report** and name an owner per finding (table in `references/triage-and-actions.md`).
8. **Hand over.** Bundle files go to the OD lead (owner of the Department OS); skills and registry marks go to the
   registry owner (`human:jakob.gabriel`). Nothing is changed by this skill.

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

## Open

- ⟨Who re-verifies a bundle file when the OD lead is away⟩: deputisation covers prioritization and rollout, not hygiene.
- ⟨Whether 90 days is the right staleness threshold⟩ for skills: it follows the quarterly cadence, nothing else.
- ⟨A `verified` field⟩: no skill has one (`docs/okf-conventions.md`: every concept is unverified), so "stale" and
  "verified" cannot yet be told apart. Until somebody adds `verified: {by: human:<id>, at: <date>}`, freshness means
  "last read", not "last checked by a human".
- Company figures inside prose (counts, euro amounts, dates of the company's own state) should not exist in skills; the figure finder in step 6 is a heuristic, so read the flagged files too.

## Do not

- Do not edit any `last-verified`, `valid-until`, `sources_read` or `*_as_of` value to clear a finding.
- Do not bump a skill's `sources_read` unless the sources were re-read in that session.
- Do not mark anything verified, expired or stable on the script's say-so alone: the report recommends.
- Do not open vault or registry files for writing; the script has no write path.
- Do not fix the findings in the same pass; report first, then let the owners decide.
