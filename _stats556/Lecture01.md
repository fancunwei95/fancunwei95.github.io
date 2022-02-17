---
title: Lecture 01 (Jan 21, 2022)
classes: wide
excerpt: "First Lecture: Intorduction of autocorrleation for linear time series"
date: 2022-01-21

---


### Autocorrelation

Let $(x_t)_{t=1}^T$ be a sequence of random variables. We calssify the sequence as:

- **strict stationarity** : for any fixed $k\geq 1$ and $t_1,\dots, t_k$ collection of positive integer, $(x_{t_1}, \dots, x_{t_k})$ has the same distributin of $(x_{t_1+l}, \dots, x_{t_k+l})$  for all $l\in \mathbb{Z}$.
- __weak stationarity__ :
  1. $\mathbb{E}(x_t) = \mu$ constant
  2. $\text{Cov}(x_t, x_{t-l}) = \gamma_l$ for $l\in\mathbb{Z}$. (This is called lag-l auto-covariance of $x_t$)

properties of $\gamma_l$ for weak stationary $x_t$ :

1. $\gamma_0 = \text{Cov}(x_t, x_t) = \text{Var}(x_t)$
2. $\gamma_{-l} = \text{Cov}(x_t, x_{t+l}) = \text{Cov}(x_{t-l}, x_t) = \gamma_l$.  

__Def__ the correlation coefficient between $x_t$ and $x_{t-l}$ for a weakly stationary time series $\{x_t\}$ is called the lag-l autocorrelation of $x_t$ (ACF), denoted by $\rho_l$:

$$
\rho_l = \frac{\text{Cov}(x_t, x_{t-l})}{\sqrt{\text{Var}(x_t)}\sqrt{\text{Var}(x_{t-l})}} = \frac{\gamma_l}{\gamma_0}
$$

properties of $\rho_l$ :

1. $\rho_0 = 1$
2. $\rho_{-l} = \rho_l$. 
3. $-1\leq \rho_l \leq 1 $. (by correlation property which implied by Cauchy-Swartz)
4. $\rho_l = 0, \forall l\geq 1$ is equivalent to $x_t$ is not serielly correlated. 

__Def__ __[lag-$l$ sample auto-correlation]__ :

$$
\hat{\rho}_l = \frac{\sum_{t=l+1}^T(x_t-\bar{x})(x_{t-l}-\bar{x})}{\sum_{t=1}^T(x_t-\bar{x})} \\\text{ where } \bar{x} = \frac{1}{T} \sum_{t=1}^T x_t \quad 0\leq l\leq T-1
$$

__Remark__: the numerator should be $1/(T-l)$ but when $l\ll T$, we will neglect the $-l $ and use $1/T$ directly and the $1/T$ cancles up and down and the $\hat{\rho}_l$ becomes what it is here. 

__Def__ __[m-dependent sequence]__ A sequnce of random variables $y_1, y_2,\dots $ is m-dependent if for $\forall s \geq l$ and $s\in \mathbb{Z}$, $\{y_1,\dots, y_s\}$ is independent of  $\{y_{m+s+1}, y_{m+s+2},\dots\}$ . 

Example: $x_1,x_2,\dots $ independent sequence, define $y_i = x_i x_{i+m}$  $\frac{1}{n} \sum_{i=1}^n y_i = \frac{1}{n}\sum_{i=1}^n x_i x_{i+m}$ is the auto product moment at lag-m. Here $y_i$ is an m-dependent sequence. 

Suppose $y_1,y_2,\dots $ is a staitonary sequence, i.e. $\mu=\mathbb{E}y_1$ and $\gamma_0 = \text{Var}(y_1)$ and $\gamma_l = \text{Cov}(y_1, y_{1+l})$ . If in addition, $y_t$ is m-dependent, then $\gamma_i = 0$ for $\forall i > m$. Let $S_n =\sum_{i=1}^n y_i$. Then $\mathbb{E}[S_n] = \sum_{i=1}^n \mathbb{E}[y_i] = n\mu $.  


$$
\begin{aligned}
\text{Var}(S_n) &= \text{Cov} \left(\sum_{i=1}^n y_i, \sum_{j=1}^n y_j \right) \\
&= \sum_{i=1}^n \sum_{j=1}^n \text{Cov} (y_i, y_j) \\
&= \sum_{i=1}^n\sum_{j=1}^n \gamma_{i-j} \\
&= n \gamma_0 + 2(n-1) \gamma_1 + 2(n-2)\gamma_2+\dots + 2 (n-m) \gamma_m + \dots + 2\gamma_n \\
&= n \gamma_0 + 2(n-1)\gamma_1+ 2(n-2)\gamma_2 +\dots +2 (n-m) \gamma_m \\
&= n\gamma_0 + 2 \sum_{i=1}^m (n-i) \gamma_i
\end{aligned}
$$

where we used $\gamma_i = \gamma_{-i}$.  Then

$$
\frac{1}{n} \text{Var}(S_n) = \gamma_0 + 2 \sum_{i=1}^m \left(1-\frac{i}{n}\right)\gamma_i
$$
If $m$ ix fixed , then as $n\rightarrow \infty$ , 
$$
\frac{\text{Var}(S_n)}{n} \rightarrow \gamma_0 + 2 \sum_{i=1}^m \gamma_i = \sum_{i=-m}^m \gamma_i
$$

**Theorem** __[CLT for m-dependent sequence]__ Let $y_1,y_2,\dots $ be stationary $m$-dpendent sequence with finite variance and $S_n = \sum_{i=1}^n y_i$. Then 

$$
\sqrt{n} \left(\frac{S_n}{n} - \mu\right) \rightarrow \mathcal{N}(0,\tau^2)
$$
 as $n\rightarrow \infty$ where 

$$
\tau^2 = \sum_{i=-m}^m \gamma_i = \gamma_0 + 2\sum_{i=1}^m \gamma_i \quad \mu = \mathbb{E}[y_1]
$$




