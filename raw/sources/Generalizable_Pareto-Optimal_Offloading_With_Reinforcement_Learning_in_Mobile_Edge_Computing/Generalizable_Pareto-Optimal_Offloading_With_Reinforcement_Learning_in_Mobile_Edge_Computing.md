# Generalizable Pareto-Optimal Offloading with Reinforcement Learning in Mobile Edge Computing

Ning Yang\*<sup>1∗</sup> Junrui Wen\*<sup>1</sup> Meng Zhang<sup>2</sup> Ming Tang<sup>3</sup>

<sup>1</sup>Institute of Automation, Chinese Academy of Sciences

<sup>2</sup>ZJU-UIUC Institute, Zhejiang University

<sup>3</sup>Department of Computer Science and Engineering, Southern University of Science and Technology

## Abstract

Mobile edge computing (MEC) is essential for next-generation mobile network applications that prioritize various performance metrics, including delays and energy efficiency. However, conventional single-objective scheduling solutions cannot be directly applied to practical systems in which the preferences (i.e., the weights of different objectives) are often unknown or challenging to specify in advance. In this study, we formulate a multi-objective offloading problem for MEC with multiple edges to minimize the sum of expected long-term energy consumption and delay while considering unknown preferences. To address the challenge of unknown preferences and the potentially diverse MEC systems, we propose a generalizable multi-objective (deep) reinforcement learning (GMORL)- based tasks offloading framework, which employs the Discrete Soft Actor-Critic (Discrete-SAC) method. Our method uses a single policy model to efficiently schedule tasks based on varying preferences and adapt to heterogeneous MEC systems with different CPU frequencies and server quantities. Under the proposed framework, we introduce a histogram-based state encoding method for constructing features for multiple edges in MEC systems, a sophisticated reward function for accurately computing the utilities of delay and energy consumption, and a novel neural network architecture for improving generalization. Simulation results demonstrate that our proposed GMORL scheme enhances the hypervolume of the Pareto front by up to 121.0% compared to benchmarks. Our code are avavilable at https://github.com/gracefulning/Generalizable-Pareto-Optimal-Offloading-with-Reinforcement-Learning-in-Mobile-Edge-Computing

Keywords: Mobile edge computing, multi-objective reinforcement learning, resource scheduling, discrete-soft actor-critic.

## 1 introduction

## 1.1 Background and Challenges

The rise of next-generation networks and the increasing use of mobile devices have resulted in an exponential growth of data transmission and diverse computing needs. With the emergence of new computing-intensive applications, there is a possibility that device computing capacity may not suffice. To tackle this challenge, mobile edge computing (MEC) has emerged as a promising computing paradigm. MEC enables the offloading of computing workloads to edge or cloud networks, offering the potential for achieving low latency and high efficiency [1]. In MEC systems, task offloading is crucial in achieving low latency and energy consumption [2]. The scheduling of task offloading in MEC systems is challenging due to the dynamic and unpredictable nature of users’ workloads and computing requirements. Some works apply traditional optimization methods to schedule for MEC systems [3, 4]. These methods assume deterministic objective functions that cannot cope well with uncertainty or dynamics in the problem parameters.

The application of deep reinforcement learning (DRL) has shown substantial potential in addressing sequential decision-making problems and have demonstrated the effectiveness of applying DRL in MEC systems to address the unknown dynamics. For instance, Cui et al. [5] employed DRL to solve the user association and offloading sub-problems in MEC networks. Lei et al. [6] investigated computation offloading and multi-user scheduling algorithms in edge IoT networks and proposed a DRL algorithm to solve the continuous-time problem, supporting implementation based on semidistributed auctions. Jiang et al. [7] proposed an online DRL-based resource scheduling framework to minimize the delay in large-scale MEC systems. However, a challenge that has been overlooked by researchers is the issue of generalization.

Challenge 1 DRL policies are typically trained for specific environments, rendering them less adaptable to novel contexts.

Nevertheless, it is important to acknowledge that the training and application environments may not always align and that there may be variations in their parameters. Consequently, the scheme must be flexible enough to accommodate a range of diverse and unknown preferences. To achieve the generalization of preferences, we have to seek out new methodologies to address the following questions:

Question 1 How should we design a scheduling policy that can apply to various MEC systems with diverse preferences?

The challenge of addressing this problem can be summarized in two aspects. First, there may be conflicts between different objectives, such as delay and energy consumption, that cannot be optimized simultaneously. Second, since MEC systems serve diverse applications with varying preferences, it is challenging to design an offloading policy that can generate Pareto optimal solutions under diverse and unknown preferences.

It is worth noting that the direct application of single-objective DRL through scalarization, which involves taking a weighted sum, is not a valid approach due to the following issues [8]:

1. Impossibility: Weights may be unknown when designing or learning an offloading scheme.

2. Infeasibility: Weights may be diverse, which is true when MEC systems have different restrictive constraints on latency or energy.

3. Undesirability: Even if weights are known, nonlinear objective functions may lead to nonstationary optimal policies.

To effectively address these challenges, we propose to employ multi-objective reinforcement learning (MORL) to design a task offloading policy. However, this method faces certain limitations. Firstly, when dealing with a large number of preferences, it can become computationally and storage-intensive [8]. Secondly, since the preference is typically unknown in advance, it becomes infeasible to search for a specific policy that matches a particular preference from a pre-trained set of policies [9]. Therefore, we propose a novel single-policy MORL method to schedule tasks for MEC systems. To this end, we propose to use a single policy to accommodate diverse preferences.

Compared with multi-policy approaches, our single-policy MORL method is more lightweight and more feasible for deployment.

Although the MORL approach can deal with diverse preference problems, there are other generalization issues worth considering.

Question 2 How should we deploy a well-trained DRL-based policy to new MEC systems with different CPU frequencies and server quantities?

Existing DRL methods for task offloading scheduling in MEC networks have, to date, exhibited limited research pertaining to matters of generalization. Yan et al. [10] introduced a DRL method to optimize offloading scheduling, but they exclusively considered a fixed preference and a set of constant system parameters. Li et al. [11] proposed a meta-reinforcement learning method to lead an DRL-based policy quickly adaptive to new environments. However, this approach lacks the capability to generalize to new environments with varying server quantities. Gao et al. [12] proposed a multi-agent DRL method to schedule tasks for large-scale MEC systems. This method can handle systems with different quantities of servers, but it can only optimize for a single fixed preference. Ren et al. [13] exploited learning-experience utility to improve the generalization of a DRL policy. Nonetheless, when the quantity of servers varied, the policy network had to be redesigned and retrained. In contrast, a majority of other studies [2, 5–7, 14] have predominantly disregarded the aspect of generalization in their methodologies.

Solving the generalization problem has been the subject of research, and various methods have been proposed. Two widely used technologies to improve the generalization of DRL methods are domain randomization [15] and adapting online [16]. These methods utilize context to characterize a system with specific parameters. For a contextual Markov decision process (MDP) [17, 18], domain randomization approaches train an DRL model in randomized environments to make the model adapt to diverse systems. Therefore, we improve the MORL and propose the generalizable multiobjective reinforcement learning (GMORL). We summarize the differences between our method and other existing works in the study of generalization in Table 1, with comprehensive details provided in the Appendix.

Table 1: Relate works about DRL method for offloading task scheduling in MEC system.

<table><tr><td rowspan="2">Refs.</td><td colspan="3">Generalization across different aspects</td></tr><tr><td>Multi-preference</td><td>System parameters</td><td>Server quantities</td></tr><tr><td>[2,5,6,14,19,20]</td><td>✕</td><td>✕</td><td>✕</td></tr><tr><td>[11,13,21–23]</td><td>✕</td><td>✕</td><td>✕</td></tr><tr><td>[7,24,25]</td><td>✕</td><td>✕</td><td>✕</td></tr><tr><td>[12]</td><td>✕</td><td>✕</td><td>✕</td></tr><tr><td>Ours</td><td>✕</td><td>✕</td><td>✕</td></tr></table>

## 1.2 Research Goals, Approaches, and Contributions

In summary, there are three main challenges to MEC task offloading. Firstly, task requirements are uncertain, and the system is dynamic. Secondly, there are diverse and unknown preferences. Thirdly, task offloading policies must be generalizable to accommodate different systems.

The main contributions of this paper are as follows:

• Multi-objective MEC Framework: We formulate the multi-objective contextual MDP problem framework. Compared with previous works, our framework focuses on the Pareto optimal solutions, which characterize the performance of the offloading scheduling policy with multiple objectives under different preferences.

• Multi-objective Decision Model: We propose a novel GMORL method based on Discrete-SAC to solve the multi-objective problem. Our proposed method aims to achieve the Pareto near-optimal solution for diverse preferences through only one policy model. Moreover, we introduce a histogram-based encoding method to construct features for multi-edge systems and a sophisticated reward function to compute delay and energy consumption.

• Multi-system Generalization Model: To guarantee the generalization of our method so that it applies to MEC environments with varying CPU frequencies and edge quantities after training. We propose a novel neural network architecture that supports generalization.

• Numerical Results: Compared to benchmarks, our GMORL scheme increases the hypervolume of the Pareto front up to 121.0%. Moreover, our approach exhibits strong generalization.

## 2 System Model

We consider a set of servers $\mathcal { E } = \{ 0 , 1 , 2 , . . . , E \}$ with one remote cloud server (denoted by index 0) and E edge servers (denoted by set $\mathcal { E } ^ { \prime } = \{ 1 , 2 , . . . , E \} )$ , and consider a set of users $\mathcal { U } = \{ 1 , 2 , . . . , U \}$ in an MEC system. We use index $e \in { \mathcal { E } }$ to denote a server and use index $e ^ { \prime } \in \mathcal { E } ^ { \prime }$ to denote an edge server. Index $u \in \mathcal { U }$ denotes a user. Our model is a continuous-time system and has discrete decision steps. Consider one episode consisting of T steps, and each step is denoted by $t \in \{ 1 , 2 , . . . , T \}$ , each with a duration of $\Delta \bar { t }$ seconds. The MEC system model we consider is illustrated in Fig. A1 of the Appendix.

## 2.1 System Overview

Consider multiple users and servers in the MEC system. Tasks randomly arrive at users. Users may offload the tasks to the servers. Let $\mathcal { M } = \{ 1 , 2 , . . . , M \}$ denote the set of tasks in an episode. We use m $\in \mathcal { M }$ to denote a task and use $L _ { m }$ to denote the size of task $m ,$ which follows an exponential distribution [26] with mean L<sup>¯</sup>. At the beginning of each step, the arrival time of a series of tasks follows a Poisson distribution for each user, and the Poisson arrival rate for each user is $\lambda _ { p } .$ The tasks are placed in a queue with a first in, first out (FIFO) queue strategy. In each step, the system will offload the first task in the queue to one of the servers. Then the task is removed from the queue.

We assumed that the uplink operates in an interference-free ideal communication environment, i.e., only additive white Gaussian noise (AWGN) is considered, and factors such as co-channel interference are not introduced. The mean of task size $\bar { L }$ represents the demand for tasks. If the computational capability of the system exceeds the demand, the scheduling pressure decreases. Conversely, if the demand surpasses the capability, the system will continuously accumulate tasks over time. Therefore, we consider a system that balances computational capability and task demand. The mean of task size L<sup>¯</sup> satisfies

$$
\Delta t \left(\sum_ {e \in \mathcal {E}} \frac {f _ {e}}{\eta}\right) = \lambda_ {p} \bar {L} U,\tag{1}
$$

where $f _ { e }$ is the CPU frequency (in cycles per second) of server e, and η is the number of CPU cycles required for computing a one-bit task.

We consider a Rayleigh fading channel model in the MEC network. We denote $\pmb { h } \in \mathbb { R } ^ { U \times ( E + 1 ) }$ as the $U \times ( E + 1 )$ channel matrix. Thus, the achievable data rate from user u to server e is

$$
C _ {u, e} = W \log_ {2} \left(1 + \frac {p ^ {\text { off }} | h _ {u , e} | ^ {2}}{\sigma^ {2}}\right), \forall u \in \mathcal {U}, e \in \mathcal {E},\tag{2}
$$

where $\sigma ^ { 2 }$ is additive white Gaussian noise (AWGN) power, and $W$ is the bandwidth. The offloading power is $p ^ { \mathrm { o f f } }$ , and the channel coefficient from user u to server e is $h _ { u , e }$

In real scenarios, simultaneous offloading flows in the uplink will generate interference. This interference will have an impact on both dense 5G/6G or license-free MEC deployments. Suppose that server e has $N _ { e }$ connected users, and the users are arranged in descending order of channel gain as $| h _ { 1 , e } | \geq | h _ { 2 , e } | \geq \cdots \geq | h _ { N _ { e } , e } | .$

To simplify the analysis of the initial model, it is assumed here that the uplink is in an ideal interference-free communication environment, and only AWGN is considered. Therefore, the data rate is described by Eq.(2). In practical scenarios, the interference of synchronous offloading flows cannot be ignored, and the interference term $I _ { u , e }$ needs to be introduced to correct the data rate, as shown in the following equations. Suppose that server e has $N _ { e }$ connected users, and the users are arranged in descending order of channel gain as $| h _ { 1 , e } | \geq | h _ { 2 , e } | \geq \cdot \cdot \cdot \geq | h _ { N _ { e } , e } |$ . Denote the interference at the receiver of user u when offloading to server e as $I _ { u , e } .$ . Then we have the interference $I _ { u , e }$ as follows:

$$
I _ {u, e} = \sum_ {u ^ {\prime} = 1} ^ {U} p ^ {\mathrm{off}} | h _ {u ^ {\prime}, e} | ^ {2}\tag{3}
$$

Therefore, the achievable data rate with the interference from user u to server e is

$$
C _ {u, e} ^ {\prime} = W \log_ {2} \left(1 + \frac {p ^ {\text { off }} | h _ {u , e} | ^ {2}}{\sigma^ {2} + I _ {u , e}}\right).\tag{4}
$$

Offloading: We denote the offloading decision (matrix) as $\pmb { x } = \{ x _ { m , e } \} _ { m \in \mathcal { M } , e \in \mathcal { E } }$ , where $x _ { m , e } \in$ $\{ 0 , 1 \}$ is an offloading indicator variable; $x _ { m , e } = 1$ indicates that task m is offloaded to server e. Here, we adopt a binary offloading assumption, where each task is either fully offloaded to a server $( x _ { m , e } = 1 )$ or executed locally $( x _ { m , e } = 0 )$ without splitting. If task m comes from user u, the offloading delay for task m is given by [27]

$$
T _ {m} ^ {\mathrm{off}} = \sum_ {e \in \mathcal {E}} x _ {m, e} \frac {L _ {m}}{C _ {u , e}}, \forall m \in \mathcal {M}.\tag{5}
$$

The offloading energy consumption for task m with offloading power $p ^ { \mathrm { o f f } }$ is

$$
E _ {m} ^ {\mathrm{off}} = p ^ {\mathrm{off}} T _ {m} ^ {\mathrm{off}}, \forall m \in \mathcal {M}.\tag{6}
$$

