---
type: concept
title: "Semantic Communication"
tags: [6g, semantic, source-channel-coding, data-compression, physical-layer]
related:
  - "[[multi-functional-ris]]"
  - "[[anti-jamming-mec]]"
  - "[[over-the-air-computation]]"
  - "[[mobile-edge-computing]]"
  - "[[sun-2024-mfris-semantic-antijamming]]"
created: 2026-05-31
updated: 2026-06-01
---

# Semantic Communication

A 6G transmission paradigm that — unlike Shannon (bit) communication, which transmits the full bit sequence of a source — transmits only the **key (semantic) information**, discarding irrelevant content without task-level performance degradation. It has been demonstrated for text, speech, and image sources, typically via deep-learning-based joint source-channel coding, and is reported to improve spectral efficiency, energy efficiency, and transmission reliability.

## Relevance to MEC

Semantic transceivers bring **inherent robustness** and **data compression**, which reduce the data volume that must be offloaded and make computation more efficient under poor or adversarial channels. A recurring open issue (per the corpus) is **resource management** for semantic systems — e.g. semantic-aware division factors, channel assignment, and the number of transmitted symbols — especially beyond simplistic single-antenna setups.

## In this wiki

- [[sun-2024-mfris-semantic-antijamming]] pairs a semantic transceiver with a [[multi-functional-ris]] to maximize a **semantic computation rate** under jamming and imperfect CSI, subject to a **semantic-similarity requirement**. It positions itself against prior semantic-MEC work limited to single-antenna setups and prior RIS-MEC work using bit-level (non-semantic) transmission, motivating its multi-antenna MF-RIS-aided semantic MEC-IAGN under jamming.
