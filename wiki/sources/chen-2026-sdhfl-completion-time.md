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
updated: 2026-07-16
modeling_card: required
---

# Completion Time Minimization for UAV-Assisted Semi-Decentralized Hybrid Federated Learning

## Citation

Chen, K., Zhang, J., Xiao, Y., Jo, M., & Ng, D. W. K. (2026). *Completion Time Minimization for UAV-Assisted Semi-Decentralized Hybrid Federated Learning*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2025.3634664.

## TL;DR

Proposes semi-decentralized hybrid federated learning (SDHFL) for wide-area IoT: devices reach model consensus inside geographic D2D clusters, while a mobile UAV asynchronously aggregates one selected cluster per global round. Lyapunov control and alternating resource optimization jointly choose clusters, UAV speed, computation, transmit power, and subcarriers to minimize training completion time under energy and queue-stability constraints.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Wide-area IoT devices are partitioned into D2D clusters that perform local training and consensus over OFDMA links. A rotary-wing UAV flies among predefined hovering points, selects one cluster in each global round, receives its consensus model, performs global aggregation, and broadcasts the updated model under non-IID data and round-varying channels.

**Problem & objective**: Problem P1 is a nonconvex MINLP that minimizes the expected overall SDHFL completion time, $\min \mathbb E[T]$, over cluster scheduling, UAV speed, computation, uplink power, D2D subcarrier assignment, and D2D transmit power.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Cluster selection | $a_k(b)$ | Binary, $\{0,1\}$ | Selects cluster $k$ in global round $b$ |
| UAV speed | $v(b)$ | Continuous, $[0,v_{\max}]$ | Controls travel time between hovering points |
| Cluster-head uplink power | $p_k$ | Continuous, $[0,p_{\max}]$ | Sets the selected head's UAV uplink power |
| Device and UAV CPU rates | $f_m,f_u$ | Continuous, $f_{\min}\leq f_m\leq f_{\max}$ and $0\leq f_u\leq f_{u,\max}$ | Allocates computation capacity |
| D2D subcarrier assignment | $s_{m,m',g}^{b}$ | Binary, $\{0,1\}$ | Assigns subcarrier $g$ to a D2D model exchange |
| D2D transmit power | $P_{m,m',g}^{b}$ | Continuous, nonnegative feasible power | Powers the D2D consensus link |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Target model accuracy: $F(\mathbf w^{(B)})-F(\mathbf w^*)\leq\varepsilon$ |
| C2 | Mean-rate queue stability: $\lim_{V\to\infty}g_k(V)=0$ for every cluster $k$ |
| C3 | UAV per-round energy: $E(b)\leq E_{\mathrm{limit}}$ |
| C4 | Selected-head upload: $t_k^u B_U\log_2\!\left(1+\frac{p_kh_k}{B_UN_0}\right)\geq d_k$ |
| C5 | Scheduling and staleness: $a_k(b)\in\{0,1\}$ and $\tau_k^b(a_k(b))\leq\tau_{\max}$ |
| C6 | D2D interference and assignment obey C10 and $s_{m,m',g}^{b}\in\{0,1\}$ |

**Algorithm**: Analyze SDHFL convergence and derive a lower bound on the required global rounds, set the optimal head power and device CPU rate to their maxima, transform queue stability and per-round completion time with a Lyapunov drift-minus-utility bound, alternately optimize UAV speed and relaxed D2D subcarrier and power allocation, recover binary assignments, and select the cluster using the derived queue-aware rule.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Chen et al. [x] studied completion-time minimization for UAV-assisted semi-decentralized hybrid federated learning in wide-area IoT networks with D2D clusters and non-IID data. They formulated a MINLP over cluster selection, UAV speed, device and UAV computation, uplink power, D2D subcarriers, and D2D power under accuracy, queue-stability, energy, staleness, and interference constraints. They derived a convergence bound on the required global rounds and designed a Lyapunov-based adaptive cluster-selection and alternating resource-allocation algorithm. Simulations reported accuracy above 98.26% on MNIST and 65.21% on CIFAR-10, respectively 1.06% and 3.76% above the asynchronous-FL baseline, while the proposed resource controller yielded lower completion time than the compared baselines.

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
