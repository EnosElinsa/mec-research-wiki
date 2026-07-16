---
type: source
title: "Energy-Efficient Multi-UAV Navigation for Cooperative Data Sensing and Transmission"
authors: ["Hu He", "Jun Peng", "Lin Cai", "Weirong Liu", "Chenglong Wang", "Xin Gu", "Zhiwu Huang"]
year: 2026
url: "https://doi.org/10.1109/TMC.2025.3612221"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC), vol. 25, no. 3, pp. 3119-3136"
modeling_card: required
tags: [source, multi-uav, uav-data-collection, memory-augmented-madrl, convlstm, prioritized-experience-replay, trajectory-control, fairness, energy-efficiency]
related:
  - "[[memory-augmented-multi-uav-navigation]]"
  - "[[uav-data-collection]]"
  - "[[ma-pomdp]]"
  - "[[multi-agent-td3]]"
  - "[[prioritized-experience-replay]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[jains-fairness-index]]"
  - "[[uav-trajectory-control]]"
  - "[[rotary-wing-propulsion-energy-model]]"
  - "[[liu-2021-edivert-mobile-crowdsensing]]"
  - "[[liu-2020-distributed-uav-coverage-navigation]]"
created: 2026-07-13
updated: 2026-07-16
---

# Energy-Efficient Multi-UAV Navigation for Cooperative Data Sensing and Transmission

## Citation

He, H., Peng, J., Cai, L., Liu, W., Wang, C., Gu, X., & Huang, Z. (2026). *Energy-Efficient Multi-UAV Navigation for Cooperative Data Sensing and Transmission*. **IEEE Transactions on Mobile Computing**, 25(3), 3119-3136. DOI: 10.1109/TMC.2025.3612221. Final bibliographic fields were verified by exact-title Crossref match because the parse omits them.

## TL;DR

MEMDRL combines a MATD3 backbone, BeBold-style exploration, ConvLSTM state histories, and fleet-level prioritized replay for decentralized multi-UAV collection. Policies balance uploaded PoI data, geographical visit fairness, and propulsion energy under local observations, obstacles, and no-fly zones.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Fixed-altitude UAVs with local observations move through a bounded region containing points of interest, obstacles, and no-fly zones. Each slot allocates time to motion, sensing, and orthogonal upload to a ground base station, and the fleet must explore fairly while conserving propulsion energy.

**Problem & objective**: Maximize fairness-weighted fleet energy efficiency, $\max_{\mathbf p}F_TK^{-1}\sum_k(\sum_tD_t^k)/(\sum_tE_t^k)$, by choosing every UAV's sequence of movement directions and distances.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Flight direction | $\theta_t^k$ | continuous, $[0,2\pi)$ | Heading chosen by UAV $k$ in slot $t$ |
| Travel distance | $d_t^k$ | continuous, $[0,d_{\max}]$ | Distance moved during the slot |
| UAV trajectory | $\mathbf p=\{\mathbf p_t^k\}$ | continuous position sequence | Positions induced by all movement actions |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Heading and travel distance remain within their action bounds. |
| C2 | Every UAV stays in the target region and outside obstacles and no-fly zones. |
| C3 | Pairwise separation satisfies $\lVert\mathbf p_t^i-\mathbf p_t^j\rVert_2\geq d_{\mathrm{safe}}$. |
| C4 | Same-slot upload capacity covers all newly collected data, so UAVs carry no backlog. |
| C5 | Cumulative movement and hovering energy stays below $E_{\max}$ for every UAV. |
| C6 | Jain's index rewards balanced cumulative PoI visits rather than data volume alone. |

**Algorithm**: Cast local movement control as a multi-agent POMDP with direction-distance actions and fairness-weighted bits-per-joule reward. Train MATD3 with twin centralized critics, delayed actor updates, and smoothed targets; add ConvLSTM histories for partial observations, BeBold intrinsic reward for first visits to underexplored cells, and fleet-level prioritized replay based on summed TD errors.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

