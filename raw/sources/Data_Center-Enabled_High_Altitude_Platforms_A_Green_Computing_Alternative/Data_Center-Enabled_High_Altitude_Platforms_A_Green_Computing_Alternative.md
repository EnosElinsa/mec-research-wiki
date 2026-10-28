# Data Center-Enabled High Altitude Platforms: A Green Computing Alternative

Wiem Abderrahim , Member, IEEE, Osama Amin , Senior Member, IEEE, and Basem Shihada , Senior Member, IEEE

Abstract—Information technology organizations and companies are seeking greener alternatives to traditional terrestrial data centers to mitigate global warming and reduce carbon emissions. Currently, terrestrial data centers consume a significant amount of energy, estimated at about 1.5% of worldwide electricity use. Furthermore, the increasing demand for data-intensive applications is expected to raise energy consumption, making it crucial to consider sustainable computing paradigms. In this study, we propose a data center-enabled High Altitude Platform (HAP) system, where a flying data center supports the operation of terrestrial data centers. We conduct a detailed analytical study to assess the energy benefits and communication requirements ofthis approach. Our findings demonstrate that a data center-enabled HAP is more energy-efficient than a traditional terrestrial data center, owing to the naturally low temperature in the stratosphere and the ability to harvest solar energy. Adopting a data center-HAP can save up to 14% of energy requirements while overcoming the offloading outage problem and the associated delay resulting from server distribution. Our study highlights the potential of a data centerenabled HAP system as a sustainable computing solution to meet the growing energy demands and reduce carbon footprint.

Index Terms—Data centers, data center-enabled high altitude platforms, energy-efficiency (EE), high altitude platforms (HAP), workload offloading.

## I. INTRODUCTION

D <sup>ATA</sup> <sup>centers</sup> <sup>are</sup> <sup>one</sup> <sup>of</sup> <sup>the</sup> <sup>top</sup> <sup>enabling</sup> <sup>technologies</sup> <sup>for</sup>the information technology industry, with a global market the information technology industry, with a global market spending of216,095 million US dollars in 2022 [1], [2]. They are considered the mission-critical infrastructure of this computing era because they play a pivotal role in processing and storing our continuously-growing data [3]. This role is unprecedentedly crucial given the data-intensive applications used in nowadays advanced fields such as artificial intelligence and internet-ofeverything applications [1], [4], [5], [6], which require extensive growth of this infrastructure’s sizes and functionalities [1], [7]. However, data centers face major energy-efficiency issues [3], [8] as a large-scale computing infrastructure. Indeed, they consume not only substantial amounts of energy, around 1.5% of the worldwide electricity use but also the annual growth of the consumed energy by data centers is predicted to rise exponentially in the upcoming years [1], [9], [10], [11], [12]. For example, the electricity demand of Google’s data centers increased twenty fold over the last ten years [10]. Moreover, China’s data centers will be devouring more than 400 billion kWh by 2030, accounting for 3.7 percent of the country’s total electricity consumption [13]. In addition, the annual energy cost of data centers is expected to surpass their construction cost and equipment price within the upcoming few years [1], [3], [10]. These statistics are particularly alarming because the non-renewable energy is still the predominant source to generate electricity nowadays [9]. Therefore, serious research efforts should be conducted towards finding practical solutions that improve the current data center energy efficiency, which can help reduce global carbon emissions. According to Gartner, Inc., it is expected that by 2027, around 75% of organizations will have implemented a data center infrastructure sustainability program due to cost optimization and stakeholder pressures. [14].

## A. Literature Review

Data center energy consumption is primarily distributed between the cooling infrastructure (30%–40%) and the computing infrastructure (26%–56%) [3], [9], [15]. As a result, various energy-aware approaches have been investigated in the literature to improve data center energy efficiency from both computation and cooling perspectives [1], [9], [10], [16], [17], [18], [19], [20]. On the one hand, cooling energy can be reduced through strategies such as raised floors, racks’ arrangement following hot/cold aisles, chillers configuration, and fan optimization [9], [16]. Additionally, load balancing across geographically distributed data centers can decrease cooling power. For instance, workload distribution and scheduling should consider the energy/cooling efficiency of servers, as well as electricity costs and experienced delays [1], [10], [17], [18]. On the other hand, data center computational energy can be reduced through dynamic management of capacity by controlling idle servers [3], [12], [17], [21]. Furthermore, optimizing server speed by adjusting central processing unit (CPU) frequency can help reduce associated computational power [19]. Another way to decrease energy consumption in data centers is to leverage green options. For example, renewable energy sources like wind and solar power can supply electricity to data centers, as demonstrated by companies such as Apple, Google, Microsoft, and Facebook [18], [22]. Consequently, it is vital to explore how data centers can utilize renewable energy and study the factors that favor renewable energy over traditional sources, especially for geographically distributed data centers [18], [20], [23]. Most existing research efforts mainly focus on reducing computational energy and overlook cooling energy, a significant factor in terrestrial data centers [8] Moreover, renewable energy sources, such as solar and wind power, can be unreliable for mission-critical and large-scale data centers due to their dependence on variable weather conditions like cloud cover and wind patterns [11], [22].

## B. Contributions

To overcome the continual growth of data centers’ energy consumption, non-traditional energy-efficient computation paradigms are needed. We advocate data center-enabled High Altitude Platform (HAP) as a practical and green alternative to terrestrial data centers [24]. HAPs can be a core futuristic airborne network component that will revolutionize the networking frontier in the stratospheric range at an altitude between 17 km and 20 km [24], [25], [26]. HAPs offer several unique advantages, particularly from energy and ubiquity perspectives. First, being located in the stratosphere saves cooling energy thanks to the naturally low atmospheric temperature, which ranges between $- 5 0 ~ ^ { \circ } \mathrm { C }$ and $1 5 ~ ^ { \circ } \mathrm { C } .$ Therefore, a HAP-enabled data center can offload some workloads from terrestrial data centers, saving the associated cooling energy. Additionally, HAPs can host large solar panels on their large surfaces that supply electricity to the data center servers and partially cover the required computational power [24], [25], [26]. Second, HAPs have a pervasiveness advantage over terrestrial data centers thanks to the large footprint offered by the line of sight (LoS) links to the terrestrial infrastructure, wireless communication abilities and flexible relocation abilities [24], [25], [26]. HAPs can host multiple-input multiple-output (MIMO) antennas on their large surfaces and provide higher data rates to their users [24], [26], [27]. However, it is necessary to define the limits and conditions under which HAP-enabled data centers can be beneficial, considering the practical limitations of HAPs, the quality of communication links, the range of proper offloaded workloads, and the impact of transmission delay on queuing time. Nonetheless, HAP-enabled data centers offer a promising and sustainable solution to the increasing energy consumption of traditional terrestrial data centers.

In this paper, we analyze the operation of a data center on a HAP considering practical and realistic operational conditions. First, we compare the energy models ofHAP-enabled and terrestrial data centers, demonstrating significant energy savings with the former. We then analyze the harvested energy requirements to maintain the HAP’s flying condition while performing the required computation for the offloaded terestrial workload. Next, we examine the reliability of the transmission link between terrestrial data centers and HAP-based systems by studying the outage probability. To address transmission outages, we propose a re-transmit dropped workloads solution using a portion of the saved energy. Finally, we explore the delay experienced in transmitting or re-transmitting workloads to a HAP-enabled data center without affecting the queuing time and verify the conditions that enable reliable operation. Our study presents an extensive and pioneering analysis of energy, communication, and delay performance aspects of HAP-enabled data centers. The system model is presented in Section II, followed by our system analysis in Section III. In Section IV, we discuss and analyze our results. We conclude the paper in Section V.

![](images/66c6e95037a7bb8253714b315cc8fd2987ccceaa452ffc6a96400266e126d15b.jpg)  
Fig. 1. Data Center-enabled HAP architecture.

Notations: Lower case boldface letters denote vectors while upper case boldface letters denote matrices. The conjugatetranspose of matrix A is denoted by $A ^ { H }$ and the transpose of matrix A is denoted by $A ^ { T } . \parallel \cdot \parallel _ { F } ^ { 2 }$ denotes the square of Frobenius norm.  ·  denotes euclidean norm. $\pmb { I } _ { M }$ denotes the $M \times M$ identity matrix. $\mathbb { C } ^ { M \times N }$ denotes the complex space of $M \times N . \ \operatorname* { P r } ( \cdot )$ denotes the probability. Moreover, Table I summarizes the main notations used in this paper and their respective descriptions.

## II. SYSTEM MODEL

Our system model comprises a terrestrial data center and airborne data centers to offload some of the workloads. The terrestrial data center includes a set $\mathcal { I } = s _ { 1 } , . . . , s _ { I }$ of I servers arranged in a hot aisle/cold aisle configuration. The cold aisles face each other, while the hot aisles face each other. Additionally, the terrestrial data center has a cooling system consisting of a set ${ \mathcal { I } } = a c _ { 1 } , . . . , a c _ { J }$ of J computer room air conditioning (CRAC) units, as shown in Fig. 1. The purpose of the CRAC units is to maintain a temperature range of $1 8 ~ ^ { \circ } \mathrm { C }$ to $2 6 \ { } ^ { \circ } { \bf C } .$ following the recommendation of the American Society of Heating, Refrigerating, and Air-Conditioning Engineers [28]. On the other hand, the data center-enabled HAP comprises a set $\mathcal { T } ^ { \prime } = s _ { I + 1 } , . . . , s _ { I } + I ^ { \prime }$ of $I ^ { \prime } < I$ servers. Since the stratosphere’s average temperature falls between $- 5 0 ~ ^ { \circ } \mathrm { C }$ and $- 1 5 ~ ^ { \circ } \mathrm { C } .$ we assume that the data center-enabled HAP does not require any CRAC units [25], [26].

## A. Workload Model

The controller station (dispatcher) schedules the total workload that needs to be processed by our system among the servers $s _ { i \in \{ 1 , . . . , I + I ^ { \prime } \} }$ in the terrestrial data center and data centerenabled HAP, according to a Poisson process [10]. Let Λ denote the total workload arrival rate, such that $\begin{array} { r } { K = \int _ { t _ { 1 } } ^ { t _ { 2 } } \Lambda ( t ) } \end{array}$ dt, where $K$ -is the total number of tasks arriving in the system. The number of tasks $K _ { i }$ processed by server $s _ { i }$ can be expressed as $\begin{array} { r } { K _ { i } = \int _ { t _ { 1 } } ^ { t _ { 2 } } \lambda _ { i } ( t ) d t } \end{array}$ , where $\lambda _ { i }$ is the workload arrival rate to server $s _ { i }$ - . We assume that the arrival rate follows a Poisson process when distributed by the controller station. Therefore, $\begin{array} { r } { \sum _ { i = 1 } ^ { I + I ^ { \prime } } K _ { i } = \sum _ { i = 1 } ^ { I + I ^ { \prime } } \lambda _ { i } \left( t _ { 2 } - t _ { 1 } \right) \le K } \end{array}$

