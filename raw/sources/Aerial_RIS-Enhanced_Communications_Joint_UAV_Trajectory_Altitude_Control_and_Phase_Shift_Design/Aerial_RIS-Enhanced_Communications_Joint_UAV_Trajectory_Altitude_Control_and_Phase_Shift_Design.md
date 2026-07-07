# Aerial RIS-Enhanced Communications: Joint UAV Trajectory, Altitude Control, and Phase Shift Design

Bin Li , Member, IEEE, Dongdong Yang , Lei Liu , Member, IEEE, and Dusit Niyato , Fellow, IEEE

Abstract—Reconfigurable intelligent surface (RIS) has emerged as a pivotal technology for enhancing wireless networks. Compared to terrestrial RIS deployed on building facades, aerial RIS (ARIS) mounted on quadrotor uncrewed aerial vehicle (UAV) offers superior flexibility and extended coverage. However, the inevitable tilt and altitude variations of a quadrotor UAV during flight may lead to severe beam misalignment, significantly degrading ARIS’s performance. To address this challenge, we propose an Euler angles-based ARIS control scheme that jointly optimizes the altitude and trajectory of the ARIS by leveraging the UAV’s dynamic model. Considering the constraints on ARIS flight energy consumption, flight safety, and the transmission power of a base station (BS), we jointly design the ARIS’s altitude, trajectory, phase shifts, and BS beamforming to maximize the system sum-rate. Due to the continuous control nature of ARIS flight and the strong coupling among variables, we formulate the problem as a Markov decision process and adopt a soft actor-critic algorithm with prioritized experience replay to learn efficient ARIS control policies. Based on the optimized ARIS configuration, we further employ the water-filling and bisection method to efficiently determine the optimal BS beamforming. Numerical results demonstrate that the proposed algorithm significantly outperforms benchmarks in both convergence and communication performance, achieving approximately 14.4% improvement in sum-rate. Moreover, in comparison to the fixed-horizontal ARIS scheme, the proposed scheme yields more adaptive trajectories and significantly mitigates performance degradation caused by ARIS tilting, demonstrating strong potential for practical ARIS deployment.

Index Terms—Reconfigurable intelligent surface, UAV altitude, Euler angle, multi-user communication, deep reinforcement learning.

## I. INTRODUCTION

S A paradigm-shifting wireless communication technology, reconfigurable intelligent surface (RIS) leverages   
massive low-cost passive elements to achieve programmable   
signal enhancement via phase-coherent superposition, offering

unprecedented advantages in low-power implementation and economical deployment [1]. However, conventional terrestrial RIS is constrained by its fixed deployment, limiting service area to static coverage regions [2]. This limitation can be mitigated by integrating RIS with uncrewed aerial vehicle (UAV), renowned for their superior line-of-sight (LoS) probability and three-dimensional maneuverability [3]. The resultant aerial RIS (ARIS) architecture synergistically integrates the complementary benefits of both technologies, establishing itself as a promising solution for next-generation adaptive networks with dynamic beamforming capabilities and extended service coverage [4].

However, in practical ARIS deployments, a UAV inevitably experiences fuselage tilting due to inertial resistance during acceleration/deceleration and aerodynamic effects [5], leading to beam misalignment and channel variations that degrades ARIS-assisted communications [6]. Furthermore, existing research has demonstrated that the practical gain of RIS is highly sensitive to signal incidence and reflection angles [7]. Despite these physical constraints, current studies predominantly neglect the impact of ARIS altitude variations, resulting in suboptimal system performance that fails to achieve the theoretical upper-bound of ARIS gains [8]. This persistent oversight in system modeling fundamentally limits the practical implementation effectiveness of ARIS, presenting a critical challenge remaining to address in ARIS deployment optimization.

## A. Prior Work

1) RIS-Assisted Communications: To fully leverage the channel enhancement benefits of RIS in wireless communications, extensive efforts have been devoted to exploring RIS applications across various communication scenarios. In particular, Guo et al. [9] explored the application of RIS in a downlink scenario, employing fractional programming and descent-based methods to enhance the sum-rate. Similarly, Yang et al. [10] addressed resource allocation challenges in a distributed RIS-enabled wireless network and introduced two distinct algorithms tailored for both single-user and multi-user cases. More recently, RIS has also been applied to wireless powered mobile edge computing networks. Zhai et al. [11] proposed a Stackelberg game-based offloading framework, aiming to enable efficient energy trading and computation between passive devices and the energy station. Considering the halfspace coverage limitation of conventional RIS, Xu et al. [12] proposed the simultaneously transmitting and reflecting RIS (STAR-RIS) architecture, extending its service to full-space domains through its simultaneous transmission and reflection capabilities. In [13], Mu et al. investigated STAR-RIS-assisted MISO systems, establishing three fundamental operating protocols and developing a penalty-based iterative algorithm with successive convex approximation. Moreover, building on the concept of STAR-RIS, the intelligent omni-surface (IOS) has been proposed in [14] which enables simultaneous reflection and refraction to achieve full-dimensional coverage. A hybrid beamforming scheme and prototype validation further demonstrated the feasibility and potential of IOS-assisted communications. Driven by the aforementioned advantages of RIS in wireless communications, several studies have explored its role in enhancing UAV-assisted networks, where the UAV functions as an aerial base station (BS). For instance, Li et al. [15] conducted a joint design of UAV trajectory and RIS passive beamforming to enhance the average achieve rate. Considering the constrained energy capacity of UAV, Liu et al. [16] proposed a deep Q-network (DQN)-based approach to optimization UAV trajectory and power allocation, aiming to minimize the energy consumption. Furthermore, Zhai et al. [17] promoted this paradigm to wireless powered communication networks, and proposed a hierarchical Stackelberg game method to address sum-rate and fairness tradeoffs while enhancing utility. However, most existing RISassisted schemes assume fixed terrestrial deployment, which limits their adaptability to dynamic user distributions and environmental variations. This motivates the integration of UAV and RIS to enhance coverage and flexibility.

2) ARIS-Assisted Communications: Currently, ARIS trajectory and phase shifts optimization methods generally fall into two main categories, traditional mathematical optimization technologies and data-driven machine learning approaches. For example, Liu et al. [18] jointly optimized ARIS trajectory and dynamic power allocation to maximize average downlink throughput in time-slotted transmissions. Furthermore, considering the influence of the incident and reflected angles of signals, Liu et al. [19] took into account the elevation angle and established an optimization problem with the minimum average achievable rate maximization as the optimization objective, jointly optimizing communication resource allocation, ARIS phase shifts, and trajectory by an efficient iterative algorithm. Deep reinforcement learning (DRL) has become a cornerstone methodology for intelligent aerial network, particularly in joint UAV trajectory and RIS configurations optimization under dynamic channel conditions and operational uncertainties [20]. Peng and Wang [21] proposed an energy-harvesting ARIS scheme to enhance UAV endurance and developed a soft-max deep deterministic policy gradient (DDPG)-based solution. To address the massive access demands of GUs, Wu et al. [22] integrated the ARIS into a satellite-air-ground integrated relay network and proposed an algorithm combining long short-term memory and double DQN to maximize the system ergodic rate with limited flight energy consumption. Considering the half-space coverage limitation of the RIS, Aung et al. [23] introduced the aerial STAR-RIS into the mobile edge computing system and utilized a proximal policy optimization (PPO)-based DRL approach to design the UAV trajectory, STAR-RIS configurations, and task offloading strategies. Although ARIS improves coverage and adaptability, existing work primarily focused on trajectory and phase shift optimization while neglecting UAV altitude variations, which may influence the ARIS gain, thereby degrading communication performance.

3) RIS Orientation and UAV Tilt: Recent studies have demonstrated the significant impact of RIS orientation on overall performance. In [7], Cheng et al. systematically quantified the impact of RIS orientation on communications, introducing rotation as an auxiliary control dimension to augment the channel gain of RIS. Similarly, in [24], Zeng et al. analyzed a downlink RIS-assisted network with one BS and one user, and proposed a coverage maximization algorithm with a closedform solution for optimal RIS orientation. To further enhance the effectiveness of RIS in extending cell coverage, Zeng et al. [24] examined a downlink RIS-enhanced network comprising single BS and user, and focused on the optimization of RIS orientation and position to enhance overall coverage. Furthermore, in [25], Wang et al. explored the rotation of STAR-RIS and utilized deep learning to optimize STAR-RIS orientation in various scenarios, achieving full-space coverage while maximizing STAR-RIS gain. Li et al. [26] and Yang et al. [27] studied rotatable RIS-assisted and rotatable STAR-RIS-assisted mobile edge computing systems, respectively.

On the other hand, the impact of UAV tilt on communication performance has also been explored. As a representative study, Wang and Zhang [28] systematically investigated UAV jitter effects in millimeter-wave (mmWave) systems and established an unified planar array-based mmWave channel model by analyzing spatial correlations among antenna elements, deriving explicit mathematical relationships between UAV’s tilt and 3D positional coordinates. Ouyang et al. [29] investigated a robust beamforming scheme for rate-splitting multiple access-enabled UAV uplink communication systems under UAV jitter-induced effects, and developed a second-order Taylor series expansionbased approximation method to simplify the characterization of angle of arrival uncertainties caused by UAV’s fluctuation. Xiong et al. [30] developed a novel channel model for ARISassisted mmWave networks, explicitly accounting for UAV’s tilt instability. Utilizing the refined model, they formulated a closed-form expression to characterize the signal-to-noise ratio under UAV’s tilt. Furthermore, Xu et al. [31] proposed considering UAV’s tilt to be an optimization variable to enhance the ergodic sum-rate in ARIS-assisted systems. By jointly optimizing the ARIS rotation in both elevation and azimuth angular dimensions, they formulated a dual-angle optimization problem and derived closed-form solutions. Despite these works demonstrating the impact of RIS orientation and UAV tilt on communication performance, few studies have integrated UAV’s tilt into ARIS optimization.

## B. Motivations and Contributions

Existing work predominantly neglects the critical impacts of altitude variations during ARIS flight and overlooks orientation-dependent performance degradation in communication systems. However, in practical scenarios, a quadrotor UAV inevitably experiences altitude variations due to inertial forces and acceleration, substantially constraining the achievable ARIS deployment gains. To address this challenge, we propose an Euler angles-based flight control paradigm integrated with quadrotor dynamics modeling. This framework enables simultaneous ARIS trajectory design and altitude optimization through control Euler angles, while maintaining optimal beamforming alignment via real-time phase shift adjustments.

![](images/09869bea08c51ff2211844732e676611da7c555b0bc80dcc21215fe89fadd90e.jpg)  
Fig. 1. The system model of ARIS-assisted communication system with UAV altitude control.

Building upon the preceding discussion, the key contributions of this paper are outlined as follows:

• We investigate an ARIS-assisted communication system, where ARIS reflects signals from a BS to GUs. Given the impact of ARIS’s altitude on performance gain, we propose an Euler angles-based ARIS control scheme for joint ARIS altitude and trajectory optimization. Therefore, we formulate an optimization problem to maximize the sumrate by adjusting ARIS’s altitude, trajectory, phase shifts, and BS beamforming, while ensuring compliance with constraints on BS transmission power, ARIS flight energy consumption, and flight safety.

• We transform the sum-rate maximization problem into a Markov decision process (MDP)-based model. Considering that the intractability of convex optimization-based methods and the limited exploration capabilities of conventional DRL algorithms in high-dimensional action space, a novel DRL framework based on the soft actor-critic with prioritized experience replay (SAC-PER) algorithm is proposed. The algorithm synergistically integrates maximum entropy reinforcement learning principles with stochastic policy optimization to enhance exploration efficiency while maintaining stable convergence.

• Numerical results demonstrate that the proposed Euler angles-based UAV control scheme effectively achieves joint altitude and trajectory optimization, exhibiting distinctly different trajectory compared to conventional horizontal ARIS baseline. Furthermore, the proposed SAC-PER outperforms benchmark methods in both learning efficiency and steady-state performance.

Notation: Scalars, vectors, and matrices are represented by italic letters, bold lowercase letters, and bold uppercase letters, respectively. The collection of $N \times M$ complex-valued matrices is symbolized as $\mathbb { C } ^ { N \times M }$ . For any complex-valued vector $\mathbf { a } , \parallel \mathbf { a } \parallel , \mathbf { \bar { a } } ^ { T }$ , and $\mathbf { a } ^ { H }$ indicate its Euclidean norm, transpose, and conjugate transpose, respectively. The expectation operator is written as $\mathbb { E } [ \cdot ]$ , and diag(a) represents a diagonal matrix whose main diagonal entries are elements of a.

## II. SYSTEM MODEL AND PROBLEM FORMULATION

In this section, we begin by introducing the ARIS-assisted communication system, where a BS with multiple antennas provides service to multiple single-antenna GUs with the ARIS. Next, we present an Euler angles-based ARIS flight control framework and derive its associated flight energy consumption model. Building on these foundation, we analyze the practical ARIS channel gain and establish the signal transmission model.

## A. Scenario Description

Considering an ARIS-assisted wireless communication system in which a BS equipped with M antennas provides service to $K ( K \ \leq \ M )$ single-antenna GUs. The set of GUs is denoted by $\mathcal { K } = \{ 1 , \ldots , k , \ldots , K \}$ . As depicted in Fig. 1, the potential obstacles may cause the direct links between the BS and GUs to be unreliable or even blocked. In response, an ARIS composed of N elements is introduced, denoted by $\mathcal { N } = \{ 1 , \ldots , n , \ldots , N \}$ , mounted on the UAV to establish high-quality communication links. Specially, the RIS is fixed beneath the UAV and tilting in accordance with the UAV’s altitude. Let T represent the flight duration of the UAV. For tractability, we partition T into L equal and non-overlapping time slots, each with length $\delta = T / L$ . The set of time slots is represented by $\mathcal { L } = \left\{ 1 , \dots , l , \dots , L \right\}$ . The ARIS flies at a fixed altitude H while continuously adjusting its Euler angles to achieve altitude and trajectory control. In each time slot, the position of the UAV is defined as ${ \bf q } [ l ] = ( x [ l ] , y [ l ] , H )$ the velocity is denoted by $\mathbf { v } [ l ] ~ = ~ ( v _ { x } [ l ] , v _ { y } [ l ] , 0 )$ , and the acceleration is ${ \bf a } [ l ] = ( a _ { x } [ l ] , a _ { y } [ l ] , 0 )$ . Considering the practical scenario, the ARIS flight is subject to maximum speed and acceleration constraints as follows:

