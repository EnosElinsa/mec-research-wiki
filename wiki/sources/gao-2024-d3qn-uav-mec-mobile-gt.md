---
type: source
title: "UAV-Assisted MEC System With Mobile Ground Terminals: DRL-Based Joint Terminal Scheduling and UAV 3D Trajectory Design"
authors: ["Yunfei Gao", "Xiaopeng Yuan", "Dingcheng Yang", "Yulin Hu", "Yue Cao", "Anke Schmeink"]
year: 2024
url: "https://doi.org/10.1109/TVT.2024.3367624"
venue: "IEEE Transactions on Vehicular Technology (IEEE TVT)"
tags: [source, uav-trajectory-control, deep-reinforcement-learning, dueling-dqn, ddqn, obstacle-avoidance, probabilistic-los-channel, post-disaster-mec]
related:
  - "[[uav-trajectory-control]]"
  - "[[ddqn]]"
  - "[[dueling-dqn]]"
  - "[[deep-q-network]]"
  - "[[blockage-aware-channel-model]]"
  - "[[collision-avoidance-mgi]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[post-disaster-mec]]"
  - "[[gauss-markov-mobility-model]]"
  - "[[van-hasselt-2016-double-dqn]]"
  - "[[zhan-2020-completion-time-energy-uav-mec]]"
  - "[[dingcheng-yang]]"
created: 2026-06-02
updated: 2026-07-14
---

# UAV-Assisted MEC System With Mobile Ground Terminals: DRL-Based Joint Terminal Scheduling and UAV 3D Trajectory Design

## Citation

Gao, Y., Yuan, X., Yang, D., Hu, Y., Cao, Y., & Schmeink, A. (2024). *UAV-Assisted MEC System With Mobile Ground Terminals: DRL-Based Joint Terminal Scheduling and UAV 3D Trajectory Design*. **IEEE Transactions on Vehicular Technology**, 73(7), 10164–10180. DOI: 10.1109/TVT.2024.3367624. (Manuscript received 28 September 2023; accepted 23 January 2024; date of publication 27 March 2024; date of current version 16 July 2024.)

## TL;DR

Considers a UAV-assisted MEC network in a **3D urban post-disaster** scenario with multiple **mobile** ground terminals (GTs). A single UAV's mission is to collect computation tasks from a set of **source** GTs, process them, and transmit the decision results to a set of **destination** GTs, minimizing the **total operation time** (offloading + computation + decision transmission). It jointly designs the **UAV's 3D trajectory** and the **communication scheduling** to/from different GTs, under practical assumptions: GT mobility, **obstacle avoidance** to 3D buildings, the possibility of the UAV flying *among* buildings (altitude below building height), and a **probabilistic LoS** channel. The non-convex, dynamic problem is transformed into an **MDP** and solved with a **multi-step dueling double DQN (D3QN)** — dueling network + multi-step bootstrapping on top of DDQN.

## Problem framing

UAV-assisted MEC benefits from trajectory design, but prior trajectory works assume a simplified LoS-dominant channel and a **2D** trajectory (fixed altitude). A **3D** trajectory promises higher performance by exploiting altitude freedom, but adds two challenges: simultaneous horizontal + vertical motion raises complexity, and 3D flight is more sensitive to environment detail (altitude variation, multi-dimensional propagation, building blockage), demanding a probabilistic-LoS model. Moreover, most prior works assume **fixed** GTs and assume the UAV flies *above* buildings, ignoring obstacle avoidance. For practical multi-mobile-GT MEC with a 3D feasible flying area and obstacle avoidance, jointly designing the UAV 3D trajectory plus communications scheduling (offloading + decision transmission) was an open problem. The dynamic GT mobility makes analytical methods (convex optimization, matching theory) intractable, and 3D's enlarged exploration space slows convergence — motivating a modified RL approach where the UAV agent learns the GTs' random-mobility model through interaction.

## System model

- **Mission.** UAV collects tasks from source GTs (data offloading), computes joint decisions, and transmits results to destination GTs. Objective: minimize **total time cost** = task offloading + computation + decision transmission.
- **Practical assumptions.** GTs are **always moving** (random mobility, including different mobility models); 3D buildings impose **obstacle avoidance**; the UAV may fly *between* buildings (low altitude, lower than building heights) in emergency/military scenarios to approach GTs and boost transmission; a **probabilistic LoS** channel models building blockage.
- **Feasible domain.** An **unrestricted** feasible flying domain is adopted while obstacle avoidance to 3D buildings is guaranteed; the paper studies how UAV flying-height/area limits affect the design.
- **Decisions.** UAV 3D trajectory + the scheduling of which GT communicates (offloading from source GTs, decision transmission to destination GTs) per step. Non-convex and analytically intractable due to GT-mobility randomness and many coupled variables.

## Method

- **MDP transformation.** The problem is recast as a Markov decision process with the UAV as the agent exploring/improving its 3D-trajectory + GT-scheduling policy through environment interaction.
- **Multi-step D3QN.** A modified DDQN with (i) a **dueling network** (separating state-value and advantage) to boost system performance and (ii) **multi-step bootstrapping** (with a suitable step) to accelerate convergence relative to traditional DDQN — together the **multi-step dueling DDQN (D3QN)** method. A **greedy scheme** handles mobile-GT scheduling.
- **Convergence parameter.** A step-related parameter σ trades convergence speed against UAV mission-completion time; too-small σ raises complexity and risks local optima / oscillations, while the method still converges across σ values.

## Key findings

- The **3D trajectory design outperforms a 2D** one (exploiting altitude freedom).
- The design is **robust** across different GT mobility models and different UAV flying-height/area limits.
- **Unrestricted feasible flying domains** (UAV allowed among buildings) are superior to restricted ones for the UAV flight.
- Convergence is confirmed; the σ hyperparameter is a documented trade-off between convergence speed and mission completion time. Specific numeric margins are figure-derived; treat exact values as indicative.

## Limitations / future work

Evaluation is **simulation-only**, with a **single** UAV. The decision is split: a learned policy for trajectory plus a **greedy** scheme for GT scheduling (not jointly learned). Explicit future-work statements are `not in parse`.

## Relation to the corpus

A **DRL UAV-MEC** entry distinguished by three practical features rarely combined in the corpus: a genuine **3D** trajectory, **mobile** GTs, and **obstacle avoidance among buildings** under a probabilistic-LoS / [[blockage-aware-channel-model|blockage-aware]] channel — a [[post-disaster-mec|post-disaster]] urban setting. Its **multi-step D3QN** builds on the [[dueling-dqn|dueling]] + [[ddqn|double-DQN]] lineage anchored by [[van-hasselt-2016-double-dqn]]. The source→compute→destination time-minimization structure contrasts with the classical-optimization fixed-wing **completion-time-vs-energy** design of [[zhan-2020-completion-time-energy-uav-mec]] (which uses path discretization + AO + SCA rather than DRL), and its mobile-GT modeling complements the [[gauss-markov-mobility-model]] used elsewhere in the corpus.

## Raw artifacts

- `raw/sources/UAV-Assisted_MEC_System_With_Mobile_Ground_Terminals_DRL-Based_Joint_Terminal_Scheduling_and_UAV_3D_Trajectory_Design/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
