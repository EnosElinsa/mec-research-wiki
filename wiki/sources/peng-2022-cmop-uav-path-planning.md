---
type: source
title: "Constrained Multi-Objective Optimization for UAV-Enabled Mobile Edge Computing: Offloading Optimization and Path Planning"
authors: ["Chaoda Peng", "Xumin Huang", "Yuan Wu", "Jiawen Kang"]
year: 2022
url: "https://doi.org/10.1109/LWC.2022.3149007"
venue: "IEEE Wireless Communications Letters"
tags: [uav, mec, cmop, evolutionary-algorithm, b-spline-trajectory, infeasible-individuals, safe-flight]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[uav-trajectory-control]]"
  - "[[constrained-multi-objective-evolutionary-algorithm]]"
  - "[[b-spline-trajectory]]"
  - "[[infeasible-individual-utilization]]"
  - "[[wu-2026-terrain-aware-uav-mec]]"
  - "[[peng-2024-energy-time-uav-its]]"
created: 2026-05-29
updated: 2026-05-29
---

# Constrained Multi-Objective Optimization for UAV-Enabled MEC: Offloading Optimization and Path Planning

## Citation

Peng, C., Huang, X., Wu, Y., & Kang, J. (2022). *Constrained Multi-Objective Optimization for UAV-Enabled Mobile Edge Computing: Offloading Optimization and Path Planning*. **IEEE Wireless Communications Letters**. DOI: 10.1109/LWC.2022.3149007.

## TL;DR

A single UAV sequentially visits I device locations to offer offloading services, then flies to a final destination. The paper jointly optimizes:

- **Energy-efficient offloading** — device transmit power, UAV CPU frequency, UAV flight speed.
- **Safe path planning** — a B-spline curve through λ control points, kept above the minimum flight altitude, below the max altitude, with bounded turning angle, and far from terrain obstacles.

These are two genuinely conflicting objectives, framed as a **CMOP**. The authors solve it with a **constrained decomposition-based multi-objective evolutionary algorithm** that explicitly **uses infeasible individuals with good objective values** to inform the search before driving the population back to the feasible region.

## Why this matters

This 2022 letter is the **methodological seed** for a whole sub-thread by the same group that now spans the wiki: [[peng-2024-energy-time-uav-its]] (UAV-ITS energy + time-difference), [[wu-2026-terrain-aware-uav-mec]] (urban terrain awareness), [[xie-2026-uav-multisource-fusion]] (cooperative perception), and [[huang-2023-mu-aec-task-energy]] (multi-UAV interdependent tasks). All inherit the **CMOP + evolutionary** template — UAV trajectory as B-spline, infeasibility-aware constraint handling, two conflicting objectives — and refine it for new scenarios.

It's worth treating this paper as the **canonical reference** for the wiki's evolutionary / non-DRL UAV-MEC stream. When users ask "why evolutionary instead of DRL here," the answer pattern is set here:

1. The objectives are **truly conflicting** with no obvious scalar combination.
2. The constraints (turning angle, terrain, altitude) are **non-differentiable** and brittle under DRL gradients.
3. The decision space is mixed-integer (offloading association is discrete; trajectory is continuous) and population-based search handles that gracefully.

## Method outline

- **Decision vector x.** λ B-spline control points (3λ continuous) + per-device {p_i^tx, f_UAV,i, v_i} (3I continuous).
- **Objectives.**
  - G₁ = D_s = Σ (d_safe / d_{j,k})² over path-mesh-point distances within d_safe — minimize to stay clear of obstacles.
  - G₂ = Σᵢ E_i — total UAV energy consumption.
- **Constraints.** Hovering+flight time deadline T_i; min/max flight altitude; turning angle ≤ θ_max.
- **Algorithm.** Decomposition-based evolutionary algorithm with **dynamic infeasibility allocation** (parameter α controls how many infeasible-but-good individuals are retained per generation). Early generations explore freely; later generations push toward feasibility.

## Findings

- Infeasible-individual retention beats both ToP and PPS (the previous-SOTA constrained evolutionary algorithms) on Pareto convergence and diversity.
- Best path: low altitude where terrain allows, climbing only to clear obstacles. Naive straight-line flight either crashes or wastes energy on excessive altitude.

## Limitations

- I = 1 device in the experiments — multi-device generalization is not empirically validated here (it lands later in the lineage).
- Evolutionary cost is high (3 × 10⁴ function evaluations per run) — not real-time. Suitable for mission-planning, not online control.
- B-spline path is optimized end-to-end before flight; no in-flight replanning. Real obstacles change.

## Cross-link with related sources

- **Lineage anchor:** the seed of the wiki's evolutionary UAV-MEC thread. A dedicated lineage synthesis page should be written once a few more entries land.
- **Direct refinements:** [[peng-2024-energy-time-uav-its]] (adds time-balancing objective + multi-UAV), [[wu-2026-terrain-aware-uav-mec]] (terrain-aware channel model, multi-tasking CMOEA), [[huang-2025-cmop-dispersed-computing]] (dispersed-computing variant), [[huang-2023-mu-aec-task-energy]] (interdependent task graph).
- **Different solver class** from the DRL papers — see contrast in [[drl-backbones-across-uav-mec-sources]].

## Raw artifacts

- `raw/sources/Constrained_Multi-Objective_Optimization_for_UAV-Enabled_Mobile_Edge_Computing_Offloading_Optimization_and_Path_Planning/full.md`
