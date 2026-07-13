---
type: concept
title: "Non-Dominated Sorting Genetic Algorithms (NSGA-II / NSGA-III)"
tags: [evolutionary, multi-objective, pareto, classical-solver]
related:
  - "[[guo-2026-dual-objective-multiuav-isac]]"
  - "[[constrained-multi-objective-evolutionary-algorithm]]"
  - "[[pan-2025-uav-ris-energy-efficient-comm]]"
  - "[[jiang-2026-bi-level-uav-delivery-safety]]"
  - "[[kanani-2026-haps-uav-isac]]"
created: 2026-06-03
updated: 2026-07-14
---

# Non-Dominated Sorting Genetic Algorithms (NSGA-II / NSGA-III)

The NSGA family evolves a population toward a Pareto front by ranking individuals with non-dominated sorting and then preserving diversity along that front. NSGA-II uses crowding distance, while NSGA-III replaces that diversity mechanism with reference points so the method scales better to many-objective problems. The result of one run is a **set** of non-dominated trade-off solutions rather than a single scalarized optimum, so a decision-maker can choose after seeing the front. The family is a canonical member of the broader [[constrained-multi-objective-evolutionary-algorithm|CMOEA]] family.

Because the base algorithm assumes continuous, real-valued genes, applying it to mixed problems usually requires problem-specific encoding/operators for discrete or complex-valued variables.

In the wiki, [[pan-2025-uav-ris-energy-efficient-comm]] builds **INSGA-II-CDC**, an improved NSGA-II augmented with continuous, discrete, and complex solution-processing mechanisms, so a single run can jointly handle UAV-RIS 3D locations (continuous), discrete RIS phase shifts, and the complex-valued BS beamforming vector while returning a Pareto set across its three objectives (max-min rate, max total rate, min energy).

[[jiang-2026-bi-level-uav-delivery-safety]] uses a task-collaborative NSGA-III variant (TC-NSGA-III) for UAV delivery allocation, returning tradeoffs across delivery-time cost, total ground risk, and workload balance before the lower-level RG-FMT* path planner enforces [[target-level-of-safety]].

[[kanani-2026-haps-uav-isac]] uses NSGA-II to retain target-echo-power and worst-user-SINR trade-offs that a weighted-sum GA or PPO reward can miss on non-convex parts of the Pareto front.
