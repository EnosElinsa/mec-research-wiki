---
type: concept
title: "Edge Intelligence"
tags: [mec, edge-ai, intelligent-transportation-systems]
related:
  - "[[mobile-edge-computing]]"
  - "[[vehicular-mec]]"
  - "[[uav-enabled-its]]"
  - "[[gong-2023-edge-intelligence-its-survey]]"
  - "[[xu-2024-mobile-aigc-survey]]"
  - "[[li-2026-aeroguard-uav-fault-detection]]"
  - "[[hybrid-uav-flight-data-fault-detection]]"
  - "[[li-2026-dff-slam]]"
  - "[[dynamic-feature-filtering-vslam]]"
  - "[[liao-2026-semantic-twinning-tracking]]"
  - "[[cheng-2026-cnn-mamba-cracks]]"
created: 2026-07-07
updated: 2026-07-13
---

# Edge Intelligence

Edge intelligence places AI training, inference, and decision services across the end-edge-cloud continuum instead of treating the cloud as the only intelligence layer. For MEC, the term emphasizes low-latency local inference, privacy-preserving data handling, reduced backbone load, and adaptive offloading between user devices, nearby edge nodes, and cloud resources.

In [[gong-2023-edge-intelligence-its-survey]], edge intelligence is the organizing concept for intelligent transportation systems: vehicles, cameras, traffic infrastructure, UAVs, and rail systems generate edge data, while RSUs, APs, micro data centers, and cloud centers split AI workloads according to latency, privacy, energy, and model-complexity requirements. The concept overlaps with [[vehicular-mec]], [[uav-enabled-its]], and the edge-cloud AI service framing in [[xu-2024-mobile-aigc-survey]].

[[li-2026-aeroguard-uav-fault-detection]] adds an onboard-safety instance: [[hybrid-uav-flight-data-fault-detection]] fuses LSTM and ARX predictions and runs lightweight residual tests within Raspberry Pi-class latency budgets.

[[li-2026-dff-slam]] adds onboard visual localization: [[dynamic-feature-filtering-vslam]] combines YOLOv3, optical flow, and epipolar filtering on a Jetson Xavier NX, retaining 16 FPS in the reported UAV-platform runtime test.

[[liao-2026-semantic-twinning-tracking]] places state inference, fusion, control, and incremental MARL updates on LEO satellite edge modules. [[cheng-2026-cnn-mamba-cracks]] instead emphasizes local perception deployment: its wavelet-Mamba crack segmenter is converted to ONNX/Triton and evaluated on a Jetson AGX Orin, although the proposed UAV/vehicle acquisition platform is not tested quantitatively.
