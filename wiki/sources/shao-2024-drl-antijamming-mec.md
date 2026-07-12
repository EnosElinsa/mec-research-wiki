---
type: source
title: "Deep Reinforcement Learning-Based Resource Management for UAV-Assisted Mobile Edge Computing Against Jamming"
tags: [source, uav-mec, anti-jamming, multi-agent-drl, resource-management, td3]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[mobile-edge-computing]]"
  - "[[anti-jamming-mec]]"
  - "[[multi-agent-td3]]"
  - "[[prioritized-experience-replay]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[ddpg]]"
  - "[[csi-estimation-error]]"
  - "[[physical-layer-security]]"
  - "[[spectrum-sensing-channel-selection]]"
  - "[[energy-latency-tradeoff]]"
  - "[[qin-2025-bcuav-masac]]"
  - "[[ma-2025-pdqn-vehicular-mec]]"
  - "[[bao-2025-ddpg-video-offloading]]"
  - "[[wu-2026-terrain-aware-uav-mec]]"
  - "[[zhu-2025-lycnn-drl-wpt-mec]]"
  - "[[hardware-validation-and-sim-to-real-in-mec]]"
  - "[[zehui-xiong]]"
  - "[[yang-2026-embodied-antijamming-uav]]"
  - "[[embodied-anti-jamming-resource-allocation]]"
created: 2026-05-29
updated: 2026-07-13
authors: [Ziling Shao, Helin Yang, Liang Xiao, Wei Su, Yifan Chen, Zehui Xiong]
year: 2024
url: https://doi.org/10.1109/TMC.2024.3432491
venue: "IEEE Transactions on Mobile Computing (TMC)"
---

# Deep Reinforcement Learning-Based Resource Management for UAV-Assisted Mobile Edge Computing Against Jamming

## TL;DR
A [[multi-uav-assisted-mec]] system where each UAV serves one ground user faces multiple malicious jammers plus co-channel interference, and the objective is to minimize a weighted sum of latency and energy consumption (the [[energy-latency-tradeoff]] cost Ω = ξ·T + (1−ξ)·E). The authors jointly tune each UAV's CPU frequency, bandwidth allocation, and channel selection using **PER-MATD3** — a multi-agent twin-delayed DDPG ([[multi-agent-td3]]) with [[prioritized-experience-replay]]. Simulation and a Raspberry Pi / USRP testbed show lower system cost and faster convergence than single-agent, non-PER, no-channel-selection, and random baselines.

## Problem
UAVs serving as aerial edge servers compute tasks and transmit results to ground users over wireless downlinks that are vulnerable to malicious [[anti-jamming-mec|jamming]] and to co-channel interference when UAVs reuse channels. Most prior UAV-[[mobile-edge-computing]] resource-allocation work ignores jamming, and classical/heuristic optimizers are too slow for the non-convex, time-varying environment. The paper formulates joint computing-and-communication resource management under multiple jammers, minimizing the weighted sum of total latency and energy. Decision variables per UAV are the CPU frequency adjustment factor, bandwidth allocation share, and subchannel selection, all under time-varying compute capacity and imperfect CSI ([[csi-estimation-error]]).

## System model
- **Actors:** K UAVs (aerial servers) and J jammers; K air-to-ground downlink pairs, one ground user per UAV. Jammers may be flexibly deployed UAVs.
- **Two stages per slot:** computation on the UAV, then transmission UAV → user (downlink only).
- **Compute:** latency T_comp = D·c/(η·f); energy ∝ ϑ·(η·f)²·c·D with effective switched capacitance ϑ.
- **Comms:** SINR accounts for jammer power via a jammed-channel access indicator ρ∈{0,1}, summed co-channel interference, and noise; capacity C = (1−ε)·β·B·log2(1+SINR), ε = spectrum-sensing time fraction, β = bandwidth share.
- **Imperfect CSI:** h = ĥ + Δh random perturbation models observation error / channel variation.
- **Anti-jamming sensing:** energy-detection [[spectrum-sensing-channel-selection|spectrum sensing]] detects/locates jammed subchannels so UAVs switch to a free channel (ρ=0).
- **Cost:** Ω = ξ·T + (1−ξ)·E with bandwidth constraint Σβ < 1; assumes fully cooperative UAVs and a ~1000-round battery budget.

