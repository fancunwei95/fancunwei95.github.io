---
title: Lecture 11 (Feb 16, 2022)
classes: wide
excerpt: "Spectral representation sample version proof. Variance decomposition into Fourier components. Estimate spectral density"
date: 2022-02-16

---
proof for spectral representation sample version:

Assume $T$ is odd and define $M = (T-1)/2$. Then we define $\omega_1 = 2\pi/T, \omega_2 = 4\pi/T,\dots, \omega_M = 2M\pi/T$. (Thus, at least use 2 points to define a cycle, $T$ contains at most $T/2$ cycles). Note $\cos(\omega_j t)$ and $\sin(\omega_j t)$ and $1_T$ constitute $2M +1 = T$ linearly independent vectors and $x_t$ lives in $\mathbb{R}^T$. then we can find coeffcients for each vector. Specifically, the desgin matrix is 

$$
M_t = \left(1, \cos(\omega_1(t-1)), \sin(\omega_1(t-1)), \dots ,\cos(\omega_M(t-1)), \sin(\omega_M(t-1)) \right)
$$

with $t$ acts as the row index. Thus, the coeffcients will be 

$$
\hat\theta = \left(\sum_{i=1}^T M_t^TM_t \right)^{-1} \left(\sum_{t=1}^T M_t x_t \right)
$$

The exact form of the $M^TM$ will be 

$$
\sum_{t=1}^T M_t^T M_t = \begin{bmatrix} 
T & 0^T \\
0 & \frac{T}{2} I_{T-1} 
\end{bmatrix}
$$
thus, the parameters become 
$$
\hat{\theta} = \begin{bmatrix} 
T & 0^T \\
0 & \frac{T}{2} I_{T-1} 
\end{bmatrix} \begin{bmatrix}
\sum_{t=1}^T x_t \\
\sum_{t=1}^T x_t\cos(\omega_1(t-1)) \\
\sum_{t=1}^T x_t\sin(\omega_1(t-1)) \\
\vdots \\
\sum_{t=1}^T x_t\cos(\omega_M(t-1))\\
\sum_{t=1}^T x_t\sin(\omega_M(t-1))
\end{bmatrix}
$$

we then see that 

$$
\begin{aligned}
&\hat{\mu} = \frac{1}{T} \sum_{t=1}^T x_t \\
&\hat\alpha_j = \frac{2}{T} \sum_{t=1}^T x_t \cos(\omega_j(t-1)) \\
&\hat\beta_j = \frac{2}{T} \sum_{t=1}^T x_t \sin(\omega_j(t-1)) 
\end{aligned}
$$

which is just an ordinary sample Fourier decomposition. 

because the decomposition is exact we have 

$$
\sum_{t=1}^T (\hat x_t - x_t)^2 = 0
$$

for $\hat{x}_t = M_T \hat\theta $. By some calculation, we could find that 

$$
\frac{1}{T} \sum_{t=1}^T (x_t - \hat\mu)^2 = \frac{1}{2}\sum_{j=1}^M(\hat\alpha_j^2 + \hat\beta_j^2)
$$

we can further write it in the periodigram as 

$$
\frac{1}{T} \sum_{t=1}^T (x_t - \hat\mu)^2 = \frac{1}{2}\sum_{j=1}^M(\hat\alpha_j^2 + \hat\beta_j^2) = \frac{4\pi}{T} \sum_{j=1}^M\hat S(\omega_j)
$$

### Estimating spectral density

Goal: given the observations $(x_1, \dots, x_T)$ estimate $S(\omega)$. 

Naive idea: use sample periodogram $\hat{S}(\omega)$ to estimate $S(\omega)$. 

Consider $X_t = \sum_{j=0}^\infty \psi_j \epsilon_{t-j}$ where $\sum_{j=0}^\infty |\psi_j| < \infty$ Asssume $s(\omega) >0$ , for $\forall \omega$ ,  then 
$$
\begin{aligned}
&\frac{2\hat S(\omega) }{ S(\omega)} \rightarrow \chi^2(2)\\
&\hat{S}(\omega) \text{ and } \hat{S}(\lambda) \text{ asymptotically independent}
\end{aligned}

$$
This shows 

$$
\mathbb{E} \left[\frac{2\hat{S}(\omega)}{S(\omega)} \right] \sim 2
$$

this means $\hat{S}(\omega)$ is unbiased. But there is no variance reduction asymptotically. 

To fix, there are two ways: parametric models and nonparametric models. 

### parametric estimation

Assum $ARMA(p,q)$ model, we have 

$$
x_t = \phi_0 + \phi_1 x_{t-1} + \dots + \phi_p x_{t-p} +\epsilon_t - \theta_1\epsilon_{t-1} - \theta_2\epsilon_{t-2} -\dots
$$

Step1: estimate the parameters $(\phi_1,\dots,\phi_p)$ 

Step2: esimate the spectral density by closed form formula:

$$
\hat S(\omega)  = \frac{\hat{\sigma}^2}{2\pi }
$$
