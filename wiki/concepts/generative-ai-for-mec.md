---
type: concept
title: Generative AI for MEC (GAI-MEC)
tags: [gai, llm, gdm, mec, beamforming, semantic-communication]
related:
  - "[[mobile-edge-computing]]"
  - "[[wang-2025-lae-network-survey]]"
  - "[[mobile-aigc-network]]"
  - "[[xu-2024-mobile-aigc-survey]]"
created: 2026-05-28
updated: 2026-05-31
---

# Generative AI for MEC (GAI-MEC)

The application of **generative AI** — large language models (LLMs), diffusion models (GDMs), GANs — to the optimization, control, and service layer of MEC systems. Distinct from *running* generative AI as an offloaded workload (which is also active research).

## Where GAI fits in MEC

| Use case | Generative tool | Benefit |
|---|---|---|
| **Channel prediction** | GDMs / GANs | Generate plausible channel realizations from sparse observations |
| **Beamforming** | GAI-augmented optimization | Sample candidate beam patterns; refine with classical methods |
| **Semantic communication** | LLMs / diffusion encoders | Transmit *meaning* not bits, reducing bandwidth |
| **Trajectory planning** | GAI + DRL hybrids | Generate diverse candidate trajectories; evaluate with classical RL |
| **Digital twin synthesis** | GDMs | Hallucinate plausible airspace / scene reconstructions |
| **Prompt-based control** | LLMs | Convert high-level mission specs to control programs |

## Why this is showing up now

- LLM / diffusion model inference is finally cheap enough to run at the edge or via a thin cloud-edge handoff.
- The classical optimization stack hits diminishing returns; sample-and-refine is more flexible than fixed analytical solvers.
- Semantic compression aligns naturally with generative encoders: send only what the receiver can't reconstruct.

## In this wiki

[[wang-2025-lae-network-survey]] surveys this thread under "GAI-driven Computing" and "GAI-driven MEC and Cloud-Edge-End Collaboration". The distinct but adjacent thread of *serving* generative AI as the edge workload — **mobile AIGC networks** — is surveyed by [[xu-2024-mobile-aigc-survey]] (see [[mobile-aigc-network]]).

## Open questions

- What's the right cost model for GAI at the edge? Inference latency vs cloud round-trip vs accuracy.
- Privacy: GAI models trained on pooled data may leak; federated training (cf. [[federated-reinforcement-learning]]) is the natural answer.
- Hallucination tolerance — for control loops, hallucinated channel predictions are catastrophic.
