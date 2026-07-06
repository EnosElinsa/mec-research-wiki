---
type: concept
title: "Model-Based Multi-Agent Reinforcement Learning"
tags: [drl, marl, model-based, sample-efficiency]
related:
  - "[[ppo]]"
  - "[[communication-constrained-marl]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[wu-2026-model-based-ppo-ris-uav-mec]]"
created: 2026-07-07
updated: 2026-07-07
---

# Model-Based Multi-Agent Reinforcement Learning

Multi-agent reinforcement learning in which agents learn an explicit or implicit transition model and use it to generate additional rollouts, improve value estimates, or anticipate other agents' effects. The motivation is sample efficiency: real environment interactions can be expensive, slow, or hard to reproduce, especially in aerial networks with coupled mobility, interference, and offloading states.

In [[wu-2026-model-based-ppo-ris-uav-mec]], each UAV learns a local dynamics model and uses short-horizon branched rollouts inside [[ppo]] updates. The method stays decentralized by using local plus k-hop neighborhood observations rather than a global critic, connecting it to [[communication-constrained-marl]] while contrasting with [[centralized-training-decentralized-execution]] methods that depend on full-state critics during training.

The tradeoff is model bias: learned rollouts can stabilize and enrich training, but errors compound with rollout horizon and can mislead policy gradients if uncertainty is not handled.
