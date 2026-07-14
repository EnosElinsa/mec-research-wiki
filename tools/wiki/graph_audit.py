"""Build and compare immutable-cohort wiki graph audit reports.

The graph is wiki-only, simple, and undirected.  Snapshot membership is
selected once from frontmatter ``created`` dates; comparisons always reuse that
stored member list, so later pages cannot change the induced cohort metrics.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
import re
import sys
import tempfile
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Iterable

import wikilib


SCHEMA_VERSION = 1
DEFAULT_EXCLUSIONS = frozenset({"index", "log", "overview"})

_TYPE_BY_DIRECTORY = {
    "sources": "source",
    "concepts": "concept",
    "entities": "entity",
    "findings": "finding",
    "synthesis": "synthesis",
    "comparisons": "comparison",
    "methodology": "methodology",
    "queries": "query",
    "thesis": "thesis",
    "references": "reference",
}
_MEMBER_TYPES = frozenset(_TYPE_BY_DIRECTORY.values())
_METRIC_KEYS = (
    "induced_edge_count",
    "possible_edge_count",
    "local_cohesion",
    "component_count",
    "largest_component_size",
    "isolate_count",
    "weak_member_count",
    "bridge_edge_count",
)
_INTEGER_METRIC_KEYS = frozenset(_METRIC_KEYS) - {"local_cohesion"}
_SEMANTIC_KEYS = frozenset(
    {"graph", "cohort", "local_cohesion", "external_degrees"}
)
_FRONTMATTER = re.compile(r"\A\ufeff?---\s*\r?\n(.*?)\r?\n---\s*(?:\r?\n|\Z)", re.S)
_CREATED = re.compile(r"(?m)^created\s*:\s*(.*?)\s*$")


class GraphAuditError(ValueError):
    """Raised when a graph report or frozen cohort is unsafe to use."""


def _utc_timestamp(value: str | None = None) -> str:
    if value is not None:
        return _valid_timestamp(value)
    return (
        datetime.now(timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )


def _valid_timestamp(value: str) -> str:
    if not isinstance(value, str) or not value:
        raise GraphAuditError("timestamp must be an offset-aware UTC ISO-8601 string")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise GraphAuditError(
            "timestamp must be an offset-aware UTC ISO-8601 string"
        ) from exc
    if (
        parsed.tzinfo is None
        or parsed.utcoffset() != timezone.utc.utcoffset(parsed)
    ):
        raise GraphAuditError("timestamp must be an offset-aware UTC ISO-8601 string")
    return value


def _validate_report_metadata(report: dict, report_type: str) -> None:
    if type(report.get("schema_version")) is not int or report["schema_version"] != SCHEMA_VERSION:
        raise GraphAuditError("unsupported graph audit schema version")
    if report.get("report_type") != report_type:
        raise GraphAuditError(f"report type must be {report_type}")
    _valid_timestamp(report.get("generated_at_utc"))
    if not isinstance(report.get("label"), str) or not report["label"].strip():
        raise GraphAuditError("report label must be a non-empty string")
    semantics = report.get("graph_semantics")
    if not isinstance(semantics, dict) or not _SEMANTIC_KEYS.issubset(semantics):
        raise GraphAuditError("graph semantics must contain the required fields")
    if any(
        not isinstance(semantics[key], str) or not semantics[key].strip()
        for key in _SEMANTIC_KEYS
    ):
        raise GraphAuditError("graph semantics fields must be non-empty strings")
    if "external_observation" not in report:
        raise GraphAuditError("external UI observation field is required")
    observation = report["external_observation"]
    if observation is None:
        _ui_observation(None, None)
    elif isinstance(observation, dict) and set(observation) == {
        "source", "pages", "cohesion"
    }:
        if observation["source"] != "LLM Wiki UI":
            raise GraphAuditError("external UI observation source must be LLM Wiki UI")
        _ui_observation(observation["pages"], observation["cohesion"])
    else:
        raise GraphAuditError("invalid external UI observation")


def _valid_date(value: str) -> str:
    if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        raise GraphAuditError("created date must use YYYY-MM-DD")
    try:
        date.fromisoformat(value)
    except ValueError as exc:
        raise GraphAuditError("created date must use YYYY-MM-DD") from exc
    return value


def _valid_weak_degree(value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise GraphAuditError("weak degree must be a non-negative integer")
    return value


def _normalized_exclusions(
    exclusions: set[str] | frozenset[str] | Iterable[str] | None,
) -> frozenset[str]:
    values = set(DEFAULT_EXCLUSIONS)
    if exclusions is not None:
        for value in exclusions:
            if not isinstance(value, str):
                raise GraphAuditError("exclusions must contain slugs")
            slug = wikilib.wikilink_basename(value)
            if not slug:
                raise GraphAuditError("exclusions must contain non-empty slugs")
            values.add(slug)
    return frozenset(values)


def frontmatter_created(source: str | os.PathLike[str]) -> str | None:
    """Return a page's frontmatter ``created`` value, if present.

    ``source`` may be a page path or the Markdown text itself.  The parser is
    deliberately narrow: no general YAML dependency is needed for a scalar
    ISO date.
    """
    raw_source = os.fspath(source)
    if "\n" not in raw_source and "\r" not in raw_source and os.path.isfile(raw_source):
        text = wikilib.read_text(raw_source)
    else:
        text = raw_source
    frontmatter = _FRONTMATTER.match(text)
    if not frontmatter:
        return None
    match = _CREATED.search(frontmatter.group(1))
    if not match:
        return None
    value = match.group(1).strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        value = value[1:-1].strip()
    return value or None


def cohort_hash(members: Iterable[str]) -> str:
    """Hash the sorted member array as compact UTF-8 JSON."""
    canonical = sorted(members)
    encoded = json.dumps(
        canonical, ensure_ascii=False, separators=(",", ":")
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def select_created_members(
    pages: dict[str, str],
    created: str,
    exclusions: set[str] | frozenset[str] | Iterable[str],
) -> list[str]:
    """Select non-administrative wiki pages with an exact created date."""
    created = _valid_date(created)
    excluded = _normalized_exclusions(exclusions)
    return sorted(
        slug
        for slug, path in pages.items()
        if slug not in excluded and frontmatter_created(path) == created
    )


def _member_type(path: str, slug: str) -> str:
    directory = Path(path).parent.name.lower()
    member_type = _TYPE_BY_DIRECTORY.get(directory)
    if member_type is None:
        raise GraphAuditError(
            f"cannot derive member type from wiki directory for: {slug}"
        )
    return member_type


def _member_types(members: list[str], pages: dict[str, str]) -> dict[str, str]:
    return {slug: _member_type(pages[slug], slug) for slug in members}


def _components(
    members: list[str], adjacency: dict[str, set[str]]
) -> list[dict]:
    unseen = set(members)
    groups: list[list[str]] = []
    while unseen:
        start = min(unseen)
        stack = [start]
        unseen.remove(start)
        group: list[str] = []
        while stack:
            node = stack.pop()
            group.append(node)
            for neighbor in sorted(adjacency[node], reverse=True):
                if neighbor in unseen:
                    unseen.remove(neighbor)
                    stack.append(neighbor)
        groups.append(sorted(group))
    groups.sort(key=lambda group: (-len(group), group))
    return [
        {"id": component_id, "size": len(group), "members": group}
        for component_id, group in enumerate(groups, 1)
    ]


def _bridges(
    members: list[str], adjacency: dict[str, set[str]]
) -> list[list[str]]:
    discovery: dict[str, int] = {}
    low: dict[str, int] = {}
    parent: dict[str, str] = {}
    found: set[tuple[str, str]] = set()
    clock = 0

    def visit(node: str) -> None:
        nonlocal clock
        clock += 1
        discovery[node] = clock
        low[node] = clock
        for neighbor in sorted(adjacency[node]):
            if neighbor not in discovery:
                parent[neighbor] = node
                visit(neighbor)
                low[node] = min(low[node], low[neighbor])
                if low[neighbor] > discovery[node]:
                    found.add(tuple(sorted((node, neighbor))))
            elif parent.get(node) != neighbor:
                low[node] = min(low[node], discovery[neighbor])

    for member in members:
        if member not in discovery:
            visit(member)
    return [list(edge) for edge in sorted(found)]


def _graph_from_edges(
    members: list[str],
    induced_edges: list[tuple[str, str]],
    external_degrees: dict[str, int],
    member_types: dict[str, str] | None,
    weak_degree: int,
) -> dict:
    adjacency = {member: set() for member in members}
    for left, right in induced_edges:
        adjacency[left].add(right)
        adjacency[right].add(left)

    internal_degrees = {member: len(adjacency[member]) for member in members}
    components = _components(members, adjacency)
    component_by_member = {
        member: component["id"]
        for component in components
        for member in component["members"]
    }
    isolates = [member for member in members if internal_degrees[member] == 0]
    weak_rows = []
    for member in members:
        if internal_degrees[member] > weak_degree:
            continue
        row = {
            "slug": member,
            "internal_degree": internal_degrees[member],
            "external_degree": external_degrees[member],
            "component_id": component_by_member[member],
        }
        if member_types is not None:
            row["type"] = member_types[member]
        weak_rows.append(row)
    bridge_edges = _bridges(members, adjacency)
    possible_edges = len(members) * (len(members) - 1) // 2
    local_cohesion = (
        len(induced_edges) / possible_edges if possible_edges else 0.0
    )
    metrics = {
        "induced_edge_count": len(induced_edges),
        "possible_edge_count": possible_edges,
        "local_cohesion": local_cohesion,
        "component_count": len(components),
        "largest_component_size": max(
            (item["size"] for item in components), default=0
        ),
        "isolate_count": len(isolates),
        "weak_member_count": len(weak_rows),
        "bridge_edge_count": len(bridge_edges),
    }
    return {
        "metrics": metrics,
        "internal_degrees": internal_degrees,
        "external_degrees": external_degrees,
        "induced_edges": [list(edge) for edge in induced_edges],
        "components": components,
        "isolates": isolates,
        "weak_members": weak_rows,
        "bridge_edges": bridge_edges,
    }


def _partition_edges(
    members: list[str], all_edges: Iterable[tuple[str, str] | list[str]]
) -> tuple[list[tuple[str, str]], dict[str, int]]:
    member_set = set(members)
    normalized_edges: set[tuple[str, str]] = set()
    for raw_edge in all_edges:
        if (
            not isinstance(raw_edge, (tuple, list))
            or len(raw_edge) != 2
            or any(not isinstance(node, str) for node in raw_edge)
        ):
            raise GraphAuditError("invalid graph edge")
        left, right = raw_edge
        if left == right:
            continue
        normalized_edges.add(tuple(sorted((left, right))))

    induced: set[tuple[str, str]] = set()
    external_degrees = {member: 0 for member in members}
    for left, right in sorted(normalized_edges):
        left_inside = left in member_set
        right_inside = right in member_set
        if left_inside and right_inside:
            induced.add((left, right))
        elif left_inside:
            external_degrees[left] += 1
        elif right_inside:
            external_degrees[right] += 1
    return sorted(induced), external_degrees


def graph_payload(
    members: Iterable[str],
    all_edges: Iterable[tuple[str, str] | list[str]],
    weak_degree: int,
) -> dict:
    """Compute the induced graph from a pre-resolved wiki edge set."""
    weak_degree = _valid_weak_degree(weak_degree)
    member_list = list(members)
    if any(not isinstance(member, str) or not member for member in member_list):
        raise GraphAuditError("cohort members must be non-empty slugs")
    if len(member_list) != len(set(member_list)):
        raise GraphAuditError("cohort members must be unique")
    member_list = sorted(member_list)
    induced, external_degrees = _partition_edges(member_list, all_edges)
    return _graph_from_edges(
        member_list,
        induced,
        external_degrees,
        None,
        weak_degree,
    )


def _ui_observation(
    observed_ui_pages: int | None, observed_ui_cohesion: float | None
) -> dict | None:
    if (observed_ui_pages is None) != (observed_ui_cohesion is None):
        raise GraphAuditError(
            "observed UI pages and cohesion must be provided together"
        )
    if observed_ui_pages is None:
        return None
    if (
        isinstance(observed_ui_pages, bool)
        or not isinstance(observed_ui_pages, int)
        or observed_ui_pages < 0
    ):
        raise GraphAuditError("observed UI pages must be a non-negative integer")
    if (
        isinstance(observed_ui_cohesion, bool)
        or not isinstance(observed_ui_cohesion, (int, float))
        or not 0 <= observed_ui_cohesion <= 1
    ):
        raise GraphAuditError("observed UI cohesion must be between 0 and 1")
    return {
        "source": "LLM Wiki UI",
        "pages": observed_ui_pages,
        "cohesion": observed_ui_cohesion,
    }


def build_snapshot(
    pages: dict[str, str],
    *,
    created: str,
    label: str,
    weak_degree: int = 1,
    exclusions: set[str] | frozenset[str] | Iterable[str] = DEFAULT_EXCLUSIONS,
    observed_ui_pages: int | None = None,
    observed_ui_cohesion: float | None = None,
) -> dict:
    """Build a frozen created-date cohort snapshot."""
    created = _valid_date(created)
    if not isinstance(label, str) or not label.strip():
        raise GraphAuditError("label must be a non-empty string")
    weak_degree = _valid_weak_degree(weak_degree)
    excluded = _normalized_exclusions(exclusions)
    members = select_created_members(pages, created, excluded)
    member_types = _member_types(members, pages)
    all_edges = wikilib.wiki_undirected_edges(pages, excluded=excluded)
    induced_edges, external_degrees = _partition_edges(members, all_edges)
    snapshot = {
        "schema_version": SCHEMA_VERSION,
        "report_type": "snapshot",
        "generated_at_utc": _utc_timestamp(),
        "label": label.strip(),
        "graph_semantics": {
            "graph": "wiki-only simple undirected unique-basename wikilink graph",
            "cohort": "exact frontmatter created date, frozen as the stored member array",
            "local_cohesion": "induced_edges / (members * (members - 1) / 2)",
            "external_degrees": "boundary edges to non-member wiki pages; exclusions omitted",
        },
        "parameters": {
            "weak_degree": weak_degree,
            "exclusions": sorted(excluded),
        },
        "cohort": {
            "selector": {"created": created},
            "members": members,
            "member_types": member_types,
            "member_count": len(members),
            "member_hash_algorithm": "sha256-canonical-json",
            "member_hash": cohort_hash(members),
        },
        "external_observation": _ui_observation(
            observed_ui_pages, observed_ui_cohesion
        ),
        "graph": _graph_from_edges(
            members,
            induced_edges,
            external_degrees,
            member_types,
            weak_degree=weak_degree,
        ),
    }
    validate_snapshot(snapshot)
    return snapshot


def _validate_context(
    report: dict, pages: dict[str, str] | None = None
) -> tuple[list[str], dict[str, str], frozenset[str], int]:
    cohort = report.get("cohort")
    if not isinstance(cohort, dict):
        raise GraphAuditError("cohort must be an object")
    members = cohort.get("members")
    if not isinstance(members, list) or any(
        not isinstance(member, str) or not member for member in members
    ):
        raise GraphAuditError("cohort members must be a sorted string array")
    if members != sorted(members) or len(members) != len(set(members)):
        raise GraphAuditError("cohort members must be sorted and unique")
    if type(cohort.get("member_count")) is not int or cohort["member_count"] != len(members):
        raise GraphAuditError("cohort member count mismatch")
    if cohort.get("member_hash_algorithm") != "sha256-canonical-json":
        raise GraphAuditError("unsupported cohort hash algorithm")
    if cohort.get("member_hash") != cohort_hash(members):
        raise GraphAuditError("cohort hash mismatch")

    member_types = cohort.get("member_types")
    if not isinstance(member_types, dict) or set(member_types) != set(members):
        raise GraphAuditError("cohort member type coverage mismatch")
    if any(
        not isinstance(member_types[member], str)
        or member_types[member] not in _MEMBER_TYPES
        for member in members
    ):
        raise GraphAuditError("cohort member type mismatch")
    if pages is not None:
        missing = sorted(set(members) - set(pages))
        if missing:
            raise GraphAuditError(f"missing frozen member(s): {', '.join(missing)}")
        actual_types = _member_types(members, pages)
        mismatched = [
            member
            for member in members
            if member_types[member] != actual_types[member]
        ]
        if mismatched:
            raise GraphAuditError(
                f"cohort member type mismatch: {', '.join(mismatched)}"
            )

    selector = cohort.get("selector")
    if not isinstance(selector, dict) or set(selector) != {"created"}:
        raise GraphAuditError("cohort selector must contain only created")
    _valid_date(selector["created"])

    parameters = report.get("parameters")
    if not isinstance(parameters, dict):
        raise GraphAuditError("parameters must be an object")
    weak_degree = _valid_weak_degree(parameters.get("weak_degree"))
    exclusions = parameters.get("exclusions")
    if not isinstance(exclusions, list) or any(
        not isinstance(item, str) or not item for item in exclusions
    ):
        raise GraphAuditError("exclusions must be a sorted string array")
    if exclusions != sorted(exclusions) or len(exclusions) != len(set(exclusions)):
        raise GraphAuditError("exclusions must be sorted and unique")
    excluded = frozenset(exclusions)
    missing_admin = sorted(DEFAULT_EXCLUSIONS - excluded)
    if missing_admin:
        raise GraphAuditError(
            f"missing administrative exclusion(s): {', '.join(missing_admin)}"
        )
    return members, member_types, excluded, weak_degree


def _validated_induced_edges(raw_edges: object, members: list[str]) -> list[tuple[str, str]]:
    if not isinstance(raw_edges, list):
        raise GraphAuditError("induced edges must be an array")
    member_set = set(members)
    edges: list[tuple[str, str]] = []
    for raw_edge in raw_edges:
        if (
            not isinstance(raw_edge, list)
            or len(raw_edge) != 2
            or any(not isinstance(node, str) for node in raw_edge)
        ):
            raise GraphAuditError("invalid induced edge")
        left, right = raw_edge
        if left not in member_set or right not in member_set:
            raise GraphAuditError("induced edge endpoint is outside the cohort")
        if left >= right:
            raise GraphAuditError("induced edges must be canonical")
        edges.append((left, right))
    if edges != sorted(edges):
        raise GraphAuditError("induced edges must be sorted")
    if len(edges) != len(set(edges)):
        raise GraphAuditError("duplicate induced edge")
    return edges


def _validate_graph(
    graph: object,
    members: list[str],
    member_types: dict[str, str],
    weak_degree: int,
) -> dict:
    if not isinstance(graph, dict):
        raise GraphAuditError("graph must be an object")
    metrics = graph.get("metrics")
    if not isinstance(metrics, dict) or set(metrics) != set(_METRIC_KEYS):
        raise GraphAuditError("graph metric fields mismatch")
    for field in _INTEGER_METRIC_KEYS:
        if type(metrics[field]) is not int:
            raise GraphAuditError(f"integer metric must be an exact int: {field}")
    if type(metrics["local_cohesion"]) is not float:
        raise GraphAuditError("local_cohesion metric must be a float")
    edges = _validated_induced_edges(graph.get("induced_edges"), members)
    external = graph.get("external_degrees")
    if not isinstance(external, dict) or set(external) != set(members):
        raise GraphAuditError("external degree coverage mismatch")
    if any(
        isinstance(external[member], bool)
        or not isinstance(external[member], int)
        or external[member] < 0
        for member in members
    ):
        raise GraphAuditError("external degrees must be non-negative integers")
    internal = graph.get("internal_degrees")
    if not isinstance(internal, dict) or set(internal) != set(members):
        raise GraphAuditError("internal degree coverage mismatch")
    if any(
        type(internal[member]) is not int or internal[member] < 0
        for member in members
    ):
        raise GraphAuditError("internal degrees must be exact non-negative integers")
    components = graph.get("components")
    if not isinstance(components, list) or any(
        not isinstance(component, dict)
        or set(component) != {"id", "size", "members"}
        or type(component["id"]) is not int
        or component["id"] < 1
        or type(component["size"]) is not int
        or component["size"] < 1
        or not isinstance(component["members"], list)
        or any(not isinstance(member, str) for member in component["members"])
        for component in components
    ):
        raise GraphAuditError(
            "components must use exact integer identifiers and sizes"
        )
    weak_members = graph.get("weak_members")
    weak_fields = {
        "slug",
        "type",
        "internal_degree",
        "external_degree",
        "component_id",
    }
    if not isinstance(weak_members, list) or any(
        not isinstance(row, dict)
        or set(row) != weak_fields
        or not isinstance(row["slug"], str)
        or not isinstance(row["type"], str)
        or type(row["internal_degree"]) is not int
        or row["internal_degree"] < 0
        or type(row["external_degree"]) is not int
        or row["external_degree"] < 0
        or type(row["component_id"]) is not int
        or row["component_id"] < 1
        for row in weak_members
    ):
        raise GraphAuditError("weak members must use exact integer graph fields")
    expected = _graph_from_edges(
        members, edges, external, member_types, weak_degree
    )
    checks = (
        ("metrics", "graph metric mismatch"),
        ("internal_degrees", "internal degree mismatch"),
        ("components", "component mismatch"),
        ("isolates", "isolate mismatch"),
        ("weak_members", "weak member mismatch"),
        ("bridge_edges", "bridge mismatch"),
    )
    for field, message in checks:
        if graph.get(field) != expected[field]:
            raise GraphAuditError(message)
    return graph


def validate_snapshot(
    payload: dict,
) -> dict:
    """Validate a stored snapshot without consulting mutable graph edges."""
    if not isinstance(payload, dict):
        raise GraphAuditError("snapshot must be an object")
    _validate_report_metadata(payload, "snapshot")
    members, member_types, _, weak_degree = _validate_context(payload)
    _validate_graph(payload.get("graph"), members, member_types, weak_degree)
    return payload


def build_comparison(
    baseline: dict | str | os.PathLike[str],
    pages: dict[str, str],
    *,
    baseline_path: str,
) -> dict:
    """Compare current wiki edges using the baseline's immutable member list."""
    if isinstance(baseline, (str, os.PathLike)):
        source_path = os.fspath(baseline)
        baseline = _read_json(Path(source_path))
    validate_snapshot(baseline)
    members = baseline["cohort"]["members"]
    missing = sorted(set(members) - set(pages))
    if missing:
        raise GraphAuditError(f"missing frozen member(s): {', '.join(missing)}")
    current_types = _member_types(members, pages)
    if current_types != baseline["cohort"]["member_types"]:
        mismatched = [
            member
            for member in members
            if current_types[member] != baseline["cohort"]["member_types"][member]
        ]
        raise GraphAuditError(
            f"cohort member type mismatch: {', '.join(mismatched)}"
        )

    weak_degree = baseline["parameters"]["weak_degree"]
    exclusions = frozenset(baseline["parameters"]["exclusions"])
    all_edges = wikilib.wiki_undirected_edges(pages, excluded=exclusions)
    induced_edges, external_degrees = _partition_edges(members, all_edges)
    current_graph = _graph_from_edges(
        members,
        induced_edges,
        external_degrees,
        current_types,
        weak_degree,
    )
    baseline_graph = baseline["graph"]
    baseline_metrics = baseline_graph["metrics"]
    current_metrics = current_graph["metrics"]
    metric_deltas = {
        key: current_metrics[key] - baseline_metrics[key]
        for key in _METRIC_KEYS
    }
    internal_deltas = {
        member: current_graph["internal_degrees"][member]
        - baseline_graph["internal_degrees"][member]
        for member in members
    }
    external_deltas = {
        member: current_graph["external_degrees"][member]
        - baseline_graph["external_degrees"][member]
        for member in members
    }
    baseline_edges = {tuple(edge) for edge in baseline_graph["induced_edges"]}
    current_edges = {tuple(edge) for edge in current_graph["induced_edges"]}
    return {
        "schema_version": SCHEMA_VERSION,
        "report_type": "comparison",
        "generated_at_utc": _utc_timestamp(),
        "label": baseline["label"],
        "graph_semantics": copy.deepcopy(baseline["graph_semantics"]),
        "parameters": copy.deepcopy(baseline["parameters"]),
        "cohort": copy.deepcopy(baseline["cohort"]),
        "external_observation": copy.deepcopy(baseline["external_observation"]),
        "baseline": {
            "path": baseline_path,
            "metrics": copy.deepcopy(baseline_metrics),
        },
        "graph": current_graph,
        "comparison": {
            "metric_deltas": metric_deltas,
            "internal_degree_deltas": internal_deltas,
            "external_degree_deltas": external_deltas,
            "added_edges": [
                list(edge) for edge in sorted(current_edges - baseline_edges)
            ],
            "removed_edges": [
                list(edge) for edge in sorted(baseline_edges - current_edges)
            ],
        },
    }


