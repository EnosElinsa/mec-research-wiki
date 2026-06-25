# Communications and Control for Wireless Drone-Based Antenna Array

Mohammad Mozaffari , Student Member, IEEE, Walid Saad , Senior Member, IEEE, Mehdi Bennis , Senior Member, IEEE, and Mérouane Debbah, Fellow, IEEE

Abstract— In this paper, the effective use of multiple quadrotor drones as an aerial antenna array that provides wireless service to ground users is investigated. In particular, under the goal of minimizing the airborne service time needed for communicating with ground users, a novel framework for deploying and operating a drone-based antenna array system whose elements are single-antenna drones is proposed. In the considered model, the service time is minimized by minimizing the wireless transmission time as well as the control time that is needed for movement and stabilization of the drones. To minimize the transmission time, first, the antenna array gain is maximized by optimizing the drone spacing within the array. In this case, using perturbation techniques, the drone spacing optimization problem is addressed by solving successive, perturbed convex optimization problems. Then, according to the location of each ground user, the optimal locations of the drones around the array’s center are derived such that the transmission time for the user is minimized. Given the determined optimal locations of drones, the drones must spend a control time to adjust their positions dynamically so as to serve multiple users. To minimize this control time of the quadrotor drones, the speed of rotors is optimally adjusted based on both the destinations of the drones and external forces (e.g., wind and gravity). In particular, using bang–bang control theory, the optimal rotors’ speeds as well as the minimum control time are derived in closed-form. Simulation results show that the proposed approach can significantly reduce the service time to ground users compared with a fixed-array case in which the same number of drones form a fixed uniform antenna array. The results also show that, in comparison with the fixed-array case, the network’s spectral efficiency can be improved by 32% while leveraging the drone antenna array

Manuscript received April 2, 2018; revised August 5, 2018; accepted September 8, 2018. Date of publication September 20, 2018; date of current version January 15, 2019. This work was supported in part by the Army Research Office (ARO) under Grant W911NF-17-1-0593 and in part by the US NSF under Grant AST-1506297 and Grant CNS-1739642. The work of M. Bennis was supported in part by the Academy of Finland project CARMA, in part by the INFOTECH project NOOR, and in part by the Academy of Finland project SMARTER. This paper was presented in [1]. The associate editor coordinating the review of this paper and approving it for publication was R. Zhang. (Corresponding author: Mohammad Mozaffari.)

M. Mozaffari was with Wireless@VT, Electrical and Computer Engineering Department, Virginia Tech, VA 24061 USA. He is now with Ericsson, Santa Clara, CA 95054 USA (e-mail: mohammad.mozaffari@ericsson.com).

W. Saad is with Wireless@VT, Electrical and Computer Engineering Department, Virginia Tech, VA USA (e-mail: walids@vt.edu).

M. Bennis is with the Centre for Wireless Communications, University of Oulu, Oulu, Finland (e-mail: bennis@ee.oulu.fi).

M. Debbah is with the Mathematical and Algorithmic Sciences Laboratory, Huawei France R&D, Paris, France, and also with CentraleSupelec, Université Paris-Saclay, Gif-sur-Yvette, France (e-mail: merouane.debbah@huawei.com).

Color versions of one or more of the figures in this paper are available online at http://ieeexplore.ieee.org.

Digital Object Identifier 10.1109/TCOMM.2018.2871453

system. Finally, the results reveal an inherent tradeoff between the control time and transmission time while varying the number of drones in the array.

Index Terms— Drone, UAV, antenna array, wireless communications, beamforming, control, optimization, service time.

# I. INTRODUCTION

THE use of unmanned aerial vehicles (UAVs) such asdrones is growing rapidly across many domains includ- drones is growing rapidly across many domains including delivery, communications, surveillance, and search and rescue in emergency operations [2]–[6]. In wireless networks, drones can be used as flying base stations to provide reliable and cost-effective wireless connectivity [2]–[12]. Due to their flexibility, agility, and mobility, drones can support reliable, cost-effective, and high data rate wireless communications for ground users. In particular, during major public events such as Olympic games that generate a substantial demand for communication, there is a need to supplement the limited capacity and coverage capabilities of existing cellular networking infrastructure. In such scenarios, drone-based wireless communication is an ideal solution. For instance, AT&T and Verizon are planning to use flying drones to boost the Internet coverage for the college football national championship and the Super Bowl. Drones can also play a key role in enabling wireless connectivity in other key scenarios such as public safety, and Internet of Things (IoT) scenarios [4]. To effectively leverage drones for wireless networking applications, one must address a number of challenges that include optimal placement of drones, path planning, resource management, control, and flight time optimization [2], [4], [11].

# A. Related Work on UAV Communications

There has been a recent surge of literature discussing the use of drones for wireless communication purposes [2]–[7], [9], [11], [13]–[16]. For instance, in [3], the authors studied the optimal 3D placement of UAVs for maximizing the number of covered users with different quality-of-service (QoS) requirements. The works in [2] and [7] studied path planning and optimal deployment problems for UAV-based communications and computing. The work in [9] proposed a framework for the optimal placement and distribution of UAVs to minimize the overall delay in a UAV-assisted wireless network. A comparison between the performance of aerial base stations and terrestrial base stations in terms of average sum rate and transmit power is presented in [13]. In [14], a polynomial-time algorithm for the optimal placement of drones that provide coverage for ground terminals is proposed.

One of the fundamental challenges in drone-based communications systems is the limited flight endurance of drones. Naturally, flying drones have a limited amount of on-board energy which must be used for transmission, mobility, control, data processing, and payloads purposes. Consequently, the flight duration of drones is typically short and can be insufficient for providing a long-term, continuous wireless coverage. Furthermore, due to the limited transmit power of drones, providing long-range, high rate, and low latency communications can be challenging in drone-enabled wireless systems. In this regard, a key performance metric in drone-enabled wireless networks is airborne service time, which is defined as the time needed for servicing ground users. The service time directly impacts the flight time of drones as well as the quality-of-service (i.e., delay) for ground users. From the drones’ perspective, a lower service time corresponds to a shorter flight time as well as less energy consumption. From the users’ point of view, a lower service time is also needed as it directly yields lower latency. To address the flight time and energy consumption challenges of drones, the authors in [5] proposed a comprehensive analytical framework for optimizing the trajectory of a fixed-wing UAV with the objective of minimizing the UAV’s energy consumption while serving a ground user. In particular, a new design paradigm is developed that jointly considers the communication rate and the UAV’s energy consumption. The work in [15] minimized the hover time of drone base stations by deriving the optimal cell association schemes. However, the model in [15] is limited to static single-antenna drones. In [16], the trajectory and mission completion time of a single UAV that serves ground users are optimized. However, the work in [16] does not analyze a scenario with multiple UAVs.

One promising approach to provide high data rate and low service time is to utilize multiple drones within an antenna array system composed of multiple single-antenna drones [17]. Compared to conventional antenna array systems, a dronebased antenna array has the following advantages. First, the number of antenna elements (i.e., drones) is not limited by space constraints. Second, the gain of the drone-based antenna array can be increased by adjusting the array element spacing. Third, the mobility and flexibility of drones enable an effective mechanical beam-steering in any three-dimensional (3D) direction. Clearly, a high gain drone-based antenna array can provide high data rate wireless services to ground users thus reducing the service time.

In [17], the authors studied the design of a UAV-based antenna array for directivity maximization. However, the approach presented in [17] is based on a heuristic and a computationally demanding evolutionary algorithm. Moreover, the service time analysis is ignored in [17]. In [18], the authors derived the asymptotic capacity of an airborne multiple-input-multiple-output (MIMO) wireless communication system. However, the work in [18] considers fixed positions for the antenna elements of the transmitter and the receiver. Furthermore, this work does not analyze the control aspect of drones which is essential in designing drone-based MIMO systems. In fact, none of the previous works on drone communications, such as in [2]–[4] and [6]–[19], has studied the use of a drone-based antenna array system for service time minimization.

We note that, there exist some studies on time-optimal motion planning [20]–[23]. However, most of the previous works do not address the time-optimal control problem of quadrotor drones. While the authors in [23] consider a quadrotor drone in their model, they ignore the effect of external forces on the control time. Furthermore, the approach in [23] is based on a genetic algorithm which is computationally demanding. Unlike our work, the work in [23] ignores the communication aspects of drones, and does not capture the impact of control time on the performance of drone-enabled wireless networks. Compared to [23], our proposed framework comprises both communication and control aspects of drones and it is analytically tractable.

# B. Contributions

The main contribution of this paper is a novel framework for deploying and operating a drone-based antenna array system that delivers wireless service to a number of ground users within a minimum time. In particular, we minimize the service time that includes both the transmission time and the control time needed to control the movement and orientation of the drones. To this end, we minimize the transmission time, by optimizing the drones’ locations, as well as the control time that the drones need to move between these optimal locations. To minimize the transmission time, first, we determine the optimal drone spacing for which the array directivity is maximized. In this case, using perturbation theory [24], we solve the drone spacing optimization problem by successively solving a number of perturbed convex optimization problems. Next, given the derived drone spacing, we optimally adjust the locations of the drones according to the position of each ground user. In order to serve different users, the drones must dynamically move between the derived optimal locations, during the control time period. To minimize the control time of quadrotor drones, we determine the optimal speeds of rotors such that the drones can update their positions and orientations within a minimum time. In this case, using bang-bang control theory [25], we derive a closed-form expression for the minimum control time as a function of external forces (e.g., wind and gravity), the drone’s weight, and the destinations of drones. Our results show that the proposed drone antenna array approach can significantly reduce the service time and improve the spectral and energy efficiency of the network. In particular, our approach yields 32% improvement in spectral efficiency compared to a case in which the same number of drones form a fixed uniform aerial antenna array. The results also reveal a tradeoff between the control time and transmission time while varying the number of drones.

# II. SYSTEM MODEL AND GENERAL PROBLEM FORMULATION

Consider a set L of L single-antenna wireless users located within a given geographical area. In this area, a set M of M quadrotor drones are used as flying access points to provide downlink wireless service for ground users. The M drones will form an antenna array in which each element is a single-antenna drone, as shown in Fig. 1. For tractability, we consider a linear antenna array whose elements are symmetrically excited and located about the origin of the array as done in [26]. The results that we will derive for the linear array case can provide a key guideline for designing more complex 2D and 3D array configurations. The 3D location of drone $m \in \mathcal { M }$ and of user $i \in \mathcal { L }$ is given by $( x _ { i } ^ { \mathrm { u } } , y _ { i } ^ { \mathrm { u } } , z _ { i } ^ { \mathrm { u } } )$ , and the location of drone m while serving user i is $( x _ { m , i } , y _ { m , i } , z _ { m , i } )$ . To avoid collisions, we assume ( )that adjacent drones in the array are separated by at least $D _ { \mathrm { m i n } }$ . Let $a _ { m }$ and $\beta _ { m }$ be the amplitude and phase of the signal (i.e. excitation) at element m in the array. Let $d _ { m , i } =$ $\sqrt { \left( x _ { m , i } - x _ { o } \right) ^ { 2 } + \left( y _ { m , i } - y _ { o } \right) ^ { 2 } + \left( z _ { m , i } - z _ { o } \right) ^ { 2 } }$ be the distance ( ) + ( ) + ( )of drone m from the origin of the array whose 3D coordinate is $( x _ { o } , y _ { o } , z _ { o } )$ . The magnitude of the far-field radiation pattern ( )of each element is $w ( \theta , \phi )$ , where θ and φ are the polar and ( )azimuthal angles in the spherical coordinate.

![](images/ad45f289458b5038ad8a92fbb6afee8e13d74bf216191a89401bdad1967cd99e.jpg)

<details>
<summary>text_image</summary>

Origin of the array
(x₀,y₀,z₀)
Array axis
Drone m
(xₘ,yₘ,zₘ)
Array Beam
User i
(xᵢᵘ,yᵢᵘ,zᵢᵘ)
</details>

Fig. 1. Drone-based antenna array.

To serve ground users distributed over a geographical area, the drones will dynamically change their positions based on each user’s location. In our model, drones hover at specific locations to serve a user, and fly to a new position to serve another user. Such repositioning is needed for adjusting the distance and beam direction of the antenna array to each ground user. We consider a “fly-then-hover-and-transmit" operation (as also done in [27]) for the drone-based antenna array system. In this case, drones transmit when they are stationary and, hence, transmission is not performed while the array moves. Such a transmission protocol is suitable for the considered drone-based antenna array system since the antenna array needs to be stable so as to effectively perform beamforming and to establish reliable communication links to ground users. Note that, unlike a classical linear phased array that uses electronic beam steering, the proposed drone-based antenna array relies on the repositioning of drones.1 This is due to the fact that, in the drone antenna array, precisely adjusting

1In general, the array gain depends on the elements’ positions and the phase of the elements. In classical antenna array systems with fixed elements, the phase of the elements is often optimized. Here, we exploit the drones’ flexibility to maximize the array directivity by optimizing the element (i.e., drone) spacing, given the elements’ phases.

the elements’ phase is more challenging than the phased array whose elements are directly connected. In addition, a linear phased array cannot perform 3D beam steering. Hence, in our model, the drones dynamically adjust their positions in order to steer the beam towards ground users. Clearly, the service time, which is the time needed to serve the ground users, depends on the transmission time and the control time during which the drones must move and stabilize their locations. The transmission time is inversely proportional to the downlink data rate which depends on the signal-to-noise-ratio (SNR) which is, in turn, function of the array’s beamforming gain.

The service time is an important metric for both users and drones. A lower service time yields a lower delay and, hence, higher quality-of-service for the users. Also, the service time is directly related to spectral efficiency as it depends on data rate and transmission bandwidth. For drones, a lower service time corresponds to a shorter flight time and less energy consumption. In fact, minimizing the service time improves both energy and spectral efficiency. Therefore, our goal is to minimize the total service time of the ground users by optimally adjusting the drones’ locations, within a minimum control time, that can provide a maximum data rate.

For drone-to-ground communications, we consider a line-ofsight (LoS) propagation model as done in [2] and [16]. Such a channel model is reasonable here as the effect of multipath is significantly mitigated due to the high altitude of drones and using beamforming [16]. The transmission rate from the drone antenna array to ground user i in a far-field region is given by [16]:

$$
R _ {i} (\boldsymbol {x} _ {i}, \boldsymbol {y} _ {i}, \boldsymbol {z} _ {i}) = B \log_ {2} \left(1 + \frac {r _ {i} ^ {- \alpha} P _ {t} K _ {o} G _ {i} (\boldsymbol {x} _ {i} , \boldsymbol {y} _ {i} , \boldsymbol {z} _ {i})}{\sigma^ {2}}\right), \tag {1}
$$

