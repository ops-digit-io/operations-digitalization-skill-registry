---
type: Skill Reference
title: Triage and actions
description: Each kind of flag the freshness script raises, who owns it, what to do, and the first run of 2026-11-05 as a dated worked example - open it when turning the script output into a hygiene report.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [all, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Triage and actions

## 1. How the script decides

| Check | Rule | Source of the rule |
|---|---|---|
| Bundle: expired | `valid-until` is before today | the field itself |
| Bundle: expires soon | `valid-until` within `--soon` days (default 30) | script default |
| Bundle: review overdue | `last-verified` plus the cadence length is before today. Cadence lengths: weekly 7, monthly 31, quarterly 92, yearly 366 days | script convention, not a department rule |
| Bundle: no usable date | cadence given but `last-verified` is missing or a placeholder | script |
| Skill: stale | `sources_read` older than `--threshold` days (default 90) | script default, near the quarterly cadence |
| Skill: priority | stale **and** at least one unresolved `⟨…⟩` marker in SKILL.md or `references/` | the skill map row |
| Skill: rests on an out-of-date source | a full `ops-knowledge-graph/...md` path in `derived_from` points to a file that is expired or overdue | script (`--cross`) |
| Registry: old mark | `data_as_of`, `graph_as_of` or `flows_as_of` older than the threshold | script |

Paths in `derived_from` that use braces or ellipses (`{playbook,tasks}`, `.../`) cannot be resolved and are counted,
not guessed. A skill whose sources are listed that way is only partly covered by the cross check.

## 2. Flags, owners, actions

| Flag | Owner | Action | Do not |
|---|---|---|---|
| EXPIRED | The OD lead, who owns the Department OS | Ask for a re-verify using the file's own `verification-method`; note which skills copy it | Do not extend `valid-until` |
| EXPIRES SOON | The OD lead | Put on the review agenda; tell dependent skill owners | Do not wait for the date |
| REVIEW OVERDUE | The OD lead | Ask for a re-verify; weekly-cadence files (the metrics pages) are expected to drift fastest | Do not treat as wrong, only as unchecked |
| Skill priority (stale and gaps) | The registry owner | Ask whether the gaps were answered since the read; if so, re-read the sources | Do not close a gap from memory |
| Skill stale, no gaps | The registry owner | Spot-check one quoted figure against its source | Do not bump `sources_read` without a re-read |
| Rests on an out-of-date source | The registry owner, with the file's owner | Re-read the source; update the skill; then update `sources_read` | Do not update the date first |
| Old registry mark | The registry owner | Request a new Scorecard or graph export; re-quote the figures | Do not edit the mark |
| Cannot assess | The registry owner | Fix the front matter | - |

## 3. First run, 2026-11-05 (dated worked example)

Run read-only on 2026-11-05 against the registry working tree, the Department OS bundle and `registry.yaml`.
The numbers are that day's output, not a standing state.

**Bundle (38 files with front matter, 14 flags in 13 files).**

- `valid-until 2026-11-10`, five days away: strategy, metrics, decision-rights, swot and the systems-of-record
  module. The decision-rights file carries the decision table that `od-decision-routing` and `od-cybersec-gate`
  copy; it is the highest-leverage review on the list. A re-run dated 2026-11-12 reported all five as `EXPIRED`.
- `REVIEW OVERDUE`: the four lane metrics pages and the department metrics page (weekly cadence, last verified
  2026-08-10, 80 days late), plus objectives, service catalog, risks and portfolio (monthly, 56 days late).
- 37 of 38 files carry `last-verified: 2026-08-10`. That is the date of one verification pass, so everything
  falls due together.

**Skills.** No skill was stale at the 90-day threshold; the oldest `sources_read` was 2026-08-10 (87 days). The
weak point is not the skills' own dates but the sources they name: the cross check listed 12 skill-and-source pairs
where the named bundle file was overdue (risks, portfolio, service catalog and metrics pages), and 17 `derived_from`
paths could not be resolved.

**Registry marks.** `data_as_of` 2026-08-10 (87 days), `graph_as_of` 2026-08-24 (73), `flows_as_of` 2026-08-25
(72). 65 `open_gaps` entries.

**What this says.** The registry is young enough that skills are not stale; the **context layer behind them reaches
its first expiry on 2026-11-10**. The quarterly hygiene has most value now, and a report should lead with the five
expiring files.

## 4. Reading the bundle gap list against `open_gaps`

The bundle README lists nine open gaps (named owners; targets and thresholds; value delivery cycle; named lane
owners; adoption and recipient feedback; systems detail; data platform detail; decision counterparts; naming).
Each quarter, mark every item **closed**, **still open** or **changed**, with the source that shows it. Do not close
an item because a skill papered over it: a skill that writes `⟨…⟩` for the same gap is evidence the gap is still
open.

## 5. Not covered, on purpose

- Fixing any flag.
- Judging whether a bundle file is right; only whether it is current by its own marks.
- The vault's generated notes: checked only for their stamps (see [`staleness-signals.md`](staleness-signals.md)).
