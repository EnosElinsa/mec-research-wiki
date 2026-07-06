---
type: source
title: "Task Assignment and Exploration Optimization for Low Altitude UAV Rescue via Generative AI Enhanced Multi-Agent Reinforcement Learning"
authors: ["Xin Tang", "Qian Chen", "Wenjie Weng", "Chao Jin", "Zhang Liu", "Jiacheng Wang", "Geng Sun", "Xiaohuan Li", "Dusit Niyato"]
year: 2026
url: "https://doi.org/10.1109/TMC.2025.3594188"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC), vol. 25, no. 1, pp. 627-643, Jan. 2026"
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
updated: 2026-07-07
---

# Task Assignment and Exploration Optimization for Low Altitude UAV Rescue via Generative AI Enhanced Multi-Agent Reinforcement Learning

## Citation

Tang, X., Chen, Q., Weng, W., Jin, C., Liu, Z., Wang, J., Sun, G., Li, X., & Niyato, D. (2026). *Task Assignment and Exploration Optimization for Low Altitude UAV Rescue via Generative AI Enhanced Multi-Agent Reinforcement Learning*. **IEEE Transactions on Mobile Computing**, 25(1), 627-643. DOI: 10.1109/TMC.2025.3594188. DOI evidence appears in the local parse and was cross-checked against title-matched DOI metadata.

## TL;DR

Models low-altitude UAV rescue in unknown post-disaster areas with UAVs, ground embedded robots, and airships. The proposed HG-MADDPG framework combines Hungarian area assignment, Lyapunov energy control, and a generative-diffusion-enhanced MADDPG policy for task assignment, offloading-ratio, GER selection, and exploration decisions.

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
