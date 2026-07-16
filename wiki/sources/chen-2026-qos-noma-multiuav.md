---
type: source
title: "QoS-Oriented Task Offloading in NOMA-Based Multi-UAV Cooperative MEC Systems"
authors: ["Peipei Chen", "Lailong Luo", "Deke Guo", "Jiaju Wu", "Kaikai Chi", "Chenggang Yan", "Xudong Dong"]
year: 2026
url: "https://doi.org/10.1109/TWC.2025.3593884"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, uav-mec, noma, task-offloading, task-priority, soft-actor-critic, qos]
related:
  - "[[noma]]"
  - "[[task-priority-in-mec]]"
  - "[[dynamic-qos-constraints]]"
  - "[[soft-actor-critic]]"
  - "[[task-offloading]]"
  - "[[uav-trajectory-control]]"
  - "[[qoe-modeling-mec]]"
created: 2026-07-07
updated: 2026-07-16
modeling_card: required
---

# QoS-Oriented Task Offloading in NOMA-Based Multi-UAV Cooperative MEC Systems

## Citation

Chen, P., Luo, L., Guo, D., Wu, J., Chi, K., Yan, C., & Dong, X. (2026). *QoS-Oriented Task Offloading in NOMA-Based Multi-UAV Cooperative MEC Systems*. **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2025.3593884. DOI/venue/year are parse-silent at the top level and verified against a title-matched Crossref/IEEE DOI record.

## TL;DR

Formulates QoS-oriented task offloading for a NOMA-based multi-UAV cooperative MEC system. Tasks carry data size, CPU cycles, deadline, and priority; the objective maximizes average system utility by jointly optimizing UAV 3D trajectories, mobile-user association, offloading ratios, and UAV compute allocation. The proposed ISAC algorithm combines Lagrange duality with an improved [[soft-actor-critic]] loss to improve exploration and avoid local minima.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A slotted NOMA-based cooperative MEC network contains $K$ mobile users and $L$ UAV edge servers. Users offload through shared subchannels, UAVs apply successive interference cancellation, and each task is characterized by data size, CPU cycles, a delay threshold, and a high- or low-priority label.

**Problem & objective**: Problem (29) is a constrained nonconvex long-term utility maximization, $\max_{\Lambda,\mathbf Q,\mathcal A,\mathcal F}\lim_{N\to\infty}\frac{1}{N}\sum_{k=1}^{K}\sum_{n=1}^{N}U_k(n)$, where $U_k(n)$ applies different post-deadline penalties to high- and low-priority tasks.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| MU association | $\alpha_{kl}(n)$ | Binary, $\{0,1\}$ | Associates user $k$ with UAV $l$ in slot $n$ |
| UAV trajectory | $\mathbf q_l(n)=[x_l(n),y_l(n),z_l(n)]$ | Continuous within the service region and altitude bounds | Sets each UAV's 3D position |
| Offloading ratio | $a_k(n)$ | Continuous, $[0,1]$ | Fraction of user $k$'s task offloaded to a UAV |
| UAV computation allocation | $f_{kl}(n)$ | Continuous, $f_{kl}(n)\geq 0$ | CPU rate allocated by UAV $l$ to user $k$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Offloading fraction: $0\leq a_k(n)\leq 1$ |
| C2 | UAV computation capacity: $\sum_{k=1}^{K}f_{kl}(n)\leq F_l$ |
| C3 | Mobility: $\bar d_l(n)\leq\bar d_{\max}^{h}$, $z_{\min}\leq z_l(n)\leq z_{\max}$, and $\Delta z_l(n)\leq\bar d_{\max}^{v}$ |
| C4 | Coverage and association: $\alpha_{kl}(n)r_{kl}(n)\leq R_l^{\max}(n)$ and $\alpha_{kl}(n)\in\{0,1\}$ |

