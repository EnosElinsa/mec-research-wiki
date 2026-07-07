# Ray Antenna Array Achieves Uniform Angular Resolution Cost-Effectively for Low-Altitude UAV Swarm ISAC

Haoyu Jiang , Member, IEEE, and Yong Zeng , Fellow, IEEE

Abstract—Ray antenna array (RAA) is a novel multi-antenna architecture comprising massive low-cost antenna elements, no phase shifters and a few radio-frequency (RF) chains. Compared to the classic hybrid analog/digital beamforming based on conventional antenna arrays, RAA has three appealing advantages: 1) dramatically reduced hardware cost since no phase shifters are needed; 2) enhanced beamforming gain as antenna elements with higher directivity can be used; 3) uniform angular resolution across all signal directions. Such benefits make RAA especially appealing for integrated sensing and communication (ISAC), particularly for low-altitude unmanned aerial vehicle (UAV) swarm ISAC, where high-mobility aerial targets may easily move away from the boresight of conventional antenna arrays, causing severe communication and sensing performance degradation. Therefore, this paper studies RAA-based ISAC for low-altitude UAV swarm systems. First, we establish an inputoutput mathematical model for RAA-based UAV ISAC and rigorously show that RAA achieves uniform angular resolution for all directions through beam pattern analysis. Besides, we design the RAA orientation and ray selection network (RSN) to fully reap its advantages. Furthermore, RAA-based ISAC with orthogonal frequency division multiplexing (OFDM) for UAV swarm is studied, and an efficient algorithm is proposed for sensing target parameter estimation. Extensive simulation results are provided to demonstrate the significant performance improvement by RAA system over the conventional antenna arrays, in terms of sensing angular resolution and communication spectral efficiency, highlighting the great potential of the novel RAA system to meet the growing demands of low-altitude UAV ISAC.

Index Terms—Ray antenna array (RAA), low-altitude UAV, ISAC, UAV swarm, uniform angular resolution.

## I. INTRODUCTION

regarded as important aerial platforms for the emerging

Received 15 May 2025; revised 23 October 2025 and 5 December 2025; accepted 7 December 2025. Date of publication 19 December 2025; date of current version 12 January 2026. This work was supported in part by the National Natural Science Foundation of China under Grant 62571116 and in part by the Natural Science Foundation for Distinguished Young Scholars of Jiangsu Province under Grant BK20240070. The associate editor coordinating the review of this article and approving it for publication was M.-C. Lee. (Corresponding author: Yong Zeng.)

Haoyu Jiang is with the National Mobile Communications Research Laboratory, Southeast University, Nanjing 210096, China (e-mail: 230258936@seu.edu.cn).

Yong Zeng is with the National Mobile Communications Research Laboratory, Southeast University, Nanjing 210096, China, and also with Purple Mountain Laboratories, Nanjing 211111, China (e-mail: yong zeng@seu.edu.cn).

Digital Object Identifier 10.1109/TWC.2025.3643458 low-altitude economy, driven by their flexible maneuverability, rapid deployment capabilities, and cost-effectiveness [1], [2]. The advent of UAV swarm technology has further amplified these advantages, enabling collaborative task execution through distributed sensing and autonomous coordination [3], [4]. Modern multi-functional UAV systems now support critical applications ranging from traffic congestion monitoring to disaster zone search-and-rescue operations, delivering unprecedented spatial coverage and real-time observational precision [5], [6]. However, the very attributes that make UAVs indispensable – affordability, ease of operation, and payload capacity [7] – also render them vulnerable to malicious exploitation, including illegal surveillance, airspace trespassing, and contraband delivery by maliciously manipulated commercial UAVs [8], [9]. This duality underscores an urgent need for effective solutions that simultaneously enhance UAV operational capabilities while enforcing stringent airspace supervision. Such a challenge perfectly aligns with the core objectives of integrated sensing and communication (ISAC) systems [10], [11], [12]. ISAC has emerged as a new paradigm for next-generation wireless systems, enabling the co-design of communication and sensing functionalities through shared hardware infrastructure, signal processing algorithms, and spectral resources [13], [14], [15], [16]. This integration is particularly critical for low-altitude UAV swarm management, where real-time detection and reliable command transmission must coexist to prevent collisions and ensure mission success [17], [18], [19].

Multi-antenna or multiple-input multiple-output (MIMO) has been a key technology for both wireless communication and radar sensing for decades. By exploiting the additional spatial multiplexing, diversity and beamforming gains offered by large array apertures [20], [21], MIMO systems may simultaneously enhance communication and sensing performance. These advantages scale up with array size, driving modern systems toward massive MIMO deployments with dozens or even hundreds of antenna elements. At higher frequency regimes like millimeter-wave (mmWave) and Terahertz bands [22], the further scaling of array size creates additional implementation challenges. While smaller wavelengths at higher frequencies allow denser antenna packing, they also exacerbate path loss and phase noise sensitivity. In addition, the conventional fully digital architecture, where each antenna element requires one dedicated radio frequency (RF) chain, incurs prohibitive hardware cost, signal processing complexity, and energy consumption. This becomes particularly acute in high-frequency systems where wideband operation demands ultra-fast analog-to-digital converters (ADCs) and precise phase synchronization across hundreds or even thousands of array elements. This issue becomes even more severe for 6G and beyond in the era of extremely large-scale MIMO (XL-MIMO) [23]. Such prohibitive overheads necessitate innovative antenna architectures that preserve performance while radically reducing implementation difficulty.

To address such issues, researchers have been exploring various solutions, including analog beamforming [24], hybrid analog/digital beamforming (HBF) [25], [26], [27], [28], [29], lens antenna arrays [30], [31], [32], [33], fluid antenna/movable antenna [34], [35], [36], [37], [38], pinching antenna [39] and tri-hybrid MIMO [20]. With analog beamforming, phase shifters are applied in the analog domain to achieve directional signal reception/transmission, and only one RF chain is needed regardless of the number of antenna elements [24], [40], [41]. However, analog beamforming is inherently limited to single-stream MIMO transmission. HBF further integrated analog and digital beamforming together to make multi-stream transmission possible and achieves comparable performance with respect to fully digital solution when the number of transmitted data stream is relatively small [25], [26], [42], [43]. However, in high-frequency systems such as mmWave and THz systems, accurate phase shifters are hard to design. On the other hand, lens antenna arrays can transform the signal from the antenna space to the beamspace that has much lower dimensions, so as to reduce the number of RF chains significantly [33], [44]. More recently, fluid or movable antenna systems have been proposed by dynamically optimizing antenna shape/positions at transceivers (Tx/Rx) [35], [36]. Compared to fixed antennas, fluid/movable antenna systems achieve superior performance with equal or fewer antennas and RF chains [37]. Besides, pinching antenna [39] applies small dielectric particles to waveguides to build line of sight (LoS) paths for users. Moreover, tri-hybrid MIMO architecture [20] has been proposed to incorporate reconfigurable antennas with both digital and analog precoding. However, all the aforementioned methods require additional hardware cost such as massive number of phase shifters, bulky electromagnetic lenses, motors, long waveguides or reconfigurable antennas, resulting in extra energy consumption, implementation complexity, and/or responding time.

To practically enable flexible beamforming for highfrequency systems like mmWave and THz systems, and further enhance wireless communication and sensing performance cost-effectively, recently a novel multi-antenna architecture termed ray antenna array (RAA) was proposed [45]. RAA leverages the design degree of freedom (DoF) in the spatial domain by deliberately placing massive inexpensive antenna elements in a ray-like structure, where each ray corresponds to a so-called simple uniform linear array (sULA), for the fact that all the antenna elements within each ray are directly connected. This configuration enables each sULA to form a beam with the mainlobe direction matching the ray orientation without relying on any analog or digital beamforming. Thus, compared to the classic fully digital or hybrid beamforming based ULA, the RAA system can achieve even better beamforming capability and uniform angular resolution for all signal directions, while greatly reducing hardware cost by replacing expensive phase shifters with much cheaper antenna elements. Note that the price paid by RAA is its larger size to accommodate the more antenna elements. Fortunately, such an issue is greatly alleviated for high-frequency systems like mmWave or THz systems where the signal wavelengths are very small.

Motivated by the appealing advantages of RAA mentioned above and to fully reap its uniform angular resolution characteristic, in this paper we propose to use RAA for low-altitude UAV swarm ISAC systems. The main contributions of this paper are summarized as follows:

First, we investigate the novel RAA architecture for lowaltitude UAV swarm ISAC systems. The input-output communication and sensing signal models are derived for the RAA-based UAV ISAC system. Besides, by analyzing the beam pattern of RAA, we rigorously show that RAA can achieve uniform angular resolution across all signal directions, which is strictly better than the conventional ULA that achieves equal array gain. In particular, different from ULA that suffers from poor angular resolution when the user/target is far away from the array boresight, RAA can maintain its high resolution ability in all directions. Besides, we also show that with the same array gain, since each sULA is only responsible for a smaller portion of the angular range, RAA can achieve higher beamforming gain than the conventional ULA since it can use antenna elements with higher directivity, benefiting both communication and sensing.

Next, based on the beam pattern analysis, we design the orientation of each sULA and the ray selection network (RSN) to fully reap the advantages of RAA. We analyze the signal model and propose efficient sensing algorithms for RAA based UAV swarm ISAC with orthogonal frequency division multiplexing (OFDM). In particular, as RAA has different equivalent array response vectors from the conventional ULAs, traditional array structure based sensing algorithms like Periodogram cannot be directly applied. Therefore, multiple signal classification (MUSIC) algorithm tailored for RAA is proposed to estimate the AoAs of targets. Based on these results, we further transform the multiple target estimation problem into single target sensing problem by performing zero forcing (ZF) spatial beamforming on the received signal to filter out the sensing matrix of other targets. Then, for delay and Doppler estimation of each target, we exploit the frequency and symbol diversity of OFDM and apply the 2-D Periodogram algorithm to obtain the delay and Doppler pairs.

• We demonstrate the effectiveness of the proposed RAA based ISAC via extensive numerical results. In particular, we simulate a UAV swarm moving in the air with varying AoAs. For sensing, compared with classic discrete Fourier transform (DFT) codebook based hybrid analog/digital beamforming with ULA, the RAA systems can achieve robust angular estimation across all directions, while the performance of ULA degrades significantly as the targets moving away from the boresight, which confirms the analytical results. In extreme cases when the targets are along the extended line of the linear array, ULA is unable to sense any target even if super-resolution algorithm is used. Moreover, the proposed algorithm also shows effective performance in delay and Doppler estimation. For communication, RAA also outperforms conventional ULA in terms of communication rate, thanks to its larger beamforming gain enabled by antenna elements with higher directivity.

![](images/fee6231e71e24aca680366a7583d202d8551ef83a6a3cc89b9476ba7c2104062.jpg)  
Fig. 1. An illustration of RAA-based ISAC for low-altitude UAV swarm.

The rest of this paper is organized as follows. Section II introduces system model for RAA based UAV swarm ISAC. Section III presents the the comparison of RAA versus conventional ULA. In Section IV, the proposed sensing algorithm for RAA-based OFDM ISAC is presented. Simulation results and performance analysis are detailed in Section V. Finally, we conclude the paper in Section VI.

Notation: Scalars are denoted by italic letters. Vectors and matrices are denoted by boldface lower and upper case letters, respectively. The matrix inverse, transpose, and Hermitian transpose operations are given by $( \cdot ) ^ { - 1 } , \bar { ( } \cdot ) ^ { \mathrm { T } }$ and $( \cdot ) ^ { \mathrm { H } }$ , respectively. The absolute value and $l _ { 2 }$ norm are given by | · | and $\| { \bf \cdot } \| _ { 2 } ,$ , respectively. $\mathbb { C } ^ { M \times N }$ denotes the space of $M \times N$ complex-valued matrices. The operator d·e is an integer ceiling operation, $\delta ( \cdot )$ denotes the Kronecker delta function, and card(·) denotes the cardinality of a set. $j = \sqrt { - 1 }$ denotes the imaginary unit of complex numbers, and <sup>E</sup>(·) denotes the statistical expectation. The distribution of a circularly symmetric complex Gaussian (CSCG) random variable with zero mean and variance $\sigma ^ { 2 }$ is denoted by $\mathcal { C N } ( 0 , \sigma ^ { 2 } )$ and ∼ stands for “distributed $\mathrm { { a s } } ^ { \prime \prime }$

## II. SYSTEM MODEL

## A. UAV Swarm ISAC

As shown in Fig. 1, we consider a low-altitude UAV swarm ISAC system, which consists of a single-antenna ISAC Tx and a multi-antenna ISAC Rx. The channel from the Tx to the Rx comprises one LoS component and L non-line-of-sight (NLoS) components induced by sensing targets. The lth path (l = 0 for LoS) is parameterized by the tuple $\{ \theta _ { l } , \tau _ { l } , f _ { D , l } \}$ which represents the AoA, path delay and Doppler frequency, respectively. The ISAC system simultaneously pursues three key objectives: (1) localization of the ISAC Tx UAV, (2) uplink communication from the ISAC-Tx to the BS, and (3) bi-static sensing of surrounding targets using reflected signals.

