---
type: concept
title: "Interference-Aware DBSCAN Pilot Assignment"
tags: [clustering, dbscan, pilot-assignment, pilot-contamination, cell-free-massive-mimo]
related:
  - "[[shah-2026-cellfree-mimo-fap-control]]"
  - "[[aerial-terrestrial-cell-free-massive-mimo]]"
  - "[[csi-estimation-error]]"
  - "[[k-dbscan-uav-deployment]]"
created: 2026-07-13
updated: 2026-07-13
---

# Interference-Aware DBSCAN Pilot Assignment

A pilot-reuse pipeline that first forms Euclidean-distance DBSCAN clusters, assigns distinct pilots within each cluster where possible, and splits oversized clusters. It then detects cross-cluster users sharing both a pilot and serving FAP and re-associates one conflicting user to a nearest FAP without that pilot conflict.

In [[shah-2026-cellfree-mimo-fap-control]], the method follows trajectory/power and FAP-user association optimization. Its implemented interference awareness lies in post-clustering conflict repair, despite stronger abstract language suggesting interference enters clustering itself. It remains a heuristic whose outcome depends on DBSCAN radius, minimum-sample settings, association geometry, and the available pilot count.
