#!/usr/bin/env python3
"""Audit repeated IEEE-style numeric citations in a Markdown Introduction."""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys
from collections import defaultdict
from typing import Any


HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
INTRODUCTION_RE = re.compile(r"(?:\bintroduction\b|引言)", re.IGNORECASE)
CITATION_RE = re.compile(r"\[(\d+)\](?:\s*[–—-]\s*\[(\d+)\])?")


def _introduction_bounds(lines: list[str]) -> tuple[int, int]:
    start = None
    level = None
    for index, line in enumerate(lines):
        match = HEADING_RE.match(line)
        if match and INTRODUCTION_RE.search(match.group(2)):
            start = index + 1
            level = len(match.group(1))
            break

    if start is None or level is None:
        raise ValueError("Introduction section not found")

    end = len(lines)
    for index in range(start, len(lines)):
        match = HEADING_RE.match(lines[index])
        if match and len(match.group(1)) <= level:
            end = index
            break
    return start, end


def _citation_numbers(line: str) -> list[int]:
    numbers: list[int] = []
    for match in CITATION_RE.finditer(line):
        first = int(match.group(1))
        last = int(match.group(2)) if match.group(2) else first
        if last < first:
            first, last = last, first
        numbers.extend(range(first, last + 1))
    return numbers


def audit_markdown(markdown: str) -> dict[str, Any]:
    lines = markdown.splitlines()
    start, end = _introduction_bounds(lines)
    occurrences: dict[int, list[dict[str, int]]] = defaultdict(list)
    paragraph = 0
    inside_paragraph = False

    for index in range(start, end):
        line = lines[index]
        if not line.strip():
            inside_paragraph = False
            continue
        if not inside_paragraph:
            paragraph += 1
            inside_paragraph = True
        for reference in _citation_numbers(line):
            occurrences[reference].append(
                {"line": index + 1, "paragraph": paragraph}
            )

    duplicates: dict[int, dict[str, Any]] = {}
    for reference, uses in sorted(occurrences.items()):
        if len(uses) <= 1:
            continue
        duplicates[reference] = {
            "count": len(uses),
            "excess": len(uses) - 1,
            "lines": sorted({use["line"] for use in uses}),
            "paragraphs": sorted({use["paragraph"] for use in uses}),
        }

    total = sum(len(uses) for uses in occurrences.values())
    return {
        "section_start_line": start + 1,
        "section_end_line": end,
        "total_occurrences": total,
        "unique_references": len(occurrences),
        "excess_occurrences": total - len(occurrences),
        "duplicates": duplicates,
    }


def audit_file(path: pathlib.Path) -> dict[str, Any]:
    return audit_markdown(path.read_text(encoding="utf-8"))


def _print_report(path: pathlib.Path, report: dict[str, Any]) -> None:
    print(f"Introduction citation audit: {path}")
    print(
        "occurrences={total_occurrences}; unique={unique_references}; "
        "excess={excess_occurrences}; repeated_refs={repeated}".format(
            repeated=len(report["duplicates"]), **report
        )
    )
    for reference, details in report["duplicates"].items():
        lines = ",".join(str(value) for value in details["lines"])
        paragraphs = ",".join(str(value) for value in details["paragraphs"])
        print(
            f"[{reference}] count={details['count']} excess={details['excess']} "
            f"lines={lines} paragraphs={paragraphs}"
        )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Flag any numbered reference used more than once in a Markdown "
            "Introduction. Ranges such as [1]–[3] are expanded."
        )
    )
    parser.add_argument("markdown", type=pathlib.Path)
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args(argv)

    try:
        report = audit_file(args.markdown)
    except (OSError, UnicodeError, ValueError) as error:
        parser.error(str(error))

    if args.as_json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        _print_report(args.markdown, report)
    return 1 if report["duplicates"] else 0


if __name__ == "__main__":
    sys.exit(main())
