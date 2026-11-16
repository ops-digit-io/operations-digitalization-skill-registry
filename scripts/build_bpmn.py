#!/usr/bin/env python3
"""Build the process map as a BPMN 2.0 flow chart from docs/new-state/process.yaml.

    docs/new-state/OD_NewState_BPMN_Flow.bpmn   the BPMN 2.0 XML (pool, lanes, tasks, gateways, events, diagram interchange);
                                                 opens in any BPMN tool (bpmn.io, Camunda Modeler, yEd, yFiles-based editors)
    docs/new-state/OD_NewState_BPMN_Map.html    the same diagram as a web page: bpmn-js (bpmn.io) renders the XML, the
                                                 skills sit under their tasks as links, OpenSpec's skills are external links

    python scripts/build_bpmn.py            # write both files
    python scripts/build_bpmn.py --check    # fail if they are stale

The layout is computed here (columns left to right, one row per branch), so the picture is regenerated from the data and
cannot drift from it. The sub-steps of step 3a4 (the IT demand follows OpenSpec) are an expanded sub-process whose tasks
link to OpenSpec's own skills in its repository; no OpenSpec file is copied into this registry.
"""
from __future__ import annotations

import json
import pathlib
import sys
from xml.sax.saxutils import escape, quoteattr

import yaml

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import skillpaths as sp  # noqa: E402
from build_process_overview import REPO  # noqa: E402
from build_skill_map import state  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
PROC = ROOT / "docs" / "new-state" / "process.yaml"
OUT_XML = ROOT / "docs" / "new-state" / "OD_NewState_BPMN_Flow.bpmn"
OUT_HTML = ROOT / "docs" / "new-state" / "OD_NewState_BPMN_Map.html"
BPMNJS = "17.11.1"   # bpmn-js release the page loads from jsdelivr (pinned)

TW, TH = 120, 80          # task
GW = 50                   # gateway
EV = 36                   # event
X0, CW = 100, 170         # first column, column pitch
ROW = 215                 # lane row height
LABEL_W = 30              # lane label column
POOL_PAD = 120


class Node:
    def __init__(self, id, kind, name, x, y, w, h, lane=None, parent=None):
        self.id, self.kind, self.name, self.x, self.y, self.w, self.h, self.lane, self.parent = id, kind, name, x, y, w, h, lane, parent
        self.children: list[Node] = []

    @property
    def cx(self): return self.x + self.w / 2
    @property
    def cy(self): return self.y + self.h / 2
    @property
    def right(self): return self.x + self.w
    @property
    def bottom(self): return self.y + self.h


class Flow:
    def __init__(self, id, src, tgt, name="", mode="h", parent=None):
        self.id, self.src, self.tgt, self.name, self.mode, self.parent = id, src, tgt, name, mode, parent


def safe(s: str) -> str:
    return "".join(c if c.isalnum() else "_" for c in s)


