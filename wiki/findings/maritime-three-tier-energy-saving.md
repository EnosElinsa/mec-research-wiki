---
type: finding
title: Three-tier maritime offloading saves 39.3% system energy vs benchmarks
source: "[[zhang-2025-three-tier-maritime-offloading]]"
confidence: medium
replicated: null
tags: [maritime-mec, energy, offloading, benchmark]
related:
  - "[[maritime-mec]]"
  - "[[three-tier-cloud-edge-end]]"
  - "[[mixed-integer-nonlinear-programming]]"
  - "[[energy-latency-tradeoff]]"
  - "[[maritime-mec-architectures]]"
created: 2026-05-30
updated: 2026-05-30
---

# Three-tier maritime offloading saves 39.3% system energy vs benchmarks

In [[zhang-2025-three-tier-maritime-offloading]], the proposed three-tier (MWD / OBS / LEO-satellite) computation-offloading scheme reduces total system energy consumption under latency constraints. The headline number is stated explicitly in both the abstract and the results discussion:

> "the proposed algorithm saves 39.3% of system energy consumption compared to benchmark schemes" (parse abstract; restated in the simulation-results section).

## Mechanism

The system jointly optimizes the association variable, task partitioning, transmission power, and computing-resource allocation, formulated as a [[mixed-integer-nonlinear-programming|MINLP]] problem and decomposed into four subproblems:

1. association variable — slack-variable method;
2. transmission power — quadratic transformation + difference-of-convex algorithm;
3. task partitioning — closed-form offload-size bounds, then standard convex solve;
4. joint LEO/OBS computing-resource allocation — Lagrangian dual method.

Each iteration provably lowers the objective (system energy), so the iterative scheme converges monotonically.

## Caveats

- Single-paper result, simulation only — `confidence: medium`. The 10 km × 10 km LEO deployment, 2 MB task size, and altitude range [400, 500] km are the parse's stated simulation parameters.
- "39.3%" is an aggregate over the benchmark set; the per-benchmark margin varies with MWD count, LEO count, and MWD compute capacity (parse Figs. 6 and 8 show the trends).
- The benchmarks are alternative offloading/resource-allocation heuristics, not other full three-tier schemes.

## Relation to the corpus

Anchors the energy-saving end of the [[maritime-mec-architectures]] synthesis alongside the other maritime sources ([[wang-2026-aerial-marine-msar]], [[wang-2025-double-edge-samin]], [[you-2025-uncertain-maritime-hasac]], [[wang-2024-twotier-satellite-marine]], [[liu-2025-haps-uav-maritime-iot]], [[zhang-2024-dlrl-maritime-usv]]). It is the clearest "classical MINLP decomposition saves N%" data point in the maritime track.
