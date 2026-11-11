---
type: Skill Reference
title: Review template
description: "The review output: region-grouped verdict tables (OD-owned and OD-relevant), visible sub-scores, open questions per region."
resource: ../SKILL.md
status: draft
tags: [invest-screen, gate, department-package]
---
> Transcribed from the department package `investment-checking.zip/reference/review-template.md` (the master).

# Review template + report skeleton + worked example

## Per-item review block

```
### [<ID>] <Title> — <Location> (<Cluster = region>), <Year>, <Status>
Class: <OD-owned | OD-touching | Cross-region interlock>   Owner dept: <Department>
Trigger signal: <the word(s)/reason it entered scope>

Software/IT-footprint gate: <Clear | Blocked — reason>
Scores: BC <0-2> · Compound <0-2> · Interface <0-2> · Complexity <0-2> · Interlock <0-2>  (S=<sum>)
VERDICT: <Go | PoC-first | Reduce-complexity | Hold | Reject | Blocked>
Decisive reason: <one line>
OD action / question: <what OD should raise or do next; ⟨open⟩ where unknown>
```

## Report skeleton (the deliverable)

**Group the shortlist by region (`Cluster`) — this is the default structure.** OD runs a separate controlling cycle per region, so the report must map onto them. The `Cluster` field has five values: `EMEA WEST`, `EMEA EAST`, `AMERICAS`, `APAC`, and `OESL` (global/cross-region; screen with whichever region owns delivery). Only depart from region grouping if the user explicitly asks for a different cut (e.g. by status, by owner department).

1. **Header** — snapshot date + link to the live Invest list + "list is source of truth; this is a dated analysis".
2. **Coverage line** — total rows screened, counts by class (OD-owned / OD-touching / interlock / not-involved), and a per-region count line.
3. **Cross-region themes** — put these *before* the regional sections: the capabilities being bought plant-by-plant in multiple regions (e.g. vision/AI inspection, traceability, the software blind spot). This is the argument for one OD standard across the regional cycles.
4. **One section per region** (`EMEA WEST`, `EMEA EAST`, `AMERICAS`, `APAC`, then `OESL`/global). Each section carries:
   - an **OD-owned** table for that region,
   - an **OD-relevant (cross-department)** table: `ID · Title · Dept · Location · Class · Gate · Verdict · OD action`,
   - a short list of light-touch / ⟨confirm⟩ items,
   - **region open questions** — what OD takes into *that* region's controlling cycle.
5. **Software/IT-footprint gate — items that trip it** (consolidated across all regions; this is the blind spot).
6. **Questions for the invest review** — the consolidated set OD takes forward.

Per-item action blocks (below) are used inside the regional sections for anything Blocked / PoC-first / Reduce-complexity / needs OD to engage. Go/Reject items can stay table-only unless notable.

Output in **English**. Keep reasoning visible.

## Worked example (from a real screen)

### [445] Tia Portal licence (Software for Siemens PLC) — Kranj, 2026, live
Class: OD-touching   Owner dept: MANUFACTURING ENGINEERING
Trigger signal: "software", "licence", "Siemens PLC" — software footprint on an ME row.

Software/IT-footprint gate: **Blocked** — a PLC-programming software license with recurring cost and a runtime that lands on an engineering PC; ownership after go-live and approved-list status ⟨open⟩; who carries the renewal ⟨open⟩.
Scores: BC 1 · Compound 1 · Interface 1 · Complexity 1 · Interlock 1 (S=5) — *not computed to a Go; gate dominates.*
VERDICT: **Blocked**
Decisive reason: recurring-cost software with an unnamed owner and unclear approved-list status — resolve footprint before it is waved through as "just an ME license".
OD action / question: confirm license type + renewal owner, check against approved software list, and decide whether OD or ME operates it. Small €, but it is the exact pattern (indirect software on an equipment row) OD must not miss.

> Note how the gate overrides an otherwise middling numeric score — that is the point of making it a hard gate.
