---
type: concept
title: "AirComp-Assisted Asynchronous Federated Learning"
tags: [federated-learning, over-the-air-computation, uav-swarm, model-staleness]
related:
  - "[[huang-2026-aircomp-uav-swarms-afl]]"
  - "[[over-the-air-computation]]"
  - "[[federated-learning]]"
  - "[[autonomous-uav-swarms]]"
  - "[[du-2024-distributed-foundation-models-6g]]"
created: 2026-07-11
updated: 2026-07-11
---

# AirComp-Assisted Asynchronous Federated Learning

AirComp-assisted asynchronous federated learning combines two acceleration ideas for wireless FL: asynchronous aggregation avoids waiting for every client, while [[over-the-air-computation]] lets multiple selected clients transmit model updates simultaneously so the channel directly computes an aggregate.

The UAV-swarm version in [[huang-2026-aircomp-uav-swarms-afl]] makes the coupling concrete. Sensing UAVs collect data and train local models, communication UAVs act as parameter servers, and AirComp aggregation is constrained by signal distortion and beamforming power. Because AirComp superposes updates, the server cannot easily inspect each client's stale update, so the paper moves staleness handling to the UAV side: a selected UAV compares local and global layers by cosine similarity and uploads only layers that remain close enough to the current global model.

The concept sits between [[federated-learning]] and swarm networking. It is not only a communication shortcut; the aggregation schedule, receive beamforming, and staleness rule jointly decide which UAV data actually influences the global model.
