---
type: source
title: "Resource Allocation and Trajectory Design for MISO UAV-Assisted MEC Networks"
authors: ["Boyang Liu", "Yiyao Wan", "Fuhui Zhou", "Qihui Wu", "Rose Qingyang Hu"]
year: 2022
url: "https://doi.org/10.1109/TVT.2022.3140833"
venue: "IEEE Transactions on Vehicular Technology (IEEE TVT)"
tags: [source, uav-mec, miso, beamforming, trajectory-design, energy-minimization, sca]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[uav-trajectory-control]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[qcqp-sdr-probabilistic-mapping]]"
  - "[[energy-latency-tradeoff]]"
  - "[[zhang-2019-uav-iot-comp-comm]]"
  - "[[yu-2020-uav-ec-collaborative-offloading]]"
  - "[[fuhui-zhou]]"
created: 2026-05-29
updated: 2026-07-16
modeling_card: required
---

# Resource Allocation and Trajectory Design for MISO UAV-Assisted MEC Networks

## Citation

Liu, B., Wan, Y., Zhou, F., Wu, Q., & Hu, R. Q. (2022). *Resource Allocation and Trajectory Design for MISO UAV-Assisted MEC Networks*. **IEEE Transactions on Vehicular Technology**. DOI: 10.1109/TVT.2022.3140833.

## TL;DR

A **multiple-input single-output (MISO)** UAV-assisted MEC network that uses UAV beamforming to overcome poor channel quality from multipath/blockages. The paper minimizes system energy consumption by jointly optimizing the UAV's beamforming vectors, UAV CPU frequency, UAV trajectory, UE transmit power, and UE CPU frequency, via a **three-stage iterative algorithm** with closed-form expressions derived for the optimal UAV CPU frequency and UE transmit power.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A multi-antenna UAV MEC server serves single-antenna UEs with partial task offloading and can relay unprocessed results to an access point over a LoS link during $N$ slots.

**Problem & objective**: Jointly optimize resource allocation and UAV trajectory to minimize weighted UE and UAV energy, $\min_{\mathbf L,\mathbf w_u,\mathbf q[n]}E_I[n]+\eta E_U[n]$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
| --- | --- | --- | --- |
| UE CPU frequency | $f_{l,k}[n]$ | continuous in $[0,f_{l,\max}]$ | Local computing rate of UE $k$ |
| UAV CPU allocation | $f_{u,k}[n]$ | continuous, nonnegative with $\sum_k f_{u,k}[n]\leq f_{u,\max}$ | UAV computing rate assigned to UE $k$ |
| UE transmit power | $p_k[n]$ | continuous in $[0,p_{l,\max}]$ | Uplink offloading power |
| UAV beamforming | $\mathbf w_{u,k}[n]$ | complex vector under a total-power bound | Beam for UE $k$ and result delivery |
| UAV trajectory | $\mathbf q[n]$ | continuous slot positions | Horizontal UAV location over the mission |

**Constraints**:

| ID | Meaning and key expression |
| --- | --- |
| C1 | Each UE completes its task within the slot horizon and processed bits do not exceed causally offloaded bits. |
| C2 | CPU frequencies and UE/UAV transmit powers satisfy their individual and aggregate upper bounds. |
| C3 | Beamforming meets each UE's minimum SINR and maximum tolerated interference, with $\lVert\mathbf q[n]-\mathbf q[n-1]\rVert\leq d_{\min}$. |
| C4 | The UAV starts at $\mathbf q_I$, reaches $\mathbf q_F$, and obeys the per-slot mobility and reachability constraints. |

**Algorithm**: Alternate three blocks for CPU frequency and UE power, semidefinite-relaxed beamforming, and trajectory SCA; use closed-form frequency and power updates and recover rank-one beams by eigenvalue decomposition.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Liu et al. [x] extended UAV-assisted MEC to a MISO server that jointly acts as a computing node and relay. Their per-slot formulation minimizes weighted UE and UAV energy over partial offloading, CPU frequencies, UE transmit powers, beamforming vectors, and UAV trajectory, subject to task, SINR, power, and mobility constraints. A three-stage alternating method combines dual and subgradient updates, semidefinite relaxation, and successive convex approximation, with closed-form CPU and UE-power solutions. The derived offloading rule depends on the UAV UE channel state, and simulations show lower energy than benchmark designs, especially for computation-intensive tasks. The model makes beamforming and trajectory coupling explicit in an optimization-based UAV MEC formulation.

## Problem framing

Traditional MEC suffers poor channel quality from multipath and blockages. Equipping the UAV with multiple antennas (MISO) and beamforming improves links, but the joint beamforming + frequency + trajectory + power design is non-convex.

## System model

- **Actors.** A MISO UAV (multiple antennas) serving single-antenna UEs.
- **Objective.** Minimize system energy consumption.
- **Variables.** UAV beamforming vectors, UAV CPU frequency, UAV trajectory, UE transmit power, UE CPU frequency, under task/trajectory/computation constraints.

## Method

- A **three-stage alternating algorithm**; closed-form expressions derived for optimal UAV CPU frequency and UE transmit power. The beamforming sub-problem uses semidefinite-relaxation-style convexification (rank-one constraint dropped, strong duality) ([[alternating-optimization-sdr-sca]], [[qcqp-sdr-probabilistic-mapping]]).

## Key findings

- The derived results show the UE offloading decision is determined by the UAV–UE CSI; simulations show superiority over benchmarks in energy consumption, especially for computation-intensive tasks, with guaranteed convergence (qualitative; specific curves in the paper).

## Limitations / future work

The conclusion does not enumerate explicit future work beyond the established design.

## Relation to the corpus

A **MISO/beamforming** twist on the optimization-based single-UAV MEC formulation shared with [[zhang-2019-uav-iot-comp-comm]] and [[yu-2020-uav-ec-collaborative-offloading]]; the explicit CSI-driven offloading-decision result connects to the CSI-uncertainty thread ([[jia-2025-dro-uav-hap-mec]], [[wu-2026-terrain-aware-uav-mec]]). Reinforces [[alternating-optimization-sdr-sca]] and [[uav-trajectory-control]]. Shares co-author Qihui Wu with several aerial sources.

## Raw artifacts

- `raw/sources/Resource_Allocation_and_Trajectory_Design_for_MISO_UAV-Assisted_MEC_Networks/full.md`
- Original PDF and extracted figures in the same folder.
