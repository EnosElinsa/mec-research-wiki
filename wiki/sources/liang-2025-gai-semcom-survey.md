---
type: source
title: "Generative AI-Driven Semantic Communication Networks: Architecture, Technologies, and Applications"
authors: ["Chengsi Liang", "Hongyang Du", "Yao Sun", "Dusit Niyato", "Jiawen Kang", "Dezong Zhao", "Muhammad Ali Imran"]
year: 2025
url: "https://doi.org/10.1109/TCCN.2024.3435524"
venue: "IEEE Transactions on Cognitive Communications and Networking (IEEE TCCN)"
tags: [source, semantic-communication, generative-ai, aigc, survey, knowledge-management, resource-allocation]
related:
  - "[[semantic-communication]]"
  - "[[task-oriented-communication]]"
  - "[[mobile-aigc-network]]"
  - "[[dusit-niyato]]"
  - "[[xu-2024-mobile-aigc-survey]]"
  - "[[khoramnejad-2025-gai-wireless-optimization-survey]]"
created: 2026-06-04
updated: 2026-06-04
---

# Generative AI-Driven Semantic Communication Networks: Architecture, Technologies, and Applications

## Citation

Liang, C., Du, H., Sun, Y., Niyato, D., Kang, J., Zhao, D., & Imran, M. A. (2025). *Generative AI-Driven Semantic Communication Networks: Architecture, Technologies, and Applications*. **IEEE Transactions on Cognitive Communications and Networking**, 11(1). DOI: 10.1109/TCCN.2024.3435524. (Received 22 December 2023; accepted 19 July 2024; published 29 July 2024; current version 7 February 2025.)

## TL;DR

A comprehensive survey on the synthesis of **generative AI (GAI)** and **semantic communication (SemCom)** — the first to jointly cover framework architecture, transceiver design, information-effectiveness metrics, resource allocation, and **knowledge management** for GAI-driven SemCom networks. Proposes a novel three-plane network architecture (data plane, physical infrastructure, network control plane). Covers GAI models (unimodal + multimodal), SemCom transceiver design, knowledge construction/update/sharing, and use cases (autonomous driving, smart cities, Metaverse). Companion paper to [[xu-2024-mobile-aigc-survey]] (AIGC services focus) and [[khoramnejad-2025-gai-wireless-optimization-survey]] (wireless optimization focus).

## Problem framing

Traditional Shannon communication transmits bits regardless of semantic content, wasting bandwidth on irrelevant data. AIGC services (text, image, video generation) impose high throughput + low latency demands that existing networks struggle to meet. SemCom addresses this by conveying meaning rather than bits. GAI provides the ML backbone for SemCom encoders/decoders and knowledge base construction; SemCom in turn provides low-latency AIGC delivery. Their mutual reinforcement is the central insight. Three open challenges identified: (1) multimodal GAI encoder/decoder design; (2) measuring semantic information effectiveness; (3) managing knowledge as a network resource with freshness vs. update-cost tradeoffs.

## System model

- **Architecture.** Three-plane design: (a) data plane — GAI models + SemCom transceivers on user devices; (b) physical infrastructure — RAN + edge servers + cloud; (c) network control plane — resource allocation, knowledge management, policy coordination.
- **Transceiver design.** GAI-augmented semantic encoder extracts compressed semantic features; channel encoder adapts to channel conditions; semantic decoder on receiver side reconstructs meaning using shared knowledge base.
- **Information effectiveness.** Surveys new metrics beyond Shannon capacity: task-completion rate, semantic similarity, goal-oriented quality, age-of-information extensions.
- **Knowledge management.** Knowledge base construction (from sensing/history data), update (freshness vs. cost tradeoff), sharing across nodes (compression, privacy).
- **Use cases.** Autonomous driving (V2X SemCom), smart cities (IoT sensor semantic compression), Metaverse (high-fidelity holographic SemCom).

## Key findings

- Survey identifies GAI and SemCom as **mutually reinforcing**: GAI enables intelligent SemCom encoding/generation; SemCom enables efficient AIGC delivery (parse Sections I-B, II).
- Existing semantic effectiveness metrics (Shannon-derived SNR, BER) are inadequate for SemCom; task-specific and goal-oriented metrics are needed (parse Section II-C, challenge 2).
- Knowledge management is a first-class network resource — update frequency, storage capacity, and sharing protocols must be co-designed with SemCom resource allocation (parse challenge 3, Section V).
- Proposed architecture cleanly separates data, infrastructure, and control responsibilities, enabling modular deployment (parse Section II-A).

## Limitations / future work

Survey does not include experimental/simulation results — it is a conceptual framework and literature synthesis. Security/privacy of knowledge bases and GAI-generated content is flagged as an open direction but not fully treated.

## Relation to the corpus

Complements [[xu-2024-mobile-aigc-survey]] (which focuses on AIGC service lifecycle and mobile-edge infrastructure) and [[khoramnejad-2025-gai-wireless-optimization-survey]] (GAI for wireless optimization). Together these three surveys anchor the GAI/SemCom survey space in the corpus. The [[semantic-communication]] concept and knowledge-management challenges recur in [[zheng-2024-semcom-sec-offloading]], [[sun-2024-mfris-semantic-antijamming]], and the semantic successive refinement paper in this wiki.

## Raw artifacts

- `raw/sources/Generative_AI-Driven_Semantic_Communication_Networks_Architecture_Technologies_and_Applications/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
