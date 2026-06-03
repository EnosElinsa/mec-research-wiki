---
type: concept
title: "Hot Spot Problem in IoT Routing"
tags: [iot, wireless-sensor-network, routing, energy-efficiency, load-balancing]
related:
  - "[[omrp-overlap-routing]]"
  - "[[first-order-radio-energy-model]]"
  - "[[load-balancing-uav-mec]]"
  - "[[fairness-metrics-in-mec]]"
  - "[[collaborative-beamforming]]"
  - "[[li-2025-omrp-cb-iot]]"
created: 2026-06-03
updated: 2026-06-03
---

# Hot Spot Problem in IoT Routing

The hot spot problem is the disproportionate energy drain on IoT nodes near the base station (BS) or sink. These nodes bear a double burden: they relay data from many upstream nodes (transmission energy proportional to total traffic), and distance-greedy routing keeps selecting them, accelerating their depletion.

## Mechanism
In a hierarchical routing protocol, the last-hop cluster heads / relay nodes nearest the BS transmit the most accumulated data over the longest single link. Under the [[first-order-radio-energy-model]], long-distance transmission energy scales as d⁴ in the multipath regime, so the penalty is severe. Once these near-BS nodes die, the network can partition or lose its path to the BS even while many other nodes still have energy.

## Consequences
- First-Node-Death and early degradation concentrated in the near-BS zone.
- Throughput collapses before the network's overall energy budget is exhausted.
- Residual-energy fairness ([[fairness-metrics-in-mec]]) degrades rapidly once hot-spot nodes deplete.

## Mitigations in the literature
| Approach | Mechanism |
|---|---|
| LEACH / R-LEACH | Round-robin CH election spreads relay load over time |
| [[omrp-overlap-routing]] | Elects geographically central (high-overlap) CHs and uses multihop to shorten last-hop distance |
| [[collaborative-beamforming]] | A virtual antenna array lets any node — not just the nearest — contribute to long-range transmission, decoupling geography from relay duty |
| [[load-balancing-uav-mec]] (UAV context) | Mobile UAVs reposition to equalize load; not applicable to static IoT |

## Connection to collaborative beamforming
As argued in [[li-2025-omrp-cb-iot]], CB decouples geographic position from transmission capability: an N-node virtual antenna array yields N²-fold received-power gain, so nodes far from the BS can still contribute to the uplink without being individually burdened. The [[softppo-lstm]] node-selection policy weighs residual energy and location jointly rather than always picking near-sink nodes, avoiding the hot-spot formation that pure distance-greedy strategies cause.
