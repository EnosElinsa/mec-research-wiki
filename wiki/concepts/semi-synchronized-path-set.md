---
type: concept
title: "Semi-Synchronized Path Set"
tags: [wideband, path-selection, synchronization, cell-free-massive-mimo]
related:
  - "[[hong-2026-beam-delay-alignment]]"
  - "[[beam-delay-alignment-transmission]]"
  - "[[graph-neural-network]]"
created: 2026-07-14
updated: 2026-07-14
---

# Semi-Synchronized Path Set

An AP-local set of user propagation paths whose compensated-delay mismatches are pairwise within a cyclic-prefix-derived tolerance. Restricting service to such a set allows broad distributed cooperation while excluding path combinations that would create the modeled ICI/ISI.

In [[hong-2026-beam-delay-alignment]], compatible paths form a graph and an SSP-Set is a clique. A GCN ranks nodes before greedy maximal-clique construction and gain/resource filtering; this candidate procedure is not guaranteed to return the maximum clique or globally optimal path set.
