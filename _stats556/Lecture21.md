---
title: Lecture 21 (March 11, 2022)
classes: wide
excerpt: "Statistical Test for The Drift Term"
date: 2022-03-11

---

Previously we found that 

$$
\begin{pmatrix} 
T^{1/2} & 0 \\
0 & T^{3/2} 
\end{pmatrix} 
\begin{pmatrix} \hat\alpha-\alpha\\ \hat\phi_1-1 \end{pmatrix} \rightarrow \begin{pmatrix}
1 & \alpha/2 \\ \alpha/2 & \alpha^2/3
\end{pmatrix}^{-1} \begin{pmatrix}\frac{1}{\sqrt{T}} \sum \epsilon_t \\ \frac{1}{T^{3/2}}\sum x_{t-1}\epsilon_t \end{pmatrix} = Q^{-1} \begin{pmatrix}\frac{1}{\sqrt{T}} \sum \epsilon_t \\ \frac{1}{T^{3/2}}\sum x_{t-1}\epsilon_t \end{pmatrix}
$$

The problem is what is the limiting distribution for the last vector. 

The term $\sum x_{t-1} \epsilon_t = \sum (t-1)\alpha\epsilon_t + \sum\xi_{t-1}\epsilon_t$ and the first term has $O(T^{3/2})$ scaling and the second term has $O(T)$ scaling because $\xi_{t-1}\sim O(\sqrt{t})$. Therefore, when we scale by $T^{-3/2}$ only the first term survives. The question then becomes the limiting distribution of 
$$
\begin{pmatrix}
\frac{1}{\sqrt{T}} \sum \epsilon_t \\ \frac{\alpha}{\sqrt{T}} \sum \frac{t}{T}\epsilon_t
\end{pmatrix}
$$

If we assume $\epsilon_t$ are iid and $\mathbb{E}[\epsilon_t] = 0$ and $\text{Var}[\epsilon_t] = \sigma^2$ and $\mathbb{E}\epsilon_t^4 < \infty$, then by central limit theorem we have 

$$
\frac{1}{\sqrt{T}}\sum \epsilon_t \rightarrow \mathcal N(0,\sigma^2)
$$

The next question is what the second component will be in the limiting case. 

**Theorem** [CLT for martingale difference sequence]:

Let $x_t$ be a Martingale difference sequence (the sequence created by martingale one lag difference $x_t = y_t -y_{t-1}$ for $y_t$ martingale) with $\bar{X}_t \equiv \frac{1}{T}\sum_{t=1}^T x_t$ , suppose that 

	1. $\mathbb{E}x_t^2 = \sigma_t^2 > 0$ s.t. $\frac{1}{T}\sum_{t=1}^T \sigma_t^2 \rightarrow \sigma^2 >0$ 
	2. $\mathbb{E}|x_t|^r <\infty$ for some $r>2$ and for all $t$
	3. $\frac{1}{T}\sum_{t=1}^Tx_t^2 \rightarrow \sigma^2$ 

Then $\sqrt{T}\bar{X}_T \rightarrow \mathcal{N}(0,\sigma^2)$. 

Note that $t/T\epsilon_t$ is an MD sequence (because $E[t/T\epsilon_t | \mathcal{F}_{t-1}] =0$ and $\mathbb{E}[t/T \epsilon_t] <\infty$ ) also the condition that \

$$
\mathbb{E}\left(\frac{t}{T}\epsilon_t\right)^2 = \frac{t^2}{T^2}\sigma^2 \quad \text{ and \quad} \frac{1}{T}\sum_{t=1}^T \frac{t^2}{T^2}\sigma^2 \rightarrow \frac{\sigma^2}{3}
$$

the second condition is trivial and we want to check the third condition to show that 

$$
\frac{1}{T}\sum_{t=1}^T \frac{t^2}{T^2}\epsilon_t^2 \rightarrow \frac{\sigma^2}{3}
$$

we can do the check: we first find that the expectation is the desired limit and we need to show the variance vanishes: 

$$
\mathbb{E}\left(\frac{1}{T}\sum_{t=1}^T \frac{t^2}{T^2}\epsilon_t^2 - \frac{1}{T}\sum_{t=1}^T \frac{t^2}{T^2}\sigma^2 \right)^2 = \mathbb{E}\frac{1}{T^2}\left[ \sum_{t=1}^T \frac{t^2}{T^2}(\epsilon_t^2-\sigma^2)\right]^2 = O(\frac{1}{T}) \rightarrow 0
$$

and thus the third condition is checked. This shows that 

$$
\frac{\alpha}{\sqrt{T}} \sum_{t=1}^T \frac{t}{T}\epsilon_t \rightarrow \mathcal{N}(0, \alpha^2\sigma^2/3)
$$

However, here we find that the final limiting distribution for the error term depends on linear combinations of $\epsilon_t$ and $\sum t/T\epsilon_t$ we thus want to find that the limiting behaviour of 

$$
\frac{1}{\sqrt{T}} \sum_{t=1}^T \epsilon_t(\lambda_1 + \lambda_2 \frac{\alpha t}{T})
$$

for some coefficient $\lambda_1, \lambda_2$. Using similar argument as above, we find that 

$$
\frac{1}{\sqrt{T}} \sum_{t=1}^T \epsilon_t (\lambda_1+\lambda_2 \frac{\alpha t}{T}) \rightarrow \mathcal{N}(0, \sigma^2 \lambda^T Q\lambda)
$$

with $\lambda = (\lambda_1,\lambda_2)^T$ and 

$$
Q = \begin{pmatrix} 1 & \frac{\alpha}{2} \\ \frac{\alpha}{2} & \frac{\alpha^2}{3} \end{pmatrix}
$$

and as a result : 

$$
\begin{pmatrix}\sqrt{T}(\hat\alpha - \alpha) \\ T^{3/2} (\hat\phi_1 - 1) \end{pmatrix} \rightarrow \mathcal{N}(0, \sigma^2 Q^{-1})
$$
