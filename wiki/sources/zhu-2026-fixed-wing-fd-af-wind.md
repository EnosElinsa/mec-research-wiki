---
type: source
title: "Fixed-Wing UAV Aided Full-Duplex Amplify-and-Forward Relaying With Constant Ambient Wind"
authors: ["Xuan Zhu", "Xiaodong Ji", "Ansheng Yin", "Jian-Feng Gu"]
year: 2026
url: "https://doi.org/10.1109/TGCN.2025.3603164"
venue: "IEEE Transactions on Green Communications and Networking (IEEE TGCN)"
tags: [source, fixed-wing-uav, full-duplex-relaying, amplify-and-forward, ambient-wind, propulsion-energy, wind-triangle]
related:
  - "[[fixed-wing-propulsion-energy-model]]"
  - "[[uav-mobile-relaying]]"
  - "[[energy-latency-tradeoff]]"
  - "[[uav-trajectory-control]]"
  - "[[zeng-2017-energy-efficient-uav-trajectory]]"
modeling_card: required
created: 2026-07-13
updated: 2026-07-16
---

# Fixed-Wing UAV Aided Full-Duplex Amplify-and-Forward Relaying With Constant Ambient Wind

## Citation

Zhu, X., Ji, X., Yin, A., & Gu, J.-F. (2026). *Fixed-Wing UAV Aided Full-Duplex Amplify-and-Forward Relaying With Constant Ambient Wind*. **IEEE Transactions on Green Communications and Networking**, 10, 896-908. DOI: 10.1109/TGCN.2025.3603164.

## TL;DR

Derives a constant-3-D-wind propulsion model for a fixed-wing UAV acting as an in-band full-duplex amplify-and-forward relay. Wind-triangle case analysis and closed-form propositions choose air speed and flight time, then derive crab and pitch angles so the aircraft follows a predetermined ground track while meeting a data requirement with minimum propulsion energy.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: One fixed-wing UAV provides in-band full-duplex amplify-and-forward relaying between two single-antenna ground users on a predetermined straight, level flight track; both hops use free-space channels with perfect Doppler compensation under a constant three-dimensional wind vector.

**Problem & objective**: Problem (8), a wind-conditioned continuous optimization, minimizes $T E_n(U)$, the propulsion energy required to deliver a demanded data amount.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Air speed | $U$ | Continuous, $U_{\min}\le U\le U_{\max}$ | Magnitude of the UAV velocity relative to air |
| Flight time | $T$ | Continuous, positive | Relay service duration |
| Crab angle | $\phi$ | Continuous angle derived from wind triangle | Horizontal attitude correction for the ground track |
| Pitch angle | $\alpha$ | Continuous angle derived from wind triangle | Vertical attitude correction against wind |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Air speed remains within $[U_{\min},U_{\max}]$ and satisfies wind-triangle feasibility |
| C2 | Delivered data meets demand, $Q_{\mathrm{lb}}T\ge Q$ |
| C3 | Delivery finishes before the UAV reaches the route endpoint, $T\le l_{12}/v_g$ |
| C4 | Crab and pitch angles produce the predetermined ground-speed direction under the wind vector |

**Algorithm**: Wind-triangle case decomposition, set the active data constraint to $T=Q/Q_{\mathrm{lb}}$, solve the feasible air-speed branches with the paper's propositions and bisection where needed, select the lower-energy branch, and derive ground speed, pitch, and crab angles.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zhu et al. [x] studied fixed-wing UAV-aided full-duplex amplify-and-forward relaying under constant ambient wind. They formulated propulsion-energy minimization over UAV air speed and flight time while requiring delivery of a prescribed data amount before the relay reaches the end of its ground track. Wind-triangle case analysis separates the feasible air-speed branches, and the resulting propositions determine the optimal branch before computing the crab and pitch angles. Simulations confirm that the optimized UAV follows the predetermined track and satisfies the data demand. In the reported wind-speed sweep, the method saves about 3% energy relative to the fixed minimum-air-speed scheme and more relative to the median- and maximum-speed schemes.

## Problem framing

Wind separates air speed, which determines aerodynamic forces, from ground speed, which determines relay geometry. A route planned under no wind can drift or consume unnecessary energy. The paper asks how a battery-limited fixed-wing relay can resist constant wind, remain on a source-destination ground track, deliver the required data, and minimize propulsion use.

## System model

- A fixed-wing UAV relays a required data amount `Q` between two single-antenna ground nodes with no direct link, using two antennas for full-duplex AF operation.
- It flies straight and level at fixed altitude along the source-destination axis; Doppler is perfectly compensated and both hops use free-space path loss.
- The constant 3-D wind vector, air-speed vector, and ground-speed vector obey the wind triangle. Angle of attack is ignored.
- The objective includes propulsion energy only; transmit powers, altitude, path, and communication energy are fixed or omitted.

## Method

An aerodynamic force-balance derivation expresses engine power under wind. Ground-speed feasibility is split by horizontal-wind direction and positive-speed branch. Since energy rises with service time, the data constraint is active at `T = Q / Q_lb`. Three wind-conditioned subproblems use six propositions to classify feasible air-speed intervals and minimize absolute engine power; bisection finds zero-power roots where needed. Algorithm 1 selects the lower-energy feasible branch and derives ground speed, pitch, and crab angles.

The analytical solution is checked against sequential quadratic programming from MATLAB Optimization Toolbox and against fixed minimum-, median-, and maximum-air-speed baselines.

## Key findings

- At fixed air speed in straight level flight, the derived engine power depends on the vertical wind component but not horizontal components; horizontal wind still changes ground speed and delivered data.
- Upward wind can create a zero-power condition when the forward gravity component offsets drag; no numerical threshold is stated.
- In the reported wind-speed sweep, Algorithm 1 uses about `3%` less propulsion energy than the fixed minimum-air-speed baseline and much less than median/maximum-speed baselines.
- All compared schemes meet the data requirement in that test, while higher ground speed reduces actual received data because the relay spends less time in service geometry.

## Limitations / future work

Wind strength and direction are constant; block-varying wind is proposed as an extension. The route is fixed, straight, and level, and the method does not optimize 2-D/3-D trajectory, altitude, radio power, or scheduling. Communication energy is excluded, channels are free-space, Doppler is perfectly compensated, and evidence is simulation/SQP rather than flight testing. The topology is restricted to one source, one relay, and one destination.

## Relation to the corpus

This paper extends [[fixed-wing-propulsion-energy-model]] from no-wind velocity/acceleration accounting to wind-triangle kinematics and attitude compensation. It remains a communication-relay design, not MEC: there are no computation tasks, CPU cycles, offloading decisions, or edge-server queues.

## Raw artifacts

- Parse: `raw/sources/Fixed-Wing_UAV_Aided_Full-Duplex_Amplify-and-Forward_Relaying_With_Constant_Ambient_Wind/Fixed-Wing_UAV_Aided_Full-Duplex_Amplify-and-Forward_Relaying_With_Constant_Ambient_Wind.md`
- Origin PDF: `raw/sources/Fixed-Wing_UAV_Aided_Full-Duplex_Amplify-and-Forward_Relaying_With_Constant_Ambient_Wind/Fixed-Wing_UAV_Aided_Full-Duplex_Amplify-and-Forward_Relaying_With_Constant_Ambient_Wind.pdf`
- Figures: `raw/sources/Fixed-Wing_UAV_Aided_Full-Duplex_Amplify-and-Forward_Relaying_With_Constant_Ambient_Wind/images/`
