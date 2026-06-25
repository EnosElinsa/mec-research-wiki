# Drone Small Cells in the Clouds: Design, Deployment and Performance Analysis

Mohammad Mozaffari1, Walid Saad1, Mehdi Bennis2, and Merouane Debbah3

1 Wireless@VT, Electrical and Computer Engineering Department, Virginia Tech, VA, USA, Emails: {mmozaff,walids}@vt.deu

2 CWC - Centre for Wireless Communications, Oulu, Finland, Email: bennis@ee.oulu.fi

3 Mathematical and Algorithmic Sciences Lab, Huawei France R & D, Paris, France, Email:merouane.debbah@huawei.com

Abstract—The use of drone small cells (DSCs) which are aerial wireless base stations that can be mounted on flying devices such as unmanned aerial vehicles (UAVs), is emerging as an effective technique for providing wireless services to ground users in a variety of scenarios. The efficient deployment of such DSCs while optimizing the covered area is one of the key design challenges. In this paper, considering the low altitude platform (LAP), the downlink coverage performance of DSCs is investigated. The optimal DSC altitude which leads to a maximum ground coverage and minimum required transmit power for a single DSC is derived. Furthermore, the problem of providing a maximum coverage for a certain geographical area using two DSCs is investigated in two scenarios; interference free and full interference between DSCs. The impact of the distance between DSCs on the coverage area is studied and the optimal distance between DSCs resulting in maximum coverage is derived. Numerical results verify our analytical results on the existence of optimal DSCs altitude/separation distance and provide insights on the optimal deployment of DSCs to supplement wireless network coverage.

## I. INTRODUCTION

Recently, using aerial base stations to support ground cellular networks has received significant attention. Particularly, drone small cells (DSCs) can act as aerial base stations to support cellular networks in high demand and overloaded situations, or for the purpose of public safety and disaster management [1]. The main advantage of using DSCs is that they do not need to have an actual pilot and hence they can be autonomously deployed in dangerous environments for the purpose of search, rescue and communication. Furthermore, since DSCs are essentially mobile base stations, they are more robust against environmental changes as compared to fixed ground base stations. For example, in disaster situations such as earthquakes or floods where some of ground base stations are damaged, or during big public events such as Olympic Games where a huge demand for communication is observed, the cellular network needs to be assisted to provide the needed capacity and coverage [1]. In these cases, deploying DSCs acting as base stations is extremely useful in providing an improved quality-of-service (QoS) for ground users. The deployment of DSCs faces many challenges such as power consumption, coverage optimization and interference management [2].

To address some of these challenges, the authors in [2] provided a general view of practical considerations for the integration of DSCs with cellular networks. The work in [3], considered the use of DSCs to compensate for the cell overload

This research was supported by the U.S. National Science Foundation under Grant AST-1506297.

and outage in cellular networks. However, in this body of work there is no extensive discussion on the coverage performance of DSCs and deployment methods. Due to the special application of DSCs in unexpected events such as disaster, rapid and efficient deployment of DSCs is mandatory to provide a maximum coverage service for ground users. DSCs can be deployed in a high altitude platform (HAP) which is above 10 km height or in low altitude platform (LAP) with the altitude of below 10 km [4]. In [5] the optimal deployment/movement of DSCs in order to improve the connectivity of wireless ad-hoc networks was studied. In [6], considering static ground users, the optimum trajectory and heading of DSCs equipped with multiple antennas for ground to air uplink scenario was investigated.

Beyond deployment, another important challenge for mobile DSC base stations is channel modeling. For instance, in [7], the probability of line of sight (LOS) for air to ground communication as a function of elevation angle and average height of buildings in a dense urban area was determined. The air to ground path loss model has been presented in [8], [9]. As discussed in [9] , due to path loss and shadowing effects of obstacles, the characteristics of the air to ground channel depend on the height of the aerial base stations. By increasing the altitude of a DSC, the path loss increases, however, shadowing effect decreases and the possibility of having LOS connections between ground users and DSCs increases. Therefore, an optimum altitude for the aerial base station which results in a maximum coverage exists. In [10], assuming only one DSC operating with no inter-cell interference, the optimum altitude for the DSC which leads to a maximum coverage was derived. However, the authors did not consider the case of multiple DSCs where beyond altitude, the distance between DSCs also impacts the overall coverage performance. The problem of multiple DSC deployment becomes even more challenging when interference occurs between the received signal from different DSCs. The impact of interference on the coverage performance of DSC has not been investigated in prior studies.

The main contribution of this paper is to develop fundamental results on the coverage and optimal deployment of wireless DSCs. First, we analyze the optimal height for a DSC for which the required transmit power for covering a target area is minimized. Next, to achieve the maximum coverage performance for a specified area, the optimal deployment of two DSCs in both interference and interference-free situations is studied. The goal is to maximize the coverage performance of DSCs by calculating optimal values for DSCs altitude and the distance between them. To this end, we consider a target area with a specific size and for a single static DSC and we find the optimum altitude ensuring sufficient coverage using minimum transmit power. Next, with the goal of offering maximum coverage for the target area the optimal deployment of two DSCs over the area is investigated. Numerical evaluations are then used to validate the derived analytical results.

