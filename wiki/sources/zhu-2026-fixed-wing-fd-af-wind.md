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
created: 2026-07-13
updated: 2026-07-13
---

# Fixed-Wing UAV Aided Full-Duplex Amplify-and-Forward Relaying With Constant Ambient Wind

## Citation

Zhu, X., Ji, X., Yin, A., & Gu, J.-F. (2026). *Fixed-Wing UAV Aided Full-Duplex Amplify-and-Forward Relaying With Constant Ambient Wind*. **IEEE Transactions on Green Communications and Networking**, 10, 896-908. DOI: 10.1109/TGCN.2025.3603164.

## TL;DR

Derives a constant-3-D-wind propulsion model for a fixed-wing UAV acting as an in-band full-duplex amplify-and-forward relay. Wind-triangle case analysis and closed-form propositions choose air speed and flight time, then derive crab and pitch angles so the aircraft follows a predetermined ground track while meeting a data requirement with minimum propulsion energy.

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
