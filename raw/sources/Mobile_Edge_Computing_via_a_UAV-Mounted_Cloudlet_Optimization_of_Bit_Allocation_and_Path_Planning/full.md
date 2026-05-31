# Mobile Edge Computing via a UAV-Mounted Cloudlet: Optimization of Bit Allocation and Path Planning

Seongah Jeong, Osvaldo Simeone, Fellow, IEEE, and Joonhyuk Kang , Member, IEEE

Abstract—Unmanned aerial vehicles (UAVs) have been recently considered as means to provide enhanced coverage or relaying services to mobile users (MUs) in wireless systems with limited or no infrastructure. In this paper, a UAV-based mobile cloud computing system is studied in which a moving UAV is endowed with computing capabilities to offer computation offloading opportunities to MUs with limited local processing capabilities. The system aims at minimizing the total mobile energy consumption while satisfying quality of service requirements of the offloaded mobile application. Offloading is enabled by uplink and downlink communications between the mobile devices and the UAV, which take place by means of frequency division duplex via orthogonal or nonorthogonal multiple access schemes. The problem of jointly optimizing the bit allocation for uplink and downlink communications as well as for computing at the UAV, along with the cloudlet’s trajectory under latency and UAV’s energy budget constraints is formulated and addressed by leveraging successive convex approximation strategies. Numerical results demonstrate the significant energy savings that can be accrued by means of the proposed joint optimization of bit allocation and cloudlet’s trajectory as compared to local mobile execution as well as to partial optimization approaches that design only the bit allocation or the cloudlet’s trajectory.

Index Terms—Communication, computation, mobile cloud computing, successive convex approximation (SCA), unmanned aerial vehicles (UAVs).

# I. INTRODUCTION

HE deployment of moving base stations or relays mounted T on unmanned aerial vehicles (UAVs) is a promising solution to extend the coverage of a wireless system to areas in which there is a limited available infrastructure of wireless ac-

Manuscript received September 17, 2016; revised March 14, 2017; accepted May 11, 2017. Date of publication May 19, 2017; date of current version March 15, 2018. This work was supported by ICT R&D program of MSIP/IITP. (2015- 0-00820, A research on a novel communication system using storage as wireless communication resource.) The work of O. Simeone was supported in part by the U.S. NSF under Grant CCF-1525629 and in part by the European Research Council under the European Union’s Horizon 2020 Research and Innovation Programme under Grant 725731. The review of this paper was coordinated by Prof. J. Sun. (Corresponding author: Joonhyuk Kang.)

S. Jeong is with the School of Engineering and Applied Sciences, Harvard University, Cambridge, MA 02138 USA (e-mail: sej293@g.harvard.edu).

O. Simeone is with the Department of Informatics, King’s College London, London WC2R 2LS U.K. (e-mail: osvaldo.simeone@kcl.ac.uk).

J. Kang is with the Department of Electrical Engineering, Korea Advanced Institute of Science and Technology, Daejeon 34141 South Korea (e-mail: jhkang@ee.kaist.ac.kr).

Color versions of one or more of the figures in this paper are available online at http://ieeexplore.ieee.org.

Digital Object Identifier 10.1109/TVT.2017.2706308 cess points, such as in developing countries or rural environments, as well as in disaster response, emergency relief and military scenarios [1]–[7]. However, the limited coverage and mobility of energy-constrained UAVs introduce new challenges for the design of UAV-based wireless communications. As a result, recent research activity has focused on the problems of path planning and energy-aware deployment for UAV-based systems [8]–[18], as we briefly review below.

# A. State of the Art

In [8]–[11], a UAV-enabled mobile relaying system is studied, where the role of the UAV is to act as a relay for communication between wireless devices. In particular, the problem of jointly optimizing the power allocation at source and moving relay, as well as the relay’s trajectory, is tackled in [8] with the aim of maximizing the throughput under mobility constraints on the relay’s speed and terminal locations and assuming a decodestore-and-forward scheme. To address the problem, an iterative algorithm is proposed to alternatively optimize the power allocation and relay’s trajectory. In [9], the problem of efficient data delivery in sparse mobile ad hoc networks is studied, where a set of moving relays between pairs of sources and destinations is employed. Two types of relaying schemes are developed in order to minimize the message drop rate under energy constraints, whereby either the nodes move to meet a given relay’s trajectory, or a relay moves to meet static nodes. Both schemes are optimized in terms of trajectory of either the nodes or the relay. A similar scheme has also been introduced for sparse sensor networks in [10].

The authors in [11] study the deployment of UAVs acting as relays between ground terminals and a network base station so as to provide uplink transmission coverage for ground-to-UAV communication. The problem of optimizing the UAV heading angle is tackled with the goal of maximizing the sum-rate under individual minimal rate constraints. To this end, the authors derive a closed-form expression approximate for the average uplink data rate for each link. In [12], a scheduling and resource allocation framework is developed for energy-efficient machineto-machine communications with UAVs, where multiple UAVs provide uplink transmission to collect the data from the heads of the clusters consisting of a number of machine-type devices. The authors investigate the minimum number of required UAVs to serve the cluster heads and their dwelling time over each cluster head by using the queue rate stability concept.

TABLE I LIST OF SYMBOLS 

<table><tr><td>Parameter</td><td>Definition</td></tr><tr><td> $K$ </td><td>Number of mobile users (MUs)</td></tr><tr><td> $I_{k}$ </td><td>Number of input information bits of MU  $k$  to be processed</td></tr><tr><td> $C_{k}$ </td><td>Number of CPU cycles per input bit of MU  $k$  needed for computing</td></tr><tr><td> $O_{k}$ </td><td>Number of output bits produced by the execution of the application per input bits of MU  $k$ </td></tr><tr><td> $T$ </td><td>Latency constraint or deadline</td></tr><tr><td> $N$ </td><td>Number of frames within  $T$ </td></tr><tr><td> $\boldsymbol{p}_{k}^{m}$ </td><td>Position of MU  $k$ </td></tr><tr><td> $\boldsymbol{p}_{i}^{c}(t)$  ( $\boldsymbol{p}_{n}^{c}$ )</td><td>Position of UAV</td></tr><tr><td> $\boldsymbol{p}_{I}^{c}$  ( $\boldsymbol{p}_{1}^{c}$ )</td><td>Initial position of UAV projected onto xy-plane</td></tr><tr><td> $\boldsymbol{p}_{F}^{c}$  ( $\boldsymbol{p}_{N+1}^{c}$ )</td><td>Final position of UAV projected onto xy-plane</td></tr><tr><td> $H$ </td><td>Altitude of the UAV</td></tr><tr><td> $\boldsymbol{v}_{n}^{c}$ </td><td>UAV’s velocity at the  $n$ th frame</td></tr><tr><td> $\boldsymbol{v}_{n}^{c}$ </td><td>UAV’s initial and final velocity constraint</td></tr><tr><td> $v_{\text{max}}$ </td><td>UAV’s maximum speed</td></tr><tr><td> $\boldsymbol{a}_{n}^{c}$ </td><td>UAV’s acceleration at the  $n$ th frame</td></tr><tr><td> $a_{\text{max}}$ </td><td>UAV’s maximum acceleration</td></tr><tr><td> $\Delta$ </td><td>Frame duration</td></tr><tr><td> $\mathcal{E}$ </td><td>UAV’s energy budget</td></tr><tr><td> $\boldsymbol{g}_{k,n}$  ( $\boldsymbol{p}_{n}^{c}$ )</td><td>Path loss between MU  $k$  and cloudlet at the  $n$ th frame</td></tr><tr><td> $g_{0}$ </td><td>Received power at the reference distance  $d_{0} = 1$  m for a transmission power of 1 W</td></tr><tr><td> $E^{m}$ </td><td>Total energy consumption in mobile execution</td></tr><tr><td> $E_{k}^{m}$ </td><td>Energy consumption of MU  $k$  in mobile execution</td></tr><tr><td> $E_{k,n}^{c}$ </td><td>Computation energy consumption at cloudlet for MU  $k$  at the  $n$ th frame</td></tr><tr><td> $E_{O,k,n}^{d}$ </td><td>Transmission energy consumption for communication between MU  $k$  and cloudlet at the  $n$ th frame in orthogonal access ( $d =$  m for uplink,  $d =$  c for downlink)</td></tr><tr><td> $E_{N,k,n}^{d}$ </td><td>Transmission energy consumption for communication between MU  $k$  and cloudlet at the  $n$ th frame in non-orthogonal access ( $d =$  m for uplink,  $d =$  c for downlink)</td></tr><tr><td> $E_{F,n}^{c}$ </td><td>Flying energy consumption of the  $n$ th frame</td></tr><tr><td> $L_{k,n}^{d}$ </td><td>Number of bits transmitted for communication between MU  $k$  and cloudlet at the  $n$ th frame ( $d =$  m for uplink,  $d =$  c for downlink)</td></tr><tr><td> $l_{k,n}$ </td><td>Number of bits computed for application of MU  $k$  at cloudlet in  $n$ th frame</td></tr><tr><td> $f_{k}^{m}$ </td><td>CPU frequency of MU  $k$ </td></tr><tr><td> $f_{n}^{c}$ </td><td>CPU frequency of cloudlet at the  $n$ th frame</td></tr><tr><td> $B$ </td><td>Bandwidth</td></tr><tr><td> $N_{0}$ </td><td>Noise spectrum density</td></tr><tr><td> $\gamma_{k}^{m}$ </td><td>Effective switched capacitance of MU  $k$ &#x27;s processor</td></tr><tr><td> $\gamma^{c}$ </td><td>Effective switched capacitance of cloudlet processor</td></tr><tr><td> $M$ </td><td>UAV’s gross mass</td></tr><tr><td> $g$ </td><td>Gravitational acceleration</td></tr><tr><td> $\kappa$ </td><td>Constant for Model 1 in (8) ( $\kappa = 0.5M\Delta$ )</td></tr><tr><td> $\kappa_{1}$ </td><td>Constant for Model 2 in (29) ( $\kappa_{1} = 0.5\rho C_{D_{0}}S_{r}\Delta$  for fixed-wing UAV and  $\kappa_{1} = 0.5\rho C_{D_{f}}S_{r}\Delta$  for rotary-wing UAV)</td></tr><tr><td> $\kappa_{2}$ </td><td>Constant for Model 2 in (29)( $\kappa_{2} = 2M^{2}g^{2}\Delta /(\pi e_{0}A_{R}\rho S_{r})$  for fixed-wing UAV and  $\kappa_{2} = \epsilon M^{2}g^{2}\Delta /(2\rho A)$  for rotary-wing UAV)</td></tr></table>

References [13], [14], instead, study the optimal deployment of multiple UAVs acting as flying base stations in the downlink scenario. The optimal altitude for a single UAV is addressed with the aim of minimizing the required downlink transmit power for covering a target area, and then the treatment is extended to two UAVs with and without interference between the UAVs in [13]. In contrast, in [14], the minimization of the total required downlink transmit power from the UAVs is tackled under minimum users’ rate requirements by iteratively addressing the optimizations of the UAV’s locations and of the boundaries of their coverage areas. The authors in [15] analyze the downlink coverage and rate performance for static and mobile UAV. For a static UAV, they derive coverage probability and system sumrate as a function of the UAV’s altitude and of the number of users. For a mobile UAV, the minimum number of stop points for the UAV required to completely cover the area of interest is analyzed via disk covering problem. A point-to-point communication link between the UAV and a ground user is investigated in [16] with the goal of optimizing the UAV’s trajectory under a UAV’s energy consumption model that accounts for the impact of the UAV’s velocity and acceleration.

Beside the communication scenarios reviewed above, other optimization problems involving UAV path planning have been studied. For instance, in [17], a scenario is investigated in which a ground vehicle and an aerial vehicle move cooperatively to carry out intelligence, surveillance and reconnaissance (ISR) missions. Path planning for the ground and aerial vehicles is carried out via a branch-and-cut algorithm. As another example, [18] tackles the problem of UAV trajectory optimization for drone delivery of material goods by minimizing the total energy cost under a delivery time limit constraint, as well as by minimizing the overall delivery time under an energy budget constraint. Sub-optimal solutions for the problem of interest are presented via a simulated annealing heuristic approach.

# B. UAV as a Moving Cloudlet

As briefly reviewed above, most prior works on the deployment of UAVs in communication system assume their use either as moving relays [8]–[11] or as flying base stations [12]–[18]. It was instead noted in [4] that UAVs can also be used as mobile cloud computing systems, in which a UAV-mounted cloudlet [3]–[5] provides application offloading opportunities to mobile users (MUs). UAVs can hence enable fog computing [19] even in the absence of a working wireless infrastructure. Specifically, MUs can offload computationally heavy tasks, such as object recognition or augmented-reality applications, to the cloudlet by means of uplink/downlink communications with the UAV. Referring to Fig. 1 for an illustration, the offloading procedure requires uplink transmission of input data for the application to be run at the cloudlet from the mobiles to the UAV, computing at the UAV-mounted cloudlet, and downlink transmission of outcome of computing at the cloudlet from the UAV to the mobiles. Among the possible examples and applications, the use of the moving cloudlets can for instance play an important role in disaster response, emergency relief or military scenarios, as mobile devices with limited processing capabilities can benefit from the cloudlet-aided execution of data analytics application for the assessment of the status of victims, enemies, or hazardous terrain and structures.

# C. Main Contributions

In this paper, we focus on the scenario illustrated in Fig. 1 in which a moving UAV is deployed to offer offloading opportunities to mobile devices. We tackle the key design problem of optimizing the bit allocation for communication in uplink and downlink and for computing at the cloudlet, as well as the UAV’s trajectory, with the goal of minimizing the mobile energy consumption. For uplink and downlink transmission, we assume frequency division duplex (FDD) and either orthogonal or non-orthogonal multiple access (NOMA) schemes. We note that the latter is a promising multiple access technique for 5G networks which is currently being considered due to its potentially superior spectral efficiency [20], [21]. The design problem is formulated for both orthogonal access and non-orthogonal access under latency and UAV’s energy budget constraints. The UAV’s energy budget includes the energy consumption for communication and computing as well as for flying. For the latter energy constraint, we consider two different models, both of which are investigated in the literature. The first model, adopted in [22]–[25], postulates the flying energy to depend only on the UAV’s velocity, while the second model accounts also for the impact of the acceleration following [16], [26]–[28]. The resulting non-convex problem is tackled by means of successive convex approximation (SCA) [29], [30], which allows us to derive an efficient iterative algorithm that is guaranteed to converge to a local minimum of the original non-convex problem.

