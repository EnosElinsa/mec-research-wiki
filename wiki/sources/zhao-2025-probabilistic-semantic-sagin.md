---
type: source
title: "Energy-Efficient Probabilistic Semantic Communication Over Space-Air-Ground Integrated Networks"
authors: ["Zhouxiang Zhao", "Zhaohui Yang", "Mingzhe Chen", "Chen Zhu", "Wei Xu", "Zhaoyang Zhang", "Kaibin Huang"]
year: 2025
url: "https://doi.org/10.1109/TWC.2025.3569102"
venue: "IEEE Transactions on Wireless Communications"
tags: [source, sagin, semantic-communication, probabilistic-semantic-communication, energy-efficiency, computation-offloading]
related:
  - "[[probabilistic-semantic-communication]]"
  - "[[semantic-communication]]"
  - "[[space-air-ground-integrated-network]]"
  - "[[task-oriented-communication]]"
  - "[[task-offloading]]"
  - "[[zheng-2024-semcom-sec-offloading]]"
  - "[[wang-2026-diffusion-semantic-uav-edge]]"
  - "[[sun-2024-mfris-semantic-antijamming]]"
  - "[[du-2024-yolo-semcom-digital-twin]]"
created: 2026-07-07
updated: 2026-07-07
---

# Energy-Efficient Probabilistic Semantic Communication Over Space-Air-Ground Integrated Networks

## Citation

Zhao, Z., Yang, Z., Chen, M., Zhu, C., Xu, W., Zhang, Z., & Huang, K. (2025). *Energy-Efficient Probabilistic Semantic Communication Over Space-Air-Ground Integrated Networks*. **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2025.3569102.

## TL;DR

Introduces a SAGIN-enabled probabilistic semantic communication (PSCom) model where a satellite sends data to ground terminals through a UAV relay. Satellite or UAV nodes may semantically compress data using shared probabilistic graphs, while ground terminals recover omitted relations. The optimization minimizes total communication plus computation energy by balancing semantic compression ratio, computation placement, bandwidth, power, and UAV placement.

## Problem

Semantic compression reduces transmitted bits but creates extra computation overhead. In SAGINs, communication resources are constrained and propagation distances are long, so the energy benefit of compression depends on where computation is performed and how aggressively the semantic representation is compressed. The paper models PSCom overhead as a piecewise function of semantic compression ratio and optimizes the communication-computation tradeoff.

## System model

- A satellite transmits data to multiple ground terminals through one UAV relay.
- Satellite, UAV, and GTs share probabilistic graphs built from semantic triplets and semantic quadruples.
- A transmitter can omit relation information when the shared graph gives enough probability structure for the receiver to recover it.
- Each GT has a semantic compression ratio; lower ratios transmit fewer bits but trigger higher-dimensional conditional probabilities and more computation.
- Computation tasks can be assigned to the satellite, the UAV, or neither, with each GT's semantic compression performed at most once.
- The decision variables include satellite/UAV computation allocation, compression ratio, UAV computation capacity, transmit power, bandwidth, altitude, beamwidth, and horizontal UAV location.

## Method

The energy minimization is decomposed into six iterative subproblems: satellite-UAV computation task allocation, semantic compression-ratio optimization, computation-capacity allocation, power/bandwidth allocation, UAV altitude/beamwidth design, and UAV horizontal location planning. The parse reports closed-form solutions for computation-capacity allocation and UAV altitude in each iteration, and proves convergence because the objective is non-increasing and lower-bounded by zero.

## Key findings

- The proposed SAGIN-PSCom algorithm converges in about three iterations in the reported simulation.
- SAGIN-PSCom has the lowest total energy among the non-semantic, random computation allocation, simplified PSCom, and fixed-UAV-location baselines in the reported comparisons.
- The energy savings from reduced transmission outweigh PSCom computation overhead when the semantic compression ratio is optimized.
- Under one reported setting, SAGIN-PSCom allocates all compression computation to the satellite and matches the comp-only-at-satellite baseline; a separate seven-GT table shows dynamic allocation to the UAV for a GT with smaller data demand.
- The benefit is especially pronounced when satellite beam gain is low; fixed UAV location remains close in total energy because UAV-to-GT communication energy is a small share of the system total in the tested setup.

## Limitations / future work

The model uses one satellite and one hovering UAV relay, with numerical evaluation rather than a deployment. The paper's future work names multi-satellite/multi-UAV extensions plus dynamic satellite motion and UAV trajectory control.

## Relation to the corpus

This source extends [[semantic-communication]] from aerial-ground or satellite-edge settings into a [[space-air-ground-integrated-network]] energy-minimization problem. It differs from [[zheng-2024-semcom-sec-offloading]] because the focus is not FL-coded semantic offloading in a satellite-borne edge cloud, but graph-based [[probabilistic-semantic-communication]] and the compression/computation energy tradeoff across satellite and UAV tiers. It is also adjacent to [[wang-2026-diffusion-semantic-uav-edge]], which optimizes semantic extraction and UAV trajectory inside a UAV-assisted edge system.

## Raw artifacts

- Parse: `raw/sources/Energy-Efficient Probabilistic Semantic Communication Over Space-Air-Ground Integrated Networks/Energy-Efficient Probabilistic Semantic Communication Over Space-Air-Ground Integrated Networks.md`
- Origin PDF: `raw/sources/Energy-Efficient Probabilistic Semantic Communication Over Space-Air-Ground Integrated Networks/Energy-Efficient Probabilistic Semantic Communication Over Space-Air-Ground Integrated Networks.pdf`
- Figures: `raw/sources/Energy-Efficient Probabilistic Semantic Communication Over Space-Air-Ground Integrated Networks/images/`
