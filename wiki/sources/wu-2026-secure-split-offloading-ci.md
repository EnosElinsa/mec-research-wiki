---
type: source
modeling_card: required
title: "Secure Split Offloading and Trajectory Design for UAV-Assisted Multi-Exit Collaborative DNN Inference"
authors: ["Mengru Wu", "Haonan Wu", "Weidang Lu", "Zhaolong Ning", "Lei Guo", "Abbas Jamalipour"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3708394"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, collaborative-inference, multi-exit-dnn, physical-layer-security, cooperative-jamming, uav-trajectory-control, whale-optimization]
related:
  - "[[collaborative-dl-inference]]"
  - "[[multi-exit-dnn]]"
  - "[[dnn-model-partition]]"
  - "[[physical-layer-security]]"
  - "[[friendly-jamming-uav]]"
  - "[[whale-optimization-algorithm]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[uav-trajectory-control]]"
  - "[[zhaolong-ning]]"
  - "[[lei-guo]]"
created: 2026-07-07
updated: 2026-07-16
---

# Secure Split Offloading and Trajectory Design for UAV-Assisted Multi-Exit Collaborative DNN Inference

## Citation

Wu, M., Wu, H., Lu, W., Ning, Z., Guo, L., & Jamalipour, A. (2026). *Secure Split Offloading and Trajectory Design for UAV-Assisted Multi-Exit Collaborative DNN Inference*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2026.3708394. DOI/venue/year are parse-silent at the top level and verified against a title-matched Crossref/IEEE DOI record.

## TL;DR

Combines [[collaborative-dl-inference]], [[multi-exit-dnn]] early exits, and a friendly-jamming UAV. Devices run initial DNN layers, upload intermediate feature data to a UAV server, and a second UAV sends artificial noise against an eavesdropper. The optimization jointly chooses dual-UAV trajectories, early-exit points, DNN partition points, and UAV compute allocation to balance energy, inference accuracy, delay, and secure split-offloading rate.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Wireless devices execute initial layers of a multi-exit DNN and securely upload intermediate features to a UAV inference server, while a second UAV sends artificial noise toward an uncertain-location eavesdropper. Both UAVs move at fixed altitude over discrete slots.

**Problem & objective**: A robust mixed discrete-continuous problem minimizes energy while rewarding inference accuracy, $\min E_{\mathrm{dev}}+E_{\mathrm{UAV}}-\lambda_A A_{\mathrm{inf}}$, over dual trajectories, early exits, split points, and UAV compute allocation.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Inference-UAV trajectory | $\mathbf q_S(t)$ | continuous position | UAV server path |
| Jammer-UAV trajectory | $\mathbf q_J(t)$ | continuous position | Friendly jammer path |
| Early-exit choice | $e_k$ | integer/categorical | DNN exit used for device $k$ |
| DNN partition point | $l_k$ | integer layer index | Last locally executed layer |
| UAV compute allocation | $f_k(t)$ | continuous, nonnegative | Server CPU resource for device $k$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | End-to-end inference delay remains below each task deadline |
| C2 | Worst-case secure split-offloading rate exceeds its threshold |
| C3 | Selected exit achieves the minimum inference accuracy |
| C4 | UAV compute allocations do not exceed server capacity |
| C5 | Both UAVs obey speed, endpoint, region, separation, and energy limits |

**Algorithm**: Derive closed-form compute allocation from KKT conditions → fix discrete inference decisions and update the server-UAV trajectory by SCA → update the jammer-UAV trajectory by SCA → map whale-optimization updates to valid early-exit and partition choices → alternate all blocks to convergence.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Wu et al. [x] studied secure split offloading and trajectory design for UAV-assisted multi-exit collaborative DNN inference. Devices execute initial layers locally, upload intermediate features to a UAV server, and receive protection from a friendly-jamming UAV. The formulation jointly selects both UAV trajectories, early exits, DNN partition points, and UAV computing resources under delay, secure-rate, accuracy, computation, mobility, and collision constraints. A KKT step allocates compute, SCA updates the two trajectories, and discrete whale optimization selects exit and partition decisions inside an alternating loop. Simulations report a better energy-accuracy objective than the evaluated fixed-trajectory, no-early-exit, one-shot, and independently alternating baselines.

## Problem

UAV-assisted collaborative inference reduces raw-data upload but exposes intermediate feature data over vulnerable ground-to-air links. UAV servers also have limited compute and energy, so always choosing the deepest DNN exit can violate energy or delay constraints. The paper therefore treats inference depth, split point, secure transmission, and UAV mobility as one coupled problem.

## System model

The system has multiple wireless devices, one UAV inference server, one UAV jammer, and one eavesdropper over discrete slots. Each device processes the first part of a DNN locally and uploads intermediate feature data to the UAV server for the remaining layers. A multi-exit ResNet-18 trained on CIFAR-10 provides four exit paths with depths 6, 10, 14, and 18 layers and reported accuracies 77.4%, 84.3%, 87.5%, and 88.3%. Both UAVs fly at fixed altitude with speed and collision constraints in an 800 m by 800 m area.

## Method

The objective minimizes total device/UAV energy while maximizing inference accuracy, subject to inference-delay, secure-offloading-rate, accuracy, mobility, collision, and UAV-compute constraints. The paper derives a closed-form compute-allocation solution via KKT conditions, then alternates among UAV-server trajectory optimization, UAV-jammer trajectory optimization, and discrete early-exit/partition selection. The trajectory subproblems use Taylor expansion and SCA, while a discrete whale optimization algorithm maps continuous WOA-style updates into valid early-exit and partition decisions.

## Key findings

- The SCA, DWOA, and full alternating-optimization loops converge within a limited number of iterations across the parsed simulation scenarios.
- Increasing the inference-accuracy weight improves average accuracy when the accuracy threshold is low; at a high threshold the selected exits are already constrained to high-accuracy options.
- Jamming power has a non-monotonic security effect: secure split-offloading rate first increases as eavesdropping is suppressed, then decreases when excessive jamming interferes with the legitimate link.
- The proposed scheme outperforms fixed-trajectory, no-early-exit, one-shot iteration, and independent-alternating baselines in the energy/accuracy objective across bandwidth, device-computing, and transmit-power sweeps.
- Fixed dual trajectories reduce the secure offloading rate; removing early exits keeps a similar secure rate but raises the inference energy/accuracy cost.
- Under eavesdropper-location errors from 10 m to 50 m, the proposed scheme degrades less than the fixed-dual-trajectory baseline.

## Limitations / future work

The paper concludes with heterogeneous inference tasks as a future direction, specifically DNN deployment and secure split offloading in UAV-assisted collaborative inference. Hardware validation is not in parse.

## Relation to the corpus

This source extends [[zhai-2026-collaborative-inference-uav-mec]] from ordinary UAV split inference to secure split inference with a dedicated jamming UAV and [[multi-exit-dnn]] control. It also links the distributed-inference track to [[physical-layer-security]], [[friendly-jamming-uav]], and [[whale-optimization-algorithm]].

## Raw artifacts

- `raw/sources/Secure Split Offloading and Trajectory Design for UAV-Assisted Multi-Exit Collaborative DNN Inference/Secure Split Offloading and Trajectory Design for UAV-Assisted Multi-Exit Collaborative DNN Inference.md`
- Original PDF and extracted figures (`images/`) in the same folder.
