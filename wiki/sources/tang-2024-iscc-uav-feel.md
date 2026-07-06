---
type: source
title: "Integrated Sensing, Computation, and Communication for UAV-Assisted Federated Edge Learning"
authors: ["Yao Tang", "Guangxu Zhu", "Wei Xu", "Man Hon Cheung", "Tat-Ming Lok", "Shuguang Cui"]
year: 2025
url: "https://doi.org/10.1109/TWC.2024.3523381"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, isac, federated-edge-learning, uav, resource-allocation, alternating-optimization, integrated-sensing-computation-communication]
related:
  - "[[integrated-sensing-and-communication]]"
  - "[[integrated-sensing-computation-communication]]"
  - "[[federated-learning]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[uav-trajectory-control]]"
  - "[[meng-2024-uav-isac-overview]]"
  - "[[han-2024-sagin-fl-handover]]"
  - "[[zhai-2023-fedleo-decentralized-fl]]"
created: 2026-05-29
updated: 2026-07-07
---

# Integrated Sensing, Computation, and Communication for UAV-Assisted Federated Edge Learning

## Citation

Tang, Y., Zhu, G., Xu, W., Cheung, M. H., Lok, T.-M., & Cui, S. (2025). *Integrated Sensing, Computation, and Communication for UAV-Assisted Federated Edge Learning*. **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2024.3523381. (Date of publication 6 Jan 2025; date of current version 11 Apr 2025.)

## TL;DR

Jointly designs **UAV deployment + resource allocation** for **federated edge learning (FEEL)** where UAV-mounted edge devices sense data, compute, and communicate — all competing for limited onboard resources. The paper links UAV deployment to sensing quality (human motion recognition), derives a training-loss upper bound as a function of successful sensing probability, and minimizes total training time by jointly optimizing deployment and integrated sensing-computation-communication (ISCC) resources via **alternating optimization** (the BBPO scheme: bandwidth, batch size, position).

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

## Raw artifacts

- `raw/sources/Integrated Sensing- Computation- and Communication for UAV-Assisted Federated Edge Learning/Integrated Sensing- Computation- and Communication for UAV-Assisted Federated Edge Learning.md`
- `raw/sources/Integrated_Sensing_Computation_and_Communication_for_UAV-Assisted_Federated_Edge_Learning/full.md`
- Original PDF and extracted figures in the corresponding raw folders.
