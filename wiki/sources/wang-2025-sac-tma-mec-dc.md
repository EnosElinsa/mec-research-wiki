---
type: source
modeling_card: required
title: "AAV-Assisted Joint Mobile Edge Computing and Data Collection via Matching-Enabled Deep Reinforcement Learning"
authors: ["Boxiong Wang", "Hui Kang", "Jiahui Li", "Geng Sun", "Zemin Sun", "Jiacheng Wang", "Dusit Niyato"]
year: 2025
url: "https://doi.org/10.1109/JIOT.2025.3542025"
venue: "IEEE Internet of Things Journal (IEEE IoT-J)"
tags: [source, uav-mec, data-collection, soft-actor-critic, matching-theory, mixed-integer-nonlinear-programming, drl]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[uav-data-collection]]"
  - "[[masac]]"
  - "[[matching-theory-for-resource-allocation]]"
  - "[[mixed-integer-nonlinear-programming]]"
  - "[[uav-trajectory-control]]"
  - "[[chen-2025-swipt-mec-sac]]"
created: 2026-05-31
updated: 2026-11-03
---

# AAV-Assisted Joint Mobile Edge Computing and Data Collection via Matching-Enabled Deep Reinforcement Learning

## Citation

Wang, B., Kang, H., Li, J., Sun, G., Sun, Z., Wang, J., & Niyato, D. (2025). *AAV-Assisted Joint Mobile Edge Computing and Data Collection via Matching-Enabled Deep Reinforcement Learning*. **IEEE Internet of Things Journal**. DOI: 10.1109/JIOT.2025.3542025.

## TL;DR

Unlike prior work that treats AAV-assisted **MEC** and **data collection (DC)** as separate problems, this paper studies a **joint multi-AAV MEC-DC system**: multiple AAVs process computation-intensive MEC tasks while a single AAV performs freshness-insensitive DC, with co-channel interference among UAVs explicitly modeled. The authors formulate a two-objective problem — **minimize total MEC latency** and **maximize collected data volume** — as a non-convex mixed-integer program with long-term, dynamic structure, then solve it with **SAC-TMA**: a soft actor-critic agent that jointly optimizes AAV movement, user transmit power, and user association in real time, where association is handled by a **two-phase matching-based association (TMA)** strategy.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Several MEC-AAVs process tasks of ground users (GUs) while one DC-AAV collects data from DC users in the same area. All links reuse spectrum, so AAV positions, GU association, and GU transmit powers jointly set interference, latency, collected data, and AAV energy.
**Problem & objective**: Problem $\mathcal P$ (15) is a two-objective problem, $\min_{\{V,p,X\}}Q=\{f_1,-f_2\}$: minimize MEC latency $f_1$ and maximize collected data $f_2=\sum_tD(t)$ (14).
**Decision variables**:
| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| AAV positions | $V=\{V_u(t)\}$ | continuous 2-D | Trajectories of the MEC-AAVs and the DC-AAV |
| GU transmit power | $p_g(t)$ | continuous, $\le p_g^{\max}$ | Uplink power of GU $g$ |
| Association | $X_{u,g}(t)$ | binary | GU $g$ served by AAV $u$ |
**Constraints**:
| ID | Meaning and key expression |
|---|---|
| (15b) | MEC task latency $T_{i,m}^f(t)\le T_{m,f}^{\max}$ |
| (15c) | GU power $p_g(t)\le p_g^{\max}$ |
| (15d) | AAV energy $\sum_tE_u^{total}(t)\le E_u^{\max}$ |
| (15e)-(15g) | Binary association, each GU served by one AAV, $\sum_uX_{u,g}(t)=1$, and at most $N_u^{\max}$ GUs per AAV |
| (15h)-(15j) | Area bounds in $x$ and $y$ and per-slot moving distance $0\le m_u(t)\le m_u^{\max}$ |
| (15k) | Collision avoidance $\lVert V_a(t)-V_b(t)\rVert\ge d_{\min}$ |
**Algorithm**: SAC-TMA uses a two-phase matching game with externalities to set GU association, which shrinks the action space, and a soft actor-critic agent to choose AAV movements and GU powers; the reward combines latency (17), collected data, and boundary and energy penalties (20)-(21).

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Wang et al. [x] studied an aerial network that jointly supports mobile edge computing and data collection with multiple MEC-AAVs and one DC-AAV. They formulated a long-term non-convex mixed-integer problem that minimizes MEC latency and maximizes collected data under latency, power, energy, association, movement-range, and collision constraints. Their SAC-TMA method combines soft actor-critic control of AAV movement and user transmit power with a two-phase matching-based association strategy. The matching stage reduces the reinforcement-learning action space while accounting for association externalities. Simulation results show improvements in latency, collected data volume, and coverage over the evaluated benchmark algorithms.

## Problem framing

MEC and DC are usually run on different UAVs (MEC tasks need real-time, continuous compute; mixing in DC hurts MEC latency and raises energy use; isolating the data also aids privacy). But agricultural, traffic-management, and post-disaster scenarios need both at once in the same area. The two goals conflict and interact through shared spectrum and interference, and through energy/trajectory coupling, making a joint design necessary and hard.

## System model

- **Actors.** Multiple MEC-AAVs (process computation-intensive tasks) + one DC-AAV (collects freshness-insensitive data) serving ground users (GUs); co-channel interference among UAVs is modeled rather than ignored.
- **Objectives.** Minimize total MEC system latency; maximize total collected data volume — conflicting and interdependent.
- **Decision variables.** AAV movement (trajectory), user association, and user transmit power.
- **Problem class.** Mixed-integer non-convex with long-term / dynamic optimization properties.

## Method

- **Action-space-reduced MDP.** User association is modeled as a **one-to-many matching game with externalities**, which reduces the action space the DRL agent must search ([[matching-theory-for-resource-allocation]]).
- **SAC-TMA.** A **soft actor-critic** ([[masac|SAC]]) algorithm integrated with the **two-phase matching-based association (TMA)** strategy, jointly optimizing AAV movement, user association, and user transmit power in real time.

## Key findings

- SAC-TMA outperforms four benchmark algorithms across different numbers of MEC-users, jointly improving latency, collected data volume, and coverage (qualitative; specific curves in the paper).
- The TMA strategy outperforms traditional matching-based algorithms and random strategies, and is feasible in terms of algorithm running time.

## Limitations / future work

The parse's contribution/intro framing does not enumerate explicit limitations; the work is simulation-based.

## Relation to the corpus

A **matching + SAC** entry in the Jilin-University / NTU aerial-MEC cluster, sharing the Geng Sun group lineage with [[chen-2025-swipt-mec-sac]] (co-authors Boxiong Wang, Hui Kang, Jiahui Li, Zemin Sun, Jiacheng Wang, Dusit Niyato). It pairs SAC with [[matching-theory-for-resource-allocation]] much as other corpus sources pair Stackelberg/bargaining with matching, and it adds the **data-collection** objective ([[uav-data-collection]]) to the usual MEC offloading picture. Reinforces [[masac]] and [[mixed-integer-nonlinear-programming]].

## Raw artifacts

- `raw/sources/AAV-Assisted_Joint_Mobile_Edge_Computing_and_Data_Collection_via_Matching-Enabled_Deep_Reinforcement_Learning/AAV-Assisted_Joint_Mobile_Edge_Computing_and_Data_Collection_via_Matching-Enabled_Deep_Reinforcement_Learning.md`
- Original PDF and extracted figures in the same folder.
