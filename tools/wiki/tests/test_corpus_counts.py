from __future__ import annotations

import pathlib
import sys
import tempfile
import unittest
from unittest import mock


TOOLS_DIR = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS_DIR))

import corpus_counts  # noqa: E402
import wikilib  # noqa: E402


class CorpusCountsTests(unittest.TestCase):
    def test_update_overview_replaces_inventory_counts_only(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            entities = root / "entities"
            entities.mkdir()
            (entities / "author.md").write_text(
                "---\ntype: entity\ntags: [author]\n---\n", encoding="utf-8"
            )
            (entities / "tool.md").write_text(
                "---\ntype: entity\ntags: [tool]\n---\n", encoding="utf-8"
            )
            overview = root / "overview.md"
            overview.write_text(
                "- **Curated sources:** 1 - catalogue\n"
                "- **Concepts:** 2 across topics\n"
                "- **Entities:** 1 author pages + 0 tool pages (1 entity pages total).\n",
                encoding="utf-8",
            )

            with mock.patch.object(wikilib, "wiki_dir", return_value=str(root)):
                corpus_counts.update_overview(
                    str(overview), {"sources": 494, "concepts": 458, "entities": 2}
                )

            self.assertEqual(
                overview.read_text(encoding="utf-8"),
                "- **Curated sources:** 494 - catalogue\n"
                "- **Concepts:** 458 across topics\n"
                "- **Entities:** 1 author pages + 1 tool pages (2 entity pages total).\n",
            )


if __name__ == "__main__":
    unittest.main()
