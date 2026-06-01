---
type: comparison
title: "j-PPO vs P-DQN for hybrid-action MEC"
tags: [drl, comparison, action-space, hybrid-action]
related:
  - "[[j-ppo]]"
  - "[[parameterized-dqn]]"
  - "[[hybrid-action-decision-making]]"
  - "[[liu-2026-jppo-en-convntm]]"
  - "[[ma-2025-pdqn-vehicular-mec]]"
  - "[[ddpg-vs-jppo]]"
  - "[[drl-backbones-across-uav-mec-sources]]"
created: 2026-06-02
updated: 2026-06-02
---

# j-PPO vs P-DQN for hybrid-action MEC

The corpus has two sources that take the **native hybrid-action** route — a single policy network that emits a discrete decision *and* its continuous parameters jointly, without discretizing the continuous part or relaxing the discrete part. They land in opposite corners of the DRL design space: [[liu-2026-jppo-en-convntm]]'s [[j-ppo|j-PPO]] is an on-policy modified-PPO learner, and [[ma-2025-pdqn-vehicular-mec]]'s [[parameterized-dqn|P-DQN]] is an off-policy value-based learner. This page is the head-to-head that [[drl-backbones-across-uav-mec-sources]] flagged as missing and [[ddpg-vs-jppo]]'s P-DQN caveat implied. Both papers solve a different MEC problem, so this is a **method-shape** comparison, not a benchmark on a shared instance.

## Where each comes from

- **j-PPO** — [[liu-2026-jppo-en-convntm]], a high-density multi-UAV-MEC controller. The joint action couples a continuous part (trajectory, power, offloading ratios) with discrete parts (charging on/off, quantized choices); j-PPO modifies the PPO probability ratio so a single clipped-surrogate update covers both heads. The paper reports its full stack (j-PPO + EN-ConvNTM memory) beating DDPG/TD3/A2C/DQN, attributing those baselines' "severe performance degradation" to their inability to represent the joint continuous-discrete action (see [[hybrid-action-beats-pure-drl]]).
- **P-DQN** — [[ma-2025-pdqn-vehicular-mec]], a three-tier vehicular MEC offloading problem. Each vehicle picks one of M+2 destinations (local / M edge servers / cloud) — discrete — paired with a continuous transmit power. P-DQN learns a discrete-action Q-function plus a continuous-action actor parameterized per discrete option, so the hybrid action is handled natively. The parse states the scheme "secures a higher reward in comparison to the baseline algorithms".

## The structural contrast

| Aspect | j-PPO ([[liu-2026-jppo-en-convntm]]) | P-DQN ([[ma-2025-pdqn-vehicular-mec]]) |
|---|---|---|
| Base algorithm | PPO (policy-gradient, on-policy) | DQN + deterministic continuous actor (value-based, off-policy) |
| Discrete action | Sampled from a categorical/Bernoulli head | argmax over the Q-function |
| Continuous action | Sampled from a Gaussian (stochastic) | Deterministic actor head, one per discrete option |
| Exploration | Stochastic policy + entropy | ε-greedy on discrete + actor noise on continuous |
| Data usage | On-policy rollouts, discarded after update | Replay buffer (higher sample efficiency) |
| Stability lever | Clipped trust region bounds the update | Target networks; carries Q-overestimation risk |
| Continuous heads | One shared head | **One actor head per discrete action** (scales with the discrete-action count) |
| Demonstrated regime | Many UAVs, high-density mobility, long horizon | Per-vehicle decision, M+2 destinations |

## How to read the tradeoff

The split is the classic **on-policy stochastic vs off-policy value-based** one, specialized to hybrid actions:

- **Sample efficiency.** P-DQN's replay buffer reuses experience, which matters when environment interaction is expensive. j-PPO discards rollouts after each update, so it typically needs more samples — but on-policy data avoids the distribution-shift staleness that off-policy replay can suffer.
- **Stability vs overestimation.** j-PPO's clipped surrogate bounds each update, which is why the high-density, long-horizon UAV setting reaches for it (paired with external memory). P-DQN inherits DQN's Q-overestimation risk, but the per-vehicle vehicular problem is lower-dimensional and shorter-horizon, so that risk is easier to control.
- **How the continuous part is produced.** j-PPO samples it from a Gaussian (good for exploration over a coupled continuous vector); P-DQN produces it deterministically from a per-discrete-action actor head. The per-option head is clean when the discrete set is small and fixed (M+2 destinations) but multiplies parameters as the discrete action count grows — a reason the many-UAV joint-action setting did not take this route.
- **Discrete-action scale.** P-DQN's per-option actor architecture fits a modest, enumerable destination set; j-PPO's single stochastic policy is the more natural fit when the discrete component is itself high-dimensional or entangled with the continuous one.

## Which to reach for

Distilled from the two sources' problem shapes, not from a shared benchmark:

- **Lean P-DQN** when the discrete choice is a small, fixed menu (a destination among a handful), interaction is expensive enough that replay-buffer reuse pays off, and the horizon is short — the vehicular-offloading profile.
- **Lean j-PPO** when the action is a high-dimensional continuous vector entangled with several discrete switches, the horizon is long enough that on-policy stability and external memory matter, and the system is multi-agent / high-density — the UAV-swarm profile.

## Caveat

No curated source runs both on the **same** MEC instance, so the choice is currently a problem-shape decision rather than an empirical preference — the same open-comparison status that [[ddpg-vs-jppo]] notes for vanilla DDPG. A controlled study placing j-PPO and P-DQN on one hybrid-action MEC environment (matched state/reward, swept agent count and horizon) would turn this structural contrast into a measured one. Both belong to the **native-hybrid-policy** cell of the hybrid-action design space mapped in [[drl-backbones-across-uav-mec-sources]]; the latent-space-encoding and stage-separated cells are the alternatives they are implicitly chosen over.
