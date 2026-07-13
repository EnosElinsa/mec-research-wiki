---
type: concept
title: "Meta Deep Reinforcement Learning"
tags: [drl, meta-learning, transfer-learning, adaptation]
related:
  - "[[td3]]"
  - "[[episodic-experience-replay]]"
  - "[[low-altitude-intelligent-network]]"
  - "[[cell-level-mobile-traffic-prediction]]"
  - "[[ye-2026-meta-deepesc-lae-isac]]"
  - "[[ma-not-in-parse-reinforced-traffic-prediction]]"
  - "[[betalo-2026-meta-uav-scheduling]]"
  - "[[mw-mad3pg]]"
created: 2026-07-07
updated: 2026-07-13
---

# Meta Deep Reinforcement Learning

Meta-DRL trains a learner, initialization, or adaptation rule across related tasks so it can handle a held-out task with fewer samples. The adaptation target is source-specific in this wiki: a continuous control policy across LAE-ISAC flight periods in Meta-DeepESC, and a predictor's network structure across heterogeneous cell-traffic traces in RML-TP.

[[ye-2026-meta-deepesc-lae-isac]] uses a TD3-style controller as the base learner and adds meta-learning through dynamic task weighting plus meta-parameter smoothing. The practical aim is rapid adaptation when the LAE flight period changes, while keeping the sensing-SNR, mission-completion, collision-avoidance, and transmit-power constraints satisfied.

[[ma-not-in-parse-reinforced-traffic-prediction]] applies the same adaptation principle to a different target: a value-based meta-learner changes the structure of a DNN base learner for [[cell-level-mobile-traffic-prediction]], then transfers the learned value table to unseen cells. It adapts predictor architecture rather than a continuous control policy.

Meta-DRL should be read here as a sample-efficiency and generalization device rather than a separate architecture class. The underlying learner and adaptation target remain source-specific: continuous UAV trajectory and GBS beamforming control in Meta-DeepESC, and value-table-guided predictor structure selection in RML-TP.

[[betalo-2026-meta-uav-scheduling]] adds [[mw-mad3pg]], where MAML-style inner/outer updates adapt a fairness-aware multi-UAV actor-critic across traffic, sensor-distribution, energy, and channel tasks.