Execution: Each server executes tasks in parallel. We denote the beginning of step t as time instant $\tau _ { t } .$ , given by $\tau _ { t } = t \Delta t$ . The computing speed for each task in server e at time instant $\tau _ { t }$ is

$$
q _ {e} (\tau_ {t}) = \frac {f _ {e}}{n _ {e} ^ {\mathrm{exe}} (\tau_ {t}) \eta}, \forall e \in \mathcal {E},\tag{7}
$$

We define $n _ { e } ^ { \mathrm { e x e } } ( \tau _ { t } )$ as the number of tasks that are being executed in server e at time $\tau _ { t }$ . The $n _ { e } ^ { \mathrm { e x e } } ( \tau _ { t } )$ tasks share equally the computing resources of server e. Thus, we give the relation between task size $L _ { m }$ and execution delay $T _ { m } ^ { \mathrm { e x e } }$ for task m as

$$
\begin{array}{l} L _ {m} = g _ {m} (T _ {m} ^ {\mathrm{exe}}) \\ = \sum_ {e \in \mathcal {E}} x _ {m, e} \int_ {m \Delta t + T _ {m} ^ {\mathrm{off}}} ^ {m \Delta t + T _ {m} ^ {\mathrm{off}} + T _ {m} ^ {\mathrm{exe}}} q _ {e} (\tau) d \tau , \forall m \in \mathcal {M}, \end{array}\tag{8}
$$

where $\tau$ is a time instant. The integral function $g _ { m } ( T _ { m } ^ { \mathrm { e x e } } )$ denotes the aggregate executed size for task m from $m \Delta t + T _ { m } ^ { \mathrm { o f f } }$ to $m \Delta t + \bar { T } _ { m } ^ { \mathrm { o f f } } + T _ { m } ^ { \mathrm { e x e } }$ . Therefore, execution time delay $T _ { m } ^ { \mathrm { e x e } }$ of task m is

$$
T _ {m} ^ {\mathrm{exe}} = \frac {L _ {m} \cdot n _ {e} ^ {\mathrm{exe}} (\tau_ {t}) \eta}{f _ {e}}, \forall m \in \mathcal {M}.\tag{9}
$$

The total energy consumption of execution for task m is modeled as [27]

$$
E _ {m} ^ {\mathrm{exe}} = \sum_ {e \in \mathcal {E}} x _ {m, e} \kappa \eta f _ {e} ^ {2} L _ {m}, \forall m \in \mathcal {M},\tag{10}
$$

where κ denotes an effective capacitance coefficient for each CPU cycle.

To summarize, the overall delay and the overall energy consumption for task m $\in \mathcal { M }$ are

$$
T _ {m} = T _ {m} ^ {\mathrm{off}} + T _ {m} ^ {\mathrm{exe}}, E _ {m} = E _ {m} ^ {\mathrm{off}} + E _ {m} ^ {\mathrm{exe}},\tag{11}
$$

respectively.

## 2.2 Problem Formulation

We introduce the preference vector $\omega = \left( \omega _ { \mathrm { T } } , \omega _ { \mathrm { E } } \right)$ , which satisfies $\omega _ { \mathrm { T } } + \omega _ { \mathrm { E } } = 1$ . A (stochastic) sequential decision-making policy is a mapping π. For any given task m and system state, policy π selects an offloading decision $x _ { m , e }$ according to a certain probability distribution.

Given any one possible $\omega ,$ the multi-objective resource scheduling problem under the policy $\pi$ is given by

$$
\min _ {\boldsymbol \pi} \mathbb {E} _ {\boldsymbol x \sim \boldsymbol \pi} \left[ \sum_ {m \in \mathcal {M}} \gamma^ {m} \left(\omega_ {\mathrm{T}} T _ {m} + \omega_ {\mathrm{E}} E _ {m}\right) \right]\tag{12a}
$$

$$
\begin{array}{l l} \text {s.t.} & x _ {m, e} \in \{0, 1 \}, \forall m \in \mathcal {M}, \forall e \in \mathcal {E}, \end{array}\tag{12b}
$$

$$
\sum_ {e \in \mathcal {E}} x _ {m, e} = 1, \forall m \in \mathcal {M},\tag{12c}
$$

where constraint (12b) restricts task offloading variables to be binary, and constraint (12c) guarantees that each task can be only offloaded to one server. A discount factor γ characterizes the discounted objective in the future. The expectation <sup>E</sup> accounts for the distribution of the task size $L _ { m } ,$ the arrival of users, and stochastic policy π. The problem (12) is non-convex due to constraint (12b), which requires the decision variables to be discrete. This makes the feasible set non-convex, as linear combinations of feasible solutions are not guaranteed to remain feasible, leading to the non-convex nature of the problem. Moreover, when making offloading decisions at each time step, the sizes of tasks arriving after that time step are unknown. As shown in Eq. (7), (8), and (9), the execution time of a task is related to the offloading decisions made in subsequent time steps, as well as the size of the tasks. Therefore, without information about future time steps, convex optimization methods cannot be used to solve problem (12).

The challenge of this problem lies in two aspects: First, there is a conflict between optimizing delay and energy consumption. According to Eq. (4) and Eq. (8), the main energy consumption of a task depends on execution energy, which increases with higher server CPU frequencies. Therefore, reducing energy consumption involves offloading tasks to edge servers with lower CPU frequencies. According to Eq. (3) and Eq. (7), the main delay of a task depends on execution time, which is lower on cloud servers with higher CPU frequencies, but increases as more tasks are executed on a single server. Thus, reducing delay requires offloading a larger number of tasks to cloud servers with higher CPU frequencies, leading to a conflict between optimizing delay and energy consumption. Second, the scheduling policy must optimize problem (10) under distinct preferences to achieve the optimal solution, rather than just under a fixed preference.

Consider a preference set $\boldsymbol { \Omega } = \{ \omega _ { 1 } , \omega _ { 2 } , . . . , \omega _ { n } \}$ with n preferences. A generalizable scheduling policy aims at solving Problem (12) given any preference in Ω. To facilitate illustration, we consider the policy under a specific preference as a sub-policy. When dealing with the preference set Ω, we define the sub-policies set $\Pi = \{ \pi _ { 1 } , \pi _ { 2 } , . . . , \pi _ { n } \}$ . Let $\scriptstyle { \boldsymbol { y } } ^ { \pi }$ denote the performance vector for π, given by

$$
\boldsymbol {y} ^ {\pi} = \left\{y _ {\mathrm{T}} ^ {\pi}, y _ {\mathrm{E}} ^ {\pi} \right\} = \left\{\sum_ {m \in \mathcal {M}} T _ {m}, \sum_ {m \in \mathcal {M}} E _ {m} \right\}.\tag{13}
$$

The performance profile of Π is denoted as $Y = \{ \pmb { y } ^ { \pi _ { 1 } } , \pmb { y } ^ { \pi _ { 2 } } , . . . , \pmb { y } ^ { \pi _ { n } } \}$ . We consider Pareto front [8] to characterize the optimal trade-offs between two performance metrics. For a sub-policies set Π, Pareto front $P F ( \Pi )$ is the undominated set:

$$
P F (\Pi) = \{\pi \in \Pi \mid \nexists \pi^ {\prime} \in \Pi : \boldsymbol {y} ^ {\pi^ {\prime}} \succ_ {P} \boldsymbol {y} ^ {\pi} \},\tag{14}
$$

where $\succ _ { P }$ is the Pareto dominance relation, satisfying

$$
\begin{array}{l} \boldsymbol {y} ^ {\pi} \succ_ {P} \boldsymbol {y} ^ {\pi^ {\prime}} \iff \\ (\forall i: y _ {i} ^ {\pi} \geq y _ {i} ^ {\pi^ {\prime}}) \wedge (\exists i: y _ {i} ^ {\pi} > y _ {i} ^ {\pi^ {\prime}}), i \in \{\mathrm{T}, \mathrm{E} \}. \end{array}\tag{15}
$$

We aim to approximate the exact Pareto front by searching for policies set Π. In the multi-objective MEC scheduling problem, as a Pareto front approximation ${ \cal P } \bar { F ( \Pi ) }$ , the hypervolume metric is

$$
\mathcal {V} (P F (\Pi)) = \int_ {\mathbb {R} ^ {2}} \mathbb {1} _ {V _ {h} (P F (\Pi))} (z) d z,\tag{16}
$$

where $V _ { h } ( P F ( \Pi ) ) = \{ z \in Z | \exists \pi \in P F ( \Pi ) : y ^ { \pi } \succ _ { P } z \succ _ { P } y ^ { \mathrm { r e f } } \}$ , and $y ^ { \mathrm { r e f } } \in \mathbb { R } ^ { 2 }$ is a reference performance point. Function $\mathbb { 1 } _ { V _ { h } ( P F ( \Pi ) ) }$ is an indicator function that returns 1 if $z \in V _ { h } ( P F ( \Pi ) ^ { \prime } )$ and 0 otherwise.

The multi-objective resource scheduling problem is still a challenge for MEC networks for the following reasons:

• The natural MEC network environments are full of dynamics and uncertainty (e.g. the size of the next arriving task), leading to unknown preferences of MEC systems.

• The objective function (12) and the feasible set of constraints (12b) and (12c) are nonconvex as a result of binary variables x. Although it is possible to transform them into convex problems, the computational complexity of convex optimization is demanding since the goal is to get a vector reward instead of a reward value.

• Designing an offloading scheme for various MEC systems with different CPU frequencies and numbers of servers is difficult, due to the system optimization equations and the value space of decision variables have changed.

The aforementioned problems motivate us to design a GMORL-based scheme to solve (12) and improve the generalization.

## 3 GMORL Scheduling Method

This section considers the situation of multiple preferences, CPU frequencies, and server quantities. We consider that a (central) agent makes all offloading decisions in a fully observable setting. We model the MEC environment as a novel MDP framework named contextual MOMDP (multiobjective Markov decision process).

## 3.1 The Contextual MOMDP Framework

The traditional MDP framework considers only a single objective, while the MOMDP framework extends it to multiple objectives. Additionally, in MDPs, the contextual characteristics of the environment directly influence the transition process. However, the traditional MDP framework lacks a definition of contextual characteristics for environments, leading to algorithms being unable to formulate the optimal policy based on the specific environment. Contextual MDP, which considers this definition, has been extensively employed in research on the generalization of DRL algorithms [17].

Thus, to address the challenges of unknown user preferences and system heterogeneity, we first propose the contextual MOMDP framework for unknown preferences and system heterogeneity to formulate our problem (12) as a standard form of DRL.

Definition 1 (Contextual MOMDP) The contextual MOMDP is a tuple $\langle \mathcal { S } \times \mathcal { C } , \mathcal { A } , \mathcal { T } , \gamma , \mu , \mathcal { R } \rangle$ where the underlying state is $s ^ { \prime } \in { \mathcal { S } } ,$ , context is $c \in { \mathcal { C } } ,$ , context space is C, and state space is ${ \mathcal { S } } \times { \mathcal { C } } .$ It also includes action space ${ \mathcal { A } } ,$ probabilistic transition process $\mathcal { T } : \mathcal { S } \times \mathcal { A }  \mathcal { S } ,$ , discount factor $\gamma \in [ 0 , 1 )$ , probability distribution over initial states $\mu : { \mathcal { S } }  [ 0 , 1 ] ,$ , and a vector-valued reward function $\mathcal { R } : \mathcal { S } \times \mathcal { A } \stackrel { \cdot } { \to } \mathbb { R } ^ { 2 }$ that specifies the immediate reward for the delay objective and the energy consumption objective.

In contextual MOMDP, the reward function returns a vector reward instead of a scalar. Context space is used to describe variations across different environment parameters, and a context corresponds to a specific environment (MEC system) and remains constant within an episode. The training context space is a subset of the full context space. An agent learns from environments within the training context space. The evaluation performance gap between training context space and full context space measures the generalization ability of an agent.

For one episode, the contextual MOMDP samples a context $c$ in context space $\mathcal { C }$ to construct an environment. The context c determines the transition $\tau$ and reward function $\mathcal { R }$ of the environment. For a decision step $t ,$ an agent offloads task m from user $u .$ It has $m = t$ for task index m and step-index t. We specify the contextual MOMDP framework in the following:

Context C: A context $c = ( \omega , E , f _ { \varepsilon } )$ contains a preference vector ω, the number of edge server $E ,$ the CPU frequencies of all servers $\pmb { f } _ { \pmb { \xi } } = ( f _ { 0 } , f _ { 1 } , f _ { 2 } , \dots , f _ { E } )$ ). The composition of the context space C is

$$
\mathcal {C} = \Omega \times \mathcal {C} _ {E} \times \mathcal {C} _ {\boldsymbol {f} _ {\varepsilon}},\tag{17}
$$

where $\boldsymbol { \Omega } = \{ \omega _ { 1 } , \omega _ { 2 } , . . . , \omega _ { n } \}$ is the preference set. The range of edge server quantity is $\mathcal { C } _ { E } ~ =$ $\{ 1 , 2 , \dots , E ^ { \mathrm { m a x } } \}$ . The range of CPU frequency for all servers is $\mathcal { C } _ { \pmb { f } _ { \varepsilon } } \overset { \mathbf { \check { \mathbf { \alpha } } } } { = } \{ \mathcal { C } _ { \pmb { f } _ { 0 } } , \mathcal { C } _ { \pmb { f } _ { \varepsilon ^ { \prime } } } \}$ , where $\mathcal { C } _ { f _ { 0 } }$ is the range CPU frequency for a cloud server and $\mathcal { C } _ { f _ { \varepsilon ^ { \prime } } }$ is the range of CPU frequency for all edge servers. We have $\mathcal { C } _ { f _ { 0 } } = [ f _ { 0 } ^ { \operatorname* { m i n } } , f _ { 0 } ^ { \operatorname* { m a x } } ]$ and $\mathcal { C } _ { f _ { \varepsilon ^ { \prime } } } = [ f _ { \mathcal { E } ^ { \prime } } ^ { \operatorname* { m i n } } , f _ { \mathcal { E } ^ { \prime } } ^ { \operatorname* { m a x } } ]$ . For an MEC system with context $c \in { \mathcal { C } } .$ , it follows that $\omega \in \mathcal { C } _ { \omega } , E \in \mathcal { C } _ { E }$ , and $\bar { f _ { e } } \in \mathcal { C } _ { f _ { \varepsilon } }$ for any $e \in { \mathcal { E } }$

State S: We employ a well-designed approach to encode the system state. We consider $E ^ { \mathrm { m a x } } + 1$ servers $( E ^ { \mathrm { m a x } }$ edge servers and a cloud server). Hence, the state $\pmb { s } _ { t } \in \mathcal { S } \times \mathcal { C }$ at step t is a fixed length set and contains $\breve { E } ^ { \mathrm { m a x } } + 1$ server information vectors and a preference vector ω. We formulate state $\mathbf { } _  \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf \mathbf { } \mathbf { } \mathbf \mathbf { } \mathbf { } \mathbf \mathbf { } \mathbf { } \mathbf \mathbf { } \mathbf \mathbf { } \mathbf { } \mathbf \mathbf { } \mathbf \mathbf { } \mathbf \mathbf { } \mathbf \mathbf { } \mathbf $ as $\pmb { s } _ { t } = \{ \pmb { s } _ { t , e } | e \in \mathcal { E } \} \cup \{ \pmb { s } _ { t , e } | e \notin \mathcal { E } \wedge e \in \mathcal { C } _ { E } \} \cup \{ \omega \}$ . The information vector of server e at step t is

