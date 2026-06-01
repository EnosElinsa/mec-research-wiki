# Cramér-Rao Bound Optimization for Active RIS-Empowered ISAC Systems

Qi Zhu, Ming Li , Senior Member, IEEE, Rang Liu , Member, IEEE, and Qian Liu , Member, IEEE

Abstract— Integrated sensing and communication (ISAC), which simultaneously performs sensing and communication functions within a shared frequency band and hardware platform, has emerged as a promising technology for future wireless systems. Nevertheless, the weak echo signal received by the low-sensitivity ISAC receiver significantly constrains sensing performance in scenarios involving obstructed targets. Active reconfigurable intelligent surface (RIS) has become a prospective solution by situationally manipulating the wireless propagations and amplifying the signals. In this paper, we investigate active RIS-empowered ISAC systems to enhance radar echo signal quality as well as communication performance. In particular, we focus on the joint design of the base station (BS) transmit precoding and the active RIS reflection beamforming to optimize the parameter estimation performance in terms of Cramér-Rao bound (CRB) subject to the communication users’ signal-tointerference-plus-noise ratio (SINR) requirements. An efficient algorithm based on alternating optimization, semidefinite relaxation (SDR), and majorization-minimization (MM) is proposed to solve the formulated challenging non-convex problem. Finally, simulation results validate the effectiveness of the developed algorithm and the potential of employing active RIS in ISAC systems to enhance direct-of-arrival (DoA) estimation performance.

Index Terms— Integrated sensing and communication (ISAC), active reconfigurable intelligent surface (RIS), multi-user multiinput single-output (MU-MISO) communications, direct-ofarrival (DoA) estimation, Cramér-Rao bound (CRB).

# I. INTRODUCTION

BOTH high-quality wireless connectivity and high-accuratesensing ability are required in next-generation wireless

Manuscript received 23 May 2023; revised 18 October 2023 and 8 February 2024; accepted 24 March 2024. Date of publication 10 April 2024; date of current version 12 September 2024. This work was supported in part by the National Natural Science Foundation of China under Grant 62371090 and Grant 62071083, in part by Liaoning Applied Basic Research Program under Grant 2023JH2/101300201 and Grant 2023JH2/101700364, and in part by Dalian Science and Technology Innovation Project under Grant 2022JJ12GX014. The associate editor coordinating the review of this article and approving it for publication was I. Bergel. (Corresponding author: Ming Li.)

Qi Zhu and Ming Li are with the School of Information and Communication Engineering, Dalian University of Technology, Dalian 116024, China (e-mail: qzhu@mail.dlut.edu.cn; mli@dlut.edu.cn).

Rang Liu is with the Center for Pervasive Communications and Computing, University of California at Irvine, Irvine, CA 92697 USA (e-mail: rangl2@uci.edu).

Qian Liu is with the School of Computer Science and Technology, Dalian University of Technology, Dalian 116024, China (e-mail: qianliu@dlut.edu.cn).

Color versions of one or more figures in this article are available at https://doi.org/10.1109/TWC.2024.3384501.

Digital Object Identifier 10.1109/TWC.2024.3384501

networks to support intelligent manufacturing, intelligent transportation, intelligent medical, and other emerging applications. Benefiting from the widespread employment of millimeter wave (mmWave) and massive multiple-input multiple-output (MIMO) technologies, communication signals exhibit high resolution in the angular domain, enabling sensing with communication signals, which motivates integrated sensing and communication (ISAC) to become one of the leading technical trends [1], [2], [3], [4]. By utilizing a fully shared platform and transmitting dual-functional waveforms to simultaneously perform sensing and communication, ISAC is expected to significantly boost spectral efficiency and energy efficiency as well as reduce hardware costs and signaling overhead.

Instead of treating communication and sensing as two separate goals, ISAC pursues a deeper level of integration of them to achieve mutual benefit through co-designs. Various advanced signal processing techniques are proposed to design dual-functional waveforms based on different communication/sensing metrics [5], [6], [7], [8], [9]. Typical communication performance metrics include the signal-to-interference-plus-noise ratio (SINR), the multi-user interference (MUI), and the achievable sum-rate. Meanwhile, frequently used sensing performance metrics include the beampattern mean squared error (MSE), the waveform similarity, and the received echo power/signal-to-noise ratio (SNR). In addition to the metrics mentioned above, Cramér-Rao bound (CRB) is also an essential sensing performance metric for target parameter estimation, which provides a lower bound on the variance of any unbiased estimator [10], [11].

Reconfigurable intelligent surface (RIS) is also recognized as a key enabling technology for next-generation wireless networks thanks to its superior ability to intelligently reconfigure the wireless propagation environment. Specifically, RIS is a meta-surface composed of passive electromagnetic elements, in which each element can individually and adaptively tune the phase-shifts of the incident signals. By intelligently coordinating reflections, RIS can establish a favorable virtual line-of-sight (LoS) link between the transmitter and the receiver, thus providing a novel approach for addressing wireless channel fading impairment and interference problems [12], [13]. By introducing additional degrees of freedom (DoFs), deploying RIS in existing wireless networks can not only substantially improve communication quality, but also significantly expand communication coverage [14], [15], [16], [17].

The success of RIS applications in various communication scenarios has inspired research to explore the combination of RIS and ISAC technologies [18], [19], [20]. The authors in [21], [22] employ RIS within ISAC systems to offer additional propagation paths for radar echo signals and simultaneously enhance communication performance. In [23], RIS is utilized to create virtual LoS links to sense the potential target blocked by obstacles. The co-design of transmit waveform, receive filter, and RIS reflection coefficients in the presence of strong clutter in the RIS-aided ISAC systems is considered in [24]. The multi-user sum-rate maximization under the radar SNR constraint or CRB constraint is investigated in [25]. In [26], the authors explore the performance trade-off maximization between communication data rate and sensing mutual information (MI). Robust beamforming design for RIS-aided ISAC systems under imperfect angle knowledge and channel state information (CSI) is studied in [27]. In [28], [29], RIS is deployed in ISAC systems to mitigate MUI while guaranteeing the radar sensing beampattern and CRB constraint, respectively. Moreover, different from previous studies on narrowband scenarios, recent works [30], [31] investigate wideband RISaided ISAC systems in conjunction with orthogonal frequency division multiplexing (OFDM) technology.

While numerous studies on RIS have demonstrated its advantages in both communication and ISAC systems, its fatal defect, i.e., the “multiplicative fading” effect, has also been exposed. The equivalent path-loss of the RIS-introduced reflection link is a product of the path-losses of the transmitter-RIS link and the RIS-receiver link, thus this phenomenon can be mathematically described as the signal from the transmitter to the receiver via RIS undergoing multiplicative fading. Consequently, in the case of a strong direct link or when the receiver is not close enough to RIS, the performance improvement from the reflection link provided by the passive RIS is marginal. Active RIS is an emerging technology proposed to effectively mitigate the multiplicative fading issue existing in conventional passive RIS-aided systems [32], [33]. By integrating reflection-type amplifiers into existing passive electromagnetic components, active RIS is capable of not only reflecting the incident signal with the desired phase-shift, but also amplifying the reflected signal, thereby efficiently compensating the path-loss. Recent research works [32], [33], [34], [35], [36], [37], [38] have confirmed the advantages of active RIS and further investigated its various communication application scenarios. Although the active RIS has potential drawbacks and limitations in that it is more costly and has more power consumption than the passive one due to the integration of active amplifiers, a satisfactory balance between performance and cost/power consumption can be achieved by appropriately selecting the number of reflection elements. In general, active RIS is increasingly becoming one of the key enablers to realize more spectrum- and energy-efficient wireless communications.

Owing to its significant advantage in overcoming severe path-loss, active RIS intrinsically possesses immense potential in ISAC systems. The reason for this is that the receivers in practical ISAC systems are typically less sensitive than traditional radar receivers, primarily due to cost considerations related to hardware. Hence, the reception of weak echo signals by the low-sensitivity ISAC receivers results in unsatisfactory target detection/parameter estimation performance. Active RIS has become a prospective solution for ISAC systems to address the above issues and enhance both radar echo signal quality and communication performance by situationally manipulating the wireless propagations and amplifying the signals. There are several studies intended to explore the application of active RIS in ISAC systems. The authors in [39] propose to utilize an active RIS to improve the achievable communication secrecy rate while taking into account the worst radar detection SNR. Moreover, an active RIS-aided ISAC system in the scenario of a cloud radio access network (C-RAN) is investigated in [40]. Our recent work [41] employs active RIS to overcome the blockage issue by introducing an additional virtual LoS link between the base station (BS) and the target. Both transmit/receive and reflection beamformings are jointly designed to maximize the radar SNR while guaranteeing pre-defined SINRs for communication users. While existing works on active RIS-empowered ISAC systems focus on target detection function, target parameter estimation is also an important task in radar sensing and should be further explored.

Motivated by the aforementioned discussions, we investigate the deployment of active RIS in ISAC systems in this paper, with an emphasis on the parameter estimation function for the radar sensing component. Specifically, we consider an ISAC system where BS communicates with multiple users and simultaneously senses a point target blocked by an obstacle. An active RIS is employed to support both communication and sensing functions. Our goal is to jointly design the BS transmit precoding and the active RIS reflection beamforming to optimize the direct-of-arrival (DoA) estimation performance and satisfy the users’ quality of service (QoS) demands and the power limitations at the BS and the active RIS. The main novelties and contributions of this paper are summarized as follows.

• Firstly, we introduce active RIS in ISAC systems to enhance the radar parameter estimation performance while guaranteeing the quality of multi-user communications. We formulate signal models for the reception at both the communication users and the BS, from which we derive performance metrics for communication and radar sensing, respectively. More specifically, the CRB for the target DoA estimation in this considered active RIS-empowered ISAC system is meticulously derived for the first time, which is quite different from the CRB for passive RIS-assisted ISAC systems. While the CRB of DoA estimation is utilized to evaluate the sensing performance of target DoA estimation, the SINR of each user is employed to assess the communication performance.

• Then, we formulate the joint transmit precoding and active RIS beamforming design problem that aims at minimizing the CRB for target DoA estimation, subject to communication users’ SINR requirements, power limitations at the BS and the active RIS, and amplitude constraints of the active RIS reflection coefficients. In an effort to tackle the intricate joint design challenge due to the introduction of active RIS, we develop an effective algorithm that leverages alternating optimization, semidefinite relaxation (SDR), and majorization-minimization (MM) methods.

![](images/5565e7d533dbf2d4642eeb402b91fdb03a758abd14a3a80f81b74602bbd048d2.jpg)

<details>
<summary>text_image</summary>

G
h_d,k
h_r,k
h_r,t
</details>

Fig. 1. An active RIS-empowered ISAC system.

• Finally, we provide extensive simulation results to verify the advantages of the proposed active RIS-empowered ISAC scheme and the effectiveness of the developed joint design algorithm. Notably, active RIS can offer over 30dB CRB reduction compared to passive RISassisted ISAC systems, thereby achieving substantial sensing performance improvement.

Notations: a is a scalar, a is a column vector, and A is a matrix, respectively. $\mathbf { A } ^ { T } , \ \mathbf { A } ^ { * } , \ \mathbf { A } ^ { H }$ and ${ { \bf A } ^ { - 1 } }$ denote the transpose, conjugate, Hermitian (conjugate transpose) and inverse operations, respectively. $| a | , \ \lVert \mathbf { a } \rVert _ { 2 }$ and $\| \mathbf { A } \| _ { F }$ denote the magnitude of a scalar $^ { a , }$ the norm of a vector a and the Frobenius norm of matrix A. diag{a} is a diagonal matrix whose diagonal elements are extracted from vector a. rank{A} is the rank of the matrix A, Tr{A} is the trace of the matrix A and vec{A} denotes vectorization of the matrix A. ${ \mathbf { I } } _ { N }$ is an identity matrix of N dimension and 0 refers to an all-zeros vector. ⊗ is the Kronecker product. C represents the set of complex numbers. $\Re \{ \cdot \}$ and $\Im \{ \cdot \}$ extract the real part and imaginary part of a complex number, respectively.

# II. SYSTEM MODEL AND PROBLEM FORMULATION

We consider an active RIS-empowered ISAC system as depicted in Fig. 1, in which a dual-functional BS simultaneously performs multi-user communication and co-located radar sensing functions. Particularly, the BS equipped with $N _ { \mathrm { t } }$ transmit antennas and $N _ { \mathrm { r } }$ receive antennas communicates with K single-antenna users and senses one potential target with the aid of an M -element active RIS. The target is located in the blind zone of the BS, where the direct BS-target link is blocked by obstacles. For simplicity, we adopt the assumption that $N _ { \mathrm { t } } = N _ { \mathrm { r } } = N$ in the following. To achieve both satisfactory communication and sensing performance, the transmit dualfunctional signal in the l-th time slot is composed of precoded communication symbols and radar signals, which can be expressed as

$$
\mathbf {x} [ l ] = \mathbf {W} _ {\mathrm{c}} \mathbf {s} _ {\mathrm{c}} [ l ] + \mathbf {W} _ {\mathrm{r}} \mathbf {s} _ {\mathrm{r}} [ l ] = \mathbf {W} \mathbf {s} [ l ], \tag {1}
$$

where $\mathbf { s } _ { \mathrm { c } } [ l ] \in \mathbb { C } ^ { K }$ denotes the communication symbols satisfying $\mathbb { E } \{ \mathbf { \bar { s } } _ { \mathrm { c } } [ l ] \mathbf { s } _ { \mathrm { c } } [ l ] ^ { H } \} = \mathbf { I } _ { K }$ and $\mathbf { s } _ { \mathrm { r } } [ l ] \in \mathbb { C } ^ { N }$ denotes the radar signals with $\mathbb { E } \{ \mathbf { s } _ { \mathrm { r } } [ \boldsymbol { l } ] \mathbf { s } _ { \mathrm { r } } [ \boldsymbol { l } ] ^ { H } \} = \mathbf { I } _ { N } , \mathbb { E } \{ \mathbf { s } _ { \mathrm { c } } [ \boldsymbol { l } ] \mathbf { s } _ { \mathrm { r } } [ \boldsymbol { l } ] ^ { H } \} = \mathbf { 0 . ~ W }$ c ∈ $\mathbb { C } ^ { \smile N \times K }$ and $\mathbf { W } _ { \mathrm { r } } \in \dot { \mathbb { C } } ^ { N \times N }$ represent the communication/radar beamforming matrices, respectively. Furthermore, we define $\mathbf { W } \triangleq [ \mathbf { W } _ { \mathrm { c } } \ \mathbf { W } _ { \mathrm { r } } ]$ and ${ \bf s } [ l ] \triangleq \mathrm { [ } { \bf s } _ { \mathrm { c } } [ l ] ^ { T } { \bf \dot { s } } _ { \mathrm { r } } [ l ] ^ { T } ] ^ { T }$ for brevity.

# A. Communication Signal Model

The received signal at the k-th communication user is presented as

$$
y _ {k} [ l ] = (\mathbf {h} _ {\mathrm{d}, k} ^ {T} + \mathbf {h} _ {\mathrm{r}, k} ^ {T} \boldsymbol {\Phi} \mathbf {G}) \mathbf {x} [ l ] + \mathbf {h} _ {\mathrm{r}, k} ^ {T} \boldsymbol {\Phi} \mathbf {z} _ {0} [ l ] + n _ {k} [ l ], \tag {2}
$$

where $\mathbf { h } _ { \mathrm { d } , k } \in \mathbb { C } ^ { N }$ represents the channel between the BS and the k-th user, $\mathbf { G } \in \mathbb { C } ^ { M \times N }$ represents the channel between the BS and the active RIS, and $\mathbf { h } _ { \mathrm { r } , k } \in \mathbb { C } ^ { M }$ represents the channel between the active RIS and the k-th user. With advanced channel estimation methods, we assume that the channel is perfectly known. $\Phi ~ \in ~ \mathbb { C } ^ { M \times M }$ denotes the active RIS reflection beamforming matrix with ${ \Phi } \triangleq \mathrm { d i a g } \{ { \phi } \}$ , in which $\boldsymbol { \phi } \triangleq [ \phi _ { 1 } , \dots , \phi _ { M } ] ^ { T } \in \mathbf { \bar { \mathbb { C } } } ^ { M }$ is the reflection coefficient vector. Unlike traditional passive RIS which only has the capacity to tune the phase-shift of the incident signal, active RIS can further amplify its amplitude thanks to the integration of additional amplifiers into each electromagnetic element. It is assumed that all active RIS reflection elements are realized by the same type of amplifier, namely, they have the same amplification capacity. Accordingly, we can formulate the reflection coefficient of the active RIS as $\phi _ { m } \triangleq a _ { m } e ^ { \mathcal { I } \varphi _ { m } }$ , ∀m, and the amplitude $a _ { m }$ can be continuously adjusted within the interval $a _ { m } \in ( 0 , { a } _ { \operatorname* { m a x } } ]$ , in which $a _ { \mathrm { m a x } } \geq 1$ is the maximum signal amplification provided by the amplifier. In addition, $\mathbf { z } _ { 0 } [ l ] \sim \mathcal { C N } ( \mathbf { 0 } , \sigma _ { \mathrm { z } } ^ { 2 } \mathbf { I } _ { M } )$ and $n _ { k } [ l ] \sim \mathcal { C N } ( 0 , \sigma _ { k } ^ { 2 } )$ denote additive white Gaussian noise (AWGN) at the active RIS and the k-th user, respectively.

For multi-user communications, the widely-used SINR is adopted as the performance metric. Based on the received signal expression in (2), the SINR of the k-th user can be calculated as

$$
\mathrm{SINR} _ {k} = \frac {\left| \mathbf {h} _ {k} ^ {T} \mathbf {w} _ {k} \right| ^ {2}}{\sum_ {i \neq k} ^ {K + N} \left| \mathbf {h} _ {k} ^ {T} \mathbf {w} _ {i} \right| ^ {2} + \left\| \mathbf {h} _ {\mathrm{r} , k} ^ {T} \boldsymbol {\Phi} \right\| _ {2} ^ {2} \sigma_ {\mathrm{z}} ^ {2} + \sigma_ {k} ^ {2}}, \tag {3}
$$

