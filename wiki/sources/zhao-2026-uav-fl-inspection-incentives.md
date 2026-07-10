---
type: source
title: "An Incentive Assignment Scheme of UAV Clients for Federated Intelligent Inspection Based on Communication-Sensing-Computing Integration"
authors: ["Haitao Zhao", "Mengqi Sui", "Miao Liu", "Chun Zhu", "Hongbo Zhu"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3651590"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC), vol. 25, no. 6, pp. 9137-9151, Jun. 2026"
tags: [source, federated-learning, uav-inspection, incentive-mechanism, contract-theory, client-selection, iscc]
related:
  - "[[contract-theoretic-fl-incentives]]"
  - "[[contract-theory]]"
  - "[[federated-learning]]"
  - "[[integrated-sensing-computation-communication]]"
  - "[[air-to-ground-channel-model]]"
  - "[[guo-2026-aot-uav-inspection-offloading]]"
  - "[[jia-2026-ufsp-rail-inspection]]"
  - "[[aircomp-assisted-asynchronous-fl]]"
created: 2026-07-11
updated: 2026-07-11
---

# An Incentive Assignment Scheme of UAV Clients for Federated Intelligent Inspection Based on Communication-Sensing-Computing Integration

## Citation

Zhao, H., Sui, M., Liu, M., Zhu, C., & Zhu, H. (2026). *An Incentive Assignment Scheme of UAV Clients for Federated Intelligent Inspection Based on Communication-Sensing-Computing Integration*. **IEEE Transactions on Mobile Computing**, 25(6), 9137-9151. DOI: 10.1109/TMC.2026.3651590. DOI evidence appears in the parse and was verified against a title-matched Crossref/IEEE DOI record.

## TL;DR

Proposes Multi-Dimensional Selection (MDS) for UAV-assisted federated intelligent inspection. MDS scores UAV clients by data quality and contribution value, builds a candidate pool using [[contract-theory]] and residual-battery management, and then uses Bayesian optimization to select high-contribution UAVs for federated training incentives.

## Problem

UAV inspection clients collect heterogeneous sensing data and consume communication, sensing, and computation energy during federated training. A model owner needs enough high-quality participants for accuracy but cannot simply select every UAV because incentives, bandwidth, latency, and energy costs rise sharply. The paper therefore treats UAV client selection and incentive assignment as a communication-sensing-computing integration problem.

## System model

UAVs collect inspection data with cameras/sensors and participate in FL for a model owner. The process includes task/contract broadcast, UAV contract choice, candidate-pool construction, UAV selection, local training, model upload, and global aggregation. The cost model includes sensing energy, computation energy, communication energy over air-to-ground links, residual battery management, and incentive payments.

## Method

MDS combines data-quality and contribution-value indicators into a multidimensional client score. Contract theory handles bilateral selection and participation incentives under private UAV conditions, while residual battery management prevents selecting UAVs whose energy state makes participation impractical. Bayesian optimization then selects UAVs from the candidate pool for each FL round.

## Key findings

- On F-MNIST with balanced division, MDS and selecting all 100 clients reach similar accuracy/loss, but at 500 rounds the all-client scheme requires 149210.228 incentive versus 6886.769 for MDS, about 21.7 times higher.
- On non-IID F-MNIST, MDS improves convergence accuracy by 13.7 percentage points over IMP, 10.7 over POC, 10.7 over DivFL, and about 16.7 over RAND, while matching COR-like accuracy with lower incentive cost.
- At 150 F-MNIST rounds, MDS uses lower total incentives than RAND, IMP, POC, COR, and DivFL in Table III.
- On CIFAR, MDS improves convergence accuracy by 3.36 percentage points over POC, 4.01 over IMP, 7.34 over DivFL, and about 5.46 over RAND, while saving incentives versus all listed baselines including COR.
- On the UAV-CM-Dataset, MDS improves average accuracy over rounds 600-620 by 12.6 percentage points over RAND, 8.0 over POC, 3.4 over DivFL, and 3.6 over IMP, while saving 5.1%-8.5% incentive depending on the baseline.

## Limitations / future work

The application discussion notes communication-cost and delay challenges for wide-area UAV inspection. It proposes combining MDS with hierarchical FL, where relay nodes aggregate client updates before forwarding them to the model owner, as a future direction for large-scale heterogeneous UAV inspection networks.

## Relation to the corpus

This source links [[federated-learning]], [[contract-theory]], and [[integrated-sensing-computation-communication]] through a UAV inspection incentive mechanism. It is different from UAV inspection offloading papers such as [[guo-2026-aot-uav-inspection-offloading]] and [[jia-2026-ufsp-rail-inspection]]: here the central decision is which UAV clients should be paid to train, not where inspection tasks should execute. It also complements [[huang-2026-aircomp-uav-swarms-afl]] because both target UAV-swarm FL, but Zhao et al. focus on client motivation/selection while Huang et al. focus on wireless aggregation and staleness.

## Raw artifacts

- `raw/sources/An_Incentive_Assignment_Scheme_of_UAV_Clients_for_Federated_Intelligent_Inspection_Based_on_Communication-Sensing-Computing_Integration/An_Incentive_Assignment_Scheme_of_UAV_Clients_for_Federated_Intelligent_Inspection_Based_on_Communication-Sensing-Computing_Integration.md`
- Original PDF and extracted figures (`images/`) in the same folder.
