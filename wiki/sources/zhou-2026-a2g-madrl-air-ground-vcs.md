---
type: source
modeling_card: required
title: "AoI and Latency-Aware Air-Ground Vehicular Crowdsensing by Sequential Multi-Agent Deep Reinforcement Learning"
authors: ["Fan Zhou", "Chi Harold Liu", "Jianxin Zhao", "Chen Fang", "Hao Wang", "Guozheng Li", "Guangpeng Qi", "Dapeng Wu", "Kin K. Leung", "Jon Crowcroft"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3708370"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, vehicular-crowdsensing, age-of-information, multi-agent-drl, graph-neural-network, noma, uav-ugv-coordination]
related:
  - "[[age-of-information]]"
  - "[[uav-assisted-mobile-crowd-sensing]]"
  - "[[sequential-multi-agent-policy-generation]]"
  - "[[graph-neural-network]]"
  - "[[noma]]"
  - "[[ma-pomdp]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[uav-trajectory-control]]"
  - "[[guo-2026-aoi-uav-mcs-contract]]"
  - "[[gao-2023-uav-mcs-uma]]"
  - "[[chi-harold-liu]]"
created: 2026-07-11
updated: 2026-07-16
---

# AoI and Latency-Aware Air-Ground Vehicular Crowdsensing by Sequential Multi-Agent Deep Reinforcement Learning

## Citation

Zhou, F., Liu, C. H., Zhao, J., Fang, C., Wang, H., Li, G., Qi, G., Wu, D., Leung, K. K., & Crowcroft, J. (2026). *AoI and Latency-Aware Air-Ground Vehicular Crowdsensing by Sequential Multi-Agent Deep Reinforcement Learning*. IEEE Transactions on Mobile Computing. https://doi.org/10.1109/TMC.2026.3708370

## TL;DR

Introduces A2G-MADRL for air-ground vehicular crowdsensing with UAV-UGV pairs. The method jointly plans routes and NOMA channel assignments while optimizing sensing capability-aware AoI, latency-weighted data collection ratio, energy consumption ratio, and sensing efficiency.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Multiple fixed-altitude UAV-UGV pairs collect non-uniform data streams from points of interest in an urban work zone, with UGVs restricted to road graphs and UAVs also serving as relays. Air-ground cooperative NOMA lets each paired UAV and UGV reuse a channel, while channels across pairs are orthogonal and rates follow SINR-based Shannon models.

**Problem & objective**: The air-ground VCS control problem is a POMDP that maximizes the shared sensing reward, $\max_\pi\mathbb E_\pi[\sum_t\gamma^t r_t]$, where $r_t$ is the ratio of latency-weighted collected data to aggregate sAoI minus an energy-depletion penalty.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV movement | $(\theta_t^u,l_t^u)$ | continuous/discretized, $0\leq l_t^u\leq l_{\max}^u$ | Heading and travel distance of UAV $u$ |
| UGV movement | $a_{t,\mathrm{move}}^g$ | categorical road node | Next reachable road-network node for UGV $g$ |
| Channel assignment | $\chi_{t,c}^{n,p}$ | binary | Whether agent $n$ collects from PoI $p$ on channel $c$ |
| Joint policy | $\pi_\phi(\mathbf a_t\mid\mathbf o_t)$ | stochastic policy | Sequential joint UAV and UGV control policy |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Each agent uses at most $C$ channels, $\sum_{c,p}\chi_{t,c}^{n,p}\leq C$ |
| C2 | Each channel of one agent is assigned to at most one PoI, $\sum_p\chi_{t,c}^{n,p}\leq1$ |
| C3 | UAV travel is bounded by $l_{\max}^u$, and UGV moves remain on one-slot reachable road nodes |
| C4 | NOMA rates and relay transmissions follow the paired-channel SINR model |
| C5 | Energy depletion is penalized and unavailable actions are removed by action masks |

**Algorithm**: Build the dynamic UAV-UGV-PoI graph → project heterogeneous features and compute interaction-aware HVGCN embeddings → choose a dynamic agent order → generate masked actions autoregressively with DOMPG → update the shared policy using sequential weighted importance factors.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zhou et al. [x] studied AoI- and latency-aware air-ground vehicular crowdsensing with cooperative UAV-UGV pairs and NOMA channel assignment. They introduced sensing capability-aware age of information and latency-weighted data collection ratio for non-uniform status data. The control task is modeled as a POMDP whose UAV and UGV actions jointly determine movement and PoI channel assignments while accounting for sensing freshness, collected data, and energy. Their A2G-MADRL framework uses a heterogeneous vehicular graph convolution network for interaction features and a dynamically ordered masked policy generator for sequential coordination. Experiments on the KAIST and Roma datasets report better sAoI and latency-weighted data collection ratio than seven evaluated baselines across changes in fleet size, data-generation speed, and channel count.

## Problem

Urban traffic sensing needs both fresh updates and enough useful data from points of interest. Standard AoI is too coarse when surveillance/video PoIs generate non-uniform packet sizes, and independent UAV/UGV controllers miss the order-dependent coupling between vehicle motion, channel assignment, and data urgency.

## System model

- The system contains UAVs, UGVs, and PoIs in a workzone. PoIs continuously generate data and maintain FIFO queues.
- UAVs move at fixed altitude and can relay data; UGVs move on roads and collect or upload data.
- NOMA supports ground-to-air, air-to-ground relay, and ground-to-ground data collection, so channel assignment is part of the control problem.
- The main metrics are sensing capability-aware AoI (sAoI), latency-weighted data collection ratio, energy consumption ratio, and sensing efficiency.

## Method

A2G-MADRL combines an interaction-aware heterogeneous vehicular graph convolution network (HVGCN) with a dynamically ordered masked policy generator (DOMPG). HVGCN extracts UAV-UGV-PoI interaction features, while DOMPG generates agent actions sequentially with dynamic decision ordering and masking so later agents can condition on earlier actions instead of acting independently.

## Key findings

- The paper reports best tuning at one HVGCN layer and `alpha_seq = 0.3`, with sAoI / latency-weighted data collection ratio of `14.456 / 0.772` on KAIST and `14.672 / 0.769` on Roma.
- Removing HVGCN increases sAoI by 37.2% on KAIST and 40.5% on Roma; removing DOMPG increases sAoI by 27.9% on KAIST and 39.8% on Roma.
- Combining HVGCN and DOMPG improves sensing efficiency by 83.6% on KAIST and 137.2% on Roma.
- Under `C = 10` channels, A2G-MADRL reaches sAoI / latency-weighted collection ratio of `10.048 / 0.827` on KAIST and `10.188 / 0.822` on Roma.
- A Jetson TX2 inference test reports millisecond-scale HVGCN inference and DOMPG inference below 200 ms.

## Limitations / future work

The parse has heavily corrupted comparison tables and repeated accepted-manuscript banners, so the page relies on stable prose and table values. Future work extends A2G-MADRL to flexible 3D UAV trajectories with altitude-dependent channels, larger observation/action spaces, and safety constraints for vertical mobility.

## Relation to the corpus

This source connects [[age-of-information]] to air-ground [[uav-assisted-mobile-crowd-sensing]] rather than classic fixed-sensor UAV data collection. It complements [[guo-2026-aoi-uav-mcs-contract]], which studies AoI incentives for UAV-assisted mobile crowdsensing, by focusing on sequential UAV/UGV control. Methodologically, it adds [[sequential-multi-agent-policy-generation]] to the DRL toolbox and gives [[graph-neural-network]] / [[noma]] a concrete vehicular-crowdsensing use case.

## Raw artifacts

- `raw/sources/AoI_and_Latency-Aware_Air-Ground_Vehicular_Crowdsensing_by_Sequential_Multi-Agent_Deep_Reinforcement_Learning/AoI_and_Latency-Aware_Air-Ground_Vehicular_Crowdsensing_by_Sequential_Multi-Agent_Deep_Reinforcement_Learning.md`
- Original PDF and extracted figures (`images/`) in the same folder.
