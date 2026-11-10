---
type: Skill Reference
title: Route choice per machine type
description: How to choose the connector and route for each machine type in a wave - data classes, when an edge device is needed, the low-cost address-translation pattern, legacy and camera cases - rules only, to be confirmed per machine in mi-connector.
resource: ../procedure.md
status: draft
owner: human:jakob.gabriel
tags: [information-integration-service, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Route choice per machine type

This is the **plan-level** choice, one route per machine type. The per-machine detail (four gates,
configuration, fallbacks) stays in `mi-connector` (`connectors`, `decision-paths`,
`fallbacks`). Confirm the route per machine there before ordering.

## 1. Architecture in one line

Machine -> optional edge device -> either an OPC-UA server (client/server, rule engine subscribed,
central aggregation server) or an MQTT broker. The service bus is the default hub for transactional and
streaming data with an agreed payload and topic structure; the rule engine transforms; MES, process data
acquisition, energy management, analytics and edge apps sit downstream. Consumers get one interface so
applications are not tailored to device interfaces; third-party models map into the standard model.

## 2. Data classes decide the hub

| Class | Examples | Propagation | Default hub |
|---|---|---|---|
| Transactional | events, cycle time, counters, set values, limits, alarms | changes hard to propagate | Service bus with OPC-UA |
| Time series | curves, process values | easy to propagate | MQTT stream |
| Master data | single source of truth | leading system (ERP) | ERP is master for material, order and product master data; local systems (MES etc.) are derived and report back; other systems via API |

For every machine type decide in the tag list: transactional signals, streaming signals, what connected
systems need, what analytics wants.

## 3. Route per machine type (decision table)

| Machine type | Route | Why |
|---|---|---|
| Native OPC-UA machine | Direct to the aggregation server | No device needed |
| Controller family with a known process, ordinary signals | Aggregation server or OPC-UA client/server | Scale-known-types rule |
| Vision system or robot; full traceability expected; high-resolution time series from process-critical sensors; inline measurement; planned anomaly detection or predictive work | **Edge device** | Data loss would reject parts or analytics needs the rate |
| Many machines, low data frequency, addresses must stay unchanged | **Low-cost pattern**: one edge or switch with address translation, no per-device change | One configuration instead of many; trial one device on one machine before ordering more |
| Legacy shop-floor system with only a non-standard interface (for example SOAP) and no cyber security | Custom managed connector in the edge platform's connector framework | Many plants run the same system, so one connector scales |
| Camera or vision connector | Edge connector per camera system; features extracted on the edge, only features or images forwarded | Cheaper and faster than vendor turnkey adjustments to third-party software |
| Old HMI on an old machine | Treat as a barrier-log candidate; needs an emergency strategy when the system is down | Hard to connect |
| Bus-based metering (energy) | Check meter compatibility with the bus, one converter per pulse output, unique bus addresses, segment limits | Past issues: unreliable WLAN between logger and plant LAN |

Edge is **not** needed when the machine has no high-frequency signals and OPC-UA can carry the time series.

## 4. Rule-engine versus PLC placement

- In the PLC: values that control the process or depend on equipment condition or safety (process values, set values, machine mode, safety doors).
- In the rule engine: logic needing context from several machines or systems, single-source-of-truth concepts (work-centre or location naming), complex logic likely to be iterated (SPC alerts, statistical functions).

## 5. Side notes for the plan

- A sensor value is not automatically an event; decide events in the flow design (`ops-pipeline`).
- Measure-point naming must be thought through up front; master data entry is laborious.
- Standard machine-state signals and template flows are enablers of the waves (`od-signal-standardization`).
- Reusing existing edge devices with network address translation avoids IP conflicts, only for lower data frequency.
- An OPC-UA runtime licence can be bound to one machine: confirm the key before migrating a server.
- Where Cyber Security approval is needed, list the route's components for the package (`od-cybersec-gate`).

## 6. Questions that fix the route

Which data class? Data frequency and loss tolerance? Is a vision system, robot or inline measurement
involved? Is there an OPC-UA server or edge platform at the plant? Is the PLC program available and under
own control? Is the machine type known (scale rule)? Does the compatibility check pass?
