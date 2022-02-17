---
title: Lecture 10 (Feb 14, 2022)
classes: wide
excerpt: "Spectral density as the Fourier transform of autocovariance, the sample version spectral representation theory and sample periodogram"
date: 2022-02-14

---

Review: Spectral representation theorem: for weakly stationary $x_t$, 

$$
x_t = \mu + \int_0^\pi \alpha(\omega) \cos(\omega t) d\omega + \int_0^\pi \beta(\omega)\sin(\omega t)d\omega
$$

where $\forall 0\leq \omega_1\leq \omega_2<\omega_3\leq \omega_4\leq \pi $ , $\alpha(\omega)\vert_{\omega_1}^{\omega_2}$ and $\alpha(\omega)\vert_{\omega_3}^{\omega_4}$ uncorrelated,  $\beta(\omega)\vert_{\omega_1}^{\omega_2}$ and  $\beta(\omega)\vert_{\omega_3}^{\omega_4}$ uncorrelated and $\alpha(\omega)$ and $\beta(\omega)$ are uncorrelated. The sepctral density is defined as 

$$
s(\omega) = \frac{1}{2\pi} \sum_{j=-\infty}^\infty \gamma_j e^{-i\omega j}
$$

which is the fourier transform of $\gamma_j$. Then:

1. $s(\omega)$ is well defined .
2. $s(\omega) \in \mathbb{R}^+$ and differentiable in $\omega$
3. $s(-\omega) = s(\omega)$
4. $s(\omega+2\pi k) = s(\omega)$

a. For $MA(\infty)$, for $\psi(z) = \sum_{j=0}^\infty \psi_j z^j$.  

$$
2\pi s(\omega) = \sigma^2\psi(e^{-i\omega})\psi(e^{i\omega})
$$

b. For $MA(1)$, $\psi(z) = 1- \theta_z$ and thus, 

$$
s(\omega) = \frac{\sigma^2}{2\pi}(1-2\theta_1\cos(\omega) +\theta_1^2)
$$

c. For $AR(1)$, $\psi(z) = \frac{1}{\phi(z)} = \frac{1}{1-\phi_1z}$. Thus, 

$$
\begin{aligned}
s(\omega) &= \frac{\sigma^2}{2\pi} \frac{1}{1-\phi_1e^{-i\omega}}\frac{1}{1-\phi_1e^{i\omega}}\\
&=\frac{\sigma^2}{2\pi}\frac{1}{1-2\phi_1\cos\omega + \phi_1^2}
\end{aligned}
$$

when $\phi_1>0$, this is a positive dependence but the $s(\omega)$ decreases from $\omega = 0$ to $\pi$ and thus this is low frequency dominant. when $\phi_1<0$ , this is a negative dependency and $s(\omega)$ increases from $\omega = 0$ to $\pi$ and thus is a high frequency dominant sequence. 

d. For $ARMA(p,q)$ , $\phi(B) x_t = \phi_0 + \theta(B)\epsilon_t$. and thus

$$
s(\omega) = \frac{\sigma^2}{2\pi} \frac{1-\theta_1e^{-i\omega} -\dots - \theta_1e^{-i\omega q}}{1-\phi_1e^{-i\omega} -\dots \phi_pe^{-i\omega p} } \frac{1-\theta_1e^{i\omega} -\dots - \theta_1e^{i\omega q}}{1-\phi_1e^{i\omega} -\dots \phi_pe^{i\omega p} }
$$

**Theorem** Let $\gamma_k$ be an absolutely summable sequence of autocovariance. and let $s(\omega) = \frac{1}{2\pi}\sum \gamma_j e^{-i\omega j}$ Then

$$
\gamma_j = \int_{-\pi}^\pi s(\omega)e^{i\omega j} d\omega 
$$

which is the inverse Fourier transform. 
For $j=0$, $\gamma_0 = \int_{-\pi}^\pi s(\omega)$ which is the integration of the spectral density. 

The integration cut off from $-a$ to $a$ is the importance of low frequency components. 

### Sample version periodogram

$Let (X_t)$ be a weakly stationary time series with absolutely summable autocovariances. The popluation spectram 

$$
s(\omega) = \frac{1}{2\pi}\sum_{j\in\mathbb{Z}} \gamma_j e^{-i\omega j}
$$

The sample autocovaraince function:

$$
\hat{\gamma}_j =  \frac{1}{T} \sum_{t=j+1}^T (x_t- \bar{x})(x_{t-j}-\bar{x}) 
$$

sample periodogram:

$$
\hat{s}(\omega) = \frac{1}{2\pi}\left[\hat{\gamma}_0 + 2 \sum_{j=1}^{T-1} \hat\gamma_j e^{-i\omega j}\right]
$$

### spectral representation theorem ( finite sample version )

Given $x_1,\dots, x_T$, there exists frequencies $(\omega_, \dots, \omega_m)$ and random coefficients $\hat\mu, \hat\alpha_1,\dots,\hat\alpha_m, \hat\beta_1,\dots\hat\beta_m$  s,t, 

$$
x_t = \hat\mu + \sum_{j=1}^m \hat\alpha_j\cos(\omega_j(t-1)) + \sum_{j=1}^m \hat\beta_j \sin(\omega_j(t-1))
$$

where 

$$
\sum_{t=1}^T \cos(\omega_j(t-1))\sin(\omega_k(t-1)) = 0 \\
\sum_{t=1}^T \sin(\omega_j(t-1))\sin(\omega_k(t-1)) = \frac{T}{2}\delta_{jk}
$$

