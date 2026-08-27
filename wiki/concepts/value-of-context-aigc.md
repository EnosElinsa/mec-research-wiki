---
type: concept
title: "Value of Context for AIGC"
tags: [aigc, contextual-memory, service-migration, inference-accuracy, edge-intelligence]
related:
  - "[[mobile-aigc-network]]"
  - "[[service-migration]]"
  - "[[age-of-information]]"
  - "[[wang-2026-context-aigc-migration]]"
created: 2026-08-27
updated: 2026-08-27
---

# Value of Context for AIGC

The **Value of Context (VoC)** scores how useful a historical AIGC context window is for a current request by combining freshness and semantic relevance. In [[wang-2026-context-aigc-migration]], freshness is represented by the age of the window and relevance by a keyword-indicator distance; accumulated VoC then feeds a logarithmic inference-accuracy model and guides which context to migrate.

VoC is a task-specific metric in that source, not a replacement for [[age-of-information]] or a universal accuracy guarantee. Its role is to expose the accuracy benefit that can be traded against context-transfer cost and inference latency.
