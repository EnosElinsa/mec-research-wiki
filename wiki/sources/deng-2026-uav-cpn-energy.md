---
type: source
title: "UAV-Enabled Computing Power Networks: Design and Performance Analysis Under Energy Constraints"
authors: ["Yiqin Deng", "Zhengru Fang", "Senkang Hu", "Yanan Ma", "Xiaoyu Guo", "Haixia Zhang", "Yuguang Fang"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3655118"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC), vol. 25, no. 7, pp. 9563-9577, Jul. 2026"
tags: [source, computing-power-network, uav, stochastic-geometry, energy-constraints, task-offloading]
related:
  - "[[uav-enabled-computing-power-network]]"
  - "[[stochastic-geometry-network-analysis]]"
  - "[[low-altitude-intelligent-network]]"
  - "[[task-offloading]]"
  - "[[uav-mobile-relaying]]"
  - "[[yuguang-fang]]"
  - "[[hu-2026-segmented-irs-cpn]]"
created: 2026-07-07
updated: 2026-07-13
---

# UAV-Enabled Computing Power Networks: Design and Performance Analysis Under Energy Constraints

## Citation

Deng, Y., Fang, Z., Hu, S., Ma, Y., Guo, X., Zhang, H., & Fang, Y. (2026). *UAV-Enabled Computing Power Networks: Design and Performance Analysis Under Energy Constraints*. **IEEE Transactions on Mobile Computing**, 25(7), 9563-9577. DOI: 10.1109/TMC.2026.3655118.

## TL;DR

Introduces [[uav-enabled-computing-power-network|UAV-enabled Computing Power Networks]] as a way to mitigate MEC resource islands. A UAV relays tasks from a request zone to a wider service zone of computing nodes, and stochastic-geometry analysis quantifies task-completion probability under communication, computation, fuel, and battery constraints.

## Problem

MEC resources can be geographically isolated: users in a request zone may not have enough nearby computing capacity, while farther computing nodes sit unused. The paper asks how a UAV relay can expand the service zone and how altitude, transmit power, computing-node density, and UAV energy jointly affect the probability that a task completes before its latency deadline.

## System model

The benchmark model uses one UAV hovering above the request-zone center, ground users uniformly distributed in the request zone, and computing nodes drawn from a Poisson point process over a service zone. A ground user uploads through the UAV to a computing node; result return is ignored because result data are assumed small. The UAV has hybrid fuel-cell and battery energy constraints, and air-ground channels use probabilistic LoS/NLoS modeling.

## Method

The paper derives task-completion probability as the probability that at least one computing node satisfies both communication and computation latency constraints. It thins the computing-node PPP by feasible communication and computation conditions, derives the effective computing-node density and expected qualified-node count, then optimizes UAV altitude and transmit power under fuel and battery constraints with alternating single-parameter optimization.

## Key findings

- Monte Carlo simulation with 10000 runs and 400 ground users validates the analytical task-completion probability.
- Task-completion probability is poor at too-low and too-high altitudes; the parsed example reports an optimal altitude around 200 m when the computation-latency parameter is 2 ms.
- Increasing the computing-node distribution radius from 200 m to 1000 m raises task-completion probability from 46.65% to 99.14% in the reported case.
- Energy constraints are severe: at 30 dBW and 310 m, task-completion probability drops from the ideal value of 1 to nearly 0 in the parsed energy-constrained comparison.
- Joint altitude/power optimization reports average gains of 29.6%-247.7% and a peak gain above 390% across the tested scenarios.
- Compared with Bayesian optimization, the proposed algorithm reports 13.8% average improvement, 49.16% peak improvement, and better performance in 69.2% of scenarios.

## Limitations / future work

The paper uses a single-UAV and single-computing-node execution benchmark for tractability. It does not model multi-CN parallel/cooperative execution, multi-user interference, or resource contention. Future work includes joint CN selection, task partitioning, and more integrated computing/communication designs.

## Relation to the corpus

This is an analytical [[stochastic-geometry-network-analysis]] entry rather than a DRL offloading policy. It connects low-altitude relaying to computing-resource pooling and complements UAV mobile-relay foundations such as [[zeng-2016-throughput-relaying]], but its metric is task-completion probability over a PPP-distributed computing-power service zone.

## Raw artifacts

- `raw/sources/UAV-Enabled Computing Power Networks Design and Performance Analysis Under Energy Constraints/UAV-Enabled Computing Power Networks Design and Performance Analysis Under Energy Constraints.md`
- Original PDF and extracted figures (`images/`) in the same folder.
