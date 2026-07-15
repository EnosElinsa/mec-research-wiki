---
type: concept
title: "Robust Offloading"
tags: [robust-optimization, uncertainty, computation-offloading, csi]
related:
  - "[[csi-estimation-error]]"
  - "[[distributionally-robust-optimization]]"
  - "[[chance-constraint]]"
  - "[[li-2024-robust-bmappo-multiuav-mec]]"
  - "[[uav-trajectory-safety-guarantee-ladder]]"
created: 2026-05-31
updated: 2026-07-14
---

# Robust Offloading

**Robust offloading** builds computation-offloading decisions that guarantee performance under bounded uncertainty rather than assuming perfect knowledge. Three common uncertainty sources are distinguished: **scheduling robustness** (uncertain offloading failures), **channel robustness** (imperfect CSI / channel-estimation error), and **computation robustness** (inaccurate task-complexity or provisioning estimates). The design provides worst-case-style guarantees over the uncertainty set while optimizing the nominal objective (often energy or latency).

## In this wiki

- [[li-2024-robust-bmappo-multiuav-mec]] jointly handles **both** channel uncertainty (imperfect UAV–UE CSI, [[csi-estimation-error]]) and computation uncertainty (bounded task-complexity estimation error) in a multi-UAV-MEC network, minimizing weighted energy with a Beta-policy MAPPO. It is a bounded-uncertainty cousin of the [[distributionally-robust-optimization]] approach (uncertainty over distributions) and the [[chance-constraint]] approach (probabilistic guarantees).
