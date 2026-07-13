---
type: concept
title: "Graph Neural Network (GNN)"
tags: [graph-neural-network, machine-learning, resource-allocation, graph-theory, scalability]
related:
  - "[[graph-based-resource-management]]"
  - "[[drl-backbones-across-uav-mec-sources]]"
  - "[[dai-2024-graph-rm-survey-learning]]"
  - "[[dai-2024-graph-rm-survey-optimization]]"
  - "[[li-2026-cdto-inland-waterways]]"
  - "[[teng-2026-gstrl-sequential-offloading]]"
  - "[[sequential-task-offloading]]"
  - "[[zhan-2026-gatd3qn-dependent-offloading]]"
  - "[[wang-2026-llm-qos-multiuav-resource]]"
  - "[[he-2026-lscr-uav-relay-tracking]]"
  - "[[target-graph-representation]]"
  - "[[zhou-2026-a2g-madrl-air-ground-vcs]]"
  - "[[sequential-multi-agent-policy-generation]]"
  - "[[zhou-2026-multiscale-dt-uav-delivery]]"
  - "[[xie-2026-geoagg-hsac]]"
  - "[[liao-2026-semantic-twinning-tracking]]"
  - "[[tang-2026-gat-antijamming]]"
  - "[[lu-2026-multiuav-iscpt]]"
  - "[[ye-2023-graph-uav-coverage]]"
created: 2026-06-03
updated: 2026-07-13
---

# Graph Neural Network (GNN)

A graph neural network is a learning architecture that operates directly on graph-structured data, following a graph-in / graph-out template: each node iteratively aggregates ("message passes") features from its neighbors and updates its own representation, so the learned function respects the graph's connectivity. In wireless networks, GNNs are applied to resource-management problems by mapping the network onto a graph (see [[graph-based-resource-management]]) and learning a policy over it.

## Why GNNs for resource management

Per [[dai-2024-graph-rm-survey-learning]], GNNs are attractive for wireless resource management because of four stated properties:

- **Scalability** — the parameter count is independent of network size, so a model trained on a small network can run on a larger one.
- **Training efficiency** on wireless-network data.
- **Generalization** to dynamic network status, via permutation invariance/equivariance.
- **Compatibility** with existing graph models.

## Hybridization patterns

The survey highlights two recurring designs: combining GNNs with **classical iterative algorithms** (to get learning's efficiency with iteration's accuracy) and coupling GNNs with **reinforcement-learning** frameworks (to handle dynamic, random wireless environments) — connecting to the corpus's heavy [[drl-backbones-across-uav-mec-sources|DRL-for-MEC]] literature. The survey traces the lineage from Eisen and Ribeiro's first use of GNNs for link/multiple-access scheduling through demonstrations that GNNs converge faster and generalize better than MLPs at large scale.

## In the corpus

This is the corpus's primary anchor for the GNN concept; it is introduced and reviewed in [[dai-2024-graph-rm-survey-learning]] (the learning half) and motivated by the scaling limits of graph optimization laid out in [[dai-2024-graph-rm-survey-optimization]]. [[li-2026-cdto-inland-waterways]] provides a task-offloading example where a topology-aware GNN represents D2D links among USVs for multi-agent offloading decisions. [[teng-2026-gstrl-sequential-offloading]] uses a heterogeneous graph neural network to encode UAVs, requesting tasks, offloaded tasks, and dynamic U2U/task edges for [[sequential-task-offloading]]. [[zhan-2026-gatd3qn-dependent-offloading]] uses graph attention over task DAGs before D3QN offloading, while [[wang-2026-llm-qos-multiuav-resource]] uses relation-aware GAT inside an LLM teacher for QoS-aware multi-UAV resource allocation. [[he-2026-lscr-uav-relay-tracking]] shows a sensing-side use: a lightweight GRCN extracts [[target-graph-representation]] features for multi-UAV target handover. [[zhou-2026-a2g-madrl-air-ground-vcs]] adds an air-ground VCS use: HVGCN encodes UAV, UGV, and PoI interactions before [[sequential-multi-agent-policy-generation]] assigns routes and NOMA channels.

Three physical-state uses broaden the graph role. [[xie-2026-geoagg-hsac]] contrastively aggregates terrain-occlusion-equivalent network states, [[liao-2026-semantic-twinning-tracking]] predicts missing SINR from a UAV electromagnetic graph, and [[tang-2026-gat-antijamming]] maps desired/interfering/jamming channels directly to beamformers.
