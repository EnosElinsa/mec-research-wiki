# Low-Altitude UAV Friendly-Jamming for Satellite-Maritime Communications via Generative AI-Enabled Deep Reinforcement Learning

Jiawei Huang, Aimin Wang, Geng Sun , Senior Member, IEEE, Jiahui Li , Member, IEEE, Jiacheng Wang , Dusit Niyato , Fellow, IEEE, and Victor C. M. Leung , Life Fellow, IEEE

Abstract—Low Earth orbit (LEO) satellites can be used to assist maritime wireless communications for wide-area data transmission. However, the extensive coverage of LEO satellites, combined with the openness of channels, can cause the communication process to suffer from security risks. This paper presents a LEO satellite-maritime communication system assisted by low-altitude uncrewedaerial vehicle (UAV) friendly-jamming to ensure data security at the physical layer. Since such a system requires balancing the conflicting performance metrics of secrecy rate and energy consumption of the UAV to meet evolving scenario demands, we formulate a secure satellite-maritime communication multiobjective optimization problem (SSMCMOP). In order to solve the

Received 26 January 2025; revised 11 October 2025; accepted 9 November 2025. Date of publication 11 November 2025; date of current version 6 March 2026. This work was supported in part by the National Natural Science Foundation of China under Grant 62272194 and Grant 62471200, in part by the Science and Technology Development Plan Project of Jilin Province under Grant 20250101027JJ, in part by Seatrium New Energy Laboratory, Singapore Ministry of Education (MOE) Tier 1 under Grant RT5/23 and RG24/24, in part by the Nanyang Technological University (NTU) Centre for Computational Technologies in Finance (NTU-CCTF), in part by the Research Innovation and Enterprise (RIE) 2025 Industry Alignment Fund - Industry Collaboration Projects (IAF-ICP) under Grant I2301E0026, administered by Agency for Science, Technology and Research (A\*STAR), in part by the Postdoctoral Fellowship Program of China Postdoctoral Science Foundation under Grant GZC20240592, in part by China Postdoctoral Science Foundation General Fund under Grant 2024M761123, and in part by Graduate Innovation Fund of Jilin University under Grant 2025CX213. Recommended for acceptance by J. Lee. (Corresponding authors: Geng Sun; Jiahui Li.)

Digital Object Identifier 10.1109/TMC.2025.3631861

dynamic and long-term optimization problem, we reformulate it into a Markov decision process. We then propose a transformerenhanced soft actor-critic (TransSAC) algorithm, which is a generative artificial intelligence-enabled deep reinforcement learning approach to solve the reformulated problem, thus capturing strong temporal correlations and diversely exploring weights. Simulation results demonstrate that the TransSAC algorithm outperforms comparative approaches and algorithms, maximizing the secrecy rate while effectively minimizing the energy consumption of the UAV. Moreover, the results identify more suitable constraints for the system.

Index Terms—LEO satellite-maritime communications, physical layer secure, UAV friendly-jamming, multi-objective optimization, deep reinforcement learning.

## I. INTRODUCTION

N RECENT years, with the rapid expansion of the maritime increased significantly [1]. A reliable and stable communication network is essential to ensure the efficiency of maritime operations [2]. However, the challenges of deploying foundational communication infrastructures, combined with the complexity and variability of the maritime channels, may result in lower transmission rates for maritime networks than terrestrial cellular networks [3]. In this case, satellites, with extensive coverage capabilities, are increasingly being utilized for maritime data transmission, thereby facilitating the effective exchange of data from vessels at sea [4]. In particular, the low Earth orbit (LEO) satellites, operating closer to the Earth, have higher stability for enhancing communication performance [5]. However, the open channels and extensive coverage of LEO satellites make them vulnerable to unauthorized access and potential eavesdropping by malicious users, which may pose security risks [6]. Although the traditional cryptography-based methods can cope with the security risks in some cases, they require frequent data encoding and decoding, and complex key distribution and management, which pose challenges in the energy-limited maritime environment when large amounts of data are transmitted [7].

In this case, physical layer security (PLS) can dynamically adjust security mechanisms, making it a suitable way to ensure secure communication in the LEO satellite-maritime networks [8].

This article has supplementary downloadable material available at https://doi.org/10.1109/TMC.2025.3631861, provided by the authors.

For example, through intelligent beamforming methods, LEO satellites can focus signals on target vessels by optimizing the directionality and power distribution of the transmitting antenna, thereby reducing the probability of illegitimate users acquiring signals [9]. However, for high-speed moving LEO satellites, real-time computation and adjustment of beamforming parameters place high demands on the hardware, leading to a greater computational burden [10]. As such, low-altitude platforms are used to introduce friendly-jamming signals to enhance PLS.

Common low-altitude platforms include uncrewed aerial vehicles (UAVs) and electric vertical take-off and landing (eV-TOL) aircraft [11]. In complex maritime environments, UAVs, with low costs, adjustable flight altitudes, and flexible mobility, are particularly suitable for overcoming movement and operation limitations imposed by sea terrain and obstacles [12]. For example, the authors in [13] utilized UAVs to form a virtual antenna array as a jammer to send jamming signals to an illegitimate vessel, thus protecting legitimate data signals against being eavesdropped. The authors in [14] introduced a cooperative jamming scheme for UAV-assisted networks to enhance security by regulating the position of UAVs. However, the aforementioned works overlook the mobility of vessels, which is a crucial factor for maintaining reliable connectivity in practical scenarios [15]. In such dynamic conditions, the original solutions become ineffective, as vessel movement degrades previously stable links. Moreover, continuous real-time computation during the operation creates computational overhead that affects the responsiveness of the system. Therefore, to achieve the LEO satellite-maritime PLS communication system via UAVs, we need to focus on the movement of vessels and the temporal dynamics of maritime channels.

Implementing such systems encounters several challenges. First, the movements of vessels are dynamic as they traverse the ocean in varying directions, constantly changing their relative positions in communication networks. Similarly, LEO satellites experience rapid motion, continuously altering their positions relative to the vessels. In this case, traditional offline methods (e.g., convex optimization and evolutionary computation) become ineffective in such a dynamic condition [16], [17], while deep reinforcement learning (DRL) algorithms integrate the feature extraction capabilities of deep learning and the decisionmaking capabilities of reinforcement learning, demonstrating remarkable adaptability in dynamic environments [18], [19]. Second, when controlling UAVs for jamming, the potential impact on legitimate users needs to be considered to ensure their normal communications. As such, the transmit power of the UAV should be carefully optimized based on user requirements. Meanwhile, UAVs need to frequently adjust their positions to optimize system performance, which increases their energy consumption. Thus, secure communications and energy consumption are conflicting and require balancing. Additionally, since the relative importance of these objectives can change depending on the specific scenarios, existing methods (i.e., [20]) that prioritize one goal and constrain others become inapplicable for this case. Finally, our considered scenario is time-sensitive and involves large-scale decision making, which requires solutions that can adapt quickly while remaining computationally efficient, further increasing the complexity. Thus, an innovative approach, different from previous works, is needed to jointly optimize multiple conflicting objectives and efficiently respond to the dynamic maritime conditions.

Accordingly, we formulate a multi-objective optimization problem (MOP), and propose a generative AI (GenAI)-enabled DRL approach to solve the problem. The main contributions of this work are summarized as follows.

Low-altitude UAV Friendly-Jamming for the LEO Satellite-Maritime Communication System: We present an LEO satellite-maritime communication system assisted by lowaltitude UAV friendly-jamming, where an LEO satellite sends data signals to a legitimate vessel within range, and a UAV sends jamming signals to a potential eavesdropping vessel. This system is the first to holistically consider the movements of LEO satellites and vessels while designing an adaptive UAV friendly-jamming mechanism that ensures real-time maritime communication security.

Multi-objective Optimization Problem Formulation: The security performance and energy consumption of the system are in conflict due to shared decision variables. To balance these key performance metrics, we formulate a secure satellite-maritime communication multi-objective optimization problem (SSMCMOP) to jointly maximize the secrecy rate and minimize the energy consumption of the UAV. However, the problem is an NP-hard and long-term optimization problem, making it more complex to be solved.

GenAI-enabled DRL Approach: Conventional DRL algorithms confront the challenges of large solution spaces and strong temporal correlation when addressing the formulated SSMCMOP. In this case, we first reformulate the problem into a Markov decision process (MDP). We then propose a transformer-enhanced soft actor-critic (TransSAC) algorithm, which is a GenAI-enabled DRL approach to solve the problem. Specifically, the TransSAC algorithm captures temporal dependencies through encoded sequences and accelerates learning policies via parallel processing, while diversely exploring weights to effectively balance multiple optimization objectives.

Simulations and Performance: Simulation results indicate that the proposed UAV-assisted approach can achieve secure and energy-efficient LEO satellite-maritime communications, significantly outperforming the non-UAV approach. Moreover, comparative results illustrate that TransSAC outperforms other conventional DRL algorithms, achieving the maximum secrecy rate with the minimum energy consumption of the UAV. In addition, we identify optimal constraint values for the formulated MDP, thereby enhancing the performance of algorithms.

The rest of this paper is organized as follows: Section II reviews the related work. Section III introduces the models and preliminaries. Section IV formulates the SSMCMOP. The GenAI-enabled DRL approach is proposed in Section V. Section VI illustrates the simulation results. Section VII presents some discussions and Section VIII summarizes the overall work.

## II. RELATED WORK

In this section, we review the related works associated with LEO satellite maritime communications, security strategies, and optimization approaches.

## A. LEO Satellite-Maritime Communications

The rapid advancement of maritime wireless communications has attracted much attention, while deployment problems in practice pose a considerable challenge to transmission rates [21]. The satellites, with wide coverage capabilities, serve as valuable auxiliary equipment to facilitate the effective exchange of centralized data and information between vessels at sea [22]. For example, the authors in [23] proposed an energy-efficient multiaccess edge computing scheme for heterogeneous satellitemaritime networks to enhance the perception and offloading endurance of UAVs. Moreover, the authors in [24] proposed an intelligent spectrum-sharing scheme for the satellite-maritime integrated network to optimize throughput and spectral efficiency. However, the significant latency caused by long-distance satellite transmission can negatively impact the efficiency of communications.

LEO satellites, with their proximity to Earth, significantly reduce latency and improve data transmission efficiency. Moreover, LEO satellites can be deployed in satellite constellations to achieve seamless global coverage, allowing them to be gradually applied in maritime communications. For example, the authors in [25] proposed an LEO satellite-assisted shore-to-vessel network to achieve end-to-end communications. The authors in [26] considered a UAV-assisted LEO satellite communication network to provide coverage for low-end maritime users. Note that the open channels and extensive coverage of satellites make them susceptible to eavesdropping during data transmission. However, the aforementioned works focus mainly on communication efficiency, which ignores the potential security risks.

## B. Security Strategies

As aforementioned, it is essential to take measures to improve the security of maritime communications. As such, the authors in [27] presented analyses on cross-layer attacks and security measures in the satellite MCNs. In addition, the authors in [28] explored a secure and robust communication scheme by modeling the channel phase and angle uncertainties of geostationary Earth orbit and LEO. However, the encryption and decryption methods in the abovementioned works have limitations, as transmitting large amounts of data requires significant computational energy, resulting in transmission delays.

In this case, PLS can dynamically adapt security mechanisms according to the channel conditions, achieving secure transmissions for the maritime networks [12]. For example, the authors in [29] aimed to enhance the performance of the satellite-terrestrial MCN by optimizing the transmission beamforming of the base station and LEO satellites. However, for fast-moving LEO satellites, the immediate processing and regulating of beamforming parameters demand significant resources, increasing computational load. As such, low-altitude platforms are employed to introduce friendly jamming signals, which can significantly enhance PLS [13]. Common low-altitude platforms, such as eVTOL aircrafts and UAVs, play key roles in various applications [11]. Moreover, UAVs, with low cost, high mobility, and flexible deployment, are well-suited for implementing maritime PLS [12]. For example, the authors in [30] considered a power allocation scheme to optimize secrecy throughput to improve the PLS of downlink transmission. In addition, the authors in [31] presented a reinforcement learning-enabled UAV maritime communication relay strategy with a dueling structure to resist jamming attacks. However, the aforementioned works overlook the complex trade-offs between conflicting objectives such as security performance and energy efficiency, as well as the varying importance of these objectives across different scenarios, which often leads to suboptimal solutions.

## C. Optimization Approaches

To address these challenges, MOP provides a mathematical framework for optimizing multiple conflicting objectives simultaneously [32]. By formulating an MOP, we can model the correlations between conflicting objectives and find solutions that offer a better compromise across varying conditions. Generally, several common methods exist for handling MOP. First, swarm intelligence optimization algorithms can solve MOP, which gradually approximates the Pareto front and obtains multiple non-dominated solutions [33]. For example, the authors in [13] proposed a collaborative beamforming method to resist eavesdropping via UAVs, and presented a swarm intelligence algorithm to address MOP. Moreover, the authors in [34] considered a UAV-assisted communication scenario where eavesdroppers aim to intercept the data, and proposed a multi-objective salp swarm algorithm to deal with the MOP. However, swarm intelligence algorithms lack dynamic adjustment and timely feedback mechanisms, which affects overall performance and is not applicable to real-time problems.

Furthermore, DRL has adaptive learning capabilities and can handle complex action spaces, making it suitable for solving dynamic timing problems [35]. For example, the authors in [36] considered a dual-UAV secure maritime communication system that maximizes the minimum secrecy rate for the mobile user over all time slots. Moreover, the authors in [37] considered a UAV reconfigurable intelligent surface-assisted maritime communication system to maximize energy efficiency and ensure the quality of requirements against jamming attacks. However, the aforementioned works overlook crucial challenges such as the local optimal problem in the long-term optimization process, computational burden in large-scale action spaces, and suboptimal solutions due to improper weight value settings.

