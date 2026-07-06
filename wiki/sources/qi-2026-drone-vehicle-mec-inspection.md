---
type: source
title: "Cooperative Drone-Vehicle Mobile Edge Computing for Low-Altitude Inspection"
authors: ["Weidong Qi", "Weifeng Zhong", "Jiawen Kang", "Xumin Huang", "Dong In Kim", "Shengli Xie", "Chau Yuen"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3698194"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, vehicle-fog-computing, vehicular-mec, uav-enabled-its, task-offloading, uav-charging-scheduling, route-planning, makespan-minimization]
related:
  - "[[vehicle-fog-computing]]"
  - "[[vehicular-mec]]"
  - "[[uav-enabled-its]]"
  - "[[task-offloading]]"
  - "[[uav-charging-scheduling]]"
  - "[[makespan-minimization]]"
  - "[[rotary-wing-propulsion-energy-model]]"
  - "[[sun-2024-mvtora-postdisaster-vfc]]"
  - "[[wei-2026-airfogsim-uav-vfc]]"
  - "[[weifeng-zhong]]"
  - "[[jiawen-kang]]"
  - "[[xumin-huang]]"
  - "[[shengli-xie]]"
created: 2026-07-06
updated: 2026-07-06
---

# Cooperative Drone-Vehicle Mobile Edge Computing for Low-Altitude Inspection

## Citation

Qi, W., Zhong, W., Kang, J., Huang, X., Kim, D. I., Xie, S., & Yuen, C. (2026). *Cooperative Drone-Vehicle Mobile Edge Computing for Low-Altitude Inspection*. **IEEE Transactions on Mobile Computing**, 1-18. DOI: 10.1109/TMC.2026.3698194.

## TL;DR

Proposes a drone-vehicle MEC (DVMEC) model for low-altitude inspection. A ground vehicle carries an accompanying drone and a detached drone; the accompanying drone collects data at vehicle-visited nodes, while the detached drone visits other nodes independently, processes some data in flight, returns to the vehicle for battery swapping, and offloads remaining data to the vehicle for processing. A heuristic jointly optimizes the ground-vehicle route, detached-drone sorties, and detached-drone speeds to minimize mission completion time.

## Problem framing

Drone-assisted MEC is flexible but constrained by onboard compute, battery energy, and dependence on infrastructure. Fixed base stations can help but are costly and inflexible in remote inspection areas. A vehicle can instead carry compute and energy resources into the field, but this creates a coupled route-planning and compute-offloading problem: the vehicle route, detached-drone sorties, in-flight processing, vehicle processing, and battery swaps all affect the mission completion time.

## System model

- A ground vehicle departs from and returns to a depot while visiting data collection nodes.
- The accompanying drone stays with the vehicle and collects data when the vehicle is stationed at a node.
- The detached drone can leave the vehicle, visit one data collection node per sortie, process data while flying to the rendezvous node, and offload remaining data to the vehicle.
- The vehicle supplies battery swapping and processes data offloaded from the drones.
- Each collection node is visited exactly once, either by the ground vehicle/accompanying drone or by the detached drone.

## Method

- Formulates a DVMEC route-planning and offloading problem that includes route variables, detached-drone sortie variables, battery capacity, data collection, data processing, and mission completion time.
- Uses a heuristic to optimize the vehicle route and detached-drone sorties.
- Optimizes detached-drone speed by analyzing the relationship between flight speed and the amount of data the drone can process before rendezvous.
- Derives two approximate flight-power expressions through series expansions so speed optimization can be solved efficiently.

## Key findings

- The approximate detached-drone flight-power model has a maximum relative error no greater than 0.8% in Fig. 4.
- In an 8-node example, the optimized route reduces mission completion time from 138.72 minutes to 107.04 minutes, a 22.84% reduction.
- In a 30-node example, the optimized route reduces completion time from 429.96 minutes to 356.24 minutes, a 17.14% reduction.
- With 20 collection nodes and varying mean data size, the proposed model reduces completion time by 3.59%, 2.93%, and 10.42% compared with fixed detached-drone speed, no detached-drone computing, and no detached drone.
- With node count varying from 15 to 30, the corresponding reductions are 4.25%, 3.75%, and 14.21%.
- Increasing detached-drone battery capacity from 130 kJ to 250 kJ increases feasible sorties and reduces mission time; above 250 kJ the detached-drone node proportion fluctuates around 36%.

## Limitations / future work

The model focuses on one ground vehicle carrying one accompanying drone and one detached drone, and on a setting where drones collect data with onboard sensors rather than relaying data from pre-deployed sensors or IoT devices. The parse does not state a separate future-work section.

## Relation to the corpus

This is a vehicle-assisted MEC entry adjacent to [[vehicle-fog-computing]] and [[vehicular-mec]], but its vehicle is a mobile compute/energy carrier for drones rather than a vehicular user offloading to RSUs. It complements [[wei-2026-airfogsim-uav-vfc]], which supplies simulation infrastructure for UAV-integrated vehicular fog systems, and [[sun-2024-mvtora-postdisaster-vfc]], where vehicles form a fog layer under UAV clients and UAV-edge servers. The repeated Guangdong University of Technology authors link it to the existing [[jiawen-kang]], [[xumin-huang]], [[weifeng-zhong]], and [[shengli-xie]] entity pages.

## Raw artifacts

- `raw/sources/Cooperative Drone-Vehicle Mobile Edge Computing for Low-Altitude Inspection/Cooperative Drone-Vehicle Mobile Edge Computing for Low-Altitude Inspection.md`
- Original PDF and extracted figures (`images/`) in the same folder.
