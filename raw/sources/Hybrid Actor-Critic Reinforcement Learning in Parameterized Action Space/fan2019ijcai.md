# Hybrid actor-critic reinforcement learning in parameterized action space

Local text extraction from fan2019ijcai.pdf; page numbers refer to the PDF.

## PDF page 1

Hybrid Actor-Critic Reinforcement Learning in Parameterized Action Space
Zhou Fan∗, Rui Su∗, Weinan Zhang† and Yong Yu
Shanghai Jiao Tong University
zhou.fan@sjtu.edu.cn, {surui, wnzhang, yyu}@apex.sjtu.edu.cn
Abstract
In this paper we propose a hybrid architecture
of actor-critic algorithms for reinforcement learn-
ing in parameterized action space, which consists
of multiple parallel sub-actor networks to decom-
pose the structured action space into simpler ac-
tion spaces along with a critic network to guide
the training of all sub-actor networks. While this
paper is mainly focused on parameterized action
space, the proposed architecture, which we call hy-
brid actor-critic, can be extended for more general
action spaces which has a hierarchical structure.
We present an instance of the hybrid actor-critic
architecture based on proximal policy optimization
(PPO), which we refer to as hybrid proximal pol-
icy optimization (H-PPO). Our experiments test H-
PPO on a collection of tasks with parameterized
action space, where H-PPO demonstrates superior
performance over previous methods of parameter-
ized action reinforcement learning.
1
Introduction
Reinforcement learning (RL) has achieved impressive per-
formance on a wide range of tasks including game playing,
robotics and natural language processing. Most of recent ex-
citing achievements is obtained by the combination of deep
learning and reinforcement learning, known as deep rein-
forcement learning [Mnih et al., 2013]. In game playing do-
mains, deep Q-network (DQN) [Mnih et al., 2013] is capable
of learning control policies directly from high-dimensional
sensory input in Atari games, and AlphaGo [Silver et al.,
2016] has defeated world champions in the game of Go and
could achieve superhuman performance even without human
knowledge for training [Silver et al., 2017]. Robotics is also
a signiﬁcant aspect of applications of RL, where RL enables a
robot to autonomously learn a sophisticated behavior through
interactions with its environment [Kober et al., 2013].
In the general setup of RL, an agent interacts with an envi-
ronment in the following way: at each time step t, it observes
(either fully or partially) a state st and takes an action at, then
∗Equal contribution.
†Corresponding author.
3
2
1
4
……
……
…
Discrete Action Selection
Continuous Parameter Selection
Continuous Set
Continuous Set
Continuous Set
Figure 1: Illustration of a parameterized action space.
receives a reward signal rt as well as the next state st+1. Here
the action at is selected by the agent from its action space A.
The type of the action space is an important characteristic
of the setup of an RL problem, and problems with different
types of action space are usually solved with different algo-
rithms. A typical RL setup may come with a discrete action
space or a continuous one, and most RL algorithms are de-
signed for either one of these two types. The agent simply
selects its actions from a ﬁnite set of discrete actions if the
action space is discrete, or from a single continuous space in
the case of a continuous action space. However, action space
could also have some hierarchical structure instead of being
a ﬂat set. The most common class of structured action space
is known as parameterized action spaces, where a parameter-
ized action is a discrete action parameterized by a continuous
real-valued vector [Masson et al., 2016]. With a parameter-
ized action space, the agent not only selects an action from a
discrete set, but selects the parameter to use with that action
from the continuous parameter set of that action as well.
Figure 1 shows an example of parameterized action space.
The hierarchically structured action space contains four types
of discrete actions shown in blue, and every discrete action
has a continuous parameter space marked with rounded rect-
angles in grey. In this example, the discrete action with index
2 is actually not parameterized. It can also be viewed as a
special case that the parameter space of discrete action 2 only
has one element. Parameterized action space perfectly mod-
els the scenarios where there are different categories of con-
tinuous actions. Many games as well as real world tasks have
a parameterized action space. For example, in the Half Field
Offense (HFO) [Hausknecht et al., 2016] domain, which is a
subtask based on the RoboCup 2D simulation platform, the
agent may choose the discrete action Kick and specify its
real-valued parameters (power and direction). Moreover, pa-
Proceedings of the Twenty-Eighth International Joint Conference on Artiﬁcial Intelligence (IJCAI-19)
2279


## PDF page 2