where we define $\mathbf { h } _ { k } ^ { T } \triangleq \mathbf { h } _ { \mathrm { d } , k } ^ { T } + \mathbf { h } _ { \mathrm { r } , k } ^ { T }$ hTd,k ΦG as the equivalent compound channel between the BS and the k-th user and $\mathbf { w } _ { i }$ as the i-th column of W.

# B. Radar Signal Model

Since the direct BS-target link is blocked by obstacles, the transmitted signal can only reach the target through the active RIS-assisted reflected link and return via the same path. Therefore, the received echo signal at the BS is denoted as

$$
\mathbf {y} _ {\mathrm{r}} [ l ] = \mathbf {G} ^ {T} \boldsymbol {\Phi} \left(\mathbf {h} _ {\mathrm{r}, \mathrm{t}} \alpha \mathbf {h} _ {\mathrm{r}, \mathrm{t}} ^ {T} \boldsymbol {\Phi} (\mathbf {G x} [ l ] + \mathbf {z} _ {0} [ l ]) + \mathbf {z} _ {1} [ l ]\right) + \mathbf {n} _ {\mathrm{r}} [ l ], \tag {4}
$$

where $\alpha \sim \mathcal { C N } ( 0 , \sigma _ { \mathrm { t } } ^ { 2 } )$ is the target’s radar cross section (RCS) and $\mathbf { h } _ { \mathrm { r , t } } \in \mathbb { C } ^ { M }$ is the LoS channel from the active RIS to the target. Specifically, $\mathbf { h } _ { \mathrm { r , t } } \triangleq \alpha _ { \mathrm { r , t } } \mathbf { a } _ { M } ( \theta )$ , where $\alpha _ { \mathrm { r , t } }$ represents the path-loss and $\mathbf { a } _ { M } ( \theta ) \ \triangleq \ [ 1 , e ^ { \jmath \tilde { \pi } \sin \theta } , \dots , e ^ { \jmath ( M - 1 ) \pi \sin \theta } ] ^ { T }$ represents the steering vector with θ being the DoA of the target with respect to the active RIS. We assume that the target is potentially located at a certain angle/range detection cell. As a result, the DoA with respect to the active RIS and the LoS link of the RIS-target channel are considered known for the purpose of calculating the target estimation CRB. Moreover, $\mathbf { z } _ { 1 } [ l ] \sim \mathcal { C N } ( \mathbf { 0 } , \sigma _ { \mathrm { z } } ^ { 2 } \mathbf { I } _ { M } )$ and $\mathbf { n } _ { \mathrm { r } } [ l ] \sim \mathcal { C } \mathcal { N } ( \mathbf { 0 } , \sigma _ { \mathrm { r } } ^ { 2 } \mathbf { I } _ { N } )$ are AWGN at the active RIS and the BS, respectively. Since the noise signal ${ \bf z } _ { 0 } [ l ]$ undergoes multiple attenuations through the RIStarget-RIS-BS link, when the echo signal reaches the BS, its power is substantially smaller than that of other signals, typically of the order of $1 0 ^ { 6 }$ , thereby can be ignored. Then, the received signal $\mathbf { y } _ { \mathrm { r } } [ l ]$ can be further approximated as

$$
\mathbf {y} _ {\mathrm{r}} [ l ] \approx \alpha \mathbf {G} ^ {T} \boldsymbol {\Phi} \mathbf {h} _ {\mathrm{r}, \mathrm{t}} \mathbf {h} _ {\mathrm{r}, \mathrm{t}} ^ {T} \boldsymbol {\Phi} \mathbf {G} \mathbf {W} \mathbf {s} [ l ] + \mathbf {G} ^ {T} \boldsymbol {\Phi} \mathbf {z} _ {1} [ l ] + \mathbf {n} _ {\mathrm{r}} [ l ]. \tag {5}
$$

By stacking L samples, we can express the combined received signals as

$$
\mathbf {Y} _ {\mathrm{r}} = \alpha \mathbf {Q W S} + \mathbf {G} ^ {T} \boldsymbol {\Phi} \mathbf {Z} _ {1} + \mathbf {N} _ {\mathrm{r}}, \tag {6}
$$

where we define $\mathbf { Q } \triangleq \mathbf { G } ^ { T } \Phi \mathbf { h } _ { \mathrm { r } , \mathrm { t } } \mathbf { h } _ { \mathrm { r } , \mathrm { t } } ^ { T }$ tΦG and the symbol/noise matrices as $\mathbf { S } \triangleq [ \mathbf { s } [ 1 ] , \ldots , \mathbf { s } [ L ] ] , \ : \mathbf { Z } _ { 1 } \triangleq [ \mathbf { z } _ { 1 } [ 1 ] , \ldots , \mathbf { z } _ { 1 } [ L ] ]$ and $\mathbf { N } _ { \mathrm { r } } \triangleq [ \mathbf { n } _ { \mathrm { r } } [ 1 ] , \dots , \mathbf { n } _ { \mathrm { r } } [ L ] ]$ ], respectively. As the dual-functional BS executes the co-located radar sensing function, it has full knowledge of the transmit signal. Therefore, the entire first term in (6), including both the communication and sensing components, is regarded as a useful signal for estimating target parameters, while the second and third terms are considered as noise signals. The vectorized signal is further denoted as

$$
\widetilde {\mathbf {y}} = \operatorname{vec} \left\{\mathbf {Y} _ {\mathrm{r}} \right\} = \mathbf {y} + \mathbf {n}, \tag {7}
$$

in which we apply the definitions of $\mathbf { y } \triangleq \alpha \mathbf { v e c } \{ \mathbf { Q } \mathbf { W } \mathbf { S } \}$ and $\begin{array} { r } { \mathbf { n } \triangleq \mathrm { v e c } \{ \mathbf { G } ^ { T } \boldsymbol { \Phi } \mathbf { \bar { Z } } _ { 1 } + \mathbf { N } _ { \mathrm { r } } \} } \end{array}$ .

From the perspective of radar sensing, we focus on parameter estimation performance in terms of CRB. It offers a lower-bound on any unbiased estimator and is an extensively utilized radar metric. Let $\begin{array} { r } { \pmb { \xi } \triangleq [ \pmb { \theta } , \pmb { \alpha } ^ { T } ] ^ { T } } \end{array}$ denote the target parameters to be estimated with α $\triangleq [ \Re \{ \alpha \} , \Im \{ \alpha \} ] ^ { T }$ . The CRB matrix is the inverse of the Fisher information matrix (FIM) for estimating ξ [42]. In order to facilitate the derivation of CRB, we let $ { \mathbf { M } } \in \mathbb { C } ^ { 3 \times 3 }$ represent the FIM. As presented in [42], based on the complex observation $\widetilde { \mathbf { y } } \sim \mathcal { C N } ( \mathbf { y } , \mathbf { R } _ { \mathrm { n } } )$ with $\mathbf { R } _ { \mathrm { n } } \triangleq \mathbf { I } _ { L } \otimes ( \sigma _ { \mathbf { z } } ^ { 2 } \mathbf { G } ^ { T } \pmb { \Phi } \pmb { \Phi } ^ { H } \mathbf { G } ^ { \ast } + \sigma _ { \mathrm { r } } ^ { 2 } \mathbf { I } _ { N } )$ e, each element of M for estimating the unknown parameters ξ can be calculated by

$$
\mathbf {M} (i, j) = \operatorname{Tr} \left\{\mathbf {R} _ {\mathrm{n}} ^ {- 1} \frac {\partial \mathbf {R} _ {\mathrm{n}}}{\partial \boldsymbol {\xi} _ {i}} \mathbf {R} _ {\mathrm{n}} ^ {- 1} \frac {\partial \mathbf {R} _ {\mathrm{n}}}{\partial \boldsymbol {\xi} _ {j}} \right\} + 2 \Re \left\{\frac {\partial \mathbf {y} ^ {H}}{\partial \boldsymbol {\xi} _ {i}} \mathbf {R} _ {\mathrm{n}} ^ {- 1} \frac {\partial \mathbf {y}}{\partial \boldsymbol {\xi} _ {j}} \right\}. \tag {8}
$$

According to the definition of $\begin{array} { r l r } { { \bf y } } & { { } \triangleq } & { \alpha { \bf v e c } \{ { \bf Q } { \bf W } { \bf S } \} } \end{array}$ , the derivatives of y with respect to each parameter can be obtained as

$$
\frac {\partial \mathbf {y}}{\partial \theta} = \alpha \mathrm{vec} \{\dot {\mathbf {Q}} \mathbf {W} \mathbf {S} \}, \tag {9a}
$$

$$
\frac {\partial \mathbf {y}}{\partial \boldsymbol {\alpha}} = [ 1, j ] \otimes \operatorname{vec} \left\{\mathbf {Q W S} \right\}, \tag {9b}
$$

where ${ \dot { \mathbf { Q } } } \triangleq { \frac { \partial \mathbf { Q } } { \partial \theta } }$ denotes the partial derivative of Q in terms of $\theta \ [ 4 3 ]$ . Recalling $\mathbf { Q } \triangleq \mathbf { G } ^ { T } \Phi \mathbf { h } _ { \mathrm { r , t } } \mathbf { h } _ { \mathrm { r , t } } ^ { T } \Phi \mathbf { G } , \mathbf { h } _ { \mathrm { r , t } } \triangleq \alpha _ { \mathrm { r , t } } \mathbf { a } _ { M } ( \theta )$ , and defining $\mathbf { q } \triangleq \mathbf { G } ^ { T } \Phi \mathbf { a } _ { M } ( \theta )$ , Q can be re-expressed as $\mathbf Q =$ $\alpha _ { \mathrm { r , t } } ^ { 2 } \mathbf { q } \mathbf { q } ^ { T }$ . Thus, the partial derivative $\dot { \mathbf { Q } }$ is written as

$$
\begin{array}{l} \dot {\mathbf {Q}} = \alpha_ {\mathrm{r}, \mathrm{t}} ^ {2} (\dot {\mathbf {q}} \mathbf {q} ^ {T} + \mathbf {q} \dot {\mathbf {q}} ^ {T}) \\ = c _ {0} \mathbf {G} ^ {T} \mathbf {A} (\mathbf {L} \phi \phi^ {T} + \phi \phi^ {T} \mathbf {L}) \mathbf {A} \mathbf {G}, \tag {10} \\ \end{array}
$$

where $\dot { \mathbf { q } }$ is the partial derivative of q with respect to $\theta ,$ which is derived as $\begin{array} { r } { \dot { \mathbf { q } } \ \triangleq \ \frac { \partial \mathbf { q } } { \partial \theta } \ = \ j \pi \mathrm { c o s } \theta \mathbf { G } ^ { T } \Phi \dot { \mathbf { L a } } _ { M } ( \theta ) \ = \ } \end{array}$ ȷπ cos $\theta \mathbf { G } ^ { T } \mathbf { A L } \phi$ with $\mathrm { ~ \bf ~ L ~ } \stackrel { \Delta } { = } \mathrm { d i a g } \{ 0 , 1 , \cdot \cdot \cdot , M - 1 \}$ and $\mathbf { A } \triangleq \mathrm { d i a g } \{ \mathbf { a } _ { M } ( \theta ) \}$ . In addition, we define $c _ { 0 } \triangleq \alpha _ { \mathrm { r , t } } ^ { 2 } \jmath \pi$ cos θ n  L (σ2z GT ΦΦH G∗ + σ2r IN ) is irrelevant to ξ, that is, ∂Rn∂ξi for simplicity. Moreover, it is obvious that $( \sigma _ { \mathbf { z } } ^ { 2 } \mathbf { G } ^ { T } \dot { \Phi } \Phi ^ { H } \mathbf { \bar { G } } ^ { * } + \sigma _ { \mathrm { r } } ^ { 2 } \mathbf { I } _ { N } )$ $\xi ,$ $\mathbf { R } _ { \mathrm { n } } \triangleq \mathbf { I } _ { L } \otimes$ $\begin{array} { r } { \frac { \partial \mathbf { R } _ { \mathrm { n } } } { \partial \pmb { \xi } _ { i } } = } \end{array}$ = 0, ∀i. For ease of subsequent handling, we partition M into $2 \times 2$ blocks as

$$
\mathbf {M} = \left[ \begin{array}{l l} \mathbf {M} _ {\theta \theta} & \mathbf {M} _ {\theta \alpha} \\ \mathbf {M} _ {\theta \alpha} ^ {T} & \mathbf {M} _ {\alpha \alpha} \end{array} \right]. \tag {11}
$$

Accordingly, based on the above derivations, $\mathbf { M } _ { \theta \theta }$ can be calculated as

$$
\mathbf {M} _ {\theta \theta} = 2 \Re \left\{\frac {\partial \mathbf {y} ^ {H}}{\partial \theta} \mathbf {R} _ {\mathrm{n}} ^ {- 1} \frac {\partial \mathbf {y}}{\partial \theta} \right\} \tag {12a}
$$

$$
= 2 \Re \left\{\alpha^ {*} \operatorname{vec} ^ {H} \left\{\dot {\mathbf {Q}} \mathbf {W} \mathbf {S} \right\} \left(\mathbf {I} _ {L} \otimes \widetilde {\mathbf {R}} _ {\mathrm{n}} ^ {- 1}\right) \alpha \operatorname{vec} \left\{\dot {\mathbf {Q}} \mathbf {W} \mathbf {S} \right\} \right\} \tag {12b}
$$

$$
= 2 | \alpha | ^ {2} \operatorname{Tr} \left\{\dot {\mathbf {Q}} \mathbf {W} \mathbf {S} \mathbf {S} ^ {H} \mathbf {W} ^ {H} \dot {\mathbf {Q}} ^ {H} \widetilde {\mathbf {R}} _ {\mathrm{n}} ^ {- 1} \right\} \tag {12c}
$$

$$
= 2 L | \alpha | ^ {2} \mathrm{Tr} \{\dot {\mathbf {Q}} \mathbf {W} \mathbf {W} ^ {H} \dot {\mathbf {Q}} ^ {H} \widetilde {\mathbf {R}} _ {\mathrm{n}} ^ {- 1} \}, \tag {12d}
$$

where (12a)-(12b) holds since we re-denote $\mathbf { R } _ { \mathrm { n } } \triangleq \mathbf { I } _ { L } \otimes \widetilde { \mathbf { R } } _ { \mathrm { n } }$ with $\widetilde { \mathbf { R } } _ { \mathrm { n } } \triangleq \sigma _ { \mathrm { z } } ^ { 2 } \mathbf { G } ^ { T } \boldsymbol { \Phi } \boldsymbol { \Phi } ^ { H } \mathbf { G } ^ { \ast } + \sigma _ { \mathrm { r } } ^ { 2 } \mathbf { I } _ { N }$ eand apply the property ${ \bf R } _ { \mathrm { n } } ^ { - 1 } \ = \ { \bf I } _ { L } \ \tilde { \otimes } \ \tilde { \bf R } _ { \mathrm { n } } ^ { - 1 }$ . The transformations Tr{ABCD} = $\mathrm { v e c } ^ { - } { \overset { \vartriangle } { \left\{ { \bf D } ^ { H } \right\} } } ( { \bf C } ^ { T } \ \otimes { \bf A } ) \mathrm { v e c } \{ { \bf B } \}$ and $\mathrm { T r } \{ { \bf A B } \} = \mathrm { T r } \{ { \bf B A } \}$ are utilized to support the conversion in (12b)-(12c) [44]. Moreover, it is noted that due to the facts that $\mathbb { E } \{ { \bf S } { \bf S } ^ { H } \} =$ $L \mathbf { I } _ { N + K }$ and sufficient samples are usually collected for parameter estimation, we assume that $\begin{array} { l } { { \bf { S } } { { \bf { \bar { S } } } } ^ { H } } \end{array} = \begin{array} { c } { { L { \bf { I } } _ { N + K } } } \end{array}$ in (12c)-(12d). Similarly, $\mathbf { M } _ { \theta \alpha }$ and $\mathbf { M } _ { \alpha \alpha }$ are given by

$$
\mathbf {M} _ {\theta \boldsymbol {\alpha}} = 2 \Re \left\{\frac {\partial \mathbf {y} ^ {H}}{\partial \theta} \mathbf {R} _ {\mathrm{n}} ^ {- 1} \frac {\partial \mathbf {y}}{\partial \boldsymbol {\alpha}} \right\} \tag {13a}
$$

$$
= 2 \Re \left\{\alpha^ {*} \operatorname{vec} ^ {H} \left\{\dot {\mathbf {Q}} \mathbf {W} \mathbf {S} \right\} \mathbf {R} _ {\mathrm{n}} ^ {- 1} ([ 1, j ] \otimes \operatorname{vec} \left\{\mathbf {Q} \mathbf {W} \mathbf {S} \right\}) \right\} \tag {13b}
$$

$$
= 2 \Re \left\{\alpha^ {*} \operatorname{vec} ^ {H} \left\{\dot {\mathbf {Q}} \mathbf {W S} \right\} \mathbf {R} _ {\mathrm{n}} ^ {- 1} \operatorname{vec} \left\{\mathbf {Q W S} \right\} [ 1, j ] \right\} \tag {13c}
$$

$$
= 2 L \Re \left\{\alpha^ {*} \operatorname{Tr} \left\{\mathbf {Q W W} ^ {H} \dot {\mathbf {Q}} ^ {H} \widetilde {\mathbf {R}} _ {\mathrm{n}} ^ {- 1} \right\} [ 1, j ] \right\}, \tag {13d}
$$

$$
\mathbf {M} _ {\boldsymbol {\alpha} \boldsymbol {\alpha}} = 2 \Re \left\{\frac {\partial \mathbf {y} ^ {H}}{\partial \boldsymbol {\alpha}} \mathbf {R} _ {\mathrm{n}} ^ {- 1} \frac {\partial \mathbf {y}}{\partial \boldsymbol {\alpha}} \right\} \tag {14a}
$$

