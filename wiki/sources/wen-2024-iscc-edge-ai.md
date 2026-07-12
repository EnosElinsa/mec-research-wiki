---
type: source
title: "Task-Oriented Sensing, Computation, and Communication Integration for Multi-Device Edge AI"
authors: ["Dingzhu Wen", "Peixi Liu", "Guangxu Zhu", "Yuanming Shi", "Jie Xu", "Yonina C. Eldar", "Shuguang Cui"]
year: 2024
url: "https://doi.org/10.1109/TWC.2023.3303232"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, integrated-sensing-computation-communication, integrated-sensing-and-communication, task-oriented-communication, discriminant-gain, sum-of-ratios-optimization, edge-ai, split-inference]
related:
  - "[[integrated-sensing-computation-communication]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[task-oriented-communication]]"
  - "[[discriminant-gain]]"
  - "[[sum-of-ratios-optimization]]"
  - "[[dnn-model-partition]]"
  - "[[over-the-air-computation]]"
  - "[[mobile-edge-computing]]"
  - "[[tang-2024-iscc-uav-feel]]"
  - "[[isac-sensing-in-aerial-mec]]"
  - "[[jie-xu]]"
  - "[[yuanming-shi]]"
created: 2026-06-02
updated: 2026-07-13
---

# Task-Oriented Sensing, Computation, and Communication Integration for Multi-Device Edge AI

## Citation

Wen, D., Liu, P., Zhu, G., Shi, Y., Xu, J., Eldar, Y. C., & Cui, S. (2024). *Task-Oriented Sensing, Computation, and Communication Integration for Multi-Device Edge AI*. **IEEE Transactions on Wireless Communications**, 23(3), 2486–2502. DOI: 10.1109/TWC.2023.3303232. (Manuscript received 20 April 2023; accepted 24 July 2023; date of publication 14 August 2023; date of current version 12 March 2024.)

## TL;DR

Designs a **multi-device edge-AI inference system** that jointly exploits **AI model split inference** and **integrated sensing and communication (ISAC)**. Multiple single-antenna ISAC devices, each with a dual-functional radar-communication (DFRC) transceiver, perform radar sensing to obtain **multi-view** data, extract and quantize features locally, then offload the quantized features over wireless links to a single edge server that runs the remaining inference on the **cascaded feature vector**. The system targets **inference accuracy** (not throughput) under a latency constraint, measured by a tractable surrogate metric — **discriminant gain** (KL-divergence-derived class separability in normalized feature space). The resulting non-convex **integrated sensing, computation, and communication (ISCC)** resource-management problem is shown to be **optimally solvable by the sum-of-ratios method**, jointly allocating per-device sensing/transmit power, communication time, and quantization-bit allocation.

## Problem framing

Edge inference can be run on-device (storage/compute heavy, needs light/compressed models), on-server (privacy leakage from raw-data upload), or via **split inference** (model split into a device-side feature extractor — e.g. PCA / convolutional layers — and a server-side classifier), which preserves privacy and offloads heavy compute. Existing split-inference designs optimize only device computation *or* communication overhead. But the split-inference workflow has **three coupled processes** — data acquisition (sensing), feature extraction + quantization (computation), and feature transmission (communication) — and sensing and communication compete for the same radio resources, while the communication budget dictates the feasible quantization (distortion) level. The paper argues these must be designed jointly under a **task-oriented** principle whose performance metric is inference accuracy + latency, and notes prior task-oriented ISAC works addressed only the *training* phase and ignored computation. It claims to be the first task-oriented ISCC design for edge AI *inference*.

## System model

