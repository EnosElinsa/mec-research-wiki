---
type: concept
title: "Privacy-Sensitive Data Partitioning"
tags: [privacy, federated-learning, data-offloading]
related:
  - "[[federated-learning]]"
  - "[[adaptive-inter-layer-data-offloading]]"
  - "[[zero-trust-architecture]]"
  - "[[han-2024-sagin-fl-handover]]"
created: 2026-05-29
updated: 2026-05-29
---

# Privacy-Sensitive Data Partitioning

Splitting each device's dataset into a **privacy-sensitive** part that must stay local and a **non-sensitive** part that may be offloaded to other nodes for processing. A fraction $\alpha = |D^{\text{non-sensitive}}| / |D|$ controls how much data can move. This is the key enabler *and* the key constraint of cross-tier data offloading: larger $\alpha$ gives more flexibility (faster training) while $\alpha = 0$ degenerates to conventional, local-only federated learning.

In the wiki, [[han-2024-sagin-fl-handover]] uses this partition to bound [[adaptive-inter-layer-data-offloading]] across SAGIN tiers, showing time-to-accuracy improves markedly with larger $\alpha$. It is a pragmatic middle ground between full data localization (classic [[federated-learning]]) and unrestricted data sharing, and connects to the corpus's [[zero-trust-architecture]] security thread.
