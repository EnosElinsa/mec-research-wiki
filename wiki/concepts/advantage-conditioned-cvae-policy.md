---
type: concept
title: "Advantage-Conditioned CVAE Policy"
tags: [reinforcement-learning, cvae, advantage-function, continuous-control]
related:
  - "[[huang-2026-intelligent-jamming-maritime]]"
  - "[[variational-autoencoder]]"
  - "[[soft-actor-critic]]"
  - "[[pomdp]]"
  - "[[multi-objective-reinforcement-learning]]"
created: 2026-07-14
updated: 2026-07-14
---

# Advantage-Conditioned CVAE Policy

An advantage-conditioned conditional variational autoencoder learns a distribution of actions from the state together with an estimate of how much better an action is than the state's baseline value. Its latent variable can represent multiple action modes, while changing the advantage condition biases decoding toward actions of different estimated quality.

[[huang-2026-intelligent-jamming-maritime]] combines this model with [[soft-actor-critic]] for continuous UAV trajectory and power control. Training conditions the CVAE on state plus normalized advantage; policy optimization decodes at a fixed maximum-advantage condition while lower-advantage samples still supervise their corresponding conditional distributions.

The method depends on the accuracy and calibration of learned Q and value estimates. The supporting source fixes the maximum normalized condition to one and provides simulation evidence only; it does not establish that decoded actions are globally optimal, feasible under unseen dynamics, or consistently superior when the advantage estimator is biased.
