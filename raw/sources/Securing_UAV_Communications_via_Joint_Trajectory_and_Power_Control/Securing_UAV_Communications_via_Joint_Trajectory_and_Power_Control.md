# Securing UAV Communications via Joint Trajectory and Power Control

Guangchi Zhang , Member, IEEE, Qingqing Wu , Member, IEEE, Miao Cui , and Rui Zhang , Fellow, IEEE

Abstract— Unmanned aerial vehicle (UAV) communication is anticipated to be widely applied in the forthcoming fifthgeneration wireless networks, due to its many advantages such as low cost, high mobility, and on-demand deployment. However, the broadcast and line-of-sight nature of air-to-ground wireless channels give rise to a new challenge on how to realize secure UAV communications with the destined nodes on the ground. This paper aims to tackle this challenge by applying the physical layer security technique. We consider both the downlink and uplink UAV communications with a ground node, namely, UAV-to-ground (U2G) and ground-to-UAV (G2U) communications, respectively, subject to a potential eavesdropper on the ground. In contrast to the existing literature on the wireless physical layer security only with the ground nodes at fixed or quasi-static locations, we exploit the high mobility of the UAV to proactively establish favorable and degraded channels for the legitimate and eavesdropping links, through its trajectory design. We formulate new problems to maximize the average secrecy rates of the U2G and G2U transmissions, by jointly optimizing the UAV’s trajectory, and the transmit power of the legitimate transmitter over a given flight period of the UAV. Although the formulated problems are non-convex, we propose iterative algorithms to solve them efficiently by applying the block coordinate descent and successive convex optimization methods. Specifically, both the transmit power and UAV trajectory are optimized, with the other being fixed in an alternating manner, until the algorithms converge. The simulation results show that the proposed algorithms can improve the secrecy rates for both U2G and G2U communications, as compared to other benchmark schemes without power control and/or trajectory optimization.

Index Terms— 5G and UAV communications, physical layer security, secrecy rate maximization, trajectory design, power control.

## I. INTRODUCTION

ITH many advantages such as high mobility, low cost, wide coverage, and on-demand deployment, unmanned aerial vehicles (UAVs) have been extensively used in both military and civilian applications, such as search and rescue, inspection and surveillance, cargo transportation, etc. Recently, UAVs have also found increasingly more substantial applications in wireless communication [2], and are expected to play a significant role in the forthcoming fifth-generation (5G) wireless networks [3], [4]. To seize this growing opportunity, internationally leading telecommunication companies such as Qualcomm, Ericsson, and China Mobile have already launched their research projects on integrating UAVs into the 5G networks [5], [6]. Generally speaking, there are two main paradigms of UAV applications in 5G. In the first one, termed as “UAV-assisted wireless communication”, UAVs are utilized as airbone communication platforms such as mobile base stations (BSs) and/or relays that can be flexibly deployed on demand to assist the communications in terrestrial networks such as 5G. For example, UAV-mounted BSs can be used to enable rapid wireless communication service recovery after ground infrastructure damages, or provide offloading service for terrestrial BSs in extremely crowded areas [7]–[15]. Another example is to use UAVs as mobile relays to provide reliable connectivity between distant users in remote areas (e.g., an uninhabited desert) that are not covered by any existing wireless networks [16], [17]. Moreover, in future internet of things (IoT) applications, UAVs can be dispatched to disseminate/collect data to/from widespread distributed wireless devices efficiently and with low cost [18]–[20]. By contrast, in the other paradigm, known as “cellular-enabled UAV communication”, UAVs are regarded as new “sky” users in the cellular networks that enable two-way communications of the UAVs with ground BSs. For example, the future 5G networks can provide reliable communications for UAVs even beyond the range of their operators’ visual line-of-sight (LoS) to achieve long-range UAV control in real time [21]. Besides, in UAVenabled surveillance applications, the captured pictures and/or videos by the UAVs in real time can be uploaded timely to the ground data centers via the 5G networks [22].

In the aforementioned UAV communication applications in 5G, due to the broadcast nature of wireless channels, their security and privacy are of utmost concern [23], [24]. One major advantage of UAV-ground communications is that UAVs usually have LoS channels for the communications with ground nodes, especially in outdoor environments. However, such LoS communication links are also more prone to the eavesdropping by illegitimate nodes on the ground, which gives rise to a new security challenge. Although security was conventionally viewed as a higher layer communication protocol stack design problem that can be tackled by using cryptographic methods, physical layer security has emerged as a promising alternative way of defense to realize secrecy in wireless communication.

A key design metric that has been widely adopted in physical layer security is the so-called secrecy rate [23]–[35], at which confidential message can be reliably transmitted without having the eavesdropper infer any information about the message. A non-zero secrecy rate can be achieved when the strength of the legitimate link is stronger than that of the eavesdropping link. In the existing literature on physical layer security, communication nodes are usually assumed to be at fixed or quasi-static locations. As a result, the average channel quality of the legitimate/eavesdropping link mainly depends on the path loss and shadowing from the transmitter to receiver, which are determined if the locations of the legitimate transmitter/receiver and the eavesdropper are given. Thus, in the case that the average channel gain of the legitimate receiver is smaller than that of the eavesdropper (e.g., due to longer distance from the legitimate transmitter), in order to achieve positive secrecy rates, the exploitation of the wireless channel small-scale fading in time, frequency, and/or space becomes essential, and various techniques such as power control in time and/or frequency as well as multi-antenna beamforming have been investigated. In [23], power control with rate adaptation over fading channels is proposed to maximize the average secrecy rate. This work is also extended to characterize the secrecy rate region of parallel-fading broadcast channels [24]. In [25], power control over frequency subcarriers is investigated for secrecy rate maximization in an orthogonal frequency-division multiple access (OFDMA) system. In [26], joint power control on information signal and artificial noise (AN) is proposed to maximize the secrecy rate of a simultaneous wireless information and power transfer (SWIPT) system. In multiple-input multiple-output (MIMO) systems, transmit beamforming can be jointly employed with AN transmission to effectively enhance the legitimate link capacity and at the same time degrade that of the eavesdropping link. For example, the legitimate transmitter can use beamforming to steer a null to the eavesdropper, or send AN in the direction of the eavesdropper to interferer with it [27]. In [28], beamforming is jointly designed with channel coding to achieve unconditional security in MIMO communications. If one or more relay helpers are available, they can also cooperatively send AN or jamming signals to interfere with the eavesdroppers to achieve better secrecy communication performance. In [29], optimal cooperative jamming via relays is studied to maximize the secrecy rate of a single-antenna pointto-point legitimate link. Besides, transmission scheduling by exploiting multiuser channel diversity is another effective approach to improve the secrecy communication performance in a system with multiple legitimate users/eavesdroppers. In [30], a transmission scheduling scheme is proposed to maximize the secrecy rate of a multiuser cognitive radio network. In [31], it is shown that for a terrestrial point-topoint wireless communication system, a moving receiver can achieve better secrecy performance than that of the system with a static receiver.

![](images/e774cee4736102bcddc6a61725233a6dadc3cc399f663a3868cc059887940c99.jpg)  
Fig. 1. A UAV wireless communication system consisting of a UAV above ground and a node on the ground. A potential eavesdropper on the ground intends to intercept the wireless communication between them.

However, there are still two major challenges that remain unsolved in the existing physical layer security literature. First, the practically achievable secrecy rate can be severely limited if the distance between the legitimate transmitter and its intended receiver is fixed and significantly larger than that between it and a potential eavesdropper, even if the various approaches mentioned above are applied. Second, the channel state information (CSI) of the eavesdropper is usually required at the legitimate transmitter for the implementation of effective power control and/or beamforming techniques. This is practically challenging since the eavesdropper is usually a passive device and thus it is difficult to estimate such CSI. In this paper, we study physical layer security in UAV-ground communications, which may potentially overcome the above two critical issues in conventional studies. First, in contrast to the existing literature with fixed or quasi-static nodes only, the high mobility of UAVs can be exploited to proactively establish stronger links with the legitimate ground nodes and/or degrade the channels of the eavesdroppers, by flying closer/farther to/from them, respectively, via proper trajectory design. This approach is particularly effective in the context of UAV-ground communications (as compared to conventional terrestrial communications), since the LoS links are usually much more dominant over other channel impairments such as shadowing and small-scale fading, due to the much larger height of the UAV than typical ground nodes such as mobile terminals or BSs. Furthermore, since the LoS channel gain is only determined by the link distance, the UAV can practically obtain the channel gain to any potential eavesdropper on the ground if its location is known, which thus resolves the eavesdropper-CSI issue in the existing literature. Note that the location of any ground node as a potential eavesdropper can be practically detected and tracked by the UAV via using an optical camera or synthetic aperture radar (SAR) equipped on the UAV [36], [37].

For an initial exposition, in this paper we consider a simplified three-node secrecy UAV-ground communication system as shown in Fig. 1, where a UAV at fixed altitude intends to communicate with a ground node, while a potential eavesdropper on the ground may intercept their communication. The secure communications of both UAV-to-ground (U2G) and ground-to-UAV (G2U) links are considered. In the U2G case, the UAV and the ground node are the legitimate transmitter and receiver, respectively, where both the legitimate and eavesdropping links are modeled as LoS channels. By contrast, in the G2U case, the ground node and the UAV are the legitimate transmitter and receiver, respectively. Since the legitimate transmitter and potential eavesdropper are both on the ground in this case, different from the U2G case, only the legitimate link is modeled as a LoS channel, while the eavesdropping link is practically modeled as a channel consisting of both distance-dependent path-loss and smallscale Rayleigh fading. Thus, the problem formulations for the secrecy rate maximization in these two cases are generally different, which will be detailed later in this paper. Nevertheless, the secrecy rates of both U2G and G2U transmissions can benefit from the joint design of UAV trajectory and transmit power control at the legitimate transmitter (i.e., UAV and ground node in the U2G and G2U cases, respectively), explained as follows. On one hand, the location of the UAV can be adjusted dynamically to establish stronger channels for the legitimate link than that for the eavesdropping link. On the other hand, due to practical constraints such as the UAV’s initial and final locations, the legitimate link may not be always stronger than the eavesdropping link during the whole flight period of the UAV. In this case, transmit power can be adapted to the channel variations arising from the UAV’s movement to further improve the secrecy rate. For example, in the U2G case, the UAV should transmit higher power when it flies closer to the ground node while being more far away from the eavesdropper, and transmit lower or zero power otherwise.

Motivated by this, we aim to design joint UAV trajectory and transmit power optimization algorithms to secure both U2G and G2U communications. Our goal is to maximize the average secrecy rate over a finite flight period of the UAV in each case, subject to the practical mobility constraints on the UAV’s maximum speed and its initial and final locations, as well as the average and peak transmit power constraints. For the U2G case, the formulated joint trajectory optimization and power control problem for average secrecy rate maximization is difficult to be solved directly due to its non-smooth objective function. To tackle this difficulty, we reformulate the problem into an equivalent problem with a smooth objective function without loss of optimality. Although the non-smoothness issue is resolved, the reformulated problem is still non-convex due to the coupling of the transmit power and UAV trajectory optimization variables. We thus propose an efficient iterative algorithm for solving this problem approximately based on the block coordinate descent method. Specifically, we divide the optimization variables into two blocks, one for transmit power control and the other for UAV trajectory optimization. Then the two blocks of variables are optimized alternately in an iterative manner, i.e., in each iteration one block is optimized with the other block fixed and vice versa. One corresponding sub-problem that optimizes the UAV trajectory under given transmit power is still difficult to solve due to its non-convexity. We thus apply the successive convex optimization method to solve the problem approximately. Finally, we show that our proposed joint optimization algorithm is guaranteed to converge. On the other hand, for the G2U case, similar to the U2G case, we also propose an efficient algorithm to solve the formulated problem by using the block coordinate descent and successive convex optimization methods, while some modification is made in the problem formulation to deal with the non-LoS channel of the eavesdropper link in this case. Simulation results show that the proposed joint trajectory and transmit power designs can improve the average secrecy rates in both U2G and G2U communications, as compared to other benchmark schemes without applying the trajectory optimization and/or transmit power control. Furthermore, it is observed that trajectory optimization and transmit power control are both essential for the U2G case, while for the G2U case, trajectory optimization is less effective as compared to power control.

