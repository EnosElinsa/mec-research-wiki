---
type: concept
title: "Constraint Violation Evaluation (CVE)"
tags: [constrained-optimization, evolutionary-algorithm, constraint-handling]
related:
  - "[[wang-acve-constraint-violation-cmop]]"
  - "[[constrained-multi-objective-evolutionary-algorithm]]"
  - "[[dual-population-evolutionary-algorithm]]"
  - "[[infeasible-individual-utilization]]"
created: 2026-05-29
updated: 2026-05-29
---

# Constraint Violation Evaluation (CVE)

In constrained multiobjective evolutionary optimization, a **constraint violation evaluation** framework quantifies how badly a solution violates the constraints; this value, combined with a **constraint handling technique (CHT)**, drives selection. How CVE is computed strongly affects how effectively constraint information is exploited, yet it has received less attention than CHTs.

[[wang-acve-constraint-violation-cmop]] proposes **adaptive CVE (ACVE)**: cluster solutions, reassign each cluster a constraint-violation value, and adapt the number of clusters to the evolutionary state, using constraint information at different granularities to better balance constraint satisfaction against objective optimization. CVE is the constraint-handling counterpart to the broader [[constrained-multi-objective-evolutionary-algorithm]] machinery used across the wiki's CMOP lineage.
