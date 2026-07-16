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
updated: 2026-07-16
modeling_card: required
---

# Cost-Aware UAV-Enabled Computation Offloading for Green Internet of Things

## Citation

Panahi, F. H., & Panahi, F. H. (2026). *Cost-Aware UAV-Enabled Computation Offloading for Green Internet of Things*. **IEEE Transactions on Green Communications and Networking**, 10, 366-375. DOI: 10.1109/TGCN.2025.3580453.

## TL;DR

A single UAV provides computation offloading (COF) service to IoT devices while managing its own energy procurement cost (EPC). The UAV can draw paid laser energy from local laser beam directors (LBDs), harvest local renewable energy (wind in the simulations), and earn compensation by charging IoT devices for COF and wireless charging service. A lightweight Q-learning trajectory policy selects which regions to visit within a mission-time limit; a deterministic EPC minimization then decides how much energy to draw from laser, battery, renewable generation, computation service, and WPT.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: One UAV edge server visits $K$ ground regions containing $N$ IoT devices. It hovers to receive and compute offloaded tasks, may wirelessly charge devices, procures energy from local laser beam directors, and stores renewable energy in an onboard battery.

**Problem & objective**: First maximize the number of offloaded devices by selecting a region order $V$ under mission time $T^m$; then minimize each region's procurement cost $C_k=\rho_k^l\eta_l e_k^l-(\rho_k^w\eta_w e_k^w+\rho_k^c e_k^c)$ and the aggregate cost over the selected route.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Region visit order | $V$ | discrete sequence | Order in which the UAV visits regions |
| Offloading indicator | $\delta_{ik}$ | binary | Device $i$ offloads while the UAV is over region $k$ |
| Wireless-charging energy | $e_k^w$ | continuous, nonnegative | Energy sent to IoT devices in region $k$ |
| Battery energy | $e_k^b$ | continuous, nonnegative | Energy drawn from the onboard battery |
| Laser energy | $e_k^l$ | continuous, nonnegative | Energy procured from the nearest LBD |
| Computation energy | $e_k^c$ | continuous, $0\le e_k^c\le e_k^{c,\mathrm{req}}$ | Energy assigned to offloaded computation |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Residual mission time is nonnegative for every visited region: $T_k^r=T^m-T_k^e\ge0$ |
| C2 | UAV energy balance: $e_k^b+e_k^l=e_k^u$ |
| C3 | Battery bounds after cumulative renewable generation: $B_l\le\sum_{i=1}^ke_i^r-\sum_{i=1}^k(e_i^b+e_i^w+e_i^c)\le B_u$ |
| C4 | Computation allocation cannot exceed required energy: $0\le e_k^c\le e_k^{c,\mathrm{req}}$ |
| C5 | Energy allocations are nonnegative: $e_k^b,e_k^w,e_k^l\ge0$ |

**Algorithm**: Use action-candidate Q-learning with a reduced feasible next-region set satisfying coverage and residual-time checks to choose $V$; for each selected route solve the region-level linear EPC program over $e_k^w,e_k^b,e_k^l,e_k^c$.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Panahi and Panahi [x] develop a cost-aware UAV computation-offloading model that combines paid laser energy, renewable generation, onboard storage, computation service, and wireless charging revenue. A lightweight Q-learning policy selects a feasible sequence of regions to maximize the number of served IoT devices within the mission-time budget. Given that route, a linear procurement-cost problem allocates laser, battery, charging, and computation energy under energy-balance, battery, and computation limits. Simulations show route coverage and procurement cost respond to service prices, conversion losses, flight speed, and processing capacity, while cost compensation remains more profitable than a baseline without service pricing.

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
