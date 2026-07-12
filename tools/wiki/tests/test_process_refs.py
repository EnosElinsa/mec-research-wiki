from __future__ import annotations

import sys
import unittest
from pathlib import Path


TOOLS_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS_DIR))

import process_refs  # noqa: E402


class ProcessReferenceTests(unittest.TestCase):
    def test_flags_standalone_this_pass(self):
        match = process_refs.find_offending(
            "These collaborators are noted here rather than promoted this pass."
        )
        self.assertIsNotNone(match)
        self.assertEqual(match.group(0).lower(), "this pass")

    def test_does_not_flag_ordinary_passage(self):
        self.assertIsNone(
            process_refs.find_offending(
                "This passage describes the paper's communication model."
            )
        )

    def test_preserves_minibatch_exemption(self):
        self.assertIsNone(process_refs.find_offending("The mini-batch size is 128."))


if __name__ == "__main__":
    unittest.main()
