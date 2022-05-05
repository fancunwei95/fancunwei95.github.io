---
title: Lecture 23 (March 23, 2022)
classes: wide
excerpt: "Introduction to Ito's Process and Ito's Lemma"
date: 2022-03-23

---

### Ito's Process (diffusion process)

Stochastic process $(x_t)$ real valued 

$$
dx_t = \mu(x_t,t) dt + \sigma(x_t,t)dw_t
$$

where $\mu : \mathbb{R} \times \mathbb{R}_+ \rightarrow \mathbb{R}$. as the drift and $\sigma:\mathbb{R}\times\mathbb{R}_+ \rightarrow \mathbb{R}$ volatility function. and $w_t$ is the standard Brownian motion with $w_0 = 0$. 

example: $\mu = 0, \sigma=1$, we have $x_t = w_t$ , which is the Brownian motion. 

when $\sigma = 0$< we have $dx_t = \mu(x_t,t)dt$ and this is the deterministic function $\dot{x}_t = \mu(x_t,t)$. 

when $\mu$ and $\sigma$ are constants, then $dx_t = \mu dt + \sigma dw_t$, is the generalized Brownian motion. the solution will be 

$$
x_t = x_0 + \mu t + \sigma\sqrt{t}\epsilon
$$

for $\epsilon \sim \mathcal{N}(0,1)$. 

Motivation: If the asset price is an Ito process, then we would like to calculate the price of a financial derivative. 

### Ito's Lemma:

$G(x)$ is differentiable in $x$, then 

$$
\Delta G = G(x+ \Delta x) - G(x) = \frac{d}{dx} G(x)\Delta x + \frac{1}{2}\frac{d^2}{dx^2} G(x) (\Delta x)^2 + \dots 
$$

take $\Delta x \rightarrow 0$ , $dG = \frac{d}{dx} G(x) dx$. 

$G(x,y)$ is differentiable in $(x,y)$, 

$$
\begin{aligned}
\Delta G &= G(x+\Delta x, y +\Delta y) - G(x,y) \\
&=\frac{\partial G}{\partial x}  \Delta x + \frac{\partial G}{\partial y} \Delta y + \frac{1}{2} \frac{\partial^2 G}{\partial x^2} (\Delta x)^2  +  \frac{1}{2}\frac{\partial^2 G}{\partial y^2} (\Delta y)^2 + \frac{\partial^2 G}{\partial x \partial y} (\Delta x)(\Delta y) + \cdots 
\end{aligned}
$$

take $\Delta x \rightarrow 0$ and $\Delta y \rightarrow 0$, 

$$
dG = \frac{\partial G}{\partial x} \cdot dx + \frac{\partial G}{\partial y} \cdot dy 
$$

Think $x = x_t$ (Ito process) and $y=t$ (time). Then $G(x_t, t)$ can be treated as the values of the financial derivatitives. Then we have 

$$
\Delta G(x,t) = \frac{\partial G}{\partial x}\Delta x + \frac{\partial G}{\partial t}\Delta t + \frac{1}{2}\frac{\partial^2 G}{\partial x^2} (\Delta x)^2 + \frac{1}{2} \frac{\partial^2 G}{\partial t^2}(\Delta t)^2 + \frac{\partial^2 G}{\partial x\partial t} (\Delta x)(\Delta t) + \cdots 
$$

roughly speaking, $(\Delta x)^2 \sim \Delta t$. This is because: 

$$
\begin{aligned}
&\Delta x = \mu \Delta t + \sigma\epsilon \sqrt{\Delta t} \\
&(\Delta x)^2 = \mu^2 (\Delta t)^2 + \sigma^2\epsilon^2 \Delta t + 2\mu \sigma \epsilon (\Delta t)^{3/2}
\end{aligned}
$$

Thus, for Ito's process, $(\Delta x)^2 \sim \sigma^2 \Delta t \epsilon^2$. and thus, 

$$
\mathbb{E}[(\Delta x)^2] \rightarrow  \sigma^2 d t \quad \text{ as } \Delta t \rightarrow 0
$$

This leads to that as $dt\rightarrow 0$, 

$$
\begin{aligned}
d G (x,t) &= \frac{\partial G}{\partial x} dx_t + \frac{\partial G}{\partial t} dt + \frac{1}{2} \frac{\partial^2 G}{\partial x^2} \sigma^2 dt  \\
&= \frac{\partial G}{\partial x}(\mu dt + \sigma dw_t) + \frac{\partial G}{\partial t} dt + \frac{1}{2}\frac{\partial^2 G}{\partial x^2} \sigma^2dt \\
&= \left(\frac{\partial G}{\partial x} \mu + \frac{\partial G}{\partial t} + \frac{1}{2}\frac{\partial^2 G}{\partial x^2}\sigma^2\right) dt + \sigma \frac{\partial G}{\partial x} dw_t
\end{aligned}
$$

**Theorem [Ito Lemma]** Let $G(x,t)$ be a differentiable in $x,t$,If $x_t$ is an Ito process s.t. 

$$
dx_t = \mu(x_t,t) dt + \sigma(x_t,t)dw_t
$$

where $w_t$ is the standard Brownian motion with $w_0 =0$. Then 

$$
dG(x_t, t) = \left[\mu \frac{\partial G}{\partial x} + \frac{\partial G}{\partial t} + \frac{1}{2}\frac{\partial^2 G}{\partial x^2} \sigma^2  \right] dt + \sigma \frac{\partial G}{\partial x} dw_t
$$