In summary, different from previous works, we employ lowaltitude UAV friendly-jamming for LEO satellite-maritime communications and propose a novel GenAI-enabled DRL approach that can derive a high-quality policy for resolving dynamic SSMCMOP. This approach is more suitable for dynamic scenarios requiring trade-offs between conflicting objectives while enabling fast response to changing conditions.

TABLE I MAIN NOTATIONS
<table><tr><td>Notation</td><td>Definition</td></tr><tr><td></td><td>Notation in the system model</td></tr><tr><td>ω</td><td>Argument of periapsis</td></tr><tr><td> $\varsigma$ </td><td>Rician fading</td></tr><tr><td> $\rho$ </td><td>Air density</td></tr><tr><td> $a _ { r }$ </td><td>Rotor disk area</td></tr><tr><td> $d _ { U , V }$ </td><td>Distance between the UAV and vessel</td></tr><tr><td> $d _ { S , V }$ </td><td>Distance between the LEO satellite and vessel</td></tr><tr><td> $F _ { s }$ </td><td>Rician factor</td></tr><tr><td> $h _ { U , V }$ </td><td>Channel of the UAV to vessel</td></tr><tr><td> $h _ { S , V }$ </td><td>Channel of the LEO Satellite to vessel</td></tr><tr><td> $I _ { 0 }$ </td><td>Maximum value of allowable interference power</td></tr><tr><td> $P _ { B }$ </td><td>Blade profile power</td></tr><tr><td> $P _ { I }$ </td><td>Induced power</td></tr><tr><td> $P L _ { U , V }$ </td><td>Path loss between the UAV and vessel</td></tr><tr><td> $P L _ { S , V }$ </td><td>Path loss between the LEO satellite and vessel</td></tr><tr><td> $r _ { a }$ </td><td>Airframe drag ratio</td></tr><tr><td> $s _ { r }$ </td><td>Rotor robustness</td></tr><tr><td> $v _ { f }$ </td><td>Forward direction velocity of the UAV</td></tr><tr><td> $v _ { i }$ </td><td>Average rotor induced velocity</td></tr><tr><td> $v _ { h }$ </td><td>Horizontal direction velocity of the UAV</td></tr><tr><td> $\boldsymbol { v } _ { t i p }$ </td><td>Rotor blade tip velocity</td></tr><tr><td> $v _ { v }$ </td><td>Vertical direction velocity of the UAV</td></tr><tr><td></td><td>Notation in the algorithm</td></tr><tr><td> $\tau _ { m }$ </td><td>Weights for the optimization objective m</td></tr><tr><td> $\alpha$ </td><td>Temperature parameter of SAC</td></tr><tr><td> $\mathcal { D }$ </td><td>Replay buffer</td></tr><tr><td> $\mathcal { A }$ </td><td>Action set</td></tr><tr><td> $J _ { m } ( \pi )$ </td><td>The expected return for the optimization objective m</td></tr><tr><td> $\kappa$ </td><td>Key matrix</td></tr><tr><td> $N ( a )$ </td><td>Number of arms of MAB</td></tr><tr><td> $Q$ </td><td>Query matrix</td></tr><tr><td> $Q _ { m } ^ { \theta }$ </td><td>Q estimated value for the optimization objective m</td></tr><tr><td> ${ \mathcal { R } } _ { m }$ </td><td>Reward for the optimization objective m</td></tr><tr><td> $\boldsymbol { s }$ </td><td>State set</td></tr><tr><td> $V$ </td><td>Value matrix</td></tr><tr><td> $V _ { m } ^ { \psi }$ </td><td>State-value for the optimization objective m</td></tr><tr><td> $V _ { m } ^ { \psi }$ </td><td>Target state-value for the optimization objective m</td></tr></table>

## III. MODELS AND PRELIMINARIES

In this section, we first present the LEO satellite-maritime communication system assisted by a low-altitude UAV. Then, we introduce the LEO satellite orbit model and vessel movement model. Next, the corresponding communication network is presented. Finally, the energy consumption model of the UAV is presented. In addition, the main notations are shown in Table I.

## A. System Overview

As shown in Fig. 1, we consider an LEO satellite-maritime communication system assisted by a low-altitude UAV, which involves an LEO satellite, a UAV, a legitimate vessel denoted as Alice, and an illegitimate user denoted as Eve. Among them, the LEO satellite receives information from the data fusion center and forwards it to the target vessel Bob within range. Note that the LEO satellite is equipped with high-performance antennas with adequate power, which can ensure efficient downlink communication to the vessels. However, its open channel is vulnerable to eavesdropping by Eve. In this case, due to the dynamics of the marine channels and constraints of marine routes, it is challenging to combat the eavesdropping attack with existing vessels. Moreover, the offshore evaporation ducts and multipath scattering increase the complexity of vesselaided methods. Therefore, we mainly focus on the low-altitude friendly-jamming platforms to deal with eavesdropping attacks. Among the platforms, UAVs, with great mobility, high flexibility, and wide coverage, are particularly suited for implementing secure maritime communications [38].

![](images/1e2b7d5a2bdfbc544f2811d30dfc17f9460b872e32d233ab42d0238a31d8ffff.jpg)  
Fig. 1. An LEO satellite-maritime communication system assisted by lowaltitude UAV.

Without loss of generality, we take into account a discretetime system that operates in a finite time T $\mathbf { \bar { \Psi } } , \mathcal { T } = \{ 1 , 2 , \dots , T \}$ The LEO satellite follows its fixed orbit, and the vessels (Alice and Eve) navigate on their predetermined trajectories. In this case, the LEO satellite sends signals to Alice over a legitimate link, whereas Eve aims to eavesdrop on the data content by the eavesdropping link. To enhance the reliability of the LEO satellite communications, the UAV sends jamming signals to Eve. Moreover, the UAV is configured with a single omni-directional antenna and optical camera, which can sense and detect the position of the eavesdropping vessel when the vessel temporarily regulates position and direction.

During the process of satellite-maritime communications, we utilize the 3D Cartesian coordinate system to indicate the time-varying positions of Alice, Eve, the UAV, and the LEO satellite at time slot t as $( x _ { A } [ t ] , y _ { A } [ t ] , z _ { A } [ t ] ) , ( x _ { E } [ t ] , y _ { E } [ t ] , z _ { E } [ t ] )$ $( x _ { U } [ t ] , y _ { U } [ t ] , z _ { U } [ t ] )$ , and $( x _ { S } [ t ] , y _ { S } [ t ] , z _ { S } [ t ] )$ , respectively. The satellite spectrum resources are limited and UAV needs to share spectrum with satellites, which complicates the dynamic communications [39]. To this end, we model the LEO satellite orbit and the vessel movement, as well as the communication processes of the LEO satellite and vessels, the UAV and vessels, to express the dynamics of the system.

## B. LEO Satellite Orbit Model

LEO satellites orbit at altitudes ranging from about 500 to 2,000 kilometers above the surface of Earth [40]. Since the orbital altitudes are relatively low, LEO satellites are characterized by fast orbital speeds, usually circling the Earth every 90 to 120 minutes [5]. Mathematically, the motion of the LEO satellite is usually described by the Keplerian six elements $\langle \beta , \omega , \Omega , e , a , \vartheta \rangle$ [40], as shown in the orbit model in Fig. 2, which is introduced in detail as follows.

\- Inclination Angle (β): It is the intersection angle between the orbital plane of the LEO satellite and the equatorial plane. Specifically, the satellite is moving in the opposite direction of rotation of the Earth if β is more than 90<sup>◦</sup>.

![](images/ff2d16e0994a9d8c6e6dbf9e10a91ff03818936ffc1c6b2665edee85b9cd0856.jpg)  
Fig. 2. LEO satellite orbit model.

![](images/bfcd3c52a17b7fc8da36c39d42b811322e69c83601161585b5f95fc87ae8289c.jpg)  
Fig. 3. Vessel coordinate systems.

\- Argument of Periapsis (ω): It denotes the angle between the direction of the LEO satellite and intersections of the orbital and equatorial planes.

\- Right Ascension of Ascending Node (Ω): It denotes the angle between the vernal equinox and intersections of the orbital and equatorial planes.

\- Eccentricity (e): It is the eccentricity of the orbital ellipse.

\- Semi-Major Axis (a): It is the distance from the center of the track to the furthest point on the edge of the track.

\- True Anomaly (ϑ): It is the angle between the satellite direction and perigee direction.

We consider that the LEO satellite orbit is circular [40]. In this case, e and ϑ are set to 0, and a is equal to the orbital radius $l _ { S }$ . Accordingly, the elements of the LEO satellite in m orbit at t time can be set as $\langle \beta _ { m } , \omega _ { m } [ t ] , \Omega _ { m } , l _ { S m } \rangle$ , wherein $\omega _ { m } [ t ] = \omega _ { m } [ t ] + 2 \pi ( ( t / T _ { S m } )$ mod 1) and $\mathcal { T } _ { S m }$ denotes the orbital period of the LEO satellite. Moreover, $l _ { S m } = H _ { S m } +$ $R _ { E }$ , where $H _ { S m }$ and $R _ { E }$ are the orbital altitude of the LEO satellite and the radius of Earth, respectively. In this case, the orientation of the LEO satellite in the 3D Cartesian coordinates $( x _ { S m } [ t ] , y _ { S m } [ t ] , z _ { S m } [ t ] )$ at time slot t is expressed by

$$
\begin{array} { r l } & { \left( \begin{array} { l } { x _ { S m } [ t ] } \\ { y _ { S m } [ t ] } \\ { z _ { S m } [ t ] } \end{array} \right) } \\ & { = l _ { S m } \left( \begin{array} { l } { \cos \omega _ { m } [ t ] \cos \Omega _ { m } - \sin \omega _ { m } [ t ] \cos \beta _ { m } \sin \Omega _ { m } } \\ { \cos \omega _ { m } [ t ] \sin \Omega _ { m } + \sin \omega _ { m } [ t ] \cos \beta _ { m } \cos \Omega _ { m } } \\ { \sin \omega _ { m } [ t ] \sin \beta _ { m } } \end{array} \right) . } \end{array}\tag{1}
$$

## C. Vessel Movement Model

As shown in Fig. 3, two three-dimensional right-handed Cartesian coordinate systems of a vessel are generally used to represent movement of the vessel [41]. Specifically, one is a general coordinate system $\{ g \}$ in which the origin is on the surface of the sea, and the defined $x , y ,$ and z axes are pointing the north, east, and down, respectively. The other is a fixed coordinate system $\{ f \}$ in which the origin is the gravity of the vessel, with $x ^ { f } , y ^ { f }$ , and $z ^ { f }$ pointing to the bow, starboard, and down, respectively. The rotations around the $x ^ { f } , y ^ { f }$ , and $z ^ { f }$ axes are defined as roll $( \phi ) .$ , pitch $( \theta ) .$ , and yaw $( \psi ) .$ , respectively. Moreover, the Euler angle vector is denoted as $\Theta = [ \bar { \phi } , \theta , \psi ] ^ { \bar { T } }$ Mathematically, the six degree-of-freedom (DOF) vessel model $\langle x , y , z , \phi , \theta , \psi \rangle$ is used to represent movement of a vessel, which is as follows:

$$
\dot { \pmb { \eta } } [ t ] = \mathbf { \Gamma } \mathbf { \Gamma } ( \pmb { \Theta } [ t ] ) \pmb { \nu } [ t ] ,\tag{2}
$$

where $\pmb { \eta } [ t ] = [ x [ t ] , y [ t ] , z [ t ] , \phi [ t ] , \theta [ t ] , \psi [ t ] ] ^ { T }$ indicates the displacement and rotation vector at time slot t, and $\nu [ t ] =$ $\bar { [ } u [ t ] , v [ t ] , w [ t ] , p [ t ] , q [ t ] , r [ t ] ] ^ { T }$ is the vector of translational and rotational velocities at time slot t. Moreover, ˙ [t] denotes the <sup>η</sup>first derivative of , and Γ denotes the horizontal plane rotation matrix from $\{ f \}$ <sup>η</sup>to $\{ g \}$ . Moreover, the velocity vector is often related to the corresponding forces caused by the wind, waves, propulsion, and inertia factors, and it is calculated by

$$
\begin{array} { r l } & { \left( M _ { R } + M _ { A } \right) \dot { \nu } [ t ] + C ( \nu [ t ] ) \nu [ t ] + D ( \nu [ t ] ) \nu + g ( \eta ) } \\ & { \quad = \tau _ { \mathrm { t h } } [ t ] + \tau _ { \mathrm { w i n d } } + \tau _ { \mathrm { c u r } } + \tau _ { \mathrm { w a v e } } , } \end{array}\tag{3}
$$

where $M _ { R } , M _ { A } , C ( \nu )$ , and $D ( \nu )$ denote the matrices of the rigid-body mass, added mass, Coriolis, and damping coefficient, respectively. Moreover, ${ \dot { \nu } } [ t ]$ denotes the first derivative of $\nu ,$ $g ( \eta )$ denotes the resilience, $\tau _ { \mathrm { t h } } [ t ]$ is the vessel thrusters vector at time slot $t , \tau _ { \mathrm { w i n d } } , \tau _ { \mathrm { c u r } }$ , and $\tau _ { \mathrm { w a v e } }$ indicate vectors of force on the vessel arising from wind, current, and wave, respectively.

The relative positions of the vessel and LEO satellite affect the satellite-vessel signal transmission, and the relative positions of the vessel and the UAV determine the quality of jamming signal transmission. Next, we describe the corresponding communication model in detail.

## D. Communication Model

In the designed system, our concerned communication links include the LEO satellite-to-vessel (S2V) link and UAV-tovessel (U2V) link. Specifically, the S2V link is employed for transmitting data signals, which are at risk of being eavesdropped by Eve. Moreover, the U2V link is utilized to jam Eve, which may interfere with the effective data reception of Alice. The two communication links are elaborated in detail below.

