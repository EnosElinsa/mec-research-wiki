---
type: source
title: "Task Assignment and Exploration Optimization for Low Altitude UAV Rescue via Generative AI Enhanced Multi-Agent Reinforcement Learning"
authors: ["Xin Tang", "Qian Chen", "Wenjie Weng", "Chao Jin", "Zhang Liu", "Jiacheng Wang", "Geng Sun", "Xiaohuan Li", "Dusit Niyato"]
year: 2026
url: "https://doi.org/10.1109/TMC.2025.3594188"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC), vol. 25, no. 1, pp. 627-643, Jan. 2026"
modeling_card: required
tags: [source, low-altitude-economy, post-disaster-mec, task-offloading, lyapunov-optimization, generative-diffusion-model, maddpg]
related:
  - "[[ground-embedded-robot]]"
  - "[[low-altitude-intelligent-network]]"
  - "[[post-disaster-mec]]"
  - "[[task-offloading]]"
  - "[[uav-trajectory-control]]"
  - "[[lyapunov-optimization]]"
  - "[[maddpg]]"
  - "[[generative-diffusion-model]]"
  - "[[generative-ai-for-mec]]"
  - "[[sun-2024-mvtora-postdisaster-vfc]]"
created: 2026-07-07
updated: 2026-07-16
---

# Task Assignment and Exploration Optimization for Low Altitude UAV Rescue via Generative AI Enhanced Multi-Agent Reinforcement Learning

## Citation

Tang, X., Chen, Q., Weng, W., Jin, C., Liu, Z., Wang, J., Sun, G., Li, X., & Niyato, D. (2026). *Task Assignment and Exploration Optimization for Low Altitude UAV Rescue via Generative AI Enhanced Multi-Agent Reinforcement Learning*. **IEEE Transactions on Mobile Computing**, 25(1), 627-643. DOI: 10.1109/TMC.2025.3594188. DOI evidence appears in the local parse and was cross-checked against title-matched DOI metadata.

## TL;DR

Models low-altitude UAV rescue in unknown post-disaster areas with UAVs, ground embedded robots, and airships. The proposed HG-MADDPG framework combines Hungarian area assignment, Lyapunov energy control, and a generative-diffusion-enhanced MADDPG policy for task assignment, offloading-ratio, GER selection, and exploration decisions.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Multiple UAVs explore disjoint post-disaster subareas and run object-detection tasks while moving. Ground embedded resources provide nearby computation, and higher-altitude airships supply communication coverage and fallback processing when terrestrial infrastructure is unavailable.

**Problem & objective**: Problem P1 minimizes total task-completion latency, $\min_{\mathbf F,\mathbf M,\mathbf W}\sum_i T^{total}(t_i)$, over offloading, computation-resource, and UAV trajectory decisions while enforcing long-term energy, task-service, resource, mobility, and collision constraints.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Task offloading decision | $\varsigma_{u,j}(t_i)$ | continuous, $[0,1]$ | Fraction or association of UAV $u$ offloaded to ground resource $j$ |
| Computation allocation | $f_{j,u}(t_i)$ | continuous, bounded | Ground computation assigned to UAV $u$ by resource $j$ |
| UAV trajectory control | $\mathbf W$ | continuous motion sequence | Per-slot exploration position and movement decisions |
| Subarea assignment | $A_{u,b}$ | binary matching | Assignment of UAV $u$ to rescue subarea $b$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| 20a | Long-term average UAV energy stays below budget $\bar E_u$ |
| 20b-20d | Offloading fractions are bounded and UAV-resource assignments obey one-to-one service limits |
| 20e-20f | Local and offloaded processing satisfy task deadline $\tau_u$ |
| 20g-20h | Per-user and aggregate ground computation remain within resource capacity |
| 20i-20k | UAV speed, route length, and pairwise safety-distance constraints hold |