To reduce the hardware cost while enhancing the performance, RAA is used at the ISAC Rx. The RAA architecture is composed by N sULAs [45], making them ray-like as shown in Fig. 1. Each sULA has M antenna elements separated by a distance $d \ = \ \lambda / 2 ,$ , with λ being the signal wavelength. Different from the conventional ULA, all the M antenna elements of each sULA are directly combined without any analog or digital beamforming, which justifies the term sULA. In addition, with only $N _ { \mathrm { R F } } \leq N$ RF chains, a RSN is designed to select $N _ { \mathrm { R F } }$ ports from the N equivalent sULA outputs. The RSN is denoted by $\mathbf { S } \in \{ 0 , 1 \} ^ { N _ { \mathrm { R F } } \times N }$ . Note that RSN has the function of selecting $N _ { \mathrm { R F } }$ terms from N elements, so the rows of S are composed of $N _ { \mathrm { R F } }$ rows specially selected from an identity matrix ${ \bf I } _ { N } \in \mathbb { R } ^ { N \times N }$ , i.e., $\mathbf { S } = [ \mathbf { e } _ { i _ { 1 } } , \mathbf { e } _ { i _ { 2 } } , \ldots , \mathbf { e } _ { i _ { N _ { \mathrm { R F } } } } ] ^ { \mathrm { T } }$ where $\mathbf { e } _ { i _ { k } } \in \mathbb { R } ^ { N \times 1 } , k = 1 , \dots , N _ { \mathrm { R F } }$ denotes the $i _ { k } { \mathrm { t h } }$ row of ${ \mathbf { I } } _ { N }$ . After that, the $N _ { \mathrm { R F } }$ selected sULA outputs will be connected to the RF-chains for subsequent baseband digital processing for communication data decoding and sensing parameter estimation.

Let the ISAC signal transmitted by the Tx be $x ( t )$ . The resulting signal at the N sULAs of the RX, denoted by ${ \tilde { \mathbf { y } } } ( t ) \in$

$\mathbb { C } ^ { N \times 1 }$ , is expressed as

$$
\tilde { \mathbf { y } } ( t ) = \int \mathbf { h } ( t , \tau ) x ( t - \tau ) d \tau + \mathbf { z } ( t ) ,\tag{1}
$$

where $\mathbf { h } ( t , \tau ) \in \mathbb { C } ^ { N \times 1 }$ is the equivalent channel between the Tx and the N sULAs that will be modelled in Section II-B, $\mathbf { z } ( t ) \in \mathbb { C } ^ { N \times 1 }$ is the additive white Gaussian noise (AWGN) vector. After passing through the RSN S, the resulting signal $\mathbf { y } ( t ) \in \mathbb { C } ^ { N _ { \mathrm { R F } } \times 1 }$ can be expressed as

$$
\begin{array} { l } { { \displaystyle { \bf y } ( t ) = { \bf S } { \tilde { \bf y } } ( t ) } \ ~ } \\ { { \displaystyle ~ = { \bf S } \int { { \bf h } ( t , \tau ) } x ( t - \tau ) d \tau + { \bf S } { \bf z } ( t ) } . } \end{array}\tag{2}
$$

In the following, we will introduce the specific design of RAA, RSN, and derive the equivalent channel vector $\mathbf { h } ( t , \tau )$

## B. RAA-Based ISAC

As a novel multi-antenna architecture, the RAA system employs N radially arranged sULAs with M elements each, as shown in Fig. 1. We establish a Cartesian coordinate system so that the sULA indexed by n = 0 aligns with the positive z-axis, as shown in Fig. 1. Furthermore, the orientation of the nth sULA with respect to (w.r.t.) the positive z-axis is denoted by $\eta _ { n } ~ \in ~ [ - \eta _ { \mathrm { m a x } } , \eta _ { \mathrm { m a x } } ]$ , with $\eta _ { \mathrm { m a x } }$ denoting the maximum orientation and $\eta _ { 0 } ~ = ~ 0$ , where $\textit { n } \in \textit { N }$ with $\begin{array} { r } { \mathcal { N } = \{ - \frac { N - 1 } { 2 } , \dots , 0 , \dots , \frac { N - 1 } { 2 } \} } \end{array}$ being the set of sULA index, assuming N is an odd number for notational convenience. To avoid strong mutual coupling for antenna elements across different sULAs, the first element of each sULA has a distance D from the origin. Thus, the RAA is characterized by the set of parameters $( N , M , D , \{ \eta _ { n } \} _ { n \in \mathcal { N } } )$

Consider the incoming signal from a certain path with a given elevation AoA w.r.t. the negative x-axis, denoted by $\theta ,$ with $\theta \in ( - \pi / 2 , \pi / 2 ]$ . Therefore the array response vector of a certain sULA with orientation η for path angle θ can be expressed as [45]

$$
\mathbf { a } ( \theta , \eta ) = [ 1 , e ^ { j \pi \sin ( \theta - \eta ) } , \ldots , e ^ { j \pi ( M - 1 ) \sin ( \theta - \eta ) } ] ^ { \mathrm { T } } .\tag{3}
$$

Thus, we may define the array response matrix of the RAA, denoted by $\mathbf { A } ( \mathbf { \bar { \theta } } ) \in \mathbb { C } ^ { M \times N }$ , given by

$$
\mathbf { A } ( \theta ) = [ \mathbf { a } ( \theta , \eta _ { n } ) ] _ { n \in \mathcal { N } } \times \mathrm { d i a g } ( \mathbf { b } ) ,\tag{4}
$$

where $\mathbf { b } = [ b ( \theta - \eta _ { n } ) ] _ { n \in \mathcal { N } } \in \mathbb { C } ^ { N \times 1 }$ captures the response of the reference element of each sULA, say the first element, given by

$$
b ( \theta - \eta _ { n } ) = e ^ { j \frac { 2 \pi } { \lambda } D \sin ( \theta - \eta _ { n } ) } \sqrt { G ( \theta - \eta _ { n } ) } ,\tag{5}
$$

where the term $e ^ { j { \frac { 2 \pi } { \lambda } } D \sin ( \theta - \eta _ { n } ) }$ represents the phase shift of the first element of the nth sULA relative to the original point, and the second term $G ( \theta \mathrm { ~ - ~ } \eta _ { n } )$ accounts for the radiation pattern of each antenna element in the nth sULA, and it is characterized by the peak antenna gain $G ( 0 )$ , the 3dB beamwidth $\theta _ { \mathrm { 3 d B } }$ , and the total power gain denoted by $\begin{array} { r } { G _ { \mathrm { s u m } } = \int _ { - \pi } ^ { \pi } G ( \theta ) d \theta . } \end{array}$

With all the M antenna elements of each sULA directly connected, the resulted array response vector for all the N sULAs, denoted by $\mathbf { r } ( \theta ) \in \dot { \mathbb { C } } ^ { N \times 1 }$ , is expressed as

$$
\begin{array} { r l } & { \mathbf { r } ( \theta ) = \mathbf { A } ( \theta ) ^ { \mathrm { T } } \mathbf { 1 } _ { M \times 1 } = \operatorname { d i a g } ( \mathbf { b } ) \left[ \mathbf { a } ( \theta , \eta _ { n } ) ^ { \mathrm { T } } \mathbf { 1 } _ { M \times 1 } \right] _ { n \in \mathcal { N } } } \\ & { \quad \quad = \operatorname { d i a g } ( \mathbf { b } ) \left[ M H _ { M } \left( \sin ( \theta - \eta _ { n } ) \right) \right] _ { n \in \mathcal { N } } , } \end{array}\tag{6}
$$

where $\begin{array} { r } { H _ { M } \left( \sin ( \theta - \eta _ { n } ) \right) = \frac { 1 } { M } \mathbf { a } ( \theta , \eta _ { n } ) ^ { T } \mathbf { 1 } _ { M \times 1 } } \end{array}$ is the Dirichlet kernel function given by

$$
H _ { M } \left( x \right) = e ^ { j \frac { \pi } { 2 } \left( M - 1 \right) x } \frac { \sin \left( \frac { \pi } { 2 } M x \right) } { M \sin \left( \frac { \pi } { 2 } x \right) } .\tag{7}
$$

Based on (6), the response of the nth sULA with AoA θ is

$$
r ( \theta , \eta _ { n } ) = M b ( \theta - \eta _ { n } ) H _ { M } \left( \sin ( \theta - \eta _ { n } ) \right) .\tag{8}
$$

As a result, for the UAV swarm ISAC system with one LoS component and L NLoS components, the equivalent channel $\mathbf { h } ( t , \tau )$ in (1) between the Tx and the N sULAs of the RAA can be expressed as

$$
{ \bf h } ( t , \tau ) = \sum _ { l = 0 } ^ { L } \alpha _ { l } { \bf r } ( \theta _ { l } ) \delta ( \tau - \tau _ { l } ) e ^ { j 2 \pi f _ { D , l } t } ,\tag{9}
$$

where $\alpha _ { l }$ denotes the path coefficient, $\theta _ { l } , \tau _ { l }$ , and $f _ { D , l }$ respectively denote the path AoA, delay and Doppler frequency. By substituting (9) into (2), the resulting signal at the RX for RAA-based ISAC system is

$$
\mathbf { y } ( t ) = \mathbf { S } \sum _ { l = 0 } ^ { L } \alpha _ { l } \mathbf { r } ( \theta _ { l } ) e ^ { j 2 \pi f _ { D , l } t } x ( t - \tau _ { l } ) + \mathbf { S } \mathbf { z } ( t ) .\tag{10}
$$

Due to the limited RF chains, we need to choose $N _ { \mathrm { R F } }$ out of N RAA outputs. To fully exploit the energy-focusing ability of RAA, we propose the simple energy based ray selection, i.e., S is selected based on this criterion: max $\| \mathbf { y } ( t ) \| _ { 2 } ^ { 2 }$ , where the $N _ { \mathrm { R F } }$ RAA outputs with the maximum sum energy are chosen. To realize the energy based ray selection, we only need to sweep all the RAA ports to obtain full information about the response magnitude of different sULAs. The switching time for the RF components is typically on the order of microseconds, which is comparable to the duration of a single OFDM symbol in typical systems. Besides, thanks to the parallel processing capability of the RAA architecture with $N _ { \mathrm { R F } }$ RF chains, the exhaustive sweeping across all N ports is effectively parallelized. This would require $\left\lceil \frac { N } { N _ { \mathrm { R F } } } \right\rceil$ sweeps or symbol time to cover all the N sULAs. This entire process is completed well within a single CPI, as validated in the simulation, where the channel parameters, including the AoAs, are assumed to be constant. Therefore, S will be determined and fixed for the subsequent analysis.

## III. RAA VERSUS CONVENTIONAL ULA

On the basis of the RAA models presented in Section II, in this section we analyze the corresponding beam patterns for RAA and compare it with conventional ULA which employs DFT codebook based HBF. Beam pattern characterizes the intensity variation of a beam designed for a certain desired direction $\theta ^ { \prime }$ as a function of the actual observation direction θ. It is crucial for ISAC as it reflects the level of angular resolution ability for sensing and inter-user interference (IUI) suppression capability for communication. For the conventional ULA with M antenna elements, with a beamforming vector $\mathbf { v } ( \theta ^ { \prime } ) \in \mathbb { C } ^ { M \times 1 }$ aiming to beamsteer energy towards the desired direction $\theta ^ { \prime } { } .$ , the beam pattern at the observation direction θ is defined as

$$
\begin{array} { r l r } & { } & { \mathcal { G } _ { \mathrm { U L A } } ( \theta , { \boldsymbol { \theta } } ^ { \prime } ) \triangleq \Big | \sqrt { G _ { \mathrm { U L A } } ( \theta ) } { \mathbf { v } } ^ { \mathrm { H } } ( { \boldsymbol { \theta } } ^ { \prime } ) { \mathbf { a } } ( \theta ) \Big | } \\ & { } & { = \Big | \sqrt { G _ { \mathrm { U L A } } ( \theta ) } { \mathbf { a } } ^ { \mathrm { H } } ( { \boldsymbol { \theta } } ^ { \prime } ) { \mathbf { a } } ( { \boldsymbol { \theta } } ) \Big | , } \end{array}\tag{11}
$$

where $\mathbf { a } ( \theta ) \in \mathbb { C } ^ { M \times 1 }$ is the array response vector of ULA at the observation direction θ that will be given in this section. The second equality follows by applying the analog maximal-ratio transmission (MRT) beamforming, i.e. $\mathbf { v } ( \theta ^ { \prime } ) \ = \ \mathbf { a } ( \theta ^ { \prime } )$ , and $G _ { \mathrm { U L A } } ( \theta )$ denotes the radiation pattern of each antenna element in ULA, characterized by the peak antenna gain $G _ { \mathrm { U L A } } ( 0 )$ the 3dB beamwidth $\theta _ { \mathrm { 3 d B } } ^ { \mathrm { U L } \bar { \mathrm { A } } }$ , and the total power gain denoted by $\begin{array} { r } { G _ { \mathrm { U L A } } ^ { \mathrm { s u m } } = \int _ { - \pi } ^ { \pi } G _ { \mathrm { U L A } } ( \theta ) d \theta } \end{array}$ . For RAA, based on (8), the desired direction $\theta ^ { \prime }$ achieves the maximum power by selecting the sULA with array orientation matching the desired signal direction, i.e., $\eta _ { n } = \theta ^ { \prime }$ . Therefore, the beam pattern of RAA can be defined as

$$
\mathcal { G } _ { \mathrm { R A A } } ( \theta , \theta ^ { \prime } ) \triangleq \Big | r ( \theta , \theta ^ { \prime } ) \Big | ,\tag{12}
$$

where $r ( \theta , \theta ^ { \prime } )$ is defined in (8). Based on beam pattern, we can have the definition of angular resolution:

Definition 1: The angular resolution $\gamma$ of any type of array is a function of the desired signal direction $\theta ^ { \prime } { } .$ which is defined as half of the main lobe beam width $\Delta _ { \theta }$ of its beam pattern $\mathcal { G } ( \theta , \theta ^ { \prime } )$ , i.e.,

