# Joint UAV Deployment and Resource Allocation in THz-Assisted MEC-Enabled Integrated Space-Air-Ground Networks

Yan Kyaw Tun , Member, IEEE, György Dán , Senior Member, IEEE, Yu Min Park , and Choong Seon Hong , Fellow, IEEE

Abstract—Multi-access edge computing (MEC)-enabled integrated space-air-ground (SAG) networks have drawn much attention recently, as they can provide communication and computing services to wireless devices in areas that lack terrestrial base stations (TBSs). Leveraging the ample bandwidth in the terahertz (THz) spectrum, in this paper, we propose MEC-enabled integrated SAG networks with collaboration among unmanned aerial vehicles (UAVs). We then formulate the problem of minimizing the energy consumption of devices and UAVs in the proposed MEC-enabled integrated SAG networks by optimizing tasks offloading decisions, THz sub-bands assignment, transmit power control, and UAVs deployment. The formulated problem is a mixed-integer nonlinear programming (MILP) problem with a non-convex structure, which is challenging to solve. We thus propose a block coordinate descent (BCD) approach to decompose the problem into four sub-problems: 1) device task offloading decision problem, 2) THz sub-band assignment and power control problem, 3) UAV deployment problem, and 4) UAV task offloading decision problem. We then propose to use a matching game, concave-convex procedure (CCP) method, successive convex approximation (SCA), and block successive upperbound minimization (BSUM) approaches for solving the individual subproblems. Finally, extensive simulations are performed to demonstrate the effectiveness of our proposed algorithm.

Index Terms—Multi-access edge computing (MEC), integrated space-air-ground networks, task offloading, resource allocation, one-to-one matching game, successive convex approximation (SCA), block successive upper-bound minimization (BSUM).

## I. INTRODUCTION

NTERNET of Things (IoT) devices are expected to be I deployed worldwide for performing latency-sensitive tasks with significant computation requirements, such as autonomic navigation, road traffic monitoring, forest fire monitoring, and rescue operations in disaster areas [1]. However, it is problematic for energy-constraint IoT devices to execute complex tasks on time locally. Edge computing could enable the devices to execute their tasks on time by offloading the tasks to computing servers deployed at terrestrial base stations (TBSs) and access points (APs), but terrestrial networks may not be available in remote areas and in disaster areas.

MEC-enabled integrated SAG networks have recently emerged as a potential technology for providing remote computation services to IoT devices in areas where there is no terrestrial infrastructure [2], [3]. Integrated SAG networks can leverage the computational and communication resources of unmanned aerial vehicles (UAVs) and of low earth orbit (LEO) satellites for providing pervasive access to computing services.

A key requirement for the integrated SAG networks to become successful is high bitrate connectivity between IoT devices and UAVs. A promising candidate for this purpose could be THz communication, ranging from 0.1 to 10 THz, since it can provide higher bitrates due to the vast spectrum than what is achievable at lower frequency bands [4], [5], [6]. The main detriment of relying on the THz band is severe link attenuation, which is combined with high dispersion [7] and the easy obstruction of communication links through objects. Thus, the use of the THz frequency band in SAG networks could be feasible for short-range aerial communication, i.e., communication between UAVs and ground IoT devices to offload the devices’ tasks to the servers attached to UAVs for further processing, due to the existence of line-of-sight (LoS) communication links in the Air-to-Ground communication [8]. However, its efficient use requires joint consideration of UAV deployment for optimizing LoS communication links between UAVs and ground IoT devices, and the optimization of wireless resources, such as sub-band allocation and transmit power control [9], [10], [11].

In this paper, we address the above challenge, considering energy efficient task offloading in MEC-enabled integrated SAG networks. The considered architecture adopts the THz frequency band for aerial base stations (i.e., UAVs) to provide remote wireless access to the ground wireless devices for offloading their computation tasks to the edge servers installed at UAVs. Importantly, the proposed architecture allows collaboration among UAVs, i.e., UAVs can decide whether to relay computational tasks among each other or to offload them to LEO satellites. As a result of collaboration among the UAVs, the energy consumption of the devices can be further reduced.

To the best of our knowledge, this paper is the first to study the energy minimization problem in THz-assisted MEC-enabled integrated SAG networks, incorporating UAV collaboration by concurrently optimizing task offloading decisions of UAVs and devices, THz sub-bands assignment, transmit power control, and UAV deployment. The main contributions of this paper are as follows:

We first formulate the energy minimization problem in THz-assisted MEC-enabled integrated space-air-ground networks by optimizing the offloading decisions of the devices and the UAVs, THz sub-bands assignment and transmit power control, UAVs deployment, while satisfying the delay constraint of each device’s task, resource constraints of the THz band, and the transmit power constraint of each device.

Second, we show that the formulated problem is a nonconvex mixed integer programming problem due to the coupling of decision variables in the objective function and constraints. To obtain a solution, we divide the problem into four sub-problems using the block coordinate descent (BCD) method: 1) device task offloading decision problem, 2) the THz sub-band assignment and power control problem, 3) UAV deployment problem, and 4) UAV task offloading decision problem.

Third, we show that the device task offloading decision problem is convex and then propose the standard optimization technique to solve the problem. Then, a one-toone matching game and CCP approach are proposed to solve sub-bands assignment and power control problems. Finally, SCA and BSUM methods are proposed to solve the UAVs deployment and UAVs tasks offloading decision problems, respectively.

Finally, we demonstrate the convergence of the proposed algorithm by using extensive simulations. Furthermore, to show the effectiveness of our proposed algorithm, we compare the results of our proposed algorithm to the baseline schemes proposed in recent literature [12] and [13].

The rest of this paper is organized as follows. The related works and system model are described in Sections II and III, respectively. Section IV presents the problem formulation and the proposed solution is presented in Section V. Simulation results are shown in Section VI. Section VII concludes the paper.

## II. RELATED WORKS

## A. Multi-Access Edge Computing (MEC)-Enabled Integrated Space-Air-Ground Networks

MEC-enabled integrated SAG networks have received increasing attention in the recent literature [14], [15], [16], [17], [18], [19], [20]. In [14], the authors studied robust optimization-based UAV trajectory optimization and power control in SAG networks. Moreover, the work [15] investigated linear programming-based UAV trajectory optimization and task offloading scheme. However, both [14] and [15] only took into account a single UAV scenario, leaving out power control, resource allocation, and interference management. In [16], the authors proposed greedy and SCA-based task offloading and UAVs deployment schemes in the integrated SAG networks. The work [17] proposed radio resource allocation and task offloading framework for the integrated SAG vehicular networks. The authors in [18] investigated a machine learning-based framework for the MEC-enabled integrated SAG networks in order to offer computation services to numerous internet of vehicles (IoVs) in remote regions. In [19], the authors studied SCA-based hybrid task offloading and computing resource allocation scheme in the SAG networks. However, power control, interference management, and collaboration among UAVs were omitted in [16], [17], [18], [19]. The authors in [20] introduced the collaboration among UAVs in the multi-UAV-assisted MEC system. However, deployment of the UAVs, power control, interference management, and MEC-enabled satellites were omitted.

All of the aforementioned works, however, made the assumption that their proposed SAG networks would operate in the sub-6 GHz frequency band. With the rapid growth of connected wireless devices and the limited available bandwidth (i.e., communication resource) at the sub-6 GHz band, the maximum bandwidth usage at the considered frequency band has been reached. Thus, researchers are eager to explore the untouched THz frequency band with available abundant bandwidth to fill the resource requirement of the devices in future wireless networks.

## B. THz-Assisted Multi-Access Edge Computing

The management of the THz spectrum for MEC was considered in [21], [22], [23], [24], [25], [26], [27], [28], [29], [30], [31]. In [21], the authors proposed a secure mobile relaying system with UAV assistance that gathers data from several ground user equipment (UEs) and sends it to a destination using THz bands. The work [22] presented a viewpoint rendering offloading decision and transmit power control technique based on deep reinforcement learning for virtual reality (VR) video streaming via THz-wireless channels. Furthermore, in [23], the authors proposed a machine learning-based phase-shift design of IRS elements and rendering transmission for the VR system via IRS-assisted THz networks. The authors proved that using the THz frequency band could satisfy the ultra-reliable and low-latency requirement of the VR system in [24], and [25]. The work [26] discussed an optimization technique-based framework for the transmit power control and task offloading via THz frequency in the MEC system. In [27], the authors discussed the ruin theory-based age of information (AoI) minimization scheme in augmented reality (AR) system over THz networks. The work [28] presented a hybrid beamforming scheme for the vehicular networks over THz massive MIMO system. In [29], the authors proposed a penalty-constrained convex approximation (PCCA)-based framework for transferring data and power concurrently over THz networks. In [30], distributed proximal policy optimization (DPPO) based beamforming and phase-shift design for the IRS-assisted cooperative communication and sensing system over THz networks were examined. The study [31] presented a multi-hop IRS-assisted THz communication system beamforming architecture based on deep reinforcement learning.

![](images/e540278e18bb6e3f71756382c2b91e54bb4b910c517815a6ffc80c95bf05ad68.jpg)  
Fig. 1. Illustration of MEC-enabled integrated space-air-ground networks.

All of the aforementioned existing works separately considered THz-assisted wireless networks and MEC-enabled integrated SAG networks. As a result, in contrast to previously published studies, we explore MEC-enabled integrated SAG networks over the THz frequency band in this paper. Additionally, we consider collaboration among UAVs in the proposed THz-assisted MEC-enabled integrated SAG networks, which has never been taken into account in all of the existing works.

## III. SYSTEM MODEL

We consider a MEC system in the integrated space-air-ground network that consists of a set $\mathcal { I }$ of J wireless devices, a set K of K UAVs, and a set S of S LEO satellites, as illustrated in Fig. 1. Each device $j \in \mathcal { I }$ in the considered network has a latencysensitive computation task $T _ { j }$ , which can be characterized by a tuple $T _ { j } = \{ \varphi _ { j } , \alpha _ { j } , A _ { j } \}$ , where $\varphi _ { j }$ is the maximum tolerable delay of the task, $\alpha _ { j }$ is the CPU cycles needed to compute one bit of data, and $A _ { j }$ is the data size of the task. Devices are energy constrained, we thus consider that each device offloads a certain amount of data of its computation task to its associated UAVs. In this paper, we assume that the association between devices and UAVs is already determined depending on the distance via the K-means algorithm.

We use $\mathcal { T } _ { k }$ to denote the set of devices that offload a certain amount of data of their computation tasks to UAV $k ,$ and assume $\begin{array} { r } { \mathcal { I } = \bigcup _ { k = 1 } ^ { K } \mathcal { I } _ { k } } \end{array}$ where $\mathcal { T } _ { k } \cap \mathcal { T } _ { k ^ { \prime } } = \emptyset , \forall k , k ^ { \prime } \in \mathcal { K } , k \neq k ^ { \prime }$ We consider that the THz frequency band is adopted for communication between devices and UAVs due to the abundance of bandwidth in this frequency band. The available bandwidth in the considered THz frequency band is divided into a set B of $B$ sub-bands, and we use $\omega$ to denote the bandwidth of each sub-band. Since, the THz frequency band is only suitable for short-range communication due to severe link attenuation and dispersion, we consider that mmWave (28 GHz) backhaul links are adopted to communicate among UAVs and satellites. Furthermore, we consider that UAVs and satellites can obtain the channel state information (CSI) of associated devices and UAVs, e.g., using techniques presented in [32], [33], [34].

## A. Local Computing Model

Let $( A _ { j } - \beta _ { j } ^ { k } )$ be the amount of data of device $j ^ { \prime } { \bf s }$ task that is processed locally on device $j$ and $\beta _ { j } ^ { k }$ be the amount of data that is offloaded to the associated UAV $\bar { k } \in \mathcal { K }$ for remote computing. Thus, wireless device j’s local computation delay for completing the task which is calculated by [11] as

$$
l _ { j } ^ { k , \mathrm { l o c } } = \frac { ( A _ { j } - \beta _ { j } ^ { k } ) \alpha _ { j } } { f _ { j } } , \forall j \in \mathcal { I } ,\tag{1}
$$

where $f _ { j }$ represents the computation capacity of device $j .$ . The local energy usage of wireless device $j$ which is expressed in [11] as

$$
E _ { j } ^ { k , \mathrm { l o c } } = \kappa _ { j } ( f _ { j } ) ^ { 2 } \alpha _ { j } ( A _ { j } - \beta _ { j } ^ { k } ) , \forall j \in \mathcal { I } ,\tag{2}
$$

where $\kappa _ { j }$ is a constant that depends on the wireless device’s chip architecture.

## B. Communication Model

Each device uses one of the available THz sub-bands at its associated UAV for data transmission for offloading. We define $a _ { j } ^ { k , b } \in \{ 0 , 1 \}$ as the sub-band assignment variable, which represents whether or not sub-band b is assigned to device $j$ associated to UAV $k ,$ i.e.,

