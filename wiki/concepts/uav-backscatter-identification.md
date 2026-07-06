---
type: concept
title: "UAV Backscatter Identification"
tags: [uav, backscatter, identification, sensing]
related:
  - "[[backscatter-communication]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[mmwave-radar-sensing]]"
  - "[[low-altitude-intelligent-network]]"
  - "[[zeng-2026-fmcw-isibc-lae]]"
created: 2026-07-07
updated: 2026-07-07
---

# UAV Backscatter Identification

UAV backscatter identification attaches a low-power backscatter device to an aerial vehicle so the sensing infrastructure can recover an identity-bearing symbol from the reflected radio signal. It fills the gap between passive sensing, which estimates motion but not identity, and active communication, which identifies a UAV but costs more power and may be decoupled from radar sensing.

In [[zeng-2026-fmcw-isibc-lae]], the ground base station sends FMCW chirps and jointly estimates UAV range, radial velocity, and backscatter-device symbols. The BD effectively acts as an electronic identifier for low-altitude economy traffic, connecting [[backscatter-communication]] to [[integrated-sensing-and-communication]] and [[mmwave-radar-sensing]].
