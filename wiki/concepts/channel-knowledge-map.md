---
type: concept
title: "Channel Knowledge Map"
tags: [channel-knowledge-map, radio-map, low-altitude-economy, environment-aware-communication]
related:
  - "[[radio-map-assisted-channel-estimation]]"
  - "[[radio-map-aided-uav-path-planning]]"
  - "[[low-altitude-intelligent-network]]"
  - "[[rong-not-in-parse-3dckmdiff]]"
  - "[[li-2025-ckm-air-corridor-isac-bs-deployment]]"
created: 2026-11-02
updated: 2026-11-02
---

# Channel Knowledge Map

A channel knowledge map (CKM) is a location-indexed database of channel information, such as path gain, LoS state, or angles, that gives a network a prior on the channel at a position before measuring it there. For low-altitude networks the map must cover 3-D airspace rather than a ground plane, and it is usually built from sparse samples.

## In this wiki

- **Construction.** [[rong-not-in-parse-3dckmdiff]] completes a 3-D CKM from sparse slice measurements by solving an inverse problem with a 2-D diffusion model trained on the joint distribution of slices.
- **Planning use.** [[li-2025-ckm-air-corridor-isac-bs-deployment]] reads minimum and maximum gains and LoS indicators from CKMs to plan an air corridor and choose ISAC base station sites offline.

Related radio-map pages cover channel estimation ([[radio-map-assisted-channel-estimation]]) and communication-aware path planning ([[radio-map-aided-uav-path-planning]]). The CKM term emphasizes the map as reusable prior knowledge for both communication and sensing.
