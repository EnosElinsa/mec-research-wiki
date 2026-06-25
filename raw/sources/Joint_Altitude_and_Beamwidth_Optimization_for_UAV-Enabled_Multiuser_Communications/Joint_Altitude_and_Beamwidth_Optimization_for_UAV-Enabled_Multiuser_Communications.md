# Joint Altitude and Beamwidth Optimization for UAV-Enabled Multiuser Communications

Haiyun He , Shuowen Zhang , Student Member, IEEE, Yong Zeng , Member, IEEE, and Rui Zhang , Fellow, IEEE

Abstract— We study multiuser communication systems enabled by an unmanned aerial vehicle (UAV) that is equipped with a directional antenna of adjustable beamwidth. We propose a flyhover-and-communicate protocol, where the ground terminals are partitioned into disjoint clusters that are sequentially served by the UAV as it hovers above the corresponding cluster centers. We jointly optimize the UAV’s flying altitude and antenna beamwidth for throughput optimization in three fundamental multiuser communication models, namely, UAV-enabled downlink multicasting, downlink broadcasting, and uplink multiple access. Results show that the optimal UAV altitude and antenna beamwidth critically depend on the communication model considered.

Index Terms— UAV communication, altitude optimization, directional antenna, beamwidth optimization, wireless network.

## I. INTRODUCTION

W IRELESS communication assisted by unmanned aerialvehicles (UAVs) is a promising technology to meet the vehicles (UAVs) is a promising technology to meet the highly diversified and dynamic data demands in future wireless systems [1]. Compared to existing technologies such as small cell and satellite communication, UAV-enabled wireless communication has appealing advantages, such as the ability of on-demand and fast deployment, higher capacity due to dominant line-of-sight (LoS) communication links with the ground terminals (GTs), and additional design degrees of freedom by exploiting the fully controllable UAV mobility. Thus, UAV-enabled communication is expected to play a significant role in future wireless systems, especially for applications such as data offloading for cellular base stations (BSs) in temporary hotspot areas, mobile relaying for emergency responses, periodic information dissemination and data collection in large Internet of Things (IoT) networks, etc.

To realize the full potential of UAV-enabled communication, it is crucial to maximally exploit the fully controllable UAV mobility in three-dimensional (3D) space. The horizontal/vertical positions of the UAVs could be optimized for their deployment, leading to various two-dimensional (2D) or 3D UAV placement designs [2]–[8]. Furthermore, the UAVs’ locations could be contiguously adjusted over time to best meet the communication requirement, which leads to the more general UAV trajectory optimization problems [9], [10].

However, the existing works mainly assume that the UAVs are equipped with either omnidirectional antenna or directional

Manuscript received September 9, 2017; revised November 3, 2017; accepted November 6, 2017. Date of publication November 10, 2017; date of current version February 9, 2018. The associate editor coordinating the review of this paper and approving it for publication was K. N. Pappi. (Corresponding author: Yong Zeng.)

The authors are with the Department of Electrical and Computer Engineering, National University of Singapore, Singapore 117583 (e-mail: haiyun.he@u.nus.edu; shuowen.zhang@u.nus.edu; elezeng@ nus.edu.sg; elezhang@nus.edu.sg).

Digital Object Identifier 10.1109/LCOMM.2017.2772254 antenna with fixed beamwidth. In this letter, we consider the new case where the UAV is equipped with a directional antenna whose beamwidth can be adjusted. Note that with contemporary beamwidth tuning technologies [11], antennas with tunable radiation patterns have already been applied for various applications such as satellite communication and remote sensing. For UAV-enabled wireless communication systems with tunable antenna beamwidth, there is in general an interesting trade-off in adjusting the antenna beamwidth of the UAV versus its altitude above a ground position. Specifically, for a given UAV altitude, increasing the antenna beamwidth helps cover more GTs within the antenna’s main lobe, but at the cost of reduced link capacity for each of those GTs due to the reduced antenna gain in the main lobe. On the other hand, for a given antenna beamwidth, an increase in the UAV altitude would cover more GTs, but with lower link capacity for each GT due to the increased link distance.

To optimally resolve such a trade-off, we study in this letter the joint UAV altitude and beamwidth optimization problem for UAV-enabled multiuser communication systems. We propose a practical fly-hover-and-communicate protocol, where the GTs are partitioned into disjoint clusters with the size of each cluster determined by the area projected by the antenna’s main lobe on the ground. Each cluster is then sequentially served by the UAV as it hovers above the corresponding cluster center. Note that although this protocol may be suboptimal in general, it is favorable for practical implementation. We study three fundamental UAV-enabled multiuser communication models, namely, downlink multicasting (MC), where the UAV sends common information to all GTs in each cluster, downlink broadcasting (BC), where the UAV sends independent information to different GTs via frequency division multiple access (FDMA), and uplink multiple access (MAC), where each GT sends independent information to the UAV via FDMA. Our results show that the optimal UAV altitude and antenna beamwidth critically depend on the communication model considered.

## II. SYSTEM MODEL

