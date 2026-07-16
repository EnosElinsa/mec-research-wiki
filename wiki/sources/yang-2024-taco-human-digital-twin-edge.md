---
type: source
modeling_card: required
title: "Dynamic Human Digital Twin Deployment at the Edge for Task Execution: A Two-Timescale Accuracy-Aware Online Optimization"
authors: ["Yuye Yang", "You Shi", "Changyan Yi", "Jun Cai", "Jiawen Kang", "Dusit Niyato", "Xuemin Shen"]
year: 2024
url: "https://doi.org/10.1109/TMC.2024.3406607"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, digital-twin, mobile-edge-computing, two-timescale-optimization, lyapunov-optimization, task-offloading, service-caching-mec, end-edge-cloud]
related:
  - "[[mobile-edge-computing]]"
  - "[[three-tier-cloud-edge-end]]"
  - "[[two-timescale-optimization]]"
  - "[[lyapunov-optimization]]"
  - "[[task-offloading]]"
  - "[[service-caching-mec]]"
  - "[[task-migration]]"
  - "[[mobility-aware-offloading]]"
  - "[[sun-2025-tjcct-twotimescale-uav-mec]]"
  - "[[zhang-2025-mcma-task-migration]]"
  - "[[edge-user-allocation]]"
created: 2026-06-01
updated: 2026-07-16
---

# Dynamic Human Digital Twin Deployment at the Edge for Task Execution: A Two-Timescale Accuracy-Aware Online Optimization

## Citation

Yang, Y., Shi, Y., Yi, C., Cai, J., Kang, J., Niyato, D., & Shen, X. (2024). *Dynamic Human Digital Twin Deployment at the Edge for Task Execution: A Two-Timescale Accuracy-Aware Online Optimization*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2024.3406607. (Received 26 Jan 2024; revised 12 Apr 2024; accepted 24 May 2024; date of publication 28 May 2024; date of current version 5 Nov 2024. Corresponding author: Changyan Yi.)

## TL;DR

The first study of **human digital twin (HDT)** deployment at the network edge for assisting task execution, under an **end-edge-cloud** collaborative framework. Each physical twin's (PT) virtual twin (VT) on an edge server (ES) is a **generic model** placed by downloading experiential knowledge from the cloud **plus** a **customized model** updated from personalized sensor data. The goal is to **maximize average task-execution accuracy** under stringent energy and delay constraints amid PT **mobility** and **status-variation** uncertainty, by jointly optimizing VT construction (generic placement + customized update), PT task offloading, ES access selection, and communication/computation resource allocation. The solver, **TACO (Two-timescale Accuracy-aware online Optimization)**, uses an improved Lyapunov method plus **piecewise McCormick envelopes (PME)** and **block coordinate descent (BCD)**.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: An end-edge-cloud HDT system contains mobile physical twins (PTs), virtual twins (VTs) hosted by geographically distributed edge servers, and a cloud knowledge repository. Each VT has a generic model placed from experiential knowledge and a customized model updated from personalized sensor data; PTs can execute tasks locally or offload them to the associated ES.

**Problem & objective**: Problem $\mathcal P_1$ maximizes the long-term average HDT-assisted task accuracy, $\max_{\mathcal J_i^A(t),\mathcal J_i^B(\tau)}\lim_{t\to\infty}\mathcal A$, while keeping average task response delay and total system energy below prescribed thresholds.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| ES access selection | $a_{i,m}(t)$ | binary | Selects the ES accessed by PT $i$ in frame $t$ |
| Generic-model granularity | $x_i(t)$ | continuous, bounded | Controls experiential knowledge used for generic VT placement |
| Customized-data size | $y_i(\tau)$ | continuous, bounded | Personalized data uploaded for customized VT update |
| Bandwidth allocation | $b_i(\tau)$ | continuous, nonnegative | Communication resource assigned to PT $i$ |
| Computation allocation | $f_i(\tau)$ | continuous, nonnegative | Edge or local compute resource assigned to PT $i$ |
| Task offloading | $z_i(\tau)$ | binary | Selects local execution or edge execution |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| 17a | Each PT connects to at most one ES, $\sum_m a_{i,m}(t)\le1$ |
| 17b | ES bandwidth allocation is capacity limited, $\sum_i a_{i,m}(t)b_i(\tau)\le1$ |
| 17c | ES computation allocation is capacity limited, $\sum_i a_{i,m}(t)f_i(\tau)\le1$ |
| 17d | Long-term average task response delay is bounded by $T_i^{\max}$ |
| 17e | Long-term average system energy is bounded by $E^{\max}$ |

