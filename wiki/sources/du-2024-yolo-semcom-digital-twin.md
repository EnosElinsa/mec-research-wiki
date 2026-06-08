---
type: source
title: "YOLO-Based Semantic Communication With Generative AI-Aided Resource Allocation for Digital Twins Construction"
authors: ["Baoxia Du", "Hongyang Du", "Haifeng Liu", "Dusit Niyato", "Peng Xin", "Jun Yu", "Mingyang Qi", "You Tang"]
year: 2024
url: "https://doi.org/10.1109/JIOT.2023.3317629"
venue: "IEEE Internet of Things Journal (IEEE IoT-J)"
tags: [source, semantic-communication, yolov7-object-detection, generative-diffusion-model, diffusion-model-as-optimizer, digital-twin, uav-data-collection, resource-allocation]
related:
  - "[[semantic-communication]]"
  - "[[yolov7-object-detection]]"
  - "[[generative-diffusion-model]]"
  - "[[diffusion-model-as-optimizer]]"
  - "[[generative-ai-for-mec]]"
  - "[[digital-twin]]"
  - "[[uav-data-collection]]"
  - "[[ddqn]]"
  - "[[zheng-2024-semcom-sec-offloading]]"
  - "[[sun-2024-mfris-semantic-antijamming]]"
  - "[[du-2024-d2sac-aigc-asp-selection]]"
  - "[[ye-2025-aigc-diffusion-contract]]"
  - "[[yang-2024-taco-human-digital-twin-edge]]"
created: 2026-06-02
updated: 2026-06-08
---

# YOLO-Based Semantic Communication With Generative AI-Aided Resource Allocation for Digital Twins Construction

## Citation

Du, B., Du, H., Liu, H., Niyato, D., Xin, P., Yu, J., Qi, M., & Tang, Y. (2024). *YOLO-Based Semantic Communication With Generative AI-Aided Resource Allocation for Digital Twins Construction*. **IEEE Internet of Things Journal**. DOI: 10.1109/JIOT.2023.3317629. (Manuscript received 23 June 2023; revised 19 August 2023; accepted 10 September 2023; date of publication 20 September 2023; date of current version 21 February 2024. Corresponding authors: Mingyang Qi; You Tang. Volume/issue/pages not in parse.)

## TL;DR

A [[semantic-communication]] framework for building a [[digital-twin|digital twin]] of an apple orchard while cutting the cost of transmitting UAV-captured images. A UAV runs a [[yolov7-object-detection|YOLOv7-X]] object detector to extract only the **semantic information** (cropped apple images + confidence + position) instead of sending whole images, then allocates limited transmission power across those crops by their **importance**. Importance is read from the detector's confidence. Two allocation schemes are proposed — a **confidence-based** rule (Conf-SemCom) and an **AI-generated** scheme that uses a [[generative-diffusion-model|diffusion model]] as the power-allocation optimizer ([[diffusion-model-as-optimizer]]) — both compared against an average-allocation baseline (Avg-SemCom). The detector is also slimmed and sharpened (ELAN-H + SimAM → "YOLOv7-HS") for edge deployment.

## Problem framing

Keeping a digital twin synchronized with a dynamic physical world (here, a fruit orchard) requires edge devices such as UAVs to continuously capture and transmit large volumes of data (e.g. high-definition images). Sending every image is expensive and strains the wireless link. The paper's premise: for orchard management the user only cares about the fruit, so transmitting the *meaning* of an image (which apples, where, how confidently detected) rather than the full image both reduces data volume and lets scarce transmission power be steered toward the most important content. Prior semantic-communication work, the authors argue, ignores the **varying importance** of different pieces of semantic information, risking the loss of critical content under channel competition.

## System model

- **Pipeline.** Apple trees → UAV takes photos along a trajectory → YOLOv7-HS detects apples and emits cropped apple images with confidence and position → importance-based power allocation → transmit semantic information to users/applications ([[uav-data-collection]]).
- **Importance score.** For object $i$ with detector confidence $c_i$, importance $W_i = c_i^{\sigma}$ ($\sigma$ tunes the spread; default $\sigma = 1$, confidence threshold $c_\min = 0.25$).
- **MIST metric.** The authors define a *metric for image semantic transmission* (MIST): $E = A \sum_i (W_i \times Q(p_i))$, where $A$ is the detector's extraction accuracy (AP@0.5) and $Q(p_i)$ is the post-transmission [[semantic-communication|SSIM]] of object $i$, increasing in allocated power $p_i$. The objective maximizes MIST subject to a total power budget $\sum_i p_i \le P$.
- **Channel.** Fisher–Snedecor $\mathcal{F}$ fading model (Nakagami-$m$ small-scale fading + inverse-Nakagami-$m$ shadowing); default fading/shadowing parameters $m_f = m_s = 6$, default transmit power $P = 3000$ W (and $P = 4$ kW in the diffusion-scheme comparison — large simulation values, stated as set "by default").

## Method

- **Detector enhancement (YOLOv7-HS).** Two modifications to YOLOv7-X, both placed in the Neck:
  - **ELAN-H** — the ELAN-X module is simplified (long branch cut from seven to three CBS convolutions, output feature maps reduced to four) and one CBS convolution replaced by a **HorNet block** (recursive gated convolution, $g^n\text{Conv}$) to recover the lost detection capability while cutting parameters/FLOPs.
  - **SimAM** — a parameter-free 3-D attention module (energy-function-based neuron importance) integrated to focus the model without adding parameters.
