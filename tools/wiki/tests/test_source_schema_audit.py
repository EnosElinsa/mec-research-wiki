from __future__ import annotations

import pathlib
import json
import sys
import tempfile
import unittest
from unittest import mock


TOOLS_DIR = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS_DIR))

import source_schema_audit  # noqa: E402


BASE_FRONTMATTER = """---
type: source
title: \"Example source\"
authors: [\"A. Author\"]
year: 2026
url: \"\"
venue: \"Example venue\"
tags: [source]
related: []
created: 2026-07-16
updated: 2026-07-16
modeling_card: {status}
---
"""

CARD = r"""## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A UAV serves mobile users over a fading wireless channel.

**Problem & objective**: A stochastic control problem with objective $\min_\pi J(\pi)$ for long-run task latency.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Offloading action | $a_t$ | discrete | Selected service decision |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | $a_t$ must belong to the feasible action set. |

**Algorithm**: Actor-critic learning with constrained action selection.
"""

RELATED = """## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Author et al. [x] studied UAV service control for mobile users. They formulated a stochastic control problem with latency as the objective. The method selects feasible actions with an actor-critic learner. Simulation results show lower task latency under the reported settings.
"""


def page(status: str = "required", *, card: str | None = CARD, related: str = RELATED) -> str:
    return (
        BASE_FRONTMATTER.format(status=status)
        + "# Example source\n\n"
        + "## Citation\n\nCitation details.\n\n"
        + "## TL;DR\n\nA concise positioning sentence.\n\n"
        + (card or "")
        + related
        + "\n## Problem framing\n\nThe paper frames a decision problem.\n"
    )


