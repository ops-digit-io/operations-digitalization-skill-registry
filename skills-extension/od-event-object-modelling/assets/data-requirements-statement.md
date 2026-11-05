---
type: Skill Asset
title: Data requirements statement
description: What a use case asks of the data platform and the integration lane - identifiers, events, resolution, relation, data class and hub, master data, ETL jobs, retention, gaps.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [all, practice, template]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Data requirements - <use case> · <plant>

Derived from the event definition canvas of <date>. Draft; nothing here connects or changes a system.

| Item | Statement |
|---|---|
| Objects and identifiers | <object: tag or field, source> |
| Events | <event: source or derived, rule, timestamp source> |
| Time resolution needed | <resolution> |
| Relation to production metadata | <serial / order / part / batch / recipe, source, or gap> |
| Data class and hub | <transactional: service bus · time-series: stream · master data: leading system> |
| Route to platform | <native / aggregation server / edge device>, reason <...> |
| Master data and leading system | <system, how received> |
| ETL jobs | <job, new or existing, batch or streaming, owner role> |
| Retention (if claims traceability applies) | <rule> |
| Handoff files | signal list, mapping tables, start/stop signals, first datasets |
| Open gaps | <gap, owner role, route: od-data-availability-check / Information Integration lane> |
| Next skill | <od-requirements-breakdown / od-signal-standardization / od-analytics-asset-build> |
