---
type: source
modeling_card: required
title: "Joint Trajectory and Communication Design for Multi-UAV Enabled Wireless Networks"
authors: ["Qingqing Wu", "Yong Zeng", "Rui Zhang"]
year: 2018
url: "https://doi.org/10.1109/TWC.2017.2789293"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, multi-uav-assisted-mec, aerial-base-station, trajectory-design, power-control, user-scheduling, min-rate-fairness, block-coordinate-descent]
related:
  - "[[qingqing-wu]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[uav-trajectory-control]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[mixed-integer-nonlinear-programming]]"
  - "[[fairness-metrics-in-mec]]"
  - "[[zeng-2019-uav-comm-tutorial-5g]]"
  - "[[zeng-2019-rotary-wing-energy-min]]"
  - "[[chang-2022-marl-multiuav-trajectory]]"
  - "[[hu-2019-pdd-uav-mec-offloading]]"
created: 2026-05-31
updated: 2026-07-16
---

# Joint Trajectory and Communication Design for Multi-UAV Enabled Wireless Networks

## Citation

Wu, Q., Zeng, Y., & Zhang, R. (2018). *Joint Trajectory and Communication Design for Multi-UAV Enabled Wireless Networks*. **IEEE Transactions on Wireless Communications**, 17(3), 2109–2121. DOI: 10.1109/TWC.2017.2789293. (Date of publication 5 Jan 2018; date of current version 8 Mar 2018. Presented in part at IEEE GLOBECOM 2017.)

## TL;DR

A foundational **multi-UAV communications** paper where multiple UAV-mounted aerial base stations serve ground users sharing one frequency band. To achieve **fairness**, it **maximizes the minimum average throughput (max-min rate)** over all ground users in the downlink by jointly optimizing multiuser **communication scheduling + association**, **UAV trajectories**, and **transmit power control**. The mixed-integer non-convex problem is solved by an iterative **block coordinate descent (BCD) + successive convex optimization** algorithm (guaranteed to converge), with a **circular-trajectory + circle-packing** initialization scheme.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Multiple fixed-altitude UAV base stations share one downlink band and serve ground users in periodic TDMA slots, with return-to-start trajectories and collision avoidance.

**Problem & objective**: The max-min fairness formulation maximizes the minimum user average rate, $\max_{\eta,\mathbf A,\mathbf Q,\mathbf P}\eta$, where each user's average throughput is at least $\eta$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Scheduling and association | $\alpha_{k,m}[n]$ | binary | UAV $m$ serves user $k$ in slot $n$ |
| UAV trajectory | $\mathbf q_m[n]$ | continuous, speed bounded | UAV position over the period |
| Transmit power | $p_m[n]$ | continuous, $[0,P_{max}]$ | UAV downlink power |
| Fairness auxiliary | $\eta$ | continuous | Minimum average user rate |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Each user's average rate is at least $\eta$. |
| C2 | At most one user is scheduled by a UAV in a slot: $\sum_k\alpha_{k,m}[n]\leq1$. |
| C3 | At most one UAV serves a user in a slot: $\sum_m\alpha_{k,m}[n]\leq1$. |
| C4 | Scheduling is binary: $\alpha_{k,m}[n]\in\{0,1\}$. |
| C5 | Trajectories obey speed and periodic return: $\lVert\mathbf q_m[n+1]-\mathbf q_m[n]\rVert^2\leq S_{max}^2$ and $\mathbf q_m[1]=\mathbf q_m[N]$. |
| C6 | UAVs maintain separation: $\lVert\mathbf q_m[n]-\mathbf q_j[n]\rVert^2\geq d_{min}^2$. |
| C7 | Transmit power obeys $0\leq p_m[n]\leq P_{max}$. |

**Algorithm**: Relax binary scheduling, alternately solve scheduling with linear programming, trajectory and power with successive convex optimization, and initialize with circular trajectories and circle packing before reconstructing a binary solution.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Wu et al. [x] formulate multi-UAV downlink control as max-min average-rate optimization for users sharing one frequency band. Binary scheduling and association, UAV trajectories, and transmit powers are coupled by rate, one-user-per-slot, periodic-return, collision-avoidance, and power constraints. Their block-coordinate descent alternates linear scheduling with successive convex trajectory and power updates, initialized by circular trajectories and circle packing. The iterative method is proved to converge and improves throughput and fairness over static or simpler deployment baselines.

## Problem framing

UAVs as aerial BSs enhance cellular coverage; a single UAV has limited capability and availability under size-weight-and-power (SWAP) constraints, motivating multiple/swarm UAVs serving users in parallel. Trajectory design proactively builds short-distance LoS for desired UAV-user pairs while enlarging interfering distances, and adaptive power control mitigates co-channel interference when UAVs get close. The joint scheduling + trajectory + power problem is mixed-integer non-convex and tightly coupled.

## System model

- **Actors.** M ≥ 1 UAVs at fixed altitude H serving K > 1 ground users via periodic/cyclical **TDMA** within each period T; all UAVs share the same band.
- **Constraints.** Per-period trajectory return (q(0)=q(T)), maximum-speed, and inter-UAV **collision-avoidance** (minimum distance) constraints.
- **Objective.** Maximize the minimum average rate among all users (a max-min fairness objective; [[fairness-metrics-in-mec]]).

## Method

- Relax binary scheduling/association into continuous variables; partition variables into three blocks (scheduling+association, trajectory, power) and **alternately optimize** via [[alternating-optimization-sdr-sca|BCD]].
- For the non-convex trajectory and power subproblems, apply **successive convex optimization (SCA)**; prove convergence.
- A **systematic circular-trajectory + circle-packing** initialization speeds convergence and improves throughput.

## Key findings

- UAV mobility yields better air-to-ground channels and extra interference-mitigation flexibility, improving system throughput over static-BS cases (the paper's stated result).
- The proposed trajectory design **significantly outperforms a simple circular trajectory**.
- A **throughput-access-delay tradeoff** emerges (max-min rate non-decreasing with period T for mobile-UAV designs); using multiple UAVs significantly improves this tradeoff vs a single UAV.

## Limitations / future work

Downlink only, fixed altitude, 2D trajectory. Future work (stated): co-existence of aerial + ground BSs; **3D trajectory** with altitude + horizontal optimization; and **energy-efficient** trajectory accounting for UAV movement energy.

## Relation to the corpus

A canonical **multi-UAV-as-base-station** trajectory/scheduling/power paper from the Wu/Zeng/Zhang group — a **communications** (max-min rate) framing rather than compute offloading, so it is a methodological ancestor to the offloading-centric multi-UAV work and pairs naturally with the same group's UAV-comm tutorial [[zeng-2019-uav-comm-tutorial-5g]] and rotary-wing energy paper [[zeng-2019-rotary-wing-energy-min]]. Its BCD+SCA + min-rate fairness machinery recurs in the DRL multi-UAV trajectory study [[chang-2022-marl-multiuav-trajectory]]. Distinct from the single-UAV **MEC offloading** paper [[hu-2019-pdd-uav-mec-offloading]] (different author group, offloading objective). This is the most-cited anchor of the UAV-communications track.

## Raw artifacts

- `raw/sources/Joint_Trajectory_and_Communication_Design_for_Multi-UAV_Enabled_Wireless_Networks/full.md`
- Original PDF and extracted figures in the same folder.