- **Network.** One mobile edge server with a single-antenna access point (AP) coordinating `K` single-antenna ISAC devices with DFRC transceivers; TDMA. The total latency budget for the real-time task is `T`, split per device into sensing time `T_{r,k}`, computation time `T_{m,k}` (both constant), and communication time `T_{c,k}`; total bandwidth `B`; static wireless channels (duration shorter than coherence time); global CSI at the AP.
- **Multi-view sensing.** A single ISAC device sees only a narrow view, insufficient for the task, so multiple devices sense non-overlapping areas → independent feature subsets. Sensing uses FMCW up-ramp chirps; the radar echo is processed (sampling → SVD-based clutter filtering → PCA feature extraction in the slow-time dimension). The sensed feature is polluted by Gaussian **clutter** and **sensing noise** scaled by the radar sensing power `P_{r,k}`.
- **Quantization.** Each feature element is linearly quantized with Gaussian **quantization distortion** (variance shrinks with higher quantization gain), recovered at the server.
- **Accuracy metric.** Per class-pair **discriminant gain** is derived from the KL divergence (distance between two class centroids under normalized covariance); the overall discriminant gain averages over all class pairs and sums over the independent feature elements. Larger discriminant gain → higher inference accuracy.
- **Objective.** Maximize the overall discriminant gain subject to the total-latency constraint, the per-device communication-rate (quantization-bits-vs-capacity) constraint, and a per-device energy budget — an NP-hard non-convex problem coupling sensing power, transmit power, communication time, and quantization bits, with device heterogeneity in channel gain, quantization level, and feature importance.

## Method

- **Equivalent reformulation.** Through variable transformations the discriminant-gain objective is recast as a **sum of multiple quasi-linear ratios** subject to a convex feasible region (the latency, rate, and energy constraints are each shown convex).
- **Sum-of-ratios optimal solution.** The reformulated problem is solved **optimally and iteratively** by the [[sum-of-ratios-optimization|sum-of-ratios]] method: each iteration solves a convex subproblem minimizing the sum of weighted sensing + quantization distortion under given class-pair discriminant gains, then updates the discriminant gains using the solved distortion levels.
- **Output.** The optimal ISCC scheme jointly sets each device's transmit power and time allocation for sensing and communication, plus its quantization-bit allocation for computation-distortion control.

## Key findings

- Inference accuracy **increases with discriminant gain** for both an SVM and an MLP classifier, validating discriminant gain as an accuracy surrogate. At large discriminant gain (small distortion) the SVM beats the MLP (the MLP is more sensitive to small distortion); at small discriminant gain (large distortion) the MLP is more robust. At very large discriminant gain the accuracy gain saturates.
- The proposed **optimal ISCC scheme outperforms** benchmark schemes that design sensing, quantization, and communication separately or only partially, for both SVM and MLP models, across energy-threshold and permitted-latency sweeps.
- **More ISAC devices → higher accuracy** (more views enlarge the feature space and class separation). Specific numeric margins are figure-derived (Figs. 6–10 over a high-fidelity wireless-sensing simulator with a multi-view human-motion-recognition task); treat exact values as indicative.

## Limitations / future work

Evaluation is **simulation-only** (a high-fidelity wireless-sensing simulator, human-motion recognition). The model assumes **static channels** within `T`, **constant** per-device sensing and computation time, **single-antenna** devices and AP, **TDMA**, and **independent non-overlapping** feature subsets. The authors name two future directions: **ISAC device scheduling / feature selection** when radio resources (time, frequency) are scarce, and extending to **broadband frequency-selective** channels.

## Relation to the corpus

The corpus's second [[integrated-sensing-computation-communication|ISCC]] entry and its **inference-side** counterpart to [[tang-2024-iscc-uav-feel]], which applies ISCC to federated edge *learning* (training) on a UAV via alternating optimization. Where Tang et al. optimize deployment + sensing/compute/comm to minimize FEEL training time, this paper optimizes power/time/quantization to maximize *inference* accuracy via [[discriminant-gain]], solved exactly by [[sum-of-ratios-optimization]] rather than AO. It extends [[integrated-sensing-and-communication|ISAC]] from the corpus's communication/sensing-only designs (mapped in [[isac-sensing-in-aerial-mec]]) toward a **[[task-oriented-communication|task-oriented]]** objective, and its device-side feature extractor is an instance of [[dnn-model-partition|split inference]]. It is distinct from the over-the-air-computation ISAC integration it cites ([[over-the-air-computation]]). Co-author [[jie-xu]] (CUHK-Shenzhen) also appears on the corpus's UAV-ISAC works.

## Raw artifacts

- `raw/sources/Task-Oriented_Sensing_Computation_and_Communication_Integration_for_Multi-Device_Edge_AI/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