It is worth noting that UAV systems, there have been prior works (e.g., [38]–[40]) that address the security and safety issues of UAVs from other perspectives. In [38], the security vulnerabilities in the global positioning system (GPS) spoofing attack and WiFi attack in UAV applications have been addressed, and effective solutions to these attacks have been suggested. In [39], a monocular camera and inertial measurement unit (IMU) sensor based GPS spoofing detection scheme and an image localization approach for UAV autonomous return have been proposed to support the security and safety of UAVs. In [40], a biometric system based on encryption has been proposed to secure the communication link between a UAV and a BS on the ground. Note that these prior works are fundamentally different from this paper which applies the physical layer security technique to deal with the eavesdropping attack in UAV-ground communication systems. It is also noted that there have been prior works (e.g., [11]–[14], [16], [41], and [42]) on trajectory optimization for various UAV communication systems, which consider different system setups and design objectives. In [11], three fundamental tradeoffs in UAV-enabled wireless networks have been identified, i.e., throughput-delay tradeoff, throughput-energy tradeoff, and delay-energy tradeoff. In [12], a UAV mobile BS serving multiple users is considered, where the UAV trajectory and multiuser scheduling are jointly designed to maximize the minimum throughput of the users. In particular, it is shown in [13] that significant communication throughput gains can be achieved by mobile UAVs over static UAVs/fixed terrestrial BSs by exploiting the new design degree of freedom of UAV trajectory optimization, especially for delay-tolerant applications. To study the fundamental limits of the UAVenabled wireless network, the capacity region of a two-user broadcast channel is characterized in [14] where it has been rigorously proved that a simple “fly-hover-fly” trajectory is capacity achieving. In [16], a UAV-enabled mobile relaying system is investigated, where the UAV trajectory and transmit power are jointly designed to maximize the throughput. In [41], the UAV flying heading is optimized to maximize the achievable sum rate from ground nodes to a UAV by assuming a constant flying speed. In [42], a new design paradigm that jointly considers both the communication throughput and the

UAV’s flying energy consumption is proposed to maximize the energy efficiency of a point-to-point U2G communication system. Different from these prior works, in this paper, we apply both trajectory optimization and transmit power control to maximize the secrecy rates of both U2G and G2U communications. The main contributions of this paper are highlighted as follows.

Compared to the existing physical layer security literature, this paper is the first to exploit the high mobility of UAVs to improve the secrecy rate via joint trajectory and power control optimization.

Both the U2G and G2U cases in UAV-ground communications are considered. The considered problems for both the two cases are difficult to be solved optimally due to their non-smooth and non-concave objective functions. To tackle this difficulty, we first reformulate the problems into equivalent problems with smooth objective functions, and then propose efficient algorithms to solve the reformulated problems approximately based on the block coordinate descent method and the successive convex optimization method. The obtained results show the fundamental secrecy rate limits of the U2G and G2U communications and demonstrate the importance and necessity of the joint UAV trajectory and transmit power optimization in maximizing the secrecy rate for the new settings. Moreover, the obtained results provide different design guidelines for the U2G case and the G2U case, respectively.

The remainder of this paper is organized as follows. Section II presents the system model and problem formulation. Sections III and IV present joint trajectory optimization and transmit power control algorithms for the U2G and G2U cases, respectively. Section V provides simulation results to validate the performance of the proposed algorithms as compared to three benchmark schemes. Finally, Section VI concludes the paper.

## II. SYSTEM MODEL AND PROBLEM FORMULATION

## A. System Model

As shown in Fig. 1, we consider a UAV-enabled wireless communication system where a UAV above ground and a node on the ground communicate with each other, while a potential eavesdropper on the ground aims to intercept the communications between them. Without loss of generality, we consider a three-dimensional (3D) Cartesian coordinate system with the ground node and the eavesdropper located at $( x _ { \mathrm { G } } , y _ { \mathrm { G } } , 0 )$ and $( x _ { \mathrm { E } } , y _ { \mathrm { E } } , 0 )$ in meters (m), respectively. Their locations are assumed to be fixed and known to the UAV, where the location of the eavesdropper can be detected by using an optical camera or SAR equipped on the UAV. On the other hand, the obtained secrecy rate when the location of the eavesdropper is known serves as an upper bound for that when the location of the eavesdropper is not known.

We consider a given finite flight period of the UAV, with the duration denoted by $T$ in seconds (s). It is assumed that the UAV flies at a fixed altitude of H in m above ground, which can be considered as the minimum altitude required for safety considerations such as terrain or building avoidance. The coordinate of the UAV over time is denoted as $( x ( t ) , y ( t ) , H )$ in m, $0 \leq t \leq T$ . For convenience, we divide the period $T$ into $N$ time slots with equal length, i.e., $T = N d _ { t }$ , with $d _ { t }$ in s denoting the length of a time slot, which is chosen sufficiently small such that the $\mathrm { U A V } _ { \mathrm { \Delta } }$ location can be regarded as unchanged within each time slot from the viewpoint of the ground node. As a result, the UAV’s coordinate in slot n can be denoted as $( x [ n ] , y [ n ] , H )$ , and the UAV’s horizontal trajectory $( x ( t ) , y ( t ) )$ over the flight period $T$ can be approximated by the sequence $\{ x [ n ] , y [ n ] \} _ { n = 1 } ^ { N }$ . Denote the maximum speed of the UAV as $v _ { \mathrm { m a x } }$ in m/s. Thus, the maximum flying distance of the UAV in each slot is $D = v _ { \operatorname* { m a x } } d _ { t }$ . The initial and final locations of the UAV are assumed to be given, which are denoted by $( x _ { 0 } , y _ { 0 } , H )$ and $( x _ { F } , y _ { F } , H )$ in m, respectively. For the UAV trajectory to be feasible, we assume that the distance between the initial and final location satisfies that $\sqrt { ( x _ { F } - x _ { 0 } ) ^ { 2 } + ( y _ { F } - y _ { 0 } ) ^ { 2 } } \leq v _ { \mathrm { m a x } } T$ . As a result, the mobility constraints of the UAV can be expressed as

$$
( x [ 1 ] - x _ { 0 } ) ^ { 2 } + ( y [ 1 ] - y _ { 0 } ) ^ { 2 } \leq D ^ { 2 } ,
$$

$$
( x [ n + 1 ] - x [ n ] ) ^ { 2 } + ( y [ n + 1 ] - y [ n ] ) ^ { 2 } \leq D ^ { 2 } ,\tag{1a}
$$

$$
n = 1 , \ldots , N - 1 ,
$$

$$
( x _ { F } - x [ N ] ) ^ { 2 } + ( y _ { F } - y [ N ] ) ^ { 2 } \leq D ^ { 2 } .\tag{1b}
$$

(1c)

We consider both the U2G and G2U communications in the system of interest, which are specified in detail in the following, respectively.

1) U2G Transmission: In the U2G case, the UAV and the ground node play the roles of legitimate transmitter and receiver, respectively. The legitimate link from the UAV to the ground node and the eavesdropping link from the UAV to the eavesdropper are both assumed to be LoS channels, as the recent measurement results in [43] have shown that the LoS model offers a good approximation for practical UAV-ground communications. Thus, the LoS channel power gain from the UAV to the ground node in time slot n follows the free-space path loss model, given by

$$
g _ { \mathrm { U G } } [ n ] = \beta _ { 0 } d _ { \mathrm { U G } } ^ { - 2 } [ n ] = \frac { \beta _ { 0 } } { ( x [ n ] - x _ { \mathrm { G } } ) ^ { 2 } + ( y [ n ] - y _ { \mathrm { G } } ) ^ { 2 } + H ^ { 2 } } ,\tag{2}
$$

where $\beta _ { 0 }$ denotes the channel power gain at the reference distance $d _ { 0 } = 1 \mathrm { m }$ , which depends on the carrier frequency and the antenna gains of the transmitter and receiver, and $d _ { \mathrm { U G } } [ n ] =$ $\sqrt { ( x [ n ] - x _ { \mathrm { G } } ) ^ { 2 } + ( y [ n ] - y _ { \mathrm { G } } ) ^ { 2 } + H ^ { 2 } }$ <sup>[ ] =</sup>is the distance from the <sup>( [ ] ) + ( [ ] ) +</sup>UAV to the ground node in time slot $n .$ Similarly, the LoS channel power gain from the UAV to the eavesdropper in time slot n is given by

$$
g _ { \mathrm { U E } } [ n ] = \frac { \beta _ { 0 } } { ( x [ n ] - x _ { \mathrm { E } } ) ^ { 2 } + ( y [ n ] - y _ { \mathrm { E } } ) ^ { 2 } + H ^ { 2 } } .\tag{3}
$$

We denote $p [ n ]$ as the transmit power of the UAV in time slot $n .$ <sup>[ ]</sup> In practice, $p [ n ] \mathrm { { s } }$ are usually subject to both average and peak limits over time, denoted by $\bar { P }$ and $P _ { \mathrm { p e a k } }$ , respectively. Thus, the transmit power constraints are

expressed as

$$
\frac { 1 } { N } \sum _ { n = 1 } ^ { N } p [ n ] \leq \bar { P } ,\tag{4a}
$$

$$
0 \leq p [ n ] \leq P _ { \mathrm { p e a k } } , \forall n .\tag{4b}
$$

To make the constraint in (4a) non-trivial, we assume $\bar { P } <$ $P _ { \mathrm { p e a k } }$ in this paper. In the absence of the eavesdropper, the achievable rate from the UAV to the ground node in bits/second/Hertz (bps/Hz) in time slot n can be expressed as

$$
\begin{array} { l } { { \displaystyle R _ { \mathrm { U G } } [ n ] = \log _ { 2 } \left( 1 + \frac { p [ n ] g _ { \mathrm { U G } } [ n ] } { \sigma ^ { 2 } } \right) } } \\ { { \displaystyle \qquad = \log _ { 2 } \left( 1 + \frac { \gamma _ { 0 } p [ n ] } { ( x [ n ] - x _ { \mathrm { G } } ) ^ { 2 } + ( y [ n ] - y _ { \mathrm { G } } ) ^ { 2 } + H ^ { 2 } } \right) } , } \end{array}\tag{5}
$$

where $\sigma ^ { 2 }$ is the additive white Gaussian noise (AWGN) power at the receiver and $\gamma _ { 0 } = \beta _ { 0 } / \sigma ^ { 2 }$ is the reference signal-to-noise ratio (SNR). Similarly, the achievable rate from the UAV to the eavesdropper in bps/Hz in time slot n is given by

$$
R _ { \mathrm { U E } } [ n ] = \log _ { 2 } { \left( 1 + \frac { \gamma _ { 0 } p [ n ] } { ( x [ n ] - x _ { \mathrm { E } } ) ^ { 2 } + ( y [ n ] - y _ { \mathrm { E } } ) ^ { 2 } + H ^ { 2 } } \right) } .\tag{6}
$$

With (5) and (6), the average secrecy rate achievable for the U2G link in bps/Hz over the total N time slots is given by [23]

$$
\begin{array} { l } { { \displaystyle R _ { \mathrm { s e c } } ^ { ( \mathrm { U Z G } ) } } } \\ { { \displaystyle ~ = \frac { 1 } { N } \sum _ { n = 1 } ^ { N } \left[ \log _ { 2 } \left( 1 + \frac { \gamma _ { 0 } p [ n ] } { ( x [ n ] - x _ { \mathrm { G } } ) ^ { 2 } + ( y [ n ] - y _ { \mathrm { G } } ) ^ { 2 } + H ^ { 2 } } \right) \right. } } \\ { { \displaystyle ~ \left. - \log _ { 2 } \left( 1 + \frac { \gamma _ { 0 } p [ n ] } { ( x [ n ] - x _ { \mathrm { E } } ) ^ { 2 } + ( y [ n ] - y _ { \mathrm { E } } ) ^ { 2 } + H ^ { 2 } } \right) \right] ^ { + } , } } \end{array}\tag{7}
$$

where $[ x ] ^ { + } \triangleq \operatorname* { m a x } ( x , 0 )$

2) G2U Transmission: In the G2U case, the ground node and the UAV play the roles of legitimate transmitter and receiver, respectively. The legitimate channel from the ground node to the UAV is assumed to be LoS, similar as in the U2G case, whose channel power gain in time slot n is given by

$$
g _ { \mathrm { G U } } [ n ] = \frac { \beta _ { 0 } } { ( x [ n ] - x _ { \mathrm { G } } ) ^ { 2 } + ( y [ n ] - y _ { \mathrm { G } } ) ^ { 2 } + H ^ { 2 } } .\tag{8}
$$

Since both the ground node and the eavesdropper are on the ground, the eavesdropping channel between them is assumed to constitute both distance-dependent path loss with passloss exponent $\kappa \geq 2$ and small-scale Rayleigh fading. Thus, the channel power gain from the ground node to the eavesdropper at any time is given by

$$
g _ { \mathrm { G E } } = \frac { \beta _ { 0 } } { d _ { \mathrm { G E } } ^ { \kappa } } \zeta ,\tag{9}
$$

