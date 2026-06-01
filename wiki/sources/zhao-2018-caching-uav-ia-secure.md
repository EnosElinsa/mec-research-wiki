---
type: source
title: "Caching UAV Assisted Secure Transmission in Hyper-Dense Networks Based on Interference Alignment"
authors: ["Nan Zhao", "Fen Cheng", "F. Richard Yu", "Jie Tang", "Yunfei Chen", "Guan Gui", "Hikmet Sari"]
year: 2018
url: "https://doi.org/10.1109/TCOMM.2018.2792014"
venue: "IEEE Transactions on Communications (IEEE TCOMM)"
tags: [source, unmanned-aerial-vehicle, interference-alignment, physical-layer-security, small-cell-mec, service-caching-mec, cooperative-jamming, video-transcoding-tradeoff]
related:
  - "[[interference-alignment]]"
  - "[[physical-layer-security]]"
  - "[[cooperative-jamming]]"
  - "[[friendly-jamming-uav]]"
  - "[[small-cell-mec]]"
  - "[[service-caching-mec]]"
  - "[[video-transcoding-tradeoff]]"
  - "[[uav-mobile-relaying]]"
  - "[[wireless-backhaul]]"
  - "[[zhao-2019-uav-emergency-disasters]]"
  - "[[chen-2024-dro-video-caching]]"
  - "[[michailidis-2024-secure-ris-uav-mec-iot]]"
created: 2026-06-02
updated: 2026-06-02
---

# Caching UAV Assisted Secure Transmission in Hyper-Dense Networks Based on Interference Alignment

## Citation

Zhao, N., Cheng, F., Yu, F. R., Tang, J., Chen, Y., Gui, G., & Sari, H. (2018). *Caching UAV Assisted Secure Transmission in Hyper-Dense Networks Based on Interference Alignment*. **IEEE Transactions on Communications**. DOI: 10.1109/TCOMM.2018.2792014. (Manuscript received 24 July 2017; revised 15 November 2017 and 26 December 2017; accepted 6 January 2018; date of publication 11 January 2018; date of current version 15 May 2018 → year 2018. A precursor appeared at ICNC 2018.)

## TL;DR

A **caching-UAV-assisted secure transmission** scheme for **hyper-dense small-cell networks** that combines **interference alignment (IA)** with **physical-layer security via friendly jamming**. UAVs act as mobile small-cell base stations (SBSs) carrying caches that store popular (enhancement-layer) video during off-peak periods, offloading SBS traffic over a capacity-limited wireless backhaul. Each UAV has a **single antenna** (no precoding / CSI needed at the UAV), so only the multi-antenna SBSs' precoding matrices are cooperatively designed to **align and eliminate interference**. The SBSs that the UAVs replace become **idle and are repurposed to emit jamming signals** that disrupt a passive eavesdropper, with the jamming **zero-forced** at the legitimate users so legitimate transmission is unaffected. The paper derives the scheme's feasibility conditions, analyzes secrecy performance, and validates by simulation.

## Problem framing

5G small-cell densification raises throughput but worsens inter-user interference, so interference management (IA) is essential; small-cell security is also a concern. UAVs can serve as low-cost, mobile SBSs that relieve cells via wireless backhaul, but backhaul capacity is limited, degrading QoS when users are crowded. **Caching** at the UAVs lets popular content be delivered directly at peak time without backhaul, shifting traffic to off-peak and reducing latency. The combined challenge is to manage interference in a UAV+SBS network where UAVs are single-antenna, while simultaneously guaranteeing secure transmission against an eavesdropper.

## System model

- **Topology.** One macro BS (optical backhaul to core), K SBSs and K corresponding users, plus A (< K) cache-equipped UAVs connected to the MBS via wireless backhaul.
- **UAV properties.** Single antenna (scattering-poor UAV environment, SWaP limits, no easy CSI) → one data stream, no precoding, no CSI knowledge needed; rotary-wing UAVs hover stationary while transmitting, so CSI changes slowly and IA is applicable.
- **Caching strategy.** Scalable video split into a base layer (BL) and enhancement layer (EL); UAVs cache EL segments while SBSs cache both BL and EL. UAVs serve EL (high-definition) demand; idle SBSs (those replaced by UAVs) become jammers.
- **Adversary.** A passive multi-antenna eavesdropper attempting to intercept the legitimate transmission.

## Method

- **Interference alignment.** Cooperative design of the SBSs' precoding matrices (and users' decoding matrices/vectors) confines all interference into a common subspace so it cancels at each legitimate receiver; the paper derives the **feasibility conditions** under which perfect interference elimination is achievable.
- **Friendly-jamming security.** Idle SBSs transmit jamming via unitary precoding matrices designed so the jamming lies in the same interference subspace at legitimate users — i.e., **zero-forced** there — while degrading the eavesdropper. Secrecy performance (with the eavesdropper present) is analyzed.
- **Distributed algorithm.** An iterative distributed algorithm realizes the joint IA + jamming design.

## Key findings

- The scheme perfectly eliminates inter-user interference at legitimate users when the derived IA feasibility conditions hold, and the friendly jamming from idle SBSs is cancelled at legitimate users while disrupting the eavesdropper (analytical results).
- Simulations verify the secrecy performance and the effectiveness of the combined caching + IA + jamming scheme (the paper's stated simulation results; specific secrecy-rate curves are in the parse's figures, so treat exact values as indicative).

## Limitations / future work

A physical-layer / interference-management study (this is a UAV-communications + caching + PLS paper, not an MEC offloading paper). IA is acknowledged to degrade at low SNR and under imperfect CSI; the analysis assumes a single active user per cell band and rotary-wing UAVs that hover (static) while transmitting. Results are simulation-based.

## Relation to the corpus

An early (2018) **caching-UAV + physical-layer-security** anchor. Its friendly-jamming-for-secrecy idea connects to [[cooperative-jamming]] / [[friendly-jamming-uav]] and the secure-MEC thread (e.g. [[michailidis-2024-secure-ris-uav-mec-iot]]), while its EL/BL transcode-and-cache structure relates to the video-caching tradeoffs in [[chen-2024-dro-video-caching]] and [[video-transcoding-tradeoff]]. It shares an author neighborhood (Nan Zhao, Jie Tang, Yunfei Chen, F. Richard Yu) with the UAV emergency-networks paper [[zhao-2019-uav-emergency-disasters]]; the recurring **Nan Zhao** identity is flagged for human confirmation rather than promoted to an entity page here.

## Raw artifacts

- `raw/sources/Caching_UAV_Assisted_Secure_Transmission_in_Hyper-Dense_Networks_Based_on_Interference_Alignment/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
