# Can Movable Antenna-Enabled Micro-Mobility Replace UAV-Enabled Macro-Mobility? A Physical Layer Security Perspective

Kaixuan Li, Kan Yu , Member, IEEE, Dingyou Ma , Member, IEEE, Yujia Zhao, Xiaowu Liu , Qixun Zhang , Member, IEEE, and Zhiyong Feng , Senior Member, IEEE

Abstract—This paper investigates the potential of movable antenna (MA)-enabled micro-mobility to replace UAV-enabled macro-mobility for enhancing physical layer security (PLS) in air-to-ground communications. While UAV trajectory optimization offers high flexibility and Line-of-Sight (LoS) advantages, it suffers from significant energy consumption, latency, and complex trajectory optimization. Conversely, MA technology provides fine-grained spatial reconfiguration (antenna positioning within a confined area) with ultra-low energy overhead and millisecond-scale response, enabling real-time channel manipulation and covert beam steering. To systematically compare these paradigms, we establish a dual-scale mobility framework where a UAV-mounted uniform linear array (ULA) serves as a base station transmitting confidential information to a legitimate user (Bob) in the presence of an eavesdropper (Eve). We formulate non-convex average secrecy rate (ASR) maximization problems for both schemes: 1) MA-based micro-mobility: Jointly optimizing antenna positions and beamforming (BF) vectors under positioning constraints; 2) UAV-based macro-mobility: Jointly optimizing the UAV’s trajectory and BF vectors under kinematic constraints. Extensive simulations reveal distinct operational regimes: MA micro-mobility demonstrates significant ASR advantages in low-transmit-power scenarios or under antenna constraints due to its energy-efficient spatial control. Conversely, UAV macro-mobility excels under resource-sufficient conditions (higher power, larger antenna arrays) by leveraging global mobility for optimal positioning. The findings highlight the complementary strengths of both approaches, suggesting hybrid micro-macro mobility as a promising direction for balancing security, energy efficiency, and deployment complexity in future wireless networks.

Index Terms—Movable antenna (MA), physical layer security (PLS), UAV trajectory design, average secrecy rate (ASR) maximization.

## I. INTRODUCTION

U <sup>NMANNED</sup> <sup>aerial</sup> <sup>vehicles</sup> <sup>(UAVs)</sup> <sup>have</sup> <sup>emerged</sup> <sup>as</sup>pivotal platforms for next-generation wireless communi- pivotal platforms for next-generation wireless communication, offering unique advantages such as rapid deployment, flexible altitude control, and high-probability line-of-sight (LoS) links. These attributes make UAVs ideal for applications ranging from IoT data harvesting and emergency response to coverage extension [1], [2]. However, the inherent broadcast nature of wireless channels renders UAV communications highly susceptible to eavesdropping attacks, posing significant threats to information confidentiality. Physical layer security (PLS), exploiting the intrinsic randomness of wireless channels to achieve secure transmission without relying on cryptographic keys, has thus become a critical technique for safeguarding UAV communications [3], [4]. A fundamental objective in PLS design is the maximization of the secrecy capacity (or secrecy rate), defined as the difference between the achievable rates of the legitimate link and the eavesdropper (Eve)’s link.

To enhance secrecy performance, the predominant strategy in UAV-aided secure communication involves the joint optimization of the UAV’s flight trajectory and beamforming (BF) [5], [6]. By dynamically planning the UAV’s path and adjusting BF matrix, this approach aims to favorably shape the legitimate channel while degrading the quality of eavesdropping channel. While demonstrably effective in boosting secrecy rates, this paradigm suffers from several inherent and significant limitations that hinder practical deployment:

\- Substantial energy consumption: UAV propulsion dominates onboard energy use. Security driven trajectory maneuvers rapidly drain battery reserves, critically curtailing endurance. Moreover, secrecy rate maximization fundamentally conflicts with propulsion energy minimization.

\- Latency and adaptability deficits: Computing and executing new trajectories introduces significant latency, under which evolving channel conditions render optimized trajectories obsolete, undermining sustained security;

\- Compromising flight pattern alterations: Conspicuous trajectory adjustments intended to evade Eves may inadvertently reveal the UAV’s position or intention, heightening vulnerability.

Recently, movable antenna (MA) technology has emerged as a revolutionary hardware solution offering unprecedented spatial degrees of freedom (DoF) for fine-grained channel manipulation [7], [8]. An MA enables the physical position of a transmit/receive antenna element to be dynamically adjusted within a confined region on a platform (e.g., a linear rail or 2D surface on the UAV). By precisely controlling the antenna’s location (typically on centimeter or millimeter scales), the position-dependent channel response (amplitude and phase) to both the legitimate receiver and potential Eves can be actively engineered, enabling real-time beam pattern and phase front shaping. Crucially, MA technology promises transformative advantages over trajectory manipulation:

Electromechanical efficiency: Repositioning lightweight antenna elements incurs negligible energy overhead compared to UAV propulsion, fundamentally contrasting electromechanical actuation with platform movement [8], [9];

\- Ultra-fast response: Millisecond-scale antenna relocation enables real-time channel tracking–a critical advantage for dynamic environments where second-scale trajectory adjustments exceed channel coherence times [7], [10];

Covert communication: By flexibly adjusting antenna positions at the wavelength scale, MAs achieve wavelengthlevel high-precision BF resolution, enabling fine-grained reconfiguration of multi-path phases and thereby suppressing the illegitimate user’s ability to detect the presence of communication for covert transmission [7].

The integration of MAs on UAV platforms establishes a hierarchical control paradigm: UAV macro-mobility provides coverage, while MA micro-positioning enables real-time channel state manipulation with minimal energy overhead. This dualscale approach fundamentally overcomes trajectory-based PLS limitations. Nevertheless, the capability of UAV-mounted MAs to supersede trajectory optimization for robust PLS remains experimentally unvalidated. This work pioneers the exploration of UAV-mounted MAs for PLS, introducing a paradigm shift from conventional BF optimization. As a result, “Can joint optimization of antenna positioning and transmit BF matrix achieve comparable or superior secrecy performance to conventional joint trajectory-BF design?” needs to be answered.

To systematically quantify performance boundaries between spatial control strategies, we develop a dual-scale mobility framework for an air-to-ground scenario where a UAV-mounted uniform linear array (ULA) structure (FPA for UAV trajectory control or MA for antenna positioning) serves as an aerial base station and transmits the confidential information to a legitimate receiver (Bob), in the presence of an Eve. Both Bob and Eve equip with fixed antennas. This framework quantifies the performance gap between UAV-based macro-mobility and MA micro-positioning, enabling a systematic evaluation of their respective advantages and applicability in communication scenarios under varying system conditions. To our knowledge, this constitutes the first systematic quantification of macro-micro mobility substitutability for secure UAV-assisted wireless communication scenarios. The main contributions of this paper can be summarized as follows.

\- We establish a novel air-to-ground communication model to systematically compare MA-enabled micro-mobility and UAV-enabled macro-mobility for PLS. Furthermore, non-convex average secrecy rate (ASR) maximization problems for both mobility paradigms are formulated, namely joint optimization of antenna positioning and BF vectors under spatial constraints for MA micro-mobility, while joint optimization of UAV trajectory and BF under kinematic constraints for UAV macro-mobility;

\- We develop an efficient alternating optimization (AO) framework to decompose complex joint optimizations into tractable subproblems: 1) Integrated projected gradient ascent (PGA) with simulated annealing (SA) to optimize antenna positioning and BF for MA micro-mobility, avoiding local optima; 2) Combined successive convex approximation (SCA) with interior-point methods to handle trajectory-BF coupling For UAV macro-mobility. Comprehensive computational complexities are analyzed;

Simulations demonstrate that MA micro-mobility outperforms in low-power scenarios (< 0.1W) and antennaconstrained settings (optimal at 4 and 5 antennas), leveraging energy-efficient spatial reconfiguration; 2) UAV macromobility excels under high-power regimes (≥ 1W) and with large antenna arrays, utilizing global mobility for optimal positioning. These findings highlight the adaptive suitability of each scheme under distinct application scenarios, offering critical insights into their respective advantages and optimal deployment conditions.

The remainder of the paper is organized as follows: The related works on UAV and MA assisted technologies are demonstrated in Section II. In Section III, the system model is introduced, and the ASR maximization problems and the performance gap function are formulated. In Section IV, communication duration of confidential information is optimized. Simulations are conducted to demonstrate how the performance gap between the two schemes evolves under different system parameters. Finally, conclusions and future works are discussed in Section VI.

Notations: In this paper, $( \cdot ) ^ { \mathbf { H } }$ and $( \cdot ) ^ { \mathbf { T } }$ denote the Hermitian (conjugate transpose) and transpose operations, respectively. $\mathbf { t r } ( \mathbf { X } )$ represents the trace with diagonal elements <sup>X</sup>. ∇ denote the gradient operator.

## II. RELATED WORKS

PLS methods are gaining significant attention in wireless networks due to their potential for safeguarding sensitive information without relying on cryptographic techniques. Among emerging PLS research trends, UAV trajectory design, MA positioning, and secure BF design have attracted considerable interest for their ability to exploit spatial degrees of freedom to enhance secrecy performance. In this section, we comprehensively review representative PLS schemes leveraging both UAV macro-trajectory optimization and MA micro-positioning to improve the whole system’s performance.

## A. UAV Macro-Mobility Based PLS Design

UAV-enabled macroscopic mobility has emerged as a compelling solution for PLS enhancement, owing to its ability to flexibly control trajectories and establish favorable LoS links.

By planning and tuning the two-dimensional (2D) trajectory of the UAV with integrated and communication systems, it was shown in [22] that UAV can significantly improve the network capacity. Extending into three-dimensional (3D) space, the trajectory and transmission power of the jammer UAV were carefully designed to maximize the security region [11]. Similar works were done [23], [24], [25]. Unlike BF design schemes for confidential signals, Zhang et al. exploited base station-generated jamming signals to degrade the eavesdropping channel and optimized their waveform design accordingly [12]. In addition, the sensing signal was exploited by Zhang et al. for user localization and channel state information (CSI) estimation, leading to the formulation of a joint design problem for UAV trajectory and receive BF [6]. Focusing on the ISAC secure communication system, where the UAV is equipped with a ULA, the average communication secrecy rate was maximized by optimizing the UAV trajectory and ISAC-based BF vectors, as proposed in [13]. Diverging from the aforementioned algorithm, in [14], Tarekegn et al. proposed a novel multi-UAV trajectory control and fair communication framework, by leveraging federated multi-agent deep reinforcement learning (DLA) to autonomously optimize 3D flight paths, which concurrently maximized ground user data rates and network coverage. In both ULA and UPA configurations, Sun et al. derived closed-form lower-bound equations for the ASR after conducting a thorough investigation of the three-dimensional antenna gain characteristics [26].

To sum up, these studies reveal the superiority of UAV macro-scale mobility in achieving substantial performance enhancements across secure communication, network coverage, and system throughput optimization.

## B. MA Micro-Mobility Based PLS Design

In recent years, numerous studies have demonstrated the significant advantages of MA over fixed-position antennas, specifically with regard to improved spatial multiplexing capabilities, interference suppression, flexible BF design, and signal power enhancement [7].

In [15], an MA-MIMO system was proposed to maximize channel capacity through the joint optimization of the transmit and receive MA positions and the transmit signal covariance matrix, demonstrating significant advantages over conventional FPA-MIMO systems, particularly in multipath-rich environments. In comparison, six-dimensional MAs (6DMA) offer significantly enhanced spatial degrees of freedom, which can be separately adjusted in terms of both 3D positions and 3D rotations, subject to practical movement constraints. In [16], Shao et al. identified the directional sparsity property of 6DMA systems, under which a practical three-stage protocol for CSI estimation was established, and the user’s instantaneous channel was optimized.