TABLE I DESCRIPTION OF MAIN NOTATIONS
<table><tr><td rowspan=1 colspan=1>Notation</td><td rowspan=1 colspan=1>Description</td><td rowspan=1 colspan=1>Unit</td></tr><tr><td rowspan=1 colspan=1>I</td><td rowspan=3 colspan=1>Number of servers in the terrestrial data centerNumber of cooling units in the terrestrial data centerNumber of servers in the HAP</td><td rowspan=3 colspan=1></td></tr><tr><td rowspan=1 colspan=1>J</td></tr><tr><td rowspan=1 colspan=1>I&#x27;</td></tr><tr><td rowspan=1 colspan=1> $\lambda _ { i }$ </td><td rowspan=1 colspan=1>Workload arrival rate to server si</td><td rowspan=1 colspan=1>task/s</td></tr><tr><td rowspan=1 colspan=1> $u _ { i }$ </td><td rowspan=1 colspan=1>Utilization ratio of server $s _ { i }$ </td><td rowspan=1 colspan=1> $\%$ </td></tr><tr><td rowspan=1 colspan=1> $\mu _ { i }$ </td><td rowspan=1 colspan=1>Service rate of server $s _ { i }$ </td><td rowspan=1 colspan=1>MIPS</td></tr><tr><td rowspan=1 colspan=1> $\theta ^ { * }$ </td><td rowspan=1 colspan=1>Computational task length</td><td rowspan=1 colspan=1>Bits</td></tr><tr><td rowspan=1 colspan=1> $P _ { i } ^ { \mathrm { i d l e } }$ </td><td rowspan=1 colspan=1>Average power of idle server $s _ { i }$ </td><td rowspan=1 colspan=1>Watt</td></tr><tr><td rowspan=1 colspan=1> $P _ { i } ^ { \mathrm { p e a k } }$ </td><td rowspan=1 colspan=1>Average power of fully utilized server $s _ { i }$ </td><td rowspan=1 colspan=1>Watt</td></tr><tr><td rowspan=1 colspan=1> $P ^ { \mathrm { f a n } }$ </td><td rowspan=1 colspan=1>Fan power</td><td rowspan=1 colspan=1>Watt</td></tr><tr><td rowspan=1 colspan=1> $Q _ { j }$ </td><td rowspan=1 colspan=1>Heat amount removed by cooling unit $a c _ { j }$ </td><td rowspan=1 colspan=1>Watt</td></tr><tr><td rowspan=1 colspan=1> $\mathrm { C O P }$ </td><td rowspan=1 colspan=1>Performance coefficient of cooling unit acj</td><td rowspan=1 colspan=1>%</td></tr><tr><td rowspan=1 colspan=1> $P _ { i } ^ { \mathrm { c o m p } }$ </td><td rowspan=1 colspan=1>Computational power of server si</td><td rowspan=1 colspan=1>Watt</td></tr><tr><td rowspan=1 colspan=1> $E _ { i } ^ { \mathrm { c o m p } }$ </td><td rowspan=1 colspan=1>Computational energy of server si</td><td rowspan=1 colspan=1>Joule</td></tr><tr><td rowspan=1 colspan=1> $E _ { \mathrm { T D C } } ^ { \mathrm { c o m p } }$ </td><td rowspan=1 colspan=1>Computational energy of the terrestrial data center</td><td rowspan=1 colspan=1>Joule</td></tr><tr><td rowspan=1 colspan=1> $P _ { j } ^ { \mathrm { c o o l } }$ </td><td rowspan=1 colspan=1>Cooling power of cooling unit $a c _ { j }$ </td><td rowspan=1 colspan=1>Watt</td></tr><tr><td rowspan=1 colspan=1> $E _ { i } ^ { \mathrm { c o m p } }$ </td><td rowspan=1 colspan=1>Cooling energy of cooling unit $a c _ { j }$ </td><td rowspan=1 colspan=1>Joule</td></tr><tr><td rowspan=1 colspan=1> $E _ { \mathrm { T D C } } ^ { \mathrm { c o o l } }$ </td><td rowspan=1 colspan=1>Cooling energy of the terrestrial data center</td><td rowspan=1 colspan=1>Joule</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=2 colspan=1>HAP latitudeConsidered day of the year</td><td rowspan=2 colspan=1>Degree</td></tr><tr><td rowspan=1 colspan=1> $\mathrm { _ d }$ </td></tr><tr><td rowspan=1 colspan=1> $\eta _ { \mathrm { p v } }$ </td><td rowspan=1 colspan=1>Efficiency of the photo-voltaic system of the HAP</td><td rowspan=1 colspan=1> $\%$ </td></tr><tr><td rowspan=1 colspan=1> $\boldsymbol { A } _ { \mathrm { p v } }$ </td><td rowspan=1 colspan=1>Area of the photo-voltaic system of the HAP</td><td rowspan=1 colspan=1> $\mathrm { m ^ { 2 } }$ </td></tr><tr><td rowspan=1 colspan=1> $G$ </td><td rowspan=1 colspan=1>Total extra-terrestrial solar radiance per $\mathrm { m ^ { 2 } }$ </td><td rowspan=1 colspan=1> $W / \mathrm { m } ^ { 2 }$ </td></tr><tr><td rowspan=1 colspan=1> $\rho$ </td><td rowspan=1 colspan=1>Air density</td><td rowspan=1 colspan=1> $k g / \mathrm { m } ^ { 3 }$ </td></tr><tr><td rowspan=1 colspan=1> $\eta _ { \mathrm { p r o p } }$ </td><td rowspan=1 colspan=1>Propeller efficiency</td><td rowspan=1 colspan=1> $\%$ </td></tr><tr><td rowspan=1 colspan=1> $v _ { \mathrm { w i n d } }$ </td><td rowspan=1 colspan=1>Wind velocity</td><td rowspan=1 colspan=1> $\mathrm { m } / \mathrm { s }$ </td></tr><tr><td rowspan=1 colspan=1> $v _ { \mathrm { H A P } }$ </td><td rowspan=1 colspan=1>HAP velocity</td><td rowspan=1 colspan=1> $\mathrm { m } / \mathrm { s }$ </td></tr><tr><td rowspan=1 colspan=1> $C _ { \mathrm { D } }$ </td><td rowspan=1 colspan=1>Drag coefficient</td><td rowspan=1 colspan=1>%</td></tr><tr><td rowspan=1 colspan=1> $\Psi _ { 0 }$ </td><td rowspan=1 colspan=1>Channel power gain at the reference distance</td><td rowspan=1 colspan=1>dB</td></tr><tr><td rowspan=1 colspan=1> $L _ { \mathrm { H A P } }$ </td><td rowspan=1 colspan=1>Distance between the terrestrial data center and HAP</td><td rowspan=3 colspan=1>mHz</td></tr><tr><td rowspan=1 colspan=1>ζ</td><td rowspan=2 colspan=1>Rician factorCarrier frequency</td></tr><tr><td rowspan=1 colspan=1> $f _ { \mathrm { c a r r i e r } }$ </td></tr><tr><td rowspan=1 colspan=1> $P _ { \mathrm { H A P } } ^ { \mathrm { h a r v } }$ </td><td rowspan=1 colspan=1>Harvested power of the HAP</td><td rowspan=1 colspan=1>Watt</td></tr><tr><td rowspan=1 colspan=1> $E _ { \mathrm { H A P } } ^ { \mathrm { h a r v } }$ </td><td rowspan=1 colspan=1>Harvested energy of the HAP</td><td rowspan=1 colspan=1>Joule</td></tr><tr><td rowspan=1 colspan=1> $P _ { \mathrm { H A P } } ^ { \mathrm { p r o p } }$ </td><td rowspan=1 colspan=1>Propulsion power of the HAP</td><td rowspan=1 colspan=1>Watt</td></tr><tr><td rowspan=1 colspan=1> $E _ { \mathrm { H A P } } ^ { \mathrm { p r o p } }$ </td><td rowspan=1 colspan=1>Propulsion energy of the HAP</td><td rowspan=1 colspan=1>Joule</td></tr><tr><td rowspan=1 colspan=1> $P _ { \mathrm { H A P } } ^ { \mathrm { p a y l o a d } }$ </td><td rowspan=1 colspan=1>Payload power of the HAP</td><td rowspan=1 colspan=1>Watt</td></tr><tr><td rowspan=1 colspan=1> $E _ { \mathrm { H A P } } ^ { \mathrm { p a y l o a d } }$ </td><td rowspan=1 colspan=1>Payload energy of the HAP</td><td rowspan=2 colspan=1>JouleJoule</td></tr><tr><td rowspan=1 colspan=1> $E _ { \mathrm { T D C - H A P } } ^ { \mathrm { t r a n s } }$ </td><td rowspan=1 colspan=1>Transmission energy of the data center enabled-HAP</td></tr></table>

When the arriving workload is processed by server $s _ { i } ,$ it transitions from the idle state to the active state and generates a CPU utilization ratio of $0 < u _ { i } ( \lambda _ { i } ) \leq \overline { { u } } _ { i } < 1 0 0 \%$ , where $\overline { { u } } _ { i }$ is the desirable utilization ratio of server $s _ { i }$ . We can express the utilization ratio $u _ { i }$ as a function of the arrival rate $u _ { i } ( \lambda _ { i } ) = \theta ^ { * } \lambda _ { i } / \mu _ { i }$ where $\theta ^ { * }$ is the expected value of the task length assumed to be constant for all tasks. The service rate of server $s _ { i } ,$ denoted by $\mu _ { i }$ and measured in millions of instructions per second (MIPS), refers to the capacity of its CPU to process tasks.

## B. Power Model ofthe Terrestrial Data Center

A breakdown of the energy consumed by a data center shows that the computational infrastructure and the cooling infrastructure are the two primary components that absorb the data center energy [3]. Therefore, we focus on studying the energy consumed by these components in the following subsections.

1) Computational Model: The I servers of the data center have different characteristics in terms of CPU capacity. We assume that the server power consumption and the CPU utilization have a linear relationship [3]. Therefore, the computational power $P _ { i } ^ { \mathrm { c o m p } }$ consumed by $s _ { i }$ can be expressed as [3], [9], [29]

$$
P _ { i } ^ { \mathrm { c o m p } } ( \lambda _ { i } ) = P _ { i } ^ { \mathrm { i d l e } } + \left( P _ { i } ^ { \mathrm { p e a k } } - P _ { i } ^ { \mathrm { i d l e } } \right) u _ { i } ( \lambda _ { i } ) ,\tag{1}
$$

where $P _ { i } ^ { \mathrm { i d l e } }$ is the average power value when server $s _ { i }$ is idle $( \mathrm { i . e . }$ $u _ { i } ( \lambda _ { i } ( t ) ) = 0 \% )$ and $P _ { i } ^ { \mathrm { p e a k } }$ is the average power value when the server is fully utilized, i.e., $u _ { i } ( \lambda _ { i } ( t ) ) = \overline { { u } } _ { i }$

2) Cooling Model: The compressor and the fans of the CRAC units are the main consumers of the cooling energy in a data center [3], [10]. In a data center, the cold air supplied by the CRAC units enters through the cold aisle to the server inlets in the front of the server racks and is exhausted into the hot aisle through the server outlets in the back of the server racks. As a result of this air circulation, each node in the data center, whether a server $s _ { i \in 1 \ldots I }$ or a CRAC unit $\begin{array} { l } { { a c _ { j \in 1 \dots J } } } \end{array}$ , has an inlet temperature $T ^ { \mathrm { i n } }$ and an outlet temperature $T ^ { \mathrm { o u t } }$ . The inlet temperature $T ^ { \mathrm { i n } }$ represents the amount of heat received from other nodes, while the outlet temperature $T ^ { \mathrm { o u t } }$ represents the amount of heat contained in a given node. Therefore, we can express the cooling power $P ^ { \mathrm { c o o l } } \bar { j }$ of CRAC unit $a c _ { j \in 1 \ldots J }$ as the power necessary to cool the servers under its coverage. This cooling power can be calculated as follows [10], [30],

$$
P _ { j } ^ { \mathrm { c o o l } } ( t ) = P _ { j } ^ { \mathrm { f a n } } + \frac { Q _ { j } ( t ) } { \mathrm { C O P } ( T _ { j } ^ { \mathrm { o u t } } ) } ,\tag{2}
$$

where $P ^ { \mathrm { f a n } }$ is the fan power, $Q _ { j }$ is the heat amount removed by CRAC unit $a c _ { j }$ and COP is the $a c _ { j }$ performance coefficient given by $\mathrm { C O P } ( T _ { j } ^ { \mathrm { o u t } } ) = 0 . 0 0 6 8 ( T _ { j } ^ { \mathrm { o u t } } ) ^ { \ddot { 2 } } + 0 . 0 0 8 T _ { j } ^ { \mathrm { o u t } } + 0 . 4 5 8$

## C. Power Model ofthe Data Center-Enabled HAP

Managing energy in HAPs is crucial because they are typically designed for long-duration missions (at least one year). Throughout this subsection, we study the energy harvested and consumed by a data center-enabled HAP.

1) Energy Harvesting Model: The main energy source for the daytime operation of HAPs is the solar energy [25], [26]. HAPs also incorporate energy storage components; which are typically Lithium-Sulphur batteries or hydrogen fuel cells [26], [31]. These batteries support the nighttime operation of the HAP and are fed by the solar energy harvested during the daytime [26], [31]. By assuming that the energy harvested can be stored for

24 $h ,$ the mean solar power harvested by the HAP at latitude l on day d can be expressed as [31],

$$
P _ { \mathrm { H A P } } ^ { \mathrm { h a r v } } ( l , d ) = \eta _ { \mathrm { p v } } \mathcal { A } _ { \mathrm { p v } } G ( l , d ) ,\tag{3}
$$

where $\eta _ { \mathrm { p v } }$ is the efficiency of the photo-voltaic system, ${ \mathcal A } _ { \mathrm { p v } }$ is the area of the photo-voltaic system and G is the total extraterrestrial solar radiance per $\mathrm { m } ^ { 2 }$ and is given by [31],

$$
G ( l , d ) = \frac { \tau ( l , d ) G _ { \operatorname* { m a x } } ( l , d ) } { \xi _ { \operatorname* { m a x } } ( l , d ) } \left( 1 - \cos ( \xi _ { \operatorname* { m a x } } ( l , d ) ) \right) ,\tag{4}
$$

where $\tau ( l , d )$ is the daylight duration at latitude l on day $d ,$ $G _ { \operatorname* { m a x } } ( l , d )$ is corresponding maximum radiation intensity and $\xi _ { \operatorname* { m a x } } ( l , d )$ is the corresponding maximum altitude of the sun (in rd). τ (l, d) is expressed in hours from [31],

$$
\tau ( l , d ) = 1 - \frac { 1 } { \pi } \cos ^ { - 1 } \left( \frac { \tan ( l ) \sin ( \epsilon ) \sin ( \phi ( d ) ) } { \sqrt { 1 - \sin ^ { 2 } ( \epsilon ) \sin ^ { 2 } ( \phi ( d ) ) } } \right) ,\tag{5}
$$

where $\epsilon = 0$ .4093 is the angle of obliquity of the Earth and $\phi ( d )$ is the azimuthal angle of the sun and is given by [31],

$$
\begin{array} { c } { { \phi ( d ) = \mathrm { ~ - 1 . 3 4 1 1 + } M ( d ) + 0 . 0 3 3 4 \sin ( M ( d ) ) } } \\ { { { } } } \\ { { + 0 . 0 0 0 3 \sin ( 2 M ( d ) ) , } } \end{array}\tag{6}
$$

such that $M ( d ) = - 0 . 0 4 1 + 0 . 0 1 7 2 0 2$ d is the angular distance of the sun, which is also known as mean anomaly $[ 3 1 ] . G _ { \mathrm { m a x } } ( l , d )$ can be computed from [31],

