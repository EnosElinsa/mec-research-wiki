---
type: source
modeling_card: required
title: "Multi-Agent Transformer Learning for Moving Target Positioning and Tracking in Complex Environments Using UAV Swarms"
authors: ["Haowen Wang", "Junyu Wei", "Ni Zhu", "Zongqing Zhao", "Zhuoyuan Wu", "Shiqi Li", "Yuyang Xiao", "Jiangyi Qin", "Zhiqiang Wang"]
year: 2026
url: "https://doi.org/10.1109/TITS.2026.3679479"
venue: "IEEE Transactions on Intelligent Transportation Systems (IEEE T-ITS), vol. 27, pp. 6647-6663"
tags: [source, uav-swarm, target-tracking, tdoa, multi-agent-transformer, trajectory-control, localization]
related:
  - "[[multi-agent-transformer]]"
  - "[[tdoa-based-uav-localization]]"
  - "[[geometric-dilution-of-precision]]"
  - "[[autonomous-uav-swarms]]"
  - "[[ma-pomdp]]"
  - "[[uav-trajectory-control]]"
  - "[[sequential-multi-agent-policy-generation]]"
  - "[[transformer-encoder]]"
  - "[[ppo]]"
created: 2026-07-13
updated: 2026-07-16
---

# Multi-Agent Transformer Learning for Moving Target Positioning and Tracking in Complex Environments Using UAV Swarms

## Citation

Wang, H., Wei, J., Zhu, N., Zhao, Z., Wu, Z., Li, S., Xiao, Y., Qin, J., & Wang, Z. (2026). *Multi-Agent Transformer Learning for Moving Target Positioning and Tracking in Complex Environments Using UAV Swarms*. **IEEE Transactions on Intelligent Transportation Systems, 27**, 6647-6663. DOI: 10.1109/TITS.2026.3679479.

## TL;DR

Combines Taylor-iteration TDOA localization, Hungarian formation assignment, and an encoder-decoder Multi-Agent Transformer to position a UAV swarm around one moving ground target while balancing GDOP, obstacle clearance, and flight distance.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A swarm of passive UAV receivers localizes and tracks one signal-emitting moving ground target from TDOA measurements under LoS and biased NLoS errors. Virtual tracking points define a sensing formation in complex obstacle maps, and each UAV controls planar velocity from local observations.

**Problem & objective**: A partially observed multi-agent trajectory problem minimizes localization geometry and travel cost, $\min \sum_t[\lambda_G\operatorname{GDOP}(t)+\lambda_L\sum_m\lVert\mathbf q_m(t+1)-\mathbf q_m(t)\rVert]$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Target estimate | $\hat{\mathbf p}(t)$ | continuous 2-D position | Taylor-iteration TDOA estimate |
| Formation assignment | $x_{m,j}(t)$ | binary | Virtual tracking point $j$ assigned to UAV $m$ |
| UAV velocity action | $\Delta\mathbf v_m(t)$ | discrete planar action | Velocity change selected by the policy |
| UAV trajectory | $\mathbf q_m(t)$ | continuous position | Resulting receiver path around the target |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Hungarian assignment maps each UAV to one virtual tracking point |
| C2 | UAV positions and velocities follow the discrete motion model and action limits |
| C3 | UAVs maintain obstacle clearance and feasible map boundaries |
| C4 | Formation geometry remains informative for TDOA localization and tracking |
| C5 | Path length and motion changes are penalized as flight-cost proxies |

**Algorithm**: Estimate the target by iterative TDOA localization → place virtual tracking points around the estimate → assign UAVs with the Hungarian algorithm → encode all local observations with a Multi-Agent Transformer → generate actions sequentially with a masked autoregressive PPO decoder → move the swarm and repeat.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Wang et al. [x] studied moving-target positioning and tracking with UAV swarms in complex environments. Their system combines iterative TDOA localization with virtual sensing formations and Hungarian assignment of UAVs to formation points. A Multi-Agent Transformer encodes all UAV observations, and a masked autoregressive decoder generates discrete velocity actions using multi-agent advantage decomposition and a clipped PPO objective. The control objective balances geometric dilution of precision, obstacle avoidance, progress toward assigned points, and flight distance. Simulations report lower mean positioning error than the evaluated learning baselines across the tested environments and retain performance in additional zero-shot simulated maps.

## Problem and system model

Passive UAV receivers estimate one signal-emitting ground target from time-difference-of-arrival measurements. LoS errors are zero-mean Gaussian; NLoS errors are biased and larger. Around each target estimate, virtual tracking points define a sensing formation and Hungarian assignment maps UAVs to those points.

Each UAV observes its position/velocity, eight obstacle distances, and relative geometry to its assigned point. Actions are discrete planar velocity changes. The continuous objective combines time-integrated [[geometric-dilution-of-precision|GDOP]] and total path length, while the practical reward adds progress, obstacle, geometry, and movement terms.

## Method

The [[multi-agent-transformer]] encoder contextualizes all UAV observations. A masked autoregressive decoder uses multi-agent advantage decomposition and a clipped PPO objective to generate actions sequentially; stored previous actions allow parallel training computation. This joins [[tdoa-based-uav-localization]] with controlled sensing geometry rather than treating target estimates as fixed observations.

## Key findings

- Across three Blocks simulations, MAT has mean MAE 1.14 m, RMSE 1.99 m, and GDOP 1.94, best among the listed mean values.
- Across Neighborhood/Village/Forest simulations, MAT has the lowest mean MAE (1.54 m) and RMSE (5.81 m), but its mean GDOP (15.37) is worse than several baselines.
- Zero-shot transfer across four additional simulated maps reports mean MAE 1.39 m, RMSE 2.71 m, and GDOP 2.80.
- In the preliminary 1,000-run all-LoS/low-GDOP experiment, more than 80% of errors are below 0.5 m; NLoS links and poor geometry broaden the error.

## Limitations

All environments are simulations, including the realistic-looking maps. The study tracks one target, uses simplified directional obstacle distances, and controls only planar velocity despite 3-D notation. Path length is an energy proxy without propulsion or battery validation. MAT does not minimize GDOP in every environment, and transfer remains sim-to-sim. Several motion constraints and table headers are parse-damaged.

## Relation to the corpus

This source extends the TDOA tracking in [[zhu-2024-zdrl-uav-tracking]] with explicit virtual-formation assignment and autoregressive Transformer coordination. It connects swarm motion, localization geometry, and partial-observation MARL without modeling MEC computation.

## Raw artifacts

- `raw/sources/Multi-Agent_Transformer_Learning_for_Moving_Target_Positioning_and_Tracking_in_Complex_Environments_Using_UAV_Swarms/Multi-Agent_Transformer_Learning_for_Moving_Target_Positioning_and_Tracking_in_Complex_Environments_Using_UAV_Swarms.md`
- Original PDF and extracted figures (`images/`) are in the same folder.
