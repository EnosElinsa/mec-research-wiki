# Energy-Efficient Design of Satellite-Terrestrial Computing in 6G Wireless Networks

Qi Wang , Student Member, IEEE, Xiaoming Chen , Senior Member, IEEE, and Qiao Qi , Member, IEEE

Abstract— In this paper, we investigate the issue of satellite-terrestrial computing in the sixth generation (6G) wireless networks, where multiple terrestrial base stations (BSs) and low earth orbit (LEO) satellites collaboratively provide edge computing services to ground user equipments (GUEs) and space user equipments (SUEs) over the world. In particular, we design a complete process of satellite-terrestrial computing in terms of communication and computing according to the characteristics of 6G wireless networks. In order to minimize the weighted total energy consumption while ensuring delay requirements of computing tasks, an energy-efficient satellite-terrestrial computing algorithm is put forward by jointly optimizing offloading selection, beamforming design and resource allocation. Finally, both theoretical analysis and simulation results confirm fast convergence and superior performance of the proposed algorithm for satellite-terrestrial computing in 6G wireless networks.

Index Terms— 6G, satellite-terrestrial computing, computing offloading, resource allocation, beamforming design.

# I. INTRODUCTION

WITH the fast development of information technologyin recent years, many new intelligent applications and in recent years, many new intelligent applications and services have emerged, such as extended reality, holographic communication, and autonomous driving which require mass data processing. However, due to limited computing power, it is impossible to complete mass data processing at the terminals in real time. In this context, mobile edge computing (MEC) has become a key enabling technology for the fifth generation (5G) wireless networks by deploying computing servers at the network edge, e.g., base station (BS), to provide low-latency computing services [1]. However, 5G wireless networks only cover a small proportion of the world. According to statistics, more than half of the global region, especially in oceans, deserts and remote mountainous areas, still suffers from the lack of Internet access [2]. Thus, it is desired to design the sixth generation (6G) wireless networks with ubiquitous communication and real-time computing capabilities.

Manuscript received 11 April 2023; revised 7 September 2023 and 14 November 2023; accepted 15 November 2023. Date of publication 20 November 2023; date of current version 19 March 2024. The work was supported by the Natural Science Foundation of China under Grant U21A20443 and 62231009, and the Zhejiang Provincial Natural Science Foundation of China under Grant LR20F010002. The associate editor coordinating the review of this article and approving it for publication was J. Lee. (Corresponding author: Xiaoming Chen.)

The authors are with the College of Information Science and Electronic Engineering, Zhejiang University, Hangzhou 310027, China (e-mail: wang-qi@zju.edu.cn; chen xiaoming@zju.edu.cn; qiqiao1996@zju.edu.cn).

Color versions of one or more figures in this article are available at https://doi.org/10.1109/TCOMM.2023.3334813.

Digital Object Identifier 10.1109/TCOMM.2023.3334813

On the one hand, for the special areas that the terrestrial communication cannot cover, satellite communication can be adopted as a supplement for providing access services. Compared to terrestrial communication, satellite communication has a large coverage area and a more flexible deployment due to the geographical advantages, which has been widely regarded as one of typical application scenarios of 6G wireless network [3], [4], [5]. In particular, low earth orbit (LEO) satellites with lower orbital altitude can provide high-efficiency communications because of the low transmission delay and propagation pathloss [6], [7]. As is well-known to all, SpaceX is executing the “Starlink” program, which aims to launch 12,000 LEO satellites by 2024 for providing global satellite access [8]. On the other hand, due to limited computing resources, MEC servers at the terrestrial BSs are often overloaded in computing-intensive areas. In this context, LEO satellites equipped with MEC servers can be regarded as space network nodes to offer additional computing power. Driven by these issues, it makes sense to explore satellite-terrestrial computing in 6G wireless networks to meet the requirements of high-reliable communication and low-latency computing for various intelligent applications around the world [9].

Generally speaking, satellite-terrestrial computing makes use of global-covered integrated satellite-terrestrial network to provide edge computing [10]. For satellite-terrestrial computing, communication and computing are two key issues affecting the edge computing. The former decides the quality of data transmission, and the latter determines the performance of data processing. To improve the quality of data transmission for computing tasks, the communication in integrated satellite-terrestrial networks has been extensively studied. For instance, the authors investigated the channel characteristics of the integrated satellite-terrestrial system and designed a strategy to maximize the utilization of communication resources [11]. In [12], the transmission performance of a cognitive satellite-terrestrial system was analyzed when the satellite link and the terrestrial link shared the same spectrum. In order to avoid inter-user interference, orthogonal resources are usually allocated to the terminals in satellite-terrestrial systems, resulting in a low spectrum utility [13], [14]. To cope with this issue, non-orthogonal multiple access (NOMA)- based satellite-terrestrial systems are proposed to improve the spectral efficiency. In [15] and [16], the authors studied the beamforming design and power allocation to reduce the co-channel interference in NOMA-based satellite-terrestrial systems. Moreover, some novel communication techniques, such as rate splitting multiple access [17], reconfigurable intelligent surface-assisted [18], and millimeter wave communication [19], have been extensively studied in research related to satellite-terrestrial networks.

For computing, it is desired to select an appropriate computing node, namely computing offloading, according to the characteristics of satellite-terrestrial computing. Previously, computing offloading in terrestrial networks has been well investigated [20]. For example, a joint offloading decision and resource allocation scheme was provided in [21] to minimize the total energy cost in the mobile cloud networks. Moreover, the authors in [22] studied an energy-aware task offloading problem for user-intensive terrestrial systems. However, computing offloading for integrated satellite-terrestrial networks is still an open issue. This is due to the more complex transmission environment for the integrated satellite-terrestrial network, which requires a comprehensive architecture to coordinate wireless and computing resources across multiple terminals and nodes. To this end, a series of works have focused on resource allocation in satellite-terrestrial networks. For example, a novel double edge computing framework of satellite-terrestrial networks was proposed in [23] to minimize the offloading delay and the required energy by resource allocation. The authors in [24] jointly optimized task execution sequence and computing resource allocation for the satellite-terrestrial double edge computing system. In [25], the authors put forward a joint offloading strategy and resource scheduling design to improve the overall performance for integrated satellite-terrestrial networks with hybrid cloud and edge computing.

Recently, there has been a growing emergence of satellites and space applications, including full-coverage communications, climate monitoring, navigation and positioning, earth observation and aeronautical exploration, which also require some certain computing power. Therefore, LEO satellites are expected to serve as space computing nodes to provide communication and computing services for space terminals. Nevertheless, existing works lack consideration of inter-satellite communication and space resource sharing, as well as the deep collaboration of multiple types of computing nodes in integrated satellite-terrestrial networks. In this context, this paper aims to design a general framework for satellite-terrestrial computing in 6G wireless networks, providing high-reliable communication and low-latency computing services for ground user equipments (GUEs) and space user equipments (SUEs) simultaneously. The contributions of this paper are as follows.

1) We present a general satellite-terrestrial computing framework for providing global seamless computing power supply. In particular, multiple types of computing nodes cooperatively provide low-latency computing power support to both GUEs and SUEs simultaneously. The framework meets the increasing demand for space applications and supplements terrestrial computing power.   
2) Within satellite-terrestrial computing system, we evaluate the performance in terms of the energy consumption and execution time, which yields valuable insights for