1) S2V Link From LEO Satellite: During the S2V link, we consider that the vessels can detect the signals from the LEO satellite by using the approach in [27], thus obtaining the quantized form of the actual channel state information (CSI). In this case, since the altitude of the LEO satellite is sufficient for line-of-sight (LoS) transmission [42], we employ a typical composite channel to represent the communications from the LEO satellite to vessels. The channel of the S2V link at time slot t can be expressed by [39]

$$
h _ { S , V } [ t ] = \sqrt { P L _ { S , V } [ t ] } \left( \sqrt { \frac { F _ { S } } { 1 + F _ { S } } } + \sqrt { \frac { 1 } { 1 + F _ { S } } } M _ { S , V } [ t ] \right) ,\tag{4}
$$

where $F _ { S }$ denotes the Rician factor, and $M _ { S , V } [ t ] \in \mathcal { C N } ( 0 , 1 )$ Moreover, the path loss $P L _ { S , V } [ t ]$ between the LEO satellite and vessel is defined by

$$
P L _ { S , V } [ t ] ( d B ) = C _ { S } + 1 0 W _ { S } \log 1 0 \left( d _ { S , V } [ t ] \right) + \delta _ { S , V } [ t ] ,\tag{5}
$$

where $C _ { S }$ and $W _ { S }$ are the path loss parameter and exponent, respectively. Moreover, $d _ { S , V } [ t ]$ is the distance between the LEO satellite and vessel (Alice or Eve) at time slot t, which is computed by the 3D positions of the LEO satellite and vessel according to (1) and (2), respectively. In addition, $\delta _ { S , V } [ t ]$ is the zero-mean Gaussian random variable with standard deviation $\sigma _ { X _ { S } }$ [43], [44]. Note that $d _ { S , A } [ t ]$ and $d _ { S , E } [ t ]$ are the distance from the LEO satellite to Alice and Eve at time slot t, respectively, which are used to calculate corresponding path loss $( P L _ { S , A } [ t ]$ and $P L _ { S , E } [ t ] )$ , and get the matching channels $( h _ { { S } , A } [ t ]$ and $h _ { S , E } [ t ] )$ .

2) U2V Link From UAV: In the considered system, the antenna on the UAV is notably higher than that of the vessel. Thus, the path loss of jamming signals between the UAV and the vessel at time slot t is calculated as follows:

$$
P L _ { U , V } [ t ] ( d B ) = C _ { U } + 1 0 W _ { U } \log 1 0 \left( \frac { d _ { U , V } [ t ] } { d _ { c } } \right) + \delta _ { U , V } [ t ] ,\tag{6}
$$

where $d _ { U , V } [ t ]$ denotes the distance from the UAV to vessel (Alice or Eve) at time slot t, which is computed based on the movements of the UAV and vessel. Moreover, $C _ { U }$ denotes the path loss parameter, $d _ { c }$ denotes the reference distance, $W _ { U }$ and $\delta _ { U , V } [ t ]$ are the path loss parameter and zero-mean Gaussian random variable with $\sigma _ { X _ { U } }$ , respectively [45]. Note that $P L _ { U , A } [ t ]$ and $P L _ { U , E } [ t ]$ denote the path loss from the UAV to Alice and Eve at time slot t, respectively, which are obtained by the distance from the UAV to Alice and Eve $( d _ { U , A } [ t ]$ and $d _ { U , E } [ t ] )$ , respectively.

On the basis of the path loss between the UAV and vessel, the U2V link channel at time slot t is indicated by

$$
h _ { U , V } [ t ] = \frac { \varsigma [ t ] ^ { 2 } } { P L _ { U , V } [ t ] } ,\tag{7}
$$

where $\varsigma [ t ]$ is the Rician fading at time slot t. Moreover, $h _ { U , A } [ t ]$ and $h _ { U , E } [ t ]$ are used to represent the channels from the UAV to Alice and Eve at time slot t, respectively.

According to the S2V link and U2V link, the achieved transmission rate of Alice at time slot t is denoted by

$$
R _ { A } [ t ] = \log _ { 2 } \left( 1 + \frac { P _ { S } G _ { S } G _ { S , S } \left| h _ { S , A } [ t ] \right| ^ { 2 } } { P _ { U } [ t ] G _ { U } h _ { U , A } [ t ] + \sigma ^ { 2 } } \right) ,\tag{8}
$$

where $P _ { S }$ is the transmit power of the LEO satellite, $G _ { S }$ and $G _ { U }$ denote the antenna gains of the satellite and UAV, respectively. Moreover, $G _ { S , S }$ is the antenna gain of the vessel served by the LEO satellite, $P _ { U } [ t ]$ denotes the transmit power of the UAV at time slot t, and $\sigma ^ { 2 }$ denotes the maritime additive white Gaussian noise power.

Furthermore, the reachable transmission rate of Eve at time slot t is denoted by

$$
R _ { E } [ t ] = \log _ { 2 } \left( 1 + \frac { P _ { S } G _ { S } G _ { S , S } \left. { h _ { S , E } } [ t ] \right. ^ { 2 } } { P _ { U } [ t ] G _ { U } G _ { U , E } h _ { U , E } \left. t \right. + \sigma ^ { 2 } } \right) ,\tag{9}
$$

where $G _ { U , E }$ denotes the antenna gain of Eve served by the UAV, as the UAV acts as a jammer mainly towards the eavesdropper Eve.

Thereby, with $R _ { A } [ t ]$ and $R _ { E } [ t ]$ , the secrecy rate from the LEO satellite to Alice at time slot t is expressed by

$$
R _ { S E C } [ t ] = [ R _ { A } [ t ] - R _ { E } [ t ] ] ^ { + } ,\tag{10}
$$

where $[ \chi ] ^ { + }$ indicates the value at which the larger of 0 and $\chi .$

From the aforementioned discussion, the 3D position and transmit power of the UAV are critical parameters for regulating the communication network. Note that the position of the UAV changes continuously over $\tau$ time slots, resulting in inevitable energy consumption. Therefore, the following section details the UAV energy consumption model.

## E. UAV Energy Consumption Model

We consider that in each time slot, the UAV performs action $\mathbf { a } ^ { U } [ t ] = ( a _ { x } ^ { U } [ t ] , a _ { y } ^ { U } [ t ] , a _ { z } ^ { U } [ t ] )$ to move. Thereby, at time slot t, the positional regulation of the UAV can be determined by the action $\mathbf { a } ^ { U } [ t ]$ , which can be expressed as $( x _ { U } [ t ] , y _ { U } [ t ] , z _ { U } [ { \dot { t } } ] ) =$ $( x _ { U } [ t - 1 ] , \dot { y } _ { U } [ t - 1 ] , z _ { U } [ t - \mathbf { \dot { 1 } } ] ) + \mathbf { a } ^ { U } [ t ]$

Furthermore, we introduce the moving UAV energy consumption. Commonly, the total energy consumption of a UAV is composed of communication energy and propulsion energy. However, the communication energy is usually ignored during the calculation because its value is extremely small compared to propulsion energy [46]. Thus, the propulsion power consumption of the UAV in 2D horizontal state is calculated by [46]

$$
P _ { p } ( v _ { h } [ t ] ) = P _ { I } \left[ \sqrt { 1 + \left( \frac { v _ { h } ^ { 2 } [ t ] } { 2 v _ { i } ^ { 2 } } \right) ^ { 2 } } - \left( \frac { v _ { h } [ t ] } { \sqrt { 2 } v _ { i } } \right) ^ { 2 } \right] ^ { \frac { 1 } { 2 } }
$$

$$
+ P _ { B } \left[ 1 + \left( \frac { \sqrt { 3 } v _ { h } [ t ] } { v _ { t i p } } \right) ^ { 2 } \right] + \frac { 1 } { 2 } r _ { a } s _ { r } a _ { r } \rho v _ { h } [ t ] ^ { 3 } ,\tag{11}
$$

where $v _ { h } [ t ] = \sqrt { ( a _ { x } ^ { U } [ t ] ) ^ { 2 } + ( a _ { y } ^ { U } [ t ] ) ^ { 2 } / \Delta t }$ is the horizontal direction velocity of the UAV, $P _ { I }$ and $P _ { B }$ are the induced power and blade profile power, respectively, $v _ { t i p }$ and $v _ { i }$ are the rotor blade tip velocity and average rotor induced velocity, respectively. Moreover, $r _ { a } , s _ { r } , a _ { r } ,$ and ρ denote the airframe drag ratio, rotor robustness, rotor disk area, and air density, respectively.

Note that we exclude the energy consumed by the UAV accelerating or decelerating, since this process occupies only a minor fraction of the total UAV flight time [47]. Therefore, we use a heuristic closed approximation to express the 3D energy consumption of the UAV, where the considerations include the propulsive energy, kinetic energy, and gravitational energy during the ascent and descent of the UAV over time. The 3D trajectory energy consumption of the UAV is denoted by

$$
\begin{array} { l } { { E _ { U } ( T ) \approx \displaystyle \int _ { 0 } ^ { T } P _ { p } \left( v _ { h } [ t ] \right) d t + \frac { 1 } { 2 } m _ { U } \left( v _ { f } [ T ] ^ { 2 } - v [ 0 ] ^ { 2 } \right) } } \\ { { \ ~ + m _ { U } g \left( h [ T ] - h [ 0 ] \right) , } } \end{array}\tag{12}
$$

where $v _ { f } [ t ] = \sqrt { ( v _ { h } [ t ] ) ^ { 2 } + ( v _ { v } [ t ] ) ^ { 2 } }$ is the UAV forward direction velocity at time slot t, of which $v _ { v } [ t ] = | a _ { z } ^ { U } [ t ] | / \Delta t$ denotes the vertical direction velocity of the UAV. Moreover, $h [ 0 ]$ and $h [ T ]$ are the UAV flight altitudes at start time and end time, respectively, $m _ { U }$ and $g$ denote the mass and gravitational acceleration of the UAV, respectively.

## IV. PROBLEM FORMULATION AND ANALYSES

In this section, we first state the optimization problem, and then analyze the problem.

## A. Problem Statement

In the considered scenario, the trajectories of the LEO satellites and vessels are not controllable. Specifically, the vessels sail along specific routes dictated by engines and perform tasks such as sensing and data collection. Moreover, the LEO satellites operate in particular orbits, and their movements are governed by orbital mechanics. The altitude and inclination of the orbit of the satellite are precisely designed to achieve a specific observation or communication mission.

In this case, this work utilizes the UAV to transmit jamming noise to Eve to resist eavesdropping, thereby enabling secure communications from the LEO satellite to Alice. Due to the spectrum scarcity problem, the UAV and the LEO satellite share the spectrum [39]. The jamming link between the UAV and Eve may interfere with Alice. To address this, we need to regulate the jamming signals transmitted by the UAV, improving its effect on Eve while minimizing the interference on Alice. Therefore, we focus on maximizing the secrecy rate as shown in (10), which can be controlled by the 3D position and transmit power of the UAV. Note that regulations in the 3D position inevitably result in additional energy consumption of the UAV. Therefore, minimizing the positional regulations of the UAV is essential to enhance overall energy efficiency.

Combining the aforementioned factors, the decision variables to be jointly optimized are the following UAV-related parameters: $( i ) \mathbb { L } = \{ \mathbb { X } , \mathbb { Y } , \mathbb { Z } \}$ denotes the 3D location set of the UAV over T time slots, where $\mathbb { X } = \{ x _ { U } [ t ] \} _ { t = 0 } ^ { T } , \mathbb { Y } = \{ y _ { U } [ t ] \} _ { t = 0 } ^ { T }$ , and $\mathbb { Z } = \{ z _ { U } [ t ] \} _ { t = 0 } ^ { T } . ( i i ) \mathbb { P } = \{ P _ { U } [ t ] \} _ { t = 0 } ^ { T }$ is the transmit power of the UAV over T time slots.

## B. Problem Formulation

In the LEO satellite-maritime communication system assisted by a low-altitude UAV, we contemplate the following two optimization objectives.

Optimization Objective 1: To achieve secure LEO satellitemaritime communications, the first optimization objective is to maximize the average secrecy rate over $\tau$ time slots by regulating the 3D position and transmit power of the UAV, which is expressed by

$$
f _ { 1 } ( \mathbb { L } , \mathbb { P } ) = \frac { 1 } { T } \sum _ { t = 0 } ^ { T } R _ { S E C } [ t ] .\tag{13}
$$

Optimization Objective 2: In the process of accomplishing the first optimization objective, the UAV needs to constantly adjust the position, increasing energy consumption. Given the

limited energy supply at sea, the second optimization objective is to minimize the average energy consumption of the UAV over $\tau$ time slots, which is expressed by

$$
f _ { 2 } ( \mathbb { L } ) = \frac { 1 } { T } \sum _ { t = 0 } ^ { T } E _ { U } [ t ] ,\tag{14}
$$

where $E _ { U } [ t ]$ denotes the energy consumption of the UAV at time slot t.

Maximizing the average secrecy rate requires regulating the position of the UAV, which conflicts with minimizing the average energy consumption of the UAV. Moreover, according to (11), higher UAV speeds lead to increased energy consumption. Conversely, as the UAV slows down, communication time increases, leading to higher hovering energy consumption. Consequently, the two optimization objectives are in conflict, requiring a suitable modeling method to balance this conflicting relationship. In this case, the multi-objective optimization problem modeling provides a mathematical framework that simultaneously optimizes multiple conflicting objectives, which is well-suited for capturing trade-offs of conflicting metrics and can be used to formulate our optimization problem [32].

According to the aforementioned optimization objectives, we formulate the SSMCMOP as follows:

$$
\operatorname* { m i n } _ { \{ \mathbb { L } , \mathbb { P } \} } F = \left\{ - f _ { 1 } , f _ { 2 } \right\} ,\tag{15a}
$$

$$
\mathrm { s . t . } C 1 : x _ { m i n } \leq x _ { U } [ t ] \leq x _ { m a x } , \forall t \in \mathcal { T } ,
$$

