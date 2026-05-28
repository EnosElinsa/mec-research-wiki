---
type: comparison
title: j-PPO encoder ablation — EN-ConvNTM vs ConvNTM vs ConvLSTM vs NeuralMap vs raw
tags: [drl, ablation, memory]
related:
  - "[[en-convntm]]"
  - "[[ntm]]"
  - "[[convlstm]]"
  - "[[en-convntm-beats-baselines]]"
  - "[[neuralmap-loses-spatial-info]]"
created: 2026-05-28
updated: 2026-05-28
---

# j-PPO encoder ablation

Holding the [[j-ppo]] policy fixed and swapping the spatiotemporal encoder, the four ablations in [[liu-2026-jppo-en-convntm]] line up as:

| Encoder | Memory model | Spatial structure preserved? | Long-horizon? | Ω rank |
|---|---|---|---|---|
| **EN-ConvNTM** | 3-D external memory + STN + attention | ✅ | ✅✅ | **1 (best)** |
| ConvNTM | 2-D external memory | ✅ | ✅ | 2 |
| ConvLSTM | hidden state only | ✅ | ⚠️ short | 3 |
| NeuralMap | 1-D vector per 2-D cell | ⚠️ identity collisions | ✅ | 4 |
| j-PPO (raw) | none | ❌ | ❌ | 5 (worst) |

## Reading the ranking

- The jump from **none → ConvLSTM** is large: any temporal aggregation helps.
- The jump from **ConvLSTM → ConvNTM** is non-trivial: external memory enables longer-horizon recall.
- The jump from **ConvNTM → EN-ConvNTM** is the value of the [[stn]] front-end + attention-driven enhancement.
- **NeuralMap** ranks fourth despite having a memory because the memory is too narrow — see [[neuralmap-loses-spatial-info]].

## When you might pick a different encoder

- **ConvLSTM** if compute budget is tight and history depth is shallow.
- **Plain ConvNTM** if you don't need the STN's spatial-attention benefit (e.g. the relevant region is fixed and pre-cropped).
- **EN-ConvNTM** as a default for cooperative multi-agent grid-observation tasks.
