---
type: source
title: "Semantic Successive Refinement: A Generative AI-Aided Semantic Communication Framework"
authors: ["Kexin Zhang", "Lixin Li", "Wensheng Lin", "Yuna Yan", "Rui Li", "Wenchi Cheng", "Zhu Han"]
year: 2025
url: "https://doi.org/10.1109/TCCN.2025.3526839"
venue: "IEEE Transactions on Cognitive Communications and Networking (IEEE TCCN)"
tags: [source, semantic-communication, generative-ai, diffusion-model, swin-transformer, multi-user, image-transmission]
related:
  - "[[semantic-communication]]"
  - "[[generative-diffusion-model]]"
  - "[[task-oriented-communication]]"
  - "[[liang-2025-gai-semcom-survey]]"
  - "[[zhu-han]]"
  - "[[zhu-han]]"
created: 2026-06-04
updated: 2026-07-13
---

# Semantic Successive Refinement: A Generative AI-Aided Semantic Communication Framework

## Citation

Zhang, K., Li, L., Lin, W., Yan, Y., Li, R., Cheng, W., & Han, Z. (2025). *Semantic Successive Refinement: A Generative AI-Aided Semantic Communication Framework*. **IEEE Transactions on Cognitive Communications and Networking**, 11(2). DOI: 10.1109/TCCN.2025.3526839. (Received 30 June 2024; accepted 31 December 2024; published 7 January 2025; current version 9 April 2025.)

## TL;DR

Proposes a **Generative AI Semantic Communication (GSC)** system for image transmission: at the transmitter, a **Swin Transformer**-based joint source-channel coding (JSCC) extracts and compresses semantic features; at the receiver, a **Diffusion Model (DM)** reconstructs high-quality images from degraded signals, improving perceptual quality over CNN-based methods (especially at low SNR). Extends to a **Multi-User GSC (MU-GSC)** system with asynchronous concurrent processing and task-parallel caching. Achieves +17.75% PSNR vs CNN-based DeepJSCC in AWGN channels and +20.84% in Rayleigh channels.

## Problem framing

Traditional semantic communication minimizes signal distortion (MSE/SSIM) but neglects perceptual quality — especially problematic at low SNR where fine image details are lost. GAI models (particularly diffusion models) excel at perceptual reconstruction by generating realistic details from degraded inputs. Integrating diffusion model decoding with semantic encoding bridges the gap between information-theoretic compression and human-perceptual quality. Multi-user scenarios require managing simultaneous requests with shared compute/channel resources — addressed by asynchronous processing.

## System model

- **Single-user GSC:** Swin Transformer-based encoder compresses image semantic features → transmitted over wireless channel (AWGN or Rayleigh) → diffusion model decoder reconstructs image iteratively by estimating a compact conditional vector (not full diffusion chain).
- **Diffusion-model decoder:** estimates a conditional vector from degraded received features; this guides the reverse diffusion process to reconstruct the original image's perceptual content.
- **Multi-user MU-GSC:** asynchronous concurrent processing + task-parallel execution + caching mechanism to serve multiple users simultaneously with shared resources.
- **Comparison baseline:** CNN-based DeepJSCC.
- **Metrics:** PSNR (Peak Signal-to-Noise Ratio), subjective perceptual quality.

## Key findings

- GSC achieves **+17.75% PSNR improvement** over CNN-based DeepJSCC in AWGN channels and **+20.84% in Rayleigh channels** (parse Abstract).
- The diffusion model decoder significantly improves perceptual quality at **low SNR** where CNN-based reconstruction fails to recover fine details (parse Section I motivation + Section IV results).
- MU-GSC with asynchronous concurrent processing efficiently serves multiple users while maintaining high image quality, demonstrating scalability (parse Section III-B + IV).

## Limitations / future work

Computational cost of diffusion model decoding (iterative denoising) is higher than CNN decoding — addressed partially by the conditional-vector simplification but not fully eliminated. The parse does not enumerate explicit latency benchmarks for the diffusion decoder vs. CNN decoder.

## Relation to the corpus

Zhu Han ([[zhu-han]]) is a co-author. A concrete system implementation paper within the [[semantic-communication]] / GAI-SemCom space surveyed in [[liang-2025-gai-semcom-survey]]. The Swin-Transformer encoder + diffusion-model decoder architecture is distinct from other corpus SemCom papers (e.g., [[zheng-2024-semcom-sec-offloading]] which uses PSFed for coding updates). The PSNR improvement figures are the primary quantitative grounding claim.

## Raw artifacts

- `raw/sources/Semantic_Successive_Refinement_A_Generative_AI-Aided_Semantic_Communication_Framework/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
