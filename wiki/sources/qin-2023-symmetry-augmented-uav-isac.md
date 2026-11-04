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
updated: 2026-11-03
---

# Deep Reinforcement Learning Based Resource Allocation and Trajectory Planning in Integrated Sensing and Communications UAV Network

## Citation

Qin, Y., Zhang, Z., Li, X., Huangfu, W., & Zhang, H. (2023). *Deep Reinforcement Learning Based Resource Allocation and Trajectory Planning in Integrated Sensing and Communications UAV Network*. **IEEE Transactions on Wireless Communications**, 22(11), 8158-8169. DOI: 10.1109/TWC.2023.3260304.

## TL;DR

Jointly controls multi-UAV user association, horizontal trajectory, and sensing/communication power for max-min weighted spectral efficiency. Centralized SAC is strengthened with reward-preserving UAV-label permutations in replay memory, while MASAC provides a local-observation execution alternative.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: $K$ single-antenna UAVs at fixed altitude $H$ communicate with and sense $M$ static ground target users over distance-dependent LoS links. Each target user is served by one UAV, spectrum is reused across UAVs, and sensing uses the two-way echo gain $h_{k,m,t} \propto d^{-4}$.

**Problem & objective**: (P0), a mixed-integer non-convex problem, maximizes the minimum total weighted spectral efficiency among UAVs, $\max_{\alpha, p, \Theta} \min_{k\in\mathcal K} E_k$ with $E_k = \sum_t E_{k,t}$ and $E_{k,t} = (\omega_c E_{k,t}^{\mathrm{com}} + \omega_s E_{k,t}^{\mathrm{sen}})/(\omega_c + \omega_s)$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| User association | $\alpha_{k,m,t}$ | binary | Target user $m$ is served by UAV $k$ in slot $t$ |
| Transmit power | $p_{k,t}$ | continuous, $[0, p_k^{\max}]$ | Power of UAV $k$ used for communication and sensing |
| UAV trajectory | $\Theta_{k,t} = (X_{k,t}, Y_{k,t})$ | continuous horizontal position | Position of UAV $k$ in slot $t$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| (11a)-(11b) | Binary association, and each target user served by exactly one UAV, $\sum_k \alpha_{k,m,t} = 1$. |
| (11c)-(11d) | Per-slot power $0 \le p_{k,t} \le p_k^{\max}$ and energy budget $\sum_t p_{k,t} \le e_k^{\max}$. |
| (11e) | Per-slot travel distance, $\lVert \Theta_{k,t} - \Theta_{k,t-1} \rVert \le V$. |
| (11f) | Collision avoidance, $\lVert \Theta_{i,t} - \Theta_{j,t} \rVert \ge D$. |
| (11g) | Rectangular flight region bounds on $X_{k,t}$ and $Y_{k,t}$. |

**Algorithm**: Transform the max-min objective into a reward of the minimum weighted spectral efficiency plus a Jain-fairness term, train centralized SAC with random or adaptive data augmentation that permutes UAV labels in replayed transitions, and optionally run decentralized multi-agent SAC.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Qin et al. [x] studied joint resource allocation and trajectory planning for a multi-UAV integrated sensing and communications network. They formulated a mixed-integer non-convex control problem that maximizes the minimum horizon weighted spectral efficiency through target-user association, UAV positions, and transmit power under power, energy, movement, separation, and flight-region constraints. Their centralized SAC controller is augmented with reward-preserving UAV-label permutations in replay memory, while a MASAC variant supports local-observation execution. The permutation augmentation is applied consistently to UAV-indexed states, actions, channels, positions, powers, and next states. Simulations report a text-stated 14.3% weighted spectral-efficiency improvement over vanilla SAC in the main setting.

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
