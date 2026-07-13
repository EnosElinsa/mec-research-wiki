---
type: concept
title: "Generative Diffusion Model (GDM)"
tags: [generative-ai, diffusion, decision-generation]
related:
  - "[[jin-2026-skyndn-incentivizer]]"
  - "[[wu-2026-sensing-error-uav-scheduling]]"
  - "[[diffusion-augmented-madrl-replay]]"
  - "[[generative-ai-for-mec]]"
  - "[[diffusion-model-as-optimizer]]"
  - "[[prompt-engineering]]"
  - "[[ye-2025-aigc-diffusion-contract]]"
  - "[[peng-2025-drudm-cfg]]"
  - "[[tang-2026-hg-maddpg-uav-rescue]]"
  - "[[zhao-2026-temporal-spectrum-cartography]]"
  - "[[multi-agent-diffusion-policy]]"
  - "[[niu-2026-falcon-semantic]]"
created: 2026-05-29
updated: 2026-07-14
---

# Generative Diffusion Model (GDM)

[[jin-2026-skyndn-incentivizer]] uses reverse diffusion as the actor that generates many-to-many UAV content allocations, with critic feedback during training and the paper's stated execution design.

[[wu-2026-sensing-error-uav-scheduling]] uses diffusion for replay augmentation rather than action generation: a model learns complete transition tuples and mixes synthetic error-bearing samples with real experience through [[diffusion-augmented-madrl-replay]].

A generative model that learns to reverse a gradual noising process: a **forward** chain adds Gaussian noise to data over K steps, and a learned **reverse** (denoising) chain reconstructs samples from noise. Beyond generating media (images, audio), GDMs can generate **decisions** — conditioning the reverse chain on an environment/state vector to emit an action or design directly.

In the wiki, [[ye-2025-aigc-diffusion-contract]] uses a GDM in both roles' spirit: the service generates images via diffusion, *and* the optimizer generating contract items is itself a conditional diffusion policy (see [[diffusion-model-as-optimizer]]). It also appears in [[peng-2025-drudm-cfg]] (diffusion with classifier-free guidance for MEC decisions), [[tang-2026-hg-maddpg-uav-rescue]] (diffusion-enhanced MADDPG action generation for UAV rescue), and [[zhao-2026-temporal-spectrum-cartography]] (a [[multi-agent-diffusion-policy]] for mobile spectrum-sensor placement). This page is the concrete diffusion-mechanism slug; [[generative-ai-for-mec]] remains the broad umbrella.

[[niu-2026-falcon-semantic]] uses diffusion in a different role: its receiver reconstructs a distorted semantic JSCC signal rather than generating an action. A DDIM-style reverse path is constrained by range/null-space correction, with an uncertainty gate that suppresses pseudo-inverse correction when channel-error propagation would amplify noise.