$$
C 2 : y _ { m i n } \leq y _ { U } [ t ] \leq y _ { m a x } , \forall t \in T ,\tag{15b}
$$

$$
C 3 : z _ { m i n } \leq z _ { U } [ t ] \leq z _ { m a x } , \forall t \in \mathcal { T } ,\tag{15c}
$$

(15d)

$$
C 4 : P _ { m i n } \leq P _ { U } [ t ] \leq P _ { m a x } , \forall t \in { \cal T } ,\tag{15e}
$$

$$
\begin{array} { r } { C 5 : \sum _ { t = 0 } ^ { T } P _ { U } [ t ] \Delta t \leq E _ { 0 } , \forall t \in { \cal T } , } \end{array}\tag{15f}
$$

$$
C 6 : { \cal P } _ { U } [ t ] { \cal G } _ { U } h _ { U , A } [ t ] \leq I _ { 0 } , \forall t \in { \cal T } ,\tag{15g}
$$

$$
C 7 : { \mathit { P } } _ { U } [ t ] { \mathit { G } } _ { U } { \mathit { G } } _ { U , E } h _ { U , E } [ t ] \leq I _ { 0 } , \forall t \in { \mathcal { T } } ,\tag{15h}
$$

where C1 and C2 indicate the horizontal flight ranges of the UAV, C3 denotes the vertical flight height of the UAV, and C4 indicates the transmit power limitation of the UAV. Moreover, C5 denotes the energy consumption constraint, where $E _ { 0 }$ is the maximum allowable energy consumption of the UAV over $\tau$ time slots. In addition, C6 and C7 are the interference temperature limitations of the UAV, where $I _ { 0 }$ is the maximum allowable interference power to ensure that the interference does not excessively affect the communications of other legitimate devices.

## C. Problem Analyses

Subsequently, we present the corresponding analyses of the formulated SSMCMOP.

(i) The SSMCMOP is a dynamic and large-scale problem: In our considered scenario, both the LEO satellites and vessels move along the respective orbits, reflecting a realistic setup. In this case, the UAV needs to transmit jamming signals based on the position of the vessel, leading to a dynamic communication channel. At this point, the SSMCMOP involves two optimization objectives over T time slots, both of which change in real-time. In addition, the UAV has multiple variables (3D position and transmit power) to be optimized. Therefore, SSMCMOP is a dynamic and large-scale problem.

(ii) The SSMCMOP is with long-term optimization objectives: The changes of the LEO satellite, vessels, and UAV can lead to fluctuations in signal strength, which in turn affects the optimization objectives. Moreover, since we consider optimization objective values over $\tau$ time slots, an optimal solution at any specific moment may not necessarily represent the optimal solution over a longer time scale. Therefore, SSMCMOP involves long-term optimization objectives and requires balancing current objectives with long-term objectives.

(iii) The SSMCMOP is an NP-hard problem: To simplify the analysis, we only focus on the first optimization objective. Specifically, we fix the positions of vessels and the LEO satellite and set $P _ { U } [ t ]$ to discrete. In this case, the simplified SSMCMOP is expressed by

$$
\operatorname* { m i n } _ { \{ \mathbb { L } , \mathbb { P } \} } F = - f _ { 1 } ,\tag{16a}
$$

$$
{ \mathrm { s . t . } } \operatorname { E q s . } ( 1 5 { \mathrm { b } } ) - ( 1 5 { \mathrm { d } } ) , ( 1 5 { \mathrm { f } } ) - ( 1 5 { \mathrm { h } } ) ,\tag{16b}
$$

$$
P _ { U } [ t ] \in \{ 0 , P _ { m a x } \} , \forall t \in \mathcal { T } ,\tag{16c}
$$

$$
\begin{array} { r } { \sum _ { t = 0 } ^ { T } P _ { U } [ t ] < T P _ { m a x } , \forall t \in T . } \end{array}\tag{16d}
$$

Clearly, the simplified SSMCMOP is a classic nonlinear multidimensional 0-1 knapsack problem, which has been proved to be NP-hard [48]. Consequently, the original continuous SSM-CMOP is an NP-hard problem.

In summary, since the SSMCMOP presents significant challenges, traditional convex optimization methods and evolutionary computation methods struggle to address the dynamic problem [17]. In this case, the DRL algorithms can adaptively learn strategies through continuous environmental interaction in the online training phase, followed by offline execution where the trained model can quickly generate actions to respond to real-time changes [35]. Therefore, we employ a DRL-based algorithm to tackle the SSMCMOP.

## V. ALGORITHM

In this section, we first transform the SSMCMOP into an MDP, then introduce the process of conventional SAC. Next, considering the weaknesses of SAC for MDP, we propose a TransSAC algorithm to address these challenges.

## A. MDP Formulation

In the considered scenario, our main concern is ensuring the availability of trained DRL models. To this end, we transform the SSMCMOP into an MDP. Specifically, MDP is a mathematical framework used to model decision-making in an uncertain environment, defined by {S, A, P, R, γ} [49], which is introduced in detail as follows.

Each state $\mathbf { \boldsymbol { s } } [ t ] \in S$ describes the situation of the system at time slot t, given the current state $s [ t ]$ , and the agent can choose the action $\mathbf { \delta } \mathbf { \mathbf { } } a [ t ] \in \mathcal { A }$ . Moreover, $\mathscr { P } ( s [ t + 1 ] | s [ t ] , \mathbf { } a [ t ] )$ is the probability of reaching to state $s [ t + 1 ]$ <sup>s a</sup>after taking action $\mathbf { \delta } _ { \mathbf { { \boldsymbol { a } } } } [ t ]$ Then, the reward function ${ \bf R } = \{ \mathcal { R } _ { 1 } ( \pmb { s } [ t ] , \pmb { a } [ t ] ) , \mathcal { R } _ { 2 } ( \pmb { s } [ t ] , \pmb { a } [ t ] ) \}$ is used to evaluate the effectiveness of the decision by calculating the immediate reward for $\mathbf { \Delta } _  \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha \alpha } \mathbf { \alpha } \mathbf { \alpha \alpha } \mathbf { \alpha \alpha } \mathbf { \alpha \alpha } \mathbf { \alpha \alpha } \mathbf { \alpha \alpha } \mathbf { \alpha \alpha } \mathbf { \alpha \alpha } \mathbf { \alpha \alpha } \mathbf { \alpha \alpha } \mathbf { \alpha \alpha } \mathbf { \alpha \alpha } \mathbf { \alpha \alpha \alpha } \mathbf  \alpha \alpha \beta \alpha \alpha \beta \alpha \alpha \beta \alpha \beta \alpha \beta \alpha \alpha \beta \alpha \beta \alpha \beta \alpha \beta \alpha \beta \alpha \beta \alpha \beta \alpha \beta \alpha \beta \alpha \beta \alpha \beta \alpha \beta \alpha \beta \alpha \beta \alpha \alpha \beta \alpha \beta \alpha \beta \alpha \delta \alpha \delta \delta \delta \delta \delta \delta \alpha \delta \delta \delta \delta \delta \delta \delta \alpha \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta $ according to the optimization objectives. In addition, the discount factor $\gamma \in [ 0 , 1 )$ is utilized to weigh the relative importance of current and future rewards. MDP aims to determine a policy π that maximizes the expected cumulative reward. For the optimization objective $m _ { : }$ the expected return is defined by

$$
J _ { m } ( \pi ) = \frac { 1 } { T } \mathbf { E } \{ \sum _ { t = 0 } ^ { T } \gamma \mathcal { R } _ { m } ( s [ t ] , a [ t ] ) | s [ 0 ] = s , a [ 0 ] = a \} ,\tag{17}
$$

where $\mathbf { E } \{ \cdot \}$ is the expectation according to the policy $\pi .$ Moreover, the state space, action space, and reward function of SSMCMOP are introduced in detail as follows.

1) State Space: At each time slot, the agent focuses on relevant state information to make decisions. In this system, the agent (i.e., the UAV) is concerned with its own relevant information, and the positions of the LEO satellite and vessels. Since the UAV is equipped with a positioning device, and the locations of the vessels and LEO satellites can be computed based on their models given in Section III, obtaining the data is feasible. As such, the state of the system is expressed by

$$
\begin{array} { r } { S = \{ s [ t ] | s [ t ] = ( \eta _ { A } [ t ] , \nu _ { A } [ t ] , \eta _ { E } [ t ] , \nu _ { E } [ t ] , P _ { U } [ t ] , } \end{array}
$$

$$
( x _ { U } [ t ] , y _ { U } [ t ] , z _ { U } [ t ] ) , ( x _ { S m } [ t ] , y _ { S m } [ t ] , z _ { S m } [ t ] ) ) , \forall t \in \mathcal { T } \} ,\tag{18}
$$

where $\eta _ { A } [ t ]$ and $\nu _ { A } [ t ]$ are the position and velocity of Alice at time slot t, respectively. Moreover, $\eta _ { E } [ t ]$ and $\nu _ { E } [ t ]$ are the position and velocity of Eve at time slot t, respectively. Note that the current scenario includes a UAV with a single antenna, which limits the UAV to jam one illegitimate vessel at a time. Furthermore, our algorithm can be extended to scenarios with multiple UAVs, and the details are provided in Section VII.

2) Action Space: In the considered system, the UAV acts as an agent that can take actions based on the current state. Thus, the action space includes the 3D position and transmit power of the UAV, which is denoted by

$$
\begin{array} { r } { \mathcal { A } = \{ \pmb { a } [ t ] | \pmb { a } [ t ] = ( \mathbf { a } ^ { U } [ t ] , P _ { U } [ t ] ) , \forall t \in \mathcal { T } \} . } \end{array}\tag{19}
$$

3) Immediate Reward: The reward mechanism acts as a feedback signal to direct the agent in a series of actions and directly affects the quality of the final policy. Therefore, designing an effective reward method is critical to improve overall performance. Note that the constraints C1-C5 of the SSMCMOP are satisfied by setting the parameters of the UAV within the predetermined ranges. Moreover, the constraints C6 and $C 7$ are satisfied by incorporating them into the reward function as penalty items, and we further incorporate constraints C1, C2, and C3 into the reward function to ensure strict adherence to flight boundaries. In our work, the MDP employs a reward function in vector form, which is defined by

$$
\begin{array} { r l } & { { \bf R } = \{ \mathcal { R } _ { 1 } ( s [ t ] , a [ t ] ) , \mathcal { R } _ { 2 } ( s [ t ] , a [ t ] ) \} } \\ & { \quad = \left\{ \begin{array} { l l } { ( \mu _ { 1 } W _ { c } [ t ] R _ { S E C } [ t ] , - \mu _ { 2 } W _ { c } [ t ] E _ { U } [ t ] ) , } & { k [ t ] = 1 , } \\ { \left( \mu _ { 1 } \varrho _ { 1 } W _ { c } [ t ] R _ { S E C } [ t ] , - \mu _ { 2 } \varrho _ { 2 } W _ { c } [ t ] E _ { U } [ t ] \right) , } & { k [ t ] = 0 , } \end{array} \right. } \end{array}\tag{20}
$$

where $\mathcal { R } _ { 1 } [ t ]$ and $\mathcal { R } _ { 2 } [ t ]$ denote the scaled reward values of the optimization objectives $R _ { S E C } [ t ]$ and $E _ { U } [ t ]$ , respectively. Moreover, when the UAV moves within the defined range at time slot $t , k [ t ]$ is assigned to 1. Otherwise, $k [ t ]$ is assigned to 0. Moreover, the coefficients $\mu _ { 1 }$ and $\mu _ { 2 }$ are proportionality factors used to ensure that the rewards for both targets are on the same order of magnitude. Additionally, $\varrho _ { 1 }$ and $\varrho _ { 2 }$ are used to penalize when the UAV leaves the service area. Additionally, $W _ { c } [ t ] = W _ { 1 } [ t ] W _ { 2 } [ t ]$ represents the comprehensive penalty term of the constraints C6 and C7 of the SSMCMOP. Correspondingly, $W _ { 1 }$ and $W _ { 2 }$ represent the penalty items when the strength of the interference signals received by Alice and Eve affects the maritime communications, respectively.

Following this, we utilize the linear weighting approach to compute the overall expected return [50]. This approach offers low computational complexity and adjustable priority, making it well-suited for the SSMCMOP in resource-constrained dynamic maritime environments. The overall expected return is denoted by

$$
J ( \pi ) = \tau _ { 1 } J _ { 1 } ( \pi ) + \tau _ { 2 } J _ { 2 } ( \pi ) ,\tag{21}
$$

where $\tau _ { 1 }$ and $\tau _ { 2 }$ are the weights of the two optimization objectives, with $\tau _ { 1 } + \tau _ { 2 } = 1$

## B. Conventional SAC

Next, we discuss the advantages of SAC in dealing with MDP and describe the process in detail.

1) Advantages of SAC: General DRL approaches, such as the deep Q-network (DQN), are typically effective for discrete action space [51], whereas discretizing for continuous action space problems is not feasible. Moreover, trust region policy optimization (TRPO) can enhance policy stability by optimizing the trust region, while the computational complexity is higher [52]. In contrast, SAC is well-suited for continuous-time problems [53]. First, by incorporating maximum entropy theory, SAC promotes policy diversity, enabling better adaptation and exploration in complex environments and avoiding local optima. Second, the offline data update strategy further enhances sample efficiency through the iterative use of the replay buffer. Finally, SAC integrates the policy gradient approach with the Q-value function for policy updates, which improves both sample efficiency and training stability. Therefore, we select SAC as the framework for addressing the MDP.

2) Process of SAC: A crucial feature of SAC is the maximum entropy theory, which enhances policy randomness and improves the exploratory capability. The expected return, including the entropy term, is expressed by

$$
J _ { m } ( \pi ) = \frac { 1 } { T } \mathbf { E } \{ \sum _ { t = 0 } ^ { T } \gamma \left[ \mathcal { R } _ { m } \left( s [ t ] , \pmb { a } [ t ] \right) - \alpha \log \pi ( \pmb { a } [ t ] | s [ t ] ) \right] \} ,\tag{22}
$$

