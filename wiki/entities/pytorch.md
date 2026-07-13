---
type: entity
title: PyTorch
tags: [tool, deep-learning, framework]
related:
  - "[[bai-2026-passive-uav-detection]]"
  - "[[kim-2026-qmarl-sagin-access]]"
  - "[[liu-2026-jppo-en-convntm]]"
  - "[[ye-2023-graph-uav-coverage]]"
created: 2026-05-28
updated: 2026-07-14
---

# PyTorch

Open-source deep-learning framework maintained by Meta and the PyTorch Foundation. The reference implementation of [[j-ppo-en-convntm]] is built on **PyTorch 2.1.0** per [[liu-2026-jppo-en-convntm]] (Section V-A).

The project's PPO codebase derives from [Kostrikov's `pytorch-a2c-ppo-acktr-gail`](https://github.com/ikostrikov/pytorch-a2c-ppo-acktr-gail) (cited as reference [35]).

[[ye-2023-graph-uav-coverage]] reports PyTorch 1.4.0 for its recurrent FANET graph-learning implementation.

[[bai-2026-passive-uav-detection]] uses PyTorch for its compact multi-scale and multi-period temporal network over estimated broadcast-channel impulse responses.

[[kim-2026-qmarl-sagin-access]] uses PyTorch 2.2.0 with TorchQuantum 0.1.7 to emulate parameterized quantum actors and a centralized critic on conventional GPU hardware.
