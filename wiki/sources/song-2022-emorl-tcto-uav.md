---
type: source
title: "Evolutionary Multi-Objective Reinforcement Learning Based Trajectory Control and Task Offloading in UAV-Assisted Mobile Edge Computing"
authors: ["Fuhong Song", "Huanlai Xing", "Xinhan Wang", "Shouxi Luo", "Penglin Dai", "Zhiwen Xiao", "Bowen Zhao"]
year: 2022
url: "https://doi.org/10.1109/TMC.2022.3208457"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, uav-mec, multi-objective-reinforcement-learning, evolutionary-reinforcement-learning, trajectory-control, task-offloading]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[multi-objective-reinforcement-learning]]"
  - "[[evolutionary-reinforcement-learning]]"
  - "[[multi-objective-mdp-vectorial-reward]]"
  - "[[uav-trajectory-control]]"
  - "[[ppo]]"
  - "[[song-2024-mol-aoi-energy]]"
  - "[[peng-2024-energy-time-uav-its]]"
created: 2026-05-29
updated: 2026-05-29
---

# Evolutionary Multi-Objective Reinforcement Learning Based Trajectory Control and Task Offloading in UAV-Assisted Mobile Edge Computing

## Citation

Song, F., Xing, H., Wang, X., Luo, S., Dai, P., Xiao, Z., & Zhao, B. (2022). *Evolutionary Multi-Objective Reinforcement Learning Based Trajectory Control and Task Offloading in UAV-Assisted Mobile Edge Computing*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2022.3208457.

## TL;DR

Studies **trajectory control and task offloading (TCTO)** for a single UAV that flies a planned trajectory to collect tasks from smart devices, acting either as MEC server or relay to a base station. TCTO is a three-objective problem — minimize task delay, minimize UAV energy, maximize collected tasks — that conflict. Single-objective and single-policy multi-objective RLs can't emit a set of policies for different preferences in one run, so the authors apply **evolutionary multi-objective RL (EMORL)**, improving its multi-task multi-objective PPO by retaining all new learning tasks in the offspring population. The result, **EMORL-TCTO**, yields better non-dominated policy sets.

## Problem framing

Smart devices not directly connected to a base station need a UAV to collect and process/relay their computation tasks. The TCTO objectives (delay, energy, throughput) trade off, and practitioners want a Pareto set spanning preferences, not a single weighted solution — motivating a multi-policy approach.

## System model

- **Roles.** One UAV alternates between MEC server (compute locally) and relay (offload to BS); makes online offloading decisions while following a trajectory.
- **Formulation.** Multi-objective MDP (MOMDP) with a [[multi-objective-mdp-vectorial-reward|vectorial reward]] over the three objectives.

## Method

- **EMORL-TCTO:** an evolutionary multi-objective RL algorithm that improves the original EMORL's multi-task multi-objective PPO by **retaining all new learning tasks in the offspring population**, preserving promising tasks and producing many non-dominated policies per run ([[evolutionary-reinforcement-learning]] + [[multi-objective-reinforcement-learning]]).

## Key findings

- Compared with NSGA-II, MOEA/D, EDDPG, ETD3, and the original EMORL, EMORL-TCTO strikes a better balance between objectives on nearly all instances by IGD and hypervolume, and leads on system metrics (average task delay, average UAV energy, average tasks collected, comprehensive objective indicator). It also ranks first in a Friedman test (qualitative summary; specific scores in the paper).

## Limitations / future work

Single-UAV setting. The authors flag extending to **multi-UAV** MEC with collision avoidance and inter-UAV collaboration via multi-agent multi-objective approaches.

## Relation to the corpus

A bridge between the wiki's **DRL** and **multi-objective/evolutionary** branches: it uses an evolutionary mechanism *around* an RL policy learner, unlike the pure-CMOP lineage ([[peng-2022-cmop-uav-path-planning]], [[peng-2024-energy-time-uav-its]]) and the pure-MORL approach of [[song-2024-mol-aoi-energy]] (note both share the multi-objective-learning framing). Introduces/reinforces [[multi-objective-reinforcement-learning]] and [[evolutionary-reinforcement-learning]].

## Raw artifacts

- `raw/sources/Evolutionary_Multi-Objective_Reinforcement_Learning_Based_Trajectory_Control_and_Task_Offloading_in_UAV-Assisted_Mobile_Edge_Computing/full.md`
- Original PDF and extracted figures in the same folder.