$$
a _ { j } ^ { k , b } = \left\{ { \begin{array} { l } { 1 , \ { \mathrm { i f ~ s u b - b a n d } } \ b { \mathrm { ~ i s ~ a s s i g n e d ~ t o ~ d e v i c e } } \ j , \ { \mathrm { w h i c h } } } \\ { { \mathrm { o f f l o a d s } } \ \beta _ { j } ^ { k } \ { \mathrm { a m o u n t ~ o f ~ d a t a ~ o f ~ i t s ~ t a s k ~ t o ~ U A V } } \ k , } \\ { 0 , \ { \mathrm { o t h e r w i s e } } . } \end{array} } \right.\tag{3}
$$

We consider that the orthogonal frequency division multiple access (OFDMA) scheme is used for communication between a UAV and its associated devices in order to avoid intra-cell interference. To improve spectrum efficiency, we consider frequency reuse between UAVs, i.e., all UAVs operate on the same frequency band to communicate with their associated devices. Thus, inter-cell interference between different UAVs may exist. As a result, in each UAV, a sub-band can be assigned to at most one device,

$$
\sum _ { j \in \mathcal { T } _ { k } } a _ { j } ^ { k , b } \leq 1 , \forall b \in \boldsymbol { B } , \forall k \in \boldsymbol { K } .\tag{4}
$$

Furthermore, we assume that at most one sub-band can be assigned to a device,

$$
\sum _ { b \in \mathcal { B } } a _ { j } ^ { k , b } \leq 1 , \forall j \in \mathcal { T } _ { k } , \forall k \in \mathcal { K } .\tag{5}
$$

Additionally, molecular absorption is the primary factor influencing signal propagation at the THz frequency band, leading to molecular absorption loss [35]. This loss is caused by certain types of molecules, such as $H _ { 2 } O$ vapor in the air, each with a distinct absorption spectrum. Given the proximity of UAVs to their associated devices and their ability to fly, we consider a line-of-sight (LoS) communication link between UAVs and their devices [9]. Thus, we can express the channel gain of device j on sub-band b to UAV k as [9]

$$
g _ { j } ^ { k , b } = g _ { 0 } ( d _ { j } ^ { k } ) ^ { - 2 } e ^ { - i _ { b } ( f ) d _ { j } ^ { k } } , \forall j \in \mathcal { T } _ { k } , \forall b \in \mathcal { B } , \forall k \in \mathcal { K } ,\tag{6}
$$

where $g _ { 0 }$ is the channel gain at reference distance d = 1 m, $i _ { b } ( f )$ is the coefficient of molecular absorption, which is influenced by both the concentration of water vapor molecules in the air and the network operating frequency (i.e., THz frequency), and $d _ { j } ^ { k }$ is the distance between device $j$ and UAV k, which can be computed as

$$
d _ { j } ^ { k } = \sqrt { ( x _ { k } - x _ { j } ) ^ { 2 } + ( y _ { k } - y _ { j } ) ^ { 2 } + h _ { k } ^ { 2 } } , \forall j \in \mathcal { T } _ { k } , \forall k \in \mathcal { K } ,\tag{7}
$$

where $\pmb { \ddot { c } } _ { j } = [ x _ { j } , y _ { j } ] ^ { T }$ and $\mathbf { \phi } _ { o _ { k } } = [ x _ { k } , y _ { k } ] ^ { T }$ are the horizontal coordinates of device $j \in \mathcal I$ and UAV $k \in \mathcal { K }$ respectively, and $h _ { k }$ is the hovering altitude of the UAV.

The received signal to interference plus noise ratio (SINR) between device j on sub-band b and its associated UAV k is then given by [9] as

$$
\gamma _ { j } ^ { k , b } = \frac { P _ { j } ^ { k , b } g _ { j } ^ { k , b } } { I _ { j } ^ { k , b } + \sigma ^ { 2 } } , \forall j \in \mathcal { T } _ { k } , \forall b \in \mathcal { B } , \forall k \in \mathcal { K } ,\tag{8}
$$

where $P _ { j } ^ { k , b }$ represents the transmit power of device $j , \sigma ^ { 2 }$ is the additive white Gaussian noise power, and

$$
I _ { j } ^ { k , b } = \sum _ { k ^ { \prime } \in \mathcal { K } , k ^ { \prime } \neq k } \sum _ { j ^ { \prime } \in \mathcal { J } , j ^ { \prime } \neq j } P _ { j ^ { \prime } } ^ { k ^ { \prime } , b } g _ { j ^ { \prime } } ^ { k , b }\tag{9}
$$

is the interference experienced at UAV k. Finally, we can calculate the achievable data rate of device $j$ on sub-band b as

$$
\begin{array} { r } { R _ { j } ^ { k , b } = \omega \log _ { 2 } ( 1 + \gamma _ { j } ^ { k , b } ) , \forall j \in \mathcal { T } _ { k } , \forall b \in \mathcal { B } , \forall k \in \mathcal { K } . } \end{array}\tag{10}
$$

We use (10) to compute the data rate $\begin{array} { r } { R _ { j } ^ { k } = \sum _ { b \in B } a _ { j } ^ { k , b } R _ { j } ^ { k , b } } \end{array}$ of device $j ,$ , which can be used for computing the transmission delay experienced by device j when offloading $\beta _ { j } ^ { k }$ amount of data of its task to UAV k which is described by [11] as

$$
l _ { j } ^ { k , \mathrm { t r a n s } } = \frac { \beta _ { j } ^ { k } } { R _ { j } ^ { k } } , \forall j \in \mathcal { T } _ { k } , \forall k \in \mathcal { K } .\tag{11}
$$

We express the transmission energy consumed at device j when offloading a $\beta _ { j } ^ { k }$ amount of data of its task to UAV k as [11]

$$
E _ { j } ^ { k , \mathrm { t r a n s } } = l _ { j } ^ { k , \mathrm { t r a n s } } \sum _ { b \in \mathcal { B } } P _ { j } ^ { k , b } , \forall j \in \mathcal { T } _ { k } , \forall k \in \mathcal { K } .\tag{12}
$$

After receiving the offloaded data from its associated devices, UAV k decides to either process them locally on its server or transfer them to neighboring UAVs or to the satellites.

Thus, we introduce the binary decision variable $x _ { j } ^ { k  k ^ { \prime } } \in$ $\{ 0 , 1 \}$ , indicating whether or not the offloaded data of device j is transferred to neighboring UAV $k ^ { \prime } \in \mathcal { K }$

$$
v _ { j } ^ { k  k ^ { \prime } } = \{ { \begin{array} { l } { 1 , ~ { \mathrm { i f ~ o f f l o a d e d ~ d a t a ~ o f ~ d e v i c e ~ } } j { \mathrm { ~ i s ~ t r a n s f e r r e d } } } \\ { { \mathrm { f r o m ~ U A V ~ } } k { \mathrm { ~ t o ~ U A V ~ } } k ^ { \prime } , } \\ { 0 , ~ { \mathrm { o t h e r w i s e } } . } \end{array} }\tag{13}
$$

We use $\begin{array} { r } { \beta ^ { k  k ^ { \prime } } = \sum _ { j \in \mathcal { T } _ { k } } v _ { j } ^ { k  k ^ { \prime } } \beta _ { j } ^ { k } } \end{array}$ to denote the total amount of data transferred from UAV k to UAV $k ^ { \prime } .$ The transmission time from UAV k to k<sup></sup> is determined by the achievable channel gain between these UAVs. Recall that the proposed integrated SAG network is meant to provide remote computing services to IoT devices in remote areas without terrestrial infrastructure. We expect that in these areas there would be few obstacles and thus we do not need to account for small-scale fading caused by the multi-path effect. Thus, taking the free space loss and rain attenuation into consideration, the achievable channel gain between UAV k to k<sup></sup> can be expressed as [20]

$$
\Gamma ^ { k  k ^ { \prime } } = \frac { P ^ { k  k ^ { \prime } } g _ { k } ^ { \mathrm { t x } } g _ { k ^ { \prime } } ^ { \mathrm { r x } } L _ { r } } { t _ { n } H B _ { \mathrm { m m } } ^ { k  k ^ { \prime } } } ( \frac { c } { 4 \pi d _ { k } ^ { k ^ { \prime } } f _ { c } ^ { \mathrm { m m } } } ) ^ { 2 } ,\tag{14}
$$

where $P ^ { k  k ^ { \prime } }$ is the transmit power of UAV k, $g _ { k } ^ { \mathrm { t x } }$ and $g _ { k ^ { \prime } } ^ { \mathrm { r x } }$ represent the antenna gains of the transmitter, UAV $k ,$ and the receiver UAV k<sup></sup>, L<sub>r</sub> is the amplification factor, $t _ { n }$ is the noise temperature, H is Boltzmann’s constant, $f _ { c } ^ { \mathrm { m m } }$ is the mmWave carrier frequency, $B _ { \mathrm { m m } } ^ { k  k ^ { \prime } }$ is the available bandwidth between UAV k and UAV k<sup></sup>, and $d _ { k } ^ { k ^ { \prime } }$ denotes the distance between UAV k and k<sup></sup>. Then, the achievable backhaul capacity between UAV k and k<sup></sup> is given by

$$
R ^ { k \to k ^ { \prime } } = B _ { \operatorname* { m m } } ^ { k \to k ^ { \prime } } \log _ { 2 } \Big ( 1 + \Gamma ^ { k \to k ^ { \prime } } \Big ) , \forall k , k ^ { \prime } \in \mathcal { K } .\tag{15}
$$

Finally, the transmission delay assuming that device j’s data is transferred to UAV k’ is as [20]

$$
l _ { j } ^ { k \to k ^ { \prime } , \mathrm { t r a n s } } = \frac { \beta ^ { k \to k ^ { \prime } } } { R ^ { k \to k ^ { \prime } } } , \forall k , k ^ { \prime } \in { \mathcal { K } } .\tag{16}
$$

Moreover, the total transmission energy consumed at UAV k when transferring the data of its associated devices to nearby UAV k<sup></sup> is given by [20] as

$$
E ^ { k \to k ^ { \prime } , \mathrm { t r a n s } } = P ^ { k \to k ^ { \prime } } \left( { \frac { \beta ^ { k \to k ^ { \prime } } } { R ^ { k \to k ^ { \prime } } } } \right) , \forall k , k ^ { \prime } \in { \mathcal { K } } .\tag{17}
$$

Finally, we introduce the binary decision variable $z _ { j } ^ { k  s } \in$ {0, 1}, to indicate whether or not UAV k transfers the offloaded data of device j to satellite s

$$
z _ { j } ^ { k  s } = \{ \begin{array} { l l } { { 1 , } } & { { \mathrm { i f ~ o f f l o a d e d ~ d a t a ~ o f ~ d e v i c e ~ } j \mathrm { ~ i s ~ t r a n s f e r r e d } } } \\ { { \mathrm { f r o m ~ U A V } \ k \mathrm { ~ t o ~ s a t e l l i t e } \ s , } } \\ { { 0 , } } & { { \mathrm { o t h e r w i s e . } } } \end{array}\tag{18}
$$

Let $\begin{array} { r } { \beta ^ { k  s } = \sum _ { j \in \mathcal { T } _ { k } } z _ { j } ^ { k  s } \beta _ { j } ^ { k } } \end{array}$ be the total amount of data transferred from UAV k to satellite s. Then, the transmission delay incurred when device j’s offloaded data is transferred from UAV k to satellite s can be expressed as [36]

$$
l _ { j } ^ { k \to s , \mathrm { t r a n s } } = \frac { \beta ^ { k \to s } } { R ^ { k \to s } } , \forall k \in \mathcal { K } , \forall s \in \mathcal { S } ,\tag{19}
$$

where $R ^ { k  s }$ is the achievable backhaul link capacity between the UAV and the satellite that can be calculated based on (15). Additionally, the amount of transmission energy used by UAV k when transferring the total offloaded data of its associated devices to the satellite s is given by [36]

$$
E ^ { k  s , \mathrm { t r a n s } } = P ^ { k  s } ( \frac { \beta ^ { k  s } } { R ^ { k  s } } ) , \forall k \in \mathcal { K } , \forall s \in \mathcal { S } .\tag{20}
$$

## C. Remote Computing Model

In order to express whether or not the offloaded data of device $j$ is computed at UAV k, we define the binary decision variable,

$w _ { j } ^ { j  k } \in \{ 0 , 1 \}$ , i.e.,

$w _ { j } ^ { k } = \left\{ { \bf { l } } _ { \backslash j } \right.$ , if offloaded data of device j is computed at UAV k, , otherwise.

(21)

If indeed the wireless device j’s offloaded data is computed at UAV k, i.e., $w _ { j } ^ { k } = 1$ , then the computation delay is [11]

$$
l _ { j } ^ { k , \mathrm { c o m p } } = \frac { \alpha _ { j } \beta _ { j } ^ { k } } { f _ { j } ^ { k } } , \forall j \in \mathcal { T } _ { k } , \forall k \in \mathcal { K } ,\tag{22}
$$

where $f _ { j } ^ { k }$ is the computation capacity of UAV k that is allotted to compute the offloaded data of wireless device j. We consider that the UAVs use proportional allocation [37] as

$$
f _ { j } ^ { k } = \frac { \alpha _ { j } \beta _ { j } ^ { k } } { \displaystyle \sum _ { j ^ { \prime } \in \mathcal { I } } w _ { j ^ { \prime } } ^ { k } \alpha _ { j ^ { \prime } } \beta _ { j ^ { \prime } } ^ { k } } F _ { k } ^ { \mathbf { m a x } } ,\tag{23}
$$

where $F _ { k } ^ { \mathbf { m a x } }$ denotes the computation capacity of UAV k. As a result, when wireless device j offloads ${ \beta } _ { j } ^ { \hat { k } }$ amount of data of its computation task to UAV k, the total delay it encounters is

$$
l _ { j } ^ { k , \mathrm { r e m o t e } } = l _ { j } ^ { k , \mathrm { t r a n s } } + l _ { j } ^ { k , \mathrm { c o m p } } , \forall j \in \mathcal { T } _ { k } , k \in \mathcal { K } .\tag{24}
$$

The energy usage at UAV k for processing the offloaded data of wireless device $j$ can be written as [11]

$$
E _ { j } ^ { k , \mathrm { c o m p } } = \kappa ( f _ { j } ^ { k } ) ^ { 2 } \alpha _ { j } \beta _ { j } ^ { k } , \forall j \in \mathcal { I } _ { k } , \forall k \in \mathcal { K } ,\tag{25}
$$

where κ is a constant that depends on the chip architecture of the UAV’s MEC server. Consequently, the total delay that the device j experiences when the offloaded data of its task is performed at UAV $k ^ { \prime }$ is as

$$
l _ { j } ^ { k  k ^ { \prime } , \mathrm { r e m o t e } } = l _ { j } ^ { k , \mathrm { t r a n s } } + l _ { j } ^ { k  k ^ { \prime } , \mathrm { t r a n s } } + l _ { j } ^ { k  k ^ { \prime } , \mathrm { c o m p } } , \forall j \in \mathcal { T } _ { k } ,
$$

$$
\forall k , k ^ { \prime } \in \mathcal { K } , k \neq k ^ { \prime } .\tag{26}
$$

Finally, let $l _ { i } ^ { k \to s , \mathrm { c o m p } }$ denote the computation delay when wireless device $j ^ { \mathrm { { ' } } } \mathrm { s }$ offloaded data is processed at satellite s which can be calculated based on (22). Then, the total delay that wireless device j encounters when its offloaded data is transferred to the satellite is

$$
l _ { j } ^ { k \to s , \mathrm { r e m o t e } } = l _ { j } ^ { k , \mathrm { t r a n s } } + l _ { j } ^ { k \to s , \mathrm { t r a n s } } + l _ { j } ^ { k \to s , \mathrm { c o m p } } + 2 l _ { j } ^ { k \to s , \mathrm { p r o } } ,
$$

$$
\forall j \in \mathcal { T } _ { k } , \forall k \in { \mathcal { K } } , \forall s \in { \mathcal { S } } ,\tag{27}
$$

where $2 l _ { j } ^ { k \to s , \mathrm { p r o } } = \frac { 2 d _ { k } ^ { s } } { c }$ is the round-trip propagation delay between UAV k and the satellite s. In this paper, we consider that the satellite has a renewable energy source. Thus, we disregard the satellite’s energy usage for computing the data transferred from all UAVs.

We make the reasonable assumption that the available computation capacity at the satellites is significantly greater than that at the UAVs and devices, and thus the computation time at the satellites is negligible compared to the computation time at the UAVs and devices. As a result, in our work, we do not account for the computation time of the satellites. Moreover, in the considered application scenario, the size of the output data after the offloaded task of each device has been executed at the MEC servers of UAVs and satellites is much less than the input data size of the offloaded task. We thus do not account for the downlink transmission time in the problem formulation. At the same time, our model accounts for the downlink propagation delay, which may be significant for satellite communication. Therefore, the downlink communication from the UAVs and satellites to the ground devices is disregarded in this study. Thus, the total delay encountered by device j when $\beta _ { j } ^ { k }$ amount of data of its computation task is offloaded to the associated UAV k for remote computing is as

$$
\begin{array} { r } { l _ { j } ^ { \mathrm { k , R e m o t e } } = w _ { j } ^ { k } l _ { j } ^ { k , \mathrm { r e m o t e } } + \displaystyle \sum _ { k ^ { \prime } \in \mathcal { K } , k ^ { \prime } \neq k } v _ { j } ^ { k  k ^ { \prime } } l _ { j } ^ { k  k ^ { \prime } , \mathrm { r e m o t e } } } \\ { + \displaystyle \sum _ { s \in \mathcal { S } } z _ { j } ^ { k  s } l _ { j } ^ { k  s , \mathrm { r e m o t e } } , \forall j \in \mathcal { T } _ { k } , \forall k \in \mathcal { K } . } \end{array}\tag{28}
$$

Finally, the total amount of energy used by the UAV to execute the offloaded data of the devices in the considered integrated SAG network is provided by

$$
E _ { k } ^ { \mathrm { { T o t } } } = \sum _ { j \in \mathcal { I } } w _ { j } ^ { k } E _ { j } ^ { k , \mathrm { { c o m p } } } + \sum _ { k ^ { \prime } \in \mathcal { K } , k ^ { \prime } \ne k } E ^ { k \to k ^ { \prime } , \mathrm { { t r a n s } } } + \sum _ { s \in \mathcal { S } } E ^ { k \to s , \mathrm { { t r a n s } } } ,
$$

$$
\forall k \in { \cal K } .\tag{29}
$$

## IV. PROBLEM FORMULATION

Our objective is to jointly optimize the deployment of UAVs, the task offloading decision for the devices and the UAVs, the transmit power, and the assignment of communication resources with the aim of minimizing the energy consumption of the UAVs and the devices subject to the available wireless resources (i.e., sub-bands and transmit power) and computing time constraints. Thus, we define the objective function as

$$
\mathbf { Q } ( o , \beta , P , a , w , v , z ) = \sum _ { k \in { \cal K } } \sum _ { j \in { \cal J } } \left( E _ { j } ^ { k , \mathrm { l o c } } + E _ { j } ^ { k , \mathrm { t r a n s } } \right) + \sum _ { k \in { \cal K } } E _ { k } ^ { \mathrm { T o t } } .\tag{30}
$$

We can then formulate the proposed optimization problem as

$$
\mathbf { P } : \operatorname* { m i m i z e } _ { o , \beta , P , a , w , v , z } \quad \mathbf { Q } ( o , \beta , P , a , w , v , z )\tag{31a}
$$

$$
\mathrm { s u b j e c t ~ t o ~ } l _ { j } ^ { k , \mathrm { l o c } } \leq \varphi _ { j } , \forall j \in \mathcal { I } _ { k } , \forall k \in \mathcal { K } ,\tag{31b}
$$

$$
l _ { j } ^ { k , \mathrm { R e m o t e } } \leq \varphi _ { j } , \forall j \in \mathcal { T } _ { k } , \forall k \in K ,\tag{31c}
$$

$$
0 \leq \beta _ { j } ^ { k } \leq A _ { j } , \forall j \in \mathcal { I } , \forall k \in \mathcal { K } ,\tag{31d}
$$

$$
\sum _ { b \in \mathcal { B } } a _ { j } ^ { k , b } \leq 1 \forall j \in \mathcal { T } _ { k } , \forall k \in \mathcal { K } ,\tag{31e}
$$

$$
\sum _ { j \in \mathcal { T } _ { k } } a _ { j } ^ { k , b } \leq 1 \forall b \in \boldsymbol { B } , \forall k \in \boldsymbol { K } ,\tag{31f}
$$

$$
0 \leq P _ { j } ^ { k , b } \leq P _ { j } ^ { \mathbf { m a x } } , \forall j \in \mathcal { I } _ { k } , \forall k \in \mathcal { K } ,\tag{31g}
$$

$$
w _ { j } ^ { k } + \sum _ { \stackrel { k ^ { \prime } \in \mathcal { K } } { k ^ { \prime } \ne k } } v _ { j } ^ { k  k ^ { \prime } } + \sum _ { s \in \mathcal { S } } z _ { j } ^ { k  s } = 1 ,
$$

$$
\forall j \in { \mathcal { I } } _ { k } ,\tag{31h}
$$

$$
a _ { j } ^ { k , b } \in \{ 0 , 1 \} , \forall j \in \mathcal { T } _ { k } , \forall b \in \mathcal { B } , \forall k \in \mathcal { K } ,\tag{31i}
$$

$$
w _ { j } ^ { k } \in \{ 0 , 1 \} , \forall j \in \mathcal { T } _ { k } , \forall k \in K ,\tag{31j}
$$

$$
v _ { j } ^ { k  k ^ { \prime } } \in \{ 0 , 1 \} , \forall j \in \mathcal { T } _ { k } , \forall k , k ^ { \prime } \in \mathcal { K } ,\tag{31k}
$$

$$
z _ { j } ^ { k  s } \in \{ 0 , 1 \} , \forall j \in \mathcal { T } _ { k } , \forall k \in K , \forall s \in S ,\tag{31l}
$$

$$
X _ { k } ^ { \mathbf { m i n } } \leq x _ { k } \leq X _ { k } ^ { \mathbf { m a x } } , \forall k \in \mathcal { K } ,\tag{31m}
$$

$$
Y _ { k } ^ { \mathbf { m i n } } \le y _ { k } \le Y _ { k } ^ { \mathbf { m a x } } , \forall k \in \mathcal { K } ,\tag{31n}
$$

where constraints (31b) and (31c) guarantee that a task is executed within the task’s maximum tolerable delay, then constraint (31d) assures that the data size of the task that is offloaded to the associated UAV $k \in \mathcal { K }$ must be less than the total input data size of the task of device j. Constraints (31e) and (31f) ensure that each THz sub-band in a UAV can only be assigned to one device, and the same is true for each device associated with a UAV. Constraint in (31g) guarantees that the device’s transmit power is less than its maximum available power. Constraint (31h) ensures that the offloaded data of the device is computed at a single location (i.e., at the associated UAV (or) one of the nearby UAVs (or) one of the LEO satellites). Moreover, (31i), (31j), (31k), and (31l) are the binary decision variables. Finally, limitations on the coordinates of each UAV are ensured by constraints (31m) and (31n).

## V. SOLUTION APPROACH

Convex optimization techniques cannot be employed directly to address the optimization problem in (31) because decision variables are coupled in the objective function and in the constraints, the problem has nonlinear constraints and binary variables, and has a non-convex structure. We thus propose to use the block coordinate descent (BCD) approach to decompose the problem into four sub-problems: 1) device task offloading decision problem, 2) sub-band assignment and transmit power control problem, 3) UAV deployment problem, and 4) UAV task offloading problem. Then, the decomposed sub-problems are solved alternatingly.

## A. Device Task Offloading Decision

For a given sub-band assignment and transmit power decision $\{ P , a \}$ , deployment {o} of UAVs, and offloading decision $\{ w , v , z \}$ of UAVs, we can formulate the device task offloading decision problem as

$$
{ \bf P 1 } : \operatorname* { m i n i m i z e } _ { \beta } { \bf Q } \left( \beta \right)\tag{32a}
$$

$$
\mathrm { s u b j e c t ~ t o ~ } l _ { j } ^ { k , \mathrm { l o c } } \leq \varphi _ { j } , \forall j \in \mathcal { I } _ { k } , \forall k \in \mathcal { K } ,\tag{32b}
$$

$$
l _ { j } ^ { k , \mathrm { R e m o t e } } \leq \varphi _ { j } , \forall j \in \mathcal { T } _ { k } , \forall k \in K ,\tag{32c}
$$

$$
0 \leq \beta _ { j } ^ { k } \leq A _ { j } , \forall j \in \mathcal { I } , \forall k \in K ,\tag{32d}
$$

From problem P1, we can see that the objective function (32a) and the constraints (32b)–(32d) are linear. Thus, we can conclude that problem P1 is convex. As a result, we can solve the problem using convex optimization techniques.

## B. Sub-Band Assignment and Power Control

For a given task offloading decision {β} of devices, a deployment $\{ o \}$ of UAVs, and offloading decision $\{ w , v , z \}$ of UAVs, we can formulate the sub-band assignment and power control problem as

$$
\mathbf { P 2 } : \operatorname* { m i m i m i z e } _ { P , a } \quad \mathbf { Q } ( P , a )\tag{33a}
$$

$$
{ \mathrm { s u b j e c t ~ t o ~ ( 3 1 c ) , ~ ( 3 1 e ) } } { \mathrm { - } } ( 3 1 \mathrm { g } ) , { \mathrm { ~ ( 3 1 i ) } } ,\tag{33b}
$$

Unfortunately, the decision variables in P2 are coupled in the objective function and in the constraints, and the problem has a combination of binary and continuous variables. Thus, problem P2 is a mixed-integer nonlinear programming (MINLP) problem that is NP-hard. Therefore, we develop a polynomial time two-stage distributed approach to address P2, by combining a matching game to assign sub-bands, and the concave-convex procedure (CCP) approach to evaluate the power control at each UAV.

Stage 1 (Sub-band Assignment): We want to maximize the total transmission rate of the devices because by doing so, we can decrease their transmission delay, i.e., constraint (31c), and transmission energy, i.e., the objective function, as indicated in (11) and (12), respectively. In other words, transmission energy and delay have an inverse relationship with data rate. As a result, we can formulate the sub-band assignment problem as a data rate (i.e., transmission rate between devices and UAVs) maximization problem. However, the sub-band assignment problem is a combinatorial integer programming problem. Thus, deploying centralized optimization techniques can cause significant overhead and complexity. As a result, we propose a low complexity distributed matching algorithm [38] to solve the problem. Since a wireless device can only have one sub-band assigned to it and a sub-band can only be assigned to a maximum of one device, we can model our sub-band assignment problem as a one-to-one matching game. We first provide the definition of the one-to-one matching game for sub-band assignment at each UAV $k \in { \mathcal { K } }$

Definition 1: Given two disjoint sets of players, $\mathcal { T } _ { k }$ and $B ,$ the one-to-one matching game $\vartheta _ { k } : { \mathcal { I } } _ { k }  B$ for the sub-band assignment is defined as:

$$
I ) \vartheta _ { k } ( b ) \subseteq { \mathcal { T } } _ { k } { \mathrm { ~ a n d ~ } } | \vartheta _ { k } ( b ) | \in \{ 0 , 1 \} , \forall b \in B ;
$$

$$
2 ) \vartheta _ { k } ( j ) \subseteq B \mathrm { ~ a n d ~ } | \vartheta _ { k } ( j ) | \in \{ 0 , 1 \} , \forall j \in \mathcal { T } _ { k } ;
$$

$$
3 ) \ : j = \vartheta _ { k } ( b )  b = \vartheta _ { k } ( j ) , \forall b \in \mathcal { B } , \forall j \in \mathcal { T } _ { k } .
$$

