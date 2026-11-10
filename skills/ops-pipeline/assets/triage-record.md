---
type: Skill Asset
title: Triage record
description: A one-page record a key user fills in while diagnosing a broken flow, in the order that avoids the commonest wrong starts, so the next person can see what was checked and what was only assumed.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [information-integration-service, technical, node-red]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Triage record

Copy this into the ticket. Fill in each line with what you **saw**, not what you expect.
Leave `⟨...⟩` where you did not check; an unchecked line is information.

## A. The report

| Item | Entry |
|---|---|
| Flow (tab label) and instance (repository name) | ⟨⟩ |
| Symptom in one sentence (publishes nothing / wrong value / wrong timestamp / stopped after redeploy / works on test only) | ⟨⟩ |
| Asset or dashboard that shows it, and since when | ⟨⟩ |
| Reported by (role) | ⟨⟩ |

## B. Cheapest checks first (walk outward from the machine)

| # | Check | Result | If it fails, owner |
|---|---|---|---|
| 1 | Is the **tab enabled** on this instance? (some tabs are disabled by design or abandoned; check the state on the instance) | ⟨yes/no⟩ | IIAE: enable on test, ask before prod |
| 2 | Is the machine integrated and publishing? (Machine List status, connector status) | ⟨⟩ | Plant ME / IIAE |
| 3 | Does the **input topic** carry messages? (wildcard subscribe) | ⟨⟩ | If no: not a flow problem - `mi-connector` |
| 4 | Does the **input UUID** appear on that topic? | ⟨⟩ | Wrong UUID in the config, or data point not configured on the edge platform |
| 5 | Does the **output UUID** differ from the input UUID and exist on the edge platform? | ⟨⟩ | IIAE |
| 6 | Does the dashboard query use that output UUID and the right time range? | ⟨⟩ | Dashboard owner |

## C. The analyser

| Item | Entry |
|---|---|
| Export date of the flow JSON | ⟨⟩ |
| Command run (`python3 scripts/analyze_flow.py <file>`) and exit code (2 blocker, 1 warn, 0 clean) | ⟨⟩ |
| Blockers found (secret / sysTime / oneof) | ⟨⟩ |
| `spine-severed`, `output-uuid-not-set`, `unset-context-read`, `hardcoded-threshold` | ⟨⟩ |
| Secret found? Rotated by (role) and date | ⟨⟩ |
| Do the neighbouring flows on the same instance show the same finding? (copied pattern) | ⟨⟩ |

## D. What the analyser cannot see

| Question | Answer | Evidence |
|---|---|---|
| Timezone of the instance clock vs the plant shift plan | ⟨⟩ | ⟨⟩ |
| Is flow context persistent on this instance? Is shift state held globally? | ⟨⟩ | ⟨⟩ |
| Does the flow use a subflow? Was its body read? | ⟨⟩ | ⟨⟩ |
| Is there a `catch`, and does it name the failing node? | ⟨⟩ | ⟨⟩ |
| Does an `http request` node in the path have its URL set at run time? | ⟨⟩ | ⟨⟩ |

## E. Decision

| Item | Entry |
|---|---|
| Diagnosis (one sentence) and the layer it sits in (machine / connector / edge / broker / flow / offload / asset) | ⟨⟩ |
| Fix applied on test (what) and test result | ⟨⟩ |
| Prod deployment approved by (role) and date | ⟨⟩ |
| Topic or UUID renamed? (must be **no**; raise a data-model change instead) | ⟨⟩ |
| Re-run of the analyser after the fix: blockers | ⟨⟩ |
| Recorded against (machine, not flow, when the cause was upstream) | ⟨⟩ |
