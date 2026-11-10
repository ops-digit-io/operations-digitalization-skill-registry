#!/usr/bin/env python3
"""Build docs/process-overview.html - the OD process as a BPMN-style flow with every
registry skill attached to the step it serves.

The flow is the four service lanes of the "Operations Digitalization - Department on a
Page" deck (OD_One-Pagers.pptx, verified 2026-08-10): per lane a trigger, seven steps,
error-path gateways, wait states and a definition of done. The step wording is the deck's;
the step -> skill assignment is this registry's judgement and is the part to review.
A skill tagged `partial` covers only a part of the step.

Skill state (deep / documented / stub) and descriptions are read from skills/, so the page
cannot drift from the registry. Every skill in registry.yaml must be placed somewhere on
the flow, or the build fails.

    python scripts/build_process_overview.py            # write the page
    python scripts/build_process_overview.py --check    # fail if the page is stale
"""
from __future__ import annotations

import json
import pathlib
import re
import sys

import yaml

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build_skill_map import LABEL, state  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
import skillpaths as sp
OUT = ROOT / "docs" / "process-overview.html"
REPO = "https://github.com/ops-digit-io/operations-digitalization-skill-registry"

VALUE_CHAIN = ["Captured", "Evaluated", "Assessed", "Planned", "Handed over", "Effective"]

