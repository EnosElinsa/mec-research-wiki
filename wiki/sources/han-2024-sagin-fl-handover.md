---
type: source
title: "Orchestrating Federated Learning in Space-Air-Ground Integrated Networks: Adaptive Data Offloading and Seamless Handover"
tags: [source, federated-learning, sagin, leo-satellite, data-offloading, handover, mec]
related:
  - "[[space-air-ground-integrated-network]]"
  - "[[leo-satellite-edge-computing]]"
  - "[[federated-learning]]"
  - "[[seamless-handover]]"
  - "[[adaptive-inter-layer-data-offloading]]"
  - "[[walker-star-constellation]]"
  - "[[privacy-sensitive-data-partitioning]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[load-balancing-uav-mec]]"
  - "[[makespan-minimization]]"
  - "[[mao-2025-bcsa-frl]]"
  - "[[nabi-2025-jour-hierarchical-aerial]]"
  - "[[jia-2025-dro-uav-hap-mec]]"
  - "[[liu-2025-haps-uav-maritime-iot]]"
created: 2026-05-29
updated: 2026-05-29
authors: [Dong-Jun Han, Wenzhi Fang, Seyyedali Hosseinalipour, Mung Chiang, Christopher G. Brinton]
year: 2024
url: https://doi.org/10.1109/JSAC.2024.3459090
venue: "IEEE Journal on Selected Areas in Communications (JSAC)"
---

# Orchestrating Federated Learning in Space-Air-Ground Integrated Networks: Adaptive Data Offloading and Seamless Handover

## TL;DR
A [[federated-learning]] framework for remote regions that lack terrestrial base stations, using LEO satellites and UAVs in a [[space-air-ground-integrated-network]] as both edge-computing units and model aggregators. Each global round, ground devices adaptively offload portions of their non-sensitive data across the three layers according to satellites' time-varying compute power and limited coverage times ([[adaptive-inter-layer-data-offloading]]), and a data/model [[seamless-handover]] passes the dataset and partially trained model to the next incoming satellite so training continues uninterrupted. The authors analyze per-round latency, optimize offloading via nested bisection search, prove convergence to a stationary point for non-convex losses, and show faster time-to-accuracy than baselines on MNIST/FMNIST/CIFAR-10.

## Problem
Remote regions (mountains, forests, deserts, coasts, rural farms, disaster/maritime zones) hold valuable ground-device data from IoT sensors, vehicles, and hospitals, but lack the terrestrial base stations that conventional FL needs for aggregation, and the ground devices have weak compute. The paper orchestrates FL across the space, air, and ground tiers of a SAGIN so that satellites and UAVs act both as model aggregators (handling the missing base station) and as edge computing units (handling weak ground compute). This introduces challenges absent in terrestrial FL: satellite mobility, heterogeneous/time-varying compute, and inconsistent coverage times of incoming LEO satellites — all while minimizing training latency and preserving convergence guarantees.

## System model
- Three tiers: ground (K=50 devices in a 1200 m × 1200 m base-station-free region), air ([[multi-uav-assisted-mec]] with N=5 UAVs at 20 km, each serving 10 disjoint devices), and space ([[leo-satellite-edge-computing]] with a series of moving LEO satellites, one covering the region at a time).
- Connectivity: device → associated air node → current satellite; satellites relay via inter-satellite links (ISL).
- Data: device dataset splits into privacy-sensitive (local-only) and non-sensitive (offloadable) parts with portion alpha (default 0.8) — see [[privacy-sensitive-data-partitioning]]. Space/air nodes hold no data initially.
- FL objective: minimize dataset-size-weighted sum of local losses; FedAvg-style aggregation weighted by per-node data portions.
- Latency model: per-node compute time = m · |dataset| / f (CPU frequency); ISL handover delay = (model size + per-sample size · |D_S|) / ISL rate; satellite-side latency is a recursive, per-coverage-window expression that triggers handover when a satellite cannot finish in its window.
- Constellation: MATLAB [[walker-star-constellation]] with 80 LEO satellites over 5 orbits at 800 km altitude, 85° inclination, 15° min elevation; coverage times via accessIntervals. Channels: Rayleigh fading for ground-air (free-space LoS variant also tested).
- Standard analysis assumptions: L-smoothness, bounded stochastic-gradient variance, bounded gradient dissimilarity (data heterogeneity).

