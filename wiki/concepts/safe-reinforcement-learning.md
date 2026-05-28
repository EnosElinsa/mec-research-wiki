---
type: concept
title: Safe Reinforcement Learning
tags: [drl, safety, constraints]
related:
  - "[[zhang-2025-ssac-mgi-heterogeneous-uav]]"
  - "[[collision-avoidance-mgi]]"
created: 2026-05-28
updated: 2026-05-28
---

# Safe Reinforcement Learning

A family of RL formulations that enforce **constraints** (safety, fairness, resource limits) in addition to or instead of penalty terms in the reward. Soft penalties are easy but unreliable: at the optimum, the penalty is balanced against gain, so the constraint is *almost* satisfied — sometimes acceptable, sometimes catastrophic.

## Standard formulations

| Approach | Mechanism | Trade-off |
|---|---|---|
| **Reward shaping** | Add penalty term to reward | Easy; constraint violated with positive probability |
| **Constrained MDP (CMDP)** | Optimize reward subject to expected-cost constraint $\le c$ | Requires Lagrangian or primal-dual solver |
| **Shielding** | External controller intervenes when policy would violate | Hard guarantees but conservative; reduces achievable reward |
| **Game-theoretic intervention** | One agent designated as constraint-enforcer in a sub-game | Asymmetric — can break symmetry that confuses cooperative agents |

## Why MEC research uses it

- **Collision avoidance** — UAVs must not crash. A reward penalty isn't sufficient; you need a guarantee.
- **Energy safety** — UAV must not deplete battery mid-flight.
- **Fairness floors** — no UE should be starved beyond a threshold.

## In this wiki

[[zhang-2025-ssac-mgi-heterogeneous-uav]] uses the **Markov Game of Intervention** ([[collision-avoidance-mgi|MGI]]) — a game-theoretic intervention scheme that asymmetrically assigns one UAV as the deflector when two UAVs threaten collision. This avoids the symmetric-swerve failure mode of pure cooperative deflection.
