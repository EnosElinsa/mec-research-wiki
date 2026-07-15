---
type: source
title: "Enhancing A2G Robustness in Energy-Constrained Multi-UAV Networks: MADRL for Trajectory Control and Resource Allocation"
authors: ["Jingyu Wang", "Xuming Fang", "Xianbin Wang", "Li Yan", "Junjie Wu", "Baolin Yin"]
year: 2026
url: "https://doi.org/10.1109/TWC.2026.3657894"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, multi-uav, air-to-ground, network-robustness, trajectory-control, resource-allocation, mappo, qmix, fairness]
related:
  - "[[chen-2026-traffic-aware-asynchronous-control]]"
  - "[[yin-2026-m2llm-trajectory-beamforming]]"
  - "[[air-to-ground-channel-model]]"
  - "[[gauss-markov-mobility-model]]"
  - "[[jains-fairness-index]]"
  - "[[uav-trajectory-control]]"
  - "[[uav-trajectory-safety-guarantee-ladder]]"
  - "[[rotary-wing-propulsion-energy-model]]"
  - "[[ma-pomdp]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[mappo]]"
  - "[[qmix]]"
  - "[[wang-2026-wutf-fair-communication]]"
  - "[[shi-2025-aoi-energy-replenishment-multiuav]]"
  - "[[li-2024-robust-bmappo-multiuav-mec]]"
  - "[[liu-2026-usp-nfrp-emergency-communication]]"
  - "[[zhou-2026-a2g-madrl-air-ground-vcs]]"
  - "[[parameter-sharing-marl]]"
  - "[[xianbin-wang]]"
created: 2026-07-13
updated: 2026-07-14
---

# Enhancing A2G Robustness in Energy-Constrained Multi-UAV Networks: MADRL for Trajectory Control and Resource Allocation

## Citation

Wang, J., Fang, X., Wang, X., Yan, L., Wu, J., & Yin, B. (2026). *Enhancing A2G Robustness in Energy-Constrained Multi-UAV Networks: MADRL for Trajectory Control and Resource Allocation*. **IEEE Transactions on Wireless Communications**, 25, 11286-11302. DOI: 10.1109/TWC.2026.3657894.

## TL;DR

Studies downlink service continuity when energy-limited UAV base stations stop operating at different times. A joint trajectory-control and resource-allocation framework gives each UAV separate trajectory and communication decision roles, shares parameters within each role, and implements the controller with either MAPPO or QMIX. The trained policies redirect surviving UAVs toward users left in coverage gaps while enforcing a terminal Jain-fairness requirement.

## Problem framing

Most multi-UAV coverage designs optimize service quality while all aircraft remain available. Here, a UAV stops communication when its residual energy falls below a threshold, so its users can suddenly lose service. Re-running an iterative optimizer after every dropout is poorly suited to real-time response. The paper instead asks whether a decentralized learned policy can use the remaining fleet to preserve throughput and fairness as the active set shrinks.

## System model

- Multiple fixed-altitude UAVs provide OFDMA downlink service to mobile ground users over a shared band, including inter-UAV interference.
- Ground-user motion follows a [[gauss-markov-mobility-model|Gauss-Markov model]], and the A2G link uses elevation-dependent LoS/NLoS path loss plus a two-lobe directional-antenna model.
- A UAV consumes communication and [[rotary-wing-propulsion-energy-model|propulsion energy]], stops service below a residual-energy threshold, and does not rejoin after returning to recharge.
- A user unserved for a configurable number of slots can send infrequent location and identity information through satellite short-message communication. Satellite signaling cost is not modeled.
- The objective maximizes cumulative throughput while requiring the final [[jains-fairness-index|Jain fairness index]] to meet a threshold.

## Method

The JTCRA framework models the task as a cooperative Dec-POMDP under [[centralized-training-decentralized-execution|CTDE]]. Each UAV has a trajectory role that selects discrete speed and heading and a communication role that selects power and bandwidth levels for associated users. User association is not learned independently: each in-range user attaches to the UAV with the strongest signal, and the selected radio levels are proportionally normalized into feasible allocations.