class SourceSchemaAuditTests(unittest.TestCase):
    def test_accepts_complete_modeling_page(self):
        self.assertEqual(source_schema_audit.audit_text(page()), [])

    def test_accepts_non_modeling_page_without_card(self):
        text = page(status="not_applicable", card=None)
        self.assertEqual(source_schema_audit.audit_text(text), [])

    def test_requires_citation_as_first_h2(self):
        no_citation = page().replace("## Citation\n\nCitation details.\n\n", "")
        errors = source_schema_audit.audit_text(no_citation)
        self.assertTrue(any("Citation" in error for error in errors))

    def test_requires_card_for_modeling_page(self):
        errors = source_schema_audit.audit_text(page(card=None))
        self.assertTrue(any("Modeling Quick-Use Card" in error for error in errors))

    def test_rejects_card_on_non_modeling_page(self):
        errors = source_schema_audit.audit_text(page(status="not_applicable"))
        self.assertTrue(any("not_applicable" in error for error in errors))

    def test_rejects_invalid_modeling_card_value(self):
        errors = source_schema_audit.audit_text(page(status="maybe"))
        self.assertTrue(any("modeling_card" in error for error in errors))

    def test_related_work_must_follow_tldr_and_card(self):
        text = page().replace(CARD + RELATED, RELATED + CARD, 1)
        errors = source_schema_audit.audit_text(text)
        self.assertTrue(any("order" in error.lower() for error in errors))

    def test_related_work_rejects_em_dash_double_dash_cjk_and_missing_placeholder(self):
        bad_related = RELATED.replace("[x]", "[1]").replace("for mobile users", "for mobile users — safely").replace("actor-critic", "actor--critic") + "中文\n"
        errors = source_schema_audit.audit_text(page(related=bad_related))
        self.assertTrue(any("[x]" in error for error in errors))
        self.assertTrue(any("dash" in error.lower() for error in errors))
        self.assertTrue(any("CJK" in error for error in errors))

    def test_related_work_requires_exact_single_guidance_blockquote(self):
        without_note = RELATED.replace(
            "> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.\n\n",
            "",
        )
        extra_note = RELATED.replace(
            "> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.",
            "> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.\n> Extra note.",
        )
        self.assertTrue(
            any("guidance blockquote" in error for error in source_schema_audit.audit_text(page(related=without_note)))
        )
        self.assertTrue(
            any("guidance blockquote" in error for error in source_schema_audit.audit_text(page(related=extra_note)))
        )

    def test_related_work_requires_blank_line_after_guidance(self):
        lazy_quote = RELATED.replace(
            "formal citation number.\n\nAuthor",
            "formal citation number.\nAuthor",
        )
        errors = source_schema_audit.audit_text(page(related=lazy_quote))
        self.assertTrue(any("blank line" in error for error in errors))

    def test_related_work_rejects_lists_tables_and_code_fences(self):
        prose = RELATED.rstrip() + "\n"
        variants = [
            prose + "- Extra list item.\n",
            prose + "| Extra | Table |\n|---|---|\n| a | b |\n",
            prose + "```text\nextra code\n```\n",
            prose + "### Note\nAdditional text.\n",
        ]
        for variant in variants:
            with self.subTest(variant=variant[-30:]):
                errors = source_schema_audit.audit_text(page(related=variant))
                self.assertTrue(any("prose only" in error for error in errors))

    def test_related_work_sentence_count_handles_fig_abbreviation(self):
        with_figure = RELATED.replace(
            "Simulation results show",
            "Fig. 3 reports that simulation results show",
        )
        self.assertEqual(source_schema_audit.audit_text(page(related=with_figure)), [])

    def test_sentence_count_masks_abbreviations_and_counts_lowercase_starts(self):
        three_sentences = RELATED.split("\n\n", 2)[0] + "\n\n" + RELATED.split("\n\n", 2)[1] + "\n\n" + (
            "Author et al. [x] studied the setting in Sec. IV. "
            "They compared TD3 vs. SAC under the stated configuration. "
            "Results report the measured outcome.\n"
        )
        errors = source_schema_audit.audit_text(page(related=three_sentences))
        self.assertTrue(any("4-8 sentences" in error for error in errors))

        lowercase_start = RELATED.replace(
            "They formulated",
            "j-PPO represented the control policy. They formulated",
        )
        self.assertEqual(source_schema_audit.audit_text(page(related=lowercase_start)), [])

    def test_card_requires_labels_and_non_placeholder_values(self):
        bad_card = CARD.replace("**Algorithm**: Actor-critic learning with constrained action selection.", "**Algorithm**: ...").replace("| Variable | Symbol | Type / range | Meaning |", "| Variable | Symbol | Meaning |")
        errors = source_schema_audit.audit_text(page(card=bad_card))
        self.assertTrue(any("Algorithm" in error for error in errors))
        self.assertTrue(any("table" in error.lower() for error in errors))

    def test_card_requires_standard_guidance_blockquote(self):
        no_note = CARD.replace(
            "> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.\n\n",
            "",
        )
        errors = source_schema_audit.audit_text(page(card=no_note))
        self.assertTrue(any("guidance blockquote" in error for error in errors))

    def test_card_problem_objective_requires_math(self):
        no_math = CARD.replace(r"$\min_\pi J(\pi)$", "minimize J")
        errors = source_schema_audit.audit_text(page(card=no_math))
        self.assertTrue(any("math expression" in error for error in errors))

    def test_related_work_requires_one_prose_paragraph(self):
        split_related = RELATED.replace(
            "They formulated", "\n\nThey formulated", 1
        )
        errors = source_schema_audit.audit_text(page(related=split_related))
        self.assertTrue(any("one prose paragraph" in error for error in errors))

    def test_card_rejects_blank_table_cells(self):
        blank_row = CARD.replace(
            "| Offloading action | $a_t$ | discrete | Selected service decision |",
            "| Offloading action |  | discrete | Selected service decision |",
        )
        errors = source_schema_audit.audit_text(page(card=blank_row))
        self.assertTrue(any("blank cell" in error for error in errors))

    def test_card_requires_table_labels_and_separator_rows(self):
        bad_card = CARD.replace("**Decision variables**:\n\n", "").replace(
            "|---|---|\n| C1", "| C1", 1
        )
        errors = source_schema_audit.audit_text(page(card=bad_card))
        self.assertTrue(any("Decision variables" in error for error in errors))
        self.assertTrue(any("separator" in error.lower() for error in errors))

    def test_card_tables_require_contiguous_rows(self):
        variants = [
            CARD.replace("| Variable | Symbol | Type / range | Meaning |\n|---", "| Variable | Symbol | Type / range | Meaning |\n\n|---"),
            CARD.replace("|---|---|---|---|\n| Offloading", "|---|---|---|---|\n\n| Offloading"),
        ]
        for variant in variants:
            with self.subTest():
                errors = source_schema_audit.audit_text(page(card=variant))
                self.assertTrue(any("table" in error.lower() for error in errors))

    def test_card_rejects_dash_as_table_placeholder(self):
        dash = CARD.replace("| $a_t$ |", "| - |")
        errors = source_schema_audit.audit_text(page(card=dash))
        self.assertTrue(any("placeholder" in error.lower() for error in errors))

    def test_card_enforces_decision_constraints_algorithm_order(self):
        decision_start = CARD.index("**Decision variables**:")
        constraint_start = CARD.index("**Constraints**:")
        algorithm_start = CARD.index("**Algorithm**:")
        swapped = (
            CARD[:decision_start]
            + CARD[constraint_start:algorithm_start]
            + CARD[decision_start:constraint_start]
            + CARD[algorithm_start:]
        )
        errors = source_schema_audit.audit_text(page(card=swapped))
        self.assertTrue(any("label order" in error.lower() for error in errors))

    def test_card_rejects_blank_cells_in_any_data_row(self):
        extra_blank = CARD.replace(
            "| C1 | $a_t$ must belong to the feasible action set. |",
            "| C1 | $a_t$ must belong to the feasible action set. |\n| C2 |  |",
        )
        errors = source_schema_audit.audit_text(page(card=extra_blank))
        self.assertTrue(any("blank cell" in error for error in errors))

    def test_card_allows_escaped_pipe_in_expression(self):
        escaped_pipe = CARD.replace(
            "$a_t$ must belong to the feasible action set.",
            "$a_t \\| s_t$ must belong to the feasible action set.",
        )
        self.assertEqual(source_schema_audit.audit_text(page(card=escaped_pipe)), [])

    def test_headings_inside_fenced_code_do_not_count_as_sections(self):
        fenced_example = page().replace(
            "The paper frames a decision problem.",
            "The paper frames a decision problem.\n\n```markdown\n## Related Work Paragraph\n## Modeling Quick-Use Card\n```",
        )
        self.assertEqual(source_schema_audit.audit_text(fenced_example), [])

    def test_empty_h2_does_not_consume_following_tldr_text(self):
        malformed = page().replace("## TL;DR", "##\nTL;DR")
        errors = source_schema_audit.audit_text(malformed)
        self.assertTrue(any("TL;DR" in error for error in errors))

    def test_rejects_duplicate_exact_h2_headings(self):
        duplicated = page() + "\n## Problem framing\n\nDuplicate section.\n"
        errors = source_schema_audit.audit_text(duplicated)
        self.assertTrue(any("duplicate H2" in error for error in errors))

    def test_source_paths_accepts_repeated_files_and_directories(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            source_dir = root / "wiki" / "sources"
            source_dir.mkdir(parents=True)
            first = source_dir / "first.md"
            second = source_dir / "second.md"
            first.write_text(page(), encoding="utf-8")
            second.write_text(page(status="not_applicable", card=None), encoding="utf-8")

            with mock.patch.object(source_schema_audit.wikilib, "repo_root", return_value=str(root)):
                paths = source_schema_audit.source_paths(
                    ["wiki/sources", "wiki/sources/first.md"]
                )

            self.assertEqual(paths, sorted([str(first), str(second)]))

    def test_cli_returns_nonzero_and_writes_json_for_failures(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            source_dir = root / "wiki" / "sources"
            source_dir.mkdir(parents=True)
            bad = source_dir / "bad.md"
            bad.write_text(page(status="maybe"), encoding="utf-8")
            scratch = root / ".curation-out"

            with (
                mock.patch.object(source_schema_audit.wikilib, "repo_root", return_value=str(root)),
                mock.patch.object(source_schema_audit.wikilib, "scratch_dir", return_value=str(scratch)),
            ):
                result = source_schema_audit.main(
                    ["--path", str(bad), "--json", "source-schema.json"]
                )

            self.assertEqual(result, 1)
            report = json.loads((scratch / "source-schema.json").read_text(encoding="utf-8"))
            self.assertIn("modeling_card", json.dumps(report))

    def test_cli_returns_usage_error_for_missing_path(self):
        result = source_schema_audit.main(["--path", "wiki/sources/missing.md"])
        self.assertEqual(result, 2)

    def test_cli_returns_usage_error_for_empty_directory(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = source_schema_audit.main(["--path", tmp])
        self.assertEqual(result, 2)

    def test_cli_rejects_non_source_markdown_paths(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            concept_dir = root / "wiki" / "concepts"
            concept_dir.mkdir(parents=True)
            concept = concept_dir / "concept.md"
            concept.write_text(page(), encoding="utf-8")
            result = source_schema_audit.main(["--path", str(concept)])
        self.assertEqual(result, 2)

    def test_rejects_duplicate_modeling_card_keys(self):
        duplicate = page().replace(
            "modeling_card: required",
            "modeling_card: required\nmodeling_card: not_applicable",
        )
        errors = source_schema_audit.audit_text(duplicate)
        self.assertTrue(any("exactly one modeling_card" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
