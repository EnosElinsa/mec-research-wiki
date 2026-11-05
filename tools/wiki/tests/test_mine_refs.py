from __future__ import annotations

import pathlib
import sys
import tempfile
import unittest
from unittest import mock

TOOLS_DIR = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS_DIR))

import mine_refs  # noqa: E402
import wikilib  # noqa: E402


PARSE_WITH_REFERENCES = (
    "# A Paper Title\n\nBody text.\n\n# REFERENCES\n\n"
    '[1] A. Author and B. Writer, "Joint offloading and trajectory design for '
    'UAV-enabled mobile edge computing," IEEE Trans. Wireless Commun., vol. 20, '
    "no. 3, pp. 1-14, Mar. 2021.\n"
    '[2] C. Coder, "Deep reinforcement learning for task offloading in mobile '
    'edge computing networks," IEEE Trans. Mobile Comput., vol. 22, no. 1, '
    "pp. 15-30, Jan. 2023.\n"
)


def _write(folder: pathlib.Path, name: str, text: str = "# Title\n") -> pathlib.Path:
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / name
    path.write_text(text, encoding="utf-8")
    return path


class RawParsePathTests(unittest.TestCase):
    def test_resolves_legacy_title_named_and_citekey_parses(self):
        with tempfile.TemporaryDirectory() as tmp:
            raw = pathlib.Path(tmp) / "raw"
            legacy = _write(raw / "Legacy_Paper", "full.md")
            _write(raw / "Legacy_Paper", "Legacy_Paper.md")
            titled = _write(raw / "Title_Named_Paper", "Title_Named_Paper.md")
            citekey = _write(raw / "Attention Learn to Solve Routing Problems", "kool2019iclr.md")
            (citekey.parent / "kool2019iclr.bib").write_text("@inproceedings{}", encoding="utf-8")
            with mock.patch.object(wikilib, "raw_sources_dir", return_value=str(raw)):
                self.assertEqual(wikilib.raw_parse_path("Legacy_Paper"), str(legacy))
                self.assertEqual(wikilib.raw_parse_path("Title_Named_Paper"), str(titled))
                self.assertEqual(
                    wikilib.raw_parse_path("Attention Learn to Solve Routing Problems"),
                    str(citekey),
                )

    def test_returns_none_for_missing_or_ambiguous_parse(self):
        with tempfile.TemporaryDirectory() as tmp:
            raw = pathlib.Path(tmp) / "raw"
            (raw / "Empty_Folder").mkdir(parents=True)
            _write(raw / "Two_Parses", "a.md")
            _write(raw / "Two_Parses", "b.md")
            with mock.patch.object(wikilib, "raw_sources_dir", return_value=str(raw)):
                self.assertIsNone(wikilib.raw_parse_path("Empty_Folder"))
                self.assertIsNone(wikilib.raw_parse_path("Two_Parses"))


class MineAllTests(unittest.TestCase):
    def test_mines_title_named_and_citekey_parses_and_reports_ambiguous_folders(self):
        with tempfile.TemporaryDirectory() as tmp:
            raw = pathlib.Path(tmp) / "raw"
            _write(raw / "Title_Named_Paper", "Title_Named_Paper.md", PARSE_WITH_REFERENCES)
            _write(raw / "Citekey_Paper", "kool2019iclr.md", PARSE_WITH_REFERENCES)
            _write(raw / "Two_Parses", "a.md", PARSE_WITH_REFERENCES)
            _write(raw / "Two_Parses", "b.md", PARSE_WITH_REFERENCES)
            with mock.patch.object(wikilib, "raw_sources_dir", return_value=str(raw)):
                per_folder, skipped = mine_refs.mine_all()

        self.assertEqual(sorted(per_folder), ["Citekey_Paper", "Title_Named_Paper"])
        for refs in per_folder.values():
            self.assertEqual(len(refs), 2)
            self.assertEqual(refs[0]["year"], "2021")
        self.assertEqual(skipped, [("Two_Parses", "no single Markdown parse")])


if __name__ == "__main__":
    unittest.main()
