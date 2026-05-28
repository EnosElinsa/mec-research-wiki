---
type: concept
title: "Interdependent Tasks (DAG)"
tags: [scheduling, dag, dependency, task-graph]
related:
  - "[[task-offloading]]"
  - "[[task-migration]]"
  - "[[makespan-minimization]]"
  - "[[huang-2023-mu-aec-task-energy]]"
created: 2026-05-29
updated: 2026-05-29
---

# Interdependent Tasks (DAG)

A task graph $\mathcal{G} = (\mathcal{V}, \mathcal{E})$ where each node is a sub-task and each edge $(i, l)$ encodes a precedence constraint: task $i$ must finish (and transmit its output to $l$) before task $l$ can start. Common in real applications — face recognition, vehicular navigation, augmented reality — where Alibaba's data trace shows >75% of applications contain interdependent tasks.

Why this matters for offloading: scheduling decisions are no longer independent per task. If task $l$ runs on UAV B but its predecessor task $i$ ran on UAV A, the intermediate data $M_{i,l}$ must transit between the UAVs — an additional cost. The optimizer has to consider the **assignment graph** plus the dependency graph together.

The wiki's DAG-aware source is [[huang-2023-mu-aec-task-energy]], which uses a custom genetic operator that respects predecessor ordering during crossover and mutation. Standard scheduling literature also uses HEFT (Heterogeneous Earliest Finish Time) and its variants for the same problem; the wiki doesn't currently have an HEFT-based source for direct comparison.