Here, $| \vartheta _ { k } ( . ) |$ is a representation of the cardinality of the matching outcome $\vartheta _ { k } ( . )$ . Conditions (1) and (2) in the definition ensure that a sub-band can only be assigned to one device at a time and that a device can only have one sub-band assigned to it. Furthermore, according to condition (3), if device $j$ is matched with sub-band $b ,$ then sub-band b must also be matched with device $j .$ . The outcome of the one-to-one matching game is the assignment mapping between a set of devices $\mathcal { T } _ { k }$ and sub-bands B.

First, we define the preference function of device $j \in \mathcal { I } _ { k }$ for sub-band $b \in B$ and the preference function of sub-band $b \in B$ for device $j \in \mathcal { I } _ { k }$ as $\theta _ { j } ( b )$ and $\theta _ { b } ( j )$ , respectively. The notation $b _ { 1 } \succ _ { j } b _ { 2 }$ implies that device $j$ prefers sub-band $b _ { 1 }$ over $b _ { 2 }$ , i.e., $\theta _ { j } ( b _ { 1 } ) > \theta _ { j } ( b _ { 2 } )$ , and at the same time the notation $j _ { 1 } \succ b \ j _ { 2 }$ indicates that the sub-band prefers device $j _ { 1 }$ over $j _ { 2 } ,$ $\mathrm { i . e . , } \theta _ { b } ( j _ { 1 } ) > \theta _ { b } ( j _ { 2 } )$

