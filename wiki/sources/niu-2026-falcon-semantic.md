---
type: source
title: "FALCON: A Diffusion Model-Empowered Semantic Communication Framework for Low-Altitude Wireless Networks"
authors: ["Xupeng Niu", "Weijie Yuan", "Qingqing Cheng", "Long Tan"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3709169"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, semantic-communication, multimodal, diffusion-model, low-altitude-wireless-network, jscc, task-oriented-communication]
related:
  - "[[multi-modal-semantic-communication]]"
  - "[[semantic-communication]]"
  - "[[generative-diffusion-model]]"
  - "[[task-oriented-communication]]"
  - "[[pytorch]]"
  - "[[weijie-yuan]]"
created: 2026-07-13
updated: 2026-07-13
---

# FALCON: A Diffusion Model-Empowered Semantic Communication Framework for Low-Altitude Wireless Networks

## Citation

Niu, X., Yuan, W., Cheng, Q., & Tan, L. (2026). *FALCON: A Diffusion Model-Empowered Semantic Communication Framework for Low-Altitude Wireless Networks*. **IEEE Transactions on Mobile Computing**, 1-15. DOI: 10.1109/TMC.2026.3709169.

## TL;DR

FALCON aligns visual, textual, and acoustic semantics with a KANet-based shared-prompt module, ranks tokens by self-attention, cross-modal relevance, and channel state, and reconstructs distorted JSCC signals with a range-null diffusion model. It targets task accuracy, payload/computation reduction, and low-SNR robustness in low-altitude UAV links.

## Problem framing

UAV semantic links combine heterogeneous sensing modalities with strict onboard compute, energy, and bandwidth limits. Independent modality encoders can create representation silos, uniform token transmission wastes scarce radio resources, and direct decoding is fragile under fading, interference, and Doppler-related distortion.

## System model

- UAV transmitters preprocess and encode onboard sensor data; a ground base station recovers the signal, decodes semantics, and runs task heads.
- ViT-Base-Patch16-224 and BERT-Base-uncased provide representative visual and text front ends; experiments also include audio.
- The JSCC link is evaluated under AWGN and Rayleigh fading. RNDM uses a least-squares channel-gain estimate.
- Simulations use 100 m altitude, 2 MHz bandwidth, OFDM, 16QAM, and 30 dBm maximum UAV transmit power.
- Training and latency tests run in [[pytorch|PyTorch]] on Ubuntu 22.04 with an RTX 4090; no onboard or over-the-air flight test is reported.

## Method

The Knowledge Enhancement Module maps heterogeneous features through fourth-order B-spline Kolmogorov-Arnold layers and aligns them with a shared semantic prompt. Each token receives an average score from normalized self-attention, cross-modal attention, and an SNR-derived noise feature. Sparsemax and a dynamic threshold retain salient tokens for adaptive transmission.

At the receiver, the Range-Null Diffusion Model follows a deterministic DDIM-style reverse path. It enforces clean-signal distribution consistency and observed-channel degradation consistency through range/null-space correction. A binary uncertainty gate disables pseudo-inverse correction when estimated channel error would amplify noise.

## Key findings

- On integrated CLEVR reasoning under AWGN, FALCON reports average gains of `5.08%`, `6.52%`, and `14.17%` over DeepSC-VQA, CDDM, and U-DeepSC.
- Under Rayleigh fading on CLEVR, it reports `5.98%` average improvement over DeepSC-VQA and up to `16.52%` over U-DeepSC.
- High-SNR average compute is reported `40.67%` below low-SNR compute across the two evaluated channel models.
- With 50 diffusion steps, reported per-sample latency is `6.06 ms` vision, `5.26 ms` text, and `6.13 ms` audio, or about `17.45 ms` total on the workstation.
- Removing RNDM costs `0.93%` at high SNR and `2.8%` at low SNR in the stated AWGN ablation; KANet improves fading-channel accuracy by up to `1.098%` over an MLP.

## Limitations / future work

The experiments are workstation-based and cover classification/reasoning on CLEVR, CMU-MOSEI, and FLAME rather than an airborne radio deployment. AWGN and Rayleigh models exclude measured air-ground traces, Rician fading, interference, and explicit mobility/Doppler tests. Channel-estimation sensitivity is not isolated. CDDM is adapted from a unimodal design, and FLAME prose gives no exact accuracy values. The embedded NCS2/Jetson Nano claim is theoretical; consumer UAVs may require pruning or distillation.

## Relation to the corpus

FALCON expands [[multi-modal-semantic-communication]] beyond link-aware control: it aligns heterogeneous modalities, selects semantic tokens, and uses [[generative-diffusion-model|diffusion]] as a receiver-side signal reconstructor. This differs from [[wang-2026-diffusion-semantic-uav-edge]], where diffusion generates trajectory actions around a semantic edge-computing optimizer.

## Raw artifacts

- Parse: `raw/sources/FALCON_A_Diffusion_Model-Empowered_Semantic_Communication_Framework_for_Low-Altitude_Wireless_Networks/FALCON_A_Diffusion_Model-Empowered_Semantic_Communication_Framework_for_Low-Altitude_Wireless_Networks.md`
- Origin PDF: `raw/sources/FALCON_A_Diffusion_Model-Empowered_Semantic_Communication_Framework_for_Low-Altitude_Wireless_Networks/FALCON_A_Diffusion_Model-Empowered_Semantic_Communication_Framework_for_Low-Altitude_Wireless_Networks.pdf`
- Figures: `raw/sources/FALCON_A_Diffusion_Model-Empowered_Semantic_Communication_Framework_for_Low-Altitude_Wireless_Networks/images/`
