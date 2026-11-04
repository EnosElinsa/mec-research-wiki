---
type: source
title: "HyAR: Addressing Discrete-Continuous Action Reinforcement Learning via Hybrid Action Representation"
authors: ["Boyan Li", "Hongyao Tang", "Yan Zheng", "Jianye Hao", "Pengyi Li", "Zhen Wang", "Zhaopeng Meng", "Li Wang"]
year: 2022
url: "https://arxiv.org/abs/2109.05490"
venue: "ICLR 2022 (International Conference on Learning Representations)"
modeling_card: not_applicable
tags: [source, hybrid-action-space, action-representation, conditional-vae, td3, foundational-method]
related:
  - "[[hybrid-action-representation]]"
  - "[[hybrid-action-decision-making]]"
  - "[[variational-autoencoder]]"
  - "[[td3]]"
  - "[[parameterized-dqn]]"
  - "[[fan-2019-h-ppo-parameterized-action]]"
  - "[[hao-2024-clp-multiuav-priority-offloading]]"
created: 2026-11-02
updated: 2026-11-02
---

# HyAR: Addressing Discrete-Continuous Action Reinforcement Learning via Hybrid Action Representation

## Citation

Li, B., Tang, H., Zheng, Y., Hao, J., Li, P., Wang, Z., Meng, Z., & Wang, L. (2022). *HyAR: Addressing Discrete-Continuous Action Reinforcement Learning via Hybrid Action Representation*. **ICLR 2022**. arXiv:2109.05490.

## TL;DR

HyAR learns a compact, decodable latent space for hybrid actions: an embedding table represents discrete actions, and a conditional VAE encodes continuous parameters conditioned on the discrete choice. Training the representation to predict environment dynamics keeps it semantically smooth, so a standard continuous-action agent such as TD3 can act in latent space and decode to the original hybrid action.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Li et al. [x] addressed reinforcement learning with discrete-continuous hybrid action spaces, noting that converting them into a homogeneous space by discretization or continualization ignores the underlying structure and causes scalability and approximation problems. They proposed Hybrid Action Representation, which learns a compact and decodable latent representation space for the original hybrid action space. The latent space embeds the dependence between discrete actions and continuous parameters through an embedding table and a conditional variational auto-encoder, and it is trained to be semantically smooth through unsupervised environmental dynamics prediction. The agent then learns its policy with conventional deep reinforcement learning algorithms in the latent space and decodes the embeddings to act in the environment. Evaluations in several hybrid-action environments show that HyAR outperforms previous baselines, especially in high-dimensional action spaces.

## Scope and method

HyAR-TD3 and HyAR-DDPG run a warm-up stage that trains the representation and a training stage that alternates policy learning and representation updates. Benchmarks are Platform, Goal, Hard Goal, Catch Point, and Hard Move. It is a general RL method without an application-specific decision model.

## Key findings

- HyAR consistently outperforms prior hybrid-action algorithms on the benchmarks.
- Its advantage grows as the hybrid action space becomes larger, as in Hard Move.

## Limitations / future work

The representation must be learned before and during policy training, adding a warm-up cost.

## Relation to the corpus

The origin of the latent [[hybrid-action-representation]] reused in [[hao-2024-clp-multiuav-priority-offloading]], an alternative to parameterized heads such as [[parameterized-dqn]] and [[fan-2019-h-ppo-parameterized-action]] for [[hybrid-action-decision-making]].

## Raw artifacts

- Parse: `raw/sources/HyAR Addressing Discrete-Continuous Action Reinforcement Learning via Hybrid Action Representation/li2022iclr.md`
- Origin PDF is in the same folder.