more layers of branching nodes
Layer-1 Action Selection
Layer-2 Action Selection
Layer-3 Action Selection
Figure 2: A hierarchically structured action space.
rameterized actions naturally exist in the context of robotics,
where the action space can be constructed in a way that a set
of meta-actions deﬁnes the higher-level selection of actions
and every meta-action is controlled with ﬁne-grained param-
eters [Kober et al., 2013].
In addition to parameterized action spaces, action spaces
may have more general hierarchical structures. For exam-
ple, the parameters for the different actions are discretized in
some game environments such as StarCraft II Learning Envi-
ronment [Vinyals et al., 2017]. Also, the action space may be
manually constructed to have a hierarchical structure of more
than two layers, which is a technique often used to reduce the
size of an extremely large action space, with OpenAI Five1
on Dota 2 as a remarkable example. While it is intractable to
choose an action directly from a set that contains millions of
discrete actions, we can tackle this problem by constructing a
hierarchically structured action space with a hierarchical tax-
onomy. As is shown in Figure 2, the action space has a tree
structure of multi-layer classiﬁcations of actions, in a way
that each action selection node only has a small number of
branches. Note that this tree structure could have more than
two layers, and the external nodes of the tree structure could
be continuous action-selection instead of discrete branching.
In this view, the parameterized action space is a special case
of hierarchical action space which has a discrete layer and
then a continuous layer.
In this work, we propose a hybrid architecture of actor-
critic algorithms for RL in parameterized action space.
It is based on original architecture of actor-critic algo-
rithms [Konda and Tsitsiklis, 2000], but contains multiple
parallel sub-actor networks instead of one to solve multi-
layer action selection respectively and has one global critic
network to update the policy parameters of all sub-actor net-
works. Moreover, the hybrid actor-critic architecture we pro-
pose is ﬂexible to the structure of the action space, such that
it can also be generalized for other hierarchically structured
action spaces. Speciﬁcally, we present an instance of the hy-
brid actor-critic architecture based on the proximal policy op-
timization (PPO) [Schulman et al., 2017], which we call hy-
brid proximal policy optimization (H-PPO). We show that H-
PPO outperforms previous methods on a collection of tasks
with parameterized action space.
The rest of this paper is organized as follows: Section 2
introduces related work in the parameterized action space do-
main. The detailed architecture of hybrid actor-critic algo-
rithms and H-PPO is presented in Section 3. Section 4 shows
1https://blog.openai.com/openai-ﬁve/
experiments and results. Finally, conclusion and future work
are presented in Section 5.
2
Related Work
Parameterized action spaces and other hierarchical action
spaces are more difﬁcult to deal with in RL compared to
purely discrete or continuous action spaces for the following
reasons. First, the action space has a hierarchical structure,
which makes selecting an action more complicated than just
choosing one element from a ﬂat set of actions. Second, a
parameterized action space involves both discrete action se-
lection and continuous parameter selection, while most RL
models are designed for only discrete action spaces or con-
tinuous action spaces.
2.1
RL Methods for Discrete Action Space and
Continuous Action Space
The Q-learning algorithm [Watkins and Dayan, 1992] is a
value-based method which updates the Q-function using the
Bellman equation
Q(s, a) =
E
rt,st+1[rt + γ max
a′∈A Q(st+1, a′) | st = s, at = a]. (1)
In the domain of discrete action space, deep Q-network
(DQN) [Mnih et al., 2013] takes the framework and uses a
deep neural network to approximate the Q function. Some
variations of DQN are also widely used in discrete action
space, including asynchronous DQN [Mnih et al., 2016], dou-
ble DQN [Hasselt et al., 2016] and dueling DQN [Wang et al.,
2016].
Policy gradient [Sutton et al., 2000] is another class of RL
algorithms which optimizes a stochastic policy πθ parameter-
ized by θ to maximize the expected policy value J(πθ). The
gradient of the stochastic policy is given by the policy gradi-
ent theorem [Sutton et al., 2000] as
∇θJ(πθ) = E
s,a[∇θ log πθ(a | s)Qπθ(s, a)].
(2)
As an alternative, the policy gradient could also be computed
with the advantage function Aπθ(s, a) as
∇θJ(πθ) = E
s,a[∇θ log πθ(a | s)Aπθ(s, a)].
(3)
Similarly in continuous action spaces, the deterministic
policy gradient (DPG) algorithm [Silver et al., 2014] and the
DDPG algorithm [Lillicrap et al., 2016] optimize a determin-
istic policy µθ parameterized by θ based on the deterministic
policy gradient theorem [Silver et al., 2014] as
∇θJ(µθ) = E
s[∇θµθ(s)∇θQµθ(s, a) |a=µθ(s)].
(4)
Based on the policy gradient methods, trust region policy
optimization (TRPO) [Schulman et al., 2015] and proximal
policy optimization (PPO) [Schulman et al., 2017] improve
the optimization techniques to achieve better performance.
2.2
RL Methods for Parameterized Action Space
To deal with the fact that a parameterized action space con-
tains both discrete actions and continuous parameters, one
Proceedings of the Twenty-Eighth International Joint Conference on Artiﬁcial Intelligence (IJCAI-19)
2280