$$
| \mathbf { v } [ l ] | \leq v _ { \operatorname* { m a x } } , l \in \mathcal { L } ,
$$

$$
\vert \mathbf { a } [ l ] \vert \leq a _ { \mathrm { m a x } } , l \in \mathcal { L } .\tag{1}
$$

(2)

Although introducing ARIS can significantly improve the communication quality, the BS-ARIS-GU links suffer from substantial path loss due to multiplicative fading, requiring a large number of ARIS elements to compensate. However, a large number of ARIS elements may cause excessive channel state information acquisition and ARIS design complexity. To solve this, the approach in [32] is adopted to partition the N elements into N<sup>¯</sup> sub-surfaces. Each sub-surface, indexed by the set $\bar { \mathcal { N } } = 1 , . . . , \bar { n } , . . . , \bar { N }$ , consists of $\tilde { N } \ = \ N / \bar { N }$ (assumed to be an integer) adjacent elements sharing the same phase shift, thereby decreasing the overall implementation complexity. Specifically, for the n¯-th sub-surface at time slot l, the reflection coefficient is given by $\theta _ { \bar { n } } [ l ] = e ^ { j \varphi _ { \bar { n } } [ l ] }$ , where $\varphi _ { \bar { n } } [ l ] \ \in \ [ 0 , 2 \pi )$ denotes the phase shift of this sub-surface. Therefore, the diagonal reflection coefficient matrix can be expressed as Θ = diag $\mathbf { \Gamma } \left( \pmb { \theta } [ l ] \otimes \mathbf { 1 } _ { \tilde { N } \times 1 } \right) \ \in \ \mathbb { C } ^ { N \times N }$ , where $\pmb { \theta } [ l ] ~ = ~ \{ \theta _ { 1 } [ l ] , \dots , \theta _ { \bar { n } } [ l ] , \dots , \bar { \theta } _ { \bar { N } } [ l ] \}$ , where $\otimes$ denotes the Kronecker product.

## B. Dynamic Model of ARIS

In this paper, we model the ARIS as a rigid body, with its Euler angles at time slot l represented by the set $\Phi [ l ] =$ $\{ \phi [ l ] , \theta [ l ] , \psi [ l ] \}$ , where $\phi [ l ] , \theta [ l ]$ , and ψ[l] represent the roll, pitch, and yaw angles, respectively. The flight dynamics of the ARIS are powered by the continuous rotation of its four rotors. By adjusting the angular velocities of rotors, denoted by $\omega _ { i } > 0 , i \in \{ 1 , 2 , 3 , 4 \}$ (only considering the magnitude of angular velocities), both trajectory and altitude control of ARIS can be achieved. According to [33], the thrust at time instant for each rotor is given by

$$
F _ { i } [ l ] = C _ { t } \omega _ { i } ^ { 2 } [ l ] , i \in \left\{ 1 , 2 , 3 , 4 \right\} ,\tag{3}
$$

where $C _ { t }$ is the constant thrust coefficient.

The dynamic model governing the ARIS flight control is described by (4), as shown at the bottom of the page, where the total thrust is calculated by

$$
F _ { \mathrm { t o t } } [ l ] = C _ { t } \left( \omega _ { 1 } ^ { 2 } [ l ] + \omega _ { 2 } ^ { 2 } [ l ] + \omega _ { 3 } ^ { 2 } [ l ] + \omega _ { 4 } ^ { 2 } [ l ] \right) .\tag{5}
$$

As we consider the ARIS flight at a fixed altitude H, which implies that $v _ { z } = 0$ and $a _ { z } = 0$ , the total thrust $F _ { \mathrm { t o t } }$ can be calculated by

$$
F _ { \mathrm { t o t } } [ l ] = \frac { m g } { \cos \phi [ l ] \cos \theta [ l ] } .\tag{6}
$$

Consequently, given the ARIS’s Euler angles, the accelerations along the x- and y-axes are given by (7) and (8), as shown at the bottom of the page.

Therefore, both the ARIS’s altitude and trajectory control can be realized.

## C. Energy Consumption Model

Assuming uniform angular velocities for all rotors, the angular velocity of each rotor can be obtained according to (5) and (6), given by

$$
\omega _ { i } [ l ] = \sqrt { \frac { m g } { 4 C _ { t } \cos \phi [ l ] \cos \theta [ l ] } } , i \in \{ 1 , 2 , 3 , 4 \} .\tag{9}
$$

For each rotor, the corresponding current and voltage at each time slot are calculated by [33]

$$
{ I _ { i } [ l ] } = \frac { { C _ { m } } } { { K _ { T } } } \omega _ { i } ^ { 2 } [ l ] + I _ { 0 } ,\tag{10}
$$

$$
U _ { i } [ l ] = K _ { E } N _ { i } [ l ] + I _ { i } [ l ] R _ { 0 } .\tag{11}
$$

Therefore, the energy consumption of each motor can be obtained by

$$
\begin{array} { r l r } & { } & { P _ { i } [ l ] = U _ { i } [ l ] I _ { i } [ l ] } \\ & { } & { \qquad = c _ { 4 } \omega _ { i } ^ { 4 } [ l ] + c _ { 3 } \omega _ { i } ^ { 3 } [ l ] + c _ { 2 } \omega _ { i } ^ { 2 } [ l ] + c _ { 1 } \omega _ { i } [ l ] + c _ { 0 } , } \end{array}\tag{12}
$$

where $c _ { 0 } = I _ { 0 } ^ { 2 } R _ { 0 } , c _ { 1 } = 3 0 K _ { E } I _ { 0 } / \pi , c _ { 2 } = 2 C _ { m } R _ { 0 } I _ { 0 } / K _ { T }$ $c _ { 3 } = 3 0 C _ { m } K _ { E } / ( \pi K _ { T } )$ , and $c _ { 4 } = C _ { m } ^ { 2 } R _ { 0 } / K _ { T } ^ { 2 }$

Combining equations (9) and (12), the flight energy consumption of the ARIS during time slot l is given by

