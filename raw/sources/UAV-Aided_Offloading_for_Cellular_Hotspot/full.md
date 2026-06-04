# UAV-Aided Offloading for Cellular Hotspot

Jiangbin Lyu , Member, IEEE, Yong Zeng , Member, IEEE, and Rui Zhang , Fellow, IEEE

Abstract— In conventional terrestrial cellular networks, mobile terminals (MTs) at the cell edge often pose a performance bottleneck due to their long distances from the serving ground base station (GBS), especially in the hotspot period when the GBS is heavily loaded. This paper proposes a new hybrid network architecture that leverages use of unmanned aerial vehicle (UAV) as an aerial mobile base station, which flies cyclically along the cell edge to offload data traffic for cell-edge MTs. We aim to maximize the minimum throughput of all MTs by jointly optimizing the UAV’s trajectory, bandwidth allocation, and user partitioning. We first consider orthogonal spectrum sharing between the UAV and GBS, and then extend to spectrum reuse where the total bandwidth is shared by both the GBS and UAV with their mutual interference effectively avoided. Numerical results show that the proposed hybrid network with optimized spectrum sharing and cyclical multiple access design significantly improves the spatial throughput over the conventional GBS-only network; while the spectrum reuse scheme provides further throughput gains at the cost of slightly higher complexity for interference control. Moreover, compared with the conventional small-cell offloading scheme, the proposed UAV offloading scheme is shown to outperform in terms of throughput, besides saving the infrastructure cost.

Index Terms— UAV communication, mobile base station, cellular offloading, spectrum sharing, cyclical multiple access.

# I. INTRODUCTION

W ITH their high mobility and ever-reducing cost, unmanned aerial vehicles (UAVs) are expected to play an important role in future wireless communication systems. There are assorted appealing applications by leveraging UAVs for wireless communications [2], such as UAV-enabled ubiquitous coverage or drone small cells (DSCs) [3]–[12], UAV-enabled mobile relaying [13]–[15] and UAV-enabled information dissemination/data collection [16]–[18]. In particular, for UAV-enabled ubiquitous coverage, the UAV is deployed to assist the existing terrestrial communication system in providing seamless wireless coverage. Two typical use scenarios are rapid service recovery after ground infrastructure malfunction [19] and cellular traffic offloading from overloaded ground base stations (GBSs) in, e.g., hotspot areas.

Manuscript received November 21, 2017; revised January 29, 2018; accepted March 19, 2018. Date of publication March 30, 2018; date of current version June 8, 2018. This work was supported by the National University of Singapore under Research Grant R-263-000-B62-112. This paper was presented in part at the IEEE GLOBECOM, Singapore, December 2017 [1]. The associate editor coordinating the review of this paper and approving it for publication was D. Niyato. (Corresponding author: Jiangbin Lyu.)

J. Lyu is with the School of Information Science and Engineering, Xiamen University, Xiamen 361005, China (e-mail: ljb@xmu.edu.cn).

Y. Zeng and R. Zhang are with the Department of Electrical and Computer Engineering, National University of Singapore, Singapore 117583 (e-mail: elezeng@nus.edu.sg; elezhang@nus.edu.sg).

Color versions of one or more of the figures in this paper are available online at http://ieeexplore.ieee.org.

Digital Object Identifier 10.1109/TWC.2018.2818734

