---
type: concept
title: EN-ConvNTM (Enhanced Convolutional Neural Turing Machine)
tags: [drl, memory, attention, ntm, stn]
related:
  - "[[ntm]]"
  - "[[convlstm]]"
  - "[[stn]]"
  - "[[j-ppo-en-convntm]]"
  - "[[liu-2026-jppo-en-convntm]]"
created: 2026-05-28
updated: 2026-05-28
---

# EN-ConvNTM (Enhanced Convolutional Neural Turing Machine)

A spatiotemporal encoder introduced in [[liu-2026-jppo-en-convntm]] that converts a sequence of 3-channel observation grids $\mathbf{o}_n$ (UAV positions / energies / device-visit-counts) into a context vector $\mathbf{h}_n$ suitable for the [[j-ppo]] policy and value heads.

```
o_n → STN → ConvNTM(read,context,write,enhance,update,output) → h_n
            with 3-D external memory m_n = [b^1, ..., b^L]
```

## Differences vs vanilla [[ntm|ConvNTM]]

| Aspect | ConvNTM | EN-ConvNTM |
|---|---|---|
| Memory dimensionality | 2-D | 3-D blocks |
| Front-end | conv stack | [[stn|STN]] before conv |
| Per-step ops | read / write / update / output | adds an *enhancement* op (attention-weighted refinement) |
| Long-sequence handling | weakens with depth | better — STN + attention focus on operationally-significant regions |

## The enhancement step

Combines:

1. STN-transformed input — sharpens spatial focus
2. Contextual write embedding $\mathbf{w}_n$
3. Attention output over $[\phi(\mathbf{r}_n), \mathbf{w}_n]$

Then fuses with a linear + nonlinearity to produce the enhanced vector $\mathbf{e}_n$, which is what gets folded into the next memory state $\mathbf{m}_{n+1}$.

## Why it matters here

UAV decisions depend on **historical** trajectories of moving devices, not just the current frame. Pure [[convlstm]] only carries forward a hidden state and forgets distant context. NeuralMap stores a flat 1-D vector per 2-D cell and collides identities when multiple UAVs occupy the same region. EN-ConvNTM's external memory + STN sidesteps both — see [[en-convntm-beats-baselines]] and [[neuralmap-loses-spatial-info]].
