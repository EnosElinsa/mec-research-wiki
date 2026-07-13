---
type: source
title: "Seizing Critical Learning Period in UAV-Assisted Hierarchical Personalized Federated Learning"
authors: ["Yanlu Li", "Yiming Liu", "Yuzhen Huang", "Zhi Zhang"]
year: 2026
url: "https://doi.org/10.1109/TMC.2025.3639671"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, uav-networks, hierarchical-federated-learning, personalized-federated-learning, critical-learning-period, data-drift, soft-actor-critic, energy-efficiency]
related:
  - "[[critical-learning-period]]"
  - "[[federated-kl-divergence-norm]]"
  - "[[federated-drift-norm]]"
  - "[[federated-learning]]"
  - "[[soft-actor-critic]]"
  - "[[rotary-wing-propulsion-energy-model]]"
  - "[[air-to-ground-channel-model]]"
  - "[[uav-trajectory-control]]"
created: 2026-07-14
updated: 2026-07-14
---

# Seizing Critical Learning Period in UAV-Assisted Hierarchical Personalized Federated Learning

## Citation

Li, Y., Liu, Y., Huang, Y., & Zhang, Z. (2026). *Seizing Critical Learning Period in UAV-Assisted Hierarchical Personalized Federated Learning*. **IEEE Transactions on Mobile Computing**, 25(5), 6740-6754. DOI: 10.1109/TMC.2025.3639671.

## TL;DR

Builds a UAV-assisted hierarchical personalized [[federated-learning]] framework that spends more participation and revisit resources during consequential training stages. It detects those [[critical-learning-period|critical learning periods]] from local-global parameter divergence or temporal data drift, then uses [[soft-actor-critic]] to coordinate active UAVs, cluster visits, UAV positions, and local/edge/global aggregation periods under energy and training constraints.

## Problem framing

Treating every FL round as equally valuable can waste UAV flight, communication, and training resources after the model's most sensitive stages, while insufficient participation during early or distribution-shifted stages can leave lasting model damage. Non-IID and time-varying device data also require personalization and repeated cluster observation. The paper therefore detects high-impact learning periods online and adapts device participation, UAV revisit behavior, and aggregation timing around them.

## System model

- A central server coordinates multiple UAVs serving geographically distributed device clusters. Devices train locally, UAVs perform edge aggregation, and the server performs global aggregation. Every UAV is assumed to connect directly to the server, and every device can upload parameters to a nearby UAV.
- Devices share a neural-network architecture but maintain different parameters under non-IID data. Local SGD feeds averaging at UAVs and then at the server.
- Personalized learning uses the server distribution as a Bayesian prior. Each device balances expected negative log-likelihood against a weighted KL divergence between its local parameter distribution and the global distribution.
- Device-UAV and UAV-server links use LoS/NLoS expected channel gains and OFDMA. The energy model covers device computation and upload plus UAV edge computation, upload, and [[rotary-wing-propulsion-energy-model|rotary-wing propulsion]], although the final optimization omits communication energy because flight energy is assumed dominant.

## Method

Two detectors identify [[critical-learning-period|critical learning periods]]:

- [[federated-kl-divergence-norm]] models neural-network parameters with mean-field Gaussian distributions and sums selected devices' local-to-global Gaussian KL divergences. A sufficiently large relative increase marks a CLP. The prose calls this a weighted average, but the displayed equation is an unweighted sum.
- [[federated-drift-norm]] uses bounded temporal gradient variation and a Taylor approximation of one-step loss change to estimate drift from sample-size-weighted device loss changes. A sufficiently large relative increase marks a CLP, and clusters with greater estimated drift are revisited more frequently.

The optimization minimizes a weighted average of UAV flight energy and a gradient-staleness proxy over training sequences. It is cast as an MDP whose state includes active UAVs, UAV coordinates and energy, recent cluster drift, and aggregation-period variables. Actions choose the next active UAV set, positions, and sequence/local/global periods. The solver is SAC with one actor, twin critics and target critics, replay, entropy regularization, automatic temperature adjustment, and soft target updates.