$$
\boldsymbol {s} _ {t, e} = (L _ {m}, C _ {u, e}, f _ {e}, n _ {e} ^ {\mathrm{exe}} (\tau_ {t}), E, \boldsymbol {\mathcal {B}} _ {e}), \forall e \in \mathcal {E}.\tag{18}
$$

State $\mathbf { \Delta } _ { \mathbf { \boldsymbol { s } } _ { t , e } }$ contains task size $L _ { m }$ , data rate $C _ { u , e } ,$ , CPU frequency $f _ { e } ,$ , the number of execution task $n _ { e } ^ { \mathrm { e x e } } ( \tau _ { t } )$ , the number of edge server $E _ { \mathrm { { : } } }$ and task histogram vector $\pmb { { \cal B } } _ { e }$ , which is the residual size distribution for tasks executed in server e at time instant $\tau _ { t }$ . We employ the histogram vector $\pmb { { \cal B } } _ { e }$ to represent the current state of the dynamic workload on the servers. That is,

$$
\boldsymbol {\mathcal {B}} _ {e} (\tau_ {t}) = (b _ {1, e} ^ {\mathrm{exe}} (\tau_ {t}), b _ {2, e} ^ {\mathrm{exe}} (\tau_ {t}),..., b _ {N, e} ^ {\mathrm{exe}} (\tau_ {t})).\tag{19}
$$

We denote one of previous tasks as $m ^ { \prime }$ and denote the execution residual size of task $m ^ { \prime }$ at time instant $\tau _ { t }$ as $L _ { m ^ { \prime } } ^ { \mathrm { r e s } } ( \tau _ { t } )$ . In Eq. (19), the i-th entry $b _ { i , e } ^ { \mathrm { e x e } } ( \tau _ { t } )$ in $\pmb { { \cal B } } _ { e }$ denotes the number of tasks with execution residual size $L _ { m ^ { \prime } } ^ { \mathrm { r e s } } ( \tau _ { t } )$ ) within the range of $[ i - 1 , i )$ Mbits. In order to tally all tasks, the last element $b _ { N , e } ^ { \mathrm { e x e } } ( \tau _ { t } )$ denotes the number of tasks with execution residual size $L _ { m ^ { \prime } } ^ { \mathrm { r e s } } ( \tau _ { t } )$ within the range of $[ N - 1 , + \infty )$ ) Mbits. The execution residual size $L _ { m ^ { \prime } } ^ { \mathrm { r e s } } ( \tau _ { t } )$ of task $m ^ { \prime }$ at time instant $\tau _ { t }$ is given by

$$
\begin{array}{r} L _ {m ^ {\prime}} ^ {\mathrm{res}} (\tau_ {t}) = L _ {m ^ {\prime}} - \min \left(g _ {m ^ {\prime}} \left(\tau_ {t} - m ^ {\prime} \Delta t\right), L _ {m ^ {\prime}}\right), \\ \forall \tau_ {t} \in [ t \Delta t, T \Delta t ], m ^ {\prime} \in \{1, 2, \ldots , m - 1 \}. \end{array}\tag{20}
$$

The total number of servers E varies across different contexts, but we assume that E does not exceed $E ^ { \mathrm { m a x } }$ . For a dummy edge server e, which satisfies e $\notin \mathcal { E }$ and $e \in { \mathcal { C } } _ { E }$ (or expressed as $e > E$ and $e \leq E ^ { \mathrm { m a x } } )$ , the vector $\mathbf { \Delta } _ { s _ { t , e } }$ is a padding vector that every element is equal $\mathrm { t o } - 1$

Action A: The action $a _ { t } \in \mathcal A$ denotes that offloading task m to which server. The action space is $\mathcal { A } = \{ 0 , 1 , 2 , \ldots , E \}$ . Hence, the action at step t is represented by the following

$$
a _ {t} = \sum_ {e \in \mathcal {E}} e x _ {m, e} (t).\tag{21}
$$

Transition $\tau { : }$ It describes the transition from $\mathbf { \boldsymbol { s } } _ { t }$ to $s _ { t + 1 }$ with action $a _ { t } .$ , which is denoted by $\textstyle P ( s _ { t + 1 } | s _ { t } , a _ { t } )$

Reward R: Unlike a classical MDP setting in which each reward is a scalar, a multi-objective setting requires a vector. Therefore, our reward (profile) function is given by $\mathcal { R } : \mathcal { S } \times \mathcal { C } \times \dot { \mathcal { A } }  \mathbb { R } ^ { 2 }$ . We denote the reward of energy consumption and delay as r<sub>E</sub> and r<sub>T</sub>. Since the server CPU frequency $f _ { \varepsilon }$ affects the execution delay $T _ { m } ^ { \mathrm { e x e } }$ , the calculation of r<sub>T</sub> and r<sub>E</sub> depends on the system parameters $E$ and $f _ { \varepsilon }$ in the current context c. If the agent offloads task m to server e at step t, the reward of energy consumption given state $\mathbf { \boldsymbol { s } } _ { t }$ and action $a _ { t }$ is

$$
r _ {\mathrm{E}} (\pmb {s} _ {t}, a _ {t}) = - \hat {E} _ {m},\tag{22}
$$

where $\hat { E } _ { m }$ is the estimated energy consumption of task $m .$ , which can be obtained in Eq. (11). For one episode, the total reward for energy consumption is given by

$$
R _ {\mathrm{E}} = \sum_ {t = 1} ^ {T} r _ {\mathrm{E}} (\boldsymbol {s} _ {t}, a _ {t}) = - \sum_ {m \in \mathcal {M}} \hat {E} _ {m}.\tag{23}
$$

The reward for delay is

$$
r _ {\mathrm{T}} (\boldsymbol {s} _ {t}, a _ {t}) = - \left(\hat {T} _ {m} + \sum_ {m ^ {\prime} \in \mathcal {M} _ {e} (\tau_ {t})} \Delta \hat {T} _ {m ^ {\prime}} ^ {a _ {t}}\right),\tag{24}
$$

where $\hat { T } _ { m }$ is the estimated delay for task $m ,$ , and $\boldsymbol { \mathcal { M } } _ { e } ( \boldsymbol { \tau } _ { t } )$ is a set of tasks, which are executed in server e at time instant $\tau _ { t }$ . The estimated correction of delay $\Delta \hat { T } _ { m ^ { \prime } } ^ { a _ { t } }$ describes how much delay will increase to task $m ^ { \prime }$ with action $a _ { t } .$ . For one episode, the total reward of delay has

$$
R _ {\mathrm{T}} = \sum_ {t = 1} ^ {T} r _ {\mathrm{T}} (\pmb {s} _ {t}, a _ {t}) = - \sum_ {m \in \mathcal {M}} T _ {m}.\tag{25}
$$

To compute reward $r _ { T }$ , we rewrite $\operatorname { E q . } ( 2 4 )$ as

$$
r _ {\mathrm{T}} (\pmb {s} _ {t}, a _ {t}) = - \hat {T} _ {m} - \sum_ {m ^ {\prime} \in \mathcal {M} _ {e} (\tau_ {t})} (\hat {T} _ {m ^ {\prime}} ^ {a _ {t}} - \hat {T} _ {m ^ {\prime}} ^ {a ^ {*} (t)}),\tag{26}
$$

where $\hat { T } _ { m ^ { \prime } } ^ { a _ { t } }$ denotes the estimated residual delay of task $m ^ { \prime }$ with taking action $a _ { t }$ at step $t .$ The residual delay of task $m ^ { \prime }$ before taking action $a _ { t }$ is $\hat { T } _ { m ^ { \prime } } ^ { a ^ { * } ( t ) }$ , which is the estimated residual delay at the end of step $t - 1$ . Next, we introduce the computation of the two cases.

(1) The no-offloading case: For task set $\boldsymbol { \mathcal { M } } _ { e } ( \boldsymbol { \tau } _ { t } )$ with $n _ { e } ^ { \mathrm { e x e } } ( \tau _ { t } )$ tasks, the execution residual size is a set $\mathcal { L } _ { \mathcal { M } _ { e } ( \tau _ { t } ) } ^ { \mathrm { r e s } } = \{ L _ { m ^ { \prime } } ^ { \mathrm { \tilde { r e s } } } ( \tau _ { t } ) | m ^ { \prime } \in \mathcal { M } _ { e } ( \tau _ { t } ) \}$ . We sort residual task size set $\mathcal { L } _ { \mathcal { M } _ { e } ( \tau _ { t } ) } ^ { \mathrm { r e s } }$ in the ascending order and get a vector $\pmb { L } _ { \mathcal { M } _ { e } ( \tau _ { t } ) } ^ { \mathrm { s o r t } } = ( \pmb { L } _ { 1 , e } ^ { \mathrm { s o r t } } ( \tau _ { t } ) , \pmb { L } _ { 2 , e } ^ { \mathrm { s o r t } } ( \tau _ { t } ) , . . . , \pmb { L } _ { n _ { e } ^ { \mathrm { e x e } } ( \tau _ { t } ) , e } ^ { \mathrm { s o r t } } ( \tau _ { t } ) )$ , where $L _ { i , e } ^ { \mathrm { s o r t } } ( \tau _ { t } )$ is the i-th least residual task size in $\mathcal { L } _ { \mathcal { M } _ { e } ( \tau _ { t } ) } ^ { \mathrm { r e s } }$ . Specifically, we define $L _ { 0 , e } ^ { \mathrm { s o r t } } ( \tau _ { t } ) = 0$ . Then, we have

$$
\begin{array}{l} \sum_ {m ^ {\prime} \in \mathcal {M} _ {e} (\tau_ {t})} \hat {T} _ {m ^ {\prime}} ^ {a ^ {*} (t)} = \sum_ {i = 1} ^ {n _ {e} ^ {\mathrm{exe}} (\tau_ {t})} (n _ {e} ^ {\mathrm{exe}} (\tau_ {t}) - i + 1) \hat {T} _ {i, e} ^ {\mathrm{dur}} \\ = \sum_ {i = 1} ^ {n _ {e} ^ {\mathrm{exe}} (\tau_ {t})} (n _ {e} ^ {\mathrm{exe}} (\tau_ {t}) - i + 1) \frac {(L _ {i , e} ^ {\mathrm{sort}} (\tau_ {t}) - L _ {i - 1 , e} ^ {\mathrm{sort}} (t))}{q _ {e} (\tau_ {t} + (i - 1) \Delta t)} \\ = \sum_ {i = 1} ^ {n _ {e} ^ {\mathrm{exe}} (\tau_ {t})} \frac {\eta}{f _ {e}} (n _ {e} ^ {\mathrm{exe}} (\tau_ {t}) - i + 1) ^ {2} (L _ {i, e} ^ {\mathrm{sort}} (\tau_ {t}) - L _ {i - 1, e} ^ {\mathrm{sort}} (t)), \end{array}\tag{27}
$$

where $\hat { T } _ { i , e } ^ { \mathrm { d u r } }$ denotes the estimated during of time from the completing instant of residual task $L _ { i - 1 , e } ^ { \mathrm { s o r t } } ( \tau _ { t } )$ to the completing instant of residual task $L _ { i , e } ^ { \mathrm { s o r t } } ( \tau _ { t } )$

(2) The case with taking action $a _ { t } \colon$ The MEC system completes offloading task m at time instant $\tau _ { t } ^ { \prime } = \tau _ { t } + T _ { m } ^ { \mathrm { o f f } }$ . We consider a high-speed communication system that offloading delay $T _ { m } ^ { \mathrm { o f f } }$ is shorter than the duration of one step $\Delta t$ and satisfies $T _ { m } ^ { \mathrm { o f f } } < \Delta t$ . For task set $\boldsymbol { \mathcal { M } } _ { e } ( \boldsymbol { \tau } _ { t } ^ { \prime } )$ with $n _ { e } ^ { \mathrm { e x e } } ( \tau _ { t } ^ { \prime } )$ tasks, the execution residual size is a set $\mathcal { L } _ { \mathcal { M } _ { e } ( \tau _ { t } ^ { \prime } ) } ^ { \mathrm { r e s } } = \{ \ddot { L } _ { m } ^ { \mathrm { r e s } } ( \tau _ { t } ^ { \prime } ) | m \in \mathcal { M } _ { e } ( \tau _ { t } ^ { \prime } ) \}$ }. We sort set $\mathcal { L } _ { \mathcal { M } _ { e } ( \tau _ { t } ^ { \prime } ) } ^ { \mathrm { r e s } }$ in the ascending order and get a vector $\pmb { L } _ { \mathcal { M } _ { e } ( \tau _ { t } ^ { \prime } ) } ^ { \mathrm { s o r t } } = ( \pmb { L } _ { 1 , e } ^ { \mathrm { s o r t } } ( \tau _ { t } ^ { \prime } ) , \pmb { L } _ { 2 , e } ^ { \mathrm { s o r t } } ( \tau _ { t } ^ { \prime } ) , . . . , \pmb { L } _ { n _ { e } ^ { \mathrm { e x e } } ( \tau _ { t } ^ { \prime } ) , e } ^ { \mathrm { s o r t } } ( \tau _ { t } ^ { \prime } ) )$ , where $L _ { i , e } ^ { \mathrm { s o r t } } ( \tau _ { t } ^ { \prime } )$ is the i-th least residual task size in $\mathcal { L } _ { \mathcal { M } _ { e } ( \tau _ { t } ^ { \prime } ) } ^ { \mathrm { r e s } }$ . Then, it satisfies

$$
\begin{array}{r l} & {\hat {T} _ {m} + \sum_ {m ^ {\prime} \in \mathcal {M} _ {e} (\tau_ {t} ^ {\prime})} \hat {T} _ {m ^ {\prime}} ^ {a _ {t}} = \sum_ {i = 1} ^ {n _ {e} ^ {\mathrm{exe}} (\tau_ {t})} (n _ {e} ^ {\mathrm{exe}} - i + 1) \mathrm{min} \Bigg (\hat {T} _ {i, e} ^ {\mathrm{dur}}, \mathrm{max} \Bigg (\hat {T} _ {m} ^ {\mathrm{off}} - \sum_ {j = 1} ^ {i - 1} \hat {T} _ {j, e} ^ {\mathrm{dur}}, 0 \Bigg) \Bigg)} \\ & {\qquad + \sum_ {i = 1} ^ {n _ {e} ^ {\mathrm{exe}} (\tau_ {t} ^ {\prime})} \frac {\eta}{f _ {e}} (n _ {e} ^ {\mathrm{exe}} (\tau_ {t} ^ {\prime}) - i + 1) ^ {2} (L _ {i, e} ^ {\mathrm{sort}} (\tau_ {t} ^ {\prime}) - L _ {i - 1, e} ^ {\mathrm{sort}} (\tau_ {t} ^ {\prime})) + \hat {T} _ {m} ^ {\mathrm{off}},} \end{array}\tag{28}
$$

