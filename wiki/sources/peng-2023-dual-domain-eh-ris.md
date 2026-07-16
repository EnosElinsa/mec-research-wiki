---
type: source
title: "Energy Harvesting Reconfigurable Intelligent Surface for UAV Based on Robust Deep Reinforcement Learning"
authors: ["Haoran Peng", "Li-Chun Wang"]
year: 2023
url: "https://doi.org/10.1109/TWC.2023.3245820"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, uav-mounted-ris, swipt, rf-energy-harvesting, dual-domain-energy-harvesting, sd3, resource-allocation]
related:
  - "[[dual-domain-ris-energy-harvesting]]"
  - "[[softmax-deep-double-deterministic-policy-gradients]]"
  - "[[simultaneous-wireless-information-and-power-transfer]]"
  - "[[rf-energy-harvesting]]"
  - "[[intelligent-reflecting-surface]]"
  - "[[uav-mounted-ris]]"
  - "[[td3]]"
  - "[[ddpg]]"
  - "[[uav-trajectory-control]]"
  - "[[an-2024-multilayer-ris-hap-swipt]]"
  - "[[chen-2025-swipt-mec-sac]]"
  - "[[chhea-2025-irs-uav-swipt-drl]]"
created: 2026-07-13
updated: 2026-07-16
modeling_card: required
---

# Energy Harvesting Reconfigurable Intelligent Surface for UAV Based on Robust Deep Reinforcement Learning

## Citation

Peng, H., & Wang, L.-C. (2023). *Energy Harvesting Reconfigurable Intelligent Surface for UAV Based on Robust Deep Reinforcement Learning*. **IEEE Transactions on Wireless Communications**, 22(10), 6826-6838. DOI: 10.1109/TWC.2023.3245820.

## TL;DR

Extends harvest-transmit-store SWIPT for a UAV-mounted RIS from time splitting alone to joint time-and-space harvesting. During information transmission, selected RIS elements reflect toward users while the remaining elements continue harvesting RF energy. An SD3 controller jointly chooses the harvesting duration, transmit powers, element scheduling, and RIS phases under per-user throughput constraints.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: An AP with $Z$ antennas communicates with $K$ single-antenna users through a UAV-RIS with $M\times N$ reflecting elements because direct links are blocked. Each slot has an EH phase of length $\tau(t)$ and an information phase of length $1-\tau(t)$; in the dual-domain scheme, individual elements can harvest or reflect for a selected user.

**Problem & objective**: Maximize the horizon energy-harvesting efficiency $\bar{\mathcal E}=\max\sum_{t=1}^{T}\mathcal E(t)$ while every user meets $\Gamma_k(t)\ge\Gamma_{\min}$ and the AP and RIS hardware limits hold.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| EH time fraction | $\tau(t)$ | continuous, $[0,1]$ | Time allocated to harvesting in slot $t$ |
| AP power allocation | $P=[p_1,\ldots,p_K]$ | continuous, nonnegative | AP power assigned to users |
| Element scheduling | $\omega_{i,j}^{k}$ | binary | Element $(i,j)$ reflects toward user $k$ |
| RIS phases | $\theta_l^r$ | continuous, $[0,2\pi]$ | Phase of reflecting element $l$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Per-user throughput: $\Gamma_k(t)\ge\Gamma_{\min}$ |
| C2 | Time split: $0\le\tau(t)\le1$ |
| C3 | AP total power: $0\le\sum_k\|V_k\|^2\le p_{\max}$ |
| C4 | Per-user power: $0\le p_k\le p_{\max}'$ |
| C5 | Element assignment is binary: $\omega_{i,j}^{k}\in\{0,1\}$ |
| C6 | One reflection target per element: $\sum_k\omega_{i,j}^{k}\le1$ |
| C7 | Phase range: $\theta_l^r\in[0,2\pi]$ |
| C8 | Unit-modulus reflection: $\lvert e^{j\theta_l^r}\rvert=1$ |

**Algorithm**: Use the dual-domain action $\{\tau,P,\omega,\Theta\}$ in a robust SD3 controller with twin actors and critics, clipped exploration actions, softmax target evaluation, replay, and soft target updates; UAV horizontal placements are supplied by density-aware K-means or Fermat-point design.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Peng and Wang [x] study a UAV-mounted RIS that harvests RF energy while serving users through blocked AP-user links. Their problem maximizes dual-domain harvesting efficiency by jointly selecting the time split, user powers, element-level reflection schedule, and RIS phases under throughput and hardware constraints. A robust SD3 controller handles the mixed continuous and discrete action space with clipped softmax targets and replay, while density-aware and Fermat-point rules provide UAV placements. In the reported experiments, dual-domain SD3 achieves substantially higher harvesting efficiency than time-domain SD3, TD3, and DDPG in both single-user and multi-user cases.

