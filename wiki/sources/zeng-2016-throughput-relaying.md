---
type: source
modeling_card: required
title: "Throughput Maximization for UAV-Enabled Mobile Relaying Systems"
authors: ["Yong Zeng", "Rui Zhang", "Teng Joon Lim"]
year: 2016
url: "https://doi.org/10.1109/TCOMM.2016.2611512"
venue: "IEEE Transactions on Communications (IEEE TCOMM)"
tags: [source, uav-mobile-relaying, uav-communications, trajectory-optimization, power-allocation, information-causality-constraint, alternating-optimization-sdr-sca]
related:
  - "[[uav-mobile-relaying]]"
  - "[[uav-trajectory-control]]"
  - "[[information-causality-constraint]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[energy-latency-tradeoff]]"
  - "[[zeng-2017-energy-efficient-uav-trajectory]]"
  - "[[zeng-2019-uav-comm-tutorial-5g]]"
  - "[[wu-2018-multiuav-minrate-trajectory]]"
  - "[[hu-2019-uav-relay-edge-computing]]"
  - "[[zhao-2019-uav-emergency-disasters]]"
  - "[[yong-zeng]]"
  - "[[li-2016-energy-balanced-uav-relaying]]"
  - "[[energy-balanced-cooperative-uav-relaying]]"
created: 2026-06-01
updated: 2026-07-16
---

# Throughput Maximization for UAV-Enabled Mobile Relaying Systems

## Citation

Zeng, Y., Zhang, R., & Lim, T. J. (2016). *Throughput Maximization for UAV-Enabled Mobile Relaying Systems*. **IEEE Transactions on Communications**, 64(12), 4983–4996. DOI: 10.1109/TCOMM.2016.2611512. (Received 8 Apr 2016; revised 14 Jul 2016; accepted 7 Sep 2016; date of publication 20 Sep 2016; date of current version 15 Dec 2016. Presented in part at IEEE GLOBECOM Workshops 2016.)

## TL;DR

A foundational **UAV mobile-relaying** paper. A relay node mounted on a high-mobility UAV assists communication from a fixed source (S) to a fixed destination (D). Unlike conventional **static relaying**, mobile relaying adds a new degree of freedom — **relay trajectory design** — to proactively construct favorable channels. The paper **maximizes end-to-end throughput** over a finite horizon by jointly optimizing the **source/relay transmit power allocation** and the **UAV relay trajectory**, subject to UAV speed and initial/final-location mobility constraints and the relay's **information-causality constraint** (the relay can only forward data it has already received). It shows the optimal power allocation follows a **"staircase" water-filling** structure, optimizes the trajectory via **successive convex optimization (SCA)**, and derives a closed-form jointly-optimal solution for the free-endpoint special case.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A fixed source sends data through a decode-and-forward fixed-altitude UAV relay to a fixed destination over a finite horizon. The source-to-relay and relay-to-destination LoS rates vary with the mobile relay's horizontal position.

**Problem & objective**: A non-convex joint power and trajectory problem maximizes delivered end-to-end throughput, $\max \sum_n R_{R\to D}[n]$, subject to mobility, power, and information causality.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Source power | $p_S[n]$ | continuous, nonnegative | Source transmission power in slot $n$ |
| Relay power | $p_R[n]$ | continuous, nonnegative | UAV forwarding power in slot $n$ |
| UAV trajectory | $\mathbf q[n]$ | continuous 2-D position | Relay horizontal location |
| Delivered data | $l[n]$ | continuous, nonnegative | Bits forwarded to the destination |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Cumulative forwarded data cannot exceed previously received data |
| C2 | Source and relay powers satisfy average and peak budgets |
| C3 | UAV displacement satisfies $\lVert\mathbf q[n+1]-\mathbf q[n]\rVert\le V_{\max}\Delta t$ |
| C4 | Prescribed initial and final relay locations are met |
| C5 | Per-slot source and relay rates follow their position-dependent channels |

