---
type: concept
title: "Dynamic Voltage Scaling (DVS)"
tags: [energy-efficiency, local-computing, design-choice]
related:
  - "[[energy-latency-tradeoff]]"
  - "[[binary-vs-partial-offloading]]"
  - "[[mobile-edge-computing]]"
  - "[[wang-2016-partial-offloading-dvs]]"
  - "[[zhang-2013-energy-optimal-mcc-stochastic]]"
  - "[[mao-2016-lodco-eh-mec-offloading]]"
created: 2026-06-02
updated: 2026-06-02
---

# Dynamic Voltage Scaling (DVS)

A processor power-management technique that varies the **supply voltage and clock frequency** with the computation load. Because dynamic CPU power scales super-linearly with frequency (commonly modeled as $P = k f^3$, so energy per cycle $\propto k f^2$), lowering the clock saves energy at the cost of longer compute time, and raising it shortens compute time at higher energy. In MEC/mobile-cloud offloading this makes the device's **local computational speed a continuous decision variable** alongside the transmit power and the offloading ratio, rather than a fixed constant. The same idea is often called **DVFS** (dynamic voltage and frequency scaling).

DVS reshapes the offloading decision: tuning the local speed changes how attractive offloading is, so it cannot be optimized independently of the transmit power or the partition. In [[wang-2016-partial-offloading-dvs]], jointly optimizing the SMD's DVS speed, transmit power, and offloading ratio yields a key structural result — **total offloading can never be energy-optimal once DVS is available**, because some residual local computation is always preferable. DVS-style CPU-frequency control also appears as a decision knob in the energy-optimal mobile-cloud scheduling of [[zhang-2013-energy-optimal-mcc-stochastic]] and the green energy-harvesting LODCO offloading of [[mao-2016-lodco-eh-mec-offloading]] (which couples offloading with DVFS frequency selection). It is one of the levers underlying the [[energy-latency-tradeoff]] and interacts directly with the [[binary-vs-partial-offloading]] choice.
