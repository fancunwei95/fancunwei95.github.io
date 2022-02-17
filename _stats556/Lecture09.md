---
title: Lecture 09 (Feb 11, 2022)
classes: wide
excerpt: "Introduction of Karhunen-Leove theorem, the spectral theorem and autocovariance generating function"
date: 2022-02-07

---


$ARMA(p,q)$, $\phi(B) x_t = \phi_0 + \theta(B)\epsilon_t$.  Define $\pi(B) = \frac{\phi(B)}{\theta(B)}$ and the AR representation is 

$$
\pi(B) x_t = \frac{\phi_0}{\theta(B)} + \epsilon_t
$$

and the MA model becomes 

$$
x_t = \frac{\phi_0}{\phi(B)} + \psi(B) \epsilon_t
$$

Time domain representation: 

$$
x_t = \mu + \sum_{j=0}^\infty \psi_j \epsilon_{t-j}
$$

$\epsilon_t$ iid mean-zero and $\text{var}(\epsilon_t) = \sigma^2$

**Karhunen-Loeve theorem:**

For any mean-zero, weakly stationary $x_t$, $t\in[a,b]$ , $x_t$ can be representated by 

$$
x_t = \sum_{k=1}^\infty z_k e_k(t)
$$

$\mathbb{E}z_k = 0 $ and $\mathbb{E}z_iz_j = \lambda_j \delta_{ij}$ ($z_i$ are uncorrelated). Here, $e_k(t)_{k=1}^\infty$ continuous function on $[a,b]$, orthogonal in $L^2([a,b])$ , i.e.

$$
\int_a^b e_k(t)e_j(t) dt = \delta_{kj}
$$


The orthogonality of $e_k$ shows that 

$$
\int_a^b x_t e_j(t) dt = \int_a^b \sum_{k=1}^\infty  z_k e_k(t) e_j(t) dt = \sum_{k=1}^\infty z_k\delta_{kj} = z_j
$$

Now we consider the representation 

$$
x_t = \phi_0 + \int_0^\pi \alpha(\omega) \cos(\omega t) d\omega + \int_0^\pi \beta(\omega) \sin(\omega t) d\omega 
$$

This is the spectral frequency domain. With the property that 

$$\alpha (\omega)\vert_{\omega_1}^{\omega_2}$$ 

and 

$$\alpha (\omega)\vert_{\omega_3}^{\omega_4}$$ 

are uncorrelated when $\omega_1\leq \omega_2 \leq \omega_3\leq \omega_4 $. 

Define **autocovariance generating function (ACGF)** 

$$
g(z) = g_x(z) = \sum_{j=\infty}^\infty \gamma_j z^j
$$

where $\gamma_j = \text{Cov}(x_t,x_{t-j})$ for $(x_t)$ weakly stationary. The spectral, 

$$
\begin{aligned}
s(\omega) &= \frac{1}{2\pi} g(e^{-i\omega})= \frac{1}{2\pi} \sum_{j\in\mathbb{Z}} \gamma_j e^{-i\omega j} \\
&= \frac{1}{2\pi} \sum_j \gamma_j[\cos(\omega j) - i\sin(\omega j)] \\
&= \frac{1}{2\pi} \left[\gamma_0 + 2\sum_{j=1}^\infty \gamma_j \cos(\omega j)\right]
\end{aligned}
$$

where we used the fact that $\gamma_j$ is an even function of $j$ while $\sin(\omega j)$ is odd. 

Properties: If  $ \sum_{j\in\mathbb{Z}} \vert\gamma_j \vert < \infty $

1. the $s(\omega)$ exists 
2. $s(\omega)$ is continuous and differentiable in $\omega$. 
3. $s(-\omega) = s(\omega)$ symmetric around zero
4. $s(\omega + 2\pi k) = s(\omega)$ for $\forall k \in \mathbb{Z}$. 

Thus, we could only need to consider the $s(\omega)$ for $\omega \in [0, \pi]$. 

Back to $MA(\infty)$ representation $(\mu = 0)$ 

$$
x_t = \sum_{j=0}^\infty \psi_j \epsilon_{t-j}
$$

Assume $\sum_{j=0}^\infty \vert \psi_j \vert <\infty$ and $\text{Var}(\epsilon_t) = \sigma^2$ , 

$$
g(z) = \sigma^2 \psi(z) \psi(z^{-1}) 
$$

Then 

$$
s(\omega) = \frac{1}{2\pi} g(e^{-i\omega}) = \frac{\sigma^2}{2\pi} \psi(e^{-i\omega}) \psi(e^{i\omega}) 
$$

If $\psi_0 = 1$ and $\psi_1=\psi_2 = \dots = 0 $ , we have 

$$
\psi(z) = 1 - \psi_1(z) - \psi_2(z) - \dots = 1 \quad \Rightarrow s(\omega) = \frac{\sigma^2}{2\pi}
$$

Thus this is called the white noise. 

If $\psi_0 = 1$ and $\psi_i = 0$ for $i\geq 2$. Then 

$$
\begin{aligned}
s(\omega) &= \frac{\sigma^2}{2\pi} (1-\psi_1 e^{-i\omega}) ( 1 - \psi_1 e^{i\omega})
&= \frac{\sigma^2}{2\pi} (1+2\cos(\omega) \psi_1 + \psi_1^2)
\end{aligned}
$$
