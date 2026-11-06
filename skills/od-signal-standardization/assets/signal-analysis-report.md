---
type: Skill Asset
title: Signal analysis report
description: The ten-section report the signal skill writes, so its output is a defined format rather than prose.
resource: ../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [signals, report, template]
generated: { by: claude-code/1, at: 2026-08-25T00:00:00Z }
---
# Signal Analysis — ⟨Machine⟩ ⟨(EQ id)⟩

| | |
|---|---|
| **Plant** | ⟨plant⟩ |
| **Machine** | ⟨name⟩ ⟨(EQ id)⟩ · ⟨vendor⟩ ⟨PLC model⟩ |
| **Process group** | ⟨one of the process groups⟩ · family ⟨Rubber / Plastic / Metal / Assembly⟩ |
| **Capability in scope** | ⟨one of the capability templates, or "inventory only"⟩ |
| **Analyst / date** | ⟨name⟩ · ⟨date⟩ |
| **Overall verdict** | ⟨ready / gaps block delivery / inventory incomplete⟩ |

---

## 1 · How the machine works

⟨Three or four sentences: what it makes, what one cycle is, where it waits, and what makes a
part good. If this cannot be written, the context is not yet sufficient and everything below
is a guess.⟩

**Cycle boundary.** ⟨what starts and ends a cycle, and which signal marks each⟩
**Wait states.** ⟨where it waits, and on what — operator, upstream, downstream, heating⟩
**Good-part definition.** ⟨what makes a part countable as good, and at which station⟩

## 2 · Sources used

| Source | Obtained | Contributed | Confidence |
|---|---|---|---|
| ⟨PLC program ⟨version/date⟩⟩ | ⟨yes/no⟩ | ⟨step chain, mode word, alarm table⟩ | ⟨High / Medium / Low⟩ |
| ⟨Tag / symbol export⟩ | | ⟨candidate names + addresses⟩ | High for existence, low for meaning |
| ⟨Sequence / flow chart⟩ | | ⟨cycle boundaries, wait states⟩ | |
| ⟨Layout⟩ | | ⟨station order, buffers, count point⟩ | |
| ⟨Machine handbook⟩ | | ⟨modes, alarm codes, units, interfaces⟩ | |
| ⟨HMI observation⟩ | | ⟨what the operator actually uses⟩ | Medium — high for importance |
| ⟨Live data-point config / OPC UA browse⟩ | | ⟨existence verdicts⟩ | Verified |
| ⟨Proven instance at ⟨plant⟩⟩ | | ⟨baseline signal list⟩ | |
| ⟨Operator / setter conversation⟩ | | ⟨what actually goes wrong⟩ | |

**Context situation:** ⟨full context · tag export only · handbook only · nothing but the
machine · adopting a proven instance⟩

## 3 · Signal inventory

| Candidate (as found) | Canonical name | Area | Dir | Source | Exists? | Unit | Collection | Action |
|---|---|---|---|---|---|---|---|---|
| ⟨as it appears⟩ | ⟨CanonicalName⟩ | ⟨machine-state⟩ | in | ⟨source⟩ | ⟨yes ⟨uuid⟩ / no / unverified⟩ | ⟨unit⟩ | ⟨transition / sample @ n s⟩ | ⟨use / rename / register / drop⟩ |

**Legend — Action.** `use` canonical already · `rename` variant → canonical · `register`
derived output to be created on the edge platform · `drop` not needed, recorded as a decision.

## 4 · Functional areas and priority

⟨Paste the `--cluster` output, or summarise:⟩

| Rank | Area | Signals | Canonical | Setpoints | Note |
|---|---|--:|--:|--:|---|
| ⟨1⟩ | ⟨machine-state⟩ | ⟨n⟩ | ⟨n⟩ | ⟨n⟩ | ⟨⟩ |

**Standardize first:** ⟨the two or three families that unblock the most⟩

## 5 · Standard and data model

| | |
|---|---|
| Cluster | ⟨C01…C12⟩ |
| Standard KPIs required | ⟨from the cluster KPI set⟩ |
| Public data model available | ⟨EUROMAP 77/83/84 · OPC UA for Machinery · PackML · none⟩ |
| Machine already exposes it? | ⟨yes — route changes / no / not checked⟩ |
| State model | ⟨PackML mapping, or the raw code table with meanings⟩ |
| Deltas from the standard | ⟨only what this machine does differently⟩ |

## 6 · Capability coverage

| Capability | Requires | Present | Missing | Verdict |
|---|---|---|---|---|
| ⟨oee⟩ | ⟨MachineStatus, TotalPartCounter, CycleTime, StandardSpeed⟩ | ⟨…⟩ | ⟨…⟩ | ⟨buildable / blocked⟩ |

**For each missing signal, say which problem it is:**

| Missing signal | Cause | Owner |
|---|---|---|
| ⟨name⟩ | ⟨PLC does not expose it / not configured on the edge platform / no sensor exists⟩ | ⟨engineering / integration / investment⟩ |

## 7 · Findings

⟨From `analyze_signals.py`. Blockers first.⟩

| Severity | Finding | Detail | Fix |
|---|---|---|---|
| ⟨BLOCKER⟩ | ⟨raw-plc-tag⟩ | ⟨`_part0_io`⟩ | ⟨name it from the data model⟩ |

## 8 · Recommended actions

| # | Action | Owner | Depends on | By |
|---|---|---|---|---|
| 1 | ⟨rename ⟨variant⟩ → ⟨canonical⟩ before anything consumes it⟩ | ⟨⟩ | — | ⟨⟩ |
| 2 | ⟨register ⟨derived signal⟩ on the edge platform⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ |
| 3 | ⟨confirm unit convention for ⟨signal⟩⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ |

**Renaming a live signal is a breaking change**, not a tidy-up. Any rename above needs its
consumers listed and a migration, or it stays as-is with the deviation recorded.

## 9 · Open questions

- ⟨what could not be established, and who can answer it⟩

## 10 · Feeds

⟨`od-requirements-breakdown` §5 Tags of Interest · `od-equipment-integration` (guidance route) ·
`od-node-red-flows` config · the Machine CV⟩
