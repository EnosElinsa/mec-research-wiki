---
type: source
title: "Constrained Multi-Objective Optimization for UAV-Enabled Mobile Edge Computing: Offloading Optimization and Path Planning"
authors: ["Chaoda Peng", "Xumin Huang", "Yuan Wu", "Jiawen Kang"]
year: 2022
url: "https://doi.org/10.1109/LWC.2022.3149007"
venue: "IEEE Wireless Communications Letters"
tags: [source, uav, mec, cmop, evolutionary-algorithm, b-spline-trajectory, infeasible-individuals, safe-flight]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[uav-trajectory-control]]"
  - "[[constrained-multi-objective-evolutionary-algorithm]]"
  - "[[b-spline-trajectory]]"
  - "[[infeasible-individual-utilization]]"
  - "[[wu-2026-terrain-aware-uav-mec]]"
  - "[[peng-2024-energy-time-uav-its]]"
created: 2026-05-29
updated: 2026-07-16
modeling_card: required
---

# Constrained Multi-Objective Optimization for UAV-Enabled MEC: Offloading Optimization and Path Planning

## Citation

Peng, C., Huang, X., Wu, Y., & Kang, J. (2022). *Constrained Multi-Objective Optimization for UAV-Enabled Mobile Edge Computing: Offloading Optimization and Path Planning*. **IEEE Wireless Communications Letters**. DOI: 10.1109/LWC.2022.3149007.

## TL;DR

A single UAV sequentially visits I device locations to offer offloading services, then flies to a final destination. The paper jointly optimizes:

- **Energy-efficient offloading** — device transmit power, UAV CPU frequency, UAV flight speed.
- **Safe path planning** — a B-spline curve through λ control points, kept above the minimum flight altitude, below the max altitude, with bounded turning angle, and far from terrain obstacles.

These are two genuinely conflicting objectives, framed as a **CMOP**. The authors solve it with a **constrained decomposition-based multi-objective evolutionary algorithm** that explicitly **uses infeasible individuals with good objective values** to inform the search before driving the population back to the feasible region.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: One computing UAV visits $I$ device hovering locations, serves each device, and then flies to a destination. A B-spline path is defined by $\lambda$ 3-D control points and sampled into path points around modeled terrain obstacles.

**Problem & objective**: Minimize the safe-path penalty $G_1(\mathbf x)=D_s=\sum_{j,k}(d_s/d_{j,k})^2$ and total UAV energy $G_2(\mathbf x)=\sum_{i=1}^{I}E_i$ subject to the offloading deadline and flight-safety constraints.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| B-spline control points | $\{(x_l,y_l,z_l)\}_{l=1}^{\lambda}$ | continuous 3-D | Control the UAV path |
| Device transmit power | $p_i^{tx}$ | continuous | Uplink power for device $i$ |
| UAV CPU allocation | $f_{\mathrm{UAV},i}$ | continuous | Computing resource for device $i$ |
| Segment speed | $v_i$ | continuous | UAV speed on segment $i$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Per-device deadline: $T_i-\tau_i^H-\tau_i^F\ge0$ |
| C2 | Minimum altitude: $h_2=\sum_j[d_j^{\min}]^- =0$ |
| C3 | Maximum altitude: $h_3=\sum_j[d_j^{\max}]^- =0$ |
| C4 | Turning-angle limit: $h_4=\sum_j[\Delta\theta_j]^-=0$ with $\theta\le\theta_{\max}$ |
| C5 | Decision domain: $\mathbf x\in\mathcal D$, with $3\lambda+3I$ components |

**Algorithm**: Decompose the CMOP with weight vectors, evolve mixed continuous individuals, and use dynamic infeasibility allocation to retain useful infeasible candidates early before progressively selecting lower-violation feasible Pareto solutions.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Peng et al. [x] formulate a constrained multi-objective UAV-MEC problem that couples energy-efficient offloading with safe 3-D path planning. The decision vector contains B-spline control points, device transmit powers, UAV CPU allocations, and segment speeds, while the objectives are obstacle-clearance penalty and total UAV energy. Feasibility requires task deadlines, minimum and maximum altitude, and bounded turning angles. Their decomposition-based evolutionary method dynamically retains informative infeasible individuals and achieves better feasible Pareto convergence and diversity than ToP and PPS in the reported experiments.

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

- Parse: `raw/sources/Constrained_Multi-Objective_Optimization_for_UAV-Enabled_Mobile_Edge_Computing_Offloading_Optimization_and_Path_Planning/full.md`
- Origin PDF: `raw/sources/Constrained_Multi-Objective_Optimization_for_UAV-Enabled_Mobile_Edge_Computing_Offloading_Optimization_and_Path_Planning/e2cbd4fd-01db-4ad4-a0b5-46084bd1f98c_origin.pdf`
- Figures: `raw/sources/Constrained_Multi-Objective_Optimization_for_UAV-Enabled_Mobile_Edge_Computing_Offloading_Optimization_and_Path_Planning/images/`
