# A Multi-Scale Feature Extraction and Fusion U-Net for Pathloss Prediction in UAV-Assisted mmWave Radio Networks

Sajjad Hussain

Abstract—Accurate pathloss prediction is essential for the design and optimization of unmanned aerial vehicles (UAV) assisted millimeter-wave (mmWave) networks. While deep learning approaches have shown strong potential, their generalization across diverse environments, robustness to noisy inputs, and sensitivity to UAV altitude remain underexplored. To address these challenges, we propose a U-Net-based deep learning architecture that combines multi-scale feature extraction, convolution-based feature fusion, and an atrous spatial pyramid pooling (ASPP) bottleneck for efficient context aggregation. The model predicts pathloss maps from log-distance, line-of-sight (LOS) mask, and building mask inputs. In addition, we develop a fully vectorized LOS mask computation algorithm that significantly accelerates pre-processing and enables large-scale dataset generation. Extensive evaluations on both in-house ray-tracing data and the RadioMapSeer benchmark demonstrate that the proposed model outperforms several state-of-the-art baselines in accuracy and efficiency. All source code is publicly released to support reproducibility and future research.

Index Terms—UAV communications, mmWave propagation, pathloss prediction, deep learning, U-Net, LOS estimation, raytracing, wireless channel modeling.

## I. INTRODUCTION

avenue for enhancing coverage, especially in urban and dense environments [1], [2]. Millimeter wave (mmWave) frequencies, particularly around 28 GHz, offer significant capacity benefits for UAV-assisted communications due to large available bandwidth. UAVs offer distinct advantages because their elevated position can mitigate the severe pathloss and blockage sensitivity of mmWave signals by improving the likelihood of maintaining LoS links with ground users. Furthermore, the short wavelength enables compact, high-gain antenna arrays on UAV platforms, facilitating narrow-beam directional transmissions that enhance spatial reuse and reduce interference in dense user scenarios. However, accurate pathloss modeling in such scenarios is challenging due to complex urban geometries, mobility, and non-line-of-sight (NLOS) conditions [3], [4].

Traditional radio channel modeling approaches, including field measurements [5], deterministic models [6], and stochastic models [7] have well-known limitations in the context of UAV-assisted communication networks. Field measurements are often site-specific and lack scalability; deterministic models such as ray-tracing are computationally intensive; and stochastic models offer limited ability to capture fine-grained spatial variations. To address these issues, classical machine learning (ML) techniques such as support vector regression (SVR), random forests (RF), k-nearest neighbors (k-NN), multi-layer perceptron (MLP), and ensemble-based models have historically been employed for pathloss prediction in UAV scenarios [8], [9], [10], [11], [12], [13]. These models leverage spatial and contextual features to approximate pathloss while offering a balance between computational efficiency and prediction accuracy.

More recently, the field has witnessed a growing trend toward the application of deep learning and generative Artificial Intelligence (AI) techniques including convolutional neural networks (CNNs), U-Net architectures, conditional generative adversarial networks (cGANs), and Transformerbased models for pathloss estimation [14], [15], [16], [17], [18], [19]. These approaches have demonstrated superior performance in capturing non-linear spatial dependencies and generalizing across diverse environments, thereby marking a significant shift in the modeling paradigm from classical ML to data-driven, end-to-end learning frameworks.

Levie et al. [14] introduced RadioUNet, a U-Net-based deep learning architecture for pathloss prediction in deviceto-device (D2D) communications at 5.9 GHz. Alongside the model, they released RadioMapSeer, a large-scale dataset of simulated radio maps that has since become a widely used benchmark in the literature. The architecture consists of two cascaded UNets: the first predicts the initial pathloss map from the input features, while the second refines this prediction by incorporating it as an additional input. Experimental results demonstrate that RadioUNet not only achieves competitive accuracy but also exhibits strong transferability to previously unseen radio environments.

Chaves-Villota et al. [15] presented DeepREM that evaluates two deep learning models, a U-Net and a cGAN, for estimating pathloss for urban scenarios from sparse reference signal received power (RSRP) measurements. While terrain and base station (BS) data are utilized during training dataset generation via intelligent ray-tracing, the models require only sparse measurements during inference. The results showed that the U-Net model performs better for RSRP prediction while cGAN variant demonstrates improved BS coverage prediction. However, the reported root mean squared error (RMSE) (approximately 6.3 dBm) is higher than some recent methods.

A U-Net–based model, termed PMNet, was proposed in [16] for large-scale pathloss map prediction and later extended in [17]. PMNet leverages supervised learning on ray-tracing and measurement data along with morphological map data to accurately estimate pathloss across geographic areas. The enhanced version of PMNet incorporates transfer learning, allowing rapid adaptation to new network environments with faster training and less data, while maintaining low RMSE.

Jiang et al. [18] proposed a U-Net-based model, termed PEFNet, for pathloss prediction in outdoor urban environments. The model employs a hybrid loss function that integrates a physics-informed component based on the volume integral equation (VIE) to estimate the total electric field (Efield) from the incident E-field, and a data-driven component that minimizes the error between predicted and measured pathloss values. The input to the network includes the BS location, buildings layout, and the incident E-field, while the output is the total E-field (comprising both incident and scattered fields). This predicted field is subsequently used to compute the pathloss. PEFNet has been evaluated on the publicly available RadioMapSeer and RSRPSet datasets, demonstrating strong performance across multiple scenarios. However, the reliance on VIE solved via the Method of Moments introduces computational overhead, which may limit scalability for electrically large environments in practical deployments.

Fang et al. in [19] introduced a novel Transformer-based architecture, RadioFormer, for radio map estimation under ultra-sparse spatial sampling conditions, achieving reliable predictions with as little as 0.01% of the full measurement grid. Departing from convolutional approaches like U-Net, RadioFormer leverages a Dual-stream Self-Attention (DSA) mechanism that separately processes signal strength correlations and building geometry features. These dual representations are fused through a Cross-stream Cross-Attention (CCA) module, enabling the model to jointly capture both fine-grained radio signal structure and large-scale environmental context. This multiple-granularity attention design allows RadioFormer to model long-range spatial dependencies essential for accurate radio map inference in obstructed and irregular environments.

Despite substantial advances in pathloss prediction through classical ML, deep learning, and more recently generative AI-based methods, several critical challenges remain insufficiently addressed. First, the generalization capability of existing models across diverse environments is largely underexplored, especially when evaluated under varying building densities or at different carrier frequencies. Second, the robustness of existing models to noisy or imperfect input, such as perturbed building layouts or measurement errors, has rarely been examined through systematic evaluation. Motivated by these limitations, this work focuses on three key research gaps: (i) evaluating the generalization of the model in urban environments with varying density, area and building counts; (ii) investigating, for the first time to the best of our knowledge, the influence of varying UAV altitudes on deep learning-based pathloss prediction; and (iii) quantifying the robustness of the model under input perturbations representative of noisy sensor conditions in the real world.

To address these challenges, we proposed a U-Net-based architecture that combines multi-scale feature extraction with convolution-based feature fusion to achieve higher prediction accuracy at reduced complexity. The network integrates an ASPP bottleneck for enhanced context aggregation across multiple receptive fields. In addition, we used a vectorized LOS mask computation algorithm, which accelerates the preprocessing pipeline and enables efficient large-scale dataset generation. Using an in-house ray-tracing model, we construct a diverse dataset spanning five representative urban scenarios, Munich (two sites), Helsinki, London, and Manhattan, with varying UAV transmitter positions and altitudes. The proposed model is evaluated using two datasets: (i) the inhouse ray-tracing dataset designed for UAV-assisted mmWave communications at 28 GHz, and (ii) the RadioMapSeer benchmark, a widely used open-access D2D communications dataset operating at 5.9 GHz. This dual evaluation enables assessment across distinct frequency bands and propagation scenarios under diverse environmental configurations with varying building densities. Performance is rigorously compared against state-of-the-art pathloss prediction models.

The main contributions of this paper are summarized as follows:

• A U-Net based multi-scale feature extraction architecture with convolution-based feature fusion, and ASPP bottleneck is proposed for efficient and accurate pathloss prediction.

• A fully vectorized LOS mask computation algorithm that significantly reduces the pre-processing time.

• Construction of a large-scale, high-fidelity synthetic dataset using an in-house ray-tracing model for UAVassisted mmWave scenarios.

• Comprehensive evaluation against state-of-the-art models, including cross-city generalization and multi-altitude performance analysis.

• Public release of the complete source code, training pipeline, and evaluation scripts to facilitate reproducibility and foster future research in this domain.<sup>1</sup>

This work focuses exclusively on large-scale pathloss under stationary channel assumptions. Effects such as UAV airframe occlusion, airframe shadowing, and channel non-stationarity arising from UAV mobility or altitude variations are not modeled and are beyond the scope of this work.

The remainder of this paper is structured as follows. Section II describes the dataset generation and system setup, including the ray-tracing framework, empirical models for NLOS receivers and building entry losses, and the construction of input features for learning. Section III presents the proposed U-Net-based architecture, highlighting the multi-scale feature extraction module, feature fusion strategy, and the ASPP bottleneck. Section IV introduces the vectorized algorithm for LOS estimation that enables efficient pre-processing. Section V outlines the training strategy and evaluation pipeline. Section VI reports the experimental results with comprehensive comparisons and analysis. Finally, Section VII concludes the paper and outlines directions for future work.

TABLE I  
ENVIRONMENT STATISTICS FOR PATHLOSS PREDICTION BENCHMARKING
<table><tr><td>Statistic</td><td>Munich-01</td><td>Munich-02</td><td>Helsinki</td><td>Manhattan</td><td>London</td></tr><tr><td>Number of Buildings</td><td>67</td><td>49</td><td>248</td><td>459</td><td>300</td></tr><tr><td>Average Building Height (m)</td><td>19.76</td><td>17.69</td><td>15.01</td><td>29.46</td><td>29.58</td></tr><tr><td>Cross-section Area  $( \mathbf { m } ^ { 2 } )$ </td><td> $4 0 8 \times 5 9 8$ </td><td> $3 7 8 \times 4 4 8$ </td><td> $1 2 2 0 \times 1 5 4 5$ </td><td> $6 9 0 \times 8 0 5$ </td><td> $1 1 2 3 \times 1 4 0 1$ </td></tr><tr><td>Average LOS Computation Time (s)</td><td>1.74</td><td>1.29</td><td>21.04</td><td>16.39</td><td>20.2</td></tr></table>

