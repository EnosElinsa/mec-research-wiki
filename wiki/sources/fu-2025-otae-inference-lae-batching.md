---
type: source
title: "Over-the-Air Edge Inference for Low-Altitude Airspace: Generative AI-Aided Multi-Task Batching and Beamforming Design"
authors: ["Yang Fu", "Peng Qin", "Yifei Wang", "Liming Chen", "Mengyao Li", "Xiongwen Zhao"]
year: 2025
url: "https://doi.org/10.1109/TCOMM.2025.3563657"
venue: "IEEE Transactions on Communications (IEEE TCOMM)"
tags: [source, low-altitude-economy, edge-inference, over-the-air-computation, beamforming, diffusion-model, batching]
related:
  - "[[low-altitude-intelligent-network]]"
  - "[[over-the-air-computation]]"
  - "[[collaborative-dl-inference]]"
  - "[[generative-diffusion-model]]"
  - "[[diffusion-model-as-optimizer]]"
  - "[[cooperative-perception]]"
  - "[[qin-2025-matd3-noma-queue-sagin]]"
  - "[[khoramnejad-2025-gai-wireless-optimization-survey]]"
created: 2026-05-29
updated: 2026-05-29
---

# Over-the-Air Edge Inference for Low-Altitude Airspace: Generative AI-Aided Multi-Task Batching and Beamforming Design

## Citation

Fu, Y., Qin, P., Wang, Y., Chen, L., Li, M., & Zhao, X. (2025). *Over-the-Air Edge Inference for Low-Altitude Airspace: Generative AI-Aided Multi-Task Batching and Beamforming Design*. **IEEE Transactions on Communications**. DOI: 10.1109/TCOMM.2025.3563657.

## TL;DR

A multi-task **over-the-air edge inference** system for low-altitude (LA) airspace: a 6G base station aggregates features from multiple sensors' views via **over-the-air computation** and processes multiple inference tasks **in batches** to reduce memory access. The authors jointly design batching and beamforming to maximize the number of completed tasks under latency and inference-accuracy constraints, handling synchronous (single-batch) and asynchronous task arrivals — the latter with a **diffusion-model-based online batching policy**.

## Problem framing

LA airspace sensing requires the BS to aggregate multi-sensor features and run an AI model, but high-dimensional feature uploading and frequent memory access create communication + computation bottlenecks. Over-the-air feature aggregation and batched inference relieve them; batching and beamforming must be co-designed.

## System model / method

- **Synchronous arrivals, single batch:** a spatial-correlation-aware beamforming approach (**JB2-Synchronous**) suppresses feature-aggregation error and ensures inference accuracy; batch size found via the maximum feasible size.
- **Asynchronous arrivals:** **GAI-Asynchronous** uses a **diffusion-model-based actor network** to output batching decisions online, adapting to dynamic/uncertain arrivals while balancing completed tasks, waiting latency, and BS busy time ([[diffusion-model-as-optimizer]], [[over-the-air-computation]]).

## Key findings

- On a real-world dataset, capturing spatial correlation among sensors is important (especially with insufficient spatial DoF); the approach beats benchmark batching/beamforming/learning methods and approaches offline optimization with prior task information (qualitative; specific curves in the paper).

## Limitations / future work

Future work is truncated in the parse, but the synchronous→asynchronous progression and real-dataset evaluation are emphasized; full WCAG-style robustness across deployments is not claimed.

## Relation to the corpus

A **low-altitude-economy edge-inference** entry that brings the diffusion-as-optimizer pattern (cf. [[ye-2025-aigc-diffusion-contract]], [[zhang-2024-gdmtd3-aerial-secure-cb]], survey [[khoramnejad-2025-gai-wireless-optimization-survey]]) to over-the-air inference and batching. Its cooperative multi-sensor feature aggregation connects to [[cooperative-perception]] and [[collaborative-dl-inference]]; it shares authors Yang Fu / Peng Qin with [[qin-2025-matd3-noma-queue-sagin]]. Reinforces [[low-altitude-intelligent-network]] and introduces [[over-the-air-computation]].

## Raw artifacts

- `raw/sources/Over-the-Air_Edge_Inference_for_Low-Altitude_Airspace_Generative_AI-Aided_Multi-Task_Batching_and_Beamforming_Design/full.md`
- Original PDF and extracted figures in the same folder.