Algorithm 1: One-to-One Matching Game-Based   
Sub-Band Assignment Algorithm.   
1: Input: ${ \mathcal { I } } _ { k } , B ;$   
2: Initialization: Set $\mathcal { T } _ { k } ^ { \mathrm { u n } } = \mathcal { T } _ { k } , \mathcal { B } _ { j } = \mathcal { B } , \forall j \in \mathcal { T } _ { k }$ , a set   
of devices requested to sub-band $b , \mathcal { T } _ { k } ^ { b , \mathrm { r e q } } = \emptyset$ , and a   
set of rejected devices from sub-band $b , \mathcal { T } _ { k } ^ { b , \mathrm { r e j } } , \forall b \in \{ 1 \} ;$   
3: Construct the preference list of devices in $\mathcal { T } _ { k }$   
according to (34) by equally allocating its available   
transmit power to all sub-bands, i.e.,   
$\begin{array} { r } { P _ { j } ^ { k , b } = \frac { \bar { P } _ { j } ^ { \operatorname* { m a x } } } { B } , \forall j \in \mathcal { T } _ { k } ; } \end{array}$   
4: Find a stable matching $\vartheta _ { k } ^ { * }$   
5: while $\begin{array} { r } { \sum _ { b \in B } \sum _ { j \in \mathcal { T } _ { k } } q _ { j b } \ne } \end{array}$ 0 do   
6: for $j = 1$ to $| \mathcal { T } _ { k } ^ { \mathrm { u n } } |$ do   
7: Find b = argmax $\theta _ { j } ( b )$   
b∈B   
8: Make a request to the UAV k by setting $q _ { j b } = 1$   
9: end for   
10: for b = 1 to B do   
11: Update $\mathcal { T } _ { k } ^ { b , \mathrm { r e q } }  \{ j : q _ { j b } = 1 , \forall j \in \mathcal { T } _ { k } \}$   
12: Construct the preference list of UAV for its   
13: available sub-bands according to (35).   
14: Find j = argmax $\theta _ { b } ( j )$   
$\breve { j } \in \mathcal I _ { k }$   
15: Assign sub-band b to device $j .$   
16: Update $\mathcal { I } _ { k } ^ { b , \mathrm { r e j } }  \{ \mathcal { I } _ { k } ^ { b , \mathrm { r e q } } \backslash j \} .$   
17: Update $B _ { j }  \{ B _ { j } \setminus b \} , \forall j \in \mathcal { T } _ { k } ^ { b , \mathrm { r e j } } .$   
18: end for   
19: Update $\mathcal { T } _ { k } ^ { \mathrm { u n } }  \mathcal { T } _ { k } ^ { \mathrm { u n } } \cap \{ \mathcal { T } _ { k } ^ { 1 , \mathrm { r e j } } \cup . . . . \cup \mathcal { T } _ { k } ^ { B , \mathrm { r e j } } \}$   
20: end while   
21: Until: Achieve the stable matching $\vartheta _ { k } ^ { * }$   
22: Sub-bands Assignment: $\vartheta _ { k } ^ { * }  { \pmb a } _ { k }$

Preference of the device: The preference function of device j for sub-band b can be defined as

$$
\theta _ { j } ( b ) = \underbrace { \omega \log _ { 2 } \left( 1 + \frac { P _ { j } ^ { k , b } g _ { j } ^ { k , b } } { \sum _ { k ^ { \prime } \in K , k ^ { \prime } \neq k } \sum _ { j ^ { \prime } \in \mathcal { T } , j ^ { \prime } \neq j } P _ { j ^ { \prime } } ^ { k ^ { \prime } , b } g _ { j ^ { \prime } } ^ { k , b } + \sigma ^ { 2 } } \right) } _ { R _ { j } ^ { k , b } }\tag{34}
$$

The preference function of device $j \in \mathcal { I } _ { k }$ in (34) indicates two facts: 1) the device’s choice of sub-band only determines the transmission rate that can be achieved, which then determines the transmission delay and energy consumption when offloading a certain amount of data of its computation task to the associated UAV, as we can see in (11) and (12), and 2) the device would wish to offload a certain amount of its computation task to the associated UAV via the sub-band which can provide the highest transmission rate.

Preference of the UAV for its available sub-bands: UAV k’s preference function for matching device $j \in \mathcal { I } _ { k }$ with sub-band

$b \in B$ can be expressed as

$$
\begin{array} { l } { { \displaystyle \theta _ { b } ( j ) = \Phi _ { 1 } \underbrace { \omega \log _ { 2 } \left( 1 + \frac { P _ { j } ^ { k , b } g _ { j } ^ { k , b } } { k ^ { \prime } \in X , k ^ { \prime } \ne k \mathrm { ~ \underline { ~ } { ~ \epsilon ~ } } \epsilon \mathrm { ~ } \epsilon \mathrm { ~ J } _ { j } ^ { k ^ { \prime } , b } g _ { j ^ { \prime } } ^ { k , b } + \sigma ^ { 2 } } \right) } _ { { \displaystyle R _ { j } ^ { k , b } } } } } \\ { { - \underbrace { \sum _ { k ^ { \prime } \in K , k ^ { \prime } \ne k } \Phi _ { j } ^ { k ^ { \prime } , b } P _ { j } ^ { k , b } g _ { j } ^ { k ^ { \prime } , b } } _ { \mathrm { C u n u l a t i v i e r ~ f r e r e n c e ~ t o ~ o p h e r ~ U ~ \le ~ \epsilon ~ } } , } } \end{array}
$$

where $\Phi _ { 1 }$ and $\Phi _ { j } ^ { k ^ { \prime } , b }$ are weighting parameters. The UAV will assign sub-band b to device j in order to maximize the achievable transmission rate and reduce cumulative interference to the other UAVs, as can be shown in (35).

Definition 2: A stable matching $\vartheta _ { k } ^ { * }$ is achieved if there is no blocking pair $( j , b )$ , where a pair $( j , b )$ is a blocking pair when $j \notin \vartheta _ { k } ( b ) , b \notin \vartheta _ { k } ( j )$ , and $b \succ _ { j } \vartheta _ { k } ( b )$ and $j \succ _ { b } \vartheta _ { k } ( j )$

$$
\mathbf { P 2 . 1 } : \operatorname* { m i n i m i z e } \quad \sum _ { k \in { \mathcal { K } } } \sum _ { j \in { \mathcal { I } } } E _ { j } ^ { j  k , \operatorname { t r a n s } } ( P )\tag{36a}
$$

$$
\begin{array}{c} { \mathrm { s u b j e c t ~ t o } } \quad \underbrace { \beta _ { j } ^ { k } } _ { \begin{array} { l } { \omega \log _ { 2 } \left( 1 + \frac { P _ { j } ^ { k , b } g _ { j } ^ { k , b } } { k ^ { \prime } \in { \mathcal { K } } , k ^ { \prime } \not = k ~ j ^ { \prime } \in { \mathcal { I } } , j ^ { \prime } \not = j } \right)} \end{array}  ^ { { P _ { j } ^ { k , b } g _ { j ^ { \prime } } ^ { k , b } + \sigma ^ { 2 } } } }  \end{array} 
$$

$$
\leq \varphi _ { j } , \forall j \in { \mathcal { T } } _ { k } , \forall k \in K ,\tag{36b}
$$

$$
0 \leq P _ { j } ^ { k , b } \leq P _ { j } ^ { \mathbf { m a x } } , \forall j \in \mathcal { I } _ { k } , \forall k \in \mathcal { K } ,\tag{36c}
$$

The proposed game guarantees to converge to the stable matching since it is implemented identically to the standard deferred acceptance algorithm [39]. The pseudocode of the one-to-one matching game-based sub-band assignment algorithm is shown in Algorithm 1. First, we acquire a set of devices $\mathcal { T } _ { k }$ , a set of sub-bands B, and initialize a set of unmatched devices $\mathcal { I } _ { k } ^ { \mathrm { u n } }$ , a set of prospective sub-bands for each device $B _ { j }$ , a set of requested devices to each sub-band $\mathcal { I } _ { k } ^ { b , \mathrm { r e q } }$ , and a set of rejected devices by each sub-band $\mathcal { I } _ { k } ^ { b , \mathrm { r e j } }$ . Every device builds its own preference list for all possible sub-bands (line 3) and then chooses the best sub-band b (line 7) that can provide the highest transmission rate and sends the request to UAV k in order to get access to that sub-band (line 8). When device $j$ selects sub-band b, the value of $q _ { j b }$ is set to 1, and if not, to 0. After receiving requests from devices, the UAV updates the set of devices that have requested sub-band b (line 11). Then, the UAV constructs the preference list of sub-band b for all requested devices (lines 12–13). After that, the UAV will choose the best device for sub-band b from the list of devices that have requested that sub-band, $\mathcal { I } _ { k } ^ { b , \mathrm { r e q } }$ (line 14), and assign the chosen device to sub-band b (line 15). Then after, the set of rejected devices for sub-band b is updated (line 16), and sub-band b is deleted from the list of prospective sub-bands of its rejected devices (line 17). Finally, the set of unmatched devices is likewise updated based on the sets of rejected users for all sub-bands (line 19). The matching process is conducted iteratively until a stable match is established between both sides (i.e., devices and sub-bands). The process will stop when all devices are assigned to the sub-bands or there are no more sub-bands to send the access request to. Finally, the output of the one-to-one matching, $\vartheta _ { k } ^ { * }$ is mapped to the sub-band assignment vector $\mathbf { \Delta } a _ { k } , \mathrm { i . e . , } \vartheta _ { k } ^ { \ast }  \mathbf { \Delta } a _ { k }$ , (line 22).

Stage 2 (Power Control Problem). Utilizing the output of the proposed one-to-one matching game-based sub-band assignment algorithm that we presented in Algorithm 1, the power control problem can be expressed as P2.1.

Theorem 1: The objective function (36a) of the power control problem P2.1 is a concave function.

Proof. Let us define

$$
L ( P _ { j } ^ { k , b } ) = \frac { 1 } { \omega \log _ { 2 } \left( 1 + \frac { g _ { j } ^ { k , b } } { \underset { k ^ { \prime } \in \mathcal { K } , k ^ { \prime } \ne k } { \sum } \frac { g _ { j } ^ { k ^ { \prime } , b } } { \underset { j ^ { \prime } \in \mathcal { I } , j ^ { \prime } \ne j } { \sum } P _ { j ^ { \prime } } ^ { k ^ { \prime } , b } g _ { j ^ { \prime } } ^ { k , b } + \sigma ^ { 2 } } } \right) , }\tag{37}
$$

where $\pmb { P } _ { j } ^ { k , b } = \{ P _ { j ^ { \prime } } ^ { 1 , b } , P _ { j ^ { \prime } } ^ { 2 , b } , \ldots , P _ { j ^ { \prime } } ^ { K , b } \} , j ^ { \prime } \in \mathcal { I }$ . In accordance with the definition presented in $( 1 2 ) , E _ { j } ^ { k , \mathrm { t r a n s } }$ which is the objective function (36a), is the perspective function of $L ( P _ { j } ^ { k , b } )$ , i.e., $\begin{array} { r } { E _ { j } ^ { j  k , \mathrm { t r a n s } } ( { P } ) = \beta _ { j } ^ { k } P _ { j } ^ { k , b } L ( \frac { { P } _ { j } ^ { k , b } } { P _ { j } k , b } ) } \end{array}$ . Since the perspective function maintains concavity, if we can demonstrate that $L ( P _ { j } ^ { k , b } )$ is concave, then its perspective function $E _ { j } ^ { j \to k , \mathrm { t r a n s } } ( P )$ must also be concave. In order to keep things simple, we will demonstrate that $L ( P _ { j ^ { \prime } } ^ { k , b } )$ is concave for a single variable. The case with multiple variables consists of a concave affine function and a single variable function, hence if we are able to demonstrate that the perspective function is concave in the single variable scenario, then it will also be concave for multiple variables. Let us introduce

$$
M ( P _ { j ^ { \prime } } ^ { k , b } ) = \frac { 1 } { \log _ { 2 } \left( 1 + \frac { 1 } { P _ { j ^ { \prime } } ^ { k ^ { \prime } , b } } \right) } , P _ { j ^ { \prime } } ^ { k ^ { \prime } , b } > 0 ,
$$

as the function of the single variable case of $L ( P _ { j } ^ { k , b } )$ . Then, the first-order derivative of $M ( P _ { j ^ { \prime } } ^ { k , b } )$ w.r.t $P _ { j ^ { \prime } } ^ { k ^ { \prime } , b }$ , will be

$$
\frac { \mathrm { d } M ( P _ { j ^ { \prime } } ^ { k , b } ) } { \mathrm { d } P _ { j ^ { \prime } } ^ { k ^ { \prime } , b } } = \frac { 1 } { \ln 2 P _ { j ^ { \prime } } ^ { k ^ { \prime } , b } ( P _ { j ^ { \prime } } ^ { k ^ { \prime } , b } + 1 ) \log _ { 2 } \left( 1 + \frac { 1 } { P _ { j ^ { \prime } } ^ { k ^ { \prime } , b } } \right) ^ { 2 } . }\tag{38}
$$

From (38), we observe that $\frac { \mathrm { d } M ( P _ { j ^ { \prime } } ^ { k , b } ) } { \mathrm { d } P _ { i ^ { \prime } } ^ { k ^ { \prime } , b } } > 0 .$ . Thus, $M ( P _ { j ^ { \prime } } ^ { k , b } )$ is a non-decreasing function of the transmit power profile P . The second-order derivative is then

$$
\frac { \mathrm { d } ^ { 2 } M ( P _ { j ^ { \prime } } ^ { k , b } ) } { \mathrm { d } P _ { j ^ { \prime } } ^ { ( k ^ { \prime } , b ) 2 } } = \frac { 2 ( P _ { j ^ { \prime } } ^ { k ^ { \prime } , b } + 0 . 5 ) } { 0 . 4 8 \left( ( P _ { j ^ { \prime } } ^ { k ^ { \prime } , b } ) ^ { 2 } + P _ { j ^ { \prime } } ^ { k ^ { \prime } , b } \right) \log _ { 2 } \left( 1 + \frac { 1 } { P _ { j ^ { \prime } } ^ { k ^ { \prime } , b } } \right) ^ { 3 } }
$$

$$
\left[ \frac { 1 } { P _ { j ^ { \prime } } ^ { k ^ { \prime } , b } + 0 . 5 } - \ln { \left( 1 + \frac { 1 } { P _ { j ^ { \prime } } ^ { k ^ { \prime } , b } } \right) } \right] .\tag{39}
$$

From (39), we can conclude that

$$
\frac { 1 } { P _ { j ^ { \prime } } ^ { k ^ { \prime } , b } + 0 . 5 } < \ln { \left( 1 + \frac { 1 } { P _ { j ^ { \prime } } ^ { k ^ { \prime } , b } } \right) }\tag{40}
$$

when $P _ { j ^ { \prime } } ^ { k ^ { \prime } , b } > 0 $ . Therefore, $\frac { \mathrm { d } ^ { 2 } M ( P _ { j ^ { \prime } } ^ { k , b } ) } { \mathrm { d } P _ { i ^ { \prime } } ^ { ( k ^ { \prime } , b ) 2 } } < 0$ , and $M ( P _ { j ^ { \prime } } ^ { k , b } )$ is concave. Additionally, constraint (36b) is concave, which can be shown following the same steps. -

Thus, to make problem P2.1 tractable, we first transform the problem into DC (i.e., difference of two convex functions) form. Following that, we develop a CCP (concave-convex procedure)- based technique to approach its stationary point, which is the optimal solution to the power control problem.

First, the DC form of the constraint (36b) is