where $d _ { \mathrm { G E } } = \sqrt { ( x _ { \mathrm { G } } - x _ { \mathrm { E } } ) ^ { 2 } + ( y _ { \mathrm { G } } - y _ { \mathrm { E } } ) ^ { 2 } }$ denotes the distance between the ground node and the eavesdropper, and ζ is an exponentially distributed random variable with unit mean accounting for the Rayleigh fading.

We denote $q [ n ]$ as the transmit power of the ground node in time slot n. Similar to the U2G case, $q [ n ] \mathrm { { s } }$ are constrained by average power limit $\bar { Q }$ and peak power limit $Q _ { \mathrm { p e a k } }$ , i.e.,

$$
\frac { 1 } { N } \sum _ { n = 1 } ^ { N } q [ n ] \leq \bar { Q } ,\tag{10a}
$$

$$
0 \leq q [ n ] \leq Q _ { \mathrm { p e a k } } , \forall n ,\tag{10b}
$$

where $\bar { Q } < Q _ { \mathrm { p e a k } }$ is assumed. Similar to (5), the achievable rate from the ground node to the UAV in bps/Hz in time slot n can be expressed as

$$
R _ { \mathrm { G U } } [ n ] = \log _ { 2 } \bigg ( 1 + \frac { \gamma _ { 0 } q [ n ] } { ( x [ n ] - x _ { \mathrm { G } } ) ^ { 2 } + ( y [ n ] - y _ { \mathrm { G } } ) ^ { 2 } + H ^ { 2 } } \bigg ) .\tag{11}
$$

The achievable rate from the ground node to the eavesdropper in bps/Hz in time slot n is expressed as

$$
R _ { \mathrm { G E } } [ n ] = \mathbb { E } _ { \zeta } \left[ \log _ { 2 } \left( 1 + \frac { \gamma _ { 0 } \ q [ n ] } { d _ { \mathrm { G E } } ^ { \kappa } } \zeta \right) \right]\tag{12a}
$$

$$
\leq \log _ { 2 } \left( 1 + \frac { \gamma _ { 0 } \ q [ n ] } { d _ { \mathrm { G E } } ^ { \kappa } } \mathbb { E } _ { \zeta } \left[ \zeta \right] \right)\tag{12b}
$$

$$
= \log _ { 2 } { \left( 1 + \frac { \gamma _ { 0 } q [ n ] } { d _ { \mathrm { G E } } ^ { \kappa } } \right) } ,\tag{12c}
$$

where $\mathbb { E } _ { \zeta } [ \cdot ]$ in (12a) denotes the mathematical expectation with <sup>[ ]</sup>respect to random variable ζ, and the inequality in (12b) is due to Jensen’s inequality and the fact that $\log _ { 2 } ( 1 + \gamma _ { 0 } q [ n ] \zeta / d _ { \mathrm { G E } } ^ { \kappa } )$ is concave with respect to ζ. (12c) shows an upper bound of $R _ { \mathrm { G E } } [ n ]$ . We consider the worst-case secrecy rate performance by assuming that the eavesdropper is able to achieve this upper bound. With (11) and (12c), the following average secrecy rate of the G2U link in bps/Hz over the total N time slots is thus achievable,

$$
\begin{array}{c} \begin{array} { c l r } { { \displaystyle R _ { \mathrm { s e c } } ^ { ( \mathrm { G Z U } ) } } } \\ { { \displaystyle } } \\ { { \displaystyle } } \end{array} = \frac { 1 } { N } \sum _ { n = 1 } ^ { N } \left[ \log _ { 2 } \left( 1 + \frac { \gamma _ { 0 } q [ n ] } { ( x [ n ] - x _ { \mathrm { G } } ) ^ { 2 } + ( y [ n ] - y _ { \mathrm { G } } ) ^ { 2 } + H ^ { 2 } } \right) \right.  \\ { { \displaystyle } } & { { \displaystyle } } & { { \displaystyle \left. - \log _ { 2 } \left( 1 + \frac { \gamma _ { 0 } q [ n ] } { d _ { \mathrm { G } } ^ { k } } \right) \right] ^ { + } . } } \end{array}
$$

## B. Problem Formulation

For the U2G case, our goal is to maximize the average secrecy rate $R _ { \mathrm { { s e c } } } ^ { \mathrm { ( U 2 G ) } }$ in (7) by jointly optimizing the UAV’s transmit power $\mathbf { p } \triangleq [ p [ 1 ] , \dots , \hat { p [ N ] } ] ^ { \dagger }$ and the UAV’s trajectory in terms of its horizontal coordinates $\mathbf { x } \triangleq [ x [ 1 ] , \ldots , { \overset { } { x } } [ N ] ] ^ { \dagger }$ and $\mathbf { y } \triangleq [ y [ 1 ] , \dots , y [ N ] ] ^ { \dagger }$ over all the N time slots, where the superscript † denotes the transpose operation. The optimization variables are subject to the UAV’s mobility constraints in (1) and the average and peak transmit power constraints in (4). We formulate the secrecy rate maximization problem as follows (by dropping the constant term $1 / N$ in $( 7 ) ) ^ { 1 }$

$$
\begin{array} { l } { { \displaystyle \operatorname* { m a x } _ { { \bf x } , { \bf y } , { \bf p } } ~ \sum _ { n = 1 } ^ { N } \left[ \log _ { 2 } \left( 1 + \frac { \gamma _ { 0 } p [ n ] } { ( x [ n ] - x _ { \mathrm { G } } ) ^ { 2 } + ( y [ n ] - y _ { \mathrm { G } } ) ^ { 2 } + H ^ { 2 } } \right) \right. } } \\ { { \displaystyle \qquad - \left. \log _ { 2 } \left( 1 + \frac { \gamma _ { 0 } p [ n ] } { ( x [ n ] - x _ { \mathrm { E } } ) ^ { 2 } + ( y [ n ] - y _ { \mathrm { E } } ) ^ { 2 } + H ^ { 2 } } \right) \right] ^ { + } } } \\ { { \mathrm { s . t . ~ } ( 1 ) , ~ ( 4 ) . } } \end{array}\tag{P1}
$$

Similarly, for the G2U case, we maximize $R _ { \mathrm { { s e c } } } ^ { \mathrm { { ( G 2 U ) } } }$ in (13) by jointly optimizing the ground node’s transmit power $\mathbf { q } \triangleq$ $[ q [ 1 ] , \ldots , q [ N ] ] ^ { \dagger }$ and the UAV’s horizontal trajectory x and $\mathbf { y }$ The problem is thus formulated as

$$
\begin{array} { l } { { \displaystyle \operatorname* { m a x } _ { { \bf x } , { \bf y } , { \bf q } } ~ \sum _ { n = 1 } ^ { N } \left[ \log _ { 2 } \left( 1 + \frac { \gamma _ { 0 } q [ n ] } { ( x [ n ] - x _ { \mathrm { G } } ) ^ { 2 } + ( y [ n ] - y _ { \mathrm { G } } ) ^ { 2 } + H ^ { 2 } } \right) \right. } } \\ { { \displaystyle \qquad - \left. \log _ { 2 } \left( 1 + \frac { \gamma _ { 0 } q [ n ] } { d _ { \mathrm { G E } } ^ { \kappa } } \right) \right] ^ { + } } } \\ { { \displaystyle \mathrm { s . t . } ~ ( 1 ) , ~ ( 1 0 ) . } } \end{array}\tag{P2}
$$

Note that different from problem (P1), only the first logarithmic function in the objective of (P2), i.e., $\log _ { 2 } { \left( 1 + \right. }$ $\frac { \gamma _ { 0 } ~ q [ n ] } { ( \underline { { x } } [ n ] - x \underline { { G } } ) ^ { 2 } + ( \underline { { y } } [ n ] - y _ { \mathrm { G } } ) ^ { 2 } + H ^ { 2 } } \Big )$ , contains the UAV trajectory variables. This is because the achievable rate from the ground node to the eavesdropper does not depend on the trajectory of the UAV.

Problems (P1) and (P2) are both difficult to be solved optimally due to the following two reasons. First, the operator $[ \cdot ] ^ { + }$ makes the objective functions of (P1) and (P2) nonsmooth at zero value. Second, even without $[ \cdot ] ^ { + }$ , their objective functions are non-concave with respect to either x, y, or p. In Sections III and IV, we propose efficient algorithms for solving problems (P1) and (P2) approximately, respectively.

## III. PROPOSED ALGORITHM FOR PROBLEM (P1)

First, we consider problem (P1) for the U2G case. To handle the non-smoothness of the objective function of (P1), the following lemma is used.

Lemma 1: Problem (P1) has the same optimal value as that of the following problem,

$$
\begin{array} { l } { \displaystyle \operatorname* { m a x } _ { { \bf x } , { \bf y } , { \bf p } } \ \sum _ { n = 1 } ^ { N } \left[ \log _ { 2 } \left( 1 + \frac { \gamma _ { 0 } p [ n ] } { ( x [ n ] - x _ { \mathrm { G } } ) ^ { 2 } + ( y [ n ] - y _ { \mathrm { G } } ) ^ { 2 } + H ^ { 2 } } \right) \right. } \\ { \displaystyle \left. - \ \log _ { 2 } \left( 1 + \frac { \gamma _ { 0 } p [ n ] } { ( x [ n ] - x _ { \mathrm { E } } ) ^ { 2 } + ( y [ n ] - y _ { \mathrm { E } } ) ^ { 2 } + H ^ { 2 } } \right) \right] } \\ { \mathrm { s . t . } \ ( 1 ) , \ ( 4 ) . } \end{array}\tag{P3}
$$

Proof: Denote $L _ { 1 }$ and $L _ { 3 }$ as the optimal values of (P1) and (P3), respectively. First, we have $L _ { 1 } \ge L _ { 3 }$ , since the objective function of (P1) is no smaller than that of (P3), and (P1) and (P3) have the same constraints.

Next, we show $L _ { 3 } \geq L _ { 1 }$ also holds. Denote $\left( \mathbf { x } ^ { * } , \mathbf { y } ^ { * } , \mathbf { p } ^ { * } \right)$ as the optimal solution to (P1), where $\mathbf { x } ^ { * } = [ x ^ { * } [ 1 ] , \dots , x ^ { * } [ N ] ] ^ { \dagger }$ $\begin{array} { r } { \begin{array} { l } { \mathbf { y } ^ { * } } \end{array} = \begin{array} { l } { [ y ^ { * } [ 1 ] , \dotsc , y ^ { * } [ N ] ] ^ { \dagger } } \end{array} } \end{array}$ , and $\begin{array} { r } { \mathbf { p } ^ { * } ~ = ~ [ p ^ { * } [ 1 ] , \dots , p ^ { * } [ N ] ] ^ { \dagger } } \end{array}$ <sup>=</sup>Define

$$
\begin{array} { l } { f ( x [ n ] , y [ n ] , p [ n ] ) \smallskip \qquad } \\ { \triangleq \log _ { 2 } \bigg ( 1 + \frac { \gamma _ { 0 } p [ n ] } { ( x [ n ] - x _ { \mathrm { G } } ) ^ { 2 } + ( y [ n ] - y _ { \mathrm { G } } ) ^ { 2 } + H ^ { 2 } } \bigg ) } \\ { \quad \qquad - \log _ { 2 } \bigg ( 1 + \frac { \gamma _ { 0 } p [ n ] } { ( x [ n ] - x _ { \mathrm { E } } ) ^ { 2 } + ( y [ n ] - y _ { \mathrm { E } } ) ^ { 2 } + H ^ { 2 } } \bigg ) . } \end{array}
$$

We construct a feasible solution to (P3), termed $( \tilde { \mathbf { x } } , \tilde { \mathbf { y } } , \tilde { \mathbf { p } } )$ , such that $\tilde { \mathbf { x } } = \mathbf { x } ^ { * } , \tilde { \mathbf { y } } = \mathbf { y } ^ { * }$ , and the elements of $\tilde { \mathbf { p } }$ are obtained as