## II. DATASET GENERATION AND SYSTEM SETUP

To support supervised learning for UAV-based mmWave pathloss prediction, we construct a high-fidelity dataset using an in-house ray-tracing simulator across five diverse urban environments. These include two regions from Munich (Munich-01, Munich-02), and one each from Helsinki, London, and Manhattan. Building geometries for all sites were extracted from OpenStreetMaps vector data and processed into 3D models.

In each environment, four unique UAV transmitter locations were defined. At each transmitter location, we simulated airto-ground (A2G) propagation at three distinct UAV altitudes: 25 m, 35 m, and 45 m. This resulted in a total of $5 \times 4 \times 3 = 6 0$ transmitter deployment scenarios. UAV altitude is defined as the vertical distance above ground level (AGL), measured relative to the local ground plane immediately beneath the UAV. This AGL reference is maintained even when the UAV is positioned above buildings, ensuring a consistent metric. For each scenario, pathloss values were computed over a fixed receiver grid of size 256 × 384, with receiver height set at 1.5 m. This yields a total of 5,898,240 simulated receiver points across 60 transmitter scenarios in the dataset. A uniform grid resolution was maintained across all environments, despite differences in geometry, area, and building density. This design choice ensures consistent spatial coverage while simultaneously producing a diversified dataset, making it a strong candidate for rigorous evaluation of model generalization. In the considered downlink scenario, the UAV operates as an aerial BS transmitting at 28 GHz, while the ground nodes represent user equipment (UEs) receiving the signals. This setup models typical UAV-assisted wireless coverage in urban areas.

The UAV transmitter is modeled as an isotropic antenna operating at a carrier frequency of 28 GHz and transmit power of 30 dBm. For both the transmitter (UAV) and receivers (ground users), ideal isotropic antennas with unity gain (0 dBi) are assumed. An overview of the urban layouts and UAV transmitters horizontal locations is provided in Fig. 1, while key environment statistics are summarized in Table I.

## A. Ray-Tracing Simulation Framework

Pathloss values were computed using an in-house raytracing model [20], [21], [22] developed in Python. The model accounts for three main propagation mechanisms:

• LOS

• Ground reflection

• First-order specular reflections from building walls.

To improve the accuracy of pathloss modeling at mmWave frequencies, the model incorporates diffuse scattering effects arising from rough surfaces in addition to specular reflections. A 10λ × 10λ region centered at each reflection point is sampled at a resolution of 0.5λ, producing up to 400 secondary scattering points per reflection. The scattered field is computed using the directive scattering model proposed in [23]. To accelerate simulation, we parallelize the diffuse scattering module using Python’s concurrent.futures.ProcessPoolExecutor.

## B. Handling NLOS and Indoor Conditions

For NLOS receiver locations where the ray-tracer either fails to find a valid path or predicts an extremely weak signal, we fall back on the Close-In (CI) reference model [24], that computes pathloss at a distance d as:

$$
{ \mathrm { P a t h l o s s } } ( d ) = { \mathrm { F S P L } } ( d _ { 0 } ) + 1 0 n \log _ { 1 0 } \left( { \frac { d } { d _ { 0 } } } \right) + \chi _ { \sigma }\tag{1}
$$

Here, FSPL(d<sub>0</sub>) is the free-space pathloss at $d _ { 0 } = 1$ m:

$$
\mathrm { F S P L } ( d _ { 0 } ) = 2 0 \log _ { 1 0 } \left( { \frac { 4 \pi d _ { 0 } } { \lambda } } \right)\tag{2}
$$

with λ denoting the carrier wavelength. The NLOS pathloss exponent is set to $n = 3 . 0$ in accordance with the Haneda et al. [24] 3GPP-like CI model for urban macrocellular (UMa) NLOS environments with base station heights at or above 25 m. Additionally, a log-normal shadow fading term χ<sub>σ</sub> with standard deviation σ = 6.8 dB is included to capture small-scale signal variability due to unmodeled obstructions and environmental clutter. For each NLOS receiver, both raytraced and CI pathloss are computed, and the smaller of the two values is retained to ensure physically consistent pathloss levels in shadowed regions.

For indoor receivers, identified using building masks, an additional building entry loss (BEL) correction is applied in accordance with ITU-R P.2109 [25] to account for wall penetration effects and ensure alignment with empirical measurements. Finally, to enhance spatial consistency and suppress abrupt transitions, a 2D smoothing filter is applied to the pathloss maps. Each grid point is averaged with its four immediate neighbors under edge-aware handling, producing more coherent and physically plausible pathloss distributions over the $2 5 6 \times 3 8 4$ receiver grids.

![](images/cc73a01b2d6256198485b461668e661c10efe75bdfa3796d851519c6ee1869d6.jpg)

![](images/3a9c989b9fdca5d08d1b35e6c804d51e995e77bef887b35ed69d3006195dc225.jpg)

![](images/7c84ab70fa63f7ad107f423fc3bd5a164f47eb8fcbfe30c8fd3e68ed33bdef0e.jpg)

![](images/3d47c51798af998775191ef8450e72c6cde8ae7119045d9b023f18c745c01c45.jpg)

![](images/7bd16f03d8b4656874fc86b80b0c8da4069955eb15f21bd810813629f50ab28a.jpg)  
Fig. 1. Top-down views of the urban environments used for dataset generation: (a) Munich01 $( 4 8 ^ { \circ } 0 9 ^ { \prime } 1 3 . 2 ^ { \prime \prime } \mathrm { N } , 1 1 ^ { \circ } 3 4 ^ { \prime } 1 2 . 7 ^ { \prime \prime } \mathrm { E } )$ , (b) Munich02 $( 4 8 ^ { \circ } 0 9 ^ { \prime } 3 1 . 1 ^ { \prime \prime } \mathrm { N } .$ $1 1 ^ { \circ } 3 3 ^ { \prime } 5 2 . \dot { 5 } ^ { \prime \prime } \mathrm { E } ) .$ , (c) Helsinki $( 6 0 ^ { \circ } 1 0 ^ { \prime } 1 5 . 5 ^ { \prime \prime } \mathrm { N } , 2 4 ^ { \circ } 5 7 ^ { \prime } 3 5 . 4 ^ { \prime \prime } \mathrm { E } ) .$ , (d) Manhattan $( 4 0 ^ { \circ } 4 7 ^ { \prime } 4 1 . 0 ^ { \prime \prime } \mathrm { N } ,$ $7 3 ^ { \circ } 5 6 ^ { \prime } 3 3 . 0 ^ { \prime \prime } \mathrm { W } ) ,$ , and (e) London $( 5 1 ^ { \circ } 3 1 ^ { \prime } 0 2 . 4 ^ { \prime \prime } \mathrm { N } ,$ $0 ^ { \circ } 0 5 ^ { \prime } 1 9 . 5 ^ { \prime \prime } \mathrm { W } )$

TABLE II  
SIMULATION PARAMETERS USED FOR RAY-TRACING BASED DATASET GENERATION
<table><tr><td>Parameter</td><td>Value / Description</td></tr><tr><td>Carrier frequency</td><td>28 GHz</td></tr><tr><td>Transmit power</td><td>30 dBm</td></tr><tr><td>Antenna type</td><td>Isotropic</td></tr><tr><td>Antenna Gain</td><td>0 dBi</td></tr><tr><td>Building material</td><td>Concrete</td></tr><tr><td>Wall permittivity (€r)</td><td>5.31</td></tr><tr><td>Wall conductivity (σ)</td><td>0.626 S/m</td></tr><tr><td>Ground permittivity  $( \epsilon _ { g } )$ </td><td>3.00</td></tr><tr><td>Ground conductivity (σg)</td><td>0.0496 S/m</td></tr><tr><td>UAV altitude range</td><td>25 m, 35 m, 45 m</td></tr><tr><td>Receiver grid resolution</td><td>256 × 384 (total 98,304 receivers)</td></tr><tr><td>Receiver height</td><td>1.5m</td></tr><tr><td>Ray contributions</td><td>LOS, specular &amp; ground reflections</td></tr><tr><td>Scattering model</td><td>Directive scattering [23]</td></tr></table>

Table II summarizes the ray-tracing simulation parameters used in the dataset generation process.

## C. Input Feature Extraction

To enable effective spatial learning in our CNN-based architecture, we also compute three auxiliary input features, referred to as input channels, that exhibit strong correlation with the target variable, pathloss. Since CNNs expect inputs in spatial (image-like) formats, all feature vectors are reshaped into 2D grids matching the receiver layout for each transmitter scenario. Therefore, these features are computed for each transmitter scenario across 256 × 384 receiver grid, and later reshaped into smaller, fixed-size patches suitable for model training.

The three input channels are defined as follows:

• Log-distance map: The 20 log -transformed 3D Euclidean distance between the UAV transmitter and each receiver location.

• LOS mask: A binary map indicating whether a direct LOS path exists between the transmitter and the corresponding receiver. A value of 1 indicates LOS; 0 indicates obstruction. The LOS condition is determined solely by direct geometric visibility, whether the straight line between transmitter and receiver is obstructed. Future work could extend this model to include Fresnel zone clearance.

• Building occupancy mask: A binary map representing whether a receiver location lies inside a building (value of 1) or in free space (value of 0).

While the log-distance and building occupancy maps are readily computed from known environmental metadata and transmitter-receiver geometry, determining the LOS mask is significantly more complex, particularly in dense urban environments. To address this challenge, we implement an efficient, vectorized LOS estimation algorithm that uses geometric projection and tensor broadcasting to determine visibility across the entire grid. This approach enables rapid and scalable LOS computation, and is further explained in section IV.

