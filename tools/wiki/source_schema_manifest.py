#!/usr/bin/env python3
"""Build a no-silent-skip source-page to raw-parse migration manifest.

The report is scratch state for the conditional modeling-card migration.  It
retains every recorded Raw-artifacts reference, resolves stale ``full.md`` and
folder paths conservatively, and proves that every source page and raw Markdown
parse is represented.  It does not classify modeling applicability or generate
prose.
"""

from __future__ import annotations

import argparse
import datetime as dt
import glob
import hashlib
import json
import os
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path, PurePosixPath

import curation_status
import frontmatter_audit
import wikilib


RAW_HEADING_RE = re.compile(r"(?im)^##[ \t]+Raw artifacts[ \t]*$")
NEXT_H2_RE = re.compile(r"(?m)^##[ \t]+[^\r\n]+$")
CODE_SPAN_RE = re.compile(r"`([^`\r\n]+)`")
H1_RE = re.compile(r"(?m)^#[ \t]+([^\r\n]+?)[ \t]*$")
LINE_SEGMENT_RE = re.compile(r"^(\d+)(?:-(\d+))?$")


def _posix_relative(path: Path, root: Path) -> str:
    return path.resolve().relative_to(root.resolve()).as_posix()


def _raw_title(path: Path) -> str:
    match = H1_RE.search(path.read_text(encoding="utf-8", errors="replace")[:65536])
    return match.group(1).strip() if match else ""


def _frontmatter_title(text: str) -> str:
    fm = frontmatter_audit._front_matter(text)
    if fm is None:
        return ""
    value = frontmatter_audit._scalar(fm, "title") or ""
    return value.strip().strip("'\"").strip()


def _modeling_card(text: str) -> str | None:
    fm = frontmatter_audit._front_matter(text)
    if fm is None:
        return None
    value = frontmatter_audit._scalar(fm, "modeling_card")
    if value is None:
        return None
    normalized = value.strip().strip("'\"").strip()
    return normalized if normalized in {"required", "not_applicable"} else None


def _recorded_refs(text: str, repo_root: Path) -> tuple[list[dict], int | None]:
    heading = RAW_HEADING_RE.search(text)
    if not heading:
        return [], None
    following = NEXT_H2_RE.search(text, heading.end())
    end = following.start() if following else len(text)
    block = text[heading.end() : end]
    refs: list[dict] = []
    for match in CODE_SPAN_RE.finditer(block):
        value = match.group(1).strip().replace("\\", "/")
        if not value.startswith("raw/sources/"):
            continue
        absolute_start = heading.end() + match.start(1)
        line = text.count("\n", 0, absolute_start) + 1
        lowered = value.lower().rstrip("/")
        if lowered.endswith(".md"):
            kind = "parse"
        elif lowered.endswith(".pdf"):
            kind = "pdf"
        elif lowered.endswith("/images") or lowered.split("/")[-1] == "images":
            kind = "images"
        else:
            kind = "other"
        refs.append(
            {
                "path": value,
                "kind": kind,
                "exists": (repo_root / Path(*PurePosixPath(value).parts)).exists(),
                "line": line,
            }
        )
    return refs, text.count("\n", 0, heading.start()) + 1


def _parse_record(path: Path, raw_root: Path) -> dict:
    data = path.read_bytes()
    return {
        "path": _posix_relative(path, raw_root.parents[1]),
        "folder": path.parent.name,
        "raw_title": _raw_title(path),
        "sha256": hashlib.sha256(data).hexdigest(),
        "bytes": len(data),
    }