![](images/4a175c8a1c5ac76c1b26713202e6e74adc4ed2a13058c2e9f814fe3b018d528d.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["SUEs"] -->|Wireless| B["LEO Satellites"]
    B --> C["Satellite MEC Server"]
    C --> D["BS"]
    C --> E["BS"]
    C --> F["GPS"]
    D --> G["BSI"]
    E --> H["GUEs"]
    F --> I["GPS"]
    style A fill:#f9f,stroke:#333
    style B fill:#ccf,stroke:#333
    style C fill:#cfc,stroke:#333
    style D fill:#fcc,stroke:#333
    style E fill:#cff,stroke:#333
    style F fill:#ffc,stroke:#333
```
</details>

Fig. 1. System model for satellite-terrestrial computing in 6G wireless networks.

optimal design. To minimize the weighted total energy consumption while ensuring delay requirements, we formulate a key problem for satellite-terrestrial computing by jointly optimizing offloading selection, beamforming design and resource allocation.

3) To solve the formulated complex optimization problem, we decompose the original NP-hard problem into three subproblems. For the offloading selection subproblem, we adopt the relaxation mapping method to strike a balance between optimization results and computational complexity. For the beamforming design and resource allocation subproblems, a combination of closed-form solutions and convex approximation techniques is employed for effective solution. The effectiveness and superiority of the proposed algorithm are validated through theoretical analysis and simulation results.

The rest of this paper is organized as follows: Section II introduces the satellite-terrestrial computing model. Section III designs a satellite-terrestrial computing algorithm to minimize the weighted total energy consumption. Section IV presents simulation results to verify the effectiveness of the proposed algorithm. Finally, Section V concludes the paper.

Notations: Bold lower case and upper case letters denote column vectors and matrices, respectively. $( \cdot ) ^ { H }$ , Rank(·) and tr(·) indicate the conjugate transpose, the rank and the trace of a matrix, respectively. | · | means the absolute value of a scalar, ∥ · ∥ means the 2-norm of a vector, $\mathbf { X } \succeq \mathbf { 0 }$ means that matrix X is a positive semi-definite matrix, $\mathbb { C } ^ { a \times b }$ denotes the set of $a \times b$ dimensional complex matrixes, and ⊙ denotes Hadamard product.

# II. SYSTEM MODEL

Let us consider an integrated satellite-terrestrial 6G wireless network consisting of M BSs each equipped with $N _ { t } ^ { g }$ antennas, N LEO satellites each equipped with $N _ { t } ^ { s }$ antennas, K single-antenna GUEs and L single-antenna ${ \mathrm { S U E s } } , { ^ 1 }$ as shown in Fig. 1. Specifically, BSs with MEC servers provide real-time

1Note that common types of SUEs include remote sensing satellites, spacecraft, space telescopes, space stations, planetary rovers and landers, and large-scale scientific experiment instruments. In Particular, unmanned aerial vehicles (UAVs) and high-altitude platforms (HAPs) can be regarded as special cases of SUEs that operate in super-near-ground environments.

computing services to GUEs, and LEO satellites with MEC servers supply the computing power for GUEs and SUEs.2 Each GUE and SUE has an indivisible computing task that needs to be offloaded to a MEC server for processing due to its own limited computing capability and stored energy. Note that the GUE is allowed to select at most one BS or LEO satellite for computing offloading, while the SUE adopts the concept of satellite clustering to select one LEO satellite from a group of N available options, i.e., $\sum _ { m = 1 } ^ { M } \alpha _ { k , m } + \sum _ { n = 1 } ^ { N } \beta _ { k , n } = 1 , \forall k \ \in$ K and $\sum _ { n = 1 } ^ { N } \gamma _ { l , n } = 1 , \forall l \in L$ , where binary variables $\alpha _ { k , m } , \beta _ { k , n } , \gamma _ { l , n } ~ \in ~ \{ 0 , 1 \}$ indicate offloading selection for computing tasks. Particularly, if the task of the k-th GUE is offloaded to the m-th BS then $\alpha _ { k , m } = 1$ , if the task of the k-th GUE is offloaded to the n-th LEO satellite then $\beta _ { k , n } = 1$ , if the task of the l-th SUE is offloaded to the n-th LEO satellite then $\gamma _ { l , n } = 1$ , and otherwise the variable coefficient is equal to 0. In general, the whole computing offloading process consists of three stages. At first, GUEs and SUEs transmit the raw data of computing tasks to the BS or LEO satellite via uplink channels. Then, the BSs and LEO satellites decode the data of computing tasks, and perform the data computing at their own MEC servers. Finally, computing results are returned back to the corresponding GUEs and SUEs through downlink channels. Since the data size of computing results is much smaller than that of computing tasks, it is usual to ignore the transmission delay and energy consumption caused by the stage of returning the computing results [26]. In the following, we describe the process of satellite-terrestrial computing in 6G wireless networks from the perspectives of communication and computing, respectively.

# A. Communication Model

During the stage of data transmission, there involves three different channels,3 i.e., inter-terrestrial channel, satelliteterrestrial channel and inter-satellite channel. Thus, we will discuss the communication models based on these three channels in turn.

1) Terrestrial-to-Terrestrial Communication: For the interterrestrial channel between the GUE and the BS, we consider both small-scale and large-scale fading. Specifically, the smallscale fading is assumed to obey Rayleigh model [28], and the large-scale fading is modeled as a practical distance-dependent path loss attenuation, i.e., $\mathrm { P L } _ { \mathrm { d B } } = 1 2 8 . 1 + 3 7 . 6 \log _ { 1 0 } \tau$ [29], where τ (km) is the distance between the transmitter and receiver. To improve the spectrum utility, GUEs transmit data signals for computing offloading to the BSs in the NOMA manner. Then, successive interference cancellation (SIC) and receive beamforming technologies are adopted at the BS to suppress co-channel interference. In particular, we define

2Here, we consider the new-generation LEO satellites with strong payload processing capabilities, which provide sufficient computing power resources for traditional GUEs and SUEs by deploying MEC servers to efficiently handle and analyze received data and conduct complex computing tasks.

3In this paper, we assume that the channel state information (CSI) of these three channels are completely available and unchanged during a time slot, but independently fade over time slots [27].

$\mathbf { h } _ { k , m } \in \mathbb { C } ^ { N _ { t } ^ { g } \times 1 }$ is the channel vector from the k-th GUE to the m-th BS, and $\pi ^ { m } \left( k \right)$ as the SIC order number of the k-th GUE at the m-th BS. If for any k′-th GUE and $k ^ { \prime \prime } { \mathrm { - t h } }$ GUE with $\left\| \mathbf h _ { k ^ { \prime } , m } \right\| ^ { 2 } > \left\| \mathbf h _ { k ^ { \prime \prime } , m } \right\| ^ { 2 }$ , then there is $\pi ^ { m } \left( k ^ { \prime } \right) < \pi ^ { m } \left( k ^ { \prime \prime } \right)$ , which represents that the signal of the k′-th GUE at the m-th BS is decoded and eliminated from the received signal before the $k ^ { \prime \prime } .$ -th GUE [30]. Based on the principle of SIC that the GUE signal with a high channel quality is decoded first, the data transmission rate from the k-th GUE to the m-th BS is given by

$$
R _ {k, m} ^ {g - g} = B _ {1} \log_ {2} \left(1 + \frac {\left| \mathbf {w} _ {k , m} ^ {H} \mathbf {h} _ {k , m} \right| ^ {2} p _ {k}}{\sum_ {\pi^ {m} (i) > \pi^ {m} (k)} \left| \mathbf {w} _ {k , m} ^ {H} \mathbf {h} _ {i , m} \right| ^ {2} p _ {i} + \delta_ {1} ^ {2}}\right), \tag {1}
$$

where $\mathbf { w } _ { k , m } \in \mathbb { C } ^ { N _ { t } ^ { g } \times 1 }$ denotes a receive beamforming vector at the m-th BS with $\mathbf { w } _ { k , m } ^ { H } \mathbf { w } _ { k , m } = 1 , p _ { k }$ is the transmit power of the k-th GUE, $B _ { 1 }$ and $\delta _ { 1 } ^ { 2 }$ represent the bandwidth and the variance of additive white Gaussian noise (AWGN) for the inter-terrestrial channel, respectively.

2) Terrestrial-to-Satellite Communication: According to the propagation characteristics of LEO satellite communication, the satellite-terrestrial channel between the k-th GUE and the n-th LEO satellite can be modeled as [31] and [32]

$$
\mathbf {g} _ {k, n} = \sqrt {C _ {k , n}} \mathbf {b} _ {k, n} ^ {\frac {1}{2}} \odot \mathbf {r} _ {k, n} \cdot \exp \left\{j 2 \pi v _ {k, n} ^ {\mathrm{sat}} \right\}, \tag {2}
$$

where $C _ { k , n } , \mathbf { r } _ { k , n } , \mathbf { b } _ { k , n }$ and $v _ { k , n } ^ { \mathrm { s a t } }$ denote the large-scale fading coefficient, the rain attenuation effect, the satellite antenna gain and Doppler shift caused by the motion of the n-th LEO satellite relative to the k-th GUE, respectively. In particular, $C _ { k , n }$ is defined as

$$
C _ {k, n} = \left(\frac {\mu}{4 \pi f \varphi_ {k , n}}\right) ^ {2} \frac {G _ {k , n}}{\kappa B _ {2} T}, \tag {3}
$$

where $\mu$ is the speed of light, f is the carrier frequency, $B _ { 2 }$ is bandwidth of the satellite-terrestrial channel, κ is Boltzmann constant, $T$ is the noise temperature, $\varphi _ { k , n }$ and $G _ { k , n }$ are the distance and transmit antenna gain from the k-th GUE to the n-th LEO satellite, respectively. In addition, the satellite-terrestrial channel is affected by various atmospheric attenuations in the troposphere, with rain attenuation having a dominant impact on channel quality. The rain attenuation vector can be expressed as [33]

$$
\mathbf {r} _ {k, n} = \xi^ {\frac {1}{2}} e ^ {- j \boldsymbol {\theta} _ {k, n}}, \tag {4}
$$

where $\xi ^ { \frac { 1 } { 2 } }$ denotes the power gain of the rain attenuation in dB, following log-normal distribution, i.e., ln $\left( \xi ^ { 1 / 2 } \right) \ \sim$ $\mathscr { C N } \left( \mu _ { r } , \sigma _ { r } ^ { 2 } \right)$ , and $\boldsymbol { \theta } _ { k , n }$ is a phase vector whose components obey a uniform distributed between 0 and $2 \pi$ . Moreover, the elements of the $N _ { t } ^ { s } .$ -dimensional satellite receive antenna gain $\mathbf { b } _ { k , n }$ are approximated by [34]

$$
\mathbf {b} _ {k, n} (i) = b _ {n, \max} \left(\frac {J _ {1} \left(u _ {i}\right)}{2 u _ {i}} + 3 6 \frac {J _ {3} \left(u _ {i}\right)}{u _ {i} ^ {3}}\right) ^ {3}, \tag {5}
$$

where $u _ { i } ~ = ~ 2 . 0 7 1 2 3 \left( \sin { \left( \varepsilon _ { i , k , n } \right) } \middle / \sin { \left( \varepsilon _ { n } ^ { 3 d B } \right) } \right)$ with $\varepsilon _ { i , k , n }$ being the angle between the i-th antenna of the n-th LEO satellite and the k-th GUE, and tfor the n-th LEO satellite, tantis $\varepsilon _ { n } ^ { 3 d B }$ being 3-dB anglemaximum antenna $b _ { n , \mathrm { m a x } }$ gain of the n-th LEO satellite, $J _ { 1 }$ and $J _ { 3 }$ are the first-kind Bessel functions of the first and third order, respectively. Similarly, GUEs transmit signals for computing tasks to the LEO satellites by NOMA over the uplink satellite-terrestrial channel. Then, LEO satellites perform Doppler compensation on the received signals and apply receive beamforming to decode the data from GUEs by $\mathrm { S I C . ^ { 4 } }$ Similarly, we define $\pi ^ { n } \left( k \right)$ as the SIC order number of the k-th GUE at the $n \mathrm { - }$ th LEO satellite. If for any $k ^ { \prime } \mathrm { - t h }$ GUE and $k ^ { \prime \prime } .$ -th GUE with $\left\| \mathbf { g } _ { k ^ { \prime } , n } \right\| ^ { 2 } > \left\| \mathbf { g } _ { k ^ { \prime \prime } , n } \right\| ^ { 2 }$ , then there is $\pi ^ { n } \left( k ^ { \prime } \right) < \pi ^ { n } \left( k ^ { \prime \prime } \right)$ , which represents that the signal of the k′-th GUE at the n-th LEO satellite is decoded and eliminated from the received signal before the k′′-th GUE. In this context, the data transmission rate from the k-th GUE to the n-th LEO satellite is given by

$$
R _ {k, n} ^ {g - s} = B _ {2} \log_ {2} \left(1 + \frac {\left| \mathbf {v} _ {k , n} ^ {H} \mathbf {g} _ {k , n} \right| ^ {2} p _ {k}}{\sum_ {\pi^ {n} (i) > \pi^ {n} (k)} \left| \mathbf {v} _ {k , n} ^ {H} \mathbf {g} _ {i , n} \right| ^ {2} p _ {i} + \delta_ {2} ^ {2}}\right), \tag {6}
$$

where $\mathbf { v } _ { k , n } ~ \in ~ \mathbb { C } ^ { N _ { t } ^ { s } \times 1 }$ denotes receive beamforming at the n-th LEO satellite for the k-th GUE with $\mathbf { v } _ { k , n } ^ { H } \mathbf { v } _ { k , n } = 1$ , and $\delta _ { 2 } ^ { 2 }$ denotes the variance of AWGN for the satellite-terrestrial channel.

3) Satellite-to-Satellite Communication: For the intersatellite channel between the SUE and the LEO satellite, free space optical (FSO) communication is used to reduce inter-user interference and improve communication security for achieving the long-range and high-speed data transmission. According to the characteristics of FSO communication described in [36] and [37], the data transmission rate from the l-th SUE to the n-th LEO satellite can be expressed as

$$
R _ {l, n} ^ {s - s} = B _ {3} \mathrm{log} _ {2} \left(1 + \frac {q _ {l} \eta_ {l} ^ {t} \eta_ {n} ^ {r} \left(\frac {\lambda}{4 \pi \phi_ {l , n}}\right) ^ {2} G _ {l} ^ {t} G _ {n} ^ {r} L _ {l} ^ {t} L _ {n} ^ {r}}{\delta_ {3} ^ {2}}\right), (7)
$$

where $q _ { l }$ is the transmit power of the l-th SUE, λ is the wavelength, $\phi _ { l , n }$ is the distance between the l-th SUE and the n-th LEO satellite, $B _ { 3 }$ and $\delta _ { 3 } ^ { 2 }$ represent the bandwidth and the variance of AWGN for the inter-satellite channel, respectively. $G _ { l } ^ { t } = ( \pi D _ { l } ^ { t } / \lambda ) ^ { 2 } , L _ { l } ^ { t } = \exp ( - G _ { l } ^ { t } ( e _ { l } ^ { t } ) ^ { 2 } ) , D _ { l } ^ { t } , e _ { l } ^ { t }$ and $\eta _ { l } ^ { t }$ are the aperture gain, the pointing loss factor, the aperture diameter, the pointing error angle and the optical efficiency of transmitter at the l-th SUE, respectively. Similarly, $G _ { n } ^ { r } ~ = ~ ( \pi D _ { n } ^ { r } / \lambda ) ^ { 2 }$ , $L _ { n } ^ { r } \ = \ \exp ( - G _ { n } ^ { r } ( e _ { n } ^ { r } ) ^ { 2 } ) , \ D _ { n } ^ { r } , \ e _ { n } ^ { r }$ and $\eta _ { n } ^ { r }$ are corresponding parameters of receiver at the n-th LEO satellite.

4In satellite-terrestrial networks, the high speed mobility of satellites relative to the ground can cause Doppler shift effects, which have a serious impact on communication performance. Doppler compensation is therefore required at the satellite receivers to improve signal transmission efficiency and accuracy [35].

# B. Computing Model

In general, execution time and energy consumption are two key performance metrics for completing computing tasks. Thus, we characterize the computing model from these two aspects. For easy notation, the computing task of the k-th GUE is defined as $\Omega _ { k } ^ { g } \triangleq ( d _ { k } , c _ { k } )$ , where $d _ { k }$ denotes the input data size in bits and $c _ { k }$ denotes task complexity in cycles/bit which means the number of CPU cycles required to compute per bit of input data. Similarly, the computing task of the l-th SUE is defined as $\Omega _ { l } ^ { s } \triangleq \mathsf { \bar { \Gamma } } ( d _ { l } ^ { s p a c e } , c _ { l } ^ { s p \hat { a } c e } )$ , where $d _ { l } ^ { s p a c e }$ and cspacel $c _ { l } ^ { s p a c e }$ are the input data size and task complexity of the SUE task, respectively. In what follows, we analyze the performance of execution time and energy consumption for completing computing tasks from three different computing models, respectively.

1) Terrestrial-to-Terrestrial Computing: According to the inter-terrestrial communication model in (1), the uplink transmission delay for computing task $\Omega _ { k } ^ { g }$ from the k-th GUE to the BS can be computed as

$$
T _ {k} ^ {g - g, t r a} = \sum_ {m = 1} ^ {M} \alpha_ {k, m} \frac {d _ {k}}{R _ {k , m} ^ {g - g}}. \tag {8}
$$

Then, the decoded computing task $\Omega _ { k } ^ { g }$ is sent to the MEC server by the BS for data computing. The computing delay at the MEC server is given by

$$
T _ {k} ^ {g - g, c o m} = \sum_ {m = 1} ^ {M} \alpha_ {k, m} \frac {d _ {k} c _ {k}}{f _ {k , m} ^ {g r o}}, \tag {9}
$$

where $f _ { k , m } ^ { g r o } \ge 0$ denotes the computing resources allocated to the k-th GUE by the MEC server of the m-th BS. Therefore, the total execution time for completing the computing task of the k-th GUE can be expressed as

$$
T _ {k} ^ {g - g} = T _ {k} ^ {g - g, t r a} + T _ {k} ^ {g - g, c o m}. \tag {10}
$$

Moreover, the transmission energy consumption from the k-th GUE to the BS is given by

$$
E _ {k} ^ {g - g, t r a} = \sum_ {m = 1} ^ {M} \alpha_ {k, m} p _ {k} \frac {d _ {k}}{R _ {k , m} ^ {g - g}}. \tag {11}
$$

The computing energy consumption for processing the task can be modeled as [38]

$$
E _ {k} ^ {g - g, c o m} = \sum_ {m = 1} ^ {M} \alpha_ {k, m} \tau_ {m} ^ {g r o} d _ {k} c _ {k} \left(f _ {k, m} ^ {g r o}\right) ^ {2}, \tag {12}
$$

where $\tau _ { m } ^ { g r o }$ is the energy coefficient of the MEC server at the m-th BS, which is related to the chip architecture [39]. Hence, the total energy consumption for computing offloading from the k-th GUE to the BS can be expressed as

$$
E _ {k} ^ {g - g} = E _ {k} ^ {g - g, t r a} + E _ {k} ^ {g - g, c o m}. \tag {13}
$$

2) Terrestrial-to-Satellite Computing: Compared with terrestrial-to-terrestrial computing, terrestrial-to-satellite computing with very long transmission distance needs to consider the propagation delay [40]. Thus, the total execution time consists of three components, i.e., transmission delay

T g−s,tra, $\begin{array} { l } { T _ { k } ^ { g - s , t r a } , } \\ { T _ { k } ^ { g - s , c o m } } \end{array}$ propagation delay T g−s,pro $T _ { k } ^ { g - s , p r o }$ and computing delay , which can be expressed as

$$
\begin{array}{l} T _ {k} ^ {g - s} = T _ {k} ^ {g - s, t r a} + T _ {k} ^ {g - s, p r o} + T _ {k} ^ {g - s, c o m} \\ = \sum_ {n = 1} ^ {N} \beta_ {k, n} \frac {d _ {k}}{R _ {k , n} ^ {g - s}} + \sum_ {n = 1} ^ {N} \beta_ {k, n} \frac {\varphi_ {k , n}}{\mu} \\ + \sum_ {n = 1} ^ {N} \beta_ {k, n} \frac {d _ {k} c _ {k}}{f _ {k , n} ^ {s a t - g}}, \tag {14} \\ \end{array}
$$

where f satk,n $f _ { k , n } ^ { s a t - g } \geq 0$ denotes the computing resources allocated to the k-th GUE by the MEC server of the n-th LEO satellite. Likewise, the total energy consumption for computing offloading from the k-th GUE to the LEO satellite can be expressed as

$$
\begin{array}{l} E _ {k} ^ {g - s} = E _ {k} ^ {g - s, t r a} + E _ {k} ^ {g - s, c o m} \\ = \sum_ {n = 1} ^ {N} \beta_ {k, n} p _ {k} \frac {d _ {k}}{R _ {k , n} ^ {g - s}} \\ + \sum_ {n = 1} ^ {N} \beta_ {k, n} \tau_ {n} ^ {\text { sat }} d _ {k} c _ {k} \left(f _ {k, n} ^ {\text { sat } - g}\right) ^ {2}, \tag {15} \\ \end{array}
$$

where the n- $\tau _ { m } ^ { s a t }$ is the energy coefficient of the MEC server atEO satellite, which is determined by the chip architecture.

3) Satellite-to-Satellite Computing: Similar to terrestrial-tosatellite computing, the total execution time for completing the computing tasks of SUEs also includes transmission delay, propagation delay and computing delay, namely

$$
\begin{array}{l} T _ {l} ^ {s - s} = T _ {l} ^ {s - s, t r a} + T _ {l} ^ {s - s, p r o} + T _ {l} ^ {s - s, c o m} \\ = \sum_ {n = 1} ^ {N} \gamma_ {l, n} \frac {d _ {l} ^ {\text { space }}}{R _ {l , n} ^ {s - s}} + \sum_ {n = 1} ^ {N} \gamma_ {l, n} \frac {\phi_ {l , n}}{\mu} \\ + \sum_ {n = 1} ^ {N} \gamma_ {l, n} \frac {d _ {l} ^ {\text { space }} c _ {l} ^ {\text { space }}}{f _ {l , n} ^ {\text { sat } - s}}, \tag {16} \\ \end{array}
$$

where $f _ { l , n } ^ { s a t - s } \geq 0$ denotes the computing resources allocated to the l-th SUE by the MEC server of the n-th LEO satellite. Correspondingly, the total energy consumption for computing offloading from the l-th SUE to the LEO satellite is given by

$$
\begin{array}{l} E _ {l} ^ {s - s} = E _ {l} ^ {s - s, t r a} + E _ {l} ^ {s - s, c o m} \\ = \sum_ {n = 1} ^ {N} \gamma_ {l, n} q _ {l} \frac {d _ {l} ^ {\text { space }}}{R _ {l , n} ^ {s - s}} \\ + \sum_ {n = 1} ^ {N} \gamma_ {l, n} \tau_ {n} ^ {s a t} d _ {l} ^ {s p a c e} c _ {l} ^ {s p a c e} \left(f _ {l, n} ^ {s a t - s}\right) ^ {2}. \tag {17} \\ \end{array}
$$

It is observed that the offloading selection $\{ \alpha _ { k , m } ,$ $\beta _ { k , n } , \gamma _ { l , n } \}$ , beamforming design $\left\{ \mathbf { w } _ { k , m } , \mathbf { v } _ { k , n } \right\}$ , and resource allocation {pk, ql, k,m k,n $\{ p _ { k } , q _ { l } , f _ { k , m } ^ { g r o } , \bar { f } _ { k , n } ^ { s a t - \bar { g } } , \bar { f } _ { l , n } ^ { s a t - s } \}$ f gro , f sat−g, f sat−s} all have important l,n effects on the execution time and energy consumption for completing the computing tasks. Therefore, it makes sense to develop a joint design to reduce the time and energy costs for satellite-terrestrial computing in 6G wireless networks.

# III. JOINT DESIGN FOR SATELLITE-TERRESTRIAL COMPUTING

In this section, we provide an energy-efficient design for satellite-terrestrial computing by jointly optimizing offloading selection, beamforming design and resource allocation.

# A. Problem Formulation

Considering that user experience is mainly determined by the energy consumption and the execution time of completing tasks, we aim to minimize the weighted total energy consumption while ensuring delay requirements of computing tasks. In this context, the joint design can be mathematically formulated as the following optimization problem:

$$
\min _ {\boldsymbol {\alpha}, \boldsymbol {\beta}, \boldsymbol {\gamma}, \boldsymbol {w}, \boldsymbol {v}, \mathbf {p}, \mathbf {q}, \mathbf {f}} \sum_ {k = 1} ^ {K} \rho_ {k} ^ {g} \left(E _ {k} ^ {g - g} + E _ {k} ^ {g - s}\right) + \sum_ {l = 1} ^ {L} \rho_ {l} ^ {s} E _ {l} ^ {s - s} \tag {18a}
$$

$\mathrm { s . t . } T _ { k } ^ { g - g } + T _ { k } ^ { g - s } \leq Z _ { k } ^ { g } ,$ (18b)

$$
T _ {l} ^ {s - s} \leq Z _ {l} ^ {s}, \tag {18c}
$$

$$
\sum_ {k = 1} ^ {K} \alpha_ {k, m} f _ {k, m} ^ {g r o} \leq F _ {m} ^ {g r o}, \tag {18d}
$$

$$
\sum_ {k = 1} ^ {K} \beta_ {k, n} f _ {k, n} ^ {s a t - g} + \sum_ {l = 1} ^ {L} \gamma_ {l, n} f _ {l, n} ^ {s a t - s} \leq F _ {n} ^ {s a t}, \tag {18e}
$$

$$
\alpha_ {k, m}, \beta_ {k, n}, \gamma_ {l, n} \in \{0, 1 \}, \tag {18f}
$$

$$
\sum_ {m = 1} ^ {M} \alpha_ {k, m} + \sum_ {n = 1} ^ {N} \beta_ {k, n} = 1, \tag {18g}
$$

$$
\sum_ {n = 1} ^ {N} \gamma_ {l, n} = 1, \tag {18h}
$$

$$
0 \leq p _ {k} \leq P _ {k} ^ {\max}, \tag {18i}
$$

$$
0 \leq q _ {l} \leq Q _ {l} ^ {\max}, \tag {18j}
$$

$$
\left\| \mathbf {w} _ {k, m} \right\| ^ {2} = \left\| \mathbf {v} _ {k, n} \right\| ^ {2} = 1, \tag {18k}
$$

where $\alpha = \{ \alpha _ { k , m } , \forall k \in K , \forall m \in M \} , \beta = \{ \beta _ { k , n } , \forall k \in$ $K , \forall n \in N \} , \gamma \ = \ \{ \gamma _ { l , n } , \forall l \in L , \forall n \in N \} , w \ = \ \{ \mathbf { w } _ { k , m } ,$ ∀k $\in \ K , \forall m \ \in \ M \} , \ v \ = \ \{ \mathbf { v } _ { k , n } , \forall k \ \in \ K , \forall n \ \in \ \mathring N \} .$ , ${ \mathbf p } = \{ p _ { k } , \forall k \in K \} , { \mathbf q } = \{ q _ { l } , \forall l \in L \}$ and $\mathbf { f } = \{ f _ { k , m } ^ { g r o } , \forall k \in$ $K , \forall m \in M \} \bigcup \{ f _ { k . n } ^ { s a t - g } , \forall k \in K , \forall n \in N \} \bigcup \{ f _ { l . n } ^ { s a t - s } , \forall l \in$ $L , \forall n \in N \}$ problem (18), the objective function (18a) is the weighted sum of energy consumption, where $\rho _ { k } ^ { g }$ and $\rho _ { l } ^ { s }$ are the energy weights of the k-th GUE and the l-th SUE, respectively. Constraints (18b) and (18c) are the execution time requirements with $Z _ { k } ^ { g }$ and $Z _ { l } ^ { s }$ being the maximum delay of the k-th GUE and the l-th SUE, respectively. Constrains (18d)-(18e) describe computing resources restrictions imposed by MEC servers at the BSs and the LEO satellites with $F _ { m } ^ { g r o }$ and $F _ { n } ^ { s a t }$ being the maximum computing power of the MEC server at the m-th BS and the n-th LEO satellite, respectively. Constrains (18f)-(18h) are the rules of offloading selection, namely the GUE is allowed to select at most one BS or LEO satellite for computing offloading, while the SUE can only select at most one LEO satellite. Constraints (18i) and (18j) mean transmit power limitations, where $P _ { k } ^ { \mathrm { m a x } }$ and $Q _ { l } ^ { \mathrm { m a x } }$ are the maximum transmit power budget of the k-th GUE and the l-th SUE, respectively. Finally, constraint (18k) denotes the normalized receive beamforming at the BSs and the LEO satellites. Note that problem (18) is a typical mixed-integer nonlinear programming (MINLP) problem, which is proved to be NP-hard and is extremely intractable to obtain its optimal solution in polynomial time [41]. To this end, we turn to develop an effective algorithm for finding a feasible sub-optimal solution to achieve a competitive performance of satellite-terrestrial computing in 6G wireless networks.

# B. Algorithm Design

It is seen that the optimization variables are coupled in the objective function and the constraints, causing problem (18) to be unmanageable. To address this challenge, we adopt the commonly used alternating optimization (AO) method [42] to decompose problem (18) into three subproblems, i.e., offloading selection subproblem, beamforming design subproblem and resource allocation subproblem. Now, we consider the first subproblem that optimizing offloading selection while fixing others, which is given by

$$
\min _ {\boldsymbol {\alpha}, \boldsymbol {\beta}, \boldsymbol {\gamma}} \sum_ {k = 1} ^ {K} \rho_ {k} ^ {g} \left(E _ {k} ^ {g - g} + E _ {k} ^ {g - s}\right) + \sum_ {l = 1} ^ {L} \rho_ {l} ^ {s} E _ {l} ^ {s - s}
$$

$\mathrm { s . t . } \quad ( 1 8 b ) - ( 1 8 h ) .$ (19)

Notice that problem (19) is a binary integer programming problem, which can be solved by using the well-known branch and bound (B&B) method [43]. Specifically, problem (19) can be considered as the root node of the B&B search tree, which is constructed and traversed by the processes of branching and bounding. In short, branching is to divide a parent problem into two subproblems by adding binary constraints on the nodes, and bounding is to check the upper and lower bounds of the subproblems during branching. In this context, we need to find the lower bound of problem (19) by solving the following relaxed optimization:

$$
\min _ {\boldsymbol {\alpha}, \boldsymbol {\beta}, \gamma} \sum_ {k = 1} ^ {K} \rho_ {k} ^ {g} \left(E _ {k} ^ {g - g} + E _ {k} ^ {g - s}\right) + \sum_ {l = 1} ^ {L} \rho_ {l} ^ {s} E _ {l} ^ {s - s} \tag {20a}
$$

$\begin{array} { r l } { \mathrm { s . t . ~ } } & { { } ( 1 8 b ) - ( 1 8 e ) , ( 1 8 g ) , ( 1 8 h ) , } \end{array}$

$$
\alpha_ {k, m}, \beta_ {k, n}, \gamma_ {l, n} \in [ 0, 1 ], \tag {20b}
$$

where binary variables $\alpha , \beta$ and γ are relaxed to be continuous with a range of 0 to 1. In this case, problem (20) is a convex optimization problem, whose optimal solution is just the lower bound of the objective value of problem (19). Thus, the optimal solution of problem (19) can be found by solving problem (20) with the B&B algorithm during the operations of branching and bounding. Although the B&B algorithm can provide superior and optimal solutions for small and medium-sized problems, it is not an effective method for handling large-scale user offloading selection cases due to its exponential search space in the worst case. Therefore, for the offloading selection subproblem, we adopt a relaxation mapping method with lower complexity. Specifically, after the 0-1 constraint $\alpha _ { k , m } , \beta _ { k , n } , \gamma _ { l , n } ~ \in ~ \{ 0 , 1 \}$ is relaxed to $\alpha _ { k , m } , \beta _ { k , n } , \gamma _ { l , n } ~ \in ~ [ 0 , 1 ]$ , the practical significance of the optimization problem (20) can be regarded as each computing task can be partitioned into multiple parts to complete the computing offloading, so that $\alpha _ { k , m }$ and $\beta _ { k , n }$ denote the offloading portion of the k-th GUE’s computing task for the m-th BS and the n-th LEO satellite, respectively, and $\gamma _ { l , n }$ denotes the offloading portion of the l-th SUE’s computing task for the n-th LEO satellite. However, the optimal solution to the standard linear optimization problem (20) is continuous and needs to be mapped to 0-1 variables. The specific mapping strategy is to compare the values of $\alpha _ { k , m } , \forall m \ \in \ M$ and $\beta _ { k , n } , \forall n \ \in \ N$ for the k-th GUE, mapping the largest of them to 1 and the others to 0, and compare the values of $\gamma _ { l , n } , \forall n ~ \in ~ N$ for the l-th SUE, mapping the largest one to 1 and the others to 0. In this way, we obtain a suboptimal solution to the offloading selection subproblem (19), and since problem (19) is a standard linear discrete programming, the suboptimal solution obtained through the aforementioned relaxation mapping method approximates the optimal solution [25].

Next, we consider the beamforming design subproblem, which is formulated as

$$
\min _ {\boldsymbol {w}, \boldsymbol {v}} \sum_ {k = 1} ^ {K} \rho_ {k} ^ {g} \left(E _ {k} ^ {g - g, t r a} + E _ {k} ^ {g - s, t r a}\right)
$$

$\mathrm { s . t . } ~ ( 1 8 b ) , ( 1 8 k ) ,$ (21)

where constraints (18c)-(18j) that do not involve beamforming vectors w and v are not considered. Note that problem (21) is nonconvex because the variables w and v exist in quadratic fractional form in the objective function and constraint To solve this issue, we introduce the auxiliary variables $A _ { k , m } ^ { g }$ and $A _ { k , n } ^ { s } ,$ and then transform the original problem (21) as

$$
\min _ {\boldsymbol {w}, \boldsymbol {v}, A _ {k, m} ^ {g}, A _ {k, n} ^ {s}} \sum_ {k = 1} ^ {K} \rho_ {k} ^ {g} \left(\sum_ {m = 1} ^ {M} \alpha_ {k, m} p _ {k} A _ {k, m} ^ {g} + \sum_ {n = 1} ^ {N} \beta_ {k, n} p _ {k} A _ {k, n} ^ {s}\right) \tag {22a}
$$

s.t. (18k),

$$
\frac {d _ {k}}{R _ {k , m} ^ {g - g}} \leq A _ {k, m} ^ {g}, \tag {22b}
$$

$$
\frac {d _ {k}}{R _ {k , n} ^ {g - s}} \leq A _ {k, n} ^ {s}, \tag {22c}
$$

$$
\sum_ {m = 1} ^ {M} \alpha_ {k, m} A _ {k, m} ^ {g} + \sum_ {n = 1} ^ {N} \beta_ {k, n} A _ {k, n} ^ {s} \leq Z _ {k} ^ {g}
$$

$$
- \sum_ {m = 1} ^ {M} \alpha_ {k, m} \frac {d _ {k} c _ {k}}{f _ {k , m} ^ {g r o}}
$$

$$
- \sum_ {n = 1} ^ {N} \beta_ {k, n} \frac {d _ {k} c _ {k}}{f _ {k , n} ^ {s a t - g}} - \sum_ {n = 1} ^ {N} \beta_ {k, n} \frac {\varphi_ {k , n}}{\mu}, \tag {22d}
$$

where constraint (18b) is substituted for constraints (22b)-(22d), but constraints (22b) and (22c) are still noncovex. To address the noncovewe bring in new auxiliary variables $\tilde { R } _ { k , m } ^ { g - g }$ f coand Γ˜g−g $\tilde { \Gamma } _ { k , m } ^ { g - g }$ t (22b),. In this context, (22b) can be replaced by

$$
\frac {d _ {k}}{\tilde {R} _ {k , m} ^ {g - g}} \leq A _ {k, m} ^ {g}, \tag {23}
$$

$$
\tilde {R} _ {k, m} ^ {g - g} \leq B _ {1} \log_ {2} \left(1 + \tilde {\Gamma} _ {k, m} ^ {g - g}\right), \tag {24}
$$

and

$$
\begin{array}{l} \sum_ {\pi^ {m} (i) > \pi^ {m} (k)} \mathrm{tr} (\mathbf {h} _ {i, m} \mathbf {h} _ {i, m} ^ {H} \mathbf {w} _ {k, m} \mathbf {w} _ {k, m} ^ {H}) p _ {i} + \delta_ {1} ^ {2} \\ \leq \frac {\operatorname{tr} (\mathbf {h} _ {k , m} \mathbf {h} _ {k , m} ^ {H} \mathbf {w} _ {k , m} \mathbf {w} _ {k , m} ^ {H}) p _ {k}}{\tilde {\Gamma} _ {k , m} ^ {g - g}}. \tag {25} \\ \end{array}
$$

Similarly, through introducing auxiliary variables $\tilde { R } _ { k , n } ^ { g - s }$ and Γ˜g−s, $\tilde { \Gamma } _ { k , n } ^ { g - s }$ k,n nonconvex constraint (22c) can be converted as

$$
\frac {d _ {k}}{\tilde {R} _ {k , n} ^ {g - s}} \leq A _ {k, n} ^ {s}, \tag {26}
$$

$$
\tilde {R} _ {k, n} ^ {g - s} \leq B _ {2} \log_ {2} \left(1 + \tilde {\Gamma} _ {k, n} ^ {g - s}\right), \tag {27}
$$

and

$$
\begin{array}{l} \sum_ {\pi^ {n} (i) > \pi^ {n} (k)} \operatorname{tr} \left(\mathbf {g} _ {i, n} \mathbf {g} _ {i, n} ^ {H} \mathbf {v} _ {k, n} \mathbf {v} _ {k, n} ^ {H}\right) p _ {i} + \delta_ {2} ^ {2} \\ \leq \frac {\operatorname{tr} (\mathbf {g} _ {k , n} \mathbf {g} _ {k , n} ^ {H} \mathbf {v} _ {k , n} \mathbf {v} _ {k , n} ^ {H}) p _ {k}}{\tilde {\Gamma} _ {k , n} ^ {g - s}}. \tag {28} \\ \end{array}
$$

However, additional nonconvex constraints (25) and (28) block the solve of the problem. To this end, we utilize the successive convex approximation (SCA) technique to handle them. In particular, the binary first-order Taylor series expansion (w#k,m, Γ˜#g−k,m is appoint $( \mathbf { w } _ { k , m } ^ { \# } , \tilde { \Gamma } _ { k , m } ^ { \# g - g } )$ g ) ght-hand, where $\bar { \mathbf { w } } _ { k , m } ^ { \# }$ of t and $\tilde { \Gamma } _ { k , m } ^ { \# g - g }$ uality (25) at are the value of ${ \mathbf w } _ { k , m }$ and $\tilde { \Gamma } _ { k , m } ^ { g - g }$ in the last iteration, respectively. Hence, constraint (25) can be rewritten as

$$
\begin{array}{l} \sum_ {\pi^ {m} (i) > \pi^ {m} (k)} \mathrm{tr} (\mathbf {h} _ {i, m} \mathbf {h} _ {i, m} ^ {H} \mathbf {w} _ {k, m} \mathbf {w} _ {k, m} ^ {H}) p _ {i} + \delta_ {1} ^ {2} \\ \leq \left(\frac {X _ {k , m} \tilde {\Gamma} _ {k , m} ^ {\# g - g} - X _ {k , m} ^ {\#} \tilde {\Gamma} _ {k , m} ^ {g - g} + X _ {k , m} ^ {\#} \tilde {\Gamma} _ {k , m} ^ {\# g - g}}{\left(\tilde {\Gamma} _ {k , m} ^ {\# g - g}\right) ^ {2}}\right) p _ {k}, \tag {29} \\ \end{array}
$$

$X _ { k , m } ~ = ~ \operatorname { t r } \left( \mathbf { h } _ { k , m } \mathbf { h } _ { k , m } ^ { H } \mathbf { w } _ { k , m } \mathbf { w } _ { k , m } ^ { H } \right)$ and raint (2 $X _ { k , m } ^ { \# } ~ =$ $\mathrm { t r } \left( \mathbf { h } _ { k , m } \mathbf { h } _ { k , m } ^ { H } \mathbf { w } _ { k , m } ^ { \# } \mathbf { w } _ { k , m } ^ { \# } \mathbf { \Phi } _ { H } \right)$

$$
\begin{array}{l} \sum_ {\pi^ {n} (i) > \pi^ {n} (k)} \operatorname{tr} \left(\mathbf {g} _ {i, n} \mathbf {g} _ {i, n} ^ {H} \mathbf {v} _ {k, n} \mathbf {v} _ {k, n} ^ {H}\right) p _ {i} + \delta_ {2} ^ {2} \\ \leq \left(\frac {Y _ {k , n} \tilde {\Gamma} _ {k , n} ^ {\# g - s} - Y _ {k , n} ^ {\#} \tilde {\Gamma} _ {k , n} ^ {g - s} + Y _ {k , n} ^ {\#} \tilde {\Gamma} _ {k , n} ^ {\# g - s}}{\left(\tilde {\Gamma} _ {k , n} ^ {\# g - s}\right) ^ {2}}\right) p _ {k}, \tag {30} \\ \end{array}
$$

where $\begin{array} { r l r } { Y _ { k , n } } & { { } = } & { \mathrm { t r } \left( \mathbf { g } _ { k , n } \mathbf { g } _ { k , n } ^ { H } \mathbf { v } _ { k , n } \mathbf { v } _ { k , n } ^ { H } \right) } \end{array}$ and Y #k,n $\begin{array} { r l } { Y _ { k , n } ^ { \# } } & { { } = } \end{array}$ $\mathrm { t r } \left( \mathbf { g } _ { k , n } \mathbf { g } _ { k , n } ^ { H } \mathbf { v } _ { k , n } ^ { \# } \mathbf { v } _ { k , n } ^ { \# } H \right) . \mathbf { \Delta } \mathbf { v } _ { k , n } ^ { \# }$ v# and Γ˜#g−s $\tilde { \Gamma } _ { k , n } ^ { \# g - s }$ are the values of $\mathbf { v } _ { k , n }$ and $\tilde { \Gamma } _ { k , n } ^ { g - s }$ in the last iteration, respectively. Furthermore, by using the semi-definite relaxation (SDR) technique, i.e., $\mathbf { W } _ { k , m } = \mathbf { w } _ { k , m } \mathbf { w } _ { k , m } ^ { H }$ and $\mathbf { V } _ { k , n } = \mathbf { v } _ { k , n } \mathbf { v } _ { k , n } ^ { H }$ , the beamforming design subproblem (22) can be reconstructed as

$$
\min _ {\Lambda} \sum_ {k = 1} ^ {K} \rho_ {k} ^ {g} \left(\sum_ {m = 1} ^ {M} \alpha_ {k, m} p _ {k} A _ {k, m} ^ {g} + \sum_ {n = 1} ^ {N} \beta_ {k, n} p _ {k} A _ {k, n} ^ {s}\right) \tag {31a}
$$

s.t. (22d), (23), (24), (26), (27),

$$
\begin{array}{l} \sum_ {\pi^ {m} (i) > \pi^ {m} (k)} \mathrm{tr} (\mathbf {h} _ {i, m} \mathbf {h} _ {i, m} ^ {H} \mathbf {W} _ {k, m}) p _ {i} + \delta_ {1} ^ {2} \\ \leq \left(\frac {X _ {k , m} \tilde {\Gamma} _ {k , m} ^ {\# g - g} - X _ {k , m} ^ {\#} \tilde {\Gamma} _ {k , m} ^ {g - g} + X _ {k , m} ^ {\#} \tilde {\Gamma} _ {k , m} ^ {\# g - g}}{\left(\tilde {\Gamma} _ {k , m} ^ {\# g - g}\right) ^ {2}}\right) p _ {k}, \tag {31b} \\ \end{array}
$$

$$
\sum_ {\pi^ {n} (i) > \pi^ {n} (k)} \mathrm{tr} (\mathbf {g} _ {i, n} \mathbf {g} _ {i, n} ^ {H} \mathbf {V} _ {k, n}) p _ {i} + \delta_ {2} ^ {2}
$$

$$
\leq \left(\frac {Y _ {k , n} \tilde {\Gamma} _ {k , n} ^ {\# g - s} - Y _ {k , n} ^ {\#} \tilde {\Gamma} _ {k , n} ^ {g - s} + Y _ {k , n} ^ {\#} \tilde {\Gamma} _ {k , n} ^ {\# g - s}}{\left(\tilde {\Gamma} _ {k , n} ^ {\# g - s}\right) ^ {2}}\right) p _ {k}, (3 1 c)
$$

$$
\mathbf {W} _ {k, m} \succeq 0, \mathbf {V} _ {k, n} \succeq 0, \tag {31d}
$$

$$
\operatorname{tr} (\mathbf {W} _ {k, m}) = \operatorname{tr} (\mathbf {V} _ {k, n}) = 1, \tag {31e}
$$

where $\begin{array} { r l r } { \Lambda } & { { } \triangleq } & { \{ \mathbf { W } _ { k , m } , \mathbf { V } _ { k , n } , A _ { k , m } ^ { g } , A _ { k , n } ^ { s } , \tilde { R } _ { k , m } ^ { g - g } , \tilde { \Gamma } _ { k , m } ^ { g - g } , \tilde { R } _ { k , n } ^ { g - s } , } \end{array}$ $\tilde { \Gamma } _ { k . n } ^ { g - s } , \forall k \in K , \forall m \in M , \forall n \in N \}$ . It is worth pointing that the nonconvex rank-one constraints Rank $\mathbf { \Phi } ( \mathbf { W } _ { k , m } ) = 1$ and Rank $( \mathbf { V } _ { k , n } ) = 1$ in problem (31) have been dropped because it is proved in Appendix A that the solutions always meet the rank-one constraints. Through a series of transformation, problem (31) become a standard convex optimization problem, which can be directly solved by some optimization toolboxes, such as CVX [44]. As a result, after obtaining the optimal solution $( \mathbf { W } _ { k , m } ^ { * } , \mathbf { V } _ { k , n } ^ { * } )$ to problem (31), the optimal solution $( \mathbf { w } _ { k , m } ^ { * } , \mathbf { v } _ { k , n } ^ { * } )$ to problem (21) can be obtained via eigenvalue decomposition (EVD).

Finally, the resource allocation subproblem by jointly optimizing transmit power and computing power can be formulated as

$$
\min _ {\mathbf {p}, \mathbf {q}, \mathbf {f}} \sum_ {k = 1} ^ {K} \rho_ {k} ^ {g} \left(E _ {k} ^ {g - g} + E _ {k} ^ {g - s}\right) + \sum_ {l = 1} ^ {L} \rho_ {l} ^ {s} E _ {l} ^ {s - s}
$$

$$
\text { s.t. } \quad (1 8 b) - (1 8 e), (1 8 i), (1 8 j). \tag {32}
$$

Since each GUE is allowed to select at most one BS or LEO satellite for computing offloading, problem (32) can be solved by two ways in terms of the transmit power of GUEs. Specifically, if $\alpha _ { k , m } ~ = ~ 1$ , the transmission energy consumption from the k-th GUE to the BS can be expressed as a function of the transmit power pk, i.e.,

$$
E _ {k} ^ {g - g, t r a} (p _ {k}) = \sum_ {m = 1} ^ {M} p _ {k} \frac {d _ {k}}{B _ {1} \log_ {2} \left(1 + \frac {| \mathbf {w} _ {k , m} ^ {H} \mathbf {h} _ {k , m} | ^ {2} p _ {k}}{I _ {k , m} ^ {g} + \delta_ {1} ^ {2}}\right)}, \tag {33}
$$

where Igk,m $I _ { k , m } ^ { g } = \sum _ { \pi ^ { m } ( i ) > \pi ^ { m } ( k ) } { | \bf w } _ { k , m } ^ { H } \mathbf { h } _ { i , m } | ^ { 2 } p _ { i }$ . And if $\beta _ { k , n } = 1$ , the transmission energy consumption from the k-th GUE to the LEO satellite is also a function of $p _ { k }$ , which is given by

$$
E _ {k} ^ {g - s, t r a} \left(p _ {k}\right) = \sum_ {n = 1} ^ {N} p _ {k} \frac {d _ {k}}{B _ {2} \log_ {2} \left(1 + \frac {\left| \mathbf {v} _ {k , n} ^ {H} \mathbf {g} _ {k , n} \right| ^ {2} p _ {k}}{I _ {k , n} ^ {s} + \delta_ {2} ^ {2}}\right)}, \tag {34}
$$

where ${ \cal I } _ { k , n } ^ { s } \ = \ \sum _ { \pi ^ { n } ( i ) > \pi ^ { n } ( k ) } | \mathbf { v } _ { k , n } ^ { H } \mathbf { g } _ { i , n } | ^ { 2 } p _ { i } .$ πn(i)>πn(k) . It is obvious that functions $E _ { k } ^ { g - g , t r a } \left( p _ { k } \right)$ and $E _ { k } ^ { g - s , t r a } \left( p _ { k } \right)$ are monotonically increasing for variable $p _ { k }$ , whose minimum values can be obtained when the variable is minimized. Thus, according to the delay requirements of GUEs in constraint (18b), the optimal solution for the transmit power of GUEs can be computed as

pk

$$
= \left\{ \begin{array}{l l} \min \left(\frac {I _ {k , m} ^ {g} + \delta_ {1} ^ {2}}{\left| w _ {k , m} ^ {H} h _ {k , m} \right| ^ {2}} \left(2 ^ {\frac {d _ {k}}{B _ {1} Z _ {k , m} ^ {\alpha}}} - 1\right), P _ {k} ^ {\max}\right), & \text { if } \alpha_ {k, m} = 1, \\ \min \left(\frac {I _ {k , n} ^ {s} + \delta_ {2} ^ {2}}{\left| v _ {k , n} ^ {H} g _ {k , n} \right| ^ {2}} \left(2 ^ {\frac {d _ {k}}{B _ {2} Z _ {k , n} ^ {\beta}}} - 1\right), P _ {k} ^ {\max}\right), & \text { if } \beta_ {k, n} = 1, \end{array} \right. \tag {35}
$$

where Zαk,m $Z _ { k , m } ^ { \alpha } \ = \ Z _ { k } ^ { g } - d _ { k } c _ { k } / f _ { k , m } ^ { g r o }$ and $Z _ { k , n } ^ { \beta } ~ = ~ Z _ { k } ^ { g } - { d _ { k } c _ { k } } / { }$ f sat−gk,n − φk,n/µ. In addition, the transmission energy con- $f _ { k , n } ^ { s a t - g } - \varphi _ { k , n } / \mu$ Jk,n sumption from the l-th SUE to the LEO satellite is a nonconvex function for the transmit power of SUEs $q _ { l } .$ , namely

$$
E _ {l} ^ {s - s, t r a} (q _ {l}) = q _ {l} \frac {d _ {l} ^ {s p a c e}}{B _ {3} \log_ {2} (1 + q _ {l} I _ {l})}, \tag {36}
$$

where $\begin{array} { r } { I _ { l } = \underset { n = 1 } { \overset { N } { \sum } } \gamma _ { l , n } \eta _ { l } ^ { t } \eta _ { n } ^ { r } \bigg ( \frac { \lambda } { 4 \pi \phi _ { l , n } } \bigg ) ^ { 2 } G _ { l } ^ { t } G _ { n } ^ { r } L _ { l } ^ { t } L _ { n } ^ { r } / \delta _ { 3 } ^ { 2 } } \end{array}$ 4πϕl,n . In order to resolve the nonconvexity of $E _ { l } ^ { s - s , t r a } \left( q _ { l } \right)$ ) in (36), duce auxiliary variable q˜l = 1log (1+qlIl $\begin{array} { r } { \tilde { q } _ { l } = \frac { 1 } { \log _ { 2 } ( 1 + q _ { l } I _ { l } ) } \geq 0 . } \end{array}$ ) ≥ 0, and then Es−s,tral $E _ { l } ^ { s - s , t r a }$ be rewritten as a convex function of $\tilde { q } _ { l }$ , i.e.,

$$
E _ {l} ^ {s - s, t r a} \left(\tilde {q} _ {l}\right) = \frac {d _ {l} ^ {s p a c e}}{B _ {3} I _ {l}} \tilde {q} _ {l} \left(2 ^ {\frac {1}{\tilde {q} _ {l}}} - 1\right). \tag {37}
$$

At the same time, the transmission delay $T _ { l } ^ { s - s , t r a }$ from the l-th SUE to the LEO satellite is replaced by

$$
T _ {l} ^ {s - s, t r a} (\tilde {q} _ {l}) = \frac {\tilde {q} _ {l} d _ {l} ^ {s p a c e}}{B _ {3}}. \tag {38}
$$

For a given transmit power $p _ { k }$ of GUEs based on (35), the original problem (32) is equivalently transformed as

$$
\begin{array}{l} \min _ {\tilde {\mathbf {q}}, \mathbf {f}} \sum_ {k = 1} ^ {K} \rho_ {k} ^ {g} (E _ {k} ^ {g - g} + E _ {k} ^ {g - s}) \\ + \sum_ {l = 1} ^ {L} \rho_ {l} ^ {s} (E _ {l} ^ {s - s, t r a} (\tilde {q} _ {l}) + E _ {l} ^ {s - s, c o m}) \tag {39a} \\ \end{array}
$$

s.t. (18b), (18d), (18e),

$$
T _ {l} ^ {s - s, t r a} \left(\tilde {q} _ {l}\right) + T _ {l} ^ {s - s, c o m} + T _ {l} ^ {s - s, p r o} \leq Z _ {l} ^ {s}, \tag {39b}
$$

$$
\tilde {q} _ {l} \geq \frac {1}{\log_ {2} \left(1 + Q _ {l} ^ {\max} I _ {l}\right)}, \tag {39c}
$$

where $\tilde { \mathbf { q } } = \{ \tilde { q } \boldsymbol { \imath } , \forall l \in L \}$ . Since the objective function and all constraints of problem (39) are convex, it is likely to obtain its optimal solution by off-the-shelf methods. After obtaining the solution, the transmit power of SUEs can be computed as

$$
q _ {l} = \left(2 ^ {\frac {1}{\overline {{{q}}} _ {l}}} - 1\right) / I _ {l}. \tag {40}
$$

In conclusion, by iteratively optimizing offloading selection subproblem, beamforming design subproblem and resource allocation subproblem, a feasible solution can be achieved when its objective value converges. The proposed AO-based algorithm for satellite-terrestrial computing is summarized as Algorithm 1.

Remark 1: Note that the integrated satellite-terrestrial computing framework proposed in this paper is suitable for dynamic satellite-terrestrial networks. In particular, the satellite-terrestrial network is dynamic over time slots, but is relatively static in a time slot. For a dynamic satellite-terrestrial computing networks, once the topology and channel information is obtained in a time slot, the proposed Algorithm 1 can be employed to carry out computing offloading. As a result, different optimization results can be obtained for different time slots based on the dynamic characteristics of the network and channel to achieve highly reliable communication and low-latency computing at any moment. With strong payload processing capabilities of the new-generation LEO satellites, the computing task is able to be transmitted within a single time slot. In addition, we plan to analyze multi-hop computing offloading in the subsequent research to adjust the routing plan in time according to the dynamic changes of the network topology and to select the best transmission paths to achieve the cooperative resources utilization and efficient computing tasks processing.

Algorithm 1 Energy-Efficient Design of Satellite-Terrestrial Computing

Input: $K , L , M , N , N _ { t } ^ { g } , N _ { t } ^ { s } , Z _ { k } ^ { g } , Z _ { l } ^ { s } , d _ { k } , c _ { k } , d _ { l } ^ { s p a c e } , c _ { l } ^ { s p a c e } \rho _ { k } ^ { g } ,$ ce, cspaceρ $\rho _ { l } ^ { s } , F _ { m } ^ { g r o } , F _ { n } ^ { s a t } , P _ { k } ^ { \operatorname* { m a x } } , \tilde { Q _ { l } ^ { \operatorname* { m a x } } } .$

Output: $\alpha , \beta , \gamma , w , v , \mathbf { p } , \mathbf { q } , \mathbf { f } .$

1: Initialize iteration index $t = 0 , p _ { k } ^ { ( t ) } = P _ { k } ^ { \operatorname* { m a x } } / 2 , q _ { l } ^ { ( t ) } =$ $Q _ { l } ^ { \operatorname * { m a x } } / 2 , f _ { k , m } ^ { g r o ( t ) } = F _ { m } ^ { g r o } / K , f _ { k , n } ^ { s a t { - } \tilde { g } ( t ) } = \ddot { F } _ { n } ^ { s a t } / ( K + L ) .$ = F grom /K, f sat−k,n $f _ { l , n } ^ { s a t - s ( t ) } = F _ { n } ^ { s a t } / ( K + L )$ .

2: repeat

3: Obtain $\alpha ^ { ( t + 1 ) } , \beta ^ { ( t + 1 ) }$ and $\gamma ^ { ( t + 1 ) }$ based on the relaxation mapping method according to the problem (20) with fixed $\mathbf { \tilde { \mathbf { \psi } } } \mathbf { \tilde { \mathbf { \psi } } } \mathbf { \tilde { \mathbf { \psi } } } \mathbf { \tilde { \mathbf { \psi } } } \mathbf { \tilde { \mathbf { \psi } } } \mathbf { \tilde { \mathbf { \psi } } } \mathbf { \tilde { \mathbf { \psi } } } \mathbf { \tilde { \mathbf { \psi } } } \mathbf { \tilde { \mathbf { \psi } } } \mathbf { \tilde { \mathbf { \psi } } } \mathbf { \tilde { \mathbf { \psi } } } \mathbf { \tilde { \mathbf { \psi } } } \mathbf { \tilde { \mathbf { \psi } } } \mathbf { \tilde { \mathbf { \psi } } } \mathbf { \tilde { \mathbf { \psi } } } \mathbf { \tilde { \mathbf { \psi } } } \mathbf { \tilde { \mathbf { \psi } } } \mathbf { \tilde { \mathbf { \psi } } } \mathbf { \tilde { \mathbf { \psi } } } \mathbf { \tilde { \mathbf { \psi } } } \mathbf { \tilde { \mathbf { \psi } } } \mathbf { \tilde { \mathbf { \psi } } } \mathbf { \tilde { \mathbf { \psi } } } \mathbf { \tilde { \mathbf { \psi } } } \mathbf { \tilde { \mathbf { \psi } } } \mathbf { \tilde { \mathbf { \psi } } } \mathbf { \tilde { \mathbf { \psi } } } \mathbf { \tilde { \mathbf { \psi } } } \mathbf { \tilde { \mathbf { \psi } } } \mathbf { \tilde { \mathbf { \psi } } } \mathbf { \tilde { \mathbf { \psi } } } \mathbf { \tilde \psi } \mathbf { \psi } \mathbf { \psi } \mathbf { \psi \psi } \mathbf { \psi \psi } \mathbf { \psi \psi } \mathbf { \psi } \mathbf { \psi \psi } \mathbf { \psi \psi } \mathbf { \psi \psi } \mathbf { \psi \psi } \mathbf { \psi \psi } \mathbf { \psi \psi } \mathbf { \psi \psi } \mathbf { \psi \psi } \mathbf { \psi \psi } \mathbf { \psi \psi } \mathbf \mathbf { \psi \psi } \mathbf { \psi \psi \psi } \mathbf \mathbf { \psi \psi } \mathbf { \psi \psi \psi \psi } \mathbf \mathbf  \psi \psi \psi \psi \psi \psi \psi \psi \psi \psi \psi \psi \psi \psi \mathbf \psi \psi \psi \psi \psi \psi \psi \psi \psi \psi \psi \psi \psi \psi \psi \psi \mathbf \psi \psi \psi \psi \psi \psi \psi \psi $ and $\mathbf { f } ^ { ( t ) }$ ;

4: Obtain $\mathbf { \boldsymbol { w } } ^ { ( t + 1 ) }$ and $\mathbf { \nabla } _ { \pmb { v } ^ { ( t + 1 ) } }$ by solving problem (31) with fixed $ { \alpha } ^ { ( t + 1 ) } ,  { \beta } ^ { ( t + 1 ) } ,  { \gamma } ^ { ( t + 1 ) } ,  { \mathbf { p } } ^ { ( t ) } ,  { \mathbf { q } } ^ { ( t ) }$ and $\mathbf { f } ^ { ( t ) }$ ;

5: Compute $\mathbf { p } ^ { ( t + 1 ) }$ by equation (35);

6: Obtain $\mathbf { q } ^ { ( \bar { t } + 1 ) }$ and $\mathbf { \widehat { f } } ^ { ( t + 1 ) }$ by solving problem (39) with fixed $\mathbf { \boldsymbol { \alpha } } ^ { ( \lfloor + 1 ) } , \boldsymbol { \beta } ^ { ( t + 1 ) } , \boldsymbol { \gamma } ^ { ( t + 1 ) } , \boldsymbol { w } ^ { ( t + 1 ) } , \boldsymbol { v } ^ { ( t + 1 ) }$ and $\mathbf { p } ^ { ( t + 1 ) } \{$

7: Update $t = t + 1 ;$

8: until Convergence

# C. Algorithm Analysis

In this part, we analyze the convergence and complexity of the proposed algorithm to verify its feasibility for satellite-terrestrial computing in 6G wireless networks.

Convergence Analysis: For the sake of description, the objective value of problem (18) at the t-th iteration is defined as $\mathbf { \bar { \rho } } \equiv \left( \mathbf { \alpha } \mathbf { \alpha } ^ { ( t ) } , \beta ^ { ( t ) } , \boldsymbol { \hat { \gamma ^ { ( t ) } } } , \boldsymbol { w } ^ { ( t ) } , \boldsymbol { v } ^ { ( t ) } , \mathbf { p } ^ { ( t ) } , \mathbf { q } ^ { ( t ) } , \mathbf { f } ^ { ( t ) } \right)$ . According to Algorithm 1, the solution to the original problem (18) is achieved by iteratively implementing steps 3-6. Particularly, in step 3 of Algorithm 1, since the optimal solutions of offloading selection subproblem $\alpha ^ { ( t + 1 ) } , \beta ^ { ( t + 1 ) }$ and $\gamma ^ { ( t + 1 ) }$ are obtained based on the relaxation mapping method with given other variables, we have

$$
\begin{array}{l} \Xi \left(\boldsymbol {\alpha} ^ {(t)}, \boldsymbol {\beta} ^ {(t)}, \boldsymbol {\gamma} ^ {(t)}, \boldsymbol {w} ^ {(t)}, \boldsymbol {v} ^ {(t)}, \mathbf {p} ^ {(t)}, \mathbf {q} ^ {(t)}, \mathbf {f} ^ {(t)}\right) \\ \geq \Xi \left(\boldsymbol {\alpha} ^ {(t + 1)}, \boldsymbol {\beta} ^ {(t + 1)}, \boldsymbol {\gamma} ^ {(t + 1)}, \boldsymbol {w} ^ {(t)}, \boldsymbol {v} ^ {(t)}, \mathbf {p} ^ {(t)}, \mathbf {q} ^ {(t)}, \mathbf {f} ^ {(t)}\right). \tag {41} \\ \end{array}
$$

Next, in step 4 of Algorithm 1, due to the convexity of beamforming design subproblem (31), we obtain

$$
\begin{array}{l} \Xi \left(\boldsymbol {\alpha} ^ {(t + 1)}, \boldsymbol {\beta} ^ {(t + 1)}, \boldsymbol {\gamma} ^ {(t + 1)}, \boldsymbol {w} ^ {(t)}, \boldsymbol {v} ^ {(t)}, \mathbf {p} ^ {(t)}, \mathbf {q} ^ {(t)}, \mathbf {f} ^ {(t)}\right) \\ \geq \Xi \left(\boldsymbol {\alpha} ^ {(t + 1)}, \boldsymbol {\beta} ^ {(t + 1)}, \boldsymbol {\gamma} ^ {(t + 1)}, \boldsymbol {w} ^ {(t + 1)}, \boldsymbol {v} ^ {(t + 1)}, \mathbf {p} ^ {(t)}, \mathbf {q} ^ {(t)}, \mathbf {f} ^ {(t)}\right). \tag {42} \\ \end{array}
$$

Then, because of the monotonicity of the objective function for the transmit power of GUEs, it is known that

$$
\begin{array}{l} \Xi \left(\boldsymbol {\alpha} ^ {(t + 1)}, \boldsymbol {\beta} ^ {(t + 1)}, \boldsymbol {\gamma} ^ {(t + 1)}, \boldsymbol {w} ^ {(t + 1)}, \boldsymbol {v} ^ {(t + 1)}, \mathbf {p} ^ {(t)}, \mathbf {q} ^ {(t)}, \mathbf {f} ^ {(t)}\right) \\ \geq \Xi \left(\boldsymbol {\alpha} ^ {(t + 1)}, \boldsymbol {\beta} ^ {(t + 1)}, \boldsymbol {\gamma} ^ {(t + 1)}, \boldsymbol {w} ^ {(t + 1)}, \boldsymbol {v} ^ {(t + 1)}, \mathbf {p} ^ {(t + 1)}, \mathbf {q} ^ {(t)}, \mathbf {f} ^ {(t)}\right). \tag {43} \\ \end{array}
$$

Similarly, since problem (39) is jointly convex with respect to the transmit power of SUEs and computing power, we have

$$
\begin{array}{l} \Xi \left(\boldsymbol {\alpha} ^ {(t + 1)}, \boldsymbol {\beta} ^ {(t + 1)}, \boldsymbol {\gamma} ^ {(t + 1)}, \boldsymbol {w} ^ {(t + 1)}, \boldsymbol {v} ^ {(t + 1)}, \mathbf {p} ^ {(t + 1)}, \mathbf {q} ^ {(t)}, \mathbf {f} ^ {(t)}\right) \\ \geq \Xi \left(\boldsymbol {\alpha} ^ {(t + 1)}, \boldsymbol {\beta} ^ {(t + 1)}, \boldsymbol {\gamma} ^ {(t + 1)}, \boldsymbol {w} ^ {(t + 1)}, \boldsymbol {v} ^ {(t + 1)}, \right. \\ \left. \mathbf {p} ^ {(t + 1)}, \mathbf {q} ^ {(t + 1)}, \mathbf {f} ^ {(t + 1)}\right). \tag {44} \\ \end{array}
$$

Finally, based on (41), (42), (43) and (44), we can conclude

$$
\begin{array}{l} \Xi \left(\boldsymbol {\alpha} ^ {(t)}, \boldsymbol {\beta} ^ {(t)}, \boldsymbol {\gamma} ^ {(t)}, \boldsymbol {w} ^ {(t)}, \boldsymbol {v} ^ {(t)}, \mathbf {p} ^ {(t)}, \mathbf {q} ^ {(t)}, \mathbf {f} ^ {(t)}\right) \\ \geq \Xi \left(\boldsymbol {\alpha} ^ {(t + 1)}, \boldsymbol {\beta} ^ {(t + 1)}, \boldsymbol {\gamma} ^ {(t + 1)}, \boldsymbol {w} ^ {(t + 1)}, \boldsymbol {v} ^ {(t + 1)}, \right. \\ \left. \mathbf {p} ^ {(t + 1)}, \mathbf {q} ^ {(t + 1)}, \mathbf {f} ^ {(t + 1)}\right), \tag {45} \\ \end{array}
$$

which indicates that the weighted total energy consumption is non-increasing during the iterations of Algorithm 1. In addition, there is a lower bound on the weighted total energy consumption of the satellite-terrestrial computing system, owing to the delay requirements of computing tasks. As a result, the convergence of Algorithm 1 is guaranteed according to the monotone bounded convergence theorem [45]. Furthermore, we confirm the convergence of Algorithm 1 for different numbers of GUEs and SUEs by simulation in Fig. 2.

Complexity Analysis: It is worth pointing out that the computational complexity of Algorithm 1 is mainly attributed to step 3, step 4 and step 6. For linear programming or convex optimization problem which only contains linear matrix inequalities (LMI) and second-order cone (SOC) constraints can be effectively solved by the interior point method [46]. Thus, it is possible to measure the worst-case complexity of the proposed algorithm by the interior point method [47]. Specifically, for the relaxation optimization problem (20) in step 3, it has $2 K + 2 L + M + N$ LMI constraints of dimension 1. Thus, for a given precision $\zeta _ { 1 } ~ > ~ 0$ , the worst-case complexity of obtaining the optimal solution for√ problem (20) is $\sqrt { 2 K + 2 L + M + N } \cdot \varpi _ { 1 } \cdot \ln ( 1 / \zeta _ { 1 } )$ , where $\varpi _ { 1 } = z _ { 1 } [ 2 K + 2 L + M + N + z _ { 1 } ( 2 K + 2 L + M + N ) + z _ { 1 } ^ { 2 } ]$ with decision variable $z _ { 1 } = \mathcal { O } ( K M + K N + L N )$ . Similarly, for the beamforming design subproblem (31) in step 4, there are $K ( 3 M + 3 N + 1 )$ LMI constraints of dimension 1, KM LMI constraints of dimension $N _ { t } ^ { g }$ , KN LMI constraints of dimension N s, KM SOC constraints of dimension $N _ { t } ^ { g } + 1$ and KN SOC constraints of dimension $N _ { t } ^ { s } + 1$ . In this context, for a given precision $\zeta _ { 2 } > 0 ,$ , the worst-case complexity of obtaining the optimal solution for problem (31) is $\sqrt { K ( M ( N _ { t } ^ { g } + 5 ) + N ( N _ { t } ^ { s } + 5 ) + 1 ) } \cdot \varpi _ { 2 } \cdot \ln ( 1 / \zeta _ { 2 } )$ , where $\circledast { 2 } = z _ { 2 } [ K M ( ( N _ { t } ^ { g } ) ^ { 3 } + ( \dot { N } _ { t } ^ { g ^ { - } } + 1 ) ^ { 2 } + 3 ) + K N ( ( N _ { t } ^ { s } ) ^ { 3 } + ( N _ { t } ^ { g } +$ $1 ) ^ { 2 } + 3 ) + K + K z _ { 2 } ( M ( ( N _ { t } ^ { g } ) ^ { 2 } + 3 ) + N ( ( N _ { t } ^ { s } ) ^ { 2 } + 3 ) + 1 ) + z _ { 2 } ^ { 2 } ]$ with decision variable $z _ { 2 } ~ = ~ \mathcal { O } ( K M { ( N _ { t } ^ { g } ) } ^ { 2 } + K N { ( N _ { t } ^ { s } ) } ^ { 2 } )$ . Finally, for step 6, there are $K + 2 L + M + N$ LMI constraints of dimension 1. Thus, for a given precision $\zeta _ { 3 } > 0 ,$ , the worst-case complexity of solving the problem (39) is $\sqrt { K + 2 L + M + N } . { \varpi _ { 3 } } . \ln ( 1 / { \zeta _ { 3 } } )$ , where $\varpi _ { 3 } = z _ { 3 } [ K + 2 L +$ $M + N { + } z _ { 3 } ( K { + } 2 L { + } M { + } N ) { + } z _ { 3 } ^ { 2 } ]$ with decision variable $z _ { 3 } =$ $\mathcal { O } ( K M + K N + L N )$ . To make it more intuitive, we show the realistic runtime of the proposed algorithm in an Intel i5- 10400F CPU by MATLAB simulation for different parameters in Table I. It is worth noting that dedicated processors are used for parallel computing processing in real-world applications to achieve millisecond response.

![](images/6228f0b2f8f7065d2f1a1d608c6e946e6562895b87d993a82e838f2119aaa461.jpg)

<details>
<summary>line</summary>

| Iteration Index | K=15, L=10 | K=10, L=15 | K=10, L=10 |
| --------------- | ---------- | ---------- | ---------- |
| 1               | 0.82       | 0.77       | 0.65       |
| 2               | 0.78       | 0.73       | 0.62       |
| 3               | 0.77       | 0.72       | 0.61       |
| 4               | 0.77       | 0.72       | 0.61       |
| 5               | 0.77       | 0.72       | 0.61       |
| 6               | 0.77       | 0.72       | 0.61       |
| 7               | 0.77       | 0.72       | 0.61       |
</details>

Fig. 2. Convergence behavior of Algorithm 1.

# IV. SIMULATION RESULTS

In this section, we present simulation results to validate the effectiveness of the proposed algorithm in practical satellite-terrestrial computing systems. Particularly, we consider that there is a Walker Delta constellation with orbital altitude of 550 km, inclination of 53 degrees, and constellation parameters of 1584/72/1, which represents the number of planes as 72, with 22 satellites in each plane and the phase factor of 1 [48]. Then, we select a set of neighboring satellites in the above satellite constellation for simulation based on the desired number of LEO satellites. In this context, it can be obtained that the communication distance $\varphi _ { k , n }$ between the GUE and the LEO satellite is in the range from about 550 km to 2700 km [49]. For convenience, it is assumed that all GUEs/SUEs have the same maximum transmission power budgets and delay requirements, and all MEC servers at the BSs/LEO satellites have the same maximum computing power, $\mathrm { i . e . , } \ P _ { k } ^ { \operatorname* { m a x } } = P _ { 0 } ^ { \operatorname* { m a x } } , Q _ { l } ^ { \operatorname* { m a x } } = Q _ { 0 } ^ { \operatorname* { m a x } } , Z _ { k } ^ { g } = Z _ { 0 } ^ { g } , Z _ { l } ^ { s } = Z _ { 0 } ^ { s } .$ $F _ { m } ^ { g r o } = F _ { 0 } ^ { g r o }$ = F g r o and $F _ { n } ^ { s a t } = F _ { 0 } ^ { s a t } , \forall k , l , m , n$ . Unless otherwise stated, the default simulation parameters are listed in Table II.

TABLE I THE REALISTIC RUNTIME (S) OF ALGORITHM 1 

<table><tr><td> $N_t^g = N_t^s$ </td><td>16</td><td>24</td><td>32</td><td>40</td><td>48</td><td>56</td><td>64</td></tr><tr><td>K=10,M=N=2</td><td>1.4088</td><td>1.5539</td><td>1.7751</td><td>2.0879</td><td>2.5873</td><td>3.1910</td><td>4.3601</td></tr><tr><td>K=20,M=N=2</td><td>2.7269</td><td>3.2337</td><td>3.9893</td><td>5.4930</td><td>8.1524</td><td>10.5377</td><td>12.8983</td></tr><tr><td>K=10,M=N=4</td><td>2.0136</td><td>2.2904</td><td>2.7164</td><td>3.4456</td><td>4.3796</td><td>6.2297</td><td>7.5781</td></tr><tr><td>K=20,M=N=4</td><td>4.1305</td><td>5.1796</td><td>7.2161</td><td>11.1879</td><td>15.1425</td><td>18.7489</td><td>23.8465</td></tr></table>

TABLE II SIMULATION PARAMETERS 

<table><tr><td>Parameters</td><td>Values</td></tr><tr><td>Number of GUEs and SUEs</td><td> $K = 10, L = 10$ </td></tr><tr><td>Number of BSs and its antennas</td><td> $M = 2, N_{t}^{g} = 16$ </td></tr><tr><td>Number of LEO satellites and its antennas</td><td> $N = 3, N_{t}^{s} = 16$ </td></tr><tr><td>Bandwidth</td><td> $B_{1} = B_{2} = 20 \text{ MHz}, B_{3} = 100 \text{ MHz}$ </td></tr><tr><td>Maximum transmit power budget of GUE and SUE</td><td> $P_{0}^{\max} = 30 \text{ dBm}, Q_{0}^{\max} = 30 \text{ dBm}$ </td></tr><tr><td>Computing task of GUE</td><td> $d_{k} \in [200 \sim 400] \text{ KB}, c_{k} \in [100 \sim 150] \text{ cycles/bit}$ </td></tr><tr><td>Computing task of SUE</td><td> $d_{k}^{space} \in [200 \sim 400] \text{ KB}, c_{k}^{space} \in [100 \sim 150] \text{ cycles/bit}$ </td></tr><tr><td>Delay requirement of GUE and SUE</td><td> $Z_{0}^{g} = 100 \text{ ms}, Z_{0}^{s} = 100 \text{ ms}$ </td></tr><tr><td>Maximum computing power of BS and LEO satellite</td><td> $F_{0}^{gro} = 30 \text{ GHz}, F_{0}^{sat} = 10 \text{ GHz}$ </td></tr><tr><td>Energy weights for GUE and SUE</td><td> $\rho_{k}^{g} = 1, \rho_{l}^{s} = 1$ </td></tr><tr><td>Noise power</td><td> $\sigma_{1}^{2} = \sigma_{2}^{2} = \sigma_{3}^{2} = -110 \text{ dBm}$ </td></tr><tr><td>Boltzmann constant</td><td> $\kappa = 1.38 \times 10^{-23} \text{ J/m}$ </td></tr><tr><td>Energy coefficient</td><td> $\tau_{m}^{gro} = \tau_{n}^{sat} = 5 \times 10^{-27} [50]$ </td></tr><tr><td>Carrier frequency</td><td> $f = 6 \text{ GHz}$ </td></tr><tr><td>Distance between SUE and LEO satellite</td><td> $\phi_{l,n} \in [500 - 1500] \text{ km}$ </td></tr><tr><td>Transmit antenna gain per noise temperature</td><td> $G_{k,n}/T = 34 \text{ dB/K}$ </td></tr><tr><td>Rain fading mean and variance</td><td> $\mu_{r} = -2.6 \text{ dB}, \sigma_{r}^{2} = 1.63 \text{ dB}$ </td></tr><tr><td>3-dB angle</td><td> $\varepsilon_{n}^{3dB} = 0.4^{\circ}$ </td></tr><tr><td>Maximum satellite antenna gain</td><td> $b_{n,\max} = 14 \text{ dBi}$ </td></tr><tr><td>Optical efficiency of the transmitter and receiver</td><td> $\eta_{l}^{t} = 0.9, \eta_{n}^{r} = 0.9$ </td></tr><tr><td>Wavelength</td><td> $\lambda = 1550 \text{ nm}$ </td></tr><tr><td>Aperture diameter of transmitter and receiver</td><td> $D_{l}^{t} = 20 \text{ cm}, D_{n}^{r} = 20 \text{ cm}$ </td></tr><tr><td>Pointing error angle of transmitter and receiver</td><td> $e_{l}^{t} = 0.8 \mu\text{rad}, e_{n}^{r} = 0.8 \mu\text{rad}$ </td></tr></table>

First of all, we provide the convergence of the Algorithm 1 with different numbers of GUEs and SUEs. From Fig. 2, it is evident that the value of the weighted total energy consumption decreases monotonically over the iterations and converges to a stable point within 5 iterations. Thus, the computational complexity of the proposed algorithm is affordable in practical applications for satellite-terrestrial computing systems.

Then, we present the superior performance of Algorithm 1 compared to five baseline algorithms, i.e., Fixed Transmit Power (FTP) Algorithm with $p _ { k } ~ = ~ P _ { K } ^ { \mathrm { m a x } } / 2$ and $q _ { l } =$ $Q _ { l } ^ { \mathrm { m a x } } / 2$ , Zero-Forcing Beamforming (ZFBF) Algorithm with zero-forcing receivers on BSs and LEO satellites [51],

![](images/510dcb9c2034d4f380b13d8cfef6ea6d9f748af470efd1048398164e86d87c1d.jpg)

<details>
<summary>line</summary>

| Delay Requirement of GUEs and SUEs: Z₀^g=Z₀^s (ms) | FTP Algorithm | ACR Algorithm [23] | RO Algorithm | HCO Algorithm [52] | ZFBF Algorithm [51] | Proposed Algorithm 1 |
| --- | --- | --- | --- | --- | --- | --- |
| 60 | 0.89 | 0.79 | 0.86 | 0.71 | 0.82 | 0.67 |
| 80 | 0.87 | 0.76 | 0.84 | 0.67 | 0.78 | 0.63 |
| 100 | 0.86 | 0.75 | 0.83 | 0.64 | 0.76 | 0.61 |
| 120 | 0.85 | 0.74 | 0.82 | 0.62 | 0.75 | 0.60 |
| 140 | 0.84 | 0.74 | 0.81 | 0.61 | 0.74 | 0.59 |
| 160 | 0.84 | 0.74 | 0.81 | 0.60 | 0.73 | 0.59 |
| 180 | 0.84 | 0.74 | 0.80 | 0.59 | 0.73 | 0.58 |
</details>

Fig. 3. Performance comparison of different algorithms.

Random Offloading (RO) Algorithm by randomly selecting any BS or LEO satellite, Average Computing Resources (ACR) Algorithm with $f _ { l , n } ^ { s a t - s } ~ = ~ F _ { n } ^ { s a t } / ( K + L )$ $f _ { k , m } ^ { g r o } ~ = ~ { \bf \bar { \nabla } } \bar { F } _ { m } ^ { g r o } / \bar { K }$ m m [23] and Heuristic Computing and $f _ { k , n } ^ { s a t - g } ~ =$ fk,n Offloading (HCO) Algorithm based on the constrained particle swarm optimization proposed in the related work [52]. In Fig. 3, it is seen that the proposed Algorithm 1 always consumes the minimum weighted total energy compared to other algorithms in the whole delay requirement region. This can be attributed to the fact that the proposed Algorithm 1 is adaptively optimized according to the characteristics of the integrated satellite-terrestrial 6G wireless network compared to other baselines, and heuristic algorithms often fail to reach the optimal value when solving large-scale 0-1 programming problems, which also validates the effectiveness of the proposed Algorithm 1. In addition, the more stringent delay requirement of GUEs and SUEs, the higher the energy consumption. This is because higher transmit power is used for data transmission and more computing resources are used to complete the computing tasks to meet stringent delay requirements. Thus, it makes sense to balance the performance between time cost and energy cost based on realistic scenarios.

![](images/010edf3d2d95288ef64ae997bcefde3b81f20ddc7ed785a3dbb538d58a2f7427.jpg)

<details>
<summary>bar</summary>

| Number of GUEs: K | Number of SUEs: L | Weighted Total Energy Consumption (J) |
| ----------------- | ----------------- | ------------------------------------ |
| 30                | 15                | 1.2                                  |
| 25                | 15                | 1.4                                  |
| 20                | 15                | 1.6                                  |
| 15                | 15                | 1.8                                  |
| 10                | 15                | 2.0                                  |
| 5                 | 15                | 1.8                                  |
| 30                | 20                | 1.6                                  |
| 25                | 20                | 1.4                                  |
| 20                | 20                | 1.2                                  |
| 15                | 20                | 1.0                                  |
| 10                | 20                | 0.8                                  |
| 5                 | 20                | 0.6                                  |
| 3                 | 25                | 0.4                                  |
| 2                 | 25                | 0.2                                  |
| 1                 | 25                | 0.1                                  |
| 0                 | 25                | 0.0                                  |
</details>

Fig. 4. Weighted total energy consumption versus different numbers of GUEs and SUEs.

Next, Fig. 4 reveals the impacts of the number of GUEs K and the number of SUEs L on the weighted total energy consumption for satellite-terrestrial computing in 6G wireless networks. Apparently, as the number of GUEs and SUEs increases, the weighted total energy consumption increases accordingly. On the one hand, the more data need to be processed, the more energy caused by data transmission and computing is consumed. On the other hand, increasing the number of GUEs will bring more co-channel interference, which degrades the data transmission efficiency. Therefore, the number of GUEs and SUEs supported by the integrated satellite-terrestrial 6G wireless network should match its affordable energy consumption level.

Furthermore, we investigate the effects of the bandwidth of the inter-terrestrial and satellite-terrestrial channels, as well as the number of antennas at BSs and LEO satellites on the weighted total energy consumption. In Fig. 5, it is seen that the weighted total energy consumption decreases as the channel bandwidth and the number of antennas increase, because both of them have a significant impact on the data transmission rate for computing tasks. Notice that the performance gain from $N _ { t } ^ { g } = N _ { t } ^ { s } = 2 4$ to $N _ { t } ^ { g } = N _ { t } ^ { s } = 3 2$ is less than that from $N _ { t } ^ { g } = N _ { t } ^ { s } = 1 6$ to $N _ { t } ^ { g } = N _ { t } ^ { s } = 2 4$ , indicating that the performance gain of the system by increasing the number of antennas is limited. Thus, a suitable number of antennas should be deployed at the BSs and LEO satellites to balance performance and cost.

![](images/d1aa4906aae87249d910e3929cecc6736e56e972fc291630da10caa2c608f44f.jpg)

<details>
<summary>line</summary>

| Bandwidth: B₁=B₂ (MHz) | Nᵗᵍ=Nᵗˢ=16 | Nᵗᵍ=Nᵗˢ=24 | Nᵗᵍ=Nᵗˢ=32 |
| ---------------------- | ---------- | ---------- | ---------- |
| 10                     | 1.2        | 0.9        | 0.78       |
| 14                     | 0.95       | 0.75       | 0.65       |
| 18                     | 0.8        | 0.65       | 0.57       |
| 22                     | 0.72       | 0.58       | 0.52       |
| 26                     | 0.65       | 0.54       | 0.49       |
| 30                     | 0.6        | 0.5        | 0.47       |
</details>

Fig. 5. Weighted total energy consumption versus bandwidth for different numbers of antennas at BSs and LEO satellites.

![](images/6c4a7d3d5c4bd3f5dac13f3c16d9e49d1b2467333e1ea60088ce317eef79b4eb.jpg)

<details>
<summary>line</summary>

| Number of LEO satellites: N | M=2   | M=3   | M=4   |
| ---------------------------- | ----- | ----- | ----- |
| 2                            | 0.73  | 0.57  | 0.51  |
| 3                            | 0.63  | 0.50  | 0.45  |
| 4                            | 0.61  | 0.48  | 0.43  |
| 5                            | 0.60  | 0.47  | 0.42  |
| 6                            | 0.60  | 0.46  | 0.42  |
</details>

Fig. 6. Weighted total energy consumption versus number of LEO satellites for different numbers of BSs.

Fig. 6 examines the influence of the number of BSs M and the number of LEO satellites N for satellite-terrestrial computing in 6G wireless networks. As is expected that increasing the number of BSs and LEO satellites leads to lower energy consumption, since it expands the total computing power of the system and also gives more offloading options for computing tasks at the same time. In fact, the proposed Algorithm 1 theoretically supports an arbitrary number of BSs and LEO satellites. However, in practical systems, it is essential to consider a combination of deployment costs, operational costs, and actual user requirements. The appropriate number of BSs and LEO satellites should be determined based on the specific circumstances to ensure the feasibility and cost-effectiveness of the system and to achieve the best possible performance in practical applications. Meanwhile, with the development of lightweight satellites, construction and launch costs have been greatly reduced, making it possible to deploy a large number of LEO satellites in real-world applications, e.g., starlink program with 42000 LEO satellites.

Finally, we show the impacts of the data size of computing tasks and the maximum computing power provided by the MEC servers on the performance of the weighted total energy consumption. It is seen that a larger amount of data requires more energy consumption since it requires longer time both in data transmission and processing. Moreover, the increase of the maximum computing capacity of the MEC servers at the BSs saves more energy consumption than that at the LEO satellites. This is because the computing tasks of GUEs are preferentially offloaded to the BSs when their MEC severs have sufficient computing resources, in order to avoid the long-distance propagation loss caused by the satelliteterrestrial communication.

![](images/2597bca98e256b010f30310fc1610dc31aeba7ee0d2a1b3f1d95f570d767b4e9.jpg)

<details>
<summary>bar</summary>

| Data Size | F₀^gro=20 GHz, F₀^sat=20 GHz (J) | F₀^gro=30 GHz, F₀^sat=20 GHz (J) | F₀^gro=20 GHz, F₀^sat=30 GHz (J) |
| :--- | :--- | :--- | :--- |
| dₖ,d₁^space ∈[200-300] kB | 0.42 | 0.28 | 0.38 |
| dₖ,d₁^space ∈[300-400] kB | 0.61 | 0.40 | 0.55 |
| dₖ,d₁^space ∈[400-500] kB | 0.82 | 0.54 | 0.73 |
</details>

Fig. 7. Weighted total energy consumption versus data sizes of computing tasks for different maximum computing power.

# V. CONCLUSION

This paper presented a comprehensive satellite-terrestrial computing architecture in 6G wireless networks. To enhance the overall performance, an energy-efficient design was proposed according to the characteristics of integrated satelliteterrestrial networks. In particular, the design was formulated as a complicated MINLP problem with weighted total energy consumption minimization while ensuring the delay requirements of GUEs and SUEs. To obtain the feasible solution, we decompose the original NP-hard problem into three subproblems, i.e., offloading selection, beamforming design and resource allocation, and then solve them iteratively in turn. Theoretical analysis confirmed the fast convergence behavior and low computational complexity of the proposed algorithm. Moreover, simulation results revealed some useful insights of parameter selection of the proposed algorithm.

# APPENDIX A

# PROOF OF THE RANK-ONE CONSTRAINTS

Herein, we give the proof for dropping the rank-one constraints in problem (31). Based on the offloading selection, problem (31) has two cases that the computing tasks are offloaded to the BS or to the LEO satellite. In particular, when $\alpha _ { k , m } = 1 $ , the Lagrangian function for problem (31) with respect to $\mathbf { W } _ { k , m }$ can be obtained as

$$
\begin{array}{l} \mathcal {L} (\mathbf {W} _ {k, m}) = \rho_ {k} ^ {g} p _ {k} A _ {k, m} ^ {g} + \xi_ {1} \left(\operatorname{tr} (\mathbf {W} _ {k, m}) - 1\right) \\ + \xi_ {2} \left(A _ {k, m} ^ {g} + \frac {d _ {k} c _ {k}}{f _ {k , n} ^ {s a t - g}} - Z _ {k} ^ {g}\right) \\ + \xi_ {3} \left(\frac {d _ {k}}{\tilde {R} _ {k , m} ^ {g - g}} - A _ {k, m} ^ {g}\right) \\ \end{array}
$$

$$
\begin{array}{l} + \xi_ {4} \left(\tilde {R} _ {k, m} ^ {g - g} - B _ {1} \log_ {2} \left(1 + \tilde {\Gamma} _ {k, m} ^ {g - g}\right)\right) \\ + \xi_ {5} \left(\sum_ {i = k + 1} ^ {K} \operatorname{tr} \left(\mathbf {h} _ {i, m} \mathbf {h} _ {i, m} ^ {H} \mathbf {W} _ {k, m}\right) p _ {i} + \delta_ {1} ^ {2} \right. \\ \left. - \frac {\operatorname{tr} (\mathbf {h} _ {k , m} \mathbf {h} _ {k , m} ^ {H} \mathbf {W} _ {k , m}) p _ {k}}{\tilde {\Gamma} _ {k , m} ^ {g - g}}\right) - \boldsymbol {\Omega} \mathbf {W} _ {k, m}, \\ \end{array}
$$

where $\xi _ { 1 } , \ldots , \xi _ { 5 }$ and Ω are the Lagrange multipliers. By utilizing the Karush-Kuhn-Tucher (KKT) conditions, we have

$$
\sum_ {i = k + 1} ^ {K} \operatorname{tr} (\mathbf {h} _ {i, m} \mathbf {h} _ {i, m} ^ {H} \mathbf {W} _ {k, m} ^ {*}) p _ {i} + \delta_ {1} ^ {2} \leq \frac {\operatorname{tr} (\mathbf {h} _ {k , m} \mathbf {h} _ {k , m} ^ {H} \mathbf {W} _ {k , m} ^ {*}) p _ {k}}{\tilde {\Gamma} _ {k , m} ^ {g - g}} \tag {46a}
$$

$$
\boldsymbol {\Omega} \mathbf {W} _ {k, m} ^ {*} = \mathbf {0} \tag {46b}
$$

$$
\begin{array}{l} \nabla_ {\mathbf {W} _ {k, m} ^ {*}} \mathcal {L} = \xi_ {1} ^ {*} \mathbf {I} _ {N _ {t} ^ {g}} \\ + \xi_ {5} ^ {*} \left(\sum_ {i = k + 1} ^ {K} \mathbf {h} _ {i, m} \mathbf {h} _ {i, m} ^ {H} p _ {i} - \frac {\mathbf {h} _ {k , m} \mathbf {h} _ {k , m} ^ {H} p _ {k}}{\tilde {\Gamma} _ {k , m} ^ {g - g}}\right) - \boldsymbol {\Omega} ^ {*} = \mathbf {0} \tag {46c} \\ \end{array}
$$

$$
\boldsymbol {\Omega} ^ {*} \succeq \mathbf {0}, \mathbf {W} _ {k, m} ^ {*} \succeq \mathbf {0}, \xi_ {1} ^ {*} \geq 0, \xi_ {5} ^ {*} \geq 0. \tag {46d}
$$

Since $\delta _ { 1 } ^ { 2 } > 0$ , it is inferred from (46a) that $\mathbf { W } _ { k , m } ^ { * } \neq \mathbf { 0 } ,$ , i.e.,

$$
\operatorname{Rank} (\mathbf {W} _ {k, m} ^ {*}) \geq 1. \tag {47}
$$

Moreover, it can be found from (46b) that

$$
\operatorname{Rank} (\boldsymbol {\Omega} ^ {*}) + \operatorname{Rank} (\mathbf {W} _ {k, m} ^ {*}) \leq N _ {t} ^ {g}. \tag {48}
$$

Based on (47) and (48), we have

$$
\operatorname{Rank} (\boldsymbol {\Omega} ^ {*}) \leq N _ {t} ^ {g} - 1. \tag {49}
$$

According to the properties of the rank of matrix, it is known from (46c) that

$$
\operatorname{Rank} \left(\boldsymbol {\Omega} ^ {*}\right) + \operatorname{Rank} (\boldsymbol {\Upsilon}) \geq \operatorname{Rank} \left(\xi_ {1} ^ {*} \mathbf {I} _ {N _ {t} ^ {g}}\right), \tag {50}
$$

where $\begin{array} { r } { \hat { \textbf { \textit { Y } } } = \ \xi _ { 5 } ^ { * } \left( \frac { \mathbf { h } _ { k , m } \mathbf { h } _ { k , m } ^ { H } p _ { k } } { \tilde { \Gamma } _ { k , m } ^ { g - g } } - \sum _ { i = k + 1 } ^ { K } \mathbf { h } _ { i , m } \mathbf { h } _ { i , m } ^ { H } p _ { i } \right) } \end{array}$ Obviously, $\Upsilon \neq \mathbf { 0 } ,$ namely Rank $\mathbf { \hat { \mathbf { \rho } } } ( \mathbf { \hat { T } } ) \geq 1$ . Considering the fact that $\mathrm { R a n k } ( \xi _ { 1 } ^ { * } \mathbf { I } _ { N _ { t } ^ { g } } ) = N _ { t } ^ { g }$ , we can infer that

$$
\operatorname{Rank} (\boldsymbol {\Omega} ^ {*}) \geq N _ {t} ^ {g} - 1. \tag {51}
$$

Combining (49) and (51), we have $\mathrm { R a n k } ( \Omega ^ { * } ) = N _ { t } ^ { g } - 1$ . Substituting it into (48), we can get

$$
\operatorname{Rank} (\mathbf {W} _ {k, m} ^ {*}) \leq 1. \tag {52}
$$

Finally, it is proved from (47) and (52) that $\mathrm { R a n k } ( \mathbf { W } _ { k , m } ^ { * } ) =$ 1. Similarly, when $\beta _ { k , n } ~ = ~ 1$ , it also can be verified that Rank $( \mathbf { V } _ { k , n } ^ { * } ) = 1$ always holds true. The proof is finished.

# REFERENCES

[1] K. Dolui and S. K. Datta, “Comparison of edge computing implementations: Fog computing, cloudlet and mobile edge computing,” in Proc. Global Internet Things Summit (GIoTS), Jun. 2017, pp. 1–6.   
[2] C. Ding, J.-B. Wang, H. Zhang, M. Lin, and G. Y. Li, “Joint optimization of transmission and computation resources for satellite and high altitude platform assisted edge computing,” IEEE Trans. Wireless Commun., vol. 21, no. 2, pp. 1362–1377, Feb. 2022.

[3] X. Zhu and C. Jiang, “Integrated satellite-terrestrial networks toward 6G: Architectures, applications, and challenges,” IEEE Internet Things J., vol. 9, no. 1, pp. 437–461, Jan. 2022.   
[4] X. Fang, W. Feng, T. Wei, Y. Chen, N. Ge, and C.-X. Wang, “5G embraces satellites for 6G ubiquitous IoT: Basic models for integrated satellite terrestrial networks,” IEEE Internet Things J., vol. 8, no. 18, pp. 14399–14417, Sep. 2021.   
[5] S. Chen, S. Sun, and S. Kang, “System integration of terrestrial mobile communication and satellite communication—The trends, challenges and key technologies in B5G and 6G,” China Commun., vol. 17, no. 12, pp. 156–171, Dec. 2020.   
[6] L. You et al., “Beam squint-aware integrated sensing and communications for hybrid massive MIMO LEO satellite systems,” IEEE J. Sel. Areas Commun., vol. 40, no. 10, pp. 2994–3009, Oct. 2022.   
[7] Y. Zhang, Y. Wu, A. Liu, X. Xia, T. Pan, and X. Liu, “Deep learning-based channel prediction for LEO satellite massive MIMO communication system,” IEEE Wireless Commun. Lett., vol. 10, no. 8, pp. 1835–1839, Aug. 2021.   
[8] J. Huang and J. Cao, “Recent development of commercial satellite communications systems,” in Artificial Intelligence in China. Singapore: Springer, 2020, pp. 531–536.   
[9] J. Zhang, X. Zhang, P. Wang, L. Liu, and Y. Wang, “Double-edge intelligent integrated satellite terrestrial networks,” China Commun., vol. 17, no. 9, pp. 128–146, Sep. 2020.   
[10] X. Zhu and C. Jiang, “Delay optimization for cooperative multi-tier computing in integrated satellite-terrestrial networks,” IEEE J. Sel. Areas Commun., vol. 41, no. 2, pp. 366–380, Feb. 2023.   
[11] Y. Song, X. Li, H. Ji, and H. Zhang, “Joint computing, caching and communication resource allocation in the satellite-terrestrial integrated network with UE cooperation,” in Proc. IEEE/CIC Int. Conf. Commun. China (ICCC), China, Aug. 2022, pp. 604–609.   
[12] K. An, M. Lin, J. Ouyang, and W.-P. Zhu, “Secure transmission in cognitive satellite terrestrial networks,” IEEE J. Sel. Areas Commun., vol. 34, no. 11, pp. 3025–3037, Nov. 2016.   
[13] A. Agarwal and P. Kumar, “Analysis of variable bit rate SOFDM transmission scheme over multi-relay hybrid satellite-terrestrial system in the presence of CFO and phase noise,” IEEE Trans. Veh. Technol., vol. 68, no. 5, pp. 4586–4601, May 2019.   
[14] J. Mashino and T. Sugiyama, “Subcarrier suppressed transmission for OFDMA in satellite/terrestrial integrated mobile communication system,” in Proc. IEEE Int. Conf. Commun. (ICC), Jun. 2011, pp. 1–5.   
[15] Z. Lin, M. Lin, J.-B. Wang, T. de Cola, and J. Wang, “Joint beamforming and power allocation for satellite-terrestrial integrated networks with non-orthogonal multiple access,” IEEE J. Sel. Topics Signal Process., vol. 13, no. 3, pp. 657–670, Jun. 2019.   
[16] Y. Zhang, L. Yin, C. Jiang, and Y. Qian, “Joint beamforming design and resource allocation for terrestrial-satellite cooperation system,” IEEE Trans. Commun., vol. 68, no. 2, pp. 778–791, Feb. 2020.   
[17] Z. Lin, M. Lin, T. de Cola, J.-B. Wang, W.-P. Zhu, and J. Cheng, “Supporting IoT with rate-splitting multiple access in satellite and aerial-integrated networks,” IEEE Internet Things J., vol. 8, no. 14, pp. 11123–11134, Jul. 2021.   
[18] Z. Lin et al., “Refracting RIS aided hybrid satellite-terrestrial relay networks: Joint beamforming design and optimization,” IEEE Trans. Aerosp. Electron. Syst., vol. 58, no. 4, pp. 3717–3724, Aug. 2022.   
[19] Z. Lin, M. Lin, B. Champagne, W.-P. Zhu, and N. Al-Dhahir, “Secrecyenergy efficient hybrid beamforming for satellite-terrestrial integrated networks,” IEEE Trans. Commun., vol. 69, no. 9, pp. 6345–6360, Sep. 2021.   
[20] Q. Wang, X. Chen, and Q. Qi, “Task-driven robust integration of communication and computation for edge-intelligent networks,” IEEE Trans. Commun., vol. 71, no. 1, pp. 244–255, Jan. 2023.   
[21] N. Eshraghi and B. Liang, “Joint offloading decision and resource allocation with uncertain task computing requirement,” in Proc. IEEE INFOCOM Conf. Comput. Commun., Apr. 2019, pp. 1414–1422.   
[22] H. Guo, J. Zhang, J. Liu, and H. Zhang, “Energy-aware computation offloading and transmit power allocation in ultradense IoT networks,” IEEE Internet Things J., vol. 6, no. 3, pp. 4317–4329, Jun. 2019.   
[23] Y. Wang, J. Zhang, X. Zhang, P. Wang, and L. Liu, “A computation offloading strategy in satellite terrestrial networks with double edge computing,” in Proc. IEEE Int. Conf. Commun. Syst. (ICCS), Dec. 2018, pp. 450–455.

[24] B. Wang, X. Li, D. Huang, and J. Xie, “A profit maximization strategy of MEC resource provider in the satellite-terrestrial double edge computing system,” in Proc. IEEE 21st Int. Conf. Commun. Technol. (ICCT), Oct. 2021, pp. 906–912.   
[25] K. Wei, Q. Tang, J. Guo, M. Zeng, Z. Fei, and Q. Cui, “Resource scheduling and offloading strategy based on LEO satellite edge computing,” in Proc. IEEE 94th Veh. Technol. Conf. (VTC-Fall), Sep. 2021, pp. 1–6.   
[26] Y. Mao, J. Zhang, and K. B. Letaief, “Dynamic computation offloading for mobile-edge computing with energy harvesting devices,” IEEE J. Sel. Areas Commun., vol. 34, no. 12, pp. 3590–3605, Dec. 2016.   
[27] Q. Qi, X. Chen, and D. W. K. Ng, “Robust beamforming for NOMAbased cellular massive IoT with SWIPT,” IEEE Trans. Signal Process., vol. 68, pp. 211–224, 2020.   
[28] Z. Song, Y. Hao, Y. Liu, and X. Sun, “Energy-efficient multiaccess edge computing for terrestrial-satellite Internet of Things,” IEEE Internet Things J., vol. 8, no. 18, pp. 14202–14218, Sep. 2021.   
[29] Coordinated Multi-Point Operation for LTE Physical Layer Aspects (Rel. 11), document TR 36.819 V1.0.0, 3GPP, Jun. 2011.   
[30] Q. Gao, M. Jia, Q. Guo, X. Gu, and L. Hanzo, “Jointly optimized beamforming and power allocation for full-duplex cell-free NOMA in space-ground integrated networks,” IEEE Trans. Commun., vol. 71, no. 5, pp. 2816–2830, May 2023.   
[31] Z. Gao, A. Liu, C. Han, and X. Liang, “Max completion time optimization for Internet of Things in LEO satellite-terrestrial integrated networks,” IEEE Internet Things J., vol. 8, no. 12, pp. 9981–9994, Jun. 2021.   
[32] J. Chu and X. Chen, “Robust design for integrated satellite-terrestrial Internet of Things,” IEEE Internet Things J., vol. 8, no. 11, pp. 9072–9083, Jun. 2021.   
[33] G. Zheng, S. Chatzinotas, and B. Ottersten, “Generic optimization of linear precoding in multibeam satellite systems,” IEEE Trans. Wireless Commun., vol. 11, no. 6, pp. 2308–2320, Jun. 2012.   
[34] M. A. Diaz, N. Courville, C. Mosquera, G. Liva, and G. E. Corazza, “Non-linear interference mitigation for broadband multimedia satellite systems,” in Proc. Int. Workshop Satell. Space Commun., Sep. 2007, pp. 61–65.   
[35] L. You, K.-X. Li, J. Wang, X. Gao, X.-G. Xia, and B. Ottersten, “Massive MIMO transmission for LEO satellite communications,” IEEE J. Sel. Areas Commun., vol. 38, no. 8, pp. 1851–1865, Aug. 2020.   
[36] P. Kumar and A. Srivastava, “Enhanced performance of FSO link using OFDM and comparison with traditional TDM-FSO link,” in Proc. IEEE Int. Broadband Photon. Conf. (IBP), Apr. 2015, pp. 65–70.   
[37] M. M. Tawfik, M. F. A. Sree, M. Abaza, and H. H. M. Ghouz, “Intersatellite optical wireless communication (IsOWC) system analysis for optimizing performance between GEO and LEO satellites,” in Proc. Int. Telecommun. Conf. (ITC-Egypt), Jul. 2021, pp. 1–4.   
[38] J. Wang, D. Feng, S. Zhang, A. Liu, and X.-G. Xia, “Joint computation offloading and resource allocation for MEC-enabled IoT systems with imperfect CSI,” IEEE Internet Things J., vol. 8, no. 5, pp. 3462–3475, Mar. 2021.   
[39] Y. Wang, M. Sheng, X. Wang, L. Wang, and J. Li, “Mobileedge computing: Partial computation offloading using dynamic voltage scaling,” IEEE Trans. Commun., vol. 64, no. 10, pp. 4268–4282, Oct. 2016.   
[40] S. Zhang, G. Cui, Y. Long, and W. Wang, “Joint computing and communication resource allocation for satellite communication networks with edge computing,” China Commun., vol. 18, no. 7, pp. 236–252, Jul. 2021.   
[41] J. Zhang, W. Xia, F. Yan, and L. Shen, “Joint computation offloading and resource allocation optimization in heterogeneous networks with mobile edge computing,” IEEE Access, vol. 6, pp. 19324–19337, 2018.   
[42] J. C. Bezdek and R. J. Hathaway, “Convergence of alternating optimization,” Neural, Parallel Sci. Comput., vol. 11, no. 4, pp. 351–368, 2003.   
[43] J. Clausen, “Branch and bound algorithms-principles and examples,” Dept. Comput. Sci., Univ. Copenhagen, Copenhagen, Denmark, Tech. Rep., 1999, pp. 1–30.   
[44] M. Grant and S. Boyd. (Sep. 2013). CVX: MATLAB Software for Disciplined Convex Programming. [Online]. Available: http://cvxr.com/cvx   
[45] V. A. Zorich and O. Paniagua, Mathematical Analysis II. Berlin, Germany: Springer, 2016.   
[46] A. Ben-Tal and A. Nemirovski, Lectures on Modern Convex Optimization: Analysis, Algorithms, and Engineering Applications (MPS-SIAM Series on Optimization). Philadelphia, PA, USA: SIAM, 2001.

[47] K.-Y. Wang, A. M. So, T.-H. Chang, W.-K. Ma, and C.-Y. Chi, “Outage constrained robust transmit optimization for multiuser MISO downlinks: Tractable approximations by conic optimization,” IEEE Trans. Signal Process., vol. 62, no. 21, pp. 5690–5705, Nov. 2014.   
[48] A. Al-Hourani, “Session duration between handovers in dense LEO satellite networks,” IEEE Wireless Commun. Lett., vol. 10, no. 12, pp. 2810–2814, Dec. 2021.   
[49] C. Spring-Turner and R. T. Rajan, “Performance bounds for cooperative localisation in the starlink network,” 2022, arXiv:2207.04691.   
[50] T. X. Tran and D. Pompili, “Joint task offloading and resource allocation for multi-server mobile-edge computing networks,” IEEE Trans. Veh. Technol., vol. 68, no. 1, pp. 856–868, Jan. 2019.   
[51] M. Lin, Z. Lin, W.-P. Zhu, and J.-B. Wang, “Joint beamforming for secure communication in cognitive satellite terrestrial networks,” IEEE J. Sel. Areas Commun., vol. 36, no. 5, pp. 1017–1029, May 2018.   
[52] J. Bi, H. Yuan, S. Duanmu, M. Zhou, and A. Abusorrah, “Energyoptimized partial computation offloading in mobile-edge computing with genetic simulated-annealing-based particle swarm optimization,” IEEE Internet Things J., vol. 8, no. 5, pp. 3774–3785, Mar. 2021.

![](images/d3012df7682ab590693c9957829d4510cc4e133e23051a79c03dfc1e6a1ca9ff.jpg)

<details>
<summary>natural_image</summary>

Portrait of a man wearing glasses and a striped shirt against a blue background (no text or symbols visible)
</details>

Xiaoming Chen (Senior Member, IEEE) received the B.Sc. degree in electronic engineering from Hohai University in 2005, the M.Sc. degree in electronic engineering from the Nanjing University of Science and Technology in 2007, and the Ph.D. degree in electronic engineering from Zhejiang University, Hangzhou, China, in 2011.

From March 2011 to October 2016, he was with the Nanjing University of Aeronautics and Astronautics, Nanjing, China. From February 2015 to June 2016, he was a Humboldt Research Fellow

with the Institute for Digital Communications, Friedrich-Alexander-University Erlangen-Nürnberg (FAU), Germany. He is currently a Professor with the College of Information Science and Electronic Engineering, Zhejiang University. His current research interests include LEO satellite constellation, the Internet of Things, and smart communications. He received the Best Paper Awards at the 2020 IEEE Global Communications Conference (GLOBE-COM), the 2020 International Conference on Wireless Communications and Signal Processing (WCSP), the 2019 IEEE International Conference on Communications (ICC), and the 2018 IEEE/CIC International Conference on Communications in China (ICCC). He served as an Editor for IEEE TRANS-ACTIONS ON COMMUNICATIONS and IEEE COMMUNICATIONS LETTERS and a Guest Editor for IEEE JOURNAL ON SELECTED AREAS IN COM-MUNICATIONS “Massive Access for 5G and Beyond” and IEEE WIRELESS COMMUNICATIONS “Massive Machine-Type Communications for IoT.”

![](images/4eabee825cc70d740d7c8dadb28a76ee3124981d90948ed6f7398300975466d8.jpg)

<details>
<summary>natural_image</summary>

Portrait photo of a young man in a black shirt (no text or symbols visible)
</details>

Qi Wang (Student Member, IEEE) received the B.E. degree in communication engineering from Nankai University, Tianjin, China, in 2021. He is currently pursuing the Ph.D. degree with the College of Information Science and Electronic Engineering, Zhejiang University, Hangzhou, China. His current research interests include integrated computing and communications, the Internet of Things, and satellite communications.

![](images/1b400396ea337ddd9e918dea2464e3b3d553590f99aed38ddf79c4518ca6e9f3.jpg)

<details>
<summary>natural_image</summary>

Portrait photo of a woman in formal attire against a blue background (no text or symbols visible)
</details>

Qiao Qi (Member, IEEE) received the B.S. degree in electronic information engineering from Hangzhou Dianzi University in 2018 and the Ph.D. degree in information and communication engineering from Zhejiang University, Hangzhou, China, in 2023. She is currently a Lecturer with the School of Information Science and Technology, Hangzhou Normal University, Hangzhou. Her current research interests include cellular IoT, edge intelligence, integrated sensing, and communication and computing.