However, the threat posed by the existence of eavesdropping parties to the system was ignored by the above-mentioned research. To alleviate the risk of confidential signal interception, Tang et al. employed the assumption of perfect CSI to simplify the design of the transmit precoding matrix, artificial noise covariance, and MA positions in pursuit of maximizing the secrecy rate [17]. Building upon this idea, in [21], Liu et al. explored a UAV-mounted linear MA system under the pretense of perfect CSI, where the goal was to enhance throughput capacity by jointly optimizing the transmit BF, the UAV trajectory, and the positions of the MA array elements. Considering the secure transmission with the CSI of eavesdropping parties being unknown, in [27], Hu et al. derived an approximate expression of the secrecy outage probability by using the Laguerre series to approximate the close distribution of the received power gain of eavesdropping parties. Moreover, a joint optimization of the BF at the transmitting end and the antenna position was done for minimizing the secrecy outage probability. Furthermore, in [18], they jointly designed the transmit BF and MA’s positions within the budget constraints, aiming to enhance the secrecy rate. A similar work was presented in [19], Feng et al. demonstrated that moving partial antennas may yield better results than moving all antennas for enhancing the secrecy rate. In [20], Wang et al. adopted MA functions as an interference generator, replacing the traditional FPA-based interference generation scheme. To overcome the analytical challenges posed by unknown Eves locations, an equivalent model was proposed, which approximated the impact of multiple static Eves using a single virtual Eve equipped with an MA array, thereby capturing the spatial reconfigurability of MA [28].

![](images/1c0b79c5e25065fb49bb424a207a5b689f3c15d1e979fc34f75d215cf48902b9.jpg)  
Fig. 1. System model.

Table I provides a comprehensive overview of prominent PLS designs leveraging UAV macro-mobility and MA micromobility. Nevertheless, prior work lacks a systematic comparative analysis quantifying performance difference between MA micro-mobility and UAV macro-mobility paradigms.

## III. NETWORK MODEL AND PRELIMINARIES

As illustrated in Fig. 1, an air-to-ground communication framework is formulated to investigate micro-macro mobility impacts on PLS. Specifically, a UAV equipped with a M transmitting antennas featured by ULA serving as aerial base station sends confidential information to the Bob, in the presence of an passive Eve. Both the Bob and the Eve employ single receiving antennas with fixed positions at (0,0,0) and $( x _ { e } , y _ { e } , 0 )$ , respectively. To more precisely capture the temporal system evolution, the total mission duration $T$ is partitioned into N time slots of duration $\Delta _ { t } = T / N$ , indexed by $n .$ For UAV macro-mobility characterization, UAV altitude is fixed at Hm with horizontal trajectory, and M transmitting antennas are regarded as FPAs. As a result, the position of UAV at n-th time slot is $\mathbf { q } _ { u } [ n ] = ( x _ { u } [ n ] , y _ { u } [ n ] , H )$ . To mitigate mutual coupling between antenna elements, the antennas are typically separated by a distance of $d _ { \mathrm { f i x } } ^ { \mathrm { F P A } } \left( \geq 1 / 2 \lambda \right)$ . For MA micro-mobility <sup>1 2</sup>characterization, UAV maintains hovering at altitude Hm, and each of M transmitting antennas adjusts position within , λ , <sup>[0 4 ]</sup>where λ denotes the wavelength. In this case, the m-th antenna position can be represented as $\mathbf { \bar { p } } _ { m } ^ { \mathrm { L o c } } [ n ] = ( x _ { m } ^ { \mathrm { L o c } } [ n ] , y _ { m } ^ { \mathrm { L o c } } [ n ] , 0 )$ for $m \in \{ 1 , \ldots , M \}$ . The minimum inter-antenna spacing among movable elements is denoted by $d _ { \operatorname* { m i n } } ^ { \mathrm { M A } }$ . In addition, elevation $\theta _ { i } [ n ]$ and azimuth $\phi _ { i } [ n ]$ from UAV to node i ∈ {Bob, Eve} are defined, and $\cos ( \alpha _ { i } [ n ] ) = \sin ( \theta _ { i } [ n ] ) \cdot \cos ( \phi _ { i } [ n ] ) [ 2 6 ] , [ 2 9 ]$ . The key symbols and variables used in this paper are summarized in Table II for clarity and ease of reference.

TABLE I  
MAIN RESEARCHES ON MA/UAV-ENABLED PLS DESIGN
<table><tr><td>Mobility Type</td><td>Reference</td><td>Techniques</td><td>Metrics</td><td>Key Contributions</td></tr><tr><td rowspan="5">macro-mobility</td><td>Zhang et al. [11]</td><td>3D trajectory design of friendly jamming UAV</td><td>Secrecy region</td><td>Investigated the effect of UAVs 3D posi- tion and jamming power on expanding the secrecy region.</td></tr><tr><td>Zhang et al. [12]</td><td>3D trajectory design of UAV&#x27;s trajectory, transmit power, jamming BF and user scheduling</td><td>Secrecy rate</td><td>Jamming signals were utilized to degrade the eavesdropper&#x27;s channel, and their BF is jointly designed for optimal interfer- ence.</td></tr><tr><td>Zhang et al. [6]</td><td>Joint design of UAV&#x27;s 2D trajectory, transmit power and RIS phase shift co-design</td><td>ASR</td><td>Proposed a joint UAV-RIS framework with alternating optimization to achieve near- optimal secrecy rate under perfect CSI.</td></tr><tr><td>Xiu et al. [13]</td><td>Joint design of UAV&#x27;s 2D trajectory and ISAC BF</td><td>ASR</td><td>Proposed a novel autonomous aerial ve- hicle secure communication system with</td></tr><tr><td>Tarekegn et al. [14]</td><td>Multi-UAV 3D trajectory optimization</td><td>Communication coverage, network throughput</td><td>ISAC. Developed a federated deep reinforcement learning scheme to balance communica-</td></tr><tr><td rowspan="5">Micro-mobility</td><td>Ma et al. [15]</td><td>6D MA arrays</td><td>Channel capacity</td><td>tion coverage and throughput. Demonstrated significant capacity gains over FPA-MIMO, especially in rich mul- tipath environments.</td></tr><tr><td>Shao et al. [16]</td><td>Joint design of directional sparse matrix and 6D MA placement design</td><td>Detection error rate, normalized mean squared error</td><td>First identified and exploited directional s- parsity in MA-assisted systems, improving detection and estimation accuracy.</td></tr><tr><td>Tang et al. [17]</td><td>Joint design of transmit precoding, AN covariance and 2D MA positioning</td><td>Secrecy rate</td><td>Pioneered the evaluation of PLS perfor- mance in MA-assisted systems under op- timized spatial configurations.</td></tr><tr><td>Hu et al. [18]</td><td>Joint design of the BF and MA&#x27;s position of transmitter</td><td>Secrecy rate</td><td>Investigated secure communication from an MA-equipped transmitter to a single- antenna receiver under multiple Eves.</td></tr><tr><td>Feng et al. [19]</td><td>Joint design of the BF and MA&#x27;s position of transmitter</td><td>Secrecy rate</td><td>Moving partial antennas may yield better results than moving all antennas.</td></tr><tr><td></td><td>Wang et al. [20]</td><td>Joint design of the BF of MA and FPA, and MA&#x27;s position of transmitter</td><td>Secrecy rate</td><td>MA functions as an interference generator to suppress the eavesdropping channel.</td></tr><tr><td>Macro- &amp; Micro-mobility</td><td>Liu et al. [21]</td><td>Joint design of UAV trajectory, MA positions, transmit BF</td><td>Throughput</td><td>Demonstrated the feasibility of hybrid mo- bility strategies in boosting secure trans-</td></tr></table>

## A. Communication Model

To facilitate tractable analysis, the UAV-to-ground links are modeled as deterministic LoS channels, thereby explicitly excluding complexities arising from aerial scattering and blockage phenomena. Consistent with common practice in related literature [30], [31], perfect knowledge of user positions and CSI is assumed at both Bob and Eve. Let $\mathbf { w } [ n ] \in \mathbb { C } ^ { M \times 1 }$ be the BF vector generated by UAV with M transmitting antennas. Based on the conclusion of [15], [32], the received signal at Bob from UAV can be expressed as

KEY SYMBOLS AND MEANINGS IN THIS PAPER  
TABLE II
<table><tr><td>Symbols</td><td>Meanings</td><td>Pages</td></tr><tr><td> $H$ </td><td>UAV flight altitude</td><td>4</td></tr><tr><td> $M$ </td><td>number of antennas</td><td>4</td></tr><tr><td> $T$ </td><td>total mission duration</td><td>4</td></tr><tr><td> $N$ </td><td>number of time slots</td><td>4</td></tr><tr><td> $\mathbf { q } _ { u }$ </td><td>UAV position</td><td>4</td></tr><tr><td> $\mathbf { p } _ { m } ^ { \mathrm { L o c } }$ </td><td>m-th antenna position</td><td>4</td></tr><tr><td> $d _ { c } ^ { \mathrm { F P A } }$ </td><td>FPA&#x27;s antenna spacing</td><td>4</td></tr><tr><td> $\mathbf { \Pi } _ { J \mathrm { M A } } ^ { \mathrm { n x } }$   $\operatorname* { \omega } _ { \tau \mathrm { ~ M ~ A ~ } }$ </td><td>minimum inter-MA spacing</td><td>4</td></tr><tr><td> $L _ { \mathrm { m a x } } ^ { \mathrm { a v 1 . t . } }$ </td><td>maximum MA-spacing between two time slots</td><td>5</td></tr><tr><td> $\theta _ { i }$ </td><td>elevation angle from UAV to user i</td><td>4</td></tr><tr><td> $\phi _ { i }$ </td><td>azimuth angle from UAV to ground user i</td><td>4</td></tr><tr><td> $d _ { u , i }$ </td><td>distance between UAV and ground user ¿</td><td>4</td></tr><tr><td> $\mathbf { a } _ { i }$ </td><td>steering vectors for ground user i</td><td>4</td></tr><tr><td> $\mathbf { h } _ { i }$ </td><td>channel vector from UAV to ground user ¿</td><td>4</td></tr><tr><td> $\mathbf { w }$ </td><td>transmitting BF vector</td><td>4</td></tr><tr><td> $\sigma _ { i } ^ { 2 }$ </td><td>noise power of user i</td><td>5</td></tr><tr><td> $x _ { \mathrm { m i n } } ^ { m , \mathrm { L o c } } , x _ { \mathrm { m a x } } ^ { m , \mathrm { L o c } }$ </td><td>m-th antenna positioning bounds</td><td>5</td></tr><tr><td> $P _ { \mathrm { m a x } }$ </td><td>maximum communication power</td><td>5</td></tr><tr><td> $\gamma _ { i }$ </td><td>SINR of ground user i</td><td>5</td></tr><tr><td> $\tau$ </td><td>the secrecy rate ¿</td><td>5</td></tr><tr><td> $v _ { u } , a _ { u }$ </td><td>velocity and acceleration of UAV</td><td>6</td></tr><tr><td> $v _ { \mathrm { m a x } } , a _ { \mathrm { m a x } }$ </td><td>maximum velocity and acceleration of UAV</td><td>6</td></tr></table>

$$
y _ { b } [ n ] = \mathbf { h } _ { b } [ n ] ^ { \mathbf { H } } \mathbf { w } [ n ] s [ n ] + \sigma _ { b } ^ { 2 } [ n ] ,\tag{1}
$$

