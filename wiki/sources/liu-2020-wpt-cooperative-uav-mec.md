---
type: source
title: "UAV-Assisted Wireless Powered Cooperative Mobile Edge Computing: Joint Offloading, CPU Control, and Trajectory Optimization"
authors: ["Yuan Liu", "Ke Xiong", "Qiang Ni", "Pingyi Fan", "Khaled Ben Letaief"]
year: 2020
url: "https://doi.org/10.1109/JIOT.2019.2958975"
venue: "IEEE Internet of Things Journal (IEEE IoT-J)"
tags: [source, uav-mec, wireless-power-transfer, computation-offloading, cpu-control, trajectory-optimization, alternating-optimization]
related:
  - "[[mobile-edge-computing]]"
  - "[[wireless-power-transfer]]"
  - "[[rf-energy-harvesting]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[uav-trajectory-control]]"
  - "[[rotary-wing-propulsion-energy-model]]"
  - "[[zhou-2018-uav-wireless-powered-mec]]"
  - "[[zhu-2025-lycnn-drl-wpt-mec]]"
  - "[[liu-2022-miso-uav-mec-trajectory]]"
created: 2026-05-31
updated: 2026-05-31
---

# UAV-Assisted Wireless Powered Cooperative Mobile Edge Computing: Joint Offloading, CPU Control, and Trajectory Optimization

## Citation

Liu, Y., Xiong, K., Ni, Q., Fan, P., & Letaief, K. B. (2020). *UAV-Assisted Wireless Powered Cooperative Mobile Edge Computing: Joint Offloading, CPU Control, and Trajectory Optimization*. **IEEE Internet of Things Journal**. DOI: 10.1109/JIOT.2019.2958975. (Manuscript received 2 Sep 2019; date of publication 20 Dec 2019; date of current version 14 Apr 2020.)

## TL;DR

A **UAV-enabled wireless-powered cooperative MEC** system, where a UAV carrying an **energy transmitter (ET)** and an **MEC server** provides both energy and computing to sensor devices (SDs). **Active** SDs (with tasks) complete computing with help from the UAV and from **neighboring idle SDs** (no task), which act as cooperative helpers using harvested energy. The problem **minimizes the total required energy of the UAV** by jointly optimizing CPU frequencies, offloading amount, transmit power, and the UAV trajectory. The non-convex problem is solved by an **SCA-based** algorithm and, as a lower-complexity alternative, a **decomposition-and-iteration (DAI)-based** algorithm.

## Problem framing

Low-power SDs are constrained in compute and battery. Wireless power transfer + MEC can extend both, and a UAV exploits short-range LoS air-to-ground links for both energy and computing. A key observation: due to the broadcast nature of wireless links, the UAV's transmitted signals reach **idle** SDs too — so idle SDs' computing resources can be harnessed cooperatively to assist active SDs, fully using the transferred energy. The joint CPU/offloading/power/trajectory problem is non-convex.

## System model

- **Actors.** One UAV (energy transmitter + MEC server), active SDs (with tasks), and idle SDs (cooperative helpers) ([[wireless-power-transfer]], [[rf-energy-harvesting]]).
- **Cooperation.** Idle SDs harvest energy from the UAV and help compute active SDs' tasks.
- **Objective.** Minimize the **total required energy of the UAV**.
- **Variables.** CPU frequencies, offloading amount (bits), transmit power, and UAV trajectory ([[uav-trajectory-control]]).

## Method

- **SCA-based algorithm** for the non-convex problem ([[alternating-optimization-sdr-sca]]).
- **Decomposition-and-iteration (DAI)-based algorithm** as a lower-complexity alternative; theoretical analysis shows DAI has lower computational complexity than SCA.

## Key findings

- Both algorithms **converge within several iterations** and achieve **similar minimal required energy** and optimized trajectory; for **large** data amounts the SCA-based algorithm should be used (to find an optimal solution), while for **small** data amounts DAI gives smaller computing energy consumption (verbatim from the parse).
- **Trajectory optimization is the dominant factor** in minimizing total required energy, and optimizing acceleration greatly affects the UAV's required energy — propulsion-related energy dominates the total ([[rotary-wing-propulsion-energy-model]] context).
- Jointly optimizing the UAV's CPU frequency and offloaded bits greatly reduces computing energy; leveraging idle SDs further reduces the UAV's computing energy. A noted cost: more idle SDs means more optimization variables and longer convergence time.

## Limitations / future work

The parse's conclusion does not enumerate explicit future work; it notes the convergence-time growth as the number of idle SDs increases. Results are simulation-based.

## Relation to the corpus

A **classical / convex-optimization** WPT-MEC entry that extends the single-UAV WPT-MEC line of [[zhou-2018-uav-wireless-powered-mec]] (Zhou et al. 2018, computation-rate maximization) by adding **idle-SD cooperation** and a UAV-energy-minimization objective with explicit **CPU control** and trajectory. It predates and motivates the DRL treatment of WPT-MEC in [[zhu-2025-lycnn-drl-wpt-mec]], and sits alongside the AO-based single-UAV MEC work [[liu-2022-miso-uav-mec-trajectory]]. Reinforces [[wireless-power-transfer]] and [[alternating-optimization-sdr-sca]].

## Raw artifacts

- `raw/sources/UAV-Assisted_Wireless_Powered_Cooperative_Mobile_Edge_Computing_Joint_Offloading_CPU_Control_and_Trajectory_Optimization/full.md`
- Original PDF and extracted figures in the same folder.