def build_manifest(
    *,
    wiki_sources: Path | str | None = None,
    raw_sources: Path | str | None = None,
    repo_root: Path | str | None = None,
) -> dict:
    root = Path(repo_root or wikilib.repo_root()).resolve()
    wiki_root = Path(wiki_sources or Path(wikilib.wiki_dir()) / "sources").resolve()
    raw_root = Path(raw_sources or wikilib.raw_sources_dir()).resolve()

    source_files = sorted(wiki_root.glob("*.md"))
    raw_folders = sorted(path for path in raw_root.iterdir() if path.is_dir())

    actual_records: dict[Path, dict] = {}
    raw_title_index: dict[str, list[Path]] = defaultdict(list)
    folder_key_index: dict[str, list[Path]] = defaultdict(list)
    folder_files: dict[str, list[Path]] = {}
    for folder in raw_folders:
        markdown = sorted(folder.glob("*.md"))
        folder_files[folder.name] = markdown
        for parse in markdown:
            record = _parse_record(parse, raw_root)
            actual_records[parse.resolve()] = record
            title_key = wikilib.title_match_key(record["raw_title"])
            if title_key:
                raw_title_index[title_key].append(parse.resolve())
            folder_key_index[wikilib.title_match_key(folder.name)].append(parse.resolve())

    entries: list[dict] = []
    unresolved: list[dict] = []
    ambiguous: list[dict] = []
    used_parses: set[Path] = set()
    resolution_counts: Counter[str] = Counter()
    total_recorded_refs = 0
    total_parse_refs = 0
    recorded_parse_paths_existing = 0

    for source_path in source_files:
        text = source_path.read_text(encoding="utf-8", errors="replace")
        slug = source_path.stem
        title = _frontmatter_title(text)
        refs, heading_line = _recorded_refs(text, root)
        total_recorded_refs += len(refs)
        parse_refs = [ref for ref in refs if ref["kind"] == "parse"]
        total_parse_refs += len(parse_refs)
        recorded_parse_paths_existing += sum(1 for ref in parse_refs if ref["exists"])

        resolved_for_page: dict[Path, dict] = {}
        entry_unresolved = False
        for ref in parse_refs:
            recorded = ref["path"]
            parts = PurePosixPath(recorded).parts
            if len(parts) < 4:
                unresolved.append({"slug": slug, "path": recorded, "reason": "malformed path"})
                entry_unresolved = True
                continue
            recorded_folder = parts[2]
            exact = (root / Path(*parts)).resolve()
            candidates: list[Path] = []
            resolution = ""

            if exact.is_file():
                candidates = [exact]
                resolution = "explicit_path"
            elif recorded_folder in folder_files and len(folder_files[recorded_folder]) == 1:
                candidates = [folder_files[recorded_folder][0].resolve()]
                resolution = "folder_exists_title_named_or_single_md"
            else:
                title_candidates = raw_title_index.get(wikilib.title_match_key(title), [])
                if len(title_candidates) == 1:
                    candidates = title_candidates
                    resolution = "raw_title_match"
                else:
                    folder_candidates = folder_key_index.get(
                        wikilib.title_match_key(recorded_folder), []
                    )
                    if len(folder_candidates) == 1:
                        candidates = folder_candidates
                        resolution = "recorded_folder_key_match"
                    elif title_candidates:
                        candidates = title_candidates

            if len(candidates) != 1:
                issue = {
                    "slug": slug,
                    "path": recorded,
                    "candidates": [
                        _posix_relative(candidate, root) for candidate in sorted(candidates)
                    ],
                }
                if candidates:
                    ambiguous.append(issue)
                else:
                    issue["reason"] = "no conservative resolution"
                    unresolved.append(issue)
                entry_unresolved = True
                continue

            parse_path = candidates[0].resolve()
            existing = resolved_for_page.get(parse_path)
            if existing:
                existing["recorded_paths"].append(recorded)
                continue
            resolved = dict(actual_records[parse_path])
            resolved["resolution"] = resolution
            resolved["recorded_paths"] = [recorded]
            resolved_for_page[parse_path] = resolved
            used_parses.add(parse_path)
            resolution_counts[resolution] += 1

        if not parse_refs:
            unresolved.append(
                {"slug": slug, "path": None, "reason": "missing Raw artifacts parse reference"}
            )
            entry_unresolved = True

        classification = _modeling_card(text)
        entries.append(
            {
                "slug": slug,
                "page_path": _posix_relative(source_path, root),
                "frontmatter_title": title,
                "raw_artifacts_heading_line": heading_line,
                "recorded_refs": refs,
                "parses": sorted(resolved_for_page.values(), key=lambda item: item["path"]),
                "modeling_card": classification,
                "classification_evidence": [],
                "related_work_evidence": [],
                "review_status": "classified" if classification else "pending",
                "status": "unresolved" if entry_unresolved else "resolved",
            }
        )

    actual_parse_paths = set(actual_records)
    orphan_paths = sorted(actual_parse_paths - used_parses)
    orphan_folders = sorted({path.parent.name for path in orphan_paths})

    counts = {
        "source_pages": len(source_files),
        "raw_folders": len(raw_folders),
        "raw_markdown_files": len(actual_records),
        "recorded_raw_refs": total_recorded_refs,
        "recorded_parse_refs": total_parse_refs,
        "recorded_parse_paths_existing": recorded_parse_paths_existing,
        "resolved_parse_paths": len(used_parses),
        "pages_with_multiple_parses": sum(
            1 for entry in entries if len(entry["parses"]) > 1
        ),
    }

    return {
        "report_type": "source-raw-manifest",
        "schema_version": 1,
        "generated_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "roots": {"wiki_sources": "wiki/sources", "raw_sources": "raw/sources"},
        "counts": counts,
        "resolution_counts": dict(sorted(resolution_counts.items())),
        "entries": entries,
        "orphan_raw_folders": orphan_folders,
        "unresolved_recorded_refs": unresolved,
        "ambiguous_resolutions": ambiguous,
        "evidence_files": [],
        "evidence_conflicts": [],
        "grounding_counts": {
            "grounded": sum(1 for entry in entries if entry["review_status"] == "grounded"),
            "classified": sum(1 for entry in entries if entry["review_status"] == "classified"),
            "pending": sum(1 for entry in entries if entry["review_status"] == "pending"),
        },
    }