![](images/f972b795989219b82e448073dad51b518f4bb0076ad7fca489eeb178231947fe.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["UAV-Mounted Cloudlet p^c(t) = (x^c(t), y^c(t), H)"] --> B["Device 1"]
    A --> C["Device 2"]
    A --> D["Device 3"]
    A --> E["Device 4"]
    B --> F["ML 1"]
    C --> G["ML k"]
    D --> H["ML K"]
    E --> I["..."]
    F --> J["UL"]
    G --> K["DL"]
    H --> L["..."]
    I --> M["p^m_k = (x^m_k, y^m_k, 0)"]
    J --> N["z"]
    K --> O["y"]
    L --> P["x"]
    M --> Q["y"]
    N --> R["z"]
```
</details>

Fig. 1. Illustration of the considered mobile cloud computing system based on a UAV-mounted cloudlet that provides application offloading opportunities to MUs. The key design problem is the optimization of the bit allocation for communication in uplink (UL) and downlink (DL) and computing, as well as the cloudlet’s trajectory with the goal of minimizing the mobile energy consumption.

The rest of this paper is organized as follows. Section II presents the system model including the energy consumption models for communication, computation and flying. In Section III and Section IV, we formulate and tackle the mentioned joint optimization problems over the bit allocation and UAV’s trajectory under the first UAV’s flying energy consumption model for orthogonal access and NOMA, respectively. Then, in Section V, the joint optimization problems are studied with the second UAV’s flying energy consumption model. Finally, numerical results are given in Section VI, and conclusions are drawn in Section VII.

# II. SYSTEM MODEL

# A. Set-Up

In this paper, we consider the mobile cloud computing system illustrated in Fig. 1, which consists of K MUs and a UAV-mounted cloudlet. We study the optimization of the offloading process from the MUs to the moving cloudlet with the goal of minimizing the total energy consumption of all the MUs. To enable the offloading of a given application for each MU k, with $k \in \mathcal { K } = \{ 1 , \dots , K \}$ , the following steps are necessary; (i) uplink transmission of the application input data from the MU k to the UAV; (ii) execution of the application by the UAV-mounted cloudlet; and (iii) downlink transmission of the output of the application from the UAV to MU k. We assume frequency division duplex (FDD) with equal channel bandwidth B allocated for uplink and downlink. Moreover, for uplink and downlink communications, two types of access schemes are considered, namely orthogonal and non-orthogonal access. We note that, in 5G, the latter is typically referred to as NOMA. Receivers at the MUs and cloudlet are assumed to have no limitations on the resolution of their digital front-ends. The application of the MU k ∈ K is characterized by the number $I _ { k }$ of input information bits to be processed, the number $C _ { k }$ of CPU cycles per input bit needed for computing, and the number $O _ { k }$ of output bits produced per input bit by the execution of the application. We assume that all applications need to be computed within a time T .

![](images/13ba650998b0839045ae807746076eb202f1fc361deb09af5f93a21fcf61abd7.jpg)

<details>
<summary>text_image</summary>

Frame n - 1
Frame n
Frame n + 1
...
p_n-1^c
p_n^c
p_n+1^c
p_n+2^c
Time
Δ
Δ/K
MU 1
MU 2
...
MU k
...
MU K - 1
MU K
(a)
Δ
MU 1 ... MU K
(b)
</details>

Fig. 2. Frame structure of the considered mobile cloud computing system: (a) Orthogonal access, (b) non-orthogonal access.

A three-dimensional Cartesian coordinate system is adopted, as shown in Fig. 1, whose coordinates are measured in meters. We assume that all MUs are located at the xy-plane, e.g., on the ground, with MU k located at position $\pmb { p } _ { k } ^ { m } = ( x _ { k } ^ { m } , y _ { k } ^ { m } , 0 )$ , for $k \in { \mathcal { K } } .$ , while the UAV flies along a trajectory $\pmb { p } ^ { c } ( t ) =$ $( x ^ { c } ( t ) , y ^ { c } ( t )$ , H) with a fixed altitude H, for $0 \leq t \leq T$ . In this work, since the UAV flies horizontally at a constant altitude H, we focus on the UAV’s trajectory projected onto the xy-plane. Due to its launching and landing locations, flying paths and operational capability, the initial and final location and maximum speed of the UAV are assumed to be predetermined as $\pmb { p } _ { I } ^ { c } = ( x _ { I } ^ { c } , y _ { I } ^ { c } ) , \pmb { p } _ { F } ^ { c } = ( x _ { F } ^ { c } , y _ { F } ^ { c } )$ ), both with the altitude H , and vmax , respectively.

As seen in Fig. 2, the time horizon T is divided into N intervals each of duration Δ seconds [3], [8], [16], i.e., T = N Δ, in which the UAV continuously communicates and computes while flying. The frame duration $\Delta$ is chosen to be sufficiently small for the UAV’s location to be approximately constant within each frame. Accordingly, the UAV’s trajectory pc (t) can be characterized by the discrete-time UAV’s location $\pmb { p } _ { n } ^ { c } = ( x _ { n } ^ { c } , y _ { n } ^ { c } )$

with altitude H , for $n \in \mathcal { N } = \{ 1 , \dots , N \}$ , where ${ \pmb { p } } _ { 1 } ^ { c } = { \pmb { p } } _ { I } ^ { c }$ and $\pmb { p } _ { N + 1 } ^ { c } = \pmb { p } _ { F } ^ { c }$ . The trajectory $\{ { \pmb p } _ { n } ^ { c } \} _ { n \in \{ 2 , . . . , N \} }$ is subject to optimization. The quantity

$$
\boldsymbol {v} _ {n} ^ {c} = \frac {\boldsymbol {p} _ {n + 1} ^ {c} - \boldsymbol {p} _ {n} ^ {c}}{\Delta} \tag {1}
$$

represents the velocity vector in the nth frame. As mentioned, we have the constraint on the maximum speed

$$
\left\| \boldsymbol {v} _ {n} ^ {c} \right\| = \frac {\left\| \boldsymbol {p} _ {n + 1} ^ {c} - \boldsymbol {p} _ {n} ^ {c} \right\|}{\Delta} \leq v _ {\max}. \tag {2}
$$

Note that the final position should be assumed no later than after a time T from the initial time. As a result, we have the constraint

$$
\frac {\left\| \boldsymbol {p} _ {N + 1} ^ {c} - \boldsymbol {p} _ {1} ^ {c} \right\|}{N \Delta} \leq v _ {\max}, \tag {3}
$$

in order for a feasible trajectory from the UAV’s initial to final location to exist.

For orthogonal access, each nth frame, for $n \in { \mathcal { N } } .$ , is assumed to have K equally spaced time slots, each of which has the duration of $\Delta / K$ seconds and is preallocated to one MU in both uplink and downlink. For non-orthogonal access, all MUs simultaneously transmit and receive data within the entire frame of Δ seconds in uplink and downlink. In the latter case, we treat the interference from undesired signals as additive noise. This assumption is standard in the practical implementation of communication systems, as well as in the communication and information theory literatures (see, e.g., [31]). We recall that uplink and downlink do not interfere with one another due to the assumption of FDD.

As in [3], [8], [16], we assume that the communication channels between MUs and UAV are dominated by line-of-sight links. At the nth frame, the channel gain between the MU k and cloudlet is accordingly given by [3], [8], [16]

$$
g _ {k, n} (\boldsymbol {p} _ {n} ^ {c}) = \frac {g _ {0}}{(x _ {n} ^ {c} - x _ {k} ^ {m}) ^ {2} + (y _ {n} ^ {c} - y _ {k} ^ {m}) ^ {2} + H ^ {2}}, \tag {4}
$$

where $g _ { 0 }$ represents the received power at the reference distance $d _ { 0 } = 1$ m for a transmission power of 1 W. An additive white Gaussian channel noise with zero mean and power spectral density $N _ { 0 }$ [dBm/Hz] is assumed. In the following, we summarize the energy consumption model for computation [32], [33], communication [3], [8], [16] and flying [22]–[25]. As we will detail in the following sections, our goal is to minimize the mobile energy consumption.

# B. Energy Consumption Model for Offloading

Computation energy: First, we review the energy consumption model for computation at the cloudlet [32], [33]. When the CPU of the cloudlet is operated at the frequency $f ^ { c }$ [CPU cycles/s], the energy consumption required for executing the application of MU k over l input bits is given as

$$
E _ {k} ^ {c} (l, f ^ {c}) = \gamma^ {c} C _ {k} l (f ^ {c}) ^ {2}, \tag {5}
$$

where $\gamma ^ { c }$ is the effective switched capacitance of the cloudlet processor.

Communication energy: The energy consumption for communication at the mobile and at the UAV depends on whether orthogonal access or non-orthogonal access are deployed. With orthogonal access, the energy consumption for transmitting $L _ { k , n } ^ { m }$ bits in the uplink, or $L _ { k , n } ^ { c }$ in the downlink, between the MU k and cloudlet, within the allocated slot $\Delta / K$ seconds at the nth frame, can be computed based on standard informationtheoretic arguments [34] as

$$
E _ {O, k, n} ^ {d} (L _ {k, n} ^ {d}, \boldsymbol {p} _ {n} ^ {c}) = \frac {N _ {0} B \Delta / K}{g _ {k , n} (\boldsymbol {p} _ {n} ^ {c})} \left(2 ^ {\frac {L _ {k , n} ^ {d}}{B \Delta / K}} - 1\right), \tag {6}
$$

where we recall that $g _ { k , n } ( \pmb { p } _ { n } ^ { c } )$ in (4) is the path loss between the MU k and cloudlet at the nth frame, and d = m for uplink while $d = c$ for downlink.

With non-orthogonal access, e.g., NOMA in 5G, since all the MUs can simultaneously transmit and receive data within entire frame of duration Δ in both uplink and downlink, interference is caused by the undesired signals of other MUs which are assumed to be treated as additive noise [31]. When $L _ { k , n } ^ { m }$ and $L _ { k , n } ^ { c }$ bits are transmitted in uplink and in downlink, respectively, between the MU k and cloudlet experiencing a path loss $g _ { k , n } ( \pmb { p } _ { n } ^ { c } )$ at the nth frame, the transmission energy consumptions of uplink and downlink are calculated as [34]

$$
\begin{array}{l} E _ {N, k, n} ^ {m} (L _ {n} ^ {m}, \pmb {p} _ {n} ^ {c}) = \frac {1}{g _ {k , n} (\pmb {p} _ {n} ^ {c})} (N _ {0} B \Delta \\ \left. + \sum_ {k ^ {\prime} = 1, k ^ {\prime} \neq k} ^ {K} g _ {k ^ {\prime}, n} \left(\boldsymbol {p} _ {n} ^ {c}\right) E _ {N, k ^ {\prime}, n} ^ {m} \left(L _ {n} ^ {m}, \boldsymbol {p} _ {n} ^ {c}\right)\right) \left(2 ^ {\frac {L _ {k , n} ^ {m}}{B \Delta}} - 1\right) (7 a) \\ \end{array}
$$

and

$$
\begin{array}{l} E _ {N, k, n} ^ {c} \left(L _ {n} ^ {c}, \boldsymbol {p} _ {n} ^ {c}\right) = \left(\frac {N _ {0} B \Delta}{g _ {k , n} \left(\boldsymbol {p} _ {n} ^ {c}\right)} \right. \\ \left. + \sum_ {k ^ {\prime} = 1, k ^ {\prime} \neq k} ^ {K} E _ {N, k ^ {\prime}, n} ^ {c} (L _ {n} ^ {c}, \boldsymbol {p} _ {n} ^ {c})\right) \left(2 ^ {\frac {L _ {k , n} ^ {c}}{B \Delta}} - 1\right), \tag {7b} \\ \end{array}
$$

respectively, where the sets of all the uplink and downlink transmission bits related to the nth frame are denoted as $L _ { n } ^ { m } = \{ L _ { k , n } ^ { m } \} _ { k \in \mathcal { K } }$ and $L _ { n } ^ { c } = \{ L _ { k , n } ^ { c } \} _ { k \in \mathcal { K } }$ . Note that in the nonorthogonal access, the transmission energies required for the applications of $\mathbf { M U } k \in \mathcal { K }$ in both uplink and downlink depend on the transmission energies of the other MUs due to the interference.

Flying energy: As for the energy consumption at the UAV due to flying, we will consider two different models that have been adopted in the literature. The first model considered in, e.g., [22]–[25], postulates the flying energy at each frame n to depend only on the velocity vector $\pmb { v } _ { n } ^ { c }$ as

$$
\text {(Model 1)} E _ {F, n} ^ {c} \left(\boldsymbol {v} _ {n} ^ {c}\right) = \kappa \left\| \boldsymbol {v} _ {n} ^ {c} \right\| ^ {2}, \tag {8}
$$

where $\kappa = 0 . 5 M \Delta$ and M is the UAV’s mass, including its payload. Note that only the kinetic energy is accounted for in Model 1, due to the fact that constant-height flight entails no change in the gravitational potential energy. The second model assumes that the energy $E _ { F , n } ^ { c }$ depends also on the acceleration vector (cf. (29)) according to [16], [26]–[28]. We will describe and study this model in Section V.

# C. Energy Consumption Model for Mobile Execution

For reference, we consider the total energy consumption of the MUs if all applications are executed locally. In order to guarantee that each MU k processes the $I _ { k }$ input bits within $T$ seconds, the CPU frequency $f _ { k } ^ { m }$ must be chosen as [32], [33]

$$
f _ {k} ^ {m} = \frac {C _ {k} I _ {k}}{T}, \tag {9}
$$

which yields the total energy consumption of MUs of

$$
E ^ {m} \triangleq \sum_ {k = 1} ^ {K} E _ {k} ^ {m} (I _ {k}, f _ {k} ^ {m}) = \sum_ {k = 1} ^ {K} \frac {\gamma_ {k} ^ {m} C _ {k} ^ {3}}{T ^ {2}} I _ {k} ^ {3}, \tag {10}
$$

where $\gamma _ { k } ^ { m }$ is the effective switched capacitance of the MU k’s processor.

# III. OPTIMAL ENERGY CONSUMPTION FOR ORTHOGONAL ACCESS

In this section, we tackle the problem of minimizing the total mobile energy consumption for offloading assuming orthogonal access in uplink and downlink. Specifically, we focus on the joint optimization of the bit allocation for uplink and downlink data transmission and for cloudlet’s computing, as well as of the cloudlet’s trajectory, under constraints on the UAV’s energy budget and mobility constraints. We consider the model (8) for the UAV flying model.

# A. Problem Formulation

At the nth frame, for $n \in { \mathcal { N } } .$ , we define the number of input bits transmitted in the uplink from the MU k to cloudlet as $L _ { k , n } ^ { m } ,$ the number of bits computed for the application of the MU k at the cloudlet as $l _ { k , n }$ , and the number of bits transmitted in the downlink from cloudlet to MU k as $L _ { k , n } ^ { c }$ . Also, we denote the frequency at which the cloudlet CPU is operated for the offloaded applications from MUs at the nth frame as $f _ { n } ^ { c }$ . Along with the cloudlet position $\{ { \pmb p } _ { n } ^ { c } \}$ , these variables are subject to optimization.

According to the definitions above, at every nth frame, the CPU frequency $f _ { n } ^ { c }$ selected by the UAV must be such that the UAV can process $\textstyle \sum _ { k = 1 } ^ { K } l _ { k , n }$ bits from the applications of all the MUs within the given frame as

$$
f _ {n} ^ {c} = \frac {\sum_ {k = 1} ^ {K} C _ {k} l _ {k , n}}{\Delta}. \tag {11}
$$

This yields the computation energy required for offloading by MU k at the nth frame as

$$
E _ {k, n} ^ {c} (l _ {n}) \triangleq E _ {k} ^ {c} (l _ {n}, f _ {n} ^ {c}) = \frac {\gamma^ {c} C _ {k} l _ {k , n}}{\Delta^ {2}} \left(\sum_ {k ^ {\prime} = 1} ^ {K} C _ {k ^ {\prime}} l _ {k ^ {\prime}, n}\right) ^ {2}, \tag {12}
$$

where we have defined the total number of computing bits at the nth frame as $l _ { n } = \{ l _ { k , n } \} _ { k \in \mathcal { K } }$ . Our objective is to minimize the total energy consumption at the MUs by jointly optimizing the bit allocation $\{ L _ { k , n } ^ { m } \} _ { n \in \{ 1 , \dots , N - 2 \} , k \in K } , \{ l _ { k , n } \} _ { n \in \{ 2 , \dots , N - 1 \} , k \in K }$ and $\{ L _ { k , n } ^ { c } \} _ { n \in \{ 3 , \dots , N \} , k \in \mathcal { K } }$ for communication and computing needed to support offloading from all MUs along with the cloudlet trajectory $\{ \pmb { p } _ { n } ^ { c } \} _ { n \in \{ 2 , . . . , N \} }$ . The corresponding design problem is formulated as follows:

$$
\underset {\{L _ {k, n} ^ {m} \}, \{l _ {k, n} \}, \{L _ {k, n} ^ {c} \}, \{\boldsymbol {p} _ {n} ^ {c} \}} {\text { minimize }} \sum_ {k = 1} ^ {K} \sum_ {n = 1} ^ {N - 2} E _ {O, k, n} ^ {m} (L _ {k, n} ^ {m}, \boldsymbol {p} _ {n} ^ {c}) \tag {13a}
$$

$$
\text { s.t. } \sum_ {k = 1} ^ {K} \sum_ {n = 1} ^ {N - 2} E _ {k, n + 1} ^ {c} (l _ {n + 1}) + E _ {O, k, n + 2} ^ {c} (L _ {k, n + 2} ^ {c}, \boldsymbol {p} _ {n + 2} ^ {c})
$$

$$
+ \sum_ {n = 1} ^ {N} E _ {F, n} ^ {c} (\boldsymbol {v} _ {n} ^ {c}) \leq \mathcal {E} \tag {13b}
$$

$$
\sum_ {i = 1} ^ {n} l _ {k, i + 1} \leq \sum_ {i = 1} ^ {n} L _ {k, i} ^ {m},
$$

$$
\text { for   } k \in \mathcal {K} \text {   and   } n = 1, \dots , N - 2 \tag {13c}
$$

$$
\sum_ {i = 1} ^ {n} L _ {k, i + 2} ^ {c} \leq O _ {k} \sum_ {i = 1} ^ {n} l _ {k, i + 1},
$$

$$
\text { for   } k \in \mathcal {K} \text {   and   } n = 1, \dots , N - 2 \tag {13d}
$$

$$
\sum_ {n = 1} ^ {N - 2} L _ {k, n} ^ {m} = I _ {k}, \text {   for   } k \in \mathcal {K} \tag {13e}
$$

$$
\sum_ {n = 1} ^ {N - 2} l _ {k, n + 1} = I _ {k}, \text {   for   } k \in \mathcal {K} \tag {13f}
$$

$$
\sum_ {n = 1} ^ {N - 2} L _ {k, n + 2} ^ {c} = O _ {k} I _ {k}, \text {   for   } k \in \mathcal {K} \tag {13g}
$$

$$
L _ {k, n} ^ {m}, l _ {k, n}, L _ {k, n} ^ {c} \geq 0, \text {   for   } k \in \mathcal {K} \text {   and   } n \in \mathcal {N} \tag {13h}
$$

$$
\boldsymbol {p} _ {1} ^ {c} = \boldsymbol {p} _ {I} ^ {c}, \boldsymbol {p} _ {N + 1} ^ {c} = \boldsymbol {p} _ {F} ^ {c}, \tag {13i}
$$

$$
\left\| \boldsymbol {v} _ {n} ^ {c} \right\| \leq v _ {\max}, \text {   for   } n \in \mathcal {N} \tag {13j}
$$

$$
\boldsymbol {v} _ {n} ^ {c} = \frac {\boldsymbol {p} _ {n + 1} ^ {c} - \boldsymbol {p} _ {n} ^ {c}}{\Delta} \text {   for   } n \in \mathcal {N}, \tag {13k}
$$

where ${ \pmb v } _ { n } ^ { c }$ is defined in (13k) (cf. (1)); the energies $E _ { O , k , n } ^ { m } ( \cdot )$ and $E _ { O , k , n } ^ { c } ( \cdot )$ needed for uplink and downlink communication between MU k and cloudlet in (13a) and (13b), respectively, are defined in (6); and E in (13b) represents the UAV energy budget constraint, accounting for offloading and flying. In problem (13), the inequality constraints (13c) and (13d) ensure that the number of bits computed at the $( n + 1 )$ )th frame by the cloudlet is no larger than the number of bits received by the cloudlet in the uplink in the previous n frames, and the number of bits transmitted from the cloudlet in the downlink at the $( n + 2 )$ th frame is no larger than the number of bits available at the cloudlet after computing in the previous $( n + 1 )$ frames, respectively, for the MU $k \in \mathcal { K }$ and $n = 1 , \ldots , N - 2$ . The equality constraints (13e)–(13g) enforce the completion of offloading while (13h) is imposed for the non-negative bit allocations. The constraints (13i) and (13j) guarantee the cloudlet’s initial and final position constraint and maximum speed constraints, respectively.

# B. Successive Convex Approximation

The problem (13) is non-convex due to the non-convex objective function (13a) and non-convex constraint (13b). To tackle this problem without resorting to expensive global optimization methods, we develop an SCA-based algorithm that builds on the inner convex approximation framework proposed in [29], [30]. This approach prescribes the iterative solution of problems in which the non-convex objective function and constraints are replaced by suitable convex approximations. Each problem can be further solved in a distributed manner by using dual decomposition techniques.

In order to develop the SCA-based algorithm, we use the following lemmas.

Lemma 1 ([29, Example 8). Given a non-convex objective function $U ( { \pmb x } ) = f _ { 1 } ( { \pmb x } ) f _ { 2 } ( { \pmb x } )$ , with $f _ { 1 }$ and $f _ { 2 }$ convex and nonnegative, for any y in the domain of $U ( { \pmb x } )$ , a convex approximant of $U ( { \pmb x } )$ that has the properties required by the SCA algorithm [29, Assumption 2] is given as

$$
\begin{array}{l} \bar {U} (\boldsymbol {x}; \boldsymbol {y}) = f _ {1} (\boldsymbol {x}) f _ {2} (\boldsymbol {y}) + f _ {1} (\boldsymbol {y}) f _ {2} (\boldsymbol {x}) \\ + \frac {\tau_ {i}}{2} (\boldsymbol {x} - \boldsymbol {y}) ^ {T} \boldsymbol {H} (\boldsymbol {y}) (\boldsymbol {x} - \boldsymbol {y}), \tag {14} \\ \end{array}
$$

where $\tau _ { i } > 0$ is a positive constant (ensuring that (14) is strongly convex) and $\pmb { H } ( \pmb { y } )$ is a positive definite matrix.

Lemma $2 \ : ( \ : I 2 9 ,$ , Example 4). ] Given a non-convex constraint $g ( \pmb { x } _ { 1 } , \pmb { x } _ { 2 } ) \leq 0$ , where $g ( \pmb { x } _ { 1 } , \pmb { x } _ { 2 } ) = h _ { 1 } ( \pmb { x } _ { 1 } ) h _ { 2 } ( \pmb { x } _ { 2 } )$ is the product of $h _ { 1 }$ and $h _ { 2 }$ convex and non-negative, for any $\left( { \pmb y } _ { 1 } , { \pmb y } _ { 2 } \right)$ in the domain of $g ( \pmb { x } _ { 1 } , \pmb { x } _ { 2 } )$ , a convex approximation that satisfies the conditions [29, Assumption 3] required by the SCA algorithm is given as

$$
\begin{array}{l} \bar {g} (\boldsymbol {x} _ {1}, \boldsymbol {x} _ {2}; \boldsymbol {y} _ {1}, \boldsymbol {y} _ {2}) \\ \triangleq \frac {1}{2} \left(h _ {1} (\boldsymbol {x} _ {1}) + h _ {2} (\boldsymbol {x} _ {2})\right) ^ {2} - \frac {1}{2} \left(h _ {1} ^ {2} (\boldsymbol {y} _ {1}) + h _ {2} ^ {2} (\boldsymbol {y} _ {2})\right) \\ - h _ {1} (\boldsymbol {y} _ {1}) h _ {1} ^ {\prime} (\boldsymbol {y} _ {1}) \left(\boldsymbol {x} _ {1} - \boldsymbol {y} _ {1}\right) - h _ {2} (\boldsymbol {y} _ {1}) h _ {2} ^ {\prime} (\boldsymbol {y} _ {2}) \left(\boldsymbol {x} _ {2} - \boldsymbol {y} _ {2}\right). \tag {15} \\ \end{array}
$$

We recall that, beside technical conditions on continuity and smoothness, the SCA algorithm requires the strongly convex approximation of the objective function to have the same first derivative of the objective function, while the convex approximation of the constraints is required to be tight at the approximation point and to upper bound the original constraints.

To proceed, define the set of primal variables for problem (13) as $z = \{ z _ { n } \} _ { n \in \mathcal { N } }$ with $z _ { n } = ( \{ L _ { k , n } ^ { m } \} _ { k \in \mathcal { K } } ,$ $\{ l _ { k , n } \} _ { k \in \mathcal { K } } , \{ L _ { k , n } ^ { c } \} _ { k \in \mathcal { K } } , { \pmb { p } } _ { n } ^ { c } \big )$ being the optimization variables for the nth frame. We observe that the function $\begin{array} { l } { { E _ { O , k , n } ^ { m } ( z _ { n } ) \triangleq } } \end{array}$ $E _ { O , k , n } ^ { m } \big ( L _ { k , n } ^ { m } , { \pmb { p } } _ { n } ^ { c } \big )$ is the product of two convex and non-negativey

$$
f _ {1} (L _ {k, n} ^ {m}) = \frac {N _ {0} B \Delta / K}{g _ {0}} \left(2 ^ {\frac {L _ {k , n} ^ {m}}{B \Delta / K}} - 1\right) \tag {16a}
$$

and

$$
f _ {2} (\boldsymbol {p} _ {n} ^ {c}) = (x _ {n} ^ {c} - x _ {k} ^ {m}) ^ {2} + (y _ {n} ^ {c} - y _ {k} ^ {m}) ^ {2} + H ^ {2}. \tag {16b}
$$

Then, using Lemma 1 and defining ${ \pmb z } _ { n } ( v ) = ( \{ L _ { k , n } ^ { m } ( v ) \} _ { k \in K } ,$ $\{ l _ { k , n } ( v ) \} _ { k \in \mathcal { K } } , \{ L _ { k , n } ^ { c } ( v ) \} _ { k \in \mathcal { K } } , \pmb { p } _ { n } ^ { c } ( v ) ) \in \mathcal { X }$ for the vth iterate

Algorithm 1: SCA-based algorithm for problem (13) for orthogonal access. 

<table><tr><td>Input:  $z(0) = \{z_n(0)\}_{n \in \mathcal{N}} \in \mathcal{X}$  with  $z_n(0) \triangleq \left( \{L_{k,n}^m(0)\}_{k \in \mathcal{K}}, \{l_{k,n}(0)\}_{k \in \mathcal{K}}, \{L_{k,n}^c(0)\}_{k \in \mathcal{K}}, \boldsymbol{p}_n^c(0) \right)$ , and  $\tau_{L_{k,n}^m}, \tau_{x_n^c}, \tau_{y_n^c} > 0$  for  $k \in \mathcal{K}$  and  $n \in \mathcal{N}$ . Set  $v = 0$ .</td></tr><tr><td>1. If  $z(v)$  is a stationary solution of (13), stop;</td></tr><tr><td>2. Compute  $\hat{\boldsymbol{z}}(\boldsymbol{z}(v))$  using (20);</td></tr><tr><td>3. Set  $z(v+1) = z(v) + \gamma(v)(\hat{\boldsymbol{z}}(\boldsymbol{z}(v)) - \boldsymbol{z}(v))$  for some  $\gamma(v) \in (0,1]$ ;</td></tr><tr><td>4.  $v \leftarrow v+1$  and go to step 1.</td></tr><tr><td>Output:  $\{L_{k,n}^m\}, \{l_{k,n}\}, \{L_{k,n}^c\}$  and  $\{\boldsymbol{p}_n^c\}$ .</td></tr></table>

within the feasible set X of (13), we obtain a strongly convex surrogate function $\bar { E } _ { O , k , n } ^ { m } ( { \pmb z } _ { n } ; { \pmb z } _ { n } ( v ) )$ of $E _ { O , k , n } ^ { m } ( \pmb { z } _ { n } )$ as

$$
\begin{array}{l} \bar {E} _ {O, k, n} ^ {m} \left(\boldsymbol {z} _ {n}; \boldsymbol {z} _ {n} (v)\right) \triangleq \bar {E} _ {O, k, n} ^ {m} \left(L _ {k, n} ^ {m}, \boldsymbol {p} _ {n} ^ {c}; L _ {k, n} ^ {m} (v), \boldsymbol {p} _ {n} ^ {c} (v)\right) \\ = f _ {1} (L _ {k, n} ^ {m}) f _ {2} (\boldsymbol {p} _ {n} ^ {c} (v)) + f _ {1} (L _ {k, n} ^ {m} (v)) f _ {2} (\boldsymbol {p} _ {n} ^ {c}) \\ + \frac {\tau_ {L _ {k , n} ^ {m}}}{2} \left(L _ {k, n} ^ {m} - L _ {k, n} ^ {m} (v)\right) ^ {2} + \frac {\tau_ {x _ {n} ^ {c}}}{2} \left(x _ {n} ^ {c} - x _ {n} ^ {c} (v)\right) ^ {2} \\ + \frac {\tau_ {y _ {n} ^ {c}}}{2} \left(y _ {n} ^ {c} - y _ {n} ^ {c} (v)\right) ^ {2}, \tag {17} \\ \end{array}
$$

where $\tau _ { L _ { k . n } ^ { m } } , \tau _ { x _ { n } ^ { c } } , \tau _ { y _ { n } ^ { c } } > 0 .$

For the non-convex constraint (13b), we derive a convex upper bound using Lemma 2 given that the constraint can be written as the sum of two products of convex functions, namely

$$
E _ {k, n} ^ {c} (\boldsymbol {z} _ {n}) \triangleq E _ {k, n} ^ {c} (l _ {n}) = \frac {\gamma^ {c} C _ {k}}{\Delta^ {2}} g (\boldsymbol {x} _ {1}, \boldsymbol {x} _ {2}) \tag {18a}
$$

and

$$
\begin{array}{l} E _ {O, k, n} ^ {c} (\boldsymbol {z} _ {n}) \triangleq E _ {O, k, n} ^ {c} (L _ {k, n} ^ {c}, \boldsymbol {p} _ {n} ^ {c}) \\ = \frac {N _ {0} B \Delta / K}{g _ {0}} g (\boldsymbol {x} _ {1}, \boldsymbol {x} _ {2}), \tag {18b} \\ \end{array}
$$

where $h _ { 1 } ( { \pmb x } _ { 1 } ) = l _ { k , n }$ and $\begin{array} { r } { h _ { 2 } ( \pmb { x } _ { 2 } ) = ( \sum _ { k ^ { \prime } = 1 } ^ { K } C _ { k ^ { \prime } } l _ { k ^ { \prime } , n } ) ^ { 2 } } \end{array}$ with $\pmb { x } _ { 1 } = l _ { k , n }$ and $\pmb { x } _ { 2 } = l _ { n } = \{ l _ { k ^ { \prime } , n } \} _ { k ^ { \prime } \in \mathcal { K } }$ in (18a), while $h _ { 1 } ( { \pmb x } _ { 1 } ) =$ $2 ^ { \frac { L _ { k , n } ^ { c } } { B \Delta / K } } - 1$ L ck , and $h _ { 2 } ( { \pmb x } _ { 2 } ) = ( x _ { n } ^ { c } - x _ { k } ^ { m } ) ^ { 2 } + ( y _ { n } ^ { c } - y _ { k } ^ { m } ) ^ { 2 } + H ^ { 2 }$ with $\pmb { x } _ { 1 } = { L } _ { k , n } ^ { c }$ and ${ \pmb x } _ { 2 } = { \pmb p } _ { n } ^ { c }$ in (18b). Then, given a possible solution $z _ { n } \left( v \right)$ , we obtain a valid convex upper bound of (13b) by applying (15) as

$$
\begin{array}{l} E _ {k, n + 1} ^ {c} \left(\boldsymbol {z} _ {n + 1}\right) + E _ {O, k, n + 2} ^ {c} \left(\boldsymbol {z} _ {n + 2}\right) \leq \bar {E} _ {k, n + 1} ^ {c} \left(\boldsymbol {z} _ {n + 1}; \boldsymbol {z} _ {n + 1} (v)\right) \\ + \bar {E} _ {O, k, n + 2} ^ {c} (\boldsymbol {z} _ {n + 2}; \boldsymbol {z} _ {n + 2} (v)), \tag {19} \\ \end{array}
$$

where $\bar { E } _ { k . n } ^ { c } \left( { \pmb z } _ { n } ; { \pmb z } _ { n } \left( v \right) \right)$ ) and $\bar { E } _ { O , k , n } ^ { c } ( { \pmb z } _ { n } ; { \pmb z } _ { n } ( v ) )$ are defined in (39) and (41), respectively, in Appendix A, where their derivations are discussed.

Finally, the resulting strongly convex inner approximation of (13), for a given a feasible ${ \pmb z } ( { \boldsymbol v } ) = \{ { \pmb z } _ { n } ( { \boldsymbol v } ) \} _ { n \in \mathcal { N } }$ , is given by

$$
\underset {z} {\text { minimize }} \sum_ {k = 1} ^ {K} \sum_ {n = 1} ^ {N - 2} \bar {E} _ {O, k, n} ^ {m} (z _ {n}; z _ {n} (v)) \tag {20a}
$$

$$
\text { s.t. } \sum_ {k = 1} ^ {K} \sum_ {n = 1} ^ {N - 2} \left(\bar {E} _ {k, n + 1} ^ {c} (\boldsymbol {z} _ {n + 1}; \boldsymbol {z} _ {n + 1} (v)) \right.
$$

$$
+ \bar {E} _ {O, k, n + 2} ^ {c} (\boldsymbol {z} _ {n + 2}; \boldsymbol {z} _ {n + 2} (v)) + \sum_ {n = 1} ^ {N} E _ {F, n} ^ {c} (\boldsymbol {z} _ {n}) \leq \mathcal {E} (2 0 b)
$$

$$
(1 3 \mathrm{c}) - (1 3 \mathrm{k}), \tag {20c}
$$

which has a unique solution denoted by $\hat { \pmb z } ( \pmb z ( v ) )$ . The problem (20) is convex. We note that closed-form solutions could be obtained via dual decomposition by following the approach in [3], but we do not elaborate on this here given that the resulting expressions are rather cumbersome. Using (20), the SCA-based algorithm is summarized in Algorithm 1. The convergence of Algorithm 1 in the sense of [29, Th. 2] is guaranteed if the step size sequence $\{ \gamma ( v ) \}$ is selected such that $\gamma ( v ) \in ( 0 , 1 ]$ , $\gamma ( v )  0$ , and $\textstyle \sum _ { v } \gamma ( v ) = \infty$ . More specifically, the sequence $\{ z ( v ) \}$ is bounded, and every point of its limit points of $z ( \infty )$ is a stationary solution of problem (13). Furthermore, if Algorithm 1 does not stop after a finite number of steps, none of the limit points $z ( \infty )$ is a local minimum of problem (13).

# IV. OPTIMAL ENERGY CONSUMPTION FOR NON-ORTHOGONAL ACCESS

In this section, we discuss the design of bit allocation and UAV trajectory for non-orthogonal access.

# A. Problem Formulation

Using the same definitions as in the previous section, the problem of minimizing the total energy consumption of the MUs is formulated as in (13) by substituting the energies needed for uplink and downlink communication in (13a) and (13b) with (7a) and (7b), respectively. We summarize the resulting problem as

$$
\underset {\{L _ {k, n} ^ {m} \}, \{l _ {k, n} \}, \{L _ {k, n} ^ {c} \}, \{\boldsymbol {p} _ {n} ^ {c} \}} {\text { minimize }} \sum_ {k = 1} ^ {K} \sum_ {n = 1} ^ {N - 2} E _ {N, k, n} ^ {m} (L _ {n} ^ {m}, \boldsymbol {p} _ {n} ^ {c}) \tag {21a}
$$

$$
\text { s.t. } \sum_ {k = 1} ^ {K} \sum_ {n = 1} ^ {N - 2} E _ {k, n + 1} ^ {c} (l _ {n + 1}) + E _ {N, k, n + 2} ^ {c} (L _ {n + 2} ^ {c}, \boldsymbol {p} _ {n + 2} ^ {c})
$$

$$
+ \sum_ {n = 1} ^ {N} E _ {F, n} ^ {c} (\boldsymbol {v} _ {n} ^ {c}) \leq \mathcal {E} \tag {21b}
$$

$$
(1 3 \mathrm{c}) - (1 3 \mathrm{k}). \tag {21c}
$$

# B. Successive Convex Approximation

The problem (21) is non-convex due to the non-convex objective function (21a) and the non-convex constraint (21b). To address this problem, here we propose an SCA-based algorithm, for the reasons discussed in Section III. We start by rewriting the non-convex problem (21) in an equivalent non-convex form by introducing the slack variables $\alpha _ { k , n } \geq 0$ and $\beta _ { k , n } \geq 0$ for $n \in \mathcal N$ and $k \in \mathcal { K }$ as

$$
\underset {\left\{L _ {k, n} ^ {m} \right\}, \left\{l _ {k, n} \right\}, \left\{L _ {k, n} ^ {c} \right\},} {\text { minimize }} \sum_ {k = 1} ^ {K} \sum_ {n = 1} ^ {N - 2} \frac {\alpha_ {k , n}}{g _ {k , n} \left(\boldsymbol {p} _ {n} ^ {c}\right)} \tag {22a}
$$

$$
\{\boldsymbol {p} _ {n} ^ {c} \}, \{\alpha_ {k, n} \}, \{\beta_ {k, n} \}
$$

$$
\text { s.t. } \sum_ {k = 1} ^ {K} \sum_ {n = 1} ^ {N - 2} E _ {k, n + 1} ^ {c} (l _ {n + 1}) + \beta_ {k, n + 2}
$$

$$
+ \sum_ {n = 1} ^ {N} E _ {F, n} ^ {c} (\boldsymbol {v} _ {n} ^ {c}) \leq \mathcal {E} \tag {22b}
$$

$$
g _ {k, n} \left(\boldsymbol {p} _ {n} ^ {c}\right) \hat {E} _ {N, k, n} ^ {m} \left(L _ {k, n} ^ {m}, \boldsymbol {p} _ {n} ^ {c}, \alpha_ {- k, n}\right) \leq \alpha_ {k, n},
$$

$$
\text { for } k \in \mathcal {K} \text { and } n = 1, \dots , N - 2 \tag {22c}
$$

$$
\hat {E} _ {N, k, n + 2} ^ {c} (L _ {k, n + 2} ^ {c}, \boldsymbol {p} _ {n + 2} ^ {c}, \beta_ {- k, n + 2}) \leq \beta_ {k, n + 2},
$$

$$
\text { for } k \in \mathcal {K} \text { and } n = 1, \dots , N - 2 \tag {22d}
$$

$$
\alpha_ {k, n}, \beta_ {k, n} \geq 0, \text {   for   } k \in \mathcal {K} \text {   and   } n \in \mathcal {N} \tag {22e}
$$

$$
(1 3 \mathrm{c}) - (1 3 \mathrm{k}), \tag {22f}
$$

where the uplink and downlink transmission energies in (7a) and (7b) are redefined with slack variables $\alpha _ { - k , n } =$ $\{ \alpha _ { k ^ { \prime } , n } \} _ { k ^ { \prime } \in \mathcal { K } , k ^ { \prime } \ne k }$ and $\beta _ { - k , n } = \{ \beta _ { k ^ { \prime } , n } \} _ { k ^ { \prime } \in \mathcal { K } , k ^ { \prime } \ne k }$ as

$$
\hat {E} _ {N, k, n} ^ {m} (L _ {k, n} ^ {m}, \boldsymbol {p} _ {n} ^ {c}, \alpha_ {- k, n}) = \frac {1}{g _ {k , n} (\boldsymbol {p} _ {n} ^ {c})} \left(N _ {0} B \Delta \right.
$$

$$
\left. + \sum_ {k ^ {\prime} = 1, k ^ {\prime} \neq k} ^ {K} \alpha_ {k ^ {\prime}, n}\right) \left(2 ^ {\frac {L _ {k , n} ^ {m}}{B \Delta}} - 1\right) \tag {23a}
$$

and

$$
\hat {E} _ {N, k, n} ^ {c} (L _ {k, n} ^ {c}, \boldsymbol {p} _ {n} ^ {c}, \beta_ {- k, n}) = \left(\frac {N _ {0} B \Delta}{g _ {k , n} (\boldsymbol {p} _ {n} ^ {c})} \right.
$$

$$
\left. + \sum_ {k ^ {\prime} = 1, k ^ {\prime} \neq k} ^ {K} \beta_ {k ^ {\prime}, n}\right) \left(2 ^ {\frac {L _ {k , n} ^ {c}}{B \Delta}} - 1\right), \tag {23b}
$$

respectively.

In order to tackle the problem (22) via the SCA algorithm [29], [30], as discussed in Section III-B, we need to derive convex approximations for the non-convex objective function (22a) and constraints (22b), (22c) and (22d) according to Lemma 1 and Lemma 2, respectively. To this end, let us define the set of primal variables of problem (22) as $z = \{ z _ { n } \} _ { n \in \mathcal { N } }$ with $z _ { n } = ( \{ L _ { k , n } ^ { m } \} _ { k \in \mathcal { K } } , \{ l _ { k , n } \} _ { k \in \mathcal { K } }$ , $\{ L _ { k , n } ^ { c } \} _ { k \in \mathcal { K } } , \pmb { p } _ { n } ^ { c } , \{ \alpha _ { k , n } \} _ { k \in \mathcal { K } } , \{ \beta _ { k , n } \} _ { k \in \mathcal { K } } \}$ being the optimization variables for the nth frame. The objective function $\alpha _ { k , n } / g _ { k , n } ( \pmb { p } _ { n } ^ { c } )$ in (22a) is the product of one non-negative linear function and one non-negative convex function, namely

$$
f _ {1} (\alpha_ {k, n}) = \frac {\alpha_ {k , n}}{g _ {0}}, \tag {24a}
$$

and

$$
f _ {2} (\boldsymbol {p} _ {n} ^ {c}) = (x _ {n} ^ {c} - x _ {k} ^ {m}) ^ {2} + (y _ {n} ^ {c} - y _ {k} ^ {m}) ^ {2} + H ^ {2}. \tag {24b}
$$

Therefore, using Lemma 1 and ${ \pmb z } _ { n } ( v ) = ( \{ L _ { k , n } ^ { m }$ $( v ) \} _ { k \in \mathcal { K } } , \{ l _ { k , n } ( v ) \} _ { k \in \mathcal { K } } , \{ L _ { k , n } ^ { c } ( v ) \} _ { k \in \mathcal { K } } , \pmb { p } _ { n } ^ { c } ( v ) , \quad \{ \alpha _ { k , n } ( v ) \} _ { k \in \mathcal { K } } .$ $\{ \beta _ { k , n } \left( v \right) \} _ { k \in \mathcal { K } } ) \in \mathcal { X }$ for the vth iterate in the feasible set X of (22), a strongly convex surrogate function $\bar { E } _ { N , k , n } ^ { m } ( { \pmb z } _ { n } ; { \pmb z } _ { n } ( v ) )$ of the objective function $\alpha _ { k , n } / g _ { k , n } ( pmb { p } _ { n } ^ { c } )$ in (22a) is obtained as

$$
\begin{array}{l} \bar {E} _ {N, k, n} ^ {m} (\boldsymbol {z} _ {n}; \boldsymbol {z} _ {n} (v)) \triangleq f _ {1} (\alpha_ {k, n}) f _ {2} (\boldsymbol {p} _ {n} ^ {c} (v)) \\ + f _ {1} (\alpha_ {k, n} (v)) f _ {2} (\boldsymbol {p} _ {n} ^ {c}) \\ + \frac {\tau_ {\alpha_ {k , n}}}{2} \left(\alpha_ {k, n} - \alpha_ {k, n} (v)\right) ^ {2} \\ + \frac {\tau_ {x _ {n} ^ {c}}}{2} \left(x _ {n} ^ {c} - x _ {n} ^ {c} (v)\right) ^ {2} \\ + \frac {\tau_ {y _ {n} ^ {c}}}{2} \left(y _ {n} ^ {c} - y _ {n} ^ {c} (v)\right) ^ {2}, \tag {25} \\ \end{array}
$$

where $\tau _ { \alpha _ { k , n } } , \tau _ { x _ { n } ^ { c } } , \tau _ { y _ { n } ^ { c } } > 0$ , for $k \in \mathcal { K }$ and $n \in \mathcal N .$ .

Moreover, using Lemma 2, the non-convex function $h _ { k , n } ^ { m } ( L _ { k , n } ^ { m } , \alpha _ { - k , n } ) \triangleq g _ { k , n } ( \pmb { p } _ { n } ^ { c } ) \hat { E } _ { N , k , n } ^ { m } ( L _ { k , n } ^ { m } , \pmb { p } _ { n } ^ { c } , \alpha _ { - k , n } )$ in (22c) and $\hat { E } _ { N , k , n } ^ { c } ( L _ { k , n } ^ { c } , \pmb { p } _ { n } ^ { c } , \beta _ { - k , n } )$ in the constraint (22d) can be upper bounded for a given ${ \pmb z } ( { \boldsymbol v } ) = \{ { \pmb z } _ { n } ( { \boldsymbol v } ) \} _ { n \in \mathcal { N } } \in \mathcal { X }$ as

$$
h _ {k, n} ^ {m} (L _ {k, n} ^ {m}, \alpha_ {- k, n}) \leq \bar {h} _ {k, n} ^ {m} (\boldsymbol {z} _ {n}; \boldsymbol {z} _ {n} (v)) \tag {26a}
$$

and

$$
\hat {E} _ {N, k, n} ^ {c} (L _ {k, n} ^ {c}, \boldsymbol {p} _ {n} ^ {c}, \beta_ {- k, n}) \leq \bar {E} _ {N, k, n} ^ {c} (\boldsymbol {z} _ {n}; \boldsymbol {z} _ {n} (v)), \tag {26b}
$$

where $\bar { h } _ { k , n } ^ { m } ( z _ { n } ; z _ { n } ( v ) )$ and $\bar { E } _ { N , k , n } ^ { c } ( z _ { n } ; z _ { n } ( v ) )$ are convex functions calculated by (43) and (45), respectively, in Appendix B, where the details of the derivations are discussed.

By using (25) and (26), given a feasible $z ( v ) \in \mathcal { X }$ , we have a strongly convex inner approximation of (22) as (cf. (20))

$$
\underset {\boldsymbol {z}} {\text { minimize }} \sum_ {k = 1} ^ {K} \sum_ {n = 1} ^ {N - 2} \bar {E} _ {N, k, n} ^ {m} (\boldsymbol {z} _ {n}; \boldsymbol {z} _ {n} (v)) \tag {27a}
$$

$$
\text { s.t. } \sum_ {k = 1} ^ {K} \sum_ {n = 1} ^ {N - 2} \bar {E} _ {k, n + 1} ^ {c} (\boldsymbol {z} _ {n + 1}; \boldsymbol {z} _ {n + 1} (v)) + \beta_ {k, n + 2}
$$

$$
+ \sum_ {n = 1} ^ {N} E _ {F, n} ^ {c} (\boldsymbol {z} _ {n}) \leq \mathcal {E} \tag {27b}
$$

$$
\bar {h} _ {k, n} ^ {m} \left(\boldsymbol {z} _ {n}; \boldsymbol {z} _ {n} (v)\right) \leq \alpha_ {k, n},
$$

$$
\text { for } k \in \mathcal {K} \text { and } n = 1, \dots , N - 2 \tag {27c}
$$

$$
\bar {E} _ {N, k, n + 2} ^ {c} \left(\boldsymbol {z} _ {n + 2}; \boldsymbol {z} _ {n + 2} (v)\right) \leq \beta_ {k, n + 2},
$$

$$
\text { for } k \in \mathcal {K} \text { and } n = 1, \dots , N - 2 \tag {27d}
$$

$$
(2 2 \mathrm{e}), (1 3 \mathrm{c}) - (1 3 \mathrm{k}), \tag {27e}
$$

where $\bar { E } _ { k , n } ^ { c } \left( \pmb { z } _ { n } ; \pmb { z } _ { n } \left( v \right) \right)$ is defined equivalently in (39), which provides a unique solution denoted by $\hat { \pmb z } ( \pmb z ( \eta ) )$ . The SCAbased algorithm is summarized using (27) in Algorithm 2. Its convergence is established by following [29, Th. 2] as discussed in Section III.

Algorithm 2: SCA-based algorithm for problem (22) for non-orthogonal access. 

<table><tr><td>Input:  $z(0) = \{z_n(0)\}_{n \in \mathcal{N}} \in \mathcal{X}$  with  $z_n(0) \triangleq \left( \{L_{k,n}^m(0)\}_{k \in \mathcal{K}}, \{l_{k,n}(0)\}_{k \in \mathcal{K}}, \{L_{k,n}^c(0)\}_{k \in \mathcal{K}}, \boldsymbol{p}_n^c(0), \{\alpha_{k,n}(0)\}_{k \in \mathcal{K}}, \{\beta_{k,n}(0)\}_{k \in \mathcal{K}} \right)$ , and  $\tau_{\alpha_{k,n}}, \tau_{x_n^c}, \tau_{y_n^c} > 0$  for  $k \in \mathcal{K}$  and  $n \in \mathcal{N}$ . Set  $v = 0$ .</td></tr><tr><td>1. If  $z(v)$  is a stationary solution of (22), stop;</td></tr><tr><td>2. Compute  $\hat{z}(z(v))$  using (27);</td></tr><tr><td>3. Set  $z(v+1) = z(v) + \gamma(v)(\hat{z}(z(v)) - z(v))$  for some  $\gamma(v) \in (0,1]$ ;</td></tr><tr><td>4.  $v \leftarrow v+1$  and go to step 1.</td></tr><tr><td>Output:  $\{L_{k,n}^m\}, \{l_{k,n}\}, \{L_{k,n}^c\}, \{\boldsymbol{p}_n^c\}, \{\alpha_{k,n}\}$  and  $\{\beta_{k,n}\}$ .</td></tr></table>

# V. UAV’S PROPULSION ENERGY CONSUMPTION

In the previous sections, we assumed the UAV’s energy consumption model (8) for flying, in which the flying energy depends only on the velocity. In this section, we adopt a more refined model following [16], [26]–[28], in which the propulsion energy of the UAV depends on both the velocity and acceleration vectors. One of the goals of this study is to understand the impact of the energy consumption model on the optimal system design.

Let us denote the UAV’s acceleration vector for the nth frame as ${ \pmb a } _ { n } ^ { c }$ , where

$$
\boldsymbol {a} _ {n} ^ {c} = \frac {\boldsymbol {v} _ {n + 1} ^ {c} - \boldsymbol {v} _ {n} ^ {c}}{\Delta}. \tag {28}
$$

Following [16], [26]–[28], the UAV’s propulsion energy consumption at the nth frame can be modeled as

(Model 2)

$$
E _ {F, n} ^ {c} \left(\boldsymbol {v} _ {n} ^ {c}, \boldsymbol {a} _ {n} ^ {c}\right) = \kappa_ {1} \left\| \boldsymbol {v} _ {n} ^ {c} \right\| ^ {3} + \frac {\kappa_ {2}}{\left\| \boldsymbol {v} _ {n} ^ {c} \right\|} \left(1 + \frac {\left\| \boldsymbol {a} _ {n} ^ {c} \right\| ^ {2}}{g ^ {2}}\right), \tag {29}
$$

where $g$ is gravitational acceleration. A discussion of model (29) can be found along with the values for the constants $\kappa _ { 1 }$ and $\kappa _ { 2 }$ in Appendix C. The velocity vector ${ \pmb v } _ { n } ^ { c }$ and acceleration vector ${ \pmb a } _ { n } ^ { c }$ are related to the UAV’s position ${ \pmb p } _ { n } ^ { c }$ according to the second-order Taylor approximation model

$$
\boldsymbol {p} _ {n + 1} ^ {c} = \boldsymbol {p} _ {n} ^ {c} + \boldsymbol {v} _ {n} ^ {c} \Delta + \frac {1}{2} \boldsymbol {a} _ {n} ^ {c} \Delta^ {2}, \tag {30}
$$

for $n \in { \mathcal { N } } .$

Considering an overall constraint on the UAV energy with (29) in lieu of (8) yields the following optimization problem for

orthogonal access

$$
\underset { \begin{array}{c} \left\{L _ {k, n} ^ {m} \right\}, \left\{l _ {k, n} \right\}, \left\{L _ {k, n} ^ {c} \right\}, \\ \left\{\boldsymbol {p} _ {n} ^ {c} \right\}, \left\{\boldsymbol {v} _ {n} ^ {c} \right\}, \left\{\boldsymbol {a} _ {n} ^ {c} \right\} \end{array} } {\text { minimize }} \sum_ {k = 1} ^ {K} \sum_ {n = 1} ^ {N - 2} E _ {O, k, n} ^ {m} \left(L _ {k, n} ^ {m}, \boldsymbol {p} _ {n} ^ {c}\right) \tag {31a}
$$

$$
\text { s.t. } \sum_ {k = 1} ^ {K} \sum_ {n = 1} ^ {N - 2} E _ {k, n + 1} ^ {c} (l _ {n + 1}) + E _ {O, k, n + 2} ^ {c} (L _ {k, n + 2} ^ {c}, \boldsymbol {p} _ {n + 2} ^ {c})
$$

$$
+ \sum_ {n = 1} ^ {N} E _ {F, n} ^ {c} (\boldsymbol {v} _ {n} ^ {c}, \boldsymbol {a} _ {n} ^ {c}) \leq \mathcal {E} \tag {31b}
$$

$$
\boldsymbol {v} _ {n + 1} ^ {c} = \boldsymbol {v} _ {n} ^ {c} + \boldsymbol {a} _ {n} ^ {c} \Delta , \text {   for   } n \in \mathcal {N} \tag {31c}
$$

$$
\boldsymbol {p} _ {n + 1} ^ {c} = \boldsymbol {p} _ {n} ^ {c} + \boldsymbol {v} _ {n} ^ {c} \Delta + \frac {1}{2} \boldsymbol {a} _ {n} ^ {c} \Delta^ {2}, \text {   for   } n \in \mathcal {N} \tag {31d}
$$

$$
\boldsymbol {v} _ {1} ^ {c} = \boldsymbol {v} _ {N + 1} ^ {c} = \boldsymbol {v} ^ {c} \tag {31e}
$$

$$
\left\| \boldsymbol {a} _ {n} ^ {c} \right\| \leq a _ {\max}, \text {   for   } n \in \mathcal {N} \tag {31f}
$$

$$
(1 3 \mathrm{c}) - (1 3 \mathrm{j}), \tag {31g}
$$

where (31b) is the overall UAV energy constraint; (31e) represents the UAV’s initial and final velocity constraint; and (31f) guarantees a maximum acceleration constraint of $a _ { \mathrm { m a x } }$ . Note that, as compared to (13), problem (31) has the additional optimization variables $\{ \pmb { v } _ { n } ^ { c } \}$ and $\{ { \pmb a } _ { n } ^ { c } \}$ .

To tackle the non-convex problem (31), we apply the SCA approach as above in Section III-B. The key difference with respect to Section III-B is the need to cope with the non-convex function $E _ { F , n } ^ { c } ( \pmb { v } _ { n } ^ { c } , \pmb { a } _ { n } ^ { c } )$ in (31b). To elaborate, we introduce nonnegative slack variables $\left\{ \tau _ { v _ { n } ^ { c } } \geq 0 \right\}$ , and impose the additional constraints $\| \pmb { v } _ { n } ^ { c } \| \geq \tau _ { v _ { n } ^ { c } }$ for $n \in \mathcal N$ . Under these constraints, the propulsion energy consumption $E _ { F , n } ^ { c } ( \pmb { v } _ { n } ^ { c } , \pmb { a } _ { n } ^ { c } )$ in (29) is upper bounded as

$$
\begin{array}{l} E _ {F, n} ^ {c} (\boldsymbol {v} _ {n} ^ {c}, \boldsymbol {a} _ {n} ^ {c}) \leq \kappa_ {1} \| \boldsymbol {v} _ {n} ^ {c} \| ^ {3} + \frac {\kappa_ {2}}{\tau_ {v _ {n} ^ {c}}} + \frac {\kappa_ {2} \| \boldsymbol {a} _ {n} ^ {c} \| ^ {2}}{\tau_ {v _ {n} ^ {c}} g ^ {2}} \\ \triangleq \bar {E} _ {F, n} ^ {c} (\boldsymbol {z} _ {n}; \boldsymbol {z} _ {n} (v)), \tag {32} \\ \end{array}
$$

where the inequality in (32) results from the constraint $\| \pmb { v } _ { n } ^ { c } \| ^ { 2 } \geq$ $\tau _ { v _ { n } ^ { c } } ^ { 2 }$ , yielding the convex upper bound $\bar { E } _ { F , n } ^ { c } \left( { \pmb z } _ { n } ; { \pmb z } _ { n } \left( v \right) \right)$ . In (32), we redefined the set of variables z and $z _ { n } ( v )$ by including the additional variables $\{ \pmb { v } _ { n } ^ { c } \} , \{ \pmb { a } _ { n } ^ { c } \}$ and $\{ \tau _ { v _ { n } ^ { c } } \} \mathrm { a s } z = \{ z _ { n } \} _ { n \in \mathcal { N } }$ with $\boldsymbol { z } _ { n } = ( \{ L _ { k , n } ^ { m } \} _ { k \in \mathcal { K } } , \{ l _ { k , n } \} _ { k \in \mathcal { K } } , \{ L _ { k , n } ^ { c } \} _ { k \in \mathcal { K } } , \boldsymbol { p } _ { n } ^ { c } , \boldsymbol { v } _ { n } ^ { c } , \boldsymbol { a } _ { n } ^ { c } , \tau _ { v _ { n } ^ { c } } )$ ) and as $\boldsymbol { z } _ { n } ( \boldsymbol { v } ) = ( \{ L _ { k , n } ^ { m } ( \boldsymbol { v } ) \} _ { k \in \mathcal { K } } , \{ l _ { k , n } ( \boldsymbol { v } ) \} _ { k \in \mathcal { K } } , \{ L _ { k , n } ^ { c } ( \boldsymbol { v } ) \}$ k∈K, $\pmb { p } _ { n } ^ { c } ( v ) , \pmb { v } _ { n } ^ { c } ( v ) , \pmb { a } _ { n } ^ { c } ( v ) , \tau _ { v _ { n } ^ { c } } ( v ) ) \in \mathcal { X }$ for the vth iterate, where X is the feasible set of problem (31). By using the bound (32), we obtain the convex program to be solved at the vth iteration as

$$
\underset {z} {\text { minimize }} \sum_ {k = 1} ^ {K} \sum_ {n = 1} ^ {N - 2} \bar {E} _ {O, k, n} ^ {m} (z _ {n}; z _ {n} (v)) \tag {33a}
$$

$$
\text { s.t. } \sum_ {k = 1} ^ {K} \sum_ {n = 1} ^ {N - 2} \left(\bar {E} _ {k, n + 1} ^ {c} (z _ {n + 1}; z _ {n + 1} (v)) \right.
$$

$$
+ \bar {E} _ {O, k, n + 2} ^ {c} \left(\boldsymbol {z} _ {n + 2}; \boldsymbol {z} _ {n + 2} (v)\right)) + \sum_ {n = 1} ^ {N} \bar {E} _ {F, n} ^ {c} \left(\boldsymbol {z} _ {n}; \boldsymbol {z} _ {n} (v)\right) \leq \mathcal {E} \tag {33a}
$$

$$
\tau_ {v _ {n} ^ {c}} ^ {2} \leq f ^ {L B} (\boldsymbol {z} _ {n}; \boldsymbol {z} _ {n} (v)), \text {   for   } n \in \mathcal {N} \tag {33b}
$$

$$
\tau_ {v _ {n} ^ {c}} \geq 0, \text {   for   } n \in \mathcal {N} \tag {33c}
$$

$$
(3 1 \mathrm{c}) - (3 1 \mathrm{g}), \tag {33d}
$$

where $f ^ { L B } \left( z _ { n } ; z _ { n } \left( v \right) \right)$ is the linear lower bound on the squared norm $\| \pmb { v } _ { n } ^ { c } \| ^ { 2 }$ as

$$
\begin{array}{l} f ^ {L B} \left(\boldsymbol {z} _ {n}; \boldsymbol {z} _ {n} (v)\right) = \left\| \boldsymbol {v} _ {n} ^ {c} (v) \right\| ^ {2} + 2 \left(\boldsymbol {v} _ {n} ^ {c} (v)\right) ^ {T} \left(\boldsymbol {v} _ {n} ^ {c} - \boldsymbol {v} _ {n} ^ {c} (v)\right) \\ \leq \| \boldsymbol {v} _ {n} ^ {c} \| ^ {2}. \tag {34} \\ \end{array}
$$

The problem (33) is used within Algorithm 1, where (13) and (20) is substituted with (31) and (33), respectively, to yield the proposed SCA solution.

In a similar manner, we can consider non-orthogonal access yielding the problem

$$
\underset { \begin{array}{c} \left\{L _ {k, n} ^ {m} \right\}, \left\{l _ {k, n} \right\}, \left\{L _ {k, n} ^ {c} \right\}, \\ \left\{\boldsymbol {p} _ {n} ^ {c} \right\}, \left\{\boldsymbol {v} _ {n} ^ {c} \right\}, \left\{\boldsymbol {a} _ {n} ^ {c} \right\} \end{array} } {\text {minimize}} \sum_ {k = 1} ^ {K} \sum_ {n = 1} ^ {N - 2} E _ {N, k, n} ^ {m} \left(L _ {n} ^ {m}, \boldsymbol {p} _ {n} ^ {c}\right) \tag {35a}
$$

$$
\text { s.t. } \sum_ {k = 1} ^ {K} \sum_ {n = 1} ^ {N - 2} E _ {k, n + 1} ^ {c} (l _ {n + 1}) + E _ {N, k, n + 2} ^ {c} (L _ {n + 2} ^ {c}, \boldsymbol {p} _ {n + 2} ^ {c})
$$

$$
+ \sum_ {n = 1} ^ {N} E _ {F, n} ^ {c} (\boldsymbol {v} _ {n} ^ {c}, \boldsymbol {a} _ {n} ^ {c}) \leq \mathcal {E} \tag {35b}
$$

$$
(3 1 \mathrm{c}) - (3 1 \mathrm{g}), \tag {35c}
$$

where (35b) is the overall UAV energy constraint. Then, using slack variables $\alpha _ { k , n } \geq 0$ and $\beta _ { k , n } \geq 0$ for $k \in \mathcal { K }$ and $n \in \mathcal N$ as in (22), we can rewrite the problem (35) into

$$
\begin{array}{l} \underset {\{L _ {k, n} ^ {m} \}, \{l _ {k, n} \}, \{L _ {k, n} ^ {c} \}} {\text { minimize }} \sum_ {k = 1} ^ {K} \sum_ {n = 1} ^ {N - 2} \frac {\alpha_ {k , n}}{g _ {k , n} (\boldsymbol {p} _ {n} ^ {c})} \tag {36a} \\ \{\boldsymbol {p} _ {n} ^ {c} \}, \{\boldsymbol {v} _ {n} ^ {c} \}, \{\boldsymbol {a} _ {n} ^ {c} \}, \\ \{\alpha_ {k, n} \}, \{\beta_ {k, n} \} \\ \end{array}
$$

$$
\text { s.t. } \sum_ {k = 1} ^ {K} \sum_ {n = 1} ^ {N - 2} E _ {k, n + 1} ^ {c} (l _ {n + 1}) + \beta_ {k, n + 2}
$$

$$
+ \sum_ {n = 1} ^ {N} E _ {F, n} ^ {c} (\boldsymbol {v} _ {n} ^ {c}, \boldsymbol {a} _ {n} ^ {c}) \leq \mathcal {E} \tag {36b}
$$

$$
(3 1 \mathrm{c}) - (3 1 \mathrm{g}), (2 2 \mathrm{c}) - (2 2 \mathrm{e}). \tag {36c}
$$

This can be tackled using SCA in Algorithm 2 with the following convex problem as

$$
\underset {\boldsymbol {z}} {\text { minimize }} \sum_ {k = 1} ^ {K} \sum_ {n = 1} ^ {N - 2} \bar {E} _ {N, k, n} ^ {m} (\boldsymbol {z} _ {n}; \boldsymbol {z} _ {n} (v)) \tag {37a}
$$

$$
\text { s.t. } \sum_ {k = 1} ^ {K} \sum_ {n = 1} ^ {N - 2} \bar {E} _ {k, n + 1} ^ {c} (\boldsymbol {z} _ {n + 1}; \boldsymbol {z} _ {n + 1} (v)) + \beta_ {k, n + 2}
$$

$$
+ \sum_ {n = 1} ^ {N} \bar {E} _ {F, n} ^ {c} (\boldsymbol {z} _ {n}; \boldsymbol {z} _ {n} (v)) \leq \mathcal {E} \tag {37b}
$$

$$
(3 3 \mathrm{c}) - (3 3 \mathrm{e}), (2 7 \mathrm{c}), (2 7 \mathrm{d}), (2 2 \mathrm{e}), \tag {37c}
$$

in lieu of (22) and (27), respectively, where ${ \pmb z } = \{ { \pmb z } _ { n } \} _ { n \in \mathcal { N } }$ with $z _ { n } = ( \{ L _ { k , n } ^ { m } \} _ { k \in K } , \{ l _ { k , n } \} _ { k \in K } , \quad \{ L _ { k , n } ^ { c } \} _ { k \in K } , \mathbf { \Phi } _ { { n } } ^ { c } , \mathbf { \Phi } _ { { n } } ^ { c } , \mathbf { a } _ { n } ^ { c }$ , $\begin{array} { r } { \{ \alpha _ { k , n } \} _ { k \in \mathcal { K } } , \{ \beta _ { k , n } \} _ { k \in \mathcal { K } } , \tau _ { v _ { n } ^ { c } } ) ; z _ { n } ( v ) = ( \{ L _ { k , n } ^ { m } ( v ) \} _ { k \in \mathcal { K } } , \{ l _ { k , n } \} _ { k } ) } \end{array}$ $( v ) \} _ { k \in \mathcal { K } } , \ \{ L _ { k , n } ^ { c } ( v ) \} _ { k \in \mathcal { K } } , \ p _ { n } ^ { c } ( v ) , \pmb { v } _ { n } ^ { c } ( v ) , \ \pmb { a } _ { n } ^ { c } ( v ) , \ \{ \alpha _ { k , n } ( v ) \} _ { k \in \mathcal { K } } $ }k∈K, $\{ \beta _ { k , n } ( v ) \} _ { k \in \mathcal { K } } , ~ \tau _ { v _ { n } ^ { c } } ( v ) ) ~ \in \mathcal { X }$ with the feasible set X ; and $E _ { F , n } ^ { c } ( \pmb { v } _ { n } ^ { c } , \pmb { a } _ { n } ^ { c } )$ and $\because z _ { F , n } ^ { c } ( z _ { n } ; z _ { n } ( v ) )$ ) are defined in (29) and (32), respectively.

# VI. NUMERICAL RESULTS

In this section, we evaluate the performance of the proposed optimization algorithm over bit allocation and UAV’s trajectory via numerical experiments. We will consider both the results of the optimization studied in Sections III and IV in which the UAV energy for flying is given by (8) (Model 1) or (29) (Model 2). Furthermore, for reference, we consider the following schemes: (i) No optimization: With this scheme, the same number of bits is transmitted in uplink and downlink in each frame, the same number of bits is computed at the cloudlet at each frame, and the cloudlet flies at constant velocity between the initial and final positions, i.e., $L _ { k , n } ^ { m } =$ $l _ { k , n + 1 } = I _ { k } / ( N - 2 )$ and $L _ { k . n + 2 } ^ { c } = I _ { k } O _ { k } / ( N - 2 )$ for $k \in \mathcal { K }$ and $n = 1 , \ldots , N - 2$ , and $x _ { n } ^ { c } = x _ { I } ^ { c } + ( n - 1 ) ( x _ { F } ^ { c } - x _ { I } ^ { c } ) / N$ and $y _ { n } ^ { c } = y _ { I } ^ { c } + ( n - 1 ) ( y _ { F } ^ { c } - y _ { I } ^ { c } ) / N$ for $n \in \mathcal N ; ( i i )$ Optimized bit allocation: With this scheme, the optimized number of bits is transmitted in each uplink and downlink frame and computed at the cloudlet by the proposed algorithms while keeping the described constant-velocity cloudlet’s trajectory; (iii) Optimized UAV’s trajectory: With this scheme, the cloudlet flies along the optimized trajectory between the initial and final positions as obtained by the proposed algorithms with fixed equal bit allocation in each frame. The UAV’s initial and final velocity constraint for Model 2 is set to be ${ \pmb v } ^ { c } = \| { \pmb v } ^ { c } \| ( { \pmb p } _ { F } ^ { c } - { \pmb p } _ { I } ^ { c } ) / \| { \pmb p } _ { F } ^ { c } -$ $\pmb { p } _ { I } ^ { c } \mathinner { | { | { \bf { \mu } } } \rangle }$ , where $\| \pmb { v } ^ { c } \| \le v _ { \operatorname* { m a x } }$ is its initial and final speed. The remaining parameters used in the simulations, unless specified otherwise, are summarized in Table II, where $\kappa _ { 1 }$ and $\kappa _ { 2 }$ are set for Model 2 by considering the fixed-wing UAV’s parameters.

As shown in Fig. 3, in the first scenario under study, there are K = 3 MUs located at positions $\pmb { p } _ { 1 } ^ { m } = ( 0 , 1 0 , 0 ) , \pmb { p } _ { 2 } ^ { m } =$ (10, 10, 0) and $\pmb { p } _ { 3 } ^ { m } = ( 1 0 , 0 , 0 )$ , while the initial and final positions of the cloudlet are $\pmb { p } _ { I } ^ { c } = ( 0 , 0 ) \mathrm { t o } \pmb { p } _ { F } ^ { c } = ( 5 , 0 )$ , respectively, with the UAV’s initial speed $\lVert \pmb { v } ^ { c } \rVert = 2 . 2 2$ m/s. The numbers of bits to be offloaded in the uplink from the MUs are assumed to be $I _ { 1 } = 4 \ : \mathrm { M b i t s }$ , $I _ { 2 } = 6$ Mbits and $I _ { 3 } = 2 ~ \mathrm { M b i t s }$ . The

TABLE II SIMULATION PARAMETERS 

<table><tr><td>Parameter</td><td>Value</td><td>Parameter</td><td>Value</td></tr><tr><td> $B$ </td><td>40 MHz</td><td> $N_0$ </td><td>-174 dBm/Hz</td></tr><tr><td> $\gamma_k^m, \gamma^c$ </td><td> $10^{-28}$  [32], [33]</td><td> $O_k$ </td><td>0.5</td></tr><tr><td> $C_k$ </td><td>1550.7 (95th percentile of random  $C_k$  in [32], [33])</td><td> $H$ </td><td>5 m</td></tr><tr><td> $\mathcal{E}$ </td><td>500 kJ</td><td> $g$ </td><td>9.8 m/s $^2$ </td></tr><tr><td> $v_{\text{max}}$ </td><td>50 m/s</td><td> $a_{\text{max}}$ </td><td>30 m/s $^2$ </td></tr><tr><td> $\Delta$ </td><td>45 ms</td><td> $M$ </td><td>9.65 kg</td></tr><tr><td> $\rho$ </td><td>1.225 kg/m $^3$ </td><td> $C_{D_0}$ </td><td>0.0355</td></tr><tr><td> $S_r$ </td><td>3.77 m $^2$ </td><td> $e_0$ </td><td>0.85</td></tr><tr><td> $A_R$ </td><td>13</td><td> $\kappa$ </td><td>0.2171</td></tr><tr><td> $\kappa_1$ </td><td>0.0037</td><td> $\kappa_2$ </td><td>5.0206</td></tr></table>

![](images/4e154d7aaef2395730aa6d984c9a76f843cbf93d13427e6b7f64ac2cc459a06d.jpg)

<details>
<summary>line</summary>

| x (m) | y (m) - Optimized UAV's trajectory (Model 1) | y (m) - Optimized UAV's trajectory (Model 2) |
|-------|-----------------------------------------------|-----------------------------------------------|
| 0     | 0                                             | 0                                             |
| 1     | 3                                             | 3                                             |
| 2     | 3.5                                           | 3.5                                           |
| 3     | 4                                             | 4.5                                           |
| 4     | 4.5                                           | 5                                             |
| 5     | 4.5                                           | 5.5                                           |
| 6     | 4.5                                           | 5                                             |
| 7     | 4.5                                           | 4.5                                           |
| 8     | 4.5                                           | 4.5                                           |
| 9     | 4.5                                           | 4.5                                           |
| 10    | 4.5                                           | 4.5                                           |
</details>

Fig. 3. Position of the MUs and optimized UAV’s trajectory for orthogonal access with Algorithm 1 $( K = 3 , \dot { T } = 2 . 2 5 \mathrm { ~ s } , \left( I _ { 1 } , I _ { 2 } , \dot { I } _ { 3 } \right) = \dot { ( 4 , 6 , 2 ) }$ Mbits, $\pmb { p } _ { 1 } ^ { m } = ( 0 , 1 0 , 0 )$ m, pm2 = (10, 10, 0) m, $\pmb { p } _ { 3 } ^ { m } = ( 1 0 , 0 , 0 ) ~ \mathrm { m } , \pmb { p } _ { I } ^ { c } = ( 0 , 0 )$ m, ${ \pmb p } _ { F } ^ { \hat { c } } = ( 5 , 0 )$ ) m and the reference SNR $g _ { 0 } / \bar { ( N _ { 0 } B ) } = - 5 \mathrm { d B } )$ .

latency constraint is $T = 2 . 2 5 \mathrm { s } ,$ or $N = 5 0$ with the parameters in Table II, and the reference SNR $g _ { 0 } / ( N _ { 0 } B ) = - 5 \mathrm { d B }$ .

Fig. 3 shows the optimized trajectories obtained for orthogonal access under both UAV’s flying energy consumption models. The same qualitative behavior was observed for non-orthogonal access with Algorithm 2 (not reported here). Fig. 3 shows that, under both models, the UAV tends to stay longer near MU 2, which has the largest number of input bits to offload. However, when including the UAV’s propulsion energy consumption as in Model 2, the trajectory tends to turn smoothly compared to Model 1 in order to limit the energy consumption caused by accelerations. This demonstrates the impact of the energy consumption model on the optimal system design.

For the same example, Fig. 4 shows the optimized bit allocation for the UAV trajectory in Fig. 3 that is attained under Model 2. A similar trend is observed also under Model 1 (not shown here). It is seen that, when the UAV is closer to an MU k, a larger number $\{ L _ { k , n } ^ { m } \}$ of bits for uplink transmission is allocated for MU k. Moreover, the bit allocation $\{ l _ { k , n } \}$ for computation and $\{ L _ { k , n } ^ { c } \}$ for downlink transmission are constrained by the number of bits received in the uplink and on the output bits obtained as a result of computing, respectively. Finally, the downlink bit allocation $\{ L _ { k , n } ^ { c } \}$ is seen to be less affected by the k,n cloudlet’s position compared to the uplink bit allocation $\{ L _ { k , n } ^ { m } \}$ since the algorithm does not attempt to minimize UAV’s energy consumption but it only imposes the UAV energy budget at the cloudlet.

![](images/f9019abea08ea4203903f9de3b8cd28cf76f4a43f808f2fd3d4e62a018eac758.jpg)

<details>
<summary>line</summary>

| Slot n | L_k,n^m (×10⁵) | l_k,n (×10⁵) | L_k,n^c (×10⁵) |
| ------ | -------------- | ------------ | -------------- |
| 1      | 0              | 0            | 0              |
| 5      | 0              | 0            | 0              |
| 10     | 0              | 0            | 0              |
| 15     | 2              | 1            | 0              |
| 20     | 2              | 1            | 0              |
| 25     | 2              | 1            | 0              |
| 30     | 2              | 1            | 0              |
| 35     | 0              | 1            | 0              |
| 40     | 0              | 1            | 0              |
| 45     | 0              | 1            | 0              |
| 50     | 0              | 4            | 4              |
</details>

![](images/27c5a415a5f79e2556f449d543ca0b7863eb39184f078abc6e35030a8a4481cc.jpg)

<details>
<summary>line</summary>

| Slot n | L_k,n^m | l_k,n | L_k,n^c |
| ------ | ------- | ----- | ------- |
| 1      | 0       | 0     | 0       |
| 5      | 0       | 0     | 0       |
| 10     | 0       | 0     | 0       |
| 15     | 0       | 0     | 0       |
| 20     | 0       | 0     | 0       |
| 25     | 2       | 1     | 0       |
| 30     | 4       | 2     | 0       |
| 35     | 4       | 3     | 0       |
| 40     | 2       | 3     | 0       |
| 45     | 0       | 3     | 2       |
| 50     | 0       | 8     | 8       |
</details>

![](images/642fcfae60e7f85db09437bc98e2c07168b5fa13c5db66de16258e3532473ec3.jpg)

<details>
<summary>line</summary>

| Slot n | L_k,n^m | l_k,n | L_k,n^c |
| ------ | ------- | ----- | ------- |
| 1      | 0       | 0     | 0       |
| 5      | 0       | 0     | 0       |
| 10     | 0       | 0     | 0       |
| 15     | 0       | 0     | 0       |
| 20     | 0       | 0     | 0       |
| 25     | 0       | 0     | 0       |
| 30     | 0       | 0     | 0       |
| 35     | 0       | 0     | 0       |
| 40     | 2.0e5   | 1.5e5 | 0.5e5   |
| 45     | 1.5e5   | 2.0e5 | 1.0e5   |
| 50     | 0       | 4.0e5 | 4.5e5   |
</details>

Fig. 4. Optimized bit allocation for the UAV trajectory under Model 2 in Fi $\bar { \mathsf { g } } . 3 ( K \bar { = } 3 , T = 2 . 2 5 \mathsf { s } , \left( I _ { 1 } , I _ { 2 } , I _ { 3 } \right) = ( 4 , 6 , 2 )$ Mbits, $\pmb { p } _ { 1 } ^ { m } = ( 0 , 1 0 , 0 )$ m, $\pmb { p } _ { 2 } ^ { m } = ( 1 0 , 1 0 , 0 )$ m, $\pmb { p } _ { 3 } ^ { m } = ( 1 0 , 0 , 0 )$ m, $\pmb { p } _ { I } ^ { c } = ( 0 , 0 )$ m, ${ \pmb p } _ { F } ^ { \dot { c } } = ( 5 , 0 )$ m and the reference SNR $g _ { 0 } \bar { / } ( N _ { 0 } B ) = - 5 \mathrm { d B } )$ .

Fig. 5 compares the average total energy consumptions (10) for mobile execution with the mobile energy needed for offloading using orthogonal and non-orthogonal access as a function of the deadline $T$ under Model 1. For this experiment, we have K = 2 MUs with input bits $I _ { 1 } = I _ { 2 } = 8$ Mbits that are uniformly distributed in a $1 0 \times 1 0 ~ \mathrm { m } ^ { 2 }$ square region. We assume the initial and final position of cloudlet as $\pmb { p } _ { I } ^ { c } = ( 0 , 0 )$ and ${ \pmb p } _ { F } ^ { c } = ( 0 , 8 )$ , respectively. The energy shown in Fig. 5 is averaged with respect to the MUs’ locations. The reference SNR $g _ { 0 } / ( N _ { 0 } B )$ is set to be −2.5 dB. From Fig. 5, we first observe that as the deadline $T$ becomes more stringent, the energy savings of cloudlet offloading become more prominent compared with respect to mobile execution given that mobile computing energy grows as $T ^ { - 2 }$ as per (10) while the mobile energy with offloading decreases more slowly with T . Furthermore, we note the significant gains obtained by means of joint optimization of trajectory and bit allocation. For instance, for $T = 2 . 7 ~ \mathrm { s } ,$ , the proposed scheme requires an average total MUs’ energy consumption of 36.8 J for orthogonal access and 29.9 J for non-orthogonal access, whereas the non-optimized systems with equal bit allocation and constant-velocity cloudlet trajectory requires 43.1 J and 44.3 J, respectively, which implies a 14.5% and 32.7% decrease on the mobile energy consumption. The larger gain for non-orthogonal access can be attributed to the dependence of its performance on the mutual interference among MUs, which is affected by bit allocation. Also, optimizing the trajectory is seen to be more advantageous than optimizing only the bit allocation. For instance, of the mentioned 32.7% decrease in energy with non-orthogonal access, 27.4% can be obtained by optimizing only the trajectory, while 2% is achieved by optimizing only the bit allocation. Finally, upon optimization, non-orthogonal access is preferred to the orthogonal access unless $T$ is small. This can be explained since a shorter deadline T requires a larger energy consumption, which renders the performance of nonorthogonal access interference-limited. Note that if the deadline $T$ is not enough long for the UAV to fly from its initial to final location under its maximum velocity constraint, the offloading becomes infeasible (cf. (3)).

![](images/8669c9edf4ae0cdd54bb805cd541d6a820f0a7f45d952f4b728ad26b3f6d2477.jpg)

<details>
<summary>line</summary>

| Deadline T (s) | Nonorthogonal | Orthogonal | No opt. | Opt. bit allocation | Opt. trajectory | Opt. trajectory and bit allocation |
| -------------- | ------------- | ---------- | ------- | ------------------- | --------------- | ---------------------------------- |
| 0.54           | 70            | 53         | 70      | 68                  | 65              | 62                                 |
| 0.9            | 55            | 48         | 55      | 52                  | 50              | 48                                 |
| 1.2            | 48            | 45         | 48      | 45                  | 42              | 38                                 |
| 1.5            | 45            | 43         | 45      | 42                  | 38              | 35                                 |
| 1.8            | 43            | 42         | 43      | 40                  | 36              | 33                                 |
| 2.1            | 42            | 41         | 42      | 39                  | 35              | 32                                 |
| 2.4            | 41            | 40         | 41      | 38                  | 34              | 31                                 |
| 2.7            | 40            | 39         | 40      | 37                  | 33              | 30                                 |
</details>

Fig. 5. Average total energy consumption of the MUs as a function of the deadline T under Model 1 when the MUs are uniformly distributed in $\mathrm { ~ a ~ } 1 0 \times$ 10 $\mathrm { m } ^ { 2 }$ square region $( K = 2 , ( I _ { 1 } , I _ { 2 } ) = ( 8 , 8 )$ Mbits, $\pmb { p } _ { I } ^ { c } = ( 0 , 0 )$ m, ${ \pmb { p } } _ { F } ^ { c } =$ (0, 8) m and the reference SNR $g _ { 0 } / ( N _ { 0 } B ) = - 2 . 5 \ : \mathrm { d B } )$ .

# VII. CONCLUDING REMARKS

In this paper, we studied a mobile cloud computing architecture based on a UAV-mounted cloudlet which provides the offloading opportunities to multiple static mobile devices. Two types of access schemes, namely orthogonal access and nonorthogonal access, were considered for the uplink and downlink transmissions required for the offloading procedure. We tackled the minimization of the mobile energy over the bit allocation for uplink, downlink and computation as well as over the UAV’s trajectory for both access schemes by means of successive convex approximation methods. Numerical results verify the significant mobile energy savings of the proposed joint optimization of bit allocation and cloudlet’s trajectory as compared to local mobile execution, as well as to partial optimization approaches that design only the bit allocation or the cloudlet’s trajectory. They also point to the importance of acquiring accurate energy consumption models for the UAV. Interesting open problems concern the generalization of the optimization studied here to multiple moving interfering mobile devices and to trajectories with a variable altitude.

# APPENDIX A DERIVATIONS OF (19)

In this appendix, for a given $z ( v ) \in \mathcal { X }$ with the feasible set X of problem (13), we derive the convex upper bounds $\bar { E } _ { k , n } ^ { c } \left( \pmb { z } _ { n } ; \pmb { z } _ { n } \left( v \right) \right)$ and $\bar { E } _ { O , k , n } ^ { c } ( { \pmb z } _ { n } ; { \pmb z } _ { n } ( v ) )$ of non-convex funck,n tions $E _ { k , n } ^ { c } ( \pmb { z } _ { n } )$ and $E _ { O , k , n } ^ { c } ( { \pmb z } _ { n } )$ , respectively, in (13b) by following Lemma 2.

The computing energy consumption $E _ { k , n } ^ { c } ( \pmb { z } _ { n } )$ of MU k can be first rewritten as

$$
\begin{array}{l} E _ {k, n} ^ {c} \left(\boldsymbol {z} _ {n}\right) = \frac {\gamma^ {c} C _ {k}}{\Delta^ {2}} \left[ \frac {1}{2} \left(l _ {k, n} + \left(\sum_ {k ^ {\prime} = 1} ^ {K} C _ {k ^ {\prime}} l _ {k ^ {\prime}, n}\right) ^ {2}\right) ^ {2} \right. \\ \left. - \frac {1}{2} \left(\left(l _ {k, n}\right) ^ {2} + \left(\sum_ {k ^ {\prime} = 1} ^ {K} C _ {k ^ {\prime}} l _ {k ^ {\prime}, n}\right) ^ {4}\right) \right], \tag {38} \\ \end{array}
$$

which leads to the convex upper bound of $E _ { k , n } ^ { c } ( { \pmb z } _ { n } )$ around $z _ { n } ( v )$ as

$$
\bar {E} _ {k, n} ^ {c} (\boldsymbol {z} _ {n}; \boldsymbol {z} _ {n} (v)) \triangleq E _ {k, n} ^ {c} (l _ {n}; l _ {n} (v))
$$

$$
= \frac {\gamma^ {c} C _ {k}}{2 \Delta^ {2}} \left[ \left(l _ {k, n} + \left(\sum_ {k ^ {\prime} = 1} ^ {K} C _ {k ^ {\prime}} l _ {k ^ {\prime}, n}\right) ^ {2}\right) ^ {2} \right.
$$

$$
\left. - \left(l _ {k, n} (v)\right) ^ {2} - \left(\sum_ {k ^ {\prime} = 1} ^ {K} C _ {k ^ {\prime}} l _ {k ^ {\prime}, n} (v)\right) ^ {4} \right]
$$

$$
- \frac {\gamma^ {c} C _ {k}}{\Delta^ {2}} \left[ l _ {k, n} (v) \left(l _ {k, n} - l _ {k, n} (v)\right) + 2 \left(\sum_ {k ^ {\prime} = 1} ^ {K} C _ {k ^ {\prime}} l _ {k ^ {\prime}, n} (v)\right) ^ {3} \right.
$$

$$
\left. \times \left(\sum_ {k ^ {\prime} = 1} ^ {K} C _ {k ^ {\prime}} (l _ {k ^ {\prime}, n} - l _ {k ^ {\prime}, n} (v))\right) \right]. \tag {39}
$$

Similarly, we can rewrite the downlink communication energy consumption $E _ { O , k , n } ^ { c } ( { \pmb z } _ { n } )$ as

$$
\begin{array}{l} E _ {O, k, n} ^ {c} (\boldsymbol {z} _ {n}) = \frac {N _ {0} B \Delta / K}{g _ {0}} \left[ \frac {1}{2} \left(2 ^ {\frac {L _ {k , n} ^ {c}}{B \Delta / K}} - 1 \right. \right. \\ \left. + \left(x _ {n} ^ {c} - x _ {k} ^ {m}\right) ^ {2} + \left(y _ {n} ^ {c} - y _ {k} ^ {m}\right) ^ {2} + H ^ {2}\right) ^ {2} - \frac {1}{2} \left(\left(2 ^ {\frac {L _ {k , n} ^ {c}}{B \Delta / K}} - 1\right) ^ {2} \right. \\ \left. \left. + \left(\left(x _ {n} ^ {c} - x _ {k} ^ {m}\right) ^ {2} + \left(y _ {n} ^ {c} - y _ {k} ^ {m}\right) ^ {2} + H ^ {2}\right) ^ {2}\right) \right]. \tag {40} \\ \end{array}
$$

Then, the desired convex upper bound of $E _ { O , k , n } ^ { c } ( z _ { n } )$ around $z _ { n } ( v )$ can then be obtained as

$$
\begin{array}{l} \bar {E} _ {O, k, n} ^ {c} \left(\boldsymbol {z} _ {n}; \boldsymbol {z} _ {n} (v)\right) \triangleq E _ {O, k, n} ^ {c} \left(L _ {k, n} ^ {c}, \boldsymbol {p} _ {n} ^ {c}; L _ {k, n} ^ {c} (v), \boldsymbol {p} _ {n} ^ {c} (v)\right) \\ = \frac {N _ {0} B \Delta / K}{2 g _ {0}} \left[ \left(2 ^ {\frac {L _ {k , n} ^ {c}}{B \Delta / K}} - 1 \right. \right. \\ \left. + (x _ {n} ^ {c} - x _ {k} ^ {m}) ^ {2} + (y _ {n} ^ {c} - y _ {k} ^ {m}) ^ {2} + H ^ {2}\right) ^ {2} - \left(2 ^ {\frac {L _ {k , n} ^ {c} (v)}{B \Delta / K}} - 1\right) ^ {2} \\ \left. - \left(\left(x _ {n} ^ {c} (v) - x _ {k} ^ {m}\right) ^ {2} + \left(y _ {n} ^ {c} (v) - y _ {k} ^ {m}\right) ^ {2} + H ^ {2}\right) ^ {2} \right] \\ - \frac {N _ {0} \ln 2}{g _ {0}} 2 ^ {\frac {L _ {k , n} ^ {c} (v)}{B \Delta / K}} \left(2 ^ {\frac {L _ {k , n} ^ {c} (v)}{B \Delta / K}} - 1\right) \left(L _ {k, n} ^ {c} - L _ {k, n} ^ {c} (v)\right) \\ - \frac {2 N _ {0} B \Delta / K}{g _ {0}} \left(\left(x _ {n} ^ {c} (v) - x _ {k} ^ {m}\right) ^ {2} + \left(y _ {n} ^ {c} (v) - y _ {k} ^ {m}\right) ^ {2} + H ^ {2}\right) \\ \end{array}
$$

$$
\left(\left(x _ {n} ^ {c} (v) - x _ {k} ^ {m}\right) \left(x _ {n} ^ {c} - x _ {n} ^ {c} (v)\right) + \left(y _ {n} ^ {c} (v) - y _ {k} ^ {m}\right) \left(y _ {n} ^ {c} - y _ {n} ^ {c} (v)\right)\right). \tag {41}
$$

# APPENDIX B DERIVATIONS OF (26)

Here, for a given $z ( v ) \in \mathcal { X }$ with the feasible set X of problem (22), we derive the convex upper bounds of $h _ { k , n } ^ { m } ( { \pmb z } _ { n } ; { \pmb z } _ { n } ( v ) )$ and $\hat { E } _ { N , k , n } ^ { c } ( z _ { n } ; z _ { n } ( v ) )$ in (26) similarly with Appendix A based on

We can rewrite the non-convex function $h _ { k , n } ^ { m } \left( L _ { k , n } ^ { m } , \alpha _ { - k , n } \right)$ of (22c) as

$$
\begin{array}{l} h _ {k, n} ^ {m} (\boldsymbol {z} _ {n}) \triangleq h _ {k, n} ^ {m} (L _ {k, n} ^ {m}, \alpha_ {- k, n}) = N _ {0} B \Delta \left(2 ^ {\frac {L _ {k , n} ^ {m}}{B \Delta}} - 1\right) \\ + \frac {1}{2} \left(2 ^ {\frac {L _ {k , n} ^ {m}}{B \Delta}} - 1 + \sum_ {k ^ {\prime} = 1, k ^ {\prime} \neq k} ^ {K} \alpha_ {k ^ {\prime}, n}\right) ^ {2} \\ - \frac {1}{2} \left(\left(2 ^ {\frac {L _ {k , n} ^ {m}}{B \Delta}} - 1\right) ^ {2} + \left(\sum_ {k ^ {\prime} = 1, k ^ {\prime} \neq k} ^ {K} \alpha_ {k ^ {\prime}, n}\right) ^ {2}\right), \tag {42} \\ \end{array}
$$

whose convex upper bound is given as

$$
\begin{array}{l} \bar {h} _ {k, n} ^ {m} \left(\boldsymbol {z} _ {n}; \boldsymbol {z} _ {n} (v)\right) \triangleq \bar {h} _ {k, n} ^ {m} \left(L _ {k, n} ^ {m}, \alpha_ {- k, n}; L _ {k, n} ^ {m} (v), \alpha_ {- k, n} (v)\right) \\ = N _ {0} B \Delta \left(2 ^ {\frac {L _ {k , n} ^ {m}}{B \Delta}} - 1\right) \\ + \frac {1}{2} \left[ \left(2 ^ {\frac {L _ {k , n} ^ {m}}{B \Delta}} - 1 + \sum_ {k ^ {\prime} = 1, k ^ {\prime} \neq k} ^ {K} \alpha_ {k ^ {\prime}, n}\right) ^ {2} - \left(2 ^ {\frac {L _ {k , n} ^ {m} (v)}{B \Delta}} - 1\right) ^ {2} \right. \\ \left. - \left(\sum_ {k ^ {\prime} = 1, k ^ {\prime} \neq k} ^ {K} \alpha_ {k ^ {\prime}, n} (v)\right) ^ {2} \right] \\ \end{array}
$$

$$
\begin{array}{l} - \frac {\ln 2}{B \Delta} 2 ^ {\frac {L _ {k , n} ^ {m} (v)}{B \Delta}} \left(2 ^ {\frac {L _ {k , n} ^ {m} (v)}{B \Delta}} - 1\right) \left(L _ {k, n} ^ {m} - L _ {k, n} ^ {m} (v)\right) \\ - \left(\sum_ {k ^ {\prime} = 1, k ^ {\prime} \neq k} ^ {K} \alpha_ {k ^ {\prime}, n} (v)\right) \left(\sum_ {k ^ {\prime} = 1, k ^ {\prime} \neq k} ^ {K} \alpha_ {k ^ {\prime}, n} - \alpha_ {k ^ {\prime}, n} (v)\right) \tag {43} \\ \end{array}
$$

Similarly, the non-convex function $\hat { E } _ { N , k , n } ^ { c } \big ( L _ { k , n } ^ { c } , \pmb { p } _ { n } ^ { c } , \beta _ { - k , n } \big )$ in the constraint (22d) can be expressed as

$$
\begin{array}{l} \hat {E} _ {N, k, n} ^ {c} (\boldsymbol {z} _ {n}) \triangleq \hat {E} _ {N, k, n} ^ {c} (L _ {k, n} ^ {c}, \boldsymbol {p} _ {n} ^ {c}, \beta_ {- k, n}) \\ = \frac {1}{2} \left[ \frac {N _ {0} B \Delta}{g _ {0}} \left(2 ^ {\frac {L _ {k , n} ^ {c}}{B \Delta}} - 1 + (x _ {n} ^ {c} - x _ {k} ^ {m}) ^ {2} \right. \right. \\ \left. \left. + \left(y _ {n} ^ {c} - y _ {k} ^ {m}\right) ^ {2} + H ^ {2}\right) ^ {2} + \left(2 ^ {\frac {L _ {k , n} ^ {c}}{B \Delta}} - 1 + \sum_ {k ^ {\prime} = 1, k ^ {\prime} \neq k} ^ {K} \beta_ {k ^ {\prime}, n}\right) ^ {2} \right] \\ - \frac {1}{2} \left[ \left(\frac {N _ {0} B \Delta}{g _ {0}} + 1\right) \left(2 ^ {\frac {L _ {k , n} ^ {c}}{B \Delta}} - 1\right) ^ {2} + \left(\sum_ {k ^ {\prime} = 1, k ^ {\prime} \neq k} ^ {K} \beta_ {k ^ {\prime}, n}\right) ^ {2} \right. \\ \left. + \frac {N _ {0} B \Delta}{g _ {0}} \left(\left(x _ {n} ^ {c} - x _ {k} ^ {m}\right) ^ {2} + \left(y _ {n} ^ {c} - y _ {k} ^ {m}\right) ^ {2} + H ^ {2}\right) ^ {2} \right], \tag {44} \\ \end{array}
$$

which is upper bounded by the convex surrogate function to linearize the concave parts of $\hat { E } _ { N , k , n } ^ { c } ( { \pmb z } _ { n } )$ as

$$
\begin{array}{l} \bar {E} _ {N, k, n} ^ {c} (\pmb {z} _ {n}; \pmb {z} _ {n} (v)) \\ \triangleq \bar {E} _ {N, k, n} ^ {c} (L _ {k, n} ^ {c}, \boldsymbol {p} _ {n} ^ {c}, \beta_ {- k, n}; L _ {k, n} ^ {c} (v), \boldsymbol {p} _ {n} ^ {c} (v), \beta_ {- k, n} (v)) \\ = \frac {1}{2} \left[ \frac {N _ {0} B \Delta}{g _ {0}} \left(2 ^ {\frac {L _ {k , n} ^ {c}}{B \Delta}} - 1 + (x _ {n} ^ {c} - x _ {k} ^ {m}) ^ {2} \right. \right. \\ \left. + \left(y _ {n} ^ {c} - y _ {k} ^ {m}\right) ^ {2} + H ^ {2}\right) ^ {2} + \left(2 ^ {\frac {L _ {k , n} ^ {c}}{B \Delta}} - 1 + \sum_ {k ^ {\prime} = 1, k ^ {\prime} \neq k} ^ {K} \beta_ {k ^ {\prime}, n}\right) ^ {2} \\ - \left(\frac {N _ {0} B \Delta}{g _ {0}} + 1\right) \left(2 ^ {\frac {L _ {k , n} ^ {c} (v)}{B \Delta}} - 1\right) ^ {2} \\ - \left(\sum_ {k ^ {\prime} = 1, k ^ {\prime} \neq k} ^ {K} \beta_ {k ^ {\prime}, n} (v)\right) ^ {2} - \frac {N _ {0} B \Delta}{g _ {0}} \left((x _ {n} ^ {c} (v) - x _ {k} ^ {m}) ^ {2} \right. \\ \left. \left. + \left(y _ {n} ^ {c} (v) - y _ {k} ^ {m}\right) ^ {2} + H ^ {2}\right) ^ {2} \right] \\ - \ln 2 \left(\frac {N _ {0}}{g _ {0}} + \frac {1}{B \Delta}\right) 2 ^ {\frac {L _ {k , n} ^ {c} (v)}{B \Delta}} \left(2 ^ {\frac {L _ {k , n} ^ {c} (v)}{B \Delta}} - 1\right) \\ \times \left(L _ {k, n} ^ {c} - L _ {k, n} ^ {c} (v)\right) - \left(\sum_ {k ^ {\prime} = 1, k ^ {\prime} \neq k} ^ {K} \beta_ {k ^ {\prime}, n} (v)\right) \\ \times \left(\sum_ {k ^ {\prime} = 1, k ^ {\prime} \neq k} ^ {K} \beta_ {k ^ {\prime}, n} - \beta_ {k ^ {\prime}, n} (v)\right) - \frac {2 N _ {0} B \Delta}{g _ {0}} \\ \end{array}
$$

$$
\begin{array}{l} \times \left(\left(x _ {n} ^ {c} (v) - x _ {k} ^ {m}\right) ^ {2} + \left(y _ {n} ^ {c} (v) - y _ {k} ^ {m}\right) ^ {2} + H ^ {2}\right) \\ \times \left(\left(x _ {n} ^ {c} (v) - x _ {k} ^ {m}\right) \left(x _ {n} ^ {c} - x _ {n} ^ {c} (v)\right) \right. \\ + \left(y _ {n} ^ {c} (v) - y _ {k} ^ {m}\right) \left(y _ {n} ^ {c} - y _ {n} ^ {c} (v)\right). \tag {45} \\ \end{array}
$$

# APPENDIX C DERIVATIONS OF MODEL 2 IN (29)

Here, following [16], [26]–[28], we briefly discuss the propulsive energy consumption model (29) which can be applied for both fixed-wing and rotary-wing UAV of weight $W = M g$ . For a fixed-wing UAV with initial and final velocity constraint (31e), the propulsion energy consumption is upper bounded by (29), where $\kappa _ { 1 } = 0 . 5 \rho C _ { D _ { 0 } } S _ { r } \Delta$ and $\kappa _ { 2 } = { 2 M ^ { 2 } g ^ { 2 } \Delta } / { ( \pi { e _ { 0 } } A _ { R } \rho { S _ { r } } ) }$ are derived by following [16, Eq. (56)]; ρ is the air density in $\mathrm { k g / m } ^ { 3 } ;$ $C _ { D _ { 0 } }$ is the zero-lift drag coefficient; Sr is a reference area; $e _ { 0 }$ is the Oswald efficiency; and $A _ { R }$ is the aspect ratio of the wing. For a rotary-wing UAV, the power $P _ { F }$ required for constant-height flight with speed $\| \pmb { v } ^ { c } \|$ can be approximated as [26]–[28]

$$
P _ {F} \approx P _ {0} + P _ {p} + P _ {i}, \tag {46}
$$

where $P _ { 0 }$ is the so called profile power, which is the power spent to turn the rotors and overcome the rotor aerodynamic drag force; $P _ { p }$ is the so called parasitic power, which is the power required to overcome parasite drag; and $P _ { i }$ is the so called induced power, which is the power required to produce lift by moving a mass of air through the disk at the induced velocity. In (46), although the profile power $P _ { 0 }$ is a function of flight speed $\| \pmb { v } ^ { c } \|$ , its contribution is constant in low-speed flight and small compared to the other components, and is hence generally neglected. Moreover, following [26]–[28], the other two components in (46) can be modeled as

$$
\begin{array}{l} P _ {F} (\boldsymbol {v} ^ {c}, \boldsymbol {a} ^ {c}) \approx 0. 5 \rho C _ {D _ {f}} S _ {r} \| \boldsymbol {v} ^ {c} \| ^ {3} + \frac {\epsilon \| \boldsymbol {T} \| ^ {2}}{2 \rho A \| \boldsymbol {v} ^ {c} \|} (47a) \\ = \frac {\kappa_ {1}}{\Delta} \| \boldsymbol {v} ^ {c} \| ^ {3} + \frac {\kappa_ {2}}{\Delta \| \boldsymbol {v} ^ {c} \|} \left(1 + \frac {\| \boldsymbol {a} ^ {c} \| ^ {2}}{g ^ {2}}\right), (47b) \\ \end{array}
$$

where $\kappa _ { 1 } = 0 . 5 \rho C _ { D _ { f } } S _ { r } \Delta$ and $\kappa _ { 2 } = \epsilon M ^ { 2 } g ^ { 2 } \Delta / ( 2 \rho A ) ; { \pmb a } ^ { c }$ is the UAV’s acceleration vector; $C _ { D _ { f } }$ is the drag coefficient based on the reference area $S _ { r } ; A$ is the area of the main rotor disk;  is the induced power factor; and $_ { T }$ is the total required thrust, which can be calculated as $\| \pmb { T } \| ^ { 2 } = W ^ { 2 } ( 1 + \| \hat { \pmb { a } } ^ { c } \| ^ { 2 } / g ^ { 2 } )$ for constant-height flight. For a trajectory ${ \pmb p } ^ { c } ( t )$ , velocity ${ \pmb v } ^ { c } ( t )$ and acceleration ${ \pmb a } ^ { c } ( t )$ , the total propulsion energy is then given by integrating (47) over time

$$
E _ {F} ^ {c} (\boldsymbol {v} ^ {c} (t), \boldsymbol {a} ^ {c} (t)) = \int P _ {F} (\boldsymbol {v} ^ {c} (t), \boldsymbol {a} ^ {c} (t)) d t. \tag {48}
$$

By applying the discrete linear state-space approximation in [16] to (48), the rotary-wing UAV’s propulsion energy consumption at the nth frame can be also derived as Model 2 in (29).

# REFERENCES

[1] [Online]. Available: https://info.internet.org/en. Accessed: Jan. 21, 2018.   
[2] [Online]. Available: https://x.company/loon. Accessed: Jan. 21, 2018.

[3] S. Jeong, O. Simeone, A. Haimovich, and J. Kang, “Mobile cloud computing with a UAV-mounted cloudlet: Optimal bit allocation for communication and computation,” IET Commun., vol. 11, no. 7, pp. 969–974, May 2017.   
[4] S. W. Loke, “The internet of flying-things: Opportunities and challenges with airborne fog computing and mobile cloud in the clouds,” arXiv:1507.04492v1, Jul. 2015.   
[5] Y. Zeng, R. Zhang, and T. J. Lim, “Wireless communications with unmanned aerial vehicles: Opportunities and challenges,” IEEE Commun. Mag., vol. 54, no. 5, pp. 36–42, May. 2016.   
[6] M. Asadpour, D. Giustiniano, K. Hummel, S. Heimlicher, and S. Egli, “Now or later?: Delaying data transfer in time-critical aerial communication,” in Proc. ACM Conf. Emerg. Netw. Exp. Technol., New York, NY, USA, Dec. 2013, pp. 127–132.   
[7] M. Asadpour, B. V. den Bergh, D. Giustiniano, K. Hummel, S. Pollin, and B. Plattner, “Micro aerial vehicle networks: An experimental analysis of challenges and opportunities,” IEEE Commun. Mag., vol. 52, no. 7, pp. 141–149, Jul. 2014.   
[8] Y. Zeng, R. Zhang, and T. J. Lim, “Throughput maximization for UAVenabled mobile relaying systems,” IEEE Trans. Commun., vol. 64, no. 12, pp. 4983–4996, Dec. 2016.   
[9] W. Zhao, M. Ammar, and E. Zegura, “A message ferrying approach for data delivery in sparse mobile ad hoc networks,” in Proc. ACM Int. Symp. Mobile Ad Hoc Netw. Comput., Tokyo, Japan, May 2004, pp. 187–198.   
[10] R. Shah, S. Roy, S. Jain, and W. Brunette, “Data MULEs: Modeling and analysis of a three-tier architecture for sparse sensor networks,” Ad Hoc Netw., vol. 1, no. 2, pp. 215–233, Sep. 2003.   
[11] P. Zhan, K. Yu, and A. L. Swindlehurst, “Wireless relay communications with unmanned aerial vehicles: Performance and optimization,” IEEE Trans. Aerosp. Electron. Syst., vol. 47, no. 3, pp. 2068–2085, Jul. 2011.   
[12] M. N. Soorki, M. Mozaffari, W. Saad, M. H. Manshaei, and H. Saidi, “Resource allocation for machine-to-machine communications with unmanned aerial vehicles,” in Proc. 2016 IEEE Globecom Workshops, Washington, DC, USA, Dec. 2016, pp. 1–6.   
[13] M. Mozaffari, W. Saad, M. Bennis, and M. Debbah, “Drone small cells in the clouds: Design, deployment and performance analysis,” in Proc. IEEE Global Commun. Conf., San Diego, CA, USA, Dec. 2015, pp. 1–6.   
[14] M. Mozaffari, W. Saad, M. Bennis, and M. Debbah, “Optimal transport theory for power-efficient deployment of unmanned aerial vehicles,” in Proc. IEEE Int. Conf. Commun., Kuala Lumpur, Malaysia, May 2016, pp. 1–6.   
[15] M. Mozaffari, W. Saad, M. Bennis, and M. Debbah, “Unmanned aerial vehicle with underlaid device-to-device communications: Performance and tradeoffs,” IEEE Trans. Wireless Commun., vol. 15, no. 6, pp. 3949–3963, Jun. 2016.   
[16] Y. Zeng and R. Zhang, “Energy-efficient UAV communication with trajectory optimization,” IEEE Trans. Wireless Commun., vol. 16, no. 6, pp. 3747–3760, Mar. 2017.   
[17] S. Manyam, D. Casbeer, and K. Sundar, “Path planning for cooperative routing of air-ground vehicles,” in Proc. Amer. Control Conf., Boston, MA, USA, Jul. 2016, pp. 4630–4635.   
[18] K. Dorling, J. Heinrichs, G. Messier, and S. Magierowski, “Vehicle routing problems for drone delivery,” IEEE Trans. Syst., Man, Cybern., Syst., vol. 47, no. 1, pp. 70–85, Jul. 2016.   
[19] F. Bonomi, R. Milito, P. Natarajan, and J. Zhu, “Fog computing: A platform for internet of things and analytics,” in Big Data and Internet of Things: A Roadmap for Smart Environments. New York, NY, USA: Springer, 2014, vol. 546, pp. 169–186.   
[20] Y. Saito, A. Benjebbour, Y. Kishiyama, and T. Nakamura, “System level performance evaluation of downlink non-orthogonal multiple access (NOMA),” in Proc. IEEE Int. Symp. Pers., Indoor Mobile Radio Commun., London, U.K., Sep. 2013, 611–615.   
[21] Z. Ding, Z. Yang, P. Fan, and H. Poor, “On the performance of nonorthogonal multiple access in 5G systems with randomly deployed users,” IEEE Signal Process. Lett., vol. 21, no. 12, pp. 1501–1505, Dec. 2014.

[22] N. Xue, “Design and optimization of lithium-ion batteries for electricvehicle applications,” Doctoral dissertation, Univ. Michigan, Ann Arbor, MI, USA, 2014.   
[23] C. Borst, F. Sjer, M. Mulder, M. V. Paassen, and J. Mulder, “Ecological approach to support pilot terrain awareness after total engine failure,” J. Aircr., vol. 45, no. 1, pp. 159–171, Jan. 2008.   
[24] A. Chakrabarty and J. Langelaan, “Energy maps for long-range path planning for small-and micro-UAVs,” in Proc. AIAA Guid., Navig., Control Conf., Honolulu, HI, USA, Aug. 2009.   
[25] A. Chakrabarty and J. Langelaan, “Energy-based long-range path planning for soaring-capable unmanned aerial vehicles,” J. Guid., Control, Dyn., vol. 34, no. 41, pp. 1002–1015, Jul. 2011.   
[26] A. Filippone, Flight Performance of Fixed and Rotary Wing Aircraft. Amsterdam, The Netherlands: Elsevier, 2006.   
[27] G. J. Leishman, Principles of Helicopter Aerodynamics. Cambridge, U.K.: Cambridge Univ. Press, 2006.   
[28] Z. Kong, V. Korukanti, and B. Mettler, “Mapping 3D guidance performance using approximate optimal cost-to-go function,” in Proc. AIAA Guid., Navig., Control Conf., Honolulu, HI, USA, Aug. 2009, pp. 6017–6027.   
[29] G. Scutari, F. Facchinei, L. Lampariello, and P. Song, “Parallel and distributed methods for nonconvex optimization part I: Theory,” arXiv:1410.4754v2, Jan. 2016.   
[30] G. Scutari, F. Facchinei, L. Lampariello, P. Song, and S. Sardellitti, “Parallel and distributed methods for nonconvex optimization part II: Applications,” arXiv:1601.04059v1, Jan. 2016.   
[31] C. Geng, N. Naderializadeh, A. S. Avestimehr, and S. A. Jafar, “On the optimality of treating interference as noise,” IEEE Trans. Inf. Theory, vol. 61, no. 4, pp. 1753–1767, Apr. 2015.   
[32] W. H. Yuan and K. Nahrstedt, “Energy-efficient soft real-time CPU scheduling for mobile multimedia systems,” ACM SIGOPS Oper. Syst. Rev., vol. 37, no. 5, pp. 149–163, Dec. 2003.   
[33] W. H. Yuan and K. Nahrstedt, “Energy-efficient CPU scheduling for multimedia applications,” ACM Trans. Comput. Syst., vol. 24, no. 3, pp. 292–331, Aug. 2006.   
[34] T. M. Cover and J. A. Thomas, Element of Information Theory. Hoboken, NJ, USA: Wiley, 2006.

![](images/527e78b191efa9c6bf3b5043cc4ff180a9aa192a5411de057b99a76a506a223e.jpg)

<details>
<summary>natural_image</summary>

Black-and-white portrait of a woman with long dark hair, wearing earrings (no visible text or symbols)
</details>

Seongah Jeong received the B.Sc. degree in electrical communications engineering (Magna cum laude) and the M.Sc. and Ph.D. degrees in electrical engineering from the Korea Advanced Institute of Science and Technology (KAIST), Daejeon, South Korea, in 2010, 2012, and 2015, respectively. She is currently a Postdoctoral Research Fellow in the John A. Paulson School of Engineering and Applied Sciences, Harvard University, Cambridge, MA, USA. In 2009, she was an Intern in the Electria-Wireless Sensor Network Lab, Helsinki Metropolia Univer-

sity of Applied Sciences, Vantaa, Finland. From 2013 to 2014, she was a Visiting Scholar with the New Jersey Institute of Technology, Newark, NJ, USA. From 2015 to 2016, she was a Postdoctoral Research Fellow with the Information and Electronics Research Institute, KAIST. Her research interests include signal processing and optimization for biology, wireless localization, and wireless communications. Her achievements have been recognized with awards including the Silver Prize (2015) and the Bronze Prize (2014) in Samsung Humantech Thesis Award and KAIST Research Excellence Award (2015).

![](images/9bdb76962e158da068fd2b9f914c03680c7d799ab2132c08635203fcfcfbd0ba.jpg)

<details>
<summary>natural_image</summary>

Portrait of a man in a collared shirt, standing in front of a bookshelf (no visible text or symbols)
</details>

Osvaldo Simeone (F’15) received the M.Sc. degree (with Hons.) and the Ph.D. degree in information engineering from the Politecnico di Milano, Milan, Italy, in 2001 and 2005, respectively. He is currently a Professor of information engineering in the Department of Informatics, King’s College London, London, U.K. He was a Professor with the Center for Wireless Information Processing, New Jersey Institute of Technology. He is a coauthor of a monograph, an edited book published by Cambridge University Press, and more than 100 research journal papers. His research interests include wireless communications, information theory, optimization, and machine learning. His research has been supported by the U.S. NSF, the ERC, the Vienna Science and Technology Fund, as well by a number of industrial collaborations. He is a corecipient of the 2017 JCN Best Paper Award, the 2015 IEEE Communication Society Best Tutorial Paper Award, and the Best Paper Awards of IEEE SPAWC 2007 and IEEE WRECOM 2007. He received a Consolidator grant by the European Research Council in 2016. He is currently a Distinguished Lecturer of the Information Theory Society and a member of the Signal Processing for Communications and Networking Technical Committee.

![](images/b76964acae4105287c21aaea8c48fe6c185712a78e107c6f050669bc31f1ff44.jpg)

<details>
<summary>natural_image</summary>

Portrait of a man wearing glasses and a suit (no text or symbols visible)
</details>

Joonhyuk Kang (M’00) received the B.S.E. and M.S.E. degrees from the Seoul National University, Seoul, South Korea, in 1991 and 1993, respectively, and the Ph.D. degree in electrical and computer engineering from the University of Texas at Austin, Austin, TX, USA, in 2002. He is currently a faculty member in the Department of Electrical Engineering, Korea Advanced Institute of Science and Technology, Daejeon, South Korea. From 1993 to 1998, he was a research staff with SAMSUNG Electronics, Suwon, South Korea, where he involved in the development of DSP-based real-time control systems. In 2000, he was with Cwill Telecommunications, Austin, TX, USA, where he participated in the project for multicarrier CDMA systems with antenna array. He was a Visiting Scholar with the School of Engineering and Applied Sciences, Harvard University, Cambridge, MA, USA, from 2008 to 2009. His research interest includes signal processing for cognitive radio, cooperative communication, physicallayer security, and wireless localization. He is a member of IEEE Korea Information and Communications Society and Tau Beta Pi (The Engineering Honor Society) and has received a Texas Telecommunication Consortium Graduate Fellowship from 2000 to 2002.