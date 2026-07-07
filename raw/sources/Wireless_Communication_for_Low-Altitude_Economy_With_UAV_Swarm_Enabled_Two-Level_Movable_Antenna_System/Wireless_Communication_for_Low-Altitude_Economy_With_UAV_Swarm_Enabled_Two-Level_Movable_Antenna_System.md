# Wireless Communication for Low-Altitude Economy With UAV Swarm Enabled Two-Level Movable Antenna System

Haiquan Lu , Member, IEEE, Yong Zeng , Fellow, IEEE, Shaodan Ma , Senior Member, IEEE, Bin Li , Senior Member, IEEE, Shi Jin , Fellow, IEEE, and Rui Zhang , Fellow, IEEE

Abstract—Unmanned aerial vehicle (UAV) is regarded as a key enabling platform for low-altitude economy, due to its advantages such as three-dimensional (3D) maneuverability, flexible deployment, and line-of-sight (LoS) air-to-air/ground communication links. In particular, the intrinsic high mobility renders UAV especially suitable for operating as a movable antenna (MA) from the sky. In this paper, by exploiting the flexible mobility of UAV swarm and antenna position adjustment of MA, we propose a novel UAV swarm enabled two-level MA system, where UAVs not only individually deploy a local MA array, but also form a largerscale MA system with their individual MA arrays via swarm coordination. We formulate a general optimization problem to maximize the minimum achievable rate over all ground user equipments (UEs), by jointly optimizing the 3D UAV swarm placement positions, their individual MAs’ positions (or local positions), and receive beamforming for different UEs. To gain useful insights, we first consider the special case where each UAV has only one antenna, under different scenarios of one single

Shi Jin is with the School of Information Science and Engineering, Southeast University, Nanjing 210096, China (e-mail: jinshi@seu.edu.cn).

Digital Object Identifier 10.1109/TWC.2026.3689048

UE, two UEs, and arbitrary number of UEs. In particular, for the two-UE case, we derive the optimal UAV swarm placement positions in closed-form that achieves inter-UE interference (IUI)- free communication when the uniform plane wave (UPW) model holds, where the UAV swarm forms a uniform sparse array (USA) satisfying minimum safe distance constraint. While for the general case with arbitrary number of UEs, we propose an efficient alternating optimization algorithm to solve the formulated non-convex optimization problem. Then, we extend the results to the case where each UAV is equipped with multiple antennas. Numerical results verify that the proposed low-altitude UAV swarm enabled MA system significantly outperforms various benchmark schemes, thanks to the exploitation of two-level mobility to create more favorable channel conditions for multi-UE communications.

Index Terms—Low-altitude economy, UAV swarm, movable antenna (MA), multi-user communication, array geometry, placement optimization.

## I. INTRODUCTION

L <sup>OW-ALTITUDE</sup> <sup>economy</sup> <sup>has</sup> <sup>emerged</sup> <sup>as</sup> <sup>a</sup> <sup>new</sup> <sup>inte-</sup>grated economic form, involving assorted low-altitude I grated economic form, involving assorted low-altitude activities within sub-1,000-meter airspace domains [2], [3]. By leveraging manned/unmanned aerial vehicles (UAVs), and electric vertical take-off and landing (eVTOL) aircrafts, low-altitude economic ecosystems begin to flourish, which encompass a wide range of applications like logistics and delivery, agricultural plant protection, cultural tourism, environmental monitoring, and so on. In particular, benefiting from the advantages such as three-dimensional (3D) maneuverability, flexible deployment, and line-of-sight (LoS) air-to-air/ground communication links, UAV is regarded as an indispensable part of the low-altitude economy, which has driven various applications in wireless communication and sensing [4], [5], [6]. Specifically, from the perspective of wireless communication, there exist two paradigms, i.e., UAV-assisted wireless communication and cellular-connected UAV communication [7]. For example, UAV equipped with a base station (BS) or relay can be deployed on demand to assist in the conventional cellular wireless networks, so as to satisfy the ubiquitous connectivity required by the future sixthgeneration (6G) wireless network. Extensive research efforts have been devoted to this direction, including UAV channel and energy consumption modeling, performance analysis, and placement/trajectory design [4], [5]. On the other hand, the role of UAV can be shifted from the aerial BS/relay to aerial user equipments (UEs), thus enabling a new paradigm where both the ground and aerial UEs coexist in future wireless networks [4], [7], [8]. Moreover, as integrated sensing and communication (ISAC) has been identified as one of the six major usage scenarios for 6G [9], research on ISAC with UAV has gained a surge of interest recently [10], [11], [12]. Similarly, UAV can act as an aerial anchor for providing the ISAC service from the sky, or an aerial target to be sensed [6].

However, UAVs are subject to various practical constraints in terms of size, weight, dynamics, and power, rendering a single UAV challenging to execute sophisticated communication or sensing missions [4], [13], [14], [15], [16]. To tackle this issue, UAV swarm, i.e., a group of coordinated UAVs, can cooperatively accomplish sophisticated tasks, e.g., largescale data collection and environment monitoring. Compared to single UAV, UAV swarm is able to significantly improve the overall payload capability and expand the communication and sensing coverage area. Moreover, the cooperative mechanism helps to reduce the task completion time and offers an enhanced robustness against anomalies or failures than single UAV, since the task of any malfunctioning UAV can be transferred to its neighboring functioning UAVs [17]. Given the above promising advantages, extensive research endeavours have been devoted to UAV swarm assisted communication and sensing. For example, in [18], an efficient channel estimation and self-positioning approach was proposed for UAV swarm communication with unknown displacements among UAVs. The authors in [19] proposed a 3D irregular terrain area coverage scheme with UAV swarm, and the results show that the proposed scheme can cover the area with little redundancy. Besides UAV swarm assisted communication, recent research works have studied the integration of ISAC with UAV swarm, since the LoS-dominating channel is particularly favorable for sensing [6]. Research on UAV swarm ISAC involves various performance metrics, including signal-to-interferenceplus-noise ratio (SINR) and achievable rate for communication [3], [12], radar mutual information [20] and Cramer-Rao´ lower bound (CRLB) for sensing [11], [12], [21]. Despite the promising advantages, UAV swarm also involves several issues, such as the latency caused by information exchange among UAVs, complex collision avoidance planning, and highprecision localization and sensing for UAV swarm regulation [13], [22]. In particular, to tackle the challenge of accurately localizing and sensing the densely located swarm UAVs, a super-resolution communication and sensing method was proposed for UAV swarm in [22].

It is worth mentioning that the inherent flexible mobility of UAV renders it particularly suitable for operating as a movable antenna (MA) [23], [24], [25], [26], [27], [28], [29], [30], [31], [32] or fluid antenna system (FAS) [33], [34] from the sky. For example, each UAV may be equipped with a single or multiple antennas, and a flexible antenna array architecture can be enabled via adjusting the UAV swarm topology. In contrast to conventional fixed-position antenna (FPA) where inter-antenna spacing is usually fixed as half wavelength, MA dynamically adjusts the antenna position via mechanical and/or electrical control, so as to pursue a favorable channel condition and circumvent the deep fading scenario [23], [33]. This thus achieves performance improvement with optimized antenna positions, which may be a complement to extremely large-scale multiple-input multiple-output (MIMO) technique whereby the spectral efficiency and spatial resolution are significantly enhanced via the orders-of-magnitude scaling of antennas [35], [36]. Subsequently, antenna mobility is extended to a more general concept, where both the antenna position and rotation can be flexibly adjusted, i.e., six-dimensional movable antenna (6DMA) [29], [30], [31], [32]. Driven by such new design degrees of freedom (DoFs), a large body of literature focuses on this technology and demonstrates its performance gain in communication outage probability, spectral efficiency and network capacity, as well as sensing accuracy (see [26], [32], [34] and references therein). Besides active MA, the authors in [37] further proposed a new flexible passive reflector architecture, enabling the flexible beamforming direction adjustment via reflector placement and rotation angle optimization.

Note that compared to MAs, UAVs possess even more flexible and wider-range movement, and thus an interesting new idea is to utilize UAV swarm to form MA array. Moreover, different from existing research on MA that only optimizes antenna positions, UAV swarm enabled MA can fully unlock its mobility advantage, where the array geometry is able to be dynamically reconfigured via trajectory optimization, thus yielding a varying array geometry. Preliminary efforts have been devoted to the single UAV-mounted MA [38], [39], [40], [41]. Specifically, a directional MA was mounted on a UAV to minimize the total data collection time in a backscatter sensor network in [38]. In [39] and [40], the authors utilized the single UAV-mounted MA array to facilitate the minimum beamforming gain for secondary users (SUs) and enhance the sum rate of all UEs, respectively. In [41], the 6DMA was deployed at the single UAV to mitigate the interference caused by the co-channel terrestrial transmissions. Besides the active antenna, the authors in [42] utilized the single UAV-mounted passive 6DMA, i.e., by carrying an intelligent reflecting surface (IRS) on a UAV [43], to maximize the minimum received signal-to-noise ratio (SNR) among all UEs. Nevertheless, these works neither take into account the UAV swarm scenario, nor explore the capability of MA system enabled by UAV swarm. Meanwhile, it is also worth pointing out that the UAV swarm enabled MA system may face several practical challenges, such as the limited endurance of UAV swarm due to the finite onboard battery, positional inaccuracy, array misalignment, orientation jitter, and synchronization issues, which deserve further investigations.

In this paper, motivated by the inherent mobility of UAV swarm and antenna position adjustment of MA, we propose a novel UAV swarm enabled two-level MA system. Specifically, by individually deploying a local MA array on each UAV, all the spatially distributed UAVs cooperatively construct a larger-scale MA system according to their topology. Compared to existing MA systems, UAV swarm enabled MA system involves the dual-scale antenna spatial movement, i.e., the small-scale antenna movement within each local MA array, e.g., at wavelength level, and the large-scale UAV movement, so as to better harness the spatial variations of wireless channels in different scales. In particular, the UAV swarm enabled MA system can be deployed on demand, which is appealing for assorted application scenarios, such as information dissemination and data collection, data offloading in hotspot areas, and rapid communication restoration after infrastructure failure [4]. Moreover, benefiting from the desired LoS air-toair/ground links, UAV swarm enabled MA system can provide the ISAC service efficiently, so as to support low-altitude economy applications such as logistics and delivery as well as environmental monitoring. In this paper, by considering low-altitude UAV swarm enabled uplink multi-UE communication, we aim to maximize the minimum achievable rate over all ground UEs. The main contributions of this paper are summarized as follows.

• First, we propose a novel low-altitude UAV swarm enabled two-level MA system, where each UE channel depends on both UAV swarm placement positions and their mounted MA array positions. Subject to the minimum safe distance constraint for UAVs [4], as well as mutual coupling avoidance constraint for UAV-mounted MA array, we formulate an optimization problem to maximize the minimum achievable rate over all ground UEs, by jointly optimizing the 3D UAV swarm placement positions, their individual MAs’ positions, and receive beamforming for all UEs.

• Second, to gain useful insights, we consider the special case of single-antenna UAV. It is shown that for the single UE communication, the resulting SNR after applying the optimal maximal-ratio combining (MRC) beamforming only depends on the number of UAVs, irrespective of their array geometry. Then, for the two-UE communication, we derive the optimal UAV swarm placement positions that achieves the maximum communication rate without suffering any inter-UE interference (IUI) when the uniform plane wave (UPW) model holds. The result shows that under the minimum safe distance constraint, UAV swarm forms a uniform sparse array (USA) [44] for the IUI-free communication. Moreover, for arbitrary number of UEs, we propose an efficient alternating optimization algorithm to solve the highly non-convex problem, where the optimal receive beamforming is derived in closedform for given UAV swarm placement positions, and for given receive beamforming, the UAV swarm placement optimization problem can be solved via the successive convex approximation (SCA) technique [4].

• Last, we consider the general case of multi-antenna UAV, where each antenna can move independently within the specified region at its mounted UAV. For the single and two-UE communications, similar results can be obtained as in the scenario of single-antenna UAV. In particular, we also consider the special case where all the UAVs adopt the USA [45], the IUI-free communication can be achieved in the two-UE case via joint UAV placement positions and sparsity level adjustment. Next, the alternating optimization method is applied to solve the problem with arbitrary number of UEs. Subsequently, we extend the analysis to the practical case by considering synchronization and position errors, where a channel estimation-based error compensation scheme is proposed. Numerical results are presented to validate the superior performance of the proposed UAV swarm enabled MA system over various benchmarks, thanks to the two-level mobility to create more favorable channel conditions.

![](images/ee3191cf34d9d2563502899cdefc252592ccecd494dd4ca72f8973bea98df9f1.jpg)  
Fig. 1. Wireless communication with a low-altitude UAV swarm enabled two-level MA system.

The remainder of the paper is organized as follows. Section II presents the system model of a low-altitude UAV swarm enabled MA system and formulates the problem to maximize the minimum achievable rate among UEs. Section III considers the special case of single-antenna UAV, and the result is extended to the general case of multi-antenna UAV in Section IV. Section V presents the numerical results to validate the performance of UAV swarm enabled MA systems. Finally, we conclude the paper in Section VI.

Notations: Scalars are denoted by italic letters. Vectors and matrices are denoted by bold-face lower- and upper-case letters, respectively. The spaces of $M \times N$ complex-valued matrices are denoted as $\mathbb { C } ^ { \hat { M } \times N }$ . For a vector x, $\| \mathbf { x } \|$ denotes its Euclidean norm. For an arbitrary-size matrix A, its complex conjugate, transpose, and Hermitian transpose are denoted by $\mathbf { A } ^ { * } , \mathbf { A } ^ { T } , \mathbf { A } ^ { H }$ , respectively. The spectral norm and Frobenius norm of A are denoted as $\lVert \mathbf { A } \rVert _ { 2 }$ and $\| \mathbf { A } \| _ { F } ,$ respectively. The distribution of a circularly symmetric complex Gaussian random vector with mean x and covariance matrix Σ is denoted as $\mathcal { C N } ( \mathbf { x } , \pmb { \Sigma } )$ , and ∼ stands for “distributed $\mathrm { a s } ^ { \prime \prime }$ . For a complex-valued number x, Re {x} represents its real part. mod $( a , b )$ represents the integer modulo operation, which returns the remainder after division of a by b. The symbol j denotes the imaginary unit of complex numbers, with $\mathrm { j } ^ { 2 } = - 1$ $\mathcal { O } \left( \cdot \right)$ denotes the standard big-O notation.

## II. SYSTEM MODEL AND PROBLEM FORMULATION

As illustrated in Fig. 1, we consider a low-altitude UAV swarm enabled wireless communication system, where L UAVs cooperatively serve K single-antenna ground UEs. Each UAV is equipped with a linear MA array with M antenna elements, while a flexible two-level MA system is formed by dynamically moving each UAV and the positions of its individual MAs. Without loss of generality, we consider a 3D Cartesian coordinate system, where the location of UE k is denoted as $\mathbf { w } _ { k } = \left[ x _ { k } , \overline { { y _ { k } } } , 0 \right] ^ { T } , k \in \mathcal { K }$ , with ${ \cal K } \triangleq [ 1 , \cdots , { \cal K } ]$ Let the first antenna be the reference point for each UAV, with the coordinate of UAV l denoted as $\bar { \mathbf q } _ { l } = [ \bar { x } _ { l } , \bar { y } _ { l } , \bar { z } _ { l } ] ^ { T }$ $1 \le l \le L$ . Moreover, the coordinate of antenna m for UAV l is $\bar { \mathbf q } _ { l , m } = \bar { \mathbf q } _ { l } + \mathbf b _ { l , m }$ , where $\mathbf { b } _ { l , m } \triangleq \left[ b _ { l , m } , 0 , 0 \right] ^ { T }$ and we assume $b _ { l , 1 } = 0 ,$ ∀l, without loss of generality. As such, the position of antenna m can be dynamically changed by adjusting $b _ { l , m }$ for UAV l. This thus enables a two-level MA system, realized by the joint control of UAVs’ movement and their individual antennas’ movement.

Let $\begin{array} { c c l } { \mathbf { q } _ { r } } & { = } & { \left[ x _ { r } , y _ { r } , z _ { r } \right] ^ { T } } \end{array}$ denote the reference location for the L UAVs. Let $\begin{array} { r l r } { \kappa _ { k } } & { { } = } & { \left[ \Phi _ { k } , \Psi _ { k } , \Theta _ { k } \right] ^ { T } } \end{array}$ denote the wave propagation direction from UE k to $\mathbf { q } _ { r }$ , with $\Phi _ { k } \ { \triangleq } \ \sin \theta _ { k }$ cos $\phi _ { k }$ $\Psi _ { k } \ \triangleq$ sin $\theta _ { k }$ sin $\phi _ { k }$ , and $\Theta _ { k } \ { \triangleq } \ \cos \theta _ { k } ,$ respectively, where $\theta _ { k }$ and $\phi _ { k }$ denote the elevation and azimuth angles of arrival $\mathbf { \Gamma } ( \operatorname { A o A s } )$ , respectively, as illustrated in Fig. 1. Moreover, let $\mathbf q _ { l } = \left[ x _ { l } , y _ { l } , z _ { l } \right] ^ { T }$ denote the position of UAV l relative to the reference point $\mathbf { q } _ { r } ,$ , and it follows that $\bar { \mathbf q } _ { l } = \mathbf q _ { r } + \mathbf q _ { l }$ . Similarly, we have $\bar { \mathbf q } _ { l , m } = \mathbf q _ { r } + \mathbf q _ { l , m }$ , with ${ \bf q } _ { l , m } = { \bf q } _ { l } + { \bf b } _ { l , m }$ denoting the position of antenna m for UAV l relative to the reference point $\mathbf { q } _ { r }$ . We assume that each UAV knows its relative position to the reference point, which can be obtained via satellite-based localization systems, $\mathrm { e . g . }$ global positioning system (GPS) or Beidou.

In practice, the minimum safe distance constraints need to be satisfied by UAVs, which is given by [4]

$$
\| \mathbf { q } _ { l } - \mathbf { q } _ { l ^ { \prime } } \| \geq d _ { \operatorname* { m i n } } , \ \forall l , l ^ { \prime } \neq l ,\tag{1}
$$

where $d _ { \mathrm { m i n } }$ denotes the minimum distance to guarantee the safe operation between UAVs. Besides, to avoid the mutual coupling between adjacent MA elements at each UAV, the minimum distance $\tilde { d } _ { \mathrm { m i n } }$ is required, which yields the following constraints,

$$
\left\| \mathbf { q } _ { l , m } - \mathbf { q } _ { l , m ^ { \prime } } \right\| = \left| b _ { l , m } - b _ { l , m ^ { \prime } } \right| \geq \tilde { d } _ { \operatorname* { m i n } } , \forall l , m , m ^ { \prime } \neq m ,
$$