$$
\tilde { p } [ n ] = \left\{ p ^ { * } [ n ] \begin{array} { l l } { f ( x ^ { * } [ n ] , y ^ { * } [ n ] , p ^ { * } [ n ] ) \ge 0 , } \\ { 0 } & { f ( x ^ { * } [ n ] , y ^ { * } [ n ] , p ^ { * } [ n ] ) < 0 . } \end{array} \right.
$$

Denote $\tilde { L }$ as the objective value of (P3) attained at $( \tilde { \mathbf { x } } , \tilde { \mathbf { y } } , \tilde { \mathbf { p } } )$ The newly constructed solution $( \tilde { \mathbf { x } } , \tilde { \mathbf { y } } , \tilde { \mathbf { p } } )$ ensures that $\ddot { L } = L _ { 1 }$ Since $( \tilde { \mathbf { x } } , \tilde { \mathbf { y } } , \tilde { \mathbf { p } } )$ <sup>(˜ ˜ ˜) =</sup>is a feasible solution to (P3), it follows that $L _ { 3 } \ \ge \ \tilde { L }$ , and thus $L _ { 3 } ~ \ge ~ L _ { 1 }$ . Therefore, $L _ { 1 } ~ = ~ L _ { 3 }$ , which completes the proof. 

Based on Lemma 1, we only need to focus on solving problem (P3). Although problem (P3) resolves the nonsmoothness issue, it is still non-convex and difficult to solve. However, we observe that the constraint (1) contains only the variables $\displaystyle ( \mathbf { x } , \mathbf { y } )$ for UAV trajectory optimization and the constraint (4) contains only the variables p for transmit power control. As such, the optimization variables of (P3) can be partitioned into two blocks, i.e., p and $\displaystyle ( \mathbf { x } , \mathbf { y } )$ , respectively, which facilitates the development of an iterative algorithm for solving problem (P3) by applying the block coordinate descent method. Specifically, we solve problem (P3) by solving the following two sub-problems iteratively: one (denoted by subproblem 1) optimizes the transmit power p under given UAV trajectory $\displaystyle ( \mathbf { x } , \mathbf { y } )$ , while the other (denoted by sub-problem 2) optimizes the UAV trajectory $\displaystyle ( \mathbf { x } , \mathbf { y } )$ under given transmit power p, as detailed in the next two subsections, respectively. Then, we present the overall algorithm and show that it is guaranteed to converge.

A. Sub-Problem 1: Optimizing Transmit Power Given UAV Trajectory

For given UAV trajectory $\displaystyle ( \mathbf { x } , \mathbf { y } )$ , sub-problem 1 can be expressed as

$$
\begin{array} { r l } & { \underset { \mathbf { p } } { \operatorname* { m a x } } ~ \displaystyle \sum _ { n = 1 } ^ { N } \left[ \log _ { 2 } \left( 1 + a _ { n } p [ n ] \right) - \log _ { 2 } \left( 1 + b _ { n } p [ n ] \right) \right] } \\ & { \mathrm { s . t . } ~ ( 4 ) , } \end{array}\tag{17}
$$

where

$$
a _ { n } = \frac { \gamma _ { 0 } } { ( x [ n ] - x _ { \mathrm { G } } ) ^ { 2 } + ( y [ n ] - y _ { \mathrm { G } } ) ^ { 2 } + H ^ { 2 } } ,\tag{18}
$$

$$
b _ { n } = \frac { \imath \upsilon } { ( x [ n ] - x _ { \mathrm { E } } ) ^ { 2 } + ( y [ n ] - y _ { \mathrm { E } } ) ^ { 2 } + H ^ { 2 } } .\tag{19}
$$

Although problem (18) is non-convex, it has been shown in [23] and [33] that the optimal solution can be obtained as

$$
p ^ { * } [ n ] = \left\{ { \begin{array} { l l } { \operatorname* { m i n } \left( [ { \hat { p } } [ n ] ] ^ { + } , P _ { \mathrm { p e a k } } \right) } & { a _ { n } > b _ { n } , } \\ { 0 } & { a _ { n } \le b _ { n } , } \end{array} } \right.\tag{20}
$$

where

$$
\hat { p } [ n ] = \sqrt { \left( \frac { 1 } { 2 b _ { n } } - \frac { 1 } { 2 a _ { n } } \right) ^ { 2 } + \frac { 1 } { \lambda \ln 2 } \left( \frac { 1 } { b _ { n } } - \frac { 1 } { a _ { n } } \right) } - \frac { 1 } { 2 b _ { n } } - \frac { 1 } { 2 a _ { n } } .\tag{21}
$$

In (21), $\lambda \geq 0$ is a constant that ensures the average power constraint $\begin{array} { r } { \frac { 1 } { N } \sum _ { n = 1 } ^ { N } p [ n ] \leq \bar { P } } \end{array}$ to be satisfied when the optimal solution of problem (18) is attained, which can be found efficiently via a one-dimensional bisection search [33], [44].

## B. Sub-Problem 2: Optimizing UAV Trajectory Given Transmit Power

For given transmit power p, by letting $P _ { n } = \gamma _ { 0 } p [ n ]$ , we can express sub-problem 2 as

$$
\begin{array} { l } { { \displaystyle \operatorname* { m a x } _ { \mathbf { x } , \mathbf { y } } \sum _ { n = 1 } ^ { N } \left[ \log _ { 2 } \left( 1 + \frac { P _ { n } } { ( x [ n ] - x _ { \mathrm { G } } ) ^ { 2 } + ( y [ n ] - y _ { \mathrm { G } } ) ^ { 2 } + H ^ { 2 } } \right) \right. } } \\ { { \displaystyle \qquad - \left. \log _ { 2 } \left( 1 + \frac { P _ { n } } { ( x [ n ] - x _ { \mathrm { E } } ) ^ { 2 } + ( y [ n ] - y _ { \mathrm { E } } ) ^ { 2 } + H ^ { 2 } } \right) \right] } } \\ { { \mathrm { s . t . ~ } ( 1 ) . } } \end{array}
$$

Note that the objective function of problem (22) is nonconcave with respect to x and y, so it is a non-convex optimization problem and cannot be solved optimally in general. By introducing slack variables $\mathbf { t } \triangleq [ t [ 1 ] , \dots , t [ N ] ] ^ { \dagger }$ and $\mathbf { u } \triangleq \mathbb { \tilde { \ } } { [ u [ 1 ] , \dots , u [ \overset { \cdot } { N } ] ] } ^ { \dagger }$ , we first consider the following problem,

$$
\operatorname* { m a x } _ { \mathbf { x } , \mathbf { y } , \mathbf { t } , \mathbf { u } } \sum _ { n = 1 } ^ { N } \left[ \log _ { 2 } \left( 1 + { \frac { P _ { n } } { u [ n ] } } \right) - \log _ { 2 } \left( 1 + { \frac { P _ { n } } { t [ n ] } } \right) \right]\tag{23a}
$$

$$
\mathrm { s . t . } ~ t [ n ] - x ^ { 2 } [ n ] + 2 x _ { \mathrm { E } } x [ n ] - x _ { \mathrm { E } } ^ { 2 } - y ^ { 2 } [ n ] + 2 y _ { \mathrm { E } } y [ n ]
$$

$$
- y _ { \mathrm { E } } ^ { 2 } - H ^ { 2 } \leq 0 , \forall n ,\tag{23b}
$$

$$
x ^ { 2 } [ n ] - 2 x _ { \mathrm { G } } x [ n ] + x _ { \mathrm { G } } ^ { 2 } + y ^ { 2 } [ n ] - 2 y _ { \mathrm { G } } y [ n ] + y _ { \mathrm { G } } ^ { 2 }
$$

$$
+ H ^ { 2 } - u [ n ] \leq 0 , \forall n ,\tag{23c}
$$

$$
t [ n ] \geq H ^ { 2 } , \quad \forall n ,\tag{23d}
$$

(1).

At the optimal solution of problem (23), constraints (23b) and (23c) should hold with equalities, since otherwise $t [ n ]$ $( u [ n ] )$ can be increased (decreased) to improve the objective value. Therefore, problems (22) and (23) have the same optimal value and optimal solution of $\displaystyle ( \mathbf { x } , \mathbf { y } )$ . Next, we focus on solving problem (23).

The term $\begin{array} { r } { \log _ { 2 } { \left( 1 + \frac { P _ { n } } { u [ n ] } \right) } } \end{array}$ in (23a) is convex with respect to $u [ n ]$ , and the terms $- x ^ { 2 } [ n ]$ and $- y ^ { 2 } [ n ]$ in (23b) are concave with respect to $x [ n ]$ and $y [ n ]$ , respectively. However, a maximization problem with a non-concave objective function and/or a non-convex feasible region is in general non-convex and thus difficult to be solved optimally. Based on the facts that the first-order Taylor expansion of a convex function is its global under-estimator and that of a concave function is its global over-estimator [44], we propose an iterative algorithm to solve problem (23) approximately by applying the successive convex optimization method. The algorithm obtains an approximate solution to problem (23) by maximizing a concave lower bound of its objective function within a convex feasible region, which is detailed as follows. First, the algorithm assumes a given initial point $\left( \mathbf { x } _ { \mathrm { f e a } } , \mathbf { y } _ { \mathrm { f e a } } , \mathbf { u } _ { \mathrm { f e a } } \right)$ which is feasible to (23), where $\mathbf { x } _ { \mathrm { f e a } } \triangleq [ x _ { \mathrm { f e a } } [ 1 ] , \hdots , x _ { \mathrm { f e a } } [ N ] ] ^ { \dagger } , \mathbf { y } _ { \mathrm { f e a } } \triangleq$ $[ y _ { \mathrm { f e a } } [ 1 ] , \dots , y _ { \mathrm { f e a } } [ N ] ] ^ { \dagger }$ , and $\mathbf { u } _ { \mathrm { f e a } } \triangleq [ u _ { \mathrm { f e a } } [ 1 ] , \dots , u _ { \mathrm { f e a } } [ N ] ] ^ { \dagger }$ . Then, by using the first-order Taylor expansions of $\begin{array} { r } { \left( 1 + \frac { P _ { n } } { u [ n ] } \right) } \end{array}$ $- x ^ { 2 } [ n ]$ , and $- y ^ { 2 } [ n ]$ at the points $u _ { \mathrm { f e a } } [ n ] , x _ { \mathrm { f e a } } [ n ]$ , and $y _ { \mathrm { f e a } } [ \hat { n } ]$ respectively, i.e.,

$$
\begin{array} { l } { { \displaystyle \log _ { 2 } \left( 1 + \frac { P _ { n } } { u [ n ] } \right) \geq \log _ { 2 } \left( 1 + \frac { P _ { n } } { u _ { \mathrm { f e a } } [ n ] } \right) } } \\ { { \displaystyle \qquad - \frac { P _ { n } ( u [ n ] - u _ { \mathrm { f e a } } [ n ] ) } { \ln 2 ( u _ { \mathrm { f e a } } ^ { 2 } [ n ] + P _ { n } u _ { \mathrm { f e a } } [ n ] ) } , } } \end{array}\tag{24}
$$

$$
- x ^ { 2 } [ n ] \leq x _ { \mathrm { f e a } } ^ { 2 } [ n ] - 2 x _ { \mathrm { f e a } } [ n ] x [ n ] ,\tag{25}
$$

$$
- y ^ { 2 } [ n ] \leq y _ { \mathrm { f e a } } ^ { 2 } [ n ] - 2 y _ { \mathrm { f e a } } [ n ] y [ n ] ,\tag{26}
$$

problem (23) is approximated as

$$
\operatorname* { m a x } _ { \mathbf { x } , \mathbf { y } , \mathbf { t } , \mathbf { u } } \sum _ { n = 1 } ^ { N } \left[ - \frac { P _ { n } u [ n ] } { \ln 2 ( u _ { \mathrm { f e a } } ^ { 2 } [ n ] + P _ { n } u _ { \mathrm { f e a } } [ n ] ) } - \log _ { 2 } \left( 1 + \frac { P _ { n } } { t [ n ] } \right) \right]\tag{27a}
$$

$$
\begin{array} { r l } & { \mathrm { s . t . ~ } t [ n ] + x _ { \mathrm { f e a } } ^ { 2 } [ n ] - 2 x _ { \mathrm { f e a } } [ n ] x [ n ] + 2 x _ { \mathrm { E } } x [ n ] - x _ { \mathrm { E } } ^ { 2 } + y _ { \mathrm { f e a } } ^ { 2 } [ n ] } \\ & { \phantom { \mathrm { s . t . ~ } } - 2 y _ { \mathrm { f e a } } [ n ] y [ n ] + 2 y _ { \mathrm { E } } y [ n ] - y _ { \mathrm { E } } ^ { 2 } - H ^ { 2 } \leq 0 , \quad \forall n , \quad \phantom { \mathrm { ~ \ } } ( } \\ & { ( 1 ) , ~ ( 2 3 \mathrm { c } ) , ~ ( 2 3 \mathrm { d } ) . } \end{array}\tag{27b}
$$

After such approximation, we note that the objective function of problem (27) is concave and its feasible region is convex. Thus, problem (27) is a convex optimization problem, which can be optimally solved by the interior-point method [44]. Since the first-order Taylor expansions of $- x ^ { 2 } [ n ] { \mathrm { ~ a n d ~ } } - y ^ { 2 } [ n ]$ are their global over-estimators, any solution $( x [ n ] , y [ n ] )$ satisfying (27b) will satisfy (23b). As a result, the solution of problem (27) is guaranteed to be a feasible solution of problem (23). Moreover, the first-order Taylor expansion of 2 $\begin{array} { r } { \left( 1 + \frac { P _ { n } } { u [ n ] } \right) } \end{array}$ is its global under-estimator. As such, problem (27) maximizes a lower bound of the objective function of problem (23), and the lower bound and the objective function of (23) are equal only at the given point $\left( \mathbf { x } _ { \mathrm { f e a } } , \mathbf { y } _ { \mathrm { f e a } } , \mathbf { u } _ { \mathrm { f e a } } \right)$ ; thus, the objective value of problem (23) with the solution obtained by solving problem (27) is no smaller than that with the given point $\left( \mathbf { x } _ { \mathrm { f e a } } , \mathbf { y } _ { \mathrm { f e a } } , \mathbf { u } _ { \mathrm { f e a } } \right)$

## C. Overall Algorithm

In summary, the overall algorithm can find a suboptimal solution to problem (P1) by applying the block coordinate descent method, and solves the two sub-problems (18) and (27) alternately in an iterative manner. The details of the proposed algorithm are summarized in Algorithm 1, where $\mathbf { \bar { \Psi } } R ^ { ( \bar { k } ) } = f _ { ( \mathrm { P 3 } ) } ( \mathbf { p } ^ { ( k ) } , \mathbf { x } ^ { ( k ) } , \mathbf { y } ^ { ( k ) } )$ denotes the objective value of problem (P3) with variables $\mathbf { p } ^ { ( k ) } , \mathbf { x } ^ { ( k ) }$ , and $\bar { \mathbf { y } } ^ { ( k ) }$ in iteration k, and  denotes a small positive threshold indicating the accuracy of convergence. The convergence of Algorithm 1 is proved as follows. First, we show that in iteration k $( k \geq 1 )$ of Algorithm 1, the objective value of problem (P3) is nondecreasing after executing steps 4 and 5. Denote $\phi ( \mathbf { x } , \mathbf { y } , \mathbf { p } )$ as the objective value of problem (P3), and $\xi ( \mathbf { x } , \mathbf { y } , \mathbf { u } , \mathbf { p } )$ and $\xi _ { l b } ( { \bf x } , { \bf y } , { \bf u } , { \bf p } )$ as the objective values of problems (23) and (27), respectively. In step 4, we have the following results:

```latex
Algorithm 1 Proposed Algorithm for Problem (P1)
1: Initialization: Set ${ \overline { { k = 0 } } } .$ . Find an initial feasible solution
$( { \bf p } ^ { ( 0 ) } , { \bf x } ^ { ( 0 ) } , { \bf y } ^ { ( 0 ) } )$ and an initial slack variable $\mathbf { u } ^ { ( 0 ) }$ . Set
$\begin{array} { r } { \bar { R } ^ { ( 0 ) } = f _ { ( \mathrm { P 3 } ) } ( \mathbf { p } ^ { ( 0 ) } , \mathbf { x } ^ { ( 0 ) } , \mathbf { y } ^ { ( 0 ) } ) } \end{array}$ .
2: repeat
3: Set $k = k + 1 .$
4: <sup>= +</sup>With given $\mathbf { p } ^ { ( k - 1 ) }$ , set the feasible solution $\begin{array} { r l } { \mathbf { X } _ { \mathrm { f e a } } } & { { } = } \end{array}$
$\mathbf { x } ^ { ( k - 1 ) } , \mathbf { y } _ { \mathrm { f e a } } = \mathbf { y } ^ { ( k - 1 ) }$ and $\mathbf { u } _ { \mathrm { f e a } } = \mathbf { u } ^ { ( k - 1 ) }$ <sup>=</sup>, then update
<sup>=</sup>the trajectory variable $\left( \mathbf { x } ^ { ( k ) } , \mathbf { y } ^ { ( k ) } \right)$ and the slack variable
$\mathbf { u } ^ { ( k ) }$ <sup>(</sup>by solving problem (27).
5: With given $( \mathbf { x } ^ { ( k ) } , \mathbf { y } ^ { ( k ) } )$ , update the transmit power con
trol variable $\mathbf { \bar { p } } ^ { ( k ) }$ using (20).
6: Set $R ^ { ( k ) } = \bar { f _ { ( \mathrm { P 3 } ) } } ( \mathbf { p } ^ { ( k ) } , \mathbf { \bar { x } } ^ { ( k ) } , \mathbf { y } ^ { ( k ) } )$
7: until $\begin{array} { r } { \frac { R ^ { ( k ) } - R ^ { ( { \check { k } } - 1 ) ^ { \prime } } } { R ^ { ( k ) } } < \epsilon . } \end{array}$
```

$$
\phi ( \mathbf { x } ^ { ( k - 1 ) } , \mathbf { y } ^ { ( k - 1 ) } , \mathbf { p } ^ { ( k - 1 ) } )
$$

$$
= \xi ( \mathbf { x } ^ { ( k - 1 ) } , \mathbf { y } ^ { ( k - 1 ) } , \mathbf { u } ^ { ( k - 1 ) } , \mathbf { p } ^ { ( k - 1 ) } )\tag{28a}
$$

$$
= \xi _ { l b } ( \mathbf { x } ^ { ( k - 1 ) } , \mathbf { y } ^ { ( k - 1 ) } , \mathbf { u } ^ { ( k - 1 ) } , \mathbf { p } ^ { ( k - 1 ) } )\tag{28b}
$$

$$
\leq \xi _ { l b } ( \mathbf { x } ^ { ( k ) } , \mathbf { y } ^ { ( k ) } , \mathbf { u } ^ { ( k ) } , \mathbf { p } ^ { ( k - 1 ) } )\tag{28c}
$$

$$
\leq \xi ( \mathbf { x } ^ { ( k ) } , \mathbf { y } ^ { ( k ) } , \mathbf { u } ^ { ( k ) } , \mathbf { p } ^ { ( k - 1 ) } )\tag{28d}
$$

$$
= \phi ( \mathbf { x } ^ { ( k ) } , \mathbf { y } ^ { ( k ) } , \mathbf { p } ^ { ( k - 1 ) } ) ,\tag{28e}
$$

where (28a) and (28e) hold because problems (22) and (23) have the same optimal value and optimal solution of $( \mathbf { x } , \mathbf { y } ) ;$ (28b) holds because the first-order Taylor expansions in (24), (25), and (26) are tight at the feasible point $( { \bf x } _ { \mathrm { f e a } } , { \bf y } _ { \mathrm { f e a } } , { \bf u } _ { \mathrm { f e a } } ) = ( { \bf x } ^ { ( k - 1 ) } , { \bf y } ^ { ( k - 1 ) } , { \bf \bar { u } } ^ { ( k - 1 ) } ) ;$ (28c) holds because $( \mathbf { x } ^ { ( k ) } , \mathbf { y } ^ { ( k ) } , \mathbf { u } ^ { ( k ) } )$ is the optimal solution to problem (27); (28d) holds because the objective value of problem (27) is a lower bound of that of problem (23). Moreover, in step 5, we have the following inequality

$$
\phi ( \mathbf { x } ^ { ( k ) } , \ \mathbf { y } ^ { ( k ) } , \ \mathbf { p } ^ { ( k - 1 ) } ) \leq \phi ( \mathbf { x } ^ { ( k ) } , \ \mathbf { y } ^ { ( k ) } , \ \mathbf { p } ^ { ( k ) } ) ,\tag{29}
$$

because $\mathbf { p } ^ { ( k ) }$ is the optimal solution to problem (18). Based on (28) and (29), we obtain

$$
\phi ( \mathbf { x } ^ { ( k - 1 ) } , \ \mathbf { y } ^ { ( k - 1 ) } , \ \mathbf { p } ^ { ( k - 1 ) } ) \leq \phi ( \mathbf { x } ^ { ( k ) } , \ \mathbf { y } ^ { ( k ) } , \ \mathbf { p } ^ { ( k ) } ) ,\tag{30}
$$

which means that the objective value of problem (P3) is nondecreasing over iterations in Algorithm 1. In addition, since the optimal value of (P3) is upper-bounded by a finite value, Algorithm 1 is guaranteed to converge. The complexity of Algorithm 1 can be shown to be of $\mathcal { O } ( N _ { \mathrm { i t e } } N ^ { 3 . 5 } )$ , where $N _ { \mathrm { i t e } }$ denotes the iteration number.

## IV. PROPOSED ALGORITHM FOR PROBLEM (P2)

In this section, we consider problem (P2) for the G2U case. Similar to (P1), we solve problem (P2) by considering the following equivalent problem,

$$
\begin{array} { l } { { \displaystyle ( { \bf P 4 } ) \colon } } \\ { { \displaystyle \operatorname* { m a x } _ { { \bf x , y } , { \bf q } } \sum _ { n = 1 } ^ { N } \left[ \log _ { 2 } \left( 1 + \frac { \gamma _ { 0 } q [ n ] } { ( x [ n ] - x _ { \mathrm { G } } ) ^ { 2 } + ( y [ n ] - y _ { \mathrm { G } } ) ^ { 2 } + H ^ { 2 } } \right) \right. } } \\ { { \displaystyle \phantom { \operatorname* { m a x } _ { { \bf x , y } , { \bf q } } \sum _ { n = 1 } ^ { N } \left[ \log _ { 2 } \left( 1 + \frac { \gamma _ { 0 } q [ n ] } { d _ { \mathrm { G E } } ^ { \kappa } } \right) \right] } \left. \qquad \quad ( 3 1 ) \right. } } \end{array}
$$

Although problem (P4) is non-convex, it has a similar structure as problem (P3), which facilitates us to also apply the block coordinate descent method to find an approximate solution for it. Like (P3), problem (P4) can also be decomposed into two sub-problems: one (denoted by sub-problem 3) is to optimize transmit power q under given trajectory $( \mathbf { x } , \mathbf { y } ) ;$ while the other (denoted by sub-problem 4) is to optimize trajectory $\displaystyle ( \mathbf { x } , \mathbf { y } )$ under given transmit power q. The two sub-problems are solved alternately in an iterative manner until convergence. Next, we discuss on how to solve the two sub-problems, respectively.

A. Sub-Problem 3: Optimizing Transmit Power Given UAV Trajectory

With given $\displaystyle ( \mathbf { x } , \mathbf { y } )$ , sub-problem 3 can be expressed as

$$
\operatorname* { m a x } _ { \mathbf { q } } \ \sum _ { n = 1 } ^ { N } \left[ \log _ { 2 } \left( 1 + a _ { n } q [ n ] \right) - \log _ { 2 } \left( 1 + b q [ n ] \right) \right]
$$

$$
{ \mathrm { s . t . ~ } } ( 1 0 ) ,\tag{32}
$$

where $a _ { n }$ is defined in (18) and

$$
b = \frac { \gamma _ { 0 } } { d _ { \mathrm { G E } } ^ { \kappa } } .\tag{33}
$$

Problem (33) is similar to sub-problem 1 given in (18), thus it can be solved by using (20) and (21), provided that $b _ { n }$ in (20) and (21) is replaced with b in (33).

## B. Sub-Problem 4: Optimizing UAV Trajectory Given Transmit Power

With given q, by letting $Q _ { n } = \gamma _ { 0 } \ q [ n ]$ and removing the <sup>= [ ]</sup>terms in the objective function in (31) which are irrelevant to x and y, we express sub-problem 4 as

$$
\begin{array} { r l r } {  { \operatorname* { m a x } _ { \mathbf { x } , \mathbf { y } } \ \sum _ { n = 1 } ^ { N } \log _ { 2 } ( 1 + \frac { Q _ { n } } { ( x [ n ] - x _ { \mathrm { G } } ) ^ { 2 } + ( y [ n ] - y _ { \mathrm { G } } ) ^ { 2 } + H ^ { 2 } } ) } } \\ & { \mathrm { s . t . } \ ( 1 ) . } \end{array}
$$

Unlike sub-problem 2 given in (22) for the U2G case, problem (34) is simplified as maximizing only the average achievable rate from the ground node to the UAV. This is because the trajectory of the UAV determines only the channel gain from the ground node to the UAV, but does not have any effect on the channel from the ground node to the eavesdropper.

Despite the non-convexity of problem (34), we apply the successive convex optimization to approximately solve it, similar to problem (22). First, we introduce slack variable $\mathbf { u } \triangleq [ u [ 1 ] , \dots , u [ N ] ] ^ { \dagger }$ , and solve the following problem which has the same optimal solution of $\displaystyle ( \mathbf { x } , \mathbf { y } )$ as problem (34),

$$
\operatorname* { m a x } _ { \mathbf { x } , \mathbf { y } , \mathbf { u } } \ \sum _ { n = 1 } ^ { N } \log _ { 2 } \left( 1 + { \frac { Q _ { n } } { u [ n ] } } \right)\tag{35a}
$$

$$
\mathrm { s . t . } ~ ( x [ n ] - x _ { \mathrm { G } } ) ^ { 2 } + ( y [ n ] - y _ { \mathrm { G } } ) ^ { 2 } + H ^ { 2 } - u [ n ] \leq 0 ,\tag{∀n,}
$$

(35b)

With a given initial point $\mathbf { u } _ { \mathrm { f e a } } \triangleq [ u _ { \mathrm { f e a } } [ 1 ] , \dots , u _ { \mathrm { f e a } } [ N ] ] ^ { \dagger }$ , which is feasible to (35), and by applying the first-order Taylor expansion of $\begin{array} { r } { \log _ { 2 } { \left( 1 + \frac { Q _ { n } } { u \left[ n \right] } \right) } } \end{array}$ given in (24) (where $P _ { n }$ is replaced by $Q _ { n } )$ , problem (35) is recast as

$$
\begin{array} { l } { \displaystyle \operatorname* { m a x } _ { \mathbf { x } , \mathbf { y } , \mathbf { u } } \ \sum _ { n = 1 } ^ { N } - \frac { Q _ { n } u [ n ] } { \ln 2 \left( u _ { \mathrm { f e a } } ^ { 2 } [ n ] + Q _ { n } u _ { \mathrm { f e a } } [ n ] \right) } } \\ { \displaystyle \mathrm { s . t . } \ ( 1 ) , \ ( 3 5 \mathrm { b } ) . } \end{array}\tag{36}
$$

It can be shown that problem (37) is a convex quadratically constrained quadratic programming (QCQP) problem, and thus can be efficiently solved by the interior-point method [44]. The details of the overall algorithm for solving (P2) are omitted for brevity, given the similarity to that for (P1).

## V. SIMULATION RESULTS

In this section, we provide simulation results to verify the performance of our proposed joint UAV trajectory optimization and transmit power control algorithm (denoted as T-OPT-With-PC). For comparison, we also consider the following three benchmark schemes without optimized trajectory and/or power control:

Trajectory optimization without transmit power control (denoted as T-OPT-Without-PC);

Best-effort trajectory design with transmit power control (denoted as BET-With-PC);

Best-effort trajectory design without transmit power control (denoted as BET-Without-PC).

Specifically, the T-OPT-Without-PC algorithm designs the UAV trajectories for the U2G and G2U cases by solving problems (27) and (37) iteratively until convergence, respectively, with transmit power equally set over time, $\mathrm { i . e . , } \ p [ n ] \ = \ \bar { P }$ and $q [ n ] = \bar { Q }$ , ∀n. The complexity of the T-OPT-Without-PC algorithm is $\mathcal { O } ( N _ { \mathrm { i t e } } N ^ { 3 . 5 } )$ , where $N _ { \mathrm { i t e } }$ denotes the number of iterations required for convergence [35]. Both the BET-With-PC and BET-Without-PC algorithms design the UAV trajectories in the following heuristic best-effort manner: the UAV first flies straight to the point above the ground node at its maximum speed, then remains static at that point (if time permits), and finally flies at its maximum speed to reach its final location by the end of the last time slot. Note that if the UAV does not have sufficient time to reach the point above the ground node, it will turn at a certain midway point and then fly to the final location at the maximum speed. Given this trajectory, the BET-With-PC algorithm optimizes the transmit power in the U2G or G2U case by solving problem (18) or (33), respectively; while the BET-Without-PC algorithm sets transmit power equally over time, i.e., $p [ n ] = { \bar { P } }$ and $q [ n ] = { \bar { Q } } .$ , ∀n. The complexities of the BET-<sup>[ ] = [ ] =</sup>With-PC and BET-Without-PC algorithms are both $\mathcal { O } ( N )$ . The initial feasible solutions for the proposed T-OPT-With-PC and benchmark T-OPT-Without-PC algorithms are generated by the BET-Without-PC algorithm.

![](images/ed23c11f4ee511b436bbdd5113068960e5062f1791231f4622fb1f073efd0676.jpg)  
Fig. 2. Trajectories of the UAV for the U2G communication in Case 1.

The coordinates of the ground node and the eavesdropper are set as (0,0,0)m and (200, 0, 0)m, respectively, and the flying altitude of the UAV is set as $H = 1 0 0 \mathrm { m }$ . The maximum speed of the UAV is $v _ { \mathrm { m a x } } = 3 \mathrm { m } / \mathrm { s }$ . The flight period T is <sup>=</sup>divided into multiple time slots with equal length of $d _ { t } = 0 . 5 \mathrm { s } .$ The communication bandwidth is 20MHz with the carrier frequency at 5GHz, and the noise power spectrum density is −169dBm/Hz. Thus, the reference SNR at the reference distance $d _ { 0 } = 1 \mathrm { m }$ is $\gamma _ { 0 } ~ = ~ 8 0 \mathrm { d B }$ . The peak transmit power limits for the U2G and G2U links are set as $P _ { \mathrm { p e a k } } ~ = ~ 4 \bar { P }$ and $Q _ { \mathrm { p e a k } } = 4 \bar { Q }$ , respectively. The threshold in Algorithm 1 is set as $\epsilon ~ = ~ 1 0 ^ { - 4 }$ . We consider two cases, denoted as Case 1 and Case 2, in which the UAV has different initial and final locations. In Case 1, the UAV’s initial and final locations are on the vertical line in the middle of the ground node and the eavesdropper, and the coordinates of them are set as $( x _ { 0 } , y _ { 0 } ) = ( 1 0 0 , 6 0 0 ) \mathrm { m }$ and $( x _ { F } , y _ { F } ) = ( 1 0 0 , - 6 0 0 ) \mathrm { m }$ <sup>( ) = (100 600) (</sup>as shown in Fig. 2. In Case 2, the $\mathrm { U A V } _ { \mathrm { \Delta } }$ initial and final locations are on the parallel line of that connecting the ground node and the eavesdropper, and the coordinates of them are set as $( x _ { 0 } , y _ { 0 } ) = ( - 5 0 0 , - 1 5 0 )$ m and $( x _ { F } , y _ { F } ) = ( 7 0 0 , - 1 5 0 ) \mathrm { m }$ 9 as shown in Figs. 5 and 9.

## A. U2G Communication

In the U2G case, we first consider Case 1. Fig. 2 shows the trajectories of the UAV by applying different algorithms with different values of flight period T . The average transmit power is set as $\bar { P } \ = \ - 5 \mathrm { d B m }$ . The locations of the ground node, eavesdropper, as well as the $\mathrm { U A V } _ { \mathrm { \Delta } }$ initial and final locations are marked with $\bigcirc , \bigtriangleup , \times$ , and , respectively. It is observed <sup>+</sup>that when T 400s which is the minimum time required for the UAV to fly from the initial location to the final location in a straight line at the maximum speed, the trajectories of all algorithms are identical. As T increases, the trajectories by the proposed T-OPT-With-PC and the benchmark T-OPT-Without-PC algorithms are still similar, i.e., the UAV tries to fly as close as possible to the ground node and at the same time as far away as possible to the eavesdropper, while they appear different compared to that by the heuristic best-effort trajectory (BET) design (same for with and without power control). When T is sufficiently large, i.e. $T = 6 0 0 \mathrm { s } .$ for the proposed T-OPT-With-PC algorithm or the benchmark T-OPT-Without-PC algorithm, it is observed that the UAV first flies at the maximum speed to reach a certain location on the left of the ground node (not directly above it), then remains stationary at this location as long as possible, and finally flies to the final location in an arc path at the maximum speed and reaches there by the end of the last time slot. These stationary locations, which are on the opposite direction of the eavesdropper, strike an optimal balance between enhancing the legitimate link channel and degrading the eavesdropping link channel and hence maximize the secrecy rate in each of these two cases. In fact, this is also why the UAV follows an arc path rather than the straight path as in the heuristic BET design.

![](images/ea0416b430b53c2dc117782ac09c06ba67ec64fbb37820b59b680a1345ad63f2.jpg)  
Fig. 3. Secrecy rate versus flight period T for the U2G communication in Case 1.

Fig. 3 shows the corresponding average secrecy rates of different algorithms versus flight period T when $\bar { P } = - 5 \mathrm { d B m }$ and 5dBm. It is observed that the secrecy rates of all algorithms increase significantly with T . This is because for all algorithms the maximum secrecy rate is achieved at their respective stationary locations (see Fig. 2) for sufficiently large T , and larger $T$ results in longer hovering time at such locations for the UAV. The proposed T-OPT-With-PC algorithm always achieves the highest secrecy rate, while the benchmark BET-Without-PC algorithm has the lowest secrecy rate, as expected. When $\bar { P } = - 5 \mathrm { d B m }$ , the benchmark BET-With-PC algorithm has higher secrecy rate than that of the benchmark T-OPT-Without-PC algorithm. In contrast, when $\bar { P } \ = \ 5 \mathrm { d B m }$ , the latter algorithm has higher secrecy rate than the former. Such results suggest that in the low transmit power regime, power control is more important for improving the secrecy rate; while in the high transmit power regime, trajectory optimization is more significant. Furthermore, it is worth pointing out that trajectory adaptation with increasing T is essential for the secrecy rate improvement, even for the case with heuristic BET design. Otherwise, if the trajectory is fixed (e.g., following the straight line from the initial to final location with constant speed of $\sqrt { ( x _ { F } - x _ { 0 } ) ^ { 2 } + ( y _ { F } - y _ { 0 } ) ^ { 2 } } / T$ regardless of $T ,$ then the secrecy rate will remain unchanged as the case with required minimum $T = 4 0 0 { \mathrm { s } }$ in Fig. 3, i.e., the UAV cannot exploit its mobility to improve the secrecy rate, even with sufficiently large T .

![](images/3bb8b86ffdfe211117a37611eba7f3d2f5c7e531ead87d2f007d2bd938b65bbc.jpg)  
Fig. 4. Secrecy rate versus average transmit power P<sup>¯</sup> for the U2G communication in Case 1.

Fig. 4 shows the average secrecy rates of different algorithms versus the average transmit power $\bar { P }$ when $T = 4 0 3 \mathrm { s }$ and 600s. It is observed that the proposed T-OPT-With-PC algorithm always achieves the highest secrecy rate, while the benchmark BET-Without-PC algorithm has the lowest secrecy rate. In addition, when ${ \bar { P } } \leq - 5 \mathrm { d B }$ , we note that the benchmark BET-With-PC algorithm achieves a secrecy rate performance close to the proposed T-OPT-With-PC algorithm, and also significantly outperforms the benchmark T-OPT-Without-PC algorithm. However, when P increases, the secrecy rate of the benchmark T-OPT-Without-PC algorithm will eventually exceed that of the benchmark BET-With-PC algorithm and even get closer to that of the proposed T-OPT-With-PC algorithm. Furthermore, the rate gap between the benchmark T-OPT-Without-PC and BET-With-PC algorithms becomes larger with increasing P . The above results further demonstrate that transmit power control is more effective in improving secrecy rate than trajectory optimization when the average transmit power is low, while trajectory optimization is more effective when the average transmit power is high.

Next, we consider Case 2. Fig. 5 shows the trajectories of the UAV by using different algorithms when ${ \bar { P } } = - 5 \mathrm { d B m } .$ It is observed that different from the results in Case 1 shown in Fig. 2, the trajectories by the proposed T-OPT-With-PC and benchmark T-OPT-Without-PC algorithms with $T =$ <sup>=</sup>405s or 600s differ significantly, especially when the UAV flies towards the final location. For the proposed algorithm, the UAV flies along a relatively direct path towards the ground node and then towards the final location. In contrast, for this benchmark, the UAV first flies almost directly to the ground node, but then flies along an arc path to the final location, which inevitably consumes more time on the traveling compared to the trajectory of the proposed algorithm. The reason for such a difference is that in Case 2, flying from the ground node towards the final location reduces the distance from the UAV to the eavesdropper less much as compared to that from it to the ground node, which is undesired. This means that to improve the secrecy rate, the UAV should reduce transmit power when it gets farther away from the ground node and closer to the final location. Considering this fact, the proposed T-OPT-With-PC algorithm is able to decrease the UAV transmit power or even turn off the transmitter to save power and also protect from eavesdropping when the UAV flies directly towards the final location. However, for the benchmark T-OPT-Without-PC algorithm that employs a constant transmit power, the UAV can only rely on adjusting its trajectory to keep far away from the eavesdropper to avoid being eavesdropped, which however requires more traveling time and leads to a longer arc trajectory. This fact is verified by Fig. 6, which shows the transmit power of the UAV over time slot when the flight period is $T = 6 0 0 { \mathrm { s } }$ . It is observed <sup>=</sup>that both the proposed T-OPT-With-PC and benchmark BET-With-PC algorithms increase UAV transmit power when the UAV gets closer to the ground node, and reduce UAV transmit power when the UAV gets farther away from the ground node and closer to the final location. When the UAV is in the zone where the distance from it to the ground node is larger than that to the eavesdropper, the proposed T-OPT-With-PC and benchmark BET-With-PC algorithms set UAV transmit power to zero.

![](images/b8adcc1fc5d9e4a1c27cd389e3dc93791e285db39cb2f26d5d2c0b42f738d032.jpg)  
Fig. 5. Trajectories of the UAV for the U2G communication in Case 2.

![](images/bb6e5863976f036625092922c43725dd9370ca8b453c3b8044355d3f8fe8fd70.jpg)  
Fig. 6. Transmit power versus time slot for the U2G communication in Case 2 when $T = { \bar { 6 0 0 } } \mathrm { s }$

![](images/ec076ecdee930491991baf999b98080c2b5132fdd70282629fc7540c1fb9b5b0.jpg)  
Fig. 7. Secrecy rate versus flight period $_ T$ for the U2G communication in Case 2.

![](images/d98f04fd365d214f08ed8cebb152e8955d1a05d2a6a1ccd3e0a7509ad666caae.jpg)  
Fig. 8. Secrecy rate versus average transmit power $\bar { P }$ for the U2G communication in Case 2.

With the UAV trajectory difference in Fig. 5, the secrecy rate performances of different algorithms versus $T$ and ${ \bar { P } } ,$ which are shown in Figs. 7 and 8 respectively, are also quite different from those shown in Figs. 3 and 4 for Case 1. Specifically, the secrecy rate gaps between the proposed T-OPT-With-PC and benchmark T-OPT-Without-PC algorithms versus $T \ \mathrm { o r } \ \bar { P }$ in Case 2 are significantly larger than those in Case 1. For example, in Fig. 7, the T-OPT-Without-PC algorithm even has lower secrecy rate than the BET-Without-PC algorithm in the regime of $T \leq 6 5 0 \mathrm { s }$ s when $\bar { P } = - 5 \mathrm { d B m }$ or in the regime of $T \le 5 5 0 \mathrm { s }$ when $\bar { P } = 5 \mathrm { d B m }$ . In addition, in Fig. 8, the T-OPT-Without-PC algorithm has a lower secrecy rate than the BET-Without-PC algorithm over the whole $\bar { P }$ regime when $T = 4 0 5 \mathrm { s }$ and in the regime of $\bar { P } \le 0 \mathrm { d B m }$ when $T = 6 0 0 \mathrm { s }$ <sup>= =</sup>This is mainly because the UAV wastes more time on travelling along a longer arc trajectory to reach the final location which in turn leads to the inefficient use of the transmit power. The above results demonstrate the importance and necessity of the joint UAV trajectory optimization and transmit power control in maximizing the secrecy rate for U2G communication.

From Figs. 2–8, it is observed that although the proposed T-OPT-With-PC algorithm always achieves the highest secrecy rate in all cases, other benchmark algorithms of lower complexity may achieve reasonably good performance as compared to the proposed algorithm in certain cases. As such, depending on the system parameters (e.g., average transmit power, flight period, and the $\mathrm { U A V } _ { \mathrm { \Delta } }$ initial and final locations), the UAV may adopt different algorithms to strike a balance between the achievable performance and computational complexity. In particular, for the case with short $T$ and/or high ${ \bar { P } } ,$ trajectory optimization is generally less effective as compared to transmit power control in improving secrecy rate, thus the benchmark algorithm BET-With-PC performs very close to the proposed algorithm; while if both the initial and final locations of the UAV are closer to the ground node than the eavesdropper, trajectory optimization is more effective, thus T-OPT-Without-PC is a good choice from both performance and complexity considerations.

![](images/6c59d6019f46dab721ffab60db1870bc0596633d9cb2847a0a8767aff25d60f7.jpg)  
Fig. 9. Trajectories of the UAV for the G2U communication in Case 2.

## B. G2U Communication

In the G2U case, the channel gain from the ground node to the eavesdropper given in (9) contains a small-scale Rayleigh fading term ζ. Thus, all secrecy rate results in the following are averaged over 5000 random independent realizations of $\zeta ,$ where the path-loss exponent is set as $\kappa = 3 .$ . Since our results obtained for Cases 1 and 2 lead to consistent observations, we only present the results for Case 2 due to the space limitation.

Fig. 9 shows the trajectories of the UAV with different values of $T$ when the average transmit power is $\bar { Q } = - 5 \mathrm { d B m }$ <sup>=</sup>It is observed that the trajectories of the proposed T-OPT-With-PC and benchmark T-OPT-Without-PC algorithms are very similar for different values of T , i.e., the UAV tries to fly as close as possible to the ground node as T increases. When $T$ is sufficiently large, i.e., $T = 6 0 0 { \mathrm { s } }$ , the trajectories of them <sup>=</sup>are the same as the heuristic BET design, i.e., the UAV first flies at the maximum speed to reach the point right above the ground node, then remains static as long as possible, and finally flies to the final location directly at the maximum speed in order to reach there by the end of the last time slot. The fundamental reason of such a result is that in the G2U setup, the channel between the ground node (transmitter) and the eavesdropper is independent of the UAV’s location. Therefore, the UAV trajectory is only optimized to maximize achievable rate from the ground node to the UAV. Obviously, the point right above the ground node is the best location for achieving its largest rate. This explains why the optimized trajectory also converges to the heuristic BET design when T is sufficiently large.

![](images/a1fe5d4fa5533c7a535ac53de4e3a2e1b6e2d071bf970b604ec6921e34a2e0af.jpg)

Fig. 10. Secrecy rate versus flight period T for the G2U communication in Case 2.  
![](images/d21d228244fcaf0d51b3908208e0138a1c3513cc2d0f07c190d927d113025eab.jpg)  
Fig. 11. Secrecy rate versus average transmit power $\bar { Q }$ for the G2U communication in Case 2.

Fig. 10 shows the average secrecy rates of different algorithms versus flight period $T$ when $\bar { Q } = - 5 \mathrm { d B m }$ and 5dBm. When $T \geq 4 1 0 \mathrm { s }$ , the algorithms with transmit power control, i.e. the proposed T-OPT-With-PC and benchmark BET-With-PC algorithms, achieve the same secrecy rate since they have the same trajectory and hence the same transmit power control, while they both outperform the benchmark algorithms without power control, i.e., the T-OPT-Without-PC and BET-Without-PC algorithms. These results suggest that transmit power control is more effective than trajectory optimization in improving secrecy rate in the G2U case, as shown in Fig. 9, since the optimal trajectory can be easily achieved by the BET design when T is sufficiently large. Furthermore, the secrecy rate gap between the algorithms with and without power control when $\bar { Q } \ = \ - 5 \mathrm { d B m }$ is significantly larger than that when Q 5dBm, since power control is more effective when the average transmit power is low.

Fig. 11 shows the average secrecy rates of different algorithms versus average transmit power $\bar { Q }$ when $T = 4 0 5 \mathrm { s }$ and 600s. It can be also observed that transmit power control is effective for improving secrecy rate when ${ \bar { Q } } ~ \leq ~ 0 \mathrm { d B m }$ When $T = 4 0 5 \mathrm { s } ,$ the secrecy rate gap between the proposed <sup>=</sup>T-OPT-With-PC algorithm and the benchmark algorithms with BET design exists due to their trajectory difference. When $T = 6 0 0 { \mathrm { s } }$ , the secrecy rates of all algorithms tend to be very similar when $\bar { Q } \ge 1 0 \mathrm { d B m }$ . This is because their trajectories are the same and the power control only provides marginal rate gain when transmit power is high.

## VI. CONCLUSION

In this paper, we study the physical layer security for emerging UAV communications in the forthcoming 5G wireless networks. Specifically, we propose to enhance the security performance by proactively controlling channel gains via adjusting the UAV trajectory in addition to applying the conventional power/rate adaptation, which leads to a new joint optimization framework. For both the U2G and G2U communications, the transmit power control and UAV trajectory are jointly designed to maximize the average secrecy rate over a finite horizon, subject to the average and peak transmit power constraints as well as practical UAV’s mobility constraints. By applying the block coordinate descent and successive convex optimization methods, efficient iterative algorithms are proposed to solve the joint design problems. Simulation results show that joint trajectory optimization and transmit power control improves the physical layer security performance, and more significantly in the U2G case compared to the G2U case, as the UAV trajectory in the U2G case has an effect on both the legitimate and eavesdropping channels, instead of the legitimate channel only in the G2U case. Furthermore, it is found that both UAV trajectory optimization and transmit power control are generally necessary in the U2G case; while in the G2U case, transmit power control is more effective than UAV trajectory optimization for improving the secrecy rate performance, and the heuristic best-effort trajectory already performs quite close to the optimized trajectory.

## REFERENCES

[1] G. Zhang, Q. Wu, M. Cui, and R. Zhang, “Securing UAV communications via trajectory optimization,” in Proc. IEEE GLOBECOM, Dec. 2017, pp. 1–6.

[2] Y. Zeng, R. Zhang, and T. J. Lim, “Wireless communications with unmanned aerial vehicles: Opportunities and challenges,” IEEE Commun. Mag., vol. 54, no. 5, pp. 36–42, May 2016.

[3] Q. Wu, G. Y. Li, W. Chen, D. W. K. Ng, and R. Schober, “An overview of sustainable green 5G networks,” IEEE Wirless Commun., vol. 24, no. 4, pp. 72–80, Aug. 2017.

[4] S. Zhang, Q. Wu, S. Xu, and G. Y. Li, “Fundamental green tradeoffs: Progresses, challenges, and impacts on 5G networks,” IEEE Commun. Surveys Tuts., vol. 19, no. 1, pp. 33–56, 1st Quart., 2017.

[5] Paving the Path to 5G: Optimizing Commercial LTE Networks for Drone Communication. Accessed: Jan. 2018. [Online]. Available: https://www.qualcomm.com/news/onq/2016/09/06/paving-path-5g optimizing-commercial-lte-networks-drone-communication

[6] Ericsson and China Mobile Conduct world’s First 5G Drone Prototype Field Trial. Accessed: Jan. 2018. [Online]. Available: https://www.ericsson.com/en/news/2016/8/ericsson-and-china-mobileconduct-worlds-first-5g-drone-prototype-field-trial

[7] M. Mozaffari, W. Saad, M. Bennis, and M. Debbah, “Drone small cells in the clouds: Design, deployment and performance analysis,” in Proc. IEEE Global Commun. Conf. (GLOBECOM), Dec. 2015, pp. 1–6.

[8] M. Mozaffari, W. Saad, M. Bennis, and M. Debbah, “Unmanned aerial vehicle with underlaid device-to-device communications: Performance and tradeoffs,” IEEE Trans. Wireless Commun., vol. 15, no. 6, pp. 3949–3963, Jun. 2016.

[9] R. I. Bor-Yaliniz, A. El-Keyi, and H. Yanikomeroglu, “Efficient 3-D placement of an aerial base station in next generation cellular networks,” in Proc. IEEE ICC, May 2016, pp. pp. 1–5.

[10] J. Lyu, Y. Zeng, R. Zhang, and T. J. Lim, “Placement optimization of UAV-mounted mobile base stations,” IEEE Commun. Lett., vol. 21, no. 3, pp. 604–607, Mar. 2017.

[11] Q. Wu, L. Liu, and R. Zhang, “Fundamental tradeoffs in communication and trajectory design for UAV-enabled wireless network,” IEEE Wireless Commun., to be published. [Online]. Available: https://arxiv.org/pdf/1805.07038

[12] Q. Wu, Y. Zeng, and R. Zhang, “Joint trajectory and communication design for multi-UAV enabled wireless networks,” IEEE Trans. Wireless Commun., vol. 17, no. 3, pp. 2109–2121, Mar. 2018.

[13] Q. Wu and R. Zhang, “Common throughput maximization in UAVenabled OFDMA systems with delay consideration,” IEEE Trans. Commun., vol. 66, no. 12, pp. 6614–6627, Dec. 2018.

[14] Q. Wu, J. Xu, and R. Zhang, “Capacity characterization of UAV-enabled two-user broadcast channel,” IEEE J. Sel. Areas Commun., vol. 36, no. 9, pp. 1955–1971, Sep. 2018.

[15] V. Sharma, M. Bennis, and R. Kumar, “UAV-assisted heterogeneous networks for capacity enhancement,” IEEE Commun. Lett., vol. 20, no. 6, pp. 1207–1210, Jun. 2016.

[16] Y. Zeng et al., “Throughput maximization for UAV-enabled mobile relaying systems,” IEEE Trans. Commun., vol. 64, no. 12, pp. 4983–4996, Dec. 2016.

[17] T. A. Johansen, A. Zolich, T. Hansen, and A. J. Sørensen, “Unmanned aerial vehicle as communication relay for autonomous underwater vehicle—Field tests,” in Proc. IEEE GLOBECOM Workshops, Dec. 2014, pp. 1469–1474.

[18] S. Sotheara, K. Aso, N. Aomi, and S. Shimamoto, “Effective data gathering and energy efficient communication protocol in wireless sensor networks employing UAV,” in Proc. IEEE WCNC, 2014, pp. 2342–2347.

[19] J. Lyu, Y. Zeng, and R. Zhang, “Cyclical multiple access in UAV-aided communications: A throughput-delay tradeoff,” IEEE Wireless Commun. Lett., vol. 5, no. 6, pp. 600–603, Dec. 2016.

[20] M. Mozaffari, W. Saad, M. Bennis, and M. Debbah, “Mobile unmanned aerial vehicles (UAVs) for energy-efficient Internet of Things communications,” IEEE Trans. Wireless Commun., vol. 16, no. 11, pp. 7574–7589, Nov. 2017.

[21] Cellular Enables Safer Drone Deployments. [Online]. Available: https://www.qualcomm.com/invention/technologies/lte/advancedpro/cellular-drone-communication

[22] N. H. Motlagh, M. Bagaa, and T. Taleb, “UAV-based IoT platform: A crowd surveillance use case,” IEEE Commun. Mag., vol. 55, no. 2, pp. 128–134, Feb. 2017.

[23] P. K. Gopala, L. Lai, and H. El Gamal, “On the secrecy capacity of fading channels,” IEEE Trans. Inf. Theory, vol. 54, no. 10, pp. 4687–4698, Oct. 2008.

[24] Y. Liang, H. V. Poor, and S. Shamai (Shitz), “Secure communication over fading channels,” IEEE Trans. Inf. Theory, vol. 54, no. 6, pp. 2470–2492, Jun. 2008.

[25] X. Wang, M. Tao, J. Mo, and Y. Xu, “Power and subcarrier allocation for physical-layer security in OFDMA-based broadband wireless networks,” IEEE Trans. Inf. Forensics Security, vol. 6, no. 3, pp. 693–702, Sep. 2011.

[26] H. Xing, L. Liu, and R. Zhang, “Secrecy wireless information and power transfer in fading wiretap channel,” IEEE Trans. Veh. Technol., vol. 65, no. 1, pp. 180–190, Jan. 2016.

[27] A. Khisti and G. W. Wornell, “Secure transmission with multiple antennas—Part II: The MIMOME wiretap channel,” IEEE Trans. Inf. Theory, vol. 56, no. 11, pp. 5515–5532, Nov. 2010.

[28] J. Tang et al., “Associating MIMO beamforming with security codes to achieve unconditional communication security,” IET Commun., vol. 10, no. 12, pp. 1522–1531, Aug. 2016.

[29] G. Zheng, L.-C. Choo, and K.-K. Wong, “Optimal cooperative jamming to enhance physical layer security using relays,” IEEE Trans. Signal Process., vol. 59, no. 3, pp. 1317–1322, Mar. 2011.

[30] Y. Zou, X. Wang, and W. Shen, “Physical-layer security with multiuser scheduling in cognitive radio networks,” IEEE Trans. Commun., vol. 61, no. 12, pp. 5103–5113, Dec. 2013.

[31] J. Tang, M. Dabaghchian, K. Zeng, and H. Wen, “Impact of mobility on physical layer security over wireless fading channels,” IEEE Trans. Wireless Commun., vol. 17, no. 12, pp. 7849–7864, Dec. 2018.

[32] G. Zhang, X. Li, M. Cui, G. Li, and L. Yang, “Signal and artificial noise beamforming for secure simultaneous wireless information and power transfer multiple-input multiple-output relaying systems,” IET Commun., vol. 10, no. 7, pp. 796–804, May 2016.

[33] G. Zhang, J. Xu, Q. Wu, M. Cui, X. Li, and F. Lin, “Wireless powered cooperative jamming for secure OFDM system,” IEEE Trans. Veh. Technol., vol. 67, no. 2, pp. 1331–1346, Feb. 2018.

[34] A. Li, Q. Wu, and R. Zhang, “UAV-enabled cooperative jamming for improving secrecy of ground wiretap channel,” IEEE Wireless Commun. Lett., to be published. [Online]. Available: https://ieeexplore.ieee.org/document/8438310, doi: 10.1109/LWC.2018.2865774.

[35] M. Cui, G. Zhang, Q. Wu, and D. W. K. Ng, “Robust trajectory and transmit power design for secure UAV communications,” IEEE Trans. Veh. Technol., vol. 67, no. 9, pp. 9042–9046, Sep. 2018.

[36] M. Erdelj, E. Natalizio, K. R. Chowdhury, and I. F. Akyildiz, “Help from the sky: Leveraging UAVs for disaster management,” IEEE Pervasive Comput., vol. 16, no. 1, pp. 24–32, Jan. 2017.

[37] M. Caris et al., “mm-Wave SAR demonstrator as a test bed for advanced solutions in microwave imaging,” IEEE Aerosp. Electron. Syst. Mag., vol. 29, no. 7, pp. 8–15, Jul. 2014.

[38] D. He, S. Chan, and M. Guizani, “Communication security of unmanned aerial vehicles,” IEEE Wireless Commun., vol. 24, no. 4, pp. 134–139, Aug. 2017.

[39] D. He, Y. Qiao, S. Chan, and N. Guizani, “Flight security and safety of drones in airborne fog computing systems,” IEEE Commun. Mag., vol. 56, no. 5, pp. 66–71, May 2018.

[40] A. Singandhupe, H. M. La, and D. Feil-Seifer, “Reliable security algorithm for drones using individual characteristics from an EEG signal,” IEEE Access, vol. 6, pp. 22976–22986, 2018.

[41] F. Jiang and A. L. Swindlehurst, “Optimization of UAV heading for the ground-to-air uplink,” IEEE J. Sel. Areas Commun., vol. 30, no. 5, pp. 993–1005, Jun. 2012.

[42] Y. Zeng and R. Zhang, “Energy-efficient UAV communication with trajectory optimization,” IEEE Trans. Wireless Commun., vol. 16, no. 6, pp. 3747–3760, Jun. 2017.

[43] X. Lin et al., “The sky is not the limit: LTE for unmanned aerial vehicles,” IEEE Commun. Mag., vol. 56, no. 4, pp. 204–210, Apr. 2018.

[44] S. Boyd and L. Vandenberghe, Convex Optimization. Cambridge, U.K.: Cambridge Univ. Press, 2004.

![](images/b3ddaa7682f0a5904d9a54db76c1cd6c086d23d9f1782491bd8e4081d1e0a041.jpg)

Guangchi Zhang (M’13) received the B.S. degree in electronic engineering from the Nanjing University, Nanjing, China, in 2004, and the Ph.D. degree in communication engineering from the Sun Yat-sen University, Guangzhou, China, in 2009. He has been with the School of Information Engineering, Guangdong University of Technology, Guangzhou, since 2009, where he is currently a Professor. From 2011 to 2012, he was a Senior Research Associate with the City University of Hong Kong. From 2017 to 2018, he was a Visiting Professor with

the National University of Singapore. His research interests include MIMO and relay wireless communications, wireless power transfer, unmanned aerial vehicle communications, and physical layer security. He was a recipient of the IEEE Communications Society 2014 Heinrich Hertz Award and the IEEE Communication Letters 2014 Exemplary Reviewer.

![](images/cc5913fb73663f989e2a49e9ef3173274a6de4b0126d906dac4099e220901851.jpg)

Qingqing Wu (S’13–M’16) received the B.Eng. degree in electronic engineering from the South China University of Technology in 2012, and the Ph.D. degree in electronic engineering from the Shanghai Jiao Tong University, China, in 2016 (in advance). He is currently a Research Fellow with the National University of Singapore. His research interests include intelligent reflecting surface, energy-efficient wireless communications, wireless power transfer, and unmanned aerial vehicle communications. He has served

as a TPC member of the IEEE ICC, GLOBECOM, WCNC, VTC, APCC, and WCSP. He received the IEEE WCSP Best Paper Award in 2015, the Exemplary Reviewer of the IEEE COMMUNICATIONS LETTERS in 2016 and 2017, and the Exemplary Reviewer of the IEEE TRANSAC-TIONS ON COMMUNICATIONS and the IEEE TRANSACTIONS ON WIRELESS COMMUNICATIONS in 2017. He was a recipient of the Outstanding Ph.D. Thesis Funding in SJTU in 2016, and the Best Ph.D. Thesis Award of the China Institute of Communications in 2017. He is currently an Editor of the IEEE COMMUNICATIONS LETTERS and the Workshop Co-Chair of the ICC 2019.

![](images/697a1cd85cc19a4a9f1d5ae73b664f6aab95f34001c260f67f8567784dfc2c00.jpg)

Miao Cui received the B.E. degree in communication engineering and the M.S. degree in computer science from the Northeast Electric Power University, Jilin, China, in 2001 and 2003, respectively, and the Ph.D. degree in circuit system from the South China University of Technology, Guangzhou, China, in 2009. She is currently a Lecturer with the Guangdong University of Technology, Guangzhou. Her research interests include the analysis, optimization, and design of wireless networks.

![](images/c8be8a9b8a110cb45b4fdeb71d585a43c7b6d655b1856036026bc68d97c6197b.jpg)

Rui Zhang (S’00–M’07–SM’15–F’17) received the B.Eng. (Hons.) and M.Eng. degrees from the National University of Singapore, Singapore, and the Ph.D. degree from the Stanford University, Stanford, CA, USA, all in electrical engineering.

From 2007 to 2010, he was a Research Scientist at the Institute for Infocomm Research, A\*STAR, Singapore. Since 2010, he has been with the Department of Electrical and Computer Engineering, National University of Singapore, where he is currently the Dean’s Chair Associate Professor with the Faculty

of Engineering. He has authored over 300 papers. Since 2015, he has been listed as a Highly Cited Researcher (also known as the World’s Most Influential Scientific Minds), by Thomson Reuters (Clarivate Analytics). His research interests include UAV/satellite communication, wireless information and power transfer, multiuser MIMO, smart and reconfigurable environment, and optimization methods.

Dr. Zhang has served as the TPC co-chair or an organizing committee member for over 30 international conferences. From 2012 to 2017, he was an Elected Member of the IEEE Signal Processing Society SPCOM Technical Committee, and the SAM Technical Committee from 2013 to 2015. He serves as a member of the Steering Committee for the IEEE WIRELESS COMMUNICATIONS LETTERS. He was a recipient of the 6th IEEE Communications Society Asia-Pacific Region Best Young Researcher Award in 2011, and the Young Researcher Award of the National University of Singapore in 2015. He was a co-recipient of the IEEE Marconi Prize Paper Award in wireless communications in 2015, the IEEE Communications Society Asia-Pacific Region Best Paper Award in 2016, the IEEE Signal Processing Society Best Paper Award in 2016, the IEEE Communications Society Heinrich Hertz Prize Paper Award in 2017, the IEEE Signal Processing Society Donald G. Fink Overview Paper Award in 2017, and the IEEE Technical Committee on Green Communications and Computing Best Journal Paper Award in 2017. His co-authored paper received the IEEE Signal Processing Society Young Author Best Paper Award in 2017. He has served as the Vice Chair of the IEEE Communications Society Asia-Pacific Board Technical Affairs Committee from 2014 to 2015. He has served as a Guest Editor for three special issues of the IEEE JOURNAL OF SELECTED TOPICS IN SIGNAL PROCESSING and the IEEE JOURNAL ON SELECTED AREAS IN COMMUNICATIONS, and as an Editor for the IEEE TRANSACTIONS ON WIRELESS COMMUNICATIONS, from 2012 to 2016, the IEEE JOURNAL ON SELECTED AREAS IN COMMUNICATIONS: Green Communications and Networking Series, from 2015 to 2016, and the IEEE TRANSACTIONS ON SIGNAL PROCESSING from 2013 to 2017. He is currently an Editor of the IEEE TRANSACTIONS ON COMMUNICATIONS and the IEEE TRANSACTIONS ON GREEN COMMUNICATIONS AND NETWORKING. He is a Distinguished Lecturer of the IEEE Signal Processing Society and the IEEE Communications Society.