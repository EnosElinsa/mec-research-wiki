---
type: query
title: "Is end-to-end DRL feasible in large-scale multi-UAV MEC?"
created: 2026-05-31
updated: 2026-05-31
tags: [drl, end-to-end, scalability, research-gap, open-question]
related: [end-to-end-vs-decomposition-in-drl-mec, action-space-explosion-in-multi-uav-mec, no-true-end-to-end-drl-in-corpus, hybrid-action-decision-making, hybrid-action-memory-augmented-drl-wins-uav-mec, two-stage-decomposition, decomposition-beats-end-to-end-drl-in-mec]
---
# Is end-to-end DRL feasible in large-scale multi-UAV MEC?

## Background

The corpus analysis shows that all current DRL works adopt some degree of decomposition-based design (see [[no-true-end-to-end-drl-in-corpus]]). A truly end-to-end model — a single network from raw observations directly to all decision variables — is entirely absent from the multi-UAV-MEC domain.

## Sub-questions

1. **Can the dimensionality bottleneck be broken?** Can the sequence-modeling capacity of Transformers / large models handle the combinatorial action space of multi-UAV MEC?
2. **Out-of-domain transfer:** Can end-to-end success stories from autonomous driving, multi-robot coordination, and similar domains transfer to MEC?
3. **Theoretical bounds:** Is there a provable performance–efficiency trade-off bound between end-to-end and decomposition-based designs?
4. **The scaling limit of hybrid actions:** How many UAVs can j-PPO / P-DQN-style methods scale to?

## Current evidence

- The corpus's closest-to-end-to-end methods (j-PPO, P-DQN) are validated only in single-agent or small-fleet settings.
- [[action-space-explosion-in-multi-uav-mec|Action-space explosion]] is the core technical obstacle.
- [[two-timescale-optimization|Heterogeneous timescales]] provide a physical motivation for decomposition.
- There is no counterfactual experiment (no record of anyone trying end-to-end and failing).

## Possible research directions

- Transformer-based sequential decision models (Decision Transformer family) applied to MEC.
- Graph-attention networks encoding the UAV–user topology to compress the action space.
- Curriculum learning, scaling gradually from small to large fleets.
- Ablation studies directly comparing end-to-end vs decomposition-based designs.

## Related pages

- [[end-to-end-vs-decomposition-in-drl-mec]]
- [[hybrid-action-memory-augmented-drl-wins-uav-mec]]
- [[drl-vs-evolutionary-vs-classical-solvers]]