where $\hat { T } _ { m } ^ { \mathrm { o f f } }$ is the estimated offloading delay for task m given in Eq. (5). In the right-hand-side of Eq. (28), the first term estimates the sum of delay for tasks $\boldsymbol { \mathcal { M } } _ { e } ( \boldsymbol { \tau } _ { t } )$ from time instant $\tau _ { t }$ to $\tau _ { t } ^ { \prime }$ The second term estimates the sum of delay for tasks $\boldsymbol { \mathcal { M } } _ { e } ( \boldsymbol { \tau } _ { t } ^ { \prime } )$ from time instant $\tau _ { t } ^ { \prime }$ to infinity. The expression $\begin{array} { r } { \frac { \eta } { f _ { e } } ( L _ { i , e } ^ { \mathrm { s o r t } } ( \tau _ { t } ^ { \prime } ) - L _ { i - 1 , e } ^ { \mathrm { s o r t } } ( \tau _ { t } ^ { \prime } ) ) } \end{array}$ in Eq. (28) represents the required time from completing residual size $L _ { i - 1 , e } ^ { \mathrm { s o r t } } ( \tau _ { t } ^ { \prime } )$ to completing residual size $L _ { i , e } ^ { \mathrm { s o r t } } ( \tau _ { t } ^ { \prime } )$ . We set $L _ { 0 , e } ^ { \mathrm { s o r t } } ( \tau _ { t } ^ { \prime } ) = 0$ To summarize, if the agent offloads task m to server e at step $t ,$ the reward of delay is

$$
\begin{array}{l} r _ {\mathrm{T}} (\pmb {s} _ {t}, a _ {t}) = - \hat {T} _ {m} ^ {\mathrm{off}} + \sum_ {i = 1} ^ {n _ {e} ^ {\mathrm{exe}} (\tau_ {t})} (n _ {e} ^ {\mathrm{exe}} (\tau_ {t}) - i + 1) \hat {T} _ {i, e} ^ {\mathrm{dur}} \\ - \sum_ {i = 1} ^ {n _ {e} ^ {\mathrm{exe}} (\tau_ {t})} (n _ {e} ^ {\mathrm{exe}} - i + 1) \min \Bigg (\hat {T} _ {i, e} ^ {\mathrm{dur}}, \max \left(\hat {T} _ {m} ^ {\mathrm{off}} - \sum_ {j = 1} ^ {i - 1} \hat {T} _ {j, e} ^ {\mathrm{dur}}, 0\right) \Bigg) \\ - \sum_ {i = 1} ^ {n _ {e} ^ {\mathrm{exe}} (\tau_ {t} ^ {\prime})} \frac {\eta}{f _ {e}} (n _ {e} ^ {\mathrm{exe}} (\tau_ {t} ^ {\prime}) - i + 1) ^ {2} (L _ {i, e} ^ {\mathrm{sort}} (\tau_ {t} ^ {\prime}) - L _ {i - 1, e} ^ {\mathrm{sort}} (\tau_ {t} ^ {\prime})). \end{array}\tag{29}
$$

To achieve the GMORL algorithm, we compute a scalarized reward given preference ω:

$$
r _ {\pmb {\omega}} (\pmb {s} _ {t}, a _ {t}) = \pmb {\omega} ^ {T} \times (\alpha_ {\mathrm{T}} r _ {\mathrm{T}} (\pmb {s} _ {t}, a _ {t}), \alpha_ {\mathrm{E}} r _ {\mathrm{E}} (\pmb {s} _ {t}, a _ {t})),\tag{30}
$$

where $\alpha _ { \mathrm { T } }$ and $\alpha _ { \mathrm { E } }$ are coefficients for adjusting delay $r _ { \mathrm { T } } ( t )$ and energy consumption $r _ { \mathrm { E } } ( t )$ to the same order of magnitude. The total reward is

$$
R _ {\omega} = \sum_ {t = 1} ^ {T} r _ {\omega} (\pmb {s} _ {t}, a _ {t}).\tag{31}
$$

## 3.2 Generalizable Neural Network Architecture

In the following, we first present the neural network architecture. When applying DRL-based methods to schedule tasks for multi-edge systems, the generalization problem arises. That is, the output of a neural network has a fixed length, but the number of edge server $E \in { \mathcal { C } } _ { E }$ are not the same in different MEC systems, which means that the trained neural network is not directly applicable to new environments. To tackle this challenge, we introduce a novel neural network architecture for the GMORL algorithm to accomplish generalization. The neural network architecture is shown in Fig. 1. The neural network takes the state information of each server and the context as input, processes the features of each server individually through convolutional modules, then aggregates all features through MLP modules, and finally, for the actor network, outputs the selection probabilities for each server, and for the critic network, outputs the values of each server.

To resolve the inherent conflict between dekay and energy consumption, we employ the Discrete-SAC algorithm to optimize a scalarized reward. For the Discrete-SAC-based algorithm, the neural networks contain a policy network with parameters $\phi ,$ , two local Q-function networks with parameters $\pmb { \theta } _ { 1 }$ and $\pmb { \theta } _ { 2 } .$ , respectively, and two target Q-function networks with parameters ${ \bar { \theta } } _ { 1 }$ and ${ \bar { \theta } } _ { 2 } .$ , respectively. The policy network and the Q-function network share a similar structure. For the policy network, the pre-output is probability vector $\pi _ { \phi } ^ { \prime } ( \cdot | s _ { t } )$ without normalization. For a Q-function network, the output is an estimated Q-value vector $Q _ { \theta } ^ { \prime } ( s _ { t } , \cdot )$

The neural network receives state $\mathbf { } _  \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf \mathbf { } \mathbf { } \mathbf \mathbf { } \mathbf { } \mathbf \mathbf { } \mathbf { } \mathbf \mathbf { } \mathbf \mathbf { } \mathbf { } \mathbf \mathbf { } \mathbf \mathbf { } \mathbf \mathbf { } \mathbf \mathbf { } \mathbf $ as input, and it can work for the environments with any server quantity $E \in { \mathcal { C } } _ { E }$ . We split the input state $\mathbf { \Delta } _ { \mathbf { \mathcal { S } } _ { t } }$ into two parts which have $\pmb { s } _ { t } ^ { \prime } = \{ \pmb { s } _ { t , e } | e \in \mathcal { E } \} \cup \{ \pmb { \mathscr { s } } _ { t , e } | e \notin$ $\bar { \mathcal { E } } \wedge e \in \mathcal { C } _ { E } \}$ and $\mathbf { \Delta } _ { \mathbf { { s } } _ { t } ^ { \prime \prime } } = \bar { \boldsymbol { \omega } }$ . After receiving input, the neural network processes it through convolution layers and MLP layers to generate a preliminary pre-output.

Different contexts may have different numbers of edge servers $E .$ . However, the dimensions of $\pi _ { \phi } ^ { \prime } ( \cdot | s _ { t } )$ and $Q _ { \theta } ^ { \prime } ( s _ { t } , \cdot )$ are fixed. To design a neural network suitable for any number of edge server $E \in \mathcal { C } _ { E }$ , we expand the action space from $\mathcal { A } = \mathcal { E } = \{ 0 , 1 , 2 , \dotsc , E \}$ to $\mathcal { A } ^ { \prime } = \mathcal { E } =$ $\{ 0 , 1 , 2 , \dots , E , \dots , E ^ { \mathrm { m a x } } \}$ . Thus, the length of pre-outputs $\pi _ { \phi } ^ { \prime } ( \cdot | \dot { \boldsymbol { s } } _ { t } )$ and $Q _ { \theta } ^ { \prime } ( s _ { t } , \cdot )$ are expanded to $E ^ { \mathrm { m a x } } + 1$ . Next, we introduce a masked operator which satisfies

$$
\operatorname{mask} (\pi_ {\phi} ^ {\prime} (a _ {t} | \boldsymbol {s} _ {t})) = \left\{ \begin{array}{l l} \pi_ {\phi} ^ {\prime} (a _ {t} | \boldsymbol {s} _ {t}), & \text {if a_{t} \in\mathcal {A}}, \\ - \infty , & \text {if a_{t} \notin\mathcal {A} and a_{t} \in\mathcal {A} ^{\prime}}. \end{array} \right.\tag{32}
$$

![](images/65e2d81e50a77d2e3abbae58e6e28eeff05218af628b46a949e26dbf6b904191.jpg)  
Figure 1: The neural network architecture of the scheduling policy.

This operator masks the actions of dummy edge servers, making their selection probability zero. We apply the mask operator to each element of vector $\pi _ { \phi } ^ { \prime } ( \cdot | s _ { t } )$ to get a new vector $\bar { \pi } _ { \phi } ^ { \prime \prime } ( \cdot | s _ { t } )$ that satisfies $\pi _ { \phi } ^ { \prime \prime } ( a _ { t } | s _ { t } ) = \mathrm { m a s k } ( \pi _ { \phi } ^ { \prime } ( a _ { t } | s _ { t } ) )$ for $\forall a _ { t } \in { \mathcal { A } } ^ { \prime }$ . Then, we use the softmax regression to normalize vector $\pi _ { \phi } ^ { \prime \prime } ( \cdot | s _ { t } )$ and get the probability vector $\pi _ { \phi } ( \cdot | s _ { t } )$ , via the following softmax expression:

$$
\pi_ {\phi} (a _ {t} | \boldsymbol {s} _ {t}) = \mathrm{softmax} (\pi_ {\phi} ^ {\prime \prime} (a _ {t} | \boldsymbol {s} _ {t})) = \frac {\exp (\pi_ {\phi} ^ {\prime \prime} (a _ {t} | \boldsymbol {s} _ {t}))}{\sum_ {a _ {t} ^ {\prime} \in \mathcal {A} ^ {\prime}} \exp (\pi_ {\phi} ^ {\prime \prime} (a _ {t} ^ {\prime} | \boldsymbol {s} _ {t}))}, \forall a _ {t} \in \mathcal {A} ^ {\prime},\tag{33}
$$

Finally, we apply the mask operator to each element of vector $Q _ { \theta } ^ { \prime } ( s _ { t } , \cdot )$ to get Q-value vector $Q _ { \theta } ( s _ { t } , \cdot )$ . Through this way, the probability $\pi _ { \phi } { \left( a _ { t } ^ { \mathrm { o u t } } | s _ { t } \right) }$ of action $a _ { t } ^ { \mathrm { { \bar { o u t } } } }$ which outside action space $\mathcal { A }$ is set to 0, and Q-value $\mathbf { \dot { Q } } _ { \theta } ^ { \prime } ( a _ { t } ^ { \mathrm { o u t } } , s _ { t } )$ is set to ψ. It constrains an agent to take action and learn policy in effective action space A. Furthermore, it enables a policy π to schedule for any multi-edge system with $E \in { \mathcal { C } } _ { E }$

## 3.3 Policy Update for the GMORL Model

The policy update for the GMORL model with the Discrete-SAC, which is a family of policy gradient methods [28]. We employ the updating method proposed in [29]. The Discrete-SAC algorithm aims to simultaneously maximize the expected reward and entropy to achieve a stochastic policy, and it improves the sample efficiency and robustness of traditional policy gradient methods. The optimal Discrete-SAC policy with maximum entropy objective is

$$
\pi^ {*} = \arg \max _ {\pi} \sum_ {t} ^ {T} \mathbb {E} _ {(\boldsymbol {s} _ {t}, a _ {t}) \sim \rho_ {\pi}} [ \gamma^ {t} (r _ {\boldsymbol {\omega}} (\boldsymbol {s} _ {t}, a _ {t}) + \alpha_ {H} \mathcal {H} (\pi (\cdot | \boldsymbol {s} _ {t}))) ],\tag{34}
$$

where $\rho _ { \pi }$ denotes the trajectory distribution of policy $\pi ,$ and $\alpha _ { H }$ is a temperature parameter that determines the importance of the entropy term. The action probability vector of policy π at state $\mathbf { \boldsymbol { s } } _ { t }$ is $\pi ( \cdot | s _ { t } )$ . The entropy of $\pi ( \cdot | s _ { t } )$ is $\mathcal { H } \big ( \pi ( \cdot | \boldsymbol { s } _ { t } ) \big )$ ), and it satisfies $\mathcal { H } ( \pi ( \cdot | s _ { t } ) ) = - \log \pi ( \cdot | s _ { t } )$

In the policy evaluation step, we can obtain the soft Q-value function by starting from any function $Q : { \mathcal { S } } \times { \mathcal { A } }  \mathbb { R } ^ { 2 }$ and repeatedly applying the modified Bellman backup operator $\tau ^ { \pi }$ which satisfies

$$
\mathcal {T} ^ {\pi} Q (\boldsymbol {s} _ {t}, a _ {t}) = r (\boldsymbol {s} _ {t}, a _ {t}) + \gamma \mathbb {E} _ {\boldsymbol {s} _ {t + 1} \sim \rho_ {\pi}} (V (\boldsymbol {s} _ {t + 1})),\tag{35}
$$

where $V ( \cdot )$ is a soft state-value function of policy $\pi ,$ and it satisfies

$$
V (\pmb {s} _ {t}) = \mathbb {E} _ {a _ {t} \sim \pi} [ Q (\pmb {s} _ {t}, a _ {t}) - \alpha_ {H} \log (\pi (a _ {t} | \pmb {s} _ {t})) ].\tag{36}
$$

$$
\begin{array}{l} J _ {Q} (\boldsymbol {\theta} _ {i}) = \mathbb {E} _ {(\boldsymbol {s} _ {t}, a _ {t}) \sim \mathcal {D}} \left[ \frac {1}{2} \left(Q _ {\boldsymbol {\theta} _ {i}} (\boldsymbol {s} _ {t}, a _ {t}) \right. \right. \\ \left. - \left(r (\boldsymbol {s} _ {t}, a _ {t}) + \gamma \mathbb {E} _ {\boldsymbol {s} _ {t + 1} \sim \mathcal {T}} \left[ V _ {\bar {\boldsymbol {\theta}} _ {i}} (\boldsymbol {s} _ {t + 1}) \right]\right)\right) ^ {2} \Bigg ], \forall i \in \{1, 2 \} \end{array}\tag{37}
$$

Then we train soft Q-function parameters $\pmb \theta _ { i }$ for $i \in \{ 1 , 2 \}$ to minimize the soft Bellman residual. Soft Bellman residual $J _ { Q } ( \pmb \theta _ { i } )$ is given by Eq. (37), where D is a replay buffer of past experiences, and $Q _ { \pmb { \theta } _ { i } } ( \cdot )$ is the soft Q-function with parameters $\theta _ { i }$ . Soft state-value $V _ { \bar { \pmb { \theta } } _ { i } } ( \pmb { s } _ { t + 1 } )$ is estimated by a target Q-function network according to Eq. (36). Based on $J _ { Q } ( \pmb { \theta } _ { i } )$ , we update local soft Q-function parameters $\theta _ { i }$ by

$$
\boldsymbol {\theta} _ {i} \leftarrow \boldsymbol {\theta} _ {i} - \lambda_ {Q} \hat {\nabla} _ {\boldsymbol {\theta} _ {i}} J _ {Q} (\boldsymbol {\theta} _ {i}),\tag{38}
$$