LANES = [
    {
        "id": "uc", "name": "Smart Factory Use Case Support", "skill": "od-use-case-definition",
        "owner": "DBVE · 2 roles", "customer": "Plant ME / plant operations",
        "trigger": "Plant use-case demand or definition-workshop request",
        "done": "Use case defined, prioritized, impact-evaluated and handed to integration with a business case",
        "steps": [
            ("Collect plant demand", "Collect plant demand (workshop / request) — logged vs. roadmap", [("od-use-case-intake-triage", 0)]),
            ("Define use case", "Define use case; process diagnostics and analytical insight", [("od-use-case-definition", 0), ("od-use-case-standardization", 0)]),
            ("Break down requirement", "Break down requirement; assess MF-IT systems", [("funnel-requirements", 0), ("invest-screen", 0)]),
            ("Business case", "Benefit calculation and business case; prioritize by value", [("od-use-case-solution-evaluation", 0), ("bc-build", 0)]),
            ("Hand to integration", "Hand to Information Integration for integration", [("od-data-availability-check", 0), ("od-decision-routing", 1)]),
            ("Qualify and train", "System qualification and training; execution support", [("od-handover-and-adoption", 1)]),
            ("Confirm impact", "Evaluate impact; confirm adoption into the daily process", [("od-scorecard-reporting", 0), ("od-handover-and-adoption", 0)]),
        ],
        "gates": [
            (3, "System deployed, ops concept in place?", "No → mark blocked, escalate to strategy", ["invest-screen"]),
            (4, "Business case nameable?", "No → refuse the request", ["bc-build", "od-use-case-intake-triage"]),
            (6, "Acceptance passed?", "No → rework", ["od-acceptance-test"]),
        ],
        "wait": "Investment approval · Cyber Security sign-off · ContiTech tooling / licensing decision",
        "rights": "Prioritization and selection: recommend (tandem with Plant ME). Refuse requests with no nameable business case. Escalate a blocked use case to the OD lead, ODEC / COP window.",
        "agent_may": "Read MDL / Scorecard; draft definitions, benefit calculations, prioritization; assemble impact reports; prepare workshops.",
        "agent_not": "Commit investment; approve integration; change data models; publish externally.",
        "guard": "Never invent savings — mark to-be-collected.",
        "metrics": "Use cases per year 101 / 153 (behind plan). Per month: target 12, red bar below 12.",
    },
    {
        "id": "ii", "name": "Information Integration Service", "skill": "mi-connector",
        "owner": "IIAE · 3 roles", "customer": "Plant ME / plant IT",
        "trigger": "Equipment integration or data-model harmonization need per roadmap",
        "done": "Machine / equipment integrated, signals standardized, data flowing into the MDL",
        "steps": [
            ("Assess and roadmap", "Equipment assessment and integration roadmap per plant", [("mi-connector", 0), ("od-data-availability-check", 0)]),
            ("Plan investment", "Integration investment planning", [("od-decision-routing", 1), ("bc-build", 1)]),
            ("Integrate machine", "Machine integration and data acquisition — connect to the IIoT Edge", [("mi-connector", 0)]),
            ("Standardize signals", "Signal standardization; data pipelines into the MDL", [("od-signal-standardization", 0), ("ops-pipeline", 0), ("ops-pipeline", 0)]),
            ("Acceptance test", "Interface / software integration consulting and acceptance test", [("od-acceptance-test", 0)]),
            ("Prepare rollout", "Prepare Manufacturing Software Suite rollout; training", [("od-handover-and-adoption", 1)]),
            ("Update readiness", "Update the Equipment Integration report and readiness matrix", [("od-scorecard-reporting", 0)]),
        ],
        "gates": [
            (1, "Ops concept (MSB / MDL) in place?", "No → escalate to strategy", ["od-data-availability-check"]),
            (3, "Machine can connect?", "No (legacy / protocol) → log the barrier, escalate the roadmap", ["mi-connector"]),
            (5, "Acceptance passed?", "No → escalate to the OD lead via COP", ["od-acceptance-test"]),
        ],
        "wait": "Integration investment approval · Cyber Security / OT sign-off · ContiTech signal-standard decision",
        "rights": "Integration go-ahead: execute with approval (tandem Plant ME / IT; Cyber Security sign-off for external). Signal / data-model standardization: recommend, keep ContiTech compatibility.",
        "agent_may": "Read inventory / MDL / Scorecard; draft assessments and roadmaps; update reports and readiness; prepare acceptance protocols.",
        "agent_not": "Connect machines or write to production; approve investment; change standards; approve an external connection.",
        "guard": "No external connection without Cyber Security / OT sign-off.",
        "metrics": "Equipment per year 338 / 331 (above target). Per month: target 25, red bar below 25. Readiness RAG by location.",
    },
    {
        "id": "ps", "name": "Project Support & Application Consultancy", "skill": "it-demand-package",
        "owner": "IIAE", "customer": "Plant / project teams",
        "trigger": "Digital investment project kick-off",
        "done": "Integration project managed to acceptance test; application consulted and accepted",
        "steps": [
            ("Initiate project", "Project initiated per plant roadmap", [("od-decision-routing", 1)]),
            ("Kick-off", "Kick-off with the MPEE OD team; scope and requirements", [("funnel-requirements", 0)]),
            ("Manage project", "Equipment and solution integration project management", [("it-demand-package", 0)]),
            ("Consult on application", "Application consultancy (Manufacturing Software Suite, apps)", [("invest-screen", 1)]),
            ("Acceptance test", "Acceptance testing", [("od-acceptance-test", 0)]),
            ("Embed in daily work", "Ensure use cases are integrated into daily processes", [("od-handover-and-adoption", 0)]),
            ("Report", "Report progress and impact (Equipment / Applications / Use Cases)", [("od-scorecard-reporting", 0)]),
        ],
        "gates": [
            (2, "Investment / resources allocated?", "No → stays Captured, flagged blocked", ["od-decision-routing"]),
            (5, "Acceptance passed?", "No → rework", ["od-acceptance-test"]),
        ],
        "wait": "Resource allocation · ContiTech decision (tool / licensing / DeepSpect) · Cyber Security sign-off",
        "rights": "Acceptance and deployment: human-only, execute with approval. Investment / resource allocation: OD lead / BA Operations. Escalate a blocked project to the OD lead via ODEC.",
        "agent_may": "Read tracker / roadmaps; draft kick-off agendas, requirement specs, status; assemble ODEC progress and impact; flag blocked.",
        "agent_not": "Commit investment or resources; approve acceptance; deploy; make ContiTech licensing commitments.",
        "guard": "Never sign off acceptance; never invent progress or impact figures.",
        "metrics": "Projects to acceptance: passed / active (tracker to collect). Equipment and applications progress vs. plan.",
    },
    {
        "id": "as", "name": "Analytical Support Service", "skill": "od-first-aid-kit",
        "owner": "DBVE", "customer": "Plant / OPEX / operations",
        "trigger": "Analytical request or ad-hoc process-insight need",
        "done": "Process diagnostics / analytical insight delivered",
        "steps": [
            ("Receive request", "Analytical / ad-hoc request received (Process First-Aid Kit)", [("od-use-case-intake-triage", 0)]),
            ("Check data in MDL", "Check data availability in the MDL", [("od-data-availability-check", 0), ("od-sharepoint-list-export", 0)]),
            ("Diagnose", "Process diagnostics and analytical insight — validated", [("od-portfolio-and-savings-analysis", 0), ("od-first-aid-kit", 0)]),
            ("Build asset", "Build asset — dashboard / report / analytics / app", [("od-analytics-asset-build", 0), ("ops-dashboard-engine", 0)]),
            ("Deliver", "Deliver insight and asset; explain to the requester", [("od-analytics-asset-build", 0)]),
            ("Track and promote", "Track utilization; promote recurring value to a standard use case", [("od-scorecard-reporting", 0), ("od-use-case-standardization", 0)]),
        ],
        "gates": [
            (2, "Data in the MDL?", "No → route to Information Integration, mark the data gap", ["od-data-availability-check"]),
            (5, "Recurring value?", "No → close the ad-hoc request", ["od-analytics-asset-build"]),
            (6, "Utilization healthy?", "Low → review or retire", ["od-scorecard-reporting"]),
        ],
        "wait": "Data integration (Information Integration lane) · requester feedback / validation",
        "rights": "Ad-hoc analytics delivery: execute autonomously, read-only on sources. Publishing and industrialization: human-approved. Escalate missing data to Information Integration; low utilization to the OD lead via COP.",
        "agent_may": "Read MDL / Scorecard; run analytical queries; draft dashboards, reports, summaries; track utilization; propose promotion.",
        "agent_not": "Write to production; publish externally; industrialize without a human; present unvalidated insight as fact.",
        "guard": "No figure without a nameable source; flag data gaps.",
        "metrics": "Utilization rate (Scorecard). Asset output. Ad-hoc to standard use-case conversion.",
    },
]

