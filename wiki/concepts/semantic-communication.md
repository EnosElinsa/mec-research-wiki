---
type: concept
title: "Semantic Communication"
tags: [6g, semantic, source-channel-coding, data-compression, physical-layer]
related:
  - "[[multi-functional-ris]]"
  - "[[anti-jamming-mec]]"
  - "[[over-the-air-computation]]"
  - "[[mobile-edge-computing]]"
  - "[[semantic-content-reuse]]"
  - "[[probabilistic-semantic-communication]]"
  - "[[sun-2024-mfris-semantic-antijamming]]"
  - "[[du-2024-yolo-semcom-digital-twin]]"
  - "[[wang-2026-lifelong-semantic-content-reuse]]"
  - "[[wang-2026-diffusion-semantic-uav-edge]]"
  - "[[zhao-2025-probabilistic-semantic-sagin]]"
  - "[[multi-modal-semantic-communication]]"
  - "[[liu-2025-multimodal-semantic-iov-jamming]]"
  - "[[kernel-density-mean-field-marl]]"
  - "[[li-2026-uav-bs-semantic-mfmaddpg-kde]]"
  - "[[zhang-2026-distributed-jscc-uav-video]]"
created: 2026-05-31
updated: 2026-07-13
---

# Semantic Communication

A 6G transmission paradigm that — unlike Shannon (bit) communication, which transmits the full bit sequence of a source — transmits only the **key (semantic) information**, discarding irrelevant content without task-level performance degradation. It has been demonstrated for text, speech, and image sources, typically via deep-learning-based joint source-channel coding, and is reported to improve spectral efficiency, energy efficiency, and transmission reliability.

## Relevance to MEC

Semantic transceivers bring **inherent robustness** and **data compression**, which reduce the data volume that must be offloaded and make computation more efficient under poor or adversarial channels. A recurring open issue (per the corpus) is **resource management** for semantic systems — e.g. semantic-aware division factors, channel assignment, and the number of transmitted symbols — especially beyond simplistic single-antenna setups.

## In this wiki

- [[sun-2024-mfris-semantic-antijamming]] pairs a semantic transceiver with a [[multi-functional-ris]] to maximize a **semantic computation rate** under jamming and imperfect CSI, subject to a **semantic-similarity requirement**. It positions itself against prior semantic-MEC work limited to single-antenna setups and prior RIS-MEC work using bit-level (non-semantic) transmission, motivating its multi-antenna MF-RIS-aided semantic MEC-IAGN under jamming.
- [[du-2024-yolo-semcom-digital-twin]] applies semantic communication to [[digital-twin]] construction: a [[yolov7-object-detection|YOLOv7]] detector extracts only the semantically-relevant content (cropped objects + confidence + position) from UAV images, then allocates transmission power by per-object importance (a confidence rule and a diffusion-model-generated scheme), cutting transmitted data ~91% on its case study.
- [[wang-2026-lifelong-semantic-content-reuse]] uses semantic request representations for [[semantic-content-reuse]] in UAV-assisted Metaverse rendering: cache hits, semantic reuse, and full computation are treated as distinct service modes.
- [[wang-2026-diffusion-semantic-uav-edge]] formulates semantic extraction, transmission, and recovery as a UAV-assisted edge-computing optimization problem, with semantic processing rate as the objective.
- [[zhao-2025-probabilistic-semantic-sagin]] narrows semantic communication to [[probabilistic-semantic-communication]]: shared probabilistic graphs let the transmitter omit recoverable semantic relations, trading lower communication energy for added semantic-computation overhead in a SAGIN.
- [[liu-2025-multimodal-semantic-iov-jamming]] extends the line to [[multi-modal-semantic-communication]] in IoV, combining image and text semantics under jamming while UAV agents choose trajectories, user associations, and channels.
- [[li-2026-uav-bs-semantic-mfmaddpg-kde]] moves semantic communication into aerial-BS deployment: UAV-BSs are positioned to maximize BLEU-derived semantic fidelity, with [[kernel-density-mean-field-marl]] modeling continuous neighboring actions in a scalable mean-field MADDPG policy.