where $\tilde { d } _ { \mathrm { m i n } }$ is in practice much smaller than $d _ { \mathrm { m i n } }$

(2)

Note that the communication links between UAVs and ground UEs are of high probability to be over LoS channels in practice. We consider the general near-field spherical wavefront model for the channels between UAVs and ground UEs, which includes the far-field UPW model as a special case. Meanwhile, the signals from UE to the local MA array of each UAV can be well approximated as UPW, since the movable region of the local MA array is much smaller than the link distance. Let $\boldsymbol { \kappa } _ { k , l } ~ = ~ \left[ \Phi _ { k , l } , \dot { \Psi } _ { k , l } , \Theta _ { k , l } \right] ^ { T }$ denote the wave propagation direction from UE k to $\bar { \mathbf q } _ { l }$ , where $\Phi _ { k , l } =$ sin $\theta _ { k , l }$ cos $\phi _ { k , l }$ $\Psi _ { k , l } =$ sin $\theta _ { k , l }$ sin φ<sub>k,l</sub>, and $\Theta _ { k , l } = \cos \theta _ { k , l } ,$ with $\theta _ { k , l }$ and $\phi _ { k , l }$ being the elevation and azimuth AoAs, respectively. For UAV l, the difference of the wavefront propagation distance between $\bar { \mathbf q } _ { l }$ and $\bar { \mathbf q } _ { l , m }$ for UE k is

$$
\varphi _ { k } \left( \bar { \mathbf { q } } _ { l , m } \right) = \kappa _ { k , l } ^ { T } \left( \bar { \mathbf { q } } _ { l , m } - \bar { \mathbf { q } } _ { l } \right) = \kappa _ { k , l } ^ { T } \mathbf { b } _ { l , m } = \Phi _ { k , l } b _ { l , m } ,\tag{3}
$$

which is the projection length of the vector $\left( \bar { \mathbf q } _ { l , m } - \bar { \mathbf q } _ { l } \right)$ onto the wave propagation direction vector $\kappa _ { k , l }$ . Then, the receive array response vector of UAV l for UE k is given by [36]

$$
\begin{array} { r l } & { \mathbf { a } _ { k , l } \left( \left\{ \bar { \mathbf { q } } _ { l , m } , \forall m \right\} \right) = e ^ { - \mathrm { j } \frac { 2 \pi } { \lambda } r _ { k , l } } \times } \\ & { \quad \quad \quad \quad \left[ e ^ { - \mathrm { j } \frac { 2 \pi } { \lambda } \varphi _ { k } \left( \bar { \mathbf { q } } _ { l , 1 } \right) } , \cdot \cdot \cdot , e ^ { - \mathrm { j } \frac { 2 \pi } { \lambda } \varphi _ { k } \left( \bar { \mathbf { q } } _ { l , M } \right) } \right] ^ { T } , } \end{array}\tag{4}
$$

where $r _ { k , l } = \| \bar { \mathbf q } _ { l } - \mathbf w _ { k } \|$ denotes the link distance between $\bar { \mathbf q } _ { l }$ and $\mathbf { w } _ { k }$ . By applying the second-order Taylor approximation, we have

$$
\begin{array} { r } { r _ { k , l } \approx r _ { k , l } ^ { \mathrm { s e c o n d } } \triangleq r _ { k } + x _ { l } \Phi _ { k } + y _ { l } \Psi _ { k } + z _ { l } \Theta _ { k } + } \\ { \underbracket { x _ { l } ^ { 2 } + y _ { l } ^ { 2 } + z _ { l } ^ { 2 } - \left( x _ { l } \Phi _ { k } + y _ { l } \Psi _ { k } + z _ { l } \Theta _ { k } \right) ^ { 2 } } _ { 2 r _ { k } } , } \end{array}\tag{5}
$$

where $r _ { k } = \| \mathbf { w } _ { k } - \mathbf { q } _ { r } \|$ denotes the distance between q and $\mathbf { w } _ { k }$

Moreover, the L UAVs cooperate to form an LM-element distributed antenna array, and thus the channel from UE k to the UAV swarm enabled MA system $\mathrm { i s } ^ { 1 }$

$$
\begin{array} { r } { \mathbf { h } _ { k } \left( \left\{ \bar { \mathbf { q } } _ { l , m } , \forall l , m \right\} \right) = \alpha _ { k } \mathbf { a } _ { k } \left( \left\{ \bar { \mathbf { q } } _ { l , m } , \forall l , m \right\} \right) , } \end{array}\tag{6}
$$

where $\alpha _ { k } = \sqrt { \beta _ { 0 } } / r _ { k } ,$ , with $\beta _ { 0 }$ being the channel power at the reference distance of $d _ { 0 } = 1$ m. Besides, $\mathbf { a } _ { k } \left( \left\{ \bar { \mathbf { q } } _ { l , m } , \forall l , m \right\} \right) \in$ $\mathbb { C } ^ { L M \times 1 }$ denotes the receive array response vector of UE k, given by

$$
\begin{array} { r } { \mathbf { a } _ { k } \left( \left\{ \bar { \mathbf { q } } _ { l , m } , \forall l , m \right\} \right) = \left[ \mathbf { a } _ { k , 1 } ^ { T } \left( \left\{ \bar { \mathbf { q } } _ { 1 , m } , \forall m \right\} \right) , \cdots , \right. } \\ { \left. \mathbf { a } _ { k , L } ^ { T } \left( \left\{ \bar { \mathbf { q } } _ { L , m } , \forall m \right\} \right) \right] ^ { T } . } \end{array}\tag{7}
$$

In the following, for brevity, we use the notations $\mathbf { h } _ { k } , \mathbf { a } _ { k }$ and ${ \bf a } _ { k , l }$ to replace h<sub>k</sub> $\bigl ( \bigl \{ \bar { \mathbf { q } } _ { l , m } , \forall l , m \bigr \} \bigr ) , \ \mathbf { a } _ { k } \bigl ( \bigl \{ \bar { \mathbf { q } } _ { l , m } , \forall l , m \bigr \} \bigr )$ and $\mathbf { a } _ { k , l } \left( \left\{ \overline { { \mathbf { q } } } _ { l , m } , \forall m \right\} \right)$ , respectively.

Denote by $s _ { k }$ the independent and identically distributed (i.i.d.) information-bearing symbol of UE k, with $\dot { \mathbb { E } } [ | s _ { k } | ^ { 2 } ] = 1$ To detect its symbol, the receive beamforming $\mathbf { v } _ { k } \in \mathbb { C } ^ { L M \times 1 } \mathrm { i s }$ applied at the UAV swarm enabled MA system, with $\| \mathbf { v } _ { k } \| =$ 1. Thus, the resulting signal of UE k after applying the receive beamforming is

$$
y _ { k } = { \bf { v } } _ { k } ^ { H } { \bf { h } } _ { k } \sqrt { P _ { k } } s _ { k } + { \bf { v } } _ { k } ^ { H } \sum _ { i = 1 , i \ne k } ^ { K } { { \bf { h } } _ { i } \sqrt { P _ { i } } s _ { i } + { \bf { v } } _ { k } ^ { H } { \bf { z } } } ,\tag{8}
$$

where $P _ { i } , ~ i ~ = ~ 1 , \cdot \cdot \cdot , K$ , denotes the transmit power of UE $i , \mathbf { z } \sim \mathcal { C N } \left( \mathbf { 0 } , \sigma ^ { 2 } \mathbf { I } _ { L M } \right)$ , with each element denoting the i.i.d. additive white Gaussian noise (AWGN) with zero mean and power $\sigma ^ { 2 }$ . To reveal the fundamental performance limit, synchronization is assumed for the UAV swarm system, which can be achieved via a synchronization protocol as in [46].

The resulting SINR for UE k is

$$
\gamma _ { k } = \frac { { \bar { P } _ { k } } { { \left| { { { \bf { v } } _ { k } ^ { H } } { { \bf { h } } _ { k } } } \right| } ^ { 2 } } }  { { { \sum _ { i = 1 , i \ne k } ^ { K } { { { \bar { P } } _ { i } } { { \left| { { { \bf { v } } _ { k } ^ { H } } { { \bf { h } } _ { i } } } \right| } ^ { 2 } } } + 1 } } } = \frac { { { \bar { P } _ { k } } { { \bf { v } } _ { k } ^ { H } } { { \bf { h } } _ { k } } { { \bf { h } } _ { k } ^ { H } } { { \bf { v } } _ { k } } } } { { { \bf { v } } _ { k } ^ { H } } { { \bf { C } } _ { k } } { { \bf { v } } _ { k } } } ,\tag{9}
$$

where $\begin{array} { r l } { { \bf C } _ { k } } & { { } \triangleq { { \mathrm { ~ \bf ~ I } } } _ { L M } + \sum _ { i = 1 , i \neq k } ^ { K } { \bar { P } } _ { i } { \bf h } _ { i } { \bf h } _ { i } ^ { H } } \end{array}$ denotes the interference-plus-noise covariance matrix with respect to $\mathrm { ( w . r . t . ) }$ UE $k ,$ and ${ \bar { P } } _ { i } \ { \triangleq } \ P _ { i } / \sigma ^ { 2 }$ . The achievable rate of UE k is

$$
R _ { k } = \log _ { 2 } \left( 1 + \gamma _ { k } \right) .\tag{10}
$$

<sup>1</sup>The LoS channel can be further generalized to the multi-path channel.

Our objective is to maximize the minimum achievable rate over K UEs, by jointly optimizing the 3D UAV swarm (relative) placement positions $\mathbf { Q } = \{ \mathbf { q } _ { l } , \forall l \}$ , the local positions of MAs at all UAVs $\mathbf { B } = \{ b _ { l , m } , \forall l , m = 2 , \cdot \cdot \cdot , M \}$ and receive beamforming for all UEs $\mathbf { V } ~ = ~ \{ \mathbf { v } _ { k } , \forall k \}$ . Let $\rho \left( \mathbf { Q } , \mathbf { B } , \mathbf { V } \right) = \operatorname* { m i n } _ { k \in \mathcal { K } } R _ { k }$ , which is a function of Q, B, and V. The optimization problem can be formulated as

$$
\mathrm { ( P 1 ) } \operatorname* { m a x } _ { \mathbf { Q } , \mathbf { B } , \mathbf { V } , \rho } \rho\tag{11}
$$

$$
{ \mathrm { s . t . ~ } } R _ { k } \geq \rho , \ \forall k ,\tag{11a}
$$

$$
\mathbf { q } _ { r } + \mathbf { q } _ { l } \in \mathcal { C } , \ \forall l ,\tag{11b}
$$

$$
\left\| \mathbf { q } _ { l } - \mathbf { q } _ { l ^ { \prime } } \right\| ^ { 2 } \geq d _ { \operatorname* { m i n } } ^ { 2 } , \ \forall l , l ^ { \prime } \neq l ,\tag{11c}
$$

$$
b _ { l , m } \in \tilde { \mathcal { C } } , \ \forall l , m ,\tag{11d}
$$

$$
\left| b _ { l , m } - b _ { l , m ^ { \prime } } \right| ^ { 2 } \geq \tilde { d } _ { \mathrm { m i n } } ^ { 2 } , \ \forall l , m , m ^ { \prime } \neq m ,\tag{11e}
$$

$$
\lVert \mathbf { v } _ { k } \rVert = 1 , ~ \forall k ,\tag{11f}
$$

where C denotes the movable region of UAVs, $\tilde { \mathcal { C } }$ denotes the (local) movable region of MAs at each UAV, and the minimum safe distance constraint and mutual coupling avoidance constraint in (1) and (2) have been replaced by their equivalent quadratic forms, i.e., (11c) and (11e), respectively. Problem (P1) is challenging to be directly solved due to the nonconcave objective function and (some) non-convex constraints. Besides, the optimization variables Q, B and V are intricately coupled in the objective function, which makes their joint optimization a challenging task.

## III. SPECIAL CASE OF SINGLE-ANTENNA UAV

In this section, to gain useful insights, we first consider the special case of single-antenna UAV, i.e., M = 1, where (P1) is reduced to

$$
\begin{array} { r l } & { \underset { \mathbf { Q } , \mathbf { V } , \rho } { \mathrm { m a x } } ~ \rho } \\ & { ~ \mathrm { s . t . } ~ R _ { k } \geq \rho , ~ \forall k , } \\ & { ~ \mathbf { q } _ { r } + \mathbf { q } _ { l } \in \mathcal { C } , ~ \forall l , } \\ & { ~ \| \mathbf { q } _ { l } - \mathbf { q } _ { l ^ { \prime } } \| ^ { 2 } \geq d _ { \operatorname* { m i n } } ^ { 2 } , ~ \forall l , l ^ { \prime } \not = l , } \\ & { ~ \| \mathbf { v } _ { k } \| = 1 , ~ \forall k . } \end{array}\tag{12}
$$

In the following, the cases of one single UE, two UEs and arbitrary number of UEs are studied, respectively.

## A. Single UE and Two UEs

For the single UE communication, the receive signal in (8) reduces to

$$
y = \mathbf { v } ^ { H } \mathbf { h } \sqrt { P } s + \mathbf { v } ^ { H } \mathbf { z } ,\tag{13}
$$

where the UE index is omitted for brevity. By applying the optimal MRC beamforming, i.e., $\mathbf { v } = \mathbf { h } / \left. \mathbf { h } \right.$ , the resulting SNR is given by

$$
\gamma = \bar { P } \| \mathbf { h } \| ^ { 2 } = \bar { P } | \alpha | ^ { 2 } L ,\tag{14}
$$

which only depends on the number of UAVs L, irrespective of the geometry formed by the UAV swarm enabled MA system. As a result, any UAV swarm placement within the movable region while satisfying the minimum safe distance constraint can achieve the maximum achievable rate.

Next, we consider the classic MRC, zero-forcing (ZF) and minimum mean-square error (MMSE) beamforming schemes for the case of two UEs. Denote by $\begin{array} { r } { \xi _ { k , k ^ { \prime } } \triangleq \frac { \left| \mathbf { h } _ { k } ^ { H } \mathbf { \overline { { h } } } _ { k ^ { \prime } } \right| ^ { 2 } } { \left\| \mathbf { h } _ { k } \right\| ^ { 2 } \left\| \mathbf { h } _ { k ^ { \prime } } \right\| ^ { 2 } } } \end{array}$ the channel’s squared-correlation coefficient between UEs k and k<sup>0</sup>, where $k , k ^ { \prime } = 1 , 2$ and $k \neq k ^ { \prime }$ . Besides, we have $\left\| \mathbf { h } _ { k } \right\| ^ { 2 } =$ ${ | \alpha _ { k } | } ^ { 2 } L$ . The resulting SINR/SNR of UE k after applying the three beamforming schemes are respectively given by [35], [36]

$$
\gamma _ { \mathrm { M R C } , k } = \bar { P } _ { k } | \alpha _ { k } | ^ { 2 } L \left( 1 - \frac { \bar { P } _ { k ^ { \prime } } | \alpha _ { k ^ { \prime } } | ^ { 2 } L \xi _ { k , k ^ { \prime } } } { \bar { P } _ { k ^ { \prime } } | \alpha _ { k ^ { \prime } } | ^ { 2 } L \xi _ { k , k ^ { \prime } } + 1 } \right) ,\tag{15}
$$

$$
\gamma _ { \mathrm { Z F } , k } = \bar { P } _ { k } \vert \alpha _ { k } \vert ^ { 2 } L \left( 1 - \xi _ { k , k ^ { \prime } } \right) ,\tag{16}
$$

$$
\gamma _ { \mathrm { M M S E } , k } = \bar { P } _ { k } | \alpha _ { k } | ^ { 2 } L \left( 1 - \frac { \bar { P } _ { k ^ { \prime } } | \alpha _ { k ^ { \prime } } | ^ { 2 } L \xi _ { k , k ^ { \prime } } } { \bar { P } _ { k ^ { \prime } } | \alpha _ { k ^ { \prime } } | ^ { 2 } L + 1 } \right) .\tag{17}
$$

It is observed from (15)-(17) that the SINRs of MRC, ZF, and MMSE beamforming depend on the coefficient $\xi _ { k , k ^ { \prime } }$ , and a larger SINR can be achieved as $\xi _ { k , k ^ { \prime } }$ decreases. Moreover, the terms $\frac { \bar { P } _ { k ^ { \prime } } | \alpha _ { k ^ { \prime } } | ^ { 2 } L \xi _ { k , k ^ { \prime } } } { \bar { P } _ { k ^ { \prime } } | \alpha _ { k ^ { \prime } } | ^ { 2 } L \xi _ { k , k ^ { \prime } } + 1 } , \xi _ { k , k ^ { \prime } }$ , and $\frac { \bar { P } _ { k ^ { \prime } } | \alpha _ { k ^ { \prime } } | ^ { 2 } L \xi _ { k , k ^ { \prime } } } { \bar { P } _ { k ^ { \prime } } | \alpha _ { k ^ { \prime } } | ^ { 2 } L + 1 }$ in (15)-(17) account for the SNR loss factors for UE k due to applying the MRC, ZF, and MMSE beamforming schemes, respectively. By substituting (6) into $\xi _ { k , k ^ { \prime } }$ , we have

$$
\xi _ { k , k ^ { \prime } } = \frac { 1 } { L ^ { 2 } } { \left| \mathbf { a } _ { k } ^ { H } \mathbf { a } _ { k ^ { \prime } } \right| } ^ { 2 } .\tag{18}
$$

Based on the above observation, for the case of two UEs, we aim to minimize the channels’ squared-correlation coefficient, which can be formulated as

$$
\begin{array} { r l } & { \underset { \mathbf { Q } } { \operatorname* { m i n } } \ : \frac { 1 } { L ^ { 2 } } \big | \mathbf { a } _ { k } ^ { H } \mathbf { a } _ { k ^ { \prime } } \big | ^ { 2 } } \\ & { \mathrm { ~ s . t . ~ } \mathbf { q } _ { r } + \mathbf { q } _ { l } \in \mathcal { C } , \ \forall l , } \\ & { \quad \quad \quad \left\| \mathbf { q } _ { l } - \mathbf { q } _ { l ^ { \prime } } \right\| ^ { 2 } \geq d _ { \operatorname* { m i n } } ^ { 2 } , \ \forall l , l ^ { \prime } \neq l . } \end{array}\tag{19}
$$