**Algorithm**: Apply Lagrange duality to transform the constrained MDP, use state $s_n=[\mathbf M_k(n),\mathbf q_l(n),\zeta_k(n),\gamma_{kl}(n)]$ and utility reward $r_n=\sum_k U_k(n)$, then train the improved soft actor-critic policy with the perturbed Q-network loss $J_Q(\theta+\varepsilon)+\frac{\varphi}{2}\lVert\theta\rVert_2^2$ and alternating updates of $\varepsilon$ and $\theta$.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Chen et al. [x] studied QoS-oriented task offloading in a NOMA-based multi-UAV cooperative MEC system with high- and low-priority tasks. They maximized long-term average system utility by jointly optimizing UAV 3D trajectories, mobile-user associations, task offloading ratios, and computation allocation under mobility, coverage, association, and resource constraints. Their solution applied Lagrange duality and then an improved soft actor-critic algorithm whose Q-network loss includes a perturbation term. Simulations reported better convergence, offloading transmission rate, task completion rate, and system utility than SAC, PPO, and DDPG.

## Problem

Existing UAV-MEC offloading methods often minimize delay, energy, cost, or throughput without explicitly differentiating high-priority and low-priority tasks. In emergency, navigation, and AR-like applications, missed deadlines have priority-dependent consequences. The paper therefore defines utility functions that penalize high-priority deadline violations sharply while allowing low-priority tasks to degrade more gradually.

## System model

The NMCM system contains multiple mobile users and multiple UAVs over slotted time. Each mobile user generates a task tuple `{D_k(n), C_k(n), omega_k(n), E_k(n)}` for transmitted data size, CPU cycles, maximum delay threshold, and priority level. Users offload via NOMA to UAVs; UAV receivers apply successive interference cancellation. A central controller aggregates beacon information and decides UAV association, trajectories, offloading ratios, and computation resource allocation.

## Method

The paper first applies Lagrange duality to transform the constrained nonconvex problem into an unconstrained dual form. It then proposes ISAC, an improved SAC variant whose Q-network loss includes a perturbation term intended to expand exploration beyond local minima. The reward is tied to system utility while the transformed constraints guide feasible trajectory, association, offloading, and resource decisions.

## Key findings

- ISAC is reported to outperform PPO, SAC, and DDPG on offloading transmission rate at varying bandwidths and task sizes.
- Task completion rate improves as bandwidth increases, but the parse notes that around 50 MHz the offloading rate and completion rate saturate for 1 MB tasks.
- For larger task sizes under fixed 20 MHz bandwidth, offloading performance drops for all methods, but ISAC remains above PPO, SAC, and DDPG in resource-limited settings.
- System utility rises with the number of UAVs, and ISAC is reported to maintain stronger performance as the number of mobile users grows; PPO and DDPG drop sharply when the user count exceeds 40 in the reported experiment.
- The conclusion states that ISAC improves convergence performance, offloading transmission rates, task completion rates, and system utility relative to benchmark algorithms.

## Limitations / future work

The paper does not model high-speed-UAV Doppler effects because of modeling complexity. The conclusion states future research will explore multi-modal learning and aggregation techniques for multi-UAV task offloading.

## Relation to the corpus

This source joins [[task-priority-in-mec]], [[dynamic-qos-constraints]], [[noma]], and [[task-offloading]] in a single multi-UAV formulation. It is close to [[hao-2024-clp-multiuav-priority-offloading]] and [[wang-2026-llm-qos-multiuav-resource]] on priority/QoS-aware UAV-MEC control, but its technical distinction is the Lagrangian-dual plus improved-SAC treatment of constrained NOMA offloading.

## Raw artifacts

- `raw/sources/QoS-Oriented Task Offloading in NOMA-Based Multi-UAV Cooperative MEC Systems/QoS-Oriented Task Offloading in NOMA-Based Multi-UAV Cooperative MEC Systems.md`
- Original PDF and extracted figures (`images/`) in the same folder.
