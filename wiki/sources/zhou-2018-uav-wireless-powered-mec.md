---
type: source
title: "Computation Rate Maximization in UAV-Enabled Wireless-Powered Mobile-Edge Computing Systems"
authors: ["Fuhui Zhou", "Yongpeng Wu", "Rose Qingyang Hu", "Yi Qian"]
year: 2018
url: "https://doi.org/10.1109/JSAC.2018.2864426"
venue: "IEEE Journal on Selected Areas in Communications (IEEE JSAC)"
tags: [source, uav-mec, wireless-power-transfer, computation-rate-maximization, binary-vs-partial-offloading, alternating-optimization, resource-allocation]
related:
  - "[[mobile-edge-computing]]"
  - "[[wireless-power-transfer]]"
  - "[[rf-energy-harvesting]]"
  - "[[binary-vs-partial-offloading]]"
  - "[[uav-trajectory-control]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[zhu-2025-lycnn-drl-wpt-mec]]"
  - "[[zhang-2019-uav-iot-comp-comm]]"
  - "[[liu-2022-miso-uav-mec-trajectory]]"
created: 2026-05-31
updated: 2026-06-09
---

# Computation Rate Maximization in UAV-Enabled Wireless-Powered Mobile-Edge Computing Systems

## Citation

Zhou, F., Wu, Y., Hu, R. Q., & Qian, Y. (2018). *Computation Rate Maximization in UAV-Enabled Wireless-Powered Mobile-Edge Computing Systems*. **IEEE Journal on Selected Areas in Communications**. DOI: 10.1109/JSAC.2018.2864426.

## TL;DR

An early, foundational study of a **UAV-enabled wireless-powered MEC system**: a UAV both transmits energy (via [[wireless-power-transfer|WPT]]) to ground users and serves as the MEC server they offload to. The paper maximizes the **weighted sum computation bits** of all users under two modes — **partial** and **binary** computation offloading — subject to an energy-harvesting causal constraint and a UAV speed constraint, jointly optimizing CPU frequencies, user offloading times, user transmit powers, and the UAV trajectory. The authors state this is, to their knowledge, the **first** work on UAV-enabled wireless-powered MEC computation-rate maximization.

## Problem framing

Low-power IoT devices have limited compute and battery. MEC plus WPT can extend both, but ground-based WPT suffers severe propagation loss; a UAV energy transmitter exploits short-distance LoS air-to-ground links to raise the harvested power. The joint resource + trajectory problem is non-convex; under binary offloading the mode-selection variables make it a mixed-integer non-convex problem.

## System model

- **Actors.** One UAV (energy transmitter + MEC server), multiple ground wireless devices.
- **Energy.** Users harvest energy from the UAV's RF signal; the harvested energy bounds local computing and offloading ([[rf-energy-harvesting]]).
- **Offloading modes.** Partial (task splittable between local + offload) and binary (local-or-offload only) — see [[binary-vs-partial-offloading]].
- **Objective.** Maximize the weighted sum of computation bits across all users.

## Method

- **Partial offloading mode.** A **two-stage algorithm**; the paper derives closed-form expressions for the optimal CPU frequencies, user offloading times, and user transmit powers.
- **Binary offloading mode.** A **three-stage alternative algorithm**, plus an optimal selection scheme for whether each user computes locally or offloads ([[alternating-optimization-sdr-sca]] family of solver).

## Key findings

- The proposed resource-allocation schemes outperform benchmark schemes in simulation, converge fast, and have low computational complexity (qualitative; specific curves in the paper).
- Closed-form optimal solutions are obtained for the per-user continuous variables in the partial-offloading case, and an explicit local-vs-offload selection rule is given for the binary case.

## Limitations / future work

The study is single-UAV and simulation-based. The authors state that UAV flight time limits computation performance and identify multiple-antenna techniques as a future direction.

## Relation to the corpus

A **classical / convex optimization** anchor at the intersection of UAV-MEC and WPT. It predates and motivates the DRL treatment of the same WPT-MEC problem in [[zhu-2025-lycnn-drl-wpt-mec]], and sits alongside the other early optimization-based single-UAV MEC works [[zhang-2019-uav-iot-comp-comm]] and [[liu-2022-miso-uav-mec-trajectory]]. Reinforces [[wireless-power-transfer]], [[binary-vs-partial-offloading]], and [[alternating-optimization-sdr-sca]].

## Raw artifacts

- `raw/sources/Computation_Rate_Maximization_in_UAV-Enabled_Wireless-Powered_Mobile-Edge_Computing_Systems/full.md`
- Original PDF and extracted figures in the same folder.
