---
type: concept
title: "Expert-Assisted Anomaly-Aware Tracking"
tags: [uav, active-tracking, embodied-ai, anomaly-detection, human-in-the-loop]
related:
  - "[[li-2026-la4h-uav-active-tracking]]"
  - "[[expert-guided-warm-start-rl]]"
  - "[[knowledge-distillation-for-drl]]"
  - "[[pomdp]]"
  - "[[uav-enabled-its]]"
  - "[[attention-based-uav-target-search]]"
created: 2026-07-10
updated: 2026-07-10
---

# Expert-Assisted Anomaly-Aware Tracking

Expert-assisted anomaly-aware tracking gives a UAV tracker an explicit recovery path for states where ordinary autonomous tracking is likely to fail. In [[li-2026-la4h-uav-active-tracking]], the abnormal states are prolonged occlusion and intense distractor interference. The policy detects those states through cross-modal anomaly cognition, then decides whether to request expert help instead of continuing to act only from its local observation.

The concept is adjacent to [[expert-guided-warm-start-rl]], but the timing is different. Warm-start RL uses expert demonstrations mainly as training data; LA4H makes expert assistance an online action with a cost. The deployability lever is [[knowledge-distillation-for-drl]], because the paper distills a heavier teacher policy into a lighter student policy suitable for onboard execution.
