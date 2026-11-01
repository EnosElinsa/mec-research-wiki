---
type: source
title: "Energy Efficient Spectrum Sharing and Resource Allocation for 6G Air-Ground Integrated Networks"
authors: ["Tao Huang", "Jingyuan Liu", "Zheng Chang", "Yao Wei", "Xu Zhao", "Ying-Chang Liang"]
year: 2025
url: "https://doi.org/10.1109/TNSM.2025.3527651"
venue: "IEEE Transactions on Network and Service Management, 22(4)"
modeling_card: required
tags: [source, spectrum-sharing, spectrum-pricing, stackelberg-game, high-altitude-platform-station, air-ground-integrated-network, energy-efficiency]
related:
  - "[[stackelberg-game]]"
  - "[[air-ground-integrated-network]]"
  - "[[high-altitude-platform-station]]"
  - "[[licensed-unlicensed-spectrum-sharing]]"
  - "[[zheng-chang]]"
created: 2026-11-02
updated: 2026-11-02
---

# Energy Efficient Spectrum Sharing and Resource Allocation for 6G Air-Ground Integrated Networks

## Citation

Huang, T., Liu, J., Chang, Z., Wei, Y., Zhao, X., & Liang, Y.-C. (2025). *Energy Efficient Spectrum Sharing and Resource Allocation for 6G Air-Ground Integrated Networks*. **IEEE Transactions on Network and Service Management, 22**(4). DOI: 10.1109/TNSM.2025.3527651.

## TL;DR

A HAP owns the spectrum in an area where autonomous aerial vehicles (AAVs) must serve or execute missions. The HAP sets spectrum prices and its own transmit power, and each AAV chooses transmit power to balance task revenue against power and spectrum costs. The leader-follower game is solved by convex optimization to a Stackelberg equilibrium without degrading HAP QoS.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: One HAP and $M$ AAVs share the HAP's spectrum. The HAP serves its own users with power $P^H_{h,n,k}$ and sells spectrum to AAV $m$ at price share $\mu_m$; AAV $m$ transmits with power $P^U_{m,k}$ and earns revenue from executing tasks.

**Problem & objective**: Stackelberg game. P1 (leader, HAP): $\max_{\boldsymbol\mu,\mathbf P^H}$ HAP utility from spectrum revenue and energy cost. P2 (follower, AAV $m$): $\max_{P^U_{m,k}}U_m(\mu_m,P^H_{h,n,k},P^U_{m,k})$, task revenue minus power and spectrum payments.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Spectrum price | $\mu_m$ | $0<\mu_m<1$ | Pricing applied to AAV $m$ |
| HAP power | $P^H_{h,n,k}$ | $0<P^H_{h,n,k}<P^H_{\max}$ | HAP transmit power |
| AAV power | $P^U_{m,k}$ | $0<P^U_{m,k}<P^U_{m,\max}$ | AAV transmit power |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1.1 | HAP QoS must be preserved. |
| C1.2, C2.2 | $0<\mu_m<1$. |
| C1.3 | $0<P^H_{h,n,k}<P^H_{\max}$. |
| C2.1 | AAV QoS, $R_{m,k}\ge C_{m,k}$. |
| C2.3 | $0<P^U_{m,k}<P^U_{m,\max}$. |

**Algorithm**: Derive each AAV's best-response power by convex optimization, substitute it into the HAP problem, and solve for prices and HAP power, yielding the Stackelberg equilibrium.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Huang et al. [x] investigated spectrum sharing and resource allocation for an air-ground integrated wireless network consisting of multiple autonomous aerial vehicles and a high altitude platform. They considered AAVs that must provide services or execute missions in an area where the HAP owns the spectrum and other resources. An energy efficient spectrum sharing and resource allocation scheme jointly optimizes spectrum pricing and transmit power to maximize the utilities of both the HAP and the AAVs without degrading the HAP's quality of service. A game theoretic approach determines the spectrum sharing and resource allocation strategies, and the resulting problems are addressed through convex optimization. Extensive simulations show improvements in system utility, spectrum efficiency, and energy efficiency.

## Problem framing

AAV missions need spectrum that a HAP already licenses. Pricing lets the HAP monetize spare spectrum while limiting interference to its users.

## System model

- AAV utility balances task revenue against power and spectrum payments.
- HAP utility combines spectrum revenue with its own service and power cost.

## Method

Backward induction over the Stackelberg game with convex subproblems.

## Key findings

- The scheme improves system utility, spectrum efficiency, and energy efficiency over the compared schemes.
- HAP QoS is preserved while AAVs access its spectrum.

## Limitations / future work

The paper's numerical gains are reported graphically.

## Relation to the corpus

A [[stackelberg-game]] spectrum-pricing design for the [[air-ground-integrated-network]] with a [[high-altitude-platform-station]] as spectrum owner.

## Raw artifacts

- Parse: `raw/sources/Energy_Efficient_Spectrum_Sharing_and_Resource_Allocation_for_6G_Air-Ground_Integrated_Networks/Energy_Efficient_Spectrum_Sharing_and_Resource_Allocation_for_6G_Air-Ground_Integrated_Networks.md`
- Origin PDF and extracted figures are in the same folder.
