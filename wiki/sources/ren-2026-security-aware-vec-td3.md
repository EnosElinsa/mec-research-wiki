---
type: source
modeling_card: required
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
updated: 2026-11-03
---

# UAV-Assisted Security-Aware Vehicular Edge Computing: A TD3-Enhanced Scheme

## Citation

Ren, T., Cui, J., Cao, X., & Ren, Y. (2026). *UAV-Assisted Security-Aware Vehicular Edge Computing: A TD3-Enhanced Scheme*. **IEEE Transactions on Mobile Computing**, 1-14. DOI: 10.1109/TMC.2026.3709174. The top-level local parse is silent on DOI; DOI/venue/year were verified against a title-matched Crossref/IEEE DOI record.

## TL;DR

Formulates UAV-assisted [[vehicular-mec]] under a passive eavesdropper and uses [[td3]] to jointly control UAV movement, VUE offloading ratios, and vehicle-UAV association. Security enters through an effective secure offloading rate, so transmissions below the secure-rate threshold suffer degraded task-upload capacity.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Multiple vehicular user equipments (VUEs) offload tasks to a base station or UAV edge servers in the presence of a passive eavesdropper. Orthogonal VUE bands separate users, UAVs move in time slots, Eve's location has Gaussian estimation error, and the effective secure offloading rate is the positive legitimate-rate minus eavesdropping-rate difference with a threshold penalty.

**Problem & objective**: Problem (12) minimizes the maximum computation latency among all VUEs, where each VUE's latency is the larger of its local time and its offloading-plus-edge time, by jointly selecting offloading ratios $\rho_j$, offloading targets $A_{j,k}$, and UAV positions $Z_k$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Offloading ratio | $\rho_j$ | continuous, $[0,1]$ | Fraction of VUE $j$'s task offloaded |
| Offloading target | $A_{j,k}$ | binary | VUE $j$ offloads to device $k$ (the BS or a UAV) |
| UAV position | $Z_k$ | continuous | Location of UAV $k$ in each slot |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Each VUE's local or offloaded computation latency does not exceed the slot duration $\eta_1$ |
| C2 | $0\le\rho_j\le1$ |
| C3 | Each VUE selects exactly one device, while several VUEs may share a device |
| C4 | Per-slot UAV movement is at most $\eta_0\cdot v_{\max}$ |
| C5 | UAVs keep at least the safe distance $D$ from each other |

**Algorithm**: Cast offloading, movement, and association as a continuous-action MDP → train standard TD3 with centralized state information and distributed execution → use replay, target smoothing, delayed actor updates, and continuous association scores → compute latency from the secure effective rate → execute the learned policy over VUE and UAV slots.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Ren et al. [x] studied security-aware vehicular edge computing assisted by multiple UAV servers and a passive eavesdropper. They formulated a maximum-latency minimization problem that jointly controls VUE offloading ratios, UAV movement, and VUE association with the base station or a UAV while using a secure effective offloading rate. The proposed controller is a TD3 scheme with centralized training and distributed execution, continuous association scores, replay memory, target smoothing, and delayed policy updates. Security affects the task-upload latency through the legitimate-rate and eavesdropping-rate difference and its secure-threshold degradation. Simulations report at least 20% higher cumulative reward and at least 1.7% lower latency than the benchmark schemes, with a 38% latency reduction relative to PPO in the stated three-UAV comparison.

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

- `raw/sources/UAV-Assisted_Security-Aware_Vehicular_Edge_Computing_A_TD3-Enhanced_Scheme/UAV-Assisted_Security-Aware_Vehicular_Edge_Computing_A_TD3-Enhanced_Scheme.md`
- Original PDF and extracted figures (`images/`) in the same folder.
