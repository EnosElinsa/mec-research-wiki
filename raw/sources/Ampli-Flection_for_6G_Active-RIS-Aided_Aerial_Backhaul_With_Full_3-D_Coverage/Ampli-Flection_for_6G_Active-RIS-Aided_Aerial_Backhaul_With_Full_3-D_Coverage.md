# Ampli-Flection for 6G: Active-RIS-Aided Aerial Backhaul With Full 3-D Coverage

Hong-Bae Jeon , Member, IEEE, and Chan-Byoung Chae , Fellow, IEEE

Abstract—In this paper, we propose a novel aerial backhaul architecture that employs an aerial active reconfigurable intelligent surface (RIS) to achieve energy-efficient, full 3D coverage including UAV-BSs and ground users in 6G wireless networks. Unlike prior aerial-RIS approaches limited to 2D coverage with only servicing ground users or passive operation, the proposed design integrates an active-RIS onto a high-altitude aerial platform, enabling reliable line-of-sight links and overcoming multiplicative fading through amplification. In a scenario with UAV-BSs deployed to handle sudden traffic surges in urban areas, the aerial-active-RIS both reflects and amplifies backhaul signals to overcome blockage. We jointly optimize the aerial platform placement, array partitioning, and RIS phase configuration to maximize UAV-BS energy-efficiency. Simulation results confirm that the proposed method significantly outperforms benchmarks, demonstrating its strong potential to deliver resilient backhaul connectivity with comprehensive 3D coverage in 6G networks.

Index Terms—Active reconfigurable intelligent surface, uncrewed aerial vehicle, wireless backhaul, non-convex optimization, energy-efficiency.

## I. INTRODUCTION

O <sup>F</sup> <sup>LATE,</sup> <sup>the</sup> <sup>rapid</sup> <sup>expansion</sup> <sup>of</sup> <sup>data-driven</sup> <sup>applica-</sup>tions with the push for extended wireless coverage tions with the push for extended wireless coverage in beyond fifth-generation (B5G) and sixth-generation (6G) networks have driven an unprecedented demand for providing ultra-reliable and high-capacity communications anywhere [2], [3], [4]. In response, researchers have been exploring the deployment of aerial base stations, realized through uncrewedaerial-vehicle-base-stations (UAV-BSs), for rapid and flexible coverage extensions [5], [6]. These UAV-BSs present a compelling solution for extending network coverage to areas where conventional base station infrastructure is inadequate, offering rapid deployment capabilities in emergency or high-traffic scenarios. Their high-altitude operation further enhances the likelihood of rich line-of-sight (LoS) links [7], [8], thereby improving communication reliability and efficiency. To enable efficient UAV-BS deployment, prior studies have investigated deployment strategy design [9], [10], trajectory optimization [11], [12], and power control schemes [13], [14]. One of the critical challenges that remains for deploying UAV-BSs is the backhaul connectivity, particularly in dense urban areas where obstacles obstruct direct backhaul links from terrestrial sources and generates non-LoS (NLoS) components, which severely deteriorates the system’s energy-efficiency, posing a critical challenge for 6G wireless networks operating with higher spectrum [15], [16], [17].

Therefore, the reconfigurable intelligent surface (RIS) has been explored as a means to enhance wireless coverage and mitigate blockages [18], [19], [20], [21]. RIS is an artificial metasurface composed of passive reflecting elements capable of adjusting both the amplitude and phase of an incident signal [22], [23]. Furthermore, due to its passive array architecture, the RIS exhibits high channel capacity with low power consumption, which leads to the energy-efficiency compared to conventional decode-and-forward or amplify-andforward (DF/AF) relays in several scenarios [24], [25], [26]. However, conventional RIS has passive reflection elements, which highly suffer from severe “multiplicative fading,” where the path loss is given by the multiplication of Tx-to-RIS and RIS-to-Rx links, limiting their effectiveness in practical scenarios [27], [28]. These disadvantages become more severe when the RIS is deployed in terrestrial infrastructure on dense urban areas.

To overcome the fundamental physical limitation imposed by the multiplicative fading effect of cascaded channels in RIS-assisted systems, the concept of active-RIS has recently been proposed [27], [29]. Unlike conventional passive-RISs, which only reflect incident signals without amplification, active-RISs incorporate reflection-type amplifiers within each element, thereby enabling signal amplification at the cost of additional power consumption [30]. This capability fundamentally changes the power-rate trade-off and opens up new possibilities for performance enhancement in future 6G wireless networks.

Early studies, such as [27], focused on characterizing the performance gains of active-RIS over passive-RIS through sum-rate maximization and comparative analyses, demonstrating that active-RIS can effectively mitigate the double-fading loss inherent in passive architectures. These works established the potential of active-RIS as a promising technology for next-generation systems. Building upon this foundation, subsequent research addressed practical implementation challenges. In particular, [31] investigated a sub-connected active-RIS architecture and proposed a joint beamforming design that balances hardware complexity and performance, revealing important trade-offs between achievable gains and circuitlevel constraints. From a performance perspective, [28], [32] further examined the SNR advantages of active-RIS under a unified power budget, showing that, when properly optimized, active-RIS can significantly outperform passive-RIS counterparts. More recently after performance characterization and architectural investigations, attention has shifted toward robustness and practical deployability. To bridge the gap between theoretical analysis and real-world operation, [33], [34] studied active-RIS transmission designs under partial channel state information (CSI). Specifically, [33] aimed at maximizing the average sum-rate, while [34] focused on minimizing the average total transmit power subject to rate and outage probability constraints. These works highlight the importance of accounting for CSI uncertainty when designing active-RIS-assisted systems.

Most prior work, however, has primarily focused on deploying the active-RIS in terrestrial environments, such as those involving buildings and walls. These environments impose several limitations on communication performance. In dense urban areas with many buildings, reliable transmission often depends on multiple reflections, which requires deploying a large number of RIS units to alleviate severe signal attenuation. Moreover, a terrestrial RIS can only reflect signals from the source to destinations located on the same side, thereby restricting the angular range of reflection and preventing isotropic coverage over $0 ^ { \circ } \ \sim \ 3 6 0 ^ { \circ }$ arrival angles. Several studies have investigated the deployment of RIS on aerial platforms (e.g., [35], [36], [37]); however, most of these works focus on conventional passive RIS architectures and consider only 2D coverage, or assume fixed transmit power at the source, thereby largely overlooking energy-efficiency considerations. Although a few recent studies have explored active-RIS-assisted aerial systems [38], [39], [40], they still restrict their scope to 2D coverage scenarios,<sup>1</sup> which limits their applicability in dense urban 6G environments with heterogeneous mobility and altitude-dependent service demands.

In contrast, this paper proposes a novel aerial active-RIS architecture that explicitly distinguishes the geometric benefits of aerial deployment from the amplification-enabled gains introduced by the active-RIS itself. While the elevated platform inherently improves LoS availability and alleviates blockage through favorable 3D geometry, the active-RIS provides an additional and fundamentally different advantage by amplifying the reflected signals at the element level. This amplification capability mitigates the multiplicative pathloss of cascaded source-RIS-destination links, which is an important issue due to the long link distance of aerial platform and cannot be achieved by aerial placement or passive RIS alone under the same power budget [41]. As a result, the proposed architecture enables energy-efficient 3D coverage and, for the first time, facilitates an aerial-active-RIS-assisted backhaul network capable of reliably supporting UAV-BSs and heterogeneous users in future 6G wireless networks.

The key contributions are summarized as follows:

1) We propose a novel aerial-active-RIS architecture aimed at enhancing 3D backhaul connectivity to UAV-BSs in urban environments characterized by severe blockages. The proposed scheme deploys an RIS on a high-altitude platform, where each RIS element is equipped with an active amplifier, ensuring both a rich LoS component and robustness against multiplicative fading, respectively. To maximize the received SNR and minimize the transmit power, we show that the maximum-ratio transmission (MRT) strategy achieves the purpose.

2) We verify that equal amplification gain across active-RIS elements is a feasible approach for optimizing the energy-efficiency by minimizing the total consumed power of the system. Under this assumption, an optimization framework is developed to determine the placement, array-partitioning strategy, phase control and optimal amplification gain of the aerial-active-RIS with the objective of maximizing energy-efficiency. Specifically, a nonzero closed-form value of the source transmit power for each UAV-BS is derived, and a minimization problem is formulated by adjusting the numerator and denominator of the value. The problem is efficiently solved using the global criterion method, which selects a minimal-total-distance operating point corresponding to a Pareto-efficient solution, and considering the partition of full RIS array, respectively.

3) The proposed approach is evaluated numerically in a realistic urban outdoor environment with $1 0 ^ { 3 }$ randomly distributed ground users and corresponding UAV-BSs. Extensive numerical results demonstrate that the proposed aerial-active-RIS scheme significantly outperforms conventional benchmarks including the aerial-AF-relay and the aerial-passive-RIS schemes and aerial-active-RIS with randomly determined amplification gain in terms of energy-efficiency.

## II. SYSTEM MODEL

## A. Aerial Backhaul With Conventional Passive-RIS

We consider an urban area $\mathcal { G }$ with origin $\pmb { \rho } _ { \mathcal { G } }$ on xy-plane, as depicted in Fig. 1(a). We assume that $\mathcal { G }$ contains $N _ { 0 }$ ground users equipped with omnidirectional antenna, and served by multiple stationary UAV-BSs with a directional antenna, represented as $\mathbb { M } = \{ 1 , \cdots , M _ { 0 } \}$ . The directional antenna of each UAV-BS has different azimuth and elevation half-power beamwidths (HPBW) [42]. The 3D coordinates of a UAV-BS m are expressed as $\pmb { \rho } _ { m } \triangleq \left[ \mathbf { w } _ { m } ^ { \mathrm { T } } h _ { m } \right] ^ { \mathrm { T } }$ , with its 2D coordinate $\mathbf { w } _ { m }$ and altitude $h _ { m }$

To alleviate interference among adjacent cells, we assume that each UAV-BS serves a distinct, non-overlapping subset of users. In this context, the Ellipse Clustering algorithm [8] is employed to allocate ground users and determine $M _ { 0 } ,$ while significantly reducing the transmit power through optimized

![](images/9385c8c81d39fb395494f2808ead74cdf0fa75f015c0c778aee484d2559a361e.jpg)  
Fig. 1. (a) UAV-BS access network supported by an aerial-active-RIS backhaul and (b) signal model illustration of the aerial-active-RIS.

3D deployment.<sup>2</sup> Under this setup, the throughput $C _ { m }$ of UAV-BS m is expressed as

$$
C _ { m } = \sum _ { n \in \mathbb { U } _ { m } } \frac { B _ { \mathrm { f } } } { \left. \mathbb { U } _ { m } \right. } \log _ { 2 } \left( 1 + \frac { P _ { \mathrm { f } , n } } { \sigma _ { \mathrm { f } } ^ { 2 } } \right) ,\tag{1}
$$

where $\mathbb { U } _ { m }$ represents the user set served by UAV-BS $m ,$ $B _ { \mathrm { f } }$ denotes the fronthaul bandwidth, which is evenly divided among the $\left| \mathbb { U } _ { m } \right|$ users in $\mathbb { U } _ { m } , \ P _ { \mathrm { f } , n }$ is the received power at user $n \in \mathbb { U } _ { m }$ , and $\sigma _ { \mathrm { f } , m } ^ { 2 }$ represents the noise power of the fronthaul link for UAV-BS m. By adopting the frequency-division-multiple-access $( \mathrm { F D M A } ) ^ { 3 }$ within each cell and non-overlapping UAV-BS coverage regions, both intraand inter-cell interference are eliminated, and the achievable rate in (1) directly follows.

For an aerial-active-RIS which maintains an altitude H, and designating the first element as the reference, the 3D coordinates of the aerial-RIS are expressed as ${ \pmb \rho } _ { \mathrm { R I S } } \triangleq \left[ { \bf q } ^ { \mathrm { T } } \ H \right] ^ { \mathrm { T } }$ . We consider a source at origin, which is equipped with a uniform linear array (ULA) comprising M antennas with inter-element spacing $d _ { \mathrm { s } }$ and an antenna gain of $G _ { \mathrm { s } }$ . Note that although the source and, as will be discussed later, the aerial-active-RIS employ ULAs, the considered coverage is inherently “threedimensional”, as the RIS and UAV-BS location, propagation distance, and elevation angle are explicitly characterized in a 3D coordinate system [45], [46], [47]. In particular, H and $\left\{ h _ { m } \right\}$ induce elevation-dependent path loss and phase variations, which are fully captured in the channel model.

The distance between the source and the center of the coverage area is denoted by $d _ { \mathcal { G } } \triangleq | | \pmb { \rho } _ { \mathcal { G } } | | _ { 2 }$ , and is assumed to be sufficiently large and the direct transmission path from the source to the UAV-BS is blocked. The aerial-RIS is modeled as a $\mathrm { { U L A } ^ { 4 } }$ comprising N reflecting elements with inter-element spacing $d _ { \mathrm { R I S } } ,$ and carrier wavelength λ. We assumed an uncoupled model for the RIS elements under this ULA-spacing configuration [50], [51], [52]. Without loss of generality, the RIS is assumed to be aligned parallel to the x-axis.

![](images/1c968f3c24da2afb76efc202610e54c61af142ff8d20e3716929a6b5357ee58a.jpg)  
Fig. 2. Illustration of passive beamforming gain g and the full/sub-array structure: (a) The main lobe characteristics obtained under a general unequal gain configuration $\{ \alpha _ { n } \} _ { n = 1 } ^ { N }$ are nearly identical to those under the equal-gain case $\alpha _ { n } = \alpha \ ( \forall n )$ . (b) When the sin-AoD deviation lies beyond the HPBW of the full-array beamforming pattern, a sub-array structure is employed to accommodate the deviated point.

Due to the elevated altitude of the aerial-RIS, the backhaul link is assumed to be dominated by an LoS component. Considering that d is significantly smaller than both H and $d _ { \mathcal { G } }$ , the backhaul link is approximated using a uniform planewave model, implying that the path loss is assumed to be identical across all RIS-element pairs. Accordingly, the path loss associated with the source-to-RIS link, $\beta _ { \mathrm { s } } \left( \mathbf { q } \right)$ , and the RIS-to-UAV-BS link, $\beta \left( \mathbf { q } , \pmb { \rho } _ { m } \right)$ , are formulated as [53]:

$$
\beta _ { \mathrm { s } } \left( \mathbf { q } \right) = \beta _ { 0 } { \left| \left| \rho _ { \mathrm { R I S } } \right| \right| } _ { 2 } ^ { - 2 } , \ \beta \left( \mathbf { q } , \pmb { \rho } _ { m } \right) = \beta _ { 0 } { \left| \left| \rho _ { \mathrm { R I S } } - \pmb { \rho } _ { m } \right| \right| } _ { 2 } ^ { - 2 } ,\tag{2}
$$

where $\beta _ { 0 }$ represents the reference path loss at a 1 m distance. Therefore, the channel for the source-to-RIS link,

H $\mathbf { \Psi } ( \mathbf { q } ) \in \mathbb { C } ^ { N \times M }$ , and the RIS-to-destination link, $\mathbf { h } ^ { \ast } \left( \mathbf { q } , \cdot \right) \in$ $\mathbb { C } ^ { 1 \times \bar { N } }$ , are expressed as:

