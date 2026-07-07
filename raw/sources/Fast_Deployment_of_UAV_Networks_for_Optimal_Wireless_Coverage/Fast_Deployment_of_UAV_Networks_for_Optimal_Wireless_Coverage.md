# Fast Deployment of UAV Networks for Optimal Wireless Coverage

Xiao Zhang , Member, IEEE and Lingjie Duan , Senior Member, IEEE

Abstract—Unmanned Aerial Vehicle (UAV) networks have emerged as a promising technique to rapidly provide wireless coverage to a geographical area, where a flying UAV can be fast deployed to serve as cell site. Existing work on UAV-enabled wireless networks overlook the fast UAV deployment for wireless coverage, and such deployment problems have only been studied recently in sensor networks. Unlike sensors, UAVs should be deployed to the air and they are generally different in flying speed, operating altitude and wireless coverage radius. By considering such UAV heterogeneity to cover the whole target area, this paper studies two fast UAV deployment problems: one is to minimize the maximum deployment delay among all UAVs (min-max) for fairness consideration, and the other is to minimize the total deployment delay (min-sum) for efficiency consideration. We prove both min-max and min-sum problems are NP-complete in general. When dispatching UAVs from the same location, we present an optimal algorithm of low computational complexity Oðn Þ for the min-max problem. When UAVs are dispatched from different locations, we propose to preserve their location order during deployment and successfully design a fully polynomial time approximation scheme (FPTAS) of computation complexity O n to arbitrarily approach the global optimum with relative error -. The min-sum problem is more challenging. When UAVs are dispatched from the same initial location, we present an approximation algorithm of linear time. As for the general case, we further reformulate it as a dynamic program and propose a pseudo polynomial-time algorithm to solve it optimally.

Index Terms—Unmanned aerial vehicle networks, wireless coverage, fast deployment, approximation algorithm

## 1 INTRODUCTION

works for rapidly providing wireless coverage [1]. This flying cell site technology enabled by UAV rapidly expands the wireless coverage of the static territorial base stations on the ground, where UAVs serve as flying base stations to serve a geographical area (e.g., a disaster zone) out of the reach of the cellular networks. For example, Verizon has developed airborne LTE service allowing communications between a UAV and hurricane disaster victims [2]. Moreover, Project Loon [3] uses balloons as flying base stations to provide high speed internet coverage to people in rural and remote areas worldwide. In addition, traditional base stations or access points [4] are deployed at fixed locations for a long term by meeting the average traffic load, while flying UAVs are mobile and do not have such constraint to meet varying traffic load [5]. Thanks to such advantage, wireless carriers such as AT&T have started to use UAVs to opportunistically boost wireless coverage for crowds in big concerts or sports, where people continuously post their selfies and videos online [6].

There is increasingly more research work to deploy UAVs for providing wireless coverage (e.g., [1], [7], [8], [9]). For example, [7] and [8] consider the scenario that the wireless communication channels between UAVs and ground users are dominated by both line-of-sight (LoS) and Non-lineof-sight (NLOS) links. They investigate the optimal operating altitude for a single UAV, where a larger UAV height increases the line-of-sight opportunity of air-to-ground transmission but incurs a larger path loss. In a UAV-enabled wireless network, [9] adopts the LoS dominated communication and studies the tradeoff between a UAVs energy consumption and communication throughput by optimizing the UAVs moving trajectory. However, the existing work on UAV networks overlook the fast UAV deployment problems to rapidly provide the wireless coverage. Only some recent work about sensor networks study the deployment problems (e.g., [10]). Such results cannot apply to our fast UAV deployment problems. Unlike sensors or traditionally vehicular networks [11], [12], UAVs should be deployed to the air and the optimal deployment should take into account their heterogeneity in flying speed, operating altitude and wireless coverage radius.

Given the aforementioned limitations, we advance the research on fast deployment of heterogeneous UAVs. In practice, UAVs have limited coverage radii and can only serve users closely. Before servicing its associated users, each UAV takes the travel time or deployment delay to reach its final position and the delay depends on the travel distance to its final operational position, flying speed and operating altitude. As reported in [13], different types of UAV have different mission altitudes, radii, flying speeds and endurance. For example, Micro UAV’s altitude is generally smaller than 400 feet, flying speed is from 10 to 25 miles/hour, radius is from 1 to 5 miles and endurance is about 1 hour. By considering such UAV heterogeneity and focusing on the LoS dominated communication scenario to cover the whole target area, we comprehensively study two fast deployment problems: one is to minimize the maximum deployment delay among all UAVs for fairness consideration and the other is to minimize the total deployment delay for efficiency consideration. The min-max optimization problem arises naturally in situations of disasters or battle fields when we fairly care about the service delivery delay to any potential wireless user in the target region. A disaster victim or soldier may appear in any location of the target region and the min-max problem targets at minimizing the worse-case delay performance of any user. We want to avoid the unfair deployment outcome that some users are served shortly while some others start services after a long time.

Different from the min-max optimization problem, the min-sum problem targets at minimizing the sum of all UAVs’ travel time, or equivalently, the average travel time to attain a full coverage of the target region. This efficiency problem arises naturally in a situation when we aim to service many users in a big concert or sport and care the average waiting time performance of the crowd rather than the performance difference between individuals. Minimizing the total delay helps to improve the average service quality. Both the min-max and min-sum problems are important for different scenarios and they are conflicting in nature. On one hand, minimizing the maximum deployment delay may imply a significant increase in the total deployment delay. On the other hand, minimizing the total deployment delay may imply a significant increase in maximum deployment delay, since it does not consider reducing deployment delays of all UAVs in a fair manner. Designing different algorithms for both problems is wellmotivated.

Our key novelty and main contributions are summarized as follows.

Novel UAV fast deployment for Wireless Coverage (Section 3): To our best knowledge, this is the first paper to study heterogenous UAV deployment for providing emergent wireless coverage to a target geographical area. We prove that the both problems with objectives of min-max and min-sum deployment delay are NP-complete in general.

Minimizing maximum UAV deployment delay (Section 4): When a number n of diverse UAVs are dispatched from the same initial location (e.g., the closest UAV station) to the target area, we present an optimal deployment algorithm of low computational complexity $O ( n ^ { 2 } )$ by balancing UAVs’ diverse flying speeds and coverage radii.

When UAVs are generally dispatched from different locations, we propose to preserve their location order during deployment and successfully design a fully polynomial time approximation scheme (FPTAS) of computation complexity $O ( n ^ { 2 } \log { \frac { 1 } { \epsilon } } )$ to arbitrarily approach the global opti-<sup>log</sup>mum with relative error -.

\- Minimizing total UAV deployment delay (Section 5):

When UAVs are dispatched from the same initial location, we present a linear time approximation algorithm with provable performance bound.

When dispatching UAVs from different locations, we further reformulate the min-sum problem as a dynamic program and propose a pseudo polynomial-time algorithm to solve it optimally.

## 2 RELATED WORK

The use of UAVs as flying base stations is attracting growing interests from researchers [14], [15], [16]. The literature on UAV-enabled communications focus on developing the air-to-ground transmission model and explore the line of sight opportunity [7], [8]. Further, Azari et al. [17] consider the co-channel interference effect and study the UAV coverage maximization problem.

With respect to the UAV network deployment, most of existing works investigate the deployment or movement schemes of UAVs for reducing transmit power consumption [18], [20] or the propulsion energy consumption [9], [21]. Specifically, in [18], Li et al. present a UAV energy-efficient relaying system to guarantee the success rate such that the lifetime is maximized. In this system, the transmission schedule of the UAVs is optimized to reduce the maximum energy consumption of the UAVs, thereby extending its lifetime. In [20], Wu et al. use UAVs as flying base stations to serve a group of users fairly for transmission throughput. They optimize the multiuser communication scheduling jointly with the UAVs trajectory and power control. In [9], Zeng and Zhang present a UAV propulsion energy consumption model and optimize the UAVs’ coverage radii and flying speeds to maximize the energy efficiency for communication. By deriving an energy consumption model from real measurements [21], Carmelo and Giorgio optimize the UAV path to minimize the energy consumption such that all points of a specific area is covered. In [22], Orfanus et al. use multiple UAVs as relay nodes in the self-organizing paradigm to support military operations. [23] uses the UAV as base station to provide wireless serivce to low-mobility ground users with QoS requirements, in which they aim to maximize the number of covered users. [24] derives the wireless coverage probability for UAVs as a function of the operating altitude and the antenna gain. Then, it presents a deployment scheme to maximize the coverage performance with minimum transmit power. Few of the existing work study the fast UAV deployment for providing wireless coverage.

Related to the fast UAV deployment, there are only a few recent theoretical works on sensor networks (e.g., [10], [25]). These work focus on minimizing the sensors’ maximum or total moving/deployment distance in the one-dimensional ground. Wang and Zhang [10] assume an identical sensing range for all sensors and present the first exact algorithm to compute the maximum weighted movement of sensors, which has the computation complexity Oðn n nÞ. <sup>log log log</sup>To deal with the more general case of diverse sensing ranges and even weights for sensors, Benkoczi et al. [25] strongly assume all sensors are on one end of the target interval and thus present an approximation algorithm to minimize the total weighted movement. However, the above algorithm design methods about sensor networks cannot apply to our fast UAV deployment problems, where UAVs should be deployed to the air and the optimal deployment should take into account their heterogeneity in flying speed, operating altitude and wireless coverage radius. Regarding to the short delay wireless service by UAVs, Mohammad et al. [26] consider a system of UAV with underlaid Device-to-Device communications and study the tradeoff between the coverage and delay. None of the existing work study the fast UAV deployment for providing full wireless coverage over a target area.

![](images/c2b7d8356a3cc4f2b299f5a29751e353a2fb7e87bbe86c3f6dc439e8d50b9210.jpg)  
Fig. 1. System model for deploying UAVs to provide wireless coverage to the target area A $( \beta , d )$ , where UAV $\mu _ { i }$ with coverage radius $r _ { i }$ is deployed from $x _ { i }$ <sup>b</sup>initially to $y _ { i } \in [ 0 , \beta ]$ <sup>m</sup>at operating altitude $\dot { h } _ { i }$

## 3 SYSTEM MODEL AND PROBLEM FORMULATION

This section introduces our system model and problem formulation for deploying UAVs to provide wireless coverage to the whole target.