where $\pmb { x } _ { i } = [ x _ { m , i } ] _ { M \times 1 } , \pmb { y } _ { i } = [ y _ { m , i } ] _ { M \times 1 } , \ z _ { i } = [ z _ { m , i } ] _ { M \times 1 } ,$ $m \in \mathcal { M }$ = [ ] = [ ] = [ ]representing the 3D coordinates of the drones while serving user i. B is the transmission bandwidth, $r _ { i }$ is the distance between the origin of the array and user $i , P _ { t }$ is the total transmit power of the array, $\sigma ^ { 2 }$ is the noise power, and $K _ { o }$ is the constant path loss coefficient. $G _ { i } ( x _ { i } , y _ { i } , z _ { i } )$ is the ( )gain of the antenna array towards the location of user i. In the proposed drone-based antenna array system, each drone is an antenna element of the array. In this case, the entire antenna array can be modeled as a single directional antenna whose gain is the total array gain [28]. The array gain is given by [29]:

$$
G _ {i} \left(\boldsymbol {x} _ {i}, \boldsymbol {y} _ {i}, \boldsymbol {z} _ {i}\right) = \frac {4 \pi \left| F \left(\theta_ {i} , \phi_ {i}\right) \right| ^ {2} w \left(\theta_ {i} , \phi_ {i}\right) ^ {2}}{\int_ {0} ^ {2 \pi} \int_ {0} ^ {\pi} | F (\theta , \phi) | ^ {2} w (\theta , \phi) ^ {2} \sin \theta \mathrm{d} \theta \mathrm{d} \phi} \eta , \tag {2}
$$

where $0 \leq \eta \leq 1$ is the antenna array efficiency which is 0 1multiplied by directivity to compute the antenna gain. In fact, the antenna gain is equal to the antenna directivity multiplied by η. In (2), $F ( \theta , \phi )$ is the array factor which can be written as [29]:

$$
\begin{array}{l} F (\theta , \phi) \\ = \sum_ {m = 1} ^ {M} a _ {m} e ^ {j [ k (x _ {m, i} \sin \theta \cos \phi + y _ {m, i} \sin \theta \sin \phi + z _ {m, i} \cos \theta) + \beta_ {m} ]}, \tag {3} \\ \end{array}
$$

where $k = 2 \pi / \lambda$ is the phase constant, and λ is the wave-= 2length. Note that, the overall radiation pattern of the antenna array is equal to $F ( \theta , \phi ) w ( \theta _ { i } , \phi _ { i } )$ which follows from the pattern multiplication rule [29].

Now, the total time that the drones spend to service the ground users will be:

$$
T _ {\text { service }} = \sum_ {i = 1} ^ {L} \frac {q _ {i}}{R _ {i} (\boldsymbol {x} _ {i} , \boldsymbol {y} _ {i} , \boldsymbol {z} _ {i})} + T _ {i} ^ {\mathrm{crl}} (\boldsymbol {V}, \boldsymbol {x} _ {i}, \boldsymbol {y} _ {i}, \boldsymbol {z} _ {i}), \tag {4}
$$

where $T _ { \mathrm { s e r v i c e } }$ represents the total service time, $q _ { i }$ is the load of user i which represents the number of bits that must be transmitted to user i. $T _ { i } ^ { \mathrm { c r l } }$ is the control time during which the drones adjust their locations according to the location of ground user i. In particular, $T _ { i } ^ { \mathrm { c r l } }$ captures the time needed for updating the drones’ locations from state i −  (i.e., locations of drones while serving user $i - 1 , i > 1 )$ 1to state i. The 1 1control time is obtained based on the dynamics of the drones and is a function of control inputs, external forces, and the movement of drones. In fact, each drone needs a vector of control inputs in order to move from its initial location to a new location while serving different users. For quadrotor drones, the rotors’ speeds are commonly considered as control inputs. Therefore, in (4), we have $V = [ v _ { m n } ( t ) ] _ { M \times 4 }$ with $v _ { m n } ( t )$ = [ ( )]being the speed of rotor n of drone m at time t. The ( )maximum speed of each rotor is $v _ { \mathrm { m a x } }$ . In this case, one can minimize the control time of the drones by properly adjusting the rotors’ speeds. In Section IV, we will provide a detailed analysis of the control time given the drones’ dynamics.

Clearly, to effectively employ drones within an aerial antenna array, it is crucial to ensure the stability of the drones. Hence, in the proposed drone-based antenna array system, we adopt quadrotor drones which can hover (remain stationary) and move to any direction [30]. In Section ${ \mathrm { I V } } ,$ we analyze the stability of the drones in the array when serving ground users. We derive the optimal rotors’ speeds for which the quadrotor drones can stabilize their positions. Moreover, we account for wind effects while analyzing the drones’ stability.2

Given this model, our goal is to minimize the total service time of drones by finding the optimal locations of the drones with respect to the center of the array, as well as the optimal control inputs. Our optimization problem, in its general form, is given by:

$$
\underset {\boldsymbol {X}, \boldsymbol {Y}, \boldsymbol {Z}, \boldsymbol {V}} {\text { minimize }} \sum_ {i = 1} ^ {L} \frac {q _ {i}}{R _ {i} (\boldsymbol {x} _ {i} , \boldsymbol {y} _ {i} , \boldsymbol {z} _ {i})} + T _ {i} ^ {\mathrm{crl}} (\boldsymbol {V}, \boldsymbol {x} _ {i}, \boldsymbol {y} _ {i}, \boldsymbol {z} _ {i}), \tag {5}
$$

$\mathrm { s t . } d _ { m + 1 , i } - d _ { m , i } \geq D _ { \operatorname* { m i n } } , \forall m \in \mathcal { M } \backslash \{ M \} ,$ (6)

$$
0 \leq v _ {m w} (t) \leq v _ {\max}, \quad \forall m \in \mathcal {M}, w \in \{1,..., 4 \}, \tag {7}
$$

where X, Y , and $Z$ are matrices whose rows $i$ are, respectively, vectors ${ \mathbf { } } x _ { i } , \ y _ { i }$ , and $z _ { i } , \forall i \in { \mathcal { L } } .$ . The constraint in (6) indicates that the minimum separation distance between two adjacent drones must be greater than $D _ { \mathrm { m i n } }$ to avoid collision.

2We also note that the proposed drone-based antenna array system is more suitable for a low frequency (e.g., below 600 MHz) case in which the wavelength is above 0.5 m. In this case, the array performance will not be significantly affected by drones’ vibrations.

(7) represents the constraints on the speed of each rotor. Note that, the first term in (5) represents the transmission time which depends on the drones’ locations. The second term, $T _ { i } ^ { \mathrm { c r l } }$ , is the control time which is a function of the rotors’ speeds as well as the drones’ locations. Solving (5) is challenging as it is highly nonlinear due to (2). Moreover, as we can see from (3), the array factor is a complex function of the array element’s positions. In addition, due to the nonlinear nature of quadrotor’s dynamic system, finding the optimal control inputs is a challenging task, as will be discussed in Section IV.

We note that, considering a narrow-beam antenna array communication, (5) can be solved by separately optimizing drones’ locations and rotors’ speeds. In the narrow-beam case, the drone array must perfectly steer its beam towards each ground user. Hence, we can first determine the optimal drones’ positions and, then, optimize the rotors’ speeds to move to these optimal positions within a minimum time. Our approach for solving (5) includes two key steps. First, given the location of any ground user, we optimize the locations of the drones in the linear array to minimize the transmission time. Thus, given L ground users, we will have L sets of drones’ locations. In the second step, using the result of the first step, we determine the drones’ optimal control strategy to update their locations within a minimum time. Hence, the solution of the transmission time optimization problem (in the first step) is used as inputs to the time-optimal control problem (in the second step). While, in general, this approach leads to a suboptimal solution, it is analytically tractable and practically easy to implement. Next, we will optimize the location of drones to achieve a minimum transmission time for any arbitrary ground user.

# III. OPTIMAL POSITIONS OF DRONES IN ARRAY FOR TRANSMISSION TIME MINIMIZATION

In this section, we determine the optimal positions of the drones in the array based on the location of each user such that the transmission time to the user is minimized. Clearly, given (1), (2), and (4), to minimize the transmission time, we need to maximize the array gain (i.e., directivity) towards each ground user.

Without loss of generality, we consider an even number of drones. For an odd number of drones, the same analysis will still hold. Now, the array factor for M drones located on the x-axis of the Cartesian coordinate can be given by:

$$
\begin{array}{l} F (\theta , \phi) = \sum_ {m = 1} ^ {M} a _ {m} e ^ {j [ k x _ {m, i} \sin \theta \cos \phi + \beta_ {m} ]} \\ \stackrel {(a)} {=} \sum_ {n = 1} ^ {M / 2} a _ {n} \left(e ^ {j [ k d _ {n} \sin \theta \cos \phi + \beta_ {n} ]} + e ^ {- j [ k d _ {n} \sin \theta \cos \phi + \beta_ {n} ]}\right) \\ \stackrel {(b)} {=} 2 \sum_ {n = 1} ^ {N} a _ {n} \cos \left(k d _ {n} \sin \theta \cos \phi + \beta_ {n}\right), \tag {8} \\ \end{array}
$$

where $\begin{array} { c c c } { N } & { = } & { M / 2 } \end{array}$ , and $d _ { n }$ is the distance of element $n \in \mathcal { N } = \{ 1 , 2 , . . . , N \}$ from the center of the array (origin). = 1 2Also, a follows from the fact that the array is symmetric ( )with respect to the origin, and b is based on the Euler’s rule.

Now, we can maximize the directivity of the array by optimizing $d _ { n } , \forall n \in { \mathcal { N } } \colon$

$$
\underset {d _ {n}, \forall n \in \mathcal {N}} {\text { maximize }} \frac {4 \pi | F (\theta_ {\max} , \phi_ {\max}) | ^ {2} w (\theta_ {\max} , \phi_ {\max}) ^ {2}}{\int_ {0} ^ {2 \pi} \int_ {0} ^ {\pi} | F (\theta , \phi) | ^ {2} w (\theta , \phi) ^ {2} \sin \theta \mathrm{d} \theta \mathrm{d} \phi}, \tag {9}
$$

where $( \theta _ { \mathrm { m a x } } , \phi _ { \mathrm { m a x } } )$ are the polar and azimuthal angles at ( )which the total antenna pattern $F ( \theta , \phi ) w ( \theta , \phi )$ has a max-( ) ( )imum value. Clearly, solving (9) is challenging due to the non-linearity and complex expression of the objective function of this optimization problem. Moreover, this problem is non-convex and, hence, cannot be exactly solved using classical convex optimization methods. Next, we solve (9) by exploiting the perturbation technique [26]. In general, perturbation theory aims at finding the solution of a complex problem, by starting from the exact solution of a simplified version of the original problem [24]. This technique is thus useful when dealing with nonlinear and analytically intractable optimization problems such as (9).

# A. Perturbation Technique for Drone Spacing Optimization

To optimize the distance between drones, we first consider an initial value for the distance of each drone from the origin. Then, we find the optimal perturbation value that must be added to this initial value. Let $d _ { n } ^ { 0 }$ be the initial distance for drone n, the perturbed distance is:

$$
d _ {n} = d _ {n} ^ {0} + e _ {n}, \tag {10}
$$

where $\begin{array} { r l r } { e _ { n } } & { { } < < } & { \lambda } \end{array}$ , with λ being the wavelength, is the perturbation value. Given (10), the array factor can be approximated by:

$$
\begin{array}{l} F (\theta , \phi) \\ = 2 \sum_ {n = 1} ^ {N} a _ {n} \cos \left(k (d _ {n} ^ {0} + e _ {n}) \sin \theta \cos \phi + \beta_ {n}\right) \\ = 2 \sum_ {n = 1} ^ {N} a _ {n} \cos \left[ \left(k d _ {n} ^ {0} \sin \theta \cos \phi + \beta_ {n}\right) + k e _ {n} \sin \theta \cos \phi \right] \\ \stackrel {(a)} {\approx} \sum_ {n = 1} ^ {N} 2 a _ {n} \cos \left(k d _ {n} ^ {0} \sin \theta \cos \phi + \beta_ {n}\right) \\ - \sum_ {n = 1} ^ {N} 2 a _ {n} k e _ {n} \sin \theta \cos \phi \sin \left(k d _ {n} ^ {0} \sin \theta \cos \phi + \beta_ {n}\right), \tag {11} \\ \end{array}
$$

where in (a) we used the trigonometric properties, and the fact that sin $( x ) \approx x$ for small values of x. Clearly, given $e _ { n } < < \lambda$ , ( )the numerator of (9) can be computed based on the values of $d _ { n } ^ { 0 } , \forall n \in \mathcal { N }$ . Hence, given $d _ { n } ^ { 0 }$ , our optimization problem in (9) can be written as:

$$
\min _ {e} \int_ {0} ^ {2 \pi} \int_ {0} ^ {\pi} F (\theta , \phi) ^ {2} w (\theta , \phi) ^ {2} \sin \theta \mathrm{d} \theta \mathrm{d} \phi , \tag {12}
$$

$$
\text { s.t. } d _ {n + 1} ^ {0} + e _ {n + 1} - d _ {n} ^ {0} - e _ {n} \geq D _ {\min}, \quad \forall n \in \mathcal {N} \backslash \{N \}, \tag {13}
$$

where e is the perturbation vector having elements $e _ { n } , n \in { \mathcal { N } } .$ For brevity, we define the following functions:

$$
F ^ {0} (\theta , \phi) = \sum_ {n = 1} ^ {N} a _ {n} \cos \left(k d _ {n} ^ {0} \sin \theta \cos \phi + \beta_ {n}\right), \tag {14}
$$

$$
I _ {\text { int }} (x) = \int_ {0} ^ {2 \pi} \int_ {0} ^ {\pi} x \sin \theta \mathrm{d} \theta \mathrm{d} \phi . \tag {15}
$$

Theorem 1: The optimization problem in (12) is convex, and the optimal perturbation vector is the solution of the following system of equations:

