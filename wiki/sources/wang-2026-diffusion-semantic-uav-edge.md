---
type: source
title: "Diffusion-Based Trajectory and Semantic Resource Optimization in UAV-Assisted Edge Computing"
authors: ["Chen Wang", "Ruonan Zhang", "Zehui Xiong", "Daosen Zhai", "Dusit Niyato", "Zhu Han"]
year: 2026
url: "https://doi.org/10.1109/TWC.2026.3657387"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, uav-assisted-edge-computing, semantic-communication, diffusion-model, ddpg, trajectory-optimization, resource-allocation, semantic-edge-computing]
related:
  - "[[semantic-communication]]"
  - "[[diffusion-model-as-optimizer]]"
  - "[[generative-diffusion-model]]"
  - "[[ddpg]]"
  - "[[uav-trajectory-control]]"
  - "[[task-oriented-communication]]"
  - "[[sun-2024-mfris-semantic-antijamming]]"
  - "[[zheng-2024-semcom-sec-offloading]]"
  - "[[dusit-niyato]]"
  - "[[zhu-han]]"
  - "[[zehui-xiong]]"
created: 2026-07-06
updated: 2026-07-13
---

# Diffusion-Based Trajectory and Semantic Resource Optimization in UAV-Assisted Edge Computing

## Citation

Wang, C., Zhang, R., Xiong, Z., Zhai, D., Niyato, D., & Han, Z. (2026). *Diffusion-Based Trajectory and Semantic Resource Optimization in UAV-Assisted Edge Computing*. **IEEE Transactions on Wireless Communications**, 25, 11672-11687. DOI: 10.1109/TWC.2026.3657387.

## TL;DR

A UAV-assisted semantic edge computing network that jointly optimizes UAV trajectory, edge-device data allocation, and semantic extraction factor to maximize semantic processing rate. The paper first builds H-DDPG, combining DDPG trajectory control with convex optimization for semantic resource decisions, then introduces H-D3PG, where a diffusion denoising actor generates richer UAV movement actions.

## Problem

Raw-data uplink transmission strains bandwidth and energy budgets in edge sensing applications, while optimizing UAV trajectory and semantic extraction separately can be suboptimal. The paper models semantic extraction, semantic transmission, and semantic recovery jointly, then maximizes semantic processing rate under per-slot time, device-energy, buffer, and UAV-mobility constraints.

## System model

- **Network:** one UAV collects semantic information from M edge devices such as smart cameras or environmental sensors.
- **Semantics:** each device extracts task-oriented latent features using a compact Transformer-style semantic encoder following DeepSC; the paper distinguishes this from information-theoretic semantic entropy.
- **Decision variables:** per-slot data allocation, UAV trajectory, semantic extraction factor, and an auxiliary computation-time variable.
- **Constraints:** semantic extraction / transmission / recovery must fit within a slot; each device has an energy budget; UAV motion is bounded by a maximum per-slot flight distance.
- **Metric:** semantic processing rate measures semantic data successfully extracted, transmitted, and recovered per unit time.

## Method

H-DDPG treats the UAV as a continuous-control agent whose action is the trajectory movement, while a convex optimization module solves data allocation and semantic extraction decisions for a given trajectory using block-coordinate ideas. H-D3PG replaces the deterministic DDPG actor with a denoising diffusion policy: actions start from Gaussian noise and are refined through reverse diffusion steps guided by the critic. The paper uses offline training and forward inference during deployment.

## Key findings

- H-D3PG generally reaches higher convergence levels than H-DDPG across the learning-rate configurations reported in the convergence plots.
- Inference-latency measurements show per-step decision latency from **88.64 ms** for 10 users to **205.99 ms** for 25 users, below the 1 s slot duration in the simulated setting.
- Under stochastic user mobility, semantic processing rate decreases from **92.04 suts/s** at 0 m/step to **84.02 suts/s** at 10 m/step, about an 8-9% degradation.
- The paper reports that H-D3PG improves semantic processing rate by up to **38.8%** compared with Raw Data Transmission under the evaluated edge-device computing-resource setting.

## Limitations / future work

The work primarily assumes static edge devices, with only a supplementary stochastic-mobility robustness test. The conclusion identifies fully mobile scenarios, multimodal semantic data, and multi-UAV networks as future extensions. The UAV energy is not explicitly modeled; the parse states that the UAV is assumed to have a more flexible energy supply and that the latency constraint limits flight duration.

## Relation to the corpus

This is a strong bridge between [[semantic-communication]] and [[diffusion-model-as-optimizer]]. Unlike [[sun-2024-mfris-semantic-antijamming]], which optimizes semantic computation rate under jamming and RIS constraints, this source focuses on UAV mobility plus semantic extraction / allocation. It is also complementary to [[zheng-2024-semcom-sec-offloading]]: both use semantic communication for edge offloading, but this paper's distinctive move is diffusion-actor trajectory optimization inside a UAV-assisted semantic edge network.

## Raw artifacts

- `raw/sources/Diffusion-Based Trajectory and Semantic Resource Optimization in UAV-Assisted Edge Computing/Diffusion-Based Trajectory and Semantic Resource Optimization in UAV-Assisted Edge Computing.md`
- Original PDF and extracted figures (`images/`) in the same folder.
