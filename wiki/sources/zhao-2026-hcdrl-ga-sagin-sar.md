---
type: source
title: "Joint Offloading, Trajectory and Deployment Optimization for Multi-UAV Cooperative Regional Search in SAGINs: A Hybrid DRL-GA Framework"
authors: ["Peng Zhao", "Hongbing Cheng", "Hangyu Zhang", "Zhiguo Wan"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3709181"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, sagin, search-and-rescue, task-offloading, uav-trajectory-control, soft-actor-critic, graph-neural-network, genetic-algorithm]
related:
  - "[[space-air-ground-integrated-network]]"
  - "[[uav-trajectory-control]]"
  - "[[soft-actor-critic]]"
  - "[[graph-neural-network]]"
  - "[[genetic-algorithm]]"
  - "[[post-disaster-mec]]"
  - "[[gao-2024-sagin-perception-offloading]]"
  - "[[zhao-2025-probabilistic-semantic-sagin]]"
created: 2026-07-07
updated: 2026-07-07
---

# Joint Offloading, Trajectory and Deployment Optimization for Multi-UAV Cooperative Regional Search in SAGINs: A Hybrid DRL-GA Framework

## Citation

Zhao, P., Cheng, H., Zhang, H., & Wan, Z. (2026). *Joint Offloading, Trajectory and Deployment Optimization for Multi-UAV Cooperative Regional Search in SAGINs: A Hybrid DRL-GA Framework*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2026.3709181.

## TL;DR

Targets multi-UAV search and rescue in [[space-air-ground-integrated-network|SAGIN]] settings where wind, terrain, coverage, and heterogeneous offloading tiers interact. The paper decomposes the problem into online HCDRL control and low-frequency GA deployment search: an HCSAC policy uses CNN local perception plus GCN topology/offloading embeddings for trajectory and offloading, while a [[genetic-algorithm]] evaluates takeoff/recovery deployments through learned-policy rollouts. NOAA-derived GFS wind fields and uncertainty-aware terrain abstraction make the simulation less idealized than a static-grid UAV-MEC benchmark.

## Problem framing

Search-and-rescue UAV fleets must cover uncertain terrain while conserving energy and selecting where computation runs. Fixed deployment, idealized channels, and no-wind simulations can misrepresent mountainous SAR missions: poor initial geometry becomes expensive under wind, offloading nodes differ across BS/HAPS/LEO/cloud tiers, and monolithic DRL over deployment, trajectory, and offloading suffers from a large hybrid action-state space.

## System model

- A 10 km x 10 km search region is discretized into a 20 x 20 grid; the default fleet has four UAVs at 200 m altitude, with 20 m/s flight speed and `3.6e5 J` battery capacity.
- UAVs sense grid cells with onboard cameras and generate computation tasks while communicating with a SAGIN support stack that includes BS, HAPS, LEO, and cloud/central-edge resources.
- The wind state comes from offline NOAA GFS records, cropped and interpolated into local wind-u/wind-v maps; the authors state this is simulation input, not a real-time weather-data pipeline.
- The optimization couples deployment/recovery positions, per-step trajectory decisions, offloading-tier choices, task-completion latency, search coverage, and energy cost.

## Method

- **HCDRL / HCSAC.** Soft Actor-Critic is wrapped in hybrid convolutional state encoding: each UAV receives a local three-channel map for uncertainty and wind, while GCN embeddings capture SAGIN topology and offloading connectivity.
- **Policy-in-the-loop GA.** A chromosome represents candidate takeoff/recovery configurations. Each candidate is scored through HCDRL rollouts with normalized coverage, energy, and task-completion latency terms.
- **Module separation.** GA handles mission-level deployment at low frequency, while HCDRL handles online trajectory and offloading; this avoids forcing all decisions into one monolithic distributed DRL policy.
- **Interpretability.** Offloading heatmaps and UAV visit-frequency maps are used to inspect tier preference and emergent spatial partitioning.

## Key findings

- The full GA-HCSAC variant reports the best lifetime and coverage under low, moderate, and strong wind. Under strong wind, it reaches `38.47 +/- 1.19` minutes and `62.77 +/- 2.01%` coverage, versus `31.65 +/- 1.23` minutes and `53.20 +/- 1.97%` coverage without GA.
- Removing both offloading and GA gives the largest strong-wind drop: `27.85 +/- 0.99` minutes and `47.20 +/- 1.60%` coverage.
- The authors report that the full model extends mission lifetime by up to 38% and coverage by 33% under strong wind versus standard baselines; the GA deployment module alone contributes a nearly 18% strong-wind coverage lift.
- Standard DRL variants scale poorly in the preliminary no-wind comparison, while HCDRL remains trainable up to the tested six-UAV case.
- Training 1000 episodes takes 1.41 hours on the reported RTX 3060 / R7 5800H setup; forward inference latency is 8.96 ms per decision step at batch size 1.

## Limitations / future work

The validation is simulation-only. NOAA-derived wind fields improve environmental realism, but the paper does not test real UAV hardware, onboard processors, wireless-link instability, sensor delays, online environment updates, communication holes, or post-failure recovery. Scalability evidence covers one to six UAVs only. The GA module returns one weighted-sum deployment configuration rather than a Pareto front; the authors name NSGA-II-style Pareto variants, field validation, larger deployments, connectivity-aware offloading, and efficient GA replanning as future work.

## Relation to the corpus

This source strengthens the [[space-air-ground-integrated-network]] line from a SAR / deployment angle. Compared with [[gao-2024-sagin-perception-offloading]], it models wind-terrain search and deployment optimization rather than perception-aided queue-stable task hosting. It also connects to [[post-disaster-mec]] because the SAR setting shares weak-infrastructure and emergency-response assumptions, but its main architectural home is SAGIN. Methodologically, it adds a [[genetic-algorithm]] deployment layer on top of [[soft-actor-critic]], [[graph-neural-network]], and [[uav-trajectory-control]].

## Raw artifacts

- `raw/sources/Joint Offloading- Trajectory and Deployment Optimization for Multi-UAV Cooperative Regional Search in SAGINs A Hybrid DRL-GA Framework/Joint Offloading- Trajectory and Deployment Optimization for Multi-UAV Cooperative Regional Search in SAGINs A Hybrid DRL-GA Framework.md`
- Original PDF and extracted figures (`images/`) in the same folder.