$$
\begin{array} { c } { { P ^ { \mathrm { \tiny { H y } } } [ l ] = \displaystyle \frac { c _ { 4 } } { 4 } \left( \frac { m g } { C _ { t } \cos \phi [ l ] \cos \theta [ l ] } \right) ^ { \frac { 3 } { 2 } } } } \\ { { + \displaystyle \frac { c _ { 3 } } { 2 } \left( \frac { m g } { C _ { t } \cos \phi [ l ] \cos \theta [ l ] } \right) ^ { \frac { 3 } { 2 } } + \frac { c _ { 2 } m g } { C _ { t } \cos \phi [ l ] \cos \theta [ l ] } } } \\ { { + \displaystyle 2 c _ { 1 } \left( \frac { m g } { C _ { t } \cos \phi [ l ] \cos \theta [ l ] } \right) ^ { \frac { 1 } { 2 } } + 4 c _ { 0 } . \qquad ( 1 } } \end{array}\tag{3}
$$

Therefore, the sum energy consumption for ARIS can be calculated by $\begin{array} { r } { E ^ { \mathrm { H y } } = \sum _ { l = 1 } ^ { L ^ { \mathrm { - } } } P ^ { \mathrm { f i y } } [ l ] \delta } \end{array}$

## D. Corresponding Angle Calculation

As shown in Fig. 2(a), the unit normal vector of the ARIS plane, aligned with the negative ˜z-axis in the local coordinate system (LCS) ˜x-˜y-˜z, is defined as

$$
e _ { \perp } ^ { \mathrm { l o c } } = \left[ 0 0 - 1 \right] ^ { T } .\tag{14}
$$

Since the different coordinate frames are defined, the relationship between them, namely the coordinate transformation between global coordinate system and LCS, must be established. Firstly, the origin should be translated from $( 0 , 0 , 0 )$ to point $( x [ l ] , y [ l ] , H )$ . Subsequently, the system undergoes sequential rotations: roll angle around $\mathbf { X } _ { 1 } \mathbf { - a x i s } .$ , pitch angle around y<sub>2</sub>-axis, and yaw angle around $\mathrm { Z _ { 3 } \mathrm { - } a x i s }$ , as shown in Fig. 2(b)-(d). Consequently, the transformation can be

$$
\left\{ \begin{array} { l l } { m a _ { x } [ l ] } & { = F _ { \mathrm { t o t } } [ l ] ( \sin \psi [ l ] \sin \phi [ l ] + \sin \theta [ l ] \cos \psi \cos \phi [ l ] ) } \\ & { - C _ { d \infty } v _ { \infty } [ l ] \left| v _ { \infty } [ l ] \right| , } \\ { m a _ { y } [ l ] } & { = F _ { \mathrm { t o t } } [ l ] ( \sin \theta [ l ] \sin \psi [ l ] \cos \phi [ l ] - \sin \phi [ l ] \cos \psi [ l ] ) } \\ & { - C _ { d y } v _ { y } [ l ] \left| v _ { y } [ l ] \right| , } \\ { m a _ { z } [ l ] } & { = F _ { \mathrm { t o t } } [ l ] \cos \phi [ l ] \cos \theta [ l ] - m g - C _ { d z } v _ { z } [ l ] \left| v _ { z } [ l ] \right| , } \end{array} \right.\tag{4}
$$

$$
a _ { x } [ l ] = \frac { g \tan \phi [ l ] \sin \psi [ l ] } { \cos \theta [ l ] } - g \tan \theta [ l ] \cos \psi [ l ] - \frac { C _ { d \infty } v _ { \infty } [ l ] | v _ { \infty } [ l ] | } { m } ,
$$

$$
a _ { 3 } [ l ] = g \tan \theta [ l ] \sin \psi [ l ] - \frac { g \tan \phi [ l ] \cos \psi [ l ] } { \cos \theta [ l ] } - \frac { C _ { d y } v _ { 3 } [ l ] | v _ { 3 } [ l ] | } { m } .\tag{7}
$$

(8)

![](images/88b705531b3e641f2e8c0c8ec5fa6cc81730d454f39b0e163ad2c7e7a718aebc.jpg)  
Fig. 2. The altitude variation and definition of ARIS Euler angles.

accomplished by multiplying the relevant rotation matrices, given by

$$
\mathbf { R } _ { x } \left( \theta [ l ] \right) = \left[ \begin{array} { c c c } { \cos \theta [ l ] } & { 0 \sin \theta [ l ] } \\ { 0 } & { 1 } & { 0 } \\ { - \sin \theta [ l ] \ 0 \cos \theta [ l ] } \end{array} \right] ,\tag{15}
$$

$$
\mathbf { R } _ { y } \left( \phi [ l ] \right) = \left[ \begin{array} { l l } { 1 } & { 0 } \\ { 0 \cos \phi [ l ] - \sin \phi [ l ] } \\ { 0 \sin \phi [ l ] } & { \cos \phi [ l ] } \end{array} \right] ,\tag{16}
$$

$$
\mathbf { R } _ { z } \left( \psi [ l ] \right) = \left[ \begin{array} { c c c } { \cos \psi [ l ] } & { - \sin \psi [ l ] } & { 0 } \\ { \sin \psi [ l ] } & { \cos \psi [ l ] } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right] .\tag{17}
$$

The translation matrix could be obtained by multiplying these matrices, as shown in equation (18), at the bottom of the page. Specifically, the unit normal vector ${ \bf e } _ { \perp } ^ { \mathrm { l o c } }$ would be translated to

$$
\begin{array} { r l r } {  { \mathbf { e } _ { \perp } [ l ] = \mathbf { R } [ l ] \mathbf { e } _ { \perp } ^ { \mathrm { l o c } } } } \\ & { } & { = [ - \cos \psi [ l ] \cos \phi [ l ] \sin \theta [ l ] - \sin \psi [ l ] \sin \theta [ l ] ] } \\ & { } & { = [ - \sin \psi [ l ] \cos \phi [ l ] \sin \theta [ l ] + \cos \psi [ l ] \sin \theta [ l ] ] } \\ & { } & { ~ - \cos \phi [ l ] \cos \theta [ l ] } \end{array}\tag{19}
$$

The unit direction vectors of incident (between the BS and ARIS) and reflected signals (between the ARIS and GU k) are given by

$$
\mathbf { e } _ { k / \mathrm { B S } } ^ { \mathrm { R I S } } [ l ] = \left[ \begin{array} { c } { \cos \beta _ { k / \mathrm { B S } } ^ { \mathrm { R I S } } [ l ] \cos \alpha _ { k / \mathrm { B S } } ^ { \mathrm { R I S } } [ l ] } \\ { \cos \beta _ { k / \mathrm { B S } } ^ { \mathrm { R I S } } [ l ] \sin \alpha _ { k / \mathrm { B S } } ^ { \mathrm { R I S } } [ l ] } \\ { \sin \beta _ { k / \mathrm { B S } } ^ { \mathrm { R I S } } [ l ] } \end{array} \right] ,\tag{20}
$$

where $\alpha _ { k / \mathrm { B S } } ^ { \mathrm { R I S } }$ and $\beta _ { k / \mathrm { B S } } ^ { \mathrm { R I S } }$ denote the azimuth and elevation angles from GU k and the BS to the ARIS, respectively.

Therefore, the angle between the incident/reflected signal and the normal vector of the ARIS plane can be obtained by

$$
\begin{array} { r l } & { \cos \gamma _ { k / \mathrm { B S } } ^ { \mathrm { R I S } } [ l ] } \\ & { = \frac { - \mathbf { e } _ { \perp } ^ { T } [ l ] \| 1 m u \mathbf { e } _ { k / \mathrm { B S } } ^ { \mathrm { R I S } } [ l ] } { \| - \mathbf { e } _ { \perp } [ l ] \| } } \\ & { = \cos \phi [ l ] \sin \theta [ l ] \cos \beta _ { k / \mathrm { B S } } ^ { \mathrm { R I S } } [ l ] \cos \left( \alpha _ { k / \mathrm { B S } } ^ { \mathrm { R I S } } [ l ] - \psi [ l ] \right) } \\ & { \phantom { = } + \cos \beta _ { k / \mathrm { B S } } ^ { \mathrm { R I S } } [ l ] \sin \theta [ l ] \sin \left( \psi [ l ] - \alpha _ { k / \mathrm { B S } } ^ { \mathrm { R I S } } [ l ] \right) } \\ & { \phantom { = \ } + \sin \beta _ { k / \mathrm { B S } } ^ { \mathrm { R I S } } [ l ] \cos \phi [ l ] \cos \theta [ l ] . } \end{array}\tag{21}
$$

This result highlights that the ARIS’s altitude directly impact the incident and reflection angles, thereby altering ARIS gain and overall performance.

## E. Signal Model

For any time slot, the narrow-band quasi-static fading channels from the BS to ARIS, as well as from ARIS to GU k, denoted by $\mathbf { H } [ l ] \in \mathbb { C } ^ { M \times N }$ and $\mathbf h _ { k } [ l ] \in \mathbb { C } ^ { N \times 1 }$ , are modeled as Rician fading channels, given by

$$
\mathbf { H } [ l ] = \sqrt { \frac { \rho _ { 0 } } { d _ { \mathrm { R , B } } [ l ] ^ { \alpha _ { 1 } } } } \left( \sqrt { \frac { K _ { 1 } } { 1 + K _ { 1 } } } \bar { \mathbf { H } } [ l ] + \sqrt { \frac { 1 } { 1 + K _ { 1 } } } \tilde { \mathbf { H } } [ l ] \right) ,\tag{22}
$$

$$
\mathbf { h } _ { k } [ l ] = \sqrt { \frac { \rho _ { 0 } } { d _ { \mathrm { R } , k } [ l ] ^ { \alpha _ { 2 } } } } \left( \sqrt { \frac { K _ { 2 } } { 1 + K _ { 2 } } } \bar { \mathbf { h } } _ { k } [ l ] + \sqrt { \frac { 1 } { 1 + K _ { 2 } } } \tilde { \mathbf { h } } _ { k } [ l ] \right)\tag{23}
$$

where $\rho _ { 0 }$ represents the path loss at the reference distance of 1 meter, $\alpha _ { 1 }$ and $\alpha _ { 2 }$ are the pass loss exponents, $d _ { \mathrm { R , B } } [ l ] =$ $\| \mathbf { q } [ l ] - \mathbf { q } _ { \mathrm { B } } \|$ is the distance between the ARIS and BS, $d _ { \mathrm { R } , k } [ l ] = \lVert \mathbf { q } [ l ] - \mathbf { q } _ { k } \rVert$ is the distance between GU k and the ARIS, with $\mathbf { q } _ { \mathrm { B } }$ and $\mathbf q _ { k }$ denote the position of the BS and GU $k ,$ respectively. $K _ { 1 }$ and $K _ { 2 }$ denote the Rician factors, H<sup>˜</sup> [l] and $\tilde { \mathbf { h } } _ { k } [ l ]$ are complex Gaussian random variables with independently and identically distributed zero mean and unit variance, H<sup>¯</sup> [l] and $\bar { \mathbf { h } } _ { k } ^ { \mathrm { R } } [ l ]$ represent the LoS components.

Considering that the practical channel gain of ARIS is influenced by the angles of signal incidence and reflection, the actual gain of the ARIS can be modeled as follows [25]:

$$
\begin{array} { r l } & { \pmb { \xi } _ { k } = G _ { k } [ l ] G _ { \mathrm { B } } [ l ] \Phi _ { m } [ l ] } \\ & { \overset { \Delta } { = } D _ { m } ^ { 2 } F \left( v _ { k , \mathrm { R } } ^ { \mathrm { A O D } } [ l ] , \vartheta _ { k , \mathrm { R } } ^ { \mathrm { A O D } } [ l ] \right) F \left( v _ { \mathrm { R } , \mathrm { B } } ^ { \mathrm { A O A } } [ l ] , \vartheta _ { \mathrm { R } , \mathrm { B } } ^ { \mathrm { A O A } } [ l ] \right) \Phi [ l ] , } \end{array}\tag{24}
$$

where $D _ { m }$ represents the ARIS’s maximum directivity, $G _ { k }$ signifies the reception gain from the BS to ARIS, and $G _ { \mathrm { B } }$ represents the transmission gain from the ARIS to GU k. Additionally, $F \left( v , \vartheta \right)$ indicates the normalized power radiation

$$
\begin{array} { r l r } {  { \mathbf { R } [ l ] = \mathbf { R } _ { z } ( \psi [ l ] ) \mathbf { R } _ { y } ( \theta [ l ] ) \mathbf { R } _ { \infty } ( \phi [ l ] ) } } \\ & { } & { = [ \begin{array} { l } { \cos \psi [ l ] \cos \theta [ l ] \cos \psi [ l ] \sin \phi [ l ] \sin \theta [ l ] - \sin \psi [ l ] \cos \phi [ l ] \cos \psi [ l ] \cos \phi [ l ] \sin \theta [ l ] + \sin \psi [ l ] \sin \phi [ l ] } \\ { \sin \psi [ l ] \cos \theta [ l ] \sin \psi [ l ] \sin \phi [ l ] \sin \theta [ l ] + \cos \psi [ l ] \sin \psi [ l ] \cos \phi [ l ] \sin \phi [ l ] \sin \theta [ l ] - \cos \psi [ l ] \sin \phi [ l ] } \\ { - \sin \theta [ l ] } & { \sin \phi [ l ] \cos \theta [ l ] \cos \theta [ l ] } \end{array} ] } \end{array}\tag{18}
$$

pattern of the ARIS, with υ and ϑ denoting the azimuth and elevation angles between GU k (BS) and the ARIS, respectively. This can be modeled using an exponential-Lambertian radiation pattern parameterized by z, which is given by

$$
F \left( v , \vartheta \right) = \left\{ \begin{array} { l l } { \cos ^ { z } \left( \vartheta \right) , } & { v \in \left[ 0 , 2 \pi \right] , \vartheta \in \left[ 0 , \pi \right] , } \\ { 0 , } & { \mathrm { o t h e r w i s e } . } \end{array} \right.\tag{25}
$$

Based on equations (21), (24), and (25), the ARIS’s gain for GU k can is given by

$$
\begin{array} { r } { \pmb { \xi } _ { k } = \left\{ \begin{array} { l l } { D _ { m } ^ { 2 } \big | \mathrm { c o s } \gamma _ { \mathrm { B S } } ^ { \mathrm { R I S } } [ l ] \mathrm { c o s } \gamma _ { k } ^ { \mathrm { R I S } } [ l ] \big | ^ { z } \Theta [ l ] , } & { \mathrm { c o s } \gamma _ { \mathrm { B S } / k } ^ { \mathrm { R I S } } [ l ] > 0 , } \\ { \mathbf { 0 } _ { N \times N } , } & { \mathrm { o t h e r w i s e } . } \end{array} \right. } \end{array}\tag{26}
$$

Therefore, the received signal of GU k is expressed as

$$
y _ { k } [ l ] = \mathbf { v } _ { k } [ l ] \mathbf { w } _ { k } [ l ] x _ { k } [ l ] + \sum _ { j \neq k } ^ { K } \mathbf { v } _ { k } [ l ] \mathbf { w } _ { j } [ l ] x _ { j } [ l ] + n _ { k } ,\tag{27}
$$

where $\begin{array} { r } { { \bf v } _ { k } [ l ] = { \bf h } _ { k } ^ { H } [ l ] \pmb { \xi } _ { k } [ l ] { \bf H } [ l ] + { \bf h } _ { \mathrm { B S } , k } ^ { H } } \end{array}$ denotes the concatenated channel from the BS to GU k, $\mathbf { \bar { w } } _ { k } [ l ] \in \mathbb { C } ^ { M \times 1 }$ is the k-th column of $\mathbf { W } [ l ] \in \mathbb { C } ^ { M \times K }$ , which represents the BS’s beamforming matrix, $x _ { k } [ l ]$ is the transmission signal to GU k, satisfying $\mathbb { E } \left\lceil \left. x _ { k } [ l ] \right. ^ { 2 } \right\rceil = \bar { 1 }$ , and $n _ { k } \sim \mathcal { C N } \left( 0 , \sigma ^ { 2 } \right)$ represents the additive Gaussian noise. Therefore, the achievable rate of GU k is given by

$$
R _ { k } [ l ] = { \log _ { 2 } } \left( 1 + \frac { | \mathbf { v } _ { k } [ l ] \mathbf { w } _ { k } [ l ] | ^ { 2 } } { \sum _ { j \neq k } ^ { K } | \mathbf { v } _ { k } [ l ] \mathbf { w } _ { j } [ l ] | ^ { 2 } + \sigma ^ { 2 } } \right) ,\tag{28}
$$

The total sum-rate of all GUs over all time slots is expressed as

$$
R _ { \mathrm { s u m } } = \sum _ { l = 1 } ^ { L } \sum _ { k = 1 } ^ { K } R _ { k } [ l ] .\tag{29}
$$

## III. PROBLEM FORMULATION AND MARKOV DECISION PROCESS MODEL

In this section, we develop a sum-rate maximization problem that jointly optimizes the ARIS’s altitude, trajectory, phase shifts and BS beamforming. We then model this problem as an MDP framework.

## A. Problem Formulation

As indicated in equation (28), the achievable rate of GU k is determined by the ARIS’s position, altitude, phase shifts, and the BS beamforming. To investigate the impact of ARIS on communications, our goal is to maximize the sum-rate during the ARIS’s flight duration through the joint optimization of the ARIS’s Euler angles Φ, reflection coefficient matrix Θ, and the BS beamforming matrix W. In particular, the optimization problem is formulated as

$$
\operatorname* { m a x } _ { \Phi , { \bf W } , \Theta } { R _ { \mathrm { s u m } } }\tag{30a}
$$

$$
\mathrm { s . t . ~ T r } \left( { \mathbf { W } } ^ { H } [ l ] { \mathbf { W } } [ l ] \right) \leq P _ { \mathrm { B S } } ^ { \mathrm { m a x } } , \forall l \in \mathcal { L } ,\tag{30b}
$$

$$
\varphi _ { \bar { n } } [ l ] \in \left[ 0 , 2 \pi \right) , \forall \bar { n } \in \bar { \mathcal { N } } , \forall l \in \mathcal { L } ,\tag{30c}
$$

$$
\Phi [ l ] \in [ \Phi _ { \operatorname* { m i n } } , \Phi _ { \operatorname* { m a x } } ] , \forall l \in \mathcal { L } ,\tag{30d}
$$

$$
\operatorname* { m a x } \Big \{ | \Phi [ l + 1 ] - \Phi [ l ] | - \tilde { \Phi } _ { \operatorname* { m a x } } \Big \} \leq 0 , l \leq L - 1 ,
$$

$$
E ^ { \mathrm { { f l y } } } \leq E _ { \operatorname* { m a x } } ^ { \mathrm { { f l y } } } ,\tag{30e}
$$

$$
\operatorname* { m i n } \left\{ \mathbf { q } [ l ] - \mathbf { q } _ { l } \right\} \geq 0 , l \in \mathcal { L } ,\tag{30f}
$$

$$
\operatorname* { m a x } \left\{ \mathbf { q } [ l ] - \mathbf { q } _ { r } \right\} \leq 0 , l \in \mathcal { L } ,\tag{30g}
$$

$$
( 1 ) , ( 2 ) .\tag{30h}
$$

(30i)

Constraint (30b) ensures that the transmission power of the BS should not exceed the maximal transmission power. Constraint (30c) defines the feasible range of the ARIS’s phase shifts. Constraints (30d) are established for flight safety consideration where $\Phi _ { \mathrm { m i n } } ~ = ~ \{ - \phi _ { \mathrm { m a x } } , - \theta _ { \mathrm { m a x } } , 0 \} , ~ \Phi _ { \mathrm { m a x } } ~ =$ $\{ \phi _ { \mathrm { m a x } } , \theta _ { \mathrm { m a x } } , 2 \pi \}$ , imposing restrictions on the ARIS’s pitch and roll angles, respectively. Constraint (30e) specifies the allowable variation in Euler angles between consecutive time slots, where $\tilde { \Phi } _ { \mathrm { m a x } } ~ = ~ \{ \tilde { \phi } _ { \mathrm { m a x } } , \tilde { \tilde { \theta } } _ { \mathrm { m a x } } , \tilde { \psi } _ { \mathrm { m a x } } \}$ . Constraint (30f) governs the $\mathrm { U A V } \mathbf { \hat { s } }$ flight energy consumption. Constraints (30g) and (30h) specify that the ARIS can only move within a given range, where $\mathbf { q } _ { l }$ and $\mathbf { q } _ { r }$ represent the two vertices of the rectangular region. Constraint (30i) imposes limitations on the $\mathbf { A R I S } ^ { \prime } \mathbf { s }$ flight speed and acceleration.

Problem (30) presents significant challenges for the following reasons. Firstly, the ARIS’s altitude is intricately coupled with its flight trajectory, and optimizing the $\mathbf { A R I S } ^ { \prime } \mathbf { s }$ altitude inevitably impacts its trajectory. Secondly, the gain of the ARIS is contingent upon the angles of signal incidence and departure, while the variation in ARIS’s altitude and position further exacerbate the computational complexity associated with calculating the actual gain and optimizing the ARIS’s phase shifts. Lastly, in uncertain environments, accurate online decision-making heavily relies on exhaustive environmental sampling during offline training. However, due to the practical limitations on feasible sampling, ensuring worst-case performance and guaranteeing safe online deployment emerge as additional formidable challenges. These factors make problems difficult to solve using traditional convex-based methods. Therefore, we adopt the SAC-PER-based algorithm to tackle these challenges.

## B. MDP Formulation

In implementing DRL, we begin by defining the MDP which serves as the core structure for addressing sequential decision-making in uncertain environments. An MDP is characterized by a five-tuple $\{ \boldsymbol { S } , \mathcal { A } , \mathcal { P } , \mathcal { R } , \gamma \}$ , where $s$ is the set of environment states, A denotes the set of actions, $\mathcal { P }$ signifies the state transition probabilities, R represents the reward function, and γ indicates the discount factor. At each time slot, the agent observes current state $s _ { l } \in S$ and selects an action $a _ { l } \in \mathcal { A }$ following its stochastic policy $\pi ( a _ { l } | s _ { l } ) = P \left[ A _ { l } = a _ { l } | S _ { l } = s _ { l } \right] \in [ 0 , 1 ]$ . After receiving the action $a _ { l }$ , the environment transitions to the state $s _ { l + 1 }$ and feeds back the reward $r _ { l }$ . The specific definitions for the state, action, reward, and state transition in our formulated MDP are provided below.

1) State: At time slot l, the state is denoted by $s _ { l } =$ $\left\{ \Phi [ l ] , \mathbf { q } [ l ] , \mathbf { v } [ l ] , R _ { \mathrm { s u m } } [ l ] , E _ { \mathrm { r e s } } ^ { \mathrm { f i y } } \right\}$ , which include the following five components:

• $\mathrm { \Phi } \Psi [ l ] = \{ \phi [ l ] , \theta [ l ] , \psi [ l ] \}$ : The set of $\mathbf { A R I S } ^ { \prime } \mathbf { s }$ Euler angles at time slot l, including the roll, pitch, and yaw angles, respectively;

$\mathbf { q } [ l ] \colon$ : The position of the ARIS at time slot $l ;$

• $\mathbf { v } [ l ]$ : The velocity of the ARIS at time slot $l ;$

$\begin{array} { r } { \dot { R _ { \mathrm { c u m } } } [ l ] = \sum _ { i = 1 } ^ { l - 1 } \sum _ { k = 1 } ^ { K } R _ { k } [ i ] ; } \end{array}$ : The sum-rate of all GUs from time slot 1 to l − 1;

$E _ { \mathrm { r e m } } ^ { \mathrm { f l y } } [ l ]$ : The remaining flight energy of the ARIS.

2) Action: The formulated MDP’s action space consists of the ARIS’s Euler angles, phase shifts of each sub-surface, and BS beamforming decision at each time slot. Given the above action space, determining the optimal policy poses critical challenges due to the following factors. Firstly, for flight safety considerations, the variation and maximum values of the ARIS’s Euler angles in each time slot are subject to constraints (30e), (30f), and (30g). Directly using Euler angles as optimization variables makes it challenging to simultaneously satisfy both of these constraints. Additionally, the high-dimensional action space and environmental uncertainties render the MDP difficult to solve, as the transition probabilities are unknown, and the curse of dimensionality further complicates the optimization process. To address the above challenging issues, we treat the variation in Euler angles as optimization variables, denoted as $\tilde { \Phi } ~ = ~ \left\{ \tilde { \phi } , \tilde { \theta } , \tilde { \psi } \right\}$ . To satisfy constraint (30g), we impose bounds on their values, i.e. max $\left\{ { \left| \tilde { \Phi } \right| } - \tilde { \Phi } _ { \mathrm { m a x } } \right\} \leq 0 .$ . Furthermore, to meet constraints (30e) and (30f), after the agent selects an action, we adjust the action based on current Euler angles to ensure compliance with these constraints. Additionally, to keep the action relatively small, a low-complexity method is proposed to design the BS beamforming matrix under the given ARIS’s altitude, position, and phase shifts. The details of this approach are presented as follows.

Since the BS beamforming matrix is independent across different time slots, we omit the time slot l in the beamforming matrix derivation for simplicity. At a particular time slot, once the ARIS’s altitude, position and phase shifts are given, the BS beamforming optimization subproblem can be reformulated as

$$
\operatorname* { m a x } _ { \mathbf { W } } R _ { \mathrm { s u m } }\tag{31a}
$$

$$
\mathrm { s . t . } \operatorname { T r } \left( \mathbf { W } ^ { H } \mathbf { W } \right) \leq P _ { \mathrm { B S } } ^ { \operatorname* { m a x } } .\tag{31b}
$$

To address the digital beamforming optimization problem (31), zero-forcing (ZF) precoding, a low-complexity strategy that can effectively eliminate multi-user interference while achieving the near-optimal performance, is employed. The received signal in equation (27) can be rewritten as $\mathbf { y } = \mathbf { V } \mathbf { W } \mathbf { x } + \mathbf { n }$ where we have $\mathbf { y } = [ y _ { 1 } , \ldots , y _ { K } ] ^ { T } , \mathbf { x } = [ x _ { 1 } , \ldots , x _ { K } ] ^ { T }$ V denotes a $K \times M$ matrix with the k-th row being $\mathbf { v } _ { k } ,$ , and n is the noise vector. The ZF beamforming matrix is calculated by

$$
\mathbf { W } = { \mathbf { V } } ^ { H } \left( { \mathbf { V } } { \mathbf { V } } ^ { H } \right) ^ { - 1 } { \mathbf { P } } ^ { \frac { 1 } { 2 } } = { \tilde { \mathbf { V } } } { \mathbf { P } } ^ { \frac { 1 } { 2 } } ,\tag{32}
$$

where $\tilde { \mathbf { V } } = \mathbf { V } ^ { H } \big ( \mathbf { V } \mathbf { V } ^ { H } \big ) ^ { - 1 }$ , and P is a diagonal matrix with the k-th diagonal element being $p _ { k } .$ , calculated by

$$
p _ { k } = \frac { 1 } { \nu _ { k } } \operatorname* { m a x } \left\{ \frac { 1 } { \mu } - \nu _ { k } \sigma ^ { 2 } , 0 \right\} ,\tag{33}
$$

Algorithm 1 Water-Filling and Bisection-Based Algorithm for   
Solving (32)   
Input: $\mathbf { h } _ { \mathrm { R } , k } , \mathbf { h } _ { \mathrm { B S } , k } , \mathbf { H } , \xi _ { k } , \sigma ^ { 2 } , \kappa _ { \mathrm { m i n } } = 1 0 ^ { - 4 }$   
1. Initialization:   
Calculate matrix $\tilde { \mathbf { V } } ^ { H } \tilde { \mathbf { V } }$ and obtain $\nu _ { k }$ for each GU   
Initialize $\mu _ { \mathrm { m a x } } = \mu _ { \mathrm { m i n } } = \mu _ { \mathrm { i n i t } }$   
2. Finding upper and lower bounds for $\mu { : }$   
for $k \leq K$ do   
if $\nu _ { k } \sigma ^ { 2 } \le 1 / \mu _ { \operatorname* { m a x } }$ and $\kappa _ { k } > \kappa _ { \mathrm { m i n } } { \bf t h e n } \mu _ { \mathrm { m a x } } = 1 / \nu _ { k } \sigma ^ { 2 }$   
if $\nu _ { k } \sigma ^ { 2 } > 1 / \mu _ { \mathrm { m i n } }$ and $\kappa _ { k } > \kappa _ { \mathrm { m i n } } { \bf t h e n } \mu _ { \mathrm { m i n } } = 1 / \nu _ { k } \sigma ^ { 2 }$   
end for   
3. Finding the optimal $\mu$ based on bisection method:   
repeat   
Calculate the middle value $\mu _ { \mathrm { m i d } } = \left( \mu _ { \mathrm { m a x } } + \mu _ { \mathrm { m i n } } \right) / 2$   
if $\textstyle \sum _ { k = 1 } ^ { K }$ max $\begin{array} { r } { \left\{ \frac { 1 } { \mu _ { \mathrm { m i d } } } - \nu _ { k } \sigma ^ { 2 } , 0 \right\} > \tilde { P } _ { \mathrm { B S } } ^ { \mathrm { m a x } } } \end{array}$   
then $\mu _ { \mathrm { m i n } } = \mu _ { \mathrm { m i d } }$   
else if $\begin{array} { r } { \cdot \sum _ { k = 1 } ^ { K } \operatorname* { m a x } \Big \{ \frac { 1 } { \mu _ { \mathrm { m i d } } } - \nu _ { k } \sigma ^ { 2 } , 0 \Big \} < P _ { \mathrm { B S } } ^ { \mathrm { m a x } } } \end{array}$   
then $\mu _ { \mathrm { m a x } } = \mu _ { \mathrm { m i d } }$   
else break   
4. Obtaining the optimal beamforming based on (33)

where $\nu _ { k }$ represent the k-th diagonal element of $\widetilde { \mathbf { V } } ^ { H } \widetilde { \mathbf { V } } .$ , and $\mu$ serves as a normalization factor chosen to ensure

$$
\sum _ { k = 1 } ^ { K } \operatorname* { m a x } \bigg \{ \frac { 1 } { \mu } - \nu _ { k } \sigma ^ { 2 } , 0 \bigg \} = P _ { \mathrm { B S } } ^ { \mathrm { m a x } } .\tag{34}
$$

Considering the ARIS’s altitude, some GUs may fall outside the service half-space of ARIS, leading to obstructed communication links between these GUs and the BS. This makes it challenging to determine the feasible bounds of the normalization factor $\mu ,$ causing prohibitively high computational complexity in solving for the optimal $\mu$ via the bisection method. To mitigate this issue, we introduce a service factor $\kappa _ { k }$ prior to conducting the bisection method, given by

$$
\kappa _ { k } [ l ] = \left\{ \begin{array} { l l } { D _ { m } ^ { 2 } \big | \cos \gamma _ { \mathrm { B S } } ^ { \mathrm { R I S } } [ l ] \cos \gamma _ { k } ^ { \mathrm { R I S } } [ l ] \big | ^ { \it z } , } & { \cos \gamma _ { \mathrm { B S } / k } ^ { \mathrm { R I S } } [ l ] > 0 , } \\ { 0 , } & { \mathrm { o t h e r w i s e } . } \end{array} \right.\tag{35}
$$

When $\begin{array} { r } { \kappa _ { k } [ l ] > \kappa _ { \mathrm { m i n } } . } \end{array}$ , the ARIS effectively covers GU k within its half-space. This condition is employed as a criterion when determining the feasible bound for the bisection method. The algorithm is summarized in Algorithm 1.

From equations (32) and (33), the optimal BS beamforming matrix is derived under given ARIS’s altitude, position, and phase shifts. Consequently, in our MDP formulation, only the ARIS’s phase shifts and the variations of Euler angles need to be involved in the action space, while the optimal BS beamforming is determined based on equations (32) and (33) to facilitate state-value computation. Therefore, the action space consists of two components as follows:

$\tilde { \Phi } [ l ] = \left\{ \tilde { \phi } [ l ] , \tilde { \theta } [ l ] , \tilde { \psi } [ l ] \right\}$ : The variation of ARIS’s Euler angles at time slot l;

$\{ \varphi _ { 1 } [ l ] , \dots , \varphi _ { \tilde { n } } [ l ] , \dots , \varphi _ { \tilde { N } } [ l ] \}$ : The phase shifts of ARIS’s sub-surfaces at time slot l.

3) Reward: As stated in (30), the objective of optimizing ARIS’s altitude, trajectory, phase shifts, and BS beamforming matrix is to maximize the sum-rate across all time slots. To align with this objective, the reward guiding the learning should incorporate all GUs’s instantaneous sum-rate at each time slot, namely $\begin{array} { r } { \bar { R } [ l ] = \sum _ { k = 1 } ^ { K } R _ { k } [ l ] } \end{array}$ . To address the flight range constraint, we introduce a penalty $P _ { 1 }$ when the ARIS exits the designated rectangular region. Furthermore, to account for the energy consumption constraint during flight, we incorporate a penalty term ω $E _ { \mathrm { r e s } } ^ { \mathrm { f l y } }$ when the ARIS’s remaining flight energy becomes negative. Finally, to enforce the maximum speed and acceleration constraints during ARIS flight, we introduce penalty terms $P _ { 3 }$ and $P _ { 4 }$ , respectively. Thus, the reward function is defined as follows:

$$
r _ { t } = \left\{ \begin{array} { l l } { \bar { R } [ l ] - P _ { 1 } , } & { \mathrm { i f } \operatorname* { m i n } \left\{ \mathbf { q } [ l ] - \mathbf { q } _ { l } \right\} < 0 , } \\ { \bar { R } [ l ] - P _ { 1 } , } & { \mathrm { i f } \operatorname* { m a x } \left\{ \mathbf { q } [ l ] - \mathbf { q } _ { r } \right\} > 0 , } \\ { \bar { R } [ l ] + \omega E _ { \mathrm { r e s } } ^ { \mathrm { f l y } } , } & { \mathrm { i f } l < L \mathrm { a n d } E _ { \mathrm { r e s } } ^ { \mathrm { f l y } } < 0 , } \\ { \bar { R } [ l ] - P _ { 2 } , } & { \mathrm { i f } \mathbf { v } [ l ] > \mathbf { v } _ { \mathrm { m a x } } , } \\ { \bar { R } [ l ] - P _ { 3 } , } & { \mathrm { i f } \mathbf { a } [ l ] > \mathbf { a } _ { \mathrm { m a x } } . } \end{array} \right.\tag{36}
$$

Note that parameters P<sub>1</sub>, P<sub>2</sub>, $P _ { 3 } ,$ , and $\omega$ should be finely adjusted to enhance both the the expected accumulated reward and convergence performance.

4) State Transition: After the agent selects an action, the state is updated accordingly. Firstly, the ARIS’s Euler angles are updated based on the determined variation, given by

$$
\Phi [ l + 1 ] = \Phi [ l ] + \tilde { \Phi } [ l ] .\tag{37}
$$

Next, the ARIS’s acceleration during this time slot can be computed using equations (7) and (8), and the velocity is updated as

$$
\mathbf { v } [ l + 1 ] = \mathbf { v } [ l ] + \mathbf { a } [ l ] \delta .\tag{38}
$$

Using the updated acceleration, the ARIS’s position is updated by

$$
\mathbf { q } [ l + 1 ] = \mathbf { q } [ l ] + \mathbf { v } [ l ] \delta + \frac { 1 } { 2 } \mathbf { a } [ l ] \delta ^ { 2 } .\tag{39}
$$

Given the ARIS’s altitude and position, the transmission rate for each user can be computed using equation (28), and the cumulative rate is updated by

$$
R _ { \mathrm { c u m } } [ l + 1 ] = R _ { \mathrm { c u m } } [ l ] + \bar { R } [ l ] .\tag{40}
$$

Finally, the ARIS’s flight energy consumption at this time slot can be computed using equation (13), and the remaining flight energy is updated by

$$
\begin{array} { r } { E _ { \mathrm { r e m } } ^ { \mathrm { f l y } } [ l + 1 ] = E _ { \mathrm { r e m } } ^ { \mathrm { f l y } } [ l ] - P ^ { \mathrm { f l y } } [ l ] \delta . } \end{array}\tag{41}
$$

## C. SAC-Based Algorithm

1) SAC Framework: Although DRL has been highly anticipated for real-world applications, its progress remains slow, largely due to limited sampling efficiency and unstable convergence [32]. To address these issues, the SAC framework, grounded in the maximum entropy principle, was introduced to promote sample efficiency in training. Compared with conventional DRL methods, SAC provides multiple benefits, including multi-mode near-optimal policies, more efficient exploration, and faster training speed, particularly for challenging tasks. In standard DRL frameworks, the optimization objective is to maximize the expected cumulative rewards from the initial state. Let the policy π induce a state-action trajectory distribution denoted by $\rho _ { \pi }$ . Thus, the agent’s objective can be expressed as

$$
\operatorname* { m a x } _ { \pi } \sum _ { l = 1 } ^ { L } \mathbb { E } _ { ( s _ { l } , a _ { l } ) \sim \rho _ { \pi } } \left[ \gamma ^ { l - 1 } r ( s _ { l } , a _ { l } ) \right] .\tag{42}
$$

The SAC framework incorporates an entropy term into the objective function to encourage exploration. Specifically, the objective is formulated as

$$
\sum _ { l = 1 } ^ { L } \mathbb { E } _ { ( s _ { l } , a _ { l } ) \sim \rho _ { \pi } } \left[ \gamma ^ { l - 1 } r ( s _ { l } , a _ { l } ) + \alpha \mathcal { H } ( \pi ( \cdot | s _ { l } ) ) \right] ,\tag{43}
$$

where $\begin{array} { r } { \alpha \mathcal { H } ( \pi ( \cdot | s _ { l } ) ) ~ = ~ - \mathbb { E } _ { a \sim \pi ( \cdot | s _ { l } ) } \log _ { 2 } \pi ( a | s _ { l } ) } \end{array}$ denotes the entropy of policy distribution, with the temperature hyperparameter α regulates the weight of the entropy and reflects the degree of stochasticity in the optimal policy $\pi ^ { * }$

The SAC framework is fundamentally based on the policy iteration algorithm, including two primary phases: policy evaluation and policy improvement. Within the evaluation phase, the action values for a given policy π are assessed by the Bellman expectation function, given by $Q _ { \pi } ( s _ { l } , a _ { l } ) =$ $\begin{array} { r } { r ( s _ { l } , a _ { l } ) + \gamma \mathbb { E } _ { s _ { l + 1 } \sim \rho _ { \pi } } \left[ v _ { \pi } ( s _ { l + 1 } ) \right] } \end{array}$ . Compared to the traditional DRL algorithms, by involving the entropy, the state-value function of SAC is given by

$$
v _ { \pi } ( s _ { l } ) = \mathbb { E } _ { a _ { l } \sim \pi } [ Q _ { \pi } ( s _ { l } , a _ { l } ) - \alpha \mathrm { l o g } _ { 2 } ( \pi ( a _ { t } | s _ { l } ) ) ] .\tag{44}
$$

Given that the state space in our proposed MDP is continuous, neural networks are employed to approximate the state values. Let ω represent the parameters of the Q-network. Then, its loss function is expressed as

$$
L _ { Q } ( \omega ) = \mathbb { E } _ { ( s _ { l } , a _ { l } ) \sim \mathcal { D } } \left[ \frac { 1 } { 2 } \left( Q _ { \omega } \left( s _ { l } , a _ { l } \right) - \hat { Q } \left( s _ { l } , a _ { l } \right) \right) ^ { 2 } \right]\tag{45}
$$

where

$$
\begin{array} { l } { { \displaystyle \hat { Q } \left( s _ { l } , a _ { l } \right) = r \left( s _ { l } , a _ { l } \right) + \gamma \sum _ { a _ { l + 1 } \in A } \pi \left( a _ { l + 1 } | s _ { l + 1 } \right) } } \\ { { \displaystyle \qquad \times \left[ Q _ { \hat { \omega } } \left( s _ { l + 1 } , a _ { l + 1 } \right) - \alpha \log \left( \pi \left( a _ { l + 1 } | s _ { l + 1 } \right) \right) \right] } } \end{array}\tag{46}
$$

Here, D represents the replay buffer, ωˆ is the parameter of target Q-network, which is periodically copied from ω.

The policy improvement iteratively enhances the policy π by leveraging real-time Q-values estimated from policy evaluation. The loss function for the network is given by

$$
L _ { \pi } ( \varphi ) = \mathbb { E } _ { s _ { l } \sim \mathcal { D } } \mathbb { E } _ { a _ { l } \sim \pi _ { \varphi } } \left[ \alpha \log _ { 2 } \left( \pi _ { \varphi } \left( a _ { l } \mid s _ { l } \right) \right) - Q _ { \omega } \left( s _ { l } , a _ { l } \right) \right]\tag{47}
$$

2) Temperature Auto-Adjustment: SAC is highly sensitive to the temperature coefficient of entropy, as it controls the balance between reward and entropy, influencing the algorithm’s ability to explore and exploit. In the early state of training, the temperature α should be increased to encourage better exploration. As the training progresses, a smaller α can allow agent to make more effective use of high-quality samples.

