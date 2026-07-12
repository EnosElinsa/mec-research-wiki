---
type: source
title: "Energy-Efficient Trajectory Optimization for UAV-Assisted IoT Networks"
authors: ["Liang Zhang", "Abdulkadir Celik", "Shuping Dang", "Basem Shihada"]
year: 2022
url: "https://doi.org/10.1109/TMC.2021.3075083"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC), vol. 21, no. 12, pp. 4323-4337"
tags: [source, uav-iot, trajectory-control, solar-energy-harvesting, charging-stations, reinforcement-learning, fairness, energy-efficiency]
related:
  - "[[uav-trajectory-control]]"
  - "[[uav-charging-scheduling]]"
  - "[[energy-harvesting-mec]]"
  - "[[jains-fairness-index]]"
  - "[[rotary-wing-propulsion-energy-model]]"
  - "[[zeng-2017-energy-efficient-uav-trajectory]]"
  - "[[liu-2020-distributed-uav-coverage-navigation]]"
  - "[[lin-2025-energy-effective-ris-multiuav-coverage]]"
created: 2026-07-13
updated: 2026-07-13
---

# Energy-Efficient Trajectory Optimization for UAV-Assisted IoT Networks

## Citation

Zhang, L., Celik, A., Dang, S., & Shihada, B. (2022). *Energy-Efficient Trajectory Optimization for UAV-Assisted IoT Networks*. **IEEE Transactions on Mobile Computing**, 21(12), 4323-4337. DOI: 10.1109/TMC.2021.3075083.

## TL;DR

A solar-powered UAV chooses reachable charging-station or serving-point destinations with action-confined Q-learning or SARSA. The reward balances downlink data, net energy, battery survival, and Jain-style service fairness for intermittently active IoT terminals.

## Problem

A UAV base station must keep serving spatially distributed IoT terminals without exhausting its battery. Solar input, terminal activity, flight cost, charging access, link quality, and accumulated service fairness all change the value of the next destination.

## System model

- One rotary-wing UAV moves among fixed charging stations and candidate serving points over finite decision epochs.
- Each epoch consists of travel followed by land-and-charge or hover-and-serve operation. The state contains UAV location, time, and residual battery.
- DRX terminals are active with time-varying probabilities and are served only when active and above an SNR threshold. Orthogonal channels and uniform bandwidth allocation remove modeled co-channel interference.
- The UAV harvests solar energy while moving or serving and receives additional energy at charging stations. Energy accounting includes horizontal/vertical motion, hovering, and transmission.
- [[jains-fairness-index|Jain's index]] is applied to cumulative per-terminal service counts.

## Method

Both tabular schemes prune destinations that cannot be reached within the epoch and then use epsilon-greedy exploration. The off-policy controller applies Q-learning and updates toward the best next action, while the on-policy controller applies SARSA and updates toward the action it will execute. Battery depletion terminates the episode and produces a large penalty.

## Key findings

- Both methods converge after about `3 x 10^5` training episodes in the reported setup; epsilon `0.1` performs best, while greedy control obtains about half the best reward and fully random control frequently depletes the battery.
- With epsilon `0.01`, the on-policy method reaches about `80%` of its maximum cumulative reward after `45,000` episodes; the off-policy method reaches that level sooner.
- In the five-hour deployment test, greedy and random search deplete the battery at steps `3` and `5`, whereas the epsilon-greedy learned policies complete the simulated run.
- Higher altitude trades lower data rate for greater modeled solar harvest. Beyond `50` terminals, data-rate growth slows and fairness falls in the reported sensitivity study.

## Limitations / parse caveats

The evaluation is simulation-only and covers one UAV, fixed candidate destinations, specified simulation models for terminal activity and solar harvest, constant-speed motion, orthogonal channels, and no multi-UAV interference. The conclusion defers partial observability, multi-UAV cooperation, resource allocation, interference mitigation, and UAV-to-UAV links. The parse damages the optimization display, epsilon-greedy probabilities, complexity expressions, and several equations; its battery recursion prints `max` where the capacity description suggests an upper cap. Separate result paragraphs report on-policy reward as both `96.3%` and `90%` of off-policy reward, so neither ratio is promoted as a reconciled finding.

## Relation to the corpus

This source combines renewable harvesting and explicit [[uav-charging-scheduling]] with discrete [[uav-trajectory-control]]. Unlike [[zeng-2017-energy-efficient-uav-trajectory]], its route is learned over charging/serving points rather than optimized as a continuous trajectory, and unlike [[liu-2020-distributed-uav-coverage-navigation]], it explicitly models solar input and station charging.

## Raw artifacts

- Parse: `raw/sources/Energy-Efficient_Trajectory_Optimization_for_UAV-Assisted_IoT_Networks/Energy-Efficient_Trajectory_Optimization_for_UAV-Assisted_IoT_Networks.md`
- Origin PDF: `raw/sources/Energy-Efficient_Trajectory_Optimization_for_UAV-Assisted_IoT_Networks/Energy-Efficient_Trajectory_Optimization_for_UAV-Assisted_IoT_Networks.pdf`
- Figures: `raw/sources/Energy-Efficient_Trajectory_Optimization_for_UAV-Assisted_IoT_Networks/images/`