The abstract and introduction also claim participant-device selection and UAV visit-frequency optimization, but the printed optimization variables and SAC action do not expose an explicit device-selection variable. The formulation should therefore not be read as a complete mathematical account of every claimed policy decision.

## Key findings

- Simulations use five UAVs, 100 devices, and ten clusters with non-IID MNIST and CIFAR-10 data; CIFAR-100 also appears in one result figure although its split and model setup are not specified in the experimental-setting prose.
- FKN and FDN thresholds of 0.01 are selected from 0.001, 0.01, and 0.1. Lower thresholds detect more periods but increase training/resource use, while higher thresholds risk missing consequential divergence or drift.
- UAV visits are most frequent during epochs 0-200, consistent with concentrating resources in early sensitive training stages.
- The full CLP-aware design reports 54% lower communication overhead than the No-CLP ablation while maintaining comparable or better accuracy. This overhead is an operation-count measure covering communication rounds, uploads/downloads, and on-device training steps; it is not a 54% flight-energy reduction.
- The proposed design reports the best final accuracy against CriticalFL, pFedBayes, FedExp, and FedAvg in the displayed CIFAR-10, MNIST, and CIFAR-100 comparisons. Exact final accuracies are not stated in the prose.
- The reported energy comparison favors the proposed design, especially through fewer visits after CLP and to low-drift clusters, but gives no exact energy values or percentage reduction.
- Under random bit flips on CIFAR-10 over AWGN, BER 0.05 and 0.1 are described as nearly ideal, while BER 0.2 causes noticeable degradation; no exact accuracy loss is stated.

## Limitations

All evidence is simulation-based. The model assumes direct UAV-server connectivity, nearby device-UAV reachability, homogeneous architectures, mean-field Gaussian parameter distributions, bounded and slowly varying gradient drift, and OFDMA. The objective uses flight energy plus a drift/staleness surrogate rather than optimizing accuracy directly, and omits communication energy despite deriving it. Privacy leakage, stragglers, poisoning, adversarial clients, secure aggregation, and realistic packet failures are not addressed. The paper defers real UAV/IoT prototyping, extreme non-IID and highly dynamic settings, lightweight deployment, and poisoning/interference resilience.

Several displayed expressions are internally inconsistent: energy consumption and residual battery are conflated in constraints; the printed battery-penalty event conflicts with its prose explanation; and the target-network update omits the online critic term expected in a Polyak update. The referenced online appendices containing convergence and KL details are not included in the local parse/PDF body.

## Relation to the corpus

This source connects [[federated-learning]] resource management to [[critical-learning-period]] detection rather than treating all rounds uniformly. [[federated-kl-divergence-norm]] targets local-global parameter separation, while [[federated-drift-norm]] targets temporal distribution shift; together they drive UAV participation and revisit intensity. Its use of [[uav-trajectory-control]] is scheduling-oriented: SAC selects active UAVs and positions across training sequences, rather than continuously optimizing radio trajectories or transmit power.

## Raw artifacts

- Parse: `raw/sources/Seizing_Critical_Learning_Period_in_UAV-Assisted_Hierarchical_Personalized_Federated_Learning/Seizing_Critical_Learning_Period_in_UAV-Assisted_Hierarchical_Personalized_Federated_Learning.md`
- Origin PDF: `raw/sources/Seizing_Critical_Learning_Period_in_UAV-Assisted_Hierarchical_Personalized_Federated_Learning/Seizing_Critical_Learning_Period_in_UAV-Assisted_Hierarchical_Personalized_Federated_Learning.pdf`
- Figures: `raw/sources/Seizing_Critical_Learning_Period_in_UAV-Assisted_Hierarchical_Personalized_Federated_Learning/images/`