$$
\gamma ( \theta ^ { \prime } ) = \frac { 1 } { 2 } \Delta _ { \theta } ,\tag{13}
$$

where $\Delta _ { \theta } = \left| \theta _ { 1 } - \theta _ { 2 } \right|$ , with $\theta _ { 1 }$ and $\theta _ { 2 }$ being the first right and left null points of $\mathcal { G } ( \theta , \theta ^ { \prime } )$ for any given desired direction θ<sup>0</sup>, i.e.,

$$
\theta _ { 1 } = \operatorname* { m i n } _ { \theta } \ \left\{ \theta > \theta ^ { \prime } \big | \mathcal { G } ( \theta , \theta ^ { \prime } ) = 0 \right\} .\tag{14}
$$

$$
\theta _ { 2 } = \operatorname* { m a x } _ { \theta } \ : \left\{ \theta < \theta ^ { \prime } \big | \mathcal { G } ( \theta , \theta ^ { \prime } ) = 0 \right\} .\tag{15}
$$

Remark 1: With finite number of sULAs, the sULA orientation may fail to match with the desired direction, i.e. $\eta _ { n } \neq \theta ^ { \prime } , \forall n$ . For Definition 1, it suffices to guarantee that the set of N sULAs collectively covers all directions, so that any arbitrary direction $\theta ^ { \prime }$ falls within the main lobe of at least one sULA (such as sULA k). In this case, we have

$$
\mathcal G _ { \mathrm { R A A } } ( \theta , \theta ^ { \prime } ) = \Big | r ( \theta , \eta _ { k } ) \Big | .\tag{16}
$$

## A. Beam Pattern and Angular Resolution of RAA

To achieve effective interference suppression between adjacent sULAs, as proposed in [45], the angular null position of one sULA’s principal lobe is designed to align with the peak direction of its adjacent counterpart. In this case, the orientation of the N sULAs are designed as

$$
\eta _ { n } = n \times \arcsin ( 2 / M ) , \forall n \in \mathcal { N } .\tag{17}
$$

This closed-form solution ensures orthogonality between adjacent sULAs while maintaining full angular coverage.

There will be a total of $\begin{array} { r } { N = \mathrm { ~ 2 ~ } \Big \lvert \frac { \eta _ { \mathrm { m a x } } } { \arcsin ( 2 / M ) } + 1 \Big \rvert } \end{array}$ sULAs in RAA. If the RAA needs to cover the half space so that $\eta _ { \mathrm { m a x } } ~ = ~ \pi / 2$ , then $N ~ \approx ~ \left\lfloor ( \pi M / 2 ) \right\rfloor$ when $M \ \gg \ 1$ . In addition, to ensure all antenna elements are separated by at least half wavelength, the distance D needs to satisfy $D \geq \lambda / ( 4 \sin ( 0 . 5 \arcsin ( 2 / M ) ) )$ .

By substituting (5) and (8) into (12), the beam pattern of RAA can be expressed as

$$
\mathcal { G } _ { \mathrm { R A A } } ( \theta , \theta ^ { \prime } ) = M \sqrt { G ( \theta - \theta ^ { \prime } ) } \bigg \vert H _ { M } \left( \sin ( \theta - \theta ^ { \prime } ) \right) \bigg \vert .\tag{18}
$$

With beam pattern $\mathcal { G } ( \theta , \theta ^ { \prime } )$ in (18), we try to derive the angular resolution of RAA. For convenience, we make the assumption that the beamwidth of each antenna element $G ( \zeta )$ is wider than that of $H _ { M } \left( \sin ( \theta - \theta ^ { \prime } ) \right)$ ). Therefore, we have the following theorem:

Theorem 1: Assuming that all directions are covered with the N sULAs, for any desired direction $\theta ^ { \prime }$ , the angular resolution of RAA is a constant, given by

$$
\gamma _ { \mathrm { R A A } } ( \theta ^ { \prime } ) = \gamma _ { \mathrm { R A A } } = \arcsin \frac { 2 } { M } , \forall \theta ^ { \prime } .\tag{19}
$$

Proof: Based on (18), by letting si $\begin{array} { r } { \mathrm { ~  ~ \psi ~ } _ { 1 } ( \theta - \theta ^ { \prime } ) = \pm \frac { 2 } { M } } \end{array}$ , we have $H _ { M } \left( \sin ( \theta - \theta ^ { \prime } ) \right) = 0 .$ . Thus, according to Definition 1, $\theta _ { 1 } = \theta ^ { \prime } +$ arcsin $\left( { \frac { 2 } { M } } \right) , \theta _ { 2 } = \theta ^ { \prime } -$ arcsin $\left( { \frac { 2 } { M } } \right)$ , so the main lobe beam width can be obtained as $\begin{array} { r } { \Delta _ { \theta } = | \theta _ { 1 } { - } \theta _ { 2 } | = 2 \arcsin \left( \frac { 2 } { M } \right) } \end{array}$ which yields $\begin{array} { r } { \gamma _ { \mathrm { R A A } } = \frac 1 2 \Delta _ { \theta } = } \end{array}$ arcsin $\frac { 2 } { M }$

Theorem 1 demonstrates that RAA achieves uniform angular resolution across all signal directions, i.e., it is independent of the desired signal direction $\theta ^ { \prime }$ . When $\begin{array} { r } { M \gg 1 , \gamma _ { \mathrm { R A A } } \approx \frac { 2 } { M } } \end{array}$ which is inverse proportional to the aperture of the sULA.

Note that for RAA, each sULA is only responsible for a small portion of the whole angular range from $[ - \eta _ { \mathrm { m a x } } , \eta _ { \mathrm { m a x } } ]$ Therefore, different from the conventional antenna arrays where the antenna elements are shared by all beams or signal directions, we can use antenna elements with stronger directivity to enhance the overall beamforming gain as rigorously proved in [46].

Fig. 2a illustrates the beam patterns of the different sULAs in the proposed RAA architecture, where $M \ = \ 8$ and $\theta _ { \mathrm { { m a x } } } ~ = ~ \eta _ { \mathrm { { m a x } } } ~ = ~ \pi / 2$ . The antenna element pattern adopts the 3GPP radiation pattern [47], where we set $\theta _ { \mathrm { 3 d B } } = 0 . 3 \pi$ and $G _ { \mathrm { d B } } ( 0 ) = 5 . 1 3 ~ \mathrm { d B }$ . It reveals two key characteristics of RAA:

• Full angular coverage: For any signal with AoA $\theta ,$ there exists at least one sULA exhibiting a dominant main lobe response.

• Uniform angular resolution: The resolution $\gamma _ { \mathrm { R A A } }$ remains the same across all directions, as mathematically proved in Theorem 1 and verified numerically in Fig. 2a.

## B. Beam Pattern and Angular Resolution of Conventional ULA

As illustrated in Fig. 3, we use conventional ULA which employs DFT codebook based HBF as a benchmark comparison.To ensure fair comparison, we assume that the RAA and ULA have the same number of RF-chains $N _ { \mathrm { R F } }$ and array gain M. The array response vector of the Melement ULA is $\mathbf { a } ( \theta ) \ = \ [ e ^ { j \in m - 1 ) \sin \theta } ] _ { 1 \leq m \leq M } \ \in \ \mathbb { C } ^ { M \times 1 }$ The DFT codebook for the HBF architecture is denoted by $\mathbf { A } _ { \mathrm { D F T } } \ = \ \mathsf { \Gamma } [ \mathbf { a } ( \varphi _ { n } ) ] _ { n , \epsilon , N ^ { \prime } } \ \in \ \mathbb { C } ^ { M \times M }$ , where $\begin{array} { l } { \mathbf { a } ( \varphi _ { n } ) } & { = } \end{array}$ $\left[ e ^ { j \pi ( m - 1 ) \sin \varphi _ { n } } \right] _ { 1 < m < M } \in \mathbb { C } ^ { M \times 1 }$ is the nth DFT codeword, $\mathcal { N } ^ { \prime } = \{ 1 , 2 , \dots , \overset { \cdot } { M } \}$ is the index set of DFT codewords, and sin $\varphi _ { n } = - 1 + 2 ( n - 1 ) / M$

![](images/38e49509b8af113066fcd46714d35dd1920c4e4d70fe3c5621f8f606f3d70148.jpg)  
(a) RAA beam patterns

![](images/3b628a8850f51c3d18f3d857b0dd5f5a2e8a6b047f8d4d9a126c71a9ef64c7f5.jpg)  
(b) HBF ULA beam patterns

Fig. 2. The beam patterns for (a) RAA, where each curve represents the response of one sULA. (b) ULA, where each curve corresponds to one codeword in the DFT codebook. Both RAA and ULA achieves the same array gain $M \stackrel { = } { = } 8 ,$ but RAA achieves uniform angular resolution and higher beamforming gain.  
![](images/ad4d16f9adaacf5cc7996d4272a4069dcd63a4bd2cc4cefa31e7ee10412094cc.jpg)  
Fig. 3. An illustration of conventional ULA-based ISAC for low-altitude UAV swarm.

Note that for ULA, the whole angular range needs to be covered by a single antenna array. This implies that each element of ULA should have a wider coverage (or smaller directivity) than that of RAA, i.e. $\theta _ { \mathrm { 3 d B } } ^ { \mathrm { U L A } } > \theta _ { \mathrm { 3 d B } } \ [ 4 6 ]$

By substituting the array response vector ${ \bf a } ( \theta )$ into (11), the beam pattern of ULA is

$$
\mathcal { G } _ { \mathrm { U L A } } ( \theta , \theta ^ { \prime } ) = M \sqrt { G _ { \mathrm { U L A } } ( \theta ) } \Big \vert H _ { M } \left( \sin \theta - \sin \theta ^ { \prime } \right) \Big \vert .\tag{20}
$$

Note that at the first glance, the beam pattern of ULA in (20) looks very similar to that of RAA in (18). However, they have two important differences. Firstly, they have different antenna element radiation pattern of $G _ { \mathrm { U L A } } ( \theta )$ and $G ( \theta - \theta ^ { \prime } )$ respectively. Secondly, their variables in the Dirichlet kernel function are not the same, which are sin $\theta \ : - \ : \sin \theta ^ { \prime }$ and sin $( \theta - \theta ^ { \prime } )$ for ULA and RAA, respectively.

Fig. 2b shows the beam patterns of ULA under different desired direction $\theta ^ { \prime }$ for $M \ = \ 8$ and $\theta _ { \mathrm { { m a x } } } ~ = ~ \pi / 2$ with $\theta _ { \mathrm { 3 d B } } ^ { \mathrm { U L A } } ~ = ~ \pi$ and $G _ { \mathrm { d B } } ^ { \mathrm { U L A } } ( 0 ) ~ = ~ 0 { \mathrm { d B } } ~$ , ensuring that the total radiation power satisfies $G _ { \mathrm { U L A } } ^ { \mathrm { s u m } } ~ = ~ G _ { \mathrm { s u m } }$ . It can be found that both RAA and ULA have full array gain when θ matches with $\theta ^ { \prime } ,$ i.e. $H _ { M } ( \sin \theta - \sin \theta ^ { \prime } ) \Big | _ { \theta = \theta ^ { \prime } } \ = \ 1$ and $H _ { M } ( \sin ( \theta - \theta ^ { \prime } ) ) \Big | _ { \theta = \theta ^ { \prime } } = 1$ . However, with higher directional antenna elements, RAA can achieve higher overall beamforming gain compared to ULA. Besides, it is noteworthy that when $\theta ^ { \prime }$ grows larger, the mainlobe of ULA beam pattern becomes wider, as rigorously shown by the following theorem:

![](images/8dc5e6d0c21a5628d19aef32f72b0270bc7637a1fe8013cb7fb629de8190dc0d.jpg)  
Fig. 4. The comparision of angular resolution of RAA versus the conventional ULA, for $M = \stackrel { \cdot } { 1 } 2 8$

Theorem 2: The angular resolution of ULA as a function of the desired signal direction $\theta ^ { \prime }$ is

$$
\gamma _ { \mathrm { U L A } } ( \theta ^ { \prime } ) = \frac { 1 } { 2 } \arcsin \left( \sin \theta ^ { \prime } + \frac { 2 } { M } \right) - \frac { 1 } { 2 } \arcsin \left( \sin \theta ^ { \prime } - \frac { 2 } { M } \right)
$$

where $\theta ^ { \prime }$ satisfies $\begin{array} { r } { - 1 + \frac { 2 } { M } \le \sin \theta ^ { \prime } \le 1 - \frac { 2 } { M } } \end{array}$

Proof: Based on Definition 1 and $\mathcal { G } _ { \mathrm { U L A } } ( \theta , \theta ^ { \prime } )$ in (20), by letting sin θ − sin $\begin{array} { l l l } { \theta ^ { \prime } } & { = } & { \pm \frac { 2 } { M } } \end{array}$ , we will get $\theta \quad =$ arcsin  sin $\begin{array} { r } { \theta ^ { \prime } \pm \frac { 2 } { M } ) } \end{array}$ , and we have $H _ { M }$ (sin $\theta - \sin \theta ^ { \prime } ) = 0 .$ Therefore, the main lobe beam width can be obtained as $\Delta _ { \theta } =$ arcsin  sin $\textstyle { \theta ^ { \prime } + \frac { 2 } { M } } )$ −arcsin  sin $\textstyle \theta ^ { \prime } - { \frac { 2 } { M } } \ O \Big )$ , which yields $\begin{array} { r } { \gamma _ { \mathrm { U L A } } ( \theta ^ { \prime } ) = \frac { 1 } { 2 } } \end{array}$ arcsin $( \sin \theta ^ { \prime } + { \frac { 2 } { M } } ) \dot { - } { \frac { 1 } { 2 } }$ arcsin $\left( \sin \theta ^ { \prime } - \frac { 2 } { M } \right)$

