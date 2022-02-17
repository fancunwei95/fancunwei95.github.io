---
title: Lecture 05 (Feb 02, 2022)
classes: wide
excerpt: "Periodicity of AR models with complex roots; Asymptotic statistics of AR(p) models "
date: 2022-02-02
---


Since $\omega_1$ and $\omega_2$ is a conjugate pair ($x_1, x_2$ is a conjugate pair and thus their inverse). The stochastic cycle of the AR(2) is then 

$$
k = \frac{2\pi}{\cos^{-1}{\frac{\phi_1}{2\sqrt{-\phi_2}}}}
$$

The complex angle $\theta$ controls the cycle length because 

$$
(1-\omega B) x_t = 0 \quad \Rightarrow x_t = ae^{i\theta} x_{t-1}
$$

Thus, $2\pi/\theta$ is approximately the periodic length. 

### Asymptotics of AR(p) models 

$x_t = \phi_0 + \phi_1 x_{t-1} + \dots. + \phi_p x_{t-p} + \epsilon_t$ where $\epsilon_t$ iid mean-zero with $\text{Var}(\epsilon_t) = \sigma^2$. 

Assume $\phi_0=0$ estimate the coefficients, the vecotr $\phi = (\phi_1, \phi_2,\dots,\phi_p)^T$.  By the least squares, let $M_t = (x_{t-1}, \dots, x_{t-p})$ design matrix. Write $x_t = M_t \phi + \epsilon_t$. 

Thus, 

$$
\hat{\phi} = \arg\min_{\phi} \sum_{t=p+1}^T (x_t - M_t\phi)^2
$$

Take derivative, we find 

$$
\begin{aligned}
\hat{\phi} &= \left(\sum_{t=p+1}^T M_t^{T}M_t \right)^{-1}\left(\sum_{t=p+1}^T M_t^T X_t \right)\\
&= \left(\sum_{t=p+1}^T M_t^T M_t \right)^{-1} \left(\sum_{t=p+1}^T M_t^T(\phi_1x_{t-1} + \dots \phi_p x_{t-p} + \epsilon_t) \right) \\
&= \phi + \left(\sum_{t=p+1}^T M_t^T M_t\right)^{-1} \left(\sum_{t=p+1}^T M_t^T \epsilon_t \right)
\end{aligned}
$$

provide that $\sum_{t=p+1}^T M_t^T M_t $ positive definite. 

Write 

$$
\sqrt{T}(\hat{\phi} - \phi) = \left(\frac{1}{T}\sum_{t=p+1}^T M_t^T M_t \right)^{-1} \left(\frac{1}{\sqrt{T}} \sum_{t=p+1}^T M_t^T \epsilon_t \right)
$$

The numerator becomes 

$$
\frac{1}{T} \sum_{t=p+1}^T M_t^T M_t = \frac{1}{T} \sum_{t=p+1}^T \begin{pmatrix}x_{t-1} \\ x_{t-2}\\ \vdots \\ x_{t-p} \end{pmatrix} \begin{pmatrix}x_{t-1} & x_{t-2} &\dots & x_{t-p} \end{pmatrix}
$$

which converges 

$$
\Gamma = \begin{pmatrix}
\mathbb{E}x_{t-1}^2 &\dots &\mathbb{E}x_{t-1}x_{t-p} \\
\vdots & \ddots & \vdots \\
\mathbb{E}x_{t-1}x_{t-p} & \dots & \mathbb{E}x_{t-p}^2
\end{pmatrix}
$$

Claim, $\frac{1}{\sqrt{T}}\sum_{t=p+1}^T M_t^T\epsilon_t \rightarrow \mathcal{N}(0,\sigma^2\Gamma) $ because $M_t^T \epsilon_t$ is a martingale difference sequence. That is if $\mathcal{F}_t$ is the filtration $(\epsilon_1,\dots, \epsilon_t)$ then 

$$
\mathbb{E}[M_t^T\epsilon_t | \mathcal{F}_{t-1}] = 0
$$

which is the martingale. Also, since $\epsilon_t$ are independnet, the variance is the sum of each term and the variance of each term is $\frac{1}{T}M_t^TM_t\sigma^2$ and the sum will converge to  the above sum.

So 

$$
\sqrt{T}(\hat{\phi} - \phi) \rightarrow \Gamma^{-1} \mathcal{N}(0,\sigma^2\Gamma) = \mathcal{N}(0,\sigma^2\Gamma^{-1})
$$




