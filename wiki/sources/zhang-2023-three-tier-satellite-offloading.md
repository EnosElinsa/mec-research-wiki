---
type: source
title: "Partial Computation Offloading in Satellite-Based Three-Tier Cloud-Edge Integration Networks"
authors: ["Yaomin Zhang", "Haijun Zhang", "Kai Sun", "Jiahao Huo", "Ning Wang", "Victor C. M. Leung"]
year: 2023
url: "https://doi.org/10.1109/TWC.2023.3282630"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, leo-satellite-edge-computing, task-offloading, binary-vs-partial-offloading, three-tier-cloud-edge-end, noma, fractional-programming-dinkelbach, energy-latency-tradeoff]
related:
  - "[[leo-satellite-edge-computing]]"
  - "[[task-offloading]]"
  - "[[binary-vs-partial-offloading]]"
  - "[[three-tier-cloud-edge-end]]"
  - "[[noma]]"
  - "[[fractional-programming-dinkelbach]]"
  - "[[energy-latency-tradeoff]]"
  - "[[non-terrestrial-network]]"
  - "[[zhou-2024-mco-satellite-edge-offloading]]"
  - "[[zhang-2024-mhspo-satellite-peer-offloading]]"
  - "[[wang-2024-satellite-terrestrial-computing]]"
  - "[[zhang-2025-three-tier-maritime-offloading]]"
  - "[[you-2017-meco-resource-allocation]]"
  - "[[wang-2016-partial-offloading-dvs]]"
created: 2026-06-02
updated: 2026-06-02
---

# Partial Computation Offloading in Satellite-Based Three-Tier Cloud-Edge Integration Networks

## Citation

Zhang, Y., Zhang, H., Sun, K., Huo, J., Wang, N., & Leung, V. C. M. (2023). *Partial Computation Offloading in Satellite-Based Three-Tier Cloud-Edge Integration Networks*. **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2023.3282630. (Manuscript received 30 November 2022; revised 6 April 2023; accepted 23 May 2023; date of publication 9 June 2023; date of current version 13 February 2024 → year 2023.)

## TL;DR

Constructs a **three-tier cloud-edge integration network** in which remote ground UEs offload computation, under a **data-partition partial-offloading (PO)** model, to a **LEO-satellite-based edge server** and further to a **ground cloud server** over a backhaul link. The objective is to **minimize total system energy consumption** by jointly optimizing **user association, power allocation, task scheduling (bit splitting), and backhaul bandwidth assignment**. The coupled non-convex problem is decomposed into four subproblems — solved respectively by **relaxation transformation**, the **quadratic-transform** method for the sum-of-ratio power objective, upper/lower-bound task scheduling, and CVX-based bandwidth assignment — and combined in a **joint iterative (block-coordinate-style) algorithm** whose energy is non-increasing per iteration and hence convergent.

## Problem framing

LEO-satellite communication extends network service to remote areas without terrestrial infrastructure, but offloading there is constrained by **scarce spectrum** and **precious satellite energy**. The paper argues that most prior satellite-offloading work optimizes power/task scheduling between only two computing entities (UE–cloud or UE–MEC) and **ignores bandwidth assignment between the edge-offloading and cloud-offloading paths**. It therefore studies all of power, bandwidth, user association, and task scheduling **systematically together** in a three-tier (local UE / LEO edge / ground cloud) setting, with energy minimization as the goal.

## System model

- **Architecture.** `S` LEO satellites (edge servers) at altitude `H^S` serve `U` randomly-located remote ground UEs (no terrestrial infrastructure); each LEO relays further to a ground cloud server via backhaul. A task can run in parallel across **local UE, LEO edge, and cloud** under data-partition PO.
- **Communication.** Fronthaul (UE→LEO) uses **NOMA** with successive interference cancellation (SIC), decoding ordered by uplink channel quality; backhaul (LEO→cloud) uses **orthogonal multiple access** to avoid inter-LEO interference. A backhaul-bandwidth assignment factor `α` splits the system bandwidth `B` between fronthaul and backhaul.
- **Computation/energy.** Per-tier delay and energy are modeled for local (`κ^L f^2`-style), LEO-edge (transmission + computation + round-trip propagation, with overhead coefficient `β`), and cloud (relayed via the satellite). System energy is a weighted sum across UE/LEO/cloud (weights `w^L`, `w^S`, `w^C`).
- **Problem.** Minimize `Σ e_u` over `{a_{u,s}, p_{u,s}, p_{s,c}, l^S_u, l^C_u, α}` subject to single-LEO association (binary), UE/LEO peak-power caps, bit-budget constraints, a fronthaul-vs-backhaul rate constraint, and per-mode (local/edge/cloud) delay deadlines. The problem is highly non-convex (coupled variables, binary association, fractional sums).

