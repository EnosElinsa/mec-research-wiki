---
type: source
title: "PointRL: Reinforcement Learning-Based Approach for Air-Ground Communications Using Multi-Dimensional Target Sensing Point Cloud"
authors: ["Leyan Chen", "Kai Liu", "Peng Yang", "Zehui Xiong", "Tony Q. S. Quek", "Jisi Fang", "Zhibo Zhang"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3679741"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC), pp. 1-15"
tags: [source, uav-isac, radar-point-cloud, reinforcement-learning, trajectory-control, resource-allocation, vehicular-network]
related:
  - "[[radar-point-cloud-driven-uav-isac]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[mmwave-radar-sensing]]"
  - "[[uav-trajectory-control]]"
  - "[[zehui-xiong]]"
  - "[[tony-q-s-quek]]"
created: 2026-07-14
updated: 2026-07-14
---

# PointRL: Reinforcement Learning-Based Approach for Air-Ground Communications Using Multi-Dimensional Target Sensing Point Cloud

## Citation

Chen, L., Liu, K., Yang, P., Xiong, Z., Quek, T. Q. S., Fang, J., & Zhang, Z. (2026). *PointRL: Reinforcement Learning-Based Approach for Air-Ground Communications Using Multi-Dimensional Target Sensing Point Cloud*. **IEEE Transactions on Mobile Computing**, 1-15. DOI: 10.1109/TMC.2026.3679741.

## TL;DR

Maps 3-D mmWave radar point clouds of vehicles into segmented trajectory and power-allocation action spaces, then uses deep Q-learning with a sliding-window reward to balance UAV-to-vehicle communication capacity, radar capacity, and minimum-user fairness.

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
