---
type: source
title: "Multi-Objective Optimization for UAV Swarm-Assisted IoT With Virtual Antenna Arrays"
authors: ["Jiahui Li", "Geng Sun", "Lingjie Duan", "Qingqing Wu"]
year: 2024
url: "https://doi.org/10.1109/TMC.2023.3298888"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, collaborative-beamforming, multi-objective-optimization, uav-data-collection, physical-layer-security, salp-swarm-algorithm, swarm-intelligence, virtual-antenna-array]
related:
  - "[[collaborative-beamforming]]"
  - "[[salp-swarm-algorithm]]"
  - "[[multi-objective-reinforcement-learning]]"
  - "[[uav-data-collection]]"
  - "[[physical-layer-security]]"
  - "[[mixed-integer-nonlinear-programming]]"
  - "[[sun-2025-emoppo-vlh-aerial-cb]]"
  - "[[li-2024-emodrl-ground-space-cb]]"
created: 2026-05-31
updated: 2026-05-31
---

# Multi-Objective Optimization for UAV Swarm-Assisted IoT With Virtual Antenna Arrays

## Citation

Li, J., Sun, G., Duan, L., & Wu, Q. (2024). *Multi-Objective Optimization for UAV Swarm-Assisted IoT With Virtual Antenna Arrays*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2023.3298888. (Manuscript received 7 February 2023; date of publication 26 July 2023; date of current version 4 April 2024 → year 2024 per the date-of-current-version convention.)

## TL;DR

For UAV-swarm-assisted IoT **data harvesting and dissemination**, the paper introduces **collaborative beamforming (CB)** into *both* IoT sensors and UAVs simultaneously — forming sensor-enabled **ground virtual antenna arrays (GVAAs)** and UAV-enabled **aerial virtual antenna arrays (AVAAs)** — so data moves from IoT clusters to remote base stations without frequent/long-range UAV flights. It formulates a **multi-objective optimization problem (MOP)** to jointly minimize **mission completion time**, **signal strength toward an eavesdropper** (physical-layer security), and **total UAV energy cost**. The MOP is proven **NP-hard, mixed-variable, and large-scale**, and solved by an **enhanced multi-objective salp swarm algorithm (EMSSA)** that returns a set of trade-off (Pareto) solutions at low computational complexity.

## Problem framing

UAVs and IoT sensors have limited transmit power/directivity, so existing harvesting/dissemination schemes require UAVs to fly between sensors and access points (multi-hop links or back-and-forth flight), inflating time and energy cost. Boosting both UAV and sensor transmission performance via CB avoids these flights. But CB performance depends on the (random) positions of array elements and their excitation-current weights, and a CB-by-eavesdropper conflict (suppressing leakage costs energy/time) makes the goals competing — hence a multi-objective formulation.

## System model

- **Virtual antenna arrays.** Sensors form GVAAs and UAVs form AVAAs; received power scales with array size, extending range and improving interference/eavesdropper resistance without changing the devices.
- **Operational choices.** Which sensors join the GVAA, UAV positions (AVAA geometry), excitation-current weights (beamforming coefficients), which UAVs receive harvested data, and the **order** in which UAVs access multiple BSs (affects energy).
- **Objectives (competing).** Minimize (1) data-transmission/mission completion time, (2) eavesdropper signal strength (PLS), and (3) total UAV swarm energy cost.
- **Hardness.** Proven NP-hard, mixed-variable, large-scale.

## Method

- **EMSSA** — an enhanced multi-objective **salp swarm algorithm** ([[salp-swarm-algorithm]]) that improves the conventional MSSA's **solution initialization**, **solution update**, and **algorithm-parameter update** phases to handle the mixed-variable, large-scale MOP and the four decision-variable types.
- Maintains a Pareto-dominance **archive** (with a hypercube-based pruning mechanism) of trade-off solutions.

## Key findings

- EMSSA outperforms various state-of-the-art multi-objective swarm-intelligence algorithms (per the parse).
- The method "can reduce time and energy costs significantly" versus benchmark strategies that require UAVs to fly frequently (multi-hop links or direct sensor↔BS flights) (verbatim qualitative claim; specific magnitudes are in the figures and not asserted here as exact).

## Limitations / future work

No explicit quantitative future-work targets are grounded in the captured parse → `not in parse`.

## Relation to the corpus

A **collaborative-beamforming / virtual-antenna-array** entry from the Jilin-University ([[geng-sun]]) cluster — the **earliest-dated** CB source in the corpus and a methodological precursor to the evolutionary CB line. It pairs naturally with [[sun-2025-emoppo-vlh-aerial-cb]] (aerial CB to a mobile user, EMOPPO-VLH) and [[li-2024-emodrl-ground-space-cb]] (ground-space CB, EMODRL), and shares the secure-CB-against-eavesdropper theme with [[zhang-2024-gdmtd3-aerial-secure-cb]]. Unlike those DRL/evolutionary-RL approaches, this one uses a pure **swarm-intelligence (salp swarm)** multi-objective optimizer, grounding the new [[salp-swarm-algorithm]] page. Reinforces [[collaborative-beamforming]], [[uav-data-collection]], and [[physical-layer-security]].

## Raw artifacts

- `raw/sources/Multi-Objective_Optimization_for_UAV_Swarm-Assisted_IoT_With_Virtual_Antenna_Arrays/full.md`
- Original PDF (`12c88c8c-3b81-48e0-803f-406912824221_origin.pdf`) and extracted figures (`images/`) in the same folder.
