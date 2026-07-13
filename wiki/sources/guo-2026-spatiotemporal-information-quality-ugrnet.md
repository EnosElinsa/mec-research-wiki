---
type: source
title: "Spatiotemporal Information Quality Optimization for UAV-Assisted Ground Robot Networks"
authors: ["Shun Guo", "Jiawen Kang", "Dusit Niyato", "Qingqing Zhang", "Weidang Lu", "Zhu Han"]
year: 2026
url: "https://doi.org/10.1109/TMC.2025.3646651"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC), vol. 25, no. 6, pp. 8002-8015"
tags: [source, uav-assisted-ground-robot-network, information-quality, delay-violation, martingale, wasserstein-distance, data-collection]
related:
  - "[[martingale-delay-violation-bound]]"
  - "[[spatiotemporal-information-quality]]"
  - "[[queueing-theory]]"
  - "[[stochastic-network-calculus]]"
  - "[[uav-mobile-relaying]]"
  - "[[uav-data-collection]]"
  - "[[post-disaster-mec]]"
  - "[[jiawen-kang]]"
  - "[[dusit-niyato]]"
  - "[[weidang-lu]]"
  - "[[zhu-han]]"
  - "[[li-2025-dt-uav-swarm-resource-management]]"
  - "[[zhang-2020-response-delay-uav-swarm]]"
  - "[[tang-2026-hg-maddpg-uav-rescue]]"
created: 2026-07-14
updated: 2026-07-14
---

# Spatiotemporal Information Quality Optimization for UAV-Assisted Ground Robot Networks

## Citation

Guo, S., Kang, J., Niyato, D., Zhang, Q., Lu, W., & Han, Z. (2026). *Spatiotemporal Information Quality Optimization for UAV-Assisted Ground Robot Networks*. **IEEE Transactions on Mobile Computing, 25**(6), 8002-8015. DOI: 10.1109/TMC.2025.3646651.

## TL;DR

Couples a martingale upper bound on heterogeneous multi-hop queueing-delay violations with Wasserstein distance from a required sensing distribution. Task completion improves spatial coverage but raises traffic load, producing an interior completion ratio in the paper's simulations.

## Problem

Emergency ground robots can collect more spatially complete information by scanning additional regions, but the resulting traffic increases queueing delay across robot, UAV, and command-center relays. Throughput alone does not express this tradeoff. The paper therefore models information quality as a cost with temporal and spatial components controlled by each robot's task-completion ratio.

## System model

- Ground robots sense local regions, multiple UAVs coordinate disjoint robot subsets and relay data, and one command center consumes the information.
- Traffic may traverse robot-to-robot, robot-to-UAV, and UAV-to-command-center links, forming heterogeneous tandem queues. A robot can relay through peers when it lacks direct UAV access.
- For information type `i`, robot `j` chooses completion ratio `gamma_{j,i}` in `[0,1]`. Its arrival rate scales with that ratio, sensing rate, and sensing-task count.
- Arrival and service are represented as finite-state steady-state Markov processes. Link service rates use Shannon-style bandwidth, power, fixed gain, noise, distance, and path-loss parameters.
- Each robot is assigned ten isolated regions in the simulation. Binary transition variables describe one-to-one regional scanning, while information-density coefficients shape the collected distribution.

## Method

For each queue, [[martingale-delay-violation-bound]] constructs exponential supermartingales for Markov arrivals and services. The heterogeneous end-to-end bound minimizes the sum of per-hop violation bounds over allocations of the total delay threshold. Its joint decay term harmonically combines the hop-specific decay rates instead of assuming homogeneous nodes or retaining only the smallest-capacity bottleneck.

The spatial term is a weighted first-order Wasserstein distance between the required information distribution and the distribution produced by the selected regions. Smaller distance means better spatial completeness. [[spatiotemporal-information-quality]] combines this distance with the temporal delay-violation bound as a weighted cost, then aggregates information types with a piecewise saturation rule.

The stated optimization minimizes aggregate quality cost over completion ratios and regional-assignment variables. However, the paper provides no algorithm, relaxation, pseudocode, complexity analysis, or convergence proof. Its numerical section sweeps completion ratios and identifies empirical minima rather than demonstrating a general solver or UAV path optimizer.

## Key findings

- Across 2-, 3-, and 5-hop routes, the martingale bound visually follows simulated delay box plots more closely than the bottleneck min-method and homogeneous MGF stochastic-network-calculus baseline. No scalar fit error is reported.
- At a delay threshold near 300 ms, Figure 2 approximately shows martingale bounds of `1.5e-3`, `2e-2`, and `1.5e-1` for 2, 3, and 5 hops. These are figure-read values.
- More robots sharing UAV bandwidth increases the delay-violation bound. At roughly 100 ms in Figure 3, the martingale curves are approximately `1e-3`, `1e-2`, and `1e-1` for 15, 20, and 25 robots.
- Spatial Wasserstein distance decreases as completion rises, while temporal delay cost eventually rises sharply. For five robots sending image data over two hops, the tested per-robot minima lie between completion ratios `0.6` and `0.8`.
- With 15 robots and 2-hop transmission, Figure 8 places the tested aggregate minima around `gamma=0.6` for 2, 5, and 10 information types. The plotted cost magnitudes are figure-derived and have no competing spatial/joint-optimization baseline.

## Limitations

The study is analytical and simulation-based, with no robots, UAV flights, measured queue traces, or real sensing distributions. Markov model order, MCMC fitting details, and goodness-of-fit are absent. Arrival and service are independent, hop services are independent, and stochastic propagation loss is omitted. Interference, fading distributions, scheduling overhead, retransmissions, packet loss, UAV energy and motion, robot travel time, obstacles, and overlapping coverage are not modeled.

The required and collected spatial distributions are assumed available, without estimation or sample-complexity analysis. Despite path-planning claims, the formulation contains no positions, distances, speed constraints, travel cost, or UAV trajectory variable. The quality quantity is mathematically minimized as a cost even though parts of the paper describe it as a positive contribution. The martingale propositions are upper bounds only under the stated stationarity, stability, independence, and loss assumptions; they are not worst-case guarantees for arbitrary traffic.

## Relation to the corpus

[[li-2025-dt-uav-swarm-resource-management]] also uses [[stochastic-network-calculus]] to pre-assess multi-hop delay, but embeds the bound in digital-twin resource scheduling. [[zhang-2020-response-delay-uav-swarm]] analyzes queueing-based swarm response delay with stochastic geometry and hardware validation. [[tang-2026-hg-maddpg-uav-rescue]] is the closest rescue architecture with UAVs and ground robots, but optimizes exploration, assignment, and offloading rather than Wasserstein spatial completeness and heterogeneous tandem-queue delay bounds.

## Raw artifacts

- Parse: `raw/sources/Spatiotemporal_Information_Quality_Optimization_for_UAV-Assisted_Ground_Robot_Networks/Spatiotemporal_Information_Quality_Optimization_for_UAV-Assisted_Ground_Robot_Networks.md`
- Origin PDF: `raw/sources/Spatiotemporal_Information_Quality_Optimization_for_UAV-Assisted_Ground_Robot_Networks/Spatiotemporal_Information_Quality_Optimization_for_UAV-Assisted_Ground_Robot_Networks.pdf`
- Figures: `raw/sources/Spatiotemporal_Information_Quality_Optimization_for_UAV-Assisted_Ground_Robot_Networks/images/`
