---
type: concept
title: Markov Game of Intervention (MGI) for Collision Avoidance
tags: [game-theory, safe-rl, multi-agent, uav]
related:
  - "[[safe-reinforcement-learning]]"
  - "[[zhang-2025-ssac-mgi-heterogeneous-uav]]"
created: 2026-05-28
updated: 2026-06-01
---

# Markov Game of Intervention (MGI) for Collision Avoidance

A **per-UAV** two-agent safe-RL design introduced in [[zhang-2025-ssac-mgi-heterogeneous-uav]] to keep UAVs from colliding with other UAVs or obstacles. Rather than folding safety into the reward (reward shaping), MGI controls each UAV with two cooperating agents and a gating policy that decides, slot by slot, which one acts:

- **Standard Agent.** A stochastic, reward-maximizing policy $\pi$ that pursues the mission objective — minimizing job miss rate and the average energy of UAVs and UEs.
- **Safety Agent.** A risk-averse policy $\pi^{\mathrm{safe}}$ paired with a **binary gating/intervention policy** $\mathbf{g}(s_t)\in\{0,1\}$ that prevents unsafe actions.

## Mechanism

At each step the executed action is a gated switch between the two agents:

$$\tilde a_t = \mathbf{g}(s_t)\cdot a_t^{\mathrm{safe}} + (1-\mathbf{g}(s_t))\cdot a_t.$$

When the gate triggers ($\mathbf{g}(s_t)=1$) the Safety Agent's action **overrides** the Standard Agent; otherwise the Standard Agent follows its stochastic policy. The Standard Agent's reward is likewise assigned according to whichever action was actually executed, so it learns to maximize return *under the influence of* the Safety Agent. The Safety Agent's objective trades off minimizing unsafe-action risk against avoiding excessive interference with the Standard Agent (each intervention is discouraged), so overrides stay selective.

This decoupling — reward maximization in the Standard Agent, safety enforcement in the Safety Agent — is what gives MGI safety guarantees **during and after** training, unlike reward-shaping baselines where a single policy must balance both. The two-agent model is formalized as a two-agent Dec-POMDP and solved jointly with the SSAC backbone (see [[zhang-2025-ssac-mgi-heterogeneous-uav]]).

## Trade-offs and scope

- The gating policy must learn *when* to intervene; too-frequent overrides interfere with the mission objective, too-rare ones admit unsafe actions — hence the intervention cost in the Safety Agent's objective.
- Evaluated for UAV-UAV and UAV-obstacle avoidance at a **constant flight altitude** (2-D planning over a $500\times500$ grid); full 3-D maneuvering is not modeled.
- Belongs to the broader [[safe-reinforcement-learning]] family of constraint-enforcing (rather than reward-shaping) approaches.