where $\lambda _ { Q }$ is the learning rate of soft Q-function, and $\hat { \nabla } _ { \pmb { \theta } _ { i } } J _ { Q } ( \pmb { \theta } _ { i } )$ is the approximated gradient of $J _ { Q } ( \pmb { \theta } _ { i } )$ . Next, we update target soft Q-function parameters $\bar { \pmb { \theta } } _ { i }$ by

$$
\bar {\boldsymbol {\theta}} _ {i} \leftarrow \beta \boldsymbol {\theta} _ {i} + (1 - \beta) \bar {\boldsymbol {\theta}} _ {i},\tag{39}
$$

where $\beta$ is a target smoothing coefficient. In the policy improvement step, we update policy π according to

$$
\pi_ {\text { new }} = \arg \min _ {\pi \in \Pi^ {\prime}} D _ {\mathrm{KL}} \left(\pi (\cdot | \boldsymbol {s} _ {t}) \left\| \frac {\exp \left(\frac {1}{\alpha_ {H}} Q ^ {\pi_ {\text { old }}} (\boldsymbol {s} _ {t} , \cdot)\right)}{Z ^ {\pi_ {\text { old }}} (\boldsymbol {s} _ {t})}\right) \right.\tag{40}
$$

$$
J _ {\pi} (\boldsymbol {\phi}) = \mathbb {E} _ {\boldsymbol {s} _ {t} \sim \mathcal {D}} \Big [ \pi_ {t} (\cdot , \boldsymbol {s} _ {t}) ^ {T} \left(\alpha_ {H} \log \pi_ {\boldsymbol {\phi}} (\cdot , \boldsymbol {s} _ {t}) - \min \big (Q _ {\boldsymbol {\theta} _ {1}} (\boldsymbol {s} _ {t}, \cdot), Q _ {\boldsymbol {\theta} _ {2}} (\boldsymbol {s} _ {t}, \cdot) \big)\right) \Big ]\tag{41}
$$

where $D _ { \mathrm { K L } } ( \cdot )$ is the Kullback-Leibler (KL)-divergence function, and $\Pi ^ { \prime }$ is a policy search space that is applied to restrict the policy. The partition function $Z ^ { \pi _ { \mathrm { o l d } } } \left( \cdot \right)$ normalizes the policy distribution, ensuring that it sums up to a probability of 1 over the entire action space. We optimize policy parameters $\phi$ to minimize the KL-divergence by the policy objective $J _ { \pi } ( \phi )$ which is given by Eq. (41), where $Q _ { \pmb { \theta } _ { 1 } } ( \cdot , s _ { t } )$ and $Q _ { \theta _ { 2 } } ( \cdot , s _ { t } )$ are the Q-value vectors for all actions at state $\mathbf { \Delta } _ { \mathbf { \mathcal { S } } _ { t } }$ , with parameters $\pmb { \theta } _ { 1 }$ and $\pmb { \theta } _ { 2 }$

We denote the policy gradient direction for the reward of delay $r _ { \mathrm { T } }$ as $\hat { \nabla } _ { \phi } J _ { \pi , \mathrm { T } } ( \phi )$ , and denote the policy gradient direction for the reward of energy consumption $r _ { \mathrm { E } }$ as $\hat { \nabla } _ { \phi } J _ { \pi , \mathrm { E } } ( \phi )$ . The policy gradient direction for reward $r _ { \omega }$ is

$$
\hat {\nabla} _ {\phi} J _ {\pi , \pmb {\omega}} (\phi) = \pmb {\omega} ^ {T} \times (\hat {\nabla} _ {\phi} J _ {\pi , \mathrm{T}} (\phi), \hat {\nabla} _ {\phi} J _ {\pi , \mathrm{E}} (\phi)).\tag{42}
$$

Given the gradient directions of the delay objective and the energy consumption objective, a policy can reach the Pareto front by following a direction in ascent simplex [30]. An ascent simplex is defined by the convex combination of single–objective gradients.

Synthesizing the above, we update policy parameters $\phi$ by

$$
\phi \leftarrow \phi - \lambda_ {\pi} \hat {\nabla} _ {\phi} J _ {\pi} (\phi),\tag{43}
$$

where $\lambda _ { \phi }$ is the learning rate of policy parameters $\phi ,$ , and $\hat { \nabla } _ { \phi } J _ { \pi } ( \phi )$ is the approximated gradient of $J _ { \pi } ( \phi )$ .

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 1 The GMORL Scheduling Algorithm
1: Initialize replay buffer D, policy network parameters  $\phi$ , the parameters of two local Q-function networks  $\theta_{1}$  and  $\theta_{2}$ , the parameters of two target Q-function networks  $\bar{\theta}_{1}$  and  $\bar{\theta}_{2}$ .
2: Given training context space C and set preference context space  $\Omega$  from Eq. (32).
3: for each epoch:  $i_{ep} \leftarrow 1, \ldots, N_{ep}$  do
4:    for each environment:  $i_{env} \leftarrow 1, \ldots, N_{g}$  do
5:    $\omega \leftarrow \omega_{i_{env}}$ 
6:    $E \sim C_{E}$ 
7:    $f_{0} \sim C_{f_{0}}$ 
8:    for each edge server:  $e' \leftarrow 1, \ldots, E$  do
9:    $f_{e'} \sim C_{f_{\varepsilon'}}$ 
10:    end for
11:    for each step:  $t \leftarrow 1, \ldots, T$  do
12:    $a_{t} \sim \pi_{\phi}(\cdot | s_{t})$ 
13:    $s_{t+1} \sim T(s_{t+1} | s_{t}, a_{t})$ 
14:    $D \leftarrow D \cup \{\langle s_{t}, a_{t}, r_{\omega}(s_{t}, a_{t}), s_{t+1} \rangle\}$ 
15:    end for
16:    for each update round:  $i_{up} \leftarrow 1, \ldots, N_{up}$  do
17:    Sample experiences from D
18:    Compute  $J_{Q}(\theta_{i})$  for  $i \in \{1, 2\}$ ,  $J_{\pi}(\phi)$ , and  $J(\alpha_{H})$  by Eq. (37), Eq. (41), and Eq. (44).
19:    Update the parameters according to Eq. (38), Eq. (39), Eq. (33) and Eq. (45):
20:    $\theta_{i} \leftarrow \theta_{i} - \lambda_{Q} \hat{\nabla}_{\theta_{i}} J_{Q}(\theta_{i})$  for  $i \in \{1, 2\}$ 
21:    $\phi \leftarrow \phi - \lambda_{\pi} \hat{\nabla}_{\phi} J_{\pi}(\phi)$ 
22:    $\alpha_{H} \leftarrow \alpha_{H} - \lambda_{\alpha} \hat{\nabla}_{\alpha_{H}} J(\alpha_{H})$ 
23:    $\bar{\theta}_{i} \leftarrow \beta \theta_{i} + (1 - \beta) \bar{\theta}_{i}$  for  $i \in \{1, 2\}$ 
24:    end for
25:    end for
26: end for
27: Output policy  $\pi_{\phi}$
</div>

Finally, the temperature parameter $\alpha _ { H }$ is learnable. The temperature objective is

$$
\begin{array}{r} J (\alpha_ {H}) = \pi_ {t} (\pmb {s} _ {t}) ^ {T} \\ \times \left[ - \alpha_ {H} (\log (\pi_ {\phi} (\pmb {s} _ {t})) + \overline {{H}}) \right] \end{array}\tag{44}
$$

where $\bar { \mathcal { H } }$ is a constant vector equal to the hyperparameter representing the target entropy. We update α<sub>H</sub> by

$$
\alpha_ {H} \leftarrow \alpha_ {H} - \lambda_ {\alpha} \hat {\nabla} _ {\alpha_ {H}} J (\alpha_ {H}),\tag{45}
$$

where $\lambda _ { \alpha }$ is the learning rate of temperature parameter $\alpha _ { H }$ , and $\hat { \nabla } _ { \alpha _ { H } } J ( \alpha _ { H } )$ is the approximated gradient of $J ( \alpha _ { H } )$ . We present the proposed GMORL in Algorithm 1.

## 4 Performance Analysis

## 4.1 Generalization Performance

We propose a training approach to enable the generalization for GMORL. A generalization policy learns in training context space and strives to generalize to the entire context space C. It aims at achieving optimal offloading scheduling for any context $c \in { \mathcal { C } }$ . Context space $\mathcal { C }$ represents the range of generalization. We use the domain randomization approach, which creates various MEC environments with randomized properties to train a policy.

When the gradient directions of the two objectives are not completely opposite, the ascent simplex exists. If the gradient direction lies within the scent simplex, both objectives can be optimized simultaneously, and the gradient descent algorithm can reach a Pareto local optimum. We sample

$N _ { \mathrm { g } }$ contexts to generate $N _ { \mathrm { g } }$ MEC environments for one epoch. We define a preference set with $N _ { \mathrm { g } }$ preferences as $\Omega _ { N _ { \mathrm { g } } } = \{ \omega _ { 1 } , \omega _ { 2 } , \ldots , \omega _ { N _ { \mathrm { g } } } \}$ , where the i-th preference is

$$
\boldsymbol {\omega} _ {i} = \left(\frac {i - 1}{N _ {\mathrm{g}} - 1}, 1 - \frac {i - 1}{N _ {\mathrm{g}} - 1}\right).\tag{46}
$$

The training preference context space is $\Omega _ { N _ { \mathrm { g } } }$ , and it has equally spaced intervals, each having a length of $\displaystyle \frac { 1 } { N _ { \mathrm { g } } - 1 }$ . We sequentially apply the $N _ { \mathrm { g } }$ preferences to the corresponding $N _ { \mathrm { g } }$ environments. We randomly sample the number of edge server $E ,$ the CPU frequency of cloud server $f _ { 0 }$ and the CPU frequency of edge servers $\scriptstyle f _ { \varepsilon ^ { \prime } }$ in training context space for each MEC environment.

## 4.2 Convergence Performance

We prove the convergence properties of GMORL:

Theorem 1 (Convergence of GMORL Scheduling Algorithm) Given a sufficiently diverse action-state space, the GMORL scheduling algorithm converges to the optimal policy $\pi ^ { * }$ and Q-function $Q ^ { \ast }$ as the number of epochs $N _ { \mathrm { e p } }$ and update rounds $N _ { \mathrm { u p } }$ approach infinity.

Theorem 1 guarantees that the GMORL algorithm can find the optimal scheduling policy with sufficient training iterations. The proof of Theorem 1 is in Appendix E.1.

The structure of the GMORL algorithm is illustrated in Appendix F.

Denote the training rounds as $N _ { \mathrm { e p } } .$ , the number of sampled environments in each round as $N _ { \mathrm { g } } ,$ , the time steps contained in each environment as $T$ , the update rounds as $N _ { \mathrm { u p } } ,$ , the number of edge servers as E and the number of neural network parameters as $N _ { \mathrm { n e t } }$ . Regarding the complexity of the GMORL algorithm, we can obtain it from the following corollary:

Corollary 1 (Complexity of GMORL) In the $N _ { \mathrm { e p } }$ training session, the computational complexity of GMORL algorithm is $\dot { O } ( N _ { \mathrm { e p } } ( N _ { \mathrm { g } } ( E + T ) + N _ { \mathrm { u p } } ^ { \ } N _ { \mathrm { n e t } } ) )$ .

The proof of Corollary 1 has shown in Appendix D.2.

## 4.3 Performance Difference Bound

Our goal is to minimize the objective function, defined in Eq. (12) as

$$
J (\pi) = \min _ {\pi} \mathbb {E} _ {\mathbf {x} \sim \pi} \left[ \sum_ {m \in \mathcal {M}} \gamma^ {m} (\omega_ {\mathrm{T}} T _ {m} + \omega_ {\mathrm{E}} E _ {m}) \right].\tag{47}
$$

Consequently, we anticipate that $J ( \pi _ { t } ) > J ( \pi _ { t + 1 } )$ , indicating an improvement in policy from $\pi _ { t }$ to $\pi _ { t + 1 }$ . To substantiate the theoretical guarantees of our GMORL algorithm, we derive a lower bound for the performance difference between adjacent policies.

Theorem 2 (Performance Difference Bound of GMORL) For any two adjacent policies $\pi _ { t }$ and $\pi _ { t + 1 }$ in the policy space of GMORL, their performance difference $\dot { \Delta J } = J ( \dot { \pi } _ { t } ) - \dot { J ( \pi } _ { t + 1 } )$ is lower bounded by:

$$
\Delta J \geq A \| \pi_ {t} - \pi_ {t + 1} \| _ {1},\tag{48}
$$

where $A = \mathrm { m i n } \{ \Phi _ { m i n } , \mathrm { m i n } _ { m } \{ \gamma ^ { m } \omega _ { T } \} \} , \Phi _ { m i n } = \mathrm { m i n } _ { m , e } \{ \gamma ^ { m } \omega _ { E } \Phi _ { m , e } \}$ , and $\begin{array} { r } { \Phi _ { m , e } = p ^ { o f f } \frac { L _ { m } } { C _ { u , e } } + } \end{array}$ $\kappa \eta f _ { e } ^ { 2 } L _ { m }$

Theorem 2 ensures a lower bound on the performance improvement for each policy update in the GMORL algorithm, guaranteeing the stability of the model. The proof of Theorem 2 is in Appendix D.3.

## 5 Experimental Results

In this section, we evaluate the performances of the GMORL scheduling scheme and compare it with benchmarks. First, we introduce the simulation setup and evaluation metrics. Then, we specifically investigate convergence, multi-objective performances, and generalization. Finally, we analyze the Pareto fronts and compare them with the benchmarks.

![](images/38645400e4ae90baaa7578ac2f010537ad903237a9b67fb985ee115a97c3f13a.jpg)  
Figure 2: Pareto fronts of the proposed GMORL algorithm and benchmark algorithms.

## 5.1 Simulation Setup

In the training stage, we set $N _ { g } ~ = ~ 6 4$ The context space of edge server quantity is $\mathcal { C } _ { E } ~ =$ $\{ 1 , 2 , \ldots , 8 \}$ . The context space of cloud server CPU frequency is $\mathcal { C } _ { f _ { 0 } } ~ = ~ [ 3 . 5 , 4 . 5 ]$ GHz. The context space of edge server CPU frequency is $\mathcal { C } _ { f _ { \varepsilon ^ { \prime } } } = [ 1 . \bar { 7 5 } , 2 . \bar { 2 } 5 ]$ GHz. In the testing stage, we set $N _ { q } = 1 0 1$ (corresponding to an increment of 0.01). The context space of edge server quantity is $\mathcal { C } _ { E } = \{ 1 , 2 , \dots , 1 0 \}$ . The context space of cloud server CPU frequency is $\mathcal { C } _ { f _ { 0 } } = [ 3 . 0 , 5 . 0 ]$ GHz. The context space of edge server CPU frequency is $\mathcal { C } _ { f _ { \varepsilon ^ { \prime } } } = [ 1 . 5 , 2 . 5 ] \mathrm { \bar { G } H z }$ . The testing context space has a larger scope than the training context space. We provide the detailed simulation setup of our model parameters in Table II. In the Appendix, we present the context space settings in Table A1.

Table 2: Model Parameters