In order to accomplish this, we leverage the recursive form of $\mathbb { E } _ { ( s _ { l } , a _ { l } ) \sim \rho _ { \pi } } \left[ \gamma ^ { l - 1 } r ( s _ { l } , a _ { l } ) \right]$ and apply the strong duality principle. Consequently, the optimal dual variable $\alpha _ { l } ^ { \ast }$ is given by

$$
\alpha _ { l } ^ { * } = \arg \operatorname* { m i n } _ { \alpha _ { l } } \mathbb { E } _ { \alpha _ { l } \sim \pi _ { l } ^ { * } } \left[ - \alpha _ { l } \log \left( \pi _ { l } ^ { * } \left( a _ { l } \mid s _ { l } ; \alpha _ { l } \right) \right) - \alpha _ { l } \mathcal { H } _ { \operatorname* { m i n } } \right] ,\tag{48}
$$

where $\pi _ { l } ^ { * } \left( a _ { l } \vert s _ { l } ; \alpha _ { l } \right)$ represents the optimal policy under the temperature $\alpha _ { l } , \ \mathcal { H } _ { \operatorname* { m i n } }$ denotes the minimum-entropy constraint. Therefore, dual gradient descent stands out as a viable approach, with the objective being

$$
L ( \alpha ) = \mathbb { E } _ { a _ { l } \sim \pi _ { l } } \left[ - \alpha \log \left( \pi _ { l } \left( A _ { l } \mid S _ { l } \right) \right) - \alpha \mathcal { H } _ { \operatorname* { m i n } } \right] .\tag{49}
$$