def _component_map(graph: dict) -> dict[str, int]:
    return {
        member: component["id"]
        for component in graph["components"]
        for member in component["members"]
    }


def build_coverage_ledger(snapshot: dict) -> dict:
    """Create the editorial coverage ledger for a validated baseline."""
    validate_snapshot(snapshot)
    graph = snapshot["graph"]
    component_by_member = _component_map(graph)
    members = snapshot["cohort"]["members"]
    return {
        "schema_version": SCHEMA_VERSION,
        "report_type": "coverage-ledger",
        "baseline_label": snapshot["label"],
        "baseline_member_hash": snapshot["cohort"]["member_hash"],
        "entries": [
            {
                "slug": member,
                "type": snapshot["cohort"]["member_types"][member],
                "baseline_component": component_by_member[member],
                "baseline_internal_degree": graph["internal_degrees"][member],
                "theme": None,
                "status": "pending",
                "evidence_paths": [],
                "candidate_relationships": [],
                "accepted_links": [],
                "deferral_reason": None,
                "post_batch_internal_degree": graph["internal_degrees"][member],
            }
            for member in members
        ],
    }


def _validated_report_graph(report: dict) -> tuple[list[str], dict]:
    if not isinstance(report, dict):
        raise GraphAuditError("graph report must be an object")
    report_type = report.get("report_type")
    if report_type == "snapshot":
        validate_snapshot(report)
        return report["cohort"]["members"], report["graph"]
    if report_type != "comparison":
        raise GraphAuditError("ledger refresh requires a graph report")
    _validate_report_metadata(report, "comparison")
    members, member_types, _, weak_degree = _validate_context(report)
    graph = _validate_graph(report.get("graph"), members, member_types, weak_degree)
    return members, graph