**Algorithm**: An improved two-timescale Lyapunov decomposition converts the long-term mixed-integer problem into instant subproblems. TACO alternates a piecewise McCormick-envelope solver for large-timescale access and placement decisions with a block-coordinate-descent solver for small-timescale update, offloading, and resource decisions.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Yang et al. [x] studied dynamic human digital twin deployment at the edge in an end-edge-cloud system with mobile physical twins and uncertain status changes. They maximized average HDT-assisted task execution accuracy while constraining long-term response delay and total energy, jointly selecting edge access, generic placement granularity, customized updates, task offloading, and communication and computation resources. An improved two-timescale Lyapunov method decomposes the online problem, and alternating PME and BCD procedures solve the coupled large- and small-timescale subproblems. The paper's analysis gives an asymptotically optimal solution with polynomial-time complexity. Simulations report higher task accuracy together with lower response delay and system energy than the compared schemes.

## Problem framing

Prior HDT work builds twins solely on the cloud (ignoring edge resources), and general edge digital-twin / service-deployment work assumes fixed locations, known mobility, or encapsulated non-customized services — none fit HDT, where PTs are **highly mobile with unpredictable patterns** and **personalized status varies frequently**. Two unique requirements follow: dynamically **place** each PT's VT on the ES it may hand over to, and continuously **update** the customized VT to stay high-fidelity. These create a tension: finer VTs raise accuracy but inflate data volume, delay, and energy, so generic-placement and customized-update data sizes must be balanced against task offloading that shares the same resources. Crucially, the decisions trigger on **different timescales** — generic placement / access handover changes slowly (PT mobility), while customized update and task offloading change fast (status variation) — so optimization must be **asynchronous across two timescales**, online, without future statistics.

## System model

- **Framework.** End (PT sensors) — edge (ES hosting VTs) — cloud (experiential-knowledge repository); each PT pairs with a VT split into a generic + customized model ([[three-tier-cloud-edge-end]]).
- **Large-timescale decisions.** Granularity of each PT's experiential knowledge for **generic VT placement**, and **ES access selection** per PT.
- **Small-timescale decisions.** Amount of personalized data for **customized VT update**, **task-offloading** decision (local vs edge) per task, and per-ES communication/computation **resource allocation**.
- **Objective.** Maximize average **task-execution accuracy** subject to long-term energy and delay constraints under mobility/status uncertainty.

## Method

- **TACO** — built on an **improved Lyapunov optimization** that decomposes the long-term online problem into a series of deterministic short-term subproblems at the two timescales.
- An **alternating algorithm** integrating **piecewise McCormick envelopes (PME)** (for the bilinear/non-convex couplings) and **block coordinate descent (BCD)** solves the decoupled subproblems in the large- and small-timescale alternately.
- **Theory.** The paper derives the closed-form **gap to optimum** and **polynomial-time** complexity, showing **asymptotic optimality**.

## Key findings

- TACO is shown (theory + simulation) to be **superior to counterparts** in HDT deployment, simultaneously **improving HDT-assisted task-execution accuracy**, **reducing service response delay**, and **lowering overall system energy consumption** (the paper's stated results; specific curves figure-derived and indicative).
- The two-timescale decomposition is what lets slowly-triggered placement/handover and fast-triggered update/offloading be optimized asynchronously yet near-optimally.

## Limitations / future work

The authors flag (stated) handling **varying personalized-data quality** (possibly using AIGC to synthesize high-quality personalized datasets) and **VT migration** between ESs (introducing mobility prediction, migration delay, and model privacy as new factors). Simulation-based; quantitative magnitudes are figure-derived.

## Relation to the corpus

A **digital-twin + MEC** entry that brings the [[two-timescale-optimization]] + [[lyapunov-optimization]] pattern to **human-centric** twin placement and update. Its large/small-timescale split mirrors the UAV-MEC two-timescale design of [[sun-2025-tjcct-twotimescale-uav-mec]], while its VT-on-edge placement-and-update problem is kin to [[service-caching-mec]] and the task-migration framing of [[zhang-2025-mcma-task-migration]]. The ES access-selection subproblem connects to [[edge-user-allocation]] and [[mobility-aware-offloading]]. Shares the Niyato/Kang/Shen author cluster (see [[dusit-niyato]], [[jiawen-kang]], [[xuemin-shen]]).

## Raw artifacts

- `raw/sources/Dynamic_Human_Digital_Twin_Deployment_at_the_Edge_for_Task_Execution_A_Two-Timescale_Accuracy-Aware_Online_Optimization/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
