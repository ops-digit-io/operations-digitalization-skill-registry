---
type: Skill Reference
title: Finding decks
description: How to find which archive deck holds what for the integration lane - the Slide Index and how to search it, and a topic-to-deck map for machine integration workshops, initiatives, tools and architecture, energy, QFPR, MIL and roadmaps.
resource: ../procedure.md
status: draft
owner: human:jakob.gabriel
tags: [information-integration-service, lane]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---

# Finding decks

Much of what the lane knows lives in slide decks of the department archive (read-only,
outside the vault). The vault holds an index of them so a single slide can be found without
opening hundreds of decks.

## The index and its limits (record)

- **What it is:** `Slide Index/` in the vault: one folder note per archive folder plus a
  master note `Slide Index`; two machine-readable files, `slide-decks.jsonl` (one row per
  deck: path, name, date from the file name, size, slide count) and `slide-manifest.jsonl`
  (one row per slide: number, title, text snippet, speaker notes, shape counts). Generated
  on the date the master note states, "AI-drafted; not reviewed by a human".
- **Size and coverage:** read the master note `Slide Index` for the current number of decks and slides, how many slides carry a title or text, and how many repeat another deck's slide (agenda, title and divider slides repeat a lot). Re-read it; do not quote a remembered figure.
- **Limits:** only `.pptx` is read (older `.ppt`, `.potx`, `.ppsx` and Keynote files stay
  file-level in the Archive Index); text is English only; no thumbnails; snippets are cut at
  a fixed length (so tables and long lists are not complete); the archive's students,
  OneNote, packed archives, commercial and offer files are never read.
- **How to search:** search the vault for a topic, phrase or slide title; the folder note
  shows the deck path and slide number. **Open the deck in the archive before relying on a
  slide and cite it as `Archive: <deck path>, slide N`.** To see how often a slide
  repeats, read the entry's "repeated" marker and prefer the canonical copy.
- **Related, file level:** `Archive Index/` (all archive files, including those the Slide Index
  does not read); `ODEC Facts/` (AI-extracted facts from the ODEC and CoP call decks, staging).

## Topic to deck (archive paths relative to the archive root)

