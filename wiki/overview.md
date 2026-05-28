---
type: overview
title: Project Overview
tags: [mec, research-wiki]
related:
  - "[[mobile-edge-computing]]"
  - "[[wang-2025-lae-network-survey]]"
  - "[[design-recipe-multi-uav-mec]]"
---

# Overview

A long-running research wiki on **mobile edge computing (MEC)** broadly construed — task offloading, resource allocation, trajectory and infrastructure design, and intelligent decision-making algorithms across UAV, LEO-satellite, vehicular, and terrestrial deployments. Open-ended scope; sources accumulate as the corpus grows.

## Snapshot

- **Curated sources:** 12 (initial corpus complete) — see `wiki/index.md` for the type-grouped directory.
- **Concepts:** ~50 across MEC fundamentals, aerial architectures, DRL backbones, optimization techniques, security/federation, metrics, and safety.
- **Methodology / findings / thesis / synthesis:** anchored in the UAV-MEC track ([[liu-2026-jppo-en-convntm]] and follow-ups). Other tracks (LEO security, vehicular perception, low-altitude economy) have curated sources but not yet thesis pages.

## Tracks emerging from the corpus

| Track | Representative sources | Status |
|---|---|---|
| UAV-MEC + DRL | [[liu-2026-jppo-en-convntm]], [[peng-2025-drudm-cfg]], [[zhang-2025-ssac-mgi-heterogeneous-uav]], [[bi-2025-sg-mapg]] | Working thesis: [[hybrid-action-memory-augmented-drl-wins-uav-mec]] |
| Vehicular-MEC | [[zhang-2025-mcma-task-migration]], [[xie-2026-uav-multisource-fusion]] | Two sources, no thesis yet |
| Trust / security / federation | [[mao-2025-bcsa-frl]], [[qin-2025-bcuav-masac]] | Two sources, no thesis yet |
| Spectrum / governance / architecture | [[wang-2025-uav-swarm-stackelberg]], [[wang-2025-lae-network-survey]] | Foundational, anchors the broader LAE umbrella |
| Energy efficiency & WPT | [[zhu-2025-lycnn-drl-wpt-mec]] | Single-source so far |
| Generic offloading techniques | [[hao-2025-priority-aware-task-driven-co]] | Single-source so far |

## Cross-cutting observations from the first 12 sources

1. **Lyapunov + DRL hybrids are the dominant pattern** for long-term-constrained per-slot MEC optimization ([[qin-2025-bcuav-masac]], [[zhu-2025-lycnn-drl-wpt-mec]], plus the classical decompositions in others).
2. **CTDE is the default multi-agent paradigm** ([[peng-2025-drudm-cfg]], [[zhang-2025-mcma-task-migration]], [[zhang-2025-ssac-mgi-heterogeneous-uav]], [[qin-2025-bcuav-masac]]).
3. **Stackelberg + matching** keeps showing up at the resource-allocation / pricing layer ([[wang-2025-uav-swarm-stackelberg]], [[bi-2025-sg-mapg]]).
4. **Fairness metrics fragment** — Jain ([[liu-2026-jppo-en-convntm]]) vs Theil ([[peng-2025-drudm-cfg]]). A side-by-side comparison page would help future cross-source synthesis.
5. **Most papers are simulation-only.** The wiki has 0 hardware-validated curated sources. Worth noting in any thesis claim.

## Open questions

- [[query-real-world-validation-of-jppo-en-convntm]] — sim-to-real transfer.
- [[query-does-en-convntm-generalize-beyond-uav-mec]] — generalization of memory-augmented encoders.
- (More to come as additional sources highlight new gaps.)

## Where to go next

- `wiki/index.md` — full type-grouped page directory.
- `wiki/log.md` — reverse-chronological activity log.
- `raw/sources/` — drop new papers here for the next curation pass.