To tackle problem (19), we first study the property of the objective function. Note that when the movable region size is much smaller than the link distance, the UPW model gives a valid approximation of spherical wavefront for channels between UAVs and ground UEs [36], which may correspond to the cases of small movable region and/or high UAV operation altitude. In this case, the receive response vector in (7) reduces to $\mathbf { a } _ { k } = e ^ { - \mathrm { j } \frac { 2 \pi } { \lambda } r _ { k } } \Big [ e ^ { - \mathrm { j } \frac { 2 \pi } { \lambda } \kappa _ { k } ^ { T } \mathbf { q } _ { 1 } } , \therefore \cdot \cdot , e ^ { - \mathrm { j } \frac { 2 \pi } { \lambda } \kappa _ { k } ^ { T } \mathbf { q } _ { L } } \Big ] ^ { T }$ . By substituting it into the objective function, we have

$$
\frac { 1 } { L ^ { 2 } } { \left| { \bf { a } } _ { k } ^ { H } { \bf { a } } _ { k ^ { \prime } } \right| } ^ { 2 } = \frac { 1 } { L ^ { 2 } } { \left| \sum _ { l = 1 } ^ { L } e ^ { \mathrm { { j } } \frac { 2 \pi } { \lambda } ( \kappa _ { k } - \kappa _ { k ^ { \prime } } ) ^ { T } { \bf { q } } _ { l } } \right| } ^ { 2 } .\tag{20}
$$

By letting $\nu _ { \mathrm { m i n } } = \lceil L d _ { \mathrm { m i n } } \rceil \| \kappa _ { k } - \kappa _ { k ^ { \prime } } \| / \lambda - 1 \rceil$ , we obtain the following theorem for UAV position without drift. In particular, high-accuracy positioning technologies, such as real-time kinematic (RTK) global navigation satellite system (GNSS), multi-sensor fusion, and robust flight control algorithms help to mitigate the issue of UAV position drift [47].

Theorem 1: An optimal solution to (19) that achieves zero objective value is

$$
{ \bf q } _ { l } = { \bf q } _ { 1 } + \left( l - 1 \right) \frac { \left( \boldsymbol { \varsigma } ^ { \star } + 1 / L \right) \lambda } { \left\| \boldsymbol { \kappa } _ { k } - \boldsymbol { \kappa } _ { k ^ { \prime } } \right\| ^ { 2 } } \left( \boldsymbol { \kappa } _ { k } - \boldsymbol { \kappa } _ { k ^ { \prime } } \right) ,\tag{21}
$$

where $\mathbf { q } _ { 1 }$ can be any vector to guarantee $\mathbf { q } _ { r } + \mathbf { q } _ { l } \in \mathcal { C } , \forall l .$ , and $\varsigma ^ { \star }$ is given by

$$
\begin{array} { r } { \varsigma ^ { \star } = \left\{ \begin{array} { r l } & { \frac { \nu _ { \mathrm { m i n } } } { L } , \qquad \mathrm { i f ~ \ m o d ~ } ( \nu _ { \mathrm { m i n } } + 1 , L ) \ne 0 , } \\ & { \frac { \nu _ { \mathrm { m i n } } + 1 } { L } , \mathrm { ~ o t h e r w i s e . } } \end{array} \right. } \end{array}\tag{22}
$$

Proof: Please refer to Appendix A.

Note that Theorem 1 extends the 1D result in [24] to the general 3D placement, and the derived closed-form solution $\varsigma ^ { \star }$ can be a fraction, which removes the requirement of being an integer imposed in [24]. Moreover, a sufficient condition for $\mathbf q _ { r } + \mathbf q _ { l } \in \mathcal L , \forall l$ , is that C contains a line segment parallel to $\left( \kappa _ { \boldsymbol { k } } - \kappa _ { \boldsymbol { k } ^ { \prime } } \right)$ with length no smaller than $\begin{array} { r } { \| \mathbf { q } _ { L } - \mathbf { q } _ { 1 } \| = \frac { ( L - 1 ) ( \varsigma ^ { \star } + 1 / L ) \lambda } { \| \kappa _ { k } - \kappa _ { \iota , \prime } \| } } \end{array}$

With (21) and (22), we have $\xi _ { k , k ^ { \prime } } = 0 \ :$ and $\gamma _ { \mathrm { M R C } , k } ~ =$ $\begin{array} { r l } { \gamma _ { \mathrm { Z F } , k } } & { = \gamma _ { \mathrm { M M S E } , k } = \bar { P } _ { k } \| \mathbf { h } _ { k } \| ^ { 2 } = \bar { P } _ { k } | \alpha _ { k } | ^ { 2 } L } \end{array}$ , i.e., they are identical to the single UE SNR without IUI. Thus, an IUI-free communication can be achieved with the UAV swarm enabled MA system, by setting the UAVs’ static positions according to Theorem 1. It is worth noting that the adjacent inter-UAV distance is $\frac { | \varsigma ^ { \star } + 1 / L | \lambda } { \| \kappa _ { k } - \kappa _ { k ^ { \prime } } \| } \geq d _ { \operatorname* { m i n } }$ , where the minimum distance $d _ { \mathrm { m i n } }$ is in general much larger than half wavelength. Thus, the UAV swarm forms a USA for the IUI-free communication. In particular, compared to the classic compact array where antenna spacing is separated by half wavelength, USA can achieve a larger array aperture, and thus a narrower beamwidth of the main lobe is enabled.

Moreover, the objective function in (P1) is given by

$$
\operatorname* { m i n } _ { k \in \mathcal K } \log _ { 2 } \left( 1 + \bar { P } _ { k } { \left| { \alpha _ { k } } \right| } ^ { 2 } L \right) .\tag{23}
$$

It can be observed that the UAV swarm enabled MA system not only completely eliminates the IUI, but also achieves the full beamforming gain at each ${ \mathrm { U E } } ,$ in terms of the number of UAVs L in (23), without suffering from any performance loss as in the traditional FPA system [35].

## B. Arbitrary Number of UEs

In this subsection, for arbitrary number of UEs, we propose an alternating optimization algorithm to solve problem (12) sub-optimally, where the receive beamforming and each UAV placement position are optimized alternately in an iterative manner.

1) Optimization of V With Given $\varrho \colon$ For given UAV swarm placement positions Q, the receive beamforming optimization problem in (12) is expressed as

$$
\begin{array} { r l } & { \underset { { \bf V } , \rho } { \mathrm { m a x } } ~ \rho } \\ & { ~ \mathrm { s . t . } ~ R _ { k } \geq \rho , ~ \forall k , } \\ & { ~ \| { \bf v } _ { k } \| = 1 , ~ \forall k . } \end{array}\tag{24}
$$

A closer look at (9) shows that the receive beamforming $\mathbf { v } _ { k }$ only impacts the SINR for UE k, and (9) is a generalized Rayleigh quotient w.r.t. $\mathbf { v } _ { k }$ , the optimal $\mathbf { v } _ { k }$ to (24) is given by the classical MMSE beamforming [48]:

$$
\mathbf { v } _ { k } ^ { \star } = \frac { \mathbf { C } _ { k } ^ { - 1 } \mathbf { h } _ { k } } { \left\| \mathbf { C } _ { k } ^ { - 1 } \mathbf { h } _ { k } \right\| } , \ \forall k .\tag{25}
$$

2) Optimization of q With Given V and $\{ \mathbf { q } _ { l ^ { \prime } } , \forall l ^ { \prime } \neq l \}$ For given V and $\{ \mathbf { q } _ { l ^ { \prime } } , \forall l ^ { \prime } \neq l \}$ , the sub-problem of (12) for optimizing the placement position of UAV l can be expressed as

$$
\operatorname* { m a x } _ { \mathbf { q } _ { l } , \rho } \rho\tag{26}
$$

$$
\mathrm { s . t . } \ R _ { k } \geq \rho , \ \forall k \in { \mathcal K } ,\tag{26a}
$$

$$
\mathbf { q } _ { r } + \mathbf { q } _ { l } \in \mathcal { C } ,\tag{26b}
$$

$$
\left\| \mathbf { q } _ { l } - \mathbf { q } _ { l ^ { \prime } } \right\| ^ { 2 } \geq d _ { \operatorname* { m i n } } ^ { 2 } , \ \forall l ^ { \prime } \neq l .\tag{26c}
$$

Moreover, to tackle the non-convexity of the constraint (26a), the slack variables $\{ \eta _ { k } , \mu _ { k } , \forall k \}$ are introduced such that

$$
e ^ { \eta _ { k } } = 1 + \sum _ { i = 1 } ^ { K } \bar { P } _ { i } \big | { \bf v } _ { k } ^ { H } { \bf h } _ { i } \big | ^ { 2 } ,\tag{27}
$$

$$
e ^ { \mu _ { k } } = 1 + \sum _ { i = 1 , i \neq k } ^ { K } \bar { P } _ { i } \big | { \bf v } _ { k } ^ { H } { \bf h } _ { i } \big | ^ { 2 } .\tag{28}
$$

Thus, problem (26) is transformed into

max ρ q<sub>l</sub>,ρ,{η<sub>k</sub>,µ<sub>k</sub>}<sub>k=1</sub> K

(29)

$$
\mathrm { s . t . } \quad { \frac { \ln \left( e ^ { \eta _ { k } - \mu _ { k } } \right) } { \ln 2 } } \geq \rho , \forall k \in { \mathcal { K } } ,\tag{29a}
$$

$$
\sigma ^ { 2 } + \sum _ { i = 1 } ^ { K } P _ { i } \big | \mathbf { v } _ { k } ^ { H } \mathbf { h } _ { i } \big | ^ { 2 } \geq \sigma ^ { 2 } e ^ { \eta _ { k } } , \ \forall k \in \mathcal { K } ,\tag{29b}
$$

$$
\sigma ^ { 2 } + \sum _ { i = 1 , i \neq k } ^ { K } P _ { i } \big | { \mathbf { v } _ { k } ^ { H } \mathbf { h } _ { i } } \big | ^ { 2 } \leq \sigma ^ { 2 } e ^ { \mu _ { k } } , \ \forall k \in \mathcal { K } ,
$$

$$
\mathbf { q } _ { r } + \mathbf { q } _ { l } \in \mathcal { C } ,\tag{29c}
$$

$$
\left\| \mathbf { q } _ { l } - \mathbf { q } _ { l ^ { \prime } } \right\| ^ { 2 } \geq d _ { \operatorname* { m i n } } ^ { 2 } , ~ l ^ { \prime } \neq l .\tag{29d}
$$

(29e)

Note that problem (29) is still challenging to be solved since the constraints (29b), (29c) and (29e) are non-convex. To tackle this issue, the SCA technique [4] is applied in the following, which is an efficient iterative optimization technique that successively updates the optimization variables by solving the approximated convex problem at each iteration.

Let $\bar { \mathbf { h } } _ { i , l } ~ \in ~ \bar { \mathbb { C } } ^ { \left( L - 1 \right) \times 1 }$ denote the resulting channel after removing $h _ { i , l }$ from $\mathbf { h } _ { i } ,$ and $\bar { \mathbf { v } } _ { k , l } ~ \in ~ \mathbb { C } ^ { ( L - 1 ) \times 1 }$ denote the resulting beamforming vector after removing $v _ { k , l }$ from $\mathbf { v } _ { k } .$ where $h _ { i , l }$ and $v _ { k , l }$ denote the l-th element of $\mathbf { h } _ { i }$ and $\mathbf { v } _ { k } .$ respectively. Then, $f _ { k , i } \triangleq \big | \mathbf { v } _ { k } ^ { H } \mathbf { h } _ { i } \big | ^ { 2 }$ can be expressed as

$$
\begin{array} { r l } & { f _ { k , i } = \mathbf { h } _ { i } ^ { H } \mathbf { v } _ { k } \mathbf { v } _ { k } ^ { H } \mathbf { h } _ { i } = \underset { \underset { \bar { g } _ { k , i } , \bar { \iota } } { \underbrace { \mathrm { I } ^ { \prime } = 1 , \bar { \iota } ^ { \prime } \neq l } } } { \sum _ { i = 1 , \bar { \iota } ^ { \prime } \neq l } } 2 \mathrm { R e } \left\{ h _ { i , l } ^ { * } V _ { k , l , \bar { \iota } ^ { \prime } } h _ { i , l ^ { \prime } } \right\} } \\ & { ~ + \underset { \bar { g } _ { k , i , l } } { \underbrace { \mathrm { \ I } \alpha _ { i } \mathrm { \ I } ^ { 2 } V _ { k , l , l } + \bar { \mathbf { h } } _ { i , l } ^ { H } \bar { \mathbf { v } } _ { k , l , l } \bar { \mathbf { h } } _ { i , l } } } , } \end{array}\tag{30}
$$

where $\begin{array} { r } { V _ { k , l , l ^ { \prime } } \triangleq v _ { k , l } v _ { k , l ^ { \prime } } ^ { * } , \bar { \mathbf { V } } _ { k , l , l } \in \mathbb { C } ^ { ( L - 1 ) \times ( L - 1 ) } \triangleq \bar { \mathbf { v } } _ { k , l } \bar { \mathbf { v } } _ { k , l } ^ { H } , } \end{array}$ and ${ \bar { g } } _ { k , i , l }$ is independent of $\mathbf { q } _ { l }$ . By substituting $\begin{array} { r l } { h _ { i , l } } & { { } = } \end{array}$ $\alpha _ { i } e ^ { - \mathrm { j } \frac { 2 \pi } { \lambda } r _ { i , l } }$ into $g _ { k , i , l }$ , we have

$$
\begin{array} { r l } & { g _ { \boldsymbol { k } , i , l } = \displaystyle \sum _ { l ^ { \prime } = 1 , l ^ { \prime } \neq l } ^ { L } 2 | \alpha _ { i } | ^ { 2 } \mathrm { R e } \left\{ V _ { \boldsymbol { k } , l , l ^ { \prime } } e ^ { \mathrm { j } \frac { 2 \pi } { \lambda } \left( r _ { i , l } - r _ { i , l ^ { \prime } } \right) } \right\} } \\ & { = \displaystyle \sum _ { l ^ { \prime } = 1 , l ^ { \prime } \neq l } ^ { L } 2 | \alpha _ { i } | ^ { 2 } | V _ { \boldsymbol { k } , l , l ^ { \prime } } | \cos \left( \frac { 2 \pi } { \lambda } \left( r _ { i , l } - r _ { i , l ^ { \prime } } \right) + \angle V _ { \boldsymbol { k } , l , l ^ { \prime } } \right) . } \end{array}\tag{31}
$$

It is observed that (31) is neither convex nor concave w.r.t. $\mathbf { q } _ { l }$ . To this end, two quadratic surrogate functions are respectively constructed to serve as the lower and upper bounds for $g _ { k , i , l }$ , shown in the following lemma.

Lemma 1: The lower and upper bounds of $g _ { k , i , l }$ are respectively given by

$$
\begin{array} { r l r } & { } & { g _ { k , i , l } \geq [ g _ { k , i , l } ] _ { \mathrm { l b } } = g _ { k , i , l } \left( \mathbf { q } _ { l } ^ { ( j ) } \right) + \nabla g _ { k , i , l } \left( \mathbf { q } _ { l } ^ { ( j ) } \right) ^ { T } \left( \mathbf { q } _ { l } - \mathbf { q } _ { l } ^ { ( j ) } \right) } \\ & { } & { - \displaystyle \frac { \delta _ { k , i , l } } { 2 } \Big ( \mathbf { q } _ { l } - \mathbf { q } _ { l } ^ { ( j ) } \Big ) ^ { T } \left( \mathbf { q } _ { l } - \mathbf { q } _ { l } ^ { ( j ) } \right) , \qquad ( 3 2 ) } \end{array}
$$

$$
\begin{array} { r l r } & { } & { g _ { k , i , l } \leq [ g _ { k , i , l } ] _ { \mathrm { u b } } = g _ { k , i , l } ( \mathbf { q } _ { l } ^ { ( j ) } ) + \nabla g _ { k , i , l } ( \mathbf { q } _ { l } ^ { ( j ) } ) ^ { T } ( \mathbf { q } _ { l } - \mathbf { q } _ { l } ^ { ( j ) } ) } \\ & { } & { +  \frac { \delta _ { k , i , l } } { 2 } \Big ( \mathbf { q } _ { l } - \mathbf { q } _ { l } ^ { ( j ) } \Big ) ^ { T } ( \mathbf { q } _ { l } - \mathbf { q } _ { l } ^ { ( j ) } ) , \qquad ( 3 3 ) } \end{array}
$$

where $\delta _ { k , i , l } = \frac { 2 \pi } { \lambda } \sum _ { l ^ { \prime } = 1 , l ^ { \prime } \neq l } ^ { L } 2 { \left| { \alpha _ { i } } \right| } ^ { 2 } { \left| { V _ { k , l , l ^ { \prime } } } \right| }$

$\begin{array} { r } { \sqrt { \frac { 2 } { r _ { i } ^ { 2 } } + \left( \frac { 2 \pi } { \lambda } \right) ^ { 2 } \left( 1 + \frac { C _ { \operatorname* { m a x } } } { r _ { i } ^ { 2 } } \right) ^ { 2 } } , \ \mathbf { q } _ { l } ^ { ( j ) } } \end{array}$ denotes the resulting placement position of UAV l in the j-th iteration, and $\dot { \nabla } g _ { k , i , l } ( \mathbf { q } _ { l } ^ { ( j ) } )$ denotes the gradient of $g _ { k , i , l }$ over $\mathbf { q } _ { l } ^ { ( j ) }$

Proof: Please refer to Appendix B.

With Lemma 1, the lower and upper bounds of the function $f _ { k , i }$ are

$$
f _ { k , i } \geq [ f _ { k , i } ] _ { \mathrm { l b } } \triangleq [ g _ { k , i , l } ] _ { \mathrm { l b } } + \bar { g } _ { k , i , l } ,\tag{34}
$$

$$
f _ { k , i } \leq [ f _ { k , i } ] _ { \mathrm { u b } } \triangleq [ g _ { k , i , l } ] _ { \mathrm { u b } } + \bar { g } _ { k , i , l } ,\tag{35}
$$

which are concave and convex w.r.t. $\mathbf { q } _ { l } ,$ , respectively.

Moreover, to tackle the non-convexity of $e ^ { \mu _ { k } }$ on the righthand-side (RHS) of (29c), let $\mu _ { k } ^ { ( j ) }$ denote the resulting variable in the $j \cdot$ th iteration; then the convex function $e ^ { \mu _ { k } }$ is lowerbounded by

$$
e ^ { \mu _ { k } } \geq \left[ e ^ { \mu _ { k } } \right] _ { \mathrm { l b } } \triangleq \mu _ { k } e ^ { \mu _ { k } ^ { ( j ) } } + \left( 1 - \mu _ { k } ^ { ( j ) } \right) e ^ { \mu _ { k } ^ { ( j ) } } .\tag{36}
$$

