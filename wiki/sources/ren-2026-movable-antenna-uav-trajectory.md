---
type: source
modeling_card: required
title: "Movable Antenna Enhanced Cellular-Connected UAV Communication With Trajectory Planning"
authors: ["Tianshi Ren", "Xianchao Zhang", "Wenyan Ma", "Lipeng Zhu", "Xiaozheng Gao", "Rui Zhang"]
year: 2026
url: "https://doi.org/10.1109/TWC.2026.3687538"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), vol. 25, pp. 16351-16368"
tags: [source, movable-antenna, cellular-connected-uav, trajectory-planning, beamforming, graph-search]
related:
  - "[[movable-antenna]]"
  - "[[cellular-connected-uav]]"
  - "[[uav-trajectory-control]]"
  - "[[air-to-ground-channel-model]]"
  - "[[selective-uniform-cost-search]]"
created: 2026-07-13
updated: 2026-07-16
---

# Movable Antenna Enhanced Cellular-Connected UAV Communication With Trajectory Planning

## Citation

Ren, T., Zhang, X., Ma, W., Zhu, L., Gao, X., & Zhang, R. (2026). *Movable Antenna Enhanced Cellular-Connected UAV Communication With Trajectory Planning*. **IEEE Transactions on Wireless Communications, 25**, 16351-16368. DOI: 10.1109/TWC.2026.3687538.

## TL;DR

Minimizes a cellular-connected UAV's mission time by jointly planning its path, serving-BS association, MMSE receive beamforming, and onboard movable-antenna positions under a lower-bound expected-SINR condition and mechanical movement constraints.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: One fixed-altitude cellular-connected UAV flies between prescribed endpoints while ground base stations share spectrum and one serving BS is selected per location. The UAV carries a two-dimensional movable receive array with MMSE combining; a Jensen lower bound on expected SINR provides the communication-feasibility condition, and the flight region is discretized into a square grid.

**Problem & objective**: A mixed discrete-continuous path-planning problem minimizes mission time, $\min T_{\mathrm{mission}}$, while requiring the lower-bound expected SINR to exceed its threshold.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Grid path | $\mathcal G$ | discrete node sequence | UAV route between prescribed endpoints |
| Serving-BS association | $a_b(n)$ | binary | BS selected at grid node $n$ |
| Receive beamformer | $\mathbf w(n)$ | complex continuous vector | MMSE combiner at grid node $n$ |
| Movable antenna positions | $\mathbf r(n)$ | continuous 2-D positions | Element locations of the UAV receive array |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | The Jensen lower bound on expected SINR satisfies $\underline{\gamma}(n)\ge\gamma_{\min}$ |
| C2 | Each grid edge has its prescribed flight time and the route connects the endpoints |
| C3 | Every antenna element stays inside the movable-array region |
| C4 | Element displacement and pairwise spacing satisfy mechanical speed and separation limits |
| C5 | One feasible serving BS is selected at each visited node |

**Algorithm**: Discretize the flight region into a grid → propagate antenna positions and compute MMSE combining at each node → improve movable-antenna positions by successive linearization and feasible-direction line search → expand the lowest-bound-time node with selective uniform-cost search → prune histories using the remaining-time lower bound.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Ren et al. [x] studied mission-time minimization for a cellular-connected UAV equipped with a movable receive antenna array. They jointly planned the UAV path, serving-base-station association, MMSE receive beamforming, and antenna-element positions under an expected-SINR lower bound and mechanical movement constraints. The antenna solver uses successive linearization and feasible-direction line search, while selective uniform-cost search expands grid nodes with a remaining-time lower bound and prunes candidate histories. The antenna-position iterations converge to a first-order stationary point under the stated procedure. At a 13 dB SINR threshold, simulations report mission-time reductions of 6.46%, 18.55%, and 28.35% relative to the evaluated movable-antenna MRC, single-antenna MMSE, and fixed-array MMSE schemes.

## Problem and system model

One fixed-altitude UAV flies between prescribed endpoints while ground BSs share spectrum. One BS serves the UAV and the others interfere. The UAV carries a two-dimensional movable receive array whose elements obey region, speed, and spacing limits. Slowly varying channel/loading information is assumed known for offline planning, and a tractable Jensen lower bound on expected SINR supplies the communication-feasibility condition.

## Method

The flight region becomes a square grid with horizontal and diagonal edges flown at maximum speed. At each candidate node, the algorithm carries forward the previous antenna-position vector, computes MMSE combining, retains the serving BS when feasible or selects the best-SINR BS, and improves antenna positions by successive linearization with feasible-direction line search. [[selective-uniform-cost-search]] expands the lowest accumulated-plus-lower-bound-time node and prunes its candidate history.

The antenna solver converges to a first-order stationary point. The graph-search optimality statement is conditional on a valid remaining-time lower bound; practical pruning, discretization, and local antenna solutions do not establish a global solution to the original continuous problem.

## Key findings

- The antenna-position solver converges within ten iterations in the displayed experiment.
- At a 13 dB SINR threshold, MA-MMSE reduces mission time by 6.46%, 18.55%, and 28.35% relative to MA-MRC, single-antenna MMSE, and fixed-position-array MMSE.
- The proposed scheme remains feasible at SINR thresholds 8, 10, 14, and 22 dB above the four reported comparison methods, respectively.

## Limitations

Results are simulations. The model assumes fixed altitude, LoS free-space links, equivalent single-antenna BSs, and known slowly varying interference loading. Grid granularity and pruning trade quality for complexity; a 20 m grid misses a feasible path at 29 dB in one test. Mechanical settling, fast channel changes, and flight validation are not evaluated.

## Relation to the corpus

This paper adds local [[movable-antenna]] control to the interference-limited aerial-user problem in [[cellular-connected-uav]]. Unlike rate-maximizing trajectory designs, it uses communication feasibility to minimize endpoint-to-endpoint mission time.

## Raw artifacts

- `raw/sources/Movable_Antenna_Enhanced_Cellular-Connected_UAV_Communication_With_Trajectory_Planning/Movable_Antenna_Enhanced_Cellular-Connected_UAV_Communication_With_Trajectory_Planning.md`
- Original PDF and extracted figures (`images/`) are in the same folder.
