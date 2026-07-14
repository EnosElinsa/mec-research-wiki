# Research Log Cohesion Improvement Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a reproducible graph audit for the frozen Research Log core, then add parse-grounded core-to-core links and analytical navigation until the repository and LLM Wiki meet the approved cohesion acceptance criteria.

**Architecture:** A standard-library Python CLI freezes the 286-page cohort and compares every later tree against that immutable membership. Five sequential evidence batches add direct semantic relationships among frozen members, plus derived synthesis/comparison pages and reciprocal navigation; a gitignored coverage ledger accounts for every member. Each accepted batch passes independent evidence review, repository gates, graph gates, a scoped commit, a push, and remote-SHA verification before the next batch begins.

**Tech Stack:** Python 3.14 standard library (`argparse`, `hashlib`, `json`, `unittest`), Markdown/YAML frontmatter, Obsidian wikilinks, PowerShell, Git, and the local LLM Wiki UI/API.

---

## Approved baseline and acceptance contract

The implementation begins from commit `6e174c54ff7be11ab3dffd35c7153f0150b4fb8e`. A read-only independent reproduction found:

- 286 frozen members selected by `created: 2026-07-14`;
- 341 unique induced undirected edges from 40,755 possible edges;
- local cohesion `0.008367071524966262`;
- 47 connected components, largest component 68;
- 1 isolate, 87 members with internal degree at most 1, and 100 bridges;
- canonical member hash `af0f4c50eb67112a33c321852b2be9bd8e9a78ab693de97f2bfee8aedf242752`.

The maintained tool must recompute these figures before wiki edits. Its generated baseline is authoritative if any value differs. Program acceptance is relative to that generated baseline:

- internal induced edges increase by at least 25%;
- component count decreases by at least 25%;
- degree-zero-or-one members decrease by at least 50%;
- every member is `linked`, `derived`, or `deferred` with evidence or a concrete reason;
- all repository gates pass and every accepted commit is present on `origin/main`;
- after an LLM Wiki rescan, the Research Log sparse-cluster card is absent or displays cohesion greater than `0.03`.

New analytical pages are outside the frozen membership even when their frontmatter date is `2026-07-14`. Links to them improve navigation and external degree, but do not count toward the internal-edge threshold. Every theme must therefore add justified direct relationships among pre-existing frozen members.

## File responsibility map

| File | Responsibility |
|---|---|
| `tools/wiki/wikilib.py` | Unique wiki-basename index, path-qualified wikilink resolution, and collapsed undirected wiki edges. |
| `tools/wiki/graph_audit.py` | Snapshot/compare CLI, graph algorithms, schema validation, report paths, and initial coverage-ledger generation. |
| `tools/wiki/tests/test_graph_audit.py` | Unit and CLI regression coverage for all approved graph semantics and failure modes. |
| `tools/wiki/README.md` | User-facing commands, JSON/ledger semantics, exit behavior, and the baseline/compare workflow. |
| `.curation-out/research-log-2026-07-14-baseline.json` | Immutable local baseline report; gitignored, retained for the full program. |
| `.curation-out/research-log-2026-07-14-ledger.json` | Mutable local coverage ledger; gitignored, refreshed after each batch. |
| `.curation-out/research-log-theme-*-evidence.md` | Parse locators, claim/edge rationales, assumptions, caveats, and verdicts for one theme. |
| `.curation-out/research-log-theme-*-after.json` | Cumulative graph comparison after one theme. |
| `wiki/synthesis/*.md`, `wiki/comparisons/*.md` | Evidence-earned analytical outputs. |
| Named `wiki/sources/*.md` and `wiki/concepts/*.md` files | Direct frozen-core links, narrowly corrected raw-artifact paths, and reciprocal analytical navigation. |
| `wiki/index.md` | Catalogue every new analytical page exactly once. |
| `wiki/overview.md` | Durable reader navigation and mechanically refreshed inventory counts only. |
| `wiki/log.md` | One dated run record per accepted batch; no run narration elsewhere. |

## Global execution rules

- Use one repository-owning coordinator for all wiki, navigation, ledger, Git, and push writes.
- Workers are read-only evidence reviewers unless the coordinator assigns a non-overlapping file explicitly.
- Read the current raw parse for every factual claim. Curated source pages locate evidence but are not the factual authority.
- Record one evidence-matrix row for every proposed claim and every proposed core-to-core edge.
- Accept an edge only when the two pages share a specific mechanism, assumption, constraint, metric contrast, or dependency. “Same topic” is not a rationale.
- Do not rank numeric results across incompatible systems, metrics, channel models, horizons, or solver evidence.
- Never change frozen membership after the baseline is written.
- Never stage `.curation-out/`, unrelated user work, or generated credentials.
- Stop before overwriting overlapping user edits. Never force-push or rewrite published history.
- If evidence workers return rate limits or stream failures, reduce concurrency or serialize; never weaken the evidence gate.
- On a non-fast-forward push, fetch and rebase once, rerun the full batch gates, and retry once. If a push is ambiguous, compare local, tracking, and `git ls-remote` SHAs before retrying.
- If an HTTPS push names an unexpected account, inspect `git credential fill` for this remote before changing authentication state.

### Task 1: Publish the approved preparatory commits

**Files:**

- Create/commit: `docs/superpowers/plans/2026-07-14-research-log-cohesion.md`

- [ ] **Step 1: Confirm the branch contains the approved local commits and preserve unrelated work**

Run:

```powershell
git status --short --branch
git log --oneline origin/main..HEAD
git diff --check origin/main..HEAD
```

Expected:

```text
## main...origin/main [ahead 3]
6e174c54f Design Research Log cohesion improvement program
17e368527 Refine MEC wiki agent roles and workflows
afe6d6729 Add project-scoped MEC wiki Codex agents
```

The plan directory is untracked at handoff. A line-ending-only user change was also observed in `wiki/synthesis/drl-backbones-across-uav-mec-sources.md`; preserve it if still present. `git diff --check origin/main..HEAD` must print nothing.

- [ ] **Step 2: Commit only the reviewed implementation plan**

Run:

```powershell
git add docs/superpowers/plans/2026-07-14-research-log-cohesion.md
git diff --cached --name-only
git diff --cached --check
git commit -m "Plan Research Log cohesion improvement program"
```

Expected staged path: exactly the implementation plan. The unrelated wiki change remains unstaged.

- [ ] **Step 3: Fetch and require a fast-forward publication**

Run:

```powershell
git fetch origin main
git merge-base --is-ancestor origin/main HEAD
if ($LASTEXITCODE -ne 0) { throw "origin/main is not an ancestor of HEAD" }
```

Expected: exit code `0`.

- [ ] **Step 4: Push and verify all three SHA views**

Run:

```powershell
git push origin main
git fetch origin main
$head = (git rev-parse HEAD).Trim()
$tracking = (git rev-parse '@{upstream}').Trim()
$remote = ((git ls-remote origin refs/heads/main) -split '\s+')[0]
if ($head -ne $tracking -or $head -ne $remote) {
    throw "SHA mismatch: HEAD=$head tracking=$tracking remote=$remote"
}
$head
```

Expected: all three values equal the new implementation-plan commit SHA.

### Task 2: Build and freeze the graph-audit foundation

**Files:**

- Modify: `tools/wiki/wikilib.py` after `page_slugs()`
- Create: `tools/wiki/graph_audit.py`
- Create: `tools/wiki/tests/test_graph_audit.py`
- Modify: `tools/wiki/README.md` in the script table, JSON-output section, and recommended workflow
- Generate, do not stage: `.curation-out/research-log-2026-07-14-baseline.json`
- Generate, do not stage: `.curation-out/research-log-2026-07-14-ledger.json`
- Generate, do not stage: `.curation-out/research-log-2026-07-14-after.json`

- [ ] **Step 1: Record the pre-foundation state**

Run:

```powershell
git status --short --branch
python --version
python -m unittest discover -s tools/wiki/tests -p "test_*.py" -v
```

Expected: `main` matches its verified remote after Task 1, Python `3.14.x`, and the existing 12 tests report `OK`. Any recorded unrelated user path may remain modified, but no `tools/wiki/` foundation path may already be dirty.

- [ ] **Step 2: Create the complete failing graph test module**

Create `tools/wiki/tests/test_graph_audit.py` with:

```python
from __future__ import annotations

import copy
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


class GraphAuditTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = pathlib.Path(self.temp.name)
        self.wiki = self.root / "wiki"
        self.scratch = self.root / ".curation-out"
        self.raw = self.root / "raw" / "sources"
        self.wiki.mkdir()
        self.raw.mkdir(parents=True)
        self._fixture()

    def tearDown(self):
        self.temp.cleanup()

    def _page(
        self,
        relative: str,
        *,
        created: str = "2026-07-14",
        body: str = "",
    ) -> pathlib.Path:
        path = self.wiki / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        page_type = {
            "sources": "source",
            "concepts": "concept",
            "synthesis": "synthesis",
        }.get(path.parent.name, "concept")
        path.write_text(
            "---\n"
            f"type: {page_type}\n"
            f"title: \"{path.stem}\"\n"
            "tags: [test]\n"
            f"created: {created}\n"
            f"updated: {created}\n"
            "---\n\n"
            f"# {path.stem}\n\n{body}\n",
            encoding="utf-8",
        )
        return path

    def _fixture(self):
        self._page(
            "sources/a.md",
            body="[[concepts/b|B]] [[b]] [[a]] [[old]]",
        )
        self._page("concepts/b.md", body="[[a]] [[c]]")
        self._page("concepts/c.md")
        self._page("concepts/d.md")
        self._page("concepts/old.md", created="2026-07-13", body="[[a]]")
        (self.wiki / "index.md").write_text("[[d]]\n", encoding="utf-8")
        (self.wiki / "overview.md").write_text("[[a]]\n", encoding="utf-8")
        (self.wiki / "log.md").write_text("[[c]]\n", encoding="utf-8")
        (self.raw / "raw-only.md").write_text("[[d]]\n", encoding="utf-8")

    def _pages(self) -> dict[str, str]:
        return wikilib.wiki_page_index(str(self.wiki))

    def _snapshot(self) -> dict[str, object]:
        return graph_audit.build_snapshot(
            self._pages(),
            created="2026-07-14",
            label="fixture",
            weak_degree=1,
            observed_ui_pages=323,
            observed_ui_cohesion=0.03,
        )

    def test_wiki_scope_and_simple_undirected_edges(self):
        pages = self._pages()
        edges = wikilib.wiki_undirected_edges(
            pages, excluded=set(graph_audit.DEFAULT_EXCLUSIONS)
        )
        self.assertEqual(
            edges,
            {("a", "b"), ("a", "old"), ("b", "c")},
        )
        self.assertNotIn("raw-only", pages)

    def test_snapshot_metrics_and_ui_observation_are_separate(self):
        report = self._snapshot()
        metrics = report["graph"]["metrics"]
        self.assertEqual(report["cohort"]["members"], ["a", "b", "c", "d"])
        self.assertEqual(metrics["induced_edge_count"], 2)
        self.assertEqual(metrics["possible_edge_count"], 6)
        self.assertAlmostEqual(metrics["local_cohesion"], 1 / 3)
        self.assertEqual(metrics["component_count"], 2)
        self.assertEqual(metrics["largest_component_size"], 3)
        self.assertEqual(metrics["isolate_count"], 1)
        self.assertEqual(metrics["weak_member_count"], 3)
        self.assertEqual(metrics["bridge_edge_count"], 2)
        self.assertEqual(report["graph"]["external_degrees"]["a"], 1)
        self.assertEqual(
            report["external_observation"],
            {"source": "LLM Wiki UI", "pages": 323, "cohesion": 0.03},
        )
        self.assertNotIn("observed_ui_cohesion", metrics)

    def test_comparison_reuses_frozen_membership_and_reports_deltas(self):
        baseline = self._snapshot()
        self._page("concepts/e.md", body="[[d]]")
        self._page("sources/a.md", body="[[b]] [[c]] [[old]]")
        self._page("concepts/b.md", body="[[a]]")
        self._page("concepts/c.md", body="[[a]] [[d]]")
        self._page("concepts/d.md", body="[[c]]")

        comparison = graph_audit.build_comparison(
            baseline,
            self._pages(),
            baseline_path=".curation-out/baseline.json",
        )

        self.assertEqual(comparison["cohort"]["members"], ["a", "b", "c", "d"])
        self.assertNotIn("e", comparison["cohort"]["members"])
        self.assertEqual(
            comparison["comparison"]["added_edges"],
            [["a", "c"], ["c", "d"]],
        )
        self.assertEqual(
            comparison["comparison"]["removed_edges"],
            [["b", "c"]],
        )
        self.assertEqual(
            comparison["comparison"]["metric_deltas"]["induced_edge_count"], 1
        )
        self.assertEqual(
            comparison["comparison"]["metric_deltas"]["component_count"], -1
        )
        self.assertEqual(
            comparison["comparison"]["metric_deltas"]["isolate_count"], -1
        )
        self.assertEqual(
            comparison["comparison"]["metric_deltas"]["weak_member_count"], -1
        )
        self.assertEqual(
            comparison["comparison"]["internal_degree_deltas"],
            {"a": 1, "b": -1, "c": 1, "d": 1},
        )

    def test_compare_rejects_a_missing_frozen_member(self):
        baseline = self._snapshot()
        (self.wiki / "concepts" / "d.md").unlink()
        with self.assertRaisesRegex(
            graph_audit.GraphAuditError,
            r"missing frozen member\(s\): d",
        ):
            graph_audit.build_comparison(
                baseline,
                self._pages(),
                baseline_path=".curation-out/baseline.json",
            )

    def test_duplicate_wiki_basenames_fail_closed(self):
        self._page("synthesis/a.md")
        with self.assertRaisesRegex(ValueError, "duplicate wiki basename"):
            self._pages()

    def test_snapshot_validation_rejects_a_corrupt_member_hash(self):
        corrupt = copy.deepcopy(self._snapshot())
        corrupt["cohort"]["member_hash"] = "0" * 64
        with self.assertRaisesRegex(
            graph_audit.GraphAuditError, "member hash mismatch"
        ):
            graph_audit.validate_snapshot(corrupt)

    def test_comparison_refreshes_post_batch_ledger_degrees(self):
        baseline = self._snapshot()
        ledger = graph_audit.build_coverage_ledger(baseline)
        self._page("sources/a.md", body="[[b]] [[c]] [[old]]")
        comparison = graph_audit.build_comparison(
            baseline,
            self._pages(),
            baseline_path=".curation-out/baseline.json",
        )
        refreshed = graph_audit.refresh_coverage_ledger(
            ledger,
            comparison,
        )
        rows = {row["slug"]: row for row in refreshed["entries"]}
        self.assertEqual(rows["a"]["post_batch_internal_degree"], 2)
        self.assertEqual(rows["c"]["post_batch_internal_degree"], 2)
        # unittest creates a fresh fixture; this test never links isolate d.
        self.assertEqual(rows["d"]["post_batch_component"], 2)

    def test_relative_json_and_ledger_paths_land_in_scratch(self):
        with (
            mock.patch.object(wikilib, "wiki_dir", return_value=str(self.wiki)),
            mock.patch.object(
                wikilib, "scratch_dir", return_value=str(self.scratch)
            ),
        ):
            code = graph_audit.main(
                [
                    "snapshot",
                    "--created",
                    "2026-07-14",
                    "--label",
                    "fixture",
                    "--json",
                    "snapshot.json",
                    "--ledger",
                    "ledger.json",
                ]
            )
        self.assertEqual(code, 0)
        snapshot = json.loads(
            (self.scratch / "snapshot.json").read_text(encoding="utf-8")
        )
        ledger = json.loads(
            (self.scratch / "ledger.json").read_text(encoding="utf-8")
        )
        self.assertEqual(snapshot["cohort"]["member_count"], 4)
        self.assertEqual(len(ledger["entries"]), 4)
        self.assertEqual({row["status"] for row in ledger["entries"]}, {"pending"})


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 3: Run the new tests and observe the red state**

Run:

```powershell
python -m unittest tools.wiki.tests.test_graph_audit -v
```

Expected: `ERROR` because `graph_audit` does not exist.

- [ ] **Step 4: Add the exact wiki graph primitives**

Insert this block after `page_slugs()` in `tools/wiki/wikilib.py`:

```python
def wiki_page_index(root: str | None = None) -> dict[str, str]:
    """Map every wiki Markdown basename to one path, failing on ambiguity."""
    root = root or wiki_dir()
    grouped: dict[str, list[str]] = {}
    for path in md_files(root):
        slug = os.path.splitext(os.path.basename(path))[0]
        grouped.setdefault(slug, []).append(path)
    duplicates = {
        slug: sorted(paths)
        for slug, paths in grouped.items()
        if len(paths) > 1
    }
    if duplicates:
        details = "; ".join(
            f"{slug}: {', '.join(paths)}"
            for slug, paths in sorted(duplicates.items())
        )
        raise ValueError(f"duplicate wiki basename(s): {details}")
    return {
        slug: paths[0]
        for slug, paths in sorted(grouped.items())
    }


