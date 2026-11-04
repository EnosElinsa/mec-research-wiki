---
type: source
title: "Hybrid Actor-Critic Reinforcement Learning in Parameterized Action Space"
authors: ["Zhou Fan", "Rui Su", "Weinan Zhang", "Yong Yu"]
year: 2019
url: "not in parse"
venue: "Proceedings of the Twenty-Eighth International Joint Conference on Artificial Intelligence (IJCAI-19)"
modeling_card: not_applicable
tags: [source, parameterized-action-space, hybrid-actor-critic, ppo, hybrid-action, foundational-method]
related:
  - "[[hybrid-action-decision-making]]"
  - "[[ppo]]"
  - "[[parameterized-dqn]]"
  - "[[j-ppo]]"
  - "[[li-2022-hyar-hybrid-action-representation]]"
created: 2026-11-02
updated: 2026-11-02
---

# Hybrid Actor-Critic Reinforcement Learning in Parameterized Action Space

## Citation

Fan, Z., Su, R., Zhang, W., & Yu, Y. (2019). *Hybrid Actor-Critic Reinforcement Learning in Parameterized Action Space*. **Proceedings of IJCAI-19**. DOI not in parse.

## TL;DR

For actions made of a discrete choice plus continuous parameters, the paper uses parallel sub-actors: a discrete actor picks the action type and a continuous actor outputs Gaussian parameters, both guided by one shared critic. The PPO-based instance, H-PPO, beats earlier parameterized-action methods on four tasks.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Fan et al. [x] proposed a hybrid architecture of actor-critic algorithms for reinforcement learning in parameterized action space. The architecture consists of multiple parallel sub-actor networks that decompose the structured action space into simpler action spaces, together with a critic network that guides the training of all sub-actors. A discrete actor learns a stochastic policy over discrete actions and a continuous actor learns Gaussian policies over their continuous parameters, and the two are updated separately at each step. They presented an instance based on proximal policy optimization, called hybrid proximal policy optimization, and noted that the architecture extends to more general hierarchically structured action spaces. Experiments on a collection of parameterized-action tasks show that it outperforms previous methods, including parameterized DDPG and P-DQN.

## Scope and method

Tasks are Catching Point, Moving, Chase and Attack, and Half Field Football. The method is a general RL architecture without an application-specific decision model.

## Key findings

- H-PPO outperforms the compared parameterized-action baselines on the four tasks.
- Separate discrete and continuous actors simplify learning compared with one joint actor.

## Limitations / future work

The authors note the architecture can extend to other hierarchical action spaces.

## Relation to the corpus

A parallel-actor baseline for [[hybrid-action-decision-making]], related to [[j-ppo]] designs in UAV-MEC and contrasted with [[parameterized-dqn]] and the latent approach of [[li-2022-hyar-hybrid-action-representation]].

## Raw artifacts

- Parse: `raw/sources/Hybrid Actor-Critic Reinforcement Learning in Parameterized Action Space/fan2019ijcai.md`
- Origin PDF is in the same folder.
