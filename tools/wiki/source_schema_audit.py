#!/usr/bin/env python3
"""Audit the conditional source-page body contract.

The source pages in this repository are grounded in the Markdown parse under
``raw/sources/<folder>/`` (``full.md`` or a title-named ``.md``) and do not use
a BibTeX ingest pipeline.  This audit therefore checks only the editorial
contract introduced by the modeling-card migration:

* ``modeling_card`` is either ``required`` or ``not_applicable``;
* a required card appears after ``TL;DR`` and before ``Related Work Paragraph``;
* every source page has one English, copy-ready Related Work paragraph;
* the card labels and tables are present and do not contain placeholders.

It is a structural lint, not a claim-grounding oracle.  Human review still has
to decide the frontmatter value and verify every sentence against the raw parse.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

import frontmatter_audit
import wikilib


VALID_MODELING_CARD_VALUES = {"required", "not_applicable"}
SECTION_RE = re.compile(r"(?m)^##[ \t]+([^\r\n]+?)[ \t]*$")
CJK_RE = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff\u3040-\u30ff\uac00-\ud7af]")
PLACEHOLDER_RE = re.compile(
    r"(?i)(?:\.\.\.|\b(?:tbd|todo|n/?a|not applicable)\b)"
)
PLACEHOLDER_VALUES = {"-", "–", "—", "...", "tbd", "todo", "n/a", "na", "not applicable"}
RELATED_GUIDANCE = (
    "> Ready to reuse in a literature review. Replace `[x]` with the formal citation number."
)
CARD_GUIDANCE = (
    "> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm."
)

CARD_LABELS = {
    "Scenario": re.compile(r"(?m)^\*\*Scenario\*\*:\s*(.*)$"),
    "Problem & objective": re.compile(
        r"(?m)^\*\*Problem\s*&\s*objective\*\*:\s*(.*)$"
    ),
    "Algorithm": re.compile(r"(?m)^\*\*Algorithm\*\*:\s*(.*)$"),
}
CARD_TABLE_LABELS = {
    "Decision variables": re.compile(r"(?m)^\*\*Decision variables\*\*:\s*$"),
    "Constraints": re.compile(r"(?m)^\*\*Constraints\*\*:\s*$"),
}

VARIABLE_HEADER = ("variable", "symbol", "type / range", "meaning")
CONSTRAINT_HEADER = ("id", "meaning and key expression")


def _strip_quotes(value: str | None) -> str | None:
    if value is None:
        return None
    return value.strip().strip("'\"").strip()


def _is_placeholder(value: str) -> bool:
    normalized = value.strip().lower()
    return normalized in PLACEHOLDER_VALUES or PLACEHOLDER_RE.search(value) is not None


def _mask_abbreviation_periods(prose: str) -> str:
    patterns = [
        r"(?i)\b(?:et\s+al|e\.g|i\.e|fig|eq|sec|no|vs)\.",
        r"\b(?:[A-Z]\.){2,}",
        r"\b[A-Z]\.(?=\s+[A-Z])",
    ]
    masked = prose
    for pattern in patterns:
        masked = re.sub(
            pattern,
            lambda match: match.group(0).replace(".", "\x00"),
            masked,
        )
    return masked


def _sentence_spans(prose: str) -> list[tuple[int, int]]:
    masked = _mask_abbreviation_periods(prose)
    endings = list(re.finditer(r"[.!?](?:[\"')\]]*)?(?=\s|$)", masked))
    spans: list[tuple[int, int]] = []
    start = 0
    for ending in endings:
        spans.append((start, ending.end()))
        start = ending.end()
    return spans


def _guidance_errors(body: str, expected: str, section_name: str) -> list[str]:
    errors: list[str] = []
    lines = body.splitlines()
    nonblank = [(index, line.strip()) for index, line in enumerate(lines) if line.strip()]
    quote_lines = [line for _, line in nonblank if line.startswith(">")]
    if not nonblank or nonblank[0][1] != expected or quote_lines != [expected]:
        errors.append(
            f"{section_name} must begin with exactly one standard guidance blockquote"
        )
        return errors
    quote_index = nonblank[0][0]
    if quote_index + 1 >= len(lines) or lines[quote_index + 1].strip():
        errors.append(f"{section_name} requires a blank line after the guidance blockquote")
    return errors


def _line_ending(line: str) -> str:
    if line.endswith("\r\n"):
        return "\r\n"
    if line.endswith("\n") or line.endswith("\r"):
        return line[-1]
    return ""


def _mask_fenced_code(text: str) -> str:
    """Replace fenced-code characters with spaces while preserving offsets."""
    stripped = wikilib._strip_fenced_code(text)
    original_lines = text.splitlines(keepends=True)
    stripped_lines = stripped.splitlines(keepends=True)
    if len(original_lines) != len(stripped_lines):
        return stripped

    rendered: list[str] = []
    for original, clean in zip(original_lines, stripped_lines):
        if original == clean:
            rendered.append(original)
            continue
        ending = _line_ending(original)
        rendered.append(" " * (len(original) - len(ending)) + ending)
    return "".join(rendered)


def _sections(text: str) -> list[tuple[str, int, int, int]]:
    matches = list(SECTION_RE.finditer(_mask_fenced_code(text)))
    result: list[tuple[str, int, int, int]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        result.append((match.group(1).strip(), match.start(), match.end(), end))
    return result


def _section_body(text: str, section: tuple[str, int, int, int]) -> str:
    return text[section[2] : section[3]]


def _one_section(
    sections: list[tuple[str, int, int, int]], name: str
) -> list[tuple[str, int, int, int]]:
    return [section for section in sections if section[0] == name]


def _table_cells(line: str) -> tuple[str, ...]:
    sentinel = "\x00ESCAPED_PIPE\x00"
    value = line.strip().replace(r"\|", sentinel)
    if value.startswith("|"):
        value = value[1:]
    if value.endswith("|"):
        value = value[:-1]
    return tuple(cell.replace(sentinel, "|").strip() for cell in value.split("|"))


def _normalise_table_line(line: str) -> tuple[str, ...]:
    cells = [cell.lower() for cell in _table_cells(line)]
    return tuple(re.sub(r"\s+", " ", cell) for cell in cells)


def _table_state(body: str, expected: tuple[str, ...]) -> str:
    lines = body.splitlines()
    for index, line in enumerate(lines):
        if _normalise_table_line(line) != expected:
            continue
        cursor = index + 1
        if cursor >= len(lines) or not lines[cursor].strip():
            return "separator"
        separator_cells = _table_cells(lines[cursor])
        if len(separator_cells) != len(expected) or not all(
            re.fullmatch(r":?-{3,}:?", cell) for cell in separator_cells
        ):
            return "separator"

        cursor += 1
        data_found = False
        if cursor >= len(lines) or not lines[cursor].strip():
            return "missing"
        while cursor < len(lines):
            stripped = lines[cursor].strip()
            if not stripped:
                if data_found:
                    break
                cursor += 1
                continue
            if "|" not in stripped:
                break
            cells = _table_cells(stripped)
            if len(cells) != len(expected) or any(not cell for cell in cells):
                return "blank"
            if all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
                return "separator_data"
            if any(_is_placeholder(cell) for cell in cells):
                return "placeholder"
            data_found = True
            cursor += 1
        return "ok" if data_found else "missing"
    return "missing"


def _prose_paragraphs(body: str) -> list[str]:
    paragraphs: list[str] = []
    current: list[str] = []
    for line in body.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith(">"):
            if current:
                paragraphs.append(" ".join(current))
                current = []
            continue
        current.append(stripped)
    if current:
        paragraphs.append(" ".join(current))
    return paragraphs


def _audit_related_work(body: str) -> list[str]:
    errors: list[str] = []
    original_body = body
    errors.extend(_guidance_errors(original_body, RELATED_GUIDANCE, "Related Work Paragraph"))

    contains_fence = wikilib._strip_fenced_code(original_body) != original_body
    contains_list = re.search(
        r"(?m)^\s*(?:[-+*]|\d{1,9}[.)])\s+", original_body
    ) is not None
    contains_table = re.search(r"(?m)^\s*\|", original_body) is not None
    contains_heading = re.search(r"(?m)^\s*#{1,6}[ \t]+", original_body) is not None
    if contains_fence or contains_list or contains_table or contains_heading:
        errors.append(
            "Related Work Paragraph must contain prose only after the guidance blockquote"
        )

    body = _mask_fenced_code(body)
    paragraphs = _prose_paragraphs(body)
    if not paragraphs:
        return ["Related Work Paragraph has no prose"]
    if len(paragraphs) != 1:
        errors.append(
            f"Related Work Paragraph must contain one prose paragraph (found {len(paragraphs)})"
        )
    prose = " ".join(paragraphs)

    if "[x]" not in prose:
        errors.append("Related Work Paragraph must contain the [x] citation placeholder")
    if "—" in body or "--" in body:
        errors.append("Related Work Paragraph contains a forbidden dash (em dash or --)")
    if "[[" in body or "]]" in body:
        errors.append("Related Work Paragraph must not contain internal wikilinks")
    if CJK_RE.search(body):
        errors.append("Related Work Paragraph contains CJK text")

    sentence_spans = _sentence_spans(prose)
    sentence_count = len(sentence_spans)
    if sentence_count < 4 or sentence_count > 8:
        errors.append(
            f"Related Work Paragraph should contain 4-8 sentences (found {sentence_count})"
        )
    if sentence_spans and "[x]" not in prose[sentence_spans[0][0] : sentence_spans[0][1]]:
        errors.append("Related Work Paragraph must place [x] in the first prose sentence")
    return errors


def _audit_card(body: str) -> list[str]:
    errors: list[str] = []
    errors.extend(_guidance_errors(body, CARD_GUIDANCE, "Modeling Quick-Use Card"))
    body = _mask_fenced_code(body)
    if CJK_RE.search(body):
        errors.append("Modeling Quick-Use Card contains CJK text")

    label_matches: dict[str, re.Match[str]] = {}
    for label, pattern in CARD_LABELS.items():
        match = pattern.search(body)
        if not match:
            errors.append(f"Modeling Quick-Use Card is missing '{label}'")
        else:
            label_matches[label] = match
            value = match.group(1).strip()
            if not value:
                errors.append(f"Modeling Quick-Use Card has an empty '{label}' value")
            elif _is_placeholder(value):
                errors.append(
                    f"Modeling Quick-Use Card has a blank or placeholder '{label}' value"
                )
            elif label == "Problem & objective" and not re.search(r"\$[^$\n]+\$", value):
                errors.append(
                    "Modeling Quick-Use Card 'Problem & objective' must contain a math expression"
                )

    table_label_matches: dict[str, re.Match[str]] = {}
    for label, pattern in CARD_TABLE_LABELS.items():
        match = pattern.search(body)
        if not match:
            errors.append(f"Modeling Quick-Use Card is missing '{label}'")
        else:
            table_label_matches[label] = match

    ordered_names = [
        "Scenario",
        "Problem & objective",
        "Decision variables",
        "Constraints",
        "Algorithm",
    ]
    positions = {
        **{name: match.start() for name, match in label_matches.items()},
        **{name: match.start() for name, match in table_label_matches.items()},
    }
    if all(name in positions for name in ordered_names) and [positions[name] for name in ordered_names] != sorted(
        positions[name] for name in ordered_names
    ):
        errors.append("Modeling Quick-Use Card label order is invalid")

    decision_region = body
    constraint_region = body
    if all(name in positions for name in ("Decision variables", "Constraints", "Algorithm")):
        decision_region = body[positions["Decision variables"] : positions["Constraints"]]
        constraint_region = body[positions["Constraints"] : positions["Algorithm"]]

    variable_state = _table_state(decision_region, VARIABLE_HEADER)
    if variable_state == "missing":
        errors.append("Modeling Quick-Use Card is missing a populated decision-variable table")
    elif variable_state == "separator":
        errors.append("Modeling Quick-Use Card decision-variable table is missing a separator row")
    elif variable_state == "blank":
        errors.append("Modeling Quick-Use Card decision-variable table contains a blank cell")
    elif variable_state in {"placeholder", "separator_data"}:
        errors.append("Modeling Quick-Use Card decision-variable table contains a placeholder row or cell")

    constraint_state = _table_state(constraint_region, CONSTRAINT_HEADER)
    if constraint_state == "missing":
        errors.append("Modeling Quick-Use Card is missing a populated constraints table")
    elif constraint_state == "separator":
        errors.append("Modeling Quick-Use Card constraints table is missing a separator row")
    elif constraint_state == "blank":
        errors.append("Modeling Quick-Use Card constraints table contains a blank cell")
    elif constraint_state in {"placeholder", "separator_data"}:
        errors.append("Modeling Quick-Use Card constraints table contains a placeholder row or cell")
    return errors


def audit_text(text: str, slug: str = "<text>") -> list[str]:
    """Return structural errors for one source-page Markdown string."""
    errors: list[str] = []
    fm = frontmatter_audit._front_matter(text)
    if fm is None:
        return [f"{slug}: no parseable frontmatter block"]

    raw_value = frontmatter_audit._scalar(fm, "modeling_card")
    modeling_card = _strip_quotes(raw_value)
    modeling_card_keys = re.findall(r"(?m)^modeling_card\s*:", fm)
    if len(modeling_card_keys) != 1:
        errors.append(f"{slug}: frontmatter must contain exactly one modeling_card key")
    if modeling_card not in VALID_MODELING_CARD_VALUES:
        errors.append(
            f"{slug}: modeling_card must be one of {sorted(VALID_MODELING_CARD_VALUES)}"
        )

    sections = _sections(text)
    citation = _one_section(sections, "Citation")
    tldr = _one_section(sections, "TL;DR")
    related = _one_section(sections, "Related Work Paragraph")
    cards = _one_section(sections, "Modeling Quick-Use Card")

    if len(citation) != 1:
        errors.append(f"{slug}: expected exactly one 'Citation' section")
    elif sections and sections[0][0] != "Citation":
        errors.append(f"{slug}: Citation must be the first H2 section")
    if len(tldr) != 1:
        errors.append(f"{slug}: expected exactly one 'TL;DR' section")
    if len(related) != 1:
        errors.append(f"{slug}: expected exactly one 'Related Work Paragraph' section")
    if modeling_card == "required" and len(cards) != 1:
        errors.append(f"{slug}: modeling_card=required needs one 'Modeling Quick-Use Card'")
    if modeling_card == "not_applicable" and cards:
        errors.append(
            f"{slug}: modeling_card=not_applicable must not contain a Modeling Quick-Use Card"
        )

    if len(citation) == 1 and len(tldr) == 1 and citation[0][1] >= tldr[0][1]:
        errors.append(f"{slug}: Citation and TL;DR are in the wrong order")

    if len(tldr) == 1 and len(related) == 1:
        tldr_pos = tldr[0][1]
        related_pos = related[0][1]
        if related_pos <= tldr_pos:
            errors.append(f"{slug}: Related Work Paragraph is in the wrong order")
        between = [
            section[0]
            for section in sections
            if tldr_pos < section[1] < related_pos
            and section[0] != "Modeling Quick-Use Card"
        ]
        if between:
            errors.append(
                f"{slug}: Related Work Paragraph must follow TL;DR and the optional card directly (found {between})"
            )
        errors.extend(f"{slug}: {error}" for error in _audit_related_work(_section_body(text, related[0])))

    if modeling_card == "required" and len(cards) == 1 and len(related) == 1:
        card_pos = cards[0][1]
        if not (len(tldr) == 1 and tldr[0][1] < card_pos < related[0][1]):
            errors.append(f"{slug}: Modeling Quick-Use Card is in the wrong order")
        errors.extend(f"{slug}: {error}" for error in _audit_card(_section_body(text, cards[0])))

    return errors


def audit_page(path: str) -> list[str]:
    slug = os.path.splitext(os.path.basename(path))[0]
    return audit_text(wikilib.read_text(path), slug)


def _resolve_path(value: str) -> str:
    if os.path.isabs(value):
        return os.path.abspath(value)
    return os.path.abspath(os.path.join(wikilib.repo_root(), value))


def source_paths(values: list[str] | None) -> list[str]:
    if not values:
        root = os.path.join(wikilib.wiki_dir(), "sources")
        return sorted(str(path) for path in Path(root).glob("*.md"))

    source_root = Path(wikilib.wiki_dir(), "sources").resolve()
    paths: list[str] = []
    for value in values:
        path = Path(_resolve_path(value)).resolve()
        try:
            path.relative_to(source_root)
        except ValueError as error:
            raise ValueError(f"path is outside wiki/sources: {value}") from error
        if path.is_dir():
            paths.extend(str(candidate) for candidate in path.rglob("*.md"))
        elif path.is_file():
            paths.append(str(path))
        else:
            raise FileNotFoundError(value)
    resolved = sorted(set(paths))
    if values and not resolved:
        raise FileNotFoundError("no Markdown source pages found in requested path(s)")
    return resolved


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--path",
        action="append",
        help="source Markdown file or directory; repeat for multiple paths (default: wiki/sources)",
    )
    parser.add_argument(
        "--json",
        dest="json_path",
        help="write a machine-readable report (relative paths land in .curation-out/)",
    )
    args = parser.parse_args(argv)

    try:
        paths = source_paths(args.path)
    except (FileNotFoundError, ValueError) as error:
        print(f"invalid source path: {error}", file=sys.stderr)
        return 2
    failures: dict[str, list[str]] = {}
    for path in paths:
        errors = audit_page(path)
        if errors:
            failures[os.path.relpath(path, wikilib.repo_root())] = errors

    print("=" * 70)
    print(f"SOURCE SCHEMA AUDIT: {len(paths)} pages checked")
    print("=" * 70)
    if failures:
        print(f"PAGES WITH ERRORS: {len(failures)}")
        for path in sorted(failures):
            print(f"  {path}")
            for error in failures[path]:
                print(f"      - {error}")
    else:
        print("PAGES WITH ERRORS: 0")

    if args.json_path:
        output = args.json_path
        if not os.path.isabs(output):
            output = os.path.join(wikilib.scratch_dir(), output)
        os.makedirs(os.path.dirname(os.path.abspath(output)), exist_ok=True)
        with open(output, "w", encoding="utf-8") as handle:
            json.dump(
                {"checked": len(paths), "failures": failures},
                handle,
                indent=2,
                ensure_ascii=False,
            )
        print(f"Report written to {output}")

    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
