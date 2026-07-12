---
type: concept
title: "Wavelet-Guided Mamba Crack Segmentation"
tags: [image-segmentation, mamba, wavelet, edge-inference, pavement-crack]
related:
  - "[[cheng-2026-cnn-mamba-cracks]]"
  - "[[edge-intelligence]]"
  - "[[uav-assisted-edge-inference]]"
created: 2026-07-13
updated: 2026-07-13
---

# Wavelet-Guided Mamba Crack Segmentation

A slender-object segmentation architecture that combines local CNN detail extraction with state-space modeling over spatial-frequency features. [[cheng-2026-cnn-mamba-cracks]] decomposes decoder features into Haar approximation and directional bands, processes them with a reduced CVSS/SS2D block, and fuses them with channel attention and progressive convolution.

The architecture targets global crack continuity without Transformer-style quadratic attention. Its deployment contribution is separate from the segmentation design: an LMC-Belloch/Triton scan preserves ONNX output fidelity while raising Jetson inference speed over a serial PyTorch scan.
