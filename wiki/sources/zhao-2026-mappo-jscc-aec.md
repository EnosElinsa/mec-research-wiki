---
type: source
title: "Joint Optimization of Sensing, Communication, and Computing for Collaborative Multi-UAV Edge Computing System"
authors: ["Hui Zhao", "Mingan Luan", "Madhusanka Liyanage", "Zheng Chang"]
year: 2026
url: "https://doi.org/10.1109/TWC.2025.3590253"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, integrated-sensing-computation-communication, high-altitude-platform-station, multi-uav-assisted-mec, lyapunov-optimization, mappo, noma, fractional-programming-dinkelbach]
related:
  - "[[integrated-sensing-computation-communication]]"
  - "[[high-altitude-platform-station]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[lyapunov-optimization]]"
  - "[[mappo]]"
  - "[[noma]]"
  - "[[fractional-programming-dinkelbach]]"
  - "[[ctde-multi-agent-drl-protocol]]"
  - "[[tang-2024-iscc-uav-feel]]"
  - "[[zheng-chang]]"
modeling_card: required
created: 2026-07-07
updated: 2026-07-16
---

# Joint Optimization of Sensing, Communication, and Computing for Collaborative Multi-UAV Edge Computing System

## Citation

Zhao, H., Luan, M., Liyanage, M., & Chang, Z. (2026). *Joint Optimization of Sensing, Communication, and Computing for Collaborative Multi-UAV Edge Computing System*. **IEEE Transactions on Wireless Communications**, 25, 1272-1286. DOI: 10.1109/TWC.2025.3590253.

## TL;DR

Constructs a HAP-assisted multi-UAV aerial edge computing system where sensing devices generate data, UAVs collect and relay it, and the HAP provides upper-tier edge computing. The paper jointly optimizes sensing times, UAV trajectories, D2U/U2H transmit powers, offloading ratios, and communication resources. Lyapunov optimization turns the objective into task-completion minimization with energy-stability control, and MAPPO-JSCC embeds numerical sensing optimization, SCA, and Dinkelbach power solvers inside a PPO-based MADRL framework.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Sensing devices are clustered under multiple UAVs, which sense and process data locally or offload it to a stationary HAP edge server. Device-to-UAV access uses NOMA over probabilistic LoS/NLoS air-to-ground channels, while UAV-to-HAP access uses OMA subcarriers over a LoS channel.

**Problem & objective**: P1, an NP-hard MINLP obtained from Lyapunov drift-plus-penalty transformation, minimizes $Z_2[t]+\kappa Z_3[t]$, where $Z_3[t]=\sum_{u\in\mathcal U}\tau_{u,k,h}[t]$, to reduce average task-completion time while stabilizing long-term energy consumption.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Number of sensing repetitions | $\omega_k[t]$ | Nonnegative integer | Repeated sensing attempts for device cluster $k$ |
| UAV position / trajectory | $l_u[t]$ | Discrete feasible flight positions | Position of UAV $u$ in slot $t$ |
| D2U and U2H powers | $\mathbf p_{sd}[t],\mathbf p_u[t]$ | Continuous, bounded nonnegative | Sensing-device and UAV uplink transmit powers |
| Offloading ratio | $z_{u,k}[t]$ | Continuous, $[0,1]$ | Fraction of cluster $k$'s task processed by UAV $u$ rather than the HAP |
| U2H subcarrier assignment | $y_{u,s}[t]$ | Binary, $\{0,1\}$ | Assign OMA subcarrier $s$ to UAV $u$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Consecutive UAV positions obey the maximum flight-distance limit |
| C2-C3 | Device and UAV powers satisfy $p_{u,k,i}[t]\le p_i^{\max}$ and $p_u[t]\le p_u^{\max}$ |
| C4 | Offloading is fractional: $0\le z_{u,k}[t]\le1$ |
| C5-C6 | Device and UAV energy use does not exceed $E_{SD}$ and $E_u^{\max}$ |
| C7 | Sensing probability/satisfaction hold, each subcarrier serves at most one UAV, and assignment and mobility constraints (5), (6), (27), (28), and (30) hold |

