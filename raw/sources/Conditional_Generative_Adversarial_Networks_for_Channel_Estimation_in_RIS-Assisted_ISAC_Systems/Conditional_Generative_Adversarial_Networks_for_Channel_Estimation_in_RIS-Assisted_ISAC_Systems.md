# Conditional Generative Adversarial Networks for Channel Estimation in RIS-Assisted ISAC Systems

Alice Faisal , Graduate Student Member, IEEE, Ibrahim Al-Nahhal , Senior Member, IEEE, Kyesan Lee, Member, IEEE, Octavia A. Dobre , Fellow, IEEE, and Hyundong Shin , Fellow, IEEE

Abstract— Integrated sensing and communication (ISAC) technology has been explored as a potential advancement for future wireless networks, striving to effectively use spectral resources for both communication and sensing. The integration of reconfigurable intelligent surfaces (RIS) with ISAC further enhances this capability by optimizing the propagation environment, thereby improving both the sensing accuracy and communication quality. Within this domain, accurate channel estimation is crucial to ensure a reliable deployment. Traditional deep learning (DL) approaches, while effective, can impose performance limitations in modeling the complex dynamics of wireless channels. This paper proposes a novel application of conditional generative adversarial networks (CGANs) to solve the channel estimation problem of an RIS-assisted ISAC system. The CGAN framework adversarially trains two DL networks, enabling the generator network to not only learn the mapping relationship from observed data to real channel conditions but also to improve its output based on the discriminator network feedback, thus effectively optimizing the training process and estimation accuracy. The numerical simulations demonstrate that the proposed CGAN-based method improves the estimation performance effectively compared to conventional DL techniques. The results highlight the CGAN’s potential to revolutionize channel estimation, paving the way for more accurate and reliable ISAC deployments.

Index Terms— Integrated sensing and communication (ISAC), reconfigurable intelligent surface (RIS), channel estimation, deep learning (DL), conditional generative adversarial networks (CGAN).

# I. INTRODUCTION

HE recent releases by the third generation partnership project (3GPP) represent crucial advancements in the

Received 18 August 2024; revised 8 December 2024 and 26 January 2025; accepted 29 January 2025. Date of publication 11 February 2025; date of current version 18 September 2025. This work was supported in part by the Canada Research Chairs Program under Grant CRC-2022-00187. The associate editor coordinating the review of this article and approving it for publication was F. Gao. (Corresponding authors: Octavia A. Dobre; Hyundong Shin.)

Alice Faisal and Ibrahim Al-Nahhal are with Memorial University, St. John’s, NL A1C 5S7, Canada (e-mail: afaisal@mun.ca; ioalnahhal@ mun.ca).

Kyesan Lee and Hyundong Shin are with the Department of Electronics and Information Convergence Engineering, Kyung Hee University, Yongin-si, Gyeonggi-do 17104, Republic of Korea (e-mail: kyesan@khu.ac.kr; hshin@khu.ac.kr).

Octavia A. Dobre is with the Memorial University, St. John’s, NL A1C 5S7, Canada, and also with the Department of Electronic Engineering, Kyung Hee University, Yongin 17104, Republic of Korea (e-mail: odobre@mun.ca).

Digital Object Identifier 10.1109/TCOMM.2025.3541047

evolution of fifth-generation (5G) networks, aiming at realizing the full potential of 5G and bridging the transition to the sixth-generation (6G) networks. One of the key focus areas of 3GPP Release-19 is the integration of sensing capabilities into communication networks, which paves the way for new applications [1], [2]. To this end, integrated sensing and communication (ISAC) is envisioned to play a key role in future generations of wireless networks by efficiently merging radar sensing with communication technologies within a single system. This convergence is expected to enhance spectrum utilization and reduce hardware costs compared to deploying separate systems with independent hardware for each function. ISAC is well-suited for a wide range of applications, such as drone operation, industrial automation, and health monitoring, where simultaneous data transmission and environmental sensing is needed.

ISAC has been investigated in the literature from various perspectives to realize its full potential [3], [4], [5], [6], [7], [8], [9], [10]. In particular, novel ISAC transceivers were investigated through the development of advanced beamforming and signal processing techniques [3], [4], [5]. Privacy and security concerns were addressed through the design of robust security protocols and privacy-preserving methods [6]. Some works focused on resource allocation problems in ISAC-based systems to maintain effective sensing and communication (SAC) operations [7], [8], [9], [10]. Solving optimization problems in ISAC systems often involve complex trade-offs between enhancing signal quality and optimizing power consumption across both SAC tasks. ISAC faces additional challenges, such as complex interference management issues that arise from simultaneously handling SAC tasks. Furthermore, the overlapping use of the spectrum for both functions can lead to signal contamination, necessitating advanced signal processing techniques to effectively distinguish between communication signals and sensing echoes. Moreover, the dual-use can also introduce power management difficulties, as both SAC operations can be power-intensive. Addressing these challenges is crucial for realizing the potential of ISAC networks.

Besides ISAC, the reconfigurable intelligent surfaces (RIS) have emerged as a potential technology to meet the demands of next-generation wireless networks. RIS consists of a two-dimensional array of low-cost passive elements that can be individually controlled to tune the phase, amplitude, and polarization of incoming signal. This enables RIS to effectively mitigate interference, enhance signal strength at the receiverside, and extend the wireless communication coverage [11]. Due to the unique properties of RIS and ISAC, the integration of both technologies represents a significant advancement in the development of future wireless networks. Notably, RIS can be deployed to help combat some of the ISAC system challenges. In particular, RIS can mitigate interference between SAC signals by enabling precise control over the propagation environment. Additionally, the passive nature of RIS elements can help reduce the overall energy consumption of the ISAC systems. This capability enhances the wireless communication signal quality and minimizes the system power simultaneously.

Recently, the joint integration of ISAC and RIS has been investigated in various wireless communication scenarios [12], [13], [14], [15], [16]. For example, the authors in [12] and [13] focused on optimizing the base station (BS) transmit precoding and RIS phase shifts to improve the radar estimation performance subject to the signal-to-interference-plus-noise ratio requirements of communication users. Furthermore, the work in [14] developed a beam training scheme that enables the BS to communicate with the users while also sensing targets. This approach distinguishes between the RIS and targets based on their mixed echoes, which is crucial to ensure seamless integration of RIS-assisted ISAC systems. Since conventional methods often face limitations, either suffering from high computational complexity when using iterative approaches or poor performance when using heuristic approaches, some studies considered deep learning (DL) for resource allocation tasks [17], [18].

It is important to note that accurate channel state information (CSI) is needed for all the above designs. The aforementioned works generally assumed that CSI is available at the receiver side and only focused on the resource allocation and interference mitigation problems in RIS-assisted ISAC systems. However, in practical scenarios, obtaining accurate CSI poses a significant challenge due to the coexistence of SAC channels within the same system. This introduces the need of innovative channel estimation strategies that can effectively distinguish between the mixed signals in RIS-assisted ISAC systems, ensuring both accurate sensing data and reliable communication. Despite its importance, only a limited number of studies addressed the channel estimation challenges in RIS-assisted ISAC systems [19], [20], [21], [22]. In [19], the authors focused on a single-RIS-assisted ISAC system and introduced a novel three-stage method to simplify the channel estimation process. The presented approach starts with direct channels estimation, followed by the estimation of reflected communication channel, and finally the reflected sensing channel. This framework utilizes two distinct convolutional neural network (CNN) models to accurately estimate the channels at the ISAC BS. Furthermore, the work in [20] considered a multi-user downlink RIS-assisted ISAC system and proposed two deep neural network (DNN) models to estimate the SAC channels. Specifically, the first DNN is implemented at the ISAC BS for the sensing channel estimation, while the second is deployed at each downlink user for communication channel estimation. Finally, the work in [21] considered a multi-user RIS-assisted ISAC system and proposed a two-stage framework to estimate the SAC channels, focusing sequentially on the direct and reflected links. The presented framework considered extreme learning machine (ELM) to meet the system requirements with accelerated training speed.

All the above works have benchmarked their performance against the least squares (LS) estimation technique. While commonly used, the LS estimation has several limitations including its sensitivity to noise, which can significantly degrade its performance in scenarios with low signal-tonoise ratio (SNR). Additionally, the LS estimator does not account for model non-linearities in the system, which can lead to biased and inefficient estimates in RIS-assisted ISAC environments. This gap points to the necessity for innovative approaches that enhance the estimation performance efficiently. Therefore, this work applies the conditional generative adversarial networks (CGANs) for channel estimation in RIS-assisted ISAC systems. Unlike regular DL methods that typically learn to map inputs to outputs in a supervised fashion, CGANs operate by training two models: a generator that creates data following the real data distribution, and a discriminator that learns to distinguish between the real and fake (i.e., generated) data. This adversarial process allows CGANs to generate accurate data and capture complex distributions, thereby enhancing the estimation and generalization capabilities over standard DL approaches. To the best of the authors’ knowledge, this is the first work to consider employing CGANs for channel estimation tasks in multi-user RIS-assisted ISAC systems. The contributions of this paper are summarized as follows:

• A CGAN-based estimation framework, incorporating two distinct DNN architectures, is devised to estimate the SAC channels for a multi-user RIS-assisted ISAC system. One DNN operates at the ISAC BS to estimate the sensing channel, while the other one is deployed at each downlink user to estimate the cascaded communication channel.   
• A custom loss function is carefully designed for training the proposed CGAN-based estimator to ensure accurate and robust channel estimation performance even in environments with low SNRs.   
• The proposed CGAN framework operates as a minimax two-player game, where the generative and discriminative models continuously compete and evolve during the training process. This dynamic interaction leads to a generative model capable of producing channel samples that mimic real distribution patterns. This advanced approach enables the CGAN to exhibit exceptional adaptability and scalability, which is essential for RIS-assisted ISAC systems.   
• The proposed CGAN-based channel estimation approach demonstrates strong generalization capabilities, where it achieves robust performance at SNR ranges that are not considered during the training phase. This robustness indicate that the model effectively eliminates the need for the SNR estimation stage in practical deployments.