As shown in Fig. 1, a centralized system needs to emergently deploy UAVs to provide full wireless coverage over the target area A, which is a rectangle with length $\beta$ and <sup>b</sup>width d as in Equation (1). Restricting the target area to be a thin rectangular area is reasonable to mimic avenues, streets and highways. The notations and corresponding meanings are given in Table 1. The UAVs in a set $\bar { \mathbf { U } } = \{ \mu _ { 1 } , \ldots , \mu _ { n } \}$ are initially located in different locations $\{ x _ { 1 } , \ldots , x _ { n } \}$ along <sup>1 . . .</sup>x-axis (e.g., in ground UAV stations) before the deployment. Without loss of generality, we assume $x _ { 1 } \leq \cdots \leq x _ { n }$ . We denote a UAV $\mu _ { i } { ' } \mathfrak { s }$ <sup>1</sup>s final position after deployment as $( y _ { i } , h _ { i } )$ <sup>m</sup>at operating altitude $h _ { i } .$ . The $\mathrm { U A V } ~ \mu _ { i }$ flies from its initial location $( x _ { i } , 0 )$ <sup>m</sup>to its designed destination $( y _ { i } , h _ { i } )$ and then hovers at the operating altitude $h _ { i }$ to serve the ground users.

$$
\mathbf { A } = \{ ( w , l ) | 0 \leq w \leq d , 0 \leq l \leq \beta \} .\tag{}
$$

We assume that the UAVs have sufficient bandwidth resources so that all UAVs can be assigned orthogonal channels and for avoiding interference-free. This interferencefree model is widely used (e.g., [14], [27]). In practice the assigned channels for distant UAVs can be reused during deployment. Thus, we assume the interference among UAVs can be ignored, and henceforth we focus our study on dealing with the UAV coverage issue.

As in [9], we adopt the air-to-ground model where the wireless communication channels between UAVs and ground users in the target area are dominated by LoS links. LoS links are expected for air-to-ground channels in many scenarios [1]. Therefore, the channel power gain from the UAV to each user k is modeled as the free-space path loss model, i.e., $g _ { k } = \xi \bar { d _ { k } } ^ { - 2 } ,$ , where $\xi$ denotes the channel power gain at a reference distance. $\bar { d } _ { k }$ is the link distance between the UAV and ground user k. Given a standard transmission power $P _ { i } ,$ , the signal-to-noise ration (SNR) at ground user k is given by $\begin{array} { r } { \gamma _ { k } = \frac { P _ { i } g _ { k } } { \sigma ^ { 2 } } } \end{array}$ , where $\sigma ^ { 2 }$ denotes the noise power at <sup>s</sup>each ground user. We say a ground user k is covered by a UAV if the SNR at user k is no less than a threshold value $\gamma _ { t h } ,$ which indicates the target data rate of each user is at <sup>g</sup>least þ $( 1 + \gamma _ { t h } )$ . Thus, we can obtain the correlation 1 l $\mathrm { U A V ^ { \prime } s }$ wireless coverage range r (i.e., the maximum ground range for just achieving the threshold SNR $\gamma _ { t h } )$ and operating altitude h as $\begin{array} { r } { \frac { P _ { i } \xi } { \sigma ^ { 2 } ( r ^ { 2 } + h ^ { 2 } ) } = \gamma _ { t h } . } \end{array}$ We have $\begin{array} { r } { r _ { i } = \sqrt { \frac { P _ { i } \xi } { \gamma _ { t h } \sigma ^ { 2 } } - h _ { i } ^ { 2 } } } \end{array}$ for $\mathrm { U A V } \mu _ { i }$

TABLE 1 Notations and Their Physical Meanings
<table><tr><td>Notation</td><td>Meaning</td></tr><tr><td>n</td><td>Number of UAVs</td></tr><tr><td> $\mu _ { i }$ </td><td>Index of UAV i</td></tr><tr><td> $\beta$ </td><td>Rightmost endpoint of the interval  $L = [ 0 , \beta ]$ </td></tr><tr><td> $x _ { i }$ </td><td>Initial location of UAV i before deployment</td></tr><tr><td> $y _ { i }$ </td><td>Final location of UAV i after deployment</td></tr><tr><td> $r _ { i }$ </td><td>Coverage radius of UAV i</td></tr><tr><td> $h _ { i }$ </td><td>Operating altitude of UAV i</td></tr><tr><td> $v _ { i }$ </td><td>Flying speed of UAV i</td></tr><tr><td> $T$ </td><td>Maximum deployment delay obtained by Algorithm 3</td></tr><tr><td> $T ^ { * }$ </td><td>Minimum maximum deployment delay of problem (6)</td></tr><tr><td> $\Gamma ^ { \prime }$ </td><td>Total deployment delay obtained by Algorithm 3</td></tr><tr><td> $\Gamma ^ { * }$ </td><td>Minimum total deployment delay  $\begin{array} { r } { \dot { \Gamma } ^ { * } = \sum _ { 1 \leq i \leq n } T _ { i } ^ { * } } \end{array}$ </td></tr><tr><td>€</td><td>The relative error in Algorithm 3</td></tr></table>

A particular UAV $\mu _ { i }$ operating at final position $( y _ { i } , h _ { i } )$ covers a region $D _ { i }$ <sup>m</sup>in the target rectangular, which is defined in Equation (2).

$$
\begin{array} { c } { { D _ { i } = \left\{ ( w , l ) | - \displaystyle \frac { d } { 2 } \leq w \leq \displaystyle \frac { d } { 2 } , \right. } } \\ { { \left. y _ { i } - \sqrt { r _ { i } ^ { 2 } - \left( \displaystyle \frac { d } { 2 } \right) ^ { 2 } } \leq l \leq y _ { i } + \sqrt { r _ { i } ^ { 2 } - \left( \displaystyle \frac { d } { 2 } \right) ^ { 2 } } \right\} . } } \end{array}\tag{}
$$

We require a full coverage over the target target area A $( \beta , d )$ by deploying n diverse UAVs, i.e., $\mathbf { A } ( { \bar { \beta } } , d ) \subseteq \cup { } _ { 1 } ^ { n } D _ { i }$

During the deployment, UAV $\mu _ { i }$ <sup>b 1</sup>travels an Euclidean distance $\sqrt { \left( y _ { i } - x _ { i } \right) ^ { 2 } + h _ { i } ^ { 2 } }$ at constant flying speed $v _ { i }$ as in [29]. Thus, its travel time is given $\mathrm { b y } ^ { 2 }$

$$
T _ { i } ( y _ { i } ) = \frac { \sqrt { ( y _ { i } - x _ { i } ) ^ { 2 } + h _ { i } ^ { 2 } } } { v _ { i } } .\tag{}
$$

After considering all UAVs’ travel time, we define the maximum deployment delay as the maximum travel time among all UAVs till reaching the full coverage over the

target area A. Our maximum deployment delay optimization problem is thus

$$
\begin{array} { r l } & { \underset { \{ y _ { 1 } , \ldots , y _ { n } \} } { \operatorname* { m i n } } \underset { 1 \leq i \leq n } { \operatorname* { m a x } } T _ { i } ( y _ { i } ) , } \\ & { } \\ & { \mathrm { s . } t . , \textbf { A } \subseteq \bigcup _ { 1 } ^ { n } D _ { i } . } \end{array}\tag{}
$$

Note that the min-max objective is to balance the deployment time among all UAVs and fairly optimize the delay bottleneck for reaching the full coverage of the target.

In addition, we further consider the total deployment delay objective as the summation of travel times of all UAVs till reaching the full coverage over the target inter-$\mathrm { v a l } . ^ { 3 }$ Under the efficiency consideration, our total deployment delay optimization problem is thus

$$
\begin{array} { l } { \displaystyle \operatorname* { m i n } _ { \{ y _ { 1 } , \ldots , y _ { n } \} } \sum _ { 1 \leq i \leq n } T _ { i } ( y _ { i } ) , } \\ { \mathrm { s . } t . , \ \mathbf { A } \subseteq \bigcup _ { 1 } ^ { n } D _ { i } . } \end{array}\tag{}
$$

We assume $\begin{array} { r } { 2 \sum _ { i = 1 } ^ { n } \sqrt { r _ { i } ^ { 2 } - ( \frac { d } { 2 } ) ^ { 2 } } \ge \beta } \end{array}$ and $\begin{array} { r } { r _ { i } \geq \frac { d } { 2 } } \end{array}$ throughout the paper. Otherwise, there is no feasible deployment to problems (4) and (5). Since the width d of the rectangular area A is a given constant value, we can restrict $d \to 0$ to facilitate the <sup>0</sup>theoretical analysis in the following. Thus, the target region becomes a line interval $L = [ 0 , \beta ]$ as in [30], [31]. We show later in Sections 4 and 5 that our problems on this line interval are already NP-complete, which can shed light on the solutions to a rectangular target area A. Note that the minimum total deployment delay in problem (4) is not smaller than that in problem (5), while the maximum deployment delay in problem (5) is not smaller than that in problem (4).

Based on above problem formulations, the two fast UAV deployment problems belong to the domain of combinatorial optimization. The optimal UAV deployment is a specific combination of ordered UAVs, which is generally exponential in the number of UAVs. For a combinatorial optimization problem, theoretical insights of tractability and algorithmic results are the main concerns for problem solution. Though we consider the simplest possible line interval for target area as in [31], the fast UAV deployment problems (by considering different coverage radii $r _ { i } ^ { \prime } \mathbf { s } ,$ operating altitudes $h _ { i } ^ { \prime } \mathbf { s }$ and flying speeds $v _ { i } ^ { \prime } \mathbf { s }$ are beyond prior deployment literature’s methods for homogeneous sensor networks $( \mathrm { i . e . , }$ , [30], [32]). As we will show later in Sections 4 and 5, both problems (4) and (5) are actually NP-complete. They are difficult to solve due to the UAVs’ distinct initial locations and their multi-dimensional heterogeneity, which result in exponential number of sequences and combinations of UAVs.

Due to page limit, we skip several proofs in the maintext, and readers can find them in the appendices or directly from [19].

## 4 OPTIMIZATION OF MIN-MAX DEPLOYMENT PROBLEM

In this section, we investigate how to dispatch a number n of UAVs in a fair manner by targeting at the deployment delay to a user location in the worst case. Our min-max problem in (4) aims to minimize the maximum deployment delay among all UAVs such that any possible user located in the target region A $( \beta , d )$ is treated fairly.

<sup>b</sup>In the following, we first show that the problem (4) when UAVs are dispatched from different locations $( { \mathrm { i . e . , ~ } } x _ { i } \neq x _ { j } )$ is NP-complete by reduction from the classic 3-partition problem [33].

Theorem 1. The min-max deployment delay problem in (4) is NP-complete.

Proof. See Appendix A, which can be found on the Computer Society Digital Library at http://doi.ieeecomputersociety. org/10.1109/TMC.2018.2840143. tu

## 4.1 Optimal UAV Deployment from the Same Location

We first study a special case of problem (4) by dispatching the UAVs from the same initial location $( \mathbf { i . e . } , \ x _ { i } = x _ { j }$ for $1 \leq i , j \leq n )$ . Without loss of generality, we assume that $x _ { i } \leq 0 , \forall \mu _ { i } , 1 \leq i \leq n ,$ , which is symmetric to the case of $x _ { i } \geq \beta .$ <sup>m 1</sup>. Note that for the case of $0 < x _ { i } < \beta ,$ we can divide <sup>b 0</sup>the line interval into two subintervals, i.e., $[ 0 , x _ { i } ]$ and $[ x _ { i } , \beta ] .$ <sup>0 b</sup>and apply our deployment algorithm (as presented later) similarly over both subintervals.

If a UAV has the larger the distance from the initial location to the target position, it incurs a larger travel time. Among all $\mathrm { U A V s } ,$ we first consider which UAV to send and cover the furthest point of the target area. Specifically, given the current uncovered line interval (½ ;  initially or uncovered subinter-<sup>0 b</sup>val), we sequentially select an unassigned $\mathrm { U A V } \left( \mathrm { e . g . , } \mu _ { i } \right)$ with <sup>m</sup>the minimum travel time to just cover the furthest point on the remaining uncovered interval during deployment. In our problem, though we dispatch all UAVs simultaneously, it is equivalent to dispatching of UAVs one by one to cover the line interval ½ ; . We only count and compare each UAV’s <sup>0 b</sup>travel time to calculate the maximum delay objective.

As shown in Algorithm 1, initially, we set ${ \overline { { \beta } } } = \beta$ and the available (unassigned) UAV set $\mathbf { U } ^ { - } = \mathbf { U }$ <sup>b b</sup>, as we haven’t sent any UAV to cover any point in the line interval yet. In each iteration, we dispatch a UAV $\mu _ { j }$ with the minimum travel

distance $T _ { j } = \frac { \sqrt { ( \overline { { \beta } } - r _ { j } ) ^ { 2 } + h _ { j } ^ { 2 } } } { v _ { i } }$ in the available UAV set ${ \bf U } ^ { - }$ to new position $( \overline { { \beta } } - r _ { j } , h _ { j } )$ . Then the uncovered interval decreases from $[ 0 , { \overline { { \beta } } } ]$ to $[ 0 , \overline { { \beta } } - 2 r _ { j } ]$ . We record $\mu _ { j } ^ { \prime } \boldsymbol { \mathsf { s } }$ travel time $T _ { j }$ <sup>0 b 0 b 2</sup>into set T and remove UAV $\mu _ { j }$ <sup>m</sup>from U<sup></sup>. We con-<sup>m</sup>tinue to dispatch another UAV until the target interval is fully covered. In the end, we obtain the maximum deployment delay T as the optimum T. Note that given the <sup>max</sup>UAVs operating altitudes, we prefer to deploy those UAVs with larger flying speeds and larger coverage radius further away in the target area.

Proof. See Appendix B, available in the online supplemental material. tu

Algorithm 1. Optimal UAV Dispatching Algorithm from   
the Same Location   
1: Input:   
$\mathbf { U } = \{ \mu _ { 1 } , \mu _ { 2 } , \ldots , \mu _ { n } \}$   
<sup>m1</sup>2: Output:   
y<sup></sup>: final location of $\mu _ { i }$   
<sup>m</sup>T: optimal deployment delay   
3: $\overline { { \beta } } = \dot { \boldsymbol { \beta } } , \mathbf { U } ^ { - } = \dot { \bar { \mathbf { U } } } , \dot { \bar { \mathbf { T } } } = \boldsymbol { \emptyset }$   
<sup>b b</sup>4: while $\overline { { \beta } } > 0$ do   
5: $\begin{array} { r } { \mu _ { j }  \arg \operatorname* { m i n } _ { \mu _ { i } \in \mathbf { U } ^ { - } } \frac { \sqrt { ( \overline { { \beta } } - r _ { i } ) ^ { 2 } + h _ { i } ^ { 2 } } } { v _ { i } } } \end{array}$   
6: $\begin{array} { r } { \mathbf { T }  \mathbf { T } \cup T _ { j } = \frac { \sqrt { ( \overline { { \beta } } - r _ { j } ) ^ { 2 } + h _ { j } ^ { 2 } } } { v _ { j } } } \end{array}$   
7: $\overline { { \beta } } \gets \overline { { \beta } } - 2 r _ { j }$   
8: $y _ { j }  \overline { { \beta } } - r _ { j } , \mathbf { U } ^ { - }  \mathbf { U } ^ { - } \backslash \{ \mu _ { j } \}$   
<sup>b</sup>9: end while   
10: return T T

## 4.2 Problem Reformulation under Order Preserving of UAVs’ Locations

Since problem (4) is NP-complete generally, there is no efficient algorithm to find the optimal solution, unless $\mathrm { P } = \mathrm { N P }$ Accordingly, we propose that the UAVs preserve their initial locations’ order during the deployment. Without loss of generality, we assume $x _ { 1 } \leq x _ { 2 } \ldots \leq x _ { n }$ Given the order $\propto$ <sup>1 2 . . .</sup>according to the UAVs’ initial locations $x _ { i } ^ { \prime } \mathbf { s } ,$ the final locations $y _ { i } ^ { \prime } \mathbf { s }$ of UAVs must meet the requirement: $y _ { i } \le y _ { j }$ if and only if $x _ { i } \leq x _ { j }$ . This simplifies the coordination among UAVs, and thus will simplify the algorithm design later. In practice, this is reasonable as it avoids any possible collision when two UAVs cross each other to reach their final positions [34].

Our optimization problem is to minimize the deployment delay for reaching full coverage of the target area subject to the order $\propto ,$ i.e.,

$$
\begin{array} { r l r } {  { \operatorname* { m i n } _ { \{ y _ { 1 } , \ldots , y _ { n } \} } \operatorname* { m a x } _ { 1 \leq i \leq n } T _ { i } ( y _ { i } ) , } } \\ & { } & \\ & { } & { \mathrm { s . } t . , \ [ 0 , \beta ] \subseteq \bigcup _ { 1 } ^ { n } [ y _ { i } - r _ { i } , y _ { i } + r _ { i } ] , } \\ & { } & \\ & { } & { y _ { i } \leq y _ { i + 1 } , \forall 1 \leq i \leq n - 1 . } \end{array}\tag{}
$$

Note that the last inequality is due to location order preserving and $x _ { 1 } \leq \cdots \leq x _ { n }$ . This simplified problem is still diffi-<sup>1</sup>cult to solve since selecting a specific combination of UAVs as the optimal UAV deployment is generally exponential in the number of UAVs. In the following, we first introduce the feasibility checking problem for problem (6) and design the corresponding algorithm to determine whether we can find a deployment scheme within the deadline. Then, we use binary search over those feasible deadlines to find the minimum deployment delay (deadline).

## 4.2.1 Feasibility Checking Problem

We first define the feasibility checking problem as follows: given any deployment delay $T > 0$ and order requirement $\propto ,$ determine whether $\mathrm { \dot { U } A V s }$ <sup>0</sup>can be moved to reach a full coverage within deadline T . Let $T ^ { * }$ denotes the optimal deployment delay of problem (6), we next design a feasibility checking algorithm to determine whether $T \geq T ^ { * }$ or whether such $\bar { T }$ is feasible to achieve via UAV dispatching.

Consider any $T > 0 ,$ for $\mathrm { U A V } \mu _ { i } \in \mathbf { U }$ with altitude $h _ { i } ,$ if $v _ { i } \cdot T \geq h _ { i } , \sqrt { \left( v _ { i } T \right) ^ { 2 } - h _ { i } ^ { 2 } }$ is the maximum horizontal distance to move on $L = [ 0 , \beta ]$ . We define $a _ { i }$ as the leftmost point and $b _ { i }$ <sup>0 b</sup>as the rightmost point on $L$ that can be covered by $\mu _ { i }$ within T . We call $a _ { i } \ ( { \mathrm { r e s p . } } , b _ { i } )$ <sup>m</sup>the leftmost (resp., rightmost) T -coverable point of $\mu _ { i }$ . Then we have

$$
a _ { i } = x _ { i } - r _ { i } - \sqrt { \left( v _ { i } T \right) ^ { 2 } - h _ { i } ^ { 2 } } ,\tag{}
$$

$$
b _ { i } = x _ { i } + r _ { i } + \sqrt { \left( v _ { i } T \right) ^ { 2 } - h _ { i } ^ { 2 } } .\tag{}
$$

Algorithm 2 solves the feasibility checking problem. It first computes $a _ { i }$ and $b _ { i }$ in Equations (7) and (8), then deploys the UAVs one by one according to the order / from the left endpoint of target interval ½ ; . As $x _ { 1 } \leq x _ { 2 } \leq \cdot \cdot \cdot \leq x _ { n } ,$ , we start with UAV $\mu _ { 1 }$ <sup>0 b</sup>and end up with $\mu _ { n } .$ <sup>2</sup>. Given our current covered interval $[ 0 , { \overline { { \beta } } } ]$ <sup>m</sup>where the boundary ${ \overline { { \beta } } } < \beta ,$ iteration i <sup>0 b</sup>starts with checking whether UAV $\mu _ { i }$ <sup>b b</sup>can fly to altitude $h _ { i }$ $( { \mathrm { i . e . , } } v _ { i } \cdot T \geq h _ { i } )$ or not.

\- If $v _ { i } T < h _ { i } ,$ , we will not consider dispatching UAV $\mu _ { i } .$

<sup>m</sup>If $v _ { i } T \geq h _ { i } ,$ we still need to check if $\mu _ { i }$ can seamlessly cover the point $\overline { { \beta } } ( \mathrm { i . e . , ~ } \overline { { \beta } } \in [ a _ { i } , b _ { i } ] )$ <sup>m</sup>. If this also holds, <sup>b b</sup>we will efficiently deploy $\mu _ { i }$ to $y _ { i } = \operatorname* { m i n } ( { \overline { { \beta } } } + r _ { i }$ $b _ { i } - r _ { i } )$

Noted that once $\mu _ { i }$ is deployed to the left of UAV $\mu _ { j } ,$ in which $j < i ,$ <sup>m m</sup>then Algorithm 2 in line 10 will undo dispatching of $\mu _ { j }$ and will not use this UAV. After a successful dis-<sup>m</sup>patching of UAV $\mu _ { i } ,$ the covered interval prolongs from ½ ;  to $\left[ 0 , y _ { i } + r _ { i } \right]$ in this iteration.

<sup>b 0</sup>If T is feasible $( T \geq T ^ { * } )$ , our algorithm will return a subset ${ \bf U } ^ { - }$ of UAVs and their new locations $y _ { i } \mathrm { ' s }$ to fully cover target L within T. For each UAV $\mu _ { i } \in \mathbf { U } \backslash \mathbf { U } ^ { - }$ <sup></sup>, it will not be <sup>m</sup>used and just stay at the initial location.

Proposition 2. The feasibility checking problem for a particular deadline is optimally solved by Algorithm 2 in $O ( n ^ { 2 } )$ time.

Proof. See Appendix $C ,$ available in the online supplemental material. tu

Remark that the feasibility checking problem has independent interest because it characterizes the minimization problem model, in which each UAV has the same deployment delay deadline T and we want to know whether they can move to reach a full coverage.

## 4.2.2 Binary Search over Feasible Deadlines

With the help of Algorithm 2, we can verify whether a given deadline T is feasible or not. The minimum deadline among all feasible ones is actually the optimum of problem (6). Here, we apply binary search to find the minimum deadline and solve problem (6). Before the search, we still need to determine the search scope and step of T .

```perl
feasibility checking
infeasible feasible
T' T"
εT1
$T _ { l }$ $T _ { u }$
```  
Fig. 2. Binary search on $[ T _ { l } , T _ { u } ]$ with accuracy level of $\epsilon \cdot T _ { l } .$

Algorithm 2. Feasibility Checking Algorithm   
1: Input:   
$\mathbf { U } = \{ \mu _ { 1 } , \mu _ { 2 } , \ldots , \mu _ { n } \}$   
<sup>m1 m2 . . . m</sup>T : a given deployment delay deadline for all UAVs   
2: Output:   
y : final locations of $\mu _ { i }$   
3: Compute $a _ { i }$ <sup>m</sup>in Equation (7) and $b _ { i }$ in Equation (8) if $v _ { i } T \geq h _ { i }$   
4: $\overline { { { \boldsymbol \beta } } } = \dot { 0 } ; { \bf U } ^ { - } = { \bf U } ; { \bf S } ^ { c } = \boldsymbol \emptyset$   
5: for $i = 1$ to n do   
6: if ${ \overline { { \beta } } } \notin [ a _ { i } , b _ { i } ]$ or $v _ { i } T < h _ { i }$ then   
7: $\mathbf { U } ^ { - }  \mathbf { U } ^ { - } \backslash \{ \mu _ { i } \}$   
8: else   
9: $y _ { i } \gets \operatorname* { m i n } \{ \overline { { \beta } } + r _ { i } , b _ { i } - r _ { i } \}$   
10: $\mathbf { S } ^ { c } \gets \mathbf { S } ^ { c } \dot { \cup } \left\{ u _ { j } \in U ^ { - } : j < i , y _ { j } > y _ { i } \right\}$   
11: $\mathbf { U } ^ { - }  \mathbf { U } ^ { - } \backslash \bar { \mathbf { S } } ^ { c } , \overline { { \beta } }  y _ { i } + r _ { i }$   
12: end if   
13: $\mathbf { i } \mathbf { f } \ \overline { { \beta } } \ < \ \beta$ then   
14: <sup>b b</sup>Break;   
15: end if   
16: end for   
17: i $\mathsf { f } \ \overline { { \beta } } \ < \ \beta$ then   
<sup>b b</sup>18: return $T$ is notfeasible $( T < T ^ { * } )$   
19: else   
20: return $T$ is feasible $( T \geq T ^ { * } )$   
21: end if

For each single UAV $\mu _ { i } ,$ the minimum moving distance is altitude $h _ { i } .$ <sup>m</sup>. Thus, the lower bound of $T$ (denoted as $T _ { l } )$ among all UAVs can be determined according to

$$
T _ { l } = \operatorname* { m i n } _ { 1 \leq i \leq n } \frac { h _ { i } } { v _ { i } } .\tag{}
$$

In general, T is not feasible because it is the minimum possible travel time among all UAVs. We next determine the upper bound of $T$ (denoted as $\boldsymbol { T _ { u } } )$ . For UAV $\mu _ { i } ,$ the maximum possible moving distance of $\mu _ { i }$ <sup>m</sup>is to reach position $( 0 , h _ { i } )$ or $( \beta , h _ { i } )$ <sup>m</sup>beyond the leftmost or rightmost location on <sup>0 b</sup>the target interval $L = [ 0 , \beta ]$ . Thus, the upper bound of $T$ (denoted as $\boldsymbol { T _ { u } } )$ <sup>0 b</sup>among all UAVs is given by

$$
T _ { u } = \operatorname* { m a x } _ { 1 \leq i \leq n } \left\{ \frac { \operatorname* { m a x } \{ \sqrt { ( \beta - x _ { i } ) ^ { 2 } + h _ { i } ^ { 2 } } , \sqrt { x _ { i } ^ { 2 } + h _ { i } ^ { 2 } } \} } { v _ { i } } \right\} .\tag{}
$$

In the binary search, we define the relative error as - which is a small constant value, and accordingly set the search accuracy as $\epsilon T _ { l }$ . As illustrated in Fig. 2, the binary search starting with $T _ { l }$ stops once switching from infeasible deadline $T ^ { \prime }$ to feasible $T ^ { \prime \prime } ,$ such that the resultant $T ^ { \prime \prime }$ is our searched optimum for problem (6).

Thus, we can obtain the following fully polynomial-time approximation scheme (i.e., Algorithm 3) to solve problem (6) by combining both binary search and Algorithm 2.

Theorem 2. Let $T ^ { * }$ be the optimal deployment delay of problem   
(6). Given any small allowable error $\epsilon > 0 ,$ , there exists an   
FPTAS with running time $\begin{array} { r } { O ( n ^ { 2 } \log { \frac { 1 } { \epsilon } } ) } \end{array}$ <sup>0</sup>to arbitrarily approach   
the global optimum (i.e., $T ^ { \ast } \leq T \leq ( 1 + \epsilon ) T ^ { \ast } )$

Proof. The deployment delay of a given instance has an upper bounded of $T _ { u }$ and a lower bound of $T _ { l } .$ Obviously, $\begin{array} { r } { \hat { T _ { l } } \overset { \cdot } { \leq } T ^ { * } \leq T _ { u } . } \end{array}$ . Choosing a small constant $\epsilon > 0 ,$ we divide each $T _ { l }$ into $\frac { 1 } { \epsilon }$ <sup>0</sup>sub-intervals. Here, to make the discussion easier, we assume $\textstyle { \frac { 1 } { \epsilon } }$ is an integer). Each interval has length $\epsilon \cdot T _ { l } ,$ where $\epsilon \cdot T _ { l } \leq \epsilon \cdot T ^ { * }$ . We divide $T _ { u }$ by $\epsilon \cdot T _ { l }$ into $\begin{array} { r } { \lceil \frac { T _ { u } } { \epsilon \cdot T _ { l } } \rceil } \end{array}$ sub-intervals as I as in Algorithm 3. Overall, we have $\lceil \frac { T _ { u } } { \epsilon \cdot T _ { l } } \rceil$ intervals on I.

Then, each step of binary search will shrink the interval I by applying Algorithm $2$ on certain value of T . It terminates with deployment delays $T ^ { \prime }$ and $T ^ { \prime \prime } ,$ as shown in Fig. 2, in which $\dot { T } ^ { \prime } < T ^ { * }$ and $T ^ { \prime \prime } = T ^ { \prime } + \epsilon \cdot T _ { l } > T ^ { * }$ . The resultant $T ^ { \prime \prime }$ is our searched optimum for problem (6). We have that $T ^ { \prime \prime } = T ^ { \prime } + \epsilon \cdot T _ { l } \leq \hat { T ^ { * } } + \epsilon \cdot T _ { l } \leq \hat { ( 1 + \epsilon ) } T ^ { * }$ . Overall, we obtain $T ^ { \ast } < T \leq ( 1 + \epsilon ) T ^ { \ast }$

<sup>1</sup>Therefore, we obtain the deployment delay which has an approximation ratio $1 + \epsilon$ over the global optimum. <sup>1</sup>Our feasibility checking algorithm runs in $O ( \bar { n ^ { 2 } } )$ time, and we have $\begin{array} { r } { { \cal { \dot { O } } } ( [ \frac { T _ { u } } { \epsilon \cdot T _ { l } } ] ) } \end{array}$ candidate deadlines. Overall, this algorithm runs in $\dot { O } ( n ^ { 2 } \log \frac { 1 } { \epsilon } )$ since binary search runs in at worst logarithmic time. tu

Note that the relative error of the proposed FPTAS is only due to the small constant value - that we choose in binary search.

Algorithm 3. FPTAS for Minimizing the Maximum   
Deployment Delay   
1: Input:   
$\begin{array} { r } { I \stackrel { \cdot } { = } \{ \epsilon T _ { l } , 2 \epsilon T _ { l } , . . . , \lceil \frac { T _ { u } } { \epsilon \cdot T _ { l } } \rceil \epsilon T _ { l } \} } \end{array}$ where $T _ { l }$ and $T _ { u }$ are given in (9)   
and (10)   
2: Output:   
IðidxÞ: idx is the index   
3: low and $\begin{array} { r } { h i g h  \lceil \frac { T _ { u } } { \epsilon \cdot T _ { l } } \rceil } \end{array}$   
<sup>1</sup>4: while low $< = h i g h$ do   
5: mid floorððlow þ highÞ= Þ   
6: <sup>2</sup>feasibility checking by Algorithm 2 on IðmidÞ   
7: if IðmidÞ is feasible then   
8: high mid   
9: else   
10: low mid   
11: end $\mathbf { i f }$   
12: if low ¼¼ high  then   
13: idx high   
14: break   
15: end if   
16: end while   
17: return $I ( i d x )$

## 5 TOTAL UAV DEPLOYMENT DELAY OPTIMIZATION

In this section, we further consider the efficiency problem through minimizing the total UAV deployment delay for July 05,2026 at 12:27:12 UTC from IEEE Xplore. Restrictions apply.

covering the target interval. We first show that problem (5) when UAV dispatching from different locations is NP-complete by reduction from 3-partition problem [33]. The proof is similar to Theorem 1.

Theorem 3. The total deployment delay minimization problem in (5) is NP-complete.

Proof. See Appendix D, available in the online supplemental material. tu

## 5.1 Fast Algorithm for UAVs Deployment from the Same Location

We first study the problem of dispatching the UAVs from the same initial location, i.e., $x _ { i } = x _ { j }$ for $1 \leq i , j \leq n$ . Different <sup>1</sup>from the previous min-max optimization problem in Section 4.1, the problem here is still difficult to solve. Because in minmax optimization problem, we only focus on the bottleneck (the maximum one) of all UAVs’ deployment delay and reduce deployment delays of all UAVs in a fair manner, while the min-sum problem targets at minimizing the sum of the deployment delays of selected UAVs in the solution. Without loss of generality, we assume that $x _ { i } \leq 0 , \ \forall \ \mu _ { i } , 1 \leq i \leq n ,$ which is symmetrical to the case that $x _ { i } \geq \beta .$ <sup>m 1</sup>Our problem of <sup>b</sup>dispatching all UAVs simultaneously is equivalent to dispatching of UAVs one by one to cover the line interval $[ 0 , \beta ]$ from its right endpoint (or furthest point) $\beta$ <sup>0 b</sup>to left endpoint <sup>b</sup>(closest point) 0. Intuitively, if all UAVs have the same flying speed and operating altitude, the optimal deployment scheme is to deploy a UAV with longer wireless coverage radius to further location for saving the travel distance and delay. Specifically, given a target interval $( [ 0 , \beta ]$ initially or remaining <sup>0 b</sup>uncovered interval during deployment), we sequentially select the unused UAV with the longest wireless coverage radius among all available UAVs to reach the furthest point in the remaining uncovered interval.

As shown in Algorithm 4, initially, we set ${ \overline { { \beta } } } = \beta$ and the available UAV set $\mathbf { \bar { U } } ^ { - } = \mathbf { U }$ <sup>b b</sup>. In each iteration, we dispatch a UAV $\mu _ { j }$ from the available UAV set ${ \bf U } ^ { - }$ with longest wire-<sup>m</sup>less coverage radius $r _ { j }$ to extend the current covered interval $[ { \overline { { \beta } } } , \beta ] .$ , as shown in Lines 7 and 8 of Algorithm 4. Next, <sup>b b</sup>we add $\mu _ { j } ^ { \prime } \boldsymbol { \mathsf { s } }$ travel time $T _ { j }$ to T. Then, we update the covered interval to $[ \overline { { \beta } } - 2 r _ { j } , \beta ]$ and remove the $\mathrm { U A V } \mu _ { j }$ from U<sup></sup> <sup>b 2 b m</sup>until the target interval is fully covered. In the end, we obtain the total deployment delay $\Gamma = \sum \mathbf { T } .$ . Note that we may only select a subset of UAVs with minimum total deployment delay to cover the target interval ½ ;  in final solution, since $2 \dot { \sum _ { i = 1 } } { r _ { i } } \ge \beta .$

Lemma 1. If all UAVs have the same flying speed and operating altitude, Algorithm 4 optimally solves the min-sum deployment problem when dispatching n UAVs from the same location.

Proof. See Appendix E, available in the online supplemental material. tu

Proposition 3. Let G<sup></sup> be the optimal total deployment delay of problem (5) when dispatching the UAVs from the same initial location. Algorithm 4 of computational complexity $O ( n )$ can obtain the total deployment delay $\Gamma \leq \dot { \kappa } \tau \Gamma ^ { * }$ , where $\kappa =$ $h _ { m a x } / h _ { m i n }$ and $\tau = v _ { m a x } / v _ { m i n } .$

Proof. Suppose that all the UAVs are fixed with the same altitude and flying speed, by applying Algorithm 4, we Authorized licensed use limited to: Guangxi University. Downloaded o can obtain the optimal solution of minimizing the total delay for dispatching UAVs from the same location by Lemma 1.

Next, we assume that all the UAVs are fixed with the same altitude $h _ { m a x } = \operatorname* { m a x } h _ { i }$ and flying speed $v _ { m i n } = \mathrm { m i n } v _ { i } .$ <sup>max min</sup>Thus, on one hand, we can find the optimal solution by Algorithm 4 and obtain the total deployment delay $\begin{array} { r } { \Gamma _ { m a x } = \frac { 1 } { v _ { m i n } } \sum _ { 1 \leq i \leq n } \sqrt { y _ { i } ^ { 2 } + h _ { m a x } ^ { 2 } } . } \end{array}$ On the other hand, by applying the same algorithm, we find the total deployment delay $\begin{array} { r } { \Gamma _ { m i n } = \frac { 1 } { v _ { m a x } } \sum _ { 1 \leq i \leq n } \sqrt { y _ { i } ^ { 2 } + h _ { m i n } ^ { 2 } } } \end{array}$ if all the UAVs are fixed with the same altitude $h _ { m i n } = \operatorname* { m i n } h _ { i }$ and flying speed $v _ { m a x } = \operatorname* { m a x } v _ { i }$ . We can see that $\Gamma _ { m i n } \leq \Gamma ^ { * }$ , in which $\bar { \Gamma ^ { * } }$ is the <sup>max</sup>total deployment delay in the optimal solution. Moreover, since $\begin{array} { r } { \kappa = \frac { \displaystyle h _ { m a x } } { \displaystyle h _ { m i n } } \ge 1 } \end{array}$ and $\begin{array} { r } { \tau = \frac { v _ { m a x } } { v _ { m i n } } \ge 1 } \end{array}$ , the following holds:

$$
\begin{array} { r l r } {  { \Gamma _ { m a x } = \frac { 1 } { v _ { m i n } } \sum \sqrt { y _ { i } ^ { 2 } + h _ { m a x } ^ { 2 } } } } \\ & { } & { = \frac { \tau } { v _ { m a x } } \sum \sqrt { y _ { i } ^ { 2 } + \kappa ^ { 2 } h _ { m i n } ^ { 2 } } } \\ & { } & { \leq \kappa \tau \frac { 1 } { v _ { m a x } } { \sum \sqrt { y _ { i } ^ { 2 } + h _ { m i n } ^ { 2 } } } } \\ & { } & { \leq \kappa \tau \Gamma _ { m i n } . } \end{array}
$$

The total deployment delay obtained by Algorithm 4 is G and we have $\Gamma \leq \Gamma _ { m a x } ^ { \dot { } }$ . Thus, $\mathrm { \bar { \Gamma } } \leq \mathrm { \bar { \Gamma } } _ { m a x } \leq \kappa \tau$ $\Gamma _ { m i n } \leq \kappa \tau \Gamma ^ { * }$

<sup>kt</sup>With respect to the time complexity, we can see that there are at most n iterations for the while loop, Algorithm 4 runs in linear time, which completes our proof. tu

Algorithm 4. Fast Algorithm for Dispatching UAVs from   
the Same Location   
1: Input:   
$\mathbf { U } = \{ \mu _ { 1 } , \mu _ { 2 } , \ldots , \mu _ { n } \}$   
<sup>m1</sup>2: Output:   
y : final location of $\mu _ { i }$   
<sup>m</sup>G: total deployment delay   
3: $\overline { { \beta } } = \beta , \mathbf { U } ^ { - } \overset { \bullet } { = } \bar { \mathbf { U } } , \mathbf { T } = \varnothing$   
<sup>b b</sup>4: while $0 < \overline { { \beta } } \le \beta$ do   
5: $\mu _ { j }  \arg \operatorname* { m a x } _ { \mu _ { i } \in \mathbf { U } ^ { - } } r _ { i }$   
6: $\mathbf { T }  \mathbf { T } \cup T _ { j } = \frac { \sqrt { ( ( \overline { { \beta } } - r _ { j } ) ^ { 2 } + h _ { j } ^ { 2 } ) } } { v _ { j } }$   
7: $\overline { { \beta } } \gets \overline { { \beta } } - 2 r _ { j }$   
8: $y _ { j }  \overline { { \beta } } - r _ { j } , \mathbf { U } ^ { - }  \mathbf { U } ^ { - } \backslash \{ \mu _ { j } \}$   
<sup>b</sup>9: end while   
10: return $\Gamma  \sum \mathbf { T }$

Note that the minimum and maximum possible flying altitudes influence the computed total deployment delay. As the value of ratio $\frac { h _ { m a x } } { h _ { m i n } }$ (variance of flying altitudes) increases, the total deployment delay increases. Algorithm 4 works in a greedy way based on the wireless coverage radius without considering the UAVs’ diversity in operating altitude and flying speed. It has the advantage of low computational time. However, the gap between its obtained total deployment delay and the optimal one can be large if the variance of operating altitudes or flying speeds is large. To achieve a better performance, we can use the scheme with the pseudo-polynomial time algorithm developed in July 05,2026 at 12:27:12 UTC from IEEE Xplore. Restrictions apply.

Section 5.3, which is designed for a more general setting of the min-sum problem.

## 5.2 Reformulation of Problem (5) and Bound Analysis

We further study the general min-sum problem (5), when UAVs are dispatched from different locations. As in the min-max problem in Section 4.2, here we add the order preserving constraint to make the analysis tractable. The problem is defined as follows:

$$
\begin{array} { r l r } {  { \operatorname* { m i n } _ { \{ y _ { 1 } , \ldots , y _ { n } \} } \sum _ { 1 \leq i \leq n } T _ { i } ( y _ { i } ) , } } \\ & { } & \\ & { } & { \mathrm { s . } t . , \ [ 0 , \beta ] \subseteq \bigcup _ { 1 } ^ { n } [ y _ { i } - r _ { i } , y _ { i } + r _ { i } ] , } \\ & { } & \\ & { } & { \forall 1 \leq i \leq n - 1 , \ y _ { i } \leq y _ { i + 1 } . } \end{array}\tag{}
$$

Note that the last inequality is due to the constraint of initial location order preserving given $x _ { 1 } \leq \cdots \leq x _ { n }$

<sup>1</sup>It is still difficult to solve problem (11) directly even under the constraint of order preserving, since there are still factorial number of combinations in solution. In the previous min-max optimization problem (6), we use feasibility checking algorithm by assigning an identical deadline to all UAVs. However, it can not provide satisfactory solution for problem (11), which targets at minimizing the sum of the deployment delays of selected UAVs in the solution. In spite of this, before presenting the optimal algorithm for problem (11), we claim that we can still apply Algorithm 3 for the new min-sum problem here to find a value $\ddot { \Gamma ^ { \prime } }$ that roughly approximates the optimal total deployment delay $\Gamma ^ { * } . \stackrel { \smile } { \Gamma ^ { \prime } }$ is the summation of all UAVs’ delays obtained by Algorithm $^ { 3 , }$ which aims to minimize the maximum deployment delay. Next, we show the fact that the solution obtained by Algorithm 3 can achieve an nð þ -Þ-approximation for problem (11). Conversely, we can <sup>1</sup>also show that the optimal solution of problem (11) achieves an n-approximation for min-max problem (6).

Lemma 2. $\Gamma ^ { * } \leq \Gamma ^ { \prime } \leq n ( 1 + \epsilon ) \Gamma ^ { * }$ . Conversely, $T ^ { * } \leq T _ { m a x } ^ { * } \leq n T ^ { * }$

Proof. For any instance of problem (11), we have $\begin{array} { r } { \Gamma ^ { * } = \sum _ { 1 \leq i \leq n } { \hat { T } } _ { i } ^ { * } } \end{array}$ , and $T _ { m a x } ^ { * }$ is the maximum one among all $T _ { i } ^ { * \prime } s$ <sup>1</sup>as shown in Table 1. Then, we have $T _ { m a x } ^ { * } \leq \Gamma ^ { * } . \operatorname { A s } T ^ { * }$ is the minimum maximum deployment delay of problem (6), we have $T ^ { * } \le T _ { m a x } ^ { * }$ since the maximum deployment delay in problem (6) is not lower than the maximum deployment delay in problem (11). Since $T$ is obtained by Algorithm 3, the following holds:

$$
\Gamma ^ { \prime } \leq n \cdot T \leq n ( 1 + \epsilon ) T ^ { * } \leq n ( 1 + \epsilon ) T _ { m a x } ^ { * } \leq n ( 1 + \epsilon ) \Gamma ^ { * }
$$

Since $\Gamma ^ { * } \leq \Gamma ^ { \prime }$ , we conclude $\Gamma ^ { * } \leq \Gamma ^ { \prime } \leq n ( 1 + \epsilon ) \Gamma ^ { * }$

Conversely, $T _ { m a x } ^ { * }$ <sup>1</sup>is the maximum deployment delay among all UAVs obtained by the optimal algorithm for problem (11). Then, we have $T _ { m a x } ^ { * } \dot { \leq } \Gamma ^ { * }$ , where G<sup></sup> is the optimal total deployment delay for problem (11). We conclude $\Gamma ^ { * } \leq n \cdot T ^ { * }$ , since the total deployment delay in problem (6) is not lower than the total deployment delay in problem (11). Thus, we obtain $T ^ { * } \leq T _ { m a x } ^ { * } \overset { \cdot } { \leq } n T ^ { * }$ tu

## 5.3 Dynamic Programming for Solving Problem (11)

Different from the min-max optimization problem (6), the feasibility checking algorithm by assigning an identical deadline to all UAVs can not provide satisfactory solution for problem (11). Because problem (11) is to compute the optimal configuration of the UAV network to coordinately minimize the sum of the deployment delays of selected UAVs in the configuration. Given the order $\propto$ defined in Section 4.2, we present a dynamic programming approach for solving the problem (11), which starts with the leftmost point in ½ ;  and sequentially dispatch the UAVs one by <sup>0 b</sup>one according to /.

For the leftmost i UAVs $\mu _ { 1 } , \mu _ { 2 } , \ldots , \mu _ { i }$ and any given delay $j > 0 ,$ , we use $[ 0 , R ( i , j ) ]$ <sup>m2 . . . m</sup>to denote the left-aligned <sup>0 0</sup>interval covered by using only the leftmost i UAVs within total deployment delay $j .$ The initial value of $R ( 0 , j ) = 0$ and $R ( i , 0 ) = 0$ <sup>0 0</sup>. If we want to cover the longest left-aligned <sup>0 0</sup>interval with the leftmost i UAVs $( { \mathrm { i . e . , ~ } } \{ \mu _ { 1 } , \ldots , \mu _ { i } \} )$ and total deployment delay ${ \mathrm { ~ \it ~ { ~ j ~ } ~ } } ,$ <sup>m1 . . . m</sup>then we may or may not use $\mathrm { U A V } \mu _ { i }$ . We are using the following recurrence to capture <sup>m</sup>the idea that either the solution witnessing the left-aligned covered interval $R ( i , j )$ uses $\mu _ { i }$ and how much time t is spent from $j$ in moving $\mu _ { i }$ <sup>m</sup>or else it does not $( R ( i , j ) =$ $\bar { R } ( i - 1 , j ) )$

If we do not use $\mu _ { i } , { \mathrm { ~ i . e . , ~ U A V ~ } } \mu _ { i }$ can not be used to <sup>m m</sup>extend the current left-aligned covered interval within $T _ { i } = t ,$ where t is denoted as the time budget for UAV $\mu _ { i } .$ <sup>m</sup>The longest left-aligned interval can be covered is $R ( i , j ) = \bar { R } ( i - 1 , j )$ . In the other case where we do use $\mu _ { i } ,$ <sup>1 m</sup>the total deployment delay can be divided into two parts, $\mathrm { i . e . , ~ } j - t$ and $t ,$ where t is the delay of UAV $\mu _ { i } ,$ , and $j - t$ is the delay of the remaining $i - 1 \mathrm { U A V s } . t$ <sup>m</sup>is feasible for $\mu _ { i }$ if it allows $\mu _ { i }$ <sup>1</sup>to fly up vertically to $h _ { i }$ <sup>m</sup>at least, i.e., $\left( v _ { i } t \right) ^ { 2 } - h _ { i } ^ { 2 } \geq 0$ <sup>m</sup>. In the following, we use $\Delta _ { ( i , t ) } > 0$ to denote $\left( v _ { i } t \right) ^ { 2 } - h _ { i } ^ { 2 }$ <sup>0</sup>, then $\sqrt { \Delta _ { ( i , t ) } }$ is the horizontal distance that UAV $\mu _ { i }$ can move with delay t. By computing each time budget $t \in \{ 1 , \ldots , j \}$ for moving $\mathrm { U A V } \mu _ { i } ,$ we select the one (best t if <sup>1 . . . m</sup>it exists) that maximizing the left-aligned covered interval by using the leftmost i UAVs $\mu _ { 1 } , \mu _ { 2 } , \ldots , \mu _ { i }$ with total delay $j .$ <sup>m1 m2 . . . m</sup>We have the following three cases that can possibly extend the currently covered left-aligned interval $R ( i - 1 , j - t )$ Þ depending on the relative initial position $x _ { i }$ of $\mu _ { i }$ <sup>1</sup>and $R ( i - 1 , \bar { j } - t )$ . Note that the currently covered left-<sup>m 1</sup>aligned interval can not be extended in the cases that $x _ { i } - r _ { i } - \sqrt { \Delta _ { ( i , t ) } } > R ( i - 1 , j - t )$ and $x _ { i } + r _ { i } + \sqrt { \Delta _ { ( i , t ) } } <$ $R ( i - 1 , j - t )$

Case 1: If $\Delta _ { ( i , t ) } < 0 ,$ , then we do not use UAV $\mu _ { i }$ to <sup>0</sup>cover the target interval. We have $R ( i , j ) = R$ $( i - 1 , j )$ . Otherwise, we have only the following two <sup>1</sup>cases of using $\mathrm { U A V } \mu _ { i }$

Case 2: If $x _ { i } - r _ { i } - \sqrt { \Delta _ { ( i , t ) } } < R ( i - 1 , j - t ) < x _ { i } - r _ { i } ,$ as shown in Fig. $3 , \ \mathrm { U A V } \ \mu _ { i }$ <sup>1</sup>can seamlessly cover from $R ( i - 1 , j - t )$ <sup>m</sup>and the new covered interval can <sup>1</sup>be extended to $R ^ { \prime } = R ( i - 1 , j - t ) + 2 r _ { i }$ . The new position of $\mu _ { i }$ is $( y _ { i } = R ( i - 1 , j - t ) + r _ { i } , h _ { i } )$

Case 3: If $x _ { i } - r _ { i } \le R ( i - 1 , j - t ) < x _ { i } + r _ { i } + \sqrt { \Delta _ { ( i , t ) } } ,$ <sup>1</sup>as shown in Fig. 4, the new covered interval can be extended to $R ^ { \prime } = \mathrm { m i n } \{ x _ { i } + r _ { i } + \sqrt { \Delta _ { ( i , t ) } } , R ( i - 1 $ $j - t ) + 2 r _ { i } \}$ <sup>min</sup>. The new position of $\mu _ { i }$ is $\left( { R ^ { \prime } - r _ { i } , h _ { i } } \right)$

Moreover, if $R ^ { \prime } > R ( i - 1 , j )$ , then $R ( i , j ) = R ^ { \prime }$ . Otherwise, $R ( i , j ) = R ( i - 1 , j ) , \mathrm { ~ i . e , ~ } \mu _ { i }$ will not be used. We can see that $R ( i , j )$ <sup>1 m</sup>is the longest left-aligned interval covered by the leftmost $i \mathrm { U A V }$ within delay j.

Authorized licensed use limited to: Guangxi University. Downloaded on July 05,2026 at 12:27:12 UTC from IEEE Xplore. Restrictions apply.

![](images/ef2c10afdee3301213f64ec761249af8a262032d5b78850f6b46950187709f19.jpg)  
Fig. 3. Case 2: deploying $\mu _ { i }$ to the left to seamlessly cover from $\bar { R ( i - 1 , j - t ) }$ where $\begin{array} { r } { x _ { i } - r _ { i } - \sqrt { \Delta _ { ( i , t ) } } < R ( i - 1 , j - t ) < x _ { i } - r _ { i } . } \end{array}$

The optimal total deployment delay for reaching full coverage of L by using $n \mathrm { U A V s }$ is as follows.

$$
\Gamma ^ { * } = \operatorname* { m i n } _ { \Gamma \geq 0 } \{ \Gamma \mid R ( n , \Gamma ) \geq \beta \} .\tag{}
$$

The dynamic programming is given in Algorithm $5 ,$ where we check the upper bound of G (denoted as $\Gamma _ { u } )$ in problem (11) to help search for the global optimum. For any UAV $\mu _ { i } ,$ the maximum possible moving distance of $\mu _ { i }$ is to <sup>m</sup>reach the furthest position $( 0 , h _ { i } )$ or $( \beta , h _ { i } )$ <sup>m</sup>. Thus, G to sum-<sup>0 b</sup>marize all UAVs is loosely bounded by

$$
\Gamma _ { u } = \sum _ { 1 \leq i \leq n } \left\{ \frac { \operatorname* { m a x } \{ \sqrt { \left( \beta - x _ { i } \right) ^ { 2 } + h _ { i } ^ { 2 } } , \sqrt { x _ { i } ^ { 2 } + h _ { i } ^ { 2 } } \} } { v _ { i } } \right\} .\tag{}
$$

The dynamic programming terminates with a table, whose $( i , j )$ entry records the value of $R ( i , j )$ . Each entry can be computed in constant time. To get the optimal solution, the whole table can be computed in $\ ' { O } ( n \Gamma _ { u } ^ { 2 } )$ time in worst case since $\Gamma \leq \Gamma _ { u } .$ Because $\Gamma _ { u } ^ { - }$ may not be bounded by a polynomial of $n ,$ Algorithm 5 runs in pseudo-polynomial time.

Theorem 4. Algorithm 5 returns the optimum of problem (11) in pseudo-polynomial time.

Proof. We first show that the computed solution of total deployment delay $\Gamma ^ { \prime \prime }$ is feasible. We know that the final locations of UAVs in the computed solution follows order preserving. Moreover, the algorithm does not terminate until $R ( n , { \bar { \Gamma } } ) \geq \beta ,$ then the target interval is fully covered. <sup>b</sup>Thus, the solution of $\Gamma ^ { \prime \prime }$ output by Algorithm 5 is feasible.

It remains to show that $\bar { R } ( i , j )$ is the longest left-aligned interval covered by the leftmost i UAVs within total delay $j .$ Considering the optimal solution for $R ( i , j ) , { \mathrm { U A V } } \ \mu _ { i }$ is <sup>m</sup>either dispatched or not. If not, then we have the same interval $\bar { R ( i - 1 , j ) }$ covered by $\mathrm { U A V s } \mu _ { 1 } , \ldots , \mu _ { i - 1 } .$ Alternatively, $\mathrm { U A V } \mu _ { i }$ is dispatched for $R ( i , j ) = R ( i - 1 , j - t ) +$ $2 r _ { i }$ or $R ( i , j ) = x _ { i } + \bar { r } _ { i } + \sqrt { \Delta _ { ( i , t ) } }$ <sup>1</sup>as Figs. 3 and 4, respec-<sup>2</sup>tively. In each case, $R ( i , j )$ is maximized.

There are three levels of for loops in Line 8 (n loops), Line $9 \ ( \Gamma _ { u } )$ and Line 11 $( \Gamma _ { u } )$ . Thus, Algorithm 5 runs in time $O ( n \Gamma _ { u } ^ { 2 } )$ , which is pseudo-polynomial time. tu

By Lemma 2 and Theorem 4, the Corollary 1 holds.

Corollary 1. Algorithm 5 can also attain an n-approximation for the min-max problem (6).

## 6 PERFORMANCE EVALUATION

In this section, we conduct simulations to evaluate the performances of our proposed UAV deployment algorithms. All the values reported later are collected from the average of 1,000 runs for each algorithm. All UAVs are initially deployed randomly and the width d is set as a small constant. The coverage radius, operating altitude and flying speed are randomly generated, while the length of target interval $L ,$ maximum flying speed, and maximum coverage radius are set to be 20 kilometers (km), 50 km per hour, and 3 km, unless otherwise stated. We set the users’ SNR threshold $\gamma _ { t h }$ to be dB as in [8], which determines the target <sup>g 10</sup>data rate of each ground user (see Section 3).

![](images/e9cb331bfdaa0fd94dccb2ce8f82d49d0cdfcfed70d88f4592a24470a7e6550e.jpg)  
Fig. 4. Case 3: deploying $\mu _ { i }$ to the rightmost position where $x _ { i } - r _ { i } \le R ( i - 1 , j - t ) < x _ { i } + r _ { i } + \sqrt { \Delta _ { ( i , t ) } } .$

```latex
Algorithm 5. Dynamic Programming for Problem (11)
1: Input:
$\mathbf { U } = \{ \mu _ { 1 } , \mu _ { 2 } , \ldots , \mu _ { n } \}$
<sup>m1</sup>2: Output:
$\Gamma ^ { \prime \prime } ;$ total deployment delay
3: for i ¼ to n do
4: for $j = 0$ to $\Gamma _ { u }$ do
5: $R [ i , j ] \gets 0$
6: end for
7: end for
8: for $i = 1$ to $n$ do
<sup>1</sup>9: for j ¼ to $\Gamma _ { u }$ do
10: $R ^ { \prime } \gets 0$
11: <sup>0</sup>for t ¼ to j do
12: if $\Delta _ { ( i , t ) } < 0$ then
13: $R ^ { \prime } \gets R [ i - 1 , j ]$
14: continue;
15: else if $\begin{array} { r } { x _ { i } - r _ { i } - \sqrt { \Delta _ { ( i , t ) } } < R ( i - 1 , j - t ) < x _ { i } - r _ { i } } \end{array}$
then
16: $R ^ { \prime } = R ( i - 1 , j - t ) + 2 r _ { i }$
17: <sup>1 2</sup>y<sub>i</sub> Rði  ; j  tÞ þ r<sub>i</sub>
18: else if $x _ { i } - r _ { i } \le R ( i - 1 , j - t ) < x _ { i } + r _ { i } + \sqrt { \Delta _ { ( i , t ) } }$
then
19: R<sup>0</sup> ¼ $\{ x _ { i } + r _ { i } + \sqrt { \Delta _ { ( i , t ) } } , R ( i - 1 , j - t ) + 2 r _ { i } \}$
20: $y _ { i } \gets R ^ { \prime } - r _ { i }$
21: else
22: $R ^ { \prime } \gets R [ i - 1 , j ]$
23: end if
24: end for
25: $R [ i , j ] \gets \operatorname* { m a x } \{ R [ i - 1 , j ] , R ^ { \prime } \}$
26: end for
27: end for
28: return $\Gamma ^ { \prime \prime } \gets \operatorname* { m i n } \{ j | 1 \leq j \leq \Gamma _ { u } , R ( n , j ) \geq \beta \}$
```

## 6.1 Optimizing Maximum Deployment Delay

In this section, we first present the experimental results for optimizing the maximum deployment delay to dispatch the UAVs in a fair manner.

## 6.1.1 Dispatching of UAVs from the Same Location in Problem (4)

We first present the simulation results of Algorithm 1 when dispatching the UAVs from the same location. Fig. 5 shows July 05,2026 at 12:27:12 UTC from IEEE Xplore. Restrictions apply.

![](images/8082039e37b93566abaa54cc27ade6cbb54dabe4cd19829d591897bc74df7b50.jpg)  
Fig. 5. The optimal deployment delay, the number of UAVs versus r (km) and v (km per hours) of all UAVs.

the optimal deployment delay as a function of the number of UAVs under different mean values of coverage radius $\begin{array} { r } { ( \overline { { r } } = \frac { 1 } { n } \sum _ { i = 1 } ^ { n } r _ { i } ) } \end{array}$ and flying speed $\begin{array} { r } { ( \overline { { v } } = { \frac { 1 } { n } } \sum _ { i = 1 } ^ { n } v _ { i } ) } \end{array}$

<sup>1 1</sup>By increasing v or r, the deployment delay decreases. Note that larger coverage radius (flying speed) of UAVs helps save the moving distance (time) to cover the whole target interval. By increasing the number of UAVs, the deployment delay decreases due to the increased UAV diversity and the flexibility to sample better UAVs. Still, there is a converging trend of the deployment delay with the increase of UAV number. Therefore, depending on the size of the target area and potential size of UAVs, an appropriate number of UAVs needs to be selected and deployed.

## 6.1.2 Dispatching of UAVs from Different Locations in Problem (6)

By running FPTAS in Algorithm 3, we first show the time complexity for solving problem (6). In Fig. 6, we show the running time of our approximation algorithms under different values of -, i.e., 1, 0.1 and 0.01 percent. It is observed that the smaller value of - is, the larger running time is required. In addition, as the number of UAVs increases, the running time is concavely increasing, which is actually much smaller than the theoretical bound $O ( n ^ { 2 } )$ in Theorem 2. This is because as the increase of the number of UAVs n while the length of the line interval is fixed, Algorithm 2 may not need to compute all the UAVs in Line 5.

Fig. 7 shows the difference of the maximum deployment delay between problem (6) and the original problem (4). Actually, it examines the performance loss due to the proposal of preserving UAVs’ initial locations for Algorithm 3.

![](images/45b2b727b0b357f7c0e1d21991dc4d3132002e5d793d3a2fe3082be97ff70e0c.jpg)  
Fig. 6. The running time (in milliseconds) of our approximation algorithms with different values of relative error -.

![](images/89dc5cc168b6484f6198d521baeb69a5201241edc21a353e8355419ff5360454.jpg)  
Fig. 7. The deployment delays obtained by FPTAS for problem (6) and Brute-Force algorithm for original problem (4).

In this figure, problem (6) is solved by our proposed FPTAS by setting $\epsilon = 0 . 1 \%$ and 0.001 percent, while problem (4) is <sup>0 1%</sup>solved optimally by Brute-Force algorithm despite the high complexity. The generated flying speed and coverage radius are uniformly distributed, and the minimum coverage radius is set to be 4 kilometers to guarantee the full coverage. It can be observed that our proposed FPTAS for solving the reformulated problem (6) can obtain a close deployment delay when comparing to the optimal deployment delay (obtained by Brute-Force algorithm for problem (4)). The gap does not necessarily increase with the number of UAVs, as our FPTAS greatly benefits from more UAVs.

## 6.2 Optimizing Total Deployment Delay

In this section, we further present the evaluation on algorithms for efficiently optimizing the total deployment delay for covering the target interval.

## 6.2.1 Dispatching of UAVs from the Same Location in Problem (5)

We present the simulation results of Algorithm 4 when dispatching the UAVs from the same location. In this experiment, we set mean v as 40 km per hour, r as 2.0 kilometer, h as 5.0 kilometer. Fig. 8 shows the optimal the total deployment delay as a function of the number of UAVs under different variances of flying speed ½v and operating altitude $\mathrm { V a r } [ h ]$

<sup>Var</sup>By increasing ½v or ${ \mathrm { V a r } } [ h ]$ , the deployment delay increases, because $\kappa = h _ { m a x } / h _ { m i n }$ and $\tau = v _ { m a x } / v _ { m i n }$ become <sup>k t</sup>larger. This is consistent with Proposition 3. By increasing the number of UAVs, the deployment delay decreases due to the increased UAV diversity and the flexibility to sample more appropriate UAVs. The influence of variance of $h _ { i }$ is relative minor compared to variance of $v _ { i }$ since the final moving distance is determined by both horizontal distance and operating altitude. Still, there is a converging trend of the deployment delay with the increase of UAV number.

![](images/c72f487bfa4335273052e3650c2c9caa9a403eb60c0256af66cb696de8f39242.jpg)  
Fig. 8. The optimal deployment delay versus the number of UAVs versus ½v and ½h of all UAVs.

![](images/c2964860390d8bfa4be54af7a8c4615c84957d5f4231ea3a9f9d71085d3bf42b.jpg)  
Fig. 9. The total deployment delay comparison between Algorithms 3 and 5.

## 6.2.2 Dispatching of UAVs from Different Locations in Problem (11)

Similar to the results in Fig. 7, we can show that Algorithm 5 introduces only small performance loss due to the constraint of preserving UAVs’ initial locations. Next we compare the performance between Algorithm 3 (providing $n ( 1 + \epsilon ) { \cdot }$ -approximation in Lemma 2) and Algorithm 5 (opti-<sup>1</sup>mal for the min-sum problem) for total deployment delay minimization problem (11).

In Fig. 9, problem (11) is solved by both Algorithms 5 and 3 with $\epsilon = 0 . 0 1 \%$ . Since Algorithm 5 provides the optimal <sup>0 01%</sup>solutions for the min-sum design purpose, it always obtains lower total deployment delays than Algorithm 3 (for minmax design purpose) in Fig. 9. However, Algorithm 5 (pseudo-polynomial time) needs more computational time than Algorithm 3 (in $O ( n ^ { 2 } \log \frac { 1 } { \epsilon } ) )$ . By increasing the number <sup>log</sup>of UAVs, the deployment delays obtained by both algorithms decreases due to the UAV diversity gain. Fig. 9 tells that minimizing the maximum deployment delay can imply a significant increase in total deployment delay. However, the empirical performance of Algorithm 3 is better than the worst-case theoretical upper bounds indicated in Lemma 2.

Similarly, in Fig. 10, min-max problem (6) is solved by both Algorithm 5 (n-approximation according to Corollary 1) and Algorithm 3 (providing ð þ -Þ-approximation, $\epsilon = 0 . 0 1 \%$ <sup>1</sup>here in the simulation). We show the performan-<sup>0 01%</sup>ces of Algorithms 3 and 5 in terms of maximum deployment delay. It can be observed that the maximum deployment delay obtained by Algorithm 3 is lower than Algorithm 5. Fig. 10 also tells that minimizing the total deployment delay can imply a significant increase in maximum deployment delay. However in fact, the empirical performance of Algorithm 5 not as bad as the worst-case theoretical upper bound indicated in Corollary 1.

## 7 2D EXTENSION FOR DEPLOYMENT ALGORITHMS

![](images/60d56c35c871201eda91cb58168937593627dd3183a0845d95884de648c2d687.jpg)  
Fig. 10. Comparison between Algorithms 3 and 5 in terms of the maximum deployment delay.

relax our model in two perspectives. One is to relax the initial locations of UAVs, the other is to relax the target area. Due to page limit, we only study the generalized min-max problem and the other generalized min-sum problem can be analyzed similarly.

## 7.1 UAVs are Initially Located in 2D Area

In current model, all UAVs are initially located on a line interval, i.e., x-axis. It can be extended to a 2D area by adding one more dimension of the UAVs’ initial positions, $\mathrm { i . e . , }$ z-axis. Specifically, for each UAV $\mu _ { i } ,$ we use $z _ { i }$ to denote the UAV $\mu _ { i } { ' } s$ <sup>m m</sup>offset along x-axis. Thus, the initial location of the UAV is $( x _ { i } , z _ { i } , 0 )$ , and it will be deployed to $( y _ { i } , 0 , h _ { i } )$ cover the target <sup>0 0</sup>region, as shown in Fig. 11. During the deployment, UAV $\mu _ { i }$ travels an Euclidean distance $\sqrt { \left( y _ { i } - x _ { i } \right) ^ { 2 } + z _ { i } ^ { 2 } + h _ { i } ^ { 2 } }$ at flying speed $v _ { i }$ . Thus, its travel time is given by

$$
T _ { i } ( y _ { i } ) = \frac { \sqrt { \left( y _ { i } - x _ { i } \right) ^ { 2 } + z _ { i } ^ { 2 } + h _ { i } ^ { 2 } } } { v _ { i } } .\tag{}
$$

A particular UAV $\mu _ { i }$ hovering at final position $( y _ { i } , 0 , h _ { i } )$ covers a region $D _ { i }$ <sup>m 0</sup>(Equation (2)) in the target area. It is required that all points of the target area A are covered after the deployment of UAVs, i.e., $\mathbf { A } \subseteq \cup _ { 1 } ^ { n } D _ { i }$ . We only need to change the travel time function $T _ { i } ( y _ { i } )$ <sup>1</sup>in Algorithms 1 and 3 to be as in Equation (14). Both algorithms can be applied directly when all UAVs are initially located in 2D area, and all theories still hold by similar proofs in Proposition 1 and Theorem 2.

![](images/b6aa43abb774eadbf7a28ac05aa3fb84c5370c7c4aa475fd1c08adb9ea4ee90c.jpg)

In this section, we discuss how to extend the proposed algo- <sub>Fig. 11. Adding one dimension of the UAVs’ initial positions, i.e., z-axis.</sub> rithms with theoretical guarantee to 2D. We consider to x-domain and z-domain constitute the 2D ground space. Authorized licensed use limited to: Guangxi University. Downloaded on July 05,2026 at 12:27:12 UTC from IEEE Xplore. Restrictions apply.

![](images/b7cb295b2674f304471006c904a6ed1aa56aba22fd0e9ec77324a954c9e7d54b.jpg)  
Fig. 12. Deploying UAVs to provide full wireless coverage over the rectangular area $\mathbf { \delta A } ,$ where the coverage radius of UAVs is much smaller than the target area.

## 7.2 Both UAVs and Target Area Are in 2D

In this section, we further relax our model to fast deploy diverse UAVs to provide full wireless coverage over a 2D rectangular ground plane $[ 0 , \beta ] \times [ 0 , d ]$

<sup>0 b 0</sup>Recall that both min-max and min-max problems are NPcomplete when the target is line interval in Theorems 1 and 3, thus the general problem of covering a 2D area is also NP-complete. Moreover, to reach a full coverage in the plane by using UAVs’ disk-shaped coverage circles (no longer line segments in the 1D model) is general very difficult to solve [35], because the full coverage problem without any interstices is difficult to be solved by using UAVs’ nonuniform coverage circles. Even if we have a solution for this static circle packing, we cannot use it for our fast UAV deployment problem because we also aim to minimize the travel time during the deployment. Despite the difficulties above, we manage to extend our prior algorithms to 2D area by applying proper approximations.

## 7.2.1 Uniform Coverage Radius

We first look at the case that all UAVs have the same coverage radius, then grid the rectangular area so that each grid square can be covered by a UAV.<sup>4</sup>

As shown in Fig. 12, we want to fast deploy UAVs to provide full wireless coverage over the rectangular area A in Equation (1). A particular $\mathrm { U A V } \mu _ { i }$ operating at final position $( y _ { i } , h _ { i } , z _ { i } ^ { \prime } )$ covers a region A as Equation (15) in the target rectangle. We require a full coverage over a rectangular area A by deploying n diverse UAVs with identical coverage radius r.

$$
\begin{array} { r } { A _ { i } = \Bigg \{ ( w , l ) | z _ { i } ^ { \prime } - \frac { \sqrt { 2 } } { 2 } r _ { i } \leq w \leq z _ { i } ^ { \prime } + \frac { \sqrt { 2 } } { 2 } r _ { i } , } \\ { y _ { i } - \frac { \sqrt { 2 } } { 2 } r _ { i } \leq l \leq y _ { i } + \frac { \sqrt { 2 } } { 2 } r _ { i } \Bigg \} . } \end{array}\tag{}
$$

We first study the min-max problem (4) of covering a 2D area as in Section 4.1, when UAVs are dispatched from the same location, i.e., $, ( x _ { i } = 0 , z _ { i } = 0 )$ for all UAVs. Algorithm 1 <sup>0 0</sup>can be applied directly. Since any UAV with larger distance from the initial location to the target position, it needs a larger travel time. Among all UAVs, we first consider which UAV to send and cover the furthest square of the target area. Specifically, given the current uncovered area, we sequentially select an unassigned UAV $( \mathrm { e . g . , ~ } \mu _ { i } )$ with the <sup>m</sup>minimum travel time to just cover the furthest square on the remaining uncovered area during deployment. We only need to compare each UAV’s travel time to calculate the maximum delay objective.

We further study the min-max problem (6) of covering a 2D area, when UAVs are dispatched from different locations. The new problem can be generalized from problem (6)

$$
\begin{array} { r l } & { \displaystyle \operatorname* { m i n } _ { \{ ( y _ { 1 } , z _ { 1 } ^ { \prime } ) , \ldots , ( y _ { n } , z _ { n } ^ { \prime } ) \} \ 1 \leq i \leq n } T _ { i } ( y _ { i } , z _ { i } ^ { \prime } ) , } \\ & { \displaystyle } \\ & { \mathrm { s . } t . , \textbf { A } \subseteq \bigcup _ { 1 } ^ { n } A _ { i } , } \\ & { \displaystyle \forall \ 1 \leq i \leq n - 1 , \ y _ { i } \leq y _ { i + 1 } , } \\ & { \displaystyle \forall \ 1 \leq i \leq n - 1 , \ z _ { i } ^ { \prime } \leq z _ { i + 1 } ^ { \prime } . } \end{array}\tag{}
$$

Note that the last two inequalities denotes the constraint of initial location order preserving along x-axis and z-axis for possible collision avoidance.

We can decompose the problem (16) into p subproblems, in which each subproblem $P _ { i }$ are given a set of sequential UAVs $\Phi ( t _ { i } , \lambda _ { i } ) = \bar { \{ }  \mu _ { t _ { i } } , \mu _ { t _ { i } + 1 } , \ldots , \mu _ { t _ { i } + \lambda _ { i } - 1 } ^ { - } \}$ , then UAVs in $\Phi ( t _ { i } , \lambda _ { i } )$ are assigned to cover $q$ squares and they are with the same x-coordinate.

By combining Algorithm 6 and binary search (similar to Algorithm 3), we can obtain an FPTAS (2D deployment Algorithm) to solve problem (16).

```latex
Algorithm 6. Feasibility Checking Algorithm for 2D
UAV Deployment
1: Input:
$\mathbf { U } = \{ \mu _ { 1 } , \mu _ { 2 } , \ldots , \mu _ { n } \}$
<sup>m1 m2 . . . m</sup>T : a given deployment delay deadline for all UAVs
2: Output:
$y _ { i } , z _ { i } ^ { \prime } \colon$ final locations of $\mu _ { i }$
3: Compute $\begin{array} { r } { p = \left\lceil \frac { \beta } { \sqrt { 2 } r } \right\rceil } \end{array}$ and $\begin{array} { r } { q = \left\lceil \frac { d } { \sqrt { 2 } r } \right\rceil } \end{array}$
{Calculate the number of UAVs needed to cover the 2D
area.}
4: $t _ { 0 } = 1 , \lambda _ { 0 } = 0$
<sup>0 1 0</sup>5: for i ¼ to $p$ do
6: for $j = q \mathrm { t o } n - t _ { i - 1 } - \lambda _ { i - 1 } - ( p - i ) q \ d$ o
7: <sup>1 1</sup>Apply Algorithm 2 to subproblem $P ( i )$ with
$\Phi \bar { ( } t _ { i - 1 } + \bar { \lambda _ { i - 1 } } , j )$
<sup>1 1</sup>{The remaining UAVs are insufficient to cover the
residual area.}
8: if T is feasible for P ðiÞ then
9: $\lambda _ { i }  j , t _ { i } = t _ { i - 1 } + \lambda _ { i - 1 }$
10: else
11: continue;
12: end if
13: if $j = = n - t _ { i - 1 } - \lambda _ { i - 1 } - ( p - i ) q$ then
14: <sup>1 1</sup>return T is notfeasible for problem (16)
15: end if
16: end for
17: end for
18: return T is feasible for problem (16)
```

![](images/e0c0675cc80b15f92e6f2a2db71a58da1ca51209acf9278a8e63bba65293f91c.jpg)  
Fig. 13. The deployment delays obtained by 2D deployment Algorithm and Brute-Force Algorithm for the min-max problem in 2D area.

Proposition 4. 2D deployment Algorithm runs in $O ( n ^ { 3 } \log { \frac { 1 } { \epsilon } } )$ <sup>log</sup>which can arbitrarily approach the global optimum by assuming the $U A V s ^ { \prime }$ coverage radii are identical.

Proof. Similar to Equations (9) and (10), we can find the lower and upper bounds of the delay T. Then, we use binary search over those feasible deadlines to find the minimum deployment delay $T \leq ( 1 + \epsilon ) T ^ { * }$ as in Section <sup>1</sup>4.2.2. With respect to the time complexity, we can see that there are at most $\textstyle p \cdot { \frac { n } { q } }$ iterations for the for loops, and Algorithm 2 runs in ${ } ^ { \mathsf { ^ { q } } } O ( n ^ { 2 } )$ time. Overall, Algorithm 6 runs in $O ( n ^ { 3 } )$ time, which implies the obtained FPTAS runs in $O ( n ^ { 3 } \log { \frac { 1 } { \epsilon } } )$ tu

## 7.2.2 Different Coverage Radius

Now we look at the general case when UAVs have different coverage radii and extend 2D deployment Algorithm to solve it. As the general case is difficult to solve optimally, we view each UAV’s coverage radius the same (equal to the minimum radius among all UAVs). Then we grid the rectangular target area according to the minimum coverage radius among UAVs. To show the effectiveness of 2D deployment Algorithm for this case, we compare it with the optimal solution obtained by Brute-Force algorithm. In this experiment, we set $\epsilon = 0 . 1 \%$ as in Proposition 4. The 2D <sup>0 1%</sup>area is set as a square with length of 4 km and width of 4 km. The average flying speed is 20 km/hour, and the minimum and mean coverage radius is set to be 1.5 and 2 km to guarantee the full coverage. Fig. 13 shows the Maximum Deployment Delay under 2D deployment Algorithm versus the variance of UAVs’ coverage radius and compares with the optimum obtained by brute-force. We can see that the performance gap between 2D deployment Algorithm and the brute-force algorithm is small especially when the variance of UAV’s coverage radius is small. As 2D deployment Algorithm views all UAVs the same, this gap enlarges as the variance of UAVs’ coverage radius increases. As we have more UAVs or larger N, the maximum delay reduces.

## 8 CONCLUSION

The fast deployment of heterogeneous UAVs to provide wireless coverage is of great practical importance. To the best of our knowledge, this is the first work to deal with the emergency criteria of minimization of the maximum deployment delay and the total deployment delay among all UAVs till covering the whole target area. We prove that both min-max and min-sum problems are NP-complete in general. On one hand, when a number n of diverse UAVs are dispatched from the same location, we present an optimal deployment algorithm of computational complexity $O ( n ^ { 2 } )$ for the min-max problem. When UAVs are in general dispatched from different locations, by preserving UAVs’ location order, we successfully design an FPTAS of computation complexity $\begin{array} { r } { O ( n ^ { 2 } \log { \frac { 1 } { \epsilon } } ) } \end{array}$ . On the other hand, for the <sup>log</sup>min-sum problem when UAVs are dispatched from the same location, we present an approximation algorithm runs in linear time. As for the general case, we further reformulate it as a dynamic program and propose a pseudo polynomial-time algorithm to solve it optimally. The theoretical results draw in this paper are further confirmed by simulation.

The interference among UAVs’ ground user services will be considered in future work, in which UAVs’ coverage radius could be reduced accordingly and we need more UAVs to deploy for full coverage.

## ACKNOWLEDGMENTS

A preliminary version of this paper appeared in the Proceedings of 2017 IEEE Global Communications Conference. This work was supported by the Singapore Ministry of Education Academic Research Fund Tier 2 under Grant MOE2016-T2-1-173.

## REFERENCES

[1] Y. Zeng, R. Zhang, and T. J. Lim, “Wireless communications with unmanned aerial vehicles: Opportunities and challenges,” IEEE Commun. Mag., vol. 54, no. 5, pp. 36–42, May 2016.

[2] “First responders utilize drone for wireless coverage,” [Online]. Available: http://www.unmannedsystemstechnology.com/ 2017/06/first-responders-utilize-drone-wireless-coverage/, Accessed on: Jul. 7, 2017, Unmanned Systems News.

[3] Project loon. [Online]. Available: https://x.company/loon/, Accessed on: Sep. 13, 2017.

[4] X. Liu, H. Zhao, M. Pan, H. Yue, X. Li, and Y. Fang, “Trafficaware multiple mix zone placement for protecting location privacy,” in Proc. IEEE Int. Conf. Comput. Commun., 2012, pp. 972–980.

[5] C. Zhang and W. Zhang, “Spectrum sharing for drone networks,” IEEE J. Sel. Areas Commun., vol. 35, no. 1, pp. 136–144, Jan. 2017.

[6] P. Art, “When cows fly: At&T sending LTE signals from drones,” [Online]. Available: http://about.att.com/innovationblog/ cows\_fly, Accessed on: Apr. 7, 2017.

[7] A. Al-Hourani, S. Kandeepan, and S. Lardner, “Optimal LAP altitude for maximum coverage,” IEEE Wireless Commun. Lett., vol. 3, no. 6, pp. 569–572, Dec. 2014.

[8] M. Mozaffari, W. Saad, M. Bennis, and M. Debbah, “Drone small cells in the clouds: Design, deployment and performance analysis,” in Proc. IEEE Global Commun. Conf., 2015, pp. 1–6.

[9] Y. Zeng and R. Zhang, “Energy-efficient UAV communication with trajectory optimization,” IEEE Trans. Wireless Commun., vol. 16, no. 6, pp. 3747–3760, Jun. 2017.

[10] H. Wang and X. Zhang, “Minimizing the maximum moving cost of interval coverage,” in Proc. Int. Symp. Algorithms Comput., 2015, pp. 188–198.

[11] Y. Pang, Y. Zhang, Y. Gu, M. Pan, Z. Han, and P. Li, “Efficient data collection for wireless rechargeable sensor clusters in harsh terrains using UAVs,” in Proc. IEEE Global Commun. Conf., 2014, pp. 234–239.

[12] M. Pan, P. Li, and Y. Fang, “Cooperative communication aware link scheduling for cognitive vehicular networks,” IEEE J. Sel. Areas Commun., vol. 30, no. 4, pp. 760–768, May 2012.

[13] M. Bedford, “Unmanned Aircraft System (UAS) service demand 2015–2035,” U.S. Department of Transportation, Washington, DC, Tech. Rep. DOT-VNTSC-DoD-13-01, 2013.

[14] M. Mozaffari, W. Saad, M. Bennis, and M. Debbah, “Mobile unmanned aerial vehicles (UAVs) for energy-efficient internet of things communications,” 2017. [Online]. Available: https://arxiv. org/abs/1703.05401

[15] X. Zhang and L. Duan, “Optimization of emergency UAV deployment for providing wireless coverage,” in Proc. IEEE Global Commun. Conf., 2017, pp. 1–6.

[16] X. Xu, L. Duan, and M. Li, “UAV placement games for optimal wireless service provision,” in Proc. 16th Int. Symp. Model. Optimization Mobile Ad Hoc Wireless Netw., 2018, pp. 1–8.

[17] M. M. Azari, Y. Murillo, O. Amin, F. Rosas, M.-S. Alouini, and S. Pollin, “Coverage maximization for a poisson field of drone cells,” 2017. [Online]. Available: https://arxiv.org/abs/1708.06598

[18] K. Li, W. Ni, X. Wang, R. P. Liu, S. S. Kanhere, and S. Jha, “Energyefficient cooperative relaying for unmanned aerial vehicles,” IEEE Trans. Mobile Comput., vol. 15, no. 6, pp. 1377–1386, Jun. 2016.

[19] X. Zhang and L. Duan, “Fast deployment of UAV networks for optimal wireless coverage,” 2017. [Online]. Available: https:// arxiv.org/abs/1710.05616

[20] Q. Wu, Y. Zeng, and R. Zhang, “Joint trajectory and communication design for multi-UAV enabled wireless networks," 2017. [Online]. Available: https://arxiv.org/abs/1705.02723

[21] C. Di Franco and G. Buttazzo, “Energy-aware coverage path planning of UAVs,” in Proc. IEEE Int. Conf. Auton. Robot Syst. Competitions, 2015, pp. 111–117.

[22] D. Orfanus, E. P. de Freitas, and F. Eliassen, “Self-organization as a supporting paradigm for military UAV relay networks,” IEEE Commun. Lett., vol. 20, no. 4, pp. 804–807, Apr. 2016.

[23] M. Alzenad, A. El-Keyi, and H. Yanikomeroglu, “3D placement of an unmanned aerial vehicle base station for maximum coverage of users with different QoS requirements,” IEEE Wireless Commun. Lett., vol. 7, no. 1, pp. 38–41, Feb. 2018.

[24] M. Mozaffari, W. Saad, M. Bennis, and M. Debbah, “Efficient deployment of multiple unmanned aerial vehicles for optimal wireless coverage,” IEEE Commun. Lett., vol. 20, no. 8, pp. 1647– 1650, Aug. 2016.

[25] R. Benkoczi, D. Gaur, and M. Thom, “A 2-approximation algorithm for barrier coverage by weighted non-uniform sensors on a line,” in Proc. Int. Symp. Algorithms Experiments Sensor Syst. Wireless Netw. Distrib. Robot., 2016, pp. 95–111.

[26] M. Mozaffari, W. Saad, M. Bennis, and M. Debbah, “Unmanned aerial vehicle with underlaid device-to-device communications: Performance and tradeoffs,” IEEE Trans. Wireless Commun., vol. 15, no. 6, pp. 3949–3963, Jun. 2016.

[27] P. Zhan, K. Yu, and A. L. Swindlehurst, “Wireless relay communications with unmanned aerial vehicles: Performance and optimization,” IEEE Trans. Aerosp. Electron. Syst., vol. 47, no. 3, pp. 2068–2085, Jul. 2011.

[28] M. M. Azari, F. Rosas, K.-C. Chen, and S. Pollin, “Ultra reliable UAV communication using altitude and cooperation diversity,” 2017. [Online]. Available: https://arxiv.org/abs/1705.02877

[29] M. J. Henchey, R. Batta, M. Karwan, and A. Crassidis, “A flight time approximation model for unmanned aerial vehicles,” in Operations Research for Unmanned Systems. Hoboken, NJ, USA: Wiley, 2016, pp. 95–117.

[30] H. Fan, V. Lee, M. Li, X. Zhang, and Y. Zhao, “Barrier coverage using sensors with offsets,” in Proc. 9th Int. Conf. Wireless Algorithms Syst. Appl., 2014, pp. 389–400.

[31] J. Lyu, Y. Zeng, and R. Zhang, “Cyclical multiple access in UAVaided communications: A throughput-delay tradeoff,” IEEE Wireless Commun. Lett., vol. 5, no. 6, pp. 600–603, Dec. 2016.

[32] V. C. Lee, H. Wang, and X. Zhang, “Minimizing the maximum moving cost of interval coverage,” Int. J. Comput. Geom. Appl., vol. 27, no. 03, pp. 187–205, 2017.

[33] M. Garey and D. Johnson, Computers and Intractability. New York, NY, USA: W. H. Freeman, 2002, vol. 29.

[34] I. Mahjri, A. Dhraief, A. Belghith, and A. AlMogren, “SLIDE: A straight line conflict detection and alerting algorithm for multiple unmanned aerial vehicles,” IEEE Trans. Mobile Comput., vol. 17, no. 5, pp. 1190–1203, May 2018.

[35] K. Stephenson, Introduction to Circle Packing: The Theory of Discrete Analytic Functions. Cambridge, U.K.: Cambridge University Press, 2005.

![](images/08f53df170f72b8ca3a7dbfc31c437bb23d946f7da4f40bdf8a0b91369301715.jpg)

Xiao Zhang received the BEng and MEng degrees from the South-Central University for Nationalities, Wuhan, China, in 2009 and 2011, respectively, and the PhD degree from the Department of Computer Science, City University of Hong Kong, Hong Kong, 2016. In 2015, he was a visiting scholar with Utah State University, Utah. He is currently a postdoctoral research fellow with the Engineering Systems and Design Pillar, Singapore University of Technology and Design. His research interests include algorithms design

and analysis, combinatorial optimization, wireless, and UAV networking He is a member of the IEEE

![](images/145c0176e2526c20baf837a19610cd343ede48063c169577b65771cfae94d5b4.jpg)

Lingjie Duan (S’09-M’12-SM’16) received the PhD degree from the Chinese University of Hong Kong, in 2012. In 2011, he was a visiting scholar with the University of California, Berkeley, CA. He is currently an assistant professor with the Engineering Systems and Design Pillar, Singapore University of Technology and Design, Singapore. His current research interests include network economics and game theory, cognitive and cooperative communications, energy harvesting wireless communications, and mobile crowdsourcing.

He is an editor of the IEEE Transactions on Wireless Communications and the IEEE Communications Surveys and Tutorials. In 2016, he was a guest editor of the IEEE Journal on Selected Areas in Communications’ special issue on human-in-the-loop mobile networks, and was also a guest editor of the IEEE Wireless Communications Magazine for feature topic of sustainable green networking and computing in 5G systems. He was a recipient of the 2016 SUTD Excellence in Research Award, the 10th IEEE ComSoc Asia-Pacific Outstanding Young Researcher Award in 2015, and the Hong Kong Young Scientist Award (Finalist in Engineering Science track), in 2014. He is a senior member of the IEEE.

" For more information on this or any other computing topic, please visit our Digital Library at www.computer.org/publications/dlib.