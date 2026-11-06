---
type: Skill Asset
title: Guidance protocol
description: The defined output of Route B - one machine's gates answered in order, the connector and configuration chosen, and the fallback taken if a path blocked, so the result is a reusable record rather than prose.
resource: ../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [information-integration-service, template, protocol]
generated: { by: claude-code/1, at: 2026-09-17T00:00:00Z }
---

# Machine integration guidance — ⟨plant⟩ · ⟨machine⟩

| | |
|---|---|
| **Plant** | ⟨plant⟩ |
| **Machine** | ⟨name⟩ ⟨(EQ id)⟩ · ⟨vendor⟩ ⟨PLC model⟩ |
| **From assessment** | ⟨assessment-protocol.md reference, if a Route A already covered this machine — otherwise: assessment not yet done, scope confirmed here⟩ |
| **Engineer / date** | ⟨name⟩ · ⟨date⟩ |
| **Overall verdict** | ⟨connected · blocked, pending ⟨item⟩ · configuration in progress⟩ |

## Gate 0 · What's installed at this plant

⟨IIoT Edge Platform available? Central Aggregation Server (Softing dataFEED) available?
Edge device on hand? "Not sure" → Plant Capabilities & System Availability & Rollout list,
then a call with MPEE OD.⟩

**Cheap question asked first:** is the machine already on an OPC-UA server? ⟨yes / no⟩ — if
yes, skip to Gate 4; no PLC program or cabinet work needed.

## Gate 1 · Variant chosen

| Variant | Available at this plant? | Chosen? | Why |
|---|---|---|---|
| ① edge device | | | |
| ② connector, no device | | | |
| ③ via aggregation server | | | |

## Gate 2 · Connector / data source driver

| | |
|---|---|
| **Connector or driver** | ⟨name, e.g. DTQ-S7-Connector⟩ |
| **Available?** | ⟨checked against connectors.md — yes / no, alternate route⟩ |
| **Configuration pattern followed** | ⟨softing-datafeed.md § … / iiot-edge-platform.md § …⟩ |

## Gate 3 · Preparation gates, in order

| # | Gate | Status | Note |
|---|---|---|---|
| 1 | Budget | ⟨clear / blocked⟩ | |
| 2 | Infrastructure (cabling, power, IP) | ⟨clear / blocked⟩ | |
| 3 | **PLC program** — the breakpoint | ⟨have it / requested ⟨date⟩, lead time ⟨⟩ / not needed, on OPC-UA server⟩ | |
| 4 | Tags exported, mandatory vs optional split | ⟨clear / blocked⟩ | |
| 5 | Cyber security sign-off | ⟨clear / pending — no expedited path⟩ | |

**If gate 3 blocked:** fallback rungs worked (`references/fallbacks.md` §1) before declaring
it blocked —

| # | Try | Result |
|---|---|---|
| 1 | Already on an OPC-UA server? | |
| 2 | Vendor-specific connector? | |
| 3 | Writes a file (FTP/SMB)? | |
| 4 | HTTP / SOAP / web service? | |
| 5 | Serial interface? | |
| 6 | Signal available on a neighbouring PLC? | |
| 7 | Sensor addable instead? | |

## Gate 4 · Recorded

- [ ] Machine List — name, PLC IP, protocols, PLC type, PLC program
- [ ] Machine CV — PLC program and tag list, mandatory vs optional
- [ ] Edge Device List (edge routes only)
- [ ] MPEE Operations Digitalization informed
- [ ] Status remains **not** `INTEGRATED` until `od-acceptance-test` passes

## Blocked, if applicable

| Blocker | Class (barrier-classes.md) | Owner | Next step |
|---|---|---|---|

## Hand-off

→ `od-signal-standardization`, then `od-node-red-flows`, then `od-acceptance-test`.

## Sign-off

| Role | Name | Date |
|---|---|---|
| IIAE | | |
| Plant ME / IT (if connecting) | | |
