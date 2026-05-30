---
type: concept
title: "AIGC Service Provider (ASP)"
tags: [generative-ai, edge-computing, service-role, incentive]
related:
  - "[[generative-ai-for-mec]]"
  - "[[mobile-aigc-network]]"
  - "[[contract-theory]]"
  - "[[prompt-engineering]]"
  - "[[qoe-modeling-mec]]"
  - "[[ye-2025-aigc-diffusion-contract]]"
  - "[[xu-2024-mobile-aigc-survey]]"
created: 2026-05-29
updated: 2026-05-31
---

# AIGC Service Provider (ASP)

The edge entity that deploys a **pretrained foundation model** (e.g. Stable Diffusion XL) at the network edge and sells AIGC inference (e.g. text-to-image generation) to mobile users. The ASP allocates its compute/communication resources — prompt-optimization effort, diffusion denoising steps, CPU frequency, transmission rate — and prices its service, while users are self-interested with private valuations.

In the wiki, [[ye-2025-aigc-diffusion-contract]] casts the ASP as the **principal** in a [[contract-theory]] mechanism: it designs a menu of contract items so users self-select truthfully under information asymmetry. The ASP role situates generative AI within the corpus's [[generative-ai-for-mec]] and [[qoe-modeling-mec]] threads, with [[prompt-engineering]] as a distinctive new resource lever. The ASP-selection problem is one of the case studies surveyed by [[xu-2024-mobile-aigc-survey]] (see [[mobile-aigc-network]]).
