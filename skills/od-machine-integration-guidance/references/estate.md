# The machine estate

1,715 machines and PLCs, from the Machine List as exported into the knowledge graph
(`90-Sources/generated/kg_nodes.csv`, `type=Machine`). Read 2026-08-24.

Each row records plant, vendor, PLC model, part number, network protocol, integration
status, integration method and — where somebody wrote one — an integration blocker.

## Integration status

| Status | Machines |
|---|--:|
| `INTEGRATED` | 821 |
| `NOT INTEGRATED` | 395 |
| `INTEGRATION ONGOING` | 48 |
| not recorded | 451 |

**451 rows carry no status at all.** Any "integration rate" that divides 821 by 1,715 is
answering a different question from one that divides 821 by 1,264. State the denominator.

## Integration method

| Method | Machines |
|---|--:|
| IIoT Edge Computing Platform | 672 |
| Central OPC-UA Aggregation Server | 384 |
| `EVALUATION ONGOING` | 117 |
| not recorded | 542 |

## PLC vendors

| Vendor | Machines |
|---|--:|
| Siemens | 1,032 |
| Rockwell Automation — Allen Bradley | 220 |
| Beckhoff | 42 |
| Bachmann Electronic GmbH | 39 |
| Engel | 38 |
| B&R Industrial Automation | 32 |
| Schneider Electric | 32 |
| Bachmann OPC | 24 |
| Mitsubishi Electric | 17 |
| Delta Electronic | 14 |
| Omron | 12 |
| Keyence | 12 |
| Philips | 9 |
| not recorded | 133 |

Siemens is **60 % of the estate**. Any integration capability decision that optimises for
anything else is optimising for the tail. `Bachmann Electronic GmbH` and `Bachmann OPC`
are the same vendor recorded two ways.

## PLC models (top)

| Model | Machines |
|---|--:|
| SIMATIC S7-300 | 324 |
| SIMATIC S7-1200 | 264 |
| SIMATIC S7-1500 | 171 |
| Compact Logix 5370 | 104 |
| PLC 5069-L306ER | 47 |
| Schneider *(unspecified)* | 44 |
| Automation PC | 32 |
| SINUMERIK 840D SL | 19 |
| SIMATIC S7-200 | 19 |
| MX213 | 18 |
| Compact Logix | 15 |
| SLC5/05 | 12 |
| DVP14SS2 | 12 |
| SIMATIC ET200S / ET200SP / ET200 | 12 / 12 / 9 |
| Keyence | 12 |
| Compact GuardLogix 5380 | 10 |
| not recorded | 447 |

The **S7-300 is the single largest model at 324 machines and it is a legacy platform** —
which is why the S7 route, its PLC-program requirement and the TIA upgrade blocker come up
more often than any other integration question.

## Vendor × method, where both are recorded

| Vendor | Method | Machines |
|---|---|--:|
| Siemens | IIoT Edge | 451 |
| Siemens | Central OPC-UA | 251 |
| Siemens | evaluation ongoing | 51 |
| Rockwell / Allen Bradley | IIoT Edge | 78 |
| Rockwell / Allen Bradley | evaluation ongoing | 52 |
| Rockwell / Allen Bradley | Central OPC-UA | 30 |
| Beckhoff | IIoT Edge | 35 |
| B&R Industrial Automation | Central OPC-UA | 30 |
| Bachmann Electronic GmbH | Central OPC-UA | 16 |
| Delta Electronic | IIoT Edge | 14 |
| Omron | IIoT Edge | 12 |
| Keyence | IIoT Edge | 12 |

Neither route is the default for Siemens — both are used at scale, and the choice is per
machine, made through the decision tree, not per vendor.

## Machines per plant

| Plant | Machines | Integrated |
|---|--:|--:|
| Subotica | 181 | 27 |
| Mako | 128 | 71 |
| Vac | 103 | 20 |
| Changshu | 99 | 21 |
| Timisoara | 91 | 26 |
| Waltershausen | 87 | 69 |
| Northeim | 87 | 83 |
| Monterrey | 82 | 25 |
| Tlalnepantla | 82 | 0 |
| Carei | 81 | 29 |
| Ponta Grossa | 75 | 62 |
| Qingdao | 74 | 59 |
| Auburn | 60 | 57 |
| Dolne Vestenice | 59 | 48 |
| Rennes | 58 | 58 |
| Montemorelos | 51 | 0 |
| Delicias | 51 | 22 |
| Karben | 46 | 23 |
| Changchun | 43 | 21 |
| Sun Prairie | 39 | 39 |
| Caluire | 33 | 24 |
| Somersworth | 26 | 26 |
| Tanger | 20 | 0 |
| Hannover Stöcken | 17 | 2 |
| San Luis Potosi | 16 | 0 |
| Korbach | 16 | 0 |
| Hann. Münden | 9 | 9 |
| Ostrava | 1 | 0 |

**The estate is bimodal, not a gradient.** Rennes, Sun Prairie, Somersworth, Hann. Münden
and Auburn are effectively complete. Tlalnepantla (82), Montemorelos (51), Tanger (20),
San Luis Potosi (16) and Korbach (16) are at zero — 185 machines that have not started, not
185 that are behind. Subotica is the largest single opportunity in the estate: 181 machines,
27 integrated.

Plants with a large gap and a large base — Subotica, Vac, Changshu, Timisoara, Monterrey,
Carei — are wave candidates. Plants at zero are a different conversation: check whether the
target platform is even installed there before planning machines.

## Fields that exist and are empty on every row

`production_criticality` · `cyber_security_status` · `machine_blockers` · `input_protocol`

All four are empty on all 1,715 rows. They are unpopulated fields, **not** a statement that
no machine is critical and none has a security finding. Never read one as a value.