TABLE III  
NUMBER OF FILTERS IN THE MULTI-SCALE FEATURE EXTRACTOR AT EACH ENCODER STAGE
<table><tr><td>Stage</td><td>F1 (1×1)</td><td>F2 (3×3)</td><td>F3 (5×5)</td><td>F4 (7×7)</td><td>F5 (1×1)</td></tr><tr><td>ENC-1</td><td>32</td><td>32</td><td>32</td><td>32</td><td>64</td></tr><tr><td>ENC-2</td><td>64</td><td>64</td><td>32</td><td>1</td><td>128</td></tr><tr><td>ENC-3</td><td>128</td><td>128</td><td>64</td><td>一</td><td>256</td></tr><tr><td>ENC-4</td><td>256</td><td>256*</td><td>64*</td><td>一</td><td>512</td></tr></table>

In ENC-4, the second convolutions for F2 (3×3) and F3 (5×5) employ a dilation rate of 2.

## III. MODEL ARCHITECTURE

We propose a fully convolutional encoder-decoder model based on the U-Net framework [26], tailored for spatial pathloss prediction in urban environments. Our model accepts a $1 2 8 \times 1 2 8 \times 3$ input tensor comprising logarithmic distance, LOS mask, and building mask, and produces a single-channel 128 × 128 output map representing normalized pathloss.

To overcome the limitations of standard U-Net in capturing complex propagation phenomena, we introduce two key enhancements: (1) a multi-scale convolutional encoder with feature fusion, and (2) a context-aware ASPP bottleneck. Together, these augmentations enable our model to effectively capture local and global spatial dependencies for accurate pathloss prediction.

## A. Multi-Scale Feature Extraction and Fusion

Each encoder stage in our model is designed as a multi-branch module that processes the input using parallel convolutional kernels of varying receptive fields as shown in Fig. 2. Specifically, every encoder block includes three branches with one 1 × 1, two 3 × 3, and two 5 × 5 convolution kernels, and the first encoder stage additionally includes a 7 × 7 kernel to capture broader context near the input layer. All convolutions are followed by Batch Normalization (BN) and ReLU activation.

The outputs from these branches are concatenated along the channel dimension and passed through a 1 × 1 convolutional layer to fuse and compress the features. This feature fusion step not only reduces the dimensionality of the concatenated output, it also produces a unified feature representation that integrates information from all convolutional scales. As the network progresses deeper into the encoder, the number of filters per branch increases to capture increasingly abstract and hierarchical representations as shown in Fig. 3. The number of filters in each encoder stage is summarized in Table III.

This multiscale design is motivated by the observation that pathloss in urban environments is influenced by structural features spanning a wide range of spatial resolutions, e.g., from fine-grained building edges to broader LOS corridors and open areas. By allowing multiple spatial receptive fields at each encoder stage, the network can learn to model small variations and large-scale propagation patterns simultaneously.

## B. ASPP Bottleneck for Context Aggregation

The deepest layer of the network features an ASPP module, which captures multi-receptive field context via parallel dilated convolutions with dilation rates of 1, 2, and 4. A global average pooling branch is also included to encode scene-wide context. The outputs from all branches are concatenated and passed through a final $1 \times 1$ fusion layer. This allows the model to incorporate both local detail and global scene structure, improving its robustness to diverse urban layouts.

![](images/1c0159ecd12943b3dca984dbe1dd8ee2439df6fbee15580946a7ce8bebae2493.jpg)

Fig. 2. Multi-branch feature extraction and fusion block in the encoder.  
![](images/ca3aa9bdc00874dc7c28dc16e8849230ed99dee1b05e97a5c66e761f6111c4cb.jpg)  
Fig. 3. Proposed U-Net architecture with encoder–decoder stages, MaxPooling, skip connections, and ASPP bottleneck (dimensions shown at each stage).

## C. Decoder and Output Prediction

The decoder path mirrors the encoder, using transposed convolutions to up-sample features and $3 \times 3$ convolutional blocks to refine predictions. Skip connections are used at each resolution level to preserve spatial detail by concatenating encoder features with corresponding decoder features. The final layer uses a 1×1 convolution to produce a single-channel output representing the predicted normalized pathloss.

Overall, our architecture is designed to efficiently capture multi-scale spatial dependencies and contextual relationships necessary for accurate pathloss prediction in dense urban environments.

## IV. VECTORIZED LOS ESTIMATION

Accurate mmWave pathloss prediction requires reliable LOS visibility modeling. In urban and semi-urban environments, buildings significantly obstruct propagation paths, making an explicit, geometry-aware LOS computation essential. We propose a fast vectorized algorithm that efficiently generates binary LOS masks over dense receiver grids.

## A. Problem Formulation

Let the transmitter be located at

$$
\mathbf { T } = ( x _ { t } , y _ { t } , z _ { t } ) \in \mathbb { R } ^ { 3 }
$$

and,

$$
\mathcal { R } = \{ ( \mathbf { x } _ { r } ^ { ( i ) } , \mathbf { y } _ { r } ^ { ( i ) } , \mathbf { z } _ { r } ^ { ( i ) } ) \} _ { i = 1 } ^ { N } ,
$$

denote a set of candidate receiver points in 3D space where $\mathbf { x } _ { r } , \mathbf { y } _ { r } , \mathbf { z } _ { r } \in \mathbb { R } ^ { N \times 1 }$ are vectors representing the coordinates of the receiver points.

The environment includes M vertical walls represented as line segments in the 2D plane with associated heights:

$$
\begin{array} { r } { { \mathscr W } = \left\{ (  { \mathbf { x } } _ { 1 } ^ { ( m ) } ,  { \mathbf { y } } _ { 1 } ^ { ( m ) } ,  { \mathbf { x } } _ { 2 } ^ { ( m ) } ,  { \mathbf { y } } _ { 2 } ^ { ( m ) } , h ^ { ( m ) } ) \right\} _ { m = 1 } ^ { M } , } \end{array}
$$

where $\mathbf { x } _ { 1 } , \mathbf { y } _ { 1 } , \mathbf { x } _ { 2 } , \mathbf { y } _ { 2 } \ \in \ \mathbb { R } ^ { M \times 1 }$ are vectors representing the coordinates of the endpoints of each wall’s bottom edge, and h $\mathbf { \Psi } \in \mathbb { R } ^ { M \times 1 }$ is the vector of corresponding wall heights.

![](images/57d42965245030d6a3cccd57436e6512c61f79329e13d844dd4256b0f5debfa9.jpg)  
(a) Ground Truth MLP (RMSE = 3.57 dB)

![](images/e000b596635bda83573088951b15fd64c400af5b12c703e535252bbdd40e71cd.jpg)  
(b) Our Model

![](images/656bf9a6658762054a6ca53534e5658ef07590f9cd6e1cf3fe4bb765a05f81ab.jpg)

![](images/e24029c24036eeedda8542341c1341a5c14cf794e92ce9c29bc036362ba70c61.jpg)  
(d) RadioUNet (3-CH)

(e) MLP  
![](images/5631209dff654300ba6582546d7a732e8651bcbb4b9a0e0c5395d4b2163fbf60.jpg)

![](images/06d2854888d9923a713352c1ef8541ed16153e306fbdc43de0158da6bf68b02a.jpg)  
(f) XGBoost

(c) RadioUNet (2-CH)  
![](images/297436fd608f5f2723c011413b2114ac99c518989b4277cbbe2fe963d5819215.jpg)  
(g) Linear Regression

![](images/b0d33a23120f9226b85b6be49d6fab3ef85d81040c23626936c7680cf4d983dd.jpg)  
(h) 3GPP  
Fig. 4. Predicted pathloss maps for a test environment in Munich-02. (a) Ground truth pathloss, (b) Proposed model, (c) RadioUNet (2-CH), (d) RadioUNet (3-CH), (e) MLP, (f) XGBoost, (g) Linear regression, and (h) 3GPP model.

Our goal is to determine a binary LOS mask vector ${ \mathcal { L } } \in$ $\{ 0 , 1 \} ^ { \bar { N } \times 1 }$ , that determines, for each receiver $r ^ { n }$ , whether the direct line from transmitter to $r ^ { n }$ $\overline { { \mathbf { T r } ^ { n } } }$ , intersects any wall segment $\mathbf { w } ^ { m }$

$$
\mathcal { L } ^ { ( n ) } = \left. \begin{array} { l l } { 1 , } & { \mathrm { i f } \left. \overline { { \mathbf { T r } ^ { n } } } \cap \mathbf { w } ^ { m } = \emptyset , \forall m \in \left. 1 , . . . , M \right. \right. , } \\ { 0 , } & { \mathrm { o t h e r w i s e . } } \end{array} \right.
$$

## B. Algorithm Overview

The algorithm constructs a boolean intra-visibility matrix $\mathcal { V } \in \bar { \{ 0 , 1 \} } ^ { N \times M }$ , where $\gamma _ { n , m } ~ = ~ 1$ if the line segment from the transmitter to receiver $\mathbf { r } ^ { n } , \ \overline { { \mathbf { T r } ^ { n } } }$ , intersects wall $\mathbf { w } ^ { m }$ , and $\nu _ { n , m } = 0$ otherwise. The matrix V is initialized with zeros, corresponding to the assumption that all receivers have unobstructed LOS to the transmitter. To enable efficient computation of LOS visibility over large receiver grids, the following steps are applied:

• Wall Filtering: Only walls that are directly facing the transmitter and visible to it can obstruct the direct LOS between the transmitter and the receiver grid. Given that wall coordinates are stored in vector form, we employ vectorized operations to compute the outward normal vectors of all walls. Similarly, the midpoints of the bottom edges of the walls are computed in vector form as $\mathcal { P } = \bar { \{ \bf p } _ { x } , \bf p _ { y } \} \in \mathbb { R } ^ { M \times 1 }$ , which serve as reference points for visibility testing. A geometric visibility test is then performed by evaluating the vectorized dot product between each wall’s outward normal vector and the vector from its reference point $\mathcal { P }$ to the transmitter location. Walls with a positive dot product are classified as directly facing the transmitter and are retained as potential occluders in subsequent LOS computations.

• 3D Intersection Check: For each transmitter–receiver pair $( \mathbf { T } , \mathbf { r } ^ { n } )$ , and for each wall $\mathbf { w } ^ { m }$ in the subset of walls identified as directly visible to the transmitter, the 3D intersection point between the line segment $\overline { { \mathbf { T r } ^ { n } } }$ and the 2D rectangular wall segment $\mathbf { w } ^ { m }$ is computed.

