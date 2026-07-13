from __future__ import annotations

import contextlib
import io
import pathlib
import sys
import tempfile
import unittest


TOOLS_DIR = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS_DIR))

import make_batches  # noqa: E402


class MakeBatchesTests(unittest.TestCase):
    def test_batch_prints_only_selected_allowlist(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = pathlib.Path(tmp) / "papers.txt"
            source.write_text("one\ntwo\nthree\nfour\nfive\n", encoding="utf-8")
            output = io.StringIO()

            with contextlib.redirect_stdout(output):
                result = make_batches.main(
                    ["--size", "2", "--input", str(source), "--batch", "2"]
                )

            self.assertEqual(result, 0)
            rendered = output.getvalue()
            self.assertIn("=== BATCH 2 (2) ===", rendered)
            self.assertIn("  - three", rendered)
            self.assertIn("  - four", rendered)
            self.assertNotIn("=== BATCH 1", rendered)
            self.assertNotIn("  - five", rendered)

    def test_batch_rejects_out_of_range_number(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = pathlib.Path(tmp) / "papers.txt"
            source.write_text("one\ntwo\n", encoding="utf-8")
            errors = io.StringIO()

            with contextlib.redirect_stderr(errors):
                with self.assertRaises(SystemExit) as raised:
                    make_batches.main(
                        ["--size", "2", "--input", str(source), "--batch", "2"]
                    )

            self.assertEqual(raised.exception.code, 2)
            self.assertIn("--batch must be between 1 and 1", errors.getvalue())


if __name__ == "__main__":
    unittest.main()
