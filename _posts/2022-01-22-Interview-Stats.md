---
title: Interesting Statsitcal Problems in Interviews
category: tech
classes: wide
---

### Problem 1
**If we have $n$ dice draws with a dice that has $k$ sides. Let $X_i$ to be the random variables that describes the number of times that the dice faces $i$.  What is the correlation between $x_i$ and $x_j$ for $i\neq j$**.

We first notice, $X_i$ are identitically distributed. Thus, the correlation between $X_i$ and $X_j$ does depend on $i$ and $j$ and they they have the same variance. Thus, we only need to calculate covariance first. We then notice

$$
X_1+X_2 + \dots + X_k = n
$$

Next we compute

$$
\begin{aligned}
&\text{Cov}[X_i, X_1+X_2+\dots + X_k] = \text{Cov}[X_i, n] =0 \\
&=\text{Cov}(X_i, X_i) + (k-1)\text{Cov}(x_i,x_j)\\
\end{aligned}
$$

Thus, we find 

$$
(k-1)\text{Cov}(x_i,x_j) = - \text{Var}(X_i)
$$

Thus,

$$
\text{Cov}(x_i,x_j) = - \frac{\text{Var}(x_i)}{k-1}
$$

Therefore, the correlation becomes 

$$
\text{Corr}(X_i,X_j) = \frac{\text{Cov}(X_i,X_j)}{\text{Var}(X_i)} = - \frac{1}{k-1} 
$$


### Problem 2

**With a set of 52 cards, we draw without replacement from the card. What is the expected number of draws to see the first Ace?**

Counting down from the top of the deck of cards. Let $X_1$ be the number of cards before the first Ace. Let $X_2$ be the number of cards between the first and the second Ace. Let $X_3$ be the number of cards between the second and third Ace. Let $X_4$ be the number of cards between the third Ace and the fourth Ace. Finally, let $X_5$ be the number of cards between the fourth Ace and the bottom of the deck. We find 

$$
X_1+X_2+X_3+X_4+X_5 = 52-4 = 48
$$

We also find the distribution of $X_i$'s are the same and thus, 

$$
5E[X_1] = 48\quad \Rightarrow \quad E[X_1] = \frac{48}{5}
$$

### Problem 3

**A 2D random walk starts from $(1,1)$. If it will stop once it hits the $y$-axis. What is the probability that it will stop at the negative part of the $y$-axis?**

![image](/assets/images/stats_posts/randomwalk.png)

Notice the symmetry of the problem. In 2D random walk, the problem is symmetric. At a given time, it will be uniformly distributed in the direction respect to the starting point. Given it hits $y$-axis, it will be uniformly distributed around within the angle ($0$,$\pi$) with respect to the starting point. However, the probability of going to the negative part is the last $\pi/4$ angle. Thus, the probability of landing in the negative part of $y$-axis is $1/4$. 




### Problem 4

**Give an example that two random variables are uncorrelated but dependent**

Let $X = \sin(\tau)$ and $Y = \cos(\tau)$ and $\tau\sim U(0,2\pi)$. This is uncorrelate becuase, if we plot $(X,Y)$, it relys on the unit circle. If we run a linear regression on that, the line will have zero slope. Since correlation between $Y$ and $X$ is the $R^2$ score and it is zero in this case. They are dependent because, once we know $X$, $Y$ can only have at most two values. 

### Problem 5

**How to uniformly generate points on a disc with radiu $R$?** 

If we label points by $(r,\theta)$, the probability density function of $(r,\theta)$ is 

$$
p(r,\theta)drd\theta = \frac{rd\theta dr }{\pi R^2} = \frac{d\theta}{2\pi} \cdot \frac{d r^2}{R^2} = p(\theta) p(r^2)
$$

Thus, we uniformly generate $r^2$ in the interval $[0,R^2]$ and uniform generate $\theta$ from $[0,2\pi)$. 

