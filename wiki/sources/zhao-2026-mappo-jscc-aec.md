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
created: 2026-07-07
updated: 2026-07-07
---

# Joint Optimization of Sensing, Communication, and Computing for Collaborative Multi-UAV Edge Computing System

## Citation

Zhao, H., Luan, M., Liyanage, M., & Chang, Z. (2026). *Joint Optimization of Sensing, Communication, and Computing for Collaborative Multi-UAV Edge Computing System*. **IEEE Transactions on Wireless Communications**, 25, 1272-1286. DOI: 10.1109/TWC.2025.3590253.

## TL;DR

Constructs a HAP-assisted multi-UAV aerial edge computing system where sensing devices generate data, UAVs collect and relay it, and the HAP provides upper-tier edge computing. The paper jointly optimizes sensing times, UAV trajectories, D2U/U2H transmit powers, offloading ratios, and communication resources. Lyapunov optimization turns the objective into task-completion minimization with energy-stability control, and MAPPO-JSCC embeds numerical sensing optimization, SCA, and Dinkelbach power solvers inside a PPO-based MADRL framework.

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

- `raw/sources/Joint Optimization of Sensing- Communication- and Computing for Collaborative Multi-UAV Edge Computing System/Joint Optimization of Sensing- Communication- and Computing for Collaborative Multi-UAV Edge Computing System.md`
- Original PDF and extracted figures (`images/`) in the same folder.
