---
type: source
modeling_card: required
title: "Dynamic Trajectory Design for Multi-UAV-Assisted Mobile Edge Computing"
authors: ["Zhuwei Wang", "Haowei Wang", "Lihan Liu", "Enchang Sun", "Haijun Zhang", "Zhidu Li", "Chao Fang", "Meng Li"]
year: 2025
url: "https://doi.org/10.1109/TVT.2024.3485182"
venue: "IEEE Transactions on Vehicular Technology (IEEE TVT)"
tags: [source, uav-mec, multi-uav-assisted-mec, trajectory-optimization, flight-dynamics, maddpg, blockchain, resource-allocation]
related:
  - "[[haijun-zhang]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[uav-trajectory-control]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[blockchain-for-fl-aggregation]]"
  - "[[maddpg]]"
created: 2026-06-04
updated: 2026-07-16
---

# Dynamic Trajectory Design for Multi-UAV-Assisted Mobile Edge Computing

## Citation

Wang, Z., Wang, H., Liu, L., Sun, E., Zhang, H., Li, Z., Fang, C., & Li, M. (2025). *Dynamic Trajectory Design for Multi-UAV-Assisted Mobile Edge Computing*. **IEEE Transactions on Vehicular Technology**, 74(3). DOI: 10.1109/TVT.2024.3485182. (Received 28 June 2024; accepted 15 October 2024; published 5 November 2024; current version 5 March 2025.)

## TL;DR

Addresses **UAV flight dynamics** constraints in multi-UAV MEC trajectory optimization — a constraint explicitly noted as overlooked in prior work. Within a blockchain-secured multi-UAV MEC framework, proposes **MADDPG-LC**: MADDPG handles desired-trajectory design; a Linear Quadratic Regulator (LQR) tracks actual trajectories subject to real flight-dynamics equations; a CVXPY solver handles user association and computing frequency assignment. The algorithm jointly minimizes weighted energy consumption and delay in a dynamic environment with user mobility and time-varying task demands.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: $K$ mobile users with Gauss-Markov mobility and time-varying tasks offload to $M$ UAV MEC servers that also maintain a blockchain ledger. Air-to-ground rates, blockchain generation and verification overhead, and continuous UAV flight dynamics jointly determine energy and delay.

**Problem & objective**: P1 is a dynamic mixed discrete-continuous control problem that minimizes a weighted energy-delay cost, $\min \omega_E E_{\mathrm{tot}}+\omega_D D_{\mathrm{tot}}$, over trajectories, association, and computing resources.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Desired UAV trajectory | $\mathbf q_m^{\mathrm d}(t)$ | continuous position | Communication-aware path requested from UAV $m$ |
| UAV acceleration | $\mathbf a_m(t)$ | continuous bounded control | Flight-dynamics input used to track the desired path |
| User association | $x_{k,m}(t)$ | binary | Whether user $k$ offloads to UAV $m$ |
| Computing frequency | $f_{k,m}(t)$ | continuous, nonnegative | CPU frequency assigned to user $k$ at UAV $m$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | UAV position and velocity follow the discretized flight-dynamics equations |
| C2 | Acceleration, speed, flight-region, and tracking commands remain feasible |
| C3 | Each user associates with at most one UAV, $\sum_m x_{k,m}(t)\le 1$ |
| C4 | Each UAV serves no more than its user limit and CPU allocations stay within capacity |
| C5 | Communication, computation, propulsion, and blockchain delay and energy terms enter the horizon cost |

**Algorithm**: Use MADDPG to generate desired multi-UAV trajectories → track physically feasible trajectories with LQR → solve association and CPU-frequency allocation in CVXPY for the realized geometry → update the dynamic state and repeat.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Wang et al. [x] studied dynamic trajectory design in a blockchain-secured multi-UAV mobile edge computing network with mobile users and time-varying tasks. They formulated a joint energy and delay minimization problem subject to UAV flight dynamics, user association, and computing-resource constraints. Their MADDPG-LC method uses MADDPG to generate desired trajectories, an LQR controller to track physically feasible trajectories, and convex optimization to allocate associations and CPU frequencies. The blockchain model accounts for transaction generation, broadcast, consensus verification, and their associated energy and delay. Simulation results show lower weighted energy-delay cost and smaller desired-to-actual trajectory error than the evaluated trajectory baselines.