## Method
- Per round: adaptive inter-layer offloading, then parallel local training at ground/air/satellite, intra-layer data/model handover when coverage expires, then weighted (FedAvg) global aggregation through air nodes to the satellite.
- [[adaptive-inter-layer-data-offloading]]: derives the no-offloading per-round latency as a max over the space-layer completion time and the air-node completion + air-to-satellite upload. Two regimes — Case I offloads space → air/ground when satellites are resource-poor; Case II offloads air/ground → space when satellites are resource-rich — with offloading capped by each device's non-sensitive data.
- Optimization: minimize the per-round max completion time (a [[makespan-minimization]]-style latency) over the offloaded data amounts, solved by hierarchical nested bisection search exploiting monotonicity (Algorithm 1: air node vs its ground devices; Algorithm 2: across all layers). Runs at the nearest gateway, then dispatches the plan to nodes. Complexity is logarithmic in the bisection precisions and linear in the number of nodes.
- [[seamless-handover]]: the departing satellite sends its updated model and dataset to the next satellite over an ISL so local training resumes seamlessly; repeated until the round's space-layer data is processed.
- Convergence (Theorem 1): with η^(r) ≤ 1/(2√(1+c_r) H L) and a decaying η=η0/(r+1) or constant η=1/√(HR) learning rate, the time-averaged squared gradient norm vanishes, guaranteeing convergence to a stationary point of the non-convex loss even under per-round adaptive offloading.

## Key findings
- On MNIST, FMNIST, and CIFAR-10 (IID and non-IID), the proposed scheme reaches target accuracy with less training time than every baseline; ordering: proposed > adaptive-without-satellites / adaptive-without-air-nodes > static optimization / offload-proportional-to-compute > no-offloading.
- Ground-only (no offloading) is slowest, confirming the value of using space/air nodes as edge computing units rather than mere aggregators; adaptive offloading clearly beats a fixed one-shot solution.
- Allocation adapts to compute/battery: with ample space+air CPU only ~20% of samples stay on ground (the minimum set by 1 − alpha = 0.2); with scarce resources more data stays on ground and the air layer gets more than the space layer.
- Larger alpha yields faster time-to-target-accuracy (alpha=0 degenerates to plain FL). Approximate figure-read values: MNIST to 95% ~800 s (alpha=0.8) vs ~2900 s (alpha=0); FMNIST to 88% ~3500 s (alpha=0.8) vs ~10000 s (alpha=0).
- A free-space line-of-sight channel speeds up all schemes versus Rayleigh fading, with the proposed method still leading.

## Limitations
Simulation-only (no hardware/real-satellite testbed). UAV trajectories are fixed (not optimized) and there is no base-station or GEO tier — both flagged as future work. Energy enters only abstractly via CPU frequency, with no explicit energy objective. The scheme assumes a known offloadable non-sensitive fraction alpha and estimable coverage times, uses FedAvg aggregation, and relies on standard FL convergence assumptions. Parsed accuracy-vs-time figures appear partly reconstructed by the PDF extractor, so only qualitative orderings and captioned target accuracies are treated as reliable.

## Relation to the corpus
This is one of the first works to jointly optimize [[adaptive-inter-layer-data-offloading]] and intra-space [[seamless-handover]] for [[federated-learning]] across a [[space-air-ground-integrated-network]], extending [[leo-satellite-edge-computing]] and [[multi-uav-assisted-mec]] from pure connectivity/compute toward distributed ML. It complements [[mao-2025-bcsa-frl]] (federated/reinforcement learning over aerial-edge nodes — and the corpus's other FL entry), [[nabi-2025-jour-hierarchical-aerial]] (hierarchical multi-tier aerial MEC offloading), [[jia-2025-dro-uav-hap-mec]] (multi-tier UAV/HAP MEC under uncertainty), and [[liu-2025-haps-uav-maritime-iot]] (non-terrestrial coverage and computing for remote/maritime regions). It shares the [[task-offloading]] and [[load-balancing-uav-mec]] themes of the corpus but reframes them around moving data samples (not tasks) to balance a [[makespan-minimization]]-style per-round training latency.

## Raw artifacts
- `raw/sources/Orchestrating_Federated_Learning_in_Space-Air-_Ground_Integrated_Networks_Adaptive_Data_Offloading_and_Seamless_Handover/full.md`
