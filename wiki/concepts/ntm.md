---
type: concept
title: Neural Turing Machine (NTM)
tags: [neural-network, memory, attention]
related:
  - "[[en-convntm]]"
  - "[[convlstm]]"
created: 2026-05-28
updated: 2026-05-28
---

# Neural Turing Machine (NTM)

A neural architecture (Graves et al., 2014/2016) that augments a recurrent controller with a differentiable external memory matrix. Read and write heads emit content- and location-based attention weights over the memory, allowing the network to learn algorithmic patterns and to recall information across long temporal gaps that would otherwise be erased by a hidden state.

In the LLM Wiki context, the relevant variant is the **ConvNTM** — a convolutional version where memory blocks preserve spatial structure (good for grid-like observations such as occupancy or device-density maps). [[en-convntm]] takes this further with a 3-D memory and an attention-driven enhancement step.

## Reference

Graves, A., Wayne, G., Reynolds, M., et al. (2016). *Hybrid computing using a neural network with dynamic external memory*. **Nature**, 538(7626), 471–476. (Cited as [30] in [[liu-2026-jppo-en-convntm]].)