$$
G _ { \mathrm { m a x } } ( l , d ) = G _ { \mathrm { s o l a r } } \left( 1 + 0 . 0 3 3 \cos \left( \frac { 3 6 0 d } { 3 6 5 } \right) \right) \cos \left( l - \delta ( d ) \right) ,\tag{7}
$$

where $G _ { \mathrm { s o l a r } } = 1 3 6 6 . 1 \ : \mathrm { W / m ^ { 2 } }$ is the standard solar constant at zero air mass and δ is the solar declination angle expressed as (in rd) [31]

$$
\delta ( d ) = 0 . 4 0 9 3 \sin \left( { \frac { 2 \pi ( d - 7 9 . 7 5 ) } { 3 6 5 } } \right) .\tag{8}
$$

Whereas $\xi _ { \mathrm { m a x } }$ is given by $\begin{array} { r } { \xi _ { \mathrm { m a x } } ( l _ { r } , d ) = \frac { \pi } { 2 } + l _ { r } - \delta ( d ) } \end{array}$ ; where $l _ { \mathrm { r } }$ is the latitude in rd [31].

2) Consumption Model: The power consumed by a HAP is determined mainly by both the payload and the propulsion subsystems [26], [31]. The required power by the payload is the computational power of the servers carried by the HAP. The required power by the HAP propeller can be expressed as [32],

$$
P _ { \mathrm { H A P } } ^ { \mathrm { p r o p } } ( l , d ) = \ : \frac { \rho } { 2 \eta _ { \mathrm { p r o p } } } \ : v _ { \mathrm { w i n d } } ^ { 3 } ( l , d ) \ : v _ { \mathrm { H A P } } ^ { 2 / 3 } \ : C _ { \mathrm { D } } ,\tag{9}
$$

where $\rho$ is the air density, $\eta _ { \mathrm { p r o p } }$ is the propeller efficiency, $v _ { \mathrm { w i n d } }$ is the wind velocity, v<sub>HAP</sub> is the HAP velocity and $C _ { \mathrm { D } }$ is the drag coefficient, which is expressed as $C _ { D } = N _ { \mathrm { C } } \ : C _ { \mathrm { e n v e l o p e } } ;$ ; such that $N _ { \mathrm { C } }$ is a constant equal to 1.8 in the scope of this paper and C<sub>envelope</sub> is given by [32],

$$
C _ { \mathrm { e n v e l o p e } } = { \frac { 0 . 1 7 2 ~ f _ { \mathrm { r } } ^ { \frac { 1 } { 3 } } + 0 . 2 5 2 ~ f _ { \mathrm { r } } ^ { - 1 . 2 } + 1 . 0 3 2 ~ f _ { \mathrm { r } } ^ { - 2 . 7 } } { R _ { \mathrm { e } } ^ { \frac { 1 } { 6 } } } } ,\tag{10}
$$

where $\begin{array} { r } { f _ { \mathrm { r } } = \frac { L _ { \mathrm { H A P } } } { D _ { \mathrm { H A P } } } } \end{array}$ is the fitness ratio ofthe HAP body length $L _ { \mathrm { H A P } }$ to its maximum width/diameter $D _ { \mathrm { H A P } }$ , and $R _ { \mathrm { e } }$ is the Reynolds

number given by [32],

$$
R _ { \mathrm { e } } = \frac { \rho { v _ { \mathrm { w i n d } } ( l , d ) } { \cal D } _ { \mathrm { H A P } } } { \kappa } ,\tag{11}
$$

where $\kappa$ is the air dynamic viscosity [32].

## D. Channel Model

We assume that both the terrestrial data center and the data center-enabled HAP utilize MIMO technology to overcome path loss and fading [27]. Specifically, the terrestrial data center is equipped with N antennas, and the HAP is equipped with M antennas. The channel between the terrestrial data center and the HAP can be modeled using Rician fading, which accounts for both a line-of-sight component and a scattered component. This channel model can be expressed as follows [27], [33], [34], [35]:

$$
{ \cal H } _ { \mathrm { H A P } } ( l ) = \sqrt { \frac { \Psi _ { 0 } } { L _ { \mathrm { H A P } } ^ { 2 } } } \left( \sqrt { \frac { \zeta } { \zeta + 1 } } \bar { \cal H } _ { \mathrm { H A P } } ( l ) + \sqrt { \frac { 1 } { \zeta + 1 } } \hat { \cal H } _ { \mathrm { H A P } } \right) ,\tag{12}
$$

where $\Psi _ { 0 }$ is the channel power gain at the reference distance; $L _ { \mathrm { H A P } }$ is the distance between the terrestrial data center and the HAP; ζ is the Rician factor; $\bar { \pmb { H } } _ { \mathrm { H A P } } \in \mathbb { C } ^ { M \times N }$ is the LoS channel component and $\hat { \pmb { H } } _ { \mathrm { H A P } } \in \mathbb { C } ^ { M \times N }$ is the Rayleigh fading component. The LoS channel component is given by $\bar { \pmb { H } } _ { \mathrm { H A P } } ( l ) =$ $\begin{array} { r } { \exp ( - j \frac { 2 \pi f _ { \mathrm { c a r r i e r } } } { C } r _ { \mathrm { H A P } } ( l ) ) } \end{array}$ where $f _ { \mathrm { c a r r i e r } }$ is the carrier frequency; $C$ is the speed of light and r is the length of the direct path between the transmit and receive antennas. The Rayleigh fading component $\hat { H } _ { \mathrm { H A P } }$ follows the distribution ${ \mathcal { C N } } ( 0 , I )$ Accordingly, the achievable data rate between the terrestrial data center and the HAP can be expressed as [27],

$$
R _ { \mathrm { H A P } } ( l ) = B \log \operatorname * { d e t } { ( I _ { M } + H _ { \mathrm { H A P } } ( l ) q _ { \mathrm { H A P } } q _ { \mathrm { H A P } } ^ { H } H _ { \mathrm { H A P } } ^ { H } ( l ) n ^ { - 1 } ) } ,\tag{(13}
$$

where B is the bandwidth available for the transmission between the terrestrial data center and the HAP; $\pmb { q } _ { \mathrm { H A P } } \in \mathbb { C } ^ { N \times 1 }$ is the precoding matrix of the terrestrial data center; $\mathbf { \boldsymbol { n } } \in \mathbb { C } ^ { M \times 1 }$ is the additive white Gaussian noise (AWGN) with distribution $\mathcal { C N } ( 0 , \sigma ^ { 2 } I _ { M } )$

## III. SYSTEM ANALYSIS

In this section, we analyze the performance of a data centerenabled HAP and compare it with a terrestrial data center. We begin by examining the conditions under which the energy harvested by the $\mathrm { H A P } ^ { \prime } \mathrm { s }$ solar panels can sustain the HAP’s flight and power the hosted servers. Next, we establish a comprehensive energy model for both systems and demonstrate that a data center-enabled HAP can achieve significant energy savings compared to a terrestrial data center. We then investigate the outage probability of the transmission link between the terrestrial data center and the HAP and explore whether the saved energy can be utilized to manage dropped workloads. Finally, we analyze the delay experienced in a data center-enabled HAP, which consists of the transmission delay and the mean waiting time that represents the queuing time of tasks in the servers before processing. To facilitate our analysis, we define the workload arrival rate vector for the terrestrial data center as $\lambda _ { \mathrm { T D C } } = [ \lambda _ { i } ] \in \mathbb { R } ^ { I }$ and the workload arrival rate vector for the data center-enabled HAP as $\lambda _ { \mathrm { H A P } } = [ \lambda _ { i } ] \in \mathbb { R } ^ { I ^ { \prime } }$ . By using these vectors, we can compare and evaluate the workload performance of the two systems.

## A. HAP Flying Condition

Throughout the following analysis, we aim to determine whether the energy harvested by the solar panels on the HAP $( E _ { \mathrm { H A P } } ^ { \mathrm { h a r v } } )$ is sufficient to meet the energy requirements of both the payload $( E _ { \mathrm { H A P } } ^ { \mathrm { p a y l o a d } } )$ and propulsion $( E _ { \mathrm { H A P } } ^ { \mathrm { p r o p } } )$ . In our study, we consider the HAP payload to be a modular data center comprising a set of $I ^ { \prime }$ servers denoted by $T ^ { \prime } = s _ { I + 1 } , . . s _ { I + I ^ { \prime } }$ The power consumption of the payload is determined by the computational power of the servers, as given in (1). Therefore, the total power consumption of the payload can be expressed as,

$$
P _ { \mathrm { H A P } } ^ { \mathrm { p a y l o a d } } ( \lambda _ { \mathrm { H A P } } ) = \sum _ { i = 1 } ^ { I ^ { \prime } } \left( P _ { i } ^ { \mathrm { i d l e } } + \left( P _ { i } ^ { \mathrm { p e a k } } - P _ { i } ^ { \mathrm { i d l e } } \right) u _ { i } ( \lambda _ { i } ) \right) .\tag{14}
$$

Hence, $E _ { \mathrm { H A P } } ^ { \mathrm { p a y l o a d } }$ can be determined by integrating (14), resulting in the following expression:

$$
E _ { \mathrm { H A P } } ^ { \mathrm { p a y l o a d } } ( \lambda _ { \mathrm { H A P } } ) = \sum _ { i = I + 1 } ^ { I + I ^ { \prime } } \left( P _ { i } ^ { \mathrm { i d l e } } + \frac { \lambda _ { i } \theta ^ { * } } { \mu _ { i } } \left( P _ { i } ^ { \mathrm { p e a k } } - P _ { i } ^ { \mathrm { i d l e } } \right) \right) ( t _ { 2 } - t _ { 1 } ) .\tag{15}
$$

Similarly, $E _ { \mathrm { H A P } } ^ { \mathrm { p r o p } }$ is derived by integrating (9), which yields

$$
E _ { \mathrm { H A P } } ^ { \mathrm { p r o p } } ( l , d ) = v _ { \mathrm { w i n d } } ^ { \frac { 1 7 } { 6 } } ( l , d ) C _ { D } ^ { \prime } \left( t _ { 2 } - t _ { 1 } \right) ,\tag{16}
$$

where

$$
C _ { D } ^ { \prime } = \frac { \rho ^ { \frac { 5 } { 6 } } v _ { \mathrm { H A P } } ^ { 2 / 3 } } { 2 \eta _ { \mathrm { p r o p } } } \frac { \kappa ^ { \frac { 1 } { 6 } } N _ { \mathrm { C } } ( 0 . 1 7 2 f _ { \mathrm { r } } ^ { \frac { 1 } { 3 } } + 0 . 2 5 2 f _ { \mathrm { r } } ^ { - 1 . 2 } + 1 . 0 3 2 f _ { \mathrm { r } } ^ { - 2 . 7 } ) } { D _ { \mathrm { H A P } } ^ { \frac { 1 } { 6 } } } .
$$

Therefore, we define the flying condition of the HAP as follows:

$$
\begin{array} { r } { E _ { \mathrm { H A P } } ^ { \mathrm { p r o p } } ( l , d ) + E _ { \mathrm { H A P } } ^ { \mathrm { p a y l o a d } } ( \lambda _ { \mathrm { H A P } } ) \le E _ { \mathrm { H A P } } ^ { \mathrm { h a r v } } ( l , d ) . } \end{array}\tag{17}
$$

The flying condition of the HAP is affected by three parameters: l, d and $\lambda _ { \mathrm { H A P } }$ . To maintain the desired flying condition, we control the workload arrival rate that can be processed by the servers on the HAP, i.e., $\lambda _ { \mathrm { H A P } } \in \mathbb { R } ^ { I ^ { \prime } }$ . Specifically, for a fixed latitude $l ^ { * }$ and day of operation $d ^ { * }$ , the workload arrival rate $\lambda _ { \mathrm { H A P } }$ must satisfy the constraint $\lambda _ { \mathrm { H A P } } \leq \lambda _ { \mathrm { H A P } } ^ { \mathrm { m a x } } ,$ , where $\lambda _ { \mathrm { H A P } } ^ { \mathrm { m a x } }$ is the maximum allowable workload arrival rate. Hence, the corresponding energy consumption is $E _ { \mathrm { H A P } } ^ { \mathrm { p a y l o a d } } ( \lambda _ { \mathrm { H A P } } ^ { \mathrm { m a x } } ) =$ $E _ { \mathrm { H A P } } ^ { \mathrm { h a r v } } ( l ^ { * } , \bar { d ^ { * } } ) - E _ { \mathrm { H A P } } ^ { \bar { \mathrm { p r o p } } } ( l ^ { * } , \bar { d ^ { * } } )$

Assuming symmetrical characteristics for the servers, including the same service rate $( \mu _ { i } = \mu )$ , desirable utilization ratio $( \overline { { u } } i = \overline { { u } } )$ , and power consumption $( P _ { i } ^ { \mathrm { i d l e } } = P ^ { \mathrm { i d l e } }$ and $P _ { i } ^ { \mathrm { p e a k } } =$ $P ^ { \mathrm { p e a k } } )$ , the workload can be evenly distributed across multiple servers with $\lambda i ^ { \mathrm { m a x } } = \lambda ^ { \mathrm { m a x } }$ . To determine the maximum allowable workload arrival rate $\lambda ^ { \mathrm { m a x } }$ , we can use the following expression:

$$
\begin{array} { r l } & { \lambda ^ { \operatorname* { m a x } } ( l ^ { * } , d ^ { * } ) = } \\ & { \left( \frac { \eta _ { p v } \mathcal { A } _ { p v } \tau ( l ^ { * } , d ^ { * } ) G _ { \operatorname* { m a x } } ( l ^ { * } , d ^ { * } ) \left( 1 - \cos ( \xi _ { \operatorname* { m a x } } ( l ^ { * } , d ^ { * } ) ) \right) } { 2 4 \xi _ { \operatorname* { m a x } } ( l ^ { * } , d ^ { * } ) } \right. } \end{array}
$$

$$
- v _ { \mathrm { w i n d } } ^ { \frac { 1 7 } { 6 } } ( l ^ { * } , d ^ { * } ) C _ { D } ^ { \prime } - I ^ { \prime } P ^ { \mathrm { i d l e } } ) \frac \mu { I ^ { \prime } \theta ^ { * } ( P ^ { \mathrm { p e a k } } - P ^ { \mathrm { i d l e } } ) } .\tag{18}
$$

## B. Energy Saving

In this section, we investigate and compare the energy consumed by a terrestrial data center $E _ { \mathrm { T D C } } ^ { \mathrm { c o n s } }$ to the energy consumed by a data center-enabled HAP $E _ { \mathrm { T D C - H A P } } ^ { \mathrm { c o n s } }$ . Hence, we assume that all the workload directed to the HAP is successfully transmitted and no link outage is experienced. To establish a fair comparison, we assume that both systems have $I + I ^ { \prime }$ servers in total. Therefore, $I + I ^ { \prime }$ servers are placed in the terrestrial data center. In the data center-enabled HAP, I servers are placed in the terrestrial data center and $I ^ { \prime }$ servers are placed in the HAP.

1) Energy Consumption in Terrestrial Data Center: To understand the energy consumption of a terrestrial data center, i.e., $E _ { \mathrm { T D C } } ^ { \mathrm { c o n s } }$ , we break it down into two components: the computational energy consumed by the servers $\bar { ( }  { \boldsymbol { E } } _ { \mathrm { T D C } } ^ { \mathrm { c o m p } } (  { \lambda } _ { \mathrm { T D C } } ) )$ and the cooling energy consumed by CRAC units $( E _ { \mathrm { T D C } } ^ { \mathrm { c o o l } } ( \lambda _ { \mathrm { T D C } } ) )$ , which is written as,

