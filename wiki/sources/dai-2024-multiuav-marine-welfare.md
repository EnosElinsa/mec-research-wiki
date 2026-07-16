---
type: source
title: "Multi-UAV Aided Multi-Access Edge Computing in Marine Communication Networks: A Joint System-Welfare and Energy-Efficient Design"
authors: ["Minghui Dai", "Chenglong Dou", "Yuan Wu", "Liping Qian", "Rongxing Lu", "Tony Q. S. Quek"]
year: 2024
url: "https://doi.org/10.1109/TCOMM.2024.3388501"
venue: "IEEE Transactions on Communications (IEEE TCOMM)"
modeling_card: required
tags: [source, maritime-mec, multi-uav-assisted-mec, computation-offloading, double-auction, two-stage-decomposition, energy-latency-tradeoff]
related:
  - "[[maritime-mec]]"
  - "[[multi-uav-assisted-mec]]"
  - "double-auction"
  - "[[two-stage-decomposition]]"
  - "[[task-offloading]]"
  - "[[energy-latency-tradeoff]]"
  - "[[dai-2023-hybrid-marine-mmwl]]"
  - "[[wang-2024-twotier-satellite-marine]]"
created: 2026-05-31
updated: 2026-07-16
---

# Multi-UAV Aided Multi-Access Edge Computing in Marine Communication Networks: A Joint System-Welfare and Energy-Efficient Design

## Citation

Dai, M., Dou, C., Wu, Y., Qian, L., Lu, R., & Quek, T. Q. S. (2024). *Multi-UAV Aided Multi-Access Edge Computing in Marine Communication Networks: A Joint System-Welfare and Energy-Efficient Design*. **IEEE Transactions on Communications**. DOI: 10.1109/TCOMM.2024.3388501. (Manuscript received 4 Sep 2023; date of publication 15 Apr 2024; date of current version 18 Sep 2024 → year 2024.)

## TL;DR

A two-layer marine MEC framework — a cluster of UAVs (aerial layer, with onboard edge servers) and a group of **ocean beacon stations (OBSs)** (sea-surface layer, with edge servers). Each UAV processes part of its workload locally and offloads the rest to one of multiple OBSs (**multi-access**). The paper defines **system welfare** as the total task-completion utility and **system revenue** as welfare minus total energy consumption, and maximizes system revenue by jointly optimizing OBS selection, offloading ratio, and transmission duration. The non-convex problem is solved by a **vertical (layered) decomposition** into three sub-problems, with a **double-auction** game for OBS selection.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A cluster of UAVs collects marine data and has onboard edge computing, while multiple ocean beacon stations provide additional edge capacity. Each UAV processes part of its workload locally and can offload the remaining fraction to one selected station over a multi-access marine link.

**Problem & objective**: The maximum-system-revenue problem jointly chooses station matching and offloading resources to maximize welfare minus weighted energy, $\max_{\boldsymbol\Delta,\boldsymbol\epsilon,\mathbf t} R^{\mathrm{tot}}=U^{\mathrm{tot}}-\varpi E^{\mathrm{tot}}$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| OBS selection | $\Delta_{i,j}(m_i)$ | binary, $\{0,1\}$ | Whether UAV $i$ offloads task $m_i$ to OBS $j$ |
| Offloading ratio | $\epsilon_i$ | continuous, $0\leq\epsilon_i\leq1$ | Fraction of UAV $i$'s workload processed at an OBS |
| Phase-II transmission time | $t_{i,j}^{\mathrm{Ph-II}}$ | continuous, $0\leq t_{i,j}^{\mathrm{Ph-II}}\leq T_{i,j}^{\max}$ | Time allocated to upload UAV $i$'s offloaded data to OBS $j$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| 22 | Station selection is binary and each UAV offloads a task to one OBS at a time, $\Delta_{i,j}(m_i)\in\{0,1\}$ |
| 23-24 | Each OBS respects its computing-resource limits, $\sum_i\Delta_{i,j}(m_i)\varrho_j\leq\varrho_j^{\max}$ and $\sum_i\Delta_{i,j}(m_i)\eta_j\leq\eta_j^{\max}$ |
| 25 | Allocated OBS bandwidth does not exceed capacity, $\sum_i\Delta_{i,j}(m_i)W_j\leq W_j^{\max}$ |
| 26-27 | Overall completion time and Phase-II upload time meet their deadlines, $t_i^{\mathrm{ove}}\leq T_i^{\max}$ and $t_{i,j}^{\mathrm{Ph-II}}\leq T_{i,j}^{\max}$ |
| 28-29 | Workload size and partial-offloading ratio remain feasible, $S_i^{\mathrm{tot}}\leq S_i^{\max}$ and $0\leq\epsilon_i\leq1$ |