_LEDGER_ENTRY_FIELDS = frozenset(
    {
        "slug",
        "type",
        "baseline_component",
        "baseline_internal_degree",
        "theme",
        "status",
        "evidence_paths",
        "candidate_relationships",
        "accepted_links",
        "deferral_reason",
        "post_batch_internal_degree",
    }
)


def _validate_coverage_ledger(ledger: dict) -> list[str]:
    if not isinstance(ledger, dict):
        raise GraphAuditError("coverage ledger must be an object")
    if type(ledger.get("schema_version")) is not int or ledger["schema_version"] != SCHEMA_VERSION:
        raise GraphAuditError("unsupported coverage ledger schema version")
    if ledger.get("report_type") != "coverage-ledger":
        raise GraphAuditError("report type must be coverage-ledger")
    if not isinstance(ledger.get("baseline_label"), str) or not ledger["baseline_label"].strip():
        raise GraphAuditError("coverage ledger baseline label is required")
    member_hash = ledger.get("baseline_member_hash")
    if not isinstance(member_hash, str) or not re.fullmatch(r"[0-9a-f]{64}", member_hash):
        raise GraphAuditError("coverage ledger baseline member hash is invalid")
    entries = ledger.get("entries")
    if not isinstance(entries, list) or any(not isinstance(entry, dict) for entry in entries):
        raise GraphAuditError("coverage ledger entries must be an array")
    slugs = [entry.get("slug") for entry in entries]
    if any(not isinstance(slug, str) or not slug for slug in slugs):
        raise GraphAuditError("coverage ledger member coverage mismatch")
    if slugs != sorted(slugs) or len(slugs) != len(set(slugs)):
        raise GraphAuditError("coverage ledger member coverage mismatch")
    allowed = _LEDGER_ENTRY_FIELDS | {"post_batch_component"}
    for entry in entries:
        if set(entry) - allowed or not _LEDGER_ENTRY_FIELDS.issubset(entry):
            raise GraphAuditError("coverage ledger member row is malformed")
        if not isinstance(entry["type"], str) or entry["type"] not in _MEMBER_TYPES:
            raise GraphAuditError("coverage ledger member row is malformed")
        for field, minimum in (
            ("baseline_component", 1),
            ("baseline_internal_degree", 0),
            ("post_batch_internal_degree", 0),
        ):
            value = entry[field]
            if isinstance(value, bool) or not isinstance(value, int) or value < minimum:
                raise GraphAuditError("coverage ledger member row is malformed")
        if "post_batch_component" in entry:
            value = entry["post_batch_component"]
            if isinstance(value, bool) or not isinstance(value, int) or value < 1:
                raise GraphAuditError("coverage ledger member row is malformed")
        if entry["theme"] is not None and not isinstance(entry["theme"], str):
            raise GraphAuditError("coverage ledger member row is malformed")
        if not isinstance(entry["status"], str) or not entry["status"].strip():
            raise GraphAuditError("coverage ledger member row is malformed")
        if any(not isinstance(entry[field], list) for field in (
            "evidence_paths", "candidate_relationships", "accepted_links"
        )):
            raise GraphAuditError("coverage ledger member row is malformed")
        if entry["deferral_reason"] is not None and not isinstance(
            entry["deferral_reason"], str
        ):
            raise GraphAuditError("coverage ledger member row is malformed")
    return slugs