$$
\begin{array} { r } { E _ { \mathrm { T D C } } ^ { \mathrm { c o n s } } ( \lambda _ { \mathrm { T D C } } ) = E _ { \mathrm { T D C } } ^ { \mathrm { c o m p } } ( \lambda _ { \mathrm { T D C } } ) + E _ { \mathrm { T D C } } ^ { \mathrm { c o o l } } ( \lambda _ { \mathrm { T D C } } ) . } \end{array}
$$

$E _ { \mathrm { T D C } } ^ { \mathrm { c o m p } }$ captures the computational energy consumed by all the servers expressed as,

$$
E _ { \mathrm { T D C } } ^ { \mathrm { c o m p } } ( \lambda _ { \mathrm { T D C } } ) = \sum _ { i = 1 } ^ { I + I ^ { \prime } } E _ { i } ^ { \mathrm { c o m p } } .
$$

To calculate the computational energy consumed by each server, we integrate (1) and obtain the value of $E _ { i } ^ { \mathrm { { c o m p } } }$ as,

$$
E _ { i } ^ { \mathrm { c o m p } } ( \lambda _ { i } ) = \left( P ^ { \mathrm { i d l e } } + \frac { \lambda _ { i } \theta ^ { * } } { \mu } \left( P ^ { \mathrm { p e a k } } - P ^ { \mathrm { i d l e } } \right) \right) ( t _ { 2 } - t _ { 1 } ) .\tag{19}
$$

$E _ { \mathrm { T D C } } ^ { \mathrm { c o o l } }$ captures the energy consumed by the J CRAC units, i.e.,

$$
E _ { \mathrm { T D C } } ^ { \mathrm { c o o l } } ( \lambda _ { \mathrm { T D C } } ) = \sum _ { j = 1 } ^ { J } E _ { j } ^ { \mathrm { c o o l } } ,
$$

where the cooling energy consumed by CRAC unit $j ,$ , denoted as $E _ { j } ^ { \mathrm { c o o l } }$ , is obtained by integrating (2) as,

$$
E _ { j } ^ { \mathrm { c o o l } } = \int _ { t _ { 1 } } ^ { t _ { 2 } } P _ { j } ^ { \mathrm { f a n } } + \frac { Q _ { j } ( t ) } { \mathrm { C O P } ( T _ { j } ^ { \mathrm { o u t } } ) } d t ,\tag{20}
$$

where $P _ { j } ^ { \mathrm { f a n } }$ is computed from

$$
P _ { j } ^ { \mathrm { f a n } } = \frac { \dot { V } \Delta p ^ { \mathrm { f a n } } } { \eta _ { j } ^ { \mathrm { f a n } } \eta _ { j } ^ { \mathrm { f a n , m o t o r } } } ,
$$

with $\dot { V }$ denoting the air flow rate of the CRAC unit, $\Delta p ^ { \mathrm { f a n } }$ is the pressure loss due to air flow resistances, $\eta _ { j } ^ { \mathrm { f a n } }$ and $\eta _ { j } ^ { \mathrm { f a n , m o t o r } }$ are the efficiencies of the fan and motor fan, respectively [36].

The heat removed by CRAC unit $a c _ { j }$ from $I _ { 1 } < I$ servers in the data center, i.e., $Q _ { j } ( t )$ is found from [9],

$$
Q _ { j } ( t ) = \sum _ { i = 1 } ^ { I _ { 1 } } \left( C _ { \mathrm { a i r } } ~ f _ { \mathrm { a i r } } \left( T _ { i } ^ { \mathrm { o u t } } ( t ) - T _ { i } ^ { \mathrm { i n } } ( t ) \right) \right) ,\tag{21}
$$

where $C _ { \mathrm { a i r } }$ is the air heat capacity, $f _ { \mathrm { a i r } }$ is the air flow rate through the server CPU; $T _ { i } ^ { \mathrm { i n } }$ and $T _ { i } ^ { \mathrm { o u t } }$ are respectively the inlet temperature and the outlet temperature of server $s _ { i } . \ T _ { i } ^ { \mathrm { i n } }$ is expressed as [10],

$$
T _ { i } ^ { \mathrm { i n } } ( t ) = T _ { j } ^ { \mathrm { o u t } } + \gamma + \left( T _ { i } ^ { \mathrm { i n } } ( 0 ) - T _ { j } ^ { \mathrm { o u t } } - \gamma \right) e ^ { - \nu t } ,\tag{22}
$$

where $T _ { i } ^ { \mathrm { i n } } ( 0 )$ is the initial inlet temperature of server $s _ { i } ; \gamma$ is the temperature raise imposed by the recirculated exhausted air in the data center and ν reflects the temperature influence of the closest CRAC. On the other handm, $T _ { i } ^ { \mathrm { o u t } }$ is found from [9],

$$
T _ { i } ^ { \mathrm { o u t } } ( t ) = \left( 1 - \frac { 1 } { C _ { \mathrm { a i r } } f _ { \mathrm { a i r } } R } \right) T _ { i } ^ { \mathrm { i n } } ( t ) + \frac { 1 } { C _ { \mathrm { a i r } } f _ { \mathrm { a i r } } R } T _ { i } ^ { \mathrm { C P U } } ( t ) ,\tag{23}
$$

where R is the thermal resistance of the CPU and $T _ { i } ^ { \mathrm { C P U } }$ is the CPU temperature such that [10], [37]

$$
\begin{array} { r l r } & { T _ { i } ^ { \mathrm { { C P U } } } ( t ) = T _ { i } ^ { \mathrm { { i n } } } ( t ) + R P _ { i } ^ { \mathrm { { c o m p } } } + \bigg ( T _ { i } ^ { \mathrm { { C P U } } } ( 0 ) - T _ { i } ^ { \mathrm { { i n } } } ( t ) - R P _ { i } ^ { \mathrm { { c o m p } } } \bigg ) } & \\ & { } & { \quad \quad \quad e ^ { - \frac { t } { R C _ { i } } } , } \end{array}
$$

where $T _ { i } ^ { \mathrm { C P U } } ( 0 )$ is the CPU temperature at the initial time and $C _ { i }$ is the server heat capacity. Substituting (22), (23) and (24) in (21) yields

$$
\begin{array} { r l r } {  { Q _ { j } ( t ) = \frac { 1 } { R } \sum _ { i = 1 } ^ { I _ { 1 } } ( R ( 1 - e ^ { - \frac { t } { R C _ { i } } } ) P _ { i } ^ { \mathrm { c o m p } } + ( T _ { i } ^ { \mathrm { C P U } } ( 0 ) - T _ { j } ^ { \mathrm { o u t } } - \gamma )  } } \\ & { } & {  e ^ { - \frac { t } { R C _ { i } } } - ( T _ { i } ^ { \mathrm { i n } } ( 0 ) - T _ { j } ^ { \mathrm { o u t } } - \gamma ) e ^ { - ( \nu + \frac { 1 } { R C _ { i } } ) t } ) . } \end{array}
$$

By substituting (25) in (20), $E _ { j } ^ { \mathrm { c o o l } }$ consumed by $a c _ { j }$ can be rewritten as,