where log $\pi ( \mathbf { \boldsymbol { a } } [ t ] | \mathbf { \boldsymbol { s } } [ t ] )$ denotes the entropy of the policy $\pi ,$ <sup>a s</sup>which promotes explorability. Moreover, α is the temperature parameter to balance the reward and entropy [53].

Furthermore, the value $Q ^ { \theta }$ can evaluate the soft Q-value network which is parameterized by θ. To reduce the correlation between the input data, the outcome of each step is saved in the

replay buffer $\mathcal { D } ,$ and the network performance can be evaluated by using the mean square error (MSE) as follows:

$$
L _ { m } ( \theta ) = \mathbf { E } \left\{ \frac { 1 } { 2 } [ Q _ { m } ^ { \theta } \left( s [ t ] , a [ t ] \right) - \hat { Q } _ { m } \left( s [ t ] , a [ t ] \right) ] ^ { 2 } | \mathcal { D } \right\} ,\tag{23}
$$

where $Q _ { m } ^ { \theta } ( s [ t ] , \pmb { a } [ t ] )$ and $\hat { Q } _ { m } ( \pmb { s } [ t ] , \pmb { a } [ t ] )$ are the Q estimated value and Q target value for the optimization objective m at time slot $t ,$ respectively, and $\hat { Q } _ { m } ( s [ t ] , a [ t ] )$ is computed by

$$
\hat { Q } _ { m } \left( s [ t ] , a [ t ] \right) = \mathcal { R } _ { m } \left( s [ t ] , a [ t ] \right) + \gamma \mathbf { E } \{ V _ { m } ^ { \hat { \psi } } ( s [ t + 1 ] ) \} ,\tag{24}
$$

where $V _ { m } ^ { \hat { \psi } } ( s [ t + 1 ] )$ is the target state-value, which will be introduced later. To minimize the $L _ { m } ( \theta )$ , stochastic gradient $\nabla _ { \boldsymbol { \theta } } L _ { m } ( \boldsymbol { \theta } )$ is commonly used to optimize the parameter $\theta .$

To improve training stability, the state-value network $V _ { m } ^ { \psi }$ parameterized by $\psi$ is introduced. Similarly, we use MSE to evaluate network performance as follows:

$$
\begin{array} { l } { { \displaystyle { \cal L } _ { m } ( \psi ) = { \bf E } \{ \frac 1 2 ( V _ { m } ^ { \psi } ( s [ t ] )  } \ } \ ~  \\ { { \displaystyle ~  - { \bf \sigma } { \bf E } \{ Q _ { m } ^ { \theta } ( s [ t ] , a [ t ] ) - \alpha \log \pi _ { \Phi } ( a [ t ] | s [ t ] ) | \pi _ { \Phi } \} ) ^ { 2 } } \vert \mathcal { D } \} , } \end{array}\tag{25}
$$

where $V _ { m } ^ { \psi } ( s [ t ] )$ denotes the state-value for the optimization objective m at time slot t, and $\psi$ is updated by the stochastic gradient $\nabla _ { \psi } L _ { m } ( \psi )$ . Moreover, to stabilize the critic network update, the parameter $\hat { \psi }$ can estimate $V _ { m } ^ { \hat { \psi } } ( s [ t ] )$ by the soft <sup>s</sup>update. Furthermore, Φ indicates the policy network parameter, and the corresponding policy loss function is denoted by

$$
\begin{array} { l } { { { \cal L } ( \Phi ) = { \bf E } \left\{ \alpha \log \pi _ { \Phi } \left( f _ { \Phi } ( \epsilon [ t ] ; s [ t ] ) | s [ t ] \right) \right. } } \\ { { { \mathrm { } } } } \\ { { { \mathrm { } } - \left. \sum _ { m = 1 } ^ { 2 } \tau _ { m } Q _ { m } ^ { \theta } \left( s [ t ] , f _ { \Phi } ( \epsilon [ t ] ; s [ t ] ) \right) | \mathcal { D } , \mathcal { N } \right\} , } } \end{array}\tag{26}
$$

where $f _ { \Phi } ( \epsilon [ t ] ; s [ t ] )$ denotes a reparameterization trick, and  is the action noise sampled from a stationary distribution ${ \mathcal { N } } .$ Accordingly, Φ is updated by gradient descent $\nabla _ { \Phi } L ( \Phi )$

## C. The Proposed TransSAC Algorithm

1) Motivation of TransSAC Algorithm: While SAC has advantages in solving continuous-time problems, it still faces the following challenges.

(i) Strong Temporal Correlation: The vessels and LEO satellites are governed by constrained moving trajectories, and the UAV flight paths need to satisfy physical continuity constraints. These constraints make their current positions strictly limited by previous states, thereby causing the MDP to exhibit strong temporal correlation. At this point, conventional SAC primarily focuses on the current state and ignores the strong temporal correlation, which may result in ineffective decision-making. Note that this may cause policies to fall into local optima and further affect the performance of the optimization objectives.

(ii) Large-Scale State and Action Spaces: In the MDP, the UAV needs to process large state inputs and select action spaces. This results in the MDP having large-scale state and action spaces where multiple action dimensions need to be jointly optimized, resulting in combinatorial complexity. However, conventional SAC relies on trial-and-error learning to discover relevant patterns and optimize policies. As such, large-scale state and action spaces result in SAC requiring more training rounds to interact with the environment to discover effective policies, which reduces sampling efficiency.

![](images/7f0c0eeb7aca24726036ec81476cbf2fa5c9c7a86aae497d0b70bd8a0f1e86ca.jpg)  
Fig. 4. The framework of the proposed TransSAC algorithm for solving the SSMCMOP, where a transformer-enhanced learning strategy and an MAB-based weight optimization scheme are integrated into the network to capture global dependencies and explore weights diversely.

(iii) Preset Suboptimal Weights for Multiple Optimization Objectives: In the MDP, we aim to simultaneously optimize multiple objectives. Generally, conventional SAC uses fixed weights for each optimization objective, yet sensitive weight configurations may make it potentially difficult to adapt to the long-term dynamic problem. Moreover, improper weight configurations may lead to suboptimal performance. At this point, SAC may prioritize energy consumption over security, and vice versa. This makes it challenging to effectively balance the conflicting objectives when the preset weights are suboptimal.

Therefore, considering the aforementioned weaknesses of the conventional SAC, we propose a TransSAC algorithm, and Fig. 4 shows the framework of the proposed TransSAC algorithm for solving the SSMCMOP. Moreover, the overall structure is illustrated in Algorithm V-C2, and the corresponding improvements are introduced as follows.

2) Transformer-Enhanced Learning Strategy: The transformer, a key GenAI approach, employs the self-attention mechanism to compute the global correlation weights across temporal samples, so that it can establish comprehensive feature interactions between multiple states [54]. As such, by incorporating the transformer into standard DRL algorithms, we can enhance temporal modeling capabilities, allowing policy networks to explicitly capture long-term dependencies and sequential patterns. This process effectively addresses biases in locally correlated samples, thereby overcoming the challenge of local optima in conventional SAC. Furthermore, the transformer employs parallelized sequence processing to efficiently handle large-scale state and action spaces. Moreover, through multi-head attention mechanisms, the transformer can decompose high-dimensional actions and process different dimensions separately, improving the ability of the neural network to fit policy functions. Therefore, we use the transformer to process actions and states to improve the performance of the conventional SAC. Note that this approach does not conflict with the Markov property of the MDP, as the approach does not rely on complete historical information. Instead, the approach can enhance the representation of the current state and action, providing contextual information to optimize decision-making. The overall framework is presented in Algorithm V-C2, with the details as follows.

First, positional encoding is a key component used to give positional information for each element in the sequence [55]. In the MDP, positional encoding provides relative or absolute temporal positions for the inputs (states and actions), which can be denoted by [55]

$$
\mathcal { E } _ { 2 i } = \sin \left( \frac { P [ t ] } { \varpi ^ { 2 i / d _ { e } } } \right) ,\tag{27a}
$$

$$
\mathcal { E } _ { 2 i + 1 } = \cos \left( \frac { P [ t ] } { \varpi ^ { 2 i / d _ { e } } } \right) ,\tag{27b}
$$

where ${ \mathcal { E } } _ { 2 i }$ and $\mathcal { E } _ { 2 i + 1 }$ are the positional encoding of even and odd numbers, respectively. Moreover, $P [ t ]$ indicates the position of the inputs at time slot $t , \varpi$ is the related constant, and $d _ { e }$ is the embedding dimension of the model.

Second, the self-attention mechanism is a key for the transformer, which can capture global information by quantifying the relevance between each action and current state. This allows algorithms to efficiently evaluate the subsequent impact of decisions, thereby solving the challenge of local optima caused by strong temporal correlation. Accordingly, the self-attention mechanism is expressed by [55]

Algorithm 1: TransSAC Algorithm.   
Input: Number of iterations, batch size, smoothing   
parameter $\kappa ,$ and learning rates.   
1 Initialize the parameters with soft Q-value network   
$\theta ,$ policy network $\Phi ,$ , state-value network $\psi ,$ and   
target state-value network $\hat { \psi } ,$ and initialize replay   
buffer $\mathcal { D } ;$   
2 for each iteration do   
3 for each environment step do   
4 Obtain weights by Algorithm $3 ;$   
5 Select and execute action ${ \mathbf { } } _ { { \mathbf { } } } { \mathbf { } } _ { a \left[ t \right] , }$   
$\mathbf { \boldsymbol { a } } [ t ] \sim \pi _ { \Phi } ( \mathbf { \boldsymbol { a } } [ t ] | \mathbf { \boldsymbol { s } } [ t ] ) ;$   
6 Observe next state $s [ t + 1 ]$ and reward $R ;$   
7 Update replay buffer D,   
$\begin{array} { r } { \dot { \mathcal { D } } \gets \mathcal { D } \dot { \cup } ( s [ t ] , a [ t ] , \mathcal { R } _ { m } ( s [ t ] , a [ t ] ) , s [ t + 1 ] ) ; } \end{array}$   
8 Obtain enhanced states and actions by   
Algorithm 2;   
9 end   
10 for each gradient step do   
11 Calculate the MSE of the state-value network   
by Eq. (25) and update parameter ψ;   
12 Soft update the target state-value network;   
13 Calculate the Q target value $\hat { Q } _ { m }$ by Eq. (24);   
14 Compute the MSE of the soft Q-value   
network by Eq. (23) and update parameter $\theta ;$   
15 Calculate weighted policy network loss by   
Eq. (26) and update parameter $\Phi ;$   
16 end   
17 end   
Output: Trained model.

$$
\mathcal { M } _ { S A } ( Q , K , V ) = \mathcal { U } _ { s o f t m a x } \left( \frac { Q K ^ { T } } { \sqrt { d _ { K } } } \right) V ,\tag{28}
$$

where $\begin{array} { r } { Q = H W ^ { Q } , K = H W ^ { K } } \end{array}$ , and $\pmb { V } = \pmb { H } \pmb { W } ^ { V }$ denote the query, key, and value matrices, respectively, with $W ^ { Q } , W ^ { K }$ and $\dot { W } ^ { V }$ indicate the corresponding learnable weight matrices, and denotes the joint denotation of S and A. Moreover, $\mathcal { U } _ { s o f t m a x }$ is the normalization operation performed using the softmax function, and $d _ { K }$ denotes the dimension of the - matrix. Note that the parallelized sequence processing capability of the self-attention mechanism can comprehensively analyze entire state-action sequences, effectively avoiding random and ineffective explorations and greatly improving sample efficiency in the large action space.

Third, multi-head attention mechanism decomposes highdimensional actions into subspaces, enabling different attention heads to focus on different action dimensions. This approach can improve the fitting ability of the neural network, which is defined by

$$
\mathcal { M } _ { M S A } ( \boldsymbol { Q } , \boldsymbol { K } , \boldsymbol { V } ) = \mathcal { C } \left( \mathcal { H } _ { 1 } , \ldots , \mathcal { H } _ { h } \right) \boldsymbol { W } ^ { O } ,\tag{29a}
$$

Algorithm 2: Transformer-Enhanced Learning Strategy.   
Input: States and actions from D.   
1 Add positional encoding using (27a) and (27b);   
2 Perform a linear transformation of , , and $V ;$   
<sup>Q K V</sup>3 Calculate the attention values for all heads with the   
softmax function by (29b) and (28);   
4 Splice the output of all heads by (29a);   
5 Apply residual linking and layer normalization;   
6 Perform FFN with two linear layers by (30);   
Output: Enhanced states and actions representations.

$$
\mathcal { H } _ { i } = \mathcal { M } _ { S A } \left( \pmb { H } \pmb { W } _ { i } ^ { Q } , \pmb { H } \pmb { W } _ { i } ^ { K } , \pmb { H } \pmb { W } _ { i } ^ { V } \right) ,\tag{29b}
$$

where $\mathcal { H } _ { i }$ is the output of attention head i, C is the concat processing, and $W ^ { \boldsymbol { O } }$ is the output weight matrix. Moreover, the attention output for each $\mathcal { H }$ is computed independently and then linearly transformed through $W ^ { \dot { O } }$

Finally, the output after the self-attention layer is fed into a feed-forward neural (FFN), which performs an independent nonlinear transformation of the output at each time slot. As such, the FFN enhances the capability of the model to learn complex patterns, and the transformation is given by [55]

$$
\boldsymbol { \mathcal { M } } _ { F F N } ( \boldsymbol { x } ) = \left[ \boldsymbol { x } \boldsymbol { W } _ { 1 } + \boldsymbol { b } _ { 1 } \right] ^ { + } \boldsymbol { W } _ { 2 } + \boldsymbol { b } _ { 2 } ,\tag{30}
$$