3) Prioritized Experience Replay (PER): In contrast to traditional experience replay mechanisms, we employ PER to improve the training efficiency in DRL frameworks. Specifi cally, each transition is prioritized according to its temporal difference error (TD-error), which quantifies the discrepancy between the value predicted by the current model and the target value of the sample. Transitions with larger TD-error values are deemed more critical for model updates, as they indicate regions where the model’s predictions are less accurate. The implementation of a prioritized sampling mechanism, which selectively experience data based on estimated sample importance, enables more efficient neural network training by focusing computational resources on high-impact transitions.

Taking DQN with PER as an example, the TD-error for each experience tuple is calculated based on the interpolation between the current and target Q values, given by

$$
\delta _ { l } = r \left( s _ { l } , a _ { l } \right) + \gamma Q _ { \mathrm { t a r g e t } } \left( s _ { l + 1 } , a _ { l + 1 } \right) - Q \left( s _ { l } , a _ { l } \right) ,\tag{50}
$$

where $Q _ { \mathrm { t a r g e t } }$ denote the target Q network, and Q is the current Q network. As the SAC algorithm contains two $Q -$ network, the TD-error is set as the mean absolute value of the TD-error for the two Q-network, which is expressed as

$$
| \delta _ { l } | = \frac { 1 } { 2 } \sum _ { i = 1 } ^ { 2 } | Q _ { \omega _ { i } } ( s _ { l } , a _ { l } ) - Q _ { \mathrm { t a r g e t } } ( r _ { l } , s _ { l + 1 } ) | .\tag{51}
$$

Therefore, the sampling probability for sample i is given by

$$
P ( i ) = \frac { p _ { i } ^ { \beta _ { 1 } } } { \sum _ { k } p _ { k } ^ { \beta _ { 1 } } } ,\tag{52}
$$

where $\beta _ { 1 }$ is the distribution factor, and $p _ { i }$ denotes the priority of sample i, calculated by $p _ { i } = | \delta _ { i } | + \varepsilon .$ , with ε denoting a positive constant to prevent the priority $p _ { i }$ from becoming zero. Since the prioritized replay alters sample’s likelihood of being drawn, an importance sampling weight $w _ { i }$ must be introduced to adjust the error updates, given by

$$
w _ { i } = \left( \frac { 1 } { N _ { D } } \cdot \frac { 1 } { P \left( i \right) } \right) ^ { \beta _ { 2 } } ,\tag{53}
$$

where $N _ { D }$ denotes the capacity of the experience replay, $\beta _ { 2 }$ is a constant value for adjusting sampling weight [34], satisfying $\beta _ { 2 } \in [ 0 , 1 ]$ . When $\beta _ { 2 }$ is equal to 0, the importance sampling is not used, and when $\beta _ { 2 }$ is equal to 1, the impact of PER on convergence is completely offset. Fig. 3 and Algorithm 2 illustrate the architecture and training process of proposed SAC-PER algorithm.

Algorithm 2 Our Proposed SAC-PER Algorithm   
1 Initialize the environment.   
2 Initialize critic network parameters $\omega _ { i } ( i = 1 , 2 )$ and actor   
network parameter $\varphi .$   
3 Set entropy level ${ \mathcal { H } } _ { \operatorname* { m i n } } .$ , replay buffer ${ \mathcal { D } } = \emptyset .$ , learning   
rate, temperature parameter $\alpha ,$ and discount factor $\gamma ,$   
respectively.   
4 for each episode do   
5 for each environment step do   
6 Select action $a _ { l }$ based on current policy.   
7 Take action $a _ { l }$ and calculate the ARIS’s altitude and   
position based on equations (37) and (39). Then,   
use equations (21) and (26) to compute the gain   
of ARIS. Finally, apply Algorithm 1 to obtain the   
optimal BS beamforming matrix.   
8 Transmit to the next state $s _ { l + 1 }$ , calculate the reward   
$r _ { l }$ and then store transition tuple $\left\{ s _ { l } , a _ { l } , r _ { l } , s _ { l + 1 } \right\}$ in   
the D.   
9 if Sample size meets the requirement of $N _ { b }$ do   
10 for $b \in B _ { \mathrm { b a t c h } }$ do   
11 Sample i with probability $P _ { i } .$   
12 Calculate importance sampling by (53).   
13 Calculate TD-error $\delta _ { i }$ by (51).   
14 Calculate priority $p _ { i } .$   
15 end for   
16 end if   
17 end for   
18 for each gradient step do   
19 Update critic networks $\omega _ { i }$ by loss function (45):   
$\omega _ { i } \gets \omega _ { i } - \lambda \nabla _ { \omega _ { i } } L _ { Q } \left( \omega _ { i } \right) , i \in \{ 1 , 2 \}$   
20 Update the actor network $\varphi$ by loss function (47):   
$\varphi  \varphi - \lambda \nabla _ { \varphi } L _ { \pi } ( \varphi ) .$   
21 Update temperature α by solving (48):   
$\alpha  \alpha - \lambda \nabla _ { \alpha } L ( \alpha ) .$   
22 Update target network parameter $\hat { \omega } _ { i } \mathrm { : }$   
$\hat { \omega } _ { i } \gets \tau \omega _ { i } + \left( 1 - \tau \right) \hat { \omega } _ { i } , i \in \{ 1 , 2 \}$   
23 end for   
24 end for

## IV. COMPLEXITY ANALYSIS

Within the proposed SAC-PER algorithm, the complexity mainly arises from training actor and critic networks. Specially, the training complexity arises from the forward and backward propagation performed in DNNs. Since the complexity of backward propagation is comparable to that of forward propagation, the time complexity of network training is $\mathcal { O } \left( \sum _ { i = 0 } ^ { I - 1 } l _ { i } l _ { i + 1 } + \sum _ { j = 0 } ^ { J - 1 } \hat { l } _ { j } \hat { l } _ { j + 1 } \right)$ , where $l _ { i }$ denotes the number of neurons within the actor network’s i-th layer while $\hat { l } _ { j }$ is the number of neurons within the critic network’s j-th layer. I and J represent the quantities of fully connected layers for the actor and critic networks, respectively. When PER is introduced, the experience replay complexity increases due to the additional operations required for managing and sampling experiences according to their priorities. Using a SumTree data structure, the time complexity is $\mathcal { O } \left( N _ { b } \log { N _ { D } } \right)$ . Moreover, the complexity for obtain the optimal beamforming of the BS is $O \left( K \right)$ . Therefore, the time complexity for all $N _ { e }$ episodes can be represented as $\mathcal { O } \left( N _ { e } N _ { s } \left( \sum _ { i = 0 } ^ { I - 1 } l _ { i } l _ { i + 1 } + \sum _ { j = 0 } ^ { J - 1 } \hat { l } _ { j } \hat { l } _ { j + 1 } + N _ { b } \log N _ { D } + K \right) \right)$

