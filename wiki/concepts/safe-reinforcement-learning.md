---
type: concept
title: Safe Reinforcement Learning
tags: [drl, safety, constraints]
related:
  - "[[zhang-2025-ssac-mgi-heterogeneous-uav]]"
  - "[[zhou-2021-delay-sagin-task-scheduling]]"
  - "[[collision-avoidance-mgi]]"
  - "[[compliance-aware-uav-trajectory]]"
  - "[[gong-2026-safe-economic-lae-trajectory]]"
  - "[[hsu-2022-collision-avoidance-trajectory]]"
  - "[[distributed-tabular-q-learning-uav-collision-avoidance]]"
created: 2026-05-28
updated: 2026-07-14
---

# Safe Reinforcement Learning

A family of RL formulations that enforce **constraints** (safety, fairness, resource limits) in addition to or instead of penalty terms in the reward. Soft penalties are easy but unreliable: at the optimum, the penalty is balanced against gain, so the constraint is *almost* satisfied — sometimes acceptable, sometimes catastrophic.

## Standard formulations

| Approach | Mechanism | Trade-off |
|---|---|---|
| **Reward shaping** | Add penalty term to reward | Easy; constraint violated with positive probability |
| **Constrained MDP (CMDP)** | Optimize reward subject to expected-cost constraint $\le c$ | Requires Lagrangian or primal-dual solver |
| **Shielding** | External controller intervenes when policy would violate | Hard guarantees but conservative; reduces achievable reward |
| **Gated intervention agent** | A per-agent Safety Agent overrides the task policy via a learned binary gating policy | Hard safety guarantees during *and* after training; a per-intervention cost keeps overrides selective |

## Why MEC research uses it

- **Collision avoidance** — UAVs must not crash. A reward penalty isn't sufficient; you need a guarantee.
- **Energy safety** — UAV must not deplete battery mid-flight.
- **Fairness floors** — no UE should be starved beyond a threshold.

## In this wiki

[[zhang-2025-ssac-mgi-heterogeneous-uav]] uses the **Markov Game of Intervention** ([[collision-avoidance-mgi|MGI]]) — a **per-UAV** two-agent scheme in which a stochastic, reward-maximizing **Standard Agent** is paired with a deterministic **Safety Agent** plus a binary gating policy $\mathbf{g}(s)\in\{0,1\}$ that *overrides* the Standard Agent's action whenever an intervention triggers ($\tilde a = \mathbf{g}\cdot a^{\mathrm{safe}} + (1-\mathbf{g})\cdot a$). A per-intervention cost keeps overrides selective. This enforces collision/obstacle avoidance as an explicit constraint rather than a reward penalty, giving safety guarantees during and after training.

[[zhou-2021-delay-sagin-task-scheduling]] uses a different safety pattern for SAGIN task scheduling: it keeps a separate risk Q-function for UAV energy-capacity violations and combines it with the delay-cost Q-function through an adaptive weight, so the learned scheduler searches for low delay without exceeding the energy budget.

[[hsu-2022-collision-avoidance-trajectory]] is a useful boundary case: [[distributed-tabular-q-learning-uav-collision-avoidance]] learns heading changes from local observations, but its reward penalties and simulated successes do not provide a formal collision-avoidance guarantee.

[[gong-2026-safe-economic-lae-trajectory]] uses LLM reasoning as a training-time intervention path for low-altitude trajectory safety and compliance. The final online SAC policy runs without LLM inference, but the training loop invokes LLM guidance near obstacles and constrained airspace to bias exploration toward [[compliance-aware-uav-trajectory]] behavior.
