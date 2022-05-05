---
title: Lecture 24 (March 25, 2022)
classes: wide
excerpt: "Introduction to Ito's Process and Ito's Lemma"
date: 2022-03-25

---

### Ito process as a stochastic differential equation

Recall that the Ito's process is 

$$
dx_t = \mu(x_t,t) dt + \sigma(x_t,t)dw_t
$$

where $w_t$ is the standard BM with $w_0 = 0$ . If $G(x,t)$ is twice differentiable 

Ito formula:

$$
dG(x_t,t) = \left(\frac{\partial G}{\partial x}\mu + \frac{\partial G}{\partial t} + \frac{1}{2}\frac{\partial^2 G}{\partial x^2}\sigma^2\right)dt + \sigma\frac{\partial G}{\partial x} dw_t
$$

For example: 

$$
dx_t = \mu dt + \sigma dw_t
$$

If $y_t = G(x,t) = x_t^2$, then 

$$
\frac{\partial G}{\partial x} = 2x \quad \frac{\partial^2 G}{\partial x^2} = 2 \quad \frac{\partial G}{\partial t} = 0
$$

This leads to that 

$$
\begin{aligned}
dy_t &= (2x_t \mu + \frac{1}{2}\times 2\sigma^2) dt + 2x_t\sigma dw_t \\
&=(2x_t\mu + \sigma^2)dt + 2x_t\sigma dw_t
\end{aligned}
$$

Another example If $\mu = 0$ and $\sigma = 1$, then $dx_t = dw_t$. This leads to that 

$$
dw_t^2 = dt + 2 w_t  dw_t
$$

The term $dt$ which should not appear in classical differential calculus, is from the quadratic variation of $w_t$. 

Another example: Geometric Brownian motion. Consider stock price at time $t$, it satisfies that 

$$
dP_t = \mu P_t dt + \sigma P_t dt 
$$

As an Ito process, $\mu(P_t, t) = \mu P_t$ and $\sigma(P_t,t) = \sigma P_t$. We can get the formula for log prices $\log P_t$. Let $G(x,t) = \log(x)$, then 

$$
\frac{\partial G}{\partial x} = \frac{1}{x}\quad \frac{\partial^2 G}{\partial x^2} = -\frac{1}{x^2} \quad \frac{\partial G}{\partial t} = 0
$$

This leads to that 

$$
d\log P_t = \left( \mu - \frac{\sigma^2}{2}\right) dt + \sigma dw_t
$$

Summary: If the price is a geometric BM, then the log price follows a generalized BM with drift $\mu-\sigma^2/2$ and volatility $\sigma$. 

This shows that the change of log-prices 

$$
\log P_{t_2} - \log P_{t_1} \sim \mathcal{N} \left( (\mu-\frac{\sigma^2}{2})(t_2-t_1), \sigma^2 (t_2-t_1) \right)
$$

If we have data $p_0, p_1,\dots p_n$ at equally spaced time interval $\Delta$, we want to estimate $\mu$ and $\sigma$. Note first that the log return follows the distribution

$$
r_t = \log P_t - \log P_{t-1} \sim \mathcal{N}((\mu-\sigma^2/2)\Delta, \sigma^2\Delta)
$$

then we let 

$$
\bar{r}_n = \frac{1}{n}\sum_{t=1}^n r_t \quad s_n = \sqrt{\frac{1}{n-1}\sum_{i=1}^n (r_t-\bar{r}_n)^2}
$$

By law of large numbers 

$$
\bar{r}_n \rightarrow \mathbb{E}[r_t] = (\mu -\frac{\sigma^2}{2})\Delta \quad s_n \rightarrow \sqrt{\text{Var}(r_t)} = \sigma\sqrt{\Delta}
$$

method of moments: 

$$
\hat{\sigma} = \frac{s_n}{\sqrt{\Delta}}, \quad \hat\mu = \frac{\bar{r}_n}{\Delta} + \frac{\hat{\sigma}^2}{2} = \frac{\bar{r}_n}{\Delta} + \frac{s_n^2}{2\Delta}
$$

**Def [log-normed distribution]** $X$ is log-normed distribution if $Y = \log(X)$ follows a normed distribution. 

If $Y\sim \mathcal{N}(\mu,\sigma^2)$, then $X\sim \text{log-normed} (\mu,\sigma^2)$ s.t. 

$$
\mathbb{E} X = \exp (\mu + \sigma^2/2) \quad \text{Var}(X) = \exp(2\mu+\sigma^2)[\exp(\sigma^2)-1]
$$

$t_1 < t_2$, then 

$$
p_{t_2}/p_{t_1} \sim \text{log-normal} \left((\mu-\frac{\sigma^2}{2})(t_2-t_1), \sigma^2(t_2-t_1) \right) 
$$

Then 

$$
\mathbb{E}\left[\frac{P_{t_2}}{P_{t_1}}\right] = \exp \left[(\mu-\frac{\sigma^2}{2})(t_2-t_1) + \frac{\sigma^2(t_2-t_1)}{2} \right] = \exp(\mu(t_2-t_1))
$$

$$
\text{Var}\left(\frac{P_{t_2}}{P_{t_1}}\right) = \exp\left[ 2\mu(t_2-t_1) \right]\left\{ \sigma^2(t_2-t_1) -1 \right\}
$$

This shows that 

$$
\mathbb{E}[P_{t_2}|P_{t_1}] = P_{t_1} \mathbb{E} \left[\frac{P_{t_2}}{P_{t_1}} \right] = P_{t_1}\exp(\mu(t_2-t_1))
$$

and 

$$
\text{Var}[P_{t_2}|P_{t_1}] = P_{t_1}^2 \text{Var}\left(\frac{P_{t_2}}{P_{t_1}} \right) = P_{t_1}^2\exp(2\mu(t_2-t_1))\left\{\exp(\sigma^2(t_2-t_1)) - 1\right\}
$$

Summary:

$$
\begin{aligned}
&dP_t = \mu P_t dt + \sigma P_t dw_t \\
&d\log P_t = (\mu-\frac{\sigma^2}{2}) dt + \sigma dw_t
\end{aligned}
$$

This shows that 

$$
\log P_t - \log P_0 = (\mu-\frac{\sigma^2}{2})t + \sigma(w_t - w_0)
$$

which gives 

$$
P_t = P_0 \exp \left( (\mu-\frac{\sigma^2}{2})t + \sigma w_t\right)
$$

