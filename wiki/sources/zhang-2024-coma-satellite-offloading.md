---
type: source
modeling_card: required
title: "Collaborative Task Offloading Optimization for Satellite Mobile Edge Computing Using Multi-Agent Deep Reinforcement Learning"
authors: ["Hangyu Zhang", "Hongbo Zhao", "Rongke Liu", "Aryan Kaushik", "Xiangqiang Gao", "Shenzhan Xu"]
year: 2024
url: "https://doi.org/10.1109/TVT.2024.3405642"
venue: "IEEE Transactions on Vehicular Technology (IEEE TVT)"
tags: [source, leo-satellite-edge-computing, computation-offloading, multi-agent-q-learning, counterfactual-multi-agent-policy-gradient, centralized-training-decentralized-execution, non-terrestrial-network]
related:
  - "[[rongke-liu]]"
  - "[[counterfactual-multi-agent-policy-gradient]]"
  - "[[leo-satellite-edge-computing]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[pomdp]]"
  - "[[free-space-optical-isl]]"
  - "[[task-offloading]]"
  - "[[non-terrestrial-network]]"
  - "[[cheng-2025-dos-satellite-edge-computing]]"
  - "[[chen-2024-thoas-traffic-aware-sagin]]"
  - "[[qin-2025-matd3-noma-queue-sagin]]"
  - "[[mao-2025-bcsa-frl]]"
created: 2026-06-02
updated: 2026-11-03
---

# Collaborative Task Offloading Optimization for Satellite Mobile Edge Computing Using Multi-Agent Deep Reinforcement Learning

## Citation

Zhang, H., Zhao, H., Liu, R., Kaushik, A., Gao, X., & Xu, S. (2024). *Collaborative Task Offloading Optimization for Satellite Mobile Edge Computing Using Multi-Agent Deep Reinforcement Learning*. **IEEE Transactions on Vehicular Technology**. DOI: 10.1109/TVT.2024.3405642. (Manuscript received 8 March 2024; revised 29 April 2024; accepted 23 May 2024; date of publication 11 July 2024; date of current version 17 October 2024 → year 2024.)

## TL;DR

A **multi-agent collaborative task-offloading** scheme for **distributed satellite MEC (SMEC)** on a LEO constellation. Each satellite is an autonomous agent that, facing **time-varying inter-satellite-link (ISL) visibility** and mission demands, decides offloading ratios and computing-resource allocation from local observations to **minimize total energy consumption** under task delay and resource constraints. The problem is cast as a **POMDP** and solved with **counterfactual multi-agent policy gradients (COMA)** in an **actor-critic / centralized-training-decentralized-execution (CTDE)** setup: a centralized critic (trained on the terrestrial cloud) computes a per-agent counterfactual baseline for credit assignment, and the learned actor runs on each satellite. The actor is redesigned with an **attention-based bidirectional LSTM (Atten-BiLSTM)** to exploit the temporal regularity of the (preset, periodic) LEO topology. A Satellite-Tool-Kit (STK)-built constellation is used for evaluation.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: MEC-enabled LEO satellites cooperatively process divisible tasks: the satellite $L_u$ that receives task $\mathcal K_t$ keeps part of it and offloads parts to visible satellites $M_v$ over single-hop ISLs. ISL visibility changes periodically, and each satellite observes only its own visibility and distance rows.
**Problem & objective**: Problem (10) minimizes long-term system energy, $\min_{x_t,f_t}\sum_{t=1}^{\mathcal T}E_t^{exe}$, where $E_t^{exe}=\sum_v(E_t^{tran}+E_t^{comp})$ (9).
**Decision variables**:
| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Offloading ratio | $x_t^v$ | continuous, $[0,1]$ | Fraction of task $\mathcal K_t$ processed by satellite $M_v$ |
| Computing capability | $f_t^v$ | continuous, $[0,F]$ | CPU frequency satellite $M_v$ assigns to its fraction |
| Agent action | $a_t^u=\{x_t^u,f_t^u\}$ | discretized (14) | Per-satellite action in the POMDP |
**Constraints**:
| ID | Meaning and key expression |
|---|---|
| (10a) = (7) | Parallel completion time within the deadline: $T_t^{exe}=\max\{T_t\}\leq T_t^{\max}$ |
| (10a) = (8) | Offloaded parts finish within the ISL visibility window: $T_t\leq T_t^{hold}$ |
| (10b) | $0\leq x_t^v\leq1$ |
| (10c) | Ratios sum to one: $\sum_vx_t^v=1$ |
| (10d) | $0\leq f_t^v\leq F$ |
| Reward (15) | $r_t=\mathcal R-\omega E_t^{exe}-\varrho_1-\varrho_2$, with penalties for timeout and broken ISL windows |
**Algorithm**: Model the satellites as cooperative agents in a POMDP with global state (12) and local observations (13). COMA trains a centralized critic with TD($\lambda$) targets and a per-agent counterfactual baseline on the ground; an attention-based BiLSTM actor captures periodic topology changes, and the trained actors execute onboard from local observations.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zhang et al. [x] studied collaborative task offloading in distributed satellite mobile edge computing with time-varying inter-satellite visibility. They formulated a POMDP in which satellites select offloading ratios and computing resources to minimize energy under task-delay, visibility, and resource constraints. COMA uses a centralized critic and per-agent counterfactual baselines during terrestrial training while satellite actors execute from local observations. An attention-based bidirectional LSTM actor captures periodic topology evolution. STK-based simulations report better convergence and energy performance than the evaluated MADDPG, DDPG, independent actor-critic, unimproved-actor, random-offloading, and local-computing baselines.

