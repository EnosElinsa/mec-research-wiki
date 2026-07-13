---
type: concept
title: "Sparse XL-MIMO"
tags: [xl-mimo, sparse-array, near-field, physical-layer]
related:
  - "[[min-2026-sparse-bistatic-nearfield-isac]]"
  - "[[extremely-large-scale-mimo]]"
  - "[[near-field-communications]]"
  - "[[symmetric-double-nested-array]]"
  - "[[integrated-sensing-and-communication]]"
created: 2026-07-14
updated: 2026-07-14
---

# Sparse XL-MIMO

An [[extremely-large-scale-mimo|XL-MIMO]] architecture that deliberately spaces some antenna elements farther apart than a compact half-wavelength array to enlarge physical aperture and spatial degrees of freedom without proportionally increasing element count. The larger aperture can improve angular resolution and channel separation, but sparse placement introduces grating lobes and makes performance depend on array geometry and signal processing.

[[min-2026-sparse-bistatic-nearfield-isac]] uses a [[symmetric-double-nested-array]] at an ISAC transmitter and compares sparse and compact arrays for communication and near-field UAV sensing. Its sensing pipeline combines the sparse geometry with a [[fourth-order-bistatic-virtual-array]] rather than treating the physical sparse array alone as ambiguity-free.

Sparse aperture does not by itself guarantee better estimation or communication. The source's gains are simulation-based under known array geometry, synchronization, transmitted symbols, and simplified channel and target models; calibration error, mutual coupling, attitude jitter, and hardware implementation are not evaluated.
