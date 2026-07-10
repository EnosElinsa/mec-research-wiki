---
type: concept
title: "Soft Actor-Critic (SAC)"
tags: [drl, actor-critic, off-policy, maximum-entropy, continuous-action]
related:
  - "[[masac]]"
  - "[[ddpg]]"
  - "[[td3]]"
  - "[[ppo]]"
  - "[[xiang-sac-mapless-robot-navigation]]"
  - "[[du-2024-d2sac-aigc-asp-selection]]"
  - "[[chen-2025-swipt-mec-sac]]"
  - "[[wen-2026-hybridrag-low-carbon-lae]]"
  - "[[chen-2026-qos-noma-multiuav]]"
  - "[[gong-2026-safe-economic-lae-trajectory]]"
  - "[[li-2026-aerial-ris-trajectory-phase]]"
  - "[[bai-2026-aoi-uav-isac]]"
created: 2026-05-31
updated: 2026-07-10
---

# Soft Actor-Critic (SAC)

An off-policy, **maximum-entropy** actor-critic algorithm for (originally continuous) control. It augments the standard reward objective with a policy-entropy bonus

$$
J(\pi) = \mathbb{E}\Big[\textstyle\sum_t \gamma^t\big(r(s_t,a_t,s_{t+1}) + \alpha\,H(\pi(\cdot|s_t))\big)\Big]
$$

so the optimal policy maximizes return **and** stays as stochastic as possible at each state, which improves exploration and robustness. SAC combines off-policy learning, an actor-critic structure, and maximum entropy; it uses **twin Q-networks** (clipped double-Q to curb overestimation), a replay buffer, soft target updates (Polyak averaging $\rho$), and — through the inherent policy stochasticity — benefits from something like target-policy smoothing. The temperature $\alpha$ trades off reward vs entropy and can be auto-tuned.

## Relationship to other backbones

- Bridges stochastic-policy optimization and **[[ddpg|DDPG]]**-style deterministic methods; shares the clipped double-Q trick with **[[td3|TD3]]**.
- More exploration-stable than DDPG/TD3 on many tasks; off-policy + replay makes it more sample-efficient than on-policy **[[ppo|PPO]]**.
- Its multi-agent extension is **[[masac|MASAC]]** (decentralized actors + centralized critic).

## In this wiki

[[wen-2026-hybridrag-low-carbon-lae]] uses double-regularized diffusion-enhanced SAC for low-carbon LAE MEC control.

[[xiang-sac-mapless-robot-navigation]] uses single-agent SAC (with LSTM value/Q networks) for mapless robot navigation — a foundational continuous-control grounding for the SAC vocabulary. [[du-2024-d2sac-aigc-asp-selection]] hosts a diffusion-policy actor inside SAC (D2SAC) for discrete ASP selection. [[chen-2025-swipt-mec-sac]] uses an improved SAC (SAC-SK) for SWIPT-MEC. [[chen-2026-qos-noma-multiuav]] improves SAC with a perturbation term in the loss for constrained NOMA multi-UAV task offloading, and [[gong-2026-safe-economic-lae-trajectory]] uses SAC as the online policy after LLM-guided safety/compliance training. [[li-2026-aerial-ris-trajectory-phase]] combines SAC with [[prioritized-experience-replay]] for tilt-aware aerial RIS control, while [[bai-2026-aoi-uav-isac]] uses SAC to choose UAV motion and beam-activation priorities for AoI-centric UAV-ISAC. The cooperative-MEC multi-agent variant appears in [[qin-2025-bcuav-masac]] and [[you-2025-uncertain-maritime-hasac]] (see [[masac]]).