def refresh_coverage_ledger(ledger: dict, comparison: dict) -> dict:
    """Refresh graph-derived ledger fields while preserving editorial work."""
    ledger_slugs = _validate_coverage_ledger(ledger)
    members, graph = _validated_report_graph(comparison)
    comparison_cohort = comparison["cohort"]
    if ledger["baseline_member_hash"] != comparison_cohort["member_hash"]:
        raise GraphAuditError("coverage ledger cohort hash mismatch")
    if ledger_slugs != members:
        raise GraphAuditError("coverage ledger member list mismatch")
    report_types = comparison_cohort["member_types"]
    for entry in ledger["entries"]:
        if entry["type"] != report_types[entry["slug"]]:
            raise GraphAuditError("coverage ledger member type mismatch")

    refreshed = copy.deepcopy(ledger)
    component_by_member = _component_map(graph)
    for row in refreshed["entries"]:
        member = row["slug"]
        row["post_batch_component"] = component_by_member[member]
        row["post_batch_internal_degree"] = graph["internal_degrees"][member]
    return refreshed


def _date_argument(value: str) -> str:
    try:
        return _valid_date(value)
    except GraphAuditError as exc:
        raise argparse.ArgumentTypeError(str(exc)) from exc


def _nonnegative_integer(value: str) -> int:
    try:
        parsed = int(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("must be a non-negative integer") from exc
    if parsed < 0:
        raise argparse.ArgumentTypeError("must be a non-negative integer")
    return parsed


def _cohesion_argument(value: str) -> float:
    try:
        parsed = float(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("must be between 0 and 1") from exc
    if not 0 <= parsed <= 1:
        raise argparse.ArgumentTypeError("must be between 0 and 1")
    return parsed


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    snapshot = subparsers.add_parser("snapshot", help="freeze a created-date cohort")
    snapshot.add_argument("--created", required=True, type=_date_argument)
    snapshot.add_argument("--label", required=True)
    snapshot.add_argument("--weak-degree", type=_nonnegative_integer, default=1)
    snapshot.add_argument("--exclude", action="append", default=[], metavar="SLUG")
    snapshot.add_argument("--observed-ui-pages", type=_nonnegative_integer)
    snapshot.add_argument("--observed-ui-cohesion", type=_cohesion_argument)
    snapshot.add_argument("--json", required=True, metavar="PATH")
    snapshot.add_argument("--ledger", metavar="PATH")

    compare = subparsers.add_parser("compare", help="compare a frozen cohort")
    compare.add_argument("--baseline", required=True, metavar="PATH")
    compare.add_argument("--json", required=True, metavar="PATH")
    compare.add_argument("--ledger", metavar="PATH")
    return parser


def _win32_alias_path(value: str) -> str:
    """Normalize Win32-equivalent spellings before collision checks."""
    normalized = value.replace("/", "\\")
    folded = normalized.casefold()
    if folded.startswith("\\\\?\\unc\\"):
        normalized = "\\\\" + normalized[8:]
    elif folded.startswith(("\\\\?\\", "\\\\.\\")):
        normalized = normalized[4:]

    drive, tail = os.path.splitdrive(normalized)
    components = tail.split("\\")
    components = [
        component
        if component in {"", ".", ".."}
        else component.rstrip(" .")
        for component in components
    ]
    return drive + "\\".join(components)


def _path_key(path: Path) -> str:
    """Canonical comparison key for path aliases, including Windows case."""
    resolved = os.fspath(path.resolve(strict=False))
    if os.name == "nt":
        resolved = _win32_alias_path(resolved)
    return os.path.normcase(os.path.normpath(resolved))


def _reject_alternate_stream(path: Path, role: str) -> None:
    if os.name != "nt":
        return
    normalized = _win32_alias_path(os.fspath(path))
    _, tail = os.path.splitdrive(normalized)
    if ":" in tail:
        raise GraphAuditError(
            f"path collision risk: alternate data streams are not supported "
            f"for {role}: {path}"
        )


def _resolved_path(value: str, root: str, role: str) -> Path:
    path = Path(value)
    if path.is_absolute():
        candidate = path.resolve(strict=False)
    else:
        root_path = Path(root).resolve(strict=False)
        candidate = (root_path / path).resolve(strict=False)
        root_key = _path_key(root_path)
        candidate_key = _path_key(candidate)
        try:
            confined = os.path.commonpath((root_key, candidate_key)) == root_key
        except ValueError:
            confined = False
        if not confined:
            raise GraphAuditError(
                f"relative {role} path escapes {root_path}: {value}"
            )
    _reject_alternate_stream(candidate, role)
    return candidate


def _output_path(value: str) -> Path:
    return _resolved_path(value, wikilib.scratch_dir(ensure=False), "output")


def _input_path(value: str) -> Path:
    return _resolved_path(value, wikilib.repo_root(), "input")


def _reject_path_collisions(named_paths: list[tuple[str, Path]]) -> None:
    seen: list[tuple[str, str, Path]] = []
    for name, path in named_paths:
        key = _path_key(path)
        for prior_key, prior_name, prior_path in seen:
            same_existing_file = False
            try:
                same_existing_file = os.path.samefile(prior_path, path)
            except OSError:
                pass
            if key == prior_key or same_existing_file:
                raise GraphAuditError(
                    f"path collision: {prior_name} and {name} resolve to {path}"
                )
        seen.append((key, name, path))


def _read_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        payload = json.load(handle)
    if not isinstance(payload, dict):
        raise GraphAuditError(f"JSON report must be an object: {path}")
    return payload


def _write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(
        prefix=f".{path.name}.", suffix=".tmp", dir=path.parent
    )
    try:
        handle = os.fdopen(descriptor, "w", encoding="utf-8", newline="\n")
        descriptor = -1
        with handle:
            json.dump(payload, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        if descriptor >= 0:
            os.close(descriptor)
        if os.path.exists(temporary):
            os.unlink(temporary)


def _metrics_line(
    prefix: str,
    graph: dict,
    deltas: dict | None = None,
    member_count: int | None = None,
) -> str:
    metrics = graph["metrics"]
    rendered = (
        f"{prefix} members={member_count if member_count is not None else '-'} "
        f"edges={metrics['induced_edge_count']}/{metrics['possible_edge_count']} "
        f"cohesion={metrics['local_cohesion']:.17g} "
        f"components={metrics['component_count']} largest={metrics['largest_component_size']} "
        f"isolates={metrics['isolate_count']} weak={metrics['weak_member_count']} "
        f"bridges={metrics['bridge_edge_count']}"
    )
    if deltas is not None:
        rendered += (
            f" delta_edges={deltas['induced_edge_count']:+d}"
            f" delta_components={deltas['component_count']:+d}"
            f" delta_isolates={deltas['isolate_count']:+d}"
            f" delta_weak={deltas['weak_member_count']:+d}"
        )
    return rendered


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        if args.command == "snapshot":
            if (args.observed_ui_pages is None) != (
                args.observed_ui_cohesion is None
            ):
                raise GraphAuditError(
                    "observed UI pages and cohesion must be provided together"
                )
            json_output = _output_path(args.json)
            ledger_output = _output_path(args.ledger) if args.ledger else None
            output_paths = [("--json", json_output)]
            if ledger_output is not None:
                output_paths.append(("--ledger", ledger_output))
            _reject_path_collisions(output_paths)
            snapshot = build_snapshot(
                wikilib.wiki_page_index(),
                created=args.created,
                label=args.label,
                weak_degree=args.weak_degree,
                exclusions=set(args.exclude),
                observed_ui_pages=args.observed_ui_pages,
                observed_ui_cohesion=args.observed_ui_cohesion,
            )
            ledger = build_coverage_ledger(snapshot) if args.ledger else None
            _write_json(json_output, snapshot)
            if ledger_output is not None:
                _write_json(ledger_output, ledger)
            print(
                _metrics_line(
                    "SNAPSHOT",
                    snapshot["graph"],
                    member_count=snapshot["cohort"]["member_count"],
                )
            )
            return 0

        baseline_input = _input_path(args.baseline)
        json_output = _output_path(args.json)
        ledger_path = _input_path(args.ledger) if args.ledger else None
        compare_paths = [
            ("--baseline", baseline_input),
            ("--json", json_output),
        ]
        if ledger_path is not None:
            compare_paths.append(("--ledger", ledger_path))
        _reject_path_collisions(compare_paths)
        baseline = _read_json(baseline_input)
        comparison = build_comparison(
            baseline,
            wikilib.wiki_page_index(),
            baseline_path=args.baseline,
        )
        refreshed_ledger = None
        if ledger_path is not None:
            refreshed_ledger = refresh_coverage_ledger(
                _read_json(ledger_path), comparison
            )
        _write_json(json_output, comparison)
        if ledger_path is not None:
            _write_json(ledger_path, refreshed_ledger)
        print(
            _metrics_line(
                "COMPARE",
                comparison["graph"],
                comparison["comparison"]["metric_deltas"],
                comparison["cohort"]["member_count"],
            )
        )
        return 0
    except (GraphAuditError, OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"graph_audit: error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
