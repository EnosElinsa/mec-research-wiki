---
type: synthesis
title: DRL backbone choices across the UAV-MEC corpus
tags: [synthesis, drl, uav, mec, comparison]
related:
  - "[[liu-2026-jppo-en-convntm]]"
  - "[[peng-2025-drudm-cfg]]"
  - "[[zhang-2025-ssac-mgi-heterogeneous-uav]]"
  - "[[bi-2025-sg-mapg]]"
  - "[[qin-2025-bcuav-masac]]"
  - "[[zhang-2025-mcma-task-migration]]"
  - "[[zhu-2025-lycnn-drl-wpt-mec]]"
  - "[[hao-2025-priority-aware-task-driven-co]]"
  - "[[mao-2025-bcsa-frl]]"
  - "[[xie-2026-uav-multisource-fusion]]"
  - "[[ppo]]"
  - "[[j-ppo]]"
  - "[[masac]]"
  - "[[ddqn]]"
  - "[[hybrid-action-decision-making]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[lyapunov-optimization]]"
  - "[[ma-pomdp]]"
  - "[[design-recipe-multi-uav-mec]]"
created: 2026-05-29
updated: 2026-05-29
---

# DRL backbone choices across the UAV-MEC corpus

A cross-cutting look at *how* the curated sources actually do reinforcement learning. Pulls together the algorithmic choices made in 9 of the 12 curated sources (the 3 outliers — [[wang-2025-uav-swarm-stackelberg]] uses pure game theory, [[xie-2026-uav-multisource-fusion]] uses an evolutionary multi-objective solver, and [[wang-2025-lae-network-survey]] is a survey).

The goal is to make the design space legible: which backbone, which framing, which architectural augmentations, and *why* each choice was made.

## At a glance

| Source | Backbone | Multi-agent? | Framing | Action space | Key augmentation |
|---|---|---|---|---|---|
| [[liu-2026-jppo-en-convntm]] | [[j-ppo|j-PPO]] (modified PPO) | Single (joint controller) | [[pomdp|POMDP]] | Hybrid continuous + discrete | [[en-convntm|EN-ConvNTM]] memory + [[stn|STN]] |
| [[qin-2025-bcuav-masac]] | [[masac|MASAC]] | Multi (per-UAV, per-terminal) | Per-slot decomposed via [[lyapunov-optimization|Lyapunov]] | Continuous (trajectory + power) + DOA for resources | Lyapunov virtual queues |
| [[peng-2025-drudm-cfg]] | MA-DRL (paper-level abstract) | Multi (per-UAV) | [[ma-pomdp|MA-POMDP]] | Hybrid (DRUDM admission + continuous trajectory) | [[adaptive-entropy-priority-replay|AEP replay]] |
| [[zhang-2025-ssac-mgi-heterogeneous-uav]] | SSAC (Shared SAC) | Multi (per-UAV) | MA-POMDP + safe-RL sub-game | Continuous trajectory + admission | [[collision-avoidance-mgi|MGI]] safety constraint |
| [[bi-2025-sg-mapg]] | Multi-agent policy gradient (MAPG) | Multi-tier (BS / UAV / UE) | Stackelberg-MDP hybrid | Mixed (pricing + trajectory + admission) | [[stackelberg-game|Stackelberg]] equilibrium as convergence target |
| [[zhang-2025-mcma-task-migration]] | MADDPG / MAPPO (compatible) | Multi (per-edge-server) | MA-POMDP with [[centralized-training-decentralized-execution|CTDE]] | Two-stage (discrete migration + continuous resource) | [[informer-trajectory-prediction|Informer]] forecast as state input |
| [[zhu-2025-lycnn-drl-wpt-mec]] | CNN actor-critic | Single | Per-slot via Lyapunov + fractional programming | Binary offload + continuous resources | [[fractional-programming-dinkelbach|Fractional programming]] for EE objective |
| [[hao-2025-priority-aware-task-driven-co]] | Hybrid actor (DDPG-style + Q-head) | Single | Event-driven MDP | Hybrid binary + continuous | Dependence-aware **latent space** for variable-size action sets |
| [[mao-2025-bcsa-frl]] | [[ddqn|Double DQN]] | Federated (per-satellite) | MDP (per-satellite local) + FRL aggregation | Discrete (offload destination) | [[ccvm-correction-voting|CCVM]] + [[csra-cold-start-reputation-aggregation|CSRA]] over consensus |

