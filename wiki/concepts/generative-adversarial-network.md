---
type: concept
title: "Generative Adversarial Network (GAN)"
tags: [generative-ai, deep-learning]
related:
  - "[[yang-2026-generative-radio-map-lae]]"
  - "[[radio-map-assisted-channel-estimation]]"
  - "[[zhang-2025-gan-td3-isac-active-ris]]"
  - "[[conditional-gan]]"
  - "[[generative-diffusion-model]]"
  - "[[generative-ai-for-mec]]"
  - "[[khoramnejad-2025-gai-wireless-optimization-survey]]"
  - "[[wang-2023-differentiated-uav-services]]"
  - "[[multi-agent-imitation-learning]]"
created: 2026-05-29
updated: 2026-07-13
---

# Generative Adversarial Network (GAN)

A generative model trained as a two-player game: a **generator** produces samples while a **discriminator** tries to distinguish them from real data; adversarial training drives the generator toward the true data distribution. GANs can model complex, high-dimensional distributions, which is useful for channel modeling, data augmentation, and policy enhancement in wireless/MEC settings.

In the wiki, GANs appear as: a policy enhancer integrated into TD3 for ISAC beamforming in [[zhang-2025-gan-td3-isac-active-ris]] (GAN-TD3); the conditional variant for channel estimation in [[faisal-2025-cgan-ris-isac-channel]] (see [[conditional-gan]]); CVCGAN for [[radio-map-assisted-channel-estimation]] in [[yang-2026-generative-radio-map-lae]]; and as one of the GAI model families surveyed by [[khoramnejad-2025-gai-wireless-optimization-survey]] alongside [[generative-diffusion-model]] and GFlowNets.