The rest of this paper is organized as follows: Section II presents the system model describing the air to ground channel model. In Section III, coverage performance of a single DSC and multiple DSCs is investigated. In Section IV, we present the numerical results. Finally, Section V concludes the paper.

## II. SYSTEM MODEL AND THE SINGLE DSC CASE

Consider a static DSC located at an altitude of h meters transmitting signals to static users on the ground. In order to analyze the coverage of such a DSC, it is imperative to adopt an appropriate path loss model that is suitable for air to ground communication. In this section after presenting the air to ground channel model, the optimal altitude for a single DSC case is derived.

## A. Air to Ground Channel Model

As discussed in [4] and [11], the ground receiver receives three groups of signals including LOS, strong reflected signals (NLOS) and multiple reflected components which cause multipath fading. These groups can be considered separately with different probabilities of occurrence. Typical, as discussed in [8], it is assumed that the received signal is categorized only in one of the mentioned groups. Each group has a specific probability of occurrence which is a function of environment, density and height of buildings and elevation angle. The probability of receiving LOS and strong NLOS components are significantly higher than fading [8]. Therefore, the impact of small scale fading can be neglected. A common approach to model air to ground propagation channel is to consider LOS and NLOS components along with their occurrence probabilities separately. Note that for NLOS connections due to the shadowing effect and reflection of signals from obstacles, path loss is higher than LOS. Hence, in addition to the free space propagation loss, different excessive path loss values are assigned to LOS and NLOS links.

Figure 1 shows a DSC located at an altitude of h and ground users at the radius of R from a point corresponding to the projection of DSC onto the ground. The distance between the DSC and the ground receiver is $d \ = \ { \sqrt { R ^ { 2 } + h ^ { 2 } } }$ and $\theta = \tan ^ { - 1 } ( h / R )$ = +indicates the elevation angle (in radian) DSC = tan ( )with respect to the user.

The path loss for LOS and NLOS connections are [4]:

$$
L _ {\mathrm{LoS}} (d B) = 2 0 \log (\frac {4 \pi f _ {c} d}{c}) + \xi_ {\mathrm{LoS}}, \tag {1}
$$

$$
L _ {\mathrm{NLoS}} (d B) = 2 0 \log (\frac {4 \pi f _ {c} d}{c}) + \xi_ {\mathrm{NLoS}}, \tag {2}
$$

where $L _ { \mathrm { L o S } }$ and $L _ { \mathrm { N L o S } }$ are the average path loss for LOS and NLOS links, $\xi _ { \mathrm { L o S } }$ and $\xi _ { \mathrm { N L o S } }$ are the average additional loss to the free space propagation loss which depend on the environment, c is the speed of light, $f _ { \mathrm { c } }$ is the carrier frequency and d is the distance between the DSC and ground receiver.

![](images/767e1d4efe26c533c411b98ebe59f941921be9d74d63317e11e7c2985443db18.jpg)

<details>
<summary>text_image</summary>

DSC
d
h
θ
R
</details>

Fig. 1: Low altitude platform.

The probability of having LOS connections at an elevation angle of θ is given by [10]

$$
\mathrm{P} (\mathrm{LOS}) = \frac {1}{1 + \alpha \exp (- \beta \left[ \frac {1 8 0}{\pi} \theta - \alpha \right])}, \tag {3}
$$

where α and $\beta$ are constant values which depend on the environment (rural, urban, dense urban, etc.). Also, probability of NLOS is P NLOS −P LOS . Equation (3) indicates that ( ) = 1 ( )the probability of having LOS connection between the aerial base station and to ground users is an increasing function of elevation angle. In other words, by increasing the elevation angle between the receiver and transmitter, the shadowing effect decreases and clear LOS path exists with high probability. Finally, the average path loss as a function of the DSC altitude and coverage radius becomes

$$
\overline {{{L}}} (R, h) = \mathrm{P} (\mathrm{LoS}) \times L _ {\mathrm{LoS}} + \mathrm{P} (\mathrm{NLOS}) \times L _ {\mathrm{NLoS}}. \tag {4}
$$

## B. Optimal Altitude for Single DSC

Given this channel model, our first goal is to study the problem of optimal altitude for a single DSC seeking maximum ground coverage. Consider a DSC transmitting its signal with the power of $P _ { \mathrm { t } } ,$ , then the received power is written as

$$
P _ {\mathrm{r}} (d B) = P _ {\mathrm{t}} - \overline {{{L}}} (R, h). \tag {5}
$$

