---
type: source
title: "Can 5G mmWave Enable Edge-Assisted Real-Time Object Detection for Augmented Reality?"
authors: ["Moinak Ghoshal", "Z. Jonny Kong", "Qiang Xu", "Zixiao Lu", "Shivang Aggarwal", "Imran Khan", "Jiayi Meng", "Yuanjie Li", "Y. Charlie Hu", "Dimitrios Koutsonikolas"]
year: "not in parse"
url: "not in parse"
venue: "not in parse"
modeling_card: not_applicable
tags: [source, mmwave, 5g, augmented-reality, edge-offloading, object-detection, measurement]
related:
  - "[[video-analytics-offloading]]"
  - "[[edge-intelligence]]"
  - "[[hardware-validation-and-sim-to-real-in-mec]]"
created: 2026-11-02
updated: 2026-11-02
---

# Can 5G mmWave Enable Edge-Assisted Real-Time Object Detection for Augmented Reality?

## Citation

Ghoshal, M., Kong, Z. J., Xu, Q., Lu, Z., Aggarwal, S., Khan, I., Meng, J., Li, Y., Hu, Y. C., & Koutsonikolas, D. *Can 5G mmWave Enable Edge-Assisted Real-Time Object Detection for Augmented Reality?* Venue, year, and DOI are not in the parse.

## TL;DR

A measurement study of whether commercial 5G mmWave with an in-network edge cloud can support edge-assisted object detection for mobile AR. It finds the uplink falls far short for a baseline offloading design, and that pre-5G app optimizations and better edge hardware matter more than the radio.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Ghoshal et al. [x] conducted an in-depth measurement study of whether 5G mmWave combined with an in-network edge cloud can support baseline edge-assisted object detection for augmented reality. They found that 5G mmWave is unlikely to achieve the uplink performance needed by a baseline edge-assisted object detection implementation in the near future. They then quantified the benefits of retrofitting app-level optimizations developed before 5G, such as frame compression and local tracking, and of upgrading edge hardware. These optimizations significantly improve object detection over both LTE and 5G mmWave, so the additional benefit of 5G mmWave is marginal. Without them, 5G mmWave would need a stable uplink of 273 Mbps to 1.3 Gbps for satisfactory performance.

## Scope and method

Experiments measure end-to-end detection accuracy on Argoverse and MOT datasets over LTE and 5G mmWave in static, walking, and driving scenarios. It is a measurement study with no decision model.

## Key findings

- Encoding at 12 Mbps shrinks frames from about 450 KB to 50 KB with accuracy within 2% of uncompressed frames.
- With optimizations, apps reach 90% of offline accuracy in static scenarios but not in walking or driving.
- Edge hardware upgrades combined with app-level optimizations are more promising than the radio upgrade.

## Limitations / future work

Results reflect the measured operator deployments.

## Relation to the corpus

A measured counterpoint to bandwidth-driven assumptions in [[video-analytics-offloading]] and [[edge-intelligence]], with evidence relevant to [[hardware-validation-and-sim-to-real-in-mec]].

## Raw artifacts

- Parse: `raw/sources/Can_5G_mmWave_Enable_Edge-Assisted_Real-Time_Object_Detection_for_Augmented_Reality/Can_5G_mmWave_Enable_Edge-Assisted_Real-Time_Object_Detection_for_Augmented_Reality.md`
- Extracted figures are in the same folder; no companion PDF is present.
