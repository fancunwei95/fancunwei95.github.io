---
title: Lecture 31 (April 11, 2022)
classes: wide
excerpt: "Introduction to state space model, the Kalman Filterl"
date: 2022-04-11

---

### Kalman Filter

Goal: Express a dynamical system with state-space representation. 

State-space model: 

Data: $y_1,\dots, y_T\in \mathbb{R}^n$ 

hidden latent state vector: $\xi_t \in \mathbb{R}^r$ 

Example: Hidden Markov Model : transition for the hidden vector $\xi_t$ is markov and the emssion takes $\xi_t$ and $x_t$ to get $y_t$. 

$$
\begin{aligned}
&\xi_{t+1} = F\xi_t + V_{t+1} \quad \text{state equation}\\
&y_t = A^T x_t + H^T \xi_t + w_t
\end{aligned}
$$

where $\xi_t \in \mathbb{R}^r$ and $y_t\in \mathbb{R}^n$ . $F$ is $r\times r$ matrix and $A^T$ is an $n\times k$ matrix and $H^T$ is $n\times r$ matrix. 

$x_t\in \mathbb{R}^k$ is the exogenous/predetermined variables. $x_t$ contains no information about $\xi_t$. 

$v_t$ and $w_t$ are iid with mean zero 

$$
\mathbb{E}v_tv_\tau^T = Q_{r\times r} \delta_{t,\tau}
$$

and 

$$
\mathbb{E}w_tw_t^T = R_{n\times n} \delta_{t,\tau}
$$

Initial state $\xi_1$ s.t. 

$$
\mathbb{E} v_t \xi_1^T = 0 \quad \mathbb{E} w_t \xi_1^T =0
$$

Note these conditions does not require independence but only correlation to be zero. 

The parameters are $(F, A, H, Q, R)$ . The state equation is 

$$
\xi_t = F\xi_{t-1} + V_t = V_t + FV_{t-1} + F ^2 V_{t-2} + \dots + F^{t-2} V_{t-2} + F^{t-1} \xi_1
$$

The causal constraints require that 

$$
\begin{aligned}
&\mathbb{E} v_t \xi^T_\tau  = 0 \quad \tau \leq t-1 \\
&\mathbb{E} v_t y_\tau^T = 0 \quad \tau \leq t-1\\
&\mathbb{E} w_t y_\tau^T = 0 \quad \tau \leq t-1
\end{aligned}
$$

and by construction, we need 

$$
\mathbb{E} w_t\xi_\tau^T = 0 \quad \forall \tau
$$

Example: The $AR(p)$ Process can be described as a state space equation:

$$
\begin{pmatrix} y_{t+1} - \mu \\ y_t - \mu \\ \vdots \\ y_{t-p+2} - \mu\end{pmatrix}
= \begin{pmatrix}
\phi_1 & \dots & \phi_{p-1} & \phi_p \\
0 & 1 & \dots & 0 \\ 
0 & 0 & \ddots & \vdots \\
0 & 0 & \dots & 1
\end{pmatrix}
\begin{pmatrix} y_t-\mu \\ y_{t+1}-\mu \\ \vdots \\ y_{t-p+1}-\mu \end{pmatrix} +
\begin{pmatrix} \epsilon_{t+1} \\ 0 \\ \vdots \\ 0 \end{pmatrix}
$$

The observation equation becomes 

$$
y_t = \mu + \begin{pmatrix}1 & 0 \dots & 0 \end{pmatrix} \begin{pmatrix} y_t -\mu \\ y_{t-1}-\mu \\ \dots \\y_{t-p+1} -\mu \end{pmatrix} + 0
$$

which is of the form 

$$
y_t = A^T x_t + H^T \xi_t + w_t
$$

where $w_t = 0$ and $A^Tx_t = \mu$ and $\xi_t$ is just $(y_{t-\mu} , \dots, y_{t-p+1}-\mu)^T$. 

We could set $x_t =1 $ and $A^T = \mu$ and $R= 0 $ and 

$$
Q = \mathbb{E}V_tV_t^T = \begin{pmatrix} \sigma^2 & 0 & \cdots & 0 \\
0 & \\
\vdots &\\
0 & \\
\end{pmatrix}_{p\times p}
$$
