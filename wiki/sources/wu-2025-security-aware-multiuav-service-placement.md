---
type: source
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
created: 2026-07-07
updated: 2026-07-07
---

# Security-Aware Designs of Multi-UAV Deployment, Task Offloading and Service Placement in Edge Computing Networks

## Citation

Wu, M., Wu, H., Lu, W., Guo, L., Lee, I., & Jamalipour, A. (2025). *Security-Aware Designs of Multi-UAV Deployment, Task Offloading and Service Placement in Edge Computing Networks*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2025.3574061. DOI/venue/year are parse-silent at the top level and verified against a title-matched Crossref/IEEE DOI record.

## TL;DR

Studies multi-UAV MEC where devices offload only to UAV servers that have cached the required service program, while eavesdroppers threaten the offloading link. A UAV jammer provides cooperative jamming, and OE-MATD3 jointly learns UAV deployment, offloading, service placement, and jamming power while a closed-form transmit-power solver handles device power.

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

- `raw/sources/Security-Aware Designs of Multi-UAV Deployment- Task Offloading and Service Placement in Edge Computing Networks/Security-Aware Designs of Multi-UAV Deployment- Task Offloading and Service Placement in Edge Computing Networks.md`
- Original PDF and extracted figures (`images/`) in the same folder.
