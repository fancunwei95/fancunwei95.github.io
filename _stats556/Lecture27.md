---
title: Lecture 27 (April 01, 2022)
classes: wide
excerpt: "Continutation of Jump Diffusion Model and Introduction to Multiple Time Series"
date: 2022-04-01

---

Recall the jump diffusion model:

$$
\frac{dP_t}{P_t} = \mu dt + \sigma dw_t + d \left[\sum_{i=1}^{n_t} (J_i-1) \right]
$$

with $\mu$, $\sigma$ constants, This gives 

$$
P_t = P_0 \exp \left[(\mu-\frac{\sigma^2}{2}) t + \sigma w_t \right] \prod_{i=1}^{n_t} J_i
$$

For small $\Delta t$, 

$$
\frac{P_{t+\Delta t} - P_t}{ P_t} \approx \mu \Delta t  + \sigma\sqrt{\Delta t} \epsilon_t  + \sum_{i=n_t+1}^{n_{t+\Delta t}} x_i
$$

with $x_i = \log J_i$ and $n_t$ is a Poisson process. When $\Delta t$ is small, 

$$
\sum_{i=n_t+1}^{n_{t+\Delta t}}x_i = \left\{ 
\begin{aligned}
&x_{n_t+1} \text{ with prob } \lambda \Delta t\\
&0 \text{ with prob } 1-\lambda \Delta t 
\end{aligned}
\right.
$$

and thus, 

$$
\frac{P_{t+\Delta t} - P_t}{P_t} = \mu \Delta t + \sigma \sqrt{\Delta t} \epsilon + Z\times X
$$

with $Z\sim \text{Bernoulli}(\lambda \Delta t)$ , $X\sim \text{Laplace}(\kappa, \eta)$.  $Z$ is the number of jumps and $X$ is the jump size. 

It is shown that $G = Z\times X$ has pdf as 

$$
\begin{aligned}
g(x) = \frac{\lambda \Delta t}{2\eta} e^{\sigma^2\Delta t/(2\eta^2)} \sum_{i=0}^1 \exp \left(\frac{(-1)^i w}{n} \right) \Phi\left(\frac{w \eta + (-1)^i \sigma^2 \Delta t}{\sigma \eta \sqrt{\Delta t}} \right) \\
+ (1-\lambda \Delta t) \frac{1}{\sigma \sqrt{\Delta t}} \phi\left(\frac{x-\mu\Delta t}{\sigma \sqrt{\Delta t}} \right)
\end{aligned}
$$

where $w = x -\mu \Delta t - \kappa$, $\Phi$ \& $\phi$ is the cdf and pdf of $N(0,1)$ respectively. 

with 

$$
\begin{aligned}
&\mathbb{E} G = \kappa \lambda \Delta t \\
&\text{Var}(G) = \sigma^2 \Delta t + \lambda \Delta t [2\eta^2 + \kappa^2(1-\lambda \Delta t)]
\end{aligned}
$$

### Multiple Time Series

$x_t = (x_{1t}, \dots, x_{kt})^T$, $t=1, \dots, T$ weakly stationary. $\mu = \mathbb{E} x_t\sim \mathbb{R}^k$, $\Gamma(0) = \Gamma_0 = \mathbb{E}(x_t-\mu)(x_t-\mu)^T \in \mathbb{R}^{k\times k}$ Concurrent/contemporanerous covariance matrix. 

**lag**-0 **correlation matrix** : 

$$
\rho_0 = \left[ \rho_{ij} (0)\right]^k_{i,j=1} = D^{-1} \Gamma_0 D^{-1}
$$

where 

$$
D = [\text{diag}(\Gamma_0)]^{1/2}
$$

that is 

$$
\rho_{ij}(0) = \frac{\Gamma_{ij}(0)}{\sqrt{\Gamma_{ii}(0) \Gamma_{jj}(0)}}
$$

Properties: 

1. $\rho_0^T = \rho_0$ symmetric 
2. $-1 \leq \rho_{ij}(0) \leq 1$ 
3. $\rho_{ii}(0) = 1, \quad i=1,\dots, n$. 

**lag-$l$ cross correlation matrix**

$$
\rho_l = [\rho_{ij}(l)]_{ij}^k = D^{-1} \Gamma_l D^{-1}
$$

data: $(x_t)_{t=1}^T$ $k$-dim time series

Test: $H_0$: $\rho_1 = \dots \rho_m = 0_{k\times k}$ v.s. $H_1: \rho_i \neq 0$ for some $i\in [m]$. 

**Ljung-Box test statistics**: 

recall $k=1$, $Q(m) = T^2 \sum_{l=1}^m \frac{\hat\rho_l}{T-l}$ with $\hat\rho_0 = 1$.  Here, we define $Q_k(m)$ as follows 

$$
Q_k(m) = T^2 \sum_{l=1}^m \frac{1}{T-l} \text{tr}( \hat\Gamma_l^T \hat\Gamma_0^{-1}\hat\Gamma_l \hat\Gamma_0^{-1})
$$

Under $H_0$, $Q_k(m)\rightarrow \chi^2(km)$ , as $T\rightarrow \infty$ . 

Remark:

1. $\text{tr}(ABC) = \text{vec}(A^T)^T (C^T\otimes I) \text{vec}(B)$. 
2. $\text{vec}(ABC) = (C^T\otimes A) \text{vec}(B)$ 
3. $(A\otimes B) (C\otimes D) = (AC)\otimes (BD)$ 

Then 

$$
\begin{aligned}
&\text{tr}(\hat{\Gamma}_l^T \hat{\Gamma}_0^{-1} \hat\Gamma_l \hat\Gamma_0^{-1}) \\
&= \text{vec}(\hat\Gamma_l)^T (\hat\Gamma_0^{-1}\otimes I) \text{vec}(\hat\Gamma_0^{-1} \Gamma _l I) \\
&= \text{vec}(\hat\Gamma_l)^T (\hat\Gamma_0^{-1}\otimes I) (I\otimes \Gamma_0^{-1})\text{vec}(\hat\Gamma_l) \\
&= \text{vec}(\hat\Gamma_l)^T (\hat\Gamma_0^{-1}\otimes \hat\Gamma_0^{-1}) \text{vec}(\hat\Gamma_l)  
\end{aligned}
$$

Note that 

$$
\begin{aligned}
&\text{tr} (\hat\Gamma_l^{-1}\hat\Gamma_0^{-1} \hat\Gamma_l\hat\Gamma_0 ^{-1}) \\
&=\text{tr} (\hat D (\hat D ^{-1} \hat\Gamma_l^T \hat D ^{-1}) (\hat D^{-1} \hat \Gamma_0 \hat D^{-1})^{-1}(\hat D ^{-1} \hat\Gamma_l^T \hat D ^{-1}) (\hat D^{-1} \hat \Gamma_0 \hat D^{-1})^{-1} \hat{D}^{-1} )\\
&=\text{tr}\left( \hat \rho_l \hat\rho_0^{-1} \hat\rho_l \hat\rho_0^{-1}\right)\\
&=\text{vec}(\hat\rho_l)^T(\hat\rho_0^{-1}\otimes \hat\rho_0^{-1})\text{vec}(\hat\rho_l)
\end{aligned}
$$


