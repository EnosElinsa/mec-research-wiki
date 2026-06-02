---
type: finding
title: "No true end-to-end DRL model exists in the corpus"
created: 2026-05-31
updated: 2026-05-31
tags: [drl, end-to-end, decomposition, research-gap]
related: [end-to-end-vs-decomposition-in-drl-mec, action-space-explosion-in-multi-uav-mec, hybrid-action-decision-making, two-stage-decomposition, drl-vs-evolutionary-vs-classical-solvers, decomposition-beats-end-to-end-drl-in-mec]
source: "[[drl-vs-evolutionary-vs-classical-solvers]]"
confidence: high
replicated: null
---
# No true end-to-end DRL model exists in the corpus

## Finding

A systematic review of the curated papers in the wiki corpus finds **no work that uses a truly end-to-end DRL model** — i.e. a single neural network mapping raw observations directly to all decision variables with no explicit problem-structure prior.

## Evidence

Every DRL work exploits the decomposable structure of the problem to some degree:

- The **closest-to-end-to-end** works (j-PPO, P-DQN, [[hao-2025-priority-aware-task-driven-co]]) use a single policy network to emit hybrid actions, but are limited to single-agent or low-dimensional settings, and their effectiveness implicitly depends on the "discrete decisions dominate structure, continuous decisions conditionally convex" property.
- **Multi-agent joint-action** methods ([[li-2024-robust-bmappo-multiuav-mec|b-MAPPO]], [[seid-2021-madrl-multiuav-iot-edge|MADDPG]]) rely on the structured information sharing of the CTDE framework.
- **Mainstream** methods use explicit decomposition, with different sub-problems solved by different solvers ([[li-2025-twohop-airground-drl-offloading|JPTORAUTD]], [[nabi-2025-jour-hierarchical-aerial|matching+SAC]]).

## Confidence

**High.** Based on a systematic comparison across many parsed papers in the corpus, with broad coverage. One caveat: there is no counterfactual experiment (no record of anyone trying an end-to-end model and failing), so "whether end-to-end is feasible" remains an open question.

## Significance

This finding itself identifies an important research gap: the feasibility of end-to-end DRL in large-scale multi-UAV MEC, and its performance–efficiency trade-off against decomposition-based methods, has not been explored. See [[end-to-end-drl-feasibility-large-scale-mec]].

## See also

- [[end-to-end-vs-decomposition-in-drl-mec]] — the full conceptual analysis
- [[hybrid-action-beats-pure-drl]] — a complementary finding on the effectiveness of hybrid actions
