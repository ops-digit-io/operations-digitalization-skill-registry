---
type: Skill Reference
title: Package contents
description: What the Cyber Security sign-off package holds for a machine connection and for an app deployment, and which existing skill or record already produces each item - open when filling the package.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [information-integration-service, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Package contents

The department has not collected what Cyber Security asks for (see [`gate-rules.md`](gate-rules.md), "What the
sources do not give"). The list below is built the other way round: it names what the OD side **already knows and
writes down** about a connection or an app, so the request is complete on OD's side whatever Cyber Security
adds. Items Cyber Security adds are entered as `⟨…⟩` rows in the package.

## A. Machine connection

| Item | What to write | Where it already exists |
|---|---|---|
| Plant, machine, owner | Plant, machine name and EQ id, vendor, PLC model; Plant ME and Plant IT roles | Machine List; `mi-connector` guidance protocol header |
| Route chosen | One of three: edge device in or beside the cabinet; connector with no device; via the Softing dataFEED aggregation server bridged with the OPC UA connector | `mi-connector` `references/decision-paths.md`, guidance protocol Gate 1 |
| Connector | The driver and its status (some connectors cannot be used, for example status Idea or "DO NOT USE"; check the connector list) | `mi-connector` `references/connectors.md` |
| Data path, end to end | machine, connector, edge, platform, offload to Databricks and the Azure Storage Account (Parquet, global layer) | `references/iiot-edge-platform.md`; `15-resources.md` |
| What is read, what is written | Signals in scope; read-only versus any write to the controller | acceptance protocol section 1 (`od-acceptance-test`) |
| Network position | Where the edge device or server sits and how it reaches the platform | Phase 2 of `references/iiot-edge-platform.md`; ⟨network diagram - Plant IT⟩ |
| Credentials and certificates | **Only** that endpoint credentials and certificates exist and which role holds them. Never the values | `iiot-edge-platform.md` bridge task 3 |
| Known security barriers | Firmware patch needed; no security-compliant communication; flat network | `references/barrier-classes.md`, `fallbacks.md` section 4 |
| Cover | Wave-level sign-off in force? reference and scope | ⟨where recorded⟩ |
| Investment status | Approved or not (a precondition of the go-ahead) | `mi-connector` Route A step 6 |
| Acceptance protocol | Drafted before the build | `od-acceptance-test` `assets/acceptance-test-protocol.md` |

## B. App deployment (Lane 3a)

| Item | What to write | Where it already exists |
|---|---|---|
| App, owner, plant sponsor | What it is, who owns it | `deploy-appstore` step 3 |
| Sourcing route | Reuse, self-developed, external, integrated foreign app | `deploy-appstore` route table |
| Target | The platform as the requester names it; whether the container platform is the IIoT Edge runtime stays an open question | `deploy-appstore` "Which platform" |
| Data read and written | Against the systems of record | `deploy-appstore` step 3 |
| Functionality, network, dependencies | What the app does, how it is reached, what it depends on | precedent: the QFPR inputs for Group IT began with an explanation of the application (functionalities) and the network; the list is cut off in the vault note |
| Rollback owner | Named role | `deploy-appstore` step 3 |
| Containerization, image, registry | ⟨requirements⟩ | not recorded (`deploy-appstore` open list) |
| Acceptance protocol | Drafted | `od-acceptance-test` |

## C. Common to both

| Item | What to write |
|---|---|
| Decision request | Row "Equipment integration go-ahead" or the relevant gate; mode Tandem; link to the request |
| Escalation owner | Who follows up and on which date |
| Open Cyber Security questions | `⟨…⟩` rows, each with the role that must answer |
| Answer record | Who, date, scope, conditions, validity - filled only when given |

## Quality checks before it leaves OD

- Every item has a source in the right-hand column or is a visible `⟨…⟩`.
- No secret: no password, token, certificate, address or host name.
- Scope is exact: which machines, which app version. A sign-off for "the wave" lists the machines in it.
- The package says what it does **not** know.
