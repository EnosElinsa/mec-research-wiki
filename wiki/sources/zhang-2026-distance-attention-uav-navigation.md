---
type: source
modeling_card: required
title: "Distance-Attention Augmented Reinforcement Learning: A Robust Approach for 3D Cooperative UAV Navigation in Dense Urban Environments"
authors: ["Lijuan Zhang", "Hang Lin", "Shihong Zhao", "Fei Wang", "Chao Yan", "Pan Gao"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3668827"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, multi-uav, cooperative-navigation, distance-attention, ctde, pomdp, collision-avoidance, trajectory-control]
related:
  - "[[distance-attention-uav-navigation]]"
  - "[[ma-pomdp]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[maddpg]]"
  - "[[autonomous-uav-swarms]]"
  - "[[uav-trajectory-control]]"
created: 2026-07-13
updated: 2026-07-16
---

# Distance-Attention Augmented Reinforcement Learning: A Robust Approach for 3D Cooperative UAV Navigation in Dense Urban Environments

## Citation

Zhang, L., Lin, H., Zhao, S., Wang, F., Yan, C., & Gao, P. (2026). *Distance-Attention Augmented Reinforcement Learning: A Robust Approach for 3D Cooperative UAV Navigation in Dense Urban Environments*. **IEEE Transactions on Mobile Computing**, 25(8), 11520-11536. DOI: 10.1109/TMC.2026.3668827.

## TL;DR

Extends a MADDPG-style CTDE controller for continuous 3-D cooperative navigation with vertical-layer LiDAR attention, historical observation queues, and a critic that fuses current joint features with global history. Five dense reward terms trade route efficiency against obstacle/UAV collision avoidance and communication connectivity.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Multiple UAVs use three-layer, 16-direction LiDAR and nearby-UAV messages to navigate from arbitrary starts to a target area through dense three-dimensional urban obstacles. Each agent acts from partial observations while a centralized critic uses joint and historical information during training.

**Problem & objective**: The cooperative POMDP learns policies that maximize discounted return, $\max_{\pi}\mathbb E_{\pi}[\sum_t\gamma^t\mathcal R_i(t)]$, where the reward combines target progress, obstacle and inter-UAV safety, communication connectivity, and travel time.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Horizontal acceleration | $a^i$ | continuous, normalized to $[-1,1]$ | Change in forward speed of UAV $i$ |
| Yaw rate | $\phi^i$ | continuous, normalized to $[-1,1]$ | Horizontal turning control |
| Vertical acceleration | $\kappa^i$ | continuous, normalized to $[-1,1]$ | Climb or descent acceleration |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | The normalized control vector satisfies $\mathbf u_{\mathrm{norm}}^i\in[-1,1]^3$. |
| C2 | Obstacle proximity is penalized through $r_2^i=\sigma(d^i/D_r-1)$ using the minimum LiDAR range. |
| C3 | Inter-UAV separation below $d_{\mathrm{nei}}$ activates the collision penalty $r_3^i$. |
| C4 | Losing all neighbors beyond communication range $r_{\mathrm{com}}$ activates the connectivity penalty $r_4^i$. |
| C5 | Target deviation beyond $D_0$ and each additional movement step are penalized. |

**Algorithm**: Maintain historical observation queues, weight vertical LiDAR layers in the distance-attention actor, fuse current joint state-action features with global history in the critic, collect replay transitions under CTDE, and update deterministic actors, critics, and target networks off policy.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zhang et al. [x] studied cooperative three-dimensional UAV navigation through dense urban environments as a partially observable multi-agent control problem. They defined continuous horizontal-acceleration, yaw-rate, and vertical-acceleration actions and a non-sparse reward that combines target approach, obstacle avoidance, inter-UAV collision avoidance, connectivity maintenance, and a time-step cost. Their DA2RL method couples a distance-attention actor for layered LiDAR observations with a historical-feature-flow critic and trains the policies with historical queues and centralized action-value information. Across 200 random tests in the training environment, the reported results include a 94.6% success rate, 5.17% collision rate, 0.908 velocity consistency, and 985.3 m average path length, with convergence within about 400 episodes.

## Problem

Multi-UAV navigation in dense urban space combines partial observation, three-dimensional motion, narrow passages, dynamic obstacles, inter-UAV safety, and limited A2A range. Flat LiDAR features and memoryless critics can miss which vertical obstacle layer matters or how recent swarm motion affects the current action value.

## System model

- UAVs travel from arbitrary ground starts to a common target region among buildings and simulated dynamic obstacles.
- Each UAV senses 16 horizontal directions at three vertical LiDAR orientations (`-10`, `0`, and `+10` degrees).
- State evolution tracks 3-D position, yaw, forward speed, and vertical speed. Continuous actions are horizontal acceleration, yaw rate, and vertical acceleration.
- The [[ma-pomdp|multi-agent POMDP]] observation combines obstacle ranges, internal motion state, distances to the two nearest UAVs, and relative horizontal/vertical target distance and angles.
- Neighbor distances come from echo or ADS-B exchange and are capped by A2A communication range.

## Method

[[distance-attention-uav-navigation]] reshapes the three LiDAR layers, projects each layer, combines them with the preceding LSTM hidden state, and applies Softmax weights across vertical layers. The actor concatenates this attended obstacle representation with motion, neighbor, and target features to output normalized continuous controls.

The historical-feature-flow critic has one branch for current global observation-action features and a second FC/LSTM branch for prior global observations. Their concatenation estimates each UAV's Q-value under [[centralized-training-decentralized-execution|CTDE]]. Training is off-policy deterministic actor-critic with replay, target networks, and soft updates. Reward sums target approach, continuous obstacle-distance penalty, inter-UAV collision penalty, connectivity penalty, and a per-step cost; safety remains reward-shaped rather than a hard constraint or shield.

## Key findings

- The reported learning curves show MADDPG stabilizing after about 1,750 episodes, while recurrent MARDPG and DA2RL converge within 400 episodes.
- Across 200 random tests, DA2RL records `94.6%` success, `5.17%` collision, `0.23%` timeout, `0.908` velocity consistency, and `985.3 m` mean path length.
- At four times the training area, DA2RL retains `78.6%` success. With 12 UAVs after training on three, it reaches `79.6%` success and `20.35%` collision, versus `47.7%` and `52.27%` for MADDPG.
- Among the 3-D methods, total modeled energy is `148.16 kJ`, compared with `150.36 kJ` for MADDPG and `217.34 kJ` for MARDPG. The 2-D RL-CN baseline is lower at `137.01 kJ` because it does not adjust altitude.
- Target-only reward yields `58.1%` success and `41.81%` collision; all five reward terms yield `94.6%` and `5.17%`, while increasing path length relative to the no-connectivity ablation.

## Limitations / parse caveats

Training and evaluation are simulation-only, with idealized fixed-ray LiDAR, three training UAVs, cylindrical obstacles, a fixed 150 m communication threshold, and periodically repositioned obstacles rather than a physical motion model. The two-nearest-neighbor observation degrades as swarm size rises. Safety and connectivity are reward penalties, so they are not guaranteed constraints. RL-CN is a structurally different 2-D baseline. No communication delay, packet loss, heterogeneous fleet, or physical flight test is evaluated. Some figure labels and energy constants are OCR-corrupted; table values and explicit prose are retained. Publication metadata is absent from the parse and was verified through the exact-title Crossref record.

## Relation to the corpus

The source adds history-conditioned vertical-range attention to [[uav-trajectory-control]] and [[autonomous-uav-swarms]]. It is a reward-only safety contrast to [[zhang-2025-ssac-mgi-heterogeneous-uav]], whose intervention/gating mechanism modifies unsafe actions, and a point-to-point navigation counterpart to the attention-based target-search controller in [[zhu-2026-hab-mappo-target-search]].

## Raw artifacts

- Parse: `raw/sources/Distance-Attention_Augmented_Reinforcement_Learning_A_Robust_Approach_for_3D_Cooperative_UAV_Navigation_in_Dense_Urban_Environments/Distance-Attention_Augmented_Reinforcement_Learning_A_Robust_Approach_for_3D_Cooperative_UAV_Navigation_in_Dense_Urban_Environments.md`
- Origin PDF: `raw/sources/Distance-Attention_Augmented_Reinforcement_Learning_A_Robust_Approach_for_3D_Cooperative_UAV_Navigation_in_Dense_Urban_Environments/Distance-Attention_Augmented_Reinforcement_Learning_A_Robust_Approach_for_3D_Cooperative_UAV_Navigation_in_Dense_Urban_Environments.pdf`
- Figures: `raw/sources/Distance-Attention_Augmented_Reinforcement_Learning_A_Robust_Approach_for_3D_Cooperative_UAV_Navigation_in_Dense_Urban_Environments/images/`
