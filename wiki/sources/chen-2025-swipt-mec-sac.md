---
type: source
modeling_card: required
title: "Joint Resource Management for Energy-Efficient UAV-Assisted SWIPT-MEC: A Deep Reinforcement Learning Approach"
authors: ["Yue Chen", "Hui Kang", "Jiahui Li", "Geng Sun", "Boxiong Wang", "Jiacheng Wang", "Cong Liang", "Shuang Liang", "Dusit Niyato"]
year: 2025
url: "https://doi.org/10.1109/JIOT.2025.3574332"
venue: "IEEE Internet of Things Journal (IEEE IoT-J)"
tags: [source, uav-mec, swipt, wireless-power-transfer, soft-actor-critic, energy-efficiency, drl]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[wireless-power-transfer]]"
  - "[[rf-energy-harvesting]]"
  - "[[masac]]"
  - "[[hybrid-action-decision-making]]"
  - "[[uav-charging-scheduling]]"
  - "[[zhu-2025-lycnn-drl-wpt-mec]]"
  - "[[hsu-2025-drl-hues-hap-noma]]"
created: 2026-05-29
updated: 2026-07-16
---

# Joint Resource Management for Energy-Efficient UAV-Assisted SWIPT-MEC: A Deep Reinforcement Learning Approach

## Citation

Chen, Y., Kang, H., Li, J., Sun, G., Wang, B., Wang, J., Liang, C., Liang, S., & Niyato, D. (2025). *Joint Resource Management for Energy-Efficient UAV-Assisted SWIPT-MEC: A Deep Reinforcement Learning Approach*. **IEEE Internet of Things Journal**. DOI: 10.1109/JIOT.2025.3574332.

## TL;DR

A directional-antenna-enhanced UAV that acts as both base station and MEC server, providing **simultaneous wireless information and power transfer (SWIPT)** plus computation to energy-constrained ground IoT terminals in infrastructure-free areas. The paper formulates a **bi-objective** problem (minimize system energy consumption; maximize terminal battery energy) with charging fairness, reformulates it as an MDP with a hybrid solution space, and solves it with an improved **soft actor-critic** (SAC-SK) featuring an action-simplification mechanism plus boundary-penalty and charging-reward designs.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: One fixed-altitude UAV with a directional antenna acts as base station, MEC server, and SWIPT energy source for fixed ground IoT terminals with Bernoulli task arrivals, nonlinear energy harvesting, binary whole-task offloading, and slotted UAV motion.

**Problem & objective**: Problem P is a nonconvex mixed-integer bi-objective program that seeks $\min_{\mathbf v,\boldsymbol\theta,\mathbf O}\sum_tE_{total}(t)$ and $\max_{\mathbf v,\boldsymbol\theta,\mathbf O}\sum_tF_{energy}(t)$, balancing total system energy against fairness-weighted terminal battery energy.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Task offloading | $o_i^t$ | Binary, $\{0,1\}$ | Selects local execution or complete UAV offloading for terminal $i$. |
| UAV velocity | $v(t)$ | Continuous, $[0,v_{\max}]$ | Sets UAV movement speed in slot $t$. |
| UAV direction | $\theta(t)$ | Continuous, $[0,2\pi]$ | Sets UAV movement angle in slot $t$. |
| Hybrid MDP action | $a_t=\{\mathcal O^t,v^t,\theta^t\}$ | Mixed discrete-continuous domain | Jointly schedules all terminal offloads and the UAV motion command. |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | The UAV starts at $p_u^0=(0,0)$, with $0\le v(t)\le v_{\max}$ and $0\le\theta(t)\le2\pi$. |
| C2 | SWIPT splitting and battery limits require $0<\eta\le1$ and $E_{\min}\le E_i(t)\le E_{\max}$. |
| C3 | Local or offloaded execution must finish in one slot as specified by (19e). |
| C4 | Both downlink and uplink rates satisfy $\min\{R_{u\to i},R_{i\to u}\}\ge R_{\min}$. |
| C5 | Local CPU feasibility requires $C_iD_{i,p}^t\le\tau f_i$, and local or transmit energy cannot reduce a terminal below its protected reserve. |

**Algorithm**: The model is converted to an MDP whose scalar reward combines normalized energy objectives, boundary penalties, terminal-access bias, and low-battery charging rewards; SAC-SK then applies action simplification, SRU temporal encoding, and a KAN-based function approximator to learn the maximum-entropy hybrid policy.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Chen et al. [x] studied joint whole-task offloading and UAV trajectory control for a directional-antenna SWIPT-MEC system serving energy-limited IoT terminals in infrastructure-free areas. They formulated a mixed discrete-continuous bi-objective problem that minimizes UAV-plus-terminal energy while maximizing Jain-fairness-weighted terminal battery energy under timing, rate, battery, CPU, and flight constraints. Their SAC-SK method converts the model to an MDP, simplifies the hybrid action space, and combines SRU temporal encoding, a KAN approximator, boundary penalties, and low-battery charging rewards. Against standard SAC, simulations report 47.86% higher average retained terminal energy, 65.15% higher charging fairness, and 109.252 J lower system energy consumption, with consistent gains across three terminal-layout seeds.

## Problem framing

In remote/disaster areas without ground infrastructure, SWIPT-enabled UAV-MEC must balance UAV energy, terminal battery levels, and compute allocation under limited UAV battery, nonlinear energy-harvesting characteristics, and dynamic task arrivals — competing objectives needing multiple trade-off policies.

## System model

- **UAV roles.** Base station + MEC server with directional antennas; supplies charging ([[wireless-power-transfer]] / [[rf-energy-harvesting]]) and computation offloading to ground terminals.
- **Objective.** Bi-objective: minimize system energy consumption and maximize terminal battery energy, ensuring charging fairness.
- **Reformulation.** MDP with a hybrid (discrete + continuous) solution space.

## Method

- **SAC-SK:** improved soft actor-critic with an **action-simplification mechanism** for convergence/generalization, learning a maximum-entropy policy that schedules offloading decisions and UAV trajectory; **boundary-penalty** and **charging-reward** mechanisms aid learning ([[masac]]/[[hybrid-action-decision-making]]).

## Key findings

- SAC-SK significantly outperforms baselines across multiple metrics and shows robust generalization across diverse scenarios, particularly in complex environments (qualitative; specific curves in the paper).

## Limitations / future work

The authors explicitly note: static ground terminals may not capture real mobility; the energy model ignores signal interference in dense deployments; and although SAC-SK reduces training time/compute, it still has costs. Future work would address these.

## Relation to the corpus

An **energy-efficiency + WPT** entry that complements [[zhu-2025-lycnn-drl-wpt-mec]] (Lyapunov-guided DRL for WPT-MEC) and the energy-harvesting HAP-NOMA scheduling of [[hsu-2025-drl-hues-hap-noma]]. Its hybrid-action SAC connects to the hybrid-action DRL family ([[ma-2025-pdqn-vehicular-mec]], [[liu-2026-jppo-en-convntm]]). Reinforces [[wireless-power-transfer]], [[masac]], and [[uav-charging-scheduling]]. Shares the Geng Sun / Jiahui Li / Dusit Niyato cluster with several aerial sources.

## Raw artifacts

- `raw/sources/Joint_Resource_Management_for_Energy-Efficient_UAV-Assisted_SWIPT-MEC_A_Deep_Reinforcement_Learning_Approach/full.md`
- Original PDF and extracted figures in the same folder.