$$
\begin{array} { l } { E _ { j } ^ { \mathrm { s o l t } } = \displaystyle \sum _ { s = 1 } ^ { I _ { 1 } } \frac { C _ { i } ( T _ { i } ^ { \mathrm { o u l } } ( 0 ) - T _ { j } ^ { \mathrm { o u t } } - \gamma ) ( e ^ { - \frac { t _ { \mathrm { o u t } } ^ { - } } { \mathrm { R e } } } - e ^ { - \frac { t _ { \mathrm { o u t } } ^ { s } } { \mathrm { R e } } } ) } { ( 1 0 0 0 8 ( \Gamma _ { j } ^ { \mathrm { o u t } } ) ^ { 2 } ) ^ { 2 } } } \\ { + \displaystyle \sum _ { s = 1 } ^ { I _ { 1 } } \frac { C _ { i } ( T _ { i } ^ { \mathrm { o u l } } ( 0 ) - T _ { j } ^ { \mathrm { o u t } } - \gamma ) ( e ^ { - ( \varepsilon + \frac { t _ { \mathrm { e v } } ^ { - } } { \mathrm { R e } } ) t _ { j } } - e ^ { - ( \varepsilon + \frac { t _ { \mathrm { e v } } ^ { - } } { \mathrm { R e } } ) t _ { 1 } } ) } { ( 1 0 0 0 8 \Gamma _ { i } ^ { \mathrm { o u t } } ) ^ { 2 } + ( 1 0 0 8 \Gamma _ { j } ^ { \mathrm { o u t } } ) ^ { 2 } } } \\ { + \displaystyle \sum _ { s = 1 } ^ { I _ { 1 } } \frac { C _ { i } ( T _ { i } ^ { \mathrm { o u l } } ( 0 ) - T _ { j } ^ { \mathrm { o u t } } - \gamma ) ( e ^ { - ( \varepsilon + \frac { t _ { \mathrm { e v } } ^ { - } } { \mathrm { R e } } ) t _ { 2 } } - e ^ { - ( \varepsilon + \frac { t _ { \mathrm { e v } } ^ { - } } { \mathrm { R e } } ) t _ { 1 } } ) } { ( 1 0 0 0 8 ( \Gamma _ { i } ^ { \mathrm { o u t } } ) ^ { 2 } + 0 . 0 0 8 \Gamma _ { j } ^ { \mathrm { o u t } } + 0 . 4 5 8 ) } } \\  + \displaystyle \sum _ { s = 1 } ^ { I _ { 1 } } \frac  ( P ^ { \mathrm { i n t } } + \frac  \lambda _  j  \end{array}\tag{26}
$$

By summing over (19) and (26), $E _ { \mathrm { T D C } } ^ { \mathrm { c o n s } } ( \lambda _ { \mathrm { T D C } } )$ can be re-written as,

$$
\begin{array} { r l } & { E _ { \mathrm { T D C } } ^ { \mathrm { c o n s } } ( \lambda _ { \mathrm { T D C } } ) = \displaystyle \sum _ { i = 1 } ^ { I + I ^ { \prime } } \bigg ( P ^ { \mathrm { i d l e } } + \frac { \lambda _ { i } \theta ^ { * } } { \mu } \left( P ^ { \mathrm { p e a k } } - P ^ { \mathrm { i d l e } } \right) \bigg ) ( t _ { 2 } - t _ { 1 } ) } \\ & { + \displaystyle \sum _ { j = 1 } ^ { J } P _ { j } ^ { \mathrm { f a n } } \left( t _ { 2 } - t _ { 1 } \right) } \end{array}
$$

$$
\begin{array} { r l } & { + \displaystyle \sum _ { s = 1 } ^ { { \frac { I + j } { n } } } C _ { s } ( \overline { { U _ { s } ^ { \mathrm { e f f } } ( \Omega ) - T _ { 3 } ^ { \mathrm { m a } } - \gamma ) \Big ( e ^ { - \frac { \mathrm { i } \kappa _ { \mathrm { f f } } } { n \Omega } } - e ^ { - \frac { \mathrm { i } \kappa _ { \mathrm { f f } } } { n \Omega } } \Big ) } }  } \\ & { +  \sum _ { s = 1 } ^ { \infty } ( \overline { { 0 . 0 0 6 8 ( T _ { 3 } ^ { \mathrm { m a } } ) ^ { 2 } } } + 0 . 0 1 8 \mathrm { I } \mathrm { T } _ { 3 } ^ { \mathrm { m a } } + 0 . 4 5 8 ) } \\ & { + \displaystyle \sum _ { s = 1 } ^ { { \frac { I + j } { n } } } C _ { s } ( \overline { { t _ { s } ^ { \mathrm { e f f } } ( \Omega ) - T _ { 3 } ^ { \mathrm { m a } } - \gamma } } ) ( e ^ { - ( \mathrm { i } + \kappa _ { \mathrm { e f f } } ^ { \mathrm { a } } ) \kappa _ { \mathrm { o } } } - e ^ { - ( \mathrm { i } + \frac { \kappa _ { \mathrm { e f f } } } { n \Omega } ) \kappa _ { \mathrm { o } } } ) } \\ & { + \displaystyle \sum _ { s = 1 } ^ { { \frac { I + j } { n } } } ( \nu \overline { { k _ { G } ^ { \mathrm { e f f } } ( 1 + 1 ) } } ( \overline { { 0 . 0 0 6 8 ( T _ { 3 } ^ { \mathrm { m a } } ) ^ { 2 } } } + 0 . 0 0 0 \overline { { 0 . 0 5 T _ { 3 } ^ { \mathrm { m a } } } } + 0 . 4 5 8 ) } \\ &  + \displaystyle \sum _ { s = 1 } ^ { { \frac { I + j } { n } } } ( \overline { { 0 . 0 0 6 8 ( \frac { \mathrm { i } \kappa _ { \mathrm { f f } } } { n \Omega } ) ^ { 2 } } } + 0 . 0 1 8 ) ( t _ { 2 } - t _ { 1 } \ \end{array}\tag{27}
$$

2) Energy Consumption in Data Center-Enabled HAP: The energy consumed by the data center-enabled HAP is expressed as a function of l, d and the processed workload $\lambda =$ $\dot { [ \lambda _ { \mathrm { H A P } } ^ { T } \lambda _ { \mathrm { T D C } } ^ { T } ] ^ { T } } \in \mathbb { R } ^ { I + I ^ { \prime } }$

$$
\begin{array} { r l } & { E _ { \mathrm { T D C - H A P } } ^ { \mathrm { c o n s } } ( \lambda , l , d ) = E _ { \mathrm { H A P } } ^ { \mathrm { p a y l o a d } } ( \lambda _ { \mathrm { H A P } } ) + E _ { \mathrm { H A P } } ^ { \mathrm { p r o p } } ( l , d ) } \\ & { + E _ { \mathrm { T D C - H A P } } ^ { \mathrm { t r a n s } } ( l , \lambda _ { \mathrm { H A P } } ) + E _ { \mathrm { T D C - H A P } } ^ { \mathrm { c o m p } } ( \lambda _ { \mathrm { T D C } } ) + E _ { \mathrm { T D C - H A P } } ^ { \mathrm { c o o l } } ( \lambda _ { \mathrm { T D C } } ) . } \end{array}\tag{28}
$$

Specifically, $E _ { \mathrm { T D C - H A P } } ^ { \mathrm { c o n s } }$ comprises the computational energy (19) and the cooling energy (26) besides the payload energy (15), the propulsion energy of the HAP (16) and the transmission energy. The transmission energy required to send the workload from the terrestrial data center to the HAP is expressed as [27]

$$
E _ { \mathrm { T D C - H A P } } ^ { \mathrm { t r a n s } } ( l , \lambda _ { \mathrm { H A P } } ) = \frac { \beta b ( \lambda _ { \mathrm { H A P } } ) } { R _ { \mathrm { H A P } } ( l ) } \left. q _ { \mathrm { H A P } } \right. _ { F } ^ { 2 } ( t _ { 2 } - t _ { 1 } ) ,\tag{29}
$$

where $\beta$ is the ratio of the transmitted data size to the original task data size due to the transmission overhead; b is the size of the input data (in bits) and $\| q _ { \mathrm { H A P } } \| _ { F } ^ { 2 }$ is the transmit power from the terrestrial data center to the HAP. The size of the input data b can be expanded as $\begin{array} { r } { b ( \lambda _ { \mathrm { H A P } } ) = \sum _ { i = I + 1 } ^ { I + I ^ { \prime } } ( \lambda _ { i } \theta ^ { \ast } b ^ { \ast } ) } \end{array}$ such that $b ^ { * }$ is the size of the instruction in bits.

By substituting (15), (16), (29) in (28) and summing over (19) and (26), the energy consumed by the data center-enabled HAP is re-written as

$$
\begin{array} { l } { { \displaystyle E _ { \mathrm { T I C } } ^ { \mathrm { c o n s } } \mathrm { e } ^ { ( \lambda , l , d ) = } v _ { \mathrm { w i d t } } ^ { \frac { 1 } { 2 } } ( l , d ) C _ { D } ^ { \prime } ( t _ { 2 } - t _ { 1 } ) } } \\ { { \displaystyle ~ + \frac { \beta b } { R _ { \mathrm { H A F } } ( l ) } \left\| q _ { \mathrm { H A F } } \right\| _ { F } ^ { 2 } ( t _ { 2 } - t _ { 1 } ) + \displaystyle \sum _ { j = 1 } ^ { J } P _ { j } ^ { \mathrm { f a n } } \left( t _ { 2 } - t _ { 1 } \right) } } \\ { { \displaystyle ~ + \sum _ { i = 1 } ^ { I + I ^ { \prime } } \left( P ^ { \mathrm { i d e } } + \frac { \lambda _ { i } \theta ^ { * } } { \mu } \left( P ^ { \mathrm { p a k } } - P ^ { \mathrm { i d e } } \right) \right) \left( t _ { 2 } - t _ { 1 } \right) } } \\ { { \displaystyle ~ + \sum _ { i = 1 } ^ { \frac { I } { \gamma } } \frac { C _ { i } \left( T _ { i } ^ { \mathrm { c p t } } ( 0 ) - T _ { 0 } ^ { \mathrm { g a t } } - \gamma \right) \left( e ^ { - \frac { t _ { 1 } } { R C _ { i } } } - e ^ { - \frac { t _ { 2 } } { R C _ { i } } } \right) } { \left( 0 . 0 0 6 8 \left( T _ { j } ^ { \mathrm { g a t } } \right) ^ { 2 } + 0 . 0 0 8 T _ { j } ^ { \mathrm { g a t } } + 0 . 4 5 8 \right) } } } \end{array}
$$

$$
\begin{array} { r l } & { \quad + \displaystyle \sum _ { i = 1 } ^ { \frac { 7 } { 7 } } \frac { C _ { i } \big ( T _ { i } ^ { \mathrm { i n } } ( 0 ) - T _ { j } ^ { \mathrm { u n } } - \gamma \big ) \big ( e ^ { - ( \nu + \frac { 1 } { \kappa C _ { i } } ) t _ { 2 } } - e ^ { - ( \nu + \frac { 1 } { \kappa C _ { i } } ) t _ { 1 } } \big ) } { ( \nu R C _ { i } + 1 ) \left( 0 . 0 0 6 8 \left( T _ { j } ^ { \mathrm { o u t } } \right) ^ { 2 } + 0 . 0 0 8 T _ { j } ^ { \mathrm { o u t } } + 0 . 4 5 8 \right) } } \\ & { \quad + \displaystyle \sum _ { i = 1 } ^ { \frac { 7 } { 7 } } \frac { \bigg ( P ^ { \mathrm { i d t } } + \frac { \lambda _ { i } \theta ^ { * } } { \mu } \big ( P ^ { \mathrm { p e a k } } - P ^ { \mathrm { i d t } } \big ) \bigg ) \left( t _ { 2 } - t _ { 1 } \right) } { 0 . 0 0 6 8 \big ( T _ { j } ^ { \mathrm { o u t } } \big ) ^ { 2 } + 0 . 0 0 8 T _ { j } ^ { \mathrm { o u t } } + 0 . 4 5 8 } } \\ & { \quad + \displaystyle \sum _ { i = 1 } ^ { \frac { 7 } { 7 } } \frac { \bigg ( P ^ { \mathrm { i d t } } + \frac { \lambda _ { i } \theta ^ { * } } { \mu } \big ( P ^ { \mathrm { p e a k } } - P ^ { \mathrm { i d t } } \big ) \bigg ) R C _ { i } \big ( e ^ { - \frac { t _ { 2 } } { \kappa C _ { i } } } - e ^ { - \frac { t _ { 1 } } { \kappa C _ { i } } } \big ) } { 0 . 0 0 6 8 \big ( T _ { j } ^ { \mathrm { o u t } } \big ) ^ { 2 } + 0 . 0 0 8 T _ { j } ^ { \mathrm { o u t } } + 0 . 4 5 8 } . } \end{array}\tag{30}
$$

We propose that using a data center-enabled high-altitude platform (HAP) is a more energy-efficient option compared to a terrestrial data center. This is because the HAP does not require cooling units, as the average temperature in the stratosphere is significantly lower than the recommended temperature for a data center. Additionally, the HAP utilizes solar energy harvested during the daytime and stored in Lithium-Sulphur batteries during the nighttime to power its servers, whereas a terrestrial data center relies on electric energy supplied through the electrical grid constantly. As a result, the energy saved by using the HAP can be expressed as the difference between the energy consumed by the HAP data center, denoted as $E _ { \mathrm { T D C - H A P } } ^ { \mathrm { c o n s } } ( \lambda , l , d )$ , and that consumed by the terrestrial data center, denoted as $E _ { \mathrm { T D C } } ^ { \mathrm { c o n s } } ( \lambda \mathrm { T D C } )$ , which can be written as $\begin{array} { r } { E ^ { \mathrm { s a v } } ( \lambda , l , d ) = E \mathrm { T D C - H A P } ^ { \mathrm { \bar { c } o n s } } ( \lambda , l , d ) - E _ { \mathrm { T D C } } ^ { \mathrm { c o n s } } ( \lambda _ { \mathrm { T D C } } ) } \end{array}$

## C. Outage Probability of Offloading

In this section, we investigate the outage probability of offloading workload to the data center-enabled high-altitude platform (HAP). Specifically, we analyze the scenario where the established transmission link between the terrestrial data center and the HAP cannot support the offloaded workload. As we assume that this link uses MIMO technology, we refer to the outage probability analysis of MIMO Rician fading channels presented in [38]. In [38], the authors derive a lower bound and an upper bound of the outage probability’s distribution by considering the trace of a non-central Wishart matrix derived from the channel matrix. Therefore, the upper bound $\mathrm { P r } _ { \mathrm { t r \_ U } }$ of the complementary cumulative distribution function (CCDF) of the data rate for the transmission link to the HAP is given by [38]

$$
\operatorname* { P r } \left( R _ { \mathrm { H A P } } > \lambda \right) \le \operatorname* { P r } _ { \mathrm { t r _ { - } U } } ( \lambda ) = Q _ { M N } \left( \sqrt { 2 \delta ^ { \prime } } , \sqrt { 2 a N \left( 2 ^ { \frac { \lambda } { N } } - 1 \right) } \right) ,\tag{31}
$$

where $\lambda = \sum \lambda _ { \mathrm { H A P } }$ is the total offloaded workload, $\delta ^ { \prime } =$ $\zeta \| \overline { { H } } _ { \mathrm { H A P } } \| _ { F } ^ { 2 }$ is the non-centrality parameter, $\begin{array} { r } { a = \frac { 1 + \zeta } { n ^ { \prime } } } \end{array}$ with $\eta ^ { \prime }$ defined as the average signal to noise ration (SNR) at each receive antenna and $Q _ { M N } ( a , y )$ is the generalized Marcum Q-function of order $M \times N$ given by

$$
Q _ { M N } ( a , y ) = \int _ { y } ^ { \infty } x \left( { \frac { x } { a } } \right) ^ { M N - 1 } e ^ { - { \frac { ( x ^ { 2 } + a ^ { 2 } ) } { 2 } } } I _ { M N - 1 } ( a x ) d x ,\tag{32}
$$

with $I _ { M N - 1 }$ is denoting the modified Bessel function of the first kind of order $M N - 1$

Moreover, the lower bound $\mathrm { P r } _ { \mathrm { t r \perp } }$ <sub>L</sub> of the CCDF of the HAP data rate is given by [38]

$$
\operatorname* { P r } ( R _ { \mathrm { H A P } } > \lambda ) \ge \operatorname* { P r } _ { \mathrm { t r } _ { - } \mathrm { L } } ( \lambda ) = Q _ { M N } \left( \sqrt { 2 \delta ^ { \prime } } , \sqrt { 2 a \left( 2 ^ { \lambda } - 1 \right) } \right)\tag{33}
$$

Given the upper bound and the lower bound of the CCDF of the HAP data rate, we investigate the dropping rate of the data center-enabled HAP; which is given by

$$
\operatorname* { P r } _ { \mathrm { d r o p } } ( \lambda ) = 1 - \operatorname* { P r } ( R _ { \mathrm { H A P } } > \lambda ) .\tag{34}
$$

To mitigate this dropping rate, the dropped workload can be re-transmitted thanks to the energy saved by the data centerenabled HAP (as studied in the previous sub-section). Accordingly, the number of re-transmissions $N _ { \mathrm { r } }$ can be expressed as a function of the dropped workload $\lambda ^ { \mathrm { d r o p } }$ as follows:

$$
N _ { \mathrm { r } } = \left\{ \begin{array} { l l } { \left\lceil \frac { E ^ { \mathrm { s a v } } ( \lambda ) } { E _ { \mathrm { T D C - H A P } } ^ { \mathrm { t r a n s } } ( \lambda ^ { \mathrm { d r o p } } ) } \right\rceil , } & { \mathrm { i f } \lambda \geq \lambda ^ { \mathrm { d r o p } ^ { \ast } } , } \\ { 0 , } & { \mathrm { o t h e r w i s e } . } \end{array} \right.\tag{35}
$$

with $\lambda ^ { \mathrm { d r o p ^ { * } } }$ denotes the maximum workload arrival with no dropped workload such that $\operatorname* { P r } ( R _ { \mathrm { H A P } } > \lambda ) = 1 , \forall \lambda \le \lambda ^ { \mathrm { d r o p } ^ { * } }$

## D. Delay in Data Center-Enabled HAP

In this section, we analyze the delay D that occurs in a data center-enabled high-altitude platform (HAP) system. This delay is primarily composed of two components: the waiting time, also known as the queuing time, denoted as $\mathcal { W } _ { i }$ , for each task to be executed on server $s _ { i } ,$ , and the round trip time (RTT) required to send the task to the HAP and receive the execution result, such that $\mathcal { D } = \overline { { \mathcal { W } _ { i } } } + \mathcal { R } \mathcal { T } \mathcal { T }$ . The RTT is determined by the transmission delay and can be expressed as follows:

$$
\mathcal { R T T } ( l , \lambda _ { \mathrm { H A P } } ) = 2 t _ { \mathrm { t r a n s } } ( l , \lambda _ { \mathrm { H A P } } ) = \frac { 2 b ( \lambda _ { \mathrm { H A P } } ) } { R _ { \mathrm { H A P } } ( l ) } .\tag{36}
$$

In order to calculate the mean waiting time, we model the server as an M/G/1 queue with vacations, since the server enters an idle mode when there are no tasks to be executed. Our approach closely follows the standard derivations for M/G/1 queues, as described in [39], [40], [41]. Specifically, we employ the following:

\- the arriving workload follows a Poisson process with rate $\lambda _ { i } .$

\- the service time distribution is general because the control commands are assumed to be random.

We are interested in obtaining the mean waiting time $\overline { { \mathcal { W } _ { i } } }$ at server $s _ { i }$ and its second moment $\overline { { \mathcal { W } _ { i } ^ { 2 } } }$ . The waiting time of task k scheduled after $K ^ { \prime }$ tasks is given by $\begin{array} { r } { \mathcal { W } _ { i } = \sum _ { k ^ { \prime } = 1 } ^ { K ^ { \prime } } \mathcal { X } _ { i } ^ { k ^ { \prime } } + \mathcal { R } _ { i } ; } \end{array}$ where $\mathcal { X } _ { i } ^ { k ^ { \prime } }$ is the service time of task $k ^ { \prime }$ that arrived before task k at server $s _ { i }$ and $\mathcal { R } _ { i }$ is the residual service time of server $s _ { i } . \mathcal { R } _ { i }$ can be either residual service time $\mathcal { R } _ { i } ^ { \mathrm { s } }$ or residual vacation time $\mathcal { R } _ { i } ^ { \mathrm { v } }$ depending on utilization. The first moment of this residual time can then be written as

$$
\overline { { \mathcal { R } _ { i } } } = \overline { { \mathcal { R } _ { i } ^ { \mathrm { s } } } } + \overline { { \mathcal { R } _ { i } ^ { \mathrm { v } } } } = \frac { 1 } { 2 } \left( u _ { i } \frac { \overline { { X _ { i } ^ { 2 } } } } { \overline { { X _ { i } } } } + \left( 1 - u _ { i } \right) \frac { \overline { { V _ { i } ^ { 2 } } } } { \overline { { V _ { i } } } } \right)
$$

$$
= { \frac { 1 } { 2 } } \left( \lambda _ { i } { \overline { { X _ { i } ^ { 2 } } } } + ( 1 - u _ { i } ) { \frac { \overline { { V _ { i } ^ { 2 } } } } { \overline { { V _ { i } } } } } \right) ;\tag{37}
$$

where $u _ { i }$ is the utilization ratio of server $s _ { i } , \ { \overline { { V _ { i } } } }$ is the mean vacation time duration at server i and $\overline { { V _ { i } ^ { 2 } } }$ is the second moment of vacation time duration at server i. By applying Little’s formula, we obtain the average waiting time as follows:

$$
\overline { { \mathcal { W } _ { i } } } = \frac { \overline { { \mathcal { R } _ { i } } } } { 1 - u _ { i } } = \frac { \lambda _ { i } \overline { { X _ { i } ^ { 2 } } } } { 2 \left( 1 - u _ { i } \right) } + \frac { \overline { { V _ { i } ^ { 2 } } } } { 2 \overline { { V _ { i } } } } .\tag{38}
$$

## E. Complexity Analysis

In this subsection, we analyze the complexity of the proposed data center enabled HAP system and we discuss its feasibility for implementation in a realistic setup. The complexity analysis considers various factors that include the computational complexity, the communication complexity and the deployment complexity.

1) Computational Complexity: To assess the computational complexity of the proposed framework, we consider the time and resources required to process the offloaded workload form the terrestrial data center. The energy saving complexity of our proposed framework can be evaluated as $O ( \frac { \bar { \lambda } \times \bar { N } } { \mu } )$ where λ is the workload arrival rate N is the total number of servers in the system and $\mu$ is the server capability. The time complexity of our proposed framework can be evaluated as $\mathcal { O } ( \frac { \lambda \times \bar { N } } { \mu ^ { 2 } } ) ;$ ; where we consider the waiting time and the offloading time of the tasks to the HAP. We notice the trade-off between the energy saving offered by the HAP-enabled system and the increased computational requirements due to the limited resources available on the HAP. Specifically, the more servers are deployed in the HAP with increasing workload offloading, the more energy is saved in the terrestrial data center. However, this strategy impacts resource utilization since energy consumption is strongly coupled to servers’ capabilities. Accordingly, over-utilization and under-utilization of the flying servers must be avoided during resource’ provisioning and allocation [24].

2) Communication Complexity: The communication complexity of the proposed framework involves the analysis of the communication links between the terrestrial data centers and the HAP. This includes the evaluation of the bandwidth requirements, signal propagation delays and the reliability of these links through the outage probability as studied in Section III-C. We can model the communication complexity by using a combination of metrics such as the bit error rate (BER), signal-to-noise ratio (SNR) and throughput.

3) Deployment Complexity: The deployment complexity of the proposed framework involves the practical challenges associated with deploying and maintaining HAPs in the stratosphere. This complexity encompasses the HAP positioning and buoyancy control; which are tightly related to weather conditions in the stratosphere determined mainly by the wind speed. Moreover, this complexity includes the use of sophisticated and resilient electronic devices in the flying servers to guarantee their operation in the low temperature of the stratosphere and afford a reliable computing service. The deployment complexity involves also the regulatory rules; which impose strict conformity with the standards of design, transport and operation to guarantee airships’ safety in the stratosphere.