A point on the ground is covered by the DSC if its signal to noise ratio (SNR) is greater than a threshold $( \gamma _ { \mathrm { t h } } \ )$ . That is

$$
\gamma (R, h) = \frac {P _ {\mathrm{r}}}{N} \geqslant \gamma_ {\mathrm{th}}, \tag {6}
$$

where N is the noise power. Obviously, to find the maximum achievable coverage radius we should have $\gamma ( R , h ) = \gamma _ { \mathrm { t h } }$ . For ( ) =a fixed transmit power, the optimal DSC height which results in maximum coverage is computed by solving the following equation [8]:

$$
\frac {1 8 0 (\xi_ {\mathrm{NLoS}} - \xi_ {\mathrm{LoS}}) \beta Z}{\pi (Z + 1) ^ {2}} - \frac {2 0 \mu}{\log (1 0)} = 0, \tag {7}
$$

where $Z = \alpha \exp ( - \beta \left\lceil \frac { 1 8 0 } { \pi } \mathrm { t a n } ^ { - 1 } ( \mu ) - \alpha \right\rceil )$ and $\mu = h / R .$ By =solving (7), $\mu _ { \mathrm { o p t } } = h _ { \mathrm { o p t } } / R _ { \mathrm { m a x } }$ ( ) ) =is computed and using (5), $h _ { \mathrm { o p t } }$ and $R _ { \mathrm { m a x } }$ =are found.

Note that due to the limitation on the altitude of DSCs, we have $h \leqslant h _ { \operatorname* { m a x } } .$ , where $h _ { \mathrm { m a x } }$ is the maximum allowable altitude for DSCs. It can be shown that using the typical values for the parameters in (4) and (3), $\begin{array} { r } { \frac { \partial ^ { 2 } h } { \partial ^ { 2 } R } < \bar { 0 } } \end{array}$ which implies that R as 0a function of h is a concave function. Therefore, the coverage range increases as the altitude increases up to the optimal point and after that it decreases. As a result, considering a constraint on the maximum allowable altitude, the feasible optimal altitude is equal to $\hat { h } _ { \mathrm { o p t } } ~ = ~ \operatorname* { m i n } \{ h _ { \mathrm { m a x } } , h _ { \mathrm { o p t } } \}$ . Now, assume that the =target area which should be covered is fixed with radius of $R _ { \mathrm { c } }$ and the goal is to find the an optimal altitude where the minimum transmit power is required to cover the target area. The derivative of transmit power with respect to the altitude is:

$$
\partial P _ {\mathrm{t}} / \partial h = \partial \overline {{L}} (R _ {\mathrm{c}}, h) / \partial h = 0 \rightarrow h _ {\mathrm{opt}} = \mu_ {\mathrm{opt}} R _ {\mathrm{c}}. \tag {8}
$$

Finally, considering the feasible optimal altitude, the minimum required transmit power will be

$$
P _ {\mathrm{t,min}} (d B) = \overline {{L}} (R _ {\mathrm{c}}, \hat {h} _ {\mathrm{opt}}) + \gamma_ {\mathrm{th}} N. \tag {9}
$$

Now, we prove that R as a function of h does not have more than one local maximum. In other words, if a local maximum exists, the corresponding h is the optimal altitude. Clearly, if a DSC is deployed at the optimal altitude, it provides a maximum SNR for any ground users. This is equivalent to have a minimum path loss for the users. Consider a ground user located at the radius of $R _ { o }$ from a point corresponding to the projection of a DSC onto to the ground. The average path loss at the user location as a function of elevation angle can be written as:

$$
\overline {{{L}}} (\theta) = \frac {\left(\xi_ {\mathrm{LoS}} - \xi_ {\mathrm{NLoS}}\right)}{1 + \alpha \exp \left(- \beta \left[ \frac {1 8 0}{\pi} \theta - \alpha \right]\right)} \tag {10}
$$

$$
- 2 0 \log (R _ {o} c o s (\theta)) + 2 0 \log (\frac {4 \pi f _ {c} d}{c}).
$$

Since altitude and elevation angle are directly related, the optimal altitude corresponds to the optimal elevation angle. To show that the number of local minimum path loss as a function of elevation angle is not greater than one, we should have:

Proposition 1. If a local minima exists in the path loss function, then it is the only local minima of the function.

Proof:

we have to show if $\frac { \partial \overline { { { \cal L } } } ( \theta ) } { \partial \theta } > 0  \frac { \partial ^ { 2 } \overline { { { \cal L } } } ( \theta ) } { \partial \theta ^ { 2 } } > 0 .$

$$
\frac {\partial \overline {{L}} (\theta)}{\partial \theta} = \frac {\frac {1 8 0}{\pi} \beta (\xi_ {\mathrm{NLoS}} - \xi_ {\mathrm{LoS}}) Z}{(1 + Z) ^ {2}} + \tan (\theta)
$$