$$
\left\{ \begin{array} { l l } { \mathbf { H } \left( \mathbf { q } \right) } \\ { = \sqrt { \beta _ { \mathrm { s } } \left( \mathbf { q } \right) } e ^ { j \left( \Phi _ { \mathrm { H } } - \frac { 2 \pi \left| \left| \rho _ { \mathrm { R I S } } \right| \right| _ { 2 } } { \lambda } \right) } \mathbf { a } _ { \mathrm { R I S } } \left( \phi _ { \mathrm { r } , \mathrm { R I S } } \left( \mathbf { q } \right) \right) \mathbf { a } _ { \mathrm { s } } ^ { \ast } \left( \phi _ { \mathrm { t , s } } \left( \mathbf { q } \right) \right) } \\ { \mathbf { h } ^ { \ast } \left( \mathbf { q } , \pmb { \rho } _ { m } \right) } \\ { = \sqrt { \beta \left( \mathbf { q } , \pmb { \rho } _ { m } \right) } e ^ { j \left( \Phi _ { \mathrm { h } } - \frac { 2 \pi \left| \left| \rho _ { \mathrm { R I S } } - \pmb { \rho } _ { m } \right| \right| _ { 2 } } { \lambda } \right) } \mathbf { a } _ { \mathrm { R I S } } ^ { \ast } \left( \phi _ { \mathrm { t , R I S } } \left( \mathbf { q } , \pmb { \rho } _ { m } \right) \right) , } \end{array} \right.\tag{3}
$$

where $\Phi _ { \mathbf { H } }$ and $\Phi _ { \mathbf { h } }$ are independent and uniformly-distributed random phases within [0, 2π). Therein, the array response $\mathbf { a } _ { \mathrm { s } } \left( \cdot \right)$ and $\mathbf { a } _ { \mathrm { R I S } } \left( \cdot \right) \mathbf { \Psi } \in \mathbf { \Psi } \mathbb { C } ^ { N }$ of the source and aerial-RIS, respectively, are given by:

$$
\begin{array} { r } { \{ \mathbf { a } _ { \mathrm { s } } ( \cdot ) = [ \{ e ^ { - j 2 \pi ( m - 1 ) \bar { d } _ { \mathrm { s } } ( \sin ( \cdot ) ) } \} _ { m = 0 } ^ { M - 1 } ] ^ { \mathrm { T } } \phantom { , } } \\ { \mathbf { a } _ { \mathrm { R I S } } ( \cdot ) = [ \{ e ^ { - j 2 \pi ( n - 1 ) \bar { d } ( \sin ( \cdot ) ) } \} _ { n = 0 } ^ { N - 1 } ] ^ { \mathrm { T } } , } \end{array}\tag{4}
$$

where $\bar { d } _ { \mathrm { s } } \ \triangleq \ \frac { d _ { \mathrm { s } } } { \lambda }$ and $\bar { d } \triangleq \frac { d _ { \mathrm { R I S } } } { \lambda }$ . Lastly, $\phi _ { \mathrm { t , s } } ( \mathbf { q } ) , \phi _ { \mathrm { t , R I S } } ( \mathbf { q } , \cdot )$ and $\phi _ { \mathrm { r , R I S } } \left( \mathbf { q } \right)$ denote the angle-of-departure (AoD) of the source-RIS and RIS-destination links and the angle-of-arrival (AoA) of the source-RIS link, respectively. For analytical tractability, it is assumed that the ground source has knowledge of channels, which can be obtained using methods outlined in [54], [55], [56], and [57].

## B. Implementation of Active-RIS

Since conventional RIS consists of passive elements which cannot amplify the signal, the reflected signal has to suffer from “multiplicative fading” induced by the multiplication of the path loss of source-to-RIS and RIS-to-UAV-BS links [27], which is presented by $| | \pmb { \rho } _ { \mathrm { R I S } } ^ { * } - \pmb { \rho } _ { m } | | _ { 2 } ^ { 2 } \left| \left| \pmb { \rho } _ { \mathrm { R I S } } ^ { * } \right| \right| _ { 2 } ^ { 2 }$ in (14), shown at the bottom of the next page. Recently, by accompanying the active-RIS [28], [31], [32], [58], we can solve the aforementioned “multiplicative fading” problem by compensating signal power at the active-RIS component.

We assume that, as illustrated in Fig. 1(b), the active amplification circuit with amplification factor $\{ \alpha _ { n } \} _ { n = 1 } ^ { N }$ and the element-wise hardware power consumption $P _ { \mathrm { { E } } }$ is implemented into the N -element aerial-RIS. In other words, after supplying the hardware power consumption for N active elements, we can generate feasible amplification gain by remaining power for a given power budget [27], [32]. The reflected and amplified signal $\mathbf { y } _ { \mathrm { r a } }$ for incident signal $\mathbf { x } _ { \mathrm { r a } }$ is modeled by [27]:

$$
\mathrm { \bf y } _ { \mathrm { r a } } = \underbrace { { \bf A } \Theta { \bf x } _ { \mathrm { r a } } } _ { \mathrm { D e s i r e d ~ s i g n a l } } + \underbrace { { \bf A } \Theta { { \bf n } _ { \mathrm { a } } } } _ { \mathrm { D y n a m i c ~ n o i s e } } .\tag{5}
$$

Here, $\mathbf { A } \triangleq$ diag $\left( \left\{ \alpha _ { n } \right\} _ { n = 1 } ^ { N } \right)$ is the amplification matrix of the active-RIS, wherein we assume $1 < \alpha _ { n } \le \alpha _ { \mathrm { m a x } }$ (∀n) [59]. Moreover, Θ <sup>,</sup> diag $\left( \left\{ e ^ { j \theta _ { n } } \right\} _ { n = 1 } ^ { N } \right) \in \mathbb { C } ^ { N \times N }$ is a phase shift matrix with phase shift $\theta _ { n } \in [ 0 , \mathring { 2 } \pi )$ of the nth element, and $\mathbf { n } _ { \mathrm { a } } \sim \mathcal { C N } \left( \mathbf { 0 } _ { N } , \sigma _ { \mathrm { a } } ^ { 2 } \mathbf { I } _ { N } \right)$ is the dynamic noise induced by the amplification of the active-RIS elements [27], [31].

By definition, ${ \bf x } _ { \mathrm { r a } }$ is given by $\mathbf { x } _ { \mathrm { r a } } = \mathbf { H } \left( \mathbf { q } \right) \mathbf { x } .$ , where x is the total transmit signal. We can represent x as a sum of unitmagnitude precoding vectors $ { \mathbf { v } } _ { m } \in \mathbb { C } ^ { M }$ , each corresponding to a unit-power signal $s _ { m }$ intended for UAV-BS m, with transmit power $P _ { m }$ at the source. Therefore, x is:

$$
\mathbf { x } = \sum _ { m \in \mathbb { M } } \mathbf { v } _ { m } \sqrt { P _ { m } G _ { \mathrm { s } } } s _ { m } ,\tag{6}
$$

which implies that the source transmit power $P _ { \mathrm { t o t , s } }$ is:

$$
P _ { \mathrm { t o t , s } } = \mathcal { E } \left[ \left| \left| \mathbf { x } \right| \right| ^ { 2 } \right] = \mathrm { t r } \left( G _ { \mathrm { s } } \mathbf { P } \mathbf { V } ^ { * } \mathbf { V } \right) = G _ { \mathrm { s } } \sum _ { m \in \mathbb { M } } P _ { m } .\tag{7}
$$

By (5), the reflection power of active-RIS is given by [26]

$$
P _ { \mathrm { R } } = \mathcal { E } \left[ | | \mathbf { A } \mathbf { \Theta } ( \mathbf { x } _ { \mathrm { r a } } + \mathbf { n } _ { \mathrm { a } } ) | | _ { 2 } ^ { 2 } \right] = \mathcal { E } [ | | \mathbf { A } \mathbf { H } ( \mathbf { q } ) \mathbf { x } | | _ { 2 } ^ { 2 } ] + \sigma _ { \mathrm { a } } ^ { 2 } \sum _ { n = 1 } ^ { N } \alpha _ { n } ^ { 2 } ,\tag{8}
$$

and the power consumed by the active hardware components is expressed as $N P _ { \mathrm { E } } \triangleq N (  { \dot { P } _ { \mathrm { D C } } } + P _ { \mathrm { S W } } )$ [28], where $P _ { \mathrm { { E } } }$ denotes the per-element hardware power consumption comprising the control and phase-shift switching power $P _ { \mathrm { S W } }$ and the direct current (DC) biasing power $P _ { \mathrm { D C } }$ required for the amplifier in each active-RIS element [17]. Consequently, the total power consumption of the active-RIS is given by

$$
P _ { \mathrm { t o t , a } } = P _ { \mathrm { R } } + N P _ { \mathrm { E } } ,\tag{9}
$$

where we assume that the efficiency of the power amplifier is 1 in both source and aerial-active-RIS.

Moreover, $\mathbf { y } _ { \mathrm { r a } }$ faces the channel $\mathbf { h } ^ { * } \left( \mathbf { q } , \pmb { \rho } _ { m } \right)$ from RISdestination. Hence, by concatenating the effects, the signal model from source-to-RIS-to-UAV-BS-m is given by [26]

$$
y _ { m } = \mathbf { h } ^ { * } \left( \mathbf { q } , \rho _ { m } \right) \mathbf { A } \varTheta \mathbf { H } \left( \mathbf { q } \right) \mathbf { x } + \mathbf { h } ^ { * } \left( \mathbf { q } , \rho _ { m } \right) \mathbf { A } \varTheta \mathbf { n } _ { \mathbf { a } } + n ,\tag{10}
$$

where $n \sim \mathcal { C N } ( 0 , \sigma ^ { 2 } )$ is the noise at the receiver. By (10), the backhaul rate of UAV-BS m is given by [26]

$$
R _ { m } = \frac { B _ { \mathrm { b } } } { M _ { 0 } } \log _ { 2 } ( 1 + \underbrace { \frac { P _ { m } G _ { \mathrm { s } } | \mathbf { h } ^ { * } ( \mathbf { q } , \rho _ { m } ) \mathbf { A } \Theta \mathbf { H } ( \mathbf { q } ) \mathbf { v } _ { m } | ^ { 2 } } { \sigma _ { \mathrm { a } } ^ { 2 } | | \mathbf { A } \Theta ^ { * } \mathbf { h } ( \mathbf { q } , \rho _ { m } ) | | ^ { 2 } + \sigma ^ { 2 }  } } _ { \triangleq \gamma _ { m } } ) ,\tag{11}
$$

where $B _ { \mathrm { b } }$ denotes the backhaul bandwidth, which is equally partitioned into $M _ { 0 }$ sub-bands assigned to each UAV-BS, and $\gamma _ { m }$ is the received SNR of UAV-BS m. Here, we can notice the definition of $\gamma _ { m }$ that the signal is amplified by $\left\{ \alpha _ { n } \right\}$ and the denominator is extended with the power of the dynamic noise signal $\mathbf { h } ^ { * } \left( \mathbf { q } , \pmb { \rho } _ { m } \right) \mathbf { A } \Theta \mathbf { n } _ { \mathbf { a } }$ . Moreover, since $\mathbf { h } ^ { * } \left( \mathbf { q } , \pmb { \rho } _ { m } \right)$ contains $\begin{array} { r } { \beta \left( \mathbf { q } , \pmb { \rho } _ { m } \right) \triangleq \frac { \beta _ { 0 } } { | | \pmb { \rho } _ { \mathrm { R I S } } - \pmb { \rho } _ { m } | | _ { 2 } ^ { 2 } } } \end{array}$ , the effect of the dynamic noise gets weaker when the RIS-to-UAV-BS distance gets larger.

To enhance energy-efficiency by minimizing the source transmit power, i.e., $\textstyle \sum _ { m \in \mathbb { M } } { \dot { P } } _ { m }$ [8], [45], which will be clarified in (27), we first derive the precoding vector ${ \bf v } _ { m }$ for UAV-BS m that maximizes $\gamma _ { m }$ under a given $P _ { m }$ . This approach enables a reduction in transmit power while maintaining the required data rate, and is formulated by MRT:

$$
\mathbf { v } _ { m } = \frac { \mathbf { a } _ { \mathrm { s } } \left( \phi _ { \mathrm { t , s } } \left( \mathbf { q } \right) \right) } { \sqrt { M } } \left( \forall m \in \mathbb { M } \right) ,\tag{12}
$$

which implies that the optimal transmission strategy $\{ \mathbf { v } _ { m } \} _ { m \in \mathbb { M } }$ is given to maximize the inner-product with $\mathbf { a } _ { \mathrm { s } } ^ { * } \left( \phi _ { \mathrm { t , s } } \left( \mathbf { q } \right) \right)$ ) [45]. Moreover, in (11) it is clear that

$$
| | \mathbf { A } \boldsymbol { \Theta } ^ { * } \mathbf { h } \left( \mathbf { q } , \pmb { \rho } _ { m } \right) | | _ { 2 } ^ { 2 } = | | \mathbf { A } \mathbf { h } \left( \mathbf { q } , \pmb { \rho } _ { m } \right) | | _ { 2 } ^ { 2 } = \beta \left( \mathbf { q } , \pmb { \rho } _ { m } \right) \sum _ { n = 1 } ^ { N } \alpha _ { n } ^ { 2 } ,\tag{13}
$$

where the first equality comes from the fact that $\Theta \triangleq$ diag $\left( \left\{ e ^ { j \theta _ { n } } \right\} _ { n = 1 } ^ { N } \right)$ is unitary. By applying MRT and (13), $\gamma _ { m }$ becomes (14) where $\begin{array} { r } { \bar { \gamma } \triangleq \frac { P _ { m } G _ { \mathrm { s } } \beta _ { 0 } ^ { 2 } M } { \sigma _ { \mathrm { a } } ^ { 2 } \beta ( \mathbf { q } , \pmb { \rho } _ { m } ) \sum _ { n = 1 } ^ { N } \alpha _ { n } ^ { 2 } + \sigma ^ { 2 } } } \end{array}$ [45].

For $\{ \theta _ { n } ^ { * } \} _ { n = 1 } ^ { N }$ to maximize $\gamma _ { m }$ for a given $P _ { m }$ , they must be configured to ensure that the reflected signals are constructively combined at the designated point $\pmb { \rho } _ { m } \mathrm { . }$

$$
\begin{array} { r l } & { \theta _ { n } ^ { * } \left( \mathbf { q } , \pmb { \rho } _ { m } \right) } \\ & { \ = \bar { \theta } - 2 \pi \left( n - 1 \right) \bar { d } \left( \sin \left( \phi _ { \mathrm { t , R I S } } \left( \mathbf { q } , \pmb { \rho } _ { m } \right) \right) - \sin \left( \phi _ { \mathrm { r , R I S } } \left( \mathbf { q } \right) \right) \right) , } \end{array}\tag{15}
$$

where $\bar { \theta }$ is a random phase shift in RIS. However, since $M _ { 0 }$ UAV-BSs need to be served, the optimal $\{ \theta _ { n } ^ { * } \} _ { n = 1 } ^ { N }$ vary for each $m \in \mathbb { M }$ . Therefore, it is necessary to determine a phase alignment point ρ¯ that achieves a Pareto-optimal solution with respect to $\{ \gamma _ { m } \} _ { m \in \mathbb { M } }$ . That is, for given q and $\bar { \pmb { \rho } } ,$ the phase shifts $\left\{ \theta _ { n } ^ { * } \right\} _ { n = 1 } ^ { N }$ are set as

$$
\begin{array} { r l } & { \theta _ { n } ^ { * } \left( \mathbf { q } , \hat { \rho } \right) } \\ & { = \hat { \theta } - 2 \pi \left( n - 1 \right) \hat { d } \left( \sin \left( \phi _ { \mathrm { t , R I S } } \left( \mathbf { q } , \hat { \rho } \right) \right) - \sin \left( \phi _ { \mathrm { r , R I S } } \left( \mathbf { q } \right) \right) \right) } \end{array}\tag{16}
$$

which coherently overlaps the reflected signal to ${ \bar { \pmb { \rho } } } .$ By substituting (16) into (14), $\gamma _ { m }$ becomes

$$
\gamma _ { m } = \bar { \gamma } \frac { \tilde { g } \left( \Delta \phi _ { m } \left( \bar { \pmb { \rho } } \right) \right) } { \left| \left| \pmb { \rho } _ { \mathrm { R I S } } - \pmb { \rho } _ { m } \right| \right| _ { 2 } ^ { 2 } \left| \left| \pmb { \rho } _ { \mathrm { R I S } } \right| \right| _ { 2 } ^ { 2 } } ,\tag{17}
$$

where $\tilde { g } \left( \Delta \phi _ { m } \left( \bar { \pmb { \rho } } \right) \right)$ represents the passive beamforming gain of the aerial-active-RIS towards $\pmb { \rho } _ { m } .$ , assuming that the phases are aligned with ${ \bar { \pmb { \rho } } } .$ This gain is derived by evaluating

$$
\tilde { g } \left( \Delta \phi _ { m } \left( \bar { \pmb { \rho } } \right) \right) = \left| \sum _ { n = 1 } ^ { N } \alpha _ { n } e ^ { j \left( 2 \pi \left( n - 1 \right) \bar { d } \Delta \phi _ { m } \left( \bar { \pmb { \rho } } \right) \right) } \right| ^ { 2 }\tag{18}
$$

in (14), where $\Delta \phi _ { m } \left( \bar { \pmb { \rho } } \right)$ is the sin-AoD deviation between $\bar { \pmb \rho }$ and $\pmb { \rho } _ { m } ,$ , that is, $\begin{array} { r l } { \dot { \Delta } \phi _ { m } \left( \bar { \pmb { \rho } } \right) } & { { } \triangleq } \end{array}$ sin $\left( \phi _ { \mathrm { t , R I S } } \left( \mathbf { q } , \pmb { \rho } _ { m } \right) \right) \ -$ sin $\left( \phi _ { \mathrm { t , R I S } } \left( \mathbf { q } , \bar { \pmb { \rho } } \right) \right)$ . As depicted in Fig. 2(a), the optimal beamforming gain is achieved within the main lobe of ${ \tilde { g } } .$ Moreover, Fig. 2(a) demonstrates that adopting the equal active-RIS gain scenario yields nearly identical results within the main lobe region. This observation is actually rigorously true, which can be proved by the triangular and Cauchy-Schwartz inequality,

$$
\tilde { g } ( \Delta \phi ) \leq \left( \sum _ { n = 1 } ^ { N } \alpha _ { n } \right) ^ { 2 } \leq N \sum _ { n = 1 } ^ { N } \alpha _ { n } ^ { 2 } ,\tag{19}
$$

respectively, with the first inequality becoming tight when $\Delta \phi$ is sufficiently small (main-lobe region) so that the phasors are nearly aligned. In our deployment, the aerial-active-RIS is placed close to the source and the beam is steered towards ρ¯ chosen to represent the Pareto-optimal directions of the UAV-BSs; consequently, $\Delta \phi _ { m } ( \bar { \pmb { \rho } } )$ stays within the main-lobe vicinity and the variation of the denominator term is minor. In this regime, maximizing $\tilde { g }$ is equivalently achieved by uniform $\alpha _ { n } = \alpha$ by the second inequality, which yields the dominant gain improvement while avoiding an ill-conditioned optimization over element-wise amplitudes that provides marginal additional benefit, as it matches with Fig 2(a).

Considering $\alpha _ { n } = \alpha \left( \forall n \right)$ and $\bar { N } \left( \leq N \right)$ utilized active-RIS elements, g˜ becomes

$$
\tilde { g } = \alpha ^ { 2 } g \left( \Delta \phi _ { m } \left( \bar { \rho } \right) \right) \triangleq \alpha ^ { 2 } \left. \frac { \sin \left( \pi \bar { N } \bar { d } \Delta \phi _ { m } \left( \bar { \rho } \right) \right) } { \sin \left( \pi \bar { d } \Delta \phi _ { m } \left( \bar { \rho } \right) \right) } \right. ^ { 2 } ,\tag{20}
$$

As in Fig. 2(b), g dissipates to 0 out of its HPBW ∆φ<sub>HPBW</sub> [60]:

$$
\Delta \phi _ { \mathrm { H P B W } } \left( \bar { N } \right) \approx \frac { 0 . 8 8 5 8 } { \bar { N } \bar { d } } , \ \Delta \phi _ { \mathrm { H P B W } } \left( N \right) \triangleq \Delta \phi _ { \mathrm { H P B W } } ,\tag{21}
$$

and the peak gain of $g$ is $\bar { N } ^ { 2 }$ . Thus, it is necessary to fine-tune $\bar { \pmb \rho }$ and determine the maximum value of $\bar { N }$ to locate every UAV-BS within the HPBW, thereby maximizing $\{ g \left( \Delta \phi _ { m } \left( \bar { \pmb { \rho } } \right) \right) \} _ { m \in \mathbb { M } } .$

Moreover, γ¯ is transformed into

$$
\bar { \gamma } \triangleq \frac { P _ { m } G _ { \mathrm { s } } \beta _ { 0 } ^ { 2 } M } { \sigma _ { \mathrm { a } } ^ { 2 } \beta ( \mathbf { q } , \pmb { \rho } _ { m } ) N \alpha ^ { 2 } + \sigma ^ { 2 } } .\tag{22}
$$

and we can also manipulate (8) by (23), shown at the bottom of the next page.

By adding $N P _ { \mathrm { E } }$ to (23) [32], it implies that for given $\alpha ^ { 2 } , G _ { \mathrm { s } } , N$ , and $P _ { \mathrm { E } } ,$ the maximum power constraint of active-RIS is given by

$$
\begin{array} { l } { P _ { \mathrm { t o t , a } } = P _ { \mathrm { R } } + N P _ { \mathrm { E } } } \\ { \displaystyle \quad = \alpha ^ { 2 } \left( N M \beta _ { \mathrm { s } } G _ { \mathrm { s } } \sum _ { m \in \mathbb { M } } P _ { m } + N \sigma _ { \mathrm { a } } ^ { 2 } \right) + N P _ { \mathrm { E } } \leq P _ { \mathrm { m a x , a } } , } \end{array}\tag{24}
$$

where $P _ { \mathrm { m a x , a } }$ is the maximum threshold of the active-RIS reflection power. From (24), the trade-off between $\alpha ^ { 2 }$ and the consumed power becomes explicit. Increasing $\alpha ^ { 2 }$ directly raises the required $P _ { \mathrm { R } }$ , which in turn tightens $P _ { \mathrm { m a x , a } } .$ . Consequently, the feasible power budget for signal transmission $( \sum _ { m \in \mathbb { M } } P _ { m } )$ is reduced, thereby limiting the admissible $\{ P _ { m } \}$ and reflecting the inherent trade-off between higher amplification gain and increased aerial-active-RIS power consumption.

To reliably support the UAV-BSs, the backhaul rate $\{ R _ { m } \} _ { m \in \mathbb { M } }$ provided by the source should be balanced with the throughput $\{ C _ { m } \} _ { m \in \mathbb { M } }$ of the fronthaul link: $R _ { m }$ = $C _ { m } \in \forall m \in \mathbb { M } )$ , where the balance between fronthaul and