## Problem framing

Most UAV-MEC trajectory designs treat the UAV as a point that can change course arbitrarily. In reality, UAV velocity and acceleration are governed by Newtonian flight dynamics (parse Eq. 21–25), so the "desired" trajectory computed by an optimizer may be physically unrealizable. Additionally, offloading sensitive task data over wireless links raises security concerns; blockchain is integrated for tamper-proof logging of offloading transactions. User mobility follows a Gauss-Markov model, and task arrivals vary per slot, creating a highly dynamic optimization landscape that rules out offline trajectory planning.

## System model

- **M UAVs**, each carrying a MEC server and acting as a blockchain node. **K mobile users** with time-varying tasks.
- **UAV dynamics.** Continuous-time double-integrator model (position + velocity states, acceleration input), discretized per slot. Delay τ between command and execution is modeled (parse Eqs. 21–25).
- **Blockchain.** Each offloading record is hashed into a transaction, broadcast to all UAVs, and verified via a consensus process. Block generation and verification introduce additional delay D_m^g, D^v and energy (parse Eqs. 12–17).
- **Objective (P1).** Minimize weighted sum of total energy and total delay over the horizon, subject to flight dynamics, user association (each user connected to at most one UAV; each UAV serves ≤ N_max users), computing resource constraints.
- **Decomposition.** P1 → three subproblems: (P2.1) desired trajectory design (MADDPG), (P2.2) actual trajectory tracking (LQR), (P2.3) user association and CPU frequency assignment (CVXPY).

## Method

1. **MADDPG** (Multi-Agent DDPG, centralized-training / decentralized-execution) treats each UAV as an agent with local observations (UAV positions, user locations, task loads). Outputs desired flight acceleration; continuous action space.
2. **LQR tracking controller** maps the desired trajectory to the actual physically feasible trajectory by minimizing deviation from the desired path while respecting flight-dynamics constraints. This two-stage design separates the communication/compute optimization from real flight control.
3. **CVXPY** solves the convex user-association and computing-frequency allocation problem per slot given the derived trajectories.

## Key findings

- MADDPG-LC achieves **lower weighted energy-delay cost** than benchmark strategies (including MADDPG without LQR, random trajectory, and hover-only) in numerical simulations (parse Section V).
- Accounting for UAV flight dynamics via LQR tracking reduces the gap between desired and actual trajectories, avoiding performance degradation caused by physically infeasible trajectory commands (parse Section V and abstract).
- The blockchain overhead (block generation + consensus delay) is quantified and shown to be manageable within the system's energy-delay budget (parse Sections III-D, V).

## Limitations / future work

Parse does not enumerate explicit quantitative gains over baselines beyond figures. Blockchain consensus overhead grows with M; scalability to very large UAV swarms is not analyzed. Channel model is a simplified air-to-ground path loss without small-scale fading in the trajectory optimization loop.

## Relation to the corpus

Distinguished from most corpus UAV-MEC trajectory papers by explicitly modeling **flight dynamics** constraints (via LQR) rather than treating UAVs as free-flying points. The [[centralized-training-decentralized-execution]] pattern ([[maddpg]]) is shared with [[chang-2022-marl-multiuav-trajectory]] and others, but the LQR tracking layer is unique in the corpus. Blockchain integration for MEC security connects to [[blockchain-for-fl-aggregation]]. Complements [[multi-uav-assisted-mec]] trajectory design literature.

## Raw artifacts

- `raw/sources/Dynamic_Trajectory_Design_for_Multi-UAV-Assisted_Mobile_Edge_Computing/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
