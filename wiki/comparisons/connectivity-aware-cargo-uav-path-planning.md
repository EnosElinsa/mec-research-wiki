---
type: comparison
title: "Connectivity-aware cargo-UAV path planning: outage, coverage, and handoff formulations"
tags: [comparison, cargo-uav, cellular-connected-uav, radio-map, path-planning, handoff]
related:
  - "[[peng-2025-cargo-uav-energy-outage-tradeoff]]"
  - "[[huang-2026-hgadrl-cargo-uav-pickup-delivery]]"
  - "[[deng-2024-radio-map-uav-pickup-delivery]]"
  - "[[cao-2026-radio-map-cargo-pickup]]"
  - "[[chen-2026-cargo-uav-pickup-lae]]"
  - "[[cherif-2021-disconnectivity-aware-cargo-uav]]"
  - "[[cherif-2024-rl-cargo-uav-cell-association]]"
  - "[[radio-map-aided-uav-path-planning]]"
  - "[[handoff-aware-uav-trajectory-planning]]"
  - "[[cellular-connected-uav]]"
  - "[[uav-delivery-pickup-dropoff]]"
  - "[[ant-colony-optimization]]"
  - "[[genetic-algorithm]]"
  - "[[particle-swarm-optimization]]"
  - "[[dueling-dqn]]"
  - "[[uav-energy-replenishment-and-service-continuity]]"
created: 2026-11-03
updated: 2026-11-03
---

# Connectivity-aware cargo-UAV path planning: outage, coverage, and handoff formulations

A cargo UAV flying beyond visual line of sight depends on terrestrial base stations for command and control, but those base stations are tilted toward the ground. Seven sources in the wiki plan cargo-UAV routes so that the link stays usable while energy is minimized. They agree on that goal and differ in how they turn link quality into an objective term or a constraint, in what map they assume, and in how they split the task-order and path decisions. This page compares those choices.

## Roster

| Source | Fleet and task | Link-quality term | Map assumption | Order and path split | Reported result |
|---|---|---|---|---|---|
| [[peng-2025-cargo-uav-energy-outage-tradeoff]] | One UAV, deliveries from a warehouse | Expected outage time in a weighted-sum objective with energy | Radio map of outage probability | Improved ant colony for delivery order; dueling DDQN for the trajectory | About 6% to 50% better than the comparisons; higher outage weight improves the link at higher energy |
| [[huang-2026-hgadrl-cargo-uav-pickup-delivery]] | One UAV, deliveries then pickups | Coverage probability along the trajectory kept above a threshold | Radio coverage map from outage probability at the flight altitude | Genetic algorithm for service order; multi-step dueling DDQN per stage | Lower energy than DDQN and RRT benchmarks under four outage thresholds |
| [[deng-2024-radio-map-uav-pickup-delivery]] | One UAV, paired pickup and delivery | Interruption time added to Dijkstra edge weights | Radio map built first | Dijkstra variant for pairwise paths; hybrid genetic algorithm for the pickup-and-delivery order | About 20% energy saving over a pickup-and-delivery plan that ignores energy |
| [[cao-2026-radio-map-cargo-pickup]] | One UAV, pickups over multiple trips to a charging station | Cells below an SNR threshold excluded | Expected-SNR grid from a physical map | A* for pairwise paths; PSO for task allocation and flight speed | About 5% to 50% higher energy efficiency than the comparison |
| [[chen-2026-cargo-uav-pickup-lae]] | Several UAVs, pickups with customer time windows | Communication-aware trajectory learning; zero outage reported | No prior radio map | Simulated annealing for task sequences; D3QN for trajectories; explicit conflict resolution | 70% to 75% lower total weighted cost than baselines; 1,719 s completion time and 0.9969 satisfaction score |
| [[cherif-2021-disconnectivity-aware-cargo-uav]] | One UAV, delivery mission | Handoff rate in the objective; disconnectivity rate as a constraint | Connectivity heatmap; strongest-SIR base station serves each location | Dynamic programming over the trajectory | Parameter study over altitude, disconnectivity rate, and environment |
| [[cherif-2024-rl-cargo-uav-cell-association]] | One UAV, delivery mission | Energy, handoff events, and reliability as three objectives | Cell association chosen during flight | Q-learning for joint trajectory and cell association | Fewer handoffs, less disconnectivity, and less energy than benchmarks |

