---
type: concept
title: "Implicit Opponent Modeling"
tags: [opponent-modeling, fictitious-self-play, adversarial-rl, partial-observability]
related: ["[[yin-2026-uav-antijamming-nfsp]]", "[[fictitious-self-play]]", "[[stochastic-game]]", "[[unpredictable-uav-trajectory-control]]", "[[navigation-stochastic-control-decomposition]]", "[[uav-trajectory-safety-guarantee-ladder]]"]
created: 2026-07-14
updated: 2026-07-14
---

# Implicit Opponent Modeling

Adapting to another learner without directly observing its private state, action, or policy. In [[yin-2026-uav-antijamming-nfsp]], each UAV/jammer policy mixes a recurrent best response with a supervised historical average policy, so changes in the opponent are inferred from the agent's own observation/action history.