![](images/32aa85526d66aa00a235c13a4a57d390882eaeaf8fa313b85fa85d7aed9a4b85.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Target"] -->|A| B["ISAC BS"]
    B -->|H| C["RIS"]
    C -->|r1 ... rk| D["k Users"]
    D -->|dk| E["User"]
    E --> F["User"]
    F --> G["User"]
    G --> H["User"]
    H --> I["User"]
    I --> J["User"]
```
</details>

(a)   
![](images/8dd6eca070b1f66630d6f3c3c274d1684faaa45cbf97d14d63b5b6e838268ef5.jpg)

<details>
<summary>text_image</summary>

BS
X₁
X₂
...
X_C
x₁ x₂ ... x_P x₁ x₂ ... x_P ... x₁ x₂ ... x_P
RIS
Θ
θ₁
θ₂
...
θ_C
</details>

Fig. 1. RIS-assisted ISAC system. (a) System model, (b) Pilot protocol.

• The computational complexity of the proposed CGAN approach is evaluated based on the number of real additions and multiplications. The numerical results indicate that the proposed algorithm achieves a complexity comparable to the DL-based benchmark estimator, which satisfies the low-cost deployment demands of RIS-assisted ISAC systems.   
• Extensive simulations are conducted to validate the estimation performance of the proposed approach. Numerical findings prove that the proposed method significantly outperforms the conventional DL-based approaches in the literature under a range of SNR conditions and system parameters.

The remainder of this paper1is organized as follows: The system model and problem formulation are introduced in Section II. The proposed channel estimation approach is presented in Section III, and the computational complexity is analyzed in Section IV. Finally, simulation results are shown in Section V and conclusions are drawn in Section VI.

# II. SYSTEM MODEL

Consider an RIS-assisted multiple-input single-output (MISO) ISAC system as illustrated in Fig. 1a, where the RIS facilitates the communication between the ISAC BS and

1Boldface uppercase and lowercase letters denote matrices and vectors, respectively. C and CN stand for a complex-valued variable and a complex-valued normally distributed random variable, respectively. $\mathrm { R e } \{ \cdot \}$ and Im{·} denote the real and imaginary components of a variable, respectively. $\mathbb { E } \{ \cdot \}$ denotes the expectation operation. The operators $( \cdot ) ^ { \mathrm { H } } , \mathrm { v e c } [ \cdot ] , ( \cdot ) ^ { - 1 }$ , $\| \cdot \| _ { 2 } ,$ , and ∥ · ∥F represent the Hermitian, vectorization, inverse, second order norm, and Frobenius norm of their arguments, respectively. diag{x} returns a matrix whose diagonal consists of the elements of x.

K downlink user equipments (UEs) and the BS communicates with a target for sensing purposes. The BS has M transmit antennas and one receive antenna, and each UE is equipped with one receive antenna. The RIS consists of N programmable reflecting elements. For target sensing, the BS sends radar signals towards the target and receives the echo signals through the BS-target-BS channel, denoted by ${ \textbf { A } } \in$ $\mathbb { C } ^ { \mathbf { \breve { M } } \times M }$ . The channel coefficients of the BS-RIS, RIS- $\mathrm { U E } _ { k } .$ , and ${ \mathrm { B S - U E } } _ { k }$ are represented as $\mathbf { H } \in \mathbb { C } ^ { M \times N } , ~ \mathbf { r } _ { k } \in \mathbb { C } ^ { N \times 1 }$ , and $\mathbf { d } _ { k } \in \mathbb { C } ^ { M \times 1 }$ , respectively. Note that all the SAC channels are assumed to be flat-fading considering the narrowband transmission [23], [24], [25], [26]. Given that the ISAC BS operates in full-duplex mode, transmitting and receiving signals simultaneously, it experiences self-interference (SI); the SI channel is represented as $\mathbf { S } \in \mathbb { C } ^ { M \times M }$ .

A pilot transmission policy is developed to estimate the SAC channels in the multi-user RIS-assisted ISAC system, as shown in Fig. 1b. The ISAC BS transmits pilot sequences in C subframes, in which each sub-frame is divided into $P$ time slots. The pilot signal of the ISAC BS at the p-th time slot is defined as $\mathbf { x } _ { p } \in \mathbb { C } ^ { M \times 1 }$ . To this end, the pilot matrix in sub-frame c is represented as ${ \bf X } _ { c } = [ { \bf x } _ { 1 } , { \bf x } _ { 2 } , \cdot \cdot \cdot , { \bf x } _ { P } ] \in \mathbb { C } ^ { M \times P }$ . It is worth noting that the ISAC BS transmits the same pilot sequences (i.e., denoted as X) in each sub-frame. Consequently, the RIS phase shifts remain unchanged within a single sub-frame, being denoted by $\pmb { \theta } _ { c } \in \mathbb { C } ^ { N \times 1 }$ . The corresponding phase shift matrix is represented by $\Theta = [ \pmb { \theta } _ { 1 } , \pmb { \theta } _ { 2 } , \cdot \cdot \cdot , \pmb { \theta } _ { C } ] \in \mathbb { C } ^ { N \times C }$ . Let $P = M$ and $C = N$ to accommodate the necessity for low pilot overhead. This design allows to effectively capture the necessary channel information without requiring additional pilot resources, which significantly reduces redundancy and prevents excessive pilot usage. Furthermore, both X and Θ are modeled as a discrete Fourier transform (DFT) matrix, expressed as

$$
\mathbf {X} = \left[ \begin{array}{c c c c} 1 & 1 & \dots & 1 \\ 1 & X ^ {1} & \dots & X ^ {P - 1} \\ \vdots & \vdots & \ddots & \vdots \\ 1 & X ^ {M - 1} & \dots & X ^ {(M - 1) (P - 1)} \end{array} \right], \tag {1}
$$

where $X ^ { ( m , p ) } ~ = ~ { \frac { 1 } { \sqrt { M } } } e ^ { j { \frac { 2 \pi } { M } } m p }$ is the $( m , p )$ -th entry of X. Modeling X as a DFT matrix helps combat the interference between the SAC signals and distinguish between multi-user signals. Furthermore, it has been demonstrated that designing Θ as a DFT matrix helps to boost the power of the received signal at UEs and ensure accurate channel estimation [27].

To this end, the received signal at the k-th downlink UE for sub-frame c and time slot p is expressed as

$$
y _ {k, c, p} ^ {\mathrm{UE}} = \left(\mathbf {r} _ {k} ^ {H} \operatorname{diag} \left\{\boldsymbol {\theta} _ {c} ^ {H} \right\} \mathbf {H} ^ {H} + \mathbf {d} _ {k} ^ {H}\right) \mathbf {x} _ {p} + n _ {k, c, p}. \tag {2}
$$

Here, $n _ { k , c , p } ~ \sim ~ \mathcal { C N } ( 0 , \sigma ^ { 2 } )$ is the complex additive white Gaussian noise (AWGN) with zero-mean and variance $\sigma ^ { 2 } .$ . The RIS phase shifts are expressed as [28]

$$
\boldsymbol {\theta} _ {c} = \left[ \beta_ {c} e ^ {j \varphi_ {c, 1}}, \beta_ {c} e ^ {j \varphi_ {c, 2}}, \dots , \beta_ {c} e ^ {j \varphi_ {c, N}} \right] ^ {T},
$$

$$
\varphi_ {c, n} \in [ 0, 2 \pi), \beta_ {c} \in [ 0, 1 ], \tag {3}
$$

where $\beta _ { c } \in [ 0 , 1 ]$ represents the RIS element amplitude. The direct link is assumed to be blocked by obstacles and the reflected link is considered to support the communication. Here, diag {.} transforms a vector into a diagonal matrix. This transformation implies the following

$$
\operatorname{diag} \left\{\boldsymbol {\theta} _ {c} \right\} \mathbf {r} _ {k} = \left[ \theta_ {1} r _ {1}, \theta_ {2} r _ {2}, \dots , \theta_ {N} r _ {N} \right]. \tag {4}
$$

Similarly, constructing diag $\left\{ \boldsymbol { r } _ { k } \right\}$ and multiplying it by $\pmb { \theta } _ { c }$ would produce the same result, confirming the equality diag $\begin{array} { r } { \{ \pmb { \theta } _ { c } \} { \bf r } _ { k } ~ = ~ \mathrm { d i a g } \{ { \bf r } _ { k } \} \pmb { \theta } _ { c } } \end{array}$ c [29]. Using this property, the cascaded reflected channel of the $\mathbf { B S - R I S - U E } _ { k }$ is expressed as

$$
\mathbf {G} _ {k} = \mathbf {H} \operatorname{diag} \{\mathbf {r} _ {k} \} \in \mathbb {C} ^ {M \times N}. \tag {5}
$$

Therefore, (2) can be formulated as

$$
y _ {k, c, p} ^ {\mathrm{UE}} = \boldsymbol {\theta} _ {c} ^ {H} \mathbf {G} _ {k} ^ {H} \mathbf {x} _ {p} + n _ {k, c, p}. \tag {6}
$$

On the other hand, the received signal at the ISAC BS is expressed as

$$
\mathbf {y} _ {c, p} ^ {\mathrm{BS}} = \underbrace {\mathbf {A} ^ {H} \mathbf {x} _ {p}} _ {\text { Sensing   signal }} + \underbrace {\mathbf {S} ^ {H} \mathbf {x} _ {p}} _ {\text { SI }} + \mathbf {n} _ {c, p}, \tag {7}
$$

where $\mathbf { n } _ { c , p } \sim \mathcal { C N } ( 0 , \sigma ^ { 2 } \mathbf { I } _ { M } )$ denotes the complex AWGN with zero-mean and variance $\sigma ^ { 2 }$ . Here, ${ \mathbf { I } } _ { M }$ represents an identity matrix with size M. Since the propagation environment between the ISAC BS transmitting and receiving antennas is presumed to be stable [30], the SI channel, S, can be pre-determined at the ISAC BS. This allows for the compensation of any residual SI in (7) prior to the SAC estimation process. The estimation problems of the SAC channels in (6) and (7) are challenging. In what follows, we propose a novel approach to estimate both $\mathbf { G } _ { k }$ and A based on the pilot protocol in Fig. 1b.

# III. PROPOSED ESTIMATION APPROACH

In traditional DL approaches for channel estimation, performance can saturate or generalize poorly when dealing with noisy or complex data environments, due to their dependence on direct mappings from input to output data. To address these limitations, the proposed method leverages GANs, which integrate a network feedback to refine the generation process. This adversarial setup not only enhances the ability to handle diverse and noisy datasets but also improves the network capability to generate realistic channel estimates that closely mimic actual channel conditions, ensuring robust performance across various scenarios. This section provides an overview of GANs and then details the proposed framework for the channel estimation problem in RIS-assisted ISAC systems.

# A. Overview of Generative Adversarial Networks

GANs are a novel class of DL frameworks introduced in [31], consisting of two DNNs: the generator and discriminator. In this framework, the generator strives to produce data that cannot be distinguished from the original dataset. The discriminator, on the other hand, tries to classify the given data as real or fake (i.e., generated samples). Both networks engage in a continuous adversarial training process, where the discriminator learns to identify generated data more accurately and the generator learns to better generate data samples given the mutual feedback. This process continues until the generator learns to produce real-like samples that the discriminator fails to identify as fake.

GANs and their variants have been utilized across a range of applications beyond the realm of wireless communications. It has been considered to generate synthetic human faces and transforming real-world scenery images into styles of famous paintings [32]. Additional examples include enhancing image resolution, and generating music, audio, and video [33], [34], [35]. In the field of wireless communications, GANs have emerged as powerful tool for various applications [36]. In particular, GANs has been used to generate synthetic data that augment existing datasets in situations where collecting real wireless communication data is challenging. This is particularly useful for tasks such as signal classification, mitigating wireless jamming attacks, and spectrum sensing [37], [38], [39]. GANs have been further considered for optimizing wireless systems, where they learn to generate accurate resource allocation decisions by modeling the network environment and the continuous feedback from the discriminator [40]. Overall, GANs contribute significantly to advancements in network design, optimization, and data generation in wireless communications, driving forward innovations that enhance the efficiency and reliability of wireless systems.

In traditional GANs, the generator, $G ,$ takes as an input random noise vector, z, typically drawn from a Gaussian or uniform distribution, $d ( \mathbf { z } )$ . It outputs data that resemble the target data on which the model was trained, denoted by $G ( \mathbf { z } )$ . The discriminator takes the target (i.e., real data) as an input, x, with distribution $d ( \mathbf { x } )$ , and the generated data, $G ( \mathbf { z } )$ . The output of the discriminator is a binary classification, $D ( \mathbf { x } )$ and $D ( G ( \mathbf { z } ) ) \in \{ 0 , 1 \}$ , where the goal is to determine whether the given data are real or fake. The objective function of GANs is represented as

$$
\min _ {G} \max _ {D} \mathbb {E} _ {\mathbf {x} \sim d (\mathbf {x})} [ \log (D (\mathbf {x})) ] + \mathbb {E} _ {\mathbf {z} \sim d (\mathbf {z})} [ \log (1 - D (G (\mathbf {z}))) ]. \tag {8}
$$

The first term in (8) represents the expected value of the discriminator output (i.e., probability that x is real) over all real data samples, x. The discriminator focuses on maximize this term by assigning higher probabilities to real data, thus maximizing log $\mathbf { \nabla } _ { \mathbf { D } ( \mathbf { x } ) ) }$ . Furthermore, the discriminator aims to maximize the value of the second term by minimizing $D ( G ( \mathbf { z } ) )$ (i.e., probability that input is generated). On the other hand, the generator aims to maximize $D ( G ( \mathbf { z } ) )$ by convincing the discriminator that the generated input is real.

Both the generator and discriminator are updated through an iterative process, each using a distinct loss function derived from the overall objective function in (8). This training process involves alternating updates to the discriminator and the generator with the goal of optimizing their respective loss functions. The loss functions of the discriminator and generator are respectively given as

$$
L _ {D} = - \frac {1}{2} \sum_ {j = 1} ^ {b} \left[ \log D (\mathbf {x} _ {j}) + \log (1 - D (G (\mathbf {z} _ {j}))) \right], \tag {9}
$$

and

$$
L _ {G} = - \frac {1}{b} \sum_ {j = 1} ^ {b} \log D (G (\mathbf {z} _ {j})), \tag {10}
$$

where b is the batch size.

Given the above concept, GANs have made significant progress in the field of generative modeling, offering the ability to produce highly realistic samples across various domains. However, despite their successes, traditional GANs face a primary challenge that can affect their applicability to wireless systems. The main issue is the lack of control over the generated data. In particular, the generator learns to create data that can fool the discriminator but does not necessarily retain the essential features or characteristics of the target. This can result in a lack of diversity in the outputs, making it difficult to capture the complexity of channel variations and the specific structure of wireless communication signals. Furthermore, traditional GANs have limited interpretability, where changes in the input noise vector do not directly correspond to meaningful variations in the generated data, which is a critical requirement in complex environments, such as wireless communication systems.

To address these limitations, CGANs have been specifically developed to incorporate additional information that guides the data generation process [41]. In CGANs, the generator and discriminator models are conditioned on auxiliary information, such as class labels or specific data attributes. This conditioning allows the generator to produce samples that align with the provided conditions, ensuring that the generated outputs maintain the necessary characteristics of the target data distribution. As a result, CGANs offer improved diversity, stability, and faster convergence in training. In the context of channel estimation, CGANs enable the generator to be conditioned on different channel states or environmental parameters, which is essential for accurately modeling the characteristics of the channel. This conditioning mechanism allows CGANs to adapt to variations in channel properties, leading to a more robust channel estimation process that can handle rapidly changing communication environments. Unlike basic GANs, which rely solely on input noise, the proposed CGAN framework in this work uses received observations as conditional inputs, allowing it to learn and reproduce complex channel structures with higher accuracy. In what follows, we detail the proposed CGAN channel estimation approach for RIS-assisted ISAC systems.

# B. Proposed CGAN-Based DL Framework

This section introduces a novel channel estimation approach utilizing CGANs. Initially, the configuration of the input-output pairs for the framework is carefully designed. Building on this, a CGAN-based channel estimation approach is developed to enhance the estimation performance.

# 1) Input-Output Pair Design:

a) SAC Design: Consider the received signal in (6) to construct the input-output pairs for estimating the communication channel. In each sub-frame, the received signal at $\mathrm { U E } _ { k }$ across P time slots is represented by

$$
\mathbf {y} _ {k, c} ^ {\mathrm{UE}} = \boldsymbol {\theta} _ {c} ^ {H} \mathbf {G} _ {k} ^ {H} \mathbf {X} + \mathbf {n} _ {k, c}, \tag {11}
$$

where yUEk,c $\mathbf { y } _ { k , c } ^ { \mathrm { U E } } = \left[ y _ { k , c , 1 } ^ { \mathrm { U E } } , y _ { k , c , 2 } ^ { \mathrm { U E } } , \cdot \cdot \cdot , y _ { k , c , P } ^ { \mathrm { U E } } \right] \in \mathbb { C } ^ { 1 \times P }$ and $\mathbf { n } _ { k , c } =$ $[ n _ { k , c , 1 } , n _ { k , c , 2 } , \dot { \mathrm { \dots ~ } } , n _ { k , c , P } ] \in \mathbb { C } ^ { 1 \times P }$ . Based on this, the communication data design is given as

$$
\mathbf {R} ^ {\mathrm{UE} _ {k}} = \left[ \operatorname{Re} \left\{\mathbf {y} _ {k, 1} ^ {\mathrm{UE}}, \mathbf {y} _ {k, 2} ^ {\mathrm{UE}}, \dots , \mathbf {y} _ {k, C} ^ {\mathrm{UE}} \right\}, \right.
$$

$$
\left. \operatorname{Im} \left\{\mathbf {y} _ {k, 1} ^ {\mathrm{UE}}, \mathbf {y} _ {k, 2} ^ {\mathrm{UE}}, \dots , \mathbf {y} _ {k, C} ^ {\mathrm{UE}} \right\} \right] ^ {T}. \tag {12}
$$

The corresponding output (i.e., target) is the ground truth channel, Gk, given as

$$
\mathbf {O} ^ {\mathrm{UE} _ {k}} = \left[ \operatorname{Re} \{\operatorname{vec} [ \mathbf {G} _ {k} ] \}, \operatorname{Im} \{\operatorname{vec} [ \mathbf {G} _ {k} ] \} \right] ^ {T}. \tag {13}
$$

On the other hand, to construct the input-output pairs for estimating the sensing channel, consider the received signal in (7). Similarly, the received signals at the ISAC BS are stacked across each sub-frame, C, leading to

$$
\mathbf {Y} _ {c} ^ {\mathrm{BS}} = \mathbf {A} ^ {H} \mathbf {X} + \mathbf {N} _ {c}, \tag {14}
$$

where $\mathbf { N } _ { c } ~ = ~ [ \mathbf { n } _ { c , 1 } , \mathbf { n } _ { c , 2 } , \cdots , \mathbf { n } _ { c , P } ] ~ \in ~ \mathbb { C } ^ { M \times P }$ and $\mathbf { Y } _ { c } ^ { \mathrm { B S } } \ =$ $\left[ \mathbf { y } _ { c , 1 } ^ { \mathrm { B S } } , \mathbf { y } _ { c , 2 } ^ { \mathrm { B S } } , \cdot \cdot \cdot , \mathbf { y } _ { c , P } ^ { \mathrm { B S } } \right] \in \mathbb { C } ^ { M \times P }$ . To this end, the sensing data is generated as

$$
\mathbf {R} ^ {\mathrm{BS}} = \left[ \operatorname{Re} \left\{\operatorname{vec} \left[ \mathbf {Y} _ {1} ^ {\mathrm{BS}}, \mathbf {Y} _ {2} ^ {\mathrm{BS}}, \dots , \mathbf {Y} _ {C} ^ {\mathrm{BS}} \right] \right\}, \right.
$$

$$
\left. \operatorname{Im} \left\{\operatorname{vec} \left[ \mathbf {Y} _ {1} ^ {\mathrm{BS}}, \mathbf {Y} _ {2} ^ {\mathrm{BS}}, \dots , \mathbf {Y} _ {C} ^ {\mathrm{BS}} \right] \right\} \right] ^ {T}. \tag {15}
$$

Accordingly, the output is the ground truth channel, A, given as

$$
\mathbf {O} ^ {\mathrm{BS}} = \left[ \operatorname{Re} \{\operatorname{vec} [ \mathbf {A} ] \}, \operatorname{Im} \{\operatorname{vec} [ \mathbf {A} ] \} \right] ^ {T}. \tag {16}
$$

It is worth noting that ground truth channels are used solely for the training phase. During training, the availability of the true channel values enables the CGAN network to learn the underlying channel generation process effectively. However, in the testing phase, the only available information is the observation, represented by the received signal at the BS or UE. In this phase, the trained CGAN relies on this received signal to generate an estimate of the channels. This ensures that the CGAN model generalizes well to real-world scenarios, where the true channels are unknown. Note that the generated dataset will not be used for direct input-output relationship as the case with regular NNs. The following sub-section will detail the working principle of the proposed CGAN channel estimation framework.

b) Dataset Generation: The training samples are produced by utilizing Q received signals (i.e., each of the communication and sensing signals in (11) and (14), respectively), along with V − 1 duplicates of the q-th signal. The duplicates are created by adding synthetic AWGN to the l chaand ccording to SNRdenote the chan $\begin{array} { r } { \dot { { \bf A } } / { \bf G } _ { k } } & { { } = \frac { p { \bf A } / { \bf G } _ { k } } { \sigma _ { { \bf A } / { \bf G } _ { k } } ^ { 2 } } } \end{array}$ pA/Gk σ2A/Gk , wheresynthetic $p _ { \mathbf { A } / \mathbf { G } _ { k } }$ $\sigma _ { \mathbf { A } / \mathbf { G } _ { k } } ^ { 2 }$ noise, respectively [20]. This dataset includes both noise-free original signals and their noisy versions to enhance the robustness and performance of the CGAN estimation model.

![](images/1ea9be567e95898fd5ebd32e0bc5beda1dcccaba192e7df2d5a2492a681bf55e.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Received signal at the BS"] --> B["R^BS_ Standardization"]
    B --> C["Generator SE-CGAN"]
    C --> D["Estimated Â"]
    D --> E["Target A"]
    E --> F["Discriminator SE-CGAN"]
    F --> G["Real"]
    F --> H["Fake"]
    C --> I["Generator Loss"]
    I --> J["∇Λg ½ Σj=1^b [log(1 - D(G(Rj^BS))) + αL2"]]
    D --> K["Discriminator Loss"]
    K --> L["∇Λd ½ Σj=1^b [log(D(A^j))"] + log(1 - D(G(Rj^BS)))]
    C --> M["FF NN"]
    M --> N["O^BS Scaling (×ρ)"]
    N --> C
    style A fill:#f9f,stroke:#333
    style F fill:#bbf,stroke:#333
```
</details>

![](images/d9132940023bb902a32e1f43da4acc4e3e0a9f6faee7d9767864f6ca03183661.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Received signal at the UE"] --> B["Generator CE-CGAN"]
    B --> C["Estimated Ĝ_k"]
    C --> D["Target G_k"]
    D --> E["Discriminator CE-CGAN"]
    E --> F["Real Fake"]
    B --> G["Generator Loss"]
    G --> H["∇_Λ_b ½ Σ_j=1^b [log(1 - D(G(R_j^UE_k))) + αL_2"]]
    C --> I["Discriminator Loss"]
    I --> J["∇_Λ_d ½ Σ_j=1^b [log(D(G_R_j^UE_k)) + log(1 - D(G(R_j^UE_k))))"]]
    B --> K["Scaling (×ρ)"]
    K --> L["σ^UE_k\nR^UE_k\nStandardization\nR^UE_k\nR^UE_k\nR^UE_k\nO^UE_k"]
    style A fill:#f9f,stroke:#333
    style E fill:#bbf,stroke:#333