<table><tr><td>Resource Scheduling Hyperparameters</td><td>Values</td></tr><tr><td>The number of steps for one episode  $T$ </td><td>100</td></tr><tr><td>Step duration  $\Delta t$ </td><td>1 s</td></tr><tr><td>The number of users  $U$ </td><td>10</td></tr><tr><td>The number of tasks  $M$ </td><td>100</td></tr><tr><td>System bandwidth  $W$ </td><td>16.6MHz [31]</td></tr><tr><td>Offloading power  $p^{\text{off}}$ </td><td>10 mW</td></tr><tr><td>The number of CPU cycles  $\eta$  for one-bit task</td><td> $10^{3}$ </td></tr><tr><td>Effective capacitance coefficient  $\kappa$ </td><td> $5 \times 10^{-31}$ </td></tr><tr><td>Poisson arrival rate  $\lambda_{p}$  for each user</td><td>0.1</td></tr><tr><td>DRL Hyperparameters</td><td>Values</td></tr><tr><td>The number of epochs for training  $N_{\text{ep}}$ </td><td>4000</td></tr><tr><td>The number of environments for one epoch  $N_{\text{g}}$ </td><td>64</td></tr><tr><td>Update round  $N_{\text{up}}$ </td><td>10</td></tr><tr><td>Replay memory</td><td> $1 \times 10^{5}$ </td></tr><tr><td>Batch size</td><td>4096</td></tr><tr><td>SAC temperature parameter  $\alpha_{H}$ </td><td>0.05</td></tr><tr><td>The learning rate of policy  $\lambda_{\pi}$ </td><td> $1 \times 10^{-6}$ </td></tr><tr><td>The learning rate of soft Q-function  $\lambda_{Q}$ </td><td> $1 \times 10^{-6}$ </td></tr><tr><td>The learning rate of temperature  $\lambda_{\alpha_{H}}$ </td><td>0</td></tr><tr><td>Discount factor  $\gamma$ </td><td>0.95</td></tr></table>

![](images/12d829936e981c5ad7767cf6e39a7943dee7c908a89b8804f55ae80ffbc22b80.jpg)  
(a) Pareto fronts of total delay and energy consumption

![](images/126cd6ea27856ae0c87026cedbeb6527e2c1994d023892677831f7befab852c3.jpg)  
(b) Pareto fronts of total delay and energy consumption per Mbits task  
Figure 3: Pareto fronts of the proposed GMORL algorithm.

## 5.2 Performance Comparison

## 5.2.1 Baseline Algorithms

We evaluate the performance of the proposed GMORL algorithms with a single policy and compare it with a linear upper confidence bound (LinUCB)-based scheme [32], a multi-policy MORL scheme [24], a simulated annealing (SA)-based scheme, and a random-based scheme. LinUCB algorithms belong to contextual multi-arm bandit (MAB) algorithms, widely used in task offloading problems [33, 34]. Some work [4, 34, 35] apply heuristic methods to schedule for offloading. The non-dominated sorting genetic algorithm (NSGA-II) [36, 37], and Pareto Q-learning [38] are well-known multi-objective solution approaches. Furthermore, we compare our algorithm with a multi-policy MORL approach [39] based on the standard Discrete-SAC algorithm. We provide a detailed introduction to the baseline algorithms in the Appendix.

We evaluate these schemes with the number of edge servers $E = 6 .$ . Notably, in the multi-policy MORL scheme, we build 101 Discrete-SAC policy models for the 101 preference in $\Omega _ { 1 0 1 }$ correspondingly. We train each policy model with $f _ { 0 } = 4$ GHz and $f _ { e ^ { \prime } } = \bar { 2 } \mathrm { G H z }$ . This method has no generalization ability. A well-trained policy model is applicable to a specific context. However, benefiting from focusing on a specific context, this method is more likely to achieve optimal performance. We apply the method to determine the upper bound of the Pareto front.

Then we show the simulation results. Fig. 2 illustrates the Pareto fronts of these schemes. The Pareto front of the multi-policy MORL scheme shows an approximate upper bound of the performance. The result indicates that the proposed GMORL scheme dominates the LinUCB-based, SA-based, random-based schemes, NSGA-II, and Pareto Q-learning. Our method can approach the upper bound. We select the maximum delay and energy consumption across all Pareto fronts as the reference point to compute the hypervolumes. The Pareto front hypervolume of the proposed GMORL scheme is 64.1, the LinUCB-based scheme is 57.9, the multi-policy MORL scheme is 64.3, the SA-based scheme is 30.2, and the random-based is 29.0. The results show that the Pareto front hypervolume of the proposed GMORL scheme outperforms the LinUCB-based scheme by $\frac { 6 4 . 1 - 5 7 . 9 } { 5 7 . 9 } \ = \ 1 0 . 7 \%$ , outperforms the SA-based scheme by $\begin{array} { r } { \frac { 6 4 . 1 - 3 0 . 2 } { 3 0 . 2 } = 1 1 2 . 3 \% } \end{array}$ , and outperforms the random-based scheme by $\begin{array} { r } { \frac { 6 4 . 1 - 2 9 . 0 } { 2 9 . 0 } = 1 2 1 . 0 \% } \end{array}$ . The Pareto front hypervolume of the proposed GMORL scheme is $\begin{array} { r } { \frac { 6 4 . 3 - 6 4 . 1 } { 6 4 . 3 } = 0 . { \overset { \sim } { 3 } \% } } \end{array}$ lower than but close to the approximate upper bound.

## 5.3 Performance Analysis

## 5.3.1 State description in no-uninstall scenario

Multi-Edge: To evaluate the performance of the proposed GMORL algorithm in scenarios with different server quantities, we tested its Pareto front. In Fig. 3, each point corresponds to a preference. In these scenarios, the context space of cloud server CPU frequency is $\mathcal { C } _ { f _ { 0 } } \overset { \cdot } { = } \left[ 3 . 5 , 4 . 5 \right]$ GHz, the context space of edge server CPU frequency is $\mathcal { C } _ { f _ { \varepsilon ^ { \prime } } } = [ 1 . 7 5 , 2 . 2 5 ]$ GHz. The mean of task size, represented by ${ \bar { L } } ,$ is determined by Eq. (1) to balance the supply and demand of computational capability. The performances are computed per 1 Mbits task in Fig. 3b for a fair comparison. As the number of edge servers increases, the Pareto front of a more edge servers case can dominate the less one. The result shows that though more edge servers match more task demands, deploying more edge servers can significantly improve delay and energy consumption per Mbits tasks for each preference.

![](images/c9ccf1a1ff6643125f956bcd5509675c425e7ac9e42d583f66a700ce1fc68ff5.jpg)

![](images/15ad1146127de370fb0a16f6073477831e31961cd0f38ade4db7b7829f138fcc.jpg)  
(a) Total delay per Mbits task  
(b) Total energy consumption per Mbits task

Figure 4: Total task delay and energy consumption with different preferences.  
![](images/90fa43fc7322aa3fffc0ba519431af70200d4e034a6641c9e61f1adecf77169d.jpg)  
Figure 5: Pareto fronts of GMORL policy and reference policy when $E = 6 , \mathcal { C } _ { f _ { 0 } } = [ 3 . 0 , 5 . 0 ]$ GHz and $\mathcal { C } _ { f _ { \varepsilon ^ { \prime } } } = [ 1 . 5 , 2 . 5 ]$ GHz.

Multi-Preference: We conducted specific tests for delay and energy consumption.

Fig. 4a illustrates total delay performances per Mbits task with different preferences of delay ω<sub>T</sub>. Fig. 4b illustrates total energy consumption performances per Mbits task with different preferences of energy consumption $\omega _ { \mathrm { E } }$ . These simulation results validate that the proposed GMORL algorithm can achieve trade-offs between delay and energy consumption by tuning a preference ω. Furthermore, we observe that the more edge servers in an MEC system, the less delay and energy consumption per Mbits task the system performs. This further corroborates the conclusion drawn in the preceding paragraph.

![](images/adb445f321eb258b42ed545d705b08a46a2d8dd99b17dae34b881b5a090efa50.jpg)  
(a)

![](images/ce62c4005715cc1981a56797baae96b87ef60d06fd8ef0bb9f889c1d463c9e39.jpg)  
(b)

![](images/cb6178742f01eee825c7dbe36839a374172989bba59963ab841355c1d8e897d5.jpg)  
(c)

![](images/c05a6f6875f5b5194a9761b70ac8dea40554cf45651e392a3f1274b77449b5cb.jpg)  
(d)  
Figure 6: CPU frequency generalization experiment when $E = 6 , \bar { L } = 1 6 \mathrm { M b i t s }$ regarding total task delay (a), (b) and total energy consumption (c), (d). The greater similarity between the performances of the two policies indicates a higher degree of CPU frequency generalization of the GMORL policy.

## 5.3.2 Generalization analysis

In this subsection, we evaluate the generalization of the proposed GMORL scheme from the number of edge servers $E ,$ cloud server CPU frequency $f _ { 0 } ,$ and edge server CPU frequency $f _ { e ^ { \prime } }$ . To evaluate the generalization of the proposed algorithm, we consider a reference policy where the training context space is equivalent to the testing context space. The reference policy serves as an upper bound for performance against which we compare the GMORL policy. Smaller discrepancies between the two indicate superior generalization of the GMORL policy.

![](images/df9cd5b3a627eab35f218412fa9aac5241df8ef724426224fd938141d3310e96.jpg)  
Figure 7: Pareto fronts of GMORL policy and reference policy when $E = 9 , \mathcal { C } _ { f _ { 0 } } = [ 3 . 0 , 5 . 0 ]$ GHz and $\mathcal { C } _ { f _ { \varepsilon ^ { \prime } } } = [ 1 . 5 , 2 . 5 ]$ GHz.

• Reference policy: The same method as GMORL scheme, however, we define it as $R e f -$ erence policy due to it trained in a larger context space with $\Omega _ { 6 4 } , \mathcal { C } _ { E } = \{ 1 , 2 , \ldots , 1 0 \}$ $\mathcal { C } _ { f _ { 0 } } = [ 3 . 0 , 5 . 0 ]$ GHz and $\mathcal { C } _ { f _ { \varepsilon ^ { \prime } } } = [ 1 . 5 , 2 . 5 ]$ GHz, where $\mathcal { C } _ { E } , \mathcal { C } _ { f _ { 0 } }$ and $\mathcal { C } _ { f _ { \varepsilon ^ { \prime } } }$ are consistent with the testing context space.

## Generalization of CPU frequencies :

First, we study the CPU frequency generalization of the proposed GMORL scheme. Fig. 5 illustrates the Pareto fronts of the GMORL policy and reference policy with edge server quantity $E = 6 .$ . For the GMORL policy, the CPU frequency context space during training has a smaller range ([1.75, 2.25] GHz) than during testing ([2.00, 2.50] GHz). For the reference policy, the CPU frequency context space during training is consistent with during testing. We use the Pareto front of reference policy as a reference for comparison. The hypervolume of reference policy is 81.69, and the hypervolume of the GMORL policy is 80.29, the hypervolume error between the two policies is 81 $\begin{array} { r } { \frac { . 6 9 - 8 0 . 2 9 } { 8 0 . 2 9 } = 1 . 7 \% } \end{array}$

Next, we evaluate the total delay and energy consumption performances with different CPU frequencies. Fig. 6a and $\mathrm { f i g . }$ . 6b illustrate the total task delay of the GMORL policy and the reference policy with edge server quantity $E = 6$ , the mean of task size $\bar { L } = 1 \bar { 6 }$ Mbits, and preference $\omega = ( 1 , 0 )$ This group of numerical results indicates that with the increase of $f _ { 0 }$ or $f _ { e ^ { \prime } }$ , the delay changing trend of the GMORL policy and the reference policy is basically consistent. It is the same for regions outside the training context space of GMORL policy.

Fig. 6c and fig. 6d illustrates the total energy consumption of GMORL policy and reference policy with the number of edge server $E = 6$ , the mean of task size $\bar { L } = 1 6$ Mbits, and preference $\omega = ( 0 , 1 )$ . The simulation results show that with the increase of $f _ { 0 }$ or $f _ { e ^ { \prime } }$ , the energy consumption changing trend of the GMORL and the reference policies are highly consistent. It is the same for the regions that are outside the training context space of the GMORL policy. These results also show that the proposed GMORL scheme has a certain generalization ability to achieve superior performance in the CPU frequencies outside the training context space.

Generalization of server quantities : We compute the Pareto front of the GMORL policy and reference policy with the number of edge servers $E = 9$ , which are outside the GMORL policy’s training context space. Fig. 7 illustrates the Pareto fronts. The result shows that though there is a certain gap between the two Pareto fronts, they present a moderate level of concordance in value.

These simulation results show that the proposed GMORL scheme has a strong generalization capability to schedule tasks for the MEC systems with CPU frequencies or the number of edge servers outside the training context space. As demonstrated in Fig. 3a, the proposed GMORL scheme exhibits generalization in scheduling MEC systems with varying quantities of edge servers within the training context space. When scheduling for the MEC systems with a number of edge servers outside the training context space, the performance of the proposed GMORL scheme has a certain gap compared to a well-trained one. However, when designing a policy model, the neural network architecture determines the maximum number of edge servers $E ^ { \mathrm { { \bar { m a x } } \prime } }$ that the policy can schedule. Generally, it satisfies $E ^ { \mathrm { m a x } \prime } = E ^ { \mathrm { m a x } }$ , where $E ^ { \mathrm { m a x } }$ is the maximum edge server quantity in training context space. Specifically, in fig. 7, it satisfies E = 9, $E ^ { \mathrm { m a x } \prime } = 1 0 $ but $E ^ { \mathrm { m a x } } = 8$ . The occurrence is generally infrequent. This occurrence typically only arises when computing resources or training time are constrained.

## 6 Conclusion

In this work, we investigated the offloading problem in MEC systems and proposed a GMORLbased algorithm that can generalize to diverse MEC systems and achieve Pareto fronts. The proposed GMORL method has two key advantages: (1) it employs a single-policy GMORL framework for various preferences rather than multiple-policy models. (2) it can adapt to heterogeneous MEC systems with varying CPU frequencies and server quantities.

We present a novel contextual MOMDP framework for the multi-objective offloading problem in MEC systems. Our framework includes three key components: (1) a well-designed encoding method to construct features of multi-edge MEC systems. (2) a sophisticated reward function to evaluate the immediate utility of delay and energy consumption. (3) an innovative neural network architecture that supports policy generalization. Simulation results demonstrate the effectiveness of our proposed GMORL scheme, which achieves Pareto fronts in various scenarios and outperforms benchmarks by up to 121.0%.

## References

[1] Farhan Pervez, Ajmery Sultana, Cungang Yang, and Lian Zhao. Energy and latency efficient joint communication and computation optimization in a multi-uav-assisted mec network. IEEE Transactions on Wireless Communications, 23(3):1728–1741, 2024.

[2] Ji Li, Hui Gao, Tiejun Lv, and Yueming Lu. Deep reinforcement learning based computation offloading and resource allocation for mec. In 2018 IEEE Wireless Communications and Networking Conference (WCNC), pages 1–6. IEEE, 2018.

