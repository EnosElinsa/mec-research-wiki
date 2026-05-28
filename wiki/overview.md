---
type: overview
title: Project Overview
tags: [mec, research-wiki]
related:
  - "[[mobile-edge-computing]]"
  - "[[liu-2026-jppo-en-convntm]]"
  - "[[design-recipe-multi-uav-mec]]"
---

# Overview

This is a long-running research wiki on **mobile edge computing (MEC)** broadly construed — covering task offloading, resource allocation, trajectory and infrastructure design, and intelligent decision-making algorithms across UAV, LEO-satellite, vehicular, and terrestrial deployments.

The scope is intentionally open-ended. Sources accumulate as the corpus grows; the page-type vocabulary in `schema.md` is generic enough to absorb new sub-topics without restructuring.

## Snapshot

- **Curated sources:** 1 — [[liu-2026-jppo-en-convntm]] (Multi-UAV path planning for MEC under high-density mobility).
- **Raw, awaiting curation:** 11 papers under `raw/sources/` covering UAV trajectory design, multi-agent DRL for offloading, wireless-powered MEC, blockchain / zero-trust offloading on LEO satellites, low-altitude economy networks, UAV swarm spectrum sharing, and vehicular UAV data fusion.
- **Working synthesis (UAV-MEC track):** [[design-recipe-multi-uav-mec]] — a 10-step recipe for DRL-controlled UAV-MEC under dense mobility.
- **Working thesis (UAV-MEC track):** [[hybrid-action-memory-augmented-drl-wins-uav-mec]] — `supported`, medium confidence, single-source.

These working positions belong to *one track* (UAV-MEC) within the wider MEC scope. Other tracks (LEO offloading, vehicular MEC, wireless-powered MEC, etc.) will get their own theses and syntheses as their respective sources get curated.

## Open questions, current

- [[query-real-world-validation-of-jppo-en-convntm]] — sim-to-real transfer.
- [[query-does-en-convntm-generalize-beyond-uav-mec]] — does the EN-ConvNTM design hold outside UAV-MEC grids?

## Where to go next

- `wiki/index.md` — full type-grouped page directory.
- `wiki/log.md` — reverse-chronological activity log.
- `raw/sources/` — papers awaiting curation. Pick any to ingest next.