Theorem 2 demonstrates that different from that for RAA in Theorem 1, the angular resolution of ULA in general gets worse at higher AoA. In extreme cases where sin $\theta ^ { \prime } =$ $\begin{array} { r } { \dot { { \bf \Phi } } \pm \left( 1 - \frac { 2 } { M } \right) } \end{array}$ , we have $\begin{array} { r } { \gamma _ { \mathrm { U L A } } ( \theta ^ { \prime } ) = \frac { \pi } { 4 } - \frac { 1 } { 2 } } \end{array}$ arcsin $\textstyle \left( 1 - { \frac { 4 } { M } } \right) \geq$ $\textstyle { \sqrt { \frac { 2 } { M } } }$ . When $M = 1 6 , \gamma _ { \mathrm { U L A } } ( \theta ^ { \prime } ) \geq 0 . 3 5 \mathrm { r a d } \approx 2 0 ^ { \circ }$ . Note that $\begin{array} { r } { \dot { \gamma } _ { \mathrm { U L A } } ( 0 ) = \arcsin \left( \frac { 2 } { M } \right) = \gamma _ { \mathrm { R A A } } . } \end{array}$

Theorem 3: For equal array gain factor M, the angular resolution of RAA is always superior than that of ULA, i.e.,

$$
\gamma _ { \mathrm { U L A } } ( \theta ^ { \prime } ) \geq \gamma _ { \mathrm { R A A } } ( \theta ^ { \prime } ) = \arcsin \left( \frac { 2 } { M } \right) , \forall \theta ^ { \prime } .\tag{22}
$$

where the equality holds if and only if $\theta ^ { \prime } = 0$

Proof: Please refer to Appendix.

The resolution comparison established in Theorem 3 is also illustrated in Fig. 4. It is observed that when the desired direction $\theta ^ { \prime }$ deviates from the boresight angle, the main lobe of the conventional ULA beam pattern becomes wider. When the communication user or sensing targets are located at a direction with large $\theta ^ { \prime }$ , ULA may fail to distinguish them due to the poor angular resolution. However, RAA is able to achieve uniform angular resolution of arcsin $\frac { 2 } { M }$ across all directions $\theta ^ { \prime } { } .$ , making it quite appealing for IUI suppression for multi-user communication and multi-target resolution for sensing.

Furthermore, to quantitatively evaluate the hardware cost advantage of the proposed RAA architecture, a comparison is made against the classic HBF system. The key hardware components and their quantities for both architectures are summarized in Table I, where the number of sULAs is approximated by $\begin{array} { r } { N = \mathrm { ~ 2 ~ } \Big | \frac { \eta _ { \operatorname* { m a x } } } { \arcsin ( 2 / M ) } + 1 \Big | \ \approx \ M \eta _ { \operatorname* { m a x } } } \end{array}$ .Compared to the fully-connected HBF architecture that requires $M N _ { \mathrm { R F } }$ phase shifters and M antennas, the proposed $\mathbf { R A A }$ architecture requires only $N _ { \mathrm { R F } } M \eta _ { \mathrm { m a x } }$ RF switches and $M ^ { 2 } \eta _ { \mathrm { m a x } }$ antenna elements. Since phase shifters are typically much more expensive than antenna elements and switches, the RAA architecture can significantly reduce hardware costs. The main hardware costs of the RAA and HBF architectures can be expressed as

TABLE I  
COMPARISON OF KEY HARDWARE COMPONENTS
<table><tr><td rowspan=1 colspan=1>Component</td><td rowspan=1 colspan=1>RAA</td><td rowspan=1 colspan=1>HBF</td></tr><tr><td rowspan=1 colspan=1>Antenna elements</td><td rowspan=1 colspan=1> $\overline { { M ^ { 2 } \eta _ { \mathrm { m a x } } } }$ </td><td rowspan=1 colspan=1>M</td></tr><tr><td rowspan=1 colspan=1>RF switches</td><td rowspan=1 colspan=1> $\overline { { N _ { \mathrm { R F } } M \eta _ { \mathrm { m a x } } } }$ </td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>Phase shifters</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1> $\overline { { N _ { \mathrm { R F } } M } }$ </td></tr></table>

$$
\mathrm { c o s t } _ { \mathrm { R A A } } = N _ { \mathrm { R F } } M \eta _ { \mathrm { m a x } } p _ { \mathrm { s w } } + M ^ { 2 } \eta _ { \mathrm { m a x } } p _ { \mathrm { a n t } } ,\tag{23}
$$

$$
\mathrm { c o s t } _ { \mathrm { H B F } } = N _ { \mathrm { R F } } M p _ { \mathrm { p s } } + M p _ { \mathrm { a n t } } ,\tag{24}
$$

where $p _ { \mathrm { s w } } , ~ p _ { \mathrm { a n t } } ,$ and $p _ { \mathrm { p s } }$ represent the unit prices of RF switches, antenna elements, and phase shifters, respectively.

Consider an example of a communication system operates at the carrier frequency of 38 GHz employing the TGP2108- SM 6-bit digital phase shifter and the QM12002 RF switch. The hardware cost is estimated based on the unit prices of individual components, referenced from Qorvo’s official data [48]. The unit prices of different components are as follows: RF switch at 14.3\$, antenna element at 0.01\$, and phase shifter at 131.2\$. The system parameters for this evaluation are: the number of antenna elements in the ULA $M = 1 2 8$ , number of RF chains $N _ { \mathrm { R F } } = 1 6$ , and number of sULAs for the RAA is $\begin{array} { r } { N = 2 \left| \frac { \eta _ { \mathrm { m a x } } } { \arcsin ( 2 / M ) } + 1 \right| = 2 0 1 } \end{array}$ . The total hardware costs for the two architectures are calculated as $\mathrm { c o s t } _ { \mathrm { R A A } } = 4 6 2 7 8 \ S$ and $\mathrm { c o s t } _ { \mathrm { U L A } } ~ = ~ 2 6 8 7 0 0 \ S$ . The results demonstrate that the proposed RAA architecture achieves a significant cost reduction, with its total cost being approximately 17.2% of the HBF cost: $\mathrm { c o s t } _ { \mathrm { R A A } } \approx 1 7 . 2 \% \cdot \mathrm { c o s t } _ { \mathrm { U L A } }$ .This substantial cost saving primarily stems from the RAA architecture’s elimination of the need for costly phase shifters, which constitute a major expense in the HBF system. By replacing a large number of phase shifters with more economical RF switches, the RAA architecture offers a hardware-efficient solution for highfrequency wireless systems.

In summary, the comparison of RAA and conventional ULA demonstrates the following advantages of RAA:

• Higher beamforming gain: RAA has higher overall beamforming gain since it can use antenna elements with higher directivity.

• Uniform angular resolution: RAA can achieve uniform angular resolution across all signal directions.

• Cost effective: RAA is more cost effective since no single phase shifter is needed, which is typically expensive and difficult to design, especially for high-frequency systems.

## IV. SENSING ALGORITHM FOR RAA-BASED OFDM-ISAC A. RAA-Based OFDM-ISAC

In this section, we apply the proposed RAA-based ISAC system with OFDM waveform [11]. Let $N _ { \mathrm { s c } }$ denote the number of subcarriers and $M _ { \mathrm { s y m } }$ being the number of OFDM symbols within a coherent processing interval (CPI). The system bandwidth is $B ,$ , and the subcarrier spacing is $\Delta f =$ $B / N _ { \mathrm { s c } } ~ = ~ 1 / T$ , where $T$ represents the OFDM symbol duration before adding the cyclic prefix (CP). The duration of CP is denoted as $T _ { \mathrm { c p } }$ . Then, the OFDM symbol duration including CP is $T _ { \mathrm { s } } = T \mathrm { { + } } T _ { \mathrm { c p } }$ . Denote the communication data of subcarrier p and symbol q as $d _ { p q } \in \mathbb { C }$ with $\mathbb { E } [ | d _ { p q } | ^ { 2 } ] = P _ { t }$ where $P _ { t }$ is the transmit power. After IFFT and adding CP, the transmitted signal $x ( t )$ in (1) can be expressed as [11]

$$
x ( t ) = \sum _ { p = 0 } ^ { N _ { \mathrm { s c } } - 1 } \sum _ { q = 0 } ^ { M _ { \mathrm { s y m } } - 1 } d _ { p q } e ^ { j 2 \pi p \Delta f ( t - q T _ { \mathrm { s } } - T _ { \mathrm { c p } } ) } \mathrm { r e c t } \left( \frac { t - q T _ { \mathrm { s } } } { T _ { \mathrm { s } } } \right) .\tag{25}
$$

Then, substituting (9) and (25) into (1), the resulting signal by the N sULAs at the Rx side before RSN can be expressed as

$$
\begin{array} { l }  { \displaystyle { \widetilde { \mathbf { y } } ( t ) = \sum _ { l = 0 } ^ { L } \sum _ { p = 0 } ^ { N _ { \mathrm { s c } } - 1 } \sum _ { q = 0 } ^ { M _ { \mathrm { s y m } } - 1 } \alpha _ { l } \mathbf { r } ( \theta _ { l } ) d _ { p q } e ^ { j 2 \pi p \Delta f ( t - \tau _ { l } - q T _ { \mathrm { s } } - T _ { \mathrm { c p } } ) } } } \\ { { \displaystyle ~ \times e ^ { j 2 \pi f _ { D , l } t } \mathrm { r e c t } \left( \frac { t - \tau _ { l } - q T _ { \mathrm { s } } } { T _ { \mathrm { s } } } \right) + \mathbf { z } ( t ) } , ~ } \end{array}
$$

where $\begin{array} { r } { \mathbf { z } ( t ) = \left[ \sum _ { m = 0 } ^ { M - 1 } z _ { m , n } ( t ) \right] _ { n \in \mathcal { N } } } \end{array}$ , and $z _ { m , n } ( t )$ denotes the noise from the mth element of the nth sULA.

By subsituting (5) and (6) into (26), the received signal of each of the N sUL $\mathcal { A } \widetilde { y } _ { n } ( t )$ can be further written as

$$
\begin{array} { r l r } & { } & { \tilde { y } _ { n } ( t ) = \displaystyle \sum _ { l = 0 } ^ { L } \sum _ { p = 0 } ^ { N _ { \mathrm { s c } } - 1 } \sum _ { q = 0 } ^ { M _ { \mathrm { s y m } } - 1 } \bar { \alpha } _ { n , l } d _ { p q } e ^ { j 2 \pi p \Delta f ( t - \tau _ { l } - q T _ { \mathrm { s } } - T _ { \mathrm { c p } } ) } } \\ & { } & { e ^ { j 2 \pi f _ { D , l } t } \mathrm { r e c t } \left( \frac { t - \tau _ { l } - q T _ { \mathrm { s } } } { T _ { \mathrm { s } } } \right) + z _ { n } ( t ) , \qquad ( 2 } \end{array}\tag{7}
$$

where α¯<sub>n,l</sub> = α<sub>l</sub>b(θ<sub>l</sub> − η<sub>n</sub>)M H<sub>M</sub> (sin(θ<sub>l</sub> − η<sub>n</sub>)) , z<sub>n</sub>(t) = $\textstyle \sum _ { m = 0 } ^ { M - 1 } z _ { m , n } ( t )$

By substituing (9) and (25) into (2), the resulting signal at the RX is

$$
\begin{array} { l } { { \displaystyle { \bf y } ( t ) = { \bf S } \tilde { \bf y } ( t ) = { \bf S } \sum _ { l = 0 } ^ { L } \sum _ { p = 0 } ^ { N _ { \mathrm { s c } } - 1 } \sum _ { q = 0 } ^ { M _ { \mathrm { s y m } } - 1 } \alpha _ { l } { \bf r } ( \theta _ { l } ) d _ { p q } } } \\ { { \displaystyle e ^ { j 2 \pi p \Delta f ( t - \tau _ { l } - q T _ { \mathrm { s } } - T _ { \mathrm { c p } } ) } e ^ { j 2 \pi f _ { D , l } t } \mathrm { r e c t } \left( \frac { t - \tau _ { l } - q T _ { \mathrm { s } } } { T _ { \mathrm { s } } } \right) + { \bf S } { \bf z } ( t ) } . } \end{array}\tag{28}
$$

After RSN, the received signal in (28) is first divided into $M _ { \mathrm { s y m } }$ blocks with equal block duration $T _ { \mathrm { s } }$ . The qth block is given by

$$
{ \bf y } _ { q } ( t ) = { \bf y } \left( t + q T _ { \mathrm { s } } \right) \mathrm { r e c t } \left( \frac { t } { T _ { \mathrm { s } } } \right) .\tag{29}
$$

Then, the CP removal is performed on ${ \bf y } _ { q } ( t )$

$$
{ \bar { \mathbf { y } } } _ { q } ( t ) = \mathbf { y } _ { q } ( t + T _ { \mathrm { c p } } ) \mathrm { r e c t } \left( { \frac { t } { T } } \right) .\tag{30}
$$

Assuming that the CP duration is larger than the maximum delay, i.e., $T _ { \mathrm { c p } } > \operatorname* { m a x } ( \tau _ { l } )$ ), we have

