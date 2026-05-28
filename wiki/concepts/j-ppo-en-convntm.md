---
type: concept
title: j-PPO+EN-ConvNTM Framework
tags: [drl, framework, uav, mec]
related:
  - "[[liu-2026-jppo-en-convntm]]"
  - "[[j-ppo]]"
  - "[[en-convntm]]"
  - "[[stn]]"
  - "[[ppo]]"
  - "[[pomdp]]"
  - "[[hybrid-action-decision-making]]"
created: 2026-05-28
updated: 2026-05-28
---

# j-PPO+EN-ConvNTM Framework

The end-to-end DRL pipeline introduced in [[liu-2026-jppo-en-convntm]] for [[multi-uav-assisted-mec]] under [[high-density-mobile-device-scenarios]]. Two cooperating modules:

```
o_n  →  STN  →  EN-ConvNTM  →  h_n  →  j-PPO  →  (a_n^{1:U},  1_n)
                (3-D memory)         (hybrid clip + VF + entropy)
```

- **[[en-convntm]]** turns a sequence of 3-channel observation grids into a context-rich representation $\mathbf{h}_n$ via a [[stn]] front-end and an attention-augmented [[ntm|NTM]] memory.
- **[[j-ppo]]** maps $\mathbf{h}_n$ to two action heads: a continuous head for UAV trajectory $\mathbf{a}_n^{1:U}$ and a discrete head for the offloading + charging indicator $\mathbf{1}_n$. Both share the [[gae|GAE]]-driven value function.

## Why the combination

- Pure [[ppo]] gives stable on-policy updates but struggles when actions span continuous *and* discrete spaces — addressed by the hybrid clipped objective.
- Pure ConvLSTM / NeuralMap retains spatial structure but loses long-horizon temporal context or compresses identities — addressed by the NTM-style external memory and the STN's spatial-attention front-end.

See [[en-convntm-beats-baselines]] for the empirical justification.

## Training loop (Algorithm 1, paraphrased)

1. Run $\tilde{N}$ parallel episodes, $N$ steps each, with policy $\pi_{\theta_{\text{old}}}$.
2. At each step: encode $\mathbf{o}_n$ with EN-ConvNTM, sample hybrid action, step env, log reward.
3. Compute [[gae|GAE]] advantages over the trajectory.
4. Slice the trajectory into segments of length $K$ to break the sequential-correlation problem the NTM creates.
5. Optimize the hybrid PPO loss for $K$ epochs with mini-batch size $M$.
6. Set $\theta_{\text{old}} \leftarrow \theta$, repeat.

## Hyperparameter sweet spot (empirical)

From Table I of [[liu-2026-jppo-en-convntm]]:

- VF loss coefficient $c_1 = 0.1$
- Entropy coefficient $c_2 = 0.01$
- Hybrid-ratio weight $c_3 = 0.5$ (balances continuous vs discrete contributions)

See [[finding-optimal-loss-entropy-weight-coefs]].
