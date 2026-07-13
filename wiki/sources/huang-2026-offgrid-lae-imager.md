---
type: source
title: "Learned Off-Grid Imager for Low-Altitude Economy With Cooperative ISAC Network"
authors: ["Yixuan Huang", "Jie Yang", "Shuqiang Xia", "Chao-Kai Wen", "Shi Jin"]
year: 2026
url: "https://doi.org/10.1109/TWC.2025.3603255"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), 25, 2026"
tags: [source, low-altitude-economy, integrated-sensing-and-communication, wireless-perception, compressed-sensing, wireless-imaging, physics-embedded-learning]
related:
  - "[[shi-jin]]"
  - "[[low-altitude-intelligent-network]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[wireless-perception]]"
  - "[[cramer-rao-bound]]"
  - "[[tang-2025-cooperative-isac-lae]]"
  - "[[jiang-2025-isac-lae-overview]]"
  - "[[yang-2026-generative-radio-map-lae]]"
created: 2026-07-07
updated: 2026-07-14
---

# Learned Off-Grid Imager for Low-Altitude Economy With Cooperative ISAC Network

## Citation

Huang, Y., Yang, J., Xia, S., Wen, C.-K., & Jin, S. (2026). *Learned Off-Grid Imager for Low-Altitude Economy With Cooperative ISAC Network*. **IEEE Transactions on Wireless Communications**, 25, 3333-3348. DOI: 10.1109/TWC.2025.3603255. (DOI appears in the parse; volume/year/pages verified against the title-matched Crossref/IEEE DOI record.)

## TL;DR

Formulates low-altitude flight-activity surveillance as cooperative ISAC wireless imaging. Multiple synchronized full-duplex base stations use OFDM sensing signals and raw CSI measurements to reconstruct sparse aerial images, rather than first estimating target parameters and then associating them. The paper analyzes point spread functions for system design and proposes a physics-embedded learning method with OHEM-style loss design to reduce off-grid errors for UAV detection.

## Problem framing

Low-altitude economy surveillance must detect sparse, mobile, and sometimes uncooperative UAVs over large 3D regions. GNSS can be jammed or disabled, camera-based systems fail in poor visibility and require extra hardware, and traditional monostatic or localization-first RF methods suffer from result fusion, parameter matching, and data-association errors. Cooperative ISAC turns existing cellular infrastructure into a passive imaging network.

## System model

- Multiple full-duplex BSs with vertically aligned UPAs surround a 3D region of interest.
- BSs are synchronized by optical fiber and use OFDM subcarriers.
- Communication and sensing beams are designed to be spatially orthogonal while BSs serve downlink users and sense the ROI.
- The sensing model includes monostatic and multistatic returns; a CPU collects channel estimates and reconstructs the aerial scattering-coefficient image.

## Method

The paper first derives a CS-based on-grid imaging formulation and a point spread function (PSF) to assess resolution effects from antenna layout, subcarrier count, bandwidth, and voxel size. It then addresses off-grid target locations by feeding physics-derived primary results into a DNN, rather than relying on black-box CSI-to-image learning. Online hard example mining is added to the loss functions so training focuses on difficult positive/negative voxel samples in a highly sparse airspace.

## Key findings

- Under off-grid conditions, the proposed physics-embedded method using $\mathbf A^H \mathbf y$ as DNN input reports the strongest overall sensing metrics in Table III, with MSE 0.0009, SSIM 0.9186, OSPA 7.5957, DR 86.24%, FAR 3.29%, and 13.35 ms GPU runtime.
- The loss-function ablation reports Net-10 reaching the highest detection rate, 97.55%, with FAR 3.22%; Net-9 gives the strongest accuracy-oriented tradeoff in MSE/SSIM/OSPA.
- The OHEM ratio has to be tuned: too few negative samples yields false non-zero voxels, while too many pushes the network toward all-zero images.
- Sionna urban-canyon experiments show the method remains useful in 3D ROI imaging, but residual building interference degrades SSIM and detection rate; beamforming/background-removal suppression is critical.
- The communication-sensing tradeoff experiment reports negligible communication degradation when imaging occupies only a small fraction of frame resources and the sensing-signal interference remains much weaker than the desired communication signal.

## Limitations / future work

Future work includes improving detection rates in complex environments, reducing DNN training overhead, dynamic imaging for UAV tracking across successive time instants, field trials in live commercial networks, and applying the framework to other CS-based off-grid problems such as channel estimation.

## Relation to the corpus

This source extends the LAE-ISAC track from beamforming/trajectory control into cooperative wireless imaging. It complements [[tang-2025-cooperative-isac-lae]]: both use multiple BSs for low-altitude sensing, but this paper reconstructs sparse aerial images directly from CSI instead of fusing estimated positions. It strengthens [[wireless-perception]], [[integrated-sensing-and-communication]], and [[low-altitude-intelligent-network]], and is adjacent to [[yang-2026-generative-radio-map-lae]] through physics-guided processing of wireless measurements.

## Raw artifacts

- `raw/sources/Learned Off-Grid Imager for Low-Altitude Economy With Cooperative ISAC Network/Learned Off-Grid Imager for Low-Altitude Economy With Cooperative ISAC Network.md`
- Original PDF and extracted figures (`images/`) in the same folder.
