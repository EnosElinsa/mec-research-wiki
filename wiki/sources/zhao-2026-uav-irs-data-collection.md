---
type: source
title: "Joint Optimization of UAV Trajectory and Number of Reflecting Elements for UAV-Mounted Intelligent Reflecting Surface-Assisted Data Collection in Wireless Sensor Networks Under Transmission Prioritized Scheme"
authors: ["Hong Zhao", "Hongbin Chen", "Shichao Li", "Ling Zhan"]
year: 2026
url: "https://doi.org/10.1109/TGCN.2026.3654945"
venue: "IEEE Transactions on Green Communications and Networking (TGCN)"
tags: [source, uav-mounted-ris, uav-data-collection, energy-efficiency, trajectory-optimization]
related:
  - "[[uav-mounted-ris]]"
  - "[[uav-data-collection]]"
  - "[[conditional-judgment-binary-search]]"
  - "[[rotary-wing-propulsion-energy-model]]"
  - "[[genetic-algorithm]]"
  - "[[hongbin-chen]]"
  - "[[shichao-li]]"
  - "[[mahmoud-2021-uav-irs-iot-analysis]]"
  - "[[pan-2025-uav-ris-energy-efficient-comm]]"
modeling_card: required
created: 2026-07-13
updated: 2026-07-16
---

# Joint Optimization of UAV Trajectory and Number of Reflecting Elements for UAV-Mounted Intelligent Reflecting Surface-Assisted Data Collection in Wireless Sensor Networks Under Transmission Prioritized Scheme

## Citation

Zhao, H., Chen, H., Li, S., & Zhan, L. (2026). Joint optimization of UAV trajectory and number of reflecting elements for UAV-mounted intelligent reflecting surface-assisted data collection in wireless sensor networks under transmission prioritized scheme. *IEEE Transactions on Green Communications and Networking, 10*, 1854-1866. https://doi.org/10.1109/TGCN.2026.3654945

## TL;DR

A rotary-wing UAV carries an IRS to relay fixed sensor data to a fusion center when direct links are blocked. Under a transmission-prioritized fly-hover-communicate policy, an alternating CJ-BS/SCA/GA pipeline selects active reflecting elements, hover locations, and multi-sensor visit order to reduce total energy for fixed payloads.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A fixed-altitude rotary-wing UAV carries an IRS to relay data from fixed ground sensor nodes to a fusion center when the direct paths are blocked. Under the fly-hover-communicate transmission-prioritized scheme, sensors use TDMA and one sensor transmits per hover point through a cascaded UAV-IRS channel with distance-dependent path loss and small-scale fading.

**Problem & objective**: P3 in (31), a non-convex MINLP under fixed transmitted payloads, minimizes $E_{\mathrm{total}}(\{\tilde{\mathbf q}_k(t)\},\tilde N_k,\lambda_k(t))$, equivalently maximizing system energy efficiency subject to spectrum-efficiency and delivery requirements.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV hover positions / trajectory | $\{\tilde{\mathbf q}_k(t)\}$ | Continuous, $\mathbb R^2$ at fixed altitude | Select the hover point associated with each sensor and the flight path between points |
| Active reflecting elements | $\tilde N_k$ | Integer, $1\le\tilde N_k\le N$ | Number of IRS elements activated for sensor $k$ |
| Sensor service indicator | $\lambda_k(t)$ | Binary, $\{0,1\}$ | Indicate whether sensor $k$ transmits at time $t$ and encode its visit order |
| Visit permutation | $\pi(k)$ | Permutation of $\{1,\ldots,K\}$ | Order in which the UAV visits sensor-specific hover points |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Fixed payload and minimum spectrum-efficiency requirements ensure complete sensor-data delivery |
| C2 | UAV speed obeys $\lVert\dot{\mathbf q}(t)\rVert\le V_{\max}$ |
| C3 | At most one sensor transmits while hovering: $\sum_k\lambda_k(t)\le1$ |
| C4 | The trajectory begins at $\mathbf q_I$, ends at $\mathbf q_F$, and remains in the allowed flight region |
| C5 | UAV propulsion, hovering, and IRS energy does not exceed $E_{UAV,\max}$ |
| C6 | Sensor power satisfies $\eta p_k+P_{s,k}\le P_{k,\max}$ and $1\le\tilde N_k\le N$ |

