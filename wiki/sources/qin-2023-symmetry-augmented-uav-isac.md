---
type: source
modeling_card: required
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
updated: 2026-07-16
---

# Deep Reinforcement Learning Based Resource Allocation and Trajectory Planning in Integrated Sensing and Communications UAV Network

## Citation

Qin, Y., Zhang, Z., Li, X., Huangfu, W., & Zhang, H. (2023). *Deep Reinforcement Learning Based Resource Allocation and Trajectory Planning in Integrated Sensing and Communications UAV Network*. **IEEE Transactions on Wireless Communications**, 22(11), 8158-8169. DOI: 10.1109/TWC.2023.3260304.

## TL;DR

Jointly controls multi-UAV user association, horizontal trajectory, and sensing/communication power for max-min weighted spectral efficiency. Centralized SAC is strengthened with reward-preserving UAV-label permutations in replay memory, while MASAC provides a local-observation execution alternative.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Fixed-altitude UAVs communicate with and sense static ground targets over slotted distance-dependent LoS links. Each target associates with one UAV, spectrum is reused across UAVs, sensing uses a two-way channel, and the system tracks communication and sensing weighted spectral efficiency while enforcing separation and flight-region safety.

**Problem & objective**: A mixed-integer non-convex sequential-control problem maximizes the minimum horizon weighted spectral efficiency, $\max\min_m\sum_t\big(R_m^{\mathrm c}(t)+R_m^{\mathrm s}(t)\big)$, with a Jain-fairness reward component.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Target association | $a_{m,n}(t)$ | binary | Whether target $n$ is served by UAV $m$ |
| UAV position | $\mathbf q_m(t)$ | continuous horizontal position | UAV trajectory in each slot |
| Communication/sensing power | $p_m^{\mathrm c}(t),p_m^{\mathrm s}(t)$ | continuous, bounded | Power assigned to communication and sensing |
| Policy action | $\pi_m(a\mid s)$ | hybrid action policy | Learned mapping from global or local observations to association, motion, and power |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Each target associates with exactly one UAV |
| C2 | Per-slot and horizon transmit powers satisfy UAV budgets |
| C3 | UAV movement remains inside the rectangular flight region |
| C4 | Pairwise UAV separation avoids collisions |
| C5 | All action variables and association choices remain in their specified domains |

**Algorithm**: Relax the hybrid association action for centralized SAC → train with the minimum weighted-efficiency plus fairness reward → augment replay transitions with consistent UAV-label permutations → decay augmentation as replay grows → optionally execute decentralized MASAC actors with centralized critics.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Qin et al. [x] studied joint resource allocation and trajectory planning for a multi-UAV integrated sensing and communications network. They formulated a mixed-integer non-convex control problem that maximizes the minimum horizon weighted spectral efficiency through target association, UAV positions, and communication and sensing power under power, movement, separation, and flight-region constraints. Their centralized SAC controller is augmented with reward-preserving UAV-label permutations in replay memory, while a MASAC variant supports local-observation execution. The permutation augmentation is applied consistently to UAV-indexed states, actions, channels, positions, powers, and next states. Simulations report a text-stated 14.3% weighted spectral-efficiency improvement over vanilla SAC in the main setting.

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
