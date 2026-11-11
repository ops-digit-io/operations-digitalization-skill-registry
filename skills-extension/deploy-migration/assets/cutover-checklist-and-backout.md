---
type: Skill Asset
title: Cutover checklist and backout
description: Template for one location - checklist with RAG, outage window, key-user verification, parallel-run end, back-out plan (proposal) and decommissioning record.
resource: ../SKILL.md
status: draft
tags: [migration, template]
---
# Cutover - `<application or platform>` at `<location>`

| | |
|---|---|
| Stage | `<n>` |
| Announced on (two weeks ahead) | `<date>` |
| Outage window | `<from - to>`; process data and dashboards unavailable, announced to `<roles>` |
| Fixed external dates checked (audits, shutdowns) | `<>` |
| Key user / central server team / application owner | `<roles>` |

## 1 Checklist with RAG
| Item | Owner | Status (G / A / R) | Verified by key user | Note |
|---|---|---|---|---|
| Network and certificates (new names) | `<>` | `<>` | `<>` | `<>` |
| Interfaces: source repository, artifact registry | `<>` | `<>` | `<>` | `<>` |
| Directory integration, access carry-over, DNS | `<>` | `<>` | `<>` | `<>` |
| Runtime licence key available | `<>` | `<>` | `<>` | `<>` |
| Preconditions and approvals (firewall, security, cloud) | `<>` | `<>` | `<>` | `<>` |
| Backup or snapshot taken and restore tested | `<>` | `<>` | `<>` | `<>` |
| Edge devices reconfigured | `<>` | `<>` | `<>` | `<>` |
| Reporting reproduced on the new platform | `<>` | `<>` | `<>` | `<>` |
| Service concept refreshed (change, incident, roles, connection matrix) | `<>` | `<>` | `<>` | `<>` |

Rule: any red item at window start means hold.

## 2 Key-user verification (after cutover)
| Function / data / interface | Expected | Observed | OK / not OK | Date |
|---|---|---|---|---|
| `<>` | `<>` | `<>` | `<>` | `<>` |

## 3 Parallel run
Start `<>`; end `<>`; comparison checks `<>`; person who stops the old process `<role>`; paper or shadow tools switched off `<yes/no>`.

## 4 Back-out plan (PROPOSAL, confirm with the owner)
Scope `<>`; decision owner `<role>`; executor `<role>`; trigger criteria `<>`; decision time-box `<>`; points of no return `<>`; preparation done `<backup, old config, licence key, old server kept>`; steps `<1..n>`; verification after back-out `<>`; communication `<>`; rehearsed or read by executors `<yes/no, date>`.

## 5 Decommissioning record
| Step | Done by / date |
|---|---|
| All flows migrated and verified; observation period over | `<>` |
| Old process switched off | `<role>` |
| Old data copied or cleaned up per rule | `<>` |
| Uninstall change request raised; VM or server released | `<>` |
| Licences returned; application list and documentation updated | `<>` |
| Back-out plan closed | `<>` |
