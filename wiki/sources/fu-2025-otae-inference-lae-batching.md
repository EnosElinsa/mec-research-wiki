---
type: source
title: "Over-the-Air Edge Inference for Low-Altitude Airspace: Generative AI-Aided Multi-Task Batching and Beamforming Design"
authors: ["Yang Fu", "Peng Qin", "Yifei Wang", "Liming Chen", "Mengyao Li", "Xiongwen Zhao"]
year: 2025
url: "https://doi.org/10.1109/TCOMM.2025.3563657"
venue: "IEEE Transactions on Communications (IEEE TCOMM)"
modeling_card: required
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
updated: 2026-07-16
---

# Over-the-Air Edge Inference for Low-Altitude Airspace: Generative AI-Aided Multi-Task Batching and Beamforming Design

## Citation

Fu, Y., Qin, P., Wang, Y., Chen, L., Li, M., & Zhao, X. (2025). *Over-the-Air Edge Inference for Low-Altitude Airspace: Generative AI-Aided Multi-Task Batching and Beamforming Design*. **IEEE Transactions on Communications**. DOI: 10.1109/TCOMM.2025.3563657.

## TL;DR

A multi-task **over-the-air edge inference** system for low-altitude (LA) airspace: a 6G base station aggregates features from multiple sensors' views via **over-the-air computation** and processes multiple inference tasks **in batches** to reduce memory access. The authors jointly design batching and beamforming to maximize the number of completed tasks under latency and inference-accuracy constraints, handling synchronous (single-batch) and asynchronous task arrivals — the latter with a **diffusion-model-based online batching policy**.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Low-altitude sensors extract multi-view features and upload them simultaneously to a multi-antenna BS through over-the-air computation. The BS reconstructs each task's global feature and batches inference requests with heterogeneous deadlines and accuracy targets to amortize model-loading latency.

**Problem & objective**: Maximize inference throughput, $\max_{B,\mathbf y,\mathbf t,\mathbf w,\mathbf v}\sum_n\sum_b y_{n,b}$, by jointly selecting completed tasks, batch count and timing, and AirComp transceiver beamforming for synchronous or stochastic asynchronous arrivals.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Task-batch assignment | $y_{n,b}$ | binary | Whether task $n$ is executed in batch $b$ |
| Number and start time of batches | $B,t_b$ | integer and continuous | Batch schedule at the BS |
| Sensor transmit beam | $\mathbf w_{n,k}$ | complex continuous | Beamformer of sensor $k$ for task $n$ |
| BS receive beam and scaling | $\mathbf v_n,\eta_n$ | complex and positive continuous | AirComp combiner and denoising factor |
| Online start and selection action | $a^{\mathrm{sta}},a_n^{\mathrm{bat}}$ | binary | Whether to start now and which waiting tasks to include |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Each task is assigned at most once: $\sum_b y_{n,b}\leq1$. |
| C2 | A batch starts after all included tasks arrive and after the preceding batch completes. |
| C3 | Included tasks finish by their deadlines: $y_{n,b}(t_b+l_b)\leq D_n$. |
| C4 | Expected feature-aggregation error meets the margin-derived accuracy bound. |
| C5 | Every sensor beam respects $\lVert\mathbf w_{n,k}\rVert_2^2\leq P$, and each receive beam is unit norm. |
| C6 | For asynchronous operation, $1\leq B\leq N$ and the BS cannot start a new batch while it is busy. |

**Algorithm**: For synchronous arrivals, increase candidate batch size until feasibility fails, prioritize deadline- and accuracy-feasible tasks, and alternate spatial-correlation-aware transmit and receive beamforming updates. For asynchronous arrivals, formulate remaining deadlines, waiting-task count, and BS busy time as an MDP state and train a diffusion-model actor with critic feedback and replay to generate batch-start and task-selection actions online.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Fu et al. [x] developed multi-task over-the-air edge inference for low-altitude sensing with joint batching and transceiver beamforming. They maximized the number of completed tasks over task-batch assignments, batch timing, transmit beams, and receive combiners under one-execution, deadline, inference-accuracy, sensor-power, and combiner-normalization constraints. Their synchronous method searches for the largest feasible batch with spatial-correlation-aware alternating beamforming, while the asynchronous method uses a diffusion actor to generate online batch-start and task-selection actions. ModelNet experiments reported up to 29.89% higher synchronous inference throughput than the listed baselines, and the asynchronous policy was only 4% below prior-aware offline MINLP while exceeding other baselines by 21.18% to 40.25%.

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
