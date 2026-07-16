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
updated: 2026-07-16
modeling_card: required
---

# Joint Optimization of Latency and Energy Consumption for Computing Task Offloading Based on Cooperative Multi-UAV and HAP Networks

## Citation

Li, M., Wan, H., Lv, S., Si, P., Zhang, H., & Yu, F. R. (2026). *Joint Optimization of Latency and Energy Consumption for Computing Task Offloading Based on Cooperative Multi-UAV and HAP Networks*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2026.3683404.

## TL;DR

Builds a [[hierarchical-aerial-mec]] offloading model with terrestrial UEs, multiple UAVs, and one [[high-altitude-platform-station|HAP]]. Each task can be processed by a single UAV, split across multiple UAVs, or sent through UAVs to the HAP. The objective is a weighted system consumption combining processing latency and energy. The method is a two-stage DRL controller: [[ddqn]] chooses the offloading mode, and [[ppo]] sets task-splitting ratios when cooperative multi-UAV processing is selected.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Ground UEs generate tasks for a hierarchical aerial MEC network with multiple MEC-enabled UAVs and one HAP. A task is processed by one UAV, split among cooperative UAVs, or forwarded through UAVs to the HAP; the model includes ground-UAV, UAV-UAV, and UAV-HAP links with queue-dependent transmission and computation latency.

**Problem & objective**: Problem $\mathcal P0$, an NP-hard MINLP reformulated as an MDP, minimizes weighted latency and energy, $\min\sum_{i,u,n}(\alpha T_i+\beta E_i)$, while selecting one offloading mode, cooperative split ratios, and CPU allocations.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Single-UAV mode | $\mu_i^{sp}$ | binary | Task $i$ is processed by one UAV |
| Multi-UAV mode | $\mu_i^{mp}$ | binary | Task $i$ is split among cooperative UAVs |
| HAP mode | $\mu_i^H$ | binary | Task $i$ is forwarded to the HAP |
| Cooperative split ratio | $P_u^i$ | continuous, $0\le P_u^i\le1$ | Fraction of a multi-UAV task assigned to UAV $u$ |
| UAV/HAP CPU frequency | $f_u$ | continuous, $10^9\le f_u\le3\times10^9$ | Computation rate of aerial server $u$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Exactly one mode is selected, $\mu_i^{sp}+\mu_i^{mp}+\mu_i^H=1$ |
| C2 | Every task meets its maximum allowable processing delay |
| C3 | Cooperative ratios sum to one when multi-UAV mode is selected, $\sum_uP_u^i=1$ |
| C4 | CPU frequencies stay in the UAV/HAP operating interval |
| C5 | Queue, communication, and task-completion equations remain feasible for each slot |

**Algorithm**: Observe the MDP state → DDQN selects single-UAV, multi-UAV, or HAP mode → PPO outputs continuous cooperative split ratios when needed → update rewards from weighted latency and energy → repeat with replay and target-network updates.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Li et al. [x] studied cooperative computation offloading in a hierarchical aerial MEC network with ground UEs, multiple UAVs, and a HAP. They formulated an NP-hard mixed-integer nonlinear program that minimizes a weighted combination of task-processing latency and energy consumption while choosing single-UAV, multi-UAV, or HAP processing and the cooperative split ratios. The problem was reformulated as a Markov decision process, with DDQN selecting the discrete offloading mode and PPO assigning continuous ratios when multi-UAV processing is selected. The state includes aerial energy, inter-UAV and UAV-HAP rates, queues, CPU frequencies, and task size. Simulations report lower latency and weighted system consumption than the evaluated DDPG, SAC, TD3, greedy, and random alternatives under varying user counts and task complexity.

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