$$
= 2 \Re \{([ 1, j ] \otimes \operatorname{vec} \{\mathbf {Q W S} \}) ^ {H} \mathbf {R} _ {\mathrm{n}} ^ {- 1} \tag {14b}
$$

$$
\times ([ 1, \jmath ] \otimes \operatorname{vec} \{\mathbf {Q W S} \}) \}
$$

$$
\begin{array}{l} = 2 \Re \{([ 1, j ] ^ {H} [ 1, j ]) \otimes (\mathrm{vec} ^ {H} \{\mathbf {Q W S} \}) (14c) \\ \times (\mathbf {I} _ {L} \otimes \widetilde {\mathbf {R}} _ {\mathrm{n}} ^ {- 1}) \mathrm{vec} \{\mathbf {Q W S} \}) \} \\ = 2 \Re \left\{\left([ 1, j ] ^ {H} [ 1, j ]\right) \otimes \operatorname{Tr} \left\{\mathbf {Q W S S} ^ {H} \mathbf {W} ^ {H} \mathbf {Q} ^ {H} \widetilde {\mathbf {R}} _ {\mathrm{n}} ^ {- 1} \right\} \right\} (14d) \\ = 2 L \operatorname{Tr} \left\{\mathbf {Q} \mathbf {W} \mathbf {W} ^ {H} \mathbf {Q} ^ {H} \widetilde {\mathbf {R}} _ {\mathrm{n}} ^ {- 1} \right\} \mathbf {I} _ {2}. (14e) \\ \end{array}
$$

After the complete derivation of FIM, the CRB for the $_ { i - }$ th parameter to be estimated (i.e., the i-th element of ξ) can be found as the $( i , i )$ -th element of the inverse of M [42]. In the considered scenario, the dual-functional BS performs a radar function to sense the target’s direction. Thus we are more interested in estimating the target’s $\mathrm { D o A } , ^ { 1 }$ i.e. the parameter θ which is the first element of ξ. Therefore, substituting the results in (12), (13) and (14) and applying the inverse matrix definition of a partitioned matrix, the CRB for estimating the target’s DoA θ can be denoted as [44]

$$
\begin{array}{l} \mathrm{CRB} _ {\theta} \\ = \left[ \mathbf {M} ^ {- 1} \right] _ {1, 1} = \left[ \mathbf {M} _ {\theta \theta} - \mathbf {M} _ {\theta \alpha} \mathbf {M} _ {\alpha \alpha} ^ {- 1} \mathbf {M} _ {\theta \alpha} ^ {T} \right] ^ {- 1} \\ = \frac {1}{2 L | \alpha | ^ {2} \left(\operatorname{Tr} \left\{\dot {\mathbf {Q}} \mathbf {W} \mathbf {W} ^ {H} \dot {\mathbf {Q}} ^ {H} \widetilde {\mathbf {R}} _ {\mathrm{n}} ^ {- 1} \right\} - \frac {\left| \operatorname{Tr} \left\{\mathbf {Q} \mathbf {W} \mathbf {W} ^ {H} \dot {\mathbf {Q}} ^ {H} \widetilde {\mathbf {R}} _ {\mathrm{n}} ^ {- 1} \right\} \right| ^ {2}}{\operatorname{Tr} \left\{\mathbf {Q} \mathbf {W} \mathbf {W} ^ {H} \mathbf {Q} ^ {H} \widetilde {\mathbf {R}} _ {\mathrm{n}} ^ {- 1} \right\}}\right)}. \tag {15} \\ \end{array}
$$

# C. Problem Formulation

In this paper, we aim at minimizing the CRB for estimating the target’s DoA θ by jointly designing transmit precoding W and active RIS reflection beamforming ϕ to improve the radar parameter estimation performance while assuring the QoS requirements of communication users. Consequently, the optimization problem can be formulated as

$$
\min _ {\mathbf {W}, \phi} \quad \mathrm{CRB} _ {\theta} \tag {16a}
$$

$$
\text { s.t. } \quad \| \mathbf {W} \| _ {F} ^ {2} \leq P _ {\mathrm{BS}}, \tag {16b}
$$

$$
\mathcal {P} (\mathbf {W}, \phi) \leq P _ {\mathrm{RIS}}, \tag {16c}
$$

$$
\mathrm{SINR} _ {k} \geq \gamma_ {k}, \forall k, \tag {16d}
$$

$$
a _ {m} \leq a _ {\max}, \forall m, \tag {16e}
$$

where $\mathcal { P } ( \mathbf { W } , \phi )$ is the power consumption at the active RIS, denoted as

$$
\begin{array}{l} \mathcal {P} (\mathbf {W}, \phi) = \| \boldsymbol {\Phi} \mathbf {G} \mathbf {W} \| _ {F} ^ {2} + \sigma_ {\mathrm{t}} ^ {2} \| \boldsymbol {\Phi} \mathbf {h} _ {\mathrm{r}, \mathrm{t}} \mathbf {h} _ {\mathrm{r}, \mathrm{t}} ^ {T} \boldsymbol {\Phi} \mathbf {G} \mathbf {W} \| _ {F} ^ {2} \\ + \sigma_ {\mathrm{t}} ^ {2} \sigma_ {\mathrm{z}} ^ {2} \| \boldsymbol {\Phi} \mathbf {h} _ {\mathrm{r}, \mathrm{t}} \mathbf {h} _ {\mathrm{r}, \mathrm{t}} ^ {T} \boldsymbol {\Phi} \| _ {F} ^ {2} + 2 \sigma_ {\mathrm{z}} ^ {2} \| \boldsymbol {\Phi} \| _ {F} ^ {2}. \tag {17} \\ \end{array}
$$

Moreover, (16b) and (16c) represent the power constraints, where $P _ { \mathrm { B S } }$ and $P _ { \mathrm { R I S } }$ are the power budgets at the BS/active RIS, respectively. In general, the transmit power budget of the BS is greater than the amplification power budget of the active RIS, varying between $2 0 \ \sim \ 5 0$ dBm and $0 \sim 1 0$ dBm, respectively. The specific values of $P _ { \mathrm { B S } }$ and PRIS for simulation studies will be provided in Section IV. (16d) guarantees the worst-case user’s communication SINR γk and (16e) is the maximum amplitude constraint of the

1Considering factors such as application scenarios, resource limitations, and algorithm complexity, in this initial work, we focus exclusively on CRB optimization for DoA estimation. The CRB optimization for RCS/range estimation will be investigated in our future work.

active RIS. The complicated expression with fractional terms and the coupling of optimization variables in both objective function and constraints make problem (16) non-convex and highly challenging to solve. To overcome these difficulties, we propose to alternatively optimize the sub-problems on each variable.

# III. JOINT TRANSMIT PRECODING AND RIS REFLECTION BEAMFORMING DESIGN

# A. Objective Transformation

According to the expression of $\mathrm { C R } \mathbf { B } _ { \theta }$ in (15), minimizing $\mathrm { C R } \mathbf { B } _ { \theta }$ is equivalent to maximizing its denominator, and thereby we can reasonably transform the original objective function in (16) into

$$
\begin{array}{l} \max _ {\mathbf {W}, \phi} g (\mathbf {W}, \phi) \triangleq \operatorname{Tr} \left\{\dot {\mathbf {Q}} \mathbf {W} \mathbf {W} ^ {H} \dot {\mathbf {Q}} ^ {H} \widetilde {\mathbf {R}} _ {\mathrm{n}} ^ {- 1} \right\} \\ - \frac {\left| \operatorname{Tr} \left\{\mathbf {Q W W} ^ {H} \dot {\mathbf {Q}} ^ {H} \widetilde {\mathbf {R}} _ {\mathrm{n}} ^ {- 1} \right\} \right| ^ {2}}{\operatorname{Tr} \left\{\mathbf {Q W W} ^ {H} \mathbf {Q} ^ {H} \widetilde {\mathbf {R}} _ {\mathrm{n}} ^ {- 1} \right\}}. \tag {18} \\ \end{array}
$$

In the following, we alternately design the transmit precoding W and the active RIS beamforming $\phi$ to maximize the objective function $g ( \mathbf { W } , \phi )$ for improving CRB performance.

# B. Transmit Precoding W Design

With fixed active RIS reflection beamforming vector $\phi ,$ the sub-problem for optimizing W can be formulated as

$$
\max _ {\mathbf {W}} g (\mathbf {W}) \tag {19a}
$$

$$
\text { s.t. } \quad \sum_ {i = 1} ^ {K + N} \| \mathbf {w} _ {i} \| _ {2} ^ {2} \leq P _ {\mathrm{BS}}, \tag {19b}
$$

$$
\sum_ {i = 1} ^ {K + N} \mathrm{Tr} \{\mathbf {w} _ {i} \mathbf {w} _ {i} ^ {H} \mathbf {E} \} \leq P _ {\mathrm{RIS}} - c _ {\mathrm{r}}, \tag {19c}
$$

$$
(1 + \gamma_ {k} ^ {- 1}) \mathbf {h} _ {k} ^ {T} \mathbf {w} _ {k} \mathbf {w} _ {k} ^ {H} \mathbf {h} _ {k} ^ {*} \tag {19d}
$$

$$
\geq \sum_ {i = 1} ^ {K + N} \mathbf {h} _ {k} ^ {T} \mathbf {w} _ {i} \mathbf {w} _ {i} ^ {H} \mathbf {h} _ {k} ^ {*} + c _ {\mathrm{s}}, \forall k,
$$

where for clarity we define

$$
\mathbf {E} \triangleq \mathbf {G} ^ {H} \boldsymbol {\Phi} ^ {H} \boldsymbol {\Phi} \mathbf {G} + \sigma_ {\mathrm{t}} ^ {2} \mathbf {G} ^ {H} \boldsymbol {\Phi} ^ {H} \mathbf {h} _ {\mathrm{r}, \mathrm{t}} ^ {*} \mathbf {h} _ {\mathrm{r}, \mathrm{t}} ^ {H} \boldsymbol {\Phi} ^ {H} \boldsymbol {\Phi} \mathbf {h} _ {\mathrm{r}, \mathrm{t}} \mathbf {h} _ {\mathrm{r}, \mathrm{t}} ^ {T} \boldsymbol {\Phi} \mathbf {G}, \tag {20a}
$$

$$
c _ {\mathrm{r}} \triangleq \sigma_ {\mathrm{t}} ^ {2} \sigma_ {\mathrm{z}} ^ {2} \| \boldsymbol {\Phi} \mathbf {h} _ {\mathrm{r}, \mathrm{t}} \mathbf {h} _ {\mathrm{r}, \mathrm{t}} ^ {T} \boldsymbol {\Phi} \| _ {F} ^ {2} + 2 \sigma_ {\mathrm{z}} ^ {2} \| \boldsymbol {\Phi} \| _ {F} ^ {2}, \tag {20b}
$$

$$
c _ {\mathrm{s}} \triangleq \| \mathbf {h} _ {\mathrm{r}, k} ^ {T} \boldsymbol {\Phi} \| _ {2} ^ {2} \sigma_ {\mathrm{z}} ^ {2} + \sigma_ {k} ^ {2}. \tag {20c}
$$

In particular, $g ( \mathbf { W } )$ is a complicated expression with fractional term and higher-order term with respect to W. In order to address the above issues, we propose to introduce a lowerbound for g(W) rather than directly optimizing it, and then invoke the Schur complement and SDR method to effectively solve the sub-problem.

Specifically, we introduce an auxiliary variable $t _ { \mathrm { w } }$ and favorably represent problem (19) as

$$
\max _ {\mathbf {W}, t _ {\mathrm{w}}} \quad t _ {\mathrm{w}} \tag {21a}
$$

$$
\text { s.t. } \quad g (\mathbf {W}) \geq t _ {\mathrm{w}}, \tag {21b}
$$

$$
\sum_ {i = 1} ^ {K + N} \| \mathbf {w} _ {i} \| _ {2} ^ {2} \leq P _ {\mathrm{BS}}, \tag {21c}
$$

$$
\sum_ {i = 1} ^ {K + N} \mathrm{Tr} \{\mathbf {w} _ {i} \mathbf {w} _ {i} ^ {H} \mathbf {E} \} \leq P _ {\mathrm{RIS}} - c _ {\mathrm{r}}, \tag {21d}
$$

$$
\begin{array}{l} (1 + \gamma_ {k} ^ {- 1}) \mathbf {h} _ {k} ^ {T} \mathbf {w} _ {k} \mathbf {w} _ {k} ^ {H} \mathbf {h} _ {k} ^ {*} \\ \geq \sum_ {i = 1} ^ {K + N} \mathbf {h} _ {k} ^ {T} \mathbf {w} _ {i} \mathbf {w} _ {i} ^ {H} \mathbf {h} _ {k} ^ {*} + c _ {\mathrm{s}}, \forall k. \tag {21e} \\ \end{array}
$$

The constraint in (21b) can be further converted into the below semidefinite form via the Schur complement:

$$
\left[ \begin{array}{c c} \operatorname{Tr} \{\dot {\mathbf {Q}} \mathbf {W} \mathbf {W} ^ {H} \dot {\mathbf {Q}} ^ {H} \widetilde {\mathbf {R}} _ {\mathrm{n}} ^ {- 1} \} - t _ {\mathrm{w}} & \operatorname{Tr} \{\mathbf {Q} \mathbf {W} \mathbf {W} ^ {H} \dot {\mathbf {Q}} ^ {H} \widetilde {\mathbf {R}} _ {\mathrm{n}} ^ {- 1} \} \\ \operatorname{Tr} \{\widetilde {\mathbf {R}} _ {\mathrm{n}} ^ {- 1} \dot {\mathbf {Q}} \mathbf {W} \mathbf {W} ^ {H} \mathbf {Q} ^ {H} \} & \operatorname{Tr} \{\mathbf {Q} \mathbf {W} \mathbf {W} ^ {H} \mathbf {Q} ^ {H} \widetilde {\mathbf {R}} _ {\mathrm{n}} ^ {- 1} \} \end{array} \right] \succeq \mathbf {0}. \tag {22}
$$

It is easy to see that the constraints (21e) and (22) are still non-convex with respect to variable W and hard to tackle. Therefore, we propose to convert the optimization variable and further utilize the SDR algorithm for an easier solution. Specifically, by defining

$$
\mathbf {W} _ {i} \triangleq \mathbf {w} _ {i} \mathbf {w} _ {i} ^ {H}, i = 1, \dots , K + N, \tag {23a}
$$

$$
\mathbf {R} _ {\mathrm{w}} \triangleq \sum_ {i = 1} ^ {K + N} \mathbf {W} _ {i} = \mathbf {W} \mathbf {W} ^ {H}, \tag {23b}
$$

the quadratic terms $\mathbf { w } _ { i } \mathbf { w } _ { i } ^ { H } , \ \forall i$ and $\mathbf { W W } ^ { H }$ are transformed into the forms related to primary variables $\mathbf { W } _ { i } , \ \forall i$ and ${ \mathbf { R } } _ { \mathrm { w } }$ . Meanwhile, these rank-one Hermitian positive semidefinite matrices $\mathbf { W } _ { i } , \mathbf { \Pi } \forall i ,$ and the Hermitian positive semidefinite matrix $\mathbf { R } _ { \mathrm { w } }$ should satisfy

$$
\mathbf {W} _ {i} = \mathbf {W} _ {i} ^ {H}, \mathbf {W} _ {i} \succeq \mathbf {0}, \operatorname{rank} \{\mathbf {W} _ {i} \} = 1, \forall i, \tag {24a}
$$

$$
\mathbf {R} _ {\mathrm{w}} = \mathbf {R} _ {\mathrm{w}} ^ {H}, \mathbf {R} _ {\mathrm{w}} \succeq \mathbf {0}. \tag {24b}
$$

It is worth noting that the individual matrices $\mathbf { W } _ { i } ,$ $i = K + 1 , \ldots , K + N$ have no impact on problem (21), and are contained in the matrix $\mathbf { R } _ { \mathrm { w } }$ . Accordingly, we propose to remove these optimization variables to simplify the transformed optimization problem. Moreover, the rank-one constraint in (24a) poses a significant obstacle to finding a straightforward solution, thus, we apply SDR algorithm to relax it. As a result, problem (21) can be converted into

$$
\max _ {\mathbf {W} _ {i}, i = 1, \dots , K, \mathbf {R} _ {\mathrm{w}}, t _ {\mathrm{w}}} t _ {\mathrm{w}} \tag {25a}
$$

$$
\begin{array}{l} \text {s.t.} \left[ \begin{array}{c c} \operatorname{Tr} \left\{\dot {\mathbf {Q}} \mathbf {R} _ {\mathrm{w}} \dot {\mathbf {Q}} ^ {H} \widetilde {\mathbf {R}} _ {\mathrm{n}} ^ {- 1} \right\} - t _ {\mathrm{w}} & \operatorname{Tr} \left\{\mathbf {Q} \mathbf {R} _ {\mathrm{w}} \dot {\mathbf {Q}} ^ {H} \widetilde {\mathbf {R}} _ {\mathrm{n}} ^ {- 1} \right\} \\ \operatorname{Tr} \left\{\widetilde {\mathbf {R}} _ {\mathrm{n}} ^ {- 1} \dot {\mathbf {Q}} \mathbf {R} _ {\mathrm{w}} \mathbf {Q} ^ {H} \right\} & \operatorname{Tr} \left\{\mathbf {Q} \mathbf {R} _ {\mathrm{w}} \mathbf {Q} ^ {H} \widetilde {\mathbf {R}} _ {\mathrm{n}} ^ {- 1} \right\} \end{array} \right] \\ \succeq \mathbf {0}, \end{array} \tag {25b}
$$

$$
\mathrm{Tr} \{\mathbf {R} _ {\mathrm{w}} \} \leq P _ {\mathrm{BS}}, \tag {25c}
$$

$$
\mathrm{Tr} \{\mathbf {R} _ {\mathrm{w}} \mathbf {E} \} \leq P _ {\mathrm{RIS}} - c _ {\mathrm{r}}, \tag {25d}
$$

