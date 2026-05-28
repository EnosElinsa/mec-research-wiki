---
type: source
title: "Computation Offloading and Resource Allocation in Vehicular MEC: A Parameterized Deep Reinforcement Learning Approach"
authors: ["Ruofei Ma", "Jingyang Zhou", "Ruisong Wang", "Hsiao-Hwa Chen", "Gongliang Liu"]
year: 2025
url: "https://doi.org/10.1109/TVT.2025.3574783"
venue: "IEEE Transactions on Vehicular Technology"
tags: [vehicular-mec, iov, drl, p-dqn, parameterized-dqn, hybrid-action, three-tier-offloading]
related:
  - "[[vehicular-mec]]"
  - "[[parameterized-dqn]]"
  - "[[hybrid-action-decision-making]]"
  - "[[three-tier-cloud-edge-end]]"
  - "[[ddqn]]"
  - "[[binary-vs-partial-offloading]]"
  - "[[zhang-2025-mcma-task-migration]]"
created: 2026-05-29
updated: 2026-05-29
---

# Computation Offloading and Resource Allocation in Vehicular MEC: A Parameterized Deep Reinforcement Learning Approach

## Citation

Ma, R., Zhou, J., Wang, R., Chen, H.-H., & Liu, G. (2025). *Computation Offloading and Resource Allocation in Vehicular MEC: A Parameterized Deep Reinforcement Learning Approach*. **IEEE Transactions on Vehicular Technology**. DOI: 10.1109/TVT.2025.3574783.

## TL;DR

Joint binary-offloading + transmit-power-allocation problem in a **three-tier vehicular MEC** (local vehicle → RSU-MEC → cloud). Vehicles pick one of M+2 destinations (local, M MEC servers, cloud) — a **discrete** decision — and a continuous transmit power per task. Existing DRL approaches either discretize the continuous action (loss of accuracy) or relax the discrete one (loss of integrality). This paper applies **Parameterized DQN (P-DQN)**, which natively handles a hybrid action space by jointly learning a discrete-action Q-function and a continuous-action actor parametrized per discrete option.

Optimization target: weighted long-term sum of latency, energy, and monetary cost.

## Why this matters

It's the wiki's first **P-DQN** entry. P-DQN sits in a different corner of the hybrid-action design space than [[liu-2026-jppo-en-convntm|j-PPO]]:

| Aspect | j-PPO ([[liu-2026-jppo-en-convntm]]) | P-DQN (this paper) |
|---|---|---|
| Backbone | PPO (on-policy, stochastic policy) | DQN (off-policy, value-based) |
| Discrete action | Sampled from softmax | argmax over Q |
| Continuous action | Sampled from Gaussian | Deterministic actor head per discrete option |
| Sample efficiency | Lower | Higher (replay buffer) |
| Stability | Higher (clipping) | Lower (Q-overestimation risk) |

This is now the second wiki source that picks **DQN-family** for hybrid actions, after [[liu-2026-jppo-en-convntm]]'s ablation comparison. Worth a synthesis page when a third arrives.

## System model

- **Network.** N vehicles on a road segmented into M sub-segments, each covered by an RSU+MEC. RSUs interconnect via wired backhaul; cloud reachable through any RSU.
- **Mobility.** Truncated Gaussian speed; vehicle handoff between RSUs is modeled.
- **Channels.** V2I Rayleigh fading + slow log-normal shadowing.
- **Tasks.** Per slot, each vehicle generates one task (input size, computation intensity, deadline).
- **Action.** a_i(t) ∈ {0, 1, ..., M+1} — local, RSU m, or cloud — paired with continuous transmit power p_i(t).

## Findings

- P-DQN beats DQN, DDPG, and convex-optimization baselines on cumulative reward.
- The **handoff cost** (extra inter-RSU transmission when a vehicle leaves its source RSU before result delivery) is non-trivial. The reward function captures it explicitly.

## Limitations

- Single-agent assumption — each vehicle independently optimizes. Multi-vehicle interference and competition for RSU compute are baked into the reward but not into the action space.
- No federated or privacy-preserving variant.
- Reliability/security ignored, so it doesn't compete in the [[mao-2025-bcsa-frl|trust]] track.

## Cross-link with related sources

- **Vehicular-MEC track:** alongside [[zhang-2025-mcma-task-migration]] (task migration with Informer prediction) and [[xie-2026-uav-multisource-fusion]] (UAV-fusion for V2X perception).
- **Hybrid-action DRL:** alongside [[liu-2026-jppo-en-convntm]] — together they motivate a `j-ppo-vs-pdqn` comparison page once a deciding factor (memory, mobility, etc.) becomes clear.
- **Three-tier cloud-edge-end:** introduces this architectural pattern to the wiki; future ground-MEC papers will likely revisit it.

## Raw artifacts

- `raw/sources/Computation Offloading and Resource Allocation in Vehicular MEC A Parameterized Deep Reinforcement/full.md`