where $\mathbf h _ { b } [ n ] \in \mathbb { C } ^ { M \times 1 }$ denotes the channel response from the <sup>[ ]</sup>UAV to the Bob at the n-th time slot, which is dependent on their instantaneous positions, s n represents the transmitted signal with zero mean and unit power, and $\sigma _ { b } ^ { 2 } [ n ]$ denotes the additive white Gaussian noise (AWGN) at the Bob. Similarly,the signal received at the Eve is given by

$$
y _ { e } [ n ] = \mathbf { h } _ { e } [ n ] ^ { \mathbf { H } } \mathbf { w } [ n ] s [ n ] + \sigma _ { e } ^ { 2 } [ n ] ,\tag{2}
$$

where $\mathbf { h } _ { e } [ n ] \in \mathbb { C } ^ { M \times 1 }$ signifies the channel response from the <sup>[ ]</sup>UAV to the Eve at the n-th time slot, and $\sigma _ { b } ^ { 2 } [ n ]$ denotes the AWGN at the Eve.

For MA micro-mobility characterization, $\cos ( \alpha _ { i } ) =$ sin $( \theta _ { i } [ 0 ] ) \cdot \cos ( \phi _ { i } [ 0 ] )$ holds, since the UAV hovers at its initial location. Accordingly, at the n-th time slot, the steering vectors from UAV to Bob and Eve are given by

$$
\mathbf { a } _ { b } [ n ] = \left[ e ^ { j \frac { 2 \pi } { \lambda } x _ { 1 } ^ { \mathrm { L o c } } [ n ] \cos \alpha _ { b } [ n ] } , \quad \cdot \cdot \quad , e ^ { j \frac { 2 \pi } { \lambda } x _ { M } ^ { \mathrm { L o c } } [ n ] \cos \alpha _ { b } [ n ] } \right] ^ { \mathbf { T } } ,\tag{3}
$$

and

$$
\mathbf { a } _ { e } [ n ] = \left[ e ^ { j \frac { 2 \pi } { \lambda } x _ { 1 } ^ { \mathrm { L o c } } [ n ] \cos { \alpha _ { e } [ n ] } } \quad , \cdot \cdot , \quad e ^ { j \frac { 2 \pi } { \lambda } x _ { M } ^ { \mathrm { L o c } } [ n ] \cos { \alpha _ { e } [ n ] } } \right] ^ { \mathbf { T } } ,\tag{4}
$$

respectively.

Given the elevated deployment of UAV and minimal ground obstructions, the air-to-ground channel exhibits a dominant LoS component.<sup>1</sup> Consequently, based on the conclusion of [25], the path gain at the n-th time slot can be modeled using freespace path loss (FSPL) channel, which accurately captures LoS propagation conditions. This is,

$$
g _ { i } [ n ] = { \frac { \beta _ { 0 } } { d _ { u , i } ^ { \alpha } [ n ] } } , i \in \{ \mathrm { B o b , E v e } \} ,\tag{5}
$$

where $\beta _ { 0 }$ is the reference path loss at a standardized distance of 1 m, and $d _ { u , i } [ n ]$ is the distance between the UAV to ground user i at the n-th time slot. Due to the dominated LoS propagation channel, the setting of $\alpha = 2$ is reasonable. Then, we get

$$
\begin{array} { r } { \mathbf { h } _ { i } [ n ] = \sqrt { g _ { 0 } } \mathbf { a } _ { i } [ n ] , i \in \{ \mathrm { B o b } , \mathrm { E v e } \} . } \end{array}\tag{6}
$$

Given the n-th time slot, the instantaneous signal-to-noise ratio (SNR) at the Bob and the Eve can be expressed as

$$
\gamma _ { b } [ n ] = \frac { { \left| { { \bf { h } } _ { b } ^ { \bf { H } } [ n ] { \bf { w } } [ n ] } \right| ^ { 2 } } } { { \sigma _ { b } ^ { 2 } } } = \frac { { \beta _ { 0 } } { \left| { { \bf { a } } _ { b } ^ { \bf { H } } [ n ] { \bf { w } } [ n ] } \right| ^ { 2 } } } { { d _ { u , b } ^ { 2 } [ n ] \sigma _ { b } ^ { 2 } } } ,\tag{7}
$$

and

$$
\gamma _ { e } [ n ] = \frac { \left| \mathbf { h } _ { e } ^ { \mathbf { H } } [ n ] \mathbf { w } [ n ] \right| ^ { 2 } } { \sigma _ { b } ^ { 2 } } = \frac { \beta _ { 0 } \left| \mathbf { a } _ { e } ^ { \mathbf { H } } [ n ] \mathbf { w } [ n ] \right| ^ { 2 } } { d _ { u , e } ^ { 2 } [ n ] \sigma _ { e } ^ { 2 } } ,\tag{8}
$$

respectively.

Average secrecy rate: According to the Shannon theorem [35], the achievable rate (bits/s/Hz) between the UAV and the Bob at the n-th time slot is $R _ { b } [ n ] = \log ( 1 + \gamma _ { b } [ n ] )$ . Similarly, the achievable rate (bits/s/Hz) between the Alice and the Eve for decoding the confidential information at the n-th time slot is given by $R _ { e } [ n ] = \log ( 1 + \gamma _ { e } [ n ] )$ . Hence, the secrecy rate between the UAV and the Bob at the n-th time slot can be represented as

$$
\tau [ n ] = [ R _ { b } [ n ] - R _ { e } [ n ] ] ^ { + } ,\tag{9}
$$

where $[ x ] ^ { + } \triangleq \operatorname* { m a x } ( x , 0 )$ , and the ASR of the system over all time slots is given by

$$
\frac { 1 } { N } \sum _ { n = 1 } ^ { N } \tau [ n ] ,
$$

which represents a long-term secrecy performance of the systems across all time slots and provides a more comprehensive perspective for evaluating the overall secrecy performance rather than focusing on instantaneous state.

## B. Optimization Problem Formulation

Motivated by micro-macro mobility impacts on PLS, different from the conventional PLS design, this paper aims to answer the question of “Can joint optimization of antenna positioning and transmit BF matrix achieve comparable or superior secrecy performance to conventional joint trajectory-BF design?”, by jointly optimizing the time-varying positions of the MA/UAV and the BF vectors of M transmitting antennas. Specifically, for the case of MA micro mobility, the variables are associated with the antenna positioning and BF vectors, and the optimization problem can be formulated as

$$
\operatorname { P 1 : } \quad \operatorname* { m a x } _ { \mathbf { x } _ { m } , \mathbf { w } } \quad \frac { 1 } { N } \sum _ { n = 1 } ^ { N } \tau [ n ]\tag{10a}
$$

$$
\mathrm { s . t . } \quad \big | x _ { m } ^ { \mathrm { L o c } } [ n ] - x _ { m } ^ { \mathrm { L o c } } [ n - 1 ] \big | \leq L _ { \operatorname* { m a x } } ^ { \mathrm { M A } } , \forall m \in \{ 1 , \ldots , M \} ,
$$

$$
\forall n \in \{ 1 , \ldots , N \}\tag{10b}
$$

$$
x _ { m } ^ { \mathrm { L o c } } \in \left[ x _ { \mathrm { m i n } } ^ { m , \mathrm { L o c } } , x _ { \mathrm { m a x } } ^ { m , \mathrm { L o c } } \right] ,\tag{10c}
$$

$$
\mathbf { t r } \left( \mathbf { w } \mathbf { w } ^ { \mathrm { H } } \right) \leq P _ { \mathrm { m a x } }\tag{10d}
$$

where $\mathbf { x } _ { \mathrm { m } } = [ x _ { 1 } ^ { \mathrm { L o c } } , \dots , x _ { M } ^ { \mathrm { L o c } } ]$ represents the x-axis of MA <sup>= [ ]</sup>in local coordinate system; (10b) limits the displacement of the m-th antenna element within consecutive time slots to the maximum allowable movement distance $L _ { \operatorname* { m a x } } ^ { \mathrm { M A } }$ ; Constraint (10c) restricts the antenna positioning to the designated feasible $\Psi _ { m } ,$ while (10d) enforces the transmit power budget with $P _ { \mathrm { m a x } }$ denoting the upper bound. For the case of UAV macro-mobility, all antenna elements become fixed. Then, the optimization problem

can be written as

$$
\mathrm { P 2 } \colon \operatorname* { m a x } _ { \mathbf { q } _ { u } , \mathbf { w } } \ \frac { 1 } { N } \sum _ { n = 1 } ^ { N } \tau [ n ]\tag{11a}
$$

$$
\begin{array} { r l } { \mathrm { s . t . } } & { { } | v _ { u } [ n ] | \leq v _ { \operatorname* { m a x } } , } \end{array}\tag{11b}
$$

$$
| a _ { u } [ n ] | \leq a _ { \operatorname* { m a x } } ,\tag{11c}
$$

$$
\mathbf { t r } \left( \mathbf { w } \mathbf { w } ^ { \mathrm { H } } \right) \leq P _ { \mathrm { m a x } }\tag{11d}
$$

Constraints (11b) and (11c) limit the UAV’s velocity and acceleration vectors, respectively, and $v _ { \mathrm { m a x } }$ and $a _ { \mathrm { m a x } }$ denote their maximum allowable magnitudes.

However, Problem (10) and Problem (11) are non-convex optimization problems, which are difficult to be solved directly, due to the following three reasons: 1) the operator of $[ \cdot ] ^ { + }$ is <sup>[ ]</sup>non-smoothness for the objective function; 2) the variables $\mathbf { x } _ { m }$ (or $\mathbf { q } _ { u } )$ and <sup>w</sup> are intricately coupling; 3) and they further are quadratic and fractional, which makes it more challenging to be solved. Although there is no general approach to solving them optimally, in the following section IV, we reformulate it and prove that the obtained solution can be approximated as the solution of the original problem.

## IV. PERFORMANCE ANALYSIS AND SECRET RATE MAXIMISATION

In this section, we address the ASR-oriented optimization problems for cases of UAV macro mobility and MA micro mobility. To ensure tractable solutions, the BCD method decomposes each problem into two subproblems. AO algorithm then iteratively updates UAV’s trajectory/MA’s antenna positioning and their associated BF vectors. Finally, a detailed analysis of the computational complexity is provided to evaluate the algorithmic efficiency.

## A. Optimization of Antenna Positioning and BF Matrix for MA Micro-Mobility

To maximize the ASR across all time slots, joint optimization focuses on the x-axis positions of MA elements $\mathbf { x } _ { m }$ and the BF vector <sup>w</sup>. To overcome the non-smooth objective function in Problem (10) caused by the $[ \cdot ] ^ { + }$ operator, which can be eliminated safely through transmission power control. Specifically, transmission suspension occurs when $\tau [ n ] < 0 [ 2 6 ]$

1) Antenna Positioning Optimization for Given BF Vector: The MA position matrix ${ \bf x } _ { m }$ is optimized while fixing both the UAV’s initial position and the BF vector <sup>w</sup>. Since the MA’s displacement range operates at centimeter-to-millimeter scales, it induces negligible variation in the departure angle under far-field propagation conditions. Consequently, the angle $\alpha _ { i }$ remains effectively constant. Let $d _ { u , i }$ be the distance between the UAV and ground user i. To sum up, the steering vector can be expressed as

$$
\mathbf { a } _ { i } [ n ] = \left[ e ^ { j \frac { 2 \pi } { \lambda } x _ { 1 } ^ { \mathrm { L o c } } [ n ] \cos { \alpha _ { u , i } } } , \quad \cdot \cdot \cdot \quad , e ^ { j \frac { 2 \pi } { \lambda } x _ { M } ^ { \mathrm { L o c } } [ n ] \cos { \alpha _ { u , i } } } \right] _ { ( 1 7 ) } ^ { \mathbf { T } } .\tag{12}
$$