Parameters are shared among all trajectory roles and separately among all communication roles. The paper gives two implementations:

- **MAPPO-JTCRA:** on-policy [[mappo|MAPPO]] with generalized-advantage estimation, clipped actor/value objectives, death masks, invalid-action masks, and GRU memory.
- **QMIX-JTCRA:** off-policy [[qmix|QMIX]] with individual recurrent Q-networks, a monotonic mixing network, hypernetworks, replay, Double DQN, and target-network updates.

The shared reward combines average per-user slot throughput with a fairness-shortfall penalty whose weight increases as fleet energy is depleted.

## Key findings

- In the main three-UAV, 18-user simulation, only the proposed MAPPO-JTCRA both meets the 0.9 fairness threshold and attains the highest throughput among the reported baselines; the prose reports mean per-user cumulative throughput of 168.4 Mbit.
- Parameter sharing improves throughput over the corresponding separate-policy implementations. MAPPO-JTCRA is reported as more stable and higher-throughput than QMIX-JTCRA.
- Disabling satellite short-message requests reduces reported fairness to 0.7045, while long request tolerances also degrade fairness. This supports the short-message mechanism's role in exposing users outside current UAV coverage.
- As UAVs stop, the remaining fleet changes from partitioned coverage to sweeping and then wide spiral-like trajectories. These figures provide qualitative service-reassignment evidence, not a formal robustness guarantee.
- The proposed method maintains the tested fairness requirement when scaling from three UAVs and 18 users to five UAVs and 30 users, while widening its reported throughput lead over HAPPO-HSA.

## Limitations / future work

Validation is simulation-only and depends on modeled energy depletion, threshold stopping, known mobility/channel structure, and satellite user reports. Recharging UAVs never return to service; recharge-and-resume operation is future work. The high-level formulation lists association as an optimization variable, but the implemented environment derives it by strongest received signal. The parse is also inconsistent about the physical count of communication agents and contains damaged radio-allocation equations and table cells, so those formulas and ambiguous values are not reproduced here.

## Relation to the corpus

This is an A2G communication-control source rather than an MEC offloading design. It complements [[wang-2026-wutf-fair-communication]], which also couples energy-aware multi-UAV trajectories with fairness, and [[shi-2025-aoi-energy-replenishment-multiuav]], which uses QMIX under UAV energy dynamics. Its robustness mechanism differs from uncertainty-aware [[li-2024-robust-bmappo-multiuav-mec]]: here robustness means service reconfiguration after modeled UAV dropout. It also contrasts with [[liu-2026-usp-nfrp-emergency-communication]], where replacement UAVs sustain service instead of permanently shrinking the active fleet.

## Comparison boundary

The protected object here is service continuity and fairness after energy depletion, not geometric collision safety or uncertainty-set robustness. The distinction is explicit in [[uav-trajectory-safety-guarantee-ladder]].

## Raw artifacts

- Parse: `raw/sources/Enhancing_A2G_Robustness_in_Energy-Constrained_Multi-UAV_Networks_MADRL_for_Trajectory_Control_and_Resource_Allocation/Enhancing_A2G_Robustness_in_Energy-Constrained_Multi-UAV_Networks_MADRL_for_Trajectory_Control_and_Resource_Allocation.md`
- Origin PDF: `raw/sources/Enhancing_A2G_Robustness_in_Energy-Constrained_Multi-UAV_Networks_MADRL_for_Trajectory_Control_and_Resource_Allocation/Enhancing_A2G_Robustness_in_Energy-Constrained_Multi-UAV_Networks_MADRL_for_Trajectory_Control_and_Resource_Allocation.pdf`
- Figures: `raw/sources/Enhancing_A2G_Robustness_in_Energy-Constrained_Multi-UAV_Networks_MADRL_for_Trajectory_Control_and_Resource_Allocation/images/`