$$
\begin{array} { l } { { \displaystyle \bar { \bf y } _ { q } ( t ) = { \bf S } \sum _ { l = 0 } ^ { L } \sum _ { p = 0 } ^ { N _ { \mathrm { s c } } - 1 } \alpha _ { l } { \bf r } ( \theta _ { l } ) d _ { p q } e ^ { j 2 \pi p \Delta f ( t - \tau _ { l } ) } e ^ { j 2 \pi f _ { D , l } ( t + q T _ { \mathrm { s } } } } } \\ { { \displaystyle \quad \quad + T _ { \mathrm { c p } } ) } } \\ { { \displaystyle \quad \times \mathrm { r e c t } \left( \frac { t } { T } \right) + { \bf S } { \bf z } ( t + q T _ { \mathrm { s } } + T _ { \mathrm { c p } } ) \mathrm { r e c t } \left( \frac { t } { T } \right) } . \qquad ( 3 1 \mathrm { ~ a d } ) }  \end{array}
$$

Within one symbol duration, the Doppler term $e ^ { j 2 \pi f _ { D , l } ( t + q T _ { \mathrm { s } } + T _ { \mathrm { c p } } ) }$ can be approximated as a constant $e ^ { j 2 \pi f _ { D , l } \left( q T _ { \mathrm { s } } + T _ { \mathrm { c p } } \right) }$ . The waveform (31) is sampled at an interval of $T / N _ { \mathrm { s c } } ,$ and then $N _ { \mathrm { s c } } { \mathrm { - p o i n t } }$ fast Fourier transform (FFT) is performed on each symbol to obtain a spatialfrequency-time domain tensor $\mathcal { V } \bar { \in } \mathbb { C } ^ { N _ { \mathrm { R F } } \times N _ { \mathrm { s c } } \times M _ { \mathrm { s y n } } }$ m

$$
\mathcal { V } _ { : , p , q } = \mathbf { S } \sum _ { l = 0 } ^ { L } \bar { \alpha } _ { l } \mathbf { r } ( \theta _ { l } ) d _ { p q } e ^ { - j 2 \pi p \Delta f \tau _ { l } } e ^ { j 2 \pi f _ { D , l } q T _ { \mathrm { s } } } + \mathbf { S } \mathbf { Z } _ { p , q } ,\tag{32}
$$

where $\begin{array} { r l r } { \bar { \alpha } _ { l } } & { { } \quad } & { = \quad \quad \alpha _ { l } e ^ { j 2 \pi f _ { D , l } T _ { \mathrm { c p } } } , \quad \quad { \bf Z } _ { p , q } } \end{array}$ $\begin{array} { r } { \frac { 1 } { N _ { \mathrm { s c } } } \mathrm { F F T } \left\{ \mathbf { z } ( i T / N _ { \mathrm { s c } } + q T _ { \mathrm { s } } + T _ { \mathrm { c p } } ) \right\} _ { i } , 1 \leq i \leq \hat { N _ { \mathrm { s c } } } . } \end{array}$ . Suppose $z _ { m , n } ( t )$ follows i.i.d. CSCG distribution with variance $\sigma ^ { 2 }$ at each time sample, i.e., $z _ { m , n } ( t ) \sim \mathcal { C N } ( 0 , \sigma ^ { 2 } )$ . Then we can get $\begin{array} { r } { \mathbf { z } ( t ) \sim \mathcal { C N } ( 0 , M \sigma ^ { 2 } \mathbf { I } _ { N } ) , \mathbf { Z } _ { p , q } \sim \mathcal { C N } \left( 0 , \frac { M } { N _ { \mathrm { s c } } } \sigma ^ { 2 } \mathbf { I } _ { N } \right) } \end{array}$

1) Communication Model: From the communication perspective, the received signal (32) at the Rx can be written as

$$
\begin{array} { r } { \mathbf { y } _ { p q } ^ { \mathrm { c } } = \mathbf { h } _ { p q } ^ { \mathrm { c } } d _ { p q } + \mathbf { n } _ { p q } ^ { \mathrm { c } } , } \end{array}\tag{33}
$$

where $\begin{array} { r l r } { { \bf h } _ { p q } ^ { \mathrm { c } } } & { { } = } & { { \bf S } \sum _ { l = 0 } ^ { L } \bar { \alpha } _ { l } { \bf r } ( \theta _ { l } ) e ^ { - j 2 \pi p \Delta f \tau _ { l } } e ^ { j 2 \pi f _ { D , l } q T _ { \mathrm { s } } } } \end{array}$ is the equivalent communication channel for the pth subcarrier of OFDM symbol $q ,$ and ${ \bf n } _ { p q } ^ { \mathrm { c } } ~ = ~ { \bf S } { \bf Z } _ { p , q }$ denotes the AWGN vector with each entry having zero mean and $\begin{array} { r } { \frac { M } { N _ { \mathrm { s c } } } \sigma ^ { 2 } } \end{array}$ variance. Accordingly, the expected uplink communication rate is given by

$$
\mathcal { R } = \frac { 1 } { B T _ { \mathrm { s } } } \mathbb { E } \left[ \frac { 1 } { M _ { \mathrm { s y m } } } \sum _ { q = 0 } ^ { M _ { \mathrm { s y m } } - 1 } \sum _ { p = 0 } ^ { N _ { \mathrm { s c } } - 1 } \log _ { 2 } \left( 1 + \frac { \lVert \mathbf { h } _ { p q } ^ { \mathrm { c } } \rVert ^ { 2 } P _ { t } } { \frac { M } { N _ { \mathrm { s c } } } \sigma ^ { 2 } } \right) \right] ,\tag{34}
$$

where $\mathbb { E } [ \cdot ]$ means takes expectation w.r.t $\alpha _ { l } , \theta _ { l } , \tau _ { l } , f _ { D , l } .$

2) Sensing Model: With the communication symbols $d _ { p q }$ demodulated, we can perform data removal on (32)

$$
\bar { \mathcal { V } } _ { : , p , q } = \frac { \mathcal { V } _ { : , p , q } } { d _ { p q } } = \mathbf { S } \sum _ { l = 0 } ^ { L } \bar { \alpha } _ { l } \mathbf { r } ( \theta _ { l } ) e ^ { - j 2 \pi p \Delta f \tau _ { l } } e ^ { j 2 \pi f _ { D , l } q T _ { \mathrm { s } } } + \frac { \mathbf { S } \mathbf { Z } _ { p , q } } { d _ { p q } }\tag{35}
$$

where $\mathbf { h } _ { \mathbf { s } } ( \theta _ { l } ) \ = \ \mathbf { S } \mathbf { r } ( \theta _ { l } )$ is the equivalent steering vector, $\omega _ { u } ^ { l } ~ = ~ - 2 \pi \Delta f \tau _ { l }$ and $\omega _ { v } ^ { l } \ = \ 2 \pi f _ { D , l } T _ { \mathrm { s } }$ are phase coefficient of subcarrier and symbol, respectively, and $\begin{array} { r l r } {  { \mathbf { n } } _ { s } } & { { } = } & { \frac {  { \mathbf { S } }  { \mathbf { Z } } _ { p , q } } { d _ { n \sigma } } } \end{array}$ denotes the noise vector. Based on (35), we try to obtain $\theta _ { l } ^ { ' \dagger } , \tau _ { l }$ and $f _ { D , l }$

## B. Sensing Algorithm Design

1) AoA Estimation: The spatial domain of (35) only contains angular information of targets $\theta _ { l } .$ , so the subcarrier and symbol domain can be treated as snapshots. To this end, the $N _ { \mathrm { R F } } \times N _ { \mathrm { s c } } \times M _ { \mathrm { s y m } }$ dimensional signal tensor $\bar { \mathcal { D } }$ in (35) can be reorganized as a $N _ { \mathrm { R F } } \times N _ { \mathrm { s c } } M _ { \mathrm { s y m } }$ dimensional matrix $\mathbf { Y } _ { \theta }$ as below

$$
\mathbf { Y } _ { \theta } ( : , n _ { p , q } ) = \bar { \mathcal { N } } _ { : , p , q } ,\tag{36}
$$

where $n _ { p , q } ~ = ~ p + q M _ { \mathrm { s y m } }$ . Thus, $\mathbf { X } _ { \theta }$ can be equivalently expressed in matrix form as

$$
\mathbf { Y } _ { \theta } = \mathbf { H } _ { \theta } \mathbf { X } _ { \theta } ,\tag{37}
$$

where $\mathbf { H } _ { \theta } \in \mathbb { C } ^ { N _ { \mathrm { R F } } \times ( L + 1 ) }$ is the array manifold matrix, and $\mathbf { X } _ { \theta } \in \mathbb { C } ^ { ( L + 1 ) \times N _ { \mathrm { s c } } M _ { \mathrm { s y m } } }$ , given by

$$
{ \bf H } _ { \theta } = [ { \bf h } _ { \mathrm { s } } ( \theta _ { 0 } ) , { \bf h } _ { \mathrm { s } } ( \theta _ { 1 } ) , \dots , { \bf h } _ { \mathrm { s } } ( \theta _ { L } ) ] .\tag{38}
$$

$$
{ \bf X } _ { \theta } ( l , n _ { p , q } ) = \bar { \alpha } _ { l } e ^ { j \omega _ { u } ^ { l } p } e ^ { j \omega _ { v } ^ { l } q } .\tag{39}
$$

2) Delay and Doppler Estimation: The AoA estimation problem is to estimate the angles $\mathbb { S } _ { \theta } = \{ \theta _ { 0 } , \theta _ { 1 } , \dots , \theta _ { L } \}$ of the $L + 1$ localization/sensing targets embedded in the array manifold matrix $\mathbf { H } _ { \theta }$ . Note that different from the conventional arrays where the array manifold matrix are usually rotational invariance, the $\mathbf { H } _ { \theta }$ for RAA no longer has such property. Therefore, we adopt the MUSIC algorithm which leverages the orthogonality between the noise subspace and the signal subspace to estimate target parameters. The required subspaces are derived through eigenvalue decomposition (EVD) of the covariance matrix for the observed data $\mathbf { Y } _ { \theta }$ in (37), which can be expressed as

$$
\begin{array} { l } { \displaystyle \mathbf { C } _ { \mathbf { Y } } = \frac { 1 } { N _ { \mathrm { s c } } M _ { \mathrm { s y m } } } \mathbf { Y } _ { \theta } \mathbf { Y } _ { \theta } ^ { \mathrm { H } } } \\ { = \mathbf { E } _ { \mathrm { s } } \boldsymbol { \Sigma } _ { \mathrm { s } } \mathbf { E } _ { \mathrm { s } } ^ { \mathrm { H } } + \mathbf { E } _ { \mathrm { n } } \boldsymbol { \Sigma } _ { \mathrm { n } } \mathbf { E } _ { \mathrm { n } } ^ { \mathrm { H } } , } \end{array}\tag{40}
$$

where $\pmb { \Sigma } _ { \mathrm { s } } \in \mathbb { C } ^ { ( L + 1 ) \times ( L + 1 ) } , \pmb { \Sigma } _ { \mathrm { n } } \in \mathbb { C } ^ { ( N _ { \mathrm { R F } } - L - 1 ) \times ( N _ { \mathrm { R F } } - L - 1 ) }$ are diagonal matrices composed by the $L + 1$ largest eigenvalues and the remaining $N _ { \mathrm { R F } } - L - 1$ eigenvalues, respectively. ${ \bf E } _ { \mathrm { s } }$ and $\mathbf { E } _ { \mathrm { n } }$ denote the signal and noise subspaces, respectively. The MUSIC spatial spectrum is subsequently formulated as

$$
P _ { \mathrm { M U S I C } } ( \boldsymbol { \theta } ) = \frac { 1 } { \mathbf { h } _ { \mathrm { s } } ^ { \mathrm { H } } ( \boldsymbol { \theta } ) \mathbf { E } _ { \mathrm { n } } \mathbf { E } _ { \mathrm { n } } ^ { \mathrm { H } } \mathbf { h } _ { \mathrm { s } } ( \boldsymbol { \theta } ) } .\tag{41}
$$

As such, the peaks of the MUSIC spectrum correspond to the estimation of AoAs of sensing targets. The estimation result is denoted by $\hat { \mathbb { S } } _ { \theta } = \{ \hat { \theta } _ { 0 } , \hat { \theta } _ { 1 } , \dots , \hat { \theta } _ { L _ { k } } \}$ , where $L _ { k } \leq L + 1$ due to the limitation of resolution or noise.

Owing to the super-resolution capability of the MUSIC algorithm, closely spaced AoAs can be effectively discriminated, which enables sequential parameter estimation through spatial beamforming. Furthermore, the signal tensor $\bar { \mathcal { V } } _ { : , p , q }$ in (35) exhibits distinctive structural properties across its subcarrier and symbol dimensions: The signal phase increases linearly w.r.t. subcarrier index $p$ and symbol index $q .$ This structural regularity constitutes critical prior knowledge that can be exploited to simplify the estimation problem and reduce computational complexity. For range and Doppler estimation, we therefore implement a two-stage approach:

• ZF spatial beamforming to isolate target-specific signals.

• Periodogram algorithm leveraging the spectral characteristics in subcarrier and symbol domains.

![](images/1284d17a96e452ab0b6288f9be026af58b52128d669cf0787b48d1cd81a5abf4.jpg)  
(a)

![](images/1c18ea95804cd7d8090b915a39372e74169413362df8dd6c6e88f914ace148b7.jpg)  
(b)  
Fig. 5. MUSIC specturm of (a) RAA (b) ULA with moderate AoAs.

This methodology takes advantage of the OFDM waveform structure while maintaining estimation accuracy and computational efficiency through decoupled processing of spatial and spectral parameters.