$$
\frac {\partial \overline {{L}} (\theta)}{\partial \theta} > 0 \rightarrow \tan (\theta) > \frac {\frac {1 8 0}{\pi} \beta (\xi_ {\mathrm{NLoS}} - \xi_ {\mathrm{LoS}}) Z}{(1 + Z) ^ {2}},
$$

$$
\begin{array}{l} [ \tan (\theta) ] ^ {2} > \frac {\left[ \frac {1 8 0}{\pi} \beta (\xi_ {\mathrm{LoS}} - \xi_ {\mathrm{NLoS}}) Z \right] ^ {2}}{(1 + Z) ^ {4}} \\ = \frac {\left[ \frac {1 8 0}{\pi} \beta \right] ^ {2} \left(\xi_ {\mathrm{LoS}} - \xi_ {\mathrm{NLoS}}\right) Z ^ {3}}{(1 + Z) ^ {4}} \times \frac {\left(\xi_ {\mathrm{LoS}} - \xi_ {\mathrm{NLoS}}\right)}{Z} \\ \end{array}
$$

$$
\stackrel {(a)} {>} \frac {\left[ \frac {1 8 0}{\pi} \beta \right] ^ {2} (\xi_ {\mathrm{LoS}} - \xi_ {\mathrm{NLoS}}) Z ^ {3}}{(1 + Z) ^ {4}},
$$

Finally,

$$
\frac {\partial^ {2} \overline {{L}} (\theta)}{\partial \theta^ {2}} = \frac {- \left[ \frac {1 8 0}{\pi} \beta \right] ^ {2} (\xi_ {\mathrm{LoS}} - \xi_ {\mathrm{NLoS}}) (Z ^ {3} - Z)}{(1 + Z) ^ {4}} + \tan^ {2} (\theta) + 1 > 0,
$$

where $Z = \alpha \exp ( - \beta \left[ \theta - \alpha \right] )$ and (a) is based on $\left( \xi _ { \mathrm { L o S } } - \xi _ { \mathrm { N L o S } } \right) > Z$ ( [ ])which is hold for the typical values related ( )to urban environments and elevation angles greater than 5 degree.

Now, assume $\theta = \theta _ { o }$ is a local minimum, then,

$$
\left. \frac {\partial \overline {{L}} (\theta)}{\partial \theta} \right| _ {\theta = \theta_ {o} ^ {+}} > 0 \rightarrow \text { for } \theta > \theta_ {o} \text { we   have } \frac {\partial^ {2} \overline {{L}} (\theta)}{\partial \theta^ {2}} > 0.
$$

Hence, $\theta = \theta _ { o }$ is the only local minimum and is the optimal =elevation angle.

Knowing that the path loss as a function of altitude has only one local minima, the optimal altitude can be found by increasing the DSC altitude up to a point where the path loss starts increasing.

## III. CASE OF TWO NON-INTERFERING DSCS

Here, assuming that two DSCs are operating together in a given area, the optimal distance between them in both interference and interference-free situations is analyzed.

## A. Two DSCs in interference free situations

Next, we consider two DSCs that are used to provide coverage for a target area. Here, without loss of generality, we consider the target area to be a rectangle whose length is given by a and whose width is given by b. To have maximum coverage for this target area, optimal values for DSCs altitude and distance should be determined. Intuitively, for a given target area in the absence of interference between the two DSCs, the maximum overall coverage is obtained if the effective coverage inside the target area provided by each DSC is maximized while the overlap between the coverages of DSCs is minimum. These conditions are satisfied if each DSC is at its optimal altitude and they are separated as far as possible but they should not cover outside the target area. In general, the DSCs can be deployed in different altitude and they might use a different transmit power. As a result, they can provide a different coverage radius.

Figure 2 shows the coverage of two DSCs located at their optimal altitudes, D is the distance between DSCs, $R _ { 1 } ^ { \mathrm { m a x } }$ and $R _ { 2 } ^ { \mathrm { m a x } }$ and second DSC, and $O ( x , y )$ is the origin of coverage area with ( )respect to the center of target area. The optimal deployment of two DSCs in the absence of interference can be determined by the following set of equations:

