---
type: source
modeling_card: not_applicable
title: "Energy Efficiency of Mobile Clients in Cloud Computing"
authors: ["Antti P. Miettinen", "Jukka K. Nurminen"]
year: 2010
url: ""
venue: "2nd USENIX Workshop on Hot Topics in Cloud Computing (HotCloud '10)"
tags: [source, mobile-edge-computing, computation-offloading, energy-latency-tradeoff, measurement-study, computation-to-communication-ratio]
related:
  - "[[mobile-edge-computing]]"
  - "[[task-offloading]]"
  - "[[computation-to-communication-ratio]]"
  - "[[energy-latency-tradeoff]]"
  - "[[binary-vs-partial-offloading]]"
  - "[[zhang-2013-energy-optimal-mcc-stochastic]]"
  - "[[you-2017-meco-resource-allocation]]"
  - "[[mao-2017-mec-survey-communication]]"
created: 2026-06-02
updated: 2026-07-16
---

# Energy Efficiency of Mobile Clients in Cloud Computing

## Citation

Miettinen, A. P., & Nurminen, J. K. (2010). *Energy Efficiency of Mobile Clients in Cloud Computing*. **2nd USENIX Workshop on Hot Topics in Cloud Computing (HotCloud '10)**, Boston, MA, June 2010. No DOI - USENIX workshop paper.

## TL;DR

An early, foundational **analysis and measurement** of when offloading computation from a mobile device to the cloud actually **saves energy**. The central quantity is the **computing-to-communication ratio**: offloading helps only when the energy cost of transferring input/output data is less than the energy of computing locally ($E_{cloud} < E_{local}$). Using measurements of contemporary handheld devices over **WLAN and 3G**, the authors show the trade-off is **highly sensitive** to workload characteristics, the amount *and pattern* of data communication (bursts vs many small packets), and the wireless technology used - and they draw out the engineering implications for energy-efficient mobile cloud computing.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Miettinen and Nurminen [x] studied the energy efficiency of computation offloading from mobile clients to cloud infrastructure. They expressed the offloading condition as $E_{cloud}<E_{local}$ and related the crossover to a workload's computing-to-communication ratio. Their analysis combines processing-energy estimates with measurements of contemporary handheld communication over WLAN and 3G. The measurements show that the offloading threshold depends on the radio technology and that many small transfers consume more energy than sending the same data in a burst. The paper reports that cloud execution saves client energy only when the avoided local computation cost exceeds the communication energy required for the input and output data.

## Problem framing

Battery capacity grows only slowly (the paper cites ~5%/year) and thermal limits cap small-device power budgets, so energy efficiency is a first-order constraint. Cloud computing can offload work to save mobile energy - but **only if** the communication energy is smaller than the saved computation energy. Many mobile applications are deliberately light-weight (a "natural selection" toward what runs on limited devices), so the computational characteristics of much current software actually favor **local** processing; offloading pays off for the genuinely compute-heavy cases. The paper sets out to map this basic local-vs-remote balance empirically.

## System model

This is a **measurement and analysis** study, not an algorithm. The model is an energy-cost comparison: local execution energy $E_{local}$ (set by the workload's CPU cycles C and the device's processing energy efficiency) versus offloading energy $E_{cloud}$ (set by the data volume D, the traffic pattern, and the wireless-link energy efficiency). The offloading-beneficial condition is $E_{cloud} < E_{local}$, which reduces to a **computing-to-communication ratio** threshold (cycles per byte) that depends on the device and the radio.

## Method

- **Energy trade-off analysis.** Derive the crossover condition $E_{cloud} < E_{local}$ and express it through the computing-to-communication ratio.
- **Device characterization.** Measure energy-per-bit / energy characteristics of contemporary handheld devices over **WLAN and 3G**, plus the effect of **traffic pattern** (a sequence of small packets costs more than the same data sent in one burst).
- **Worked example.** Demonstrate a concrete case where cloud offloading yields energy savings, and discuss preliminary mechanisms for estimating the energy cost of modern web-oriented workloads.

## Key findings

- Offloading is beneficial **only** when the workload is sufficiently compute-intensive relative to its data transfer - i.e., a high enough computing-to-communication ratio; many light-weight mobile apps fall below this and are better run locally.
- The crossover is **strongly dependent on the wireless technology**: WLAN and 3G give very different thresholds for when moving to the cloud pays off.
- Not only data volume but **traffic pattern** matters: bursty transfers are more energy-efficient than many small packets. This puts real responsibility on developers and content producers to structure communication well.

## Limitations / future work

A snapshot of *then-contemporary* devices and radios (circa 2010, WLAN + 3G); findings are technology-specific and would shift with newer hardware/radios. It evaluates feasibility of moving tasks wholesale rather than fine-grained program partitioning. Concrete future-work items beyond the stated developer/content-producer implications are `not in parse`.

## Relation to the corpus

The corpus's **earliest** anchor and a conceptual root for the whole offloading literature: it states, empirically, the **local-vs-offload energy crossover** that later MEC papers formalize and optimize. It precedes and motivates the structural multiuser resource-allocation result of [[you-2017-meco-resource-allocation]] and the stochastic-channel MCC scheduling of [[zhang-2013-energy-optimal-mcc-stochastic]], and the **communication-energy-vs-computation-energy** balance it identifies is exactly the framing surveyed in [[mao-2017-mec-survey-communication]]. It grounds the [[computation-to-communication-ratio]] concept.

## Raw artifacts

- `raw/sources/Energy_Efficiency_of_Mobile_Clients_in_Cloud_Computing/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