$$
\gamma _ { m } = \bar { \gamma } \left| \mathbf { h } ^ { * } \left( \mathbf { q } , \rho _ { m } \right) \mathbf { A } \Theta \mathbf { H } \left( \mathbf { q } \right) \frac { \mathbf { a } _ { s } \left( \phi _ { t , s } \left( \mathbf { q } \right) \right) } { \sqrt { M } } \right| ^ { 2 } = \bar { \gamma } \frac { \left| \sum _ { n = 1 } ^ { N } \alpha _ { n } e ^ { j \left( \theta _ { n } + 2 \pi \left( n - 1 \right) \bar { d } \left( \sin \left( \phi _ { t , \mathrm { R I S } } \left( \mathbf { q } , \rho _ { m } \right) \right) - \sin \left( \phi _ { x , \mathrm { R I S } } \left( \mathbf { q } \right) \right) \right) \right) } \right| ^ { 2 } } { \left\| \rho _ { \mathrm { H S } } \right\| _ { 2 } ^ { 2 } \left\| \rho _ { \mathrm { H I S } } - \rho _ { m } \right\| _ { 2 } ^ { 2 } } ,\tag{14}
$$

backhaul capacities is critical for optimal network performance with avoidance of bottleneck in B5G/6G wireless network [45], [61]. By $\begin{array} { r } { R _ { m } = \frac { B _ { \mathrm { b } } } { M _ { \mathrm { n } } } \log _ { 2 } { ( 1 + \gamma _ { m } ) } , P _ { m } } \end{array}$ must satisfy the following constraint (25), shown at the bottom of the page.

Moreover, the maximum power budget of the source and aerial-active-RIS is given by [32], [62]

$$
( 1 ) : P _ { \mathrm { t o t , s } } = G _ { \mathrm { s } } \sum _ { m \in \mathbb { M } } P _ { m } \leq P _ { \mathrm { m a x } } , ( 2 ) : ( 2 4 ) ,\tag{26}
$$

respectively, wherein $\mathbf { V } ~ \triangleq ~ [ \mathbf { v } _ { 1 } \cdot \cdot \cdot \mathbf { v } _ { M _ { 0 } } ] \ \in \ \mathbb { C } ^ { M \times M _ { 0 } }$ derived by (12), P <sup>,</sup> diag $\bigl ( \{ P _ { m } \} _ { m \in \mathbb { M } } \bigr ) \in \mathbb { R } ^ { M _ { 0 } \times M _ { 0 } }$ and $P _ { \mathrm { m a x } }$ is the feasible threshold of the source transmit power, respectively.

The definition of energy-efficiency is given by [62]

$$
\eta \triangleq \frac { \sum _ { m \in \mathbb { M } } C _ { m } } { \underbrace { \sum _ { m \in \mathbb { M } } \left( P _ { m } + P _ { \mathrm { U A V - B S } , m } \right) + P _ { \mathrm { t o t , a } } + P _ { \mathrm { g B S } } + P _ { \mathrm { A P } } } _ { \triangleq P _ { 0 } } , }\tag{27}
$$

where the $\textstyle \sum _ { m \in \mathbb { M } } C _ { m }$ comes from $R _ { m } = C _ { m } \ ( \forall m \in \mathbb { M } )$ and $P _ { \mathrm { A P } } , \ P _ { \mathrm { g B S } }$ and $\scriptstyle \sum _ { m \in \mathbb { M } } P _ { \mathrm { U A V - B S } , m }$ are the hardwaredissipated power used by the aerial platform that carries active-RIS, ground backhaul source and the UAV-BS m, respectively. Hence, since the numerator $\textstyle \sum _ { m \in \mathbb { M } } R _ { m }$ becomes constant since the backhaul rate $\{ R _ { m } \} _ { m \in \mathbb { M } }$ is balanced with the fronthaul throughput $\{ C _ { m } \} _ { m \in \mathbb { M } } .$ , we can conclude that the energy-efficiency maximization problem is equivalent to the minimization of $P _ { 0 }$ , the total power consumption of the whole system. From the denominator of (27), $P _ { 0 }$ includes $P _ { \mathrm { A P } } , P _ { \mathrm { g B S } }$ and $\scriptstyle \sum _ { m \in \mathbb { M } } P _ { \mathrm { U A V - B S } , m }$ . In this paper, we adopt two key assumptions: (i) the transmit amplifiers operate within their linear region, and (ii) the circuit power consumption is independent of the communication rate [62], [63], [64]. These assumptions are valid for most practical wireless communication systems [28], [32], [62], where amplifiers are typically designed to work within the linear portion of their transfer function, and where the hardware power consumption

$P _ { \mathrm { A P } } , ^ { 5 } \ P _ { \mathrm { B S } }$ and $\{ P _ { \mathrm { U A V - B S } , m } \} _ { m \in \mathbb { M } }$ can be treated as constant offsets. Therefore, together with $\begin{array} { r } { \sum _ { m \in \mathbb { M } } R _ { m } = \sum _ { m \in \mathbb { M } } C _ { m } , } \end{array}$ we exclude them from the energy-efficiency maximization process, and consider

$$
{ \mathrm { o b j } } \triangleq \sum _ { m \in \mathbb { M } } P _ { m } + P _ { \mathrm { t o t , a } } ,\tag{28}
$$

which is total transmit and operation (reflection + hardware components) power of the source and aerial-active-RIS, respectively, as a objective function of the energy-efficiency maximization, which can be formulated by (29), shown at the bottom of the page. From now on, we will use term “total power” as (28).

Remark 1: Since $C _ { m } \ > \ 0 , \ | | \pmb { \rho } _ { \mathrm { R I S } } | | _ { 2 } \ \geq \ H \ > \ 0$ and $| | \pmb { \rho } _ { \mathrm { R I S } } - \pmb { \rho } _ { m } | | _ { 2 } > 0 \left( \because \pmb { \rho } _ { \mathrm { R I S } } \right.$ is extremely close to the origin, as shown in Theorem 1 and Fig. 5). Thereby, the right-hand side (RHS) of (25) is non-zero, thus ensuring non-zero transmit power for every UAV-BS via aerial-active-RIS.

## III. PROPOSED ALGORITHM

## A. Minimizing the Numerator

Problem (29) is highly nonlinear and non-convex due to its highly-cluttered ${ \mathrm { R H S } } _ { 1 }$ and ${ \mathrm { R H S } } _ { 2 }$ of the constraints. Therefore, we will approach the problem by first assuming that α is given, and minimizing the numerator and maximizing the denominator of RHS<sub>1</sub>, respectively, which leads to the minimization of the objective function. After that, we will minimize the total power with respect to $\alpha .$ . Through numerical simulations, we will show that the second constraint, which represents the upper-bound of the source transmit power, does not impact the feasibility of the problem. Therefore, our approach of focusing primarily on the first constraint is justified for energyefficiency minimization.

It first leads to minimizing the numerator of ${ \mathrm { R H S } } _ { 1 }$ . For given $\alpha ,$ if we multiply $1 + \alpha ^ { 2 } N M \beta _ { \mathrm { s } } G _ { \mathrm { s } }$ to the both sides of the first constraint of (29), which becomes the first term of

$$
P _ { \mathrm { R } } = \alpha ^ { 2 } \left( N \beta _ { \mathrm { s } } \mathcal { E } \left[ \left| \mathbf { a } _ { s } ^ { \mathrm { s } } ( \phi _ { t , s } ( \mathbf { q } ) ) \sum _ { m \in \mathbb { N } } \frac { \mathbf { a } _ { s } ( \phi _ { t , s } ( \mathbf { q } ) ) } { | \mathbf { a } _ { s } ( \phi _ { t , s } ( \mathbf { q } ) ) | | _ { 2 } } \sqrt { P _ { m } G _ { \mathrm { s } } } s _ { m } \right| ^ { 2 } \right] + N \sigma _ { \mathrm { a } } ^ { 2 } \right) = \alpha ^ { 2 } \left( N M \beta _ { \mathrm { s } } G _ { \mathrm { s } } \sum _ { m \in \mathbb { N } } P _ { m } + N \sigma _ { \mathrm { a } } ^ { 2 } \right)\tag{23}
$$

$$
P _ { m } = \alpha ^ { - 2 } \left( 2 ^ { \frac { M _ { 0 } } { B _ { \mathrm { b } } } C _ { m } } - 1 \right) \frac { \left( \sigma ^ { 2 } + \alpha ^ { 2 } \sigma _ { \mathrm { a } } ^ { 2 } N \frac { \beta _ { 0 } } { \| \rho _ { \mathrm { H z } } - \rho _ { m } \| _ { 2 } ^ { 2 } } \right) \| \rho _ { \mathrm { R I S } } - \rho _ { m } \| _ { 2 } ^ { 2 } \| \rho _ { \mathrm { H I S } } \| _ { 2 } ^ { 2 } } { G _ { \mathrm { s } } \beta _ { 0 } ^ { 2 } M g \left( \Delta \phi _ { m } \left( \overline { { \rho } } \right) \right) } \left( \forall m \in \mathbb { M } \right)\tag{25}
$$

$$
\begin{array} { r l } & { \underset { \mathbf { q } , \boldsymbol { \tilde { \rho } } , \{ \tilde { N } \} , \alpha , \{ P _ { m } \} } { \operatorname* { m i n } } \left( 1 + \alpha ^ { 2 } N M \beta _ { \mathrm { s } } G _ { \mathrm { s } } \right) \underset { m \in \mathbb { N } } { \sum } P _ { m } + \alpha ^ { 2 } N \sigma _ { \mathrm { a } } ^ { 2 } + N P _ { \mathrm { E } } \left( \frac { \Delta } { \mathrm { a } } \operatorname { b } \right) } \\ & { \mathrm { s . t . } P _ { m } = \alpha ^ { - 2 } \left( 2 ^ { \frac { M _ { 0 } } { P _ { \mathrm { b } } } C _ { m } } - 1 \right) \frac { \left( \sigma ^ { 2 } + \alpha ^ { 2 } \sigma _ { \mathrm { a } } ^ { 2 } N \frac { \beta _ { 0 } } { \| \beta \mathbf { q } \scriptscriptstyle { \mathrm { R } } - \beta _ { m } \| _ { 2 } ^ { 2 } } \right) \left\| \rho _ { \mathrm { R I S } } - \rho _ { m } \right\| _ { 2 } ^ { 2 } \left\| \rho _ { \mathrm { R I S } } \right\| _ { 2 } ^ { 2 } } { G _ { \mathrm { s } } \beta _ { 0 } ^ { 2 } M g \left( \Delta \phi _ { m } \left( \overline { { \rho } } \right) \right) } ( \triangleq \mathrm { R H S } _ { 1 } ) \ ( \forall m \in \mathbb { M } ) , } \\ & { \underset { m \in \mathbb { N } } { \sum } P _ { m } \leq \operatorname* { m i n } \left\{ G _ { \mathrm { s } } ^ { - 1 } P _ { \mathrm { m a x } } , \alpha ^ { - 2 } G _ { \mathrm { s } } ^ { - 1 } N ^ { - 1 } M ^ { - 1 } \beta _ { \mathrm { s } } ^ { - 1 } \left( P _ { \mathrm { m a x } , \mathrm { a } } - N P _ { \mathrm { E } } - \alpha ^ { 2 } N \sigma _ { \mathrm { a } } ^ { 2 } \right) \right\} ( \triangleq \mathrm { R H S } _ { 2 } ) } \end{array}\tag{29}
$$

the objective function in (29) related to $\textstyle \sum _ { m \in \mathbb { M } } P _ { m }$ , it becomes (30), shown at the bottom of the page.

Hence, the RHS of (30) is determined by

$$
( | | \pmb { \rho } _ { \mathrm { R I S } } | | _ { 2 } ^ { 2 } + \tilde { \Omega } _ { 1 } ) ( | | \pmb { \rho } _ { \mathrm { R I S } } - \pmb { \rho } _ { m } | | _ { 2 } ^ { 2 } + \tilde { \Omega } _ { 2 } ) ,\tag{31}
$$

where

$$
\tilde { \Omega } _ { 1 } = \alpha ^ { 2 } N M \beta _ { 0 } G _ { \mathrm { s } } , \tilde { \Omega } _ { 2 } = \alpha ^ { 2 } \frac { \sigma _ { \mathrm { a } } ^ { 2 } } { \sigma ^ { 2 } } N \beta _ { 0 } .\tag{32}
$$

Thereafter, by letting $\mathbf { q } _ { m }$ the 2D location of the aerial-active-RIS considering only UAV-BS m $( \pmb { \rho } _ { \mathrm { R I S } } \ = \ [ \mathbf { q } _ { m } ^ { \mathrm { T } } \ H ] ^ { \mathrm { T } } )$ , the numerator minimization becomes equivalent to:

$$
\begin{array} { r l r } {  { \operatorname* { m i n } \big ( \| \rho _ { \mathrm { R I S } } \| _ { 2 } ^ { 2 } + \tilde { \Omega } _ { 1 } \big ) \big ( \| \rho _ { \mathrm { R I S } } - \pmb { \rho } _ { m } \| _ { 2 } ^ { 2 } + \tilde { \Omega } _ { 2 } \big ) } } \\ & { } & { \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } } \\ & { } & { = \Big ( H ^ { 2 } + \| \mathbf { q } _ { m } \| _ { 2 } ^ { 2 } + \tilde { \Omega } _ { 1 } \Big ) ( ( H - h _ { m } ) ^ { 2 } + \| \mathbf { q } _ { m } - \mathbf { w } _ { m } \| _ { 2 } ^ { 2 } + \tilde { \Omega } _ { 2 } ) } \\ & { } & { \mathrm { ~ } \mathrm { ~ s . t . ~ } \| \mathbf { q } _ { m } \| _ { 2 } \ll \delta \| \mathbf { w } _ { m } \| _ { 2 } , \qquad ( 3 3 ) } \end{array}
$$

where $\delta \ll 1$ is constant. The constraint $\begin{array} { r }   { \mathbf { \tilde { \mathbf { \Lambda } } } ^ { * * } | | \mathbf { q } _ { m } | | _ { 2 } \ll \delta | | \mathbf { w } _ { m } | | _ { 2 } , \mathbf { \tilde { \lambda } } } \end{array}$ is imposed to keep ${ \bf q } _ { m }$ near the source. Positioning $\mathbf { q } _ { m }$ with fixed H close to the source ensures that the full-array RIS architecture $( { \bar { N } } \ = \ N )$ is almost certainly utilized, which maximizes the minimum SNR [50] and consequently reduces the total transmit power $( 1 + \alpha ^ { 2 } N M \beta _ { \mathrm { s } } G _ { \mathrm { s } } ) \sum _ { m \in \mathbb { M } } P _ { m }$ . Fortunately, we can find a practical solution for the problem, as stated in Theorem 1.

