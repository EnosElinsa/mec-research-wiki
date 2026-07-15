---
type: concept
title: "Proactive Eavesdropping"
tags: [physical-layer-security, surveillance, jamming]
related:
  - "[[physical-layer-security]]"
  - "[[friendly-jamming-uav]]"
  - "[[cooperative-jamming]]"
  - "[[uav-trajectory-control]]"
  - "[[guo-2024-multiuav-proactive-eavesdropping]]"
  - "[[aerial-observation-control-covertness-surveillance-and-monitoring]]"
created: 2026-06-01
updated: 2026-06-01
---

# Proactive Eavesdropping

A legitimate-surveillance technique in which an authorized monitor actively **degrades a suspicious link** so that it can reliably intercept it, rather than passively listening. Passive eavesdropping only succeeds when the eavesdropping channel already beats the suspicious channel; proactive eavesdropping breaks that limitation, most commonly via **cognitive jamming** (a full-duplex monitor jams the suspicious receiver to force the suspicious source to lower its transmission rate into the monitor's decodable range), and also via spoofing relays or pilot contamination.

It inverts the usual [[physical-layer-security]] framing: jamming here serves the *eavesdropper*, not the protected link. In this wiki, [[guo-2024-multiuav-proactive-eavesdropping]] uses multiple full-duplex UAVs to proactively eavesdrop on multiple mobile suspicious UAV links, jointly optimizing per-UAV jamming power and trajectory. Contrast with [[friendly-jamming-uav]] / [[cooperative-jamming]], where jamming protects a legitimate transmission.

[[aerial-observation-control-covertness-surveillance-and-monitoring]] further separates this authorized-interception outcome from activity hiding, camera monitoring, and echo-based tracking.