The MA positioning problem thus reduces to a computationally tractable form:

$$
\mathbf { P 1 } - \mathbf { 1 } : \operatorname* { m a x } _ { \mathbf { x } _ { m } } \quad \frac { 1 } { N } \sum _ { n = 1 } ^ { N } \left[ \log _ { 2 } \left( 1 + \frac { \beta _ { 0 } \left| \mathbf { a } _ { b } ^ { \mathbf { H } } [ n ] \mathbf { w } \right| ^ { 2 } } { d _ { u , b } ^ { 2 } \sigma _ { b } ^ { 2 } } \right) \right.
$$

$$
- \log _ { 2 } \left( 1 + \frac { \beta _ { 0 } \left| \mathbf { a } _ { e } ^ { \mathbf { H } } [ n ] \mathbf { w } \right| ^ { 2 } } { d _ { u , e } ^ { 2 } \sigma _ { e } ^ { 2 } } \right) \Biggr ]
$$

$$
\mathrm { s . t . } ( 1 0 \mathsf { b } ) , ( 1 0 \mathsf { c } ) , ( 1 0 \mathsf { d } ) .\tag{13a}
$$

Problem (13) still is a non-covex program of $\mathbf { x } _ { \mathbf { M A } }$ , since the dependence of the steering vector on antenna positions is expressed through complex exponential functions, with the resulting function proven to be non-convex with respect to ${ \bf a } _ { i }$ A PGA algorithm to compute a high-quality feasible solution solution. The gradient of $\tau [ n ]$ with respect to $\mathbf { x } _ { m } [ n ]$ is given by

$$
\begin{array} { r } { \nabla _ { \mathbf { x } _ { m } [ n ] } \tau [ n ] = \frac { \beta _ { 0 } } { \ln 2 } \left( \frac { 2 \mathbf { a } ^ { \mathbf { H } } _ { b } [ n ] \mathbf { w } [ n ] \cdot \nabla _ { \mathbf { x } _ { m } [ n ] } \mathbf { a } ^ { \mathbf { H } } _ { b } [ n ] \cdot \mathbf { w } [ n ] } { d _ { u , b } ^ { 2 } [ n ] \sigma _ { b } ^ { 2 } ( 1 + A [ n ] ) } \right. } \\ { \left. - \frac { 2 \mathbf { a } ^ { \mathbf { H } } _ { e } [ n ] \mathbf { w } [ n ] \cdot \nabla _ { \mathbf { x } _ { m } [ n ] } \mathbf { a } ^ { \mathbf { H } } _ { e } [ n ] \cdot \mathbf { w } [ n ] } { d _ { u , e } ^ { 2 } [ n ] \sigma _ { e } ^ { 2 } ( 1 + B [ n ] ) } \right) , } \end{array}
$$

where $\begin{array} { r } { A [ n ] = \frac { \beta _ { 0 } | { \bf a } _ { b } ^ { \bf H } [ n ] { \bf w } [ n ] | ^ { 2 } } { d _ { u . b } ^ { 2 } [ n ] \sigma _ { b } ^ { 2 } } } \end{array}$ , and $\begin{array} { r } { B [ n ] = \frac { \beta _ { 0 } | { \bf a } _ { e } ^ { \bf H } [ n ] { \bf w } [ n ] | ^ { 2 } } { d _ { u , e } ^ { 2 } [ n ] \sigma _ { e } ^ { 2 } } } \end{array}$ . The derivative of ${ \bf a } _ { i } [ n ]$ with respect to $\mathbf { x } _ { \mathrm { M A } } [ n ]$ is given by [18], [36]

(14)

$$
\nabla _ { \mathbf { x } _ { \mathrm { M A } } [ n ] } \mathbf { a } _ { i } [ n ] = \left[ \frac { \partial a _ { i } [ n ] } { \partial x _ { 1 } ^ { \mathrm { L o c } } [ n ] } , \dots , \ \frac { \partial a _ { i } [ n ] } { \partial x _ { M } ^ { \mathrm { L o c } } [ n ] } \right] .\tag{15}
$$

Let symbol of <sup>∗</sup> denote the complex conjugate. By expressing $a _ { i } [ n ] ^ { * }$ in trigonometric form by using Euler’s formula, $e ^ { j x } = $ [ ] $x + j$ x [37], its derivative can be characterized as

$$
\begin{array} { l } { { \displaystyle \nabla _ { x _ { m } ^ { \mathrm { L o c } } [ n ] } a _ { i } [ n ] ^ { * } = \frac { 2 \pi } { \lambda } \cos \alpha _ { i } \cdot \left[ - \sin \left( \frac { 2 \pi } { \lambda } x _ { m } ^ { \mathrm { L o c } } [ n ] \cos \alpha _ { i } \right) \right. } } \\ { { \displaystyle \left. - j \cos \left( \frac { 2 \pi } { \lambda } x _ { m } ^ { \mathrm { L o c } } [ n ] \cos \alpha _ { i } \right) \right] . } } \end{array}\tag{16}
$$

Building on this formulation, we integrate the gradient of $\tau [ n ]$ into the AdaGrad optimization framework to iteratively optimize MA element positions. Specifically, according to the accumulated historical gradient information, the position of the m-th antenna element at $( k + 1 )$ -th iteration is updated as

$$
x _ { m } ^ { \mathrm { L o c } ^ { ( k + 1 ) } } [ n ] = x _ { m } ^ { \mathrm { L o c } ^ { \mathrm { L e } ^ { ( k ) } } [ n ] } + \zeta _ { \mathrm { a d a } } \cdot \nabla _ { x _ { m } ^ { \mathrm { L o c } } [ n ] } \tau [ n ] ,\tag{17}
$$

which adaptively adjusts the learning rate for each dimension, and where $\zeta _ { \mathrm { a d a } }$ represents the adaptive step size. To enforce the movement constraint (10c) maintaining minimum safety distances between adjacent antennas, each position update undergoes a feasibility check to verify compliance with spatial constraints. That is,

$$
\begin{array} { r l } & { x _ { m } ^ { \mathrm { L o c } } ^ { ( k + 1 ) } [ n ] = x _ { m } ^ { \mathrm { L o c } ^ { k } } [ n ] } \\ & { \qquad + d _ { \mathrm { m i n } } ^ { \mathrm { M A } } \cdot \frac { x _ { m } ^ { \mathrm { L o c } ^ { ( k + 1 ) } } [ n ] - x _ { m } ^ { \mathrm { L o c } } [ n - 1 ] } { \left\| x _ { m } ^ { \mathrm { L o c } ^ { \mathrm { [ } k + 1 ) } } [ n ] - x _ { m } ^ { \mathrm { L o c } } [ n - 1 ] \right\| } } \end{array}\tag{18}
$$

Subsequently, the feasible antenna positioning is rigorously constrained within the predefined spatial boundaries satisfying the constraint in (10c), ensuring strict operational region compliance. Finally, the suboptimal antenna positioning in the n-th time slot can be determined by

$$
x _ { m } ^ { \mathrm { { L o c } ^ { * } } } [ n ] = \operatorname* { m i n } ( \operatorname* { m a x } ( x _ { m } ^ { \mathrm { { L o c } } ^ { ( k + 1 ) } [ n ] , x _ { \mathrm { { m i n } } } ^ { m , \mathrm { { L o c } } } } ) , x _ { \mathrm { { m a x } } } ^ { m , \mathrm { { L o c } } } ) )\tag{19}
$$

2) BF Optimization Given Positions of MA Elements: Given a fixed configuration of the MA element positions, the objective is to maximize the ASR by exclusively optimizing the BF vector <sup>w</sup>, subject to the power constraint in (10d). The subproblem is formulated as follows:

$$
\begin{array} { r l r } { \mathbf { P 1 } - \mathbf { 2 } : \underset { \mathbf { w } _ { \mathbf { M A } } } { \mathbf { m a x } } } & { \displaystyle \frac { 1 } { N } \sum _ { n = 1 } ^ { N } \left[ \log _ { 2 } \left( 1 + \varepsilon _ { 1 } \left| \mathbf { a } _ { b } ^ { \mathbf { H } } [ n ] \mathbf { w } [ n ] \right| ^ { 2 } \right) \right. } \\ & { \displaystyle \left. - \log _ { 2 } \left( 1 + \varepsilon _ { 1 } \left| \mathbf { a } _ { e } ^ { \mathbf { H } } [ n ] \mathbf { w } [ n ] \right| ^ { 2 } \right) \right] } & \\ { \mathrm { s . t . ~ } \left( 1 0 \mathrm { d } \right) . } & { \left( \mathrm { \Sigma } \right. } \end{array}\tag{20a}
$$

where $\begin{array} { r } { \varepsilon _ { 1 } = \frac { \beta _ { 0 } } { d _ { u , b } ^ { 2 } \sigma _ { b } ^ { 2 } } } \end{array}$ and $\begin{array} { r } { \varepsilon _ { 2 } = \frac { \beta _ { 0 } } { d _ { u , e } ^ { 2 } \sigma _ { e } ^ { 2 } } . } \end{array}$

For the non-convex optimization of <sup>w</sup> $[ n ]$ , PGA method is adopted again, which is consistent with the approach employed in solving Problem (13). The gradient of the objective function with respect to ${ \bf w } [ n ]$ is given by

$$
\begin{array} { r l r } & { } & { \nabla _ { \mathbf { w } [ n ] } \tau [ n ] = \frac { \beta _ { 0 } } { \ln 2 } \left[ \frac { \varepsilon _ { 1 } [ n ] \nabla _ { \mathbf { w } [ n ] } \left. \mathbf { a } _ { b } ^ { \mathbf { H } } [ n ] \mathbf { w } [ n ] \right. ^ { 2 } } { 1 + \varepsilon _ { 1 } [ n ] \left. \mathbf { a } _ { b } ^ { \mathbf { H } } [ n ] \mathbf { w } [ n ] \right. ^ { 2 } } \right. } \\ & { } & { \left. - \frac { \varepsilon _ { 2 } \left[ n \right] \nabla _ { \mathbf { w } [ n ] } \left. \mathbf { a } _ { e } ^ { \mathbf { H } } [ n ] \mathbf { w } [ n ] \right. ^ { 2 } } { 1 + \varepsilon _ { 2 } \left[ n \right] \left. \mathbf { a } _ { e } ^ { \mathbf { H } } [ n ] \mathbf { w } [ n ] \right. ^ { 2 } } \right] , } \end{array}\tag{21}
$$

where

$$
\begin{array} { r } { \nabla _ { { \mathbf w } [ n ] } \left| { \mathbf a } _ { b } ^ { \mathbf H } [ n ] { \mathbf w } [ n ] \right| ^ { 2 } = 2 { \mathbf a } _ { b } [ n ] { \mathbf a } _ { b } ^ { \mathbf H } [ n ] { \mathbf w } [ n ] , } \end{array}\tag{22}
$$

$$
\nabla _ { \mathbf { w } [ n ] } \left| \mathbf { a } _ { e } ^ { \mathbf { H } } [ n ] \mathbf { w } [ n ] \right| ^ { 2 } = 2 \mathbf { a } _ { e } [ n ] \mathbf { a } _ { e } ^ { \mathbf { H } } [ n ] \mathbf { w } [ n ] .\tag{23}
$$

Similarly, the BF vector is updated using AdaGrad framework [38], [39] as follows

$$
\begin{array} { r } { \mathbf { w } ^ { ( k + 1 ) } [ n ] = \mathbf { w } ^ { ( k ) } [ n ] + \delta _ { \mathrm { a d a g } } \nabla _ { \mathbf { w } [ n ] } C ( \mathbf { w } [ n ] ) . } \end{array}\tag{24}
$$

A projection is applied to ensure the updated vector satisfies the power constraint

$$
{ \bf w } ^ { ( k + 1 ) * } [ n ] = \Pi \left\{ { \bf w } ^ { ( k + 1 ) } [ n ] , { \bf w } ^ { \prime } [ n ] \right\} ,\tag{25}
$$

where the normalized vector ${ \bf w } ^ { \prime } [ n ]$ is defined by [19], [40]

$$
{ \bf w } ^ { \prime } [ n ] = { \bf w } [ n ] \sqrt { \frac { P _ { \mathrm { m a x } } } { q } } ,\tag{26}
$$

where $q = \mathrm { t r } ( \mathbf { w } [ n ] \mathbf { w } ^ { \mathrm { H } } [ n ] )$ denotes the instantaneous transmit power associated with the unnormalized BF vector.

3) Simulated Annealing Algorithm for Convergence: To mitigate local optimal convergence risks, we employ the simulated annealing (SA) method [41], a well-established stochastic optimization technique. Candidate solutions are probabilistically accepted with probability $p ,$ which is defined as