where x denotes the input vector, and it is also the output obtained from the previous layer. Moreover, $W _ { 1 }$ and $W _ { 2 }$ denote the weight matrices of the first and second linear transformations, respectively, $b _ { 1 }$ and $b _ { 2 }$ are corresponding bias vectors.

In summary, the transformer-enhanced learning strategy can effectively address the challenge of strong temporal correlation through enhanced state and action representations while handling large-scale state and action spaces through parallelized processing. These capabilities make the transformer particularly well-suited for our large-scale and long-term optimization problem.

3) Multi-Armed Bandit (MAB)-Based Weight Optimization Scheme: Different from the preset weights, we employ an MABbased weight optimization scheme that dynamically explores weights during the multi-objective optimization process. The MDP is dynamic with long-term optimization objectives, and balancing the conflicting objectives is crucial and challenging. Moreover, fixed and preset weights may prioritize one objective over others, causing algorithms to converge to a local optimum over time. In this case, the MAB-based scheme continuously and diversely explores weights, allowing the algorithm to discover a broader solution space. Specifically, by using the ε-greedy strategy, MAB balances exploration and exploitation, reducing the risk of falling into local optima. In addition, MAB does not require complex models or enormous computational resources, enabling quick execution. This makes it well-suited for real-time optimization within the system. The general process is presented in Algorithm V-C3, and the details are introduced as follows.

In the MAB, each arm a represents a weight, MAB selects an arm and calculates the corresponding reward for estimating the arm. The updated rule of reward is defined by

```powershell
Algorithm 3: MAB-Based Weight Optimization Scheme.
1 Initialize the reward $\textstyle { \mathcal { R } } _ { n } ( a )$ for each arm, selection
count $N ( a )$ for each arm, and probability ε;
2 Randomly initialize the weights $\tau _ { 1 }$ and $\tau _ { 2 } ;$
3 if random $< \varepsilon$ then
4| Randomly select an arm;
5 else
6 | Select the arm with the maximum $\textstyle { \mathcal { R } } _ { n } ( a ) ;$
7 end
8 Update $N ( a )$ for the chosen arm;
9 Update $\textstyle { \mathcal { R } } _ { n } ( a )$ for the chosen arm by Eq. (31)
Output: Optimal weights $\tau _ { 1 }$ and $\tau _ { 2 } .$
```

$$
\mathcal { R } _ { n } ( a ) = \mathcal { R } _ { n } ( a ) + \frac { \mathcal { R } - \mathcal { R } _ { o } ( a ) } { N ( a ) } ,\tag{31}
$$

where $\mathcal { R } _ { o } ( a )$ and $\textstyle { \mathcal { R } } _ { n } ( a )$ are the old and new rewards, respectively. Moreover, R is the reward value for the time slot, and $N ( a )$ indicates the number of times the arm has been chosen.

In summary, the MAB-based weight optimization scheme diversely explores weights for MDP, effectively balancing the solutions among conflicting optimization objectives. This avoids inappropriate weights that could lead to suboptimal performance and maintains computational efficiency.

## D. Complexity Analysis of TransSAC Algorithm

In this part, we analyze the computational complexity and space complexity of the TransSAC algorithm.

The overall computational complexity of the TransSAC algorithm is $\mathcal { O } ( 2 \vert \theta \vert + \vert \Phi \vert + N _ { t } M _ { s } ( \vert \Phi \vert + N ( a ) ) + N _ { t } M _ { s } T D _ { t } +$ $N _ { t } G ( 2 | \theta | + | \Phi | ) )$ , which is detailed as follows:

\- Network Initialization: This process involves parameter initialization. The computational complexity is $\mathcal { O } ( 2 | \theta | +$ |Φ|), where |θ| and |Φ| are the number of parameters in the critic and actor networks, respectively [56].

\- Action Selection: Action selection is performed using the policy network. The computational complexity is $\mathcal { O } ( N _ { t } M _ { s } ( | \Phi | + N ( a ) ) )$ , where $N _ { t }$ indicates the number of training iteration, Ms denotes the number of steps per iteration, and $N ( a )$ denotes the arms in the MAB.

\- Transformer Executing: The complexity of executing the transformer is $\mathcal { O } ( N _ { t } M _ { s } W _ { t } D _ { t } )$ , where $D _ { t }$ indicates the data sampled from D, and $W _ { t }$ denotes the computational complexity of the transformer [54].

\- Network Update: For updating the critic and actor networks, the computational complexity is $\mathcal { O } ( N _ { t } G ( 2 | \theta | +$ |Φ|)), where G is the number of each gradient update.

The space complexity accounts for storing network parameters and the replay buffer, which contains states, actions, rewards, and next states tuples. Therefore, the space complexity of the TransSAC algorithm is $\mathcal { O } ( 2 | \theta | + | \Phi | + N ( a ) +$ $P _ { T } + D ( 2 | \pmb { s } | + | \pmb { a } | + 1 ) ,$ ), where $P _ { T }$ is the storage space for transformer-related parameters, D represents the replay buffer size, | | and | | are the dimensions of the state and action spaces, respectively.

MAIN PARAMETERS IN THE SIMULATION PROCESS
<table><tr><td>Notation</td><td>Definition</td><td>Value</td></tr><tr><td> $\beta _ { m }$ </td><td>Inclination angle</td><td>80°</td></tr><tr><td> $\Omega _ { m }$ </td><td>Right ascension of ascending node</td><td> $7 0 ^ { \circ }$ </td></tr><tr><td> $\sigma ^ { 2 }$ </td><td>Power of additive white Gaussian noise</td><td>-107 dBm</td></tr><tr><td> $\gamma$ </td><td>Discount factor</td><td>0.9</td></tr><tr><td> $\kappa$ </td><td>Parameter for soft update</td><td>0.005</td></tr><tr><td> $\varepsilon$ </td><td>Probability of exploration of MAB</td><td>0.1</td></tr><tr><td> $\varpi$ </td><td>Constant of MAB</td><td>10000</td></tr><tr><td> $C _ { S }$ </td><td>Path loss parameter of the S2V link</td><td>46.4</td></tr><tr><td> $C _ { U }$ </td><td>Path loss parameter of the U2V link</td><td>116.7</td></tr><tr><td> $d _ { c }$ </td><td>Reference distance of the U2V link</td><td>2600 m</td></tr><tr><td> $E _ { 0 }$ </td><td>Total communication energy of the UAV</td><td>500 J</td></tr><tr><td> $F _ { S }$ </td><td>Rician factor</td><td>31.3</td></tr><tr><td> $G _ { E }$ </td><td>Gain of the vessel served by UAV</td><td>8 dBi</td></tr><tr><td> $G _ { S }$ </td><td>Antenna gain of the LEO satellite</td><td>52 dBi</td></tr><tr><td> $G _ { S , S }$ </td><td>Gain of the vessel served by satellite</td><td>30 dBi</td></tr><tr><td> $G _ { U }$ </td><td>Antenna gain of the UAV</td><td>8 dBi</td></tr><tr><td> $H _ { S m }$ </td><td>Orbital altitude of the LEO satellite</td><td>900 km</td></tr><tr><td> $I _ { 0 }$ </td><td>Maximum allowable interference power</td><td>-74 dBm</td></tr><tr><td> $m _ { U }$ </td><td>Aircraft mass</td><td>2 kg</td></tr><tr><td> $P _ { S }$ </td><td>Transmit power of the LEO satellite</td><td>49.03 dBm</td></tr><tr><td> $R _ { E }$ </td><td>Radius of the Earth</td><td>6371 km</td></tr><tr><td> $T$ </td><td>Total time slots</td><td>40 s</td></tr><tr><td> $W _ { S }$ </td><td>Path loss constant exponent</td><td>2</td></tr><tr><td> $W _ { U }$ </td><td>Path loss constant exponent</td><td>1.5</td></tr><tr><td> $z _ { m i n }$ </td><td>Minimum altitude of the UAV</td><td>50 m</td></tr><tr><td> $z _ { m a x }$ </td><td>Maximum altitude of the UAV</td><td>70 m</td></tr></table>

TABLE II

## VI. SIMULATION RESULTS AND ANALYSES

In this section, we perform simulations to assess the performance of the TransSAC algorithm.

## A. Simulation Settings

1) Parameter Settings: We conduct simulation experiments in Python 3.8 and Visual Studio Code 1.91 environments, and perform all the experiments on a server with AMD EPYC 7642 48-Core CPU, NVIDIA GeForce RTX 3090 GPU, and 128 GB RAM.

In the simulation, we randomly initialize the UAV within an 80 m × 80 m feasible flight region, as the UAV could be on another mission before. Note that our simulations account for vessel trajectory variability through stochastic environmental influences and dynamic random seed strategies, while varying the initial positions of LEO satellites across training episodes. These enable the agent to explore diverse states, enhancing simulation realism and facilitating comprehensive performance evaluation. Moreover, for the TransSAC algorithm, each actor and critic network has two hidden layers and an output layer, with ReLU as the activation function, and the parameters are updated with the standard Adam optimizer. In addition, the batch size for sampling from the replay buffer is set to 128, and the number of attention heads and expansion multiplier of the hidden layer in the forward propagation are both set to 8. Additionally, the remaining primary parameters are presented in Table II [40], [47].

2) Baselines: To illustrate the performance of the TransSAC algorithm, we compare it with the theoretical optimal secrecy rate, a comparative approach, and various comparison algorithms as follows:

TABLE III  
PARAMETERS OF THE COMPARISON ALGORITHMS
<table><tr><td>Algorithm</td><td>Parameters</td></tr><tr><td>DDPG</td><td> $B _ { z } = 1 2 8 , R _ { U } = 0 . 0 0 5 , \theta = 0 . 1 5 , \sigma = 0 . 2 ,$   $\gamma = 0 . 9 , R _ { L } = 0 . 0 0 0 3 .$ </td></tr><tr><td>PPO</td><td> $B _ { z } = 1 2 8 , R _ { U } = 0 . 0 0 5 , \epsilon = 0 . 2 , \lambda = 0 . 9 ,$   $\gamma = 0 . 9 , R _ { L } = 0 . 0 0 0 3 , C _ { e } = 0 . 0 1 .$ </td></tr><tr><td>SAC</td><td> $B _ { z } = 1 2 8 , R _ { U } = 0 . 0 0 5 , \gamma = 0 . 9 , R _ { L } = 0 . 0 0 0 3 .$ </td></tr><tr><td>TD3</td><td> $B _ { z } = 1 2 8 , F _ { P } = 2 , P _ { n c } = 0 . 5 , P _ { p n } = 0 . 2 ,$   $R _ { U } = 0 . 0 0 5 , \gamma = 0 . 9 , R _ { L } = 0 . 0 0 0 3 .$ </td></tr></table>

(i) Theoretical Optimal Secrecy Rate: Under the fixed LEO satellite orbit and vessel moving trajectories, we consider a theoretical scenario where legitimate vessels receive LEO satellite signals without UAV interference, and the eavesdropper receives the maximum jamming power from the UAV. This idealized scenario allows us to calculate a theoretical optimal secrecy rate. Note that due to the NP-hard complexity and temporal characteristics of the problem, it is nearly impossible to obtain the theoretical optimal secrecy rate within real-world time constraints. Thus, this comparison indicates that our approach can obtain a near-optimal secrecy rate, making it more suitable and valuable for the considered scenario.

(ii) Non-UAV Approach: The approach relies on the LEO satellite sending signals to the legitimate vessel, without using UAV to interfere with the illegitimate vessel. As such, this comparison approach emphasizes the necessity of the UAVassisted friendly-jamming approach in implementing secure LEO satellite-maritime communications.

(iii) State-of-the-art Comparison Algorithms: We select deep deterministic policy gradient (DDPG) [57], twin delayed deep deterministic policy gradient (TD3) [58], proximal policy optimization (PPO) [59], and conventional SAC as comparison algorithms. These algorithms are commonly used to solve dynamic optimization problems [56]. Specifically, DDPG leverages the advantages of policy gradient approaches and deep learning, using the actor-critic structure to enhance policy learning, TD3 is a modification of the DDPG that improves performance through three aspects, including double Q-learning, delayed update, and target policy smoothing, and PPO improves the performance of the agent by optimizing the policy function and proposes trimming operations to maintain the stability and efficiency of training. The parameters of comparison algorithms are presented in Table III. Additionally, we set the total number of iterations in the aforementioned algorithms to $1 \times 1 0 ^ { 6 }$ , and evaluate these algorithms every 80 iterations during the training process.

## B. Simulation Results

1) Hyper-Parameters Results: Since the hyper-parameters influence DRL performance, the key parameters of the TransSAC algorithm, including learning rate (LR), number of neurons, and update rate (UR), should be considered critically. Thus, we evaluate their impact on the TransSAC to determine optimal values.

(i) LR: LR controls the step size of parameter updates, affecting training speed and stability. Fig. 5(a) shows the learning process of the TransSAC under different LR values. As can be seen, the average rewards are highest and converge fastest when LR is set to 0.003. While an LR of 0.0003 achieves comparable rewards, the convergence speed is slower. Other LR settings show lower rewards, indicating suboptimal performance.

(ii) Number of Neurons: The number of neurons in the hidden layer affects training efficiency and resource consumption. Fig. 5(b) presents the performance of the TransSAC for different neurons. Specifically, the 128-neuron setting achieves the best performance, with higher rewards and minimal fluctuations after convergence. The 64-neuron setting performs reasonably while converging slower. In contrast, the 256 neurons result in lower rewards. Despite similar rewards to the 128-neuron setting, the 512-neuron setting suffers from higher variance, reducing stability.

(iii) UR: UR controls the soft update speed, impacting training stability and convergence speed. Fig. 5(c) describes the average reward curves of various UR values. As can be seen, a UR of 0.5 achieves the highest average rewards with the fastest convergence, making it the most effective setting. A UR of 0.005 yields comparable rewards yet converges slightly slower. A UR of 0.0005 stabilizes after convergence, while it is slower and less effective. In contrast, a UR of 0.05 results in much lower rewards, indicating suboptimal performance.

