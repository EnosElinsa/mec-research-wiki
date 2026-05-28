---
type: concept
title: "Video Transcoding Tradeoff"
tags: [video, transcoding, bitrate, accuracy]
related:
  - "[[video-analytics-offloading]]"
  - "[[qoe-modeling-mec]]"
  - "[[bao-2025-ddpg-video-offloading]]"
created: 2026-05-29
updated: 2026-05-29
---

# Video Transcoding Tradeoff

Transcoding compresses a video stream to a lower bitrate before transmission, reducing transmission time and bandwidth use at the cost of **video quality**. For analytics workloads this matters because lower-bitrate inputs degrade DNN accuracy — image detail (small objects, fine textures, edges) is exactly what compression discards.

The tradeoff has three coupled knobs:

- **Offloading ratio** $\eta$ — what fraction of video to send to the remote server.
- **Transcoding decision + ratio** $(\epsilon, \bar\epsilon)$ — whether to transcode, and how aggressively.
- **Compute resource allocation** at the server — how much CPU to give each transcoded stream.

The "right" point on this surface is not stable: under good channel conditions, send less-compressed video; under bad channels, compress more (or skip offloading). [[bao-2025-ddpg-video-offloading]] solves this with a DDPG policy that adapts all three knobs per slot, with a [[qoe-modeling-mec|QoE]] reward that bakes in the bitrate-accuracy curve.

Practical caveat: the bitrate→accuracy curve depends on content (low-light, fast motion, model architecture). Treat any specific fitted curve as scenario-dependent.
