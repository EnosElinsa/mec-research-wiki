---
type: concept
title: "Mogrifier LSTM Policy"
tags: [reinforcement-learning, recurrent-policy, lstm, temporal-modeling]
related:
  - "[[xie-2026-uav-irs-eppo]]"
  - "[[ppo]]"
  - "[[convlstm]]"
created: 2026-07-13
updated: 2026-07-13
---

# Mogrifier LSTM Policy

A recurrent policy encoder that alternately gates the current input and previous hidden state several times before applying an ordinary LSTM update. This multiplicative interaction lets each representation reshape the other before temporal memory is updated.

[[xie-2026-uav-irs-eppo]] inserts the mechanism into its PPO actor for UAV motion history. Its reported benefit is a modest simulation ablation gain; it should not be conflated with replay-based episodic memory or with convolutional recurrent encoders such as [[convlstm]].
