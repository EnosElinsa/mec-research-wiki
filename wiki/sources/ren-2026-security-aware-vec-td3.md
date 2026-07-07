---
type: source
title: "UAV-Assisted Security-Aware Vehicular Edge Computing: A TD3-Enhanced Scheme"
authors: ["Tao Ren", "Jun Cui", "Xueyan Cao", "Yuzheng Ren"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3709174"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC), pp. 1-14, 2026"
tags: [source, vehicular-mec, uav, physical-layer-security, td3, offloading]
related:
  - "[[vehicular-mec]]"
  - "[[td3]]"
  - "[[physical-layer-security]]"
  - "[[task-offloading]]"
  - "[[uav-trajectory-control]]"
created: 2026-07-07
updated: 2026-07-07
---

# UAV-Assisted Security-Aware Vehicular Edge Computing: A TD3-Enhanced Scheme

## Citation

Ren, T., Cui, J., Cao, X., & Ren, Y. (2026). *UAV-Assisted Security-Aware Vehicular Edge Computing: A TD3-Enhanced Scheme*. **IEEE Transactions on Mobile Computing**, 1-14. DOI: 10.1109/TMC.2026.3709174. The top-level local parse is silent on DOI; DOI/venue/year were verified against a title-matched Crossref/IEEE DOI record.

## TL;DR

Formulates UAV-assisted [[vehicular-mec]] under a passive eavesdropper and uses [[td3]] to jointly control UAV movement, VUE offloading ratios, and vehicle-UAV association. Security enters through an effective secure offloading rate, so transmissions below the secure-rate threshold suffer degraded task-upload capacity.

## Problem

Vehicular tasks need low-latency edge execution while vehicle and UAV positions change rapidly. A passive Eve can intercept VUE-to-UAV uploads, making ordinary rate-maximizing offloading unsafe. The paper minimizes the maximum computation latency while accounting for secure offloading, dynamic UAV placement, and association decisions.

## System model

The system contains a base station, multiple vehicular user equipments, multiple UAV edge servers, and a malicious eavesdropper. Time slots include parameter-optimization and computation subslots. VUE frequency bands are orthogonal. Eve's location is estimated with Gaussian error, and the secure offloading rate is modeled as the positive difference between the legitimate offloading rate and the eavesdropping rate, then degraded by a factor when it falls below a secure threshold.

## Method

The paper casts the joint offloading, UAV-movement, and association problem as a DRL task. The [[td3|TD3]] controller uses centralized training and distributed execution, continuous association scores for discrete vehicle-UAV association, replay memory, target smoothing, and delayed policy updates. The state contains entity positions and VUE task sizes; the action contains UAV movement, offloading ratios, and association scores. The reward is latency-oriented, while security affects the effective rate used to compute latency.

## Key findings

- Optimizing UAV positions improves reward and convergence relative to random UAV placement.
- TD3 stabilizes at a higher final reward than DDPG, PPO, and random baselines in the parsed reward curves; DDPG converges faster but to a lower reward.
- A learning rate of 0.001 balances convergence speed and stability in the reported sweep.
- With 3 UAVs, TD3 reduces latency by 38% relative to PPO and 1% relative to DDPG in the parsed comparison; with 20 VUEs, the corresponding improvements are 47% and 12%.
- The abstract/conclusion report cumulative rewards at least 20% higher and latency at least 1.7% lower than the benchmark schemes.
- Increasing transmit power from 0.01 W to 10 W lowers latency from 3.947 s to 2.048 s in the parsed sensitivity analysis.

## Limitations / future work

The paper uses fixed UAV altitude and does not model onboard UAV energy. It names energy-aware trajectory design, 3D trajectory optimization, hybrid DRL-optimization, and multiple-eavesdropper settings as future extensions.

## Relation to the corpus

This source adds a security-aware offloading entry to the [[vehicular-mec]] track. It complements [[hu-2026-ertatd3-secure-caching]], which secures vehicular task-result caching, and [[beishenalieva-2026-secrecy-aware-uav-path-planning]], which protects UAV-assisted ITS offloading against malicious aerial eavesdroppers and jammers. Methodologically, it is a plain TD3 control counterpart to ERTATD3 and SC-MA-TD3 variants already in the corpus.

## Raw artifacts

- `raw/sources/UAV-Assisted Security-Aware Vehicular Edge Computing A TD3-Enhanced Scheme/UAV-Assisted Security-Aware Vehicular Edge Computing A TD3-Enhanced Scheme.md`
- Original PDF and extracted figures (`images/`) in the same folder.
