---
type: Skill Asset
title: Hygiene report
description: The quarterly context-freshness report - script output pasted in, findings with owners and actions, the manual checks, and the gap-list comparison - drafted by the assistant, decided by the owners.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [all, practice, template]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Context hygiene report - ⟨quarter⟩

| | |
|---|---|
| **Run date** | ⟨YYYY-MM-DD, the `--today` used⟩ |
| **Thresholds** | sources_read stale after ⟨90⟩ days; valid-until flagged ⟨30⟩ days ahead |
| **Command** | ⟨the exact command line used⟩ |
| **Drafted by** | assistant, read-only; decisions by the owners named below |

## 1 · Headline

⟨Three lines at most: what expires next, how many files are overdue, whether any skill rests on an expired source.⟩

## 2 · Bundle files (owner: OD lead)

⟨Paste the bundle table from the script.⟩

| File | Finding | Skills that copy it (from the cross table) | Action requested | Decision by owner |
|---|---|---|---|---|
| ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨open⟩ |

## 3 · Skills (owner: registry owner)

⟨Paste the skills table and the cross table.⟩

| Skill | Why listed | Action requested | Decision by owner |
|---|---|---|---|
| ⟨⟩ | ⟨stale · stale with gaps · rests on an out-of-date source⟩ | ⟨⟩ | ⟨open⟩ |

## 4 · Registry marks

| Mark | Date | Age (days) | Figures that rely on it | Action |
|---|---|---|---|---|
| data_as_of | ⟨⟩ | ⟨⟩ | ⟨e.g. targets and actuals quoted by lane skills⟩ | ⟨⟩ |
| graph_as_of | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ |
| flows_as_of | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ |

`open_gaps` entries: ⟨count⟩ (previous quarter: ⟨count⟩).

## 5 · Manual checks

| Check | Result |
|---|---|
| Figure finder run over the skills; hits triaged | ⟨file · hit · rewritten / technical constant / method⟩ |
| Bundle README gap list against `open_gaps` | ⟨closed · still open · changed, per item, with the source⟩ |
| Vault notes relied on: stamps noted | ⟨note · stamp · reviewed or machine extract⟩ |

## 6 · Not assessed

⟨Skills with unresolved `derived_from` paths; files without front matter; anything the script could not read.⟩

## 7 · Rules kept

- [ ] No date in any file was edited to clear a finding
- [ ] No `sources_read` was bumped without a re-read
- [ ] No file was opened for writing by the script
- [ ] Every finding has an owner and an action
