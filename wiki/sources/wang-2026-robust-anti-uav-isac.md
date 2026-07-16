---
type: source
title: "ISAC Enabled Anti-UAV: Joint Beamforming and Trajectory Design for Multi-UAVs"
authors: ["Xiaojie Wang", "Lingfei Li", "Zhaolong Ning", "Xiaoming Tao", "Tie Qiu", "Lei Guo", "Yan Zhang"]
year: 2026
url: "https://doi.org/10.1109/TWC.2026.3707705"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, isac, anti-uav, multi-uav, robust-optimization, beamforming, trajectory-optimization, cramer-rao-bound]
related:
  - "[[spatially-separated-uav-isac-role-scheduling]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[cramer-rao-bound]]"
  - "[[cooperative-isac-transceiver-beamforming]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[uav-trajectory-control]]"
  - "[[zhaolong-ning]]"
  - "[[xiaojie-wang]]"
  - "[[lei-guo]]"
  - "[[zhang-2025-cooperative-anti-uav-isac]]"
  - "[[wang-2026-multiuav-transceiver-beamforming]]"
  - "[[li-2026-control-based-uav-isac]]"
created: 2026-07-13
updated: 2026-07-16
modeling_card: required
---

# ISAC Enabled Anti-UAV: Joint Beamforming and Trajectory Design for Multi-UAVs

## Citation

Wang, X., Li, L., Ning, Z., Tao, X., Qiu, T., Guo, L., & Zhang, Y. (2026). *ISAC Enabled Anti-UAV: Joint Beamforming and Trajectory Design for Multi-UAVs*. **IEEE Transactions on Wireless Communications**, 25, 19611-19627. DOI: 10.1109/TWC.2026.3707705.

*Metadata note:* The accepted-manuscript parse supplies the venue and DOI but not the final issue record; an exact-title Crossref record supplies the 2026 volume and pages above.

## TL;DR

Uses satellite-coordinated authorized UAVs to track one moving unauthorized UAV while serving communication users. Per-slot transmitter/receiver role scheduling, robust CRB reformulation, beamforming, association, and 3-D trajectory updates are combined in the AIEA alternating solver.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Satellite-coordinated authorized UAVs cooperatively sense a moving unauthorized UAV while serving ground communication users. In each slot, authorized UAVs are scheduled as sensing transmitters or echo receivers and move in three dimensions under bounded target-position uncertainty.

**Problem & objective**: Problem P1 minimizes the worst-case time-average cooperative position-error bound, $\min \max_{\Delta\mathbf p_L[n]\in\Omega_L[n]}\frac{1}{N}\sum_{n\in\mathcal N}\operatorname{Tr}(\mathbf{CRB}(\mathbf p_L[n]))$, under bounded target-position error.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Communication beamforming | $\mathbf w[t]$ | complex continuous | Downlink beams for communication users |
| Sensing transmit beamforming | $\mathbf r[t]$ | complex continuous | ISAC waveform beams transmitted toward the target |
| Sensing receive beamforming | $\mathbf u[t]$ | complex continuous | Echo-combining beams at receiver UAVs |
| User association | $\alpha[t]$ | binary | Assigns each communication user to at most one UAV |
| UAV sensing role | $\beta[t]$ | binary | Selects transmitter or receiver operation in each slot |
| UAV trajectory | $\mathbf p[t]$ | continuous, bounded | Three-dimensional authorized-UAV positions |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| 32a | ISAC transmit power is bounded at each sensing transmitter |
| 32b | Satellite communication, ISAC transmission, and propulsion stay within each UAV power budget |
| 32c | Every served user meets its minimum downlink SINR |
| 32d-32e | User associations are binary and each user is assigned to at most one UAV |
| 32f-32g | Sensing roles are binary and at least one UAV receives target echoes |
| 32h-32j | Horizontal speed, vertical speed, and altitude satisfy flight limits |

**Algorithm**: AIEA replaces the robust CRB condition by finite LMIs using Schur complements, a first-order uncertainty model, and the generalized Petersen lemma. It alternates semidefinite-relaxed beamforming with rank recovery, penalty-SCA updates for association and role variables, and convexified trajectory and propulsion updates.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Wang et al. [x] studied cooperative anti-UAV sensing by satellite-coordinated authorized UAVs that simultaneously serve communication users. They minimized the worst-case time-average target-position CRB over transmit and receive beamforming, user association, sensing-role scheduling, and three-dimensional trajectories. Their AIEA solver combines robust LMI reformulation, semidefinite relaxation, penalty successive convex approximation, and alternating optimization. The reported four-UAV experiments converged in fewer than five outer iterations and maintained the lowest CRB among the compared methods across the examined uncertainty and system-parameter sweeps. The results also showed that scheduling spatially separated sensing transmitters and receivers can preserve user SINR while improving sensing geometry under bounded target-location error.

