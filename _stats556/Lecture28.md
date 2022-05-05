---
title: Lecture 28 (April 04, 2022)
classes: wide
excerpt: "Introduction to Vector Autoregressive (VAR) model"
date: 2022-04-04

---

### Vector Autoregressive (VAR) model

The VAR($1$) model:

$$
x_t = \phi_0 + \Phi x_{t-1} + \epsilon_t
$$

Assume that $x_t$ is weakly stationary

$$
\mu = E x_t \quad \Rightarrow \mu = \phi_0 + \Phi \mu \quad \Rightarrow \quad \mu = (I-\Phi)^{-1} \phi_0
$$

Let $\tilde{x}_t = x_t-\mu$. 

$$
\tilde{x}_t = \Phi \tilde{x}_{t-1} + \epsilon_t = \dots = \epsilon_t + \Phi \epsilon_{t-1} + \Phi^2 \epsilon_{t-2} + \dots 
$$

Let $\Sigma = \text{Cov}(\epsilon_t)$. The covariance of $\tilde{x}_t$ is 

$$
\Gamma_0 = \text{Cov}(\epsilon_t + \Phi \epsilon_{t-1} + \Phi^2 \epsilon_{t-2} + \dots) = \sum_{l=0}^\infty \Phi^l \Sigma(\Phi^l)^T
$$

Also

$$
\Gamma_l = \text{Cov}[x_t, x_{t-l}] = \text{Cov}[ \Phi x_{t-1} + \epsilon_t, x_{t-l}]= \Phi \Gamma_{l-1}
$$

which implies that 

$$
\Gamma_l =\Phi^l \Gamma_0
$$

If $\|\Phi \| < 1$ then $\|\Gamma_l\|\leq  \|\Phi\|^l \|\Gamma_0\| \rightarrow 0$. 

Recall when $k=1$, $|\phi|<1$ implies weakly stationary of $(x_t)$. when $k>1$, the absolute value of all egienvalues of $\Phi$ less than $1$ will give weakly stationary of $x_t$. The eigen value of $\Phi$ will be 

$$
\det(\lambda I_k - \Phi) = \lambda^k \det (I_k - \frac{1}{\lambda} \Phi)
$$

This shows the eigenvalue $\lambda$ of $\Phi$, is just the inverse of zeros of the polynomial $\det(I_k-\Phi B)$. Thus, we need the root of the poly nomial to be $>1$. 

Remark: $VAR(p)$ model can be recasted to $VAR(1)$ model by augmenting space. For example 

$$
x_t = \Phi x_{t-1} + \dots  + \Phi_p x_{t-p} + \epsilon_t
$$

Let $y_t = (x_{t-p+1}, x_{t-p+2},\dots, x_t)$ and $\eta_t = (0,\dots, 0, \epsilon_t)$ , Then we have 

$$
\begin{pmatrix}
x_{t-p+1} \\ x_{t-p+2} \\ \vdots \\ x_t
\end{pmatrix} 
=\begin{pmatrix}
0 & I_k &\dots &0 \\ \vdots & \vdots  & \ddots & \vdots \\
0 & 0 & \dots & I_k \\
\Phi_p & \Phi_{p-1} &\dots & \Phi_1 
\end{pmatrix} 
\begin{pmatrix}
x_{t-p} \\ x_{t-p+1} \\ \vdots \\ x_{t-1} 
\end{pmatrix} + \begin{pmatrix} 0 \\ 0 \\ \vdots \\ \epsilon_t \end{pmatrix}
$$

This is just 

$$
y_t = \Phi^* y_{t-1} + \eta_t
$$

Then the polynomial 

$$
\det(I_{pk} - \Phi^* B) = 0 \Leftrightarrow \det(I_k- \Phi_1 B - \dots -\Phi_p B^p) = 0
$$

momentum equation: 

$$
\rho_l = \Lambda_1 \rho_{l-1} + \cdots + \Lambda_p \rho_{l-p}  
$$

Where $\Lambda_i = D^{-1/2} \Phi_i D^{1/2}$. 

 