TABLE I LIST OF VARIABLES
<table><tr><td>Variable</td><td>Description</td></tr><tr><td> $K$ </td><td>The number of GUs</td></tr><tr><td> $N / \bar { N }$ </td><td>The number of ARIS/sub-surface elements</td></tr><tr><td> $M$ </td><td>The number of BS&#x27;s antennas</td></tr><tr><td> $\mathbf { w } _ { k }$ </td><td>The transmission beamforming at the BS for GU k</td></tr><tr><td> $L$ </td><td>Frame size (meter)</td></tr><tr><td> $I _ { 0 }$ </td><td>No-load current (A)</td></tr><tr><td> $U _ { 0 }$ </td><td>No-load voltage (V)</td></tr><tr><td> $R _ { 0 }$ </td><td>Motor resistance (Ω)</td></tr><tr><td> $K _ { v }$ </td><td>Nominal no-load motor constant (rpm/V)</td></tr><tr><td> $K _ { E }$ </td><td> $\begin{array} { r } { K _ { E } \triangleq { \frac { U _ { 0 } - I _ { 0 } R _ { 0 } } { K _ { v } U _ { 0 } } } } \end{array}$  Back-electromotive force constant</td></tr><tr><td> $K _ { T }$ </td><td>Torque constant  $K _ { T } \triangleq 9 . 5 5 K _ { E }$ </td></tr><tr><td> $P _ { \mathrm { { r o c } } } ^ { \mathrm { { m a x } } }$  BS</td><td>The maximum transmission power at the BS (W)</td></tr><tr><td> $T$ </td><td>The duration of flight (s)</td></tr><tr><td> $L$ </td><td>The number of time slots</td></tr><tr><td> $\delta$ </td><td>The length of each time slot (s)</td></tr><tr><td> $v _ { x } / v _ { y } / v _ { z }$ </td><td>The speed of the ARIS on x-/y-/z-axis  $\mathrm { ( m / s ) }$   $\mathrm { ( m / s ^ { 2 } ) }$ </td></tr><tr><td> $a _ { x } / a _ { y } / a _ { z }$ </td><td>The acceleration of the ARIS on x-/y-/z-axis</td></tr><tr><td> $C _ { t }$ </td><td>Thrust coefficient  $\mathrm { ( N / ( r a d / s ) ^ { 2 } ) }$ </td></tr><tr><td> $C _ { m }$ </td><td>Torque coefficient  $( \Nu \cdot \mathrm { m } / ( \mathrm { r a d } / \mathrm { s } ) ^ { 2 } )$ </td></tr><tr><td> $C _ { d x } / C _ { d y } / C _ { d z }$ </td><td>Drag coefficient of x-/y-/z-axis  $\mathrm { ( N / ( m / s ) ^ { 2 } ) }$ </td></tr><tr><td> $\omega _ { i }$ </td><td>Speed of motor  $i \ ( \mathrm { r a d } / \mathrm { s } )$ </td></tr><tr><td> $\phi / \theta / \psi$ </td><td>Roll/pitch/yaw angle (rad)</td></tr><tr><td> $\phi _ { \mathrm { m a x } } / \theta _ { \mathrm { m a x } }$ </td><td>Safety margin for  $\phi / \theta$  (rad)</td></tr><tr><td> $\tilde { \phi } _ { \mathrm { m a x } } / \tilde { \theta } _ { \mathrm { m a x } } / \tilde { \psi } _ { \mathrm { m a x } }$ </td><td>Safety variation for  $\phi / \theta / \psi \ ( \mathrm { r a d } )$ </td></tr><tr><td> $m$ </td><td>Aircraft mass (kg)</td></tr><tr><td> $g$ </td><td>The acceleration of gravity  $\left( \mathrm { m } / \mathrm { s } ^ { 2 } \right)$ </td></tr><tr><td> $\alpha _ { k } ^ { \mathrm { R I S } } / \alpha _ { \mathrm { R S } } ^ { \mathrm { R I S } }$ </td><td>The azimuth from GU  $k / \mathrm { B S }$  to the ARIS (rad)</td></tr><tr><td> $\beta _ { k } ^ { \mathrm { R I S } } / \beta _ { \mathrm { B S } } ^ { \mathrm { R I S } }$ </td><td>The elevation from GU  $k / \mathrm { B } S$  to the ARIS (rad)</td></tr><tr><td> $K _ { 1 } / K _ { 2 }$ </td><td>The Rician factors</td></tr><tr><td> $d _ { \mathrm { R , B } } / d _ { \mathrm { R } , k }$ </td><td>The distance between GU k/BS and the ARIS (m)</td></tr><tr><td> $\rho _ { 0 }$ </td><td>The pass-loss factor at a reference distance (dBm)</td></tr><tr><td> $\alpha _ { 1 } / \alpha _ { 2 }$ </td><td>The pass-loss exponents</td></tr><tr><td> $H$ </td><td>The altitude of ARIS (m)</td></tr><tr><td> $D _ { m }$ </td><td>The maximum directivity of the ARIS</td></tr><tr><td> $G _ { k } / G _ { \mathrm { B } }$ </td><td>The reception/transmission gain</td></tr><tr><td> $R _ { k }$ </td><td>The achievable communication rate of GU k</td></tr></table>

## V. SIMULATION RESULTS

This section provides a comprehensive evaluation of our proposed algorithm for ARIS-assisted communications in terms of the sum-rate. For comparison, the following benchmark schemes are used:

• SAC scheme: We utilize this algorithm to solve the formulated sum-rate maximization problem, which serves as a benchmark to show the superior training efficiency of the PER.

• PPO scheme: This method is a popular and reliable DRL algorithm that uses a stochastic policy, which defines a distribution over actions instead of providing a deterministic policy. PPO utilizes a clipped objective function to ensure stable updates, effectively mitigating abrupt policy changes and enhancing training robustness [35].

• DDPG scheme: This algorithm integrates deep learning with deterministic policy approaches, designed to handle scenarios characterized by high-dimensional state and continuous action spaces [36].

• Fixed RIS scheme: In this scheme, the ARIS is fixed at (60, 60, H) m, where is the center of the GUs. Algorithm 1 and Algorithm 2 are performed for the joint optimization of ARIS phase shifts and beamforming at the BS, aiming to show the advantage of flexible deployment of the ARIS.

• Random phase shift scheme: In this scheme, Algorithm 1 and Algorithm 2 are used to jointly optimize ARIS’s altitude, trajectory, and BS beamforming, while the phase shifts of each ARIS sub-surfaces are randomly generated.

• ARIS without tilting scheme: In this comparative baseline scheme, the UAV employs the proposed Eulerangle-based control method for trajectory optimization, while the onboard RIS maintains a fixed horizontal orientation without angular variation [19].

• Ignoring tilt scheme: In this scheme, the impact of altitude variations is ignored, but the altitude of ARIS still varies during flight.

## A. Simulation Setup

In the simulation, the ARIS is initially positioned at (20, 20, 100) m, while the BS is located at (100, 100, 10) m. The ARIS flies within a 150m × 150m horizontal area bounded by the lower-left corner $\mathbf { q } _ { l } = ( 0 , 0 , 1 0 0 )$ m and upper-right corner $\mathbf { q } _ { l } = ( 1 5 0 , 1 5 0 , 1 0 0 )$ m, with its altitude maintained at 100 m. GUs are randomly distributed across this area. Table II documents the system configurations [37], [38], while Table III lists the proposed SAC-PER hyperparameter settings, both serving as baseline configurations unless specified otherwise.

## B. Performance Evaluation

1) Convergence: To verify the effectiveness of the proposed SAC-PER algorithm, we compare it against the SAC, PPO, and DDPG algorithms in Fig. 4(a). As observed, the proposed algorithm achieves faster convergence and superior overall performance compared to the benchmark algorithms. Specifically, SAC-PER converges at around 150K steps, whereas PPO and SAC require approximately 200K steps, and DDPG fails to achieve satisfactory convergence during the entire training process. Furthermore, upon convergence, SAC-PER achieves a significantly higher reward than that of the PPO, highlighting its superior learning efficiency.

The selection of network parameters plays an important role in DRL. For example, the learning rate significantly affects convergence and network stability. By choosing the appropriate learning rate, the DRL can quickly achieve the desired results. We analyze the impact of learning rate on the SAC-PER algorithm as shown in Fig. 4(b), where the learning rates are set to 0.0001, 0.001, and 0.01, respectively. It can be observed that the best performance is achieved when the learning rate is set to 0.0001, compared to other values. When it is equal to 0.01, the convergence is slow, and it is difficult to converge to a satisfying value, as a large learning rate may cause the step size of each parameter update to be excessively large, resulting in oscillations and instability during the training.

TABLE II SYSTEM PARAMETER
<table><tr><td rowspan=1 colspan=1>Aircraft mass m</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>Transmission power of BS $\overline { { P _ { \mathrm { B S } } ^ { \mathrm { m a x } } } }$ </td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>Safety variation for roll angle $\phi _ { \mathrm { m a x } }$ </td><td rowspan=1 colspan=1> $\pi / 1 2$ </td></tr><tr><td rowspan=1 colspan=1>Acceleration of gravity g</td><td rowspan=1 colspan=1>9.81</td><td rowspan=1 colspan=1>Duration of flight $T$ </td><td rowspan=1 colspan=1>30</td><td rowspan=1 colspan=1>Safety variation for yaw angle $\underline { { \ddot { \theta } _ { \mathrm { m a x } } } }$ </td><td rowspan=1 colspan=1> $\pi / 1 2$ </td></tr><tr><td rowspan=1 colspan=1>Number of GUs K</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>Number of time slots $L$ </td><td rowspan=1 colspan=1>60</td><td rowspan=1 colspan=1>Safety variation for pitch angle $\psi _ { \mathrm { m a x } }$ </td><td rowspan=1 colspan=1>π/12</td></tr><tr><td rowspan=1 colspan=1>Number of ARIS&#x27;s elements N</td><td rowspan=1 colspan=1>40</td><td rowspan=1 colspan=1>Thrust coefficient $\overline { { C _ { t } } }$ </td><td rowspan=1 colspan=1> $\overline { { 4 . 8 4 8 \times 1 0 ^ { - 5 } } }$ </td><td rowspan=1 colspan=1>Nominal no-load motor constant $\overline { { K _ { v } } }$ </td><td rowspan=1 colspan=1>380</td></tr><tr><td rowspan=1 colspan=1>Number of BS&#x27;s antennas M</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>Torque coefficient $\overline { { C _ { m } } }$ </td><td rowspan=1 colspan=1> $\overline { { 8 . 8 9 1 \times 1 0 ^ { - 7 } } }$ </td><td rowspan=1 colspan=1>Pass-loss factor $\rho _ { 0 }$ </td><td rowspan=1 colspan=1>10</td></tr><tr><td rowspan=1 colspan=1>Number of sub-surface&#x27;s elements Ñ</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>Drag coefficient of x-axis $C _ { d x }$ </td><td rowspan=1 colspan=1>0.11</td><td rowspan=1 colspan=1>Maximum speed $\underline { { v _ { \mathrm { m a x } } } }$ </td><td rowspan=1 colspan=1>15</td></tr><tr><td rowspan=1 colspan=1>No-load current $\overline { { I _ { 0 } } }$ </td><td rowspan=1 colspan=1>0.3</td><td rowspan=1 colspan=1>Drag coefficient of y-axis $C _ { d y }$ </td><td rowspan=1 colspan=1>0.11</td><td rowspan=1 colspan=1>Maximum acceleration $\underline { { a _ { \mathrm { m a x } } } }$ </td><td rowspan=1 colspan=1>5</td></tr><tr><td rowspan=1 colspan=1>No-load voltage $\overline { { U _ { 0 } } }$ </td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>Drag coefficient of z-axis $\overline { { C _ { d z } } }$ </td><td rowspan=1 colspan=1>0.2</td><td rowspan=1 colspan=1>Frame size</td><td rowspan=1 colspan=1>0.3</td></tr><tr><td rowspan=1 colspan=1>Motor resistance $\overline { { R _ { 0 } } }$ </td><td rowspan=1 colspan=1>0.4</td><td rowspan=1 colspan=1>Safety margin for roll angle $\phi _ { \mathrm { m a x } }$ </td><td rowspan=1 colspan=1> $\overline { { \pi / 4 } }$ </td><td rowspan=1 colspan=1>pass-loss exponents $\alpha _ { 1 } / \alpha _ { 2 }$ </td><td rowspan=1 colspan=1>2</td></tr><tr><td rowspan=1 colspan=1>The altitude of ARIS H</td><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1>Safety margin for yaw angle $\theta _ { \mathrm { m a x } }$ </td><td rowspan=1 colspan=1> $\overline { { \pi / 4 } }$ </td><td rowspan=1 colspan=1>Rician factors $\overline { { K _ { 1 } , K _ { 2 } } }$ </td><td rowspan=1 colspan=1>10</td></tr></table>

![](images/12fd84d516b046166f42ce5241587f6e07558cf30749c48b186c9aada4cdd753.jpg)  
Fig. 3. The SAC-PER framework.

TABLE III  
HYPERPARAMETERS OF THE ALGORITHM
<table><tr><td rowspan=1 colspan=1>Parameters</td><td rowspan=1 colspan=1>Values</td></tr><tr><td rowspan=1 colspan=1>Episode length</td><td rowspan=1 colspan=1>1000</td></tr><tr><td rowspan=1 colspan=1>Maximum steps in each episode</td><td rowspan=1 colspan=1>1000</td></tr><tr><td rowspan=1 colspan=1>Replay buffer size</td><td rowspan=1 colspan=1> $\overline { { 5 \times 1 0 ^ { 5 } } }$ </td></tr><tr><td rowspan=1 colspan=1>Learning rate for actor network</td><td rowspan=1 colspan=1> $5 \times 1 0 ^ { - 4 }$ </td></tr><tr><td rowspan=1 colspan=1>Learning rate for critic network</td><td rowspan=1 colspan=1> $5 \times 1 0 ^ { - 4 }$ </td></tr><tr><td rowspan=1 colspan=1>Discount factor</td><td rowspan=1 colspan=1>0.99</td></tr><tr><td rowspan=1 colspan=1>Batch size</td><td rowspan=1 colspan=1>256</td></tr></table>