def _evidence_errors(
    items: object,
    *,
    entry: dict,
    repo_root: Path,
    line_counts: dict[str, int],
) -> list[str]:
    """Validate that evidence points into this page's resolved raw parse."""
    if not isinstance(items, list) or not items:
        return ["evidence list is empty"]
    resolved_paths = {parse["path"] for parse in entry.get("parses", [])}
    errors: list[str] = []
    for index, item in enumerate(items, start=1):
        if not isinstance(item, dict):
            errors.append(f"evidence item {index} is not an object")
            continue
        evidence_path = item.get("path")
        line_spec = item.get("lines")
        note = item.get("note")
        if not isinstance(evidence_path, str) or evidence_path not in resolved_paths:
            errors.append(f"evidence item {index} does not reference a resolved raw parse")
            continue
        if not isinstance(note, str) or not note.strip():
            errors.append(f"evidence item {index} has an empty note")
        if not isinstance(line_spec, str) or not line_spec.strip():
            errors.append(f"evidence item {index} has an invalid line range")
            continue
        absolute = repo_root / Path(*PurePosixPath(evidence_path).parts)
        if evidence_path not in line_counts:
            if not absolute.is_file():
                errors.append(f"evidence item {index} raw parse does not exist")
                continue
            text = absolute.read_text(encoding="utf-8", errors="replace")
            line_counts[evidence_path] = text.count("\n") + 1
        line_count = line_counts[evidence_path]
        for segment in line_spec.split(","):
            match = LINE_SEGMENT_RE.fullmatch(segment.strip())
            if not match:
                errors.append(f"evidence item {index} has an invalid line range")
                continue
            start = int(match.group(1))
            end = int(match.group(2) or match.group(1))
            if start < 1 or end < start or end > line_count:
                errors.append(f"evidence item {index} line range is outside parse bounds")
    return errors


def merge_evidence(
    report: dict,
    evidence_paths: list[Path | str],
    *,
    repo_root: Path | str | None = None,
) -> None:
    """Merge non-overlapping grounding sidecars into an existing manifest."""
    root = Path(repo_root or wikilib.repo_root()).resolve()
    by_slug = {entry["slug"]: entry for entry in report["entries"]}
    conflicts = report.setdefault("evidence_conflicts", [])
    files = report.setdefault("evidence_files", [])
    line_counts: dict[str, int] = {}
    seen_slugs = {
        entry["slug"]
        for entry in report["entries"]
        if entry.get("classification_evidence") or entry.get("related_work_evidence")
    }
    for raw_path in evidence_paths:
        path = Path(raw_path).resolve()
        files.append(path.as_posix())
        payload = json.loads(path.read_text(encoding="utf-8"))
        rows = payload.get("entries", []) if isinstance(payload, dict) else payload
        if not isinstance(rows, list):
            conflicts.append({"path": path.as_posix(), "reason": "sidecar is not a row list"})
            continue
        for row in rows:
            slug = row.get("slug") if isinstance(row, dict) else None
            if not slug or slug not in by_slug:
                conflicts.append(
                    {"path": path.as_posix(), "slug": slug, "reason": "unknown source slug"}
                )
                continue
            entry = by_slug[slug]
            classification = row.get("modeling_card")
            if classification != entry.get("modeling_card"):
                conflicts.append(
                    {
                        "path": path.as_posix(),
                        "slug": slug,
                        "reason": "sidecar classification disagrees with source frontmatter",
                        "source": entry.get("modeling_card"),
                        "sidecar": classification,
                    }
                )
                continue
            if slug in seen_slugs:
                conflicts.append(
                    {
                        "path": path.as_posix(),
                        "slug": slug,
                        "reason": "duplicate evidence row for source slug",
                    }
                )
                continue
            classification_evidence = row.get("classification_evidence", [])
            related_evidence = row.get("related_work_evidence", [])
            if not classification_evidence or not related_evidence:
                conflicts.append(
                    {
                        "path": path.as_posix(),
                        "slug": slug,
                        "reason": "grounding sidecar lacks classification or Related Work evidence",
                    }
                )
                continue
            evidence_errors = _evidence_errors(
                classification_evidence,
                entry=entry,
                repo_root=root,
                line_counts=line_counts,
            ) + _evidence_errors(
                related_evidence,
                entry=entry,
                repo_root=root,
                line_counts=line_counts,
            )
            if row.get("review_status") != "grounded":
                evidence_errors.append("review_status must be grounded")
            if evidence_errors:
                conflicts.extend(
                    {"path": path.as_posix(), "slug": slug, "reason": reason}
                    for reason in evidence_errors
                )
                continue
            entry["classification_evidence"] = classification_evidence
            entry["related_work_evidence"] = related_evidence
            entry["review_status"] = "grounded"
            seen_slugs.add(slug)

    report["evidence_files"] = sorted(set(files))
    report["grounding_counts"] = {
        "grounded": sum(1 for entry in report["entries"] if entry["review_status"] == "grounded"),
        "classified": sum(1 for entry in report["entries"] if entry["review_status"] == "classified"),
        "pending": sum(1 for entry in report["entries"] if entry["review_status"] == "pending"),
    }