2) Comparisons With Theoretical Optimal Secrecy Rate: We compare the security performance of LEO satellite-maritime communications between our approach and a theoretical scenario. Fig. 6 illustrates the secrecy rate obtained by our approach in comparison to the theoretical optimal secrecy rate during an episode. It can be seen that our method approaches the theoretical optimal secrecy rate. Note that our approach solves a multi-objective optimization problem, which requires trade-offs between secrecy rate and energy consumption of the UAV. Thus, our approach achieves a near-optimal secrecy rate, offering a practical and valuable solution for the considered scenario.

3) Comparisons With Non-UAV LEO Satellite-Maritime Communications: We compare the security performance of LEO satellite-maritime communications by using UAV-assisted and non-UAV approaches. Fig. 7 presents the average secrecy rates obtained by both approaches. As can be seen, the UAVassisted approach can consistently maintain superior secrecy rates, ensuring reliable communications. In contrast, the non-UAV approach struggles to reach a comparable secrecy rate. This demonstrates the superior performance of the UAV-assisted approach in achieving secure LEO satellite-maritime communications.

4) Comparison With Other Algorithms: Fig. 8 gives the optimization objective values obtained by different algorithms. Specifically, the TransSAC algorithm has an optimal average secrecy rate, achieving secure communications. Moreover, the average energy consumption of the UAV of the TransSAC algorithm is considerably lower, which is crucial in maritime environments where recharging UAVs is challenging. Therefore, the reliable security and minimal energy consumption make TransSAC a practical and effective algorithm. Notably, since

![](images/413276c5079b257f781823abc71d209bc76974b1d78127491ef69d11c43d2224.jpg)  
(a) LR.

![](images/3a02d3d3a4f9f22ad4dd20c7d1552fcac818d8c43f4274a1ee8710975949b6a9.jpg)  
(b) Number of Neurons.

![](images/8b6bb78e14291ec8c82565707a51997831aef3a4f5c3933da4920ea1e7e10ef4.jpg)  
(c) UR.

Fig. 5. Average reward of different hyper-parameters of the TransSAC algorithm.  
![](images/ac41fc2dbf3c0e1786307f14cfee0f46eada4d0d1d2cf830b97d578b8bc1a28a.jpg)  
Fig. 6. Secrecy rate obtained by our approach in comparison to the theoretical optimal secrecy rate.

![](images/42c83912a6ebc97ed94ecae688c53f0bf9410ce17f0539984761b8c03da7a1f0.jpg)  
Fig. 7. Average secrecy rates obtained by the UAV-assisted and non-UAV approaches.

![](images/e7b85ad3affee288ead51a5f4dad6fe2032cabb4c2e79dcc71aa9ca0c1e69367.jpg)

![](images/cf4962d556ece4eee55df7df8e2fb09535a9ba44328d47eab6a0f3ee085d5cdc.jpg)  
Fig. 8. The optimization objective values obtained by different algorithms.

![](images/6a55ed841e1f95c0ab569a127ed215664f7fa0d6554807ddfc1a2c4d57a7718d.jpg)

![](images/5445b0d6d5fb445daec2fcf2b536701d8a9c9918b904f3ca4acc8e27e6c4fb3c.jpg)  
Fig. 9. Impact of constraint changes on optimization objectives obtained by all algorithms with various $P _ { m a x }$

![](images/eb4529f0ef033ccd88d45ae05dd2c04d2fdbf1ecd5e3d93c772e40c10f97eac9.jpg)

![](images/44763e7b93773c78e5e7a9480c75bfd93a90787af4508416488cd0553f2d6d6b.jpg)  
Fig. 10. Impact of constraint changes on optimization objectives obtained by all algorithms with various $I _ { 0 } .$

TD3 is an improvement on the DDPG, the average energy consumption of the UAV of TD3 has a minimal enhancement in DDPG, resulting in similar values for both.

Furthermore, we consider determining suitable constraints in the MDP. Fig. 9 compares the optimization objective values obtained by different algorithms at various $P _ { m a x }$ values. As can be seen, the average secrecy rates gradually decrease as $P _ { m a x }$ increases. When $P _ { m a x }$ reaches 22, the secrecy rate of TransSAC drops sharply. Moreover, the average energy consumption values of PPO and TransSAC decrease significantly when $P _ { m a x }$ is 20, while the other algorithms show little sensitivity to changes in $P _ { m a x }$ . The observations suggest that $P _ { m a x }$ value of 20 is a suitable maximum transmit power to balance objective performance. In addition, Fig. 10 illustrates the optimization objectives of all algorithms at different $I _ { 0 }$ values. Clearly, the average secrecy rates and energy consumption of the UAV are optimal for most algorithms when $I _ { 0 }$ is -74, which serves as an appropriate maximum interference power, and the TransSAC algorithm demonstrates superior performance. Notably, when $I _ { 0 }$ is below -86, the secrecy rates of some algorithms approach 0, indicating ineffective UAV jamming. Therefore, we identify suitable constraints for the MDP. Moreover, the TransSAC algorithm can maximize the secrecy rate and minimize the energy consumption of the UAV under the constraints, further confirming its effectiveness.

![](images/9b9f2296aa6253f751a2a502da1960a29be1f10d0308dd9db580a1907f29edd0.jpg)  
Fig. 11. Convergence performance obtained by different algorithms.

5) Convergence Performance: The convergence performance is a key metric for evaluating DRL, reflecting the ability to stabilize and reach optimal solutions over time. Fig. 11 indicates the convergence performance of different algorithms. Clearly, the converged TransSAC obtains significantly higher average rewards than those of the other algorithms, demonstrating the ability to learn effective strategies. Notably, TransSAC converges relatively slowly (around 1000 iterations). This is because the self-attention mechanism in the transformer captures more complex features, making the training process more difficult. However, the longer convergence time is acceptable, as the significant improvements in the optimization objectives demonstrate that this trade-off is worthwhile.

## VII. DISCUSSION

In this section, we further discuss the performance of the proposed approach, and the details are as follows:

- The Extended Scenarios of Our Approach: Our approach can be extended to multiple UAV cases, achieving enhanced security performance and expanding maritime security coverage capabilities, and the details are presented in Appendix A, available online.

- Indicative Simulation Scenario: We present an indicative simulation scenario, including the trajectories of the LEO satellite, vessels, and the UAV, as well as the performance of key parameters, to enhance the clarity of our results. The detailed analysis and simulations are shown in Appendix B, available online.

- Fulfillment of Constraints of the SSMCMOP: We elaborate that our approach and various algorithms all satisfy the constraints of the SSMCMOP, and the detailed discussion is provided in Appendix C, available online.

\- Implementation of Real-time Data Transmission of Our Approach: We demonstrate that our DRL-based framework with the offline training and online execution approach can optimize real-time transmission rates by adapting to changing environmental states. Moreover, we use a Raspberry Pi to confirm that our approach can achieve real-time data transmission. See Appendix D, available online for details.

## VIII. CONCLUSION

This work has studied secure LEO satellite-maritime communications by low-altitude UAV friendly-jamming. We have considered the system that utilizes a UAV as a low-altitude platform to send jamming signals, mitigating the risk of satellitetransmitted data being eavesdropped by the illegitimate vessel. Considering the conflicting objectives, we have formulated the SSMCMOP to maximize the secrecy rate and minimize the energy consumption of the UAV simultaneously. To tackle the dynamic and NP-hard problem, we have reformulated it into an MDP. Then, we have proposed the TransSAC algorithm, a GenAI-enabled DRL approach that integrates transformer and MAB strategies to capture long-term dependencies and diversely explore weights. Simulation results have shown that the TransSAC algorithm outperforms other comparative methods and algorithms, achieving maximum secrecy rate with minimal energy consumption of the UAV. Additionally, we have determined the suitable constraint values for the MDP. This work can be extended by incorporating the imperfect positions of eavesdropping vessels and leveraging a DRL-based framework to predict the position of the illegitimate user, which will be explored in future work.

## REFERENCES

[1] Y. Yuan et al., “An air-sea-ground integrated observation system based on ad hoc network for the archipelagic environment,” in Proc. Int. Wireless Commun. Mobile Comput., 2024, pp. 1388–1393.

[2] C. Zeng et al., “Collaborative USV-buoy enabled maritime wireless networks: Cache-aided beamforming and trajectory design,” IEEE Trans. Commun., vol. 73, no. 9, pp. 8345–8361, Sep. 2025.

[3] H. Zhang, T. Zhou, T. Xu, M. Cheng, and H. Hu, “Field measurement and channel modeling around wailingding island for maritime wireless communication,” IEEE Antennas Wireless Propagat. Lett., vol. 23, no. 6, pp. 1934–1938, Jun. 2024.

[4] D. Zhou, M. Sheng, J. Li, and Z. Han, “Aerospace integrated networks innovation for empowering 6G: A survey and future challenges,” IEEE Commun. Surv. Tut., vol. 25, no. 2, pp. 975–1019, Secondquarter 2023.

[5] S. R. Pokhrel and J. Choi, “Data-driven satellite communication and control for future IoT: Principles and opportunities,” IEEE Trans. Aerosp. Electron. Syst., vol. 60, no. 3, pp. 3307–3318, Jun. 2024.

[6] P. Yue et al., “Low earth orbit satellite security and reliability: Issues, solutions, and the road ahead,” IEEE Commun. Surv, vol. 25, no. 3, pp. 1604–1652, Third Quarter 2023.

[7] Y. Wu, A. Khisti, C. Xiao, G. Caire, K. Wong, and X. Gao, “A survey of physical layer security techniques for 5G wireless networks and challenges ahead,” IEEE J. Select. Areas Commun., vol. 36, no. 4, pp. 679–695, Apr. 2018.

[8] D. Wang, B. Bai, W. Zhao, and Z. Han, “A survey of optimization approaches for wireless physical layer security,” IEEE Commun. Surv. Tut., vol. 21, no. 2, pp. 1878–1911, Second Quarter 2019.

[9] B. Zheng, S. Lin, and R. Zhang, “Intelligent reflecting surface-aided LEO satellite communication: Cooperative passive beamforming and distributed channel estimation,” IEEE J. Select. Areas Commun., vol. 40, no. 10, pp. 3057–3070, Oct. 2022.

[10] H. Xv, Y. Sun, Y. Zhao, M. Peng, and S. Zhang, “Joint beam scheduling and beamforming design for cooperative positioning in multi-beam LEO satellite networks,” IEEE Trans. Veh. Technol., vol. 73, no. 4, pp. 5276–5287, Apr. 2024.

[11] H. Huang, J. Su, and F. Wang, “The potential of low-altitude airspace: The future of urban air transportation,” IEEE Trans. Intell. Veh., vol. 9, no. 8, pp. 5250–5254, Aug. 2024.

[12] L. P. Qian, M. Li, X. Dong, Y. Wu, and X. Yang, “Secure computation offloading via cooperative jamming in marine IoT networks,” in Proc. IEEE Glob. Commun. Conf., 2022, pp. 4389–4394.

[13] J. Huang et al., “Dual AAV cluster-assisted maritime physical-layer secure communications via collaborative beamforming,” IEEE Internet Things J., vol. 12, no. 9, pp. 12589–12 607, May 2025.

[14] H. Dang-Ngoc et al., “Secure swarm UAV-assisted communications with cooperative friendly jamming,” IEEE Internet Things J., vol. 9, no. 24, pp. 25596–25611, Dec. 2022.

[15] X. Wang, H. Jiao, Q. Gao, Y. Wu, T. Jing, and J. Qian, “Trajectory optimization for maximization of energy efficiency with dynamic cluster and wireless power for UAV-assisted maritime communication,” IET Commun., vol. 18, no. 6, pp. 409–420, 2024.

[16] X. Yuan, T. Yang, Y. Hu, J. Xu, and A. Schmeink, “Trajectory design for UAV-enabled multiuser wireless power transfer with nonlinear energy harvesting,” IEEE Trans. Wireless Commun., vol. 20, no. 2, pp. 1105–1121, Feb. 2021.

[17] F. Wang, D. Jiang, Z. Wang, and S. Mumtaz, “Service continuity based data delivery optimization in satellite-terrestrial networks,” IEEE Trans. Veh. Technol., vol. 72, no. 10, pp. 13604–13617, Oct. 2023.

[18] C. Liao et al., “Game theory and multi–agent DRL based anti-jamming transmission for integrated air-ground network,” IEEE Trans. Veh. Technol., vol. 73, no. 12, pp. 19565–19 581, Dec. 2024.

[19] Z. Shao, H. Yang, L. Xiao, W. Su, Y. Chen, and Z. Xiong, “Deep reinforcement learning-based resource management for UAV-assisted mobile edge computing against jamming,” IEEE Trans. Mobile Comput., vol. 23, no. 12, pp. 13358–13374, Dec. 2024.

[20] Y. Cai, Z. Wei, R. Li, D. W. K. Ng, and J. Yuan, “Joint trajectory and resource allocation design for energy-efficient secure UAV communication systems,” IEEE Trans. Commun., vol. 68, no. 7, pp. 4536–4553, Jul. 2020.

[21] Y. He, F. Huang, D. Wang, L. Yang, and R. Zhang, “Delay minimization for NOMA-MEC offloading in ABS-aided maritime communication networks,” IEEE Trans. Veh. Technol., vol. 74, no. 6, pp. 9577–9590, Jun. 2025.

[22] F. S. Alqurashi, A. Trichili, N. Saeed, B. S. Ooi, and M. Alouini, “Maritime communications: A survey on enabling technologies, opportunities, and challenges,” IEEE Internet Things J., vol. 10, no. 4, pp. 3525–3547, Feb. 2023.

[23] M. Dai, S. Chang, Y. Wang, and Z. Su, “Energy-efficient multi-access edge computing for heterogeneous satellite-maritime networks: A hybrid harvesting-and-offloading design,” IEEE Trans. Mobile Comput., to be published, doi: 10.1109/TMC.2025.3581607.

