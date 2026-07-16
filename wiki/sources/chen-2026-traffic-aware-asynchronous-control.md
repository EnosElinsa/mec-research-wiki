---
type: source
title: "Traffic-Aware Asynchronous Trajectory Planning and Scheduling in UAV-Assisted Wireless Networks With Heterogeneous Traffic Demands"
authors: ["Che Chen", "Bo Gu", "Bin Lyu", "Shimin Gong", "Zhi Liu", "Yuming Fang"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3656507"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC), vol. 25, no. 7, pp. 9816-9832"
tags: [source, multi-uav, traffic-clustering, asynchronous-control, noma, uav-relaying, graph-neural-network, ppo]
related:
  - "[[spatial-temporal-graph-attention-traffic-clustering]]"
  - "[[traffic-aware-asynchronous-uav-control]]"
  - "[[noma]]"
  - "[[ppo]]"
  - "[[graph-neural-network]]"
  - "[[uav-trajectory-control]]"
  - "[[wang-2026-robust-multiuav-jtcra]]"
  - "[[mobility-asynchrony-and-geometry-in-aerial-coverage]]"
created: 2026-07-14
updated: 2026-07-16
modeling_card: required
---

# Traffic-Aware Asynchronous Trajectory Planning and Scheduling in UAV-Assisted Wireless Networks With Heterogeneous Traffic Demands

## Citation

Chen, C., Gu, B., Lyu, B., Gong, S., Liu, Z., & Fang, Y. (2026). *Traffic-Aware Asynchronous Trajectory Planning and Scheduling in UAV-Assisted Wireless Networks With Heterogeneous Traffic Demands*. **IEEE Transactions on Mobile Computing, 25**(7), 9816-9832. DOI: 10.1109/TMC.2026.3656507.

## TL;DR

Clusters source devices from spatial position and directional traffic patterns, then uses a GNN/GRU-enhanced PPO controller to coordinate multiple UAVs' trajectories, NOMA access, inter-UAV relaying, and asynchronous time division among flight, collection, relay, and delivery modes.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: In a post-disaster M2M network without direct device-to-device links, multiple fixed-altitude UAVs collect directional sensing flows from source user devices and deliver them to target devices. Each UAV asynchronously divides a slot into flight, NOMA uplink sensing, UAV-to-UAV relaying, and NOMA downlink transmission while managing interference and data buffers.

**Problem & objective**: Problem (13) is a mixed-integer max-min throughput problem, $\max_{\ell,\tau,\Phi}\min_{k\in\mathcal K}\frac{1}{T}\sum_{t=0}^{T-1}\mathbb E[\Re^k(t)]$, subject to the time-allocation, mobility, access, SINR, and queue relations in (1)-(12).

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV trajectory | $\ell_i(t)$ | Continuous 3D position at fixed altitude | Sets UAV $i$'s position and implicit speed |
| Asynchronous mode times | $\tau_{i,f}(t),\tau_{i,s}(t),\tau_{i,r}(t),\tau_{i,d}(t)$ | Continuous, nonnegative | Allocates flight, sensing, relay, and downlink time |
| Device access and network formation | $\Phi=\{\phi_{m,i}^{k}(t)\}$ | Binary selections | Schedules source and target devices and relay links |
| Cluster and peer choices | $c_i(t),\{\phi_{i,j}(t)\}$ | Discrete | Selects a traffic cluster and at most one relay peer |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Slot budget: $\tau_{i,f}+\tau_{i,s}+\tau_{i,r}+\tau_{i,d}\leq\delta$ |
| C2 | Collision avoidance: $\lVert\ell_i(t)-\ell_j(t)\rVert\geq d_{\min}$ |
| C3 | Mobility: $\lVert\ell_i(t+1)-\ell_i(t)\rVert\leq v_{\max}\tau_{i,f}$ |
| C4 | Single association or relay: $\sum_i\phi_{m,i}^{k}(t)\leq1$ and $\sum_{j\neq i}\phi_{i,j}(t)\leq1$ |
| C5 | Uplink, relay, and downlink decoding satisfy $\gamma_{m,i}^{\tau}\geq\gamma_{\mathrm{th}}$, $\gamma_{i,j}^{\tau}\geq\gamma_{\mathrm{th}}$, and the corresponding downlink SINR threshold |

**Algorithm**: Use STGAN to cluster devices from geographic and directional-flow features, build a dynamic UAV-cluster graph, fuse GCN features and GRU temporal state with the raw observation, and train a PPO actor with hybrid discrete scheduling and continuous trajectory/time heads using a soft-min throughput reward plus trajectory-flow similarity and collision penalties.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Chen et al. [x] studied max-min traffic-flow throughput in a post-disaster UAV-assisted M2M network with heterogeneous directional demands and no direct ground links. They jointly controlled UAV trajectories, asynchronous flight and transmission times, NOMA device scheduling, and UAV-to-UAV relay formation under mobility, collision, decoding, and buffer constraints. Their Cluster-AC pipeline first used STGAN for spatial-temporal traffic clustering and then applied a dynamic-graph and GRU enhanced PPO controller. Simulations reported convergence for the clustered controllers while both non-clustered variants failed to converge, and Cluster-AC achieved the highest cumulative throughput among the compared schemes with relay use varying between 25% and 50% of slots over a reported 30-slot horizon.

## System model

- Multiple fixed-altitude UAVs relay heterogeneous directional M2M flows from source devices to target devices when direct ground links are unavailable.
- Historical outgoing traffic is represented as angular-sector histograms. Devices are clustered before control to reduce scheduling granularity.
- Each UAV independently divides a slot into flight, uplink collection, UAV-to-UAV relay, and downlink delivery mini-slots.
- NOMA/SIC, inter-UAV and cross-mode interference, source/UAV buffers, collision separation, and flow conservation are modeled.
- The objective is max-min delivered throughput across traffic flows, jointly over trajectories, mode times, access schedules, and relay topology.

## Method

[[spatial-temporal-graph-attention-traffic-clustering]] combines directional-flow similarity with spatial compactness. A dynamic graph then represents UAV-UAV and UAV-cluster channel/topology relationships. Graph features, a GRU temporal state, and PPO form the centralized controller described by [[traffic-aware-asynchronous-uav-control]].

The pipeline has no global-optimality, approximation-ratio, convergence, or throughput guarantee. Training curves demonstrate empirical convergence only in the evaluated simulation.

## Findings

- Clustered asynchronous control and clustered synchronous control converge in the reported training, while both non-cluster variants are reported not to converge; the asynchronous design attains the higher reward.
- GNN/GRU-enhanced PPO exceeds conventional PPO and a static-GNN comparator in plotted reward.
- Experiments use real IP-flow records for traffic patterns but assign physical device coordinates synthetically. Clusters qualitatively reflect proximity and flow direction, with no NMI, ARI, confidence interval, or statistical test.
- The proposed controller is highest-throughput across the plotted density/distance sweeps. Its UAV-to-UAV mode is used in 25%-50% of slots over one reported 30-slot horizon.

## Limitations

Validation is simulation-only, with no flight trial, radio prototype, measured channel, repeated-seed statistic, or runtime/energy measurement. Device mobility is omitted, UAVs are homogeneous, historical traffic is assumed predictive, and centralized state availability plus modeled NOMA/SIC are taken for granted. A baseline-ordering discussion around one distance sweep is internally inconsistent, so no crossover claim is preserved. Equation OCR is severe, and traffic "radiation pattern" denotes a directional histogram rather than an antenna pattern.

## Relation to the corpus

The paper complements learned multi-UAV resource control in [[wang-2026-robust-multiuav-jtcra]] with traffic clustering, asynchronous operation modes, and inter-UAV data handoff rather than energy-depletion robustness.

## Raw artifacts

- Parse: `raw/sources/Traffic-Aware_Asynchronous_Trajectory_Planning_and_Scheduling_in_UAV-Assisted_Wireless_Networks_With_Heterogeneous_Traffic_Demands/Traffic-Aware_Asynchronous_Trajectory_Planning_and_Scheduling_in_UAV-Assisted_Wireless_Networks_With_Heterogeneous_Traffic_Demands.md`
- Original PDF and extracted figures are in the same folder.
