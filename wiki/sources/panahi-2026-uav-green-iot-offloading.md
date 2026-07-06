---
type: source
title: "Cost-Aware UAV-Enabled Computation Offloading for Green Internet of Things"
authors: ["Fereidoun H. Panahi", "Farzad H. Panahi"]
year: 2026
url: "https://doi.org/10.1109/TGCN.2025.3580453"
venue: "IEEE Transactions on Green Communications and Networking (IEEE TGCN)"
tags: [source, uav-mec, green-iot, computation-offloading, energy-procurement, wireless-power-transfer, renewable-energy, q-learning]
related:
  - "[[wireless-power-transfer]]"
  - "[[energy-harvesting-mec]]"
  - "[[energy-procurement-compensation]]"
  - "[[task-offloading]]"
  - "[[uav-trajectory-control]]"
  - "[[air-ground-integrated-network]]"
  - "[[wang-2025-airground-laser-mec]]"
  - "[[zhou-2018-uav-wireless-powered-mec]]"
  - "[[xu-2018-uav-wpt-trajectory]]"
created: 2026-07-06
updated: 2026-07-06
---

# Cost-Aware UAV-Enabled Computation Offloading for Green Internet of Things

## Citation

Panahi, F. H., & Panahi, F. H. (2026). *Cost-Aware UAV-Enabled Computation Offloading for Green Internet of Things*. **IEEE Transactions on Green Communications and Networking**, 10, 366-375. DOI: 10.1109/TGCN.2025.3580453.

## TL;DR

A single UAV provides computation offloading (COF) service to IoT devices while managing its own energy procurement cost (EPC). The UAV can draw paid laser energy from local laser beam directors (LBDs), harvest local renewable energy (wind in the simulations), and earn compensation by charging IoT devices for COF and wireless charging service. A lightweight Q-learning trajectory policy selects which regions to visit within a mission-time limit; a deterministic EPC minimization then decides how much energy to draw from laser, battery, renewable generation, computation service, and WPT.

## Problem

Most UAV-enabled COF papers optimize trajectory or energy consumption, but do not model how a long-running UAV buys energy, uses local renewable supply, or offsets those procurement costs through service revenue. This paper asks how a UAV can remain economically and energetically viable while serving IoT devices under limited mission time and battery capacity.

## System model

- **Actors:** one GBS, one UAV edge server, N stationary IoT / mobile devices divided across K regions, and ground LBDs distributed by a Poisson point process.
- **Energy sources:** nearest LBD laser energy, an onboard battery, and local renewable energy; wind energy is used in the numerical model.
- **Services:** the UAV processes offloaded tasks and can wirelessly recharge low-power IoT devices via [[wireless-power-transfer]].
- **Pricing:** the UAV pays for laser-procured energy and receives fixed-price payments for COF and WPT service.
- **Timing:** the UAV selects a region sequence within mission time `T_m`; in the default scenario it hovers over visited regions to process scheduled offloaded tasks.

## Method

The trajectory problem is formulated as a lightweight reinforcement-learning task: Q-learning selects the sequence of regions that maximizes the number of offloaded IoT devices under mission-time constraints. Given that sequence, the energy-control unit solves a region-level EPC minimization problem over laser-procured energy, battery energy, wireless-charging energy, and computation energy. The resulting cost can be positive or negative depending on procurement cost versus COF / WPT income.

## Key findings

- With a 180 s mission, the learned trajectory serves about **28% of IoT devices** and **32% of regions** in the reported setup.
- Increasing the unit COF price makes the UAV allocate more energy to computation, increasing the COF rate and lowering EPC, but also raises UAV energy consumption because more task service is delivered.
- Realistic energy-conversion losses do not change the internal usable-energy allocation, but they increase EPC / expenses and reduce WPT income and profit versus ideal conversion.
- The proposed cost-compensation model maintains higher profit than a conventional baseline without service pricing as unit laser-energy price increases.
- The paper explicitly discusses future beam-tracking / alignment errors, AI-based power control, DQL / Meta-RL, multi-UAV MARL, and deployment / regulatory integration.

## Limitations / future work

The work is simulation-only and single-UAV. Prices are fixed by region rather than dynamically negotiated. Laser-beam alignment, weather, safety, malicious demand, and regulatory constraints are acknowledged but not modeled in the core experiments. The Q-learning trajectory is intentionally lightweight; continuous trajectories and large-scale multi-UAV coordination are left to future DQL / MARL extensions.

## Relation to the corpus

This source sits in the [[wireless-power-transfer]] and energy-efficiency track, but its distinctive contribution is economic: [[energy-procurement-compensation]] links the UAV's paid LBD / renewable energy supply to revenue from COF and WPT service. It is adjacent to [[wang-2025-airground-laser-mec]], where a ground AP laser-charges a UAV, but differs by using distributed LBDs, local renewable energy, and explicit service-pricing compensation. It also contrasts with [[zhou-2018-uav-wireless-powered-mec]] and [[xu-2018-uav-wpt-trajectory]], which optimize WPT / trajectory structure without the same procurement-cost accounting.

## Raw artifacts

- `raw/sources/Cost-Aware UAV-Enabled Computation Offloading for Green Internet of Things/Cost-Aware UAV-Enabled Computation Offloading for Green Internet of Things.md`
- Original PDF and extracted figures (`images/`) in the same folder.