Furthermore, Fig. 4(c) portrays the performance of our proposed SAC-PER algorithm under various random seeds. As observed, the proposed algorithm consistently achieves favorable outcomes across different seeds, which further confirms the applicability of the proposed algorithm for various scenarios.

2) Trajectory: Fig. 5 compares the trajectories of the proposed ARIS scheme with the benchmark where the RIS maintains a fixed horizontal orientation. It can be observed that the proposed scheme’s trajectories deviate more flexibly to maintain favorable alignment with both the BS and GUs under different seed and height. By contrast, the baseline scheme follows a comparatively rigid path, as it does not adapt its orientation to compensate for changing ARIS’s altitude. Specifically, in Figs. 5(a) and 5(c), when $H = 1 0 0 \mathrm { ~ m ~ }$ , the proposed scheme yields a slightly modified yet more targeted flight trajectory that maintains strong communication links with intermediate GUs. Meanwhile, the baseline scheme, due to the horizontal orientation, occasionally takes a less efficient trajectory in terms of balancing the distances to multiple GUs. Similar trends appear in Figs. 5(b) and 5(d), where the proposed scheme more effectively maneuvers toward areas of higher GUs density and better overall channel quality. Hence, allowing the ARIS to adjust its altitude can lead to improved spatial coverage and greater flexibility compared with the baseline schemes.

3) Sum-Rate and RIS Elements: As shown in Fig. 6, the sum-rate steadily increases with the number of ARIS elements N . This trend is intuitive, as a large N provides greater beamforming flexibility, enabling stronger desired signals and more effective suppression of multi-user interference. Moreover, the proposed ARIS scheme outperforms both random phase shifts and fixed RIS schemes in terms of sum-rate, indicating its effectiveness for ARIS’s altitude, trajectory, and phase shifts optimization. Moreover, compared to the benchmark PPO scheme, our proposed SAC-PER algorithm could attain greater sum-rate, up to 14.4%, further demonstrating the advantage of the proposed SAC-PER algorithm in exploration.

![](images/123a85a70c54f115f45f118319a973c5d549cf79687f2eaaa221e38604ec9ce1.jpg)

(a) The convergence performance of different algorithms.  
![](images/1aa4035e5645f25a016d6bc5c693b71102c7ca2919706c296abe3bf886ccd9e4.jpg)

(b) The performance of the proposed SAC-PER algorithm under different learning rates.  
![](images/fd95c05600fe4f51cbbc009ff2a6d111df38f97d16b0e7e8c403590a2ff4755e.jpg)  
(c) The performance of the proposed SAC-PER algorithm under different seeds  
Fig. 4. The performance of proposed algorithm.

4) Sum-Rate and Antennas: In Fig. 7, we evaluate the performance gain of the proposed ARIS scheme under different numbers of BS antennas. Specifically, we set the number of GUs $K \ = \ B .$ . As illustrated in Fig. 7(a), where the number of ARIS element $N ~ = ~ 2 0 0$ , the sum-rate grows as the BS antenna count increases. This is because, under

![](images/1f06230d5b5cfe9f3bdc37e136896d50da49810f1238d6d43686deefaed8d332.jpg)  
(a) H = 100 m, seed=2019.

![](images/6f84159c54ee678c98a6a5255b0006b7a95b13f17842093a1e2460beffa74e09.jpg)  
(b) H = 150 m, seed=2019.

![](images/ecc2f7893599ad0d9a33a021199dbf492e7bfea832be41c773e5245e942f3b9a.jpg)  
(c) $H = 1 0 0$ m, seed=2020.

![](images/5b2ef45036dcd6d17c3f0483262a91e2e16584cc2429f9ae42e3640376579f51.jpg)  
(d) $H = 1 5 0$ m, seed=2020.

Fig. 5. The trajectories of ARIS for different random seed and height, where $K = 8 .$  
![](images/ab48fa4c4a6ea60c4616b0ac60d6cb12ef1597822027166a4bdc8ca1e8c65a83.jpg)  
Fig. 6. The sum-rate versus the number of ARIS elements N, where $M = 8 ,$ $K = 8 .$

ZF precoding, more antennas provide greater spatial degrees of freedom and stronger interference-cancellation capability, thereby improving the overall channel gain. Furthermore, in multi-user systems, a larger number of antennas can better allocate beams to each GU, reducing interference and ultimately enhancing system capacity. Furthermore, we analyze the sum-rate of different schemes under identical number of BS’s antennas but varying maximum transmission power in Fig. 7(b). It is evident that, as the transmission power rises, the performance gain of our proposed scheme becomes increasingly prominent relative to the benchmark schemes. This finding highlights the effectiveness of jointly optimizing the ARIS trajectory, altitude, and phase shifts in further enhancing the overall spectral efficiency, particularly when sufficient transmission power is available.

5) Sum-Rate and GUs: To demonstrate the extensibility of the proposed scheme, we compare the performance of different approaches under different numbers of GUs K. Given the random nature of GUs positions, we fix the random seed for all schemes to 2019, ensuring consistency in GUs distribution at each GUs count. As shown in Fig. 8, when K is relatively small, all three schemes achieve their highest sum-rate. This is because, in the low-GUs regime, the ZF can fully exploit the available spatial degrees of freedom, effectively mitigating multi-user interference to a negligible level. Moreover, in all tested scenarios, the proposed scheme consistently outperforms the baseline methods, further highlighting its superiority.

![](images/f6cfa991cab0659d12a00a8b58a6bb3a46c73fede72cfc46598aa31fcb63d59f.jpg)

(a) The sum-rate versus the number of antennas M, where $N = 2 0 0 .$  
![](images/dd734c65eaddc8a5df19e7cd25240840e146fcb1b6d9561c073cc41fb2b6f53d.jpg)  
(b) The sum-rate versus the maximum power of BS $P _ { \mathrm { B S } } ^ { \mathrm { m a x } }$ , where $M = 8 , N = 4 0 .$

Fig. 7. The sum-rate versus BS antennas and transmission power, where K = 8.  
![](images/66ba677dfe7f17f42306cc85b97d7b70e6b9440da88426fa4ebdd5c9e08d5156.jpg)  
Fig. 8. The sum-rate versus the number of GUs K, where $N = 4 0 , M = 8 ,$ seed = 2019.

![](images/9980fd52718ccb36f0b81a66e90fe5c2891dc4745bb3176ab7ee6b69d1d4ba56.jpg)  
Fig. 9. The sum-rate versus the altitude of ARIS, where $N = 4 0 , M = 8 ,$ ${ \mathrm { s e e d } } = 2 0 1 8 .$

6) Sum-Rate and ARIS Altitude: To clearly compare the performance differences among different ARIS control strategies, we further evaluate the sum-rate of three schemes at various flight altitudes, as illustrated in Fig. 9. The proposed ARIS scheme is compared with two benchmark schemes, namely the ARIS without tilting scheme which maintains a fixed ARIS orientation, and the ignoring tilt scheme which allows altitude variations during flight but neglects the effect of ARIS attitude variations. The proposed scheme exhibits significant advantages, especially at low altitudes, where the impact of altitude-induced angular deviations on signal incidence and reflection is more pronounced. In contrast, the baseline schemes, due to their lack of dynamic attitude adjustment or omission of tilt effects, fail to adapt to such variations and suffer from degraded channel alignment. By integrating an Euler angles-based control mechanism with the SAC-PER algorithm, the proposed scheme jointly optimizes the ARIS’s altitude, trajectory, and phase shifts. This allows the ARIS elements to dynamically align with the optimal signal reflection directions, thereby compensating for misalignment caused by flight perturbations and improving overall channel gain. As a result, the proposed method effectively balances multi-user coverage with directional signal enhancement. These results validate the technical superiority of the altitude-integrated ARIS scheme in dynamic environments and provide theoretical support for the engineering deployment of ARIS systems.

7) Sum-Rate and Flight Energy: To demonstrate the influence of the flight energy consumption, we compare the ARIS’s trajectory and sum-rate under different flight energy budget. As illustrated in Fig. 10(a), the ARIS trajectories exhibit significant variations under three different maximum flight energy constraints, namely 8500 J, 9000 J, and 9500 J. Under the 9500 J energy budget, the ARIS demonstrates more aggressive motion behavior in the initial time slots, characterized by higher acceleration and longer displacement per time slot. This phenomenon arises because, according to equations (7) and (8), a higher acceleration requires larger roll and pitch angles, which, based on equation (13), results in greater flight energy consumption. With a larger power budget, the ARIS is capable of executing more rapid maneuvers despite the higher energy cost. Furthermore, as depicted in Fig. 10(b), the sum-rate increases with the available flight energy. This is attributed to the ARIS reaching favorable positions with higher channel gains more quickly, thereby enhancing the overall communication performance.

![](images/5d9ad112afd657f1fd9b20ad684aec1c661a2f2a1681fcf7461521245c5cde8e.jpg)  
(a) Trajectory versus flight energy.

![](images/1c1341f95936adafa19cf8d0328e5545d741a38ee3fd58bc4714d434acdb27ef.jpg)  
(b) Sum-rate versus flight energy.

Fig. 10. The performance of the proposed scheme under different flight energies.  
![](images/972d250bd98968f91066417821510a5869b8e46a192e845f760a3814b256b001.jpg)  
Fig. 11. The trajectory for the proposed ARIS scheme with uncertainty.

8) Robustness Analysis: In practical scenarios, due to inaccurate positioning information, wind gusts, and other factors, the ARIS may deviate from the scheduled trajectory, which may affect the communication performance. Therefore, in order to adapt to actual scenarios, the unpredictable ARIS trajectory caused by uncertainties should be specially addressed to design a robust ARIS-assisted communications. The uncertainty trajectory can be modeled as

$$
\hat { \mathbf { q } } [ l ] = \mathbf { q } [ l ] + \Delta \mathbf { q } [ l ] , \forall l \in \mathcal { L } ,\tag{54}
$$

where ${ \bf q } [ l ]$ is the scheduled trajectory and $\Delta \mathbf q [ l ]$ is the position error caused by uncertainties. According to [39], the uncertainty can be modeled as a Gaussian random variable, given by

$$
\Delta \mathbf { q } [ l ] \sim { \mathcal { N } } \left( 0 , \varepsilon _ { 0 } ^ { 2 } \mathbf { I } \right) , \forall l \in { \mathcal { L } } ,\tag{55}
$$

where I is a third-order identity matrix corresponding to the three dimensions in space. Note that although we have assumed that the ARIS flight at a fixed height, there are still uncertainties in the vertical dimension. In Fig. 11, we compare the trajectories and it can be seen that the proposed scheme can effectively adapt to the uncertainty caused by factors such as wind gusts.

![](images/e0eefee4c541908cb7dcbbbe54dcf74ebb9503b6ca62421cc96bae61539d3952.jpg)  
(a) The convergence performance.

![](images/8c9c230275080681ae9cb50d0b6640413fce2bc50bc68d011ba85020f8c544dd.jpg)  
(b) The trajectories of ARISs.  
Fig. 12. The performance of the proposed scheme for multi-ARIS, where ${ \mathrm { I } } = 2 .$

9) Multi-ARIS Scenario: Considering that the collaboration between ARISs can further enhance the communication performance and coverage, we further consider the scenario of multi-ARIS-assisted communications. First, we define the set of ARISs as $\begin{array} { r c l } { \mathcal { T } } & { = } & { \{ 1 , \dots , i , \dots , I \} } \end{array}$ . The gain from ARIS i to GU k can still be calculated using equation (26), denoted as $\xi _ { i , k }$ . Notably, since multi-ARIS is introduced, the concatenated channel $\mathbf { v } _ { k }$ defined previously would become $\mathbf { v } _ { k } [ l ] = \sum _ { i = 1 } ^ { I } \mathbf { h } _ { i , k } ^ { H } [ l ] \pmb { \xi } _ { i , k } [ l ] \mathbf { H } _ { i } [ l ] + \mathbf { h } _ { \mathrm { B S } , k } ^ { H }$ . Furthermore, to ensure safe flight of multi-ARIS, we introduce a minimum distance constraint:

$$
\begin{array} { r } { \| \mathbf { q } _ { i } [ l ] - \mathbf { q } _ { j } [ l ] \| ^ { 2 } \geq d _ { \operatorname* { m i n } } ^ { 2 } , \forall i , j \in \mathcal { T } , i \neq j , l \in \mathcal { L } . } \end{array}\tag{56}
$$

We continue to adopt the proposed SAC-PER algorithm to solve this problem. The state space is augmented by incorporating the Euler angles, position, velocity, and remaining flight energy of each ARIS at every time slot. Meanwhile, the action space is extended to include the variations of Euler angles and the phase shifts of each sub-surface. It is worth noting that, due to the introduction of new constraints, the reward function is redesigned to ensure flight safety, given by

$$
r _ { t } = \bar { R } [ l ] - P _ { 4 } , \mathrm { i f } \ \| \mathbf { q } _ { i } [ l ] - \mathbf { q } _ { j } [ l ] \| ^ { 2 } < d _ { \operatorname* { m i n } } ^ { 2 } , \forall i , j \in \mathcal { I } , i \neq j .\tag{57}
$$

where the penalty $\mathrm { P } _ { 4 }$ is introduced to keep all ARIS at a safe distance.

As illustrated in Fig. 12(a), the proposed SAC-PER algorithm maintains strong performance in the multi-ARIS scenario, achieving convergence within approximately 400K steps. Compared to the single-ARIS-assisted case, it yields improved communication performance. Furthermore, Fig. 12(b) depicts the trajectories of two ARISs, which clearly demonstrate the effectiveness of the proposed algorithm in optimizing the trajectories of multiple ARISs while ensuring flight safety.

## VI. CONCLUSION