Similarly, for given $\mathbf { q } _ { l } ^ { ( j ) }$ , the convex function $\| \mathbf { q } _ { l } - \mathbf { q } _ { l ^ { \prime } } \| ^ { 2 }$ on the left-hand-side (LHS) of (29e) is lower-bounded by [4]

$$
\begin{array} { r l } & { \left\| \mathbf { q } _ { l } - \mathbf { q } _ { l ^ { \prime } } \right\| ^ { 2 } \geq \left[ \left\| \mathbf { q } _ { l } - \mathbf { q } _ { l ^ { \prime } } \right\| ^ { 2 } \right] _ { \mathrm { l b } } } \\ & { \triangleq 2 \Big ( \mathbf { q } _ { l } ^ { ( j ) } - \mathbf { q } _ { l ^ { \prime } } \Big ) ^ { T } \Big ( \mathbf { q } _ { l } - \mathbf { q } _ { l } ^ { ( j ) } \Big ) + \left\| \mathbf { q } _ { l } ^ { ( j ) } - \mathbf { q } _ { l ^ { \prime } } \right\| ^ { 2 } . } \end{array}\tag{37}
$$

As a result, problem (29) is lower-bounded by the following problem for given $\{ \mathbf { q } _ { l } ^ { ( j ) } , \boldsymbol { \mu } _ { k } ^ { ( j ) } \}$

$$
\begin{array} { r l } & { \underset { \mathbf { q } _ { l } , \rho , \left\{ \eta _ { k } , \mu _ { k } \right\} _ { k = 1 } ^ { K } } { \mathrm { m a x } } \quad \rho } \\ & { \quad \quad \quad \mathrm { s . t . } \ \eta _ { k } - \mu _ { k } \geq \rho \ln 2 , \ \forall k \in \mathcal { K } , } \\ & { \quad \quad \quad \quad \sigma ^ { 2 } + \displaystyle \sum _ { i = 1 } ^ { K } P _ { i } [ f _ { k i } ] _ { \mathrm { l b } } \geq \sigma ^ { 2 } e ^ { \eta _ { k } } , \ \forall k \in \mathcal { K } , } \end{array}
$$

$$
\begin{array} { r l r } { \displaystyle \sigma ^ { 2 } + \sum _ { i = 1 , i \neq k } ^ { K } P _ { i } [ f _ { k i } ] _ { \mathrm { u b } } \leq \sigma ^ { 2 } [ e ^ { \mu _ { k } } ] _ { \mathrm { l b } } , } & { \forall k \in \mathcal { K } , } & \\ { \displaystyle \mathbf { q } _ { r } + \mathbf { q } _ { l } \in \mathcal { C } , } & { } & \\ { \displaystyle \left[ \left. \mathbf { q } _ { l } - \mathbf { q } _ { l ^ { \prime } } \right. ^ { 2 } \right] _ { \mathrm { l b } } \geq d _ { \mathrm { m i n } } ^ { 2 } , ~ \forall l ^ { \prime } \neq l , } & { \mathrm { ( ~ } } \end{array}\tag{38}
$$

which is a convex optimization problem and can be solved via the standard convex optimization tools, such as CVX.

Algorithm 1 Proposed Alternating Optimization for Solving   
Problem (12)   
1: Initialize $\mathbf { Q } ^ { ( 0 ) }$ and $\{ \mathbf { v } _ { k } ^ { ( 0 ) } \}$ randomly, and let $j = 0 .$   
2: repeat   
3: For given $\mathbf { Q } ^ { ( j ) }$ , obtain the optimal solution to (24)   
based on (25), denoted as $\{ \mathbf { v } _ { k } ^ { ( \dot { j } + 1 ) } \}$   
4: for $l = 1 : L$ do   
5: Obtain $\{ \mathbf { q } _ { l } ^ { ( j + 1 ) } \}$ by solving problem (38), given   
$\{ \mathbf { q } _ { 1 } ^ { ( j + 1 ) } , \cdots , \mathbf { q } _ { l - 1 } ^ { ( j + 1 ) } , \mathbf { q } _ { l } ^ { ( j ) } , \cdots , \mathbf { q } _ { L } ^ { ( j ) } \}$ and $\{ \bar { \mathbf { v } } _ { k } ^ { ( j + 1 ) } \}$   
6: end for   
7: Update $j = j + 1 .$   
8: until the fractional increase in the objective function value   
is below a given threshold $\epsilon > 0$

The overall algorithm is summarized in Algorithm 1, and its convergence proof is given as follows.

Proposition 1: The objective value of problem (12) obtained by Algorithm 1 is guaranteed to converge.

## Proof: Please refer to Appendix C.

It is worth mentioning that the objective value at each iteration is non-decreasing, thus guaranteeing the convergence of Algorithm 1. Moreover, the computational complexity is analyzed as follows. In step 3, the complexity for obtaining the receive beamforming is $\mathcal { O } ( K L ^ { 3 } )$ . The complexity from step 4 to step 6 is approximately ${ \dot { O } } ( I _ { 1 } L ( 2 K ) ^ { 3 } )$ , where $I _ { 1 }$ denotes the maximum number of iterations required by SCA for convergence. Thus, the total computational complexity of Algorithm 1 is $\mathcal { O } ( I _ { 2 } K L ^ { 3 } + I _ { 1 } I _ { 2 } L ( \bar { 2 } K ) ^ { 3 } )$ , where $I _ { 2 }$ denotes the number of iterations required by the alternating optimization for convergence.

## IV. MULTI-ANTENNA UAV

In this section, we consider the general case of multiantenna UAV, where each UAV deploys an MA array and all the UAVs simultaneously forms a larger-scale MA system with their individual MA arrays.

## A. Single UE and Two UEs

For the single UE communication, similar to (14), the resulting SNR is

$$
\gamma = \bar { P } \Vert \mathbf { h } \Vert ^ { 2 } = \bar { P } { \vert \alpha \vert } ^ { 2 } L M .\tag{39}
$$

For the scenario with two UEs, the resulting SINR/SNR of UE k with the MRC, ZF, and MMSE beamforming can be similarly obtained by substituting L with LM in (15)-(17),

respectively. Besides, when UPW model holds, the channel’s squared-correlation coefficient between UEs k and $k ^ { \prime }$ is

$$
\begin{array} { l } { { \displaystyle \xi _ { k , k ^ { \prime } } = \frac { 1 } { L ^ { 2 } M ^ { 2 } } \Biggl | \sum _ { l = 1 } ^ { L } \mathbf { a } _ { k , l } ^ { H } \mathbf { a } _ { k ^ { \prime } , l } \Biggr | ^ { 2 } } } \\ { { \displaystyle \qquad = \frac { 1 } { L ^ { 2 } M ^ { 2 } } \Biggl | \sum _ { l = 1 } ^ { L } e ^ { \mathrm { j } \frac { 2 \pi } { \lambda } \bigl ( \star _ { k } ^ { T } - \star _ { k ^ { \prime } } ^ { T } \bigr ) } \mathbf { q } _ { l } \sum _ { m = 1 } ^ { M } e ^ { \mathrm { j } \frac { 2 \pi } { \lambda } b _ { l , m } \Delta \Phi _ { k , k ^ { \prime } } } \Biggr | ^ { 2 } , } } \end{array}\tag{40}
$$

where $\Delta \Phi _ { k , k ^ { \prime } } \triangleq \Phi _ { k } - \Phi _ { k ^ { \prime } }$ . It is observed from (40) that when $\begin{array} { r } { \sum _ { m = 1 } ^ { M } e ^ { \mathrm { j } \frac { 2 \pi } { \lambda } b _ { l , m } \Delta \Phi _ { k , k ^ { \prime } } } = 0 , \forall l , } \end{array}$ we have $\xi _ { k , k ^ { \prime } } = 0$

Similar to Theorem 1, an optimal solution of $\left\{ b _ { l , m } \right\}$ to (40) that achieves zero objective value is

$$
b _ { l , m } = \left( m - 1 \right) \frac { \left( \zeta _ { l } ^ { \star } + 1 / M \right) \lambda } { \left. \Delta \Phi _ { k , k ^ { \prime } } \right. } ,\tag{41}
$$

where the common coefficient $\zeta _ { l } ^ { \star }$ is derived to satisfy the mutual coupling avoidance constraint between adjacent MA elements for each UAV, given by

$$
\zeta _ { l } ^ { \star } = \left\{ \frac { \displaystyle \frac { \tilde { \nu } _ { \mathrm { m i n } } } { \cal M } , \qquad \mathrm { i f } \mod ( \tilde { \nu } _ { \mathrm { m i n } } + 1 , { \cal M } ) \neq 0 , } { \displaystyle \frac { \tilde { \nu } _ { \mathrm { m i n } } + 1 } { { \cal M } } , \ \mathrm { o t h e r w i s e } , } \right.\tag{42}
$$

with $\tilde { \nu } _ { \mathrm { m i n } } = \left\lceil M \tilde { d } _ { \mathrm { m i n } } \left| \Delta \Phi _ { k , k ^ { \prime } } \right| / \lambda - 1 \right\rceil$ common to all UAVs. Moreover, MA position $b _ { l , m } \in \tilde { \mathcal { C } } , \dot { \forall l } , m$ , can be satisfied when $\begin{array} { r } { | b _ { l , M } - b _ { l , 1 } | = \left( M - 1 \right) \frac { ( \zeta _ { l } ^ { \star } + 1 / M ) \lambda } { \left| \Delta \Phi _ { k , k ^ { \prime } } \right| } } \end{array}$ is no greater than the maximum distance between any two points in ${ \tilde { \mathcal { C } } } .$

Note that the MAs’ positions given in (41)-(42) enable an IUI-free communication via $\mathbf { M A s } ^ { \prime }$ positions adjustment, irrespective of UAV swarm placement positions. The objective function in (P1) is thus given by

$$
\operatorname* { m i n } _ { k \in \mathcal K } \log _ { 2 } { \left( 1 + \bar { P } _ { k } | \alpha _ { k } | ^ { 2 } L M \right) } .\tag{43}
$$

In fact, the results in (41)-(42) correspond to the case where all MA arrays have the identical architecture. To gain further insights, we express $\mathbf { b } _ { l , m }$ as $\mathbf { b } _ { l , m } = \mathbf { b } _ { m } = \left[ b _ { m } , 0 , \overline { { 0 } } \right] ^ { T }$ , ∀l, the channels’ squared-correlation coefficient in (40) is reduced to

$$
\xi _ { k , k ^ { \prime } } = \frac { 1 } { L ^ { 2 } } \Bigg | \underset { l = 1 } { \overset { L } { \sum } } e ^ { \mathrm { j } \frac { 2 \pi } { \lambda } \left( \kappa _ { k } ^ { T } - \kappa _ { k ^ { \prime } } ^ { T } \right) \mathbf { q } _ { l } } \Bigg | \overset { 2 }  \underset { \Longleftrightarrow } { \underbrace { \frac { 1 } { M ^ { 2 } } \Bigg | \underset { m = 1 } { \overset { M } { \sum } } } } e ^ { \mathrm { j } \frac { 2 \pi } { \lambda } b _ { m } \Delta \Phi _ { k , k ^ { \prime } } } \Bigg | ^ { 2 } .\tag{44}
$$

It is observed that (44) differs from (20) in the term $\begin{array} { r } { \frac { 1 } { M ^ { 2 } } | \sum _ { m = 1 } ^ { M } e ^ { \mathrm { j } \frac { 2 \pi } { \lambda } b _ { m } \Delta \Phi _ { k , k ^ { \prime } } } | ^ { 2 } \leq 1 } \end{array}$ , which characterizes the capability of the MA array mounted on each UAV to distinguish UE k and $k ^ { \prime }$ in the spatial domain. Thus, the IUI can be mitigated by adjusting not only the UAV swarm placement positions, but also the local positions of MAs at all UAVs.

In particular, when the USA is adopted, i.e., $\begin{array} { r l } { b _ { m } } & { { } = } \end{array}$ $\left( m - 1 \right) \Gamma d \ = \ \left( m - 1 \right) \Gamma \lambda / 2$ , where $\Gamma \geq 1$ denotes the sparsity level [27], [45], (44) reduces to

![](images/ca006440fc993ebfb01a5c82f11d2726b71da8d7d75feba3474a433a7bcd1a08.jpg)  
Fig. 2. The channels’ squared-correlation coefficient $\xi _ { 1 , 2 }$ versus ς and Γ.

$$
\begin{array} { c } { { \displaystyle { \xi _ { k , k ^ { \prime } } = \frac { 1 } { L ^ { 2 } } \left| \sum _ { l = 1 } ^ { L } e ^ { \mathrm { j } \frac { 2 \pi } { \lambda } \left( \kappa _ { k } ^ { T } - \kappa _ { k ^ { \prime } } ^ { T } \right) } \mathbf { q } _ { l } \right| ^ { 2 } } } } \\ { { \displaystyle { \times \frac { 1 } { M ^ { 2 } } \left| \frac { \sin { \left( \frac { \pi M \Gamma \Delta \Phi _ { k , k ^ { \prime } } } { 2 } \right) } } { \sin { \left( \frac { \pi \Gamma \Delta \Phi _ { k , k ^ { \prime } } } { 2 } \right) } } \right| ^ { 2 } } . } } \end{array}\tag{45}
$$

Then, the coefficient $\xi _ { k , k ^ { \prime } }$ is equal to zero when sparsity level satisfies

$$
\Gamma \in \left\{ \frac { 2 \varepsilon } { M \Delta \Phi _ { k , k ^ { \prime } } } \bigg | \varepsilon \in \mathbb { Z } , \frac { 2 \varepsilon } { M \Delta \Phi _ { k , k ^ { \prime } } } \geq 1 , \mathrm { m o d } \left( \varepsilon , M \right) \neq 0 \right\} .\tag{46}
$$

Fig. 2 shows the channels’ squared-correlation coefficient $\xi _ { 1 , 2 }$ versus ς and Γ for the two-UE communication, by considering the placement positions given in (21) and (22). The UE directions are $( \theta _ { 1 } , \phi _ { 1 } ) = ( 3 0 ^ { \circ } , 6 0 ^ { \circ } )$ and $( \theta _ { 2 } , \phi _ { 2 } ) =$ $( 0 ^ { \circ } , 0 ^ { \circ } )$ , respectively. The number of UAVs is $L \ = \ 4 ,$ and each UAV is equipped with a USA with $M \ = \ 4$ antennas. For convenience of presentation, the coefficient $\xi _ { 1 , 2 }$ below −200 dB is truncated to −200 dB. It is observed that when ς satisfies (59) in Appendix A, the coefficient $\xi _ { 1 , 2 }$ is equal to zero, i.e., the channel of UE 1 is orthogonal to that of UE 2, and an IUI-free communication can be obtained. It is also observed that the coefficient $\xi _ { 1 , 2 }$ can be reduced by adjusting the sparsity level Γ, and thus providing an extra DoF for IUI mitigation as compared to the single-antenna UAV.

## B. Arbitrary Number of UEs

Furthermore, for arbitrary number of UEs, an alternating optimization algorithm similar to Algorithm 1 is proposed, where the receive beamforming, UAV swarm placement positions, and local positions of MAs are alternately optimized in an iterative manner.

1) Optimization of V With Given Q and B: The optimization of receive beamforming is the same as (25), which are omitted for brevity.

2) Optimization of q With Given $V , \ \{ \mathbf { q } _ { l ^ { \prime } } , \forall l ^ { \prime } \neq l \}$ , and $B \colon$ Let $\tilde { \mathbf { h } } _ { i , l } \in \mathbb { C } ^ { ( L - \mathrm { 1 } ) \tilde { M } \times 1 }$ denote the resulting channel after removing $\mathbf { h } _ { i , l } \in \mathbb { C } ^ { M \times 1 } = \alpha _ { i } \mathbf { a } _ { i , l }$ from $\mathbf { h } _ { i } , \tilde { \mathbf { v } } _ { k , l } \in \mathbb { C } ^ { ( L - 1 ) M \times 1 }$ denote the resulting beamforming after removing $\mathbf { v } _ { k , l } ~ \in$ $\mathbb { C } ^ { M \times 1 }$ from $\mathbf { v } _ { k } .$ , where $\mathbf { h } _ { i , l }$ and $\mathbf { v } _ { k , l }$ denote the l-th block of $\mathbf { h } _ { i }$ and $\mathbf { v } _ { k } .$ , respectively. For the case of multi-antenna UAV, after some manipulations, $f _ { k , i } = \left| \mathbf { v } _ { k } ^ { H } \mathbf { h } _ { i } \right| ^ { 2 }$ can be expressed as

$$
\begin{array} { r } { f _ { k , i } = \underbrace { \sum _ { l ^ { \prime } = 1 , l ^ { \prime } \neq l } ^ { L } { 2 { \left| { \alpha _ { i } } \right| } ^ { 2 } { \mathrm { R e } } \left\{ { e ^ { \mathrm { j } \frac { { 2 \pi } } { \lambda } \left( { r _ { i , l } } - { r _ { i , l ^ { \prime } } } \right) } { \bf { d } } _ { i , l } ^ { H } { { \bf { V } } _ { k , l , l ^ { \prime } } } { \bf { d } } _ { i , l ^ { \prime } } } \right\} } } _ { \tilde { g } _ { k , i } , l } } \\ { + \underbrace { { \left| { \alpha _ { i } } \right| } ^ { 2 } { \bf { d } } _ { i , l } ^ { H } { { \bf { V } } _ { k , l , l } } { \bf { d } } _ { i , l } + \tilde { { \bf { h } } } _ { i , l } ^ { H } { \tilde { { \bf { V } } } _ { k , l , l } } { \tilde { { \bf { h } } } _ { i , l } } } _ { \tilde { g } _ { k , i , l } } , } \end{array}\tag{7}
$$

where $\mathbf { d } _ { i , l } ~ = ~ \Bigl [ e ^ { - \mathrm { j } \frac { 2 \pi } { \lambda } \kappa _ { i , l } ^ { T } \mathbf { b } _ { l , 1 } } , \cdot \cdot \cdot ~ , e ^ { - \mathrm { j } \frac { 2 \pi } { \lambda } \kappa _ { i , l } ^ { T } \mathbf { b } _ { l , M } } \Bigr ] ^ { T } , ~ \mathbf { V } _ { k , l , l ^ { \prime } } \in \mathrm { ~ V ~ } ,$ $\begin{array} { r } { \mathbb { C } ^ { M \times M } \triangleq \mathbf { v } _ { k , l } \mathbf { \bar { v } } _ { k , l ^ { \prime } } ^ { H } , } \end{array}$ , and $\tilde { \mathbf { V } } _ { k , l , l } ~ \in ~ \mathbb { C } ^ { ( L - 1 ) \tilde { M } \times ( L - 1 ) M } ~ \triangleq$ $\tilde { \mathbf { v } } _ { k , l } \tilde { \mathbf { v } } _ { k , l } ^ { H }$ . Moreover, we adopt the quasi-static local AoA approximation, ${ \hat { g } } _ { k , i , l }$ is a constant term, and $\tilde { g } _ { k , i , l }$ can be expressed in terms of $\mathbf { q } _ { l }$ as