**Algorithm**: Initialize hover points, element counts, and visit order $\rightarrow$ use GA for the TSP-like service permutation $\rightarrow$ use conditional judgment and binary search for each integer element count $\rightarrow$ use SCA for continuous hover positions $\rightarrow$ alternate while rejecting energy-increasing updates.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zhao et al. [x] studied UAV-mounted IRS-assisted data collection from wireless sensor nodes whose direct links to a fusion center are blocked. They adopted a fly-hover-communicate protocol and formulated an energy-efficiency and spectrum-efficiency trade-off by jointly optimizing UAV hover locations, the number of reflecting elements, and multi-sensor service order under a transmission-prioritized scheme. For one sensor, they alternated conditional judgment with binary search for the reflecting-element count and successive convex approximation for the hover position. For multiple sensors, they added a genetic algorithm for the TSP-like service order and alternated the three subproblems. Simulations report energy-efficiency factors of 1.07 for the single-sensor case and 1.43 for the multi-sensor case relative to hovering directly above each sensor.

## Problem and system model

The UAV flies at fixed altitude, communicates with only one fixed sensor at a time while hovering, and travels between hover points at the maximum-range speed. IRS phases ideally cancel the cascaded channel phase. The energy model includes propulsion and hovering, active IRS elements, sensor amplifier/circuit power, and fusion-center receive power.

The operational problem minimizes total travel and communication energy subject to fixed data delivery, minimum rate, sensor-power, UAV-energy, speed, endpoint, and one-active-sensor constraints. In the multi-sensor formulation, the paper's "user association" variable is the order in which sensor-specific hover points are visited.

## Method

The [[conditional-judgment-binary-search]] block searches the integer number of reflecting elements after classifying the scalar energy curve as monotone or decrease-then-increase. Its unimodality premise comes from earlier work. At fixed element counts, SCA optimizes hover positions through first-order convex surrogates. A [[genetic-algorithm]] handles the TSP-like visit order, and the outer alternating loop rejects energy-increasing updates.

This monotonic outer sequence does not establish a global optimum for the coupled design. The paper's global statement applies only to the scalar element-count block under its imported unimodality premise.

## Key findings

- The single-sensor simulation reports energy efficiency equal to **1.07x** the directly-above-sensor baseline; the four-sensor example reports **1.43x**.
- The optimized design accepts lower spectral efficiency and longer aggregate hover time to shorten propulsion distance and reduce total energy.
- As payload grows, hover points move toward sensors. Per-sensor hover-time effects remain heterogeneous because distance and active-element count change together.

These are MATLAB simulation results. The setup text says five sensors, while the reported multi-sensor coordinates and plots use four.

## Limitations

The model assumes fixed known sensors, fixed altitude, a blocked direct path, ideal phase alignment, one sensor per hover, and no communication in flight. It omits phase quantization, CSI error/overhead, blockage uncertainty, and field validation. The parsed parameter table is damaged, including an implausible noise value, so those corrupted entries are not reproduced here.

## Relation to the corpus

This source adds propulsion-aware hover placement and element-count selection to the [[uav-mounted-ris]] thread. [[mahmoud-2021-uav-irs-iot-analysis]] analyzes a static UAV-IRS link, [[pan-2025-uav-ris-energy-efficient-comm]] studies cooperative UAV-RIS communication, and [[you-2019-rician-uav-data-harvesting]] optimizes WSN harvesting trajectories without an aerial IRS.

## Raw artifacts

- Parse: `raw/sources/Joint_Optimization_of_UAV_Trajectory_and_Number_of_Reflecting_Elements_for_UAV-Mounted_Intelligent_Reflecting_Surface-Assisted_Data_Collection_in_Wireless_Sensor_Networks_Under_Tra/Joint_Optimization_of_UAV_Trajectory_and_Number_of_Reflecting_Elements_for_UAV-Mounted_Intelligent_Reflecting_Surface-Assisted_Data_Collection_in_Wireless_Sensor_Networks_Under_Tra.md`
- Origin PDF and extracted figures (`images/`) are in the same folder.