TABLE II SIMULATION SETTINGS
<table><tr><td rowspan=1 colspan=1>Type</td><td rowspan=1 colspan=2>Parameter</td><td rowspan=1 colspan=1>Numerical Value</td></tr><tr><td rowspan=1 colspan=1>Cooling/ThermalInputs[10]</td><td rowspan=1 colspan=2>Supply TemperatureServer Initial TemperatureCPU Initial TemperatureThermal ResistanceServer Heat Capacity</td><td rowspan=1 colspan=1>299.15 K310 K318 K0.34 K/W340 J/K</td></tr><tr><td rowspan=1 colspan=1>HAPInputs[31], [32]</td><td rowspan=1 colspan=2>Area of the PVEfficiency of the PVPropeller efficiencyAir DensityDynamic Air Viscosity</td><td rowspan=1 colspan=1> $8 0 0 0 { \mathrm { m } } ^ { 2 }$ 0.40.8 $0 . 0 8 8 9 1 k g / m ^ { 3 }$  $1 . 4 2 2 . 1 0 ^ { - 5 } \ N . s / m ^ { 2 }$ </td></tr><tr><td rowspan=1 colspan=1>Trans-mission</td><td rowspan=1 colspan=2>Antennas in TDCAntennas in HAP</td><td rowspan=2 colspan=1>21631 GHz100 MHz</td></tr><tr><td rowspan=1 colspan=1>Inputs[27]</td><td rowspan=1 colspan=2>Channel Bandwidth</td><td rowspan=1 colspan=1>arrier Frequency</td></tr></table>

In summary, the complexity analysis of the proposed framework demonstrates its feasibility for implementation in a realistic setup while considering the important trade-offs. The energy savings and environmental benefits offered by the data center enabled HAP outweigh the computational and communication complexity. Moreover, the deployment challenges can be addressed through technological advancements and regulatory efforts.

## IV. RESULTS AND DISCUSSION

In this section, we consider a stratospheric airship-based highaltitude platform (HAP) that has a significant surface area and can harvest notable amounts of solar energy. We assume that the HAP can support a maximum payload of 450 kg, similar to the Stratobus airship HAP [26], [42]. Additionally, we assume that the hosted data center has a rack weight of 363 kg [43], with each server in the rack characterized by a service rate of μ = 580 MIPS and a weight of approximately 9 kg [43]. The remaining parameters used in our simulations are detailed in Table II.

Throughout our numerical results, we employ the derived expressions in Section III to quantify the performance gain of the data center-enabled HAP compared to a terrestrial data center under various operational conditions. To analyze the scalability of our solution, we consider various workload scenarios including the homogeneous workload and heterogeneous workload. The considered workload model in each scenario has a wide range of arrival rates throughout all the conducted simulations. The homogeneous workload scenario involves workloads with the same characteristics in terms of task’s size. The heterogeneous workloads scenario involves workloads characterized with small task length and workloads characterized with large task length. For each workload scenario, we investigate the data center enabled HAP’s ability to handle the increased demand by augmenting the workload arrival rate without significantly impacting the performance metric.

![](images/c2fe91b4efd5746109bd2c3abd6589a7a62cab1a86403a7fcadcc832d82fd28a.jpg)

Southern Hemisphere (Latitude=-20)  
![](images/fa072cbf0c3f3f35fe7c55846f8fdbc38826243075809df3ded62f4d4bd9ae42.jpg)  
Fig. 2. Maximum workload arrival rate under the HAP flying condition.

We consider four simulation scenarios to investigate the impact of HAP location over the course of a year, workload arrival rate, and the number of servers present in the HAP on the relative performance gain. First, we verify the HAP’s flying condition in the homogeneous workload scenario by monitoring the energy balance based on the number of servers in the HAP and the maximum workload arrival rate. Second, we evaluate the energy efficiency of the data center-enabled HAP by assessing the saved energy for different latitudes throughout the year. To further validate the scalability of our proposed framework, we consider the deployment of a constellation of HAPs along with the terrestrial data center. Third, we explore the impact of re-transmitting dropped tasks in case of link outage on system performance for heterogeneous workload scenario. Finally, we analyze the delay experienced in the data center-enabled HAP by comparing the queuing delay, i.e., the waiting time, to the transmission delay in the heterogeneous workload scenario.

## A. HAP Flying Condition

The first simulation example investigates the workload arrival rate, i.e., λ<sup>max</sup>, that maintains the HAP flying condition versus the number of HAP servers, i.e., I<sup></sup>, for different locations and time along the year, as depicted in Fig. 2. It is necessary to consider the physical capacity of our system beforehand. Specifically, the maximum payload supported by the HAP imposes a limit on the maximum number of servers hosted in the HAP, as shown in Fig. 2. Moreover, the server’s service rate characteristic μ combined with the desired utilization ratio u dictate a limit on the supported workload. Since we want to leverage the full performance of the HAP, we assume that the HAP is fully occupied and consider the Maximum HAP Payload limit in our simulations. Moreover, we suppose that the servers hosted in the HAP are fully-utilized by imposing that u ≈ 100%. This maximum utilization ratio yields a High-load Threshold for the workload arrival rate, as shown in Fig. 2; beyond which the servers are dysfunctional.

We observe first from Fig. 2 that the harvested energy is underutilized when the number of airborne servers is low because the desirable utilization ratio u restricts the accepted workload. For instance, the supported maximum arrival rate in the Northern Hemisphere is around 2,600 task/s for ten servers on December Solstice. However, the actual server capacity of the server is below 1,000 task/s even when it is highly loaded. Therefore, the number of servers in the HAP should be increased to utilize the harvested energy fully. However, there is a limitation on the maximum number ofairborne servers according to the supported HAP payload. Indeed, we notice that the harvested energy and the servers’ capacity are ideally utilized when the number of servers reaches the maximum HAP payload. Moreover, we notice a lower maximum arrival rate allowed per server when more servers are present in the HAP. This observation is because the same number of tasks can be distributed and processed by more servers to maintain the flying condition. Otherwise, the harvested energy would not cover the payload energy, which is equivalent to the computational energy of the servers. We also notice an opposite behavior for the maximum arrival rate when comparing the Northern hemisphere to the Southern hemisphere. For instance, in the Northern hemisphere, more tasks are accepted during June than December solstice. However, more tasks are carried out in the Southern hemisphere during December than June solstice. This observation is because the solar radiation and the daylight duration are more critical during June in the Northern hemisphere; because the Northern hemisphere is closer to the Sun during June. However, the solar radiation and the daylight duration are more critical during December in the Southern hemisphere because the Southern hemisphere is closer to the Sun during December. Therefore, more solar energy can be harvested during June in the Northern hemisphere and December in the Southern hemisphere. Hence, more computational energy can be covered, and accordingly, more tasks can be processed in the HAP during June in the Northern hemisphere and December in the Southern hemisphere.

