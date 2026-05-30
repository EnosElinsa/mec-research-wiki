---
type: source
title: "Data Offloading in UAV-Assisted Multi-Access Edge Computing Systems Under Resource Uncertainty"
authors: ["Pavlos Athanasios Apostolopoulos", "Georgios Fragkos", "Eirini Eleni Tsiropoulou", "Symeon Papavassiliou"]
year: 2021
url: "https://doi.org/10.1109/TMC.2021.3069911"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, uav-mec, data-offloading, prospect-theory, nash-equilibrium, convex-optimization, computing-uncertainty]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[prospect-theory]]"
  - "[[nash-equilibrium]]"
  - "[[binary-vs-partial-offloading]]"
  - "[[task-offloading]]"
  - "[[energy-latency-tradeoff]]"
  - "[[he-2019-euagame-user-allocation]]"
created: 2026-05-31
updated: 2026-05-31
---

# Data Offloading in UAV-Assisted Multi-Access Edge Computing Systems Under Resource Uncertainty

## Citation

Apostolopoulos, P. A., Fragkos, G., Tsiropoulou, E. E., & Papavassiliou, S. (2021). *Data Offloading in UAV-Assisted Multi-Access Edge Computing Systems Under Resource Uncertainty*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2021.3069911.

> **Metadata note:** the parse has no `Digital Object Identifier` header line, but an appendix-reference link inside the parse points to `10.1109/TMC.2021.3069911` (IEEE TMC), and the DOI/venue were web-confirmed against the authors' record. Year 2021 follows the DOI-embedded year per the wiki convention.

## TL;DR

A risk-aware **partial data-offloading** framework where each user can split its data among local computing, a **ground MEC server** (a *guaranteed* slice of resources), and **UAV-mounted MEC servers** (a *common pool of resources* with potentially superior but uncertain payoff). User behavior is modeled with **Prospect Theory** ([[prospect-theory]]) so that decisions reflect real-life risk-seeking / loss-aversion under uncertainty rather than pure expected-utility maximization. Each user maximizes a prospect-theoretic satisfaction utility; because users compete for shared resources, the problem is a **non-cooperative game** whose **Pure Nash Equilibrium (PNE)** is proven to exist and be unique, with a distributed low-complexity algorithm that converges to it.

## Problem framing

Most prior UAV-MEC offloading work assumes **rational** users who blindly maximize utility and ignores the **uncertainty** of UAV-mounted server resources (constrained by UAV energy, the servers can fail to serve / over-exploit). The paper fills this gap by (1) treating UAV-mounted servers as a Common Pool of Resources (CPR) with probabilistic payoff, subject to the *Tragedy of the Commons* when over-used; (2) keeping local computing and ground MEC servers as safe/guaranteed options; and (3) modeling each user's risk-aware behavior via prospect-theoretic utility, capturing latency/energy requirements and their perception of gains and losses.

## System model

- **Servers.** A set of ground MEC servers $\mathbb{G}$ (attached to base stations, guaranteed slice per user) and a set of UAV-mounted MEC servers $\mathbb{F}$ (CPR, superior-but-uncertain payoff from better channel proximity), plus local computing — the union $\mathbb{S} = \mathbb{G}\cup\mathbb{F}$, $S=G+F$.
- **Users.** Set $\mathbb{U}$; each user partially offloads data across the available options ([[binary-vs-partial-offloading|partial offloading]], contrasted with binary offloading).
- **Uncertainty.** UAV-server payoff is probabilistic, depending on the computing load/congestion at the UAV servers, which may fail under energy constraints.
- **Utility.** Each user's prospect-theoretic satisfaction combines the expected prospect utility from UAV-mounted servers with the time/energy overhead of ground-server offloading and local execution.

## Method

- **Prospect-theoretic utility functions** encode risk-aware behavior (gain/loss domains, probabilistic payoff) — [[prospect-theory]].
- The optimal per-user data allocation is a **convex optimization** of satisfaction utility; because users compete for shared UAV/ground resources, it is treated as a **non-cooperative game**.
- The **existence and uniqueness of a Pure Nash Equilibrium** ([[nash-equilibrium]]) is proven, and a **distributed low-complexity algorithm** that converges to the PNE is proposed.

## Key findings

- The system converges to the **PNE in only a few iterations** (parse abstract / numerical results).
- Accounting for user risk-awareness and computing uncertainty leads to a more **sophisticated exploitation of system resources** and superior experienced performance vs alternative approaches.
- The impact of **user-behavior heterogeneity** (different risk profiles) on the equilibrium is evaluated.

## Limitations / future work

Simulation-based; the parse's contributions/results do not enumerate explicit limitations beyond the modeled assumptions (rational-within-prospect users, known type structure, CPR failure model).

## Relation to the corpus

A **game-theoretic, behavior-aware** offloading entry that is methodologically distinct from the rest of the corpus: it introduces [[prospect-theory]] (risk-aware decision-making under uncertainty) as a new vocabulary item, contrasting with the expected-utility / cost-minimization framing of nearly every other offloading source. Its non-cooperative-game + PNE structure parallels the potential-game treatments ([[he-2019-euagame-user-allocation]], [[chen-2024-ulse-game]]) and the coalition game in [[lyu-2023-noma-marine-emergency-offloading]], while its ground-vs-UAV-server heterogeneity echoes the multi-tier offloading in [[zhang-2025-three-tier-maritime-offloading]]. Reinforces [[multi-uav-assisted-mec]] and [[binary-vs-partial-offloading]].

## Raw artifacts

- `raw/sources/Data_Offloading_in_UAV-Assisted_Multi-Access_Edge_Computing_Systems_Under_Resource_Uncertainty/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