## Problem framing

Fixed cellular anti-UAV infrastructure can be blocked or unable to follow a target across regions. Mobile cooperative UAVs improve geometry, but target-position uncertainty, cross-UAV interference, transmit/receive role assignment, user service, and propulsion constraints create a mixed-integer non-convex design.

## System model

- Four authorized multi-antenna UAVs cooperatively sense one unauthorized UAV and serve five moving ground communication users in the main Manhattan-map simulation.
- A LEO satellite coordinates control, synchronization, CSI, sensing samples, and platform status; handover, latency, capacity, and satellite energy are excluded.
- Each slot assigns UAVs to type-1 sensing transmitters or type-2 echo receivers while both types may continue communication service.
- Target position is an estimate plus coordinate-wise bounded uncertainty; the objective minimizes worst-case time-average cooperative position-CRB trace.
- Communication appears as minimum-SINR constraints rather than a rate/fairness objective.

## Method

[[spatially-separated-uav-isac-role-scheduling]] separates sensing transmitters from receivers to avoid direct self-interference. The paper derives minimum satellite-link power under a Rician outage constraint, then obtains a cooperative position FIM/CRB for bistatic echoes.

Schur complements and a generalized Petersen sign-definiteness lemma convert the uncertainty-dependent FIM condition into finite LMIs after first-order target-position approximation. AIEA alternates lifted transmit/receive beamforming with rank-one recovery, penalty-SCA relaxation of association and role binaries, and convexified 3-D trajectory/propulsion updates.

## Key findings

- All shown objective curves stabilize within five optimization iterations; this is iteration count, not wall-clock evidence.
- When each coordinate uncertainty bound rises from `4 m` to `10 m`, the paper states that random association's CRB trace rises from `1.5` to `2.5`; the corresponding plot appears inconsistent, so the prose value should be treated cautiously.
- AIEA is reported to maintain the lowest and most stable CRB across uncertainty, CU count/noise, transmit power, UAV count, speed, and SINR sweeps, but exact superiority percentages are not transcribed.
- Larger uncertainty, CU noise, CU count, and SINR requirements worsen sensing; more UAVs and transmit power generally improve it.

## Limitations / parse caveats

The study is simulation-only and considers one target UAV. It assumes modeled box uncertainty, global coordination, per-slot stationarity, and no collision avoidance, horizontal geofence, or fixed endpoints. Robustness applies to a first-order approximation of the sensing vector, and alternating monotonicity does not establish global optimality.

The parse contains an outage-monotonicity sign conflict, theorem/appendix mismatch, penalty-sign conflict, damaged robust-LMI expressions, shifted aerodynamic parameters, and ambiguous antenna counts. No code, runtime, seed, Monte Carlo count, confidence interval, or exact stopping tolerance is given.

## Relation to the corpus

Where [[zhang-2025-cooperative-anti-uav-isac]] coordinates fixed multi-cell BS beamformers, this paper mobilizes the sensing layer, adds 3-D trajectories and per-slot transmit/receive roles, and minimizes a worst-case cooperative CRB. It remains a communication-security and sensing source, not an MEC offloading model.

## Raw artifacts

- Parse: `raw/sources/ISAC_Enabled_Anti-UAV_Joint_Beamforming_and_Trajectory_Design_for_Multi-UAVs/ISAC_Enabled_Anti-UAV_Joint_Beamforming_and_Trajectory_Design_for_Multi-UAVs.md`
- Origin PDF: `raw/sources/ISAC_Enabled_Anti-UAV_Joint_Beamforming_and_Trajectory_Design_for_Multi-UAVs/ISAC_Enabled_Anti-UAV_Joint_Beamforming_and_Trajectory_Design_for_Multi-UAVs.pdf`
- Figures: `raw/sources/ISAC_Enabled_Anti-UAV_Joint_Beamforming_and_Trajectory_Design_for_Multi-UAVs/images/`
