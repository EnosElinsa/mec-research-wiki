---
type: concept
title: Spatial Transformer Network (STN)
tags: [neural-network, attention, vision]
related:
  - "[[en-convntm]]"
  - "[[liu-2026-jppo-en-convntm]]"
created: 2026-05-28
updated: 2026-05-28
---

# Spatial Transformer Network (STN)

A learnable module that applies a parameterized spatial transformation (affine, projective, or thin-plate-spline) to its input feature map *before* downstream processing, allowing the network to attend to operationally relevant regions and normalize spatial variability. Originally proposed by Jaderberg et al. (2015).

In [[en-convntm]] the STN sits in front of the ConvNTM front-end:

$$
\mathbf{h}_n = \text{EN-ConvNTM}(\text{STN}(\phi(\mathbf{o}_n)))
$$

Its job in this project is to focus the memory's read/write attention on the high-information regions of the observation grid (clusters of devices, the relevant charging station) rather than treating the grid uniformly.