Specially, the $\mathrm { Z F }$ beamforming vectors are given by

$$
\mathbf { h } _ { \mathrm { Z F } } ( \hat { \theta _ { l } } ) = \frac { \hat { \mathbf { H } } _ { l } \mathbf { h } _ { \mathrm { s } } ( \hat { \theta } _ { l } ) } { \left\| \hat { \mathbf { H } } _ { l } \mathbf { h } _ { \mathrm { s } } ( \hat { \theta } _ { l } ) \right\| _ { 2 } } ,\tag{42}
$$

where

$$
\hat { \mathbf { H } } _ { l } = \mathbf { I } _ { M } - \mathbf { H } _ { l } ( \mathbf { H } _ { l } ^ { \mathrm { H } } \mathbf { H } _ { l } ) ^ { - 1 } \mathbf { H } _ { l } ^ { \mathrm { H } } .
$$

$$
\mathbf { H } _ { l } = \left[ \mathbf { h } _ { \mathrm { s } } ( \hat { \theta } _ { 0 } ) \dots \mathbf { h } _ { \mathrm { s } } ( \hat { \theta } _ { l - 1 } ) \ \mathbf { h } _ { \mathrm { s } } ( \hat { \theta } _ { l + 1 } ) \dots \mathbf { h } _ { \mathrm { s } } ( \hat { \theta } _ { L - 1 } ) \right] .\tag{43}
$$

(44)

Then for target k, the beamformed signal matrix ${ \textbf { Y } } ^ { k } \in$ $\mathbb { C } ^ { N _ { \mathrm { { s c } } } \times M _ { \mathrm { { s y m } } } }$ can be obtained as

$$
\begin{array} { r l } & { \mathbf { Y } _ { p , q } ^ { k } = \mathbf { h } _ { \mathrm { Z F } } ^ { \mathrm { H } } ( \hat { \theta } _ { k } ) \bar { \mathcal { V } } _ { : , p , q } } \\ & { \quad \quad \quad = \mathbf { h } _ { \mathrm { Z F } } ^ { \mathrm { H } } ( \hat { \theta } _ { k } ) \displaystyle \sum _ { l = 0 } ^ { L } \bar { \alpha } _ { l } \mathbf { h } _ { \mathrm { s } } ( \theta _ { l } ) e ^ { j \omega _ { u } ^ { k } p } e ^ { j \omega _ { v } ^ { l } q } + \mathbf { h } _ { \mathrm { Z F } } ^ { \mathrm { H } } ( \hat { \theta } _ { k } ) \mathbf { n } _ { s } } \\ & { \quad \quad \stackrel { ( a ) } { \approx } \bar { \alpha } _ { k } \mathbf { h } _ { \mathrm { Z F } } ^ { \mathrm { H } } ( \hat { \theta } _ { k } ) \mathbf { h } _ { \mathrm { s } } ( \theta _ { k } ) e ^ { j \omega _ { u } ^ { k } p } e ^ { j \omega _ { v } ^ { k } q } + \mathbf { h } _ { \mathrm { Z F } } ^ { \mathrm { H } } ( \hat { \theta } _ { k } ) \mathbf { n } _ { s } , } \end{array}\tag{45}
$$

![](images/61155eae0ec0b329baea75e7dc30d5dbe48a8c6aac46febcaf03d50d6d2a7ece.jpg)  
(a)

![](images/b8e7e6686e3b357741483a075ec97208489c31440d95fec84683a43fa978d758.jpg)  
(b)  
Fig. 6. MUSIC specturm of (a) RAA (b) ULA with large AoAs.

where (a) holds because $\mathbf { h } _ { \mathrm { Z F } } ^ { \mathrm { H } } ( \hat { \theta } _ { k } ) \mathbf { h } _ { \mathrm { s } } ( \theta _ { l } ) \approx 0 , k \neq l .$

By substituting $\omega _ { u } ^ { l } ~ = ~ - 2 \pi \Delta f \tau _ { l }$ and $\omega _ { v } ^ { l } \ = \ 2 \pi f _ { D , l } T _ { \mathrm { s } }$ into (45), we consider $( N _ { \mathrm { s c } } , M _ { \mathrm { s y m } } )$ -point 2D-Periodogram algorithm on $\mathbf { Y } _ { p , q } ^ { l }$

$$
\begin{array} { r l r } & { \tilde { \mathbf { Y } } _ { \mathbf { Y } _ { \mathbf { Y } _ { \mathbf { Y } } } ^ { \prime } } ^ { \prime \prime } = \mathrm { F r } [ ( \mathbf { I } \mathrm { F r } ] \mathrm { Y } _ { \mathbf { X } } ^ { \prime } \mathrm { Y } _ { \mathbf { y } _ { \mathbf { Y } } } ^ { \prime \prime } ) \mathbf { I } _ { \mathbf { Y } _ { \mathbf { Y } _ { \mathbf { Y } } } ^ { \prime } } ^ { \prime } } \\ & { = \alpha _ { \mathrm { h } } \frac { 1 } { N \sigma _ { \mathbf { Y } } } \langle \theta \rangle _ { \mathbf { J } _ { \mathbf { Y } _ { \mathbf { Y } } } } [ \delta _ { \mathbf { J } _ { \mathbf { Y } _ { \mathbf { Y } } } } \delta _ { \mathbf { Y } } ^ { \prime \prime \prime } \mathbf { I } _ { \mathbf { Y } _ { \mathbf { Y } } } - \delta _ { \mathbf { Y } } ( \mathbf { Z } _ { \mathbf { Y } _ { \mathbf { Y } } } - \Delta f _ { \mathbf { Y } _ { \mathbf { Y } } } ) ] } \\ & { \times \exp ^ { i ( \mathbf { Z } _ { \mathbf { Y } _ { \mathbf { Y } } } - \mathbf { I } ) } ( \sigma _ { \mathbf { Z } _ { \mathbf { Y } _ { \mathbf { Y } } } } - \sigma _ { \mathbf { Y } _ { \mathbf { Y } } , \mathbf { Z } _ { \mathbf { Y } _ { \mathbf { Y } } } } ) \frac { \sin ( \mathbf { I } \mathrm { T x } _ { \mathbf { X } } ) ( \mathbf { I } _ { \mathbf { Y } _ { \mathbf { X } } } ^ { \prime } - \Delta f _ { \mathbf { Y } } ) ) } { \sin ( \mathbf { \sigma } ) } } \\ & { \times \frac { \sin ( \pi \mathrm { M o } _ { \mathbf { Z } } ( \frac { 1 } { N \sigma _ { \mathbf { Y } } } - \mathcal { T } _ { \mathbf { Y } _ { \mathbf { Z } } \mathbf { Z } _ { \mathbf { Y } _ { \mathbf { Y } } } } ) ) } { \sin ( \pi ) } }  \end{array}
$$

TABLE II  
SYSTEM SETTINGS
<table><tr><td>Parameter</td><td>Symbol</td><td>Value</td></tr><tr><td>Carrier frequency</td><td> $f _ { c }$ </td><td>39GHz</td></tr><tr><td>System bandwidth</td><td> $B$ </td><td>61.44MHz</td></tr><tr><td>Number of subcarriers</td><td> $N _ { \mathrm { s c } }$ </td><td>512</td></tr><tr><td>Number of OFDM symbols</td><td> $M _ { \mathrm { s y m } }$ </td><td>2048</td></tr><tr><td>Subcarrier spacing</td><td> $\Delta f$ </td><td>120kHz</td></tr><tr><td>OFDM symbol duration</td><td> $\check { T }$ </td><td> $8 . 3 3 \mu \mathrm { s }$ </td></tr><tr><td>CP duration</td><td> $T _ { \mathrm { c p } }$ </td><td> $0 . 6 7 \mu \mathrm { s }$ </td></tr><tr><td>Total symbol duration</td><td> $T _ { \mathrm { s } }$ </td><td> $9 \mu \mathrm { s }$ </td></tr><tr><td>Number of antenna elements in sULA/ULA</td><td> $M$ </td><td>128</td></tr><tr><td>Number of sULAs</td><td> $N$ </td><td>201</td></tr><tr><td>Number of RF-chains</td><td> $N _ { \mathrm { R F } }$ </td><td>8</td></tr><tr><td>Number of DFT codewords</td><td>N′</td><td>128</td></tr><tr><td>Ratio of transmit power and noise</td><td> $P _ { t } / \sigma ^ { 2 }$ </td><td>20dB</td></tr></table>

where $\alpha _ { l p ^ { \prime } q ^ { \prime } }$ denotes the equivalent path coefficient, and $\mathrm { F F T } \{ \cdot \} _ { p } , \mathrm { \bar { I F F T } } \{ \cdot \} _ { q }$ means perform FFT and inverse FFT (IFFT) algorithm on a designated dimension, respectively. Therefore, we have obtained the spectrum of delay and Doppler of target l. By searching the peaks of 2-D matrix $| \bar { \mathbf { Y } } _ { p ^ { \prime } , q ^ { \prime } } ^ { \bar { l } } | ^ { 2 }$ , those indexes $\hat { p } _ { l } ^ { \prime } , \hat { q } _ { l } ^ { \prime }$ of peak values can be transformed into our desired parameters

$$
\hat { \tau } _ { l } = \frac { \hat { p } _ { l } ^ { \prime } } { N _ { \mathrm { s c } } \Delta f } , \quad \hat { f } _ { D , l } = \frac { \hat { q } _ { l } ^ { \prime } } { M _ { \mathrm { s y m } } T _ { \mathrm { s } } } ,\tag{47}
$$

where $\hat { \tau } _ { l }$ and $\hat { f } _ { D , l }$ are the estimated delay and Doppler of target $l ,$ respectively. For target l, all the parameters $\{ \theta _ { l } , \tau _ { l } , f _ { D , l } \}$ can thus be obtained. Note that the resolution limit of Periodogram algorithm depends on FFT/IFFT points, while the computational complexity also increases with it. Therefore, a proper value for the size of the FFT/IFFT should be selected.

Algorithm 1 Proposed Algorithm for OFDM-ISAC With RAA   
Input: Signal tensor $\bar { \mathcal { D } }$ in (35)   
Output: $\theta _ { l } , \tau _ { l } , f _ { D , l } , \forall l$   
1: Reorganize $\bar { \mathcal { V } } _ { : , p , q }$ as $\mathbf { Y } _ { \theta }$ in (36)   
2: Calculate the covariance matrix $\mathbf { C _ { Y } }$ of $\mathbf { Y } _ { \theta }$ with (40)   
3: Perform EVD of the covariance of $\mathbf { C _ { Y } }$ , and obtain the   
noise subspace $\mathbf { E } _ { \mathrm { n } }$   
4: for $\theta \in [ - \theta _ { \mathrm { m a x } } , \theta _ { \mathrm { m a x } } ]$ do   
5: Calculate the equivalent steering vector ${ \bf h } _ { \mathrm { s } } ( \theta )$ in (35)   
6: Calculate the searching spectrum $P _ { \mathrm { M U S I C } } ( \boldsymbol { \theta } )$ in (41)   
7: end for   
8: Find the $L _ { k } \leq L + 1$ highest peaks of $P _ { \mathrm { M U S I C } } ( \boldsymbol { \theta } )$ to obtain   
the estimated AoAs $\hat { \mathbb S } _ { \boldsymbol \theta } = \{ \hat { \theta } _ { 0 } , \hat { \theta } _ { 1 } , \dots , \hat { \theta } _ { L _ { k } } \}$   
9: for $l \in \{ 0 , 1 , \ldots , L _ { k } \}$ do   
10: Calculate ZF beamforming vector $\mathbf { h } _ { \mathrm { Z F } } ( \hat { \theta _ { l } } )$ in (42)   
11: Perform spatial filtering on $\bar { \mathcal { V } } _ { : , p , q }$ in (45) to obtain $\mathbf { Y } _ { p , q } ^ { l }$   
12: Perform Periodogram algorithm on $\mathbf { Y } _ { p , q } ^ { l }$ in (46) to   
obtain $\bar { \mathbf { Y } } _ { p ^ { \prime } , q ^ { \prime } } ^ { l }$   
13: Search the peak of $\bar { \mathbf { Y } } _ { p ^ { \prime } , q ^ { \prime } } ^ { l }$ and transform them into   
desired parameters $\hat { \tau } _ { l } , \hat { f } _ { D , l }$ in (47)   
14: end for   
15: Match the parameters and obtain $\{ \theta _ { l } , \tau _ { l } , f _ { D , l } \}$   
16: return $\theta _ { l } , \tau _ { l } , f _ { D , l } , l = \left\{ 0 , 1 , \ldots , L _ { k } \right\}$

The pseudo-code of the proposed sensing algorithm is summarized in Algorithm 1.

![](images/285099ecb207c5eef35eeaa74a11c678c8e6a6d2c4ea61bad34fb3768d18adc3.jpg)  
(a)

![](images/f134990195d3920e7a4f490e268a7d110cad8a4bdff565de2df2b234506215c8.jpg)

![](images/d671bad73bf8dc06c17450db50cd9db028afcdc7d28d799018f239b113436cb4.jpg)

![](images/3e785ae081234e0dde75cbb28d48f004d358bc26a5ebba74f01980195d69c634.jpg)  
(d)

(b)  
![](images/840c972d419903c885e41439b4bd85b408e4fa08fca64b959ceadbfa4fd9af8a.jpg)  
(e)

(c)  
![](images/6c92bc9e7c6da89ef065981d275a574a6154f1a5474e202475cf5624a80d1ec9.jpg)  
(f)  
Fig. 7. An example of Delay-Doppler maps of targets (a) without ZF beamforming, (b)-(f) with ZF beamforming.

