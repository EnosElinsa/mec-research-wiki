---
type: source
title: "Computation Offloading and Resource Allocation in Vehicular MEC: A Parameterized Deep Reinforcement Learning Approach"
authors: ["Ruofei Ma", "Jingyang Zhou", "Ruisong Wang", "Hsiao-Hwa Chen", "Gongliang Liu"]
year: 2025
url: "https://doi.org/10.1109/TVT.2025.3574783"
venue: "IEEE Transactions on Vehicular Technology"
tags: [source, vehicular-mec, iov, drl, p-dqn, parameterized-dqn, hybrid-action, three-tier-offloading]
related:
  - "[[vehicular-mec]]"
  - "[[parameterized-dqn]]"
  - "[[hybrid-action-decision-making]]"
  - "[[three-tier-cloud-edge-end]]"
  - "[[ddqn]]"
  - "[[binary-vs-partial-offloading]]"
  - "[[zhang-2025-mcma-task-migration]]"
  - "[[j-ppo-vs-pdqn]]"
created: 2026-05-29
updated: 2026-11-03
modeling_card: required
---

# Computation Offloading and Resource Allocation in Vehicular MEC: A Parameterized Deep Reinforcement Learning Approach

## Citation

Ma, R., Zhou, J., Wang, R., Chen, H.-H., & Liu, G. (2025). *Computation Offloading and Resource Allocation in Vehicular MEC: A Parameterized Deep Reinforcement Learning Approach*. **IEEE Transactions on Vehicular Technology**. DOI: 10.1109/TVT.2025.3574783.

## TL;DR

Joint binary-offloading + transmit-power-allocation problem in a **three-tier vehicular MEC** (local vehicle → RSU-MEC → cloud). Vehicles pick one of M+2 destinations (local, M MEC servers, cloud) — a **discrete** decision — and a continuous transmit power per task. Existing DRL approaches either discretize the continuous action (loss of accuracy) or relax the discrete one (loss of integrality). This paper applies **Parameterized DQN (P-DQN)**, which natively handles a hybrid action space by jointly learning a discrete-action Q-function and a continuous-action actor parametrized per discrete option.

Optimization target: weighted long-term sum of latency, energy, and monetary cost.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Vehicles in a road network choose local execution, one of $M$ RSU-MEC servers, or a cloud server for each task. V2I links use Rayleigh fading, RSUs are connected by wired links, and each task has input size, computation demand, and a delay tolerance shortened when the vehicle is about to leave all RSU coverage.

**Problem & objective**: Problem (21) maximizes the long-term average utility, $J=\max_{\mathcal A,\mathcal F,\mathcal P}\frac1T\sum_t\sum_iU_i(t)$, where (20) gives $U_i=w_1\frac{T_{\max}-T_i}{T_{\max}}+w_2\frac{E_{\max}-E_i}{E_{\max}}-w_3\frac{\epsilon_i}{\epsilon_{\max}}$, so higher utility means lower normalized delay, energy, and monetary cost.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Offloading decision | $a_i(t)$ | discrete, $\{0,1,\ldots,M+1\}$ | Local execution, one RSU-MEC server, or the cloud |
| Execution indicators | $s_i^l(t),s_i^E(t),s_i^c(t)$ | binary | Local, MEC, or cloud execution of vehicle $i$'s task |
| Computation allocation | $f_{i,m}^E(t),f_i^c(t)$ in $\mathcal F$ | continuous, bounded | MEC-server and cloud CPU resources for vehicle $i$ |
| Transmit power | $p_i(t)$ in $\mathcal P$ | continuous, $[P_{\min},P_{\max}]$ | Uplink power of vehicle $i$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| 21a-21b | Exactly one of local, MEC, or cloud execution is chosen, with binary indicators |
| 21c | Offloading decision $a_i(t)\in\{0,1,\ldots,M+1\}$ |
| 21d | Task delay satisfies $T_i(t)\le T_i^{\max}(t)=\min\{t_i^{\mathrm{finish}},t_i^{\mathrm{link}}\}$ |
| 21e | Each MEC server's allocations stay within its capacity $F$ |
| 21f | Cloud allocation per vehicle stays within $F^c$ |
| 21g | Transmit power lies in $[P_{\min},P_{\max}]$ |

**Algorithm**: Treat each discrete offloading choice as an action with continuous resource and power parameters → a parameter actor outputs the continuous parameters for every discrete option → a Q-network evaluates each option and its parameters → train with replay, target networks, and multi-step returns.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Ma et al. [x] studied computation offloading and resource allocation in a three-tier vehicular MEC network with local vehicles, RSU-MEC servers, and a cloud. They formulated a hybrid discrete-continuous problem that maximizes long-term average utility, which rewards lower normalized delay, energy, and monetary cost, by selecting an execution destination, computation resources, and transmit power for each task. They proposed Parameterized DQN, which learns a discrete Q-function and a continuous actor parameterized by each candidate destination. The action design preserves destination integrality without discretizing resource and power parameters, and each task's delay tolerance is shortened when the vehicle is about to leave all RSU coverage. Simulations report higher cumulative reward than DDQN, DDPG, and AllCloud baselines in the evaluated vehicular settings.

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
- **Hybrid-action DRL:** alongside [[liu-2026-jppo-en-convntm]] — together they motivate the [[j-ppo-vs-pdqn]] comparison, which contrasts P-DQN's off-policy value-based handling with j-PPO's on-policy stochastic one.
- **Three-tier cloud-edge-end:** introduces this architectural pattern to the wiki; future ground-MEC papers will likely revisit it.

## Raw artifacts

- `raw/sources/Computation Offloading and Resource Allocation in Vehicular MEC A Parameterized Deep Reinforcement/Computation Offloading and Resource Allocation in Vehicular MEC A Parameterized Deep Reinforcement.md`
