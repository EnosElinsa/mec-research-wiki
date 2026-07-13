---
type: source
title: "Deep Reinforcement Learning Based Resource Allocation and Trajectory Planning in Integrated Sensing and Communications UAV Network"
authors: ["Yunhui Qin", "Zhongshan Zhang", "Xulong Li", "Wei Huangfu", "Haijun Zhang"]
year: 2023
url: "https://doi.org/10.1109/TWC.2023.3260304"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, isac, uav, sac, masac, replay-augmentation, fairness, trajectory-control]
related:
  - "[[permutation-equivariant-replay-augmentation]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[uav-trajectory-control]]"
  - "[[soft-actor-critic]]"
  - "[[masac]]"
  - "[[jains-fairness-index]]"
  - "[[hybrid-action-decision-making]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[haijun-zhang]]"
  - "[[xulong-li]]"
  - "[[wei-huangfu]]"
created: 2026-07-12
updated: 2026-07-14
---

# Deep Reinforcement Learning Based Resource Allocation and Trajectory Planning in Integrated Sensing and Communications UAV Network

## Citation

Qin, Y., Zhang, Z., Li, X., Huangfu, W., & Zhang, H. (2023). *Deep Reinforcement Learning Based Resource Allocation and Trajectory Planning in Integrated Sensing and Communications UAV Network*. **IEEE Transactions on Wireless Communications**, 22(11), 8158-8169. DOI: 10.1109/TWC.2023.3260304.

## TL;DR

Jointly controls multi-UAV user association, horizontal trajectory, and sensing/communication power for max-min weighted spectral efficiency. Centralized SAC is strengthened with reward-preserving UAV-label permutations in replay memory, while MASAC provides a local-observation execution alternative.

## Problem

Multiple UAVs simultaneously communicate with and sense static ground targets while sharing spectrum. Association, power, and motion jointly determine communication rate, echo quality, interference, collision safety, and fairness. The resulting mixed-integer non-convex problem is treated as sequential control because complete channel knowledge and exhaustive search are impractical under mobility.

## System model

- Fixed-altitude UAVs with omnidirectional antennas serve static ground targets over slotted LoS distance-based links.
- Each target associates with exactly one UAV, while one UAV may serve several targets. Spectrum reuse creates inter-UAV interference in both communication and sensing spectral efficiency.
- Sensing uses a two-way inverse-fourth-power channel; communication uses inverse-square distance loss.
- Per-UAV weighted spectral efficiency combines communication and sensing terms. The objective maximizes the minimum horizon total across UAVs.
- Constraints cover binary association, per-slot and horizon transmit power, horizontal movement, pairwise separation, and rectangular flight bounds. Propulsion energy is not included in the energy budget.

## Method

The centralized [[soft-actor-critic|SAC]] state contains all communication/sensing gains and remaining UAV energies. Its hybrid action contains UAV locations, user associations, and powers; association is relaxed to an approximate continuous representation before deterministic discrete selection. The reward combines the minimum UAV weighted spectral efficiency with [[jains-fairness-index|Jain fairness]]. SAC separately adds policy entropy to its return objective.

[[permutation-equivariant-replay-augmentation]] exploits arbitrary UAV labels. A symmetric-group permutation is applied consistently to every UAV-indexed state, action, channel, position, power, and next-state component while preserving the reward. RSAC adds a fixed random number of equivalent transitions; ASAC starts with more permutations and decays the augmentation count to limit later replay correlation.

The decentralized [[masac|MASAC]] alternative assigns one actor to each UAV. Actors use only local channel gains and remaining energy, while twin critics consume global observations and joint actions during centralized training. The extracted local-reward equation is malformed, so the surrounding prose rather than the formula establishes its weighted-efficiency-plus-fairness intent.

## Key findings

- ASAC improves weighted spectral efficiency by a text-stated `14.3%` over vanilla SAC in the main simulation.
- MASAC learns fastest early but falls behind centralized methods later because actors have incomplete observations; no wall-clock comparison is reported.
- For five or six UAVs, ASAC has not converged after `30,000` episodes, although the paper reports comparable weighted spectral efficiency at that point.
- Across UAV- and user-count sweeps, ASAC is generally described as strongest, but the remaining numerical values are figure-only and are not transcribed as exact results.

## Limitations / parse caveats

Validation is PyTorch simulation only. The model fixes altitude and target positions, assumes level flight and distance-only LoS channels, and omits propulsion energy, richer blockage/fading, target mobility, hardware runtime, and field validation. Scaling beyond four UAVs is visibly difficult. Several extracted equations and algorithms have damaged symbols; the sensing notation alternates between `rad` and `sen`, the local MASAC reward omits a prose-described fairness term, and one result paragraph prints `ARAC` where the method context identifies ASAC. Publication volume/issue/pages were verified through the DOI's Crossref record; technical claims come only from the parse.

## Relation to the corpus

This source adds symmetry-based replay augmentation to the corpus's multi-UAV [[integrated-sensing-and-communication|ISAC]] controllers. Unlike trajectory-only SAC designs, it treats user association and sensing/communication power as a [[hybrid-action-decision-making|hybrid action]] and compares centralized augmented SAC with a [[centralized-training-decentralized-execution|CTDE]] MASAC alternative. Co-author [[haijun-zhang]] also appears in the corpus's hybrid-action UAV-MEC and satellite three-tier offloading lines.

## Raw artifacts

- Parse: `raw/sources/Deep_Reinforcement_Learning_Based_Resource_Allocation_and_Trajectory_Planning_in_Integrated_Sensing_and_Communications_UAV_Network/Deep_Reinforcement_Learning_Based_Resource_Allocation_and_Trajectory_Planning_in_Integrated_Sensing_and_Communications_UAV_Network.md`
- Origin PDF: `raw/sources/Deep_Reinforcement_Learning_Based_Resource_Allocation_and_Trajectory_Planning_in_Integrated_Sensing_and_Communications_UAV_Network/Deep_Reinforcement_Learning_Based_Resource_Allocation_and_Trajectory_Planning_in_Integrated_Sensing_and_Communications_UAV_Network.pdf`
- Figures: `raw/sources/Deep_Reinforcement_Learning_Based_Resource_Allocation_and_Trajectory_Planning_in_Integrated_Sensing_and_Communications_UAV_Network/images/`
