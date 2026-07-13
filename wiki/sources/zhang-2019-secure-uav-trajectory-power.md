---
type: source
title: "Securing UAV Communications via Joint Trajectory and Power Control"
authors: ["Guangchi Zhang", "Qingqing Wu", "Miao Cui", "Rui Zhang"]
year: 2019
url: "https://doi.org/10.1109/TWC.2019.2892461"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, uav-communications, physical-layer-security, secrecy-rate, trajectory-optimization, power-control, block-coordinate-descent, successive-convex-approximation]
related:
  - "[[u2g-g2u-secrecy-asymmetry]]"
  - "[[physical-layer-security]]"
  - "[[uav-trajectory-control]]"
  - "[[air-to-ground-channel-model]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[zeng-2016-throughput-relaying]]"
  - "[[zhang-2022-uav-relay-substitution]]"
created: 2026-07-14
updated: 2026-07-14
---

# Securing UAV Communications via Joint Trajectory and Power Control

## Citation

Zhang, G., Wu, Q., Cui, M., & Zhang, R. (2019). *Securing UAV Communications via Joint Trajectory and Power Control*. **IEEE Transactions on Wireless Communications**, 18(2), 1376-1389. DOI: 10.1109/TWC.2019.2892461.

## TL;DR

Uses UAV mobility as a physical-layer security control: over a finite flight period, the design jointly adjusts the UAV's horizontal trajectory and the legitimate transmitter's slotwise power to improve average secrecy rate against a fixed ground eavesdropper. The UAV transmits in U2G and the ground node transmits in G2U. The two formulations reveal an important asymmetry: trajectory shapes both receiver links in U2G, but only the legitimate air-ground link in G2U under the paper's ground-ground eavesdropper model.

## Problem framing

The broadcast and line-of-sight character of UAV-ground links benefits legitimate communication but also exposes it to interception. Conventional terrestrial secrecy designs treat node positions as fixed or nearly fixed. This paper instead uses UAV macro-mobility for physical-layer security by moving the UAV to strengthen the legitimate channel, weaken the eavesdropping channel where geometry permits, and coordinate those channel changes with temporal power allocation. Its [[u2g-g2u-secrecy-asymmetry]] distinguishes which links motion can change in each direction.

## System model

- One fixed-altitude UAV communicates with one fixed legitimate ground node in the presence of one fixed ground eavesdropper. Both ground locations are known; the paper suggests detecting the eavesdropper with an optical camera or synthetic-aperture radar and treats the known-location secrecy rate as an upper bound for unknown-location operation.
- The finite horizon is divided into slots. Horizontal positions obey prescribed initial and final locations and a per-slot displacement limit derived from maximum speed.
- In UAV-to-ground (U2G) transmission, both UAV-ground links use deterministic free-space LoS gains. UAV power obeys average and peak constraints.
- In ground-to-UAV (G2U) transmission, the legitimate ground-UAV link is LoS, while the fixed ground-eavesdropper link includes distance-dependent loss and unit-mean Rayleigh fading. The eavesdropper rate is replaced by a Jensen upper bound and treated as attained, yielding a worst-case secrecy calculation within this model.

## Method

The U2G and G2U problems maximize average secrecy rate over trajectory and transmit power. A lemma removes the positive-part operator without changing the optimum because any slot with a negative raw secrecy difference can be assigned zero power. Block coordinate descent then alternates two blocks:

- For a fixed trajectory, a water-filling-like closed-form rule assigns zero power when the legitimate channel is no better than the eavesdropping channel, otherwise clips power at the peak; one-dimensional bisection enforces average power.
- For fixed power, successive convex approximation introduces distance slack variables and first-order bounds. The U2G block uses a feasible convex inner approximation; the G2U block reduces to maximizing the legitimate rate because its eavesdropper term is independent of UAV position.

The objective is non-decreasing and upper-bounded across iterations, so the algorithms converge in objective value to local/suboptimal designs. They do not establish global optimality or stationarity.

## Key findings

- In U2G Case 1, the optimized path at a 600 s horizon moves to a stationary point on the side of the legitimate node away from the eavesdropper, hovers, and then arcs toward the required endpoint.
- U2G trajectory and power control complement each other: the reported comparisons indicate that power control matters more at low average power, while trajectory control becomes more important as available power rises.
- In U2G Case 2, optimized power is reduced or shut off when the UAV is farther from the legitimate ground node than from the eavesdropper, allowing the joint design to use a more direct path than constant-power trajectory optimization.
- In G2U, trajectory has less security leverage because the UAV position changes only the legitimate link. For horizons of at least 410 s in the reported case, the joint method and the best-effort path with power control use the same path and power policy.
- Across the displayed comparisons, joint trajectory and power control gives the highest reported secrecy rate, while methods omitting one control can change order with horizon and average power. The prose provides no exact secrecy-rate gains.

## Limitations

The evaluation is simulation-only and considers one legitimate node, one passive eavesdropper, fixed altitude, deterministic endpoints, and perfectly known geometry. It does not model uncertain or multiple eavesdroppers, collusion, location-estimation error, shadowing, blockage, antenna orientation, Doppler, or propulsion energy. U2G channels are pure free-space LoS, and G2U secrecy uses a Jensen upper bound for the fading eavesdropper. The iterative design is initialization-dependent; it establishes monotonic objective convergence to a suboptimal/approximate design, not stationarity or local/global optimality.

## Relation to the corpus

This source makes [[physical-layer-security]] an explicit UAV mobility objective rather than an added jammer or reflecting-surface design. Its alternating trajectory-power structure extends the methodology used for throughput in [[zeng-2016-throughput-relaying]] and later relay substitution in [[zhang-2022-uav-relay-substitution]], but optimizes secrecy against a known ground eavesdropper. It also gives [[uav-trajectory-control]] different roles by direction: proactive legitimate/eavesdropper channel shaping in U2G and legitimate-link improvement in G2U.

## Raw artifacts

- Parse: `raw/sources/Securing_UAV_Communications_via_Joint_Trajectory_and_Power_Control/Securing_UAV_Communications_via_Joint_Trajectory_and_Power_Control.md`
- Origin PDF: `raw/sources/Securing_UAV_Communications_via_Joint_Trajectory_and_Power_Control/Securing_UAV_Communications_via_Joint_Trajectory_and_Power_Control.pdf`
- Figures: `raw/sources/Securing_UAV_Communications_via_Joint_Trajectory_and_Power_Control/images/`
