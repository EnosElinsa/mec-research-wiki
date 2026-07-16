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
updated: 2026-07-16
---

# Evolutionary Multi-Objective Reinforcement Learning Based Trajectory Control and Task Offloading in UAV-Assisted Mobile Edge Computing

## Citation

Song, F., Xing, H., Wang, X., Luo, S., Dai, P., Xiao, Z., & Zhao, B. (2022). *Evolutionary Multi-Objective Reinforcement Learning Based Trajectory Control and Task Offloading in UAV-Assisted Mobile Edge Computing*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2022.3208457.

## TL;DR

Studies **trajectory control and task offloading (TCTO)** for a single UAV that flies a planned trajectory to collect tasks from smart devices, acting either as MEC server or relay to a base station. TCTO is a three-objective problem — minimize task delay, minimize UAV energy, maximize collected tasks — that conflict. Single-objective and single-policy multi-objective RLs can't emit a set of policies for different preferences in one run, so the authors apply **evolutionary multi-objective RL (EMORL)**, improving its multi-task multi-objective PPO by retaining all new learning tasks in the offspring population. The result, **EMORL-TCTO**, yields better non-dominated policy sets.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: One UAV follows a trajectory through smart-device locations, acting either as an MEC server or as a relay to a base station. Online offloading and movement form a multi-objective MDP with task delay, UAV energy, and collected-task throughput objectives.

**Problem & objective**: A three-objective MOMDP seeks a Pareto set for $\min(A_{\mathrm{delay}},E_{\mathrm{UAV}})$ and $\max N_{\mathrm{collected}}$ over trajectory and offloading policies.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV movement | $a_t$ | discrete/continuous action | Direction and displacement selected in slot $t$ |
| Offloading mode | $o_t$ | discrete | Local MEC processing or relay offloading to the BS |
| Policy parameters | $\pi_\theta$ | continuous neural parameters | Policy producing movement and offloading actions |
| Preference vector | $\mathbf w$ | continuous simplex | Relative weighting of delay, energy, and throughput objectives |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | UAV movement stays in the service region and obeys speed/energy limits |
| C2 | Tasks are collected only when the UAV reaches a device and can process or relay them |
| C3 | Offloading and relay capacity determine feasible task completion latency |
| C4 | Each policy produces a valid vectorial reward trajectory for the three objectives |

**Algorithm**: Represent the problem as a vector-reward MOMDP → initialize policy individuals for multiple preference vectors → train multi-objective PPO → retain nondominated policies → apply crossover and Gaussian mutation to policy parameters → return a Pareto policy set.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Song et al. [x] studied trajectory control and task offloading for a UAV that acts as an MEC server or relay for smart-device tasks. They formulated a three-objective multi-objective Markov decision process that minimizes task delay and UAV energy while maximizing collected tasks. EMORL-TCTO extends multi-task multi-objective PPO with an evolutionary population that retains new learning tasks and produces multiple nondominated policies in one run. The resulting policy set spans different preference vectors instead of one fixed scalarization. Experiments report better inverted generational distance, hypervolume, and system metrics than NSGA-II, MOEA/D, EDDPG, ETD3, and the original EMORL in the evaluated instances.

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
