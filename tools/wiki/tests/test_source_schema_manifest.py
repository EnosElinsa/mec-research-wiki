from __future__ import annotations

import pathlib
import json
import sys
import tempfile
import unittest


TOOLS_DIR = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS_DIR))

import source_schema_manifest  # noqa: E402


def source_page(title: str, refs: list[str], modeling_card: str | None = None) -> str:
    field = f"modeling_card: {modeling_card}\n" if modeling_card else ""
    bullets = "\n".join(f"- `{ref}`" for ref in refs)
    return (
        "---\n"
        "type: source\n"
        f'title: "{title}"\n'
        "authors: []\n"
        "year: 2026\n"
        "url: \"\"\n"
        "venue: \"\"\n"
        f"{field}"
        "tags: [source]\n"
        "related: []\n"
        "created: 2026-07-16\n"
        "updated: 2026-07-16\n"
        "---\n\n"
        f"# {title}\n\n"
        "## Raw artifacts\n\n"
        f"{bullets}\n"
    )


class SourceSchemaManifestTests(unittest.TestCase):
    def test_resolves_exact_folder_fallback_and_title_match_without_skips(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            wiki_sources = root / "wiki" / "sources"
            raw_sources = root / "raw" / "sources"
            wiki_sources.mkdir(parents=True)
            raw_sources.mkdir(parents=True)

            exact_folder = raw_sources / "Exact_Paper"
            exact_folder.mkdir()
            (exact_folder / "Exact_Paper.md").write_text(
                "# Exact Paper\n\nEvidence.\n", encoding="utf-8"
            )

            duplicate_a = raw_sources / "Duplicate_A"
            duplicate_b = raw_sources / "Duplicate_B"
            duplicate_a.mkdir()
            duplicate_b.mkdir()
            (duplicate_a / "Duplicate_A.md").write_text(
                "# Shared Paper\n\nFirst parse.\n", encoding="utf-8"
            )
            (duplicate_b / "Duplicate_B.md").write_text(
                "# Shared Paper\n\nSecond parse.\n", encoding="utf-8"
            )

            (wiki_sources / "exact.md").write_text(
                source_page(
                    "Exact Paper",
                    ["raw/sources/Exact_Paper/full.md"],
                    modeling_card="required",
                ),
                encoding="utf-8",
            )
            (wiki_sources / "shared.md").write_text(
                source_page(
                    "Shared Paper",
                    [
                        "raw/sources/Duplicate_A/Duplicate_A.md",
                        "raw/sources/Duplicate_B/Duplicate_B.md",
                    ],
                ),
                encoding="utf-8",
            )

            report = source_schema_manifest.build_manifest(
                wiki_sources=wiki_sources,
                raw_sources=raw_sources,
                repo_root=root,
            )

            self.assertEqual(report["counts"]["source_pages"], 2)
            self.assertEqual(report["counts"]["raw_markdown_files"], 3)
            self.assertEqual(report["counts"]["resolved_parse_paths"], 3)
            self.assertEqual(report["counts"]["pages_with_multiple_parses"], 1)
            self.assertEqual(report["unresolved_recorded_refs"], [])
            self.assertEqual(report["ambiguous_resolutions"], [])
            self.assertEqual(report["orphan_raw_folders"], [])

            entries = {entry["slug"]: entry for entry in report["entries"]}
            self.assertEqual(entries["exact"]["modeling_card"], "required")
            self.assertEqual(entries["exact"]["review_status"], "classified")
            self.assertEqual(entries["shared"]["modeling_card"], None)
            self.assertEqual(entries["shared"]["review_status"], "pending")
            self.assertEqual(len(entries["shared"]["parses"]), 2)

    def test_reports_source_without_raw_artifacts_block(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            wiki_sources = root / "wiki" / "sources"
            raw_sources = root / "raw" / "sources"
            wiki_sources.mkdir(parents=True)
            raw_sources.mkdir(parents=True)
            (wiki_sources / "missing.md").write_text(
                "---\ntype: source\ntitle: Missing\n---\n# Missing\n",
                encoding="utf-8",
            )

            report = source_schema_manifest.build_manifest(
                wiki_sources=wiki_sources,
                raw_sources=raw_sources,
                repo_root=root,
            )

            self.assertEqual(report["entries"][0]["status"], "unresolved")
            self.assertTrue(report["unresolved_recorded_refs"])

    def test_merges_grounding_sidecars_and_detects_classification_conflicts(self):
        report = {
            "entries": [
                {
                    "slug": "paper",
                    "modeling_card": "required",
                    "parses": [{"path": "raw/sources/paper/paper.md"}],
                    "classification_evidence": [],
                    "related_work_evidence": [],
                    "review_status": "classified",
                }
            ],
            "evidence_conflicts": [],
        }
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            parse = root / "raw" / "sources" / "paper" / "paper.md"
            parse.parent.mkdir(parents=True)
            parse.write_text("\n".join(f"line {number}" for number in range(1, 51)), encoding="utf-8")
            grounded = root / "grounded.json"
            grounded.write_text(
                json.dumps(
                    [
                        {
                            "slug": "paper",
                            "modeling_card": "required",
                            "classification_evidence": [
                                {"path": "raw/sources/paper/paper.md", "lines": "10-20", "note": "objective and constraints"}
                            ],
                            "related_work_evidence": [
                                {"path": "raw/sources/paper/paper.md", "lines": "1-40", "note": "abstract and method"}
                            ],
                            "review_status": "grounded",
                        }
                    ]
                ),
                encoding="utf-8",
            )
            conflict = root / "conflict.json"
            conflict.write_text(
                json.dumps(
                    [
                        {
                            "slug": "paper",
                            "modeling_card": "not_applicable",
                            "classification_evidence": [],
                            "related_work_evidence": [],
                            "review_status": "grounded",
                        }
                    ]
                ),
                encoding="utf-8",
            )
            duplicate = root / "duplicate.json"
            duplicate.write_text(grounded.read_text(encoding="utf-8"), encoding="utf-8")

            source_schema_manifest.merge_evidence(report, [grounded], repo_root=root)
            self.assertEqual(report["entries"][0]["review_status"], "grounded")
            self.assertTrue(report["entries"][0]["classification_evidence"])
            self.assertEqual(report["evidence_conflicts"], [])

            source_schema_manifest.merge_evidence(report, [duplicate], repo_root=root)
            self.assertIn(
                "duplicate evidence row",
                "\n".join(item["reason"] for item in report["evidence_conflicts"]),
            )

            source_schema_manifest.merge_evidence(report, [conflict], repo_root=root)
            self.assertTrue(report["evidence_conflicts"])

    def test_rejects_evidence_outside_resolved_parse_or_invalid_line_ranges(self):
        report = {
            "entries": [
                {
                    "slug": "paper",
                    "modeling_card": "not_applicable",
                    "parses": [{"path": "raw/sources/paper/paper.md"}],
                    "classification_evidence": [],
                    "related_work_evidence": [],
                    "review_status": "classified",
                }
            ],
            "evidence_conflicts": [],
        }
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            parse = root / "raw" / "sources" / "paper" / "paper.md"
            parse.parent.mkdir(parents=True)
            parse.write_text("one\ntwo\nthree\n", encoding="utf-8")
            sidecar = root / "invalid.json"
            sidecar.write_text(
                json.dumps(
                    [
                        {
                            "slug": "paper",
                            "modeling_card": "not_applicable",
                            "classification_evidence": [
                                {
                                    "path": "raw/sources/other/other.md",
                                    "lines": "1-2",
                                    "note": "wrong parse",
                                }
                            ],
                            "related_work_evidence": [
                                {
                                    "path": "raw/sources/paper/paper.md",
                                    "lines": "2-9",
                                    "note": "past end of parse",
                                }
                            ],
                            "review_status": "grounded",
                        }
                    ]
                ),
                encoding="utf-8",
            )

            source_schema_manifest.merge_evidence(report, [sidecar], repo_root=root)

            reasons = "\n".join(item["reason"] for item in report["evidence_conflicts"])
            self.assertIn("resolved raw parse", reasons)
            self.assertIn("outside parse bounds", reasons)
            self.assertEqual(report["entries"][0]["review_status"], "classified")


if __name__ == "__main__":
    unittest.main()
