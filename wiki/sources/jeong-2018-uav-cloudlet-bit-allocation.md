---
type: source
title: "Mobile Edge Computing via a UAV-Mounted Cloudlet: Optimization of Bit Allocation and Path Planning"
authors: ["Seongah Jeong", "Osvaldo Simeone", "Joonhyuk Kang"]
year: 2018
url: "https://doi.org/10.1109/TVT.2017.2706308"
venue: "IEEE Transactions on Vehicular Technology (IEEE TVT)"
tags: [source, uav-mec, mobile-cloud-computing, bit-allocation, uav-trajectory-control, successive-convex-approximation, noma, energy-latency-tradeoff]
related:
  - "[[mobile-edge-computing]]"
  - "[[uav-trajectory-control]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[noma]]"
  - "[[energy-latency-tradeoff]]"
  - "[[rotary-wing-propulsion-energy-model]]"
  - "[[fixed-wing-propulsion-energy-model]]"
  - "[[zhang-2019-uav-iot-comp-comm]]"
  - "[[mozaffari-2019-uav-wireless-tutorial]]"
created: 2026-06-01
updated: 2026-11-03
modeling_card: required
---

# Mobile Edge Computing via a UAV-Mounted Cloudlet: Optimization of Bit Allocation and Path Planning

## Citation

Jeong, S., Simeone, O., & Kang, J. (2018). *Mobile Edge Computing via a UAV-Mounted Cloudlet: Optimization of Bit Allocation and Path Planning*. **IEEE Transactions on Vehicular Technology**. DOI: 10.1109/TVT.2017.2706308. (Manuscript received 17 September 2016; date of publication 19 May 2017; date of current version 15 March 2018 → year 2018 per the date-of-current-version convention.)

## TL;DR

An early **UAV-mounted cloudlet** MEC paper: a moving UAV carries computing resources and offers **computation offloading** to ground mobile users (MUs) with weak local processors. The system **minimizes total mobile energy consumption** subject to a latency deadline and a UAV energy budget, by **jointly optimizing** (i) the **bit allocation** for uplink transmission, downlink transmission, and computing at the cloudlet, and (ii) the **UAV trajectory**. Uplink/downlink use frequency-division duplex with either **orthogonal access or NOMA**. The resulting non-convex problem is solved via **successive convex approximation (SCA)**, yielding an iterative algorithm guaranteed to converge to a local optimum. Numerical results report significant energy savings over local execution and over partial schemes that optimize only the bit allocation or only the trajectory.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A UAV-mounted cloudlet at fixed altitude $H$ serves $K$ ground mobile users (MUs) over $N$ frames of length $\Delta$. Each MU offloads its input bits, the cloudlet computes them, and the output bits are returned in the downlink while the UAV flies from $\mathbf p_I^c$ to $\mathbf p_F^c$. Both orthogonal and non-orthogonal access are studied.

**Problem & objective**: Problem (13a) minimizes total MU offloading energy, $\min\sum_k\sum_{n=1}^{N-2}E_{O,k,n}^m(L_{k,n}^m,\mathbf p_n^c)$, over uplink bits, cloudlet computing bits, downlink bits, and the cloudlet trajectory, subject to a UAV energy budget $\mathcal E$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
| --- | --- | --- | --- |
| Uplink bits | $L_{k,n}^{m}$ | nonnegative continuous | Input bits sent by MU $k$ in frame $n$ |
| Cloudlet-computed bits | $l_{k,n}$ | nonnegative continuous | Input bits computed at the UAV cloudlet in frame $n$ |
| Downlink bits | $L_{k,n}^{c}$ | nonnegative continuous | Output bits returned to MU $k$ in frame $n$ |
| Cloudlet trajectory | $\mathbf p_n^c$ | continuous 2-D positions | UAV location at each frame |

**Constraints**:

| ID | Meaning and key expression |
| --- | --- |
| (13b) | Cloudlet computing, downlink, and flying energy stay within the UAV budget $\mathcal E$ |
| (13c)-(13d) | Computation and downlink causality prevent processing or returning bits before they arrive |
| (13e)-(13g) | All input, computed, and output bits are delivered, $\sum_nL_{k,n}^m=I_k$, $\sum_nl_{k,n+1}=I_k$, $\sum_nL_{k,n+2}^c=O_kI_k$ |
| (13h) | Bit allocations are nonnegative |
| (13i)-(13k) | Prescribed start and end positions, speed limit $\lVert\mathbf v_n^c\rVert\leq v_{\max}$, and velocity definition |