$$
(1 + \gamma_ {k} ^ {- 1}) \mathbf {h} _ {k} ^ {T} \mathbf {W} _ {k} \mathbf {h} _ {k} ^ {*} \geq \mathbf {h} _ {k} ^ {T} \mathbf {R} _ {\mathrm{w}} \mathbf {h} _ {k} ^ {*} + c _ {\mathrm{s}}, \forall k, (2 5 e)
$$

$$
\mathbf {W} _ {i} = \mathbf {W} _ {i} ^ {H}, \mathbf {W} _ {i} \succeq \mathbf {0}, i = 1, \dots , K, \tag {25f}
$$

$$
\mathbf {R} _ {\mathrm{w}} = \mathbf {R} _ {\mathrm{w}} ^ {H}, \mathbf {R} _ {\mathrm{w}} \succeq \mathbf {0}, \tag {25g}
$$

$$
\mathbf {R} _ {\mathrm{w}} - \sum_ {i = 1} ^ {K} \mathbf {W} _ {i} \succeq \mathbf {0}. \tag {25h}
$$

Clearly, problem (25) is a convex problem and can be easily solved by standard convex optimization algorithms. After obtaining an optimal solution $\mathbf { W } _ { i } , \ i \ = \ 1 , \dots , K$ and ${ \mathbf { R } } _ { \mathrm { w } }$ of (25), the optimal communication beamforming vectors $\mathbf { w } _ { i } , \ i = 1 , \dots , K$ can be recovered as

$$
\mathbf {w} _ {i} = (\mathbf {h} _ {i} ^ {T} \mathbf {R} _ {\mathrm{w}} \mathbf {h} _ {i} ^ {*}) ^ {- 1 / 2} \mathbf {R} _ {\mathrm{w}} \mathbf {h} _ {i} ^ {*}, i = 1, \dots , K. \tag {26}
$$

The proof of (26) is given in detail in [5].

On the other hand, the radar beamforming vectors $\mathbf { w } _ { i } , i = K + 1 , \ldots , K + N$ can be calculated by the Cholesky decomposition, i.e.,

$$
\mathbf {W} _ {\mathrm{r}} \mathbf {W} _ {\mathrm{r}} ^ {H} = \mathbf {R} _ {\mathrm{w}} - \sum_ {i = 1} ^ {K} \mathbf {W} _ {i}, \tag {27}
$$

where $\mathbf { W } _ { \mathrm { r } } ~ = ~ \left[ \mathbf { w } _ { K + 1 } , \ldots , \mathbf { w } _ { K + N } \right]$ . Finally, by combining $\mathbf { W } = [ \mathbf { w } _ { 1 } , \cdots , \mathbf { w } _ { K + N } ]$ , the optimal transmit precoding can be achieved.

# C. Active RIS Reflection Beamforming ϕ Design

After obtaining transmit precoding W, we focus on the subproblem of optimizing the active RIS reflection coefficients $\phi .$ As demonstrated in (18), the quadratic term $\widetilde { \mathbf { R } } _ { \mathrm { n } }$ on $\phi$ exists in $g ( \phi )$ in the form of an inverse, which is extremely challenging to optimize. To address this difficulty, we propose to first introduce an auxiliary variable $\Psi$ to take $\widetilde { \mathbf { R } } _ { \mathrm { n } }$ out of the objective function, and then iteratively update the variables $\phi$ and Ψ until the convergence is achieved.

1) Update $\phi \colon$ Specifically, the optimization with respect to $\phi$ is formulated as

$$
\max _ {\phi} g (\phi) \tag {28a}
$$

$$
\text { s.t. } \quad \mathcal {P} (\phi) \leq P _ {\mathrm{RIS}}, \tag {28b}
$$

$$
\mathrm{SINR} _ {k} \geq \gamma_ {k}, \forall k, \tag {28c}
$$

$$
a _ {m} \leq a _ {\max}, \forall m. \tag {28d}
$$

In order to promote the algorithm development, we start by reformulating the original problem as an explicit problem with respect to ϕ, i.e.,

$$
\min _ {\phi} \frac {\boldsymbol {\xi} _ {1} ^ {H} \mathbf {v v} ^ {H} \boldsymbol {\Xi} _ {1} \mathbf {v}}{\phi^ {H} \mathbf {R} _ {2} \phi} + \frac {\boldsymbol {\xi} _ {2} ^ {H} \mathbf {v v} ^ {H} \boldsymbol {\Xi} _ {2} \mathbf {v}}{\phi^ {H} \mathbf {R} _ {1} \phi} - \mathbf {v} ^ {H} \mathbf {F v} \tag {29a}
$$

$$
\text { s.t. } \quad \phi^ {H} \mathbf {J} \phi \phi^ {H} \phi + \sigma_ {\mathrm{t}} ^ {2} \sigma_ {\mathrm{z}} ^ {2} \alpha_ {\mathrm{r}, \mathrm{t}} ^ {4} (\phi^ {H} \phi) ^ {2} \tag {29b}
$$

$$
+ \phi^ {H} \mathbf {K} \phi \leq P _ {\mathrm{RIS}},
$$

$$
\phi^ {H} \mathbf {C} _ {k} \phi + \Re \{\mathbf {d} _ {k} ^ {H} \phi \} + c _ {\phi , k} \tag {29c}
$$

$$
- (1 + \gamma_ {k} ^ {- 1}) \boldsymbol {\phi} ^ {H} \mathbf {b} _ {k, k} ^ {*} \mathbf {b} _ {k, k} ^ {T} \boldsymbol {\phi} \leq 0, \forall k,
$$

$$
a _ {m} \leq a _ {\max}, \forall m, \tag {29d}
$$

where $\begin{array} { c c c c c c } { { { \bf v } } } & { { \triangleq } } & { { \mathrm { v e c } \{ \phi \phi ^ { H } \} } } & { { = } } & { { \phi ^ { \ast } \otimes \phi } } \end{array}$ . The proof of equivalence between objective functions (28a) and (29a) is presented in Appendix A. For ease of notation, in (29) we define

$$
\mathbf {R} _ {1} \triangleq \mathbf {A} ^ {H} \mathbf {G} ^ {*} \mathbf {W} ^ {*} \mathbf {W} ^ {T} \mathbf {G} ^ {T} \mathbf {A}, \tag {30a}
$$

$$
\mathbf {R} _ {2} \triangleq \mathbf {A} ^ {H} \mathbf {G} ^ {*} \boldsymbol {\Psi} ^ {- 1} \mathbf {G} ^ {T} \mathbf {A}, \tag {30b}
$$

$$
\boldsymbol {\xi} _ {i} \triangleq \operatorname{vec} \left\{\mathbf {R} _ {i} ^ {H} \right\}, i = 1, 2, \tag {30c}
$$

$$
\boldsymbol {\Xi} _ {i} \triangleq \mathbf {L R} _ {\hat {i}} ^ {T} \otimes \mathbf {L R} _ {\hat {i}}, \forall i, \hat {i} \neq i, \tag {30d}
$$

$$
\mathbf {F} _ {i} \triangleq \mathbf {L R} _ {\hat {i}} ^ {T} \mathbf {L} \otimes \mathbf {R} _ {i}, \forall i, \hat {i} \neq i, \tag {30e}
$$

$$
\mathbf {F} \triangleq \mathbf {F} _ {1} + \mathbf {F} _ {2}, \tag {30f}
$$

$$
\mathbf {J} \triangleq \sigma_ {\mathrm{t}} ^ {2} \alpha_ {\mathrm{r}, \mathrm{t}} ^ {2} \operatorname{diag} \left\{\mathbf {h} _ {\mathrm{r}, \mathrm{t}} ^ {*} \right\} \mathbf {G} ^ {*} \mathbf {W} ^ {*} \mathbf {W} ^ {T} \mathbf {G} ^ {T} \operatorname{diag} \left\{\mathbf {h} _ {\mathrm{r}, \mathrm{t}} \right\}, \tag {30g}
$$

$$
\mathbf {K} \triangleq \sum_ {k = 1} ^ {K + N} \operatorname{diag} \left\{\mathbf {G} ^ {*} \mathbf {w} _ {k} ^ {*} \right\} \operatorname{diag} \left\{\mathbf {G} \mathbf {w} _ {k} \right\} + 2 \sigma_ {\mathrm{z}} ^ {2} \mathbf {I} _ {M}, \tag {30h}
$$

$$
\mathbf {C} _ {k} \triangleq \sum_ {i = 1} ^ {K + N} \mathbf {b} _ {k, i} ^ {*} \mathbf {b} _ {k, i} ^ {T} + \sigma_ {\mathrm{z}} ^ {2} \operatorname{diag} \left\{\mathbf {h} _ {\mathrm{r}, k} ^ {H} \right\} \operatorname{diag} \left\{\mathbf {h} _ {\mathrm{r}, k} \right\}, \tag {30i}
$$

$$
\mathbf {d} _ {k} \triangleq \sum_ {i = 1} ^ {K + N} 2 a _ {k, i} \mathbf {b} _ {k, i} ^ {*} - 2 (1 + \gamma_ {k} ^ {- 1}) a _ {k, k} \mathbf {b} _ {k, k} ^ {*}, \tag {30j}
$$

$$
c _ {\phi , k} \triangleq \sum_ {i = 1} ^ {K + N} | a _ {k, i} | ^ {2} - (1 + \gamma_ {k} ^ {- 1}) | a _ {k, k} | ^ {2} + \sigma_ {k} ^ {2}, \tag {30k}
$$

$$
a _ {k, i} \triangleq \mathbf {h} _ {\mathrm{d}, k} ^ {T} \mathbf {w} _ {i}, \quad \mathbf {b} _ {k, i} \triangleq \operatorname{diag} \left\{\mathbf {G} \mathbf {w} _ {i} \right\} \mathbf {h} _ {\mathrm{r}, k}, \tag {301}
$$

where ˆi represents the element in the set {1, 2} other than $i ,$ i.e., if $i = 1$ then $\hat { i } = 2$ and ${ \mathrm { i f ~ } } i = 2$ then $\ddot { i } = 1$ .

To handle the non-convex fractional terms in (29a), we propose to introduce two auxiliary variables $t _ { 1 }$ and $t _ { 2 }$ to replace them, as shown below:

$$
\min _ {\phi , t _ {1}, t _ {2}} \quad t _ {1} + t _ {2} - \mathbf {v} ^ {H} \mathbf {F} \mathbf {v} \tag {31a}
$$

$$
\text { s.t. } \quad \phi^ {H} \mathbf {J} \phi \phi^ {H} \phi + \sigma_ {\mathrm{t}} ^ {2} \sigma_ {\mathrm{z}} ^ {2} \alpha_ {\mathrm{r}, \mathrm{t}} ^ {4} (\phi^ {H} \phi) ^ {2} \tag {31b}
$$

$$
+ \phi^ {H} \mathbf {K} \phi \leq P _ {\mathrm{RIS}},
$$

$$
\phi^ {H} \mathbf {C} _ {k} \phi + \Re \{\mathbf {d} _ {k} ^ {H} \phi \} + c _ {\phi , k} \tag {31c}
$$

$$
- (1 + \gamma_ {k} ^ {- 1}) \boldsymbol {\phi} ^ {H} \mathbf {b} _ {k, k} ^ {*} \mathbf {b} _ {k, k} ^ {T} \boldsymbol {\phi} \leq 0, \forall k,
$$

$$
t _ {i} \geq \frac {\boldsymbol {\xi} _ {i} ^ {H} \mathbf {v v} ^ {H} \boldsymbol {\Xi} _ {i} \mathbf {v}}{\phi^ {H} \mathbf {R} _ {\hat {i}} \phi}, \forall i, \hat {i} \neq i, \tag {31d}
$$

$$
a _ {m} \leq a _ {\max}, \forall m. \tag {31e}
$$

Obviously, when $\phi$ is given, the problem (31) becomes relevant only for the auxiliary variables $t _ { 1 }$ and $t _ { 2 } .$ . Thus, the optimal solutions $t _ { 1 }$ and $t _ { 2 }$ in each iteration can be obtained as

$$
t _ {i} ^ {\star} = \frac {\boldsymbol {\xi} _ {i} ^ {H} \mathbf {v v} ^ {H} \boldsymbol {\Xi} _ {i} \mathbf {v}}{\phi^ {H} \mathbf {R} _ {\hat {i}} \phi}, \forall i, \hat {i} \neq i. \tag {32}
$$

Furthermore, with optimal $t _ { 1 }$ and $t _ { 2 } .$ , the optimization on $\phi$ can be formulated as solving the following problem:

$$
\min _ {\phi} - \mathbf {v} ^ {H} \mathbf {F} \mathbf {v} \tag {33a}
$$

$$
\text { s.t. } \quad \phi^ {H} \mathbf {J} \phi \phi^ {H} \phi + \sigma_ {\mathrm{t}} ^ {2} \sigma_ {\mathrm{z}} ^ {2} \alpha_ {\mathrm{r}, \mathrm{t}} ^ {4} (\phi^ {H} \phi) ^ {2} \tag {33b}
$$

$$
+ \phi^ {H} \mathbf {K} \phi \leq P _ {\mathrm{RIS}},
$$

$$
\phi^ {H} \mathbf {C} _ {k} \phi + \Re \left\{\mathbf {d} _ {k} ^ {H} \phi \right\} + c _ {\phi , k} \tag {33c}
$$

$$
- \left(1 + \gamma_ {k} ^ {- 1}\right) \boldsymbol {\phi} ^ {H} \mathbf {b} _ {k, k} ^ {*} \mathbf {b} _ {k, k} ^ {T} \boldsymbol {\phi} \leq 0, \forall k,
$$

$$
\boldsymbol {\xi} _ {i} ^ {H} \mathbf {v v} ^ {H} \boldsymbol {\Xi} _ {i} \mathbf {v} - t _ {i} \phi^ {H} \mathbf {R} _ {\hat {i}} \phi \leq 0, \forall i, \hat {i} \neq i, \tag {33d}
$$

$$
a _ {m} \leq a _ {\max}, \forall m. \tag {33e}
$$

Now, the design problem with regard to active RIS reflection coefficients $\phi$ is relatively more straightforward. Nevertheless, due to the existence of the quartic terms with respect to $\phi$ in (33a) and (33b) $( \mathrm { i . e . , ~ } { \bf v } ^ { H } \dot { \bf F } { \bf v } , \ \phi ^ { H } { \bf J } \phi \phi ^ { H } \phi$ and $( \phi ^ { H } \phi ) ^ { 2 } )$ , the non-convex constraint in (33c) and the sextic terms with respect to $\phi$ in (33d) (i.e., $\xi _ { i } ^ { H } \mathbf { v } \mathbf { v } ^ { H } \Xi _ { i } \mathbf { v } )$ , problem (33) is very tough to deal with. To tackle this difficulty, the MM algorithm is utilized to find a series of convex tractable surrogate functions for these non-convex terms via both firstorder Taylor expansion and second-order Taylor expansion, as presented in the following.

Transformation for Objective (33a): Concretely, by using the solution $\phi _ { s }$ obtained in the s-th iteration and applying first-order Taylor expansion, we can derive an upper-bound for $- \mathbf { v } ^ { H } \mathbf { F } \mathbf { v }$ as

$$
- \mathbf {v} ^ {H} \mathbf {F} \mathbf {v} \leq - \mathbf {v} _ {s} ^ {H} \mathbf {F} \mathbf {v} _ {s} - 2 \Re \{\mathbf {v} _ {s} ^ {H} \mathbf {F} (\mathbf {v} - \mathbf {v} _ {s}) \}, \tag {34a}
$$

$$
= \Re \{\mathbf {v} ^ {H} \mathbf {f} \} + c _ {1}, \tag {34b}
$$

$$
= \Re \{\phi^ {H} \widetilde {\mathbf {F}} \phi \} + c _ {1}, \tag {34c}
$$

where we define $\begin{array} { r l r } { \mathbf { f } } & { { } \triangleq } & { - 2 \mathbf { F } ^ { H } \mathbf { v } _ { s } } \end{array}$ and $c _ { \frac { 1 } { s } . } \triangleq \mathbf { v } _ { s } ^ { H } \mathbf { F } \mathbf { v } _ { s }$ is a constant independent of $\phi .$ Besides, $\widetilde { \mathbf { F } }$ is a reshaped matrix form corresponding to the vector f , that $\mathrm { i s } , \ \mathbf { f } \ =$ $\mathrm { v e c } \{ \widetilde { \mathbf { F } } \}$ . Nevertheless, the real-valued function $\Re \{ \phi ^ { H } \widetilde { \mathbf { F } } \phi \}$ is still non-convex. Moreover, we suggest re-writing expression $\Re \{ \phi ^ { H } \widetilde { \mathbf { F } } \phi \}$ in the form of real-valued variables and further find a tractable upper-bound for it via the second-order Taylor expansion. In particular, with the definitions

$$
\bar {\phi} \triangleq \left[ \Re \{\phi^ {T} \} \quad \Im \{\phi^ {T} \} \right] ^ {T}, \tag {35a}
$$

$$
\bar {\mathbf {F}} \triangleq \left[ \begin{array}{c c} \Re \{\widetilde {\mathbf {F}} \} & - \Im \{\widetilde {\mathbf {F}} \} \\ \Im \{\widetilde {\mathbf {F}} \} & \Re \{\widetilde {\mathbf {F}} \} \end{array} \right], \tag {35b}
$$

we have

$$
\Re \{\phi^ {H} \widetilde {\mathbf {F}} \phi \} = \bar {\phi} ^ {T} \bar {\mathbf {F}} \bar {\phi}, \tag {36a}
$$

$$
\leq \bar {\phi} _ {s} ^ {T} \bar {\mathbf {F}} \bar {\phi} _ {s} + \bar {\phi} _ {s} ^ {T} (\bar {\mathbf {F}} + \bar {\mathbf {F}} ^ {T}) (\bar {\phi} - \bar {\phi} _ {s}) \tag {36b}
$$

$$
+ \frac {\widetilde {\lambda} _ {1}}{2} (\bar {\phi} - \bar {\phi} _ {s}) ^ {T} (\bar {\phi} - \bar {\phi} _ {s}),
$$