The intersection is validated through (i) a planar geometric test to confirm that the intersection lies within the 2D wall footprint, and (ii) a height constraint ensuring that the intersection lies within the wall’s vertical extent. For all receivers where a valid intersection with wall $\mathbf { w } ^ { m }$ is detected, the corresponding entry $\nu _ { n , m }$ in the intravisibility matrix is set to 1.

• LOS Mask Computation: A receiver $\mathbf { r } ^ { n }$ with no intersections on all facing walls will have $\nu _ { n , m } = 0$ for all $m \in \{ 1 , . . . , M \}$ indicating that no wall obstructs the receiver and hence will be in LOS. Thus, the binary LOS label ${ \mathcal { L } } ^ { n }$ is obtained by summing over the n-th row of V:

$$
\mathcal { L } ^ { n } = \left\{ \begin{array} { l l } { 1 , } & { \mathrm { i f } \sum _ { m = 1 } ^ { M } \mathcal { V } _ { n , m } = 0 , } \\ { 0 , } & { \mathrm { o t h e r w i s e } . } \end{array} \right.
$$

All computations are implemented using the Python NumPy library with full vectorization. The algorithm exhibits good scalability to tens of thousands of receiver points, as intersection tests are restricted to the subset of walls that directly face the transmitter, thereby avoiding unnecessary computations. Table I lists the average LOS computation times per scenario (98,304 receivers per site) for each of the five urban environments.

```latex
Algorithm 1 Vectorized LOS Estimation
Input: Transmitter location $\overline { { \mathbf { T } \in \mathbb { R } ^ { 3 } } }$ , receivers
$\mathcal { R } = \{ ( \mathbf { x } _ { r } ^ { ( i ) } , \mathbf { y } _ { r } ^ { ( i ) } , \mathbf { z } _ { r } ^ { ( i ) } ) \} _ { i = 1 } ^ { N }$ , wall segments
$\begin{array} { r } { \mathbf { \mathcal { W } } = \left\{ ( \mathbf { x } _ { 1 } ^ { ( m ) } , \mathbf { y } _ { 1 } ^ { ( m ) } , \mathbf { x } _ { 2 } ^ { ( m ) } , \mathbf { y } _ { 2 } ^ { ( m ) } , h ^ { ( m ) } ) \right\} _ { m = 1 } ^ { M } , } \end{array}$
Output: LOS mask $\mathcal { L } \in \{ 0 , 1 \} ^ { N }$
Compute outward normal vectors $\mathbf { n } ^ { m }$ for all walls
(vectorized);
Compute transmitter-to-wall midpoints vectors
$\mathbf { v } ^ { m } = \mathbf { T } - \mathcal { P } ^ { m } ;$
Determine facing walls:
$\mathbf { f }   \mathbf { n } ^ { m } , \mathbf { v } ^ { m }  > 0 \forall m \in \{ 1 , \dots , M \}$
$/ /$ Vectorized dot product
Initialize intra-visibility matrix: $\gamma \gets \mathbf { 0 } ^ { N \times M }$
foreach wall m with $\mathbf { f } _ { m } = 1$ do
Compute 3D intersections between all rays $\overrightarrow { \mathbf { T r } ^ { n } }$
and wall $\mathbf { w } ^ { m }$ (vectorized over n);
Apply height constraint $0 \leq z \leq h _ { m } ;$
Set $\nu _ { n , m } \gets 1$ for valid intersections;
foreach receiver n do
$\begin{array} { r } { \mathcal { L } _ { n } \gets \mathbb { I } \left[ \sum _ { m = 1 } ^ { M } \mathcal { V } _ { n , m } = 0 \right] ; } \end{array}$
return L
```

## V. TRAINING AND EVALUATION SETUP

## A. In-House Dataset Preparation and Input Generation

We prepare our training and evaluation dataset using highresolution simulation files, where each file corresponds to a unique transmitter scenario over a $2 5 6 \times 3 8 4$ receiver grid. For every receiver point, three spatial features are available: (1) logarithmic distance, (2) LOS mask, and (3) building occupancy mask. These form the three input channels for our model, while the target is the pathloss value at each receiver location.

The input tensor to the model is of shape $1 2 8 \times 1 2 8 \times 3 ,$ where the three channels represent the aforementioned features. The log-distance channel is normalized using global min-max scaling across the training set, while the LOS and building masks are binary and inherently normalized. The corresponding output tensor contains normalized pathloss values and has shape $1 2 8 \times 1 2 8 \times 1$ . These input-output pairs are provided to the model via a custom dataset class.

To construct each training and test sample, we extract patches of size $1 2 8 \times 1 2 8$ from the full $2 5 6 \times 3 8 4$ grid. The patching process involves two steps:

• Structured Patch Extraction: From each $2 5 6 \times 3 8 4$ grid, a total of 18 unique $1 2 8 \times 1 2 8$ patches are systematically generated to ensure diverse yet structured spatial coverage. First, the grid is fully tiled into a nonoverlapping $2 \times 3$ layout, producing six patches. Next, horizontal downsampling is applied by sampling every second pixel along the horizontal axis (horizontal stride $= 2 )$ , and segmenting vertically without overlap, yielding three patches. Vertical downsampling is then performed twice: once with sampling starting from the top row (vertical stride = 2) and once from a vertically offset row (vertical stride = 2), each producing two patches in a $2 \times 1$ layout. A bidirectional downsampling strategy combines horizontal stride of 2 sampling with each of the two vertical alignments (starting from the top row and the offset row), generating two more patches. Additionally, vertical 1/3-rate sampling combined with segmenting horizontally without overlap, is applied to form two $2 \times 1$ patches, and finally, one mixed-sampling patch is obtained by combining horizontal stride-2 and vertical stride-3 sampling. This exhaustive pairing yields multiple combinations that capture various spatial overlaps and receptive field densities, thereby offering the model multiple effective zoom levels across the environment. These combinations effectively capture finer and coarser spatial patterns.

Random Patch Sampling: We randomly extract 82 more patches using varying strides and random starting positions, ensuring no duplicate coverage. These patches introduce further spatial diversity by capturing random building configurations and propagation scenarios.

In total, 100 unique patches are generated per transmitter scenario. To augment the dataset, we apply horizontal and vertical flips to each patch, resulting in 300 total samples per scenario.

The complete dataset comprises five different urban environments, each simulated with four transmitter locations at three UAV altitudes. For training, we use data from three transmitters (all three altitudes) per environment, resulting in 45 distinct scenarios. The remaining one transmitter per environment (all three altitudes) is used for testing, totaling 15 test scenarios. With 300 samples per scenario, this yields 13,500 training and 4,500 test samples of dimensions $1 2 8 \times 1 2 8 .$

## B. RadioMapSeer Dataset Preparation

We also evaluate our model using the publicly available RadioMapSeer dataset [14], which provides over 56,000 raytraced pathloss maps for D2D communication at 5.9 GHz across diverse urban environments. Each map is of size 256×256 and includes detailed spatial information on pathloss and building occupancy.

Our model requires an LOS mask as an input channel. Since generating these masks for the entire RadioMapSeer dataset is computationally infeasible, we use the IRT-4 subset in the RadioMapSeer dataset, which includes ray-traced simulations with up to four ray interactions. This subset includes 1,400 maps from 700 unique urban environments, each with two transmitter locations, offering realistic multipath propagation characteristics.

To match our model’s input resolution of $1 2 8 \times 1 2 8 ,$ each 256 × 256 map is divided into four non-overlapping quadrants (top-left, top-right, bottom-left, bottom-right), producing four

$1 2 8 \times 1 2 8$ samples. For training, we select 500 environments (1,000 original maps), which yield 4,000 processed samples after segmentation. The test set consists of 200 held-out environments (400 maps), providing 1,600 test samples.

Input features for our model are prepared as follows: (i) the logarithmic distance channel is computed using the known 1 m pixel spacing; (ii) building occupancy masks are directly extracted from the dataset; and (iii) LOS masks are generated using our proposed vectorized LOS computation algorithm based on the transmitter positions in each map.

## C. Model Training and Evaluation

To train the proposed U-Net architecture, we employ a custom training pipeline designed to handle both training and validation phases concurrently. The model is trained for 40 epochs using the Adam optimizer with a learning rate of $1 \times 1 0 ^ { - 4 }$ , batch size of 16 and random seed of 42. Early stopping is applied with a patience of 10 epochs.

The primary loss function used for training is RMSE, defined as:

$$
\mathrm { R M S E } = \sqrt { \frac { 1 } { N } \sum _ { i = 1 } ^ { N } ( y _ { i } - \hat { y } _ { i } ) ^ { 2 } } ,\tag{3}
$$

where $y _ { i }$ and $\hat { y } _ { i }$ represent the ground truth and predicted pathloss values, respectively, and N is the total number of samples.

To facilitate stable training and faster convergence, the normalized pathloss values are used for loss computation and back propagation. However, for a meaningful evaluation, the predicted and ground-truth values are rescaled (denormalized) back to their original range in dB before calculating performance metrics.

In addition to RMSE, we monitor two additional metrics: the mean absolute error (MAE) and the Normalized Mean Squared Error (NMSE), computed as:

$$
\mathrm { M A E } = \frac { 1 } { N } \sum _ { i = 1 } ^ { N } \left| y _ { i } - \hat { y } _ { i } \right| ,\tag{4}
$$

$$
\mathrm { N M S E } = \frac { \sum _ { i = 1 } ^ { N } ( y _ { i } - \hat { y } _ { i } ) ^ { 2 } } { \sum _ { i = 1 } ^ { N } y _ { i } ^ { 2 } } .\tag{5}
$$

## VI. RESULTS AND DISCUSSION

## A. Ablation Study on Multi-Scale Feature Extraction and Context Aggregation

To rigorously quantify the necessity and sufficiency of each architectural component in the proposed network, a detailed ablation study was conducted. The proposed model consists of three key modules: (i) parallel multi-scale convolutional branches for capturing propagation characteristics at different spatial resolutions, (ii) a feature fusion block implemented via a 1 × 1 convolution for adaptive channel-wise integration, and (iii) an ASPP module for large-scale contextual aggregation.

Seven ablation configurations were evaluated by selectively removing one or more modules. All configurations are trained and evaluated using identical datasets, training schedules, and evaluation protocols.

TABLE IV  
ABLATION STUDY RESULTS FOR THE PROPOSED NETWORK
<table><tr><td>Configuration</td><td>RMSE (dB)</td><td>MAE (dB)</td><td>NMSE</td></tr><tr><td>Configuration-1</td><td>3.31</td><td>2.53</td><td>0.00397</td></tr><tr><td>Configuration-2</td><td>3.27</td><td>2.46</td><td>0.00382</td></tr><tr><td>Configuration-3</td><td>3.58</td><td>2.69</td><td>0.00460</td></tr><tr><td>Configuration-4</td><td>3.30</td><td>2.49</td><td>0.00390</td></tr><tr><td>Configuration-5</td><td>3.29</td><td>2.47</td><td>0.00380</td></tr><tr><td>Configuration-6</td><td>3.30</td><td>2.52</td><td>0.00390</td></tr><tr><td>Configuration-7</td><td>3.34</td><td>2.54</td><td>0.00390</td></tr><tr><td>Complete Model</td><td>3.15</td><td>2.37</td><td>0.00049</td></tr></table>

The evaluated configurations are summarized as follows:

• Configuration–1: Multi-scale branches removed; feature fusion block and ASPP retained

• Configuration–2: feature fusion block removed; multiscale branches and ASPP retained

• Configuration–3: ASPP removed; multi-scale branches and feature fusion block retained

• Configuration–4: Multi-scale branches and feature fusion removed; ASPP retained

• Configuration–5: feature fusion block and ASPP removed; multi-scale branches retained

• Configuration–6: ASPP and multi-scale branches removed; feature fusion block retained

• Configuration–7: All three modules removed, yielding a vanilla U-Net baseline

The quantitative results of the ablation study are reported in Table IV in terms of RMSE, MAE, and NMSE. The performance of the complete model is also shown and discussed further in the next section.

The results clearly demonstrate that each architectural component contributes positively to overall prediction accuracy, while their combined use yields the best performance. In particular, removing the ASPP module (Configuration–3) leads to the largest degradation across all evaluation metrics, highlighting the critical role of large-scale contextual aggregation in modeling the propagation effects in UAV-assisted mmWave environments. The multi-scale convolutional branches consistently improve performance, while the feature fusion block further enhances stability and accuracy by adaptively integrating information across scales. These findings confirm that the proposed integration of multi-scale feature extraction, feature fusion, and ASPP-based context aggregation is sufficient and provides a clear architectural advantage.

## B. Benchmarking and Comparative Evaluation

To rigorously evaluate the performance of the proposed model,we benchmark it against a comprehensive suite of baseline approaches, including classical ML models, empirical pathloss models, and deep learning-based architectures. The evaluation is conducted on two datasets: (i) our inhouse ray-tracing-based dataset and (ii) the publicly available RadioMapSeer dataset. The benchmarked approaches include:

1) Classical ML Models: To establish strong performance baselines, we evaluate several classical ML models as summarized below:

