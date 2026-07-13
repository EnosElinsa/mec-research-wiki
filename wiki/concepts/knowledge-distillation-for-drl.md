---
type: concept
title: "Knowledge Distillation for DRL (Policy Distillation)"
tags: [drl, model-compression, distillation, edge-inference]
related:
  - "[[ppo]]"
  - "[[chen-2024-thoas-traffic-aware-sagin]]"
  - "[[wang-2026-llm-qos-multiuav-resource]]"
  - "[[llm-assisted-mec-optimization-control-plane]]"
  - "[[xu-2026-mrlmn-llm-multihop]]"
created: 2026-05-29
updated: 2026-07-14
---

# Knowledge Distillation for DRL (Policy Distillation)

Compressing a converged deep DRL policy (the "teacher") into a much smaller, shallower network (the "student") by training the student to match the teacher's temperature-softened action distribution via a KL-divergence loss. The goal is to cut inference cost so the policy can run on resource-constrained platforms (here, low-power satellites and UAVs) without retraining from scratch.

In the wiki, [[chen-2024-thoas-traffic-aware-sagin]] distills its converged [[ppo]] offloading policy into a lightweight student: at ~6% of teacher size it retains ~73% performance, ~90% at 12%, ~97% at 50%. [[wang-2026-llm-qos-multiuav-resource]] uses the teacher-student idea at the policy-generation level: a cloud-side LLM teacher produces expert resource-allocation policies that are distilled into MAPPO UAV students. This teacher-policy variant is one branch of [[llm-assisted-mec-optimization-control-plane]]. These entries bring on-platform model-size and execution constraints into the corpus as first-class design concerns for SAGIN and UAV-edge inference (cf. the DNN-pruning angle in [[niazmand-2025-jopa-dnn-pruning-iiot]]).
