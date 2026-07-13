---
type: concept
title: Gauss-Markov Mobility Model
tags: [mobility, simulation, iot]
related:
  - "[[zhan-2026-star-ris-aerial-monitoring]]"
  - "[[jin-2026-skyndn-incentivizer]]"
  - "[[wang-2026-spatiotemporal-leo-channel-prediction]]"
  - "[[wu-2026-sensing-error-uav-scheduling]]"
  - "[[high-density-mobile-device-scenarios]]"
  - "[[liu-2026-jppo-en-convntm]]"
created: 2026-05-28
updated: 2026-07-14
---

# Gauss-Markov (GM) Mobility Model

[[jin-2026-skyndn-incentivizer]] uses a 3-D Gauss-Markov process for UAV speed, direction, and pitch in its dynamic auction environment. [[wang-2026-spatiotemporal-leo-channel-prediction]] uses Gauss-Markov ground-user motion inside a simulator-generated LEO/UAV-RIS channel dataset rather than as a decision model.

A stochastic mobility model where each device's speed and direction are smoothed first-order Markov chains driven by Gaussian noise:

$$
v_{d,n} = \alpha v_{d,n-1} + (1-\alpha)\bar v_{d,n} + \omega_{d,n}\sqrt{1-\alpha^2}
$$

$$
\zeta_{d,n} = \beta \zeta_{d,n-1} + (1-\beta)\bar\zeta_{d,n} + \varphi_{d,n}\sqrt{1-\beta^2}
$$

with positions updated by

$$
x_{d,n} = x_{d,n-1} + \tau v_{d,n-1}\cos\zeta_{d,n-1}, \quad y_{d,n} = y_{d,n-1} + \tau v_{d,n-1}\sin\zeta_{d,n-1}
$$

The coefficients $\alpha, \beta \in [0,1]$ control the *memory* of the model — at $\alpha=0$ devices move IID, at $\alpha=1$ they move deterministically. GM is preferred over Random Walk and Random Waypoint in MEC simulations because it produces smooth, physically plausible trajectories without sudden direction reversals.

[[liu-2026-jppo-en-convntm]] uses GM to drive the 256 IoT devices in the simulation arena (see Section III-A and reference [31]).

[[wu-2026-sensing-error-uav-scheduling]] uses Gauss-Markov speed and direction to move users in its multi-UAV ISAC simulation, while sensing errors alter the beam direction used for communication scheduling.
