---
type: source
title: "Enhancing Energy Efficiency in Wireless-Powered MEC Systems Through Lyapunov-Guided Deep Reinforcement Learning"
authors: ["Bincheng Zhu", "Liang Huang", "Kaikai Chi", "Abdullah Alharbi", "Keping Yu", "Mohsen Guizani"]
year: 2025
url: "https://doi.org/10.1109/TWC.2025.3561167"
venue: "IEEE Transactions on Wireless Communications"
tags: [wpt, mec, energy-efficiency, lyapunov, drl, cnn, binary-offloading, fractional-programming]
related:
  - "[[mobile-edge-computing]]"
  - "[[task-offloading]]"
  - "[[lyapunov-optimization]]"
  - "[[wireless-power-transfer]]"
  - "[[binary-vs-partial-offloading]]"
  - "[[fractional-programming-dinkelbach]]"
  - "[[qin-2025-bcuav-masac]]"
created: 2026-05-28
updated: 2026-05-28
---

# Enhancing Energy Efficiency in Wireless-Powered MEC Systems Through Lyapunov-Guided DRL

## Citation

Zhu, B., Huang, L., Chi, K., Alharbi, A., Yu, K., & Guizani, M. (2025). *Enhancing Energy Efficiency in Wireless-Powered MEC Systems Through Lyapunov-Guided Deep Reinforcement Learning*. **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2025.3561167.

## TL;DR

Long-term **energy efficiency (EE) maximization** in a [[wireless-power-transfer|WPT]]-MEC network where wireless devices (WDs) harvest energy from a power station and either compute locally or offload to a base-station-side ECS over a binary decision $x_i(k) \in \{0,1\}$. Channels and task arrivals are stochastic.

The original **LSEM** problem is a long-term MINLP with a non-convex fractional objective, queue-stability constraints, and mixed integer + continuous variables. The paper attacks it in two steps:

1. **Transform.** [[fractional-programming-dinkelbach|Fractional programming]] linearizes the EE objective; [[lyapunov-optimization|Lyapunov]] turns the long-term constraints into per-slot virtual-queue penalties.
2. **Decompose.** Per-slot MINLP is split into a **top-problem** (binary offloading $\mathbf x_t$, $2^N$ combinations) and a **sub-problem** (continuous WPT duration, CPU frequencies, transmit powers, time allocation).

The sub-problem is solved with **golden search + KKT + Lagrange dual** (closed-form-ish, low complexity). The top-problem is solved with a **CNN-based actor-critic DRL agent** (LyCNN-DRL), where the CNN is the actor and the sub-problem solution acts as the critic — sidestepping the exponential search.

## Why CNN, not FC

Authors note that for an $N$-WD system the natural input — channel + queue states — has a 2-D structure (per-WD vector × time-step / per-feature) that a CNN exploits. They report meaningful gains over a fully-connected actor of comparable parameter count.

## Findings

- LyCNN-DRL beats classical iterative MINLP solvers in execution latency by orders of magnitude (sub-millisecond inference vs seconds per iteration), while approaching their EE.
- It also beats prior DRL approaches (e.g. the OFDMA-based scheme that wastes sub-bandwidth on local-computing WDs).
- Long-term EE under stochastic channels and arrivals is achievable *without* future-knowledge — the Lyapunov drift-plus-penalty handles temporal coupling implicitly.

## Limitations / future work

- Binary offloading only; partial offloading is left to future work.
- Single ECS — distributed ECS coordination is not addressed.
- The paper assumes a single power station; multi-station WPT (with coverage trade-offs) is open.

## Cross-link with related sources

- Same Lyapunov template as [[qin-2025-bcuav-masac]] — both papers turn long-term MEC constraints into per-slot subproblems. Qin et al. plug a multi-agent SAC into the per-slot solver; Zhu et al. plug a CNN actor-critic.
- The WPT layer is the distinctive ingredient — energy is *harvested* per-slot instead of static per-UAV. Future curated UAV+WPT papers will fold cleanly into this thread.

## Raw artifacts

- `raw/sources/Enhancing_Energy_Efficiency_in_Wireless-Powered_MEC_Systems_Through_Lyapunov-Guided_Deep_Reinforcement_Learning/full.md`
