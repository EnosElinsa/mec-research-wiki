---
type: concept
title: "STAR-RIS"
tags: [ris, metasurface, uav, noma, mec]
related:
  - "[[intelligent-reflecting-surface]]"
  - "[[uav-mounted-ris]]"
  - "[[noma]]"
  - "[[mohammadi-2026-star-ris-uav-mec-noma]]"
  - "[[xiao-2025-star-ris-bidirectional-uav-mec]]"
  - "[[active-ris]]"
  - "[[multi-functional-ris]]"
created: 2026-07-07
updated: 2026-07-07
---

# STAR-RIS

A simultaneous transmitting and reflecting reconfigurable intelligent surface is an RIS variant that can serve users on both sides of the surface by controlling transmitted and reflected components. Compared with a conventional reflecting-only [[intelligent-reflecting-surface]], STAR-RIS expands coverage geometry because the surface is not limited to one half-space.

In [[mohammadi-2026-star-ris-uav-mec-noma]], a UAV carries both an MEC server and a STAR-RIS. Under a mode-switching protocol, transmitted STAR-RIS elements support offloading toward the UAV-MEC server, while reflected elements support offloading toward a terrestrial BS-MEC server. The paper couples STAR-RIS phase design with [[noma]], task-bit allocation, transmit power, and [[uav-trajectory-control]].

[[xiao-2025-star-ris-bidirectional-uav-mec]] uses a horizontally mounted STAR-RIS with energy splitting rather than mode switching. It enables a scheduled user to offload task bits bidirectionally to a BS-MEC server and a UAV-MEC server in the same slot, then maximizes system energy efficiency with Dinkelbach/SCA-based block updates.