| Topic | Deck (folder / file) | What it holds, from the index |
|---|---|---|
| Equipment integration guide | `D-Operations Digitalization/Initiatives/2024/01-Initiative_OnePager/OD Initiative - Equipment integration Guide.pptx` | Purpose and usage of the guide app (brownfield and greenfield; the IIoT edge platform and the central aggregation server) |
| Machine connectivity next wave | `.../2024/01-Initiative_OnePager/OD Initiative - Machine Connectivity Next Wave Initiative.pptx`; `MPE_white/Operations Digitalization/Projects/Madhine_Connectivity_Next_Wave_Initiative_One_Pager.pptx` | Initiative one-pager |
| Quality measurement equipment integration | `.../2024/01-Initiative_OnePager/OD Initiative - Quality Measurement Equipment Integration.pptx` | Focus topics: integrate measurement equipment within the integration waves; migrate cleanliness laboratory devices |
| State machine standardization | `.../2024/01-Initiative_OnePager/OD Initiative - State Machine Standardization.pptx`; `MPE_white/.../PREQ-StateMachineStandardization.pptx` | Application case analysis, retrofitting methodology and prototyping, target state model |
| Low cost edge devices | `D-Operations Digitalization/Initiatives/2025/OD Initiative - Low Cost Edge Devices.pptx` | Single-board PCs instead of Windows PCs on the shop floor |
| Plant and edge communication standardization | `.../2025/OD Initiative - Plant_Edge Communication Standardization.pptx` | Standardized northbound communication and data models at the edge; bidirectional communication between PLCs and upper systems |
| Legacy application as-is analysis | `.../2025/OD Initiative - CS Legacy Application As_Is_Analysis.pptx` | See [`legacy-applications-landscape.md`](../../../../invest-screen/references/legacy-applications-landscape.md) |
| Virtual facility, wireless and 5G, data platform, integration concept, equipment integration standards | `.../2025/OD Initiative - Virtual Facility Integration.pptx`; `.../2026/OD Initiative - Wireless and 5G Connectivity.pptx`; `.../2026/OD Initiative - Data Platform Integration.pptx`; `.../2026/OD Initiative - Integration Concept Iteration.pptx`; `.../2026/OD Initiative - Update Equipment Integration Standards.pptx` | One-pager templates; the last two are largely unfilled placeholders in the index |
| Plant machine integration workshops | `10-Workshops/2023-Mako_Vac_Use_Case_Workshop_Machine_Integration_Workshop/` (Mako and Vac management summaries); `2024-Vac_Machine_Integration_Workshop/` (summary); `2024-Qingdao_...`, `2024-Changchun_...` (agendas); `2025-Carei_Use_Case_Integration_Workshop/`; `2025-Subotica_Use_Case_Integration_Workshop/`; `2025-Korbach_Use_Case_Equipment_Integration_Workshop/`; `2025-Dolne_Vestenice_Use_Case_Workshop/`; `2026-Northeim_Equipment_Integration/` | Plant-level findings and next steps; the Timisoara and Subotica summaries carry the tool availability tables used in `deployment-reality.md` |
| Integration process overview | `10-Workshops/2025-MPEE_OD_Workshop_Hannover/review/2025-01-12-1.2-OnePager-Integration_Process_Overview.pptx` | One-pager on the integration process |
| Edge platform: operations concept, architecture, back-out | `Smart Factory - Tools and Architecture/02-IIoT_Edge_Computing_Platform/` (`01-Service&Operations_Concept/Operation Concept IIoT and Edge Computing.pptx`; `03-DV_Meldung/IoT Edge DV-Meldung.pptx`; `06-Backout_Plan/Backout_plan_IIoT_Edge.pptx`); `03-AMT_MI_Standard_Agenda_Use_Case_Workshop/00-Presentations_ACTUAL/1.2-Tools_Systems-IIoT_Edge_Platform.pptx` | Roles ([`roles-and-support-model.md`](roles-and-support-model.md)), the "MSB Architektur" slide, back-out plan |
| MSB: back-out and presentations | `Smart Factory - Tools and Architecture/01-Manufacturing_Service_Bus/06-Backout_Plan/Backout_plan_MSB.pptx`; `Neuer Ordner/Testing/MSB - Semana de la Industria 4.0/` (several decks) | Back-out plan and general MSB introductions |
| Energy management (WiriTec) | `Smart Factory - Tools and Architecture/08-Energy_Management_System_Wiritec/` (operation concept, architecture, back-out, system handbook, forum presentations, implementation procedure) | On-premises and cloud architecture, pricing, implementation steps |
| QFPR | `03-AMT_MI_Standard_Agenda_Use_Case_Workshop/00-Presentations_ACTUAL/1.2-Tools_Systems-QFPR.pptx`; `D-Operations Digitalization/Initiatives/2024/01-Initiative_OnePager/OD Initiative - QFPR Deployment.pptx`; `Neuer Ordner/Testing/2024-10-22-Purchasing_Input_QFPR_MTY.pptx` | Tool presentation, rollout one-pager, Monterrey purchasing input |
| MDA/PDA | `03-AMT_MI_Standard_Agenda_Use_Case_Workshop/00-Presentations_ACTUAL/1.2-Tools_Systems-MDA_PDA_Iconnics.pptx` | Tool presentation |
| MIL, image library | `D-Operations Digitalization/Initiatives/2025/OD Initiative - Manufacturing Image Library for OESL.pptx`; `13-AI_Activities/1.4-UseCase-Rollout_Northeim_DeepSpect.pptx`; `10-Workshops/2023-Northeim_CT_DeepSpect_Use_Case_Workshop/Transformation Roadmap.pptx` | Northeim pilot, plan and blockers |
| Connector framework | `2024-04-29-DTQ_Connector_Framework-Example_Winfactory_4.0.pptx`; `12-UseCase_Initiatives/OESL-Cycle_Time_Analyzer-AI_App/20240605_Exchange_with_Datatroniq.pptx`; `PoC - Downtime App/PoC - Downtime App/Supplier-DATATRONiQ/03-Request/...Questions_Round2.pptx` | Supplier exchange and requests |
| Cyber security cases | `03-AMT_MI_Standard_Agenda_Use_Case_Workshop/2022-11-30_CyberSecuritySiemens_ManagementSummary.pptx`; `Smart Factory - Tools and Architecture/99-Requested_Tools/2024-10-ME-Eagle_Eye-Smart_Klaus/06-CyberSecurity/Use_Case_Canvas-Smart_Klaus.pptx` | Two cyber-security summaries |
| eCR documents | `PoC - Downtime App/.../eCR-Process/2025-05-19-eCR_Presentation-Downtime_Application.pptx`; `D-Operations Digitalization/Initiatives/2026/OD Initiative - DevOPs for Automation/SDA_eCR.pptx`; `Smart Factory - Tools and Architecture/99-Requested_Tools/2026-01-Software_for_Chain_Oven_RFID_DataCollection/2025-02-24-eCR_Documents/` | Examples of eCR management summaries |
| Roadmaps by region | `MPE_white/Operations Digitalization/Strategy 2025/` and `Strategy 2026/` (OD roadmaps for Americas, APAC, EMEA East and West); `2024-02-20-OESL_Use_Case_Roadmap_2024.pptx` | Regional roadmaps |
| ODEC and CoP call series | `D-Operations Digitalization/Regular Exchanges/Operations Digitalization Exchange Call/` and `.../Digitalization Community of Practice Call/` (recurring call decks, not all in the Slide Index) | Department KPIs, eCR status, regional equipment-integration status. Extracted in `ODEC Facts` (staging) |

## Procedure

1. Name the topic and the plant. Look in the table; then open the folder note in
   `Slide Index/` and search for the plant or tool name.
2. Read the slide snippet; if the slide is a table or image (shape counts show `tbl` or `img`),
   the information is **not in the snippet**: open the deck.
3. Cite `Archive: <deck path>, slide N` and the date the slide carries. Slides from recurring
   call decks repeat across calls: cite the call and the slide.
4. If you rely on a slide in a decision, write the open item into the plant readiness brief
   ([`plant-readiness-brief.md`](../../../assets/plant-readiness-brief.md)).

## Not found

⟨A deck for the equipment-integration eCR cost calculator or the two OESL guideline documents
"Machine Integration - Softing DataFeed" (Siemens) and "Machine Integration - Beckhoff PLC
Integration" named in `mi-connector`. They are not in the folders read. Who could
supply them: the IIAE.⟩

## Sources

- Vault `Slide Index/Slide Index` and `slide-decks.jsonl`, `slide-manifest.jsonl`, read
  2026-11-05 (this table lists the decks that bear on the lane).
