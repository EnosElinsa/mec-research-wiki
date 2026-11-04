---
type: source
modeling_card: required
title: "Security-Aware Designs of Multi-UAV Deployment, Task Offloading and Service Placement in Edge Computing Networks"
authors: ["Mengru Wu", "Haonan Wu", "Weidang Lu", "Lei Guo", "Inkyu Lee", "Abbas Jamalipour"]
year: 2025
url: "https://doi.org/10.1109/TMC.2025.3574061"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, multi-uav-assisted-mec, physical-layer-security, cooperative-jamming, service-caching, multi-agent-td3, task-offloading]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[task-offloading]]"
  - "[[service-caching-mec]]"
  - "[[physical-layer-security]]"
  - "[[friendly-jamming-uav]]"
  - "[[cooperative-jamming]]"
  - "[[multi-agent-td3]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[lei-guo]]"
created: 2026-07-07
updated: 2026-11-03
---

# Security-Aware Designs of Multi-UAV Deployment, Task Offloading and Service Placement in Edge Computing Networks

## Citation

Wu, M., Wu, H., Lu, W., Guo, L., Lee, I., & Jamalipour, A. (2025). *Security-Aware Designs of Multi-UAV Deployment, Task Offloading and Service Placement in Edge Computing Networks*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2025.3574061. DOI/venue/year are parse-silent at the top level and verified against a title-matched Crossref/IEEE DOI record.

## TL;DR

Studies multi-UAV MEC where devices offload only to UAV servers that have cached the required service program, while eavesdroppers threaten the offloading link. A UAV jammer provides cooperative jamming, and OE-MATD3 jointly learns UAV deployment, offloading, service placement, and jamming power while a closed-form transmit-power solver handles device power.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Devices $m\in\mathcal M$ compute locally or offload to UAV servers $k\in\mathcal K$ that cache a limited set of service programs. A jammer UAV $J$ sends artificial noise against eavesdroppers with uncertain locations, so deployment, caching, secrecy rate, delay, and energy are coupled.
**Problem & objective**: Problem P (14) minimizes total task-completion delay, $\min_{\{\mathbf q_k\},\{a_{m,k}\},\{y_{n,k}\},\{P_m\},\mathbf q_J,P_J}\sum_m(T_m^{uav}+T_m^{loc})$.
**Decision variables**:
| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV-server deployment | $\mathbf q_k$ | continuous position | Location of UAV server $k$ |
| Offloading | $a_{m,k}$ | binary | Device $m$ offloads to UAV server $k$ |
| Service placement | $y_{n,k}$ | binary | Service program $n$ cached at UAV server $k$ |
| Device power | $P_m$ | continuous, $[0,P_m^{\max}]$ | Offloading transmit power of device $m$ |
| Jammer location and power | $\mathbf q_J,P_J$ | continuous, $P_J\in[0,P_J^{\max}]$ | Cooperative-jamming deployment and power |
**Constraints**:
| ID | Meaning and key expression |
|---|---|
| (14b) | At most one UAV server per device, $\sum_ka_{m,k}\le1$ |
| (14c) | Cache capacity $\sum_ny_{n,k}c_n\le S_k^{\max}$ |
| (14d) | Offload only to a server caching the required program, $a_{m,k}\le y_{n,k}\le1$ for $n=\varphi(m)$ |
| (14e) | Secrecy rate $R_{m,k}^{sec}\ge R_{m,k}^{\min}$ if $a_{m,k}=1$; replaced by a worst-case lower bound (20c) |
| (14f)-(14g) | Device energy $E_m^{uav}+E_m^{loc}\le E_m^{\max}$ and delay $T_m^{uav}+T_m^{loc}\le T_m^{\max}$ |
| (14h)-(14i) | Separation among UAV servers and between servers and the jammer, $\ge d_{\min}^2$ |
| (14j)-(14l) | Binary $a_{m,k},y_{n,k}$; power limits on $P_m$ and $P_J$ |
**Algorithm**: Replace the secrecy constraint by a worst-case lower bound (P'), solve device power P1' in closed form (Theorem 3), and train OE-MATD3 agents for UAV-server deployment, offloading, service placement, and jammer location and power (P2').

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Wu et al. [x] studied security-aware UAV deployment, task offloading, and service placement in multi-UAV edge computing networks. Devices can offload only to UAV servers that cache the required service program, while a jammer UAV protects the links against uncertain-location eavesdroppers. The formulation minimizes total task-completion delay under cache, secrecy-rate, computation, energy, movement, and collision constraints. OE-MATD3 learns UAV-server deployment, offloading, service placement, and jammer location and power, while a closed-form step selects feasible device transmit power. Simulations report lower delay than OE-MADDPG, OE-MAA2C, random service placement and offloading, fixed jamming power, fixed jammer location, and random UAV-server placement.

## Problem

UAV-MEC service diversity means edge servers cannot process every task unless the relevant service program is stored locally. At the same time, line-of-sight offloading links can leak task data to eavesdroppers. The paper minimizes total device task-completion delay under caching-space, secure-offloading-rate, execution-delay, and energy constraints.

## System model

The system contains multiple UAV servers, wireless devices, eavesdroppers, and one UAV jammer. Each device has one computation task mapped to a required service program. A device can compute locally or offload to a UAV server only if that UAV has precached the matching service program. The UAV jammer sends artificial noise toward eavesdroppers during computation offloading. The simulation uses a 400 m square region with 20 devices, 4 eavesdroppers, and 3 UAV servers, with UAV altitude 120 m and limited cache capacity.

## Method

The paper first derives a worst-case lower bound on secrecy offloading under eavesdropper location uncertainty, then derives closed-form feasible device transmit power. UAV-related variables are learned through optimization-embedding MATD3: UAV server agents and the jammer agent use local observations at execution, while critics use centralized state/action information during training. The reward is the negative delay objective with penalties for collision, UAV capacity overload, and secrecy-offloading violations.

## Key findings

- OE-MATD3 converges within 400 training episodes in the parsed mini-batch-size and learning-rate sweeps.
- A mini-batch size of 128 and actor/critic learning rates 0.0001/0.0002 are selected from the convergence comparisons.
- Total delay rises with task size; the proposed joint design remains below random service placement/offloading, fixed UAV deployment, fixed jammer location, OE-MADDPG, and OE-MAA2C baselines.
- Increasing UAV-server cache capacity reduces total delay for all schemes; the proposed method reports about 21% and 67% improvement over OE-MADDPG and OE-MAA2C in the parsed comparison.
- Tightening the minimum secrecy offloading rate increases delay because more jamming power is needed and more devices fall back to local execution.
- Delay decreases as maximum device energy increases, but the improvement slows beyond the parsed energy range because higher transmit power is not always useful under eavesdropping constraints.

## Limitations / future work

The conclusion names multi-time-scale dynamic computation offloading and service placement in satellite-terrestrial integrated networks as future work. Hardware validation is not in parse.

## Relation to the corpus

This source links [[service-caching-mec]] to secure UAV-MEC, while [[hu-2026-ertatd3-secure-caching]] focuses on secure result caching for vehicular tasks. It also broadens the [[multi-agent-td3]] line from anti-jamming and semantic IoV control to service-placement-aware secure offloading.

## Raw artifacts

- `raw/sources/Security-Aware_Designs_of_Multi-UAV_Deployment_Task_Offloading_and_Service_Placement_in_Edge_Computing_Networks/Security-Aware_Designs_of_Multi-UAV_Deployment_Task_Offloading_and_Service_Placement_in_Edge_Computing_Networks.md`
- Original PDF and extracted figures (`images/`) in the same folder.
