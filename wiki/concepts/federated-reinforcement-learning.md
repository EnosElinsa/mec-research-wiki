---
type: concept
title: Federated Reinforcement Learning (FRL)
tags: [drl, federated-learning, distributed]
related:
  - "[[ddqn]]"
  - "[[blockchain-for-fl-aggregation]]"
  - "[[fl-poisoning-attacks]]"
  - "[[mao-2025-bcsa-frl]]"
created: 2026-05-28
updated: 2026-05-28
---

# Federated Reinforcement Learning (FRL)

A federated extension of reinforcement learning: distributed RL agents train local policies on private experience, then periodically share *model parameters* (not raw transitions) to be aggregated into a global model. The participants then sync their local nets from the global model and continue training.

## Why combine FL with DRL

- Privacy — raw replay buffers may contain sensitive sensor data; only model parameters leave the device.
- Spectrum / bandwidth efficiency — model deltas are far smaller than streamed experience.
- Robustness — the aggregated global model integrates evidence from diverse environments, reducing per-device overfitting.

## Common DRL backbones

- DQN / [[ddqn|Double DQN]] — for discrete actions (offloading destination choice, charging on/off).
- PPO / [[j-ppo]] — for continuous or hybrid actions.

## Aggregation

The classical recipe is FedAvg ([37] in [[mao-2025-bcsa-frl]]'s reference list — McMahan et al. 2017): weighted average of participant model parameters. This implicitly trusts every participant. Practical extensions:

- **Reputation-weighted aggregation** — weights scaled by historical contribution quality.
- **Decentralized aggregation** — no central server; consensus reached via [[blockchain-for-fl-aggregation]].
- **Cold-start aggregation** — sharply down-weight recently-attacked participants and gradually recover them. See [[csra-cold-start-reputation-aggregation]].

## Threat model

FRL inherits FL's attack surface (see [[fl-poisoning-attacks]]) and adds RL-specific concerns:

- **Replay buffer poisoning** — the participant is honest but its experience source is corrupted.
- **Reward shaping attacks** — adversarial environments produce misleading reward signals.

These are not always distinguishable from honest model drift, so reputation systems need both detection *and* graceful recovery.
