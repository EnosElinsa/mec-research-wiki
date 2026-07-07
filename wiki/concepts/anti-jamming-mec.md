---
type: concept
title: "Anti-Jamming MEC"
tags: [security, jamming, resource-management, physical-layer]
related:
  - "[[physical-layer-security]]"
  - "[[friendly-jamming-uav]]"
  - "[[spectrum-sensing-channel-selection]]"
  - "[[csi-estimation-error]]"
  - "[[shao-2024-drl-antijamming-mec]]"
  - "[[liu-2025-multimodal-semantic-iov-jamming]]"
  - "[[uav-localization-under-jamming]]"
  - "[[zhu-2026-uav-localization-jamming]]"
created: 2026-05-29
updated: 2026-07-07
---

# Anti-Jamming MEC

Resource management and communication design for MEC systems whose wireless links are under **malicious jamming**. The jammer (possibly a hostile UAV) emits interference to disrupt the UAV→user links; the system must sense jammed channels, avoid them, and re-allocate compute/communication resources to keep latency and energy acceptable.

Crucially distinct from the wiki's [[friendly-jamming-uav]] concept: there, jamming is used **defensively** (a cooperative UAV jams an eavesdropper). Here jamming is the **threat** to be detected and evaded. In the wiki, [[shao-2024-drl-antijamming-mec]] is the anchor — it senses jammed subchannels ([[spectrum-sensing-channel-selection]]) and uses [[multi-agent-td3|PER-MATD3]] to jointly tune CPU frequency, bandwidth, and channel selection under imperfect CSI ([[csi-estimation-error]]). [[liu-2025-multimodal-semantic-iov-jamming]] adds the IoV semantic variant, where jamming disrupts image/text semantic links and the UAVs jointly adjust trajectory, association, and channel selection. [[zhu-2026-uav-localization-jamming]] is adjacent rather than MEC: the jammer disrupts UAV localization measurements, so the BS switches GAN/TDOA positioning modes and controls sensing UAV trajectories. Related to the broader [[physical-layer-security]] theme.
