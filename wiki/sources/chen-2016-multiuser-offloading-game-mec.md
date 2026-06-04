---
type: source
title: "Efficient Multi-User Computation Offloading for Mobile-Edge Cloud Computing"
authors: ["Xu Chen", "Lei Jiao", "Wenzhong Li", "Xiaoming Fu"]
year: 2016
url: "https://doi.org/10.1109/TNET.2015.2487344"
venue: "IEEE/ACM Transactions on Networking (IEEE/ACM ToN)"
tags: [source, task-offloading, game-theory, potential-game, mobile-edge-computing, multi-channel, nash-equilibrium]
related:
  - "[[potential-game]]"
  - "[[task-offloading]]"
  - "[[nash-equilibrium]]"
  - "[[chen-2015-decentralized-offloading-game]]"
created: 2026-06-04
updated: 2026-06-04
---

# Efficient Multi-User Computation Offloading for Mobile-Edge Cloud Computing

## Citation

Chen, X., Jiao, L., Li, W., & Fu, X. (2016). *Efficient Multi-User Computation Offloading for Mobile-Edge Cloud Computing*. **IEEE/ACM Transactions on Networking**, 24(5). DOI: 10.1109/TNET.2015.2487344. (Received 17 March 2015; accepted 29 September 2015; published 26 October 2015; current version 13 October 2016.)

## TL;DR

Extends the decentralized offloading game from a single-channel setting ([[chen-2015-decentralized-offloading-game]]) to a **multi-channel wireless interference environment**. Shows the multi-user computation offloading problem for mobile-edge cloud computing is NP-hard to solve centrally. Models it as a **multi-user computation offloading game**, proves it is a potential game (hence always has a Nash equilibrium with the finite improvement property), and proposes a distributed algorithm achieving NE with a bounded convergence time. Further extends to a **multi-channel wireless contention environment**. Proves the Nash equilibrium efficiency bound in terms of both beneficial-cloud-user count and system-wide overhead.

## Problem framing

Mobile-edge cloud computing (cloudlet-like servers at the edge of cellular macro/small-cell networks) enables low-latency offloading. With multiple users and multiple wireless channels, co-channel interference when many users pick the same channel degrades offloading efficiency. This paper shows centralized optimization of who offloads on which channel is NP-hard, motivating the game-theoretic distributed approach.

## System model

- **N collocated mobile users**, each with a computation task. M wireless channels. Users decide jointly: (0 = local, c ∈ {1…M} = offload on channel c).
- **Multi-channel interference model.** Users on the same channel cause SINR degradation; cost function captures weighted sum of processing time + energy.
- **Two access environments:** (a) interference model (SINR-based rate degradation from co-channel users); (b) contention model (random-access MAC: one user wins the channel per slot, others fail and must retry, incurring energy + delay overhead).
- **Game.** Multi-user computation offloading game: same potential-game structure as the single-channel version, extended to M channels.

## Method

- Constructs an explicit **potential function** for the multi-channel game; proves the game admits the finite improvement property and a Nash equilibrium.
- **Distributed algorithm:** each user locally measures interference/contention, computes best response, updates decision; converges to NE in a bounded number of steps (upper bound derived under mild conditions).
- Quantifies NE efficiency via two metrics: ratio of beneficial-cloud-user count, and ratio of system-wide computation overhead to optimal.
- Full extension to the contention environment in Section VI (distinct proof structure due to MAC layer randomness).

## Key findings

- The multi-user computation offloading game always possesses a **Nash equilibrium** under both interference and contention wireless models (parse Sections III–VI).
- The distributed algorithm achieves NE with **bounded convergence time** under mild conditions, and scales well with N in simulations (parse Section V, VII).
- The efficiency of the NE solution — measured in beneficial-cloud-user count and system-wide overhead — is bounded and demonstrated numerically to be close to the centralized optimum (parse Section V).

## Limitations / future work

Binary per-channel offloading (all-or-nothing on a chosen channel); partial offloading and multi-hop topologies deferred. The parse explicitly notes dynamic user arrivals/departures as future work.

## Relation to the corpus

Direct journal extension of [[chen-2015-decentralized-offloading-game]] to multi-channel MEC. Both papers establish [[potential-game]] theory for [[task-offloading]] under shared wireless interference — a design pattern followed by [[chen-2022-qoe-game-end-edge-cloud]] and [[he-2019-euagame-user-allocation]] in more recent corpus sources. The NP-hardness of centralized multi-user offloading motivates the game-theoretic distributed approach used widely in the corpus.

## Raw artifacts

- `raw/sources/Efficient_Multi-User_Computation_Offloading_for_Mobile-Edge_Cloud_Computing/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