![](images/39d3fa25f2e9b23835b7759d118abc8d1433c394c8ff02b68717a9a8db7ed971.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    UAV[" UAV "] --> V[" V "]
    V --> GBS[" GBS "]
    GBS --> MT1[" MT1 "]
    GBS --> MT2[" MT2 "]
    GBS --> MT3[" MT3 "]
    GBS --> MT4[" MT4 "]
    GBS --> rU[" r_U "]
    GBS --> rI[" r_I "]
    GBS --> rG[" r_G "]
    GBS --> rC[" r_C "]
    GBS --> ΦU[" Φ_U "]
    GBS --> ΦU_R[" Φ_U_R "]
    GBS --> HU[" H_U1 "]
    GBS --> HU_R
    style UAV fill:#f9f,stroke:#333
    style GBS fill:#ccf,stroke:#333
    style MT1 fill:#dfd,stroke:#333
    style MT2 fill:#dfd,stroke:#333
    style MT3 fill:#dfd,stroke:#333
    style MT4 fill:#dfd,stroke:#333
    style rU fill:#dfd,stroke:#333
    style rU_R fill:#dfd,stroke:#333
    style rC fill:#dfd,stroke:#333
    style rI fill:#dfd,stroke:#333
    style rG fill:#dfd,stroke:#333
```
</details>

Fig. 1. UAV-aided cellular offloading.

Note that the latter case has been identified as one of the five key scenarios that need to be effectively addressed by the fifth-generation (5G) wireless systems [20].

The offloading issue for cellular hotspot can be partly addressed via existing technologies such as WiFi offloading [21] or small cell [22], among others. However, these solutions usually require deploying new fixed access points/GBSs, which could be cost-ineffective for scenarios with highly dynamic and diversified traffic demand such as open air festivals and other public events with temporarily high user density. In such scenarios, UAV-aided cellular offloading provides a promising alternative solution to address the cellular hotspot issue, of which the main cost such as the energy and aircraft cost can be lower than building new ground infrastructure. Furthermore, UAV-aided cellular offloading offers promising advantages compared to the conventional cellular network with fixed GBSs, such as the ability for on-demand and swift deployment, more flexibility for network reconfiguration, and better communication channels between the UAV and ground mobile terminals (MTs) due to the dominant line-of-sight (LoS) links. Moreover, the UAV mobility provides additional design degrees of freedom via trajectory optimization [23].

In traditional terrestrial cellular networks, the cell-edge MTs often suffer from poor channel conditions due to their long distances from their associated GBS. As a result, with a limited total bandwidth available for each cell, these celledge MTs would require either more bandwidth and/or higher transmit power in order to achieve the same performance as other non-cell-edge MTs, which thus pose a fundamental performance bottleneck for the cellular system, especially for hotspot period when the GBS is heavily loaded. To tackle this issue, we propose in this paper a new hybrid cellular network architecture based on the technique of UAV-aided cellular offloading. The proposed hybrid network architecture consists of a conventional GBS and an additional UAV serving as an aerial mobile BS to jointly serve the MTs in each cell. As shown in Fig. 1, the UAV flies cyclically along the cell edge to serve the cell-edge MTs and thereby help offloading the traffic from the GBS. Accordingly, the MTs in the cell are partitioned into cell-edge and non-cell-edge MTs, which are served by the UAV and GBS, respectively. We assume that the UAV flies at a fixed altitude following a circular trajectory with a certain radius centered at the GBS, and communicates with its associated cell-edge MTs in a cyclical time-division manner [3]. Specifically, at any time instant, only those cell-edge MTs that are sufficiently close to the UAV are scheduled to communicate with the UAV. Compared to the small cell technology where usually a large number of small cells need to be deployed in different fixed locations in the cell, the UAV-enabled cyclical multiple access scheme essentially shortens the communication distance with all cell-edge users by exploiting the UAV’s mobility, and hence it is anticipated to significantly reduce the deployment cost and improve the system throughput.

With the proposed hybrid network architecture applied to a single-cell system, we study the problem of maximizing the minimum (common) throughput of all MTs in the cell, so that each MT achieves a fair common throughput. Specifically, the main contributions of this paper are summarized as follows.

First, we consider the case of orthogonal spectrum sharing between the GBS and UAV, where the total available bandwidth is partitioned into two orthogonal parts to be allocated to the UAV and GBS, respectively. Three key parameters are then jointly designed, namely the bandwidth allocation and the user partitioning between the UAV and GBS, as well as the UAV’s circular trajectory radius. The joint optimization problem is non-convex and challenging to be directly solved. To tackle this problem, we first optimize the UAV’s trajectory radius for given bandwidth allocation and user partitioning. Then we jointly optimize the bandwidth allocation and user partitioning to maximize the common throughput of all MTs.

• Second, we extend our analysis to the spectrum reuse case where the whole spectrum pool is shared by both the GBS and UAV for concurrent communications. In this case, their mutual interference is a key issue and we propose effective methods to suppress the interference by leveraging the use of directional antennas at the UAV and adaptive directional transmission at the GBS. Compared to the orthogonal spectrum sharing scheme, the spectrum reuse scheme further improves the spectrum efficiency and thus the common throughput, at the cost of more complexity in practical implementation for the interference avoidance between the UAV and GBS transmissions.

Finally, extensive numerical results are provided to validate our analytical results. It is found that the proposed hybrid network with optimized design greatly improves the spatial throughput over the traditional network with the GBS only. As a result, the proposed UAV-aided cellular offloading scheme can support higher user density under the same target rate requirements for each user, which thus provides a promising solution to address the cellular hotspot issue. Furthermore, it is shown that the

joint optimization of spectrum sharing, multiple access, and UAV trajectory design is essential to achieve the optimum throughput of the proposed UAV-assisted hybrid network, for both cases with orthogonal spectrum sharing and non-orthogonal spectrum reuse. Moreover, the proposed scheme is also compared with the conventional cell-edge throughput enhancement scheme by deploying a number of micro/small cells to help offload data traffic for cell-edge users. The simulation results show that the proposed UAV offloading scheme with only one single UAV/mobile BS significantly outperforms the micro-cell offloading scheme in terms of throughput, besides saving the infrastructure cost.

The rest of this paper is organized as follows. The system model and the proposed UAV-enabled hybrid network architecture are given in Section II. The optimized designs for maximizing the minimum throughput with orthogonal spectrum sharing scheme and spectrum reuse scheme are presented in Section III and Section ${ \mathrm { I V } } ,$ respectively. Section IV also provides discussions on the relaxation of the modeling assumptions and some practical implementation issues. Numerical results are provided in Section V. Finally, we conclude the paper in Section VI.

# II. SYSTEM MODEL

As shown in Fig. 1, we consider a single-cell wireless communication system with a GBS and a UAV jointly serving a group of MTs on the ground. In this paper, we consider the downlink communication from the GBS/UAV to the MTs, whereas the obtained results can be similarly applied to the uplink communication as well. Assume that the MTs are uniformly and randomly distributed with a given density λ in the cell of cell radius $r _ { G }$ and centered at the GBS location; thus, the total number of MTs on average is $K \ = \ \pi r _ { G } ^ { 2 } \lambda$ . Denote the set of MTs as ${ \cal K } = \{ 1 , 2 , \dots , K \}$ . The MTs are partitioned into two disjoint groups, $\kappa _ { G }$ and $\kappa _ { U }$ , based on a distance threshold $r _ { I }$ to the GBS, where $\kappa _ { G }$ denotes the set of MTs in the inner disk region of radius $r _ { I }$ , and $\kappa _ { U }$ denotes the remaining MTs in the exterior ring region. We assume that the MTs in $\kappa _ { G }$ (e.g., MTs 2 and 4 in Fig. 1) are associated with the GBS for communications, while those in $\kappa _ { U }$ (e.g., MTs 1 and 3) are served by the UAV via the cyclical multiple access scheme [3]. Hence, there are on average $K _ { G } \triangleq \vert { \mathcal { K } } _ { G } \vert = \pi \lambda r _ { I } ^ { 2 }$ MTs associated with the GBS, and $K _ { U } \ \triangleq \ | \mathcal { K } _ { U } | \ = \ \pi \lambda ( r _ { G } ^ { 2 } \ - \ r _ { I } ^ { 2 } )$ MTs to be served by the UAV, where | · | denotes the cardinality of a set. For simplicity, we assume that an ideal wireless backhaul between the UAV and GBS exists, which operates in a separate band. Several technologies such as millimeter wave and free space optical communications can be good candidates for realizing high-speed wireless backhaul between the UAV and GBS, thanks to the favorable communication channel with strong LoS link.

We assume that the UAV flies at a fixed altitude $H _ { U }$ , which could correspond to the minimum value required for safety considerations such as terrain or building avoidance. We also assume that the UAV flies at a constant speed V following a circular trajectory whose projection on the ground is centered at the GBS. Denote the radius of the UAV trajectory as $r _ { U }$ and its period as T , i.e., the UAV position repeats every $T$ seconds, as shown in Fig. 1. Then we have $T = 2 \pi r _ { U } / V$ . Note that the circular trajectory is considered since it not only enables the UAV to serve the cell-edge users in a periodic manner, but is also energy-efficient for the UAV flying [23]. For any time instant $t ,$ let $\kappa _ { U } ( t ) \subseteq \kappa _ { U }$ denote the set of celledge MTs that are scheduled for communication with the UAV. Since each MT has the best communication link when the UAV flies close to it, it is intuitive to schedule the nearest MTs from the current UAV position to communicate with the UAV, in order to maximize the system throughput. Motivated by this, we propose a simple time-division based cyclical multiple access scheme, where different cell-edge MTs are scheduled to communicate with the UAV in a cyclical time-division manner to exploit the good channel when the UAV flies close to each of them.

Next, we discuss the channel models for UAV-MT and GBS-MT communications, respectively. We assume that the UAV is equipped with a directional antenna, whose azimuth and elevation half-power beamwidths are both $2 \Phi _ { U }$ radians (rad) with $\Phi _ { U } ~ \in ~ ( 0 , \frac { \pi } { 2 } )$ . Furthermore, the corresponding antenna gain in direction $( \phi , \varphi )$ can be practically approximated as

$$
G _ {U} (\phi , \varphi) = \left\{ \begin{array}{l l} G _ {0} / \Phi_ {U} ^ {2}, & - \Phi_ {U} \leq \phi \leq \Phi_ {U}, - \Phi_ {U} \leq \varphi \leq \Phi_ {U}; \\ g _ {0} \approx 0, & \text { otherwise }, \end{array} \right. \tag {1}
$$

where $\begin{array} { r } { G _ { 0 } = \frac { 3 0 0 0 0 } { 2 ^ { 2 } } \times ( \frac { \pi } { 1 8 0 } ) ^ { 2 } \approx 2 . 2 8 4 6 ; } \end{array}$ ; φ and $\varphi$ denote the azimuth and elevation angles, respectively [24] [25]. Note that in practice, $g _ { 0 }$ satisfies $0 ~ < ~ g _ { 0 } ~ \ll ~ G _ { 0 } / \Phi _ { U } ^ { 2 }$ , and for simplicity we assume $g _ { 0 } = 0$ in this paper. On the other hand, we assume that each MT is equipped with an omnidirectional antenna of unit gain. Thus, the disk region centered at the UAV’s projection on the ground with radius $r _ { c } = H _ { U }$ tan ΦU corresponds to the ground coverage area by the antenna main lobe of the UAV, as shown in Fig. 1. By properly adjusting the beamwidth $\Phi _ { U }$ , we assume that the coverage radius $r _ { c }$ is appropriately set so that the scheduled MTs $\kappa _ { U } ( t )$ are guaranteed to lie within the coverage area of the UAV at time t. On the other hand, an increase in $\Phi _ { U }$ would reduce the antenna gain of the main lobe, as shown in (1). Thus, the beamwidth $\Phi _ { U }$ or equivalently the scheduled MTs $K _ { U } ( t )$ over time should be carefully designed.

We consider that the UAV-MT communication channels are dominated by LoS links. Though simplified, the LoS model offers a good approximation for practical UAV-MT channels, which is also one of the main motivations to utilize UAVs for wireless communication. Recent field experiments by Qualcomm [26] have verified that the UAV-to-ground channel is indeed dominated by the LoS link for UAVs flying above a certain altitude. Assume that the Doppler effect due to the UAV’s mobility is perfectly compensated at all the MT receivers.1 Thus the channel power gain from the UAV to 1In this paper, the UAV follows a simple circular trajectory with a fixed flying speed, thus the Doppler effect exhibits a certain cyclical pattern and hence can be more easily estimated and compensated.

MT k at time t follows the free-space path loss model given by

$$
h _ {k} (t) = \frac {\beta_ {0}}{d _ {k} ^ {2} (t) + H _ {U} ^ {2}}, \quad 0 \leq t \leq T, \tag {2}
$$

where $\beta _ { 0 } = ( \frac { 4 \pi f _ { c } } { c } ) ^ { - 2 }$ denotes the channel power gain at a reference distance of 1 meter (m), with $f _ { c }$ denoting the carrier frequency and c denoting the speed of light; and $d _ { k } ( t )$ is the horizontal distance between the UAV and MT k at time t.

On the other hand, for GBS-MT communications, we assume that the GBS has a fixed antenna gain for transmission, denoted by $G _ { G } \geq 1$ . In practice, the GBS could be equipped with an omnidirectional antenna, or multiple sectorized antennas with non-overlapping directional transmissions. Furthermore, we assume a fading channel between the GBS and MTs, which consists of distance-dependent path-loss with path-loss exponent $n \geq 2$ and an additional random term accounting for small-scale fading. Therefore, the channel power gain from the GBS to MT k can be modelled as $g _ { k } ~ = ~ \bar { g } _ { k } \zeta _ { k }$ , where $\bar { g } _ { k } \triangleq \alpha _ { 0 } ( H _ { G } ^ { 2 } + r ^ { 2 } ) ^ { - n / 2 }$ is the average channel power gain, with $\alpha _ { 0 } ~ = ~ ( \frac { 4 \pi f _ { c } } { c } ) ^ { - 2 }$ denoting the average channel power gain at a reference distance of 1 m, r denoting the horizontal distance between the GBS and MT $k ,$ and $H _ { G }$ denoting the height of the GBS; and $\begin{array} { r } { \zeta _ { k } \ \sim \ \mathrm { E x p } ( 1 ) } \end{array}$ is an independent and identically distributed (i.i.d.) exponential random variable with unit mean accounting for the small-scale Rayleigh fading.

In this paper, we investigate two practical spectrum sharing models for the UAV and GBS, i.e., orthogonal spectrum sharing and non-orthogonal spectrum reuse. In the orthogonal sharing case, the UAV and GBS are allocated with orthogonal spectrum respectively, and thus there is no interference between the UAV-MT and GBS-MT communications. By contrast, in the spectrum reuse case, the common spectrum pool is shared by both the GBS and UAV for concurrent transmissions, provided that their mutual interference is effectively suppressed. With directional/sectorized antennas, such interference can be avoided in practice by leveraging the joint use of directional antenna at the UAV and adaptive directional transmission at the GBS. For example, in Fig. 1, the GBS-MT4 and UAV-MT1 links can use the same frequency band at the same time without mutual interference if non-overlapping directional transmissions of the GBS and UAV are employed. Note that spectrum reuse is more general than orthogonal sharing, which improves the spectrum efficiency but is also more complicated to design and implement in practice.

We assume that the total available bandwidth is W Hz. In the orthogonal sharing case, denote the portion of bandwidth allocated to the UAV as $\rho ,$ with $0 \leq \rho \leq 1$ . Assume that the bandwidth allocated to the UAV is equally shared among the MTs associated with the UAV at each time, i.e., each MT $k \in \mathcal { K } _ { U } ( t )$ is allocated with an effective bandwidth of $b _ { U } ( t ) W$ , with $b _ { U } ( t ) \ \triangleq \ \rho / | \mathcal { K } _ { U } ( t ) |$ | denoting the normalized bandwidth for each user. Similarly, we assume that the GBS also adopts the equal bandwidth allocation scheme, i.e., each non-cell-edge MT $k ~ \in ~ { \cal K } _ { G }$ is allocated with an effective bandwidth of $b _ { G } W$ , with $b _ { G } \triangleq ( 1 - \rho ) / K _ { G }$ . On the other hand, we also assume a similar equal bandwidth allocation scheme in the spectrum reuse case, despite that the total bandwidth is now used by both the UAV and GBS concurrently.

In the following two sections, we will present the two spectrum sharing models in more details as well as their respective design optimization problems and solutions to maximize the system common throughput.

# III. ORTHOGONAL SPECTRUM SHARING

In this section, we study the orthogonal spectrum sharing scheme. First, we derive the achievable throughput of the UAV-MT and GBS-MT communications, respectively. Denote the common (minimum) throughput of all MTs as ν¯ in bits per second per Hz (bps/Hz), which is normalized with respect to the total system bandwidth W . Then, we formulate the problem to maximize ν¯ by jointly optimizing the UAV trajectory radius $r _ { U }$ , user partitioning radius threshold $r _ { I }$ , and bandwidth allocation portion $\rho .$

# A. UAV-MT Communication

1) Average Throughput: For each MT k, we define the association time $\tau _ { k }$ as the total time duration in which MT k is associated with the UAV for communications within each UAV flying period T . The average throughput of cell-edge MT $k \in \mathcal { K } _ { U }$ over each period $T$ is determined by $\tau _ { k }$ and its instantaneous communication rate with the UAV during this association time interval.

Assume that the UAV allocates transmit power $p _ { k } ( t )$ to communicate with MT $k \ \in \ \mathcal { K } _ { U } ( t )$ at time t during its association time. Then the instantaneous achievable rate $R _ { k } ( t )$ of MT $k \in \mathcal { K } _ { U } ( t )$ in bps/Hz is given by

$$
\begin{array}{l} R _ {k} (t) = b _ {U} (t) \log_ {2} \left(1 + \frac {G _ {U} h _ {k} (t) p _ {k} (t)}{b _ {U} (t) \sigma^ {2}}\right) \\ = b _ {U} (t) \log_ {2} \left(1 + \frac {\eta_ {0} G _ {U} p _ {k} (t)}{b _ {U} (t) \left(d _ {k} ^ {2} (t) + H _ {U} ^ {2}\right)}\right), \tag {3} \\ \end{array}
$$

where the receiver noise is assumed to be additive white Gaussian with power spectrum density $N _ { 0 }$ in Watts/Hz; $\sigma ^ { 2 } \triangleq$ $N _ { 0 } W$ is the total noise power over the whole bandwidth of W Hz; and $\eta _ { 0 } \triangleq \beta _ { 0 } / \sigma ^ { 2 }$ . It can be seen that $R _ { k } ( t )$ is determined by the allocated transmit power $p _ { k } ( t )$ , the UAV-MT horizontal link distance $d _ { k } ( t )$ , and the normalized per-user bandwidth $b _ { U } ( t )$ which in turn depends on the number of MTs $| \mathcal { K } _ { U } ( t ) |$ associated with the UAV at time t.

With (3), the average throughput of cell-edge MT $k \in \mathcal { K } _ { U }$ within a UAV flying period $T$ is given by

$$
\bar {R} _ {k} = \frac {1}{T} \int_ {t = t _ {s, k}} ^ {t _ {e, k}} R _ {k} (t) \mathrm{d} t, \tag {4}
$$

where $t _ { s , k }$ and $t _ { e , k }$ are the starting and ending time instants for the interval when MT k is associated with the $\mathrm { U A V } ,$ respectively, and $\tau _ { k } ~ = ~ t _ { e , k } - t _ { s , k }$ . Next, we discuss the design of transmit power $p _ { k } ( t ) , t _ { s , k } \le t \le t _ { e , k }$ , the UAV-MT association $\ K _ { U } ( t ) , 0 \leq t \leq T$ , and the distance $d _ { k } ( t ) , t _ { s , k } \le$ $t \le t _ { e , k }$ , respectively.

2) Power Allocation: Let $P _ { U }$ denote the maximum transmit power of the UAV. For simplicity, we assume that at each time instant t, the UAV allocates equal transmit power to its

![](images/b8fb5a32fdb659e194f7819f9d09dbdc0aa5b304e4eafc5dd1c7654da7c85808.jpg)

<details>
<summary>text_image</summary>

k
r
φ
0
(GBS)
ψ
A
r
r'
A'
B
B'
rU
rG
Association region Sa
</details>

Fig. 2. Proposed UAV-MT association pattern.

associated MTs $k \in \mathcal { K } _ { U } ( t )$ , i.e., $p _ { k } ( t ) = P _ { U } / | \mathcal { K } _ { U } ( t ) | , \forall k \in$ $\kappa _ { U } ( t )$ . From (3) and using the fact that $b _ { U } ( t ) = \rho / | \mathcal { K } _ { U } ( t ) |$ |, the instantaneous achievable rate $R _ { k } ( t )$ becomes

$$
\begin{array}{l} R _ {k} (t) = b _ {U} (t) \log_ {2} \left(1 + \frac {\eta_ {0} G _ {U} P _ {U} / | \mathcal {K} _ {U} (t) |}{b _ {U} (t) \left(d _ {k} ^ {2} (t) + H _ {U} ^ {2}\right)}\right) \\ = \frac {\rho}{\left| \mathcal {K} _ {U} (t) \right|} \log_ {2} \left(1 + \frac {\eta_ {0} G _ {U} P _ {U}}{\rho \left(d _ {k} ^ {2} (t) + H _ {U} ^ {2}\right)}\right), \tag {5} \\ \end{array}
$$

which depends on $\rho , G _ { U } , d _ { k } ( t )$ and $| \mathcal { K } _ { U } ( t ) |$ |. The association $\ K _ { U } ( t ) , 0 \leq t \leq T$ determines the average throughput $\bar { R } _ { k }$ in (4) in two ways, namely, the normalized per-user bandwidth $b _ { U } ( t ) = \rho / | \mathcal { K } _ { U } ( t ) |$ at each time t, and the association time period $t _ { s , k } \le t \le t _ { e , k }$ assigned for each MT k.

3) UAV-MT Association: For the analytical tractability, we design a simple yet practical UAV-MT association rule as follows. At each time t, assume that the horizontal position of the UAV is at $( r _ { U } , 0 )$ in the polar coordinate system $( r , \phi )$ . The MTs $k \in \mathcal { K } _ { U }$ in the ring region with $r _ { I } ~ \le ~ r ~ \le ~ r _ { G }$ are to be served by the UAV via cyclical multiple access. Accordingly, we choose a ring segment region (denoted as $S _ { a } )$ with central angle ψ, which is also symmetric about the horizontal axis, as shown by the shadowed region in Fig. 2. Within the region $ { \boldsymbol { S } } _ { a }$ , any arc centered at the origin (GBS location) with radius $r _ { I } ~ \le ~ r ~ \le ~ r _ { G }$ has the same central angle ψ. In particular, denote the arcs with radius $r _ { I }$ and $r _ { G }$ by AA’ and BB’, respectively.

We propose the UAV-MT association rule by which the MTs within the ring segment region $ { \boldsymbol { S } } _ { a }$ are associated with the UAV for communications at time t, which thus determines the set $\kappa _ { U } ( t )$ . This association rule simplifies our subsequent analysis in two aspects. Firstly, all cell-edge MTs $k \in \mathcal { K } _ { U }$ have equal association time with the UAV, i.e.,

$$
\tau_ {k} = \frac {\psi T}{2 \pi}, \quad \forall k \in \mathcal {K} _ {U}. \tag {6}
$$

Secondly, the average number of MTs associated with the UAV at any time t is a linearly increasing function of ψ, i.e.,

$$
K _ {a} \triangleq \lambda S _ {a} = \lambda (r _ {G} ^ {2} - r _ {I} ^ {2}) \psi / 2, \tag {7}
$$

where $S _ { a } \triangleq { \left( r _ { G } ^ { 2 } - r _ { I } ^ { 2 } \right) } \psi / 2$ is the area of $ { \boldsymbol { S } } _ { a }$ .

Note that with the proposed association rule, each MT $k \in$ KU incurs an access delay [3] given by $D _ { k } \triangleq T - \tau _ { k }$ , which is the time duration within each UAV flying period T when MT k is not associated with the UAV for communications. Therefore, the proposed scheme is most suitable for the celledge MTs with high throughput demand but less stringent delay requirement. For those cell-edge MTs with stringent delay requirement, it can still be served by the GBS in the conventional way. On the other hand, the cell-edge MTs are exclusively served by the UAV in a cyclical time-division manner, while the non-cell-edge MTs are exclusively served by the GBS. In other words, there is no need for handover of any MT between the GBS and UAV.

4) Lower Bound of Average Throughput: Based on the above association rule, the association time $\tau _ { k }$ in (6) is identical for all MTs $k \in \mathcal { K } _ { U }$ . Therefore, the average throughput $\bar { R } _ { k }$ in (4) is determined by the instantaneous rate $R _ { k } ( t ) , t _ { s , k } \le$ $t \le t _ { e , k }$ , which depends on $\rho , G _ { U } , d _ { k } ( t )$ and $b _ { U } ( t )$ . In the following, we derive a lower bound for the average throughput $\bar { R } _ { k }$ in (4), based on the upper bound of the UAV-MT horizontal distance $d _ { k } ( t )$ and the lower bound of normalized per-user bandwidth $b _ { U } ( t )$ .

First, $d _ { k } ( t )$ is a non-linear function of t and it is different for MTs located at different r. Denote $d _ { \mathrm { m a x } }$ as the upper bound of the horizontal distance from the UAV to any point in the ring segment region $ { \boldsymbol { S } } _ { a }$ . Since $\scriptstyle { S _ { a } }$ should lie within the coverage area of the UAV, we have $r _ { c } \ge d _ { \mathrm { m a x } }$ , i.e., $H _ { U }$ tan $\Phi _ { U } \geq d _ { \operatorname* { m a x } } ,$ which yields

$$
\Phi_ {U} \geq \arctan (d _ {\max} / H _ {U}). \tag {8}
$$

Since the UAV’s antenna gain of the main lobe $G _ { U }$ in (1) is a decreasing function of $\Phi _ { U } , \Phi _ { U }$ should be chosen to be the minimum possible value as in (8) in order to maximize $G _ { U }$ and hence the throughput. Therefore, the UAV antenna gain $G _ { U }$ towards the coverage area is given by

$$
G _ {U} (d _ {\max}) = \frac {G _ {0}}{(\arctan \frac {d _ {\max}}{H _ {U}}) ^ {2}}, \tag {9}
$$

which is a decreasing function of $d _ { \mathrm { m a x } }$ .

It can be verified that $d _ { \mathrm { m a x } }$ always occurs at one of the two intersection points A and B as shown in Fig. 2. Denote $d _ { A }$ and $d _ { B }$ as the horizontal distances from the UAV to points A and B, respectively. Then we have

$$
d _ {\max} = \max (d _ {A}, d _ {B}), \tag {10}
$$

where $d _ { A }$ and $d _ { B }$ can be obtained by using the cosine law as follows

$$
d _ {A} = \sqrt {r _ {U} ^ {2} + r _ {I} ^ {2} - 2 r _ {U} r _ {I} \cos \frac {\psi}{2}}, \tag {11}
$$

$$
d _ {B} = \sqrt {r _ {U} ^ {2} + r _ {G} ^ {2} - 2 r _ {U} r _ {G} \cos \frac {\psi}{2}}. \tag {12}
$$

It can be verified that $d _ { \mathrm { m a x } }$ is an increasing function of ψ for any given rI and $r _ { U } .$

Second, let $K _ { a , \operatorname* { m a x } } \triangleq \operatorname* { m a x } _ { 0 < t < T } | K _ { U } ( t ) |$ denote the maximum 0≤t≤T number of MTs associated with the UAV over the period $T ,$ and denote μ - Ka,maxK $\begin{array} { r } { \mu \triangleq \frac { K _ { a , \mathrm { m a x } } } { K _ { a } } \ge 1 } \end{array}$ . Note that $\mu$ depends on the spatial variations of the user locations. Then at any time t, $b _ { U } ( t )$ is lower-bounded by

$$
b _ {U} (t) \geq \frac {\rho}{K _ {a , \max}} = \frac {2 \rho}{\mu \lambda (r _ {G} ^ {2} - r _ {I} ^ {2}) \psi} \triangleq b _ {\min}, \tag {13}
$$

where the lower bound $b _ { \mathrm { m i n } }$ is inversely proportional to $\psi .$

Then the instantaneous rate $R _ { k } ( t )$ in (5) for any MT $k \in$ $\kappa _ { U } ( t )$ at any time t is lower-bounded by

$$
R _ {k} (t) \geq b _ {\min} \log_ {2} \left(1 + \frac {\eta_ {0} P _ {U} G _ {U} (d _ {\max})}{\rho (d _ {\max} ^ {2} + H _ {U} ^ {2})}\right) \triangleq R _ {U}, \tag {14}
$$

where the lower bound $R _ { U }$ is a decreasing function of $\psi _ { : }$ since a larger central angle ψ leads to larger $d _ { \mathrm { m a x } }$ and smaller $b _ { \mathrm { m i n } }$ .

Based on (14), we then assume that the UAV communicates with each MT $k \in \mathcal { K } _ { U } ( t )$ at any time t using a constant rate equal to $R _ { U }$ , which is achievable for all MTs in $\kappa _ { U } ( t )$ . Then the average throughput in (4) for MT $k \in \mathcal { K } _ { U }$ over each time period $T$ is given by

$$
\bar {R} _ {k} = \frac {\tau_ {k}}{T} R _ {U} = \frac {\psi}{2 \pi} R _ {U}, \tag {15}
$$

which is equal for every cell-edge MT $k \in \mathcal { K } _ { U }$ . Therefore, by substituting $R _ { U }$ from (14) and $b _ { \mathrm { m i n } }$ from (13) into (15), the common throughput $\bar { R } _ { U }$ for the cell-edge MTs served by the UAV can be expressed as

$$
\begin{array}{l} \bar {R} _ {U} (\rho , r _ {I}, d _ {\max}) \triangleq \frac {\psi}{2 \pi} R _ {U} \\ = \frac {\psi}{2 \pi} b _ {\mathrm{min}} \log_ {2} \left(1 + \frac {\eta_ {0} P _ {U} G _ {U} (d _ {\mathrm{max}})}{\rho (d _ {\mathrm{max}} ^ {2} + H _ {U} ^ {2})}\right) \\ \stackrel {(a)} {=} \frac {\rho}{\mu \lambda \pi (r _ {G} ^ {2} - r _ {I} ^ {2})} \\ \times \log_ {2} \left(1 + \frac {\eta_ {0} P _ {U} G _ {U} (d _ {\max})}{\rho (d _ {\max} ^ {2} + H _ {U} ^ {2})}\right), \tag {16} \\ \end{array}
$$

which is a function of $\rho , r _ { I }$ and $d _ { \mathrm { m a x } }$ . Note that the equality (a) follows since the proportional effect of $\psi$ on the association time $\tau _ { k }$ in (6) cancels out its inversely proportional effect on the per-user bandwidth $b _ { \mathrm { m i n } }$ in (13), under our proposed association rule.

Since $\bar { R } _ { U }$ decreases with $d _ { \mathrm { m a x } }$ which in turn increases with ψ, it is desirable to choose $\psi$ as small as possible to increase $\bar { R } _ { U }$ in (16). However, ψ cannot be arbitrarily small in practice, since there might be no MTs associated with the UAV at some time t, i.e., $| \mathcal { K } _ { U } ( t ) | = 0$ . In the rest of this paper, we assume that the value of $\psi$ is given, and hence the corresponding $d _ { \mathrm { m a x } }$ can be obtained based on (10)–(12), which is a function of $r _ { I }$ and $r _ { U }$ . Therefore, (16) becomes

$$
\bar {R} _ {U} (\rho , r _ {I}, r _ {U}) = \frac {\rho}{\mu \lambda \pi (r _ {G} ^ {2} - r _ {I} ^ {2})} \log_ {2} \left(1 + \frac {\eta_ {0} P _ {U} G _ {U} (d _ {\max})}{\rho (d _ {\max} ^ {2} + H _ {U} ^ {2})}\right). \tag {17}
$$

Finally, we define the spatial throughput as the aggregated throughput per unit area in bps/Hz/m2, i.e., θ -   RkS , $\theta \ \triangleq \ \frac { \sum R _ { k } } { S }$ where $S$ is the area of interest. The spatial throughput of the UAV-served area is thus given by $\theta _ { U } \triangleq \lambda \bar { R } _ { U } ( \rho , r _ { I } , r _ { U } )$ , i.e.,

$$
\theta_ {U} = \frac {\rho}{\mu \pi (r _ {G} ^ {2} - r _ {I} ^ {2})} \log_ {2} \left(1 + \frac {\eta_ {0} P _ {U} G _ {U} (d _ {\max})}{\rho (d _ {\max} ^ {2} + H _ {U} ^ {2})}\right). \tag {18}
$$

# B. GBS-MT Communication

On the other hand, the MTs inside the inner disk of radius $r _ { I }$ are associated with the GBS for communications, which form the non-cell-edge MT set $\kappa _ { G }$ . Recall that the GBS-MT channel gain $g _ { k }$ consists of the average channel gain $\bar { g } _ { k }$ which depends on the GBS-MT horizontal distance r with $r \leq r _ { I }$ , and an additional random term $\zeta _ { k } \sim \mathrm { E x p } ( 1 )$ accounting for small-scale fading of the channel. We assume that the GBS knows the average channel gain $\bar { g } _ { k }$ for each MT k and the distribution of $\zeta _ { k }$ .

1) Power Allocation: Assume that the GBS transmits with equal power $p _ { G } ( r )$ for MTs at the same distance $r$ from the GBS, with $r \leq r _ { I }$ . We consider that the GBS adopts the “slow” channel inversion power control [27] based on the average channel gain $\bar { g } _ { k }$ (instead of the instantaneous channel gain which requires the estimation of the instantaneous channels and hence is more costly for practical implementation), i.e., the transmit power $p _ { G } ( r )$ is allocated such that all MTs $k \in \mathcal { K } _ { G }$ have the equal average signal-to-noise ratio (SNR) at the receiver, denoted by $\bar { \gamma } .$ Thus, $p _ { G } ( r )$ can be expressed as

$$
p _ {G} (r) = \frac {\bar {\gamma} b _ {G} \sigma^ {2}}{\bar {g} _ {k} G _ {G}} = \frac {\bar {\gamma} b _ {G} (H _ {G} ^ {2} + r ^ {2}) ^ {\frac {n}{2}}}{\kappa_ {0}}, \quad \forall r, 0 \leq r \leq r _ {I}, \tag {19}
$$

where $\kappa _ { 0 } ~ \triangleq ~ \alpha _ { 0 } ~ G _ { G } / \sigma ^ { 2 }$ , and the allocated power $p _ { G } ( r )$ is inversely proportional to the average channel gain $\bar { g } _ { k }$ .

Let $P _ { G }$ denote the maximum transmit power of the GBS. Then the total transmit power to all MTs associated with the GBS needs to satisfy the following constraint:

$$
\lambda \int_ {\phi = 0} ^ {2 \pi} \int_ {r = 0} ^ {r _ {I}} p _ {G} (r) r \mathrm{d} r \mathrm{d} \phi = P _ {G}. \tag {20}
$$

The average SNR can be obtained from (19) and (20) as

$$
\bar {\gamma} = \frac {\kappa_ {0} P _ {G}}{2 \pi \lambda b _ {G} L (r _ {I})} = \frac {\kappa_ {0} P _ {G} r _ {I} ^ {2}}{2 (1 - \rho) L (r _ {I})}, \tag {21}
$$

where $\begin{array} { r } { b _ { G } = \frac { 1 - \rho } { \lambda \pi r _ { I } ^ { 2 } } } \end{array}$ and

$$
L \left(r _ {I}\right) \triangleq \int_ {r = 0} ^ {r _ {I}} \left(H _ {G} ^ {2} + r ^ {2}\right) ^ {\frac {n}{2}} r \mathrm{d} r = \frac {\left(H _ {G} ^ {2} + r _ {I} ^ {2}\right) ^ {\frac {2 + n}{2}} - H _ {G} ^ {2 + n}}{2 + n}. \tag {22}
$$

The instantaneous achievable rate for MT $k \in \mathcal { K } _ { G }$ in bps/Hz is then given by

$$
R _ {k} = b _ {G} \log_ {2} (1 + \bar {\gamma} \zeta_ {k}). \tag {23}
$$

2) Outage Probability: Due to the small-scale fading of the GBS-MT channel, an outage event occurs when the GBS-MT link cannot support the desired common throughput ν¯. According to (23), the outage probability for MT $k \in { \mathcal { K } } _ { G }$ is given by

$$
\begin{array}{l} \mathrm{P} _ {\text { out }, k} = \operatorname * {P r} \left\{b _ {G} \log_ {2} (1 + \bar {\gamma} \zeta_ {k}) <   \bar {\nu} \right\} \\ = \operatorname * {P r} \{\zeta_ {k} <   (2 ^ {\bar {\nu} / b _ {G}} - 1) / \bar {\gamma} \} \\ = 1 - \exp \left(- (2 ^ {\bar {\nu} / b _ {G}} - 1) / \bar {\gamma}\right) \triangleq \mathrm{P} _ {\text { out }} (\rho , r _ {I}, \bar {\nu}), \tag {24} \\ \end{array}
$$

which is equal for all MTs $k \in \mathcal { K } _ { G }$ due to the common average SNR $\bar { \gamma }$ with the adopted channel inversion power control. For convenience, define a function $f ( \rho , r _ { I } , \bar { \nu } )$ as follows:

$$
f (\rho , r _ {I}, \bar {\nu}) \triangleq \frac {2 ^ {\bar {\nu} / b _ {G}} - 1}{\bar {\gamma}} = \frac {2 \left(2 ^ {\frac {\pi r _ {I} ^ {2} \cdot \lambda \bar {\nu}}{1 - \rho}} - 1\right) (1 - \rho) L (r _ {I})}{\kappa_ {0} P _ {G} r _ {I} ^ {2}}. \tag {25}
$$

Then we have

$$
\mathrm{P} _ {\text { out }} (\rho , r _ {I}, \bar {\nu}) = 1 - \exp (- f (\rho , r _ {I}, \bar {\nu})). \tag {26}
$$

It can be verified from (25) that $f ( \rho , r _ { I } , \bar { \nu } )$ and hence $\mathrm { P _ { o u t } } ( \rho , r _ { I } , \bar { \nu } )$ are both increasing functions of $\rho , \ r _ { I }$ and ν¯.

Define $\theta _ { G } \triangleq { \underline { { \underline { { \Delta } } } } }$ λν¯ as the spatial throughput of the GBS-served area. Suppose that the allowed maximum outage probability is $\bar { \mathrm { P } } _ { \mathrm { o u t } }$ for all GBS-MT links. Note that in the special case without the UAV, i.e., $\rho ~ = ~ 0$ and $r _ { I } ~ = ~ r _ { G }$ , by letting $\mathrm { P _ { o u t } } ( \rho = 0 , r _ { I } = r _ { G } , \bar { \nu } ) = \bar { \mathrm { P } } _ { \mathrm { o u t } }$ in (26), we can then obtain the common throughput $\bar { \nu } _ { G } ^ { \mathrm { o p t } }$ and the corresponding spatial throughput for all MTs in this case.

# C. Problem Formulation

In this subsection, we formulate the optimization problem to maximize the common throughput $\bar { \nu }$ of all MTs subject to the maximum outage probability constraint of GBS-MT links, by jointly optimizing the bandwidth allocation portion $\rho ,$ the user partitioning distance threshold $r _ { I }$ , and the UAV trajectory radius $r _ { U }$ . The problem can be formulated as

$$
\begin{array}{l} \text {(P1)}: \quad \max _ {\rho , r _ {I}, r _ {U}, \bar {\nu}} \quad \bar {\nu} \\ \text { s.t. } \quad \mathrm{P} _ {\text { out }} (\rho , r _ {I}, \bar {\nu}) \leq \bar {\mathrm{P}} _ {\text { out }}, (27) \\ \bar {R} _ {U} (\rho , r _ {I}, r _ {U}) \geq \bar {\nu}, (28) \\ r _ {I} \leq r _ {U} \leq r _ {G}, (29) \\ 0 \leq r _ {I} \leq r _ {G}, (30) \\ 0 \leq \rho \leq 1. (31) \\ \end{array}
$$

We denote the optimal solution to (P1) as $( \rho ^ { \mathrm { { o p t } } } , r _ { I } ^ { \mathrm { { o p t } } } , r _ { U } ^ { \mathrm { { o p t } } } )$ rI and the corresponding optimal common throughput as $\bar { \nu } ^ { \mathrm { { o p t } } }$ .

# D. Proposed Solution

Solving problem (P1) is non-trivial due to the non-convex constraints (27) and (28). By exploiting its special structure, (P1) is optimally solved as follows.

First, (P1) can be equivalently reduced to a series of subproblems (P2) given below, each for a given target value $\bar { \nu } .$ Furthermore, ν¯ can be updated via bisection search method. Specifically, to check whether a certain ν¯ is achievable, we can solve problem (P2) which minimizes the outage probability of GBS-MT links subject to the constraints (28)–(31), i.e.,

$$
\text {(P2)}: \min _ {\rho , r _ {I}, r _ {U}} \quad \mathrm{P} _ {\text {out}} (\rho , r _ {I}, \bar {\nu})
$$

$$
\text { s.t. } \quad (2 8) - (3 1).
$$

If the optimal value of (P2) is no larger than $\bar { \mathsf { P } } _ { \mathrm { o u t } } .$ then (27) is satisfied, and the optimal solution to (P2) and the corresponding ν¯ is a feasible solution to (P1). On the other hand, if the optimal value of (P2) is larger than $\bar { \mathsf { P } } _ { \mathrm { o u t } }$ , then the corresponding ν¯ value is not achievable. Accordingly, bisection search can be applied to find the maximum common throughput $\bar { \nu } ^ { \mathrm { { o p t } } }$ iteratively. We thus focus on solving (P2) in the following.

Second, (P2) is still difficult to be directly solved, due to the non-convex objective function and the non-convex constraint (28). Fortunately, since the GBS-MT communication is independent of $r _ { U }$ , with given fixed $\rho$ and $r _ { I }$ , we can first optimize $r _ { U }$ to maximize the achievable UAV-MT common throughput $R _ { U } ( \rho , r _ { I } , r _ { U } )$ while satisfying the constraint (29), i.e.,

$$
\text {(P3)}: \max _ {r _ {I} \leq r _ {U} \leq r _ {G}} \bar {R} _ {U} (\rho , r _ {I}, r _ {U}).
$$

Denote the optimal value of (P3) as $\bar { R } _ { U } ^ { \operatorname* { m a x } } ( \rho , r _ { I } )$ . Problem (P3) can be optimally solved based on geometry as detailed in Section III-D1 below.

Third, after $\bar { R } _ { U } ^ { \operatorname* { m a x } } ( \rho , r _ { I } )$ is obtained from (P3), problem (P2) can be equivalently reduced to the following problem.

$$
\text {(P4)}: \min _ {\rho , r _ {I}} f (\rho , r _ {I}, \bar {\nu})
$$

s.t. (30) and (31),

$$
\bar {\nu} - \bar {R} _ {U} ^ {\max} (\rho , r _ {I}) \leq 0, \tag {32}
$$

where the objective function $\mathrm { P _ { o u t } } ( \rho , r _ { I } , \bar { \nu } )$ of (P2) is replaced by $f ( \rho , r _ { I } , \bar { \nu } )$ based on monotonicity in (26), and the constraint (28) is replaced by (32).

Finally, by exploiting the monotonicity of the objective function and constraint function over $\rho$ and $r _ { I } , \ ( \mathrm { P 4 } )$ can be optimally solved by bi-section searching for $\rho$ in the range $0 < \rho < 1$ for given $r _ { I }$ in the inner loop, while performing a one-dimensional search for $r _ { I }$ in the range $0 \leq r _ { I } \leq r _ { G }$ in the outer loop. The details are provided in Section III-D2.

1) Optimizing $r _ { U } .$ To solve (P3) for given $\rho$ and $r _ { I } .$ , we need to maximize $\bar { R } _ { U } ( \rho , r _ { I } , r _ { U } )$ in (17) by optimizing $r _ { U }$ , which is equivalent to minimizing $d _ { \operatorname* { m a x } } = \operatorname* { m a x } ( d _ { A } , d _ { B } )$ given by (10), (11) and (12). For $r _ { I } \le r _ { U } \le r _ { G }$ and a given small value $\psi \leq \psi _ { 0 }$ (ψ0 will be derived later), the minimum $d _ { \mathrm { m a x } }$ can be found by letting $d _ { A } = d _ { B }$ in (11) and (12), which yields

$$
r _ {U} ^ {*} = \frac {r _ {G} + r _ {I}}{2 \cos (\psi / 2)}, \tag {33}
$$

and

$$
d _ {\max} ^ {*} (r _ {I}) = \sqrt {\frac {(r _ {G} + r _ {I}) ^ {2}}{2 (\cos \psi + 1)} - r _ {I} r _ {G}}, \tag {34}
$$

where $d _ { \mathrm { m a x } } ^ { \ast } ( { \boldsymbol { r } } _ { I } )$ is a decreasing function of $r _ { I }$ . Note that the coordinate $( r _ { U } ^ { * } , 0 )$ corresponds to the intersection point of the horizontal axis and the perpendicular bisector of the line segment AB, as shown in Fig. 2. By geometry, it can be verified that when $r _ { U } ~ = ~ r _ { U } ^ { * }$ , the minimum value of $d _ { \mathrm { m a x } }$ is achieved as that given by (34). This conclusion is valid when the coordinate $( r _ { U } ^ { * } , 0 )$ does not go beyond the mid-point $\textstyle ( r _ { G } \cos { \frac { \psi } { 2 } } , 0 )$ of the line segment $\mathbf { B } \mathbf { B } ^ { \ast }$ , since otherwise the minimum value of $d _ { \mathrm { m a x } }$ simply equals half the length of the line segment $\mathbf { B } \mathbf { B } ^ { \prime }$ , i.e., $r _ { G }$ sin $\frac { \bar { \psi } } { 2 }$ . Therefore, from $\begin{array} { r } { \frac { \bar { r } _ { G } + r _ { I } } { 2 \cos ( \psi / 2 ) } \le } \end{array}$ $r _ { G } \cos { \frac { \psi } { 2 } }$ , we obtain the threshold $\psi _ { 0 }$ as follows.

$$
\psi_ {0} \triangleq \arccos \frac {r _ {I}}{r _ {G}} <   \frac {\pi}{2}. \tag {35}
$$

By substituting $d _ { \operatorname* { m a x } { } } ~ = ~ d _ { \operatorname* { m a x } { } } ^ { \ast } ( r _ { I } )$ in (17), we obtain the optimal value of (P3) which is given by

$$
\bar {R} _ {U} ^ {\max} (\rho , r _ {I}) = \frac {\rho}{\mu \lambda \pi (r _ {G} ^ {2} - r _ {I} ^ {2})}
$$

$$
\times \log_ {2} \left(1 + \frac {\eta_ {0} P _ {U} G _ {U} \left(d _ {\max} ^ {*} (r _ {I})\right)}{\rho \left(\left(d _ {\max} ^ {*} (r _ {I})\right) ^ {2} + H _ {U} ^ {2}\right)}\right). \tag {36}
$$

It can be verified that $\bar { R } _ { U } ^ { \operatorname* { m a x } } ( \rho , r _ { I } )$ is an increasing function of both $\rho$ and $r _ { I }$ .

2) Optimizing $\rho$ and $r _ { I } .$ Next, we investigate the performance trade-off between GBS-MT and UAV-MT communications by optimizing $\rho$ and $r _ { I }$ in (P4). In general, a larger $\rho$ means that more bandwidth is allocated to the UAV, thus improving the max-min throughput of UAV-MT communications but at the cost of degrading that of GBS-MT communications. On the other hand, a larger $r _ { I }$ means that more MTs are to be served by the GBS, which also degrades the max-min throughput of GBS-MT communications while improving that of UAV-MT communications.

Specifically, given ν¯ in (P4), the objective function $f ( \rho , r _ { I } , \bar { \nu } )$ (defined in (25)) is a non-convex function of either $\rho$ or $r _ { I }$ . Moreover, the constraint in (32) is a non-convex constraint since $\bar { \nu } - \bar { R } _ { U } ^ { \operatorname* { m a x } } ( \rho , r _ { I } )$ (with $\bar { R } _ { U } ^ { \operatorname* { m a x } } ( \rho , r _ { I } )$ given in (36)) is non-convex with respect to $r _ { I }$ . Therefore, (P4) is a non-convex optimization problem and thus cannot be directly solved with the standard convex optimization techniques.

Fortunately, we can exploit the monotonicity of $\bar { R } _ { U } ^ { \operatorname* { m a x } } ( \rho , r _ { I } )$ and $f ( \rho , r _ { I } , \bar { \nu } )$ ) with $\rho$ and $r _ { I }$ to devise an efficient algorithm to solve (P4) optimally as follows. It is observed that given $\bar { \nu }$ and $r _ { I } .$ , the objective function $f ( \rho , r _ { I } , \bar { \nu } )$ increases with $\rho$ while the constraint function $\bar { \nu } - \bar { R } _ { I J } ^ { \operatorname* { m a x } } ( \rho , r _ { I } )$ decreases with $\rho .$ Therefore, in order to minimize $f ( \rho , r _ { I } , \bar { \nu } )$ , we should choose the minimum value of $\rho$ that satisfies the constraint (32). Since $\bar { \nu } - \bar { R } _ { U } ^ { \operatorname* { m a x } } ( \rho , r _ { I } )$ decreases with $\rho ,$ a bisection search for $\rho$ in the range of $0 < \rho < 1$ can be performed to check the feasibility of the constraint (32), and to find the minimum $\rho$ if feasible. Then, we can perform a one-dimensional search for the optimal $r _ { I }$ in the range of $0 \le r _ { I } \le r _ { G }$ to further minimize the objective function $f ( \rho , r _ { I } , \bar { \nu } )$ in (P4).

# IV. SPECTRUM REUSE

In this section, we extend our analysis to the spectrum reuse scheme where the common spectrum pool of total bandwidth W Hz is shared by both the GBS and UAV, which is expected to further improve the spectrum efficiency as long as the mutual interference is well controlled between the UAV-MT and GBS-MT communications. To this end, we propose to leverage the joint use of directional/sectorized antennas at the UAV/GBS to eliminate the mutual interference and thus maximize the throughput performance. Since there is no need to design $\rho$ in the spectrum reuse case, we focus on the joint optimization of the UAV trajectory radius $r _ { U }$ and the user partitioning distance threshold $r _ { I }$ to maximize the minimum throughput ν¯ of all MTs.

# A. GBS-MT Communication

1) Directional Transmission: As shown in Fig. $^ { 3 , }$ we assume that the GBS dynamically adjusts its transmission direction towards the shadowed sector region $\boldsymbol { S } _ { b }$ with central angle $\Phi _ { G } ,$ , which is non-overlapping with the central angle ψ of the UAV association region $ { \boldsymbol { S } } _ { a }$ at each time, and thus causes no interference to the UAV-MT communications. Assume that the GBS antenna gain in the $\Phi _ { G }$ direction remains as $G _ { G }$ for fair comparison with the orthogonal sharing case. We further assume that the non-cell-edge MTs in $\boldsymbol { S _ { b } }$ are associated with the GBS for communications at time $t ,$ denoted by the set $\kappa _ { G } ( t ) \in \mathcal { K } _ { G }$ . Then on average there are $| \mathcal { K } _ { G } ( t ) | = \lambda r _ { I } ^ { 2 } \Phi _ { G } / 2$

![](images/d51c36ea9b1fddef79ed1e3ee9fe65efc3efafe186ced843dfb381b9f4165406.jpg)

<details>
<summary>text_image</summary>

r_G
r_I
Φ_C
O
A
ψ
r_U
A'
B
r_c
B'
UAV Association region S_a
GBS Association region S_b
</details>

Fig. 3. Proposed spectrum reuse model with interference-free concurrent cyclical multiple access for both UAV-MT and GBS-MT communications.

MTs in $\kappa _ { G } ( t )$ . Assume that the GBS also adopts the simple equal bandwidth allocation scheme, i.e., each MT in $\kappa _ { G } ( t )$ is allocated with an effective normalized bandwidth $b _ { G } ( t ) =$ $1 / | \mathcal { K } _ { G } ( t ) | = 2 / ( \lambda r _ { I } ^ { 2 } \Phi _ { G } )$ .

Thanks to the directional antenna at the UAV, there is practically negligible interference from the UAV to the GBS-MT communications as well. As the UAV flies cyclically, the GBS adapts its transmission direction accordingly, which can be implemented by adaptive beamforming techniques or approximately by on-off control of the sectorized antennas in practice. As a result, the GBS-MT communications also become cyclical multiple access with the same period $T$ as the UAV-MT communications, where each MT $k ~ \in ~ { \cal K } _ { G }$ has an access delay $\begin{array} { r } { D _ { k } = ( 1 - \frac { \Phi _ { G } } { 2 \pi } ) T } \end{array}$ .

2) Power Allocation: At time t, assume that the GBS adopts the $\because \mathrm { s l o w } ^ { \prime \prime }$ channel inversion power control similar to Section III-B1, despite that the associated MTs become $\kappa _ { G } ( t )$ instead. Assume that the GBS transmits with the same power $p _ { G } ( r )$ for MTs $k \in \mathcal { K } _ { G } ( t )$ at the same distance r from the GBS. The transmit power $p _ { G } ( r )$ is allocated such that all MTs $k \in \mathcal { K } _ { G } ( t )$ have the equal average SNR at the receiver, denoted by $\bar { \gamma } ( t )$ . Thus, $p _ { G } ( r )$ can be expressed as

$$
p _ {G} (r) = \frac {\bar {\gamma} (t) b _ {G} (t) \sigma^ {2}}{\bar {g} _ {k} G _ {G}} = \frac {\bar {\gamma} (t) b _ {G} (t) (H _ {G} ^ {2} + r ^ {2}) ^ {\frac {n}{2}}}{\kappa_ {0}}. \tag {37}
$$

Let $P _ { G }$ denote the maximum transmit power of the GBS. Then the total transmit power to all MTs in $\kappa _ { G } ( t )$ needs to satisfy the following constraint:

$$
\lambda \int_ {\phi = 0} ^ {\Phi_ {G}} \int_ {r = 0} ^ {r _ {I}} p _ {G} (r) r \mathrm{d} r \mathrm{d} \phi = P _ {G}. \tag {38}
$$

The average SNR can be obtained from (37) and (38) as

$$
\bar {\gamma} (t) = \frac {\kappa_ {0} P _ {G}}{\Phi_ {G} \lambda b _ {G} (t) L (r _ {I})} = \frac {\kappa_ {0} P _ {G} r _ {I} ^ {2}}{2 L (r _ {I})}, \tag {39}
$$

where $L ( r _ { I } )$ is given by (22). The instantaneous achievable rate for MT $k \in \mathcal { K } _ { G } ( t )$ in bps/Hz is then given by

$$
R _ {k} (t) = b _ {G} (t) \log_ {2} \left(1 + \bar {\gamma} (t) \zeta_ {k}\right). \tag {40}
$$

3) Outage Probability: Due to the small-scale fading of the GBS-MT channel, an outage event occurs when the GBS-MT link cannot support the desired instantaneous rate $\begin{array} { r } { \bar { \nu } _ { G } \triangleq \frac { 2 \pi } { \Phi _ { G } } \bar { \nu } } \end{array}$ 2π ν¯, where ν¯ is the desired average throughput in a period T . According to (40), the outage probability for MT $k \in \mathcal { K } _ { G } ( t )$ is given by

$$
\begin{array}{l} \mathrm{P} _ {\text { out }, k} (t) = \operatorname * {P r} \left\{b _ {G} (t) \log_ {2} \left(1 + \bar {\gamma} (t) \zeta_ {k}\right) <   \bar {\nu} _ {G} \right\} \\ = \operatorname * {P r} \left\{\frac {2}{\lambda r _ {I} ^ {2} \Phi_ {G}} \log_ {2} (1 + \bar {\gamma} (t) \zeta_ {k}) <   \frac {2 \pi}{\Phi_ {G}} \bar {\nu} \right\} \\ = \operatorname * {P r} \left\{\zeta_ {k} <   \left(2 ^ {\pi r _ {I} ^ {2} \cdot \lambda \bar {\nu}} - 1\right) / \bar {\gamma} (t) \right\} \\ = 1 - \exp \left(- (2 ^ {\pi r _ {I} ^ {2} \cdot \lambda \bar {\nu}} - 1) / \bar {\gamma} (t)\right) \\ = 1 - \exp \left(\frac {- 2 (2 ^ {\pi r _ {I} ^ {2} \cdot \lambda \bar {\nu}} - 1) L (r _ {I})}{\kappa_ {0} P _ {G} r _ {I} ^ {2}}\right) \triangleq \mathrm{P} _ {\text { out }} ^ {\prime} (r _ {I}, \bar {\nu}), \tag {41} \\ \end{array}
$$

which is identical for all MTs $k \in \mathcal { K } _ { G } ( t )$ . It can be verified from (41) that $\mathrm { P } _ { \mathrm { o u t } } ^ { \prime } ( r _ { I } , \bar { \nu } )$ is an increasing function of $r _ { I }$ and $\bar { \nu } .$ Note that $\mathrm { P } _ { \mathrm { o u t } } ^ { \prime } ( r _ { I } , \bar { \nu } )$ is equal to $\mathrm { P _ { o u t } } ( \rho , r _ { I } , \bar { \nu } )$ in (26) with $\rho = 0$ , i.e., when the whole bandwidth is used by the GBS. Since $\mathrm { P _ { o u t } } ( \rho , r _ { I } , \bar { \nu } )$ is an increasing function of $\rho ,$ the outage probability decreases to its minimum value when $\rho ~ = ~ 0$ . Therefore, the spectrum reuse scheme has a lower outage probability than that of the orthogonal sharing scheme under the same $r _ { I }$ and $\bar { \nu } ,$ which implies a higher throughput achievable by the spectrum reuse scheme under the same outage requirement. Finally, note that the central angle $\Phi _ { G }$ does not affect $\mathrm { P } _ { \mathrm { o u t } } ^ { \prime } ( r _ { I } , \bar { \nu } )$ , which can thus be chosen in practice to be as large as possible to reduce the user access delay, provided that the leakage interference to the UAV-MT communications is kept sufficiently low.

# B. UAV-MT Communication

Since the interference from the GBS is eliminated, the UAV-MT communication is similar to that in Section III-A, but the whole bandwidth is now used by the UAV. Therefore, the common throughput $\hat { R } _ { U } ^ { \prime }$ for the cell-edge MTs served by the UAV follows from (17) with $\rho = 1$ , i.e.,

$$
\bar {R} _ {U} ^ {\prime} (r _ {I}, r _ {U}) = \frac {1}{\mu \lambda \pi (r _ {G} ^ {2} - r _ {I} ^ {2})} \log_ {2} \left(1 + \frac {\eta_ {0} P _ {U} G _ {U} (d _ {\max})}{d _ {\max} ^ {2} + H _ {U} ^ {2}}\right). \tag {42}
$$

which is a function of $r _ { I }$ and $r _ { U }$ .

# C. Problem Formulation

In this subsection, we formulate the optimization problem to maximize the common throughput ν¯ of all MTs subject to the maximum outage probability constraint of GBS-MT links, by jointly optimizing the user partitioning distance threshold $r _ { I }$ , and the UAV trajectory radius $r _ { U }$ . The problem can be formulated as

$$
\text {(P5)}: \max _ {r _ {I}, r _ {U}, \bar {\nu}} \quad \bar {\nu}
$$

$\mathrm { s . t . } \quad \mathrm { P } _ { \mathrm { o u t } } ^ { \prime } ( r _ { I } , \bar { \nu } ) \leq \bar { \mathrm { P } } _ { \mathrm { o u t } } ,$ (43)

$$
\bar {R} _ {U} ^ {\prime} (r _ {I}, r _ {U}) \geq \bar {\nu}, \tag {44}
$$

$$
r _ {I} \leq r _ {U} \leq r _ {G}, \tag {45}
$$

$$
0 \leq r _ {I} \leq r _ {G}. \tag {46}
$$

We denote the optimal solution to (P5) as $( r _ { I } ^ { \mathrm { o p t } ^ { \ast } } , r _ { U } ^ { \mathrm { o p t } ^ { \ast } } )$ opt’ and the corresponding optimal common throughput as $\bar { \nu } ^ { \mathrm { { o p t } ^ { \prime } } }$ ’. Note that (P5) is similar to (P1), except that the bandwidth partition between the UAV and GBS is no more needed.

# D. Proposed Solution

Problem (P5) can be solved using similar methods as in Section III-D. First, for any given $r _ { I } ,$ the UAV trajectory radius rU can be optimized to achieve the maximum UAV-MT throughput, denoted as $\bar { R } _ { U } ^ { \prime \mathrm { m a x } } ( r _ { I } )$ , which, by following Section III-D1, is given by

$$
\begin{array}{l} \bar {R} _ {U} ^ {\prime \max} (r _ {I}) = \frac {1}{\mu \lambda \pi (r _ {G} ^ {2} - r _ {I} ^ {2})} \\ \times \log_ {2} \left(1 + \frac {\eta_ {0} P _ {U} G _ {U} \left(d _ {\max} ^ {*} (r _ {I})\right)}{\left(d _ {\max} ^ {*} (r _ {I})\right) ^ {2} + H _ {U} ^ {2}}\right), \tag {47} \\ \end{array}
$$

where the optimal $r _ { U }$ follows from (33) and $d _ { \operatorname* { m a x } } ^ { * } ( r _ { I } )$ is given by (34). It can be verified that $\bar { R } _ { U } ^ { \prime \mathrm { m a x } } ( r _ { I } )$ is an increasing function of $r _ { I }$ .

Second, for any given $r _ { I }$ , the maximum GBS-MT throughput, denoted as $\bar { R } _ { G } ^ { \prime \mathrm { m a x } } ( r _ { I } )$ , can be found as ν¯ when the constraint (43) holds with equality. It can be verified that $\bar { R } _ { G } ^ { \prime \mathrm { m a x } } ( r _ { I } )$ is a decreasing function of $r _ { I }$ . Finally, we can perform a bisection search to find the optimal $r _ { I } ,$ which achieves the max-min throughput $\begin{array} { r l } { \bar { \nu } ^ { \mathrm { o p t } ^ { \ast } } } & { { } = } \end{array}$ max min $\{ \bar { R } _ { U } ^ { \prime \mathrm { m a x } } ( r _ { I } ) , \bar { R } _ { G } ^ { \prime \mathrm { m a x } } ( r _ { I } ) \}$ }.

Note that the proposed spectrum reuse scheme requires adaptive directional transmissions at the GBS and cyclical multiple access for the GBS-MT communications, which thus requires additional complexity for implementation. However, thanks to the interference avoidance, the GBS and UAV can both access the common spectrum pool for concurrent communications, which thus further improves the system throughput, as will be shown in the next section.

# E. Further Discussions

1) Relaxation of Fixed UAV Altitude: For the schemes proposed above, the optimization results provide useful guidelines to practically design the UAV trajectory radius $r _ { U } .$ bandwidth allocation portion $\rho ,$ and user partitioning distance threshold $r _ { I } .$ , which jointly determine the radius $r _ { c }$ of the UAV coverage area so that the scheduled MTs in $\kappa _ { U } ( t )$ communicating with the UAV are guaranteed to lie within the UAV coverage area at any time t.

We have assumed that the UAV has a given altitude $H _ { U }$ for simplicity. In the case where the UAV flies at different altitudes along its optimized trajectory, the UAV antenna beamwidth $\Phi _ { U }$ can be adjusted accordingly to achieve the same coverage area of any fixed radius $r _ { c } = H _ { U }$ tan $\Phi _ { U }$ , and thus there is no fundamental change of our results with variable altitude. Moreover, the coverage radius $r _ { c }$ is only a theoretical upper bound to guarantee that all currently scheduled MTs communicating with the UAV lie within the coverage area. Therefore, a certain level of altitude/beamwidth control error in practice can be tolerated for our proposed design.

2) Requirement of User Location Information: In this paper, we mainly target for outdoor scenarios with temporary hot

spot, where our proposed optimization schemes only require the statistics of the user distribution instead of the exact location of each ground user. The obtained results provide a theoretical guideline to design the UAV trajectory, bandwidth allocation, and user partitioning in practice. Assume that the UAV follows the optimized trajectory to serve the MTs within its ground coverage area at each time instant, where the scheduled MTs typically have high received power from the UAV. As a result, the served MTs over time can be determined by using the reference signal received power (RSRP). Although accurate location information of the ground MTs can be a plus, it is not a must for our proposed schemes.

More specifically, we assume that the MTs are uniformly and randomly distributed by following a homogeneous Poisson point process (HPPP) with a certain density λ, where λ is constant in the considered cell. Therefore, a hotspot cell occurs when the user density λ is large. Under this model, a circular UAV trajectory with a constant speed along the cell edge effectively shortens the communication distance from the UAV to its associated cell-edge users, thus improving the system overall throughput. On the other hand, in scenarios where there exist “hotspots in hotspot” and the specific locations of such non-uniformly distributed users are known, the UAV trajectory and flying speed can be optimized to further improve the throughput performance. For example, the UAV can fly closer to or hover above “hotspots in hotspot” so as to shorten the communication distance and/or maintain a longer communication duration for the users therein to improve the throughput.

3) Extension to Multiple Cells: In this paper, as a preliminary study of our proposed new network architecture, we focus on the single-cell setup to investigate the fundamental design issues such as the UAV trajectory, spectrum sharing and multiple access, while the significant performance gain shown for the single-cell case will be the motivation for us to investigate UAV-aided cellular offloading for the more general multi-cell case in future work. Here we briefly discuss the possible extensions to the multi-cell setup.

Firstly, when multiple UAVs are available for a single cell, the additional UAVs can be arranged along the designed trajectory with equal separation from each other, which helps reduce the access delay and also improve the throughput. Secondly, the results developed in the current paper can be directly applied when a single UAV is available for each cell in the multi-cell scenario. There are various possible ways to mitigate the interference between a UAV flying along the cell edge and its neighboring cells. For example, in the current paper we have considered the use of a directional antenna at the UAV, which already limits the interference to/from neighboring cells. Another issue is the collision avoidance between UAVs serving adjacent cells. Fortunately, in the current paper the optimized UAV trajectory lies inside the cell boundary, which theoretically avoids the collision among UAVs in different cells. Thirdly, when a single UAV is responsible for serving multiple cells, the UAV can be scheduled to serve these cells sequentially, for each of them following circular or other optimized trajectories, which is worth studying in future work.

Finally, when a macro cell is overloaded and yet there are relatively few micro BSs (small cells) nearby, the UAV can still be employed to help offload data traffic from the macro BS. In such a case, the specific design of the UAV offloading scheme, including the UAV trajectory, user partitioning and spectrum sharing, needs to take into account the locations, user partitioning and spectrum sharing of the existing macro BS and micro BSs, which deserves further investigation.

4) Energy Constraint for UAVs: In practice, UAVs usually have limited endurance due to on-board energy constraint. One potential solution for it is to employ multiple UAVs that take turns to provide service and recharge/swap battery on the ground. Thanks to emerging techniques such as automated battery swap and recharge [28], a single UAV can accomplish long-endurance missions by automatically swapping its depleted battery at a ground charging station with a fully charged battery. Moreover, in the case with fixed-wing UAVs [29], their flight endurance is typically much longer than that of rotary-wing UAVs, which can be several hours and thus are suitable for our considered application. In Section V-B, a quantitative example is provided for the energy efficiency of UAV-aided communication in our considered system.

On the other hand, the proposed UAV-assisted offloading scheme is mainly targeted for the scenarios of temporary hotspot where the existing ground infrastructure is incapable of serving the suddenly-surged traffic demand, and it is practically costly or takes too long to install new ground infrastructure to meet such high demand. In these cases, UAVs can be more swiftly deployed in the target area to provide high throughput for the ground MTs temporally. Therefore, with the above methods for prolonging the UAV flight endurance, the proposed UAV-assisted cellular offloading scheme offers a viable new approach to resolve the hot-spot issue in the forthcoming 5G and beyond.

# V. NUMERICAL RESULTS

In this section, numerical results are provided to validate our analysis and evaluate the performance of our proposed schemes, which consist of two parts. In the first part, we evaluate the performance of our proposed schemes with optimized and fixed design parameters, respectively, and also compare with the benchmark scheme with GBS only. In the second part, the proposed scheme is further compared with the conventional cell-edge throughput enhancement scheme which deploys one or more micro/small cells at the edge of the macro cell.

# A. Performance Evalution of the Proposed Schemes

For the orthogonal sharing scheme, we obtain the optimal solution $( \rho ^ { \mathrm { o p t } } , r _ { I } ^ { \mathrm { o p t } } , r _ { U } ^ { \mathrm { o p t } } )$ , rI to (P1) with the maximum common throughput $\bar { \nu } ^ { \mathrm { { o p t } } }$ and corresponding maximum spatial throughput $\theta ^ { \mathrm { o p t } } = \lambda \bar { \nu } ^ { \mathrm { o p t } }$ . We compare the spatial throughput with those of two benchmark schemes. The first benchmark considers fixed design variables with $\rho = 0 . 5 , \ r _ { I } / r _ { G } = 0 . 5$ and $r _ { U }$ following (33), where the spatial throughput is taken to be the minimum throughput of the GBS- and UAV-served areas, i.e., $\theta ^ { \mathrm { f i x e d } } \triangleq \operatorname* { m i n } ( \theta _ { G } , \theta _ { U } )$ . The second benchmark considers the GBS-only case without the use of UAV. On the other hand, for the spectrum reuse scheme, we obtain the optimal solution (ropt’ , $( r _ { I } ^ { \mathrm { o p t } ^ { \prime } } , r _ { U } ^ { \mathrm { o p t } ^ { \prime } } )$ to (P5) with the maximum common throughput $\bar { \nu } ^ { \mathrm { o p t } ^ { \prime } }$ and corresponding maximum spatial throughput $\theta ^ { \mathrm { o p t } ^ { \prime } } =$ $\lambda \bar { \nu } ^ { \mathrm { { o p t } ^ { \ast } } }$ . We also compare with the benchmark scheme with fixed design variable $r _ { I } / r _ { G } = 0 . 5$ and $r _ { U }$ following (33).

![](images/7afbc9edc9c56cb2287a35b6596b73e5cb0916fb4527924a93d2efce22434606.jpg)

<details>
<summary>line</summary>

| UAV Transmit Power PU (dBm) | analytic (rI = rI^opt, reuse) | simulation (rI = rI^opt, reuse) | analytic (rI = rI^opt, ρ = ρ^opt, ortho.) | simulation (rI = rI^opt, ρ = ρ^opt, ortho.) | analytic (rI = rG, ρ = 0, GBS-only) | simulation (rI = rG, ρ = 0, GBS-only) |
| --------------------------- | ----------------------------- | ------------------------------- | ------------------------------------------ | -------------------------------------------- | ----------------------------------- | ------------------------------------- |
| 0                           | 3.8                           | 2.0                             | 1.7                                        | 1.6                                          | 1.2                                 | 1.1                                   |
| 5                           | 4.2                           | 2.5                             | 2.0                                        | 1.8                                          | 1.4                                 | 1.3                                   |
| 10                          | 4.6                           | 3.0                             | 2.3                                        | 2.0                                          | 1.6                                 | 1.5                                   |
| 15                          | 5.0                           | 3.5                             | 2.6                                        | 2.2                                          | 1.8                                 | 1.7                                   |
| 20                          | 5.4                           | 4.0                             | 2.9                                        | 2.4                                          | 2.0                                 | 1.9                                   |
| 25                          | 5.8                           | 4.5                             | 3.2                                        | 2.6                                          | 2.2                                 | 2.1                                   |
| 30                          | 6.2                           | 5.0                             | 3.5                                        | 2.8                                          | 2.4                                 | 2.3                                   |
| 35                          | 6.6                           | 5.5                             | 3.8                                        | 3.0                                          | 2.6                                 | 2.5                                   |
| 40                          | 7.0                           | 6.0                             | 4.1                                        | 3.2                                          | 2.8                                 | 2.7                                   |
</details>

Fig. 4. Spatial throughput θ under different UAV transmit power $P _ { U }$   
![](images/b0b53d68626176103ad93af7d48ddb37f18e6a29525e152b31c8215f72d0867a.jpg)

<details>
<summary>line</summary>

| UAV Transmit Power PU (dBm) | ρ^opt, orthogonal | r_I^opt / r_G, orthogonal | r_I^opt' / r_G, reuse |
| --------------------------- | ----------------- | ------------------------- | -------------------- |
| 0                           | 0.5               | 0.75                      | 0.75                 |
| 5                           | 0.65              | 0.65                      | 0.7                  |
| 10                          | 0.65              | 0.6                       | 0.68                 |
| 15                          | 0.7               | 0.55                      | 0.65                 |
| 20                          | 0.8               | 0.45                      | 0.63                 |
| 25                          | 0.85              | 0.4                       | 0.6                  |
| 30                          | 0.9               | 0.35                      | 0.58                 |
| 35                          | 0.92              | 0.3                       | 0.57                 |
| 40                          | 0.95              | 0.25                      | 0.56                 |
</details>

Fig. 5. Optimal solutions of orthogonal sharing versus spectrum reuse under different UAV transmit power $P _ { U }$ .

For each of these schemes, the obtained analytical results are verified by averaging over 100 independent realizations of the user locations. Each realization is drawn from a homogeneous Poisson point process (HPPP) with the given user density λ. In each realization, the GBS channel inversion power control is simulated based on specific user locations, while the parameter $\mu$ for UAV-MT association can be obtained as the average value over the 100 realizations for our analytical results. We then obtain the average spatial throughputs $\bar { \theta } _ { G }$ and ${ \bar { \theta } } _ { U }$ for the GBS- and UAV-served areas over the 100 realizations, respectively. The following parameters are used: $f _ { c } ~ = ~ 2$ GHz, W = 10 MHz, $N _ { 0 } = - 1 7 4$ dBm/Hz, $H _ { U } = 1 0 0$ m, $H _ { G } = 2 0$ m, $r _ { G } = 1 0 0 0$ m, $G _ { G } = 1 6 ~ \mathrm { d B i }$ , $\begin{array} { r } { n = 3 , \psi = \frac { \pi } { 6 } } \end{array}$ , $\begin{array} { r } { \Phi _ { G } = \frac { 4 \pi } { 3 } } \end{array}$ and $\bar { \mathsf { P } } _ { \mathrm { o u t } } = 0 . 0 1$ .

In the first set of simulations, we choose λ = 1000 $\mathrm { M T s / k m ^ { 2 } }$ and $P _ { G } = 4 0 $ dBm, and simulate the above schemes with different UAV transmit power $P _ { U }$ , where the UAV’s available transmit power $P _ { U }$ is added to the GBS transmit power $P _ { G }$ in the GBS-only benchmark case for fair comparison. The throughput results are plotted in Fig. 4, and the optimal solutions to (P1) and (P5) are plotted in Fig. 5, respectively. First, it can be observed from Fig. 4 that the analytical results match well with the simulation results in all cases. Second, for the orthogonal sharing case, our proposed scheme even with fixed (unoptimized) $\rho$ and $r _ { I }$ improves the spatial throughput over the GBS-only case when $P _ { U } \ge 1 0$ dBm. On the other hand, our proposed scheme with optimized $\rho$ and $r _ { I }$ further improves over the case with fixed $\rho$ and $r _ { I } ,$ and achieves the maximum spatial throughput which is significantly higher than that of the GBS-only case for all $P _ { U }$ values. Moreover, as $P _ { U }$ increases, it can be seen from Fig. 5 that $\rho ^ { \mathrm { { o p t } } }$ increases and $r _ { I } ^ { \mathrm { o p t } } / r _ { G }$ decreases for the orthogonal sharing scheme, which suggests that more bandwidth should be allocated to the UAV to serve more MTs when the UAV is able to transmit at a higher power. In contrast, for the spectrum reuse case, it can be seen from Fig. 4 that our proposed scheme with optimized or fixed $r _ { I }$ further improves the spatial throughput significantly as compared to the corresponding orthogonal sharing case. It is also noted from Fig. 5 that the optimal solution $\dot { r } _ { I } ^ { \mathrm { o p t } ^ { \prime } }$ in the spectrum reuse scheme decreases as $P _ { U }$ increases, which suggests that more users should be served by the UAV when the UAV is able to transmit at higher power. Moreover, $r _ { I } ^ { \mathrm { o p t } ^ { \ast } }$ opt’ is larger than $r _ { I } ^ { \mathrm { o p t } }$ in the orthogonal sharing scheme as shown in Fig. 5, since the GBS in the spectrum reuse case is able to use more bandwidth and thus should serve more noncell-edge users to achieve the maximum common throughput. In summary, our proposed joint optimization solution is essential to achieve the maximum throughput of the proposed UAV-assisted hybrid network.

![](images/85b8cadf2e417ffbbe4c9100802a22e9ff9b5d2a6599e0b1c1256128315047fa.jpg)

<details>
<summary>line</summary>

| user density λ (MTs/km²) | spectrum reuse, optimized (P_G=40dBm, analytic) | spectrum reuse, optimized (P_G=40dBm, simulation) | orthogonal sharing, optimized (P_G=40dBm, analytic) | orthogonal sharing, optimized (P_G=40dBm, simulation) | GBS only (P_G=40dBm, analytic) | GBS only (P_G=40dBm, simulation) | GBS only (P_G=30dBm, analytic) | GBS only (P_G=30dBm, simulation) |
| ------------------------ | ----------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | ------------------------------ | ------------------------------ | ----------------------------- | ----------------------------- |
| 100                      | 480                                             | 280                                                | 400                                                | 270                                                | 70                             | 65                           | 75                            | 60                          |
| 200                      | 350                                             | 220                                                | 250                                                | 180                                                | 50                             | 45                           | 55                            | 40                          |
| 300                      | 250                                             | 150                                                | 180                                                | 120                                                | 35                             | 30                           | 40                            | 25                          |
| 400                      | 200                                             | 120                                                | 140                                                | 90                                                 | 30                             | 25                           | 35                            | 20                          |
| 500                      | 150                                             | 100                                                | 110                                                | 75                                                 | 25                             | 20                           | 30                            | 15                          |
| 600                      | 120                                             | 80                                                 | 90                                                 | 65                                                 | 20                             | 15                           | 25                            | 10                          |
| 700                      | 100                                             | 70                                                 | 80                                                 | 60                                                 | 15                             | 10                           | 20                            | 5                           |
| 800                      | 80                                              | 60                                                 | 70                                                 | 55                                                 | 10                             | 5                            | 15                            | 5                           |
| 900                      | 70                                              | 55                                                 | 65                                                 | 50                                                 | 5                              | 5                            | 10                            | 5                           |
| 1000                     | 60                                              | 50                                                 | 60                                                 | 45                                                 | 5                              | 5                            | 10                            | 5                           |
</details>

Fig. 6. Common throughput ν¯ under different user density λ.

To illustrate the offloading performance more explicitly, in the second set of simulations, we compare the maximum user density $\lambda _ { \mathrm { m a x } }$ that can be supported by various schemes under the constraint that the common throughput per MT $\bar { \nu }$ should be no less than a minimum required value $\bar { \nu } _ { \mathrm { m i n } }$ . To this end, we consider the orthogonal sharing and spectrum reuse schemes with their respective optimized designs, and compare the obtained common throughput ν¯ with that of the GBS-only case under different user density λ. We choose $P _ { U } = 2 0$ dBm and $P _ { G } = 3 0 ~ $ or 40 dBm, and the results are plotted in Fig. 6. First, it can be observed from Fig. 6 that the analytical results match well with the simulation results in all cases. Second, the common throughput ν¯ decreases as the user density λ increases in all cases, since the limited resource is shared by more users. Third, suppose that the minimum desired throughput is $\bar { \nu } _ { \mathrm { m i n } } = 1 0 0$ kbps, then we can find the maximum user density $\lambda _ { \mathrm { m a x } }$ supported by each scheme. In the GBSonly case, we have $\lambda _ { \operatorname* { m a x } } < 1 0 0 ~ \mathrm { M T s / k m ^ { 2 } }$ for the case with $P _ { G } = 3 0 ~ $ dBm, and the density further increases to $\lambda _ { \operatorname* { m a x } } =$ 180 MTs/km2 with a larger transmit power $P _ { G } = 4 0 $ dBm. In the optimized orthogonal sharing scheme, $\lambda _ { \operatorname* { m a x } } = 3 0 0$ and 320 MTs/km2 for the cases with $P _ { G } = 3 0 ~ $ dBm and $P _ { G } =$ 40 dBm, respectively, which significantly outperforms the conventional system with GBS only. With the optimized spectrum reuse scheme, the maximum supported user density further increases to $\lambda _ { \operatorname* { m a x } } ~ = ~ 4 6 0$ and $5 5 0 \ \mathrm { M T s / k m ^ { 2 } }$ for the cases with $P _ { G } = 3 0 ~ $ dBm and $P _ { G } = 4 0 ~ \mathrm { d B m } .$ , respectively, which offers more performance gains over the optimized orthogonal sharing scheme. In summary, our proposed orthogonal sharing and spectrum reuse schemes with optimal designs can support higher user density than the GBS-only case, which shows the great potential of our proposed UAV-aided cellular offloading to address the cellular hotspot issue.

# B. Illustrative Example of UAV Energy Efficiency

The energy efficiency is another important aspect of UAV-aided communication. In this subsection, we provide a simple example to illustrate how to evaluate UAV energy efficiency in the proposed design.

An initial attempt for quantifying the energy efficiency of UAV-enabled communication is given in [23], where the energy efficiency is defined as the amount of transmitted information bits per unit energy (Joule) consumed by the UAV, which accounts for the UAV’s dominant propulsion energy consumption. For fixed-wing UAVs with level flight under normal operations, a generic energy consumption model is proposed in [23], which takes into account the UAV’s instantaneous velocity and acceleration. In particular, for the UAV with a constant flying speed V following a circular trajectory with radius $r _ { U }$ , the propulsion power is modeled in [23] as

$$
\bar {P} _ {\mathrm{cir}} (V, r _ {U}) = \left(c _ {1} + \frac {c _ {2}}{g ^ {2} r _ {U} ^ {2}}\right) V ^ {3} + \frac {c _ {2}}{V}, \tag {48}
$$

where $g \ : = \ : 9 . 8 \ : \ : \mathrm { m / s ^ { 2 } }$ is the gravitational acceleration, $c _ { 1 }$ is a modeling coefficient to account for the parasitic power for overcoming the parasitic drag due to the aircraft’s skin friction and form drag, and $c _ { 2 }$ is a modeling coefficient to account for the induced power for overcoming the lift-induced drag. As can be seen from (48), the UAV power consumption of a circular trajectory decreases with $r _ { U }$ , and for given $r _ { U }$ , there is an optimum speed $V ^ { * }$ at which the power consumption is minimized.

In our setup, the total UAV transmitted information bits within a UAV flying period $T$ can be estimated as $B \ =$ $T W \pi ( r _ { G } ^ { 2 } - r _ { I } ^ { 2 } ) \theta _ { U }$ , where W is the system bandwidth and $\theta _ { U }$ is the obtained spatial throughput over the UAV-served area. Consider an example setup of the orthogonal sharing scheme with $\rho = 0 . 5 , r _ { I } = 0 . 5 r _ { G } , \lambda = 1 0 0 0 ~ \mathrm { M T s / k m ^ { 2 } } , \psi = \pi / 6$ , $P _ { U } = 1 \mathrm { ~ W ~ }$ and $c _ { 1 } = 9 . 2 6 \times 1 0 ^ { - 4 } , c _ { 2 } = 2 2 5 0$ as given in [23], while the rest of the parameters are given in Section V-A. The optimized UAV trajectory radius follows from (33) and is given by $r _ { U } ^ { * } = ( r _ { G } + r _ { I } ) / \big ( 2 \cos ( \psi / 2 ) \big ) = 7 7 6$ m. The obtained spatial throughput is given by $\theta _ { U } \approx 3 . 0$ bps/Hz/km2.

![](images/898f05246a3ffc956e7fd2c38b205a01d6acffa5d1c8b8ef8779253c84a7ad5c.jpg)

<details>
<summary>text_image</summary>

r_micro
2
r_G
d_micro
GBS 0
Ground region served by micro BS1
x
y
Δ3
Δ4
Δ5
Δ6
Δ7
Δ8
</details>

(a) M=8

![](images/83f77c76ce0b5663839afc4c09cc7357cfe0b7ff25f79b93385e97303ab698b5.jpg)

<details>
<summary>text_image</summary>

rG
d_micro
GBS 0
Ground region served by micro BS 1
Y
X
r_μicro
r_1
r_2
r_3
r_4
r_5
r_6
r_7
r_8
r_9
r_{10}
r_{11}
r_{12}
r_{13}
r_{14}
r_{15}
r_{16}
</details>

(b) M=16   
Fig. 7. Benchmark scheme with M micro-cells at the cell edge.

The optimum speed at which the power consumption is minimized is given by $V ^ { * } ~ = ~ 2 9 . 7$ m/s [23], while the corresponding UAV propulsion power follows from (48) and is given by $\bar { P } _ { \mathrm { c i r } } ( V ^ { * } , r _ { U } ^ { * } ) = 1 0 1 . 0 3 \ \mathrm { W } .$ The overall energy efficiency of UAV communication is thus given by

$$
\begin{array}{l} \mathrm{EE} = \frac {B}{T \left(P _ {U} + \bar {P} _ {\mathrm{cir}} (V ^ {*} , r _ {U} ^ {*})\right)} = \frac {W \pi (r _ {G} ^ {2} - r _ {I} ^ {2}) \theta_ {U}}{P _ {U} + \bar {P} _ {\mathrm{cir}} (V ^ {*} , r _ {U} ^ {*})} \\ = 6 9 3 \text {   kbits / Joule. } \tag {49} \\ \end{array}
$$

# C. Comparison with Micro-Cell Offload Scheme

In this subsection, the proposed scheme is further compared with the conventional cell-edge throughput enhancement scheme which deploys micro/small cells at the edge of the macro cell. Specifically, we consider the benchmark scheme where M micro-cell BSs are uniformly placed at a distance $d _ { \mathrm { m i c r o } }$ from the GBS at the origin, which help to offload data traffic from MTs in the macro cell with radius $r _ { G }$ . Examples for $M = 8$ and $M = 1 6$ are shown in Fig. 7 (a) and (b), respectively. Denote $r _ { \mathrm { m i c r o } }$ as the radius of the disk coverage region of each micro BS, which helps to serve the MTs within its coverage region. In the case where the coverage regions of two adjacent micro BSs overlap, an MT in the overlapping region is served by its nearest micro BS. For example, the ground region served by micro BS 1 is represented by the shadowed area in Fig. 7. The remaining MTs in the macro cell which are not covered by any micro BS are associated with the GBS for communication.

Assume that each micro BS is equipped with an omnidirectional antenna at height $H _ { \mathrm { m i c r o } }$ with antenna gain $G _ { \mathrm { m i c r o } } .$ The channel between the micro BSs and the MTs is modeled similarly as to that of the GBS-MT channels. For simplicity, we investigate the case with orthogonal spectrum sharing between the GBS and the micro BSs. Assume that a portion ρmicro $( 0 < \rho _ { \mathrm { m i c r o } } < 1 )$ of the total bandwidth W is allocated to the micro BSs, where each micro BS is allocated with an equal portion of $\rho _ { \mathrm { m i c r o } } / M$ . Further assume that both the GBS and the micro BSs adopt the equal bandwidth sharing for their associated MTs, respectively. Assume that the total transmit power of the micro BSs is $P _ { \mathrm { m i c r o } } .$ , where each micro BS has an equal transmit power of $P _ { \mathrm { m i c r o } } / M$ . Further assume that both the GBS and the micro BSs adopt the lowž channel inversion power control (similar to that in Section III-B1) based on the average channel gain of their associated MTs, respectively.

![](images/70421f82d9640c70db0878b50d8c1129e883ed8c77396fdb67c49e63dbbef338.jpg)

<details>
<summary>line</summary>

| Number of micro BSs M | UAV offloading, optimized (θ bps/km²) | Micro-cell offloading, optimized (θ bps/km²) | GBS-only (θ bps/km²) | UAV offloading, optimized (ratio) | Micro-cell offloading, optimized (ratio) | GBS-only (ratio) | d* micro/rG (ratio) | r* micro/rG (ratio) | ρ* micro (ratio) |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 5.07 | 2.5 | 2.38 | 0.6 | 0.6 | 0.3 | 0.6 | 0.6 | 0.3 |
| 4 | 5.07 | 3.0 | 2.38 | 0.75 | 0.75 | 0.5 | 0.75 | 0.45 | 0.5 |
| 8 | 5.07 | 3.5 | 2.38 | 0.8 | 0.8 | 0.65 | 0.8 | 0.35 | 0.7 |
| 12 | 5.07 | 3.79 | 2.38 | 0.82 | 0.82 | 0.65 | 0.82 | 0.32 | 0.7 |
| 16 | 5.07 | 3.79 | 2.38 | 0.82 | 0.82 | 0.65 | 0.82 | 0.32 | 0.7 |
</details>

optimized parameters Fig. 8. Spatial throughput θ in the micro-cell offloading scheme with $d _ { \mathrm { m i c r o } } ^ { \ast } , \boldsymbol { r } _ { \mathrm { m i c r o } } ^ { \ast }$ and $\rho _ { \mathrm { m i c r o } } ^ { * } .$ .

Under the above setup, in the simulations we can independently generate $N = 2 0$ realizations of the MT locations which follow the HPPP distribution with given user density λ. For each realization, we obtain numerical results for the average throughput $\nu _ { G }$ and $\nu _ { \mathrm { m i c r o } }$ of the MTs served by the GBS and the micro BSs, respectively, for given $d _ { \mathrm { m i c r o } } , \ r _ { \mathrm { m i c r o } }$ and $\rho _ { \mathrm { m i c r o } } .$ . Then for given $d _ { \mathrm { m i c r o } }$ and $r _ { \mathrm { m i c r o } } .$ , we exhaustively search for the optimal ρmicro to maximize the minimum throughput $\nu = \mathrm { m i n } \{ \nu _ { G } , \nu _ { \mathrm { m i c r o } } \}$ for a given setup, and then obtain the average throughput ν¯ by averaging over the N realizations. Then we exhaustively search for the optimal $d _ { \mathrm { m i c r o } }$ and $r _ { \mathrm { m i c r o } }$ to maximize $\bar { \nu } ,$ and obtain the corresponding spatial throughput θ. The maximum spatial throughput and the corresponding optimal solutions $d _ { \mathrm { m i c r o } } ^ { * } , \ r _ { \mathrm { m i c r o } } ^ { * }$ and $\rho _ { \mathrm { m i c r o } } ^ { * }$ for $M = 1 , 4 , 8 , 1 2$ and 16 are plotted in Fig. 8, respectively. The parameter values from Section V-A are used here except the following: $\lambda ~ = ~ 1 0 0 0$ MTs/km2, $H _ { \mathrm { m i c r o } } ~ = ~ 1 0$ m, $G _ { \mathrm { m i c r o } } ~ = ~ 8$ dBi, $P _ { \mathrm { m i c r o } } = 4 0 $ dBm and $P _ { G } = 4 6 ~ \mathrm { d B m }$ .

For comparison, in Fig. 8 we also show the maximum spatial throughput obtained by our optimized UAV offloading scheme where the UAV has transmit power $P _ { U } ~ = ~ P _ { \mathrm { m i c r o } } ,$ as well as that obtained by the GBS-only scheme where $P _ { \mathrm { m i c r o } }$ is added to the transmit power $P _ { G }$ of the GBS for fair comparison. It can be seen that the spatial throughput obtained by the micro-cell offloading scheme gradually increases as the number of micro cells increases, where the optimized microcell placement and layout tend to be pushed closer to the cell edge and thus able to achieve better offloading performance compared to the benchmark scheme with the GBS only. Nevertheless, the proposed UAV offloading scheme with only one single UAV/mobile BS still significantly outperforms the micro-cell offloading scheme in terms of throughput for all values of M . The above performance gain is mainly due to the fact that the UAV in general offers better communication links to its served ground MTs due to the LoS channels and its mobility.

# VI. CONCLUSIONS

This paper proposes a new hybrid network architecture for cellular systems by leveraging the use of UAVs for data offloading. We first investigate the orthogonal spectrum sharing scheme between the UAV and GBS, and solve the problem to maximize the common throughput of all MTs in the cell by jointly optimizing the spectrum allocation, user partitioning, and UAV trajectory design. We then extend our study to the spectrum reuse scheme where the common spectrum pool is shared by both the GBS and UAV while effectively suppressing their mutual interference via adaptive directional transmissions, which further improves the spatial throughput. Numerical results show that the proposed hybrid network design significantly improves the throughput as compared to the conventional system with the GBS only. Moreover, our optimized UAV offloading scheme with only one single UAV is shown to be able to significantly outperform the conventional cell-edge throughput enhancement scheme with multiple micro/small cells in terms of throughput, besides saving the infrastructure cost. We hope that this work would lead to a new practical solution to address the hotspot issue in future 5G and beyond-5G wireless systems. There are still many important issues unsolved in the proposed new hybrid wireless network, e.g., how to extend this work to the scenarios with multiple UAVs and/or multiple cells is challenging and worth investigating in future work.

# REFERENCES

[1] J. Lyu, Y. Zeng, and R. Zhang, “Spectrum sharing and cyclical multiple access in UAV-aided cellular offloading,” in Proc. IEEE GLOBECOM, Singapore, Dec. 2017, pp. 1–6.   
[2] Y. Zeng, R. Zhang, and T. J. Lim, “Wireless communications with unmanned aerial vehicles, Opportunities and challenges,” IEEE Commun. Mag., vol. 54, no. 5, pp. 36–42, May 2016.   
[3] J. Lyu, Y. Zeng, and R. Zhang, “Cyclical multiple access in UAV-aided communications, A throughput-delay tradeoff,” IEEE Wireless Commun. Lett., vol. 5, no. 6, pp. 600–603, Dec. 2016.   
[4] Q. Wu, Y. Zeng, and R. Zhang, “Joint trajectory and communication design for multi-UAV enabled wireless networks,” IEEE Trans. Wireless Commun., vol. 17, no. 3, pp. 2109–2121, Mar. 2018.   
[5] J. Lyu, Y. Zeng, R. Zhang, and T. J. Lim, “Placement optimization of UAV-mounted mobile base stations,” IEEE Commun. Lett., vol. 21, no. 3, pp. 604–607, Mar. 2017.   
[6] R. I. Bor-Yaliniz, A. El-Keyi, and H. Yanikomeroglu, “Efficient 3-D placement of an aerial base station in next generation cellular networks,” in Proc. IEEE Int. Conf. Commun. (ICC), May 2016, pp. 1–5.   
[7] E. Kalantari, H. Yanikomeroglu, and A. Yongacoglu, “On the number and 3D placement of drone base stations in wireless cellular networks,” in Proc. IEEE VTC-Fall, Sep. 2016, pp. 1–6.   
[8] I. Bor-Yaliniz and H. Yanikomeroglu, “The new frontier in RAN heterogeneity: Multi-tier drone-cells,” IEEE Commun. Mag., vol. 54, no. 11, pp. 48–55, Nov. 2016.   
[9] M. Mozaffari, W. Saad, M. Bennis, and M. Debbah, “Unmanned aerial vehicle with underlaid device-to-device communications: Performance and tradeoffs,” IEEE Trans. Wireless Commun., vol. 15, no. 6, pp. 3949–3963, Jun. 2016.   
[10] M. Mozaffari, W. Saad, M. Bennis, and M. Debbah, “Efficient deployment of multiple unmanned aerial vehicles for optimal wireless coverage,” IEEE Commun. Lett., vol. 20, no. 8, pp. 1647–1650, Aug. 2016.   
[11] A. Al-Hourani, S. Kandeepan, and S. Lardner, “Optimal LAP altitude for maximum coverage,” IEEE Wireless Commun. Lett., vol. 3, no. 6, pp. 569–572, Dec. 2014.   
[12] C. Zhang and W. Zhang, “Spectrum sharing for drone networks,” IEEE J. Sel. Areas Commun., vol. 35, no. 1, pp. 136–144, Jan. 2017.   
[13] P. Zhan, K. Yu, and A. L. Swindlehurst, “Wireless relay communications with unmanned aerial vehicles: Performance and optimization,” IEEE Trans. Aerosp. Electron. Syst., vol. 47, no. 3, pp. 2068–2085, Jul. 2011.   
[14] Y. Zeng et al., “Throughput maximization for UAV-enabled mobile relaying systems,” IEEE Trans. Commun., vol. 64, no. 12, pp. 4983–4996, Dec. 2016.   
[15] S. Hayat, E. Yanmaz, and C. Bettstetter, “Experimental analysis of multipoint-to-point UAV communications with IEEE 802.11n and 802.11ac,” in Proc. IEEE Int. Symp. Pers. Indoor Mobile Radio Commun. (PIMRC), Hong Kong, Aug. 2015, pp. 1991–1996.

[16] B. Pearre and T. X. Brown, “Model-free trajectory optimization for wireless data ferries among multiple sources,” in Proc. IEEE GLOBECOM, Miami, FL, USA, Dec. 2010, pp. 1793–1798.   
[17] Y. Zeng, X. Xu, and R. Zhang, “Trajectory design for completion time minimization in UAV-enabled multicasting,” IEEE Trans. Wireless Commun., to be published. [Online]. Available: http://ieeexplore. ieee.org/document/8255824/   
[18] C. Zhan, Y. Zeng, and R. Zhang, “Energy-efficient data collection in UAV enabled wireless sensor network,” IEEE Wireless Commun. Lett., to be published. [Online]. Available: http://ieeexplore.ieee.org/document/ 8119562/   
[19] A. Merwaday and I. Guvenc, “UAV assisted heterogeneous networks for public safety communications,” in Proc. IEEE Wireless Commun. Netw. Conf. Workshops (WCNCW), Mar. 2015, pp. 329–334.   
[20] A. Osseiran et al., “Scenarios for 5G mobile and wireless communications: The vision of the METIS project,” IEEE Commun. Mag., vol. 52, no. 5, pp. 26–35, May 2014.   
[21] S. Dimatteo, P. Hui, B. Han, and V. O. K. Li, “Cellular traffic offloading through WiFi networks,” in Proc. IEEE 8th Int. Conf. Mobile Adhoc Sensor Syst. (MASS), Valencia, Spain, Oct. 2011, pp. 192–201.   
[22] J. G. Andrews et al., “What will 5G be?” IEEE J. Sel. Areas Commun., vol. 32, no. 6, pp. 1065–1082, Jun. 2014.   
[23] Y. Zeng and R. Zhang, “Energy-efficient UAV communication with trajectory optimization,” IEEE Trans. Wireless Commun., vol. 16, no. 6, pp. 3747–3760, Jun. 2017.   
[24] C. A. Balanis, Antenna Theory: Analysis and Design. Hoboken, NJ, USA: Wiley, 2016.   
[25] H. He, S. Zhang, Y. Zeng, and R. Zhang, “Joint altitude and beamwidth optimization for UAV-enabled multiuser communications,” IEEE Commun. Lett., vol. 22, no. 2, pp. 344–347, Feb. 2018.   
[26] LTE Unmanned Aircraft Systems—Trial Report, Qualcomm Technol., Inc., San Diego, CA, USA, May 2017.   
[27] A. Goldsmith, Wireless Communications. Cambridge, U.K.: Cambridge Univ. Press, 2005.   
[28] T. Toksoz et al., “Automated battery swap and recharge to enable persistent UAV missions,” in Proc. AIAA Infotech Aerosp. Conf., St. Louis, Missouri, USA, 2011, pp. 1–10.   
[29] UAV Factory. Small, Long-Endurance Fixed Wing Unmanned Aircraft and Subsystems. [Online]. Available: http://www. unmannedsystemstechnology.com/company/uav-factory/

![](images/634d701998071fa1a2505dce697582acf804a1e58917e2cc462176c026c2e302.jpg)

<details>
<summary>natural_image</summary>

Portrait photo of a man in a maroon shirt (no text or symbols visible)
</details>

Jiangbin Lyu (S’12–M’16) received the B.Eng. degree (Hons.) in control science and engineering, and completed the Chu Kochen Honors Program with Zhejiang University, Hangzhou, China, in 2011, and the Ph.D. degree from National University of Singapore (NUS) Graduate School for Integrative Sciences and Engineering (NGS), NUS, Singapore, in 2015, under the NGS Scholarship.

He was a Post-Doctoral Research Fellow with the Department of Electrical and Computer Engineering, NUS from 2015 to 2017. He is currently an Assistant

Professor with the School of Information Science and Engineering, Xiamen University, China. His research interests include UAV communications, cognitive radios, and cross-layer network optimization. He received the Best Paper Award at Singapore-Japan International Workshop on Smart Wireless Communications in 2014. He serves as a reviewer for various IEEE journals, including JSAC, TWC, TMC, TCOM, TVT, IoT Journal, CommLet, and WCL, and is a TPC member for the IEEE conferences, including GLOBECOM, ICC, ICCS, WCSP, and 5G-WF.

![](images/66fc292fecf377991e788dfeda53edffe4641b3e2c65110e091112d9021b2712.jpg)

<details>
<summary>natural_image</summary>

Portrait photo of a man in a dark shirt (no text or symbols visible)
</details>

Yong Zeng (S’12–M’14) received the B.E. (Hons.) and Ph.D. degrees from the Nanyang Technological University, Singapore, in 2009 and 2014, respectively. Since 2013, he has been with the National University of Singapore, as a Research Fellow and then a Senior Research Fellow. His research interests include UAV communications, wireless power transfer, massive MIMO and millimeter wave communications, and multi-user MIMO interfering communications. He has published over 60 IEEE journal and conference papers, including one invited paper in the IEEE TRANSACTIONS ON COMMUNICATIONS, 6 ESI highly cited papers, and 3 ESI hot papers. He was a recipient of the 2017 IEEE Communications Society Heinrich Hertz Award, the 2017 IEEE TRANSACTIONS ON WIRELESS COMMUNICATIONS Exemplary Reviewer, the 2015 and 2017 IEEE WIRELESS COMMUNICATIONS LETTERS Exemplary Reviewer, and the Best Paper Award for the 10th IEEE International Conference on Information, Communications and Signal Processing. He is the Workshop Co-Chair for two workshops in ICC 2018 and the 23rd Asia-Pacific Conference on Communications (APCC). He is currently serving as an Associate Editor for the IEEE ACCESS, a Leading Guest Editor for the IEEE WIRELESS COMMUNICATIONS on Integrating UAVs into 5G and Beyond and China Communications on Network-Connected UAV Communications.

![](images/41a12b3d33e259f4240368f6df647834dec0a1b68e972b0d00b0a4d971f3665e.jpg)

<details>
<summary>natural_image</summary>

Portrait of a man wearing glasses and a suit (no visible text or symbols)
</details>

Rui Zhang (S’00–M’07–SM’15–F’17) received the B.Eng. (Hons.) and M.Eng. degrees in electrical engineering from the National University of Singapore, Singapore, and the Ph.D. degree in electrical engineering from Stanford University, Stanford, CA, USA. From 2007 to 2010, he was a Research Scientist with the Institute for Infocomm Research, ASTAR, Singapore. Since 2010, he has been with the Department of Electrical and Computer Engineering, National University of Singapore, where he is currently a Dean’s Chair Associate Professor with the Faculty of Engineering. He has authored over 300 papers. He has been listed as a Highly Cited Researcher (also known as the World’s Most Influential Scientific Minds), by Thomson Reuters since 2015. His research interests include wireless information and power transfer, drone communications, wireless information surveillance, energy-efficient and energy-harvesting-enabled wireless communications, multiuser MIMO, cognitive radio, and optimization methods. He was an elected member of the IEEE Signal Processing Society SPCOM from 2012 to 2017 and SAM Technical Committees from 2013 to 2015. He was a recipient of the 6th IEEE Communications Society Asia-Pacific Region Best Young Researcher Award in 2011 and the Young Researcher Award of the National University of Singapore in 2015. He was a co-recipient of the IEEE Marconi Prize Paper Award in Wireless Communications in 2015, the IEEE Communications Society Asia-Pacific Region Best Paper Award in 2016, the IEEE Signal Processing Society Best Paper Award in 2016, the IEEE Communications Society Heinrich Hertz Prize Paper Award in 2017, the IEEE Signal Processing Society Donald G. Fink Overview Paper Award in 2017, and the IEEE Technical Committee on Green Communications and Computing (TCGCC) Best Journal Paper Award in 2017. He was a co-author of the paper that received the IEEE Signal Processing Society Young Author Best Paper Award in 2017. He served as the Vice Chair for the IEEE Communications Society Asia-Pacific Board Technical Affairs Committee from 2014 to 2015. He served as TPC co-chair or as an organizing committee member for over 30 international conferences, and as a guest editor for 10 special issues in IEEE and other internationally refereed journals. He served as an Editor for the IEEE TRANSACTIONS ON WIRELESS COMMUNICATIONS from 2012 to 2016 and the IEEE JOURNAL ON SELECTED AREAS IN COMMUNICATIONS Green Communications and Networking Series from 2015 to 2016. He is currently an Editor for the IEEE TRANSACTIONS ON COMMUNICATIONS, the IEEE TRANSACTIONS ON SIGNAL PROCESSING, and the IEEE TRANSACTIONS ON GREEN COMMUNICATIONS AND NETWORKING.