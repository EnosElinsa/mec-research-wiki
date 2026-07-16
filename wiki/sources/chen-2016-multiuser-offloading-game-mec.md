---
type: source
modeling_card: required
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
updated: 2026-07-16
---

# Efficient Multi-User Computation Offloading for Mobile-Edge Cloud Computing

## Citation

Chen, X., Jiao, L., Li, W., & Fu, X. (2016). *Efficient Multi-User Computation Offloading for Mobile-Edge Cloud Computing*. **IEEE/ACM Transactions on Networking**, 24(5). DOI: 10.1109/TNET.2015.2487344. (Received 17 March 2015; accepted 29 September 2015; published 26 October 2015; current version 13 October 2016.)

## TL;DR

Extends the decentralized offloading game from a single-channel setting ([[chen-2015-decentralized-offloading-game]]) to a **multi-channel wireless interference environment**. Shows the multi-user computation offloading problem for mobile-edge cloud computing is NP-hard to solve centrally. Models it as a **multi-user computation offloading game**, proves it is a potential game (hence always has a Nash equilibrium with the finite improvement property), and proposes a distributed algorithm achieving NE with a bounded convergence time. Further extends to a **multi-channel wireless contention environment**. Proves the Nash equilibrium efficiency bound in terms of both beneficial-cloud-user count and system-wide overhead.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: $N$ collocated mobile users each execute one task locally or offload it through one of $M$ base-station channels to a nearby telecom cloud; users sharing a channel create interference, and local and cloud costs combine execution time and energy.

**Problem & objective**: The centralized problems maximize beneficial cloud users or minimize system overhead, including $\min_{\mathbf a}\sum_{n\in\mathcal N}Z_n(\mathbf a)$, while the decentralized multi-user computation offloading game lets every user minimize its own $Z_n(a_n,a_{-n})$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Offloading and channel choice | $a_n$ | Discrete, $\{0,1,\ldots,M\}$ | $a_n=0$ selects local computing; $a_n=m>0$ offloads through channel $m$. |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Every user selects exactly one action from $\mathcal A_n=\{0,1,\ldots,M\}$. |
| C2 | A cloud choice is beneficial only if $K_n^c(\mathbf a)\le K_n^m$, equivalently if received co-channel interference does not exceed $T_n$. |
| C3 | Uplink rate follows the co-channel interference model in (1), coupling every offloading user's time and energy cost to the other users on its channel. |
| C4 | At equilibrium, $Z_n(a_n^*,a_{-n}^*)\le Z_n(a_n,a_{-n}^*)$ for every unilateral alternative $a_n$. |

**Algorithm**: The distributed algorithm measures interference on all channels, lets users compute improving best responses, grants one requesting user an update opportunity per decision slot, and stops at a Nash equilibrium by the finite improvement property.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Chen et al. [x] studied multi-user computation offloading in a multi-channel mobile-edge cloud where co-channel users interfere with one another. They formulated centralized objectives for maximizing beneficial cloud users and minimizing system-wide delay-energy overhead, then recast individual local-or-channel choices as a potential game. Their distributed algorithm measures channel interference and applies asynchronous improving best responses until reaching a Nash equilibrium with a bounded convergence time. Numerical results report up to 30% more beneficial cloud users than the all-cloud policy, at most 12% and 14% losses relative to centralized optimization on the two evaluation metrics, and nearly linear empirical growth in convergence slots with user count.

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