$$
p = \left\{ \begin{array} { l l } { 1 , } & { \tau [ n ] ^ { ( k + 1 ) } > \tau [ n ] ^ { ( k ) } } \\ { \exp \left( \frac { \tau [ n ] ^ { ( k + 1 ) } - \tau [ n ] ^ { ( k ) } } { T ^ { ( k + 1 ) } } \right) , } & { \tau [ n ] ^ { ( k + 1 ) } \leq \tau [ n ] ^ { ( k ) } } \end{array} \right.\tag{27}
$$

where $T ^ { ( k + 1 ) } = \rho T ^ { ( k ) }$ denotes the temperature at the k -th iteration, and $\rho$ is the cooling factor. By avoiding premature convergence to local optima in antenna positioning and BF of the MA obtained by PGA, the simulated annealing method enables the optimization process to explore a broader solution space. Consequently, a near-optimal solution for Problem (10) is attained. Although this solution may not represent the global optimum, it delivers a satisfactory high-quality outcome.

## B. UAV-Based Macro-Mobility Optimization

By jointly optimizing UAV trajectory <sup>q</sup> and BF <sup>w</sup>, we aim to maximize the ASR over all time slots. Similar to Problem (10), the $\lceil \cdot \rceil ^ { + }$ operator can be also omitted safely.

<sup>[ ]</sup>1) UAV Trajectory Optimization for Given BF Vector: The UAV trajectory is optimized for a predefined BF vector with ULA inter-element spacing fixed at $\bar { d } _ { \mathrm { f i x } } ^ { \mathrm { U L A } }$ . The steering vector is

$$
\mathbf { a } _ { i } [ n ] = \left[ e ^ { \frac { j 2 \pi } { \lambda } x _ { 1 } ^ { \mathrm { L o c } } \cos \alpha _ { i } [ n ] } , \quad \ldots , \quad e ^ { j \frac { 2 \pi } { \lambda } x _ { M } ^ { \mathrm { L o c } } \cos \alpha _ { i } [ n ] } \right] ^ { \mathrm { T } } ,\tag{28}
$$

where $x _ { m } ^ { \mathrm { L o c } } - x _ { m - 1 } ^ { \mathrm { L o c } } = d _ { \mathrm { f i x } } ^ { \mathrm { F P A } }$ for $m \in \{ 2 , . . . , M \}$

Crucially, (7) and (8) show that the distance term $d _ { u , i }$ exhibits higher sensitivity to $\mathbf { q } _ { \mathrm { U A V } }$ than the steering vector ${ \bf a } _ { i } .$ We approximate ${ \bf a } _ { i } [ n ]$ at the $( k + 1 )$ -th iteration using that of <sup>[ ]</sup>the k-th iteration trajectory $\mathbf { q } _ { u } [ n ]$ , since successive trajectory updates yield minimally displaced UAV positions [21]. Thus, corresponding Subproblem can be formulated as:

$$
\mathrm { P } ( 2 \mathrm { - } 1 ) \colon \ \operatorname* { m a x } _ { \mathbf { q } _ { \mathbf { u } } } \ \frac { 1 } { N } \sum _ { n = 1 } ^ { N } \left[ \log _ { 2 } \left( 1 + \frac { s _ { 1 } [ n ] } { d _ { u , b } ^ { 2 } [ n ] } \right) \right.\tag{29a}
$$

$$
- \log _ { 2 } \left( 1 + \frac { s _ { 2 } [ n ] } { d _ { u , e } ^ { 2 } [ n ] } \right) \Biggr ]
$$

$$
\mathrm { s . t . } \quad ( 1 1 \mathrm { b } ) , ( 1 1 \mathrm { c } ) .\tag{29b}
$$

where $\begin{array} { r } { s _ { 1 } [ n ] = \frac { \beta _ { 0 } | \mathbf { a } _ { b } ^ { \mathbf { H } } [ n ] \mathbf { w } [ n ] | ^ { 2 } } { \sigma _ { h } ^ { 2 } } } \end{array}$ and $\begin{array} { r } { s _ { 2 } [ n ] = \frac { \beta _ { 0 } | \mathbf { a } _ { e } ^ { \mathbf { H } } [ n ] \mathbf { w } [ n ] | ^ { 2 } } { \sigma _ { e } ^ { 2 } } } \end{array}$ . Under this configuration, the $\mathrm { U A V } \ ' _ { \mathrm { s } }$ positional variation primarily impacts the distance $d _ { u , i }$ . Nevertheless, the sub-problem is a non-convex integer programming problem that is difficult to be optimally solved efficiently. To address the problem, the slack variables $u [ n ]$ and w n are introduced to relax constraint (30b)–(30d). The ASR maximization problem at the n-th time slot can be reformulated as

$$
\begin{array} { r l r } { { \mathrm { P } ( 2 \mathrm { - } 1 ) } ^ { \prime } } & { \underset { \mathbf { q } [ n ] } { \mathrm { m a x } } } & { \displaystyle \frac { 1 } { N } \sum _ { n = 1 } ^ { N } \left[ \log _ { 2 } \left( 1 + \frac { s _ { 1 } [ n ] } { u [ n ] } \right) \right. } \\ & { } & \\ & { } & { \displaystyle \left. - \log _ { 2 } \left( 1 + \frac { s _ { 2 } [ n ] } { w [ n ] } \right) \right] } \\ & { } & \\ & { \mathrm { s . t . } ~ w [ n ] - x _ { n } ^ { 2 } [ n ] + 2 x _ { e } x _ { u } [ n ] - x _ { e } ^ { 2 } - y _ { u } ^ { 2 } [ n ] } \end{array}\tag{30a}
$$

$$
+ 2 y _ { e } y _ { u } [ n ] - y _ { e } ^ { 2 } - H ^ { 2 } \leq 0 , \forall n\tag{30b}
$$

$$
x _ { u } ^ { 2 } [ n ] - 2 x _ { b } x _ { u } [ n ] + x _ { b } ^ { 2 } + y _ { u } ^ { 2 } [ n ] - 2 y _ { b } y _ { u } [ n ]
$$

$$
+ y _ { b } ^ { 2 } + H ^ { 2 } - u [ n ] \leq 0 , \forall n\tag{30c}
$$

$$
w [ n ] \geq H ^ { 2 }\tag{30d}
$$

$$
( 1 1 \mathsf { b } ) , ( 1 1 \mathsf { c } )\tag{30e}
$$

Building upon the optimization structure established in prior analysis, we initialize a feasible UAV trajectory configuration $\mathbf { q } _ { 0 } \triangleq [ \mathbf { q } _ { 0 } [ 1 ] , \dots , \mathbf { q } _ { 0 } [ N ] ] ^ { \mathbf { T } }$ , along with the corresponding slack variable vector $\mathbf { u } _ { 0 } \triangleq [ \ddot { u _ { 0 } } [ 1 ] , \dots , u _ { 0 } [ N ] ] ^ { \mathbf { T } }$ . These initializations serve as the starting point for the iterative trajectory refinement procedure, ensuring that each iteration remains within the feasible region defined by the kinematic and spatial constraints. To approximate the non-convex objective and constraints, the logarithmic and squared terms are relaxed via First-order Taylor expansion around the initial points, and then the final optimization problem exhibits a concave objective function and convex constraints, which can be directly solved using the CVX toolbox in MATLAB [42], [43]. Readers are referred to [42], [43], [44] for comprehensive details.

2) BF Optimization for Given UAV Macro-Mobility Trajectory: The BF vector optimization in this case can be achieved by using similar methods in the Subsection IV-A2. .

## C. AO Algorithm for ASR Maximization

By alternately solving the above subproblems (UAV trajectory/antenna positioning and the BF), the ASR maximization for MA micro-mobility and UAV macro-mobility can be efficiently achieved. First of all, SCA method is employed to iteratively approximate the optimal UAV trajectory within a stochastic programming framework. Furthermore, to mitigate gradient estimation errors induced by random variables, a Monte Carlo sampling mechanism is integrated into PGA architecture. The pesudo-codes of the PGA-based BF optimization and AO procedure are given in Algorithm 1 and Algorithm 2, respectively.

1) Complexity Analysis of Problem (10): The original optimization problem (10) is decoupled into two interdependent subproblems via BCD method: (1) antenna positioning optimization using PGA, and (2) BF design via PGA. We solve these subproblems alternately to achieve progressive optimization. The computational complexity of the BF optimization subproblem is $\mathcal { O } ( I _ { \operatorname* { m a x } } M _ { t } )$ , dominated by the Monte Carlo sample size $M _ { t }$ and maximum iterations $I _ { \mathrm { m a x } }$ . The antenna positioning optimization subproblem exhibits higher complexity $\mathcal { O } ( M I _ { \operatorname* { m a x } } M _ { t } )$ due to sequential position exploration for each of the M antenna elements. With $I _ { \mathrm { m a x } } \mathrm { A O }$ iterations in the outer loop, the overall complexity is $\mathcal { O } ( I _ { \operatorname* { m a x } } ^ { 2 } { \tilde { } M } M _ { t } )$

