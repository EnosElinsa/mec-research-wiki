---
type: source
title: "Joint Optimization of Latency and Energy Consumption for Computing Task Offloading Based on Cooperative Multi-UAV and HAP Networks"
authors: ["Meng Li", "Haoyu Wan", "Suyu Lv", "Pengbo Si", "Haijun Zhang", "F. Richard Yu"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3683404"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, hierarchical-aerial-mec, high-altitude-platform-station, task-offloading, ddqn, ppo, mixed-integer-nonlinear-programming, energy-latency-tradeoff]
related:
  - "[[hierarchical-aerial-mec]]"
  - "[[high-altitude-platform-station]]"
  - "[[ddqn]]"
  - "[[ppo]]"
  - "[[hybrid-action-decision-making]]"
  - "[[mixed-integer-nonlinear-programming]]"
  - "[[energy-latency-tradeoff]]"
  - "[[nabi-2025-jour-hierarchical-aerial]]"
  - "[[chen-2026-dart-hap-uav-mec]]"
created: 2026-07-07
updated: 2026-07-07
---

# Joint Optimization of Latency and Energy Consumption for Computing Task Offloading Based on Cooperative Multi-UAV and HAP Networks

## Citation

Li, M., Wan, H., Lv, S., Si, P., Zhang, H., & Yu, F. R. (2026). *Joint Optimization of Latency and Energy Consumption for Computing Task Offloading Based on Cooperative Multi-UAV and HAP Networks*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2026.3683404.

## TL;DR

Builds a [[hierarchical-aerial-mec]] offloading model with terrestrial UEs, multiple UAVs, and one [[high-altitude-platform-station|HAP]]. Each task can be processed by a single UAV, split across multiple UAVs, or sent through UAVs to the HAP. The objective is a weighted system consumption combining processing latency and energy. The method is a two-stage DRL controller: [[ddqn]] chooses the offloading mode, and [[ppo]] sets task-splitting ratios when cooperative multi-UAV processing is selected.

## Problem framing

Sparse or weak terrestrial infrastructure makes ground-only MEC insufficient, while UAV-only MEC is energy- and compute-limited. HAPs add broader coverage and stronger compute, but direct device-to-HAP links are challenging and the resulting task-mode choice is mixed discrete-continuous. The paper formulates the problem as an MINLP and recasts it as an MDP to avoid solving the full coupled optimization directly.

## System model

- The network has ground UEs, ten UAVs at 100 m, and one HAP at 20 km in the default simulation.
- A UE task may be processed by one UAV, cooperatively split among multiple UAVs, or sent onward to the HAP.
- The communication model covers ground-to-UAV, UAV-to-UAV, and UAV-to-HAP channels, with default bandwidths of 1 MHz, 5 MHz, and 10 MHz.
- The energy model counts transmission and computation energy; UAV propulsion is treated as identical across offloading strategies and excluded from the optimization.
- The default simulation uses 10/20/30 UEs, task sizes in `[1, 4] MB`, UAV CPU rates in `[1, 3] GHz`, and HAP compute at 30 GHz.

## Method

- **DDQN mode selection.** The HAP acts as the agent that observes system state and chooses whether the task uses single-UAV, multi-UAV, or HAP processing.
- **PPO ratio assignment.** PPO runs only when multi-UAV cooperative processing is selected, outputting continuous workload proportions for the participating UAVs.
- **Reward design.** Both DDQN and PPO rewards penalize energy utilization and task-processing latency; the default experiments set the latency and energy weights equally.
- **Baselines.** PPO is compared against DDPG, SAC, TD3, greedy, and random variants inside the same offloading framework.

## Key findings

- The proposed DDQN-PPO scheme reaches the highest smoothed reward among the tested training methods and has smoother convergence than the reported alternatives.
- When the number of UEs varies, the proposed method reduces task-offloading latency by about 22%-27% and weighted system consumption by about 11%-20% relative to the DDPG-based Scheme 1.
- Compared with SAC/TD3-based alternatives, it reports roughly 35%-45% lower latency and 20%-30% lower weighted consumption in the UE-density experiments.
- Under varying task density, it reduces latency by about 17% and weighted consumption by about 10% versus Scheme 1.
- At task complexity 350 cycles/bit, it reports about 35% lower latency, 15% lower energy consumption, and 21% lower weighted system cost than Scheme 1.

## Limitations / future work

The evaluation is simulation-based, assumes enough UAV energy for forwarding/computation during experiments, omits return-result overhead, and treats HAP/UEs as clean-energy powered. The conclusion names future work on improving system availability, minimizing energy consumption further, and refining task-transmission strategies to improve MEC processing capacity.

## Relation to the corpus

This is a clean [[high-altitude-platform-station]] / [[hierarchical-aerial-mec]] offloading source. It complements [[nabi-2025-jour-hierarchical-aerial]], where matching and enhanced SAC coordinate UAV-HAP collaboration, and [[chen-2026-dart-hap-uav-mec]], where Lyapunov plus DDPG-attention handles HAP-UAV-MEC with NOMA and WPT. Its main method contribution is a [[hybrid-action-decision-making|discrete-continuous split]] using [[ddqn]] plus [[ppo]] rather than a single actor-critic policy.

## Raw artifacts

- `raw/sources/Joint Optimization of Latency and Energy Consumption for Computing Task Offloading Based on Cooperative Multi-UAV and HAP Networks/Joint Optimization of Latency and Energy Consumption for Computing Task Offloading Based on Cooperative Multi-UAV and HAP Networks.md`
- Original PDF and extracted figures (`images/`) in the same folder.