## PDF page 3

straightforward approach is to directly discretize the contin-
uous part of the action space and turn it into a large discrete
set (for example with the tile coding approach [Sherstov and
Stone, 2005]). This trivial method loses the advantages of
continuous action space for ﬁne-grained control, and often
ends up with an extremely large discrete action space.
Another direction is to convert the discrete action selection
into a continuous space. Hausknecht and Stone [2016] used
an actor network to output a value for each of the discrete ac-
tions, concatenated with all continuous parameters, and the
discrete action is chosen to be the one with the maximum
output value. The actor network is learned using the DDPG
algorithm. By relaxing the structured action space into a con-
tinuous set, this method might signiﬁcantly increase the com-
plexity of the action space [Xiong et al., 2018].
Masson et al. [2016] focused on how to learn an action-
selection policy given ﬁxed parameter-selection, and pro-
posed the framework called Q-PAMDP, which alternately
learns the discrete action selection with Q-learning and up-
dates parameter-selection policies with policy search meth-
ods.
Wei et al. [2018] proposed a hierarchical approach for RL
in parameterized action space where the parameter policy is
conditioned on the discrete action policy and used TRPO and
Stochastic Value Gradient [Heess et al., 2015] to train such
an architecture. Although they also found that this method
could be unstable due to the joint-learning between the dis-
crete action policy and parameter policy.
Xiong et al. [2018] proposed the parameterized deep Q-
networks (P-DQN) algorithm, which can be viewed as a com-
bination of DQN and DDPG. P-DQN has one network to se-
lect the continuous parameters for all discrete action. Another
network takes the state and the chosen continuous parameters
as input and outputs the Q-values for all discrete actions. The
discrete action with the largest Q-value is chosen. However,
the network that selects continuous parameters are updated
to maximize the sum of the Q-values for all discrete actions,
which might cause the algorithm being updated to improve
the sum of the Q-values but decrease the largest Q-value.
3
Methodologies
This section introduces the proposed hybrid actor-critic ar-
chitecture and presents the H-PPO algorithm as an instance
of this architecture. Following the notations in [Masson et
al., 2016], we describe the parameterized action space in a
mathematical way. We consider the following parameterized
action space: the discrete actions are selected from a ﬁnite set
Ad = {a1, a2, . . . , ak}, and each a ∈Ad has a set of real-
valued continuous parameters Xa ⊆Rma. In this way, a com-
plete action is represented as a tuple (a, x), where a ∈Ad is
the chosen discrete action and x ∈Xa is the chosen parame-
ter to execute with action a. The whole action space A is then
the union of each discrete action with all possible parameters
for that action:
A =
[
a∈Ad
{(a, x) | x ∈Xa}.
(5)
A Markov decision process with a parameterized action space
is referred to as parameterized-action Markov decision pro-
State Encoding Network
Continuous Actor Network
Discrete Actor Network
discrete action
parameters for each action
state input
Critic Network: State-Value Function
Figure 3: Hybrid actor-critic architecture for parameterized action
space.
cesses (PAMDPs) [Masson et al., 2016].
To design an algorithm for PAMDPs, we should ﬁrst tackle
the problem that parameterized action spaces are a class of
discrete-continuous hybrid action spaces.
Our method is
based on the actor-critic architecture for the reason that many
algorithms with actor-critic style, including policy gradient
methods and PPO, are capable of learning stochastic poli-
cies in both discrete action spaces and continuous action
spaces. Actor-critic algorithms usually have one actor net-
work and one critic network, and the critic network is used
to compute the gradient of the parameters of the actor net-
work. By contrast, our proposed architecture for parameter-
ized action space (shown in Figure 3) contains two parallel
actor networks (or even more for general hierarchical action
spaces, introduced later in subsection 3.2). The parallel ac-
tors perform action-selection and parameter-selection sepa-
rately: one discrete actor network learns a stochastic policy
πθd to select the discrete action a and one continuous actor
network learns a stochastic policy πθc to choose the continu-
ous parameters xa1, xa2, . . . , xak for all discrete actions. The
complete action to execute is the selected action a paired with
the chosen parameter xa corresponding to action a. The two
actor networks shares the ﬁrst few layers to encode the state
information. We refer to the proposed architecture as hybrid
actor-critic architecture since discrete actor and continuous
actor both exist in this architecture.
There is a single critic network in the hybrid actor-critic
architecture, which works as an estimator of the state-value
function V (s).
One important reason for us to use the
state-value function as the critic instead of the action-value
function is that action-value function suffers from the over-
parameterization problem in parameterized action space.
Speciﬁcally, if the action-value function is used as the critic,
the critic network in implementation would take the state s,
the selected discrete action a and the chosen parameters for
all discrete actions xa1, xa2, . . . , xak as input. It is impos-
sible to just feed the chosen parameter xa for one speciﬁc
discrete action a into the critic network since the parameter
dimensions of different discrete actions could be different. In
this way, the action-value function is represented in the form
of Q(s, a, xa1, xa2, . . . , xak). However, the actual action to
execute is not inﬂuenced by irrelevant parameters, so the true
Q-function value is independent of xa′ for all a′ ̸= a. There-
fore, the action-value function would suffer from the problem
Proceedings of the Twenty-Eighth International Joint Conference on Artiﬁcial Intelligence (IJCAI-19)
2281


## PDF page 4

of over-parameterization that
Q(s, a, xa1, xa2, . . . , xak) = Q(s, a, xa).
(6)
By contrast, the state-value function only takes the state s as
input and does not have this problem. In our architecture, the
state-value function V (s) is used for computing a variance-
reduced advantage function estimator ˆA. We follow the im-
plementation used by Mnih et al. [2016], which runs the pol-
icy for T timesteps and computes the estimator ˆAt using the
collected samples as
ˆAt = −V (st) + rt + γrt+1 + · · · + γT −t−1rT −1 + γT −tV (sT ), (7)
where t ∈[0, T] is the timestep index and T is much less than
the length of an episode.
With a critic network providing estimation of the advantage
function, the hybrid actor-critic architecture is ﬂexible in the
choice of the policy optimization method. The only require-
ment is that the optimization method should have an actor-
critic style and updates stochastic policies with the advantage
function provided by the critic. Although the complete action
to execute (a, xa) is decided by both of the actors, the discrete
actor and the continuous actor are updated separately by their
respective update rules at each timestep. The update rules of
the two actor networks could follow policy gradient methods
as Eq. (3) or other optimization methods for stochastic poli-
cies such as PPO. We can even use two different optimization
methods for the discrete policy πθd and the continuous policy
πθc.
Then we present the hybrid proximal policy optimization
algorithm for parameterized action space, which is a speciﬁc
instance of the hybrid actor-critic architecture based on PPO.
3.1
Hybrid Proximal Policy Optimization
The hybrid proximal policy optimization (H-PPO) takes the
hybrid actor-critic architecture in Figure 3 and uses PPO as
the policy optimization method for both its discrete policy
πθd and its continuous policy πθc.
PPO is a state-of-the-art policy optimization method that
learns a stochastic policy πθ by minimizing a clipped surro-
gate objective [Schulman et al., 2017] as
LCLIP(θ) = ˆEt[min(rt(θ) ˆAt, clip(rt(θ), 1 −ϵ, 1 + ϵ) ˆAt)], (8)
where rt(θ) denotes the probability ratio rt(θ) =
πθ(at|st)
πθold(at|st)
and ϵ is a hyperparameter.
To generate the stochastic policy for discrete actions
πθd, the discrete actor network of H-PPO outputs k values
fa1, fa2, . . . , fak for the k discrete actions, and the discrete
action a to take is randomly sampled from the softmax(f)
distribution. The continuous actor network of H-PPO gener-
ates the stochastic policy πθc for continuous parameters by
outputting the mean and variance of a Gaussian distribution
for each of the parameters. On every iteration of training,
H-PPO runs by its policies πθd and πθc in the environment
for T timesteps and updates these two policies with the col-
lected samples. The discrete policy πθd and the continuous
policy πθc are updated separately by minimizing their respec-
tive clipped surrogate objective. The objective for the discrete
policy πθd is given by
LCLIP
d
(θd) = ˆEt[min(rd
t (θd) ˆAt, clip(rd
t (θd), 1 −ϵ, 1 + ϵ) ˆAt)], (9)
Critic Network: State-Value Function
State Encoding Network
Actor
……
state input
Actor
Actor
Actor
……
Actor
Actor
Discrete Actor Networks
Continuous Actor Networks
Figure 4: Hybrid actor-critic architecture for general hierarchically
structured action space.
and similarly the objective for the continuous policy πθc is
LCLIP
c
(θc) = ˆEt[min(rc
t(θc) ˆAt, clip(rc
t(θc), 1 −ϵ, 1 + ϵ) ˆAt)]. (10)
Here the probability ratio rd
t (θd) only considers the discrete
policy and rc
t(θc) only considers the continuous policy. That
is to say, even though the two policies work with each other
to decide the complete action, their objectives are not explic-
itly conditioned on each other. In other words, πθd and πθc
are viewed as two separate distributions instead of a joint dis-
tribution in policy optimization. For example, if the com-
plete action executed at timestep t (t ∈[0, T]) is denoted by
at = (a, xa), rd
t (θd) is deﬁned as
πθd(a|st)
πθd(old)(a|st) and rc
t(θc) is
deﬁned as
πθc(xa|st)
πθc(old)(xa|st).
3.2
Hybrid Actor-Critic Architecture for General
Hierarchical Action Space
Apart from parameterized action space, the hybrid actor-critic
architecture can be extended to solve RL problems with gen-
eral hierarchical action space. Shown in Figure 2, the action-
selection process in a general hierarchical action space could
be represented with a tree structure. Each of the grey areas
in Figure 2 stands for an action-selection sub-problem. All
internal nodes of the tree structure should be discrete action-
selection sub-problems, and each discrete action on an inter-
nal node corresponds to an action-selection sub-problem of
the next layer. The leaf nodes of the tree could be either dis-
crete action-selection or continuous action-selection.
The hybrid actor-critic architecture for general hierarchical
action space contains (see Figure 4) multiple parallel actor
networks and one critic network. There is one actor network
for each of the action-selection sub-problems, either discrete
or continuous. The critic network here is the same as the
critic in the hybrid actor-critic architecture for parameterized
action space. The actor networks share the ﬁrst few layers to
encode the state and each of them generates either a stochas-
tic discrete policy or a stochastic continuous policy. During
training, the actors are updated as separate policies using a
chosen policy optimization method such as PPO.
4
Experiments
4.1
Environments
We create a collection of tasks with parameterized action
space for the experiments, which is shown in Figure 5. The
Proceedings of the Twenty-Eighth International Joint Conference on Artiﬁcial Intelligence (IJCAI-19)
2282


## PDF page 5

(a) Catching Point
(b) Moving
(c) Chase and Attack
(d) Half Field Football
Figure 5: The four environments with parameterized action space
used as the environments of the experiments. For clearness, the il-
lustrations here show only a part of the whole ﬁeld for the tasks
except Football.
tasks are brieﬂy described below, and a more detailed descrip-
tion of the environment settings can be found in the supple-
mental material2. Every task has a so-called ”winning state”,
which is a ﬁnal state of an episode indicating that the agent
has succeeded in that episode.
Catching point.
In this task, the agent should catch a tar-
get point within limited chances. The parameterized actions
are MOVE(directionM) and CATCH, where MOVE means a
movement of a constant distance in the speciﬁed direction and
CATCH is an attempt to catch the target point. The agent
could only try the CATCH action for up to 10 times. The
episode ends if the agent catches up the target point (the win-
ning state), all of its 10 chances ran out or the time limit ex-
ceeds.
Moving.
In this scenario, the goal of the agent is to move
towards a target area and stop in it. The agent can choose
its action among ACCEL(powerA), TURN(directionT) and
BRAKE. The movement of the agent is always in the direc-
tion of its current direction. An episode ends if the agent stops
in the target area (the winning state), it moves out of the ﬁeld
or the time limit exceeds.
Chase and attack.
In this task, the agent should chase a
rule-based runner and attack it. The parameterized actions of
the agent are RUSH(directionR), ATTACK(directionA). The
runner has 3 lives at the beginning, and it loses one life every
time the agent performs a successful attack. The episode ends
when the runner loses all of its lives (the winning state for the
agent) or the time limit exceeds.
Half ﬁeld football.
This environment is a similar self-
implemented version of a sub-scenario in the Half Field
2https://www.dropbox.com/s/s0ut449i3e2fsk1/suppl.pdf
Offense (HFO) [Hausknecht et al., 2016].
The task of
the agent is to score a goal in the half football ﬁeld with
no goalie, and the same task in the original HFO envi-
ronment is used as test environment for RL algorithms
in parameterized action space by Hausknecht and Stone
[2016] and Xiong et al.
[2018].
The parameterized ac-
tions are DASH(powerD, directionD), TURN(directionT) and
KICK(powerK, directionK). The episode ends when the agent
scores a goal (the winning state), the ball is out of the valid
area, or the time limit exceeds.
4.2
Experiment Settings and Results
We evaluated the performance of the H-PPO on the four tasks
above. In addition, we also implemented and tested the fol-
lowing three baseline algorithms: the extended DDPG for pa-
rameterized action space by Hausknecht and Stone [2016],
the P-DQN algorithm [Xiong et al., 2018] and DQN which
ﬁrst discretizes the parameterized action space.
The networks in the four algorithms are of the same
size, and the hidden layer sizes for each network is
(256, 256, 128, 64). The replay buffer size for DDPG and
DQN is 10000, and the batch size for sampling is 32. For
DQN, we discretizes the action space of Chase and Attack
into 30 actions, 16 discrete actions for Catching Point and 23
discrete actions for Moving. However, since the action space
of Half Field Football task contains more parameters, the dis-
cretized action space has a relatively large size of 104 even if
we only discretize each direction parameter into 8 values and
each power parameter into 6 values.
Figure 6 shows the experiments results, which contains
both the success rate (the percentage of episodes which ends
in the winning state) and mean episode reward during training
of the methods in the four test environments. The experiment
results of DDPG are not included here because the perfor-
mance of DDPG in our experiments was far worse than in the
original paper, demonstrated a large variance and it failed to
learn reasonable policies, which is an issue also reported by
Wei et al. [2018]. Table 1 shows the success rate, standard de-
viation of success rate and mean episode reward achieved by
DQN, P-DQN and H-PPO after the same number of iterations
of learning in the four environments. As we can see from
the results, H-PPO showed stable learning and achieved high
Environment
Algorithm
SuccRate
SD of SuccRate
Mean Reward
Catching Point
DQN
6.13%
±8.21%
0.796
P-DQN
82.52%
±11.60%
4.977
H-PPO
96.32%
±4.82%
4.790
Moving
DQN
0.00%
±0.00%
-0.415
P-DQN
1.56%
±2.78%
0.173
H-PPO
90.45%
±6.75%
8.955
Chase and Attack
DQN
99.91%
±0.74%
5.664
P-DQN
99.85%
±0.84%
5.589
H-PPO
99.98%
±0.30%
5.393
Half Field Football
DQN
0.00%
±0.00%
0.000
P-DQN
76.31%
±16.81%
8.762
H-PPO
95.39%
±4.81%
9.849
Table 1: Success rate, standard deviation of success rate and mean
episode reward achieved by DQN, P-DQN and H-PPO in the exper-
iment environments.
Proceedings of the Twenty-Eighth International Joint Conference on Artiﬁcial Intelligence (IJCAI-19)
2283


## PDF page 6

(a) Catching Point
(b) Moving
(c) Chase and Attack
(d) Half Field Football
Figure 6: Results of the experiments on the four tasks. Left column:
Success rate of each method during training. Right column: Mean
episode reward of each method during training.
success rate on all the four tasks. Moreover, H-PPO outper-
formed other methods by a large margin in three of the four
environments (except in Chase and Attack, where the three
algorithms all achieved similar success rate and H-PPO had
the lowest variance, see Table 1). It generally achieved higher
success rate, faster convergence and lower variance than other
methods in the experiments.
To illustrate the learned action-selection and parameter-
selection policy of H-PPO from the micro perspective, Fig-
ure 7 shows the states of three frames (placed in the order of
time) observed in an episode of Half Field Football and the
parameterized actions selected by the H-PPO agent in these
(a) TURN
(b) DASH
(c) KICK
Figure 7: Illustration of the parameterized actions selected by the
H-PPO agent in three frames of a Half Field Football episode.
frames. Black arrows in Figure 7 indicates the facing direc-
tion of the agent, and arrows in other colors show the selected
actions and parameters. The agent was not close to the ball in
frame (a) and its direction was not toward the ball, so it per-
formed a TURN (the discrete action) with the speciﬁed angle
(the continuous parameter, shown in orange) to get closer to
the ball. Then it was roughly facing the ball in frame (b), and
it chose DASH along with proper power and direction (shown
in green). Finally, it took a KICK in the direction (shown
in purple) toward the goal in frame (c), when it was close
enough to the ball to perform the KICK. This example shows
the capability of H-PPO to learn the discrete action-selection
policy and the continuous parameter-selection policy in co-
ordination with its hybrid actor-critic architecture. This co-
ordination during training comes from the characteristics of
H-PPO that not only the two parallel actors share the ﬁrst few
layers of their networks, they also share the same critic to
perform policy optimization updates with similar objectives
given by Eq. (9) and Eq. (10).
5
Conclusion and Future Work
This paper introduced a hybrid actor-critic architecture for re-
inforcement learning in parameterized action space where the
discrete action policy and the continuous parameter policy are
trained in parallel as separate actors with a global critic. As
the hybrid actor-critic architecture is ﬂexible in the choice of
the policy optimization method, we also presented H-PPO,
which is an implementation of the architecture based on PPO.
Empirically, H-PPO achieves stable learning in all of the four
tasks with parameterized action space and outperforms previ-
ous methods of parameterized action reinforcement learning.
Although this paper is mainly focused on reinforcement
learning in parameterized action space, we also brieﬂy pre-
sented an extended version of the hybrid actor-critic architec-
ture for general hierarchical action spaces. More experiments
are needed to test the performance of this architecture in gen-
eral hierarchical action spaces, and we leave this investigation
as future work.
Acknowledgments
This work is supported by Tencent AI Lab Joint Research
Program. The corresponding author Weinan Zhang thanks
the support of National Natural Science Foundation of China
(61702327, 61772333, 61632017) and Shanghai Sailing Pro-
gram (17YF1428200).
Proceedings of the Twenty-Eighth International Joint Conference on Artiﬁcial Intelligence (IJCAI-19)
2284


## PDF page 7

References
[Hasselt et al., 2016] Hado van Hasselt, Arthur Guez, and
David Silver. Deep reinforcement learning with double q-
learning. In Proceedings of the Thirtieth AAAI Conference
on Artiﬁcial Intelligence, AAAI’16. AAAI Press, 2016.
[Hausknecht and Stone, 2016] Matthew Hausknecht and Pe-
ter Stone. Deep reinforcement learning in parameterized
action space. In Proceedings of the International Confer-
ence on Learning Representations (ICLR), May 2016.
[Hausknecht et al., 2016] Matthew
Hausknecht,
Prannoy
Mupparaju, Sandeep Subramanian, Shivaram Kalyanakr-
ishnan, and Peter Stone. Half ﬁeld offense: An environ-
ment for multiagent learning and ad hoc teamwork.
In
AAMAS Adaptive Learning Agents (ALA) Workshop, May
2016.
[Heess et al., 2015] Nicolas Heess, Gregory Wayne, David
Silver, Timothy Lillicrap, Tom Erez, and Yuval Tassa.
Learning continuous control policies by stochastic value
gradients.
In C. Cortes, N. D. Lawrence, D. D. Lee,
M. Sugiyama, and R. Garnett, editors, Advances in NIPS
28. Curran Associates, Inc., 2015.
[Kober et al., 2013] Jens Kober, J. Andrew Bagnell, and Jan
Peters. Reinforcement learning in robotics: A survey. The
International Journal of Robotics Research, 32(11):1238–
1274, 2013.
[Konda and Tsitsiklis, 2000] Vijay R. Konda and John N.
Tsitsiklis. Actor-critic algorithms. In S. A. Solla, T. K.
Leen, and K. M¨uller, editors, Advances in Neural Informa-
tion Processing Systems 12, pages 1008–1014. MIT Press,
2000.
[Lillicrap et al., 2016] Timothy P. Lillicrap,
Jonathan J.
Hunt, Alexander Pritzel, Nicolas Heess, Tom Erez, Yu-
val Tassa, David Silver, and Daan Wierstra.
Continu-
ous control with deep reinforcement learning.
CoRR,
abs/1509.02971, 2016.
[Masson et al., 2016] Warwick Masson, Pravesh Ranchod,
and George Konidaris. Reinforcement learning with pa-
rameterized actions. In Proceedings of the Thirtieth AAAI
Conference on Artiﬁcial Intelligence, AAAI’16, pages
1934–1940. AAAI Press, 2016.
[Mnih et al., 2013] Volodymyr Mnih, Koray Kavukcuoglu,
David Silver, Alex Graves, Ioannis Antonoglou, Daan
Wierstra, and Martin Riedmiller. Playing atari with deep
reinforcement learning.
In NIPS Deep Learning Work-
shop. 2013.
[Mnih et al., 2016] Volodymyr Mnih, Adria Puigdomenech
Badia, Mehdi Mirza, Alex Graves, Timothy Lillicrap, Tim
Harley, David Silver, and Koray Kavukcuoglu.
Asyn-
chronous methods for deep reinforcement learning.
In
Proceedings of The 33rd International Conference on Ma-
chine Learning, Proceedings of Machine Learning Re-
search, New York, New York, USA, 2016. PMLR.
[Schulman et al., 2015] John
Schulman,
Sergey
Levine,
Pieter Abbeel, Michael Jordan, and Philipp Moritz. Trust
region policy optimization.
In Francis Bach and David
Blei, editors, Proceedings of the 32nd International Con-
ference on Machine Learning, Proceedings of Machine
Learning Research, Lille, France, 2015. PMLR.
[Schulman et al., 2017] John Schulman, Filip Wolski, Pra-
fulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal
policy optimization algorithms. CoRR, abs/1707.06347,
2017.
[Sherstov and Stone, 2005] Alexander A. Sherstov and Pe-
ter Stone. Function approximation via tile coding: Au-
tomating parameter choice.
In Jean-Daniel Zucker and
Lorenza Saitta, editors, Abstraction, Reformulation and
Approximation, pages 194–205, Berlin, Heidelberg, 2005.
Springer Berlin Heidelberg.
[Silver et al., 2014] David Silver, Guy Lever, Nicolas Heess,
Thomas Degris, Daan Wierstra, and Martin Riedmiller.
Deterministic policy gradient algorithms.
In Proceed-
ings of the 31st International Conference on International
Conference on Machine Learning - Volume 32, ICML’14,
pages I–387–I–395. JMLR.org, 2014.
[Silver et al., 2016] David Silver, Aja Huang, Christopher J.
Maddison, et al. Mastering the game of go with deep neu-
ral networks and tree search. Nature, 529:484–503, 2016.
[Silver et al., 2017] David
Silver,
Julian
Schrittwieser,
Karen Simonyan, et al. Mastering the game of go without
human knowledge. Nature, 550:354–, October 2017.
[Sutton et al., 2000] Richard S Sutton, David A. McAllester,
Satinder P. Singh, and Yishay Mansour. Policy gradient
methods for reinforcement learning with function approx-
imation. In S. A. Solla, T. K. Leen, and K. M¨uller, editors,
Advances in Neural Information Processing Systems 12,
pages 1057–1063. MIT Press, 2000.
[Vinyals et al., 2017] Oriol Vinyals, Timo Ewalds, Sergey
Bartunov, et al.
Starcraft II: A new challenge for rein-
forcement learning. CoRR, abs/1708.04782, 2017.
[Wang et al., 2016] Ziyu Wang, Tom Schaul, Matteo Hessel,
Hado Hasselt, Marc Lanctot, and Nando Freitas. Duel-
ing network architectures for deep reinforcement learning.
In Proceedings of The 33rd International Conference on
Machine Learning, Proceedings of Machine Learning Re-
search, New York, New York, USA, 2016. PMLR.
[Watkins and Dayan, 1992] Christopher J. C. H. Watkins and
Peter Dayan.
Q-learning.
In Machine Learning, pages
279–292, 1992.
[Wei et al., 2018] Ermo Wei, Drew Wicke, and Sean Luke.
Hierarchical approaches for reinforcement learning in pa-
rameterized action space. CoRR, abs/1810.09656, 2018.
[Xiong et al., 2018] Jiechao Xiong, Qing Wang, Zhuoran
Yang, Peng Sun, Lei Han, Yang Zheng, Haobo Fu, Tong
Zhang, Ji Liu, and Han Liu.
Parametrized deep q-
networks learning: Reinforcement learning with discrete-
continuous hybrid action space. CoRR, abs/1810.06394,
2018.
Proceedings of the Twenty-Eighth International Joint Conference on Artiﬁcial Intelligence (IJCAI-19)
2285