$$
\begin{array} { l } { r } { \displaystyle \tilde { g } _ { k , i , l } = \sum _ { l ^ { \prime } = 1 , l ^ { \prime } \neq l } ^ { L } 2 | \alpha _ { i } | ^ { 2 } \left| \mathbf { d } _ { i , l } ^ { H } \mathbf { V } _ { k , l , l ^ { \prime } } \mathbf { d } _ { i , l ^ { \prime } } \right| \times } \\ { \displaystyle \cos \bigg ( \frac { 2 \pi } { \lambda } \left( r _ { i , l } - r _ { i , l ^ { \prime } } \right) + \angle \mathbf { d } _ { i , l } ^ { H } \mathbf { V } _ { k , l , l ^ { \prime } } \mathbf { d } _ { i , l ^ { \prime } } \bigg ) . } \end{array}\tag{48}
$$

A closer look at (48) shows that it has a similar form to (31), and its lower and upper bounds can be correspondingly obtained. As a result, the optimization of $\mathbf { q } _ { l }$ for the multiantenna UAV can follow the similar procedure as in (38).

3) Optimization of $b _ { l , m } \mathrm { ~  ~ { ~ \textit ~ { ~ W ~ i t h } } ~ }$ Given $V , \quad Q ,$ and $\{ b _ { l ^ { \prime } , m ^ { \prime } } , \forall l ^ { \prime } \neq l , m ^ { \prime } \neq m \}$ : The sub-problem of (P1) for optimizing $b _ { l , m }$ is

max ρ   
b<sub>l,m</sub>,ρ   
s.t. R<sub>k</sub> ≥ ρ, ∀k,   
$b _ { l , m } \in \tilde { \mathcal { C } } ,$   
|b<sub>l,m</sub> − b<sub>l,m</sub>0 |<sup>2</sup> ≥ <sup>˜</sup>d<sup>2</sup><sub>min</sub>, ∀m<sup>0</sup> 6= m.

(49)

By following the similar procedure as in Section III-B2, problem (49) can be transformed to

```perl
max<sub>bl,m,ρ,{ηk,µk}Kk=1</sub> ρ
s.t. $\eta _ { k } - \mu _ { k } \geq \rho \ln 2 , \forall k \in \mathcal { K } ,$
$\sigma ^ { 2 } + \sum _ { i = 1 } ^ { K } P _ { i } \big | \mathbf { v } _ { k } ^ { H } \mathbf { h } _ { i } \big | ^ { 2 } \geq \sigma ^ { 2 } e ^ { \eta _ { k } } , \ \forall k \in \mathcal { K } ,$
$\sigma ^ { 2 } + \sum _ { i = 1 , i \neq k } ^ { K } P _ { i } { \big | } { \mathbf { v } _ { k } ^ { H } } { \mathbf { h } _ { i } } { \big | } ^ { 2 } \leq \sigma ^ { 2 } e ^ { \mu _ { k } } , \ \forall k \in \mathcal { K } ,$
$b _ { l , m } \in \tilde { \mathcal { C } } ,$
|b<sub>l,m</sub> − b<sub>l,m</sub>0 |<sup>2</sup> ≥ <sup>˜</sup>d<sup>2</sup><sub>min</sub>, ∀m<sup>0</sup> 6= m. (50)
```

Let $\tilde { \mathbf { h } } _ { i , l , m } \in \mathbb { C } ^ { ( L M - 1 ) \times 1 }$ and $\tilde { \mathbf { v } } _ { k , l , m } \in \mathbb { C } ^ { ( L M - 1 ) \times 1 }$ denote the resulting channel and beamforming vector after removing $h _ { i , l , m }$ and $v _ { i , l , m } .$ , respectively, where $h _ { i , l , m }$ and $v _ { k , l , m }$ are the $( ( l - 1 ) M + m )$ -th elements of $\mathbf { h } _ { i }$ and $\mathbf { v } _ { k } .$ , respectively. The term $f _ { k , i } = \left| \mathbf { v } _ { k } ^ { H } \mathbf { h } _ { i } \right| ^ { 2 }$ can be further expressed as

$$
f _ { k , i } = \underbrace { 2 \left| c _ { k , i , l , m } \right| \mathrm { R e } \left\{ e ^ { - \mathrm { j } \left( \frac { 2 \pi } { \lambda } \Phi _ { i , l } b _ { l , m } - \angle c _ { k , i , l , m } \right) } \right\} } _ { g _ { k , i , l , m } } +  \\  \underbrace { \left| \alpha _ { i } \right| ^ { 2 } \left| v _ { k , l , m } \right| ^ { 2 } + \tilde { \mathbf { h } } _ { i , l , m } ^ { H } \tilde { \mathbf { v } } _ { k , l , m } \tilde { \mathbf { v } } _ { k , l , m } ^ { H } \tilde { \mathbf { h } } _ { i , l , m } } _ { \bar { g } _ { k , i , l , m } } ,\tag{51}
$$

where $\begin{array} { r } { c _ { k , i , l , m } \triangleq \tilde { \mathbf { h } } _ { i , l , m } ^ { H } \tilde { \mathbf { v } } _ { k , l , m } v _ { k , l , m } ^ { * } \alpha _ { i } e ^ { - \mathrm { j } \frac { 2 \pi } { \lambda } r _ { i , l } } } \end{array}$ , and $\bar { g } _ { k , i , l , m }$ is independent of $b _ { l , m }$ . Thus, problem (50) can be solved similar to (29).

Algorithm 2 Proposed Alternating Optimization for Solving   
Problem (P1)   
1: Initialize $\mathbf { Q } ^ { ( 0 ) } , \mathbf { B } ^ { ( 0 ) }$ , and $\{ \mathbf { v } _ { k } ^ { ( 0 ) } \}$ randomly, and let $j = 0 .$   
2: repeat   
3: For given $\mathbf { Q } ^ { ( j ) }$ and $\mathbf { B } ^ { ( j ) }$ , obtain the optimal beamform  
ing $\big \{ \mathbf { v } _ { k } ^ { ( j + 1 ) } \big \}$   
4: for $l = 1 : L$ do   
5: Obtain $\{ \mathbf { q } _ { l } ^ { ( j + 1 ) } \}$ similar to problem (38), given   
$\{ \mathbf q _ { 1 } ^ { ( j + 1 ) } , \cdots , \mathbf q _ { l - 1 } ^ { ( j + 1 ) } , \mathbf q _ { l } ^ { ( j ) } , \cdots , \mathbf q _ { L } ^ { ( j ) } \} , \mathbf B ^ { ( j ) }$   
and $\{ \mathbf { v } _ { k } ^ { ( j + 1 ) } \}$   
6: end for   
7: for $l = 1 : L$ do   
8: for $m = 2 \colon M$ do   
9: Obtain $b _ { l . m } ^ { ( j + 1 ) }$ given ${ \bf Q } ^ { ( j + 1 ) } , \{ b _ { 1 , 2 } ^ { ( j + 1 ) } , \cdot \cdot \cdot ,$   
$b _ { l , m - 1 } ^ { ( j + 1 ) } , \tilde { b _ { l , m } ^ { ( j ) } } , \cdot \cdot \cdot b _ { L , M } ^ { ( j ) } \}$ , and $\{ \mathbf v _ { k } ^ { ( j + 1 ) } \}$   
10: end for   
11: end for   
12: Update $j = j + 1 .$   
13: until the fractional increase in the objective function value   
is below a given threshold $\epsilon > 0$

The main procedures for solving problem (P1) are summarized in Algorithm 2. The complexity for obtaining the receive beamforming in step 3 is $\mathcal { O } ( K ( L M ) ^ { 3 } )$ From step 4 to step 6, the complexity is approximately $\mathcal { O } ( I _ { 1 } L ( 2 \bar { K } ) ^ { 3 } )$ , where $I _ { 1 }$ denotes the maximum number of iterations required by SCA for convergence. The complexity from step 7 to step 11 is approximately given by $\dot { \mathcal { O } } ( I _ { 2 } \dot { L } ( M - 1 ) ( \dot { 2 } K ) ^ { 3 } )$ , where $I _ { 2 }$ denotes the maximum number of iterations to converge required by step 9. As a result, the total computational complexity of Algorithm 2 is $\mathcal { O } ( I _ { 3 } K ( L M ) ^ { 3 } \dot { + } I _ { 1 } I _ { 3 } L ( 2 K ) ^ { 3 } \dot { + } I _ { 2 } \dot { I _ { 3 } } L ( M - \bar { 1 } ) ( 2 K ) ^ { 3 } )$ where $I _ { 3 }$ denotes the number of iterations required by the alternating optimization for convergence.

Last, we consider the practical case in the presence of synchronization and position errors. Specifically, let τ<sub>l</sub> denote the synchronization error between the local clock of UAV l and the reference clock, which follows a Gaussian distribution [49], [50]. With slight abuse of notations, let $\bar { \mathbf q } _ { l }$ denote the nominal position of UAV l, and $\bar { \mathbf q } _ { l } ^ { \mathrm { t r u e } } = \bar { \mathbf q } _ { l } + \Delta { \mathbf q } _ { l }$ denote its true position, with $\Delta \mathbf q _ { l } \sim \mathcal N ( \mathbf 0 , \sigma _ { p } ^ { 2 } \mathbf I )$ being the position error of UAV l. By taking into account both the synchronization and position errors, the receive array response vector of UAV for UE k is given by

$$
\begin{array} { r } { \mathbf { a } _ { k , l } ^ { \mathrm { e } } = e ^ { - \mathrm { j } \frac { 2 \pi } { \lambda } r _ { k , l } ^ { \mathrm { t r u e } } } \Big [ e ^ { - \mathrm { j } \frac { 2 \pi } { \lambda } \varphi _ { k } \left( \bar { \mathbf { q } } _ { l , 1 } ^ { \mathrm { t r u e } } \right) } , \cdot \cdot \cdot , e ^ { - \mathrm { j } \frac { 2 \pi } { \lambda } \varphi _ { k } \left( \bar { \mathbf { q } } _ { l , M } ^ { \mathrm { t r u e } } \right) } \Big ] ^ { T } \boldsymbol { \varepsilon } _ { l } ^ { \mathrm { s y n } } , } \end{array}\tag{52}
$$

where $\varepsilon _ { l } ^ { \mathrm { s y n } } = e ^ { - \mathrm { j } 2 \pi f _ { c } \tau _ { l } }$ denotes the phase shift induced by the synchronization error, with $f _ { c }$ being the carrier frequency, and $r _ { k , l } ^ { \mathrm { t r u e } } = \| \bar { \mathbf { q } } _ { l } ^ { \mathrm { t r u e } } - \mathbf { w } _ { k } \|$ . Since the position error is in general much smaller than the link distance, and with the secondorder Taylor approximation to $r _ { k , l } ^ { \mathrm { t r u e } }$ , the receive array response vector in (52) is approximated as

$$
\begin{array} { r l } & { \mathbf { a } _ { k , l } ^ { \mathrm { e } } } \\ & { \approx e ^ { - \mathrm { j } \frac { 2 \pi } { \lambda } r _ { k , l } ^ { \mathrm { s e c o n d } } } \Bigl [ e ^ { - \mathrm { j } \frac { 2 \pi } { \lambda } \varphi _ { k } \left( \bar { \mathbf { q } } _ { l , 1 } \right) } , \cdots , e ^ { - \mathrm { j } \frac { 2 \pi } { \lambda } \varphi _ { k } \left( \bar { \mathbf { q } } _ { l , M } \right) } \Bigr ] ^ { T } \varepsilon _ { l } ^ { \mathrm { s y n } } \varepsilon _ { k , l } ^ { \mathrm { p o s } } , } \end{array}\tag{53}
$$

where $\varepsilon _ { k , l } ^ { \mathrm { p o s } } = e ^ { - \mathrm { j } \frac { 2 \pi } { \lambda } \kappa _ { k , l } ^ { T } \Delta \mathbf { q } _ { l } }$ denotes the phase shift induced by the position error of UAV l for UE k. Thus, the channel from UE k to the UAV swarm enabled MA system with synchronization and position errors is

$$
\begin{array} { r } { \mathbf { h } _ { k } ^ { \mathrm { e } } = \alpha _ { k } \Big [ \big ( { \mathbf { a } } _ { k , 1 } ^ { \mathrm { e } } \big ) ^ { T } , \cdot \cdot \cdot , \big ( { \mathbf { a } } _ { k , L } ^ { \mathrm { e } } \big ) ^ { T } \Big ] ^ { T } . } \end{array}\tag{54}
$$

Furthermore, we propose a channel estimation-based error compensation scheme to effectively mitigate the adverse effects of synchronization and position errors. It is worth mentioning that both the synchronization and position errors can be regarded as the non-ideal factors of channels from UEs to the UAV swarm enabled MA system. To mitigate the practical issues, when the UAV swarm arrives at the optimized placement positions based on the ideal channel, channel estimation is performed. Specifically, let $\mathbf { S } \in \mathbb { C } ^ { T _ { p } \times K } = [ \mathbf { s } _ { 1 } , \cdots , \mathbf { s } _ { K } ]$ where $\mathbf { s } _ { k } \in \mathbb { C } ^ { T _ { p } ^ { * } \times 1 }$ denotes the pilot sequence of length $T _ { p }$ for UE k, with $\mathbf { S } ^ { H } \mathbf { S } = T _ { p } \mathbf { I } _ { K }$ . The received signal of the UAV swarm enabled MA system can be expressed as

$$
\begin{array} { r } { \mathbf { Y } = \sqrt { p _ { \mathrm { t r } } } \mathbf { H } \mathbf { S } ^ { T } + \mathbf { Z } , } \end{array}\tag{55}
$$

where $p _ { \mathrm { t r } }$ denotes the training power, $\mathbf { H } ~ \in ~ \mathbb { C } ^ { L M \times K } ~ =$ $[ \mathbf { h } _ { 1 } ^ { \mathrm { e } } , \cdot \cdot \cdot \cdot , \mathbf { h } _ { K } ^ { \mathrm { e } } ] , \ \mathbf { Z } \ \in \ \mathbb { C } ^ { L M \times T _ { p } }$ denotes the AWGN matrix. By applying the least-square (LS) estimation, the estimated channel of UE k can be expressed as

$$
\hat { \mathbf { h } } _ { k } = \frac { 1 } { \sqrt { p _ { \mathrm { t r } } } T _ { p } } \mathbf { Y } \mathbf { s } _ { k } ^ { * } .\tag{56}
$$

Based on the estimated channels of UEs, the receive beamforming for UE k is updated to $\begin{array} { r } { \hat { \mathbf { v } } _ { k } = \frac { \hat { \mathbf { C } } _ { k } ^ { - 1 } \hat { \mathbf { h } } _ { k } } { \left\| \hat { \mathbf { C } } _ { k } ^ { - 1 } \hat { \mathbf { h } } _ { k } \right\| } , } \end{array}$ , ∀k, where $\begin{array} { r } { \hat { \mathbf { C } } _ { k } \triangleq \mathbf { I } _ { L M } + \sum _ { i = 1 , i \neq k } ^ { K } \bar { P } _ { i } \hat { \mathbf { h } } _ { i } \hat { \mathbf { h } } _ { i } ^ { H } } \end{array}$ . Then, the achievable rate of the channel estimation-based error compensation scheme for UE k is given by

$$
\hat { R } _ { k } = \log _ { 2 } \left( 1 + \hat { \gamma } _ { k } \right) = \log _ { 2 } \left( 1 + \frac { \bar { P } _ { k } \hat { \mathbf { v } } _ { k } ^ { H } \mathbf { h } _ { k } ^ { \mathrm { e } } ( \mathbf { h } _ { k } ^ { \mathrm { e } } ) ^ { H } \hat { \mathbf { v } } _ { k } } { \hat { \mathbf { v } } _ { k } ^ { H } \mathbf { C } _ { k } ^ { \mathrm { e } } \hat { \mathbf { v } } _ { k } } \right) ,\tag{¯q<sub>l</sub>}
$$

(57)

where $\begin{array} { r } { \mathbf { C } _ { k } ^ { \mathrm { e } } \triangleq \mathbf { I } _ { L M } + \sum _ { i = 1 , i \neq k } ^ { K } \bar { P } _ { i } \mathbf { h } _ { i } ^ { \mathrm { e } } ( \mathbf { h } _ { i } ^ { \mathrm { e } } ) ^ { H } } \end{array}$ . Accordingly, the minimum achievable rate among K UEs can be obtained.

![](images/ab6aae799037efa643afb44ed95f00072f35f2a42d05f3a4f314a2f9482c0dd1.jpg)  
Fig. 3. Convergence behaviour of Algorithm 1.

## V. NUMERICAL RESULTS

In this section, numerical results are provided to verify the performance of the proposed low-altitude UAV swarm enabled MA system. The channel power at the reference distance of $d _ { 0 } \ = \ 1$ m is $\beta _ { 0 } ~ = ~ - 6 1 . 4 ~ \mathrm { d B }$ , and the noise power is $\sigma ^ { 2 } = - 9 4$ dBm. The minimum distance to avoid the collision among UAVs is $d _ { \operatorname* { m i n } } = 1 \mathrm { m }$ . Moreover, the minimum distance to avoid mutual coupling between adjacent MA elements is $\tilde { d } _ { \mathrm { m i n } } = \lambda / 2$ . The (local) movable region of MAs at each UAV is $[ 0 , D ] ,$ , with $D = 2 0 \lambda$ . Unless otherwise stated, K = 3 UEs are uniformly distributed in a circular area with the center and radius being $[ 0 , 0 , 0 ] ^ { T }$ m and $R _ { c } = 6 0 0 ~ \mathrm { m }$ , respectively. The transmit power of each UE is $P _ { k } ~ = ~ 2 0$ dBm. The movable region of UAVs is specified by $\bar { x } _ { l } \ \in \ [ x _ { \operatorname* { m i n } } , x _ { \operatorname* { m a x } } ]$ m, $\bar { y } _ { l } ~ \in ~ [ y _ { \operatorname* { m i n } } , y _ { \operatorname* { m a x } } ]$ m, and $\bar { z } _ { l } \in \mathsf { \Gamma } [ H , H + z _ { \operatorname* { m a x } } ]$ m, with $x _ { \mathrm { m i n } } = y _ { \mathrm { m i n } } = - 5 0$ m, $x _ { \mathrm { m a x } } = y _ { \mathrm { m a x } } = 5 0$ m, z<sub>max</sub> = 40 m, and $H = 5 0 0$ m.