We consider a UAV-enabled wireless communication system as shown in Fig. 1, where the UAV is deployed as a flying BS at an altitude of H meters (m) to serve K GTs in a large area A of size $A ~ \mathrm { m } ^ { 2 }$ . The GTs are assumed to be uniformly distributed in A with density $\begin{array} { r } { \rho = \frac { K } { A } \operatorname { G T s } / \mathrm { m } ^ { 2 } } \end{array}$ . We assume that the UAV is equipped with a directional antenna of adjustable beamwidth. For simplicity, we assume that the azimuth and elevation half-power beamwidths of the UAV antenna are equal, which are both denoted as 2 in radians (rad), with $\Theta \in \left( 0 , \frac { \pi } { 2 } \right)$ . Moreover, the corresponding antenna gain in direction (θ , ψ)

![](images/a3e5271f22b5e041d608c752fbdc5a6cbaa99896054db9fda36e10a54e4930e3.jpg)

<details>
<summary>text_image</summary>

z
H
A
C
y
x
</details>

Fig. 1. A UAV-enabled outdoor wireless communication system.

is approximately modelled as

$$
G = \left\{ \begin{array}{l l} \frac {G _ {0}}{\Theta^ {2}}, & - \Theta \leq \theta \leq \Theta , - \Theta \leq \psi \leq \Theta \\ g \approx 0, & \text { otherwise }, \end{array} \right. \tag {1}
$$

where $\begin{array} { r } { G _ { 0 } ~ = ~ \frac { 3 0 0 0 0 } { 2 ^ { 2 } } \times \left( \frac { \pi } { 1 8 0 } \right) ^ { 2 } ~ \approx ~ 2 . 2 8 4 6 ; ~ \theta } \end{array}$ and $\psi$ denote the azimuth and elevation angles, respectively [12, eq. (2)– (51)]. Note that g satisfies $\begin{array} { r } { 0 < g \ll \frac { { \bf \dot { G } } _ { 0 } } { \Theta ^ { 2 } } } \end{array}$ in practice, and we assume $g = 0$ for simplicity. On the other hand, we assume that each GT is equipped with an omnidirectional antenna with unit gain. Thus, for any given UAV location, the disk region on the ground that is covered by the antenna’s main lobe with radius $\bar { r } \ = \ H$ tan  corresponds to the ground coverage area of the UAV, as illustrated in Fig. 1. Furthermore, we assume that the GTs are located outdoors in rural areas, and the communication channel between the UAV and each GT is dominated by the LoS path, thus the channel power gain between the UAV and a GT with horizontal distance $r \leq \bar { r }$ to the UAV is given by

$$
h (r) = \frac {\beta_ {0}}{H ^ {2} + r ^ {2}}, \tag {2}
$$

where $\beta _ { 0 }$ denotes the channel power gain at the reference distance $d _ { 0 } = 1 \mathrm { m }$ .

We assume that the area A is sufficiently large such that it can be partitioned into $\begin{array} { r } { N = \frac { A } { A _ { s } } } \end{array}$ As tessellated regular hexagonal cells denoted by $\{ \mathcal { A } _ { i } \} _ { i = 1 } ^ { N }$ for any given √ ${ \bar { r } } ,$ each with equal circumradius $\bar { r }$ and size $\begin{array} { r } { \dot { \mathbf { A } } _ { s } = \frac { 3 \sqrt { 3 } } { 2 } \hat { r } ^ { 2 } } \end{array}$ , as illustrated in Fig. 1. The average number of GTs in each Ai is then given by

$$
K _ {s} = \rho A _ {s} = \frac {3 \sqrt {3}}{2} \rho H ^ {2} \tan^ {2} \Theta . \tag {3}
$$

It is worth noting that the $K _ { s }$ GTs in each Ai all lie within the UAV coverage area when the UAV is hovering above the center of ${ \mathcal { A } } _ { i } ,$ denoted as $C _ { i }$ . Under the proposed flyhover-and-communicate protocol, the UAV sequentially serves the GTs in A by successively flying over $C _ { i } \mathrm { ^ { * } s }$ based on a certain order (e.g., that obtained via algorithms for solving the travelling salesman problem to minimize the total flying distance [13]), and hovering above each $C _ { i }$ for time duration $T _ { i } ~ > ~ 0$ seconds (s) to communicate with the corresponding $K _ { s }$ GTs in $\mathcal { A } _ { i }$ . In this letter, we assume that the UAV flying speed $V _ { m }$ is sufficiently large and the sum hovering time is $\begin{array} { r } { \sum _ { i = 1 } ^ { N } \bar { T } _ { i } \gg \frac { L } { V _ { m } } } \end{array}$ where L denotes the total traveling distance. Thus the mission completion time can be expressed as $\begin{array} { r } { T _ { \mathrm { c o m p l e t i o n } } = \sum _ { i = 1 } ^ { N } T _ { i } + } \end{array}$ $\begin{array} { r } { \frac { L } { V _ { m } } \approx \sum _ { i = 1 } ^ { N } T _ { i } } \end{array}$ Vm Ni =1 Ti .

We assume that the feasible range of altitude H of the UAV is given by $[ H _ { \operatorname* { m i n } } , H _ { \operatorname* { m a x } } ]$ , where $H _ { \operatorname* { m i n } } > 0$ and $H _ { \operatorname* { m a x } } > H _ { \operatorname* { m i n } }$ are practically determined by e.g., obstacle heights and authority regulations; and the feasible range of half-beamwidth  is assumed to be $[ \Theta _ { \mathrm { m i n } } , \Theta _ { \mathrm { m a x } } ]$ , where $\Theta _ { \mathrm { m i n } } > 0$ and $\Theta _ { \mathrm { m i n } } <$ < $\Theta _ { \mathrm { m a x } } < \frac { \pi } { 2 }$ are determined by the practical antenna beamwidth tuning technique adopted (e.g., [11]). For all multiuser systems considered, we denote W as the total communication bandwidth in Hz; $P _ { d }$ in watt (W) as the transmission power at the UAV for the two downlink cases (MC and BC) and $P _ { u }$ as the transmission power by each GT for the uplink case (MAC). Furthermore, $N _ { 0 }$ denotes the noise power spectrum density at all receivers in W/Hz.

## III. DOWNLINK MULTICASTING

In this section, we consider the case of downlink MC, where the UAV has a mission to deliver a common file of total size $\bar { D }$ bits to all GTs in A. Our objective is to minimize the mission completion time by jointly optimizing H and . As clarified in Section II, the mission completion time can be approximated by $\begin{array} { r } { T _ { \mathrm { M C } } \approx \sum _ { i = 1 } ^ { N } T _ { i } } \end{array}$ .

When the UAV hovers above $C _ { i } ,$ , the received signal-tonoise ratio (SNR) at a GT with distance r to $C _ { i }$ is given by

$$
\gamma_ {\mathrm{MC}} (r) = \frac {P _ {d} G h (r)}{N _ {0} W} = \frac {\alpha}{\Theta^ {2} (H ^ {2} + r ^ {2})}, \quad 0 \leq r \leq \bar {r}, \tag {4}
$$

where $\begin{array} { r } { \alpha = \frac { P _ { d } G _ { 0 } \beta _ { 0 } } { N _ { 0 } W } } \end{array}$ PdG0β0N W . The corresponding achievable communi-0 cation rate is thus given by $R _ { \mathrm { M C } } ( r ) = \log _ { 2 } ( 1 + \gamma _ { \mathrm { M C } } ( r ) )$ in bits per second per Hz (bps/Hz). By noting that $R _ { \mathrm { M C } } ( r )$ is a decreasing function of r, it follows that the common file can be completely delivered to all GTs in $\mathcal { A } _ { i }$ if Ti W $\cdot { \cal R } _ { \mathrm { M C } } ( \bar { r } ) \geq \bar { D }$ holds, with $R _ { \mathrm { M C } } ( \bar { r } )$ denoting the achievable rate of the celledge GT. Hence, the mission completion time for downlink MC with the proposed scheme can be written as

$$
T _ {\mathrm{MC}} = \frac {N \bar {D}}{W R _ {\mathrm{MC}} (\bar {r})} = \frac {\frac {K \bar {D}}{W}}{K _ {s} R _ {\mathrm{MC}} (\bar {r})} = \frac {\frac {K \bar {D}}{W}}{\tilde {R} _ {\mathrm{MC}}}. \tag {5}
$$

Consequently, $T _ { \mathrm { M C } }$ is minimized by maximizing $\tilde { R } _ { \mathrm { M C } } \ \stackrel { \Delta } { = }$ $K _ { s } R _ { \mathrm { M C } } ( \bar { r } )$ , which can be explicitly expressed as

$$
\tilde {R} _ {\mathrm{MC}} (H, \Theta) = \frac {3 \sqrt {3}}{2} \rho H ^ {2} \tan^ {2} \Theta \log_ {2} \left(1 + \frac {\alpha \cos^ {2} \Theta}{\Theta^ {2} H ^ {2}}\right). \tag {6}
$$

It is worth noting that as H or  increases, $K _ { s }$ given in (3) increases, while $R _ { \mathrm { M C } } ( \bar { r } )$ decreases. To balance the above trade-off and find the optimal H and  for maximizing $\tilde { R } _ { \mathrm { M C } } ( H , \Theta )$ , we present the following results.

Proposition 1: For any given $\Theta \in [ \Theta _ { \operatorname* { m i n } } , \Theta _ { \operatorname* { m a x } } ] , \tilde { R } _ { \operatorname { M C } } ( H , \Theta )$ is a non-decreasing function of H , with $H > 0$ .

Proof: Define $\begin{array} { r } { \tilde { \alpha } _ { 1 } ~ = ~ \frac { \alpha \cos ^ { 2 } \Theta } { \Theta ^ { 2 } } , \tilde { \alpha } _ { 2 } ~ = ~ \frac { 3 \sqrt { 3 } } { 2 \ln 2 } \rho \tan ^ { 2 } } \end{array}$ α cos2  2 2 ln 2 ρ tan2  and 3  3 $\tilde { \cal H } \ = \ \cal H ^ { 2 }$ wn that, which i $\operatorname* { l i m } _ { { \tilde { H } }  \infty } \frac { \partial { \tilde { R } } _ { \mathrm { M C } } ( H , \Theta ) } { \partial { \tilde { H } } } ~ = ~ 0$ = 0, $\begin{array} { r } { \frac { \partial ^ { 2 } \tilde { R } _ { \mathrm { M C } } ( H , \Theta ) } { \partial \tilde { H } ^ { 2 } } = \frac { - \tilde { \alpha } _ { 1 } ^ { 2 } \tilde { \alpha } _ { 2 } } { \tilde { H } ( \tilde { \alpha } _ { 1 } + \tilde { H } ) ^ { 2 } } < 0 } \end{array}$ $\begin{array} { r } { \frac { \partial \tilde { R } _ { \mathrm { M C } } ( H , \Theta ) } { \partial \tilde { H } } \geq } \end{array}$ $0 , \forall \tilde { H } > 0 .$

Proposition 1 implies that for any given , the optimal H $H _ { \mathrm { M C } } ^ { \star } = H _ { \mathrm { m a x } }$ . This is because as H grows, the increase in $K _ { s }$ is more significant than the decrease in $R _ { \mathrm { M C } } ( \bar { r } )$ .

Next, we investigate the effect of  on $\tilde { R } _ { \mathrm { M C } } ( H , \Theta )$ with given $H = H _ { \operatorname* { m a x } }$ . However, due to the complicated expression of the derivative of $\tilde { R } _ { \mathrm { M C } } ( H , \Theta )$ with respect to , it is generally difficult to obtain a closed-form solution of the optimal  to maximize $\tilde { R } _ { \mathrm { M C } } ( H , \Theta )$ , which is denoted as $\Theta _ { \mathrm { M C } } ^ { \star } .$ . As a result, $\Theta _ { \mathrm { M C } } ^ { \star }$ needs to be obtained via a one-dimensional search over $[ \Theta _ { \mathrm { m i n } } , \Theta _ { \mathrm { m a x } } ] .$ , for which the numerical results will be given later in Section VI. Nevertheless, it can be shown√ from (6) that limH→∞ $\begin{array} { r } { \tilde { R } _ { \mathrm { M C } } ( H , \Theta ) = \frac { 3 \sqrt { 3 } } { 2 } \rho \alpha \frac { \sin ^ { 2 } \Theta } { \Theta ^ { 2 } } } \end{array}$ 2 , which yields MC $\Theta _ { \mathrm { M C } } ^ { \star } = \Theta _ { \mathrm { m i n } }$ , since Thus, $\frac { \sin ^ { 2 } \Theta } { \Theta ^ { 2 } }$ ecreasing function ofis sufficiently large, $\Theta , \ : 0 \ : < \ : \Theta \ : < \ : \frac { \pi } { 2 }$ $H _ { \mathrm { m a x } }$ the corresponding optimal beamwidth is $\Theta _ { \mathrm { M C } } ^ { \star } = \Theta _ { \mathrm { m i n } } .$ .

## IV. DOWNLINK BROADCASTING

Next, we consider the case of downlink BC where the UAV needs to send independent information to each of the GTs in A. Our objective is to maximize the $\mathrm { G T s } ^ { \prime }$ sum throughput within a given period $T _ { \mathrm { B C } }$ (in s) via joint optimization of H and . Let the sum rate of all GTs in each cell $\mathcal { A } _ { i }$ be denoted by RBC in bps/Hz. Then the total throughput of all cells is given by $\begin{array} { r } { D _ { \mathrm { B C } } = \sum _ { i = 1 } ^ { N } T _ { i } W R _ { \mathrm { B C } } = T _ { \mathrm { B C } } W \bar { R } _ { \mathrm { B C } } } \end{array}$ in bits. Hence, maximizing $D _ { \mathrm { B C } }$ is equivalent to maximizing $R _ { \mathrm { B C } }$ . Note that a closed-form expression of $R _ { \mathrm { B C } }$ is generally difficult to obtain since it involves integration of GT rates over uniform distribution in the hexagonal cell Ai . For analytical tractability, we assume that when the UAV hovers above each $C _ { i }$ , it serves all GTs within the disk region $\mathcal { A } _ { i } ^ { \prime }$ centered at $C _ { i }$ with the same radius r¯ as $\mathcal { A } _ { i }$ , as shown in Fig. 1, which is of size ${ A _ { s } ^ { \prime } = } \pi \bar { r } ^ { 2 }$ . Thus, there are on average $\bar { K _ { s } ^ { \prime } } = \rho A _ { s } ^ { \prime } = \rho \pi H ^ { 2 } \tan ^ { 2 } \Theta$ GTs in $\mathcal { A } _ { i } ^ { \prime } ,$ whose sum rate is denoted by $\tilde { R } _ { \mathrm { B C } }$ in bps/Hz. In the sequel, we aim to maximize $\tilde { R } _ { \mathrm { B C } }$ as an approximation of $R _ { \mathrm { B C } }$ .

We assume FDMA for the $K _ { s } ^ { \prime }$ GTs to be simultaneously served by the UAV in each $\mathcal { A } _ { i } ^ { \prime } .$ , where each GT is allocated with an equal bandwidth $\frac { W } { K _ { s } ^ { \prime } }$ . Moreover, we consider the equal power allocation scheme, where the total UAV downlink transmission power $P _ { d }$ is equally allocated to the $K _ { s } ^ { \prime }$ GTs in each $\mathcal { A } _ { i } ^ { \prime }$ . Thus, when the UAV hovers above $C _ { i }$ , the received SNR at a GT with distance r to $C _ { i }$ is given by

$$
\gamma_ {\mathrm{BC}} (r) = \frac {\frac {P _ {d}}{K _ {s} ^ {r}} G h (r)}{N _ {0} \frac {W}{K _ {s} ^ {r}}} = \frac {\alpha}{\Theta^ {2} (H ^ {2} + r ^ {2})}, \quad 0 \leq r \leq \bar {r}. \tag {7}
$$

The corresponding GT rate is then given by $R _ { \mathrm { B C } } ( r ) ~ =$ $\begin{array} { r l r } { \frac { 1 } { K _ { s } ^ { \prime } } \log _ { 2 } { ( 1 + \gamma _ { \mathrm { B C } } ( r ) ) } } & { = } & { \frac { \log _ { 2 } { \left( 1 + \frac { \alpha } { \Theta ^ { 2 } ( H ^ { 2 } + r ^ { 2 } ) } \right) } } { \rho \pi H ^ { 2 } \tan ^ { 2 } { \Theta } } } \end{array}$ bps/Hz. Hence, the total communication rate of all GTs in $\mathcal { A } _ { i } ^ { \prime }$ is given by

$$
\begin{array}{l} \tilde {R} _ {\mathrm{BC}} (H, \Theta) \\ = \int_ {0} ^ {2 \pi} \int_ {0} ^ {H \tan \Theta} \rho R _ {\mathrm{BC}} (r) r d r d \theta \\ = \frac {1}{\sin^ {2} \Theta} \log_ {2} \left(1 + \frac {\alpha \cos^ {2} \Theta}{\Theta^ {2} H ^ {2}}\right) - \frac {1}{\tan^ {2} \Theta} \log_ {2} \left(1 + \frac {\alpha}{\Theta^ {2} H ^ {2}}\right) \\ + \frac {\alpha}{\Theta^ {2} H ^ {2} \tan^ {2} \Theta} \log_ {2} \left(\frac {\Theta^ {2} H ^ {2} + \alpha \cos^ {2} \Theta}{\Theta^ {2} H ^ {2} \cos^ {2} \Theta + \alpha \cos^ {2} \Theta}\right). \tag {8} \\ \end{array}
$$

Note that there exists a trade-off between the individual GT rate, $R _ { \mathrm { B C } } ( r )$ , and the number of GTs in $\mathcal { A } _ { i } ^ { \prime } , \ K _ { s } ^ { \prime }$ , which are decreasing and increasing functions of both H and , respectively. To obtain the optimal H and  to maximize $\tilde { R } _ { \mathrm { B C } } ( H , \Theta )$ , we provide the following proposition.

Proposition 2: For any given $\Theta \in [ \Theta _ { \operatorname* { m i n } } , \Theta _ { \operatorname* { m a x } } ] , \ \tilde { R } _ { \mathrm { B C } } ( H , \Theta )$ is a decreasing function of $H _ { ; }$ , with $H > 0$ .

Proof: Let $\tilde { H } = H ^ { 2 }$ . It can be shown that $\begin{array} { r } { \frac { \partial \tilde { R } _ { \mathrm { B C } } ( H , \Theta ) } { \partial \tilde { H } } = } \end{array}$ $\begin{array} { r } { \frac { \alpha } { \tilde { H } ^ { 2 } \Theta ^ { 2 } \tan ^ { 2 } \Theta } \left( \log _ { 2 } \left( \tilde { H } + \frac { \alpha } { \Theta ^ { 2 } } \right) - \log _ { 2 } \left( \frac { \tilde { H } } { \cos ^ { 2 } \Theta } + \frac { \alpha } { \Theta ^ { 2 } } \right) \right) } \end{array}$ which is negative since $\cos ^ { 2 } \Theta < 1$ for any $\Theta \in [ \Theta _ { \operatorname* { m i n } } , \Theta _ { \operatorname* { m a x } } ]$ .

Proposition 2 indicates that given any , the optimal H in the downlink BC case is $H _ { \mathrm { B C } } { } ^ { \star } = H _ { \operatorname* { m i n } }$ , which is in sharp contrast to the previous case of downlink MC in Section III. This can be intuitively explained as follows. Note that due to the bandwidth partitioning for FDMA, as H increases, each individual GT rate in downlink BC decreases more quickly than that in downlink MC, since in the BC case each GT is assigned smaller portion of the total bandwidth and less power with the increasing number of GTs served. On the other hand, due to the difficulty in deriving a closed-form expression of the optimal  from (8), we examine the effect of the beamwidth  on $\tilde { R } _ { \mathrm { B C } } ( H , \Theta )$ numerically in Section VI.

## V. UPLINK MULTIPLE ACCESS

Last, we consider the case of uplink MAC, where each GT in A needs to send independent information to the UAV. Our objective is to maximize the GTs’ sum throughput within a given period $T _ { \mathrm { M A C } }$ (in s) by jointly optimizing H and . Similar to the case of downlink BC in Section IV, we assume that the UAV serves all $K _ { s } ^ { \prime }$ GTs in $\mathcal { A } _ { i } ^ { \prime }$ via FDMA with equal bandwidth allocation over the served GTs, thus the sum throughput is maximized by maximizing the total communication rate of all GTs in $\mathcal { A } _ { i } ^ { \prime } ,$ , denoted as $\tilde { R } _ { \mathrm { M A C } }$ .

When the UAV hovers above $C _ { i } ,$ the received SNR at the UAV from a GT with distance r to $C _ { i }$ is given by

$$
\gamma_ {\mathrm{MAC}} (r) = \frac {P _ {u} h (r) G}{N _ {0} \frac {W}{K _ {s} ^ {\prime}}} = \frac {\eta H ^ {2} \tan^ {2} \Theta}{\Theta^ {2} (H ^ {2} + r ^ {2})}, \quad 0 \leq r \leq \bar {r}, \tag {9}
$$

where $\begin{array} { r } { \eta \ : = \ : \frac { P _ { u } \beta _ { 0 } G _ { 0 } \rho \pi } { N _ { 0 } W } } \end{array}$ Puβ0G0ρπ . The corresponding GT rate is given N0W by $\begin{array} { r } { R _ { \mathrm { M A C } } ( r ) = \frac { 1 } { K _ { \cdot } ^ { \prime } } \log _ { 2 } { ( 1 + \gamma _ { \mathrm { M A C } } ( r ) ) } } \end{array}$ bps/Hz, which can be s shown to decrease as H or  increases, since the decrease in $\frac { 1 } { K _ { s } ^ { \prime } }$ is more significant than the increase in log2 $( 1 + \gamma _ { \mathrm { M A C } } ( r ) )$ . The total rate of all GTs in $\mathcal { A } _ { i } ^ { \prime }$ is given by

$$
\begin{array}{l} \tilde {R} _ {\mathrm{MAC}} (H, \Theta) \\ = \int_ {0} ^ {2 \pi} \int_ {0} ^ {H \tan \Theta} \rho R _ {\mathrm{MAC}} (r) r d r d \theta \\ = \frac {1}{\tan^ {2} \Theta} \left[ \frac {1}{\cos^ {2} \Theta} \log_ {2} \left(1 + \frac {\eta \sin^ {2} \Theta}{\Theta^ {2}}\right) - \log_ {2} \left(1 + \frac {\eta \tan^ {2} \Theta}{\Theta^ {2}}\right) \right. \\ \left. + \frac {\eta \tan^ {2} \Theta}{\Theta^ {2}} \log_ {2} \left(1 + \frac {\Theta^ {2} \tan^ {2} \Theta}{\Theta^ {2} + \eta \tan^ {2} \Theta}\right) \right]. \tag {10} \\ \end{array}
$$

Note that interestingly, $\tilde { R } _ { \mathrm { M A C } } ( H , \Theta )$ is independent of H , since as H grows, the decrease in $R _ { \mathrm { M A C } } ( r )$ equally compensates the increase in $K _ { s } ^ { \prime }$ in (10). On the other hand, similar to the previous two cases, we will investigate the optimal , $\Theta _ { \mathrm { M A C } } ^ { \star } ,$ to maximize $\tilde { R } _ { \mathrm { M A C } } ( H , \Theta ) = \tilde { R } _ { \mathrm { M A C } } ( \Theta )$ regardless of H via numerical examples in the next section.

![](images/2aa2ed323b194239f67af44a5fc77baa71ac6d3992e8d787dd02aa4461c8c327.jpg)

<details>
<summary>line chart</summary>

| Θ (rad) | H=500m | H=1500m | H=2500m | H=3500m | H=4500m |
| ------- | ------ | ------- | ------- | ------- | ------- |
| 0.0     | 0.0000 | 0.0000  | 0.0000  | 0.0000  | 0.0000  |
| 0.2     | 0.0100 | 0.0200  | 0.0300  | 0.0400  | 0.0600  |
| 0.4     | 0.0200 | 0.0400  | 0.0600  | 0.1000  | 0.1500  |
| 0.6     | 0.0300 | 0.0600  | 0.1000  | 0.1800  | 0.2200  |
| 0.8     | 0.0400 | 0.1000  | 0.1500  | 0.2500  | 0.2800  |
| 1.0     | 0.0500 | 0.1500  | 0.2200  | 0.2800  | 0.3200  |
| 1.2     | 0.1500 | 0.2200  | 0.2800  | 0.2900  | 0.3100  |
| 1.4     | 0.2500 | 0.2800  | 0.2900  | 0.2700  | 0.2800  |
| 1.6     | 0.3500 | 0.3200  | 0.2700  | 0.2400  | 0.2400  |
</details>

Fig. 2. $\tilde { R } _ { \mathrm { M C } }$ versus $\Theta$ under different H values in downlink MC.  
![](images/e86960bce3fef6474f4b9922b7d36f87e8e2f21d63cacf328cf71d17e5a31fa1.jpg)

<details>
<summary>line chart</summary>

| H (m) | R̃_BC analytical | R̃_BC simulation |
|-------|-----------------|-----------------|
| 0     | 15.0            | 15.0            |
| 500   | 10.0            | 10.0            |
| 1000  | 8.5             | 8.5             |
| 1500  | 7.5             | 7.5             |
| 2000  | 6.5             | 6.5             |
| 2500  | 6.0             | 6.0             |
| 3000  | 5.5             | 5.5             |
| 3500  | 5.0             | 5.0             |
| 4000  | 4.5             | 4.5             |
| 4500  | 4.0             | 4.0             |
</details>

(a)Θ=1rad  
![](images/155507dd01f4294036d3b592f6d9aedfffc73692369dc051b346f072b31f3666.jpg)

<details>
<summary>line chart</summary>

| Θ (rad) | RBC analytical | RBC simulation |
| ------- | -------------- | -------------- |
| 0.0     | 15.0           | 15.0           |
| 0.2     | 12.0           | 12.0           |
| 0.4     | 9.0            | 9.0            |
| 0.6     | 7.5            | 7.5            |
| 0.8     | 6.5            | 6.5            |
| 1.0     | 5.5            | 5.5            |
| 1.2     | 4.5            | 4.5            |
| 1.4     | 3.0            | 3.0            |
| 1.6     | 1.0            | 1.0            |
</details>

(b)H= 500m  
Fig. 3. $\tilde { R } _ { \mathrm { B C } }$ versus H or  in downlink BC.

## VI. NUMERICAL RESULTS

In this section, we provide numerical results to validate our analysis. We consider $\beta _ { 0 } = 1 . 4 2 \times 1 0 ^ { - 4 } , \ W = 1 0 \mathrm { M H z } ,$ $P _ { d } ~ = ~ 1 0 \mathrm { { d B m } }$ , $P _ { u } ~ = ~ - 1 0 \mathrm { d B m }$ , $N _ { 0 } = - 1 6 9 \mathrm { d B m / H z } ,$ and $\rho { = } 0 . 0 0 5 ~ \mathrm { G T s } / \mathrm { m } ^ { 2 }$ , unless specified otherwise.

First, we consider the case of downlink MC and plot $\tilde { R } _ { \mathrm { M C } }$ given in (6) versus  under different values of H in Fig. 2. It can be observed that for any given $\Theta , \tilde { R } _ { \mathrm { M C } }$ increases with H , thus validating Proposition 1. Moreover, it is observed that given any H , $\tilde { R } _ { \mathrm { M C } }$ first increases and then decreases as  increases from 0 to $\textstyle { \frac { \pi } { 2 } } ;$ ; while the optimal $\Theta _ { \mathrm { M C } } ^ { \star }$ that maximizes $\tilde { R } _ { \mathrm { M C } }$ is shown to be non-increasing with H , which is consistent $\Theta _ { \mathrm { M C } } ^ { \star } = \Theta _ { \mathrm { m i n } }$ H→∞

Next, we consider the case of downlink BC. In Fig. 3, we plot the analytical results of $\tilde { R } _ { \mathrm { B C } }$ given in (8), versus H with fixed $\Theta = \frac { \pi } { 1 0 }$ rad or versus  with fixed $H = 5 0 0 \mathrm { m }$ . We also plot the simulation results of $\tilde { R } _ { \mathrm { B C } }$ obtained by averaging over 100 independent realizations of GT locations, which are observed to match closely with the analytical results in Section IV. It is also observed that $\tilde { R } _ { \mathrm { B C } }$ decreases with H as well as , which is consistent with our analysis in Section IV and suggests that smaller H or  is desirable for maximizing $\tilde { R } _ { \mathrm { B C } }$ .

Last, we consider the case of uplink MAC. In Fig. 4, we plot both the analytical and simulation results for $\tilde { R } _ { \mathrm { M A C } }$ given in (10) versus  with arbitrary H and $\rho ~ =$ 0.001, 0.005 or 0.01 GTs/m2. It is observed that the analytical and simulation results match well. Moreover, for each given $\rho ,$ $\tilde { R } _ { \mathrm { M A C } }$ first increases and then decreases as  increases from 0 to ${ \frac { \pi } { 2 } } .$ , and the optimal $\Theta _ { \mathrm { M A C } } ^ { \star }$ that maximizes $\tilde { R } _ { \mathrm { M A C } }$ is almost the same for different values of $\rho _ { ; }$ , which is 1.3195 (or 79.7271 in degree) if $1 . 3 1 9 5 \in [ \Theta _ { \operatorname* { m i n } } , \Theta _ { \operatorname* { m a x } } ]$ , as indicated in Fig. 4.

![](images/95a8190dada077359301044ac92dcf3aa28174bbeb65d135771c69bb30f0edc4.jpg)

<details>
<summary>line chart</summary>

| Θ (rad) | ρ = 0.001 analytical | ρ = 0.001 simulation | ρ = 0.005 analytical | ρ = 0.005 simulation | ρ = 0.010 analytical | ρ = 0.010 simulation |
| ------- | --------------------- | --------------------- | --------------------- | --------------------- | --------------------- | --------------------- |
| 0.0     | 12.0                  | 12.0                  | 12.0                  | 12.0                  | 13.0                  | 13.0                  |
| 0.2     | 12.0                  | 12.0                  | 12.0                  | 12.0                  | 13.0                  | 13.0                  |
| 0.4     | 12.0                  | 12.0                  | 12.0                  | 12.0                  | 13.0                  | 13.0                  |
| 0.6     | 12.0                  | 12.0                  | 12.0                  | 12.0                  | 13.0                  | 13.0                  |
| 0.8     | 12.0                  | 12.0                  | 12.0                  | 12.0                  | 13.0                  | 13.0                  |
| 1.0     | 12.0                  | 12.0                  | 12.0                  | 12.0                  | 13.0                  | 13.0                  |
| 1.2     | 12.0                  | 12.0                  | 12.0                  | 12.0                  | 13.0                  | 13.0                  |
| 1.4     | 12.0                  | 12.0                  | 12.0                  | 12.0                  | 13.0                  | 13.0                  |
| 1.6     | 12.0                  | 12.0                  | 12.0                  | 12.0                  | 13.0                  | 13.0                  |
</details>

Fig. 4. $\tilde { R } _ { \mathrm { M A C } }$ versus $\Theta$ under various GT density $\rho$ in uplink MAC.

## VII. CONCLUSION

In this letter, we studied the joint altitude and beamwidth optimization problem for UAV-enabled multiuser communication systems. Three fundamental models were studied based on our proposed fly-hover-and-communicate protocol. Our results show drastically different rules for setting optimal altitude and beamwidth values in different multiuser models. We hope that the results provide new and helpful insights for the design of practical UAV-enabled communication systems. Extension of our results to the case with fading UAV-GT channels and/or multiple UAVs is an interesting direction of future work.

## REFERENCES

[1] Y. Zeng, R. Zhang, and T. J. Lim, “Wireless communications with unmanned aerial vehicles: Opportunities and challenges,” IEEE Commun. Mag., vol. 54, no. 5, pp. 36–42, May 2016.  
[2] A. Al-Hourani, S. Kandeepan, and S. Lardner, “Optimal LAP altitude for maximum coverage,” IEEE Wireless Commun. Lett., vol. 3, no. 6, pp. 569–572, Dec. 2014.  
[3] R. I. Bor-Yaliniz, A. El-Keyi, and H. Yanikomeroglu, “Efficient 3-D placement of an aerial base station in next generation cellular networks,” in Proc. IEEE Int. Conf. Commun. (ICC), Kuala Lumpur, Malaysia, May 2016, pp. 1–5.  
[4] M. Mozaffari, W. Saad, M. Bennis, and M. Debbah, “Efficient deployment of multiple unmanned aerial vehicles for optimal wireless coverage,” IEEE Commun. Lett., vol. 20, no. 8, pp. 1647–1650, Aug. 2016.  
[5] M. Mozaffari, W. Saad, M. Bennis, and M. Debbah, “Unmanned aerial vehicle with underlaid device-to-device communications: Performance and tradeoffs,” IEEE Trans. Wireless Commun., vol. 15, no. 6, pp. 3949–3963, Jun. 2016.  
[6] V. Sharma, M. Bennis, and R. Kumar, “UAV-assisted heterogeneous networks for capacity enhancement,” IEEE Commun. Lett., vol. 20, no. 6, pp. 1207–1210, Apr. 2016.  
[7] J. Lyu, Y. Zeng, R. Zhang, and T. J. Lim, “Placement optimization of UAV-mounted mobile base stations,” IEEE Commun. Lett., vol. 21, no. 3, pp. 604–607, Mar. 2017.  
[8] J. Lyu, Y. Zeng, and R. Zhang, “Cyclical multiple access in UAV-aided communications: A throughput-delay tradeoff,” IEEE Wireless Commun. Lett., vol. 5, no. 6, pp. 600–603, Dec. 2016.  
[9] Y. Zeng, R. Zhang, and T. J. Lim, “Throughput maximization for UAV-enabled mobile relaying systems,” IEEE Trans. Commun., vol. 64, no. 12, pp. 4983–4996, Dec. 2016.  
[10] Y. Zeng and R. Zhang, “Energy-efficient UAV communication with trajectory optimization,” IEEE Trans. Wireless Commun., vol. 16, no. 6, pp. 3747–3760, Jun. 2017.  
[11] T. Debogovic, J. P. Carrier, and J. Bartolic, “Partially reflective surface antenna with dynamic beamwidth control,” IEEE Antennas Wireless Propag. Lett., vol. 9, pp. 1157–1160, 2010.  
[12] C. A. Balanis, Antenna Theory: Analysis and Design, 4th ed. Hoboken, NJ, USA: Wiley, 2016.  
[13] G. Laporte, “The traveling salesman problem: An overview of exact and approximate algorithms,” Eur. J. Oper. Res., vol. 59, no. 2, pp. 231–247, Jun. 1992.