# (from lane, step) -> (to lane, step); step is 1-based, "g<n>" is the gateway after step n.
FLOWS = [
    ("uc", "5", "ii", "1", "hand to integration", False),
    ("as", "g2", "ii", "1", "data gap", False),
    ("as", "6", "uc", "2", "promote to standard use case", False),
    ("ii", "2", "ps", "1", "investment → project", True),
]


def skill_info() -> dict[str, dict]:
    reg = yaml.safe_load((ROOT / "registry.yaml").read_text(encoding="utf-8"))
    info = {}
    for s in reg["skills"]:
        sid = s["id"]
        # This page draws the four service lanes. A skill born in the new-state flow
        # (origin: new-state) or taken from the department's own skill plan after this page was drawn
        # (origin: plan-draft) belongs to docs/new-state-flow.md and is not placed here.
        # Since the merge of 2026-11-10 a skill that absorbed an old lane skill is drawn in its place.
        referenced = {lane["skill"] for lane in LANES} | {k for lane in LANES for _, _, sk in lane["steps"] for k, _ in sk}
        if s.get("origin") in ("new-state", "plan-draft") and sid not in referenced:
            continue
        text = (sp.skill_dir(sid) / "SKILL.md").read_text(encoding="utf-8")
        fm = yaml.safe_load(text.split("---", 2)[1])
        desc = re.sub(r"\s+", " ", fm["description"]).strip()
        first = re.split(r"(?<=[.!?])\s", desc, maxsplit=1)[0]
        d = sp.skill_dir(sid)
        info[sid] = {
            "label": LABEL.get(sid, sid),
            "tier": s.get("tier", ""),
            "state": state(sid),
            "refs": len(list((d / "references").glob("*.md"))) if (d / "references").is_dir() else 0,
            "scripts": len(list((d / "scripts").glob("*.py"))) if (d / "scripts").is_dir() else 0,
            "summary": first,
            "path": f"../{sp.folder_of(sid)}/{sid}/SKILL.md",
            "url": f"{REPO}/blob/main/{sp.folder_of(sid)}/{sid}/SKILL.md",
        }
    return info


def model(info: dict[str, dict]) -> dict:
    placed = {"dept-os"}
    for lane in LANES:
        placed.add(lane["skill"])
        for _, _, sk in lane["steps"]:
            placed.update(s for s, _ in sk)
        for g in lane["gates"]:
            placed.update(g[3])
    missing = sorted(set(info) - placed)
    unknown = sorted(placed - set(info))
    if missing or unknown:
        raise SystemExit(f"skills not on the flow: {missing}; unknown skills on the flow: {unknown}")
    lanes = []
    for lane in LANES:
        l = {k: v for k, v in lane.items() if k not in ("steps", "gates")}
        l["steps"] = [
            {"n": i + 1, "title": t, "text": txt, "skills": [{"id": s, "partial": bool(p)} for s, p in sk]}
            for i, (t, txt, sk) in enumerate(lane["steps"])
        ]
        l["gates"] = [{"after": a, "q": q, "no": no, "skills": sk} for a, q, no, sk in lane["gates"]]
        lanes.append(l)
    return {
        "lanes": lanes, "skills": info, "valueChain": VALUE_CHAIN,
        "flows": [{"from": [a, b], "to": [c, d], "label": lb, "inferred": inf} for a, b, c, d, lb, inf in FLOWS],
        "foundation": "dept-os",
    }


