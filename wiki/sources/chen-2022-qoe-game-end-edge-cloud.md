---
type: source
title: "QoE-Aware Decentralized Task Offloading and Resource Allocation for End-Edge-Cloud Systems: A Game-Theoretical Approach"
authors: ["Ying Chen", "Jie Zhao", "Yuan Wu", "Jiwei Huang", "Xuemin Shen"]
year: 2022
url: "https://doi.org/10.1109/TMC.2022.3223119"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, task-offloading, three-tier-cloud-edge-end, potential-game, nash-equilibrium, qoe-modeling-mec, price-of-anarchy, game-theory]
related:
  - "[[task-offloading]]"
  - "[[three-tier-cloud-edge-end]]"
  - "[[potential-game]]"
  - "[[nash-equilibrium]]"
  - "[[qoe-modeling-mec]]"
  - "[[price-of-anarchy]]"
  - "[[mobile-edge-computing]]"
  - "[[chen-2024-ulse-game]]"
  - "[[chen-2023-dotora-air-ground-online]]"
  - "[[he-2019-euagame-user-allocation]]"
  - "[[ye-2025-aigc-diffusion-contract]]"
  - "[[game-theoretic-offloading-formulations]]"
created: 2026-06-02
updated: 2026-06-02
---

# QoE-Aware Decentralized Task Offloading and Resource Allocation for End-Edge-Cloud Systems: A Game-Theoretical Approach

## Citation

Chen, Y., Zhao, J., Wu, Y., Huang, J., & Shen, X. (2022). *QoE-Aware Decentralized Task Offloading and Resource Allocation for End-Edge-Cloud Systems: A Game-Theoretical Approach*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2022.3223119. (Manuscript received 24 May 2022; revised 15 November 2022; accepted 15 November 2022; date of publication 18 November 2022; date of current version 5 December 2023 → year 2022.)

## TL;DR

Studies **multi-user task offloading in an end-edge-cloud system** where all user devices (UDs) compete for limited communication channels and edge compute. The goal is to **maximize the sum Quality of Experience (QoE)** of users under resource constraints. Because each UD is self-interested, the problem is recast as a **Multi-User Task Offloading Game (MUTO-Game)**; the authors prove (via an upper bound on both interference and computing-resource competition) that the game is a **potential game** with at least one **Nash Equilibrium**, and propose the distributed **Game-based Decentralized Task Offloading (GDTO)** algorithm to reach one. They bound GDTO's convergence-time (iteration count) and characterize worst-case quality via the **Price of Anarchy (PoA)**.

## Problem framing

Computation-intensive apps (AR/VR) exceed UD compute/battery budgets. Offloading everything to a distant cloud raises delay and burdens the core network; edge servers are closer but capacity-limited, so they are backed by a cloud that absorbs overflow. In this end-edge-cloud setting, all UDs **compete** for scarce transmission channels and edge compute, each maximizing its own benefit — making a balanced, system-good offloading strategy hard. Centralized optimization suffers exponential solution-space growth with more UDs/channels, and heuristics give no guaranteed gap to the optimum. The paper targets a decentralized strategy with provable equilibrium existence and a worst-case performance guarantee.

## System model

- **Actors.** `n` UDs and `m` base stations, each BS co-located with an edge server and offering `c_j` wireless channels; UDs are pre-assigned to a BS. Each UD has a task `(B_i, X_i, δ_i)` (bits, CPU cycles, assigned BS).
- **Offloading decision.** `a_i = (λ_i, k_i)`: `(0,0)` = local; `λ_i=1` = edge; `λ_i=2` = cloud (relayed via the BS); `k_i` selects the wireless channel. Cloud compute delay is neglected (assumed ample).
- **Communication.** UDs sharing a channel interfere (SINR → Shannon rate); a minimum-rate floor `r_min` aborts a transmission below it.
- **Computation.** Edge compute is **shared by weight** `γ_i` among UDs offloading to the same server (with a minimum-allocation floor `f_min`); local/edge delays and energy follow standard `X_i/f` and `ρ_i X_i` forms.
- **QoE.** Per-UD cost `Cost_i = τ^t_i T_i + τ^e_i EC_i` (delay + energy, weights summing to 1); QoE is a **logarithmic, negatively-correlated** function of cost bounded in `[E_min, E_max]`. Objective: `max Σ E_{a_{-i}}(a_i)` subject to the rate and compute-allocation constraints. The problem is NP-hard.

## Method

- **Game reformulation.** MUTO-Game `P = (U, {A_i}, {E_i})`: players are UDs, each maximizing own QoE; the solution concept is the Nash Equilibrium.
- **Potential-game proof.** Lemma 1 bounds each UD's communication interference and degree of computing-resource competition; Theorem 1 (six cases) exhibits a potential function, so MUTO-Game is a **potential game** with the **finite improvement property** and ≥1 NE.
- **GDTO algorithm.** Distributed best-response iteration: each UD computes its best decision in parallel, then UDs that improve compete for an update slot (one winner updates per round) until no UD wants to change.
- **Analysis.** Theorem 2 gives an upper bound on the number of iterations (so per-iteration cost `O(c_max)`); Theorem 3 lower-bounds the **Price of Anarchy** (worst-NE QoE / centralized-optimal QoE), the worst-case performance guarantee.

## Key findings

- The iteration count to reach an NE grows **sub-linearly** as the offloading solution-space size grows exponentially (parse).
- **Small-scale:** GDTO's QoE is **close to the centralized optimal** solution.
- **Large-scale:** GDTO outperforms four approximate baselines. Specific numeric margins are figure/experiment-derived; treat exact values as indicative.

## Limitations / future work

Evaluation is **simulation/experiment-only**. The model assumes **UDs are pre-assigned to a BS**, **ignores queueing delay** (one task per device), and **neglects cloud computation delay**; the guarantee is a worst-case PoA bound rather than optimality, and the per-round update picks a single winner among improving UDs. Explicit future-work statements are `not in parse`.

## Relation to the corpus

A **game-theoretic end-edge-cloud offloading** entry whose local/edge/cloud structure is an instance of [[three-tier-cloud-edge-end]]. It is by the same first author as the UAV-LEO potential-game paper [[chen-2024-ulse-game]] and the air-ground online-offloading paper [[chen-2023-dotora-air-ground-online]] (shared co-authors yuan-wu, Jiwei Huang, [[xuemin-shen]]); like [[chen-2024-ulse-game]] it uses a **[[potential-game]] with a [[nash-equilibrium]] guarantee and distributed best-response dynamics**, and both quantify worst-case efficiency via [[price-of-anarchy]] — feeding the [[game-theoretic-offloading-formulations]] comparison alongside [[he-2019-euagame-user-allocation]]. Its [[qoe-modeling-mec|QoE]] objective (a bounded log-of-cost utility) is a distinct reward shape from the diffusion-contract QoE of [[ye-2025-aigc-diffusion-contract]], extending [[mobile-edge-computing]] offloading theory.

## Raw artifacts

- `raw/sources/QoE-Aware_Decentralized_Task_Offloading_and_Resource_Allocation_for_End-Edge-Cloud_Systems_A_Game-Theoretical_Approach/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