**Algorithm**: Lyapunov optimization converts the long-term energy constraint into a stable virtual queue and a per-slot drift-plus-penalty objective. A Hungarian step assigns UAVs to subareas, after which HG-MADDPG uses a diffusion-enhanced actor within centralized-training, decentralized-execution learning to choose offloading ratios, ground resources, and exploration actions.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Tang et al. [x] studied joint task assignment and exploration for low-altitude UAV rescue when terrestrial communication infrastructure is unavailable. Their model combines mobile UAV object detection, ground embedded computing resources, airship coverage, task deadlines, computation limits, propulsion and processing energy, route bounds, and collision avoidance. They formulate a long-term constrained problem over offloading, computation allocation, and trajectory control and use a Lyapunov virtual queue to expose per-slot decisions. The proposed HG-MADDPG framework applies Hungarian subarea assignment before a diffusion-enhanced multi-agent actor-critic chooses offloading ratios, ground resources, and exploration actions. Simulations report lower task-completion latency than MADDPG and MAPPO and demonstrate stable energy queues and obstacle-aware exploration in the evaluated rescue area.

## Problem

After disasters, base stations may be unavailable and single-UAV computing is insufficient for real-time object-detection workloads. UAV rescue must jointly handle exploration, obstacle-aware links, energy limits, heterogeneous compute resources, and partial observations while keeping latency low and avoiding unstable long-term energy use.

## System model

Multiple UAVs fly below 300 m and perform object detection while moving. Ground embedded robots provide ground computing support, and airships at higher altitude provide wider coverage and fallback task processing when GER resources are insufficient. The model includes U2G and U2A links, non-overlapping UAV exploration subareas, LoS/NLoS U2G channels with Nakagami fading, OFDMA access, task data size/intensity/deadline, local-UAV and GER processing, transmission/computation/propulsion/detection energy, and a long-term average energy budget.

## Method

Lyapunov optimization converts the long-term stochastic constrained problem into a per-slot drift-plus-penalty problem with an energy queue. HG-MADDPG then uses two layers:

- a Hungarian assignment step selects UAV-area assignments from a cost that combines UAV-area distance, data size, computation intensity, remaining energy, and average GER compute capability;
- a GDM-MADDPG controller replaces ordinary actor action generation with a reverse-diffusion policy under a CTDE-style multi-agent actor-critic setup.

The actions cover task assignment, offloading ratios, GER selection, and trajectory/exploration behavior.

## Key findings

- The reported simulation uses nine UAVs at 50 m over a 50 km by 50 km rescue area, with an airship at 600 m and Yolov8s object detection.
- HG-MADDPG reward stabilizes around 1200 after about 300 episodes in the parse.
- The parse reports best settings around five denoising steps, batch size 300, and learning rate 0.0001.
- The Lyapunov queue mechanism keeps queuing energy and task-latency behavior stable in the reported plots.
- HG-MADDPG selects GERs with stronger current compute capacity and lower delay, and the trajectory figures show obstacle-aware subarea exploration.
- The parse reports larger latency reductions versus MADDPG and MAPPO, but the exact unit/sign convention of the reported 20.35 and 12.56 values is not explicit in the extracted text.

## Limitations / future work

The conclusion names 3D trajectory planning and network topology optimization as future work for improving low-altitude network reliability in complex environments.

## Relation to the corpus

This source extends the [[post-disaster-mec]] and [[low-altitude-intelligent-network]] tracks with explicit [[ground-embedded-robot]] compute support. Methodologically it connects [[lyapunov-optimization]], [[maddpg]], and [[generative-diffusion-model]], making it close to [[liu-2026-lyapunov-diffusion-uav-vehicular]] on Lyapunov-plus-diffusion control but grounded in UAV rescue rather than vehicular V2X.

## Raw artifacts

- `raw/sources/Task_Assignment_and_Exploration_Optimization_for_Low_Altitude_UAV_Rescue_via_Generative_AI_Enhanced_Multi-Agent_Reinforcement_Learning/Task_Assignment_and_Exploration_Optimization_for_Low_Altitude_UAV_Rescue_via_Generative_AI_Enhanced_Multi-Agent_Reinforcement_Learning.md`
- Original PDF and extracted figures (`images/`) in the same folder.
