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
  - "[[collaborative-beamforming-in-aerial-mec]]"
created: 2026-05-31
updated: 2026-07-16
modeling_card: required
---

# Multi-Objective Optimization for UAV Swarm-Assisted IoT With Virtual Antenna Arrays

## Citation

Li, J., Sun, G., Duan, L., & Wu, Q. (2024). *Multi-Objective Optimization for UAV Swarm-Assisted IoT With Virtual Antenna Arrays*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2023.3298888. (Manuscript received 7 February 2023; date of publication 26 July 2023; date of current version 4 April 2024 → year 2024 per the date-of-current-version convention.)

## TL;DR

For UAV-swarm-assisted IoT **data harvesting and dissemination**, the paper introduces **collaborative beamforming (CB)** into *both* IoT sensors and UAVs simultaneously — forming sensor-enabled **ground virtual antenna arrays (GVAAs)** and UAV-enabled **aerial virtual antenna arrays (AVAAs)** — so data moves from IoT clusters to remote base stations without frequent/long-range UAV flights. It formulates a **multi-objective optimization problem (MOP)** to jointly minimize **mission completion time**, **signal strength toward an eavesdropper** (physical-layer security), and **total UAV energy cost**. The MOP is proven **NP-hard, mixed-variable, and large-scale**, and solved by an **enhanced multi-objective salp swarm algorithm (EMSSA)** that returns a set of trade-off (Pareto) solutions at low computational complexity.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Sensor clusters form ground virtual antenna arrays (GVAAs) to send data to selected UAV receivers; the UAV swarm broadcasts and forms aerial virtual antenna arrays (AVAAs) to disseminate data sequentially to remote BSs in the presence of an eavesdropper. Multiple access is one GVAA receiver per cluster followed by sequential AVAA-to-BS service; G2A/A2G links use probabilistic-LoS channels and UAV-to-UAV broadcast uses an LoS channel.

**Problem & objective**: An NP-hard, mixed-variable, large-scale MOP, $\min_X[f_1(X),f_2(X),f_3(X)]=[T^{\mathrm{MCT}},\mathrm{SLL}_E,E^{\mathrm{UAV}}]$, minimizing mission completion time, eavesdropper signal strength, and UAV swarm energy.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Sensor selection | $D_{i,h}$ | binary, $\{0,1\}$ | Sensor $i$ joins GVAA $h$ |
| Sensor excitation weight | $I^{\mathrm{SN}}_{i,h}$ | continuous, bounded | GVAA beamforming weight |
| UAV receiver assignment | $A_h$ | integer, one UAV per cluster | UAV receiving GVAA data |
| UAV position | $P_{j,k}$ | continuous, 3-D region | UAV position while serving BS $k$ |
| UAV excitation weight | $I^{\mathrm{UAV}}_{j,k}$ | continuous, bounded | AVAA beamforming weight |
| BS service order | $Q$ | integer permutation | Order in which AVAAs serve BSs |
| AVAA performing time | $T_{\mathrm{perf}}$ | continuous, nonnegative | Time allocated to array operation |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Sensor-selection, excitation-weight, position, and performing-time variables stay within their physical bounds |
| C2 | Each IoT cluster selects one receiving UAV, $A_h\in\mathcal U$ |
| C3 | The BS service order is a permutation, $Q\in\mathrm{Perm}(N_{\mathrm{BS}})$ |
| C4 | UAV positions remain in the reachable 3-D region and adjacent UAVs satisfy the minimum separation $d_{\min}$ |
| C5 | GVAA/AVAA transmissions use the modeled channel and eavesdropper SLL expressions |

**Algorithm**: Feasible mixed-variable population initialization → Pareto objective evaluation → EMSSA solution update for binary, integer, order, and continuous blocks → constraint repair, including Levy repositioning for collisions → archive non-dominated trade-off solutions.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Li et al. [x] studied UAV-swarm-assisted IoT data harvesting and dissemination with collaborative beamforming at both sensors and UAVs. They formulated an NP-hard, mixed-variable, large-scale multi-objective problem that minimizes mission completion time, signal strength toward an eavesdropper, and total UAV energy cost. The decision structure jointly selects GVAA sensors, assigns UAV receivers, sets sensor and UAV excitation weights, places UAVs, allocates array-performing time, and orders BS service. They proposed the enhanced multi-objective salp swarm algorithm, which improves solution initialization, parameter updates, and mixed-variable solution updates, and uses constraint handling to maintain feasible candidates. Simulations report that EMSSA outperforms the evaluated multi-objective swarm algorithms and reduces time and energy costs relative to multi-hop and long-range-flight benchmark strategies.

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