## Comparable dimensions

### How the link enters the problem

- **As a weighted cost.** [[peng-2025-cargo-uav-energy-outage-tradeoff]] puts expected outage time beside energy, and [[deng-2024-radio-map-uav-pickup-delivery]] folds interruption time into path lengths. The planner may accept outage if the energy saving is large enough.
- **As a hard limit.** [[huang-2026-hgadrl-cargo-uav-pickup-delivery]] requires coverage probability above a threshold, and [[cao-2026-radio-map-cargo-pickup]] removes cells below an SNR threshold before searching. Feasible paths are then link-safe by construction.
- **As a handoff count.** The two Cherif papers add the number of serving-cell changes to the objective because each handoff disturbs command and control. This is the [[handoff-aware-uav-trajectory-planning]] branch. The others ([[radio-map-aided-uav-path-planning]]) do not count handoffs.

### Order and path decomposition

Five of the seven sources split the problem the same way: a combinatorial order over customers or pickup points, and a path between consecutive points that respects the link model. They differ in which tools fill the two stages:

| Source | Order stage | Path stage |
|---|---|---|
| [[peng-2025-cargo-uav-energy-outage-tradeoff]] | [[ant-colony-optimization]] | [[dueling-dqn]] |
| [[huang-2026-hgadrl-cargo-uav-pickup-delivery]] | [[genetic-algorithm]] | [[dueling-dqn]] |
| [[deng-2024-radio-map-uav-pickup-delivery]] | Hybrid [[genetic-algorithm]] | Dijkstra variant |
| [[cao-2026-radio-map-cargo-pickup]] | [[particle-swarm-optimization]] (with speed) | A* |
| [[chen-2026-cargo-uav-pickup-lae]] | Simulated annealing | D3QN |

The Cherif papers plan one delivery path without a customer-order stage, using dynamic programming (2021) or Q-learning (2024).

### Energy model features

- [[peng-2025-cargo-uav-energy-outage-tradeoff]] tracks the UAV weight over time, and [[deng-2024-radio-map-uav-pickup-delivery]] ties energy to the pickup order and cargo weight, so carried load changes the cost of each leg.
- [[cao-2026-radio-map-cargo-pickup]] adds payload capacity and an on-board energy limit, so one mission takes multiple trips, and it optimizes flight speed.
- [[chen-2026-cargo-uav-pickup-lae]] adds customer time windows and inter-UAV collision avoidance, the only multi-UAV setting here.

## Non-comparability

- **No shared scenario.** Each source uses its own area, base-station layout, channel model, and customer set, and none reruns another's method. The percentage gains in the roster are each measured against that paper's own baselines.
- **Different link metrics.** Expected outage time, coverage probability thresholds, interruption-weighted distance, SNR feasibility, handoff count, and disconnectivity rate are different quantities. A plan that is best under one is not shown to be best under another.
- **Different task structures.** Delivery-only, pickup-only, paired pickup and delivery, delivery then pickup, and time-windowed multi-UAV pickup lead to different order problems, so order-stage solvers are not directly interchangeable.
- **Different map knowledge.** Five sources assume a map or heatmap computed before planning, [[cherif-2024-rl-cargo-uav-cell-association]] chooses cells online, and [[chen-2026-cargo-uav-pickup-lae]] learns without a prior radio map. Results that rely on an accurate map do not carry over to the map-free setting.
- **Simulation only.** No source reports a flight test.

## Gaps

- No source combines a handoff count with an outage-probability radio map in one objective.
- Only [[chen-2026-cargo-uav-pickup-lae]] has more than one UAV, so shared-cell load and handoff interactions between cargo UAVs are not modeled.
- [[cao-2026-radio-map-cargo-pickup]] is the only source with multiple trips and recharging; the others assume one sortie suffices. [[uav-energy-replenishment-and-service-continuity]] covers recharging in other missions.
