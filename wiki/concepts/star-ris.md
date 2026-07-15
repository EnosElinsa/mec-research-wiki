---
type: concept
title: "STAR-RIS"
tags: [ris, metasurface, uav, noma, mec]
related:
  - "[[zhan-2026-star-ris-aerial-monitoring]]"
  - "[[aerial-observation-control-covertness-surveillance-and-monitoring]]"
  - "[[intelligent-reflecting-surface]]"
  - "[[uav-mounted-ris]]"
  - "[[noma]]"
  - "[[mohammadi-2026-star-ris-uav-mec-noma]]"
  - "[[xiao-2025-star-ris-bidirectional-uav-mec]]"
  - "[[active-ris]]"
  - "[[multi-functional-ris]]"
  - "[[meng-2026-fullspace-star-ris-secure]]"
  - "[[full-space-star-ris-uav-trajectory]]"
  - "[[meng-2026-star-ris-uav-energy]]"
  - "[[uav-energy-supplied-star-ris-noma]]"
  - "[[huang-2026-star-ris-nearfield-isac]]"
created: 2026-07-07
updated: 2026-07-14
---

# STAR-RIS

A simultaneous transmitting and reflecting reconfigurable intelligent surface is an RIS variant that can serve users on both sides of the surface by controlling transmitted and reflected components. Compared with a conventional reflecting-only [[intelligent-reflecting-surface]], STAR-RIS expands coverage geometry because the surface is not limited to one half-space.

In [[mohammadi-2026-star-ris-uav-mec-noma]], a UAV carries both an MEC server and a STAR-RIS. Under a mode-switching protocol, transmitted STAR-RIS elements support offloading toward the UAV-MEC server, while reflected elements support offloading toward a terrestrial BS-MEC server. The paper couples STAR-RIS phase design with [[noma]], task-bit allocation, transmit power, and [[uav-trajectory-control]].

[[xiao-2025-star-ris-bidirectional-uav-mec]] uses a horizontally mounted STAR-RIS with energy splitting rather than mode switching. It enables a scheduled user to offload task bits bidirectionally to a BS-MEC server and a UAV-MEC server in the same slot, then maximizes system energy efficiency with Dinkelbach/SCA-based block updates.

[[meng-2026-fullspace-star-ris-secure]] removes the usual fixed-half-space assumption. Its UAV can cross the STAR-RIS plane, so a binary side variable switches reflection/transmission roles while trajectory and robust secrecy coefficients are optimized together. This mobility-dependent role change is captured by [[full-space-star-ris-uav-trajectory]].

[[meng-2026-star-ris-uav-energy]] instead fixes the STAR-RIS and UAV route, using [[uav-energy-supplied-star-ris-noma]] to charge the surface and users before uplink NOMA. Its alternating resource allocator jointly controls energy/information time, user powers, and transmission/reflection coefficients.

In [[zhan-2026-star-ris-aerial-monitoring]], transmission/reflection control delivers camera-captured content rather than intercepting a suspicious radio payload. That observation role is separated in [[aerial-observation-control-covertness-surveillance-and-monitoring]].
