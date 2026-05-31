---
type: concept
title: "Knowledge Distillation for DRL (Policy Distillation)"
tags: [drl, model-compression, distillation, edge-inference]
related:
  - "[[ppo]]"
  - "[[chen-2024-thoas-traffic-aware-sagin]]"
created: 2026-05-29
updated: 2026-06-01
---

# Knowledge Distillation for DRL (Policy Distillation)

Compressing a converged deep DRL policy (the "teacher") into a much smaller, shallower network (the "student") by training the student to match the teacher's temperature-softened action distribution via a KL-divergence loss. The goal is to cut inference cost so the policy can run on resource-constrained platforms (here, low-power satellites and UAVs) without retraining from scratch.

In the wiki, [[chen-2024-thoas-traffic-aware-sagin]] distills its converged [[ppo]] offloading policy into a lightweight student: at ~6% of teacher size it retains ~73% performance, ~90% at 12%, ~97% at 50%. It brings on-platform model-size constraints into the corpus as a first-class design concern for SAGIN edge inference (cf. the DNN-pruning angle in [[niazmand-2025-jopa-dnn-pruning-iiot]]).
