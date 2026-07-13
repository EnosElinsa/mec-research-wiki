---
type: concept
title: "Covert Communication"
tags: [security, physical-layer-security, stochastic-geometry, detection]
related:
  - "[[wang-2026-fd-covert-isac]]"
  - "[[zhang-2026-irs-uav-covert-fbl]]"
  - "[[deng-2025-covert-isac-trajectory]]"
  - "[[physical-layer-security]]"
  - "[[finite-blocklength-urllc]]"
  - "[[stochastic-geometry-network-analysis]]"
  - "[[cooperative-jamming]]"
  - "[[ma-2024-covert-mmwave-finite-blocklength]]"
  - "[[hosseini-2026-aoi-covert-uav]]"
  - "[[freshness-aware-covert-uav-communication]]"
  - "[[zhang-2026-air-ground-covert-jamming]]"
  - "[[ris-assisted-directional-jamming]]"
  - "[[chen-2026-air-ground-covert]]"
  - "[[ambient-interference-aided-covertness]]"
  - "[[noma]]"
  - "[[age-of-information]]"
  - "[[he-not-in-parse-cipc-covert-uav]]"
  - "[[channel-inversion-power-control]]"
created: 2026-06-03
updated: 2026-07-14
---

# Covert Communication

A security goal that goes beyond hiding a message's **content** (the target of encryption and classic [[physical-layer-security|PLS]]) to hiding the **existence** of the transmission itself — also called low-probability-of-detection communication. A transmitter (Alice) sends to a legitimate receiver (Bob) such that a warden (Willie) cannot reliably decide, from its observations, whether a transmission occurred. The canonical limit traces to Bash et al.'s square-root law over AWGN channels.

Core ingredients that recur in covert-communication models:

- **Detection-error criterion.** Willie performs a binary hypothesis test; covertness is enforced via a constraint on the total detection error probability, or equivalently on the total-variation distance / Kullback-Leibler divergence between the channel's "transmitting" and "silent" output distributions.
- **Sources of uncertainty Alice exploits.** Noise uncertainty, channel uncertainty, artificial noise / [[cooperative-jamming|jamming]], a public cover link, or — when blocklength is short — the limited number of observations Willie can collect.
- **[[finite-blocklength-urllc|Finite blocklength]].** Short packets both satisfy latency/power limits and naturally limit Willie's observations, so blocklength becomes a design variable trading off against transmit power.
- **Spatial randomness of wardens.** When multiple wardens are randomly located, [[stochastic-geometry-network-analysis|stochastic geometry]] (e.g. a Poisson point process) is used to characterize the covertness constraint over the warden field.

In the wiki, [[ma-2024-covert-mmwave-finite-blocklength]] studies covert **mmWave** communication with finite blocklength against spatially random wardens, deriving covertness constraints and the average effective covert throughput (AECT) for phased-array and linear frequency diverse array beamforming, then jointly optimizing transmit power and blocklength.

[[hosseini-2026-aoi-covert-uav]] moves the same low-probability-of-detection idea into a UAV freshness setting. Its [[freshness-aware-covert-uav-communication]] model uses a public [[noma|PD-NOMA]] user as cover traffic while minimizing [[age-of-information]] for the covert user's updates under an aerial eavesdropper.

[[zhang-2026-air-ground-covert-jamming]] adds [[ris-assisted-directional-jamming]]: a decode-and-forward UAV with an onboard RIS redirects a terrestrial friendly jammer's signal toward Willie while also relaying Alice's covert data. The design couples covertness, finite-blocklength relay decoding, RIS coefficients, and DDQN trajectory/user scheduling.

[[chen-2026-air-ground-covert]] adds [[ambient-interference-aided-covertness]], where uncontrolled PPP-distributed ground interferers create the uncertainty that hides a UAV Alice from a location-uncertain Willie. Its tradeoff is not free: denser or stronger interference improves covertness while reducing Bob's connection probability.

[[he-not-in-parse-cipc-covert-uav]] uses a confidential user's strong signal as cover for multiple NOMA covert users. Truncated [[channel-inversion-power-control]] stabilizes the target power at the UAV receiver while coupling connection, secrecy-outage, and detection-error behavior.
