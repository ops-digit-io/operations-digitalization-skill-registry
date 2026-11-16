#!/usr/bin/env python3
"""Build the process map as a BPMN 2.0 flow chart from docs/new-state/process.yaml.

    docs/new-state/OD_NewState_BPMN_Flow.bpmn   the BPMN 2.0 XML: a pool with the five lanes; every branch is a collapsed
                                                 sub-process with its own diagram (drill-down); the OpenSpec process has
                                                 dedicated lanes (OD, IT / external developer)
    docs/new-state/OD_NewState_BPMN_Map.html    the same as a web page: bpmn-js (bpmn.io) renders the XML; click the + on a
                                                 box to open it; skills sit under their tasks as links, OpenSpec's skills are
                                                 external links

    python scripts/build_bpmn.py            # write both files
    python scripts/build_bpmn.py --check    # fail if they are stale

The top level shows only the lanes, the hand-offs between them and one box per branch. Inside a box are its steps, the waits
(timer events) and the skills. The layout is computed here, so the picture is regenerated from the data and cannot drift
from it. No OpenSpec file is copied into this registry: its skills are links into the OpenSpec repository.
"""
from __future__ import annotations

import json
import os
import pathlib
import sys
from xml.sax.saxutils import quoteattr

import yaml

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import skillpaths as sp  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
PROC = ROOT / "docs" / "new-state" / "process.yaml"
OUT_XML = ROOT / "docs" / "new-state" / "OD_NewState_BPMN_Flow.bpmn"
OUT_HTML = ROOT / "docs" / "new-state" / "OD_NewState_BPMN_Map.html"
REPO = "https://github.com/ops-digit-io/operations-digitalization-skill-registry"
BPMNJS = "17.11.1"   # bpmn-js release the page loads from jsdelivr (pinned)

TW, TH = 120, 80          # task
SW, SH = 160, 90          # collapsed sub-process
GW = 50                   # gateway
EV = 36                   # event
GAP = 55                  # horizontal gap between neighbours
LABEL_W = 30              # lane label column


class Node:
    def __init__(self, id, kind, name, x, y, w, h, parent=None):
        self.id, self.kind, self.name, self.x, self.y, self.w, self.h, self.parent = id, kind, name, x, y, w, h, parent
        self.children: list[Node] = []     # sub-process: its own flow nodes (own diagram)
        self.flows: list[Flow] = []        # sub-process: its own sequence flows
        self.lanes: list[dict] = []        # sub-process or process: lanes {id, title, top, h, nodes}
        self.notes: list[dict] = []        # text annotations {id, text, x, y, w, h, ref}

    @property
    def cx(self): return self.x + self.w / 2
    @property
    def cy(self): return self.y + self.h / 2
    @property
    def right(self): return self.x + self.w
    @property
    def bottom(self): return self.y + self.h


class Flow:
    def __init__(self, id, src, tgt, name="", mode="h"):
        self.id, self.src, self.tgt, self.name, self.mode = id, src, tgt, name, mode


def state(skill_id: str) -> str:
    """deep = references and scripts, documented = references only, stub = SKILL.md only."""
    d = sp.skill_dir(skill_id)
    refs = len(list((d / "references").glob("*.md"))) if (d / "references").is_dir() else 0
    scripts = len(list((d / "scripts").glob("*.py"))) if (d / "scripts").is_dir() else 0
    return "deep" if refs and scripts else ("documented" if refs else "stub")


def safe(s: str) -> str:
    return "".join(c if c.isalnum() else "_" for c in s)


SHORT = {"1a": "1a Machine already connected (no spend)", "1b": "1b Not connected: standardized-system onboarding",
         "2": "Use-case funnel", "front": "Shared front-end: requirements, tool-decision gate, capital",
         "3a": "3a New system: make / buy / integrate", "3b": "3b New connector for a new machine",
         "4": "Use-case promotion via Internal Communications"}


