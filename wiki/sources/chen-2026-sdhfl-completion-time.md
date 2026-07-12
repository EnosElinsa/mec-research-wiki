---
type: source
title: "Completion Time Minimization for UAV-Assisted Semi-Decentralized Hybrid Federated Learning"
authors: ["Kui Chen", "Jing Zhang", "Yong Xiao", "Minho Jo", "Derrick Wing Kwan Ng"]
year: 2026
url: "https://doi.org/10.1109/TMC.2025.3634664"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, federated-learning, uav, d2d, lyapunov-optimization, completion-time, resource-allocation]
related:
  - "[[semi-decentralized-hybrid-federated-learning]]"
  - "[[federated-learning]]"
  - "[[device-to-device-communication]]"
  - "[[overlay-underlay-spectrum-access]]"
  - "[[lyapunov-optimization]]"
  - "[[mixed-integer-nonlinear-programming]]"
  - "[[queueing-theory]]"
  - "[[uav-trajectory-control]]"
  - "[[han-2024-ground-satellite-fl]]"
  - "[[zhai-2023-fedleo-decentralized-fl]]"
created: 2026-07-12
updated: 2026-07-12
---

# Completion Time Minimization for UAV-Assisted Semi-Decentralized Hybrid Federated Learning

## Citation

Chen, K., Zhang, J., Xiao, Y., Jo, M., & Ng, D. W. K. (2026). *Completion Time Minimization for UAV-Assisted Semi-Decentralized Hybrid Federated Learning*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2025.3634664.

## TL;DR

Proposes semi-decentralized hybrid federated learning (SDHFL) for wide-area IoT: devices reach model consensus inside geographic D2D clusters, while a mobile UAV asynchronously aggregates one selected cluster per global round. Lyapunov control and alternating resource optimization jointly choose clusters, UAV speed, computation, transmit power, and subcarriers to minimize training completion time under energy and queue-stability constraints.

## Problem

Large-area FL combines non-IID data, heterogeneous devices, stragglers, limited batteries, unstable data queues, intermittent UAV coverage, and travel/communication delay. Fully centralized aggregation burdens the aerial link, while fully decentralized learning lacks the UAV's global coordination role.

## System model

- Ground devices are partitioned into non-overlapping clusters with designated heads and static undirected D2D consensus graphs.
- Short-range D2D exchange uses OFDMA and spectrum separated from the UAV link.
- A rotary-wing UAV follows a flight-hover-flight route through predefined hovering points and aggregates one selected cluster per global round.
- Unselected clusters continue local training from their most recent global model; each device also maintains a data queue.
- Each selected round contains local training, D2D consensus, cluster-head uplink, and UAV global aggregation/broadcast.

## Method

The paper formulates a non-convex MINLP over dynamic cluster selection, UAV speed, device CPU frequency, transmit power, and subcarrier allocation. It proves convergence under smoothness and strong-convexity assumptions and derives a lower bound on the required global rounds. A Lyapunov drift-minus-utility controller handles cluster selection and queue stability; alternating convex approximations optimize UAV speed and relaxed communication resources before recovering binary assignments.

## Key findings

- Simulations cover 3-8 clusters with 7-9 devices per cluster in a `10^6 m^2` area, UAV altitude 30 m, maximum UAV speed 16 m/s, 10 MHz UAV bandwidth, 8 kJ per-round UAV energy, and a 2.81 MB model.
- SDHFL exceeds 98.26% accuracy on MNIST and 65.21% on CIFAR-10, respectively 1.06% and 3.76% above the asynchronous-FL baseline in the reported experiments.
- At the stated target parameter `phi=0.05`, the reported completion-time optimum is four clusters for both the proposed method and baseline 2, with lower completion time for SDHFL.
- Completion time decreases as UAV energy, CPU-frequency limits, or maximum UAV speed increase, while the proposed method remains below the three compared baselines in the textual comparisons.
- The parse reports a non-monotone device-count effect, but two passages describe the direction in opposite order; this page does not resolve that inconsistency.

## Limitations / parse caveats

The evidence is convergence analysis and simulation, not a field deployment. Assumptions include smooth strongly convex objectives, sufficiently large device buffers, fixed hovering points, static D2D connectivity, bounded CSI errors, LoS UAV-head links, and one selected cluster per global round. Noise density is `-174 dBm/Hz` in prose and `-170 dBm/Hz` in Table III. Several units and equations are OCR-damaged. Publication metadata is absent from the parse and was verified through the exact-title Crossref record; technical claims and values come only from the parse.

## Relation to the corpus

[[semi-decentralized-hybrid-federated-learning]] differs from server-free [[decentralized-federated-learning]]: local D2D consensus reduces aerial aggregation traffic, but the UAV remains the global aggregator. It complements [[han-2024-ground-satellite-fl]] and [[zhai-2023-fedleo-decentralized-fl]] by combining cluster-level consensus, asynchronous aerial aggregation, and completion-time resource control in a terrestrial IoT setting.

## Raw artifacts

- Parse: `raw/sources/Completion_Time_Minimization_for_UAV-Assisted_Semi-Decentralized_Hybrid_Federated_Learning/Completion_Time_Minimization_for_UAV-Assisted_Semi-Decentralized_Hybrid_Federated_Learning.md`
- Origin PDF: `raw/sources/Completion_Time_Minimization_for_UAV-Assisted_Semi-Decentralized_Hybrid_Federated_Learning/Completion_Time_Minimization_for_UAV-Assisted_Semi-Decentralized_Hybrid_Federated_Learning.pdf`
- Figures: `raw/sources/Completion_Time_Minimization_for_UAV-Assisted_Semi-Decentralized_Hybrid_Federated_Learning/images/`
