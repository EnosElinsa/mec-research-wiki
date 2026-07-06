---
type: source
title: "Decentralized Learning for Multi-UAV Rail-Line Inspection With Imperfect Information: A Fictitious Self-Play Approach"
authors: ["Yin Jia", "Li Zhu", "F. Richard Yu", "Bo Ai", "Tao Tang"]
year: 2026
url: "https://doi.org/10.1109/TITS.2026.3695610"
venue: "IEEE Transactions on Intelligent Transportation Systems (IEEE T-ITS)"
tags: [source, multi-uav, rail-line-inspection, imperfect-information, stochastic-game, potential-game, fictitious-self-play, q-learning, task-offloading]
related:
  - "[[stochastic-game]]"
  - "[[potential-game]]"
  - "[[fictitious-self-play]]"
  - "[[nash-equilibrium]]"
  - "[[multi-agent-q-learning]]"
  - "[[task-offloading]]"
  - "[[uav-enabled-its]]"
  - "[[communication-constrained-marl]]"
  - "[[li-2025-stochastic-game-uav-swarm]]"
  - "[[chen-2024-ulse-game]]"
  - "[[game-theoretic-offloading-formulations]]"
created: 2026-07-06
updated: 2026-07-06
---

# Decentralized Learning for Multi-UAV Rail-Line Inspection With Imperfect Information: A Fictitious Self-Play Approach

## Citation

Jia, Y., Zhu, L., Yu, F. R., Ai, B., & Tang, T. (2026). *Decentralized Learning for Multi-UAV Rail-Line Inspection With Imperfect Information: A Fictitious Self-Play Approach*. **IEEE Transactions on Intelligent Transportation Systems**, 1-18. DOI: 10.1109/TITS.2026.3695610.

## TL;DR

A decentralized game-theoretic learning framework for multi-UAV rail-line inspection when complete global state is unavailable. The paper models UAV task offloading / resource allocation as a stochastic game with imperfect information, proves the game is an exact potential game, and proposes U-FSP (UAV Fictitious Self-Play): each UAV uses local observations plus a belief over aggregate behavior, alternating Q-learning best responses with policy averaging. Simulations show lower energy, delay, congestion, and Nash gap; a small two-UAV real-world experiment validates the imperfect-information assumption and shows better completion rate / time than DQM.

## Problem

Rail-line inspection is corridor-shaped, long-range, and communication-limited. A UAV cannot directly observe another UAV's battery level, queue length, computational load, or task progress; forwarded peer-state packets can be unavailable, delayed, or stale. Centralized training / complete-information MARL therefore mismatches the deployment assumptions. The paper targets decentralized offloading among local processing, cooperative UAV processing, and wayside edge processing under limited information.

## System model

- **Task modes:** local processing, cooperative processing, and wayside edge offloading.
- **Private state:** each UAV observes its own battery, task load, computation status, and progress, but not the current private states of peer UAVs.
- **Costs / rewards:** progress reward, success reward, time cost, energy cost, and congestion / queueing cost for shared cooperative and edge resources.
- **Information:** decisions use local observations and lightweight aggregate feedback rather than direct peer private state.
- **Objective:** maximize each UAV's expected discounted utility while reducing energy, completion delay, and resource congestion.

## Method

The paper formulates the inspection process as a stochastic game under imperfect information and augments each UAV's MDP with a belief distribution over other UAV behavior. U-FSP alternates two stages: best-response learning with Q-learning against the current belief, and averaged-strategy learning using empirical action frequencies. The game is proven to be an exact potential game with social welfare as the potential function, and the U-FSP process is theoretically guaranteed to converge to the set of Nash equilibria under the paper's assumptions.

## Key findings

- The Nash gap decreases while social welfare rises and stabilizes in the reported training curves, supporting convergence toward a Nash equilibrium.
- For task-type completion rates, U-FSP reaches 0.877 for Task1, 0.853 for Task2, and 0.915 for Task3 in the last 1000 episodes; it is more balanced than DQM, which prioritizes the high-immediate-reward task.
- The belief mechanism is important: Table II reports U-FSP social welfare 10518.88, task completion 0.900, average task time 15.16, average energy 75.89, and Nash gap 0.034; removing belief degrades all five metrics.
- In the two-UAV real-world deployment experiment, U-FSP achieves **83.7%** task completion and **17.7 s** average completion time, versus DQM's **61.3%** and **21.7 s**, averaged over five real-flight experiments of 70 decision steps each.
- Runtime logs in the real-world experiment show peer private state is not directly accessible and peer packets can be out-of-range, delayed, newly delivered but temporally mismatched, or stale cached data.

## Limitations / future work

The real-world experiment is small-scale: two UAVs in a simplified corridor-like setup with a ground-side edge node, not a full rail-line deployment. The paper notes that unreliable links, stale peer information, and practical rail-system deployment issues remain challenges. Simulation results are richer than the hardware validation, so large-scale operational robustness is still not established.

## Relation to the corpus

This source adds [[fictitious-self-play]] and imperfect-information equilibrium learning to the wiki's game-theoretic offloading family. It is closest to [[li-2025-stochastic-game-uav-swarm]] because both use stochastic-game reasoning for UAV swarms, but U-FSP explicitly rejects complete global information and uses belief-augmented learning. It also complements [[chen-2024-ulse-game]] and [[zhang-2026-uav-task-path-lu-its]] in the [[potential-game]] line, while its rail-line inspection setting connects the UAV-MEC corpus to [[uav-enabled-its]] and real-world deployment evidence.

## Raw artifacts

- `raw/sources/Decentralized Learning for Multi-UAV Rail-Line Inspection With Imperfect Information A Fictitious Self-Play Approach/Decentralized Learning for Multi-UAV Rail-Line Inspection With Imperfect Information A Fictitious Self-Play Approach.md`
- Original PDF and extracted figures (`images/`) in the same folder.