$$
= \frac {\widetilde {\lambda} _ {1}}{2} \phi^ {H} \phi + \Re \left\{\phi^ {H} \widetilde {\mathbf {f}} \right\} - \bar {\phi} _ {s} ^ {T} \bar {\mathbf {F}} ^ {T} \bar {\phi} _ {s} + \frac {\widetilde {\lambda} _ {1}}{2} \bar {\phi} _ {s} ^ {T} \bar {\phi} _ {s}, \tag {36c}
$$

in which we define $\widetilde { \lambda } _ { 1 }$ as the maximum eigenvalue of Hessian matrix $( \bar { \mathbf { F } } + \bar { \mathbf { F } } ^ { T } ) , \widetilde { \mathbf { f } } \triangleq \mathbf { U } ( \bar { \mathbf { F } } + \bar { \mathbf { F } } ^ { T } - \widetilde { \lambda } _ { 1 } ^ { - } \mathbf { I } _ { 2 M } ) \widetilde { \boldsymbol { \phi } } _ { s }$ and $\textbf { U } \triangleq$ $\left[ \mathbf { I } _ { M } \mathbf { \Omega } \mathcal { M } \right]$ . By substituting (36) into (34), a convex surrogate function of $- \mathbf { v } ^ { H } \mathbf { F } \mathbf { v }$ can be obtained as

$$
- \mathbf {v} ^ {H} \mathbf {F} \mathbf {v} \leq \frac {\widetilde {\lambda} _ {1}}{2} \phi^ {H} \phi + \Re \{\phi^ {H} \widetilde {\mathbf {f}} \} + c _ {2}, \tag {37}
$$

where $\begin{array} { r } { c _ { 2 } \triangleq - \bar { \phi } _ { s } ^ { T } \bar { \mathbf { F } } ^ { T } \bar { \phi } _ { s } + \frac { \widetilde { \lambda } _ { 1 } } { 2 } \bar { \phi } _ { s } ^ { T } \bar { \phi } _ { s } + c _ { 1 } . } \end{array}$

Transformation for Constraint (33b): Now, the objective (33a) is tractable, we then consider handling the constraints (33b)-(33d). Thanks to the amplitude constraint of active RIS, i.e., $a _ { m } \leq a _ { \mathrm { m a x } } , \phi ^ { H } \phi$ is upper-bounded by $\phi ^ { H } \phi \leq M a _ { \operatorname* { m a x } } ^ { 2 }$ . Therefore, the power constraint of the active RIS can be written as

$$
\phi^ {H} \mathbf {J} \phi \phi^ {H} \phi + \sigma_ {\mathrm{t}} ^ {2} \sigma_ {\mathrm{z}} ^ {2} \alpha_ {\mathrm{r,t}} ^ {4} (\phi^ {H} \phi) ^ {2} + \phi^ {H} \mathbf {K} \phi
$$

$$
\leq \phi^ {H} \widetilde {\mathbf {K}} \phi + c _ {3} \leq P _ {\mathrm{RIS}}, \tag {38}
$$

with $\widetilde { \mathbf { K } } \triangleq \mathbf { K } + M a _ { \mathrm { m a x } } ^ { 2 } \mathbf { J }$ and $c _ { 3 } \triangleq \sigma _ { \mathrm { t } } ^ { 2 } \sigma _ { \mathrm { z } } ^ { 2 } \alpha _ { \mathrm { r , t } } ^ { 4 } M ^ { 2 } a _ { \mathrm { m a x } } ^ { 4 }$

Transformation for Constraint (33c): It is obvious that the presence of the concave term $- ( 1 + \gamma _ { k } ^ { - 1 } ) \boldsymbol { \phi } ^ { H } \mathbf { b } _ { k , k } ^ { * } \mathbf { b } _ { k , k } ^ { T } \boldsymbol { \phi }$ k,k causes the constraint (33c) to be non-convex. Particularly, a linear surrogate function for it can be derived as

$$
- \phi^ {H} \mathbf {b} _ {k, k} ^ {*} \mathbf {b} _ {k, k} ^ {T} \phi \leq - \phi_ {s} ^ {H} \mathbf {b} _ {k, k} ^ {*} \mathbf {b} _ {k, k} ^ {T} \phi_ {s}
$$

$$
- 2 \Re \{\phi_ {s} ^ {H} \mathbf {b} _ {k, k} ^ {*} \mathbf {b} _ {k, k} ^ {T} (\phi - \phi_ {s}) \}. \tag {39}
$$

On the basis of the result in (39), we can obtain an upperbound function for $- ( 1 + \gamma _ { k } ^ { - 1 } ) \phi ^ { H } \mathbf { b } _ { k , k } ^ { * } \mathbf { b } _ { k , k } ^ { T } \phi$ and re-arrange the SINR constraint as

$$
\phi^ {H} \mathbf {C} _ {k} \phi + \Re \{\widetilde {\mathbf {d}} _ {k} ^ {H} \phi \} + \tilde {c} _ {\phi , k} \leq 0, \forall k, \tag {40}
$$

where for brevity we define $\begin{array} { r l r } { \widetilde { { \bf d } } _ { k } ^ { H } } & { { } \triangleq } & { { \bf d } _ { k } ^ { H } - 2 ( 1 + } \end{array}$ $\gamma _ { k } ^ { - 1 } ) \phi _ { s } ^ { H } \mathbf { b } _ { k , k } ^ { * } \mathbf { b } _ { k , k } ^ { T }$ and $\tilde { c } _ { \phi , k } \triangleq c _ { \phi , k } + \mathrm { ( 1 + } \gamma _ { k } ^ { - 1 } ) \phi _ { s } ^ { H } \mathbf { b } _ { k , k } ^ { \ast } \mathbf { b } _ { k , k } ^ { T } \phi _ { s }$ H

Transformation for Constraint (33d): Recalling the definition $\begin{array} { r l r } { \bar { \phi } } & { \triangleq } & { \Big \lceil \Re \{ \phi ^ { T } \} \ \Im \{ \phi ^ { T } \} \Big \rceil ^ { T } } \end{array}$ and defining other notations for brevity as follows:

$$
\bar {\boldsymbol {\xi}} _ {i} \triangleq \left[ \Re \{\boldsymbol {\xi} _ {i} ^ {T} \} \quad \Im \{\boldsymbol {\xi} _ {i} ^ {T} \} \right] ^ {T}, \tag {41a}
$$

$$
\bar {\mathbf {v}} \triangleq \left[ \Re \{\mathbf {v} ^ {T} \} \quad \Im \{\mathbf {v} ^ {T} \} \right] ^ {T}, \tag {41b}
$$

$$
\bar {\Xi} _ {i} \triangleq \left[ \begin{array}{c c} \Re \{\widetilde {\Xi} _ {i} \} & - \Im \{\widetilde {\Xi} _ {i} \} \\ \Im \{\widetilde {\Xi} _ {i} \} & \Re \{\widetilde {\Xi} _ {i} \} \end{array} \right], \tag {41c}
$$

the equivalent real-valued form $y _ { i } ( \bar { \mathbf { v } } )$ of the first term $\pmb { \xi } _ { i } ^ { H } \mathbf { v } \mathbf { v } ^ { H } \Xi _ { i } \mathbf { v }$ in (33d) can be expressed as

$$
y _ {i} (\bar {\mathbf {v}}) = \boldsymbol {\xi} _ {i} ^ {H} \mathbf {v} \mathbf {v} ^ {H} \boldsymbol {\Xi} _ {i} \mathbf {v} = \bar {\boldsymbol {\xi}} _ {i} ^ {T} \bar {\mathbf {v}} \bar {\mathbf {v}} ^ {T} \bar {\boldsymbol {\Xi}} _ {i} \bar {\mathbf {v}}, \tag {42}
$$

whose first-order and second-order derivatives can be calculated as

$$
\nabla y _ {i} (\bar {\mathbf {v}}) = \bar {\boldsymbol {\xi}} _ {i} ^ {T} \bar {\mathbf {v}} \left(\bar {\boldsymbol {\Xi}} _ {i} + \bar {\boldsymbol {\Xi}} _ {i} ^ {T}\right) \bar {\mathbf {v}} + \bar {\mathbf {v}} ^ {T} \bar {\boldsymbol {\Xi}} _ {i} \bar {\mathbf {v}} \bar {\boldsymbol {\xi}} _ {i}, \tag {43a}
$$

$$
\nabla^ {2} y _ {i} (\bar {\mathbf {v}}) = \left(\bar {\boldsymbol {\Xi}} _ {i} + \bar {\boldsymbol {\Xi}} _ {i} ^ {T}\right) \bar {\mathbf {v}} \bar {\boldsymbol {\xi}} _ {i} ^ {T} + \left(\bar {\boldsymbol {\xi}} _ {i} \bar {\mathbf {v}} ^ {T} + \bar {\mathbf {v}} ^ {T} \bar {\boldsymbol {\xi}} _ {i} \mathbf {I} _ {2 M ^ {2}}\right) \left(\bar {\boldsymbol {\Xi}} _ {i} + \bar {\boldsymbol {\Xi}} _ {i} ^ {T}\right). \tag {43b}
$$

With $\nabla y _ { i } ( \bar { \mathbf { v } } )$ and $\nabla ^ { 2 } y _ { i } ( \bar { \bf { v } } )$ shown in (43), the upper-bounded surrogate function of $y _ { i } ( \bar { \mathbf { v } } )$ is obtained by

$$
y _ {i} (\bar {\mathbf {v}}) \leq y _ {i} (\bar {\mathbf {v}} _ {s}) + \left(\nabla y _ {i} (\bar {\mathbf {v}} _ {s})\right) ^ {T} (\bar {\mathbf {v}} - \bar {\mathbf {v}} _ {s}) \tag {44a}
$$

$$
+ \frac {\lambda_ {\mathrm{y} , i}}{2} (\bar {\mathbf {v}} - \bar {\mathbf {v}} _ {s}) ^ {T} (\bar {\mathbf {v}} - \bar {\mathbf {v}} _ {s})
$$

$$
= \frac {\lambda_ {y , i}}{2} \bar {\mathbf {v}} ^ {T} \bar {\mathbf {v}} + \bar {\mathbf {v}} ^ {T} \bar {\boldsymbol {\ell}} _ {i} + x _ {i} \tag {44b}
$$

$$
= \frac {\lambda_ {y , i}}{2} \mathbf {v} ^ {H} \mathbf {v} + \Re \left\{\mathbf {v} ^ {H} \boldsymbol {\ell} _ {i} \right\} + x _ {i} \tag {44c}
$$

$$
\leq \Re \{\phi^ {H} \boldsymbol {\Omega} _ {i} \phi \} + \frac {\lambda_ {\mathrm{y} , i}}{2} M ^ {2} a _ {\max} ^ {4} + x _ {i} \tag {44d}
$$

$$
= \bar {\phi} ^ {T} \bar {\Omega} _ {i} \bar {\phi} + \frac {\lambda_ {\mathrm{y} , i}}{2} M ^ {2} a _ {\max} ^ {4} + x _ {i} \tag {44e}
$$

$$
\leq \bar {\phi} _ {s} ^ {T} \bar {\Omega} _ {i} \bar {\phi} _ {s} + \bar {\phi} _ {s} ^ {T} (\bar {\Omega} _ {i} + \bar {\Omega} _ {i} ^ {T}) (\bar {\phi} - \bar {\phi} _ {s}) \tag {44f}
$$

$$
+ \frac {\widetilde {\lambda} _ {\mathrm{y} , i}}{2} (\bar {\phi} - \bar {\phi} _ {s}) ^ {T} (\bar {\phi} - \bar {\phi} _ {s}) + \frac {\lambda_ {\mathrm{y} , i}}{2} M ^ {2} a _ {\max} ^ {4} + x _ {i}
$$

$$
= \frac {\widetilde {\lambda} _ {y , i}}{2} \phi^ {H} \phi + \Re \left\{\phi^ {H} \widetilde {\ell} _ {i} \right\} + \widetilde {x} _ {i}, \tag {44g}
$$

where $\lambda _ { \mathrm { y } , i }$ is the maximum eigenvalue of the Hessian matrix $\begin{array} { r } { \check { \nabla } ^ { 2 } y _ { i } ( \bar { \mathbf { v } } _ { s } ) , ~ \bar { \ell } _ { i } \triangleq \nabla y _ { i } ( \bar { \mathbf { v } } _ { s } ) \stackrel {  } - \lambda _ { \mathrm { y } , i } \bar { \mathbf { v } } _ { s } , ~ x _ { i } \triangleq y _ { i } ( \bar { \mathbf { v } } _ { s } ) ~ - } \end{array}$ $\begin{array} { r } { ( \nabla y _ { i } ( \bar { \mathbf { v } } _ { s } ) ) ^ { T } \bar { \mathbf { v } } _ { s } + \frac { \lambda _ { \mathbf { y } , i } } { 2 } \bar { \mathbf { v } } _ { s } ^ { T } \bar { \mathbf { v } } _ { s } , \ell _ { i } \triangleq \mathbf { U } _ { \mathrm { v } } \bar { \ell } _ { i } = \mathrm { v e c } \{ \Omega _ { i } \} , \mathbf { U } _ { \mathrm { v } } \triangleq } \end{array}$ $\left[ { \bf I } _ { M ^ { 2 } } \ { \mathcal I } _ { M ^ { 2 } } \right]$ $\mathbf { v } ^ { H } \mathbf { v } \ =$ $( \stackrel {  } { \phi ^ { * } } \otimes \stackrel {  } { \phi } ) ^ { \dot { H } } ( \phi ^ { * } \otimes \phi ) \stackrel { \cdot } { = } ( \phi ^ { H } \phi ) ^ { 2 } \leq M ^ { 2 } a _ { \mathrm { m a x } } ^ { 4 }$ . In addition, $\bar { \Omega } _ { i } \triangleq \left\lceil \mathfrak { R } \{ \Omega _ { i } \} - \mathfrak { I } \{ \Omega _ { i } \} \right\rceil , \widetilde { \lambda } _ { \mathrm { y } , i }$ is the maximum eigenvalue of Hessian matrix $( \bar { \boldsymbol { \Omega } _ { i } } + \bar { \boldsymbol { \Omega } _ { i } ^ { T } } ) , \mathcal { \tilde { \ell } } _ { i } \triangleq \mathbf { U } ( \bar { \boldsymbol { \Omega } } _ { i } + \bar { \boldsymbol { \Omega } } _ { i } ^ { T } - \widetilde { \boldsymbol { \lambda } } _ { \mathrm { y } , i } \mathbf { I } _ { 2 M } ) \bar { \boldsymbol { \phi } } _ { s }$ and $\begin{array} { r } { \widetilde { x } _ { i } \triangleq - \bar { \phi } _ { s } ^ { T } \bar { \Omega } _ { i } ^ { T } \bar { \phi } _ { s } + \frac { \widetilde { \lambda } _ { \mathtt { y } , i } } { 2 } \bar { \phi } _ { s } ^ { T } \bar { \phi } _ { s } + \frac { \lambda _ { \mathtt { y } , i } } { 2 } M ^ { 2 } a _ { \operatorname* { m a x } } ^ { 4 } + x _ { i } . } \end{array}$ λy,i2 M 2a4max + xi.

Moreover, a linear surrogate function of $- \phi ^ { H } \mathbf { R } _ { \hat { i } } \phi$ in (33d) can be formulated as

$$
\begin{array}{l} - \phi^ {H} \mathbf {R} _ {\hat {i}} \phi \leq - \phi_ {s} ^ {H} \mathbf {R} _ {\hat {i}} \phi_ {s} - 2 \Re \{\phi_ {s} ^ {H} \mathbf {R} _ {\hat {i}} (\phi - \phi_ {s}) \}, \\ = \Re \left\{\phi^ {H} \varrho_ {i} \right\} + \kappa_ {i}, \tag {45} \\ \end{array}
$$

where we define $\underline { { \underline { { \mathbf { \Pi } } } } } _ { i } \triangleq - 2 \mathbf { R } _ { \widehat { i } } ^ { H } \phi _ { s }$ and ${ \kappa } _ { i } \ \triangleq \ \boldsymbol \phi _ { s } ^ { H } { \bf R } _ { \hat { \imath } } \boldsymbol \phi _ { s }$ s for simplicity. To sum up, we obtain the convex surrogate function for constraint (33d) as

$$
\boldsymbol {\xi} _ {i} ^ {H} \mathbf {v v} ^ {H} \boldsymbol {\Xi} _ {i} \mathbf {v} - t _ {i} \phi^ {H} \mathbf {R} _ {\hat {i}} \phi \leq \frac {\widetilde {\lambda} _ {\mathrm{y} , i}}{2} \phi^ {H} \phi + \Re \left\{\phi^ {H} \widetilde {\varrho} _ {i} \right\} + \widetilde {\kappa} _ {i}, \tag {46}
$$

with $\widetilde { \pmb { \varrho } } _ { i } \triangleq \widetilde { \pmb { \ell } } _ { i } + t _ { i } \pmb { \varrho } _ { i }$ and $\widetilde { \kappa } _ { i } \triangleq \widetilde { x } _ { i } + t _ { i } \kappa _ { i }$ .

e eThus, we can formulate the optimization problem with respect to $\phi$ at the $( s + 1 )$ )-th iteration as

$$
\min _ {\phi} \frac {\widetilde {\lambda} _ {1}}{2} \phi^ {H} \phi + \Re \left\{\phi^ {H} \widetilde {\mathbf {f}} \right\} \tag {47a}
$$

$\begin{array} { r l } { \mathrm { s . t . } } & { { } { \phi ^ { H } } \widetilde { \mathbf { K } } \phi \leq P _ { \mathrm { R I S } } - c _ { 3 } , } \end{array}$ (47b)

$$
\phi^ {H} \mathbf {C} _ {k} \phi + \Re \{\widetilde {\mathbf {d}} _ {k} ^ {H} \phi \} + \tilde {c} _ {\phi , k} \leq 0, \forall k, \tag {47c}
$$

$$
\frac {\widetilde {\lambda} _ {\mathrm{y} , i}}{2} \phi^ {H} \phi + \Re \{\phi^ {H} \widetilde {\varrho} _ {i} \} + \widetilde {\kappa} _ {i} \leq 0, \forall i, \tag {47d}
$$

