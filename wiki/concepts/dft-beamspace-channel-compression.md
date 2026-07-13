---
type: concept
title: "DFT Beamspace Channel Compression"
tags: [channel-compression, beamspace, dft, mimo]
related:
  - "[[wang-2026-spatiotemporal-leo-channel-prediction]]"
  - "[[spatiotemporal-attention-channel-prediction]]"
  - "[[masked-csi-reconstruction-pretraining]]"
  - "[[uav-mounted-ris]]"
created: 2026-07-14
updated: 2026-07-14
---

# DFT Beamspace Channel Compression

A channel representation that applies a two-dimensional discrete Fourier transform to an antenna-domain channel and retains only the strongest beam coefficients. Magnitude, phase, and normalized beam indices become compact prediction tokens; reconstruction inserts zeros in omitted bins and applies the inverse transform.

[[wang-2026-spatiotemporal-leo-channel-prediction]] applies this representation separately to satellite-RIS, RIS-user, and direct satellite-user links before [[spatiotemporal-attention-channel-prediction]]. Retaining `P` dominant beams reduces the attention sequence length and analytical compute cost, especially for large arrays.

Top-`P` truncation is generally lossy, despite the source's wording about invertibility. Its small-array experiment reports a nonzero NMSE change, and the large-array case has no full element-domain accuracy result. The method therefore relies on beamspace concentration and does not guarantee faithful reconstruction for diffuse, off-grid, or strongly nonstationary channels.
