---
type: source
title: "Joint Offloading Decision, User Association, and Resource Allocation in Hierarchical Aerial Computing: Collaboration of UAVs and HAP"
authors: ["Ahmadun Nabi", "Sangman Moh"]
year: 2025
url: "https://doi.org/10.1109/TMC.2025.3548668"
venue: "IEEE Transactions on Mobile Computing"
tags: [hierarchical-aerial-mec, hap, uav, sac, prioritized-experience-replay, matching-game, gale-shapley, jour]
related:
  - "[[hierarchical-aerial-mec]]"
  - "[[high-altitude-platform-station]]"
  - "[[matching-theory-for-resource-allocation]]"
  - "[[gale-shapley-matching]]"
  - "[[masac]]"
  - "[[prioritized-experience-replay]]"
  - "[[load-balancing-uav-mec]]"
  - "[[peng-2025-drudm-cfg]]"
  - "[[bao-2025-ddpg-video-offloading]]"
created: 2026-05-29
updated: 2026-05-29
---

# Joint Offloading Decision, User Association, and Resource Allocation in Hierarchical Aerial Computing

## Citation

Nabi, A., & Moh, S. (2025). *Joint Offloading Decision, User Association, and Resource Allocation in Hierarchical Aerial Computing: Collaboration of UAVs and HAP*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2025.3548668.

## TL;DR

A two-layer aerial MEC (UAVs + 1 HAP) with a clean **two-stage** decision split:

- **Stage 1 — discrete (matching).** Each ground user (GU) decides binary offload (local vs UAV), then GUs and UAVs are matched via a Gale-Shapley-inspired algorithm (**GOUA**: GU offloading + GU-UAV association).
- **Stage 2 — continuous (RL).** Each UAV decides a partial offloading ratio to the HAP, allocates UAV CPU to the locally-handled fraction, and the HAP allocates its CPU to the offloaded fraction. Solved by an **enhanced soft actor-critic (ESAC)** with **prioritized experience replay**.

Joint objective: minimize task energy + latency while balancing **load across UAVs** (so no UAV runs out first).

## Why this matters

This is another instance of the **discrete-then-continuous** decomposition pattern that's becoming a wiki motif: solve the integer/association part with a classical method, hand the continuous part to RL.

| Source | Discrete part | Continuous part |
|---|---|---|
| [[ma-2025-pdqn-vehicular-mec]] | P-DQN argmax | P-DQN actor (joint) |
| [[liu-2026-jppo-en-convntm]] | j-PPO discrete head | j-PPO continuous head (joint) |
| **This paper** | Gale-Shapley matching | SAC + PER (separate stages) |
| [[wang-2026-aerial-marine-msar]] | Many-to-one matching | Convex / quasi-convex (separate stages) |
| [[jia-2025-dro-uav-hap-mec]] | BWOA metaheuristic | CVX (separate stages) |

The "separate stages" choice trades joint optimality for tractability and interpretability — an important point for the wiki's **DRL-vs-classical** synthesis.

The **load-balancing** objective (penalize variance of remaining UAV energy) is a quieter contribution: it shows up as a *third* component in the reward beyond delay + energy. Useful precedent for any future paper claiming "long-lived UAV swarm".

## Method

- **Hybrid action space.** Discrete (GU offloading + GU-UAV association) handled by GOUA up front; continuous (UAV partial offloading η_u^h, UAV CPU allocation, HAP CPU allocation) handled by ESAC.
- **Reward.** Negative weighted sum of (energy, latency, UAV-load variance).
- **Why SAC + PER?** SAC's entropy regularization helps with the inherently exploratory hierarchical-aerial task; PER prioritizes high-error transitions to speed up convergence.

## Findings

- ESAC beats DDPG, MAPPO, and SAC-no-PER baselines on cumulative reward.
- The matching-based GOUA produces stable associations even under highly heterogeneous UAV capacities (no UAV is forced to take more than it can handle).
- Load-balancing variance reduction is real: max-min UAV energy gap shrinks ~30% vs greedy baselines.

## Limitations

- Single HAP. No multi-HAP coordination.
- Stage-1 association is recomputed every slot, ignoring the cost of repeated handoffs.
- GUs do not move; a moving-GU variant would change the matching frequency dramatically.
- No security or trust dimension — orthogonal to the [[mao-2025-bcsa-frl|trust]] track.

## Cross-link with related sources

- **Hierarchical aerial MEC track:** alongside [[peng-2025-drudm-cfg]] (post-disaster MEC, MASAC), [[bao-2025-ddpg-video-offloading]] (video offloading, DDPG), [[wang-2026-aerial-marine-msar]] (maritime MEC, classical). Together they form a small comparable group on the same architecture.
- **Discrete-then-continuous decomposition:** see comparison table above.
- **SAC variants:** alongside [[masac]] in [[qin-2025-bcuav-masac]] and [[zhang-2025-ssac-mgi-heterogeneous-uav]]; this is single-agent SAC, the others are multi-agent.

## Raw artifacts

- `raw/sources/Joint Offloading Decision, User Association, and Resource Allocation in Hierarchical Aerial Computin/full.md`