[3] Fang Fang, Yanqing Xu, Zhiguo Ding, Chao Shen, Mugen Peng, and George K Karagiannidis. Optimal task assignment and power allocation for noma mobile-edge computing networks. arXiv preprint arXiv:1904.12389, 2019.

[4] Tuyen X Tran and Dario Pompili. Joint task offloading and resource allocation for multi-server mobile-edge computing networks. IEEE Transactions on Vehicular Technology, 68(1):856– 868, 2018.

[5] Gaofeng Cui, Xiaoyao Li, Lexi Xu, and Weidong Wang. Latency and energy optimization for mec enhanced sat-iot networks. IEEE Access, 8:55915–55926, 2020.

[6] Lei Lei, Huijuan Xu, Xiong Xiong, Kan Zheng, Wei Xiang, and Xianbin Wang. Multiuser resource control with deep reinforcement learning in iot edge computing. IEEE Internet of Things J., 6(6):10119–10133, 2019.

[7] Feibo Jiang, Kezhi Wang, Li Dong, Cunhua Pan, and Kun Yang. Stacked autoencoder-based deep reinforcement learning for online resource scheduling in large-scale mec networks. IEEE Internet of Things J., 7(10):9278–9290, 2020.

[8] Diederik M Roijers, Peter Vamplew, Shimon Whiteson, and Richard Dazeley. A survey of multi-objective sequential decision-making. Journal of Artificial Intelligence Research, 48:67– 113, 2013.

[9] Runzhe Yang, Xingyuan Sun, and Karthik Narasimhan. A generalized algorithm for multiobjective reinforcement learning and policy adaptation. Advances in neural information processing systems, 32, 2019.

[10] Jia Yan, Suzhi Bi, and Ying Jun Angela Zhang. Offloading and resource allocation with general task graph in mobile edge computing: A deep reinforcement learning approach. IEEE Transactions on Wireless Communications, 19(8):5404–5419, 2020.

[11] Yinong Li, Jianbo Li, Zhiqiang Lv, Haoran Li, Yue Wang, and Zhihao Xu. Gasto: A fast adaptive graph learning framework for edge computing empowered task offloading. IEEE Transactions on Network and Service Management, 2023.

[12] Zhen Gao, Lei Yang, and Yu Dai. Fast adaptive task offloading and resource allocation in large-scale mec systems via multi-agent graph reinforcement learning. IEEE Internet of Things Journal, 2023.

[13] Tao Ren, Jianwei Niu, and Yuan Qiu. Enhancing generalization of computation offloading policies in novel mobile edge computing environments by exploiting experience utility. Journal of Systems Architecture, 125:102444, 2022.

[14] Liang Huang, Suzhi Bi, and Ying-Jun Angela Zhang. Deep reinforcement learning for online computation offloading in wireless powered mobile-edge computing networks. IEEE Transactions on Mobile Computing, 19(11):2581–2593, 2019.

[15] Josh Tobin, Rachel Fong, Alex Ray, Jonas Schneider, Wojciech Zaremba, and Pieter Abbeel. Domain randomization for transferring deep neural networks from simulation to the real world. In 2017 IEEE/RSJ international conference on intelligent robots and systems (IROS), pages 23–30. IEEE, 2017.

[16] Conor F Hayes, Roxana Radulescu, Eugenio Bargiacchi, Johan K˘ allstr¨ om, Matthew Macfar-¨ lane, Mathieu Reymond, Timothy Verstraeten, Luisa M Zintgraf, Richard Dazeley, Fredrik Heintz, et al. A practical guide to multi-objective reinforcement learning and planning. Autonomous Agents and Multi-Agent Systems, 36(1):1–59, 2022.

[17] Robert Kirk, Amy Zhang, Edward Grefenstette, and Tim Rocktaschel. A survey of generalisa-¨ tion in deep reinforcement learning. arXiv preprint arXiv:2111.09794, 2021.

[18] Dibya Ghosh, Jad Rahme, Aviral Kumar, Amy Zhang, Ryan P Adams, and Sergey Levine. Why generalization in rl is difficult: Epistemic pomdps and implicit partial observability. Advances in Neural Information Processing Systems, 34:25502–25515, 2021.

[19] Dinh C Nguyen, Pubudu N Pathirana, Ming Ding, and Aruna Seneviratne. Deep reinforcement learning for collaborative offloading in heterogeneous edge networks. In 2021 IEEE/ACM 21st International Symposium on Cluster, Cloud and Internet Computing (CCGrid), pages 297–303. IEEE, 2021.

[20] Feibo Jiang, Li Dong, Kezhi Wang, Kun Yang, and Cunhua Pan. Distributed resource scheduling for large-scale mec systems: A multiagent ensemble deep reinforcement learning with imitation acceleration. IEEE Internet of Things Journal, 9(9):6597–6610, 2021.

[21] Jin Wang, Jia Hu, Geyong Min, Albert Y Zomaya, and Nektarios Georgalas. Fast adaptive task offloading in edge computing based on meta reinforcement learning. IEEE Transactions on Parallel and Distributed Systems, 32(1):242–253, 2020.

[22] Tuan Wu, Wenpeng Jing, Xiangming Wen, Zhaoming Lu, and Shuyue Zhao. A scalable computation offloading scheme for mec based on graph neural networks. In 2021 IEEE Globecom Workshops (GC Wkshps), pages 1–6. IEEE, 2021.

[23] Zheyuan Hu, Jianwei Niu, Tao Ren, and Mohsen Guizani. Achieving fast environment adaptation of drl-based computation offloading in mobile edge computing. IEEE Transactions on Mobile Computing, 2023.

[24] Ning Yang, Junrui Wen, Meng Zhang, and Ming Tang. Multi-objective deep reinforcement learning for mobile edge computing. In 2023 21st international symposium on modeling and optimization in mobile, ad hoc, and wireless networks (WiOpt), pages 1–8. IEEE, 2023.

[25] Jiaxin Chang, Jian Wang, Bing Li, Yuqi Zhao, and Duantengchuan Li. Attention-based deep reinforcement learning for edge user allocation. IEEE Transactions on Network and Service Management, 2023.

[26] Lei Lei, Huijuan Xu, Xiong Xiong, Kan Zheng, and Wei Xiang. Joint computation offloading and multiuser scheduling using approximate dynamic programming in nb-iot edge computing system. IEEE Internet of Things J., 6(3):5345–5362, 2019.

[27] K. Wang, F. Fang, Dbd Costa, and Z. Ding. Sub-channel scheduling, task assignment, and power allocation for oma-based and noma-based mec systems. IEEE Trans. Commun., PP(99):1–1, 2020.

[28] Richard S Sutton, David McAllester, Satinder Singh, and Yishay Mansour. Policy gradient methods for reinforcement learning with function approximation. Advances in neural information processing systems, 12, 1999.

[29] Petros Christodoulou. Soft actor-critic for discrete action settings. arXiv preprint arXiv:1910.07207, 2019.

[30] Simone Parisi, Matteo Pirotta, Nicola Smacchia, Luca Bascetta, and Marcello Restelli. Policy gradient approaches for multi-objective sequential decision making. In 2014 International Joint Conference on Neural Networks (IJCNN), pages 2323–2330. IEEE, 2014.

[31] Ieee standard for telecommunications and information exchange between systems - lan/man specific requirements - part 11: Wireless medium access control (mac) and physical layer (phy) specifications: High speed physical layer in the 5 ghz band. IEEE Std 802.11a-1999, pages 1–102, 1999.

[32] Lihong Li, Wei Chu, John Langford, and Robert E Schapire. A contextual-bandit approach to personalized news article recommendation. In Proceedings of the 19th international conference on World wide web, pages 661–670, 2010.

[33] Lixing Chen and Jie Xu. Task replication for vehicular cloud: Contextual combinatorial bandit with delayed feedback. In IEEE INFOCOM 2019-IEEE Conference on Computer Communications, pages 748–756. IEEE, 2019.

[34] Haihong Zhao, Xinbin Li, Song Han, Lei Yan, and Junzhi Yu. Collaboration-aware relay selection for auv in internet of underwater network: Evolving contextual bandit learning approach. IEEE Internet of Things Journal, 2022.

[35] Suzhi Bi and Ying Jun Zhang. Computation rate maximization for wireless powered mobileedge computing with binary computation offloading. IEEE Transactions on Wireless Communications, 17(6):4177–4190, 2018.

[36] Kalyanmoy Deb, Amrit Pratap, Sameer Agarwal, and TAMT Meyarivan. A fast and elitist multiobjective genetic algorithm: Nsga-ii. IEEE transactions on evolutionary computation, 6(2):182–197, 2002.

[37] Haiping Ma, Yajing Zhang, Shengyi Sun, Ting Liu, and Yu Shan. A comprehensive survey on nsga-ii for multi-objective optimization and applications. Artificial Intelligence Review, 56(12):15217–15270, 2023.

[38] Kristof Van Moffaert and Ann Nowe. Multi-objective reinforcement learning using sets of ´ pareto dominating policies. The Journal of Machine Learning Research, 15(1):3483–3512, 2014.

[39] Sriraam Natarajan and Prasad Tadepalli. Dynamic preferences in multi-criteria reinforcement learning. In Proceedings of the 22nd International Conference on Machine learning, pages 601–608, 2005.

## Appendix

## A Differences in Generalization Compared to Related Works

Many studies [2, 5, 6, 14, 19, 20] are limited to problems that optimize for a single preference. Li et al. [2] employ a Q-learning-based deep reinforcement learning (DRL) method to solve the computation offloading problem in a multi-user environment. Cui et al. [5] decomposes user association, offloading decision, computing, and communication resource allocation into two related subproblems and employs the DQN algorithm for decision-making. Lei et al. [6] proposed a DRL-based joint computation offloading and multi-user scheduling algorithm for IoT edge computing systems, aiming to minimize the long-term weighted sum of delay and power consumption under stochastic traffic arrivals. Huang et al. [14] employed an improved DQN method to address offloading decision problems and resource allocation problems. The above works focus on two objectives, delay and energy consumption, and use a weight coefficient to balance them or optimize one objective while satisfying the constraints of the other. Moreover, these studies lack research on the generalization.

Some studies [11, 13, 21–23] focus only on the generalization of system parameters. Li et al. [11] combine graph neural networks and seq2seq networks to make decisions on task offloading. They employ a meta-reinforcement learning approach to enhance the generalization of the offloading strategy in environments with different system parameters. Ren et al. [13] design a set of experience maintaining and sampling strategies to improve the training process of DRL, enhancing the model’s generalization to different environments. Wang et al. [21] design an offloading decision algorithm based on meta-reinforcement learning, which uses a seq2seq neural network to represent the offloading policy. This approach can adapt to various environments covering a wide range of topologies, task numbers, and transmission rates. Wu et al. [22] propose a method that combines graph neural networks and DRL, which can be applied to various environments with inter-dependencies among different tasks. Hu et al. [23] propose a size-adaptive offloading scheme and a setting-adaptive offloading component, designed to quickly adapt to new MEC environments of varying sizes and configurations with a few interaction steps. The above work only considers generalization in terms of system parameters, without addressing generalization in terms of the number of servers and multipreference issues.

Other works [7, 24, 25] only consider the generalization of the number of servers. A few works consider the generalization of both system parameters and the number of servers. Gao et al. [12] model the decentralized task offloading problem as a partially observable Markov decision process and use a multi-agent RL method to train the policy. They consider the generalization of both system parameters and the number of servers, but do not explore multi-preference issues. Our method provides a deeper exploration of the generalization of the offloading strategy, considering the generalization in terms of multi-preference, system parameters, and server quantities.

## B Supplementary Figures

## B.1 System Model

The MEC system model we consider is illustrated in Fig. A1. An MEC system consists of E edge servers, one remote cloud server. The system processes M tasks arriving sequentially, with each task being uploaded to only one server.

![](images/211fec4952a65fd3805fdffdd51b1d56a0b10582561ba8121b3f357eaf73a0f6.jpg)  
Figure A1: An illustrative example system model of MEC.

## B.2 Learning Approach

During the training phase, we sample $N _ { \mathrm { g } }$ contexts to create $N _ { \mathrm { g } }$ MEC environments for each epoch. The preferences of these environments are determined by Eq. (32), while their number of servers E and frequencies $f _ { \mathcal { E } }$ are randomly drawn from the context space. These environments interact with the policy to generate experiences, which are stored in the replay buffer and used to update the policy.

![](images/3c17107c804e3b923f1a598777a5d0cf05dafc8b0d8393f531a0c3b3315a185a.jpg)  
Figure A2: The generalization learning approach.

## B.3 The Overview of the GMORL

The structure of the GMORL algorithm is illustrated in Fig. A3.

![](images/08a7574e3a2c7add081c1d289f1d3b55ff974ce0624754c73748e8c92f07ff27.jpg)  
Figure A3: The overview of the GMORL algorithm.

## C Simulation Setup

We provide the context in Table A1. We set testing preference set $\Omega _ { N _ { \mathrm { g } } }$ according to Eq. (32) and fit Pareto front in $N _ { \mathrm { g } }$ preferences. Each preference’s performance contains total delay and energy consumption for all tasks in one episode. We evaluate a performance (delay or energy consumption) with an average of 1000 episodes. A disk coverage has a radius of 1000m to 2000m for a cloud server and 50m to 500m for an edge server. Each episode needs to initial different radiuses for the cloud and edge servers. We set the mean of task size L<sup>¯</sup> according to Eq. (1).

## C.1 Evaluation Metrics

We consider the following metrics to evaluate the performances of the proposed algorithms.

Table A1: Context Space for Training and Testing

