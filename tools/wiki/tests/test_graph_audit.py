from __future__ import annotations

import contextlib
import copy
import io
import inspect
import json
import pathlib
import sys
import tempfile
import unittest
from unittest import mock


TOOLS_DIR = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS_DIR))

import graph_audit  # noqa: E402
import wikilib  # noqa: E402


CREATED = "2026-07-14"


class GraphAuditTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)
        self.root = pathlib.Path(self.temp_dir.name)
        self.wiki = self.root / "wiki"
        self.scratch = self.root / ".curation-out"
        self.scratch.mkdir()
        self._write_fixture()

    def _page(
        self,
        relative: str,
        *,
        page_type: str | None,
        created: str = CREATED,
        body: str = "",
    ) -> pathlib.Path:
        path = self.wiki / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        frontmatter = ""
        if page_type is not None:
            frontmatter = (
                "---\n"
                f"type: {page_type}\n"
                f"created: {created}\n"
                "---\n"
            )
        path.write_text(frontmatter + body, encoding="utf-8")
        return path

    def _write_fixture(self) -> None:
        self._page(
            "sources/a.md",
            page_type="source",
            body=(
                "[[concepts/b.md|Bee]] [[b]] [[a#self]] [[old]] [[index]] "
                "[[raw-only]]\n"
                "```markdown\n"
                "[[fenced-example]]\n"
                "```\n"
                "~~~text\n"
                "[[fenced-example]]\n"
                "~~~\n"
                "``[[fenced-example]]``\n"
                "> > - ~~~~text\n"
                "> >   [[fenced-example]]\n"
                "> >   ~~~\n"
                "> >   [[fenced-example]]\n"
                "> >   ~~~~\n"
                "- ```python\n"
                "  [[fenced-example]]\n"
                "  ````\n"
                "-\t~~~\n"
                "\t[[fenced-example]]\n"
                "\t~~~\n"
                "- list item\n"
                "  ```python\n"
                "  [[fenced-example]]\n"
                "  ```\n"
                "- - ~~~~\n"
                "    [[fenced-example]]\n"
                "    ~~~\n"
                "    [[fenced-example]]\n"
                "    ~~~~\n"
                "- > ````python\n"
                "  > [[fenced-example]]\n"
                "  > ```\n"
                "  > [[fenced-example]]\n"
                "  > ````\n"
                "- - nested list\n"
                "    continuation\n"
                "  ~~~\n"
                "  [[fenced-example]]\n"
                "[[old]]\n"
                "- unterminated list fence\n"
                "  ~~~\n"
                "  [[fenced-example]]\n"
                "[[old]]\n"
                "> > ~~~\n"
                "> > [[fenced-example]]\n"
                "[[old]]\n"
            ),
        )
        self._page(
            "concepts/b.md",
            page_type="concept",
            body="[[sources\\a#back]] [[c]] [[overview]]\n",
        )
        self._page(
            "findings/c.md",
            page_type="finding",
            body="[[concepts/b.md]] [[log]]\n",
        )
        self._page("entities/d.md", page_type="entity", body="[[index]]\n")
        self._page(
            "concepts/old.md",
            page_type="concept",
            created="2026-07-13",
            body="[[a]] [[index]]\n",
        )
        self._page(
            "concepts/fenced-example.md",
            page_type="concept",
            created="2026-07-13",
        )
        self._page(
            "index.md",
            page_type=None,
            body="[[a]] [[b]] [[c]] [[d]] [[old]]\n",
        )
        self._page("log.md", page_type=None, body="[[a]] [[d]]\n")
        self._page("overview.md", page_type=None, body="[[b]] [[c]]\n")
        raw = self.root / "raw"
        raw.mkdir()
        (raw / "raw-only.md").write_text("[[a]]\n", encoding="utf-8")

    def _pages(self) -> dict[str, str]:
        return wikilib.wiki_page_index(str(self.wiki))

    def _snapshot(self) -> dict:
        return graph_audit.build_snapshot(
            self._pages(),
            created=CREATED,
            label="fixture",
            weak_degree=1,
            exclusions=graph_audit.DEFAULT_EXCLUSIONS,
            observed_ui_pages=8,
            observed_ui_cohesion=0.25,
        )

    def test_wiki_edges_are_wiki_only_and_simple(self):
        pages = self._pages()
        self.assertIs(
            inspect.signature(graph_audit.select_created_members)
            .parameters["exclusions"]
            .default,
            inspect.Parameter.empty,
        )
        self.assertIs(
            inspect.signature(graph_audit.graph_payload)
            .parameters["weak_degree"]
            .default,
            inspect.Parameter.empty,
        )

        self.assertEqual(
            wikilib.wiki_undirected_edges(
                pages, excluded=graph_audit.DEFAULT_EXCLUSIONS
            ),
            {("a", "b"), ("a", "old"), ("b", "c")},
        )

    def test_snapshot_has_expected_metrics_and_separate_ui_observation(self):
        snapshot = self._snapshot()

        self.assertEqual(snapshot["report_type"], "snapshot")
        self.assertIn("generated_at_utc", snapshot)
        self.assertIn("graph_semantics", snapshot)
        self.assertEqual(snapshot["external_observation"], {
            "source": "LLM Wiki UI",
            "pages": 8,
            "cohesion": 0.25,
        })
        self.assertEqual(snapshot["cohort"]["members"], ["a", "b", "c", "d"])
        self.assertEqual(snapshot["cohort"]["member_count"], 4)
        self.assertEqual(snapshot["cohort"]["member_hash_algorithm"], "sha256-canonical-json")
        self.assertEqual(len(snapshot["cohort"]["member_hash"]), 64)
        self.assertEqual(snapshot["cohort"]["member_types"], {
            "a": "source",
            "b": "concept",
            "c": "finding",
            "d": "entity",
        })
        self.assertEqual(snapshot["graph"]["metrics"], {
            "induced_edge_count": 2,
            "possible_edge_count": 6,
            "local_cohesion": 1 / 3,
            "component_count": 2,
            "largest_component_size": 3,
            "isolate_count": 1,
            "weak_member_count": 3,
            "bridge_edge_count": 2,
        })
        self.assertEqual(snapshot["graph"]["external_degrees"]["a"], 1)
        self.assertEqual(
            [row["slug"] for row in snapshot["graph"]["weak_members"]],
            ["a", "c", "d"],
        )
        self.assertNotIn("weak_rows", snapshot["graph"])
        self.assertNotIn("pages", snapshot["graph"]["metrics"])
        graph_audit.validate_snapshot(payload=snapshot)

    def test_comparison_freezes_members_and_reports_deltas(self):
        baseline = self._snapshot()
        self._page(
            "sources/a.md",
            page_type="source",
            body="[[b]] [[c]] [[old]]\n",
        )
        self._page("concepts/b.md", page_type="concept", body="[[a]]\n")
        self._page("findings/c.md", page_type="finding", body="[[a]] [[d]]\n")
        self._page("entities/d.md", page_type="entity", body="[[c]]\n")
        self._page("concepts/e.md", page_type="concept", body="[[index]]\n")

        comparison = graph_audit.build_comparison(
            baseline,
            self._pages(),
            baseline_path=".curation-out/baseline.json",
        )

        self.assertEqual(comparison["cohort"]["members"], ["a", "b", "c", "d"])
        self.assertNotIn("e", comparison["cohort"]["members"])
        self.assertEqual(comparison["report_type"], "comparison")
        self.assertEqual(comparison["comparison"]["added_edges"], [["a", "c"], ["c", "d"]])
        self.assertEqual(comparison["comparison"]["removed_edges"], [["b", "c"]])
        self.assertEqual(comparison["comparison"]["metric_deltas"]["induced_edge_count"], 1)
        self.assertEqual(comparison["comparison"]["metric_deltas"]["component_count"], -1)
        self.assertEqual(comparison["comparison"]["metric_deltas"]["isolate_count"], -1)
        self.assertEqual(comparison["comparison"]["metric_deltas"]["weak_member_count"], -1)
        self.assertEqual(comparison["comparison"]["internal_degree_deltas"], {
            "a": 1,
            "b": -1,
            "c": 1,
            "d": 1,
        })

    def test_comparison_rejects_missing_frozen_member(self):
        baseline = self._snapshot()
        (self.wiki / "entities/d.md").unlink()

        with self.assertRaisesRegex(
            graph_audit.GraphAuditError, r"missing frozen member\(s\): d"
        ):
            graph_audit.build_comparison(
                baseline, self._pages(), baseline_path="baseline.json"
            )

    def test_page_index_rejects_duplicate_basename(self):
        self._page(
            "comparisons/a.md",
            page_type="comparison",
            created="2026-07-13",
        )

        with self.assertRaisesRegex(ValueError, "duplicate wiki page basename.*a"):
            wikilib.wiki_page_index(str(self.wiki))

    def test_snapshot_validation_rejects_corrupt_hash(self):
        snapshot = self._snapshot()
        snapshot["cohort"]["member_hash"] = "0" * 64

        with self.assertRaisesRegex(graph_audit.GraphAuditError, "cohort hash mismatch"):
            graph_audit.validate_snapshot(snapshot)

        with self.subTest(case="empty semantics"):
            malformed = self._snapshot()
            malformed["graph_semantics"] = {}
            with self.assertRaisesRegex(graph_audit.GraphAuditError, "semantics"):
                graph_audit.validate_snapshot(malformed)

        with self.subTest(case="missing UI observation"):
            malformed = self._snapshot()
            del malformed["external_observation"]
            with self.assertRaisesRegex(
                graph_audit.GraphAuditError, "external UI observation"
            ):
                graph_audit.validate_snapshot(malformed)

        with self.subTest(case="invalid timestamp"):
            malformed = self._snapshot()
            malformed["generated_at_utc"] = "not-a-timestamp"
            with self.assertRaisesRegex(graph_audit.GraphAuditError, "timestamp"):
                graph_audit.validate_snapshot(malformed)

        for field, value in (
            ("isolate_count", True),
            ("largest_component_size", 3.0),
        ):
            with self.subTest(case=f"non-integer {field}"):
                malformed = self._snapshot()
                malformed["graph"]["metrics"][field] = value
                with self.assertRaisesRegex(
                    graph_audit.GraphAuditError, "integer metric"
                ):
                    graph_audit.validate_snapshot(malformed)

        with self.subTest(case="extra metric"):
            malformed = self._snapshot()
            malformed["graph"]["metrics"]["unexpected"] = 0
            with self.assertRaisesRegex(graph_audit.GraphAuditError, "metric"):
                graph_audit.validate_snapshot(malformed)

        for field, mutate, message in (
            (
                "internal degree",
                lambda graph: graph["internal_degrees"].__setitem__("a", True),
                "internal degree",
            ),
            (
                "component size",
                lambda graph: graph["components"][0].__setitem__("size", 3.0),
                "component",
            ),
            (
                "weak member degree",
                lambda graph: graph["weak_members"][0].__setitem__(
                    "internal_degree", True
                ),
                "weak member",
            ),
        ):
            with self.subTest(case=f"non-integer {field}"):
                malformed = self._snapshot()
                mutate(malformed["graph"])
                with self.assertRaisesRegex(graph_audit.GraphAuditError, message):
                    graph_audit.validate_snapshot(malformed)

        for timestamp in (
            "2026-07-14",
            "2026-07-14T00:00:00",
            "2026-07-14T08:00:00+08:00",
        ):
            with self.subTest(case=f"non-UTC {timestamp}"):
                malformed = self._snapshot()
                malformed["generated_at_utc"] = timestamp
                with self.assertRaisesRegex(graph_audit.GraphAuditError, "UTC"):
                    graph_audit.validate_snapshot(malformed)

    def test_ledger_refresh_preserves_editorial_fields_and_updates_graph(self):
        baseline = self._snapshot()
        ledger = graph_audit.build_coverage_ledger(baseline)
        ledger["entries"][0]["theme"] = "air-ground scheduling"
        ledger["entries"][0]["status"] = "accepted"
        ledger["entries"][0]["evidence_paths"] = ["source note"]
        self._page(
            "sources/a.md",
            page_type="source",
            body="[[b]] [[c]] [[old]]\n",
        )
        self._page(
            "findings/c.md",
            page_type="finding",
            body="[[b]] [[a]] [[log]]\n",
        )
        comparison = graph_audit.build_comparison(
            baseline, self._pages(), baseline_path="baseline.json"
        )

        refreshed = graph_audit.refresh_coverage_ledger(
            ledger, comparison=comparison
        )
        rows = {row["slug"]: row for row in refreshed["entries"]}

        self.assertEqual(rows["d"]["post_batch_component"], 2)
        self.assertEqual(rows["d"]["post_batch_internal_degree"], 0)
        self.assertEqual(rows["a"]["post_batch_internal_degree"], 2)
        self.assertEqual(rows["c"]["post_batch_internal_degree"], 2)
        self.assertEqual(rows["a"]["theme"], "air-ground scheduling")
        self.assertEqual(rows["a"]["status"], "accepted")
        self.assertEqual(rows["a"]["evidence_paths"], ["source note"])

        malformed = graph_audit.build_coverage_ledger(baseline)
        del malformed["entries"][0]["status"]
        with self.assertRaisesRegex(
            graph_audit.GraphAuditError, "coverage ledger member row"
        ):
            graph_audit.refresh_coverage_ledger(malformed, comparison)

        malformed_comparison = copy.deepcopy(comparison)
        malformed_comparison["generated_at_utc"] = "2026-07-14T08:00:00+08:00"
        with self.assertRaisesRegex(graph_audit.GraphAuditError, "UTC"):
            graph_audit.refresh_coverage_ledger(
                ledger, comparison=malformed_comparison
            )

    def test_cli_writes_relative_snapshot_and_pending_ledger_to_scratch(self):
        def run_cli(argv):
            output = io.StringIO()
            errors = io.StringIO()
            with (
                contextlib.redirect_stdout(output),
                contextlib.redirect_stderr(errors),
            ):
                status = graph_audit.main(argv)
            return status, output.getvalue(), errors.getvalue()

        snapshot_args = [
            "snapshot",
            "--created", CREATED,
            "--label", "fixture",
            "--weak-degree", "1",
            "--observed-ui-pages", "8",
            "--observed-ui-cohesion", "0.25",
        ]
        with (
            mock.patch.object(wikilib, "wiki_dir", return_value=str(self.wiki)),
            mock.patch.object(wikilib, "repo_root", return_value=str(self.root)),
            mock.patch.object(wikilib, "scratch_dir", return_value=str(self.scratch)),
        ):
            status, output, _ = run_cli(snapshot_args + [
                "--json", "baseline.json",
                "--ledger", "ledger.json",
            ])
            self.assertEqual(status, 0)
            snapshot_path = self.scratch / "baseline.json"
            ledger_path = self.scratch / "ledger.json"
            self.assertTrue(snapshot_path.is_file())
            self.assertTrue(ledger_path.is_file())
            baseline_bytes = snapshot_path.read_bytes()
            ledger_bytes = ledger_path.read_bytes()
            snapshot = json.loads(baseline_bytes)
            ledger = json.loads(ledger_bytes)
            self.assertEqual(snapshot["cohort"]["member_count"], 4)
            self.assertTrue(
                all(row["status"] == "pending" for row in ledger["entries"])
            )
            self.assertIn("members=4", output)

            outside_output = self.root / "outside.json"
            status, _, errors = run_cli(
                snapshot_args + ["--json", "../outside.json"]
            )
            self.assertEqual(status, 2)
            self.assertIn("escapes", errors)
            self.assertFalse(outside_output.exists())

            alias = self.scratch / "alias"
            alias.mkdir()
            snapshot_collision = self.scratch / "snapshot-collision.json"
            snapshot_collision.write_bytes(b"unchanged snapshot collision")
            collision_before = snapshot_collision.read_bytes()
            status, _, errors = run_cli(snapshot_args + [
                "--json", "snapshot-collision.json",
                "--ledger", "alias/../snapshot-collision.json",
            ])
            self.assertEqual(status, 2)
            self.assertIn("collision", errors)
            self.assertEqual(snapshot_collision.read_bytes(), collision_before)

            extended_alias = pathlib.Path("\\\\?\\" + str(snapshot_collision))
            status, _, errors = run_cli(snapshot_args + [
                "--json", str(snapshot_collision),
                "--ledger", str(extended_alias),
            ])
            self.assertEqual(status, 2)
            self.assertIn("collision", errors)
            self.assertEqual(snapshot_collision.read_bytes(), collision_before)

            stream_collision = self.scratch / "snapshot-stream.json"
            status, _, errors = run_cli(snapshot_args + [
                "--json", str(stream_collision),
                "--ledger", f"{stream_collision}::$DATA",
            ])
            self.assertEqual(status, 2)
            self.assertIn("collision", errors)
            self.assertFalse(stream_collision.exists())

            trailing_collision = self.scratch / "snapshot-trailing.json"
            trailing_collision.write_bytes(b"unchanged trailing collision")
            trailing_before = trailing_collision.read_bytes()
            status, _, errors = run_cli(snapshot_args + [
                "--json", str(trailing_collision),
                "--ledger", f"{trailing_collision}.",
            ])
            self.assertEqual(status, 2)
            self.assertIn("collision", errors)
            self.assertEqual(trailing_collision.read_bytes(), trailing_before)

            compare_baseline = self.scratch / "compare-baseline.json"
            compare_baseline.write_bytes(baseline_bytes)
            compare_before = compare_baseline.read_bytes()
            status, _, errors = run_cli([
                "compare",
                "--baseline", ".curation-out/compare-baseline.json",
                "--json", "alias/../compare-baseline.json",
            ])
            compare_after = compare_baseline.read_bytes()
            self.assertEqual(status, 2)
            self.assertIn("collision", errors)
            self.assertEqual(compare_after, compare_before)

            baseline_ledger = self.scratch / "baseline-ledger.json"
            baseline_ledger.write_bytes(baseline_bytes)
            status, _, errors = run_cli([
                "compare",
                "--baseline", ".curation-out/baseline-ledger.json",
                "--json", "baseline-ledger-after.json",
                "--ledger", ".curation-out/alias/../baseline-ledger.json",
            ])
            self.assertEqual(status, 2)
            self.assertIn("collision", errors)
            self.assertEqual(baseline_ledger.read_bytes(), baseline_bytes)

            output_ledger = self.scratch / "output-ledger.json"
            output_ledger.write_bytes(ledger_bytes)
            status, _, errors = run_cli([
                "compare",
                "--baseline", ".curation-out/baseline.json",
                "--json", "alias/../output-ledger.json",
                "--ledger", ".curation-out/output-ledger.json",
            ])
            self.assertEqual(status, 2)
            self.assertIn("collision", errors)
            self.assertEqual(output_ledger.read_bytes(), ledger_bytes)

            outside_baseline = self.root.parent / f"{self.root.name}-baseline.json"
            outside_baseline.write_bytes(baseline_bytes)
            self.addCleanup(outside_baseline.unlink, missing_ok=True)
            status, _, errors = run_cli([
                "compare",
                "--baseline", f"../{outside_baseline.name}",
                "--json", "input-escape-after.json",
            ])
            self.assertEqual(status, 2)
            self.assertIn("escapes", errors)
            self.assertFalse((self.scratch / "input-escape-after.json").exists())

            outside_ledger = self.root.parent / f"{self.root.name}-ledger.json"
            outside_ledger.write_bytes(ledger_bytes)
            outside_ledger_before = outside_ledger.read_bytes()
            self.addCleanup(outside_ledger.unlink, missing_ok=True)
            status, _, errors = run_cli([
                "compare",
                "--baseline", ".curation-out/baseline.json",
                "--json", "ledger-escape-after.json",
                "--ledger", f"../{outside_ledger.name}",
            ])
            self.assertEqual(status, 2)
            self.assertIn("escapes", errors)
            self.assertFalse((self.scratch / "ledger-escape-after.json").exists())
            self.assertEqual(outside_ledger.read_bytes(), outside_ledger_before)

            self._page(
                "findings/c.md",
                page_type="finding",
                body="[[log]]\n",
            )
            self._page(
                "concepts/b.md",
                page_type="concept",
                body="[[sources\\a#back]] [[overview]]\n",
            )
            status, _, errors = run_cli([
                "compare",
                "--baseline", ".curation-out/baseline.json",
                "--json", "regression.json",
                "--ledger", ".curation-out/ledger.json",
            ])
            self.assertEqual(status, 0, errors)
            regression = json.loads(
                (self.scratch / "regression.json").read_text(encoding="utf-8")
            )
            self.assertLess(
                regression["comparison"]["metric_deltas"]["induced_edge_count"],
                0,
            )


if __name__ == "__main__":
    unittest.main()
