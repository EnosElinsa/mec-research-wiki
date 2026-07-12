---
type: concept
title: "Softmax Deep Double Deterministic Policy Gradients (SD3)"
tags: [drl, actor-critic, continuous-action, twin-critic, softmax]
related:
  - "[[td3]]"
  - "[[ddpg]]"
  - "[[fujimoto-2018-td3-actor-critic]]"
  - "[[peng-2023-dual-domain-eh-ris]]"
created: 2026-07-13
updated: 2026-07-13
---

# Softmax Deep Double Deterministic Policy Gradients (SD3)

SD3 is an off-policy continuous-control actor-critic method that modifies [[td3|TD3]]'s twin-critic target. TD3 takes the smaller of two target critics to suppress the value overestimation seen in [[ddpg|DDPG]], but a strict minimum can introduce systematic underestimation. SD3 applies a softmax expectation to the clipped minimum-Q estimates of sampled nearby target actions, seeking a less biased target while retaining twin critics, replay, target networks, and clipped action-space smoothing.

In [[peng-2023-dual-domain-eh-ris]], SD3 controls the harvesting time, access-point powers, RIS-element scheduling, and phase shifts of a UAV-mounted surface. The paper compares it with TD3, DDPG, and exhaustive search and reports that its main gain comes from combining the controller with dual-domain harvesting; SD3 does not learn the UAV placement itself.