TABLE V  
TRAINING PARAMETERS FOR CLASSICAL ML MODELS
<table><tr><td>Model</td><td>Configuration Details</td></tr><tr><td>XGBoost</td><td>Objective: reg:squarederror; Tree method: hist; Device: cuda; Max depth: 10; Learning rate: 0.1; Estimators: 100</td></tr><tr><td>MLP</td><td>Layers: [256, 128, 64, 32, 16, 8, 4, 2]; Activation: ReLU; Optimizer: Adam; Loss: MSE; Epochs: 40; Early stopping: Patience = 5 (validation loss)</td></tr></table>

• Linear Regression (LR): LR is a simple yet effective statistical model that assumes a linear relationship between input features and the output variable.

• Extreme Gradient Boosting (XGBoost): XGBoost is a high-performance ensemble learning technique based on gradient-boosted decision trees, and is known for its robustness, speed, and strong prediction capabilities on structured tabular datasets.

• MLP: A fully connected MLP comprising eight hidden layers of decreasing size is used. The MLP captures complex, non-linear relationships among features and serves as a strong deep learning baseline.

Table V summarizes the training parameters used for the XGBoost and MLP models.

2) Empirical Pathloss Models: To assess the performance of the proposed model against empirical baselines, we evaluate two empirical pathloss models.

• 3GPP Empirical Model: [27], [28] This model employs distinct distance-dependent formulations for LOS and NLOS propagation, as defined in 3GPP Technical Reports TR 38.900 and TR 38.901. For the in-house dataset (28 GHz), TR 38.900 is applied, while the RadioMapSeer dataset (5.9 GHz) utilizes TR 38.901.