$$
a _ {m} \leq a _ {\max}, \forall m. \tag {47e}
$$

Obviously, it is a simple convex problem that can be readily solved by various convex algorithms/toolboxes.

2) Update Ψ: With optimal $\phi _ { s + 1 }$ in the $( s + 1 )$ -th iteration, we appropriately update the auxiliary variable $\Psi _ { s + 1 }$ as

$$
\boldsymbol {\Psi} _ {s + 1} = \widetilde {\mathbf {R}} _ {\mathrm{n}} = \sigma_ {\mathrm{z}} ^ {2} \mathbf {G} ^ {T} \boldsymbol {\Phi} _ {s + 1} \boldsymbol {\Phi} _ {s + 1} ^ {H} \mathbf {G} ^ {*} + \sigma_ {\mathrm{r}} ^ {2} \mathbf {I} _ {N}. \tag {48}
$$

Finally, by alternatively updating $t _ { 1 } , t _ { 2 } , \phi$ and Ψ, we can solve the active RIS reflection beamforming optimization problem in an iterative manner.

# D. Summary, Initialization and Computational Complexity Analysis

According to the above derivations, we summarize the proposed joint transmit precoding and active RIS reflection beamforming design for communication QoS-constrained radar CRB minimization problem in Algorithm 1. With a suitable initialization, we can iteratively update each variable until convergence.

In general, the performance and convergence speed of the algorithm based on alternating optimization can be influenced by the initialization. It is essential to select a suitable initial point for the optimization problem. Intuitively, the active RIS is employed to improve the wireless propagation environment between the BS and the target/users. Therefore, channel power gains can be regarded as an appropriate performance metric to initialize ϕ. Specifically, we assume that all the active elements can reach their amplitude maximum $a _ { \mathrm { m a x } }$ and optimize their initialized phase-shifts $\psi \triangleq [ \psi _ { 1 } , \hdots , \psi _ { M } ] ^ { T } \in \mathbb { C } ^ { \hat { M } }$ as follows:

$$
\max _ {\boldsymbol {\psi}} \| \mathbf {h} _ {\mathrm{r}, \mathrm{t}} ^ {T} \operatorname{diag} \{\boldsymbol {\psi} \} \mathbf {G} \| _ {2} ^ {2} + \sum_ {k = 1} ^ {K} \| \mathbf {h} _ {\mathrm{d}, k} ^ {T} + \mathbf {h} _ {\mathrm{r}, k} ^ {T} \operatorname{diag} \{\boldsymbol {\psi} \} \mathbf {G} \| _ {2} ^ {2}
$$

$$
\text { s.t. } \quad | \psi_ {m} | = 1, \forall m. \tag {49}
$$

Algorithm 1 Joint Transmit Precoding and Active RIS Reflection Beamforming Design Algorithm   
Input: $h_{d,k}$ , $h_{r,k}$ , $h_{r,t}$ , G, $P_{BS}$ , $P_{RIS}$ , $\gamma_{k}$ , $a_{max}$ , $\sigma_{k}$ , $\sigma_{z}$ , $\sigma_{r}$ , $\sigma_{t}$ , N, M, K, L, $\forall k$ .

Output: $W^{\star}$ and $\phi^{\star}$ .

1: Initialize $\phi$ .

2: while no convergence do

3: Obtain $W_{i}$ , $i = 1, \ldots, K$ and $R_{w}$ by solving (25);

4: Construct $w_{i}$ , $i = 1, \ldots, K$ by (26);

5: Construct $w_{i}$ , $i = K + 1, \ldots, K + N$ by Cholesky decomposition;

6: Combine $W = [w_{1}, \ldots, w_{K+N}]$ .

7: while no convergence do

8: Calculate $t_{1}$ and $t_{2}$ by (32);

9: Update $\phi$ by solving (47);

10: Update $\Psi$ by (48).

11: end while

12: end while

13: Return $W^{\star} = W$ and $\phi^{\star} = \phi$ .

Moreover, with the following definitions

$$
\mathbf {M} \triangleq \operatorname{diag} \left\{\mathbf {h} _ {\mathrm{r}, \mathrm{t}} ^ {H} \right\} \mathbf {G} ^ {*} \mathbf {G} ^ {T} \operatorname{diag} \left\{\mathbf {h} _ {\mathrm{r}, \mathrm{t}} \right\} \tag {50a}
$$

$$
+ \sum_ {k = 1} ^ {K} \operatorname{diag} \left\{\mathbf {h} _ {\mathrm{r}, k} ^ {H} \right\} \mathbf {G} ^ {*} \mathbf {G} ^ {T} \operatorname{diag} \left\{\mathbf {h} _ {\mathrm{r}, k} \right\},
$$

$$
\mathbf {m} \triangleq 2 \sum_ {k = 1} ^ {K} \operatorname{diag} \left\{\mathbf {h} _ {\mathrm{r}, k} ^ {H} \right\} \mathbf {G} ^ {*} \mathbf {h} _ {\mathrm{d}, k}, \tag {50b}
$$

problem (49) is re-formulated as

$$
\min _ {\boldsymbol {\psi}} - \boldsymbol {\psi} ^ {H} \mathbf {M} \boldsymbol {\psi} - \Re \{\boldsymbol {\psi} ^ {H} \mathbf {m} \}
$$

$$
\text { s.t. } \quad | \psi_ {m} | = 1, \forall m, \tag {51}
$$

which can be efficiently solved by the Riemannian conjugate gradient (RCG) algorithm [45]. Finally, after having the optimal ψ in (51), the initial ϕ can be obtained as $\phi = a _ { \mathrm { m a x } } \psi$ , where $a _ { \mathrm { m a x } }$ is the maximum amplitude of the reflection coefficient.

The computational complexity of the proposed CRB optimization algorithm is analyzed as follows, where it is assumed that the popular interior point method is used for solving convex optimization problems in this paper. First of all, initializing active RIS reflection vector $\phi$ requires about $\mathcal { O } ( M ^ { 1 . 5 } )$ operations. Moreover, obtaining the optimal solutions $\mathbf { W } _ { i } , \ i = 1 , \dots , K$ and ${ \mathbf { R } } _ { \mathrm { w } }$ requires approximately $\mathcal { O } ( N ^ { 6 . 5 } K ^ { 6 . 5 } )$ operations. The construction of $\begin{array} { r l } { { \bf w } _ { i } , } & { { } i \mathrm { ~  ~ \omega ~ } = } \end{array}$ $1 , \ldots , K + N$ has a computational complexity of $\mathcal { O } ( ( K +$ $N ) N ^ { 3 } )$ . The complexity of calculating $t _ { 1 }$ and $t _ { 2 }$ is at the order of $\mathcal { O } ( M ^ { 2 } )$ . The computational complexity of solving the sub-problem with respect to $\phi$ has the order of $\mathcal { O } ( M ^ { 4 . 5 } )$ . $\mathcal { O } ( N \mathbf { \bar { } } M ^ { 2 } + M N ^ { 2 } )$ operations are demanded to update Ψ. Therefore, the overall computational complexity of Algorithm 1 can be approximated as $\mathcal { O } ( N ^ { 6 . 5 } K ^ { 6 . 5 } + M ^ { 4 . 5 } +$ $N M ^ { 2 } + M N ^ { 2 } )$ .

# IV. SIMULATION RESULTS

In this section, we provide extensive simulation results to verify the advantages of the proposed active RIS-empowered ISAC design scheme. As illustrated in Fig. 2, we assume that a dual-functional BS with $N = 1 6$ transmit/receive antennas is at the origin of coordinates and performs communication and sensing functions at the same time. The communication users are located in a circle with the center at (−10m, 40m) and a radius of 5m. Meanwhile, a potential detection target blocked by obstacles is situated in (3m, 47m). The ISAC system is assisted by an active RIS located at $( x \ = \ 0 \mathrm { m } , \ 5 0 \mathrm { m } ) . ^ { 2 }$ In light of the trade-off between performance and cost/energy efficiency considerations, we have set the number of active RIS reflection elements to $^ 8$ in this work. It is assumed that the BS-RIS channel and the BS/RIS-user channels follow the Rician fading model and Rayleigh fading model, respectively. The RIS-target channel is assumed to be the LoS model, as defined before. In specific, the DoA of the target with respect to active RIS is set as $\theta ~ = ~ \frac { \pi } { 4 }$ . The typical pathloss model $P L ( d ) \ = \ C _ { 0 } ( d _ { 0 } / d ) ^ { \iota }$ is adopted in this paper. The path-loss exponents for the above channels are set to 2.2, 3.5, 2.3, and 2.2, respectively. Besides, it is assumed that all communication users have the same QoS requirements for the sake of simplicity, i.e., $\gamma _ { k } = \gamma ,$ ∀k. Finally, the noise powers are set to $\sigma _ { k } ^ { 2 } = \sigma _ { \mathrm { z } } ^ { 2 } = \sigma _ { \mathrm { r } } ^ { 2 } = - 8 0 \mathrm { d } \mathrm { B m }$ , ∀k, the RCS is set to $\sigma _ { \mathrm { t } } ^ { 2 } = 1$ , and the number of samples is set to $L = 1 0 2 4$ .

![](images/4abb0051a6fdb48b2420f0ec6655bd102c59064ea150963187fdbaad42fe2e5f.jpg)

<details>
<summary>scatter</summary>

| Point Type       | x (m) | y (m) |
| ---------------- | ----- | ----- |
| Active RIS       | 3     | 47    |
| Obstacle         | 0     | 0     |
| Communication users | -10   | 40    |
</details>

Fig. 2. An illustration of the position of BS, active RIS, communication users, and target.

The convergence behavior of Algorithm 1 is illustrated in Fig. 3, where we set $P _ { \mathrm { B S } } = 2 7 \mathrm { d B m } .$ , $P _ { \mathrm { R I S } } \ = \ 1 0 \mathrm { d B m } ,$ $a _ { \mathrm { m a x } } = 8$ , and $\gamma = 1 6 \mathrm { d B } .$ . Specifically, Fig. 3(a) and Fig. 3(b) show the convergence of the inner active RIS reflection beamforming design algorithm and the outer whole algorithm, respectively. Particularly, the curves in Fig. 3(a) represent the inner convergence of the 1st, 5th, and 20th outer iterations, respectively, i.e., corresponding to the 1st, 5th, and 20th points in Fig. 3(b). It is observed that the proposed algorithm converges within a finite number of iterations and exhibits excellent convergence performance.

We then present the CRB for target DoA estimation versus transmit power $P _ { \mathrm { B S } }$ in Fig. 4. In order to demonstrate the advantages of the proposed active RIS-empowered ISAC scheme (denoted as ${ } ^ { 6 6 } \mathbf { A R I S - I S A C ^ { 3 3 } } ) .$ , the passive RIS-aided

2It is worth noting that both communication users and the sensing target are located in the far-field of the BS and RIS.

![](images/4c72c328126f833fa533b048397046be87b3be12162cec841824e61d30ae26dd.jpg)

<details>
<summary>line</summary>

| Number of iterations | 1st loop | 5th loop | 20th loop |
| -------------------- | -------- | -------- | --------- |
| 0                    | -8.0     | -11.5    | -12.5     |
| 20                   | -8.5     | -11.7    | -12.5     |
| 40                   | -9.0     | -11.8    | -12.5     |
| 60                   | -9.2     | -11.9    | -12.5     |
| 80                   | -9.3     | -12.0    | -12.5     |
| 100                  | -9.3     | -12.0    | -12.5     |
</details>

(a) Inner loop.

![](images/0b30128a930f71ecf4e28b8c38545200eaa25b828bb52e5d7f39a28f150de4d8.jpg)

<details>
<summary>line</summary>

| Number of iterations | CRB (dB) |
| -------------------- | -------- |
| 0                    | -7.0     |
| 1                    | -8.5     |
| 2                    | -9.5     |
| 3                    | -10.0    |
| 4                    | -10.5    |
| 5                    | -11.0    |
| 6                    | -11.5    |
| 7                    | -12.0    |
| 8                    | -12.2    |
| 9                    | -12.3    |
| 10                   | -12.4    |
| 11                   | -12.4    |
| 12                   | -12.4    |
| 13                   | -12.4    |
| 14                   | -12.4    |
| 15                   | -12.4    |
| 16                   | -12.4    |
| 17                   | -12.4    |
| 18                   | -12.4    |
| 19                   | -12.4    |
| 20                   | -12.4    |
</details>

(b) Outer loop.

Fig. 3. Convergence of Algorithm 1.   
![](images/958a81b57778324d595ec9bd3add9dfb9d17ff8be1bb11bf12810fb3529d6d50.jpg)

<details>
<summary>line</summary>

| Transmit power (dBm) | ARIS-ISAC, a_max = 8, P_RIS = 0dBm | ARIS-ISAC, a_max = 8, P_RIS = 10dBm | ARIS-ISAC, a_max = 6, P_RIS = 10dBm | PRIS-ISAC |
| --------------------- | ----------------------------------- | ------------------------------------ | ------------------------------------ | --------- |
| 20                    | -5                                  | -5                                   | 0                                    | 30        |
| 25                    | -10                                 | -10                                  | -5                                   | 25        |
| 30                    | -15                                 | -15                                  | -10                                  | 20        |
| 35                    | -20                                 | -20                                  | -15                                  | 15        |
| 40                    | -25                                 | -25                                  | -20                                  | 10        |
| 45                    | -30                                 | -30                                  | -25                                  | 5         |
| 50                    | -35                                 | -35                                  | -30                                  | 0         |
</details>

Fig. 4. CRB versus the transmit power PBS (γ = 16dB).

ISAC scheme is included as a benchmark (denoted as “PRIS-ISAC”). To achieve a fair comparison, we guarantee that the total power budgets are the same for the active RIS and passive RIS systems, i.e., $P _ { \mathrm { B S } } ^ { \mathrm { p } } \ = \ P _ { \mathrm { B S } } + P _ { \mathrm { R I S } } \ ( P _ { \mathrm { R I S } } \ = \ 1 0 \mathrm { d B m } )$ is set as transmit power for passive RIS scheme. It can be easily observed that the proposed active RIS-empowered ISAC scheme is consistently superior to the passive one for all transmit powers, and achieves up to 36dB CRB performance improvement at the case of $a _ { \mathrm { m a x } } = 8 , P _ { \mathrm { R I S } } = 1 0 \mathrm { d B m }$ , which validates the significant benefits of deploying active RIS in ISAC systems compared to passive RIS. In fact, the drawback of employing passive RIS is more pronounced in sensing a target located in a blind area of BS, since the echo signals suffer from severe fading of BS-RIS-target channel twice (forward and backward). Weak echo signals prevent us from extracting useful information on target detection/parameter estimation. Fig. 4 indicates that by favorably amplifying the echo signals twice, active RIS can successfully overcome this multiplicative fading effect. Furthermore, for given maximum amplitude factor $a _ { \mathrm { m a x } } = 8$ , we can notice that the active RIS schemes with different $P _ { \mathrm { R I S } }$ budgets have almost the same

![](images/23fc2436616d84a96412be0a3970bc52dcf9876f385be3a2df2d7faa7b89d854.jpg)

<details>
<summary>line</summary>

| SINR requirement (dB) | CRB (dB) - ARIS-ISAC, a_max = 8 | CRB (dB) - ARIS-radar-only, a_max = 8 | SER - ARIS-ISAC, a_max = 6 | SER - ARIS-radar-only, a_max = 6 |
| --------------------- | -------------------------------- | -------------------------------------- | -------------------------- | -------------------------------- |
| 2                     | -3.5                             | -3.5                                   | 4.0                        | 1.5                              |
| 4                     | -3.3                             | -3.5                                   | 2.5                        | 1.5                              |
| 6                     | -3.0                             | -3.5                                   | 1.0                        | 1.5                              |
| 8                     | -2.5                             | -3.5                                   | -1.0                       | 1.5                              |
| 10                    | -2.0                             | -3.5                                   | -4.0                       | 1.5                              |
| 12                    | -1.5                             | -3.5                                   | 3.5                        | 1.5                              |
</details>

Fig. 5. CRB/SER versus the SINR requirement $\gamma \ ( P _ { \mathrm { B S } } \ = \ 1 6 \mathrm { d } \mathrm { B m } ,$ , $\bar { P _ { \mathrm { R I S } } } = 1 0 \mathrm { d B m } ,$ solid line: CRB, dashed line: SER).

![](images/f40a522ab07dde38de032c0a30be709a0a59adaa4c1dbc4278d075a70efd6cce.jpg)

<details>
<summary>line</summary>

| Number of RIS elements | ARIS-radar-only, a_max = 8 | ARIS-ISAC, a_max = 8 | ARIS-ISAC, a_max = 6 | PRIS-ISAC |
| ---------------------- | -------------------------- | --------------------- | --------------------- | --------- |
| 4                      | 5                          | 5                     | 10                    | 40        |
| 8                      | -10                        | -10                   | -5                    | 25        |
| 12                     | -20                        | -20                   | -15                   | 18        |
| 16                     | -25                        | -25                   | -20                   | 12        |
| 20                     | -30                        | -30                   | -25                   | 7         |
| 24                     | -35                        | -35                   | -30                   | 3         |
</details>

Fig. 6. CRB versus the number of RIS elements M $( P _ { \mathrm { B S } } = 2 3 \mathrm { d B m } .$ , $\bar { P _ { \mathrm { R I S } } } = 1 0 \mathrm { d B m } , \gamma = 1 6 \mathrm { d B } )$ .

CRB when $P _ { \mathrm { B S } }$ is small. It implies that for the weak transmit power, the active RIS amplitude constraint is dominant while the active RIS power constraint is inactive. As $P _ { \mathrm { B S } }$ increases, curves with different $P _ { \mathrm { R I S } }$ settings are distinguished from the other and the CRB performance at the case of $P _ { \mathrm { R I S } } ~ { = }$ 0dBm tends to be saturated. This phenomenon reveals that in the strong transmit power scenario, the active RIS power constraint further limits the radar performance. Besides, the case of $a _ { \mathrm { m a x } } = 8 , P _ { \mathrm { R I S } } = 1 0 \mathrm { d B m }$ is always superior to the case of $a _ { \mathrm { m a x } } = 6 , P _ { \mathrm { R I S } } = 1 0 \mathrm { d B m }$ , which means that a wider range of amplitude variation can bring a higher DoF and lead to better performance when the active RIS power budget is sufficient.

