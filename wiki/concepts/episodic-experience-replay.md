---
type: concept
title: "Episodic Experience Replay"
tags: [drl, replay-buffer, sample-efficiency, episode-task]
related:
  - "[[prioritized-experience-replay]]"
  - "[[ddpg]]"
  - "[[td3]]"
  - "[[ye-2026-deeplsc-lae-isac]]"
  - "[[ye-2026-meta-deepesc-lae-isac]]"
created: 2026-07-07
updated: 2026-07-07
---

# Episodic Experience Replay

Replay-buffer design that samples or updates **whole episodes** rather than isolated transitions. It is useful when the reward and feasibility signal are dominated by flight-period constraints: mission completion, average sensing SNR, collision avoidance, or energy efficiency can only be evaluated reliably after the episode unfolds.

In [[ye-2026-deeplsc-lae-isac]], hierarchical experience replay groups all experiences from an episode so the DDPG controller trains on complete LAE ISAC trajectories. In [[ye-2026-meta-deepesc-lae-isac]], episodic experience replay stores complete episode experience sets, assigns them priorities, and samples recent or more uncertain sets more actively.

This is related to [[prioritized-experience-replay]], but the priority unit is not necessarily a single TD-error-heavy transition. The episode itself becomes the sampling object, preserving temporal structure for long-horizon UAV trajectory and beamforming control.
