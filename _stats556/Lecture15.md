---
title: Lecture 15 (Feb 25, 2022)
classes: wide
excerpt: "Estimation of ARCH Model with method of moments"
date: 2022-02-25

---

### Generalized method of moments (GMM)

Recall: $x_t = m_t^T \phi + r_t $ with the previous definition of the symbols. The residuals are $x_t- m_t^T\phi$ and $m_t$ has no correlation:

$$
\begin{aligned}
\mathbb{E}[(x_t-m_t^T\phi)m_t] &= \mathbb{E}[\mathbb{E}[(x_t-m_t^T\phi)m_t|\mathcal{F}_{t-1}]]\\
&=\mathbb{E}[m_t \mathbb{E}[\sigma_t\epsilon_t|\mathcal{F}_{t-1}]] \\
&=\mathbb{E}[m_t\sigma_t\mathbb{E}[\epsilon_t|\mathcal{F}_{t-1}]] = 0
\end{aligned}
$$

The correlation of the errors of the second moments with the series:

$$
\begin{aligned}
\mathbb{E}[(r_t^2-\sigma_t^2)z_t(\phi)] &= \mathbb{E}[\mathbb{E}[(r_t^2-\sigma_t^2)z_t(\phi)|\mathcal{F}_{t-1}]] \\
&= \mathbb{E} [\sigma_t^2 z_t(\phi) \mathbb{E}[\epsilon_t^2-1]]\\
&= 0 
\end{aligned}
$$

Thus, we have two constraints. The GMM method replaces the above expectation constraints by the samples. 

$$
\begin{aligned}
&\frac{1}{T}\sum_{t=1}^T (x_t - m_t^T\phi) m_t = 0 \\
&\frac{1}{T}\sum_{t=1}^T \left((x_t-m_t^T\phi)^2 - z_t(\phi)^T \alpha\right)z_t(\phi) = 0
\end{aligned}
$$

Methods of moments:

$$
\min_{\alpha,\phi} \left\| \frac{1}{T}\sum_{t=1}^T (x_t-m_t^T\phi) m_t \right\|^2 + \left\| \frac{1}{T}\sum_{t=1}^T \left((x_t-m_t^T\phi)^2- z_t(\phi)^T\alpha \right) z_t(\phi)\right\|^2
$$

There are some correlations between the first part and the second part and we thus diagonlaize the quadratic form for the two parts. and we get 

$$
\min_{\phi,\alpha} g(\phi,\alpha)^T \hat{S}_T^{-1} g(\phi,\alpha)
$$

where $S_T$ is the square root matrix of the estimated covariance of the two equations from the methods of moments. 

with 

$$
g(\phi,\alpha) = \begin{pmatrix} 
\frac{1}{T}\sum_{t=1}^T(x_t-m_t^T\phi)m_t \\
\frac{1}{T}\sum_{t=1}^T((x_t-m_t^T\phi)^2-z_t(\phi)^T\alpha)z_t(\phi)
\end{pmatrix}
$$
 
 $g(\phi,\alpha)$ is a $k+p+2$ vector 


