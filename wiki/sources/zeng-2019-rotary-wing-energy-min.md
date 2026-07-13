---
type: source
title: "Energy Minimization for Wireless Communication With Rotary-Wing UAV"
authors: ["Yong Zeng", "Jie Xu", "Rui Zhang"]
year: 2019
url: "https://doi.org/10.1109/TWC.2019.2902559"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags:
  - source
  - uav-communications
  - rotary-wing-uav
  - energy-model
  - trajectory-optimization
  - alternating-optimization-sdr-sca
related:
  - "[[uav-trajectory-control]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[energy-latency-tradeoff]]"
  - "[[blockage-aware-channel-model]]"
  - "[[rotary-wing-propulsion-energy-model]]"
  - "[[uav-data-collection]]"
  - "[[zeng-2019-uav-comm-tutorial-5g]]"
  - "[[liu-2022-miso-uav-mec-trajectory]]"
  - "[[zhang-2019-uav-iot-comp-comm]]"
  - "[[li-2024-rldc-uav-swarm-clustering]]"
  - "[[yong-zeng]]"
  - "[[jie-xu]]"
created: 2026-05-31
updated: 2026-07-14
---

# Energy Minimization for Wireless Communication With Rotary-Wing UAV

## Citation

Zeng, Y., Xu, J., & Zhang, R. (2019). *Energy Minimization for Wireless Communication With Rotary-Wing UAV*. **IEEE Transactions on Wireless Communications**, 18(4), 2329–2345. DOI: 10.1109/TWC.2019.2902559. (Date of publication 8 Mar 2019; current version 9 Apr 2019. Presented in part at IEEE GLOBECOM 2018, Abu Dhabi.)

## TL;DR
A foundational UAV-communications paper that derives the **closed-form propulsion-power model for rotary-wing UAVs** and uses it to minimize a UAV's total energy (propulsion + communication) while meeting each ground node's (GN) throughput requirement, by jointly optimizing the UAV **trajectory**, **communication time allocation**, and **mission completion time**. Two designs: a simple **fly-hover-communicate** scheme (solved via the travelling-salesman-problem-with-neighborhood, TSPN, + convex optimization) and a general **communicate-while-flying** scheme (solved via a novel **path discretization** + [[alternating-optimization-sdr-sca|successive convex approximation, SCA]]). Both beat benchmark schemes; this is the canonical source for the rotary-wing propulsion model reused widely in UAV-MEC papers.

## Problem
UAV-enabled wireless communication is limited by the UAV's **on-board energy**, which (unlike a terrestrial base station) must also cover **propulsion** to stay airborne and move. Prior energy-efficient UAV work derived a model only for **fixed-wing** UAVs (power convex in speed `V`, infinite at `V = 0`) and considered a single GN. Rotary-wing UAVs have fundamentally different mechanics — they can **hover** (finite power at `V = 0`) — so their power model and trajectory design differ. The paper studies a rotary-wing UAV dispatched as a flying access point to serve **multiple** GNs, each with a target number of information bits, and minimizes total UAV energy (propulsion + communication) subject to each GN's throughput requirement — a non-convex problem with infinitely many time-coupled variables.

## System model
- A single rotary-wing UAV at constant altitude `H` serves `K` GNs over **TDMA** (one GN scheduled per instant); UAV horizontal trajectory `q(t)`, max speed `V_max`.
- **Channel:** probabilistic LoS/NLoS air-to-ground large-scale model (LoS probability a logistic function of elevation angle) plus small-scale fading; expected rate via Jensen's inequality, leading to a tractable rate constraint with a regularized LoS probability and general path-loss exponent `α̃ ≥ 2` ([[blockage-aware-channel-model]]).
- **Rotary-wing propulsion power model** (the paper's signature result, [[rotary-wing-propulsion-energy-model]]):
  `P(V) = P₀(1 + 3V²/U_tip²)` (blade profile) `+ P_i(√(1 + V⁴/4v₀⁴) − V²/2v₀²)^{1/2}` (induced) `+ ½ d₀ρsAV³` (parasite).
  Hovering power `P_h = P₀ + P_i` is **finite**; `P(V)` is **neither convex nor concave** and first decreases then increases with `V` (hovering is not the most power-conserving state).
- Communication-related UAV power fixed at `P_c = 5 W`; altitude `H = 100 m` (FAA <400 ft); `B = 1 MHz`; `P = 20 dBm`.

## Method
- **Fly-hover-communicate design:** UAV visits a set of optimized hovering locations, communicating only while hovering. Reduces to choosing hovering locations + durations + visiting order + flying speed; includes the classic NP-hard TSP, solved approximately via a TSPN algorithm + convex optimization.
- **Communicate-while-flying (general) design:** a novel **path discretization** transforms the infinite-variable problem into a finite one **without pre-specifying mission completion time** (unlike the usual time discretization) — useful because completion time is itself an optimization variable; the resulting non-convex problem is solved by **SCA** (Algorithm 2), converging to a KKT point. Remark: the same algorithm extends to **mission-completion-time minimization**.

## Key findings
- Optimized hovering locations generally differ from the GN locations, reflecting an energy-vs-communication-time tradeoff (hovering above a GN minimizes link distance but lengthens flight).
- The SCA upper bound from solving the convex surrogate is practically tight (matches exact energy) and converges in a few iterations (parse, Fig. 3).
- The optimized fly-hover-communicate scheme beats "hovering at geometric center" and "hovering above GNs" benchmarks; enabling continuous communication ("optimized path, continuous commun.") beats fly-hover; and the full SCA design saves further energy by balancing instantaneous power minimization against rate maximization (parse, Fig. 7).
- Establishes that, unlike fixed-wing UAVs, hovering is feasible but not the most energy-efficient state for rotary-wing UAVs.

## Limitations / future work
Single rotary-wing UAV at fixed altitude (altitude optimization left as future work); the propulsion model is derived for a specific rotary-wing regime (generalization to more general power models noted as non-trivial); homogeneous-LoS-probability approximation used to keep the rate constraint tractable; simulation/numerical validation (no hardware).

## Relation to the corpus
This is the **origin paper for the rotary-wing propulsion-energy model** (`P₀`, `P_i`, blade-profile/induced/parasite terms) that recurs across the corpus's UAV-MEC energy formulations — including [[li-2024-rldc-uav-swarm-clustering]] (which cites it as its propulsion reference [10]) and the SCA/AO trajectory pipeline of [[liu-2022-miso-uav-mec-trajectory]] and [[zhang-2019-uav-iot-comp-comm]]. Methodologically it anchors the [[alternating-optimization-sdr-sca]] / TSPN convex-optimization track. By Yong Zeng, [[jie-xu]], and Rui Zhang, it is a sibling of the foundational tutorial [[zeng-2019-uav-comm-tutorial-5g]] and the [[uav-data-collection]] / [[uav-trajectory-control]] design space. Matching education and career biographies connect Jie Xu's Guangdong University of Technology affiliation here to his later CUHK-Shenzhen ISAC work.

## Raw artifacts
- `raw/sources/Energy_Minimization_for_Wireless_Communication_With_Rotary-Wing_UAV/full.md`
- Original PDF and extracted figures in the same folder.
