---
type: source
title: "Age of Information (AoI)-Aware Joint Optimization for Active RIS and NOMA-Assisted AGMEC Networks"
authors: ["Zhaoyuan Shi", "Zhipeng Bi", "Ruichen Zhang", "Huabing Lu", "Chongwen Huang", "Helin Yang", "Jun Cai", "Dusit Niyato"]
year: 2026
url: "https://doi.org/10.1109/TWC.2026.3686114"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, age-of-information, active-ris, noma, air-ground-integrated-network, mobile-edge-computing, task-offloading, uav-trajectory-control, ddpg, deep-reinforcement-learning]
related:
  - "[[age-of-information]]"
  - "[[active-ris]]"
  - "[[noma]]"
  - "[[air-ground-integrated-network]]"
  - "[[mobile-edge-computing]]"
  - "[[task-offloading]]"
  - "[[uav-trajectory-control]]"
  - "[[ddpg]]"
  - "[[aoi-energy-tradeoff]]"
  - "[[song-2024-mol-aoi-energy]]"
  - "[[qin-2025-matd3-noma-queue-sagin]]"
  - "[[qin-2025-urllc-noma-uav-iscc]]"
  - "[[sun-2024-active-passive-ris-receiver]]"
  - "[[dusit-niyato]]"
created: 2026-07-06
updated: 2026-07-10
---

# Age of Information (AoI)-Aware Joint Optimization for Active RIS and NOMA-Assisted AGMEC Networks

## Citation

Shi, Z., Bi, Z., Zhang, R., Lu, H., Huang, C., Yang, H., Cai, J., & Niyato, D. (2026). *Age of Information (AoI)-Aware Joint Optimization for Active RIS and NOMA-Assisted AGMEC Networks*. **IEEE Transactions on Wireless Communications**, 25, 15879-15894. DOI: 10.1109/TWC.2026.3686114.

## TL;DR

Optimizes task-data freshness in active-RIS and NOMA-assisted air-ground MEC networks. The controller jointly decides UAV trajectory, active-RIS beamforming, and UE task offloading to minimize long-term average AoI. The proposed AADDPG method augments DDPG with an action adjuster for hybrid continuous/discrete actions and a UAV battery-protection mechanism.

## Problem framing

Real-time MEC applications need fresh computation results, not only low latency or high throughput. In air-ground MEC, limited spectrum, unstable channels, UAV energy limits, and offloading decisions jointly affect freshness. The paper adds two physical-layer helpers: NOMA for spectral efficiency and active RIS for controllable amplification/beamforming. The resulting AoI minimization is dynamic, non-convex, mixed-integer, and nonlinear.

## System model

- A base station and UAV both carry MEC servers for $K$ ground UEs.
- An active RIS with $M$ elements is installed on a high-rise building surface to assist offloading.
- NOMA is used for spectrum efficiency, with SIC and an imperfect residual-interference parameter.
- Tasks arrive as a Poisson process; each task can be offloaded to the UAV or the BS.
- AoI updates according to task arrival and successful delivery status.
- The BS acts as centralized controller for UAV trajectory, active-RIS beamforming, and offloading decisions.

## Method

- Models the joint optimization as an MDP with the BS as the sole agent.
- State includes UE AoIs, task lifetimes, UAV position, and UAV remaining energy.
- Action includes active-RIS amplification/phase shifts, UAV speed/direction, and UE offloading decisions.
- Reward combines negative average AoI, UAV energy cost, battery-threshold penalty, and flight-boundary penalty.
- The action adjuster maps continuous offloading outputs to BS/UAV binary choices and forces return-to-base behavior below the UAV energy threshold.

## Key findings

- AADDPG reports average rewards 23% and 60% higher than DDPG and AC in the evaluated setting.
- AADDPG improves average AoI by 23% over conventional DDPG with 1.06% higher runtime.
- NOMA reduces average AoI by 67.68% compared with OMA in the active-RIS setting.
- Active RIS gives 29.28% higher average reward and 33.9% lower average AoI than passive RIS.
- Under SINR drops of 10 dB and 25 dB, AADDPG re-stabilizes AoI within about five episodes.
- Battery-threshold experiments report average AoI around 10 at a 40% threshold and around 6 at a 5% threshold.

## Limitations / future work

Future work targets high-density user scenarios with multi-UAV coordination, stronger robustness in dynamic AGMEC environments, and practical vertical applications such as autonomous driving and industrial IoT.

## Relation to the corpus

This source extends the wiki's [[age-of-information]] branch beyond the [[song-2024-mol-aoi-energy]] AoI-energy tradeoff into active-RIS and NOMA-assisted air-ground MEC. It also complements the RIS/PHY layer: [[sun-2024-active-passive-ris-receiver]] is an anti-jamming active/passive RIS receiver anchor, while this paper uses [[active-ris]] to improve offloading freshness. The NOMA + queue-aware SAGIN source [[qin-2025-matd3-noma-queue-sagin]] is the closest non-terrestrial freshness/queue neighbor, while [[qin-2025-urllc-noma-uav-iscc]] shares the UAV + NOMA + edge-computing setting.

## Raw artifacts

- `raw/sources/Age_of_Information_AoI--Aware_Joint_Optimization_for_Active_RIS_and_NOMA-Assisted_AGMEC_Networks/Age_of_Information_AoI--Aware_Joint_Optimization_for_Active_RIS_and_NOMA-Assisted_AGMEC_Networks.md`
- Original PDF and extracted figures (`images/`) in the same folder.