def render() -> str:
    data = json.dumps(model(skill_info()), ensure_ascii=False).replace("</", "<\\/")
    return TEMPLATE.replace("/*DATA*/null", data)


TEMPLATE = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>OD process overview</title>
<!-- Generated by scripts/build_process_overview.py - do not edit by hand. -->
<style>
:root{--bg:#f6f7f9;--surface:#fff;--ink:#1c2230;--muted:#5d6678;--line:#c5ccd8;--lane:#eef1f6;
--accent:#1f6feb;--deep:#1a7f4b;--documented:#b8860b;--stub:#8a919e;--hit:#fff6d6;--shadow:0 1px 3px rgba(20,30,50,.12)}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#12151c;--surface:#1b2030;--ink:#e6e9f0;--muted:#98a1b3;--line:#3a4256;--lane:#171c28;--accent:#5b9bff;--deep:#35b873;--documented:#e0a92b;--stub:#7d8596;--hit:#3a3318;--shadow:0 1px 3px rgba(0,0,0,.5)}}
:root[data-theme=dark]{--bg:#12151c;--surface:#1b2030;--ink:#e6e9f0;--muted:#98a1b3;--line:#3a4256;--lane:#171c28;--accent:#5b9bff;--deep:#35b873;--documented:#e0a92b;--stub:#7d8596;--hit:#3a3318;--shadow:0 1px 3px rgba(0,0,0,.5)}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:14px/1.45 system-ui,-apple-system,Segoe UI,Roboto,sans-serif}
header{padding:16px;max-width:1500px;margin:0 auto}
h1{font-size:20px;margin:0 0 4px}
.sub{color:var(--muted);max-width:75ch;margin:0 0 12px}
.bar{display:flex;flex-wrap:wrap;gap:8px;align-items:center}
.bar button,.bar input{font:inherit;color:var(--ink);background:var(--surface);border:1px solid var(--line);border-radius:6px;padding:4px 10px}
.bar button{cursor:pointer}.bar button.on{border-color:var(--accent);box-shadow:inset 0 0 0 1px var(--accent)}
.bar input{min-width:200px}
.dot{display:inline-block;width:9px;height:9px;border-radius:50%;margin-right:5px;vertical-align:baseline}
.deep>.dot,.dot.deep{background:var(--deep)}.documented>.dot,.dot.documented{background:var(--documented)}.stub>.dot,.dot.stub{background:var(--stub)}
.chain{display:flex;max-width:1468px;margin:0 16px 10px;border-radius:8px;overflow:hidden;box-shadow:var(--shadow)}
@media(min-width:1500px){.chain{margin:0 auto 10px}}
.chain div{flex:1;padding:6px 10px;background:var(--surface);border-right:1px solid var(--line);text-align:center;font-size:12px;color:var(--muted);clip-path:none}
.chain div:last-child{border-right:0}
.found{max-width:1468px;margin:0 16px 10px;padding:6px 12px;background:var(--surface);border:1px solid var(--line);border-left:4px solid var(--accent);border-radius:6px;display:flex;gap:10px;align-items:center;flex-wrap:wrap}
@media(min-width:1500px){.found{margin:0 auto 10px}}
.scroll{overflow-x:auto;padding:0 16px 24px}
#board{position:relative;min-width:1360px;max-width:1468px;margin:0 auto}
svg#flows{position:absolute;inset:0;width:100%;height:100%;pointer-events:none;z-index:3;overflow:visible}
.lane{background:var(--lane);border:1px solid var(--line);border-radius:6px;margin-bottom:14px;display:grid;grid-template-columns:34px 1fr}
.lane>.tag{writing-mode:vertical-rl;transform:rotate(180deg);text-align:center;font-weight:600;font-size:12px;letter-spacing:.03em;background:var(--surface);border-left:1px solid var(--line);padding:8px 0;cursor:pointer;color:var(--muted)}
.lane .body{padding:8px 10px 10px;min-width:0}
.lhead{display:flex;flex-wrap:wrap;gap:6px 14px;align-items:baseline;margin-bottom:8px;cursor:pointer}
.lhead b{font-size:15px}.lhead span{color:var(--muted);font-size:12px}
.grid{display:grid;grid-template-columns:44px repeat(7,minmax(140px,1fr)) 44px;gap:0 18px;align-items:start}
.ev{width:30px;height:30px;border-radius:50%;border:2px solid var(--deep);background:var(--surface);margin:20px auto 0;position:relative;cursor:help}
.ev.end{border-width:5px;border-color:var(--ink)}
.ev.start::after{content:"";position:absolute;right:-18px;top:11px;width:16px;border-top:2px solid var(--muted)}
.task{position:relative;background:var(--surface);border:1.5px solid var(--ink);border-radius:9px;padding:7px 8px 6px;box-shadow:var(--shadow);cursor:pointer;min-height:96px;display:flex;flex-direction:column;gap:5px}
.task:not(:last-child)::after,.task.sq::after{content:"";position:absolute;right:-18px;top:36px;width:18px;border-top:2px solid var(--muted)}
.task .n{position:absolute;top:-9px;left:8px;background:var(--ink);color:var(--surface);border-radius:9px;font-size:11px;padding:0 6px;font-weight:600}
.task .t{font-weight:600;font-size:13px;margin-top:2px}
.chips{display:flex;flex-wrap:wrap;gap:4px}
.chip{font-size:11px;border:1px solid var(--line);border-radius:10px;padding:1px 7px;background:var(--bg);cursor:pointer;white-space:nowrap;color:var(--ink)}
.chip.partial{border-style:dashed}.chip.partial::after{content:" ◐";color:var(--muted)}
.chip:hover{border-color:var(--accent)}
.rowx{display:grid;grid-template-columns:44px repeat(7,minmax(140px,1fr)) 44px;gap:0 18px;margin-top:6px}
.gate{grid-row:1;text-align:center;font-size:11px;color:var(--muted);cursor:pointer;position:relative;padding-top:14px}
.gate::before{content:"";position:absolute;left:50%;top:-8px;height:22px;border-left:2px dotted var(--muted)}
.gate .dia{width:26px;height:26px;transform:rotate(45deg) scale(.82);border:2px solid var(--documented);background:var(--surface);margin:2px auto 8px;display:block}
.gate .dia::after{content:"";}
.gate b{display:block;color:var(--ink);font-size:11.5px;font-weight:600}
.gate .chips{justify-content:center;margin-top:3px}
.wait{margin-top:8px;font-size:12px;color:var(--muted)}
.wait::before{content:"⏳ ";}
.link{font-size:11px;color:var(--accent);border:1px dashed var(--accent);border-radius:10px;padding:0 7px;margin-top:2px;cursor:pointer;align-self:flex-start;background:var(--surface)}
.link:hover,.link.on{background:var(--accent);color:#fff}
.dim{opacity:.25}.hit{background:var(--hit)!important;border-color:var(--accent)!important}
.chip.on{background:var(--accent);color:#fff;border-color:var(--accent)}
.task.sel,.gate.sel{outline:3px solid var(--accent)}
#panel{position:fixed;right:0;top:0;bottom:0;width:min(420px,100vw);background:var(--surface);border-left:1px solid var(--line);box-shadow:-4px 0 14px rgba(0,0,0,.18);padding:16px;overflow:auto;transform:translateX(105%);transition:transform .18s;z-index:10}
#panel.open{transform:none}
#panel h2{font-size:16px;margin:0 28px 6px 0}#panel h3{font-size:12px;text-transform:uppercase;letter-spacing:.05em;color:var(--muted);margin:14px 0 4px}
#panel p{margin:4px 0}#panel .x{position:absolute;right:10px;top:8px;border:0;background:none;color:var(--ink);font-size:22px;cursor:pointer}
.card{border:1px solid var(--line);border-radius:8px;padding:8px 10px;margin:6px 0;cursor:pointer}
.card:hover{border-color:var(--accent)}.card small{color:var(--muted)}
a{color:var(--accent)}
.use{display:inline-block;margin:2px 4px 2px 0;padding:1px 8px;border:1px solid var(--line);border-radius:10px;font-size:12px;cursor:pointer}
.legend{display:flex;flex-wrap:wrap;gap:4px 16px;color:var(--muted);font-size:12px;margin-top:8px}
</style>
</head>
<body>
<header>
  <h1>Operations Digitalization — process and skills</h1>
  <p class="sub">Historical view: the four OD service lanes the new state retires (see the new-state flow), as a BPMN-style flow taken from the department-on-a-page deck. Each step carries the registry skills that serve it. Click a step, a gateway or a skill; click a lane title for its trigger, decision rights and agent limits.</p>
  <div class="bar">
    <button data-st="all" class="on">All skills</button>
    <button data-st="deep"><span class="dot deep"></span>Deep</button>
    <button data-st="documented"><span class="dot documented"></span>Documented</button>
    <button data-st="stub"><span class="dot stub"></span>Stub</button>
    <input id="q" type="search" placeholder="Find a skill…" aria-label="Find a skill">
    <button id="hand">All hand-off arrows</button>
    <button id="reset">Reset</button>
  </div>
  <div class="legend">
    <span>○ start event (trigger) · ◉ end event (definition of done)</span><span>▭ step</span><span>◇ error-path gateway</span><span>⏳ wait states</span>
    <span>dashed chip ◐ = skill covers part of the step</span><span>⇢ dashed badge = hand-off to another lane (hover to draw it, click to jump)</span>
  </div>
</header>
<div class="chain" id="chain" title="OD value chain, from the deck"></div>
<div class="found" id="found"></div>
<div class="scroll"><div id="board"><svg id="flows"></svg></div></div>
<aside id="panel" aria-live="polite"></aside>
<script>
const D=/*DATA*/null;
const S=D.skills,$=(s,e=document)=>e.querySelector(s);
const el=(t,c,h)=>{const e=document.createElement(t);if(c)e.className=c;if(h!=null)e.innerHTML=h;return e};
const esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
let focusSkill=null,stFilter='all',query='',showHand=false,selected=null,hover=null;

$('#chain').innerHTML=D.valueChain.map(v=>`<div>${esc(v)}</div>`).join('');
const f=S[D.foundation];
$('#found').innerHTML=`<b>Applies to every step</b><span class="chip ${f.state}" data-skill="${D.foundation}"><span class="dot ${f.state}"></span>${esc(f.label)}</span><span style="color:var(--muted)">vocabulary, the four service lines, where the truth lives, who decides what, and the honesty rules every skill inherits</span>`;

function chip(id,partial){const s=S[id];return `<span class="chip${partial?' partial':''}" data-skill="${id}" title="${esc(s.summary)}"><span class="dot ${s.state}"></span>${esc(s.label)}</span>`}

const board=$('#board');
D.lanes.forEach((L,li)=>{
  const lane=el('section','lane');lane.dataset.lane=L.id;
  lane.append(el('div','tag',esc(L.id==='uc'?'Use Case Support':L.id==='ii'?'Integration':L.id==='ps'?'Project Support':'Analytics')));
  lane.firstChild.onclick=()=>openLane(L);
  const body=el('div','body');
  body.append(el('div','lhead',`<b>${esc(L.name)}</b><span>Owner ${esc(L.owner)}</span><span>Customer: ${esc(L.customer)}</span>${chip(L.skill)}`));
  body.firstChild.onclick=e=>{if(!e.target.closest('.chip'))openLane(L)};
  const g=el('div','grid');
  const start=el('div','ev start');start.title='Trigger: '+L.trigger;g.append(start);
  const n=L.steps.length;
  L.steps.forEach((s,i)=>{
    const t=el('div','task',`<span class="n">${s.n}</span><div class="t">${esc(s.title)}</div><div class="chips">${s.skills.map(k=>chip(k.id,k.partial)).join('')}</div>`);
    t.dataset.id=L.id+':'+s.n;t.style.gridColumn=i+2;t.onclick=e=>{if(!e.target.closest('.chip'))openStep(L,s)};
    g.append(t);
  });
  const end=el('div','ev end');end.style.gridColumn=n+2;end.title='Definition of done: '+L.done;g.append(end);
  body.append(g);
  const rx=el('div','rowx');
  L.gates.forEach(G=>{
    const c=el('div','gate',`<span class="dia"></span><b>${esc(G.q)}</b>${esc(G.no)}<div class="chips">${G.skills.map(k=>chip(k)).join('')}</div>`);
    c.style.gridColumn=G.after+1;c.dataset.id=L.id+':g'+G.after;c.onclick=e=>{if(!e.target.closest('.chip'))openGate(L,G)};
    rx.append(c);
  });
  body.append(rx);
  body.append(el('div','wait','<b>Wait states:</b> '+esc(L.wait)));
  lane.append(body);board.append(lane);
});

/* ---------- panel ---------- */
const P=$('#panel');
function skillCard(id,partial){const s=S[id];return `<div class="card" data-skill="${id}"><b><span class="dot ${s.state}"></span>${esc(s.label)}</b>${partial?' <small>(covers part of this step)</small>':''}<br><small>${esc(s.state)} · ${s.refs} refs · ${s.scripts} script${s.scripts===1?'':'s'} · ${esc(s.tier)}</small><p>${esc(s.summary)}</p></div>`}
function open(html){P.innerHTML='<button class="x" aria-label="Close">×</button>'+html;P.classList.add('open');$('.x',P).onclick=close}
function close(){P.classList.remove('open');select(null)}
function select(node){document.querySelectorAll('.sel').forEach(e=>e.classList.remove('sel'));selected=node;if(node)node.classList.add('sel')}
function nodeFor(key){return document.querySelector(`[data-id="${key}"]`)}
function openStep(L,s){select(nodeFor(L.id+':'+s.n));
  open(`<h2>${esc(L.name)} · step ${s.n}</h2><p><b>${esc(s.title)}</b></p><p>${esc(s.text)}</p><h3>Skills for this step</h3>${s.skills.map(k=>skillCard(k.id,k.partial)).join('')}<p style="color:var(--muted)">The deck names the step; which skill serves it is this registry's assignment.</p>`)}
function openGate(L,G){select(nodeFor(L.id+':g'+G.after));
  open(`<h2>${esc(L.name)} · after step ${G.after}</h2><p><b>${esc(G.q)}</b></p><p>${esc(G.no)}</p><h3>Skills for this check</h3>${G.skills.map(k=>skillCard(k)).join('')}`)}
function openLane(L){select(null);
  open(`<h2>${esc(L.name)}</h2><p>Owner ${esc(L.owner)} · customer ${esc(L.customer)}</p><h3>Trigger</h3><p>${esc(L.trigger)}</p><h3>Definition of done</h3><p>${esc(L.done)}</p><h3>Decision rights and escalation</h3><p>${esc(L.rights)}</p><h3>Agent may</h3><p>${esc(L.agent_may)}</p><h3>Agent may not</h3><p>${esc(L.agent_not)}</p><p><b>Guardrail:</b> ${esc(L.guard)}</p><h3>Metrics</h3><p>${esc(L.metrics)}</p><h3>Wait states</h3><p>${esc(L.wait)}</p><h3>Lane skill</h3>${skillCard(L.skill)}`)}
function openSkill(id){const s=S[id],uses=[];
  D.lanes.forEach(L=>{L.steps.forEach(st=>st.skills.forEach(k=>{if(k.id===id)uses.push(`<span class="use" data-go="${L.id}:${st.n}">${esc(L.name.split(' ')[0])} ${L.id.toUpperCase()} · ${st.n} ${esc(st.title)}</span>`)}));
    L.gates.forEach(G=>{if(G.skills.includes(id))uses.push(`<span class="use" data-go="${L.id}:g${G.after}">${L.id.toUpperCase()} · check after ${G.after}</span>`)});
    if(L.skill===id)uses.push(`<span class="use" data-go="${L.id}:lane">${esc(L.name)} (lane)</span>`)});
  if(id===D.foundation)uses.push('<span class="use">every step</span>');
  select(null);
  open(`<h2><span class="dot ${s.state}"></span>${esc(s.label)}</h2><p><code>${id}</code></p><p>${esc(s.summary)}</p><p>${s.state} · ${s.refs} references · ${s.scripts} script${s.scripts===1?'':'s'} · tier ${esc(s.tier)}</p><h3>Where it sits in the flow</h3><p>${uses.join('')||'—'}</p><p><a href="${s.path}">Open SKILL.md</a> · <a href="${s.url}" target="_blank" rel="noopener">on GitHub</a></p>`)}

/* ---------- interaction ---------- */
document.addEventListener('click',e=>{
  const go=e.target.closest('[data-go]');
  if(go){const [l,k]=go.dataset.go.split(':');const L=D.lanes.find(x=>x.id===l);
    if(k==='lane')return openLane(L);
    if(k[0]==='g'){const G=L.gates.find(x=>'g'+x.after===k);return openGate(L,G)}
    return openStep(L,L.steps[+k-1])}
  const c=e.target.closest('[data-skill]');
  if(c){focusSkill=focusSkill===c.dataset.skill?null:c.dataset.skill;apply();if(focusSkill)openSkill(c.dataset.skill);else close();e.stopPropagation()}
},true);
document.querySelectorAll('[data-st]').forEach(b=>b.onclick=()=>{stFilter=b.dataset.st;document.querySelectorAll('[data-st]').forEach(x=>x.classList.toggle('on',x===b));apply()});
$('#q').oninput=e=>{query=e.target.value.trim().toLowerCase();apply()};
$('#hand').onclick=e=>{showHand=!showHand;e.target.classList.toggle('on',showHand);drawFlows()};
$('#reset').onclick=()=>{focusSkill=null;stFilter='all';query='';$('#q').value='';document.querySelectorAll('[data-st]').forEach(x=>x.classList.toggle('on',x.dataset.st==='all'));apply();close()};
document.addEventListener('keydown',e=>{if(e.key==='Escape')$('#reset').click()});

function matches(id){const s=S[id];
  if(focusSkill)return id===focusSkill;
  if(stFilter!=='all'&&s.state!==stFilter)return false;
  if(query&&!(s.label+' '+id).toLowerCase().includes(query))return false;return true}
function apply(){
  const active=focusSkill||stFilter!=='all'||query;
  document.querySelectorAll('.chip').forEach(c=>{const ok=matches(c.dataset.skill);c.classList.toggle('on',!!focusSkill&&ok);c.classList.toggle('dim',!!active&&!ok)});
  document.querySelectorAll('.task,.gate,.lhead').forEach(n=>{
    const ids=[...n.querySelectorAll('.chip')].map(c=>c.dataset.skill);
    const hit=active&&ids.some(matches);n.classList.toggle('hit',!!hit&&n.classList.contains('task'));
    n.classList.toggle('dim',!!active&&!hit)});
}

/* ---------- hand-off arrows ---------- */
function drawFlows(){
  const svg=$('#flows'),b=board.getBoundingClientRect();svg.innerHTML='';
  svg.setAttribute('viewBox',`0 0 ${b.width} ${b.height}`);
  if(!showHand&&hover===null)return;
  svg.innerHTML=`<defs><marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="var(--accent)"/></marker></defs>`;
  D.flows.forEach((f,fi)=>{
    if(!showHand&&fi!==hover)return;
    const a=nodeFor(f.from.join(':')),t=nodeFor(f.to.join(':'));if(!a||!t)return;
    const ra=a.getBoundingClientRect(),rt=t.getBoundingClientRect();
    const down=rt.top>ra.top;
    const x1=ra.left+ra.width/2-b.left,y1=(down?ra.bottom:ra.top)-b.top;
    const x2=rt.left+rt.width/2-b.left,y2=(down?rt.top:rt.bottom)-b.top;
    const my=(y1+y2)/2,gap=Math.min(Math.abs(y2-y1)/2,120);
    const d=`M${x1},${y1} C${x1},${y1+(down?gap:-gap)} ${x2},${y2+(down?-gap:gap)} ${x2},${y2}`;
    const p=document.createElementNS('http://www.w3.org/2000/svg','path');
    p.setAttribute('d',d);p.setAttribute('fill','none');p.setAttribute('stroke','var(--accent)');
    p.setAttribute('stroke-width','2');p.setAttribute('stroke-dasharray',f.inferred?'2 5':'7 4');p.setAttribute('marker-end','url(#ah)');p.setAttribute('opacity','.75');
    svg.append(p);
    const tx=document.createElementNS('http://www.w3.org/2000/svg','text');
    tx.setAttribute('x',(x1+x2)/2+6);tx.setAttribute('y',my);tx.setAttribute('font-size','11');tx.setAttribute('fill','var(--accent)');
    tx.setAttribute('paint-order','stroke');tx.setAttribute('stroke','var(--lane)');tx.setAttribute('stroke-width','4');
    tx.textContent=f.label+(f.inferred?' (inferred)':'');svg.append(tx);
  });
}
addEventListener('resize',drawFlows);
const laneOf=id=>D.lanes.find(l=>l.id===id);
D.flows.forEach((f,i)=>{
  const mk=(key,other,dir)=>{const n=nodeFor(key.join(':'));if(!n)return;
    const o=laneOf(other[0]),what=other[1][0]==='g'?'check after '+other[1].slice(1):'step '+other[1];
    const b=el('div','link',(dir==='out'?'⇢ ':'⇠ ')+(dir==='out'?'to ':'from ')+esc(o.name.replace(/ (Service|& .*)$/,''))+' · '+what+' <small>— '+esc(f.label)+(f.inferred?' (inferred)':'')+'</small>');
    b.dataset.flow=i;n.append(b);
    b.onmouseenter=()=>{hover=i;b.classList.add('on');drawFlows()};
    b.onmouseleave=()=>{hover=null;b.classList.remove('on');drawFlows()};
    b.onclick=e=>{e.stopPropagation();const t=nodeFor(other.join(':'));t.scrollIntoView({behavior:'smooth',block:'center'});t.click()}};
  mk(f.from,f.to,'out');mk(f.to,f.from,'in');
});
apply();drawFlows();setTimeout(drawFlows,150);
</script>
</body>
</html>
"""


def main(argv: list[str]) -> int:
    want = render()
    have = OUT.read_text(encoding="utf-8") if OUT.exists() else None
    if "--check" in argv:
        if have != want:
            print(f"stale: {OUT.relative_to(ROOT)}", file=sys.stderr)
            return 1
        print("process overview up to date")
        return 0
    OUT.write_text(want, encoding="utf-8", newline="\n")
    print(f"wrote {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