$$
\left\{ \begin{array}{l} e = G ^ {- 1} [ q + \mu_ {\mathcal {L}} ], \\ \mu_ {n} \left(e _ {n} - e _ {n + 1} + D _ {\min} + d _ {n} ^ {0} - d _ {n + 1} ^ {0}\right) = 0, \quad \forall n \in \mathcal {N} \backslash \{N \}, \\ \mu_ {n} \geq 0, \forall n \in \mathcal {N} \backslash \{N \}. \end{array} \right. \tag {16}
$$

where $\pmb { G } = [ g _ { m , n } ] _ { N \times N }$ is an $N \times N$ matrix with:

$$
\begin{array}{l} g _ {m, n} \\ = I _ {\text { int }} \left(a _ {m} a _ {n} (k \sin \theta \cos \phi w (\theta , \phi)) ^ {2} \right. \\ \left. \times \sin \left(k d _ {n} ^ {0} \sin \theta \cos \phi + \beta_ {n}\right) \sin \left(k d _ {m} ^ {0} \sin \theta \cos \phi + \beta_ {m}\right)\right), \tag {17} \\ \end{array}
$$

and $\pmb q = [ q _ { n } ] _ { N \times 1 }$ whose elements are given by:

$$
q _ {n} = I _ {\mathrm{int}} \left(a _ {n} k \sin \theta \cos \phi w (\theta , \phi) F ^ {0} (\theta , \phi) \right.
$$

$$
\left. \times \sin \left(k d _ {n} ^ {0} \sin \theta \cos \phi + \beta_ {n}\right)\right). \tag {18}
$$

In (16), $\mu _ { \mathcal { L } }$ is a vector of Lagrangian multipliers, whose element n is $\mu _ { \mathcal { L } } ( n ) = \mu _ { n + 1 } - \mu _ { n }$ , with $\mu _ { n }$ being a Lagrangian ( ) =multiplier associated with constraint n.

Proof: See Appendix A.

Using Theorem 1, we can update the distance of each drone from the origin as follows:

$$
\boldsymbol {d} ^ {1} = \boldsymbol {d} ^ {0} + \boldsymbol {e} ^ {*}, \tag {19}
$$

where $\pmb { d } ^ { 1 } = [ d _ { n } ^ { 1 } ] _ { N \times 1 }$ , and $\begin{array} { r } { \pmb { d } ^ { 0 } = [ d _ { n } ^ { 0 } ] _ { N \times 1 } , n \in \mathcal { N } . } \end{array}$

Clearly, $d ^ { 1 }$ ] = [ ]leads to a better solution than $\pmb { d } ^ { 0 } = [ d _ { n } ] _ { N \times 1 }$ = [ ]In fact, we can proceed and further improve the solution to (12) by updating $d ^ { 1 }$ . In particular, at step update $r \in \mathbb N$ , we find $\dot { d } ^ { ( r ) }$ :

$$
\boldsymbol {d} ^ {(r)} = \boldsymbol {d} ^ {(r - 1)} + \boldsymbol {e} ^ {* (r)}, \tag {20}
$$

where $e ^ { * ( r ) }$ is the optimal perturbation vector at step r which is obtained based on d(r−1). $\boldsymbol { d } ^ { ( r - 1 ) }$

Note that, at each step, the objective function in (12) decreases. Since the objective function is monotonically decreasing and bounded from below, the solution converges after several updates. We note that due to the approximation used in (11), the solution may not be a global optimal. Nevertheless, as we can see from Theorem 1, it is analytically tractable and, hence, it has a low computational complexity. Here, we use $\ b { d } ^ { * }$ to represent the vector of nearly-optimal distances of drones from the original of the array. Next, we use $\ b { d } ^ { * }$ to determine the optimal 3D locations of the drones that result in a maximum array directivity towards a given ground user.

# B. Optimal Locations of Drones

