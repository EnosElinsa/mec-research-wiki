---
type: concept
title: "Non-Dominated Sorting Genetic Algorithm-II (NSGA-II)"
tags: [evolutionary, multi-objective, pareto, classical-solver]
related:
  - "[[constrained-multi-objective-evolutionary-algorithm]]"
  - "[[pan-2025-uav-ris-energy-efficient-comm]]"
created: 2026-06-03
updated: 2026-06-03
---

# Non-Dominated Sorting Genetic Algorithm-II (NSGA-II)

A widely used multi-objective evolutionary algorithm that evolves a population toward the Pareto front by ranking individuals with **fast non-dominated sorting** (assigning each solution to a dominance front) and breaking ties within a front by **crowding distance** (a density measure that preserves diversity along the front). Elitist selection then combines parents and offspring and keeps the best fronts. The result of one run is a **set** of non-dominated trade-off solutions rather than a single scalarized optimum, so a decision-maker can choose after seeing the front. NSGA-II is a canonical member of the broader [[constrained-multi-objective-evolutionary-algorithm|CMOEA]] family.

Because the base algorithm assumes continuous, real-valued genes, applying it to mixed problems usually requires problem-specific encoding/operators for discrete or complex-valued variables.

In the wiki, [[pan-2025-uav-ris-energy-efficient-comm]] builds **INSGA-II-CDC**, an improved NSGA-II augmented with continuous, discrete, and complex solution-processing mechanisms, so a single run can jointly handle UAV-RIS 3D locations (continuous), discrete RIS phase shifts, and the complex-valued BS beamforming vector while returning a Pareto set across its three objectives (max-min rate, max total rate, min energy).