class Builder:
    def __init__(self):
        self.proc = yaml.safe_load(PROC.read_text(encoding="utf-8"))
        self.reg = yaml.safe_load((ROOT / "registry.yaml").read_text(encoding="utf-8"))
        self.info = {e["id"]: {"state": state(e["id"]), "summary": " ".join(str(e.get("summary", "")).split())} for e in self.reg["skills"]}
        self.nodes: dict[str, Node] = {}
        self.flows: list[Flow] = []
        self.attach: dict[str, dict] = {}
        self.steps = {st["id"]: st for st in self.proc["intake"]["steps"]}
        self.branches = {}
        for lane in self.proc["lanes"]:
            for br in lane["branches"]:
                self.branches[br["id"]] = br
                for st in br["steps"]:
                    self.steps[st["id"]] = st
        self.top = Node("Process_OD", "process", "", 0, 0, 0, 0)
        self.unplaced = 0        # labels that had no collision-free spot (reported by main; --check fails on them)

    # ---- primitives -------------------------------------------------------------------------------------------
    def mk(self, parent: Node, id, kind, name, x, cy, w=None, h=None, lane=None):
        k = kind.split(":")[0]
        w = w or {"task": TW, "gw": GW, "ev": EV, "sub": SW}[k]
        h = h or {"task": TH, "gw": GW, "ev": EV, "sub": SH}[k]
        n = Node(id, kind, name, x, cy - h / 2, w, h, parent)
        self.nodes[id] = n
        parent.children.append(n)
        if lane is not None:
            lane["nodes"].append(n)
        return n

    def flow(self, parent: Node, a: Node, b: Node, name="", mode="h"):
        f = Flow(f"F_{len(self.flows) + 1}", a, b, name, mode)
        self.flows.append(f)
        parent.flows.append(f)
        return f

    def _a(self, n: Node) -> dict:
        return self.attach.setdefault(n.id, {"skills": [], "external": [], "optional": []})

    def chips(self, n: Node, skills=(), external=()):
        if skills or external:
            a = self._a(n)
            a["skills"] += list(skills)
            a["external"] += list(external)

    def opt(self, n: Node, ids):
        """Extension skills that can help on this step: optional, drawn under the box and marked as extension."""
        if ids:
            a = self._a(n)
            a["optional"] += [i for i in ids if i not in a["optional"]]

    # ---- a row of steps inside a sub-process plane --------------------------------------------------------------
    def row(self, sub: Node, step_ids, start_name, end_name, cy=150, x0=70, id_prefix=""):
        x, prev = x0, None

        def put(n):
            nonlocal prev
            if prev is not None:
                self.flow(sub, prev, n)
            prev = n

        s = self.mk(sub, f"E_{id_prefix}start", "ev:start", start_name, x, cy)
        put(s)
        x += EV + GAP
        for sid in step_ids:
            st = self.steps[sid]
            t = self.mk(sub, "T_" + safe(sid), "task", f"{sid} {st['title']}", x, cy)
            self.chips(t, st.get("skills") or [])
            self.opt(t, st.get("proposed") or [])
            put(t)
            x += TW + GAP
            if st.get("wait"):
                tm = self.mk(sub, "E_wait_" + safe(sid), "ev:timer", f"wait {st['wait']}", x, cy)
                put(tm)
                x += EV + GAP
        e = self.mk(sub, f"E_{id_prefix}end", "ev:end", end_name, x, cy)
        put(e)
        return s, e

    def collapsed(self, parent: Node, id, name, x, cy, lane=None):
        return self.mk(parent, id, "sub", name, x, cy, lane=lane)

    # ---- the model --------------------------------------------------------------------------------------------
    def build(self):
        top = self.top
        spec = [("intake", "Intake · triage + fit-check", 250),
                ("lane1", "Lane 1 · Run a known use case (self-service)", 300),
                ("lane2", "Lane 2 · Develop a new use case (OD-led)", 190),
                ("lane4", "Lane 4 · Promote a proven use case (IC publishes)", 190),
                ("lane3", "Lane 3 · New system or connector (OD / Ext / IT-CS)", 330)]
        y = 0
        L = {}
        for lid, title, h in spec:
            L[lid] = {"id": lid, "title": title, "top": y, "h": h, "nodes": []}
            top.lanes.append(L[lid])
            y += h
        self.H = y
        X0, CP = 110, 210

        def col(c): return X0 + c * CP + (90 if c >= 3 else 0)      # extra room after the intake routing: its three labels sit on the last leg

        def cx_col(c, w): return col(c) + (SW - w) / 2        # centre a node of width w on the column of a collapsed box

        # intake
        cyI = L["intake"]["top"] + 85
        start = self.mk(top, "E_start", "ev:start", "Demand or request", cx_col(0, EV), cyI, lane=L["intake"])
        triage = self.mk(top, "T_i1", "task", "i1 Known use case? Triage + fit-check", col(1) + 20, cyI, lane=L["intake"])
        self.chips(triage, self.steps["i1"].get("skills") or [])
        self.opt(triage, self.steps["i1"].get("proposed") or [])
        route = self.mk(top, "G_route", "gw", "Where does it go?", col(2) + 55, cyI, lane=L["intake"])
        self.flow(top, start, triage); self.flow(top, triage, route)
        top.notes.append({"id": "Note_foundation", "text": "Foundation: every skill reads dept-context first (vocabulary, decision rights, honesty rules).",
                          "x": start.x - 40, "y": cyI + 48, "w": 170, "h": 64, "ref": start, "ref_mode": "down"})
        note = Node("Note_foundation", "note", "", start.x - 40, cyI + 48, 170, 64)
        self.nodes[note.id] = note
        self.chips(note, self.proc["spine"]["skills"])
        sx, sy = col(3) - 30, L["intake"]["top"] + 30
        top.notes.append({"id": "Note_spine_ext", "text": "Any step, optional: extension skills that serve the whole process.", "x": sx, "y": sy, "w": 330, "h": 44, "ref": None})
        spine_note = Node("Note_spine_ext", "note", "", sx, sy, 330, 44)
        self.nodes[spine_note.id] = spine_note
        self.opt(spine_note, self.proc["spine"].get("proposed") or [])
        self.attach[spine_note.id]["wrap"] = 430

        # lane 1
        t1 = L["lane1"]["top"]
        cy1a, cy1b, cyg1 = t1 + 85, t1 + 215, t1 + 150
        g1 = self.mk(top, "G_connected", "gw", "Machine already connected?", col(3) + 55, cyg1, lane=L["lane1"])
        s1a = self.collapsed(top, "S_1a", SHORT["1a"], col(4), cy1a, L["lane1"])
        s1b = self.collapsed(top, "S_1b", SHORT["1b"], col(4), cy1b, L["lane1"])
        m1 = self.mk(top, "G_merge1", "gw", "", col(5) + 55, cyg1, lane=L["lane1"])
        p1 = self.mk(top, "G_promote1", "gw", "Proven and adopted: promote?", col(6) + 55, cyg1, lane=L["lane1"])
        d1 = self.mk(top, "E_done1", "ev:end", "Live", col(7) + 62, cyg1, lane=L["lane1"])
        self.flow(top, route, g1, "known use case")
        self.flow(top, g1, s1a, "yes"); self.flow(top, g1, s1b, "no")
        self.flow(top, s1a, m1); self.flow(top, s1b, m1); self.flow(top, m1, p1); self.flow(top, p1, d1, "no")

        # lane 2
        cy2 = L["lane2"]["top"] + 95
        s2 = self.collapsed(top, "S_2", SHORT["2"], col(3), cy2, L["lane2"])
        g2 = self.mk(top, "G_proven2", "gw", "Proven and repeatable?", col(4) + 55, cy2, lane=L["lane2"])
        d2 = self.mk(top, "E_done2", "ev:end", "Graduated", col(5) + 62, cy2, lane=L["lane2"])
        self.flow(top, route, s2, "new use case")
        self.flow(top, s2, g2); self.flow(top, g2, d2, "no")

        # lane 4 (entered only from a live, adopted use case)
        cy4 = L["lane4"]["top"] + 95
        s4 = self.collapsed(top, "S_4", SHORT["4"], col(7), cy4, L["lane4"])
        d4 = self.mk(top, "E_done4", "ev:end", "Published, feedback routed", col(8) + 62, cy4, lane=L["lane4"])
        self.flow(top, p1, s4, "yes", "down"); self.flow(top, g2, s4, "yes", "down")
        self.flow(top, s4, d4)

        # lane 3
        t3 = L["lane3"]["top"]
        cyF, cy3a, cy3b = t3 + 165, t3 + 90, t3 + 240
        sf = self.collapsed(top, "S_front", SHORT["front"], col(3), cyF, L["lane3"])
        r3 = self.mk(top, "G_route3", "gw", "New system, or new connector?", col(4) + 55, cyF, lane=L["lane3"])
        s3a = self.collapsed(top, "S_3a", SHORT["3a"], col(5), cy3a, L["lane3"])
        s3b = self.collapsed(top, "S_3b", SHORT["3b"], col(5), cy3b, L["lane3"])
        d3a = self.mk(top, "E_done3a", "ev:end", "Live", col(6) + 62, cy3a, lane=L["lane3"])
        d3b = self.mk(top, "E_done3b", "ev:end", "Live on MDL", col(6) + 62, cy3b, lane=L["lane3"])
        self.flow(top, route, sf, "new system / connector")
        self.flow(top, sf, r3); self.flow(top, r3, s3a, "3a"); self.flow(top, r3, s3b, "3b")
        self.flow(top, s3a, d3a); self.flow(top, s3b, d3b)

        # ---- inside the boxes
        self.inner_1a(s1a); self.inner_1b(s1b); self.inner_2(s2); self.inner_front(sf)
        self.inner_3a(s3a); self.inner_3b(s3b); self.inner_4(s4)
        self.W = max(n.right for n in top.children) + 90
        return self

    def inner_1a(self, sub):
        self.row(sub, ["1a1", "1a2", "1a3"], "Machine connected", "Live", id_prefix="1a_")

    def inner_1b(self, sub):
        self.row(sub, ["1b1", "1b2", "1b3", "1b4"], "No machine connection", "Live", id_prefix="1b_")

    def inner_2(self, sub):
        s, e = self.row(sub, ["21", "22", "23", "23a", "24", "25", "26"], "Plant use-case demand", "Graduated", id_prefix="2_")
        sub.notes.append({"id": "Note_chain2", "text": "Chains out of Lane 2: needs new software to Lane 3a, needs a new connection to Lane 3b, proven and repeatable to the catalog, then Lane 1.",
                          "x": e.x - 90, "y": e.bottom + 175, "w": 250, "h": 64, "ref": e, "ref_mode": "down"})

    def inner_front(self, sub):
        self.row(sub, ["31", "32", "33"], "Demand clear?", "Demand clear: hand on", id_prefix="front_")

    def inner_4(self, sub):
        self.row(sub, ["41", "42", "43", "44"], "Live, adopted use case", "Published", id_prefix="4_")

    def inner_3b(self, sub):
        self.row(sub, ["3b4", "3b5", "3b6"], "New connector needed", "Live on MDL", id_prefix="3b_")

    def inner_3a(self, sub):
        st = self.steps["3a4"]
        opts = {o["id"]: o for o in st["options"]}
        cyA, cyB, cyC = 120, 300, 480
        s = self.mk(sub, "E_3a_start", "ev:start", "New system", 70, cyB)
        gb = self.mk(sub, "G_build", "gw", "Build path", 70 + EV + GAP, cyB)
        x1 = gb.right + GAP + 90
        o1 = self.mk(sub, "T_3a1", "task", "3a.1 " + opts["3a.1"]["title"], x1, cyA)
        o2 = self.mk(sub, "T_3a2", "task", "3a.2 " + opts["3a.2"]["title"], x1, cyB)
        self.chips(o1, opts["3a.1"]["skills"]); self.chips(o2, opts["3a.2"]["skills"])
        s34 = self.mk(sub, "S_3a4", "sub", "3a4 Package / build: IT demand via OpenSpec (3a.3 external build, 3a.4 foreign app)", x1, cyC, w=210, h=100)
        gm = self.mk(sub, "G_merge3", "gw", "", x1 + 210 + GAP, cyB)
        t5 = self.mk(sub, "T_3a5", "task", "3a5 " + self.steps["3a5"]["title"], gm.right + GAP, cyB)
        t6 = self.mk(sub, "T_3a6", "task", "3a6 " + self.steps["3a6"]["title"], t5.right + GAP, cyB)
        e = self.mk(sub, "E_3a_end", "ev:end", "Live", t6.right + GAP, cyB)
        self.chips(t5, self.steps["3a5"].get("skills") or []); self.chips(t6, self.steps["3a6"].get("skills") or [])
        self.opt(t5, self.steps["3a5"].get("proposed") or []); self.opt(t6, self.steps["3a6"].get("proposed") or [])
        self.opt(s34, st.get("proposed") or [])
        self.flow(sub, s, gb)
        self.flow(sub, gb, o1, "3a.1 reuse"); self.flow(sub, gb, o2, "3a.2 self dev"); self.flow(sub, gb, s34, "3a.3 / 3a.4")
        self.flow(sub, o1, gm); self.flow(sub, o2, gm); self.flow(sub, s34, gm)
        self.flow(sub, gm, t5); self.flow(sub, t5, t6); self.flow(sub, t6, e)
        self.inner_openspec(s34)

    def inner_openspec(self, sub):
        """3a4: the IT demand follows OpenSpec. Dedicated lanes: OD prepares and hands over, IT / the external developer builds."""
        st = self.steps["3a4"]
        ext = st["external_process"]
        subs = st["substeps"]
        od = {"id": "OD", "title": "OD (demand owner)", "top": 30, "h": 245, "nodes": []}
        it = {"id": "IT", "title": "IT / external developer", "top": 275, "h": 250, "nodes": []}
        sub.lanes = [od, it]
        cyO, cyI = od["top"] + 105, it["top"] + 80
        x = 100
        s = self.mk(sub, "E_3a4_start", "ev:start", "Clear demand", x, cyO, lane=od)
        prev = s
        x += EV + GAP
        for ss in subs:
            lane, cy = (od, cyO) if ss["owner"] == "OD" else (it, cyI)
            tn = self.mk(sub, "T_" + safe(ss["id"]), "task", f"{ss['id']} {ss['title']}", x, cy, lane=lane)
            self.chips(tn, [], ss.get("external") or [])
            self.flow(sub, prev, tn, "hand over" if (prev.id != s.id and prev in od["nodes"] and lane is it) else "")
            prev = tn
            x += TW + GAP + 10
        e = self.mk(sub, "E_3a4_end", "ev:end", "Archived", x, cyI, lane=it)
        self.flow(sub, prev, e)
        self._a(s)["header"] = {"url": ext["url"], "how_to": ext["how_to"], "title": ext["title"]}