**Algorithm**: Apply successive convex approximation within the inner convex approximation framework, iteratively solving convex surrogates of the nonconvex energy and rate terms for both orthogonal and non-orthogonal access until convergence to a local minimum. An extension adds an acceleration limit (31f).

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Jeong et al. [x] introduced a UAV-mounted cloudlet that jointly plans a fixed-altitude trajectory and bit allocation for uplink, cloudlet computation, and downlink return. They minimize total mobile-user energy under a UAV energy budget and computation-causality, task-completion, UAV-energy, endpoint, and speed constraints for both orthogonal and non-orthogonal access. The solver applies successive convex approximation to the joint bit-allocation and trajectory problem, with separate interference models for orthogonal and non-orthogonal access. At a 2.7 s deadline, the joint design requires 36.8 J with OMA and 29.9 J with NOMA versus 43.1 J and 44.3 J for equal allocation and constant-velocity flight, corresponding to 14.5% and 32.7% reductions.

## Problem framing

UAVs deployed as moving base stations or relays extend coverage where infrastructure is limited (rural, disaster response, military). Beyond relaying/coverage, a UAV-mounted cloudlet enables **fog computing without a working terrestrial infrastructure**: MUs offload heavy tasks (object recognition, augmented reality) by uplinking input data, having the UAV compute, then downlinking the result. The challenge is that the UAV's limited coverage, mobility, and energy budget couple the communication, computation, and flight-energy decisions — and the UAV-MU channel changes as the UAV moves, so the trajectory and the bit allocation must be designed jointly.

## System model

- **Actors.** $K$ ground MUs at fixed positions on the $xy$-plane; one UAV-mounted cloudlet flying at fixed altitude $H$ along a trajectory discretized into $N$ frames of duration $\Delta$, with predetermined initial/final positions and a maximum speed.
- **Application model.** Each MU $k$ has $I_k$ input bits, $C_k$ CPU cycles per input bit, and $O_k$ output bits per input bit, all to be processed within deadline $T$.
- **Channels.** Line-of-sight-dominated UAV-MU links with gain $\propto 1/(\text{distance}^2 + H^2)$; FDD with equal bandwidth for uplink/downlink. Orthogonal access gives each MU a $\Delta/K$ slot; NOMA lets all MUs transmit simultaneously with interference treated as noise.
- **Energy models.** Computation energy $\propto C_k l (f^c)^2$ (effective switched capacitance); communication energy from information-theoretic rate expressions; **two flying-energy models** — Model 1 depends only on UAV velocity (kinetic, constant altitude), Model 2 additionally accounts for acceleration.
- **Objective.** Minimize total MU energy under the latency deadline and the UAV energy budget (which covers communication, computing, and flying).

## Method

- Formulate the joint **bit-allocation + trajectory** problem for both orthogonal access and NOMA, under latency and UAV-energy-budget constraints.
- The problem is non-convex; apply **successive convex approximation (SCA)** to derive an efficient iterative algorithm guaranteed to converge to a **local minimum** of the original problem. See [[alternating-optimization-sdr-sca]] for the wiki's convex-pipeline page.
- Study both flying-energy models (velocity-only and velocity+acceleration) in separate sections.

## Key findings

- The proposed **joint** optimization of bit allocation and cloudlet trajectory yields **significant mobile-energy savings** versus (a) local mobile execution and (b) partial schemes that optimize only the bit allocation or only the trajectory (the paper's stated headline result; specific magnitudes are in the numerical-results figures and are not asserted here as exact).
- NOMA and orthogonal-access variants are both handled within the same SCA framework, letting the design compare access schemes under the same energy/latency objective.

## Limitations / future work

The model assumes a single UAV at fixed altitude, known MU positions, LoS-dominated channels, and predetermined launch/landing points. The parse does not enumerate an explicit future-work list → `not in parse`.

## Relation to the corpus

An **early anchor for the classical/convex UAV-MEC track**, predating and conceptually upstream of the SCA/AO offloading sources such as [[zhang-2019-uav-iot-comp-comm]] (joint computation + communication via Lagrangian duality + SCA) and the trajectory-optimization line. It frames the UAV as a **moving cloudlet** offering offloading — distinct from the UAV-as-base-station / relay roles surveyed in [[mozaffari-2019-uav-wireless-tutorial]]. Its joint **bit-allocation across uplink/compute/downlink** is an unusually fine-grained decision variable for the corpus, and its two flying-energy models connect to [[rotary-wing-propulsion-energy-model]] and [[fixed-wing-propulsion-energy-model]]. Reinforces [[mobile-edge-computing]], [[uav-trajectory-control]], [[noma]], and [[energy-latency-tradeoff]].

## Raw artifacts

- `raw/sources/Mobile_Edge_Computing_via_a_UAV-Mounted_Cloudlet_Optimization_of_Bit_Allocation_and_Path_Planning/Mobile_Edge_Computing_via_a_UAV-Mounted_Cloudlet_Optimization_of_Bit_Allocation_and_Path_Planning.md`
- Original PDF and extracted figures (`images/`) in the same folder.
