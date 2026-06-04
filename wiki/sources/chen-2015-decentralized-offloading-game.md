---
type: source
title: "Decentralized Computation Offloading Game for Mobile Cloud Computing"
authors: ["Xu Chen"]
year: 2015
url: "https://doi.org/10.1109/TPDS.2014.2316834"
venue: "IEEE Transactions on Parallel and Distributed Systems (IEEE TPDS)"
tags: [source, task-offloading, game-theory, potential-game, mobile-cloud-computing, decentralized-optimization]
related:
  - "[[potential-game]]"
  - "[[task-offloading]]"
  - "[[binary-vs-partial-offloading]]"
  - "[[nash-equilibrium]]"
created: 2026-06-04
updated: 2026-06-04
---

# Decentralized Computation Offloading Game for Mobile Cloud Computing

## Citation

Chen, X. (2015). *Decentralized Computation Offloading Game for Mobile Cloud Computing*. **IEEE Transactions on Parallel and Distributed Systems**, 26(4). DOI: 10.1109/TPDS.2014.2316834. (Received 29 Oct 2013; accepted 5 Apr 2014; published 10 Apr 2014; current version 6 Mar 2015.)

## TL;DR

Multiple mobile device users share a wireless access link to a cloud (e.g., Amazon EC2). If too many users offload simultaneously they create mutual interference, reducing rates and defeating the benefit of offloading. The paper models this as a **decentralized computation offloading game**, proves it always admits a Nash equilibrium (via beneficial cloud-computing group structure for homogeneous access, and potential-game theory for heterogeneous access), and designs an efficient decentralized mechanism that converges in O(N log N) time. Numerical results show the Nash equilibrium achieves at most ~10% performance loss versus the centralized optimum.

## Problem framing

Resource-hungry mobile applications (face recognition, augmented reality, NLP) exceed local device capabilities. Mobile cloud computing offloads computation tasks to remote cloud VMs. However, multiple simultaneous offloaders cause wireless interference at the shared base station, degrading data rates and potentially making local execution preferable. Centralized scheduling requires all users to submit private information to the cloud; this paper advocates a **decentralized game-theoretic** approach where each user decides locally.

## System model

- **Users.** N collocated mobile users, each with a computation task T_n = (B_n, D_n): input data size B_n and CPU cycles D_n. Tasks are binary (execute fully local or fully remote).
- **Communication.** Shared uplink base station; SINR-based rate model — simultaneous offloaders create mutual interference via a Shannon capacity formula. Users have heterogeneous power levels and channel gains H_{n,s}.
- **Cost function.** Weighted sum of processing time and energy, with user-specific weights γ_T, γ_E (supporting battery-state adaptation). Local cost Z_n^l vs. cloud cost Z_n^c(a) (which depends on the joint offloading decisions a of all users).
- **Game.** Strategic game Γ = (N, {A_n}, {V_n}): players are users, actions are {0=local, 1=cloud}, payoff is the cost to be minimized.

## Method

- **Homogeneous access:** Game admits a "beneficial cloud computing group" structure; Nash equilibrium can be constructed in O(N log N) via a simple greedy algorithm (Algorithm 1).
- **Heterogeneous access:** Game is shown to be a **potential game** ([[potential-game]]) with an explicit potential function Φ(a). The finite improvement property guarantees convergence of any asynchronous better-response update to a Nash equilibrium.
- **Decentralized mechanism (Algorithm 2):** Each user measures local interference, computes a best-response update, and uses random-backoff contention to serialize updates. Converges to Nash equilibrium in a finite number of iterations; empirically linear in N.
- **Price of Anarchy (PoA):** Bounded by sum of local costs divided by sum of per-user minimum costs — shown to be at most ~10% overhead in the numerical setting studied.

## Key findings

- The game **always admits a Nash equilibrium** in both homogeneous and heterogeneous wireless access cases (Theorems 1, 2 in the parse).
- The decentralized mechanism achieves **at most ~10% performance loss** compared with the centralized optimal solution (parse Section 5.2 and numerical results).
- Convergence iterations scale **linearly with N** in numerical experiments, suggesting practical scalability (parse Section 6).
- The Nash equilibrium is efficiently reachable without a central coordinator; mobile users self-organize into a mutually satisfactory offloading arrangement (parse Section 5).

## Limitations / future work

Binary offloading only (no partial task split). Quasi-static user set during one offloading period (dynamic arrivals/departures deferred to future work, explicitly stated in parse Section 3). Cloud execution capacity F_n^c is treated as given, not co-optimized.

## Relation to the corpus

A foundational early work establishing [[potential-game]] theory for multi-user [[task-offloading]] decisions under shared-channel interference — a design pattern that appears in several later corpus sources using more sophisticated game formulations ([[bargaining-game]], [[stackelberg-game]], [[stochastic-game]]). Precedes MEC-era works; the "cloud" here is a remote data center rather than an edge server, but the interference-coupled offloading game structure transfers directly to MEC settings.

## Raw artifacts

- `raw/sources/Decentralized_Computation_Offloading_Game_for_Mobile_Cloud_Computing/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