$$
\begin{array} { r l } & { \left[ \underbrace { \frac { \beta _ { j } ^ { k } } { \omega \varphi _ { j } } - \log _ { 2 } \left( \sum _ { k ^ { \prime } \in \mathcal { K } _ { j } \in \mathcal { F } } P _ { j } ^ { k , b } g _ { j } ^ { k , b } + \sigma ^ { 2 } \right) } _ { \bar { R } ( P ) } \right. } \\ & { - \left. \left( \underbrace { - \log _ { 2 } \left( \sum _ { k ^ { \prime } \in \mathcal { K } , \bar { F } \neq k ^ { \prime } \in \mathcal { F } , \bar { F } ^ { k ^ { \prime } } } P _ { j } ^ { k ^ { \prime } , b } g _ { j } ^ { k , b } + \sigma ^ { 2 } \right) } _ { U ( P ) } \right) \right] \leq 0 . } \end{array}\tag{41}
$$

Moreover, according to Theorem 1, the objective function (36a) is concave, thus, we can transform the objective function into a DC form, i.e., $0 - \left( - E _ { i } ^ { j \to k , \operatorname { t r a n s } } ( P ) \right)$ . Finally, by approximating the concave parts of both the objective function and constraint in (41) using the first-order Taylor approximation approach, we can convexify the objective function and the constraint. Thus, the following is the approximation function of $U ( P )$ in (41)

$$
\bar { U } \left( P ^ { ( \hat { t } + 1 ) } \right) = U \left( P ^ { ( \hat { t } ) } \right) + \nabla U \left( P ^ { ( \hat { t } ) } \right) \left( P ^ { ( \hat { t } + 1 ) } - P ^ { ( \hat { t } ) } \right)\tag{42}
$$

where the subscript t<sup>ˆ</sup>is the current iteration and

$$
\nabla U \left( P ^ { ( \hat { t } ) } \right) = \frac { - \displaystyle \sum _ { k ^ { \prime } \in K , k ^ { \prime } \neq k } \sum _ { j ^ { \prime } \in \mathcal { J } , j ^ { \prime } \neq j } g _ { j ^ { \prime } } ^ { k , b } } { \ln 2 \left( \log _ { 2 } \bigl ( \displaystyle \sum _ { k ^ { \prime } \in K , k ^ { \prime } \neq k } \sum _ { j ^ { \prime } \in \mathcal { J } , j ^ { \prime } \neq j } P _ { j ^ { \prime } } ^ { k ^ { \prime } , b } g _ { j ^ { \prime } } ^ { k , b } + \sigma ^ { 2 } \bigr ) \right) } .\tag{43}
$$

Consequently, the objective function’s approximation function is defined as

$$
\begin{array} { r l } & { \widehat { E } _ { j } ^ { j  k , \mathrm { t r a n s } } ( { P } ^ { ( \widehat { t } + 1 ) } ) = - E _ { j } ^ { j  k , \mathrm { t r a n s } } ( { P } ^ { ( \widehat { t } + 1 ) } ) } \\ & { - \nabla E _ { j } ^ { j  k , \mathrm { t r a n s } } ( { P } ^ { ( \widehat { t } ) } ) ( { P } ^ { ( \widehat { t } + 1 ) } - { P } ^ { ( \widehat { t } ) } ) } \end{array}\tag{44}
$$

Finally, we can reformulate the power control problem as below

$$
\mathbf { P 2 . 1 1 : m i n i m i z e } \quad - \sum _ { k \in K } \sum _ { j \in \mathcal { I } } \widehat { E } _ { j } ^ { j  k , \mathrm { t r a n s } } ( P )\tag{45a}
$$

$$
\mathrm { s u b j e c t ~ t o } \quad \hat { R } ( \pmb { P } ) - \bar { U } \left( \pmb { P } \right) \leq 0 , \forall j \in \mathcal { T } _ { k } , \forall k \in \mathcal { K } ,\tag{45b}
$$

$$
0 \leq P _ { j } ^ { k , b } \leq P _ { j } ^ { \mathbf { m a x } } , \forall j \in \mathcal { I } _ { k } , \forall k \in \mathcal { K } ,\tag{45c}
$$

```latex
Algorithm 2. CCP-Based Power Control Algorithm
1: Initialization: Set $\hat { t } = 0 , \epsilon _ { 1 } = 1 0 ^ { - 4 }$ , and find initial
feasible solutions $( { P ^ { ( 0 ) } } )$
2: repeat
3: Solve the problem in (45) by using CVXPY toolkit
and find the optimal transmit power profile $P ^ { ( \hat { t } + 1 ) }$
4: Update $\hat { t } = \hat { t } + 1 ;$
5: until $\begin{array} { r l r } & { } & { \parallel \frac { \widehat { E } _ { j } ^ { j  k , \mathrm { t r a n s } } ( P ^ { ( \hat { t } ) } ) - \widehat { E } _ { j } ^ { j  k , \mathrm { t r a n s } } ( P ^ { ( \hat { t } + 1 ) } ) } { \widehat { E } _ { \ast } ^ { j  k , \mathrm { t r a n s } } ( P ^ { ( \hat { t } ) } ) } \parallel \leq \epsilon _ { 1 } ; } \end{array}$
6: Then, set $P ^ { ( \hat { t } + 1 ) }$ as the desired solutions.
```

where the objective function (45a) and constraint (45b) are convex, and the constraint (45c) is linear. Thus, problem P2.11 is a convex problem. Therefore, we can solve it by using convex optimization techniques. The summary of the CCP-based power control algorithm is presented in Algorithm 2.

## C. UAV Deployment

For a given $\{ \beta , P , a , w , v , z \}$ , we can formulate the UAV deployment problem as

$$
\mathbf { P 3 } : \operatorname* { m i m i m i z e } _ { o } \quad \mathbf { Q } ( o )\tag{46a}
$$

$$
{ \mathrm { s u b j e c t ~ t o ~ } } ( 3 1 { \mathrm { c } } ) , ( 3 1 { \mathrm { m } } ) , ( 3 1 { \mathrm { n } } ) ,\tag{46b}
$$

$$
\begin{array} { r } { \mathrm { w h e r e } \qquad \mathbf { Q } ( o ) = \sum _ { j \in \mathcal { I } _ { k } } \sum _ { k \in \mathcal { K } } E _ { j } ^ { j \to k , \mathrm { t r a n s } } + \sum _ { k \in \mathcal { K } } } \\ { \Biggl ( \sum _ { k ^ { \prime } \in \mathcal { K } , k ^ { \prime } \not = k } E ^ { k \to k ^ { \prime } , \mathrm { t r a n s } } + \sum _ { s \in \mathcal { S } } E ^ { k \to s , \mathrm { t r a n s } } \Biggr ) . \qquad \mathrm { H o w e v e r } , } \end{array}
$$

problem P3 is non-convex due to the non-convex objective function and constraint (31c). Thus, we use a successive convex approximation (SCA) approach to address the formulated UAV deployment problem and to achieve a locally optimal solution. SCA iteratively approximates every non-convex function in the optimization problem with a convex function. Then, the approximated convex problem is solved via standard optimization techniques.

We first introduce sets of auxiliary variables $\lambda _ { j , k } =$ $\{ \lambda _ { j , k } , \forall j \in \mathcal { T } _ { k } , \forall k \in \mathcal { K } \} , \quad \lambda _ { k , k ^ { \prime } } = \{ \lambda _ { k , k ^ { \prime } } , \forall k , k ^ { \prime } \in \mathcal { K } \}$ , and $\lambda _ { k , s } = \{ \lambda _ { k , s } , \forall k \in K , \forall s \in S \}$ in order to replace non-linear inequality constraint (31c) with four inequality constraints as follows

$$
\frac { \beta _ { j } ^ { k } } { R _ { j } ^ { k } } \leq \lambda _ { j , k } , \forall j \in \mathcal { T } _ { k } , \forall k \in \mathcal { K } ,\tag{47}
$$

$$
\frac { \beta ^ { k  k ^ { \prime } } } { R ^ { k  k ^ { \prime } } } \leq \lambda _ { k , k ^ { \prime } } \forall k , k ^ { \prime } \in \mathcal { K } ,\tag{48}
$$

$$
\frac { \beta ^ { k  s } } { R ^ { k  s } } \leq \lambda _ { k , s } , \forall k \in \mathcal { K } , \forall s \in \mathcal { S } ,\tag{49}
$$

$$
\lambda _ { j , k } + \lambda _ { k , k ^ { \prime } } + \lambda _ { k , s } \leq \varphi _ { j } , \forall j \in \mathcal { I } _ { k } , \forall k , k ^ { \prime } \in \mathcal { K } , \forall s \in \mathcal { S } .\tag{50}
$$

Then, we can reformulate problem P3 as shown in P3.1. (51a)– (51d) shown at the bottom of the this page.

Due to the logarithmic terms in $R _ { j } ^ { k } ( \mathrm { i } . \mathrm { e } . , N _ { 1 } ( o )$ and $N _ { 2 } ( o ) )$ $R ^ { k \to k ^ { \prime } }$ , and $R ^ { k  s }$ , problem P3.1 is non-convex. Thus, as shown in (52) shown at the bottom of the next page, we first convexify $N _ { 1 } ( o )$ by introducing its convex lower bound function, $\hat { N } _ { 1 } ( o )$ based on the first-order Taylor approximation at the given location of UAV k at tth iteration, $o _ { k } ( t )$ . In the same way, $N _ { 2 } ( o ) )$ $R ^ { k \to k ^ { \prime } }$ , and $R ^ { k  s }$ can be convexified as shown in (53)–(58) shown at the bottom of the next page, respectively.

Finally, we can approximate the non-convex problem P3.1 as a convex problem as the following

$$
\mathrm { \bf ~ P 3 . 2 : \operatorname* { m i n i m i z e } _ { { o , \lambda , \ddot { n } , \hat { n } , \tilde { n } } } } \hat { \mathrm { \bf ~ Q } } ( o , \lambda , \ddot { n } , \hat { n } , \tilde { n } )\tag{59a}
$$

$$
\begin{array} { r } { \mathrm { s u b j e c t ~ t o } \quad \hat { N } _ { 1 } ( o ) - \hat { N } _ { 2 } ( o ) \leq 0 , \forall j \in \mathcal { I } _ { k } , \forall k \in \mathcal { K } , } \end{array}\tag{59b}
$$

$$
\frac { \beta ^ { k  k ^ { \prime } } } { \ddot { R } ^ { k  k ^ { \prime } } } \leq \lambda _ { k , k ^ { \prime } } , \forall k , k ^ { \prime } \in \mathcal { K } ,\tag{59c}
$$

$$
\frac { \beta ^ { k  s } } { \ddot { R } ^ { k  s } } \leq \lambda _ { k , s } , \forall k \in { \mathcal { K } } , s \in { \mathcal { S } } ,\tag{59d}
$$

$$
\begin{array} { r l } & { \underbrace { \mathbf { P 3 . 1 \cdot m i n i m i n i z e } } _ { \mathrm { s u b j e c t ~ t o ~ } } \displaystyle \sum _ { j \in \mathcal { N } _ { k } \times k \in \mathcal { K } } E _ { j } ^ { j - k , n a s } + \displaystyle \sum _ { k \in \mathcal { K } } \left( \displaystyle \sum _ { k \in \mathcal { K } , k ^ { \prime } \neq k } E ^ { k - \mathcal { H } , \operatorname* { m a x } } + \displaystyle \sum _ { s \in \mathcal { S } } E ^ { k - s , \operatorname* { m a x } } \right) } \\ & { \qquad \mathrm { s u b j e c t ~ t o ~ } \displaystyle \underbrace { \frac { \beta _ { j } ^ { k } } { \omega \lambda _ { j , k } } - \log _ { 2 } \left( \displaystyle \sum _ { k \in \mathcal { K } / \neq \mathcal { T } } \displaystyle \sum _ { ( d _ { j } ^ { k } ) ^ { 2 } \in \mathcal { N } _ { i } \in \mathcal { I } } p _ { i } ^ { k } + \sigma ^ { 2 } \right) } _ { \displaystyle N _ { 1 } ( a ) } - } \\ & { \qquad \left( \underbrace { - \log _ { 2 } \left( \displaystyle \sum _ { k \in \mathcal { K } , k ^ { \prime } \neq k } \displaystyle \sum _ { j \in \mathcal { I } , j ^ { \prime } \in \mathcal { I } } \displaystyle \sum _ { ( d _ { k } ^ { k } ) ^ { 2 } } \displaystyle \frac { P _ { j } ^ { k ^ { \prime } , \delta } g _ { 0 } } { \sigma ^ { \mathrm { ( k ) } } } + \sigma ^ { 2 } \right) } _ { \displaystyle N _ { 2 } ( a ) } \right) \leq 0 , \forall j \in \mathcal { I } _ { k } , \forall k \in \mathcal { K } , } \end{array}\tag{51a}
$$

(51b)

(48), and (49),

(51c)

(31m), (31n), (50),

(51d)

## Algorithm 3: UAV Deployment Algorithm.

1: Initialization: Set $t = 0 , \epsilon _ { 2 } = 1 0 ^ { - 4 }$ , and find initial feasible solutions $( o ^ { ( 0 ) } , \lambda ^ { ( 0 ) } , \ddot { n } ^ { ( 0 ) } , \hat { n } ^ { ( 0 ) } , \tilde { n } ^ { ( 0 ) } )$ ;

2: repeat

3: Solve the problem in (59) by using CVXPY toolkit and find the optimal location of UAVs and auxiliary variables, $o ^ { ( t + 1 ) } , \lambda ^ { ( t + 1 ) } , \ddot { n } ^ { ( t + 1 ) } , \hat { n } ^ { ( t + 1 ) }$ , and $\tilde { n } ^ { ( t + \tilde { 1 } ) }$   
4: Update $t = t + 1 ;$

5: until $\begin{array} { r } { \parallel \frac { \hat { \mathbf { Q } } ^ { ( t ) } - \hat { \mathbf { Q } } ^ { ( t + 1 ) } } { \hat { \mathbf { Q } } ^ { ( t ) } } \parallel \leq \epsilon _ { 2 } ; } \end{array}$

6: Then, set $o ^ { ( { \dot { t } } + 1 ) } , \lambda ^ { ( t + 1 ) } , { \ddot { n } } ^ { ( t + 1 ) } , { \hat { n } } ^ { ( t + 1 ) }$ , and $\tilde { n } ^ { ( t + 1 ) }$ as the desired solution.

(30m), (30n), (50), (54), (56), (58),

(59e)

where

$$
\begin{array} { r } { \sum _ { k \in \mathcal { K } } \Bigg ( \sum _ { k ^ { \prime } \in \mathcal { K } , k ^ { \prime } \neq k } \frac { P ^ { k  k ^ { \prime } } \beta ^ { k  k ^ { \prime } } } { \ddot { R } ^ { k  k ^ { \prime } } } + \sum _ { s \in \mathcal { S } } \frac { P ^ { k  s } \beta ^ { k  s } } { \ddot { R } ^ { k  s } } \Bigg ) . } \end{array}\tag{As}
$$

