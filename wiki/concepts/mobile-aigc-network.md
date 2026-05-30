---
type: concept
title: Mobile AIGC Network
tags: [generative-ai, aigc, edge-cloud, mobile-edge-computing, service-architecture]
related:
  - "[[generative-ai-for-mec]]"
  - "[[aigc-service-provider]]"
  - "[[three-tier-cloud-edge-end]]"
  - "[[generative-diffusion-model]]"
  - "[[xu-2024-mobile-aigc-survey]]"
created: 2026-05-31
updated: 2026-05-31
---

# Mobile AIGC Network

A **mobile AIGC network** deploys Artificial-Intelligence-Generated-Content (AIGC) services — text/image/audio/video/3D generation via models like ChatGPT and DALL-E — across a **collaborative cloud-edge-mobile** infrastructure so that mobile users get personalized, low-latency content while keeping data local. The division of labor: the **cloud layer** handles resource-heavy pre-training and fine-tuning; the **edge layer** and **mobile-device layer** handle data collection, inference, and product management close to the user.

## The AIGC service lifecycle

The survey frames AIGC provisioning as a lifecycle circulated between core and edge networks: **data collection → pre-training → fine-tuning → inference → product management**. Moving the interaction-intensive stages (fine-tuning, inference, product management) to the edge is what motivates the mobile-AIGC architecture, with claimed benefits in low latency, localization/mobility, customization/personalization, and privacy/security.

## In this wiki

- [[xu-2024-mobile-aigc-survey]] is the anchor survey that defines the term and maps its implementation challenges — **edge resource allocation**, **task & computation offloading**, **edge caching**, **mobility management**, and **incentive mechanisms**.

Distinct from [[generative-ai-for-mec]] (using generative models to *optimize/control* the MEC system): a mobile AIGC network is about *serving* generative AI as the workload itself, with the [[aigc-service-provider|ASP]] as the edge service role and a [[three-tier-cloud-edge-end|cloud-edge-end]] deployment.