## Method

- **User association.** Per-UE local minimization; binary association is relaxed to `[0,1]` and the per-UE objective becomes a convex linear program solved by CVX (Algorithm 1).
- **Power allocation.** The sum-of-ratio power objective is handled by the **quadratic-transform** method (stable, equivalent for fractional/sum-of-ratio problems), iterated to convergence (Algorithm 2).
- **Task scheduling.** Optimal bit allocation `{l^S_u, l^C_u}` derived via formulated upper/lower bounds (Algorithm 3).
- **Bandwidth assignment.** The residual problem in `α` is transformed into a convex form and solved directly by CVX.
- **Joint iteration.** Algorithm 4 cycles the four subproblems (block-coordinate descent), each solved with the others fixed; system energy is proved **non-increasing and lower-bounded**, hence convergent. Reported overall complexity is `O(INSU + IKLSU + IMU + I)`.

## Key findings

- The joint iterative algorithm **converges in a few iterations** (Fig. 3: stable energy by ~3–4 iterations for `L_u = 1` MB and immediately for `2` MB; values figure-derived, treat as indicative).
- The proposed three-tier PO scheme yields **lower system energy** than four baselines: two-tier computation offloading (TTCO, cloud disabled), greedy cloud offloading (GCO), maximum-SNR association (Max-SNR), and maximum-power allocation (MPA). The gap over MPA widens as the UE count grows from 20 to 200 (Fig. 5), because joint power allocation curbs the NOMA interference that MPA's full-power transmission aggravates. Margins are figure-derived; treat exact numbers as indicative.
- Simulation setup (parse): 5 LEOs over a 1.2 km × 1.2 km area at 784 km altitude, Ka-band 20 GHz, 500 MHz total bandwidth, UE/LEO peak power 23/43 dBm, 1 MB tasks, 3 s deadline, 100 cycles/bit, UE 0.1 / LEO 5 / cloud 10 Gcycles/s.

## Limitations / future work

A **quasi-static** model is assumed (UEs and satellites stationary within a PO cycle, deterministic tasks), so LEO mobility and dynamic task arrivals are out of scope. The solution is an iterative local-optimum scheme (per-subproblem convexity, not joint global optimality), and evaluation is simulation-only. Explicit future-work statements are `not in parse`.

## Relation to the corpus

A **satellite three-tier offloading** entry whose GEO-free GroundUE / LEO-edge / ground-cloud stack is a satellite instance of [[three-tier-cloud-edge-end]], distinct from the **maritime** three-tier scheme of [[zhang-2025-three-tier-maritime-offloading]] (different first author, sea-surface devices) and from the mobility-first ADMM offloading of [[zhou-2024-mco-satellite-edge-offloading]]. Like [[zhang-2024-mhspo-satellite-peer-offloading]] and [[wang-2024-satellite-terrestrial-computing]] it targets energy-efficient [[leo-satellite-edge-computing]] within the [[non-terrestrial-network]] context, but uniquely centers **fronthaul/backhaul bandwidth assignment** alongside NOMA association and bit-splitting. Its [[binary-vs-partial-offloading|partial-offloading]] data-partition model and energy objective echo [[wang-2016-partial-offloading-dvs]] and the threshold offloading policy of [[you-2017-meco-resource-allocation]]; the sum-of-ratio power step is solved by the quadratic transform from the [[fractional-programming-dinkelbach]] family, and [[noma]] supplies the fronthaul multiple-access.

## Raw artifacts

- `raw/sources/Partial_Computation_Offloading_in_Satellite-Based_Three-Tier_Cloud-Edge_Integration_Networks/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
