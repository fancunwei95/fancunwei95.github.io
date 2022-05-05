---
title: Lecture 22 (March 21, 2022)
classes: wide
excerpt: "Continuous Time Model"
date: 2022-03-21

---

### Continuous time models

Let $(\Omega, \mathcal{F}, P)$ be a probability space and $\Omega$ is the sample space and $\mathcal{F}$ is some sigma fields on $\Omega$ and $P$ is a measure for this sigmal field. A random variable $X$ is a measurable function $X:\Omega \rightarrow \mathbb{R}$. 

Stochastic process: $X(\omega, t)$ with $\omega\in\Omega$ for $t \in I$ for some index sets $I$. Given a fixed $t$. $X(\cdot, t)$ is a random variable   

**Def [Brownian Motion]**

A standard Brownian motion $(W_t)_{t\geq 0}$ on a probability space $(\Omega, \mathcal{F},P)$ is the real valued continuous time stochastic process:

1. $t\rightarrow W_t$ with $W_t$ as a continuous function with probability $1$.
2. If $s\leq t$, $W_t-W_s$ is independent of $(W_v)_{v\leq s}$. 
3. If $s\leq t$, $W_t-W_s \sim W_{t-s}-W_0\sim \mathcal{N}(0,t-s)$. 

Komogorov construction shows that Brownian motion actually exists. 

If we define $\Delta W_t = W_{t+\Delta t} - W_t$ , then the above definition shows that $\Delta W_t$ is independent of $(W_v)_{v\leq t}$ and $\Delta W_t\sim \epsilon \sqrt{\Delta t}$. with $\epsilon$ as the standard normal. 

We can write $W_t - W_0$ as the increament of discrete intervals

$$
W_t - W_0 = \sum_{i=1}^n W_{i\Delta t} - W_{(i-1)\Delta t}
$$

with $n=t/\Delta t$. and because each increament is independent, we find that $W_t - W_0 \sim \mathcal{N}(0, n\Delta t) = \mathcal{N}(0,t)$.   

**Simulation of Brownian Motion**

We would use the Donsker/functional CLT theorem. 

**Theorem [Donsker]**

Let $(z_i)_{i=1}^n$ be iid $N(0,1)$.  Let $[nt]$ be the integer part of $nt$ with $t\in[0,1]$. Then 

$$
\left(\frac{1}{\sqrt{n}}\sum_{i=1}^{[nt]} z_i\right)_{t\in[0,1]} \rightarrow (W_t)_{t\in[0,1]}
$$

as $n\rightarrow \infty$. and this convergence is for the functional. 

Remark: The Brownian motion is continuous but it is not differentiable everywhere. 