## Problem framing

LEO satellites increasingly carry powerful onboard hardware and generate large Earth-observation data, but store-and-forward to ground stations is bottlenecked by short communication windows, propagation delay, and limited link availability. SMEC sinks cloud compute to the LEO edge for real-time onboard processing, but a single satellite often cannot meet computation-intensive / latency-sensitive missions, motivating **inter-satellite cooperative computing** over (FSO-based) ISLs. The LEO constellation's highly dynamic topology, strictly limited and unbalanced resources, and scarce solar/battery energy make this hard; most prior SMEC work assumed quasi-static models with fixed offloading locations and ignored time-varying ISL connectivity. Centralized ground control does not scale with constellation size (state-synchronization explosion, communication/command delay), motivating distributed, autonomous, local-observation decisions.

## System model

- **Constellation.** U LEO satellites across P orbital planes; each satellite carries an MEC server and maintains ISLs with four neighbors (two intra-plane, two inter-plane) via laser/FSO links. Physical visibility (Earth-blockage geometry) determines whether an ISL exists, so the available-satellite set (≤5, including itself) is time-varying; polar vs equatorial satellites see different visibility-change frequencies.
- **Tasks.** Time-slotted operation; per slot a randomly generated divisible task (source satellite, data size, workload cycles/bit, max tolerable delay) with exponential inter-arrival times. Offloading ratios across available satellites sum to one; single-hop ISL only (no multi-hop relay).
- **Models.** AWGN ISL channel with Shannon-rate transmission (assumed constant per FSO ISL), CPU energy ∝ κf², and end-to-end delay = transmission + propagation + computation (return data ignored as small).
- **Objective.** Long-term minimization of total system energy consumption subject to delay and resource limits.

## Method

- **POMDP + COMA.** Each satellite agent observes locally; a centralized critic on the terrestrial cloud computes a **counterfactual baseline** per agent to assign credit, enabling low-complexity multi-agent learning. Parameter sharing across agents reduces model complexity; critic training (ground) and actor execution (space) are separated by batches to cut onboard compute and ground dependence.
- **Atten-BiLSTM actor.** The actor network is redesigned with an attention-based bidirectional LSTM to extract the temporal characteristics of the preset, periodic LEO topology, improving predictive performance.

## Key findings

- Against benchmarks — a no-improvement actor, MADDPG, DDPG, independent actor-critic, random offloading, and local-computing — the proposed COMA + Atten-BiLSTM scheme handles collaborative task computing under constraints with **better convergence and superiority across varying environmental variables** (the paper's stated simulation results; specific margins are in the parse's figures, so treat exact values as indicative).
- The Atten-BiLSTM actor and the ground-critic/space-actor batch separation are credited with the performance and onboard-cost improvements.

## Limitations / future work

Simulation-based (STK-built constellation). The model restricts offloading to single-hop ISL neighbors (no multi-hop relay), assumes a constant per-ISL FSO rate, and ignores result-return transmission. Onboard training cost is mitigated by moving critic training to the ground but not eliminated.

## Relation to the corpus

A **LEO satellite-edge-computing** offloading entry that anchors the new [[counterfactual-multi-agent-policy-gradient]] concept and reinforces the CTDE-as-default multi-agent pattern. It joins the SAGIN/satellite-offloading track alongside [[cheng-2025-dos-satellite-edge-computing]], [[chen-2024-thoas-traffic-aware-sagin]], and [[qin-2025-matd3-noma-queue-sagin]], shares the FSO-ISL routing context of the satellite thread ([[free-space-optical-isl]]), and contrasts with the trust-oriented satellite-FL approach [[mao-2025-bcsa-frl]] in how it handles distributed decisions on a LEO constellation.

## Raw artifacts

- `raw/sources/Collaborative_Task_Offloading_Optimization_for_Satellite_Mobile_Edge_Computing_Using_Multi-Agent_Deep_Reinforcement_Learning/Collaborative_Task_Offloading_Optimization_for_Satellite_Mobile_Edge_Computing_Using_Multi-Agent_Deep_Reinforcement_Learning.md`
- Original PDF and extracted figures (`images/`) in the same folder.
