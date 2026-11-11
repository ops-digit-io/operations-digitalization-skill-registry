---
type: Skill Asset
title: Data requirements statement
description: What a use case asks of the data platform and the integration lane - identifiers, events, resolution, relation, data class and hub, master data, ETL jobs, retention, gaps.
resource: ../SKILL.md
status: draft
tags: [all, practice, template]
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
| Open gaps | <gap, owner role, route: mi-data-availability / Information Integration lane> |
| Next skill | <funnel-requirements / mi-signals / ops-analytics-asset> |