Theorem 1: The solution of Problem (33) is given by

$$
\mathbf { q } _ { m } ^ { * } = \kappa _ { m } \mathbf { w } _ { m } ,\tag{34}
$$

where

$$
\kappa _ { m } = { \frac { 1 } { 2 } } + 2 { \sqrt { - { \frac { a } { 3 } } } } \cos \left( { \frac { 1 } { 3 } } \cos ^ { - 1 } \left( { \frac { 3 b } { 2 a } } { \sqrt { - { \frac { 3 } { a } } } } \right) - { \frac { 4 } { 3 } } \pi \right)\tag{35}
$$

Here, a and b are given by

$$
a \triangleq \frac 1 2 \left( \zeta _ { 1 } ^ { 2 } + \zeta _ { 2 } ^ { 2 } + \bar { \Omega } _ { 1 } + \bar { \Omega } _ { 2 } \right) - \frac 1 4 , b \triangleq \frac 1 4 \left( \zeta _ { 2 } ^ { 2 } - \zeta _ { 1 } ^ { 2 } + \bar { \Omega } _ { 2 } - \bar { \Omega } _ { 1 } \right) ,\tag{36}
$$

where

$$
\zeta _ { 1 } \triangleq \frac { H } { | | \mathbf { w } _ { m } | | _ { 2 } } , \zeta _ { 2 } \triangleq \frac { | H - h _ { m } | } { | | \mathbf { w } _ { m } | | _ { 2 } } , \bar { \Omega } _ { i } \triangleq | | \mathbf { w } _ { m } | | _ { 2 } ^ { - 2 } \tilde { \Omega } _ { i } ( i = 1 , 2 ) .\tag{37}
$$

Proof: See Appendix A.

We numerically confirm in Section IV that $\kappa _ { m }$ remains positive yet very close to zero under the given assumptions, thereby validating that $\mathbf { q } _ { m } ^ { * } = \kappa _ { m } \mathbf { w } _ { m }$ serves as an appropriate solution for the proposed power-minimization procedure.