Since HAPs are designed to operate for long-duration missions, we assume that the full payload is used when the airship is launched, and we study the maximum workload arrival rate variation according to days and latitudes. We note that it is crucial to consider the High-load Threshold imposed by the desirable utilization ratio of the servers. Indeed, as depicted in Fig. 3, the servers tend to be over-utilized around June solstice in the Northern hemisphere and under-utilized in the Southern hemisphere if the utilization ratio is overlooked. More generally, the servers’ computational capacity is better utilized with higher latitudes in both hemispheres. Moreover, we notice that the maximum arrival rate reaches on June solstice its maximum point in the Northern hemisphere and its minimum point in the Southern hemisphere. The explanation of this observation was deeply detailed in the previous paragraph. We notice also that the maximum arrival rate increases with latitudes in the Southern hemisphere. In the Northern hemisphere, the maximum arrival rate decreases with latitudes when $d \in [ 1 , 1 0 0 ] \cup [ 2 5 0 , 3 6 6 ]$ and increases with latitudes when $d \in [ 1 0 0 , 2 5 0 ]$ . It is worthy to mention that the zigzag course of the curves is due to the expression of the solar radiation intensity given in (7). We notice also that the maximum arrival rate has less variations around the equator compared to the other latitudes along the year. Indeed, for high latitudes, the maximum arrival rate is less dynamic and is around the full capacity of the servers during different periods of the year. This observation is important because it shed light into the workload management along the year given the long-duration of HAP’s missions.

![](images/bbb5250927e1e257debc63d54a41c15e3d7eefe03c9625fb870b964faf16fa1e.jpg)  
Fig. 3. Maximum workload arrival rate under the HAP flying condition. $( I ^ { \prime } =$ 40).

## B. Energy Saving

After checking the HAP flying condition and determining the maximum arrival rate for different days and latitudes, we explore the energy-saving capabilities of the data center-enabled HAP. This simulation evaluates the consumed energy for the maximum workload arrival rate relative to different latitudes and days. First, we study the consumed energy variation for both data center-enabled HAP and terrestrial data centers versus the latitude for day number 150 in the year, as depicted in Fig. 4. We observe first that the consumed energy decreases with latitude because more workload can be accepted and hence covered by the HAP’s harvested energy. We also notice that the data centerenabled HAP helps to reduce the consumed energy for a large range of latitude $[ - 6 0 ^ { \circ } , 6 0 ^ { \circ } ]$ ]. We assess the saved energy rate $E ^ { \mathrm { s a v } } ( \% ) = 1 4 . 6 1 \\\\\%$ achieved for the maximum workload arrival rate $\lambda ^ { \mathrm { m a x } }$ when the latitude is around $6 0 ^ { \circ }$ for one HAP. Higher energy saving rates can be reached with a lower arrival rate $\lambda < \lambda ^ { \mathrm { m a x } }$ . We also note that if a larger payload can be supported by the HAP (increased by ten servers), higher energy saving can be recorded (increased by 3%). Indeed, a more important workload amount can be processed in the HAP in this case, which reduces the cooling energy consumption and yields higher energy savings.

![](images/b6d65f74c9aeab3e8a864ab05032f3802f7ff76d0b1d142f2c385f7ff855a66b.jpg)  
Fig. 4. Energy consumption according to Latitude’s variation.

![](images/048a425c9e89a0f6bbb4c6ebeafcf8b93faccda594a8bef66a776e5a69682143.jpg)  
Fig. 5. Energy consumption according to Day’s variation.

Then, we study the consumed energy variation according to different days in the year, as shown in Fig. 5. The least consumed energy record is at the middle of the year for the data centerenabled HAP. This observation is because the beginning and the end of the year are characterized by cold weather (the Winter season), where the ambient temperature reaches its lowest levels. Hence, less solar energy can be harvested by the HAP. However, the days around 200th day belong to Summer; where more solar energy can be collected within the data center-enabled HAP. We also notice that the data center-enabled HAP helps to reduce the consumed energy with an energy-saving rate $E ^ { \mathrm { s a v } } ( \% ) = 1 4 . 3 8 \%$ achieved for the maximum workload arrival rate $\lambda ^ { \mathrm { m a x } }$ around the 200th of the year. These saving rates can be substantially enhanced with the deployment of more HAPs. For instance, the saving rate exceeds 17% starting from 2 HAPs deployment along with the terrestrial data center.

![](images/cef42b58ccdab93eb35a89f241784b84e61c2f7220f72f3e4c199d6cf63ab66a.jpg)  
Fig. 6. Outage probability of the arriving workload.

## C. Outage Probability of Offloading

This simulation studies the outage probability of the communication links between terrestrial and HAP-based data centers. To this end, we plot the upper bound (31) and lower bound (33) outage probabilities respectively, versus the workload arrival rates, as illustrated in Fig. 6. We note that the partial dropping of some tasks might start at a workload arrival rate around $\lambda _ { \mathrm { p a r t i a l } } ^ { \mathrm { L B } } = 3 6 0$ task/s by considering the lower bound and at a workload arrival rate around $\lambda _ { \mathrm { p a r t i a l } } ^ { \mathrm { U B } } = 6 5 0$ task/s by considering the upper bound. Hence, $\lambda ^ { \mathrm { d r o p } ^ { * } } = 3 6 0$ task/s (c.f. (35)). The total dropping of the arriving tasks starts at a workload arrival rate around $\lambda _ { \mathrm { t o t a l } } ^ { \mathrm { L B } } = 4 0 0$ task/s by considering the lower bound and at a workload arrival rate around $\lambda _ { \mathrm { t o t a l } } ^ { \mathrm { U B } } = 7 \bar { 3 } 0$ task/s by considering the upper bound. We also study the impact of the mean task length on the outage probability. As depicted in Fig. 6, we notice that the outage probability is more important for a higher task length because of more data (b in bits (29)) is carried on the transmission link for the same workload arrival rate.

Given the outage probability and the saved energy findings, we can investigate the tasks’ retransmission impacts on the saved energy to the HAP. Therefore, we study the saved energy variation according to the workload arrival rate in two cases. In the first case, the dropped workload is processed in the terrestrial data center, while in the second case, we consider that the dropped workload is re-transmitted to the HAP. As shown in Fig. 7, if the dropped workload is not re-transmitted to the HAP, the saved energy percentage decreases notably with high arrival rates. Interestingly, the saved energy through a data center-enabled HAP is around 9% even when the workload is partially processed in the flying data center. However, under the re-transmission assumption, the saved energy becomes around

![](images/5d1f400334ba7b124dea9c5eeab51050c75c05116456bf7bd5ea7d955020795d.jpg)  
Fig. 7. Saved energy in the case of re-transmission to HAP.

11.76%, which achieves almost the same performance in the case of zero outage. This observation highlights that the saved energy is not impacted even for high data rates because the transmission energy is significantly lower than the cooling energy.

## D. Delay in Data Center-Enabled HAP

In this simulation, we study the mean waiting time (38) in our system. Therefore, we approximate the general distribution of the considered queuing model to an exponential service time distribution with a mean service rate $\mu _ { \mathrm { s } }$ and an exponential vacation time distribution with a mean vacation rate $\mu _ { \mathrm { v } }$ . Accordingly, the first moment of the residual service time can be simplified, based on (37), as follows:

$$
\overline { { \mathcal { R } _ { i } } } = \frac { \lambda _ { i } } { \mu _ { \mathrm { s } } ^ { 2 } } + \frac { ( 1 - u _ { i } ) } { \mu _ { \mathrm { v } } } \ : .\tag{39}
$$

By using this approximation, we compare the mean waiting time obtained through the analysis in Section III-D to the simulation results of an M/M/1 queue model with vacations where the service rate is $\mu _ { \mathrm { s } }$ and the vacation rate is $\mu _ { \mathrm { v } }$ . Therefore, we study the mean waiting time according to the variation of the workload arrival rate in both cases. As depicted in Fig. 8, the analytical results coincide with the simulation results for different workload arrival rates. Indeed, the difference between both curves $| \overline { { W _ { i } } } ^ { \mathrm { a n a l y s i s } } - \overline { { W _ { i } } } ^ { \mathrm { s i m u l a t i o n } } | \leq 1 0 ^ { - 6 }$ as zoomed out for the values of workload arrival rates around 700 task/s. We notice also that higher delays are attained when the workload arrival rate increases because more tasks should be waiting before their processing.

Therefore, we study the experienced delay in a data centerenabled HAP according to the variation of the workload arrival rate. As depicted in Fig. 9, we notice that this comparison depends on the mean task length of the arriving workload. For instance, the queuing delay is notably more significant than RTT for different arrival rates in the case of small task length. These results indicate that the tasks’ transmission and the re-transmission to the HAP can occur without affecting the experienced delay for a workload characterized by a small task length. However, the queuing delay is sometimes lower than RTT for a given range of arrival rates in the case of large task length. These results indicate that the tasks’ transmission and re-transmission to the HAP should be carefully studied for a workload characterized with a large task length because it depends on the arrival rate. For example, the queuing delay is close to RTT for an arrival rate 500 task/s ≤ λ ≤ 2250 task/s as depicted in Fig. 9. Therefore, the tasks’ transmission to the HAP will add an additional and substantial delay to the queuing delay in this case. But, the queuing delay becomes higher than RTT for an arrival rate 2250 task/s ≤ λ ≤ 3000 task/s as depicted in Fig. 9. We note that the difference is not important, though, and would limit the number of re-transmitted tasks in the case of an outage.

![](images/421a3784a11c972a0719fd780f3a62b896f397c253b37681b7f6cffa7248c4af.jpg)  
Fig. 8. Mean waiting time variation according to the arriving workload.

![](images/3265907bf01d026411c9cccc0e0ce7c666a9c19c6fff7f083d0032e1f842ffbb.jpg)  
Fig. 9. Comparison between the Queuing Delay and the Transmission Delay

## V. CONCLUSION

Throughout this study, the authors have explored the potential of using a data center-enabled HAP system as a green alternative to traditional terrestrial data centers. Their analysis shows that the naturally low temperature and solar power available in the stratosphere make the HAP an ideal environment for flying data centers. The authors have established the limits of our system in terms of payload capacity and server utilization ratio to determine the optimal workload arrival rate to the HAP. Their study also demonstrates the energy-saving benefits of using a data center-enabled HAP compared to traditional terrestrial data centers under various workload settings, locations, and periods of the year. They have found that energy savings can be further improved by reducing the workload arrival rate to the HAP or increasing the number of servers hosted in the HAP. To increase system reliability and save more energy, reliable communication links are necessary to re-transmit dropped workloads to the HAP. Additionally, the authors have shown that the distribution of servers between terrestrial data centers and the data center-enabled HAP has no significant impact on the transmission and re-transmission delay for workloads with low task length. However, careful design of workload scheduling is essential to take full advantage of the benefits offered by the HAP system. Overall, our findings suggest that a data centerenabled HAP system presents a promising solution for reducing energy consumption and mitigating the environmental impact of traditional terrestrial data centers. Their study provides valuable insights into the potential benefits of this innovative computing paradigm and highlights the need for continued research in this area.

## A. Research Challenges

However, it is important to explore the potential research challenges towards a comprehensive study. Therefore, the technical challenges of the data center enabled-HAP should be investigated. For instance, the unfriendly weather conditions in the stratosphere impose the deployment of adapted and more resilient electronic devices in the flying data center. Also, the frequency’s maintenance of the airship and the flying servers is crucial to balance the trade-off between the quality of the offered computing service and the HAP’s mission duration. Moreover, the economic viability of the data center enabled HAP should be considered. Capital expenditures such as the costs of the HAP platform and aerial servers, as well as operational expenditures like energy costs, must be assessed to evaluate profitability. Accordingly, a dynamic computing pricing model for the HAP is needed. Prices should adjust based on demand and network conditions to provide a satisfactory quality of experience for users while maximizing utilization of HAP resources and ensuring profitability [44]. Specifically, lower prices can be initially offered to encourage offloading to the HAP during off-peak periods. However, as the arrival rate approaches the HAP’s capacity, prices should increase to throttle demand or incentivize offloading some traffic to terrestrial data centers, which can offer lower prices during peak periods.

## B. Future Directions

To tackle these challenges and improve the performance of the data center enabled-HAP, Their future work will be based on different approaches of machine learning. For instance, meta learning can be useful to optimize the workload/network management policies in the flying data center hosted in the HAP. One way to boost the self-organization of the data center-enabled HAP network is to adopt meta-learning. Meta learning can be used in the data center-enabled HAP to learn from the output of the machine learning algorithms commonly used to optimize the network management policies in the terrestrial data center. Then, the generated models can be applied in the flying data center hosted in the HAP. These advantages are particularly valuable in the HAP because the learning process is accelerated and hence more computational energy is saved. Moreover, it is valuable to predict the highly-dynamic workload arriving at the data center by using federated learning. Federated learning can play a crucial role in predicting the workload incoming to the data center in the briefest delays without violating data privacy and less exchanging plain text data to ensure security. Indeed, federated learning can be applied within the different servers of one data center, geographically distributed sites of the same data center, or even within other data centers by only sending the prediction results and models. Accordingly, the predicted workload should be effectively scheduled spatially and temporally to leverage the renewable energy. Moreover, the renewable energy usage can be alternated with the fossil energy usage in a data center enabled-HAP when the appropriate workload amount is offloaded to the HAP; while fulfilling the QoS requirements and respecting the physical capabilities of the data center enabled-HAP.

