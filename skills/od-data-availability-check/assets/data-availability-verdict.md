---
type: Skill Asset
title: Data availability verdict
description: The defined output of an availability check - the six steps, the gap named, the route, and what still has to be checked outside the bundle.
resource: ../SKILL.md
status: stable
tags: [data-availability, template, verdict]
---

# Data availability verdict — ⟨plant⟩ ⟨· machine⟩

**Request.** ⟨the question that was asked, in the requester's words⟩
**Asked by.** ⟨name, role⟩ · **Moment of use.** ⟨when the answer gets looked at, and what
happens next⟩
**Signals needed.** ⟨canonical names⟩

## Verdict

⟨**Supportable** · **Supportable with a named reduction** · **Not supportable as asked**⟩

⟨One sentence naming the step it turns on. Steps 2, 4 and 5 look identical from a dashboard
and are three different problems with three different owners — say which one this is.⟩

## The six steps

| # | Step | Verdict | What was found | Route |
|---|---|---|---|---|
| 1 | Machine produces it | ⟨ok / blocker⟩ | ⟨n machines in scope⟩ | ⟨measurement gap → capital request⟩ |
| 2 | Machine integrated | ⟨⟩ | ⟨n of m INTEGRATED; k blank⟩ | ⟨od-equipment-integration, assessment route⟩ |
| 3 | Connector and concept | ⟨⟩ | ⟨vendor → connector, status USE?⟩ | ⟨connector gap → barrier⟩ |
| 4 | Signal flowing and standardized | ⟨⟩ | ⟨found / not found / unproven⟩ | ⟨od-signal-standardization⟩ |
| 5 | Fit for use | ⟨⟩ | ⟨granularity, freshness, completeness — from the platform⟩ | ⟨data gap, with the reason⟩ |
| 6 | Already answered | ⟨⟩ | ⟨library or portfolio hits⟩ | ⟨od-use-case-standardization⟩ |

## What can be answered today

⟨Be specific. "Availability per press for the last 90 days at 10-second resolution" — not
"some OEE data exists".⟩

## What cannot, and why

| What is missing | Which gap | Owner | What it would take |
|---|---|---|---|
| ⟨signal / period / granularity⟩ | ⟨measurement · integration · standardization · fitness · definition⟩ | ⟨name⟩ | ⟨estimate⟩ |

## Still to be checked outside the bundle

- **Step 5 in full** — granularity, freshness and completeness in Databricks and the Azure
  Storage Account. No source in the bundle carries this.
- ⟨any step-4 blocker, against the edge platform, before it is reported as absent⟩
- ⟨history depth: the earliest integration_date of every machine in scope⟩

## Dependency recorded

⟨Where this was logged so it stays visible after the requester has moved on — the use case
record, with the class: `MACHINE INTEGRATION` is already a recorded dependency class.⟩

## Turnaround

⟨Only after step 5 is answered. Before that, no date.⟩
