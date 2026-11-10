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

## 3. Reading a run

Lead the report with what expires next, then what is overdue, then which skills rest on those files. The numbers
are always that day's output, never a standing state - do not carry them into a skill or a later report.

**Bundle.** Files carrying `valid-until` are the highest-leverage reviews: when one of them holds a decision table
that other skills copy (decision rights, for example), list the dependent skills next to it. `REVIEW OVERDUE` on
weekly-cadence metrics pages is the usual pattern, because they drift fastest. Files verified in one pass all fall
due together, so a quarter's worth of flags tends to arrive on the same day.

**Skills.** A young registry shows few stale skills at the 90-day threshold; the weak point is then not the skills'
own dates but the sources they name. Read the cross table first, and count the `derived_from` paths that could not
be resolved (brace or ellipsis paths) as "not assessed".

**Registry marks.** Compare each `*_as_of` mark with the run date and name the figures that rely on it. Compare the
`open_gaps` count with the previous report.

**What it says.** If the context layer behind the skills reaches an expiry soon, the quarterly hygiene has most
value that quarter, and the report should lead with the expiring files.

## 4. Reading the bundle gap list against `open_gaps`

The bundle README lists its open gaps by theme (named owners; targets and thresholds; value delivery cycle; named lane
owners; adoption and recipient feedback; systems detail; data platform detail; decision counterparts; naming).
Each quarter, mark every item **closed**, **still open** or **changed**, with the source that shows it. Do not close
an item because a skill papered over it: a skill that writes `⟨…⟩` for the same gap is evidence the gap is still
open.

## 5. Not covered, on purpose

- Fixing any flag.
- Judging whether a bundle file is right; only whether it is current by its own marks.
- The knowledge base's generated notes: checked only for their stamps (see [`staleness-signals.md`](staleness-signals.md)).
