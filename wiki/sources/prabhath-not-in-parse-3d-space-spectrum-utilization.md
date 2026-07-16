---
type: source
modeling_card: not_applicable
title: "Analysis of 3D Space Spectrum Utilization in UAV-Enabled Cellular Networks"
authors: ["Kasun Prabhath", "Sudharman K. Jayaweera"]
year: ""
url: ""
venue: ""
tags: [source, uav-communications, spectrum-utilization, three-dimensional-frequency-reuse, channel-modeling, non-terrestrial-network, cellular-network]
related:
  - "[[spectrum-utilization-efficiency]]"
  - "[[three-dimensional-frequency-reuse]]"
  - "[[cellular-connected-uav]]"
  - "[[non-terrestrial-network]]"
  - "[[air-to-ground-channel-model]]"
  - "[[zeng-2019-uav-comm-tutorial-5g]]"
  - "[[mozaffari-2019-uav-wireless-tutorial]]"
created: 2026-07-11
updated: 2026-07-16
---

# Analysis of 3D Space Spectrum Utilization in UAV-Enabled Cellular Networks

## Citation

Prabhath, K., & Jayaweera, S. K. *Analysis of 3D Space Spectrum Utilization in UAV-Enabled Cellular Networks*. Venue / year / DOI: **not in parse**. A title/author Crossref lookup did not return a reliable title-matched record, so publication metadata is left blank rather than inferred from references or author biographies.

## TL;DR

Builds an analytical framework for link spectral efficiency (SE) and [[spectrum-utilization-efficiency|spectrum utilization efficiency (SUE)]] in 3-D UAV-enabled cellular networks. The model uses [[three-dimensional-frequency-reuse|truncated-octahedron 3-D frequency reuse]], partially loaded channels, random waypoint UAV-UE mobility, and free-space, log-normal, and Nakagami-m channel models to quantify how co-channel interference, cell radius, blocking probability, and fading affect volumetric spectrum use.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Prabhath and Jayaweera [x] analyzed link spectral efficiency and volumetric spectrum utilization efficiency in three-dimensional UAV-enabled cellular networks. Their framework combines truncated-octahedron frequency reuse, partially loaded channels, random-waypoint UAV mobility, and free-space, log-normal, and Nakagami-$m$ propagation models. They derived average expressions and upper and lower bounds under best-case and worst-case user and interference geometries. The numerical analysis varies cell radius, normalized reuse distance, blocking probability, shadowing variance, and fading parameters. Simulations report that reducing the cell radius from 800 m to 600 m increases average spectrum utilization efficiency by up to 0.78 bit/s/Hz/km$^3$ in the stated setup.

## Problem

Spectrum efficiency in aerial networks cannot be captured by single-link SE alone. UAV/HAPS/NTN systems operate in 3-D space, where user distributions, co-channel interference, frequency reuse, and channel load vary over volume and time. The paper targets the missing analytical framework for evaluating both link SE and system-level SUE under partially loaded 3-D aerial cellular conditions.

## System model

- Downlink UAV-gNB to UAV-UE communication in a 3-D cellular region.
- Frequency reuse cells are modeled as truncated octahedra, with 14 first-tier co-channel interferers.
- Channel utilization is partially loaded or fully loaded, modeled through a binomial activation/blocking-probability term.
- UAV-UEs follow a random waypoint mobility model inside a bounded 3-D region.
- Propagation models include free-space path loss, log-normal fading, and Nakagami-m fading.

## Method

The paper derives upper/lower bounds and average expressions for link SE and SUE under best-case and worst-case user/interference geometries. It combines the 3-D frequency reuse geometry with probabilistic channel utilization and then evaluates sensitivity to cell radius, normalized reuse distance, blocking probability, shadowing variance, and Nakagami fading parameters.

## Key findings

- Reducing the cell radius from 800 m to 600 m increases average SUE by up to 0.78 bit/s/Hz/km^3 in the reported simulations.
- Raising blocking probability from `1e-12` to 0.5 can increase average SUE by up to 0.088, but it lowers link SE.
- Log-normal shadowing with `sigma_LOS = 3 dB` reduces average SUE by up to 0.024 relative to the free-space case; increasing `sigma_LOS` from 3 dB to 6 dB reduces SUE by up to 0.054.
- Nakagami-m fading with `m_d = 3` reduces average SUE by up to 0.031.
- The simulation setup includes 5030-5091 MHz, 100 channels, default 800 m cell radius, 10 m inner radius, and 5000 m UAV-gNB altitude.

## Limitations / future work

The parse appears to start mid-introduction and corrupts several formulas. The analysis focuses on U2U downlink communication; the authors state that A2G and integrated space-air-ground adaptations are possible but require propagation and mobility adjustments. The paper also reports analytical mismatch in larger normalized reuse-distance regimes where noise becomes more important.

## Relation to the corpus

This is a spectrum/channel-modeling anchor, not an MEC offloading source. It sharpens the wiki's [[cellular-connected-uav]] and [[non-terrestrial-network]] vocabulary by adding a volumetric spectrum-efficiency metric and a 3-D frequency-reuse geometry. It complements the broader UAV-communication surveys [[zeng-2019-uav-comm-tutorial-5g]] and [[mozaffari-2019-uav-wireless-tutorial]], and is adjacent to [[air-to-ground-channel-model]] because its U2U results are framed as extendable to A2G and SAGIN cases.

## Raw artifacts

- `raw/sources/Analysis_of_3D_Space_Spectrum_Utilization_in_UAV-Enabled_Cellular_Networks/Analysis_of_3D_Space_Spectrum_Utilization_in_UAV-Enabled_Cellular_Networks.md`
- Original PDF and extracted figures (`images/`) in the same folder.
