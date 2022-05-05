---
title: Lecture 25 (March 28, 2022)
classes: wide
excerpt: "Application of Ito's Lemma: Derivation of Black-Scholes Formula"
date: 2022-03-28

---

Diffusion process

$$
dx_t = \mu(x_t,t) dt + \sigma(x_t,t) dw_t
$$

with $w_0 = 0$ or 

$$
x_t = \int_0^t \mu(x_s,s) ds + \int_0^t \sigma(x_s,s) dw_s
$$

and the if $G(x,t)$ is twice differentiable, we have 

$$
dG(x_t,t) = \left(\frac{dG}{dx} \mu + \frac{dG}{dt} + \frac{1}{2}\frac{d^2G}{dx^2} \sigma^2\right)dt + \frac{dG}{dx} \sigma dw_t
$$

geometric BM:

$$
d p_t = \mu p_t dt + \sigma p_t dw_t \quad d\log p_t = (\mu-\frac{\sigma^2}{2}) dt + \sigma dw_t
$$

with $\mu,\sigma$ as constants. 

### Black Scholes Formula

Suppose that the stock price follows a geometric BM

$$
dP_t = P_t \mu dt + P_t\sigma dt
$$

with $\mu,\sigma$ as constants, we want to determine the price of a derivative contingent to a stock valued at $P_t$, in a risk-free in a short time. $G_t = G(P_t, t)$ is the price of the derivative. 

Ito's Lemma says 

$$
dG_t = \left(\frac{\partial G_t}{\partial P_t} \mu P_t + \frac{\partial G_t}{\partial t} + \frac{1}{2} \frac{\partial^2 G_t}{\partial P_t^2}\sigma^2 P_t^2  \right)dt + \frac{\partial G_t}{\partial P_t}\sigma P_t dw_t
$$

Make a portfolio of the stock and the derivative cancel out the stochastic components. $(W_t)$. Let $V_t$ be the value of this portfolio: 

$$
V_t = -G_t + \Pi P_t
$$

where $\Pi$ is the share of stocks in the portfolio. This means, we pay for $G_t$ for the portfolio and get the value from the stocks. This gives that 

$$
\begin{aligned}
dV_t &= -dG_t + \Pi dP_t\\
&= -\left( \frac{\partial G_t}{\partial P_t}\mu P_t + \frac{\partial G_t}{\partial t} + \frac{1}{2}\frac{\partial^2 G_t}{\partial P_t^2}\sigma^2P_t^2 \right) dt - \frac{\partial G_t}{\partial P_t}\sigma P_t dw_t + \Pi P_t \mu dt + \Pi P_t\sigma dw_t \\
&= -\left( \frac{\partial G_t}{\partial P_t}\mu P_t + \frac{\partial G_t}{\partial t} + \frac{1}{2}\frac{\partial^2 G_t}{\partial P_t^2}\sigma^2P_t^2  - \Pi P_t \mu\right) dt + \left( \Pi P_t \sigma - \frac{\partial G_t}{\partial P_t}\sigma P_t\right)dw_t
\end{aligned}
$$

If this portfolio is the risk free, we need the randomness to chancel, which means that 

$$
\Pi = \frac{\partial G_t}{\partial P_t}
$$

which gives 

$$
dV_t = - \left(\frac{\partial G_t}{\partial t} + \frac{1}{2}\frac{\partial^2 G_t}{\partial P_t^2}\sigma^2 P_t^2 \right) dt
$$

Also, the portfolio must simultaneously earn the same rate of return as other short-term risk free securites 

$$
\frac{dV_t}{dt} = \gamma V_t = \gamma(-G_t + \frac{\partial G_t}{\partial P_t} P_t)
$$

Combining together we have 

$$
\frac{\partial G_t}{\partial P_t} + \frac{1}{2} \frac{\partial^2 G_t}{\partial P_t^2}\sigma^2 P_t + \gamma \frac{\partial G_t}{\partial P_t} P_t = \gamma G_t
$$

and this is the Black scholes equation for derivative pricing. with $G_t = G(P_t, t)$.  We could then solve the BS equation with input $\gamma, P_t$, to obtain the derivative price $G_t$. 


