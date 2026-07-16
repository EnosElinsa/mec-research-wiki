---
type: source
title: "Integrated Sensing, Computation, and Communication for UAV-Assisted Federated Edge Learning"
authors: ["Yao Tang", "Guangxu Zhu", "Wei Xu", "Man Hon Cheung", "Tat-Ming Lok", "Shuguang Cui"]
year: 2025
url: "https://doi.org/10.1109/TWC.2024.3523381"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
modeling_card: required
tags: [source, isac, federated-edge-learning, uav, resource-allocation, alternating-optimization, integrated-sensing-computation-communication]
related:
  - "[[aerial-federated-aggregation-design-space]]"
  - "[[guangxu-zhu]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[integrated-sensing-computation-communication]]"
  - "[[federated-learning]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[uav-trajectory-control]]"
  - "[[meng-2024-uav-isac-overview]]"
  - "[[han-2024-sagin-fl-handover]]"
  - "[[zhai-2023-fedleo-decentralized-fl]]"
created: 2026-05-29
updated: 2026-07-16
---

# Integrated Sensing, Computation, and Communication for UAV-Assisted Federated Edge Learning

## Citation

Tang, Y., Zhu, G., Xu, W., Cheung, M. H., Lok, T.-M., & Cui, S. (2025). *Integrated Sensing, Computation, and Communication for UAV-Assisted Federated Edge Learning*. **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2024.3523381. (Date of publication 6 Jan 2025; date of current version 11 Apr 2025.)

## TL;DR

Jointly designs **UAV deployment + resource allocation** for **federated edge learning (FEEL)** where UAV-mounted edge devices sense data, compute, and communicate — all competing for limited onboard resources. The paper links UAV deployment to sensing quality (human motion recognition), derives a training-loss upper bound as a function of successful sensing probability, and minimizes total training time by jointly optimizing deployment and integrated sensing-computation-communication (ISCC) resources via **alternating optimization** (the BBPO scheme: bandwidth, batch size, position).

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Multiple UAVs sense human-motion spectrograms, train local FEEL models, and upload updates to an edge server. UAV position controls sensing success and communication distance, while batch size and bandwidth control convergence and per-round latency.

**Problem & objective**: Problem P1 minimizes total training time $N T_{\max}$ by jointly choosing the number of rounds, per-UAV batch sizes, UAV positions, and uplink bandwidths subject to an FEEL optimality-gap target.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Training rounds | $N$ | positive integer | Number of FEEL rounds used to reach the loss target |
| Batch size | $\delta_k$ | positive integer | Samples processed by UAV $k$ in each successful round |
| UAV position | $\mathbf u_k$ | continuous spatial coordinate | Hovering position relative to sensing target and server |
| Uplink bandwidth | $B_k$ | continuous, nonnegative | Bandwidth assigned to UAV $k$ |
| Round latency bound | $T_{\max}$ | continuous, positive | Maximum expected latency among participating UAVs |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| 23a-23b | The loss bound satisfies $\Phi\leq\epsilon$ and expected per-round latency does not exceed $T_{\max}$ |
| 23c-23d | UAVs have equal sensing-success probability and meet the minimum sensing-elevation angle $\theta_0$ |
| 23e | Pairwise UAV separation is at least $d_{\min}$ |
| 23f-23g | Batch sizes are positive integers and $\sum_k B_k=B_c$ |
| 23h | Hovering energy obeys $N T_{\max}P_{hov}\leq E_0$ |

**Algorithm**: BBPO searches over feasible $N$ and alternates three subproblems: convex bandwidth allocation, Newton-based batch-size optimization, and closed-form or low-dimensional position optimization. The cycle stops when relative latency improvement is below tolerance and returns the round count with minimum $N T_{\max}$.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Tang et al. [x] investigated integrated sensing, computation, and communication for UAV-assisted federated edge learning. They derived a training-loss upper bound that links successful sensing probability and batch size to FEEL convergence and used sensing elevation angle to impose a data-quality threshold. Their mixed-integer nonconvex formulation minimizes total training time by jointly selecting training rounds, UAV positions, batch sizes, and bandwidth allocations under accuracy, latency, separation, bandwidth, and energy constraints. The proposed BBPO method alternates bandwidth, batch-size, and position subproblems for each candidate round count. Simulations report faster convergence and higher testing accuracy than fixed-position, equal-bandwidth, and equal-batch-size baselines, with performance close to an ideal always-successful sensing case.

## Problem framing

UAV-mounted devices are great for FEEL data collection (flexible, mobile), but onboard sensing, computation, and communication compete for resources, and UAV position affects both sensing and communication. Joint deployment + resource design is needed to optimize training performance.

## System model / analysis

- **Sensing.** A threshold on the sensing **elevation angle** yields satisfactory data-sample quality.
- **Convergence.** An upper bound on UAV-assisted FEEL training loss as a function of successful sensing probability; uniform successful-sensing probability across UAVs reduces the harm of data heterogeneity.
- **Objective.** Minimize total training time by jointly optimizing UAV deployment and ISCC resources — a mixed-integer non-convex problem.

## Method

- Apply **alternating optimization** to decompose the mixed-integer non-convex problem into three sub-problems and propose **BBPO** (alternately optimize **b**andwidth, **b**atch size, and **p**osition) for efficient suboptimal solutions ([[alternating-optimization-sdr-sca]]).

## Key findings

- Simulations show BBPO outperforms baselines in convergence rate and testing accuracy (qualitative; specific curves in the paper).

## Limitations / future work

Simulation-based; sensing modeled for human motion recognition. The parse does not enumerate further limitations beyond the modeled assumptions.

## Relation to the corpus

Introduces **integrated sensing-computation-communication (ISCC)** as a named concept and ties the ISAC and federated-learning threads together: it shares FEEL/federation with [[zhai-2023-fedleo-decentralized-fl]] and [[han-2024-sagin-fl-handover]], and the sensing-aware UAV-deployment angle with the ISAC overview [[meng-2024-uav-isac-overview]]. Methodologically it joins the alternating-optimization family ([[wang-2025-double-edge-samin]], [[benaya-2025-aerial-isac-haps]]). Reinforces [[integrated-sensing-and-communication]] and [[federated-learning]].

[[aerial-federated-aggregation-design-space]] treats successful sensing as an upstream participation condition: the FEEL loss bound depends on sensing probability, while deployment, bandwidth, and batch size control total training time.

## Raw artifacts

- `raw/sources/Integrated_Sensing_Computation_and_Communication_for_UAV-Assisted_Federated_Edge_Learning/Integrated_Sensing_Computation_and_Communication_for_UAV-Assisted_Federated_Edge_Learning.md`
- Original PDF and extracted figures in the corresponding raw folders.