## Problem framing

A battery-powered UAV-RIS can improve blocked access-point-to-user links, but conventional time-domain harvesting makes the whole surface alternate between harvesting and reflection. When only a few users need service, forcing every element to reflect can waste harvesting capacity. Joint time and element-level space splitting improves utilization, but introduces binary scheduling, unit-modulus phases, and tightly coupled communication and energy decisions.

## System model

- A multi-antenna access point serves single-antenna user terminals only through an `M x N` passive [[uav-mounted-ris|UAV-mounted RIS]] because the direct links are blocked.
- Each normalized slot has an energy-harvesting phase of duration `tau(t)` and an information phase of duration `1-tau(t)`.
- In the resource-allocation-based harvest-transmit-store model, all elements harvest during the first phase. During the second, each element either reflects toward at most one user or remains available for harvesting.
- The objective sums harvested-to-incident RF-energy ratios over the horizon, subject to every user's throughput requirement, access-point power limits, binary element scheduling, and continuous unit-modulus phases.
- The model assumes linear RF conversion, ideal continuous RIS phases, perfect cancellation of other RIS-user interference, a fixed UAV altitude, and no battery-state, propulsion, or hover-energy dynamics.

## Method

UAV horizontal positions are supplied by either density-aware K-means placement or a Fermat-point rule; they are not learned as part of the action. The [[softmax-deep-double-deterministic-policy-gradients|SD3]] action contains the harvesting fraction, user power allocations, binary element schedules, and RIS phases.

SD3 keeps two actors and two critics. Like [[td3|TD3]], its target uses the smaller twin-critic value and clipped nearby target actions. It then applies a softmax expectation over sampled nearby actions to reduce the underestimation introduced by a strict minimum while retaining protection against DDPG-style overestimation. The reward equals harvesting efficiency only when every user meets the throughput threshold; otherwise it is zero.

## Key findings

- In the detailed single-user results, dual-domain SD3 averages 64.2% harvested-energy efficiency, compared with 58.5% for TD3, 30.4% for DDPG, and 67.6% for exhaustive search.
- In the detailed three-user results, dual-domain SD3 averages 55.0%, compared with 52.9% for TD3, 29.6% for DDPG, and 67.2% for exhaustive search.
- Time-domain-only SD3 averages 22.5% in the single-user case and 23.2% in the three-user case, showing that the larger gain comes from spatial element partitioning rather than the DRL backbone alone.
- The contribution paragraph instead states 62.5% and 44.6% for the single- and multiple-user cases. Those values conflict with the detailed result tables and are not treated as interchangeable.
- Density-aware and Fermat-point placements are described as producing very similar test performance, including on user trajectories different from training.

## Limitations / future work

Evidence is simulation-only. The endurance claim is based on harvesting efficiency rather than an explicit battery trajectory or measured flight-time extension, and UAV propulsion is omitted. The binary scheduling action is derived from a continuous policy, but the parse does not specify the discretization rule. Robustness is evaluated through changed user trajectories and two placement rules, not through channel-estimation errors or hardware impairments. Multi-UAV-RIS/user association is deferred. One contribution sentence incorrectly calls the sustained non-convex formulation convex, and the prose description of the QoS gate conflicts with its all-users-feasible product equation.

## Relation to the corpus

This source adds [[dual-domain-ris-energy-harvesting]] to the corpus's [[simultaneous-wireless-information-and-power-transfer|SWIPT]] line. It differs from [[an-2024-multilayer-ris-hap-swipt]], which uses a multilayer refracting receiver and power splitting at HAP scale, and from [[chen-2025-swipt-mec-sac]], which applies SWIPT to UAV-assisted MEC. [[chhea-2025-irs-uav-swipt-drl]] is the closest UAV-IRS-SWIPT learning neighbor, while this paper's distinct algorithm contribution is the [[softmax-deep-double-deterministic-policy-gradients|SD3]] treatment of twin-critic estimation bias.

## Raw artifacts

- Parse: `raw/sources/Energy_Harvesting_Reconfigurable_Intelligent_Surface_for_UAV_Based_on_Robust_Deep_Reinforcement_Learning/Energy_Harvesting_Reconfigurable_Intelligent_Surface_for_UAV_Based_on_Robust_Deep_Reinforcement_Learning.md`
- Origin PDF: `raw/sources/Energy_Harvesting_Reconfigurable_Intelligent_Surface_for_UAV_Based_on_Robust_Deep_Reinforcement_Learning/Energy_Harvesting_Reconfigurable_Intelligent_Surface_for_UAV_Based_on_Robust_Deep_Reinforcement_Learning.pdf`
- Figures: `raw/sources/Energy_Harvesting_Reconfigurable_Intelligent_Surface_for_UAV_Based_on_Robust_Deep_Reinforcement_Learning/images/`
