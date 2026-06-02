---
type: thesis
title: "Decomposition-based solvers beat end-to-end DRL for joint MEC optimization"
confidence: medium
status: supported
tags: [drl, decomposition, end-to-end, design, mec]
related:
  - "[[no-true-end-to-end-drl-in-corpus]]"
  - "[[end-to-end-vs-decomposition-in-drl-mec]]"
  - "[[discrete-continuous-two-stage-decomposition]]"
  - "[[two-stage-decomposition]]"
  - "[[action-space-explosion-in-multi-uav-mec]]"
  - "[[hybrid-action-beats-pure-drl]]"
  - "[[drl-vs-evolutionary-vs-classical-solvers]]"
  - "[[drl-backbones-across-uav-mec-sources]]"
  - "[[end-to-end-drl-feasibility-large-scale-mec]]"
  - "[[lyapunov-guided-drl]]"
created: 2026-06-04
updated: 2026-06-04
---

# Decomposition-based solvers beat end-to-end DRL for joint MEC optimization

## Statement

For joint task-offloading + resource-allocation + trajectory problems in the MEC corpus, a **decomposition-based** design — split the problem into sub-blocks (discrete vs continuous, long-term vs per-slot, convex vs non-convex) and solve each with the tool its structure invites — outperforms, and is universally preferred over, a **truly end-to-end** DRL policy that maps raw observations directly to all decision variables with no problem-structure prior. The advantage comes from explicitly exploiting decomposable structure; the more the joint action space explodes (more UAVs, devices, mixed-integer coupling), the more decomposition wins.

This is a stance on **design philosophy**, not a measured benchmark ranking: the corpus shows decomposition is what every effective solver actually does, and explains *why* through the problem's structure — but it does not contain a head-to-head where someone built a genuine end-to-end policy and lost.

## Supporting evidence

- [[no-true-end-to-end-drl-in-corpus]] — a systematic review across the curated DRL papers finds **zero** truly end-to-end models. Every DRL work exploits decomposable structure to some degree (high confidence finding).
- [[end-to-end-vs-decomposition-in-drl-mec]] — lays out *why* decomposition dominates: [[action-space-explosion-in-multi-uav-mec|action-space explosion]] (multi-UAV × multi-user × continuous resources × discrete matching grows the joint action dimension exponentially), heterogeneous timescales, interpretability, and faster convergence.
- [[discrete-continuous-two-stage-decomposition]] and [[two-stage-decomposition]] — the discrete-then-continuous protocol instantiated by [[wang-2026-aerial-marine-msar]] (matching + convex), [[nabi-2025-jour-hierarchical-aerial]] (Gale-Shapley + ESAC), [[jia-2025-dro-uav-hap-mec]] (BWOA + CVX), and [[zhang-2025-mcma-task-migration]] (MAPPO + MADDPG).
- [[lyapunov-guided-drl]] — six sources independently decompose a *temporal* axis (Lyapunov strips long-term constraints, DRL solves the per-slot residual) rather than learning the whole horizon end-to-end.
- [[hybrid-action-beats-pure-drl]] — even the corpus's closest-to-end-to-end designs (j-PPO, P-DQN) win *because* they implicitly exploit the "discrete decisions dominate structure, continuous decisions conditionally convex" property, not because of structure-agnostic end-to-end capacity (analysis in [[end-to-end-vs-decomposition-in-drl-mec]]).
- [[drl-vs-evolutionary-vs-classical-solvers]] — observes that the corpus's *strongest results* come from hybrid pipelines that pick the right solver per sub-block, not from any single-family monolith.

## Status

`supported` — by a high-confidence absence finding ([[no-true-end-to-end-drl-in-corpus]]) plus convergent structural arguments across multiple synthesis pages. Not yet `settled` because:

1. **No counterfactual experiment.** No curated source builds a genuine end-to-end policy and reports it losing to a decomposed one on the same instance — the case is "every effective solver decomposes," not "end-to-end was tried and failed." This is the exact open question in [[end-to-end-drl-feasibility-large-scale-mec]].
2. **The corpus predates the transformer-policy wave.** It has zero transformer-as-policy / Decision-Transformer sources. A large-capacity sequence model might absorb the structure end-to-end and erode the dimensionality argument that underpins this thesis.
3. **"Closest-to-end-to-end" is a spectrum, not a binary.** j-PPO and P-DQN are single-network hybrid policies that already blur the line; the thesis is about *truly* structure-agnostic learning, and the boundary is fuzzy.

## What would refute this

- A curated study that trains a genuinely end-to-end policy (single network, raw observations → all decision variables, no explicit decomposition) and shows it **matches or beats** a decomposition-based solver on the same multi-UAV-MEC instance at comparable compute.
- A transformer / graph-attention policy that scales to the dense (20+ agent, large device count) regime where [[action-space-explosion-in-multi-uav-mec|action-space explosion]] is supposed to make decomposition mandatory, without per-block decomposition.
- A theoretical result bounding the performance–efficiency gap in favor of end-to-end learning above some scale, contradicting the structural argument that decomposition is necessary as the joint action space grows.