def wikilink_basename(target: str) -> str:
    """Return the Obsidian basename for a path-qualified wikilink target."""
    normalized = target.replace("\\", "/").rstrip("/")
    name = os.path.basename(normalized)
    return os.path.splitext(name)[0]


def wiki_undirected_edges(
    pages: dict[str, str] | None = None,
    *,
    excluded: set[str] | frozenset[str] | None = None,
) -> set[tuple[str, str]]:
    """Return unique resolved non-self undirected edges inside ``wiki/``."""
    if pages is None:
        pages = wiki_page_index()
    excluded = set(excluded or ())
    edges: set[tuple[str, str]] = set()
    for source, path in pages.items():
        if source in excluded:
            continue
        for raw_target in iter_wikilinks(read_text(path)):
            target = wikilink_basename(raw_target)
            if (
                target not in pages
                or target in excluded
                or target == source
            ):
                continue
            edges.add(tuple(sorted((source, target))))
    return edges
```

- [ ] **Step 5: Create the complete graph CLI implementation**

Create `tools/wiki/graph_audit.py` with:

```python
#!/usr/bin/env python3
"""Freeze and compare a reproducible semantic graph cohort under ``wiki/``."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import sys
from pathlib import Path

import wikilib


SCHEMA_VERSION = 1
DEFAULT_EXCLUSIONS = frozenset({"index", "log", "overview"})
_FRONTMATTER = re.compile(
    r"^\ufeff?---\s*\r?\n(.*?)\r?\n---\s*(?:\r?\n|$)",
    re.S,
)
_TYPE_BY_DIR = {
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


class GraphAuditError(ValueError):
    """Raised when graph inputs or frozen snapshots are invalid."""


def frontmatter_created(text: str) -> str | None:
    match = _FRONTMATTER.match(text)
    if not match:
        return None
    scalar = re.search(r"(?m)^created:\s*(.*?)\s*$", match.group(1))
    if not scalar:
        return None
    return scalar.group(1).strip().strip("'\"")


def cohort_hash(members: list[str]) -> str:
    canonical = json.dumps(
        members,
        ensure_ascii=False,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(canonical).hexdigest()


def select_created_members(
    pages: dict[str, str],
    created: str,
    exclusions: frozenset[str],
) -> list[str]:
    return sorted(
        slug
        for slug, path in pages.items()
        if slug not in exclusions
        and frontmatter_created(wikilib.read_text(path)) == created
    )


def _neighbors(
    members: list[str],
    induced_edges: set[tuple[str, str]],
) -> dict[str, set[str]]:
    out = {slug: set() for slug in members}
    for left, right in induced_edges:
        out[left].add(right)
        out[right].add(left)
    return out


def _components(neighbors: dict[str, set[str]]) -> list[list[str]]:
    remaining = set(neighbors)
    found: list[list[str]] = []
    while remaining:
        start = min(remaining)
        stack = [start]
        component: list[str] = []
        remaining.remove(start)
        while stack:
            current = stack.pop()
            component.append(current)
            for neighbor in sorted(neighbors[current], reverse=True):
                if neighbor in remaining:
                    remaining.remove(neighbor)
                    stack.append(neighbor)
        found.append(sorted(component))
    return sorted(found, key=lambda group: (-len(group), group))


def _bridges(neighbors: dict[str, set[str]]) -> list[list[str]]:
    discovery: dict[str, int] = {}
    low: dict[str, int] = {}
    parent: dict[str, str | None] = {}
    bridges: set[tuple[str, str]] = set()
    tick = 0

    def visit(node: str) -> None:
        nonlocal tick
        tick += 1
        discovery[node] = tick
        low[node] = tick
        for neighbor in sorted(neighbors[node]):
            if neighbor not in discovery:
                parent[neighbor] = node
                visit(neighbor)
                low[node] = min(low[node], low[neighbor])
                if low[neighbor] > discovery[node]:
                    bridges.add(tuple(sorted((node, neighbor))))
            elif parent.get(node) != neighbor:
                low[node] = min(low[node], discovery[neighbor])

    for node in sorted(neighbors):
        if node not in discovery:
            parent[node] = None
            visit(node)
    return [list(edge) for edge in sorted(bridges)]


def graph_payload(
    members: list[str],
    all_edges: set[tuple[str, str]],
    weak_degree: int,
) -> dict[str, object]:
    member_set = set(members)
    induced = {
        edge
        for edge in all_edges
        if edge[0] in member_set and edge[1] in member_set
    }
    neighbors = _neighbors(members, induced)
    components = _components(neighbors)
    internal_degrees = {
        slug: len(neighbors[slug])
        for slug in members
    }
    external_degrees = {slug: 0 for slug in members}
    for left, right in all_edges:
        if left in member_set and right not in member_set:
            external_degrees[left] += 1
        elif right in member_set and left not in member_set:
            external_degrees[right] += 1
    possible = len(members) * (len(members) - 1) // 2
    bridges = _bridges(neighbors)
    isolates = [
        slug
        for slug in members
        if internal_degrees[slug] == 0
    ]
    weak = [
        {"slug": slug, "internal_degree": internal_degrees[slug]}
        for slug in members
        if internal_degrees[slug] <= weak_degree
    ]
    component_rows = [
        {"id": index, "size": len(group), "members": group}
        for index, group in enumerate(components, start=1)
    ]
    return {
        "metrics": {
            "induced_edge_count": len(induced),
            "possible_edge_count": possible,
            "local_cohesion": len(induced) / possible if possible else 0.0,
            "component_count": len(components),
            "largest_component_size": max(
                (len(group) for group in components),
                default=0,
            ),
            "isolate_count": len(isolates),
            "weak_member_count": len(weak),
            "bridge_edge_count": len(bridges),
        },
        "internal_degrees": internal_degrees,
        "external_degrees": external_degrees,
        "induced_edges": [list(edge) for edge in sorted(induced)],
        "components": component_rows,
        "isolates": isolates,
        "weak_members": weak,
        "bridge_edges": bridges,
    }


def build_snapshot(
    pages: dict[str, str],
    *,
    created: str,
    label: str,
    weak_degree: int = 1,
    exclusions: frozenset[str] = DEFAULT_EXCLUSIONS,
    observed_ui_pages: int | None = None,
    observed_ui_cohesion: float | None = None,
) -> dict[str, object]:
    exclusions = frozenset(set(exclusions) | set(DEFAULT_EXCLUSIONS))
    members = select_created_members(pages, created, exclusions)
    all_edges = wikilib.wiki_undirected_edges(
        pages,
        excluded=set(exclusions),
    )
    member_types = {
        slug: _TYPE_BY_DIR.get(
            os.path.basename(os.path.dirname(pages[slug])),
            "untyped",
        )
        for slug in members
    }
    observation = None
    if observed_ui_pages is not None:
        observation = {
            "source": "LLM Wiki UI",
            "pages": observed_ui_pages,
            "cohesion": observed_ui_cohesion,
        }
    return {
        "schema_version": SCHEMA_VERSION,
        "report_type": "snapshot",
        "generated_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "label": label,
        "graph_semantics": {
            "scope": "recursive Markdown files under wiki/",
            "resolution": "unique-wiki-basename",
            "directed": False,
            "simple": True,
            "self_links": "excluded",
            "unresolved_links": "excluded",
            "cohesion_formula": "induced_edges / (n * (n - 1) / 2)",
        },
        "parameters": {
            "weak_degree": weak_degree,
            "exclusions": sorted(exclusions),
        },
        "cohort": {
            "selector": {"created": created},
            "members": members,
            "member_types": member_types,
            "member_count": len(members),
            "member_hash_algorithm": "sha256-canonical-json",
            "member_hash": cohort_hash(members),
        },
        "external_observation": observation,
        "graph": graph_payload(members, all_edges, weak_degree),
    }


def validate_snapshot(payload: object) -> dict[str, object]:
    if not isinstance(payload, dict):
        raise GraphAuditError("snapshot must be a JSON object")
    if payload.get("schema_version") != SCHEMA_VERSION:
        raise GraphAuditError("unsupported snapshot schema")
    if payload.get("report_type") != "snapshot":
        raise GraphAuditError("baseline report_type must be snapshot")
    cohort = payload.get("cohort")
    parameters = payload.get("parameters")
    graph = payload.get("graph")
    if not isinstance(cohort, dict) or not isinstance(parameters, dict):
        raise GraphAuditError("snapshot is missing cohort or parameters")
    if not isinstance(graph, dict):
        raise GraphAuditError("snapshot is missing graph")
    members = cohort.get("members")
    if (
        not isinstance(members, list)
        or not all(isinstance(slug, str) and slug for slug in members)
        or members != sorted(set(members))
    ):
        raise GraphAuditError("cohort members must be sorted unique slugs")
    if cohort.get("member_count") != len(members):
        raise GraphAuditError("member count mismatch")
    if cohort.get("member_hash") != cohort_hash(members):
        raise GraphAuditError("member hash mismatch")
    member_types = cohort.get("member_types")
    if not isinstance(member_types, dict) or set(member_types) != set(members):
        raise GraphAuditError("member type coverage mismatch")
    exclusions = parameters.get("exclusions")
    weak_degree = parameters.get("weak_degree")
    if (
        not isinstance(exclusions, list)
        or not DEFAULT_EXCLUSIONS.issubset(exclusions)
    ):
        raise GraphAuditError("required administrative exclusions are missing")
    if not isinstance(weak_degree, int) or weak_degree < 0:
        raise GraphAuditError("weak_degree must be a non-negative integer")
    edge_rows = graph.get("induced_edges")
    if not isinstance(edge_rows, list):
        raise GraphAuditError("induced_edges must be a list")
    edges: set[tuple[str, str]] = set()
    for row in edge_rows:
        if (
            not isinstance(row, list)
            or len(row) != 2
            or not all(isinstance(slug, str) for slug in row)
            or row[0] >= row[1]
            or row[0] not in members
            or row[1] not in members
        ):
            raise GraphAuditError("invalid induced edge")
        edges.add((row[0], row[1]))
    if len(edges) != len(edge_rows):
        raise GraphAuditError("duplicate induced edge")
    recomputed = graph_payload(members, edges, weak_degree)
    for key in (
        "metrics",
        "internal_degrees",
        "components",
        "isolates",
        "weak_members",
        "bridge_edges",
    ):
        if graph.get(key) != recomputed[key]:
            raise GraphAuditError(f"snapshot {key} mismatch")
    external = graph.get("external_degrees")
    if (
        not isinstance(external, dict)
        or set(external) != set(members)
        or any(
            not isinstance(value, int) or value < 0
            for value in external.values()
        )
    ):
        raise GraphAuditError("invalid external degree coverage")
    return payload


def build_comparison(
    baseline: dict[str, object],
    pages: dict[str, str],
    *,
    baseline_path: str,
) -> dict[str, object]:
    baseline = validate_snapshot(baseline)
    members = baseline["cohort"]["members"]
    missing = sorted(set(members) - set(pages))
    if missing:
        raise GraphAuditError(
            "missing frozen member(s): " + ", ".join(missing)
        )
    weak_degree = baseline["parameters"]["weak_degree"]
    exclusions = set(baseline["parameters"]["exclusions"])
    all_edges = wikilib.wiki_undirected_edges(
        pages,
        excluded=exclusions,
    )
    current_graph = graph_payload(members, all_edges, weak_degree)
    old_graph = baseline["graph"]
    old_edges = {
        tuple(row)
        for row in old_graph["induced_edges"]
    }
    new_edges = {
        tuple(row)
        for row in current_graph["induced_edges"]
    }
    metric_deltas = {
        key: current_graph["metrics"][key] - value
        for key, value in old_graph["metrics"].items()
    }
    internal_deltas = {
        slug: (
            current_graph["internal_degrees"][slug]
            - old_graph["internal_degrees"][slug]
        )
        for slug in members
    }
    external_deltas = {
        slug: (
            current_graph["external_degrees"][slug]
            - old_graph["external_degrees"][slug]
        )
        for slug in members
    }
    return {
        "schema_version": SCHEMA_VERSION,
        "report_type": "comparison",
        "generated_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "label": baseline["label"],
        "graph_semantics": baseline["graph_semantics"],
        "parameters": baseline["parameters"],
        "cohort": baseline["cohort"],
        "external_observation": baseline["external_observation"],
        "graph": current_graph,
        "baseline": {
            "path": baseline_path,
            "metrics": old_graph["metrics"],
        },
        "comparison": {
            "metric_deltas": metric_deltas,
            "internal_degree_deltas": internal_deltas,
            "external_degree_deltas": external_deltas,
            "added_edges": [
                list(edge)
                for edge in sorted(new_edges - old_edges)
            ],
            "removed_edges": [
                list(edge)
                for edge in sorted(old_edges - new_edges)
            ],
        },
    }


def build_coverage_ledger(
    snapshot: dict[str, object],
) -> dict[str, object]:
    snapshot = validate_snapshot(snapshot)
    component_by_slug: dict[str, int] = {}
    for component in snapshot["graph"]["components"]:
        for slug in component["members"]:
            component_by_slug[slug] = component["id"]
    entries = []
    for slug in snapshot["cohort"]["members"]:
        entries.append(
            {
                "slug": slug,
                "type": snapshot["cohort"]["member_types"][slug],
                "baseline_component": component_by_slug[slug],
                "baseline_internal_degree": (
                    snapshot["graph"]["internal_degrees"][slug]
                ),
                "theme": None,
                "status": "pending",
                "evidence_paths": [],
                "candidate_relationships": [],
                "accepted_links": [],
                "deferral_reason": None,
                "post_batch_internal_degree": (
                    snapshot["graph"]["internal_degrees"][slug]
                ),
            }
        )
    return {
        "schema_version": SCHEMA_VERSION,
        "report_type": "coverage-ledger",
        "baseline_label": snapshot["label"],
        "baseline_member_hash": snapshot["cohort"]["member_hash"],
        "entries": entries,
    }


def refresh_coverage_ledger(
    ledger: dict[str, object],
    comparison: dict[str, object],
) -> dict[str, object]:
    if (
        not isinstance(ledger, dict)
        or ledger.get("report_type") != "coverage-ledger"
    ):
        raise GraphAuditError("invalid coverage ledger")
    if (
        ledger.get("baseline_member_hash")
        != comparison["cohort"]["member_hash"]
    ):
        raise GraphAuditError("coverage ledger member hash mismatch")
    entries = ledger.get("entries")
    if not isinstance(entries, list):
        raise GraphAuditError("coverage ledger entries must be a list")
    by_slug = {
        row.get("slug"): row
        for row in entries
        if isinstance(row, dict)
    }
    members = comparison["cohort"]["members"]
    if set(by_slug) != set(members):
        raise GraphAuditError("coverage ledger member coverage mismatch")
    component_by_slug: dict[str, int] = {}
    for component in comparison["graph"]["components"]:
        for slug in component["members"]:
            component_by_slug[slug] = component["id"]
    for slug in members:
        by_slug[slug]["post_batch_component"] = component_by_slug[slug]
        by_slug[slug]["post_batch_internal_degree"] = (
            comparison["graph"]["internal_degrees"][slug]
        )
    ledger["last_comparison_generated_at_utc"] = (
        comparison["generated_at_utc"]
    )
    return ledger


def _resolve_output(raw_path: str) -> Path:
    path = Path(raw_path)
    if not path.is_absolute():
        path = Path(wikilib.scratch_dir()) / path
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def _resolve_input(raw_path: str) -> Path:
    path = Path(raw_path)
    if not path.is_absolute():
        path = Path(wikilib.repo_root()) / path
    return path


def _write_json(path: Path, payload: dict[str, object]) -> None:
    path.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def _valid_date(value: str) -> str:
    try:
        parsed = dt.date.fromisoformat(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError(str(exc)) from exc
    if parsed.isoformat() != value:
        raise argparse.ArgumentTypeError("date must use YYYY-MM-DD")
    return value


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="operation", required=True)

    snapshot = subparsers.add_parser("snapshot")
    snapshot.add_argument("--created", required=True, type=_valid_date)
    snapshot.add_argument("--label", required=True)
    snapshot.add_argument("--weak-degree", type=int, default=1)
    snapshot.add_argument("--exclude", action="append", default=[])
    snapshot.add_argument("--observed-ui-pages", type=int)
    snapshot.add_argument("--observed-ui-cohesion", type=float)
    snapshot.add_argument("--json", required=True)
    snapshot.add_argument("--ledger")

    compare = subparsers.add_parser("compare")
    compare.add_argument("--baseline", required=True)
    compare.add_argument("--json", required=True)
    compare.add_argument("--ledger")
    return parser


def _print_metrics(payload: dict[str, object]) -> None:
    metrics = payload["graph"]["metrics"]
    print(
        "members={member_count} edges={induced_edge_count} "
        "cohesion={local_cohesion:.12f} components={component_count} "
        "isolates={isolate_count} weak={weak_member_count} "
        "bridges={bridge_edge_count}".format(
            member_count=payload["cohort"]["member_count"],
            **metrics,
        )
    )


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        pages = wikilib.wiki_page_index()
        if args.operation == "snapshot":
            if args.weak_degree < 0:
                raise GraphAuditError(
                    "weak_degree must be a non-negative integer"
                )
            ui_values = (
                args.observed_ui_pages,
                args.observed_ui_cohesion,
            )
            if (ui_values[0] is None) != (ui_values[1] is None):
                raise GraphAuditError(
                    "UI page count and cohesion must be supplied together"
                )
            if ui_values[0] is not None and ui_values[0] <= 0:
                raise GraphAuditError("observed UI pages must be positive")
            if (
                ui_values[1] is not None
                and not 0.0 <= ui_values[1] <= 1.0
            ):
                raise GraphAuditError(
                    "observed UI cohesion must be between 0 and 1"
                )
            exclusions = frozenset(
                set(DEFAULT_EXCLUSIONS) | set(args.exclude)
            )
            payload = build_snapshot(
                pages,
                created=args.created,
                label=args.label,
                weak_degree=args.weak_degree,
                exclusions=exclusions,
                observed_ui_pages=args.observed_ui_pages,
                observed_ui_cohesion=args.observed_ui_cohesion,
            )
            validate_snapshot(payload)
            _write_json(_resolve_output(args.json), payload)
            if args.ledger:
                _write_json(
                    _resolve_output(args.ledger),
                    build_coverage_ledger(payload),
                )
        else:
            baseline_path = _resolve_input(args.baseline)
            baseline = json.loads(
                baseline_path.read_text(encoding="utf-8")
            )
            payload = build_comparison(
                baseline,
                pages,
                baseline_path=args.baseline,
            )
            _write_json(_resolve_output(args.json), payload)
            if args.ledger:
                ledger_path = _resolve_input(args.ledger)
                ledger = json.loads(
                    ledger_path.read_text(encoding="utf-8")
                )
                _write_json(
                    ledger_path,
                    refresh_coverage_ledger(ledger, payload),
                )
        _print_metrics(payload)
        return 0
    except (
        GraphAuditError,
        OSError,
        ValueError,
        json.JSONDecodeError,
    ) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 6: Compile and run the focused tests**

Run:

```powershell
python -m py_compile tools/wiki/wikilib.py tools/wiki/graph_audit.py tools/wiki/tests/test_graph_audit.py
python -m unittest tools.wiki.tests.test_graph_audit -v
```

Expected: compilation succeeds and all eight `GraphAuditTests` report `ok`.

- [ ] **Step 7: Document the exact interface**

Add this row to the script table in `tools/wiki/README.md`:

```markdown
| `graph_audit.py` | Freeze a date-selected wiki-only cohort and compare later trees against its immutable membership. Uses unique wiki basenames, a simple undirected graph, and excludes `index`, `overview`, and `log`; exits 2 for invalid input/snapshots or missing frozen members, while a valid metric regression remains exit 0 for the coordinator to judge. | `snapshot --created --label --weak-degree --observed-ui-pages --observed-ui-cohesion --json [--ledger]`; `compare --baseline --json [--ledger]` |
```

Add this workflow after the README's standard gate commands:

````markdown
### Frozen-cohort graph workflow

Relative report paths are written under `.curation-out/`. The snapshot stores
the sorted member list, its canonical-JSON SHA-256, internal/external degrees,
induced edges, components, isolates, weak members, bridges, and the separately
labeled LLM Wiki UI observation. Local cohesion is:

`induced undirected edges / (n * (n - 1) / 2)`.

```powershell
python tools/wiki/graph_audit.py snapshot `
  --created 2026-07-14 `
  --label "Research Log core" `
  --weak-degree 1 `
  --observed-ui-pages 323 `
  --observed-ui-cohesion 0.03 `
  --json research-log-2026-07-14-baseline.json `
  --ledger research-log-2026-07-14-ledger.json

python tools/wiki/graph_audit.py compare `
  --baseline .curation-out/research-log-2026-07-14-baseline.json `
  --json research-log-2026-07-14-after.json `
  --ledger .curation-out/research-log-2026-07-14-ledger.json
```

Keep the baseline and ledger for the whole cohesion program. They are scratch
state and must not be staged. A comparison reuses the baseline membership,
ignores newly created pages for induced metrics, and reports every added or
removed frozen-cohort edge plus metric and degree deltas.
````

- [ ] **Step 8: Run the full Python suite**

Run:

```powershell
python -m unittest discover -s tools/wiki/tests -p "test_*.py" -v
```

Expected: the original 12 tests plus the eight new graph tests report `OK`.

- [ ] **Step 9: Freeze the baseline and initialize the ledger**

Run:

```powershell
python tools/wiki/graph_audit.py snapshot `
  --created 2026-07-14 `
  --label "Research Log core" `
  --weak-degree 1 `
  --observed-ui-pages 323 `
  --observed-ui-cohesion 0.03 `
  --json research-log-2026-07-14-baseline.json `
  --ledger research-log-2026-07-14-ledger.json
```

Expected:

```text
members=286 edges=341 cohesion=0.008367071525 components=47 isolates=1 weak=87 bridges=100
```

Open the JSON and require `cohort.member_hash` to equal `af0f4c50eb67112a33c321852b2be9bd8e9a78ab693de97f2bfee8aedf242752`. If generated values differ, stop and reconcile the current Git tree before applying the approved relative thresholds.

- [ ] **Step 10: Prove that immediate comparison is a zero delta**

Run:

```powershell
python tools/wiki/graph_audit.py compare `
  --baseline .curation-out/research-log-2026-07-14-baseline.json `
  --json research-log-2026-07-14-after.json `
  --ledger .curation-out/research-log-2026-07-14-ledger.json
```

Expected: every `comparison.metric_deltas` and degree delta is `0`, with empty `added_edges` and `removed_edges`.

- [ ] **Step 11: Run the complete foundation gates**

Run:

```powershell
python tools/wiki/curation_status.py --dupes
python tools/wiki/corpus_counts.py
python tools/wiki/linkcheck.py --orphans
python tools/wiki/process_refs.py
python tools/wiki/index_audit.py
python tools/wiki/frontmatter_audit.py
python tools/wiki/entity_roster_audit.py
python -m unittest discover -s tools/wiki/tests -p "test_*.py" -v
git diff --check
git status --short
```

Expected: uncurated count `0`, duplicate count `0`, dangling wikilinks `0`, process references `0`, index gaps/duplicate primary listings `0`, frontmatter errors `0`, tests `OK`, and no whitespace errors. Existing raw-layer orphan reporting may remain informational; no semantic wiki page may become newly orphaned.

- [ ] **Step 12: Review, stage, commit, push, and verify the foundation**

Run:

```powershell
git diff -- tools/wiki/wikilib.py tools/wiki/graph_audit.py tools/wiki/tests/test_graph_audit.py tools/wiki/README.md
rg -n -i "(api[_-]?key|token|password|secret|authorization:|bearer )" tools/wiki/wikilib.py tools/wiki/graph_audit.py tools/wiki/tests/test_graph_audit.py tools/wiki/README.md
git add tools/wiki/wikilib.py tools/wiki/graph_audit.py tools/wiki/tests/test_graph_audit.py tools/wiki/README.md
git diff --cached --name-only
git commit -m "Add frozen-cohort graph audit foundation"
git push origin main
git fetch origin main
$head = (git rev-parse HEAD).Trim()
$tracking = (git rev-parse '@{upstream}').Trim()
$remote = ((git ls-remote origin refs/heads/main) -split '\s+')[0]
if ($head -ne $tracking -or $head -ne $remote) {
    throw "SHA mismatch: HEAD=$head tracking=$tracking remote=$remote"
}
```

Expected staged paths: exactly the four maintained tool/doc files. The credential scan must show no actual credential. The commit and push must succeed, all SHA views must match, and `.curation-out/` must remain untracked.

## Evidence-batch record format

For every theme, create the named scratch evidence file with these exact sections:

```markdown
# Theme evidence matrix

## Scope

State the analytical question, included sources, excluded near-neighbors, and
the reason for each exclusion.

## Claim and edge matrix

| ID | Proposed claim or edge | Wiki endpoints | Authoritative parse path | Locator | Paper fact or cross-source inference | Assumptions | Caveat | Verdict |
|---|---|---|---|---|---|---|---|---|

## Non-comparability decisions

Record every metric, system-model, timescale, solver-evidence, or guarantee
pair that cannot support a direct numeric ranking.

## Reviewer disposition

Record the independent reviewer's accept/revise/reject decision for every ID
and the exact revision made.
```

Populate the matrix before changing wiki prose. A locator is a parse heading plus a distinctive phrase or equation/table identifier. Keep rejected rows; they explain why an attractive-looking link was not added.

For each accepted core member, update its ledger row using the established JSON keys. A linked row has this shape:

```json
{
  "slug": "hong-2026-beam-delay-alignment",
  "theme": "mobility-asynchrony-and-geometry-in-aerial-coverage",
  "status": "linked",
  "evidence_paths": [
    "raw/sources/User-Centric_Beam-Delay_Alignment_Transmission_for_Low-Altitude_Coverage_via_Wideband_Cell-Free_Massive_MIMO/User-Centric_Beam-Delay_Alignment_Transmission_for_Low-Altitude_Coverage_via_Wideband_Cell-Free_Massive_MIMO.md"
  ],
  "candidate_relationships": [
    "wang-2026-6dara-cellfree: reversed aerial-node roles and different controlled physical-layer impairments"
  ],
  "accepted_links": ["wang-2026-6dara-cellfree"],
  "deferral_reason": null
}
```

Preserve the row's generated baseline fields. `graph_audit.py compare --ledger ...` refreshes its post-batch component and degree after the editorial decision fields have been patched.

### Task 3: Synthesize mobility, asynchrony, and geometry in aerial coverage

**Files:**

- Create: `wiki/synthesis/mobility-asynchrony-and-geometry-in-aerial-coverage.md`
- Modify sources:
  - `wiki/sources/hong-2026-beam-delay-alignment.md`
  - `wiki/sources/fang-2026-cellfree-uav-predictive-beamforming.md`
  - `wiki/sources/chen-2026-traffic-aware-asynchronous-control.md`
  - `wiki/sources/shi-2026-vhetnet-comp-coverage.md`
  - `wiki/sources/ren-2026-distributed-uav-los.md`
  - `wiki/sources/wang-2026-6dara-cellfree.md`
  - `wiki/sources/jiang-2026-ray-antenna-array.md`
  - `wiki/sources/chai-2026-random-position-relay-deployment.md`
- Modify concepts when their edge rows are accepted:
  - `wiki/concepts/beam-delay-alignment-transmission.md`
  - `wiki/concepts/wideband-asynchronous-cell-free-massive-mimo.md`
  - `wiki/concepts/cell-free-uav-predictive-beamforming.md`
  - `wiki/concepts/traffic-aware-asynchronous-uav-control.md`
  - `wiki/concepts/coordinated-multipoint-transmission.md`
  - `wiki/concepts/poisson-delaunay-comp-clustering.md`
  - `wiki/concepts/same-tier-three-site-comp.md`
  - `wiki/concepts/two-regime-aerial-user-association.md`
  - `wiki/concepts/air-to-ground-channel-model.md`
  - `wiki/concepts/blockage-aware-channel-model.md`
  - `wiki/concepts/six-dimensional-aerial-rotatable-antenna-array.md`
  - `wiki/concepts/team-mmse-receive-combining.md`
  - `wiki/concepts/ray-antenna-array.md`
  - `wiki/concepts/statistical-user-position-uav-deployment.md`
- Modify navigation: `wiki/index.md`, `wiki/overview.md`, `wiki/log.md`
- Generate, do not stage: `.curation-out/research-log-theme-1-evidence.md`, `.curation-out/research-log-theme-1-after.json`
- Patch, do not stage: `.curation-out/research-log-2026-07-14-ledger.json`

- [ ] **Step 1: Reconfirm the frozen state and isolate unrelated work**

Run:

```powershell
git status --short --branch
python tools/wiki/graph_audit.py compare `
  --baseline .curation-out/research-log-2026-07-14-baseline.json `
  --json research-log-theme-1-before.json
```

Expected: member hash unchanged and zero graph delta from the baseline. Record every pre-existing unrelated worktree path and do not stage it. If an unrelated change alters a frozen member's wikilinks, pause this batch because the graph delta would no longer be attributable.

- [ ] **Step 2: Ground the eight-source evidence matrix in current parses**

Read these exact parse files and populate `.curation-out/research-log-theme-1-evidence.md`:

```text
raw/sources/User-Centric_Beam-Delay_Alignment_Transmission_for_Low-Altitude_Coverage_via_Wideband_Cell-Free_Massive_MIMO/User-Centric_Beam-Delay_Alignment_Transmission_for_Low-Altitude_Coverage_via_Wideband_Cell-Free_Massive_MIMO.md
raw/sources/Predictive_Beamforming_and_Resource_Allocation_for_High-Mobility_Cell-Free_UAV_Networks/Predictive_Beamforming_and_Resource_Allocation_for_High-Mobility_Cell-Free_UAV_Networks.md
raw/sources/Traffic-Aware_Asynchronous_Trajectory_Planning_and_Scheduling_in_UAV-Assisted_Wireless_Networks_With_Heterogeneous_Traffic_Demands/Traffic-Aware_Asynchronous_Trajectory_Planning_and_Scheduling_in_UAV-Assisted_Wireless_Networks_With_Heterogeneous_Traffic_Demands.md
raw/sources/Vertical_Heterogeneous_Networks_Beyond_5G_CoMP_Coverage_Enhancement_and_Optimization/Vertical_Heterogeneous_Networks_Beyond_5G_CoMP_Coverage_Enhancement_and_Optimization.md
raw/sources/Performance_Analysis_of_Distributed_UAVs_in_Urban_Environments_Using_a_Practical_Line-of-Sight_Model/Performance_Analysis_of_Distributed_UAVs_in_Urban_Environments_Using_a_Practical_Line-of-Sight_Model.md
raw/sources/Two-Timescale_Optimization_for_Aerial_Rotatable_Antenna_Array_in_Cell-Free_Networks_With_Dynamic_Users/Two-Timescale_Optimization_for_Aerial_Rotatable_Antenna_Array_in_Cell-Free_Networks_With_Dynamic_Users.md
raw/sources/Ray_Antenna_Array_Achieves_Uniform_Angular_Resolution_Cost-Effectively_for_Low-Altitude_UAV_Swarm_ISAC/Ray_Antenna_Array_Achieves_Uniform_Angular_Resolution_Cost-Effectively_for_Low-Altitude_UAV_Swarm_ISAC.md
raw/sources/Transmission_Time_Minimization-Based_UAV_Deployment_and_Resource_Allocation_With_Random_User_Position_Information/Transmission_Time_Minimization-Based_UAV_Deployment_and_Resource_Allocation_With_Random_User_Position_Information.md
```

The matrix must separate:

- mobility/state prediction from traffic-timescale scheduling;
- temporal scheduling asynchrony from physical multipath delay alignment;
- ground-AP-to-UAV, aerial-AP-to-ground, and UAV-swarm ISAC roles;
- deployment/channel/CoMP geometry from antenna-array geometry;
- coverage probability, outage, spectral efficiency, sum rate, and angular/visual coverage metrics.

Do not numerically rank incompatible results.

- [ ] **Step 3: Confirm at least 18 missing core-to-core edges**

Check every pair below in the baseline JSON and both endpoint parses. Accept at least 18; reject unsupported pairs in the evidence matrix instead of linking them.

```text
coordinated-multipoint-transmission <-> poisson-delaunay-comp-clustering
coordinated-multipoint-transmission <-> two-regime-aerial-user-association
poisson-delaunay-comp-clustering <-> two-regime-aerial-user-association
same-tier-three-site-comp <-> two-regime-aerial-user-association
beam-delay-alignment-transmission <-> cell-free-uav-predictive-beamforming
wideband-asynchronous-cell-free-massive-mimo <-> six-dimensional-aerial-rotatable-antenna-array
wideband-asynchronous-cell-free-massive-mimo <-> team-mmse-receive-combining
cell-free-uav-predictive-beamforming <-> six-dimensional-aerial-rotatable-antenna-array
cell-free-uav-predictive-beamforming <-> team-mmse-receive-combining
hong-2026-beam-delay-alignment <-> wang-2026-6dara-cellfree
fang-2026-cellfree-uav-predictive-beamforming <-> wang-2026-6dara-cellfree
wang-2026-6dara-cellfree <-> wideband-asynchronous-cell-free-massive-mimo
fang-2026-cellfree-uav-predictive-beamforming <-> beam-delay-alignment-transmission
hong-2026-beam-delay-alignment <-> team-mmse-receive-combining
shi-2026-vhetnet-comp-coverage <-> hong-2026-beam-delay-alignment
shi-2026-vhetnet-comp-coverage <-> fang-2026-cellfree-uav-predictive-beamforming
coordinated-multipoint-transmission <-> wideband-asynchronous-cell-free-massive-mimo
same-tier-three-site-comp <-> wideband-asynchronous-cell-free-massive-mimo
statistical-user-position-uav-deployment <-> two-regime-aerial-user-association
chai-2026-random-position-relay-deployment <-> shi-2026-vhetnet-comp-coverage
statistical-user-position-uav-deployment <-> cell-free-uav-predictive-beamforming
```

Prioritize the links involving `two-regime-aerial-user-association` and `statistical-user-position-uav-deployment`, whose baseline degree is one, and at least two links that join their current components to the 68-page component.

- [ ] **Step 4: Write the analytical page with exact frontmatter and section order**

Create `wiki/synthesis/mobility-asynchrony-and-geometry-in-aerial-coverage.md` with this structure. Write each section's prose and tables only from accepted matrix rows:

```markdown
---
type: synthesis
title: "Mobility, asynchrony, and geometry in aerial coverage"
tags: [synthesis, aerial-networking, coverage, mobility, asynchrony, geometry]
related:
  - "[[hong-2026-beam-delay-alignment]]"
  - "[[fang-2026-cellfree-uav-predictive-beamforming]]"
  - "[[chen-2026-traffic-aware-asynchronous-control]]"
  - "[[shi-2026-vhetnet-comp-coverage]]"
  - "[[ren-2026-distributed-uav-los]]"
  - "[[wang-2026-6dara-cellfree]]"
  - "[[jiang-2026-ray-antenna-array]]"
  - "[[chai-2026-random-position-relay-deployment]]"
  - "[[beam-delay-alignment-transmission]]"
  - "[[wideband-asynchronous-cell-free-massive-mimo]]"
  - "[[cell-free-uav-predictive-beamforming]]"
  - "[[traffic-aware-asynchronous-uav-control]]"
  - "[[coordinated-multipoint-transmission]]"
  - "[[six-dimensional-aerial-rotatable-antenna-array]]"
  - "[[ray-antenna-array]]"
  - "[[statistical-user-position-uav-deployment]]"
  - "[[collaborative-beamforming-in-aerial-mec]]"
  - "[[isac-sensing-in-aerial-mec]]"
created: 2026-07-14
updated: 2026-07-14
---

# Mobility, asynchrony, and geometry in aerial coverage

## Scope: what “coverage” means across these sources

## Mobility and state prediction

## Two distinct forms of asynchrony

## Deployment, channel, association, and CoMP geometry

## Antenna and array geometry

## Cross-source design map

## Non-comparability and evidence limits

## Design implications and open gaps
```

- [ ] **Step 5: Add reciprocal and direct core navigation**

For every accepted pair, add each endpoint to the other's `related:` list without changing unrelated prose. Add the new synthesis page to the eight primary source pages and the accepted concept pages. In the new synthesis's design map, include one concise rationale for every direct core-to-core pair; distinguish paper-reported facts from the page's cross-source inference.

- [ ] **Step 6: Reconcile index, overview, log, and ledger**

Add exactly one bullet under `## Synthesis` in `wiki/index.md`:

```markdown
- [[mobility-asynchrony-and-geometry-in-aerial-coverage]] — Mobility prediction, timing/path-delay asynchrony, cooperation scope, and geometry mapped without conflating coverage metrics.
```

Add a durable cross-cutting observation or track link in `wiki/overview.md` only if it improves a current reader path, then refresh counts:

```powershell
python tools/wiki/corpus_counts.py --update-overview
```

Prepend one dated `2026-07-14` entry to `wiki/log.md` naming the new page, accepted primary sources, exact internal-edge delta, component/weak deltas, and commit scope. Update accepted ledger rows; leave rejected candidates unchanged or record a concrete deferral reason.

- [ ] **Step 7: Run an independent evidence and edge-rationale review**

Give a read-only reviewer the eight source pages, eight raw paths, evidence matrix, new synthesis, and changed concept pages. Require a row-by-row verdict:

```text
For each factual claim and each new core-to-core edge, report ACCEPT, REVISE,
or REJECT; cite the raw parse heading and distinctive locator; distinguish
paper fact from cross-source inference; identify metric/system-model
non-comparability; flag any generic same-topic link, stale raw path, invented
claim, or reciprocal link whose rationale is absent from the synthesis.
```

Apply all required revisions and record them in the matrix before graph acceptance.

- [ ] **Step 8: Run graph acceptance and refresh ledger degrees**

Run:

```powershell
python tools/wiki/graph_audit.py compare `
  --baseline .curation-out/research-log-2026-07-14-baseline.json `
  --json research-log-theme-1-after.json `
  --ledger .curation-out/research-log-2026-07-14-ledger.json
```

Require:

- no removed frozen edge;
- at least 18 added frozen edges;
- at least one component reduction;
- `two-regime-aerial-user-association` and `statistical-user-position-uav-deployment` both reach internal degree at least 2;
- every `added_edges` pair has an accepted evidence-matrix row.

- [ ] **Step 9: Run the complete repository gates**

Run:

```powershell
python tools/wiki/curation_status.py --dupes
python tools/wiki/corpus_counts.py
python tools/wiki/linkcheck.py --orphans
python tools/wiki/process_refs.py
python tools/wiki/index_audit.py
python tools/wiki/frontmatter_audit.py
python tools/wiki/entity_roster_audit.py
python -m unittest discover -s tools/wiki/tests -p "test_*.py" -v
git diff --check
```

Expected: zero genuinely uncurated sources, duplicates, dangling links, process narration, index errors, and frontmatter errors; tests `OK`; no whitespace errors; no newly orphaned semantic page.

- [ ] **Step 10: Stage only the accepted theme, commit, push, and verify**

Run `git diff` for every named path, then stage only changed files from the Task 3 allowlist:

```powershell
git add wiki/synthesis/mobility-asynchrony-and-geometry-in-aerial-coverage.md wiki/sources/hong-2026-beam-delay-alignment.md wiki/sources/fang-2026-cellfree-uav-predictive-beamforming.md wiki/sources/chen-2026-traffic-aware-asynchronous-control.md wiki/sources/shi-2026-vhetnet-comp-coverage.md wiki/sources/ren-2026-distributed-uav-los.md wiki/sources/wang-2026-6dara-cellfree.md wiki/sources/jiang-2026-ray-antenna-array.md wiki/sources/chai-2026-random-position-relay-deployment.md wiki/concepts/beam-delay-alignment-transmission.md wiki/concepts/wideband-asynchronous-cell-free-massive-mimo.md wiki/concepts/cell-free-uav-predictive-beamforming.md wiki/concepts/traffic-aware-asynchronous-uav-control.md wiki/concepts/coordinated-multipoint-transmission.md wiki/concepts/poisson-delaunay-comp-clustering.md wiki/concepts/same-tier-three-site-comp.md wiki/concepts/two-regime-aerial-user-association.md wiki/concepts/air-to-ground-channel-model.md wiki/concepts/blockage-aware-channel-model.md wiki/concepts/six-dimensional-aerial-rotatable-antenna-array.md wiki/concepts/team-mmse-receive-combining.md wiki/concepts/ray-antenna-array.md wiki/concepts/statistical-user-position-uav-deployment.md wiki/index.md wiki/overview.md wiki/log.md
git diff --cached --name-only
git diff --cached --check
rg -n -i "(api[_-]?key|token|password|secret|authorization:|bearer )" -- $(git diff --cached --name-only)
git commit -m "Synthesize aerial coverage under mobility, asynchrony, and geometry"
git push origin main
git fetch origin main
$head = (git rev-parse HEAD).Trim()
$tracking = (git rev-parse '@{upstream}').Trim()
$remote = ((git ls-remote origin refs/heads/main) -split '\s+')[0]
if ($head -ne $tracking -or $head -ne $remote) { throw "theme 1 SHA mismatch" }
```

Expected: `.curation-out/` and every unrelated worktree path remain unstaged; the commit is present at all three SHA views.

### Task 4: Synthesize constraint regimes in UAV data collection

**Files:**

- Create: `wiki/synthesis/constraint-regimes-in-uav-data-collection.md`
- Modify sources:
  - `wiki/sources/zhu-2023-aoi-transformer-trajectory.md`
  - `wiki/sources/samir-2020-time-constrained-data-collection.md`
  - `wiki/sources/chang-2026-data-offloading-energy-constraints.md`
  - `wiki/sources/qi-2026-ocma-ddqn-data-collection.md`
  - `wiki/sources/zhao-2026-uav-carrier-vcs.md`
  - `wiki/sources/li-2023-energy-constrained-uav-data-collection.md`
  - `wiki/sources/fu-2026-dubins-uav-data-collection.md`
  - `wiki/sources/guo-2026-spatiotemporal-information-quality-ugrnet.md`
- Modify concepts when their edge rows are accepted:
  - `wiki/concepts/generalized-traveling-salesman-problem.md`
  - `wiki/concepts/hovering-disk-data-collection.md`
  - `wiki/concepts/transformer-weighted-a-star-trajectory-planning.md`
  - `wiki/concepts/deadline-constrained-uav-data-collection.md`
  - `wiki/concepts/branch-reduce-and-bound.md`
  - `wiki/concepts/many-to-one-pickup-and-delivery.md`
  - `wiki/concepts/dynamic-programming-battery-station-insertion.md`
  - `wiki/concepts/mixed-integer-linear-programming.md`
  - `wiki/concepts/opportunistic-cooperative-multi-uav-ddqn.md`
  - `wiki/concepts/lstm-interruption-compensation.md`
  - `wiki/concepts/experience-value-circles.md`
  - `wiki/concepts/attentive-memory-integrated-information-exchange.md`
  - `wiki/concepts/hidden-state-sharing-marl.md`
  - `wiki/concepts/mutual-policy-divergence-exploration.md`
  - `wiki/concepts/energy-constrained-uav-data-collection-orienteering.md`
  - `wiki/concepts/heterogeneous-uav-fleet.md`
  - `wiki/concepts/spatiotemporal-information-quality.md`
  - `wiki/concepts/age-of-information.md`
- Modify navigation: `wiki/index.md`, `wiki/overview.md`, `wiki/log.md`
- Generate, do not stage: `.curation-out/research-log-theme-2-evidence.md`, `.curation-out/research-log-theme-2-after.json`
- Patch, do not stage: `.curation-out/research-log-2026-07-14-ledger.json`

- [ ] **Step 1: Reconfirm the prior remote and frozen cohort**

Run:

```powershell
git fetch origin main
$head = (git rev-parse HEAD).Trim()
$remote = ((git ls-remote origin refs/heads/main) -split '\s+')[0]
if ($head -ne $remote) { throw "theme 1 is not verified remotely" }
git status --short --branch
python tools/wiki/graph_audit.py compare `
  --baseline .curation-out/research-log-2026-07-14-baseline.json `
  --json research-log-theme-2-before.json
```

Expected: frozen member hash unchanged, no unexplained removed edge, and only recorded unrelated worktree paths are outside Task 4.

- [ ] **Step 2: Ground the eight-source evidence matrix**

Read these exact parses and populate `.curation-out/research-log-theme-2-evidence.md`:

```text
raw/sources/UAV_Trajectory_Planning_for_AoI-Minimal_Data_Collection_in_UAV-Aided_IoT_Networks_by_Transformer/UAV_Trajectory_Planning_for_AoI-Minimal_Data_Collection_in_UAV-Aided_IoT_Networks_by_Transformer.md
raw/sources/UAV_Trajectory_Planning_for_Data_Collection_from_Time-Constrained_IoT_Devices/UAV_Trajectory_Planning_for_Data_Collection_from_Time-Constrained_IoT_Devices.md
raw/sources/UAV_Trajectory_Planning_for_IoT_Data_Collection_and_Offloading_With_Energy_Constraints/UAV_Trajectory_Planning_for_IoT_Data_Collection_and_Offloading_With_Energy_Constraints.md
raw/sources/Robust_and_Energy-Efficient_Multi-UAV_Trajectory_Planning_for_Data_Collection_A_Game-Theoretic_and_Deep_Reinforcement_Learning_Approach/Robust_and_Energy-Efficient_Multi-UAV_Trajectory_Planning_for_Data_Collection_A_Game-Theoretic_and_Deep_Reinforcement_Learning_Approach.md
raw/sources/UAV_Carrier_Enabled_Vehicular_Crowdsensing_by_Multi-Agent_Reinforcement_Learning_with_Mutual_Policy_Divergence_and_Attentive_Memory_Update/UAV_Carrier_Enabled_Vehicular_Crowdsensing_by_Multi-Agent_Reinforcement_Learning_with_Mutual_Policy_Divergence_and_Attentive_Memory_Update.md
raw/sources/Data_Collection_Maximization_in_IoT-Sensor_Networks_via_an_Energy-Constrained_UAV/Data_Collection_Maximization_in_IoT-Sensor_Networks_via_an_Energy-Constrained_UAV.md
raw/sources/Dubins_Path_Planning_of_Heterogeneous_UAV_Collaborative_Data_Collection_for_IoT_Network/Dubins_Path_Planning_of_Heterogeneous_UAV_Collaborative_Data_Collection_for_IoT_Network.md
raw/sources/Spatiotemporal_Information_Quality_Optimization_for_UAV-Assisted_Ground_Robot_Networks/Spatiotemporal_Information_Quality_Optimization_for_UAV-Assisted_Ground_Robot_Networks.md
```

Classify every source by hard/soft constraints, objective, decision horizon, solver evidence, and failure mode. Keep collected bits, AoI, delay violations, mission time, energy, and information quality separate. Do not rank centralized exact, MILP/branch-and-bound, DRL, and heuristic results across different instances.

- [ ] **Step 3: Confirm at least 18 missing core-to-core edges**

Verify both endpoint parses and current absence for this queue:

```text
zhu-2023-aoi-transformer-trajectory <-> samir-2020-time-constrained-data-collection
zhu-2023-aoi-transformer-trajectory <-> chang-2026-data-offloading-energy-constraints
deadline-constrained-uav-data-collection <-> transformer-weighted-a-star-trajectory-planning
deadline-constrained-uav-data-collection <-> generalized-traveling-salesman-problem
generalized-traveling-salesman-problem <-> many-to-one-pickup-and-delivery
transformer-weighted-a-star-trajectory-planning <-> branch-reduce-and-bound
transformer-weighted-a-star-trajectory-planning <-> mixed-integer-linear-programming
samir-2020-time-constrained-data-collection <-> generalized-traveling-salesman-problem
chang-2026-data-offloading-energy-constraints <-> deadline-constrained-uav-data-collection
samir-2020-time-constrained-data-collection <-> many-to-one-pickup-and-delivery
samir-2020-time-constrained-data-collection <-> dynamic-programming-battery-station-insertion
deadline-constrained-uav-data-collection <-> many-to-one-pickup-and-delivery
deadline-constrained-uav-data-collection <-> dynamic-programming-battery-station-insertion
branch-reduce-and-bound <-> mixed-integer-linear-programming
branch-reduce-and-bound <-> dynamic-programming-battery-station-insertion
chang-2026-data-offloading-energy-constraints <-> qi-2026-ocma-ddqn-data-collection
many-to-one-pickup-and-delivery <-> opportunistic-cooperative-multi-uav-ddqn
mixed-integer-linear-programming <-> opportunistic-cooperative-multi-uav-ddqn
qi-2026-ocma-ddqn-data-collection <-> zhao-2026-uav-carrier-vcs
opportunistic-cooperative-multi-uav-ddqn <-> hidden-state-sharing-marl
lstm-interruption-compensation <-> attentive-memory-integrated-information-exchange
experience-value-circles <-> mutual-policy-divergence-exploration
lstm-interruption-compensation <-> hidden-state-sharing-marl
opportunistic-cooperative-multi-uav-ddqn <-> attentive-memory-integrated-information-exchange
```

Accept at least 18 after raw review. Prioritize `mixed-integer-linear-programming`, whose baseline degree is one, and select cross-component links joining the AoI/GTSP, deadline/energy, multi-UAV interruption, and UAV-carrier groups.

- [ ] **Step 4: Write the analytical page**

Create `wiki/synthesis/constraint-regimes-in-uav-data-collection.md`:

```markdown
---
type: synthesis
title: "Constraint regimes in UAV data collection"
tags: [synthesis, uav-data-collection, constraints, trajectory, freshness, energy]
related:
  - "[[zhu-2023-aoi-transformer-trajectory]]"
  - "[[samir-2020-time-constrained-data-collection]]"
  - "[[chang-2026-data-offloading-energy-constraints]]"
  - "[[qi-2026-ocma-ddqn-data-collection]]"
  - "[[zhao-2026-uav-carrier-vcs]]"
  - "[[li-2023-energy-constrained-uav-data-collection]]"
  - "[[fu-2026-dubins-uav-data-collection]]"
  - "[[guo-2026-spatiotemporal-information-quality-ugrnet]]"
  - "[[deadline-constrained-uav-data-collection]]"
  - "[[many-to-one-pickup-and-delivery]]"
  - "[[dynamic-programming-battery-station-insertion]]"
  - "[[opportunistic-cooperative-multi-uav-ddqn]]"
  - "[[age-of-information]]"
  - "[[spatiotemporal-information-quality]]"
  - "[[design-recipe-multi-uav-mec]]"
  - "[[safety-and-robustness-mechanisms-in-mec]]"
created: 2026-07-14
updated: 2026-07-14
---

# Constraint regimes in UAV data collection

## Scope and constraint taxonomy

## Energy, travel, and replenishment

## Deadlines and freshness

## Connectivity, interruption, and adversarial robustness

## Kinematics and fleet heterogeneity

## Information quality and delay guarantees

## Cross-source design map

## Non-comparability and evidence limits

## Design implications and open gaps
```

Write prose and tables only from accepted matrix rows. Use the design map to explain every new direct core edge.

- [ ] **Step 5: Add reciprocal links and navigation**

Add every accepted core pair reciprocally in `related:`. Add the synthesis link to all eight source pages and every accepted concept page. Catalogue it under `## Synthesis`:

```markdown
- [[constraint-regimes-in-uav-data-collection]] — Energy, deadline, freshness, connectivity, kinematic, and information-quality constraints compared without ranking incompatible metrics.
```

Run:

```powershell
python tools/wiki/corpus_counts.py --update-overview
```

Add a durable overview path when warranted, prepend one `2026-07-14` log entry with cumulative graph deltas, and patch the ledger evidence/status fields.

- [ ] **Step 6: Complete independent claim/edge review**

Give a fresh read-only reviewer the eight Task 4 source pages, eight raw parses, evidence matrix, synthesis, and changed concepts. Require:

```text
For every factual claim and new core-to-core edge, return ACCEPT, REVISE, or
REJECT with the raw parse heading and a distinctive locator. Separate paper
facts from cross-source inference. Reject generic same-topic links and any
guarantee transfer across incompatible objectives, horizons, system models, or
solver-evidence regimes. Flag stale raw paths and missing reciprocal rationale.
```

Apply and record every revision.

- [ ] **Step 7: Run graph acceptance**

Run:

```powershell
python tools/wiki/graph_audit.py compare `
  --baseline .curation-out/research-log-2026-07-14-baseline.json `
  --json research-log-theme-2-after.json `
  --ledger .curation-out/research-log-2026-07-14-ledger.json
```

Require no removed edge, at least 36 cumulative added internal edges, at least one additional component merge in this batch, `mixed-integer-linear-programming` at degree at least 2, and an accepted matrix row for every added pair.

- [ ] **Step 8: Run all repository gates**

Run:

```powershell
python tools/wiki/curation_status.py --dupes
python tools/wiki/corpus_counts.py
python tools/wiki/linkcheck.py --orphans
python tools/wiki/process_refs.py
python tools/wiki/index_audit.py
python tools/wiki/frontmatter_audit.py
python tools/wiki/entity_roster_audit.py
python -m unittest discover -s tools/wiki/tests -p "test_*.py" -v
git diff --check
```

Expected: every failing category remains zero, tests report `OK`, and no semantic orphan or whitespace error is introduced.

- [ ] **Step 9: Stage only Task 4, commit, push, and verify**

Stage only changed Task 4 allowlist paths:

```powershell
git add wiki/synthesis/constraint-regimes-in-uav-data-collection.md wiki/sources/zhu-2023-aoi-transformer-trajectory.md wiki/sources/samir-2020-time-constrained-data-collection.md wiki/sources/chang-2026-data-offloading-energy-constraints.md wiki/sources/qi-2026-ocma-ddqn-data-collection.md wiki/sources/zhao-2026-uav-carrier-vcs.md wiki/sources/li-2023-energy-constrained-uav-data-collection.md wiki/sources/fu-2026-dubins-uav-data-collection.md wiki/sources/guo-2026-spatiotemporal-information-quality-ugrnet.md wiki/concepts/generalized-traveling-salesman-problem.md wiki/concepts/hovering-disk-data-collection.md wiki/concepts/transformer-weighted-a-star-trajectory-planning.md wiki/concepts/deadline-constrained-uav-data-collection.md wiki/concepts/branch-reduce-and-bound.md wiki/concepts/many-to-one-pickup-and-delivery.md wiki/concepts/dynamic-programming-battery-station-insertion.md wiki/concepts/mixed-integer-linear-programming.md wiki/concepts/opportunistic-cooperative-multi-uav-ddqn.md wiki/concepts/lstm-interruption-compensation.md wiki/concepts/experience-value-circles.md wiki/concepts/attentive-memory-integrated-information-exchange.md wiki/concepts/hidden-state-sharing-marl.md wiki/concepts/mutual-policy-divergence-exploration.md wiki/concepts/energy-constrained-uav-data-collection-orienteering.md wiki/concepts/heterogeneous-uav-fleet.md wiki/concepts/spatiotemporal-information-quality.md wiki/concepts/age-of-information.md wiki/index.md wiki/overview.md wiki/log.md
git diff --cached --name-only
git diff --cached --check
rg -n -i "(api[_-]?key|token|password|secret|authorization:|bearer )" -- $(git diff --cached --name-only)
git commit -m "Synthesize constraint regimes in UAV data collection"
git push origin main
git fetch origin main
$head = (git rev-parse HEAD).Trim()
$tracking = (git rev-parse '@{upstream}').Trim()
$remote = ((git ls-remote origin refs/heads/main) -split '\s+')[0]
if ($head -ne $tracking -or $head -ne $remote) { throw "theme 2 SHA mismatch" }
```

Expected: exact scoped commit, scratch and unrelated paths unstaged, local/tracking/remote SHAs equal.

### Task 5: Map the aerial federated aggregation design space

**Files:**

- Create: `wiki/synthesis/aerial-federated-aggregation-design-space.md`
- Modify sources:
  - `wiki/sources/zhong-2026-hierarchical-ota-fl.md`
  - `wiki/sources/huang-2026-aircomp-uav-swarms-afl.md`
  - `wiki/sources/qian-2026-federated-bandit-aircomp.md`
  - `wiki/sources/dang-2026-uav-fl-energy.md`
  - `wiki/sources/li-2026-clp-uav-hpfl.md`
  - `wiki/sources/zhou-2026-cpsfl-uav-foundation-models.md`
  - `wiki/sources/tang-2024-iscc-uav-feel.md`
  - `wiki/sources/lim-2021-uav-iov-contract-matching.md`
  - `wiki/sources/v-2026-pb-papp-survivor-detection.md`
- Modify concepts:
  - `wiki/concepts/hierarchical-over-the-air-federated-learning.md`
  - `wiki/concepts/gradient-correlation-aware-aggregation-mse.md`
  - `wiki/concepts/aircomp-assisted-asynchronous-fl.md`
  - `wiki/concepts/federated-linear-bandit-learning.md`
  - `wiki/concepts/simultaneous-interference-uav-federated-learning.md`
  - `wiki/concepts/critical-learning-period.md`
  - `wiki/concepts/federated-drift-norm.md`
  - `wiki/concepts/federated-kl-divergence-norm.md`
  - `wiki/concepts/split-federated-learning.md`
  - `wiki/concepts/integrated-sensing-computation-communication.md`
  - `wiki/concepts/multidimensional-contract-matching.md`
  - `wiki/concepts/tree-structured-weight-synthesis.md`
- Modify navigation: `wiki/index.md`, `wiki/overview.md`, `wiki/log.md`
- Generate, do not stage: `.curation-out/research-log-theme-3-evidence.md`, `.curation-out/research-log-theme-3-after.json`
- Patch, do not stage: `.curation-out/research-log-2026-07-14-ledger.json`

- [ ] **Step 1: Verify remote continuity and current graph**

Run:

```powershell
git fetch origin main
$head = (git rev-parse HEAD).Trim()
$tracking = (git rev-parse '@{upstream}').Trim()
$remote = ((git ls-remote origin refs/heads/main) -split '\s+')[0]
if ($head -ne $tracking -or $head -ne $remote) {
    throw "theme 2 is not verified remotely"
}
python tools/wiki/graph_audit.py compare `
  --baseline .curation-out/research-log-2026-07-14-baseline.json `
  --json research-log-theme-3-before.json
git status --short --branch
```

Expected: no unexplained removed edge and only the recorded unrelated worktree paths outside this task.

- [ ] **Step 2: Ground the seven primary papers and correct two stale artifact paths**

Read:

```text
raw/sources/UAV-Enabled_Over-the-Air_Federated_Learning_A_Hierarchical_Aggregation_Approach/UAV-Enabled_Over-the-Air_Federated_Learning_A_Hierarchical_Aggregation_Approach.md
raw/sources/AirComp-Assisted_Asynchronous_Federated_Learning_for_UAV_Swarms_A_Self-Adaptive_Aggregation_Scheme_to_Tackle_Model_Staleness/AirComp-Assisted_Asynchronous_Federated_Learning_for_UAV_Swarms_A_Self-Adaptive_Aggregation_Scheme_to_Tackle_Model_Staleness.md
raw/sources/Federated_Linear_Bandit_Learning_via_UAV_Aided_Over-the-Air_Computation/Federated_Linear_Bandit_Learning_via_UAV_Aided_Over-the-Air_Computation.md
raw/sources/Optimizing_Energy_Efficiency_for_Federated_Learning_in_Rotary-Wing_UAV_Air-to-Ground_Communications/Optimizing_Energy_Efficiency_for_Federated_Learning_in_Rotary-Wing_UAV_Air-to-Ground_Communications.md
raw/sources/Seizing_Critical_Learning_Period_in_UAV-Assisted_Hierarchical_Personalized_Federated_Learning/Seizing_Critical_Learning_Period_in_UAV-Assisted_Hierarchical_Personalized_Federated_Learning.md
raw/sources/Communication-Pipelined_Split_Federated_Learning_for_Foundation_Model_Fine-Tuning_in_UAV_Networks/Communication-Pipelined_Split_Federated_Learning_for_Foundation_Model_Fine-Tuning_in_UAV_Networks.md
raw/sources/Integrated_Sensing_Computation_and_Communication_for_UAV-Assisted_Federated_Edge_Learning/Integrated_Sensing_Computation_and_Communication_for_UAV-Assisted_Federated_Edge_Learning.md
```

In the Zhou and Tang source pages, replace only stale raw-artifact path strings with the last two verified paths above. Populate `.curation-out/research-log-theme-3-evidence.md` with learning task, aggregation topology, synchronization, physical layer, mobility control, objective, proof/evidence scope, and non-comparability.

- [ ] **Step 3: Confirm at least 18 missing core-to-core edges**

Verify and disposition this queue:

```text
zhong-2026-hierarchical-ota-fl <-> dang-2026-uav-fl-energy
zhong-2026-hierarchical-ota-fl <-> li-2026-clp-uav-hpfl
dang-2026-uav-fl-energy <-> li-2026-clp-uav-hpfl
zhong-2026-hierarchical-ota-fl <-> simultaneous-interference-uav-federated-learning
zhong-2026-hierarchical-ota-fl <-> critical-learning-period
zhong-2026-hierarchical-ota-fl <-> federated-drift-norm
zhong-2026-hierarchical-ota-fl <-> federated-kl-divergence-norm
dang-2026-uav-fl-energy <-> hierarchical-over-the-air-federated-learning
dang-2026-uav-fl-energy <-> gradient-correlation-aware-aggregation-mse
dang-2026-uav-fl-energy <-> critical-learning-period
dang-2026-uav-fl-energy <-> federated-drift-norm
dang-2026-uav-fl-energy <-> federated-kl-divergence-norm
li-2026-clp-uav-hpfl <-> hierarchical-over-the-air-federated-learning
li-2026-clp-uav-hpfl <-> gradient-correlation-aware-aggregation-mse
li-2026-clp-uav-hpfl <-> simultaneous-interference-uav-federated-learning
hierarchical-over-the-air-federated-learning <-> simultaneous-interference-uav-federated-learning
hierarchical-over-the-air-federated-learning <-> critical-learning-period
gradient-correlation-aware-aggregation-mse <-> simultaneous-interference-uav-federated-learning
gradient-correlation-aware-aggregation-mse <-> critical-learning-period
lim-2021-uav-iov-contract-matching <-> li-2026-clp-uav-hpfl
multidimensional-contract-matching <-> critical-learning-period
tree-structured-weight-synthesis <-> hierarchical-over-the-air-federated-learning
tree-structured-weight-synthesis <-> gradient-correlation-aware-aggregation-mse
v-2026-pb-papp-survivor-detection <-> zhong-2026-hierarchical-ota-fl
```

Accept at least 18 only after raw confirmation. Prioritize the degree-one pages `dang-2026-uav-fl-energy` and `simultaneous-interference-uav-federated-learning`, and include cross-component edges that connect the AirComp, CLP, simultaneous-interference, contract, and tree-aggregation groups.

- [ ] **Step 4: Write the synthesis page**

Create:

```markdown
---
type: synthesis
title: "Aerial federated aggregation design space"
tags: [synthesis, federated-learning, aggregation, aircomp, uav, learning-systems]
related:
  - "[[zhong-2026-hierarchical-ota-fl]]"
  - "[[huang-2026-aircomp-uav-swarms-afl]]"
  - "[[qian-2026-federated-bandit-aircomp]]"
  - "[[dang-2026-uav-fl-energy]]"
  - "[[li-2026-clp-uav-hpfl]]"
  - "[[zhou-2026-cpsfl-uav-foundation-models]]"
  - "[[tang-2024-iscc-uav-feel]]"
  - "[[hierarchical-over-the-air-federated-learning]]"
  - "[[aircomp-assisted-asynchronous-fl]]"
  - "[[federated-linear-bandit-learning]]"
  - "[[critical-learning-period]]"
  - "[[split-federated-learning]]"
  - "[[integrated-sensing-computation-communication]]"
created: 2026-07-14
updated: 2026-07-14
---

# Aerial federated aggregation design space

## Scope: what counts as aggregation

## System and guarantee matrix

## Hierarchical synchronous AirComp

## Asynchronous and staleness-aware AirComp

## Event-triggered, interference-limited, critical-period, split, and sensing-conditioned aggregation

## Geometry and resource-control surfaces

## Guarantee boundaries

## Non-comparability and design-selection guide

## Open gaps
```

Do not numerically compare accuracy, regret, energy, training time, aggregation MSE, and pipeline latency. Separate learning convergence/regret bounds, local optimizer convergence, and simulation evidence.

- [ ] **Step 5: Add reciprocal/core links and shared navigation**

Add accepted pairs reciprocally, the synthesis backlink to all primary sources and accepted concepts, and one rationale per added pair in the design matrix. Add under `## Synthesis`:

```markdown
- [[aerial-federated-aggregation-design-space]] — Synchronous, asynchronous, hierarchical, event-triggered, interference-limited, and split aggregation compared by learning and physical-layer assumptions.
```

Run `python tools/wiki/corpus_counts.py --update-overview`, update durable overview navigation, prepend one dated log entry, and patch ledger statuses/evidence.

- [ ] **Step 6: Complete independent review and graph acceptance**

Give a fresh read-only reviewer the seven primary source pages, verified parses, supporting core pages, evidence matrix, synthesis, and full diff. Require:

```text
Return ACCEPT, REVISE, or REJECT for every claim and new edge with a raw parse
heading and distinctive locator. Separate paper fact from inference. Reject
generic links and numeric comparisons across accuracy, regret, energy, training
time, aggregation MSE, and pipeline latency. Separate learning guarantees,
optimizer convergence, and simulation evidence.
```

Apply and record every revision. Then run:

```powershell
python tools/wiki/graph_audit.py compare `
  --baseline .curation-out/research-log-2026-07-14-baseline.json `
  --json research-log-theme-3-after.json `
  --ledger .curation-out/research-log-2026-07-14-ledger.json
```

Require no removed edge, at least 54 cumulative added internal edges, at least one component merge in this batch, both prioritized degree-one pages promoted above degree one, and accepted evidence for every added pair.

- [ ] **Step 7: Run all repository gates**

Run:

```powershell
python tools/wiki/curation_status.py --dupes
python tools/wiki/corpus_counts.py
python tools/wiki/linkcheck.py --orphans
python tools/wiki/process_refs.py
python tools/wiki/index_audit.py
python tools/wiki/frontmatter_audit.py
python tools/wiki/entity_roster_audit.py
python -m unittest discover -s tools/wiki/tests -p "test_*.py" -v
git diff --check
```

Expected: all failing categories zero, tests `OK`, no new semantic orphan, and no whitespace error.

- [ ] **Step 8: Stage, commit, push, and verify only Task 5**

```powershell
git add wiki/synthesis/aerial-federated-aggregation-design-space.md wiki/sources/zhong-2026-hierarchical-ota-fl.md wiki/sources/huang-2026-aircomp-uav-swarms-afl.md wiki/sources/qian-2026-federated-bandit-aircomp.md wiki/sources/dang-2026-uav-fl-energy.md wiki/sources/li-2026-clp-uav-hpfl.md wiki/sources/zhou-2026-cpsfl-uav-foundation-models.md wiki/sources/tang-2024-iscc-uav-feel.md wiki/sources/lim-2021-uav-iov-contract-matching.md wiki/sources/v-2026-pb-papp-survivor-detection.md wiki/concepts/hierarchical-over-the-air-federated-learning.md wiki/concepts/gradient-correlation-aware-aggregation-mse.md wiki/concepts/aircomp-assisted-asynchronous-fl.md wiki/concepts/federated-linear-bandit-learning.md wiki/concepts/simultaneous-interference-uav-federated-learning.md wiki/concepts/critical-learning-period.md wiki/concepts/federated-drift-norm.md wiki/concepts/federated-kl-divergence-norm.md wiki/concepts/split-federated-learning.md wiki/concepts/integrated-sensing-computation-communication.md wiki/concepts/multidimensional-contract-matching.md wiki/concepts/tree-structured-weight-synthesis.md wiki/index.md wiki/overview.md wiki/log.md
git diff --cached --name-only
git diff --cached --check
rg -n -i "(api[_-]?key|token|password|secret|authorization:|bearer )" -- $(git diff --cached --name-only)
git commit -m "Synthesize aerial federated aggregation design space"
git push origin main
git fetch origin main
$head = (git rev-parse HEAD).Trim()
$tracking = (git rev-parse '@{upstream}').Trim()
$remote = ((git ls-remote origin refs/heads/main) -split '\s+')[0]
if ($head -ne $tracking -or $head -ne $remote) { throw "theme 3 SHA mismatch" }
```

Expected: only accepted Task 5 paths committed, scratch/unrelated paths untouched, all SHA views equal.

### Task 6: Build the UAV trajectory safety guarantee ladder

**Files:**

- Create: `wiki/comparisons/uav-trajectory-safety-guarantee-ladder.md`
- Modify analysis:
  - `wiki/synthesis/safety-and-robustness-mechanisms-in-mec.md`
  - `wiki/thesis/explicit-constraints-beat-reward-shaping-in-mec-drl.md`
- Modify primary sources:
  - `wiki/sources/zhang-2021-safe-dqn-emergency.md`
  - `wiki/sources/hsu-2022-collision-avoidance-trajectory.md`
  - `wiki/sources/hua-2026-unpredictable-uav-trajectory.md`
  - `wiki/sources/jia-2026-dro-lawn-trajectory.md`
  - `wiki/sources/gong-2026-safe-economic-lae-trajectory.md`
  - `wiki/sources/wang-2026-robust-multiuav-jtcra.md`
  - `wiki/sources/zhang-2025-ssac-mgi-heterogeneous-uav.md`
  - `wiki/sources/li-2024-robust-bmappo-multiuav-mec.md`
- Modify supporting core sources when accepted:
  - `wiki/sources/qi-2026-ocma-ddqn-data-collection.md`
  - `wiki/sources/yin-2026-uav-antijamming-nfsp.md`
  - `wiki/sources/li-2026-full-duplex-noma-uav-relay.md`
- Modify concepts when accepted:
  - `wiki/concepts/safe-reinforcement-learning.md`
  - `wiki/concepts/distributed-tabular-q-learning-uav-collision-avoidance.md`
  - `wiki/concepts/navigation-stochastic-control-decomposition.md`
  - `wiki/concepts/unpredictable-uav-trajectory-control.md`
  - `wiki/concepts/distributionally-robust-optimization.md`
  - `wiki/concepts/compliance-aware-uav-trajectory.md`
  - `wiki/concepts/collision-avoidance-mgi.md`
  - `wiki/concepts/robust-offloading.md`
  - `wiki/concepts/convex-tsp-uav-data-collection.md`
  - `wiki/concepts/opportunistic-cooperative-multi-uav-ddqn.md`
  - `wiki/concepts/connectivity-preserving-uav-behavioral-loss.md`
  - `wiki/concepts/multi-hop-uav-emergency-networking.md`
  - `wiki/concepts/implicit-opponent-modeling.md`
  - `wiki/concepts/bernstein-safe-approximation.md`
- Modify navigation: `wiki/index.md`, `wiki/overview.md`, `wiki/log.md`
- Generate, do not stage: `.curation-out/research-log-theme-4-evidence.md`, `.curation-out/research-log-theme-4-after.json`
- Patch, do not stage: `.curation-out/research-log-2026-07-14-ledger.json`

- [ ] **Step 1: Verify the prior batch and graph attribution**

Run:

```powershell
git fetch origin main
$head = (git rev-parse HEAD).Trim()
$tracking = (git rev-parse '@{upstream}').Trim()
$remote = ((git ls-remote origin refs/heads/main) -split '\s+')[0]
if ($head -ne $tracking -or $head -ne $remote) {
    throw "theme 3 is not verified remotely"
}
git status --short --branch
python tools/wiki/graph_audit.py compare `
  --baseline .curation-out/research-log-2026-07-14-baseline.json `
  --json research-log-theme-4-before.json
```

Require no unexplained edge removal or overlapping user edit.

- [ ] **Step 2: Ground the guarantee matrix and repair four stale paths**

Read:

```text
raw/sources/Trajectory_Optimization_for_UAV_Emergency_Communication_With_Limited_User_Equipment_Energy_A_Safe-DQN_Approach/Trajectory_Optimization_for_UAV_Emergency_Communication_With_Limited_User_Equipment_Energy_A_Safe-DQN_Approach.md
raw/sources/Reinforcement_Learning-Based_Collision_Avoidance_and_Optimal_Trajectory_Planning_in_UAV_Communication_Networks/Reinforcement_Learning-Based_Collision_Avoidance_and_Optimal_Trajectory_Planning_in_UAV_Communication_Networks.md
raw/sources/Unpredictable_Trajectory_Optimization_for_UAV-Assisted_Anti-Jamming_Data_Collection/Unpredictable_Trajectory_Optimization_for_UAV-Assisted_Anti-Jamming_Data_Collection.md
raw/sources/Distributionally_Robust_Computation_Offloading_and_Trajectory_Optimization_in_Low-Altitude_Wireless_Networks/Distributionally_Robust_Computation_Offloading_and_Trajectory_Optimization_in_Low-Altitude_Wireless_Networks.md
raw/sources/Safe_and_Economical_UAV_Trajectory_Planning_in_Low-Altitude_Airspace_A_Hybrid_DRL-LLM_Algorithm_With_Compliance_Awareness/Safe_and_Economical_UAV_Trajectory_Planning_in_Low-Altitude_Airspace_A_Hybrid_DRL-LLM_Algorithm_With_Compliance_Awareness.md
raw/sources/Enhancing_A2G_Robustness_in_Energy-Constrained_Multi-UAV_Networks_MADRL_for_Trajectory_Control_and_Resource_Allocation/Enhancing_A2G_Robustness_in_Energy-Constrained_Multi-UAV_Networks_MADRL_for_Trajectory_Control_and_Resource_Allocation.md
raw/sources/Safe_and_Energy-Efficient_Trajectory_Planning_for_Heterogeneous_Multi-UAV_Enabled_Mobile_Edge_Computing/Safe_and_Energy-Efficient_Trajectory_Planning_for_Heterogeneous_Multi-UAV_Enabled_Mobile_Edge_Computing.md
raw/sources/Robust_Computation_Offloading_and_Trajectory_Optimization_for_Multi-UAV-Assisted_MEC_A_Multiagent_DRL_Approach/Robust_Computation_Offloading_and_Trajectory_Optimization_for_Multi-UAV-Assisted_MEC_A_Multiagent_DRL_Approach.md
```

Correct only the stale raw-artifact path strings in the Jia, Gong, Zhang-2025, and Li-2024 source pages. Populate `.curation-out/research-log-theme-4-evidence.md` with protected object, hazard, enforcement locus, training/deployment persistence, proof scope, evaluation evidence, and caveat.

The matrix must keep these distinct: Safe-DQN expected-cost/action filtering, Hsu simulator collision performance, Gong training-time LLM guidance, Hua bounded unpredictability control, SSAC-MGI persistent intervention, Jia distributional uncertainty, Li bounded uncertainty, and Wang service continuity.

- [ ] **Step 3: Confirm at least 18 missing core-to-core edges**

Disposition:

```text
zhang-2021-safe-dqn-emergency <-> hsu-2022-collision-avoidance-trajectory
zhang-2021-safe-dqn-emergency <-> hua-2026-unpredictable-uav-trajectory
zhang-2021-safe-dqn-emergency <-> distributed-tabular-q-learning-uav-collision-avoidance
zhang-2021-safe-dqn-emergency <-> navigation-stochastic-control-decomposition
zhang-2021-safe-dqn-emergency <-> connectivity-preserving-uav-behavioral-loss
zhang-2021-safe-dqn-emergency <-> multi-hop-uav-emergency-networking
hsu-2022-collision-avoidance-trajectory <-> hua-2026-unpredictable-uav-trajectory
hsu-2022-collision-avoidance-trajectory <-> unpredictable-uav-trajectory-control
hsu-2022-collision-avoidance-trajectory <-> navigation-stochastic-control-decomposition
hsu-2022-collision-avoidance-trajectory <-> qi-2026-ocma-ddqn-data-collection
distributed-tabular-q-learning-uav-collision-avoidance <-> opportunistic-cooperative-multi-uav-ddqn
distributed-tabular-q-learning-uav-collision-avoidance <-> connectivity-preserving-uav-behavioral-loss
convex-tsp-uav-data-collection <-> navigation-stochastic-control-decomposition
hua-2026-unpredictable-uav-trajectory <-> qi-2026-ocma-ddqn-data-collection
unpredictable-uav-trajectory-control <-> yin-2026-uav-antijamming-nfsp
unpredictable-uav-trajectory-control <-> implicit-opponent-modeling
navigation-stochastic-control-decomposition <-> implicit-opponent-modeling
qi-2026-ocma-ddqn-data-collection <-> yin-2026-uav-antijamming-nfsp
qi-2026-ocma-ddqn-data-collection <-> connectivity-preserving-uav-behavioral-loss
opportunistic-cooperative-multi-uav-ddqn <-> connectivity-preserving-uav-behavioral-loss
li-2026-full-duplex-noma-uav-relay <-> zhang-2021-safe-dqn-emergency
bernstein-safe-approximation <-> zhang-2021-safe-dqn-emergency
bernstein-safe-approximation <-> distributed-tabular-q-learning-uav-collision-avoidance
```

Accept at least 18 after parse review. Prioritize baseline-degree-one `zhang-2021-safe-dqn-emergency`, `distributed-tabular-q-learning-uav-collision-avoidance`, and `implicit-opponent-modeling`, plus cross-component edges connecting empirical avoidance, stochastic control, anti-jamming, connectivity, and chance-constrained reliability.

- [ ] **Step 4: Write the comparison and correct existing analysis**

Create:

```markdown
---
type: comparison
title: "UAV trajectory safety guarantee ladder"
tags: [comparison, uav, trajectory, safety, robustness, guarantees]
related:
  - "[[zhang-2021-safe-dqn-emergency]]"
  - "[[hsu-2022-collision-avoidance-trajectory]]"
  - "[[hua-2026-unpredictable-uav-trajectory]]"
  - "[[jia-2026-dro-lawn-trajectory]]"
  - "[[gong-2026-safe-economic-lae-trajectory]]"
  - "[[wang-2026-robust-multiuav-jtcra]]"
  - "[[zhang-2025-ssac-mgi-heterogeneous-uav]]"
  - "[[li-2024-robust-bmappo-multiuav-mec]]"
  - "[[safe-reinforcement-learning]]"
  - "[[distributionally-robust-optimization]]"
  - "[[collision-avoidance-mgi]]"
  - "[[robust-offloading]]"
  - "[[safety-and-robustness-mechanisms-in-mec]]"
  - "[[explicit-constraints-beat-reward-shaping-in-mec-drl]]"
created: 2026-07-14
updated: 2026-07-14
---

# UAV trajectory safety guarantee ladder

## Protected object and meaning of guarantee

## Hazard, enforcement, persistence, and evidence matrix

## Empirical reward-shaped avoidance

## Action filtering and constraint-aware policies

## Persistent intervention and shielding

## Bounded and distributional robustness

## Unpredictability and service continuity

## Explicit non-comparability

## Missing guarantees
```

In `safety-and-robustness-mechanisms-in-mec.md`, add Jia-2026 as the second DRO anchor and remove any single-source characterization. In `explicit-constraints-beat-reward-shaping-in-mec-drl.md`, replace its one-source distributional-robustness claim with the verified two-source distinction. Preserve broader claims unless directly contradicted by these parses.

- [ ] **Step 5: Add reciprocal links and shared navigation**

Add accepted core edges reciprocally and link the comparison from all primary sources/concepts and both refreshed analytical pages. Add under `## Comparisons`:

```markdown
- [[uav-trajectory-safety-guarantee-ladder]] — Empirical avoidance, action filtering, persistent shielding, bounded uncertainty, DRO, unpredictability, and continuity separated by guarantee scope.
```

Run `python tools/wiki/corpus_counts.py --update-overview`, add a durable overview link, prepend the dated log entry with graph deltas, and patch ledger evidence/status rows.

- [ ] **Step 6: Complete independent review and graph acceptance**

Give a fresh read-only reviewer every changed source/concept/analysis page, all primary parses, the evidence matrix, the comparison, and the full diff. Require:

```text
Return ACCEPT, REVISE, or REJECT for every claim and new edge with a parse
heading and distinctive locator. Reject generic links and any transfer of a
safety or robustness guarantee across different hazards, enforcement loci,
training/deployment persistence, proof scopes, or evaluation-only evidence.
```

Apply revisions, then run:

```powershell
python tools/wiki/graph_audit.py compare `
  --baseline .curation-out/research-log-2026-07-14-baseline.json `
  --json research-log-theme-4-after.json `
  --ledger .curation-out/research-log-2026-07-14-ledger.json
```

Require no removed edge, at least 72 cumulative added internal edges, at least one component merge in this batch, all three prioritized degree-one pages promoted, and accepted evidence for every added pair.

- [ ] **Step 7: Run all repository gates**

Run:

```powershell
python tools/wiki/curation_status.py --dupes
python tools/wiki/corpus_counts.py
python tools/wiki/linkcheck.py --orphans
python tools/wiki/process_refs.py
python tools/wiki/index_audit.py
python tools/wiki/frontmatter_audit.py
python tools/wiki/entity_roster_audit.py
python -m unittest discover -s tools/wiki/tests -p "test_*.py" -v
git diff --check
```

Expected: all failure counts zero, tests `OK`, and no new semantic orphan or whitespace error.

- [ ] **Step 8: Stage, commit, push, and verify only Task 6**

```powershell
git add wiki/comparisons/uav-trajectory-safety-guarantee-ladder.md wiki/synthesis/safety-and-robustness-mechanisms-in-mec.md wiki/thesis/explicit-constraints-beat-reward-shaping-in-mec-drl.md wiki/sources/zhang-2021-safe-dqn-emergency.md wiki/sources/hsu-2022-collision-avoidance-trajectory.md wiki/sources/hua-2026-unpredictable-uav-trajectory.md wiki/sources/jia-2026-dro-lawn-trajectory.md wiki/sources/gong-2026-safe-economic-lae-trajectory.md wiki/sources/wang-2026-robust-multiuav-jtcra.md wiki/sources/zhang-2025-ssac-mgi-heterogeneous-uav.md wiki/sources/li-2024-robust-bmappo-multiuav-mec.md wiki/sources/qi-2026-ocma-ddqn-data-collection.md wiki/sources/yin-2026-uav-antijamming-nfsp.md wiki/sources/li-2026-full-duplex-noma-uav-relay.md wiki/concepts/safe-reinforcement-learning.md wiki/concepts/distributed-tabular-q-learning-uav-collision-avoidance.md wiki/concepts/navigation-stochastic-control-decomposition.md wiki/concepts/unpredictable-uav-trajectory-control.md wiki/concepts/distributionally-robust-optimization.md wiki/concepts/compliance-aware-uav-trajectory.md wiki/concepts/collision-avoidance-mgi.md wiki/concepts/robust-offloading.md wiki/concepts/convex-tsp-uav-data-collection.md wiki/concepts/opportunistic-cooperative-multi-uav-ddqn.md wiki/concepts/connectivity-preserving-uav-behavioral-loss.md wiki/concepts/multi-hop-uav-emergency-networking.md wiki/concepts/implicit-opponent-modeling.md wiki/concepts/bernstein-safe-approximation.md wiki/index.md wiki/overview.md wiki/log.md
git diff --cached --name-only
git diff --cached --check
rg -n -i "(api[_-]?key|token|password|secret|authorization:|bearer )" -- $(git diff --cached --name-only)
git commit -m "Compare UAV trajectory safety guarantees"
git push origin main
git fetch origin main
$head = (git rev-parse HEAD).Trim()
$tracking = (git rev-parse '@{upstream}').Trim()
$remote = ((git ls-remote origin refs/heads/main) -split '\s+')[0]
if ($head -ne $tracking -or $head -ne $remote) { throw "theme 4 SHA mismatch" }
```

Expected: exact Task 6 scope, scratch and unrelated paths untouched, all SHA views equal.

### Task 7: Connect covertness, surveillance, and monitoring by observation role

**Files:**

- Create: `wiki/synthesis/aerial-observation-control-covertness-surveillance-and-monitoring.md`
- Refresh: `wiki/synthesis/isac-sensing-in-aerial-mec.md`
- Modify primary sources:
  - `wiki/sources/wang-2026-covert-cognitive-radio.md`
  - `wiki/sources/lin-2026-fc-ris-surveillance.md`
  - `wiki/sources/guo-2024-multiuav-proactive-eavesdropping.md`
  - `wiki/sources/zhan-2026-star-ris-aerial-monitoring.md`
  - `wiki/sources/wang-2026-fd-covert-isac.md`
  - `wiki/sources/deng-2025-covert-isac-trajectory.md`
  - `wiki/sources/zhang-2026-irs-uav-covert-fbl.md`
- Modify supporting core sources:
  - `wiki/sources/yan-2026-uav-trajectory-monitoring.md`
  - `wiki/sources/huang-2026-intelligent-jamming-maritime.md`
- Modify concepts when accepted:
  - `wiki/concepts/primary-signal-assisted-covertness.md`
  - `wiki/concepts/sensing-signal-assisted-covertness.md`
  - `wiki/concepts/ambient-interference-aided-covertness.md`
  - `wiki/concepts/wireless-information-surveillance.md`
  - `wiki/concepts/monitoring-success-probability.md`
  - `wiki/concepts/proactive-eavesdropping.md`
  - `wiki/concepts/full-duplex-receiver-jamming.md`
  - `wiki/concepts/integrated-sensing-and-communication.md`
  - `wiki/concepts/physical-layer-security.md`
  - `wiki/concepts/star-ris.md`
  - `wiki/concepts/cooperative-jamming.md`
  - `wiki/concepts/finite-blocklength-urllc.md`
  - `wiki/concepts/cooperative-cognitive-radio.md`
  - `wiki/concepts/fully-connected-ris.md`
  - `wiki/concepts/threshold-based-antenna-selection.md`
  - `wiki/concepts/uav-trajectory-monitoring.md`
  - `wiki/concepts/position-gated-velocity-nearest-neighbor-association.md`
  - `wiki/concepts/phase-rotated-dft-motion-parameter-estimation.md`
  - `wiki/concepts/lstm-eavesdropper-trajectory-prediction.md`
- Modify navigation: `wiki/index.md`, `wiki/overview.md`, `wiki/log.md`
- Generate, do not stage: `.curation-out/research-log-theme-5-evidence.md`, `.curation-out/research-log-theme-5-after.json`
- Patch, do not stage: `.curation-out/research-log-2026-07-14-ledger.json`

- [ ] **Step 1: Verify remote continuity and graph attribution**

Run:

```powershell
git fetch origin main
$head = (git rev-parse HEAD).Trim()
$tracking = (git rev-parse '@{upstream}').Trim()
$remote = ((git ls-remote origin refs/heads/main) -split '\s+')[0]
if ($head -ne $tracking -or $head -ne $remote) {
    throw "theme 4 is not verified remotely"
}
git status --short --branch
python tools/wiki/graph_audit.py compare `
  --baseline .curation-out/research-log-2026-07-14-baseline.json `
  --json research-log-theme-5-before.json
```

Stop on any unexplained removed edge or overlapping user edit.

- [ ] **Step 2: Ground the observer-role matrix and fix Guo's stale path**

Read:

```text
raw/sources/UAV-Assisted_Covert_Transmission_for_Cooperative_Cognitive_Radio_Networks/UAV-Assisted_Covert_Transmission_for_Cooperative_Cognitive_Radio_Networks.md
raw/sources/UAV-Borne_FC-RIS_Empowered_Wireless_Information_Surveillance_With_Threshold-Based_Antenna_Selection/UAV-Borne_FC-RIS_Empowered_Wireless_Information_Surveillance_With_Threshold-Based_Antenna_Selection.md
raw/sources/Joint_Optimization_of_Trajectory_and_Jamming_Power_for_Multiple_UAV-Aided_Proactive_Eavesdropping/Joint_Optimization_of_Trajectory_and_Jamming_Power_for_Multiple_UAV-Aided_Proactive_Eavesdropping.md
raw/sources/UAV-Enabled_Aerial_Monitoring_Aided_by_STAR-RIS_A_Stochastic_Optimization_Framework/UAV-Enabled_Aerial_Monitoring_Aided_by_STAR-RIS_A_Stochastic_Optimization_Framework.md
raw/sources/UAV-Aided_Covert_ISAC_via_Full-Duplex_Jamming/UAV-Aided_Covert_ISAC_via_Full-Duplex_Jamming.md
raw/sources/Joint_Beamforming_and_UAV_Trajectory_Optimization_for_Covert_Communications_in_ISAC_Networks/Joint_Beamforming_and_UAV_Trajectory_Optimization_for_Covert_Communications_in_ISAC_Networks.md
raw/sources/Joint_Trajectory_and_Beamforming_Optimization_for_IRS-Assisted_Multi-Antenna_UAV_Covert_Communications_With_a_Finite_Blocklength/Joint_Trajectory_and_Beamforming_Optimization_for_IRS-Assisted_Multi-Antenna_UAV_Covert_Communications_With_a_Finite_Blocklength.md
```

Correct the Guo source page's stale `full.md` reference to its verified title-named parse. Populate `.curation-out/research-log-theme-5-evidence.md` with observer, observed party, controller, desired observation outcome, masking/interception/monitoring mechanism, metric, detector assumption, horizon, and proof/evidence scope.

- [ ] **Step 3: Confirm at least 18 missing core-to-core edges**

Disposition:

```text
wang-2026-covert-cognitive-radio <-> lin-2026-fc-ris-surveillance
wang-2026-fd-covert-isac <-> lin-2026-fc-ris-surveillance
lin-2026-fc-ris-surveillance <-> zhan-2026-star-ris-aerial-monitoring
wireless-information-surveillance <-> zhan-2026-star-ris-aerial-monitoring
monitoring-success-probability <-> zhan-2026-star-ris-aerial-monitoring
zhan-2026-star-ris-aerial-monitoring <-> yan-2026-uav-trajectory-monitoring
zhan-2026-star-ris-aerial-monitoring <-> uav-trajectory-monitoring
lin-2026-fc-ris-surveillance <-> yan-2026-uav-trajectory-monitoring
wireless-information-surveillance <-> uav-trajectory-monitoring
monitoring-success-probability <-> uav-trajectory-monitoring
wang-2026-fd-covert-isac <-> yan-2026-uav-trajectory-monitoring
wang-2026-fd-covert-isac <-> phase-rotated-dft-motion-parameter-estimation
wang-2026-covert-cognitive-radio <-> huang-2026-intelligent-jamming-maritime
wang-2026-fd-covert-isac <-> huang-2026-intelligent-jamming-maritime
full-duplex-receiver-jamming <-> huang-2026-intelligent-jamming-maritime
primary-signal-assisted-covertness <-> huang-2026-intelligent-jamming-maritime
lstm-eavesdropper-trajectory-prediction <-> uav-trajectory-monitoring
lstm-eavesdropper-trajectory-prediction <-> position-gated-velocity-nearest-neighbor-association
lstm-eavesdropper-trajectory-prediction <-> phase-rotated-dft-motion-parameter-estimation
huang-2026-intelligent-jamming-maritime <-> yan-2026-uav-trajectory-monitoring
primary-signal-assisted-covertness <-> wireless-information-surveillance
full-duplex-receiver-jamming <-> wireless-information-surveillance
primary-signal-assisted-covertness <-> full-duplex-receiver-jamming
fully-connected-ris <-> zhan-2026-star-ris-aerial-monitoring
threshold-based-antenna-selection <-> zhan-2026-star-ris-aerial-monitoring
cooperative-cognitive-radio <-> wireless-information-surveillance
```

Accept at least 18 after parse review. Prioritize baseline-degree-one `full-duplex-receiver-jamming` and `lstm-eavesdropper-trajectory-prediction`, and choose cross-component links that join covertness, surveillance, physical monitoring, trajectory tracking, and maritime jamming.

- [ ] **Step 4: Write the synthesis and narrowly refresh ISAC navigation**

Create:

```markdown
---
type: synthesis
title: "Aerial observation control: covertness, surveillance, and monitoring"
tags: [synthesis, covertness, surveillance, monitoring, isac, physical-layer-security]
related:
  - "[[wang-2026-covert-cognitive-radio]]"
  - "[[lin-2026-fc-ris-surveillance]]"
  - "[[guo-2024-multiuav-proactive-eavesdropping]]"
  - "[[zhan-2026-star-ris-aerial-monitoring]]"
  - "[[wang-2026-fd-covert-isac]]"
  - "[[deng-2025-covert-isac-trajectory]]"
  - "[[zhang-2026-irs-uav-covert-fbl]]"
  - "[[primary-signal-assisted-covertness]]"
  - "[[sensing-signal-assisted-covertness]]"
  - "[[wireless-information-surveillance]]"
  - "[[monitoring-success-probability]]"
  - "[[proactive-eavesdropping]]"
  - "[[full-duplex-receiver-jamming]]"
  - "[[isac-sensing-in-aerial-mec]]"
created: 2026-07-14
updated: 2026-07-14
---

# Aerial observation control: covertness, surveillance, and monitoring

## Observer, observed party, and controller

## Role inversion: hiding, intercepting, and monitoring

## Covertness mechanisms

## Surveillance mechanisms

## Aerial monitoring as stochastic service control

## Metrics and detector assumptions

## Mobility, horizon, and control surfaces

## Explicit non-comparability

## Gaps
```

Do not equate covert rate/detection error, monitoring success probability/rate, eavesdropping success, tracking error, and long-term monitoring throughput. In `isac-sensing-in-aerial-mec.md`, describe its seven-source roster as a bounded cross-section, link this new synthesis, and correct only gap statements contradicted by the seven current parses.

- [ ] **Step 5: Add reciprocal links and shared navigation**

Add accepted core pairs reciprocally and the new synthesis backlink to all primary sources/concepts and the refreshed ISAC page. Add under `## Synthesis`:

```markdown
- [[aerial-observation-control-covertness-surveillance-and-monitoring]] — Hiding, legitimate interception, physical monitoring, and trajectory tracking separated by observer role, mechanism, and metric.
```

Run `python tools/wiki/corpus_counts.py --update-overview`, add durable overview navigation, prepend the dated log entry with graph deltas, and patch ledger evidence/status rows.

- [ ] **Step 6: Complete independent review and graph acceptance**

Give a fresh read-only reviewer all primary/supporting pages, verified parses, evidence matrix, synthesis, refreshed ISAC page, and full diff. Require:

```text
Return ACCEPT, REVISE, or REJECT for every claim and edge with a parse heading
and distinctive locator. Identify observer, observed party, controller, and
desired observation outcome. Reject generic links or equivalence among covert
detection, legitimate interception, physical monitoring, and trajectory
tracking metrics.
```

Apply revisions, then run:

```powershell
python tools/wiki/graph_audit.py compare `
  --baseline .curation-out/research-log-2026-07-14-baseline.json `
  --json research-log-theme-5-after.json `
  --ledger .curation-out/research-log-2026-07-14-ledger.json
```

Require no removed edge, at least 90 cumulative added internal edges, at least one component merge, both prioritized degree-one pages promoted, and an accepted evidence row for every added pair.

- [ ] **Step 7: Run all repository gates**

```powershell
python tools/wiki/curation_status.py --dupes
python tools/wiki/corpus_counts.py
python tools/wiki/linkcheck.py --orphans
python tools/wiki/process_refs.py
python tools/wiki/index_audit.py
python tools/wiki/frontmatter_audit.py
python tools/wiki/entity_roster_audit.py
python -m unittest discover -s tools/wiki/tests -p "test_*.py" -v
git diff --check
```

Expected: every failure count zero, tests `OK`, no new semantic orphan, no whitespace error.

- [ ] **Step 8: Stage, commit, push, and verify only Task 7**

```powershell
git add wiki/synthesis/aerial-observation-control-covertness-surveillance-and-monitoring.md wiki/synthesis/isac-sensing-in-aerial-mec.md wiki/sources/wang-2026-covert-cognitive-radio.md wiki/sources/lin-2026-fc-ris-surveillance.md wiki/sources/guo-2024-multiuav-proactive-eavesdropping.md wiki/sources/zhan-2026-star-ris-aerial-monitoring.md wiki/sources/wang-2026-fd-covert-isac.md wiki/sources/deng-2025-covert-isac-trajectory.md wiki/sources/zhang-2026-irs-uav-covert-fbl.md wiki/sources/yan-2026-uav-trajectory-monitoring.md wiki/sources/huang-2026-intelligent-jamming-maritime.md wiki/concepts/primary-signal-assisted-covertness.md wiki/concepts/sensing-signal-assisted-covertness.md wiki/concepts/ambient-interference-aided-covertness.md wiki/concepts/wireless-information-surveillance.md wiki/concepts/monitoring-success-probability.md wiki/concepts/proactive-eavesdropping.md wiki/concepts/full-duplex-receiver-jamming.md wiki/concepts/integrated-sensing-and-communication.md wiki/concepts/physical-layer-security.md wiki/concepts/star-ris.md wiki/concepts/cooperative-jamming.md wiki/concepts/finite-blocklength-urllc.md wiki/concepts/cooperative-cognitive-radio.md wiki/concepts/fully-connected-ris.md wiki/concepts/threshold-based-antenna-selection.md wiki/concepts/uav-trajectory-monitoring.md wiki/concepts/position-gated-velocity-nearest-neighbor-association.md wiki/concepts/phase-rotated-dft-motion-parameter-estimation.md wiki/concepts/lstm-eavesdropper-trajectory-prediction.md wiki/index.md wiki/overview.md wiki/log.md
git diff --cached --name-only
git diff --cached --check
rg -n -i "(api[_-]?key|token|password|secret|authorization:|bearer )" -- $(git diff --cached --name-only)
git commit -m "Connect aerial observation control roles"
git push origin main
git fetch origin main
$head = (git rev-parse HEAD).Trim()
$tracking = (git rev-parse '@{upstream}').Trim()
$remote = ((git ls-remote origin refs/heads/main) -split '\s+')[0]
if ($head -ne $tracking -or $head -ne $remote) { throw "theme 5 SHA mismatch" }
```

Expected: exact Task 7 scope, scratch/unrelated paths untouched, all SHA views equal.

### Task 8: Resolve the residual cohort until all local thresholds pass

**Files:**

- Read and patch: `.curation-out/research-log-2026-07-14-ledger.json`
- Read: `.curation-out/research-log-theme-5-after.json`
- Generate per loop, do not stage: `.curation-out/research-log-residual-N-evidence.md`, where `N` is the next positive integer
- Generate per loop, do not stage: `.curation-out/research-log-residual-N-after.json`
- Modify per loop: only the exact frozen-member pages accepted by that loop's evidence matrix
- Modify per loop: `wiki/index.md` only if a derived page is created
- Modify per loop: `wiki/overview.md` only for durable navigation/count changes
- Modify per loop: `wiki/log.md`

This task is deliberately data-dependent: exact residual page paths come from the frozen ledger after Tasks 3–7. Predetermining them would manufacture semantic links before the evidence review. The selection and acceptance algorithm below is fixed.

- [ ] **Step 1: Compute the current residual queues**

Run:

```powershell
$ledger = Get-Content -LiteralPath .curation-out/research-log-2026-07-14-ledger.json -Raw -Encoding utf8 | ConvertFrom-Json
$report = Get-Content -LiteralPath .curation-out/research-log-theme-5-after.json -Raw -Encoding utf8 | ConvertFrom-Json
$degree = @{}
foreach ($property in $report.graph.internal_degrees.PSObject.Properties) {
    $degree[$property.Name] = [int]$property.Value
}
$pending = @($ledger.entries | Where-Object status -eq 'pending')
$weakPending = @($pending | Where-Object { $degree[$_.slug] -le 1 } | Sort-Object @{Expression={$degree[$_.slug]}}, baseline_component, slug)
$fragmentedPending = @($pending | Sort-Object baseline_component, @{Expression={$degree[$_.slug]}}, slug)
"pending=$($pending.Count) weak_pending=$($weakPending.Count)"
$weakPending | Select-Object -First 30 slug, type, baseline_component, baseline_internal_degree
```

Expected: deterministic unresolved and weak-first queues. Do not treat the first 30 rows as an automatic batch.

- [ ] **Step 2: Select one evidence-coherent residual batch**

Choose 15–25 pages that satisfy all of:

1. at least half are currently degree zero or one while the weak threshold is unmet;
2. at least two current components are represented while the component threshold is unmet;
3. a shared mechanism, constraint, metric contrast, dependency, author/tool relationship, or system-model assumption is already visible in current pages;
4. the relevant current raw parses are available;
5. no proposed pair is already an induced edge.

Record the exact chosen slugs and rejected near-neighbors under `## Scope` in the numbered residual evidence file. If the set does not form a coherent analytical question, shrink or repartition it before reading/writing.

- [ ] **Step 3: Ground every residual claim and edge**

For each chosen source page, open the exact parse recorded in its Raw artifacts block. For a concept/entity/analytical page, trace its proposed relationship to the current parses of the source pages that define it. Populate the standard evidence matrix and accept only relationships with exact locators.

Use these status rules:

```text
linked   = the frozen member gained at least one accepted core-to-core edge
derived  = an accepted analytical page represents it and reciprocal navigation exists
deferred = current parses were reviewed and the ledger gives a concrete reason
pending  = review is incomplete; never allowed at program close
```

An entity is not linked merely because it shares an author name with an unrelated paper. A concept is not linked merely because two pages share a broad tag.

- [ ] **Step 4: Edit the accepted frozen pages and optional derived page**

Add accepted pairs reciprocally to `related:` and explain their rationale in the batch evidence matrix or an evidence-earned analytical page. Preserve all unrelated prose and frontmatter. Create a finding/synthesis/comparison/methodology/query/thesis only when the matrix establishes a real cross-source analytical shape; use the existing page type's frontmatter conventions and add it exactly once to the matching `wiki/index.md` section.

Patch every reviewed ledger row to `linked`, `derived`, or `deferred`. A deferred row must contain nonempty `evidence_paths` and `deferral_reason`; a linked/derived row must contain nonempty `evidence_paths` and `accepted_links`.

- [ ] **Step 5: Independently review and compare the residual batch**

Give a fresh read-only reviewer the selected wiki pages, their parses, evidence matrix, and all diffs. Require:

```text
Return ACCEPT, REVISE, or REJECT for every claim and new edge with the exact
parse heading and a distinctive locator. Separate paper fact from inference.
Reject generic same-topic links, incompatible comparisons, stale paths, and
reciprocal links whose rationale is absent. Confirm every changed ledger status
against the evidence matrix.
```

Apply revisions, then run:

```powershell
$existingNumbers = Get-ChildItem -LiteralPath .curation-out -Filter 'research-log-residual-*-after.json' -ErrorAction SilentlyContinue |
    ForEach-Object {
        if ($_.BaseName -match '^research-log-residual-(\d+)-after$') {
            [int]$Matches[1]
        }
    }
$batchNumber = if ($existingNumbers) { ($existingNumbers | Measure-Object -Maximum).Maximum + 1 } else { 1 }
python tools/wiki/graph_audit.py compare `
  --baseline .curation-out/research-log-2026-07-14-baseline.json `
  --json "research-log-residual-$batchNumber-after.json" `
  --ledger .curation-out/research-log-2026-07-14-ledger.json
```

Require no removed frozen edge. While a metric remains below acceptance, the batch must improve that metric: add at least one internal edge; reduce components when fragmented components were selected; reduce weak-member count when weak pages were selected. Every added pair must have an accepted matrix row.

- [ ] **Step 6: Gate, commit, push, and verify one residual batch**

Run:

```powershell
python tools/wiki/corpus_counts.py --update-overview
python tools/wiki/curation_status.py --dupes
python tools/wiki/corpus_counts.py
python tools/wiki/linkcheck.py --orphans
python tools/wiki/process_refs.py
python tools/wiki/index_audit.py
python tools/wiki/frontmatter_audit.py
python tools/wiki/entity_roster_audit.py
python -m unittest discover -s tools/wiki/tests -p "test_*.py" -v
git diff --check
```

Review and stage an explicit per-batch allowlist generated from the accepted matrix; never use `git add .` or `git add -A`. Require `git diff --cached --check` and the credential scan. Commit with the exact numbered form `Connect Research Log residual cohort batch N`, push `main`, fetch, and require `HEAD == @{upstream} == git ls-remote origin refs/heads/main`.

- [ ] **Step 7: Repeat the fixed residual loop to termination**

Repeat Steps 1–6 with the next integer batch number until both conditions hold:

1. every ledger status is `linked`, `derived`, or `deferred`;
2. the current comparison meets the calculated edge, component, and weak-member thresholds.

If all members are resolved but a metric is still below threshold, reopen the resolved weak/component queues and seek additional parse-grounded edges. If the LLM Wiki final rescan later remains at `0.03`, return here for another residual batch.

### Task 9: Run the whole-program audit and close only after the LLM Wiki rescan

**Files:**

- Modify: `wiki/log.md`
- Modify if required by final counts: `wiki/overview.md`
- Generate, do not stage: `.curation-out/research-log-final-after.json`
- Read, do not stage: `.curation-out/research-log-2026-07-14-baseline.json`
- Read, do not stage: `.curation-out/research-log-2026-07-14-ledger.json`

- [ ] **Step 1: Generate the final comparison and calculate thresholds**

Run:

```powershell
python tools/wiki/graph_audit.py compare `
  --baseline .curation-out/research-log-2026-07-14-baseline.json `
  --json research-log-final-after.json `
  --ledger .curation-out/research-log-2026-07-14-ledger.json

$baseline = Get-Content -LiteralPath .curation-out/research-log-2026-07-14-baseline.json -Raw -Encoding utf8 | ConvertFrom-Json
$final = Get-Content -LiteralPath .curation-out/research-log-final-after.json -Raw -Encoding utf8 | ConvertFrom-Json
$edgeMinimum = [math]::Ceiling([double]$baseline.graph.metrics.induced_edge_count * 1.25)
$componentMaximum = [math]::Floor([double]$baseline.graph.metrics.component_count * 0.75)
$weakMaximum = [math]::Floor([double]$baseline.graph.metrics.weak_member_count * 0.50)
if ($final.graph.metrics.induced_edge_count -lt $edgeMinimum) {
    throw "edge threshold failed"
}
if ($final.graph.metrics.component_count -gt $componentMaximum) {
    throw "component threshold failed"
}
if ($final.graph.metrics.weak_member_count -gt $weakMaximum) {
    throw "weak-member threshold failed"
}
"edges>=$edgeMinimum components<=$componentMaximum weak<=$weakMaximum"
```

For the reproduced baseline, expected thresholds are edges at least `427`, components at most `35`, and weak members at most `43`.

- [ ] **Step 2: Validate complete ledger accounting**

Run:

```powershell
$ledger = Get-Content -LiteralPath .curation-out/research-log-2026-07-14-ledger.json -Raw -Encoding utf8 | ConvertFrom-Json
$allowed = @('linked', 'derived', 'deferred')
$badStatus = @($ledger.entries | Where-Object { $_.status -notin $allowed })
$badDeferred = @($ledger.entries | Where-Object { $_.status -eq 'deferred' -and ([string]::IsNullOrWhiteSpace($_.deferral_reason) -or $_.evidence_paths.Count -eq 0) })
$badConnected = @($ledger.entries | Where-Object { $_.status -in @('linked', 'derived') -and ($_.accepted_links.Count -eq 0 -or $_.evidence_paths.Count -eq 0) })
if ($badStatus.Count -or $badDeferred.Count -or $badConnected.Count) {
    throw "ledger validation failed: status=$($badStatus.Count) deferred=$($badDeferred.Count) connected=$($badConnected.Count)"
}
$ledger.entries | Group-Object status | Sort-Object Name | Select-Object Name, Count
```

Expected: zero invalid rows and no `pending`.

- [ ] **Step 3: Audit edge provenance and the final repository tree**

Cross-check every `final.comparison.added_edges` pair against the accepted rows in the five theme matrices and all numbered residual matrices. Then run:

```powershell
python tools/wiki/corpus_counts.py --update-overview
python tools/wiki/curation_status.py --dupes
python tools/wiki/corpus_counts.py
python tools/wiki/linkcheck.py --orphans
python tools/wiki/process_refs.py
python tools/wiki/index_audit.py
python tools/wiki/frontmatter_audit.py
python tools/wiki/entity_roster_audit.py
python -m unittest discover -s tools/wiki/tests -p "test_*.py" -v
git diff --check
```

Expected: all failing categories zero, tests `OK`, complete unique catalogue coverage, no new semantic orphan, and no whitespace error.

- [ ] **Step 4: Trigger and inspect a fresh LLM Wiki rescan**

Invoke the `llm-wiki` skill, then open the configured LLM Wiki app at `http://127.0.0.1:19828`, select this repository, trigger its current rescan/re-index action, and wait for completion. Open the Insights view and inspect the Research Log sparse-cluster result.

Record one of these exact outcomes:

```text
PASS: Research Log sparse-cluster insight absent after rescan.
PASS: Research Log displayed cohesion is greater than 0.03 after rescan.
FAIL: Research Log remains at cohesion 0.03 or lower after rescan.
```

On `FAIL`, do not close the program: return to Task 8 with the rescan's current page count and cluster clues.

- [ ] **Step 5: Record the final durable audit**

After a passing rescan, prepend one final `2026-07-14` entry to `wiki/log.md` containing:

- baseline member hash and final member hash;
- baseline/final edge, cohesion, component, isolate, weak, and bridge counts;
- ledger counts for linked/derived/deferred;
- the exact LLM Wiki rescan outcome and displayed page/cohesion values when present;
- the thematic and residual commit SHAs.

Do not copy the transient ledger or evidence matrices into evergreen pages.

- [ ] **Step 6: Re-run gates after the log edit, commit, push, and verify**

Run:

```powershell
python tools/wiki/corpus_counts.py --update-overview
python tools/wiki/curation_status.py --dupes
python tools/wiki/corpus_counts.py
python tools/wiki/linkcheck.py --orphans
python tools/wiki/process_refs.py
python tools/wiki/index_audit.py
python tools/wiki/frontmatter_audit.py
python tools/wiki/entity_roster_audit.py
python -m unittest discover -s tools/wiki/tests -p "test_*.py" -v
git diff --check
```

Then:

```powershell
git add wiki/log.md wiki/overview.md
git diff --cached --name-only
git diff --cached --check
rg -n -i "(api[_-]?key|token|password|secret|authorization:|bearer )" -- $(git diff --cached --name-only)
git commit -m "Record Research Log cohesion program completion"
git push origin main
git fetch origin main
$head = (git rev-parse HEAD).Trim()
$tracking = (git rev-parse '@{upstream}').Trim()
$remote = ((git ls-remote origin refs/heads/main) -split '\s+')[0]
if ($head -ne $tracking -or $head -ne $remote) {
    throw "final SHA mismatch: HEAD=$head tracking=$tracking remote=$remote"
}
git status --short --branch
```

Expected: only `wiki/log.md` and a mechanically changed `wiki/overview.md` are committed; all SHA views match. Preserve any unrelated user worktree change. The goal is complete only after this remote verification succeeds.
