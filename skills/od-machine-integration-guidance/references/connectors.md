# The 26 machine connectors

From the Connector Overview list, as exported into the knowledge graph
(`90-Sources/generated/kg_nodes.csv`, 26 `Connector` nodes).

A **connector** reaches a machine. A **tool** is a system a plant uses. They are separate
row types and are never merged — see `od-context`.

| Connector | Input protocol | Supplier |
|---|---|---|
| DTQ-S7-Connector | PROFINET IO | DATATRONiQ |
| DTQ-S7-NET-Connector | ⟨not recorded⟩ | DATATRONiQ |
| DTQ-TIA-Connector | ⟨not recorded⟩ | DATATRONiQ |
| DTQ-SINUMERIK-Connector | UDP/IP | DATATRONiQ |
| DTQ-SINUVARS-Connector | TCP/IP | DATATRONiQ |
| DTQ-SIMOTIOND-Connectors | ⟨not recorded⟩ | DATATRONiQ |
| DTQ-Beckhoff-Connector | ADS | DATATRONiQ |
| DTQ-EthercatIO-Connector | ⟨not recorded⟩ | DATATRONiQ |
| DTQ-B&R-Connector | ⟨not recorded⟩ | DATATRONiQ |
| DTQ-Bachmann-Connector | ⟨not recorded⟩ | DATATRONiQ |
| DTQ-ALLENBRADLEY-ROCKWELL-Connector | ⟨not recorded⟩ | DATATRONiQ |
| DTQ-OMRON FINS-Connector | OMRON FINS | DATATRONiQ |
| DTQ-MODBUS-Connector | Modbus TCP | DATATRONiQ |
| DTQ-OPCUA-Connector | OPC-UA | DATATRONiQ |
| DTQ-RS232-Connector | RS232 | DATATRONiQ |
| DTQ-Engel EMI-Connector | Engel-specific | DATATRONiQ |
| DTQ-PIOVAN-Connector | SOAP | DATATRONiQ |
| DTQ-ZWICK-Connector | ⟨not recorded⟩ | DATATRONiQ |
| DTQ-KEYENCECAM-Connector | FTP | DATATRONiQ |
| DTQ-IROPTRIS-Connector | ⟨not recorded⟩ | DATATRONiQ |
| DTQ-Multicon CMC131-Connector | HTTP(S) | DATATRONiQ |
| DTQ-SmartKlaus-Connector | ⟨not recorded⟩ | DATATRONiQ |
| DTQ-FTP2MIL-Connector | FTP | DATATRONiQ |
| DTQ-SMB-Connector | SMB file share | DATATRONiQ |
| SFT-SIMATIC S7-Connector | SIMATIC S7 | Softing Industrial |
| SFT-OPC-Suite | ⟨not recorded⟩ | Softing Industrial |

## Reading the table

**Two suppliers, two roles.** The 24 `DTQ-*` connectors belong to the IIoT edge platform
route. The two `SFT-*` entries are Softing Industrial — the Central OPC-UA Aggregation
Server route (Softing DataFEED OPC Suite; Kepware is the legacy predecessor).

**Five connectors are not PLC drivers at all** — `FTP2MIL`, `SMB`, `KEYENCECAM`,
`Multicon CMC131` and `PIOVAN` reach a file share, a camera or a vendor web service. If
the "machine" is really a file drop or an HTTP endpoint, one of these is the route and no
PLC program is needed. That is the cheapest integration available and it is routinely
overlooked.

**Vendor-specific connectors exist for Engel, Piovan, Keyence, Zwick and Optris.** Where
one exists, use it rather than trying to reach the vendor's PLC generically.

**Input protocol is unrecorded on 11 of the 26 rows.** That is the export's state, not a
statement that the connector is protocol-free. Confirm with the IIAE before quoting one.

## Protocols present in the estate

What the 1,715 machines actually record under `network_protocol` (551 rows are empty):

| Protocol | Machines |
|---|--:|
| PROFINET | 445 |
| TCP / IP | 220 |
| Ethernet / IP | 186 |
| Modbus / TCP | 80 |
| PROFIBUS | 56 |
| EtherCAT | 49 |
| MPI | 43 |
| PROFIBUS / MPI | 38 |
| Profibus *(separate spelling)* | 14 |
| PPI | 8 |
| Profibus / Industrial Ethernet | 7 |

The duplicate spellings (`PROFIBUS` / `Profibus`, `PROFIBUS / MPI`) are a data-quality
artefact of free-text entry, not four different protocols. Normalize before counting.