## V. SIMULATION RESULTS

In this section, we provide numerical results to verify the performance of RAA in ISAC system. For RAA, we set the maximum orientation of sULAs and elements in each sULA as $\eta _ { \mathrm { m a x } } = \pi / 2 , M = 1 2 8$ at Rx, respectively. Therefore, the total number of sULAs needed is $\begin{array} { r } { N = 2 \left| \frac { \eta _ { \mathrm { m a x } } } { \arcsin ( 2 / M ) } + 1 \right| = 2 0 1 } \end{array}$ The orientation of each sULA is $\eta _ { n } \stackrel {  } { = } n \arcsin ( 2 / M ) , n \in \mathcal { N } ,$ and the distance $D$ is $\lambda / 4 ( \sin ( 0 . 5 \arcsin ( 2 / M ) ) )$ . For HBF, the number of DFT codewords is $N ^ { \prime } = \overset { 2 } { 2 } / \overset { \cdot } { M } = 1 2 8$ , and the nth codeword’s angle is ϕ<sub>n</sub> = arcsin $\begin{array} { r } { \left( \frac { n ^ { - } 6 5 } { 6 4 } \right) , 1 \le n \le N ^ { \prime } } \end{array}$ The number of RF chains is set to $N _ { \mathrm { R F } } = 8 .$ The carrier frequency is set as $f _ { c } = 3 9 \mathrm { G H z }$ , the subcarrier spacing as $\Delta f = 1 2 0 \mathrm { { k H z } }$ , and the number of subcarriers, symbols in one CPI as $N _ { \mathrm { s c } } = 5 1 2 , M _ { \mathrm { s y m } } = 2 0 4 8$ , respectively. The total number of required time slots for the RSN can be obtained as $\biggl \lceil \frac { N } { N _ { \mathrm { R F } } } \biggr \rceil = 2 6 \ll M _ { \mathrm { s y m } }$ , which justifies the effectiveness of ray selection strategy. The system bandwidth can be obtained as $B = N _ { \mathrm { s c } } \Delta f = 6 1 . 4 4 \mathrm { M H z }$ . In addition, the radiation patterns of antenna elements follow the 3GPP antenna model, which is expressed in dB as [47]

$$
G _ { \mathrm { d B } } ( \theta ) = G _ { 0 } ^ { \mathrm { d B } } - \operatorname* { m i n } \{ 1 2 ( \theta / \theta _ { 3 \mathrm { d B } } ) ^ { 2 } , A _ { \operatorname* { m a x } } ^ { \mathrm { d B } } \} ,\tag{48}
$$

where $G _ { 0 } ^ { \mathrm { d B } }$ is the peak antenna gain in dB, $A _ { \mathrm { m a x } } ^ { \mathrm { d B } } = 3 0 \mathrm { d B }$ denotes the front-to-back attenuation and $\theta _ { \mathrm { 3 d B } }$ accounts for the 3dB beamwidth. For ULA, $\theta _ { \mathrm { 3 d B } } ^ { \mathrm { U L A } }$ is set to π to cover the entire direction, while for $\mathrm { R A A } , \theta _ { \mathrm { 3 d B } } ^ { \mathrm { \tiny { K A } } }$ is set to 0.3π, as each sULA is only responsible for a narrower AoA range. Besides, $G _ { 0 } ^ { \mathrm { d B } }$ in ULA and RAA are set to 0dB and 5.1335dB to guarantee the same total power gain for all directions. The parameter settings are listed in Tab. II.

The UAV swarm comprises five low-altitude UAVs arranged with equal 0.5-degree angular spacing in their AoAs. By deliberately adjusting the geometric centroid of the swarm, distinct mean AoA values can be achieved for different sensing scenarios. The delay and Doppler frequency parameters of the targets are set following the Gaussian distribution, where the mean of delay is in accordance with the adjusted swarm centroid, the mean of Doppler is 300Hz, and their variances are $4 \times 1 0 ^ { - 1 6 } \mathrm { s ^ { 2 } }$ and $6 4 0 0 \mathrm { H z } ^ { 2 }$ , respectively. Both RAA and ULA architectures are considered to illustrate the sensing parameter estimation performance, which is evaluated in terms of the RMSE of the estimated angle.

Note that due to the close proximity of UAV swarms, adjacent targets may not be perfectly discriminated, so another criterion, termed as average missing shots, is incorporated to evaluate the performance, which is defined as

$$
\varepsilon = \frac { 1 } { Q } \sum _ { i = 1 } ^ { Q } \left( \mathrm { c a r d } \left( \mathbb { S } _ { \theta } ^ { i } \right) - \mathrm { c a r d } \left( \hat { \mathbb { S } } _ { \theta } ^ { i } \right) \right) ,\tag{49}
$$

where $Q$ denotes the total number of testing rounds, $\mathbb { S } _ { \theta } ^ { i }$ and $\hat { \mathbb { S } } _ { \theta } ^ { i }$ denote the real and estimation angle set of ith test round, respectively. We assume that card $\left( \mathbb { S } _ { \theta } ^ { i } \right) \geq \mathrm { c a r d } \left( \hat { \mathbb { S } } _ { \theta } ^ { i } \right)$ , which holds when the noise is rather small.

Fig. 5 and Fig. 6 demonstrate the MUSIC specturm of AoA estimation with RAA and ULA under large and moderate AoAs. It can be seen that when targets are around the array boresight, i.e., with relatively small AoAs, both RAA and ULA can distinguish them very well. However, if the AoAs are large, ULA fails to discriminate the different UAVs in the swarm, while RAA still have an excellent performance. This is consistent with the the resolution comparison between ULA and RAA in Fig. 4.

![](images/950440275866bd7a6d92dc8bdf1332a9d2aee03e3827345771d4a3f5b0bbcb3e.jpg)

Fig. 8. RMSE of AoA estimation.  
![](images/bf05a50805d7ff251ee1b13387bf5790ade62a5fcf72369f1dcb72b9ba5603b5.jpg)  
Fig. 9. Average missing shots of AoA estimation.

Fig. 7a demonstrates the delay and Doppler information about all the five targets. It can be inferred that if spatial ZF beamforming is not performed, some of the targets may be buried in the noise, or overlapping with each other, making them difficult to distinguish. With ZF beamforming, the delay and Doppler information of each target are shown in Fig. 7b-7f, respectively. Owing to the super resolution ability of MUSIC algorithm, all targets can be filtered out by ZF beamforming and thus achieves excellent estimation accuracy in delay and Doppler by oversampling and zero padding in Periodogram algorithm.

Fig. 8 shows the comparison of AoA estimation RMSE between RAA and ULA w.r.t. different AoAs centroid. It can be seen that as the UAV swarm moving closer with increasing AoAs, the RMSE of ULA increases dramatically while that of RAA remains almost the same. This can be explained that as the resolution of ULA degrades, adjacent AoAs cannot be discriminated and they form fake peaks, resulting in error in AoA estimation. Besides, the limited resolution also brings about missing shots, which is obvious when AoAs are large, as shown in Fig. 9.

![](images/82412a6131faf58fd8d7d66bebf1e616f7e75213a98d399763d473590d46549b.jpg)  
Fig. 10. RMSE of delay estimation.

![](images/649b4b6e7c247027d16ad1aa520d214b78bec17ea373b58a12554d7be888362a.jpg)  
Fig. 11. RMSE of doppler estimation.

The delay and Doppler estimation performance of RAA and ULA are illustrated in Fig. 10 and Fig. 11, respectively. In the simulation, both the frequency and symbol domains are oversampled by a factor of 4. Since RAA and ULA utilize the same bandwidth and OFDM symbol duration, their delay and Doppler resolutions are identical and the RMSE performance remain invariant with respect to the swarm center, as demonstrated in the figures.

Fig. 12 plots the achievable communication rate of RAA and ULA. The isotropic antenna element gain in any direction is set as $G _ { \mathrm { d B } } ^ { \mathrm { i s o } } ~ = ~ - 2 . 8 1 6 \mathrm { d B }$ to guarantee the same total power gain for all directions. It can be observed that RAA outperforms ULA in terms of communication performance as well, especially when directional antenna elements are exploited. This can be attributed to the higher directional antenna gain since each sULA is responsible for a narrower range of incoming signals. These results demonstrate that RAA can achieve better communication and sensing performance compared to ULA.

![](images/c4fb4506748697391bb3d58eed12cce3483be6d74c5701e126be03127d62c840.jpg)  
Fig. 12. Communication rate for RAA and ULA.

## VI. CONCLUSION

In this paper, we proposed and investigated the RAA-based ISAC systems for low-altitude UAV swarm. By analyzing the beam pattern of RAA, we rigorously showed that unlike conventional ULAs, RAA can achieve uniform angular resolution across all signal directions. We also demonstrated that RAA can achieve higher overall beamforming gain than the conventional ULA since antenna elements with higher directivity can be used. Besides, we proposed efficient sensing algorithms for RAA based UAV swarm ISAC with OFDM. MUSIC-based AoA estimation, ZF spatial filtering, and 2-D Periodogram enabled robust multi-target AoA-delay-Doppler detection under OFDM signaling. Numerical results demonstrated the effectiveness of the proposed RAA based ISAC system, which outperforms conventional ULA in both target estimation and communication performance.

A practical issue for the proposed RAA is the potential for blockage between adjacent sULAs in practical deployments. This occlusion can lead to power absorption and mutual interference, which may affect the overall system performance. To address this challenge in future work, we are investigating new array arrangements, such as introducing lateral displacements or adopting polygonal and conformal array, for which the key results developed in this paper are still applicable. Moreover, extending the current model into a comprehensive threedimensional framework is envisioned to effectively mitigate blockage issues while enabling seamless full-space coverage.

## APPENDIX

## PROOF OF THEOREM 3

Based on Theorem 1 and 2, in $\gamma _ { \mathrm { U L A } } ( \theta ^ { \prime } )$ we denote sin θ<sup>0</sup> by x, and take derivative of $\gamma _ { \mathrm { U L A } } ( \arcsin ( x ) )$ w.r.t. x, we will get:

$$
\frac { \mathrm { d } \gamma _ { \mathrm { U L A } } } { \mathrm { d } x } = \frac { 1 } { 2 } \frac { \mathrm { d } \left[ \arcsin \left( x + \frac { 2 } { M } \right) - \arcsin \left( x - \frac { 2 } { M } \right) \right] } { \mathrm { d } x }
$$

$$
{ \begin{array} { r l } & { \quad = { \frac { 1 } { 2 } } \left( { \frac { 1 } { \sqrt { 1 - \left( x + { \frac { 2 } { M } } \right) ^ { 2 } } } } - { \frac { 1 } { \sqrt { 1 - \left( x - { \frac { 2 } { M } } \right) ^ { 2 } } } } \right) } \\ & { \quad = { \frac { 1 } { 2 } } { \frac { { \sqrt { 1 - \left( x - { \frac { 2 } { M } } \right) ^ { 2 } } } - { \sqrt { 1 - \left( x + { \frac { 2 } { M } } \right) ^ { 2 } } } } { \sqrt { 1 - \left( x + { \frac { 2 } { M } } \right) ^ { 2 } } } } } \\ & { \quad = { \frac { 1 } { 2 } } { \frac { \left( x + { \frac { 2 } { M } } \right) ^ { 2 } - \left( x - { \frac { 2 } { M } } \right) ^ { 2 } } { \Delta } } } \\ & { \quad = { \frac { 4 x } { M \Delta } } } \\ & { { \frac { { \mathrm { d } } ^ { 2 } \gamma _ { \mathrm { t r a c } } } { { \mathrm { d } } x ^ { 2 } } } = { \frac { 4 } { M \Delta } } } \end{array} }\tag{50}
$$

where $\Delta = \sqrt { 1 - u ^ { 2 } } \sqrt { 1 - v ^ { 2 } } ( \sqrt { 1 - v ^ { 2 } } + \sqrt { 1 - u ^ { 2 } } ) \geq 0 , u =$ $\begin{array} { r } { x + \frac { 2 } { M } , v \ = \ x - \frac { 2 } { M } , } \end{array}$ , and $\begin{array} { r } { \frac { \mathrm { d } ^ { 2 } \gamma _ { \mathrm { U L A } } } { \mathrm { d } x ^ { 2 } } \geq 0 . } \end{array}$ . Therefore, $x \ = \ 0$ is the global minimum of $\gamma _ { \mathrm { U L A } } ( \arcsin ( x ) )$ and $\gamma _ { \mathrm { U L A } } ( \theta ^ { \prime } ) =$ γ<sub>UL</sub> $\begin{array} { r } { \mathrm { \phantom { } _ { A } } ( \mathrm { a r c s i n } ( x ) ) \geq \gamma _ { \mathrm { U L A } } ( 0 ) = \arcsin \left( \frac { 2 } { M } \right) = \gamma _ { \mathrm { R A A } } } \end{array}$

## REFERENCES

[1] Y. Zeng, Q. Wu, and R. Zhang, “Accessing from the sky: A tutorial on UAV communications for 5G and beyond,” Proc. IEEE, vol. 107, no. 12, pp. 2327–2375, Dec. 2019.

[2] G. Geraci et al., “What will the future of UAV cellular communications be? A flight from 5G to 6G,” IEEE Commun. Surveys Tuts., vol. 24, no. 3, pp. 1304–1335, 3rd Quart., 2022.

[3] J. Zheng et al., “An efficient strategy for accurate detection and localization of UAV swarms,” IEEE Internet Things J., vol. 8, no. 20, pp. 15372–15381, Oct. 2021.

