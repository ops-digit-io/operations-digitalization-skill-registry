#!/usr/bin/env python3
"""Check a process derivation package and its BPMN model (stdlib only).

    python check_derivation.py package.md [process.bpmn]

Package: the gate record (section 0 of assets/process-derivation-package.md) must name the use-case request, the
use-case demand and the validated prototype, and the prototype result must be "passed".
Model: well-formed BPMN 2.0 with a process, a start and an end event, connected sequence flow, named tasks, named
exclusive and inclusive splits with labelled outgoing flows, every flow node in a lane when lanes are used, at least one
alternative or exception path, and a diagram (bpmndi) so the model can be shown. These are the structural rules this skill
applies; they are good practice, not requirements of the BPMN standard.

Exit code 0 prints READY; 1 prints the findings. Nothing is changed.
"""
from __future__ import annotations

import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

GATE_KEYS = ["Use-case request", "Use-case demand", "Validated prototype", "Prototype result"]
TASKS = {"task", "userTask", "serviceTask", "manualTask", "scriptTask", "sendTask", "receiveTask", "businessRuleTask",
         "callActivity", "subProcess"}
EVENTS = {"startEvent", "endEvent", "intermediateCatchEvent", "intermediateThrowEvent", "boundaryEvent"}
GATEWAYS = {"exclusiveGateway", "inclusiveGateway", "parallelGateway", "eventBasedGateway", "complexGateway"}
SPLITTING = {"exclusiveGateway", "inclusiveGateway"}


def local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def gate_findings(text: str) -> list[str]:
    out = []
    for key in GATE_KEYS:
        m = re.search(r"^\|\s*\*\*" + re.escape(key) + r"\*\*\s*\|\s*(.*?)\s*\|\s*$", text, re.M)
        if not m:
            out.append(f"gate record: no row '{key}' (section 0 of the package)")
            continue
        value = m.group(1).strip()
        if not value or value.startswith("⟨"):
            out.append(f"gate record: '{key}' is empty; the gate is not met")
        elif key == "Prototype result" and not re.search(r"\bpassed\b", value, re.I):
            out.append(f"gate record: prototype result is '{value}', not passed; stop and send it back")
    return out


def model_findings(xml_text: str) -> list[str]:
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError as e:
        return [f"model: not well-formed XML ({e})"]
    if local(root.tag) != "definitions":
        return ["model: the root element is not bpmn:definitions"]
    out = []
    processes = [e for e in root.iter() if local(e.tag) == "process"]
    if not processes:
        return ["model: no process element"]
    if not any(local(e.tag) == "BPMNDiagram" for e in root.iter()):
        out.append("model: no diagram interchange (bpmndi:BPMNDiagram); a tool cannot show the model")
    for proc in processes:
        pid = proc.get("id", "?")
        nodes = {c.get("id"): c for c in proc if local(c.tag) in TASKS | EVENTS | GATEWAYS}
        flows = [c for c in proc if local(c.tag) == "sequenceFlow"]
        kinds = [local(c.tag) for c in nodes.values()]
        if "startEvent" not in kinds:
            out.append(f"process {pid}: no start event")
        if "endEvent" not in kinds:
            out.append(f"process {pid}: no end event")
        incoming: dict[str, int] = {}
        outgoing: dict[str, list[ET.Element]] = {}
        for f in flows:
            s, t = f.get("sourceRef"), f.get("targetRef")
            for ref, role in ((s, "source"), (t, "target")):
                if ref not in nodes:
                    out.append(f"process {pid}: flow {f.get('id')} has an unknown {role} '{ref}'")
            incoming[t] = incoming.get(t, 0) + 1
            outgoing.setdefault(s, []).append(f)
        for nid, n in nodes.items():
            k = local(n.tag)
            label = f"{k} '{n.get('name') or nid}'"
            if k not in ("startEvent", "boundaryEvent") and not incoming.get(nid):
                out.append(f"process {pid}: {label} has no incoming flow")
            if k != "endEvent" and not outgoing.get(nid):
                out.append(f"process {pid}: {label} has no outgoing flow")
            if (k in TASKS or k in ("startEvent", "endEvent")) and not (n.get("name") or "").strip():
                out.append(f"process {pid}: {k} {nid} has no name (verb and object for tasks, what has happened for events)")
            if k in SPLITTING and len(outgoing.get(nid, [])) > 1:
                if not (n.get("name") or "").strip():
                    out.append(f"process {pid}: splitting gateway {nid} has no name (write the question)")
                for f in outgoing[nid]:
                    has_cond = any(local(c.tag) == "conditionExpression" for c in f)
                    if not (f.get("name") or "").strip() and not has_cond and n.get("default") != f.get("id"):
                        out.append(f"process {pid}: flow {f.get('id')} out of gateway {nid} has no label (write the answer)")
        lanes = [e for e in proc.iter() if local(e.tag) == "lane"]
        if lanes:
            referenced = {r.text.strip() for ln in lanes for r in ln if local(r.tag) == "flowNodeRef" and r.text}
            for nid, n in nodes.items():
                if nid not in referenced:
                    out.append(f"process {pid}: {local(n.tag)} '{n.get('name') or nid}' is in no lane")
        alternative = any(local(n.tag) == "boundaryEvent" for n in nodes.values()) or any(
            local(n.tag) in SPLITTING | {"eventBasedGateway"} and len(outgoing.get(i, [])) > 1 for i, n in nodes.items())
        if not alternative:
            out.append(f"process {pid}: no alternative or exception path (a split gateway or a boundary event)")
    return out


def main(argv: list[str]) -> int:
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 2
    findings = gate_findings(Path(argv[0]).read_text(encoding="utf-8-sig"))      # utf-8-sig: tolerate a byte-order mark
    if len(argv) > 1:
        findings += model_findings(Path(argv[1]).read_text(encoding="utf-8-sig"))
    if findings:
        print("NOT READY")
        for f in findings:
            print(f"- {f}")
        return 1
    print("READY")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
