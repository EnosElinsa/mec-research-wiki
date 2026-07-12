---
type: source
title: "ISAC-Empowered Air–Sea Collaborative System: A UAV–USV Joint Inspection Framework"
authors: ["Rui Zhang", "Fuwang Dong", "Wei Wang"]
year: 2026
url: "https://doi.org/10.1109/TWC.2026.3694754"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, isac, uav-usv, maritime-inspection, trajectory-optimization, beamforming, energy-minimization]
related:
  - "[[bi-traveling-salesman-problem-with-neighborhoods]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[successive-hover-and-fly-trajectory]]"
  - "[[uav-usv-cooperative-mec]]"
  - "[[rotary-wing-propulsion-energy-model]]"
  - "[[alternating-optimization-sdr-sca]]"
created: 2026-07-13
updated: 2026-07-13
---

# ISAC-Empowered Air–Sea Collaborative System: A UAV–USV Joint Inspection Framework

## Citation

Zhang, R., Dong, F., & Wang, W. (2026). *ISAC-Empowered Air–Sea Collaborative System: A UAV–USV Joint Inspection Framework*. **IEEE Transactions on Wireless Communications**, 25, 17479-17493. DOI: 10.1109/TWC.2026.3694754.

*Metadata note:* The local parse omits the article record; an exact-title Crossref DOI record supplies the 2026 TWC volume and pages above.

## TL;DR

Jointly plans one quadrotor UAV and one slower USV for maritime target inspection while maintaining UAV-USV communication. A hierarchical solver selects hover neighborhoods, orders them with a heterogeneous energy cost, refines dwell times and positions, then alternates trajectory and beamforming updates.

## Problem framing

The UAV can quickly acquire high-quality observations but has limited endurance; the USV has greater energy and resource reserves but slower, current- and obstacle-constrained motion. Sensing geometry, communication distance, shared arrival time, and different propulsion models therefore couple the two trajectories.

## System model

- One multi-antenna quadrotor senses 16 randomly distributed targets; one single-antenna USV supports communication throughout the mission.
- The UAV communicates while flying and transmits an ISAC waveform only at hover points; both vehicles start at `(0,0)` and finish at `(300,300)` together.
- The objective minimizes a weighted normalized sum of UAV and USV energy over target scheduling, total duration, trajectories, and communication/sensing beamformers.
- Constraints cover accumulated sensing SNR, communication rate, UAV/USV speed, USV obstacle distance, battery capacities, endpoints, and transmit power.
- Edge computing and task offload are contextual USV capabilities, not optimization variables in this paper.

## Method

[[bi-traveling-salesman-problem-with-neighborhoods|Bi-TSPN]] first determines an unknown set of feasible hover neighborhoods. Virtual-base-station clustering assigns targets and rough centroids, a directed hybrid UAV/USV energy cost defines an open-loop TSP order, and SCA refines positions, speeds, dwell times, and inter-stage durations.

For each hover-and-fly stage, flying-mode MRT and trajectory/power updates maintain the UAV-USV link. At hover points, lifted communication and sensing covariances are optimized by SDP/SCA, rank-one beamformers are recovered by eigendecomposition, and the USV trajectory is updated alternately under position-dependent water-current and obstacle constraints.

## Key findings

- The proposed design reports `61.658 kJ` total energy, versus `70.165 kJ` for Sequential Access, `69.665 kJ` for Leader-Follower, and `63.007 kJ` for Fly-and-Sense.
- Those totals correspond to reductions of about `12.12%`, `11.49%`, and `2.14%`, using each baseline total as denominator.
- The proposed energy components are `57.657 kJ` propulsion, `1.016 kJ` sensing/communication, and `2.985 kJ` inertial energy.
- The plotted scenario reaches its lowest total energy at objective weight `beta=0.2`; stronger communication or sensing requirements raise energy.
- Water-current direction changes the optimized USV route, and the reported route avoids three obstacles while respecting a `15 m` safety distance.

## Limitations / parse caveats

Evaluation is simulation-only, with no sea trial, runtime, seed, confidence interval, or repeated-run statistic. The hover-and-fly mode is explicitly not energy-optimal and the coarse stage fixes powers, ignores interference, and approximates several dynamics. The maritime channel omits explicit sea-surface multipath and micro-motion Doppler.

The parse contains important unresolved conflicts: the hover-duration inequality disagrees with its prose, P5 repeats USV energy where the cross-platform objective should differ, P4 is absent, and several target indices, powers, and hovering-beam symbols are damaged. Exact ablation gaps for the Bi-TSPN substeps are not transcribed.

## Relation to the corpus

This source extends [[successive-hover-and-fly-trajectory]] into heterogeneous air-sea coordination and adds current-aware routing through [[bi-traveling-salesman-problem-with-neighborhoods]]. It is adjacent to [[uav-usv-cooperative-mec]], but its own optimization covers ISAC, propulsion, and motion rather than computation offloading.

## Raw artifacts

- Parse: `raw/sources/ISAC-Empowered_Air-Sea_Collaborative_System_A_UAV-USV_Joint_Inspection_Framework/ISAC-Empowered_Air-Sea_Collaborative_System_A_UAV-USV_Joint_Inspection_Framework.md`
- Origin PDF: `raw/sources/ISAC-Empowered_Air-Sea_Collaborative_System_A_UAV-USV_Joint_Inspection_Framework/ISAC-Empowered_Air-Sea_Collaborative_System_A_UAV-USV_Joint_Inspection_Framework.pdf`
- Figures: `raw/sources/ISAC-Empowered_Air-Sea_Collaborative_System_A_UAV-USV_Joint_Inspection_Framework/images/`
