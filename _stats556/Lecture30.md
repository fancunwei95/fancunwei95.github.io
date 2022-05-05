---
title: Lecture 30 (April 08, 2022)
classes: wide
excerpt: "Introduction to Vector Error Correction Model"
date: 2022-04-08

---

### Vector Error Correction Model (VECM)

General VARMA($p$,$q$) model:

$$
x_t - \sum_{i=1}^p \Phi_i x_{t-i} = \epsilon_t - \sum_{j=1}^q \Theta_j \epsilon_{t-j}
$$

THe VECM form:

$$
\Delta x_t = \alpha \beta^T x_{t-1} + \sum_{i=1}^{p-1} \Phi_i^*\Delta x_{t-i} + \epsilon_t - \sum_{j=1}^q \Theta_j \epsilon_{t-j}
$$

where $\Delta x_t = x_t-x_{t-1}$, $\alpha$, $\beta$  are $k\times m$ matrix with $m\leq k$ and the full rank is $k$. Also, $\Phi_{i}^* = -\sum_{j=i+1}^p \Phi_j$.  with $\beta = (\beta_1, \dots, \beta_m)$ which is a $k\times m$ matrix, which is called the cointegration vector. 

Computation:

$$
\begin{aligned}
\sum_{i=1}^{p-1} \Phi_i^*\Delta x_{t-i} &= \sum_{i=1}^{p-1} \Phi_i^* (x_{t-i} - x_{t-i-1}) \\
&=\sum_{i=1}^{p-1} \Phi_i^* x_{t-i} - \sum_{i=1}^{p-1} \Phi_i^* x_{t-i-1} \\
&=\sum_{i=1}^{p-1} \Phi_i^* x_{t-i} - \sum_{i=2}^p \Phi^*_{i-1} x_{t-i} \\
&= \Phi_1^* x_{t-1} -\Phi_{p-1}^* x_{t-p}  + \sum_{i=2}^{p-1} \Delta\Phi_i^* x_{t-i} \\
&= -\sum_{i=2}^p \Phi_i x_{t-1} + \Phi_p x_{t-p} + \sum_{i=2}^{p-1} \Phi_{i} x_{t-i} \\
&= -\sum_{i=2}^p \Phi_i x_{t-1} + \sum_{i=2}^{p} \Phi_i x_{t-i} 
\end{aligned}
$$

Then the general form of VECM becomes 

$$
x_t - \sum_{i=2}^p\Phi_i x_{t-i} = (I_k + \alpha \beta^T - \sum_{i=2}^p \Phi_i) x_{t-1} + \epsilon_t - \sum_{j=1}^q \Theta_j \epsilon_{t-j}
$$

We can add $-\Phi_{1} x_{t-1}$ on both sides, we then have 

$$
x_t - \sum_{i=1}^p \Phi_i x_{t-i} = (I_k + \alpha\beta^T - \sum_{i=1}^p\Phi_i) x_{t-1} + \epsilon_t - \sum_{j=1}^q \Theta_j \epsilon_{t-j}
$$

The left hand side is the the original $AR(p )$ part and thus we need that 

$$
\alpha\beta^T = -I_k + \sum_{i=1}^p \Phi_j = - \Phi(1)
$$

where $\Phi(B)$ is the AR polynomial $I - \Phi_1B - \Phi_2 B^2-\dots $  It looks like the matrix $\alpha\beta^T$ will be not of full rank if $\sum_{i=1}^p \Phi_j$ has an eigen value of $1$. 

Consider a cointegrated $VAR(p)$ model:

$$
x_t = \mu + \Phi_1 x_{t-1} + \dots + \Phi_p x_{t-p} + \epsilon_t
$$

Recall: if all zeros of $\det(\Phi(B))$ are outside of the unit circle then $x_t$ is a unit root stationary. If $\det (\Phi(1)) = 0$, then $x_t$ is unit root non-stationary. Unit root stationary is $I(0)$ process and unit root non-stationary is $I(1)$ process. 