In this paper, we have investigated an ARIS-assisted wireless communication system, where a quadrotor UAV is equipped with a RIS to enhance signal reflection. Unlike prior works that assume a persistently horizontal RIS, we have incorporated the UAV’s dynamics and developed an Euler-angles-based control framework, enabling simultaneous trajectory and altitude optimization. To maximize the system sum-rate, we have jointly optimized the UAV’s trajectory, RIS phase shifts, and BS beamforming. Given the strong coupling among these variables, the problem was formulated as an MDP, and a deep reinforcement learning algorithm based on SAC-PER was proposed to determine the ARIS’s Euler angles and phase shift. Additionally, the BS beamforming was optimized via a bisection-assisted water-filling algorithm under given actions. Simulation results have demonstrated that the proposed algorithm achieves superior communication performance and converges to high-quality solutions. Importantly, the integration of altitude control into trajectory design has provided a more practical and flexible framework for real-world ARIS deployment. Beyond performance gains, our findings have highlighted that explicitly considering UAV tilt and altitude variations can fundamentally influence UAV control strategies and RIS configuration. On the control side, adaptive UAV flight strategies must dynamically couple altitude variation and trajectory to maintain beam alignment under realistic disturbances. On the RIS side, the configuration should be co-designed with UAV dynamics to achieve stable performance in fluctuating environments. These were often overlooked in conventional ARIS-assisted models. Future research could extend this framework to more challenging settings, including dynamic user mobility, imperfect CSI, and distributed multi-agent learning frameworks.

## REFERENCES

[1] Y. Liu et al., “Reconfigurable intelligent surfaces: Principles and opportunities,” IEEE Commun. Surveys Tuts., vol. 23, no. 3, pp. 1546–1577, 3rd Quart., 2021.

[2] H. Yang, S. Liu, L. Xiao, Y. Zhang, Z. Xiong, and W. Zhuang, “Learning-based reliable and secure transmission for UAV-RIS-assisted communication systems,” IEEE Trans. Wireless Commun., vol. 23, no. 7, pp. 6954–6967, Jul. 2024.

[3] B. Li, Z. Fei, and Y. Zhang, “UAV communications for 5G and beyond: Recent advances and future trends,” IEEE Internet Things J., vol. 6, no. 2, pp. 2241–2263, Apr. 2019.

[4] E. M. Mohamed, S. Hashima, and K. Hatano, “Energy aware multiarmed bandit for millimeter wave-based UAV mounted RIS networks,” IEEE Wireless Commun. Lett., vol. 11, no. 6, pp. 1293–1297, Jun. 2022.

[5] B. Tian, L. Liu, H. Lu, Z. Zuo, Q. Zong, and Y. Zhang, “Multivariable finite time attitude control for quadrotor UAV: Theory and experimentation,” IEEE Trans. Ind. Electron., vol. 65, no. 3, pp. 2567–2577, Mar. 2018.

[6] K. Lee, D. You, H. Noh, and C. Lee, “Robust beamforming for UAV communication with jittering effects,” IEEE Wireless Commun. Lett., vol. 14, no. 1, pp. 48–52, Jan. 2025.

[7] Y. Cheng, W. Peng, C. Huang, G. C. Alexandropoulos, C. Yuen, and M. Debbah, “RIS-aided wireless communications: Extra degrees of freedom via rotation and location optimization,” IEEE Trans. Wireless Commun., vol. 21, no. 8, pp. 6656–6671, Aug. 2022.

[8] P. S. Aung, Y. M. Park, Y. K. Tun, Z. Han, and C. S. Hong, “Energyefficient communication networks via multiple aerial reconfigurable intelligent surfaces: DRL and optimization approach,” IEEE Trans. Veh. Technol., vol. 73, no. 3, pp. 4277–4292, Mar. 2024.

[9] H. Guo, Y.-C. Liang, J. Chen, and E. G. Larsson, “Weighted sum-rate maximization for reconfigurable intelligent surface aided wireless networks,” IEEE Trans. Wireless Commun., vol. 19, no. 5, pp. 3064–3076, May 2020.

[10] Z. Yang et al., “Energy-efficient wireless communications with distributed reconfigurable intelligent surfaces,” IEEE Trans. Wireless Commun., vol. 21, no. 1, pp. 665–679, Jan. 2022.

[11] L. Zhai, Y. Zou, F. Xiao, and J. Zhu, “A Stackelberg game-based energy trading framework for RIS-enhanced wireless powered MEC networks with multiple access points,” IEEE Trans. Commun., vol. 73, no. 9, pp. 7680–7694, Sep. 2025.

[12] J. Xu, Y. Liu, X. Mu, and O. A. Dobre, “STAR-RISs: Simultaneous transmitting and reflecting reconfigurable intelligent surfaces,” IEEE Commun. Lett., vol. 25, no. 9, pp. 3134–3138, Sep. 2021.

[13] X. Mu, Y. Liu, L. Guo, J. Lin, and R. Schober, “Simultaneously transmitting and reflecting (STAR) RIS aided wireless communications,” IEEE Trans. Wireless Commun., vol. 21, no. 5, pp. 3083–3098, May 2022.

[14] H. Zhang et al., “Intelligent omni-surfaces for full-dimensional wireless communications: Principles, technology, and implementation,” IEEE Commun. Mag., vol. 60, no. 2, pp. 39–45, Feb. 2022.

[15] S. Li, B. Duo, X. Yuan, Y.-C. Liang, and M. Di Renzo, “Reconfigurable intelligent surface assisted UAV communication: Joint trajectory design and passive beamforming,” IEEE Wireless Commun. Lett., vol. 9, no. 5, pp. 716–720, May 2020.

[16] X. Liu, Y. Liu, and Y. Chen, “Machine learning empowered trajectory and passive beamforming design in UAV-RIS wireless networks,” IEEE J. Sel. Areas Commun., vol. 39, no. 7, pp. 2042–2055, Jul. 2021.

[17] L. Zhai, Y. Zou, J. Zhu, and Y. Jiang, “RIS-assisted UAV-enabled wireless powered communications: System modeling and optimization,” IEEE Trans. Wireless Commun., vol. 23, no. 5, pp. 5094–5108, May 2024.

[18] X. Liu, Y. Yu, F. Li, and T. S. Durrani, “Throughput maximization for RIS-UAV relaying communications,” IEEE Trans. Intell. Transp. Syst., vol. 23, no. 10, pp. 19569–19574, Oct. 2022.

[19] Y. Liu, B. Duo, Q. Wu, X. Yuan, J. Li, and Y. Li, “Elevation angledependent 3D trajectory design for aerial RIS-aided communication,” IEEE Trans. Intell. Transp. Syst., vol. 25, no. 3, pp. 2696–2702, Mar. 2024.

[20] C. Jiang, H. Zhang, Y. Ren, Z. Han, K.-C. Chen, and L. Hanzo, “Machine learning paradigms for next-generation wireless networks,” IEEE Wireless Commun., vol. 24, no. 2, pp. 98–105, Apr. 2017.

[21] H. Peng and L.-C. Wang, “Energy harvesting reconfigurable intelligent surface for UAV based on robust deep reinforcement learning,” IEEE Trans. Wireless Commun., vol. 22, no. 10, pp. 6826–6838, Oct. 2023.

[22] M. Wu et al., “Deep reinforcement learning-based energy efficiency optimization for RIS-aided integrated satellite-aerial-terrestrial relay networks,” IEEE Trans. Commun., vol. 72, no. 7, pp. 4163–4178, Jul. 2024.

[23] P. S. Aung, L. X. Nguyen, Y. K. Tun, Z. Han, and C. S. Hong, “Aerial STAR-RIS empowered MEC: A DRL approach for energy minimization,” IEEE Wireless Commun. Lett., vol. 13, no. 5, pp. 1409–1413, May 2024.

[24] S. Zeng, H. Zhang, B. Di, Z. Han, and L. Song, “Reconfigurable intelligent surface (RIS) assisted wireless coverage extension: RIS orientation and location optimization,” IEEE Commun. Lett., vol. 25, no. 1, pp. 269–273, Jan. 2021.

[25] J.-B. Wang et al., “Power control and passive beamforming for the STAR-RIS with rotatable angles,” IEEE Trans. Veh. Technol., vol. 73, no. 8, pp. 12121–12125, Aug. 2024.

[26] B. Li, D. Yang, and L. Liu, “Rotatable RIS-assisted edge computing: Orientation, task offloading, and resource optimization,” IEEE Trans. Veh. Technol., vol. 74, no. 8, pp. 13290–13295, Aug. 2025.

[27] D. Yang, B. Li, and D. Niyato, “Energy-aware task offloading for rotatable STAR-RIS-enhanced mobile edge computing systems,” IEEE Internet Things J., vol. 12, no. 12, pp. 20239–20250, Jun. 2025.

[28] W. Wang and W. Zhang, “Jittering effects analysis and beam training design for UAV millimeter wave communications,” IEEE Trans. Wireless Commun., vol. 21, no. 5, pp. 3131–3146, May 2022.

[29] J. Ouyang, Y. Lu, C. Liu, B. Ma, and M. Lin, “Robust beamforming for uplink RSMA in UAV communication systems with jittering,” IEEE Commun. Lett., vol. 29, no. 4, pp. 769–773, Apr. 2025.

[30] B. Xiong, Z. Zhang, C. Pan, and J. Wang, “Performance analysis of aerial RIS auxiliary mmWave mobile communications with UAV fluctuation,” IEEE Wireless Commun. Lett., vol. 13, no. 4, pp. 1183–1187, Apr. 2024.

[31] S. Xu, H. Guo, W. Dong, and B. Lyu, “Optimal elevation and azimuth rotation for RIS-assisted wireless transmission,” IEEE Commun. Lett., vol. 28, no. 12, pp. 2909–2913, Dec. 2024.

[32] J. Zhao, Y. Zhu, X. Mu, K. Cai, Y. Liu, and L. Hanzo, “Simultaneously transmitting and reflecting reconfigurable intelligent surface (STAR-RIS) assisted UAV communications,” IEEE J. Sel. Areas Commun., vol. 40, no. 10, pp. 3041–3056, Oct. 2022.

[33] B. Li, Q. Li, Y. Zeng, Y. Rong, and R. Zhang, “3D trajectory optimization for energy-efficient UAV communication: A control design perspective,” IEEE Trans. Wireless Commun., vol. 21, no. 6, pp. 4579–4593, Jun. 2022.

[34] R. Chai, H. Niu, J. Carrasco, F. Arvin, H. Yin, and B. Lennox, “Design and experimental validation of deep reinforcement learningbased fast trajectory planning and control for mobile robot in unknown environment,” IEEE Trans. Neural Netw. Learn. Syst., vol. 35, no. 4, pp. 5778–5792, Apr. 2024.

[35] M. Sherman, S. Shao, X. Sun, and J. Zheng, “Optimizing AoI in UAV-RIS-assisted IoT networks: Off policy versus on policy,” IEEE Internet Things J., vol. 10, no. 14, pp. 12401–12415, Jul. 2023.

[36] B. Adhikari, A. S. Khwaja, M. Jaseemuddin, A. Anpalagan, and A. Nallanathan, “Energy efficient RIS-assisted UAV networks using twin delayed DDPG technique,” IEEE Trans. Wireless Commun., vol. 23, no. 12, pp. 18423–18439, Dec. 2024.

[37] Q. Han, Z. Liu, H. Su, and X. Liu, “Filter-based disturbance observer and adaptive control for Euler–Lagrange systems with application to a quadrotor UAV,” IEEE Trans. Ind. Electron., vol. 70, no. 8, pp. 8437–8445, Aug. 2023.

[38] Z. T. Dydek, A. M. Annaswamy, and E. Lavretsky, “Adaptive control of quadrotor UAVs: A design trade study with flight evaluations,” IEEE Trans. Control Syst. Technol., vol. 21, no. 4, pp. 1400–1406, Jul. 2013.

[39] X. Tang, H. Zhang, R. Zhang, D. Zhou, Y. Zhang, and Z. Han, “Robust trajectory and offloading for energy-efficient UAV edge computing in industrial Internet of Things,” IEEE Trans. Ind. Informat., vol. 20, no. 1, pp. 38–49, Jan. 2024.

![](images/f05409336046a98650f56dce4b79f12604d2551ed7b01219717ce3f3a4787126.jpg)  
Bin Li (Member, IEEE) received the Ph.D. degree from Beijing Institute of Technology, Beijing, China, in 2019. From 2013 to 2014, he was a Research Assistant with The Hong Kong Polytechnic University, Hong Kong, China. From 2017 to 2018, he was a Visiting Student with the University of Oslo, Oslo, Norway. In 2019, he joined Nanjing University of Information Science and Technology, Nanjing, China. His research interests include UAV communications, reconfigurable intelligent surface, and mobile edge computing.

![](images/eedbd8aa053dbecdfaf67c229ec0edc72e4108cb3bc487b668d528eef6ab3b46.jpg)

![](images/64ae0441952d19dc689954c17721cd82317505ebcb5c28762d50e0d0558b811b.jpg)

![](images/317689c7804289595a3a641141581c6409e3d9c6e79858f730b467b8d9d80025.jpg)

Dongdong Yang received the B.S. degree from Nanjing University of Information Science and Technology, Nanjing, China, in 2023. He is currently pursuing the M.S. degree with the School of Computer Science, Nanjing University of Information Science and Technology, Nanjing, China. His current research interests include reconfigurable intelligent surface, mobile edge computing, and deep reinforcement learning.

Lei Liu (Member, IEEE) received the B.Eng. degree in electronic information engineering from Zhengzhou University, Zhengzhou, China, in 2010, and the M.Sc. and Ph.D. degrees in communication and information systems from Xidian University, Xi’an, China, in 2013 and 2019, respectively. From 2018 to 2019, he was a Visiting Ph.D. Student with the University of Oslo, Oslo, Norway. He is currently an Associate Professor with Guangzhou Institute of Technology, Xidian University. His research interests include intelligent transportation, mobile-edge computing, and the Internet of Things.

Dusit Niyato (Fellow, IEEE) received the B.Eng. degree from the King Mongkut’s Institute of Technology Ladkrabang (KMITL), Thailand, and the Ph.D. degree in electrical and computer engineering from the University of Manitoba, Canada. He is currently a Professor with the College of Computing and Data Science, Nanyang Technological University, Singapore. His research interests are in the areas of mobile generative AI, edge intelligence, quantum computing and networking, and incentive mechanism design.