Here, following from Subsection III-A, we derive the optimal 3D positions of drones that yields a maximum directivity of the drone-based antenna array. Let $( x _ { i } ^ { \mathrm { u } } , y _ { i } ^ { \mathrm { u } } , z _ { i } ^ { \mathrm { u } } )$ and $( x _ { o } , y _ { o } , z _ { o } )$ (be, respectively, the 3D locations of user $i \in \mathcal { L }$ ( )and the origin of the antenna array.

Without loss of generality, we translate the origin of our coordinate system to the origin of the antenna array. In other words, we assume that the arrays’ center is the origin of our translated coordinate system. In this case, the 3D location of user i will be $( x _ { i } ^ { \mathrm { u } } - x _ { o } , y _ { i } ^ { \mathrm { u } } - y _ { o } , z _ { i } ^ { \mathrm { u } } - z _ { o } )$ . Subsequently, the polar ( )and azimuthal angles of user i in the spherical coordinate (with an origin of antenna array) are given by:

$$
\theta_ {i} = \cos^ {- 1} \left[ \frac {z _ {i} ^ {u} - z _ {o}}{\sqrt {\left(x _ {i} ^ {u} - x _ {o}\right) ^ {2} + \left(y _ {i} ^ {u} - y _ {o}\right) ^ {2} + \left(z _ {i} ^ {u} - z _ {o}\right) ^ {2}}} \right], \tag {21}
$$

$$
\phi_ {i} = \sin^ {- 1} \left[ \frac {y _ {i} ^ {u} - y _ {o}}{\sqrt {(x _ {i} ^ {u} - x _ {o}) ^ {2} + (y _ {i} ^ {u} - y _ {o}) ^ {2}}} \right]. \tag {22}
$$

Now, the optimal locations of the drones in the antenna array is given as follows.

Theorem 2: The optimal locations of the drones for maximizing the directivity of the drone-based antenna array towards a given ground user will be:

$$
\begin{array}{l} \left(x _ {m} ^ {*}, y _ {m} ^ {*}, z _ {m} ^ {*}\right) ^ {T} \\ = \left\{ \begin{array}{c} \boldsymbol {R} _ {\text { rot }} \left(d _ {m} ^ {*} \sin \alpha_ {o} \cos \gamma_ {o}, d _ {m} ^ {*} \sin \alpha_ {o} \sin \beta_ {o}, d _ {m} ^ {*} \cos \alpha_ {o}\right) ^ {T}, \\ m \leq M / 2, \\ - \boldsymbol {R} _ {\text { rot }} \left(d _ {m} ^ {*} \sin \alpha_ {o} \cos \gamma_ {o}, d _ {m} ^ {*} \sin \alpha_ {o} \sin \gamma_ {o}, d _ {m} ^ {*} \cos \alpha_ {o}\right) ^ {T}, \\ m > M / 2, \end{array} \right. \tag {23} \\ \end{array}
$$

where $\alpha _ { o }$ and $\gamma _ { o }$ are the initial polar and azimuthal angles of drone $m \le M / 2$ with respect to the array’s center. $R _ { \mathrm { r o t } }$ is the 2rotation matrix for updating drones’ positions, given by:

$$
\begin{array}{l} R _ {\text { rot }} \\ = \left( \begin{array}{c c c} a _ {x} ^ {2} (1 - \delta) + \delta & a _ {x} a _ {y} (1 - \delta) - \lambda a _ {z} & a _ {x} a _ {z} (1 - \delta) + \lambda a _ {y} \\ a _ {x} a _ {y} (1 - \delta) + \lambda a _ {z} & a _ {y} ^ {2} (1 - \delta) + \delta & a _ {y} a _ {z} (1 - \delta) - \lambda a _ {x} \\ a _ {x} a _ {z} (1 - \delta) - \lambda a _ {y} & a _ {y} a _ {z} (1 - \delta) + \lambda a _ {x} & a _ {z} ^ {2} (1 - \delta) + \delta \end{array} \right), \tag {24} \\ \end{array}
$$

$$
\begin{array}{l} \text {where} \delta = \| \boldsymbol {q} _ {\boldsymbol {i}} \cdot \boldsymbol {q} _ {\max} \|, \lambda = \sqrt {1 - \delta^ {2}}, \boldsymbol {q} _ {\boldsymbol {i}} = \\ \left( \begin{array}{c} \sin \theta_ {i} \cos \phi_ {i} \\ \sin \theta_ {i} \sin \phi_ {i} \\ \cos \theta_ {i} \end{array} \right), \boldsymbol {q} _ {\max} = \left( \begin{array}{c} \sin \theta_ {\max} \cos \phi_ {\max} \\ \sin \theta_ {\max} \sin \phi_ {\max} \\ \cos \theta_ {\max} \end{array} \right). \text {Moreover}, a _ {x}, \end{array}
$$

$a _ { y } .$ cos, and $a _ { z }$ cosare the elements of vector $\mathbf { \boldsymbol { a } } = \left( a _ { x } , a _ { y } , a _ { z } \right) ^ { T } =$ $q _ { i } \times$ qmax.

Proof: See Appendix B.

Using Theorem 2, we can find the optimal locations of the drones such that the directivity of the drone-based antenna

![](images/3e4648e5d13f535a0fe78ca2f7b38c87e9f2f5ae037c7d28ad6db674fff2af6a.jpg)

<details>
<summary>text_image</summary>

Drone l
Drone m
d_m*
Drone M
y
z
x
Maximum
directivity
(θ_max, φ_max)
User i
(θ_i, φ_i)
</details>

Fig. 2. Illustrative figure for Theorem 2.

# Algorithm 1 Optimizing Drones’ Locations for Maximum Array Gain Towards User i

1: Inputs: Locations of user $, ( x _ { i } ^ { \mathrm { u } } , y _ { i } ^ { \mathrm { u } } , z _ { i } ^ { \mathrm { u } } )$ , and origin of array, $( x _ { o } , y _ { o } , z _ { o } ) .$ .   
( )2: Outputs: Optimal drones’ positions, $( x _ { m , i } ^ { * } , y _ { m , i } ^ { * } , z _ { m , i } ^ { * } ) .$ , $\forall m \in { \mathcal { M } } .$   
3: Set initial values for distance between drones, d.   
4: Find $e ^ { * }$ by using (16)-(18).   
5: Update d based on (19).   
6: Repeat steps (4) and (5) to find the optimal spacing vector $\ b { d } ^ { * }$ .   
7: Use (21)-(61) to determine $( x _ { m } ^ { * } , y _ { m } ^ { * } , z _ { m } ^ { * } ) .$ ∀m $\in { \mathcal { M } } .$

array is maximized towards any given ground user. Moreover, this theorem can be used to dynamically update the drones’ positions for beam steering while serving different ground users.

Thus far, we have determined the optimal locations of the drones in the antenna array to maximize the directivity of the array towards any given ground user. Therefore, the data rate is maximized and, hence, the transmission time for serving the user is minimized. In Algorithm 1, we have summarized the key steps needed for optimizing the locations of drones with respect to the center of the array.

Hence, using Algorithm 1, we can determine the optimal locations of the array’s drones with respect to each ground user. To serve multiple users spread over a given geographical area, the drones must dynamically move between these determined optimal locations. This, in turn, yields a control time for drone movement that must be optimized. From (5), we can see that the service time decreases by reducing the control time. Therefore, next, using the determined drones’ locations in Section III, we minimize the control time of the drones.

# IV. TIME-OPTIMAL CONTROL OF DRONES

Here, our goal is to minimize the control time that the drones spend to move between the optimal locations which are determined in Section III. While moving the drone-based antenna array, we assume that the array rotates around its center in order to steer the beam and serve different users. Hence, the order of the drones (i.e., the drones’ indices) on the array does not change while moving the array. This approach significantly facilitates collision avoidance between the drones as their paths do not intersect.

![](images/05427e6ce9fca61c07c38aef5d7b9b90c3b9faf5bdb8a062f1afe3f7f39a258b.jpg)

<details>
<summary>text_image</summary>

v₂
l
mₚg
v₁
Rotor 1
z
x
y
v₃
Rotor 2
z_b
Yaw
Yaw
Roll
body
frame
Pitch
y_b
Rotor 3
Rotor 1
Rotor 4
Thrust
</details>

Fig. 3. A quadrotor drone.

In this section, we derive the optimal rotors’ speeds for which the quadrotor drones can move and stabilize their positions within a minimum time. Moreover, we account for wind effects while analyzing the drones’ stability in the proposed drone-based antenna array system.

# A. Dynamic Model of a Quadrotor Drone

Fig. 3 shows an illustrative example of a quadrotor drone. This drone has four rotors that can control the hovering and mobility of the drone. In particular, by adjusting the speed of these rotors, the drone can hover and move horizontally or vertically. Let $( x , y , z )$ be the 3D position of the drone. Also, we use $( \psi _ { \mathrm { r } } , \psi _ { \mathrm { p } } , \psi _ { \mathrm { y } } )$ )to represent the roll, pitch, and yaw angles ( )that capture the orientation (i.e., attitude) of the drone. Roll, pitch, and yaw are rotation angles defined with respect to the body frame. Here, the origin of the body frame coordinate system (represented by the $x _ { \mathrm { b } } - y _ { \mathrm { b } } - z _ { \mathrm { b } }$ axes) is at the center of the drone, $x _ { \mathrm { b } }$ is along the arm between rotors 1 and 3, yb is along the arm between rotors 2 and 4, and $z _ { \mathrm { b } }$ is in the direction of the cross product of the $x _ { \mathrm { b } }$ and $y _ { \mathrm { b } }$ axes. In this case, roll, pitch, and yaw, are rotations along $x _ { \mathrm { b } } , y _ { \mathrm { b } } .$ , and $z _ { \mathbf { b } } .$ .

The speed of rotor $i \in \{ 1 , 2 , 3 , 4 \}$ is given by $v _ { i }$ . For a 1 2 3 4quadrotor drone, the total thrust and torques that lead to the roll, pitch, and yaw movements are related to the rotors’ speeds by [31]:

$$
\left( \begin{array}{c} T _ {\text { tot }} \\ \kappa_ {1} \\ \kappa_ {2} \\ \kappa_ {3} \end{array} \right) = \left( \begin{array}{c c c c} \rho_ {1} & \rho_ {1} & \rho_ {1} & \rho_ {1} \\ 0 & - l \rho_ {1} & 0 & l \rho_ {1} \\ - l \rho_ {1} & 0 & l \rho_ {1} & 0 \\ - \rho_ {2} & \rho_ {2} & - \rho_ {2} & \rho_ {2} \end{array} \right) \left( \begin{array}{c} v _ {1} ^ {2} \\ v _ {2} ^ {2} \\ v _ {3} ^ {2} \\ v _ {4} ^ {2} \end{array} \right), \tag {25}
$$

where $T _ { \mathrm { t o t } }$ is the total thrust generated by the rotors. The direction of the thrust is upward perpendicular to the rotors’ plane, as we can see from Fig. 3. $\kappa _ { 1 } , ~ \kappa _ { 2 } .$ , and $\kappa _ { 3 }$ are the torques for roll, pitch and yaw movements. $\rho _ { 1 }$ and $\rho _ { 2 }$ are lift and torque coefficients, and l is the distance from each rotor to the center of the drone.

We can now write the dynamic equations of a quadrotor drone in presence of an external wind force as follows3:

$$
\ddot {x} = \left(\cos \psi_ {r} \sin \psi_ {p} \cos \psi_ {y} + \sin \psi_ {r} \sin \psi_ {y}\right) \frac {T _ {\text {tot}}}{m _ {D}} + \frac {F _ {x} ^ {\mathrm{W}}}{m _ {D}}, \tag {26}
$$

$$
\ddot {y} = \left(\cos \psi_ {r} \sin \psi_ {p} \sin \psi_ {y} + \sin \psi_ {r} \cos \psi_ {y}\right) \frac {T _ {\text {tot}}}{m _ {D}} + \frac {F _ {y} ^ {\mathrm{W}}}{m _ {D}}, \tag {27}
$$

$$
\ddot {z} = \left(\cos \psi_ {r} \cos \psi_ {p}\right) \frac {T _ {\mathrm{tot}}}{m _ {D}} - g + \frac {F _ {z} ^ {\mathrm{W}}}{m _ {D}}, \tag {28}
$$

$$
\ddot {\psi} _ {\mathrm{r}} = \frac {\kappa_ {2}}{I _ {x}}, \tag {29}
$$

$$
\ddot {\psi} _ {\mathrm{p}} = \frac {\kappa_ {1}}{I _ {y}}, \tag {30}
$$

$$
\ddot {\psi} _ {\mathrm{y}} = \frac {\kappa_ {3}}{I _ {z}}, \tag {31}
$$

where $m _ { D }$ is the mass of the drone, and $g$ is the gravity acceleration. F Wx , F Wy , $F _ { x } ^ { \mathrm { W } } , \ F _ { y } ^ { \mathrm { W } }$ Fy， and F Wz $F _ { z } ^ { \mathrm { W } }$ are the wind forces in positive $x , \ y ,$ and z directions. Also, $I _ { x } , \ I _ { y } , \ I _ { z }$ are constant values which represent the moments of inertia along $x , y ,$ and z directions. From (25), we can see that the total thrust, $T _ { \mathrm { t o t } }$ is directly related to the rotor speed. Also, (26)-(28) capture the relationship between $T _ { \mathrm { t o t } }$ and the drone’s acceleration. Hence, using (25)-(28), we can find the drone’s accelerations in the x, y, and z directions. These accelerations are directly related to position and velocity of the drone using classical kinematic equations [32].

Given the dynamic model of the drone, we aim to find the optimal speeds of the rotors such that the drone moves from an initial location $( x _ { I } , y _ { I } , z _ { I } )$ to a new location $\left( x _ { D } , y _ { D } , z _ { D } \right)$ ( ) ( )within a minimum time duration. Under such optimal control inputs $( \mathrm { i . e . , }$ rotors’ speed), the time needed for each UAV to update its location based on the users’ locations will be minimized. Note that the drone must be stationary at its new location and it does not move in x, y, or z direction. Let $( x ( t ) , y ( t ) , z ( t ) )$ and $( \psi _ { \mathrm { r } } ( t ) , \psi _ { \mathrm { p } } ( t ) , \psi _ { \mathrm { y } } ( t ) )$ be the 3D location ( ( ) ( ) ( )) ( ( ) ( )and orientation of the drone at time $t \in [ 0 , T _ { I , D } ]$ , with $T _ { I , D }$ [0 ]being the total control time for moving from location I to location $D .$ Now, we can formulate our time-optimal control problem for a drone, moving from location I to location D, as follows:

$$
\underset {\left[ v _ {1} (t), v _ {2} (t), v _ {3} (t), v _ {4} (t) \right]} {\text { minimize }} T _ {I, D}, \tag {32}
$$

$$
\text { st. } | v _ {w} (t) | \leq v _ {\max}, \forall w \in \{1,..., 4 \}, \tag {33}
$$

$$
(x (0), y (0), z (0)) = \left(x _ {I}, y _ {I}, z _ {I}\right), \tag {34}
$$

$$
(x (T _ {I, D}), y (T _ {I, D}), z (T _ {I, D})) = (x _ {D}, y _ {D}, z _ {D}), \tag {35}
$$

$$
(\dot {x} (T _ {I, D}), \dot {y} (T _ {I, D}), \dot {z} (T _ {I, D})) = (0, 0, 0), \tag {36}
$$

where $[ v _ { 1 } ( t ) , v _ { 2 } ( t ) , v _ { 3 } ( t ) , v _ { 4 } ( t ) ]$ represents the rotors’ speeds [ ( ) ( )at time t. In (33), $v _ { \mathrm { m a x } }$ ( )]is the maximum possible speed of each rotor. Constraints (34) and (35) show the initial and final location of the drone (which are determined based on Algorithm 1), (36) indicates that the drone will be stationary at its final location. Here, we assume $( \psi _ { r } ( 0 ) , \psi _ { p } ( 0 ) , \psi _ { y } ( 0 ) ) = ( 0 , 0 , 0 )$ .

3Note that, here, drag coefficients are assumed to be negligible.

In (32), the goal is to minimize the control time that a drone needs in order to move between two locations, along a linear path. The objective function is the control time, and the optimization variables are the speeds of rotors. In (5), $T _ { I , D }$ is the control time that a quadrotor drone spends to move from location I to location D, the optimization variables are the speeds of rotors at time t, which are denoted by $v _ { 1 } ( t ) , v _ { 2 } ( t )$ , $v _ { 3 } ( t )$ , and $v _ { 4 } ( t )$ ( ) ( ). Note that in (5), the control time for serving ( )user $i , T _ { i } ^ { \mathrm { c r l } } .$ ( ), is equal to the maximum control time among the drones that update their positions according to the user.

Our problem in (32) is difficult to solve due to its non-linear nature, and coupled relation of the dynamic system parameters as well as the infinite number of optimization variables given the continuous time interval $[ 0 , T _ { I , D } ]$ . Consequently, [0 ]in general, the exact analytical solution to such nonlinear time-optimal control problem may not be explicitly derived as pointed out in [22] and [23]. To provide a tractable solution to our time-optimal control problem in (32), we decompose the movements and orientation changes of drones. In particular, we minimize the time durations needed for orientation adjustment and displacement of the drone, separately. While this approach yields a suboptimal solution, it can be used to derive a closed-form expression for the control inputs (i.e., rotors’ speeds) in (32) and, thus, it is remarkably easy to implement. In addition, the computational time, which is a key constraint in wireless drone systems, can be reduced.

Now, we aim to derive the optimal speeds of rotors for which the drone can update its locations within a minimum time duration. To this end, we first present the following lemma from control theory [25] which will be then used to derive the optimal rotors’ speeds.

Lemma 1: (From [25]): Consider the state space equations for an object within time duration , T :

$$
\dot {\boldsymbol {x}} (t) = \boldsymbol {A} \boldsymbol {x} (t) + \boldsymbol {b} u (t), \quad u _ {\min} \leq u (t) \leq u _ {\max}, \tag {37}
$$

$$
\boldsymbol {x} (0) = \boldsymbol {x} _ {1}, \tag {38}
$$

$$
\boldsymbol {x} (T) = \boldsymbol {x} _ {2}, \tag {39}
$$

where $\pmb { x } ( t ) \in \mathbb { R } ^ { N _ { s } }$ is the state vector of the object at time $t \in [ 0 , T ] , N _ { s }$ is the number of state’s elements. $u ( t )$ is a [0 ]bounded control input with $u _ { \mathrm { m a x } }$ and $u _ { \mathrm { m i n } }$ ( )being its maximum and minimum values. $\pmb { A } \in \mathbb { R } ^ { N _ { s } \times N _ { s } }$ and $\pmb { b } \in \bar { \mathbb { R } } ^ { N _ { s } }$ are given constant matrices. x1 and x2 are the initial and final state of the object. Then, the optimal control input that leads to a minimum state update time $T ^ { * }$ is given by [25]:

$$
u ^ {*} (t) = \left\{ \begin{array}{l l} u _ {\max}, & t \leq \tau , \\ u _ {\min}, & t > \tau , \end{array} \right. \tag {40}
$$

where τ is called the switching time at which the control input changes. In this case, the control time decreases by increasing $u _ { \mathrm { m a x } }$ and/or decreasing $u _ { \mathrm { m i n } }$ .

Lemma 1 provides the solution to the time-optimal control problem for a dynamic system which is characterized by (37)-(39). In particular, the optimal control solution given in (40) is refereed to as bang-bang solution [25]. In this case, the optimal control input is always at its extreme value (i.e. maximum or minimum). Next, we provide a new lemma (Lemma 2) which will be used along with Lemma 1 to solve (32).

![](images/d39a045d1f29be00e2cb9ea114bfd74a3e0f12d7201e0acae1ce0d44fe09ccee.jpg)

<details>
<summary>text_image</summary>

P_D : (|P_D|, θ_D, φ_D)
Location D
F : (F, α, β)
Drone's center
z
Polar
x
Azimuthal
y
F_ex : (|F_ex|, θ_ex, φ_ex)
</details>

Fig. 4. Drone’s movement in presence of an external force.

Lemma 2: Consider a drone that needs to move towards a given location D (as shown in Fig.4), with a coordinate $\boldsymbol { P } _ { D } = ( x _ { D } , y _ { D } , z _ { D } )$ , in presence of an external force $\boldsymbol { F } _ { \mathrm { e x } } =$ $( F _ { \mathrm { e x } , x } , F _ { \mathrm { e x } , y } , F _ { \mathrm { e x } , z } )$ ) =. The drone’s orientation that leads to a ( )movement with the maximum acceleration towards $P _ { D }$ is:

$$
\psi_ {\mathrm{p}} ^ {D} = \cos^ {- 1} \left[ \frac {A \cos \theta_ {D} - | \boldsymbol {F} _ {\mathrm{ex}} | \cos \theta_ {\mathrm{ex}}}{F} \right], \tag {41}
$$

$$
\psi_ {\mathrm{r}} ^ {D} = \tan^ {- 1} \left(\tan \beta \times \sin \psi_ {p} ^ {D}\right), \tag {42}
$$

$$
\psi_ {\mathrm{y}} ^ {D} = 0, \tag {43}
$$

where

$$
\begin{array}{l} A = \left[ F ^ {2} + | \boldsymbol {F} _ {\mathrm{ex}} | ^ {2} + 2 F | \boldsymbol {F} _ {\mathrm{ex}} | \cos \left(\gamma + \sin^ {- 1} \left(\frac {| \boldsymbol {F} _ {\mathrm{ex}} |}{F} \sin \gamma\right)\right) \right] ^ {1 / 2}, \\ \beta \quad = \quad \phi_ {D} - \sin^ {- 1} \left[ \frac {\left| F _ {\mathrm{ex}} \right| \sin \theta_ {\mathrm{ex}} \sin (\phi_ {D} - \phi_ {\mathrm{ex}})}{F \sin \psi_ {p} ^ {D}} \right], \quad \gamma = \\ \end{array}
$$

= tanProof: See Appendix C.

Lemma 2, can be used to determine the optimal orientation of the drone that enables it to move towards any given location in presence of external forces. Next, using Lemmas 1 and 2, we derive the speed of each drone’s rotor for which the control time is minimized. In this case, we find the rotors’ speeds at several pre-defined stages in which the drone updates its position or orientation.

Theorem 3: The optimal speeds of rotors with which a drone can move from location , , , and , ,  orientation, to location $\left( x _ { D } , y _ { D } , z _ { D } \right)$ within a minimum control time are given by:

Stage 1:

$$
\left\{ \begin{array}{l} v _ {2} = 0, v _ {1} = v _ {3} = \frac {1}{\sqrt {2}} v _ {\max}, v _ {4} = v _ {\max}, \text {   if   } 0 <   t \leq \tau_ {1}, \\ v _ {4} = 0, v _ {1} = v _ {3} = \frac {1}{\sqrt {2}} v _ {\max}, v _ {2} = v _ {\max} \text {   if   } \tau_ {1} <   t \leq \tau_ {2}, \\ v _ {1} = 0, v _ {2} = v _ {4} = \frac {1}{\sqrt {2}} v _ {\max}, v _ {3} = v _ {\max}, \text {   if   } \tau_ {2} <   t \leq \tau_ {3}, \\ v _ {3} = 0, v _ {2} = v _ {4} = \frac {1}{\sqrt {2}} v _ {\max}, v _ {1} = v _ {\max}, \text {   if   } \tau_ {3} <   t \leq \tau_ {4}. \end{array} \right. \tag {44}
$$

Stage 2: $v _ { 1 } = v _ { 2 } = v _ { 3 } = v _ { 4 } = v _ { \mathrm { { m a x } } } , ~ { \mathrm { i f } } ~ \tau _ { 4 } < t \leq \tau _ { 5 } .$ . (45)

Stage 3:

$$
\left\{ \begin{array}{l} v _ {2} = 0, v _ {1} = v _ {3} = \frac {1}{\sqrt {2}} v _ {\max}, v _ {4} = v _ {\max}, \text {   if   } \tau_ {5} <   t \leq \tau_ {6}, \\ v _ {4} = 0, v _ {1} = v _ {3} = \frac {1}{\sqrt {2}} v _ {\max}, v _ {2} = v _ {\max}, \text {   if   } \tau_ {6} <   t \leq \tau_ {7}, \\ v _ {1} = 0, v _ {2} = v _ {4} = v _ {\max}, v _ {3} = v _ {\max}, \text {   if   } \tau_ {7} <   t \leq \tau_ {8}, \\ v _ {3} = 0, v _ {2} = v _ {4} = \frac {1}{\sqrt {2}} v _ {\max}, v _ {1} = v _ {\max}, \text {   if   } \tau_ {8} <   t \leq \tau_ {9}. \end{array} \right. \tag {46}
$$

Stage 4: $v _ { 1 } = v _ { 2 } = v _ { 3 } = v _ { 4 } = v _ { \mathrm { m a x } }$ , if $\tau _ { 9 } < t \leq \tau _ { 1 0 }$ . (47)

Stage 5:

$$
\left\{ \begin{array}{l} v _ {2} = 0, v _ {1} = v _ {3} = \frac {1}{\sqrt {2}} v _ {\max}, v _ {4} = v _ {\max}, \text {   if   } \tau_ {1 0} <   t \leq \tau_ {1 1}, \\ v _ {4} = 0, v _ {1} = v _ {3} = \frac {1}{\sqrt {2}} v _ {\max}, v _ {2} = v _ {\max}, \text {   if   } \tau_ {1 1} <   t \leq \tau_ {1 2}, \\ v _ {1} = 0, v _ {2} = v _ {4} = \frac {1}{\sqrt {2}} v _ {\max}, v _ {3} = v _ {\max}, \text {   if   } \tau_ {1 2} <   t \leq \tau_ {1 3}, \\ v _ {3} = 0, v _ {2} = v _ {4} = \frac {1}{\sqrt {2}} v _ {\max}, v _ {1} = v _ {\max}, \text {   if   } \tau_ {1 3} <   t \leq \tau_ {1 4}. \end{array} \right. \tag {48}
$$

Stage 6: $v _ { 1 } = v _ { 2 } = v _ { 3 } = v _ { 4 } = v _ { \mathrm { F } } , { \mathrm { ~ i f ~ } } t > \tau _ { 1 4 } .$ . (49)

Also, the total control time of the drone can be given by:

$$
\begin{array}{l} T _ {I, D} = \sqrt {2 d _ {D} \left(\frac {m _ {D}}{A _ {s 2}} - \frac {m _ {D}}{A _ {s 4}}\right)} \\ + \frac {2}{v _ {\mathrm{max}}} \Big [ \sqrt {\frac {\Delta \psi_ {\mathrm{p} , 1} I _ {y}}{l \rho_ {1}}} + \sqrt {\frac {\Delta \psi_ {\mathrm{r} , 1} I _ {x}}{l \rho_ {1}}} + \sqrt {\frac {\Delta \psi_ {\mathrm{p} , 3} I _ {y}}{l \rho_ {1}}} \\ \left. + \sqrt {\frac {\Delta \psi_ {\mathrm{r} , 3} I _ {x}}{l \rho_ {1}}} + \sqrt {\frac {\Delta \psi_ {\mathrm{p} , 5} I _ {y}}{l \rho_ {1}}} + \sqrt {\frac {\Delta \psi_ {\mathrm{r} , 5} I _ {x}}{l \rho_ {1}}} \right], \tag {50} \\ \end{array}
$$

where $v _ { \mathrm { m a x } } , \ v _ { \mathrm { i n } } ,$ , and vF are, respectively, the maximum, the initial, and the final speeds of rotors. $m _ { D }$ is the drone’s mass, $\Delta \psi _ { \mathrm { r } , i }$ and $\Delta \psi _ { \mathsf { p } , i }$ are the roll and pitch changes in Stage $i , \ d _ { D }$ Δ Δis the distance between the initial and final locations of the drone. $\tau _ { 1 } , . . . , \tau _ { 1 4 }$ are the switching times at which the rotors’ speeds changes. The values of switching times and $v _ { F }$ are provided in the proof of this theorem.

Proof: See Appendix D.

In Theorem 3, Stages 1, 3, and 5 correspond to the orientation changes, Stages 2 and 4 are related to the drone’s displacement, and Stage 6 represents the drone’s stability condition. Note that vF is adjusted such that the drone’s stability is ensured at its final location. In (50), $A _ { s 2 }$ and $A _ { s 4 }$ are, respectively, the total forces towards the drone’s destination at Stages 2 and 4.

Using Theorem 3, we can find the speeds of the rotors (at different time instances) that enable each to move towards its destination within a minimum time. The control time depends on the destination of the drone, external forces (e.g. wind and gravity), the rotors’ speed, and the drone’s weight.

# B. Collision Avoidance for Moving Drones

First, we determine a situation in which collision between two drones when updating their locations is possible. Then, we propose a solution to avoid the collision situation.

![](images/033dc5b66b759abd7f37883feaf4b52efc84d564f7ebe7511588f0b1e5828cd4.jpg)

<details>
<summary>text_image</summary>

Array axis
Drone 2
a
d
x
Drone 1
d
Rotated
array axis
</details>

Fig. 5. Drones’ movements during the antenna array rotation (linear path).

![](images/210cf744f6a943514d2107e1dda7b9d03d0ad7ab77eea2b225dd12c007497f23.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Drone 1"] --> B["Array axis"]
    B --> C["Drone 2"]
    C --> D["Array axis"]
    D --> E["Rotated axis"]
    E --> F["Orbital axis"]
    F --> G["Orbital axis"]
    G --> H["Orbital axis"]
    H --> I["Orbital axis"]
    I --> J["Orbital axis"]
    J --> K["Orbital axis"]
    K --> L["Orbital axis"]
    L --> M["Orbital axis"]
    M --> N["Orbital axis"]
    N --> O["Orbital axis"]
    O --> P["Orbital axis"]
    P --> Q["Orbital axis"]
    Q --> R["Orbital axis"]
    R --> S["Orbital axis"]
    S --> T["Orbital axis"]
    T --> U["Orbital axis"]
    U --> V["Orbital axis"]
    V --> W["Orbital axis"]
    W --> X["Orbital axis"]
    X --> Y["Orbital axis"]
    Y --> Z["Orbital axis"]
    Z --> AA["Orbital axis"]
    AA --> AB["Orbital axis"]
    AB --> AC["Orbital axis"]
    AC --> AD["Orbital axis"]
    AD --> AE["Orbital axis"]
    AE --> AF["Orbital axis"]
    AF --> AG["Orbital axis"]
```
</details>

Fig. 6. Drones’ movements during the antenna array rotation (arc path).

Consider two adjacent drones that need to change their locations, as shown in Fig. 5. Clearly, the minimum distance between drones along their path is $x = d \sin \alpha ,$ where α and =d are shown in Fig. 5. In this case, if $x \ge D _ { \mathrm { m i n } } .$ , collision does not occur. Therefore, drones can move on a linear path without any collision However, if $x \ < \ D _ { \mathrm { { m i n } } }$ , it is possible that the drones collide while they move. One way to avoid collision is to use non-straight paths for drones. For instance, an arc shape trajectory (as shown in Fig. 6) ensures that the distance between adjacent drones remains above the minimum required distance, $D _ { \mathrm { m i n } }$ .

# C. User Scheduling Order

Another factor that can impact the total control time of the drones is the user scheduling order. While any arbitrary user scheduling can be considered in our model, we adopt a scheduling order that yields a minimum total control time. To this end, we solve the following optimization problem which determines the optimal scheduling order:

$$
\underset {[ a _ {i j} ] _ {L \times L}} {\text { minimize }} \sum_ {i = 1, i \neq j} ^ {L} \sum_ {j = 1} ^ {L} a _ {i j} T _ {i j}, \tag {51}
$$

$$
\text { st. } \sum_ {j = 1, j \neq i} ^ {L} a _ {i j} = 1, \quad \forall i \in \mathcal {L}, \quad \sum_ {i = 1, i \neq j} ^ {L} a _ {i j} = 1, \quad \forall j \in \mathcal {L}, \tag {52}
$$

$$
a _ {i j} = \left\{ \begin{array}{l l} 1 & \text { if   user } j \text { is   served   after   user } i, \\ 0 & \text { otherwise }, \end{array} \right. \tag {53}
$$

where L is the number of ground users in set ${ \mathcal { L } } ,$ and $T _ { i j }$ is the control time of drones when user $j$ is served after user i. $a _ { i j }$ is a binary variable which is 1 if user $j$ is served after user i, and $[ a _ { i j } ] _ { L \times L }$ is a matrix that represents the scheduling order. [ ]Constraint (52) indicates that each user is served only once. The optimization problem in (51) is a classical integer linear programming which can be solved using various methods such as a branch-and-bound algorithm [33].

In summary, our approach for minimizing the service time, which is composed of the transmission time and the control

Algorithm 2 Steps for Minimizing the Service Time by Solving (5)

1: Inputs: Locations of users, $( x _ { i } ^ { \mathrm { u } } , y _ { i } ^ { \mathrm { u } } , z _ { i } ^ { \mathrm { u } } ) , \forall i \in \mathcal { L } ,$ and origin of array, $( x _ { o } , y _ { o } , z _ { o } )$ .   
( )2: Outputs: Optimal drones’ positions, $( x _ { m , i } ^ { * } , y _ { m , i } ^ { * } , z _ { m , i } ^ { * } ) ,$ rotors’ speeds, $v _ { m w } ( t )$ , ∀m $\in \mathcal { M } , \forall i \in \mathcal { L } , w \in$ $\{ 1 , . . . , 4 \}$ ( ), and total service time.   
1 43: Using Algorithm 1, find the optimal locations of drones with respect to each user, $( x _ { m , i } ^ { * } , y _ { m , i } ^ { * } , z _ { m , i } ^ { * } )$ .   
( )4: Using Theorem 3 and Lemma 2, for each drone, determine the rotors’ speeds for moving from $( x _ { m , i - 1 } ^ { * } , y _ { m , i - 1 } ^ { * } , z _ { m , i - 1 } ^ { * } )$ to $( x _ { m , i } ^ { * } , y _ { m , i } ^ { * } , z _ { m , i } ^ { * } )$ .   
( ) ( )5: Compute the total service time based on (5), (32), and (50).

TABLE I MAIN SIMULATION PARAMETERS 

<table><tr><td>Parameter</td><td>Description</td><td>Value</td></tr><tr><td> $f_c$ </td><td>Carrier frequency</td><td>300 MHz</td></tr><tr><td> $P_i$ </td><td>Drone transmit power</td><td>0.1 W</td></tr><tr><td> $N_o$ </td><td>Total noise power spectral density</td><td>-157 dBm/Hz</td></tr><tr><td>N</td><td>Number of ground users</td><td>100</td></tr><tr><td> $(x_o, y_o, z_o)$ </td><td>Array&#x27;s center coordinate</td><td>(0,0,100) in meters</td></tr><tr><td> $q_i$ </td><td>Load per user</td><td>100 Mb</td></tr><tr><td>α</td><td>Pathloss exponent</td><td>3</td></tr><tr><td> $I_x, I_y$ </td><td>Moments of inertia</td><td>4.9 × 10-3kg.m2[34]</td></tr><tr><td> $m_D$ </td><td>Mass of each drone</td><td>0.5 kg</td></tr><tr><td>l</td><td>Distance of a rotor to drone&#x27;s center</td><td>20 cm</td></tr><tr><td> $ρ_1$ </td><td>lift coefficient</td><td>2.9 × 10-5[34]</td></tr><tr><td> $β_m - β_{m-1}$ </td><td>Phase excitation difference for two adjacent antennas</td><td> $\frac{\pi}{5(M-1)}$ </td></tr></table>

time, is as follows. In the first step, using the approach of Section III, we minimize the transmission time for each ground user by optimizing the positions of drones with respect to the ground users. Then, based on these determined optimal drones’ locations, we minimize the control time needed for adjusting the movement and orientations of drones. In Algorithm 2, we summarize our approach for minimizing the service time.

# V. SIMULATION RESULTS AND ANALYSIS

For our simulations, we consider a number of ground users uniformly distributed within a square area of size  km× km. 1 1Unless stated otherwise, the number of users is 100, and the number of drones4 that form a linear array is assumed to be 10. The main simulation parameters are given in Table I. We compare the performance of our drone-based antenna array system with a case in which a drone-based antenna array uses a fixed uniform drone separation, without any repositioning. For the benchmark, referred to as fixed-array case, we consider half-wavelength drone spacing.5

First, we show an example on how the drones are separated in the proposed drone-based antenna array system. This result is provided in Table II for two different carrier frequencies.

Fig. 7 shows the total service time for the drone antenna array and the fixed-array case. For a given bandwidth, our proposed drone antenna array outperforms the fixed-array case

4In our simulations, each drone in the array has an omni-directional antenna, as in [17] and [18].

5For the fixed-array case, we consider electronic beam steering with a 3 dB gain loss due to an imperfect phase synchronization.

TABLE II SEPARATION DISTANCE OF ADJACENT DRONES IN AN AERIAL ANTENNA ARRAY WITH 10 DRONES 

<table><tr><td>Drones&#x27; separations (cm),  ${f}_{c} = {300}\mathrm{{MHz}},\lambda = 1\mathrm{\;m}$ </td><td>Drones&#x27; separations (cm),  ${f}_{c} = {500}\mathrm{{MHz}},\lambda = {0.6}\mathrm{\;m}$ </td><td>Compared to wavelength (λ)</td></tr><tr><td>81.9</td><td>49.1</td><td>81.9 λ</td></tr><tr><td>88.7</td><td>53.2</td><td>88.7 λ</td></tr><tr><td>89.8</td><td>54.1</td><td>89.8 λ</td></tr><tr><td>90.7</td><td>54.3</td><td>90.7 λ</td></tr><tr><td>89.8</td><td>54.1</td><td>89.8 λ</td></tr><tr><td>88.7</td><td>53.2</td><td>88.7 λ</td></tr><tr><td>81.9</td><td>49.1</td><td>81.9 λ</td></tr></table>

![](images/d633e38c04fd1a979e1f365453e8f9f86b88f3eed56548e9b68e05a3d1020721.jpg)

<details>
<summary>line</summary>

| Bandwidth (Mhz) | Proposed drone antenna array | Fixed drone antenna array |
| --------------- | ---------------------------- | ------------------------- |
| 1               | 19.5                         | 25.0                      |
| 2               | 13.0                         | 16.0                      |
| 3               | 9.0                          | 11.0                      |
| 4               | 7.0                          | 8.5                       |
| 5               | 6.0                          | 7.5                       |
</details>

Fig. 7. Service time vs. bandwidth for the drone antenna-array and fixed-array cases.

in terms of service time. This is due to the fact that, in the proposed approach, the drones’ locations (and drone spacing) are optimized such that the array antenna gain towards each user is maximized, hence reducing the transmission time. Fig. 7 also shows the tradeoff between bandwidth and service time. Clearly, the service time decreases by using more bandwidth which effectively provides a higher data rate. Fig. 7 shows that the drone antenna array improves spectral efficiency compared to the fixed-array case. For instance, to achieve 10 minutes of service time, the drone antenna array will require 32% less bandwidth than in the fixed-array scenario.

In Fig. 8, we show the impact of the number of users on the service time. Clearly, the service time increases as the number of users increases. For a higher number of users, the drones must deliver a higher data service which results in a higher transmission time. Moreover, in the proposed drone antenna array case, the control time also increases while increasing the number of users. Fig. 8 shows that our proposed drone antenna array system outperforms the fixed-array case for various number of users. For instance, using our approach, the average service time can be reduced by 8 minutes (or 27%) while serving 200 users. Meanwhile, the users can receive faster wireless services while exploiting the proposed drone antenna array system.

Fig. 9 shows how the control, transmission, and service times resulting from the proposed approach for different numbers of drones in the array. As the number of drones increases, the control time increases. In contrast, the transmission time (for 10 MHz bandwidth) decreases due to the increase of the array gain. Fig. 9 shows that, by increasing the number of drones from 10 to 30, the average control time increases by 20% while the average transmission time decreases by 36%. Therefore, there is a tradeoff between the transmission time and the control time as a function of the number of drones in the array.

![](images/c3f5ec715973ce6298bf7c8dcab45490dcf56ffd5d2237f5d6ebe2c79cd4e1bc.jpg)

<details>
<summary>bar</summary>

| Number of users | Proposed drone antenna array (min) | Fixed drone antenna array (min) |
| :--- | :--- | :--- |
| 60 | 7 | 8.5 |
| 80 | 9.5 | 12.3 |
| 100 | 11.8 | 14.5 |
| 120 | 13.7 | 16.9 |
| 140 | 16.3 | 20.5 |
| 160 | 19.2 | 24.0 |
| 180 | 20.8 | 25.5 |
| 200 | 23.6 | 30.3 |
</details>

Fig. 8. Service time vs. number of users for the drone antenna array and fixed-array (2MHz bandwidth).

![](images/d1d078b54857d7e003da7a84e5fef791fa758f32639a314e6fe27e1df0e3433d.jpg)

<details>
<summary>line</summary>

| Number of drones | Control time (s) | Transmission time (s) | Service time (s) |
| ---------------- | ---------------- | --------------------- | ---------------- |
| 6                | 95               | 240                   | 310              |
| 10               | 100              | 180                   | 270              |
| 14               | 105              | 150                   | 250              |
| 18               | 110              | 130                   | 240              |
| 22               | 115              | 125                   | 235              |
| 26               | 120              | 120                   | 230              |
| 30               | 125              | 110                   | 230              |
</details>

Fig. 9. Control, transmission, and service times vs. number of drones.

![](images/870a519aad5451b35e0623b99c5b27ce272626cedee8440185c8ea059aff2a49.jpg)

<details>
<summary>line</summary>

| Number of users | Total control time (min) for v_max = 300 rad/s | Total control time (min) for v_max = 500 rad/s |
| --------------- | ----------------------------------------------- | ----------------------------------------------- |
| 50              | 2.0                                             | 1.0                                             |
| 100             | 4.0                                             | 2.0                                             |
| 150             | 6.0                                             | 3.0                                             |
| 200             | 8.0                                             | 4.0                                             |
| 250             | 10.0                                            | 5.0                                             |
| 300             | 12.0                                            | 6.0                                             |
| 350             | 14.0                                            | 7.0                                             |
| 400             | 16.0                                            | 8.0                                             |
| 450             | 18.0                                            | 9.0                                             |
| 500             | 20.0                                            | 10.0                                            |
</details>

Fig. 10. Total control time vs. number of users.

In Fig. 10, we show how the number of users impacts the control time. As we can see from this figure, the control time increases while serving more users. This is due to the fact that, for a higher number of users, the drone-array must move more in order to steer its beam toward the users. The control time can be reduced by increasing the maximum speed of the rotors, which is in agreement with Theorem 3. For instance, increasing the maximum rotors’ speed from 300 rad/s to 500 rad/s yields around 35% control time reduction when serving 200 users.

![](images/2adbcb60b499a200968c535bbdfca371579bee70a104d05e9ac624ae48363fb5.jpg)  
Fig. 11. Speed of each rotor vs. wind force under the drone’s stability condition.

Fig. 11 represents the speeds of the rotors needed to ensure the drone’s stability in presence of wind, obtained using (80). Clearly, the drone is stable when its total force which is composed of the wind force, gravity, and the drone force is zero. For $\begin{array} { r c l } { F _ { \mathrm { w i n d } } } & { = } & { | F _ { \mathrm { w i n d } } | \bar { \vec { x } } } \end{array}$ , the rotor’s speed =must increase as the wind force increases. In the $F _ { \mathrm { w i n d } } ~ =$ $\begin{array} { r } { \left| F _ { \mathrm { w i n d } } \right| \left( \frac { 1 } { \sqrt { 3 } } \overrightarrow { x } + \frac { 1 } { \sqrt { 3 } } \overrightarrow { y } + \frac { 1 } { \sqrt { 3 } } \overrightarrow { z } \right) } \end{array}$ case, however, the rotor’s speed first decreases, and then increases. This is because, when $| F _ { \mathrm { w i n d } } | \leq 3 \mathrm { N } .$ , the wind force helps hovering the drone 3by compensating for the gravity. Hence, the drone’s force can be decreased by decreasing the speed of its rotors. For $\vert F _ { \mathrm { w i n d } } \vert ~ > ~ 3 \mathrm { N } .$ , the rotor’s speed start increasing such that 3the total force on the drone becomes zero. This result also implies that, in some cases (depending on the magnitude and direction of wind), wind can facilitate hovering of the drone by overcoming the gravity force. However, in case of strong winds, the drone’s stability may not be guaranteed by adjusting the speed of the rotors. This is because the drone force, which is limited by the maximum rotors’ speeds, cannot overcome the external forces.

# VI. CONCLUSION

In this paper, we have proposed a novel framework for employing a drone-enabled antenna array system that can provide wireless services to ground users within a minimum time. To this end, we have minimized the transmission time and the control time needed for changing the locations and orientations of the drones. First, we have optimized the positions of drones within the antenna array such that the transmission time for each user is minimized. Next, given the determined locations of drones, we have minimized the control time of the quadrotor drones by optimally adjusting the rotors’ speeds. Our results have shown that the proposed drone antenna array with the optimal configuration yields a significant improvement in terms of the service time, spectral and energy efficiency. Our results have revealed key design guidelines and fundamental tradeoffs for leveraging in an antenna array system. To our best knowledge, this is the first comprehensive study on the joint communications and control of drone antenna array systems.

# APPENDIX

# A. Proof of Theorem 1

First, we find $F ^ { 2 } ( \theta , \phi )$ by using (11):

$$
\begin{array}{l} F ^ {2} (\theta , \phi) \\ = \left[ 2 F ^ {0} (\theta , \phi) \right] ^ {2} \\ + \left[ 2 \sum_ {n = 1} ^ {N} a _ {n} k e _ {n} \sin \theta \cos \phi \sin \left(k d _ {n} ^ {0} \sin \theta \cos \phi + \beta_ {n}\right) \right] ^ {2} \\ - 8 F ^ {0} (\theta , \phi) \sum_ {n = 1} ^ {N} a _ {n} k e _ {n} \sin \theta \cos \phi \sin \left(k d _ {n} ^ {0} \sin \theta \cos \phi + \beta_ {n}\right). \\ \end{array}
$$

Subsequently, our objective function in (12) can be written as:

$$
\begin{array}{l} I _ {\text { int }} \left(F ^ {2} (\theta , \phi) w ^ {2} (\theta , \phi)\right) \\ = 4 \left[ e ^ {T} G e - 2 e ^ {T} q + I _ {\text { int }} \left(F _ {0} ^ {2} (\theta , \phi) w ^ {2} (\theta , \phi)\right) \right], \tag {54} \\ \end{array}
$$

where G and q are given in (17) and (18). Clearly, (54) is a quadratic function of e. Therefore, (54) is convex if and only if G is a positive semi-definite matrix. Given (17), we have:

$$
\boldsymbol {y} ^ {T} \boldsymbol {G} y = \sum_ {n = 1} ^ {N} y _ {n} \sum_ {m = 1} ^ {N} y _ {m} g _ {m, n}. \tag {55}
$$

Now, in (17), let us define

$$
z _ {n} = a _ {n} k \sin \theta \cos \phi w (\theta , \phi) \sin \left(k d _ {n} ^ {0} \sin \theta \cos \phi + \beta_ {n}\right), \tag {56}
$$

then, using (55), we have:

$$
\boldsymbol {y} ^ {T} \boldsymbol {G} \boldsymbol {y} = I _ {\text { int }} \left(\left[ \sum_ {n = 1} ^ {N} z _ {n} y _ {n} \right] ^ {2}\right). \tag {57}
$$

In (15), we can see that $I _ { \mathrm { i n t } } ( x ) ~ \geq ~ 0$ for $x ~ \geq ~ 0$ . Hence, ( )from (57), we can conclude that ${ \pmb y } ^ { T } { \pmb G } { \pmb y } \ \geq \ { \pmb 0 }$ 0. Therefore, 0G is positive semi-definite and the objective function in (12) is convex. Moreover, the constraints in (13) are affine functions which are convex. Hence, this optimization problem is convex. Now, we find the optimal perturbation vector e by using Karush-Kuhn-Tucker (KKT) conditions. The Lagrangian function will be:

$$
\begin{array}{l} \mathcal {L} = \boldsymbol {e} ^ {T} \boldsymbol {G} \boldsymbol {e} - 2 \boldsymbol {e} ^ {T} \boldsymbol {q} + I _ {\text { int }} \left(F _ {0} ^ {2} (\theta , \phi) w ^ {2} (\theta , \phi)\right) \\ + \sum_ {n = 1} ^ {N - 1} \mu_ {n} \left(e _ {n} - e _ {n + 1} + D _ {\min} + d _ {n} ^ {0} - d _ {n + 1} ^ {0}\right), \tag {58} \\ \end{array}
$$

where $\mu _ { n } \geq 0 , n = 1 , . . . , N - 1$ are the Lagrange multipliers.

0 = 1 1The necessary and sufficient (due to the convexity of the problem) KKT conditions for finding the optimal perturbation vector e are given by:

$$
\nabla_ {e} \left[ \mathcal {L} \right] = 0, \tag {59}
$$

which leads to $e = G ^ { - 1 } [ q + \mu _ { \mathscr { L } } ]$ , with $\mu _ { \mathcal { L } }$ being a $( N - 1 ) \times 1$ = [vector whose element n is $\mu _ { \mathcal { L } } ( n ) = \mu _ { n + 1 } - \mu _ { n }$ ( 1) 1. Based on the ( ) =complementary slackness conditions, we have:

$$
\left\{ \begin{array}{l} \mu_ {n} \left(e _ {n} - e _ {n + 1} + D _ {\min} + d _ {n} ^ {0} - d _ {n + 1} ^ {0}\right) = 0, \quad \forall n \in \mathcal {N} \backslash \{N \}, \\ \mu_ {n} \geq 0, \quad \forall n \in \mathcal {N} \backslash \{N \}. \end{array} \right. \tag {60}
$$

Finally, the optimal perturbation vector, $e ^ { * } .$ , can be determined by solving (59) and (60).

# B. Proof of Theorem 2

In Subsection III-A, we have derived the optimal distance of drones from the origin that leads to a maximum array directivity. First, we consider an initial (or arbitrary) orientation, as shown in Figure 2. Let $d _ { m } ^ { * }$ be the optimal distance of drone $\begin{array} { l } { m \ \leq \ M / 2 } \end{array}$ from the array’s center, $\alpha _ { O }$ and $\gamma _ { o }$ 2be the initial polar and azimuthal angles of the drone. Based on the considered drones’ locations, let $( \theta _ { \mathrm { m a x } } , \phi _ { \mathrm { m a x } } ) \ =$ argmax $\left\lceil F ( \theta , \phi ) w ( \theta , \phi ) \right\rceil$ be a direction at ( ) = ( ) ( )which the directivity of the array is maximized. Our goal is to achieve the maximum directivity at a given direction $( \theta _ { i } , \phi _ { i } )$ corresponding to user i. Therefore, we need to ( )change the locations of the drones such that $\theta _ { i } \ = \ \theta _ { \operatorname* { m a x } } ,$ and $\phi _ { i } ~ = ~ \phi _ { \mathrm { m a x } }$ =. To this end, we align the unit vector $( 1 , \theta _ { \mathrm { m a x } } , \phi _ { \mathrm { m a x } } )$ with $( 1 , \theta _ { i } , \phi _ { i } )$ in the spherical coordinate (1 ) (1 )and, then, we update the drones’ positions accordingly. In the Cartesian coordinate system, we need to rotate vector $\begin{array} { r l r } { q _ { \mathrm { m a x } } } & { { } \ = \ } & { \left( \sin \theta _ { \mathrm { m a x } } \cos \phi _ { \mathrm { m a x } } , \sin \theta _ { \mathrm { m a x } } \sin \phi _ { \mathrm { m a x } } , \cos \theta _ { \mathrm { m a x } } \right) ^ { T } } \end{array}$ T = sin cos sin sinsuch that it becomes aligned with $\begin{array} { r l r l } { q _ { i } } & { { } } & { = } \end{array}$ θi φi, $\theta _ { i }$ φi ,  θi 
  .

in cos sin sin cosThe rotation matrix for rotating a vector u about another vector $\mathbf { \boldsymbol { a } } = \left( a _ { x } , a _ { y } , a _ { z } \right) ^ { T }$ , with a ω rotation angle, is [35]:

$$
\boldsymbol {R} _ {\text { rot }} = \left(\boldsymbol {R} _ {\text { rot }, 1} \boldsymbol {R} _ {\text { rot }, 2} \boldsymbol {R} _ {\text { rot }, 3}\right), \tag {61}
$$

where Rrot,1 $\begin{array} { r l r } { R _ { \mathrm { r o t , 1 } } \quad } & { = } & { \left( \begin{array} { c } { a _ { x } ^ { 2 } ( 1 - \cos \omega ) + \cos \omega } \\ { a _ { x } a _ { y } ( 1 - \cos \omega ) + a _ { z } \sin \omega } \\ { a _ { x } a _ { z } ( 1 - \cos \omega ) - a _ { y } \sin \omega } \end{array} \right) , } \end{array}$

$$
\boldsymbol {R} _ {\text {rot,2}} = \left( \begin{array}{c} a _ {x} a _ {y} (1 - \cos \omega) - a _ {z} \sin \omega \\ a _ {y} ^ {2} (1 - \cos \omega) + \cos \omega \\ a _ {y} a _ {z} (1 - \cos \omega) + a _ {x} \sin \omega \end{array} \right), \text {and} \boldsymbol {R} _ {\text {rot,3}} =
$$

$$
\binom{a _ {x} a _ {z} (1 - \cos \omega) + a _ {y} \sin \omega}{a _ {y} a _ {z} (1 - \cos \omega) - a _ {x} \sin \omega}.
$$

In our problem, the rotation between $q _ { \mathrm { m a x } }$ and $\mathbf { \nabla } q _ { i }$ can be done about the normal vector of these vectors, with the rotation angle being the angle between $q _ { \mathrm { m a x } }$ and $\mathbf { \nabla } q _ { i }$ . Hence, based on the dot-product and cross-product of vectors, we use $a \ = \ q _ { i } \times q _ { \operatorname* { m a x } } .$ and $\omega = \cos ^ { - 1 } ( \pmb { q } _ { i } \cdot \pmb { q } _ { \operatorname* { m a x } } )$ to find the = = cos ( )rotation matrix in (61). Now, we update the locations of drones using the rotation matrix. Clearly, for $m \ \leq \ M / 2$ , 2the initial location of drone m in the Cartesian coordinate is $\left( d _ { m } ^ { * } \sin \alpha _ { o } \cos \gamma _ { o } , d _ { m } ^ { * } \right.$ sin $\alpha _ { o }$ sin $\beta _ { o } , d _ { m } ^ { * } \cos \alpha _ { o } ) ^ { ' }$ . As a result, sin cos sin sin costhe optimal locations of drones for serving user i is given by:

$$
\begin{array}{l} \left(x _ {m} ^ {*}, y _ {m} ^ {*}, z _ {m} ^ {*}\right) ^ {T} \\ = \boldsymbol {R} _ {\text { rot }} \left(d _ {m} ^ {*} \sin \alpha_ {o} \cos \gamma_ {o}, d _ {m} ^ {*} \sin \alpha_ {o} \sin \beta_ {o}, d _ {m} ^ {*} \cos \alpha_ {o}\right) ^ {T}, \\ \text { if } m \leq M / 2. \tag {62} \\ \end{array}
$$

Finally, due to the symmetric configuration of the antenna array about the origin, the optimal locations of drones m when $n > M / 2$ are as follows:

$$
\begin{array}{l} \left(x _ {m} ^ {*}, y _ {m} ^ {*}, z _ {m} ^ {*}\right) ^ {T} \\ = - \boldsymbol {R} _ {\text { rot }} \left(d _ {m} ^ {*} \sin \alpha_ {o} \cos \gamma_ {o}, d _ {m} ^ {*} \sin \alpha_ {o} \sin \beta_ {o}, d _ {m} ^ {*} \cos \alpha_ {o}\right) ^ {T}, \\ \text { if   } m \leq M / 2. \tag {63} \\ \end{array}
$$

This completes the proof.

# C. Proof of Lemma 2

To maximize the drone’s acceleration towards the given location D, we need to maximize the total force in the direction of $P _ { D }$ . Considering the center of the drone as the origin of the Cartesian and spherical coordinate systems, we can present the vectors of forces and the movement as in Fig. 4. In this figure, based on the Cartesian-to-spherical coordinates transformation, the polar and azimuthal angles in the spherical coordinate are given by $\theta _ { \mathrm { e x } } ~ = ~ \cos ^ { - 1 } \bigg ( { \frac { F _ { \mathrm { e x } , z } } { | F _ { \mathrm { e x } } | } } \bigg ) , ~ \phi _ { \mathrm { e x } } ~ =$ −1 $\begin{array} { r } { \tan ^ { - 1 } \Big ( \frac { F _ { \mathrm { e x } , y } } { F _ { \mathrm { e x } , x } } \Big ) , \phi _ { D } = \tan ^ { - 1 } \Big ( \frac { y _ { D } } { x _ { D } } \Big ) } \end{array}$ Fex,y , and $\begin{array} { r } { \theta _ { D } = \cos ^ { - 1 } \left( \frac { z _ { D } } { | P _ { D } | } \right) } \end{array}$ Fex,x tanLet α and $\beta ^ { ' } \mathrm { b e } ,$ = tan = cos respectively, the polar and azimuthal angles of the drone’s force. Here, we seek to determine α and $\beta$ such that the drone can move towards location D with a maximum acceleration (i.e., maximum total force). In this case, the total force $F _ { \mathrm { e x } } + F$ must be in the same direction as $P _ { D }$ . Let γ be +the angle between F and $P _ { D }$ , and q be the angle between $\pmb { F } _ { \mathrm { e x } }$ and $P _ { D }$ . To ensure that $F _ { \mathrm { e x } } + F$ is in the direction of $P _ { D } ,$ we should have:

$$
\left| \boldsymbol {F} _ {\mathrm{ex}} \right| \sin \gamma = \left| \boldsymbol {F} \right| \sin q = F \sin q. \tag {64}
$$

Also, using the inner product formula, γ is given by:

$$
\gamma = \cos^ {- 1} \left(\frac {\boldsymbol {F} _ {\mathrm{ex}} \cdot \boldsymbol {P} _ {D}}{| \boldsymbol {F} _ {\mathrm{ex}} | | \boldsymbol {P} _ {D} |}\right). \tag {65}
$$

As a result, q will be:

$$
q = \sin^ {- 1} \left(\frac {\left| \boldsymbol {F} _ {e x} \right|}{\left| \boldsymbol {F} \right|} \sin \left[ \cos^ {- 1} \left(\frac {\boldsymbol {F} _ {e x} . \boldsymbol {P} _ {D}}{\left| F _ {e x} \right| \left| P _ {D} \right|}\right) \right]\right). \tag {66}
$$

Now, based on the law of cosines, the total force magnitude is equal to:

$$
\begin{array}{l} A \triangleq | \boldsymbol {F} _ {\mathrm{ex}} + \boldsymbol {F} | \\ = \left[ F ^ {2} + \left| \boldsymbol {F} _ {\mathrm{ex}} \right| ^ {2} + 2 F \left| \boldsymbol {F} _ {\mathrm{ex}} \right| \cos \left(\gamma + \sin^ {- 1} \left(\frac {\left| \boldsymbol {F} _ {\mathrm{ex}} \right|}{F} \sin \gamma\right)\right) \right] ^ {1 / 2}. \tag {67} \\ \end{array}
$$

By projection $( F _ { \mathrm { e x } } + F ) , F _ { \mathrm { e x } }$ , and F on z-axis and x − y plane, we have:

$$
A \cos \theta_ {D} = | \boldsymbol {F} _ {\mathrm{ex}} | \cos \theta_ {\mathrm{ex}} + F \cos \alpha , \tag {68}
$$

$$
\left| \boldsymbol {F} _ {\mathrm{ex}} \right| \sin \theta_ {\mathrm{ex}} \sin \left(\phi_ {D} - \phi_ {\mathrm{ex}}\right) = F \sin \alpha \sin \left(\phi_ {D} - \beta\right). \tag {69}
$$

Subsequently, we obtain α and $\beta$ as follows:

$$
\alpha = \cos^ {- 1} \left[ \frac {A \cos \theta_ {D} - | \boldsymbol {F} _ {\mathrm{ex}} | \cos \theta_ {\mathrm{ex}}}{F} \right], \tag {70}
$$

$$
\beta = \phi_ {D} - \sin^ {- 1} \left[ \frac {\left| \boldsymbol {F} _ {\mathrm{ex}} \right| \sin \theta_ {\mathrm{ex}} \sin \left(\phi_ {D} - \phi_ {\mathrm{ex}}\right)}{F \sin \psi_ {p} ^ {D}} \right]. \tag {71}
$$

Finally, considering the fact that the drone’s force is perpendicular to its rotors’ plane, as well as using the transformation between body-frame and earth-frame, the drone’s orientation can be given by6:

$$
\psi_ {\mathrm{p}} ^ {D} = \alpha , \quad \psi_ {\mathrm{r}} ^ {D} = \tan^ {- 1} \left(\tan \beta \times \sin \psi_ {p} ^ {D}\right), \quad \psi_ {\mathrm{y}} ^ {D} = 0, \tag {72}
$$

which proves Lemma 2.

# D. Proof of Theorem 3

Let s t be the distance that the drone moves towards ( )destination D at time t. We define state $\mathbf { \boldsymbol { g } } ( t ) = \left[ \mathbf { \boldsymbol { s } } ( t ) , \dot { \boldsymbol { s } } ( t ) \right] ^ { T }$ , and provide the following equation:

$$
\dot {\boldsymbol {g}} (t) = \left[ \begin{array}{l l} 0 & 1 \\ 0 & 0 \end{array} \right] \boldsymbol {g} (t) + \left[ \begin{array}{l} 0 \\ 1 \end{array} \right] a _ {D} (t), \tag {73}
$$

where $a _ { \mathrm { m i n } } ~ \le ~ a _ { D } ( t ) ~ \le ~ a _ { \mathrm { m a x } }$ is the drone’s acceleration towards $D ,$ with $a _ { \mathrm { m i n } }$ and $a _ { \mathrm { m a x } }$ being the minimum and maximum values of $a _ { D } ( t )$ . Clearly, the drone can reach the ( )destination and stop at D within duration T , if $g ( T ) \ =$ $[ 0 , 0 ] ^ { T }$ . Based on Lemma 1, T is minimized when $a _ { D } ( t ) =$ amax, 0 < t ≤ τ, . Now, we find τ by using kinematic ${ \Big \backslash } a _ { \operatorname* { m i n } } , \quad \tau < t \leq T .$ equations that describe an object’s motion. Let $d _ { D }$ be the distance between the initial and the final locations of the drone. Clearly, the drone’s displacement until $t = \tau$ is equal to $\scriptstyle { \frac { 1 } { 2 } } a _ { \mathrm { m a x } } \tau ^ { 2 }$ . During $\tau \ < \ t \ \leq \ T$ =, the displacement will be $\begin{array} { r } { \frac { 1 } { 2 } a _ { \mathrm { m i n } } ( T - \tau ) ^ { 2 } + a _ { \mathrm { m a x } } \tau ( T - \tau ) } \end{array}$ . Hence, the total drone’s ( ) +disparagement is:

$$
d _ {D} = \frac {1}{2} a _ {\max} \tau^ {2} + \frac {1}{2} a _ {\min} (T - \tau) ^ {2} + a _ {\max} \tau (T - \tau). \tag {74}
$$

Also, considering the fact that drone stops (i.e. zero speed) at $t = T$ , we have:

$$
a _ {\max} \tau + a _ {\min} (T - \tau) = 0, \tag {75}
$$

According to (74) and (75), the total control time, T , and the switching time can be found by:

$$
T = \sqrt {2 d _ {D} (\frac {1}{a _ {\max}} - \frac {1}{a _ {\min}})}, \tag {76}
$$

$$
\tau = \frac {a _ {\min}}{a _ {\min} - a _ {\max}} T. \tag {77}
$$

As we can see from (76), T can be minimized by maximizing $a _ { \mathrm { m a x } }$ and minimizing $a _ { \mathrm { m i n } }$ . To this end, we will adjust the drone’s orientation as well as the rotors’ speeds. Each drone’s orientation can be determined by using Lemma 2. Also, given $( 2 5 ) ‐ ( 2 8 )$ , we can show that the optimal speeds of the rotors are v1 v2 v3 v4 vmax. $v _ { 1 } = v _ { 2 } = v _ { 3 } = v _ { 4 } = v _ { \mathrm { m a x } } .$

= = = =To adjust the drone’s orientation within a minimum time, we minimize the time needed for the pitch and roll updates. Using a similar approach as in (73), and considering (25), (29), (30), and zero yaw angle $( \mathrm { i . e . ~ } v _ { 2 } ^ { 2 } + v _ { 4 } ^ { 2 } = v _ { 1 } ^ { 2 } + v _ { 3 } ^ { 2 } ~ )$ , the optimal

6We consider $( 0 , 0 , 0 )$ as the initial orientation. To change the orientation, we first update the pitch and, then, update the roll.

rotors’ speeds can be given by:

positive change of pitch angle:

$$
\left\{ \begin{array}{l l} v _ {2} = 0, v _ {1} = v _ {3} = \frac {1}{\sqrt {2}} v _ {\max}, v _ {4} = v _ {\max}, & \text { if } 0 <   t \leq \tau_ {1}, \\ v _ {4} = 0, v _ {1} = v _ {3} = \frac {1}{\sqrt {2}} v _ {\max}, v _ {2} = v _ {\max}, & \text { if } \tau_ {1} <   t \leq \tau_ {2}, \end{array} \right. \tag {78}
$$

positive change of roll angle:

$$
\left\{ \begin{array}{l l} v _ {1} = 0, v _ {2} = v _ {4} = \frac {1}{\sqrt {2}} v _ {\max}, v _ {3} = v _ {\max}, & \text { if } \tau_ {2} <   t \leq \tau_ {3}, \\ v _ {3} = 0, v _ {2} = v _ {4} = \frac {1}{\sqrt {2}} v _ {\max}, v _ {1} = v _ {\max}, & \text { if } \tau_ {3} <   t \leq \tau_ {4}, \end{array} \right. \tag {79}
$$

Therefore, in the first Stage, the drone changes its orientation such that it can move towards D in presence of external forces (e.g., gravity and wind). In the second Stage, the drone moves with a maximum acceleration. In Stage 3, the drone’s orientation changes to minimize the acceleration towards D. In Stage 4, the drone moves with a minimum acceleration. In Stages 5 and 6, the drone’s orientation and the rotors’ speeds are adjusted to ensure the stability of drone at D. Clearly, the drone will be stable when its total force, A given in (67), is zero. Hence, we must have $F = | F _ { \mathrm { e x t } } |$ . Using (25) with $T _ { \mathrm { t o t } } = | F _ { \mathrm { e x t } } |$ =, the rotors’ speeds in the stable stage is:

$$
v _ {\mathrm{F}} = \sqrt {\frac {| \boldsymbol {F} _ {\text { ext }} |}{4 \rho_ {1}}}. \tag {80}
$$

The rotors’ speed in Stages 1-6 are given in (44)-(49).

In order to find the switching times, we use the dynamic equations of the drone given in (25)–(29). For instance, in Stage 1, the time needed for a $\Delta \psi _ { \mathfrak { p } , 1 }$ pitch angle change Δcan be obtained using (25) and (29). In this case, given the rotors’ speed in (44), and the dynamic equations of the drone, we can find $\tau _ { 1 }$ and $\tau _ { 2 }$ as:

$$
\tau_ {1} = \frac {1}{v _ {\max}} \sqrt {\frac {\Delta \psi_ {\mathrm{p} , 1} I _ {y}}{l \rho_ {1}}}, \quad \tau_ {2} = 2 \tau_ {1}, \tag {81}
$$

where $\Delta \psi _ { \mathfrak { p } , 1 }$ is the change of pitch angle at Stage 1. Likewise, $\tau _ { 3 }$ and $\tau _ { 4 }$ can also be determined.

In Stage 2, the time needed for moving within a $d _ { \mathrm { s } 2 }$ distance is given by:

$$
t _ {s 2} = \sqrt {\frac {2 d _ {s 2} A _ {s 2}}{m _ {D}}}, \tag {82}
$$

where $A _ { s 2 }$ is the total force towards the drone’s destination at Stage 2 which can be determined using (67). Subsequently, we can find the switching time by $\tau _ { 5 } = \tau _ { 4 } + t _ { s 2 }$ .

= +The switching times in Stages 3-5 can be determined by adopting the similar approach used in Stages 1 and 2. Note that, $\tau _ { 1 4 }$ represents the total control time the drone, which can be determined based on (76) and (81) as follows:

$$
T _ {I, D} = \tau_ {1 4} = \sqrt {2 d _ {D} \left(\frac {m _ {D}}{A _ {s 2}} - \frac {m _ {D}}{A _ {s 4}}\right)} + T ^ {O}, \tag {83}
$$

where $A _ { s 4 }$ is the total force on the drone as Stage 4. $T ^ { O }$ is the total control time needed for the orientation changes in Stages 1,3, and 5, given by:

$$
\begin{array}{l} T ^ {O} = \frac {2}{v _ {\mathrm{max}}} \Big [ \sqrt {\frac {\Delta \psi_ {\mathrm{p,1}} I _ {y}}{l \rho_ {1}}} + \sqrt {\frac {\Delta \psi_ {\mathrm{r,1}} I _ {x}}{l \rho_ {1}}} + \sqrt {\frac {\Delta \psi_ {\mathrm{p,3}} I _ {y}}{l \rho_ {1}}} \Big ] \\ \left. + \sqrt {\frac {\Delta \psi_ {\mathrm{r} , 3} I _ {x}}{l \rho_ {1}}} + \sqrt {\frac {\Delta \psi_ {\mathrm{p} , 5} I _ {y}}{l \rho_ {1}}} + \sqrt {\frac {\Delta \psi_ {\mathrm{r} , 5} I _ {x}}{l \rho_ {1}}} \right], \tag {84} \\ \end{array}
$$

where $\Delta \psi _ { \mathrm { p } , i } , \Delta \psi _ { \mathrm { r } , i }$ are the pitch and roll changes in Stage i. This completes the proof.

# REFERENCES

[1] M. Mozaffari, W. Saad, M. Bennis, and M. Debbah, “Drone-based antenna array for service time minimization in wireless networks,” in Proc. IEEE Int. Conf. Commun. (ICC), Kansas City, MO, USA, May 2018, pp. 1–6.   
[2] Q. Wu, Y. Zeng, and R. Zhang, “Joint trajectory and communication design for multi-UAV enabled wireless networks,” IEEE Trans. Wireless Commun., vol. 17, no. 3, pp. 2109–2121, Mar. 2018.   
[3] M. Alzenad, A. El-Keyi, and H. Yanikomeroglu, “3-D placement of an unmanned aerial vehicle base station for maximum coverage of users with different QoS requirements,” IEEE Wireless Commun. Lett., vol. 7, no. 1, pp. 38–41, Feb. 2018.   
[4] M. Mozaffari, W. Saad, M. Bennis, and M. Debbah, “Unmanned aerial vehicle with underlaid device-to-device communications: Performance and tradeoffs,” IEEE Trans. Wireless Commun., vol. 15, no. 6, pp. 3949–3963, Jun. 2016.   
[5] Y. Zeng and R. Zhang, “Energy-efficient UAV communication with trajectory optimization,” IEEE Trans. Wireless Commun., vol. 16, no. 6, pp. 3747–3760, Jun. 2017.   
[6] Q. Wu, J. Xu, and R. Zhang. (2018). “Capacity characterization of UAV-enabled two-user broadcast channel.” [Online]. Available: https://arxiv.org/abs/1801.00443   
[7] S. Jeong, O. Simeone, and J. Kang, “Mobile edge computing via a UAVmounted cloudlet: Optimization of bit allocation and path planning,” IEEE Trans. Veh. Technol., vol. 67, no. 3, pp. 2049–2063, Mar. 2018.   
[8] M. Mozaffari, W. Saad, M. Bennis, and M. Debbah, “Efficient deployment of multiple unmanned aerial vehicles for optimal wireless coverage,” IEEE Commun. Lett., vol. 20, no. 8, pp. 1647–1650, Aug. 2016.   
[9] V. Sharma, R. Sabatini, and S. Ramasamy, “UAVs assisted delay optimization in heterogeneous wireless networks,” IEEE Commun. Lett., vol. 20, no. 12, pp. 2526–2529, Dec. 2016.   
[10] P. G. Sudheesh, M. Mozaffari, M. Magarini, W. Saad, and P. Muthuchidambaranathan, “Sum-rate analysis for high altitude platform (HAP) drones with tethered balloon relay,” IEEE Commun. Lett., vol. 22, no. 6, pp. 1240–1243, Jun. 2018.   
[11] I. Bor-Yaliniz and H. Yanikomeroglu, “The new frontier in RAN heterogeneity: Multi-tier drone-cells,” IEEE Commun. Mag., vol. 54, no. 11, pp. 48–55, Nov. 2016.   
[12] M. Mozaffari, A. T. Z. Kasgari, W. Saad, M. Bennis, and M. Debbah. (2018). “Beyond 5G with UAVs: Foundations of a 3D wireless cellular network.” [Online]. Available: https://arxiv.org/abs/1805.06532   
[13] M. M. Azari, F. Rosas, K.-C. Chen, and S. Pollin, “Joint sum-rate and power gain analysis of an aerial base station,” in Proc. IEEE Global Commun. Conf. (GLOBECOM), Washington, DC, USA, Dec. 2016, pp. 1–6.   
[14] J. Lyu, Y. Zeng, R. Zhang, and T. J. Lim, “Placement optimization of UAV-mounted mobile base stations,” IEEE Commun. Lett., vol. 21, no. 3, pp. 604–607, Mar. 2017.   
[15] M. Mozaffari, W. Saad, M. Bennis, and M. Debbah, “Wireless communication using unmanned aerial vehicles (UAVs): Optimal transport theory for hover time optimization,” IEEE Trans. Wireless Commun., vol. 16, no. 12, pp. 8052–8066, Dec. 2017.   
[16] Y. Zeng, X. Xu, and R. Zhang, “Trajectory design for completion time minimization in UAV-enabled multicasting,” IEEE Trans. Wireless Commun., vol. 17, no. 4, pp. 2233–2246, Apr. 2018.   
[17] J. Garza, M. A. Panduro, A. Reyna, G. Romero, and C. del Rio, “Design of UAVs-based 3D antenna arrays for a maximum performance in terms of directivity and SLL,” Int. J. Antennas Propag., vol. 2016, Aug. 2016, Art. no. 2621862.   
[18] W. Su, J. D. Matyjas, M. J. Gans, and S. Batalama, “Maximum achievable capacity in airborne MIMO communications with arbitrary alignments of linear transceiver antenna arrays,” IEEE Trans. Wireless Commun., vol. 12, no. 11, pp. 5584–5593, Nov. 2013.

[19] M. N. Soorki, M. Mozaffari, W. Saad, M. H. Manshaei, and H. Saidi, “Resource allocation for machine-to-machine communications with unmanned aerial vehicles,” in Proc. IEEE Globecom Workshops (GC Wkshps), Washington, DC, USA, Dec. 2016, pp. 1–6.   
[20] J. E. Bobrow, S. Dubowsky, and J. S. Gibson, “Time-optimal control of robotic manipulators along specified paths,” Int. J. Robot. Res., vol. 4, no. 3, pp. 3–17, Sep. 1985.   
[21] W. S. Newman, “Robust near time-optimal control,” IEEE Trans. Autom. Control, vol. 35, no. 7, pp. 841–844, Jul. 1990.   
[22] T.-S. Chung and C.-J. Wu, “A computationally efficient numerical algorithm for the minimum-time control problem of continuous systems,” Automatica, vol. 28, no. 4, pp. 841–847, Jul. 1992.   
[23] L.-C. Lai, C.-C. Yang, and C.-J. Wu, “Time-optimal control of a hovering quad-rotor helicopter,” J. Intell. Robot. Syst., vol. 45, no. 2, pp. 115–135, Feb. 2006.   
[24] J. F. Bonnans and A. Shapiro, “Optimization problems with perturbations: A guided tour,” SIAM Rev., vol. 40, no. 2, pp. 228–264, Jun. 1998.   
[25] (1983). An Introduction to Mathematical Optimal Control Theory Version 0.2. [Online]. Available: http://math.berkeley.edu/ evans/control.course.pdf   
[26] D. K. Cheng, “Optimization techniques for antenna arrays,” Proc. IEEE, vol. 59, no. 12, pp. 1664–1674, Dec. 1971.   
[27] H. He, S. Zhang, Y. Zeng, and R. Zhang, “Joint altitude and beamwidth optimization for UAV-enabled multiuser communications,” IEEE Commun. Lett., vol. 22, no. 2, pp. 344–347, Feb. 2018.   
[28] K. Venugopal, M. C. Valenti, and R. W. Heath, Jr., “Device-todevice millimeter wave communications: Interference, coverage, rate, and finite topologies,” IEEE Trans. Wireless Commun., vol. 15, no. 9, pp. 6175–6188, Sep. 2016.   
[29] W. L. Stutzman and G. A. Thiele, Antenna Theory and Design. Hoboken, NJ, USA: Wiley, 2012.   
[30] Y. Zeng, R. Zhang, and T. J. Lim, “Wireless communications with unmanned aerial vehicles: Opportunities and challenges,” IEEE Commun. Mag., vol. 54, no. 5, pp. 36–42, May 2016.   
[31] S. Vaidyanathan and C.-H. Lien, Applications of Sliding Mode Control in Science and Engineering, vol. 709. Cham, Switzerland: Springer, 2017.   
[32] J. E. Hurtado, Kinematic and Kinetic Principles. Morrisville, NC, USA: Lulu, 2012.   
[33] E. L. Lawler and D. E. Wood, “Branch-and-bound methods: A survey,” Oper. Res., vol. 14, no. 4, pp. 699–719, Jul./Aug. 1966.   
[34] Y. Mutoh and S. Kuribara, “Control of quadrotor unmanned aerial vehicles using exact linearization technique with the static state feedback,” J. Automat. Control Eng., vol. 4, no. 5, pp. 340–346, Oct. 2016.   
[35] T. Bajd, M. Mihelj, and M. Munih, “Rotation and orientation,” in Introduction to Robotics. Dordrecht, The Netherlands: Springer, 2013, pp. 9–36.

![](images/bfc789c32c25ad6dabf97cd0248102e0b40df2f79b6d1d92668998f65172fa79.jpg)

<details>
<summary>natural_image</summary>

Portrait of a man with short dark hair and beard wearing a blue checkered shirt (no text or symbols visible)
</details>

Mohammad Mozaffari (S’15) received the B.Sc. degree in electrical engineering from the Sharif University of Technology, Iran, the M.Sc. degree in geomatics engineering from the University of Calgary, Canada, and the Ph.D. degree in electrical and computer engineering from Virginia Tech in 2018. He is currently an Experienced Researcher with Ericsson, Santa Clara, USA. His research interests span diverse areas, such as 5G wireless networks, unmanned aerial vehicle communications, Internet of Things, and machine learning. He has actively

served as a reviewer for flagship IEEE TRANSACTIONS and Conferences, and participated as the technical program committee member for a variety of workshops, such as ICC 18—UAVs in 5G, GLOBECOM 17—Wi-UAV, and GLOBECOM 16—Internet of Everything. He received the Exemplary Reviewer Award for the IEEE TRANSACTIONS ON COMMUNICATIONS in 2018.

![](images/f55bdf192ec0aa21eba6a285c181d4db983130df32be1f95fceb349e1e080b76.jpg)

<details>
<summary>natural_image</summary>

Portrait of a man in business attire (no text or symbols visible)
</details>

Walid Saad (S’07–M’10–SM’15) received the Ph.D. degree from the University of Oslo in 2010. He is currently an Associate Professor with the Department of Electrical and Computer Engineering, Virginia Tech, where he leads the Network Science, Wireless, and Security Laboratory, within the Wireless@VT Research Group. His research interests include wireless networks, machine learning, game theory, cybersecurity, unmanned aerial vehicles, and cyber-physical systems. He was a recipient of the NSF CAREER Award in 2013, the AFOSR Summer

Faculty Fellowship in 2014, and the Young Investigator Award from the Office of Naval Research in 2015. He was the author/co-author of six conference best paper awards at WiOpt in 2009, ICIMP in 2010, the IEEE WCNC in 2012, the IEEE PIMRC in 2015, the IEEE SmartGridComm in 2015, and EuCNC in 2017. He was a recipient of the 2015 Fred W. Ellersick Prize from the IEEE Communications Society, the 2017 IEEE ComSoc Best Young Professional in Academia Award, and the 2018 IEEE ComSoc Radio Communications Committee Early Achievement Award. He was named the Stephen O. Lane Junior Faculty Fellow at Virginia Tech from 2015 to 2017. He was named the College of Engineering Faculty Fellow in 2017. He currently serves as an Editor for the IEEE TRANSACTIONS ON WIRELESS COM-MUNICATIONS, the IEEE TRANSACTIONS ON COMMUNICATIONS, the IEEE TRANSACTIONS ON MOBILE COMPUTING, and the IEEE TRANSACTIONS ON INFORMATION FORENSICS AND SECURITY.

![](images/193f17b34eeb00172d87d52a201c0e521970f9e0df895bc110357476ebc115c4.jpg)

<details>
<summary>natural_image</summary>

Portrait of a man with curly hair and beard (no text or symbols visible)
</details>

Mehdi Bennis (S’07–AM’08–SM’15) received the M.Sc. degree in electrical engineering jointly from EPFL, Switzerland, and the Eurecom Institute, France, in 2002, and the Ph.D. degree on spectrum sharing for future mobile cellular systems in 2009. From 2002 to 2004, he was a Research Engineer with IMRA-EUROPE, where he was involved in investigating adaptive equalization algorithms for mobile digital TV. In 2004, he joined the Centre for Wireless Communications, University of Oulu, Finland, as a Research Scientist. In 2008, he was a

Visiting Researcher with the Alcatel-Lucent Chair on Flexible Radio, Supelec. He is currently an Adjunct Professor with the University of Oulu and Academy of Finland Research Fellow. His main research interests are in radio resource management, heterogeneous networks, game theory, and machine learning in 5G networks and beyond. He has co-authored one book and published over 100 research papers in international conferences, journals, and book chapters. He was a recipient of the prestigious 2015 Fred W. Ellersick Prize from the IEEE Communications Society, the 2016 Best Tutorial Prize from the IEEE Communications Society and the 2017 EURASIP Best paper Award for the Journal of Wireless Communications and Networks. He serves as an Editor for the IEEE TRANSACTIONS ON WIRELESS COMMUNICATION.

![](images/f8ff5f1c45b317fe9d2434cccd860ddaa6ad9675997d8a9bcf8ac9f364f915f5.jpg)

<details>
<summary>natural_image</summary>

Portrait of a bald man in business attire with a smile (no text or symbols visible)
</details>

Mérouane Debbah (S’01–AM’03–M’04–SM’08– F’15) received the M.Sc. and Ph.D. degrees from the Ecole Normale Supérieure Paris-Saclay, France, in 1996. He was with Motorola Labs, Saclay, France, from 1999 to 2002 and the Vienna Research Center for Telecommunications, Vienna, Austria, until 2003. From 2003 to 2007, he was an Assistant Professor with the Mobile Communications Department, Institut Eurecom, Sophia Antipolis, France. Since 2007, he has been a Full Professor with CentraleSupelec, Gif-sur-Yvette, France. From 2007 to

2014, he was the Director of the Alcatel-Lucent Chair on Flexible Radio. Since 2014, he has been the Vice-President of the Huawei France R&D Center and the Director of the Mathematical and Algorithmic Sciences Laboratory. He has managed eight EU projects and over 24 national and international projects. His research interests lie in fundamental mathematics, algorithms, statistics, and information and communication sciences research. He is a fellow of WWRF and a member of the Academic Senate of Paris-Saclay. He was a recipient of the ERC grant MORE (Advanced Mathematical Tools for Complex Network Engineering). He received 17 best paper awards, among which the 2007 IEEE GLOBECOM Best Paper Award, the Wi-Opt 2009 Best Paper Award, the 2010 Newcom++ Best Paper Award, the WUN CogCom Best Paper Award in 2012 and 2013, respectively, the 2014 WCNC Best Paper Award, the 2015 ICC Best Paper Award, the 2015 IEEE Communications Society Leonard G. Abraham Prize, the 2015 IEEE Communications Society Fred W. Ellersick Prize, the 2016 IEEE Communications Society Best Tutorial Paper Award, the 2016 European Wireless Best Paper Award, the 2017 Eurasip Best Paper Award, and the Valuetools 2007, Valuetools 2008, CrownCom2009, Valuetools 2012, and SAM 2014 Best Student Paper Awards. He was a recipient of the Mario Boella Award in 2005, the IEEE Glavieux Prize Award in 2011, and the Qualcomm Innovation Prize Award in 2012. He was an Associate and a Senior Area Editor of the IEEE TRANSACTIONS ON SIGNAL PROCESSING from 2011 to 2013 and from 2013 to 2014, respectively. He is an Associate Editor-in-Chief of the journal Random Matrix: Theory and Applications.