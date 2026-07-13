---
type: concept
title: Lyapunov Optimization (drift-plus-penalty)
tags: [optimization, queueing, online-control]
related:
  - "[[zhan-2026-star-ris-aerial-monitoring]]"
  - "[[qin-2025-bcuav-masac]]"
  - "[[lyapunov-guided-drl]]"
  - "[[he-2026-dt-sagimec-lae]]"
  - "[[ma-2026-mean-field-green-aec]]"
  - "[[liao-2026-aoi-ris-uav-usv-mec]]"
  - "[[sheng-2025-ris-online-uav-mec]]"
  - "[[feng-2026-prediction-service-migration]]"
  - "[[tang-2026-hg-maddpg-uav-rescue]]"
created: 2026-05-28
updated: 2026-07-14
---

# Lyapunov Optimization (drift-plus-penalty)

A Neely-style technique for online control under long-term constraints. The recipe:

1. Map every long-term constraint $\bar g \le 0$ into a **virtual queue** $Z(t+1) = \max\{Z(t) + g(t), 0\}$.
2. Define the Lyapunov function $L(\Theta) = \frac{1}{2}\sum Z_i^2$ over all virtual queues.
3. At each slot, minimize the **drift-plus-penalty** upper bound:
   $$\Delta L(\Theta(t)) - V \cdot f(t)$$
   where $f(t)$ is the per-slot reward / utility and $V$ trades off optimality against constraint slack.

Standard guarantee: under mild conditions, time-averaged constraint violation is $O(1/V)$ and time-averaged optimality gap is $O(V)$ — i.e. tunable.

## Why MEC research keeps reaching for it

- Long-term queue stability constraints are *exactly* what arrive in MEC: per-slot data backlog, per-slot energy budget, per-slot delay caps that the system should respect on average.
- It decouples the long-term planning from the per-slot decision, making per-slot subproblems tractable (often convex or near-convex).
- It composes cleanly with DRL — the per-slot subproblem can be solved by an RL agent while Lyapunov's virtual queues take care of the temporal coupling. This **Lyapunov + DRL** hybrid is common enough across the corpus to have its own methodology page: [[lyapunov-guided-drl]].

## In this wiki

[[qin-2025-bcuav-masac]] uses Lyapunov to split a long-term sensing-rate maximization with queue-delay and block-creation-delay caps into three per-slot subproblems (CVX + MASAC + DOA). [[he-2026-dt-sagimec-lae]] uses the same online-control pattern to convert a long-term SAGIMEC satellite/offloading/resource/trajectory problem into per-slot decisions. [[ma-2026-mean-field-green-aec]] combines Lyapunov control with [[mean-field-game]] modeling to set an energy valuation signal for long-term energy balance in green aerial edge computing. [[liao-2026-aoi-ris-uav-usv-mec]] uses a mixed linear-quadratic Lyapunov framework for AoI-aware RIS-assisted UAV-USV MEC. [[sheng-2025-ris-online-uav-mec]] applies drift-plus-penalty control to RIS-assisted UAV-MEC with mobile users, random task arrivals, queue stability, outage constraints, and finite UAV energy. [[feng-2026-prediction-service-migration]] uses a Lyapunov virtual queue to enforce a long-term service-migration cost budget while MADDPG controls UAV trajectories and service placement. [[tang-2026-hg-maddpg-uav-rescue]] uses an energy queue to convert long-term rescue-UAV energy constraints into per-slot HG-MADDPG decisions. The drift-plus-penalty template recurs across the corpus's online-control sources (e.g. [[dai-2024-uav-vehicular-offloading-lyapunov]], [[yang-2022-stochastic-uav-mec-lyapunov]], [[wang-2024-maritime-eh-jcora]], [[mao-2016-lodco-eh-mec-offloading]]).