**Algorithm**: A vertical decomposition separates OBS selection, offloading ratio, and transmission time. The selection block uses a double auction with preference filtering, K-payment, and dynamic bid adjustment; the middle block applies bisection to $\epsilon_i$; and the top block bounds and searches $t_{i,j}^{\mathrm{Ph-II}}$ until the revenue solution stabilizes.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Dai et al. [x] investigated multi-UAV multi-access edge computing in a two-layer marine network where UAVs can compute locally or partially offload workloads to ocean beacon stations. They formulated station selection, offloading ratio, and transmission duration as a nonconvex system-revenue maximization problem that subtracts weighted UAV and station energy from total participant utility. Their vertical decomposition uses a double auction for station matching, bisection for partial offloading, and a bounded search for transmission time. Simulations show higher transaction success and system revenue than distance-based and random station selection, while also exposing the additional energy consumed when more UAV-station transactions succeed.

## Problem framing

Marine activities (environment monitoring, ocean-resource exploration) demand low-latency, high-rate processing, but OBSs are sparse and costly to deploy and marine devices are battery-powered. UAVs add sensing/computing/relaying flexibility, yet collected oceanic data overwhelms their limited compute. The open gap the paper targets: multi-UAV multi-access edge computing for energy efficiency had not been studied in marine networks; prior work treated latency, energy, and UAV mobility largely in isolation.

## System model

- **Actors.** Aerial layer: a cluster of UAVs (data collection + local edge compute). Sea-surface layer: a group of OBSs with edge servers serving UAVs.
- **Objective.** Maximize **system revenue** = system welfare (total completion utility) − total UAV+OBS energy consumption, subject to task deadlines.
- **Decisions.** OBS selection per UAV, offloading ratio ε_i, and Phase-II transmission duration.

## Method

- **Vertical decomposition** of Problem (MSR) into a top-problem, mid-problem, and sub-problem ([[two-stage-decomposition]]-style layered solve).
- **Sub-problem (OBS selection):** a **double-auction** game (UAVs = buyers, OBSs = sellers, leader-OBS = auction controller) with valuation/bidding/payment rules (K-payment), a dynamic bidding-adjustment strategy to raise transaction success, and a distance/resource preference function for feasible-OBS classification. See double-auction.
- **Mid-problem (offloading ratio):** bisection search over ε_i ∈ [0,1].
- **Top-problem (transmission duration):** bound-then-search over the Phase-II offloading time.

## Key findings

- Versus **DOS** (distance-based / greedy closest-OBS) and **ROS** (random OBS selection) benchmarks, the proposed algorithms achieve the highest **transaction success ratio** (Fig. 7) and the highest **system revenue** (Figs. 8–9, stated qualitatively).
- An explicit trade-off is reported: the proposed scheme also incurs **higher energy consumption** than the benchmarks, because more UAV-OBS pairs reach agreement and complete more workload (raising both revenue and energy).

## Limitations / future work

Simulation-based; revenue/energy advantages are read from Figs. 7–9 (indicative, not asserted as exact magnitudes). Future work (stated): investigate **integrated sensing and computational-task offloading** for marine communication networks.

## Relation to the corpus

A **maritime MEC** entry distinguished by its **double-auction market** for multi-access OBS selection and its **system-welfare/system-revenue** objective (utility minus energy). It complements the same group's hybrid FDMA/NOMA marine offloading [[dai-2023-hybrid-marine-mmwl]] (shared first author Minghui Dai, senior author Yuan Wu, co-author Liping Qian) and the game-theoretic two-tier satellite-marine design [[wang-2024-twotier-satellite-marine]]. Introduces the new double-auction concept and reinforces [[maritime-mec]] and [[multi-uav-assisted-mec]].

## Raw artifacts

- `raw/sources/Multi-UAV_Aided_Multi-Access_Edge_Computing_in_Marine_Communication_Networks_A_Joint_System-Welfare_and_Energy-Efficient_Design/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