def build_model():
    proc = yaml.safe_load(PROC.read_text(encoding="utf-8"))
    reg = yaml.safe_load((ROOT / "registry.yaml").read_text(encoding="utf-8"))
    info = {e["id"]: {"state": state(e["id"]), "summary": " ".join(str(e.get("summary", "")).split())} for e in reg["skills"]}
    nodes: dict[str, Node] = {}
    flows: list[Flow] = []
    lane_nodes: dict[str, list[Node]] = {}
    attach: dict[str, dict] = {}          # node id -> {"skills": [...], "external": [...]}
    steps_by_id = {}
    for st in proc["intake"]["steps"]:
        steps_by_id[st["id"]] = st
    for lane in proc["lanes"]:
        for br in lane["branches"]:
            for st in br["steps"]:
                steps_by_id[st["id"]] = st

    # ---- lane geometry (top, height); lane 4 sits above lane 3 so the hand-offs from lanes 1 and 2 do not cross lane 3
    spec = [("intake", "Intake · triage + fit-check", 1 * ROW),
            ("lane1", "Lane 1 · Run a known use case (self-service)", 2 * ROW),
            ("lane2", "Lane 2 · Develop a new use case (OD-led)", 1 * ROW),
            ("lane4", "Lane 4 · Promote a proven use case (IC publishes)", 1 * ROW),
            ("lane3", "Lane 3 · New system or connector (OD / Ext / IT-CS)", 1130)]
    lanes, y = {}, 0
    for lid, title, h in spec:
        lanes[lid] = {"id": lid, "title": title, "top": y, "h": h}
        y += h
    H = y

    def col(c): return X0 + c * CW

    def add(id, kind, name, lane, x, cy, w=None, h=None, parent=None):
        w = w or {"task": TW, "gw": GW, "ev": EV, "sub": TW}[kind.split(":")[0]]
        h = h or {"task": TH, "gw": GW, "ev": EV, "sub": TH}[kind.split(":")[0]]
        n = Node(id, kind, name, x, cy - h / 2, w, h, lane, parent)
        nodes[id] = n
        (parent.children if parent else lane_nodes.setdefault(lane, [])).append(n)
        return n

    def task(id, c, lane, cy, step=None, name=None, w=None, parent=None, x=None, extra_skills=None):
        st = step or steps_by_id[id]
        n = add("T_" + safe(id), "task", name or f"{id} {st['title']}", lane, x if x is not None else col(c) + (CW - TW) / 2 - (CW - TW) / 2, cy, w=w, parent=parent)
        skills = list(st.get("skills") or []) + list(extra_skills or [])
        if skills:
            attach[n.id] = {"skills": skills, "external": []}
        return n

    def gw(id, c, lane, cy, name, x=None):
        # centred on the column's task centre
        return add("G_" + safe(id), "gw", name, lane, (x if x is not None else col(c) + TW / 2 - GW / 2), cy)

    def ev(id, kind, c, lane, cy, name="", x=None):
        return add("E_" + safe(id), "ev:" + kind, name, lane, (x if x is not None else col(c) + TW / 2 - EV / 2), cy)

    def flow(a, b, name="", mode="h"):
        flows.append(Flow(f"F_{len(flows) + 1}", a, b, name, mode, a.parent or b.parent))

    def chain(*ns):
        for a, b in zip(ns, ns[1:]):
            flow(a, b)

    def row_cy(lid, r): return lanes[lid]["top"] + r * ROW + 75

    def waited(prev, step_id, c, lane, cy, label=None):
        """An intermediate timer event after a step that has an external wait."""
        w = steps_by_id[step_id].get("wait")
        if not w:
            return prev
        t = ev("wait_" + step_id, "timer", c, lane, cy, f"wait {w}")
        flow(prev, t)
        return t

    # ---- intake
    cyI = row_cy("intake", 0)
    start = ev("start", "start", 0, "intake", cyI, "Demand or request")
    triage = task("i1", 1, "intake", cyI, name="i1 Known use case? Triage + fit-check")
    route = gw("route", 2, "intake", cyI, "Where does it go?")
    chain(start, triage, route)

    # ---- lane 1
    cy1a, cy1b = row_cy("lane1", 0), row_cy("lane1", 1)
    cyg1 = (cy1a + cy1b) / 2
    g1 = gw("connected", 3, "lane1", cyg1, "Machine already connected?")
    a1, a2, a3 = task("1a1", 4, "lane1", cy1a), task("1a2", 5, "lane1", cy1a), task("1a3", 6, "lane1", cy1a)
    b1 = task("1b1", 4, "lane1", cy1b)
    tb1 = waited(b1, "1b1", 5, "lane1", cy1b)
    b2 = task("1b2", 6, "lane1", cy1b)
    tb2 = waited(b2, "1b2", 7, "lane1", cy1b)
    b3 = task("1b3", 8, "lane1", cy1b)
    b4 = task("1b4", 9, "lane1", cy1b)
    flow(g1, a1, "yes (no spend)"); chain(a1, a2, a3)
    flow(g1, b1, "no: onboard std system"); flow(tb1, b2) if tb1 is not b1 else flow(b1, b2)
    if tb2 is not b2:
        flow(tb2, b3)
    else:
        flow(b2, b3)
    flow(b3, b4)
    m1 = gw("merge1", 10, "lane1", cyg1, "")
    p1 = gw("promote1", 12, "lane1", cyg1, "Proven and adopted: promote?")
    done1 = ev("done1", "end", 13, "lane1", cyg1, "Live")
    flow(a3, m1); flow(b4, m1); flow(m1, p1); flow(p1, done1, "no")

    # ---- lane 2
    cy2 = row_cy("lane2", 0)
    seq2, c = [], 3
    t_prev = None
    for sid in ("21", "22", "23", "24", "25", "26"):
        t = task(sid, c, "lane2", cy2)
        if t_prev is not None:
            flow(t_prev, t)
        tw = waited(t, sid, c + 1, "lane2", cy2)
        t_prev = tw
        c += 2 if tw is not t else 1
        seq2.append(t)
    # t_prev is the last element of the chain (step 26); c is the next free column
    g2 = gw("proven2", c, "lane2", cy2, "Proven and repeatable?")
    flow(t_prev, g2)
    done2 = ev("done2", "end", c + 1, "lane2", cy2, "Graduated")
    flow(g2, done2, "no")

    # ---- lane 4 (entered only from a live, adopted use case)
    cy4 = row_cy("lane4", 0)
    t41 = task("41", 13, "lane4", cy4)
    t42 = task("42", 14, "lane4", cy4)
    t43 = task("43", 15, "lane4", cy4)
    tw43 = waited(t43, "43", 16, "lane4", cy4)
    t44 = task("44", 17, "lane4", cy4)
    end4 = ev("end4", "end", 18, "lane4", cy4, "Story published, feedback routed")
    flow(t41, t42); flow(t42, t43); flow(tw43, t44); flow(t44, end4)
    flow(p1, t41, "yes", "down"); flow(g2, t41, "yes", "down")

    # ---- lane 3
    L3 = lanes["lane3"]["top"]
    cy3f = L3 + 75
    cyA, cyB = L3 + 290, L3 + 505
    cyG3 = (cyA + cyB) / 2
    t31, t32 = task("31", 3, "lane3", cy3f), task("32", 4, "lane3", cy3f)
    tw32 = waited(t32, "32", 5, "lane3", cy3f)
    t33 = task("33", 6, "lane3", cy3f)
    gr = gw("route3", 7, "lane3", cy3f, "Make / buy / integrate, or new connector?")
    flow(t31, t32); flow(tw32, t33); flow(t33, gr)
    # 3a
    g3a = gw("build", 8, "lane3", cyG3, "Build path")
    opts = {o["id"]: o for o in steps_by_id["3a4"]["options"]}
    o1 = add("T_3a1", "task", "3a.1 " + opts["3a.1"]["title"], "lane3", col(9), cyA)
    attach[o1.id] = {"skills": opts["3a.1"]["skills"], "external": []}
    o2 = add("T_3a2", "task", "3a.2 " + opts["3a.2"]["title"], "lane3", col(9), cyB)
    attach[o2.id] = {"skills": opts["3a.2"]["skills"], "external": []}
    flow(gr, g3a, "3a new system", "h"); flow(g3a, o1, "3a.1 reuse"); flow(g3a, o2, "3a.2 self dev")
    # 3a4 = the OpenSpec sub-process (3a.3 external build, 3a.4 foreign app)
    subs = steps_by_id["3a4"]["substeps"]
    ext = steps_by_id["3a4"]["external_process"]
    sp_x, sp_y = col(9), L3 + 650
    sp_w, sp_h = 60 + 36 + 6 * 160 + 36 + 40, 260
    sub = Node("S_3a4", "sub", "3a4 Package / build: " + ext["title"], sp_x, sp_y, sp_w, sp_h, "lane3")
    nodes[sub.id] = sub
    lane_nodes.setdefault("lane3", []).append(sub)
    attach[sub.id] = {"skills": [], "external": [], "header": {"url": ext["url"], "how_to": ext["how_to"], "title": ext["title"]}}
    s_cy = sp_y + 100
    s_start = Node("E_3a4_start", "ev:start", "", sp_x + 30, s_cy - EV / 2, EV, EV, "lane3", sub); sub.children.append(s_start); nodes[s_start.id] = s_start
    prev = s_start
    for i, ss in enumerate(subs):
        tn = Node("T_" + safe(ss["id"]), "task", f"{ss['id']} {ss['title']} ({ss['owner']})", sp_x + 30 + EV + 40 + i * 160, s_cy - TH / 2, TW, TH, "lane3", sub)
        sub.children.append(tn); nodes[tn.id] = tn
        attach[tn.id] = {"skills": [], "external": ss.get("external") or []}
        flows.append(Flow(f"F_{len(flows) + 1}", prev, tn, "", "h", sub)); prev = tn
    s_end = Node("E_3a4_end", "ev:end", "", sp_x + sp_w - 30 - EV, s_cy - EV / 2, EV, EV, "lane3", sub); sub.children.append(s_end); nodes[s_end.id] = s_end
    flows.append(Flow(f"F_{len(flows) + 1}", prev, s_end, "", "h", sub))
    flow(g3a, sub, "3a.3 / 3a.4 IT demand", "h")
    # after the build path
    mx3 = sub.right + 60
    g3m = add("G_merge3", "gw", "", "lane3", mx3, (cyA + cyB) / 2)
    flow(o1, g3m); flow(o2, g3m); flow(sub, g3m)
    t3a5 = add("T_3a5", "task", "3a5 " + steps_by_id["3a5"]["title"], "lane3", g3m.right + 60, (cyA + cyB) / 2)
    attach[t3a5.id] = {"skills": steps_by_id["3a5"]["skills"], "external": []}
    t3a6 = add("T_3a6", "task", "3a6 " + steps_by_id["3a6"]["title"], "lane3", t3a5.right + 50, (cyA + cyB) / 2)
    attach[t3a6.id] = {"skills": steps_by_id["3a6"]["skills"], "external": []}
    end3a = add("E_end3a", "ev:end", "Live", "lane3", t3a6.right + 50, (cyA + cyB) / 2)
    flow(g3m, t3a5); flow(t3a5, t3a6); flow(t3a6, end3a)
    # 3b
    cy3b = L3 + 1000
    t3b4 = task("3b4", 8, "lane3", cy3b); tw3b4 = waited(t3b4, "3b4", 9, "lane3", cy3b)
    t3b5 = task("3b5", 10, "lane3", cy3b); tw3b5 = waited(t3b5, "3b5", 11, "lane3", cy3b)
    t3b6 = task("3b6", 12, "lane3", cy3b)
    end3b = ev("end3b", "end", 13, "lane3", cy3b, "Live on MDL")
    flow(gr, t3b4, "3b new connector"); flow(tw3b4, t3b5); flow(tw3b5, t3b6); flow(t3b6, end3b)
    # intake routes
    flow(route, g1, "known use case", "h")
    flow(route, nodes["T_21"], "new use case", "h")
    flow(route, t31, "new system / connector", "h")

    width = max(n.right for n in nodes.values()) + POOL_PAD
    return {"proc": proc, "info": info, "nodes": nodes, "flows": flows, "lanes": lanes, "lane_nodes": lane_nodes,
            "attach": attach, "W": width, "H": H}


