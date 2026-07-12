---
type: concept
title: "Physical Layer Security (PLS)"
tags: [security, secrecy-rate, eavesdropper, beamforming, jamming]
related:
  - "[[friendly-jamming-uav]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[zero-trust-architecture]]"
  - "[[benaya-2025-aerial-isac-haps]]"
  - "[[collaborative-beamforming]]"
  - "[[sun-2024-imssa-uav-secure-cb]]"
  - "[[wang-2026-secure-lae-uav-scheduling]]"
  - "[[wang-2026-secure-reliable-uav-mec]]"
  - "[[cai-2026-llm-drl-secure-lae-data]]"
  - "[[beishenalieva-2026-secrecy-aware-uav-path-planning]]"
  - "[[wu-2026-secure-split-offloading-ci]]"
  - "[[wu-2025-security-aware-multiuav-service-placement]]"
  - "[[ren-2026-security-aware-vec-td3]]"
  - "[[zhang-2026-air-ground-covert-jamming]]"
  - "[[chen-2026-air-ground-covert]]"
  - "[[ris-assisted-directional-jamming]]"
  - "[[ambient-interference-aided-covertness]]"
  - "[[bayessa-not-in-parse-uav-isac-secure-content-hdrl]]"
  - "[[li-not-in-parse-movable-antenna-pls]]"
  - "[[micro-macro-mobility-security]]"
  - "[[he-not-in-parse-cipc-covert-uav]]"
  - "[[channel-inversion-power-control]]"
  - "[[li-2026-directional-modulation-irs-uav]]"
  - "[[secrecy-energy-efficiency]]"
  - "[[li-2026-secrecy-ee-uav-ris-iov]]"
created: 2026-05-29
updated: 2026-07-13
---

# Physical Layer Security (PLS)

A family of secrecy techniques that exploit physical-layer properties — channel randomness, beamforming, artificial noise — to keep messages unreadable by eavesdroppers, **without** relying on cryptographic keys. The canonical metric is **secrecy rate** = legitimate-receiver rate − eavesdropper rate (clipped at 0).

Three common levers:

- **Beamforming nulls** that steer signal away from the eavesdropper.
- **Artificial noise / jamming** that raises the eavesdropper's noise floor more than the legitimate receiver's. See [[friendly-jamming-uav]].
- **Cooperative relays** that mask the source.

In the wiki, [[benaya-2025-aerial-isac-haps]] combines two of these levers: HAPS beamforming nulls steer signal away from eavesdroppers that are identified through [[integrated-sensing-and-communication|ISAC]] sensing, and a friendly-jamming AAV reinforces the secrecy gap.

PLS complements rather than replaces upper-layer crypto. It's particularly useful when key distribution is hard (post-disaster, ad-hoc swarms) or when key-management overhead is unacceptable. [[sun-2024-imssa-uav-secure-cb]] applies PLS through [[collaborative-beamforming]]: a UAV virtual antenna array steers a high-gain mainlobe to legitimate base stations and low-gain sidelobes elsewhere, maximizing the worst-case secrecy rate even when eavesdropper locations are imperfectly known or unknown.

[[wang-2026-secure-lae-uav-scheduling]] applies PLS to low-altitude economy communications by letting UAVs dynamically switch between communication and artificial-noise jamming roles while jointly optimizing power, trajectory, and velocity for secrecy energy efficiency.

[[wang-2026-secure-reliable-uav-mec]] applies the same artificial-noise idea inside a UAV-MEC offloading problem: multi-antenna users inject AN in the legitimate channel's null space while the UAV trajectory and offloading resources are optimized for secure energy efficiency under a secrecy-outage reliability constraint.

[[li-2026-secrecy-ee-uav-ris-iov]] treats an amplify-and-forward relay as an internal eavesdropper. The target vehicle jams the relay during the first hop, a UAV-mounted RIS shapes both hops, and the controller maximizes [[secrecy-energy-efficiency]] over powers, relay amplification, RIS phases, and UAV trajectory.

The covert-communication branch tightens the adversary model from eavesdropping quality to detection probability. [[zhang-2026-air-ground-covert-jamming]] uses a UAV-mounted RIS and decode-forward relay to steer terrestrial jammer energy toward a warden through [[ris-assisted-directional-jamming]], while [[chen-2026-air-ground-covert]] studies detection under warden-location uncertainty and PPP-modeled ambient interference.

[[bayessa-not-in-parse-uav-isac-secure-content-hdrl]] applies PLS to secure content delivery: ISAC sensing estimates mobile UAV eavesdroppers, then caching, association, deployment, and beamforming are selected to improve secure throughput.

[[cai-2026-llm-drl-secure-lae-data]] connects PLS to [[age-of-information]] and [[generative-ai-for-mec]]: an LLM-enhanced DRL controller coordinates a data-collection UAV and a jamming UAV to reduce freshness/energy cost while suppressing eavesdroppers.

The corpus includes several UAV-specific PLS/offloading variants: [[beishenalieva-2026-secrecy-aware-uav-path-planning]] protects ITS offloading against malicious aerial eavesdroppers and jammers, [[wu-2026-secure-split-offloading-ci]] protects DNN intermediate feature data during split inference, [[wu-2025-security-aware-multiuav-service-placement]] embeds secrecy-rate constraints into service-placement-aware multi-UAV MEC, and [[ren-2026-security-aware-vec-td3]] degrades vehicular offloading rates when a passive eavesdropper drives the secure rate below threshold.

Two physical-mobility and power-control variants broaden this thread. [[li-not-in-parse-movable-antenna-pls]] compares local antenna repositioning with whole-UAV trajectory control through [[micro-macro-mobility-security]], while [[he-not-in-parse-cipc-covert-uav]] uses [[channel-inversion-power-control]] so a confidential signal also covers multiple covert users.
