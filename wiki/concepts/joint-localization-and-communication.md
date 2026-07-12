---
type: concept
title: "Joint Localization and Communication"
tags: [localization, communication, aoa, cooperative-beamforming, emergency-network, cross-function-optimization]
related:
  - "[[tian-2026-joint-localization-communication]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[collaborative-beamforming]]"
  - "[[air-ground-integrated-network]]"
  - "[[uav-trajectory-control]]"
  - "[[post-disaster-mec]]"
  - "[[xie-2026-geoagg-hsac]]"
created: 2026-07-13
updated: 2026-07-13
---

# Joint Localization and Communication

Joint localization and communication closes a feedback loop between position estimation and data delivery. Better measurement geometry improves the user estimate, a better estimate sharpens directional beamforming, and the communication/energy outcome can then guide the next sensing geometry or platform position.

[[tian-2026-joint-localization-communication]] uses one UAV and one ground rescuer to estimate four AOA components from a distress signal, solve for the person's position, and steer cooperative downlink beams. A DDQN controller adjusts UAV position, movement time, and powers from the combined communication-localization-energy utility.

[[xie-2026-geoagg-hsac]] extends the loop to multiple mountainous UAV base stations and users. Two-way ranging and GDOP determine localization utility, while terrain-aware graph aggregation supports hybrid control of 3-D motion, transmit power, and association under LoS blockage and inter-UAV interference.

The concept is adjacent to [[integrated-sensing-and-communication]] but is not automatically radar ISAC. Its sensing input may be a communication or distress signal, and the localization and data-transfer phases can use separate processing while still being optimized together.
