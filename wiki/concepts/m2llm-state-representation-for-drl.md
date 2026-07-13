---
type: concept
title: "M2LLM State Representation for DRL"
tags: [multimodal-large-language-model, deep-reinforcement-learning, state-representation, edge-intelligence]
related:
  - "[[ddpg]]"
  - "[[integrated-sensing-computation-communication]]"
  - "[[prediction-driven-joint-trajectory-beamforming]]"
  - "[[yin-2026-m2llm-trajectory-beamforming]]"
created: 2026-07-14
updated: 2026-07-14
---

# M2LLM State Representation for DRL

Using a fine-tuned multimodal large language model as a feature encoder for a reinforcement-learning controller. Images, sensed positions, and task text are fused by the M2LLM; a hidden representation is projected to a fixed-size numerical state instead of asking generated text to directly control continuous actions.

[[yin-2026-m2llm-trajectory-beamforming]] fine-tunes LLaVA with LoRA on AirSim data and feeds the projected last hidden layer to DDPG. The approach separates multimodal perception and prediction from continuous trajectory/beam control.

A fixed-size input representation does not automatically solve variable-size action spaces, physical consistency, or out-of-distribution robustness. The cited evaluation is simulation-only and supplies no injectivity or generalization proof for the hidden state.
