---
type: concept
title: "K-DBSCAN UAV Deployment"
tags: [uav-deployment, clustering, dbscan, fairness]
related:
  - "[[weighted-kmeans-uav-deployment]]"
  - "[[drone-cell-3d-placement]]"
  - "[[uav-trajectory-control]]"
  - "[[lin-2025-energy-effective-ris-multiuav-coverage]]"
created: 2026-07-11
updated: 2026-07-11
---

# K-DBSCAN UAV Deployment

A clustering-before-control strategy for multi-UAV coverage: partition ground terminals into dense service regions, remove outlier terminals, and use each cluster's center/radius to bound a UAV's movement region before DRL trajectory training.

[[lin-2025-energy-effective-ris-multiuav-coverage]] uses K-DBSCAN to give each RIS-assisted UAV a smaller search region and to avoid wasting training steps on sparse outliers. In the reported comparison, TDQN-RIS-K-DBSCAN-Fair achieves higher average energy efficiency than TDQN with K-means or K-means++ clustering, and the parse reports a 59.4% TDQN training-speed improvement from K-DBSCAN.

This differs from [[weighted-kmeans-uav-deployment]], which biases centroids toward important users but still assigns every point geometrically. K-DBSCAN explicitly treats outliers as outside the service set, so it improves local learning efficiency at the cost of leaving some terminals unserved.
