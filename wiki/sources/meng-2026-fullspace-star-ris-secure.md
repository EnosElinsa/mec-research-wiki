---
type: source
title: "Full-Space UAV Trajectory Design for STAR-RIS-Assisted Secure Ground–Air Communications"
authors: ["Xiangyun Meng", "Xuanli Wu"]
year: 2026
url: "https://doi.org/10.1109/TGCN.2025.3581390"
venue: "IEEE Transactions on Green Communications and Networking (IEEE TGCN)"
tags: [source, star-ris, physical-layer-security, full-space-trajectory, noma, robust-optimization, csi-uncertainty]
related:
  - "[[full-space-star-ris-uav-trajectory]]"
  - "[[star-ris]]"
  - "[[physical-layer-security]]"
  - "[[csi-estimation-error]]"
  - "[[noma]]"
  - "[[uav-trajectory-control]]"
  - "[[alternating-optimization-sdr-sca]]"
created: 2026-07-13
updated: 2026-07-13
---

# Full-Space UAV Trajectory Design for STAR-RIS-Assisted Secure Ground–Air Communications

## Citation

Meng, X., & Wu, X. (2026). *Full-Space UAV Trajectory Design for STAR-RIS-Assisted Secure Ground–Air Communications*. **IEEE Transactions on Green Communications and Networking**, 10, 376-388. DOI: 10.1109/TGCN.2025.3581390.

## TL;DR

Introduces a binary side variable and unified cascaded-channel expressions so a UAV can cross a STAR-RIS plane while collecting one secure and one regular NOMA uplink. DS-JO alternates robust STAR-RIS coefficient/role optimization with trajectory SCA to maximize worst-case average secrecy rate under colluding-eavesdropper CSI uncertainty.

## Problem framing

Conventional STAR-RIS formulas assume each terminal remains on a fixed reflecting or transmitting side. When a mobile UAV crosses the surface plane, the node roles and cascaded channels switch, making half-space formulas unsuitable for unconditional trajectory planning. The paper seeks full-space mobility while protecting node-A's confidential traffic and preserving node-B throughput.

## System model

- Two single-antenna ground nodes upload through an `M`-element fixed STAR-RIS to a single-antenna rotary-wing UAV at fixed altitude.
- Node-A is confidential; node-B has no secrecy requirement. Colluding eavesdroppers in area-A target node-A and treat node-B as interference.
- The STAR-RIS uses energy splitting. A binary variable maps the UAV side to reflection/transmission roles for both nodes.
- The UAV uses a fixed worst-case SIC order: decode node-A first, then node-B, with a received-power separation constraint.
- Legitimate CSI is perfect; eavesdropper CSI lies in a known norm-bounded uncertainty set.

## Method

The robust mixed-integer problem maximizes node-A's worst-case average secrecy rate over STAR-RIS coefficients, UAV trajectory, and side variables, subject to node-B data, SIC, surface, and mobility constraints. [[full-space-star-ris-uav-trajectory|DS-JO]] alternates two blocks. The fixed-trajectory block relaxes binary/rank constraints, applies first-order convexification and the S-Procedure, solves an SDR, and uses Gaussian randomization. The fixed-coefficient block bounds location-dependent channel terms and applies SCA to the trajectory. The paper claims monotonic convergence to a local/suboptimal solution.

## Key findings

- DS-JO and single-side JO stabilize after four reported AO iterations.
- In the `N=25` full-space example, the UAV approaches node-A, hovers above it, then departs.
- Reflection amplitude dominates in area-A; transmission amplitude dominates during the final seven slots in area-B.
- DS-JO is reported above fixed-trajectory, random-phase, and conventional-reflecting benchmarks as STAR-RIS element count grows, but the parse gives no numerical margins.
- More node-B power can improve secrecy by jamming the eavesdroppers, except for the fixed-trajectory baseline where inter-user interference at the UAV dominates.

## Limitations / parse caveats

The model has two nodes, fixed altitude, single antennas, energy-splitting STAR-RIS operation, perfect legitimate CSI, known uncertainty radius, and offline numerical optimization. SIC order is fixed, all eavesdroppers occupy one side, and validation is simulation-only. Different endpoints in double- and single-side trajectory plots weaken direct benchmark fairness. The positive-part secrecy operator disappears in later objectives without explanation, boundary handling for the side variable is unclear, and several equations/Algorithm 1 fields are damaged.

## Relation to the corpus

This source adds [[full-space-star-ris-uav-trajectory]] to the [[star-ris]] line. Existing STAR-RIS MEC pages use a surface with fixed role geometry for bidirectional task offloading; here the UAV crosses the surface plane, so role switching, robust secrecy, and trajectory control become one coupled physical-layer problem rather than an MEC offloading design.

## Raw artifacts

- Parse: `raw/sources/Full-Space_UAV_Trajectory_Design_for_STAR-RIS-Assisted_Secure_Ground-Air_Communications/Full-Space_UAV_Trajectory_Design_for_STAR-RIS-Assisted_Secure_Ground-Air_Communications.md`
- Origin PDF: `raw/sources/Full-Space_UAV_Trajectory_Design_for_STAR-RIS-Assisted_Secure_Ground-Air_Communications/Full-Space_UAV_Trajectory_Design_for_STAR-RIS-Assisted_Secure_Ground-Air_Communications.pdf`
- Figures: `raw/sources/Full-Space_UAV_Trajectory_Design_for_STAR-RIS-Assisted_Secure_Ground-Air_Communications/images/`
