import importlib.util
import pathlib
import unittest


SCRIPT_PATH = pathlib.Path(__file__).parents[1] / "audit_intro_citations.py"
SPEC = importlib.util.spec_from_file_location("audit_intro_citations", SCRIPT_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class CitationAuditTests(unittest.TestCase):
    def test_expands_ieee_ranges_and_stops_at_next_top_level_section(self):
        markdown = """# Paper

## I. Introduction

First claim [1]–[3]. Second claim [1], [4].

Another paragraph repeats one source [2].

## II. Related Work

This citation must be ignored [4].
"""

        report = MODULE.audit_markdown(markdown)

        self.assertEqual(report["total_occurrences"], 6)
        self.assertEqual(report["unique_references"], 4)
        self.assertEqual(set(report["duplicates"]), {1, 2})
        self.assertEqual(report["duplicates"][1]["lines"], [5])
        self.assertEqual(report["duplicates"][2]["lines"], [5, 7])

    def test_reports_no_duplicates_when_each_reference_has_one_evidence_role(self):
        markdown = """# Paper

## I. 引言

Background claim [1], [2].

Scenario boundary [3]–[5].

## II. 相关工作
"""

        report = MODULE.audit_markdown(markdown)

        self.assertEqual(report["total_occurrences"], 5)
        self.assertEqual(report["unique_references"], 5)
        self.assertEqual(report["duplicates"], {})

    def test_raises_when_no_introduction_section_exists(self):
        with self.assertRaisesRegex(ValueError, "Introduction section"):
            MODULE.audit_markdown("# Paper\n\n## Methods\n")


if __name__ == "__main__":
    unittest.main()