def waypoints(f: Flow):
    a, b = f.src, f.tgt
    if f.mode == "down":      # leave the gateway at the bottom, go down, enter the target from the left
        return [(a.cx, a.bottom), (a.cx, b.cy), (b.x, b.cy)]
    if abs(a.cy - b.cy) < 1:
        return [(a.right, a.cy), (b.x, b.cy)]
    mx = a.right + max(15, min(45, (b.x - a.right) / 2))
    return [(a.right, a.cy), (mx, a.cy), (mx, b.cy), (b.x, b.cy)]


def xml(m) -> str:
    nodes, flows, lanes, W, H = m["nodes"], m["flows"], m["lanes"], m["W"], m["H"]
    tag = {"task": "task", "gw": "exclusiveGateway", "sub": "subProcess"}
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<!-- Generated by scripts/build_bpmn.py from docs/new-state/process.yaml - do not edit by hand. -->',
           '<bpmn:definitions xmlns:bpmn="http://www.omg.org/spec/BPMN/20100524/MODEL" xmlns:bpmndi="http://www.omg.org/spec/BPMN/20100524/DI" '
           'xmlns:dc="http://www.omg.org/spec/DD/20100524/DC" xmlns:di="http://www.omg.org/spec/DD/20100524/DI" id="Definitions_OD" '
           'targetNamespace="https://github.com/ops-digit-io/operations-digitalization-skill-registry/bpmn">',
           '  <bpmn:collaboration id="Collaboration_OD">',
           '    <bpmn:participant id="Participant_OD" name="Operations Digitalization" processRef="Process_OD" />',
           '  </bpmn:collaboration>',
           '  <bpmn:process id="Process_OD" isExecutable="false">',
           '    <bpmn:laneSet id="LaneSet_OD">']
    for lid, lane in lanes.items():
        out.append(f'      <bpmn:lane id="Lane_{lid}" name={quoteattr(lane["title"])}>')
        for n in m["lane_nodes"].get(lid, []):
            out.append(f'        <bpmn:flowNodeRef>{n.id}</bpmn:flowNodeRef>')
        out.append("      </bpmn:lane>")
    out.append("    </bpmn:laneSet>")

    inc: dict[str, list[str]] = {}
    outg: dict[str, list[str]] = {}
    for f in flows:
        outg.setdefault(f.src.id, []).append(f.id)
        inc.setdefault(f.tgt.id, []).append(f.id)

    def emit(n: Node, ind: str):
        k = n.kind.split(":")[0]
        if k == "ev":
            sub = n.kind.split(":")[1]
            t = {"start": "startEvent", "end": "endEvent", "timer": "intermediateCatchEvent"}[sub]
            body = "<bpmn:timerEventDefinition />" if sub == "timer" else ""
        else:
            t, body = tag[k], ""
        head = f'{ind}<bpmn:{t} id="{n.id}" name={quoteattr(n.name)}>' if n.name else f'{ind}<bpmn:{t} id="{n.id}">'
        out.append(head)
        for i in inc.get(n.id, []):
            out.append(f"{ind}  <bpmn:incoming>{i}</bpmn:incoming>")
        for o in outg.get(n.id, []):
            out.append(f"{ind}  <bpmn:outgoing>{o}</bpmn:outgoing>")
        if body:
            out.append(f"{ind}  {body}")
        if k == "sub":
            for c in n.children:
                emit(c, ind + "  ")
            for f in flows:
                if f.parent is n:
                    out.append(f'{ind}  <bpmn:sequenceFlow id="{f.id}" sourceRef="{f.src.id}" targetRef="{f.tgt.id}" />')
        out.append(f"{ind}</bpmn:{t}>")

    for lid in lanes:
        for n in m["lane_nodes"].get(lid, []):
            emit(n, "    ")
    for f in flows:
        if f.parent is None:
            nm = f" name={quoteattr(f.name)}" if f.name else ""
            out.append(f'    <bpmn:sequenceFlow id="{f.id}" sourceRef="{f.src.id}" targetRef="{f.tgt.id}"{nm} />')
    out.append('    <bpmn:textAnnotation id="Note_foundation"><bpmn:text>Foundation: every skill reads dept-context first (vocabulary, decision rights, honesty rules).</bpmn:text></bpmn:textAnnotation>')
    out.append('    <bpmn:association id="Assoc_foundation" sourceRef="E_start" targetRef="Note_foundation" />')
    out.append('    <bpmn:textAnnotation id="Note_chain2"><bpmn:text>Chains out of Lane 2: needs new software to Lane 3a, needs a new connection to Lane 3b, proven and repeatable to the catalog, then Lane 1.</bpmn:text></bpmn:textAnnotation>')
    out.append('    <bpmn:association id="Assoc_chain2" sourceRef="G_proven2" targetRef="Note_chain2" />')
    out.append("  </bpmn:process>")

    # diagram interchange
    out.append('  <bpmndi:BPMNDiagram id="Diagram_OD">')
    out.append('    <bpmndi:BPMNPlane id="Plane_OD" bpmnElement="Collaboration_OD">')
    out.append(f'      <bpmndi:BPMNShape id="Participant_OD_di" bpmnElement="Participant_OD" isHorizontal="true"><dc:Bounds x="0" y="0" width="{W:.0f}" height="{H:.0f}" /></bpmndi:BPMNShape>')
    for lid, lane in lanes.items():
        out.append(f'      <bpmndi:BPMNShape id="Lane_{lid}_di" bpmnElement="Lane_{lid}" isHorizontal="true"><dc:Bounds x="{LABEL_W}" y="{lane["top"]:.0f}" width="{W - LABEL_W:.0f}" height="{lane["h"]:.0f}" /></bpmndi:BPMNShape>')

    def shape(n: Node):
        extra = ' isExpanded="true"' if n.kind == "sub" else ""
        lbl = ""
        if n.kind in ("gw",) or n.kind.startswith("ev"):
            lbl = f'<bpmndi:BPMNLabel><dc:Bounds x="{n.x - 40:.0f}" y="{n.bottom + 4:.0f}" width="{n.w + 80:.0f}" height="28" /></bpmndi:BPMNLabel>' if n.name else ""
        out.append(f'      <bpmndi:BPMNShape id="{n.id}_di" bpmnElement="{n.id}"{extra}><dc:Bounds x="{n.x:.0f}" y="{n.y:.0f}" width="{n.w:.0f}" height="{n.h:.0f}" />{lbl}</bpmndi:BPMNShape>')
        for c in n.children:
            shape(c)

    for lid in lanes:
        for n in m["lane_nodes"].get(lid, []):
            shape(n)
    for f in flows:
        pts = "".join(f'<di:waypoint x="{x:.0f}" y="{y:.0f}" />' for x, y in waypoints(f))
        lab = ""
        if f.name:
            w_ = waypoints(f)
            if len(w_) == 4:       # elbow: the label sits left of the vertical segment, level with the target's row
                lx, ly = w_[1][0] - 118, w_[2][1] - 34
            else:                  # straight or L-shaped: above the last segment
                (x1, y1), (x2, y2) = w_[-2], w_[-1]
                lx, ly = (x1 + x2) / 2 - 56, min(y1, y2) - 30
            lab = f'<bpmndi:BPMNLabel><dc:Bounds x="{lx:.0f}" y="{ly:.0f}" width="112" height="28" /></bpmndi:BPMNLabel>'
        out.append(f'      <bpmndi:BPMNEdge id="{f.id}_di" bpmnElement="{f.id}">{pts}{lab}</bpmndi:BPMNEdge>')
    s = nodes["E_start"]
    out.append(f'      <bpmndi:BPMNShape id="Note_foundation_di" bpmnElement="Note_foundation"><dc:Bounds x="{s.x - 30:.0f}" y="{s.bottom + 50:.0f}" width="150" height="62" /></bpmndi:BPMNShape>')
    out.append(f'      <bpmndi:BPMNEdge id="Assoc_foundation_di" bpmnElement="Assoc_foundation"><di:waypoint x="{s.cx:.0f}" y="{s.bottom + 22:.0f}" /><di:waypoint x="{s.cx:.0f}" y="{s.bottom + 50:.0f}" /></bpmndi:BPMNEdge>')
    g = nodes["G_proven2"]
    out.append(f'      <bpmndi:BPMNShape id="Note_chain2_di" bpmnElement="Note_chain2"><dc:Bounds x="{g.x - 110:.0f}" y="{g.y - 78:.0f}" width="250" height="56" /></bpmndi:BPMNShape>')
    out.append(f'      <bpmndi:BPMNEdge id="Assoc_chain2_di" bpmnElement="Assoc_chain2"><di:waypoint x="{g.cx:.0f}" y="{g.y:.0f}" /><di:waypoint x="{g.cx:.0f}" y="{g.y - 22:.0f}" /></bpmndi:BPMNEdge>')
    out += ["    </bpmndi:BPMNPlane>", "  </bpmndi:BPMNDiagram>", "</bpmn:definitions>", ""]
    return "\n".join(out)


