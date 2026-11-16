import unittest
from pathlib import Path

import check_derivation as c

EXAMPLE = Path(__file__).resolve().parent.parent / "assets" / "to-be-process.example.bpmn"
GOOD_PACKAGE = """
| | |
|---|---|
| **Use-case request** | record A (shift lead, line X) |
| **Use-case demand** | record B |
| **Validated prototype** | record C, click-dummy, plant representative |
| **Prototype result** | passed |
"""


class Gate(unittest.TestCase):
    def test_complete_gate_passes(self):
        self.assertEqual(c.gate_findings(GOOD_PACKAGE), [])

    def test_missing_row(self):
        text = GOOD_PACKAGE.replace("| **Use-case demand** | record B |\n", "")
        self.assertTrue(any("Use-case demand" in f for f in c.gate_findings(text)))

    def test_placeholder_is_empty(self):
        text = GOOD_PACKAGE.replace("record B", "⟨record⟩")
        self.assertTrue(any("empty" in f for f in c.gate_findings(text)))

    def test_inconclusive_stops(self):
        text = GOOD_PACKAGE.replace("passed", "inconclusive")
        self.assertTrue(any("not passed" in f for f in c.gate_findings(text)))


class Model(unittest.TestCase):
    def setUp(self):
        self.xml = EXAMPLE.read_text(encoding="utf-8")

    def test_example_is_ready(self):
        self.assertEqual(c.model_findings(self.xml), [])

    def test_not_xml(self):
        self.assertTrue(c.model_findings("<a>")[0].startswith("model: not well-formed"))

    def test_no_end_event(self):
        xml = self.xml.replace("<bpmn:endEvent", "<bpmn:intermediateThrowEvent").replace("</bpmn:endEvent>", "</bpmn:intermediateThrowEvent>")
        self.assertTrue(any("no end event" in f for f in c.model_findings(xml)))

    def test_unnamed_gateway(self):
        xml = self.xml.replace('name="Reason known?" ', "")
        self.assertTrue(any("gateway" in f and "no name" in f for f in c.model_findings(xml)))

    def test_unlabelled_flow(self):
        xml = self.xml.replace(' name="yes"', "")
        self.assertTrue(any("no label" in f for f in c.model_findings(xml)))

    def test_task_not_in_lane(self):
        xml = self.xml.replace("<bpmn:flowNodeRef>Task_assign</bpmn:flowNodeRef>", "")
        self.assertTrue(any("is in no lane" in f for f in c.model_findings(xml)))

    def test_dangling_reference(self):
        xml = self.xml.replace('targetRef="Task_assign"', 'targetRef="Task_missing"')
        self.assertTrue(any("unknown target" in f for f in c.model_findings(xml)))

    def test_no_alternative_path(self):
        xml = self.xml.replace('sourceRef="Gateway_known" targetRef="Timer_wait"', 'sourceRef="Task_select" targetRef="Timer_wait"')
        self.assertTrue(any("no alternative" in f or "no outgoing" in f for f in c.model_findings(xml)))

    def test_no_diagram(self):
        i = self.xml.index("<bpmndi:BPMNDiagram")
        j = self.xml.index("</bpmndi:BPMNDiagram>") + len("</bpmndi:BPMNDiagram>")
        self.assertTrue(any("no diagram" in f for f in c.model_findings(self.xml[:i] + self.xml[j:])))


if __name__ == "__main__":
    unittest.main()