def _manifest_clean(report: dict, *, require_grounded: bool = False) -> bool:
    counts = report["counts"]
    return (
        not report["orphan_raw_folders"]
        and not report["unresolved_recorded_refs"]
        and not report["ambiguous_resolutions"]
        and not report.get("evidence_conflicts", [])
        and counts["source_pages"] == len(report["entries"])
        and counts["resolved_parse_paths"] == counts["raw_markdown_files"]
        and (not require_grounded or report["grounding_counts"]["grounded"] == counts["source_pages"])
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--json",
        default="source-modeling-cards-manifest.json",
        help="output report path (relative paths land in .curation-out/)",
    )
    parser.add_argument(
        "--evidence",
        action="append",
        default=[],
        help="grounding sidecar path or glob; repeat for multiple batches",
    )
    parser.add_argument(
        "--require-grounded",
        action="store_true",
        help="fail unless every source row has merged classification and Related Work evidence",
    )
    args = parser.parse_args(argv)

    report = build_manifest()
    evidence_paths: list[Path] = []
    for pattern in args.evidence:
        resolved_pattern = pattern
        if not os.path.isabs(resolved_pattern):
            resolved_pattern = os.path.join(wikilib.repo_root(), resolved_pattern)
        matches = [Path(path) for path in glob.glob(resolved_pattern)]
        if not matches:
            report["evidence_conflicts"].append(
                {"path": pattern, "reason": "evidence pattern matched no files"}
            )
        evidence_paths.extend(matches)
    if evidence_paths:
        merge_evidence(report, sorted(set(evidence_paths)), repo_root=wikilib.repo_root())
    output = args.json
    if not os.path.isabs(output):
        output = os.path.join(wikilib.scratch_dir(), output)
    os.makedirs(os.path.dirname(os.path.abspath(output)), exist_ok=True)
    with open(output, "w", encoding="utf-8") as handle:
        json.dump(report, handle, ensure_ascii=False, indent=2)

    counts = report["counts"]
    print("=" * 70)
    print(
        "SOURCE RAW MANIFEST: "
        f"{counts['source_pages']} pages -> {counts['resolved_parse_paths']} parses"
    )
    print("=" * 70)
    print(f"UNRESOLVED: {len(report['unresolved_recorded_refs'])}")
    print(f"AMBIGUOUS: {len(report['ambiguous_resolutions'])}")
    print(f"ORPHAN RAW FOLDERS: {len(report['orphan_raw_folders'])}")
    print(f"EVIDENCE CONFLICTS: {len(report['evidence_conflicts'])}")
    print(f"GROUNDED: {report['grounding_counts']['grounded']}/{counts['source_pages']}")
    print(f"Report written to {output}")
    return 0 if _manifest_clean(report, require_grounded=args.require_grounded) else 1


if __name__ == "__main__":
    sys.exit(main())
