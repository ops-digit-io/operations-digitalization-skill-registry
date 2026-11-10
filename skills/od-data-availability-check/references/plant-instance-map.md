---
type: Skill Reference
title: Plant instance map
description: Which Node-RED instance belongs to which plant, how each mapping was established, and how to find the plants the flow corpus cannot speak for. No counts.
resource: ../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [data-availability, node-red, coverage]
generated: { by: claude-code/1, at: 2026-08-26T00:00:00Z }
---

# Plant instance map

Step 4 reads the flow corpus, and the corpus is organised by **instance**
(`ct-oesl-<code>-nodered-<env>`) while everything else is organised by **plant**. Nothing in
the bundle states the mapping, so it was derived - and each entry records *how*, because a
step-4 verdict is only as good as the mapping under it. Re-check the mapping against the
instance before relying on an entry that rests on inference.

| Code | Plant | Established by |
|---|---|---|
| `cshz` | Changshu | **topic** - `MFS/AS/CHN/CSHZ` in the flows |
| `qda` | Qingdao | **topic** - `OESL/AS/CHN/QDA` |
| `spr` | SunPrairie | **topic** - `OESL/NA/USA/SPR` |
| `sub` | Subotica | **machines** - machine names shared with the plant's Machine List rows, clearly more than any other plant |
| `tsaz` | Timisoara | **machines** |
| `som` | Somersworth | **machines** |
| `mak` | Mako | **machines** |
| `krb` | Karben | **machines** |
| `pogz` | PontaGrossa | **machines** (thin margin over the next best plant: re-check) |
| `cal` | Caluire | **prefix** |
| `car` | Carei | **prefix** |
| `del` | Delicias | **prefix** |
| `dol` | DolneVestenice | **prefix** |
| `vac` | Vac | **prefix** |
| `ccn` | Changchun | **abbreviation** - no corroborating evidence |
| `mty` | Monterrey | **abbreviation** - no corroborating evidence |
| `wth1`...`wth4` | Waltershausen | **abbreviation** - several instances, no corroborating evidence |
| `mpee` | - | the department's own test instance, not a plant |
| `nomz` | **unresolved** | instances that map to no plant and are excluded from step 4 |

**`nomz` is worth resolving.** It is the only unmapped code, and a large plant with no flow
evidence at all is a candidate for it. The two facts may fit together, which is exactly why
they are written here as a question rather than merged into the table. Confirm it against the
instance itself; do not assume it.

## Finding the plants the corpus cannot speak for

Take the plant list (`Graph/Plants`) and remove every plant that has a mapped instance in the
table above. What remains has no flow evidence. Rank the remainder by the number of machines
the Machine List holds for it, counted live: the large ones are where a missing answer hurts
most.

For any plant on that list, step 4 returns *unproven* - never *absent*. The edge platform has
to be checked directly, and the answer recorded, because otherwise the next person repeats the
same lookup and reaches the same non-answer.

## Why this is not hard-coded silently

A mapping derived by abbreviation could be wrong, and a wrong mapping produces a confident
step-4 verdict about the wrong plant - the one failure mode worse than no verdict. The script
therefore reports any instance it cannot map instead of dropping it, and this table says which
entries rest on evidence and which on inference (abbreviation entries are inference).