**Algorithm**: Lyapunov transformation $\rightarrow$ numerical optimization of sensing repetitions $\rightarrow$ SCA for D2U NOMA power $\rightarrow$ Dinkelbach optimization for U2H OMA power $\rightarrow$ CTDE MAPPO for trajectories, offloading ratios, and subcarrier assignments.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zhao et al. [x] studied joint sensing, communication, and computing optimization in a HAP-assisted multi-UAV aerial edge computing network. They jointly optimized sensing times, UAV trajectories, device-to-UAV and UAV-to-HAP transmit powers, offloading ratios, and communication resources to minimize average task-completion time while maintaining energy-consumption stability. Lyapunov optimization transformed the long-term objective into per-slot drift-plus-penalty problems. The resulting MAPPO-JSCC framework embeds numerical sensing optimization, successive convex approximation for NOMA power, and a Dinkelbach solver for OMA power into PPO-based multi-agent learning. Simulations report faster and more stable convergence than SAPPO, shorter completion time than SAPPO, TD3-FNM, and AAS, and 26% lower energy consumption while retaining 83% of the minimum-completion-time benchmark at $\kappa=10$.

## Problem framing

Large IoT sensing deployments need low-latency processing, but sensing devices are power-limited and UAVs must balance sensing-data collection, communication, computing, and energy. Optimizing only communication or only computing misses the interaction between repeated sensing, hybrid access, offloading, and UAV motion. The paper frames this as [[integrated-sensing-computation-communication|ISCC/JSCC]] over an aerial edge system with both UAV and HAP compute.

## System model

- One stationary HAP and multiple UAVs serve sensing devices distributed over a 1000 m x 1000 m area in the simulation.
- Sensing devices are grouped into clusters and may repeat sensing to satisfy probabilistic sensing-success and satisfaction thresholds.
- Device-to-UAV uplink uses NOMA; UAV-to-HAP uplink uses OMA/OFDMA subcarriers.
- Sensing data are bit-wise partitionable; UAVs and HAP collaboratively process the tasks.
- The main objective minimizes average task completion time while keeping energy consumption stable through Lyapunov control.

## Method

- **Sensing optimization.** The optimal number of sensing times is derived through numerical analysis under sensing-success constraints.
- **Transmission power.** D2U NOMA power is handled with SCA; U2H OMA power is handled with a Dinkelbach fractional-programming step.
- **MAPPO-JSCC.** Multi-UAV trajectories, offloading, and communication resource allocation are solved with a PPO-based multi-agent DRL design using centralized training and decentralized execution.
- **Embedded solvers.** The numerical/SCA/Dinkelbach subproblem outputs are embedded into the MADRL loop to reduce training difficulty and improve convergence.

## Key findings

- MAPPO-JSCC shows higher reward, lower fluctuation, and faster convergence than the single-agent PPO baseline in the reported experiments.
- Raising the latency-weight parameter kappa lowers average task-completion time and raises uplink rates, but increases average system energy consumption.
- The proposed scheme achieves shorter task-completion time than SAPPO, TD3-FNM, and AAS under the tested kappa values.
- At kappa = 10, the proposed scheme reports 26% lower energy consumption while maintaining 83% of the minimum completion-time benchmark.
- The authors attribute the gains to jointly optimizing node selection, NOMA power, offloading strategies, subcarrier allocation, and UAV transmit power rather than optimizing one layer alone.

## Limitations / future work

The paper is simulation-based. It uses fixed HAP altitude, fixed UAV altitude/speed settings, modeled sensing probabilities, and synthetic device distributions. The conclusion does not list a specific future-work item beyond the demonstrated simulation comparisons.

## Relation to the corpus

This is a HAP-assisted [[integrated-sensing-computation-communication]] source rather than an ISAC-only beamforming paper. It complements [[tang-2024-iscc-uav-feel]], which couples UAV deployment and federated-edge-learning data quality, and [[wen-2024-iscc-edge-ai]], which optimizes task-oriented edge-AI inference quality. Methodologically, it also extends the [[ctde-multi-agent-drl-protocol]] and [[mappo]] vocabulary into a hybrid solver where Lyapunov and convex subproblem solutions are embedded inside MADRL.

## Raw artifacts

- `raw/sources/Joint_Optimization_of_Sensing_Communication_and_Computing_for_Collaborative_Multi-UAV_Edge_Computing_System/Joint_Optimization_of_Sensing_Communication_and_Computing_for_Collaborative_Multi-UAV_Edge_Computing_System.md`
- Original PDF and extracted figures (`images/`) in the same folder.