```
</details>

(a)

![](images/ee1a5aa83bd8a91d1b06cdaa2cafc258485db97b52a5520319465ed50d841946.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["Received signal at the BS"] --> B["σ^BS Scaling (×ρ)"]
    B --> C["Generator SE-CGAN"]
    C --> D["Estimated Â"]
```
</details>

![](images/5dae1cb32b45cb72cb27a5359291dc96199c7a75e197541da5bf75bdfe15bd9d.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["Received signal at the UE"] --> B["R^UE_k Standardization"]
    B --> C["O^UE_k Scaling (×ρ)"]
    C --> D["Generator CE-CGAN"]
    D --> E["Estimated Ĝ_k"]
```
</details>

(b)   
Fig. 2. Proposed CGAN-based channel estimation framework for RIS-assisted ISAC system. (a) Offline training. (b) Online testing.

Accordingly, the dataset for communication and sensing can be respectively represented as

$$
\left(\mathcal {R} ^ {\mathrm{UE} _ {k}}, \mathcal {O} ^ {\mathrm{UE} _ {k}}\right) = \left\{\left(\mathbf {R} _ {(1, 1)} ^ {\mathrm{UE} _ {k}}, \mathbf {O} _ {(1)} ^ {\mathrm{UE} _ {k}}\right), \left(\mathbf {R} _ {(1, 2)} ^ {\mathrm{UE} _ {k}}, \mathbf {O} _ {(1)} ^ {\mathrm{UE} _ {k}}\right), \dots , \right.
$$

$$
\left. \left(\mathbf {R} _ {(1, V)} ^ {\mathrm{UE} _ {k}}, \mathbf {O} _ {(1)} ^ {\mathrm{UE} _ {k}}\right), \left(\mathbf {R} _ {(2, 1)} ^ {\mathrm{UE} _ {k}}, \mathbf {O} _ {(2)} ^ {\mathrm{UE} _ {k}}\right), \dots , \left(\mathbf {R} _ {(Q, V)} ^ {\mathrm{UE} _ {k}}, \mathbf {O} _ {(Q)} ^ {\mathrm{UE} _ {k}}\right) \right\}, \tag {17}
$$

and

$$
\begin{array}{l} \left(\mathcal {R} ^ {\mathrm{BS}}, \mathcal {O} ^ {\mathrm{BS}}\right) = \left\{\left(\mathbf {R} _ {(1, 1)} ^ {\mathrm{BS}}, \mathbf {O} _ {(1)} ^ {\mathrm{BS}}\right), \left(\mathbf {R} _ {(1, 2)} ^ {\mathrm{BS}}, \mathbf {O} _ {(1)} ^ {\mathrm{BS}}\right), \dots , \right. \\ \left. \left(\mathbf {R} _ {(1, V)} ^ {\mathrm{BS}}, \mathbf {O} _ {(1)} ^ {\mathrm{BS}}\right), \left(\mathbf {R} _ {(2, 1)} ^ {\mathrm{BS}}, \mathbf {O} _ {(2)} ^ {\mathrm{BS}}\right), \dots , \left(\mathbf {R} _ {(Q, V)} ^ {\mathrm{BS}}, \mathbf {O} _ {(Q)} ^ {\mathrm{BS}}\right) \right\}. \tag {18} \\ \end{array}
$$

2) Working Principle: The proposed CGAN-based estimation framework to estimate A and $\mathbf { G } _ { k }$ is shown in Fig. 2 and detailed as follows:   
a) Offline Training: The generator NN aims to estimate the SAC channels based on the conditional input, which includes the received signal observations, $\mathbf { R } ^ { \mathrm { B S } }$ or $\bar { \mathbf { R } } ^ { \mathrm { U E } _ { k } }$ . Prior to being passed into the generator, these received signals undergo preprocessing steps to ensure that the input data

has a consistent range and to improve the model stability. A standardization is performed on the (q, v)-th input data, which can be mathematically expressed as

$$
\mathbf {R} _ {\mathrm{std}} ^ {\mathrm{BS/UE} _ {k}} (q, v) = \frac {\mathbf {R} ^ {\mathrm{BS/UE} _ {k}} (q , v) - \mathbb {E} \left\{\mathbf {R} ^ {\mathrm{BS/UE} _ {k}} (q , v) \right\}}{\mathbb {D} \left\{\mathbf {R} ^ {\mathrm{BS/UE} _ {k}} (q , v) \right\}}, \tag {19}
$$

where ${ \mathbb E } \{ { \bf R } ^ { \mathrm { B S / U E } _ { k } } ( q , v ) \}$ and $\mathbb { D } \{ { \bf R } ^ { \mathrm { B S / U E } _ { k } } ( q , v ) \}$ denote the mean and standard deviation of the input, respectively. Additionally, the estimation target is scaled to facilitate the learning process as follows

$$
\mathbf {O} _ {s} ^ {\mathrm{BS/UE} _ {k}} (q, v) = \rho \mathbf {O} ^ {\mathrm{BS/UE} _ {k}} (q, v), \tag {20}
$$

where $\rho$ is the scaling factor.

The discriminator NN, on the other hand, aims to identify whether a given input is real (i.e., labeled 1) or fake (i.e., labeled 0), as derived from the generator output; this process is summarized as follows

$$
D (\mathbf {B}) = \left\{ \begin{array}{l l} 1, & \text { if } \mathbf {B} \in \{\mathbf {A}, \mathbf {G} _ {k} \} \\ 0, & \text { if } \mathbf {B} \in \{\hat {\mathbf {A}}, \hat {\mathbf {G}} _ {k} \}, \end{array} \right. \tag {21}
$$

TABLE I ARCHITECTURE OF SE-CGAN AND CE-CGAN 

<table><tr><td>Model</td><td>Network</td><td>Layers</td><td>Size</td><td>Filter</td><td>Activation Function</td></tr><tr><td rowspan="8">SE-CGAN</td><td rowspan="4">Generator</td><td>Input</td><td> $2MP$ </td><td>-</td><td>-</td></tr><tr><td>FFL</td><td>100</td><td>-</td><td>LeakyReLU</td></tr><tr><td>FFL</td><td>200</td><td>-</td><td>LeakyReLU</td></tr><tr><td>Output</td><td> $2M^2$ </td><td>-</td><td>-</td></tr><tr><td rowspan="4">Discriminator</td><td>Input</td><td> $2M^2$ </td><td>-</td><td>-</td></tr><tr><td>FFL</td><td>100</td><td>-</td><td>LeakyReLU</td></tr><tr><td>FFL</td><td>200</td><td>-</td><td>LeakyReLU</td></tr><tr><td>Output</td><td>1</td><td>-</td><td>-</td></tr><tr><td rowspan="8">CE-CGAN</td><td rowspan="4">Generator</td><td>Input</td><td> $2P$ </td><td>-</td><td>-</td></tr><tr><td>CL</td><td>132</td><td>4</td><td>LeakyReLU</td></tr><tr><td>FFL</td><td>500</td><td>-</td><td>LeakyReLU</td></tr><tr><td>Output</td><td> $2MN$ </td><td>-</td><td>-</td></tr><tr><td rowspan="4">Discriminator</td><td>Input</td><td> $2MN$ </td><td>-</td><td>-</td></tr><tr><td>CL</td><td>132</td><td>4</td><td>LeakyReLU</td></tr><tr><td>FFL</td><td>500</td><td>-</td><td>LeakyReLU</td></tr><tr><td>Output</td><td>1</td><td>-</td><td>-</td></tr></table>

where B represents the input to the discriminator, either as ground truth channel matrices, A or $\mathbf { G } _ { k } .$ , or generated estimates Aˆ or $\hat { \mathbf { G } } _ { k }$ .

In this work, the overall objective function of $\mathrm { G A N s }$ presented in (8) is further improved by adding an $L _ { 2 }$ term. This modification guides the generator towards more accurate estimates, ensuring that the generated channel not only deceives the discriminator but also closely approximates the true channel values. Furthermore, the $L _ { 2 }$ loss term serves as a regularizer, penalizing large deviations from the target values. This helps prevent overfitting and fosters a model that generalizes better to new, unseen data while maintaining robustness against noise in received signals. To this end, (8) becomes

$$
\begin{array}{l} \min _ {G} \max _ {D} \mathbb {E} \bigl [ \log \bigl (D \bigl (\mathbf {A}, \mathbf {G} _ {k} \bigr) \bigr) \bigr ] \\ + \mathbb {E} \left[ \log \left(1 - D \left(G \left(\mathbf {R} ^ {\mathrm{BS}}\right), G \left(\mathbf {R} ^ {\mathrm{UE} _ {k}}\right)\right)\right) \right] + \alpha L _ {2}, \tag {22} \\ \end{array}
$$

where

$$
L _ {2} = \mathbb {E} \big [ \big \| \mathbf {B} - G (\mathbf {R}) \big \| ^ {2} \big ]. \tag {23}
$$

Here, B denotes the SAC channels (i.e., $\mathbf { B } = \{ \mathbf { A } , \mathbf { G } _ { k } \} )$ , and R is the input data (i.e., ${ \bf R } = \{ { \bf R } ^ { \mathrm { B S } } , { \bf R } ^ { \mathrm { U E } _ { k } } \} )$ . Furthermore, α a weighting factor that enhances the stability of the channel estimates by penalizing large deviations from the target outputs. The generator and discriminator are trained together in an adversarial manner, where each network contributes to the loss of the other. Specifically, the generator aims to create estimates that can fool the discriminator, while the discriminator aims to correctly distinguish between real and generated data. This adversarial training is repeated until convergence, where the generator learns to produce realistic estimates. Fig. 2a illustrates the proposed CGAN DNN architectures for the SAC channels estimation and summarizes the offline training process.

In particular, two different architectures are developed within the CGAN framework: one for sensing channel estimation (SE-CGAN) and the other one for communication channel estimation (CE-CGAN). The SE-CGAN network is designed as feedforward (FF) fully connected NN, while the CE-CGAN as CNN to handle the complicated input-output relationship associated with the cascaded communication channel. In particular, the proposed SE-CGAN starts with an input layer, an FF layer (FFL) and a batch normalization layer to stabilize the NN output. The output is then fed to the second FFL followed by the second batch normalization and an output layer. On the other hand, the CE-DNN consist of one convolutional layer (CL), batch normalization layer, followed by a flatten layer, an FFL, and a second batch normalization layer at the end. The two hidden layers for each of the SE-CGAN and CE-CGAN networks use the LeakyReLU activation function. This is defined as follows

$$
\text { LeakyReLU } (x) = \left\{ \begin{array}{l l} x & \text { if   } x > 0 \\ \gamma x & \text { otherwise. } \end{array} \right. \tag {24}
$$

Here, γ is a small constant value, which is set to 0.2. Both CGANs utilize a discriminator architecture that is identical to their respective generators. The only difference consists in the output layer size; the generator outputs the estimated channels, whereas the discriminator outputs a single value (i.e., 0 or 1) to evaluate the input data. The Adam optimizer is adopted to update the generator and discriminator parameters with a learning rate of $2 \times 1 0 ^ { - 4 }$ and $2 \times 1 0 ^ { - 5 }$ , respectively [42]. These learning rates were carefully chosen based on extensive hyperparameter tuning. During this process, various learning rates were tested to find an optimal balance between convergence speed and estimation accuracy. Lower learning rates helped achieve more stable performance. Selecting a slightly higher rate for the generator enabled faster adaptation to the changes in the discriminator feedback. The minibatch transitions is set to size 16 and α = 100. The detailed architectures of the SE-CGAN and CE-CGAN are summarized in Table I.

b) Online Testing: The online testing phases for SAC channel estimation are shown in Fig. 2b. During the testing phase, only the generator network is used, with no access to the discriminator network. The generator, having been trained to generate accurate channel estimates, is now applied to the testing data to predict the channel matrices. The testing dataset, $\dot { \mathcal { R } } ^ { \mathrm { B S } }$ and $\dot { \mathcal { R } } ^ { \mathrm { U E } _ { k } }$ , first undergoes preprocessing to standardize the samples according to (19), denoted by $\bar { \mathbf { R } } ^ { \mathrm { B \bar { S } } }$ and $\bar { \mathbf { R } } ^ { \mathrm { U E } _ { k } }$ , and then is fed to the generator network. The estimated output is

represented as

$$
\hat {\mathbf {A}} = \rho^ {- 1} G (\bar {\mathbf {R}} ^ {\mathrm{BS}}; \hat {\boldsymbol {\Lambda}})
$$

$$
\hat {\mathbf {G}} _ {k} = \rho^ {- 1} G (\bar {\mathbf {R}} ^ {\mathrm{UE} _ {k}}; \hat {\boldsymbol {\Lambda}}), \tag {25}
$$

where $\hat { \Lambda }$ represents the hyperparameters of the trained CGAN network (i.e., SE-CGAN or CE-CGAN). The output of the generator is scaled by a factor of $\rho ^ { - 1 }$ to obtain the channel matrices, Aˆ and $\hat { \mathbf { G } } _ { k }$ . The proposed CGAN-based channel estimation algorithm is detailed in Algorithm 1, where $\Lambda _ { g }$ and $\Lambda _ { d }$ denote the generator and discriminator parameters, respectively.

Algorithm 1 Training a CGAN   
1 Initialize the generator G and discriminator D with random weights, batch size b, learning rates, and training epochs $\epsilon$ ;
2 Generate ( $R^{UE_{k}}$ , $O^{UE_{k}}$ ) and ( $R^{BS}$ , $O^{BS}$ ) according to Sec. III-B.1.b;
3 Pre-process ( $R^{UE_{k}}$ , $O^{UE_{k}}$ ) and ( $R^{BS}$ , $O^{BS}$ );
4 for epoch i = 1 to $\epsilon$ do
5    for batch j = 1 to B do
6    Sample batch of samples from $R^{UE_{k}}$ or $R^{BS}$ ;
7    Sample batch of samples from $O^{UE_{k}}$ or $O^{BS}$ ;
8    Generate samples from the generator $G(\mathbf{R}^{\mathrm{UE}_{k}})$ or $G(\mathbf{R}^{\mathrm{UE}_{k}})$ ;
9    Evaluate generated samples $D(G(\mathbf{R}^{\mathrm{UE}_{k}}))$ or $D(G(\mathbf{R}^{\mathrm{UE}_{k}}))$ ;
10    Evaluate target samples $D(\mathbf{O}^{\mathrm{UE}_{k}})$ or $D(\mathbf{O}^{\mathrm{BS}})$ ;
11    Update D by ascending its stochastic gradient: $\nabla_{\Lambda_{d}}\frac{1}{b}\sum_{j=1}^{b}\left[\log\left(D\left(\mathbf{A}^{j},\mathbf{G}_{k}^{j}\right)\right)\right]+\log\left(1-D\left(G\left(\mathbf{R}_{j}^{\mathrm{BS}}\right),G\left(\mathbf{R}_{j}^{\mathrm{UE}_{k}}\right)\right)\right)\right]$ (26)
12    Update G by descending its stochastic gradient: $\nabla_{\Lambda_{g}}\frac{1}{b}\sum_{j=1}^{b}\left[\log\left(1-D\left(G\left(\mathbf{R}_{j}^{\mathrm{BS}}\right),G\left(\mathbf{R}_{j}^{\mathrm{UE}_{k}}\right)\right)\right)+\alpha L_{2}\right]$ 13    end
14 end
15 Output the trained SE-CGAN, $G(\bar{\mathbf{R}}^{\mathrm{BS}};\hat{\Lambda}_{g})$ , at the ISAC BS and the trained CE-CGAN, $G(\bar{\mathbf{R}}^{\mathrm{UE}_{k}};\hat{\Lambda}_{g})$ , at the downlink $UE_{k}$ .

# IV. COMPLEXITY ANALYSIS

Based on the proposed SE-CGAN and CE-CGAN channel estimation frameworks, this section derives the computational complexity required by the trained CGAN-based framework to estimate the SAC channel. The computational complexity is computed in terms of the number of real additions, $C _ { A } ,$ and multiplications, $C _ { \mathcal { M } }$ . To provide a comprehensive analysis, we first consider the operations involved in the generator and discriminator networks of the proposed SE-CGAN. Both networks consist of several FFL, each contributing to the overall computational load. In particular, the proposed SE-CGAN contains two hidden FFL and an input and output layers. Let ηi be the number of neurons of the i-th layer. Therefore, according to the parameters presented in Table I, the computational complexity introduced by the first FFL is $\eta _ { 2 } ^ { \mathrm { S E } } ( \eta _ { 1 } ^ { \mathrm { S E } } + 1 )$ real

additions and $\eta _ { 1 } ^ { \mathrm { S E } } \eta _ { 2 } ^ { \mathrm { S E } }$ real multiplications. Similarly, the rest of the FFLs have the complexity corresponding to the number of neurons. To this end, the required number of additions and multiplications required by the generator and discriminator networks of SE-CGAN are respectively given as

$$
C _ {\mathcal {A} _ {G}} ^ {\mathrm{SE}} = \sum_ {i = 1} ^ {3} \eta_ {i} ^ {\mathrm{SE}} \eta_ {i + 1} ^ {\mathrm{SE}} + \sum_ {i = 1} ^ {3} \eta_ {i + 1} ^ {\mathrm{SE}}, \tag {28}
$$

$$
C _ {\mathcal {M} _ {G}} ^ {\mathrm{SE}} = \sum_ {i = 1} ^ {3} \eta_ {i} ^ {\mathrm{SE}} \eta_ {i + 1} ^ {\mathrm{SE}}, \tag {29}
$$

and

$$
C _ {\mathcal {A} _ {D}} ^ {\mathrm{SE}} = \sum_ {i = 1} ^ {2} \eta_ {i} ^ {\mathrm{SE}} \eta_ {i + 1} ^ {\mathrm{SE}} + \sum_ {i = 1} ^ {2} \eta_ {i + 1} ^ {\mathrm{SE}} + (\eta_ {3} ^ {\mathrm{SE}} + 1), \tag {30}
$$

$$
C _ {\mathcal {M} _ {D}} ^ {\mathrm{SE}} = \sum_ {i = 1} ^ {2} \eta_ {i} ^ {\mathrm{SE}} \eta_ {i + 1} ^ {\mathrm{SE}} + \eta_ {3} ^ {\mathrm{SE}}. \tag {31}
$$

To this end, the overall necessary number of real additions and multiplications of the proposed SE-CGAN is represented as

$$
C _ {\mathcal {A}} ^ {\mathrm{SE}} = 2 \eta_ {1} ^ {\mathrm{SE}} \eta_ {2} ^ {\mathrm{SE}} + \sum_ {i = 2} ^ {3} k _ {i} \eta_ {i} ^ {\mathrm{SE}} + \eta_ {4 G} ^ {\mathrm{SE}} + 1, \tag {32}
$$

$$
C _ {\mathcal {M}} ^ {\mathrm{SE}} = \sum_ {i = 1} ^ {2} 2 \eta_ {i} ^ {\mathrm{SE}} \eta_ {i + 1} ^ {\mathrm{SE}} + \eta_ {3} ^ {\mathrm{SE}} (\eta_ {4 _ {G}} ^ {\mathrm{SE}} + 1). \tag {33}
$$

where $k _ { 2 } = 2 ( \eta _ { 3 } ^ { \mathrm { S E } } + 1 )$ and $k _ { 3 } = 3 + \eta _ { 4 _ { G } } ^ { \mathrm { S E } } .$

On the other hand, the CE-CGAN network contains a CL, FFL, input and output layers. Similarly, the computational complexity contributions arise from both generator and discriminator networks. To this end, by summing up the contributions from all layers in both the generator and discriminator networks, the total computational complexity of the proposed CE-CGAN framework can be obtained. Let $F _ { z }$ be the filter size, $F _ { n }$ be the number of filters, and $F _ { s }$ be the stride. The output size of a CL is given by

$$
\eta_ {F} = \left\lfloor \frac {\eta_ {1} ^ {\mathrm{CE}} - F _ {z}}{F _ {s}} + 1 \right\rfloor , \tag {34}
$$

where ⌊·⌋ is the floor operation. The computational complexity is introduced by the second, third, and fourth layers, since the flatten layer does not contain any addition or multiplication complexity. The number of required additions is presented as $( F _ { z } + 1 ) \bar { \eta _ { F } } F _ { n } , \eta _ { 3 } ^ { \mathrm { C E } } ( \eta _ { F } F _ { n } + 1 )$ and $( \eta _ { 4 } ^ { \mathrm { C E } } + 1 ) \eta _ { 3 } ^ { \mathrm { C E } }$ , respectively, while the number of required multiplications is presented as $F _ { z } \eta _ { F } F _ { n } , \eta _ { 3 } ^ { \mathrm { C E } } \eta _ { F } F _ { n }$ , and $\dot { \eta } _ { 3 } ^ { \mathrm { C E } } \eta _ { 4 } ^ { \mathrm { C E } }$ , respectively. To this end, the required number of additions and multiplications required by the generator and discriminator networks of CE-CGAN are respectively given as

$$
C _ {\mathcal {A} _ {G}} ^ {\mathrm{CE}} = (F _ {z} + \eta_ {3} ^ {\mathrm{CE}} + 1) \eta_ {F} F _ {n} + (\eta_ {4 _ {G}} ^ {\mathrm{CE}} + 1) \eta_ {3} ^ {\mathrm{CE}} + \eta_ {4 _ {G}} ^ {\mathrm{CE}}, \tag {35}
$$

$$
C _ {\mathcal {M} _ {G}} ^ {\mathrm{CE}} = \left(F _ {z} + \eta_ {3} ^ {\mathrm{CE}}\right) \eta_ {F} F _ {n} + \eta_ {3} ^ {\mathrm{CE}} \eta_ {4 _ {G}} ^ {\mathrm{CE}}, \tag {36}
$$

and

$$
C _ {\mathcal {A} _ {D}} ^ {\mathrm{CE}} = (F _ {z} + \eta_ {3} ^ {\mathrm{CE}} + 1) \eta_ {F} F _ {n} + 2 \eta_ {3} ^ {\mathrm{CE}} + 1, \tag {37}
$$

$$
C _ {\mathcal {M} _ {D}} ^ {\mathrm{CE}} = (F _ {z} + \eta_ {3} ^ {\mathrm{CE}}) \eta_ {F} F _ {n} + \eta_ {3} ^ {\mathrm{CE}}. \tag {38}
$$

Consequently, the total computational complexity of the CE-CGAN framework is expressed as

$$
C _ {\mathcal {A}} ^ {\mathrm{CE}} = 2 \left(F _ {z} + \eta_ {3} ^ {\mathrm{CE}} + 1\right) \eta_ {F} F _ {n} + \eta_ {4 _ {G}} ^ {\mathrm{CE}} \left(\eta_ {3} ^ {\mathrm{CE}} + 1\right) + 3 \eta_ {3} ^ {\mathrm{CE}} + 1, \tag {39}
$$

$$
C _ {\mathcal {M}} ^ {\mathrm{CE}} = 2 (F _ {z} + \eta_ {3} ^ {\mathrm{CE}}) \eta_ {F} F _ {n} + \eta_ {3} ^ {\mathrm{CE}} (\eta_ {4 _ {G}} ^ {\mathrm{CE}} + 1). \tag {40}
$$

To this end, the total number of additions and multiplications required by the proposed CGAN framework is $C _ { A } ^ { \mathrm { S E } } + C _ { A } ^ { \mathrm { C E } }$ and CSE $C _ { \mathcal { M } } ^ { \mathrm { S E } } + C _ { \mathcal { M } } ^ { \mathrm { C E } }$ M , respectively. In particular, the number of additions and multiplications is respectively given as in (41) and (42), as shown at the bottom of the page.

# V. SIMULATION RESULTS

This section extensively validates the performance of the proposed CGAN channel estimation framework for the RIS-assisted ISAC system. First, the simulation parameters and setup are presented. Then, the SAC channel estimation performance is evaluated under different SNR values and system conditions.

# A. Simulation Parameters

Let $K = 3 , M = 4 ,$ and $N = 3 0$ for all the following simulations, unless further specified. The sensing channel is modeled according to the radar channel model as [43], [44]

$$
\mathbf {A} = \mu \mathbf {a} (\theta) \mathbf {a} (\theta) ^ {H}. \tag {43}
$$

Here, $\mu$ denotes the complex-valued reflection coefficient associated with the target with phase shifts uniformly distributed from [0, 2π), and ${ \bf a } ( \theta )$ is the steering vector, expressed as

$$
\mathbf {a} (\theta) = \left[ 1, e ^ {j \frac {2 \pi d}{\lambda} \sin (\theta)}, \dots , e ^ {j \frac {2 \pi d (M - 1)}{\lambda} \sin (\theta)} \right] ^ {T}, \tag {44}
$$

where $\begin{array} { l l l } { { \theta } } & { { = } } & { { - { \frac { 2 \pi } { 3 } } , } } \end{array} d ,$ − 2π3 , d, and λ denote the azimuth angle, BS antenna spacing, and signal wavelength, respectively. On the other hand, the communication channels (i.e., H and $\mathbf { r } _ { k } )$ are modeled as Rician, being expressed as

$$
\mathbf {h} = \sqrt {\mathrm{PL}} \left(\frac {K _ {1}}{K _ {1} + 1} \bar {\mathbf {h}} + \frac {1}{K _ {1} + 1} \tilde {\mathbf {h}}\right), \tag {45}
$$

where h represents the channels (i.e., $\textbf { h } = \{ \mathbf { H } , \mathbf { r } _ { k } \} )$ , PL denotes the path loss, and $K _ { 1 }$ is the Rician factor. h¯ and h˜ are the line-of-sight and non-line-of-sight components of the channel, respectively. Here, $\bar { { \textbf { h } } } = { \textbf { a } } ( \bar { \theta } ) { \textbf { a } } ( \bar { \theta } ) ^ { H }$ , where $\mathbf { a } ( \dot { \theta } )$ corresponds to the angle of departure from the source to destination (i.e., BS to RIS/RIS to $\mathrm { U E } _ { k } )$ and $\mathbf { a } ( \bar { \theta } )$ corresponds to the angle of arrival $\left( \mathrm { i . e . , ~ \mathsf { R I S / U E } } _ { k } \right)$ and are set to ${ \frac { \pi } { 3 } } .$ h¯ is formulated similar to (44), whereas h˜ is the random component containing independent and identical distributed $\mathcal { C N } ( 0 , 1 )$ elements. The Rician factor, $K _ { 1 }$ is set to 10 and 0 (i.e., representing a Rayleigh fading model) for H and $\mathbf { r } _ { k } .$ , respectively [27]. Furthermore, the PL is modeled as PL = $\begin{array} { r } { \mathrm { P L } _ { r } \big ( \frac { d _ { j } } { d _ { r } } \big ) ^ { - \zeta _ { j } } . ~ d _ { j } } \end{array}$ is the distance, $\mathrm { P L } _ { r }$ is the path loss at a reference distance $d _ { r } ,$ , and $\zeta _ { j }$ is the path loss exponent. We set $P L _ { r } = - 3 0 \mathrm { d B m }$ and $d _ { r } \ = 1 \mathrm { m }$ . The path loss exponents of the BS-target-BS, BS-RIS, and ${ \mathrm { R I S - U E } } _ { k }$ links are $\zeta _ { 1 } = 3 ,$ $\zeta _ { 2 } = 2 . 3$ , and $\zeta _ { 3 } = 2 ,$ respectively, while the distances are set as $d _ { 1 } = 1 4 0 \mathrm { m } , d _ { 2 } = 5 0 \mathrm { m }$ , and $d _ { 3 } = 2 \mathrm { m }$ . According to [20] and [45], the transmit power of the ISAC BS and is set to $P = - 2 0 \mathrm { d B m }$ .

The dataset size is $Q \times V = 1 0 ^ { 4 }$ for each SNR value, with $Q \ = \ 1 0 0 0$ and $V \ = \ 1 0 .$ . In this work, 90% of the dataset size is used for training, while the remaining 10% is used for testing. The SNR values in the training stage are $\mathrm { S N R \ = \ 1 0 : \ 5 : 2 0 d B }$ , whereas the testing stage uses $\mathrm { S N R \ = \ - 1 0 : 2 . 5 : 3 0 d B }$ , which includes 17 values from −10 dB to 30 dB with a step increment of 2.5 dB. The choice of the SNR region ensures that the model encounters instances from unfamiliar conditions, not only unseen samples. This way, the simulation results confirm the generalization of the model and eliminate the need of estimating the SNR prior to estimating the desired channels. Lastly, the scaling factor, $\rho ,$ is set to $1 0 ^ { 4 }$ .

To validate the performance of the proposed CGAN channel estimation approach, the normalized mean square error (NMSE) is considered as the main performance metric being expressed as

$$
\mathrm{NMSE} = \mathbb {E} \left\{\frac {\left\| \mathbf {h} _ {\text { Estimated }} - \mathbf {h} _ {\text { True }} \right\| _ {F} ^ {2}}{\left\| \mathbf {h} _ {\text { True }} \right\| _ {F} ^ {2}} \right\}. \tag {46}
$$

Furthermore, the work in [20] is considered as a benchmark to effectively evaluate the performance of the proposed algorithm in the following subsections.

# B. Impact of Varying the SNR

Fig. 3 shows the estimation performance under different SNR conditions. The NMSEs of the proposed CE-CGAN and SE-CGAN demonstrate a considerable improvement compared to the benchmark estimation approach presented in [20] as well as other traditional models, including a FF network (FFN) and ELM. It is worth noting that the FFN model consists of two hidden layers, each containing 256 neurons, with hyperparameters aligned with the benchmark in [20]. The ELM model, on the other hand, consists of one hidden layer of 256 neurons to estimate both channels. These specifications ensure a fair comparison across all approaches. For the proposed SE-CGAN, this improvement is especially notable at lower SNR levels, where the proposed approach demonstrates

$$
C _ {\mathcal {A}} ^ {\text { Total }} = 2 \eta_ {1} ^ {\mathrm{SE}} \eta_ {2} ^ {\mathrm{SE}} + \sum_ {i = 2} ^ {3} k _ {i} \eta_ {i} ^ {\mathrm{SE}} + \eta_ {4 _ {G}} ^ {\mathrm{SE}} + 1 + 2 (F _ {z} + \eta_ {3} ^ {\mathrm{CE}} + 1) \eta_ {F} F _ {n} + \eta_ {4 _ {G}} ^ {\mathrm{CE}} (\eta_ {3} ^ {\mathrm{CE}} + 1) + 3 \eta_ {3} ^ {\mathrm{CE}} + 1, \tag {41}
$$

$$
C _ {\mathcal {M}} ^ {\text { Total }} = \sum_ {i = 1} ^ {2} 2 \eta_ {i} ^ {\mathrm{SE}} \eta_ {i + 1} ^ {\mathrm{SE}} + \eta_ {3} ^ {\mathrm{SE}} \left(\eta_ {4 _ {G}} ^ {\mathrm{SE}} + 1\right) + 2 \left(F _ {z} + \eta_ {3} ^ {\mathrm{CE}}\right) \eta_ {F} F _ {n} + \eta_ {3} ^ {\mathrm{CE}} \left(\eta_ {4 _ {G}} ^ {\mathrm{CE}} + 1\right). \tag {42}
$$

![](images/d74f595634023e7ef317abc17c51d0372c455b020dbb5f2e67ef202f5eaf3c9b.jpg)

<details>
<summary>line</summary>

| SNR | G_k - ELM | G_k - FFN | G_k - Benchmark [20] | G_k - Proposed CE-CGAN | A - ELM | A - FFN | A - Benchmark [20] | A - Proposed SE-CGAN |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -10 | ~1.0 | ~1.0 | ~1.0 | ~0.01 | ~1.0 | ~1.0 | ~1.0 | ~0.01 |
| -5 | ~0.8 | ~0.8 | ~0.8 | ~0.005 | ~0.8 | ~0.8 | ~0.8 | ~0.005 |
| 0 | ~0.6 | ~0.6 | ~0.6 | ~0.002 | ~0.6 | ~0.6 | ~0.6 | ~0.002 |
| 5 | ~0.4 | ~0.4 | ~0.4 | ~0.001 | ~0.4 | ~0.4 | ~0.4 | ~0.001 |
| 10 | ~0.3 | ~0.3 | ~0.3 | ~0.0005 | ~0.3 | ~0.3 | ~0.3 | ~0.0005 |
| 15 | ~0.25 | ~0.25 | ~0.25 | ~0.00025 | ~0.25 | ~0.25 | ~0.25 | ~0.00025 |
| 20 | ~0.2 | ~0.2 | ~0.2 | ~0.000125 | ~0.2 | ~0.2 | ~0.2 | ~0.000125 |
| 25 | ~0.15 | ~0.15 | ~0.15 | ~0.0000625 | ~0.15 | ~0.15 | ~0.15 | ~0.0000625 |
| 30 | ~0.125 | ~0.125 | ~0.125 | ~0.00003125 | ~0.125 | ~0.125 | ~0.125 | ~0.00003125 |
</details>

Fig. 3. NMSE performance for estimating SAC channels.

good noise resilience, thus achieving lower NMSE values. This is one of the CGAN advantages, where the generator learns to create samples, not to map input data to an output. It generates data conditioned by the input sample but based on the loss function design, thereby reducing the noise impact. Furthermore, as the communication channel estimation is considered more complicated due to the cascaded relationship in (11), one can observe that the achieved NMSE is higher than that of the sensing link. However, overall, the proposed scheme outperforms the benchmark scheme and the additional traditional models substantially. In particular, the proposed approach achieves around 8 dB SNR improvement at $\mathrm { { N M S E } = 1 0 ^ { - 2 } }$ and $\mathrm { \Delta N M S E } = \mathrm { 1 0 ^ { - 1 } }$ as compared to [20] for estimating A and $\mathbf { G } _ { k }$ , respectively. The figure also highlights the generalization performance of the proposed CGAN approach, where it outperforms the benchmark schemes even at SNR ranges that were excluded in the training process (i.e., SNR = −10: 5 dB).

# C. Impact of Varying M

Fig. 4 analyzes the performance of the proposed approach in estimating the communication channel, $\mathbf { G } _ { k } .$ , with respect to varying M under different SNR conditions: low (i.e., −5 dB) and high (i.e., 10 dB) SNR values. As illustrated, the proposed CGAN consistently outperforms the benchmark scheme across all M values and SNR conditions, demonstrating superior channel estimation accuracy. The CGAN robustness in handling higher dimensions can be attributed to its ability to better model complex channel conditions and effectively learn from the discriminator feedback, even for larger sets of training data. Furthermore, the decrease in the NMSE as M increases at SNR = −5 dB indicates that the proposed framework is capable of leveraging the additional information present in the received signals to refine its estimation. This robustness stems from the ability of CGANs to capture and model the inherent spatial correlations in the communication channel. By leveraging its generation mechanism, the CGAN framework enables more effective utilization of the additional spatial diversity introduced as M increases. This results in enhanced noise suppression at low SNR values. This is a particularly useful feature for ISAC systems (i.e., where lower SNR values are adopted). At SNR = 10 dB, where the noise level is relatively low, the primary challenge of the proposed CGAN shifts from combating noise to accurately capturing the high-dimensional channel details. The generator network may face difficulties in fully capturing the high-dimensional dependencies, which results in a gradual increase in estimation error, especially that the overall network architecture and hyperparameters are optimized at lower channel dimensions (i.e., M = 4 and N = 30). This slight degradation at higher SNR can be attributed to increased sensitivity to minor inaccuracies in capturing subtle channel characteristics. Despite this, the NMSE increase remains minimal, demonstrating the CGAN’s effectiveness in maintaining reliable performance. Moreover, the proposed approach consistently outperforms the previous work, showcasing its adaptability and robustness across diverse real-world conditions.

![](images/09305eaa0f33df426b9eb235f0a95d278101f68f9c20a476c0843824a5f26224.jpg)

<details>
<summary>line</summary>

| M   | Gk - Proposed CE-CGAN | Gk - Benchmark [20] |
| --- | --------------------- | ------------------- |
| 4   | 0.01                  | 0.1                 |
| 8   | 0.02                  | 0.1                 |
| 12  | 0.03                  | 0.1                 |
| 16  | 0.04                  | 0.1                 |
</details>

Fig. 4. NMSE performance for the communication channel estimation versus M at N = 30.

![](images/9961310cbe06d2971015f1a60722e2458f0d0df74cbd96d5333e9994c9d61349.jpg)

<details>
<summary>line</summary>

| M   | A - Proposed SE-CGAN | A - Benchmark [20] |
| --- | -------------------- | ------------------ |
| 4   | 0.01                 | 0.1                |
| 8   | 0.003                | 0.03               |
| 12  | 0.001                | 0.01               |
| 16  | 0.0005               | 0.005              |
</details>

Fig. 5. NMSE performance for the sensing channel estimation versus M at $N = 3 0$ .

![](images/e81ab5795925efe49d754597da0635fc38e95f3c5050f197e3bf1e2dc203163f.jpg)

<details>
<summary>line</summary>

| N   | Gk - Proposed CE-CGAN | Gk - Benchmark [20] |
|-----|------------------------|---------------------|
| 20  | ~0.1                   | ~0.1                |
| 30  | ~0.1                   | ~0.1                |
| 40  | ~0.1                   | ~0.1                |
| 50  | ~0.1                   | ~0.1                |
</details>

Fig. 6. NMSE performance for the communication channel estimation versus N at M = 4.

Fig. 5 demonstrates the performance of the proposed approach in estimating the sensing channel, A, with respect to varying M under the same SNR conditions considered in Fig. 4. It can be seen that the proposed SE-CGAN algorithm significantly outperforms the benchmark in [20] at both SNR levels, evidencing its enhanced ability to estimate sensing channels under different channel dimension and noise conditions. At the SNR of −5 dB, the NMSE of both models decreases, yet the proposed SE-CGAN maintains a stable performance enhancements, showcasing its robustness against high noise levels. The consistent performance across increasing M values suggests that the proposed SE-CGAN effectively utilizes additional antennas to mitigate noise through its adaptive learning and channel modeling capabilities. On the other hand, at the SNR of 10 dB, although the NMSE for the benchmark model decreases with higher M, the proposed algorithm still holds a significant advantage. In particular, it begins with an outperforming estimation for smaller number of antennas, demonstrating robust performance right from the onset. The performance of the proposed approach saturates as M increases, which proves its scalability and capability to handle high-dimensional channel environments without substantial loss in performance. At $M \ = \ 1 6$ , both models converge to similar levels of NMSE, illustrating that while the benchmark in [20] improves, the proposed SE-CGAN effectively sustains its superior channel estimation capabilities across varying antenna configurations. This balance of initial superiority and scalability at high SNR settings emphasizes the proposed SE-CGAN advantage in complex RIS-assisted ISAC systems where both accuracy and adaptability are crucial.

# D. Impact of Varying N

Fig. 6 demonstrates the performance of the proposed approach in estimating the communication channel, $\mathbf { G } _ { k } .$ , with respect to varying N under the same SNR conditions considered throughout the simulations. Similarly, the proposed CGAN algorithm effectively outperforms the benchmark scheme in [20] across all N values and SNR conditions. At lower SNR (i.e., SNR = −5 dB), the proposed algorithm demonstrates a substantial improvement over the benchmark, with the NMSE slightly decreasing as N increases. This significant reduction emphasizes the CGAN robustness in noisy environments, effectively leveraging the increased number of RIS elements to enhance channel estimation. Alternatively, at higher SNR (i.e., SNR = 10 dB), although the CGAN continues to outperform the benchmark, the performance improvement decreases, indicating less gains from additional RIS elements. However, it is worth noting that the NMSE remains relatively stable even with increasing N, reflecting the CGAN ability to maintain its estimation accuracy across larger RIS setups. The slight increase in NMSE at higher SNR is marginal and does not significantly impact the estimation performance. It is also important to note that the model was optimized for a baseline configuration (i.e., M = 4 and $N = 3 0 )$ , which explains the observed behavior when scaling beyond these dimensions. Overall, the performance proves the CGAN scalability to larger configurations and shows the CGAN proficiency in utilizing the spatial diversity offered by larger RIS setups to optimize channel estimation, making it particularly useful for ISAC systems operating across a range of SNR scenarios.

# E. Complexity Evaluation

Figs. 7a and 7b show the computational complexity of the proposed CGAN approach as compared to the benchmark scheme presented in [20]. The complexity is analyzed in terms of the required number of real additions and multiplications according to the derived formulations in Section IV. Furthermore, the figures show the complexity reduction of using the proposed CGAN algorithm over the benchmark scheme, which is expressed as

$$
\text { Reduction } = \frac {C _ {\chi} ^ {[ 2 0 ]} - C _ {\chi} ^ {\xi}}{C _ {\chi} ^ {[ 2 0 ]}}, \chi \in \{\mathcal {A}, \mathcal {M} \}, \xi \in \{\mathrm{SE}, \mathrm{CE} \}. \tag {47}
$$

Fig. 7a illustrates the computational complexity and reduction percentage of estimating the direct channel (i.e., A) as M increases. As can be seen, the complexities of additions and multiplications for both the proposed and benchmark schemes show a trend of increasing with M. However, the proposed algorithm complexity is notably lower compared to the benchmark method. The reduction in complexity, depicted on the secondary (i.e., right) y-axis, emphasizes the efficiency gains from the proposed approach as M increases. The proposed SE-CGAN approach not only significantly reduces the computational complexity compared to the benchmark, enhancing system efficiency, but also delivers a superior performance across various conditions, making it an exceptionally effective solution for ISAC RIS-assisted systems.

Fig. 7b illustrates the computational complexity and reduction percentage of estimating the communication channel $( \mathrm { i } . \mathrm { e } . , \mathbf { G } _ { k } )$ as $N$ increases. Similarly, the number of additions and multiplications for both the proposed and benchmark schemes rapidly increase as N increases. The computational complexity of the proposed CE-CGAN approach is comparable to the benchmark scheme, even when the channel estimation dimension enlarges. This is due to the fact that estimating the communication channel is challenging and often require complex models. Despite the inherent challenges, our approach achieves a similar level of computational complexity to the benchmark, while significantly outperforming it in terms of performance. This proves the effectiveness of our model in handling the delicate features of cascaded communication channels estimation within RIS-assisted ISAC systems, ensuring practicality and timeliness in real-world deployments.

![](images/fbb3a35aded2c922757f441ac8a5f1e0eb73a3525949649a9575b102e7b5d1c1.jpg)

<details>
<summary>line</summary>

| M   | CA - Proposed | CM - Proposed | CA - Benchmark [20] | CM - Benchmark [20] | CM - Reduction | CA - Reduction |
| --- | ------------- | ------------- | ------------------- | ------------------- | -------------- | -------------- |
| 4   | 0.5           | 0.5           | 0.8                 | 0.8                 | 3.3            | 3.3            |
| 8   | 0.9           | 0.9           | 1.3                 | 1.3                 | 2.0            | 2.0            |
| 12  | 1.6           | 1.6           | 2.1                 | 2.1                 | 1.2            | 1.2            |
| 16  | 2.5           | 2.5           | 3.3                 | 3.3                 | 0.7            | 0.7            |
</details>

(a)

![](images/00e73d05e79c9b8d062c76c41fae7ae21661eb8ce7d62045813b9c8f5aa54512.jpg)

<details>
<summary>line</summary>

| N   | CA - Proposed | CM - Proposed | CA - Benchmark [20] | CM - Benchmark [20] | CM - Reduction | CA - Reduction |
| --- | ------------- | ------------- | ------------------- | ------------------- | -------------- | -------------- |
| 20  | 2.0           | 2.0           | 2.0                 | 2.0                 | 2.0            | 4.0            |
| 30  | 3.5           | 3.5           | 3.5                 | 3.5                 | 3.5            | 7.0            |
| 40  | 5.0           | 5.0           | 5.0                 | 5.0                 | 5.0            | 8.5            |
| 50  | 6.5           | 6.5           | 6.5                 | 6.5                 | 6.5            | 9.5            |
| 60  | 8.0           | 8.0           | 8.0                 | 8.0                 | 8.0            | 10.0           |
| 70  | 9.5           | 9.5           | 9.5                 | 9.5                 | 9.5            | 10.5           |
| 80  | 11.0          | 11.0          | 11.0                | 11.0                | 11.0           | 11.0           |
| 90  | 11.5          | 11.5          | 11.5                | 11.5                | 11.5           | 11.5           |
| 100 | 12.0          | 12.0          | 12.0                | 12.0                | 12.0           | 12.0           |
</details>

Fig. 7. Computational complexity evaluation. (a) Sensing link, (b) Communication link.

# VI. CONCLUSION

This paper has investigated the channel estimation problem of an RIS-assisted ISAC system. A novel CGAN approach has been proposed to enhance the estimation accuracy and stability. The proposed method has leveraged the adversarial training of two deep learning networks to accurately estimate the channel coefficients, demonstrating a superior performance over conventional techniques. The numerical results have validated the efficiency of the proposed approach across different SNR conditions and system dimensions, highlighting its robustness and adaptability. Furthermore, the complexity of the proposed approach has been analyzed and compared to that of the benchmark scheme. In particular, the proposed CE-CGAN model maintains a computational complexity comparable to that of existing DL methods while achieving a better estimation accuracy, while the SE-CGAN model outperforms the existing estimation model in both performance and computational complexity. This makes the proposed CGAN a promising solution for enhancing the reliability and efficiency of RIS-assisted ISAC systems. Future works could explore extensions of the proposed CGAN-based channel estimation approach to address further practical challenges. Examples include accommodating multi-target scenarios along with mobility of users and targets, and adapting the framework for wideband system deployments.

# REFERENCES

[1] A. Fayad, T. Cinkler, and J. Rak, “Toward 6G optical fronthaul: A survey on enabling technologies and research perspectives,” IEEE Commun. Surveys Tuts., early access, Jun. 3, 2024, doi: 10.1109/COMST.2024.3408090.   
[2] Z. Wang, Y. Zhao, Y. Zhou, Y. Shi, C. Jiang, and K. B. Letaief, “Over-the-air computation for 6G: Foundations, technologies, and applications,” IEEE Internet Things J., vol. 11, no. 14, pp. 24634–24658, Jul. 2024.   
[3] C. B. Barneto, S. D. Liyanaarachchi, M. Heino, T. Riihonen, and M. Valkama, “Full duplex radio/radar technology: The enabler for advanced joint communication and sensing,” IEEE Wireless Commun., vol. 28, no. 1, pp. 82–88, Feb. 2021.   
[4] F. Bozorgi, P. Sen, A. N. Barreto, and G. Fettweis, “RF front-end challenges for joint communication and radar sensing,” in Proc. 1st IEEE Int. Online Symp. Joint Commun. Sens. (JC&S), Dresden, Germany, Feb. 2021, pp. 1–6.   
[5] L. Han and K. Wu, “Multifunctional transceiver for future intelligent transportation systems,” IEEE Trans. Microw. Theory Techn., vol. 59, no. 7, pp. 1879–1892, Jul. 2011.   
[6] N. Su, F. Liu, and C. Masouros, “Secure radar-communication systems with malicious targets: Integrating radar, communications and jamming functionalities,” IEEE Trans. Wireless Commun., vol. 20, no. 1, pp. 83–95, Jan. 2021.   
[7] F. Dong, F. Liu, Y. Cui, W. Wang, K. Han, and Z. Wang, “Sensing as a service in 6G perceptive networks: A unified framework for ISAC resource allocation,” IEEE Trans. Wireless Commun., vol. 22, no. 5, pp. 3522–3536, May 2023.   
[8] B. Zhao, M. Wang, Z. Xing, G. Ren, and J. Su, “Integrated sensing and communication aided dynamic resource allocation for random access in satellite terrestrial relay networks,” IEEE Commun. Lett., vol. 27, no. 2, pp. 661–665, Feb. 2023.   
[9] Z. He, W. Xu, H. Shen, D. W. K. Ng, Y. C. Eldar, and X. You, “Fullduplex communication for ISAC: Joint beamforming and power optimization,” IEEE J. Sel. Areas Commun., vol. 41, no. 9, pp. 2920–2936, Sep. 2023.   
[10] Q. N. Le, V.-D. Nguyen, O. A. Dobre, and H. Shin, “RIS-assisted fullduplex integrated sensing and communication,” IEEE Wireless Commun. Lett., vol. 12, no. 10, pp. 1677–1681, Oct. 2023.   
[11] H. Li, S. Shen, M. Nerini, and B. Clerckx, “Reconfigurable intelligent surfaces 2.0: Beyond diagonal phase shift matrices,” IEEE Commun. Mag., vol. 62, no. 3, pp. 102–108, Mar. 2024.   
[12] J. Chu, Z. Lu, R. Liu, M. Li, and Q. Liu, “Joint beamforming and reflection design for secure RIS-ISAC systems,” IEEE Trans. Veh. Technol., vol. 73, no. 3, pp. 4471–4475, Mar. 2024.   
[13] Q. Zhu, M. Li, R. Liu, and Q. Liu, “Cramér–Rao bound optimization for active RIS-empowered ISAC systems,” IEEE Trans. Wireless Commun., vol. 23, no. 9, pp. 11723–11736, Sep. 2024, doi: 10.1109/TWC.2024.3384501.   
[14] K. Chen, C. Qi, O. A. Dobre, and G. Y. Li, “Simultaneous beam training and target sensing in ISAC systems with RIS,” IEEE Trans. Wireless Commun., vol. 23, no. 4, pp. 2696–2710, Apr. 2024.   
[15] Z. Liu, Y. Liu, S. Shen, Q. Wu, and Q. Shi, “Enhancing ISAC network throughput using beyond diagonal RIS,” IEEE Wireless Commun. Lett., vol. 13, no. 6, pp. 1670–1674, Jun. 2024.   
[16] K. Zhong, J. Hu, C. Pan, M. Deng, and J. Fang, “Joint waveform and beamforming design for RIS-aided ISAC systems,” IEEE Signal Process. Lett., vol. 30, pp. 165–169, 2023.

[17] J. Ye, L. Huang, Z. Chen, P. Zhang, and M. Rihan, “Unsupervised learning for joint beamforming design in RIS-aided ISAC systems,” IEEE Wireless Commun. Lett., vol. 13, no. 8, pp. 2100–2104, Aug. 2024, doi: 10.1109/LWC.2024.3402235.   
[18] W. Jiang, D. Ma, Z. Wei, Z. Feng, P. Zhang, and J. Peng, “ISAC-NET: Model-driven deep learning for integrated passive sensing and communication,” IEEE Trans. Commun., vol. 72, no. 8, pp. 4692–4707, Aug. 2024, doi: 10.1109/TCOMM.2024.3375818.   
[19] Y. Liu, I. Al-Nahhal, O. A. Dobre, and F. Wang, “Deep-learning channel estimation for IRS-assisted integrated sensing and communication system,” IEEE Trans. Veh. Technol., vol. 72, no. 5, pp. 6181–6193, May 2023.   
[20] Y. Liu, I. Al-Nahhal, O. A. Dobre, and F. Wang, “Deep-learning-based channel estimation for IRS-assisted ISAC system,” in Proc. IEEE Global Commun. Conf. (GLOBECOM), Rio de Janeiro, Brazil, Dec. 2022, pp. 4220–4225.   
[21] Y. Liu, I. Al-Nahhal, O. A. Dobre, F. Wang, and H. Shin, “Extreme learning machine-based channel estimation in IRS-assisted multi-user ISAC system,” IEEE Trans. Commun., vol. 71, no. 12, pp. 6993–7007, Dec. 2023.   
[22] Y. Liu, I. Al-Nahhal, O. A. Dobre, and F. Wang, “Chapter 4 - channel estimation in ISAC-IRS systems using machine learning approaches,” in Integrated Sensing and Communications for Future Wireless Networks, A. Kaushik, Ed., New York, NY, USA: Academic, 2025, ch. 4, pp. 97–125.   
[23] M. Elsayed, A. A. A. El-Banna, O. A. Dobre, W. Shiu, and P. Wang, “Hybrid-layers neural network architectures for modeling the selfinterference in full-duplex systems,” IEEE Trans. Veh. Technol., vol. 71, no. 6, pp. 6291–6307, Jun. 2022.   
[24] M. Elsayed, A. A. A. El-Banna, O. A. Dobre, W. Shiu, and P. Wang, “Full-duplex self-interference cancellation using dual-neurons neural networks,” IEEE Commun. Lett., vol. 26, no. 3, pp. 557–561, Mar. 2022.   
[25] M. Elsayed, A. A. A. El-Banna, O. A. Dobre, W. Shiu, and P. Wang, “Low complexity neural network structures for self-interference cancellation in full-duplex radio,” IEEE Commun. Lett., vol. 25, no. 1, pp. 181–185, Jan. 2021.   
[26] X. Wang, Z. Fei, J. A. Zhang, and J. Xu, “Partially-connected hybrid beamforming design for integrated sensing and communication systems,” IEEE Trans. Commun., vol. 70, no. 10, pp. 6648–6660, Oct. 2022.   
[27] C. Liu, X. Liu, D. W. K. Ng, and J. Yuan, “Deep residual learning for channel estimation in intelligent reflecting surface-assisted multiuser communications,” IEEE Trans. Wireless Commun., vol. 21, no. 2, pp. 898–912, Feb. 2022.   
[28] M. A. ElMossallamy, H. Zhang, L. Song, K. G. Seddik, Z. Han, and G. Y. Li, “Reconfigurable intelligent surfaces for wireless communications: Principles, challenges, and opportunities,” IEEE Trans. Cognit. Commun. Netw., vol. 6, no. 3, pp. 990–1002, Sep. 2020.   
[29] R. A. Horn and C. R. Johnson, Matrix Analysis. Cambridge, U.K.: Cambridge Univ. Press, 1985.   
[30] R. Mai, D. H. N. Nguyen, and T. Le-Ngoc, “Joint MSE-based hybrid precoder and equalizer design for full-duplex massive MIMO systems,” in Proc. IEEE Int. Conf. Commun. (ICC), May 2016, pp. 1–6.   
[31] I. Goodfellow et al., “Generative adversarial nets,” in Proc. Neural Inf. Process. Syst., vol. 27, 2014, pp. 2672–2680.   
[32] J.-Y. Zhu, T. Park, P. Isola, and A. A. Efros, “Unpaired image-to-image translation using cycle-consistent adversarial networks,” in Proc. IEEE Int. Conf. Comput. Vis. (ICCV), Oct. 2017, pp. 2242–2251.   
[33] H. W. Dong, W. Y. Hsiao, L. C. Yang, and Y. H. Yang, “MuseGAN: Multi-track sequential generative adversarial networks for symbolic music generation and accompaniment,” in Proc. 32nd AAAI Conf. Artif. Intell., 2018, pp. 34–41.   
[34] J. Kong, J. Kim, and J. Bae, “HiFi-GAN: Generative adversarial networks for efficient and high fidelity speech synthesis,” in Proc. Neural Inf. Process. Syst., vol. 33. Red Hook, NY, USA: Curran Associates, 2020, pp. 17022–17033.   
[35] X. Wang et al., “ESRGAN: Enhanced super-resolution generative adversarial networks,” in Proc. Comput. Vis.-ECCV Workshops, Munich, Germany, 2018, pp. 63–79.   
[36] C. Zou, F. Yang, J. Song, and Z. Han, “Generative adversarial network for wireless communication: Principle, application, and trends,” IEEE Commun. Mag., vol. 62, no. 5, pp. 58–64, May 2024.   
[37] T. Erpek, Y. E. Sagduyu, and Y. Shi, “Deep learning for launching and mitigating wireless jamming attacks,” IEEE Trans. Cogn. Commun. Netw., vol. 5, no. 1, pp. 2–14, Mar. 2019.

[38] B. Tang, Y. Tu, Z. Zhang, and Y. Lin, “Digital signal modulation classification with data augmentation using generative adversarial nets in cognitive radio networks,” IEEE Access, vol. 6, pp. 15713–15722, 2018.   
[39] Z. Liu, X. Jing, R. Zhang, and J. Mu, “Spectrum sensing based on deep convolutional generative adversarial networks,” in Proc. Int. Wireless Commun. Mobile Comput. (IWCMC), Jun. 2021, pp. 796–801.   
[40] Z. Li, X. Liao, J. Shi, L. Li, and P. Xiao, “MD-GAN-based UAV trajectory and power optimization for cognitive covert communications,” IEEE Internet Things J., vol. 9, no. 12, pp. 10187–10199, Jun. 2022.   
[41] M. Mirza and S. Osindero, “Conditional generative adversarial nets,” 2014, arXiv:1411.1784.   
[42] D. P. Kingma and J. Ba, “Adam: A method for stochastic optimization,” 2014, arXiv:1412.6980.   
[43] F. Liu, C. Masouros, A. P. Petropulu, H. Griffiths, and L. Hanzo, “Joint radar and communication design: Applications, state-of-the-art, and the road ahead,” IEEE Trans. Commun., vol. 68, no. 6, pp. 3834–3862, Jun. 2020.   
[44] H. Zhang, L. Chen, K. Han, Y. Chen, and G. Wei, “Coexistence designs of radar and communication systems in a multi-path scenario,” IEEE Trans. Veh. Technol., vol. 73, no. 3, pp. 3733–3749, Mar. 2024.   
[45] T. Jiang, H. V. Cheng, and W. Yu, “Learning to reflect and to beamform for intelligent reflecting surface with implicit channel estimation,” IEEE J. Sel. Areas Commun., vol. 39, no. 7, pp. 1931–1945, Jul. 2021.

![](images/3ae92424fa7c4309ae92928ab6be2908a271883c4e6343afcdc112e85fb612fb.jpg)

<details>
<summary>natural_image</summary>

Portrait of a woman with dark wavy hair wearing a beige blazer and necklace (no text or symbols visible)
</details>

Alice Faisal (Graduate Student Member, IEEE) received the M.Sc. degree in electrical engineering from Memorial University, Canada, in 2022. She is currently pursuing the Ph.D. degree with Memorial University. Her research interests include 6G enabling technologies, reconfigurable intelligent surfaces, integrated sensing and communication, and full-duplex communications.

![](images/5b41cd1afd629240c0fd42b2f40584b8d538604855067443cc516f1c7abd12a5.jpg)

<details>
<summary>natural_image</summary>

Portrait of a man with beard wearing a black polo shirt (no text or symbols visible)
</details>

Ibrahim Al-Nahhal (Senior Member, IEEE) received the B.Sc. (Hons.) degree in electronics and communications engineering from Al-Azhar University, Cairo, Egypt, in 2007, the M.Sc. degree in electronics and communications engineering from Egypt–Japan University for Science and Technology, Egypt, in 2014, and the Ph.D. degree in electronics and communications engineering from Memorial University, Canada, in 2020. From 2008 and 2012, he was an Engineer in industry and a Teaching Assistant at the Faculty of Engineering, Al-Azhar

University. From 2014 to 2015, he was a Physical Layer Expert at Nokia (formerly Alcatel-Lucent), Belgium. He has been a Research Associate and a Per-Course Instructor at Memorial University since 2021. He has also been an Assistant Professor with Memorial University since 2024. He holds three patents and co-authored more than 40 peer-reviewed journals and conference papers in top-ranked venues. His research interests include reconfigurable intelligent surfaces, full-duplex communications, integrated sensing and communication, channel estimation, machine learning, design of low-complexity receivers for emerging technologies, spatial modulation, multiple-input multiple-output communications, sparse code multiple access, and optical communications. He served as a technical program committee member and a reviewer for various prestigious journals and conferences. He was awarded the Exemplary Reviewer of IEEE COMMUNICATIONS LETTERS in 2017. He serves as an Editor for IEEE WIRELESS COMMUNICATIONS LETTERS.

![](images/fe0a9b76fd78150c184ea3572bbac357c21cad412c6527750d017ec02565a4b9.jpg)

<details>
<summary>natural_image</summary>

Portrait of a middle-aged man with short dark hair, wearing a dark jacket over a blue collared shirt (no text or symbols visible)
</details>

Kyesan Lee (Member, IEEE) received the B.E. degree in electrical engineering from Kyung Hee University, South Korea, in 1996, and the M.S. and Ph.D. degrees from the Department of Electrical Engineering, Keio University, Yokohama, Japan, in 1999 and 2002, respectively. In 2002, he joined KDDI R&D Laboratories Inc. Since 2003, he has been with the College of Electronics and Information, Kyung Hee University, where he is currently a Professor. His research interests include wireless communication networks, CDMA, OFDM, MC-CDMA, MC-DS/CDMA, MIMO, and cognitive radio and visible light communication systems. He received the IEEE VTS Japan Young Researchers Encouragement Award and the Excellent Paper Award from the IEEE International Symposium on Communication and Information Technology (ISCIT) in 2009. He also received the Prime Minister Award in 2009 and the Minister Award from the Ministry of Education, Science and Technology in 2009.

![](images/6dc2432ad8b602a7b07af558281d8c3ed2d8c2b9db39c1b1501fa459265aaa27.jpg)

<details>
<summary>natural_image</summary>

Portrait of a man wearing a gray sweater over a collared shirt (no visible text or symbols)
</details>

Hyundong Shin (Fellow, IEEE) received the B.S. degree in electronics engineering from Kyung Hee University (KHU), Yongin-si, South Korea, in 1999, and the M.S. and Ph.D. degrees in electrical engineering from Seoul National University, Seoul, South Korea, in 2001 and 2004, respectively. During his Post-Doctoral Research at Massachusetts Institute of Technology (MIT) from 2004 to 2006, he was with the Laboratory for Information Decision Systems (LIDS). In 2006, he joined the KHU, where he is currently a Professor with the Department of Electronic Engineering. His research interests include quantum information science, wireless communication, and machine intelligence. He received the IEEE Communications Society’s Guglielmo Marconi Prize Paper Award and William R. Bennett Prize Paper Award. He served as the Publicity Co-Chair for the IEEE PIMRC and the Technical Program Co-Chair for the IEEE WCNC and the IEEE GLOBECOM. He was an Editor of IEEE TRANSACTIONS ON WIRELESS COMMUNICATIONS and IEEE COMMUNICATIONS LETTERS.

![](images/22a06176c7b7519530389e6b0086ed34fdeb36080a31b62ea3106859936ee368.jpg)

<details>
<summary>natural_image</summary>

Portrait of a smiling woman with short brown hair wearing a patterned scarf (no text or symbols visible)
</details>

Octavia A. Dobre (Fellow, IEEE) is currently a Professor and the Tier-1 Canada Research Chair with Memorial University, Canada. Her research interests encompass wireless communication and networking technologies and optical and underwater communications. She has (co-)authored over 500 refereed articles in these areas. She received ten best paper awards, including the IEEE Heinrich Hertz Award. She serves as the VP of Publications of the IEEE Communications Society. She was the inaugural Editor-in-Chief (EiC) of IEEE OPEN JOURNAL OF THE COMMUNICATIONS SOCIETY and the EiC of IEEE COMMUNICATIONS LETTERS. She was a Fulbright Scholar, a Royal Society Scholar, and a Distinguished Lecturer of the IEEE Communications Society. She is an Elected Member of the European Academy of Sciences and Arts; and a fellow of the Engineering Institute of Canada, the Canadian Academy of Engineering, and the Royal Society of Canada.