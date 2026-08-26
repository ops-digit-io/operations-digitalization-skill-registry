---
type: Skill Reference
title: Plant instance map
description: Which Node-RED instance belongs to which plant, how each mapping was established, and the plants the flow corpus cannot speak for.
resource: ../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [data-availability, node-red, coverage]
generated: { by: claude-code/1, at: 2026-08-26T00:00:00Z }
---

# Plant instance map

Step 4 reads the flow corpus, and the corpus is organised by **instance**
(`ct-oesl-<code>-nodered-<env>`) while everything else is organised by **plant**. Nothing in
the bundle states the mapping, so it was derived — and each entry records *how*, because a
step-4 verdict is only as good as the mapping under it.

| Code | Plant | Established by |
|---|---|---|
| `cshz` | Changshu | **topic** — `MFS/AS/CHN/CSHZ` in the flows |
| `qda` | Qingdao | **topic** — `OESL/AS/CHN/QDA` |
| `spr` | SunPrairie | **topic** — `OESL/NA/USA/SPR` |
| `sub` | Subotica | **machines** — 20 machine names shared with Subotica's rows, next best 5 |
| `tsaz` | Timisoara | **machines** — 13, next best 9 |
| `som` | Somersworth | **machines** — 12, next best 4 |
| `mak` | Mako | **machines** — 10, next best 5 |
| `krb` | Karben | **machines** — 9, next best 5 |
| `pogz` | PontaGrossa | **machines** — 4, next best 3 |
| `cal` | Caluire | **prefix** |
| `car` | Carei | **prefix** |
| `del` | Delicias | **prefix** |
| `dol` | DolneVestenice | **prefix** |
| `vac` | Vac | **prefix** |
| `ccn` | Changchun | **abbreviation** — no corroborating evidence |
| `mty` | Monterrey | **abbreviation** — no corroborating evidence |
| `wth1`…`wth4` | Waltershausen | **abbreviation** — four instances, no corroborating evidence |
| `mpee` | — | the department's own test instance, not a plant |
| `nomz` | **unresolved** | 2 instances that map to no plant and are excluded from step 4 |

**`nomz` is worth resolving.** It is the only unmapped code, and Northeim is the largest plant
with no flow evidence at all — 87 machines, 83 of them `INTEGRATED`. The two facts fit
together and that is exactly why they are written here as a question rather than merged into
the table. Confirm it against the instance itself; do not assume it.

## The 16 plants the corpus cannot speak for

Andrezieux · Auburn · Dannenberg · HannMünden · HannoverStöcken · Jeonju · Korbach · Kranj ·
Montemorelos · Northeim · Oedelsheim · Ostrava · Rennes · SanLuisPotosi · Tanger · Tlalnepantla

Four of them are large: **Northeim (87 machines), Tlalnepantla (82), Auburn (60), Rennes
(58)**. For any of the sixteen, step 4 returns *unproven* — never *absent*. The edge platform
has to be checked directly, and the answer recorded, because otherwise the next person repeats
the same lookup and reaches the same non-answer.

## Why this is not hard-coded silently

A mapping derived by abbreviation could be wrong, and a wrong mapping produces a confident
step-4 verdict about the wrong plant — the one failure mode worse than no verdict. The script
therefore reports any instance it cannot map instead of dropping it, and this table says which
entries rest on evidence and which on inference. Six rest on inference.
