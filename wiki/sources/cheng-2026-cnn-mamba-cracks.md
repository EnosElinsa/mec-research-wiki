---
type: source
title: "Hybrid CNN-Mamba Network and Air-Ground Platform for Pavement Crack Evaluation"
authors: ["Longqi Cheng", "Decheng Wu", "Yuanyuan Li", "Peng Wang", "Rui Li", "Xinglong Gong", "Hailin Cao", "Xiaoheng Tan"]
year: 2026
url: "https://doi.org/10.1109/TITS.2026.3673474"
venue: "IEEE Transactions on Intelligent Transportation Systems (IEEE T-ITS)"
tags: [source, pavement-crack, cnn-mamba, edge-inference, image-segmentation, wavelet, uav-inspection, intelligent-transportation]
related:
  - "[[wavelet-guided-mamba-crack-segmentation]]"
  - "[[edge-intelligence]]"
  - "[[uav-enabled-its]]"
  - "[[uav-assisted-edge-inference]]"
  - "[[pytorch]]"
created: 2026-07-13
updated: 2026-07-13
---

# Hybrid CNN-Mamba Network and Air-Ground Platform for Pavement Crack Evaluation

## Citation

Cheng, L., Wu, D., Li, Y., Wang, P., Li, R., Gong, X., Cao, H., & Tan, X. (2026). *Hybrid CNN-Mamba Network and Air-Ground Platform for Pavement Crack Evaluation*. **IEEE Transactions on Intelligent Transportation Systems**, 27(7), 7756-7773. DOI: 10.1109/TITS.2026.3673474.

*Metadata note:* The local parse does not expose the final article record; an exact-title Crossref DOI record supplies the DOI, 2026 issue year, volume, issue, and pages above.

## TL;DR

Combines a lightweight dual-convolution encoder, contextual skeleton/detail propagation, and a wavelet-guided Mamba decoder for crack segmentation. An ONNX/Triton scan implementation runs at 35.63 FPS on Jetson AGX Orin, after which heuristic morphology and grid metrics estimate pavement risk.

## Problem framing

Thin pavement cracks occupy few pixels and are easily confused with markings, shadows, stains, and texture. CNNs preserve local edges but may lose global skeleton continuity; Transformers add global context at quadratic cost. The paper uses CNNs for local detail and a state-space decoder for longer-range structure under edge-device limits.

## System model

- UAVs and inspection vehicles are proposed as image-acquisition platforms, and the paper separately motivates edge inference; it does not specify or test the model's placement on those platforms.
- All benchmark images are resized to `320 x 320`; multi-scale masks supervise binary crack/background segmentation.
- A medial-skeleton stage derives length, area, width, and orientation from predicted masks.
- Grid porosity and crack occupancy form a heuristic crack-risk index; `CRI > 0.5` defines a high-risk grid.
- The claimed air-ground acquisition pipeline is not instantiated in the quantitative experiments, which use public datasets.

## Method

[[wavelet-guided-mamba-crack-segmentation|WTCMamba]] uses dual `3 x 3`/`5 x 5` depthwise convolution branches. Contextual spatial feature propagation sends skeleton structure bottom-up and shallow detail top-down. Each decoder stage applies Haar wavelets, CVSS/SS2D state-space processing, efficient channel attention, and progressive depthwise/dilated fusion.

Training combines Dice, BCE, PPA, and multi-scale losses. For edge deployment, LMC-Belloch replaces the Mamba scan with dimension optimization, Triton kernels, and operator fusion before ONNX execution.

## Key findings

- WTCMamba reports 2.31 M parameters, 1.67 G FLOPs, and 191.49 FPS on an RTX 4080S; several comparison models are faster, so the supported claim is an accuracy/complexity balance rather than top speed.
- Reported mIoU is `79.85%` on CFD, `81.48%` on Crack500, `74.65%` on CrackTree200, and `89.22%` on DeepCrack.
- On Jetson AGX Orin, LMC-Belloch reports `0.02%` nMAE, `35.63 FPS`, and `0.68 GB`, versus `1.45 FPS` for the fidelity-preserving PyTorch loop.
- Table exceptions prevent a universal best-on-every-metric claim; SegFormer and TransUNet lead selected accuracy or mIoU entries.

## Limitations / parse caveats

No real UAV/vehicle imagery, acquisition protocol, field risk validation, code, split manifest, seed, run variance, or timing protocol is supplied. Dataset patching may risk source-image leakage because split grouping is unspecified. The risk thresholds and physical grid calibration are empirical, and the scenario fixes a 32-by-32 grid rather than demonstrating the adaptive equation. The mIoU formula, Mamba encoder/decoder wording, citations, ablation checkmarks, and several equations are inconsistent or parse-damaged.

## Relation to the corpus

This source extends [[edge-intelligence]] and [[uav-assisted-edge-inference]] toward transport-infrastructure inspection. Unlike inference-offloading sources, it benchmarks the perception operator on a Jetson edge processor and does not optimize wireless, compute placement, or task offloading; the proposed UAV/vehicle platform is not quantitatively tested.

## Raw artifacts

- Parse: `raw/sources/Hybrid_CNN-Mamba_Network_and_Air-Ground_Platform_for_Pavement_Crack_Evaluation/Hybrid_CNN-Mamba_Network_and_Air-Ground_Platform_for_Pavement_Crack_Evaluation.md`
- Origin PDF: `raw/sources/Hybrid_CNN-Mamba_Network_and_Air-Ground_Platform_for_Pavement_Crack_Evaluation/Hybrid_CNN-Mamba_Network_and_Air-Ground_Platform_for_Pavement_Crack_Evaluation.pdf`
- Figures: `raw/sources/Hybrid_CNN-Mamba_Network_and_Air-Ground_Platform_for_Pavement_Crack_Evaluation/images/`
