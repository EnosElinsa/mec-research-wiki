---
type: source
title: "Enhancing Energy Efficiency in Wireless-Powered MEC Systems Through Lyapunov-Guided Deep Reinforcement Learning"
authors: ["Bincheng Zhu", "Liang Huang", "Kaikai Chi", "Abdullah Alharbi", "Keping Yu", "Mohsen Guizani"]
year: 2025
url: "https://doi.org/10.1109/TWC.2025.3561167"
venue: "IEEE Transactions on Wireless Communications"
tags: [source, wpt, mec, energy-efficiency, lyapunov, drl, cnn, binary-offloading, fractional-programming]
related:
  - "[[mobile-edge-computing]]"
  - "[[task-offloading]]"
  - "[[lyapunov-optimization]]"
  - "[[wireless-power-transfer]]"
  - "[[binary-vs-partial-offloading]]"
  - "[[fractional-programming-dinkelbach]]"
  - "[[zhou-2018-uav-wireless-powered-mec]]"
  - "[[qin-2025-bcuav-masac]]"
  - "[[lyapunov-guided-drl]]"
modeling_card: required
created: 2026-05-28
updated: 2026-07-16
---

# Enhancing Energy Efficiency in Wireless-Powered MEC Systems Through Lyapunov-Guided Deep Reinforcement Learning

## Citation

Zhu, B., Huang, L., Chi, K., Alharbi, A., Yu, K., & Guizani, M. (2025). *Enhancing Energy Efficiency in Wireless-Powered MEC Systems Through Lyapunov-Guided Deep Reinforcement Learning*. **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2025.3561167.

## TL;DR

Long-term **energy efficiency (EE) maximization** in a [[wireless-power-transfer|WPT]]-MEC network where wireless devices (WDs) harvest energy from a power station and either compute locally or offload to a base-station-side ECS over a binary decision $x_i(k) \in \{0,1\}$. Channels and task arrivals are stochastic.

The original **LSEM** problem is a long-term MINLP with a non-convex fractional objective, queue-stability constraints, and mixed integer + continuous variables. The paper attacks it in two steps:

1. **Transform.** [[fractional-programming-dinkelbach|Fractional programming]] linearizes the EE objective; [[lyapunov-optimization|Lyapunov]] turns the long-term constraints into per-slot virtual-queue penalties.
2. **Decompose.** Per-slot MINLP is split into a **top-problem** (binary offloading $\mathbf x_t$, $2^N$ combinations) and a **sub-problem** (continuous WPT duration, CPU frequencies, transmit powers, time allocation).

The sub-problem is solved with **golden search + KKT + Lagrange dual** (closed-form-ish, low complexity). The top-problem is solved with a **CNN-based actor-critic DRL agent** (LyCNN-DRL), where the CNN is the actor and the sub-problem solution acts as the critic, sidestepping the exponential search.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Multiple wireless devices harvest energy from a power station and either compute locally or offload an indivisible task to a BS-side edge server in each slot; offloading devices share the uplink through TDMA under time-varying channels and stochastic task arrivals.

**Problem & objective**: LSEM, a long-term fractional MINLP, minimizes the reciprocal energy efficiency $\lim_{K\to\infty}\eta(K)=\lim_{K\to\infty}\frac{\sum_t E_{\mathrm{tot}}(t)}{\sum_t D_{\mathrm{tot}}(t)}$ while stabilizing task and virtual-energy queues.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Binary offloading | $x_i(t)$ | Binary | Local execution or complete offloading for device $i$ |
| WPT duration fraction | $a(t)$ | Continuous, nonnegative | Portion of the slot devoted to wireless power transfer |
| Local CPU frequency | $f_i(t)$ | Continuous, $0\le f_i(t)\le f_i^{\max}$ | Local computing rate |
| Offloading energy | $e_i(t)$ | Continuous, nonnegative | Device energy used for uplink offloading |
| Offloading time fraction | $\tau_i(t)$ | Continuous, nonnegative | Uplink time allocated to device $i$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Slot time satisfies $a(t)+\sum_i\tau_i(t)\le1$ |
| C2 | Device energy consumption does not exceed available harvested and battery energy |
| C3 | CPU frequency and offloading variables obey their domains, including $x_i(t)\in\{0,1\}$ |
| C4 | Computation-task queues $Q_i(t)$ and virtual-energy queues $W_i(t)$ remain stable |

**Algorithm**: LyCNN-DRL, apply fractional programming and Lyapunov drift to obtain a per-slot MINLP, let a CNN actor propose binary offloading, solve continuous resources by golden-section search, closed-form CPU allocation, and Lagrange-dual KKT updates, and use that subproblem value as the critic.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zhu et al. [x] studied long-term energy efficiency in a wireless-powered MEC system with time-varying channels, stochastic task arrivals, and binary offloading. They formulated LSEM as a long-term fractional MINLP that jointly optimizes offloading, WPT duration, CPU frequencies, transmit energy, and offloading time under energy and queue-stability constraints. Fractional programming and Lyapunov optimization convert the problem into a per-slot bi-layer structure. LyCNN-DRL uses a CNN actor for near-optimal binary decisions, while golden search, closed-form CPU allocation, and Lagrange-dual KKT updates solve the continuous resource subproblem. Simulations report more than 97% of the reference utility and execution latency of 0.137 seconds for forty devices, compared with 35.184 seconds for LyCD.

## Why CNN, not FC

Authors note that for an $N$-WD system the natural input, channel + queue states, has a structured per-WD feature layout that a CNN exploits. They report meaningful gains over a fully-connected actor of comparable parameter count.

## Findings

- LyCNN-DRL matches the classical iterative solver **LyCD**'s energy efficiency (over **97%** of LyCD's utility; LyCD is only ~3% better) at a fraction of its execution latency: **~50 ms** in a ten-WD network and **137 ms (0.137 s)** even at $N=40$, roughly two orders of magnitude below LyCD's **35.184 s** (~250x lower at $N=40$, per Table III; verbatim).
- It also beats the DRL baselines: the non-Lyapunov-guided **HA2C** (which degrades and fails to converge for $N \ge 10$) and the Lyapunov-guided policy-gradient **LyPG-DRL** (~47.8% worse $\eta$ at $N=10$ and non-convergent for $N \ge 30$). The OFDMA scheme of ref. [26], which leaves the sub-bandwidth of local-computing WDs idle, is cited as motivating prior work rather than benchmarked here.
- Long-term EE under stochastic channels and arrivals is achievable *without* future knowledge; the Lyapunov drift-plus-penalty handles temporal coupling implicitly.

## Limitations / future work

- Binary offloading only; partial offloading is left to future work.
- Single ECS; distributed ECS coordination is not addressed.
- The paper assumes a single power station; multi-station WPT (with coverage trade-offs) is open.

## Cross-link with related sources

- Same Lyapunov template as [[qin-2025-bcuav-masac]]: both papers turn long-term MEC constraints into per-slot subproblems. Qin et al. plug a multi-agent SAC into the per-slot solver; Zhu et al. plug a CNN actor-critic.
- The WPT layer is the distinctive ingredient: energy is *harvested* per-slot instead of static per-UAV. It is the DRL counterpart to the classical/convex WPT-MEC anchor [[zhou-2018-uav-wireless-powered-mec]], which solves the same computation-rate problem without learning.

## Raw artifacts

- `raw/sources/Enhancing_Energy_Efficiency_in_Wireless-Powered_MEC_Systems_Through_Lyapunov-Guided_Deep_Reinforcement_Learning/full.md`
