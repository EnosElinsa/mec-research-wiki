---
type: source
modeling_card: required
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
updated: 2026-11-03
---

# Evolutionary Multi-Objective Reinforcement Learning Based Trajectory Control and Task Offloading in UAV-Assisted Mobile Edge Computing

## Citation

Song, F., Xing, H., Wang, X., Luo, S., Dai, P., Xiao, Z., & Zhao, B. (2022). *Evolutionary Multi-Objective Reinforcement Learning Based Trajectory Control and Task Offloading in UAV-Assisted Mobile Edge Computing*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2022.3208457.

## TL;DR

Studies **trajectory control and task offloading (TCTO)** for a single UAV that flies a planned trajectory to collect tasks from smart devices, acting either as MEC server or relay to a base station. TCTO is a three-objective problem — minimize task delay, minimize UAV energy, maximize collected tasks — that conflict. Single-objective and single-policy multi-objective RLs can't emit a set of policies for different preferences in one run, so the authors apply **evolutionary multi-objective RL (EMORL)**, improving its multi-task multi-objective PPO by retaining all new learning tasks in the offspring population. The result, **EMORL-TCTO**, yields better non-dominated policy sets.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: One UAV flies over smart devices (SDs), collects tasks from those within its coverage radius $R_{\max}$, and either computes them onboard or relays them to a base station. Task queues, UAV computation energy, and relay timing determine delay and throughput.
**Problem & objective**: The TCTO problem (25) is a three-objective problem, $\max_{\vartheta_t,d_t,b_t}(-D_{total},-E_{total},N_{total})$: minimize total task delay and UAV energy and maximize the number of collected tasks (24).
**Decision variables**:
| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Flight direction | $\vartheta_t$ | continuous, $[0,2\pi]$ | UAV heading in slot $t$ |
| Flight distance | $d_t$ | continuous, $[0,d_{\max}]$ | UAV displacement in slot $t$ |
| Offloading decision | $b_t$ | continuous, $[0,1]$ | Share of collected tasks relayed to the BS rather than computed onboard |
**Constraints**:
| ID | Meaning and key expression |
|---|---|
| C1-C2 | Heading $0\le\vartheta_t\le2\pi$ and distance $0\le d_t\le d_{\max}$ |
| C3 | Offloading decision $b_t\in[0,1]$ |
| C4-C5 | Movement area $0\le x_t^U\le x_{\max}$, $0\le y_t^U\le y_{\max}$ |
| C6 | Tasks are collected only from SDs within coverage, $d_t^k\le R_{\max}$ |
**Algorithm**: Model TCTO as a multi-objective MDP with vector rewards. EMORL-TCTO runs multi-task multi-objective PPO over a population of preference vectors, keeps nondominated policies, and uses an evolutionary stage to add new learning tasks, returning a Pareto set of policies in one run.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Song et al. [x] studied trajectory control and task offloading for a UAV that acts as an MEC server or relay for smart-device tasks. They formulated a three-objective problem, solved as a multi-objective Markov decision process, that minimizes task delay and UAV energy while maximizing collected tasks under heading, distance, offloading-ratio, area, and coverage constraints. EMORL-TCTO extends multi-task multi-objective PPO with an evolutionary population that retains new learning tasks and produces multiple nondominated policies in one run. The resulting policy set spans different preference vectors instead of one fixed scalarization. Experiments report better inverted generational distance, hypervolume, and system metrics than NSGA-II, MOEA/D, EDDPG, ETD3, and the original EMORL in the evaluated instances.

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

- `raw/sources/Evolutionary_Multi-Objective_Reinforcement_Learning_Based_Trajectory_Control_and_Task_Offloading_in_UAV-Assisted_Mobile_Edge_Computing/Evolutionary_Multi-Objective_Reinforcement_Learning_Based_Trajectory_Control_and_Task_Offloading_in_UAV-Assisted_Mobile_Edge_Computing.md`
- Original PDF and extracted figures in the same folder.
