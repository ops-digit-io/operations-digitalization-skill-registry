---
type: Skill Reference
title: Staleness signals
description: How each layer of the OD knowledge system marks freshness - bundle file, skill, registry, knowledge base note - what each mark proves and what it does not, with the field names and the conventions behind them.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [all, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Staleness signals

The layers are listed from the source outwards. This file describes the marks and what they prove; it carries no counts or dates of the current estate.

## 1. Department OS bundle files (the context layer)

The bundle README, section "How to use", says: keep the front matter (`owner`, `review-cadence`, `last-verified`;
critical files also `valid-until`, `verification-method`, `source-of-truth`) current, because "freshness is what
keeps the layer trustworthy".

| Field | Meaning | Carried by |
|---|---|---|
| `owner` | The person or role who answers for the file | all files with front matter |
| `review-cadence` | How often it should be re-checked: weekly, monthly, quarterly or yearly. Metrics pages are expected to drift fastest | all |
| `last-verified` | When someone last checked it. Files verified in one pass share a date, so they fall due together | all |
| `valid-until` | A hard expiry. Only critical files carry it | A small set of critical files (typically strategy, metrics, decision rights, SWOT and the systems-of-record module); read the set from the front matter |
| `verification-method` | How to verify: for decision rights, "confirm with OD lead and MPEE head at quarterly review" | critical files |
| `source-of-truth` | Where the content really lives | critical files |

What it proves: someone said the content was right on `last-verified`. What it does not prove: that anyone
re-checked the underlying sources. Some bundle values are `⟨…⟩` (to confirm); a file whose date is a placeholder is
reported as "no usable last-verified", not silently skipped.

## 2. Skills

| Field | Meaning | Source of the convention |
|---|---|---|
| `metadata.sources_read` | The date the source data was read. It replaced an earlier `last_verified` that asserted a verification nobody performed | `docs/okf-conventions.md`; `docs/derivation.md` |
| `metadata.status` | `draft`, `stable` or `deprecated` | `scripts/verify_okf.py` |
| `metadata.derived_from` | What the skill was built from: a bare path or a sentence | the brief; `docs/okf-conventions.md` |
| `verified: {by, at}` | A human reading, with an actor. **Absent on every skill**; the trust tier is "unverified" | `docs/okf-conventions.md` |
| `⟨…⟩` in prose | An unresolved gap: a fact the sources did not give | the registry's honesty rule in `od-context` |
| Dated figures in prose | Should not exist in skills. If one is found, rewrite it to "how to read it live" | the no-company-figures rule |

What it proves: when a person or agent last read the source. What it does not prove: that the source was current,
or that the skill still matches it.

## 3. The registry

| Mark in `registry.yaml` | Covers |
|---|---|
| `data_as_of` | Scorecard / Power BI figures |
| `graph_as_of` | Portfolio and ledger figures from the knowledge bundle |
| `flows_as_of` | The Node-RED corpus and the machine estate |
| `registry.status` | `draft`: "unverified - drafted from the bundle, not yet read line by line" |
| `open_gaps` | A list of questions the sources did not answer (count it at run time and compare with the previous run) |

These three marks are what a figure inside a skill should be read against. A skill that quotes an equipment target
is only as current as `data_as_of`.

## 4. Knowledge base notes (department knowledge base)

The knowledge base is read-only for the registry. Its notes carry their own stamps, which the report should note when a
skill relies on them:

| Stamp | Example | Reading |
|---|---|---|
| `enriched:` | "<profile version>, <date>; <fulltext version>, <date>" | When the generated profile block was last built |
| `generated:` with `review_status` | "AI-generated ... not reviewed by a human" | The note is a machine extract, unreviewed |
| Export date in prose | "SharePoint exports of <date>" | The date of the underlying list, not of the note |
| ODEC Facts slide dates | slide text with dates and `Archive:` paths | The date of the call; open the archive slide before using it as evidence |

## 5. What cannot be checked mechanically

- Whether any figure that slipped into prose is still the figure in the source. Find them with the figure finder and rewrite them.
- Whether a role named in a skill still holds the job. Named owners are an open gap throughout.
- Whether a statement the skills copy from the knowledge base is still true on the shop floor.
- Whether a `stable` skill earned that status; the status is set by the registry owner.