$$
\left\{ \begin{array}{l} h _ {1} = \hat {h} _ {1} ^ {\text { opt }}, \\ h _ {2} = \hat {h} _ {2} ^ {\text { opt }}, \\ (x _ {1}, y _ {1}) = (\frac {- a}{2} + R _ {1} ^ {\max}, \frac {- b}{2} + R _ {1} ^ {\max}), \\ (x _ {2}, y _ {2}) = (\frac {a}{2} - R _ {2} ^ {\max}, \frac {b}{2} - R _ {2} ^ {\max}), \end{array} \right. \tag {11}
$$

where $\hat { h } _ { 1 } ^ { \mathrm { { o p t } } }$ and $\hat { h } _ { 2 } ^ { \mathrm { { o p t } } }$ are the optimal feasible altitude for $\mathrm { D S C _ { 1 } }$ and DSC2. (11) is found by placing the coverage areas as separate as possible and the tangent to the borders of target area. Note that in this case the target area is larger than the coverage region of UAVs and as a result the coverage regions will be located inside the target area. By using some geometric properties for calculating the total area of intersecting circles, the maximum overall coverage area can be expressed as follows:

![](images/a118f3b871c61fc54535a3fa05500c7ba6a849d2c68becf2b7b935edd014eacd.jpg)

<details>
<summary>text_image</summary>

b
D
O(x₁,y₁)
R₁max
O(x₂,y₂)
R₂max
a
</details>

Fig. 2: Optimal deployment of two DSCs in the absence of interference.

If the two coverage areas overlap $( D \leqslant R _ { 1 } ^ { \mathrm { m a x } } + R _ { 2 } ^ { \mathrm { m a x } } )$ ,

$$
\begin{array}{l} A _ {\mathrm{C}} ^ {\max} = \pi \left[ (R _ {1} ^ {\max}) ^ {2} + (R _ {2} ^ {\max}) ^ {2} \right] \\ - (R _ {1} ^ {\max}) ^ {2} \cos^ {- 1} \left[ \frac {D ^ {2} + (R _ {1} ^ {\max}) ^ {2} - (R _ {2} ^ {\max}) ^ {2}}{2 D R _ {1} ^ {\max}} \right] \\ - \left(R _ {2} ^ {\max}\right) ^ {2} \cos^ {- 1} \left[ \frac {D ^ {2} + \left(R _ {2} ^ {\max}\right) ^ {2} - \left(R _ {1} ^ {\max}\right) ^ {2}}{2 D R _ {2} ^ {\max}} \right] + B, \tag {12} \\ \end{array}
$$

where

$$
B = \sqrt {(- D + R _ {1} ^ {\mathrm{max}} + R _ {2} ^ {\mathrm{max}}) (D - R _ {1} ^ {\mathrm{max}} + R _ {2} ^ {\mathrm{max}})}
$$

$$
\times \sqrt {(D + R _ {1} ^ {\max} - R _ {2} ^ {\max}) (D + R _ {1} ^ {\max} + R _ {2} ^ {\max})}.
$$

For the special case where the two DSCs are identical, located at the same altitude and use the same transmit power, they have the same coverage radius $( R _ { 1 } ^ { \mathrm { m a x } } = R _ { 2 } ^ { \mathrm { m a x } } = R ^ { \mathrm { m a x } } )$ . Then (13) is reduced to

$$
\begin{array}{l} A _ {C} ^ {\max} = 2 \pi (R ^ {\max}) ^ {2} - 2 (R ^ {\max}) ^ {2} \cos^ {- 1} \left(\frac {D}{2 R ^ {\max}}\right) \tag {13} \\ + \frac {D}{2} \sqrt {4 (R ^ {\mathrm{max}}) ^ {2} - D ^ {2}}, \\ \end{array}
$$

If $D \ > \ R _ { 1 } ^ { \mathrm { m a x } } + R _ { 2 } ^ { \mathrm { m a x } }$ , they do not overlap and the total coverage area is given by

$$
A _ {C} ^ {\max} = \pi \left[ (R _ {1} ^ {\max}) ^ {2} + (R _ {2} ^ {\max}) ^ {2} \right]. \tag {14}
$$

## B. Case of Two Interfering DSCs

Next, we consider a case in which the two DSCs interfere with each other during the transmission. This situation happens when DSCs are not controlled by the same control system so they might use the same transmit channel. Also, due to the limited number of available channels in a wireless network, the DSCs might transmit over the same channel resulting in interference.

Consider a given target area which should be covered by two DSCs. Clearly, the distance should not be too large to avoid covering unwanted area (outside the target area), and it should not be too small due to the high interference effect. Therefore, an optimum distance between DSCs which results in the highest coverage exists. Figure 3 illustrates two DSCs separated by D. Consider a ground user at the radius of $R _ { 1 }$ and $R _ { 1 }$ from the projection of $\mathrm { D S C _ { 1 } }$ and $\mathrm { D S C } _ { 2 }$ onto the ground. φ is the angle between $\vec { R } _ { 1 }$ and $\vec { D } .$ . In this case, a point on the ground is covered by a DSC if the signal to interference plus noise ratio (SINR) be greater than γth. Thus

![](images/994d0e21047ee19e00f73718d45372193e461f470825e250c5e96de6e0da2f5e.jpg)

<details>
<summary>text_image</summary>

DSC₁
h₁
d₁
Ground User
R₁
φ
R₂
D
h₂
DSC₂
</details>

Fig. 3: Two DSCs interfering scenario.

$$
\gamma (R _ {1}, R _ {2}, h _ {1}, h _ {2}) = \frac {P _ {\mathrm{r} , 1}}{N + P _ {\mathrm{r} , 2}} \geqslant \gamma_ {\mathrm{th}}, \tag {15}
$$

where $P _ { \mathrm { r } , 1 }$ and $P _ { \mathrm { r } , 2 }$ are the received power from the first and second DSCs.

Given that ${ R _ { 2 } } ^ { 2 } = { R _ { 1 } } ^ { 2 } + { D } ^ { 2 } - 2 { R _ { 1 } } { D } \cos ( \phi )$ , and assuming = + 2 cthat the DSCs have the same altitude of $h ,$ ( ) the SINR can be rewritten as

$$
\gamma (R _ {1}, D, \phi) = \frac {P _ {r , 1}}{P _ {r , 2} + N} \geqslant \gamma_ {\mathrm{th}}. \tag {16}
$$

Obviously, for given D and $R _ { 1 }$ values, a specific range for φ which satisfies the above inequality, is obtained. That is, for $D = D _ { o }$ and $R = R _ { o } { \mathrm { ~ } }$ , the positive coverage angle range is $\phi _ { \mathrm { m a x } } \leqslant$ =π. Note that since the target area is limited, the effective coverage angle is inside the target area. Hence, the upper bound of $\phi$ is not necessarily π and is replaced by $\phi _ { \mathrm { m a x } }$ . Assume that the maximum coverage for a DSC in the absence of interference is $R _ { \mathrm { m } }$ . Without loss of generality, we fix the location for $\mathrm { D S C } _ { 2 }$ at $\begin{array} { r } { x _ { 2 } = \mathrm { ~ \frac { \it ~ a ~ } { ~ 2 ~ } ~ } - \mathrm { ~ \it ~ R _ { m } ~ } } \end{array}$ . In addition, for simplicity, we assume that =DSCs altitude and their transmit power are fixed and identical and the only parameter that can change is the distance between DSCs. The goal is to find the optimal distance between two DSCs which leads to the maximum overall coverage inside the target area. Note that we fix the position of one DSC over the target area and then deploy the other DSC within distance D from the first one. The total coverage area is expressed as:

$$
\begin{array}{l} A _ {C} = A _ {\mathrm{C}, 1} + A _ {\mathrm{C}, 2} = 2. \int_ {R = 0} ^ {R _ {m}} \int_ {\phi = \phi_ {\min} (R)} ^ {\phi = \phi_ {\max} (R)} R. d R d \phi \tag {17} \\ + 2. \int_ {R = 0} ^ {R _ {m}} \int_ {\phi = \phi_ {m i n} (R)} ^ {\phi = \pi} R. d R d \phi , \\ \end{array}
$$

where $A _ { \mathrm { C } , 1 }$ and $A _ { \mathrm { C } , 2 }$ are the effective coverage inside the target area provided by $\mathrm { D S C _ { 1 } }$ and $\mathrm { D S C } _ { 2 }$ . It can be shown that for $\phi _ { \mathrm { m a x } }$ DSC1 that might partially cover outside the target area is computed as follows:

$$
\phi_ {\max} (R) = \cos^ {- 1} (\max \{- 1, \frac {D + R _ {\mathrm{m}} - a}{R} \}). \tag {18}
$$

Finally, the optimal distance between DSCs is

$$
D _ {\text { opt }} = \underset {D} {\arg \max} \{A _ {C} (D) \}. \tag {19}
$$

Note that although most of the analytical results shown in the previous sections have closed form expressions, in the case of two fully interfering DSCs, due to the dependency of SINR on the location of ground user, a closed form expression for the total coverage area cannot be derived. In a more general case, the DSCs can be placed at different heights and consequently they can have different coverage performance $( A _ { \mathrm { C } , 1 } \neq A _ { \mathrm { C } , 2 } )$ . The total covered area can be written as:

$$
\begin{array}{l} A _ {C} = 2. \int_ {R = 0} ^ {R _ {m, 1}} \int_ {\phi = \phi_ {\min, 1} (R)} ^ {\phi = \phi_ {\max, 1} (R)} R. d R d \phi \tag {20} \\ + 2. \int_ {R = 0} ^ {R _ {m, 2}} \int_ {\phi = \phi_ {m i n, 2} (R)} ^ {\phi = \pi} R. d R d \phi , \\ \end{array}
$$

where $R _ { m , 1 }$ and $R _ { m , 2 }$ is the maximum coverage for the first and second DSCs in the absence of interference, $\phi _ { \mathrm { m i n , 1 } } ( R )$ and $\phi _ { \mathrm { m i n , 2 } } ( R )$ ( )are the minimum angle that for a given R can be ( )covered by DSCs.

In this case, beyond the optimal DSCs distance, the optimal altitudes should also be determined. To this end, a three dimensional search over D, $h _ { 1 }$ and $h _ { 2 }$ is required. Then we should have

$$
\left(D _ {\text { opt }}, h _ {1, \text { opt }}, h _ {2, \text { opt }}\right) = \underset {D, h _ {1}, h _ {2}} {\arg \max} \{A _ {C} (D, h _ {1}, h _ {2}) \}. \tag {21}
$$

## IV. NUMERICAL RESULTS

Assuming that DSCs are operating in urban environments, numerical and analytical results are presented. Table I lists the typical parameters used in the numerical analysis [4]. Note that the values of α and β in (3) depend on the environment and are different when DSCs operate in other areas such as dense urban or suburban. Here, we consider an urban area and use the corresponding α and β parameters to compute the path loss effect.

Figure 4 shows the minimum transmit power required to have a certain coverage radius as a function of DSC altitude. Deploying a DSC at the optimal altitude minimizes the minimum required transmit power for covering a target area. In fact, for very low altitudes, due to the shadowing impact, the probability of LOS connections between transmitter and receiver decreases and consequently the coverage radius decreases. On the other hand, in very high altitude LOS links exist with a high probability. However, due to the large distance between transmitter and receiver, the path loss increases and consequently the coverage performance decreases. For instance, the optimal altitude for providing 500 m coverage radius while consuming minimum transmit power is 310 m. Moreover, in Figure 4, we can see that only one local minimum exists for the transmit power as a function of altitude. The results in Figure 4 provide very useful guidelines for power minimization which is one of the main concerns in designing DSC networks. Figure 4 shows that as the radius of target area increases, both the optimal altitude and the minimum transmit power required to cover the area increase.

TABLE I: Parameters in numerical analysis

<table><tr><td>Parameters</td><td>Value</td></tr><tr><td> $f_c$ </td><td>2 GHz</td></tr><tr><td> $\xi_{\text{LoS}}$ </td><td>1 dB</td></tr><tr><td> $\xi_{\text{LoS}}$ </td><td>20 dB</td></tr><tr><td>N(200 KHz bandwidth)</td><td>-120 dBm</td></tr><tr><td> $\alpha$ </td><td>9.6</td></tr><tr><td> $\beta$ </td><td>0.28</td></tr><tr><td>length of area (a)</td><td>2000 m</td></tr><tr><td> $\gamma_{\text{th}}$ </td><td>10 dB</td></tr></table>

![](images/89d8138ca0f2b7bd66d341e3afcb7833f1e44080a1e35b72f94c607886cd9fda.jpg)

<details>
<summary>line chart</summary>

| Altitude (m) | R_c=1500 m | R_c=1000 m | R_c=500 m |
| ------------ | ---------- | ---------- | --------- |
| 0            | 12.0       | 9.0        | 3.0       |
| 500          | -5.0       | -8.0       | -15.0     |
| 1000         | -6.0       | -7.0       | -10.0     |
| 1500         | -5.5       | -6.5       | -7.0      |
| 2000         | -4.0       | -5.0       | -5.0      |
| 2500         | -2.0       | -3.0       | -3.0      |
</details>

Fig. 4: Minimum required transmit power

In Figure 5, we show the impact of interference on the coverage performance when two DSC are located at an altitude of  m and a separation distance of  m. The target area is 300 1100a rectangle with a   m, b   m. The overall coverage = 2000 = 700area includes two parts inside and outside of the target area. Note that the effective coverage area is the part of coverage region inside the target area. Figure 5 also shows the impact of interference between DSCs that creates holes between the coverage regions provided by the two DSCs. To maximize the effective coverage area, the distance between two DSCs should be properly adjusted such that the interference between DSCs is not high while the coverage region outside the target area is minimized.

Figure 6 shows the ratio of effective coverage area to the target area that can be achieved using two DSCs for different values of D. In the presence of interference for high values of $D ,$ although the DSCs septation is sufficient to mitigate the impact of interference, they mainly provide coverage for outside of the target area which is not desirable. On the other hand, if the DSCs are very close together, interference between them will significantly reduce the overall coverage performance. As shown in Figure 6, an optimal separation distance between the two DSCs resulting in a maximum coverage in both interference and non-interference cases exists and is about 1100 m and 900 m respectively. In the non-interference situation, as expected, the overall coverage is higher and the optimal separation distance is lower compared to that of in the interference case. The reason is that when there is no interference, we can reduce the DSCs separation distance without loosing the coverage performance that can occur in the presence of interference.

![](images/13ac5363c81800f2d9f29a4e3e9af5868b1d848efa9aa107612a72375018bcd2.jpg)

<details>
<summary>radar chart</summary>

| Coverage Type             | Range     |
| ------------------------- | --------- |
| DSC₁ coverage area       | 120–150   |
| DSC₂ coverage area       | 60–330    |
</details>

Fig. 5: Coverage performance of two DSCs in the presence of interference.

![](images/520a5022cf3e2d9b243c393ea43ea410b587dfd443f4d14aea05a9db6e1535a9.jpg)

<details>
<summary>line chart</summary>

| UAVs distance (m) | Overall coverage ratio |
| ----------------- | ---------------------- |
| 1100              | 0.78                   |
</details>

Fig. 6: Overall coverage ratio versus DSCs separation distance.

In Figure 7, we show the optimal DSCs separation distance as a function of length of the target area. According to Figure 7, the optimal distance between DSCs almost linearly increases according to the size of the area. For example, when the length of the target area changes from 1800 m to 2400 m, the optimal distance between DSCs increases from 1000 m to 1350 m. In fact, to avoid interference between DSCs we should deploy them as separate as possible but still inside the target area. This can be interpreted as scaling the distance between DSCs along with the target area.

## V. CONCLUSIONS

In this paper, we have studied the coverage performance of DSCs acting as base stations in low altitude platform. First, the impact of a DSC altitude on the downlink ground coverage has been evaluated and the optimal values for altitude which lead to maximum coverage and minimum required transmit power have been determined. Next, considering an interference free situation and given a target area to be covered, the optimal deployment for two DSCs in terms of altitude and distance between them has been presented. In the presence of full interference between the two DSCs, the coverage area has been formulated. The results have shown the existence of an optimal

![](images/6011c6c563d8ca2d6d1d9a3d126949045ef9c33e8674f919ead7e69932b26efc.jpg)

<details>
<summary>line chart</summary>

| Length of the target area (m) | Optimal DSCs distance (m) |
| ----------------------------- | ------------------------- |
| 1600                          | 850                       |
| 1800                          | 1000                      |
| 2000                          | 1150                      |
| 2200                          | 1250                      |
| 2400                          | 1350                      |
| 2600                          | 1450                      |
| 2800                          | 1550                      |
| 3000                          | 1700                      |
</details>

Fig. 7: Optimal DSCs distance versus length of target area.

DSCs separation distance which provides maximum coverage for a given target area. The results presented in the paper provide a stepping stone addressing the more general cases with higher number of DSCs.

## REFERENCES

[1] I. Bucaille, S. Hethuin, A. Munari, R. Hermenier, T. Rasheed, and S. Allsopp, “Rapidly deployable network for tactical applications: Aerial base station with opportunistic links for unattended and temporary events absolute example,” in Proc. of IEEE Military Communications Conference, San Diego, CA, USA, Nov. 2013.  
[2] K. Daniel and C. Wietfeld, “Using public network infrastructures for UAV remote sensing in civilian security operations,” DTIC Document, Tech. Rep., Mar. 2011.  
[3] S. Rohde and C. Wietfeld, “Interference aware positioning of aerial relays for cell overload and outage compensation,” in Proc. of IEEE Vehicular Technology Conference (VTC Fall), Quebec, QC, Canada, Sept. 2012.  
[4] A. Hourani, S. Kandeepan, and A. Jamalipour, “Modeling air-to-ground path loss for low altitude platforms in urban environments,” in Proc. of IEEE Global Telecommunications Conference, Austin, Tx, USA, Dec. 2014.  
[5] Z. Han, A. L. Swindlehurst, and K. Liu, “Optimization of MANET connectivity via smart deployment/movement of unmanned air vehicles,” IEEE Transactions on Vehicular Technology, vol. 58, no. 7, pp. 3533– 3546, Dec. 2009.  
[6] F. Jiang and A. L. Swindlehurst, “Optimization of UAV heading for the ground-to-air uplink,” IEEE Journal on Selected Areas in Communications, vol. 30, no. 5, pp. 993–1005, June 2012.  
[7] Q. Feng, E. K. Tameh, A. R. Nix, and J. McGeehan, “Modelling the likelihood of line-of-sight for air-to-ground radio propagation in urban environments,” in Proc. of IEEE Global Telecommunications Conference, San Diego, CA, USA, Nov. 2006.  
[8] Q. Feng, J. McGeehan, E. K. Tameh, and A. R. Nix, “Path loss models for air-to-ground radio channels in urban environments,” in Proc. of IEEE Vehicular Technology Conference, Melbourne, Vic, Australia, May 2006.  
[9] J. Holis and P. Pechac, “Elevation dependent shadowing model for mobile communications via high altitude platforms in built-up areas,” IEEE Transactions on Antennas and Propagation, vol. 56, no. 4, pp. 1078– 1084, April 2008.  
[10] Y. Zheng, Y. Wang, and F. Meng, “Modeling and simulation of pathloss and fading for air-ground link of HAPs within a network simulator,” in Proc. of IEEE International Conference on Cyber-Enabled Distributed Computing and Knowledge Discovery (CyberC), Beijing, China, Oct. 2013.  
[11] A. Hourani, K. Sithamparanathan, and S. Lardner, “Optimal LAP altitude for maximum coverage,” IEEE Wireless Communication Letters, vol. 3, no. 6, pp. 569–572, Dec. 2014.