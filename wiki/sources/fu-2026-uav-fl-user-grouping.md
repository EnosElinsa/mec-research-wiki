---
type: source
title: "Energy-Efficient User Grouping-Based Federated Learning With UAV Assistance"
authors: ["Chien-Wei Fu", "Meng-Lin Ku", "Keshav Singh"]
year: 2026
url: "https://doi.org/10.1109/TGCN.2026.3676914"
venue: "IEEE Transactions on Green Communications and Networking (IEEE TGCN), vol. 10, pp. 2562-2578"
modeling_card: required
tags: [source, federated-learning, uav-assisted-learning, user-grouping, energy-efficiency, dbscan, successive-convex-approximation, trajectory-control]
related:
  - "[[federated-learning]]"
  - "[[uav-trajectory-control]]"
  - "[[rotary-wing-propulsion-energy-model]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[chen-2026-sdhfl-completion-time]]"
  - "[[huang-2026-aircomp-uav-swarms-afl]]"
  - "[[wang-2026-blockchain-lae-fl-mappo]]"
created: 2026-07-13
updated: 2026-07-16
---

# Energy-Efficient User Grouping-Based Federated Learning With UAV Assistance

## Citation

Fu, C.-W., Ku, M.-L., & Singh, K. (2026). *Energy-Efficient User Grouping-Based Federated Learning With UAV Assistance*. **IEEE Transactions on Green Communications and Networking**, 10, 2562-2578. DOI: 10.1109/TGCN.2026.3676914.

## TL;DR

Groups interfering FL clients with DBSCAN, derives how participation and data volume affect an expected-global-loss bound, and uses a two-phase SCA design to minimize UE and UAV energy over participation, local data, power, hover time, and trajectory.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A fixed-altitude UAV acts as the federated-learning server for multiple ground UEs over a finite slotted mission. UEs compute local updates while the UAV flies and transmit simultaneously over an interference-limited shared uplink while it hovers; the channel model is dominated by high-altitude LoS propagation, with an NLoS robustness study.

**Problem & objective**: Problem (P1) is a nonconvex joint design that minimizes total UE and UAV energy, $\min_{\mathbf q,\mathbf a,\mathbf p_{UE},\mathbf D,\mathbf t^{hov}} E^{tot}$, subject to communication feasibility and a target expected-global-loss gap.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV trajectory | $\mathbf q[n]$ | continuous 2D position | UAV horizontal location in slot $n$ |
| FL participation | $a_k[n]$ | binary, $\{0,1\}$ | Whether UE $k$ participates in slot $n$ |
| UE transmit power | $p_k[n]$ | continuous, bounded | Uplink model-transmission power |
| Local data volume | $D_k$ | continuous, bounded below | Data used by UE $k$ for local training |
| UAV hovering time | $t^{hov}[n]$ | continuous, nonnegative | Aggregation hover duration in slot $n$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| 2-3 | UAV initial and final positions are fixed |
| 6-8 | Flight, computation, communication, and hovering fit the slot timing limits |
| 10 | Each UE respects its maximum transmit power |
| 12 | Every participating UE uploads the model within the communication duration under the SINR-limited rate |
| 18 | The expected-global-loss gap is no greater than its target bound |
| 19-20 | Active UEs use at least the required data volume and participation remains feasible |

**Algorithm**: Use DBSCAN and the analytical SINR feasibility condition to form UE groups and initialize slots, hover points, power, and data; in Phase I relax participation through per-slot data and solve successive convex approximations; infer binary participation by thresholding; in Phase II restore one data amount per active UE and re-solve the SCA problem until the energy improvement is below $\epsilon$.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Fu et al. [x] studied energy-efficient user grouping for UAV-assisted federated learning under rate-limited simultaneous model uploads. They formulated a nonconvex total-energy minimization over UAV trajectory, UE participation, transmit power, local data volume, and hovering time while enforcing communication feasibility and a target expected-global-loss gap. Their UG-SCA method applies DBSCAN grouping and a feasibility initializer, then uses a two-phase successive convex approximation procedure to relax participation, recover binary participants, and re-optimize the continuous variables. Simulations show lower energy and faster convergence than the evaluated fixed, random, and reinforcement-learning baselines, while additional groups support larger model transmissions at the stated learning-performance tradeoff.

## Problem

Simultaneous client uploads can make a UAV-aggregated FL round infeasible when interference and a fixed upload window cannot support the model size. The design must restore communication feasibility while preserving learning quality and limiting UE computation/transmission plus UAV propulsion energy.

## System model

- One fixed-altitude UAV acts as the FL server for ground UEs over a finite mission divided into slots.
- UEs compute local updates while the UAV flies, upload simultaneously while it hovers, and then receive the aggregated model after fixed aggregation and broadcast phases.
- Shared-band uplinks interfere. The main model assumes high-altitude LoS free-space loss and fixed upload duration.
- The learning constraint is an upper bound on the expected global-loss gap under strong convexity, smoothness, bounded stochastic-gradient variance, and bounded update magnitude.
- Energy includes UE computation/transmission and UAV flight/hovering; UAV model-aggregation energy is omitted.

## Method

DBSCAN first forms user groups, and a closed-form feasibility initializer assigns slots, hover points, powers, and data. Phase I of UG-SCA relaxes binary participation into per-slot data variables and solves successive convex surrogates. Phase II thresholds participation, restores one data amount per active UE, and re-optimizes trajectory, power, hover time, and data volume with fixed participation.

## Key findings

- Equal client data volumes minimize the reported expected-global-loss bound; additional total data and participants reduce the bound with diminishing returns.
- At model size `8.065 Mb`, UG-SCA is comparable to full-participation Fixed-SCA. As model size increases, grouping lowers energy relative to the RL and RL-SCA baselines in the reported experiments.
- In the reported Fig. 9 setup, the no-grouping case is feasible only through `8.06535 Mb`; three groups have the lowest energy and are particularly suitable from `19.0034 Mb`. The reported grouped upper model-size case reaches about `39.9391 Mb`.
- Propulsion dominates total energy. More NLoS users and stronger non-IID quantity skew both increase the optimized energy demand.

## Limitations / parse caveats

The work is simulation/theory only and uses one fixed-altitude UAV, fixed protocol durations, shared-band synchronous uploads, and a theoretical loss bound rather than measured test accuracy. Strong-convexity assumptions limit direct transfer to modern non-convex deep models, and aggregation energy is omitted. The parse damages several aggregation, feasibility, EGL, and appendix equations; its maximum-power text, DBSCAN radius glyph, propulsion units, and some model-size labels are corrupted or ambiguous and are not promoted as exact values.

## Relation to the corpus

Unlike [[chen-2026-sdhfl-completion-time]], which uses D2D cluster consensus and asynchronous UAV aggregation, this source groups clients to satisfy simultaneous-uplink SINR feasibility and then optimizes data volume and propulsion. [[huang-2026-aircomp-uav-swarms-afl]] offers an AirComp/asynchronous alternative to the same communication bottleneck.

## Raw artifacts

- Parse: `raw/sources/Energy-Efficient_User_Grouping-Based_Federated_Learning_With_UAV_Assistance/Energy-Efficient_User_Grouping-Based_Federated_Learning_With_UAV_Assistance.md`
- Origin PDF: `raw/sources/Energy-Efficient_User_Grouping-Based_Federated_Learning_With_UAV_Assistance/Energy-Efficient_User_Grouping-Based_Federated_Learning_With_UAV_Assistance.pdf`
- Figures: `raw/sources/Energy-Efficient_User_Grouping-Based_Federated_Learning_With_UAV_Assistance/images/`
