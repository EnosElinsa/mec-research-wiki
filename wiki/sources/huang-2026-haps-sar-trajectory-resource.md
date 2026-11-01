---
type: source
title: "Joint Trajectory and Resource Optimization for HAPs-SAR Systems With Energy-Aware Constraints"
authors: ["Bang Huang", "Ki-Hong Park", "Xiaowei Pang", "Mohamed-Slim Alouini"]
year: 2026
url: "https://doi.org/10.1109/TWC.2026.3719226"
venue: "IEEE Transactions on Wireless Communications, 25"
modeling_card: required
tags: [source, high-altitude-platform-station, synthetic-aperture-radar, trajectory-optimization, solar-energy-harvesting, successive-convex-approximation, minlp]
related:
  - "[[high-altitude-platform-station]]"
  - "[[hap-solar-propulsion-energy-balance]]"
  - "[[mixed-integer-nonlinear-programming]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[bistatic-sar-resolution-fairness]]"
  - "[[mohamed-slim-alouini]]"
created: 2026-11-02
updated: 2026-11-02
---

# Joint Trajectory and Resource Optimization for HAPs-SAR Systems With Energy-Aware Constraints

## Citation

Huang, B., Park, K.-H., Pang, X., & Alouini, M.-S. (2026). *Joint Trajectory and Resource Optimization for HAPs-SAR Systems With Energy-Aware Constraints*. **IEEE Transactions on Wireless Communications, 25**. DOI: 10.1109/TWC.2026.3719226.

## TL;DR

A HAPS carries a synthetic aperture radar and streams raw radar data in real time to a ground base station that reconstructs images, saving onboard processing energy. The paper models circular-flight trajectory and the power for sensing, transmission, motion, and solar harvesting, and maximizes radar beam coverage in an energy-aware MINLP solved by SCA with a finite search over the number of slots.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A HAPS flies a dynamic circular trajectory with altitude $z(n)$ over $N$ time slots, illuminating ground with SAR beams. Raw SAR data generated at rate $D_{\min}(n)=B_w[\frac2c(R_{\mathrm{far}}(n)-R_{\mathrm{near}}(n))+T_p]\cdot PRF$ is sent to a ground base station. Energy evolves with solar harvesting $P_{\mathrm{Har}}$ and consumption by motion $P_{\mathrm{Mot}}$, radar $P_{\mathrm{Rad}}$, and communication $P_{\mathrm{Com}}$.

**Problem & objective**: (P1), a nonconvex MINLP that maximizes the total radar beam coverage area $S$ over the trajectory, powers, energy states, and $N$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Number of slots | $N$ | integer, finite search space | Length of the flight and imaging horizon |
| Altitude and trajectory | $z(n)$, $x(n)$, $y(n)$ | continuous | HAPS position per slot |
| Powers | $P_{\mathrm{Mot}}(n)$, $P_{\mathrm{Rad}}(n)$, $P_{\mathrm{Com}}(n)$, $P_{\mathrm{Har}}(n)$ | continuous, bounded | Motion, radar, transmission, and harvested power |
| Energy state | $E(n)$ | continuous | Stored energy at slot $n$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1-C7 | Circular motion trajectory and per-slot speed definitions. |
| C8 | Real-time backhaul, transmission rate to the base station covers the SAR data rate. |
| C9 | Energy limitation of the HAPS. |
| C10-C11 | Constant radar power and bounded radar and communication powers. |
| C12 | Echo SNR above the imaging threshold $\mathrm{SNR}_{\min}$. |
| C13-C14 | Initial energy $E(1)=E_{\mathrm{Ini}}$ and positive energy afterwards. |
| C15-C16 | Altitude and speed bounds, including the stall-speed limit. |

**Algorithm**: Fix $N$ to obtain (P2), convexify constraints C8, C9, and C12 with SCA and slack variables, and solve iteratively. Since $N$ lies in a finite set, find its best value by exhaustive search.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Huang et al. [x] investigated the joint optimization of trajectory planning and resource allocation for a high-altitude platform station synthetic aperture radar system. To support real-time sensing and conserve the limited energy budget, the acquired radar data are transmitted in real time to a ground base station for image reconstruction. They developed a dynamic trajectory model, analyzed the power consumption of radar sensing, data transmission, and circular flight, and considered solar energy harvesting to improve sustainability. An energy-aware mixed-integer nonlinear programming problem was formulated to maximize radar beam coverage under operational constraints and solved by a sub-optimal successive convex approximation framework with iterative optimization and finite search. Simulation results validate convergence and show that the method balances SAR performance, backhaul communication reliability, and energy efficiency, and a SAR imaging simulation on a 9-target lattice confirms its practical feasibility.

## Problem framing

Onboard SAR image formation costs energy that a HAPS may not afford. Offloading reconstruction to the ground makes real-time backhaul a constraint on the radar mode and trajectory.

## System model

- Radar SNR follows the radar equation with pulse width, PRF, and backscatter coefficient.
- The ground base station receives raw data over a line-of-sight link whose rate depends on HAPS position and transmit power.

## Method

SCA iterations solve the fixed-$N$ problem, and an outer finite search over $N$ selects the horizon.

## Key findings

- The SCA procedure converges in the reported simulations.
- Joint design trades imaging coverage against backhaul reliability and energy.
- Imaging of a 9-target lattice confirms that the optimized trajectory and powers support SAR reconstruction.

## Limitations / future work

The authors plan to add environmental uncertainties such as wind disturbances and cloud effects.

## Relation to the corpus

Places SAR sensing on a [[high-altitude-platform-station]] under [[hap-solar-propulsion-energy-balance]] constraints; a UAV bistatic-SAR counterpart is [[bistatic-sar-resolution-fairness]].

## Raw artifacts

- Parse: `raw/sources/Joint_Trajectory_and_Resource_Optimization_for_HAPs-SAR_Systems_With_Energy-Aware_Constraints/Joint_Trajectory_and_Resource_Optimization_for_HAPs-SAR_Systems_With_Energy-Aware_Constraints.md`
- Origin PDF and extracted figures are in the same folder.