The CRB/symbol error rate (SER) performance versus the communication users’ SINR requirement γ is studied in Fig. 5, in which the solid lines represent the CRB performance for sensing function, while the dashed lines represent the SER performance for communication function. Firstly, not surprisingly, we can observe that the SER of the active RISassisted ISAC system gradually decreases as it has higher communication SINR requirements, which means that the communication QoS can be satisfied. In addition, the active RIS-aided radar-only system is considered as a baseline (denoted $\mathrm { a s \ ^ { 6 6 } A R I S \mathrm { - r a d a r \mathrm { - } \mathbf { 0 } n l y ^ { 3 9 } ) } }$ . In comparison to the radaronly system, the active RIS-assisted ISAC system incurs a certain CRB performance loss as it has higher communication requirements. This loss is insignificant when γ is small, since the beamforming solutions obtained by minimizing the radar CRB can satisfy the communication SINR. With the growth of γ, the performance gap between the ISAC system and the radar-only system becomes more evident. This is because more resources are skewed toward communication function, resulting in a rise of the CRB for target estimation, which proves the trade-off between multi-user communications and radar sensing on ISAC systems.

![](images/09ccdecd7503a012b8042ff155c0f369a2aaa6aa9dc0fc852e669ee400970295.jpg)

<details>
<summary>line</summary>

| Number of antennas | ARIS-radar-only, a_max = 8 | ARIS-ISAC, a_max = 8 | ARIS-ISAC, a_max = 6 | PRIS-ISAC |
| ------------------ | -------------------------- | -------------------- | -------------------- | --------- |
| 12                 | -7.5                       | -6.5                 | -1.0                 | 30.0      |
| 16                 | -9.0                       | -8.5                 | -4.0                 | 27.0      |
| 20                 | -11.0                      | -10.0                | -6.0                 | 24.0      |
| 24                 | -13.0                      | -12.0                | -8.0                 | 22.0      |
| 28                 | -15.0                      | -14.0                | -9.0                 | 21.0      |
| 32                 | -16.0                      | -15.0                | -10.0                | 20.0      |
</details>

Fig. 7. CRB versus the number of antennas N $( P _ { \mathrm { B S } } ~ = ~ 2 3 \mathrm { d B m } ,$ , $P _ { \mathrm { R I S } } = 1 0 \mathrm { d } \mathrm { B m } , \gamma = 1 6 \mathrm { d } \mathrm { B } )$ .

The CRB versus the number of RIS reflection elements is demonstrated in Fig. 6. We can observe that the proposed CRB minimization for the active RIS-empowered ISAC system dramatically outperforms the passive RIS-assisted system and has quite close performance to the active RIS-empowered radar-only system. As expected, the CRB of all scenarios decreases with the increase of M owing to higher exploitable spatial DoFs.

Next, we illustrate the CRB performance versus the number of antennas $N _ { \mathrm { t } } = N _ { \mathrm { r } } = N$ in Fig. 7. Similar conclusions can be drawn from Fig. 7 that the active RIS solution performs better than the passive RIS solution and the active RIS-empowered ISAC system behaves very similarly to the active RIS-empowered radar-only system. In addition, improved performance can be obtained by adding antennas owing to more spatial diversity and larger beamforming gains. Furthermore, it is worth noting that as N grows, the performance of the ISAC system and the radar-only system gradually approaches the same due to the limitation of the active RIS power budget.

In Fig. 8, we display the CRB for target DoA estimation as a function of the number of communication users K. As we can predict, with growing K, more resources in the ISAC system are allocated to the communication function to ensure the QoS for communication users, which causes a deterioration of the radar sensing function, i.e., an increase of CRB. We also plot the CRB versus the position of RIS in Fig. 9.

![](images/06c3f310d56cdec19511d64ee2dd1e715e530abc19a661085089612cc96d6e80.jpg)

<details>
<summary>line</summary>

| Number of communication users | ARIS-ISAC, a_max = 8 | ARIS-radar-only, a_max = 8 | ARIS-ISAC, a_max = 6 | ARIS-radar-only, a_max = 6 |
| ----------------------------- | -------------------- | -------------------------- | -------------------- | -------------------------- |
| 2                             | -10.5                | -10.5                      | -5.5                 | -5.5                       |
| 3                             | -9.8                 | -10.5                      | -4.8                 | -5.5                       |
| 4                             | -8.8                 | -10.5                      | -4.2                 | -5.5                       |
| 5                             | -7.8                 | -10.5                      | -3.5                 | -5.5                       |
| 6                             | -6.8                 | -10.5                      | -2.8                 | -5.5                       |
| 7                             | -5.8                 | -10.5                      | -2.0                 | -5.5                       |
</details>

Fig. 8. CRB versus the number of communication users K $( P _ { \mathrm { B S } } = 2 3 \mathrm { d } \mathrm { B m } ,$ $\bar { P _ { \mathrm { R I S } } } = 1 0 \mathrm { d } \mathrm { B m } , \gamma = 1 6 \mathrm { d } \mathrm { B } )$ .

![](images/0f6562e77d7e8c302f20bcbd761a03ba1226335b8664badd4dc1caa560aa5d14.jpg)

<details>
<summary>line</summary>

| Position of RIS (m) | ARIS-radar-only, a_max = 8 | ARIS-ISAC, a_max = 8 | ARIS-ISAC, a_max = 6 | PRIS-ISAC |
| ------------------- | -------------------------- | --------------------- | --------------------- | --------- |
| -8                  | 9.0                        | 10.0                  | 14.0                  | 45.0      |
| -6                  | 7.0                        | 8.0                   | 12.0                  | 42.0      |
| -4                  | 3.0                        | 4.0                   | 8.0                   | 38.0      |
| -2                  | -5.0                       | -6.0                  | 2.0                   | 32.0      |
| 0                   | -10.0                      | -11.0                 | -5.0                  | 26.0      |
| 2                   | -15.0                      | -16.0                 | -10.0                 | 21.0      |
</details>

Fig. 9. CRB versus the position of $\mathrm { R I S } ~ x ~ ( P _ { \mathrm { B S } } = 2 3 \mathrm { d B n }$ m, $P _ { \mathrm { R I S } } = 1 0 \mathrm { d B m }$ $\gamma = 1 6 \mathrm { d B } )$ .

![](images/27fef7bd718e6129dd27e8e1f2e2a8ff59ef83ec2a9a959fe643e0b60e79e4d2.jpg)

<details>
<summary>heatmap</summary>

| x-axis (m) | y-axis (m) | Value |
| ---------- | ---------- | ----- |
| -15        | 43         | -     |
| -12        | 36         | -     |
| -10        | 45         | -     |
| -8         | 43         | -     |
| -5         | 43         | -     |
| -2         | 43         | -     |
| 0          | 47         | -     |
| 2          | 24         | -     |
| 3          | 50         | -     |
| 4          | 50         | -     |
| 5          | 50         | -     |
</details>

Fig. 10. Beampattern of the active RIS-assisted system (BS: diamond; RIS: square; target: star; users: circles, obstacle: triangle).

Obviously, the closer the distance between the RIS and the target, the better the sensing performance of the radar can be achieved.

In Fig. 10, we present the illustration of the beampattern of the active RIS-assisted ISAC system in the case of LoS channels. It can be observed that the BS transmit beams are strongly directed toward the active RIS and the communication users. More importantly, the reflection beams of the active RIS are also pointed toward the target and the users to achieve satisfactory communication and sensing performance.

# V. CONCLUSION

In this paper, we investigated the joint transmit precoding and active RIS reflection beamforming design for active RIS-empowered ISAC systems. In addition to the SINR performance metric for multi-user communications, we derived the CRB performance metric for evaluating the target DoA estimation to enhance the sensing performance of ISAC systems. Then, we formulated the CRB minimization problem subject to the users’ SINR requirements, the BS power budget, the active RIS power budget, and the amplitude constraint of the active RIS reflection coefficients. An effective solution based on alternating optimization, SDR, and MM was exploited to address this extremely challenging problem. Various simulation results verified the effectiveness of the proposed algorithm, illustrated the remarkable performance enhancements from active RIS, and demonstrated the tradeoff between multi-user communications and radar sensing. Compared to passive RIS-assisted ISAC systems, active RIS can provide more than 30dB reduction of CRB for the singletarget DoA estimation. For the case of sensing multiple targets in the active RIS-empowered ISAC system, the derivation of CRB for estimating multiple DoAs and the development of the associated beamforming design algorithms are substantially more complicated, which deserve further investigation in future studies.

# APPENDIX A

In order to re-arrange $g ( \phi )$ as an explicit expression over $\phi ,$ we first expand and re-write each of the components, which is presented as follows

$$
\begin{array}{l} g _ {1} (\phi) = \operatorname{Tr} \left\{\dot {\mathbf {Q}} \mathbf {W} \mathbf {W} ^ {H} \dot {\mathbf {Q}} ^ {H} \boldsymbol {\Psi} ^ {- 1} \right\} (52a) \\ = \operatorname{Tr} \left\{c _ {0} \mathbf {G} ^ {T} \mathbf {A} \left(\mathbf {L} \phi \phi^ {T} + \phi \phi^ {T} \mathbf {L}\right) \mathbf {A G W W} ^ {H} \right. (52b) \\ \times c _ {0} ^ {*} \mathbf {G} ^ {H} \mathbf {A} ^ {H} (\mathbf {L} \phi^ {*} \phi^ {H} + \phi^ {*} \phi^ {H} \mathbf {L}) \mathbf {A} ^ {H} \mathbf {G} ^ {*} \boldsymbol {\Psi} ^ {- 1} \} \\ = \left| c _ {0} \right| ^ {2} \left(\phi^ {H} \mathbf {L} \mathbf {R} _ {1} \phi \phi^ {H} \mathbf {R} _ {2} \mathbf {L} \phi + \phi^ {H} \mathbf {R} _ {1} \phi \phi^ {H} \mathbf {L} \mathbf {R} _ {2} \mathbf {L} \phi \right. (52c) \\ \end{array}
$$

$$
+ \phi^ {H} \mathbf {L} \mathbf {R} _ {1} \mathbf {L} \phi \phi^ {H} \mathbf {R} _ {2} \phi + \phi^ {H} \mathbf {R} _ {1} \mathbf {L} \phi \phi^ {H} \mathbf {L} \mathbf {R} _ {2} \phi),
$$

$$
\begin{array}{l} g _ {2} (\phi) = \left| \operatorname{Tr} \left\{\mathbf {Q W W} ^ {H} \dot {\mathbf {Q}} ^ {H} \boldsymbol {\Psi} ^ {- 1} \right\} \right| ^ {2} (52d) \\ = \left| \operatorname{Tr} \left\{\alpha_ {\mathrm{r}, \mathrm{t}} ^ {2} \mathbf {G} ^ {T} \mathbf {A} \phi \phi^ {T} \mathbf {A G W W} ^ {H} \right. \right. (52e) \\ \times c _ {0} ^ {*} \mathbf {G} ^ {H} \mathbf {A} ^ {H} (\mathbf {L} \phi^ {*} \phi^ {H} + \phi^ {*} \phi^ {H} \mathbf {L}) \mathbf {A} ^ {H} \mathbf {G} ^ {*} \boldsymbol {\Psi} ^ {- 1} \} | ^ {2} \\ = \alpha_ {\mathrm{r}, \mathrm{t}} ^ {4} \left| c _ {0} \right| ^ {2} \left(\left| \phi^ {H} \mathbf {L R} _ {1} \phi \phi^ {H} \mathbf {R} _ {2} \phi \right| ^ {2} \right. (52f) \\ + | \phi^ {H} \mathbf {R} _ {1} \phi \phi^ {H} \mathbf {L R} _ {2} \phi | ^ {2} \\ + \phi^ {H} \mathbf {L} \mathbf {R} _ {1} \phi \phi^ {H} \mathbf {R} _ {1} \phi \phi^ {H} \mathbf {R} _ {2} \phi \phi^ {H} \mathbf {R} _ {2} \mathbf {L} \phi \\ \end{array}
$$

$$
+ \phi^ {H} \mathbf {R} _ {1} \mathbf {L} \phi \phi^ {H} \mathbf {R} _ {1} \phi \phi^ {H} \mathbf {R} _ {2} \phi \phi^ {H} \mathbf {L} \mathbf {R} _ {2} \phi),
$$

$$
\begin{array}{l} g _ {3} (\phi) = \operatorname{Tr} \left\{\mathbf {Q} \mathbf {W} \mathbf {W} ^ {H} \mathbf {Q} ^ {H} \boldsymbol {\Psi} ^ {- 1} \right\} (52g) \\ = \operatorname{Tr} \left\{\alpha_ {\mathrm{r}, \mathrm{t}} ^ {2} \mathbf {G} ^ {T} \mathbf {A} \phi \phi^ {T} \mathbf {A G W W} ^ {H} \right. (52h) \\ \times \alpha_ {\mathrm{r}, \mathrm{t}} ^ {2} \mathbf {G} ^ {H} \mathbf {A} ^ {H} \boldsymbol {\phi} ^ {*} \boldsymbol {\phi} ^ {H} \mathbf {A} ^ {H} \mathbf {G} ^ {*} \boldsymbol {\Psi} ^ {- 1} \} \\ = \alpha_ {\mathrm{r}, \mathrm{t}} ^ {4} \phi^ {H} \mathbf {R} _ {1} \phi \phi^ {H} \mathbf {R} _ {2} \phi , (52i) \\ \end{array}
$$

where we define the Hermitian matrices ${ \bf R } _ { 1 }$ and ${ \bf R } _ { 2 }$ as

$$
\mathbf {R} _ {1} \triangleq \mathbf {A} ^ {H} \mathbf {G} ^ {*} \mathbf {W} ^ {*} \mathbf {W} ^ {T} \mathbf {G} ^ {T} \mathbf {A}, \tag {53a}
$$

$$
\mathbf {R} _ {2} \triangleq \mathbf {A} ^ {H} \mathbf {G} ^ {*} \boldsymbol {\Psi} ^ {- 1} \mathbf {G} ^ {T} \mathbf {A}. \tag {53b}
$$

Plugging the results $g _ { 1 } ( \phi ) , \ g _ { 2 } ( \phi )$ and $g _ { 3 } ( \phi )$ in (52), the objective function $g ( \phi )$ can be re-formulated in an explicit form of the variable ϕ as

$$
\begin{array}{l} g (\phi) = g _ {1} (\phi) - \frac {g _ {2} (\phi)}{g _ {3} (\phi)} (54a) \\ = \left| c _ {0} \right| ^ {2} \left(\phi^ {H} \mathbf {R} _ {1} \phi \phi^ {H} \mathbf {L R} _ {2} \mathbf {L} \phi + \phi^ {H} \mathbf {R} _ {2} \phi \phi^ {H} \mathbf {L R} _ {1} \mathbf {L} \phi \right. \\ - \frac {\phi^ {H} \mathbf {R} _ {2} \phi \left| \phi^ {H} \mathbf {L} \mathbf {R} _ {1} \phi \right| ^ {2}}{\phi^ {H} \mathbf {R} _ {1} \phi} - \frac {\phi^ {H} \mathbf {R} _ {1} \phi \left| \phi^ {H} \mathbf {L} \mathbf {R} _ {2} \phi \right| ^ {2}}{\phi^ {H} \mathbf {R} _ {2} \phi}). (54b) \\ \end{array}
$$

Furthermore, by utilizing the properties $\begin{array} { r l } { \operatorname { T r } \{ \mathbf { A B } \} } & { { } = } \end{array}$ $\mathrm { v e c } ^ { H } \{ { \bf B } ^ { H } \} \mathrm { v e c } \{ { \bf \bar { A } } \}$ and $\bar { \mathrm { T r } } \{ { \bf A B C D } \} \ = \mathrm { v e c } ^ { H } \{ { \bf \dot { D } } ^ { H } \} ( { \bf \dot { C } } ^ { T } \ \hat { \ \Phi }$ ⊗ $\mathbf { A } ) \mathrm { v e c } \{ \mathbf { B } \}$ , we have

$$
\begin{array}{l} \phi^ {H} \mathbf {R} _ {i} \phi = \operatorname{Tr} \left\{\phi \phi^ {H} \mathbf {R} _ {i} \right\} \\ = \operatorname{vec} ^ {H} \left\{\mathbf {R} _ {i} ^ {H} \right\} \operatorname{vec} \left\{\phi \phi^ {H} \right\} \\ = \boldsymbol {\xi} _ {i} ^ {H} \mathbf {v}, \tag {55a} \\ \end{array}
$$

$$
\left| \phi^ {H} \mathbf {L R} _ {i} \phi \right| ^ {2} = \operatorname{Tr} \left\{\mathbf {L R} _ {i} \phi \phi^ {H} \mathbf {R} _ {i} \mathbf {L} \phi \right\}
$$

$$
= \operatorname{vec} ^ {H} \left\{\phi \phi^ {H} \right\} \left(\mathbf {L R} _ {i} ^ {T} \otimes \mathbf {L R} _ {i}\right) \operatorname{vec} \left\{\phi \phi^ {H} \right\}
$$

$$
= \mathbf {v} ^ {H} \boldsymbol {\Xi} _ {\hat {i}} \mathbf {v}, \tag {55b}
$$

$$
\begin{array}{l} \phi^ {H} \mathbf {R} _ {i} \phi \phi^ {H} \mathbf {L R} _ {\hat {i}} \mathbf {L} \phi = \mathrm{Tr} \{\mathbf {R} _ {i} \phi \phi^ {H} \mathbf {L R} _ {\hat {i}} \mathbf {L} \phi \phi^ {H} \} \\ = \operatorname{vec} ^ {H} \left\{\phi \phi^ {H} \right\} \left(\mathbf {L} \mathbf {R} _ {\hat {i}} ^ {T} \mathbf {L} \otimes \mathbf {R} _ {i}\right) \operatorname{vec} \left\{\phi \phi^ {H} \right\} \\ = \mathbf {v} ^ {H} \mathbf {F} _ {i} \mathbf {v}, \tag {55c} \\ \end{array}
$$