## A. Single-Antenna UAV

First, we consider the case of single-antenna UAVs, with $L \ = \ 4$ . Fig. 3 shows the convergence behaviour of Algorithm 1. The upper bound of IUI-free communication is also provided for comparison, i.e., the result given in (23). It is observed that Algorithm 1 yields a non-decreasing minimum achievable rate, and finally approaches the converged solution that is close to the IUI-free upper bound.

Fig. 4 shows the minimum achievable rate versus the transmit power of each UE for the two-UE communication, by considering the UE directions $( \theta _ { 1 } , \phi _ { 1 } ) = ( 3 0 ^ { \circ } , 6 0 ^ { \circ } )$ and $( \theta _ { 2 } , \phi _ { 2 } ) = ( 0 ^ { \circ } , 0 ^ { \circ } )$ , respectively. The movable region of UAVs is specified by ${ \bar { x } } _ { l } ~ \in ~ [ x _ { \operatorname* { m i n } } , x _ { \operatorname* { m a x } } ] ~ \mathrm { m } , ~ { \bar { y } } _ { l } ~ \in ~ [ y _ { \operatorname* { m i n } } , y _ { \operatorname* { m a x } } ] ~ \mathrm { m }$ , and $\bar { z } _ { l } \in \mathsf { \Gamma } [ H , H + z _ { \operatorname* { m a x } } ]$ m, with $x _ { \mathrm { m i n } } = y _ { \mathrm { m i n } } = - 2 0 \mathrm { ~ m ~ }$ $x _ { \mathrm { m a x } } = y _ { \mathrm { m a x } } = 2 0 ~ \mathrm { m } , z _ { \mathrm { m a x } } = 1 0 ~ \mathrm { m }$ , and $H = 1 0 0 0 \mathrm { ~ m ~ }$ . For comparison, the benchmark scheme of circular array geometry is considered, i.e., the UAV swarm cooperatively forms a circular array, with their placement positions given by

$$
\mathbf { \Psi } = \mathbf { q } _ { r } + \left[ R \cos \left( \frac { 2 \pi } { L } \left( l - 1 \right) \right) , R \sin \left( \frac { 2 \pi } { L } \left( l - 1 \right) \right) , 0 \right] ^ { T } , \forall l ,\tag{58}
$$

![](images/03b061bab1ae40c70e444b73e7c10bc3a19b7d0424efa25302b3abd07b3b2f2a.jpg)

Fig. 4. The minimum achievable rate versus the transmit power of each UE for the two-UE communication in the single-antenna UAV case.  
![](images/e5606a8c53f8efd27ccce77755b330610640e155ae0a1ef0d49385c1eee02c1f.jpg)  
Fig. 5. The SNR loss factor versus the transmit power for the two-UE communication in the single-antenna UAV case.

where R denotes the radius of circular array geometry and is set as $R = \left( x _ { \operatorname* { m a x } } - x _ { \operatorname* { m i n } } \right) / 2 = \left( y _ { \operatorname* { m a x } } - y _ { \operatorname* { m i n } } \right) / 2$ . With the circular array geometry, the MMSE, ZF and MRC beamforming schemes are respectively considered. It is observed that the proposed UAV swarm enabled MA system achieves an IUIfree communication, thanks to the flexible placement position optimization. Besides, the proposed scheme outperforms the benchmark schemes of circular array geometry with MMSE, ZF, and MRC beamforming. This is expected since the proposed scheme is able to completely orthogonalize the channels of two UEs, while achieving the full beamforming gain at each UE. Specifically, Fig. 5 shows the SNR loss factor versus the transmit power for UE 1. It is observed that the proposed scheme always enjoys a zero SNR loss factor. By contrast, the circular array geometry with MMSE and MRC beamforming schemes experience increased SNR loss factors as the transmit power increases, as a result of suffering from more severe IUI, especially for the MRC beamforming scheme.

For further comparison, Fig. 6 shows the minimum achievable rate versus the transmit power of each UE for $K = 3$ UEs. Since MMSE beamforming achieves the balance between reducing the interference and noise enhancement, the benchmark scheme of circular array geometry with MMSE beamforming is considered in the following. Moreover, the benchmark scheme of distributed MIMO is considered [51], where four single-antenna access points (APs) cooperatively serve the UEs, and their locations are given by $[ R _ { c } / 2 , { \dot { R } } _ { c } / 2 , 0 ] ^ { T } , [ - R _ { c } / 2 , R _ { c } / 2 , 0 ] ^ { T } , [ - R _ { c } / 2 , - { \dot { R _ { c } } } / 2 , 0 ] ^ { \bar { T } }$ $[ R _ { c } / 2 , - R _ { c } / 2 , 0 ] ^ { T }$ , respectively, with $R _ { c } ~ = ~ 1 0 0 0$ m. It is firstly observed that the minimum achievable rate of both the proposed and benchmark schemes increase as the transmit power increases, as expected. Besides, similar to the case of two UEs, the proposed UAV swarm enabled MA system yields a comparable performance to the IUI-free upper bound, and is significantly superior to the benchmark scheme of circular array geometry with MMSE beamforming. This is expected since the proposed scheme can strike a good balance between the beamforming gain improvement and IUI mitigation via the flexible UAV placement position adjustment. It is also observed that the proposed scheme outperforms the benchmark scheme of distributed MIMO as the transmit power increases. This is expected since although the distributed MIMO deploys the geographically separated APs, their fixed-position antennas cannot exploit the channel variation in the spatial domain for mitigating the IUI.

![](images/7ac6fda663d2afcca8a5d2dbf83787e69e057e7508a49b89dcb755d5feb13e11.jpg)  
Fig. 6. The minimum achievable rate versus the transmit power of each UE for three UEs in the single-antenna UAV case.

Fig. 7 shows the minimum achievable rate versus the number of UEs, K. It is observed that the performance of both schemes decrease as the number of UEs increases. This is because more UEs will cause a severer IUI issue, especially when the number of UAVs/antennas is smaller than that of $\mathrm { U E s , ~ e . g . , ~ } K ~ > ~ 4$ . It is also observed that the minimum achievable rate of the proposed UAV swarm enabled MA system always surpasses the benchmark scheme of circular array geometry, thanks to the flexible UAV placement position adjustment to significantly reduce the channel correlation and thus the IUI among UEs.

## B. Multi-Antenna UAV

Next, we consider the case of multi-antenna UAVs, where the numbers of UAVs and MAs per UAV are $L \ = \ 2$ and $M \ = \ 4 .$ , respectively. For comparison, the following two benchmark schemes are considered: 1) Circular array geometry with FPA: each UAV is equipped with an FPA array (linear) and UAV swarm adopts the circular geometry given in (58); 2) Placement optimization with FPA: each UAV is equipped with the FPA array as above and UAV swarm placement is optimized similar to Section IV-B. Fig. 8 shows the minimum achievable rate versus the transmit power of each UE for the case with $K = 3 ~ \mathrm { U E s }$ . It is observed that the performance of UAV swarm enabled MA system is very close to that of the IUI-free communication, and its performance gains over the other two benchmark schemes become even more significant as the transmit power increases. This is due to the two-level mobility brought by UAV swarm enabled MA system, i.e., the intrinsic mobility of UAV swarm and additional antenna position adjustment of MA. Specifically, it can be observed that the scheme of placement optimization with FPA yields a better performance than that of circular UAV geometry with FPA, which demonstrates the importance of UAV swarm placement optimization for performance improvement. Moreover, compared to the scheme of placement optimization with FPA, considerable performance gain is achieved for UAV swarm enabled MA system, thanks to the additional antenna position adjustment of MA. The above results verify the advantages of two-level mobility brought by UAV swarm enabled MA system, i.e., it can fully exploit channel variation for balancing the beamforming gain improvement and IUI reduction.

![](images/1d66a96de195aa4e58112dae09ac6c27f68ea0bfc32539aa16959994967302ea.jpg)  
Fig. 7. The minimum achievable rate versus the number of UEs in the singleantenna UAV case.

![](images/98a1e476043fd9f6ad472b31acaaae8734634a29ea0487c9f73b13aa364ffe9a.jpg)  
Fig. 8. The minimum achievable rate versus the transmit power of each UE in the multi-antenna UAV case.

![](images/6f5dde24402607c2ddf22a1cc059c271b523816b80703532bb9c7b0c75404f77.jpg)  
(a) K = 2

![](images/3c958e91ec55fd0a1fd50fdaba44a3f8e9b7099cd49cf5bfbac2ca7525bb1ff6.jpg)  
(b) K = 3  
Fig. 9. The minimum achievable rate versus the normalized movable region size in the multi-antenna UAV case.

Fig. 9 studies the impact of the normalized movable region size $D / \lambda$ on the minimum achievable rate. For $K = 2 ,$ , the transmit power of each UE is $P _ { k } = 3 5 \ : \mathrm { d B m }$ , the UE directions remain consistent with those in Fig. 4, and the following three schemes are considered: 1) Placement optimization with USA: each UAV is equipped with a USA and UAV swarm adopts the placement given in (21) and (22); 2) Circular array geometry with USA: each UAV is equipped with a USA and UAV swarm adopts the circular geometry given in (58); 3) Circular array geometry with FPA: Similar to 2), but using FPA instead USA. For USA, the sparsity level can be dynamically adjusted. It is firstly observed from Fig. 9(a) that the scheme of placement optimization with USA directly achieves the IUI-free communication. This is because the placement given in (21) and (22) orthogonalizes the channels of two UEs. On the other hand, as the normalized movable region size increases, the scheme of circular array geometry with USA also achieves the IUI-free communication, thanks to the extra DoF of sparsity level adjustment for completely eliminating the IUI. Moreover, for $K = 3 .$ , it is observed from Fig. 9(b) that the performance of two FPA schemes remain unchanged as the normalized movable region size increases, as expected. By contrast, the performance of the proposed UAV swarm enabled MA system first increases and ultimately converges as the normalized movable region size increases. This is mainly attributed to the fact that with an enlarged movable region size, MA array has a larger spatial DoF to create favorable channels for performance improvement. However, this does not mean that the performance gain of UAV swarm enabled MA system over other benchmark schemes will continuously increase, since it is upper-bounded by the performance under IUI-free communication.

![](images/e86bf82dc4937c2e8da21bb5bc94c7c92a895f85f0febd947b186252a1f6b53f.jpg)  
Fig. 10. Comparison of the minimum achievable rate for the cases with and without synchronization and position errors.

Last, Fig. 10 compares the minimum achievable rate for the cases with and without synchronization and position errors, where for the former, the proposed channel estimationbased error compensation scheme is considered. The standard deviations of synchronization and position errors are 31.6µs, and $\sigma _ { p } ~ = ~ \lambda$ , respectively. The length of pilot sequence is $T _ { p } = 6 0$ , and the training power is $p _ { \mathrm { t r } } = P$ . It is observed that the proposed channel estimation-based error compensation scheme yields a comparable performance to the case without errors, which demonstrates the effectiveness of the proposed scheme in compensating for synchronization and position uncertainties.

## VI. CONCLUSION

This paper proposed a novel UAV swarm enabled two-level MA system to support low-altitude economy, by exploiting the controllable mobility of UAV and antenna position adjustment of MA. An optimization problem was formulated to maximize the minimum achievable rate over all ground UEs, by jointly optimizing 3D UAV swarm placement positions, their individual MAs’ positions, and receive beamforming for UEs. To gain useful insights, we first considered the special case of single-antenna UAV. It was shown that the resulting SNR of single UE communication is independent of UAV swarm array geometry, and the optimal UAV swarm placement positions were derived in closed-form for two-UE communication. For arbitrary number of UEs, an alternating optimization algorithm was proposed to efficiently solve the formulated non-convex problem. Moreover, the results of single-antenna UAV were extended to the general case with multi-antenna UAV. Numerical results demonstrated that significant performance gains can be achieved for the proposed UAV swarm enabled MA system over various benchmarks, thanks to the two-level antenna mobility to create more favorable channels.

In addition, there are many important research directions that could be pursued in the future. For instance, the channel modeling incorporating the array misalignment and orientation jitter issues, as well as the extension to multi-path channels, are worthwhile to investigate. Besides achievable rate, energy consumption and latency are the important performance metrics for UAV swarm enabled MA system, while designing the energy-efficient and low-latency UAV system needs more in-depth studies. Moreover, the flight control mechanisms of UAV swarm to guarantee the safety and mission execution are important to investigate in the future. Last, how to integrate IRS into UAV swarm enabled MA systems is an interesting direction that deserves further investigation.

## APPENDIX A PROOF OF THEOREM 1

By substituting $\begin{array} { r } { \mathbf q _ { l } = \mathbf q _ { 1 } + ( l - 1 ) \times \frac { ( \varsigma + 1 / L ) \lambda } { \| \kappa _ { k } - \kappa _ { k ^ { \prime } } \| ^ { 2 } } \left( \kappa _ { k } - \kappa _ { k ^ { \prime } } \right) } \end{array}$ into (20), where ς is a common coefficient to all the UAVs, given by

$$
\varsigma \in \left\{ \frac { \nu } { L } \bigg \vert \nu \in \mathbb { Z } , \mathrm { m o d } \left( \nu + 1 , L \right) \neq 0 \right\} ,\tag{59}
$$

it can be verified that the objective value of (20) is equal to zero. Moreover, the distance between UAV l and $l ^ { \prime }$ is given by

$$
\| { \bf q } _ { l } - { \bf q } _ { l ^ { \prime } } \| = \left\| \left( l - l ^ { \prime } \right) \left( \varsigma + 1 / L \right) \lambda \frac { \left( \kappa _ { k } - \kappa _ { k ^ { \prime } } \right) } { \left\| \kappa _ { k } - \kappa _ { k ^ { \prime } } \right\| ^ { 2 } } \right\|
$$

$$
\geq \left\| \left( \varsigma + 1 / L \right) \lambda \frac { \left( \kappa _ { k } - \kappa _ { k ^ { \prime } } \right) } { \left\| \kappa _ { k } - \kappa _ { k ^ { \prime } } \right\| ^ { 2 } } \right\| = \frac { \lambda \left| \varsigma + 1 / L \right| } { \left\| \kappa _ { k } - \kappa _ { k ^ { \prime } } \right\| } .\tag{60}
$$

To satisfy the minimum safe distance constraint for UAVs, a feasible solution of $\varsigma$ is thus given by (22). This completes the proof of Theorem 1.

## APPENDIX B PROOF OF LEMMA 1

With $g _ { k , i , l }$ given in (31), its lower and upper bounds can be constructed based on the second-order Taylor expansion [25], [52], [53]. Specifically, the gradient of $g _ { k , i , l }$ over $\mathbf { q } _ { l }$ is $\begin{array} { r } { \nabla g _ { k , i , l } = \left[ \frac { \partial g _ { k , i , l } } { \partial x _ { l } } , \frac { \partial g _ { k , i , l } } { \partial y _ { l } } , \frac { \partial g _ { k , i , l } } { \partial z _ { l } } \right] ^ { T } } \end{array}$ , where

$$
\begin{array} { l } { \displaystyle \frac { \partial g _ { k , i , l } } { \partial x _ { l } } = - \frac { 2 \pi } { \lambda } \sum _ { l ^ { \prime } = 1 , l ^ { \prime } \neq l } ^ { L } 2 | \alpha _ { i } | ^ { 2 } | V _ { k , l , l ^ { \prime } } | \frac { \partial r _ { i , l } } { \partial x _ { l } } } \\ { \displaystyle \times \sin \left( \frac { 2 \pi } { \lambda } \left( r _ { i , l } - r _ { i , l ^ { \prime } } \right) + \angle V _ { k , l , l ^ { \prime } } \right) , } \end{array}\tag{61}
$$

$$
\begin{array} { l } { \displaystyle \frac { \partial g _ { k , i , l } } { \partial y _ { l } } = - \frac { 2 \pi } { \lambda } \sum _ { \nu = 1 , \nu \neq l } ^ { L } { 2 \vert \alpha _ { i } \vert ^ { 2 } \vert V _ { k , l , \nu } \vert \cdot \frac { \partial r _ { i , l } } { \partial y _ { l } } } } \\ { \displaystyle \qquad \times \sin \left( \frac { 2 \pi } { \lambda } \left( r _ { i , l } - r _ { i , \nu } \right) + \mathcal { L } V _ { k , l , \nu } \right) , } \\ { \displaystyle \frac { \partial g _ { k , i , l } } { \partial z _ { l } } = - \frac { 2 \pi } { \lambda } \sum _ { \nu = 1 , \nu \neq l } ^ { L } { 2 \vert \alpha _ { i } \vert ^ { 2 } \vert V _ { k , l , \nu } \vert \cdot \frac { \partial r _ { i , l } } { \partial z _ { l } } } } \\ { \displaystyle \qquad \times \sin \left( \frac { 2 \pi } { \lambda } \left( r _ { i , l } - r _ { i , \nu } \right) + \mathcal { L } V _ { k , l , \nu } \right) , } \end{array}\tag{62}
$$

(63)

where ∂r<sub>i,l</sub> = Φ<sub>i</sub> x<sub>l</sub>−(x<sub>l</sub>Φ<sub>i</sub>+y<sub>l</sub>Ψ<sub>i</sub>+z<sub>l</sub>Θ<sub>i</sub>)Φ<sub>ir</sub> $\begin{array} { r l r } { \frac { \partial r _ { i , l } } { \partial u _ { l } } } & { { } = } & { \Psi _ { i } ~ + ~ \frac { y _ { l } - ( x _ { l } \Phi _ { i } + y _ { l } \Psi _ { i } + z _ { l } \Theta _ { i } ) \Psi _ { i } } { r _ { i } } } \end{array}$ , and $\begin{array} { r l } { \frac { \partial r _ { i , l } } { \partial z _ { l } } } & { { } = } \end{array}$ Θ<sub>i</sub> + <sup>zl−(xlΦi+ylΨi+zlΘi)Θi</sup> , respectively.

Besides, the Hessian matrix of $g _ { k , i , l }$ over $\mathbf { q } _ { l }$ is

$$
\nabla ^ { 2 } g _ { k , i , l } = \left[ \begin{array} { l l l } { \frac { \partial ^ { 2 } g _ { k , i , l } } { \partial x _ { l } \partial x _ { l } } } & { \frac { \partial ^ { 2 } g _ { k , i , l } } { \partial x _ { l } \partial y _ { l } } } & { \frac { \partial ^ { 2 } g _ { k , i , l } } { \partial x _ { l } \partial z _ { l } } } \\ { \frac { \partial ^ { 2 } g _ { k , i , l } } { \partial y _ { l } \partial x _ { l } } } & { \frac { \partial ^ { 2 } g _ { k , i , l } } { \partial y _ { l } \partial y _ { l } } } & { \frac { \partial ^ { 2 } g _ { k , i , l } } { \partial y _ { l } \partial z _ { l } } } \\ { \frac { \partial ^ { 2 } g _ { k , i , l } } { \partial z _ { l } \partial x _ { l } } } & { \frac { \partial ^ { 2 } g _ { k , i , l } } { \partial z _ { l } \partial y _ { l } } } & { \frac { \partial ^ { 2 } g _ { k , i , l } } { \partial z _ { l } \partial z _ { l } } } \end{array} \right] ,\tag{64}
$$

