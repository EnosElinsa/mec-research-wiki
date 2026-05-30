---
type: concept
title: "Multi-Functional RIS (MF-RIS)"
tags: [ris, reflection, refraction, amplification, energy-harvesting, full-space]
related:
  - "[[intelligent-reflecting-surface]]"
  - "[[semantic-communication]]"
  - "[[anti-jamming-mec]]"
  - "[[rf-energy-harvesting]]"
  - "[[sun-2024-mfris-semantic-antijamming]]"
created: 2026-05-31
updated: 2026-05-31
---

# Multi-Functional RIS (MF-RIS)

An extension of the conventional [[intelligent-reflecting-surface]] that supports **signal reflection, refraction, amplification, and energy harvesting** in one surface. These functions are meant to overcome three drawbacks of conventional RIS:

- **Half-space coverage** — reflection-only RIS serves users on one side; adding refraction enables **full-space** coverage.
- **Multiplicative fading** — passive RIS suffers cascaded path loss; signal **amplification** mitigates it.
- **Battery reliance** — onboard **energy harvesting** supports a self-sustainability constraint instead of a fixed battery.

## In this wiki

- [[sun-2024-mfris-semantic-antijamming]] uses an MF-RIS (with a self-sustainability/energy-partition constraint) to customize the full-space wireless environment for an integrated aerial-ground MEC network, combined with [[semantic-communication]] for anti-jamming computing. The amplitude/phase of reflection and refraction can be independently manipulated, which makes the resource-configuration problem a coupled MINLP.
