---
type: source
title: "Traffic-Aware Lightweight Hierarchical Offloading Toward Adaptive Slicing-Enabled SAGIN"
tags:
  - source
  - sagin
  - computation-offloading
  - network-slicing
  - deep-reinforcement-learning
  - knowledge-distillation
  - traffic-prediction
related:
  - "[[space-air-ground-integrated-network]]"
  - "[[leo-satellite-edge-computing]]"
  - "[[task-offloading]]"
  - "[[mobile-edge-computing]]"
  - "[[hierarchical-aerial-mec]]"
  - "[[ppo]]"
  - "[[gae]]"
  - "[[ddqn]]"
  - "[[task-priority-in-mec]]"
  - "[[network-slicing]]"
  - "[[traffic-aware-offloading]]"
  - "[[knowledge-distillation-for-drl]]"
  - "[[probsparse-self-attention-prediction]]"
  - "[[dynamic-confidence-interval-clipping]]"
  - "[[nabi-2025-jour-hierarchical-aerial]]"
  - "[[jia-2025-dro-uav-hap-mec]]"
  - "[[liu-2025-haps-uav-maritime-iot]]"
  - "[[zhang-2025-mcma-task-migration]]"
created: 2026-05-29
updated: 2026-05-29
authors:
  - Zheyi Chen
  - Junjie Zhang
  - Geyong Min
  - Zhaolong Ning
  - Jie Li
year: 2024
url: "https://doi.org/10.1109/JSAC.2024.3459020"
venue: "IEEE Journal on Selected Areas in Communications (JSAC), Vol. 42, No. 12, Dec. 2024"
---

# Traffic-Aware Lightweight Hierarchical Offloading Toward Adaptive Slicing-Enabled SAGIN

## TL;DR
THOAS is a traffic-aware hierarchical offloading framework for slicing-enabled [[space-air-ground-integrated-network|SAGIN]] that splits the network into **Communication Access Platforms (CAPs)** and **Computation Offloading Platforms (COPs)** for fine-grained [[network-slicing|slice]] provisioning. It combines a [[probsparse-self-attention-prediction|probsparse self-attention traffic predictor]] for adaptive slice resource allocation with an improved [[ppo|PPO]]-based DRL offloader that uses [[gae|GAE]] and a [[dynamic-confidence-interval-clipping|dynamic-confidence-interval clipping]] rule, then compresses the converged policy via [[knowledge-distillation-for-drl|policy distillation]] into a lightweight network. On real-world Milan cellular traffic it outperforms prediction and offloading baselines on ESP profit, prediction MSE, resource utilization, and deadline-violation ratio, while shrinking the model to ~6% size at ~73% retained performance.

## Problem
The emerging [[space-air-ground-integrated-network|SAGIN]] empowers [[mobile-edge-computing|MEC]] with global coverage by integrating LEO satellites, UAVs, and ground base stations, but fluctuating user traffic and a constrained, heterogeneous computing architecture seriously degrade QoS and resource utilization. Existing work assumes static traffic / fixed capacity, depends on prior knowledge, or ignores the cost and service interruption caused by frequent slice adjustments — leading to resource under- or over-supply. Because satellites and UAVs are low-power and compute-weak, heavy DRL models are impractical to run on them. The paper addresses the **coupled, NP-hard** problem of joint slice resource allocation and [[task-offloading|computation offloading]], maximizing the long-term profit of an Edge Service Provider (ESP) that rents communication/compute slices from an Infrastructure Provider (InP) and is paid by users only when tasks finish within a maximum tolerable delay.

## System model
- **Two-plane hierarchy:** SAGIN is separated into **CAPs** (satellite, BS, UAVs supplying OFDM subchannels/SCs) and **COPs** (BS and UAVs supplying VMs). InP virtualizes SCs/VMs as slices sold to the ESP; the ESP rents/adjusts slices and earns priority-weighted revenue from on-time tasks. See [[hierarchical-aerial-mec]] and [[network-slicing]].
- **Task tuple:** `<data size d_i, computational density η_i, priority ρ_i, connected CAP a_i, distance l_i, executing COP o_i>`, with [[task-priority-in-mec|priorities]] ρ_i ∈ {1,2,3} weighting revenue.
- **Channel model:** BS/UAV links use log-distance path loss with Gaussian shadowing; satellite links use a free-space model with antenna gains and Weibull rain attenuation. Upload rate follows Shannon's theorem over allocated SCs.
- **Routing:** BS tasks execute directly; satellite tasks relay to BS over the space-ground link; UAV tasks execute locally or forward to BS via air-space + space-ground links. Satellites are treated as **relays only** (compute too costly).
- **Timing/economics:** completion time = upload + transmission + queuing + execution; revenue accrues only if completed within `T^max`; cost = rented SC + VM prices. Slices are adjusted only every `T^slice` slots to bound interruption cost; `T^max` is split into communication (`ω·T^max`) and computing (`(1−ω)·T^max`) budgets.

