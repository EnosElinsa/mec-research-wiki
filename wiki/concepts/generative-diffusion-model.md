---
type: concept
title: "Generative Diffusion Model (GDM)"
tags: [generative-ai, diffusion, decision-generation]
related:
  - "[[generative-ai-for-mec]]"
  - "[[diffusion-model-as-optimizer]]"
  - "[[prompt-engineering]]"
  - "[[ye-2025-aigc-diffusion-contract]]"
  - "[[peng-2025-drudm-cfg]]"
created: 2026-05-29
updated: 2026-05-29
---

# Generative Diffusion Model (GDM)

A generative model that learns to reverse a gradual noising process: a **forward** chain adds Gaussian noise to data over K steps, and a learned **reverse** (denoising) chain reconstructs samples from noise. Beyond generating media (images, audio), GDMs can generate **decisions** — conditioning the reverse chain on an environment/state vector to emit an action or design directly.

In the wiki, [[ye-2025-aigc-diffusion-contract]] uses a GDM in both roles' spirit: the service generates images via diffusion, *and* the optimizer generating contract items is itself a conditional diffusion policy (see [[diffusion-model-as-optimizer]]). It also appears in [[peng-2025-drudm-cfg]] (diffusion with classifier-free guidance for MEC decisions). This page is the concrete diffusion-mechanism slug; [[generative-ai-for-mec]] remains the broad umbrella.
