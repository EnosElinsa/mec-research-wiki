---
type: source
title: "UAV-Assisted Task Offloading in Vehicular Edge Computing Networks"
authors: ["Xingxia Dai", "Zhu Xiao", "Hongbo Jiang", "John C. S. Lui"]
year: 2024
url: "https://doi.org/10.1109/TMC.2023.3259394"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, vehicular-mec, uav-mec, lyapunov-optimization, markov-approximation, task-offloading, online-algorithm]
related:
  - "[[vehicular-mec]]"
  - "[[mobile-edge-computing]]"
  - "[[lyapunov-optimization]]"
  - "[[markov-approximation]]"
  - "[[task-offloading]]"
  - "[[uav-enabled-its]]"
  - "[[yang-2022-stochastic-uav-mec-lyapunov]]"
  - "[[sun-2023-bargain-match-vec]]"
  - "[[ma-2025-pdqn-vehicular-mec]]"
  - "[[zhu-xiao]]"
created: 2026-05-31
updated: 2026-07-14
---

# UAV-Assisted Task Offloading in Vehicular Edge Computing Networks

## Citation

Dai, X., Xiao, Z., Jiang, H., & Lui, J. C. S. (2024). *UAV-Assisted Task Offloading in Vehicular Edge Computing Networks*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2023.3259394. (Manuscript received 11 Oct 2021; date of publication 20 Mar 2023; date of current version 6 Mar 2024.)

## TL;DR

Introduces a **UAV** to relieve **overloaded road-side units (RSUs)** in vehicular edge computing (VEC), especially in urban aggregation areas. The paper formulates a novel **online UAV-assisted vehicular task offloading** problem to **minimize vehicular task delay under a long-term UAV energy constraint**. The long-term energy constraint is decoupled via **Lyapunov optimization** (so the problem is solved in real time without future information), and a **Markov-approximation**-based construction finds close-to-optimal UAV-assisted offloading strategies, with a mathematical analysis of the performance.

## Problem framing

VEC pushes cloud resources to vehicular network edges (RSUs), but RSUs are prone to **overload** in dense urban areas, compromising offloading performance. Vehicular applications are computing-hungry and delay-sensitive (e.g. an AR app needs ~40 billion cycles within 10 ms), and on-board processing strains vehicle compute/battery and driving range. Introducing a UAV to absorb excess workload from overloaded RSUs is the proposed remedy — under the practical constraint that the UAV has a limited long-term energy budget.

## System model

- **Actors.** Vehicles, RSUs (potentially overloaded), and a UAV processing the excess RSU workload ([[vehicular-mec]], [[uav-enabled-its]]).
- **Objective.** Minimize the time-average vehicular task delay subject to the UAV's long-term energy budget.
- **Online reformulation.** [[lyapunov-optimization]] decouples the long-term energy constraint into a real-time solvable problem (an energy deficit/virtual queue).

## Method

- **Lyapunov optimization** transforms the long-term problem to a per-slot real-time problem.
- A **Markov chain built via Markov-approximation optimization** finds the close-to-optimal UAV-assisted offloading strategies ([[markov-approximation]]).
- A rigorous theoretical analysis proves the algorithm achieves close-to-optimal solutions.

## Key findings

- Simulations show the method significantly **reduces vehicular task delay** under the long-term UAV energy budget, across system parameters such as the energy budget and computation workloads (qualitative; specific curves in the paper).
- A multi-UAV extension discussion (Fig. 10): more UAVs reduce vehicular task delay but consume more energy (especially hovering energy), and deployment overhead should be considered in real-world scenarios (from the parse, reported qualitatively).

## Limitations / future work

The authors flag extending the UAV's role to **anomaly detection** on collected vehicular information, and studying the **impact of severe weather** on UAV navigation for offloading. Results are simulation-based.

## Relation to the corpus

A **Lyapunov + Markov-approximation online VEC** entry. It shares the Lyapunov online backbone with [[yang-2022-stochastic-uav-mec-lyapunov]] but uses a distinctive **Markov-approximation** per-slot solver (the wiki's first). It sits in the vehicular-MEC track alongside the game-theoretic [[sun-2023-bargain-match-vec]] and the DRL [[ma-2025-pdqn-vehicular-mec]], distinguished by its UAV-relieves-overloaded-RSU framing. Note: distinct from the marine-welfare paper by **Minghui** Dai ([[dai-2024-multiuav-marine-welfare]]) — different first author (Xingxia Dai), domain, and method. Introduces [[markov-approximation]]; reinforces [[lyapunov-optimization]] and [[vehicular-mec]].

## Raw artifacts

- `raw/sources/UAV-Assisted_Task_Offloading_in_Vehicular_Edge_Computing_Networks/full.md`
- Original PDF and extracted figures in the same folder.
