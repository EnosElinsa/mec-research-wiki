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
updated: 2026-11-03
---

# Secure Split Offloading and Trajectory Design for UAV-Assisted Multi-Exit Collaborative DNN Inference

## Citation

Wu, M., Wu, H., Lu, W., Ning, Z., Guo, L., & Jamalipour, A. (2026). *Secure Split Offloading and Trajectory Design for UAV-Assisted Multi-Exit Collaborative DNN Inference*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2026.3708394. DOI/venue/year are parse-silent at the top level and verified against a title-matched Crossref/IEEE DOI record.

## TL;DR

Combines [[collaborative-dl-inference]], [[multi-exit-dnn]] early exits, and a friendly-jamming UAV. Devices run initial DNN layers, upload intermediate feature data to a UAV server, and a second UAV sends artificial noise against an eavesdropper. The optimization jointly chooses dual-UAV trajectories, early-exit points, DNN partition points, and UAV compute allocation to balance energy, inference accuracy, delay, and secure split-offloading rate.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: $K$ wireless devices run the first layers of a multi-exit DNN and upload intermediate features to an inference UAV server, while a second UAV sends cooperative jamming toward an eavesdropper whose location is known only within radius $\chi$ of an estimate $\tilde{\mathbf q}_E$. Both UAVs fly at fixed altitude $H$ over $N$ slots of length $\tau$ and return to their start points.

**Problem & objective**: Problem $\mathcal P_0$ (26a) minimizes $\sum_{n=1}^{N}\big(E_I[n]+E_J[n]+\sum_kE_k[n]-\sum_k\omega_\Gamma\Gamma(s_k[n])\big)$, the UAV and device energy minus a weighted inference-accuracy reward, over $\mathbf Q_I,\mathbf Q_J,\mathbf S,\mathbf M,\mathbf F$.

**Decision variables**:
| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Server-UAV trajectory | $\mathbf Q_I=\{\mathbf q_I[n]\}$ | continuous, fixed altitude | Inference UAV path |
| Jammer-UAV trajectory | $\mathbf Q_J=\{\mathbf q_J[n]\}$ | continuous, fixed altitude | Cooperative-jamming UAV path |
| Early-exit selection | $s_k[n]$ | integer, $\{0,1,\dots,M\}$ | Exit branch used by device $k$ |
| DNN partition point | $m_k[n]$ | integer, $\{0,1,\dots,M_{s_k[n]}\}$ | Split layer within the chosen exit branch |
| UAV computing allocation | $f_k^{\mathrm{UAV}}[n]$ | continuous, $\ge0$ | Server CPU resource for device $k$ |

**Constraints**:
| ID | Meaning and key expression |
|---|---|
| (26b) | Total inference delay, $T_k^{\mathrm{total}}[n]\le\tau$ |
| (26c) | Secure split-offloading rate, $R_{k,I}^{\mathrm{sec}}[n]\ge R_{\min}$ |
| (26d) | Exit accuracy, $\Gamma(s_k[n])\ge\mu_{\min}$ |
| (26e), (26f) | $\lVert\mathbf q_U[n+1]-\mathbf q_U[n]\rVert\le\tau V_{\max}$ and $\mathbf q_U[1]=\mathbf q_U[N]=\mathbf q_U^0$ for $U\in\{I,J\}$ |
| (26g) | UAV separation, $\lVert\mathbf q_I[n]-\mathbf q_J[n]\rVert\ge d_{\min}$ |
| (26h), (26k) | $\sum_kf_k^{\mathrm{UAV}}[n]\le f_{\max}$ and $f_k^{\mathrm{UAV}}[n]\ge0$ |
| (26i), (26j) | Integer ranges of $s_k[n]$ and $m_k[n]$ |

**Algorithm**: First derive the optimal computing allocation in closed form and substitute it, giving problem (28). Then alternate three subproblems: SCA for the server-UAV trajectory ($\mathcal P_1$), SCA for the jammer-UAV trajectory ($\mathcal P_2$) using the worst-case eavesdropper distance, and a discrete whale optimization algorithm (DWOA) for early-exit selection and DNN partitioning. Repeat until the objective converges.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Wu et al. [x] studied secure split offloading and trajectory design for UAV-assisted multi-exit collaborative DNN inference. Devices execute initial layers locally, upload intermediate features to a UAV server, and receive protection from a friendly-jamming UAV. The formulation jointly selects both UAV trajectories, early exits, DNN partition points, and UAV computing resources under delay, secure-rate, accuracy, computation, mobility, and collision constraints. A closed-form step allocates compute, SCA updates the two trajectories, and a discrete whale optimization algorithm selects exit and partition decisions inside an alternating loop. Ablations against fixed circular trajectories, no early exit, and no cooperative jamming show the value of each component, and the scheme gave a better energy-accuracy objective than iterative alternating resource allocation (IAO) and on-server inference (OSI) across device computing capacities and bandwidths.

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

- `raw/sources/Secure_Split_Offloading_and_Trajectory_Design_for_UAV-Assisted_Multi-Exit_Collaborative_DNN_Inference/Secure_Split_Offloading_and_Trajectory_Design_for_UAV-Assisted_Multi-Exit_Collaborative_DNN_Inference.md`
- Original PDF and extracted figures (`images/`) in the same folder.
