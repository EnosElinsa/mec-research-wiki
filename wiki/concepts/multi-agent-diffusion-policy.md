---
type: concept
title: "Multi-Agent Diffusion Policy"
tags: [generative-ai, diffusion, multi-agent-rl, ctde]
related:
  - "[[zhao-2026-temporal-spectrum-cartography]]"
  - "[[generative-diffusion-model]]"
  - "[[diffusion-model-as-optimizer]]"
  - "[[maddpg]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[multi-agent-td3]]"
created: 2026-07-07
updated: 2026-07-07
---

# Multi-Agent Diffusion Policy

A multi-agent policy representation where each agent's action is generated through a conditional reverse-diffusion process rather than a direct deterministic or stochastic actor head. The diffusion process can represent multi-modal action distributions while still conditioning on local observations or a learned state embedding.

In [[zhao-2026-temporal-spectrum-cartography]], MADP uses a diffusion-based actor and temporal-attention state encoder for dynamic UAV spectrum-sensor placement. Training follows the multi-agent actor-critic pattern, while execution is decentralized. This makes the page a bridge between [[generative-diffusion-model]], [[diffusion-model-as-optimizer]], and the existing [[maddpg]] / [[centralized-training-decentralized-execution]] family.
