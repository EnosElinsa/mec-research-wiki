---
type: source
title: "Generative AI for the Optimization of Next-Generation Wireless Networks: Basics, State-of-the-Art, and Open Challenges"
authors: ["Fahime Khoramnejad", "Ekram Hossain"]
year: 2025
url: "https://doi.org/10.1109/COMST.2025.3535554"
venue: "IEEE Communications Surveys & Tutorials (IEEE COMST)"
modeling_card: not_applicable
tags: [source, survey, generative-ai, 6g, network-optimization, resource-allocation, diffusion-model]
related:
  - "[[generative-ai-for-mec]]"
  - "[[generative-diffusion-model]]"
  - "[[generative-adversarial-network]]"
  - "[[diffusion-model-as-optimizer]]"
  - "[[mao-2017-mec-survey-communication]]"
  - "[[wang-2025-lae-network-survey]]"
  - "[[du-2024-distributed-foundation-models-6g]]"
created: 2026-05-29
updated: 2026-07-16
---

# Generative AI for the Optimization of Next-Generation Wireless Networks: Basics, State-of-the-Art, and Open Challenges

## Citation

Khoramnejad, F., & Hossain, E. (2025). *Generative AI for the Optimization of Next-Generation Wireless Networks: Basics, State-of-the-Art, and Open Challenges*. **IEEE Communications Surveys & Tutorials**. DOI: 10.1109/COMST.2025.3535554.

## TL;DR

A **survey** of how generative AI (GAI) unlocks optimization opportunities in next-generation (xG, e.g. 6G) wireless networks. It reviews GAI model families (GANs, generative diffusion models, GFlowNets), surveys their use for resource allocation and network performance, discusses the networking requirements to support GAI applications, and closes with a case study using a diffusion-based GAI model (with RL) for load balancing, carrier aggregation, and backhauling in non-terrestrial networks.

This is the wiki's dedicated **GAI-for-wireless** survey anchor.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Khoramnejad and Hossain [x] surveyed generative artificial intelligence for the optimization of next-generation wireless networks. They reviewed generative adversarial networks, generative diffusion models, and generative flow networks together with major communication paradigms and resource-allocation applications in xG networks. The survey examined how generative models support data generation, offline configuration exploration, dynamic resource allocation, and overall network-performance optimization. It also discussed networking requirements for generative-AI applications and presented an illustrative diffusion and reinforcement-learning case study for load balancing, carrier aggregation, and backhauling in non-terrestrial networks. The authors identified model complexity, data requirements, robustness, interpretability, security, privacy, and real-time deployment as open challenges.

## Problem framing

xG networks are complex and dynamic, straining traditional optimization. GAI is positioned as a tool that learns from real network data, enables safe offline exploration of configurations, generates diverse/unseen scenarios, and scales to large networks — advantages over both classical optimization and other ML.

## Scope surveyed

- **GAI models.** GANs, generative diffusion models (GDMs), GFlowNets ([[generative-diffusion-model]], [[generative-adversarial-network]]).
- **6G communication paradigms** touched: mobile AIGC, semantic communication (SemCom), ISAC, secure communication.
- **GAI for optimization.** Resource allocation and overall network performance; networking requirements to host GAI.
- **Case study.** A diffusion-based GAI model combined with reinforcement learning for load balancing, carrier aggregation, and backhauling optimization in NTNs — a concrete [[diffusion-model-as-optimizer]] instance.

## Key findings

As a survey, no original benchmarks; its contribution is taxonomy + state-of-the-art synthesis + a worked NTN optimization case study. It flags model complexity and training-data requirements as the main hurdles, with distributed learning, edge computing, and on-device processing as promising mitigations.

## Limitations / future work

Survey/case-study, not a controlled experimental study. The case study is illustrative rather than a comprehensive benchmark.

## Relation to the corpus

The conceptual umbrella for the wiki's growing **generative-AI MEC** thread: it frames the diffusion-as-optimizer pattern used by [[ye-2025-aigc-diffusion-contract]], [[peng-2025-drudm-cfg]], and [[fu-2025-otae-inference-lae-batching]], and the GAN-enhanced approaches [[zhang-2025-gan-td3-isac-active-ris]] / [[faisal-2025-cgan-ris-isac-channel]]. Sits beside the foundational surveys [[mao-2017-mec-survey-communication]] and [[wang-2025-lae-network-survey]], and complements the 6G foundation-models overview [[du-2024-distributed-foundation-models-6g]].

## Raw artifacts

- `raw/sources/Generative_AI_for_the_Optimization_of_Next-Generation_Wireless_Networks_Basics_State-of-the-Art_and_Open_Challenges/full.md`
- Original PDF and extracted figures in the same folder.