He et al. [x] formulated cooperative multi-UAV sensing and upload as trajectory control that balances collected data, Jain geographical fairness, and propulsion energy under partial observations. UAVs choose continuous headings and travel distances subject to region, obstacle, separation, no-backlog upload, and energy-budget constraints. MEMDRL augments MATD3 with ConvLSTM observation histories, BeBold exploration, and fleet-level prioritized replay to learn decentralized policies with centralized critics. On Shenzhen and Beijing maps, MEMDRL improved the overall objective by 12.42% to 53.65% over four baselines for one Beijing UAV, with gains rising to 24.13% to 67.39% for ten UAVs.

## Problem

Fixed PoIs can report status only to nearby UAVs, so no aircraft observes the whole map. UAVs must explore unseen regions, avoid obstacles and each other, collect and immediately upload data to a ground station, and preserve energy and geographical fairness over a long service period.

## System model

- UAVs fly at fixed altitude over a bounded region containing PoIs, obstacles, and no-fly zones. Each action selects a continuous direction and travel distance.
- A slot first allocates movement time, then uses the remainder for PoI collection and orthogonal UAV-to-base-station upload. A no-backlog constraint requires upload capacity to cover the collected data.
- The global state is a spatial tensor of PoI remaining data, UAV energy/positions, and visit counts; each UAV sees only a local window.
- Geographical fairness is Jain's index over cumulative visits. Energy counts rotary-wing movement and hovering but omits communication energy.

## Method

[[memory-augmented-multi-uav-navigation|MEMDRL]] retains MATD3 twin critics, smoothed targets, delayed actor updates, and CTDE. ConvLSTM layers encode local observation histories for each actor and global state histories for centralized critics. A BeBold-inspired intrinsic reward favors first visits to less-explored cells, while replay priority sums TD errors across UAVs so fleet-wide transitions receive common importance.

## Key findings

- Simulations use 79 Shenzhen PoIs and 137 Beijing PoIs from real map datasets, with randomly initialized `(0,40] Mbit` demands and OpenStreetMap-derived obstacle/no-fly regions.
- With two UAVs in Shenzhen, MEMDRL uploads `81.62%` of PoI data versus `74.65%` for e-Divert, a `6.97` percentage-point difference.
- Action-generation time is `2.721/2.843 ms` for Shenzhen/Beijing, slower than MADDPG/MATD3 but faster than e-Divert. Rewards stabilize near 2400 and 3200 episodes, respectively.
- A Shenzhen-trained policy evaluated in Beijing reaches data/fairness/energy ratios of `0.751/0.796/0.714`, compared with `0.784/0.828/0.707` for Beijing training.
- Removing both ConvLSTM and prioritized replay lowers collection from `0.906` to `0.803` in Shenzhen and from `0.784` to `0.677` in Beijing; fairness falls from `0.946/0.828` to `0.847/0.683`.

## Limitations / parse caveats

The work simulates communications and flight over two selected city-map slices; it is not a UAV field test. PoI volumes are random, radio energy is omitted, physical acceleration/smoothing are delegated to a low-level controller, and the largest fleet has ten UAVs. Centralized training requires global state and joint actions. The convergence theorem depends on quasi-static opponents and full replay coverage, while its appendix is absent from the parse. Several fixed fleet/range values and the history length are OCR-missing, and the paper calls a 6.97 percentage-point gap a `6.97%` improvement.

## Relation to the corpus

This source is thematically related to [[liu-2020-distributed-uav-coverage-navigation]] and uses [[liu-2021-edivert-mobile-crowdsensing]] as its closest sensing baseline. Unlike e-Divert's separate CNN/LSTM feature path, MEMDRL keeps spatial layout inside ConvLSTM memory and prioritizes transitions from summed multi-agent TD error.

## Raw artifacts

- Parse: `raw/sources/Energy-Efficient_Multi-UAV_Navigation_for_Cooperative_Data_Sensing_and_Transmission/Energy-Efficient_Multi-UAV_Navigation_for_Cooperative_Data_Sensing_and_Transmission.md`
- Origin PDF: `raw/sources/Energy-Efficient_Multi-UAV_Navigation_for_Cooperative_Data_Sensing_and_Transmission/Energy-Efficient_Multi-UAV_Navigation_for_Cooperative_Data_Sensing_and_Transmission.pdf`
- Figures: `raw/sources/Energy-Efficient_Multi-UAV_Navigation_for_Cooperative_Data_Sensing_and_Transmission/images/`
