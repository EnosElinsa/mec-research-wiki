---
type: source
title: "Dynamic Computation Offloading for Mobile-Edge Computing With Energy Harvesting Devices"
authors: ["Yuyi Mao", "Jun Zhang", "Khaled B. Letaief"]
year: 2016
url: "https://doi.org/10.1109/JSAC.2016.2611964"
venue: "IEEE Journal on Selected Areas in Communications (IEEE JSAC)"
modeling_card: required
tags: [source, mobile-edge-computing, energy-harvesting-mec, computation-offloading, lyapunov-optimization, dynamic-voltage-frequency-scaling, power-control]
related:
  - "[[mobile-edge-computing]]"
  - "[[energy-harvesting-mec]]"
  - "[[lyapunov-optimization]]"
  - "[[task-offloading]]"
  - "[[binary-vs-partial-offloading]]"
  - "[[energy-latency-tradeoff]]"
  - "[[qoe-modeling-mec]]"
  - "[[zhang-2013-energy-optimal-mcc-stochastic]]"
  - "[[zhou-2018-uav-wireless-powered-mec]]"
  - "[[wang-2024-maritime-eh-jcora]]"
  - "[[mao-2017-mec-survey-communication]]"
  - "[[khaled-ben-letaief]]"
created: 2026-06-01
updated: 2026-07-16
---

# Dynamic Computation Offloading for Mobile-Edge Computing With Energy Harvesting Devices

## Citation

Mao, Y., Zhang, J., & Letaief, K. B. (2016). *Dynamic Computation Offloading for Mobile-Edge Computing With Energy Harvesting Devices*. **IEEE Journal on Selected Areas in Communications**, 34(12), 3590–3605. DOI: 10.1109/JSAC.2016.2611964. (Received 29 Jan 2016; revised 10 May 2016; accepted 4 Aug 2016; date of publication 20 Sep 2016; date of current version 29 Dec 2016.)

## TL;DR

A foundational **green MEC** paper: a single **energy-harvesting (EH)** mobile device, served by an MEC server, decides each time slot whether to execute a task locally or offload it, while controlling local **CPU-cycle frequency (via DVFS)** and **transmit power**. The performance metric is an **execution cost** combining execution delay and **task failure** (dropping). The proposed **Lyapunov-optimization-based Dynamic Computation Offloading (LODCO)** algorithm decides offloading, CPU frequency, and transmit power per slot from only the **current** system state — requiring no distribution knowledge of task arrivals, channel, or the EH process — by solving a deterministic per-slot problem in closed form or by bisection. LODCO is proven **asymptotically optimal**.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: One energy-harvesting mobile device is associated with an MEC server through an i.i.d. block-fading wireless channel. Tasks arrive as a Bernoulli process, have an execution deadline no longer than one slot, and are either executed locally, offloaded to the server, or dropped when neither mode is feasible.

**Problem & objective**: Problem $\mathcal P_1$ minimizes long-term average execution cost, $\lim_{T\to\infty}\frac{1}{T}\mathbb E[\sum_{t=0}^{T-1}\mathrm{cost}^t]$, where $\mathrm{cost}^t$ combines local or server execution delay with a weighted task-drop penalty $\phi$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Computation mode | $I_m^t,I_s^t,I_d^t$ | binary | Local execution, server offloading, or task dropping in slot $t$ |
| Local CPU frequency | $f_w^t$ | continuous, $0\leq f_w^t\leq f_{\mathrm{CPU}}^{\max}$ | DVFS frequency for CPU cycle $w$ |
| Offloading power | $p^t$ | continuous, $0\leq p^t\leq p_{\mathrm{tx}}^{\max}$ | Transmit power used for server offloading |
| Harvested-energy use | $e^t$ | continuous within harvested-energy availability | Energy drawn from the EH process in slot $t$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| 1 | Exactly one mode is selected: $I_m^t+I_s^t+I_d^t=1$ |
| 12 | Any executed task meets its deadline: $\mathcal D(\boldsymbol I^t,\boldsymbol f^t,p^t)\leq\tau_d$ |
| 14 | Battery output energy is bounded: $\mathcal E(\boldsymbol I^t,\boldsymbol f^t,p^t)\leq E_{\max}$ |
| 15-16 | Offloading power and local CPU frequencies are zero when their corresponding mode is inactive and obey their maxima |
| 17 | Mode indicators are binary: $I_m^t,I_s^t,I_d^t\in\{0,1\}$ |