[24] R. Wu, Z. Li, Z. Xie, and X. Liang, “Intelligent spectrum sharing strategy for integrated satellite-maritime heterogeneous mobile networks,” IEEE Trans. Veh. Technol., vol. 73, no. 5, pp. 6780–6794, May 2024.

[25] X. Hu et al., “Performance analysis of end-to-end LEO satellite-aided shore-to-ship communications: A stochastic geometry approach,” IEEE Trans. Wireless Commun., vol. 23, no. 9, pp. 11753–11769, Sep. 2024.

[26] N. Senadhira, S. Durrani, J. Guo, N. Yang, and X. Zhou, “Design and performance analysis of UAV-assisted maritime-LEO satellite communication networks,” IEEE Open J. Commun. Soc., vol. 6, pp. 4667–4688, 2025.

[27] H. Guo, J. Li, J. Liu, N. Tian, and N. Kato, “A survey on space-air-groundsea integrated network security in 6G,” IEEE Commun. Surv., vol. 24, no. 1, pp. 53–87, First Quarter 2022.

[28] B. Jiang, Y. Yan, L. You, J. Wang, W. Wang, and X. Gao, “Robust secure transmission for satellite communications,” IEEE Trans. Aerosp. Electron. Syst., vol. 59, no. 2, pp. 1598–1612, Apr. 2023.

[29] K. Xiong, X. Chen, and M. Ying, “Robust beamforming design for integrated satellite-terrestrial maritime communications in the presence of wave fluctuation,” 2024, arXiv:2407.19718.

[30] X. Wang, W. Feng, Y. Chen, and N. Ge, “UAV swarm-enabled aerial CoMP: A physical layer security perspective,” IEEE Access, vol. 7, pp. 120901–120 916, 2019.

[31] C. Liu, Y. Zhang, G. Niu, L. Jia, L. Xiao, and J. Luan, “Towards reinforcement learning in UAV relay for anti-jamming maritime communications,” Digit. Commun. Netw., vol. 9, pp. 1477–1485, 2022.

[32] F. Karami and A. B. Dariane, “A review and evaluation of multi and manyobjective optimization: Methods and algorithms,” Glob. J. Ecol., vol. 7, no. 2, pp. 104–119, 2022.

[33] X. Zheng et al., “Reliable and energy-efficient communications via collaborative beamforming for UAV networks,” IEEE Trans. Wireless Commun., vol. 23, no. 10, pp. 13235–13251, Oct. 2024.

[34] G. Sun et al., “UAV-enabled secure communications via collaborative beamforming with imperfect eavesdropper information,” IEEE Trans. Mobile Comput., vol. 23, no. 4, pp. 3291–3308, Apr. 2024.

[35] J. Li et al., “Collaborative ground-space communications via evolutionary multi-objective deep reinforcement learning,” IEEE J. Select. Areas Commun., vol. 42, no. 12, pp. 3395–3411, Dec. 2024.

[36] W. Wang et al., “Robust 3D-trajectory and time switching optimization for dual-UAV-enabled secure communications,” IEEE J. Select. Areas Commun., vol. 39, no. 11, pp. 3334–3347, Nov. 2021.

[37] H. Yang, K. Lin, L. Xiao, Y. Zhao, Z. Xiong, and Z. Han, “Energy harvesting UAV-RIS-assisted maritime communications based on deep reinforcement learning against jamming,” IEEE Trans. Wireless Commun., vol. 23, no. 8, pp. 9854–9868, Aug. 2024.

[38] Z. Liu, X. Meng, Y. Yang, K. Ma, and X. Guan, “Energy-efficient UAVaided ocean monitoring networks: Joint resource allocation and trajectory design,” IEEE Internet Things J., vol. 9, no. 18, pp. 17871–17884, Sep. 2022.

[39] X. Li, W. Feng, Y. Chen, C.-X. Wang, and N. Ge, “Maritime coverage enhancement using UAVs coordinated with hybrid satellite-terrestrial networks,” IEEE Trans. Commun., vol. 68, no. 4, pp. 2355–2369, Apr. 2020.

[40] R. Deng, B. Di, H. Zhang, L. Kuang, and L. Song, “Ultra-dense LEO satellite constellations: How many LEO satellites do we need,” IEEE Trans. Wireless Commun., vol. 20, no. 8, pp. 4843–4857, Aug. 2021.

[41] R. Skulstad, G. Li, T. I. Fossen, B. Vik, and H. Zhang, “A hybrid approach to motion prediction for ship docking-integration of a neural network model into the ship dynamic model,” IEEE Trans. Instrum. Meas., vol. 70, 2020, Art. no. 2501311.

[42] B. Shang, “Fundamentals of satellite-maritime communications: Downlink and uplink analysis,” IEEE Trans. Commun., vol. 73, no. 4, pp. 2191– 2206, Apr. 2025.

[43] C.-X. Wang, J. Bian, J. Sun, W. Zhang, and M. Zhang, “A survey of 5G channel measurements and models,” IEEE Commun. Surv. Tut., vol. 20, no. 4, pp. 3142–3168, Fourth Quarter 2018.

[44] S. Wu, C. Wang, E. M. Aggoune, M. M. Alwakeel, and X. You, “A general 3-D non-stationary 5G wireless channel model,” IEEE Trans. Commun., vol. 66, no. 7, pp. 3065–3078, Jul. 2018.

[45] D. W. Matolak and R. Sun, “Air–ground channel characterization for unmanned aircraft systems—Part I: Methods, measurements, and models for over-water settings,” IEEE Trans. Veh. Technol., vol. 66, no. 1, pp. 26–44, Jan. 2017.

[46] Y. Zeng, X. Xu, and R. Zhang, “Trajectory design for completion time minimization in UAV-enabled multicasting,” IEEE Trans. Wireless Commun., vol. 17, no. 4, pp. 2233–2246, 2018.

[47] J. Li, G. Sun, L. Duan, and Q. Wu, “Multi-objective optimization for UAV swarm-assisted IoT with virtual antenna arrays,” IEEE Trans. Mobile Comput., vol. 17, no. 4, pp. 2233–2246, Apr. 2018.

[48] P. Goos, U. Syafitri, B. Sartono, and A. R. Vazquez, “A nonlinear multidimensional knapsack problem in the optimal design of mixture experiments,” Eur. J. Oper. Res., vol. 281, no. 1, pp. 201–221, 2020.

[49] J. Xu, Y. Tian, P. Ma, D. Rus, S. Sueda, and W. Matusik, “Prediction-guided multi-objective reinforcement learning for continuous robot control,” in Proc. Int. Conf. Mach. Learn., 2020, pp. 10607–10 616.

[50] R. T. Marler and J. S. Arora, “The weighted sum method for multi-objective optimization: New insights,” Struct. Multidisciplinary Optim., vol. 41, pp. 853–862, 2010.

[51] J. Fan, Z. Wang, Y. Xie, and Z. Yang, “A theoretical analysis of deep Q-learning,” in Proc. Learn. Dyn. Control, 2020, pp. 486–489.

[52] J. Schulman, S. Levine, P. Moritz, M. I. Jordan, and P. Abbeel, “Trust region policy optimization,” 2015, arXiv:1502.05477.

[53] B. Zhang et al., “Soft actor-critic–based multi-objective optimized energy conversion and management strategy for integrated energy systems with renewable energy,” Energy Convers. Manage., vol. 243, 2021, Art. no. 114381.

[54] K. Han, A. Xiao, E. Wu, J. Guo, C. Xu, and Y. Wang, “Transformer in transformer,” in Proc. Adv. Neural Inf. Process. Syst., 2021, pp. 15908–15919.

[55] A. Vaswani et al., “Attention is all you need,” 2017, arXiv: 1706.03762.

[56] C. Zhang et al., “Multi-objective aerial collaborative secure communication optimization via generative diffusion model-enabled deep reinforcement learning,” IEEE Trans. Mobile Comput., vol. 24, no. 4, pp. 3041–3058, Apr. 2025.

[57] C. Qiu, Y. Hu, Y. Chen, and B. Zeng, “Deep deterministic policy gradient (DDPG)-based energy harvesting wireless communications,” IEEE Internet Things J., vol. 6, no. 5, pp. 8577–8588, Oct. 2019.

[58] S. Fujimoto, H. Hoof, and D. Meger, “Addressing function approximation error in actor-critic methods,” in Proc. Int. Conf. Mach. Learn., 2018, pp. 1587–1596.

[59] J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov, “Proximal policy optimization algorithms,” 2017, arXiv: 1707.06347.

![](images/71ceb74f51b661e9f04821b9622f56f8a8b7054e88ed4d6a771c40832dc3b51b.jpg)

Jiahui Li (Member, IEEE) received the BS degree in software engineering, and the MS and PhD degrees in computer science and technology from Jilin University, Changchun, China, in 2018, 2021, and 2024, respectively. He was a visiting PhD student with the Singapore University of Technology and Design (SUTD). He currently serves as an assistant researcher in the College of Computer Science and Technology, Jilin University. His current research focuses on integrated air-ground networks, UAV networks, wireless energy transfer, and optimization.

![](images/1a87db9332adf75c83e6b9cf4492bac65021b5d620c0a76641ca6a34bc820334.jpg)  
Jiawei Huang received the BS degree in software engineering from Dalian Jiaotong University, and the MS degree in software engineering from Jilin University, in 2019 and 2024, respectively. She is currently studying Computer Science with Jilin University to get a PhD degree. Her current research interests are UAV networks and optimization.

![](images/946a10f1844c583eb07a47d2e0eabb3a4ecfc14962b83415466b712b1f5f7604.jpg)

![](images/8439bf5789d8964f46530904762aaff45a35f51c900d4d096154035e2b25ed79.jpg)

Jiacheng Wang received the PhD degree from the School of Communication and Information Engineering, Chongqing University of Posts and Telecommunications, Chongqing, China. He is currently a research associate in computer science and engineering with Nanyang Technological University, Singapore. His research interests include wireless sensing, semantic communications, and metaverse.

Aimin Wang received the PhD degree in communication and information system from Jilin University, Changchun, China, in 2004. He is currently a professor with Jilin University. His research interests are wireless sensor networks and QoS for multimedia transmission.

![](images/402d5d2cc7021303ea7eaad6156c40e78fbe43c31a454941a8d81740c777b9cd.jpg)

Dusit Niyato (Fellow, IEEE) received the BEng degree from the King Mongkuts Institute of Technology Ladkrabang (KMITL), Thailand and PhD degree in electrical and computer engineering from the University of Manitoba, Canada. He is a professor in the College of Computing and Data Science, Nanyang Technological University, Singapore. His research interests are in the areas of mobile generative AI, edge general intelligence, quantum computing and networking, and incentive mechanism design.

![](images/6921e4584f89f02988cb966e6f79c26149db0a20d21b5a22a168952a5e979321.jpg)

Geng Sun (Senior Member, IEEE) received the BS degree in communication engineering from Dalian Polytechnic University, and the PhD degree in computer science and technology from Jilin University, in 2011 and 2018, respectively. He was a visiting researcher with the School of Electrical and Computer Engineering, Georgia Institute of Technology, USA. He is a professor in the College of Computer Science and Technology, Jilin University. Currently, he is working as a visiting scholar with the College of Computing and Data Science, Nanyang Techno-

logical University, Singapore. He has published more than 100 high-quality papers, including IEEE Transactions on Mobile Computing, IEEE Journal on Selected Areas in Communications, IEEE/ACM Transactions on Networking, IEEE Transactions on Wireless Communications, IEEE Transactions on Communications, IEEE Transactions on Antennas and Propagation, IEEE Internet of Things Journal, IEEE Transactions on Instrumentation and Measurement, IEEE INFOCOM, IEEE GLOBECOM, and IEEE ICC. He serves as the associate editors of IEEE Communications Surveys & Tutorials, IEEE Transactions on Communications, IEEE Transactions on Vehicular Technology, IEEE Transactions on Network Science and Engineering, IEEE Transactions on Network and Service Management, and IEEE Networking Letters. He serves as the lead guest editor of Special Issues for IEEE Transactions on Network Science and Engineering, IEEE Internet of Things Journal, IEEE Networking Letters. He also serves as the guest editor of Special Issues for IEEE Transactions on Services Computing, IEEE Communications Magazine, and IEEE Open Journal of the Communications Society. His research interests include Low-altitude Wireless Networks, UAV communications and Networking, Mobile Edge Computing (MEC), Intelligent Reflecting Surface (IRS), Generative AI and Agentic AI, and deep reinforcement learning.

![](images/0abd65b16487792e9836765acf801deaff04df2d2289b67e4eadc4df9d28df64.jpg)

Victor C. M. Leung (Life Fellow, IEEE) is currently a distinguished professor of computer science and software engineering with Shenzhen University, China. He is also an emeritus professor of electrial and computer engineering and the director with the Laboratory for Wireless Networks and Mobile Systems, University of British Columbia. He has coauthored more than 1300 journal/conference papers and book chapters, and has been named in the current Clarivate Analytics list of Highly Cited Researchers. His research interests include the broad areas of wireless networks and mobile systems. Dr. Leung is also on the editorial boards of IEEE Transactions on Green Communications and Networking, IEEE Transactions on Cloud Computing, IEEE Access, and several other journals. He was the recipient of the IEEE Vancouver Section Centennial Award, 2011 UBC Killam Research Prize, 2017 Canadian Award for Telecommunications Research, 2018 IEEE TCGCC Distinguished Technical Achievement Recognition Award, and has coauthored papers that were the recipient of the 2017 IEEE ComSoc Fred W. Ellersick Prize, 2017 IEEE Systems Journal Best Paper Award, 2018 IEEE CSIM Best Journal Paper Award, and 2019 IEEE TCGCC Best Journal Paper Award. He is also the life fellow of IEEE, and a fellow of the Royal Society of Canada, Canadian Academy of Engineering, and Engineering Institute of Canada.