---
type: concept
title: "Sequential Multi-Agent Policy Generation"
tags: [marl, sequential-decision, coordination, action-masking]
related:
  - "[[zhou-2026-a2g-madrl-air-ground-vcs]]"
  - "[[uav-assisted-mobile-crowd-sensing]]"
  - "[[graph-neural-network]]"
  - "[[noma]]"
  - "[[ma-pomdp]]"
  - "[[centralized-training-decentralized-execution]]"
created: 2026-07-11
updated: 2026-07-11
---

# Sequential Multi-Agent Policy Generation

Sequential multi-agent policy generation builds a joint action one agent at a time. Instead of every agent choosing independently from the same observation, later agents condition their action on earlier agents' selected actions, so the policy can capture ordering effects, reduce duplicated effort, and respect shared-resource constraints.

In [[zhou-2026-a2g-madrl-air-ground-vcs]], DOMPG uses this idea for air-ground vehicular crowdsensing. UAVs and UGVs choose route and NOMA channel-assignment actions under a dynamically optimized decision order, and masked cross-attention exposes the already chosen actions to the remaining agents. This matters because a UAV's best PoI/channel choice depends on which UGVs or other UAVs have already taken nearby sensing work.

The pattern is especially useful when the joint action space is large and sparse. It keeps the action representation factorized like a multi-agent policy, but avoids the strongest independence assumption of simultaneous decentralized actions.