**Algorithm**: Apply Lyapunov drift-plus-penalty to replace the high-dimensional MDP with a deterministic per-slot problem. Use the current task, channel, battery, and harvested-energy state to choose the mode, CPU frequencies, and transmit power, solving the scalar frequency and power subproblems in closed form or by bisection; tune the control parameters to approach the optimal average cost.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Mao et al. [x] studied computation offloading for an energy-harvesting mobile device served by an MEC server under causal task, channel, and harvested-energy information. They formulated long-term execution-cost minimization, combining execution delay with a penalty for dropped tasks, over local execution, server offloading, CPU-cycle frequency, and transmit-power decisions. Their LODCO algorithm uses Lyapunov optimization to solve a deterministic per-slot problem from the current system state, with closed-form or bisection updates and no distributional prior knowledge. Simulations reported lower execution cost and near-zero task-drop ratios than greedy baselines, asymptotic convergence to the optimal cost, and more than 40% gain over greedy offloading at a large device-server distance.

## Problem framing

Battery-powered devices interrupt computation when energy runs out; bigger batteries cost more and frequent recharging is impractical (e.g., hard-to-reach WSN/IoT nodes), while ICT energy growth motivates green computing. [[energy-harvesting-mec|Energy harvesting]] (solar, wind, motion) offers self-sustaining operation, but injects new design challenges: harvested energy is free, so the objective shifts from *minimizing* device energy to *optimizing computation performance*; energy side information (ESI) must be handled alongside channel side information (CSI); and time-correlated battery dynamics couple decisions across slots. Offloading policies designed for battery-powered devices cannot exploit renewable supply, so a new methodology is needed.

## System model

- **Actor.** One EH mobile device with a rechargeable battery, served by an MEC server; tasks can execute locally or offload to the server (mobile/edge cloud execution).
- **Performance metric.** **Execution cost** = execution delay + a penalty $\phi$ for **task failure** (a dropped/failed task), capturing the [[energy-latency-tradeoff]] under intermittent energy.
- **Controls.** Offloading decision (whether to offload), **CPU-cycle frequencies** for local execution via **DVFS**, and **transmit power** for offloading; an EH/battery-energy decision per slot.
- **Formulation.** An **execution cost minimization (ECM)** problem, an intractable high-dimensional Markov decision problem under causal SI, transformed via [[lyapunov-optimization|Lyapunov optimization]] into per-slot deterministic problems.

## Method

- **LODCO** — a low-complexity **online** Lyapunov-optimization algorithm. Each slot it solves a deterministic optimization whose optimal solution is available in **closed form or by bisection search**, deciding offloading, CPU frequency, and transmit power.
- Requires **little prior knowledge** (no statistics of task request, channel, or EH process).
- The paper characterizes **monotonic properties**: the optimal CPU-cycle frequency (local) and transmit power (offloading) are **non-decreasing in the battery energy level**, exposing how EH state shapes operation.
- Proven **asymptotically optimal** via rigorous performance analysis.

## Key findings

- LODCO **significantly outperforms benchmark greedy policies** in execution cost (the paper's stated simulation result).
- It **noticeably reduces computation failures** at the expense of only **minor execution-delay degradation** (the paper's stated trade-off).
- The monotonic dependence of CPU frequency / transmit power on battery level is established analytically (Corollary/Lemma in the parse), giving a structural guide to EH-MEC operation.

## Limitations / future work

The authors flag (stated) extensions to **multiple mobile devices**, **resource-limited MEC servers**, and **combining wireless energy transfer with EH** (a power beacon co-located with the MEC server to compensate renewable-energy deficits). The model is single-device and simulation-validated.

## Relation to the corpus

A widely-cited **MEC + energy-harvesting** anchor and one of the originators of the **Lyapunov-per-slot online offloading** pattern that recurs throughout the corpus. It grounds the [[energy-harvesting-mec]] concept and complements the renewable-EH maritime instance [[wang-2024-maritime-eh-jcora]] and the wireless-power-transfer MEC anchor [[zhou-2018-uav-wireless-powered-mec]] (whose WPT-as-energy-source idea LODCO itself flags as future work). It is contemporaneous with and complementary to the MCC offloading framework [[zhang-2013-energy-optimal-mcc-stochastic]] (closed-form energy-optimal scheduling under a stochastic channel), and the methodology it popularizes is catalogued in [[mao-2017-mec-survey-communication]] (the MEC communication survey by an overlapping author set).

## Raw artifacts

- `raw/sources/Dynamic_Computation_Offloading_for_Mobile-Edge_Computing_With_Energy_Harvesting_Devices/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