def overlays(m) -> dict:
    info = m["info"]
    data = {}
    for nid, a in m["attach"].items():
        chips = []
        for s in a["skills"]:
            i = info[s]
            chips.append({"id": s, "state": i["state"], "title": i["summary"],
                          "url": f"{REPO}/blob/main/{sp.folder_of(s)}/{s}/SKILL.md"})
        data[nid] = {"skills": chips, "external": a["external"], "header": a.get("header")}
    return data


def page(m, bpmn: str) -> str:
    n = m["nodes"]
    ov = {k: {**v, "dy": n[k].h + 4} for k, v in overlays(m).items()}
    return (HTML.replace("__XML__", bpmn.replace("</script", "<\\/script"))
            .replace("__OV__", json.dumps(ov, ensure_ascii=False).replace("</", "<\\/"))
            .replace("__VER__", BPMNJS).replace("__REPO__", REPO)
            .replace("__W__", f"{m['W']:.0f}").replace("__H__", f"{m['H']:.0f}"))


HTML = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>OD process map (BPMN)</title>
<!-- Generated by scripts/build_bpmn.py from docs/new-state/process.yaml - do not edit by hand. -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bpmn-js@__VER__/dist/assets/diagram-js.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bpmn-js@__VER__/dist/assets/bpmn-js.css">
<style>
:root{--bg:#f6f7f9;--ink:#1c2230;--muted:#5d6678;--line:#c5ccd8;--deep:#1a7f4b;--documented:#b8860b;--stub:#8a919e;--ext:#34495e}
html,body{margin:0;height:100%;background:var(--bg);color:var(--ink);font:14px/1.4 system-ui,Segoe UI,Roboto,sans-serif}
header{padding:10px 16px;border-bottom:1px solid var(--line);background:#fff;display:flex;gap:16px;align-items:center;flex-wrap:wrap}
header h1{font-size:16px;margin:0}
header .legend{display:flex;gap:10px;flex-wrap:wrap;font-size:12px;color:var(--muted)}
header button{border:1px solid var(--line);background:#fff;border-radius:6px;padding:4px 10px;cursor:pointer}
#canvas{height:calc(100% - 52px)}
.djs-container{background:#fff}
.sk{display:flex;flex-direction:column;gap:2px;width:max-content;max-width:190px;pointer-events:auto}
.sk a{display:block;font-size:10px;line-height:16px;padding:0 6px;border-radius:9px;border:1px solid var(--line);background:#fff;color:var(--ink);text-decoration:none;white-space:nowrap}
.sk a:hover{background:#eef3ff}
.sk a.deep{border-left:4px solid var(--deep)}.sk a.documented{border-left:4px solid var(--documented)}.sk a.stub{border-left:4px solid var(--stub)}
.sk a.ext{border:1px dashed #9aa7b5;background:#eef2f7;color:var(--ext)}
.sk a.ext::after{content:" \2197"}
.hdr{display:flex;gap:6px;font-size:11px}
.hdr a{white-space:nowrap;color:#1f4fbf;text-decoration:none;background:#fff;border:1px solid var(--line);border-radius:9px;padding:0 8px}
#err{display:none;padding:12px 16px;color:#a40000}
</style>
</head>
<body>
<header>
  <h1>OD process map (BPMN 2.0)</h1>
  <span class="legend"><span><b style="color:var(--deep)">|</b> built</span><span><b style="color:var(--documented)">|</b> documented</span><span><b style="color:var(--stub)">|</b> stub</span><span>dashed = OpenSpec skill, external (not part of this registry)</span><span>clock = external wait</span></span>
  <span style="flex:1"></span>
  <button id="fit">Fit</button><button id="zin">+</button><button id="zout">&minus;</button>
  <a href="OD_NewState_BPMN_Flow.bpmn" download>BPMN XML</a>
</header>
<div id="err"></div>
<div id="canvas"></div>
<script type="application/bpmn+xml" id="bpmn-src">__XML__</script>
<script src="https://cdn.jsdelivr.net/npm/bpmn-js@__VER__/dist/bpmn-navigated-viewer.production.min.js"></script>
<script>
const OV=__OV__;
const esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const viewer=new BpmnJS({container:'#canvas'});
const status=m=>{document.documentElement.setAttribute('data-status',m)};
viewer.importXML(document.getElementById('bpmn-src').textContent).then(r=>{
  const ov=viewer.get('overlays'),cv=viewer.get('canvas');
  for(const [id,a] of Object.entries(OV)){
    if(a.header){
      ov.add(id,{position:{top:-26,left:0},html:`<div class="hdr"><a href="${esc(a.header.url)}" target="_blank" rel="noopener">${esc(a.header.title)} (OpenSpec, external) ↗</a><a href="https://github.com/ops-digit-io/operations-digitalization-skill-registry/blob/main/${esc(a.header.how_to)}" target="_blank" rel="noopener">How to use</a></div>`});
    }
    const parts=[];
    for(const s of a.skills)parts.push(`<a class="${esc(s.state)}" href="${esc(s.url)}" target="_blank" rel="noopener" title="${esc(s.title)}">${esc(s.id)}</a>`);
    for(const e of a.external)parts.push(`<a class="ext" href="${esc(e.url)}" target="_blank" rel="noopener" title="OpenSpec skill (external)">${esc(e.name)}</a>`);
    if(parts.length)ov.add(id,{position:{top:a.dy,left:0},html:`<div class="sk">${parts.join('')}</div>`});
  }
  cv.zoom('fit-viewport','auto');status('ok'+(r.warnings&&r.warnings.length?' warnings='+r.warnings.length:''));
}).catch(e=>{const d=document.getElementById('err');d.style.display='block';d.textContent='BPMN import failed: '+e.message;status('error: '+e.message)});
document.getElementById('fit').onclick=()=>viewer.get('canvas').zoom('fit-viewport','auto');
document.getElementById('zin').onclick=()=>viewer.get('zoomScroll').stepZoom(1);
document.getElementById('zout').onclick=()=>viewer.get('zoomScroll').stepZoom(-1);
</script>
</body>
</html>
"""


def main() -> int:
    m = build_model()
    bpmn = xml(m)
    html = page(m, bpmn)
    if "--check" in sys.argv:
        stale = [p.name for p, t in ((OUT_XML, bpmn), (OUT_HTML, html))
                 if not p.exists() or p.read_text(encoding="utf-8").replace("\r\n", "\n") != t]
        if stale:
            print("stale: " + ", ".join(stale))
            return 1
        print("BPMN map up to date")
        return 0
    OUT_XML.write_text(bpmn, encoding="utf-8", newline="\n")
    OUT_HTML.write_text(html, encoding="utf-8", newline="\n")
    print(f"wrote {OUT_XML.name} ({len(m['nodes'])} nodes, {len(m['flows'])} flows) and {OUT_HTML.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