where

$$
\begin{array} { r l } & { \frac { \partial ^ { 2 } \mathbf { g } _ { \mathrm { p h a c } , 2 } } { \partial \mathbf { z } \partial \mathbf { z } \partial \mathbf { z } } = - \frac { 2 \pi } { \lambda } , \displaystyle \sum _ { \substack { \boldsymbol { c } , - \mathrm { l o r } , \boldsymbol { \omega } \neq \mathbf { z } \neq \mathbf { z } , \boldsymbol { \nu } \in \mathcal { K } } } \Bigg | \mathbf { z } _ { \mathrm { b } , \boldsymbol { u } , \boldsymbol { u } , \boldsymbol { u } ^ { \prime } } \Bigg | \times } \\ & { \Bigg [ \displaystyle \frac { 1 - \mathbf { c } _ { \boldsymbol { c } } ^ { 2 } } { \gamma _ { \boldsymbol { c } } } \mathrm { s i n d } \left( \frac { 2 \pi } { \lambda } ( \boldsymbol { c } _ { \boldsymbol { c } , 2 } - \boldsymbol { v } _ { \boldsymbol { c } , \boldsymbol { u } ^ { \prime } } ) \textbf { i } \cdot \mathcal { K } _ { \mathbf { b } , \boldsymbol { u } ^ { \prime } } \right) + } \\ & { \Bigg . \Bigg . \Bigg . \Bigg . \frac { 2 \pi } { \lambda } \left( \frac { \partial \mathbf { z } _ { \mathrm { c } } } { \partial \boldsymbol { c } } \right) ^ { 2 } \Bigg ] \times \Bigg ( \frac { 2 \pi } { \lambda } ( \boldsymbol { c } _ { \boldsymbol { c } , 2 } - \boldsymbol { v } _ { \boldsymbol { c } , \boldsymbol { u } ^ { \prime } } ) + \mathcal { K } _ { \mathbf { b } , \boldsymbol { u } ^ { \prime } } \Bigg ) \Bigg ] , } \\ & { \frac { \partial ^ { 2 } \mathbf { g } _ { \mathrm { p h a c } , 2 } } { \partial \mathbf { z } \partial \boldsymbol { p } _ { \mathrm { p h a c } , 1 } } = - \frac { 2 \pi } { \lambda } , \displaystyle \sum _ { \substack { \boldsymbol { c } , - \mathrm { l o r } , \boldsymbol { \omega } \neq \mathbf { z } \neq \mathbf { z } , \boldsymbol { \nu } \in \mathcal { K } } } \Bigg ] \Bigg | \mathbf { z } _ { \mathrm { b } , \boldsymbol { u } ^ { \prime } } } \\ &  \Bigg [ \frac  \partial ^ { 2 } \mathbf { g } _ { \mathrm { p h a c } , 1 } ^  \ \end{array}\tag{65}
$$

(66)

$$
\begin{array} { l } { \displaystyle \left[ \frac { - \Phi _ { i } \Theta _ { i } } { r _ { i } } \mathrm { s i n } \left( \frac { 2 \pi } { \lambda } \left( r _ { i , l } - r _ { i , l ^ { \prime } } \right) + \angle V _ { k , l , l ^ { \prime } } \right) + \right. } \\ { \displaystyle \left. \frac { 2 \pi } { \lambda } \frac { \partial r _ { i , l } } { \partial x _ { l } } \frac { \partial r _ { i , l } } { \partial z _ { l } } \mathrm { c o s } \left( \frac { 2 \pi } { \lambda } \left( r _ { i , l } - r _ { i , l ^ { \prime } } \right) + \angle V _ { k , l , l ^ { \prime } } \right) \right] , } \end{array}\tag{67}
$$

and other elements can be similarly obtained based on (61)- (63), which are omitted for brevity.

Moreover, with (64), we have (68), shown at the bottom of the page.

Let $\mathbf { \bar { \phi } } _ { C _ { \mathrm { m a x } } } \triangleq \operatorname* { m a x } _ { \mathbf { q } _ { l } } x _ { l } ^ { 2 } + y _ { l } ^ { 2 } + z _ { l } ^ { 2 }$ , it follows that

$$
\begin{array} { r l } { \left\| { \nabla ^ { 2 } } g _ { k , i , l } \right\| _ { F } ^ { 2 } \le } & { \displaystyle \left( \frac { 2 \pi } { \lambda } \displaystyle \sum _ { l ^ { \prime } = 1 , l ^ { \prime } \neq l } ^ { L } 2 | \alpha _ { i } | ^ { 2 } | V _ { k , l , l ^ { \prime } } | \right) ^ { 2 } } \\ & { \quad \quad \times \displaystyle \left[ \frac { 2 } { r _ { i } ^ { 2 } } + \left( \frac { 2 \pi } { \lambda } \right) ^ { 2 } \left( 1 + \frac { C _ { \operatorname* { m a x } } } { r _ { i } ^ { 2 } } \right) ^ { 2 } \right] . } \end{array}\tag{69}
$$

With $\nabla ^ { 2 } g _ { k , i , l } \preceq \left\| \nabla ^ { 2 } g _ { k , i , l } \right\| _ { 2 } \mathbf { I } ,$ and by choosing $\delta _ { k , i , l } ~ =$ $\begin{array} { r } { \frac { 2 \pi } { \lambda } \underset { l ^ { \prime } = 1 , l ^ { \prime } \neq l } { \sum } 2 \big | \alpha _ { i } \big | ^ { 2 } \big | V _ { k , l , l ^ { \prime } } \big | \sqrt { \frac { 2 } { r _ { i } ^ { 2 } } + \big ( \frac { 2 \pi } { \lambda } \big ) ^ { 2 } \Big ( 1 + \frac { C _ { \operatorname* { m a x } } } { r _ { i } ^ { 2 } } \Big ) ^ { 2 } } } \end{array}$ , we have $\nabla ^ { 2 } g _ { k , i , l } \preceq \delta _ { k , i , l } \mathbf { I }$ . Thus, the lower and upper bounds of $g _ { k , i , l }$ in (32) and (33) can be obtained with the Taylor’s theorem [52]. The proof of Lemma 1 is thus completed.

## APPENDIX C PROOF OF PROPOSITION 1

Denote by $\{ \mathbf { q } _ { l } ^ { ( j ) } \}$ and $\{ \mathbf { v } _ { k } ^ { ( j ) } \}$ the corresponding optimization variables in the $j \mathrm { - t h }$ iteration. Let $\rho _ { \mathrm { l b } } ^ { \mathrm { t r a j } } ( \{ \mathbf { q } _ { l } ^ { ( \bar { j } ) } \} , \{ \mathbf { v } _ { k } ^ { ( j ) } \} )$ denote the corresponding objective value of problem (38). In the j-th iteration, since the optimal solution to (24) is obtained for given $\{ \mathbf { q } _ { l } ^ { ( j ) } \}$ in step 3, it follows that

$$
\rho \left( \left\{ \mathbf { q } _ { l } ^ { \left( j \right) } \right\} , \left\{ \mathbf { v } _ { k } ^ { \left( j \right) } \right\} \right) \leq \rho \left( \left\{ \mathbf { q } _ { l } ^ { \left( j \right) } \right\} , \left\{ \mathbf { v } _ { k } ^ { \left( j + 1 \right) } \right\} \right) .\tag{70}
$$

Besides, regarding UAV l in step 5, for given $\{ \mathbf { v } _ { k } ^ { ( j + 1 ) } \}$ and $\{ \mathbf { q } _ { 1 } ^ { ( j + 1 ) } , \cdot \cdot \cdot , \mathbf { q } _ { l - 1 } ^ { ( j + 1 ) } , \mathbf { q } _ { l } ^ { ( j ) } , \cdot \cdot \cdot , \mathbf { q } _ { L } ^ { ( j ) } \}$ , we have

$$
\rho \left( \left\{ \mathbf { q } _ { 1 } ^ { ( j + 1 ) } , \cdot \cdot \cdot , \mathbf { q } _ { l - 1 } ^ { ( j + 1 ) } , \mathbf { q } _ { l } ^ { ( j ) } , \cdot \cdot \cdot , \mathbf { q } _ { L } ^ { ( j ) } \right\} , \left\{ \mathbf { v } _ { k } ^ { ( j + 1 ) } \right\} \right)
$$

$$
\begin{array} { l } { \displaystyle \| \nabla ^ { 2 } g _ { { \pmb { k } } , { \pmb \lambda } _ { t } } \| _ { 2 } ^ { 2 } \leq \| \nabla ^ { 2 } g _ { { \pmb \kappa } , { \pmb \lambda } _ { t } } \| _ { F } ^ { 2 } = ( \frac { \widetilde \phi d ^ { 2 } g _ { { \pmb \kappa } , { \pmb \lambda } _ { t } } } { \widetilde \eta _ { \pmb \kappa } } ) ^ { 2 } + \cdots + ( \frac { \widetilde \phi d ^ { 2 } g _ { { \pmb \kappa } , { \pmb \lambda } _ { t } } } { \widetilde \mathcal { D } _ { \mathscr { X } } \widetilde { \phi } d _ { { \pmb \kappa } } } ) ^ { 2 } \leq ( \frac { 2 \pi } { \widetilde \lambda } \underset { \widetilde \gamma = 1 } { \widetilde \eta _ { \pmb \kappa } } \frac { L } { \widetilde \Theta } ) ^ { 2 } ( 2 \kappa \underset { t } { \widetilde \eta _ { \pmb \kappa } } \frac { \partial ^ { 2 } } { \widetilde \Theta } ) ^ { 2 } \Bigg | ^ { 2 } \times } \\  \displaystyle [ ( \frac { 1 - \Phi _ { \pmb \kappa } ^ { 2 } } { \widetilde \tau _ { t } } ) ^ { 2 } + ( \frac { 2 \pi } { \widetilde \lambda } ( \frac { \partial \tau _ { \pm , t } } { \partial \tau _ { t } } ) ^ { 2 } ) ^ { 2 } ] ^ { 2 } + ( \frac { \widetilde \Phi d _ { \pm \pm } \Psi _ { \pm } } { \gamma _ { t } } ) ^ { 2 } + ( \frac { 2 \pi } { \widetilde \lambda } \frac { \widetilde \sigma _ { \pmb \kappa } ^ { 2 } } { \widetilde \partial \tau _ { t } } \frac { \partial \tau _ { \pmb \lambda } } { \partial \widetilde \eta _ { \pmb \kappa } } ) ^ { 2 } + ( \frac { \widetilde \Phi d _ { \pm } \Theta _ { \pm } } { \gamma _ { t } } ) ^ { 2 } + ( \frac { 2 \pi } { \widetilde \lambda } \frac { \partial \tau _ { \pm } } { \partial \tau _ { \pm } } \frac  \partial \tau \end{array}\tag{68}
$$

$$
\begin{array} { r l } & { \overset { ( a ) } { = } \rho _ { \mathrm { l b } } ^ { \mathrm { t r a j } } \left( \left\{ \mathbf { q } _ { 1 } ^ { ( j + 1 ) } , \cdots , \mathbf { q } _ { l - 1 } ^ { ( j + 1 ) } , \mathbf { q } _ { l } ^ { ( j ) } , \cdots , \mathbf { q } _ { L } ^ { ( j ) } \right\} , \left\{ \mathbf { v } _ { k } ^ { ( j + 1 ) } \right\} \right) } \\ & { \overset { ( b ) } { \leq } \rho _ { \mathrm { l b } } ^ { \mathrm { t r a j } } \left( \left\{ \mathbf { q } _ { 1 } ^ { ( j + 1 ) } , \cdots , \mathbf { \cdot } \mathbf { \cdot } , \mathbf { q } _ { l - 1 } ^ { ( j + 1 ) } , \mathbf { q } _ { l } ^ { ( j + 1 ) } , \cdots , \mathbf { q } _ { L } ^ { ( j ) } \right\} , \left\{ \mathbf { v } _ { k } ^ { ( j + 1 ) } \right\} \right) } \\ & { \overset { ( c ) } { \leq } \rho \left( \left\{ \mathbf { q } _ { 1 } ^ { ( j + 1 ) } , \cdots , \mathbf { \cdot } , \mathbf { q } _ { l - 1 } ^ { ( j + 1 ) } , \mathbf { q } _ { l } ^ { ( j + 1 ) } , \cdots , \mathbf { q } _ { L } ^ { ( j ) } \right\} , \left\{ \mathbf { v } _ { k } ^ { ( j + 1 ) } \right\} \right) , } \end{array}\tag{71}
$$

where (a) holds because the Taylor expansions are tight at the given local point $\mathbf { q } _ { l } ^ { ( j ) }$ ; the inequality (b) holds because problem (38) is solved via SCA, which ensures a non-decreasing objective value; the inequality (c) holds because the objective value of (26) is lower-bounded by that of (38) at $\mathbf { q } _ { l } ^ { ( j + 1 ) }$ . Based on (70) and (71), we have

$$
\rho \left( \left\{ \mathbf { q } _ { l } ^ { \left( j \right) } \right\} , \left\{ \mathbf { v } _ { k } ^ { \left( j \right) } \right\} \right) \leq \rho \left( \left\{ \mathbf { q } _ { l } ^ { \left( j + 1 \right) } \right\} , \left\{ \mathbf { v } _ { k } ^ { \left( j + 1 \right) } \right\} \right) .\tag{72}
$$

The result shows that the objective value of problem (12) is non-decreasing over iterations, and thus, Algorithm 1 is guaranteed to converge. This thus completes the proof of Proposition 1.

## REFERENCES

[1] H. Lu, Y. Zeng, S. Ma, B. Li, S. Jin, and R. Zhang, “Enabling aerial movable antenna system with UAV swarm for low-altitude economy,” in Proc. IEEE/CIC Int. Conf. Commun. China (ICCC Workshops), Aug. 2025, pp. 1–6.

[2] Y. Jiang et al., “6G non-terrestrial networks enabled low-altitude economy: Opportunities and challenges,” 2023, arXiv:2311.09047.

[3] G. Cheng, X. Song, Z. Lyu, and J. Xu, “Networked ISAC for low-altitude economy: Coordinated transmit beamforming and UAV trajectory design,” IEEE Trans. Commun., vol. 73, no. 8, pp. 5832–5847, Aug. 2025.

[4] Y. Zeng, Q. Wu, and R. Zhang, “Accessing from the sky: A tutorial on UAV communications for 5G and beyond,” Proc. IEEE, vol. 107, no. 12, pp. 2327–2375, Dec. 2019.

[5] M. Mozaffari, W. Saad, M. Bennis, Y.-H. Nam, and M. Debbah, “A tutorial on UAVs for wireless networks: Applications, challenges, and open problems,” IEEE Commun. Surveys Tuts., vol. 21, no. 3, pp. 2334–2360, 3rd Quart., 2019.

[6] Y. Song et al., “An overview of cellular ISAC for low-altitude UAV: New opportunities and challenges,” IEEE Commun. Mag., vol. 63, no. 12, pp. 88–95, Dec. 2025.

[7] Y. Zeng, J. Lyu, and R. Zhang, “Cellular-connected UAV: Potential, challenges, and promising technologies,” IEEE Wireless Commun., vol. 26, no. 1, pp. 120–127, Feb. 2019.

[8] S. Zhang, Y. Zeng, and R. Zhang, “Cellular-enabled UAV communication: A connectivity-constrained trajectory optimization perspective,” IEEE Trans. Commun., vol. 67, no. 3, pp. 2580–2604, Mar. 2019.

[9] Framework and Overall Objectives of the Future Development of IMT for 2030 and Beyond, ITU-R M.2160-0, Jun. 2023. [Online]. Available: https://www.itu.int/rec/R-REC-M.2160/en

[10] J. Mu, R. Zhang, Y. Cui, N. Gao, and X. Jing, “UAV meets integrated sensing and communication: Challenges and future directions,” IEEE Commun. Mag., vol. 61, no. 5, pp. 62–67, May 2023.

[11] Y. Pan et al., “Cooperative trajectory planning and resource allocation for UAV-enabled integrated sensing and communication systems,” IEEE Trans. Veh. Technol., vol. 73, no. 5, pp. 6502–6516, May 2024.

[12] X. Jing, F. Liu, C. Masouros, and Y. Zeng, “ISAC from the sky: UAV trajectory design for joint communication and target localization,” IEEE Trans. Wireless Commun., vol. 23, no. 10, pp. 12857–12872, Oct. 2024.

[13] S. Javed et al., “State-of-the-art and future research challenges in UAV swarms,” IEEE Internet Things J., vol. 11, no. 11, pp. 19023–19045, Jun. 2024.

[14] B. Li, Q. Li, Y. Zeng, Y. Rong, and R. Zhang, “3D trajectory optimization for energy-efficient UAV communication: A control design perspective,” IEEE Trans. Wireless Commun., vol. 21, no. 6, pp. 4579–4593, Jun. 2022.

[15] Q. Li, B. Li, Z.-Q. He, Y. Rong, and Z. Han, “Joint design of communication sensing and control with a UAV platform,” IEEE Trans. Wireless Commun., vol. 23, no. 12, pp. 19231–19244, Dec. 2024.

[16] H. Zhang, B. Li, Y. Rong, Y. Zeng, and R. Zhang, “Joint optimization of transmit power and trajectory for UAV-enabled data collection with dynamic constraints,” IEEE Trans. Commun., vol. 73, no. 9, pp. 8080–8091, Sep. 2025.

[17] S. Javaid et al., “Communication and control in collaborative UAVs: Recent advances and future trends,” IEEE Trans. Intell. Transp. Syst., vol. 24, no. 6, pp. 5719–5739, Jun. 2023.

[18] D. Fan et al., “Channel estimation and self-positioning for UAV swarm,” IEEE Trans. Commun., vol. 67, no. 11, pp. 7994–8007, Nov. 2019.

[19] Z. Mou, Y. Zhang, F. Gao, H. Wang, T. Zhang, and Z. Han, “Deep reinforcement learning based three-dimensional area coverage with UAV swarm,” IEEE J. Sel. Areas Commun., vol. 39, no. 10, pp. 3160–3176, Oct. 2021.

[20] X. Liu, Y. Liu, Z. Liu, and T. S. Durrani, “Fair integrated sensing and communication for multi-UAV-enabled Internet of Things: Joint 3-D trajectory and resource optimization,” IEEE Internet Things J., vol. 11, no. 18, pp. 29546–29556, Sep. 2024.

[21] C. Wang, Z. Wei, W. Jiang, H. Jiang, and Z. Feng, “Cooperative sensing enhanced UAV path-following and obstacle avoidance with variable formation,” IEEE Trans. Veh. Technol., vol. 73, no. 6, pp. 7501–7516, Jun. 2024.

[22] J. Xu, H. Min, and Y. Zeng, “Integrated super-resolution sensing and symbiotic communication with 3D sparse MIMO for low-altitude UAV swarm,” IEEE Trans. Commun., vol. 74, pp. 2812–2826, 2026.

[23] L. Zhu, W. Ma, and R. Zhang, “Movable antennas for wireless communication: Opportunities and challenges,” IEEE Commun. Mag., vol. 62, no. 6, pp. 114–120, Jun. 2024.

[24] L. Zhu, W. Ma, and R. Zhang, “Movable-antenna array enhanced beamforming: Achieving full array gain with null steering,” IEEE Commun. Lett., vol. 27, no. 12, pp. 3340–3344, Dec. 2023.

[25] W. Ma, L. Zhu, and R. Zhang, “MIMO capacity characterization for movable antenna systems,” IEEE Trans. Wireless Commun., vol. 23, no. 4, pp. 3392–3407, Apr. 2024.

[26] L. Zhu et al., “A tutorial on movable antennas for wireless networks,” IEEE Commun. Surveys Tuts., vol. 28, pp. 3002–3054, 2026.

[27] H. Lu, Y. Zeng, S. Jin, and R. Zhang, “Group movable antenna with flexible sparsity: Joint array position and sparsity optimization,” IEEE Wireless Commun. Lett., vol. 13, no. 12, pp. 3573–3577, Dec. 2024.

[28] Z. Dong et al., “Movable antenna for wireless communications: Prototyping and experimental results,” IEEE Trans. Wireless Commun., vol. 25, pp. 6586–6599, 2026.

[29] X. Shao, Q. Jiang, and R. Zhang, “6D movable antenna based on user distribution: Modeling and optimization,” IEEE Trans. Wireless Commun., vol. 24, no. 1, pp. 355–370, Jan. 2025.

[30] X. Shao, R. Zhang, Q. Jiang, and R. Schober, “6D movable antenna enhanced wireless network via discrete position and rotation optimization,” IEEE J. Sel. Areas Commun., vol. 43, no. 3, pp. 674–687, Mar. 2025.

[31] X. Shao, R. Zhang, Q. Jiang, J. Park, T. Q. S. Quek, and R. Schober, “Distributed channel estimation and optimization for 6D movable antenna: Unveiling directional sparsity,” IEEE J. Sel. Topics Signal Process., vol. 19, no. 2, pp. 349–365, Mar. 2025.

[32] X. Shao et al., “A tutorial on six-dimensional movable antenna for 6G networks: Synergizing positionable and rotatable antennas,” IEEE Commun. Surveys Tuts., vol. 28, pp. 3666–3709, 2026.

[33] K.-K. Wong, A. Shojaeifard, K.-F. Tong, and Y. Zhang, “Fluid antenna systems,” IEEE Trans. Wireless Commun., vol. 20, no. 3, pp. 1950–1962, Mar. 2021.

[34] W. K. New et al., “A tutorial on fluid antenna system for 6G networks: Encompassing communication theory, optimization methods and hardware designs,” IEEE Commun. Surveys Tuts., vol. 27, no. 4, pp. 2325–2377, Aug. 2025.

[35] H. Lu and Y. Zeng, “Near-field modeling and performance analysis for multi-user extremely large-scale MIMO communication,” IEEE Commun. Lett., vol. 26, no. 2, pp. 277–281, Feb. 2022.

[36] H. Lu et al., “A tutorial on near-field XL-MIMO communications towards 6G,” IEEE Commun. Surveys Tuts., vol. 26, no. 4, pp. 2213–2257, 4th Quart., Apr. 2024.

[37] H. Lu, Z. Yu, Y. Zeng, S. Ma, S. Jin, and R. Zhang, “Wireless communication with flexible reflector: Joint placement and rotation optimization for coverage enhancement,” IEEE Trans. Wireless Commun., vol. 24, no. 10, pp. 8252–8266, Oct. 2025.

[38] Y. Bai, B. Xie, R. Zhu, Z. Chang, and R. Jantti, “Movable antenna-¨ equipped UAV for data collection in backscatter sensor networks: A deep reinforcement learning-based approach,” in Proc. IEEE Int. Conf. Commun., Jun. 2025, pp. 6560–6565.

[39] X.-W. Tang, Y. Shi, Y. Huang, and Q. Wu, “UAV-mounted movable antenna: Joint optimization of UAV placement and antenna configuration,” 2024, arXiv:2409.02469.

[40] W. Liu, X. Zhang, H. Xing, J. Ren, Y. Shen, and S. Cui, “UAV-enabled wireless networks with movable-antenna array: Flexible beamforming and trajectory design,” IEEE Wireless Commun. Lett., vol. 14, no. 3, pp. 566–570, Mar. 2025.

[41] T. Ren, X. Zhang, L. Zhu, W. Ma, X. Gao, and R. Zhang, “6-D movable antenna enhanced interference mitigation for cellular-connected UAV communications,” IEEE Wireless Commun. Lett., vol. 14, no. 6, pp. 1618–1622, Jun. 2025.

[42] C. Liu, W. Mei, P. Wang, Y. Meng, Z. Chen, and B. Ning, “UAV-enabled passive 6D movable antennas: Joint deployment and beamforming optimization,” IEEE Trans. Wireless Commun., vol. 25, pp. 9765–9781, 2026.

[43] H. Lu, Y. Zeng, S. Jin, and R. Zhang, “Aerial intelligent reflecting surface: Joint placement and passive beamforming design with 3D beam flattening,” IEEE Trans. Wireless Commun., vol. 20, no. 7, pp. 4128–4143, Jul. 2021.

[44] X. Li et al., “Sparse MIMO for ISAC: New opportunities and challenges,” IEEE Wireless Commun., vol. 32, no. 4, pp. 170–178, Aug. 2025.

[45] H. Wang et al., “Enhancing spatial multiplexing and interference suppression for near- and far-field communications with sparse MIMO,” IEEE Trans. Commun., vol. 74, pp. 5765–5782, 2026.

[46] S. Mohanti et al., “AirBeam: Experimental demonstration of distributed beamforming by a swarm of UAVs,” in Proc. IEEE 16th Int. Conf. Mobile Ad Hoc Sensor Syst. (MASS), Nov. 2019, pp. 162–170.

[47] Z. Zuo, C. Liu, Q.-L. Han, and J. Song, “Unmanned aerial vehicles: Control methods and future challenges,” IEEE/CAA J. Autom. Sinica, vol. 9, no. 4, pp. 601–614, Apr. 2022.

[48] Z. Wang, J. Zhang, E. Bjornson, D. Niyato, and B. Ai, “Optimal bilinear¨ equalizer for cell-free massive MIMO systems over correlated Rician channels,” IEEE Trans. Signal Process., vol. 73, pp. 1501–1517, 2025.

[49] F. Quitin, A. T. Irish, and U. Madhow, “A scalable architecture for distributed receive beamforming: Analysis and experimental demonstration,” IEEE Trans. Wireless Commun., vol. 15, no. 3, pp. 2039–2053, Mar. 2016.

[50] J. Li, G. Sun, L. Duan, and Q. Wu, “Multi-objective optimization for UAV swarm-assisted IoT with virtual antenna arrays,” IEEE Trans. Mobile Comput., vol. 23, no. 5, pp. 4890–4907, May 2024.

[51] H. A. Ammar, R. Adve, S. Shahbazpanahi, G. Boudreau, and K. V. Srinivas, “User-centric cell-free massive MIMO networks: A survey of opportunities, challenges and solutions,” IEEE Commun. Surveys Tuts., vol. 24, no. 1, pp. 611–652, 1st Quart., 2022.

[52] Y. Sun, P. Babu, and D. P. Palomar, “Majorization-minimization algorithms in signal processing, communications, and machine learning,” IEEE Trans. Signal Process., vol. 65, no. 3, pp. 794–816, Feb. 2017.

[53] H. Wang et al., “Throughput maximization for movable antenna systems with movement delay consideration,” IEEE Trans. Wireless Commun., vol. 25, pp. 883–899, 2026.

![](images/de32c9e8ad953ba24908a2bfcebc7f190973e8bf12a0535ebc5ebbb9433915b2.jpg)

Haiquan Lu (Member, IEEE) received the B.S. degree in communication engineering from Yangzhou University, Yangzhou, China, in 2016, the M.S. degree in signal and information processing from Nanjing University of Posts and Telecommunications, Nanjing, China, in 2019, and the Ph.D. degree in information and communication engineering from Southeast University, Nanjing, in 2024. From January 2025 to September 2025, he was a Post-Doctoral Fellow with the State Key Laboratory of Internet of Things for Smart City, University of Macau, Macau, China. Since October 2025, he has been an Associate Professor with the School of Electronic and Optical Engineering, Nanjing University of Science and Technology. His research interests include extremely large-scale multiple-input multiple-output (XL-MIMO) communication and reconfigurable MIMO. He was a recipient of the Best Paper Award from IEEE International Conference on Communications (ICC) in 2021.

![](images/3cfdf98b4a9c957688b89511c278f9a8ab150d403d742c42e0a5515afa322e05.jpg)

Yong Zeng (Fellow, IEEE) received the Bachelor of Engineering (Hons.) and Ph.D. degrees from Nanyang Technological University, Singapore.

He is a Chief Young Professor with the National Mobile Communications Research Laboratory, Southeast University, China, and also with Purple Mountain Laboratories, Nanjing, China. From 2013 to 2018, he was a Research Fellow and a Senior Research Fellow with the Department of Electrical and Computer Engineering, National University of Singapore. From 2018 to 2019, he was a Lecturer with the School of Electrical and Information Engineering, The University of Sydney, Australia. He proposed the concept of channel knowledge map (CKM) and the transmission method of delay-Doppler alignment modulation (DDAM). He has published more than 200 papers, which have been cited by more than 37 000 times based on Google Scholar. He was elevated to IEEE Fellow “for contributions to unmanned aerial vehicle communications and wireless power transfer.” He was listed as Highly Cited Researcher by Clarivate Analytics for seven consecutive years (2019–2025). He was a recipient of the Australia Research Council (ARC) Discovery Early Career Researcher Award (DECRA), the IEEE Marconi Prize Paper Award in Wireless Communications in 2020 and 2024, the IEEE Communications Society Asia–Pacific Outstanding Young Researcher Award in 2018, the IEEE Communications Society Heinrich Hertz Prize Paper Award in 2020 and 2017, the IEEE ICC Best Paper Award in 2021, and the China Communications Best Paper Award in 2021. He was the Symposium Chair of IEEE Globecom 2021 Track on Aerial Communications, the Workshop Co-Chair of ICC 2018–2023 Workshop on UAV communications, and the Tutorial Speaker of Globecom 2018/2019 and ICC 2019 tutorials on UAV communications. He serves/served as an Associate Editor for IEEE TRANSACTIONS ON COMMUNICATIONS, IEEE TRANSACTIONS ON MOBILE COMPUTING, IEEE COMMUNICATIONS LETTERS, and IEEE OPEN JOURNAL OF VEHICULAR TECHNOLOGY; a Leading Guest Editor for IEEE WIRELESS COMMUNICATIONS on “Integrating UAVs Into 5G and Beyond” and China Communications on “Network-Connected UAV Communications.”

![](images/896d737a8d58ae9869e2c2ea350cf108521bac559947c3dce240e0a61c4ba379.jpg)

Shaodan Ma (Senior Member, IEEE) received the double bachelor’s degree in science and economics and the M.Eng. degree in electronic engineering from Nankai University, Tianjin, China, in 1999 and 2002, respectively, and the Ph.D. degree in electrical and electronic engineering from The University of Hong Kong, Hong Kong, in 2006.

From 2006 to 2011, she was a Post-Doctoral Fellow with The University of Hong Kong. Since August 2011, she has been with the University of Macau, where she is currently a Professor. Her

research interests include array signal processing, transceiver design, localization, integrated sensing and communication, mmWave/THz communications, massive MIMO, and machine learning for communications. She is an Executive Co-Chair of IEEE GLOBECOM 2026. She was the Symposium Co-Chair of various conferences, including IEEE VTC2024-Spring, IEEE ICC 2021, 2019, and 2016, IEEE GLOBECOM 2016, and IEEE/CIC ICCC 2019. She has served as an Editor for IEEE TRANSACTIONS ON COGNITIVE COMMUNICATIONS AND NETWORKING (since 2025), IEEE WIRELESS COMMUNICATIONS (since 2024), IEEE COMMUNICATIONS LETTERS (2023), Journal of Communications and Information Networks (since 2021), IEEE TRANSACTIONS ON WIRELESS COMMUNICATIONS (2018–2023), IEEE TRANSACTIONS ON COMMUNICATIONS (2018–2023), and IEEE WIRELESS COMMUNICATIONS LETTERS (2017–2022). She was an IEEE ComSoc Distinguished Lecturer from 2024 to 2025.

![](images/f9b66aee61f97e837fb3af05c6eea5af20bd1e5ee7914e059e8ac6cecfdb1531.jpg)  
Bin Li (Senior Member, IEEE) received the bachelor’s degree in automation and the master’s degree in control science and engineering from Harbin Institute of Technology, in 2005 and 2008, respectively, and the Ph.D. degree in mathematics and statistics from Curtin University in 2011. From 2012 to 2017, he visited the University of Western Australia and Curtin University. He is currently a Professor with the School of Aeronautics and Astronautics, Sichuan University, Chengdu, China. His research interests include signal processing, wireless  
communications, optimization, and optimal control.

![](images/ddf717f9a3a4544bb536f944bcbb4281a067c1e1e3197cb75ddb135f8becc5c9.jpg)

Shi Jin (Fellow, IEEE) received the B.S. degree in communications engineering from Guilin University of Electronic Technology, Guilin, China, in 1996, the M.S. degree from Nanjing University of Posts and Telecommunications, Nanjing, China, in 2003, and the Ph.D. degree in information and communications engineering from Southeast University, Nanjing, in 2007. From June 2007 to October 2009, he was a Research Fellow with University College London, Adastral Park Research Campus, London, U.K. He is currently with the faculty of the National

Mobile Communications Research Laboratory, Southeast University. His research interests include wireless communications, random matrix theory, and information theory. He and his co-authors have received the 2011 IEEE Communications Society Stephen O. Rice Prize Paper Award in the field of communication theory, the 2024 IEEE Communications Society Marconi Prize Paper Award, the IEEE Vehicular Technology Society 2023 Jack Neubauer Memorial Award, the 2022 Best Paper Award, and the 2010 Young Author Best Paper Award by the IEEE Signal Processing Society. He is serving as an Area Editor for IEEE TRANSACTIONS ON COMMUNICATIONS and IET Electronics Letters. He was an Associate Editor of IEEE TRANSACTIONS ON WIRELESS COMMUNICATIONS, IEEE COMMUNICATIONS LETTERS, and IET Communications.

![](images/e4798d15288991ab20c3c948c1ca883a9e66ba3fee6ac02965e5d00953a9bdeb.jpg)

Rui Zhang (Fellow, IEEE) received the B.Eng. (Hons.) and M.Eng. degrees from the National University of Singapore, Singapore, and the Ph.D. degree from Stanford University, Stanford, CA, USA, all in electrical engineering.

From 2007 to 2009, he was a Research Scientist with the Institute for Infocomm Research, A\*STAR, Singapore. In 2010, he joined the Department of Electrical and Computer Engineering, National University of Singapore, where he is currently a Provost’s Chair Professor. He is also an Adjunct

Professor with the School of Science and Engineering, The Chinese University of Hong Kong, Shenzhen, China. He has published over 600 papers, all in the field of wireless communications and networks. He has been listed as a Highly Cited Researcher by Thomson Reuters/Clarivate Analytics since 2015. His current research interests include intelligent surfaces, reconfigurable antennas, radio mapping, non-terrestrial communications, wireless power transfer, and AI and optimization methods.

Dr. Zhang is a fellow of the Academy of Engineering Singapore. He was a recipient of the Sixth IEEE Communications Society Asia–Pacific Region Best Young Researcher Award in 2011, the Young Researcher Award of National University of Singapore in 2015, the Wireless Communications Technical Committee Recognition Award in 2020, the IEEE Signal Processing and Computing for Communications (SPCC) Technical Recognition Award in 2021, the IEEE Communications Society Technical Committee on Cognitive Networks (TCCN) Recognition Award in 2023, and the IEEE James Evans Avant Garde Award in 2025. His works received 18 IEEE Best Journal Paper Awards, including the IEEE Marconi Prize Paper Award in Wireless Communications in 2015 and 2020; the IEEE Signal Processing Society Best Paper Award in 2016; the IEEE Communications Society Heinrich Hertz Prize Paper Award in 2017, 2020, and 2022; and the IEEE Communications Society Stephen O. Rice Prize in 2021. He served as the TPC co-chair or an organizing committee member for over 30 international conferences. He was an elected member of the IEEE Signal Processing Society SPCOM Technical Committee from 2012 to 2017 and SAM Technical Committee from 2013 to 2015. He is the Chair of the IEEE Communications Society Wireless Communications Technical Committee (WTC) Award Committee. He served as the Vice Chair for the IEEE Communications Society Asia–Pacific Board Technical Affairs Committee from 2014 to 2015 and a member of the Steering Committee of IEEE WIRELESS COMMUNICATIONS LETTERS from 2018 to 2021 and the IEEE Communications Society Wireless Communications Technical Committee (WTC) Award Committee from 2023 to 2025. He served as an Editor for several IEEE journals, including IEEE TRANSACTIONS ON WIRELESS COMMUNICATIONS from 2012 to 2016, IEEE JOURNAL ON SELECTED AREAS IN COMMUNICATIONS: Green Communications and Networking Series from 2015 to 2016, IEEE TRANSACTIONS ON SIGNAL PROCESSING from 2013 to 2017, IEEE TRANSACTIONS ON GREEN COMMUNICATIONS AND NETWORKING from 2016 to 2020, and IEEE TRANSACTIONS ON COMMUNICATIONS from 2017 to 2022. He serves as an Editorial Board Member for npj Wireless Technology. He was a Distinguished Lecturer of IEEE Signal Processing Society and IEEE Communications Society from 2019 to 2020.