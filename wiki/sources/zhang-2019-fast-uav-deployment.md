---
type: source
title: "Fast Deployment of UAV Networks for Optimal Wireless Coverage"
authors: ["Xiao Zhang", "Lingjie Duan"]
year: 2019
url: "https://doi.org/10.1109/TMC.2018.2840143"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, uav-deployment, wireless-coverage, heterogeneous-uav, min-max-delay, min-sum-delay, approximation-algorithm]
related:
  - "[[fast-heterogeneous-uav-deployment]]"
  - "[[heterogeneous-uav-fleet]]"
  - "[[drone-cell-3d-placement]]"
  - "[[geometric-disk-cover]]"
  - "[[fairness-metrics-in-mec]]"
  - "[[uav-trajectory-control]]"
created: 2026-07-13
updated: 2026-07-16
modeling_card: required
---

# Fast Deployment of UAV Networks for Optimal Wireless Coverage

## Citation

Zhang, X., & Duan, L. (2019). *Fast Deployment of UAV Networks for Optimal Wireless Coverage*. **IEEE Transactions on Mobile Computing**, 18(3), 588-601. DOI: 10.1109/TMC.2018.2840143.

## TL;DR

Optimizes where heterogeneous UAV base stations should finish deployment so their coverage regions span a target area quickly. Min-max travel time represents worst-location service fairness; min-sum travel time represents average deployment efficiency. The paper derives exact, approximation, and pseudo-polynomial algorithms for same-origin and order-preserving deployments.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A centralized controller dispatches heterogeneous UAV base stations from given ground locations to fixed operating altitudes so their coverage disks fully cover a thin rectangular target area, reduced to a line interval for the main analysis. UAVs use orthogonal channels, inter-UAV interference is ignored, and air-to-ground links follow free-space line-of-sight path loss with an SNR coverage threshold.

**Problem & objective**: The paper studies NP-complete min-max and min-sum placement problems, $\min_{\{y_i\}}\max_i T_i(y_i)$ and $\min_{\{y_i\}}\sum_iT_i(y_i)$, where $T_i(y_i)=\sqrt{(y_i-x_i)^2+h_i^2}/v_i$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Final horizontal position | $y_i$ | continuous | Deployment location of UAV $i$ along the target interval |
| Deployment ordering | $\{y_i\}_{i=1}^{n}$ | combinatorial ordered placement | Selects and orders heterogeneous UAV placements that jointly cover the interval |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| Full coverage | $[0,\beta]\subseteq\bigcup_i[y_i-r_i,y_i+r_i]$ in the line model |
| Feasibility | Available coverage satisfies $2\sum_i\sqrt{r_i^2-(d/2)^2}\geq\beta$ and $r_i\geq d/2$ |
| Order preservation | For distinct launch points, $y_i\leq y_{i+1}$ when $x_i\leq x_{i+1}$ |
| Travel time | Each assigned location incurs $T_i(y_i)=\sqrt{(y_i-x_i)^2+h_i^2}/v_i$ |

**Algorithm**: For a shared launch point, greedily assign the UAV with minimum travel time to the farthest uncovered point for the exact min-max solution; for distinct launch points, preserve location order, run a deadline-feasibility scan, and binary-search an FPTAS solution. For min-sum deployment, use a linear-time approximation at a shared launch point and a pseudo-polynomial dynamic program for the ordered general case.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zhang and Duan [x] studied fast deployment of heterogeneous UAV networks for complete wireless coverage of a target area. They formulated a min-max problem that minimizes the largest UAV deployment delay and a min-sum problem that minimizes total deployment delay, and proved both problems NP-complete in general. For UAVs dispatched from the same location, they developed an optimal low-complexity algorithm for the min-max problem and a linear-time approximation for the min-sum problem. For distinct initial locations, they imposed location-order preservation, designed an FPTAS for min-max deployment, and constructed a pseudo-polynomial dynamic program for min-sum deployment. Simulations report that the FPTAS approaches the brute-force optimum and that greater UAV speed, coverage radius, and deployment diversity reduce the resulting delay.

## Problem framing

Wireless-coverage work often optimizes altitude or service after deployment, while fast sensor-deployment methods do not capture UAV differences in speed, altitude, and coverage radius. Disaster and battlefield service need small worst-case delay; crowd coverage cares more about average waiting time, and the two objectives can conflict.

## System model

- `n` UAVs move from initial stations to hovering points that cover a thin rectangular target area, reduced to a line interval for the core theory.
- UAVs differ in initial position, constant flight speed, operating altitude, and ground coverage radius.
- LoS-dominated free-space propagation and orthogonal channels make coverage interference-free.
- Full coverage requires enough aggregate radius and `r_i >= d/2`; the decision variables are final horizontal positions.
- Different-origin tractable formulations preserve initial ordering at final positions to avoid crossing paths.

## Method

The general min-max and min-sum problems are proved NP-complete. For same-origin min-max deployment, Algorithm 1 greedily chooses the UAV that can cover the current frontier fastest and is optimal in `O(n^2)`. For different origins, an `O(n^2)` deadline-feasibility scan plus binary search gives a `(1+epsilon)` FPTAS in `O(n^2 log(1/epsilon))` under order preservation.

For same-origin min-sum deployment, the largest-radius-first greedy rule is linear-time, exact when speed and altitude are identical, and bounded by altitude ratio `kappa` times speed ratio `tau`. The order-preserving general case uses an optimal pseudo-polynomial dynamic program with `O(n Gamma_u^2)` complexity. A grid-based 2-D uniform-radius extension gives a stated `O(n^3 log(1/epsilon))` FPTAS.

## Key findings

- The FPTAS is evaluated at errors from `1%` to `0.01%`; tighter error increases runtime and remains close to brute force in the reported tests.
- Simulations average 1,000 runs and use a 20 km target interval, 50 km/h maximum speed, and 3 km maximum radius unless otherwise stated.
- The dynamic program yields lower total delay, while the min-max FPTAS yields lower maximum delay, exposing the intended fairness-efficiency tradeoff.
- The heterogeneous-radius 2-D approximation becomes less accurate as radius variance increases because every radius is conservatively replaced by the fleet minimum.

## Limitations / future work

The core geometry is one-dimensional and order preservation changes the unrestricted problem. Interference is omitted through orthogonal channels, propagation is LoS/free-space, and evaluation is simulation-only. The same-origin min-sum bound worsens with fleet heterogeneity; the exact min-sum method is pseudo-polynomial. The paper omits the full 2-D min-sum development and leaves interference-aware deployment for future work.

## Relation to the corpus

[[fast-heterogeneous-uav-deployment]] differs from [[drone-cell-3d-placement]] and [[geometric-disk-cover]] by taking the fleet and coverage requirement as inputs and minimizing travel-to-service delay. It also gives [[heterogeneous-uav-fleet]] a non-MEC case where speed, altitude, and coverage-radius differences directly determine algorithmic guarantees.

## Raw artifacts

- Parse: `raw/sources/Fast_Deployment_of_UAV_Networks_for_Optimal_Wireless_Coverage/Fast_Deployment_of_UAV_Networks_for_Optimal_Wireless_Coverage.md`
- Origin PDF: `raw/sources/Fast_Deployment_of_UAV_Networks_for_Optimal_Wireless_Coverage/Fast_Deployment_of_UAV_Networks_for_Optimal_Wireless_Coverage.pdf`
- Figures: `raw/sources/Fast_Deployment_of_UAV_Networks_for_Optimal_Wireless_Coverage/images/`