## Method
- **Formulation:** multi-agent MDP, continuous state/action. State = {CPU freq, imperfect CSI, available bandwidth, received jamming + co-channel interference}; action = {CPU freq factor η, bandwidth β, channel φ}; cooperative reward r = −Ω.
- **Algorithm:** **PER-MATD3** — each agent runs TD3 (a [[ddpg]] variant) with clipped double Q-learning, target policy smoothing, and delayed actor updates, plus a multi-agent [[prioritized-experience-replay]] (TD-error priorities, sum-tree O(log N) sampling, importance-sampling correction).
- **Training:** [[centralized-training-decentralized-execution]] — critics see joint actions/global state in training, agents act on local observations at execution; Adam, ReLU, soft target updates.
- **Theory:** Theorem 1 argues convergence via clipped double Q-learning (extending TD3's proof) even under jamming, given standard sampling and learning-rate conditions.

## Key findings
- ξ = 0.5 minimizes system cost and best balances latency vs energy (Fig. 3).
- PER-MATD3-JSC converges fastest and to the lowest cost of six methods; PER accelerates convergence over plain MATD3-JSC.
- Increasing jammers 1→5 (8 UAVs/users): PER-MATD3-JSC holds latency ~flat (~11.2) via channel selection, while non-selecting / random degrade (Fig. 7).
- Lowest weighted cost across 4→12 users vs PER-TD3-JSC, MATD3-JSC, Non-Selecting, Static(η=0.5), Random (Fig. 6).
- **Hardware** (Raspberry Pi 4B on DJI Tello, USRP N210/X310, 2.4 GHz, 5 channels, ~25 dBm jamming): channel selection holds latency ~4.0 s vs ~10.9–13.7 s, throughput ~28.7–36.5 vs ~12.2–31.6 Mbit/s, energy ~8.0 vs ~9.0 J (Figs. 11–13). Measured jammed-channel power ~−30 dBm vs co-channel ~−50 dBm.

## Limitations
Both simulation and a small **indoor** hardware experiment are shown, but the testbed is assumed ideal/stable (no weather/outdoor effects) with deliberately large jamming power for clean sensing. Scope is downlink-only with one user per UAV and no UAV trajectory optimization. Assumes cooperative UAVs and a sensing module able to detect/localize jammers. Future work: outdoor settings, multi-UAV trajectory optimization, and UAV scheduling.

## Relation to the corpus
This is the corpus's anchor for [[anti-jamming-mec]] resource management, complementing — and distinct from — [[physical-layer-security]] and the defensive [[friendly-jamming-uav]] concept (here jamming is the adversary, sensed and avoided rather than used). Methodologically it sits in the multi-agent DRL family alongside [[qin-2025-bcuav-masac]] (MASAC) and shares the actor-critic lineage ([[ddpg]], [[multi-agent-td3]]) with [[bao-2025-ddpg-video-offloading]]. As UAV-assisted MEC resource management it links to [[wu-2026-terrain-aware-uav-mec]], [[zhu-2025-lycnn-drl-wpt-mec]], and [[ma-2025-pdqn-vehicular-mec]], and it shares the [[energy-latency-tradeoff]] objective and [[csi-estimation-error]] modeling common across the MEC corpus.

## Raw artifacts
- `raw/sources/Deep_Reinforcement_Learning-Based_Resource_Management_for_UAV-Assisted_Mobile_Edge_Computing_Against_Jamming/full.md`
- Original PDF (`61d1a406-15d3-42b7-9873-b406053311ee_origin.pdf`) and extracted figures (`images/`) in the same folder.