## REFERENCES

[1] N. S. Hogade, S. Pasricha, and H. J. Siegel, “Energy and network aware workload management for geographically distributed data centers,” IEEE Trans. Sustain. Comput., vol. 7, no. 2, pp. 400–413, Second Quarter 2022.

[2] Gartner, Gartner forecasts worldwide it spending to grow 5.5% in 2023. 2023. [Online]. Available: https://www.gartner.com/en/newsroom/pressreleases/2023-04-06-gartner-forecasts-worldwide-it-spending-to-grow-5-percent-in-2023

[3] M. Dayarathna, Y. Wen, and R. Fan, “Data center energy consumption modeling: A survey,” IEEE Commun. Surveys Tut., vol. 18, no. 1, pp. 732–794, First Quarter 2016.

[4] K. Kaur, S. Garg, G. Kaddoum, E. Bou-Harb, and K.-K. R. Choo, “A big data-enabled consolidated framework for energy efficient software defined data centers in IoT setups,” IEEE Trans. Ind. Informat., vol. 16, no. 4, pp. 2687–2697, Apr. 2020.

[5] M. Aslani, O. Amin, F. Nawab, and B. Shihada, “Rethinking blockchain integration with the industrial Internet of Things,” IEEE Internet ofThings Mag., vol. 3, no. 4, pp. 70–75, Dec. 2020.

[6] W. Abderrahim, O. Amin, M.-S. Alouini, and B. Shihada, “Proactive traffic offloading in dynamic integrated multisatellite terrestrial networks,” IEEE Trans. Commun., vol. 70, no. 7, pp. 4671–4686, Jul. 2022.

[7] V. Dukic et al., “Beyond the mega-data center: Networking multi-data center regions,” in Proc. Annu. Conf. ACM Special Int. Group Data Commun. Appl., Technol. Architectures, Protoc. Comput. Commun., 2020, pp. 765–781.

[8] J. Wan, J. Zhou, and X. Gui, “Sustainability analysis of green data centers with cchp and waste heat reuse systems,” IEEE Trans. Sustain. Comput., vol. 6, no. 1, pp. 155–167, First Quarter 2021.

[9] Y. Berezovskaya, C.-W. Yang, A. Mousavi, V. Vyatkin, and T. B. Minde, “Modular model of a data centre as a tool for improving its energy efficiency,” IEEE Access, vol. 8, pp. 46 559–46 573, 2020.

[10] X. Li, P. Garraghan, X. Jiang, Z. Wu, and J. Xu, “Holistic virtual machine scheduling in cloud datacenters towards minimizing total energy,” IEEE Trans. Parallel Distrib. Syst., vol. 29, no. 6, pp. 1317–1331, Jun. 2018.

[11] X. Hu et al., “Joint workload scheduling and energy management for green data centers powered by fuel cells,” IEEE Trans. Green Commun. Netw., vol. 3, no. 2, pp. 397–406, Jun. 2019.

[12] S. Albers, “On energy conservation in data centers,” ACM Trans. Parallel Comput., vol. 6, no. 3, pp. 1–26, 2019.

[13] Thales, China energy transition status report 2021. 2021. [Online]. Available: http://english.www.gov.cn/statecouncil/ministries/202112/09/ content\_WS61b13edac6d09c94e48a1f81.html

[14] Gartner, Gartner predicts 75% of organizations will have implemented a data center infrastructure sustainability program by 2027. 2023. [Online]. Available: https://www.gartner.com/en/newsroom/pressreleases/2023-05-02-gartner-predicts-75-percent-of-organizations-willhave-implemented-a-data-center-infrastructure-sustainability-programby-2027

[15] L. Ismail and H. Materwala, “Computing server power modeling in a data center: Survey, taxonomy, and performance evaluation,” ACM Comput Surv., vol. 53, no. 3, pp. 1–34, 2020.

[16] C. S. Chan, A. S. Akyürek, B. Aksanli, and T. Š. Rosing, “Optimal performance-aware cooling on enterprise servers,” IEEE Trans. Comput.- Aided Design Integr. Circuits Syst., vol. 38, no. 9, pp. 1689–1702, Sep. 2019.

[17] Z. Zhou, F. Liu, R. Zou, J. Liu, H. Xu, and H. Jin, “Carbon-aware online control of geo-distributed cloud services,” IEEE Trans. Parallel Distrib. Syst., vol. 27, no. 9, pp. 2506–2519, Sep. 2016.

[18] N. Hogade, S. Pasricha, H. J. Siegel, A. A. Maciejewski, M. A. Oxley, and E. Jonardi, “Minimizing energy costs for geographically distributed heterogeneous data centers,” IEEE Trans. Sustain. Comput., vol. 3, no. 4, pp. 318–331, Fourth Quarter 2018.

[19] A. Wierman, L. L. Andrew, and A. Tang, “Power-aware speed scaling in processor sharing systems,” in Proc. IEEE Conf. Comput. Commun., 2009, pp. 2007–2015.

[20] Z. Liu, M. Lin, A. Wierman, S. Low, and L. L. Andrew, “Greening geographical load balancing,” IEEE/ACM Trans. Netw., vol. 23, no. 2, pp. 657–671, Apr. 2015.

[21] F. Yao, J. Wu, G. Venkataramani, and S. Subramaniam, “TS-BatPro: Improving energy efficiency in data centers by leveraging temporal–spatial batching,” IEEE Trans. Green Commun. Netw., vol. 3, no. 1, pp. 236–249, Mar. 2019.

[22] A. Agarwal et al., “Redesigning data centers for renewable energy,” in Proc. 20th ACM Workshop Hot Top. Netw., 2021, pp. 45–52.

[23] H. Yuan, H. Liu, J. Bi, and M. Zhou, “Revenue and energy cost-optimized biobjective task scheduling for green cloud data centers,” IEEE Trans. Autom. Sci. Eng., vol. 18, no. 2, pp. 817–830, Apr. 2021.

[24] W. Abderrahim, O. Amin, and B. Shihada, “How to leverage high altitude platforms in green computing?,” IEEE Commun. Mag., vol. 61, no. 7, pp. 134–140, Jul. 2023.

[25] K. Mershad, H. Dahrouj, H. Sarieddeen, B. Shihada, T. Al-Naffouri, and M.-S. Alouini, “Cloud-enabled high-altitude platform systems: Challenges and opportunities,” Front. Commun. Netw., vol. 2, pp. 1–21, 2021.

[26] G. K. Kurt et al., “A vision and framework for the high altitude platform station (HAPS) networks of the future,” IEEE Commun. Surveys Tut., vol. 23, no. 2, pp. 729–779, Second Quarter 2021.

[27] C. Ding, J.-B. Wang, H. Zhang, M. Lin, and G. Y. Li, “Joint optimization of transmission and computation resources for satellite and high altitude platform assisted edge computing,” IEEE Trans. Wireless Commun., vol. 21, no. 2, pp. 1362–1377, Feb. 2022.

[28] A. Firm, Thermal Guidelines for Data Processing Environments, 5th ed. Peachtree Corners, GA, USA: ASHRAE, 2021.

[29] G. Zhabelova, M. Vesterlund, S. Eschmann, Y. Berezovskaya, V. Vyatkin, and D. Flieller, “A comprehensive model of data center: From CPU to cooling tower,” IEEE Access, vol. 6, pp. 61254–61266, 2018.

[30] L. Parolini, B. Sinopoli, B. H. Krogh, and Z. Wang, “A cyber-physical systems approach to data center modeling and control for energy efficiency,” in Proc. IEEE, vol. 100, no. 1, pp. 254–268, Jan. 2012.

[31] S. C. Arum, D. Grace, P. D. Mitchell, M. D. Zakaria, and N. Morozs, “Energy management of solar-powered aircraft-based high altitude platform for wireless communications,” Electronics, vol. 9, no. 1, pp. 4426–4436, 2020.

[32] K. Sun, J. Li, H. Liang, and M. Zhu, “Simulation of a hybrid energy system for stratospheric airships,” IEEE Trans. Aerosp. Electron. Syst., vol. 56, no. 6, pp. 4426–4436, Dec. 2020.

[33] Z. Lian, L. Jiang, C. He, and D. He, “User grouping and beamforming for HAP massive MIMO systems based on statistical-eigenmode,” IEEE Wireless Commun. Lett., vol. 8, no. 3, pp. 961–964, Jun. 2019.

[34] P. Ji, L. Jiang, C. He, Z. Lian, and D. He, “Energy-efficient beamforming for beamspace HAP-NOMA systems,” IEEE Commun. Lett., vol. 25, no. 5, pp. 1678–1681, May 2021.

[35] E. T. Michailidis and A. G. Kanatas, “Three-dimensional HAP-MIMO channels: Modeling and analysis of space-time correlation,” IEEE Trans. Veh. Technol, vol. 59, no. 5, pp. 2232–2242, Jun. 2010.

[36] H. S. Erden, M. Koz, M. T. Yildirim, and H. E. Khalifa, “Experimental demonstration and flow network model verification of induced CRAH bypass for cooling optimization of enclosed-aisle data centers,” IEEE Trans. Compon. Packag. Manuf. Technol, vol. 7, no. 11, pp. 1795–1803, Nov. 2017.

[37] M. Wolf, “Chapter 5 - processors and systems,” in The Physics of Computing, M. Wolf Ed., Boston, MA, USA: Morgan Kaufmann, 2017, pp. 149–203. [Online]. Available: https://www.sciencedirect.com/science/ article/pii/B9780128093818000055

[38] Y. Zhu, P.-Y. Kam, and Y. Xin, “On the mutual information distribution of MIMO Rician fading channels,” IEEE Trans. Commun., vol. 57, no. 5, pp. 1453–1462, May 2009.

[39] I. Adan and J. Resing, Eindhoven University of Technology, 2015.

[40] L. Xia and B. Shihada, “Max-min optimality of service rate control in closed queueing networks,” IEEE Trans. Autom. Control, vol. 58, no. 4, pp. 1051–1056, Apr. 2013.

[41] A. Elwhishi, P.-H. Ho, K. Naik, and B. Shihada, “Self-adaptive contention aware routing protocol for intermittently connected mobile networks,” IEEETrans. Parallel Distrib. Syst., vol. 24, no. 7, pp. 1422–1435, Jul. 2013.

[42] Thales, Thales Alenia Space’s Stratobus stratospheric airship passes a new development milestone. 2021. [Online]. Available: https://www.thalesgroup.com/en/worldwide/space/press-release/thalesalenia-spaces-stratobus-stratospheric-airship-passes-new

[43] T. L. by Eaton, Edge ready micro data center. 2023. [Online]. Available: https://www.tripplite.com/micro-data-center-mdc-230vfloor-21umdk2f21upx00000/

[44] G. Mitsis, E. E. Tsiropoulou, and S. Papavassiliou, “Price and risk awareness for data offloading decision-making in edge computing systems,” IEEE Syst. J., vol. 16, no. 4, pp. 6546–6557, Dec. 2022.

![](images/8293d12bb22f505d94c2f485fe7fafaa226e8eff9c0912594d34ab40a47fa8ce.jpg)  
Wiem Abderrahim (Member, IEEE) received the undergraduate degree in electrical engineering from the Higher School of Communications of Tunis, Carthage University, Tunisia, in 2013, and the doctoral degree in information and communication technologies from the Carthage University, Tunisia, in 2017. She worked as a lecturer and then as an adjunct professor with the Higher School of Communications of Tunis between 2014 and 2018. Currently, she is a postdoctoral fellow within King Abdullah University of Science and Technology (KAUST), Thuwal, Saudi

Arabia. Her research interests include cloud computing, edge computing, network virtualization, software defined networking and recently satellite communications and machine learning.

![](images/5d12c2d340924b4d6f318e487857617f74811bfb4441d154979212b65e6ccff9.jpg)

Osama Amin (Senior Member, IEEE) received the BSc degree in electrical and electronic engineering from Aswan University, Egypt, in 2000, the MSc degree in electrical and electronic engineering from Assiut University, Egypt, in 2004, and the PhD degree in electrical and computer engineering, University of Waterloo, Canada, in 2010. In 2012, he joined Assiut University as an assistant professor with the Electrical and Electronics Engineering Department. Currently, he is a research scientist with the CEMSE Division, KAUST, Thuwal, Makkah Province, Saudi

Arabia. His general research interests lie in communication systems and signal processing for communications with special emphasis on wireless applications.

![](images/db50ab2702939d0a429837ba3e1735fe9369b45e87b932188765ea2f75624815.jpg)

Basem Shihada (Senior Member, IEEE) received the PhD degree in computer science from the University of Waterloo, Waterloo, ON, Canada. He is an associate and a founding professor with the Computer, Electrical and Mathematical Sciences Engineering Division, King Abdullah University of Science and Technology, Thuwal, Saudi Arabia. In 2009, he was appointed as a visiting faculty member with the Department of Computer Science, Stanford University, Stanford, California. His current research interests include energy and resource allocation in wired and wireless networks, software-defined networking, Internet of Things, data networks, smart systems, network security, and cloud/fog computing.