problem P3.2 is a convex problem, we can solve it using convex

optimization techniques. The summary of the SCA-based optimal UAVs deployment algorithm is presented in Algorithm 3.

## D. UAV Task Offloading Decision

For a given $\{ \beta , o , P , a \}$ , we can formulate the UAV task offloading decision problem as

$$
\mathbf { P 4 } : \operatorname* { m i n i m i z e } _ { \boldsymbol { w } , \boldsymbol { v } , \boldsymbol { z } } \quad \mathbf { Q } ( \boldsymbol { w } , \boldsymbol { v } , \boldsymbol { z } )\tag{60a}
$$

$$
{ \mathrm { s u b j e c t ~ t o ~ ( 3 1 c ) , ~ ( 3 1 h ) , ~ ( 3 1 j ) - ( 3 1 1 ) , } }\tag{60b}
$$

Problem P4 is non-convex and is a combinatorial problem. As a result, we propose to use the BSUM method to address problem P4 [40]. BSUM is a method for addressing non-convex and non-smooth optimization problems by splitting the problem into manageable subproblems. Using the BSUM approach, the decision variables w, v, z are updated consecutively in order to minimize the upper bound of the objective function. Additionally, BSUM can ensure convergence to the stationary points of the objective function in (60a). To use the BSUM technique, we first relax the binary constraints (31j)–(31l) and replace them with continuous ones. Then, we can introduce the feasible sets

$$
\begin{array} { l } { { \displaystyle \hat { N } _ { 1 } ( \sigma ) = ( \frac { \beta _ { j } ^ { k } } { \omega \lambda _ { j , k } } - \log _ { 2 } ( \sum _ { k \in K } \sum _ { j \in \mathcal { T } } \frac { P _ { j } ^ { k , b } g _ { 0 } } { ( h _ { k } ^ { 2 } + \parallel \omega _ { k } ( t ) - \tilde { c } _ { j } ) ( 2 ) e ^ { \tilde { b } _ { 0 } ( t ) ( h _ { k } ^ { 2 } + \lvert ( \omega _ { k } ( t ) - \tilde { c } _ { j } \rvert ^ { 2 } ) \rvert ^ { \prime } ) } + \sigma ^ { 2 } ) ) + ( \mathbb { 1 } \ \ \mathrm { o } _ { k } - \tilde { c } _ { j }  ^ { 2 } } } } \\   \displaystyle - \mathbb { I } \ \big \lVert \omega _ { k } ( t ) - \tilde { c } _ { j } \  ^ { 2 } ) ^ { \underline { { K } } \sum _ { j \in \mathcal { T } } } \frac { P _ { j } ^ { k , b } g _ { 0 } [ \frac { 1 } { 2 } ( h _ { k } ^ { 2 } + \lvert ( \omega _ { k } ( t ) - \tilde { c } _ { j } \rvert ^ { 2 } ) ^ { 1 / 2 } e ^ { \tilde { b } _ { 0 } ( t ) ( h _ { k } ^ { 2 } + \lvert ( \omega _ { k } ( t ) - \tilde { c } _ { j } \rvert ^ { 2 } ) \rvert ^ { \prime } ) } i _ { \tilde { a } } ( t ) + e ^ { \tilde { \iota } _ { 0 } ( t ) ( h _ { k } ^ { 2 } + \lvert ( \omega _ { k } ( t ) - \tilde { c } _ { j } \rvert ^ { 2 } ) \rvert ^ { \prime } ) } ] ^ { \underline { { K } } } }  ( ( h _ { k } ^ { 2 } + \lvert ( \omega _ { k } ( t ) - \tilde { c } _ { j } \rvert ^ { 2 } ) \rvert ^ { \alpha _ { k } } + \lvert ( \omega _ { k } ( t ) - \tilde { c } _ { j } \rvert ^ { 2 } ) \rvert ^ { \alpha _ { j } } ) ^   \end{array}\tag{52}
$$

$$
\hat { N } _ { 2 } ( o ) = - \log _ { 2 } \left( \sum _ { k ^ { \prime } \in \mathcal { K } , k ^ { \prime } \neq k } \sum _ { j ^ { \prime } \in \mathcal { I } , j ^ { \prime } \neq j } \frac { P _ { j ^ { \prime } } ^ { k ^ { \prime } , b } g _ { 0 } } { ( h _ { k } ^ { 2 } + \ddot { n } _ { k } ) e ^ { i _ { b } ( f ) ( h _ { k } ^ { 2 } + \ddot { n } _ { k } ) ^ { 1 / 2 } } } + \sigma ^ { 2 } \right) ,\tag{53}
$$

where

$$
\ddot { n } _ { k } \le \parallel o _ { k } ( t ) - \ddot { c } _ { j ^ { \prime } } \parallel ^ { 2 } + 2 ( o _ { k } ( t ) - \ddot { c } _ { j ^ { \prime } } ) ^ { T } ( o _ { k } - o _ { k } ( t ) ) , \forall k ^ { \prime } \in K , k ^ { \prime } \neq k , \forall j ^ { \prime } \in \mathcal { T } _ { k } , j ^ { \prime } \neq j ,\tag{54}
$$

$$
\ddot { R } ^ { k  k ^ { \prime } } = B _ { \mathrm { m m } } ^ { k  k ^ { \prime } } \mathrm { l o g } _ { 2 } ( 1 + \frac { P ^ { k  k ^ { \prime } } g _ { k } ^ { \mathrm { I x } } g _ { k ^ { \prime } } ^ { \mathrm { r x } } L _ { r } } { t _ { n } H B _ { \mathrm { m m } } ^ { k  k ^ { \prime } } } ( \frac { c ^ { 2 } } { 1 6 \pi ^ { 2 } \bigg ( ( h _ { k } - h _ { k ^ { \prime } } ) ^ { 2 } + \hat { n } _ { k } \bigg ) ( f _ { c } ^ { \mathrm { m m } } ) ^ { 2 } } ) ) , \forall k , k ^ { \prime } \in \mathcal { K } ,\tag{55}
$$

where

$$
\hat { n } _ { k } \ge \parallel o _ { k } ( t ) - o _ { k ^ { \prime } } ( t ) \parallel ^ { 2 } + 2 ( o _ { k } ( t ) - o _ { k ^ { \prime } } ( t ) ) ^ { T } ( o _ { k } - o _ { k ^ { \prime } } )\tag{56}
$$

$$
\ddot { R } ^ { k  s } = B _ { \mathrm { m m } } ^ { k  s } \log _ { 2 } ( 1 + \frac { P ^ { k  s } g _ { k } ^ { \mathrm { I x } } g _ { s } ^ { \mathrm { r x } } L _ { r } } { t _ { n } H B _ { \mathrm { m m } } ^ { k  s } } ( \frac { c ^ { 2 } } { 1 6 \pi ^ { 2 } \bigg ( ( h _ { k } - h _ { s } ) ^ { 2 } + \tilde { n } _ { k } \bigg ) ( f _ { c } ^ { \mathrm { m m } } ) ^ { 2 } } ) ) , \forall k \in K , \forall s \in \mathcal { S } ,\tag{57}
$$

where

$$
\begin{array} { r } { \tilde { n } _ { k } \geq \parallel \pmb { o } _ { k } ( t ) - \pmb { o } _ { s } \parallel ^ { 2 } + 2 ( \pmb { o } _ { k } ( t ) - \pmb { o } _ { s } ) ^ { T } ( \pmb { o } _ { k } - \pmb { o } _ { k } ( t ) ) , \forall k \in \mathcal { K } , \forall s \in \mathcal { S } , } \end{array}\tag{58}
$$

Algorithm 4: BSUM-Based UAV Task Offloading Decision   
Algorithm.   
1: Initialization: Set $\ddot { t } = 0 , \epsilon _ { 3 } = 1 0 ^ { - 4 }$ , and initial   
solutions $( \pmb { w } ^ { ( 0 ) } , \pmb { v } ^ { ( 0 ) } , \pmb { z } ^ { ( 0 ) } ) ;$   
2: repeat   
3: Choose index set M;   
4: Let $\begin{array} { r } { \pmb { w } _ { m } ^ { ( i + 1 ) } \in \operatorname * { a r g m i n } \mathbf { Q } _ { m } ( \pmb { w } _ { m } ; \pmb { w } ^ { ( i ) } , \pmb { v } ^ { ( i ) } , z ^ { ( t ) } ) ; } \end{array}$   
w<sub>m</sub>   
5: Set ${ \pmb w } _ { n } ^ { ( i + 1 ) } = { \pmb w } _ { n } ^ { i } , \forall n \notin \mathcal { M } ;$   
6: Find ${ \pmb v } _ { m } ^ { ( i + 1 ) }$ , and $z _ { m } ^ { ( \ddot { t } + 1 ) }$ by addressing (63) and (64);   
7: Update $\ddot { t } = \ddot { t } + 1 ;$   
8: until $\parallel \frac { \mathbf { Q } _ { m } ^ { ( \ddot { t } ) } - \mathbf { Q } _ { m } ^ { ( \ddot { t } + 1 ) } } { \mathbf { Q } _ { m } ^ { ( \ddot { t } ) } } \parallel \leq \epsilon _ { 3 }$   
9: Then, set $( \pmb { w } _ { m } ^ { ( \ddot { t } + 1 ) } , \pmb { v } _ { m } ^ { ( \ddot { t } + 1 ) } , \pmb { z } _ { m } ^ { ( \ddot { t } + 1 ) } )$ as the desired   
solution.

of w, v, and z as the following

W  w : ≤ ϕ<sub>j</sub> , w<sup>k</sup><sub>j</sub> +  v<sup>k→k</sup><sub>j</sub> + <sup></sup> j   
k<sup></sup>∈K,k<sup></sup><sup>=</sup>k s∈S   
= 1, w<sup>k</sup><sub>j</sub> ∈ [0, 1], ∀j ∈ J<sub>k</sub>, ∀k ∈ K   
V  v : l<sup>k,Remote</sup> j +  <sup></sup>+   
k<sup></sup>∈K,k<sup></sup><sup>=</sup>k s∈S   
，   
Z  z : l<sup>k,Remote</sup><sub>j</sub> ≤ ϕ<sub>j</sub> , w<sup>k</sup><sub>j</sub> j +  v<sup>k→k</sup><sub>j</sub> +<sup></sup> = 1,   
k<sup></sup>∈K,k<sup></sup><sup>=</sup>k s∈S

Finally, we establish the proximal upper bound function of the objective function (60a) for each iteration $\ddot { t } , \forall m \in \mathcal { M }$ , where M is the index set, as shown below

$$
{ \bf Q } _ { m } ( { \pmb w } _ { m } ; { \pmb w } ^ { \dag } , { \pmb v } ^ { \dag } z ^ { \dag } ) = { \bf Q } ( { \pmb w } _ { m } ; \widehat { { \pmb w } } , \widehat { { \pmb v } } , \widehat { { \pmb z } } ) + \frac { \mu _ { m } } { 2 } \parallel ( { \pmb w } _ { m } - \widehat { { \pmb w } } ) \parallel ^ { 2 }\tag{61}
$$

where the quadratic penalty term helps to convexify the proximal upper-bound function, and $\mu _ { m }$ is a positive penalty parameter that can be used for the other vectors of the variables v, and $z ,$ respectively. Additionally, the proximal upper-bound function (61) contains distinct minimizer vectors w, v, and z with respect to w, v, and z at each iteration $\ddot { t } ,$ which are taken into account as the solution of the preceding iteration $( \ddot { t } - 1 )$ . The solution at iteration (t<sup>¨</sup>+ 1) is then obtained by solving the subproblems

$$
{ \pmb w } _ { m } ^ { ( \ddot { t } + 1 ) } \in \underset { { \pmb w } _ { m } } { \mathrm { a r g m i n } } ~ { \bf Q } _ { m } \bigg ( { \pmb w } _ { m } ; { \pmb w } ^ { ( \ddot { t } ) } , { \pmb v } ^ { ( \ddot { t } ) } , z ^ { ( \ddot { t } ) } \bigg ) ,\tag{62}
$$

Algorithm 5: Joint Task Offloading, Sub-Band Assignment,   
Power Control, and UAV Deployment Algorithm.   
1: Initialization: Set $\tilde { t } = 0 , \epsilon _ { 4 } = 1 0 ^ { - 4 } .$ , and initial   
solutions $( \beta ^ { ( 0 ) } , { \pmb a } ^ { ( 0 ) } , { \pmb P } ^ { ( 0 ) } , { \pmb o } ^ { ( 0 ) } , { \pmb w } ^ { ( 0 ) } { \pmb v } ^ { ( 0 ) } , z ^ { ( 0 ) } ) ;$   
2: repeat   
3: Solve device task offloading problem P1 at the given   
$( { \pmb a } ^ { ( \tilde { t } ) } , { \pmb P } ^ { ( \tilde { t } ) } , { \pmb o } ^ { ( \tilde { t } ) } , { \pmb w } ^ { ( \tilde { t } ) } { \pmb v } ^ { ( \tilde { t } ) } , z ^ { ( \tilde { t } ) } )$ by using CVXPY   
toolkit;   
4: Solve sub-band assignment and transmit power   
control problem at the given   
$( \beta ^ { ( \tilde { t } + 1 ) } , \sigma ^ { ( \tilde { t } ) } , w ^ { ( \tilde { t } ) } v ^ { ( \tilde { t } ) } , \bar { z } ^ { ( \tilde { t } ) } )$ by using Algorithms 5   
and 2;   
5: Solve UAV deployment problem at the given   
$( \beta ^ { ( \tilde { t } + 1 ) } , \pmb { a } ^ { ( \tilde { t } + \tilde { 1 ) } } , \hat { P } ^ { ( \tilde { t } + 1 ) } , \pmb { w } ^ { ( \tilde { t } ) } \pmb { v } ^ { ( \tilde { t } ) } , \pmb { z } ^ { ( \tilde { t } ) } )$ using   
Algorithm 3;   
6: Solve UAV task offloading decision problem at the   
given $( \beta ^ { ( \tilde { t } + 1 ) } , a ^ { ( \tilde { t } + 1 ) } , P ^ { ( \tilde { \tilde { t } } + 1 ) } , o ^ { ( \tilde { t } + 1 ) } )$ by using   
Algorithm 4;   
7: Update $\tilde { t } = \tilde { t } + 1 ;$   
8: until $\lVert \frac { \mathbf { Q } ^ { ( \tilde { t } ) } - \mathbf { Q } ^ { ( \tilde { t } + 1 ) } } { \mathbf { Q } ^ { ( \tilde { t } ) } } \rVert \leq \epsilon _ { 4 }$   
9: Set $( \beta ^ { ( \tilde { t } + 1 ) } , \dot { \pmb { a } } ^ { ( \tilde { t } + 1 ) } , \pmb { P } ^ { ( \tilde { t } + 1 ) } , \pmb { o } ^ { ( \tilde { t } + 1 ) } , \pmb { w } ^ { ( \tilde { t } + 1 ) } , \pmb { v } ^ { ( \tilde { t } + 1 ) } , \pmb { v } ^ { ( \tilde { t } + 1 ) } ,$   
$z ^ { ( \tilde { t } + \mathrm { 1 } ) } )$ as the desired solution.

$$
\begin{array} { r l } & { \pmb { v } _ { m } ^ { ( \tilde { t } + 1 ) } \in \underset { \pmb { v } _ { m } } { \mathrm { a r g m i n } } ~ \mathbf { Q } _ { m } \bigg ( \pmb { v } _ { m } ; \pmb { v } ^ { ( \tilde { t } ) } , \pmb { w } ^ { ( \tilde { t } + 1 ) } , \pmb { z } ^ { ( \tilde { t } ) } \bigg ) , } \\ & { z _ { m } ^ { ( \tilde { t } + 1 ) } \in \underset { \pmb { z } _ { m } } { \mathrm { a r g m i n } } ~ \mathbf { Q } _ { m } \bigg ( z _ { m } ; z ^ { ( \tilde { t } ) } , \pmb { w } ^ { ( \tilde { t } + 1 ) } , \pmb { v } ^ { ( \tilde { t } + 1 ) } \bigg ) . } \end{array}\tag{63}
$$

(64)

Subproblems (62), (63), and (64) can be solved by using convex optimization techniques. A summary of our proposed BSUMbased UAVs tasks offloading decision algorithm is presented in Algorithm 4.

## E. Complexity of Joint Task Offloading, Sub-Band Assignment, Power Control, and UAV Deployment Algorithm

Our proposed joint task offloading, sub-band assignment, power control, and UAV deployment algorithm is summarized in Algorithm 5. The algorithm follows an alternating optimization paradigm that calls for resolving subproblems in (32), (33), (46), and (60) repeatedly prior to convergence. At each iteration, the complexity of the device task offloading decision is $\mathcal { O } ( J _ { k } K )$ Then, the complexity of achieving the stable matching in a one-to-one matching game-based sub-channel assignment algorithm is $\mathcal { O } ( J _ { k } B )$ . The computational complexity of the proposed CCP-based power control algorithm is $\mathcal { O } ( ( J _ { k } K ) ^ { 3 } ( 2 J _ { k } K ) )$ [41]. The complexity of the SCA-based UAV deployment algorithm in Algorithm 3 is $\mathcal { O } ( ( K ) ^ { 3 . 5 } ) [ 4 2 ]$ . The complexity of the BSUMbased algorithm to solve the UAV task offloading decision problem in (60) is $\mathcal { O } ( ( K S + K ^ { 2 } ) ^ { 3 . 5 } )$ . Therefore, at each iteration, the complexity of the proposed joint task offloading, sub-band assignment, power control, and UAV deployment algorithm presented in Algorithm 5 is $\mathcal { O } ( J _ { k } K + \bar { J _ { k } B _ { + } } ( J _ { k } K ) ^ { 3 } ( 2 J _ { k } \bar { K ) } +$ $( K S + K ^ { 2 } ) ^ { \sqrt { 3 } . 5 } )$

TABLE I  
SIMULATION PARAMETERS
<table><tr><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Value</td><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Value</td></tr><tr><td rowspan=1 colspan=1> $\overline { { B } }$ </td><td rowspan=1 colspan=1>25</td><td rowspan=1 colspan=1>4j</td><td rowspan=1 colspan=1>500 ms</td></tr><tr><td rowspan=1 colspan=1> $g _ { 0 }$ </td><td rowspan=1 colspan=1>-20 dB</td><td rowspan=1 colspan=1> $\frac { \cdot \cdot \cdot } { P _ { i } ^ { \bf m a x } }$ </td><td rowspan=1 colspan=1>23 dBm</td></tr><tr><td rowspan=1 colspan=1> $\overline { { \sigma ^ { 2 } } }$ </td><td rowspan=1 colspan=1>-174 dBm</td><td rowspan=1 colspan=1> $\underline { f _ { j } }$ </td><td rowspan=1 colspan=1>0.01 MHz</td></tr><tr><td rowspan=1 colspan=1> $\kappa _ { j } , \kappa$ </td><td rowspan=1 colspan=1>1 × 10−10</td><td rowspan=1 colspan=1> $\omega$ </td><td rowspan=1 colspan=1>5 × 102 Hz</td></tr><tr><td rowspan=1 colspan=1> $i _ { b } ( f )$ </td><td rowspan=1 colspan=1>0.005 [9]</td><td rowspan=1 colspan=1> $\overline { { B ^ { k \to k ^ { \prime } } } }$ </td><td rowspan=1 colspan=1>1.7 MHz</td></tr><tr><td rowspan=1 colspan=1> $\overline { { P ^ { k \to k ^ { \prime } } } }$ </td><td rowspan=1 colspan=1>30 dBm</td><td rowspan=1 colspan=1> $g _ { k } ^ { \mathrm { t x } } , g _ { k ^ { \prime } } ^ { \mathrm { r x } }$ </td><td rowspan=1 colspan=1>41 dB</td></tr><tr><td rowspan=1 colspan=1> $\overline { { L _ { r } } }$ </td><td rowspan=1 colspan=1>-23 dB</td><td rowspan=1 colspan=1>H</td><td rowspan=1 colspan=1>300 K</td></tr><tr><td rowspan=1 colspan=1> $\overline { { F _ { k } ^ { \mathbf { m a x } } } }$ </td><td rowspan=1 colspan=1>3.5MHz</td><td rowspan=1 colspan=1> $\overrightarrow { P ^ { k  k ^ { \prime } } }$ </td><td rowspan=1 colspan=1>30 dBm</td></tr><tr><td rowspan=1 colspan=1> $\overline { { B ^ { k \to k ^ { \prime } } } }$ </td><td rowspan=1 colspan=1>1.7 MHz</td><td rowspan=1 colspan=1> $\overline { { B _ { \mathrm { m m } } ^ { k \to s } } }$ </td><td rowspan=1 colspan=1>1.8MHz</td></tr><tr><td rowspan=1 colspan=1> $\overline { { f _ { c } ^ { \mathrm { m m } } } }$ </td><td rowspan=1 colspan=1>28 GHz</td><td rowspan=1 colspan=1> $\overline { { P ^ { k \to s } } }$ </td><td rowspan=1 colspan=1>30 dBm</td></tr></table>

## VI. SIMULATION RESULTS

## A. Evaluation Methodology

To evaluate the proposed solution, we consider wireless devices distributed within an area of 600 m × 600 m. To provide computing services to the devices, 4 MEC-enabled UAVs hover at an altitude of 50 m. Additionally, 2 LEO satellites at an altitude of [780, 800] km are taken into consideration to execute the devices’ tasks that the UAVs cannot handle; their locations are assumed to be unchanged during the simulation. The data size of the task, $A _ { j } ,$ is selected from a uniform distribution on [0.1, 0.5] Mbits. Furthermore, the required CPU cycles to compute a bit of data, $\alpha _ { j } ,$ is also selected from a uniform distribution on [10, 50] Cycles. The rest of the simulation parameters are shown in Table I. We use Python programming language to conduct simulation, and all of the proposed algorithms are executed on the PC with Intel(R) Core(TM) i5-8500 CPU @3.00GHz 3.00 GHz, 32.0 GB RAM, and NVIDIA GeForce GTX 1660 Ti. As a basis for comparison, we use two baseline schemes proposed in the recent literature [12] and [13], namely: 1) All local computing scheme where devices compute their tasks locally, and 2) No UAVs collaboration scheme in which the computation capacity of the UAV is not sufficient to execute the offloaded tasks of its associated devices, the UAV directly transferred its devices’ tasks to LEO satellites using mmWave backhaul links without checking its neighboring UAVs which have sufficient computation to execute its computation tasks. The results shown in this work are the averages of 100 simulations.

