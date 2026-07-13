---
type: concept
title: "LLM-Guided MARL Policy Distillation"
tags: [llm, marl, knowledge-distillation, uav-swarm, policy-learning]
related:
  - "[[xu-2026-mrlmn-llm-multihop]]"
  - "[[task-oriented-grouped-uav-marl]]"
  - "[[connectivity-preserving-uav-behavioral-loss]]"
  - "[[knowledge-distillation-for-drl]]"
  - "[[llm-assisted-resource-allocation]]"
created: 2026-07-14
updated: 2026-07-14
---

# LLM-Guided MARL Policy Distillation

LLM-guided MARL policy distillation converts occasional high-level deployment advice into action targets for decentralized multi-agent policies. A verifier first rejects infeasible advice; agent-to-target matching and directional similarities then transform accepted target positions into soft action distributions learned through a distillation loss.

[[xu-2026-mrlmn-llm-multihop]] queries an offline LLM during training and deploys the distilled UAV policies without the LLM. Its evidence does not isolate language-model reasoning from a simpler heuristic advisor, and the guidance depends on a discretized environment, proprietary model behavior, hand-written verification rules, and prompt details that are not fully reported.
