---
type: concept
title: "Meta Deep Reinforcement Learning"
tags: [drl, meta-learning, transfer-learning, adaptation]
related:
  - "[[td3]]"
  - "[[episodic-experience-replay]]"
  - "[[low-altitude-intelligent-network]]"
  - "[[ye-2026-meta-deepesc-lae-isac]]"
created: 2026-07-07
updated: 2026-07-07
---

# Meta Deep Reinforcement Learning

Meta-DRL trains a policy or initialization across a distribution of related tasks so it can adapt to a held-out task with fewer samples. In this wiki the task distribution is not a set of games; it is a set of LAE ISAC flight periods with different episode lengths and target/UAV trajectories.

[[ye-2026-meta-deepesc-lae-isac]] uses a TD3-style controller as the base learner and adds meta-learning through dynamic task weighting plus meta-parameter smoothing. The practical aim is rapid adaptation when the LAE flight period changes, while keeping the sensing-SNR, mission-completion, collision-avoidance, and transmit-power constraints satisfied.

Meta-DRL should be read here as a sample-efficiency and generalization device rather than a separate architecture class. The underlying action space remains continuous UAV trajectory and GBS beamforming control, linked to [[td3]] and [[episodic-experience-replay]].