## B. Energy Consumption Analysis

Fig. 2 shows the energy consumption as a function of the number of devices in the system, obtained using the proposed algorithm with two state-of-the-art schemes in the literature. The figure demonstrates that compared to other schemes, the total energy consumption at UAVs and devices to accomplish the execution of devices’ computation tasks under our proposed scheme is the lowest in every network size. The figure also shows that as the network size increases, the performance gap between the proposed algorithm and two state-of-the-art schemes widens. As a result, we conclude that the proposed algorithm is also appropriate for large-scale networks. Finally, we see how crucial collaboration among UAVs is to the integrated SAG networks by analyzing the energy consumption under the No UAVs collaboration scheme [13], [43] in the figure. In contrast to the proposed algorithm, the No UAVs collaboration scheme results in higher energy consumption since satellites are farther away from the UAV than its neighboring UAVs, which results in higher transmission energy (i.e., UAV-to-satellite transmission energy) than the UAV-to-UAV transmission energy.

![](images/1ffcd31be85ad17ea219d0253403e936a2ebb7fc2c69ea5f2511849d2e41d772.jpg)  
Fig. 2. Energy consumption versus number of devices for proposed, local computing only and without UAVs collaboration.

In order to evaluate the importance of different decision variables in minimizing the energy consumption, in what follows we consider the following variants of the proposed solution:

\- Centered UAVs (C-UAVs): Each UAV is deployed at the center of its associated devices, i.e., at the center of each cluster, which we established via the K-means algorithm. At the same time, sub-band assignment, power control, and UAV task offloading problems are solved via the proposed Algorithms 1, 2, and 4.

\- All tasks offloading (ATO): In this variant, devices offload all of their computation tasks to their associated UAVs to perform remote computing. Sub-band assignment, power control, UAV deployment, and UAV task offloading problems are solved via the proposed Algorithms 1, 2, 3, and 4.

\- Fixed tasks offloading (FTO): Each device offloads $\beta _ { j } ^ { k } =$ $0 . 5 \alpha _ { j }$ to its associated UAV. At the same time, sub-band assignment, power control, UAV deployment, and UAV task offloading problems are solved via the proposed Algorithms 1, 2, 3, and 4.

Random sub-band assignment (RSA): The available subbands in each UAV are randomly assigned to its associated devices, which offload their computation tasks to the UAV to perform remote computing. Device task offloading, power control, UAV deployment, and UAV task offloading problems are solved via Algorithms 2, 3, and 4.

\- Fixed power Allocation (FPA): Each device uses 50% of its maximum available power (i.e., $P _ { j } ^ { k , b } = 0 . 5 P _ { j } ^ { \bf n a x } )$ in order to offload its computation task to UAVs to perform remote computing, while Algorithms 1, 3, and 4 are used to solve device task offloading, UAV deployment, and UAV task offloading problems.

![](images/10fecd8432ccc088bb4126fada5eedef7ceeca6940bde6d203dff104eab977a5.jpg)

Fig. 3. Energy consumption as a function of the number of devices for variants of the proposed scheme.  
![](images/4f0b40e760261b3a4353702422c52586c22fea47a0210e5677c59e792075d2a6.jpg)  
Fig. 4. Energy consumption as a function of the number of UAVs for $J =$ 20, 40, 60 and 80.

Furthermore, to evaluate the optimality gap of the proposed algorithm, we compare the performance of the proposed solution with the Optimal scheme, where the sub-band assignment problem is solved by using the exhaustive search scheme, which can achieve the optimal solution. In contrast, the device task offloading, power control, UAV deployment, and UAV task offloading problems are solved via Algorithms 2, 3, and 4.

Fig. 3 shows the energy consumption as a function of the number of devices in the network. The figure shows that the energy consumption under the ATO and FTO variants is significantly higher than under other variants of the proposed scheme. These results show that the most important optimization variable for minimizing energy consumption is the amount of data to be offloaded for computation. Additionally, compared to the C-UAVs and FPA variants, the energy consumption under the RSA variant is significantly higher than that of the proposed algorithm. As a result, we may conclude that compared to the deployment of UAVs and power control, sub-band assignment (i.e., a) has a greater impact on energy consumption. In addition, as the number of devices in the network grows, the performance gap between our proposed solution and its variants which implies that optimization in all variables becomes increasingly important as the system size increases. Finally, the figure shows that the energy consumption under the proposed solution is nearly the same as that of the Optimal scheme (i.e., the lower optimality gap).

Fig. 4 shows the energy consumption as a function of the number of UAVs in the network. The figure shows that when deploying only 2 UAVs in the network, energy consumption is significantly higher than when there are 4, 6, and 8 UAVs in the network for all device counts, i.e., J = 20, 40, 60, and 80. However, it is interesting that the energy consumption under 4 UAVs, 6 UAVs, and 8 UAVs is nearly the same. Therefore, for the considered coverage area and device counts, deploying 6 UAVs and 8 UAVs will not give any benefit in terms of energy reduction, but will increase the hardware cost. In addition, when hovering energy for UAVs is taken into account, deploying 6 and 8 UAVs will even result in higher energy consumption than deploying 4 UAVs. Fig. 5 shows the energy consumption as a function of the average data size of the devices, together with the 95% confidence intervals. The results show that the energy consumption increases approximately linearly with the average data size and confirm the importance of optimizing the fraction of data offloaded and of the sub-band assignment in minimizing the energy consumption (c.f., FTO, ATO, and RSA variants versus proposed). Furthermore, the figure shows the lower optimality gap, proving the proposed solution’s efficiency.

![](images/98a6a88304d2cc257e7adf58ef11531ae703f34fcbf69e7d9c136d1bea758bb6.jpg)

Fig. 5. Energy consumption for J = 60 devices under different average data sizes.  
![](images/798e064e8d64ae16591911198b633b93f2eadf5bc9d7eb8ad17fc2b5aab8bb32.jpg)  
Fig. 6. Fraction of tasks offloaded and energy consumption versus maximum tolerable delay [ms].

## C. Impact of the Delay constraint

Fig. 6 shows the average fraction of the devices’ tasks that are offloaded as a function of the maximum allowable delay of tasks. The figure shows that the fraction of offloaded data decreases as the tasks’ allowable delay increases. At the same time, the energy consumption of the devices increases. These results show that computation offloading in the considered system is essential for satisfying the tasks’ delay constraints, but it leads to higher energy consumption than local computing.