**Algorithm**: Fix the trajectory and solve source and relay powers by duality to obtain staircase water filling → fix powers and lower-bound non-convex rate terms → update the trajectory by SCA → alternate power and trajectory blocks → use the closed-form free-endpoint solution when endpoint constraints are absent.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zeng et al. [x] studied throughput maximization for a decode-and-forward UAV mobile relay between a fixed source and destination. They jointly optimized source and relay transmit powers and the UAV trajectory under power budgets, speed, endpoint, and information-causality constraints. For a fixed trajectory, the optimal power allocation has a staircase water-filling structure derived through dual optimization. For fixed powers, successive convex approximation updates the trajectory, and the two blocks are alternated. Numerical results report higher end-to-end throughput than the evaluated static-relay and fixed-trajectory baselines, and the paper also derives a closed-form free-endpoint special case.

## Problem framing

Most relaying techniques use relays at fixed locations because of limited node mobility and wired backhaul. A UAV-borne relay can move at high speed, making on-demand deployment cheap and fast (useful for emergency/temporary events) and — crucially — letting the relay dynamically adjust its position to exploit the best channel. The paper assumes **FDD** with equal bandwidth for S→R reception and R→D transmission, so received data may need buffering before forwarding; this makes the **information-causality constraint** (forward only previously received data) more binding than in instantaneous static relaying. Trajectory planning and adaptive power allocation are tightly coupled: power should follow the movement-induced channel, while the trajectory must balance the source-relay and relay-destination links.

## System model

- **Three-node cooperative system.** Fixed source S at $(0,0,0)$ and destination D at $(L,0,0)$; a single mobile relay flies at fixed altitude $H$ with controllable horizontal trajectory, max speed, and given (or free) initial/final locations. Direct S→D link assumed negligible (extension left as future work).
- **Constraints.** Average transmit-power constraints at S and R; UAV mobility (max-speed, endpoints); the **[[information-causality-constraint]]** at the relay.
- **Objective.** Maximize end-to-end throughput over the finite horizon $T$.

## Method

- **Fixed trajectory → power allocation.** The optimal source/relay power allocation over time follows a **"staircase" water-filling** structure, with **non-increasing** water level at the source and **non-decreasing** at the relay; for monotone channel cases it reduces to conventional constant-level water-filling. (The structure is analogous to energy-harvesting power allocation, but driven by *information*-causality rather than energy-causality.)
- **Fixed power → trajectory.** Optimize the relay trajectory via **[[alternating-optimization-sdr-sca|successive convex optimization]]**, successively maximizing a lower bound of throughput.
- **Iterative algorithm.** Alternate the two steps to jointly optimize power + trajectory.
- **Free-endpoint special case.** When initial/final locations are free, derive the jointly optimal solution analytically: the relay either moves **unidirectionally at maximum speed** from S to D or **stays stationary** above S or D for an optimal duration.

## Key findings

- Compared with conventional **static relaying**, the proposed mobile relaying achieves a **significant throughput gain** (the paper's central numerical result; specific rate curves are figure-derived and indicative).
- Mobile relaying can **proactively construct favorable channels** via mobility control, unlike buffer-aided static relaying that relies on opportunistic channel fading — an extra degree of freedom for performance improvement.
- The "staircase" water-filling structure gives an interpretable optimal power policy tied to relay position over time.

## Limitations / future work

Single relay, fixed altitude, negligible direct S→D link, FDD with equal bandwidth. Future extensions (stated): different UAV-ground channel models, adaptive bandwidth allocation, limited buffer size, and explicit throughput-delay tradeoff.

## Relation to the corpus

A canonical **UAV mobile-relaying** anchor from the Zeng/Zhang group (grounding the new [[uav-mobile-relaying]] and [[information-causality-constraint]] concepts), and a methodological ancestor of the UAV relaying + MEC design [[hu-2019-uav-relay-edge-computing]] (which reuses the same information-causality + SCA machinery for a compute-offloading objective). Its SCA trajectory optimization is shared with the energy-efficiency anchor [[zeng-2017-energy-efficient-uav-trajectory]] and the multi-UAV max-min-rate design [[wu-2018-multiuav-minrate-trajectory]]; the broader context is surveyed in [[zeng-2019-uav-comm-tutorial-5g]]. It is cited as reference [2] (the throughput-of-mobile-relaying result) by the survey [[zhao-2019-uav-emergency-disasters]]. A communications (throughput) framing rather than compute offloading.

## Raw artifacts

- `raw/sources/Throughput_Maximization_for_UAV-Enabled_Mobile_Relaying_Systems/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