def waypoints(f: Flow):
    a, b = f.src, f.tgt
    if f.mode == "down":      # leave the gateway at the bottom, go down, enter the target from the left
        return [(a.cx, a.bottom), (a.cx, b.cy), (b.x, b.cy)]
    if abs(a.cy - b.cy) < 1:
        return [(a.right, a.cy), (b.x, b.cy)]
    gap = b.x - a.right
    mx = a.right + 28 if gap >= 130 else a.right + max(15, min(45, gap / 2))     # bend close to the source: the long last leg carries the label
    return [(a.right, a.cy), (mx, a.cy), (mx, b.cy), (b.x, b.cy)]


# ---- label placement: every label goes to the nearest free spot; shapes, flow lines, skill chips, notes and the
#      drill-down buttons are obstacles, and a placed label becomes one too -----------------------------------------------
CHAR_W, LINE_H = 6.2, 14


def text_box(text: str, maxw=130):
    w = min(maxw, max(36.0, len(text) * CHAR_W + 10))
    lines = max(1, -(-int(len(text) * CHAR_W) // int(w - 8)))
    return w, lines * LINE_H + 6


def overlap(a, b, m=2.0) -> bool:
    return not (a[0] + a[2] + m <= b[0] or b[0] + b[2] + m <= a[0] or a[1] + a[3] + m <= b[1] or b[1] + b[3] + m <= a[1])


def segments(f: Flow):
    pts = waypoints(f)
    return list(zip(pts, pts[1:]))


def seg_rect(p, q, pad=2.5):
    return (min(p[0], q[0]) - pad, min(p[1], q[1]) - pad, abs(p[0] - q[0]) + 2 * pad, abs(p[1] - q[1]) + 2 * pad)


def chip_stack(a: dict):
    """(width, height) of the chips under a box: core and OpenSpec chips, then the caption and the optional extension chips."""
    names = list(a["skills"]) + [e["name"] for e in a["external"]]
    opt = a.get("optional") or []
    wrap = a.get("wrap", 0)
    w = max([len(t) * 5.6 + 22 for t in names] + [len(t) * 5.6 + 46 for t in opt] + [0])
    h = 18 * len(names)
    if opt:
        if wrap:
            x, rows = 0.0, 1
            for t in opt:
                cw = len(t) * 5.6 + 46
                if x + cw > wrap:
                    rows, x = rows + 1, 0.0
                x += cw + 4
            w, h = wrap, h + 14 + 18 * rows
        else:
            h += 14 + 18 * len(opt)
    return w, h


def layout_labels(b: Builder, container: Node):
    """Returns ({node id: rect}, {flow id: rect}, number of labels that could not be placed without a collision)."""
    obstacles: list[tuple] = []
    for n in container.children:
        obstacles.append((n.x, n.y, n.w, n.h))
        a = b.attach.get(n.id)
        if a:
            w_, h_ = chip_stack(a)
            if h_:
                obstacles.append((n.x, n.bottom + (28 if n.kind == "sub" else 4), w_, h_))
            if a.get("header"):
                obstacles.append((n.x - 10, n.y - 74, 330, 22))
        if n.kind == "sub":
            obstacles.append((n.right - 22, n.bottom + 2, 26, 22))      # the drill-down button of a collapsed box
    for nt in container.notes:
        obstacles.append((nt["x"], nt["y"], nt["w"], nt["h"]))
        a = b.attach.get(nt["id"])
        if a:
            w_, h_ = chip_stack(a)
            if h_:
                obstacles.append((nt["x"], nt["y"] + nt["h"] + 4, w_, h_))
    for f in container.flows:
        for p, q in segments(f):
            obstacles.append(seg_rect(p, q))
    placed: list[tuple] = []
    node_rects: dict[str, tuple] = {}
    flow_rects: dict[str, tuple] = {}
    bad = 0

    def choose(cands, tag=""):
        nonlocal bad
        best, score = None, 1e9
        for c in cands:
            s = sum(overlap(c, o) for o in obstacles) * 3 + sum(overlap(c, o) for o in placed) * 3
            if s < score:
                best, score = c, s
            if s == 0:
                break
        if score > 0:
            bad += 1
            if os.environ.get("BPMN_DEBUG"):
                print(f"  collision in {container.id}: {tag} {tuple(round(v) for v in best)}")
        placed.append(best)
        return best

    for n in container.children:                                       # gateways and events: label above or below
        if not n.name or not (n.kind == "gw" or n.kind.startswith("ev")):
            continue
        w, h = text_box(n.name, 120 if n.kind == "gw" else 110)
        c = []
        for dy in (-h - 4, n.h + 4):
            for dx in (-w / 2 + n.w / 2, -w + n.w / 2 + 14, n.w / 2 - 14):
                c.append((n.x + dx, n.y + dy, w, h))
        c.sort(key=lambda r: 0)                                         # keep the preference order
        if n.kind.startswith("ev"):
            c = [c[3], c[0], c[4], c[5], c[1], c[2]]                    # events: below first
        node_rects[n.id] = choose(c, n.name)
    for f in container.flows:                                           # flow names: beside the segment nearest the target
        if not f.name:
            continue
        w, h = text_box(f.name, 120)
        segs = segments(f)
        order = list(reversed(range(len(segs))))
        c = []
        for i in order:
            (x1, y1), (x2, y2) = segs[i]
            if abs(y1 - y2) < 1:                                        # horizontal: above, then below, centred or at the ends
                L = abs(x2 - x1)
                for t in (0.65, 0.5, 0.8, 0.35):
                    mxp = x1 + (x2 - x1) * t
                    c.append((mxp - w / 2, y1 - h - 7, w, h))
                    c.append((mxp - w / 2, y1 + 7, w, h))
            else:                                                       # vertical: left, then right, near the target end
                ye = y2 if i == len(segs) - 1 else y1
                for yy in (ye - (y2 - y1) * 0.0, (y1 + y2) / 2):
                    c.append((x1 - w - 8, yy - h / 2, w, h))
                    c.append((x1 + 8, yy - h / 2, w, h))
        flow_rects[f.id] = choose(c, f.name)
    return node_rects, flow_rects, bad


def xml(b: Builder) -> str:
    top, flows = b.top, b.flows
    tag = {"task": "task", "gw": "exclusiveGateway", "sub": "subProcess"}
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<!-- Generated by scripts/build_bpmn.py from docs/new-state/process.yaml - do not edit by hand. -->',
           '<bpmn:definitions xmlns:bpmn="http://www.omg.org/spec/BPMN/20100524/MODEL" xmlns:bpmndi="http://www.omg.org/spec/BPMN/20100524/DI" '
           'xmlns:dc="http://www.omg.org/spec/DD/20100524/DC" xmlns:di="http://www.omg.org/spec/DD/20100524/DI" id="Definitions_OD" '
           'targetNamespace="https://github.com/ops-digit-io/operations-digitalization-skill-registry/bpmn">',
           '  <bpmn:collaboration id="Collaboration_OD">',
           '    <bpmn:participant id="Participant_OD" name="Operations Digitalization" processRef="Process_OD" />',
           '  </bpmn:collaboration>',
           '  <bpmn:process id="Process_OD" name="Operations Digitalization" isExecutable="false">']
    inc: dict[str, list[str]] = {}
    outg: dict[str, list[str]] = {}
    for f in flows:
        outg.setdefault(f.src.id, []).append(f.id)
        inc.setdefault(f.tgt.id, []).append(f.id)

    def laneset(container: Node, ind: str, prefix: str):
        if not container.lanes:
            return
        out.append(f'{ind}<bpmn:laneSet id="LaneSet_{prefix}">')
        for ln in container.lanes:
            out.append(f'{ind}  <bpmn:lane id="Lane_{prefix}_{ln["id"]}" name={quoteattr(ln["title"])}>')
            for n in ln["nodes"]:
                out.append(f"{ind}    <bpmn:flowNodeRef>{n.id}</bpmn:flowNodeRef>")
            out.append(f"{ind}  </bpmn:lane>")
        out.append(f"{ind}</bpmn:laneSet>")

    def notes(container: Node, ind: str):
        for nt in container.notes:
            out.append(f'{ind}<bpmn:textAnnotation id="{nt["id"]}"><bpmn:text>{quoteattr(nt["text"])[1:-1]}</bpmn:text></bpmn:textAnnotation>')
            if nt.get("ref"):
                out.append(f'{ind}<bpmn:association id="Assoc_{nt["id"]}" sourceRef="{nt["ref"].id}" targetRef="{nt["id"]}" />')

    def emit(n: Node, ind: str):
        k = n.kind.split(":")[0]
        if k == "ev":
            sub = n.kind.split(":")[1]
            t = {"start": "startEvent", "end": "endEvent", "timer": "intermediateCatchEvent"}[sub]
            body = "<bpmn:timerEventDefinition />" if sub == "timer" else ""
        else:
            t, body = tag[k], ""
        out.append(f'{ind}<bpmn:{t} id="{n.id}"' + (f" name={quoteattr(n.name)}" if n.name else "") + ">")
        for i in inc.get(n.id, []):
            out.append(f"{ind}  <bpmn:incoming>{i}</bpmn:incoming>")
        for o in outg.get(n.id, []):
            out.append(f"{ind}  <bpmn:outgoing>{o}</bpmn:outgoing>")
        if body:
            out.append(f"{ind}  {body}")
        if k == "sub":
            laneset(n, ind + "  ", n.id)
            for c in n.children:
                emit(c, ind + "  ")
            for f in n.flows:
                out.append(f'{ind}  <bpmn:sequenceFlow id="{f.id}" sourceRef="{f.src.id}" targetRef="{f.tgt.id}"' + (f" name={quoteattr(f.name)}" if f.name else "") + " />")
            notes(n, ind + "  ")
        out.append(f"{ind}</bpmn:{t}>")

    laneset(top, "    ", "OD")
    for n in top.children:
        emit(n, "    ")
    for f in top.flows:
        out.append(f'    <bpmn:sequenceFlow id="{f.id}" sourceRef="{f.src.id}" targetRef="{f.tgt.id}"' + (f" name={quoteattr(f.name)}" if f.name else "") + " />")
    notes(top, "    ")
    out.append("  </bpmn:process>")

    # ---- diagram interchange: one diagram per plane (the pool, and each sub-process that has content)
    def shapes(container: Node, ind: str):
        nlab, flab, bad = layout_labels(b, container)
        b.unplaced += bad
        for n in container.children:
            extra = ' isExpanded="false"' if n.kind == "sub" else ""
            lbl = ""
            if n.id in nlab:
                r = nlab[n.id]
                lbl = f'<bpmndi:BPMNLabel><dc:Bounds x="{r[0]:.0f}" y="{r[1]:.0f}" width="{r[2]:.0f}" height="{r[3]:.0f}" /></bpmndi:BPMNLabel>'
            out.append(f'{ind}<bpmndi:BPMNShape id="{n.id}_di" bpmnElement="{n.id}"{extra}><dc:Bounds x="{n.x:.0f}" y="{n.y:.0f}" width="{n.w:.0f}" height="{n.h:.0f}" />{lbl}</bpmndi:BPMNShape>')
        for f in container.flows:
            pts = "".join(f'<di:waypoint x="{x:.0f}" y="{y:.0f}" />' for x, y in waypoints(f))
            lab = ""
            if f.id in flab:
                r = flab[f.id]
                lab = f'<bpmndi:BPMNLabel><dc:Bounds x="{r[0]:.0f}" y="{r[1]:.0f}" width="{r[2]:.0f}" height="{r[3]:.0f}" /></bpmndi:BPMNLabel>'
            out.append(f'{ind}<bpmndi:BPMNEdge id="{f.id}_di" bpmnElement="{f.id}">{pts}{lab}</bpmndi:BPMNEdge>')
        for nt in container.notes:
            r = nt.get("ref")
            out.append(f'{ind}<bpmndi:BPMNShape id="{nt["id"]}_di" bpmnElement="{nt["id"]}"><dc:Bounds x="{nt["x"]:.0f}" y="{nt["y"]:.0f}" width="{nt["w"]}" height="{nt["h"]}" /></bpmndi:BPMNShape>')
            if r is not None:
                out.append(f'{ind}<bpmndi:BPMNEdge id="Assoc_{nt["id"]}_di" bpmnElement="Assoc_{nt["id"]}"><di:waypoint x="{r.cx:.0f}" y="{r.bottom + (22 if r.kind.startswith("ev") else 0):.0f}" /><di:waypoint x="{r.cx:.0f}" y="{nt["y"]:.0f}" /></bpmndi:BPMNEdge>')

    out.append('  <bpmndi:BPMNDiagram id="Diagram_OD">')
    out.append('    <bpmndi:BPMNPlane id="Plane_OD" bpmnElement="Collaboration_OD">')
    out.append(f'      <bpmndi:BPMNShape id="Participant_OD_di" bpmnElement="Participant_OD" isHorizontal="true"><dc:Bounds x="0" y="0" width="{b.W:.0f}" height="{b.H:.0f}" /></bpmndi:BPMNShape>')
    for ln in top.lanes:
        out.append(f'      <bpmndi:BPMNShape id="Lane_OD_{ln["id"]}_di" bpmnElement="Lane_OD_{ln["id"]}" isHorizontal="true"><dc:Bounds x="{LABEL_W}" y="{ln["top"]:.0f}" width="{b.W - LABEL_W:.0f}" height="{ln["h"]:.0f}" /></bpmndi:BPMNShape>')
    shapes(top, "      ")
    out += ["    </bpmndi:BPMNPlane>", "  </bpmndi:BPMNDiagram>"]

    def planes(container: Node):
        for n in container.children:
            if n.kind != "sub":
                continue
            out.append(f'  <bpmndi:BPMNDiagram id="Diagram_{n.id}">')
            out.append(f'    <bpmndi:BPMNPlane id="Plane_{n.id}" bpmnElement="{n.id}">')
            if n.lanes:
                width = max(c.right for c in n.children) + 70
                for ln in n.lanes:
                    out.append(f'      <bpmndi:BPMNShape id="Lane_{n.id}_{ln["id"]}_di" bpmnElement="Lane_{n.id}_{ln["id"]}" isHorizontal="true"><dc:Bounds x="{LABEL_W}" y="{ln["top"]}" width="{width - LABEL_W:.0f}" height="{ln["h"]}" /></bpmndi:BPMNShape>')
            shapes(n, "      ")
            out.extend(["    </bpmndi:BPMNPlane>", "  </bpmndi:BPMNDiagram>"])
            planes(n)

    planes(top)
    out += ["</bpmn:definitions>", ""]
    return "\n".join(out)


def overlays(b: Builder) -> dict:
    data = {}
    for nid, a in b.attach.items():
        chips = []
        for s in a["skills"]:
            i = b.info[s]
            chips.append({"id": s, "state": i["state"], "title": i["summary"], "url": f"{REPO}/blob/main/{sp.folder_of(s)}/{s}/SKILL.md"})
        optional = []
        for e in a.get("optional") or []:
            i = b.info[e]
            optional.append({"id": e, "state": i["state"], "title": i["summary"], "url": f"{REPO}/blob/main/{sp.folder_of(e)}/{e}/SKILL.md"})
        n = b.nodes[nid]
        data[nid] = {"skills": chips, "external": a["external"], "optional": optional, "wrap": a.get("wrap", 0), "header": a.get("header"),
                     "dy": n.h + (28 if n.kind == "sub" else 4)}
    return data


def page(b: Builder, bpmn: str) -> str:
    return (HTML.replace("__XML__", bpmn.replace("</script", "<\\/script"))
            .replace("__OV__", json.dumps(overlays(b), ensure_ascii=False).replace("</", "<\\/"))
            .replace("__VER__", BPMNJS).replace("__REPO__", REPO))


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
.djs-label{paint-order:stroke;stroke:#fff;stroke-width:3px;stroke-linejoin:round}
.sk{display:flex;flex-direction:column;gap:2px;width:max-content;max-width:190px;pointer-events:auto}
.sk a{display:block;font-size:10px;line-height:16px;padding:0 6px;border-radius:9px;border:1px solid var(--line);background:#fff;color:var(--ink);text-decoration:none;white-space:nowrap}
.sk a:hover{background:#eef3ff}
.sk a.deep{border-left:4px solid var(--deep)}.sk a.documented{border-left:4px solid var(--documented)}.sk a.stub{border-left:4px solid var(--stub)}
.sk a.ext{border:1px dashed #9aa7b5;background:#eef2f7;color:var(--ext)}
.sk a.ext::after{content:" \2197"}
.sk .optcap{font-size:9px;color:var(--muted);margin:3px 0 0 2px}.sk .optrow{display:flex;flex-direction:column;gap:2px}.sk.wrap .optrow{flex-direction:row;flex-wrap:wrap}
.sk a.opt{border:1px dotted #8a919e;background:#fafafa;color:#59627a;font-style:italic}
.xt{font-style:normal;font-size:8px;text-transform:uppercase;letter-spacing:.04em;background:#e8ebf2;border-radius:6px;padding:0 4px;margin-right:4px;color:#59627a}
.hdr{display:flex;gap:6px;font-size:11px}
.hdr a{white-space:nowrap;color:#1f4fbf;text-decoration:none;background:#fff;border:1px solid var(--line);border-radius:9px;padding:0 8px}
#err{display:none;padding:12px 16px;color:#a40000}
</style>
</head>
<body>
<header>
  <h1>OD process map (BPMN 2.0)</h1>
  <span class="legend"><span>click the <b>+</b> on a box to open it, the breadcrumb to go back</span><span><b style="color:var(--deep)">|</b> built</span><span><b style="color:var(--documented)">|</b> documented</span><span><b style="color:var(--stub)">|</b> stub</span><span>dashed = OpenSpec skill, external (not part of this registry)</span><span>clock = external wait</span><span><i class="xt">ext</i> &lt;extension&gt; skill: optional, use where it fits (below the boxes)</span></span>
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
const fit=()=>viewer.get('canvas').zoom('fit-viewport','auto');
viewer.importXML(document.getElementById('bpmn-src').textContent).then(r=>{
  const ov=viewer.get('overlays');
  for(const [id,a] of Object.entries(OV)){
    if(a.header){
      ov.add(id,{position:{top:-74,left:-10},html:`<div class="hdr"><a href="${esc(a.header.url)}" target="_blank" rel="noopener">${esc(a.header.title)}: OpenSpec (external) ↗</a><a href="__REPO__/blob/main/${esc(a.header.how_to)}" target="_blank" rel="noopener">How to use</a></div>`});
    }
    const parts=[];
    for(const s of a.skills)parts.push(`<a class="${esc(s.state)}" href="${esc(s.url)}" target="_blank" rel="noopener" title="${esc(s.title)}">${esc(s.id)}</a>`);
    for(const e of a.external)parts.push(`<a class="ext" href="${esc(e.url)}" target="_blank" rel="noopener" title="OpenSpec skill (external)">${esc(e.name)}</a>`);
    let opt='';
    if((a.optional||[]).length)opt=`<div class="optcap">&lt;extension&gt; &middot; optional</div><div class="optrow">${a.optional.map(s=>`<a class="opt ${esc(s.state)}" href="${esc(s.url)}" target="_blank" rel="noopener" title="Extension skill, optional: ${esc(s.title)}"><i class="xt">ext</i>${esc(s.id)}</a>`).join('')}</div>`;
    if(parts.length||opt)ov.add(id,{position:{top:a.dy,left:0},html:`<div class="sk${a.wrap?' wrap':''}"${a.wrap?` style="max-width:${a.wrap}px"`:''}>${parts.join('')}${opt}</div>`});
  }
  const open=location.hash.slice(1);          // deep link: ...BPMN_Map.html#S_3a4 opens that box
  if(open){const pl=viewer.get('elementRegistry').get(open+'_plane');if(pl)viewer.get('canvas').setRootElement(pl)}
  fit();status('ok'+(r.warnings&&r.warnings.length?' warnings='+r.warnings.length:''));
  viewer.on('root.set',()=>setTimeout(fit,0));
}).catch(e=>{const d=document.getElementById('err');d.style.display='block';d.textContent='BPMN import failed: '+e.message;status('error: '+e.message)});
document.getElementById('fit').onclick=fit;
document.getElementById('zin').onclick=()=>viewer.get('zoomScroll').stepZoom(1);
document.getElementById('zout').onclick=()=>viewer.get('zoomScroll').stepZoom(-1);
</script>
</body>
</html>
"""


def main() -> int:
    b = Builder().build()
    bpmn = xml(b)
    html = page(b, bpmn)
    if b.unplaced:
        print(f"{b.unplaced} label(s) overlap another element: move a box or shorten the text")
        if "--check" in sys.argv:
            return 1
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
    print(f"wrote {OUT_XML.name} ({len(b.nodes)} nodes, {len(b.flows)} flows) and {OUT_HTML.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
