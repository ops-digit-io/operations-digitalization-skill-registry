---
type: Skill Asset
title: Event definition canvas
description: One canvas per use case - plant sentence, objects, events, time axis, signal classification, object relation, archetype class, method and ETL, open gaps.
resource: ../SKILL.md
status: draft
tags: [all, practice, template]
---
# Event definition canvas - <use case> · <plant>

| | |
|---|---|
| **By / date** | <role> · <date> |
| **Draft status** | Draft; the key user confirms identifier source and event definitions |

## 1 The request as said
<plant sentence> · requester role <role> · decision that follows <decision> · named owner <role>

## 2 Objects
| Object | Identifier | Carried in (PLC / MES / ERP / manual) | Stable per cycle |
|---|---|---|---|
| <serial / order / part / tool / recipe / batch / carrier> | <tag or field> | <source> | <yes / no / to confirm> |

## 3 Events and time
| Event | Class (source / derived) | Rule or tag | Object it happens to | Time axis (live / cadence / entry) |
|---|---|---|---|---|
| <event> | <source or derived> | <tag or rule> | <object> | <axis> |

## 4 Signal classification
| Signal | Sensor value / source event / derived event / identifier / master data | Notes |
|---|---|---|
| <signal> | <class> | <resolution, scaling, mapping table needed> |

## 5 Object relation to time-series
Needs production metadata: <yes / no> · Identifier source: <named / missing> · Verdict: <served / data gap, routed to mi-data-availability>

## 6 Structure and sharpness
Planning level <machine / cell> · MES or ERP present <yes / no> · Resolution fine enough <yes / no / to confirm>

## 7 Archetype
Class <cross-process / per-process / unique> · Action <start with priority / start / impact analysis first / just do> · Category <name> · Reason <...>

## 8 Methods and ETL
| Method | ETL or analytics job | New or existing | Batch or streaming |
|---|---|---|---|
| <method> | <job> | <new / existing> | <mode> |

## 9 Open gaps and questions
<gap> · <who supplies it> · <by when>