- **Conf-SemCom (confidence-based allocation).** Sort detected crops by confidence and assign power by priority weight $w_i = c_i^{\eta}$ ($\eta$ tunes how steeply power favors high-confidence crops), using the power-allocation routine of the cited prior work.
- **AI-generated allocation (diffusion-as-optimizer).** A conditional reverse-diffusion policy $\pi_\theta(\mathbf{w}\mid\mathbf{e})$ maps an environment vector $\mathbf{e}$ (channel model, total power $P$, number of objects $U$) to power weights, trained DRL-style: a quality network $Q_\nu$ scores allocations, optimized with **double Q-learning** ([[ddqn]]) twin critics + target networks + soft updates, exploration noise added during training (DDPM formulation). Inference needs only **five** denoising steps. This is the same "diffusion model generates the decision" pattern as [[diffusion-model-as-optimizer]], motivated by the AI-generated-contract line of work.

## Key findings

- **Detector ablation (Table III).** YOLOv7-X baseline: 70.7M params, 188.0G FLOPs, AP@0.5 87.8%, AP@0.5:0.95 43.7%. Adding ELAN-H: 53.5M params, 152.6G FLOPs, AP@0.5 89.1%, AP@0.5:0.95 45.4% — i.e. **+1.3% AP@0.5 and +1.7% AP@0.5:0.95 while cutting parameters ~24% and FLOPs ~19%** (the authors' stated reductions). Adding SimAM further: AP@0.5 89.8% (**+0.8%**) with no parameter/FLOP change.
- **Detector comparison (Table IV).** The enhanced model ("Ours", 53.5M / 152.6G / AP@0.5 89.8% / AP@0.5:0.95 45.4% / 34 FPS) attains the **best AP@0.5** and the **fastest detection speed** among the compared detectors (Faster R-CNN, RetinaNet, FCOS, Scaled-YOLOv4-p5, YOLOX-X, YOLOv5-X, YOLOR-CSP-X, PPYOLOE-X) on MinneApple, with far fewer parameters/FLOPs than the other high-AP YOLO-series models.
- **Communication-cost reduction (§V-B).** Over 331 unannotated MinneApple test images, the aggregate original image size 595.2 MB drops to 55.4 MB after semantic feature extraction (54.8 MB image + 0.6 MB text) — a **91% reduction in communication cost**.
- **Conf-SemCom vs Avg-SemCom.** Conf-SemCom yields higher MIST scores than average allocation in most cases, with the gap widening as transmission distance grows; the best $\eta$ rises with distance (η ≈ 0.5 at 10 m, 0.75 at 20 m, 1 at 30 m). It also reduces bit-error rate for high-importance crops under poor channels.
- **AI-generated scheme.** The diffusion-based allocator overtakes the confidence-based scheme at roughly 500 training iterations and attains the highest MIST score in the reported comparison (D = 20 m, P = 4 kW); Avg-SemCom trails both, underscoring that importance-aware allocation matters.

## Limitations / future work

- **Single-class case study.** The evaluation is a virtual apple orchard on the MinneApple dataset (670 labeled + 331 unlabeled images); the authors note the semantic-extraction module is **replaceable** with other pretrained detectors for other object classes, but this generalization is asserted rather than demonstrated.
- **Simulated capture.** UAV image acquisition is *simulated* using a real apple dataset rather than collected from actual flights; the channel is a statistical Fisher–Snedecor model. No hardware/field trial.
- **Indicative magnitudes.** Several reported numbers (MIST and SSIM/BER curves vs $\eta$ and distance, training-iteration crossover) are read from the paper's figures and should be treated as trends; the table-reported detector metrics and the 595.2 MB → 55.4 MB / 91% reduction are stated numerically in the paper. The default transmit-power settings (3000 W; 4 kW) are large simulation parameters stated as defaults.

## Relation to the corpus

A [[semantic-communication]] entry that, unlike other semantic-communication sources in the wiki, pairs the paradigm with a concrete edge **object-detection** front end and a generative power allocator. It is the offloading/transmission counterpart to [[zheng-2024-semcom-sec-offloading]] (semantic communication for satellite-borne edge-cloud *computation offloading*) and to [[sun-2024-mfris-semantic-antijamming]] (semantic transceiver + multi-functional RIS under jamming) — where those optimize a semantic *computation/transmission rate*, this paper optimizes an importance-weighted transmission-quality metric (MIST) and additionally builds a [[digital-twin]] from the recovered content. Its AI-generated allocation scheme is a [[diffusion-model-as-optimizer]] instance, sharing that pattern (and overlapping authorship) with [[du-2024-d2sac-aigc-asp-selection]] and [[ye-2025-aigc-diffusion-contract]], and it extends the [[generative-ai-for-mec]] thread toward digital-twin synchronization. On the digital-twin axis it sits beside [[yang-2024-taco-human-digital-twin-edge]] (human-digital-twin deployment at the edge). It also grounds [[yolov7-object-detection]] as an actively-modified detector (ELAN-H + SimAM) rather than an assumed black box. The author neighborhood overlaps the generative-AI cluster — Dusit Niyato ([[dusit-niyato]]) is a confirmed entity; Hongyang Du recurs across the corpus. The remaining co-authors (Baoxia Du, Haifeng Liu, Peng Xin, Jun Yu, Mingyang Qi, You Tang; Jilin-area institutions) appear once and are not promoted.

## Raw artifacts

- `raw/sources/YOLO-Based_Semantic_Communication_With_Generative_AI-Aided_Resource_Allocation_for_Digital_Twins_Construction/full.md`
- Original PDF (`72143137-933e-46b2-b1e8-aaf9d3713ec3_origin.pdf`) and extracted figures (`images/`) in the same folder.
