#!/usr/bin/env python3
"""Build docs/new-state/OD_NewState_ProcessFlow.html - the new-state lanes with the skills on every step.

Reads docs/new-state/process.yaml (steps, core `skills`, extension `proposed`, waits) and each skill's
SKILL.md (status: stable = built, draft = draft). Core skills are the department's skills; extension skills
are drawn as small outlined chips under the step they deepen. A step with no core skill is a human or plant
step. The page keeps the owner's original design.

    python3 scripts/build_process_flow.py            # write the page
    python3 scripts/build_process_flow.py --check    # fail if the page is stale
"""
from __future__ import annotations
import html, pathlib, sys
import yaml

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import skillpaths as sp  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "new-state" / "OD_NewState_ProcessFlow.html"
PROC = ROOT / "docs" / "new-state" / "process.yaml"

CSS_EXTRA = """
  .chip.draft{background:var(--part-bg);color:var(--part);}
  .chip.ext{background:#fff;color:var(--b2);border:1px solid var(--b4);font-weight:500;font-size:8px;}
  .node.draft{border-top-color:var(--part);} .node.draft .state{color:var(--part);}
  .node.human{border-top-color:var(--b4);background:#f7f9fd;} .node.human .state{color:var(--b2);}
  .node.supplier{border-top-color:var(--melon-d);background:#fff6f3;} .node.supplier .state{color:var(--melon-d);}
  .exts{display:flex;flex-wrap:wrap;gap:0;margin-top:2px;padding-top:4px;border-top:1px dotted var(--g6);}
  .exts .lbl{font-size:7.5px;font-weight:700;letter-spacing:.04em;text-transform:uppercase;color:var(--g3);width:100%;margin-bottom:1px;}
  .sw.draft{background:var(--part);} .sw.human{background:var(--b4);} .sw.supplier{background:var(--melon-d);}
  .node .t{padding-right:40px;}
  .node .d{font-size:8.5px;color:var(--g2);margin:2px 0 4px;line-height:1.35;}
  .node .nt{font-size:8px;font-style:italic;color:var(--g3);margin-top:2px;}
  .chipk{display:inline-block;font-size:8.5px;padding:1px 6px;border-radius:3px;}
"""
LANE = {"lane1": ("l1", "Lane 1", "Self-service"), "lane2": ("l2", "Lane 2", "OD-led"),
        "lane3": ("l3", "Lane 3", "OD / Ext / IT&middot;CS")}
BTAG = {"1a": ("1a", "connected"), "1b": ("1b", "not connected"), "2": ("", ""),
        "front": ("Front&#8209;end", "shared"), "3a": ("3a", "new system"), "3b": ("3b", "new connector")}
SUPPLIER = {"3b5": "Integration execution is supplier-dependent (App-Store-Ops feature request)"}


def status(sid: str) -> str:
    fm = yaml.safe_load((sp.skill_dir(sid) / "SKILL.md").read_text(encoding="utf-8").split("---", 2)[1])
    return "built" if str(fm["metadata"].get("status")) == "stable" else "draft"


def e(s: str) -> str:
    return html.escape(str(s))


def chips(sk: list) -> str:
    return "".join(f'<span class="chip {status(x)}">{e(x)}</span>' for x in sk)


def node(st: dict) -> str:
    core = st.get("skills") or []
    states = [status(s) for s in core]
    if not core:
        cls, lab = "human", "No skill"
    elif all(x == "built" for x in states):
        cls, lab = "built", "Built"
    else:
        cls, lab = "draft", "Draft"
    out = [f'<div class="node {cls}"><span class="state">{lab}</span>',
           f'<div class="t">{e(st.get("no", ""))} &middot; {e(st["title"])}</div>',
           f'<div class="who">{e(st.get("who", ""))}</div>',
           f'<div class="d">{e(st.get("text", ""))}</div>', chips(core)]
    if st.get("note"):
        out.append(f'<div class="nt">{e(st["note"])}</div>')
    out.append("</div>")
    return "".join(out)


def track(steps: list) -> str:
    parts = []
    for i, st in enumerate(steps):
        if st.get("options"):
            continue
        parts.append(node(st))
        if i < len(steps) - 1:
            w = st.get("wait")
            parts.append(f'<div class="arr wait"><span class="wlab">{e(w.split()[0])}</span></div>' if w and "wks" in w else '<div class="arr"></div>')
    return '<div class="track">' + "".join(parts) + "</div>"


def options(steps: list) -> str:
    for st in steps:
        if st.get("options"):
            return ('<div class="opts">' + "".join(
                f'<div class="opt"><span class="h">{e(o["id"])} &middot; {e(o["owner"])}</span><b>{e(o["title"])}</b><br>{e(o["text"])}'
                f'<div style="margin-top:4px">{chips(o["skills"])}{(" <i>" + e(o["note"]) + "</i>") if o.get("note") else ""}</div></div>'
                for o in st["options"]) + "</div>")
    return ""