$$
\begin{array} { r l } & { P L _ { \mathrm { L O S } } = \left\{ \begin{array} { l l } { P L _ { \mathrm { 1 } } , } & { 1 0 \mathrm { m } \leq d _ { \mathrm { 2 D } } \leq d _ { \mathrm { B P } } ^ { \prime } } \\ { P L _ { \mathrm { 2 } } , } & { d _ { \mathrm { B P } } ^ { \prime } < d _ { \mathrm { 2 D } } \leq 5 \mathrm { k m } } \end{array} \right. ( } \\ & { \qquad P L _ { \mathrm { 1 } } = 3 2 . 4 + 2 1 \log _ { 1 0 } ( d _ { \mathrm { 3 D } } ) + 2 0 \log _ { 1 0 } ( f _ { c } ) , } \\ & { P L _ { \mathrm { 2 } } = 3 2 . 4 + 4 0 \log _ { 1 0 } ( d _ { \mathrm { 3 D } } ) + 2 0 \log _ { 1 0 } ( f _ { c } ) } \\ & { \qquad - 9 . 5 \log _ { 1 0 } \left( ( d _ { \mathrm { B P } } ^ { \prime } ) ^ { 2 } + ( h _ { \mathrm { T X } } - h _ { \mathrm { R X } } ) ^ { 2 } \right) , } \\ & { P L _ { \mathrm { N L O S } } = \operatorname* { m a x } \left( P L _ { \mathrm { L O S } } , P L _ { \mathrm { N L O S } } ^ { \prime } \right) \qquad ( } \end{array}\tag{6}
$$

(7)

For the in-house dataset (28 GHz), the NLOS component is modeled as:

$$
\begin{array} { r l } { { P } { L } _ { \mathrm { N L O S } } ^ { \prime } = 1 3 . 5 4 + 3 9 . 0 8 \log _ { 1 0 } ( d _ { \mathrm { 3 D } } ) + 2 0 \log _ { 1 0 } ( f _ { c } ) } \\ { ~ - 0 . 6 ( h _ { \mathrm { R X } } - 1 . 5 ) , } \end{array}
$$

For the RadioMapSeer dataset (5.9 GHz), the following NLOS model is applied:

$$
\begin{array} { r l } & { P L _ { \mathrm { N L O S } } ^ { \prime } = 2 2 . 4 + 3 5 . 3 \log _ { 1 0 } ( d _ { \mathrm { 3 D } } ) + 2 1 . 3 \log _ { 1 0 } ( f _ { c } ) } \\ & { \qquad - 0 . 3 ( h _ { \mathrm { R X } } - 1 . 5 ) , } \end{array}
$$

Here, $d _ { \mathrm { 2 D } }$ and $d _ { \mathrm { 3 D } }$ denote the 2D horizontal and 3D Euclidean distances (in meters), respectively; $f _ { c }$ is the carrier frequency in GHz; $h _ { \mathrm { T X } }$ and $h _ { \mathrm { R X } }$ represent the

TABLE VI  
ABG PARAMETERS FOR ITU-R 1411-12 MODEL [29]
<table><tr><td>Dataset</td><td>Condition</td><td>α</td><td>β</td><td>γ</td></tr><tr><td>In-house (28 GHz)</td><td>LOS NLOS</td><td>2.29 4.39</td><td>28.6 -6.27</td><td>1.96 2.3</td></tr><tr><td rowspan="2">RadioMapSeer (5.9 GHz)</td><td></td><td></td><td></td><td></td></tr><tr><td>LOS NLOS</td><td>2.12 5.06</td><td>29.2 -4.68</td><td>2.11 2.02</td></tr></table>

heights of the transmitter and receiver in meters. The breakpoint distance $d _ { \mathrm { B P } } ^ { \prime }$ is given by:

$$
d _ { \mathrm { B P } } ^ { \prime } = \frac { 4 h _ { \mathrm { U A V } } ^ { \prime } h _ { \mathrm { R X } } ^ { \prime } f _ { c } } { c } ,
$$

where c is the speed of light. The effective antenna heights are computed as $h _ { \mathrm { U A V } } ^ { \prime } ~ = ~ h _ { \mathrm { U A V } } - h _ { E }$ and $h _ { \mathrm { R X } } ^ { \prime } \ = \ h _ { \mathrm { R X } } - h _ { E }$ , with $h _ { E } ~ = ~ 1$ m representing the environment-specific height adjustment for urban microcellular scenarios.

• ITU-R 1411-12 Empirical Model: [29] This model employs the Alpha-Beta-Gamma (ABG) formulation to estimate pathloss based on 3D distance and carrier frequency, with distinct parameters for LOS and NLOS conditions. The general form is:

$$
\begin{array} { r } { P L _ { \mathrm { A B G } } = 1 0 \alpha \log _ { 1 0 } ( d _ { 3 \mathrm { D } } ) + \beta + 1 0 \gamma \log _ { 1 0 } ( f _ { c } ) , } \end{array}\tag{8}
$$

where $d _ { \mathrm { 3 D } }$ is the transmitter-receiver 3D distance (in meters), $f _ { c }$ is the carrier frequency (in GHz), and $\alpha , \beta , \gamma$ are model parameters tuned to the propagation environment. Parameter values used for both datasets are listed in Table VI.

## 3) State-of-the-Art Deep Learning Baseline:

• RadioUNet (2-Channel and 3-Channel Variants): RadioUNet [14] is a fully convolutional U-Net-based architecture widely recognized as a deep learning baseline for pathloss prediction. Due to its open-source availability, it serves as a common benchmark in recent literature. We evaluate both standard input variants of RadioUNet. The 2-channel configuration uses: (i) a transmitter location mask, where the transmitter position is marked with a value of 1 while all other pixels are set to 0; and (ii) a building occupancy mask, which encodes static obstacles in the environment. The 3-channel configuration extends this input with a third channel that includes sparse pathloss measurements. To ensure a fair and consistent comparison with the proposed model, the inhouse ray-tracing dataset is adapted to match the exact input-channel requirements of each RadioUNet variant. Specifically, the transmitter location mask is generated directly from the in-house dataset geometry. For the threechannel RadioUNet variant, the sparse measurement input is constructed using normalized ground-truth pathloss values at 300 randomly selected spatial locations, while all remaining pixels in this channel are set to zero, consistent with the original RadioUNet implementation. The original RadioUNet architecture is designed for input maps of size 256 × 256. Since our in-house dataset operates at a native resolution of 128×128, all input channels are upsampled to the required $2 5 6 \times 2 5 6$ resolution using bilinear interpolation before being fed into the RadioUNet model.

TABLE VII  
COMPARISON OF PATHLOSS PREDICTION PERFORMANCE ON IN-HOUSE AND RADIOMAPSEER DATASETS
<table><tr><td rowspan="3">Model</td><td colspan="6">In-house Dataset</td><td colspan="8"></td></tr><tr><td colspan="3">Error Metrics</td><td colspan="4">Absolute Error Percentiles (dB)</td><td colspan="3">Error Metrics</td><td colspan="4">Absolute Error Percentiles (dB)</td></tr><tr><td>RMSE</td><td>MAE</td><td>NMSE</td><td>50%</td><td>75%</td><td>90%</td><td>99%</td><td>RMSE</td><td>MAE</td><td>NMSE</td><td>50%</td><td>75%</td><td>90%</td><td>99%</td></tr><tr><td>Linear Regression</td><td>3.93</td><td>2.97</td><td>0.0008</td><td>2.32</td><td>4.17</td><td>7.76</td><td>11.42</td><td>8.27</td><td>5.35</td><td>0.0047</td><td>3.26</td><td>7.53</td><td>16.08</td><td>29.95</td></tr><tr><td>XGBoost Regressor</td><td>3.83</td><td>2.90</td><td>0.0007</td><td>2.14</td><td>4.03</td><td>7.62</td><td>11.07</td><td>7.82</td><td>4.51</td><td>0.0042</td><td>1.45</td><td>6.48</td><td>15.61</td><td>31.20</td></tr><tr><td>MLP (8 Dense Layers)</td><td>3.86</td><td>2.94</td><td>0.0007</td><td>2.18</td><td>4.07</td><td>7.66</td><td>11.22</td><td>9.93</td><td>7.30</td><td>0.0068</td><td></td><td></td><td></td><td></td></tr><tr><td>3GPP Model</td><td>12.22</td><td>9.53</td><td>0.0073</td><td>7.36</td><td>15.64</td><td>23.24</td><td>28.45</td><td>20.67</td><td>14.07</td><td>0.0293</td><td>6.33</td><td>26.78</td><td>43.83</td><td>55.48</td></tr><tr><td>ITU-R Model</td><td>14.40</td><td>10.82</td><td>0.0101</td><td>7.23</td><td>18.63</td><td>27.97</td><td>34.34</td><td>15.82</td><td>12.02</td><td>0.0172</td><td>9.92</td><td>17.71</td><td>30.54</td><td>47.35</td></tr><tr><td>RadioUNet (2-Ch)</td><td>7.92</td><td>5.87</td><td>0.0036</td><td>4.20</td><td>7.52</td><td>18.30</td><td>30.42</td><td>4.98</td><td>2.74</td><td>0.0017</td><td>1.17</td><td>3.69</td><td>10.80</td><td>20.61</td></tr><tr><td>RadioUNet (3-Ch)</td><td>4.59</td><td>3.26</td><td>0.0011</td><td>2.42</td><td>4.35</td><td>8.68</td><td>18.88</td><td>4.23</td><td>2.05</td><td>0.0012</td><td>0.84</td><td>2.34</td><td>8.27</td><td>19.78</td></tr><tr><td>Proposed Model (Ours)</td><td>3.15</td><td>2.37</td><td>0.00049</td><td>1.86</td><td>3.48</td><td>6.26</td><td>8.60</td><td>3.97</td><td>2.03</td><td>0.0011</td><td>0.52</td><td>2.63</td><td>8.57</td><td>15.90</td></tr></table>

To ensure a fair and consistent evaluation, all classical ML models are trained and tested using the same train/test split and input features as the proposed model. The key distinction lies in the input representation: while the proposed model utilizes spatially structured 2D input maps, the classical models operate on flattened vectorized inputs. The 3GPP and ITU-R empirical models do not require training. These empirical models are directly applied to the same test data for a consistent performance comparison with the proposed model. Similarly, the RadioUNet baseline is trained on the same data split, although it uses different input channel configurations, as previously discussed. Table VII reports the standard error metrics (RMSE, MAE, and NMSE) along with the absolute error percentiles (50th, 75th, 90th, and 99th) for all compared models on the in-house and RadioMapSeer datasets. The proposed model consistently achieves lower errors across both datasets, indicating its superior prediction accuracy under diverse propagation scenarios.

On the in-house dataset, classical ML models demonstrate competitive performance, with XGBoost achieving the best results among them (RMSE: 3.83 dB, MAE: 2.90 dB, NMSE: 0.0007). In contrast, the 3GPP and ITU-R empirical models yield significantly higher errors (e.g., ITU-R RMSE: 14.4 dB), highlighting their limited adaptability to complex and obstructed urban geometries. The RadioUNet model shows improved performance when using the 3-channel configuration (RMSE: 4.59 dB) compared to the 2-channel variant (RMSE: 7.92 dB), due to the inclusion of sparse pathloss measurements that provide additional spatial supervision. However, both configurations underperform compared to classical ML models on this dataset, which may be attributed to the original RadioUNet design being tailored for a different frequency regime and dataset (5.9 GHz RadioMapSeer). The proposed model achieves the best performance across all metrics on the in-house dataset, with an RMSE of 3.15 dB, MAE of 2.37 dB, and NMSE of 0.00049, demonstrating its ability to learn both large-scale and fine-grained spatial propagation characteristics from 2D representations due to the multiscale feature extraction architecture. To further assess the performance stability of the proposed model across multiple training runs, four independent training experiments were conducted on the in-house dataset. For each of the five environments, the model was trained on data from three transmitter locations and evaluated on the remaining fourth unseen transmitter location. Averaged over all four runs, the model achieves an RMSE of $3 . 2 6 \pm 0 . 0 9 \mathrm { d B } ,$ an MAE of $2 . 4 6 \pm 0 . 0 7 \mathrm { d B }$ , and an NMSE of $( 5 . 1 \pm 0 . 2 2 ) \times 1 0 ^ { - 4 }$ , indicating consistent performance across multiple training runs.

On the RadioMapSeer dataset, the overall trends shift. The empirical models remain the least accurate, with 3GPP RMSE at 20.67 dB and ITU-R at 15.82 dB. Classical ML models, such as XGBoost (RMSE: 7.82 dB) and Linear Regression (RMSE: 8.27 dB), show higher errors compared to their performance on the in-house dataset. As expected, RadioUNet performs notably better on the RadioMapSeer dataset, with its 3-channel variant achieving RMSE: 4.23 dB, closer to the proposed model’s performance. This is consistent with the fact that RadioUNet was originally validated on this dataset. Nevertheless, the proposed model achieves the lowest RMSE (3.97 dB), MAE (2.03 dB), and NMSE (0.0011) on the RadioMapSeer dataset, consistently outperforming all baselines.

## C. Generalization Performance Across Urban Environments

To assess the generalization capability of the proposed model across varying urban morphologies, we employ a crosscity validation strategy using our in-house dataset. In each experimental run, the model is trained using data from four cities and evaluated on the fifth, previously unseen city. The training set includes all transmitter locations and UAV altitudes from the source environments, while evaluation is performed on all transmitter locations and altitudes in the held-out target environment. Table VIII reports the generalization results.

The results show that the model achieves consistently low errors across all target cities, with only a marginal increase relative to the baseline. This demonstrates the model’s strong generalization capacity and robustness to unseen spatial configurations and urban topologies.

## D. Generalization Performance Across UAV Altitudes

To assess the robustness of our proposed model across varying UAV altitudes, we conduct a detailed evaluation by isolating performance at each of the three UAV transmitter altitudes: 25 m, 35 m, and 45 m. For this purpose, we train three separate instances of our model for each altitude using the same urban environment split as in the baseline evaluation of section VI-B. Specifically, training is performed on data from three transmitter locations of each urban environment, and testing is carried out on the remaining unseen transmitter location, keeping the UAV altitude fixed within each experiment. This process is repeated across all three altitudes. For comparison, we also train and evaluate altitude-specific versions of the RadioUNet model using both two-channel (2-CH) and three-channel (3-CH) input configurations. The comparative performance is summarized in Table IX.

TABLE VIII  
GENERALIZATION PERFORMANCE ACROSS URBAN ENVIRONMENTS (IN-HOUSE DATASET)
<table><tr><td rowspan="2">Test Environment (Held-Out City)</td><td colspan="3">Error Metrics</td><td colspan="4">Absolute Error Percentiles (dB)</td></tr><tr><td>RMSE (dB)↓</td><td>MAE (dB)↓</td><td>NMSE↓</td><td>50%</td><td>75%</td><td>90%</td><td>99%</td></tr><tr><td>Munich-01</td><td>3.24</td><td>2.31</td><td>0.00056</td><td>1.70</td><td>3.39</td><td>6.32</td><td>9.26</td></tr><tr><td>Munich-02</td><td>3.53</td><td>2.56</td><td>0.00067</td><td>2.0</td><td>3.64</td><td>6.60</td><td>10.13</td></tr><tr><td>Helsinki</td><td>3.29</td><td>2.59</td><td>0.00047</td><td>2.12</td><td>3.73</td><td>6.50</td><td>8.71</td></tr><tr><td>London</td><td>3.32</td><td>2.59</td><td>0.00047</td><td>2.15</td><td>3.73</td><td>6.48</td><td>8.74</td></tr><tr><td>Manhattan</td><td>3.16</td><td>2.48</td><td>0.00047</td><td>2.02</td><td>3.60</td><td>6.29</td><td>8.39</td></tr><tr><td>Baseline (Standard Train/Test Split)</td><td>3.15</td><td>2.37</td><td>0.00049</td><td>1.86</td><td>3.48</td><td>6.26</td><td>8.60</td></tr></table>

TABLE IX

PERFORMANCE COMPARISON ON IN-HOUSE UAV MMWAVE DATASET AT DIFFERENT TRANSMITTER ALTITUDES
<table><tr><td rowspan="2">Model</td><td colspan="3"> $\mathbf { a l t i t u d e } = 2 5 \mathbf { m }$ </td><td colspan="3"> $\mathbf { a l t i t u d e } = 3 5 \mathbf { m }$ </td><td colspan="3">altitude = 45 m</td></tr><tr><td>RMSE↓</td><td>MAE↓</td><td>NMSE↓</td><td>RMSE↓</td><td>MAE↓</td><td>NMSE↓</td><td>RMSE↓</td><td>MAE↓</td><td>NMSE↓</td></tr><tr><td>RadioUNet (2-CH)</td><td>7.84</td><td>5.85</td><td>0.0034</td><td>7.31</td><td>5.39</td><td>0.0029</td><td>7.99</td><td>5.92</td><td>0.0035</td></tr><tr><td>RadioUNet (3-CH)</td><td>5.36</td><td>3.86</td><td>0.0015</td><td>4.67</td><td>3.37</td><td>0.0011</td><td>5.46</td><td>3.68</td><td>0.0016</td></tr><tr><td>Proposed Model</td><td>3.17</td><td>2.43</td><td>0.00049</td><td>3.20</td><td>2.43</td><td>0.00050</td><td>3.28</td><td>2.45</td><td>0.00053</td></tr><tr><td>∆ vs 2-CH</td><td>59.6%</td><td>58.5%</td><td>85.6%</td><td>56.2%</td><td>54.9%</td><td>82.8%</td><td>59.0%</td><td>58.6%</td><td>84.9%</td></tr><tr><td> $\Delta \ \nu s \ 3 – C H$ </td><td>40.9%</td><td>37.0%</td><td>67.3%</td><td>31.5%</td><td>27.9%</td><td>54.5%</td><td>39.9%</td><td>33.4%</td><td>66.9%</td></tr></table>

The results clearly demonstrate that the proposed model maintains consistent and superior performance across all three UAV altitudes. In particular, the RMSE remains tightly bounded between 3.17 dB and 3.28 dB, highlighting the model’s strong generalization capability with respect to UAV altitude. Compared to the original RadioUNet (3-CH), our model achieves an average reduction of 37% in MAE and 63% in NMSE. The performance gap is even more pronounced against the 2-CH variant, with improvements exceeding 58% in MAE and 84% in NMSE on average. Notably, the RMSE of our model varies minimally, ranging from only 3.17 dB to 3.28 dB across the 25 m, 35 m, and 45 m altitudes, a variation of just 0.11 dB. This is in contrast to both variants of the RadioUNet model, where the RMSE fluctuates more substantially: the 2-CH version varies by 0.68 dB (from 7.31 dB to 7.99 dB), while the 3-CH version varies by 0.79 dB (from 4.67 dB to 5.46 dB). These results confirm that the architecture effectively learns altitude-agnostic spatial features within the low-altitude UAV regime.

To further examine whether the observed altitude invariance extends beyond the considered range of 25–45 m, we conducted additional experiments at higher UAV altitudes of 80 m and 120 m. At these altitudes, the model’s RMSE increased to 9.87 dB and 10.21 dB, respectively. These results indicate that while the model generalizes well within the low-altitude range of 25–45 m, its performance degrades at substantially higher altitudes, where the underlying propagation characteristics are not fully captured by features learned in the lower-altitude regime.

## E. Noise Sensitivity Analysis

To evaluate the robustness of the proposed architecture under moderate input perturbations, we conduct a comprehensive noise sensitivity analysis. The primary objective is to quantify the model’s performance degradation under noisy input conditions, which simulate errors commonly encountered in practical UAV scenarios. In all experiments, noise is introduced only during inference, while the trained model remains unchanged. This setup mirrors deployment conditions where a model trained on clean, simulated data must generalize to imperfect real-world inputs.

1) Distance Channel Noise: We corrupt the distance input channel by adding zero-mean Gaussian noise to the raw distance values before using $( 2 0 \log _ { 1 0 } ( \cdot ) )$ and normalization. Two spatial regimes are evaluated separately: near-field receivers (distance <300 m) and far-field receivers (distance ≥ 300 m). For each regime, 10% of the receivers in each of the test environment are randomly selected, and Gaussian noise with standard deviation of 1%, 5%, and 10% of the true (nonnormalized) distance value is applied. The corrupted distances are then converted to dB scale $( 2 0 \log _ { 1 0 } ( \cdot ) )$ and normalized as per the original pre-processing pipeline before being fed to the model.

2) LOS Mask Noise: To simulate errors in LOS estimation, e.g. due to ray-tracing inaccuracies, we randomly flip the binary values (0 to 1 and 1 to 0) of LOS mask in a randomly selected fraction (1%, 5%, and 10%) of each test environment receiver grid.

TABLE X  
NOISE SENSITIVITY ANALYSIS ON IN-HOUSE UAV MMWAVE DATASET
<table><tr><td>Noise Scenario</td><td>RMSE↓</td><td>MAE↓</td><td>NMSE↓</td><td>Noise Scenario</td><td>RMSE↓</td><td>MAE↓</td><td>NMSE↓</td></tr><tr><td>Dist. Noise (Near, 1%)</td><td>3.18</td><td>2.39</td><td>0.000499</td><td>LOS Mask Flip (1%)</td><td>3.25</td><td>2.45</td><td>0.00052</td></tr><tr><td>Dist. Noise (Near, 5%)</td><td>3.18</td><td>2.39</td><td>0.000499</td><td>LOS Mask Flip (5%)</td><td>3.67</td><td>2.76</td><td>0.00066</td></tr><tr><td>Dist. Noise (Near, 10%)</td><td>3.18</td><td>2.39</td><td>0.000499</td><td>LOS Mask Flip (10%)</td><td>4.54</td><td>3.36</td><td>0.00100</td></tr><tr><td>Dist. Noise (Far, 1%)</td><td>3.17</td><td>2.38</td><td>0.000498</td><td>Bldg. Mask Flip (1%)</td><td>3.32</td><td>2.48</td><td>0.00054</td></tr><tr><td>Dist. Noise (Far, 5%)</td><td>3.17</td><td>2.38</td><td>0.000498</td><td>Bldg. Mask Flip (5%)</td><td>3.98</td><td>2.90</td><td>0.00078</td></tr><tr><td>Dist. Noise (Far, 10%)</td><td>3.17</td><td>2.38</td><td>0.000498</td><td>Bldg. Mask Flip (10%)</td><td>4.95</td><td>3.56</td><td>0.00120</td></tr></table>

3) Building Mask Noise: To simulate map inaccuracies or segmentation errors, the binary building occupancy mask is similarly corrupted by flipping a fraction (1%, 5%, 10%) of its pixel values at random in each test environment.

