---
type: Skill Reference
title: Staged migration and cutover
description: Staging logic, preconditions, per-location checklist with RAG, outage window, key-user verification, parallel run, licence check, middleware retirement flow, decommissioning and recurring pitfalls.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [migration, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Staged migration and cutover

## Staging an application migration (illustrative order)

1. Migrate the first machine interface to the industry standard, starting with the lowest-risk machine.
2. Integrate the edge platform to read PLC data.
3. Replicate the existing reporting on the new platform as the requirement baseline.
4. Prepare the MES with the system integrator.
5. Integrate the MES with minimal downtime.
6. Migrate the remaining interfaces.

Per stage: resources, cost, risk, exit criterion, back-out. Key activities and roles: external PLC experts, OD interface-engineer capacity, plant key user, MES partner, edge partner, production software owner. Staged scope is better when step one stands alone as a benefit (for example first without ERP integration, then with it); expect approval in stages too.

## Platform or server migration across locations

1. **Scope per location**: network, certificates, interfaces (source repositories, artifact registry), directory integration, licences. Assessed by the central server team with the application owner.
2. **Time plan** across locations; communicate two weeks ahead; execute per timeline.
3. **Per-location checklist file with RAG**, one shared traffic-light table, remaining tasks per team (network, server).
4. **Outage window** per location for reconfiguring edge devices; announce that process data and dashboards are unavailable meanwhile.
5. **Key-user meeting** per location after cutover, verifying every migration item.
6. **Licence check** before moving a VM: runtime licences (for example of an OPC UA server) are often bound to one machine; keep the key to reset the state.
7. **Service concept** per application: change and incident process, connection matrix, roles and responsibilities, risk and gap assessment, RAG (approved / refining / early).
8. For Windows servers: confirm DNS, certificates for the new names, user-access carry-over.

RAG meaning (`PROPOSAL`): green = item done and verified by the key user; amber = open, owner and date set; red = blocked or no owner. Any red item at the start of the window means hold.

## Preconditions

Artifact registry, source-code host, firewall changes, cloud-system approval, security approval, licence keys, backup. A "new installation" location without a legacy baseline is the hardest case. Where a separation from a former parent is involved, track each carried-over item (service documentation, contracts, processes) with an owner; a separation or migration plan is a precondition field for initiatives needing central data.

## Parallel run

Run old and new side by side for a limited, planned period to compare results (for example for a monitoring tool; match reading dates to billing periods). The period has an end date and a named person who stops the old process. Running the new system and paper in parallel because nobody trusts the new process, with no one assigned to stop the old one, is a recurring failure. `<length of the observation period>`.

## Key-user verification

The location key user receives a location-specific meeting to verify every migration item after cutover: functions, data on dashboards, interfaces, reports, access. Result recorded per item in the checklist. Without that sign-off the location stays amber.

## Legacy middleware retirement (decision sequence)

1. Consult the plant key users.
2. If other software lives on the machine (for example an aggregation server), decide whether it stays.
3. If the flows matter, write a per-flow migration plan with the key users and execute it with shared responsibility.
4. If unknown flows exist, hand over to the other business area.
5. Raise a change request to uninstall the middleware and release the VM.
6. Update the application list.

## Decommissioning

Order: all flows migrated and verified, observation period over, old process switched off by its named owner, data copied or cleaned up per rule, uninstall change request, server or VM released, licences returned, application list and documentation updated, back-out plan closed. Definition of done for a rollout: hardware and software commissioned, master data set, monitoring running, key users trained, backup integrated, documentation complete, old process switched off.

## Pitfalls and lessons

- No reply to follow-ups, unclear owner for registry access: ownership problem.
- Cost of connecting existing devices is easily underestimated.
- Runtime licence bound to one machine; DNS and certificates forgotten.
- Customer audit deadline overlooked; customer-facing line taken down.
- Unstable rollout team, no assigned use-phase function (shop-floor IT, application key user), no 24/7 service: the system is not accepted.
- Only technical key user leaves within weeks: require documented transformation, owned workspace, access control and named successor before accepting a handover.
- Tool strategy changes over time: look up current tool status live, do not rely on an old deck.
