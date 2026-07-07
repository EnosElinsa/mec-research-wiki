---
type: source
title: "UAV-Assisted Edge Inference With Integrated Sensing, Communication, and Computation"
authors: ["Dingzhu Wen", "Shuo Zhang", "Guangxu Zhu", "Yuan Liu", "Yuanming Shi", "Honglin Hu"]
year: 2026
url: "https://doi.org/10.1109/TWC.2026.3669999"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), vol. 25, pp. 13336-13350, 2026"
tags: [source, uav, edge-inference, iscc, task-oriented-communication, trajectory-optimization]
related:
  - "[[uav-assisted-edge-inference]]"
  - "[[integrated-sensing-computation-communication]]"
  - "[[discriminant-gain]]"
  - "[[task-oriented-communication]]"
  - "[[uav-trajectory-control]]"
  - "[[alternating-optimization-sdr-sca]]"
created: 2026-07-07
updated: 2026-07-07
---

# UAV-Assisted Edge Inference With Integrated Sensing, Communication, and Computation

## Citation

Wen, D., Zhang, S., Zhu, G., Liu, Y., Shi, Y., & Hu, H. (2026). *UAV-Assisted Edge Inference With Integrated Sensing, Communication, and Computation*. **IEEE Transactions on Wireless Communications**, 25, 13336-13350. DOI: 10.1109/TWC.2026.3669999.

## TL;DR

Studies infrastructure-free [[uav-assisted-edge-inference]] where a UAV relay visits distributed ground devices, collects local feature vectors, and forwards them to an edge server. The paper minimizes end-to-end inference delay under energy and accuracy constraints by jointly optimizing device access order, UAV hovering locations, sensing power, computation frequency, and transmission parameters.

## Problem

Distributed edge-AI devices may be too sparse or infrastructure-poor to send features directly to an edge server. The UAV must move among devices, but its trajectory, sensing quality, computation frequency, feature compression, and wireless transmission settings jointly determine delay and inference accuracy. The paper asks how to optimize this coupled [[integrated-sensing-computation-communication|ISCC]] pipeline.

## System model

The system has a single-antenna UAV, multiple single-antenna ground devices with dual-function sensing/communication capability, and a single-antenna edge server. Ground devices extract features through a lightweight ANN plus PCA, approximate feature distributions with Gaussian mixture models, and upload quantized features through the UAV relay. The UAV flies at fixed altitude, visits device-associated hovering locations, and forwards collected features for final inference at the edge server.

## Method

The paper formulates a nonconvex mixed-integer nonlinear problem. It decomposes the design into:

- a graph-theoretic minimum Hamiltonian cycle for device access sequence;
- alternating optimization for hovering locations and resource allocation;
- successive approximation for trajectory refinement;
- [[discriminant-gain]] as the downstream inference-accuracy surrogate.

The convexified resource-allocation subproblem and the trajectory-refinement step are iterated until convergence to a stationary solution.

## Key findings

- The optimized trajectory can outperform a nearest-neighbor access path by accepting a longer immediate segment that shortens the total mission.
- Optimized hovering locations need not sit directly above each device; the reported solution balances movement, channel, and inference-delay terms.
- [[discriminant-gain]] positively correlates with SVM and MLP inference accuracy in the reported human-motion experiments.
- Requiring accuracy above 90% produces sharply increasing delay in the parsed accuracy-delay tradeoff, showing diminishing returns near high-accuracy operation.
- The proposed scheme yields lower delay than hover-above, nearest-neighbor, and non-optimized-velocity baselines across bandwidth and energy-budget sweeps.
- Maximum velocity is delay-sensitive at low values and then plateaus in the reported comparison around higher speed limits.

## Limitations / future work

The paper suggests extending the model to multi-UAV cooperative trajectory/task allocation, replacing backtracking with lower-complexity heuristics for massive device sets, and adding dynamic device scheduling based on data quality and channel conditions.

## Relation to the corpus

This source extends the existing [[wen-2024-iscc-edge-ai]] task-oriented ISCC entry from multi-device direct edge inference to UAV-relayed edge inference. It keeps [[discriminant-gain]] as the accuracy bridge between sensing/quantization/transmission variables and classification performance, but adds explicit [[uav-trajectory-control]] and access-order design.

## Raw artifacts

- `raw/sources/UAV-Assisted Edge Inference With Integrated Sensing- Communication- and Computation/UAV-Assisted Edge Inference With Integrated Sensing- Communication- and Computation.md`
- Original PDF and extracted figures (`images/`) in the same folder.