## Method
- **Objective (P1):** maximize long-term ESP profit `Σ(R^t − C^t)` over slice policies `B, F` and offloading policy `π` subject to SC/VM capacity limits; proven **NP-hard** by reduction from the Multiple Knapsack Problem.
- **Adaptive slice allocation:** a [[probsparse-self-attention-prediction|probsparse self-attention]] predictor (Informer-style, with inter-layer self-attention distillation, Conv1d/ELU/MaxPool, decoder + MLP head) forecasts traffic at `O(log L)` per query. Future loads/demands are inferred and the slice set is sized at `(1+δ)·peak`; adjustment fires only when expected profit gain exceeds interruption cost (`ΔP − C^int > 0`). On-demand SCs are computed in closed form using a worst-case `SNR^min` (Three-Sigma rule guarantees the upload budget with ≈99.7% probability).
- **Lightweight DRL offloading:** MDP with state = VM queues + required compute frequency + user priority; action = pick a VM or **forward to BS** when UAV capacity is insufficient; reward = priority-weighted revenue. Actor-critic [[ppo|PPO]] with [[gae|GAE]] and a new [[dynamic-confidence-interval-clipping|two-layer clipping rule]] whose confidence factor adapts to the TD-error sign to improve sample efficiency over fixed-clip PPO.
- **Compression:** [[knowledge-distillation-for-drl|policy distillation]] transfers the converged deep teacher to a shallow student via temperature-softened KL loss, lowering inference overhead for resource-limited SAGIN.

## Key findings
- **Convergence:** THOAS converges to higher reward than PPO-TO, [[ddqn|DDQN-TS]], and DQNM; distillation converges in ~50 epochs.
- **Compression:** at 6% of teacher size the student keeps ~73% performance; ~90% at 12%, ~97% at 50% size.
- **Profit/accuracy:** highest ESP profit (~1400 USD vs ~1050 GL-TCN / ~850 PredRNN / ~700 Static) and lowest traffic-prediction MSE; static provisioning is worst because over-deadline tasks earn nothing.
- **Latency:** slightly higher transmission time (UAV→BS forwarding) but much lower queuing/execution, giving the shortest total completion time among DRL baselines.
- **Utilization & reliability:** higher resource utilization than GL-TCN/PredRNN across 0.5x–1.5x traffic, and the lowest deadline-violation ratio under varying `T^max`.
- **Sensitivity:** profit peaks at moderate slice expansion (`δ ≈ 0.10`) and communication delay ratio (`ω ≈ 0.2`); THOAS dominates across both sweeps.

## Limitations
Simulation-only (single RTX 3090 workstation, PyTorch); no hardware/testbed or live satellite/UAV deployment. Traffic is emulated from a single dataset (Milan cellular, Internet service, three regions mapped to BS/UAV/satellite), so cross-pattern generalization is untested. The topology is small (one satellite, one BS, multiple UAVs); satellites are relay-only, and UAV mobility, handover, orbital dynamics, and battery/energy constraints are not modeled in the optimization. Sparse/low traffic raises prediction error and lowers utilization. Parallel offloading, efficient communication, and [[service-caching-mec|service caching]] are deferred to future work.

## Relation to the corpus
This paper sits at the intersection of [[space-air-ground-integrated-network|SAGIN]] / [[leo-satellite-edge-computing|LEO satellite edge computing]] and [[task-offloading|computation offloading]], and introduces [[network-slicing]] and [[traffic-aware-offloading]] as organizing ideas. Its lightweight DRL contributions — [[ppo|PPO]] + [[gae|GAE]] with [[dynamic-confidence-interval-clipping]], compressed via [[knowledge-distillation-for-drl|policy distillation]] — extend the corpus's DRL-for-MEC thread beyond baselines like [[ddqn|DDQN]]. The CAP/COP hierarchy connects to [[hierarchical-aerial-mec]] and to [[nabi-2025-jour-hierarchical-aerial]] (hierarchical aerial MEC), [[jia-2025-dro-uav-hap-mec]] (multi-tier UAV/HAP MEC under uncertainty), and [[liu-2025-haps-uav-maritime-iot]] (space/air edge in coverage-limited regions). Its load/traffic-driven scheduling across heterogeneous tiers relates to [[zhang-2025-mcma-task-migration]] (task migration), and its [[task-priority-in-mec|priority-weighted]] revenue model ties into corpus QoS/profit framings.

## Raw artifacts
- `raw/sources/Traffic-Aware_Lightweight_Hierarchical_Offloading_Toward_Adaptive_Slicing-Enabled_SAGIN/full.md`
