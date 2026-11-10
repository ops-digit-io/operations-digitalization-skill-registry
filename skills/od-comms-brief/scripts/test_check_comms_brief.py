#!/usr/bin/env python3
"""Tests for check_comms_brief.py. Run: python3 test_check_comms_brief.py"""
import unittest

import check_comms_brief as c

GOOD = """# Brief: Line screen at Plant A
## Message
At Plant A the shift lead reviews downtime at the daily meeting on one line.
## Audience
- Other plants and key users: you can request it from the catalogue.
## Proof points
| Claim | Evidence class | Source | Worded as |
|---|---|---|---|
| The screen is used in the daily meeting | not yet assessed | Handover record, 2026-11-01 | result |
| Expected effect on stops | ESTIMATION | Business case file, 2026-10-15 | claim |
## Call to action
A plant requests the use case through the catalogue via the DBVE role.
## Sensitivity screen
Checked: no individuals, no hosts, no internal links.
## Approvals
| Approval | Role | Status | Date |
|---|---|---|---|
| The story is true | Plant owner | pending | |
| OD tells it | OD lead | pending | |
| Publication | Internal Communications | pending | |
"""


def checks(text):
    return {f[1] for f in c.analyze(text)}


class CommsBriefChecks(unittest.TestCase):
    def test_good_brief_has_no_blocker(self):
        self.assertFalse([f for f in c.analyze(GOOD) if f[0] == "BLOCKER"])

    def test_missing_approvals_section_blocks(self):
        text = GOOD.split("## Approvals")[0]
        self.assertIn("missing-section", checks(text))

    def test_proof_without_source_blocks(self):
        text = GOOD.replace("Handover record, 2026-11-01", "")
        self.assertIn("proof-without-source", checks(text))

    def test_proof_without_class_blocks(self):
        text = GOOD.replace("ESTIMATION", "good")
        self.assertIn("proof-without-class", checks(text))

    def test_saving_as_result_blocks(self):
        text = GOOD.replace("Expected effect on stops | ESTIMATION | Business case file, 2026-10-15 | claim",
                            "Saving of cost | CALCULATION | Business case file | result")
        self.assertIn("saving-as-result", checks(text))

    def test_figure_without_class_blocks(self):
        text = GOOD.replace("on one line.", "on one line and saves 25% of stops.")
        self.assertIn("figure-without-class", checks(text))

    def test_link_blocks(self):
        text = GOOD.replace("catalogue.", "catalogue at https://intranet.example/uc.", 1)
        self.assertIn("sensitive-item", checks(text))

    def test_named_individual_blocks(self):
        text = GOOD.replace("At Plant A", "Built by Anna Example, at Plant A")
        self.assertIn("named-individual", checks(text))

    def test_superlative_warns(self):
        text = GOOD.replace("reviews downtime", "has a game-changing way to review downtime")
        self.assertIn("superlative", checks(text))

    def test_missing_approver_blocks(self):
        text = GOOD.replace("| Publication | Internal Communications | pending | |\n", "")
        self.assertIn("missing-approver", checks(text))


if __name__ == "__main__":
    unittest.main()