![](images/bbd5c7bbc6466263ff2f1e96f03f39b20cd2bddc7249044cd948cf33499496cc.jpg)  
Fig. 7. Comparison of the achievable data rate of devices.

![](images/624c8bd45fba1c7534da758cc5031f793792672aec7de63256b1dfe0912f1dcf.jpg)

![](images/362fc86f5db9462612abfb75b15070f13dfedef78629b772c9194a6b431ae29f.jpg)  
Fig. 8. The average runtime [s] and the average number of iterations for the convergence of the proposed algorithm.

## D. Data Rate Analysis

Fig. 7 shows the achievable data rate of the devices as a function of the number of devices, when using the proposed scheme and its variants. The results for the achievable data rate explain well the difference in terms of energy consumption among the variants of the proposed scheme. The data rate is lowest for the RSA variant, which explains why sub-band assignment is crucial for low energy consumption. We can also observe that the effect of not optimizing the UAVs’ locations is significant, much bigger than that of not optimizing the transmit power allocation. Finally, the total data rate attained utilizing our proposed solution is the highest compared to alternative variants, and the proposed solution achieves nearly the same total data rate compared to that of the Optimal scheme. These results explain why our proposed solution has the lowest energy consumption, according to (12) as shown in Fig. 3.

## E. Convergence of Proposed Algorithm

Fig. 8 shows the average runtime, and the average number of iterations to the convergence of the proposed solution as a function of the number of devices for $K = 4$ , and 8. The figure shows that increasing the number of devices in the network results in the runtime growing considerably. However, the average number of iterations does not significantly increase. Additionally, it is interesting that deploying 4 UAVs requires more runtime and iterations to converge the proposed solution than deploying 8 UAVs. The reason is that deploying more UAVs will result in fewer associated devices at each UAV, which results in less burden to the UAV for decision making.

## VII. CONCLUSION

In this paper, we considered THz-assisted MEC-enabled integrated SAG networks to provide computation services to wireless devices in remote areas. Then, we investigated the energy minimization problem by optimization tasks offloading decision, sub-bands assignment, power control, and UAVs deployment while guaranteeing the maximum tolerable delay of devices’ computation tasks. Following, we showed that the formulated problem is a non-convex problem. Thus, to solve the problem, we decomposed the problem into four subproblems, namely, device task offloading decision problem, sub-band assignment and power control problem, UAV deployment problem, and UAV task offloading decision problem, respectively. Then, we solved the device task offloading decision problem by using the convex optimization technique, and a two-sided one-to-one matching game and CCP approach were deployed to address the sub-band assignment and power control problem. Moreover, we proposed SCA and BSUM to solve UAV deployment and UAV task offloading decision problems. Finally, we conducted comprehensive simulations to demonstrate the effectiveness of the proposed algorithm, and it was found that when compared to benchmark schemes, our proposed method significantly reduces the energy consumption of the UAVs and devices. An interesting extension of our model would be to consider the mobility of devices, UAVs, and satellites over time, which will affect the quality of the communication links. Assuming time is slotted, one would have to optimize the offloading decisions, resource allocation, and power control depending on the achievable channel gain per time slot. Furthermore, due to the movement of all network entities, which can lead to changes in signal strength, network topology, and overall network conditions, one may have to consider re-association between devices and UAVs, as well as between UAVs and satellites at each time slot.

## REFERENCES

[1] J. Ren, H. Guo, C. Xu, and Y. Zhang, “Serving at the edge: A scalable IoT architecture based on transparent computing,” IEEE Netw., vol. 31, no. 5, pp. 96–105, 2017.

[2] J. Liu, Y. Shi, Z. M. Fadlullah, and N. Kato, “Space-air-ground integrated network: A survey,” IEEE Commun. Surv. Tut., vol. 20, no. 4, pp. 2714–2741, Fourth Quarter 2018.

[3] C.-Q. Dai, J. Luo, S. Fu, J. Wu, and Q. Chen, “Dynamic user association for resilient backhauling in satellite–terrestrial integrated networks,” IEEE Syst. J., vol. 14, no. 4, pp. 5025–5036, Dec. 2020.

[4] I. F. Akyildiz, C. Han, Z. Hu, S. Nie, and J. M. Jornet, “Terahertz band communication: An old problem revisited and research directions for the next decade,” IEEE Trans. Commun., vol. 70, no. 6, pp. 4250–4285, Jun. 2022.

[5] C. Chaccour, M. N. Soorki, W. Saad, M. Bennis, P. Popovski, and M. Debbah, “Seven defining features of terahertz (THz) wireless systems: A fellowship of communication and sensing,” IEEE Commun. Surv. Tut., vol. 24, no. 2, pp. 967–993, Second Quarter 2022.

[6] A. Shafie, N. Yang, C. Han, J. M. Jornet, M. Juntti, and T. Kurner, “Terahertz communications for 6G and beyond wireless networks: Challenges, key advancements, and opportunities,” IEEE Netw., vol. 37, no. 3, pp. 162–169, May/Jun. 2023.

[7] I. F. Akyildiz, C. Han, and S. Nie, “Combating the distance problem in the millimeter wave and terahertz frequency bands,” IEEE Commun. Mag., vol. 56, no. 6, pp. 102–108, Jun. 2018.

[8] Y. Yuan, Y. Zhao, B. Zong, and S. Parolari, “Potential key technologies for 6G mobile communications,” Sci. China Inf. Sci., vol. 63, pp. 1–19, May 2020.

[9] L. Xu et al., “Joint location, bandwidth and power optimization for THz-enabled UAV communications,” IEEE Commun. Lett., vol. 25, no. 6, pp. 1984–1988, Jun. 2021.

[10] Y. M. Park, S. S. Hassan, Y. K. Tun, Z. Han, and C. S. Hong, “Joint resources and phase-shift optimization of MEC-enabled UAV in IRSassisted 6G THz networks,” in Proc. IEEE/IFIP Netw. Operations Manage Symp., Budapest, Hungary, 2022, pp. 1–7.

[11] Y. K. Tun, Y. M. Park, N. H. Tran, W. Saad, S. R. Pandey, and C. S. Hong, “Energy-efficient resource management in UAV-assisted mobile edge computing,” IEEE Commun. Lett., vol. 25, no. 1, pp. 249–253, Jan. 2021.

[12] Y. Zhu, W. Bai, M. Sheng, J. Li, D. Zhou, and Z. Han, “Joint UAV access and GEO satellite backhaul in IoRT networks: Performance analysis and optimization,” IEEE Internet Things J., vol. 8, no. 9, pp. 7126–7139, May 2021.

[13] S. Mao, S. He, and J. Wu, “Joint UAV position optimization and resource scheduling in space-air-ground integrated networks with mixed cloud-edge computing,” IEEE Syst. J., vol. 15, no. 3, pp. 3992–4002, Sep. 2021.

[14] Y. Chen, B. Ai, Y. Niu, H. Zhang, and Z. Han, “Energy-constrained computation offloading in space-air-ground integrated networks using distributionally robust optimization,” IEEE Trans. Veh. Technol., vol. 70, no. 11, pp. 12113–12125, Nov. 2021.

[15] C. Zhou et al., “Delay-aware IoT task scheduling in space-air-ground integrated network,” in Proc. IEEE Glob. Commun. Conf., Waikoloa, HI, USA, 2019, pp. 1–6.

[16] Y. Shi, J. Zhang, Y. Gao, and Y. Xia, “Inter-server computation offloading and resource allocation in multi-drone aided space-air-ground integrated IoT networks,” J. Commun. Netw., vol. 24, no. 3, pp. 324–335, Jun. 2022.

[17] G. Wang, S. Zhou, and Z. Niu, “Radio resource allocation for bidirectional offloading in space-air-ground integrated vehicular network,” J. Commun. Inf. Netw., vol. 4, no. 4, pp. 24–31, Dec. 2019.

[18] S. Yu, X. Gong, Q. Shi, X. Wang, and X. Chen, “EC-SAGINs: Edgecomputing-enhanced space–air–ground-integrated networks for Internet of Vehicles,” IEEE Internet Things J., vol. 9, no. 8, pp. 5742–5754, Apr. 2022.

[19] B. Chen, N. Li, Y. Li, X. Tao, and G. Sun, “Energy efficient hybrid offloading in space-air-ground integrated networks,” in Proc. IEEE Wireless Commun. Netw. Conf., Austin, TX, USA, 2022, pp. 1319–1324.

[20] Y. K. Tun, T. N. Dang, K. Kim, M. Alsenwi, W. Saad, and C. S. Hong, “Collaboration in the sky: A distributed framework for task offloading and resource allocation in multi-access edge computing,” IEEE Internet Things J., vol. 9, no. 23, pp. 24221–24235, Dec. 2022.

[21] M. T. Mamaghani and Y. Hong, “Terahertz meets untrusted UAV-relaying: Minimum secrecy energy efficiency maximization via trajectory and communication co-design,” IEEE Trans. Veh. Technol., vol. 71, no. 5, pp. 4991–5006, May 2022.

[22] J. Du, F. R. Yu, G. Lu, J. Wang, J. Jiang, and X. Chu, “MEC-assisted immersive VR video streaming over terahertz wireless networks: A deep reinforcement learning approach,” IEEE Internet Things J., vol. 7, no. 10, pp. 9517–9529, Oct. 2020.

[23] X. Liu, Y. Deng, C. Han, and M. Di Renzo, “Learning-based prediction, rendering and transmission for interactive virtual reality in RISassisted terahertz networks,” IEEE J. Sel. Areas Commun., vol. 40, no. 2, pp. 710–724, Feb. 2022.

[24] C. Chaccour, M. N. Soorki, W. Saad, M. Bennis, and P. Popovski, “Can terahertz provide high-rate reliable low latency communications for wireless VR,” IEEE Internet Things J., vol. 9, no. 12, pp. 9712–9729, Jun. 2022.

[25] C. Chaccour, R. Amer, B. Zhou, and W. Saad, “On the reliability of wireless virtual reality at terahertz (THz) frequencies,” in Proc. IFIP Int. Conf. New Technol. Mobility Secur., Canary Islands, Spain, 2019, pp. 1–5.

[26] S. Xie, H. Li, L. Li, Z. Chen, and S. Li, “Reliable and energy-aware job offloading at terahertz frequencies for mobile edge computing,” China Commun., vol. 17, no. 12, pp. 17–36, Dec. 2020.

[27] C. Chaccour and W. Saad, “On the ruin of age of information in augmented reality over wireless terahertz (THz) networks,” in Proc. IEEE Glob. Commun. Conf., Taipei, Taiwan, 2020, pp. 1–6.

[28] S. A. Busari et al., “Generalized hybrid beamforming for vehicular connectivity using THz massive MIMO,” IEEE Trans. Veh. Technol., vol. 68, no. 9, pp. 8372–8383, Sep. 2019.

[29] Y. Pan, K. Wang, C. Pan, H. Zhu, and J. Wang, “Self-sustainable reconfigurable intelligent surface aided simultaneous terahertz information and power transfer (STIPT),” IEEE Trans. Wireless Commun., vol. 21, no. 7, pp. 5420–5434, Jul. 2022.

[30] X. Liu, H. Zhang, K. Long, M. Zhou, Y. Li, and H. V. Poor, “Proximal policy optimization-based transmit beamforming and phase-shift design in an IRS-aided ISAC system for the THz band,” IEEE J. Sel. Areas Commun., vol. 40, no. 7, pp. 2056–2069, Jul. 2022.

[31] C. Huang et al., “Multi-hop RIS-empowered terahertz communications: A DRL-based hybrid beamforming design,” IEEE J. Sel. Areas Commun., vol. 39, no. 6, pp. 1663–1677, Jun. 2021.

[32] D. Fan et al., “Channel estimation and self-positioning for UAV swarm,” IEEE Trans. Commun., vol. 67, no. 11, pp. 7994–8007, Nov. 2019.

[33] R. Guo, K. Wang, Z. Deng, W. Lin, and R. Song, “A prediction model for channel state information in satellite communication system,” in Proc. IEEE 31st Annu. Int. Symp. Pers. Indoor Mobile Radio Commun., London, U.K., 2020, pp. 1–6.

[34] G.-Y. Chang, C.-K. Hung, and C.-H. Chen, “A CSI prediction scheme for satellite-terrestrial networks,” IEEE Internet Things J., vol. 10, no. 9, pp. 7774–7785, May 2023.

[35] J. M. Jornet and I. F. Akyildiz, “Channel modeling and capacity analysis for electromagnetic wireless nanonetworks in the terahertz band,” IEEE Trans. Wireless Commun., vol. 10, no. 10, pp. 3211–3221, Oct. 2011.

[36] Y. K. Tun, K. T. Kim, L. Zou, Z. Han, G. Dán, and C. S. Hong, “Collaborative computing services at ground, air, and space: An optimization approach,” IEEE Trans. Veh. Technol., vol. 73, no. 1, pp. 1491–1496, Jan. 2024.

[37] Y. K. Tun, N. H. Tran, D. T. Ngo, S. R. Pandey, Z. Han, and C. S. Hong, “Wireless network slicing: Generalized kelly mechanism-based resource allocation,” IEEE J. Sel. Areas Commun., vol. 37, no. 8, pp. 1794–1807, Aug. 2019.

[38] Y. Gu, W. Saad, M. Bennis, M. Debbah, and Z. Han, “Matching theory for future wireless networks: Fundamentals and applications,” IEEE Commun. Mag., vol. 53, no. 5, pp. 52–59, May 2015.

[39] A. E. Roth, “Deferred acceptance algorithms: History, theory, practice, and open questions,” Int. J. Game Theory, vol. 36, no. 3, pp. 537–569, 2008.

[40] M. Hong, M. Razaviyayn, Z.-Q. Luo, and J.-S. Pang, “A unified algorithmic framework for block-structured optimization involving Big Data: With applications in machine learning and signal processing,” IEEE Signal Process. Mag., vol. 33, no. 1, pp. 57–77, Jan. 2016.

[41] A. Bandi, B. Shankar, M. R. S. Chatzinotas, and B. Ottersten, “A joint solution for scheduling and precoding in multiuser MISO downlink channels,” IEEE Trans. Wireless Commun., vol. 19, no. 1, pp. 475–490, Jan. 2020.

[42] Z. Li et al., “Energy efficient resource allocation for UAV-assisted spaceair-ground Internet of Remote Things networks,” IEEE Access, vol. 7, pp. 145348–145362, 2019.

[43] Z. Hu et al., “Joint resources allocation and 3D trajectory optimization for UAV-enabled space-air-ground integrated networks,” IEEE Trans. Veh. Technol., vol. 72, no. 11, pp. 14214–14229, Nov. 2023.