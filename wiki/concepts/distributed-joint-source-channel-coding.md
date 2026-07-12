---
type: concept
title: "Distributed Joint Source-Channel Coding"
tags: [joint-source-channel-coding, distributed-video-coding, semantic-communication, deep-learning, uav-video]
related:
  - "[[zhang-2026-distributed-jscc-uav-video]]"
  - "[[semantic-communication]]"
  - "[[deep-q-network]]"
  - "[[uav-mobile-relaying]]"
  - "[[energy-balancing-uav]]"
created: 2026-07-13
updated: 2026-07-13
---

# Distributed Joint Source-Channel Coding

Distributed joint source-channel coding keeps the transmitter encoder lightweight by moving correlation exploitation and reconstruction complexity to the receiver while mapping source features directly to channel symbols. For video, independently encoded key and predictive features let decoded key frames become decoder-side information for reconstructing intermediate frames.

[[zhang-2026-distributed-jscc-uav-video]] implements this pattern with UAV-side FastNet blocks and a receiver-heavy neural decoder. Key frames are reconstructed directly; Wyner-Ziv-inspired frame features are fused with interpolated side information through attention and deformable-convolution modules. A separate [[deep-q-network|DQN]] chooses direct/relay links and power rather than changing the codec architecture online.

The approach trades encoder cost for receiver computation and depends on useful temporal correlation. Poor side information and severe channels degrade reconstruction, and the parse reports the highest decoding time at the receiver despite removing the feedback channel. The term here means joint source-channel coding and must not be conflated with acronyms used for joint sensing, communication, and computation.