## Backbone choice as a function of action space

The single strongest predictor of backbone choice across the corpus is **what shape the action space has**.

```
Pure discrete                Hybrid                              Pure continuous
(destination, admission)    (trajectory + admission + pricing)  (trajectory, power, resources)
        |                              |                                |
       DDQN                        j-PPO / SSAC                      MASAC / MAPPO
       MAPPO discrete              MADDPG (hybrid)                  MADDPG / TD3
       (FedAvg over agents)        Two-stage (Q + policy-grad)      DDPG actor + KKT
```

- **Pure discrete tasks** ([[mao-2025-bcsa-frl]]'s offload-destination, [[zhang-2025-mcma-task-migration]]'s migration target) lean Q-style. DQN family with FedAvg aggregation when distributed.
- **Pure continuous tasks** ([[qin-2025-bcuav-masac]]'s trajectory + power) lean stochastic-policy actor-critic. MASAC dominates when entropy-driven exploration matters.
- **Hybrid action spaces** are where the design space fragments — there's no single best answer:
  - [[liu-2026-jppo-en-convntm]] modifies the PPO probability ratio itself ([[j-ppo|j-PPO]]).
  - [[hao-2025-priority-aware-task-driven-co]] sidesteps the heterogeneous-action problem with a learned latent space.
  - [[zhang-2025-mcma-task-migration]] decomposes the decision into two stages with different solvers.
  - [[zhu-2025-lycnn-drl-wpt-mec]] decomposes into top (binary, DRL) and sub (continuous, KKT) layers.

## Single-agent vs multi-agent

A clear shift across the corpus:

- **Single-agent joint controller** ([[liu-2026-jppo-en-convntm]], [[zhu-2025-lycnn-drl-wpt-mec]], [[hao-2025-priority-aware-task-driven-co]]) — works when the system size is small and a centralized observer is realistic. Easier to train, easier to reason about. Falls apart at scale.
- **Multi-agent CTDE** ([[peng-2025-drudm-cfg]], [[zhang-2025-mcma-task-migration]], [[zhang-2025-ssac-mgi-heterogeneous-uav]], [[qin-2025-bcuav-masac]], [[bi-2025-sg-mapg]]) — the dominant pattern when:
  - Per-UAV / per-server local observation is what's actually deployable.
  - Joint state / action space is too large for a single network.
  - Agents have *roles* worth learning separately (e.g. heterogeneous UAVs in [[zhang-2025-ssac-mgi-heterogeneous-uav]]).
- **Federated single-agent** ([[mao-2025-bcsa-frl]]) — distinct from MA-DRL: each satellite runs its own MDP locally, then the *parameters* are aggregated across satellites. This is FRL, not MA-DRL.

The wiki's curated corpus does not include any **mean-field MARL** or **value-decomposition (Qmix / VDN)** papers — those scale better past ~20 agents but none of the curated sources hit that count. Worth noting if the corpus grows toward dense LAE deployments.

## Memory and history handling

Three patterns for how the agent gets at the history:

1. **External memory.** [[liu-2026-jppo-en-convntm]]'s [[en-convntm|EN-ConvNTM]] — explicit 3-D memory blocks. Best for very long horizons; expensive at training time.
2. **Future prediction.** [[zhang-2025-mcma-task-migration]]'s [[informer-trajectory-prediction|Informer]] — encodes the *next* H steps instead of the past. Only works when the dynamics admit prediction (vehicles on roads, yes; UAV swarms, partially).
3. **Implicit (state-only).** Most others. Cheap, but leaves performance on the table when long-horizon coupling exists.

There's a clear opening here: a curated source that combines **past memory + future prediction + multi-agent CTDE** doesn't exist yet in the corpus.

## Composition with classical optimization

Three of the strongest results come from sources that **don't** put DRL alone on the critical path:

- [[qin-2025-bcuav-masac]] uses [[lyapunov-optimization|Lyapunov]] for the long-term constraint structure, MASAC for the non-convex sub-block, and DOA for the constrained allocation sub-block.
- [[zhu-2025-lycnn-drl-wpt-mec]] uses [[fractional-programming-dinkelbach|fractional programming]] for the EE objective shape, Lyapunov for time coupling, KKT/Lagrange for the continuous sub-problem, and a CNN actor only for the binary offloading combinatorics.
- [[zhang-2025-mcma-task-migration]] uses Informer for centralized prediction, then MA-DRL only for the per-server decisions.

The pattern: **DRL where the action space is genuinely intractable to enumerate; classical optimization wherever a closed-form-ish solver applies**. Sources that put DRL on every layer ([[peng-2025-drudm-cfg]], [[zhang-2025-ssac-mgi-heterogeneous-uav]]) trade simpler pipelines for slower convergence and noisier per-step decisions.

## On stability vs sample efficiency

Reading across the sources, two backbones dominate:

- **PPO / j-PPO / MAPPO.** Preferred when training stability and on-policy reasoning matter, and when the action space includes a discrete component that benefits from clipped trust regions.
- **SAC / MASAC / SSAC.** Preferred when sample efficiency matters more (off-policy + replay buffer) and when entropy-driven exploration is needed because the cooperative reward landscape has bad local equilibria.

Specific gotchas the corpus surfaces:

- **MADDPG underperforms MASAC** in [[qin-2025-bcuav-masac]]'s evaluation. The deterministic policy collapses on multi-objective rewards. (This echoes general MARL findings.)
- **DDPG / TD3 / DQN underperform [[j-ppo|j-PPO]]+EN-ConvNTM** in [[liu-2026-jppo-en-convntm]]'s evaluation specifically because they can't represent hybrid actions cleanly — see [[hybrid-action-beats-pure-drl]].

## Practical recommendations distilled from the corpus

If you're building a UAV-MEC controller from scratch, the corpus suggests:

1. **Frame as MA-POMDP first.** Even if you start single-agent, the framing forces you to acknowledge partial observation and prepares you for scaling up.
2. **Pick by action space, not by trend.**
   - Pure discrete → DDQN / Dueling-DQN family.
   - Pure continuous → SAC / TD3.
   - Hybrid → either j-PPO-style ratio modification or two-stage decomposition. Avoid threshold-on-continuous-actor (DDPG with thresholding) — the corpus shows this loses on every metric.
3. **Use Lyapunov for long-term constraints, not reward shaping.** Reward shaping is unreliable; virtual queues give you tunable optimality–violation tradeoffs and compose cleanly with DRL.
4. **Add memory only when horizon coupling is provably significant.** EN-ConvNTM-style modules pay for themselves only when long history actually matters.
5. **Consider classical sub-solvers for convex sub-blocks.** A KKT solver for the continuous resource allocation is more reliable than asking DRL to learn convexity from scratch.
6. **Reserve safe-RL machinery for hard constraints.** Reward penalties don't guarantee safety. Use [[collision-avoidance-mgi|MGI]]-style asymmetric intervention or shielding when collisions / energy depletion are catastrophic.

These compound into the [[design-recipe-multi-uav-mec|design recipe]] — extended now with the cross-source evidence above.

## Open question for the next pass

The corpus has zero **transformer-as-policy** sources. Recent literature outside the corpus uses transformer-based actors with success on long-horizon multi-agent control. A curated transformer-policy paper would let us answer [[query-does-en-convntm-generalize-beyond-uav-mec]] more directly — does the explicit external memory in EN-ConvNTM still beat a parameter-matched transformer once both are tuned?
