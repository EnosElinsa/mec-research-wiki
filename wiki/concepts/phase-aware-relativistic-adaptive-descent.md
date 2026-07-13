---
type: concept
title: "Phase-Aware Relativistic Adaptive Descent"
tags: [optimizer, conformal-hamiltonian, aerial-ris, phase-error]
related:
  - "[[feng-2026-aerial-ris-secure]]"
  - "[[environment-state-interactive-attention]]"
  - "[[td3]]"
  - "[[uav-mounted-ris]]"
  - "[[csi-estimation-error]]"
created: 2026-07-14
updated: 2026-07-14
---

# Phase-Aware Relativistic Adaptive Descent

Phase-Aware Relativistic Adaptive Descent (PRAD) maps neural-network optimization to a dissipative conformal-Hamiltonian system, applies a conformal-symplectic discretization with relativistic step limiting, and adjusts momentum from successive-gradient variation. A von-Mises factor corrects RIS-phase gradients for modeled jitter-induced phase noise.

[[feng-2026-aerial-ris-secure]] installs PRAD in the beamforming/phase-control [[td3|TD3]] agent of a two-agent aerial-RIS security controller. Its robustness and convergence gains are simulation-based and depend on the paper's phase-error and CSI models.
