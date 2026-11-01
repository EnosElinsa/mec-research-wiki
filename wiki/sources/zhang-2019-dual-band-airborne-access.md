---
type: source
title: "Channel Measurement and Resource Allocation Scheme for Dual-Band Airborne Access Networks"
authors: ["Ruonan Zhang", "Qi Guo", "Daosen Zhai", "Deyun Zhou", "Xiaojiang Du", "Mohsen Guizani"]
year: 2019
url: "https://doi.org/10.1109/ACCESS.2019.2923538"
venue: "IEEE Access, 7"
modeling_card: required
tags: [source, aerial-base-station, airship, channel-measurement, dual-band, spectrum-assignment, power-allocation, lagrange-dual]
related:
  - "[[air-to-ground-channel-model]]"
  - "[[high-altitude-platform-station]]"
  - "[[mixed-integer-nonlinear-programming]]"
  - "[[ruonan-zhang]]"
  - "[[daosen-zhai]]"
created: 2026-11-02
updated: 2026-11-02
---

# Channel Measurement and Resource Allocation Scheme for Dual-Band Airborne Access Networks

## Citation

Zhang, R., Guo, Q., Zhai, D., Zhou, D., Du, X., & Guizani, M. (2019). *Channel Measurement and Resource Allocation Scheme for Dual-Band Airborne Access Networks*. **IEEE Access, 7**. DOI: 10.1109/ACCESS.2019.2923538.

## TL;DR

An aerial base station (ABS) on an airship serves ground users with both a UHF band, for long range, and an S-band, for bandwidth. The authors measure air-to-ground large-scale fading at 785 and 2160 MHz from 50 to 950 m altitude over distances up to 70 km, then maximize sum rate by jointly assigning users to bands and allocating power.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: One airship ABS serves a set $\mathcal K$ of ground users under the dual-band aerial access (DBAA) scheme. A low-frequency band has $N_l$ subchannels of width $B_l$ and a high-frequency band has $N_h$ subchannels of width $B_h$. Path loss and shadowing follow the measured A2G models for each band.

**Problem & objective**: Problem (8), a mixed-integer program: $\max_{\mathbf X,\mathbf P}\sum_{k\in\mathcal K}\big(x_kR^l_k+(1-x_k)R^h_k\big)$, the sum rate over both bands.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Band assignment | $x_k$ | binary | 1 if user $k$ gets a low-frequency subchannel, 0 for high-frequency |
| Power | $p_k$ | $p_k\ge0$ | Transmit power to user $k$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Total ABS power, $\sum_kp_k\le P^{tot}$. |
| C2 | Low-band capacity, $\sum_kx_k\le N_l$. |
| C3 | High-band capacity, $\sum_k(1-x_k)\le N_h$. |
| C4-C5 | $x_k\in\{0,1\}$ and $p_k\ge0$. |

**Algorithm**: Design a low-complexity spectrum assignment rule for given power, then obtain the optimal power allocation with the Lagrange dual method, and combine them into joint allocation.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zhang et al. [x] proposed a hybrid-spectrum scheme for airborne access networks, named dual-band aerial access, in which an aerial base station uses both UHF and S-bands to provide connectivity for ground users. The scheme improves coverage range and reliability through the favorable propagation of the low-frequency band and increases throughput through the large bandwidth of the high-frequency band. Following a cross-layer approach, they conducted a measurement campaign on the large-scale fading of air-to-ground channels at 785 and 2160 MHz simultaneously, with an aerial base station on an airship hovering at altitudes from 50 to 950 m and a ground terminal moving in rural, suburban, and urban scenarios up to 70 km away. Based on the measured channel models, they designed a joint spectrum-and-power allocation algorithm to maximize network throughput. Simulation results show that joint allocation increases the total data rate by 55% compared with random allocation, with spectrum assignment contributing more gain than power allocation.

## Problem framing

Emergency ABSs face limited onboard power, long distances, and scarce spectrum. Low bands reach far with little loss; high bands give capacity close in. Assigning each user to a band trades the two.

## System model

- Measured path loss and shadowing at both frequencies in three environment types.
- Rate per user depends on band bandwidth, channel gain, and allocated power.

## Method

The optimal assignment policy depends on the sign of $B_lG^l_k-B_hG^h_k$ and on power, giving the low-complexity rule; the Lagrange dual then sets powers.

## Key findings

- Joint allocation raises total data rate by 55% relative to random allocation.
- Spectrum assignment contributes about 36% gain and power allocation about 19%.

## Limitations / future work

The model uses one ABS and large-scale fading only.

## Relation to the corpus

Measured airship A2G models complement [[air-to-ground-channel-model]] and the airship deployments under [[high-altitude-platform-station]].

## Raw artifacts

- Parse: `raw/sources/Channel_Measurement_and_Resource_Allocation_Scheme_for_Dual-Band_Airborne_Access_Networks/Channel_Measurement_and_Resource_Allocation_Scheme_for_Dual-Band_Airborne_Access_Networks.md`
- Origin PDF and extracted figures are in the same folder.