[4] J. Xu, H. Min, and Y. Zeng, “Integrated super-resolution sensing and symbiotic communication with 3D sparse MIMO for low-altitude UAV swarm,” 2025, arXiv:2504.13570.

[5] Z. Xiao et al., “A survey on millimeter-wave beamforming enabled UAV communications and networking,” IEEE Commun. Surveys Tuts., vol. 24, no. 1, pp. 557–610, 1st Quart., 2022.

[6] R. Liu, A. Liu, Z. Qu, and N. N. Xiong, “An UAV-enabled intelligent connected transportation system with 6G communications for Internet of Vehicles,” IEEE Trans. Intell. Transp. Syst., vol. 24, no. 2, pp. 2045–2059, Feb. 2023.

[7] M. Xu et al., “Quantum-secured space-air-ground integrated networks: Concept, framework, and case study,” IEEE Wireless Commun., vol. 30, no. 6, pp. 136–143, Dec. 2023.

[8] C. J. Swinney and J. C. Woods, “A review of security incidents and defence techniques relating to the malicious use of small unmanned aerial systems,” IEEE Aerosp. Electron. Syst. Mag., vol. 37, no. 5, pp. 14–28, May 2022.

[9] J. Zhao, J. Zhang, D. Li, and D. Wang, “Vision-based anti-UAV detection and tracking,” IEEE Trans. Intell. Transp. Syst., vol. 23, no. 12, pp. 25323–25334, Dec. 2022.

[10] Q. Wu et al., “A comprehensive overview on 5G-and-beyond networks with UAVs: From communications to sensing and intelligence,” IEEE J. Sel. Areas Commun., vol. 39, no. 10, pp. 2912–2945, Oct. 2021.

[11] Q. Dai et al., “A tutorial on MIMO-OFDM ISAC: From far-field to near-field,” 2025, arXiv:2504.19091.

[12] X. Wang et al., “Cooperative integrated sensing and communication in 6G: From operators perspective,” IEEE Wireless Commun., vol. 32, no. 1, pp. 52–59, Feb. 2025.

[13] Z. Xiao and Y. Zeng, “Waveform design and performance analysis for full-duplex integrated sensing and communication,” IEEE J. Sel. Areas Commun., vol. 40, no. 6, pp. 1823–1837, Jun. 2022.

[14] Y. Cui, F. Liu, X. Jing, and J. Mu, “Integrating sensing and communications for ubiquitous IoT: Applications, trends, and challenges,” IEEE Netw., vol. 35, no. 5, pp. 158–167, Sep. 2021.

[15] A. Liu et al., “A survey on fundamental limits of integrated sensing and communication,” IEEE Commun. Surveys Tuts., vol. 24, no. 2, pp. 994–1034, 2nd Quart., 2022.

[16] F. Liu et al., “Integrated sensing and communications: Toward dualfunctional wireless networks for 6G and beyond,” IEEE J. Sel. Areas Commun., vol. 40, no. 6, pp. 1728–1767, Jun. 2022.

[17] A. V. Savkin, W. Ni, and M. Eskandari, “Effective UAV navigation for cellular-assisted radio sensing, imaging, and tracking,” IEEE Trans. Veh. Technol., vol. 72, no. 10, pp. 13729–13733, Oct. 2023.

[18] Y. Liu, Q. Wang, H.-N. Dai, Y. Fu, N. Zhang, and C. C. Lee, “UAV-assisted wireless backhaul networks: Connectivity analysis of uplink transmissions,” IEEE Trans. Veh. Technol., vol. 72, no. 9, pp. 12195–12207, Sep. 2023.

[19] Y. Song et al., “An overview of cellular ISAC for low-altitude UAV: New opportunities and challenges,” 2024, arXiv:2412.19973.

[20] M. R. Castellanos, S. Yang, C.-B. Chae, and R. W. Heath Jr., “Embracing reconfigurable antennas in the tri-hybrid MIMO architecture for 6G and beyond,” 2025, arXiv:2501.16610.

[21] S. A. Busari, K. M. S. Huq, S. Mumtaz, L. Dai, and J. Rodriguez, “Millimeter-wave massive MIMO communication for future wireless systems: A survey,” IEEE Commun. Surveys Tuts., vol. 20, no. 2, pp. 836–869, 2nd Quart., 2018.

[22] T. S. Rappaport et al., “Wireless communications and applications above 100 GHz: Opportunities and challenges for 6G and beyond,” IEEE Access, vol. 7, pp. 78729–78757, 2019.

[23] H. Lu et al., “A tutorial on near-field XL-MIMO communications toward 6G,” IEEE Commun. Surveys Tuts., vol. 26, no. 4, pp. 2213–2257, 4th Quart., 2024.

[24] C. H. Doan, S. Emami, D. A. Sobel, A. M. Niknejad, and R. W. Brodersen, “Design considerations for 60 GHz CMOS radios,” IEEE Commun. Mag., vol. 42, no. 12, pp. 132–140, Dec. 2004.

[25] O. E. Ayach, S. Rajagopal, S. Abu-Surra, Z. Pi, and R. W. Heath Jr., “Spatially sparse precoding in millimeter wave MIMO systems,” IEEE Trans. Wireless Commun., vol. 13, no. 3, pp. 1499–1513, Mar. 2014.

[26] F. Sohrabi and W. Yu, “Hybrid analog and digital beamforming for mmWave OFDM large-scale antenna arrays,” IEEE J. Sel. Areas Commun., vol. 35, no. 7, pp. 1432–1443, Jul. 2017.

[27] X. Wang, Z. Fei, J. A. Zhang, and J. Xu, “Partially-connected hybrid beamforming design for integrated sensing and communication systems,” IEEE Trans. Commun., vol. 70, no. 10, pp. 6648–6660, Oct. 2022.

[28] M. Yuan et al., “Hybrid beamforming for mmWave integrated sensing and communication with multi-static cooperative localization,” IEEE Trans. Wireless Commun., early access, Jul. 14, 2025, doi: 10.1109/ TWC.2025.3586741.

[29] J. Singh, B. Naveen, S. Srivastava, A. K. Jagannatham, and L. Hanzo, “Optimal hybrid transmit beamforming for mm-wave integrated sensing and communication,” IEEE Trans. Commun., early access, Sep. 15, 2025, doi: 10.1109/TCOMM.2025.3610165.

[30] X. Gao, L. Dai, S. Han, I. Chih-Lin, and X. Wang, “Reliable beamspace channel estimation for millimeter-wave massive MIMO systems with lens antenna array,” IEEE Trans. Wireless Commun., vol. 16, no. 9, pp. 6010–6021, Sep. 2017.

[31] O. Quevedo-Teruel, M. Ebrahimpouri, and F. Ghasemifard, “Lens antennas for 5G communications systems,” IEEE Commun. Mag., vol. 56, no. 7, pp. 36–41, Jul. 2018.

[32] J.-H. Jo, J.-N. Shim, C.-B. Chae, D. K. Kim, and R. W. Heath Jr., “Sparse RF lens antenna array design for AoA estimation in wideband systems: Placement optimization and performance analysis,” IEEE Trans. Wireless Commun., vol. 23, no. 4, pp. 2869–2883, Apr. 2024.

[33] Y. Zeng and R. Zhang, “Millimeter wave MIMO with lens antenna array: A new path division multiplexing paradigm,” IEEE Trans. Commun., vol. 64, no. 4, pp. 1557–1571, Apr. 2016.

[34] K.-K. Wong, K.-F. Tong, Y. Zhang, and Z. Zhongbin, “Fluid antenna system for 6G: When Bruce Lee inspires wireless communications,” Electron. Lett., vol. 56, no. 24, pp. 1288–1290, Nov. 2020, doi: 10.1049/ el.2020.2788.

[35] L. Zhu, W. Ma, and R. Zhang, “Movable antennas for wireless communication: Opportunities and challenges,” IEEE Commun. Mag., vol. 62, no. 6, pp. 114–120, Jun. 2024.

[36] Z. Dong et al., “Movable antenna for wireless communications: Prototyping and experimental results,” IEEE Trans. Wireless Commun., early access, Nov. 3, 2025, doi: 10.1109/TWC.2025.3625559.

[37] L. Zhu et al., “A tutorial on movable antennas for wireless networks,” IEEE Commun. Surveys Tuts., early access, Feb. 27, 2025, doi: 10.1109/ COMST.2025.3546373.

[38] C. Jiang, C. Zhang, C. Huang, J. Ge, D. Niyato, and C. Yuen, “Movable antenna-assisted integrated sensing and communication systems,” IEEE Trans. Wireless Commun., vol. 24, no. 8, pp. 6397–6412, Aug. 2025.

[39] Z. Yang et al., “Pinching antennas: Principles, applications and challenges,” 2025, arXiv:2501.10753.

[40] Z. Pi and F. Khan, “An introduction to millimeter-wave mobile broadband systems,” IEEE Commun. Mag., vol. 49, no. 6, pp. 101–107, Jun. 2011.

[41] V. Venkateswaran and A.-J. Van Der Veen, “Analog beamforming in MIMO communications with phase shift networks and online channel estimation,” IEEE Trans. Signal Process., vol. 58, no. 8, pp. 4131–4143, Aug. 2010.

[42] S. Park, A. Alkhateeb, and R. W. Heath Jr., “Dynamic subarrays for hybrid precoding in wideband mmWave MIMO systems,” IEEE Trans. Wireless Commun., vol. 16, no. 5, pp. 2907–2920, May 2017.

[43] X. Gao, L. Dai, S. Han, I. Chih-Lin, and R. W. Heath Jr., “Energyefficient hybrid analog and digital precoding for mmWave MIMO systems with large antenna arrays,” IEEE J. Sel. Areas Commun., vol. 34, no. 4, pp. 998–1009, Apr. 2016.

[44] Y. Zeng, R. Zhang, and Z. N. Chen, “Electromagnetic lens-focusing antenna enabled massive MIMO: Performance improvement and cost reduction,” IEEE J. Sel. Areas Commun., vol. 32, no. 6, pp. 1194–1206, Jun. 2014.

[45] Z. Dong, Z. Zhou, and Y. Zeng, “Ray antenna array: A novel cost-effective multi-antenna architecture for enhanced wireless communication,” in Proc. IEEE 101st Veh. Technol. Conf. (VTC-Spring), Jun. 2025, pp. 1–5.

[46] Z. Dong, Z. Zhou, and Y. Zeng, “A novel cost-effective MIMO architecture with ray antenna array for enhanced wireless communication performance,” 2025, arXiv:2505.23394.

[47] 5G; Study on Channel Model for Frequencies From 0.5 to 100 GHz, document TS 38.901, 3GPP, Nov. 2020.

[48] Qorvo.(2025). Qorvo Official Website. Accessed: Jan. 7, 2025. [Online]. Available: https://www.qorvo.com/

![](images/c3aeabd32b8e52e3f9890a3fecf2889ac1c763a8e6e287e32ecc0571c9fdfe8c.jpg)  
Haoyu Jiang (Member, IEEE) received the B.S. degree in information science and engineering from Southeast University, Nanjing, China, in 2025, where he is currently pursuing the Ph.D. degree with the National Mobile Communications Research Laboratory. His research interests include multiple-input multiple-output (MIMO) and integrated sensing and communications (ISAC).

![](images/40891a3c968b4e631dcae75ff4a9f3164a53ab99a411448301950f1d3d56b47b.jpg)

Yong Zeng (Fellow, IEEE) received the Bachelor of Engineering (Hons.) and Ph.D. degrees from Nanyang Technological University, Singapore. From 2013 to 2018, he was a Research Fellow and the Senior Research Fellow with the Department of Electrical and Computer Engineering, National University of Singapore. From 2018 to 2019, he was a Lecturer with the School of Electrical and Information Engineering, The University of Sydney, Australia. He proposed the concept of channel knowledge map (CKM) and the transmission method of delay-Doppler alignment modulation (DDAM). He is currently a Chief Young Professor with the National Mobile Communications Research Laboratory, Southeast University, China, and also with Purple Mountain Laboratories, Nanjing, China. He has published more than 200 papers, which have been cited by more than 34 000 times based on Google Scholar. He was elevated to IEEE Fellow “for contributions to unmanned aerial vehicle communications and wireless power transfer.” He was listed as a Highly Cited Researcher by Clarivate Analytics for seven consecutive years from 2019 to 2025. He was a recipient of Australia Research Council (ARC) Discovery Early Career Researcher Award (DECRA), the 2020 and 2024 IEEE Marconi Prize Paper Award in Wireless Communications, the 2018 IEEE Communications Society Asia–Pacific Outstanding Young Researcher Award, the 2020 and 2017 IEEE Communications Society Heinrich Hertz Prize Paper Award, the 2021 IEEE ICC Best Paper Award, and the 2021 China Communications Best Paper Award. He is the Symposium Chair for IEEE Globecom 2021 Track on Aerial Communications, the Workshop Co-Chair for ICC 2018-2023 Workshop on UAV Communications, a Tutorial Speaker for Globecom 2018/2019, and ICC 2019 Tutorials on UAV Communications. He serves/served as an Associate Editor for IEEE TRANSACTIONS ON COMMUNICATIONS, IEEE TRANS-ACTIONS ON MOBILE COMPUTING, IEEE COMMUNICATIONS LETTERS, and IEEE OPEN JOURNAL OF VEHICULAR TECHNOLOGY, and the Leading Guest Editor for IEEE WIRELESS COMMUNICATIONS on “Integrating UAVs into 5G and Beyond” and China Communications on “Network-Connected UAV Communications.”