After obtaining $\{ \mathbf { q } _ { m } ^ { * } \} _ { m \in \mathbb { M } } .$ , we need to determine a single $\mathbf { q } ^ { * }$ that achieves a Pareto-optimal for all $m \in \mathbb { M }$ in relation to (33). We adopt a global criterion approach that minimizes the total \` -distances, thereby guiding the solution toward the Pareto front [66].

$$
\mathop { \operatorname* { m i n } } _ { \mathbf { q } } \sum _ { m \in \mathbb { M } } | | \mathbf { q } _ { m } ^ { * } - \mathbf { q } | | _ { 2 } .\tag{38}
$$

Problem (38) is known as the Fermat-Torricelli problem, which is convex and can therefore be efficiently solved using Weiszfeld’s algorithm [67] with guaranteeing the optimal solution [68]. Consequently, by solving (38), we obtain $\mathbf { q } ^ { * }$ which serves as a suboptimal solution for the numerator minimization. The obtained $\mathbf { q } ^ { * }$ provides a clear deployment insight: the aerial-active-RIS should be placed sufficiently closer to the source in terms of 2D distance to enhance the incident signal power, while maintaining a moderate distance from the UAV-BSs to balance the overall power consumption.

Remark 2: To keep $| | \mathbf { q } ^ { * } | | _ { 2 }$ small even in the presence of an outlier within $\{ \mathbf { q } _ { m } ^ { * } \} _ { m \in \mathbb { M } } ,$ , we minimize the sum of norms rather than the squared norms in (38), which further enhances the robustness of the solution [66].

## B. Maximizing the Denominator

We adopt the same methodology as described in Section III-B of [50] to solve the denominator (29) since the denominator is exactly same with the passive-RISimplemented scenario in [50]. This allows us to determine the sub-optimal values for $\{ \bar { N } \} , \bar { \pmb { \rho } } \ ( \mathrm { o r } \ \{ \bar { \pmb { \rho } } _ { i } ^ { * } \} _ { i = 1 } ^ { L } )$ , and Θ for utilizing both full RIS array or L-times partitioned sub-array scenario.

## C. Determining α and $\{ P _ { m } \} _ { m \in \mathbb { M } }$

Since we have determined $\mathbf { q } ^ { * } , \{ \bar { N } \} , \bar { \pmb { \rho } } \ ( \mathrm { o r } \ \{ \bar { \pmb { \rho } } _ { i } ^ { * } \} _ { i = 1 } ^ { L } ) ,$ Θ, the optimal $\alpha ^ { * }$ is determined by following Theorem 2.

Theorem 2: For given $\mathbf { \bar { q } } ^ { * } , \{ \bar { N } \} , \bar { \pmb { \rho } } ( \mathrm { o r } \{ \bar { \pmb { \rho } } _ { i } ^ { * } \} _ { i = 1 } ^ { L } ) , \mathbf { \Theta } _ { } \mathbf { \Theta } _ { }$ , the optimum α that minimizes obj is given by

$$
\alpha ^ { * } = \operatorname* { m i n } \left\{ \sqrt [ 4 ] { \frac { \sum _ { m \in \mathbb { M } } \Omega _ { 0 } \left| \left| \rho _ { \mathrm { R I S } } \right| \right| _ { 2 } ^ { 2 } \left| \left| \rho _ { \mathrm { R I S } } - \rho _ { m } \right| \right| _ { 2 } ^ { 2 } } { N \sigma _ { \mathrm { a } } ^ { 2 } + \sum _ { m \in \mathbb { M } } \Omega _ { 0 } \Omega _ { 1 } \Omega _ { 2 } } } , \alpha _ { \operatorname* { m a x } } \right\} ,
$$

where

(39)

$$
\begin{array} { l } { \Omega _ { 0 } = \sigma ^ { 2 } \frac { 2 ^ { \frac { M _ { 0 } } { B _ { \mathrm { b } } } C _ { m } } - 1 } { G _ { \mathrm { s } } \beta _ { 0 } ^ { 2 } M g \left( \Delta \phi _ { m } ^ { \ast } \right) } } \\ { \Omega _ { 1 } = \alpha ^ { - 2 } \tilde { \Omega } _ { 1 } = N M \beta _ { 0 } G _ { \mathrm { s } } , \ \Omega _ { 2 } = \alpha ^ { - 2 } \tilde { \Omega } _ { 2 } = \frac { \sigma _ { \mathrm { a } } ^ { 2 } } { \sigma ^ { 2 } } N \beta _ { 0 } . } \end{array}\tag{40}
$$

Proof: See Appendix B.

Since we determine all the variables ${ \mathbf q } , \bar { \pmb \rho } , \left\{ \bar { N } \right\} , \alpha ^ { * }$ , the power $\{ P _ { m } \} _ { m \in \mathbb { M } }$ is given by ${ \mathrm { R H S } } _ { 1 }$ , which can be expressed by (42), shown at the bottom of the next page, where $\rho _ { \mathrm { R I S } } ^ { * } =$ $\left[ \dot { \mathbf { q } } ^ { * \mathrm { T } } \dot { H } \right] ^ { \mathrm { T } }$ and $\Delta \phi _ { m } ^ { * }$ is defined by

$$
\Delta \phi _ { m } ^ { * } \triangleq \left\{ \Delta \phi _ { m } \left( \bar { \pmb { \rho } } ^ { * } \right) \ \left( \bar { N } = N \ \mathrm { ( f u l l - a r r a y ) } \right) \right.\tag{41}
$$

where the full- and L-times-partitioned sub-array scenario with phase-align points $\{ \bar { \pmb { \rho } } _ { i } ^ { * } \} _ { i = 1 } ^ { \bar { L } }$ and partitions of UAV-BS

$$
\begin{array} { r l } & { \left( 1 + \alpha ^ { 2 } N M \beta _ { \mathrm { s } } G _ { \mathrm { s } } \right) P _ { m } } \\ & { = \alpha ^ { - 2 } \left( 2 ^ { M _ { \mathrm { b } } C _ { m } } - 1 \right) \frac { \left( 1 + \alpha ^ { 2 } N M \frac { \beta _ { \mathrm { 0 } } } { \| \rho _ { \mathrm { R I S } } \| _ { 2 } ^ { 2 } } G _ { \mathrm { s } } \right) \left( \sigma ^ { 2 } + \alpha ^ { 2 } \sigma _ { \mathrm { a } } ^ { 2 } N \frac { \beta _ { \mathrm { 0 } } } { \| \rho _ { \mathrm { R I S } } - \rho _ { m } \| _ { 2 } ^ { 2 } } \right) \| \rho _ { \mathrm { R I S } } - \rho _ { m } \| _ { 2 } ^ { 2 } \| \rho _ { \mathrm { R I S } } \| _ { 2 } ^ { 2 } } { G _ { \mathrm { s } } \beta _ { \mathrm { 0 } } ^ { 2 } M g \left( \Delta \phi _ { m } \left( \overline { { \rho } } \right) \right) } \left( \gamma _ { \mathrm { a } } \right) } \end{array}\tag{30}
$$

$\{ \mathbb { M } _ { i } \} _ { i = 1 } ^ { L } ( \cup _ { i } \mathbb { M } _ { i } = \mathbb { M } )$ are defined in Section III-B in [45]. Thus, by substituting (42) and $\alpha ^ { * }$ to obj, we can achieve the optimal total power by utilizing aerial-active-RIS.

## D. Conditions for Feasibility

Although the power is to be positive in remark $^ { l , }$ we cannot claim the strict feasibility since we cannot always guarantee the upper-bound of $\textstyle \sum _ { m \in \mathbb { M } } P _ { m }$ by (42). Specifically, the backhaul-rate-ensuring constraint leads to:

$$
R _ { m } = C _ { m } \to P _ { m } = [ \mathrm { R H S } _ { 1 } ] _ { m } ~ ( \forall m \in \mathbb { M } ) ,\tag{43}
$$

where $[ \mathrm { R H S } _ { 1 } ] _ { m }$ is the RHS<sub>1</sub> corresponding to $P _ { m }$ in the first constraint of (29), and the source/active-RIS power constraint is trivially given by

$$
\sum _ { m \in \mathbb { M } } P _ { m } \leq \mathrm { R H S _ { 2 } } .\tag{44}
$$

From (43) and (44), it is clear that although the individual transmit power meets the constraint in (43) by choosing the lower-bound itself as a transmit power value, we cannot guarantee $\begin{array} { r } { \sum _ { m \in \mathbb { M } } [ \mathrm { R H S } _ { 1 } ] _ { m } \ \leq \ \mathrm { R H S } _ { 2 } \ [ 6 2 ] , \ [ 6 9 ] , \ [ 7 0 ] . \ \mathrm { W e } } \end{array}$ , however, offer some additional clarification on whether the feasibility holds or not. Using the closed-form rate-matching transmit power in (42), the total source transmit power can be expressed as

$$
\begin{array} { r l } & { \displaystyle \sum _ { m \in \mathbb { M } } P _ { m } ^ { * } } \\ & { = \frac { d _ { s } ^ { 2 } } { G _ { s } \beta _ { 0 } ^ { 2 } M } \left( \alpha ^ { - 2 } \sigma ^ { 2 } \sum _ { m \in \mathcal { M } } \frac { \Gamma _ { m } d _ { m } ^ { 2 } } { g _ { m } } + \sigma _ { a } ^ { 2 } N \beta _ { 0 } \sum _ { m \in \mathcal { M } } \frac { \Gamma _ { m } } { g _ { m } } \right) , } \end{array}\tag{45}
$$

where $\Gamma _ { m } \triangleq 2 ^ { \frac { M _ { 0 } } { B _ { b } } C _ { m } } - 1 , d _ { s } ^ { 2 } = \| \pmb { \rho } _ { \mathrm { R I S } } ^ { * } \| _ { 2 } ^ { 2 } , d _ { m } ^ { 2 } = \| \pmb { \rho } _ { \mathrm { R I S } } ^ { * } -$ $\rho _ { m } \| _ { 2 } ^ { 2 } .$ , and $g _ { m } = g ( \Delta \phi _ { m } ^ { * } )$ . Substituting (45) into the two terms in the left-hand side in (29) yields two sufficient feasibility conditions with respect to RHS<sub>2</sub>.

(1. Source power budget $P _ { \mathrm { m a x } } )$

$$
P _ { \operatorname* { m a x } } \geq \frac { d _ { s } ^ { 2 } } { \beta _ { 0 } ^ { 2 } M } \left( \alpha ^ { - 2 } \sigma ^ { 2 } \sum _ { m \in \mathcal { M } } \frac { \Gamma _ { m } d _ { m } ^ { 2 } } { g _ { m } } + \sigma _ { a } ^ { 2 } N \beta _ { 0 } \sum _ { m \in \mathcal { M } } \frac { \Gamma _ { m } } { g _ { m } } \right) .\tag{46}
$$

(2. Aerial-Active-RIS power budget $P _ { \mathrm { m a x } , a } )$

$$
\begin{array} { r l } & { P _ { \operatorname* { m a x } , a } } \\ & { \geq N P _ { E } + \alpha ^ { 2 } N \sigma _ { a } ^ { 2 } } \\ & { \phantom { \geq } + N \beta _ { s } \frac { d _ { s } ^ { 2 } } { \beta _ { 0 } ^ { 2 } } \left( \sigma ^ { 2 } \sum _ { m \in \mathcal { M } } \frac { \Gamma _ { m } d _ { m } ^ { 2 } } { g _ { m } } + \alpha ^ { 2 } \sigma _ { a } ^ { 2 } N \beta _ { 0 } \sum _ { m \in \mathcal { M } } \frac { \Gamma _ { m } } { g _ { m } } \right) . } \end{array}\tag{47}
$$

Equations (46) and (47) provide an explicit post-solution feasibility check:

• Once the optimal variables are obtained, $\sum _ { m } P _ { m } ^ { * }$ is evaluated via (45)

• The constraint $\begin{array} { r } { \sum _ { m } P _ { m } ^ { * } \leq \mathrm { R H S _ { 2 } } } \end{array}$ is verified by checking (46) and (47).

Equation (45) reveals that $\sum _ { m } P _ { m } ^ { * }$ consists of two components: an $\alpha ^ { - 2 }$ -decreasing term associated with thermal noise and an α-independent floor term induced by the amplified dynamic noise. Consequently, increasing α does not cause $et { } { _ { \sum _ { m } } } P _ { m } ^ { * }$ to diverge. Furthermore, when the phasealignment/partitioning design keeps all UAV-BSs within the RIS main lobe, the passive beamforming gain satisfies $g _ { m } \simeq$ $N ^ { 2 }$ [45]. In this regime,

$$
\sum _ { m } \frac { \Gamma _ { m } } { g _ { m } } \approx \frac { 1 } { N ^ { 2 } } \sum _ { m } \Gamma _ { m } , \sum _ { m } \frac { \Gamma _ { m } d _ { m } ^ { 2 } } { g _ { m } } \approx \frac { 1 } { N ^ { 2 } } \sum _ { m } \Gamma _ { m } d _ { m } ^ { 2 } ,\tag{48}
$$

so that the last term of the right-hand side in both (46) and (47) scale down with N. In Section IV (Fig. 8), we verify that the practical transmit power and total power obtained by the proposed algorithm remain well below the feasible threshold, achieving a feasibility rate of 100% even with conservative power budget. This confirms the almost-sure feasibility of our approach, thereby rendering the consideration of infeasible scenarios negligible.

## E. Analysis on Computational Complexity

The computational complexity of the proposed algorithm is divided into three main stages. In Section III-A, we begin by selecting $\{ \kappa _ { m } \} _ { m \in  { \mathbb { M } } }$ according to (35), which involves a complexity of $\mathcal { O } \left( M _ { 0 } \right)$ . Subsequently, we solve for $\mathbf { q } ^ { * }$ using (38), which has an upper-bounded complexity of $\mathcal { O } \left( I _ { \mathbb { M } } M _ { 0 } \right)$ , where $I _ { ( \cdot ) }$ represents the number of iterations required by Weiszfeld’s algorithm for the given set [45], [67], [68]. In Section III-B, the complexity is identical to that presented in Section III-B of [45], and is given by $\mathcal { O } ( ( L _ { \mathrm { m a x } } + \bar { I } _ { L } + M _ { 0 } ) M _ { 0 } + L )$ . Here, $L _ { \mathrm { m a x } }$ denotes the maximum candidate for L, identified through a one-dimensional search, and $I _ { L } \triangleq \operatorname* { m a x } _ { i \in \{ 1 , \cdots , L \} } I _ { \mathbb { M } _ { i } }$ . The RIS phase alignment step, performed via (16), incurs a complexity of $\mathcal { O } ( N )$ . Lastly, in Section III-C, we optimize $\alpha ^ { * }$ and $\{ P _ { m } ^ { * } \} _ { m \in \mathbb { M } }$ through (39) and (42), each requiring $\mathcal { O } \left( M _ { 0 } \right)$ Thus, the overall computational complexity is bounded as

$$
\begin{array} { r l } & { \mathcal { O } \left( \left( I _ { \mathbb { M } } + L _ { \operatorname* { m a x } } + I _ { L } + M _ { 0 } \right) M _ { 0 } + L + N \right) } \\ & { ~ \approx \mathcal { O } \left( \left( I _ { \mathbb { M } } + I _ { L } + M _ { 0 } \right) M _ { 0 } + N \right) \ \left( \because  I _ { ( \cdot ) } > L _ { \operatorname* { m a x } } \geq L \right) , } \end{array}\tag{49}
$$

which is within quadratic order. Therefore, we can conclude that the proposed algorithm is both energy-efficient and computationally efficient.

## IV. NUMERICAL RESULTS

## A. Simulation Setup

We considered $1 0 ^ { 3 }$ independent realizations of randomly distributed users and their associated UAV-BSs [8]. The fronthaul and backhaul links were assumed to operate over 2 GHz

$$
P _ { m } ^ { * } = \alpha ^ { * - 2 } \left( 2 ^ { \frac { M _ { 0 } } { B _ { \mathrm { b } } } C _ { m } } - 1 \right) \frac { \left( \sigma ^ { 2 } + \alpha ^ { * 2 } \sigma _ { \mathrm { a } } ^ { 2 } N \frac { \beta _ { 0 } } { \left| \left| \rho _ { \mathrm { R I S } } ^ { * } - \rho _ { m } \right| \right| _ { 2 } ^ { 2 } } \right) \left| \left| \rho _ { \mathrm { R I S } } ^ { * } - \rho _ { m } \right| \right| _ { 2 } ^ { 2 } \left| \left| \rho _ { \mathrm { R I S } } ^ { * } \right| \right| _ { 2 } ^ { 2 } } { G _ { \mathrm { s } } \beta _ { 0 } ^ { 2 } M g \left( \Delta \phi _ { m } ^ { * } \right) } \left( \forall m \in \mathbb { M } \right)\tag{42}
$$

![](images/66686eb0e39eb0dd7259e998b0ee049fe59e8ae4df2296490e7226e6077916cc.jpg)  
Fig. 3. Simulated aerial-active-RIS configuration with an N-element active-RIS and $M _ { 0 }$ UAV-BSs.

and sub-6 GHz frequency bands, respectively [72]. Furthermore, the directional antennas at source were assumed to follow the radiation pattern described in [72]. Accordingly, the directional antenna gain $G _ { \mathrm { s } } ( \theta , \phi )$ with maximum directional gain $G _ { \mathrm { m a x } }$ can be expressed as

$$
G _ { \mathrm { s } } \left( \theta , \phi \right) = G _ { \mathrm { m a x } } - \operatorname* { m i n } \left( A _ { \mathrm { v } } \left( \theta \right) + A _ { \mathrm { h } } \left( \phi \right) , A _ { \mathrm { m a x } } \right) .\tag{50}
$$

where the vertical and horizontal attenuations $A _ { \mathrm { v } }$ and $A _ { \mathrm { h } } ,$ respectively, are given by

$$
\left\{ { \begin{array} { l } { A _ { \mathrm { v } } \left( \theta \right) = \operatorname* { m i n } \left( 1 2 \left( { \frac { \theta - 9 0 ^ { \circ } } { \theta _ { \mathrm { H } } } } \right) ^ { 2 } , \ { \mathrm { S L A } } _ { \mathrm { v } } \right) } \\ { A _ { \mathrm { h } } \left( \phi \right) = \operatorname* { m i n } \left( 1 2 \left( { \frac { \phi } { \phi _ { \mathrm { H } } } } \right) ^ { 2 } , \ A _ { \mathrm { m a x } } \right) , } \end{array} } \right.\tag{51}
$$

where $\theta \in [ 0 ^ { \circ } , 1 8 0 ^ { \circ } ]$ and $\phi \in [ - 1 8 0 ^ { \circ } , 1 8 0 ^ { \circ } )$ denote the vertical and horizontal angles, $\theta _ { \mathrm { H } }$ and φ<sub>H</sub> represent the HPBWs in the vertical and horizontal domains, respectively, and $\operatorname { S L A } _ { \mathrm { v } }$ and $A _ { \mathrm { m a x } }$ denote the vertical side-lobe and maximum attenuations, respectively.

Under this setup, we conducted a numerical performance comparison between the proposed aerial-active-RIS scheme and the passive-RIS-based algorithm in [45], which aims to minimize the transmit power at the source. Under same achievable rate $\{ C _ { m } \} _ { m \in \mathbb { M } }$ , the energy-efficiency $\eta _ { \mathrm { p } }$ for passive-RIS is given by [45], [62]

$$
\eta _ { \mathrm { p } } = \frac { \sum _ { m \in \mathbb { M } } C _ { m } } { \sum _ { m \in \mathbb { M } } ( P _ { m , \mathrm { p } } + P _ { \mathrm { U A V - B S } , m } ) + P _ { \mathrm { g B S } } + P _ { \mathrm { A P } } } ,\tag{52}
$$

where $P _ { m , \mathrm { p } }$ is the source transmit power corresponds to UAV-BS m with aerial-passive-RIS, which also makes the backhaul rate $\{ C _ { m } \} _ { m \in \mathbb { M } }$ for each UAV-BS m [45]. Thus, it is reasonable to compare $\sum _ { m \in \mathbb { M } } P _ { m , \mathrm { p } }$ (in [45]) with obj for aerial-passive/active-RIS scenarios, respectively, which allows for a fair comparison of energy-efficiency minimization between the two cases. The simulation environment based on the parameters is illustrated in Fig. 3, and the detailed parameters are given in Table I.

## B. Active-RIS vs. Af Relay: Performance Comparison

It is reasonable to explore the scenario where the aerialactive-RIS is not deployed. In such a case, an AF relay on the aerial platform serves as a natural alternative, as it similarly receives the incoming signal and forwards an amplified one to the destination. However, a closer comparison reveals that the proposed aerial-active-RIS architecture can offer greater advantages over the aerial-AF-relay. Specifically, the total AF-relay power consumption is expressed as [73]

TABLE I  
SIMULATION PARAMETERS
<table><tr><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Description</td><td rowspan=1 colspan=1>Value</td></tr><tr><td rowspan=1 colspan=1> $\boldsymbol { B _ { \mathrm { b } } }$ </td><td rowspan=1 colspan=1>Bandwidth of the backhaul link(unless referred)</td><td rowspan=1 colspan=1>50 (MHz)</td></tr><tr><td rowspan=1 colspan=1> $\overline { { M _ { 0 } } }$ </td><td rowspan=1 colspan=1>Number of UAV-BSs</td><td rowspan=1 colspan=1>≥ 4 [8]</td></tr><tr><td rowspan=1 colspan=1> $\overline { { \mathcal { G } } }$ </td><td rowspan=1 colspan=1>Targeted urban region</td><td rowspan=1 colspan=1> $\overline { { 5 0 0 \times 5 0 0 \ ( \mathrm { m } ) } }$ </td></tr><tr><td rowspan=1 colspan=1> $\underline { { \pmb { \rho } } } _ { \mathcal { G } }$ </td><td rowspan=1 colspan=1>Center of G (unless referred)</td><td rowspan=1 colspan=1> $[ 1 0 0 0 0 ] ^ { \mathrm { T } } \ \mathrm { ( m ) }$ </td></tr><tr><td rowspan=1 colspan=1> $( P _ { \mathrm { m a x } } , P _ { \mathrm { m a x , a } } )$ </td><td rowspan=1 colspan=1>Feasible threshold ofsource transmit power andactive-RIS power consumption</td><td rowspan=1 colspan=1>20 (dBm) [32]</td></tr><tr><td rowspan=1 colspan=1> $\overline { { G _ { \mathrm { m a x } } } }$ </td><td rowspan=1 colspan=1>Maximum directional gain</td><td rowspan=1 colspan=1>8 (dB)</td></tr><tr><td rowspan=1 colspan=1> $H$ </td><td rowspan=1 colspan=1>Height of aerial-RIS(unless referred)</td><td rowspan=1 colspan=1>180 (m)</td></tr><tr><td rowspan=1 colspan=1> $N$ </td><td rowspan=1 colspan=1>Number of RIS elements(unless referred)</td><td rowspan=1 colspan=1>300</td></tr><tr><td rowspan=1 colspan=1> $\overline { { M } }$ </td><td rowspan=1 colspan=1>Number of source antennas</td><td rowspan=1 colspan=1>16</td></tr><tr><td rowspan=1 colspan=1> $( d _ { \mathrm { s } } , d _ { \mathrm { R I S } } )$ </td><td rowspan=1 colspan=1>Source antenna andRIS element separations</td><td rowspan=1 colspan=1> $\left( { \frac { \lambda } { 2 } } , { \frac { \lambda } { 1 0 } } \right) [ 7 1 ]$ </td></tr><tr><td rowspan=1 colspan=1> $\alpha _ { \mathrm { m a x } } ^ { 2 }$ </td><td rowspan=1 colspan=1>Maximum amplification gain ofthe active-RIS</td><td rowspan=1 colspan=1>40 (dB) [32]</td></tr><tr><td rowspan=1 colspan=1> $P _ { \mathrm { { E } } }$ </td><td rowspan=1 colspan=1>Power consumed bysingle active hardware component</td><td rowspan=1 colspan=1>-3.8 (dBm)[28], [32]</td></tr><tr><td rowspan=1 colspan=1> $\Delta _ { 0 }$ </td><td rowspan=1 colspan=1>Distance from $\overline { { { \alpha } ^ { * 2 } } }$ in dB fornon-optimality comparison</td><td rowspan=1 colspan=1>-5 (dB)</td></tr><tr><td rowspan=1 colspan=1> $\sigma _ { \mathrm { a } } ^ { 2 }$ </td><td rowspan=1 colspan=1>Dynamic noise of theactive-RIS elements</td><td rowspan=1 colspan=1>-80 (dBm)[28], [32]</td></tr></table>

$$
\begin{array} { l } { P _ { \mathrm { t o t , A F } } = \displaystyle \sum _ { m \in \mathbb { M } } \left( P _ { m , \mathrm { A F } } + P _ { \mathrm { U A V - B S - } m } \right) + P _ { \mathrm { R , A F } } } \\ { \displaystyle \qquad + P _ { \mathrm { g B S } } + P _ { \mathrm { c i r c , A F } } + P _ { \mathrm { A P } } , } \end{array}\tag{53}
$$

where $\sum _ { m \in \mathbb { M } } P _ { m , \mathrm { A F } }$ is the source transmit power needed to support the target rate, $P _ { \mathrm { R , A F } }$ is the relay transmit power (amplification power) required under the AF protocol, $P _ { \mathrm { c i r c , A F } }$ is hardware power cost of the N-element AF relay [73]:

$$
P _ { \mathrm { c i r c , A F } } = N ( P _ { \mathrm { D A C } } + P _ { \mathrm { m i x } } + P _ { \mathrm { f l t } } ) + P _ { \mathrm { s y n } } ,\tag{54}
$$

where $P _ { \mathrm { D A C } } , P _ { \mathrm { m i x } } , P _ { \mathrm { f i l t } }$ , and $P _ { \mathrm { s y n } }$ represent the power consumed by the digital-to-analog (DAC) converter, mixer, filter, and frequency synthesizer, respectively. Herein, same with the aerial-active-RIS, $P _ { \mathrm { A P } } , \ P _ { \mathrm { B S } }$ and $\{ P _ { \mathrm { U A V - B S } , m } \} _ { m \in \mathbb { M } }$ are treated as constant offsets. According to practical values reported in [73], the combined term $P _ { \mathrm { D A C } } + P _ { \mathrm { m i x } } + P _ { \mathrm { f i l t } }$ reaches approximately 18.2 dBm, which is over 20 dB higher than the corresponding $P _ { \mathrm { E } }$ used in Table I. Furthermore, the additional contribution from $P _ { \mathrm { s y n } }$ further exacerbates the total power requirement. Although the aerial-AF-relay operates in full-duplex mode, it incurs additional hardware complexity to suppress self-interference [27], [74]. As a result, the aerial-AF-relay suffers from significantly higher power demands, particularly on the relay side, making it substantially less energy-efficient than the proposed aerial-active-RIS architecture.

For numerical comparison, Fig. 4 plots the resulting total power versus the distance of $\pmb { \rho } _ { \mathcal { G } }$ from the source $( d _ { \mathcal { G } } )$ for aerial-active-RIS vs. $N \ = \ M .$ -element aerial-AF-relay [75], [76], $[ 7 7 ] ^ { 6 }$ with optimal configuration employed by numerical exhaustive search. The figure shows that the aerial-AF-relay consistently requires substantially higher power, even with less number of elements $( M \ < \ N$ in general), than the aerial-active-RIS under identical throughput conditions: gain produced by 25.48 and 27.19 dB in $d _ { \mathcal { G } } = 1 0 0 0$ and 1200 m, respectively. Note that beyond a certain distance in the figure, the AF-relay curve dramatically rises as the relay transmit power required to compensate for the multiplicative path loss becomes dominant [62]. Furthermore, the pronounced gap from aerial-active-RIS and aerial-AF-relay stems from the fundamental architectural differences between the two systems: the aerial-AF-relay incurs an additional relay transmission stage, where the aerial-AF-relay is located at an intermediate position between the source and the receivers, to compensate for multiplicative path loss and amplified noise, together with a significantly larger RF-chain circuit power due to high-power components mentioned in (54), whereas the aerial-active-RIS benefits from cascaded source-RIS-destination reflection with amplification gain and relies only on low-power element-level amplification and control circuitry represented by $P _ { \mathrm { { E } } }$

![](images/06e0c82599c80ef0d7b34f3f680ab4c9500137b11e477e7c2d0e6249d353e73f.jpg)  
Fig. 4. Simulated aerial-active-RIS configuration compared to M-array aerial-AF-relay.

## C. Reliability of Placement and Amplification in Aerial-Active-RIS

Fig. 5 illustrates the variation of $\kappa _ { m }$ with respect to the aerial-active-RIS height $( H )$ and the 2D distance of the UAV-BS from the source $\left( | | \mathbf { w } _ { m } | | _ { 2 } \right)$ . It is observed that $\kappa _ { m }$ is on the order of $1 0 ^ { - 2 }$ when ${ \big | } { \big | } \mathbf { w } _ { m } { \big | } { \big | } _ { 2 }$ is sufficiently large, implying that $\mathbf { q } _ { m } ^ { * } = \kappa _ { m } \mathbf { w } _ { m }$ lies extremely close to the origin relative to $\mathbf { w } _ { m }$ . Moreover, $\kappa _ { m }$ increases as $H$ grows. This occurs because a larger H yields a greater a and a smaller $\sqrt { - \frac { a } { 3 } }$ (with $a \ < \ 0 )$ in (35), while the posterior term of $\sqrt { - \frac { a } { 3 } }$ in (35), approximated by $\scriptstyle \left( - 1 + { \frac { \epsilon } { 3 { \sqrt { 3 } } } } \right)$ for $| \epsilon | \ll 1$ in (65), remains negative. Consequently, increasing H reduces $\sqrt { - \frac { a } { 3 } }$ and thereby enlarges $\kappa _ { m }$ . A similar analogy holds for decreasing $| | \mathbf { w } _ { m } | | _ { 2 }$ , which likewise results in an increase of $\kappa _ { m }$

![](images/b4bfd441a67b1a4a40e5db9912c425e42edb7e9cada05065e399a027f7efc861.jpg)

Fig. 5. Variation of $\kappa _ { m }$ as a function of the aerial-active-RIS altitude and the 2D source-UAV distance with $h _ { m } = 4 5$ m.  
![](images/a05d41c5159a1d53c08fe0fdb0c619b27e975e353cc8d5ff2be7921c35344fb7.jpg)  
(a)

![](images/c6220209ba006c77643c814c6ced06b194a3fca771cf0463f610a6bd4bc291f3.jpg)  
(b)  
Fig. 6. Behavior of (a) $\alpha ^ { * 2 }$ with $\alpha _ { \mathrm { m a x } } ^ { 2 } = 4 0$ dB with respect to the height of aerial-RIS and the source-UAV 2D distance and (b) optimal total power with respect to $\alpha ^ { 2 }$ with minimum at $\alpha ^ { * 2 }$

Fig. 6(a) and (b) show the behavior of $\alpha ^ { * 2 }$ according to H and $| | \mathbf { w } _ { m } | | _ { 2 } ,$ and the optimal total power (obj) with respect to $\alpha ^ { 2 }$ with minimum at $\alpha ^ { * 2 }$ , respectively. As shown in (a), as H and $| | \mathbf { w } _ { m } | | _ { 2 }$ increase, $\alpha ^ { * 2 }$ exhibits a rising trend, which is clear since increase in H and ${ \big | } { \big | } \mathbf { w } _ { m } { \big | } { \big | } _ { 2 }$ leads to farther link distance, which leads to stronger reflection compared to low H and $| | \mathbf { w } _ { m } | | _ { 2 }$ . This also can be found in (71), where increase of H and $\lVert \mathbf { w } _ { m } \rVert ;$ <sub>2</sub> leads to the increase of $\begin{array} { r } { \sum _ { m \in \mathbb { M } } \Omega _ { 0 } \left| \left| \pmb { \rho } _ { \mathrm { R I S } } \right| \right| _ { 2 } ^ { 2 } \left| \left| \pmb { \rho } _ { \mathrm { R I S } } - \pmb { \rho } _ { m } \right| \right| _ { 2 } ^ { 2 } } \end{array}$ . Moreover, we, in (b), can check the optimality of $\alpha ^ { * 2 }$ , where the global minimum can be achieved in $\alpha ^ { * 2 }$ with minimum total power given in obj and (69). Consequently, if $\alpha ^ { * 2 }$ exceeds the threshold of 40 dB, we select $\alpha ^ { * }$ by $\alpha ^ { * 2 } = 4 0$ dB as the optimum. From this point onward, we set $\alpha ^ { 2 } = \left( \alpha ^ { * 2 } 1 0 ^ { \frac { \Delta _ { 0 } } { 1 0 } } \right)$ dB as a reference for comparing the non-optimality with respect to $\alpha ^ { 2 } = \alpha ^ { * 2 }$

## D. Comparison of Total Power Under Various Conditions

Fig. 7(a) illustrates the total power according to the distance of $\pmb { \rho } _ { \mathcal { G } }$ from the source $( d _ { \mathcal { G } } )$ with the implementation of active-RIS. Here, the performance gain by our proposed algorithm with $\alpha ^ { 2 } = \alpha ^ { * 2 }$ is approximately given by 32.20 and 30.17 dB for the distance 800 and 1200 m, respectively, which stably ensures almost 30 dB performance compared to total power of aerial-passive-RIS. It is also clear that $d _ { \mathcal { G } }$ leads to the increase of total power, owing to the increase of path loss and probability to adopt the full-array scenario [45]. Moreover, as $d _ { \mathcal { G } }$ increases, the power growth rate of the aerial-active-RIS becomes greater than that of the aerial-passive-RIS, which is shown by decrease in performance gain. It is because at longer distances, $\alpha ^ { * }$ becomes stronger, which also leads to an increase in both amplification power and dynamic noise which leads to the increase of total power.

![](images/f83375257c7cc7c8d6b31c3c2dc31141546f010443274607be8dcb86addb6e6c.jpg)  
(a)

![](images/03b74e90e7a123111ceb8acb3441caf9f8ede432ae4e56d0fa2dc78a48d6e632.jpg)  
(b)

![](images/f951b6e4c10172c23f732599bfb8740a57d683e36e39bf632cadeaabcf1c11f4.jpg)  
(c)  
Fig. 7. Total power with respect to (a) the distance of $\mathbf { \rho } _ { \pmb { \rho } _ { \mathcal { G } } }$ from the source (b) the height of aerial-RIS (c) the number of RIS elements under the implementation of proposed aerial-active-RIS with benchmarks.

We can also notice that the difference in total power between $\alpha ^ { 2 } = \alpha ^ { * 2 }$ and $\left( \alpha ^ { * 2 } 1 0 ^ { \frac { \Delta _ { 0 } } { 1 0 } } \right)$ dB with $\Delta _ { 0 } = - 5$ decreases from 3.79 to 1.52 dB for the distance of 800 to 1200 m, respectively, which implies the dependence on α near $\alpha ^ { * }$ decreases when $d _ { \mathcal { G } }$ increases. We can analyze this phenomenon by taking the natural log of (69) by $p ( \alpha ) \ { \mathrm { ( i . e . , ~ } } p ( \alpha ) = \ln ( \mathrm { o b j ) } )$ ), and considering

$$
p ( { \boldsymbol { \alpha } } ^ { * } ( 1 + \epsilon ) ) - p ( { \boldsymbol { \alpha } } ^ { * } ) , { } ^ { 7 }\tag{55}
$$

for small $\epsilon . ^ { \mathrm { ~ 8 ~ } }$ It is evident that a smaller value of (55) indicates a weaker sensitivity to α in the vicinity of $\alpha ^ { * }$ , in terms of dB.

Hence, by directly computing (55) we can get (56), shown at the bottom of the page. From (56), it is clear that as $d _ { \mathcal { G } }$ increases, $| | \pmb { \rho } _ { \mathrm { R I S } } \ - \ \pmb { \rho } _ { m } | | _ { 2 } ^ { 2 }$ also increases, causing the RHS of (56) to approach 0. Conversely, when $d _ { \mathcal { G } }$ decreases, the argument inside the logarithm approaches $\bar { \frac { 1 } { 2 } } \Bigl ( \left( 1 + \epsilon \right) ^ { 2 } + \left( 1 + \epsilon \right) ^ { - 2 } \Bigr ) > 1$ . Therefore, we can conclude that an increase in $d _ { \mathcal { G } }$ implies a reduced dependency on α in dB for the total power in dBm.

Fig. 7(b) illustrates the total power according to feasible H with the guarantee of high LoS probability [7], [8]. Clearly, by applying our algorithm with $\bar { \alpha } ^ { 2 } = \alpha ^ { * 2 }$ , for increase of $H \ = \ 1 6 0 \ \mathrm { ~ t o ~ } \ 1 9 0 \ \mathrm { ~ m ~ }$ , we can reduce the total power by approximately 31.87 and 31.28 dB, respectively, compared to the passive-RIS-equipped benchmark algorithms. Similar to the scenario illustrated in Fig. 7, an increase in H results in a greater distance between the UAV-BS and the aerial-RIS, which leads to, similar to Fig. 7, the decrease of performance gain. Furthermore, by applying the same reasoning to the RHS of (56), and noting that $| | \pmb { \rho } _ { \mathrm { R I S } } | | _ { 2 } ^ { 2 } , | | \pmb { \rho } _ { \mathrm { R I S } } - \pmb { \rho } _ { m } | | _ { 2 } ^ { 2 } \sim \mathcal { O } ( H ^ { 2 } )$ it follows that both the numerator and denominator of the RHS of (56) scale as $\mathcal { O } ( H ^ { 2 } )$ , which implies that the RHS of (56) scales as O(1) with respect to H. This indicates that the variation in total power, measured in dBm, with respect to α in dB remains nearly constant with increasing H, which is also shown in Fig. 7(b).

Fig. 7(c) shows the total power with respect to the number of active-RIS elements (N ). Note that in particular, the N - dependent circuit-related term appears as $( \alpha ^ { 2 } \sigma _ { \mathrm { a } } ^ { 2 } + P _ { \mathrm { E } } ) N$ whereas the remaining dominant terms in obj scale as O(1) with respect to N [45]. As a result, we can observe that the power increases in large scale of N. Nevertheless, the RIS is modeled as a ULA, to avoid illustrating unrealistic regimes with excessively large arrays, we therefore restrict $N$ to a feasible range, which is the left-side of Fig. 7(c). As shown in the figure, although considering the reflection power $P _ { \mathrm { R } }$ and power consumption by active hardware NP<sub>E</sub>, the proposed method with aerial-active-RIS greatly reduces the power, where the performance gain by our proposed algorithm with $\alpha ^ { 2 } = \bar { \alpha ^ { * 2 } }$ is approximately given by 36.11 and 30.98 dB for $ { N _ { \mathrm { ~ \scriptsize ~ = ~ } 1 2 0 } }$ and 300, respectively. In addition, we can notice that the difference of total power in dB between passive and active-RIS scenario is in first (small N) large enough, and gradually gets smaller in given range of the number of RIS elements. It is because when N is small, obj is asymptotically obj $\sim \ \sum _ { m \in \mathbb { M } } P _ { m }$ , and by applying $N \  \ 0$ to (25), $P _ { m }$ goes to $\alpha ^ { - 2 } P _ { m , \mathrm { p } }$ [45]. By combining those aspects, it is clear that the total power gain between aerial-active- and passive-RIS goes to $\alpha ^ { 2 } .$ , and by increasing N, the impact of the dynamic noise $\alpha ^ { 2 } N \sigma _ { \mathrm { a } } ^ { 2 } ,$ , the active-RIS-reflection power $\alpha ^ { 2 } N \bar { M } \beta _ { \mathrm { s } } G _ { \mathrm { s } } \sum _ { m \in \mathbb { M } } P _ { m }$ , and the active-circuit-dissipated power NP is added to $\textstyle \sum _ { m \in \mathbb { M } } P _ { m }$

$$
\begin{array}{c} \begin{array} { r l } & { p ( \alpha ^ { * } ( 1 + \epsilon ) ) - p ( \alpha ^ { * } ) } \\ & { = \ln ( \frac { ( \frac { ( ( 1 + \epsilon ) ^ { 2 } + ( 1 + \epsilon ) ^ { - 2 } ) \sqrt { ( N \sigma _ { \mathrm { a } } ^ { 2 } + \sum _ { m \in \mathbb { M } } \Omega _ { 0 } \Omega _ { 1 } \Omega _ { 2 } ) ( \sum _ { m \in \mathbb { M } } \Omega _ { 0 } \| \rho _ { \mathrm { R I S } } \| _ { 2 } ^ { 2 } \| \rho _ { \mathrm { R I S } } - \rho _ { m } \| _ { 2 } ^ { 2 } ) } } { 2 \sqrt { ( N \sigma _ { \mathrm { a } } ^ { 2 } + \sum _ { m \in \mathbb { M } } \Omega _ { 0 } \Omega _ { 1 } \Omega _ { 2 } ) ( \sum _ { m \in \mathbb { M } } \Omega _ { 0 } \| \rho _ { \mathrm { R I S } } - \rho _ { m } \| _ { 2 } ^ { 2 } \| \rho _ { \mathrm { R I S } } - \rho _ { m } \| _ { 2 } ^ { 2 } ) } } + } \\ & { + \sum _ { m \in \mathbb { M } } ( \Omega _ { 0 } \| \rho _ { \mathrm { R I S } } \| _ { 2 } ^ { 2 } \Omega _ { 2 } + \Omega _ { 0 } \| \rho _ { \mathrm { R I S } } - \rho _ { m } \| _ { 2 } ^ { 2 } \Omega _ { 1 } ) + N P _ { \mathrm { E } } } \end{array} ) . } \end{array}\tag{56}
$$

![](images/ec7eb1bad21d4d7fae1e132af9358fda3f7fac73209e42e13dd687bde0f6eb6b.jpg)

Fig. 8. Behavior of RHS<sub>2</sub> in (29) with respect to the height of aerial-RIS and the number of active-RIS elements.  
![](images/e4356b61479461c4a9eea2b2be49b7dc139970eae1a39fc7b95babe7d500cdae.jpg)  
Fig. 9. Illustration of (60) in Theorem 1: orthogonal projection of $\mathbf { q } _ { m }$

and formulate obj, affects to the increase of total power in combined way and the gain is becoming less than $\bar  ( \alpha ^ { 2 }$ . Furthermore, both the numerator and the denominator of RHS of (56) scales as $\mathcal { O } \left( \sqrt { ( N + N ^ { 2 } g ^ { - 1 } ) g ^ { - 1 } } + N g ^ { - 1 } + N \right)$ , which also implies that (56) scales with O(1) with respect to $N$ . This suggests that the total power perturbation from $\alpha ^ { * }$ to $\alpha ^ { * } + d$ in dBm stays constant with N , as illustrated in Fig. 7(c).

Fig. 8 shows the behavior of ${ \mathrm { R H S } } _ { 2 }$ in (29), which is the upper-bound of source transmit power $\textstyle \sum _ { m \in \mathbb { M } } P _ { m }$ . From the given figure, the expression

$$
\alpha ^ { * - 2 } G _ { \mathrm { s } } ^ { - 1 } N ^ { - 1 } M ^ { - 1 } \beta _ { \mathrm { s } } ^ { - 1 } \left( P _ { \mathrm { m a x , a } } - N P _ { \mathrm { E } } - \alpha ^ { * 2 } N \sigma _ { \mathrm { a } } ^ { 2 } \right)\tag{57}
$$

in ${ \mathrm { R H S } } _ { 2 }$ decreases as H and N decrease, where the reduction is primarily due to the term $N ^ { - 1 } \beta _ { \mathrm { s } } ^ { - 1 }$ . Meanwhile, the term $G _ { \mathrm { s } } ^ { - 1 } P _ { \mathrm { m a x } }$ remains nearly constant, as it is almost a constant under the assumption that the antenna beamforming at the ground backhaul source is almost perfectly aligned with the aerial-active-RIS [78], [79], [80]. Moreover, the upper-bound is observed to be in range of 12 ∼ 15 dBm. Meanwhile, the total power in the simulations (obj), presented in Fig. $\mathrm { \nabla \tilde { \eta } ( a ) \sim ( c ) }$ almost surely remains below 10 dBm, which is strictly larger than the source transmit power:

$$
\begin{array} { l } { \displaystyle \mathrm { o b j } \triangleq \left( 1 + \alpha ^ { 2 } N M \beta _ { \mathrm { s } } G _ { \mathrm { s } } \right) \sum _ { m \in \mathbb { M } } P _ { m } + \alpha ^ { 2 } N \sigma _ { \mathrm { a } } ^ { 2 } + N P _ { \mathrm { E } } } \\ { \displaystyle \qquad > \sum _ { m \in \mathbb { M } } P _ { m } . \qquad ( } \end{array}\tag{58}
$$

Hence, we can observe that it leads to the fact that $\textstyle \sum _ { m \in \mathbb { M } } P _ { m }$ also stays below 10 dBm, which does not exceeds the ${ \mathrm { R H S } } _ { 2 }$

that are computed in Fig. 8. This equivalently indicates that the proposed system remains within the feasible region defined by RHS<sub>2</sub> in (29).

## V. CONCLUSION

In this paper, we proposed a novel aerial-active-RIS-assisted backhaul architecture to enable energy-efficient full 3D coverage for UAV-BS backhaul networks in 6G. We derived the minimum total power required for backhauling UAV-BSs under target data rate constraints and showed that equal amplification gain is an effective strategy for maximizing energy-efficiency. By employing a practical aerial-active-RIS signal model and accounting for active-RIS-induced dynamic noise, we optimized the placement, array configuration, amplification gain, and phase of the aerial-active-RIS. Simulation results validated the effectiveness of the proposed method, demonstrating significant energy-efficiency improvements over benchmarks and highlighting its strong potential for delivering reliable and scalable 3D backhaul coverage in 6G.

## APPENDIX A PROOF OF THEOREM 1

Let $\bar { \mathbf q } _ { m }$ be the orthogonal projection of ${ \bf q } _ { m }$ onto the line segment connecting the source and $\mathbf { w } _ { m }$ . Thereafter, the following holds:

$$
\left\{ \begin{array} { l l } { \left\| \mathbf { q } _ { m } - \mathbf { w } _ { m } \right\| _ { 2 } ^ { 2 } = \left\| \mathbf { q } _ { m } - \bar { \mathbf { q } } _ { m } \right\| _ { 2 } ^ { 2 } + \left\| \bar { \mathbf { q } } _ { m } - \mathbf { w } _ { m } \right\| _ { 2 } ^ { 2 } } \\ { \left\| \mathbf { q } _ { m } \right\| _ { 2 } ^ { 2 } = \left\| \mathbf { q } _ { m } - \bar { \mathbf { q } } _ { m } \right\| _ { 2 } ^ { 2 } + \left\| \bar { \mathbf { q } } _ { m } \right\| _ { 2 } ^ { 2 } . } \end{array} \right.\tag{59}
$$

To minimize the objective in (33), it is necessary to minimize the left-hand side in (59). Consequently, $\mathbf { q } _ { m }$ should satisfy:

$$
\| \mathbf { q } _ { m } - \bar { \mathbf { q } } _ { m } \| _ { 2 } ^ { 2 } = 0  \mathbf { q } _ { m } = \kappa _ { m } \mathbf { w } _ { m } \ ( \kappa _ { m } > 0 ) ,\tag{60}
$$

which is clarified in Fig. 9. Hence, by substituting (60) we can denote the objective of (33) by $g \left( \kappa _ { m } \right)$ , that is:

$$
g \left( \kappa _ { m } \right) \triangleq | | \mathbf { w } _ { m } | | _ { 2 } ^ { 4 } \left( \kappa _ { m } ^ { 2 } + \zeta _ { 1 } ^ { 2 } + \bar { \Omega } _ { 1 } \right) \left( \left( 1 - \kappa _ { m } \right) ^ { 2 } + \zeta _ { 2 } ^ { 2 } + \bar { \Omega } _ { 2 } \right) ,
$$

where

(61)

$$
\zeta _ { 1 } = \frac { H } { \vert \vert \mathbf { w } _ { m } \vert \vert _ { 2 } } , \zeta _ { 2 } = \frac { \vert H - h _ { m } \vert } { \vert \vert \mathbf { w } _ { m } \vert \vert _ { 2 } } , \bar { \boldsymbol { \Omega } } _ { i } = \vert \vert \mathbf { w } _ { m } \vert \vert _ { 2 } ^ { - 2 } \tilde { \boldsymbol { \Omega } } _ { i } ~ ( i = 1 , 2 ) .\tag{62}
$$

To find the minimum of $g$ at $\kappa _ { m } ~ > ~ 0$ , we have to solve $g ^ { \prime } ( \kappa _ { m } ) = 0 .$ . The discriminant $\Delta$ of the cubic equation $g ^ { \prime } \left( \kappa _ { m } \right) = 0$ is given by $\Delta ~ = ~ \left( { \textstyle { \frac { a } { 3 } } } \right) ^ { 3 } + { \bigl ( { \frac { b } { 2 } } \bigr ) } ^ { 2 }$ [81], where $\begin{array} { r } { a = \frac { 1 } { 2 } \left( \zeta _ { 1 } ^ { 2 } + \zeta _ { 2 } ^ { 2 } + \bar { \Omega } _ { 1 } + \bar { \Omega } _ { 2 } \right) - \frac { 1 } { 4 } , b = \frac { 1 } { 4 } \left( \zeta _ { 2 } ^ { 2 } - \bar { \zeta } _ { 1 } ^ { 2 } + \bar { \Omega } _ { 2 } - \bar { \Omega } _ { 1 } \right) } \end{array}$ For the range of a and b, we can assume the followings:

1) Since we assume that $d _ { \mathcal { G } }$ is sufficiently large, $| | \mathbf { w } _ { m } | | _ { 2 }$ follows a similar scale. In this paper, we will assume the scale with $1 0 ^ { 3 }$ m, which is also reflected in the simulation in Section IV and Table I.

2) $\beta _ { 0 } \approx - 4 3 . 3$ dB for sub-6 GHz backhaul (gets larger for higher-frequency applications in 6G [17], [82], [83]).

3) Feasible $\alpha _ { \mathrm { m a x } } ^ { 2 }$ is given by less than 40 dB [27], [28].

4) $G _ { \mathrm { s } } \leq G _ { \mathrm { m a x } } = 8$ dB in Table I.

5) We assume that M and N has a scale of approximately a few or less than ten and few hundred, respectively: M = 16, N ∈ [100, 400] [27], [45], [62]

$$
\begin{array} { r l } & { \Bigl ( 1 + \alpha ^ { 2 } N M \beta _ { s } G _ { s } \Bigr ) \underset { m \in \mathbb { M } } { \sum } P _ { m } + \alpha ^ { 2 } N \sigma _ { s } ^ { 2 } + N P _ { \mathbb { E } } } \\ & { \geq 2 \sqrt { ( N \sigma _ { \mathrm { a } } ^ { 2 } + \underset { m \in \mathbb { M } } { \sum } \Omega _ { 0 } \Omega _ { 1 } \Omega _ { 2 } ) ( \underset { m \in \mathbb { K } } { \sum } \Omega _ { 0 } | \rho _ { \mathrm { R I S } } | | _ { 2 } ^ { 2 } | \rho _ { \mathrm { R I S } } - \rho _ { m } | | _ { 2 } ^ { 2 } ) } + \underset { m \in \mathbb { M } } { \sum } \Bigl ( \Omega _ { 0 } | | \rho _ { \mathrm { R I S } } | | _ { 2 } ^ { 2 } \Omega _ { 2 } + \Omega _ { 0 } | | \rho _ { \mathrm { R I S } } - \rho _ { m } | | _ { 2 } ^ { 2 } \Omega _ { 1 } \Bigr ) + N P _ { \mathbb { F } } . } \end{array}\tag{70}
$$

6) $\sigma _ { \mathrm { a } } ^ { 2 }$ and $\sigma ^ { 2 }$ has the similar scale [28], [32]. Therefore, we can assume that

$$
\begin{array} { r l } & { \zeta _ { i } \ll 1 \ ( i = 1 , 2 ) } \\ & { \bar { \Omega } _ { 1 } = \alpha ^ { 2 } N M \beta _ { 0 } G _ { \mathrm { s } } | | \mathbf { w } | | _ { 2 } ^ { - 2 } \ll 1 , } \\ & { \bar { \Omega } _ { 2 } = \alpha ^ { 2 } \frac { \sigma _ { \mathrm { a } } ^ { 2 } } { \sigma ^ { 2 } } N \beta _ { 0 } | | \mathbf { w } _ { m } | | _ { 2 } ^ { - 2 } \ll 1 , } \end{array}\tag{63}
$$

which also leads to $\begin{array} { r } { a < 0 \left( \approx - \frac { 1 } { 4 } \right) } \end{array}$ and $\left| b \right| \ll 1$ . Hence, we can deduce $\Delta < 0$ , which leads to three real solutions $\left\{ \kappa _ { m , k } \right\} _ { k = 0 } ^ { 2 }$ of $g ^ { \prime } \left( \kappa _ { m } \right) = 0 ~ [ 8 1 ] ^ { \prime }$

$$
\begin{array} { c c } { \kappa _ { m , k } = \displaystyle \frac { 1 } { 2 } + 2 \sqrt { - \frac { a } { 3 } } \cos \left( \frac { 1 } { 3 } \cos ^ { - 1 } \left( \frac { 3 b } { 2 a } \sqrt { - \frac { 3 } { a } } \right) - \frac { 2 } { 3 } \pi k \right) } \\ { ( k = 0 , 1 , 2 ) . } \end{array}\tag{4}
$$

Since $\begin{array} { l } { { a \ \approx \ - \frac { 1 } { 4 } } } \end{array}$ and $| b | \ll 1$ , we define ${ \frac { 3 b } { 2 a } } { \sqrt { - { \frac { 3 } { a } } } } = \epsilon$ with $| \epsilon | \ll 1$ . By successively applying the first-order Taylor approximation to (64), the expression reduces to

$$
\left\{ \begin{array} { l l } { \displaystyle \kappa _ { m , 0 } \approx \frac { 1 } { 2 } + \sqrt { - a } \left( 1 + \frac { \epsilon } { 3 \sqrt { 3 } } \right) } & \\ { \displaystyle \kappa _ { m , 1 } \approx \frac { 1 } { 2 } + \sqrt { - a } \left( - \frac { \epsilon } { 3 \sqrt { 3 } } \right) } & \\ { \displaystyle \kappa _ { m , 2 } \approx \frac { 1 } { 2 } + \sqrt { - a } \left( - 1 + \frac { \epsilon } { 3 \sqrt { 3 } } \right) . } \end{array} \right.\tag{65}
$$

By substituting $\begin{array} { r } { a = \frac { 1 } { 2 } \left( \zeta _ { 1 } ^ { 2 } + \zeta _ { 2 } ^ { 2 } + \bar { \Omega } _ { 1 } + \bar { \Omega } _ { 2 } \right) - \frac { 1 } { 4 } } \end{array}$ , (65) becomes

$$
\left\{ \begin{array} { l l } { \kappa _ { m , 0 } \approx \displaystyle \frac { 1 } { 2 } - \sqrt { \frac { 1 } { 4 } - \frac { 1 } { 2 } \left( \zeta _ { 1 } ^ { 2 } + \zeta _ { 2 } ^ { 2 } + \bar { \Omega } _ { 1 } + \bar { \Omega } _ { 2 } \right) } \left( - 1 - \frac { \epsilon } { 3 \sqrt { 3 } } \right) } \\ { \kappa _ { m , 1 } \approx \displaystyle \frac { 1 } { 2 } - \sqrt { \frac { 1 } { 4 } - \frac { 1 } { 2 } \left( \zeta _ { 1 } ^ { 2 } + \zeta _ { 2 } ^ { 2 } + \bar { \Omega } _ { 1 } + \bar { \Omega } _ { 2 } \right) } \left( \frac { \epsilon } { 3 \sqrt { 3 } } \right) } \\ { \kappa _ { m , 2 } \approx \displaystyle \frac { 1 } { 2 } - \sqrt { \frac { 1 } { 4 } - \frac { 1 } { 2 } \left( \zeta _ { 1 } ^ { 2 } + \zeta _ { 2 } ^ { 2 } + \bar { \Omega } _ { 1 } + \bar { \Omega } _ { 2 } \right) } \left( 1 - \frac { \epsilon } { 3 \sqrt { 3 } } \right) . } \end{array} \right.\tag{66}
$$

From (66), we can derive the following outcomes:

1) It is evident that $\kappa _ { m , 0 } > \kappa _ { m , 1 } > \kappa _ { m , 2 } ( \cdot _ { \cdot } | \epsilon | \ll 1 )$

2) By the properties of the quartic equation [81], g has two local minimum: $\kappa _ { m , 0 }$ and $\kappa _ { m , 2 }$ , with one of them being the global minimum.

3) Using $| \epsilon | \ll 1$ , we can deduce the following for $\kappa _ { m , 2 } \mathrm { : }$

$$
\begin{array} { c } { \displaystyle \kappa _ { m , 2 } \approx \frac { 1 } { 2 } - \sqrt { \frac { 1 } { 4 } - \frac { 1 } { 2 } \left( \zeta _ { 1 } ^ { 2 } + \zeta _ { 2 } ^ { 2 } + \bar { \Omega } _ { 1 } + \bar { \Omega } _ { 2 } \right) } \left( 1 \right) } \\ { \displaystyle = \frac { \frac { 1 } { 2 } \left( \zeta _ { 1 } ^ { 2 } + \zeta _ { 2 } ^ { 2 } + \bar { \Omega } _ { 1 } + \bar { \Omega } _ { 2 } \right) } { \sqrt { \frac { 1 } { 4 } + \frac { 1 } { 2 } \left( \zeta _ { 1 } ^ { 2 } + \zeta _ { 2 } ^ { 2 } + \bar { \Omega } _ { 1 } + \bar { \Omega } _ { 2 } \right) } } > 0 . } \end{array}\tag{67}
$$

Furthermore, as $\zeta _ { 1 }$ and $\zeta _ { 2 }$ are sufficiently small (owing to the sufficiently large $| | \mathbf { w } _ { m } | | _ { 2 } ) .$ , it follows from (67) that $\kappa _ { m , 2 }$ should be close to the origin.

Hence, we should select $\kappa _ { m }$ as

$$
\begin{array} { l } { \displaystyle \kappa _ { m } \triangleq \kappa _ { m , 2 } } \\ { \displaystyle = \frac { 1 } { 2 } + 2 \sqrt { - \frac { a } { 3 } } \cos \left( \frac { 1 } { 3 } \cos ^ { - 1 } \left( \frac { 3 b } { 2 a } \sqrt { - \frac { 3 } { a } } \right) - \frac { 4 } { 3 } \pi \right) . } \end{array}\tag{68}
$$

By determining $\begin{array} { c c l } { \mathbf q _ { m } ^ { * } } & { = } & { \kappa _ { m } \mathbf w _ { m } } \end{array}$ accordingly, the theorem follows.

APPENDIX B PROOF OF THEOREM 2

For given $\mathbf { q } ^ { * } , \{ \bar { N } \} , \bar { \pmb { \rho } } \ ( \mathrm { o r } \ \{ \bar { \pmb { \rho } } _ { i } ^ { * } \} _ { i = 1 } ^ { L } ) , \mathbf { \Theta } ^ { }$ , obj in (29) becomes

$$
\begin{array} { r l } & { \displaystyle \left( 1 + \alpha ^ { 2 } N M \beta _ { \mathrm { s } } G _ { \mathrm { s } } \right) \sum _ { m \in \mathbb { H } } P _ { m } + \alpha ^ { 2 } N \sigma _ { \mathrm { a } } ^ { 2 } + N P _ { \mathrm { E } } ( \triangleq \mathrm { b } \mathrm { b } ) } \\ & { \displaystyle = \left( N \sigma _ { \mathrm { a } } ^ { 2 } + \sum _ { m \in \mathbb { M } } \Omega _ { 0 } \Omega _ { 1 } \Omega _ { 2 } \right) \alpha ^ { 2 } } \\ & { \quad + \left( \sum _ { m \in \mathbb { M } } \Omega _ { 0 } | | \rho _ { \mathrm { R I S } } | | _ { 2 } ^ { 2 } | | \rho _ { \mathrm { R I S } } - \rho _ { m } | | _ { 2 } ^ { 2 } \right) \alpha ^ { - 2 } } \\ & { \quad + \displaystyle \sum _ { m \in \mathbb { H } } \left( \Omega _ { 0 } | | \rho _ { \mathrm { R I S } } | | _ { 2 } ^ { 2 } \Omega _ { 2 } + \Omega _ { 0 } | | \rho _ { \mathrm { R I S } } - \rho _ { m } | | _ { 2 } ^ { 2 } \Omega _ { 1 } \right) + N P _ { \mathrm { E } } , } \end{array}\tag{69}
$$

Hence, we can derive the optimal α by applying the Arithmetic-Geometric Mean inequality, which becomes (70), shown at the top of the page.

Therefore, by the equality condition of (70), we can deduce the optimal $\alpha ^ { * }$ as

$$
\alpha ^ { * } = \operatorname* { m i n } \left\{ \sqrt [ 4 ] { \frac { \sum _ { m \in \mathbb { M } } \Omega _ { 0 } \left| \left| \pmb { \rho } _ { \mathrm { R I S } } \right| \right| _ { 2 } ^ { 2 } \left| \left| \pmb { \rho } _ { \mathrm { R I S } } - \pmb { \rho } _ { m } \right| \right| _ { 2 } ^ { 2 } } { N \sigma _ { \mathrm { a } } ^ { 2 } + \sum _ { m \in \mathbb { M } } \Omega _ { 0 } \Omega _ { 1 } \Omega _ { 2 } } } , \alpha _ { \operatorname* { m a x } } \right\} ,\tag{71}
$$

and the theorem follows.

## REFERENCES

[1] H.-B. Jeon and C.-B. Chae, “Energy-efficient aerial-RIS deployment for 6G,” in Proc. 13th Int. Conf. Inf. Commun. Technol. Converg. (ICTC), Oct. 2022, pp. 199–201.

[2] B. Smida, A. Sabharwal, G. Fodor, G. C. Alexandropoulos, H. A. Suraweera, and C.-B. Chae, “Full-duplex wireless for 6G: Progress brings new opportunities and challenges,” IEEE J. Sel. Areas Commun., vol. 41, no. 9, pp. 2729–2750, Sep. 2023.

[3] E. Bjornson et al., “Towards 6G MIMO: Massive spatial multiplexing,¨ dense arrays, and interplay between electromagnetics and processing,” 2024, arXiv:2401.02844.

[4] Y. Kim, H.-J. Moon, H. Yoo, B. Kim, K.-K. Wong, and C.-B. Chae, “A state-of-the-art survey on full-duplex network design,” Proc. IEEE, vol. 112, no. 5, pp. 463–486, May 2024.

[5] M. Giordani and M. Zorzi, “Non-terrestrial networks in the 6G era: Challenges and opportunities,” IEEE Netw., vol. 35, no. 2, pp. 244–251, Mar. 2021.

[6] M. Mozaffari, W. Saad, M. Bennis, Y.-H. Nam, and M. Debbah, “A tutorial on UAVs for wireless networks: Applications, challenges, and open problems,” IEEE Commun. Surveys Tuts., vol. 21, no. 3, pp. 2334–2360, 3rd Quart., 2019.

[7] A. Al-Hourani, S. Kandeepan, and A. Jamalipour, “Modeling air-toground path loss for low altitude platforms in urban environments,” in Proc. IEEE Global Commun. Conf., Dec. 2014, pp. 2898–2904.

[8] S.-C. Noh, H.-B. Jeon, and C.-B. Chae, “Energy-efficient deployment of multiple UAVs using ellipse clustering to establish base stations,” IEEE Wireless Commun. Lett., vol. 9, no. 8, pp. 1155–1159, Aug. 2020.

[9] Y. Zhang, M. A. Kishk, and M.-S. Alouini, “Deployment optimization of tethered drone-assisted integrated access and backhaul networks,” IEEE Trans. Wireless Commun., vol. 23, no. 4, pp. 2668–2680, Apr. 2024.

[10] C. Diaz-Vilor, A. Lozano, and H. Jafarkhani, “Cell-free UAV networks: Asymptotic analysis and deployment optimization,” IEEE Trans. Wireless Commun., vol. 22, no. 5, pp. 3055–3070, May 2023.

[11] H.-J. Moon, C.-B. Chae, K.-K. Wong, and M.-S. Alouini, “A generalized pointing error model for FSO links with fixed-wing UAVs for 6G: Analysis and trajectory optimization,” IEEE Trans. Wireless Commun., vol. 24, no. 7, pp. 5723–5737, Jul. 2025.

[12] X. Guan, K.-F.-C. Yiu, B. Li, Y. Zeng, and R. Zhang, “3D trajectory optimization for fixed-wing UAV communications with full UAV dynamics,” IEEE Trans. Veh. Technol., vol. 74, no. 10, pp. 15401–15415, Oct. 2025.

[13] H.-J. Moon and C.-B. Chae, “Cooperative ground-satellite scheduling and power allocation for urban air mobility networks,” IEEE J. Sel. Areas Commun., vol. 43, no. 1, pp. 218–233, Jan. 2025.

[14] H. Xiao, X. Hu, W. Zhang, W. Wang, K.-K. Wong, and K. Yang, “Energy-efficient STAR-RIS enhanced UAV-enabled MEC networks with bi-directional task offloading,” IEEE Trans. Wireless Commun., vol. 24, no. 4, pp. 3258–3272, Apr. 2025.

[15] H.-B. Jeon et al., “Free-space optical communications for 6G wireless networks: Challenges, opportunities, and prototype validation,” IEEE Commun. Mag., vol. 61, no. 4, pp. 116–121, Apr. 2023.

[16] Y. Kim, K.-K. Wong, J. Zhang, and C.-B. Chae, “Low complexity frequency domain nonlinear self-interference cancellation for flexible duplex,” IEEE Trans. Wireless Commun., vol. 24, no. 8, pp. 6627–6642, Aug. 2025.

[17] D. Jun, W. Ham, J.-Y. Kwon, W. Hong, C.-B. Chae, and R. W. Heath Jr., “Reconfigurable intelligence surface with potential tunable meta-devices for 6G: Design and system-level evaluation,” IEEE Commun. Standards Mag., vol. 8, no. 4, pp. 32–39, Dec. 2024.

[18] Q. Wu, S. Zhang, B. Zheng, C. You, and R. Zhang, “Intelligent reflecting surface-aided wireless communications: A tutorial,” IEEE Trans. Commun., vol. 69, no. 5, pp. 3313–3351, May 2021.

[19] E. Basar and H. V. Poor, “Present and future of reconfigurable intelligent surface-empowered communications [perspectives],” IEEE Signal Process. Mag., vol. 38, no. 6, pp. 146–152, Nov. 2021.

[20] Y. Liu et al., “Reconfigurable intelligent surfaces: Principles and opportunities,” IEEE Commun. Surveys Tuts., vol. 23, no. 3, pp. 1546–1577, 3rd Quart., 2021.

[21] L. Dai et al., “Reconfigurable intelligent surface-based wireless communications: Antenna design, prototyping, and experimental results,” IEEE Access, vol. 8, pp. 45913–45923, 2020.

[22] J. Sang et al., “Coverage enhancement by deploying RIS in 5G commercial mobile networks: Field trials,” IEEE Wireless Commun., vol. 31, no. 1, pp. 172–180, Feb. 2024.

[23] J. Sang et al., “Multi-scenario broadband channel measurement and modeling for sub-6 GHz RIS-assisted wireless communication systems,” IEEE Trans. Wireless Commun., vol. 23, no. 6, pp. 6312–6329, Jun. 2024.

[24] E. Bjornson,¨ O.<sup>¨</sup> Ozdogan, and E. G. Larsson, “Intelligent reflecting sur-<sup>¨</sup> face versus decode-and-forward: How large surfaces are needed to beat relaying?,” IEEE Wireless Commun. Lett., vol. 9, no. 2, pp. 244–248, Feb. 2020.

[25] M. Di Renzo et al., “Reconfigurable intelligent surfaces vs. relaying: Differences, similarities, and performance comparison,” IEEE Open J. Commun. Soc., vol. 1, pp. 798–807, 2020.

[26] H. Do and N. Lee, “Finding globally optimal configuration of active RIS in linear time,” IEEE Trans. Wireless Commun., vol. 23, no. 12, pp. 18142–18153, Dec. 2024.

[27] Z. Zhang et al., “Active RIS vs. passive RIS: Which will prevail in 6G?,” IEEE Trans. Commun., vol. 71, no. 3, pp. 1707–1725, Mar. 2023.

[28] K. Zhi, C. Pan, H. Ren, K. K. Chai, and M. Elkashlan, “Active RIS versus passive RIS: Which is superior with the same power budget?,” IEEE Commun. Lett., vol. 26, no. 5, pp. 1150–1154, May 2022.

[29] M. Ahmed et al., “Active reconfigurable intelligent surfaces: Expanding the frontiers of wireless communication—A survey,” IEEE Commun. Surveys Tuts., vol. 27, no. 2, pp. 839–869, Apr. 2025.

[30] G. C. Alexandropoulos, N. Shlezinger, and P. del Hougne, “Reconfigurable intelligent surfaces for rich scattering wireless communications: Recent experiments, challenges, and opportunities,” IEEE Commun. Mag., vol. 59, no. 6, pp. 28–34, Jun. 2021.

[31] Q. Zhu, M. Li, R. Liu, Y. Liu, and Q. Liu, “Joint beamforming designs for active reconfigurable intelligent surface: A sub-connected array architecture,” IEEE Trans. Commun., vol. 70, no. 11, pp. 7628–7643, Nov. 2022.

[32] R. Long, Y.-C. Liang, Y. Pei, and E. G. Larsson, “Active reconfigurable intelligent surface-aided wireless communications,” IEEE Trans. Wireless Commun., vol. 20, no. 8, pp. 4962–4975, Aug. 2021.

[33] G. Zhou et al., “A framework for transmission design for active RISaided communication with partial CSI,” IEEE Trans. Wireless Commun., vol. 23, no. 1, pp. 305–320, Jan. 2024.

[34] J. Yang, H. Lee, and J. Choi, “Robust transmission design for active RIS-aided systems,” IEEE Trans. Veh. Technol., vol. 74, no. 7, pp. 11591–11596, Jul. 2025.

[35] J. Liu and H. Zhang, “Throughput optimization in aerial RIS-assisted networks with 3D imperfect reflection,” IEEE Trans. Veh. Technol., vol. 74, no. 7, pp. 10510–10523, Jul. 2025.

[36] H. Lu, Y. Zeng, S. Jin, and R. Zhang, “Aerial intelligent reflecting surface: Joint placement and passive beamforming design with 3D beam flattening,” IEEE Trans. Wireless Commun., vol. 20, no. 7, pp. 4128–4143, Jul. 2021.

[37] B. Xiong, Z. Zhang, C. Pan, and J. Wang, “Performance analysis of aerial RIS auxiliary mmWave mobile communications with UAV fluctuation,” IEEE Wireless Commun. Lett., vol. 13, no. 4, pp. 1183–1187, Apr. 2024.

[38] S. Faramarzi et al., “Meta reinforcement learning for resource allocation in aerial active-RIS-assisted networks with rate-splitting multiple access,” IEEE Internet Things J., vol. 11, no. 15, pp. 26366–26383, Aug. 2024.

[39] J. Zhao, Q. Xu, X. Mu, Y. Liu, and Y. Zhu, “Aerial active STAR-RISaided IoT NOMA networks,” IEEE Internet Things J., vol. 12, no. 8, pp. 9525–9538, Apr. 2025.

[40] D. Wang et al., “Active aerial reconfigurable intelligent surface assisted secure communications: Integrating sensing and positioning,” IEEE J. Sel. Areas Commun., vol. 42, no. 10, pp. 2769–2785, Oct. 2024.

[41] M. Toka et al., “RIS-empowered LEO satellite networks for 6G: Promising usage scenarios and future directions,” IEEE Commun. Mag., vol. 62, no. 11, pp. 128–135, Nov. 2024.

[42] C. A. Balanis, Antenna Theory: Analysis and Design. New York, NY, USA: Wiley, 2016.

[43] C.-C. Lai, A.-H. Tsai, C.-W. Ting, K.-H. Lin, J.-C. Ling, and C.-E. Tsai, “Interference-aware deployment for maximizing user satisfaction in multi-UAV wireless networks,” IEEE Wireless Commun. Lett., vol. 12, no. 7, pp. 1189–1193, Jul. 2023.

[44] W. Mei and R. Zhang, “Aerial-ground interference mitigation for cellular-connected UAV,” IEEE Wireless Commun., vol. 28, no. 1, pp. 167–173, Feb. 2021.

[45] H.-B. Jeon, S.-H. Park, J. Park, K. Huang, and C.-B. Chae, “An energyefficient aerial backhaul system with reconfigurable intelligent surface,” IEEE Trans. Wireless Commun., vol. 21, no. 8, pp. 6478–6494, Aug. 2022.

[46] J. Lei, T. Zhang, X. Mu, and Y. Liu, “NOMA for STAR-RIS assisted UAV networks,” IEEE Trans. Commun., vol. 72, no. 3, pp. 1732–1745, Mar. 2024.

[47] N. Gao, S. Jin, X. Li, and M. Matthaiou, “Aerial RIS-assisted high altitude platform communications,” IEEE Wireless Commun. Lett., vol. 10, no. 10, pp. 2096–2100, Oct. 2021.

[48] W. Chen, L. Bai, W. Tang, S. Jin, W. X. Jiang, and T. J. Cui, “Angledependent phase shifter model for reconfigurable intelligent surfaces: Does the angle-reciprocity hold?,” IEEE Commun. Lett., vol. 24, no. 9, pp. 2060–2064, Sep. 2020.

[49] W. Chen, C.-K. Wen, X. Li, and S. Jin, “Channel customization for joint Tx-RISs-Rx design in hybrid mmWave systems,” IEEE Trans. Wireless Commun., vol. 22, no. 11, pp. 8304–8319, Nov. 2023.

[50] H. Lu, Y. Zeng, S. Jin, and R. Zhang, “Enabling panoramic full-angle reflection via aerial intelligent reflecting surface,” in Proc. IEEE Int. Conf. Commun. Workshops (ICC Workshops), Jun. 2020, pp. 1–6.

[51] X. Yu, H. Liu, S. Gong, W. Shen, J. Zhao, and C. Xing, “Channel estimation for irregular subarrayed RIS-aided mmWave communications,” IEEE Trans. Veh. Technol., vol. 74, no. 11, pp. 17247–17264, Nov. 2025.

[52] S. Chen et al., “Interference suppression for active RIS-empowered array radar using joint beamforming design,” IEEE Trans. Veh. Technol., vol. 74, no. 4, pp. 6222–6238, Apr. 2025.

[53] Calculation of Free-Space Attenuation, document P.525-2, ITU-R, 1994.

[54] L. Wei, C. Huang, G. C. Alexandropoulos, C. Yuen, Z. Zhang, and M. Debbah, “Channel estimation for RIS-empowered multi-user MISO wireless communications,” IEEE Trans. Commun., vol. 69, no. 6, pp. 4144–4157, Jun. 2021.

[55] J. Chen, Y.-C. Liang, H. V. Cheng, and W. Yu, “Channel estimation for reconfigurable intelligent surface aided multi-user mmWave MIMO systems,” IEEE Trans. Wireless Commun., vol. 22, no. 10, pp. 6853–6869, Oct. 2023.

[56] X. Wei, D. Shen, and L. Dai, “Channel estimation for RIS assisted wireless communications—Part II: An improved solution based on double-structured sparsity,” IEEE Commun. Lett., vol. 25, no. 5, pp. 1403–1407, May 2021.

[57] G. Zhou, Z. Peng, C. Pan, and R. Schober, “Individual channel estimation for RIS-aided communication systems—A general framework,” IEEE Trans. Wireless Commun., vol. 23, no. 9, pp. 12038–12053, Sep. 2024.

[58] K. Liu, Z. Zhang, L. Dai, S. Xu, and F. Yang, “Active reconfigurable intelligent surface: Fully-connected or sub-connected?,” IEEE Commun. Lett., vol. 26, no. 1, pp. 167–171, Jan. 2022.

[59] H. Niu et al., “Active RIS assisted rate-splitting multiple access network: Spectral and energy efficiency tradeoff,” IEEE J. Sel. Areas Commun., vol. 41, no. 5, pp. 1452–1467, May 2023.

[60] R. C. Hansen, Phased Array Antennas. Hoboken, NJ, USA: Wiley, 2009.

[61] Study on New Radio Access Technology: Radio Access Architecture and Interfaces, document TR 38.801, 3GPP, Jan. 2016.

[62] C. Huang, A. Zappone, G. C. Alexandropoulos, M. Debbah, and C. Yuen, “Reconfigurable intelligent surfaces for energy efficiency in wireless communication,” IEEE Trans. Wireless Commun., vol. 18, no. 8, pp. 4157–4170, Aug. 2019.

[63] J.-F. Bousquet, S. Magierowski, and G. G. Messier, “A 4-GHz active scatterer in 130-nm CMOS for phase sweep amplify-and-forward,” IEEE Trans. Circuits Syst. I, Reg. Papers, vol. 59, no. 3, pp. 529–540, Mar. 2012.

[64] F. Amato, C. W. Peterson, B. P. Degnan, and G. D. Durgin, “Tunneling RFID tags for long-range and low-power microwave applications,” IEEE J. Radio Freq. Identificat., vol. 2, no. 2, pp. 93–103, Jun. 2018.

[65] Y. Zeng, J. Xu, and R. Zhang, “Energy minimization for wireless communication with rotary-wing UAV,” IEEE Trans. Wireless Commun., vol. 18, no. 4, pp. 2329–2345, Apr. 2019.

[66] K. Miettinen, Nonlinear Multiobjective Optimization. Dordrecht, The Netherlands: Kluwer, 1998.

[67] E. Weiszfeld and F. Plastria, “On the point for which the sum of the distances to n given points is minimum,” Ann. Oper. Res., vol. 167, no. 1, pp. 7–41, Mar. 2009.

[68] A. Beck and S. Sabach, “Weiszfeld’s method: Old and new results,” J. Optim. Theory Appl., vol. 164, no. 1, pp. 1–40, May 2015.

[69] S. Boyd and L. Vandenberghe, Convex Optimization. Cambridge, U.K.: Cambridge Univ. Press, 2004.

[70] A. Zappone and E. Jorswieck, “Energy efficiency in wireless networks via fractional programming theory,” Found. Trends Commun. Inf. Theory, vol. 11, nos. 3–4, pp. 185–396, 2015.

[71] C. Liaskos, S. Nie, A. Tsioliaridou, A. Pitsillides, S. Ioannidis, and I. Akyildiz, “A new wireless communication paradigm through software-controlled metasurfaces,” IEEE Commun. Mag., vol. 56, no. 9, pp. 162–169, Sep. 2018.

[72] Study on Channel Model for Frequencies From 0.5 to 100 GHz, document TR 38.901, 3GPP, Jan. 2020.

[73] H. Kim, C.-B. Chae, G. De Veciana, and R. W. Heath Jr., “A cross-layer approach to energy efficiency for adaptive MIMO systems exploiting spare capacity,” IEEE Trans. Wireless Commun., vol. 8, no. 8, pp. 4264–4275, Aug. 2009.

[74] K. Ntontin, J. Song, and M. Di Renzo, “Multi-antenna relaying and reconfigurable intelligent surfaces: End-to-end SNR and achievable rate,” 2019, arXiv:1908.07967.

[75] A. Zappone, P. Cao, and E. A. Jorswieck, “Energy efficiency optimization in relay-assisted MIMO systems with perfect and statistical CSI,” IEEE Trans. Signal Process., vol. 62, no. 2, pp. 443–457, Jan. 2014.

[76] B. Sainath and N. B. Mehta, “Generalizing the amplify-and-forward relay gain model: An optimal SEP perspective,” IEEE Trans. Wireless Commun., vol. 11, no. 11, pp. 4118–4127, Nov. 2012.

[77] C.-B. Chae, T. Tang, R. W. Heath Jr., and S. Cho, “MIMO relaying with linear processing for multiuser transmission in fixed relay networks,” IEEE Trans. Signal Process., vol. 56, no. 2, pp. 727–738, Feb. 2008.

[78] K. Liang, G. Zheng, Z. Li, K.-K. Wong, and C.-B. Chae, “A data and model-driven deep learning approach to robust downlink beamforming optimization,” IEEE J. Sel. Areas Commun., vol. 42, no. 11, pp. 3278–3292, Nov. 2024.

[79] M. S. Sim, Y.-G. Lim, S. H. Park, L. Dai, and C.-B. Chae, “Deep learning-based mmWave beam selection for 5G NR/6G with sub-6 GHz channel information: Algorithms and prototype validation,” IEEE Access, vol. 8, pp. 51634–51646, 2020.

[80] Q. Deng et al., “Adaptive beam alignment and optimization for IRSaided high-speed UAV communications,” IEEE Trans. Green Commun. Netw., vol. 7, no. 3, pp. 1583–1595, Sep. 2023.

[81] S. Lovett, Abstract Algebra: Structures and Applications. Boca Raton, FL, USA: CRC Press, 2015.

[82] M. R. Castellanos, S. Yang, C.-B. Chae, and R. W. Heath Jr., “Embracing reconfigurable antennas in the tri-hybrid MIMO architecture for 6G and beyond,” IEEE Trans. Commun., vol. 74, pp. 381–401, 2026.

[83] R. W. Heath Jr., J. Carlson, N. V. Deshpande, M. R. Castellanos, M. Akrout, and C.-B. Chae, “The tri-hybrid MIMO architecture,” IEEE Wireless Commun., vol. 33, no. 1, pp. 199–206, Feb. 2026.

![](images/953b94729f37bb749acf2ad34aff41b2b6459015b39c20e5132f13e24c5a9bf5.jpg)

Hong-Bae Jeon (Member, IEEE) received the B.S. degree in electrical and electronic engineering and mathematics and the Ph.D. degree in integrated technology from Yonsei University, Republic of Korea, in 2017 and 2023, respectively. In 2022, he was a Visiting Researcher with The Hong Kong University of Science and Technology (HKUST), Hong Kong. He was with Samsung Electronics, Republic of Korea, in 2024, as a Staff Engineer. He is currently an Assistant Professor with the Department of Information Communications Engineering, Hankuk

University of Foreign Studies (HUFS), Republic of Korea. His research interests include core enabling technologies for 6G, with an emphasis on optimization and signal processing for reconfigurable intelligent surface (RIS), fluid antenna system (FAS), Rydberg atomic receiver (RARE), and radio resource management (RRM). He was a recipient of the Gold Prize in the 27th Samsung HumanTech Paper Award in 2021.

![](images/78db01a025e04531709b44f6aec992fb9ec8a0d69913de8eddb64c653241ccec.jpg)

Chan-Byoung Chae (Fellow, IEEE) received the Ph.D. degree in electrical and computer engineering from The University of Texas at Austin (UT), USA, in 2008. He was a member of the Wireless Networking and Communications Group (WNCG), UT. Prior to joining UT, he was a Research Engineer with the Telecommunications Research and Development Center, Samsung Electronics, Suwon, South Korea, from 2001 to 2005. He is currently an Underwood Distinguished Professor and a Lee Youn Jae Fellow (an Endowed Chair Professor) with the School of

Integrated Technology, Yonsei University, South Korea. Before joining Yonsei University, he was with Bell Labs, Alcatel-Lucent, Murray Hill, NJ, USA, from 2009 to 2011, as a member of the Technical Staff; and Harvard University, Cambridge, MA, USA, from 2008 to 2009, as a Post-Doctoral Fellow and a Lecturer. He is an Elected Member of the National Academy of Engineering of Korea (NAEK). He was a recipient/co-recipient of the Ministry of ICT and Science Award in 2024, the Ministry of Education Award in 2024, the KICS Haedong Scholar Award in 2023, the CES Innovation Award in 2023, the IEEE ICC Best Demo Award in 2022, the IEEE WCNC Best Demo Award in 2020, the Best Young Engineer Award from NAEK in 2019, the IEEE DySPAN Best Demo Award in 2018, the IEEE/KICS Journal of Communications and Networks Best Paper Award in 2018, the IEEE INFOCOM Best Demo Award in 2015, the IEIE/IEEE Joint Award for Young IT Engineer of the Year in 2014, the KICS Haedong Young Scholar Award in 2013, the IEEE Signal Processing Magazine Best Paper Award in 2013, the IEEE ComSoc AP Outstanding Young Researcher Award in 2012, and the IEEE VTS Dan. E. Noble Fellowship Award in 2008. He has held several editorial positions, including the Editor-in-Chief of IEEE TRANSACTIONS ON MOLECULAR, BIOLOGICAL, AND MULTI-SCALE COMMUNICATIONS; a Senior Editor of IEEE WIRELESS COMMUNICATIONS LETTERS; and an Editor of IEEE Communications Magazine, IEEE TRANSACTIONS ON WIRELESS COMMUNICATIONS, and IEEE WIRELESS COMMUNICATIONS LETTERS. He was an IEEE ComSoc Distinguished Lecturer from 2020 to 2023 and an IEEE VTS Distinguished Lecturer from 2024 to 2025.