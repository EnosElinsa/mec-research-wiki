---
type: concept
title: j-PPO (Joint Continuous-Discrete PPO)
tags: [drl, ppo, hybrid-action]
related:
  - "[[ppo]]"
  - "[[hybrid-action-decision-making]]"
  - "[[gae]]"
  - "[[j-ppo-en-convntm]]"
  - "[[liu-2026-jppo-en-convntm]]"
created: 2026-05-28
updated: 2026-05-28
---

# j-PPO (Joint Continuous-Discrete PPO)

A modification of [[ppo|Proximal Policy Optimization]] that supports a mixed action space — continuous actions $\mathbf{a}_n^{1:U}$ (UAV trajectories) plus discrete actions $\mathbf{1}_n$ (offloading + charging indicators) — within a single clipped objective.

The change is concentrated in the probability ratio $g_n^{\text{hybrid}}(\theta)$:

$$
g_n^{\text{hybrid}}(\theta) = c_3 \frac{\pi_\theta^{\text{cont}}(\mathbf{a}_n^{1:U}|\mathbf{h}_n)}{\pi_{\theta_{\text{old}}}^{\text{cont}}(\mathbf{a}_n^{1:U}|\mathbf{h}_n)} + (1-c_3) \frac{\pi_\theta^{\text{disc}}(\mathbf{1}_n|\mathbf{h}_n)}{\pi_{\theta_{\text{old}}}^{\text{disc}}(\mathbf{1}_n|\mathbf{h}_n)}
$$

where $c_3 \in (0,1)$ is the **hybrid weight factor** that trades off continuous vs discrete action ratios. The full objective then takes the standard PPO clip form, plus a value-function term and an entropy bonus:

$$
L_n^{\text{hybrid}+\text{VF}+\text{S}}(\theta) = \mathbb{E}_n\big[L_n^{\text{hybrid}}(\theta) - c_1 L_n^{\text{VF}}(\theta) + c_2 S[\pi_\theta](\mathbf{s}_n)\big]
$$

## Why not just use PPO?

Vanilla PPO assumes a single distribution family per action. In [[multi-uav-assisted-mec]] the UAV controller must simultaneously output positions (Gaussian) *and* binary offloading / charging flags (Bernoulli / categorical). Concatenating them under one loss without re-weighting either drowns the discrete head or destabilizes the continuous head. The hybrid ratio + clipping addresses this without splitting the actor into two independently-optimized networks.

See [[hybrid-action-beats-pure-drl]] for evidence that DDPG / TD3 (continuous-only) and DQN (discrete-only) can't reach j-PPO's $\Omega$.

## Tuning

- Best $c_3 \approx 0.5$ in the paper's regime — equal weighting kept both heads informative.
- Best $c_1 \approx 0.1$, $c_2 \approx 0.01$ — see [[finding-optimal-loss-entropy-weight-coefs]].
