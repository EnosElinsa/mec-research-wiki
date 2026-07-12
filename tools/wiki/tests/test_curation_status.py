from __future__ import annotations

import pathlib
import sys
import tempfile
import unittest
from unittest import mock


TOOLS_DIR = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS_DIR))

import curation_status  # noqa: E402
import wikilib  # noqa: E402


class CurationStatusTests(unittest.TestCase):
    def test_parse_discovery_falls_back_to_title_named_markdown(self):
        with tempfile.TemporaryDirectory() as tmp:
            raw = pathlib.Path(tmp) / "raw"
            folder = raw / "Paper_Title"
            folder.mkdir(parents=True)
            parse = folder / "Paper_Title.md"
            parse.write_text("# Paper Title\n", encoding="utf-8")

            with mock.patch.object(wikilib, "raw_sources_dir", return_value=str(raw)):
                self.assertEqual(curation_status._full_md("Paper_Title"), str(parse))

    def test_classify_uses_title_match_when_recorded_raw_path_is_stale(self):
        title = "Cargo UAVs Pick-Up Systems for Low-Altitude Economy"
        with tempfile.TemporaryDirectory() as tmp:
            raw = pathlib.Path(tmp) / "raw"
            folder = raw / "Cargo_UAVs_Pick-Up_Systems"
            folder.mkdir(parents=True)
            (folder / "Cargo_UAVs_Pick-Up_Systems.md").write_text(
                f"# {title}\n", encoding="utf-8"
            )

            with (
                mock.patch.object(wikilib, "raw_sources_dir", return_value=str(raw)),
                mock.patch.object(
                    wikilib,
                    "referenced_raw_folders",
                    return_value={"Cargo UAVs Pick-Up Systems"},
                ),
                mock.patch.object(
                    wikilib,
                    "curated_title_keys",
                    return_value={wikilib.title_match_key(title): "chen-2026-cargo-uav"},
                ),
            ):
                raw_folders, curated, uncurated, orphan_refs = curation_status.classify()

            self.assertEqual(raw_folders, ["Cargo_UAVs_Pick-Up_Systems"])
            self.assertEqual(curated, ["Cargo_UAVs_Pick-Up_Systems"])
            self.assertEqual(uncurated, [])
            self.assertEqual(orphan_refs, ["Cargo UAVs Pick-Up Systems"])

    def test_duplicate_detection_reads_title_named_markdown(self):
        text = "# Same Paper\n\nIdentical parse body.\n"
        with tempfile.TemporaryDirectory() as tmp:
            raw = pathlib.Path(tmp) / "raw"
            for name in ("Original", "Duplicate"):
                folder = raw / name
                folder.mkdir(parents=True)
                (folder / f"{name}.md").write_text(text, encoding="utf-8")

            with mock.patch.object(wikilib, "raw_sources_dir", return_value=str(raw)):
                duplicates = curation_status.detect_duplicates(["Duplicate"], ["Original"])

            self.assertEqual(
                duplicates,
                {
                    "Duplicate": {
                        "match": "Original",
                        "kind": "identical",
                        "ratio": 1.0,
                    }
                },
            )

    def test_near_duplicate_scan_skips_bodies_for_unrelated_titles(self):
        with tempfile.TemporaryDirectory() as tmp:
            raw = pathlib.Path(tmp) / "raw"
            curated = []
            for index in range(20):
                name = f"Unrelated_{index}"
                curated.append(name)
                folder = raw / name
                folder.mkdir(parents=True)
                (folder / f"{name}.md").write_text(
                    f"# Distinct Topic {index}\n\n{'x' * 1000}{index}\n",
                    encoding="utf-8",
                )

            candidate = raw / "Candidate"
            candidate.mkdir(parents=True)
            (candidate / "Candidate.md").write_text(
                f"# Completely Different Research\n\n{'y' * 1000}\n",
                encoding="utf-8",
            )

            real_matcher = curation_status.difflib.SequenceMatcher

            def guarded_matcher(*args, **kwargs):
                left, right = args[-2:]
                if len(left) > 200 or len(right) > 200:
                    raise AssertionError("unrelated parse bodies were compared")
                return real_matcher(*args, **kwargs)

            with (
                mock.patch.object(wikilib, "raw_sources_dir", return_value=str(raw)),
                mock.patch.object(
                    curation_status.difflib,
                    "SequenceMatcher",
                    side_effect=guarded_matcher,
                ),
            ):
                duplicates = curation_status.detect_duplicates(
                    ["Candidate"], curated
                )

            self.assertEqual(duplicates, {})

    def test_near_duplicate_scan_still_checks_similar_titles(self):
        with tempfile.TemporaryDirectory() as tmp:
            raw = pathlib.Path(tmp) / "raw"
            original = raw / "Original"
            duplicate = raw / "Duplicate"
            original.mkdir(parents=True)
            duplicate.mkdir(parents=True)
            body = "A" * 1000
            (original / "Original.md").write_text(
                f"# UAV Relay-Assisted Communications\n\n{body}\n",
                encoding="utf-8",
            )
            (duplicate / "Duplicate.md").write_text(
                f"# UAV Relay Assisted Communication\n\n{body}B\n",
                encoding="utf-8",
            )

            with mock.patch.object(wikilib, "raw_sources_dir", return_value=str(raw)):
                duplicates = curation_status.detect_duplicates(
                    ["Duplicate"], ["Original"], near_ratio=0.97
                )

            self.assertEqual(duplicates["Duplicate"]["match"], "Original")
            self.assertEqual(duplicates["Duplicate"]["kind"], "near")


if __name__ == "__main__":
    unittest.main()