As shown in Table X, the model demonstrates strong resilience to distance channel noise, with negligible performance degradation observed even under 10% standard deviation. In fact, RMSE remains nearly constant across both near-field and far-field scenarios, indicating that the model does not heavily rely on high precision in distance values.

In contrast, performance is more sensitive to corruption in the binary masks, particularly the building mask. A 10% noise ratio in the building mask results in a notable RMSE increase from 3.15 dB (clean) to 4.95 dB, a relative degradation of 45.7%. Similarly, LOS mask corruption degrades RMSE to 4.54 dB at 10% noise. These findings suggest that the model relies significantly on spatial structure cues encoded in these masks for accurately inferring complex propagation conditions.

## F. Training and Inference Time Comparison

To assess the computational efficiency of the proposed architecture, we benchmark its training and inference characteristics against baseline models including an MLP and two variants of the RadioUNet (with 2 and 3 input channels, respectively).

1) Training Time: Each model was trained from scratch on our in-house UAV mmWave dataset under identical conditions on Google Colab platform using an NVIDIA L4 GPU (24 GB VRAM, 7, 424 CUDA cores) and 52 GB system RAM. Reported training time corresponds to the wall-clock time required to complete 40 epochs.

2) Inference Throughput: Inference throughput is defined as the number of samples processed per second, where a sample corresponds to one spatial pathloss prediction at a single location. For convolutional models (the proposed network and RadioUNet), a forward pass processes a 128 × 128 patch and yields 16,384 spatial predictions, each counted as an individual sample. The MLP predicts single spatial points and is evaluated using batched inference. All models are evaluated on the same test set comprising 15 environments split into six non-overlapping 128 × 128 patches, resulting in $1 5 \times 6 \times 1 2 8 \times 1 2 8$ samples. Throughput is thus computed by dividing this total sample count by the end-to-end inference time, ensuring unbiased cross-model comparison.

TABLE XI  
TRAINING TIME, INFERENCE THROUGHPUT, AND AVERAGE PER-SCENARIO INFERENCE LATENCY ON THE IN-HOUSE DATASET
<table><tr><td>Model</td><td>Training Time (min)</td><td>Throughput (samples/s)</td><td>Avg. Time per trans- mitter (s)</td></tr><tr><td>MLP</td><td>127.56</td><td>1,464</td><td>67.15</td></tr><tr><td>RadioUNet (2-ch)</td><td>35.43</td><td>189,127</td><td>0.52</td></tr><tr><td>RadioUNet (3-ch)</td><td>35.22</td><td>187,716</td><td>0.52</td></tr><tr><td>Ours (Full Model)</td><td>96.63</td><td>113,866</td><td>0.86</td></tr></table>