where for conciseness we define

$$
\mathbf {v} \triangleq \operatorname{vec} \left\{\phi \phi^ {H} \right\} = \phi^ {*} \otimes \phi , \tag {56a}
$$

$$
\boldsymbol {\xi} _ {i} \triangleq \operatorname{vec} \left\{\mathbf {R} _ {i} ^ {H} \right\}, i = 1, 2, \tag {56b}
$$

$$
\boldsymbol {\Xi} _ {i} \triangleq \mathbf {L R} _ {\hat {i}} ^ {T} \otimes \mathbf {L R} _ {\hat {i}}, \forall i, \hat {i} \neq i, \tag {56c}
$$

$$
\mathbf {F} _ {i} \triangleq \mathbf {L R} _ {\hat {i}} ^ {T} \mathbf {L} \otimes \mathbf {R} _ {i}, \forall i, \hat {i} \neq i, \tag {56d}
$$

and $\hat { i }$ represents the element in the set $\{ 1 , 2 \}$ other than $i ,$ i.e., if i = 1 then $\hat { i } = 2$ and ${ \\\ i \ f \ i \ = \ 2 }$ then $\hat { i } = 1$ . Then, submitting the transformations in (55) into (54) and defining $\mathbf { F } \triangleq \mathbf { F } _ { 1 } + \mathbf { F } _ { 2 }$ , the objective of optimization problem (28) can be equivalently and concisely converted into

$$
\min _ {\phi} \frac {\boldsymbol {\xi} _ {1} ^ {H} \mathbf {v v} ^ {H} \boldsymbol {\Xi} _ {1} \mathbf {v}}{\phi^ {H} \mathbf {R} _ {2} \phi} + \frac {\boldsymbol {\xi} _ {2} ^ {H} \mathbf {v v} ^ {H} \boldsymbol {\Xi} _ {2} \mathbf {v}}{\phi^ {H} \mathbf {R} _ {1} \phi} - \mathbf {v} ^ {H} \mathbf {F v}. \tag {57}
$$

Now, the equivalence between objective functions (28a) and (29a) is proved.

# REFERENCES

[1] F. Liu, C. Masouros, A. P. Petropulu, H. Griffiths, and L. Hanzo, “Joint radar and communication design: Applications, state-of-the-art, and the road ahead,” IEEE Trans. Commun., vol. 68, no. 6, pp. 3834–3862, Jun. 2020.   
[2] J. A. Zhang et al., “Enabling joint communication and radar sensing in mobile networks—A survey,” IEEE Commun. Surveys Tuts., vol. 24, no. 1, pp. 306–345, 1st Quart., 2022.   
[3] F. Liu et al., “Integrated sensing and communications: Towards dualfunctional wireless networks for 6G and beyond,” IEEE J. Sel. Areas Commun., vol. 40, no. 6, pp. 1728–1767, Jun. 2022.   
[4] A. Liu et al., “A survey on fundamental limits of integrated sensing and communication,” IEEE Commun. Surveys Tuts., vol. 24, no. 2, pp. 994–1034, 2nd Quart., 2022.   
[5] X. Liu, T. Huang, N. Shlezinger, Y. Liu, J. Zhou, and Y. C. Eldar, “Joint transmit beamforming for multiuser MIMO communications and MIMO radar,” IEEE Trans. Signal Process., vol. 68, pp. 3929–3944, 2020.   
[6] F. Liu, C. Masouros, A. Li, H. Sun, and L. Hanzo, “MU-MIMO communications with MIMO radar: From co-existence to joint transmission,” IEEE Trans. Wireless Commun., vol. 17, no. 4, pp. 2755–2770, Apr. 2018.   
[7] F. Liu, L. Zhou, C. Masouros, A. Li, W. Luo, and A. Petropulu, “Toward dual-functional radar-communication systems: Optimal waveform design,” IEEE Trans. Signal Process., vol. 66, no. 16, pp. 4264–4279, Aug. 2018.   
[8] R. Liu, M. Li, Q. Liu, and A. L. Swindlehurst, “Dual-functional radarcommunication waveform design: A symbol-level precoding approach,” IEEE J. Sel. Topics Signal Process., vol. 15, no. 6, pp. 1316–1331, Nov. 2021.   
[9] R. Liu, M. Li, Q. Liu, and A. L. Swindlehurst, “Joint waveform and filter designs for STAP-SLP-based MIMO-DFRC systems,” IEEE J. Sel. Areas Commun., vol. 40, no. 6, pp. 1918–1931, Jun. 2022.   
[10] F. Liu, Y.-F. Liu, A. Li, C. Masouros, and Y. C. Eldar, “Cramér–Rao bound optimization for joint radar-communication beamforming,” IEEE Trans. Signal Process., vol. 70, pp. 240–253, 2022.   
[11] H. Hua, T. X. Han, and J. Xu, “MIMO integrated sensing and communication: CRB-rate tradeoff,” IEEE Trans. Wireless Commun., early access, 2024.   
[12] M. Di Renzo et al., “Smart radio environments empowered by reconfigurable intelligent surfaces: How it works, state of research, and the road ahead,” IEEE J. Sel. Areas Commun., vol. 38, no. 11, pp. 2450–2525, Nov. 2020.   
[13] Q. Wu and R. Zhang, “Towards smart and reconfigurable environment: Intelligent reflecting surface aided wireless network,” IEEE Commun. Mag., vol. 58, no. 1, pp. 106–112, Jan. 2020.   
[14] G. Zhou, C. Pan, H. Ren, K. Wang, and A. Nallanathan, “Intelligent reflecting surface aided multigroup multicast MISO communication systems,” IEEE Trans. Signal Process., vol. 68, pp. 3236–3251, 2020.   
[15] Q. Wu and R. Zhang, “Intelligent reflecting surface enhanced wireless network via joint active and passive beamforming,” IEEE Trans. Wireless Commun., vol. 18, no. 11, pp. 5394–5409, Nov. 2019.   
[16] S. Zhou, W. Xu, K. Wang, M. Di Renzo, and M.-S. Alouini, “Spectral and energy efficiency of IRS-assisted MISO communication with hardware impairments,” IEEE Wireless Commun. Lett., vol. 9, no. 9, pp. 1366–1369, Sep. 2020.   
[17] S. Zeng, H. Zhang, B. Di, Z. Han, and L. Song, “Reconfigurable intelligent surface (RIS) assisted wireless coverage extension: RIS orientation and location optimization,” IEEE Commun. Lett., vol. 25, no. 1, pp. 269–273, Jan. 2021.   
[18] R. Liu, M. Li, H. Luo, Q. Liu, and A. L. Swindlehurst, “Integrated sensing and communication with reconfigurable intelligent surfaces: Opportunities, applications, and future directions,” IEEE Wireless Commun., vol. 30, no. 1, pp. 50–57, Feb. 2023.   
[19] H. Luo, R. Liu, M. Li, and Q. Liu, “RIS-aided integrated sensing and communication: Joint beamforming and reflection design,” IEEE Trans. Veh. Technol., vol. 72, no. 7, pp. 9626–9630, Jul. 2023.   
[20] H. Luo, R. Liu, M. Li, Y. Liu, and Q. Liu, “Joint beamforming design for RIS-assisted integrated sensing and communication systems,” IEEE Trans. Veh. Technol., vol. 71, no. 12, pp. 13393–13397, Dec. 2022.   
[21] Z.-M. Jiang et al., “Intelligent reflecting surface aided dual-function radar and communication system,” IEEE Syst. J., vol. 16, no. 1, pp. 475–486, Mar. 2022.

[22] S. Yan, S. Cai, W. Xia, J. Zhang, and S. Xia, “A reconfigurable intelligent surface aided dual-function radar and communication system,” in Proc. 2nd IEEE Int. Symp. Joint Commun. Sens. (JC&S), Seefeld, Austria, Mar. 2022, pp. 1–6.   
[23] X. Song, D. Zhao, H. Hua, T. X. Han, X. Yang, and J. Xu, “Joint transmit and reflective beamforming for IRS-assisted integrated sensing and communication,” in Proc. IEEE Wireless Commun. Netw. Conf. (WCNC), Austin, TX, USA, Apr. 2022, pp. 189–194.   
[24] R. Liu, M. Li, Y. Liu, Q. Wu, and Q. Liu, “Joint transmit waveform and passive beamforming design for RIS-aided DFRC systems,” IEEE J. Sel. Topics Signal Process., vol. 16, no. 5, pp. 995–1010, Aug. 2022.   
[25] R. Liu, M. Li, Q. Liu, and A. L. Swindlehurst, “SNR/CRB-constrained joint beamforming and reflection designs for RIS-ISAC systems,” IEEE Trans. Wireless Commun., early access, 2023.   
[26] H. Zhang, “Joint waveform and phase shift design for RIS-assisted integrated sensing and communication based on mutual information,” IEEE Commun. Lett., vol. 26, no. 10, pp. 2317–2321, Oct. 2022.   
[27] M. Luan, B. Wang, Z. Chang, T. Hämäläinen, and F. Hu, “Robust beamforming design for RIS-aided integrated sensing and communication system,” IEEE Trans. Intell. Transp. Syst., vol. 24, no. 6, pp. 6227–6243, Jun. 2023.   
[28] X. Wang, Z. Fei, Z. Zheng, and J. Guo, “Joint waveform design and passive beamforming for RIS-assisted dual-functional radarcommunication system,” IEEE Trans. Veh. Technol., vol. 70, no. 5, pp. 5131–5136, May 2021.   
[29] X. Wang, Z. Fei, J. Huang, and H. Yu, “Joint waveform and discrete phase shift design for RIS-assisted integrated sensing and communication system under cramer-rao bound constraint,” IEEE Trans. Veh. Technol., vol. 71, no. 1, pp. 1004–1009, Jan. 2022.   
[30] T. Wei, L. Wu, K. V. Mishra, and M. R. B. Shankar, “Multiple IRS-assisted wideband dual-function radar-communication,” in Proc. 2nd IEEE Int. Symp. Joint Commun. Sens. (JC&S), Seefeld, Austria, Mar. 2022, pp. 1–5.   
[31] T. Wei, L. Wu, K. V. Mishra, and M. R. B. Shankar, “IRS-aided wideband dual-function radar-communications with quantized phaseshifts,” in Proc. IEEE 12th Sensor Array Multichannel Signal Process. Workshop (SAM), Trondheim, Norway, Jun. 2022, pp. 465–469.   
[32] Z. Zhang et al., “Active RIS vs. passive RIS: Which will prevail in 6G?” IEEE Trans. Commun., vol. 71, no. 3, pp. 1707–1725, Mar. 2023.   
[33] R. Long, Y.-C. Liang, Y. Pei, and E. G. Larsson, “Active reconfigurable intelligent surface-aided wireless communications,” IEEE Trans. Wireless Commun., vol. 20, no. 8, pp. 4962–4975, Aug. 2021.   
[34] L. Dong, H.-M. Wang, and J. Bai, “Active reconfigurable intelligent surface aided secure transmission,” IEEE Trans. Veh. Technol., vol. 71, no. 2, pp. 2181–2186, Feb. 2022.   
[35] Z. Peng, R. Weng, Z. Zhang, C. Pan, and J. Wang, “Active reconfigurable intelligent surface for mobile edge computing,” IEEE Wireless Commun. Lett., vol. 11, no. 12, pp. 2482–2486, Dec. 2022.   
[36] K. Zhi, C. Pan, H. Ren, K. K. Chai, and M. Elkashlan, “Active RIS versus passive RIS: Which is superior with the same power budget?” IEEE Commun. Lett., vol. 26, no. 5, pp. 1150–1154, May 2022.   
[37] Y. Ma, M. Li, Y. Liu, Q. Wu, and Q. Liu, “Active reconfigurable intelligent surface for energy efficiency in MU-MISO systems,” IEEE Trans. Veh. Technol., vol. 72, no. 3, pp. 4103–4107, Mar. 2023.   
[38] Q. Zhu, M. Li, R. Liu, Y. Liu, and Q. Liu, “Joint beamforming designs for active reconfigurable intelligent surface: A sub-connected array architecture,” IEEE Trans. Commun., vol. 70, no. 11, pp. 7628–7643, Nov. 2022.   
[39] A. A. Salem, M. H. Ismail, and A. S. Ibrahim, “Active reconfigurable intelligent surface-assisted MISO integrated sensing and communication systems for secure operation,” IEEE Trans. Veh. Technol., vol. 72, no. 4, pp. 4919–4931, Apr. 2023.   
[40] Y. Zhang, J. Chen, C. Zhong, H. Peng, and W. Lu, “Active IRS-assisted integrated sensing and communication in C-RAN,” IEEE Wireless Commun. Lett., vol. 12, no. 3, pp. 411–415, Mar. 2023.   
[41] Q. Zhu, M. Li, R. Liu, and Q. Liu, “Joint transceiver beamforming and reflecting design for active RIS-aided ISAC systems,” IEEE Trans. Veh. Technol., vol. 72, no. 7, pp. 9636–9640, Jul. 2023.   
[42] S. M. Kay, Fundamentals of Statistical Signal Processing: Estimation Theory. Englewood Cliffs, NJ, USA: Prentice-Hall, 1993.   
[43] I. Bekkerman and J. Tabrikian, “Target detection and localization using MIMO radars and sonars,” IEEE Trans. Signal Process., vol. 54, no. 10, pp. 3873–3883, Oct. 2006.

[44] X. Song, J. Xu, F. Liu, T. Xiao Han, and Y. C. Eldar, “Intelligent reflecting surface enabled sensing: Cramér–Rao bound optimization,” IEEE Trans. Signal Process., vol. 71, pp. 2011–2026, 2023.   
[45] R. Liu, M. Li, Q. Liu, and A. L. Swindlehurst, “Joint symbol-level precoding and reflecting designs for IRS-enhanced MU-MISO systems,” IEEE Trans. Wireless Commun., vol. 20, no. 2, pp. 798–811, Feb. 2021.

![](images/5710eec4963a12d6b911baa6f4750191f5b18b0d7412b82b35f8d20d187a62c5.jpg)

<details>
<summary>natural_image</summary>

Portrait of a young woman with long dark hair wearing a white top and bow tie (no text or symbols visible)
</details>

Qi Zhu received the B.S. degree in electronics information engineering from Dalian University of Technology, Dalian, China, in 2021, where she is currently pursuing the M.S. degree with the School of Information and Communication Engineering. Her current research interests include signal processing, reconfigurable intelligent surface, and integrated sensing and communication.

![](images/6ada33bef8813387d92bc3807c5e8c1a37f8edc0bdc30439e34c90167be075b3.jpg)

<details>
<summary>natural_image</summary>

Portrait of a woman wearing glasses and a white collared shirt against a gray background (no text or symbols visible)
</details>

Rang Liu (Member, IEEE) received the B.S. degree in electronics information engineering from Dalian University of Technology, Dalian, China, in 2018, and the Ph.D. degree from the School of Information and Communication Engineering, Dalian University of Technology, in 2023. She is currently a Post-Doctoral Scholar with the Department of Electrical Engineering and Computer Science, University of California at Irvine, Irvine. Her research interests mainly include signal processing, massive MIMO systems, reconfigurable intelligent surfaces, and

integrated sensing and communications.

![](images/3988f33081d6d41df2b6f1dcdfa186194154ebb3f01a5a967ebc3837555a5dd6.jpg)

<details>
<summary>natural_image</summary>

Portrait of a man wearing glasses and a blue suit (no text or symbols visible)
</details>

Ming Li (Senior Member, IEEE) received the M.S. and Ph.D. degrees in electrical engineering from The State University of New York at Buffalo (SUNY-Buffalo), Buffalo, in 2005 and 2010, respectively. From January 2011 to August 2013, he was a Post-Doctoral Research Associate with the Department of Electrical Engineering, SUNY-Buffalo. From August 2013 to June 2014, he was with Qualcomm Technologies Inc. as a Senior Engineer. Since June 2014, he has been with the School of Information and Communication Engineering, Dalian University

of Technology, Dalian, China, where he is currently a Professor. He has served as a TPC chair/member of various international flagship conferences. He was a recipient of an Exemplary Reviewer of IEEE TRANSACTIONS ON COMMUNICATIONS. His current research interests include the general areas of communication theory and signal processing with applications to integrated sensing and communication, reconfigurable intelligent surfaces, mmWave communications, massive MIMO systems, and secure wireless communications.

![](images/7fafa663b83fbc44a6902cc5f3eb904e06469e8f9f33f2caa2588f09ed5b8074.jpg)

<details>
<summary>natural_image</summary>

Portrait photo of a smiling woman with dark hair and red lipstick, wearing a dark top (no text or symbols visible)
</details>

Qian Liu (Member, IEEE) received the B.S. and M.S. degrees from Dalian University of Technology, Dalian, China, in 2006 and 2009, respectively, and the Ph.D. degree from The State University of New York at Buffalo (SUNY-Buffalo), Buffalo, NY, USA, in 2013. She is currently an Associate Professor with the Department of Computer Science and Technology, Dalian University of Technology. She was a Post-Doctoral Fellow with the Ubiquitous Multimedia Laboratory, SUNY-Buffalo, from 2013 to 2015. She was an Alexander von Humboldt Fellow

with the Chair of Media Technology and the Chair of Communication Networks, Technical University of Munich, from 2016 to 2017. Her current research interests include haptic communications and signal processing, wireless multimedia communications, and haptic-oriented human–computer interaction. She provides services to the IEEE Haptic Codec Task Group as the Secretary for standardizing haptic codecs in the Tactile Internet. She also served as the Technical Program Co-Chair of 2017 IEEE Haptic Audio Visual Environments and Games (HAVE’17), HAVE’18, AsiaHaptics 2020, and AsiaHaptics 2022.