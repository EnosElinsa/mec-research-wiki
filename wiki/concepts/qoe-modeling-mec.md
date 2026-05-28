---
type: concept
title: "QoE Modeling in MEC"
tags: [qoe, quality-of-experience, reward-shaping, mec]
related:
  - "[[video-analytics-offloading]]"
  - "[[video-transcoding-tradeoff]]"
  - "[[equilibrium-efficiency-metric]]"
  - "[[bao-2025-ddpg-video-offloading]]"
created: 2026-05-29
updated: 2026-05-29
---

# QoE Modeling in MEC

**Quality of Experience (QoE)** is a higher-level service metric than QoS. It captures user-perceived service quality — for video analytics, that's a function of latency *and* accuracy/quality. Modeling QoE means choosing a scalar that captures the tradeoff in a way that matches user preference, not just engineering convenience.

[[bao-2025-ddpg-video-offloading]] uses a typical shape: $QoE = -\alpha \cdot \text{delay} - \beta \cdot (1 - \text{bitrate}/\text{original})$. The weights $\alpha, \beta$ tune how much the policy trades delay for quality.

Why this matters as a reward signal: pure-delay rewards push the policy to over-compress; pure-quality rewards push it to never offload. The QoE form forces a Pareto-aware policy.

Compare with the [[equilibrium-efficiency-metric]] used in [[liu-2026-jppo-en-convntm]], which also encodes a multi-criteria tradeoff (data-collection × fairness / energy) — both are "scalar QoE proxies" tuned to the workload's specific concerns.