2) Complexity Analysis of Problem (11): The problem (11) can be decomposed into two subproblems: 1) the UAV trajectory optimization using the CVX toolbox; 2) BF vector optimization. The computational complexity of the BF design subproblem aligns with that of Problem (10). In contrast, the UAV trajectory optimization subproblem is formulated as a convex optimization one and solved via CVX empowered by interior-point method. The complexity of this subproblem is quantified as $O ( N _ { \mathrm { v a r } } ^ { 3 } \log ( \epsilon ^ { - 1 } )$ , where $N _ { \mathrm { v a r } }$ denotes the number of variables, and  denotes the solution accuracy. Consequently, the complete complexity is $\mathcal { O } ( I _ { \mathrm { i t e r } } ( N _ { \mathrm { v a r } } ^ { 3 } \log ( \epsilon ^ { - 1 } ) + I _ { \operatorname* { m a x } } M _ { t } ) )$

Algorithm 1: PGA-based BF Optimization.   
1: Initialization: the number of antennas M, initial BF   
$\mathbf { w } ^ { ( 0 ) }$ , the maximum iteration number $I _ { \mathrm { m a x } } ,$ the   
maximum Monte Carlo simulation number $M _ { t } ,$ , the   
gradient value G   
2: Repeat   
3: Updating $k = k + 1$   
4: Updating $G = 0$   
5: Repeat   
6: Calculating $\nabla _ { \mathbf { w } } \tau$ with Eq. (21)   
7: Updating $G = G + \nabla _ { \mathbf { w } } \tau$   
8: Until $M _ { t }$ <sup>=</sup>is reached   
9: Updating $G = G / M _ { t }$   
10: Calculating $\mathbf { w } ^ { ( k + 1 ) }$ with Eq. (25)   
11: Feasibility verification of $\mathbf { w } ^ { ( k + 1 ) }$   
12: Until the maximum iteration number $I _ { \mathrm { m a x } }$ is reached

Algorithm 2: Proposed AO for Problems (10) and (11).   
1: Initialization: the maximum iteration number $I _ { \mathrm { m a x } } ,$   
initial and terminal position of $\mathrm { U A V } ~ q _ { 0 }$ and $q _ { t } .$ , the   
initial positions of MA $\mathbf { x } _ { m } ^ { ( 0 ) }$ (or the initial trajectory of   
$\mathrm { U A V }  { \mathbf { q } } _ { u } ^ { ( 0 ) } ) .$ , the BF $\mathbf { w } ^ { ( 0 ) } , \tau _ { 0 } = f _ { \mathbf { P } \mathbf { 1 } } ( \mathbf { x } _ { m } ^ { ( 0 ) } , \mathbf { w } ^ { ( 0 ) } )$   
$( \tau _ { 0 } = f _ { \mathbf { P 2 } } ( \mathbf { q } _ { u } ^ { ( 0 ) } , \mathbf { w } ^ { ( 0 ) } ) )$ , index of initial iteration $i = 0 ,$   
<sup>= (</sup>cooling factor $\rho ,$ <sup>)</sup>and initial temperature $T ^ { 0 }$   
2: Repeat   
3: $k = k + 1$   
<sup>=</sup>4: Update $\mathbf { x } _ { \mathbf { M A } } ^ { ( k ) }$ (or $\mathbf { q } _ { u } ^ { ( k ) } )$ with initial point   
$( \mathbf { x } _ { m } ^ { ( k - 1 ) } , \mathbf { w } ^ { ( k - 1 ) } )$ (or $( \mathbf { q } _ { u } ^ { ( k - 1 ) } , \mathbf { w } ^ { ( k - 1 ) } ) )$ with (20) (or   
<sup>(</sup>(30))   
5: Updating $\mathbf { w } ^ { ( k ) }$ with initial point $( \mathbf { x } _ { m } ^ { ( k ) } \mathbf { \Lambda } _ { \mathrm { c o m } } , \mathbf { w } ^ { ( k - 1 ) } )$   
with Eq.   
6: $\tau ^ { ( k ) } = f _ { \mathbf { P 1 } } ( \mathbf { x } _ { m } ^ { ( k ) } , \mathbf { w } ^ { ( k ) } )$ (or   
$\tau ^ { ( k ) } = f _ { \mathbf { P 2 } } ( \mathbf { q } _ { u } ^ { ( k ) } , \mathbf { w } ^ { ( k ) } ) ) .$   
7: <sup>= (</sup> Calculating $p$ <sup>)</sup>with Eq. (27)   
8: if $p <$ random <sub>,</sub>   
9: $\tau ^ { ( k ) } = \tau ^ { ( k - 1 ) } , \mathbf w ^ { ( \dot { k } ) } = \mathbf w ^ { ( k - 1 ) } , \mathbf x _ { m } ^ { ( k ) } = \mathbf x _ { m } ^ { ( k - 1 ) }$   
10: end if   
11: $T ^ { ( k + 1 ) } = \rho T ^ { ( k ) }$   
12: Until the maximum iteration number $I _ { \mathrm { m a x } }$ is reached

Findings: Although both Problem (10) and Problem (11) follow a similar alternating optimization structure, the latter has higher computational complexity compared to the former due to the complexity of the trajectory optimization. In Problem (10), the antenna positions are updated independently using a simple first-order method. By contrast, Problem (11) involves joint optimization of UAV’s trajectory over multiple time slots using an interior-point method featured by second-order, resulting in higher computational complexity. Consequently, the overall complexity of Problem (11) increases substantially, especially when the number of time slots is large.

TABLE III  
SIMULATED PARAMETERS AND VALUES
<table><tr><td>Symbol</td><td>Meanings</td><td>Values</td></tr><tr><td>H</td><td>the flight altitude of UAV</td><td>{50, 100}m</td></tr><tr><td>qb</td><td>the position of Bob</td><td>(0, 0, 0)</td></tr><tr><td>qe</td><td>the position of Eve</td><td>(400, 0,0)</td></tr><tr><td>q0</td><td>the initial position of UAV</td><td>(200, 200, H)</td></tr><tr><td>qt</td><td>the target position of UAV</td><td> $( 2 0 0 , - 2 0 0 , \stackrel { . } { H } )$ </td></tr><tr><td> $_ \alpha$ </td><td>path-loss exponent</td><td></td></tr><tr><td> $M$ </td><td>the number of antennas</td><td> $[ 2 , 8 ] ^ { [ 4 6 ] }$ </td></tr><tr><td> $N$ </td><td>number of time slots</td><td> $[ 2 0 , \dot { 6 } 0 ] [ 2 4 ]$ </td></tr><tr><td> $F$ </td><td>frequency band of communication</td><td> $\bar { 2 } 8 \mathrm { G H z } ^ { [ 1 9 ] }$ </td></tr><tr><td> $\lambda$ </td><td>wavelength</td><td> $0 . 0 1 0 7 \mathrm { m } ^ { \left[ 1 9 \right] }$ </td></tr><tr><td> $T$ </td><td>Initial temperature</td><td>1</td></tr><tr><td> $\rho$ </td><td>cooling coefficient</td><td> $0 . 8 ^ { [ 1 9 ] }$ </td></tr><tr><td> $P$ </td><td>communication power</td><td> $[ 0 . 1 , 1 0 ] \mathrm { w }$ </td></tr><tr><td> $a _ { 0 } ^ { \mathrm { m a x } }$ </td><td>maximum acceleration of the UAV</td><td> $\mathrm { { \bar { 3 } m / s ^ { 2 } } }$ </td></tr><tr><td> $v _ { \mathrm { m a x } }$ </td><td>maximum speed of the UAV</td><td> $1 5 \mathrm { m / s }$ </td></tr><tr><td> $d ^ { \mathrm { M A } }$   $d _ { \mathrm { m i n } } ^ { \ast \mathbf { x } }$ </td><td>Minimum inter-MA distance</td><td> $1 / 2 \lambda ^ { [ 4 7 ] }$ </td></tr></table>

![](images/da0cad3ca848e400f76075d999bfb0023fadea98bd3f12433ab42a3b5f00f489.jpg)  
Fig. 2. ASR of MA micro-mobility vs. the number of iterations.

## V. EVALUATIONS

In this section, numerical simulations are presented to evaluate the secrecy performance of micro-mobility and macromobility and quantify their performance differences. Under a representative single-Bob single-Eve scenario, two schemes are simulated: (1) MA micro-mobility: The UAV maintains its initial position while dynamically adjusting each of M antenna elements along the x-axis within a λ range, with BF vector jointly optimized. (2) UAV macro-mobility: The UAV equipped with a λ · M-spaced ULA flies at a fixed altitude of H, with trajectory and BF optimized for secrecy performance. Key simulation parameters are listed in Table III.

## A. Convergence Behavior Analysis

The convergence performance of the proposed AO algorithm, optimizing MA positioning, is validated under the setting of $P = 1 \mathrm { W }$ and $H = 5 0$ m. Fig. 2 shows the ASR versus the number of iterations for the MA micro-mobility. Significant

![](images/cdbca07b52990df5b5dc6e1e983901d4ef1b172cf0f9e33d36397624354d96fa.jpg)  
Fig. 3. Optimal antenna positions (M = 4).

![](images/148e1eeec385e6b927cfd05e326c24570f12a68a84b2673fac9149f32db94173.jpg)  
Fig. 4. Optimal antenna positions (M = 5).

![](images/4b727cffcafb9fa725e7a02a63366c91cba587f3f95b4de9ad3cde3b2a57b3d6.jpg)  
Fig. 5. ASR of UAV macro-mobility vs. the number of iterations.

ASR fluctuations occur within the first 1,000 iterations for M 4, attributable to the probabilistic acceptance mechanism in the SA algorithm that prevents local optimum trapping. Beyond this point, the ASR stabilizes progressively, converging at th 3207-th iteration to a steady-state value of 4.1046 bps/Hz. For M $= 5 ,$ pronounced oscillations persist until 2595 iterations before converging to 5.315 bps/Hz. The stochastic nature of SA causes minor convergence-timing variations across trials, though all instances converge reliably within the 10000-iteration threshold. The ASR enhancement with the number of antenna elements, stems from improved spatial diversity and BF resolution, which will be analyzed in the following Subsection. Optimized MA configurations for M 4 and M 5 are shown in Fig. 3 and Fig. 4, respectively.

Fig. 5 illustrates convergence behavior and ASR variation for the UAV macro-mobility. The effective optimization steps total approximately 6,000 (100 outer-loop iterations×60 internal CVX optimizations). Despite initial fluctuations, ASR stabilizes within 100 iterations, demonstrating reliable convergence.

![](images/463ad105e02c178171a9aa7c7b1f0b372d1cc4944e8fec6fcc9ad8bf2512f83d.jpg)  
Fig. 6. Flight trajectory of UAV.

Fig. 7. ASR of MA micro-mobility vs. the number of antennas.  
![](images/b5fbd8ae1aafcf90a823dc63ee3fd7970ecdba603dea96b2695331e5222d6f26.jpg)

Performance improves progressively with longer time slots, as extended operational time enables more flexible trajectories. Fig. 6 confirms the UAV dynamically approaches Bob while distancing from Eve, reducing interception risk. A longer flight duration enables a more flexible trajectory, allowing the UAV to explore more favorable spatial configurations. However, when the flight duration is less than N , the UAV is constrained to <sup>= 20</sup>follow an almost straight-line trajectory toward its destination, limiting its ability to optimize secrecy performance.

## B. ASRs for MA Micro-Mobility and UAV Macro-Mobility

The MA micro-mobility and UAV macro-mobility are systematically evaluated under different settings of antenna counts and transmission powers, with comparative analysis across two mobility paradigms at H 50 m. Fig. 7 shows the ASR versus the number of antennas for the MA micro-mobility. It can be noticed that ASR increases with the number of antennas when M < due to enhanced spatial degrees of freedom, but declines over the number of antennas increasing from spatial constraints and mutual coupling effects. Conversely, Fig. 8 demonstrates ASR improvement with M for the UAV macro-mobility. Both schemes exhibit significant ASR gains with higher transmission powers $( 0 . 1 \mathrm { W } \to 1 0 \mathrm { W } )$ , attributed to improved signal fidelity and SNR of legitimate user. Fig. 9 quantifies the performance gap: The MA micro-mobility outperforms at 0.1 W, while the UAV macro-mobility dominates at higher power $( P \ge 1 \ \mathsf { W } )$ except under specific conditions. Given that the solutions derived from SA-based algorithms are suboptimal and exhibit slight variations with each execution, fitting curves are utilized to effectively capture the overall trend, providing a clear and intuitive representation of the system’s performance when plotted for distinct values of M. Notably, performance difference degradation at $M = \{ 4 , 5 \}$ in MA micro-mobility confirms excessive antenna movement provides diminishing returns.

![](images/70c39e21b99faf7db5965fb5bd4fe2d064a371aa0ee4f3aa0a8292f1ccc91722.jpg)  
Fig. 8. ASR of UAV macro-mobility vs. the number of antennas.

![](images/cfeec57cd527eac65c6d25b4080835095b2e881efb8b794f0e332e6133293d39.jpg)  
Fig. 9. Δτ vs. the number of antennas.

The impacts of transmission power and flight altitude on the ASR achieved by MA micro-mobility and UAV macro-mobility are illustrated in Fig. 10 and Fig. 11. We can confirm significant ASR improvements with increasing transmission power across both mobility paradigms, consistent with prior observations in Fig. 7 and 8. Performance at H 100 m consistently surpasses that of H 100 m due to reduced path loss to legitimate users, enhanced path loss disparity between legitimate and eavesdropper channels, and improved geometric anti-interception advantage. Fig. 12 quantifies the cross-scheme performance gap ( τ ), revealing MA-micro-mobility superiority at low power (P 0.1W), while UAV-macro-mobility dominates at higher power $( P { \ge } 1 \mathsf W )$ and altitudes owing to superior spatial reconfiguration capability – particularly evident in the performance saturation of MA micro-mobility at $M { = } 5$ and $H = 5 0$ m versus the sustained gains in UAV configurations.

![](images/9a1704cb9bc06f84e6014158a590ee351b4e74cd6298ebb7c7d0c99aabcebd13.jpg)  
Fig. 10. ASR of MA micro-mobility vs. transmission power.

![](images/682705eb8b9456f0d0dc12e32d92987c8896f1085eaaeebf9361196d71c8cc37.jpg)  
Fig. 11. ASR of UAV macro-mobility vs. transmission power.

![](images/80259e7bae2e8992f111a2b46c58c9ca5a22c79fa999385761a5924be271f416.jpg)  
Fig. 12. Δτ vs. transmission power.

![](images/4a3bcadd260e2d3ac9ee18d8db364703fc7ca63e197530b10dd01a61540d8e41.jpg)  
Fig. 13. ASR vs. noise power.

![](images/9f4fd8d792215a1b0e4abdd3976680a0798513518427542f9004381cddbaf217.jpg)  
Fig. 14. Δτ vs. noise power.

Finally, with the settings of $H = 1 0 0 \mathrm { m } , M { = } 4$ and $\mathrm { \mathit { P } = 0 . 1 W } ,$ Fig. 13 validates noise power impact on ASR, demonstrating decreasing ASR for both MA micro-mobility and UAV macro-mobility with increasing noise due to Bob’s greater sensitivity to noise variations compared to Eve. The MA-based micro-mobility scheme consistently outperforms the UAV-based counterpart in these conditions, as described by fitted curves converging, though Fig. 14 reveals the performance gap $( \Delta \tau )$ progressively narrows at higher noise levels, MA’s fine-grained spatial control advantage diminishes under severe noise interference as environmental disturbances overwhelm signal refinement capabilities.

Findings: All above results demonstrate the complementary advantages of both mobility paradigms: The MA-based micromobility approach achieves superior secrecy performance under low transmit power and moderate antenna configurations by leveraging fine-grained spatial reconfigurability to enhance legitimate link quality and suppress signal leakage. Conversely, the UAV-based macro-mobility approach excels in high-power regimes with larger antenna arrays through global mobility that enables optimal positioning relative to legitimate users and eavesdroppers. Strategic integration of MA’s local adaptability and UAV’s global flexibility can significantly enhance overall secrecy performance.

![](images/cfe47c37ca612e5f3242ecf1e6321cb900dc828f209f015d87aa658c2445fb81.jpg)  
(a) Previous beam gain

![](images/a1c6e8935c49242f84df773455b35b77c686a77b7e3ecded4a4c207a33aec46a.jpg)  
(b) Optimized beam gain

![](images/096e7d7b6f73be243cf7d616aeacfbd2e33d8f926b3569e8354d8ea7bd919ef7.jpg)  
(a) Previous beam gain

![](images/b1d721ff7e5384f0d1e2fe3cbc314d5d567023c7b41f55ce57760ae9c0cb99f5.jpg)  
(b) Optimized beam gain

Fig. 15. Receive antenna gain at different locations (4λ space).  
![](images/178b99f750de476fc54e5b01568229f03e12794f7977ed1c84db2dfd52bc0e6e.jpg)  
(a) Previous beam gain

![](images/90bfd92f9e4ecff60cfee99f7fb065b3e3fe368cb932f437725d17ef4d5c19e1.jpg)  
(b) Optimized beam gain  
Fig. 16. Receive antenna gain at different locations (λ space).

Fig. 17. Receive antenna gain (20-th time slot).  
![](images/9e3d8c210a1e8afaafcb4352d9a67b606961a54c093967cbbdcec8bbf259a05d.jpg)  
(a) Previous beam gain

![](images/150073d5720d113b8195d87f6a98fd91fff5b94ce7c5f6bea8404bf4d05b60ae.jpg)  
(b) Optimized beam gain  
Fig. 18. Receive antenna gain (40-th time slot).

## C. 3D BF Gain of MA

To evaluate BF optimization impacts at Bob and Eve under P 1W and M 2, each antenna element can move within [0, λ ], Fig. 15 demonstrates the MA micro-mobility’s 3D gain pattern: no antenna positioning reveals critical security risks with Bob’s gain substantially lower than Eve’s, as shown in Fig. 15(a). With the joint optimization of antenna positioning and BF vector, as shown in Fig. 15(b), it achieves 8.217dB gain at Bob and -11.855dB at Eve, yielding a 20.072dB security gap through spatial reconfiguration that concentrates energy toward legitimate users while suppressing Eve leakage. Contrastingly, when movement range of each MA element decreases from λ to λ, Fig. 16 exhibits broader main lobes, smoother angular distributions, and reduced side-lobe fluctuations, indicating degraded spatial resolution from constrained antenna movement. Joint optimization of antenna positioning and BF vector dynamically reshapes radiation patterns to enhance secrecy across varying mobility constraints.

Fig. 17 and Fig. 18 demonstrate dynamic BF gain evolution of the UAV macro-mobility in 20-th and 40-th time slots, where non-optimized patterns exhibit poor directional discrimination with energy leakage toward Eve and insufficient gain concentration at Bob across both time instants. While optimized configurations achieve significant spatial reconfiguration: adaptive beam steering precisely tracks Bob’s trajectory while suppressing Eve-directed side-lobes by 15 dB at least and enhancing Bob’s main-lobe gain by 8-12 dB. This temporal adaptability sustains secrecy performance despite nonlinear receiver angle variations during mobility, confirming the framework’s capability to dynamically balance signal enhancement and leakage suppression through real-time spatial optimization under UAV macro-scale movement constraints.

## VI. CONCLUSION

Based on the comprehensive investigation conducted in this paper, it was conclusively demonstrated that MA-enabled micromobility and UAV-enabled macro-mobility exhibited distinct yet complementary advantages for enhancing PLS in air-to-ground communications. Through the development of a dual-scale mobility framework and the formulation of non-convex ASR maximization problems for both paradigms, the research systematically quantified their performance boundaries. The performance gap analysis further highlighted critical limitations: MA systems faced diminishing returns beyond 5 antennas due to mutual coupling, while UAV systems exhibited restricted flexibility under short mission duration. Environmental factors such as high noise levels and increased flight altitude reduced MA’s finegrained control advantage but minimally affected UAV’s macroscale adaptability. Crucially, neither approach universally superseded the other; instead, their synergistic integration emerged as the most promising direction. The MA’s real-time beam manipulation capabilities complemented the UAV’s coverageoriented mobility, suggesting that hybrid micro-macro architectures could optimally balance security, energy efficiency, and deployment complexity in next-generation aerial networks. This work thus established a foundational framework for adaptive mobility strategy selection and pioneered the exploration of hierarchical spatial control in secure wireless communications.

## REFERENCES

[1] K. Meng et al., “UAV-enabled integrated sensing and communication: Opportunities and challenges,” IEEE Wireless Commun., vol. 31, no. 2, pp. 97–104, Apr., 2024.

[2] Z. Xiao et al., “A survey on millimeter-wave beamforming enabled UAV communications and networking,” IEEE Commun. Surveys Tut., vol. 24, no. 1, pp. 557–610, Firstquarter 2022.

[3] Y. He et al., “A review of physical layer security in aerial–terrestrial integrated Internet of Things: Emerging techniques, potential applications, and future trends,” Drones, vol. 9, no. 4, 2025, Art. no. 312.

[4] J. Wang et al., “Physical layer security for UAV communications: A comprehensive survey,” China Commun., vol. 19, no. 9, pp. 77–115, Sep., 2022.

[5] J. Du, H. Wang, C. Jiang, J. Simonjan, J. Wang, and M. Debbah, “Distributed AI-based secure communications in space-air-ground-sea integrated networks,” IEEE Commun. Mag., vol. 63, no. 7, pp. 48–55, Jul. 2025.

[6] X. Zhang, M. Peng, and C. Liu, “Sensing-assisted beamforming and trajectory design for UAV-enabled networks,” IEEE Trans. Veh. Technol., vol. 73, no. 3, pp. 3804–3819, Mar., 2024.

[7] L. Zhu, W. Ma, and R. Zhang, “Movable antennas for wireless communication: Opportunities and challenges,” IEEE Commun. Mag., vol. 62, no. 6, pp. 114–120, Jun., 2024.

[8] L. Zhu et al., “A tutorial on movable antennas for wireless networks,” IEEE Commun. Surveys Tuts., early access, Feb., 27, 2025, doi: 10.1109/COMST.2025.3546373.

[9] Z. Li et al., “Movable antennas enabled ISAC systems: Fundamentals, opportunities, and future directions,” IEEE Wireless Commun., early access, Apr. 21, 2025, doi: 10.1109/MWC.002.2400522.

[10] L. Zhu, W. Ma, and R. Zhang, “Modeling and performance analysis for movable antenna enabled wireless communications,” IEEE Trans. Wireless Commun., vol. 23, no. 6, pp. 6234–6250, Jun., 2024.

[11] H. Zhang, J. Sun, X. Wang, and C. Gong, “Achieving physical layer security against location unknown eavesdroppers via friendly jammer,” IEEE/CAA J. Automatica Sinica, vol. 10, no. 10, pp. 2038–2040, Oct., 2023.

[12] Y. Zhang et al., “Robust secure UAV communications with the aid of jamming beamforming,” IEEE Trans. Commun., early access, May, 05, 2025, doi: 10.1109/TCOMM.2025.3566977.

[13] Y. Xiu, W. Lyu, P. L. Yeoh, Y. Ai, Y. Li, and N. Wei, “Improving physical-layer security in ISAC-AAV system: Beamforming and trajectory optimization,” IEEE Trans. Veh. Technol., vol. 74, no. 2, pp. 3503–3508, Feb., 2025.

[14] B. A. Tesfaw, R.-T. Juang, D. Saha, R. B. Tarekegn, H. -P. Lin, and L. -C. Tai, “Trajectory control and fair communications for multi-UAV networks: A federated multi-agent deep reinforcement learning approach,” IEEE Trans. Wireless Commun., vol. 24, no. 9, pp. 7598–7611, Sep. 2025.

[15] W. Ma, L. Zhu, and R. Zhang, “Mimo capacity characterization for movable antenna systems,” IEEE Trans. Wireless Commun., vol. 23, no. 4, pp. 3392–3407, Apr., 2024.

[16] X. Shao, R. Zhang, Q. Jiang, J. Park, T. Q. S. Quek, and R. Schober, “Distributed channel estimation and optimization for 6D movable antenna: Unveiling directional sparsity,” IEEE J. Sel. Topics Signal Process., vol. 19, no. 2, pp. 349–365, Mar., 2025.

[17] J. Tang, C. Pan, Y. Zhang, H. Ren, and K. Wang, “Secure MIMO communication relying on movable antennas,” IEEE Trans. Commun., vol. 73, no. 4, pp. 2159–2175, Apr., 2025.

[18] G. Hu, Q. Wu, K. Xu, J. Si, and N. Al-Dhahir, “Secure wireless communication via movable-antenna array,” IEEE Signal Process. Lett., vol. 31, pp. 516–520, 2024.

[19] K. Yu et al., “Movable antenna empowered PLS with Eve’s location uncertainty: Joint optimization of beamforming and antenna positions,” IEEE Trans. Commun., early access, Sep. 2025, doi: 10.1109/TCOMM.2025.3608337.

[20] K. Yu et al., “Does movable antenna present a dual-edged nature? From the perspective of physical layer security: A joint design of fixed-position antenna and movable antenna,” 2025, arXiv:2507.05784.

[21] W. Liu, X. Zhang, H. Xing, J. Ren, Y. Shen, and S. Cui, “UAV-enabled wireless networks with movable-antenna array: Flexible beamforming and trajectory design,” IEEE Wireless Commun. Lett., vol. 14, no. 3, pp. 566–570, Mar., 2025.

[22] R. Chai, B. Wang, R. Sun, X. Jing, and Q. Chen, “System cost function optimization-based data scheduling and flight trajectory for multi-antenna UAV-assisted communication and sensing integration systems,” IEEE Trans. Cogn. Commun. Netw., vol. 11, no. 4, pp. 2399–2410, Aug. 2025.

[23] C. Wang, Z. Li, X.-G. Xia, J. Shi, J. Si, and Y. Zou, “Physical layer security enhancement using artificial noise in cellular vehicle-to-everything (c-v2x) networks,” IEEE Trans. Veh. Technol., vol. 69, no. 12, pp. 15253–15268, Dec., 2020.

[24] K. Yu et al., “Surllc: Secure ultra-reliable and low latency communication in noma-UAV intelligent transportation systems,” IEEE Trans. Veh. Technol., vol. 74, no. 1, pp. 556–570, Jan., 2025.

[25] W. Wang et al., “Robust 3D-trajectory and time switching optimization for dual-UAV-enabled secure communications,” IEEE J. Sel. Areas Commun., vol. 39, no. 11, pp. 3334–3347, Nov., 2021.

[26] X. Sun, W. Yang, Y. Cai, and M. Wang, “Secure mmwave UAV-enabled swipt networks based on random frequency diverse arrays,” IEEE Internet Things J., vol. 8, no. 1, pp. 528–540, Jan., 2021.

[27] G. Hu et al., “Movable antennas-assisted secure transmission without eavesdroppers’ instantaneous CSI,” IEEE Trans. Mobile Comput., vol. 23, no. 12, pp. 14263–14279, Dec., 2024.

[28] Y. Zhao, Z. Feng, K. Yu, and D. Li, “An effective equivalence model of analyzing PLS of multiple eavesdroppers facing low-altitude communication systems,” IEEE Trans. Commun., 2025.

[29] Q. Yuan, Y. Hu, C. Wang, and Y. Li, “Joint 3D beamforming and trajectory design for UAV-enabled mobile relaying system,” IEEE Access, vol. 7, pp. 26488–26496, 2019.

[30] P. Yan et al., “Securing UAV-aided noma wireless powered communications via artificial noise,” IEEE Trans. Wireless Commun., vol. 24, no. 6, pp. 4809–4823, Jun., 2025, doi: 10.1109/TWC.2025.3544300.

[31] J. Chu, R. Liu, M. Li, Y. Liu, and Q. Liu, “Joint secure transmit beamforming designs for integrated sensing and communication systems,” IEEE Trans. Veh. Technol., vol. 72, no. 4, pp. 4778–4791, Apr., 2023.

[32] X. Chen, B. Feng, Y. Wu, D. W. Kwan Ng, and R. Schober, “Joint beamforming and antenna movement design for moveable antenna systems based on statistical CSI,” in Proc. IEEE Glob. Commun. Conf., 2023, pp. 4387–4392.

[33] 3rd Generation Partnership Project (3GPP), “Study on channel model for frequencies from 0.5 to 100 GHz,” 3GPP, Sophia Antipolis, France, Tech. Specification 38.901, 2018.

[34] 3rd Generation Partnership Project (3GPP), “Study on new radio (nr) to support non-terrestrial networks,” 3GPP, Sophia Antipolis, France, Tech. Specification 38.811, v. 15.4.0, Oct. 2018.

[35] M. <sup>˙</sup>Ilgüy, B. Özbek, R. Mumtaz, S. A. Busari, and J. Gonzalez, “Coverage analysis of physical layer network coding in massive mimo systems,” IEEE Trans. Veh. Technol., vol. 70, no. 2, pp. 1480–1487, Feb., 2021.

[36] Y. Wang, G. Hu, X. Hu, X. Lu, and Y. Huang, “Movable antenna array aided ultra reliable covert communications,” 2024, arXiv:2412.20417.

[37] M. A. Moskowitz, A Course in Complex Analysis in One Variable. Singapore: World Sci. Publishing Co., 2002.

[38] K. E. Kolodziej, A. U. Cookson, and B. T. Perry, “Adaptive learning rate tuning algorithm for RF self-interference cancellation,” IEEE Trans. Microw. Theory Techn., vol. 69, no. 3, pp. 1740–1751, Mar., 2021.

[39] J. Lu, F. Liu, J. Sun, Q. Liu, and Y. Miao, “Joint estimation of target parameters and system deviations in MIMO radar with widely separated antennas on moving platforms,” IEEE Trans. Aerosp. Electron. Syst., vol. 57, no. 5, pp. 3015–3028, Oct., 2021.

[40] Z. Cheng, C. Ouyang, and X. Zhang, “Movable antenna aided physical layer security with no eavesdropper CSI,” in Proc. IEEE Int. Conf. Acoust., Speech Signal Process., 2025, doi: 10.1109/ICASSP49660.2025.10887653.

[41] L. T. Nguyen, J. Kim, and B. Shim, “Gradual federated learning with simulated annealing,” IEEE Trans. Signal Process., vol. 69, pp. 6299–6313, 2021.

[42] Z. He, W. Xu, H. Shen, D. W. K. Ng, Y. C. Eldar, and X. You, “Full-duplex communication for ISAC: Joint beamforming and power optimization,” IEEE J. Sel. Areas Commun., vol. 41, no. 9, pp. 2920–2936, Sep., 2023.

[43] Z. Sun, D. Yang, L. Xiao, L. Cuthbert, F. Wu, and Y. Zhu, “Joint energy and trajectory optimization for UAV-enabled relaying network with multi-pair users,” IEEE Trans. Cogn. Commun. Netw., vol. 7, no. 3, pp. 939–954, Sep., 2021.

[44] H. Wang, J. Wang, G. Ding, J. Chen, and J. Yang, “Completion time minimization for turning angle-constrained UAV-to-UAV communications,” IEEE Trans. Veh. Technol., vol. 69, no. 4, pp. 4569–4574, Apr., 2020.

[45] G. Hu et al., “Movable antennas-enabled two-user multicasting: Do we really need alternating optimization for minimum rate maximization?,” IEEE Trans. Veh. Technol., vol. 74, no. 3, pp. 5135–5140, Mar. 2025.

[46] E. N. Tominaga, O. L. A. López, T. Svensson, R. D. Souza, and H. Alves, “On the spectral efficiency of indoor wireless networks with a rotary uniform linear array,” in Proc. IEEE Wireless Commun. Netw. Conf., 2025, doi: 10.1109/WCNC61545.2025.10978615.

[47] S. Zuo, W. Jing, Z. Lu, X. Wen, and C. Liu, “Movable antenna-aided interference mitigation for LEO-GEO spectrum-sharing system,” in Proc. IEEE Wireless Commun. Netw. Conf., 2025, doi: 10.1109/WCNC61545.2025.10978720.

![](images/6bb42e5a771d61b55120c1d4fca7eb9154c8a1d4b1e6d8f929d3cee5afce0d8c.jpg)  
Kaixuan Li received the bachelor’s degree in network engineering in 2023 from Qufu Normal University, Jining, China, where she is currently working toward the master’s degree with the School of Computer Science. Her current research interests include physical layer security, integrated sensing and communications, and movable antennas.

Kan Yu (Member, IEEE) received the MS degree from the School of Information Science and Engineering, Qufu Normal University, in 2016, and the PhD degree from the College of Computer Science and Engineering, Shandong University of Science and Technology, in 2019. He is currently a tenuretrack assistant professor with the Key Laboratory of Universal Wireless Communications, Ministry of Education, Beijing University of Posts and Telecommunications, Beijing, China. His research interests include wireless network security, movable antenna

![](images/a961e1567a706d87316d66f4b65d264e8c6f3e076fc5d9cfc594af6ea422ae8e.jpg)

![](images/24bcd98331cb9423b79b9b4ed2859b3b8416c249b880b5a085c6b73ca43e076e.jpg)

and resource allocation. He was the recipient of the title of Macao Young Scholar in 2023, Best Paper Award of MICCIS 2024, and Distinguished Paper Award of IEEE GreenCom 2023. Dr. Yu is a member of China Computer Federation (CCF).

![](images/0977df0a3138d357755b199a013f5076a8eefa16cbb2fc41a3ae417600c6c744.jpg)

Dingyou Ma (Member, IEEE) received the BSc degree in aerospace science and technology from Xidian University, Xi’an, China, in 2016, and the PhD degree in electronics engineering from Tsinghua University, Beijing, China, in 2022. Since 2022, he has been with the Key Laboratory of Universal Wireless Communications, Ministry of Education, School of Information and Communication Engineering, Beijing University of Posts and Telecommunications, as a lecturer. His current research interests include communications signal processing, radar signal processing, and dual-

Yujia Zhao received the bachelor’s degree from Capital Normal University, Beijing, China, in 2023. He is currently working toward the PhD degree in information and communication engineering with the Beijing University of Posts and Telecommunications, Beijing, China. His research interests include wireless physical layer security, movable antenna, integrated sensing and communication, and low-altitude UAV detection.

![](images/e00c47ab197ee8d89d156bd9062686be17ec53d3882d219a46de2e1ce18c2d3a.jpg)  
function radar-communications system.

Xiaowu Liu received the PhD degree in computer science from Harbin Engineering University, Harbin, China, in 2009. He is currently a professor with the School of Computer Science, Qufu Normal University, Rizhao, China. His research interests include distributed computing, wireless networks, network security, privacy preserving, and Internet of Things.

![](images/bd6a8910b0ae339ebc6f0b2d2c38d080243aab90069c08ebdd7ecf3cc483f0bb.jpg)

Qixun Zhang (Member, IEEE) received the BE and PhD degrees from the Beijing University of Posts and Telecommunications (BUPT), Beijing, China, in 2006 and 2011, respectively. From Mar. 2006 to Jun. 2006, he was a visiting scholar with the University of Maryland, College Park, MD, USA. From 2018 to 2019, he was a visiting scholar with the University of Houston, TX, USA. He is currently a professor with BUPT. His research interests include 5G mobile networks, integrated sensing and communication (ISAC) for autonomous driving vehicles, mmWave communication system, and unmanned aerial vehicles communication. He is active in ITU-R WP5A/5C/5D standards.

![](images/6a7ba177188fdd043fe63ab60a55a7ac8a691669cfe59d7abd79d4690c3a5a4f.jpg)

Zhiyong Feng (Senior Member, IEEE) received the BS, MS, and PhD degrees from the Beijing University of Posts and Telecommunications (BUPT), Beijing, China, in 1993, 1997, and 2009, respectively. She is currently a professor with BUPT and director with the Key Laboratory of Universal Wireless Communications, Ministry of Education, China. Her research interests include 5G mobile networks, integrated sensing and communication (ISAC) system design, wireless network architecture design, cognitive wireless networks, universal signal detection and identification, and network information theory. She is active in ITU-R WP5A/5C/5D, IEEE 1900, ETSI, and CCSA standards.