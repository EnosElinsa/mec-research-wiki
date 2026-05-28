---
type: concept
title: ConvLSTM
tags: [neural-network, recurrent, vision]
related:
  - "[[ntm]]"
  - "[[en-convntm]]"
created: 2026-05-28
updated: 2026-05-28
---

# ConvLSTM

Convolutional Long Short-Term Memory: an LSTM whose gates and state transitions use convolutions instead of dense matrix multiplications, preserving the spatial structure of input feature maps across time.

Compared to [[ntm]]-style external memory, ConvLSTM only carries forward a single (spatial) hidden state, which limits how far back useful information can travel. [[liu-2026-jppo-en-convntm]] uses a `j-PPO+ConvLSTM` baseline and shows that the lack of an explicit memory store causes [[en-convntm-beats-baselines|measurable degradation]] on the equilibrium-efficiency metric in [[high-density-mobile-device-scenarios]].
