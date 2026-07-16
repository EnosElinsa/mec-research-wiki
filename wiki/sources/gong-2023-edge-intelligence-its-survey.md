---
type: source
title: "Edge Intelligence in Intelligent Transportation Systems: A Survey"
authors: ["Taiyuan Gong", "Li Zhu", "F. Richard Yu", "Tao Tang"]
year: 2023
url: "https://doi.org/10.1109/TITS.2023.3275741"
venue: "IEEE Transactions on Intelligent Transportation Systems"
modeling_card: not_applicable
tags: [source, survey, edge-intelligence, intelligent-transportation-systems, vehicular-mec, uav-enabled-its, edge-ai]
related:
  - "[[edge-intelligence]]"
  - "[[vehicular-mec]]"
  - "[[uav-enabled-its]]"
  - "[[mobile-edge-computing]]"
  - "[[xu-2024-mobile-aigc-survey]]"
  - "[[wang-2025-lae-network-survey]]"
created: 2026-07-07
updated: 2026-07-16
---

# Edge Intelligence in Intelligent Transportation Systems: A Survey

## Citation

Gong, T., Zhu, L., Yu, F. R., & Tang, T. (2023). *Edge Intelligence in Intelligent Transportation Systems: A Survey*. **IEEE Transactions on Intelligent Transportation Systems**. DOI: 10.1109/TITS.2023.3275741.

## TL;DR

A survey of [[edge-intelligence|edge intelligence (EI)]] for intelligent transportation systems (ITS). It frames EI as pushing AI inference and training toward the edge-device-cloud continuum so ITS applications can reduce latency, protect privacy, reduce backbone-network pressure, and exploit edge-generated transportation data. The survey covers EI-based ITS architecture, communications and data processing, AI/IoT/edge-computing enablers, applications in autonomous driving, [[vehicular-mec|vehicular edge computing]], UAV-assisted ITS, and rail transportation, plus platforms, datasets, challenges, and future directions.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Gong et al. [x] surveyed edge intelligence for intelligent transportation systems across the edge-device-cloud continuum. They presented a three-layer architecture of end devices, edge nodes, and cloud centers and reviewed communication, data processing, artificial intelligence, Internet of Things, and edge-computing enablers. The literature taxonomy covers autonomous driving, vehicular edge computing, intelligent vehicular transportation, UAV-assisted ITS, and rail transportation, together with model-training and inference platforms and datasets. The survey identifies real-time response, privacy, bandwidth pressure, and constrained edge computation as central challenges and discusses application-dependent deployment levels and future edge-intelligence directions.

## Problem framing

ITS applications generate large volumes of sensor, vehicle, camera, railway, and UAV data at the network edge. Cloud-only processing introduces transmission delay, bandwidth pressure, and privacy risk; fully local processing is often constrained by device computation and energy. The paper positions EI as a middle-ground architecture in which AI workloads can be split across end devices, edge nodes, and cloud resources according to latency, privacy, energy, and model-complexity needs.

## System model

As a survey, the paper does not define one optimization model. Its reference architecture is a three-layer EI-based ITS stack:

- **End devices:** vehicles, traffic lights, cameras, phones, UAVs, and sensors generate data and may process or share it locally.
- **Edge nodes:** RSUs, APs, micro data centers, routers, and other nearby servers process time-sensitive data and coordinate local services.
- **Cloud centers:** retain high-capacity compute and storage for complex model training, long-term analytics, and tasks that can tolerate higher latency.

The survey also discusses the seven-level EI taxonomy, from cloud-heavy co-inference/training to all-on-device training and inference.

## Method

The paper is a taxonomy and literature survey. It reviews:

- ITS challenges motivating EI: real-time response, privacy, network bandwidth, and edge-device compute limits.
- Enabling technologies: AI models, IoT, edge computing, NOMA, federated learning, model training/inference platforms, and benchmark datasets.
- Application areas: autonomous driving, vehicular edge computing, intelligent vehicular transportation, UAVs in ITS, and rail transportation control/management.
- Deployment questions: EI model training, EI inference platforms, systematic EI frameworks, and business/infrastructure challenges.

## Key findings

- The survey identifies a gap in prior surveys: many focus on connected vehicles, IoV, task offloading, or ITS sensing, while UAV and rail transportation scenarios receive less coverage.
- The paper argues that the appropriate EI level is application-dependent: higher edge/device locality reduces uploaded data and improves privacy/latency, but it also demands stronger local processors and may limit cross-vehicle or cross-infrastructure data sharing.
- UAVs are presented as future EI-enabled ITS components for RSU/sensor data collection, ground traffic monitoring, flying RSUs, and cooperative road-traffic monitoring.
- Rail transportation is treated as a separate EI domain where high-speed mobility, safety monitoring, and train-control systems create distinct networking and edge-processing requirements.

## Limitations / future work

Survey-only; no new algorithm or benchmark result. Its own comparison table says the paper gives more attention to possible EI directions and enabling technologies than to technologies already used in practice. DOI/venue/year are verified by title-matched DOI metadata because the parse does not expose a DOI line.

## Relation to the corpus

This is the corpus's ITS-side edge-intelligence survey anchor. It complements [[wang-2025-lae-network-survey]], which surveys low-altitude economy networks, and [[xu-2024-mobile-aigc-survey]], which surveys mobile edge-cloud AIGC services. For MEC, its main value is vocabulary: it connects [[vehicular-mec]], [[uav-enabled-its]], and edge AI deployment levels rather than adding a specific offloading optimizer.

## Raw artifacts

- Parse: `raw/sources/Edge Intelligence in Intelligent Transportation Systems A Survey/Edge Intelligence in Intelligent Transportation Systems A Survey.md`
- Origin PDF: `raw/sources/Edge Intelligence in Intelligent Transportation Systems A Survey/Edge Intelligence in Intelligent Transportation Systems A Survey.pdf`
- Figures: `raw/sources/Edge Intelligence in Intelligent Transportation Systems A Survey/images/`
