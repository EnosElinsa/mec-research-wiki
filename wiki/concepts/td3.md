---
type: concept
title: "TD3 (Twin Delayed DDPG)"
tags: [drl, actor-critic, continuous-action, off-policy]
related:
  - "[[ddpg]]"
  - "[[masac]]"
  - "[[multi-agent-td3]]"
  - "[[hao-2024-clp-multiuav-priority-offloading]]"
  - "[[ye-2026-meta-deepesc-lae-isac]]"
  - "[[cai-2026-llm-drl-secure-lae-data]]"
  - "[[hu-2026-ertatd3-secure-caching]]"
  - "[[ren-2026-security-aware-vec-td3]]"
created: 2026-05-29
updated: 2026-07-07
---

# TD3 (Twin Delayed DDPG)

Twin Delayed Deep Deterministic Policy Gradient — the standard hardened successor to [[ddpg]] for continuous control. It addresses DDPG's Q-overestimation and brittleness with three tricks:

- **Clipped double Q-learning** — two critics, and the TD target uses the *minimum* of the two to curb overestimation.
- **Delayed policy updates** — the actor (and targets) update less frequently than the critics, stabilizing learning.
- **Target policy smoothing** — clipped Gaussian noise added to the target action regularizes the value estimate.

In the wiki, [[hao-2024-clp-multiuav-priority-offloading]]'s CLP algorithm builds on TD3, learning over a [[hybrid-action-representation]] latent space. [[ye-2026-meta-deepesc-lae-isac]] uses TD3 as the base learner for energy-efficient LAE ISAC beamforming and UAV-trajectory control, then adds [[meta-deep-reinforcement-learning]] for faster flight-period adaptation. [[cai-2026-llm-drl-secure-lae-data]] evaluates TD3 with LLM-generated state/reward/simulation support for secure LAE data collection. [[hu-2026-ertatd3-secure-caching]] extends the TD3 line with twin actor networks and enhanced reward design for secure cache-enabled UAV-assisted vehicular MEC, while [[ren-2026-security-aware-vec-td3]] uses TD3 for UAV movement, association, and secure offloading under a passive eavesdropper. The multi-agent extension [[multi-agent-td3]] (MATD3) is used in [[shao-2024-drl-antijamming-mec]]. TD3 is the deterministic counterpart to the stochastic, entropy-regularized [[masac|SAC]] family.