def build() -> str:
    p = yaml.safe_load(PROC.read_text(encoding="utf-8"))
    css = (ROOT / "scripts" / "process_flow.css").read_text(encoding="utf-8") + CSS_EXTRA
    core = [s for s in sp.all_ids() if sp.library_of(s) == "core"]
    n_built = sum(1 for s in core if status(s) == "built")
    body = []
    body.append('<div class="lane" style="background:#f2f5fb;"><div class="spine" style="background:var(--b1);">'
                '<div class="ln">Intake</div><div class="nm">Classify</div><div class="ow">one lane per demand</div></div>'
                '<div class="body" style="background:#f2f5fb;"><div class="fallnote" style="font-size:11px">'
                '<b>Is the use case already known (in the catalog)?</b><br>'
                'YES &rarr; run it &rarr; <b>Lane&nbsp;1</b> (1a connected / 1b standardized onboarding)<br>'
                'NO, a new <b>use case</b> on an existing machine &rarr; <b>Lane&nbsp;2</b><br>'
                'NO, a new <b>system / app</b> and/or a new <b>machine connection</b> &rarr; <b>Lane&nbsp;3</b> (3a system 3a.1&ndash;3a.4 / 3b connector)'
                '</div></div></div>')
    notes = {"lane1": 'Fall-through: not truly catalogued &rarr; <b>Lane&nbsp;2</b> &nbsp;&middot;&nbsp; no standardized system fits or non-standard integration &rarr; <b>Lane&nbsp;3</b>',
             "lane2": 'Chains out: needs new software &rarr; <b>Lane&nbsp;3&middot;3a</b> &nbsp;&middot;&nbsp; needs a new machine connection &rarr; <b>Lane&nbsp;3&middot;3b</b> &nbsp;&middot;&nbsp; proven &amp; repeatable &rarr; catalogue &rarr; <b>Lane&nbsp;1</b>',
             "lane3": 'Post-handover (outside OD ownership): delivery via IT quarterly sprints or external dev; CS sign-off &amp; platform deploy; rollout &amp; adoption with OD support'}
    for lane in p["lanes"]:
        cls, ln, _ = LANE[lane["id"]]
        rows = []
        for br in lane["branches"]:
            tag, sub = BTAG[br["id"]]
            opt = options(br["steps"])
            if opt:
                rows.append(f'<div class="brow"><div class="btag">{tag}<span>{sub}</span></div><div style="flex:1">{opt}</div></div>')
            t = track(br["steps"])
            rows.append(f'<div class="brow"><div class="btag">{"" if opt else tag}<span>{"" if opt else sub}</span></div>{t}</div>' if tag else t)
        body.append(f'<div class="lane {cls}"><div class="spine"><div class="ln">{ln}</div><div class="nm">{e(lane["title"])}</div>'
                    f'<div class="ow">{e(lane["who"])}</div></div><div class="body"><div class="fallnote" style="margin:0 0 8px">{e(lane["summary"])}</div>'
                    f'{"".join(rows)}<div class="fallnote">{notes[lane["id"]]}</div></div></div>')
    spn = p["spine"]
    body.append('<div class="lane" style="background:#f7f8fc;"><div class="spine" style="background:var(--g2);"><div class="ln">Not on a step</div>'
                '<div class="nm">Department skills</div></div><div class="body" style="background:#f7f8fc;">'
                f'<div class="fallnote" style="margin:0 0 6px">{e(spn["summary"])}</div>{chips(spn["skills"])}</div></div>')
    drafts = [s for s in core if status(s) == "draft"]
    cards = "".join(f'<div class="gcard thin"><div class="gn">{e(s)}</div><div class="gl">core &middot; draft</div></div>' for s in drafts)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>OD New-State Service Lanes — Process Flow</title>
<style>{css}</style>
</head>
<body>
<div class="page">
  <header>
    <div class="logo"><div class="mark">neu<b>werk</b></div><div class="tag">The neuwerk way</div></div>
    <div class="eyebrow">Operations Digitalization &middot; MPEE</div>
    <h1>New-State Service Lanes <span class="thin">— three branched lanes, with the department skills</span></h1>
  </header>
  <div class="legend">
    <div class="grp"><b>Skill in the registry:</b>
      <span class="st"><span class="sw built"></span>Built</span>
      <span class="st"><span class="sw draft"></span>Draft</span>
      <span class="st"><span class="sw human"></span>No skill on this step</span>
    </div>
    <div class="grp"><span style="color:var(--melon-d);font-weight:700;font-size:13px;">&#8594;</span> external wait (weeks)</div>
  </div>
  <div class="flow">{"".join(body)}</div>
  <div class="gaps"><h2>{len(drafts)} of {len(core)} department skills are still drafts</h2><div class="gaprow">{cards}</div></div>
  <div class="foot">
    <div class="src">Steps, numbering and skills transcribed from the department map <b>OD_ServiceLine_NewState_VSM.html</b>
    (OD Department Knowledge/OD-instance/20-lanes-newstate-DRAFT; Thomas, 2026-09-09, 3 branched lanes 2026-09-10) via
    <b>docs/new-state/process.yaml</b>; skill state from each <code>SKILL.md</code> (stable = built, draft = draft).
    {len(core)} department skills ({n_built} built). Generated by <b>scripts/build_process_flow.py</b>.</div>
    <div class="way">The neuwerk way</div>
  </div>
</div>
</body>
</html>
"""


def main(argv: list[str]) -> int:
    page = build()
    if "--check" in argv:
        if not OUT.exists() or OUT.read_text(encoding="utf-8") != page:
            print("OD_NewState_ProcessFlow.html is stale: run scripts/build_process_flow.py", file=sys.stderr)
            return 1
        print("process flow up to date")
        return 0
    OUT.write_text(page, encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
