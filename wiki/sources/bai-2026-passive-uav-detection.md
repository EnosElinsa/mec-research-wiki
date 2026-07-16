---
type: source
title: "Passive UAV Detection Based on Channel Estimation and Temporal Variation Network"
authors: ["Jing Bai", "Zhuo Zhang", "Zhu Xiao", "Huaji Zhou", "Yongqiang Hei", "Xiaohui Liu", "Tong Li", "Licheng Jiao"]
year: 2026
url: "https://doi.org/10.1109/TWC.2026.3676229"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), vol. 25, pp. 14351-14366"
modeling_card: not_applicable
tags: [source, passive-uav-detection, channel-estimation, wireless-perception, temporal-network, dtmb, field-experiment]
related:
  - "[[csi-based-passive-uav-detection]]"
  - "[[wireless-perception]]"
  - "[[pytorch]]"
  - "[[zhu-xiao]]"
created: 2026-07-14
updated: 2026-07-16
---

# Passive UAV Detection Based on Channel Estimation and Temporal Variation Network

## Citation

Bai, J., Zhang, Z., Xiao, Z., Zhou, H., Hei, Y., Liu, X., Li, T., & Jiao, L. (2026). *Passive UAV Detection Based on Channel Estimation and Temporal Variation Network*. **IEEE Transactions on Wireless Communications, 25**, 14351-14366. DOI: 10.1109/TWC.2026.3676229.

## TL;DR

Uses channel impulse responses estimated from ambient digital-TV frame headers to detect UAV presence and distinguish four flight states, with a compact temporal network that combines multi-scale local variation and periodic structure.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Bai et al. [x] studied passive UAV state detection using ambient Digital Terrestrial Multimedia Broadcast signals and a single receiving antenna. They estimated channel state information from DTMB frame headers and arranged consecutive channel impulse responses as time series that capture UAV-induced propagation changes. Their CETVNet classifier combines an adaptive noise reduction module with a multi-period feature extraction module to preserve local variations and learn periodic motion patterns. The authors trained and evaluated the network on real signals collected with a software-defined radio for four UAV motion states and a no-UAV state across three DTMB frame-header modes. Experiments reported five-class accuracies of 96.92%, 94.45%, and 98.79% for the three modes, an average false-alarm rate of 0.44%, and cross-scene binary detection accuracy of at least 97.97%.

## Problem and system model

The receiver listens to an existing Digital Terrestrial Multimedia Broadcast (DTMB) transmitter through one ground antenna and one USRP B210 channel, so the UAV carries no cooperative radio payload. After pseudo-noise synchronization and least-squares channel estimation, the system treats sequences of channel-impulse-response magnitudes as passive sensing data.

The five labels are horizontal flight with the fuselage parallel to the receiving-antenna boresight, horizontal flight perpendicular to it, vertical flight, hovering, and no UAV. Data cover three DTMB frame-header modes, three DJI platform sizes, and two outdoor scenes.

## Method

The [[csi-based-passive-uav-detection|temporal variation network]] combines two feature paths. An adaptive noise reduction module applies temporal average pooling at scales 2, 3, and 4, fuses the paths with 1 x 1 convolutions, and preserves a residual connection. A multi-period feature extraction module reshapes the sequence at periods 8, 16, and 32 and applies multi-scale two-dimensional Inception blocks. The implementation uses [[pytorch|PyTorch]].

## Key findings

- Five-class accuracy is 96.92%, 94.45%, and 98.79% across the three evaluated DTMB modes; average false-alarm rate is 0.44%.
- Cross-scene five-class accuracy is 75.14% and 87.29%, while binary UAV-presence accuracy is 97.97% and 99.41%.
- When one UAV platform is excluded from training, five-class accuracy is 85.49%-88.81% and binary presence accuracy is 97.55%-99.34%.
- The network has 0.236 million parameters and 69.52 million FLOPs; reported inference latency is 0.24 ms on GPU and 1.03 ms on CPU.
- A coherent-integration baseline fails to detect all four UAV motion states under the paper's test conditions.

## Limitations

Signal collection is physical, but training and inference are offline on a GTX 1080/Xeon workstation; no edge deployment or receiver power measurement is reported. The output is presence and coarse motion-state classification, not localization, tracking, platform identification, or multi-target detection. Evaluation is limited to two scenes, one ambient illuminator family, and three platform sizes, under assumptions including moderate-to-high SNR, independent noise, and local stationarity.

## Relation to the corpus

This source extends [[wireless-perception]] to non-cooperative aerial-target detection using broadcast-channel temporal variation. It is distinct from UAV-mounted radar and ISAC systems because the illuminator is an ambient DTMB transmitter and the sensing receiver is passive.

## Raw artifacts

- Parse: `raw/sources/Passive_UAV_Detection_Based_on_Channel_Estimation_and_Temporal_Variation_Network/Passive_UAV_Detection_Based_on_Channel_Estimation_and_Temporal_Variation_Network.md`
- Origin PDF and extracted figures (`images/`) are in the same folder.
