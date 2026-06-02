---
type: concept
title: "End-to-End vs Decomposition-Based DRL in MEC"
created: 2026-05-31
updated: 2026-05-31
tags: [drl, end-to-end, decomposition, architecture-design, uav-mec]
related: [two-stage-decomposition, hybrid-action-decision-making, hybrid-action-representation, centralized-training-decentralized-execution, action-space-explosion-in-multi-uav-mec, drl-vs-evolutionary-vs-classical-solvers, design-recipe-multi-uav-mec, two-timescale-optimization, discrete-continuous-two-stage-decomposition, decomposition-beats-end-to-end-drl-in-mec]
---
# End-to-End vs Decomposition-Based DRL in MEC

## Definition

- **End-to-end DRL:** a single neural network maps raw observations directly to all decision variables, with no explicit problem-structure prior. The network learns the problem's structure internally.
- **Decomposition-based DRL:** the joint optimization is split into sub-problems, each solved by a different algorithm or network, with information passed between the modules through defined interfaces.

## A spectrum of "end-to-end-ness"

In the UAV-MEC corpus, DRL methods do not fall into a clean end-to-end-vs-decomposition dichotomy; they sit on a continuous spectrum:

| Degree of end-to-end-ness | Representative methods | Characteristics |
|---|---|---|
| Closest to end-to-end | j-PPO, P-DQN, [[hao-2025-priority-aware-task-driven-co\|Hao 2025]] | single policy network emitting hybrid actions; limited to single-agent or low-dimensional settings |
| Multi-agent joint | b-MAPPO, MADDPG | each agent emits a full action; relies on a centralized critic |
| Explicit decomposition (mainstream) | JPTORAUTD, matching+SAC | different sub-problems use different solvers |

## Why decomposition-based design dominates

1. **[[action-space-explosion-in-multi-uav-mec|Action-space explosion]]:** multi-UAV × multi-user × continuous resources × discrete matching drives the joint action dimension up exponentially.
2. **[[two-timescale-optimization|Heterogeneous timescales]]:** trajectory control (seconds) and resource allocation (milliseconds) are naturally suited to layering.
3. **Interpretability and debugging:** once decomposed, each sub-module can be verified and tuned independently.
4. **Convergence guarantees:** decomposition reduces the non-stationarity of each sub-problem and speeds up training convergence.

## Implicit use of structure

Even the "closest to end-to-end" hybrid-action DRL methods owe their effectiveness to the problem's decomposable nature:

> Discrete decisions dominate the structure (who goes where), while continuous decisions are conditionally convex (resource allocation given a fixed matching).

This means the success of [[hybrid-action-decision-making|hybrid-action methods]] comes precisely from implicitly exploiting problem structure, rather than from genuinely "structure-agnostic" end-to-end learning. This insight explains why [[hybrid-action-beats-pure-drl|hybrid actions beat pure DRL]] — the advantage comes from structure exploitation rather than from end-to-end capacity.

## Design guidance

Considerations when choosing the degree of end-to-end-ness:

- **Small scenario, low action dimension** → a single hybrid-action policy network is viable.
- **Multi-agent, medium scale** → joint actions under a CTDE framework.
- **Large scale, heterogeneous timescales** → explicit decomposition into sub-problems.

## Research gaps

- Is end-to-end DRL feasible in large-scale multi-UAV MEC?
- Is there a theoretical bound describing the performance–efficiency trade-off between end-to-end and decomposition-based designs?
- Can Transformers / large models break through the current dimensionality bottleneck?

## See also

- [[two-stage-decomposition]] — the core scaffold of decomposition-based design
- [[discrete-continuous-two-stage-decomposition]] — the discrete-then-continuous solver protocol
- [[decomposition-beats-end-to-end-drl-in-mec]] — the thesis that decomposition outperforms end-to-end DRL here
- [[drl-backbones-across-uav-mec-sources]] — a classification from the DRL-backbone angle
- [[design-recipe-multi-uav-mec]] — the decision node within the multi-UAV-MEC design recipe
