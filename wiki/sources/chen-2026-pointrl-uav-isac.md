---
type: source
title: "PointRL: Reinforcement Learning-Based Approach for Air-Ground Communications Using Multi-Dimensional Target Sensing Point Cloud"
authors: ["Leyan Chen", "Kai Liu", "Peng Yang", "Zehui Xiong", "Tony Q. S. Quek", "Jisi Fang", "Zhibo Zhang"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3679741"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC), pp. 1-15"
modeling_card: required
tags: [source, uav-isac, radar-point-cloud, reinforcement-learning, trajectory-control, resource-allocation, vehicular-network]
related:
  - "[[radar-point-cloud-driven-uav-isac]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[mmwave-radar-sensing]]"
  - "[[uav-trajectory-control]]"
  - "[[zehui-xiong]]"
  - "[[tony-q-s-quek]]"
created: 2026-07-14
updated: 2026-07-16
---

# PointRL: Reinforcement Learning-Based Approach for Air-Ground Communications Using Multi-Dimensional Target Sensing Point Cloud

## Citation

Chen, L., Liu, K., Yang, P., Xiong, Z., Quek, T. Q. S., Fang, J., & Zhang, Z. (2026). *PointRL: Reinforcement Learning-Based Approach for Air-Ground Communications Using Multi-Dimensional Target Sensing Point Cloud*. **IEEE Transactions on Mobile Computing**, 1-15. DOI: 10.1109/TMC.2026.3679741.

## TL;DR

Maps 3-D mmWave radar point clouds of vehicles into segmented trajectory and power-allocation action spaces, then uses deep Q-learning with a sliding-window reward to balance UAV-to-vehicle communication capacity, radar capacity, and minimum-user fairness.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A fixed-altitude mmWave-radar UAV serves moving vehicles over U2V links. Radar point clouds represent each vehicle as a rigid shape, and an optional V2V fleet groups vehicles to reduce interference while the UAV adapts its trajectory and power split.

**Problem & objective**: Without a fleet, maximize the weighted communication and radar capacity objective $\xi_c(\min_k C_{c,k})^{\eta}(\sum_k C_{c,k})^{1-\eta}+\xi_r(\min_k C_{r,k})^{\eta}(\sum_k C_{r,k})^{1-\eta}$ over UAV positions and vehicle power ratios; the fleet variant replaces individual communication capacity with fleet capacity.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV position | $q_u[n]$ | continuous 2-D position | Horizontal UAV trajectory at slot $n$ |
| Vehicle power ratio | $\rho_{u,k}[n]$ | continuous, $[0,1]$ | Fraction of UAV transmit power assigned to vehicle $k$ |
| Trajectory action | $a_\alpha$ | discrete set | Movement action selected by the RL controller |
| Power action | $a_\beta$ | discrete set | Power-ratio allocation action selected by the RL controller |
| Fleet membership | $\alpha_k$ | discrete label | Fleet index for vehicle $k$ in the V2V variant |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | UAV stays inside the horizontal region: $0\le x_u[n]\le x_u^{\max}$ and $0\le y_u[n]\le y_u^{\max}$. |
| C2 | Power ratios sum to one: $\sum_{k=1}^{K}\rho_{u,k}[n]=1$. |
| C3 | UAV speed is bounded: $\lVert\dot{\mathbf q}_u[n]\rVert\le V_{\max}$. |
| C4 | Relative radial velocity for each sensed vehicle meets the threshold: $\lvert\tilde V_{u,k}[n]\rvert\ge V_0$. |
| C5 | Fleet communication capacity is the sum of member U2V capacities: $\tilde C_{c,l}=\sum_{\alpha_k=l}C_{c,k}$. |

**Algorithm**: Encode radar point clouds with a PDNN, use separate fully connected branches for trajectory and power actions, concatenate their discrete outputs, and train a DQN-style controller with a linear weighted sliding-window reward over recent communication and radar capacities.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Chen et al. [x] proposed a radar-point-cloud-driven U2V integrated sensing and communication controller for a UAV serving moving vehicles. They optimized horizontal UAV trajectory and per-vehicle power ratios, with an optional V2V fleet formulation, to balance total and minimum communication and radar capacities under region, power-sum, speed, and sensing-velocity constraints. PointRL encodes rigid vehicle point clouds with a PDNN, separates trajectory and power action branches, and trains a DQN-style policy with a sliding-window reward. The reported controller achieved 6.34 Kbits communication capacity and 13.89 Mbits radar capacity, reduced parameters by 40.52%, and inferred in 21.37 ms.

## Problem and system model

A fixed-altitude UAV gNodeB with mmWave radar serves moving vehicles over U2V links. Vehicles are represented by range, velocity, and radar-cross-section point-cloud features rather than known point coordinates. The communication channel includes elevation-dependent LoS/NLoS attenuation and multi-user interference; radar mutual information is expressed as radar capacity.

The first optimization jointly selects horizontal UAV motion and per-vehicle power ratios. A second variant lets nearby vehicles form V2V fleets so one U2V link can serve a group, mitigating dense-vehicle interference. A fairness parameter balances minimum and total communication/radar capacities rather than applying a standalone Jain index.

## Method

[[radar-point-cloud-driven-uav-isac|PointRL]] uses a point-cloud deep neural network to encode vehicle shapes and produce trajectory and power features. Separate decision branches process the two action subspaces before concatenation, avoiding one large Cartesian-product output. A DQN-style controller selects the joint discrete action, while a linear weighted sliding-window reward smooths recent communication and radar returns.

## Key findings

- In the reported simulations, PointRL reaches 6.34 Kbits communication capacity and 13.89 Mbits radar capacity, outperforming DQN, clustering-aided DRL, PPO, TD3, and the no-sliding-window ablation.
- Action-space segmentation reduces network parameters by 40.52% relative to the unsegmented baseline; measured inference time is 21.37 ms on the evaluation platform.
- Finer trajectory and power discretization improves the reported capacities but increases parameter count and training/generalization cost.
- A small controlled-field study collects real vehicle point clouds with a DJI Inspire 2-mounted 76-81 GHz radar and numerically reproduces the method's relative advantage at different powers.

## Limitations

Most performance evidence is simulation-based. The controlled-field component validates radar input realism, not a closed-loop over-the-air U2V communication deployment. UAV altitude is fixed; actions discretize trajectory and power; training uses scenario-specific reward weights; and no safety, energy, or global-optimality guarantee is provided.

## Relation to the corpus

This source extends [[mmwave-radar-sensing]] from state estimation into direct [[uav-trajectory-control]] and resource decisions. It complements model-based UAV-ISAC papers by learning from vehicle-shape point clouds while preserving explicit communication, sensing, and minimum-user terms.

## Raw artifacts

- Parse: `raw/sources/PointRL_Reinforcement_Learning-Based_Approach_for_Air-Ground_Communications_Using_Multi-Dimensional_Target_Sensing_Point_Cloud/PointRL_Reinforcement_Learning-Based_Approach_for_Air-Ground_Communications_Using_Multi-Dimensional_Target_Sensing_Point_Cloud.md`
- Origin PDF and extracted figures (`images/`) are in the same folder.