<table><tr><td>Context space</td><td>Training</td><td>Testing</td></tr><tr><td>The number of preference  $N_g$ </td><td>64</td><td>101</td></tr><tr><td>Edge server quantity  $\mathcal{C}_E$ </td><td> $\{1, 2, \dots, 8\}$ </td><td> $\{1, 2, \dots, 10\}$ </td></tr><tr><td>Cloud server CPU frequency  $\mathcal{C}_{f_0}$ </td><td>[3.5, 4.5] GHz</td><td>[3.0, 5.0] GHz</td></tr><tr><td>Edge server CPU frequency  $\mathcal{C}_{f_{\varepsilon'}}$ </td><td>[1.75, 2.25] GHz</td><td>[1.5, 2.5] GHz</td></tr></table>

• Energy Consumption: The total energy consumption of one episode given as $\sum _ { m = 1 } ^ { M } E _ { m } ^ { \mathrm { o f f } } +$ $E _ { m } ^ { \mathrm { e x e } }$ , and the average energy consumption per Mbits task of one episode given by $\sum _ { m = 1 } ^ { M } \frac { E _ { m } ^ { \mathrm { o f f } } + E _ { m } ^ { \mathrm { e x e } } } { \bar { L } }$

• Task Delay: The total energy consumption of one episode given as $\sum _ { m = 1 } ^ { M } E _ { m } ^ { \mathrm { o f f } } + E _ { m } ^ { \mathrm { e x e } }$ , and the average energy consumption per Mbits task of one episode given by $\sum _ { m = 1 } ^ { M } \frac { E _ { m } ^ { \mathrm { o f f } } + E _ { m } ^ { \mathrm { e x e } } } { \bar { L } }$

• Pareto Front:

$P F ( \Pi ) = \{ \pi \in \Pi \mid \nexists \pi ^ { \prime } \in \Pi : y ^ { \pi ^ { \prime } } \succ _ { P } y ^ { \pi } \}$ , where the symbols are defined by Eq. (12).

• Hypervolume Metric:

$\begin{array} { r } { \mathcal { V } ( P F ( \Pi ) ) = \int _ { \mathbb { R } ^ { 2 } } \mathbb { I } _ { V _ { h } ( P F ( \Pi ) ) } ( z ) d z } \end{array}$ , where the symbols are defined by Eq. (14).

## C.2 Baselines

LinUCB-based scheme: The Offloading scheme is based on a kind of contextual MAB algorithm [32]. It is an improvement over the traditional UCB algorithm. This scheme uses states as MAB contexts and learns a policy by exploring different actions. We apply the multi-arm bandit algorithm. We regard each action as an arm and construct the feature of an arm from preference ω and server information vector $\mathbf { \Delta } _ { s _ { t , e } }$ . Then, we update the parameter matrix based on the context and exploration results to learn a strategy that maximizes rewards. We train this scheme in preference set $\Omega _ { 1 0 1 }$ and evaluate it for any preference in one. This method is computationally simple and incorporates context information, making it widely used in task offloading.

SA-based scheme: The heuristic method searches for an optimal local solution for task offloading without contexts. We use this method to observe the performance of heuristic approaches. This method generates a fixed offloading scheme for each preference and then iteratively searches for better solutions through local search. Once a better solution is found, it is accepted or rejected with a certain probability. This scheme searches 10000 episodes for each preference. However, searching for a solution that only applies to a specific context is time-consuming.

Random-based scheme: The random-based scheme has p probability to offload a task to the cloud server and $1 - p$ probability to a random edge server. We tune the probability p and evaluate the scheme to obtain a Pareto front.

Multi-policy scheme: The multi-policy MORL approach [24] is based on the standard Discrete-SAC algorithm. We build 101 Discrete- $. s \ r _ { \mathrm { A C } }$ policy models for the 101 preference in $\Omega _ { 1 0 1 }$ correspondingly. We train each policy model with $f _ { 0 } = 4 \ : \mathrm { G H z }$ and $f _ { e ^ { \prime } } = 2 \mathrm { G H z } .$ . This method has no generalization ability. A well-trained policy model is applicable to a specific context. However, benefiting from focusing on a specific context, this method is more likely to achieve optimal performance. We apply the method to determine the upper bound of the Pareto front.

## C.3 Convergence Performances

We verify the convergence of the proposed GMORL algorithm. In Fig. A4a, we evaluate and plot the training reward of our algorithm. The reward shown in this figure is scalarized using Eq. (29). We observe that with the training episode increasing, the total reward converges. In fig. A4b and fig.

A4c, as the training episodes increase, the delay and energy consumption decrease and converge to a stable value. This indicates that the GMORL algorithm converges effectively and reach a Pareto local optimum. In the following subsection, we will specifically analyze other performances in various system settings.

![](images/bc69891eae36e17d26167c5b276566d68842efc3ca03ad4c3118652fd6eb5b1a.jpg)  
(a)

![](images/7ce13a8cd8641bf574561b4325e6979f4a8d1375b758a6d345e0778c751df9fc.jpg)  
(b)

![](images/6980c70cfe4a915b03477990f1313af9736629a27c665e3dde76ea02eed9c316.jpg)  
(c)

![](images/9ffe8d0dc54619250cd90f3001c199773dc91213c0b5f43c5232cbf3f19a8a74.jpg)  
(d)  
Figure A4: Convergence performance of the proposed GMORL algorithm: (a) Reward during training; (b) Total delay during training when $E = 5 ,$ $f _ { 0 } = 4$ GHz, $f _ { e ^ { \prime } } = 2$ GHz for all $e ^ { \prime } \in \bar { \mathcal { E } } ^ { \prime }$ , and $\omega = ( 1 , 0 )$ ; (c) Total energy consumption during training when $E = 5$ , CPU frequency $f _ { 0 } = 4$ GHz, $f _ { e ^ { \prime } } = 2 \operatorname { G H z }$ for all $e ^ { \prime } \in \mathcal { E } ^ { \prime }$ , and preference $\omega = ( 0 , 1 )$ ; (d) Total energy consumption during training when $E = 5 , f _ { 0 } = 4$ GHz, $f _ { e ^ { \prime } } = 2 \ : \mathrm { G H z }$ for all $e ^ { \prime } \in \mathcal { E } ^ { \prime }$ , and performance $\omega = ( 0 . 3 , 0 . 7 )$

## C.4 GMORL under Diverse Queue Strategies

We conducted supplementary experiments incorporating preemptive scheduling and earliest deadline first (EDF) queue policies for comparison in Fig. A5. It can be seen from the experimental result graph that when GMORL is combined with FIFO, Preemptive, and EDF queue strategies respectively, the energy consumption shows a downward trend and gradually converges to a stable level as the number of training rounds increases. Although there are differences in energy consumption, the overall trend is consistent, indicating that GMORL has strong adaptability to different queue strategies when dealing with tasks with heterogeneous priorities. This verifies its robustness and generalization ability in scenarios with diverse queue strategies, indicating that the framework can flexibly adapt to the requirements of dynamic changes in task priorities in practical applications.

## D Proof of Theorems

## D.1 Proof of Theorem 1

Proof. To prove the convergence of the GMORL algorithm, we analyze the algorithm with the scalarized reward structure. The Bellman operator T of the action-value function with the scalarized reward is:

$$
\mathcal {T} ^ {\pi} Q (\boldsymbol {s} _ {t}, a _ {t}) = r _ {\omega} (\boldsymbol {s} _ {t}, a _ {t}) + \gamma \mathbb {E} _ {\boldsymbol {s} _ {t + 1} \sim \rho_ {\pi}} (V (\boldsymbol {s} _ {t + 1})),\tag{A1}
$$

where $\boldsymbol { r } _ { \omega } \big ( \boldsymbol { s } _ { t } , \boldsymbol { a } _ { t } \big ) = \omega ^ { T } \times \big ( \alpha _ { \mathrm { T } } r _ { \mathrm { T } } \big ( \boldsymbol { s } _ { t } , \boldsymbol { a } _ { t } \big ) , \alpha _ { \mathrm { E } } r _ { \mathrm { E } } \big ( \boldsymbol { s } _ { t } , \boldsymbol { a } _ { t } \big ) \big )$ is a scalarized reward function.

![](images/5eb679ac5fdcb2b34fd61f92945d1d414609ecb3cc9b39829c9bfa1a8b962d02.jpg)  
Figure A5: Comparisons of GMORL with FIFO, preemptive scheduling and EDF queue policies

For any two policies π and $\pi ^ { \prime }$ , the difference of the Bellman operators is:

$$
\begin{array}{r l} & {\| \mathcal {T} ^ {\pi} Q - \mathcal {T} ^ {\pi^ {\prime}} Q ^ {\prime} \| = \underset {\boldsymbol {s}} {\max} \left| \mathcal {T} ^ {\pi} Q (\boldsymbol {s}, a) - \mathcal {T} ^ {\pi^ {\prime}} Q ^ {\prime} (\boldsymbol {s}, a) \right|} \\ & {\qquad = \underset {\boldsymbol {s}} {\max} \left| r _ {\omega} (\boldsymbol {s}, a) + \gamma \mathbb {E} _ {\boldsymbol {s} _ {t + 1} \sim \rho_ {\pi}} (V (\boldsymbol {s} _ {t + 1})) \right.} \\ & {\qquad \left. - \left(r _ {\omega} (\boldsymbol {s}, a) + \gamma \mathbb {E} _ {\boldsymbol {s} _ {t + 1} \sim \rho_ {\pi^ {\prime}}} (V ^ {\prime} (\boldsymbol {s} _ {t + 1}))\right) \right|} \\ & {\qquad = \underset {\boldsymbol {s}} {\max} \left| \gamma \mathbb {E} _ {\boldsymbol {s} _ {t + 1} \sim \rho_ {\pi}} (V (\boldsymbol {s} _ {t + 1}) - V ^ {\prime} (\boldsymbol {s} _ {t + 1})) \right|} \\ & {\qquad \leq \gamma \underset {\boldsymbol {s}} {\max} | V (\boldsymbol {s} _ {t + 1}) - V ^ {\prime} (\boldsymbol {s} _ {t + 1}) |} \\ & {\qquad \leq \gamma \| Q - Q ^ {\prime} \|,} \end{array}\tag{A2}
$$

Since $\tau$ remains a contraction mapping even with the scalarized reward (as ω and α coefficients are fixed and do not affect the contraction property), the Banach fixed-point theorem guarantees the existence of a unique fixed point $Q ^ { * }$ such that:

$$
Q ^ {*} = \mathcal {T} Q ^ {*}.\tag{A3}
$$

Thus, we have:

$$
\lim _ {k \to \infty} Q _ {k} = Q ^ {*},\tag{A4}
$$

where $Q _ { k + 1 } = T Q _ { k }$

Next, we analyze the convergence of the policy network and the target networks. As the Q-functions converge towards $Q ^ { * }$ , the policy network updates drive the policy $\pi _ { \phi }$ towards the optimal policy $\pi ^ { * }$ that maximizes these Q-values. The target networks use the soft update rule: $\bar { \pmb { \theta } } _ { i }  \beta \pmb { \theta } _ { i } + ( 1 - \beta ) \bar { \pmb { \theta } } _ { i }$ where $\beta \in ( 0 , 1 )$ to reduce the risk of divergence caused by changing Q-value estimates. Therefore, we prove the convergence properties of GMORL.

## D.2 Proof of Corollary 1

Proof. The computational complexity of this algorithm can be assessed using several parameters. During environment sampling, relevant context and features are generated for each environment on all edge servers, requiring $O ( N _ { \mathrm { g } } E )$ operations per round. In each sampled environment, the number of operations required for the interaction processes is $O ( T )$ . Thus, for all environments in each round, these operations require $O ( N _ { \mathrm { g } } T )$ operations. For the neural network update section, as it involves operations such as replay of experiences and parameter modifications for Q functions and policy networks, the number of operations in each training round is $O ( N _ { \mathrm { { u p } } } N _ { \mathrm { { n e t } } } )$ . Therefore, in the $\bar { N } _ { \mathrm { e p } }$ training session, the computational complexity of this algorithm is $\dot { O } ( N _ { \mathrm { e p } } ( N _ { \mathrm { g } } ( E + T )$ + $N _ { \mathrm { u p } } N _ { \mathrm { n e t } } ^ { \bullet } ) \rangle$ .

## D.2 Proof of Theorem 2

Proof. Since we aim to minimize the objective function Eq.10, and let $\begin{array} { r l } { J ( \pi ) } & { { } = } \end{array}$ min<sub>π</sub> $\begin{array} { r } { \mathbb { E } \mathbf { x } \sim \pi \left[ \sum _ { m \in \mathcal { M } } \gamma ^ { m } \left( \omega _ { \mathrm { T } } T _ { m } + \omega _ { \mathrm { E } } E _ { m } \right) \right] } \end{array}$ , we hope $J ( \pi _ { t } ) ~ > ~ J ( \pi _ { t + 1 } )$ . For any two adjacent policies $\pi _ { t }$ and $\pi _ { t + 1 }$ , we derive a lower bound for their performance difference $\Delta J ^ { ' } =$ $J ( \pi _ { t } ) - J ( \pi _ { t + 1 } )$ as follows:

We first compute the performance difference for two adjacent policies:

$$
\begin{array}{r l} & {\Delta J = \left[ \sum_ {m \in \mathcal {M}} \gamma^ {m} (\omega_ {T} T _ {m} (\pi_ {t}) + \omega_ {E} E _ {m} (\pi_ {t})) \right]} \\ & {\qquad - \left[ \sum_ {m \in \mathcal {M}} \gamma^ {m} (\omega_ {T} T _ {m} (\pi_ {t + 1}) + \omega_ {E} E _ {m} (\pi_ {t + 1})) \right]} \\ & {\qquad = \sum_ {m \in \mathcal {M}} \gamma^ {m} [ \omega_ {T} (T _ {m} (\pi_ {t}) - T _ {m} (\pi_ {t + 1}))} \\ & {\qquad + \omega_ {E} (E _ {m} (\pi_ {t}) - E _ {m} (\pi_ {t + 1})) ]} \end{array}\tag{A5}
$$

The difference in energy consumption between the two policies is:

$$
\begin{array}{r l r} & & E _ {m} (\pi_ {t}) - E _ {m} (\pi_ {t + 1}) \geq p ^ {\mathrm{off}} \sum_ {e \in \mathcal {E}} [ x _ {m, e} (\pi_ {t}) - x _ {m, e} (\pi_ {t + 1}) ] \frac {L _ {m}}{C _ {u , e}} \\ & & + \sum_ {e \in \mathcal {E}} [ x _ {m, e} (\pi_ {t}) - x _ {m, e} (\pi_ {t + 1}) ] \kappa \eta f _ {e} ^ {2} L _ {m} \end{array}\tag{A6}
$$

The difference in time consumption between the two policies is:

$$
T _ {m} (\pi_ {t}) - T _ {m} (\pi_ {t + 1}) \geq \hat {T} _ {m} ^ {\mathrm{off}} (\pi_ {t}) - \hat {T} _ {m} ^ {\mathrm{off}} (\pi_ {t + 1})\tag{A7}
$$

Therefore, the lower bound for the performance difference between adjacent policies is:

$$
\begin{array}{r l} & {\Delta J \geq \sum_ {m \in \mathcal {M}} \gamma^ {m} \{\omega_ {E} \sum_ {e \in \mathcal {E}} [ x _ {m, e} (\pi_ {t}) - x _ {m, e} (\pi_ {t + 1}) ] (p ^ {\mathrm{off}} \frac {L _ {m}}{C _ {u , e}}} \\ & {\quad + \kappa \eta f _ {e} ^ {2} L _ {m}) + \omega_ {T} [ \hat {T} _ {m} ^ {\mathrm{off}} (\pi_ {t}) - \hat {T} _ {m} ^ {\mathrm{off}} (\pi_ {t + 1}) ] \}} \end{array}\tag{A8}
$$

Let $\begin{array} { r } { \Phi _ { m , e } = p ^ { \mathrm { o f f } } \frac { L _ { m } } { C _ { u , e } } + \kappa \eta f _ { e } ^ { 2 } L _ { m } } \end{array}$ and $\begin{array} { r } { \Phi _ { m i n } = \operatorname* { m i n } _ { m , e } \{ \gamma ^ { m } \omega _ { E } \Phi _ { m , e } \} } \end{array}$

Then:

$$
\Delta J \geq A \| \pi_ {t} - \pi_ {t + 1} \| _ {1}\tag{A9}
$$

where $A = \mathrm { m i n } \{ \Phi _ { m i n } , \mathrm { m i n } _ { m } \{ \gamma ^ { m } \omega _ { T } \} \}$ } and $\lVert \pi _ { t } - \pi _ { t + 1 } \rVert _ { 1 }$ represents the L1-norm difference between the two policies.