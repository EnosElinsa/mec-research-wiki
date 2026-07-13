---
type: source
title: "Semantic Communications for UAV Data Aggregation: A Layered Design Against Alterable Hovering Position"
authors: ["Lan Lin", "Wenjun Xu", "Yimeng Zhang", "Xin Yuan", "Jinglin Zhang", "Zhu Han", "Ping Zhang"]
year: 2026
url: "https://doi.org/10.1109/TWC.2025.3614182"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), vol. 25, pp. 4799-4815"
tags: [source, semantic-communication, uav-data-aggregation, deep-jscc, ofdm-noma, uav-positioning, image-transmission]
related:
  - "[[layered-semantic-communication]]"
  - "[[semantic-reference-signal-matching]]"
  - "[[semantic-communication]]"
  - "[[noma]]"
  - "[[uav-data-collection]]"
  - "[[air-to-ground-channel-model]]"
  - "[[zhu-han]]"
  - "[[zhang-2025-gsc-diffusion-semcom]]"
  - "[[zhang-2026-distributed-jscc-uav-video]]"
  - "[[wang-2026-diffusion-semantic-uav-edge]]"
  - "[[zhao-2025-probabilistic-semantic-sagin]]"
created: 2026-07-14
updated: 2026-07-14
---

# Semantic Communications for UAV Data Aggregation: A Layered Design Against Alterable Hovering Position

## Citation

Lin, L., Xu, W., Zhang, Y., Yuan, X., Zhang, J., Han, Z., & Zhang, P. (2026). *Semantic Communications for UAV Data Aggregation: A Layered Design Against Alterable Hovering Position*. **IEEE Transactions on Wireless Communications, 25**, 4799-4815. DOI: 10.1109/TWC.2025.3614182.

## TL;DR

Separates image-semantic feature extraction from adaptation to changing UAV-user geometry. A frozen fixed-geometry codec is paired either with fast learned channel-aware signal processors (CLAP) or with iterative power-and-hover-position optimization (AOPP); both improve PSNR over a dynamically trained end-to-end codec baseline in the reported OFDM-NOMA simulations.

## Problem

An image-semantic codec trained for one UAV-user geometry can lose reconstruction quality when the UAV hovering point, user distances, and Rician channels change. Training and storing a separate codec for every quantized geometry is impractical. The paper therefore asks whether a reusable semantic codec can remain fixed while a lighter second layer adapts semantic signals and the UAV hovering point.

## System model

- Multiple ground users upload images to one hovering UAV base station, which jointly decodes the superposed semantic features and aggregates the reconstructed data.
- The air interface uses 64-subcarrier OFDM with at most two non-orthogonal users per subcarrier group. Each user maps an image to a complex semantic-feature tensor and obeys an average transmit-power budget.
- Large-scale gain follows distance-based path loss and small-scale fading is Rician. User horizontal positions and perfect real-time CSI are assumed known to the UAV and users.
- The main design optimizes a static horizontal hovering point at fixed altitude. It does not model a flight trajectory, velocity, propulsion energy, collision avoidance, or no-fly regions.
- The semantic feature extraction codec is first trained over AWGN at fixed user and UAV positions and then frozen while the position-and-signal-processing layer adapts to changed geometry and fading.

## Method

The [[layered-semantic-communication]] design separates semantic feature extraction (SFE) from UAV Position and signal Processing Coordination (PPC). The SFE layer trains the encoders and decoder for image reconstruction and then freezes them.

CLAP places the UAV at a power-weighted user centroid. CNN-based transmit and receive semantic-signal processors condition the frozen-codec signals on channel gains. Their offline loss combines image reconstruction error with [[semantic-reference-signal-matching]], which pulls the changed-channel received signal toward the fixed-codec reference input. The reference term supplies a gradient path around the frozen codec, while the image term improves low-SNR reconstruction. Online operation is noniterative but requires dual-side CSI.

AOPP trains no PPC neural network. It alternates semantic transmit/receive scaling and UAV horizontal-position updates. At fixed position, a QCQP and closed-form amplitude update allocate semantic-signal power; at fixed scaling, auxiliary distances and SCA produce a convex position approximation. The BCD/SCA sequence converges to a stationary/local solution of the approximated problem, not a global optimum of the original joint formulation.

## Key findings

- For two users under Rician fading with `K^f=10 dB`, CLAP and AOPP improve average PSNR over the end-to-end codec baseline by `3.0 dB` and `3.1 dB`, respectively.
- Under AWGN, the corresponding two-user gains are `1.44 dB` for CLAP and `1.37 dB` for AOPP.
- At `SNR=5 dB` and `K^f=10 dB`, AOPP exceeds CLAP by `0.45`, `0.24`, and `0.09 dB` for 2, 4, and 6 users. CLAP is stronger at low SNR, while AOPP is slightly stronger at high SNR and changes more gradually with the Rician factor.
- On an Intel Core i9-13900KF and NVIDIA RTX 4090, the reported average processing time per non-orthogonal user-image group is `3.6 ms` for CLAP and `197.0 ms` for AOPP.
- The paper calculates an additional user-side CSI feedback load of `4 bits/subcarrier x 64 = 256 bits` per user.

## Limitations

Evaluation uses CIFAR-10 simulations only, without airborne tests, measured channel traces, confidence intervals, or an end-to-end latency deadline. Both schemes rely on perfect real-time CSI at users and the UAV; the reported feedback count omits estimation error, protocol timing, and delay. User grouping and subcarrier assignment are fixed, altitude is only swept, and CLAP's weighted centroid is a heuristic. AOPP offers only local/stationary convergence, and its `197 ms` online runtime is not compared with channel coherence time. Several optimization equations are OCR-damaged, so the page retains only report-verified variable and algorithm meanings.

## Relation to the corpus

This source extends [[semantic-communication]] with an explicit separation between a frozen image codec and geometry-dependent signal/position adaptation. [[zhang-2025-gsc-diffusion-semcom]] instead improves image reconstruction with a diffusion decoder. [[zhang-2026-distributed-jscc-uav-video]] couples DeepJSCC to UAV-constrained video delivery, while [[wang-2026-diffusion-semantic-uav-edge]] jointly treats trajectory and edge-resource decisions. The present paper is narrower: it adapts a static hovering point and semantic-signal processing for OFDM-[[noma|NOMA]] image aggregation.

## Raw artifacts

- Parse: `raw/sources/Semantic_Communications_for_UAV_Data_Aggregation_A_Layered_Design_Against_Alterable_Hovering_Position/Semantic_Communications_for_UAV_Data_Aggregation_A_Layered_Design_Against_Alterable_Hovering_Position.md`
- Origin PDF: `raw/sources/Semantic_Communications_for_UAV_Data_Aggregation_A_Layered_Design_Against_Alterable_Hovering_Position/Semantic_Communications_for_UAV_Data_Aggregation_A_Layered_Design_Against_Alterable_Hovering_Position.pdf`
- Figures: `raw/sources/Semantic_Communications_for_UAV_Data_Aggregation_A_Layered_Design_Against_Alterable_Hovering_Position/images/`