$$
\Delta x_t = \mu + \Pi x_{t-1} + \Phi_1^*\Delta x_{t-1} + \dots + \Phi_p^* \Delta x_{t-p} + \epsilon_t
$$

and $\Pi = \alpha \beta^T = - \Phi(1)$. 

When rank $\Pi$ = 0, then $\Pi = 0_{k\times k}$ matrix and then 

$$
\Delta x_t = \mu + \Phi_1^* \Delta x_{t-1} + \dots. + \Phi_p^* \Delta x_{t-p} + \epsilon_t
$$

when $x_t$ is not cointegrated (i.e. no common stochastic trend), then each $x_{it}$ is independent $I(1)$ process. 

When rank $\Pi = k$, Then $\Pi$ is not singular and thus $x_t$ is an $I(0)$ process and no need to use the VECM formulation. 

When rank $\Pi <k$  then the model is 

$$
\Delta x_t = \mu + \alpha\beta^T x_{t-1} + \Phi_1^*\Delta x_{t-1} + \dots + \Phi_p^* \Delta x_{t-p} + \epsilon_t
$$

$x_t$ is cointegrated with m linearly independent cointegration vector $\beta$ and the components of $x_t$ in these cointegration vector is  $w_t = \beta^T x_t$ and $k-m$ common stochastic rends in $x_t$.  

How to botain the $k-m$ common stochastic trends? 

$\alpha: k\times m$. and $\alpha_\perp $ is the $k\times (k-m)$ matrix that is perpendicular to $\alpha$.  i.e. the column vecotrs in $\alpha_\perp$ are all perpendicular to $\alpha$ and they are orthonormal in themselves. 

Then 

$$
\alpha_\perp^T\Delta x_t = \alpha_\perp^T \mu + \alpha_\perp^T \Pi x_{t-1} + \sum_{i=1}^p \alpha_\perp^T \Phi_i^* \Delta x_{t-i} + \alpha_\perp^T \epsilon_t
$$

If we let $\Delta y_t = \alpha_\perp^T \Delta x_t$ and $\alpha_\perp^T\alpha \beta^T = 0$ and this shows that 

$$
\Delta y_t = \alpha_\perp^T \mu + \sum_{i=1}^T \alpha_\perp^T \Phi_i^* \alpha_\perp  \Delta y_{t-1} + \alpha_\perp^T \epsilon_t
$$

which is the unit root components. and

$$
w_t = \beta^T x_t
$$

is the unit-root stationary part. 

If $\Omega \Omega^T = I_m$, then 

$$
\alpha\beta^T = \alpha \Omega \Omega^T \beta^T = (\alpha\Omega) (\beta\Omega)^T
$$

thus, $\alpha, \beta$ are not unique. We need extra constraints to fix $\alpha$ and $\beta$. Need $\beta$ to be 

$$
\beta^T = [I_m; \beta_c^T] \quad \beta_c^T : m\times (k-m)
$$

example: 

$k=2, m=1$,

$$
\Delta x_t = \mu + \begin{pmatrix} \alpha_1 \\ \alpha_2 \end{pmatrix} \begin{pmatrix} 1 & \beta_c \end{pmatrix} x_{t-1} + \epsilon_t
$$

we have $w_t = \beta^T x_t$ and thus, 

$$
\beta^T \Delta x_t = \beta^T \mu + \begin{pmatrix}1 & \beta_c \end{pmatrix} \begin{pmatrix} \alpha_1 \\ \alpha_2 \end{pmatrix} \begin{pmatrix} 1 & \beta_c \end{pmatrix} x_{t-1} + \beta^T \epsilon_t 
$$

This shows that 

$$
\Delta w_t = \beta^T \mu + (\alpha_1 + \beta_c\alpha_2) w_{t-1} + \beta^T \epsilon_t
$$

which gives 

$$
w_t = \beta^T \mu + (1 + \alpha_1 + \beta_c \alpha_2) w_{t-1} + \beta^T \epsilon_t
$$