3) Average Time per Transmitter Scenario: In addition to throughput, we report the average time required to process one transmitter scenario. Each scenario consists of 128×128×6 = 98,304 samples, and the average time is computed by dividing this value (samples per scenario) by the measured inference throughput (samples per second). This metric provides a practical measure of the end-to-end inference latency per transmitter deployment.

Table XI summarizes the training times, inference throughput, and average time per transmitter scenario for all models. The comparison highlights the trade-off between computational efficiency and prediction accuracy. The MLP, while conceptually simple, exhibits the longest training time and the lowest inference throughput due to its sequential processing nature, making it unsuitable for practical deployment. The RadioUNet models are highly efficient in terms of throughput and achieve sub-second inference latency per transmitter scenario.

The proposed model introduces a parallel multi-scale feature extraction block and an ASPP bottleneck, both of which enhance prediction accuracy and robustness across environments. These architectural additions increase computational overhead, resulting in longer training time and slightly reduced inference throughput compared to RadioUNet. Consequently, the average time per transmitter scenario for our model is 0.86 s, which is marginally higher than the RadioUNet baselines (0.52 s).

Nevertheless, this inference latency remains extremely favorable when compared to ray-tracing-based propagation modeling, where a single transmitter scenario can take several minutes to hours depending on environment complexity. Thus, despite its modest overhead, the proposed model offers a highly efficient and scalable solution for accurate pathloss prediction in UAV-assisted mmWave networks.

## VII. CONCLUSION

This paper introduced a deep learning framework for UAV-assisted mmWave pathloss prediction that leverages multi-scale feature extraction and an ASPP bottleneck to capture complex propagation characteristics. Experiments across diverse urban environments showed that the model achieves higher accuracy than baseline methods while maintaining subsecond inference times per transmitter scenario. The parallel convolutional design, however, introduces additional computational overhead and slightly reduces throughput compared to lighter baselines. Future work will be directed toward improving generalization and reducing computational overhead.

## REFERENCES

[1] H. Tataria, M. Shafi, A. F. Molisch, M. Dohler, H. Sjoland, and¨ F. Tufvesson, “6G wireless systems: Vision, requirements, challenges, insights, and opportunities,” Proc. IEEE, vol. 109, no. 7, pp. 1166–1199, Jul. 2021.

[2] B. Li, Z. Fei, and Y. Zhang, “UAV communications for 5G and beyond: Recent advances and future trends,” IEEE Internet Things J., vol. 6, no. 2, pp. 2241–2263, Apr. 2019.

[3] K. Mao et al., “A survey on channel sounding technologies and measurements for UAV-assisted communications,” IEEE Trans. Instrum. Meas., vol. 73, pp. 1–24, 2024.

[4] C. Yan, L. Fu, J. Zhang, and J. Wang, “A comprehensive survey on UAV communication channel modeling,” IEEE Access, vol. 7, pp. 107769–107792, 2019.

[5] S. J. Maeng, H. Kwon, O. Ozdemir, and <sup>˙</sup>I. Guvenc¸, “Impact of 3-D¨ antenna radiation pattern in UAV air-to-ground path loss modeling and RSRP-based localization in rural area,” IEEE Open J. Antennas Propag., vol. 4, pp. 1029–1043, 2023.

[6] M. Song, Y. Huo, Z. Liang, X. Dong, and T. Lu, “Air-to-ground largescale channel characterization by ray tracing,” IEEE Access, vol. 10, pp. 125930–125941, 2022.

[7] X. Cheng, Y. Li, C.-X. Wang, X. Yin, and D. W. Matolak, “A 3-D geometry-based stochastic model for unmanned aerial vehicle MIMO Ricean fading channels,” IEEE Internet Things J., vol. 7, no. 9, pp. 8674–8687, Sep. 2020.

[8] G. Yang, Y. Zhang, Z. He, J. Wen, Z. Ji, and Y. Li, “Machine-learningbased prediction methods for path loss and delay spread in air-to-ground millimetre-wave channels,” IET Microw., Antennas Propag., vol. 13, no. 8, pp. 1113–1121, Apr. 2019.

[9] H. Li et al., “Air-to-ground path loss prediction using ray tracing and measurement data jointly driven DNN,” Comput. Commun., vol. 196, pp. 268–276, Dec. 2022.

[10] H. Zhang, J. Dong, X. Liu, J. Liu, and X. Zhang, “An artificial intelligence radio propagation model based on geographical information,” IEEE Trans. Antennas Propag., vol. 70, no. 12, pp. 12049–12060, Dec. 2022.

[11] U. Masood, H. Farooq, A. Imran, and A. Abu-Dayya, “Interpretable AIbased large-scale 3D pathloss prediction model for enabling emerging self-driving networks,” IEEE Trans. Mobile Comput., vol. 22, no. 7, pp. 3967–3984, Jul. 2023.

[12] S. P. Sotiroudis, G. Athanasiadou, G. Tsoulos, P. Sarigiannidis, C. G. Christodoulou, and S. K. Goudos, “Evolutionary ensemble learning pathloss prediction for 4G and 5G flying base stations with UAVs,” IEEE Trans. Antennas Propag., vol. 71, no. 7, pp. 5994–6005, Jul. 2023.

[13] S. Hussain, S. F. N. Bacha, A. A. Cheema, B. Canberk, and T. Q. Duong, “Geometrical features based-mmWave UAV path loss prediction using machine learning for 5G and beyond,” IEEE Open J. Commun. Soc., vol. 5, pp. 5667–5679, 2024.

[14] R. Levie, C¸ . Yapar, G. Kutyniok, and G. Caire, “RadioUNet: Fast radio map estimation with convolutional neural networks,” IEEE Trans. Wireless Commun., vol. 20, no. 6, pp. 4001–4015, Jun. 2021.

[15] A. Chaves-Villota and C. A. Viteri-Mera, “DeepREM: Deeplearning-based radio environment map estimation from sparse measurements,” IEEE Access, vol. 11, pp. 48697–48714, 2023, doi: 10.1109/ACCESS.2023.3277248.

[16] J.-H. Lee, O. G. Serbetci, D. P. Selvam, and A. F. Molisch, “PMNet: Robust pathloss map prediction via supervised learning,” in Proc. IEEE Global Commun. Conf. (GLOBECOM), Dec. 2023, pp. 4601–4606.

[17] J.-H. Lee and A. F. Molisch, “A scalable and generalizable pathloss map prediction,” IEEE Trans. Wireless Commun., vol. 23, no. 11, pp. 17793–17806, Nov. 2024.

[18] F. Jiang, T. Li, X. Lv, H. Rui, and D. Jin, “Physics-informed neural networks for path loss estimation by solving electromagnetic integral equations,” IEEE Trans. Wireless Commun., vol. 23, no. 10, pp. 15380–15393, Oct. 2024.

[19] Z. Fang et al., “RadioFormer: A multiple-granularity radio map estimation transformer with 1% spatial sampling,” 2025, arXiv:2504.19161.

[20] S. Hussain and C. Brennan, “Efficient preprocessed ray tracing for 5G mobile transmitter scenarios in urban microcellular environments,” IEEE Trans. Antennas Propag., vol. 67, no. 5, pp. 3323–3333, May 2019.

[21] S. Hussain and C. Brennan, “A dynamic visibility algorithm for ray tracing in outdoor environments with moving transmitters and scatterers,” in Proc. 14th Eur. Conf. Antennas Propag. (EuCAP), Mar. 2020, pp. 1–5.

[22] S. Hussain and C. Brennan, “A visibility matching technique for efficient millimeter-wave vehicular channel modeling,” IEEE Trans. Antennas Propag., vol. 70, no. 10, pp. 9977–9982, Oct. 2022.

[23] V. Degli-Esposti, F. Fuschini, E. M. Vitucci, and G. Falciasecca, “Measurement and modelling of scattering from buildings,” IEEE Trans. Antennas Propag., vol. 55, no. 1, pp. 143–153, Jan. 2007.

[24] K. Haneda et al., “5G 3GPP-like channel models for outdoor urban microcellular and macrocellular environments,” in Proc. IEEE 83rd Veh. Technol. Conf., May 2016, pp. 1–7.

[25] ITU Radiocommunication Sector (ITU-R), Recommendation ITU-R P.2109-2: Prediction of Building Entry Loss, document P.2109-2, Aug. 2023.

[26] O. Ronneberger, P. Fischer, and T. Brox, “U-Net: Convolutional networks for biomedical image segmentation,” in Proc. Int. Conf. Med. Image Comput. Comput.-Assist. Intervent. Cham, Switzerland: Springer, 2015, pp. 234–241.

[27] 3GPP, Study on Channel Model for Frequency Spectrum Above 6 GHz (Release 15), document TR 38.900 V15.0.0, Jul. 2018.

[28] Study on Channel Model for Frequencies From 0.5 to 100 GHz (Release 19), document TR 38.901 V19.0.0, Jun. 2025.

[29] ITU Radiocommunication Sector (ITU-R), Recommendation ITU-R P.1411-12: Propagation Data and Prediction Methods for the Planning of Short-Range Outdoor Radiocommunication Systems and Radio Local Area Networks in the Frequency Range 300 MHz to 100 GHz, document ITU-R P.1411-12, Aug. 2023.

![](images/abe0b310494d58e0e87271e7e47634d0d41fac4dc3953f1d3214539b0ace05c9.jpg)

Sajjad Hussain received the B.Sc. degree in electrical engineering from the University of Engineering and Technology Taxila, Taxila, Pakistan, in 2006, the M.Sc. degree in telecommunications engineering from the University of Liverpool, Liverpool, U.K., in 2008, and the Ph.D. degree in electronic engineering from Dublin City University, Dublin, Ireland, in 2017. From 2009 to 2013, he was a Technical and Test Engineer with Vodafone Automotive Ltd., Manchester, U.K. He is currently an Assistant Professor with the School of Electrical Engineering

and Computer Sciences, National University of Sciences and Technology, Islamabad, Pakistan. His research interests include radio channel modeling for future radio networks using ray tracing and machine learning.